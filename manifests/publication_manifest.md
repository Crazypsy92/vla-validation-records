# VLA 验收成果归档发布清单 (Publication Manifest)

## 一、归档发布总览

- **归档时间**：2026-11-25
- **原工程命名空间**：`ai-learning/vla-learning`
- **发布工程命名空间**：`ai-learning/vla-validation-records`
- **GitHub 归档仓库**：`Crazypsy92/vla-validation-records`
- **归档范围**：Task 010 ～ Task 020 已验收成果，以及 Task021 阶段 A、B1、B2a 与 B2b（ACCEPTED_PARTIAL），以及 Task022-A 离线审计和 Task022-B 单次诊断及 Task022-C 资源预检及 Task022-C1 续跑
- **白名单发布文件总数**：424 个
- **总归档体积**：24420.01 KB
- **脱敏合规性审查**：
  - [x] 无任何绝对路径（`~/projects/...` / Windows 本地盘符）遗留；
  - [x] 无任何个人访问令牌（PAT）、API Key、密码及未公开凭据；
  - [x] 无任何超过 10 MB 的大二进制文件；
  - [x] 保留原始实验指标与失败边界，不虚标、不美化。

---

## 二、白名单发布文件清单（共 424 项）

| 任务 | 归档相对路径 | 大小 (Bytes) | SHA256 校验和 | 类别 | 发布说明 |
|:---:|---|:---:|:---:|:---:|---|
| **General** | `.gitignore` | 357 | `2c4084d6d8b90c9c...` | Config | 发布归档文件 |
| **Task022-C1** | `README.md` | 15086 | `2ea032ba5407ed40...` | Report | Task022-C1 C3 续跑 |
| **Task022-C1** | `TASKS.md` | 5873 | `f678eb1f6f21f0f7...` | Report | Task022-C1 C3 续跑 |
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
| **Task 019** | `docs/task019_replay_video.md` | 13746 | `95a26ae7c8b8021b...` | Report | 发布归档文件 |
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

