# Task022-C1 Swap 排查与 C3 组合预检续跑

**续跑结果为 `PASS`。** 本轮启动模型加载 1 次，完成 1 次，完成官方 Reset 1 次。模型前向、评测控制步和重试均为 0。组合 Reset 的状态、资产、Prompt、BDDL 和两路 RGB 指纹与 Task021、Task022-B 及 C2 一致。环境关闭、模型卸载，子进程正常退出。

第一次 C3 在启动前因旧 Swap 门槛被拒绝，SwapFree 为 348 MiB，Worker 未启动。它的报告和日志仍保留。本轮使用同一 CPU checkpoint，在独立子进程中先加载模型，随后才进入环境创建路径。

## 生效的资源条件

- 父进程启动子进程前、子进程加载模型前检查可用 RAM ≥1024 MiB。
- 模型加载后创建包装层之前、原生 MuJoCo 环境在官方 Reset 中创建之前，检查可用 RAM ≥512 MiB。
- SwapFree、CPU、PSI 每秒记录。续跑模式未调用旧 `formal_gate` 或 `under_pressure`，两者分别包含 128 MiB 硬性 Swap 下限或 RAM 和 Swap 组合条件。旧模式及 Workbench 原保护源码保持原样。
- 监督器在连续三次采样可用 RAM <256 MiB 或发现 WSL 全局 OOM kill 计数增加时写入停止标记，子进程在阶段边界读标记并清理。同步加载返回前没有可安全插入的释放点。没有结束其他进程，也没有变更 WSL 配置。

[实际入口与门禁源码](../scripts/task022_index34_diagnostic.py) · [门槛边界测试](../results/task022/c1/logs/gate_test.log) · [实际门禁采样](../results/task022/c1/logs/lifecycle/combined_resume/gates.jsonl) · [旧门禁记录](../results/task022/c/logs/lifecycle/combined/gates.jsonl)

## 本次资源读数

初始启动门禁采样可用 RAM **6478 MiB**，SwapFree **353 MiB**。模型在 314.31 秒内完成加载。创建环境前实测可用 RAM **2662 MiB**、SwapFree **315 MiB**，门禁结果为 **通过**。

| 指标 | 模型加载区间 | 子进程全程 |
| --- | ---: | ---: |
| RSS 采样峰值 (MiB) | 6255 | 6255 |
| PSS 采样峰值 (MiB) | 6256 | 6256 |
| WSL 最低可用 RAM (MiB) | 2609 | 1145 |
| 最低 SwapFree (MiB) | 316 | 0 |
| Worker CPU 采样峰值（单核 100%） | 606.0 | 606.0 |

进程 RSS 与 PSS 的全程采样峰值均发生在模型加载区间。全局可用 RAM 的最低值和 SwapFree 的最低值出现在加载完成之后，反映组合阶段的系统内存压力。

退出后 WSL 可用 RAM 为 6649 MiB，SwapFree 为 112 MiB。Worker 退出码为 `0`，WSL 全局 OOM kill 计数变化为 `0`。没有记录到临界内存停止标记。

[运行前 meminfo（含 SwapCached）](../results/task022/c1/logs/meminfo.txt) · [free](../results/task022/c1/logs/free.txt) · [swapon](../results/task022/c1/logs/swapon.txt) · [proc swaps](../results/task022/c1/logs/swaps.txt) · [vmstat](../results/task022/c1/logs/vmstat.txt) · [内存 PSI](../results/task022/c1/logs/memory_psi.txt) · [运行中采样](../results/task022/c1/logs/lifecycle/combined_resume/resources_supervisor.jsonl) · [资源曲线](../evidence/task022/c1/c3_resource_curve.png)

## 验收边界

Run ID 为 `c3_resume_index34_1795576677535882893`。配置 SHA256 为 `9f63d96cd65cfc2d297efbe0d6fd6897bcc9a00dc3b0cf0658d8c895224980e7`。权重、Prompt、Processor、动作映射和仿真配置保持原基线。官方 Reset 固有的 10 个无操作稳定步仍保留，诊断入口没有调用外层 `env.step`。本次结果限于资源生命周期，Task022-B 原诊断结果保持不变，Task022-D 未启动。

[命令与参数](../results/task022/c1/logs/lifecycle/launch.json) · [退出记录](../results/task022/c1/logs/lifecycle/combined_resume/exit.json) · [验收 JSON](../results/task022/c1/acceptance.json) · [统计 JSON](../results/task022/c1/metrics/summary.json) · [C3 Workspace](../evidence/task022/c1/0000_workspace.png) · [C3 Wrist](../evidence/task022/c1/0000_wrist.png)
