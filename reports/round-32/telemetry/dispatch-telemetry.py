#!/usr/bin/env python3
import argparse
import copy
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[3]
BASE = Path("reports/round-32/telemetry")
SNAPSHOT = BASE / "dispatch-stats.json"
COMMAND = "python3 reports/round-32/telemetry/dispatch-telemetry.py --capture"
INPUTS = {
    "declared_request": BASE / "inputs/claims.json",
    "declared_allocation": BASE / "inputs/targets.json",
    "worker_observation": BASE / "worker-observation.json",
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def derived(root):
    claims = read_json(root / INPUTS["declared_request"])
    targets = read_json(root / INPUTS["declared_allocation"])
    observation = read_json(root / INPUTS["worker_observation"])
    if claims["round"] != 32 or targets["round"] != 32 or observation["round"] != 32:
        raise ValueError("round-mismatch")
    if type(claims["workers"]) is not int or claims["workers"] <= 0:
        raise ValueError("invalid-requested-workers")
    allocation = targets["workers"]
    if not allocation or any(type(n) is not int or n <= 0 for n in allocation.values()):
        raise ValueError("invalid-worker-allocation")
    if sum(allocation.values()) != claims["workers"]:
        raise ValueError("request-allocation-mismatch")
    sessions = observation["sessions"]
    assignments = [session["assignment"] for session in sessions]
    if not assignments or len(set(assignments)) != len(assignments):
        raise ValueError("invalid-observed-sessions")
    if any(session["state_at_observation"] != "active" for session in sessions):
        raise ValueError("unexpected-worker-state")
    return {
        "requested_workers": claims["workers"],
        "requested_workers_by_group": allocation,
        "requested_model": claims["requested_model"],
        "observed_worker_sessions_lower_bound": len(sessions),
        "observed_active_sessions": len(sessions),
        "launched_workers": None,
        "completed_workers": None,
        "failed_workers": None,
        "actual_route": None,
        "runtime_concurrency": None,
        "tool_reported_wall_seconds": None,
        "http_attempts": None,
        "completion_rate": None,
    }


def capture(root):
    observation = read_json(root / INPUTS["worker_observation"])
    return {
        "round": 32,
        "kind": "dispatch-request-and-worker-observation",
        "owner": observation["owner"],
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "counts_date": date.today().isoformat(),
        "counting_command": COMMAND,
        "observation_at_utc": observation["observed_at_utc"],
        "scope": "partial-worker-observation; not a closed full-wave sample",
        "full_wave_status": "could-not-evaluate",
        "unavailable_owner": observation["unavailable_owner"],
        "unavailable_reason": observation["unavailable_reason"],
        "stats": derived(root),
        "sources": {
            key: {"path": str(path), "sha256": digest(root / path)}
            for key, path in INPUTS.items()
        },
        "limits": [
            "Requested allocation and requested model are declarations, not execution evidence.",
            "The observed session is a worker self-observation, not an independent dispatch census.",
            "Null counters are unavailable, not zero. No provider availability or round acceptance is inferred.",
            "A final-wave result must be a new snapshot backed by durable native dispatch/result extracts.",
        ],
    }


def validate(root, snapshot):
    findings = []
    try:
        agents = (root / "AGENTS.md").read_text(encoding="utf-8")
        if "reports/round-<N>/telemetry/" not in agents or "never only `.scratch`" not in agents:
            findings.append("missing-durability-convention")
        if snapshot.get("round") != 32 or snapshot.get("kind") != "dispatch-request-and-worker-observation":
            findings.append("snapshot-kind-or-round-mismatch")
        if snapshot.get("counting_command") != COMMAND:
            findings.append("counting-command-missing-or-changed")
        date.fromisoformat(snapshot["counts_date"])
        for field in ("captured_at_utc", "observation_at_utc"):
            if datetime.fromisoformat(snapshot[field]).utcoffset() is None:
                findings.append(f"{field}-missing-timezone")
        if snapshot.get("full_wave_status") != "could-not-evaluate":
            findings.append("full-wave-evidence-overclaim")
        if snapshot.get("scope") != "partial-worker-observation; not a closed full-wave sample":
            findings.append("partial-scope-missing")
        for field in ("owner", "unavailable_owner", "unavailable_reason", "limits"):
            if not snapshot.get(field):
                findings.append(f"missing-{field}")
        sources = snapshot["sources"]
        if set(sources) != set(INPUTS):
            findings.append("source-set-mismatch")
        for key, relative in INPUTS.items():
            source = sources.get(key, {})
            if source.get("path") != str(relative):
                findings.append(f"non-durable-or-wrong-source:{key}")
                continue
            path = root / relative
            if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to((root / BASE).resolve()):
                findings.append(f"missing-or-escaping-source:{key}")
            elif digest(path) != source.get("sha256"):
                findings.append(f"source-digest-mismatch:{key}")
        if snapshot["stats"] != derived(root):
            findings.append("stats-not-reproduced-from-durable-evidence")
        observation = read_json(root / INPUTS["worker_observation"])
        if snapshot["observation_at_utc"] != observation["observed_at_utc"]:
            findings.append("observation-time-mismatch")
    except (OSError, ValueError, KeyError, TypeError) as error:
        findings.append(f"could-not-evaluate:{type(error).__name__}:{error}")
    return findings


def selftest(root, snapshot):
    controls = []

    def record(name, passed, findings):
        controls.append({"name": name, "passed": passed, "findings": findings})

    findings = validate(root, snapshot)
    record("durable-live-snapshot", not findings, findings)
    with tempfile.TemporaryDirectory(prefix="r32-telemetry-control-") as temporary:
        mirror = Path(temporary)
        shutil.copytree(root / BASE, mirror / BASE)
        shutil.copy2(root / "AGENTS.md", mirror / "AGENTS.md")
        scratch = mirror / ".scratch"
        scratch.mkdir()
        (scratch / "ephemeral-sample.json").write_text("{}\n", encoding="utf-8")
        shutil.rmtree(scratch)
        findings = validate(mirror, snapshot)
        record("durable-replay-after-scratch-removal", not findings, findings)

        changed = copy.deepcopy(snapshot)
        changed["sources"]["declared_request"]["path"] = ".scratch/claims.json"
        findings = validate(mirror, changed)
        record("scratch-only-source-rejected", "non-durable-or-wrong-source:declared_request" in findings, findings)

        path = mirror / INPUTS["worker_observation"]
        original = path.read_bytes()
        path.unlink()
        findings = validate(mirror, snapshot)
        record("missing-raw-evidence-rejected", "missing-or-escaping-source:worker_observation" in findings, findings)
        path.write_bytes(original + b" \n")
        findings = validate(mirror, snapshot)
        record("raw-byte-tamper-rejected", "source-digest-mismatch:worker_observation" in findings, findings)
        path.write_bytes(original)

        changed = copy.deepcopy(snapshot)
        changed["stats"]["completed_workers"] = changed["stats"]["requested_workers"]
        findings = validate(mirror, changed)
        record("requested-is-not-completed", "stats-not-reproduced-from-durable-evidence" in findings, findings)

        changed = copy.deepcopy(snapshot)
        changed["counting_command"] = ""
        findings = validate(mirror, changed)
        record("missing-counting-command-rejected", "counting-command-missing-or-changed" in findings, findings)

        changed = copy.deepcopy(snapshot)
        changed.pop("counts_date")
        findings = validate(mirror, changed)
        record("missing-count-date-rejected", any(x.startswith("could-not-evaluate:") for x in findings), findings)

        changed = copy.deepcopy(snapshot)
        changed["full_wave_status"] = "passed"
        findings = validate(mirror, changed)
        record("unsupported-full-wave-pass-rejected", "full-wave-evidence-overclaim" in findings, findings)

        (mirror / "AGENTS.md").write_text("# No telemetry convention\n", encoding="utf-8")
        findings = validate(mirror, snapshot)
        record("missing-operating-rule-rejected", "missing-durability-convention" in findings, findings)

    return {
        "round": 32,
        "counts_date": date.today().isoformat(),
        "counting_command": "python3 reports/round-32/telemetry/dispatch-telemetry.py --selftest",
        "controls": controls,
        "passed_controls": sum(row["passed"] for row in controls),
        "total_controls": len(controls),
        "passed": all(row["passed"] for row in controls),
    }


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--capture", action="store_true")
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.capture:
        result = capture(ROOT)
    else:
        snapshot = read_json(ROOT / SNAPSHOT)
        if args.selftest:
            result = selftest(ROOT, snapshot)
        else:
            findings = validate(ROOT, snapshot)
            result = {
                "round": 32,
                "counts_date": date.today().isoformat(),
                "counting_command": "python3 reports/round-32/telemetry/dispatch-telemetry.py --check",
                "passed": not findings,
                "findings": findings,
                "full_wave_status": snapshot["full_wave_status"],
            }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("passed", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
