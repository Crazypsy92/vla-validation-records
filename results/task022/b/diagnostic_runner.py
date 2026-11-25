"""Task022-B read-only instrumentation of the unchanged Task021 B2b worker."""
import hashlib
import json
import os
from pathlib import Path
import random
import sys

os.environ.setdefault("MUJOCO_GL", "egl")

import mujoco
import numpy as np
import torch
from scipy.spatial.transform import Rotation

ROOT = Path(__file__).resolve().parents[1]
WORKER = ROOT / "workbench/workers/book_pilot.py"
BASE = ROOT / "results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532"
STAGE_A = ROOT / "results/task022/a/metrics/summary.json"
SITE = "desk_caddy_1_back_contain_region"
BOOK = "black_book_1"


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def pose(position, matrix):
    return {"position_m": np.asarray(position).copy(),
            "rotation_matrix": np.asarray(matrix).reshape(3, 3).copy()}


def relative(parent, child):
    rot = parent["rotation_matrix"].T
    return pose(rot @ (child["position_m"] - parent["position_m"]), rot @ child["rotation_matrix"])


def errors(first, second):
    delta = relative(first, second)
    return [float(np.linalg.norm(delta["position_m"])),
            float(np.degrees(Rotation.from_matrix(delta["rotation_matrix"]).magnitude()))]


def observations(row):
    eef = row["robot_state"]["eef"]
    return (pose(row["book_position"], Rotation.from_quat(np.asarray(row["book_quaternion_wxyz"])[[1, 2, 3, 0]]).as_matrix()),
            pose(eef["pos"], Rotation.from_quat(eef["quat"]).as_matrix()))


def emit(stream, row):
    print(json.dumps(row, default=lambda obj: obj.tolist(), allow_nan=False), file=stream, flush=True)


