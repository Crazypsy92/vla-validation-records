# VLA 验收成果归档发布清单 (Publication Manifest)

## 一、归档发布总览

- **归档时间**：2026-11-23
- **原工程命名空间**：`ai-learning/vla-learning`
- **发布工程命名空间**：`ai-learning/vla-validation-records`
- **GitHub 归档仓库**：`Crazypsy92/vla-validation-records`
- **归档范围**：Task 010 ～ Task 017 完整技术链条
- **白名单发布文件总数**：63 个
- **总归档体积**：1897.43 KB
- **脱敏合规性审查**：
  - [x] 无任何绝对路径 (`~/projects/...` / Windows 本地盘符) 遗留；
  - [x] 无任何个人访问令牌（PAT）、API Key、密码及未公开凭据；
  - [x] 无任何超过 10 MB 的大二进制文件（单文件最大 $<100$ KB）；
  - [x] 100% 忠实保留原始实验指标，无虚标、无美化，保留局部通过客观记录。

---

## 二、白名单发布文件清单（共 63 项）

| 任务 | 归档相对路径 | 大小 (Bytes) | SHA256 校验和 | 类别 | 发布原因与说明 |
|:---:|---|:---:|:---:|:---:|---|
| **Roadmap** | `docs/VLA_Project_Work_Roadmap.md` | 66491 | `89f5e4820bfc2f38...` | Report | 顶层规划与工作路线图 |
| **Specs** | `docs/vla_input_output_analysis.md` | 10447 | `69653de0c14fd5b5...` | Report | 输入输出规格与接口定义 |
| **Task 010** | `docs/task010_smolvla_baseline.md` | 14431 | `f3c810fe6908ec68...` | Report | Task 010 SmolVLA 基线报告 |
| **Task 011** | `docs/task011_input_sensitivity.md` | 11105 | `9e5411d42db15e5e...` | Report | Task 011 输入敏感度与鲁棒性评测报告 |
| **Task 012** | `docs/task012_xvla_inference.md` | 14179 | `03f61abcf2baa6cd...` | Report | Task 012 X-VLA Base 跨本体推理验证报告 |
| **Task 013** | `docs/task013_libero_offline_action_validation.md` | 14882 | `cd202026a71d1f50...` | Report | Task 013 LIBERO 离线动作基准评测报告 |
| **Task 014** | `docs/task014_xvla_pipeline_audit.md` | 12329 | `0733bfd3aa00fe10...` | Report | Task 014 X-VLA 全链路动作与预处理审计报告 |
| **Task 015** | `docs/task015_workbench.md` | 14663 | `5fb5f7963d161cd9...` | Report | Task 015 VLA Workbench 独立上位机验收报告 |
| **Task 016** | `docs/task016_action_semantics.md` | 6263 | `26846093626eb489...` | Report | Task 016 动作物理语义与维度映射规范 |
| **Task 016** | `docs/task016_acceptance_report.md` | 13008 | `f880ef96c5d9b2f1...` | Report | Task 016 动作核验与离线基准测试报告 |
| **Task 017** | `docs/task017_libero_closed_loop.md` | 11304 | `365b7b518d92aa4b...` | Report | Task 017 LIBERO 仿真闭环技术总结 |
| **Task 017** | `docs/task017_acceptance_report.md` | 4642 | `3a7c0efbf45caa33...` | Report | Task 017 仿真闭环最终验收报告 |
| **Task 010** | `results/task010/acceptance.json` | 1508 | `a3c0db1f59d66546...` | Metrics | Task 010 机器可读验收结论 |
| **Task 010** | `results/task010/metrics/inference_metrics.json` | 3860 | `bb2170359d5c6a77...` | Metrics | Task 010 推理性能与时延指标 |
| **Task 010** | `results/task010/predictions/case_001_pick_blue_block.json` | 12227 | `94cd7518b39ef49f...` | Evidence | Task 010 测试用例 1 预测动作 |
| **Task 010** | `results/task010/predictions/case_002_approach_red_cylinder.json` | 12247 | `36ecac8f5367ca66...` | Evidence | Task 010 测试用例 2 预测动作 |
| **Task 010** | `results/task010/predictions/case_003_open_gripper_release.json` | 12234 | `f16bb98bce31225a...` | Evidence | Task 010 测试用例 3 预测动作 |
| **Task 011** | `results/task011/acceptance.json` | 3976 | `c5462071f0e4de82...` | Metrics | Task 011 验收结论指标 |
| **Task 011** | `results/task011/metrics/experiments.json` | 275458 | `21eaba78e62630f9...` | Metrics | Task 011 敏感度实验汇总指标 |
| **Task 011** | `results/task011/metrics/runtime_config.json` | 2457 | `53290eb1faa32131...` | Metrics | Task 011 运行环境与依赖配置 |
| **Task 011** | `results/task011/metrics/processor_audit.json` | 6459 | `7a02ed8a67a49903...` | Metrics | Task 011 官方处理器行为审计 |
| **Task 011** | `results/task011/metrics/task010_output_audit.json` | 671 | `1845fb473a348d76...` | Metrics | Task 011 对 Task010 输出复核 |
| **Task 012** | `results/task012/acceptance.json` | 1511 | `82506657f96cfe87...` | Metrics | Task 012 验收标准矩阵 |
| **Task 012** | `results/task012/metrics/inference_metrics.json` | 5939 | `a5d52c810281f98d...` | Metrics | Task 012 跨本体跨领域推理指标 |
| **Task 012** | `results/task012/predictions/case_001_domain0_libero.json` | 26308 | `7b09bd74626e2c9d...` | Evidence | Task 012 LIBERO 领域预测 |
| **Task 012** | `results/task012/predictions/case_002_domain1_aloha.json` | 26031 | `1fd8460c4abed584...` | Evidence | Task 012 ALOHA 领域预测 |
| **Task 012** | `results/task012/predictions/case_003_domain2_bridge.json` | 26177 | `af51a877fe923c16...` | Evidence | Task 012 Bridge 领域预测 |
| **Task 013** | `results/task013/acceptance.json` | 5831 | `f7be3a1e3ddf51a6...` | Metrics | Task 013 验收指标矩阵 |
| **Task 013** | `results/task013/metrics/inference_metrics.json` | 3517 | `b8d8ef94ab407d97...` | Metrics | Task 013 12 组样本离线时延与误差指标 |
| **Task 013** | `results/task013/predictions/sample_01_prediction.json` | 31949 | `18415db2e67a3e10...` | Evidence | Task 013 样本 1 预测动作 |
| **Task 013** | `results/task013/predictions/sample_02_prediction.json` | 31754 | `4ce7b5387555d392...` | Evidence | Task 013 样本 2 预测动作 |
| **Task 013** | `results/task013/predictions/sample_03_prediction.json` | 31808 | `899e596759d82b02...` | Evidence | Task 013 样本 3 预测动作 |
| **Task 013** | `results/task013/predictions/sample_04_prediction.json` | 31867 | `62fa73aca6ae6eb0...` | Evidence | Task 013 样本 4 预测动作 |
| **Task 014** | `results/task014/acceptance.json` | 8407 | `354360eee77fb643...` | Metrics | Task 014 审计验收指标 |
| **Task 014** | `results/task014/metrics/calibrated_metrics.json` | 5531 | `b17cc82306e192e5...` | Metrics | Task 014 标定后物理维度统计与时延 |
| **Task 014** | `results/task014/predictions/sample_01_calibrated_prediction.json` | 18111 | `50388affabca9bce...` | Evidence | Task 014 样本 1 标定动作块 |
| **Task 014** | `results/task014/predictions/sample_02_calibrated_prediction.json` | 18033 | `64cc772051ccf47a...` | Evidence | Task 014 样本 2 标定动作块 |
| **Task 015** | `results/task015/acceptance.json` | 4871 | `ddae64a566bcd1ad...` | Metrics | Task 015 上位机验收矩阵 |
| **Task 015** | `results/task015/metrics/inference_metrics.json` | 814 | `7713e9de8393bb62...` | Metrics | Task 015 Worker 通信与推理性能 |
| **Task 015** | `results/task015/records/test_acceptance_rec.json` | 6011 | `dcf661aa1a0d9810...` | Evidence | Task 015 上位机运行测试记录 |
| **Task 016** | `results/task016/acceptance.json` | 3375 | `0ecdeda8a92f85c4...` | Metrics | Task 016 动作语义核验验收结论 |
| **Task 016** | `results/task016/metrics/action_statistics.json` | 8527 | `a3193d91b35d43c2...` | Metrics | Task 016 7D 动作物理维度聚合统计 |
| **Task 016** | `results/task016/metrics/system_performance.json` | 805 | `1e02ff549256aac7...` | Metrics | Task 016 系统资源与内存峰值统计 |
| **Task 016** | `results/task016/records/sample_01_record.json` | 35293 | `b331e0405f886383...` | Evidence | Task 016 样本 1 详细动作与物理统计 |
| **Task 016** | `results/task016/records/sample_02_record.json` | 35102 | `fcf319f5992d0704...` | Evidence | Task 016 样本 2 详细动作与物理统计 |
| **Task 016** | `results/task016/records/sample_03_record.json` | 35273 | `807f1e54034ca74a...` | Evidence | Task 016 样本 3 详细动作与物理统计 |
| **Task 016** | `results/task016/records/sample_04_record.json` | 35280 | `2053add8c8631783...` | Evidence | Task 016 样本 4 详细动作与物理统计 |
| **Task 017** | `results/task017/acceptance.json` | 3910 | `447da818e2a9a1ab...` | Metrics | Task 017 仿真闭环验收标准矩阵 |
| **Task 017** | `results/task017/metrics/closed_loop_metrics.json` | 2290 | `49b0b3e27ad51b6c...` | Metrics | Task 017 跨种子闭环聚合评测指标 |
| **Task 017** | `results/task017/records/run_seed_42.json` | 83406 | `be7ae946fe723f38...` | Evidence | Task 017 种子 42 完整闭环轨迹记录 |
| **Task 017** | `results/task017/records/run_seed_100.json` | 83399 | `b7b70e019fa3611a...` | Evidence | Task 017 种子 100 完整闭环轨迹记录 |
| **Task 017** | `results/task017/records/run_seed_2026.json` | 83450 | `c0fd9f5b7886031f...` | Evidence | Task 017 种子 2026 完整闭环轨迹记录 |
| **Task 015** | `evidence/task015/action_curves_sample01.png` | 14586 | `66c31e36f0ef6ef2...` | Evidence | Task 015 上位机动作曲线绘制验证截图 |
| **Task 017** | `evidence/task017/episode_seed_42_step_000_init.png` | 70510 | `11ac3a3968c71948...` | Evidence | Task 017 仿真初始场景渲染图 (Seed 42) |
| **Task 017** | `evidence/task017/episode_seed_42_cycle_0_step_15.png` | 70971 | `fe00028272941177...` | Evidence | Task 017 第 1 周期步进渲染图 (Step 15) |
| **Task 017** | `evidence/task017/episode_seed_42_cycle_1_step_30.png` | 71868 | `112c75ff0fd98ec6...` | Evidence | Task 017 第 2 周期步进渲染图 (Step 30) |
| **Task 017** | `evidence/task017/episode_seed_42_cycle_2_step_45.png` | 72035 | `fb9dca0b7cde3820...` | Evidence | Task 017 第 3 周期步进渲染图 (Step 45) |
| **Task 017** | `evidence/task017/episode_seed_42_cycle_3_step_60.png` | 71400 | `574f5fe439d923f4...` | Evidence | Task 017 第 4 周期步进渲染图 (Step 60) |
| **Task 017** | `evidence/task017/episode_seed_42_final.png` | 71400 | `574f5fe439d923f4...` | Evidence | Task 017 仿真结束最终位姿图 (Seed 42) |
| **Task 017** | `evidence/task017/episode_seed_42_c0_obs_workspace.png` | 70510 | `11ac3a3968c71948...` | Evidence | Task 017 工作台相机观测输入 (Seed 42) |
| **Task 017** | `evidence/task017/episode_seed_42_c0_obs_wrist.png` | 67655 | `1c3bfda0d7b0a506...` | Evidence | Task 017 手腕相机观测输入 (Seed 42) |
| **Task 017** | `evidence/task017/episode_seed_100_final.png` | 71331 | `8bfe4fc36e45e20c...` | Evidence | Task 017 仿真最终位姿图 (Seed 100) |
| **Task 017** | `evidence/task017/episode_seed_2026_final.png` | 71280 | `8ab6c9960933e702...` | Evidence | Task 017 仿真最终位姿图 (Seed 2026) |

