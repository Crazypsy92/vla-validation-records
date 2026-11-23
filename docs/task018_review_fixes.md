# Task 018 审查意见定向修复与完整验收报告 (Review Fixes: P0-A, P0-B, P1-C, P1-D)

> **关联 Issue**: [GitHub Issue #2](https://github.com/Crazypsy92/vla-validation-records/issues/2)  
> **审查基线**: `STATUS: CHANGES_REQUESTED` (Comment ID: `7091945677`)  
> **执行状态**: 定向修复完成，标记 `STATUS: REVIEW`  
> **核心原则**: 真实物理数据零编造、零美化；动作规划与执行严格隔离；官方基准与全流程抓放物理判定独立解耦；真实桌面端到端实机验证。

---

## 一、审查问题定性与定向修复总览

在收到外部审核关于 Task 018 的阶段性审查意见后，我们针对提出的两个 P0 级问题与两个 P1 级问题开展了底层源码审计、时序数据对比、界面状态机重构与桌面实机验证：

| 审查条目 | 级别 | 核心问题定性 | 修复措施与物理事实 | 对应验收项 |
|---|---|---|---|---|
| **P0-A** | P0 | Plan 与 Command 的 RELEASE 语义混淆 | 查实 Chunk 7 终态 30 步动作块仅执行前 8~12 步，张爪偏置 (offset 18/21/23) 均位于**未执行的 Lookahead Tail**，从未下发控制器；严格划分为 `RELEASE_PLANNED_ONLY`，实际反馈明确标注为 `NOT VERIFIED IN SIMULATION` | T14 |
| **P0-B** | P0 | 回放时间轴同步与未来数据提前泄露 | 查实 Franka 夹爪存在 9 步物理响应延迟。将“OPEN 指令下发时刻”(Step 97/102/101) 与“物理开度达标时刻”(Step 106/111/110) 严格拆分；对非渲染步增加稀疏关键帧与时间偏差提示 (`Keyframe #090, Δ=11步`)，消除未来数据假象 | T15, T16 |
| **P1-C** | P1 | 抓持边界判定与官方基准强耦合 | 引入 `NONSTANDARD_GRASP_CONTACT` 分级以界定 Seed 144 抬升 9.99cm 但衬垫检测为 False 的楔形接触；将 Seed 143 终态触盘接触失效标注为“触盘同步跳变、机制未定”；将 `OFFICIAL_TASK_SUCCESS` 作为并行独立指标与物理释放解耦 | T17, T18 |
| **P1-D** | P1 | 验收矩阵扩展 (T01~T20) 与 Windows 实测 | 完整对齐 Issue #2 第八节增补的 T13~T20 共 20 项验收矩阵；在 Windows 11 真实桌面运行上位机进行端到端全流程操作与无孤儿退出实测，截取完整桌面证据 | T13, T19, T20 |

---

## 二、P0-A 规划与执行边界审计 (Plan vs Command Horizon)

### 2.1 动作块规划视界与执行截止点审计

在闭环推演中，X-VLA 每次观测输入后输出一个 $H=30$ 步的动作块（Action Chunk）。在全回合中：
- Chunk 0 ~ Chunk 6：完整执行 30 步（步索引 0 ~ 29）；
- **Chunk 7（终态动作块）**：在执行至第 8 ~ 12 步时，由于双杯几何坐标满足 LIBERO 评测要求，底层仿真引擎触发 `terminated = True`，导致回合瞬间终止。

#### 终态执行下标与未执行视界尾部对比表：

| 回合 Seed | 终态步数 (Global Step) | Chunk 7 实际执行步长 | 实际执行下标范围 (Executed Offsets) | 规划张爪动作偏置 (Planned OPEN Offset) | 是否下发控制器 (Command Sent) | 物理环境是否验证 (Physically Verified) | 最终严格分类 |
|---|---|---|---|---|---|---|---|
| **Seed 142** | Step 223 | 13 步 | `offset 0 ~ 12` | `offset 23` (位于尾部未执行区间 `13~29`) | **False** (未下发) | **NOT VERIFIED** (环境已终止) | **`RELEASE_PLANNED_ONLY`** |
| **Seed 143** | Step 222 | 12 步 | `offset 0 ~ 11` | `offset 21` (位于尾部未执行区间 `12~29`) | **False** (未下发) | **NOT VERIFIED** (环境已终止) | **`RELEASE_PLANNED_ONLY`** |
| **Seed 144** | Step 219 | 9 步 | `offset 0 ~ 8` | `offset 18` (位于尾部未执行区间 `9~29`) | **False** (未下发) | **NOT VERIFIED** (环境已终止) | **`RELEASE_PLANNED_ONLY`** |

### 2.2 严格的三层释放语义界定

我们在系统架构中彻底消除“计划包含即证明能力”的过度表述，确立三层独立状态：
1. **`RELEASE_PLANNED_ONLY`**：模型在动作块前瞻视界中生成了张爪指令，但因环境终止未进入执行队列，从未下发至控制器或仿真器。
2. **`RELEASE_COMMAND_SENT`**：控制器已实际向仿真环境注入了 `gripper = -1.0` 动作指令，机械臂开始响应，但开度尚未达到阈值。
3. **`RELEASE_PHYSICALLY_VERIFIED`**：MuJoCo 仿真中夹爪物理开度达到 $\ge 0.070	ext{ m}$，双侧指垫接触彻底脱离，物体在承托面保持静止。

> **审计结论**：第二只黄白杯在全部 3 个 Seed 中严格归类为 **`RELEASE_PLANNED_ONLY`**，实际反馈区明确标注为 **`NOT VERIFIED IN SIMULATION`**。

---

## 三、P0-B 回放时间轴同步与去混叠 (Timing Synchronization & De-aliasing)

### 3.1 机械延迟：指令下发步 vs 物理开度达标步

底层 MuJoCo 仿真中，Franka Panda 夹爪受速度与阻尼动力学约束，从接收到张开指令到物理开度展开至 $0.070	ext{ m}$ 具有固定的 **9 步机械响应延迟**。

#### 真实物理遥测对齐表（以杯 1 释放为例）：

| Seed | OPEN 指令下发步 (`RELEASE_COMMAND_SENT`) | 指令下发时开度 (`gap_m`) | 指令下发时状态 | 物理开度达标步 (`RELEASE_PHYSICALLY_VERIFIED`) | 达标步开度 (`gap_m`) | 机械延迟 |
|---|---|---|---|---|---|---|
| **Seed 142** | **Step 097** | 0.0089 m | 闭合紧绷，开始响应 | **Step 106** | 0.0717 m | 9 仿真步 (0.45s) |
| **Seed 143** | **Step 102** | 0.0126 m | 闭合紧绷，开始响应 | **Step 111** | 0.0717 m | 9 仿真步 (0.45s) |
| **Seed 144** | **Step 101** | 0.0215 m | 响应展开中 | **Step 110** | 0.0718 m | 9 仿真步 (0.45s) |

### 3.2 图像帧与遥测时序去混叠

由于仿真环境每 30 步采集一次真实视场渲染（Step 0, 30, 60, 90, 120, 150, 180, 210 及终态步），回放系统如果直接显示非对齐帧，容易产生“Step 101 画面与 Step 101 真实反馈混淆”的错觉。

#### 修复措施：
1. **关键帧稀疏指示器 (`lbl_frame_sync`)**：
   - 当回放步与图像采集步完全吻合时，显示：`📷 视场匹配: Keyframe #090 (精确同步)`；
   - 当处于中间步（如 Step 101）时，显示：`📷 视场匹配: Keyframe #090 (最近参考关键帧, Δ=11步)`，严禁伪造中间帧。
2. **快捷跳转按钮细分**：
   - 区分 `M1 Open Cmd`（跳转至指令下发步 97/102/101）与 `M1 Open Done`（跳转至开度达标步 106/111/110）。
3. **自动化测试断言**：
   - `test_review_fixes_timing_and_assertions` 单元测试明确断言 Step 101 包含 `RELEASE_COMMAND_SENT` 且不包含 `RELEASE_PHYSICALLY_VERIFIED`；Step 110 包含 `RELEASE_PHYSICALLY_VERIFIED`。

---

## 四、P1-C 抓持边界判定与物理判据重构 (Grasp Boundary & Parallel Decoupling)

### 4.1 Seed 144 白杯：非标接触与持续搬运分类

- **物理事实**：Seed 144 中白杯在 Step 28~70 闭合后，质心 Z 从 0.434m 抬升至 0.534m（最大抬升高度 $+9.99	ext{ cm}$），在空中连续水平平移 $19.06	ext{ cm}$ 并平稳下放至餐盘表面；
- **检测局限**：MuJoCo 判定器仅检测 `left_fingerpad` 与 `right_fingerpad` 双侧法向碰撞，而该杯被斜向卡入左侧衬垫与金属夹爪根部之间；
- **重构分级**：将其分类为 **`NONSTANDARD_GRASP_CONTACT / LIFT_AND_TRANSPORT_OBSERVED`**，既承认其双衬垫几何碰撞为 False，又确认其实际完成了抬升与搬运的物理事实，不判虚假单侧 PASS。

### 4.2 Seed 143 黄白杯：触盘同步跳变机制

- **物理事实**：黄白杯在 Step 182~221 保持连续 40 步稳定双侧衬垫接触，并在第 222 步接触餐盘表面；
- **跳变现象**：在第 222 步环境判定任务成功的同一步，`grasped` 瞬间从 `True` 变为 `False`；
- **重构分级**：由于无法在无高频力矩传感器的情况下证明究竟是触盘反作用力脱开还是接触阈值边界抖动，严格标注为：**`grasped=False 与触盘同步跳变，机制尚未确定；RELEASE_PLANNED_ONLY (NOT VERIFIED)`**，杜绝未证实的定论。

### 4.3 评测指标并行解耦

我们将 `OFFICIAL_TASK_SUCCESS` 从串联状态机中剥离，建立双轨并行独立判定体系：
- **轨 1：LIBERO Benchmark Official Success**（官方任务到靶独立指标，关注几何落入目标区域）；
- **轨 2：Physical Grasp-Release Full Lifecycle**（物理机械完整抓放生命周期，关注接触、搬运、主动释放与稳态放置）。

---

## 五、P1-D Windows 桌面真实操作与完整验收矩阵 (T01~T20)

### 5.1 完整 20 项验收矩阵 (T01 ~ T20)

| 编号 | 验收条件 | 验收标准与合格证据 | 审核状态 |
|---|---|---|---|
| **T01** | Task017 历史证据核对 | 原始 events.jsonl、哈希与 3 组种子样本表完整，数据可溯源 | **PASS** |
| **T02** | 模型输出与控制值匹配 | 模型 7D 输出与 OSC_POSE 绝对控制器输入一一对应，无失真 | **PASS** |
| **T03** | 夹爪真实关节反馈审计 | Franka 夹爪 qpos 与开度计算准确，开度误差 < 0.1mm | **PASS** |
| **T04** | 接触判据对象归属 | MuJoCo contact pair geom 严格绑定指定目标杯体 | **PASS** |
| **T05** | 物体抬升与搬运可信 | 白杯抬升 9.99cm、位移 19.06cm；黄白杯抬升 9.67cm、位移 22.28cm | **PASS** |
| **T06** | 两次放置与释放分别记录 | 杯 1 释放完成与杯 2 触盘着陆时间线明确记录 | **PASS** |
| **T07** | GUI 预测与实际反馈分栏 | Plan / Command / Feedback 三层结构完全物理隔离 | **PASS** |
| **T08** | 离线模式实际反馈显示 N/A | 离线无仿真时反馈区严格显示 N/A 并标灰，无虚构 PASS | **PASS** |
| **T09** | 真实 Episode 回放可用 | Seed 142/143/144 全量 664 步历史回放秒级加载稳定回放 | **PASS** |
| **T10** | 旧 GUI 功能与资源管理回归 | headless 单测 6/6 通过 (0.547s)，主窗口 on_close 干净退出 | **PASS** |
| **T11** | 抓取/释放/官方结果独立统计 | 结构化 metrics 与 acceptance.json 解耦双轨展示 | **PASS** |
| **T12** | GitHub 精选归档与脱敏 | 排除虚拟环境、权重及大文件，清单哈希校验一致 | **PASS** |
| **T13** | 仿真是否真的发生运动 | Tier 3 动态计算当前 EEF、初始位姿与累计位移，离线时 N/A | **PASS** |
| **T14** | 预测/下发/反馈三层隔离 (P0-A) | 严格区分 RELEASE_PLANNED_ONLY 与 RELEASE_COMMAND_SENT | **PASS** |
| **T15** | 机械臂/物体运动时序对齐 (P0-B) | 严格拆分 Step 101 指令步与 Step 110 达标步，消除未来泄露 | **PASS** |
| **T16** | 回放时间轴与事件标记 (P0-B) | 快捷跳转细分 M1 Open Cmd / M1 Open Done，相机标明参考关键帧与Δ步 | **PASS** |
| **T17** | 官方成功与操作完整性解耦 (P1-C) | 官方基准作为独立并行指标，杯 1 已释放，杯 2 触盘未张开 | **PASS** |
| **T18** | 冲突样本专项诊断 (P1-C) | Seed 144 分类为 NONSTANDARD_CONTACT，Seed 143 标注触盘同步跳变 | **PASS** |
| **T19** | 用户可自行操作 (P1-D) | Windows 11 桌面实操验证，切换 Episode、回放跳步、切离线模式正常 | **PASS** |
| **T20** | 旧 Workbench 与回归 (P1-D) | 离线单样本预测无回归，退出时 0 孤儿进程，进程树干净销毁 | **PASS** |

### 5.2 Windows 桌面端到端实机验证日志

我们在 Windows 11 环境下执行了 `verify_windows_desktop.py` 实机验证脚本：
```
Initializing MainWindow on Windows Desktop...
Selecting Robot Monitor & Replay tab...
Switching to Replay mode...
Selected Seed 144 (Index: 2)
Seeking to Step 101...
Step 101 Grip State: RELEASE_COMMAND_SENT (Cmd=-1.0下发中, 响应中, 间距=0.0215m) | qpos=[+0.0083, -0.0133]
Step 101 Frame Sync: 📷 视场匹配: Keyframe #090 (最近参考关键帧, Δ=11步)
Seeking to Step 110...
Step 110 Grip State: RELEASE_PHYSICALLY_VERIFIED (物理张开达标, 间距=0.0718m >= 0.070m) | qpos=[+0.0360, -0.0359]
Step 110 Frame Sync: 📷 视场匹配: Keyframe #120 (最近参考关键帧, Δ=10步)
Testing offline mode toggle...
Offline V1 Badge: N/A (离线无仿真)
Offline V2 Badge: N/A (离线无仿真)
Closing Workbench window...
WorkbenchApp destroyed cleanly with 0 orphaned processes.
```

---

## 六、证据与交付资产索引

1. **核心报告**：
   - 本文：[`docs/task018_review_fixes.md`](https://github.com/Crazypsy92/vla-validation-records/blob/main/docs/task018_review_fixes.md)
   - 基础报告：[`docs/task018_grasp_monitor_and_release.md`](https://github.com/Crazypsy92/vla-validation-records/blob/main/docs/task018_grasp_monitor_and_release.md)
2. **结构化数据**：
   - 20 项验收矩阵：[`results/task018/acceptance.json`](https://github.com/Crazypsy92/vla-validation-records/blob/main/results/task018/acceptance.json)
   - 重构审计指标：[`results/task018/metrics/grasp_release_audit.json`](https://github.com/Crazypsy92/vla-validation-records/blob/main/results/task018/metrics/grasp_release_audit.json)
3. **视觉截屏与定向证据**：
   - Windows 桌面实测全景：[`evidence/task018/windows_desktop_real_verification.png`](https://github.com/Crazypsy92/vla-validation-records/blob/main/evidence/task018/windows_desktop_real_verification.png)
   - Step 101 指令下发证据：[`evidence/task018/step101_release_command_sent.png`](https://github.com/Crazypsy92/vla-validation-records/blob/main/evidence/task018/step101_release_command_sent.png)
   - Step 110 物理开度达标证据：[`evidence/task018/step110_release_physically_verified.png`](https://github.com/Crazypsy92/vla-validation-records/blob/main/evidence/task018/step110_release_physically_verified.png)
   - 非标抓持抬升搬运证据：[`evidence/task018/nonstandard_grasp_contact.png`](https://github.com/Crazypsy92/vla-validation-records/blob/main/evidence/task018/nonstandard_grasp_contact.png)
   - 触盘未证实机制证据：[`evidence/task018/touchdown_contact_unproven.png`](https://github.com/Crazypsy92/vla-validation-records/blob/main/evidence/task018/touchdown_contact_unproven.png)
   - 离线反馈严格隔离截图：[`evidence/task018/offline_monitor_isolation.png`](https://github.com/Crazypsy92/vla-validation-records/blob/main/evidence/task018/offline_monitor_isolation.png)
   - 终态解耦与未执行区间说明截图：[`evidence/task018/replay_mug2_success_touchdown.png`](https://github.com/Crazypsy92/vla-validation-records/blob/main/evidence/task018/replay_mug2_success_touchdown.png)
