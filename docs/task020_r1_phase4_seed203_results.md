# Task020-R1 Phase 4 · Seed 203 正式补测

状态 **BLOCKED**。从 Windows 桌面快捷方式进入现有 Workbench，选定 `libero_10` Task 5 / Seed 203 / Formal，唯一 Attempt ID 为 `phase4_seed_203_1795437286005880657`。本阶段仅有这一次正式尝试。Worker 退出码 0，共 7 次真实前向、191 个实际仿真步，终止原因为 `resource_pressure`。LIBERO 官方结果为 `None`，物理释放验证为 `False`。

## Reset、模型与执行

官方初始状态索引为 2，SHA256 为 `83ff554be370e25fb3b049d5c3db3f2cf4f20524a0eab8beeda093c6a81bad66`，环境上限 520 步。检查点 `lerobot/xvla-libero` revision `8e6aeef01f634f5d3b5be4340328f19cc2c25a65`，权重 SHA256 `2a0e29448111df56b9485cb1f964db799205794c49baeda48ef960589ce649ab`。CPU、Processor 文件、Task 5 BDDL、绝对 OSC_POSE、20 Hz、每块 30 步，均与既有设置相符。前一块末步、结束事件、观测时戳、下一次前向和下一块实际动作已逐块核对。

| 动作块 | 最新观测 Step | 实际执行步数 | 前向秒数 |
| --- | ---: | ---: | ---: |
| 0 | 0 | 30 | 33.6448 |
| 1 | 30 | 30 | 34.4934 |
| 2 | 60 | 30 | 35.4735 |
| 3 | 90 | 30 | 32.7093 |
| 4 | 120 | 30 | 32.0475 |
| 5 | 150 | 30 | 31.7374 |
| 6 | 180 | 11 | 53.3357 |

首次闭爪命令 Step 74；首次左/右接触 Step 81/79，首次双侧接触 Step 81。首次抬升超过 2 cm 的 Step 为 88，峰值 0.2743151702205643 m。首次进目标区域 Step None。闭爪后首条释放命令 Step None。未获得的事件取值为 None。

## 资源保护及退出

Windows 预检可用物理内存约 4107 MiB，页文件共 15360 MiB、已用 3924 MiB。WSL 在 GUI 启动门禁时可用 6585 MiB、可用 Swap 718 MiB。以 Phase 3 实测边界与基线差额估计正式阶段边界余量，投影可用 RAM 1313 MiB、Swap 183 MiB，实际仍由新门禁逐块判断。历史第二次 Seed 203 在 Step 120 后遇内核全局 OOM，第一次于 Step 150 中断、根因未确认。

原硬保护为 `MemAvailable < 512 MiB` 或 `MemAvailable < 1024 MiB 且 SwapFree < 128 MiB`。正式预启动、模型加载前和每块前向/下发前独立核对 Swap 128 MiB。128–255 MiB 时记录 WARNING 和三次采样，依据趋势放行或停止。第 7 块执行中，GUI 采到 826 MiB 可用 RAM、112 MiB 可用 Swap，触发原联合保护。Worker 随后采到 811／104 MiB，在第 191 步结束第 7 块，没有开始第 8 次前向。没有观察到新的 OOM kill。GUI 在模型加载期持续记录资源；外部内核和进程树采样器在首轮前向期间接入已启动的同一回合，早期采样器退出原因保留在日志中。

| 采样点 | WSL 可用 MiB | Swap 可用 MiB | 全局 OOM kill 计数 |
| --- | ---: | ---: | ---: |
| GUI 启动前 | 6585 | 718 | 1 |
| 本轮各自最低 | 571 | 104 | — |
| worker_exit | 4261 | 302 | 1 |
| idle_12_seconds | 5714 | 493 | 1 |

本轮 Worker RSS/PSS 采样峰值为 6610/6605 MiB，RSS 高水位 6812752 KiB。Phase 2 的 PSS 峰值 6653 MiB，Phase 3 为 6594 MiB。退出后的系统内存和 Swap 受缓存、换页与 GUI 驻留影响，单次差值不足以判定泄漏。视频解码结果为 192 帧，20 fps，SHA256 `53df7c8bc291a0b82783aecfc76da78859afef654a98681f0f7d177b41d6ec92`。

## 中断回放与修复

