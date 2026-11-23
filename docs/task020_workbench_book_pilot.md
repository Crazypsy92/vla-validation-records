# Task 020 · VLA Workbench 驱动的书本抓放闭环试点

**当前状态：READY。** 本任务由原计划的“两个非杯类任务 × 三个种子”调整为“LIBERO-10 Task 5 单任务 × 三个种子”。调整原因是本机官方 `libero_10` 任务注册表中，只有 Task 5 符合原先的单物体、单放置目标、非杯类操作要求。用户已确认先用该任务打通现有 VLA Workbench 的完整操作流程。

## 1. 本轮首要目标

**优先让用户从现有 Windows 桌面 VLA Workbench 启动并运行书本抓放仿真任务。**

不是只写一个 Python 脚本、在终端跑完实验后再导入结果。本轮正式实验必须由现有 Workbench 的 GUI 发起；模型推理和 LIBERO 仿真可以继续由后台 Worker/Python 进程完成，但启动、过程监控、停止和历史回放都应通过 Workbench 完成。

用户预期流程：

1. 打开 Windows 桌面现有 VLA Workbench 快捷方式。
2. 在任务选择器选择 `LIBERO-10 / Task ID 5`。
3. 界面显示正确的任务指令、目标物体“书本”和目标位置“收纳盒后部”。
4. 选择随机种子并点击运行。
5. 在界面观察双视角画面、模型动作、控制器指令和仿真真实反馈。
6. 结束后在历史记录中选择该 Episode 并完整回放。

终端命令允许用于开发、调试和自动化回归，但**不得把终端命令作为用户运行正式实验的唯一入口**。不新建第二套独立 VLA 上位机，不大规模重构现有 Workbench。

## 2. 任务定义

| 字段 | 内容 |
|---|---|
| Benchmark | 官方 LIBERO |
| Suite | `libero_10` |
| Task ID | `5` |
| 官方指令 | `pick up the book and place it in the back compartment of the caddy` |
| 操作物体 | `black_book_1`（黑色书本） |
| 目标区域 | `desk_caddy_1_back_contain_region`（收纳盒后部） |
| 官方目标谓词 | `In(black_book_1, desk_caddy_1_back_contain_region)` |
| 模型 | 当前已验证的 `lerobot/xvla-libero` 本地检查点 |
| 正式随机种子 | `201、202、203` |
| 正式回合数 | 3 个完整 Episode |

场景中存在黄白色杯子，但它不是本任务的操作目标，只作为场景道具/潜在干扰物记录。不得将目标标签继续显示为 Mug 1 / Mug 2，也不得把杯子误报为本任务的目标物。

原始选题审计继续保留：`docs/task020_object_generalization.md` 和 `results/task020/metrics/official_task_inventory.json` 记录的是原“两任务门槛”下只有 Task 5 一个候选的事实。本次是经用户确认后的任务范围调整，不得回写或伪装原审计结果。

## 3. 执行阶段

### Phase A：复用现有工程并完成兼容性预检

1. 检查本地 `vla-learning` 中 Task017/018/019 的闭环执行、Workbench、Worker、事件记录和回放入口。
2. 沿用 Task017 已验证的模型加载、LeRobot Processor、动作后处理、控制器和滚动时域执行链。
3. 实例化官方 Task 5 环境，确认环境可 reset/step，双视角图像键、机器人状态、动作维度和控制器输入均与现有链路兼容。
4. 记录模型 revision/权重哈希、Processor 配置、环境版本、控制器参数、设备和资源占用。
5. 不修改权重、Prompt、归一化统计、动作缩放、控制器参数或成功阈值。若发现不兼容，先定位并报告；不得靠猜测参数继续运行。

### Phase B：把 Task 5 接入现有 Workbench

只做必要的任务注册、数据显示和运行入口适配：