class Diagnostic:
    def __init__(self, directory, cfg):
        self.historical = {}
        for line in (BASE / "events.jsonl").read_text().splitlines():
            row = json.loads(line)
            if row["type"] in ("reset", "step"):
                self.historical[row["step"]] = row
        self.directory = directory
        self.log = (directory / "diagnostic.jsonl").open("x", encoding="utf-8")
        self.comparison = (directory / "reproduction.jsonl").open("x", encoding="utf-8")
        self.last_contacts = {}
        self.last_profiles = []
        self.current_prediction = None

    def compare(self, step, feedback):
        if step >= 160:
            return False
        book, eef = map(list, (errors(*pair) for pair in zip(
            observations(self.historical[step]), observations(feedback))))
        diverged = any(distance > .002 or angle > 1 for distance, angle in (book, eef))
        emit(self.comparison, dict(step=step, book_error_m_deg=book, eef_error_m_deg=eef,
                                   exceeds_threshold=diverged, checkpoint=step % 30 == 0))
        return diverged

    def attach(self, env):
        physics = env._env.env
        self.robot = physics.robots[0]
        self.sim = physics.sim
        self.site = self.sim.model.site_name2id(SITE)
        self.book = physics.obj_body_id[BOOK]
        self.book_geoms = {self.sim.model.geom_name2id(n) for n in physics.get_object(BOOK).contact_geoms}
        self.gripper_geoms = {self.sim.model.geom_name2id(n) for n in self.robot.gripper.contact_geoms}
        self.caddy_geoms = {self.sim.model.geom_name2id(n) for n in physics.get_object("desk_caddy_1").contact_geoms}
        self.indices = self.robot._ref_joint_actuator_indexes
        self.controller_code = self.robot.controller.run_controller.__func__.__code__
        self.robot_code = self.robot.control.__func__.__code__
        self.pending = None
        self.previous_time = float(self.sim.data.time)
        emit(self.log, {"type": "metadata", "control_hz": 20, "physics_timestep_s": self.sim.model.opt.timestep,
                        "contact_rate": "control-step boundary only",
                        "torque_rate": "every invocation in each control step",
                        "book_geoms": sorted(self.book_geoms), "gripper_geoms": sorted(self.gripper_geoms),
                        "caddy_geoms": sorted(self.caddy_geoms),
                        "controller_source_sha256": sha(Path(self.controller_code.co_filename)),
                        "robot_source_sha256": sha(Path(self.robot_code.co_filename))})

    def profile(self, frame, event, return_value):
        if event != "return":
            return
        if frame.f_code is self.controller_code and frame.f_locals["self"] is self.robot.controller:
            self.pending = (float(self.sim.data.time), np.asarray(return_value).copy())
        elif frame.f_code is self.robot_code and frame.f_locals["self"] is self.robot and self.pending is not None:
            timestamp, raw = self.pending
            self.pending = None
            applied = self.robot.torques.copy()
            low, high = self.robot.torque_limits
            self.last_profiles.append(dict(sim_time_s=timestamp, before_limit=raw, after_limit=applied,
                                           lower=low, upper=high, clipped=np.not_equal(applied, raw),
                                           actuator_ctrl=self.sim.data.ctrl[self.indices].copy()))

    def execute(self, env, action, capture):
        if not capture:
            return env.step(action)
        self.last_profiles = []
        self.previous_time = float(self.sim.data.time)
        previous = sys.getprofile()
        sys.setprofile(self.profile)
        try:
            return env.step(action)
        finally:
            sys.setprofile(previous)

    def collect(self, step, offset, action, feedback, success):
        sim = self.sim
        model, data = sim.model, sim.data
        native_data = data._data
        site = pose(data.site_xpos[self.site], data.site_xmat[self.site])
        site["half_size_m"] = model.site_size[self.site].copy()
        book, eef = observations(feedback)
        ctl = self.robot.controller
        goal = pose(ctl.goal_pos, ctl.goal_ori)
        boxes = [dict(geom_id=id_, geom_name=model.geom_id2name(id_), geom_type=int(model.geom_type[id_]),
                      geom_size_m=model.geom_size[id_].copy(), **pose(data.geom_xpos[id_], data.geom_xmat[id_]))
                 for id_ in sorted(self.book_geoms)]
        watched = self.book_geoms | self.gripper_geoms | self.caddy_geoms
        contacts = []
        current = {}
        for idx, contact in enumerate(native_data.contact):
            a, b = int(contact.geom1), int(contact.geom2)
            if not ({a, b} & watched):
                continue
            key = tuple(sorted((a, b)))
            current[key] = self.last_contacts.get(key, 0) + 1
            force = np.zeros(6)
            if contact.efc_address >= 0:
                mujoco.mj_contactForce(model._model, native_data, idx, force)
                force_value = float(force[0])
            else:
                force_value = {"status": "UNAVAILABLE", "reason": "inactive contact constraint"}
            contacts.append(dict(geom_ids=(a, b), geom_names=(model.geom_id2name(a), model.geom_id2name(b)),
                                 point_m=contact.pos.copy(), normal_world=contact.frame[:3].copy(),
                                 signed_distance_m=float(contact.dist), normal_force_N=force_value,
                                 consecutive_control_samples=current[key]))
        self.last_contacts = current
        joints = self.robot._ref_joint_pos_indexes
        site_local = relative(site, book)
        emit(self.log, dict(type="step", step=step, site=site, book=book, collision_geoms=boxes,
                            book_in_site=site_local, eef=eef, osc_goal=goal, book_in_eef=relative(eef, book),
                            goal_minus_feedback_world_m=goal["position_m"] - eef["position_m"],
                            goal_feedback_error_m_deg=errors(eef, goal),
                            predicted_action_7d=self.current_prediction[offset], executed_action_7d=action,
                            gripper=dict(command=float(action[-1]), qpos=feedback["robot_state"]["gripper"]["qpos"],
                                         opening_m=feedback["gripper_opening_m"], left_contact=feedback["left_contact"],
                                         right_contact=feedback["right_contact"]),
                            is_success=success, contacts=contacts, contact_count=len(contacts),
                            contact_pair_count=len(current),
                            contact_impulse={"status": "UNAVAILABLE", "reason": "boundary samples do not integrate impulse"},
                            qpos=data.qpos[joints].copy(), qvel=data.qvel[self.robot._ref_joint_vel_indexes].copy(),
                            actuator_ctrl=data.ctrl[self.indices].copy(), actuator_force=data.actuator_force[self.indices].copy(),
                            joint_constraint_force=data.qfrc_constraint[self.robot._ref_joint_vel_indexes].copy(),
                            solver_niter=native_data.solver_niter.copy(), solver_constraint_count=int(native_data.nefc),
                            solver_residual={"status": "UNAVAILABLE", "reason": "no validated scalar residual in wrapper"},
                            torques=self.last_profiles, torque_sample_count=len(self.last_profiles),
                            sim_time_s=float(data.time), sim_dt_s=float(data.time) - self.previous_time))


