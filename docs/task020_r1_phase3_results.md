# Task020-R1 Phase 3 · X-VLA 三动作块闭环与状态复验

在 Phase 2 的 `1f45f7f` 基础上，从 Windows 桌面快捷方式打开 VLA Workbench。使用 `lerobot/xvla-libero` CPU 检查点和 LIBERO-10 Task 5 Seed 201，在同一个 `phase3_seed_201` 短测中执行了三次真实前向、三个动作块和 90 个仿真步。GUI 停止后 Worker 退出码 0。验收 8 项 PASS，等待审核。官方任务终态未评估，Seed 203 未启动。

## 连续观测与控制

| Chunk | 仿真输入步 | 执行步 | 前向秒数 |
| --- | ---: | --- | ---: |
| 0 | 0 | 1–30 | 41.4525 |
| 1 | 30 | 31–60 | 38.2428 |
| 2 | 60 | 61–90 | 44.2686 |

每块用当前仿真的 Workspace 和 Wrist 各一张 256×256×3 图像和 8D 状态，沿用 9D Processor 输出与绝对 OSC_POSE。独立写入 Run ID、步号、Chunk 编号和单调时钟。验证脚本核对上一块末步与结束事件早于下一轮观测及前向，六张输入文件 SHA256 与记录相符，三轮 30×20 和 30×7 动作全部有限。逐条比较 Plan 和 Command，并核对 OSC 位置目标及 Feedback。

### 真实窗体验证

- 在 Step 30、60、90 的截图中，顶部阶段与底部运行步号对齐，Step 90 显示 `awaiting_stop`、前向 3 次、Chunk 2 Offset 29。Phase 2 的 Step 0 遗留问题在本次同阶段真实运行中未复现。
- 点击 GUI 停止后，从 Phase 3 短测历史条目播放 Step 0–90。图像、状态和命令跟随回放步更新。MP4 验证为 91 帧（含 Reset）、512×256、20 fps；SHA256 为 `8f9bf5c86b8a5b495a6db6760a133c601334263eb90072dc5abb8857e0512604`。
- Step 64 开始下发闭爪，右侧指垫首次接触 Step 68，左侧和双侧接触首次 Step 73，Step 78 抬升超过 2 cm，最高抬升约 15.68 cm。闭合期间夹爪最小开口约 29.63 mm，未达到 25 mm 的 `GRIPPER_ACTUATED` 判据。短测内未发出释放命令，未验证物理释放，未观察到官方成功。

## 资源与退出

Windows 总物理内存约 16092 MiB，基线可用约 5741 MiB，页面文件 15360 MiB、已用 4461 MiB。WSL 总内存 7798 MiB、Swap 2048 MiB。启动前只有 Workbench GUI。保留 512 MiB 单阈值与 1024 MiB/128 MiB 联合阈值。

| 采样点 | WSL 可用 MiB | 可用 Swap MiB |
| --- | ---: | ---: |
| 短测前 | 6703 | 754 |
| Worker 退出后 | 6965 | 397 |
| 静置 12 秒后 | 7001 | 398 |
| 本轮采样最低值（各自独立） | 1429 | 55 |

模型加载用时 41.27 秒。Worker 的 RSS 采样峰值 6603 MiB，PSS 采样峰值 6594 MiB，进程自报 RSS 高水位 6827592 KiB。Swap 曾低于 128 MiB，当时未同时到达 WSL 可用内存门槛，资源保护未触发。退出后两次采样仅保留 GUI。Swap 仍低于短测前，以上数据只覆盖本次运行。

## 验收

| ID | 状态 | 证据 |
| --- | --- | --- |
| P3-01 | PASS | 从桌面快捷方式打开 Workbench，并在点击运行前核对 Seed 201、Task 5 和三块短测。记录 Windows、WSL 和进程基线。 |
| P3-02 | PASS | 同一 CPU 模型实例完成三次真实前向，输入 Step 为 0、30、60。 |
| P3-03 | PASS | 逐块核验前块末步、chunk_finished、输入采样、前向开始和输出的单调时序。六张输入图像 SHA256 与记录一致，8D 输入和逐步反馈一致。 |
| P3-04 | PASS | 三块各执行 30 步。每条下发动作与对应 Plan 和 OSC 位置目标对齐，每步 Feedback 独立保留。 |
| P3-05 | PASS | 真实运行中 Step 30、60、90 的上方状态与下方当前步一致，阶段、回合、图像及状态均来自本轮。 |
| P3-06 | PASS | 从 GUI 停止，退出码 0。91 帧可解码，Phase 3 独立历史条目从 Step 0 播到 Step 90。 |
| P3-07 | PASS | 本轮保留内存压力阈值，未触发。保留每阶段用量及采样，模型卸载后 Worker 退出，GUI 保留。 |
| P3-08 | PASS | 14 个历史文件 SHA256 前后相同。短测输出、截图、源差异、日志和可核查视频哈希已归档。 |

本地源码改动集中在 `workbench/workers/book_pilot.py` 和 `workbench/ui/book_pilot_panel.py`，涵盖有界三块模式、观测记录、每块 GUI 继续以及独立短测历史列表。`source.diff` 与原始视频保留在本机。既有 GUI、IPC、官方单步仿真 11 项回归通过，逐步证据与历史哈希校验退出码 0。

- [验收 JSON](../results/task020/r1/phase3/acceptance.json)
- [推理和资源汇总](../results/task020/r1/phase3/metrics/summary.json)
- [Step 90 实跑](../results/task020/r1/phase3/screenshots/live_step_090.png)
- [Step 90 回放](../results/task020/r1/phase3/screenshots/replay_step_090.png)
