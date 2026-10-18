#!/usr/bin/env python3

import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
SCRATCH = ROOT / ".scratch"
OUTPUT = ROOT / "reports/round-14/guard/retro-tests.json"
COMMAND = "export TMPDIR=\"$PWD/.scratch\"; python3 reports/round-14/guard/retro-tests.py"
BASELINE = "926c86f8be3cc9307f8f10dce55768c290b6f94d"
R8 = "e1694bad6ac96aca45a11ca5746582b275929355"
R9 = "9dc18ec1339bffd6f81e74f1a5742464ef578749"
CLOBBER = "a3f6fcef2d92a1099581140c81d4264e9a4e2aa3"
GUARD = "tools/harness/receipt_guard.py"
RUNNERS = [f"reports/round-{number}/run-validation.py" for number in range(8, 12)]
RECEIPTS = [f"reports/round-{number}/validation.json" for number in range(8, 12)]


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(args, *, cwd=ROOT, env=None, timeout=240):
    started = now()
    result = subprocess.run(args, cwd=cwd, env=env, capture_output=True,
                            text=True, timeout=timeout)
    return {"command": shlex.join([str(arg) for arg in args]),
            "cwd": str(cwd), "started_at_utc": started,
            "finished_at_utc": now(), "exit": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr}


def blob(revision, path):
    args = ["git", "show", f"{revision}:{path}"]
    started = now()
    data = subprocess.check_output(args, cwd=ROOT)
    return data, {"command": shlex.join(args), "date_utc": started,
                  "sha256": sha(data)}


def live_hashes():
    return {path: sha((ROOT / path).read_bytes()) for path in RUNNERS + RECEIPTS}


def runner_checks():
    checks = [run(["git", "diff", "--exit-code", BASELINE, "--", *RUNNERS]),
              run(["git", "diff", "--cached", "--exit-code", BASELINE,
                   "--", *RUNNERS]),
              run(["git", "diff", "--exit-code", "HEAD", "--", *RUNNERS]),
              run(["git", "status", "--porcelain", "--", *RUNNERS])]
    pins = []
    for path in RUNNERS:
        data, evidence = blob(BASELINE, path)
        pins.append({"path": path, "baseline": evidence,
                     "live_sha256": sha((ROOT / path).read_bytes()),
                     "passed": data == (ROOT / path).read_bytes()})
    return {"commands": checks, "runner_pins": pins,
            "passed": all(check["exit"] == 0 and not check["stdout"]
                          and not check["stderr"] for check in checks)
            and all(pin["passed"] for pin in pins)}


