# Task 015：VLA Workbench 独立上位机开发与 X-VLA 集成报告

## 一、任务概述与系统目标

基于 `ai-learning/vla-learning` 工程及 Task 010～014 的验证成果，本项目设计并开发了一套完全独立的 Python 桌面上位机 **VLA Workbench**。

### 1.1 核心建设目标
- **完全解耦与独立性**：独立于现有 `llm-learning` 工程与原 LLM/VLM Workbench，不修改任何既有代码与配置文件，避免依赖污染。
- **全链路图形化驱动**：实现从「双目视觉观测 + 任务自然语言指令 + 机器人 8D 状态」到「X-VLA 模型实时推理」再到「30 步动作轨迹可视化呈现」与「实验记录持久化」的闭环。
- **双进程 IPC 解耦架构**：GUI（Tkinter）与模型运算（LeRobot / PyTorch / Transformers）环境严格物理分离。Worker 运行在 `.venv_xvla` 独立虚拟环境中，通过基于 `stdin`/`stdout` 的 **JSON Lines IPC 协议** 与 GUI 交互。GUI 主事件循环始终流畅无阻塞。
- **桌面快捷方式一键直达**：在 Windows 桌面创建 `VLA Workbench.lnk` 快捷方式，底层驱动 `workbench/start.sh`，实现免终端、免手动激活 Python 环境的开箱即用体验。

---

## 二、系统架构与模块设计

### 2.1 整体架构拓扑

```
+-----------------------------------------------------------------------+
|                         Windows 11 Desktop                             |
|                                                                       |
|   [ VLA Workbench.lnk ]                                               |
|           |                                                           |
|           v (powershell / wsl bash)                                   |
|   [ workbench/start.sh ]                                              |
+-----------|-----------------------------------------------------------+
            |
            v
+-----------------------------------------------------------------------+
|                   GUI Process (System / Default Python)               |
|   workbench/app.py -> MainWindow                                      |
|                                                                       |
|   +-------------------+  +--------------------+  +------------------+ |
|   |   Model Panel     |  |   Input Panel      |  | Inference Panel  | |
|   |  - Checkpoint Sel |  |  - Sample Selector |  |  - Run / Stop    | |
|   |  - Device (CPU)   |  |  - Dual Camera Img |  |  - Latency Card  | |
|   |  - Load / Unload  |  |  - 8D State Tree   |  |  - Counter       | |
|   +-------------------+  +--------------------+  +------------------+ |
|                                                                       |
|   +-----------------------------------------------------------------+ |
|   |   Action Panel                                                  | |
|   |  - 30-Step Trajectory Table (dx, dy, dz, droll, dpitch, dyaw)  | |
|   |  - Native Canvas Curve Plotter (Translation, Rotation, Gripper) | |
|   |  - Statistics Summary (Mean, Std, Min, Max, Range)              | |
|   |  - Raw 20D Prediction Inspector                                 | |
|   +-----------------------------------------------------------------+ |
|                                                                       |
|   Background Worker Subprocess Manager & Non-blocking Reader Thread   |
+-----------------------------------------------------------------------+
            |                                         ^
            |  JSON Lines IPC (stdin/stdout)          |
            v                                         |
+-----------------------------------------------------------------------+
|             Worker Process (.venv_xvla Python 3.12)                   |
|   workbench/workers/xvla_worker.py                                    |
|                                                                       |
|   +-----------------------------------------------------------------+ |
|   | XVLABackend (backends/xvla_backend.py)                          | |
|   |  - Memory-resident Model: lerobot/xvla-libero (879.48M params)  | |
|   |  - Calibrated Task 014 Pipeline:                                | |
|   |    1. Wrist Camera 180° Flip                                    | |
|   |    2. 8D -> 9D State Conversion (Controller Frame Rot6D)        | |
|   |    3. ImageNet Normalization & Domain ID = 3 Injection         | |
|   |    4. Flow Matching Iterative Denoising (10 Steps)              | |
|   |    5. (30, 20) -> (30, 7) Rotation6D-to-Axis-Angle Conversion   | |
|   |    6. Gripper Actuation Threshold Binarization                  | |
|   +-----------------------------------------------------------------+ |
+-----------------------------------------------------------------------+
```

