"""Task022-C preflight. This entry point never performs policy inference or control."""
import argparse
import gc
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import subprocess
import sys
import time


ARCHIVE = Path(__file__).resolve().parents[1]
REVISION = "8e6aeef01f634f5d3b5be4340328f19cc2c25a65"
HISTORY = "results/task021/b2b/runs/b2b_index_34_rng_201_1795501086954054532"
B_RUN = "diagnostic_index_34_rng_201_1795571278349401651"
INDEX, RNG = 34, 201


def read(path):
    return json.loads(path.read_text())


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def write(path, item):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n")
    temp.replace(path)


def historical_reset(path):
    with path.open() as stream:
        for line in stream:
            row = json.loads(line)
            if row["type"] == "reset":
                return row
    raise ValueError("Baseline Reset event missing")


def cache_snapshot():
    hub = Path(os.environ.get("HF_HUB_CACHE", os.environ.get("HUGGINGFACE_HUB_CACHE",
        Path(os.environ.get("HF_HOME", Path(os.environ.get("XDG_CACHE_HOME", Path.home()/".cache"))/"huggingface"))/"hub")))
    repo = hub / "models--lerobot--xvla-libero"
    if (repo/"refs/main").read_text().strip() != REVISION:
        raise ValueError("Cached backend revision differs")
    return repo/"snapshots"/REVISION


def verify(root):
    a = read(root/"results/task022/a/metrics/summary.json")
    source = read(root/"results/task021/metrics/inventory_source.json")
    ref = read(root/"results/task021/metrics/initial_states.json")[INDEX]
    old = root/HISTORY
    c = read(old/"configuration.json")
    prior = ARCHIVE/"results/task022/b"
    b = read(prior/"logs/preflight.json")
    local_b = root/"results/task022/b/runs"/B_RUN
    for name in ("preflight.json", "configuration.json", "summary.json", "reproduction.jsonl"):
        if sha(local_b/name) != sha(prior/"logs"/name):
            raise ValueError("Task022-B historical file differs: " + name)
    if not (c == read(local_b/"configuration.json") and c["checkpoint_revision"] == REVISION
            and c["device"] == "cpu" and b["historical_config_sha256"] == sha(old/"configuration.json")
            and read(prior/"acceptance.json")["status"] == "BLOCKED_RESOURCE"):
        raise ValueError("Historical Task021 / Task022-B baseline differs")
    for package, expected in c["versions"].items():
        if version(package) != expected:
            raise ValueError("Installed version differs: " + package)
    snapshot = cache_snapshot()
    for name, expected in c["checkpoint_files"].items():
        file = snapshot/name
        if file.stat().st_size != expected["bytes"] or sha(file) != expected["sha256"]:
            raise ValueError("Checkpoint/Processor file differs: " + name)
    if any(sha(root/path) != expected for path, expected in a["installed_sources_sha256"].items()):
        raise ValueError("Installed Task022-A source file differs")
    if sha(root/"workbench/workers/book_resources.py") != source["source_hashes"]["resource_guard"]:
        raise ValueError("Original Workbench resource guard differs")
    files = a["runs"]["34"]["source_files_sha256"]
    for name, expected in files.items():
        if sha(old/name) != expected:
            raise ValueError("Task021 historical file differs: " + name)
    bddl = next(root.glob(".venv_xvla/lib/python*/site-packages/libero/libero/bddl_files/libero_10/" + source["bddl"]["file"]))
    libero = bddl.parents[2]
    asset = libero/"init_files"/source["installed_asset"]["file"]
    if not asset.is_file():
        asset = next(libero.glob("*/" + source["installed_asset"]["file"]))
    portable = asset.with_suffix(asset.suffix + ".npy")
    if portable.is_file():
        asset = portable
    reset = historical_reset(old/"events.jsonl")
    fingerprint = {name: reset[name] for name in ("instruction","bddl","official_state_sha256",
                                                   "initial_state_asset_sha256","rgb_array_sha256")}
    if (sha(asset) != fingerprint["initial_state_asset_sha256"] or sha(bddl) != source["bddl"]["sha256"]
        or fingerprint["instruction"] != source["task_description"] or source["bddl"]["file"] != fingerprint["bddl"]
        or b["prompt"] != fingerprint["instruction"] or b["bddl_sha256"] != sha(bddl)
        or b["asset_sha256"] != sha(asset) or b["initial_sha256"] != fingerprint["official_state_sha256"]
        or b["rgb_array_sha256"] != fingerprint["rgb_array_sha256"]
        or ref["rgb_array_sha256"] != fingerprint["rgb_array_sha256"]
        or ref["official_state_sha256"] != fingerprint["official_state_sha256"]
        or ref["index"] != INDEX or ref["reset_seed"] != RNG):
        raise ValueError("Historical Reset, prompt, BDDL or asset differs")
    return dict(status="PASS", configuration_sha256=sha(old/"configuration.json"), hashes=c["checkpoint_files"],
                revision=REVISION, checked_history_files=len(files), versions=c["versions"],
                bddl_sha256=sha(bddl), fingerprint=fingerprint, source_entry_sha256=sha(Path(__file__)),
                project_path=root.name, archive_path=ARCHIVE.name, history_path=HISTORY)