def replay(number, revision, temporary, guard_bytes):
    clone = temporary / f"round-{number}"
    setup = [run(["git", "-c", "core.hooksPath=/dev/null", "clone",
                  "--no-hardlinks", "--no-checkout", "--quiet", str(ROOT), str(clone)]),
             run(["git", "-c", "core.hooksPath=/dev/null", "checkout",
                  "--quiet", "--detach", revision], cwd=clone)]
    if any(command["exit"] for command in setup):
        return {"round": number, "setup": setup, "passed": False}
    head = run(["git", "rev-parse", "HEAD"], cwd=clone)
    setup.append(head)
    receipt_rel = f"reports/round-{number}/validation.json"
    runner_rel = f"reports/round-{number}/run-validation.py"
    receipt = clone / receipt_rel
    runner = clone / runner_rel
    original = receipt.read_bytes()
    original_runner = runner.read_bytes()
    committed = run(["git", "ls-tree", "--full-tree", "HEAD", "--", receipt_rel], cwd=clone)
    guard = clone / GUARD
    guard.write_bytes(guard_bytes)
    scratch = clone / ".scratch"
    scratch.mkdir(exist_ok=True)
    env = dict(os.environ, TMPDIR=str(scratch), PYTHONDONTWRITEBYTECODE="1")
    env.pop("REFRESH_RECEIPTS", None)
    marker = scratch / "runner-entered"
    callback = (
        "from pathlib import Path\n"
        "import runpy, sys\n"
        "from tools.harness.receipt_guard import round_runner_main\n"
        "def runner():\n"
        "    Path('.scratch/runner-entered').write_text('entered\\n', encoding='utf-8')\n"
        f"    runpy.run_path(str(Path({runner_rel!r}).resolve()), run_name='__main__')\n"
        "    return 0\n"
        f"sys.exit(round_runner_main(runner, {receipt_rel!r}, repo_root=Path.cwd()))\n"
    )
    callback_command = [sys.executable, "-c", callback]
    controls = []

    cli = run([sys.executable, GUARD, "--repo-root", str(clone), receipt_rel],
              cwd=clone, env=env)
    controls.append({"id": f"R{number}-cli-refuses-committed", "execution": cli,
                     "before_sha256": sha(original), "after_sha256": sha(receipt.read_bytes()),
                     "passed": cli["exit"] == 3
                     and "RECEIPT-GUARD-COMMITTED" in cli["stderr"]
                     and receipt_rel in cli["stderr"] and receipt.read_bytes() == original})

    blocked = run(callback_command, cwd=clone, env=env)
    controls.append({"id": f"R{number}-actual-runner-blocked-before-effects",
                     "execution": blocked, "callback_entered": marker.exists(),
                     "before_sha256": sha(original), "after_sha256": sha(receipt.read_bytes()),
                     "passed": blocked["exit"] == 3
                     and "RECEIPT-GUARD-COMMITTED" in blocked["stderr"]
                     and receipt_rel in blocked["stderr"]
                     and not marker.exists() and receipt.read_bytes() == original})

    unguarded = run([sys.executable, runner_rel], cwd=clone, env=env)
    unguarded_bytes = receipt.read_bytes()
    controls.append({"id": f"R{number}-unguarded-real-runner-clobbers-control",
                     "execution": unguarded, "before_sha256": sha(original),
                     "after_sha256": sha(unguarded_bytes),
                     "acceptance_before": json.loads(original)["acceptance_checks_passed"],
                     "acceptance_after": json.loads(unguarded_bytes)["acceptance_checks_passed"],
                     "passed": unguarded["exit"] in (0, 1) and unguarded_bytes != original
                     and "Traceback" not in unguarded["stderr"]})
    receipt.write_bytes(original)

    refresh_env = dict(env, REFRESH_RECEIPTS="1")
    refreshed = run(callback_command, cwd=clone, env=refresh_env)
    refreshed_bytes = receipt.read_bytes()
    controls.append({"id": f"R{number}-explicit-refresh-allows-real-runner-control",
                     "execution": refreshed, "environment": {"REFRESH_RECEIPTS": "1"},
                     "callback_entered": marker.exists(),
                     "before_sha256": sha(original), "after_sha256": sha(refreshed_bytes),
                     "passed": refreshed["exit"] in (0, 1)
                     and marker.exists() and refreshed_bytes != original
                     and "Traceback" not in refreshed["stderr"]})
    marker.unlink(missing_ok=True)

    dirty_blocked = run(callback_command, cwd=clone, env=env)
    controls.append({"id": f"R{number}-dirty-committed-receipt-still-protected",
                     "execution": dirty_blocked, "callback_entered": marker.exists(),
                     "before_sha256": sha(refreshed_bytes), "after_sha256": sha(receipt.read_bytes()),
                     "passed": dirty_blocked["exit"] == 3 and refreshed_bytes != original
                     and "RECEIPT-GUARD-COMMITTED" in dirty_blocked["stderr"]
                     and not marker.exists() and receipt.read_bytes() == refreshed_bytes})
    receipt.write_bytes(original)
    runner_diff = run(["git", "diff", "--exit-code", "HEAD", "--", runner_rel], cwd=clone)
    controls.append({"id": f"R{number}-scratch-filed-runner-untouched",
                     "execution": runner_diff, "before_sha256": sha(original_runner),
                     "after_sha256": sha(runner.read_bytes()),
                     "passed": runner_diff["exit"] == 0 and not runner_diff["stdout"]
                     and runner.read_bytes() == original_runner})
    return {"round": number, "revision": revision, "setup": setup,
            "committed_receipt_lookup": committed, "guard_sha256": sha(guard_bytes),
            "controls": controls, "controls_total": len(controls),
            "controls_passed": sum(control["passed"] for control in controls),
            "passed": head["exit"] == 0 and head["stdout"].strip() == revision
            and committed["exit"] == 0 and receipt_rel in committed["stdout"]
            and all(control["passed"] for control in controls)}


