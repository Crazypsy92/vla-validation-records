# Task021 · LIBERO Task 5 初始状态泛化验证

**阶段 B2a 待审核。** 本轮只尝试官方 index 15 / Reset RNG Seed 201，结果为 **OFFICIAL_SUCCESS**。index 34 未运行。

## 阶段 B2a · index 15 正式回合

从 Windows 桌面 Workbench 以显式参数发起唯一 Attempt b2a_index_15_rng_201_1795493022081788638，使用 LIBERO-10 Task 5。模型在 CPU 上运行，配置文件与 Task020 Phase 3 完全一致。模型权重、revision、Processor 文件、Prompt、原 8D 输入、7D 绝对 OSC_POSE、20 Hz、30 步动作块、BDDL 和 520 步上限均未变。

首次前向前，Worker 核对实际官方 index 与 RNG Seed，校验官方行及资产 SHA256、书本和目标位姿、机器人状态和两路 RGB 像素哈希。数值容差沿用 1e-7。前向前的核验证据保存在 Reset 事件。每轮使用前一块执行后的新观测。实跑 Step 0 的预览等待首张实时 JPEG，先看到的是占位图。前向前的两张原始 PNG 已保存且校验通过。事后修复界面优先显示同一步的 PNG，并用本回合存档复核，不重新运行模型。

| Chunk | 推理输入步 | 实际动作步 | 前向耗时（秒） |
| --- | ---: | ---: | ---: |
| 0 | 0 | 30 | 45.3155 |
| 1 | 30 | 30 | 32.3979 |
| 2 | 60 | 30 | 37.1533 |
| 3 | 90 | 30 | 35.1262 |
| 4 | 120 | 30 | 36.5686 |
| 5 | 150 | 30 | 31.6819 |
| 6 | 180 | 21 | 30.6051 |

共 7 次推理，201 步。终止原因 official_success，官方成功记录为 True。首次闭爪 Step 46，双侧指垫首次接触 Step 54，最高抬升 0.2882842796551591 m，首次到目标区域 Step 201，物理释放验证为 False。官方终态和释放分别记录。录像 202 帧，20 fps，SHA256 58437bc17908ae25067c74e256f084d733d44399c7273e899425f3b9574329e3，原始视频保存在本机。

| 内存采样 | WSL 可用 MiB | Swap 可用 MiB |
| --- | ---: | ---: |
| GUI 启动门禁 | 6479 | 2048 |
| 实测最低值（各自独立） | 1099 | 1341 |
| worker_exit | 6779 | 1639 |
| idle_12_seconds | 6798 | 1640 |

Worker RSS/PSS 采样峰值 6474/6468 MiB，Worker 退出码 0。保留 RAM/Swap 原门禁和每次新动作块的保护；新 OOM 计数变动标志为 False。外部采样器接入时模型 Worker 已由 Workbench 启动，启动前余量取自保存的 GUI 门禁样本。正式回合结束后，GUI 关闭核验为 True。

19 项回归通过，逐步证据校验退出码 0。290 个 Task020 历史文件 SHA256 一致。本轮未重试，未启动 index 34。

[正式回合验收](../results/task021/acceptance.json) · [逐块、资源与视频指标](../results/task021/b2a/metrics/summary.json) · [正式启动确认](../evidence/task021/b2a/confirmation.png) · [窗口结束状态](../evidence/task021/b2a/finished.png) · [Reset 画面显示复核](../evidence/task021/b2a/reset_display_check.png)

## 阶段 B1 · 显式 index 与无模型复位

从 Windows 桌面快捷方式打开现有 Workbench。Task 5 界面分别选择官方 index 15 和 34，Reset RNG Seed 固定为 201，通过「仅复位」按钮串行启动两个 Worker。

| 实际 index | RNG Seed | Run ID | 位姿和 8D 最大绝对差 | 双视角 RGB | 退出码 |
| --- | --- | --- | --- | --- | --- |
| 15 | 201 | reset_index_15_rng_201_1795491280237605745 | 0 | 双视角像素一致 | 0 |
| 34 | 201 | reset_index_34_rng_201_1795491421389679840 | 0 | 双视角像素一致 | 0 |

每次复位前校验工厂游标与官方状态行，复位后核对游标增量。资产及状态行 SHA256 均与阶段 A 一致。书本和目标后格位姿、目标半尺寸、末端及关节反馈、夹爪和 8D 状态在绝对容差 1e-7 下比对，最大误差均为 0。两个视角的 RGB 像素哈希均匹配阶段 A，另存 PNG 文件哈希。

