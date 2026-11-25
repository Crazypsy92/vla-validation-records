"""Read-only MuJoCo and OSC instrumentation sampled at control boundaries."""
import hashlib
import json
from pathlib import Path
import sys

import mujoco
import numpy as np
from scipy.spatial.transform import Rotation

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
    def __init__(self, directory, historical_events):
        self.historical = {}
        for line in historical_events.read_text().splitlines():
            row = json.loads(line)
            if row["type"] in ("reset", "step"):
                self.historical[row["step"]] = row
        self.log = (directory / "diagnostic.jsonl").open("x", encoding="utf-8")
        self.comparison = (directory / "reproduction.jsonl").open("x", encoding="utf-8")
        self.last_contacts = {}
        self.last_profiles = []
        self.input_meta = None
        self.current_prediction = None

    def compare(self, step, feedback):
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
        self.arm_joint_ids = [self.sim.model.joint_name2id(name) for name in self.robot.robot_model.joints]
        self.joint_position_limits = self.sim.model.jnt_range[self.arm_joint_ids].copy()
        self.joint_position_limited = self.sim.model.jnt_limited[self.arm_joint_ids].copy()
        self.controller_code = self.robot.controller.run_controller.__func__.__code__
        self.robot_code = self.robot.control.__func__.__code__
        self.pending = None
        self.previous_time = float(self.sim.data.time)
        emit(self.log, {"type": "metadata", "control_hz": 20, "physics_timestep_s": self.sim.model.opt.timestep,
                        "contact_rate": "control-step boundary only",
                        "torque_rate": "every invocation in each control step",
                        "book_geoms": sorted(self.book_geoms), "gripper_geoms": sorted(self.gripper_geoms),
                        "caddy_geoms": sorted(self.caddy_geoms),
                        "geom_names": {i: self.sim.model.geom_id2name(i)
                                       for i in sorted(self.book_geoms | self.gripper_geoms | self.caddy_geoms)},
                        "joint_position_limits_rad": self.joint_position_limits,
                        "joint_position_limited": self.joint_position_limited,
                        "controller_source_sha256": sha(Path(self.controller_code.co_filename)),
                        "robot_source_sha256": sha(Path(self.robot_code.co_filename))})

    def profile(self, frame, event, return_value):
        if event != "return":
            return
        if frame.f_code is self.controller_code and frame.f_locals["self"] is self.robot.controller:
            if return_value is not None:
                self.pending = (float(self.sim.data.time), np.asarray(return_value).copy())
        elif frame.f_code is self.robot_code and frame.f_locals["self"] is self.robot and self.pending is not None:
            timestamp, raw = self.pending
            self.pending = None
            applied = self.robot.torques.copy()
            low, high = self.robot.torque_limits
            self.last_profiles.append(dict(sim_time_s=timestamp, before_limit=raw, after_limit=applied,
                                           lower=low, upper=high, clipped=np.not_equal(applied, raw),
                                           actuator_ctrl=self.sim.data.ctrl[self.indices].copy()))

    def execute(self, env, action):
        self.last_profiles = []
        self.pending = None
        self.previous_time = float(self.sim.data.time)
        previous = sys.getprofile()
        sys.setprofile(self.profile)
        try:
            return env.step(action)
        finally:
            sys.setprofile(previous)

    def close(self):
        self.log.close()
        self.comparison.close()

    def collect(self, step, offset, action, feedback, success, terminated, truncated):
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
        for idx in range(native_data.ncon):
            contact = native_data.contact[idx]
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
                            input_observation=self.input_meta, chunk_offset=offset,
                            predicted_action_7d=self.current_prediction[offset], executed_action_7d=action,
                            gripper=dict(command=float(action[-1]), qpos=feedback["robot_state"]["gripper"]["qpos"],
                                         opening_m=feedback["gripper_opening_m"], left_contact=feedback["left_contact"],
                                         right_contact=feedback["right_contact"]),
                            is_success=success, terminated=terminated, truncated=truncated,
                            contacts=contacts, contact_count=len(contacts),
                            contact_pair_count=len(current),
                            contact_impulse={"status": "UNAVAILABLE", "reason": "boundary samples do not integrate impulse"},
                            qpos=data.qpos[joints].copy(), qvel=data.qvel[self.robot._ref_joint_vel_indexes].copy(),
                            actuator_ctrl=data.ctrl[self.indices].copy(), actuator_force=data.actuator_force[self.indices].copy(),
                            joint_constraint_force=data.qfrc_constraint[self.robot._ref_joint_vel_indexes].copy(),
                            solver_niter=native_data.solver_niter.copy(), solver_constraint_count=int(native_data.nefc),
                            solver_residual={"status": "UNAVAILABLE", "reason": "no validated scalar residual in wrapper"},
                            torques=self.last_profiles, torque_sample_count=len(self.last_profiles),
                            torque_capture_status="AVAILABLE" if self.last_profiles else "UNAVAILABLE",
                            nearest_joint_limit_rad=np.minimum(data.qpos[joints] - self.joint_position_limits[:, 0],
                                self.joint_position_limits[:, 1] - data.qpos[joints]),
                            sim_time_s=float(data.time), sim_dt_s=float(data.time) - self.previous_time))
