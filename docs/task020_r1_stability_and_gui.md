# Task020-R1 · 书本抓放试点：内存稳定性、Workbench 状态一致性与 Seed203 补测

**状态：CHANGES_REQUESTED / 继续 Issue #4，不启动 Task021。**

## 一、审核结论与真实边界

当前归档 `docs/task020_workbench_book_pilot.md`、`results/task020/acceptance.json`、`results/task020/metrics/summary.json`、中断日志与真实 WSLg 截图已核对：

- 已从同一个 Workbench GUI 链路发起冒烟及正式实验。Seed201：6 次模型前向、169 步、官方成功；Seed202：7 次前向、183 步、官方成功。两组均有实测双指接触、书本抬升搬运和历史视频回放。
- **官方放置成功不等于完整物理松爪**。两组终态夹爪仍 CLOSE、双侧接触为 True，`RELEASE_COMMAND_SENT=false` / `RELEASE_PHYSICALLY_VERIFIED=false`。
- Seed203 首次在 150 步后中断、根因未证实；第二次在 120 步后由 WSL Linux 内核证实 `global_oom` 杀死 Python 进程（证据：`results/task020/logs/book_pilot_oom.log`）。前两轮可用结果保留；第三轮没有官方终态，**不可报告 3/3 模型成功**。
- 报告显示正式完成轮的进程峰值约 6.7 GiB RSS；不能仅凭一次 OOM 就断言有模型内存泄漏。可能与 WSL 可用内存/其他进程/模型与视频缓存并存有关，须取证。
- 实际截图的 Task5 页正确显示书本和目标，但左侧离线 Input 区仍显示 Task017 双杯样本/指令，Seed202 历史回放时 Task5 选择框仍显示 Seed201，属于数据来源与界面上下文不一致。
- 按验收矩阵：T01–T03/T05–T08 为 PASS（基于已提交报告）；T04 BLOCKED、T09/T10 PARTIAL。整体 **PARTIAL / CHANGES_REQUESTED**，不关闭 Issue。

## 二、本次修复范围

### P0-A：先诊断 WSL 内存，不盲目反复跑 Seed203

1. 记录：Windows 物理内存、`.wslconfig` 当前内存/Swap 上限、WSL `MemTotal/MemAvailable/SwapTotal/SwapFree`、OOM 前后 kernel/cgroup 日志、模型 Worker/Workbench/仿真进程 PID 树与 RSS/PSS；记录后台其他大内存进程。不要在 GitHub 公开敏感系统路径。
2. 区分进程 RSS、整机 WSL 空闲内存、内存缓存与显存；每次模型加载、前向、视频写入、Episode 切换/停止时取样；至少对已有资源日志形成过程分析，短程验证可复用已有模型但不要无界重复完整回合。
3. 检查 GUI 与 Worker 是否在新 Episode 中重复驻留多个模型实例、旧 episode 环境、图像张量、完整 Action Chunk、视频帧缓存或被引用的 Torch 计算图；明确 `eval/inference_mode`、引用释放、日志流式落盘和子进程退出时资源回收是否生效。提出证据，不得凭猜测给“无泄漏”结论。
4. 若确认属于可修复的软件资源保持，做**最小修复**（及时释放 Episode/图像/视频/临时张量；必要时在两个正式 Episode 之间隔离或重启 Worker，但不能改变模型权重与推理语义）。若主要原因是 WSL 系统内存上限，先报告建议的系统配置方案与预期资源预算，**不得未经用户授权修改宿主机 `.wslconfig`、Swap 或强制结束无关程序**。
5. 增加“剩余 WSL 可用内存/运行中 Worker 内存”提示或至少在日志中稳定采样；内存不足时能通过 GUI 报 `RESOURCE_PRESSURE` 并安全停止、保存可用 JSON/图片/视频，不能让整个窗口无说明消失。不能保证安全退出时必须说明边界。

### P0-B：让 Workbench 当前任务的数据源真正一致

1. Task5 处于运行/回放模式时，左侧离线 Sample/Task Instruction/机器人状态不能继续以“当前任务输入”形式显示 Task017 的双杯指令。优先使用最小改动：显示并标记 **Task5 当前指令及来源、当前 Episode/Seed/Step**；旧离线基准保留在“离线前向”模式可用。
2. 回放 Seed202 时，界面上与“当前回合”有关的 Seed 显示应为 202；若某个 Seed 输入框只是**下一次运行设置**，明确标为 `Next Run Seed`，不要让用户误读为当前回放 Seed。
3. Plan/Command/Feedback 三层保持隔离，任务指令、图像、8D 输入、EEF/夹爪、物体/目标和事件必须来自同一回合及时刻；没有数据就显示 N/A，不得回退静态杯子样本。
4. 状态栏明确 `Live Simulation` / `Historical Replay` / `Offline Prediction`，并标明当前步与最终成功汇总的区别。对 Seed201/202 的 GUI 截图做人工+自动化核对。

