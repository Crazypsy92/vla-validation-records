# Task022-C index34 资源生命周期预检

> Issue #16 续跑结果为 `PASS`，见 [续跑报告](task022_index34_resource_resume.md)。以下保留第一次 C3 启动门禁的原始判读。

**结果为 `BLOCKED_RESOURCE`。** C1 静态预检和 C2 独立 Reset 通过。C3 启动门禁拒绝，因为 Swap 仅剩 **348 MiB**，低于 **1024 MiB**。同次采样的 WSL 可用内存为 **6381 MiB**，达到 3072 MiB 的 RAM 门槛。C3 子进程未启动。

本轮共执行 1 次官方 Reset、0 次模型加载、0 次模型前向、0 个评测控制步和 0 次重试。官方 Reset 内置的 10 个稳定步骤保留，入口未调用外层 `env.step`。Task022-B 的实验记录保持 `REVIEW / BLOCKED_RESOURCE`，Task022-D 尚未授权。

## C1 入口和基线

规范入口为归档仓库的 `scripts/task022_index34_diagnostic.py`。它从脚本位置解析归档目录，接受显式的 Workbench 根目录，并验证输出路径可新建。旧入口移出当前树，Task022-B 报告指向包含旧脚本的原提交。C1 分别从归档仓库根目录、Workbench 根目录和 `/tmp` 实际执行，三个退出码均为 0，输出的基线 JSON 逐字节相同。静态模式没有创建仿真环境或加载模型。

本机历史 index34 的 82 项文件按 Task022-A 清单校验。另核对 Task022-B 历史预检、配置、Reset 对照和回合状态，用已安装源文件、固定 checkpoint 与 Processor 的 SHA256 验证基线。C2 的 Prompt、BDDL、官方初始状态及其资产和双视角 RGB 指纹一致。

- Run ID `preflight_index34_1795574666075878409`
- checkpoint revision `8e6aeef01f634f5d3b5be4340328f19cc2c25a65`
- 配置 SHA256 `9f63d96cd65cfc2d297efbe0d6fd6897bcc9a00dc3b0cf0658d8c895224980e7`
- 官方 index34 状态 SHA256 `8eb7e4b31ba84c940aad7fb50aff0ccb4a26f36495c2ca6986c77e890934ef84`

[规范入口](../scripts/task022_index34_diagnostic.py) · [实际命令](../results/task022/c/logs/lifecycle/launch.json) · [跨目录命令与退出码](../results/task022/c/logs/static_checks.json) · [基线指纹](../results/task022/c/logs/lifecycle/baseline.json)

## C2 独立 Reset

使用 LIBERO-10 Task 5、官方 index34、RNG201 执行一次 Reset。成功比对原 Task021、Task022-B 和 Task021 状态清单。官方环境关闭之后包装层内部环境引用已释放，子进程退出码为 0。父进程在子进程退出后再次采样。

| 指标 | 子进程启动前 | C2 最低值 | 子进程退出后 |
| --- | ---: | ---: | ---: |
| WSL 可用 RAM (MiB) | 6172 | 4267 | 6381 |
| SwapFree (MiB) | 356 | 348 | 348 |

独立 C2 子进程采样 RSS 峰值为 2359 MiB，PSS 峰值为 2354 MiB。环境和进程的关闭已确认。系统可用 RAM 和 Swap 受其他 WSL 进程及文件缓存变化影响，表内差值为全局采样。

[Reset 结果](../results/task022/c/logs/lifecycle/reset_only/result.json) · [进程退出](../results/task022/c/logs/lifecycle/reset_only/exit.json) · [资源曲线](../evidence/task022/c/reset_resource_curve.png) · [Workspace](../evidence/task022/c/0000_workspace.png) · [Wrist](../evidence/task022/c/0000_wrist.png)

## C3 组合预检

C3 独立进程的启动门禁保留了原资源保护并增加 RAM ≥3072 MiB、SwapFree ≥1024 MiB 的要求。Swap 的缺口为 **676 MiB**，因此本次资源条件不足以启动组合预检。后置门禁设为 RAM ≥1536 MiB、SwapFree ≥512 MiB，本次未到达。

当前没有模型单独加载的阶段峰值、组合工作集或 C3 Reset 指纹。无法判断模型单独加载能否安全完成，也无法判断组合 Reset 或之后的诊断能否安全运行。原 Task022-B 的加载峰值来自环境已驻留的生命周期，不能作为本轮模型优先的峰值证据。已知基线结果和本次门禁拒绝均按原样归档。

[启动门禁](../results/task022/c/logs/lifecycle/combined/gates.jsonl) · [未启动子进程记录](../results/task022/c/logs/lifecycle/combined/exit.json) · [验收 JSON](../results/task022/c/acceptance.json) · [统计 JSON](../results/task022/c/metrics/summary.json)
