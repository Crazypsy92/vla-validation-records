# VLA 任务状态与验收索引

> **任务唯一入口为 GitHub Issues**；此文件只保留导航和已审核的状态摘要。Antigravity 不应仅凭 README 自动启动实验。
>
> **默认接力状态：OFF（按需手动执行）。** 发布 Issue 不会自动启动本机 IDE、定时计划或 GPU 任务。

## 当前任务

| ID | 任务 | Issue | 状态 | 下一步 |
| --- | --- | --- | --- | --- |
| Task017-R2 | 完整回合证据归档，明确抓持判据例外 | [#1](https://github.com/Crazypsy92/vla-validation-records/issues/1) | **ACCEPTED_WITH_LIMITATIONS / 已关闭** | 官方任务 3/3 验收；抓持与释放例外转 Task018 |
| Task018 | **夹爪抓放审计与 VLA Workbench 三层监控回放** | [#2](https://github.com/Crazypsy92/vla-validation-records/issues/2) | **ACCEPTED_WITH_FOLLOWUP / 已关闭** | 20项报告归档；截图暴露的画面因果性与模式语义转 Task019 |
| Task019-R1（Task019返修） | **回放数据可信度与桌面显示修复** | [#3](https://github.com/Crazypsy92/vla-validation-records/issues/3) | **ACCEPTED_WITH_LIMITATIONS / 已关闭** | R1-01～R1-08 通过；内部回放通过。外部播放器未验证，模型前向按范围未重跑；进入 Task020 |
| Task020-R1 | **Workbench 书本抓放官方任务验证** | [#4](https://github.com/Crazypsy92/vla-validation-records/issues/4) | **ACCEPTED_WITH_LIMITATIONS / 已关闭** | 2 个官方成功、1 个资源中断未完成，物理释放未验证。 [结题报告](docs/task020_goal_met_with_limitations.md) · [Phase 4 阻断报告](docs/task020_r1_phase4_seed203_results.md) |
| Task021 | **LIBERO Task 5 初始状态泛化验证** | [#5](https://github.com/Crazypsy92/vla-validation-records/issues/5) | **阶段 A 待审核 / 阶段 B BLOCKED** | 已盘点官方状态。候选待审核，当前 Workbench 无候选索引入口。 [阶段 A 报告](docs/task021_initial_state_generalization.md) |

## 历史归档

| 范围 | 内容 | 已归档证据 | 重要边界 |
| --- | --- | --- | --- |
| Task010–011 | SmolVLA 离线推理与输入敏感性 | [docs](docs/) · [results](results/) | 不等于动作语义正确 |
| Task012–014 | X-VLA 推理、LIBERO 数据与动作处理审计 | [docs](docs/) · [results](results/) | 不等于真机任务成功 |
| Task015–016 | 独立 VLA Workbench 与动作语义核查 | [docs](docs/) · [results](results/) | 上位机为离线模型验证 |
| Task017（初期） | 60 步三种子闭环，软件 3/3、任务 0/3 | [技术报告](docs/task017_libero_closed_loop.md) · [验收](docs/task017_acceptance_report.md) | **仅初期 60 步测试，不是较新完整任务测试** |
| Task017（完整回合） | 24 次推理/664 步，LIBERO 判定 3/3 成功，第二只杯终止前未主动释放 | [技术报告](docs/task017_full_rollout.md) · [验收报告](docs/task017_full_rollout_acceptance.md) | **官方判定 3/3 成功，但第二只杯未观察到张爪释放** |
| Task018（抓放监控） | 历史数据冲突查清，证实白杯真实抬升9.99cm；确证LeRobot成功强行terminated=True；确证终态动作块已规划释放(-1.0)；完成P0/P1审查定向修复；Workbench上线三层隔离监控与历史回放 | [技术报告](docs/task018_grasp_monitor_and_release.md) · [验收报告](docs/task018_grasp_monitor_and_release_acceptance.md) · [审查修复报告](docs/task018_review_fixes.md) | **官方 3/3 成功，杯1释放通过，杯2因环境终止未下发张开** |
| Task019（连续视频回放） | 视频流审计(512x256@20FPS)，双视角流切分(主视角/副视角)，帧步1:1零插值对齐；P0.1模式单一数据源；P0.2杜绝未来帧泄漏；P0.3瞬时步与全局总结解耦；P1.1语义纠偏；上线连续播放控件(Play/Pause/Scrub/0.5x~2.0x/系统播放器) | [技术与验收报告](docs/task019_replay_video.md) · [验收矩阵](results/task019/acceptance.json) | **基于Task017原始录像，不重跑推理，不修改权重** |

## 标准工作流

1. ChatGPT 发布 **一个** [TASK] Issue，写明目标、边界和验收。
2. Antigravity 打开此仓库的 [接力规范](docs/remote_task_relay.md) 与唯一未完成 Issue；检查本地工程和上游证据，再回评论 STATUS: RUNNING。
3. 在独立工作分支只执行该任务；更新 docs/、results/、evidence/ 和发布清单。
4. 上传 commit/PR 及原始证据，评论 STATUS: REVIEW；无法完成时评论 STATUS: BLOCKED。
5. 由 ChatGPT 与用户审核后标记 STATUS: ACCEPTED，再关闭 Issue、发布下一个任务。

**只领取标题含 [TASK] 且前置依赖已完成的 Issue。** Issue #1 已独立审查并以有限边界关闭；Issue #2 已 ACCEPTED_WITH_FOLLOWUP 并关闭；Issue #3（Task019-R1）已按 ACCEPTED_WITH_LIMITATIONS 关闭；**Issue #4（Task020）已按 ACCEPTED_WITH_LIMITATIONS 验收并关闭。Issue #5（Task021）为当前唯一开放任务。** 只执行 Task021；完成并验收后再规划下一项。

**不要因为 Issue 状态被标为完成，就自动重跑模型或立即展开下一阶段。**