- 任务选择器显示真实 Suite、Task ID、官方任务名称/指令。
- 目标物显示“黑色书本”，目标位置显示“收纳盒后部”。
- 支持选择 Seed、启动、停止和查看运行状态；已有暂停功能则复用，不为此进行大规模 UI 重构。
- Worker/仿真进程由 Workbench 管理生命周期，避免用户手动敲 Python 命令。
- 运行中显示当前 Episode、Seed、Step、模型前向次数、当前执行阶段、最近推理耗时和错误信息。
- 双视角相机画面使用当前仿真观测，不得使用静态示意图冒充实时画面。
- Plan / Command / Feedback 三层继续分离：
  - Plan：模型预测动作、当前动作块/偏置、预测夹爪命令；
  - Command：实际交给控制器的目标与控制量；
  - Feedback：实际 EEF 位姿、夹爪开度、书本位姿、接触状态和任务状态。
- 没有真实数据的字段显示 N/A，不得填充模拟值或伪造 PASS。

### Phase C：先从 GUI 做一次短程冒烟验证

1. 用户通过桌面快捷方式打开 Workbench。
2. 在 GUI 选择 Task 5、Seed 201 并启动。
3. 验证环境加载、双视角更新、状态读取、至少一次真实模型前向、动作下发和反馈刷新。
4. 运行少量控制步后通过 GUI 停止，确认进程可正常退出，记录可正确保存。
5. 重新 reset 环境，确保冒烟测试不污染正式 Episode。

冒烟测试单独标记，不计入正式三个 Episode。若 Workbench 无法完整驱动该链路，先修复 GUI/Worker 集成，不要跳过 GUI 改用终端直接跑完整实验。

### Phase D：从 Workbench 完成正式闭环

冒烟验证通过后，正式执行三个完整 Episode：

| Episode | Seed | 要求 |
|---|---:|---|
| EP00 | 201 | 从官方 reset 开始，运行至官方成功或环境最大步数终止 |
| EP01 | 202 | 同上 |
| EP02 | 203 | 同上 |

- 三个正式 Episode 均通过 Workbench GUI 发起。
- 每轮模型推理都使用执行后的最新视觉观测和机器人状态。
- 不人为截断成固定 60 步；使用环境配置的真实步数上限并记录。
- 一个 Episode 失败不代表整轮停止；保留失败记录并继续其余回合。
- 仅在环境/软件管线故障、OOM 或连续异常导致无法安全继续时停止并报告。
- 不换种子、不跳过失败样本、不临时调参。

## 4. 每轮必须记录的八阶段物理证据

1. `PREDICTED_CLOSE`：模型是否预测闭爪。
2. `GRIPPER_ACTUATED`：仿真夹爪是否实际闭合。
3. `TARGET_CONTACT`：书本与左右指垫/夹爪相关碰撞几何体的接触情况，分别记录左右侧证据。
4. `OBJECT_LIFTED_AND_HELD`：书本是否离开支撑面并保持；沿用既有 Task018 判据，不得临时改变阈值。
5. `TRANSPORTED_TO_TARGET`：书本是否被搬运到收纳盒目标区域附近/上方。
6. `RELEASE_COMMAND_SENT`：模型是否预测并实际下发张爪命令。
7. `RELEASE_PHYSICALLY_VERIFIED`：夹爪是否实际张开、书本是否与夹爪解除接触并留在目标区域。
8. `OFFICIAL_TASK_SUCCESS`：LIBERO 官方 `is_success` 判定。

接触传感器应同时保存左右指垫与其他相关夹爪碰撞几何体的原始证据。不得仅凭单一接触标志就断言抓取成功或失败；结合夹爪开度、物体位姿变化、抬升和保持轨迹判定。若官方成功导致环境立即终止，必须区分“模型规划释放”“控制器已下发释放”和“物理释放已验证”。

失败类型至少区分：目标未识别/选错、接近失败、未接触、单侧接触、闭合但未抓住、抬升失败、搬运滑脱、未进入目标区域、未释放、官方超时、软件管线异常。