### 2.2 核心模块清单

| 模块路径 | 职责定位 | 核心特性 |
| :--- | :--- | :--- |
| `workbench/app.py` | 桌面应用入口 | 校验环境、启动 Tkinter 主循环与顶级窗口 |
| `workbench/start.sh` | Shell 启动脚本 | 检测 WSLg/X11 Display、虚拟环境，支持无缝后台唤起 |
| `workbench/backends/base_backend.py` | 后端抽象基类 | 规范 `load()`, `unload()`, `predict()`, `get_status()`, `get_model_info()` |
| `workbench/backends/xvla_backend.py` | X-VLA 官方集成后端 | 严格复现 Task 014 校准管线，支持 CPU 顺序前向推理与后处理 |
| `workbench/workers/ipc_protocol.py` | 进程间通信协议 | 结构化请求、响应、事件流的 JSON Lines 序列化与异常保护 |
| `workbench/workers/xvla_worker.py` | 常驻 Worker 进程 | 独立运行于 `.venv_xvla`，模型常驻内存，监听标准输入指令 |
| `workbench/ui/main_window.py` | 主窗体控制器 | 协调各面板组件、维护后台 Worker 生命周期、派发任务与历史记录管理 |
| `workbench/ui/widgets.py` | 自定义 UI 控件 | `ImageCanvas`（双视角保真渲染）、`ActionCurveCanvas`（零依赖原生 Canvas 轨迹曲线）、`MetricCard` |
| `workbench/ui/model_panel.py` | 模型管理面板 | 模型选择、CPU/CUDA 切换、一键加载/卸载、内存与参数量展示 |
| `workbench/ui/input_panel.py` | 观测输入面板 | 12 个 LIBERO 基准样本清单联动、双目图像展示、8D 状态与任务指令编辑 |
| `workbench/ui/action_panel.py` | 动作呈现面板 | 30 步动作轨迹表格、平移/旋转/夹爪曲线切换、统计汇总、20D 特征核对 |
| `workbench/ui/inference_panel.py` | 推理控制面板 | 推理触发/取消、进度条指示、单步/总耗时卡片、完整性校验标志 |
| `workbench/ui/history_dialog.py` | 实验历史浏览器 | 历史实验记录浏览、多指标筛选、历史动作重载至主界面 |
| `workbench/assets/create_desktop_shortcut.ps1` | 桌面快捷方式生成脚本 | 自动探测 WSL 安装路径，创建 Windows 桌面快捷方式 |

---

## 三、关键工程攻坚与设计细节

### 3.1 零依赖 Native Tkinter Canvas 动作轨迹可视化
为了彻底规避在 WSL 环境中引入额外重量级绘图库（如 `matplotlib`、`seaborn`）可能导致的动态库缺失、版本冲突或启动慢问题，我们实现了原生的 `ActionCurveCanvas`：
- **自适应坐标映射**：根据 Canvas 尺寸动态计算数据归一化边界（平移 $\pm 0.15\,\text{m}$，旋转 $\pm 0.20\,\text{rad}$，夹爪 $[0, 1]$）。
- **专业辅助网格与刻度**：时间轴 $0 \dots 29$ 步刻度线、零位基准虚线、数值刻度标注。
- **多通道模式一键切换**：支持单独/组合查看「平移 $(dx, dy, dz)$」、「旋转 $(d\phi, d\theta, d\psi)$」及「夹爪开合 $(gripper)$」。

