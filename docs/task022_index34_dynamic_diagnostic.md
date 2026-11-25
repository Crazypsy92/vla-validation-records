# Task022-D index34 单次动态诊断回放

**300 步，10 次前向，Step150–300 覆盖 151/151。** 诊断运行结果为 `COMPLETE`，根因结论为 `ROOT_CAUSE_UNDETERMINED`。本回合用于诊断，未计入 LIBERO 官方成功率。

## 运行与历史对照

- Run ID 为 `dynamic_index34_rng201_1795578972038190503`，执行提交为 `c873467e434f102c94db3b3fdd52a8502512bab5`，依赖 PR #17 的精确提交为 `52c3e820482663502f0f95e92a3b1ae1a009cf89`。
- 依赖与配置核验通过。原始配置 SHA256 为 `9f63d96cd65cfc2d297efbe0d6fd6897bcc9a00dc3b0cf0658d8c895224980e7`，固定 checkpoint revision 为 `8e6aeef01f634f5d3b5be4340328f19cc2c25a65`。使用固定 CPU、原 Processor、双视角输入、8D→9D、20D→7D、absolute OSC_POSE、20 Hz 以及 30 步动作块。
- 模型加载完成 1 次，环境创建 1 次，Reset 1 次，重试 0 次。官方资产、状态、Prompt、BDDL 与两路 RGB 指纹逐项核对。Reset 内置 10 个稳定步保留，外层控制步从 Step 1 计数。
- Worker 退出码为 `0`，停止原因为 `diagnostic_step_300_limit`。本轮对照范围未见超过 2 mm 或 1° 的轨迹分叉。
- 20 帧输入图片和 10 个完整动作块已核验。逐步动作与模型 7D 输出、后处理及历史步记录可交叉核对。与历史执行动作的全维最大绝对差为 `0.0`；该数值混合平移、旋转和夹爪维度，仅用于回放一致性核对。
- 使用实际渲染的双视角关键帧和逐步日志归档，没有录制完整视频。

[执行命令](../results/task022/d/logs/execution/launch.json) · [退出记录](../results/task022/d/logs/execution/exit.json) · [基线指纹](../results/task022/d/logs/execution/baseline.json) · [前向与动作块](../results/task022/d/logs/execution/worker/chunks.jsonl) · [历史逐步对照](../results/task022/d/logs/execution/worker/reproduction.jsonl)

| Step | 书本位置误差 (mm) | 书本姿态误差 (°) | EEF 位置误差 (mm) | EEF 姿态误差 (°) |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 30 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 60 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 90 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 120 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 150 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 159 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 180 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 201 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 210 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 240 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 270 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 300 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

## B1–B4 动态证据

| 假设 | 支持程度 | 主要观察 |
| --- | --- | --- |
| B1 | NOT_SUPPORTED | 84/91 步的目标位姿在固定当步抓持变换的几何投影中可使书本中心进入官方边界。 |
| B2 | INCONCLUSIVE | 中位平移跟踪误差 25.75 mm。3775 次控制器调用中 0 个关节轴发生扭矩剪裁。 |
| B3 | SUPPORTED | 持续双侧接触和闭合命令下，相对 Step 210 的书本位姿变化达 28.16 mm、12.36°。 |
| B4 | SUPPORTED | 书本 geom 92 与隔板 geom 135 从 Step 171 到 300 连续 130 个控制边界接触。 |

### B1 策略目标 X 修正

Step 210–300 的动态 site 姿态每步读取，整个窗口中其位姿不变。按安装版本 `SiteObject.in_box` 计算，91/91 步实测书本 body 原点仅越过世界 X 上界 1.36–7.54 mm，重算谓词与官方状态一致。将 `book_in_eef` 转到 OSC grip-site 基后，按 `T_world_goal · T_grip_book` 投影，89/91 步给出负 X 修正，84/91 步的三轴点谓词均满足。例外为 Step 211、241–242、271–274，集中在动作块更新后。Step 240 的实际、投影 `book-in-site` 分别为 `[30.79, −4.45, −53.90]` 和 `[12.78, −18.85, −21.68]` mm。Step 300 的实际 X 仍超界 7.54 mm，投影在 X 上界内 12.75 mm。观测不支持“策略持续给出错误或不足的 X 修正”解释整个晚段。投影假定目标完全达到且抓持刚性，不衡量碰撞可行性，也无法单独排除策略的碰撞规划问题。字段见 `target_local_m`、`implied_book_at_goal_local_m` 和 `translation_only_still_above_upper_steps`。

### B2 跟踪差与控制限值

Step 150–300 的 `goal_feedback_error_m` 中位 25.75 mm、最大 55.46 mm（Step 180），换算到同一 grip-site 坐标基后的角度误差中位 1.14°、最大 3.14°。晚段 Step 270 的误差为 39.73 mm、1.98°。`torques.before_limit` 与 `after_limit` 在全部 3775 次记录中相同，执行器边界采样的 `actuator_ctrl` 和 `actuator_force` 一致。最近关节位置极限距离仍有 0.114 rad，没有观察到触及关节位置范围。实际跟踪差与指令未转化为书本负 X 位移同时出现，但数据不支持解释为扭矩剪裁或刚性关节止挡。`joint_constraint_force` 包含复合约束贡献，存在非零值。当前回合无法分离接触载荷、顺应/动态跟踪以及其他控制因素。

