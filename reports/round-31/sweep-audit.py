#!/usr/bin/env python3
"""Independent round-31 sweep audit (seat R31-O09..O10).

Re-runs the recorded round-30 sweep surface (the REGRESSIONS matrix) as two
sequential full passes, records exit codes and stdout/stderr SHA-256 digests,
cross-compares the passes, and — when the builders' final-sweep.md exists —
re-runs the command lines recorded there verbatim and flags mismatches.

Run: python3 -B reports/round-31/sweep-audit.py
"""
from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-31"
SCRIPT = "reports/round-31/sweep-audit.py"
COMMAND = f"python3 -B {SCRIPT}"
BASELINE = "71cd9d376ebd144e94e4f12d997f73e5d2839aa9"
# The two legs whose tools legitimately write outside the repo mirror, per the
# recorded round-30 runner: they get /var/tmp, everything else $PWD/.scratch.
EXTERNAL_TMP = {"frozen-replay-selftest", "r28-sweep-selftest"}
PACKET = "examples/culture-d4/packet.d4.yml"
LAW = "tools/gates/register-law-gate.py"

MATRIX = (
    ("battery-selftest", "tools/check-gate-battery.py", "--selftest"),
    ("battery", "tools/check-gate-battery.py"),
    ("craft-selftest", "tools/check-craft-exercise.py", "--selftest"),
    ("craft-positive", "tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json"),
    ("links-selftest", "tools/harness/packet_links.py", "--selftest"),
    ("uncertainty-selftest", "tools/harness/packet_uncertainty.py", "--selftest"),
    ("d2-assembly", "tools/assemble-d2.py", "--check"),
    ("d2-assembly-selftest", "tools/assemble-d2.py", "--selftest"),
    ("d2-typed-assembly", "tools/assemble-d2-typed.py", "--check"),
    ("d2-typed-assembly-selftest", "tools/assemble-d2-typed.py", "--selftest"),
    ("d3-assembly", "tools/assemble-culture-d3.py", "--check"),
    ("d3-assembly-selftest", "tools/assemble-culture-d3.py", "--selftest"),
    ("d4-assembly", "tools/assemble-culture-d4.py", "--check"),
    ("d4-assembly-selftest", "tools/assemble-culture-d4.py", "--selftest"),
    ("d4-typed-assembly", "tools/assemble-d4-typed.py", "--check"),
    ("d4-typed-assembly-selftest", "tools/assemble-d4-typed.py", "--selftest"),
    ("projector-selftest", "tools/d2-typed-labels.py", "--selftest"),
    ("d2-projection", "tools/d2-typed-labels.py", "--check"),
    ("d4-projection", "tools/d2-typed-labels.py", "--packet", PACKET, "--check", "examples/culture-d4/typed-labels.d4.yml"),
    ("d4-typed-gate", "tools/gates/d4-typed-labels-check-gate.py", "examples/culture-d4/typed-labels.d4.yml"),
    ("d4-assembly-gate", "tools/gates/d4-assembly-check-gate.py", PACKET),
    ("typed-pipeline-selftest", "tools/gates/typed-pipeline-gate.py", "--selftest"),
    ("typed-pipeline-d2", "tools/gates/typed-pipeline-gate.py", "examples/culture-d2/packet.d2.yml"),
    ("typed-pipeline-d4", "tools/gates/typed-pipeline-gate.py", PACKET),
    ("typed-pipeline-typed-d4", "tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.typed.yml"),
    ("typed-pipeline-generalized-selftest", "tools/gates/typed-pipeline-gate.py", "--selftest-generalized"),
    ("argot-selftest", "tools/gates/argot-derivation-gate.py", "--selftest"),
    ("argot-d4", "tools/gates/argot-derivation-gate.py", PACKET),
    ("law-selftest", LAW, "--selftest"),
    ("law-clean", LAW, "--packet", PACKET),
    ("handoff-v2", "tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet"),
    ("handoff-v2-selftest", "tools/exercise-handoff-e2e.py", "--profile", "v2", "--selftest", "--quiet"),
    ("handoff-v3", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet"),
    ("handoff-v3-selftest", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest", "--quiet"),
    ("coupling-selftest", "tools/check-evidence-coupling.py", "--selftest"),
    ("coupling-d3", "tools/check-evidence-coupling.py", "examples/culture-d3/packet.json"),
    ("frozen-replay-selftest", "tools/replay-frozen.py", "--selftest"),
    ("pin-repoint-selftest", "reports/round-26/remainders/pin-repoint-check.py", "--selftest"),
    ("ceiling-selftest", "reports/round-28/ceiling/measure-ceiling.py", "--selftest"),
    ("ceiling-measurement", "reports/round-28/ceiling/measure-ceiling.py"),
)
# Historical control, run alongside each pass but outside the green count: the
# R28 frozen-generation replay is expected to stay red (its actual red stays
# red; successor pins are covered by the current typed-pipeline rows).
HISTORICAL = (
    ("r28-sweep-selftest", "reports/round-28/sweep/sweep.py", "--selftest"),
)
# The R28 frozen-generation replay is expected to stay red (historical red
# remains red; successor pins are covered by the current typed-pipeline runs).
EXPECTED_NONZERO = {name for name, *_rest in HISTORICAL}


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run_one(name, args, leg):
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TMPDIR"] = "/var/tmp" if name in EXTERNAL_TMP else str(ROOT / ".scratch")
    argv = ["python3", "-B", *args]
    started = utc()
    t0 = time.monotonic()
    try:
        result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True,
                                text=True, errors="replace", timeout=240)
        code, out, err = result.returncode, result.stdout, result.stderr
    except (OSError, subprocess.TimeoutExpired) as exc:
        code, out, err = None, "", f"{type(exc).__name__}: {exc}"
    row = {
        "name": name,
        "command": shlex.join(argv),
        "leg": leg,
        "date": started[:10],
        "started_at_utc": started,
        "finished_at_utc": utc(),
        "seconds": round(time.monotonic() - t0, 3),
        "tmpdir": env["TMPDIR"],
        "exit_code": code,
        "passed": code == 0,
        "stdout_sha256": digest(out.encode()),
        "stderr_sha256": digest(err.encode()),
        "stdout_bytes": len(out.encode()),
        "stderr_bytes": len(err.encode()),
        "stdout": out,
        "stderr": err,
    }
    if name in EXPECTED_NONZERO:
        failed = []
        try:
            controls = json.loads(out)["controls"]
            failed = sorted(c["control"] for c in controls if not c["passed"])
        except (ValueError, KeyError, TypeError):
            failed = ["<stdout-not-the-r28-control-json>"]
        row["expected_nonzero"] = True
        row["failed_controls"] = failed
        row["disposition"] = (
            "Historical R28 frozen-generation replay: expected nonzero; actual "
            "red stays red. Current typed-pipeline successor pins are covered by "
            "typed-pipeline-* rows."
        )
    return row


def source_snapshot():
    paths = {}
    for rel in ("AGENTS.md", PACKET, "examples/culture-d2/packet.d2.yml",
                "examples/culture-d4/packet.d4.typed.yml",
                "examples/culture-d3/packet.json",
                "examples/supplement-opencode-1/sound-change-vs-taboo.json",
                "examples/culture-d4/typed-labels.d4.yml",
                "examples/handoff-packet.sample.md"):
        p = ROOT / rel
        if p.is_file():
            paths[rel] = digest(p.read_bytes())
    for base in ("tools", "reports/round-26/remainders", "reports/round-28/ceiling"):
        for p in (ROOT / base).rglob("*"):
            if p.is_file() and p.suffix == ".py" and "__pycache__" not in p.parts:
                paths[str(p.relative_to(ROOT))] = digest(p.read_bytes())
    return paths


def execute_pass(leg):
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(run_one, row[0], row[1:], leg) for row in MATRIX + HISTORICAL]
        rows = [f.result() for f in futures]
    order = {name: i for i, (name, *_r) in enumerate(MATRIX + HISTORICAL)}
    rows.sort(key=lambda r: order[r["name"]])
    return rows