旧入口保留 201→0、202→1、203→2。显式 index 和 RNG Seed 独立传递给 Worker。现阶段显式选择只允许用于复位入口。正式运行参数、模型、控制、Processor 和资源保护保持原样。

index 15 实跑原窗口底部裁切了部分哈希。已将完整证据区移至相机上方，index 34 实跑验证了新位置；index 15 用真实存档记录复核完整显示，未再次复位。

两个 Worker 均退出并回收。未下载或加载 X-VLA 权重，0 次前向、0 个正式回合。17 项回归通过，包含 6 项 B1 专项，两个校验命令退出码均为 0。290 个 Task020 历史文件 SHA256 保持一致。修改源码和 source.diff 留在本地工作区。

[阶段 B1 指标](../results/task021/b1/metrics/summary.json) · [验收记录](../results/task021/acceptance.json) · [index 15 实跑](../evidence/task021/b1/index_15_result.png) · [index 15 显示复核](../evidence/task021/b1/index_15_display_check.png) · [index 34 实跑](../evidence/task021/b1/index_34_result.png) · [回归日志](../results/task021/b1/logs/regression.log)

## 阶段 A · 已验收的盘点与候选

**阶段 A 已接受，候选为 index 15 和 34。** 阶段 A 盘点时，旧 Workbench 只能选择 index 0、1、2。本轮实际执行官方复位及其内置的 10 步稳定过程。X-VLA 加载、推理及正式回合均为 0。

## 官方来源与映射

任务指令为 “pick up the book and place it in the back compartment of the caddy”。官方谓词为 In(black_book_1, desk_caddy_1_back_contain_region)。环境沿用绝对 OSC_POSE、20 Hz、7D 动作空间及 520 步上限。安装版本为 hf-libero 0.1.5、LeRobot 0.7.0、robosuite 1.4.0、MuJoCo 3.8.1。

实际加载文件为 libero_10/STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy.pruned_init，含 50×45 个 float64 元素，SHA256 为 6cd3937ba18d64e72223222af36888d26ea201840415adbc4dae590454d0a5a8。官方原始 .init 同目录存在，运行实际使用 .pruned_init。逐一复位 index 0–49，50 个原始状态行 SHA256 互异。稳定后的书本位姿去重计 50 种，双视角像素哈希对去重计 50 种。来源记录还包含 BDDL、官方包装器和 Workbench 源码指纹。 [来源与哈希](../results/task021/metrics/inventory_source.json)

| Workbench Seed | 官方 index | 对照 |
| --- | ---: | --- |
| 201 | 0 | Task020 官方成功，哈希、书本位置和 8D 与原始 Reset 一致 |
| 202 | 1 | Task020 官方成功，哈希、书本位置和 8D 与原始 Reset 一致 |
| 203 | 2 | Phase 4 资源中断，初始状态哈希一致，无官方终态 |
| 204、205 | 无映射 | GUI 下拉没有该项，Worker 命令行枚举不接受 |

GUI 的 Seed 下拉和 Worker 的 SEEDS 均限定 201、202、203。Worker 以 SEEDS.index(seed) 选工厂下标，在 reset 前核对 init_state_id。官方 reset 先读选中的状态行，再将索引按工厂 stride 递增。此次先用 stride=1 遍历全表，再用独立官方工厂复核基线 0、1、2 和两个候选。候选诊断用固定随机 Seed 201，index 由官方工厂决定。两组复位的姿态与机器人反馈通过 1e-7 的绝对误差校验。 [Task020 结题](task020_goal_met_with_limitations.md) · [Seed 203 证据](task020_r1_phase4_seed203_results.md)

## 位姿与候选

全量 JSON 逐 index 保存书本、收纳盒和杯子的世界系位置及 WXYZ 朝向，后格目标 site 的位置、朝向和半尺寸，以及末端姿态、7 个臂关节、双指 qpos、8D 状态与双视角像素哈希。物体位置在 Reset 内置稳定过程之后采集。精选图左侧为 Workspace，右侧为 Wrist。 [50 个初始状态记录](../results/task021/metrics/initial_states.json) · [index 0](../evidence/task021/index_00_reset.jpg) · [index 1](../evidence/task021/index_01_reset.jpg) · [index 2](../evidence/task021/index_02_reset.jpg) · [index 15](../evidence/task021/index_15_reset.jpg) · [index 34](../evidence/task021/index_34_reset.jpg)