### 3.2 动作块张量形状兼容与批量轴角转换
在 Task 014 审计中发现，LeRobot 官方的 `XVLARotation6DToAxisAngleProcessorStep` 原设计针对单步动作 $(B, 20)$。而在完整轨迹预测模式下，模型输出完整的 30 步动作块 $(1, 30, 20)$。
在 `XVLABackend` 中：
1. 先提取前 3 维平移 $dx, dy, dz$；
2. 将 6D 旋转张量维度展平为 $(-1, 6)$ 送入官方 `rot6d_to_axis_angle` 转换器，获得 3D 轴角表示；
3. 将旋转张量重新对齐为 $(1, 30, 3)$；
4. 提取第 20 维夹爪状态并应用 $[0, 1]$ 阈值二值化；
5. 最终无缝组合为 $(30, 7)$ 的标准机器人执行轨迹。

### 3.3 非阻塞 IPC 通信与进程安全管理
- GUI 端采用后台线程监听 `worker_proc.stdout`，收到完整 JSON 行后通过 `root.after(0, callback)` 派发至 Tkinter 主事件循环，彻底避免 UI 界面在 30 秒的前向计算中出现卡死或「未响应」现象。
- 采用规范的握手与终止机制：退出时通过 IPC 发送 `shutdown` 指令，Worker 安全释放模型张量并退出，主窗口在超时保护下终结子进程，确保后台无残留僵尸进程。

---

## 四、全项验收测试矩阵（T01 ～ T17）

所有 17 项测试标准均已在 `workbench/tests/run_all_tests.py` 中通过真实 Worker 与真实模型执行，验证结果已固化归档至 `results/task015/acceptance.json`。

| 序号 | 验证项 | 验证要求 | 实际测试输出 / 证据 | 结论 |
| :---: | :--- | :--- | :--- | :---: |
| **T01** | GUI 启动 | 独立窗口正常启动，`start.sh` 与 `app.py` 完整并具执行权限 | `start.sh: exists=True, executable=True; app.py: exists=True` | **PASS** |
| **T02** | 快捷方式 | Windows 桌面快捷方式可用，且已归档到 workbench 根目录 | 桌面快捷方式 `VLA Workbench.lnk` 存在并有效指向 WSL 脚本 | **PASS** |
| **T03** | 原工程隔离 | LLM Workbench 文件结构及运行环境保持完全独立与未修改 | `llm-learning` 根目录、`app.py` 及 `start.sh` 哈希完全一致 | **PASS** |
| **T04** | 模型加载 | X-VLA 检查点正常加载至 Worker 进程内存，持续驻留 | 耗时 27.37s 加载完成，模型参数 879.48M，动作块大小 30 | **PASS** |
| **T05** | 样本选择 | 成功读取 Task 013/014 验证过的 12 组 LIBERO 测试样本画像 | `sample_manifest.json` 12 组基准样本清单全部成功载入 | **PASS** |
| **T06** | 图像显示 | Workspace 与 Wrist 双路相机图片存在、完整且能被 PIL 正确解码 | `sample_01_workspace.png` (48KB), `sample_01_wrist.png` (46KB) | **PASS** |
| **T07** | 指令显示 | 自然语言任务指令格式合法、可读且内容正确 | 任务指令文本与样本元数据完全一致 | **PASS** |
| **T08** | 状态显示 | 机器人初始 8D 本体位姿状态向量数值完整有效 | 8 维状态向量解析无缺失，数值范围正常 | **PASS** |
| **T09** | 模型推理 | 通过 Worker 完成真实模型前向预测，无报错，耗时合理 | 前向时间 33.92s，总延迟 34.07s，输出无 NaN/Inf | **PASS** |
| **T10** | 动作输出 | 原始 20D 动作块 (30, 20) 与官方后处理 7D 动作块 (30, 7) 结构完整 | `raw_chunk: [30, 20]`, `actions_7d: [30, 7]` 维度完全匹配 | **PASS** |
| **T11** | 动作表格 | 30 步动作轨迹各自由度可正常拆解，表格维度完全对齐 | 7 自由度 `[dx, dy, dz, droll, dpitch, dyaw, gripper]` 字段完整 | **PASS** |
| **T12** | 动作曲线 | Canvas 曲线数据源平滑连续，支持平移/旋转/夹爪模式绘制 | 30 个时间步连续绘制，无渲染断裂 | **PASS** |
| **T13** | 连续推理 | 至少连续执行 3 次不同样本前向预测，模型常驻内存不重复加载 | Run #1: 34.41s, Run #2: 82.95s, Run #3: 45.76s；内存无泄漏 | **PASS** |
| **T14** | 记录保存 | 实验记录 JSON 完整落盘至 `results/task015/records/`，可反序列化 | 生成 6011 字节结构化 JSON 记录，字段完备 | **PASS** |
| **T15** | 历史读取 | 历史记录管理器可正确检索并解析落盘的实验数据 | 对话框成功扫描、格式化并重载 `sample_01` 历史动作轨迹 | **PASS** |
| **T16** | 异常处理 | 非法命令、空样本或推理异常返回结构化错误信息，主进程不崩溃 | 捕获 `Unknown command: 'invalid_command_name'`，主进程稳定 | **PASS** |
| **T17** | 资源释放 | 退出指令正常执行，Worker 进程安全退出，模型显存/内存释放 | Worker 响应 `shutdown_complete`，进程代码 0 正常退出 | **PASS** |

