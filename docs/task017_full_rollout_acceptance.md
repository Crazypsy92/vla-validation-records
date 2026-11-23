# Task 017 完整闭环长程测试验收报告 (Full Rollout Acceptance Report)

## 一、验收结论总览

依据 GitHub Issue #1 与 [接力规范](remote_task_relay.md) 要求，对 Task 017 完整长程测试（Full Rollout）的原始数据、指标文件与行为轨迹完成全面审计。

| 验收维度 | 验收判定 | 实测证据与量化指标 | 归档定位与边界说明 |
|:---:|:---:|---|---|
| **软件流水线健康度** | **PASS** | 3 个种子共 24 次 X-VLA 前向推理与 664 个仿真物理步进，零异常中断 | 软件闭环链路 100% 畅通 |
| **LIBERO 官方任务判定** | **PASS** | Seed 142/143/144 全部达到 BDDL 状态判定，`is_success = 3/3 (100%)` | 满足官方长程双目标放置基准 |
| **第一阶段操作闭环** | **PASS** | 白杯稳定拾取并放置至左盘，在 Step 97~102 成功执行主动张爪释放 | 抓取-搬运-释放完整闭环 |
| **第二阶段操作闭环** | **PARTIAL** | 黄白杯稳定拾取并送达右盘，终态距目标盘中心 $<2.8\text{ cm}$，但环境在送达时刻立即判定成功并终止，未产生张爪动作 | 搬运到位，但主动释放未被观察到 |
| **原始数据真实可追溯性** | **PASS** | 3 份单回合 `summary.json`、`manipulation.json`、`episodes.json` 均源自本地真实仿真产物 | 严禁人为虚标或篡改数据 |

**综合验收评定：STATUS: ACCEPTED (附边界说明)**  
*注：本验收报告核实并承认官方 3/3 成功，但严格限定该成功并不等同于第二只杯子已完成主动松爪。*

---

## 二、双版本测试对照表（初期 60 步 vs 完整回合）

为彻底消除理解歧义，本仓库对 Task 017 的两个测试阶段做如下明确版本切分：

| 对比维度 | Task 017 初期探索版本 | Task 017 完整长程测试版本 (本报告) |
|---|---|---|
| **定位与目的** | 初步验证控制接口与多轮闭环可行性 | 验证双目标物体长程完整拾取与放置能力 |
| **评测随机种子** | `seed=42`, `seed=100`, `seed=2026` | `seed=142`, `seed=143`, `seed=144` |
| **执行步数 / 轮数** | 每回合固定 60 步（4 轮推理，共 180 步） | 动态步进至成功，平均 221.3 步（8 轮推理，共 664 步） |
| **LIBERO 官方判定** | **0/3 (0%)**（步数不足，尚未到达目标） | **3/3 (100%)**（双杯全部送达指定托盘） |
| **第一只杯抓放** | 仅下探趋近白杯 | **完整完成（抓取 $\to$ 搬运 $\to$ 主动释放）** |
| **第二只杯抓放** | 未触及 | **抓取并搬运到位，因环境终止未执行张爪** |
| **对应技术文档** | [task017_libero_closed_loop.md](task017_libero_closed_loop.md) | [task017_full_rollout.md](task017_full_rollout.md) |
| **对应验收报告** | [task017_acceptance_report.md](task017_acceptance_report.md) | **本报告（task017_full_rollout_acceptance.md）** |

---

## 三、关键指标核验矩阵

```json
{
  "task": "Task017-R2: Full Rollout Closed-Loop Validation",
  "task_suite": "libero_10",
  "task_id": 4,
  "model": "lerobot/xvla-libero",
  "seeds_evaluated": [142, 143, 144],
  "episodes_count": 3,
  "total_inferences": 24,
  "total_sim_steps": 664,
  "official_success_rate": 1.0,
  "mug1_full_release_success": true,
  "mug2_terminal_gripper_command": 1.0,
  "mug2_release_verified": false,
  "conclusion": "ACCEPTED_WITH_GRIPPER_RELEASE_BOUNDARY"
}
```

---

## 四、归档资产与证据链接

1. **详细技术总结**：[task017_full_rollout.md](task017_full_rollout.md)
2. **多物体接触与位移指标**：[manipulation.json](../results/task017/metrics/manipulation.json)
3. **聚合回合指标**：[episodes.json](../results/task017/metrics/episodes.json)
4. **单回合详细记录**：
   - [Episode 00 Summary](../results/task017/records/episode_00_seed_142/summary.json)
   - [Episode 01 Summary](../results/task017/records/episode_01_seed_143/summary.json)
   - [Episode 02 Summary](../results/task017/records/episode_02_seed_144/summary.json)
5. **关键帧证据图像**：
   - 初始状态图：[full_rollout_ep00_0000_init.png](../evidence/task017/full_rollout_ep00_0000_init.png)
   - 第一只杯放置与释放图：[full_rollout_ep00_0090_mug1_placed.png](../evidence/task017/full_rollout_ep00_0090_mug1_placed.png)
   - 终态成功时刻图：[full_rollout_ep00_0223_final_success.png](../evidence/task017/full_rollout_ep00_0223_final_success.png)