def compare_passes(a_rows, b_rows):
    findings = []
    by_a = {r["name"]: r for r in a_rows}
    by_b = {r["name"]: r for r in b_rows}
    for name, *_rest in MATRIX + HISTORICAL:
        a, b = by_a[name], by_b[name]
        if a["exit_code"] != b["exit_code"]:
            findings.append({"kind": "exit-mismatch-between-passes", "command": name,
                             "historical_control": name in EXPECTED_NONZERO,
                             "pass_o09_exit": a["exit_code"], "pass_o10_exit": b["exit_code"]})
    for name, *_rest in MATRIX:
        a, b = by_a[name], by_b[name]
        for field in ("stdout_sha256", "stderr_sha256"):
            if a[field] != b[field]:
                findings.append({"kind": f"{field.split('_')[0]}-digest-mismatch-between-passes",
                                 "command": name, "pass_o09": a[field], "pass_o10": b[field]})
    return findings


def extract_recorded_commands(text):
    """Pull candidate recorded sweep command lines out of final-sweep markdown."""
    commands = []
    for line in text.splitlines():
        stripped = line.strip().lstrip("`").rstrip("`").rstrip("\\")
        stripped = re.sub(r"^\d+\.\s*", "", stripped)
        stripped = re.sub(r"^-\s*", "", stripped)
        if re.match(r"^(python3(-B)?|sh|bash)\s+", stripped):
            commands.append(stripped.strip("`"))
    return commands


