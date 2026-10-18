#!/usr/bin/env python3
import argparse
import copy
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COMMAND = "python3 -B reports/round-30/telemetry/check-dispatch.py"
SOURCE_PATHS = (
    "reports/round-30/claims.json",
    "reports/round-30/targets.json",
)
RUNTIME_UNKNOWN = (
    "host_dispatch_receipt", "host_completion_receipt", "launched_workers",
    "completed_workers", "failed_workers", "cancelled_workers",
    "dispatch_attempts", "retries", "provider_substitutions",
    "max_concurrent_workers", "wall_s", "prompt_tokens", "completion_tokens",
    "served_provider", "served_model", "served_effort",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(record):
    require(record["round"] == 30, "wrong round")
    date.fromisoformat(record["date"])
    date.fromisoformat(record["counts_date"])
    timestamp = datetime.fromisoformat(record["observed_at_utc"])
    require(timestamp.utcoffset() is not None, "observation needs a timezone")
    require(timestamp.date().isoformat() == record["counts_date"], "observation/count date mismatch")
    require(record["counting_command"] == COMMAND, "missing reproducible counting command")
    require(record["control_command"] == COMMAND + " --selftest", "missing control command")
    require(record["seat"] == record["owner"] == "R30-X37", "wrong reporting seat/owner")
    require(record["lane"] == "kotodama-shokunin", "wrong lane")
    require(record["state"] == "declaration-snapshot-runtime-could-not-evaluate", "scope was promoted")
    require(record["durability"]["directory"] == str(HERE.relative_to(ROOT)) + "/", "wrong durable directory")
    require(record["durability"]["scratch_dependencies"] == [], "scratch-only telemetry dependency")
    require(record["durability"]["historical_recovery_claimed"] is False, "historical telemetry was not recovered")
    require(len(record["raw_evidence"]) == len(SOURCE_PATHS), "raw evidence population changed")
    sources = {}
    for evidence in record["raw_evidence"]:
        relative = evidence["path"]
        require(relative in SOURCE_PATHS, "non-durable or unexpected evidence path")
        require(relative not in sources, "duplicate evidence path")
        path = ROOT / relative
        require(path.resolve().is_relative_to(ROOT), "evidence escapes lane")
        raw = path.read_bytes()
        require(len(raw) == evidence["bytes"], "raw evidence size mismatch")
        require(hashlib.sha256(raw).hexdigest() == evidence["sha256"], "raw evidence hash mismatch")
        sources[relative] = json.loads(raw)
    claims, targets = (sources[path] for path in SOURCE_PATHS)
    require(claims["round"] == targets["round"] == record["round"], "source round mismatch")
    require(claims["date"] == targets["date"] == record["date"], "declaration date mismatch")
    require(claims["baseline_revision"] == targets["baseline_revision"] == record["baseline_revision"], "baseline mismatch")
    require(claims["state"] == record["declaration_state"] == "declared-before-dispatch", "declaration is not an observation")
    require(claims["requested_model"] == record["requested_model"], "requested model mismatch")
    require(record["requested_model"] == f"{record['requested_provider']}/{record['requested_model_id']} ({record['requested_effort']} effort)", "requested route/effort mismatch")
    allocations = targets["workers"]
    require(all(type(value) is int and value >= 0 for value in allocations.values()), "invalid allocation")
    require(record["worker_allocations"] == allocations, "worker allocation mismatch")
    total = sum(allocations.values())
    require(type(record["requested_workers"]) is int, "requested worker count is not an integer")
    require(type(record["allocation_total"]) is int, "allocation total is not an integer")
    require(record["requested_workers"] == record["allocation_total"] == claims["workers"] == total, "requested/allocation count mismatch")
    runtime = record["runtime"]
    require(runtime["status"] == "could-not-evaluate", "runtime status was promoted")
    require(bool(runtime["owner"]) and bool(runtime["basis"]) and bool(runtime["follow_up"]), "runtime gap lacks disposition")
    for key in RUNTIME_UNKNOWN:
        require(key in runtime and runtime[key] is None, f"unsupported runtime measurement: {key}")
    for relative in SOURCE_PATHS + (
        str((HERE / "dispatch-declaration-x37.json").relative_to(ROOT)),
        str(Path(__file__).resolve().relative_to(ROOT)),
        str((HERE / "control-receipt.json").relative_to(ROOT)),
    ):
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-q", "--", relative],
            cwd=ROOT, capture_output=True, text=True,
        )
        require(result.returncode == 1, f"telemetry evidence ignored or check failed: {relative}")
    return {
        "requested_model": record["requested_model"],
        "requested_workers": total,
        "worker_allocations": allocations,
        "allocation_total": total,
        "runtime_status": runtime["status"],
        "launched_workers": runtime["launched_workers"],
        "completed_workers": runtime["completed_workers"],
        "raw_evidence_paths": list(SOURCE_PATHS),
        "scratch_dependencies": record["durability"]["scratch_dependencies"],
    }


def selftest(record):
    mutations = {
        "declared_count_inflation": lambda r: r.update(requested_workers=33),
        "allocation_drift": lambda r: r["worker_allocations"].update({"O-routed": 13}),
        "invented_completion_count": lambda r: r["runtime"].update(completed_workers=32),
        "invented_served_model": lambda r: r["runtime"].update(served_model="gpt-6.1-sol"),
        "null_to_zero": lambda r: r["runtime"].update(failed_workers=0),
        "scratch_only_dependency": lambda r: r["durability"].update(scratch_dependencies=[".scratch/dispatch.json"]),
        "scratch_evidence_path": lambda r: r["raw_evidence"][0].update(path=".scratch/claims.json"),
        "raw_evidence_tamper": lambda r: r["raw_evidence"][0].update(sha256="0" * 64),
        "duplicate_evidence": lambda r: r["raw_evidence"].__setitem__(1, copy.deepcopy(r["raw_evidence"][0])),
        "runtime_promoted_to_pass": lambda r: r["runtime"].update(status="passed"),
        "historical_recovery_overclaim": lambda r: r["durability"].update(historical_recovery_claimed=True),
    }
    outcomes = []
    for name, mutate in mutations.items():
        candidate = copy.deepcopy(record)
        mutate(candidate)
        try:
            check(candidate)
        except ValueError as error:
            outcomes.append({"control": name, "rejected": True, "finding": str(error)})
        else:
            raise ValueError(f"negative control accepted: {name}")
    return outcomes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    record = json.loads((HERE / "dispatch-declaration-x37.json").read_text())
    summary = check(record)
    command = COMMAND + (" --selftest" if args.selftest else "")
    receipt = {
        "round": 30,
        "date": datetime.now(timezone.utc).date().isoformat(),
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": command,
        "status": "passed",
        "scope": "Durable declaration telemetry and fail-closed controls only; runtime remains could-not-evaluate.",
        "summary": summary,
    }
    if args.selftest:
        receipt["negative_controls"] = selftest(record)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