def imports(root):
    sys.path.insert(0, str(root))
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ.setdefault("MUJOCO_GL", "egl")
    from workbench.workers import book_resources
    return book_resources


def gate(resources, target, phase, ram=0, swap=0):
    previous = resources.formal_gate(target, phase, component="preflight")
    sample = resources.sample()
    allowed = previous is None and sample["available_mib"] >= ram and sample["swap_free_mib"] >= swap
    with (target/"gates.jsonl").open("a", encoding="utf-8") as out:
        print(json.dumps(dict(phase=phase, allowed=allowed, min_ram_mib=ram, min_swap_mib=swap, **sample)), file=out)
    return allowed


def child(root, target, phase):
    import random
    resources = imports(root)
    from workbench.workers import book_pilot as worker
    baseline = read(target.parent/"baseline.json")["fingerprint"]
    result = dict(status="INCONCLUSIVE", phase=phase, loads_started=0, models_loaded=0,
                  environment_creations=0, resets=0, reset_started=0, forward_calls=0, control_steps=0)
    env = model = None

    def sample(stage):
        resources.log_sample(target, "child", stage, resources.sample())

    try:
        sample("child_imports_ready")
        if phase == "combined":
            if not gate(resources, target, "before_model_load", 3072, 1024):
                result["status"] = "BLOCKED_RESOURCE"
                return
            model = worker.XVLABackend()
            result["loads_started"] += 1
            sample("model_load_start_no_environment")
            model_info = model.load(worker.MODEL, "cpu")
            result["models_loaded"] += 1
            sample("model_load_end_no_environment")
            if not gate(resources, target, "after_model_before_environment", 1536, 512):
                result["status"] = "BLOCKED_RESOURCE"
                return
            if (model_info["action_chunk_size"], model_info["n_action_steps"]) != (30, 30):
                raise ValueError("Loaded policy queue differs")
        elif not gate(resources, target, "reset_only_before_environment"):
            result["status"] = "BLOCKED_RESOURCE"
            return
        random.seed(RNG)
        worker.np.random.seed(RNG)
        worker.torch.manual_seed(RNG)
        sample("before_environment_creation")
        result["environment_creations"] += 1
        env = worker.book_environment(INDEX, worker.OFFICIAL_STATE_COUNT)
        sample("after_environment_wrapper_creation")
        if resources.checkpoint(target, "before_official_reset"):
            result["status"] = "BLOCKED_RESOURCE"
            return
        result["reset_started"] += 1
        obs = worker.reset_book_environment(env, INDEX, RNG)
        result["resets"] += 1
        sample("after_official_reset")
        if resources.checkpoint(target, "after_official_reset"):
            result["status"] = "BLOCKED_RESOURCE"
            return
        _, state, fields = worker.reset_evidence(env, INDEX, RNG, target, obs)
        src, ref = worker.task021_reference(INDEX)
        worker.verify_task021_reset(env, fields, state, worker.observation_row(obs, env), src, ref)
        actual = {key: fields[key] for key in baseline}
        if actual != baseline:
            raise ValueError("Historical Reset fingerprints differ")
        if phase == "combined" and actual != read(target.parent/"reset_only/result.json")["fingerprint"]:
            raise ValueError("C2 and C3 fingerprints differ")
        result.update(status="PASS", fingerprint=actual, reset_builtin_settling_steps=env.num_steps_wait)
    except Exception as error:
        result["error"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        try:
            if env is not None:
                env.close()
                result["env_wrapper_released_inner_env"] = env._env is None
                env = None
                sample("after_environment_close")
        finally:
            try:
                if model is not None:
                    model.unload()
                    model = None
                    sample("after_model_unload")
            finally:
                gc.collect()
                sample("before_child_exit")
                write(target/"result.json", result)


def supervise(root, output, phase):
    resources = imports(root)
    target = output/phase
    target.mkdir()
    before = resources.sample()
    resources.log_sample(target, "supervisor", "before_child_start", before)
    ram, swap = (3072, 1024) if phase == "combined" else (0, 0)
    if not gate(resources, target, "supervisor_before_child", ram, swap):
        result = dict(status="BLOCKED_RESOURCE", worker_started=False, exit_code=None,
                      reason="supervisor_start_gate", before=before, after=resources.sample())
        write(target/"exit.json", result)
        return result["status"]
    command = [sys.executable, str(Path(__file__).resolve()), "--project-root", str(root),
               "--output", str(output), "--child", phase]
    with (target/"worker.log").open("x") as log:
        proc = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
        try:
            while proc.poll() is None:
                metrics = resources.sample(proc.pid)
                resources.log_sample(target, "supervisor", "child_active", metrics)
                if resources.under_pressure(metrics) or metrics["swap_free_mib"] < 128:
                    (target/"resource_pressure.request").touch()
                time.sleep(1)
        finally:
            if proc.poll() is None:
                proc.terminate()
            proc.wait()
    finish = resources.sample()
    resources.log_sample(target, "supervisor", "after_child_exit", finish)
    stopped = (target/"resource_pressure.request").exists()
    observed = read(target/"result.json") if (target/"result.json").is_file() else {}
    status = ("BLOCKED_RESOURCE" if stopped else
              observed.get("status", "INCONCLUSIVE") if proc.returncode == 0 else "INCONCLUSIVE")
    write(target/"exit.json", dict(status=status, worker_started=True, exit_code=proc.returncode,
                                  pressure_marker=stopped, command=command, before=before, after=finish))
    return status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ARCHIVE)
    parser.add_argument("--output", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight-only", action="store_true")
    mode.add_argument("--lifecycle-preflight", action="store_true")
    mode.add_argument("--child", choices=("reset_only","combined"), help=argparse.SUPPRESS)
    args = parser.parse_args()
    root, output = args.project_root.resolve(strict=True), args.output.resolve()
    if args.child:
        child(root, output/args.child, args.child)
        return
    output.mkdir(parents=True, exist_ok=False)
    write(output/"launch.json", dict(command=[sys.executable,str(Path(__file__).resolve()),*sys.argv[1:]],
          cwd=str(Path.cwd()), run_id=output.name, preflight_only=args.preflight_only))
    try:
        write(output/"baseline.json", verify(root))
    except Exception as error:
        write(output/"summary.json", dict(status="INCONCLUSIVE", error=f"{type(error).__name__}: {error}"))
        raise
    if args.preflight_only:
        write(output/"summary.json", dict(status="PASS", model_loads=0, resets=0, forward_calls=0, control_steps=0))
        return
    c2 = supervise(root, output, "reset_only")
    c3 = supervise(root, output, "combined") if c2 == "PASS" else "NOT_RUN"
    write(output/"summary.json", dict(status=c3 if c3 != "NOT_RUN" else c2, c2=c2, c3=c3,
                                      forward_calls=0, control_steps=0, retries=0))


if __name__ == "__main__":
    main()