| index | 书本 XYZ（m） | 目标后格 site XYZ（m） | 末端 XYZ（m） |
| --- | --- | --- | --- |
| 0 | (-0.21013, 0.16371, 0.88296) | (-0.43908, -0.14465, 0.97258) | (-0.29742, 0.01291, 1.17415) |
| 1 | (-0.18580, 0.14321, 0.88296) | (-0.43486, -0.14762, 0.97258) | (-0.30189, 0.00232, 1.18006) |
| 2 | (-0.19308, 0.14683, 0.88296) | (-0.43091, -0.13359, 0.97258) | (-0.30648, 0.00369, 1.15887) |
| 15 | (-0.22475, 0.13070, 0.88296) | (-0.43908, -0.14465, 0.97258) | (-0.31215, 0.01038, 1.15863) |
| 34 | (-0.19780, 0.12984, 0.88296) | (-0.43908, -0.14465, 0.97258) | (-0.30144, -0.01152, 1.18190) |

先排除 index 0、1、2。第一遍复位发现 2 mm 的初筛会排除全部新状态，因此按候选到两个基线的最远目标位置差排序，保留最接近的至少两个状态及并列者。实测门槛约 5.16 mm，共 47 个状态。在这些状态中，首选与较近基线仍有最大书本 XY 差的状态。另选一个与较近基线仍有最大书本旋转差的状态。旋转差采用 SO(3) 最小转角，世界 Z 朝向差使用书本局部 X 轴在 XY 平面的投影。

| 候选 index | 基线 index | 书本 XY 差（cm） | 书本旋转差（°） | 朝向差（°） | 目标位置差（mm） | 目标旋转差（°） | 末端差（cm） | 杯子位置差（cm） |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 15 | 0 | 3.61 | 40.10 | 40.10 | 0.00 | 0.000 | 2.16 | 2.69 |
| 15 | 1 | 4.09 | 37.19 | 37.19 | 5.16 | 0.000 | 2.51 | 2.31 |
| 34 | 0 | 3.60 | 40.17 | 40.17 | 0.00 | 0.000 | 2.59 | 1.30 |
| 34 | 1 | 1.80 | 37.25 | 37.25 | 5.16 | 0.000 | 1.40 | 4.67 |

已检查 index 3 的最小书本 XY 差为 3.04 cm，最小旋转差为 19.12°；index 4 的最小书本 XY 差为 1.33 cm，最小旋转差为 4.46°。表中的目标、机器人和杯子变化属于伴随变量，后续结果限于这些官方初始状态。 [候选比较及独立复位](../results/task021/metrics/summary.json)

### 同 index 更换诊断 Seed

下表三组均使用相同的官方状态行哈希。差异来自同一 index 下改变 reset 的 RNG Seed。以后若获准执行，可固定 RNG Seed 以减少这一伴随因素，并显式记录两者。

| index | 诊断 Seed | 书本位置差（mm） | 书本旋转差（°） | 目标位置差（mm） | 末端位置差（mm） |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | 202 → 201 | 0.000 | 0.000 | 5.156 | 0.000 |
| 15 | 201 → 202 | 0.000 | 0.000 | 5.156 | 0.000 |
| 34 | 201 → 202 | 0.000 | 0.000 | 5.156 | 0.000 |

## 阶段 A 记录的工程前置条件

待用户审核候选。若继续，最小工程变更是让 GUI 与 Worker 显式选择并校验原有官方索引，在首次前向前记录实际 index、初始状态行与资产哈希和双视角。模型、Processor、动作语义、控制和资源保护应继续沿用。本轮未修改 Workbench 或资源门禁。

| ID | 状态 | 依据 |
| --- | --- | --- |
| G21-01 | PASS | 50 个官方状态逐一复位，已核对实际文件、哈希及现有 Seed 映射。 |
| G21-02 | PASS | 候选 15 和 34 均未用于 Task020，且相对成功基线的差异可量化。 |
| G21-03 | NOT_RUN | 仅核验模拟控制接口和环境配置，未执行正式模型。 |
| G21-04 | NOT_RUN | 已在独立官方工厂诊断复位，未创建正式 GUI Attempt。 |
| G21-05 | NOT_RUN | 本轮无模型推理及任务终态。 |
| G21-06 | NOT_RUN | 未启动正式 Worker，现有资源保护源码哈希不变。 |
| G21-07 | PARTIAL | 保存了初始位姿、观测、候选和复位交叉核对，正式逐步数据及视频待后续。 |
| G21-08 | PASS | 290 个本机 Task020 历史文件与原 SHA256 一致。 |

本机复现命令为 MUJOCO_GL=egl HF_HUB_OFFLINE=1 .venv_xvla/bin/python -u results/task021/phase_a_inventory.py，退出码 0。完整原图、诊断脚本和日志保存在本机结果目录。 [验收 JSON](../results/task021/acceptance.json)
