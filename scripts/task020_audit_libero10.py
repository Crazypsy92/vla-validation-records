"""Audit Task 020 eligibility using the installed LIBERO registry and BDDL parser."""
import hashlib
import json
from importlib.metadata import version
from pathlib import Path

from libero.libero import benchmark, get_libero_path
from libero.libero.envs.bddl_utils import robosuite_parse_problem


ROOT = Path(__file__).resolve().parents[1]
SUITE = "libero_10"


def main():
    suite = benchmark.get_benchmark_dict()[SUITE]()
    bddl_root = Path(get_libero_path("bddl_files"))
    tasks = []
    for task_id, task in enumerate(suite.tasks):
        relative_bddl = Path(task.problem_folder) / task.bddl_file
        path = bddl_root / relative_bddl
        definition = robosuite_parse_problem(str(path))
        goals = definition["goal_state"]
        categories = {name: category for category, names in definition["objects"].items()
                      for name in names}
        placements = [{"predicate": goal[0], "object": goal[1], "category": categories.get(goal[1]),
                       "target": goal[2]} for goal in goals if goal[0] in {"on", "in"} and len(goal) == 3]
        extra_goals = [goal for goal in goals if goal[0] not in {"on", "in"}]
        reasons = []
        if len(placements) != 1:
            reasons.append("not_a_single_placement")
        if len({placement["object"] for placement in placements}) > 1:
            reasons.append("multiple_manipulated_objects")
        if any("mug" in placement["object"] for placement in placements):
            reasons.append("mug_is_a_task_target")
        if extra_goals:
            reasons.append("extra_non_placement_operation")
        tasks.append({"task_id": task_id, "instruction": task.language, "bddl": relative_bddl.as_posix(),
                      "bddl_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                      "goal_predicates": goals, "placements": placements,
                      "mugs_in_scene": [name for name in categories if "mug" in name],
                      "eligible_by_goal": not reasons, "exclusion_reasons": reasons})
    candidates = [task["task_id"] for task in tasks if task["eligible_by_goal"]]
    result = {"suite": SUITE, "libero_package": "hf-libero", "libero_package_version": version("hf-libero"),
              "selection_rule": "Exactly one On/In goal for a non-mug object and no additional goal predicate",
              "required_candidates": 2, "candidate_task_ids": candidates,
              "candidate_ids_if_mug_props_also_excluded": [
                  task["task_id"] for task in tasks if task["eligible_by_goal"] and not task["mugs_in_scene"]
              ],
              "status": "BLOCKED" if len(candidates) < 2 else "READY_FOR_COMPATIBILITY_CHECK",
              "tasks": tasks}
    output = ROOT / "results/task020/metrics/official_task_inventory.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{SUITE}: {len(tasks)} tasks, eligible IDs {candidates}, status {result['status']}")


if __name__ == "__main__":
    main()
