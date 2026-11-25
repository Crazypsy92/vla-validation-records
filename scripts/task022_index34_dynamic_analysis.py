"""Summarize an authorized Task022-D run without running the model or simulator."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import numpy as np
from scipy.spatial.transform import Rotation

WINDOW_START, WINDOW_END = 150, 300
CHECKPOINTS = (0,30,60,90,120,150,159,180,201,210,240,270,300)


def read(path):
    return json.loads(path.read_text()) if path.exists() else {}


def rows(path):
    if path.exists():
        with path.open() as stream:
            return [json.loads(line) for line in stream if line.strip()]
    zipped = path.with_suffix(path.suffix+".gz")
    if zipped.exists():
        with gzip.open(zipped,"rt",encoding="utf-8") as stream:
            return [json.loads(line) for line in stream if line.strip()]
    return []


def distribution(values):
    if not len(values):
        return None
    v=np.asarray(values,dtype=float)
    return dict(min=float(v.min()),median=float(np.median(v)),p95=float(np.percentile(v,95)),
                max=float(v.max()),mean=float(v.mean()))


def degrees(a,b):
    return float(np.degrees(Rotation.from_matrix(a.T@b).magnitude()))


def hand_body_to_grip_site(gripper_xml):
    root = ET.parse(gripper_xml).getroot()
    mount = root.find("./worldbody/body[@name='right_gripper']")
    grip = mount.find("./body[@name='eef']")
    site = grip.find("./site[@name='grip_site']")
    orientation = np.eye(3)
    for element in (mount, grip, site):
        if {"axisangle","xyzaxes","zaxis","euler"} & element.attrib.keys():
            raise ValueError("Unexpected gripper orientation encoding")
        q = np.fromstring(element.get("quat","1 0 0 0"),sep=" ")
        orientation = orientation @ Rotation.from_quat(q,scalar_first=True).as_matrix()
    return orientation


def summarize(execution, gripper_xml):
    hand_to_site = hand_body_to_grip_site(gripper_xml)
    w=execution/"worker"
    telemetry=rows(w/"diagnostic.jsonl")
    meta=next((r for r in telemetry if r["type"]=="metadata"),{})
    trace=[r for r in telemetry if r["type"]=="step"]
    compare=rows(w/"reproduction.jsonl")
    resource=rows(w/"resources_supervisor.jsonl")
    phases=rows(w/"resources_child.jsonl")
    gates=rows(w/"gates.jsonl")
    chunks=rows(w/"chunks.jsonl")
    result=read(w/"result.json") or read(w/"progress.json")
    terminal=read(execution/"exit.json")
    if trace:
        assert [r["step"] for r in trace]==list(range(1,len(trace)+1))
        assert len(trace)<=WINDOW_END
    sample=[r for r in trace if WINDOW_START<=r["step"]<=WINDOW_END]
    clip_by_joint=Counter()
    pair_info={}
    book_ids=set(meta.get("book_geoms",[]))
    grip_ids=set(meta.get("gripper_geoms",[]))
    caddy_ids=set(meta.get("caddy_geoms",[]))
    stage_time = {r["phase"]:r["time"] for r in phases}
    active=[r for r in resource if r["phase"]=="child_active"]
    load_time_start=stage_time.get("model_load_start_no_environment")
    load_time_end=stage_time.get("model_load_end_no_environment",float("inf"))
    resource_fields=("rss_mib","pss_mib","available_mib","swap_free_mib","cpu_percent_process","cpu_percent_system")
    def resource_stats(rs):
        return {k:distribution([r[k] for r in rs if r.get(k) is not None]) for k in resource_fields}
    active_load=[r for r in active+phases if load_time_start is not None and load_time_start<=r["time"]<=load_time_end]
    points=[]
    reference_rot=reference_translation=None
    previous_rot=previous_translation=None
    first_site_position=first_site_rotation=None
    late_rot=late_translation=None
    for r in sample:
        step = r["step"]
        site = np.array(r["site"]["position_m"])
        axis = np.array(r["site"]["rotation_matrix"])
        size = np.array(r["site"]["half_size_m"])
        if first_site_position is None:
            first_site_position,first_site_rotation=site,axis
        pos = np.array(r["book"]["position_m"])
        goal = np.array(r["osc_goal"]["position_m"])
        goal_rot = np.array(r["osc_goal"]["rotation_matrix"])
        # robot0_eef_quat is the right_hand BODY orientation, whereas
        # OSC goal_ori is a grip_site orientation. The recorded position is
        # already the grip_site origin. Resolve the rigid mounting rotation.
        grip_rot = hand_to_site.T @ np.array(r["book_in_eef"]["rotation_matrix"])
        grip_trans = hand_to_site.T @ np.array(r["book_in_eef"]["position_m"])
        site_eef_rot = np.array(r["eef"]["rotation_matrix"]) @ hand_to_site
        implied = goal+goal_rot@grip_trans
        if reference_translation is None:
            reference_translation,reference_rot=grip_trans,grip_rot
        if previous_translation is None:
            previous_translation,previous_rot=grip_trans,grip_rot
        if late_translation is None and step>=210:
            late_translation,late_rot=grip_trans,grip_rot
        # Mirrors installed SiteObject.in_box for the book body origin.
        half_world=np.abs(axis@size)
        lo,hi=site-half_world,site+half_world
        lo[2] -= .01
        inside=bool(np.all(pos>lo)&np.all(pos<hi))
        implied_inside=bool(np.all(implied>lo)&np.all(implied<hi))
        goal_x_change=float(implied[0]-pos[0])
        translation_only=pos+goal-np.array(r["eef"]["position_m"])
        axis_failures=np.flatnonzero((implied<=lo)|(implied>=hi)).tolist()
        caddy_points=[c for c in r["contacts"] if set(c["geom_ids"])&caddy_ids and
                      set(c["geom_ids"])&(book_ids|grip_ids)]
        for c in caddy_points:
            key="/".join(str(g) for g in sorted(c["geom_ids"]))
            entry=pair_info.setdefault(key,dict(geom_names=c["geom_names"],geom_ids=c["geom_ids"],
                first_step=step,last_step=step,steps=set(),point_samples=0,longest_sample_streak=0,
                extreme_force=None,minimum_signed_distance=None,force_unavailable_count=0,
                involves_book=bool(set(c["geom_ids"])&book_ids)))
            entry["last_step"]=step
            entry["steps"].add(step)
            entry["point_samples"]+=1
            entry["longest_sample_streak"]=max(entry["longest_sample_streak"],c["consecutive_control_samples"])
            if entry["minimum_signed_distance"] is None or c["signed_distance_m"]<entry["minimum_signed_distance"]["signed_distance_m"]:
                entry["minimum_signed_distance"]=dict(step=step,**c)
            v=c["normal_force_N"]
            if isinstance(v,(int,float)):
                if entry["extreme_force"] is None or v>entry["extreme_force"]["normal_force_N"]:
                    entry["extreme_force"]=dict(step=step,**c)
            else:
                entry["force_unavailable_count"]+=1
        clipped=[i+1 for tor in r["torques"] for i,c in enumerate(tor["clipped"]) if c]
        clip_by_joint.update(clipped)
        current_error=r["goal_feedback_error_m_deg"]
        points.append(dict(step=step,chunk=r["input_observation"]["chunk"],book_world_x_m=float(pos[0]),
                target_world_x_upper_m=float(hi[0]),target_local_m=r["book_in_site"]["position_m"],
                dynamic_site_shift_m=float(np.linalg.norm(site-first_site_position)),
                dynamic_site_rotation_deg=degrees(first_site_rotation,axis),
                implied_book_at_goal_local_m=(axis.T@(implied-site)).tolist(),
                actual_book_x_over_upper_m=float(pos[0]-hi[0]),
                implied_book_x_over_upper_m=float(implied[0]-hi[0]),
                implied_book_x_over_lower_m=float(implied[0]-lo[0]),
                implied_outside_world_axes=axis_failures,
                implied_x_over_upper_translation_only_m=float(translation_only[0]-hi[0]),goal_eef_world_x_m=float(goal[0]),
                actual_eef_world_x_m=r["eef"]["position_m"][0],book_world_x_if_goal_and_current_grasp_m=float(implied[0]),
                x_correction_at_goal_m=goal_x_change, inside_from_dynamic_site=inside,
                official_predicate=bool(r["is_success"]),implied_inside_at_goal=implied_inside,
                x_upper_only_violation=bool(pos[0]>=hi[0] and np.all(pos[1:]>lo[1:]) and np.all(pos[1:]<hi[1:])),
                goal_feedback_error_m=current_error[0],goal_feedback_error_deg=degrees(site_eef_rot,goal_rot),
                raw_hand_body_to_goal_site_angle_deg=current_error[1],
                nearest_joint_limit_rad=min(r["nearest_joint_limit_rad"]),torque_samples=r["torque_sample_count"],
                clipped_axis_samples=len(clipped), max_abs_constraint_Nm=float(np.max(np.abs(r["joint_constraint_force"]))),
                grip_translation_from_window_start_m=float(np.linalg.norm(grip_trans-reference_translation)),
                grip_rotation_from_window_start_deg=degrees(reference_rot,grip_rot),
                adjacent_grip_translation_m=float(np.linalg.norm(grip_trans-previous_translation)),
                adjacent_grip_rotation_deg=degrees(previous_rot,grip_rot),
                grip_translation_from_step_210_m=float(np.linalg.norm(grip_trans-late_translation)) if late_translation is not None else None,
                grip_rotation_from_step_210_deg=degrees(late_rot,grip_rot) if late_rot is not None else None,
                actuator_force_max_abs_Nm=float(np.max(np.abs(r["actuator_force"]))),
                final_actuator_ctrl_max_difference_Nm=float(np.max(np.abs(
                    np.array(r["actuator_ctrl"])-r["torques"][-1]["after_limit"]))) if r["torques"] else None,
                actuator_force_max_difference_from_ctrl_Nm=float(np.max(np.abs(
                    np.array(r["actuator_force"])-r["actuator_ctrl"]))),
                solver_niter_max=int(max(r["solver_niter"])),
                grip_position_in_eef_m=grip_trans.tolist(),bilateral=bool(r["gripper"]["left_contact"] and r["gripper"]["right_contact"]),
                opening_m=r["gripper"]["opening_m"],gripper_command=r["gripper"]["command"],
                caddy_moving_contact_count=len(caddy_points),
                caddy_book_contact_count=sum(bool(set(c["geom_ids"])&book_ids) for c in caddy_points),
                caddy_finger_contact_count=sum(bool(set(c["geom_ids"])&grip_ids) for c in caddy_points),
                sim_dt_s=r["sim_dt_s"]))
        previous_translation,previous_rot=grip_trans,grip_rot
    late=[r for r in points if r["step"]>=210]
    xonly=[r for r in late if r["x_upper_only_violation"]]
    for item in pair_info.values():
        item["steps"]=sorted(item["steps"])
    checkpoint_metrics=[r for r in compare if r["step"] in CHECKPOINTS]
    pre_drift=[r["step"] for r in compare if r["step"]<160 and r["exceeds_threshold"]]
    drift=[r["step"] for r in compare if r["exceeds_threshold"]]
    torque_tot=sum(r["torque_samples"] for r in points)
    window=dict(expected=151,observed=len(points),percent=100*len(points)/151,
        state_predicate_disagreement=[r["step"] for r in points if r["official_predicate"]!=r["inside_from_dynamic_site"]],
        torque_samples=torque_tot,clipped_axis_samples=sum(clip_by_joint.values()),clipped_by_joint=dict(clip_by_joint),
        clip_steps=[r["step"] for r in points if r["clipped_axis_samples"]],
        torque_missing_steps=[r["step"] for r in points if not r["torque_samples"]],
        actuator_force_max_abs_Nm=distribution([r["actuator_force_max_abs_Nm"] for r in points]),
        final_actuator_ctrl_max_difference_Nm=distribution([r["final_actuator_ctrl_max_difference_Nm"] for r in points if r["final_actuator_ctrl_max_difference_Nm"] is not None]),
        actuator_force_max_difference_from_ctrl_Nm=distribution([r["actuator_force_max_difference_from_ctrl_Nm"] for r in points]),
        solver_iteration_max_by_step=distribution([r["solver_niter_max"] for r in points]),
        torque_samples_per_control_step=distribution([r["torque_samples"] for r in points]),
        control_step_seconds=distribution([r["sim_dt_s"] for r in points]),
        dynamic_site_shift_m=distribution([r["dynamic_site_shift_m"] for r in points]),
        dynamic_site_rotation_deg=distribution([r["dynamic_site_rotation_deg"] for r in points]),
        goal_error_m=distribution([r["goal_feedback_error_m"] for r in points]),
        goal_error_deg=distribution([r["goal_feedback_error_deg"] for r in points]),
        closest_joint_limit_rad=distribution([r["nearest_joint_limit_rad"] for r in points]),
        peak_joint_constraint_Nm=distribution([r["max_abs_constraint_Nm"] for r in points]),
        grip_relative_translation_m=distribution([r["grip_translation_from_window_start_m"] for r in points]),
        grip_relative_rotation_deg=distribution([r["grip_rotation_from_window_start_deg"] for r in points]),
        max_adjacent_grip_translation=max((r for r in points),key=lambda e:e["adjacent_grip_translation_m"],default=None),
        max_adjacent_grip_rotation=max((r for r in points),key=lambda e:e["adjacent_grip_rotation_deg"],default=None),
        bilateral_steps=[r["step"] for r in points if r["bilateral"]],
        grip_open_steps=[r["step"] for r in points if r["gripper_command"]<0],
        caddy_contacts=pair_info,book_caddy_steps=[r["step"] for r in points if r["caddy_book_contact_count"]],
        gripper_caddy_steps=[r["step"] for r in points if r["caddy_finger_contact_count"]],
        late=dict(steps=len(late),only_world_x_upper_failed_steps=[r["step"] for r in xonly],
            overrun_m=distribution([r["actual_book_x_over_upper_m"] for r in xonly]),
            implied_overrun_m=distribution([r["implied_book_x_over_upper_m"] for r in xonly]),
            implied_negative_correction_steps=[r["step"] for r in xonly if r["x_correction_at_goal_m"]<0],
            implied_x_fixed_steps=[r["step"] for r in xonly if r["implied_book_x_over_upper_m"]<0 and r["implied_book_x_over_lower_m"]>0],
            implied_x_overshoot_lower_steps=[r["step"] for r in xonly if r["implied_book_x_over_lower_m"]<=0],
            translation_only_still_above_upper_steps=[r["step"] for r in xonly if r["implied_x_over_upper_translation_only_m"]>=0],
            implied_inside_steps=[r["step"] for r in xonly if r["implied_inside_at_goal"]],
            goal_error_m=distribution([r["goal_feedback_error_m"] for r in late]),
            grip_drift_from_210_m=distribution([r["grip_translation_from_step_210_m"] for r in late]),
            grip_drift_from_210_deg=distribution([r["grip_rotation_from_step_210_deg"] for r in late])))
    return dict(run_id=execution.parent.name, summary=result,terminal=terminal,implementation=read(execution/"implementation.json"),
        baseline=read(execution/"baseline.json"),startup_resources=read(execution/"startup_resources.json"),
        orientation_frames=dict(raw_eef_rotation="Robosuite right_hand body quaternion",
            osc_target_rotation="grip_site", hand_body_to_grip_site=hand_to_site.tolist(),
            source_gripper_xml=gripper_xml.name, gripper_xml_sha256=hashlib.sha256(gripper_xml.read_bytes()).hexdigest()),
        meta=meta,gates=gates,recorded_steps=len(trace),measurements=window,checkpoints=checkpoint_metrics,
        first_divergence_step=min(drift,default=None),divergence_before_160=pre_drift,
        chunk_boundaries=[{k:r[k] for k in ("chunk","observation_step","planned_first_control_step",
                                            "planned_last_control_step","inference_seconds")} for r in chunks],
        resource_stats=resource_stats(active+phases),load_window_resource_stats=resource_stats(active_load),
        pressure=read(w/"pressure_event.json"),time_series=points)


def figures(execution, metric, output):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    output.mkdir(exist_ok=True,parents=True)
    w=execution/"worker"
    system=rows(w/"resources_supervisor.jsonl")
    lifecycle=rows(w/"resources_child.jsonl")
    if system:
        fig,ax=plt.subplots(figsize=(9,4.2),layout="constrained")
        start=system[0]["time"]
        for key,label in (("available_mib","Available RAM"),("swap_free_mib","Free swap"),
                          ("rss_mib","Worker RSS"),("pss_mib","Worker PSS")):
            raw=system if key in ("available_mib","swap_free_mib") else [
                r for r in system if r["phase"]=="child_active"]
            values=[(r["time"]-start,r[key]) for r in raw if r[key] is not None]
            if values:
                ax.plot(*zip(*values),label=label)
        for stage in ("model_load_start_no_environment","model_load_end_no_environment","after_official_reset"):
            r=next((r for r in lifecycle if r["phase"]==stage),None)
            if r:
                ax.axvline(r["time"]-start,linestyle=":",label=stage.replace("_"," "))
        ax.set(xlabel="Seconds since worker launch",ylabel="MiB")
        ax.legend(ncol=2,fontsize=7)
        fig.savefig(output/"resource_lifecycle.png",dpi=125)
        plt.close(fig)
    pts=metric["time_series"]
    if not pts:
        return
    steps=[r["step"] for r in pts]
    fig,axes=plt.subplots(4,1,sharex=True,figsize=(9,9),layout="constrained")
    for k,label in (("book_world_x_m","Actual book"),("book_world_x_if_goal_and_current_grasp_m","Book at goal (fixed grasp)"),
                    ("target_world_x_upper_m","BDDL world X upper bound"),("actual_eef_world_x_m","EEF"),
                    ("goal_eef_world_x_m","OSC goal")):
        axes[0].plot(steps,[1000*r[k] for r in pts],label=label)
    for i in range(3):
        axes[1].plot(steps,[1000*r["target_local_m"][i] for r in pts],label=f"Book in target [{i}]")
    for k,label in (("goal_feedback_error_m","EEF tracking error"),("grip_translation_from_window_start_m","Book in EEF drift")):
        axes[2].plot(steps,[1000*r[k] for r in pts],label=label)
    for k,label in (("clipped_axis_samples","Clipped joint samples"),("caddy_book_contact_count","Book/caddy points"),
                    ("caddy_finger_contact_count","Gripper/caddy points")):
        axes[3].plot(steps,[r[k] for r in pts],label=label)
    for ax in axes:
        ax.legend(ncol=2,fontsize=8)
    for ax in axes[:3]:
        ax.set_ylabel("mm")
    axes[3].set_xlabel("Control step")
    fig.savefig(output/"alignment_tracking_contacts.png",dpi=125)
    plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("execution",type=Path)
    parser.add_argument("--gripper-xml",type=Path,required=True)
    parser.add_argument("--summary",type=Path,required=True)
    parser.add_argument("--figures",type=Path,required=True)
    opts=parser.parse_args()
    data=summarize(opts.execution,opts.gripper_xml)
    opts.summary.parent.mkdir(parents=True,exist_ok=True)
    opts.summary.write_text(json.dumps(data,indent=2,ensure_ascii=False,allow_nan=False)+"\n")
    figures(opts.execution,data,opts.figures)


if __name__=="__main__":
    main()
