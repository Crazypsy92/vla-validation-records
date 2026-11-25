
"""Offline Task022-A audit. Reads exported JSON and MP4, with no simulation imports."""
from pathlib import Path
import hashlib
import itertools
import json
import os
import xml.etree.ElementTree as ET

import cv2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
from scipy.spatial.transform import Rotation

out = Path("results/task022/a")
evidence = Path("evidence/task022/a")
evidence.mkdir(parents=True, exist_ok=True)
site = Path(".venv_xvla/lib/python3.12/site-packages")
lib = site / "libero/libero"
asset = lib / "assets/turbosquid_objects"
keys = {15: [0, 46, 54, 58, 120, 180, 200, 201],
        34: [0, 50, 56, 69, 120, 180, 200, 210, 240, 300, 390, 420, 480, 520]}
expected = {15: (201, 7, True), 34: (520, 18, False)}
runs = {i: next(Path(f"results/task021/{tag}/runs").glob("b2*")) for i, tag in [(15,"b2a"),(34,"b2b")]}

def read(p):
    return json.loads(p.read_text())

def lines(p):
    return [json.loads(l) for l in p.read_text().splitlines()]

def digest(p):
    with p.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

def rot(q):
    return Rotation.from_quat(np.roll(q, -1)).as_matrix()

def vec(node, key, default):
    return np.array([float(x) for x in node.get(key, default).split()])

def shape(node):
    return (vec(node,"pos","0 0 0"), rot(vec(node,"quat","1 0 0 0")), vec(node,"size",""))

def box_intersects(a, b):
    pa, ra, ha = a
    pb, rb, hb = b
    axes = [*ra.T, *rb.T, *(np.cross(x,y) for x in ra.T for y in rb.T)]
    return all(abs((pb-pa)@v) <= np.abs(v@ra)@ha + np.abs(v@rb)@hb + 1e-8 for v in axes)

def first(seq):
    return next((i for i, v in enumerate(seq) if v), None)

def stats(x):
    return {"min": np.min(x,axis=0).tolist(), "max":np.max(x,axis=0).tolist(),
            "mean":np.mean(x,axis=0).tolist(), "median":np.median(x,axis=0).tolist()}

bookxml = asset / "black_book/black_book.xml"
caddyxml = asset / "desk_caddy/desk_caddy.xml"
bookbox, = ET.parse(bookxml).findall(".//geom[@type='box']")
caddy = ET.parse(caddyxml)
targetpos, targetrot, targetsize = shape(caddy.find(".//site[@name='back_contain_region']"))
boxes = [shape(x) for x in caddy.findall(".//geom[@type='box']")]
bookoffset, bookboxrot, bookhalf = shape(bookbox)
corner_signs = np.array(list(itertools.product((-1,1), repeat=3)))
refs = read(Path("results/task021/metrics/initial_states.json"))
source = read(Path("results/task021/metrics/inventory_source.json"))
reference_cfg = read(Path("results/task020/r1/phase3/runs/phase3_seed_201/configuration.json"))
source_paths = [bookxml,caddyxml,lib/"envs/objects/turbosquid_objects.py",lib/"envs/objects/site_object.py",
                lib/"envs/object_states/base_object_states.py",lib/"envs/predicates/base_predicates.py",
                Path("workbench/backends/xvla_backend.py"), Path("scripts/task018_gripper_verification.py"),
                Path("workbench/workers/book_pilot.py"),site/"lerobot/sim/integrations/libero.py",
                site/"robosuite/controllers/osc.py",
                lib/"bddl_files/libero_10"/source["bddl"]["file"]]

