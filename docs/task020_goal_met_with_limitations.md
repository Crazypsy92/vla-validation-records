# Task020 结题说明

**阶段结论为 `GOAL_MET_WITH_LIMITATIONS`，待审核。** 现有证据证明 `lerobot/xvla-libero` 可通过 Windows 桌面 VLA Workbench，在官方 LIBERO-10 Task 5 中完成将书本放入收纳盒后格的任务。验收依据是 LIBERO 的 `is_success` 与正式回合终止记录。

## 正式回合结果

| Seed | 实际仿真步数 | 真实前向次数 | 官方结果 | 物理释放 |
| --- | ---: | ---: | --- | --- |
| 201 | 169 | 6 | 成功，终止步 `is_success=true` | 未验证 |
| 202 | 183 | 7 | 成功，终止步 `is_success=true` | 未验证 |
| 203 | 191（Phase 4） | 7 | 无官方终态，触发资源保护并安全停止 | 未验证 |

三个计划种子的统计为 **2 个官方成功、1 个未完成**。Seed 203 不计入成功或模型失败。此前 Seed 203 还有两次中断，其中一次有 WSL 全局 OOM 记录。Phase 4 没有新增 OOM kill。Phase 4 归档中的原始 T04、R1-06 和 P4-03 保留 `BLOCKED_RESOURCE`。

## 证据与范围

- Seed 201 和 202 的正式结果已逐一核对本机原始 `summary.json` 和 `events.jsonl` 的终止步。原始试点报告及验收摘要保留在既有书本试点分支，逐步记录和录像保存在本机工程的 `results/task020/records/seed_201/`、`results/task020/records/seed_202/`。 [原始试点报告](https://github.com/Crazypsy92/vla-validation-records/blob/a712f3071349f0c1de2bb0b75dd7d7226d6a7590/docs/task020_workbench_book_pilot.md) · [试点验收摘要](https://github.com/Crazypsy92/vla-validation-records/blob/a712f3071349f0c1de2bb0b75dd7d7226d6a7590/results/task020/acceptance.json)
- Phase 2 验证完整检查点可从 GUI 加载并驱动仿真。Phase 3 验证连续使用新观测完成三次前向、执行 90 步，以及回放和 Worker 清理。两轮短测用于核对工程链路。 [Phase 2 短测](task020_r1_phase2_results.md) · [Phase 3 闭环验证](task020_r1_phase3_results.md)
- Phase 4 的 (Seed 203) 正式尝试、资源中断、局部回放和逐项阻断状态已在 `main` 归档。 [Phase 4 报告](task020_r1_phase4_seed203_results.md) · [Phase 4 验收矩阵](../results/task020/r1/phase4/acceptance.json)

此结论适用于当前任务的官方判定。三种子完整覆盖和物理松爪仍待验证。若日后需要 Seed 203 的完整结果，可单独评估资源预算并经用户批准后调整资源配额，保留现有内存保护。 [验收口径更新](https://github.com/Crazypsy92/vla-validation-records/issues/4#issuecomment-7101776511)