## 5. Workbench 历史回放要求

- 三个正式 Episode 均可在历史列表中选择。
- 列表显示真实 Task ID、任务名、目标物、Seed、官方结果。
- 可完整播放/暂停/拖动视频或按 Step 回放。
- 双视角画面、当前 Step、EEF 位姿、夹爪开度、书本位姿、接触状态和八阶段事件同步。
- Plan / Command / Feedback 不混用。
- 失败 Episode 也必须能回放。
- 不得用预先生成的静态截图冒充当前运行过程。

## 6. 验收矩阵

| ID | 验收项 | 通过条件 |
|---|---|---|
| T01 | Task 5 环境兼容 | 官方环境可实例化/reset/step；输入输出与模型链路完成核对 |
| T02 | Workbench 任务入口 | GUI 正确显示 Task 5、书本和收纳盒后部，不残留杯类旧标签 |
| T03 | GUI 冒烟测试 | 从桌面 Workbench 启动，完成真实模型前向、控制下发和反馈刷新，可停止并复位 |
| T04 | 三个正式 Episode | Seed 201/202/203 均由 GUI 启动并完整尝试，失败不漏记 |
| T05 | 动作链证据 | 每次模型动作块、Processor 后动作、控制器输入可追溯 |
| T06 | 抓取与搬运证据 | 接触、夹爪开度、物体位姿、抬升与搬运过程有逐步记录 |
| T07 | 释放与官方结果 | 释放命令、物理张开、接触解除、官方成功分别记录 |
| T08 | Workbench 实时监控 | 双视角和 Plan/Command/Feedback 数据来自当前仿真 |
| T09 | 历史回放 | 三轮数据可加载回放，失败回合也可查看 |
| T10 | 归档与复现 | 报告、acceptance、summary、逐轮记录、日志、截图/视频元数据、复现说明齐全 |

**工程验收 PASS 不要求模型必须 3/3 成功。** PASS 表示 GUI 启动、模型推理、仿真执行、物理证据、回放和归档链路真实可靠；模型任务成功率单独报告。

## 7. 工程边界

- 只做 LIBERO 仿真，不接真实机械臂、ROS 或真实相机。
- 不训练、不微调、不换模型、不改权重。
- 不修改 Task017/018/019 历史数据。
- 不为凑结果更换种子、跳过失败或调参。
- 不新建第二套 VLA GUI，不大规模重构 Workbench。
- 不上传模型权重、第三方仿真资产、完整大视频；视频保存在本地，GitHub 归档精选截图、轻量指标和视频元数据。
- 若必须通过终端才能启动正式 Episode，视为 Workbench 集成未完成，不得把该项标 PASS。

## 8. 交付物

本地工程：`/home/bridge/projects/ai-learning/vla-learning`

- `docs/task020_workbench_book_pilot.md`：完整技术报告；
- `results/task020/acceptance.json`：T01–T10 验收结果；
- `results/task020/metrics/summary.json`：冒烟、任务级和总览指标；
- `results/task020/records/seed_<seed>/`：逐轮完整记录；
- `results/task020/logs/`：运行日志和资源采样；
- `results/task020/videos/`：本地原始视频及哈希元数据；
- Workbench 必要的任务选择、运行控制、实时监控与历史回放适配及回归测试。

GitHub 归档仓库更新 README、TASKS、发布清单；只上传报告、验收 JSON、轻量指标、精选截图和视频元数据。

完成后在 Issue #4 评论 `STATUS: REVIEW`，列出 T01–T10 的 PASS/PARTIAL/FAIL/BLOCKED、真实 GUI 启动方式、冒烟测试结果、三个 Episode 的结果、模型前向次数、Commit/PR 和证据路径。未实际从 GUI 运行的项目不得标 PASS。

**本任务完成后停止，不自动开展 Task021。**
