# Task022-B index34 单次诊断回放

**结论为 `BLOCKED_RESOURCE`，已达到原内存保护条件。** 本轮启动 1 次 Worker、完成 1 次官方 Reset 和 1 次模型加载，预测 0 次，执行 0 个控制步，重试 0 次。Step 150–300 覆盖 **0/151**。官方成功状态未评估，诊断不计入成功率。

## 基线与命令

Task021 的 index34 原失败回合和 index15 对照记录由 Task022-A 清单固定。两个回合的列明本机历史文件重新计算了 SHA256。本机和发布基线中的两回合核心文件逐字节对照了 10 项。原控制器、环境包装、模型后端及资源保护源码保持原样。

- 固定 checkpoint revision 为 `8e6aeef01f634f5d3b5be4340328f19cc2c25a65`。完整权重及 Processor 文件大小和 SHA256 与原配置一致。
- 使用官方 LIBERO-10 Task 5、index 34 / Reset RNG 201。Prompt、BDDL、原始状态 SHA256 和 Reset 双视角 RGB 指纹均通过核对后才加载模型。
- 配置为原 8D→9D、20D→7D、absolute OSC_POSE 20 Hz、30 步 Action Chunk。没有向这些接口下发新动作。
- 配置 SHA256 为 `9f63d96cd65cfc2d297efbe0d6fd6897bcc9a00dc3b0cf0658d8c895224980e7`。
- 官方状态行 SHA256 为 `8eb7e4b31ba84c940aad7fb50aff0ccb4a26f36495c2ca6986c77e890934ef84`。
- Run ID 为 `diagnostic_index_34_rng_201_1795571278349401651`。

在原 Workbench 工程根目录使用了现有 Worker 的 CLI 入口。为了让真实 Reset 也在模型加载前校验，诊断包装器把同一次 Reset 提前并保留其随机数状态，随后与模型同时保留环境实例。该生命周期顺序与原 GUI 回合不同，可能提高模型加载阶段的内存占用，当前没有受控数据衡量此影响。没有修改原 Worker 文件。诊断入口及实际命令见下方链接。

```text
.venv_xvla/bin/python -u scripts/task022_index34_diagnostic.py --task021-b2b --official-initial-state-index 34 --reset-rng-seed 201 --seed 201 --directory ./results/task022/b/runs/diagnostic_index_34_rng_201_1795571278349401651
```

[Task022-B 历史诊断脚本](https://github.com/Crazypsy92/vla-validation-records/blob/e437162a365f99bbd849b596f4ef80f711cebf0e/results/task022/b/diagnostic_runner.py) · [当前规范入口](../scripts/task022_index34_diagnostic.py) · [真实启动命令](../results/task022/b/logs/launch.json) · [退出记录](../results/task022/b/logs/exit.json) · [基线指纹](../results/task022/b/logs/preflight.json) · [原任务离线审计](task022_index34_failure_forensics.md)

## 实际停止点与轨迹对照

监督器首次触发原 `under_pressure` 阈值时，WSL 可用内存为 **445 MiB**，低于 512 MiB，进程 RSS 为 4579 MiB。全程监督采样的可用内存最低 165 MiB，Swap 剩余最低 0 MiB，Worker 采样 RSS 峰值 6541 MiB。正在进行的模型加载返回后，Worker 在 `after_model_load` 检查点读取压力标记并退出，退出码 **0**。退出后 WSL 可用内存 6364 MiB。没有进入推理、动作执行或录像阶段。

Step 0 的书本和末端位置误差均为 0 m，姿态误差均为 0°。Step 30、60、90、120、150 及其余 Step160 前的运动对照未到达。只能确认初始场景一致，运动轨迹是否分叉无法判断。

[逐步对照](../results/task022/b/logs/reproduction.jsonl) · [监督资源日志](../results/task022/b/logs/resources_supervisor.jsonl) · [Worker 检查点](../results/task022/b/logs/resources_worker.jsonl) · [资源曲线](../evidence/task022/b/resource_pressure.png) · [Reset Workspace](../evidence/task022/b/0000_workspace.png) · [Reset Wrist](../evidence/task022/b/0000_wrist.png)

## 遥测与诊断边界

从当前代码确认 OSC 的计算输出由 SingleArm 用关节扭矩限值剪裁后才写入 actuator ctrl。只读诊断钩子计划在每次控制器调用记录限幅前后的结果，并于 20 Hz 控制步边界读取 MuJoCo 实际接触和世界位姿。安装的仿真步长为 2 ms。该分辨率下的边界接触样本不能推导整个控制区间的接触冲量。未执行控制步，所以钩子只记录了 geom ID 和来源配置，扭矩、接触、动态 site 和执行轨迹均没有样本。本回合唯一图片是两张原始 Reset 帧，未生成执行轨迹图或录像。图表记录的是本次实际资源变化。

| 问题 | 结论 | 本轮缺失证据 |
| --- | --- | --- |
| B1 策略目标方向 | INCONCLUSIVE | 没有诊断窗口的模型动作、OSC 目标或目标局部误差 |
| B2 控制限幅与跟踪 | INCONCLUSIVE | 没有动作后扭矩、限幅、关节反馈或跟踪误差 |
| B3 抓持相对变换 | INCONCLUSIVE | 没有抓持过程的 book-in-EEF 变换序列 |
| B4 隔板与侧壁接触 | INCONCLUSIVE | 没有对准过程的实际 geom 对、法向、距离或接触力 |

Task022-A 的根因结论仍为 `ROOT_CAUSE_UNDETERMINED`。本轮记录保留成功完成的基线核对及资源中断证据，未追加回合。

[验收 JSON](../results/task022/b/acceptance.json) · [统计 JSON](../results/task022/b/metrics/summary.json) · [遥测元数据](../results/task022/b/logs/diagnostic.jsonl) · [Issue #12](https://github.com/Crazypsy92/vla-validation-records/issues/12)