| **Task 020** | `docs/task020_r1_phase2_results.md` | 4332 | `87852b1e33f54aa9...` | Report | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/acceptance.json` | 2949 | `86d79a0eef15fbfd...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/logs/regression_final.log` | 3695 | `41e2d0d2222b7e05...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/logs/runs_seed_201.log` | 748 | `6b79c1e9d2ce909b...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/logs/verification.log` | 1922 | `1aa59fc0554f880a...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/metrics/cancelled_mode_selection.json` | 547 | `7e1d0bd42e7f2cdc...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/metrics/exit_samples.jsonl` | 517 | `374819ef52b35630...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/metrics/history_hashes_before.json` | 1229 | `3e04c012ae81b0a2...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/metrics/run_summary.json` | 1391 | `434b97893890a556...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/metrics/windows_baseline.json` | 221 | `55a38641890e0936...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/metrics/wsl_baseline.json` | 345 | `2ba15e084286fc9e...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/chunk_000.json` | 29816 | `f57787972cdf261c...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/configuration.json` | 976 | `9f63d96cd65cfc2d...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/events.jsonl` | 56604 | `1098fe015d22dc41...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/resources_gui.jsonl` | 44042 | `b3f2a6dff1663bec...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/resources_gui_observed_worker.jsonl` | 44252 | `f45adf534d500e49...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/resources_worker.jsonl` | 13421 | `d8a4588a0df75619...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/summary.json` | 1201 | `36e57b498d9bc5be...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/runs/seed_201/worker_exit_code.txt` | 2 | `9a271f2a916b0b6e...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/screenshots/forward_validated.png` | 292381 | `ff8aee86b5928698...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/screenshots/history_check.png` | 262016 | `bb2909ab66effabd...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/screenshots/live_step_30.png` | 300123 | `f739f81c4b5755a6...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/screenshots/model_ready.png` | 169237 | `3ad15640c2240740...` | Evidence | Task020-R1 Phase 2 |
| **Task 020** | `results/task020/r1/phase2/screenshots/stopped.png` | 301965 | `21c19f33a3f1edd7...` | Evidence | Task020-R1 Phase 2 |

| **Task 020** | `docs/task020_r1_phase3_results.md` | 4631 | `7f922f2fa41747b6...` | Report | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/acceptance.json` | 2880 | `902c8e0b7c54c71e...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/logs/gui_driver.log` | 306 | `d0b219aedf108203...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/logs/regression.log` | 3695 | `21f62bcb570170a2...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/logs/runs_phase3_seed_201.log` | 748 | `6b79c1e9d2ce909b...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/logs/verification.log` | 271 | `e1b0e943651a9a31...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/metrics/history_after.json` | 1775 | `b0edfbd0216e1ad7...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/metrics/history_before.json` | 1775 | `b0edfbd0216e1ad7...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/metrics/lifecycle.jsonl` | 74541 | `d2a2bb48c854e189...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/metrics/summary.json` | 4864 | `86618b986d77f200...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/metrics/windows_baseline.json` | 121 | `45bb83e7f777df21...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/metrics/wsl_baseline.json` | 318 | `029ff07ea655b47e...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/chunk_000.json` | 29816 | `28a1b86b5a1d0f4d...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/chunk_001.json` | 29775 | `6d2954b964d58ded...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/chunk_002.json` | 29628 | `f528ffa3f6ad2ac7...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/configuration.json` | 976 | `9f63d96cd65cfc2d...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/events.jsonl` | 179395 | `7610b0f066a006af...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/resources_gui.jsonl` | 43004 | `055011df7f2a6473...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/resources_gui_observed_worker.jsonl` | 43443 | `b7771b70ee518b3c...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/resources_worker.jsonl` | 9306 | `7911f4e48f1ab7d3...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/summary.json` | 1269 | `7dff523b844e0918...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/runs/phase3_seed_201/worker_exit_code.txt` | 2 | `9a271f2a916b0b6e...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/before_run.png` | 158991 | `ff601cfcf5b6e3e7...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/chunk_0_step_000.png` | 289650 | `8ff06f37e59eb9f1...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/chunk_1_step_030.png` | 298169 | `6779dab54dc07083...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/chunk_2_step_060.png` | 299102 | `2a6f4de04ffc0ed3...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/forward_gate_step_000.png` | 166505 | `496a21a9f6d59745...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/forward_gate_step_030.png` | 299303 | `5198f1fbd6d8924c...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/forward_gate_step_060.png` | 298072 | `bc25d15845c9b786...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/live_step_090.png` | 297456 | `57ff1dbc58ae87c1...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/replay_step_000.png` | 266097 | `4bb8fe7812148b47...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/replay_step_090.png` | 284579 | `6f8f78d08375bcc1...` | Evidence | Task020-R1 Phase 3 |
| **Task 020** | `results/task020/r1/phase3/screenshots/worker_exited.png` | 299760 | `f6f0ed4ecd52a879...` | Evidence | Task020-R1 Phase 3 |

