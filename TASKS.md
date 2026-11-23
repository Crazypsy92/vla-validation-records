# VLA 任务状态与验收索引

> **任务唯一入口为 GitHub Issues**；此文件只保留导航和已审核的状态摘要。Antigravity 不应仅凭 README 自动启动实验。
>
> **默认接力状态：OFF（按需手动执行）。** 发布 Issue 不会自动启动本机 IDE、定时计划或 GPU 任务。

## 当前任务

| ID | 任务 | Issue | 状态 | 下一步 |
| --- | --- | --- | --- | --- |
| Task017-R2 | 补齐新版 Task 017 完整闭环验收证据 | [#1](https://github.com/Crazypsy92/vla-validation-records/issues/1) | OPEN / 待领取 | Antigravity 只读审计并归档已有资料 |
| Task018 | **夹爪抓取/保持/释放验证 + VLA Workbench 监控回放（合并）** | [#2 方案](https://github.com/Crazypsy92/vla-validation-records/issues/2) | PLANNED / 不可领取 | Issue #1 经审核后把 #2 从 `[PLAN]` 激活为 `[TASK]` |

## 历史归档

| 范围 | 内容 | 已归档证据 | 重要边界 |
| --- | --- | --- | --- |
| Task010–011 | SmolVLA 离线推理与输入敏感性 | [docs](docs/) · [results](results/) | 不等于动作语义正确 |
| Task012–014 | X-VLA 推理、LIBERO 数据与动作处理审计 | [docs](docs/) · [results](results/) | 不等于真机任务成功 |
| Task015–016 | 独立 VLA Workbench 与动作语义核查 | [docs](docs/) · [results](results/) | 上位机为离线模型验证 |
| Task017（初期） | 60 步三种子闭环，软件 3/3、任务 0/3 | [技术报告](docs/task017_libero_closed_loop.md) · [验收](docs/task017_acceptance_report.md) | **仅初期 60 步测试，不是较新完整任务测试** |
| Task017（完整回合） | 用户汇报 3/3 任务成功、但第二只杯子未主动释放 | [#1 待归档](https://github.com/Crazypsy92/vla-validation-records/issues/1) | **原始报告和指标待核验，暂不标为仓库 ACCEPTED** |

## 标准工作流

1. ChatGPT 发布 **一个** `[TASK]` Issue，写明目标、边界和验收。
2. Antigravity 打开此仓库的 [接力规范](docs/remote_task_relay.md) 与唯一未完成 Issue；检查本地工程和上游证据，再回评论 `STATUS: RUNNING`。
3. 在独立工作分支只执行该任务；更新 `docs/`、`results/`、`evidence/` 和发布清单。
4. 上传 commit/PR 及原始证据，评论 `STATUS: REVIEW`；无法完成时评论 `STATUS: BLOCKED`。
5. 由 ChatGPT 与用户审核后标记 `STATUS: ACCEPTED`，再关闭 Issue、发布下一个任务。

**只领取标题含 `[TASK]` 且前置依赖已完成的 Issue。** Issue #2 目前为 `[PLAN]`，不得与 #1 并行开发或自动领取；待 #1 独立审查通过再激活。

**不要因为 Issue 状态被标为完成，就自动重跑模型或立即展开下一阶段。**