def analyze(i, path):
    rows=lines(path/"events.jsonl")
    s=read(path/"summary.json")
    cfg=read(path/"configuration.json")
    directory_files={f.name:digest(f) for f in sorted(path.iterdir()) if f.is_file()}
    assert cfg==reference_cfg
    for name in ("config.json","policy_preprocessor.json","policy_postprocessor.json"):
        assert directory_files[name]==cfg["checkpoint_files"][name]["sha256"]
    assert all(r["run_id"]==path.name for r in rows)
    assert all(a["monotonic_ns"]<=b["monotonic_ns"] for a,b in zip(rows,rows[1:]))
    reset,=[r for r in rows if r["type"]=="reset"]
    step=[r for r in rows if r["type"]=="step"]
    state=[reset]+step
    infer=[r for r in rows if r["type"]=="inference"]
    obs=[r for r in rows if r["type"]=="observation"]
    n,count,result=expected[i]
    assert [r["step"] for r in state]==list(range(n+1)) and len(infer)==len(obs)==count
    assert s["official_initial_state_index"]==reset["official_initial_state_index"]==i
    assert s["reset_rng_seed"]==reset["reset_rng_seed"]==201 and s["official_success"] is result
    assert reset["official_state_sha256"]==refs[i]["official_state_sha256"]
    assert reset["initial_state_asset_sha256"]==source["installed_asset"]["sha256"]
    assert reset["instruction"]==s["instruction"]==source["task_description"]
    assert reset["bddl"]==source["bddl"]["file"] and s["max_steps"]==520
    assert int((path/"worker_exit_code.txt").read_text())==0 and not (path/"resource_pressure.request").exists()
    assert step[-1]["is_success"] is result and (step[-1]["terminated"] if result else (step[-1]["truncated"] or n==520))
    gates=lines(path/"formal_gate_gui.jsonl")+lines(path/"formal_gate_worker.jsonl")
    assert all(g["level"]!="BLOCKED_RESOURCE" for g in gates)
    summary=read(path.parents[1]/"metrics/summary.json")
    assert not summary["runtime_oom_observed"] and not summary["pressure_requested"]
    execution=[]
    plans={}
    for j,(inf,ob) in enumerate(zip(infer,obs)):
        plan=read(path/inf["file"])
        off=30*j
        executed=[r for r in step if r["chunk"]==j]
        assert inf["step"]==ob["step"]==off and inf["chunk"]==ob["chunk"]==j
        assert state[off]["monotonic_ns"]<=ob["monotonic_ns"]<=inf["monotonic_ns"]
        assert plan["initial_state_8d"]==ob["state_8d"]==inf["state_8d"] and len(ob["state_8d"])==8
        if off:
            previous,=[r for r in rows if r["type"]=="chunk_finished" and r["chunk"]==j-1]
            assert previous["step"]==off and state[off]["monotonic_ns"]<=previous["monotonic_ns"]<=ob["monotonic_ns"]
        assert plan["task"]==ob["task"]==reset["instruction"] and plan["model_id"]=="lerobot/xvla-libero"
        assert len(plan["transformed_state_9d"])==ob["processor_state_dim"]==9
        assert np.asarray(plan["raw_actions_20d"]).shape==(30,20) and np.asarray(plan["actions_7d"]).shape==(30,7)
        assert np.isfinite(plan["raw_actions_20d"]).all() and np.isfinite(plan["actions_7d"]).all()
        assert list(ob["image_shapes"].values())==[[256,256,3],[256,256,3]] and ob["files"]==inf["files"]
        assert all(directory_files[name]==ob["image_file_sha256"][view] for view,name in ob["files"].items())
        assert [r["offset"] for r in executed]==list(range(len(executed))) and len(executed)==min(30,n-off)
        np.testing.assert_allclose([r["action"] for r in executed],plan["actions_7d"][:len(executed)],atol=1e-6,rtol=0)
        assert any(g["phase"]==f"before_inference_{j}" for g in gates)
        assert any(g["phase"]==f"before_actions_{j}" for g in gates)
        execution.append(dict(chunk=j,input_step=off,executed_steps=len(executed),sample_id=plan["sample_id"]))
        plans[j]=plan
    tpos=np.array(reset["target_site_position_m"])
    tr=rot(reset["target_site_quaternion_wxyz"])
    th=np.array(reset["target_site_half_size_m"])
    np.testing.assert_allclose(th,targetsize,atol=1e-9)
    cr=tr@targetrot.T
    cp=tpos-cr@targetpos
    np.testing.assert_allclose(cp,refs[i]["caddy"]["position_m"],atol=1e-7)
    np.testing.assert_allclose(cr,rot(refs[i]["caddy"]["quaternion_wxyz"]),atol=1e-7)
    cboxes=[(cp+cr@v,cr@r,h) for v,r,h in boxes]
    delta=np.array([r["book_position"] for r in state])-tpos
    local=delta@tr
    eef=np.array([r["robot_state"]["eef"]["pos"] for r in state])
    eef_r=np.array([r["robot_state"]["eef"]["mat"] for r in state])
    obj_r=np.array([rot(r["book_quaternion_wxyz"]) for r in state])
    bookrel=np.einsum("nji,nj->ni",eef_r,delta+tpos-eef)
    relative_r=eef_r.transpose(0,2,1)@obj_r
    goal=np.array([r["osc_goal_position"] for r in step])
    command=np.array([r["action"] for r in step])
    np.testing.assert_allclose(command[:,:3],goal,atol=1e-6,rtol=0)
    osc_r=np.array([r["osc_goal_orientation"] for r in step])
    np.testing.assert_allclose(osc_r,Rotation.from_rotvec(command[:,3:6]).as_matrix(),atol=1e-6,rtol=0)
    rot_error=np.r_[np.nan,Rotation.from_matrix(eef_r[1:].transpose(0,2,1)@osc_r).magnitude()*180/np.pi]
    err=np.vstack([np.full(3,np.nan),goal-eef[1:]])@tr
    inside=np.array([r["on_target"] for r in state])
    w_half=np.abs(tr@th)
    lo=-w_half.copy()
    lo[2]-=.01
    inferred=(delta>lo)&(delta<w_half)
    margins=np.minimum(delta-lo,w_half-delta)
    opening=np.array([r["gripper_opening_m"] for r in state])
    bilateral=np.array([r["left_contact"] and r["right_contact"] for r in state])
    lift=np.array([r.get("lift_m",0) for r in state])
    lims=[]
    overlap=[]
    for row, r in zip(state,obj_r):
        center=np.array(row["book_position"])+r@bookoffset
        br=r@bookboxrot
        corners=(center+(corner_signs*bookhalf)@br.T-tpos)@tr
        lims.append([corners.min(axis=0),corners.max(axis=0)])
        overlap.append([k for k,b in enumerate(cboxes) if box_intersects((center,br,bookhalf),b)])
    lims=np.asarray(lims)
    nearest=int(np.argmin(np.linalg.norm(local,axis=1)))
    near=(np.abs(local[:,0])<=.055) & (np.abs(local[:,1])<=th[1]) & (np.abs(local[:,2])<=.10)
    snaps={}
    for j,row in enumerate(state):
        r=dict(step=j,book_world_xyz_m=row["book_position"],book_site_xyz_m=local[j].tolist(),
            book_site_quat_xyzw=Rotation.from_matrix(tr.T@obj_r[j]).as_quat().tolist(),
            book_collision_box_site_bounds_m=lims[j].tolist(),static_caddy_box_overlap_ids=overlap[j],
            book_in_eef_xyz_m=bookrel[j].tolist(),book_in_eef_quat_xyzw=Rotation.from_matrix(relative_r[j]).as_quat().tolist(),
            center_official_axis_margin_xyz_m=margins[j].tolist(),official_proxy=bool(inferred[j].all()),
            on_target=bool(inside[j]),eef_site_xyz_m=((eef[j]-tpos)@tr).tolist(),
            eef_world_xyz_m=eef[j].tolist(),eef_world_quat_xyzw=row["robot_state"]["eef"]["quat"],
            osc_goal_xyz_m=goal[j-1].tolist() if j else None,
            goal_minus_eef_site_xyz_m=err[j].tolist() if j else None,
            osc_goal_eef_rotation_error_deg=float(rot_error[j]) if j else None,
            executed_7d=row.get("action"),predicted_7d=plans[row["chunk"]]["actions_7d"][row["offset"]] if j else None,
            left_contact=row["left_contact"],right_contact=row["right_contact"],book_gripper_contacts=row["book_gripper_contacts"],
            gripper_qpos=row["robot_state"]["gripper"]["qpos"],gripper_opening_m=opening[j],lift_m=lift[j],
            frame_index=j,video_time_s=j/20)
        snaps[str(j)]=r
    encoded=json.dumps(snaps,ensure_ascii=False,allow_nan=False,separators=(",",":"))
    (out/"metrics"/f"index_{i}_trajectory.json").write_text(encoded+"\n")
    cap=cv2.VideoCapture(str(path/"rollout.mp4"))
    assert cap.isOpened()
    fps=cap.get(cv2.CAP_PROP_FPS)
    decoded=0
    rendered={}
    frameset=set(keys[i])
    while True:
        ok,im=cap.read()
        if not ok:break
        assert im.shape==(256,512,3)
        if decoded in frameset:rendered[decoded]=Image.fromarray(cv2.cvtColor(im,cv2.COLOR_BGR2RGB))
        decoded+=1
    cap.release()
    assert decoded==n+1 and fps==20 and set(rendered)==frameset
    assert directory_files["rollout.mp4"]==summary["video"]["sha256"]
    sheet=Image.new("RGB",(1024,280*((len(keys[i])+1)//2)),"white")
    draw=ImageDraw.Draw(sheet)
    for k,j in enumerate(keys[i]):
        x,y=k%2*512,k//2*280
        draw.text((x+8,y+5),f"Index {i} | Step {j} | {j/fps:.2f}s | Workspace + Wrist",fill="black")
        sheet.paste(rendered[j],(x,y+24))
    sheet.save(evidence/f"index_{i}_video_keyframes.jpg",quality=90,optimize=True)
    tail0=180 if result else 210
    tail=slice(tail0,None)
    taildelta=delta[tail]
    eef_shift=eef[-1]-eef[tail0]
    goal_shift=goal[-1]-goal[tail0-1]
    data=dict(run_id=path.name,steps=n,inferences=count,official_success=result,terminal_reason=s["terminal_reason"],
        terminated=step[-1]["terminated"],truncated=step[-1]["truncated"],worker_exit_code=0,resource_blocked=False,
        initial_state_index=i, reset_rng_seed=201, raw_state_sha256=reset["official_state_sha256"],
        source_files_sha256=directory_files,configuration=cfg,chunk_execution=execution,
        target_site=dict(center_world_m=tpos.tolist(),quat_wxyz=reset["target_site_quaternion_wxyz"],
                         half_size_m=th.tolist(),cad_body_pose_reconstruction_verified_at_reset=True),
        key_steps={str(j):snaps[str(j)] for j in keys[i]},
        phase_steps=dict(first_motion=first(np.linalg.norm(eef-eef[0],axis=1)>.01),
                         first_close=1+first(command[:,-1]>0),first_bilateral=first(bilateral),
                         first_lift_gt_2cm=first(lift>.02),first_neighborhood=first(near),closest_center_step=nearest,
                         first_on_target=first(inside),first_release_after_close=next((j+1 for j in range(1,n) if command[j-1,-1]>0>command[j,-1]),None)),
        near_definition="abs local X <=55 mm; abs local Y <= site half width; abs local Z <=100 mm",
        lift_peak_m=float(lift.max()), opening_m=stats(opening), opening_after_close_m=stats(opening[1:][command[:,-1]>0]),
        on_target_count=int(inside.sum()),release_verified=s["stages"]["RELEASE_PHYSICALLY_VERIFIED"],
        historical_gripper_actuated=s["stages"]["GRIPPER_ACTUATED"],
        official_proxy_mismatches=np.where(inferred.all(axis=1)!=inside)[0].tolist(),
        video=dict(status="AVAILABLE",frames=decoded,fps=fps,sha256=directory_files["rollout.mp4"],
                   mapping="video frame 0=reset; frame N=step N, after step; frame time=N/20 s"),
        tail=dict(start=tail0,book_world_xyz_m=stats(delta[tail]+tpos),book_site_m=stats(local[tail]),
                  goal_world_m=stats(goal[tail0-1:]),eef_world_m=stats(eef[tail]),
                  goal_minus_eef_site_m=stats(err[tail]),goal_minus_eef_world_m=stats(goal[tail0-1:]-eef[tail]),
                  goal_rotation_error_deg=stats(rot_error[tail]),book_in_eef_m=stats(bookrel[tail]),
                  book_eef_world_m=stats(delta[tail]+tpos-eef[tail]),book_relative_rotation_drift_deg=stats(Rotation.from_matrix(tiprot(relative_r[tail],relative_r[tail0])).magnitude()*180/np.pi),
                  goal_shift_world_m=goal_shift.tolist(),eef_shift_world_m=eef_shift.tolist(),
                  book_shift_world_m=(delta[-1]-delta[tail0]).tolist(),
                  center_X_margin_m=stats(margins[tail,0]),affected_axes_count=(~inferred[tail]).sum(axis=0).tolist(),
                  bilateral_count=int(bilateral[tail].sum()),opening_m=stats(opening[tail]),
                  caddy_obb_screen_overlap_steps=sum(bool(x) for x in overlap[tail0:]),
                  observation_count=len(obs)))
    return data,(local,err,rot_error,opening,bilateral,inside,margins,goal,eef,tr,tpos)

def tiprot(stack,ref):
    return ref.T@stack

all_data={}; trajectories={}
for i,p in runs.items():
    all_data[i],trajectories[i]=analyze(i,p)
# Kinematic substitution using each observed book–EEF offset, with orientation held.
# This is a diagnostic, not a feasibility test or a proposed controller change.
for i, data in all_data.items():
    local, err, _, opening, bi, target, margins, goal, eef, tr, tpos = trajectories[i]
    start=data["tail"]["start"]
    stop=len(local)
    h=np.abs(tr@np.array(data["target_site"]["half_size_m"]))
    lower=-h.copy();lower[2]-=.01
    world=local@tr.T
    substitute=world[1:]+goal-eef[1:]
    six=[]
    trajectory=read(out/"metrics"/f"index_{i}_trajectory.json")
    for j in range(30,stop,30):
        block=np.array([trajectory[str(k)]["osc_goal_xyz_m"] for k in range(j-29,j+1)])
        six.append(dict(last_step=j,goal_x_range_m=float(np.ptp(block[:,0])),goal_x_mean_m=float(block[:,0].mean())))
    proxy_axes=(substitute[start-1:]>lower)&(substitute[start-1:]<h)
    data["tracking_substitution_diagnostic"]=dict(
        first_step=start,last_step=stop-1,samples=stop-start,
        hypothetical_world_axes_within_count=proxy_axes.sum(axis=0).tolist(),
        hypothetical_all_axes_within_count=int(proxy_axes.all(axis=1).sum()),
        assumption="Book center translated only by recorded OSC goal position minus actual EEF; same orientation and observed grasp offset.")
    data["stall_probe"]=dict(tail_goal_chunks=six, book_world_x_300_to_end_mm=float(np.ptp(world[300:,0])*1000) if i==34 else None)
    data["coverage"]=dict(reset_records=1,step_records=stop-1,observation_records=data["inferences"],
        inference_records=data["inferences"],action_commands_verified=stop-1,video_frames=data["video"]["frames"],
        target_pose_recorded_at_steps=[0], all_sim_contacts_recorded=False, joint_torques_recorded=False)

fig, axs=plt.subplots(6,2,figsize=(15,14),layout="constrained")
for col,(i,pack) in enumerate(trajectories.items()):
    local,err,rerr,opening,bi,target,margin,goal,eef,tr,tpos=pack
    axs[0,col].set_title(f"Index {i} | {all_data[i]['run_id']}")
    for k, label in enumerate("XYZ"):
        axs[0,col].plot(local[:,k]*100,label=label)
        axs[2,col].plot(err[:,k]*100,label=label)
    axs[0,col].set_ylabel("Book site-local (cm)")
    axs[0,col].axhline(2.775,ls=":",color="gray");axs[0,col].axhline(-2.775,ls=":",color="gray")
    axs[1,col].plot(np.arange(1,len(goal)+1), ((goal-tpos)@tr)[:,0]*100,label="OSC goal X")
    axs[1,col].plot(((eef-tpos)@tr)[:,0]*100,label="EEF feedback X")
    axs[1,col].plot(local[:,0]*100,label="Book X")
    axs[1,col].set_ylabel("Site-local X (cm)")
    axs[2,col].set_ylabel("Goal – EEF (cm)")
    axs[3,col].plot(rerr,color="tab:purple")
    axs[3,col].set_ylabel("Rotation tracking (deg)")
    axs[4,col].plot(opening*100,label="Opening (cm)");axs[4,col].step(np.arange(len(bi)),bi*2,label="Bilateral (scaled)")
    axs[4,col].axhline(2.5,ls=":",color="gray",label="Actuated threshold")
    axs[4,col].set_ylabel("Gripper")
    axs[5,col].plot(margin[:,0]*100,label="Official world X margin (cm)")
    axs[5,col].step(np.arange(len(target)),target,label="Logged on_target")
    axs[5,col].axhline(0,ls=":",color="gray")
    axs[5,col].set_xlabel("Recorded step")
    axs[5,col].set_ylabel("Official predicate")
    for k,a in enumerate(axs[:,col]):
        for step in range(30,len(local),30):a.axvline(step,color="#aaaaaa",alpha=.4,lw=.6)
        if k!=3:a.legend(loc="best",fontsize=7)
fig.savefig(evidence/"trajectory_comparison.png",dpi=120)
plt.close(fig)
result=dict(stage="A",model_loads=0,new_inferences=0,new_formal_runs=0,runs=all_data,
    geometry=dict(book_box_offset_m=bookoffset.tolist(),book_box_half_size_m=bookhalf.tolist(),caddy_collidable_boxes=len(boxes),
       predicate="SiteObjectState.check_contact=True; check_contain calls SiteObject.in_box on book body origin with strict world-axis bounds, total_size=abs(site_matrix @ size), world Z lower bound -= 0.01 m",
       proxy_assumption="Use Reset site transform at all steps; identical target predicate comparison is a cross-check, not dynamic pose evidence.",
       contact_proxy_box_id_1=dict(role="caddy divider box", local_center_m=boxes[1][0].tolist(),half_size_m=boxes[1][2].tolist()),
       box_overlap="Static geometry OBB SAT on installed XML; screening only, not measured simulator collision or contact force.",
       missing=["per-step caddy/site transform","caddy contacts and contact impulse/normal","OSC torque limits and saturation"]),
    installed_sources_sha256={str(p):digest(p) for p in source_paths})
(out/"metrics/summary.json").write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+"\n")
for i,v in all_data.items():
 print(i,"steps",v["steps"],"infer",v["inferences"],"phase",v["phase_steps"],"terminal",v["key_steps"][str(v["steps"])]["book_site_xyz_m"],"predicate mismatch",v["official_proxy_mismatches"])
 print("tail",v["tail"])
