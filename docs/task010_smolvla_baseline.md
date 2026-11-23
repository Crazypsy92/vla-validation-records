# Task 010：SmolVLA 预训练模型与真实动作输出验证基准报告

## 一、任务背景与实验目标

在 Task 001～009 中，我们基于 llama.cpp 本地 CPU 推理引擎与 Python 上位机，完成了 Qwen3-0.6B（LLM）与 SmolVLM2-2.2B（VLM）的基础推理、流式通信、模型热切换以及视觉状态到离散动作语义的基线验证。在 Task 009 中，模型输出的是离散动作语义（如 `{"action": "pick", "target_object": "blue_block"}`），而非机器人执行机构所需的连续低层控制指令。

**Task 010 目标**：
在现有 WSL2 Ubuntu 24.04 CPU 环境中，构建完全独立的实验工程 `vla-learning/`，复现 Hugging Face 官方具身基础模型 **SmolVLA**（`lerobot/smolvla_base`），验证真实的“**多视角视觉观测 + 任务自然语言指令 + 机器人本体状态 → SmolVLA Flow Matching 推理 → 连续动作块（Action Chunk）预测**”全流程。

实验遵循以下原则：
1. **完全独立**：在独立 Python venv（`vla-learning/.venv`）中安装 LeRobot 与 PyTorch CPU 版，与 llama.cpp 及原有上位机环境物理隔离；
2. **纯真实验**：真实调用官方 `SmolVLAPolicy` 与 Flow Matching 采样生成动作，不使用随机数或数据集 Ground Truth 伪造动作；
3. **安全受控**：离线加载权重，控制推理内存峰值在可用 RAM（7.6 GB）内，严防 OOM 与 Swap 颠簸。

---

## 二、执行环境与依赖基准

### 1. 硬件与操作系统
- **宿主机环境**：Windows 10 / WSL2 Linux 6.18.54.1-microsoft-standard-WSL2 (Ubuntu 24.04 LTS)
- **CPU**：12th Gen Intel(R) Core(TM) i7-1255U（12 vCPUs，物理 6 核）
- **系统内存**：RAM 7.62 GB，空闲可用 ~5.74 GB；Swap 2.00 GB
- **磁盘可用空间**：926.2 GB（存储极充裕）
- **网络代理**：本地 Windows 代理端口 `http://172.17.240.1:7897`

### 2. 软件与核心库版本
- **Python**：3.12.3
- **PyTorch**：2.15.0+cpu（官方 CPU-only 构建版）
- **torchvision**：0.29.2+cpu
- **lerobot**：0.7.0
- **transformers**：5.22.2
- **accelerate**：1.16.0
- **datasets**：5.2.0
- **av**：15.1.0（严格适配 LeRobot 对 PyAV 选项接口的约束）
- **pandas**：2.3.3

---

## 三、SmolVLA 模型结构与配置参数

| 配置项 | 参数值 / 规范 | 说明 |
| :--- | :--- | :--- |
| **Model ID** | `lerobot/smolvla_base` | Hugging Face 官方 SmolVLA 预训练基座权重 |
| **Base VLM** | `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` | 轻量多模态视频指令大模型底座 |
| **VLM 层数剪裁** | 16 层（原 SmolVLM2 结构适配） | 适配机器人高频推理与跨模态特征提取 |
| **参数规模** | ~450M 参数 | 权重文件 `model.safetensors` 实际占用 900.5 MB |
| **视觉输入规格** | 3 路多视角相机 (`camera1`, `camera2`, `camera3`) | 每路输入张量为 `(3, 256, 256)`，自动填充并缩放到 `[512, 512]` 处理 |
| **状态输入 (State)** | 6 维浮点向量 (`observation.state`) | 对应 SO-100 机械臂 6 个驱动关节/驱动器位置 |
| **任务指令 (Task)** | 自然语言指令字符串 | Tokenizer 最大序列长度 48 tokens，右侧 Padding |
| **动作生成目标** | 流式匹配（Flow Matching）连续动作扩散 | 设定 10 步采样更新（Euler/Flow Steps） |
| **Action Chunk 大小** | `chunk_size = 50`, `n_action_steps = 50` | 单次前向推理生成未来 50 个连续控制步长 |
| **动作输出维度** | 6 自由度 (`action` shape: `[50, 6]`) | 对应 6 个执行器（5 个臂关节 + 1 个夹爪）在未/已反归一化物理值 |