| **Task 020** | `docs/task020_r1_phase4_seed203_results.md` | 7048 | `9b29851bdeaf07c2...` | Report | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/acceptance.json` | 5912 | `a93dc2f77d48373e...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/logs/gate_tests.log` | 568 | `5f5ced35c21f8f02...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/logs/monitor.log` | 358 | `67db556cc9c56e0d...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/logs/monitor_rejoined.log` | 137 | `f08dfb6aafcfbbcc...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/logs/regression.log` | 3695 | `099f1d93f78a5d40...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/logs/replay_check.log` | 359 | `9d39b19259d1e36a...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/logs/runs_phase4_seed_203_1795437286005880657.log` | 748 | `6b79c1e9d2ce909b...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/logs/verification.log` | 654 | `3a9921ebd8f29b94...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/budget.json` | 405 | `6a286c65e52e32a1...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/history_after.json` | 37388 | `271756220eaa5c2c...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/history_before.json` | 37388 | `271756220eaa5c2c...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/lifecycle.jsonl` | 150308 | `72b9b4599fc81aa5...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/summary.json` | 22377 | `80391fea641c5374...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/windows_baseline.json` | 121 | `787be0167215df98...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/wsl_baseline.json` | 430 | `7f7ff1d2b8d0eb79...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/metrics/wsl_early_worker.json` | 714 | `0860abe57f207616...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/chunk_000.json` | 29877 | `8c09027ddbb87fa9...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/chunk_001.json` | 29791 | `b1867f538f3f0223...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/chunk_002.json` | 29705 | `36cc76880d105736...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/chunk_003.json` | 29593 | `95a41dae297c4912...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/chunk_004.json` | 29634 | `72a9492480c52e60...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/chunk_005.json` | 29652 | `510e78e6798d8899...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/chunk_006.json` | 29673 | `64aa8f8b12bcac3c...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/configuration.json` | 976 | `9f63d96cd65cfc2d...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/events.jsonl` | 425299 | `a8dd604512d489de...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/formal_gate_gui.jsonl` | 248 | `27d46834ae28344f...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/formal_gate_worker.jsonl` | 5801 | `5df2854cc1a09513...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/launch_configuration.json` | 190 | `fee0a1d81a2c4289...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/resources_gui.jsonl` | 72561 | `3442a193d73064cd...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/resources_gui_observed_worker.jsonl` | 73702 | `dd087bea927620e2...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/resources_worker.jsonl` | 11290 | `6eb168430b79663b...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/summary.json` | 1275 | `6721a8284c2e8334...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/runs/phase4_seed_203_1795437286005880657/worker_exit_code.txt` | 2 | `9a271f2a916b0b6e...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/before_run.png` | 158132 | `5e170700efd72a53...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/finished.png` | 289826 | `4c07143ec7b31907...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/formal_confirmation.png` | 17317 | `34bc7e3eba64389f...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/live_input_step_000.png` | 285533 | `60da8b1cc08e1595...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/live_input_step_030.png` | 298016 | `bf4e608b5490fa6c...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/live_input_step_060.png` | 303143 | `822e755262ff8487...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/live_input_step_090.png` | 299589 | `1343a0f7104887a7...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/live_input_step_120.png` | 300411 | `021c7a99d4406e3e...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/live_input_step_150.png` | 296702 | `f179fb56f7e63408...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/live_input_step_180.png` | 292803 | `fadf1cd7323262be...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/replay_final.png` | 274505 | `49e3a417f7b40832...` | Evidence | Task020-R1 Phase 4 |
| **Task 020** | `results/task020/r1/phase4/screenshots/replay_reset.png` | 261339 | `f9cda34ac20c32ff...` | Evidence | Task020-R1 Phase 4 |


| **Task 020** | `docs/task020_goal_met_with_limitations.md` | 2532 | `0889b07986aeb4a7...` | Report | Task020 结题说明 |

| **Task 021** | `docs/task021_initial_state_generalization.md` | 15734 | `888c772c80a02343...` | Report | Task021 阶段 B2b |
| **Task 021** | `evidence/task021/index_00_reset.jpg` | 25241 | `64f41f479edba7f0...` | Screenshot | Task021 阶段 A |
| **Task 021** | `evidence/task021/index_01_reset.jpg` | 25225 | `8ad6a6e0d62f8d16...` | Screenshot | Task021 阶段 A |
| **Task 021** | `evidence/task021/index_02_reset.jpg` | 25006 | `4a47f799921d330a...` | Screenshot | Task021 阶段 A |
| **Task 021** | `evidence/task021/index_15_reset.jpg` | 24477 | `d2c54df07d0f813f...` | Screenshot | Task021 阶段 A |
| **Task 021** | `evidence/task021/index_34_reset.jpg` | 25109 | `65e81c29a4035076...` | Screenshot | Task021 阶段 A |
| **Task 021** | `results/task021/acceptance.json` | 7335 | `9d7dfd35d23367d2...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/metrics/initial_states.json` | 179862 | `c5694a6f15ff94fe...` | Evidence | Task021 阶段 A |
| **Task 021** | `results/task021/metrics/inventory_source.json` | 1758 | `768482864e98563b...` | Evidence | Task021 阶段 A |
| **Task 021** | `results/task021/metrics/summary.json` | 7916 | `1ba793df009f0dd0...` | Evidence | Task021 阶段 B2b |

| **Task 021** | `evidence/task021/b1/index_15_display_check.png` | 299272 | `dd635e4836b5cf28...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `evidence/task021/b1/index_15_result.png` | 306773 | `de968442e46be790...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `evidence/task021/b1/index_15_selected.png` | 160541 | `c9df9ca94708b784...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `evidence/task021/b1/index_34_result.png` | 305935 | `7f045e528326daa7...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `evidence/task021/b1/index_34_selected.png` | 160588 | `962715280057d436...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/logs/gui_evidence_check.log` | 217 | `9ee8f59789e4072f...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/logs/regression.log` | 4496 | `0a0b2cbd656e18ce...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/metrics/summary.json` | 2740 | `3264df4405067804...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_15_rng_201_1795491280237605745/0000_workspace.png` | 65480 | `9955aaee80ab9554...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_15_rng_201_1795491280237605745/0000_wrist.png` | 45513 | `b43af561e393673f...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_15_rng_201_1795491280237605745/events.jsonl` | 2937 | `1771cb5349103e97...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_15_rng_201_1795491280237605745/launch_configuration.json` | 198 | `1772945ba64c7606...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_15_rng_201_1795491280237605745/resources_worker.jsonl` | 588 | `d765a3f8609bfc19...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_15_rng_201_1795491280237605745/summary.json` | 1906 | `9d94497e86579551...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_15_rng_201_1795491280237605745/worker_exit_code.txt` | 2 | `9a271f2a916b0b6e...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_34_rng_201_1795491421389679840/0000_workspace.png` | 65633 | `8e430f56f86252f2...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_34_rng_201_1795491421389679840/0000_wrist.png` | 47626 | `974ecf57dc8917b7...` | Screenshot | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_34_rng_201_1795491421389679840/events.jsonl` | 2948 | `48f5d5bafea1bcd1...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_34_rng_201_1795491421389679840/launch_configuration.json` | 198 | `06b4b8b35d718f5f...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_34_rng_201_1795491421389679840/resources_worker.jsonl` | 586 | `0fbd4038fee78484...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_34_rng_201_1795491421389679840/summary.json` | 1906 | `fe8a63881cc09c1f...` | Evidence | Task021 阶段 B1 |
| **Task 021** | `results/task021/b1/runs/reset_index_34_rng_201_1795491421389679840/worker_exit_code.txt` | 2 | `9a271f2a916b0b6e...` | Evidence | Task021 阶段 B1 |

