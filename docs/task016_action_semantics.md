# Task 016：X-VLA 动作语义与映射关系深度审计规范

## 一、审计背景与目标

在 Task 015 独立桌面上位机（VLA Workbench）开发完成后，本规范对上位机中展示的动作张量维度、物理语义、参考坐标系以及与 LIBERO 数据集专家动作的映射关系进行系统性、源码级的严格核验。

核心澄清两项工程事实：
1. **模型输出的位置与姿态是绝对目标还是增量？**
2. **旋转向量的具体数学形式是欧拉角还是轴角向量？夹爪正负符号的具体物理开合含义是什么？**

---

## 二、源码级映射依据与处理链全景

### 2.1 LeRobot 官方后处理器规范

在 Hugging Face LeRobot 官方实现（`lerobot/policies/xvla/processor_xvla.py`）中，核心后处理类为 `XVLARotation6DToAxisAngleProcessorStep`：

```python
class XVLARotation6DToAxisAngleProcessorStep(ProcessorStep):
    """Convert 6D rotation representation to axis-angle and reorganize action dimensions.

    This processor step takes actions with 6D rotation representation and converts them to
    axis-angle representation, reorganizing the action dimensions as:
    - action[:, :3] -> target_eef (end-effector position)
    - action[:, 3:9] -> 6D rotation (converted to axis-angle, 3D)
    - action[:, 9:10] -> gripper action

    Final output: [target_eef (3), axis_angle (3), gripper (1)] = 7D action, in float32 as the environment takes it.
    """
    expected_action_dim: int = 10

    def __call__(self, transition: EnvTransition) -> EnvTransition:
        action_np = action.cpu().float().numpy()

        target_eef = action_np[:, :3]               # (B, 3) 末端绝对目标位置
        rotation_6d = action_np[:, 3:9]             # (B, 6) 连续正交 6D 旋转
        target_act = action_np[:, 9:10]             # (B, 1) 夹爪连续 Logit

        target_axis = rotate6d_to_axis_angle(rotation_6d)  # (B, 3) 恢复为 3D 轴角旋转向量

        action_np = np.concatenate([target_eef, target_axis, target_act], axis=-1)
        action_np[:, -1] = np.where(action_np[:, -1] > 0.5, 1.0, -1.0) # 二值化夹爪

        return new_transition
```

### 2.2 原始 20D 专家输出与 7D 动作映射表

| 原始 20D 索引 | 7D 动作索引 | 物理维度名称 | 物理单位 | 参考坐标系 | 数学与物理本质定义 |
| :---: | :---: | :--- | :---: | :--- | :--- |
| `0` | `0` | **`target_x`** | 米 (m) | Robot Base Frame (基座系) | 末端执行器在基座坐标系下的绝对目标位置 $X$ 坐标 |
| `1` | `1` | **`target_y`** | 米 (m) | Robot Base Frame (基座系) | 末端执行器在基座坐标系下的绝对目标位置 $Y$ 坐标 |
| `2` | `2` | **`target_z`** | 米 (m) | Robot Base Frame (基座系) | 末端执行器在基座坐标系下的绝对目标位置 $Z$ 坐标 (LIBERO 台面高度约 0.65m) |
| `3:9` | `3:6` | **`rot_axis_{x,y,z}`** | 弧度 (rad) | Controller Frame (控制器系) | 6D 正交基恢复后的 3D 轴角向量 $\mathbf{v} = \theta \cdot \mathbf{u}$，$\|\mathbf{v}\| \in [0, \pi]$ |
| `9` | `6` | **`gripper`** | 状态值 | 动作二值化 | 夹爪二值控制量：$\le 0.5 \to -1.0$ (张开)；$> 0.5 \to +1.0$ (闭合) |
| `10:19`| -- | *Unused Arm 2* | -- | -- | X-VLA 双臂架构中为第二只机械臂预留的特征维度，在单臂 LIBERO 中置零丢弃 |

---

## 三、三大核心物理语义界定

### 3.1 位置语义：绝对目标位置 (Absolute Target EEF Position) vs 位移增量 (Delta Action)
- **事实依据**：
  在 LIBERO 任务中，机器人初始末端状态高度通常位于 $z \approx 0.655\,\text{m}$。X-VLA 模型输出的前三维数值稳定分布于 $[0.60, 0.70]\,\text{m}$。
- **误区警示**：
  过去如果将前三维误标为 $dx, dy, dz$，会给使用者造成「单步要向上或向下移动 0.65 米」的致命误解。实际上，模型输出的是 Operational Space Controller (OSC) 的**绝对目标位姿（Commanded Pose）**。如果环境控制器支持位移增量，则必须通过 $\Delta \mathbf{p} = \mathbf{p}_{\text{target}} - \mathbf{p}_{\text{current}}$ 换算。

### 3.2 旋转语义：3D 轴角旋转向量 (Axis-Angle Vector) vs 欧拉角 (Euler Angles)
- **事实依据**：
  LeRobot 调用 `rotate6d_to_axis_angle`：
  $$\mathbf{R} = f_{\text{Gram-Schmidt}}(\mathbf{r}_{6d}) \in SO(3) \xrightarrow{\quad\text{Logarithmic Map}\quad} \mathbf{v} = \theta \mathbf{u} \in \mathbb{R}^3$$
  其中向量方向 $\mathbf{u}$ 为转轴单位矢量，模长 $\|\mathbf{v}\| = \theta$ 为绕该轴旋转的弧度角。
- **误区警示**：
  不可将三维分量标为 Roll / Pitch / Yaw。欧拉角涉及旋转顺序（如 Z-Y-X 或 X-Y-Z）且存在万向节死锁（Gimbal Lock），而轴角向量是无奇异性的紧凑旋转表示。

### 3.3 夹爪控制语义：$-1.0$（张开） vs $+1.0$（闭合）
- **事实依据**：
  在 `sample_manifest.json` 与 LIBERO 官方仿真器中，机械臂在初始接近物体阶段，夹爪处于完全张开状态，数据集专家动作标记为 `-1.0`。抓取闭合时标记为 `+1.0`。
- **阈值转换**：
  X-VLA 动作专家头输出连续 Logit，经门限 $> 0.5$ 判定为 $+1.0$（闭合），否则为 $-1.0$（张开）。

---

## 四、上位机可视化规范与坐标系标注

1. **时序曲线横坐标**：
   - 标注为 `Action Step Index (T0 ~ T29, 30-Step Horizon - NOT seconds/execution time)`。
   - 明确指出这 30 个点是模型在单次决策周期内预测的时序动作块（Action Chunk），步间间隔取决于底层控制频率（LIBERO 通常为 20Hz 即 50ms 一步），**横轴不是物理执行时间（秒）**。
2. **时序曲线纵坐标**：
   - 绝不允许未经说明地对动作数值进行伪缩放或平移。
   - 平移曲线纵轴单位：米（`m`），参考系为机器人基座绝对坐标系。
   - 旋转曲线纵轴单位：弧度（`rad`），参考系为 3D 轴角向量。
   - 夹爪曲线纵轴单位：状态值（`[-1.0, +1.0]`）。
3. **专家对比边界提示**：
   - 界面上与专家动作对比时，明确注明：**“LIBERO 数据集专家动作为归一化相对增量，模型预测为绝对目标位姿，二者不可直接计算数值 MAE，非同一量纲”**。