---

## 四、真实推理测试与实验指标

我们在 `task010_smolvla_inference.py` 中设定了 3 组具有典型代表性的机器人作业场景，每组场景包含多视角合成相机图像、真实的 SO-100 初始关节状态、以及自然语言任务指令：

1. **Case 001**：`case_001_pick_blue_block`
   - 指令："pick the blue block and place it on the plate"
   - 初始状态：`[1.59, 119.94, 109.76, 56.70, -27.42, 12.00]`（接近中立巡航姿态）
2. **Case 002**：`case_002_approach_red_cylinder`
   - 指令："move the gripper forward towards the red cylinder"
   - 初始状态：`[2.43, 124.93, 123.55, 66.99, -103.87, 2.89]`（高位俯视逼近姿态）
3. **Case 003**：`case_003_open_gripper_release`
   - 指令："open the gripper and release the target object"
   - 初始状态：`[1.42, 125.72, 125.41, 63.78, -106.54, 3.34]`（抓取后到位悬停待释放姿态）

### 实测性能数据表

| 测试用例 ID | 任务指令概要 | 预处理耗时 (ms) | 模型推理耗时 (s) | 后处理耗时 (ms) | 动作 Chunk 形状 | 步长 0 动作向量 | 步长 49 动作向量 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Case 001** | pick blue block | 3.03 ms | **42.655 s** | 0.08 ms | `[1, 50, 6]` | `[-0.316, 0.214, -0.597, 0.125, 2.102, -0.690]` | `[0.037, 1.177, 2.636, -0.227, 2.306, -0.302]` |
| **Case 002** | approach red cylinder | 0.76 ms | **40.946 s** | 0.06 ms | `[1, 50, 6]` | `[-0.456, 0.742, 1.943, -0.165, 2.016, -0.621]` | `[-1.063, 1.331, 3.141, -0.059, 3.023, 0.975]` |
| **Case 003** | open gripper release | 0.73 ms | **41.207 s** | 0.06 ms | `[1, 50, 6]` | `[0.594, 0.390, 1.298, -0.354, 0.958, 0.983]` | `[-0.276, 1.420, 3.039, -0.113, 2.302, 0.023]` |

### 系统资源基准

- **初始内存 RSS**：246.70 MB
- **模型加载后内存 RSS**：1475.80 MB（纯模型及预处理器净增量 1229.09 MB ~ 1.23 GB）
- **推理期内存峰值 RSS**：~1680 MB（增量约 200 MB，占系统可用 RAM 的 22%）
- **模型本地加载耗时**：6.41 s
- **预处理初始化耗时**：0.22 s
- **单次 Chunk 平均推理耗时**：**41.603 s**（Flow Matching 10 步采样）
- **单步动作等效周期**：单次生成 50 步动作耗时 41.6 秒，折合单步动作生成耗时约 0.832 秒（等效 1.20 Hz）

---

## 五、核心问题答复

### 1. SmolVLA 预训练模型的架构组成与参数规模是多少？底座 VLM 是什么？
- **架构组成**：SmolVLA 采用轻量化视觉语言动作（VLA）复合架构，核心包含三部分：
  1. **多模态 VLM 底座**：负责将多路相机视觉 Token 与任务语言 Token 进行交叉融合编码；
  2. **机器人状态投影层（State Projector）**：将 6 维本体关节状态投影对齐至统一特征空间；
  3. **基于流匹配的动作专家解码器（Flow-Matching Action Expert Decoder）**：利用去噪流匹配机制逐步生成连续动作序列。
- **参数规模**：总参数量约 **450M（4.5 亿参数）**，权重文件 `model.safetensors` 大小约为 **900.5 MB**。
- **底座 VLM**：官方采用 **`HuggingFaceTB/SmolVLM2-500M-Video-Instruct`**，并在策略加载阶段将其 VLM 层数裁剪配置为 16 层。

