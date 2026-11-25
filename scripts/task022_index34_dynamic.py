"""Single authorized Task022-D diagnostic with the Task022-C1 lifecycle."""
import argparse
from pathlib import Path
import random
import subprocess
import sys
import time

from task022_index34_diagnostic import (ARCHIVE, ENV_RAM_MIB, HISTORY, INDEX, RNG, START_RAM_MIB,
    imports, monitor_resume, oom_kill_count, read, resume_gate, sha, verify, write)

PARENT = "52c3e820482663502f0f95e92a3b1ae1a009cf89"
LIMIT = 300


def diagnostic_worker(root, out):
    resources = imports(root)
    result = {"status": "INCONCLUSIVE", "loads_started": 0, "loads_completed": 0,
              "environments": 0, "resets": 0, "steps": 0,
              "inference_calls": 0, "completed_inferences": 0, "retries": 0,
              "count_in_official_success_rate": False}
    backend = env = telemetry = None

    def snapshot(phase):
        resources.log_sample(out, "child", phase, resources.sample())
        write(out/"progress.json", result)

    def stop_marker():
        return (out/"resource_pressure.request").is_file()

    try:
        from workbench.backends.xvla_backend import XVLABackend
        if not resume_gate(resources, out, "before_model_load", START_RAM_MIB):
            result.update(status="BLOCKED_RESOURCE", reason="before_model_load")
            return
        backend = XVLABackend()
        result["loads_started"] += 1
        snapshot("model_load_start_no_environment")
        start = time.monotonic()
        info = backend.load("lerobot/xvla-libero", "cpu")
        result.update(loads_completed=1, model_load_seconds=time.monotonic()-start)
        snapshot("model_load_end_no_environment")
        if stop_marker():
            result.update(status="BLOCKED_RESOURCE", reason="monitor_at_model_load_end")
            return
        from workbench.workers import book_pilot as worker
        from task022_index34_telemetry import Diagnostic
        if not resume_gate(resources, out, "after_model_before_environment", ENV_RAM_MIB):
            result.update(status="BLOCKED_RESOURCE", reason="after_model_before_environment")
            return
        if (info["action_chunk_size"], info["n_action_steps"]) != (30,30):
            raise ValueError("Action chunk configuration differs")
        _, env_post = worker.make_env_pre_post_processors(
            worker.LiberoEnvConfig(task=worker.SUITE, control_mode="absolute"), backend.policy.config)
        random.seed(RNG)
        worker.np.random.seed(RNG)
        worker.torch.manual_seed(RNG)
        result["environments"] += 1
        snapshot("before_environment_wrapper_creation")
        env = worker.book_environment(INDEX, worker.OFFICIAL_STATE_COUNT)
        if not resume_gate(resources, out, "before_official_reset", ENV_RAM_MIB):
            result.update(status="BLOCKED_RESOURCE", reason="before_official_reset")
            return
        obs = worker.reset_book_environment(env, INDEX, RNG)
        result["resets"] += 1
        snapshot("after_official_reset")
        files, state, fields = worker.reset_evidence(env, INDEX, RNG, out, obs)
        feedback = worker.observation_row(obs, env)
        src, ref = worker.task021_reference(INDEX)
        worker.verify_task021_reset(env, fields, state, feedback, src, ref)
        expected = read(out.parent/"baseline.json")["fingerprint"]
        c1 = read(ARCHIVE/"results/task022/c1/logs/lifecycle/combined_resume/result.json")
        reset = {k: fields[k] for k in expected}
        if reset != expected or reset != c1["fingerprint"]:
            raise ValueError("Reset fingerprint differs from Task021/C1")
        result.update(reset_verified=True, reset_fingerprint=reset, reset_builtin_settling_steps=env.num_steps_wait)
        worker.write_json(out/"reset.json", dict(fields=fields,state_8d=state,feedback=feedback))
        telemetry = Diagnostic(out, root/HISTORY/"events.jsonl")
        telemetry.attach(env)
        if telemetry.compare(0, feedback):
            raise ValueError("Historical Step 0 pose diverges")
        with (out/"chunks.jsonl").open("x",encoding="utf-8") as log:
            for chunk in range(LIMIT//30):
                step0 = result["steps"]
                if stop_marker():
                    result.update(status="BLOCKED_RESOURCE", reason="monitor_before_inference")
                    break
                if step0:
                    files, state = worker.save_input(obs,out,step0,worker.canonical_observation)
                result["inference_calls"] += 1
                snapshot(f"before_inference_{chunk}")
                prediction = backend.predict({
                    "task": env.task_description, "state": state.tolist(),
                    "sample_id": f"task020-201-{step0}",
                    "images": {f"{view}_camera": str(out/name) for view,name in files.items()},
                })
                result["completed_inferences"] += 1
                actions = worker.validate_chunk(backend, env_post, prediction, 30)
                prediction_path = f"chunk_{chunk:03d}.json"
                worker.write_json(out/prediction_path,prediction)
                metadata = dict(chunk=chunk, inference_call=result["inference_calls"],
                    observation_step=step0, planned_first_control_step=step0+1,
                    planned_last_control_step=min(step0+len(actions),LIMIT),
                    frame_paths=files, image_sha256={view: sha(out/name) for view,name in files.items()},
                    prediction_file=prediction_path, shape=actions.shape,
                    inference_seconds=prediction["timings_seconds"]["inference"])
                worker.event(log,**metadata)
                telemetry.input_meta = metadata
                telemetry.current_prediction = prediction["actions_7d"]
                snapshot(f"after_inference_{chunk}")
                if stop_marker():
                    result.update(status="BLOCKED_RESOURCE", reason="monitor_before_action_chunk")
                    break
                for offset, action in enumerate(actions):
                    obs, _, terminated, truncated, env_info = telemetry.execute(env, action)
                    result["steps"] += 1
                    step = result["steps"]
                    success = bool(env_info["is_success"])
                    feedback = worker.observation_row(obs, env)
                    controller = env._env.robots[0].controller
                    worker.np.testing.assert_allclose(controller.goal_pos, action[:3], rtol=0, atol=1e-6)
                    if offset == 0:
                        worker.np.testing.assert_allclose(controller.goal_ori,
                            worker.Rotation.from_rotvec(action[3:6]).as_matrix(), rtol=0, atol=1e-6)
                    telemetry.collect(step,offset,action,feedback,success,terminated,truncated)
                    if telemetry.compare(step, feedback):
                        result.setdefault("first_trajectory_divergence_step",step)
                    if step in (150,159,180,201,210,240,270,300) or terminated or truncated:
                        worker.save_input(obs,out,step,worker.canonical_observation)
                    if terminated or truncated:
                        result.update(status="ENVIRONMENT_END", reason="official_environment_end",
                                      observed_official_predicate=success)
                        break
                snapshot(f"after_action_chunk_{chunk}")
                if terminated or truncated:
                    break
                if stop_marker():
                    result.update(status="BLOCKED_RESOURCE", reason="monitor_after_action_chunk")
                    break
            else:
                result.update(status="PASS", reason="diagnostic_step_300_limit",
                              observed_official_predicate=success)
        if result["steps"]:
            worker.save_input(obs,out,result["steps"],worker.canonical_observation)
    except Exception as error:
        result.update(error=f"{type(error).__name__}: {error}",reason="diagnostic_exception")
        raise
    finally:
        try:
            if telemetry is not None:
                telemetry.close()
        finally:
            try:
                if env is not None:
                    env.close()
                    result["environment_closed"] = env._env is None
                    snapshot("after_environment_close")
            finally:
                if backend is not None:
                    backend.unload()
                    snapshot("after_model_unload")
                write(out/"result.json",result)


def run(root, out):
    resources = imports(root)
    out.mkdir(parents=True,exist_ok=False)
    command = [sys.executable,str(Path(__file__).resolve()),"--project-root",str(root),"--output",str(out),"--child"]
    write(out/"launch.json",dict(run_id=out.name,command=[sys.executable,str(Path(__file__).resolve()),*sys.argv[1:]],
          worker_command=command,cwd=str(Path.cwd()),dependency_sha=PARENT,attempt_limit=1,limit=LIMIT))
    import psutil
    psi = Path("/proc/pressure/memory")
    write(out/"startup_resources.json",
          dict(**resources.sample(), cpu_percent_system=psutil.cpu_percent(interval=0.2),
               pressure_memory=psi.read_text().strip() if psi.is_file() else None,
               oom_kill_count=oom_kill_count()))
    baseline = verify(root)
    c1 = read(ARCHIVE/"results/task022/c1/metrics/summary.json")
    if c1["status"]!="PASS" or c1["configuration_sha256"]!=baseline["configuration_sha256"]:
        raise ValueError("Task022-C1 checked dependency mismatch")
    if c1["fingerprint"] != baseline["fingerprint"]:
        raise ValueError("Task022-C1 fingerprint differs from fixed baseline")
    write(out/"baseline.json",baseline)
    head = subprocess.check_output(["git","-C",str(ARCHIVE),"rev-parse","HEAD"],text=True).strip()
    subprocess.run(["git","-C",str(ARCHIVE),"merge-base","--is-ancestor",PARENT,head],check=True)
    write(out/"implementation.json",dict(head=head,dependency_sha=PARENT,branch=subprocess.check_output(
        ["git","-C",str(ARCHIVE),"branch","--show-current"],text=True).strip(),
        git_status=subprocess.check_output(["git","-C",str(ARCHIVE),"status","--short"],text=True).splitlines(),
        files={name:sha(ARCHIVE/"scripts"/name) for name in ("task022_index34_dynamic.py",
             "task022_index34_telemetry.py","task022_index34_diagnostic.py")}))
    worker_dir = out/"worker"
    worker_dir.mkdir()
    deadline = time.monotonic()+60
    while not resume_gate(resources,worker_dir,"supervisor_before_worker",START_RAM_MIB):
        if time.monotonic() >= deadline:
            write(out/"exit.json",dict(status="BLOCKED_RESOURCE",reason="startup_ram_timeout",worker_started=False,exit_code=None))
            return
        time.sleep(min(10,max(0,deadline-time.monotonic())))
    before = resources.sample()
    initial_oom=oom_kill_count()
    resources.log_sample(worker_dir,"supervisor","before_worker",before)
    with (worker_dir/"worker.log").open("x") as log:
        proc = subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT)
        try:
            monitor_resume(resources,worker_dir,proc,initial_oom)
        finally:
            if proc.poll() is None:
                proc.terminate()
            proc.wait()
    after=resources.sample()
    final_oom=oom_kill_count()
    resources.log_sample(worker_dir,"supervisor","after_worker",after)
    marker=(worker_dir/"resource_pressure.request").exists()
    observed=read(worker_dir/"result.json") if (worker_dir/"result.json").is_file() else {}
    oom_difference=(final_oom-initial_oom if initial_oom is not None and final_oom is not None else None)
    status=("BLOCKED_RESOURCE" if marker or (oom_difference and proc.returncode!=0)
            else observed.get("status","INCONCLUSIVE") if proc.returncode==0 else "INCONCLUSIVE")
    write(out/"exit.json",dict(status=status,worker_started=True,exit_code=proc.returncode,
          pressure_marker=marker,oom_kill_before=initial_oom,oom_kill_after=final_oom,
          global_oom_counter_increment=oom_difference,before=before,after=after))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--child",action="store_true",help=argparse.SUPPRESS)
    options=parser.parse_args()
    root=options.project_root.resolve(strict=True)
    out=options.output.resolve()
    if options.child:
        diagnostic_worker(root,out/"worker")
    else:
        run(root,out)


if __name__=="__main__":
    main()