录像准确覆盖 Reset 和 191 个仿真步。用 Workbench 历史条目回放时明确显示 `INCOMPLETE / RESOURCE_PRESSURE`，验证 Step 0、30、60、90、120、150、180、191 的图像、状态和命令。实跑结束截图的实时面板仍保留偶数采样帧 Step 190，顶部终态已显示 Step 191。随后修复了奇数终止步从同一步快照更新画面和数据的逻辑，用本轮真实末步做回归，未重新运行模型。已通过 6 项门禁测试、11 项现有 GUI/IPC/仿真测试，以及逐帧录像与历史回放校验。

## 逐项验收

| 编号 | 状态 | 依据 |
| --- | --- | --- |
| P4-01 | PASS | 历史 OOM、Windows/WSL/Swap、运行前预算和门禁边界测试已记录。 |
| P4-02 | PASS | Workbench 正式配置和官方 Reset 从独立 Attempt 查询。 |
| P4-03 | BLOCKED_RESOURCE | RESOURCE_PRESSURE，191 步，终止原因为 resource_pressure。 |
| P4-04 | PASS | 前向 7 次，每块按时间、当前观测、Plan、Command 和反馈核对。 |
| P4-05 | PASS | 动作、实际夹爪开度、左右接触、书本状态、物理释放和官方结果分开记录。 |
| P4-06 | PASS | Workbench 按唯一 Attempt ID 回放；视频和解码验证可查。 |
| P4-07 | PASS | 采样覆盖加载、各块、退出和静置；保护日志及 Worker 生命周期已保存。 |
| P4-08 | PASS | 290 份已保存文件的 SHA256 前后一致。 |
| P4-09 | PASS | 分别给出 R1 和原始 Task020 的逐项总结。 |

## Task020-R1 总体

| 编号 | 状态 | 依据 |
| --- | --- | --- |
| R1-01 | PASS | Windows 与 WSL 基线、完整模型峰值和历史 OOM 已记录。 |
| R1-02 | PASS | 单一模型 Worker、退出进程清点和静置复测。 |
| R1-03 | PASS | 现有联合硬保护和正式 Swap 门禁经过测试，记录每次低余量评估。 |
| R1-04 | PASS | Phase 3 复验真实画面和 Step，Phase 4 正式沿用同一界面。 |
| R1-05 | PASS | 沿用 Phase 1 已验 Seed 201/202 回放及 Next Run Seed。 |
| R1-06 | BLOCKED_RESOURCE | 只尝试一次新的官方 Seed 203，从 Reset 到记录终点。 |
| R1-07 | PASS | 检查点、Processor、控制配置及历史文件的哈希核验。 |
| R1-08 | PASS | 历史列表区分正式成功、未成功及中断，保留真实录像。 |
| R1-09 | PASS | 阶段报告、真实截图、JSON、GitHub 清单、测试命令与日志归档。 |

## Task020 原始工程验收

| 编号 | 状态 | 依据 |
| --- | --- | --- |
| T01 | PASS | 预检确认官方 BDDL、20 Hz、双 RGB、8D 状态和 7D OSC；正式前向、控制通过。 |
| T02 | PASS | 书本试点标签提供官方 Task 5、黑色书本、收纳盒后部与种子选择。 |
| T03 | PASS | 种子 201 真实前向 1 次，执行 3 步，GUI 停止并保存。 |
| T04 | BLOCKED_RESOURCE | 201/202 已完成，本轮 Seed 203 RESOURCE_PRESSURE。 |
| T05 | PASS | 原始动作和后处理形状与有限值通过校验，逐步下发值和动作块一致。 |
| T06 | PASS | 逐步记录双侧指垫、其他夹爪接触、开度、书本位置与姿态。 |
| T07 | PASS | 释放规划、实际张开指令和物理释放分别记录。 |
| T08 | PASS | 从实际 WSLg 窗口捕获仿真双视角和同一步反馈。 |
| T09 | PARTIAL | 正式回合与旧中断数据均保留，已验证可播放的回放。 |
| T10 | PARTIAL | 新旧记录独立，归档视频哈希、资源和执行证据。 |


- [验收 JSON](../results/task020/r1/phase4/acceptance.json)
- [运行、资源及视频指标](../results/task020/r1/phase4/metrics/summary.json)
- [正式启动确认](../results/task020/r1/phase4/screenshots/formal_confirmation.png)
- [终点历史回放](../results/task020/r1/phase4/screenshots/replay_final.png)
