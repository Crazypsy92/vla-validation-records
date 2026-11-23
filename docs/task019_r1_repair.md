# Task 019-R1 · 回放数据可信度与桌面显示修复

Issue #3 的本轮返修材料已就绪，正式验收待用户审核。Task 020 尚处于准备阶段。

## 问题与整改

- 旧证据由 `generate_task019_artifacts.py` 的静态示意渲染器生成。其左侧状态表与右侧遥测使用不同字段，且第 49 和 176 步的 `18.7 cm`、`16.2 cm` 直接写在脚本里，**原始日志无法验证这两项数字**。现有生成入口改为捕获实际运行的 Workbench 窗口。
- 回放索引从选中的 Episode 读取 `events.jsonl`。第 0 步使用 reset，后续使用对应的 step。左侧状态表和 Tier 3 读取该事件的同一份 `robot_state`。XYZ 是 MuJoCo 世界坐标系下的夹爪控制点位置，单位米。末端姿态由 MuJoCo 世界参考系下的 xyzw 四元数转为旋转向量，单位弧度。双指各自的滑动关节 qpos 以米记录。顶部回放标识与 Episode 来源同时更新，回到离线模式恢复原样本。
- 物体当前抬升按 `100 × (z[step] − z[reset])` 计算，Z 取同一杯体在 MuJoCo 世界坐标系的高度，结果单位厘米。Seed 142 白杯第 49 步约 +0.08 cm，黄白杯第 176 步约 +0.03 cm。Task 018 的约 9.47 cm / 9.67 cm 是抓持期间的峰值，原指标和记录照原保留。
- 回放依次解码三段真实录像的 667 帧，并核对 20 FPS 时间戳、双视角和控制步号。归档包括每个被回放的 MP4 的相对路径、文件大小和 SHA-256。
- 图像和遥测使用同一控制步。报告保留这个功能结论。现有证据未测量端到端显示延迟。

## R1 验收矩阵

| 编号 | 结果 | 证据 |
| --- | --- | --- |
| R1-01 | PASS | 在真实 Tk 窗口核对 Seed 142 的 49、97、106、176、223 步全部 8 个字段。再切换到 Seed 143，核对复位和第 49 步，以及返回离线样本。见 GUI 记录。 |
| R1-02 | PASS | 三个指定 JSON 可标准解析，发布清单 Markdown 为 UTF-8 且无 NUL。 |
| R1-03 | PASS | 发布清单的大小与 SHA-256 以提交文件逐项复核。 |
| R1-04 | PASS（WSLg） | Windows 主机上实际启动 Workbench。六张窗口截图覆盖离线及五个关键步。使用系统中文字体，状态行和八列均可见。 |
| R1-05 | PASS | 当前步 ΔZ 公式、坐标、单位和两个采样点已记录。旧示意值标记为不可验证。 |
| R1-06 | PASS | 三段实际 MP4 的文件大小、SHA-256、帧率、时长与步号映射见元数据。 |
| R1-07 | PASS | 删除缺乏测量依据的定量延迟结论，保留同一步更新。 |
| R1-08 | PASS（源码快照） | 报告链接已校正。源码快照及相对基线的 Git 差异见下。 |
| R1-09 | PARTIAL | 界面回归 7 项通过，桌面播放与跨回合核验通过。新一轮模型前向和系统外部播放器启动未执行。 |

## 源码追溯

Workbench 工作目录没有原始 Git 历史。在独立的本地源码快照仓库，以与归档提交 `897e9a1` 的已记录哈希一致的七个文件建立基线 `4fdd77db0014aab16ce2ee770e8fb9d2fc055ed8`，本轮源码提交为 `9e1a036d8ec26c989d95ee40cb9cbbaff898c4c5`。这是源码实施快照，历史归档提交 `1b87845` 及本次证据归档各有其独立 Git 历史。证据归档仅包含报告、验证结果与选定截图。

```text
workbench/tests/capture_task019_review.py     |  48 ++-
 workbench/tests/generate_task019_artifacts.py | 497 +-------------------------
 2 files changed, 42 insertions(+), 503 deletions(-)
```

- [Task 019 技术报告](task019_replay_video.md)
- [本体与跨回合桌面复核](../results/task019/metrics/gui_review.json)
- [界面回归日志](../results/task019/metrics/gui_tests.log)
- [原始视频元数据](../results/task019/metrics/video_metadata.json)
- [源码文件及校验和](../results/task019/metrics/source_files.json)
- [六张复审截图](../evidence/task019/)