### 2. 模型的输入观测结构是什么？支持多少路图像？分辨率是多少？机器人本体状态 State 的维度与含义是什么？
- **图像输入**：官方预训练模型默认配置支持 **3 路相机图像**（`observation.images.camera1`，`camera2`，`camera3`），输入分辨率为 `[3, 256, 256]`（RGB），并在预处理器中填充缩放至 `[512, 512]` 输入 VLM。
- **本体状态（State）**：维度为 **6 维**（`observation.state`: `shape=[6]`），在 LeRobot SO-100 典型配置下，对应机械臂 6 个执行机构驱动器（底座旋转、肩部、肘部、手腕俯仰、手腕旋转、夹爪开合度）的物理位置。
- **任务指令**：自然语言字符串，经由 Tokenizer 处理为形状 `[1, 48]` 的整数 Token 序列与布尔 Attention Mask。

### 3. 输入预处理流水线（Preprocessor Pipeline）包含哪些具体步骤？
预处理流水线由 `make_smolvla_pre_post_processors` 组装，严格执行 6 步转换：
1. **`rename_observations_processor`**：根据策略配置映射相机与状态命名；
2. **`to_batch_processor`**：将单帧输入张量扩充 Batch 维度（例如从 `[3, 256, 256]` 变为 `[1, 3, 256, 256]`）；
3. **`smolvla_new_line_processor`**：格式化多模态文本前缀，插入视觉与指令分隔符；
4. **`tokenizer_processor`**：使用 SmolVLM2 分词器将任务指令文本编码为 48 长度的固定 Token 序列并右侧补齐（Right Padding）；
5. **`device_processor`**：将张量移送至目标计算设备（本实验强制覆盖为 CPU）；
6. **`normalizer_processor`**：读取 `policy_preprocessor_step_5_normalizer_processor.safetensors` 中的预计算统计均值与方差，对 `observation.state` 执行标准化 $(x - \mu) / \sigma$，视觉张量保持 Identity。

### 4. 模型输出的 Action Chunk 结构是什么？包含多少个步长（Horizon）？每个步长包含几个维度的动作？动作的数值范围与物理含义是什么？
- **输出张量形状**：`[1, 50, 6]`（Batch Size=1，Horizon=50，Action Dim=6）。
- **时间步长（Horizon）**：**50 个步长**（`chunk_size=50`, `n_action_steps=50`）。在 10 Hz 控制频率下，单次 Chunk 预测覆盖未来 **5.0 秒**的连续轨迹。
- **动作维度**：每个时间步长包含 **6 维连续浮点动作**。
- **物理含义与数值范围**：
  - 经由 `unnormalizer_processor` 后，动作值代表 6 个电机的目标控制量（5 个手臂关节目标弧度/角度及夹爪开合目标量）。
  - 在归一化空间中动作值分布在 $[-3.0, +3.0]$ 区间；经反归一化还原后对应物理量程。实测 50 步轨迹呈现平滑连续的动态演进趋势，如夹爪从收缩（负值）到逐步张开（正值）。

### 5. 流式匹配（Flow Matching）在 SmolVLA 中的作用是什么？推理时经历了几个采样步数？单步推理与整块 Chunk 生成的计算关系是什么？
- **核心作用**：机械臂多模态模仿学习具有多峰分布特征（Multimodal Action Distribution，例如抓取物体可从左侧逼近或从右侧逼近）。传统回归模型容易出现“多峰平均”导致崩溃。Flow Matching 借鉴连续时间生成模型，通过学习常微分方程（ODE）向量场，从高斯噪声直接流动采样生成高质量的动作轨迹。
- **采样步数**：预训练模型配置为 **10 步**采样（`num_steps=10`）。
- **计算关系**：**Action Chunk 是整块一体化生成的**。单次 Flow Matching 的 10 次迭代同时生成全部 50 个时间步的动作矩阵 `[1, 50, 6]`，而非自回归一步步生成。在闭环控制（`select_action`）时，系统维护一个内部队列 `_action_queue`，在后续 50 帧中依次出队，每 50 步重新触发一次 Flow Matching 推理。

