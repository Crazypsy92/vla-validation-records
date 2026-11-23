# VLA 任务状态与验收索引

> **任务唯一入口为 GitHub Issues**；此文件只保留导航和已审核的状态摘要。Antigravity 不应仅凭 README 自动启动实验。
>
> **默认接力状态：OFF（按需手动执行）。** 发布 Issue 不会自动启动本机 IDE、定时计划或 GPU 任务。

## 当前任务

| ID | 任务 | Issue | 状态 | 下一步 |
| --- | --- | --- | --- | --- |
| Task017-R2 | 完整回合证据归档，明确抓持判据例外 | [#1](https://github.com/Crazypsy92/vla-validation-records/issues/1) | **ACCEPTED_WITH_LIMITATIONS / 已关闭** | 官方任务 3/3 验收；抓持与释放例外转 Task018 |
| Task018 | **夹爪抓放专项 + VLA Workbench 机械臂运行/物体/接触监控回放** | [#2](https://github.com/Crazypsy92/vla-validation-records/issues/2) | **REVIEW / 待外部审核** | 全量审计、Workbench三层隔离回放及证据已就绪，等待评审标记 ACCEPTED |

## 历史归档

| 范围 | 内容 | 已归档证据 | 重要边界 |
| --- | --- | --- | --- |
| Task010–011 | SmolVLA 离线推理与输入敏感性 | [docs](docs/) · [results](results/) | 不等于动作语义正确 |
| Task012–014 | X-VLA 推理、LIBERO 数据与动作处理审计 | [docs](docs/) · [results](results/) | 不等于真机任务成功 |
| Task015–016 | 独立 VLA Workbench 与动作语义核查 | [docs](docs/) · [results](results/) | 上位机为离线模型验证 |
| Task017（初期） | 60 步三种子闭环，软件 3/3、任务 0/3 | [技术报告](docs/task017_libero_closed_loop.md) · [验收](docs/task017_acceptance_report.md) | **仅初期 60 步测试，不是较新完整任务测试** |
| Task017（完整回合） | 24 次推理/664 步，LIBERO 判定 3/3 成功，第二只杯终止前未主动释放 | [技术报告](docs/task017_full_rollout.md) · [验收报告](docs/task017_full_rollout_acceptance.md) | **官方判定 3/3 成功，但第二只杯未观察到张爪释放** |
| Task018（抓放监控） | 历史数据冲突查清，证实白杯真实抬升9.99cm；确证LeRobot成功强行terminated=True；确证终态动作块已规划释放(-1.0)；Workbench上线三层隔离监控与历史回放 | [技术报告](docs/task018_grasp_monitor_and_release.md) · [验收报告](docs/task018_grasp_monitor_and_release_acceptance.md) | **官方 3/3 成功，杯1释放通过，杯2因环境终止未下发张开** |

## 标准工作流

1. ChatGPT 发布 **一个** [TASK] Issue，写明目标、边界和验收。
2. Antigravity 打开此仓库的 [接力规范](docs/remote_task_relay.md) 与唯一未完成 Issue；检查本地工程和上游证据，再回评论 STATUS: RUNNING。
3. 在独立工作分支只执行该任务；更新 docs/、
esults/、evidence/ 和发布清单。
4. 上传 commit/PR 及原始证据，评论 STATUS: REVIEW；无法完成时评论 STATUS: BLOCKED。
5. 由 ChatGPT 与用户审核后标记 STATUS: ACCEPTED，再关闭 Issue、发布下一个任务。

**只领取标题含 [TASK] 且前置依赖已完成的 Issue。** Issue #1 已独立审查并以有限边界关闭；当前 Issue #2（Task018）开发归档已完成，处于 STATUS: REVIEW 等待外部验收。

**不要因为 Issue 状态被标为完成，就自动重跑模型或立即展开下一阶段。**