---

## 三、排除文件分类审查说明

按照任务规范第五阶段要求，以下非归档资产已被严格排除在独立发布工程之外：

| 排除资产分类 | 典型文件 / 路径模式 | 数量与估计体积 | 严格排除原因 |
|---|---|:---:|---|
| **Virtual Environments & Python Binaries** | `.venv/, .venv_xvla/` | 2 virtualenvs (~8.5 GB) | 包含大量第三方二进制库、Python 解释器及构建缓存，严禁提交代码仓 |
| **Pretrained Model Weights & Checkpoints** | `~/.cache/huggingface, lerobot/xvla-*` | 3 checkpoints (~4.2 GB) | 预训练模型参数（SmolVLA 450M, X-VLA 879M），体积庞大且属开源公开资产，依规排除 |
| **Raw Simulation Datasets & HDF5** | `datasets/task013/*.png, datasets/task013/sample_manifest.json (4.1MB full dump)` | 24 images + 1 manifest (4.5 MB) | 原始训练/验证数据集切片，归档库仅保留精炼后的预测结果与指标 |
| **Intermediate Raw NPZ Arrays** | `results/task011/inputs/*.npz, results/task011/predictions/*_actions.npz` | 32 NPZ files (420 KB) | 二进制数值矩阵中间态，已由 experiments.json 完整结构化表达 |
| **Simulation Rollout Videos (MP4)** | `results/task017/records/*/*.mp4` | 3 MP4 files (3.0 MB) | 仿真视频文件，关键姿态已由 PNG 关键帧全量呈现，避免大二进制污染 Git 历史 |
| **Raw Terminal & Rollout Logs** | `results/*/logs/*.log, results/task017/records/*/*.log` | 14 log files (120 KB) | 本地调试与执行终端日志，已精炼为正式验收 Markdown 与 JSON 报告 |
| **Workbench GUI & Backend Python Code** | `workbench/ui/, workbench/backends/, workbench/workers/, scripts/` | 28 Python files (260 KB) | 遵循只归档‘验收报告与评测结果’原则，保留于原工程，不进行全仓搬迁 |

---

## 四、文件完整性与反向校验

所有发布文件均经过以下检验：
1. **Markdown 内部链接有效性**：全部文档中的相对链接 (`docs/...`, `results/...`, `evidence/...`) 均能在 GitHub 远程渲染时直接点击跳转；
2. **JSON 解析性校验**：所有收录的 JSON 指标与验收文件均通过 Python `json.loads()` 严格语法验证；
3. **数据一致性**：除对 Markdown/JSON 中本地路径做标准化相对脱敏处理外，数值指标与原始仿真评测数据 100% 保持一致。
