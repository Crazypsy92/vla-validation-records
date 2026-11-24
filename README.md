# VLA 具身决策模型验收成果与评测档案库 (VLA Validation Records)

[![Platform](https://img.shields.io/badge/Platform-WSL2%20%7C%20Ubuntu%2024.04-orange.svg)]()
[![Model](https://img.shields.io/badge/Model-X--VLA%20(879M)%20%7C%20SmolVLA%20(450M)-green.svg)]()
[![Simulation](https://img.shields.io/badge/Simulation-LIBERO%20%7C%20MuJoCo%203.8.1-brightgreen.svg)]()

本仓库是个人具身智能学习与技术验证体系（`ai-learning`）中 **VLA（Vision-Language-Action）具身决策层** 的独立私有归档仓库。

本仓库**仅用于归档保存**阶段验收报告、物理语义规范、结构化实验指标与精选仿真证据，不包含未经裁剪的模型权重、庞大数据集或本地开发环境。

> **任务接力入口**：[TASKS.md](TASKS.md) · [Task020 结题审核 / Issue #4](https://github.com/Crazypsy92/vla-validation-records/issues/4) · [Antigravity 接力规范](docs/remote_task_relay.md)。默认不启用定时任务。
>
> **版本提示（2026-11-23）**：仓库现有 Task017 正式报告记录的是**初期 60 步闭环（软件 3/3 PASS、任务 0/3）**；用户另汇报了**后续完整回合（664 步、24 次推理、LIBERO 3/3 成功，但第二杯未观察到主动松爪）**。后者的原始摘要、验收报告和精选证据**已归档并经有限边界审核**，参见 [Issue #1](https://github.com/Crazypsy92/vla-validation-records/issues/1)。两版证据不可混用，完整主动释放亦不可由 LIBERO 成功判定替代。

---

> **Task019-R1 验收结论（2026-11-23）**：回放数据源、状态字段、JSON/manifest、WSLg 桌面显示、指标定义及视频哈希已完成复核，按 `ACCEPTED_WITH_LIMITATIONS` 关闭；内部 Workbench 回放通过，外部播放器未验证，且本轮按范围未重跑模型/仿真。返修报告见 [task019-review 分支](https://github.com/Crazypsy92/vla-validation-records/blob/task019-review/docs/task019_r1_repair.md)。下一步转入 [Task020 / Issue #4](https://github.com/Crazypsy92/vla-validation-records/issues/4)，开展非杯类物体的 X-VLA 闭环迁移验证。

## ⚠️ 重要声明与验证边界 (Important Disclaimers)

> [!IMPORTANT]
> **本仓库所记录的所有能力、指标与测试成果，均严格限定在仿真环境与离线基准测试范围之内。**
> 
> 必须明确知悉以下技术边界：
> 1. **当前成果属于纯仿真与离线验证**：所有闭环测试均在 MuJoCo 3.8.1 物理引擎及 LIBERO 仿真环境中完成，**不代表已经在真实物理机械臂（Real Robot Arm）上完成实体部署**；
> 2. **不代表双臂协同系统已通过验证**：虽然模型支持多领域输入，但当前全链路闭环仅针对单臂（Franka Panda 7-DoF + 2指夹爪）桌面操作场景；
> 3. **不代表端侧轻量化嵌入式部署已完成**：当前推理均运行于 x86_64 CPU 架构的 Python 环境下，尚未移植至边缘算力盒（如 Jetson Orin 或嵌入式 NPU）；
> 4. **抓取-放置长程任务的验收分版本**：现有 Task017 初期 60 步报告仅验证趋近和控制闭环，任务 0/3；后续完整回合的 LIBERO 3/3 已归档审核，但第二杯主动释放未验证；Seed144 白杯抓持检测缺失、Seed143 黄白杯终点抓持为 false，见 [Task018](https://github.com/Crazypsy92/vla-validation-records/issues/2)。**不将动作输出、LIBERO 谓词成功与完整释放混为一谈**。

---

## 一、技术演进路线：从文本到物理行动

个人在 `ai-learning` 项目中，遵循循序渐进的具身智能认知与工程落地路线：

```mermaid
flowchart LR
    A["LLM<br/>(纯文本逻辑推理)"] --> B["VLM<br/>(多模态图文理解)"]
    B --> C["VLA 离线推理<br/>(视觉语言映射到动作)"]
    C --> D["VLA Workbench<br/>(动作物理语义审计)"]
    D --> E["LIBERO 仿真闭环<br/>(MuJoCo 实时环境交互)"]
```

1. **LLM 阶段**：探索大语言模型的文本生成、指令理解与基础任务分解逻辑；
2. **VLM 阶段**：引入空间几何与图像视觉输入，建立多模态对齐感知能力；
3. **VLA 离线推理阶段（Task 010～Task 014）**：打通多相机 RGB 输入、8D 机器人状态和任务指令到连续动作张量（Action Chunk）的端到端生成；
4. **动作物理语义审计阶段（Task 015～Task 016）**：纠正维度歧义，建立真实的笛卡尔空间末端位置、轴角姿态及夹爪二值物理语义映射；
5. **仿真闭环验证阶段（Task 017）**：接入官方 LIBERO 基准与 MuJoCo 物理引擎，实现“感知-推理-执行-新感知”的完整自主闭环。

---

## 二、核心模型体系

本阶段归档聚焦于当前具身智能领域的两类轻量化开源主力模型：

| 模型代号 | 架构基座与参数量 | 动作预测头 | 适用控制域 | 验证定位 |
|---|---|---|---|---|
| **SmolVLA Base** | 450M 参数（SmolLM2-135M + 视觉编码器） | Flow Matching 动作专家（50 步 Action Chunk） | 通用桌面抓取、ALOHA 双臂 | 快速端侧离线前向与输入鲁棒性基线 (Task 010~011) |
| **X-VLA Base** | 879.48M 参数（Florence-2 + Soft-Prompted Transformer） | Action Transformer + Flow Matching | LIBERO, ALOHA, BridgeData V2 | 跨本体、多领域泛化推理能力验证 (Task 012) |
| **X-VLA LIBERO** | 879.48M 参数（特定环境微调权重） | Flow Matching (30 步动作块预测) | LIBERO (Franka Panda 7D) | 物理语义审计与仿真闭环核心主力模型 (Task 013~017) |

---

## 三、Task 010 ～ Task 017 阶段成果与导航索引

| 阶段任务 | 任务主题与核心突破 | 核心模型 | 验收判定 | 正式报告 | 关键指标与记录 | 精选证据 |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| **Task 010** | SmolVLA (450M) 基线构建与 CPU 离线推理 | `smolvla_base` | **PASS** | [Task 010 报告](docs/task010_smolvla_baseline.md) | [metrics.json](results/task010/metrics/inference_metrics.json) | [case01.json](results/task010/predictions/case_001_pick_blue_block.json) |
| **Task 011** | 输入敏感度、随机噪声鲁棒性与语义消歧 | `smolvla_base` | **PASS** | [Task 011 报告](docs/task011_input_sensitivity.md) | [experiments.json](results/task011/metrics/experiments.json) | [audit.json](results/task011/metrics/processor_audit.json) |
| **Task 012** | X-VLA 离线推理与多 Domain 输入初测（不等于泛化验证） | `xvla-base` | **PASS** | [Task 012 报告](docs/task012_xvla_inference.md) | [metrics.json](results/task012/metrics/inference_metrics.json) | [libero.json](results/task012/predictions/case_001_domain0_libero.json) |
| **Task 013** | LIBERO 机器人仿真示范数据基准评测 | `xvla-libero` | **PASS** | [Task 013 报告](docs/task013_libero_offline_action_validation.md) | [metrics.json](results/task013/metrics/inference_metrics.json) | [sample01.json](results/task013/predictions/sample_01_prediction.json) |
| **Task 014** | 全链路动作空间异常审计与处理器标定 | `xvla-libero` | **PASS** | [Task 014 报告](docs/task014_xvla_pipeline_audit.md) | [calibrated.json](results/task014/metrics/calibrated_metrics.json) | [calibrated01.json](results/task014/predictions/sample_01_calibrated_prediction.json) |
| **Task 015** | VLA Workbench 独立桌面环境与常驻 Worker | `xvla-libero` | **PASS** | [Task 015 报告](docs/task015_workbench.md) | [acceptance.json](results/task015/acceptance.json) | [curves.png](evidence/task015/action_curves_sample01.png) |
| **Task 016** | 7D 动作物理语义核验与 12 组离线基准测试 | `xvla-libero` | **PASS** | [Task 016 规范](docs/task016_action_semantics.md) / [验收](docs/task016_acceptance_report.md) | [action_stats.json](results/task016/metrics/action_statistics.json) | [record01.json](results/task016/records/sample_01_record.json) |
| **Task 017（初期 60 步）** | X-VLA + LIBERO 仿真闭环与多种子重复性测试 | `xvla-libero` | **PASS** | [闭环总结](docs/task017_libero_closed_loop.md) / [验收报告](docs/task017_acceptance_report.md) | [closed_loop.json](results/task017/metrics/closed_loop_metrics.json) | [init.png](evidence/task017/episode_seed_42_step_000_init.png) / [final.png](evidence/task017/episode_seed_42_final.png) |
| **Task 017（完整长程）** | 24 次推理/664 步双杯拾放，LIBERO 判定 3/3 成功（第二只杯未观察到张爪） | `xvla-libero` | **ACCEPTED (有边界)** | [完整报告](docs/task017_full_rollout.md) / [验收报告](docs/task017_full_rollout_acceptance.md) | [episodes.json](results/task017/metrics/episodes.json) / [manipulation.json](results/task017/metrics/manipulation.json) | [mug1_placed.png](evidence/task017/full_rollout_ep00_0090_mug1_placed.png) / [final_success.png](evidence/task017/full_rollout_ep00_0223_final_success.png) |
| **Task 018** | 夹爪抓放专项审计与 Workbench 机械臂运行监控回放 (含审查定向修复) | `xvla-libero` | **ACCEPTED / 已闭环** | [专项报告](docs/task018_grasp_monitor_and_release.md) / [验收报告](docs/task018_grasp_monitor_and_release_acceptance.md) / [审查修复报告](docs/task018_review_fixes.md) | [audit.json](results/task018/metrics/grasp_release_audit.json) / [acceptance.json](results/task018/acceptance.json) | [offline.png](evidence/task018/offline_monitor_isolation.png) / [mug1_release.png](evidence/task018/replay_mug1_place_and_release.png) / [mug2_success.png](evidence/task018/replay_mug2_success_touchdown.png) / [desktop.png](evidence/task018/windows_desktop_real_verification.png) |
| **Task 019 / R1** | Workbench 连续视频回放、状态数据可信度与归档修复 | `xvla-libero` | **ACCEPTED_WITH_LIMITATIONS** | [Task019 技术报告](docs/task019_replay_video.md) / [R1 返修报告](https://github.com/Crazypsy92/vla-validation-records/blob/task019-review/docs/task019_r1_repair.md) | [video_metadata.json](results/task019/metrics/video_metadata.json) / [acceptance.json](results/task019/acceptance.json) | [复审截图](https://github.com/Crazypsy92/vla-validation-records/tree/task019-review/evidence/task019) |
| **Task 020** | Workbench 书本抓放官方任务验证 | `xvla-libero` | **GOAL_MET_WITH_LIMITATIONS / 待审核** | [Task020 Issue #4](https://github.com/Crazypsy92/vla-validation-records/issues/4) | [结题报告](docs/task020_goal_met_with_limitations.md) | 2 个官方成功，1 个资源中断未完成 |

---

## 四、当前已完成能力与未完成能力边界

### 4.1 已完成能力（Validated Capabilities）
- [x] **多模态输入对齐**：支持 Workspace Camera（全局视角）与 Wrist Camera（手腕视角）双摄 RGB 图像同步采样与归一化预处理；
- [x] **机器人本体状态投影**：支持 8D 本体感知（3D 位置 + 3D 轴角姿态 + 2D 夹爪）至模型内部 9D 张量的无损映射；
- [x] **动作空间物理语义纠偏**：纠正了“欧拉角误用”与“绝对位姿误当位移增量”的历史认知偏差，标定了绝对笛卡尔坐标与轴角旋转向量的真实物理单位；
- [x] **独立桌面上位机与常驻进程通信**：GUI 界面与深度学习推理环境解耦，实现 JSON Lines 高可靠 IPC 协议与模型常驻显存/内存；
- [x] **仿真环境动态闭环与滚动时域控制**：完成 MuJoCo 底层控制器对接，实现了执行前 15 步即触发动态重规划的 RHC 连续闭环控制；
- [x] **跨随机种子高度可重复性**：3 组独立随机种子下，末端执行器平均位移模长为 $0.1696\text{ m}$，且空间坐标离散误差 $<1.5\text{ mm}$。
- [x] **机械臂运行监控与历史回放系统**：VLA Workbench 落地 Plan / Command / Feedback 三层严格隔离，离线反馈严格标灰显示 N/A，支持轻量秒级回放、步进拖拽与双视角相机画面同步；
- [x] **长程抓放全流程物理审计**：查清 Seed 144 空中抬升 9.99cm 事实，查明 LeRobot `terminated=done or is_success` 终止机制，证实模型在终态动作块中已预测张爪释放指令。

### 4.2 未完成能力与现存瓶颈（Known Limitations）
- [ ] **物理机械臂实体适配**：尚未适配真实物理硬件（如 ROS 2 驱动层、实物 Realsense 深度相机校准、机械臂硬件急停保护）；
- [ ] **长程任务与主动释放**：现有初期 60 步归档未完成双杯放置（0/3）；较新完整回合归档 LIBERO 3/3，但第二杯未观察到主动释放，接触/抓持判据存在待复核例外；
- [ ] **CPU 推理时延瓶颈**：在没有独立 GPU 加速时，CPU 端单次前向耗时约 40~50 秒，难以满足 20Hz 实时在线伺服控制需求；
- [ ] **复杂接触动力学与滑移抗扰**：当前尚未加入力控反馈（F/T Sensor），在重接触或物体打滑场景下缺乏自主重试重捕获机制。

---

## 五、后续发展规划 (Roadmap)

1. **Task019 / R1（已完成，有限边界）**：完成真实视频连续回放、当前步状态可信度与归档数据修复；外部播放器验证保留为非阻断项；
2. **Task020（结题待审核）** 已验证 Workbench 书本抓放达到 LIBERO 官方成功。Seed 203 的资源中断仍保留在验收记录中。
3. **Task021（后续候选）**：根据 Task020 失败类型，再决定是否开展随机位置、视角变化、遮挡或任务组合的鲁棒性测试；
4. **真实机器人与边缘部署（后续）**：待机器人、相机和控制机型号明确后，再评估 ROS 2 对接、必要的数据适配、微调及 CPU/GPU/NPU 优化；当前不提前承诺实机效果。

---

## 六、归档资产与清单

- **发布白名单清单与校验结果**：[publication_manifest.md](manifests/publication_manifest.md)
- **机器可读元数据清单**：[publication_manifest.json](manifests/publication_manifest.json)