### 6. 在当前 WSL2 CPU 环境下，模型的加载时间、运行时内存峰值（RSS）与单次 Chunk 推理耗时分别是多少？当前 CPU 推理速度能否支撑实时闭环控制？为什么？
- **实测数据**：
  - 本地缓存加载时间：**6.41 秒**
  - 模型运行时内存峰值（RSS）：**1475.80 MB（~1.48 GB）**，推理过程动态增加 ~200 MB
  - 单次 Chunk 推理耗时：**40.9 ~ 42.6 秒（平均 41.6 秒）**
- **能否支撑实时闭环控制**：
  - **结论：无法直接支撑高频闭环控制**。
  - **原因**：50 步动作在 10 Hz 真实机器人执行下仅需 5.0 秒即可耗尽，但当前纯 CPU 下生成 50 步动作需耗时 41.6 秒。如果采用 Receding Horizon 实时重新规划，延迟超过 40 秒会导致机器人长时间停顿等待，无法应对动态扰动。
  - **实用优化路径**：
    1. 迁移到 NVIDIA GPU / 边缘 NPU（例如 Jetson Orin 或 RTX 显卡），利用 bfloat16/int8 量化与 TensorRT，推理耗时可从 41 秒骤降至 50~100 毫秒，轻松达到 10~20 Hz 实时闭环；
    2. 或缩减 Flow Matching 步数（如从 10 步减至 3~4 步）或采用异步动作块缓存（RTC，Real-Time Chunking）流水线。

### 7. SmolVLA 生成的底层连续动作 Chunk 与 Task 009 中生成的 LLM/VLM 高层离散动作语义（JSON）有何本质区别？
- 详见后文《VLA 输入输出全流程与分层架构分析报告》（`vla_input_output_analysis.md`），主要差异如下：
  1. **输入表达**：Task 009 依赖离散结构化检测框与属性描述；SmolVLA 直接摄取原始多路多视角图像像素与连续关节编码。
  2. **输出形式**：Task 009 输出单一离散动词与参数（如 `{"action": "pick"}`）；SmolVLA 输出 50 步 6 维高频微秒级连续数值轨迹。
  3. **计算目标**：Task 009 是离散符号语义推理与因果归因；SmolVLA 是非线性流匹配动作流场拟合。
  4. **时效性与频次**：高层语义决策执行频率为 0.1~0.5 Hz；底层 VLA 动作 Chunk 消耗频率为 10~50 Hz。

### 8. 如果在机器人系统中同时引入“Task 009 高层语义决策”与“Task 010 底层连续动作执行”，应该如何设计两者之间的分层协作架构？
- 采用 **分层分频架构（Hierarchical Asynchronous Dual-Rate Architecture）**：
  - **慢循环（Slow Loop，0.1~0.5 Hz）**：Task 009 高层决策智能体（LLM/VLM）负责全局场景理解、障碍物关系推理、任务拆解与子目标生成，输出结构化自然语言目标（如 `"align gripper with blue block"`）；
  - **快循环（Fast Loop，10~50 Hz）**：Task 010 底层 VLA（SmolVLA）负责接收慢循环发布的当前子目标、实时多视角视频流及自身关节状态，连续生成 50 步 Action Chunk，并由低层控制器执行插值与阻抗跟踪；
  - **反馈与异常中断**：快循环监测抓取力矩与接触传感器；一旦发生打滑、碰撞或超出动作范围，快循环立即停止并向慢循环抛出重规划事件。

---

## 六、交付物清单

1. **执行脚本**：`vla-learning/scripts/task010_smolvla_inference.py`
2. **基准报告**：`vla-learning/docs/task010_smolvla_baseline.md`
3. **深度分析**：`vla-learning/docs/vla_input_output_analysis.md`
4. **预测样本**：
   - `vla-learning/results/task010/predictions/case_001_pick_blue_block.json`
   - `vla-learning/results/task010/predictions/case_002_approach_red_cylinder.json`
   - `vla-learning/results/task010/predictions/case_003_open_gripper_release.json`
5. **性能指标**：`vla-learning/results/task010/metrics/inference_metrics.json`
6. **运行日志**：`vla-learning/results/task010/logs/task010_run.log`
7. **验收结论**：`vla-learning/results/task010/acceptance.json`
