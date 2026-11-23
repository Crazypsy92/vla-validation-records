# VLA GitHub ↔ Antigravity 任务接力规程

> **默认状态 OFF：仅手动触发；目前未创建或启用任何定时计划。** 本文只定义工作契约，不能远程唤醒本地 Antigravity。
>
> 仓库：`Crazypsy92/vla-validation-records`，主分支 `main`。**GitHub Issues 是唯一正式派发入口**；`TASKS.md` 只是索引。

## 一、边界与定位

- **GitHub**：有限规模的验收证据、任务、Issue、PR、报告和精选截图。
- **本地工程**：`ai-learning/vla-learning`，保存 LeRobot/X-VLA、测试脚本、数据集缓存、模型权重、全量原始产物。
- **Antigravity**：负责在本地核查和执行任务，不能把“已经发 Issue”当成“已经运行成功”。
- **ChatGPT / 用户**：按报告与可追溯原始证据评审；未验证的项目不标 ACCEPTED。

## 二、Antigravity 手动读取流程（默认）

1. 阅读本文件、`TASKS.md`、README 和仓库未关闭的 `[TASK]` Issues。
2. 只领取**一个**满足前置条件的任务；不得重复领取已标 `RUNNING`、`REVIEW` 或 `BLOCKED` 的 Issue。
3. 核实当前工作区、`git status`、分支、远程与待提交更改；不要覆盖未提交工作、不要强制推送。
4. 在 Issue 记录 `STATUS: RUNNING`、工作区、基线提交与本轮范围。
5. 在本地工程执行经授权的软件实验或证据整理，保持模型权重与历史报告不变。不要擅自连接或控制真实机器人、机械臂、相机硬件。
6. 仅将精选的可公开/可存放于本私有仓库的材料同步到归档库；形成 PR/commit、原始统计和发布清单。
7. 在 Issue 记录 `STATUS: REVIEW`、真实测试命令与退出码、commit/PR、报告路径、未完成项。资料缺失则 `STATUS: BLOCKED`，说明原因后停止。
8. 等待审查，不自动开展下一 Task。任何新阶段必须有新的 Issue。

## 三、状态协议

| 状态 | 意义 |
| --- | --- |
| OPEN | 任务已发布，尚未领取 |
| `STATUS: RUNNING` | 已核实工作区，开始当前任务 |
| `STATUS: REVIEW` | 有可核实的产物、日志和 commit/PR，待验收 |
| `STATUS: BLOCKED` | 缺数据、权限、依赖、真实日志或测试失败，停止自动推进 |
| `STATUS: ACCEPTED` | 经过外部审核，符合本轮明确定义的验收标准 |

区分 `PIPELINE_PASS`、`SIM_TASK_SUCCESS`、`FULL_RELEASE_SUCCESS`、`REAL_ROBOT_VALIDATED`；不允许互相替代。尤其 Task017 初期 60 步 0/3 与新版完整回合 3/3 属不同测试版本，均应保留原始记录。

## 四、提交与安全

- GitHub 仓库不保存 `.venv`、权重、数据集/仿真第三方资产、大视频、临时缓存、Token、内部网络地址、敏感工作资料。
- 只允许白名单发布：Markdown 报告、机器可读验收 JSON、精选低体积图片、必要的小规模匿名日志；提交前检查内容许可。
- 本地原工程的历史报告、原始数据和 Git 历史禁止覆盖。任何编辑必须能追溯原始源文件。
- 对旧版本结果进行补充时，增加版本或阶段标注，不覆盖证据、偷偷修改指标或擦掉失败记录。
- 优先通过独立分支和 PR 交付；不能提交 PR 时附可检查的 commit 和变更路径。
- 改动 README、`TASKS.md`、`manifests/publication_manifest.json` 时必须核实新旧链接及实际 SHA，不能把未验证摘要登记为已验收结果。

## 五、如需将来启用定时任务

本仓库**没有配置定时接力**。未来只有用户明确要求后才考虑 Antigravity 的定时功能；本机 IDE、会话、网络、休眠、权限均需独立验证。禁止默认无人值守启动模型、批量实验或机器人控制，也不得复制 RTOS 项目的硬件烧录授权到本项目。

## 六、首次在 Antigravity 工程对话中手动发送

```text
请打开 GitHub 仓库 Crazypsy92/vla-validation-records，先读取 main 分支 docs/remote_task_relay.md 和 TASKS.md，再读取当前唯一开放的 [TASK] Issue。核对本地 ai-learning/vla-learning 工程、git 状态和历史验收记录。只执行该 Issue 范围的工作，先在 Issue 评论 STATUS: RUNNING；完成后以独立分支/PR 或可核对的 commit 提交精选资料、真实指标和发布清单，评论 STATUS: REVIEW。任何原始证据缺失或冲突就标 STATUS: BLOCKED 并停止；不要擅自重跑模型，不接入真实机器人，不自动进行下一阶段任务。
```