def checked_preflight(directory, cfg, env, fields):
    stage_a = json.loads(STAGE_A.read_text())
    for name, expected in stage_a["installed_sources_sha256"].items():
        if sha(ROOT / name) != expected:
            raise ValueError("Stage A installed source hash differs: " + name)
    source = json.loads((ROOT / "results/task021/metrics/inventory_source.json").read_text())
    if sha(ROOT / "workbench/workers/book_resources.py") != source["source_hashes"]["resource_guard"]:
        raise ValueError("Task021 resource gate differs")
    for name, expected in stage_a["runs"]["34"]["source_files_sha256"].items():
        if sha(BASE / name) != expected:
            raise ValueError("Task021 historical file differs: " + name)
    if cfg != json.loads((BASE / "configuration.json").read_text()):
        raise ValueError("Historical config differs")
    if cfg["checkpoint_revision"] != "8e6aeef01f634f5d3b5be4340328f19cc2c25a65":
        raise ValueError("Requested revision differs")
    historical_reset = next(json.loads(line) for line in (BASE / "events.jsonl").open()
                            if json.loads(line)["type"] == "reset")
    for key in ("instruction", "bddl", "official_state_sha256", "initial_state_asset_sha256", "rgb_array_sha256"):
        if fields[key] != historical_reset[key]:
            raise ValueError("Historical reset fingerprint differs: " + key)
    checks = dict(historical_config_sha256=sha(BASE / "configuration.json"), history_files_verified=len(
        stage_a["runs"]["34"]["source_files_sha256"]), installed_sources_verified=stage_a["installed_sources_sha256"],
        original_guard_sha256=source["source_hashes"]["resource_guard"],
        initial_sha256=fields["official_state_sha256"], asset_sha256=fields["initial_state_asset_sha256"],
        bddl_sha256=source["bddl"]["sha256"], prompt=fields["instruction"], rgb_array_sha256=fields["rgb_array_sha256"],
        stage_a_summary_sha256=sha(STAGE_A), instrument_sha256=sha(Path(__file__)))
    (directory / "preflight.json").write_text(json.dumps(checks, indent=2) + "\n")


def instrumented_worker():
    source = WORKER.read_text()
    def replace(old, new):
        nonlocal source
        if source.count(old) != 1:
            raise ValueError("Worker hook no longer unique: " + old[:60])
        source = source.replace(old, new)

    reset_start = source.index('            record(log, type="status", phase="environment_reset", model=model)')
    reset_end = source.index('            summary.update(instruction=', reset_start)
    reset = source[reset_start:reset_end]
    replace(reset, '            random.setstate(rng_after_reset[0])\n            np.random.set_state(rng_after_reset[1])\n            torch.set_rng_state(rng_after_reset[2])\n')
    pre_reset = reset.replace(', model=model)', ')')
    after_reset = """            checked_preflight(directory, cfg, env, fields)
            diagnostic = Diagnostic(directory, cfg)
            diagnostic.attach(env)
            if diagnostic.compare(0, reset_row):
                raise ValueError("Historical Step 0 pose differs")
            rng_after_reset = (random.getstate(), np.random.get_state(), torch.get_rng_state())
            summary.update(mode="task022_b", preflight="PASS", source="Workbench Worker CLI")
"""
    needle = '            requested = (formal_gate(directory, "before_model_load")'
    replace(needle, pre_reset + after_reset + needle)
    replace('bddl=Path(env._task_bddl_file).name, source="Workbench GUI"', 'bddl=Path(env._task_bddl_file).name, source="Workbench Worker CLI"')
    replace('            limit = min(env._max_episode_steps, 90) if resource_check else env._max_episode_steps',
            '            limit = min(env._max_episode_steps, 300)\n            diverged = False')
    replace('                actions = validate_chunk(backend, env_post, prediction, 30)',
            '                actions = validate_chunk(backend, env_post, prediction, 30)\n                diagnostic.current_prediction = prediction["actions_7d"]')
    replace('                    obs, reward, terminated, truncated, info = env.step(action)',
            '                    obs, reward, terminated, truncated, info = diagnostic.execute(env, action, summary["steps"] >= 148)')
    replace('                    feedback = observation_row(obs, env)',
            """                    feedback = observation_row(obs, env)
                    diverged = diagnostic.compare(step, feedback)
                    if step >= 149 or diverged:
                        diagnostic.collect(step, offset, action, feedback, success)""")
    replace('                    if release_transition or success or summary["steps"] == limit:',
            """                    if diverged:
                        break
                    if release_transition or success or summary["steps"] == limit:""")
    replace('                checkpoint(directory, "after_chunk_and_video_write")',
            '                checkpoint(directory, "after_chunk_and_video_write")\n                if diverged:\n                    break')
    replace('            if resource_check and not (requested or terminated or truncated):',
            """            if diverged:
                requested = "REPLAY_DIVERGED"
            elif summary["steps"] == limit and not (requested or terminated or truncated):
                requested = "DIAGNOSTIC_LIMIT"
            if resource_check and not (requested or terminated or truncated):""")
    replace('summary.update(status="ERROR", error=', 'summary.update(status="ERROR" if summary.get("preflight") else "BLOCKED", error=')
    scope = dict(globals(), __file__=str(WORKER), __name__="__main__")
    exec(compile(source, str(WORKER), "exec"), scope)


if __name__ == "__main__":
    instrumented_worker()
