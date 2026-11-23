# Task 019 · 连续仿真回放复审

本轮复用 Task 017 的三个完整回合。播放器、原始录像与逐步日志在本地一起复核。Task 019 交回复审，Task 020 等正式验收。

| 种子 | 帧数 | 控制步 | 帧率 | 最后一步时间 |
| --- | ---: | ---: | ---: | ---: |
| 142 | 224 | 223 | 20 FPS | 11.15 s |
| 143 | 223 | 222 | 20 FPS | 11.10 s |
| 144 | 220 | 219 | 20 FPS | 10.95 s |

三段视频均为 512×256 MPEG-4 Part 2。逐帧解码校验显示时间戳等于步号除以 20，共验证 667 帧。左、右半幅分别与工作区和腕部原始快照比对。对应快照最大 RGB MAE 为 3.0699。元数据记录每段源 MP4 的 SHA-256、大小和帧数。 [视频审计](../results/task019/metrics/video_metadata.json)

## 审查整改

- 当前本体表从同一步事件读取末端 XYZ、xyzw 四元数和双指 qpos。姿态以旋转向量弧度显示，缺失数据为 N/A。五张回放截图逐一核对了表中 XYZ 与双指值和原始事件，回放时用当前 Episode 代替离线样本选择器。
- 双视角帧与反馈由同一步索引。无可信视频时采用步号不晚于当前位置的历史快照，缺失视角显示占位。当前步官方谓词和整回合统计在不同卡片显示。
- 夹爪动作与实际开度分开。种子 142 的白杯在第 97 步收到张开命令，此时开度约 0.0089 m，第 106 步达到约 0.0717 m。第 223 步记录官方成功，黄白杯的张开仍为仅规划。
- 当前抬升定义为 `100 × (object_z[step] − object_z[reset])` 厘米。种子 142 第 49 步白杯为 +0.08 cm，第 176 步黄白杯为 +0.03 cm。Task 018 的约 9.47 cm / 9.67 cm 是抓持期间的峰值。逐步 ΔZ 仍使用复位位置作为测量基准。
- Windows 主机的 WSLg 在真实 Tk 窗口中截图。界面优先选择系统已安装的中文字体，物体位姿与目标状态分别布局，长反馈支持换行。播放、暂停、五个关键步的双视角与当前表格均已复核。播放器用单个后台线程解码，切换时撤销旧回调，关闭时释放资源。锁步同步指同一步号的帧与反馈，证据范围为对应正确性。
- 报告、验收 JSON 和视频 JSON 均以 UTF-8 发布。归档清单重新记录文件大小和哈希。工作源码目录没有 Git 元数据，源码文件与 SHA-256 另列供复审。

## 复核结果

`VIDEO_SOURCE_AVAILABLE`、`VIDEO_FRAME_ALIGNMENT_VERIFIED` 和 `GUI_PLAYBACK_PASS` 已在本地验证。7 项 Tk 测试与窗口复核命令均正常退出。系统外部 MP4 播放器在该 WSL 环境无默认应用，实际启动仍待验证。模型端到端前向沿用 Task 017 的运行证据。

- [结构化验收](../results/task019/acceptance.json)
- [桌面操作证据](../results/task019/metrics/gui_review.json)
- [本地源码文件清单](../results/task019/metrics/source_files.json)

在 Workbench 的 Robot Monitor & Replay 标签选择 Historical Sim Replay，选定种子后使用播放、暂停、拖动或关键事件跳转。示例截图位于归档 `evidence/task019/`。

```bash
.venv_xvla/bin/python scripts/audit_videos_task019.py
DISPLAY=:0 .venv_xvla/bin/python -m unittest workbench.tests.test_ui_headless -v
DISPLAY=:0 .venv_xvla/bin/python workbench/tests/capture_task019_review.py
```
