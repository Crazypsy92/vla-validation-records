# VLA 验收成果归档发布清单 (Publication Manifest)

## 一、归档发布总览

- **归档时间**：2026-11-24
- **原工程命名空间**：`ai-learning/vla-learning`
- **发布工程命名空间**：`ai-learning/vla-validation-records`
- **GitHub 归档仓库**：`Crazypsy92/vla-validation-records`
- **归档范围**：Task 010 ～ Task 019 完整技术链条（含 Task 019-R1 回放数据可信度返修），以及 Task020-R1 Phase 2、Phase 3、Phase 4 及 Task020 结题说明
- **白名单发布文件总数**：209 个
- **总归档体积**：13223.50 KB
- **脱敏合规性审查**：
  - [x] 无任何绝对路径（`~/projects/...` / Windows 本地盘符）遗留；
  - [x] 无任何个人访问令牌（PAT）、API Key、密码及未公开凭据；
  - [x] 无任何超过 10 MB 的大二进制文件；
  - [x] 保留原始实验指标与失败边界，不虚标、不美化。

---

## 二、白名单发布文件清单（共 209 项）

| 任务 | 归档相对路径 | 大小 (Bytes) | SHA256 校验和 | 类别 | 发布说明 |
|:---:|---|:---:|:---:|:---:|---|
| **General** | `.gitignore` | 357 | `2c4084d6d8b90c9c...` | Config | 发布归档文件 |
| **General** | `README.md` | 13821 | `790ef5ff1f05634a...` | Config | Task020 验收索引 |
| **General** | `TASKS.md` | 4702 | `690137ac4b788fe4...` | Config | Task020 验收索引 |
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

---

## 三、校验说明

- JSON 清单为 UTF-8 标准文本，可由标准 JSON 解析器直接读取。
- SHA256 基于清单所列文件的实际 UTF-8/二进制字节计算。
- 清单不包含模型权重、完整仿真视频或第三方数据集。