| **Task 021** | `evidence/task021/b2a/before_run.png` | 160541 | `c9df9ca94708b784...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `evidence/task021/b2a/confirmation.png` | 17274 | `d3ec448d66e94969...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `evidence/task021/b2a/finished.png` | 293615 | `181d14b1359c9f9a...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `evidence/task021/b2a/input_000.png` | 169982 | `b114ef1e169588b3...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `evidence/task021/b2a/input_030.png` | 300012 | `dd024c307a954a30...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `evidence/task021/b2a/reset_display_check.png` | 298150 | `68d71cafd3df2f64...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/gui_close.log` | 49 | `433848aa932d0b82...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/monitor.log` | 368 | `b3d15c5dd405488a...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/monitor_rejoined.log` | 252 | `a790b1c57d68d7f4...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/regression.log` | 4815 | `26302a10149593f9...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/reset_display.log` | 95 | `7568236cb728f791...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/runs_b2a_index_15_rng_201_1795493022081788638.log` | 748 | `6b79c1e9d2ce909b...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/tests.log` | 1430 | `897e642eabd96855...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/logs/verification.log` | 646 | `b6f209046c220e85...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/metrics/gui_close.json` | 143 | `65b7e7f9adb1769d...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/metrics/history_after.json` | 37388 | `271756220eaa5c2c...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/metrics/lifecycle.jsonl` | 182113 | `c5e3b30094d1791c...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/metrics/preflight_fingerprints.json` | 3134 | `993a725992606a59...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/metrics/summary.json` | 19636 | `d656c693cc729a93...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/metrics/wsl_baseline.json` | 277 | `85293c053ad21700...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/metrics/wsl_early_worker.json` | 734 | `92da8c41de5d059f...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/0000_workspace.png` | 65480 | `9955aaee80ab9554...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/0000_wrist.png` | 45513 | `b43af561e393673f...` | Screenshot | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/chunk_000.json` | 29831 | `bdcebcbfc77f1f93...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/chunk_001.json` | 29744 | `b627c3f9799256a4...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/chunk_002.json` | 29647 | `9e56590b1d40d2e2...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/chunk_003.json` | 29571 | `e4bb9a78cc596148...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/chunk_004.json` | 29627 | `83b70ed2333e03fb...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/chunk_005.json` | 29650 | `d7b5e775de69995c...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/chunk_006.json` | 29720 | `a94ed15ab7b0523e...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/configuration.json` | 976 | `9f63d96cd65cfc2d...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/events.jsonl` | 431522 | `57455e5253e0bcdf...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/formal_gate_gui.jsonl` | 248 | `c505282a65f4ebed...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/formal_gate_worker.jsonl` | 3864 | `aeab7cf1fe09fa1b...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/launch_configuration.json` | 200 | `1dea0d9639710ece...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/resources_gui.jsonl` | 84440 | `d991bd3f24f9ad76...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/resources_gui_observed_worker.jsonl` | 85802 | `e068188592519840...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/resources_worker.jsonl` | 11353 | `8b412e93f366f460...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/summary.json` | 1497 | `7f3aa8023abb4f3f...` | Evidence | Task021 阶段 B2a |
| **Task 021** | `results/task021/b2a/runs/b2a_index_15_rng_201_1795493022081788638/worker_exit_code.txt` | 2 | `9a271f2a916b0b6e...` | Evidence | Task021 阶段 B2a |