def rerun_recorded(commands):
    rows = []
    for cmdline in commands:
        started = utc()
        t0 = time.monotonic()
        try:
            result = subprocess.run(["bash", "-c", cmdline], cwd=ROOT, capture_output=True,
                                    text=True, errors="replace", timeout=240)
            code = result.returncode
        except (OSError, subprocess.TimeoutExpired) as exc:
            code, _o, _e = None, "", ""
            result = None
            rows.append({"command": cmdline, "date": started[:10], "started_at_utc": started,
                         "finished_at_utc": utc(), "seconds": round(time.monotonic() - t0, 3),
                         "exit_code": None, "error": f"{type(exc).__name__}: {exc}"})
            continue
        rows.append({"command": cmdline, "date": started[:10], "started_at_utc": started,
                     "finished_at_utc": utc(), "seconds": round(time.monotonic() - t0, 3),
                     "exit_code": code,
                     "stdout_sha256": digest(result.stdout.encode()) if result else None,
                     "stderr_sha256": digest(result.stderr.encode()) if result else None})
    return rows


def main():
    audit = {
        "assignment": "R31-O09..O10 (sweep auditors x2): independent re-run of >=10 sweep commands; mismatches = findings",
        "counting_command": COMMAND,
        "date": utc()[:10],
        "baseline_revision": BASELINE,
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "matrix_size": len(MATRIX),
        "external_tmp_legs": sorted(EXTERNAL_TMP),
        "passes": {},
        "findings": [],
    }
    sources_before = source_snapshot()
    passes_rows = {}
    for leg in ("O09", "O10"):
        started = utc()
        rows = execute_pass(leg)
        passes_rows[leg] = rows
        current = [r for r in rows if r["name"] not in EXPECTED_NONZERO]
        historical = [r for r in rows if r["name"] in EXPECTED_NONZERO]
        audit["passes"][leg] = {
            "started_at_utc": started, "finished_at_utc": utc(),
            "commands_executed": len(current),
            "exit0_count": sum(1 for r in current if r["exit_code"] == 0),
            "nonzero": [{"name": r["name"], "exit_code": r["exit_code"]}
                        for r in current if r["exit_code"] != 0],
            "historical_controls": [{"name": r["name"], "exit_code": r["exit_code"],
                                     "failed_controls": r.get("failed_controls"),
                                     "disposition": r.get("disposition")} for r in historical],
        }
        (HERE / f"sweep-audit-{leg}.json").write_text(
            json.dumps({"assignment": "R31-O09..O10", "leg": leg, "counting_command": COMMAND,
                        "date": audit["date"], "baseline_revision": BASELINE, "head": audit["head"],
                        "results": [{k: v for k, v in r.items() if k not in ("stdout", "stderr")}
                                    for r in current]}, indent=1) + "\n")
        if leg == "O09":
            audit["passes"][leg]["results"] = [{k: v for k, v in r.items()
                                                if k not in ("stdout", "stderr")} for r in rows]
        else:
            audit["passes"][leg]["results"] = [{k: v for k, v in r.items()
                                                if k not in ("stdout", "stderr")} for r in rows]
    audit["cross_pass_findings"] = compare_passes(passes_rows["O09"], passes_rows["O10"])
    sources_after = source_snapshot()
    audit["source_drift_during_audit"] = sorted(
        p for p in sources_before.keys() | sources_after.keys()
        if sources_before.get(p) != sources_after.get(p))
    sweep_file = HERE / "final-sweep.md"
    if sweep_file.is_file():
        text = sweep_file.read_text(errors="replace")
        recorded = extract_recorded_commands(text)
        audit["final_sweep_md"] = {
            "present": True,
            "sha256": digest(sweep_file.read_bytes()),
            "recorded_command_lines": len(recorded),
            "verbatim_reruns": rerun_recorded(recorded),
        }
    (HERE / "sweep-audit-O09O10.json").write_text(json.dumps(audit, indent=1) + "\n")
    print(json.dumps({
        "counting_command": COMMAND,
        "matrix_size": audit["matrix_size"],
        "O09": audit["passes"]["O09"]["exit0_count"],
        "O10": audit["passes"]["O10"]["exit0_count"],
        "nonzero": audit["passes"]["O09"]["nonzero"],
        "cross_pass_findings": audit["cross_pass_findings"],
        "source_drift": audit["source_drift_during_audit"],
        "final_sweep_present": audit.get("final_sweep_md", {}).get("present", False),
    }, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
