# VLA 验收成果归档发布清单 (Publication Manifest)

## 一、归档发布总览

- **归档时间**：2026-11-23
- **原工程命名空间**：`ai-learning/vla-learning`
- **发布工程命名空间**：`ai-learning/vla-validation-records`
- **GitHub 归档仓库**：`Crazypsy92/vla-validation-records`
- **归档范围**：Task 010 ～ Task 019 完整技术链条，以及 Task020 书本试点和 R1 第一阶段
- **白名单发布文件总数**：140 个
- **总归档体积**：6176.11 KB
- **脱敏合规性审查**：
  - [x] 无任何绝对路径（`~/projects/...` / Windows 本地盘符）遗留；
  - [x] 无任何个人访问令牌（PAT）、API Key、密码及未公开凭据；
  - [x] 无任何超过 10 MB 的大二进制文件；
  - [x] 保留原始实验指标与失败边界，不虚标、不美化。

---

## 二、白名单发布文件清单（共 140 项）

| 任务 | 归档相对路径 | 大小 (Bytes) | SHA256 校验和 | 类别 | 发布说明 |
|:---:|---|:---:|:---:|:---:|---|
| **General** | `.gitignore` | 357 | `2c4084d6d8b90c9c...` | Config | 发布归档文件 |
| **General** | `README.md` | 14651 | `689111aaa5ca45cf...` | Config | 书本试点 |
| **General** | `TASKS.md` | 4969 | `a49d508a45b5dcb6...` | Config | R1 第一阶段 |
| **Docs** | `docs/VLA_Project_Work_Roadmap.md` | 66491 | `89f5e4820bfc2f38...` | Report | 发布归档文件 |
| **Docs** | `docs/remote_task_relay.md` | 4515 | `36ca245be0f78903...` | Report | 发布归档文件 |
| **Docs** | `docs/task010_smolvla_baseline.md` | 14431 | `f3c810fe6908ec68...` | Report | 发布归档文件 |
| **Docs** | `docs/task011_input_sensitivity.md` | 11105 | `9e5411d42db15e5e...` | Report | 发布归档文件 |
| **Docs** | `docs/task012_xvla_inference.md` | 14179 | `03f61abcf2baa6cd...` | Report | 发布归档文件 |
| **Docs** | `docs/task013_libero_offline_action_validation.md` | 14882 | `cd202026a71d1f50...` | Report | 发布归档文件 |
| **Docs** | `docs/task014_xvla_pipeline_audit.md` | 12329 | `0733bfd3aa00fe10...` | Report | 发布归档文件 |
| **Docs** | `docs/task015_workbench.md` | 14663 | `5fb5f7963d161cd9...` | Report | 发布归档文件 |
| **Docs** | `docs/task016_acceptance_report.md` | 13008 | `f880ef96c5d9b2f1...` | Report | 发布归档文件 |
| **Docs** | `docs/task016_action_semantics.md` | 6263 | `26846093626eb489...` | Report | 发布归档文件 |
| **Docs** | `docs/task017_acceptance_report.md` | 5110 | `fbf821f2e5c9da97...` | Report | 发布归档文件 |
| **Docs** | `docs/task017_full_rollout.md` | 8156 | `4ce145b26aa99b29...` | Report | 发布归档文件 |
| **Docs** | `docs/task017_full_rollout_acceptance.md` | 4418 | `38e0035be4181f6b...` | Report | 发布归档文件 |
| **Docs** | `docs/task017_libero_closed_loop.md` | 11809 | `fae551a5d9fd92ca...` | Report | 发布归档文件 |
| **Docs** | `docs/task018_grasp_monitor_and_release.md` | 13998 | `5e2f7836596c751d...` | Report | 发布归档文件 |
| **Docs** | `docs/task018_grasp_monitor_and_release_acceptance.md` | 6326 | `e6bd556827557469...` | Report | 发布归档文件 |
| **Docs** | `docs/task018_review_fixes.md` | 14461 | `231e554ffdbbd17f...` | Report | 发布归档文件 |
| **Task 019** | `docs/task019_replay_video.md` | 13932 | `89699e26c1b1e33a...` | Report | 发布归档文件 |
| **Docs** | `docs/vla_input_output_analysis.md` | 10447 | `69653de0c14fd5b5...` | Report | 发布归档文件 |
| **task014** | `results/task014/acceptance.json` | 8407 | `354360eee77fb643...` | Metrics | 发布归档文件 |
| **task014** | `results/task014/predictions/sample_01_calibrated_prediction.json` | 18111 | `50388affabca9bce...` | Metrics | 发布归档文件 |
| **task014** | `results/task014/predictions/sample_02_calibrated_prediction.json` | 18033 | `64cc772051ccf47a...` | Metrics | 发布归档文件 |
| **task014** | `results/task014/metrics/calibrated_metrics.json` | 5531 | `b17cc82306e192e5...` | Metrics | 发布归档文件 |
| **task016** | `results/task016/acceptance.json` | 3375 | `0ecdeda8a92f85c4...` | Metrics | 发布归档文件 |
| **task016** | `results/task016/metrics/action_statistics.json` | 8527 | `a3193d91b35d43c2...` | Metrics | 发布归档文件 |
| **task016** | `results/task016/metrics/system_performance.json` | 805 | `1e02ff549256aac7...` | Metrics | 发布归档文件 |
| **task016** | `results/task016/records/sample_01_record.json` | 35293 | `b331e0405f886383...` | Metrics | 发布归档文件 |
| **task016** | `results/task016/records/sample_02_record.json` | 35102 | `fcf319f5992d0704...` | Metrics | 发布归档文件 |
| **task016** | `results/task016/records/sample_03_record.json` | 35273 | `807f1e54034ca74a...` | Metrics | 发布归档文件 |
| **task016** | `results/task016/records/sample_04_record.json` | 35280 | `2053add8c8631783...` | Metrics | 发布归档文件 |
| **task013** | `results/task013/acceptance.json` | 5831 | `f7be3a1e3ddf51a6...` | Metrics | 发布归档文件 |
| **task013** | `results/task013/predictions/sample_01_prediction.json` | 31949 | `18415db2e67a3e10...` | Metrics | 发布归档文件 |
| **task013** | `results/task013/predictions/sample_02_prediction.json` | 31754 | `4ce7b5387555d392...` | Metrics | 发布归档文件 |
| **task013** | `results/task013/predictions/sample_03_prediction.json` | 31808 | `899e596759d82b02...` | Metrics | 发布归档文件 |
| **task013** | `results/task013/predictions/sample_04_prediction.json` | 31867 | `62fa73aca6ae6eb0...` | Metrics | 发布归档文件 |
| **task013** | `results/task013/metrics/inference_metrics.json` | 3517 | `b8d8ef94ab407d97...` | Metrics | 发布归档文件 |
| **task012** | `results/task012/acceptance.json` | 1511 | `82506657f96cfe87...` | Metrics | 发布归档文件 |
| **task012** | `results/task012/predictions/case_001_domain0_libero.json` | 26308 | `7b09bd74626e2c9d...` | Metrics | 发布归档文件 |
| **task012** | `results/task012/predictions/case_002_domain1_aloha.json` | 26031 | `1fd8460c4abed584...` | Metrics | 发布归档文件 |
| **task012** | `results/task012/predictions/case_003_domain2_bridge.json` | 26177 | `af51a877fe923c16...` | Metrics | 发布归档文件 |
| **task012** | `results/task012/metrics/inference_metrics.json` | 5939 | `a5d52c810281f98d...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/acceptance.json` | 3910 | `447da818e2a9a1ab...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/metrics/closed_loop_metrics.json` | 2290 | `49b0b3e27ad51b6c...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/metrics/episodes.json` | 5289 | `55ada229eabce7eb...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/metrics/manipulation.json` | 5691 | `97455d972faf3eb7...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/metrics/model.json` | 298 | `0df8e39ecd2c2a52...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/records/run_seed_100.json` | 83399 | `b7b70e019fa3611a...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/records/run_seed_2026.json` | 83450 | `c0fd9f5b7886031f...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/records/run_seed_42.json` | 83406 | `be7ae946fe723f38...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/records/episode_01_seed_143/summary.json` | 1477 | `54b09d277d26b6f3...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/records/episode_02_seed_144/summary.json` | 1478 | `37709d9e77207d96...` | Metrics | 发布归档文件 |
| **task017** | `results/task017/records/episode_00_seed_142/summary.json` | 1478 | `21fefdb4ef62e137...` | Metrics | 发布归档文件 |
| **task011** | `results/task011/acceptance.json` | 3976 | `c5462071f0e4de82...` | Metrics | 发布归档文件 |
| **task011** | `results/task011/metrics/experiments.json` | 275458 | `21eaba78e62630f9...` | Metrics | 发布归档文件 |
| **task011** | `results/task011/metrics/processor_audit.json` | 6459 | `7a02ed8a67a49903...` | Metrics | 发布归档文件 |
| **task011** | `results/task011/metrics/runtime_config.json` | 2457 | `53290eb1faa32131...` | Metrics | 发布归档文件 |
| **task011** | `results/task011/metrics/task010_output_audit.json` | 671 | `1845fb473a348d76...` | Metrics | 发布归档文件 |
| **task010** | `results/task010/acceptance.json` | 1508 | `a3c0db1f59d66546...` | Metrics | 发布归档文件 |
| **task010** | `results/task010/predictions/case_001_pick_blue_block.json` | 12227 | `94cd7518b39ef49f...` | Metrics | 发布归档文件 |
| **task010** | `results/task010/predictions/case_002_approach_red_cylinder.json` | 12247 | `36ecac8f5367ca66...` | Metrics | 发布归档文件 |
| **task010** | `results/task010/predictions/case_003_open_gripper_release.json` | 12234 | `f16bb98bce31225a...` | Metrics | 发布归档文件 |
| **task010** | `results/task010/metrics/inference_metrics.json` | 3860 | `bb2170359d5c6a77...` | Metrics | 发布归档文件 |
| **task018** | `results/task018/acceptance.json` | 6692 | `d30baff7a70773b1...` | Metrics | 发布归档文件 |
| **task018** | `results/task018/metrics/grasp_release_audit.json` | 7455 | `97f649cc936b0d25...` | Metrics | 发布归档文件 |
| **Task 019** | `results/task019/acceptance.json` | 12288 | `2fe4d5593bf795cb...` | Metrics | 发布归档文件 |
| **Task 019** | `results/task019/metrics/video_metadata.json` | 12288 | `073021400b4b2a50...` | Metrics | 发布归档文件 |
| **Task 019** | `results/task019/evidence/step106_dual_view_video_frame.png` | 102400 | `bcf961a579eda446...` | Evidence | 发布归档文件 |
| **Task 019** | `results/task019/evidence/step223_terminal_video_frame.png` | 90112 | `d03d0ecd335122a4...` | Evidence | 发布归档文件 |
| **Task 019** | `results/task019/screenshots/01_offline_mode_single_source.png` | 143360 | `21140df05fa40858...` | Evidence | 发布归档文件 |
| **Task 019** | `results/task019/screenshots/02_replay_step49_mug1_grasp.png` | 167936 | `23f7b9812a795714...` | Evidence | 发布归档文件 |
| **Task 019** | `results/task019/screenshots/03_replay_step97_open_cmd.png` | 167936 | `03c3d68fe8e5d0fc...` | Evidence | 发布归档文件 |
| **Task 019** | `results/task019/screenshots/04_replay_step106_release_verified.png` | 167936 | `62c276751ec4e37c...` | Evidence | 发布归档文件 |
| **Task 019** | `results/task019/screenshots/05_replay_step176_mug2_grasp.png` | 167936 | `5f62062c0a51f138...` | Evidence | 发布归档文件 |
| **Task 019** | `results/task019/screenshots/06_replay_step223_terminal_success.png` | 167936 | `02e312b4fbd61735...` | Evidence | 发布归档文件 |
| **task015** | `results/task015/acceptance.json` | 4871 | `ddae64a566bcd1ad...` | Metrics | 发布归档文件 |
| **task015** | `results/task015/metrics/inference_metrics.json` | 814 | `7713e9de8393bb62...` | Metrics | 发布归档文件 |
| **task015** | `results/task015/records/test_acceptance_rec.json` | 6011 | `dcf661aa1a0d9810...` | Metrics | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_100_final.png` | 71331 | `8bfe4fc36e45e20c...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_2026_final.png` | 71280 | `8ab6c9960933e702...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_c0_obs_workspace.png` | 70510 | `11ac3a3968c71948...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_c0_obs_wrist.png` | 67655 | `1c3bfda0d7b0a506...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_cycle_0_step_15.png` | 70971 | `fe00028272941177...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_cycle_1_step_30.png` | 71868 | `112c75ff0fd98ec6...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_cycle_2_step_45.png` | 72035 | `fb9dca0b7cde3820...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_cycle_3_step_60.png` | 71400 | `574f5fe439d923f4...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_final.png` | 71400 | `574f5fe439d923f4...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/episode_seed_42_step_000_init.png` | 70510 | `11ac3a3968c71948...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/full_rollout_ep00_0000_init.png` | 70510 | `11ac3a3968c71948...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/full_rollout_ep00_0090_mug1_placed.png` | 71370 | `36b81b13d1274b52...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/full_rollout_ep00_0223_final_success.png` | 69454 | `7827e7c797eaa381...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/full_rollout_ep01_0222_final_success.png` | 71527 | `dff85885b7606277...` | Evidence | 发布归档文件 |
| **task017** | `evidence/task017/full_rollout_ep02_0219_final_success.png` | 71230 | `e739a14516b46599...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/nonstandard_grasp_contact.png` | 20309 | `cf255cff51e5fdf7...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/offline_monitor_isolation.png` | 129314 | `2c1ade5ee1934d0f...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/replay_mug1_place_and_release.png` | 163794 | `4806745da24bde85...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/replay_mug2_success_touchdown.png` | 157706 | `fb90f677588b27ed...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/step101_release_command_sent.png` | 23733 | `411c5df4cc635ee7...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/step110_release_physically_verified.png` | 20719 | `cffaed2db811eddb...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/touchdown_contact_unproven.png` | 18232 | `b4b57c2bb122b013...` | Evidence | 发布归档文件 |
| **task018** | `evidence/task018/windows_desktop_real_verification.png` | 291287 | `476b93daf56fa9d0...` | Evidence | 发布归档文件 |
| **task015** | `evidence/task015/action_curves_sample01.png` | 14586 | `66c31e36f0ef6ef2...` | Evidence | 发布归档文件 |
| **General** | `tasks/templates/task_template.md` | 1373 | `9be0d877ae235fa0...` | Config | 发布归档文件 |
| **Task 020** | `docs/task020_object_generalization.md` | 3639 | `c293be0773a810ae...` | Report | Task 020 选题审计 |
| **Task 020** | `results/task020/acceptance.json` | 2227 | `1a5d0fcd80144cb7...` | Audit | 书本试点 |
| **Task 020** | `results/task020/logs/registry_audit.log` | 436 | `f3b38078a7d9f18a...` | Audit | Task 020 选题审计 |
| **Task 020** | `results/task020/metrics/official_task_inventory.json` | 10745 | `bf0e9e26c99f9c09...` | Audit | Task 020 选题审计 |
| **Task 020** | `results/task020/metrics/summary.json` | 9568 | `452b50296f0970f2...` | Audit | 书本试点 |
| **Task 020** | `scripts/task020_audit_libero10.py` | 3098 | `40c062518f0acabd...` | Audit | Task 020 选题审计 |
| **Task 020** | `docs/task020_workbench_book_pilot.md` | 7161 | `fba0663ee5fc28fd...` | Evidence | 书本试点 |
| **Task 020** | `evidence/task020/history_201_terminal.png` | 270905 | `d9e75afb7d8edd34...` | Evidence | 书本试点 |
| **Task 020** | `evidence/task020/history_202_terminal.png` | 271102 | `7066d7b11ee786fd...` | Evidence | 书本试点 |
| **Task 020** | `evidence/task020/history_smoke_stopped.png` | 275334 | `af3c1ad1c4b866a3...` | Evidence | 书本试点 |
| **Task 020** | `evidence/task020/smoke_201_feedback.png` | 285034 | `566796d61f82636c...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/logs/book_pilot_oom.log` | 359 | `bb10d91a72b0ada5...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/logs/book_preflight.log` | 1006 | `d76d6dea72dcf063...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/logs/history_gui.log` | 38 | `4eab3a03c9345b14...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/logs/workbench_desktop.log` | 341 | `86bf384488e0d635...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/logs/workbench_regression.log` | 1190 | `a953bb1072c564a3...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/logs/workbench_retry_203.log` | 122 | `970c9025c2f993d7...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/metrics/book_pilot_configuration.json` | 2038 | `ff269ed66ae23d31...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/metrics/book_pilot_history.json` | 575 | `91f239b2b8401d79...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/metrics/book_pilot_interruptions.json` | 876 | `2133aa81526b21ea...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/metrics/registry_audit_summary.json` | 566 | `f35340b34d7ca3b6...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/registry_audit_acceptance.json` | 1427 | `3e4f2adae4103e42...` | Evidence | 书本试点 |
| **Task 020** | `results/task020/logs/windows_shortcut.log` | 184 | `8820b736c85f64b6...` | Evidence | 书本试点 |

| **Task 020** | `docs/task020_r1_phase1_results.md` | 4739 | `ad97d36a50b359c2...` | Report | R1 第一阶段 |
| **Task 020** | `docs/task020_r1_stability_and_gui.md` | 8306 | `d3d9a90df05eab47...` | Report | R1 第一阶段 |
| **Task 020** | `results/task020/r1/acceptance.json` | 2652 | `b16c6d90820522a8...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/source_git.json` | 1020 | `bfd4359063796fdd...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/memory_test.json` | 630 | `7449322bd5820dd3...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/logs/r1_regression.log` | 3998 | `fd0fa045cf6ed294...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/logs/legacy_action_step.log` | 1035 | `c1f67a0c8baa0582...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/logs/prior_oom_excerpt.log` | 359 | `bb10d91a72b0ada5...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/screenshots/seed_201_historical.png` | 265112 | `4ec67dbc23396efe...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/screenshots/seed_202_historical.png` | 266174 | `527c7747a17f4353...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/screenshots/simulated_resource_pressure.png` | 181529 | `15f30d854b0aca02...` | Evidence | R1 第一阶段 |
| **Task 020** | `results/task020/r1/video_hashes.json` | 544 | `10a1740a9aa8f40d...` | Evidence | R1 第一阶段 |

---

## 三、校验说明

- JSON 清单为 UTF-8 标准文本，可由标准 JSON 解析器直接读取。
- SHA256 基于清单所列文件的实际 UTF-8/二进制字节计算。
- 清单不包含模型权重、完整仿真视频或第三方数据集。