| **Task 021** | `evidence/task021/b2b/before_run.png` | 214166 | `312a004f5eaea88c...` | Screenshot | Task021 阶段 B2b |
| **Task 021** | `evidence/task021/b2b/finished.png` | 306946 | `8c5976a2059409dc...` | Screenshot | Task021 阶段 B2b |
| **Task 021** | `evidence/task021/b2b/input_000.png` | 303253 | `1744995acf15773a...` | Screenshot | Task021 阶段 B2b |
| **Task 021** | `evidence/task021/b2b/input_030.png` | 313727 | `4125f9839cb56d2c...` | Screenshot | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/gui_close.log` | 49 | `433848aa932d0b82...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/gui_driver.log` | 105 | `2ab5041c32f5717c...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/monitor.log` | 735 | `23cb1b1128eefe8f...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/monitor_live.log` | 639 | `a48126902f607c0c...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/monitor_rejoined.log` | 215 | `ca52d7ce6749bb23...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/runs_b2b_index_34_rng_201_1795501086954054532.log` | 748 | `6b79c1e9d2ce909b...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/tests.log` | 1749 | `1fbab1a6494f58c1...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/logs/verification.log` | 907 | `dd139a78d8d7d450...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/b1_history_before.json` | 2895 | `650fbad51e121e3f...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/b2a_history_before.json` | 7652 | `ac23f4e3c162748d...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/gui_close.json` | 143 | `a6f69406def292c2...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/gui_confirmation.json` | 268 | `b452be7c7b86a573...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/history_after.json` | 37388 | `271756220eaa5c2c...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/lifecycle.jsonl` | 353340 | `f777850213448f66...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/preflight_fingerprints.json` | 3102 | `b5a1c5f6eaf4f2b9...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/summary.json` | 38568 | `32b5441c6c214d10...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/metrics/wsl_baseline.json` | 278 | `171e2163230b7266...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/0000_workspace.png` | 65633 | `8e430f56f86252f2...` | Screenshot | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/0000_wrist.png` | 47626 | `974ecf57dc8917b7...` | Screenshot | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_000.json` | 29893 | `2059a748acbccfb6...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_001.json` | 29816 | `fa4fcd391a61624d...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_002.json` | 29696 | `0f34a10d27d69d48...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_003.json` | 29595 | `62a578e5a118446e...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_004.json` | 29585 | `1144433da352eec2...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_005.json` | 29659 | `3fcf24a159a0cc00...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_006.json` | 29682 | `6b1ca73807a315f1...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_007.json` | 29637 | `4b52bfe08ad9de0c...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_008.json` | 29509 | `0db1c72cb11bd3be...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_009.json` | 29495 | `ef4254cc81ee3951...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_010.json` | 29467 | `77a4a246b0dddac0...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_011.json` | 29467 | `36f7e8ddd65ab002...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_012.json` | 29506 | `239e0ec072e4ea01...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_013.json` | 29472 | `a420ab15855c65d0...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_014.json` | 29509 | `e460e80c7047da24...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_015.json` | 29478 | `34c8dbe9cf1f095e...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_016.json` | 29473 | `91d97dda0fba1d29...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/chunk_017.json` | 29453 | `19e657b982c0deea...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/configuration.json` | 976 | `9f63d96cd65cfc2d...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/events.jsonl` | 1139596 | `584cbdd3d40fbdf6...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/formal_gate_gui.jsonl` | 249 | `7d240157d73c136f...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/formal_gate_worker.jsonl` | 9547 | `51e784b2a1d6f11f...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/launch_configuration.json` | 200 | `e01af5f7cdb5ef53...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/resources_gui.jsonl` | 163541 | `b3cc12e5944d1600...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/resources_gui_observed_worker.jsonl` | 166280 | `80fd998724f473ce...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/resources_worker.jsonl` | 26995 | `eddd91dde24576dd...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/summary.json` | 1504 | `4294a46a4822e3c1...` | Evidence | Task021 阶段 B2b |
| **Task 021** | `results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532/worker_exit_code.txt` | 2 | `9a271f2a916b0b6e...` | Evidence | Task021 阶段 B2b |

| **Task 022** | `docs/task022_index34_failure_forensics.md` | 9371 | `d6db904b4f7993e7...` | Report | Task022-A 离线审计 |
| **Task 022** | `evidence/task022/a/index_15_video_keyframes.jpg` | 160864 | `91e51c054badcfd5...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `evidence/task022/a/index_34_video_keyframes.jpg` | 275147 | `fb85e954530d9f14...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `evidence/task022/a/trajectory_comparison.png` | 446976 | `65be4463cbd4f552...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `results/task022/a/acceptance.json` | 1523 | `d1655154c194ab59...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `results/task022/a/audit.py` | 19789 | `a9b378220ec22471...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `results/task022/a/logs/audit.log` | 7738 | `0ce09d76f5381ab0...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `results/task022/a/metrics/index_15_trajectory.json` | 403354 | `05bcfe32319937b9...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `results/task022/a/metrics/index_34_trajectory.json` | 1073358 | `a1404cf172664f41...` | Evidence | Task022-A 离线审计 |
| **Task 022** | `results/task022/a/metrics/summary.json` | 123357 | `0262103e853ee788...` | Evidence | Task022-A 离线审计 |

