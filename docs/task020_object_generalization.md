# Task 020 · 跨物体抓放验证的选题审计

**STATUS: BLOCKED。** 官方 libero_10 只有 Task 5 符合非杯类单物体纯抓放目标，低于两个任务的启动门槛。 已完成任务定义审计。本轮正式测试为 0/6 回合，模型前向 0 次，仿真 0 步。

以本机 `hf-libero 0.1.5` 的官方 `libero_10` 注册表和 BDDL 解析器为准。合格任务需要一条 `On` 或 `In` 放置谓词，目标物体为非杯类，且没有附加操作谓词。 [Issue #4](https://github.com/Crazypsy92/vla-validation-records/issues/4)

| 官方 ID | 官方指令 | 被操作物体与目标 | 审计结论 |
| --- | --- | --- | --- |
| 0 | put both the alphabet soup and the tomato sauce in the basket | `alphabet_soup_1 → basket_1_contain_region`；`tomato_sauce_1 → basket_1_contain_region` | 需搬运两件物体 |
| 1 | put both the cream cheese box and the butter in the basket | `cream_cheese_1 → basket_1_contain_region`；`butter_1 → basket_1_contain_region` | 需搬运两件物体 |
| 2 | turn on the stove and put the moka pot on it | `moka_pot_1 → flat_stove_1_cook_region` | 还要求打开炉灶 |
| 3 | put the black bowl in the bottom drawer of the cabinet and close it | `akita_black_bowl_1 → white_cabinet_1_bottom_region` | 还要求关闭抽屉 |
| 4 | put the white mug on the left plate and put the yellow and white mug on the right plate | `porcelain_mug_1 → plate_1`；`white_yellow_mug_1 → plate_2` | 需搬运两只杯子，且为 Task017 基线 |
| 5 | pick up the book and place it in the back compartment of the caddy | `black_book_1 → desk_caddy_1_back_contain_region` | 唯一候选，书本放入收纳盒后格 |
| 6 | put the white mug on the plate and put the chocolate pudding to the right of the plate | `porcelain_mug_1 → plate_1`；`chocolate_pudding_1 → living_room_table_plate_right_region` | 需搬运两件物体，含白杯 |
| 7 | put both the alphabet soup and the cream cheese box in the basket | `alphabet_soup_1 → basket_1_contain_region`；`cream_cheese_1 → basket_1_contain_region` | 需搬运两件物体 |
| 8 | put both moka pots on the stove | `moka_pot_1 → flat_stove_1_cook_region`；`moka_pot_2 → flat_stove_1_cook_region` | 需搬运两个摩卡壶并打开炉灶 |
| 9 | put the yellow and white mug in the microwave and close it | `white_yellow_mug_1 → microwave_1_heating_region` | 操作目标是杯子，还要求关闭微波炉 |

Task 5 的目标物体为 `black_book_1`，类别为 `black_book`。官方 BDDL 文件为 `libero_10/STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy.bddl`，目标谓词为 `In(black_book_1, desk_caddy_1_back_contain_region)`。场景还有一只黄白杯作为道具，目标谓词只涉及书本。若选题还要求整个场景没有杯子，则合格任务数为 0。清单包含所有 BDDL 相对路径、文件哈希、目标谓词与排除原因。 [官方任务清单](../results/task020/metrics/official_task_inventory.json)

酒瓶放架和麦片盒放盘均未列入当前 `libero_10` 的官方指令。按 Issue 的阻塞处理规则，实验在选题门槛停止。模型与控制器兼容性、正式回合、视频和 Workbench 接入均待选题范围确定后执行。Task 017 的双杯结果仍可作后续对照。

复现命令与退出码

```bash
.venv_xvla/bin/python scripts/task020_audit_libero10.py
# 进程退出码 0，选题结果 BLOCKED
```

- [验收矩阵](../results/task020/acceptance.json)
- [任务统计](../results/task020/metrics/summary.json)
- [注册表审计日志](../results/task020/logs/registry_audit.log)
