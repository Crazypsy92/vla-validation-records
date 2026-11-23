# VLA 具身决策模型验收成果与评测档案库 (VLA Validation Records)

[![GitHub License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-WSL2%20%7C%20Ubuntu%2024.04-orange.svg)]()
[![Model](https://img.shields.io/badge/Model-X--VLA%20(879M)%20%7C%20SmolVLA%20(450M)-green.svg)]()
[![Simulation](https://img.shields.io/badge/Simulation-LIBERO%20%7C%20MuJoCo%203.8.1-brightgreen.svg)]()

本仓库是个人具身智能学习与技术验证体系（`ai-learning`）中 **VLA（Vision-Language-Action）具身决策层** 的独立公开归档仓库。

本仓库**仅用于归档保存**阶段验收报告、物理语义规范、结构化实验指标与精选仿真证据，不包含未经裁剪的模型权重、庞大数据集或本地开发环境。

---

## ⚠️ 重要声明与验证边界 (Important Disclaimers)

> [!IMPORTANT]
> **本仓库所记录的所有能力、指标与测试成果，均严格限定在仿真环境与离线基准测试范围之内。**
> 
> 必须明确知悉以下技术边界：
> 1. **当前成果属于纯仿真与离线验证**：所有闭环测试均在 MuJoCo 3.8.1 物理引擎及 LIBERO 仿真环境中完成，**不代表已经在真实物理机械臂（Real Robot Arm）上完成实体部署**；
> 2. **不代表双臂协同系统已通过验证**：虽然模型支持多领域输入，但当前全链路闭环仅针对单臂（Franka Panda 7-DoF + 2指夹爪）桌面操作场景；
> 3. **不代表端侧轻量化嵌入式部署已完成**：当前推理均运行于 x86_64 CPU 架构的 Python 环境下，尚未移植至边缘算力盒（如 Jetson Orin 或嵌入式 NPU）；
> 4. **不代表完整抓取-放置长程任务已全部通过**：在 Task 017 闭环测试中，受限于单回合 60 步的早期时域，机械臂已实现稳定下探与趋近目标，但尚未达到判定最终双杯成功放置的 300~600 步终态；**本归档坚决实事求是，绝不将动作输出混淆为物理操作成功**。

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
| **SmolVLA Base** | 450M 参数（SmolLM2-135M + 视觉编码器） | Diffusion Head (50 Diffusion Steps) | 通用桌面抓取、ALOHA 双臂 | 快速端侧离线前向与输入鲁棒性基线 (Task 010~011) |
| **X-VLA Base** | 879.48M 参数（SigLIP + Llama-3.2-1B） | Action Transformer + Flow Matching | LIBERO, ALOHA, BridgeData V2 | 跨本体、多领域泛化推理能力验证 (Task 012) |
| **X-VLA LIBERO** | 879.48M 参数（特定环境微调权重） | Flow Matching (30 步动作块预测) | LIBERO (Franka Panda 7D) | 物理语义审计与仿真闭环核心主力模型 (Task 013~017) |

---

## 三、Task 010 ～ Task 017 阶段成果与导航索引

| 阶段任务 | 任务主题与核心突破 | 核心模型 | 验收判定 | 正式报告 | 关键指标与记录 | 精选证据 |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| **Task 010** | SmolVLA (450M) 基线构建与 CPU 离线推理 | `smolvla_base` | **PASS** | [Task 010 报告](docs/task010_smolvla_baseline.md) | [metrics.json](results/task010/metrics/inference_metrics.json) | [case01.json](results/task010/predictions/case_001_pick_blue_block.json) |
| **Task 011** | 输入敏感度、随机噪声鲁棒性与语义消歧 | `smolvla_base` | **PASS** | [Task 011 报告](docs/task011_input_sensitivity.md) | [experiments.json](results/task011/metrics/experiments.json) | [audit.json](results/task011/metrics/processor_audit.json) |
| **Task 012** | X-VLA 离线推理与跨本体（3-Domain）泛化 | `xvla-base` | **PASS** | [Task 012 报告](docs/task012_xvla_inference.md) | [metrics.json](results/task012/metrics/inference_metrics.json) | [libero.json](results/task012/predictions/case_001_domain0_libero.json) |
| **Task 013** | LIBERO 机器人真实数据集基准评测 | `xvla-libero` | **PASS** | [Task 013 报告](docs/task013_libero_offline_action_validation.md) | [metrics.json](results/task013/metrics/inference_metrics.json) | [sample01.json](results/task013/predictions/sample_01_prediction.json) |
| **Task 014** | 全链路动作空间异常审计与处理器标定 | `xvla-libero` | **PASS** | [Task 014 报告](docs/task014_xvla_pipeline_audit.md) | [calibrated.json](results/task014/metrics/calibrated_metrics.json) | [calibrated01.json](results/task014/predictions/sample_01_calibrated_prediction.json) |
| **Task 015** | VLA Workbench 独立桌面环境与常驻 Worker | `xvla-libero` | **PASS** | [Task 015 报告](docs/task015_workbench.md) | [acceptance.json](results/task015/acceptance.json) | [curves.png](evidence/task015/action_curves_sample01.png) |
| **Task 016** | 7D 动作物理语义核验与 12 组离线基准测试 | `xvla-libero` | **PASS** | [Task 016 规范](docs/task016_action_semantics.md) / [验收](docs/task016_acceptance_report.md) | [action_stats.json](results/task016/metrics/action_statistics.json) | [record01.json](results/task016/records/sample_01_record.json) |
| **Task 017** | X-VLA + LIBERO 仿真闭环与多种子重复性测试 | `xvla-libero` | **PASS** | [闭环总结](docs/task017_libero_closed_loop.md) / [验收报告](docs/task017_acceptance_report.md) | [closed_loop.json](results/task017/metrics/closed_loop_metrics.json) | [init.png](evidence/task017/episode_seed_42_step_000_init.png) / [final.png](evidence/task017/episode_seed_42_final.png) |

---

## 四、当前已完成能力与未完成能力边界

### 4.1 已完成能力（Validated Capabilities）
- [x] **多模态输入对齐**：支持 Workspace Camera（全局视角）与 Wrist Camera（手腕视角）双摄 RGB 图像同步采样与归一化预处理；
- [x] **机器人本体状态投影**：支持 8D 本体感知（3D 位置 + 3D 轴角姿态 + 2D 夹爪）至模型内部 9D 张量的无损映射；
- [x] **动作空间物理语义纠偏**：纠正了“欧拉角误用”与“绝对位姿误当位移增量”的历史认知偏差，标定了绝对笛卡尔坐标与轴角旋转向量的真实物理单位；
- [x] **独立桌面上位机与常驻进程通信**：GUI 界面与深度学习推理环境解耦，实现 JSON Lines 高可靠 IPC 协议与模型常驻显存/内存；
- [x] **仿真环境动态闭环与滚动时域控制**：完成 MuJoCo 底层控制器对接，实现了执行前 15 步即触发动态重规划的 RHC 连续闭环控制；
- [x] **跨随机种子高度可重复性**：3 组独立随机种子下，末端执行器平均位移模长为 $0.1696\text{ m}$，且空间坐标离散误差 $<1.5\text{ mm}$。

### 4.2 未完成能力与现存瓶颈（Known Limitations）
- [ ] **物理机械臂实体适配**：尚未适配真实物理硬件（如 ROS 2 驱动层、实物 Realsense 深度相机校准、机械臂硬件急停保护）；
- [ ] **长程任务全流程完成率**：双马克杯长程复合放置任务需要 300~600 步，目前评测在 60 步内展示了稳定下探与趋近，但未完全达成物体入盘的终态；
- [ ] **CPU 推理时延瓶颈**：在没有独立 GPU 加速时，CPU 端单次前向耗时约 40~50 秒，难以满足 20Hz 实时在线伺服控制需求；
- [ ] **复杂接触动力学与滑移抗扰**：当前尚未加入力控反馈（F/T Sensor），在重接触或物体打滑场景下缺乏自主重试重捕获机制。

---

## 五、后续发展规划 (Roadmap)

1. **加速推理引擎引入**：探索 ONNX Runtime / TensorRT-LLM / vLLM 对 VLA 骨干的量化加速（FP8 / INT4），将单步推理时延压缩至百毫秒级；
2. **多任务 LIBERO 全覆盖评测**：扩展至 `libero_spatial` 与 `libero_object` 等单目标快速放置任务，建立 300 步全流程高成功率基准；
3. **真实机械臂 ROS 2 桥接驱动准备**：开发 ROS 2 Node 包装层，统一仿真与实体机器人的 JointTrajectoryController / CartesianPose 接口。

---

## 六、归档资产与清单

- **发布白名单清单与校验结果**：[publication_manifest.md](manifests/publication_manifest.md)
- **机器可读元数据清单**：[publication_manifest.json](manifests/publication_manifest.json)