### P0-C：只在资源问题受控后补跑 Seed203

1. 必须复用同一 `lerobot/xvla-libero` 检查点、Processor、OSC_POSE、控制频率与已记录的控制策略。核对 Task017 **完整回合**的实际时域策略；不要将 Task017 早期 15 步实验与后来完整回合直接混作同一策略。
2. 记录重跑前 WSL 内存预算，并使用独立隔离的 Worker/仿真进程从官方初始状态 index 2 **重新 reset**、通过 GUI 启动 Seed203。不得把前两次中断的 150/120 步接到新回合冒充连续轨迹。
3. 所有尝试分别归档，文件名/Attempt ID 必须唯一，原两次中断记录与日志不可覆盖。
4. 成功到官方终态则填写 Seed203 实际官方结果（成功或失败都能通过工程验收）；中途再 OOM 或其他资源中断，记录 `BLOCKED_RESOURCE` 并停止，无限重试禁止。
5. 恢复后的 Episode 无论成功或失败，都应从 Workbench 可查看实际双摄、逐步状态和历史回放；若再次中断但存在局部视频帧，允许查看**标注 INCOMPLETE 的局部回放**，不能伪装完整官方回合。

## 三、验收矩阵

| ID | 验收条件 |
|---|---|
| R1-01 | 提供 WSL 系统内存、Swap、PID/RSS 与 OOM 的可复核证据，区分根因与假设 |
| R1-02 | 证明同一时间仅有计划内模型/仿真进程驻留，Episode/Worker 切换后资源可回收 |
| R1-03 | Workbench 显示资源状态，异常终止有清晰记录，尽可能保留局部证据 |
| R1-04 | Task5 左侧指令/状态/图像来源正确，不把双杯离线样本当成书本模型输入 |
| R1-05 | Seed201/202 历史回放与任务选择状态一致；下一轮运行设置单独标记 |
| R1-06 | Seed203 在确认资源预算后由 GUI 从官方 reset 重试，记录真实退出码、前向与终态 |
| R1-07 | 模型、权重、Processor/控制器、Task017/018/019/Task020 已有记录保持不变 |
| R1-08 | 历史记录支持成功/失败/中断三种状态，所有结果不伪造完整抓放释放 |
| R1-09 | 新增中文技术报告、完整测试日志、真实 GUI 截图、验收 JSON 与轻量 GitHub 证据，远端 JSON 标准解析通过 |

**完成条件**：R1-01～R1-09 逐项出具 PASS/PARTIAL/BLOCKED。不强制 Seed203 成功；只要完成合法完整回合并有完整日志/视频，模型官方失败也能是有效实验结论。若因资源限制确实不可继续，应有可靠定位报告而非无限循环尝试。

## 四、明确不做

- 不训练、不微调、不改权重、不换模型；
- 不添加新物体或其他 LIBERO suite；
- 不为追求高成功率调整随机种子/Prompt/控制器/统计阈值；
- 不拆掉或重写 VLA Workbench，不新增另一套桌面应用；
- 不接真实机器人、ROS、NPU；
- 不擅自修改宿主系统内存/Swap 设置，不重复运行已完成的 Seed201/202；
- 不覆盖旧版 Task020 审计、Seed203 两次中断记录或 Task017/018/019 历史事实。

## 五、交付和接力

在本地 `vla-learning/docs/task020_r1_stability_and_gui.md`、`results/task020/r1/` 归档本轮结果；GitHub 分支 `task020-workbench-book-pilot` 同步 `docs/task020_r1_stability_and_gui.md`、精简验收 JSON、资源指标、精选截图和报告；原始模型权重及 MP4 大文件留本地。

完成后在 Issue #4 评论 `STATUS: REVIEW`，标明每个验收项状态、源码和归档 Commit、测试命令与退出码、Seed203 结果和本地录像哈希。若资源阻断，评论 `STATUS: BLOCKED` 并给出下一步可操作的资源预算。**不要自动开始 Task021**。
