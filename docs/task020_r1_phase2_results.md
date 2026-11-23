# Task020-R1 Phase 2 · 真实 X-VLA 短程验证

状态为 **REVIEW**。从 Windows 桌面 VLA Workbench 快捷方式启动 LIBERO-10 Task 5 的 Seed 201 资源短测。完整检查点加载成功，一次真实前向后执行了 30 个仿真步，再从 GUI 正常停止。回合官方终态未评估，Seed 203 尚未启动。

## 实验与动作验证

- 检查点为 `lerobot/xvla-libero`，revision 为 `8e6aeef01f634f5d3b5be4340328f19cc2c25a65`，权重 SHA256 为 `2a0e29448111df56b9485cb1f964db799205794c49baeda48ef960589ce649ab`。CPU 加载耗时 108.41 秒，共 879,482,456 个参数。
- 输入来自 Task 5 官方 Reset，初始状态索引为 0。双视角各 256×256×3，本体输入 8D，经既有 Processor 得到 9D。真实前向耗时 39.8515 秒，原始动作 30×20，后处理和仿真控制输入 30×7，NaN 和 Inf 均为 0。
- 经 GUI 放行，执行 1 个动作块、30 步。每步实际下发动作与块内对应动作一致，逐步核对 OSC 绝对位置及首步旋转。模型输出、控制命令和环境反馈分别保存。
- GUI 停止后退出码为 0。环境关闭，模型卸载，MP4 已验证可读 31 帧，含 Reset 帧，512×256、20 fps。用户停止时没有到达官方终态。

## 内存与回收

Windows 启动前物理内存 16092 MiB，可用约 4633 MiB。页面文件总量 15360 MiB，未使用约 11836 MiB。WSL 总内存 7798 MiB，Swap 总量 2048 MiB。基线仅有一个 Workbench GUI，无模型 Worker。曾启动一个重复的空闲 Workbench 窗口，确认无子进程后关闭。一次模式选择失误启动了 Seed 201 的独立尝试，GUI 在加载权重前停止，0 前向、0 步，另行保留记录。

| 采样点 | WSL 可用 MiB | WSL 可用 Swap MiB |
| --- | ---: | ---: |
| 回放核对后、短测前 | 6438 | 953 |
| 短测期间各自最低 | 1377 | 317 |
| Worker 退出后 | 6899 | 424 |
| 退出后静置 12 秒 | 7020 | 424 |

Worker 峰值 RSS 6827336 KiB（约 6.51 GiB），采样峰值 PSS 6653 MiB。最低可用内存和 Swap 是各自独立的极值。本轮未触发保护。退出后的两个样本均查无 Worker，GUI 仍在。Swap 未回到基线，文件缓存增加。以上证据仅覆盖本次短测，完整回合资源预算仍未验证。

## 逐项验收

| ID | 状态 | 证据 |
| --- | --- | --- |
| P2-01 | PASS | Windows/WSL 内存和页面文件、进程 PID/父 PID 与 RSS/PSS 已采样。Task 5 历史双视角回放已从桌面快捷方式核对。 |
| P2-02 | PASS | GUI 加载完整 CPU 检查点，用时 108.41 秒。配置和文件 SHA256 已保存。 |
| P2-03 | PASS | 一次真实前向用时 39.8515 秒。双视角、8D 状态、原始与后处理张量形状和有限值已核验。 |
| P2-04 | PASS | 30 条实际下发动作逐条匹配动作块。逐步核对 OSC 绝对位置，首步核对旋转。 |
| P2-05 | PARTIAL | 真实 GUI 执行 1 个动作块和 30 步。最后图像、8D 状态和底部 Step 30 同步，顶部等待状态曾误显示 Step 0。已修复并通过无模型定向回归。 |
| P2-06 | PASS | GUI 停止，Worker 退出码 0，封装的 MP4 逐帧读出 31 帧。 |
| P2-07 | PASS | 完成卸载采样，Worker PID 已回收，GUI 保留在退出后两次测量中。 |
| P2-08 | PASS | 原有 201/202/203 的 10 个记录文件前后 SHA256 一致。新增记录与视频哈希已归档。 |

实际窗口的顶部等待状态曾错误显示 Step 0。另一次点击离线加载按钮会留下旧的 Loading Model 文案，实际没有启动离线 Worker。两处已修复。修复后的事件步号、按钮行为、历史哈希与视频逐帧解码通过定向验证，既有 GUI／IPC／官方仿真集成共 11 项通过。真实模型只运行一次，实跑截图仍保留当时界面。

本地 Workbench 已增加资源短测档、GUI 分段确认和单动作块限制。执行时的源码和最终源码差异分别归档为 `source_executed.diff` 和 `source.diff`。模型、控制参数、原始历史和完整视频保留本地。

- [验收 JSON](../results/task020/r1/phase2/acceptance.json)
- [资源和推理指标](../results/task020/r1/phase2/metrics/run_summary.json)
- [真实运行第 30 步](../results/task020/r1/phase2/screenshots/live_step_30.png)
- [Worker 日志与运行证据](../results/task020/r1/phase2/runs/seed_201/)