def main():
    started = now()
    if Path(os.environ.get("TMPDIR", "")).resolve() != SCRATCH:
        raise SystemExit('First export TMPDIR="$PWD/.scratch" from the lane root')
    SCRATCH.mkdir(exist_ok=True)
    guard_bytes = (ROOT / GUARD).read_bytes()
    before = live_hashes()
    runners_before = runner_checks()
    missing_r9 = run(["git", "ls-tree", "-r", "--name-only", R8, "--",
                      "reports/round-9"])
    history = []
    for number, revision in ((8, R8), (9, R9)):
        path = f"reports/round-{number}/validation.json"
        filed, filed_evidence = blob(revision, path)
        clobbered, clobber_evidence = blob(CLOBBER, path)
        history.append({"round": number, "path": path, "filed_revision": revision,
                        "filed": filed_evidence, "clobber_revision": CLOBBER,
                        "clobbered": clobber_evidence,
                        "filed_acceptance_checks_passed": json.loads(filed)["acceptance_checks_passed"],
                        "clobbered_acceptance_checks_passed": json.loads(clobbered)["acceptance_checks_passed"],
                        "historical_bytes_differ": filed != clobbered})
    with tempfile.TemporaryDirectory(prefix="r14-retro-tests-", dir=SCRATCH) as directory:
        temporary = Path(directory)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(replay, number, revision, temporary, guard_bytes)
                       for number, revision in ((8, R8), (9, R9))]
            cases = [future.result() for future in futures]
    runners_after = runner_checks()
    after = live_hashes()
    source_unchanged = (ROOT / GUARD).read_bytes() == guard_bytes
    passed = (runners_before["passed"] and runners_after["passed"] and before == after
              and source_unchanged and missing_r9["exit"] == 0 and not missing_r9["stdout"]
              and all(row["historical_bytes_differ"] for row in history)
              and all(case["passed"] for case in cases))
    receipt = {
        "assignment": "R14-D06..D07", "axis": "D / receipt-guard retro-tests",
        "command": COMMAND, "started_at_utc": started, "finished_at_utc": now(),
        "baseline_revision": BASELINE, "guard_sha256": sha(guard_bytes),
        "guard_source_unchanged_during_test": source_unchanged,
        "historical_evidence": history,
        "round9_absent_at_required_round8_snapshot": missing_r9,
        "cases": cases,
        "controls_total": sum(case.get("controls_total", 0) for case in cases),
        "controls_passed": sum(case.get("controls_passed", 0) for case in cases),
        "D07_runners_before": runners_before, "D07_runners_after": runners_after,
        "main_tree_before_sha256": before, "main_tree_after_sha256": after,
        "main_tree_runners_and_receipts_unchanged": before == after,
        "passed": passed,
        "limits": [
            "Round 9 did not exist at e1694ba; its real filing snapshot 9dc18ec is used instead of fabricating a committed round-9 receipt there.",
            "The guard is copied into disposable clones and explicitly invoked around unchanged legacy runners. Filed rounds 8-11 remain unwired and can still overwrite receipts if called directly.",
            "Unguarded and explicit-refresh controls execute actual historical runners only in disposable clones; their acceptance results are replay observations, not revisions to historical admission.",
            "The main-tree preservation check covers rounds 8-11 runner and validation paths, not every concurrent worker output.",
            "This checks cooperative preflight protection, not filesystem locking or an arbitrary-writer sandbox."
        ]}
    return receipt


def publish_receipt(receipt):
    OUTPUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"receipt": str(OUTPUT.relative_to(ROOT)),
                      "controls_passed": receipt["controls_passed"],
                      "controls_total": receipt["controls_total"],
                      "passed": receipt["passed"]}, sort_keys=True))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    from tools.harness.receipt_guard import round_runner_main
    sys.exit(round_runner_main(main, OUTPUT, repo_root=ROOT,
                               write_receipt=publish_receipt))