---

## 三、校验说明

- JSON 清单为 UTF-8 标准文本，可由标准 JSON 解析器直接读取。
- SHA256 基于清单所列文件的实际 UTF-8/二进制字节计算。
- 清单不包含模型权重、完整仿真视频或第三方数据集。
| **Task022-C** | `docs/task022_index34_diagnostic.md` | 5200 | `02140a88d3c8681d...` | Report | Task022-C 资源预检 |
| **Task022-B** | `evidence/task022/b/0000_workspace.png` | 65633 | `8e430f56f86252f2...` | Evidence | Task022-B 单次诊断 |
| **Task022-B** | `evidence/task022/b/0000_wrist.png` | 47626 | `974ecf57dc8917b7...` | Evidence | Task022-B 单次诊断 |
| **Task022-B** | `evidence/task022/b/resource_pressure.png` | 81426 | `6fa8a3a219f53041...` | Evidence | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/acceptance.json` | 1320 | `bee5e803def29672...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/config.json` | 9307 | `2fb7f30bf3892e88...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/configuration.json` | 976 | `9f63d96cd65cfc2d...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/diagnostic.jsonl` | 518 | `d48f35d2b580f53e...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/events.jsonl` | 3385 | `908f05207d3b0e19...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/exit.json` | 123 | `e582695ecb3b51ba...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/formal_gate_supervisor.jsonl` | 256 | `ac0df2f0276a314a...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/formal_gate_worker.jsonl` | 259 | `ba245ac660ae141b...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/launch.json` | 490 | `bc86c2aab7de2caf...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/policy_postprocessor.json` | 575 | `d1d73a18f14aca0e...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/policy_preprocessor.json` | 1635 | `442ac4352dce2547...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/preflight.json` | 2866 | `76056243a77a55a8...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/reproduction.jsonl` | 123 | `21a3c7ea07ed2eea...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/resources_supervisor.jsonl` | 15201 | `9787654e165c186e...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/resources_worker.jsonl` | 988 | `8877a59bf363f3f3...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/summary.json` | 638 | `4c68c8194db39e98...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/logs/worker.log` | 748 | `bef7239f7d7f7a4a...` | Data | Task022-B 单次诊断 |
| **Task022-B** | `results/task022/b/metrics/summary.json` | 3108 | `7ce75bbbbbf65ab1...` | Data | Task022-B 单次诊断 |
| **Task022-C1** | `docs/task022_index34_resource_preflight.md` | 4089 | `fb1ebd16af505b9a...` | Report | Task022-C1 C3 续跑 |
| **Task022-C1** | `scripts/task022_index34_diagnostic.py` | 18911 | `49c9eb1368ba400c...` | Data | Task022-C1 C3 续跑 |
| **Task022-C** | `evidence/task022/c/0000_workspace.png` | 65633 | `8e430f56f86252f2...` | Evidence | Task022-C 资源预检 |
| **Task022-C** | `evidence/task022/c/0000_wrist.png` | 47626 | `974ecf57dc8917b7...` | Evidence | Task022-C 资源预检 |
| **Task022-C** | `evidence/task022/c/reset_resource_curve.png` | 66618 | `af127e50c7c1e224...` | Evidence | Task022-C 资源预检 |
| **Task022-C1** | `results/task022/c/acceptance.json` | 689 | `03e7ca185d64da76...` | Data | Task022-C1 C3 续跑 |
| **Task022-C** | `results/task022/c/logs/lifecycle/baseline.json` | 1894 | `91e27e2bc2d4980a...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/combined/exit.json` | 477 | `3f6ea8028b70650c...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/combined/formal_gate_preflight.jsonl` | 259 | `9288d53d5a083185...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/combined/gates.jsonl` | 231 | `d36ad86a6c14ddc4...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/combined/resources_supervisor.jsonl` | 193 | `c9fd1bf0af774d42...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/launch.json` | 370 | `9ce7900a58198d37...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/exit.json` | 747 | `d7998a06f7d8fe96...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/formal_gate_preflight.jsonl` | 528 | `65c7342598a25a8e...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/gates.jsonl` | 456 | `12d9f451385f3de7...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/resources_child.jsonl` | 1206 | `2d486859ab0a9866...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/resources_supervisor.jsonl` | 13248 | `b9dcd4d3c71f0771...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/resources_worker.jsonl` | 397 | `6cadec054efb31d4...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/result.json` | 896 | `5acd1cd6a810b257...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/reset_only/worker.log` | 599 | `41b960236d25f044...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle/summary.json` | 139 | `d29e5e86a14384a1...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/lifecycle_exit.json` | 21 | `81868a6e94ffc017...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_archive_root/baseline.json` | 1894 | `91e27e2bc2d4980a...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_archive_root/launch.json` | 382 | `d991ea2df1da90e0...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_archive_root/summary.json` | 102 | `1060a8d4badaa498...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_checks.json` | 1095 | `3ead81b3465b7ffb...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_other_cwd/baseline.json` | 1894 | `91e27e2bc2d4980a...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_other_cwd/launch.json` | 371 | `832544be6f78ee40...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_other_cwd/summary.json` | 102 | `1060a8d4badaa498...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_project_root/baseline.json` | 1894 | `91e27e2bc2d4980a...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_project_root/launch.json` | 384 | `92d7bbbb69cd4a7d...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/logs/static_project_root/summary.json` | 102 | `1060a8d4badaa498...` | Data | Task022-C 资源预检 |
| **Task022-C** | `results/task022/c/metrics/summary.json` | 2026 | `7fcaca6cff1b7a2e...` | Data | Task022-C 资源预检 |
| **Task022-C1** | `docs/task022_index34_resource_resume.md` | 3906 | `6c93e2074feb41da...` | Report | Task022-C1 C3 续跑 |
| **Task022-C1** | `evidence/task022/c1/0000_workspace.png` | 65633 | `8e430f56f86252f2...` | Evidence | Task022-C1 C3 续跑 |
| **Task022-C1** | `evidence/task022/c1/0000_wrist.png` | 47626 | `974ecf57dc8917b7...` | Evidence | Task022-C1 C3 续跑 |
| **Task022-C1** | `evidence/task022/c1/c3_resource_curve.png` | 123924 | `16286a82fe64f5bf...` | Evidence | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/acceptance.json` | 311 | `2329fb407b931254...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/baseline_commands.jsonl` | 529 | `5390240aea20cc91...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/free.txt` | 207 | `c370e37855e7c953...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/gate_fixture/gates.jsonl` | 808 | `c2873761d8925a77...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/gate_test.log` | 55 | `f3ea31b4da5ddd01...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/baseline.json` | 1895 | `2ec1ace56e11d656...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/combined_resume/exit.json` | 835 | `cfb9fb76676cddf7...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/combined_resume/gates.jsonl` | 1338 | `b0cdfd818d1f3d1a...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/combined_resume/progress.json` | 259 | `d48471a2f3652436...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/combined_resume/resources_child.jsonl` | 1815 | `ba93ec6830b8e50d...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/combined_resume/resources_supervisor.jsonl` | 222256 | `3c0b7545e0d77f1c...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/combined_resume/result.json` | 944 | `72a7f4c8f32e3c57...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/combined_resume/worker.log` | 768 | `4cca1097c4f16973...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/launch.json` | 367 | `4a84c85edcefd30a...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle/summary.json` | 129 | `a46ebcc4c89304c7...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/lifecycle_exit.json` | 17 | `e89df0eae5ec7db8...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/meminfo.txt` | 1475 | `9ca9ec1ebff350e8...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/memory_psi.txt` | 108 | `6a5bc9dfd601fdb7...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/oom_kill_count.txt` | 11 | `a3cb289fc1bf1f9d...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/swapon.txt` | 68 | `e040cd716ad8ff59...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/swaps.txt` | 110 | `18fc8dc432d9ccdf...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/logs/vmstat.txt` | 428 | `b7346dfff542ab3e...` | Data | Task022-C1 C3 续跑 |
| **Task022-C1** | `results/task022/c1/metrics/summary.json` | 2366 | `31b7f056ab66a54e...` | Data | Task022-C1 C3 续跑 |