### B3 抓持相对位姿发生变化

Step 150–300 的 151/151 步均为闭合命令且双侧指垫接触。`book_in_eef` 经固定基转换后，相对 Step 210 的最大平移变化和最大转角都在 Step 274，分别为 28.16 mm、12.36°。Step 272 相邻步平移变化最大，为 3.55 mm。持续双侧接触不能证明书本在夹爪中刚性固定。证据支持相对运动，尚不能把全部变化分解为纯滑移、受力转动、滚动或指垫顺应，也不足以建立独立根因。

### B4 书本与隔板持续实际接触

`black_book_1_g1` 与 `desk_caddy_1_g2` 的原生 `contacts` 记录覆盖 Step 171–300，共 131 个接触点样本，130 个连续边界采样。按 Robosuite 的 geom 命名与资产 XML 顺序，`g2` 对应离线审计中的隔板。Step 171 最大法向力 115.97 N，signed distance −0.0586 mm，世界法向约 `[0, 0.00569, −0.99998]`。Step 210–300 的法向力范围为 14.68–57.97 N，末步为 55.56 N。窗口中未发现夹爪 geom 与盒体直接接触的边界样本。该接触法向的世界 X 分量始终近零，因此法向力本身不能证明存在直接的 X 硬阻挡。整步冲量与切向载荷没有经验证的数据，无法分离接触、摩擦及抓持变形对 X 残差的贡献。

## 采样与资源

控制边界频率为 20 Hz，MuJoCo 物理步长为 2 ms。窗口内记录 3775 次控制器调用。对关节扭矩使用实际返回值、剪裁后的值与原限值，执行器控制量、实际力、关节 qpos/qvel 和约束力从仿真读回。原始 EEF 位置取 grip_site，原始观测四元数取 right_hand body。两者的位置原点和旋转基定义分别保留在原始日志。离线分析读取安装的 Panda 夹爪 XML，将固定安装旋转应用到姿态和 book-in-EEF 变换后，才与 OSC grip_site 目标比较。原始日志的旋转误差角跨了两个坐标系，不用于 B1/B2 判读。用 301 条历史记录的控制器姿态矩阵交叉检查固定转换，跨子步采样的最大角差为 0.0504°。接触来源为每个控制步边界的 `mjData.contact`，持续样本数按连续控制边界计数，无法覆盖控制步之间的瞬时接触。活动接触的法向力来自 `mj_contactForce`；未激活约束的力、整步冲量、未验证的标量求解残差均标为 `UNAVAILABLE`，另记录约束数量和求解器迭代数。

资源门禁沿用 C1。启动前可用 RAM ≥1024 MiB，创建环境前 ≥512 MiB，Swap 只记录。模型加载耗时 110.54 秒，WSL 全局 OOM kill 计数变化为 `0`。退出后 WSL 可用 RAM 为 6560 MiB。原历史文件和控制源码保持原样。

| 指标 | 模型加载区间 | Worker 全程 |
| --- | ---: | ---: |
| Worker RSS 峰值 (MiB) | 6423.0 | 6423.0 |
| Worker PSS 峰值 (MiB) | 6421.0 | 6421.0 |
| 最低 WSL 可用 RAM (MiB) | 2736.0 | 314.0 |
| 最低 SwapFree (MiB) | 150.0 | 0.0 |
| Worker CPU 峰值（单核为 100%） | 589.2 | 649.7 |

[逐控制步遥测](../results/task022/d/logs/execution/worker/diagnostic.jsonl.gz) · [资源采样](../results/task022/d/logs/execution/worker/resources_supervisor.jsonl.gz) · [资源曲线](../evidence/task022/d/resource_lifecycle.png) · [轨迹、误差和接触](../evidence/task022/d/alignment_tracking_contacts.png) · [汇总 JSON](../results/task022/d/metrics/summary.json) · [验收 JSON](../results/task022/d/acceptance.json)

[Step 0 Workspace](../evidence/task022/d/0000_workspace.png) / [Wrist](../evidence/task022/d/0000_wrist.png) · [Step 150 Workspace](../evidence/task022/d/0150_workspace.png) / [Wrist](../evidence/task022/d/0150_wrist.png) · [Step 180 Workspace](../evidence/task022/d/0180_workspace.png) / [Wrist](../evidence/task022/d/0180_wrist.png) · [Step 210 Workspace](../evidence/task022/d/0210_workspace.png) / [Wrist](../evidence/task022/d/0210_wrist.png) · [Step 240 Workspace](../evidence/task022/d/0240_workspace.png) / [Wrist](../evidence/task022/d/0240_wrist.png) · [Step 300 Workspace](../evidence/task022/d/0300_workspace.png) / [Wrist](../evidence/task022/d/0300_wrist.png)
