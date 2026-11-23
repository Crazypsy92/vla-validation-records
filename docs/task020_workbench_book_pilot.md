# Task 020 · Workbench 书本抓放闭环试点

Task 020 改为官方 `libero_10` Task 5 单任务试点。目标是把黑色书本 `black_book_1` 放进收纳盒后部 `desk_caddy_1_back_contain_region`。黄白杯是场景道具。正式种子为 201、202、203，分别使用官方初始状态索引 0、1、2。原本两任务方案的选题审计单独保留。 [Issue #4](https://github.com/Crazypsy92/vla-validation-records/issues/4)

## 从 Workbench 运行

在 Windows 桌面打开 **VLA Workbench**，进入 **Task 5 / 书本试点**，选择种子与正式或冒烟模式，点击 **运行**。右侧显示书本任务的实时双视角和 Plan、Command、Feedback。点击 **停止** 后，后台在当前推理返回或当前控制步结束时保存并退出。历史列表包含正式和冒烟回合，可选回合后连续播放或拖动步号。

自动化验证使用 Windows 主机上的 WSLg Workbench 窗口，调用与用户操作相同的运行和停止按钮。现有快捷方式的目标为 Workbench 的 `start.sh`。运行记录与截图均来自实际窗口和仿真反馈。

## 数据和控制

- 使用 Task 017 完整回合的 `lerobot/xvla-libero` 本地权重和相同 Processor。每次前向保存两路 256×256 原始输入图像、8D 状态、输入指纹和后处理动作块。运行配置记录模型快照、权重和配置的 SHA-256、依赖版本及设备。
- 预检读取官方 BDDL，验证 reset、双相机、本体状态与 7D 绝对 OSC_POSE 步进。正式控制为 20 Hz，30 步动作队列执行完后使用新观测重新推理。回合在官方终止或 520 步官方评测上限结束。
- 每个动作步保存原始控制命令、OSC 目标、夹爪开度、书本世界坐标位姿、左右指垫与书本接触和其他夹爪碰撞几何体配对。书本抬升为当前 Z 减去复位 Z，沿用 2 cm 判定阈值。暂以闭合命令持续两步高于阈值作为保持代理指标，结合接触和轨迹复核。
- 在曾下发闭合之后，模型实际下发张开命令记为释放命令。开度达到 0.070 m、抓手与书本接触解除且书本在目标区域，记为实测释放。成功终止之后的队列尾部只记规划。官方 BDDL 成功采用独立字段。
- 原始双视角 MP4 以 20 FPS 保存，帧 0 对应复位，帧 k 对应第 k 步。原始记录和完整视频在本地归档。

## 执行结果

正式回合完成 **2/3**。两个获得官方终态的回合均成功，共 13 次模型前向和 352 个控制步。冒烟单独统计。

| 模式 | 种子 | 前向次数 | 控制步数 | 终止原因 | 平均前向耗时 | 峰值 RSS |
| --- | ---: | ---: | ---: | --- | ---: | ---: |
| smoke | 201 | 1 | 3 | gui_stop | 50.4 s | 6.42 GiB |
| formal | 201 | 6 | 169 | official_success | 36.0 s | 6.78 GiB |
| formal | 202 | 7 | 183 | official_success | 47.1 s | 6.74 GiB |

Seed 203 首次尝试在 150 步、5 次已完成前向后中断，原因未确认。重开 Workbench 后以相同种子、官方初始状态、权重和参数复位重试。重试在 120 步、4 次已完成前向后发生 WSL 全局 OOM，内核日志确认 Python 进程被终止。两次均无官方终态。原始控制日志、模型输出和未封装完成的 MP4 已保留，两个中断均未计为模型失败。
按 Issue 约定，确认 OOM 后停止正式试验。

| 种子 | 左指垫步数 | 右指垫步数 | 同步双侧接触步数 | 抬升峰值 | 已下发张开 | 实测释放 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| 201 | 97 | 102 | 97 | 28.56 cm | False | False |
| 202 | 108 | 109 | 108 | 27.76 cm | False | False |

夹爪闭合运动由逐步关节反馈复核。汇总在每一次闭合命令之后测量开度差，至少减少 1 mm 即记录为驱动响应。逐回合原始摘要里的 25 mm 近闭合标志保留在汇总的 `NEAR_CLOSED_25_MM` 字段，窄阈值以下可能受书本厚度限制。任一指垫接触算目标接触，双侧是否同时接触另计。

- Seed 201 最后一步开度 0.0295 m，左右指垫接触 True/True，末帧夹爪命令 +1。队列未执行尾部含张开指令 False，实测释放 False。
- Seed 202 最后一步开度 0.0296 m，左右指垫接触 True/True，末帧夹爪命令 +1。队列未执行尾部含张开指令 False，实测释放 False。

## 对照与验收

Task 017 双杯基线有 3/3 官方成功，共 24 次模型前向、664 个控制步。书本试点与双杯任务在场景、操作物体数量和目标区域上都有差异。两组成功率描述各自任务的观测结果。

| 验收项 | 结果 | 依据 |
| --- | --- | --- |
| T01 官方环境兼容 | PASS | 预检确认官方 BDDL、20 Hz、双 RGB、8D 状态和 7D OSC；正式前向、控制通过。 |
| T02 Workbench 入口 | PASS | 书本试点标签提供官方 Task 5、黑色书本、收纳盒后部与种子选择。 |
| T03 GUI 冒烟 | PASS | 种子 201 真实前向 1 次，执行 3 步，GUI 停止并保存。 |
| T04 三组完整回合 | BLOCKED | 种子 201、202 完成。种子 203 两次由 GUI 启动，重试遇到 WSL OOM，均无官方终态。 |
| T05 动作链 | PASS | 原始动作和后处理形状与有限值通过校验，逐步下发值和动作块一致。 |
| T06 接触与动作物理证据 | PASS | 逐步记录双侧指垫、其他夹爪接触、开度、书本位置与姿态。 |
| T07 释放证据 | PASS | 释放规划、实际张开指令和物理释放分别记录。 |
| T08 实时 GUI | PASS | 从实际 WSLg 窗口捕获仿真双视角和同一步反馈。 |
| T09 历史回放 | PARTIAL | 两个正式回合及冒烟回合在 Workbench 均从复位帧播放到终帧。种子 203 的 MP4 未封装完成。 |
| T10 归档和复现 | PARTIAL | 已完成回合的原始记录、配置、日志、图、视频元数据已归档，两个中断回合保留部分证据。 |

正式回合在 Windows 主机上的 WSLg Workbench 通过按钮回调触发。自动化驱动直接打开同一个 Workbench 窗口，另实际打开现有 Windows 快捷方式，确认成功出现 Workbench 窗口后关闭验证窗口。另用未达到官方成功且由 GUI 停止的冒烟记录核对历史回放。中断回合未形成可回放的完整视频。

环境预检、界面回归、历史回放与归档校验以 0 退出。初次 GUI 批次与 Seed 203 重试均以 1 退出。

```bash
DISPLAY=:0 HF_HUB_OFFLINE=1 MUJOCO_GL=egl .venv_xvla/bin/python -u workbench/tests/run_task020_desktop.py
DISPLAY=:0 HF_HUB_OFFLINE=1 MUJOCO_GL=egl .venv_xvla/bin/python -u workbench/tests/run_task020_desktop.py --formal-seed 203
DISPLAY=:0 .venv_xvla/bin/python workbench/tests/review_task020_history.py
.venv_xvla/bin/python scripts/task020_collect_book_pilot.py
DISPLAY=:0 .venv_xvla/bin/python -m unittest workbench.tests.test_ui_headless -v
```

- [验收矩阵](../results/task020/acceptance.json)
- [回合统计及视频元数据](../results/task020/metrics/summary.json)
- [桌面历史回放验证](../results/task020/metrics/book_pilot_history.json)
- [模型与控制配置](../results/task020/metrics/book_pilot_configuration.json)
- [Workbench 截图](../evidence/task020/)