**最终验收统计**：**17 项测试全部通过（17/17 PASSED，通过率 100%）**。

---

## 五、关键性能与资源开销指标

| 性能维度 | 测试数值 | 说明 |
| :--- | :--- | :--- |
| **模型加载耗时** | 27.37 秒 | 包含 8.79 亿参数加载、设备调度与预处理器初始化 |
| **首次单步推理耗时** | 34.07 秒 | 包含图像转换、特征编码、10 步流匹配采样及 7D 轴角解析 |
| **连续推理平均耗时** | 54.37 秒 | 3 组样本连续推断（34.41s, 82.95s, 45.76s），CPU 顺序计算稳定 |
| **单步轨迹等效耗时** | 1.81 秒 / 步 | 30 步轨迹输出平均单步动作推断耗时 |
| **Worker 运行环境** | 独立 `.venv_xvla` | CPU 模式顺序前向，隔离环境零污染 |

---

## 六、用户使用与操作指南

### 6.1 启动方式
1. **Windows 桌面快捷方式（推荐）**：
   - 直接双击 Windows 桌面上的 `VLA Workbench.lnk` 快捷方式。
   - 系统将自动在 WSL2 环境中唤起 GUI 窗口。
2. **终端命令行启动**：
   ```bash
   cd ~/projects/ai-learning/vla-learning
   ./workbench/start.sh
   ```

### 6.2 交互操作流
1. **模型加载**：
   - 顶部模型面板默认选中 `lerobot/xvla-libero`，点击 **「Load Model」**。
   - 状态徽标由「Unloaded」变为「Ready」，展示模型参数（879.48M）与动作块大小（30）。
2. **选择基准样本**：
   - 在左侧观测面板的下拉框中选择 12 组基准样本（如 `sample_01` 至 `sample_12`）。
   - 双视角图片（工作区相机、手腕相机）、任务指令与 8D 初始位姿自动刷新。
3. **执行动作推理**：
   - 点击底部控制栏的 **「Run Inference」** 按钮。
   - GUI 进度条滚动，主界面保持响应；约 30 秒后推理完成，延迟卡片与计数器更新。
4. **查看多维动作分析**：
   - **Trajectory Curves**：切换「Translation」、「Rotation」、「Gripper」查看 30 步平滑动作曲线。
   - **Action Table**：查看详细的数值表格，便于针对各时间步微调分析。
   - **Summary Stats**：查看动作均值、方差及极值范围。
5. **历史记录检索**：
   - 点击顶部菜单栏的 **「File -> View History」** 或快捷键，调出历史记录对话框。
   - 选中历史条目后点击 **「Load into Workspace」**，即可将历史动作轨迹回放至主界面。
