#!/usr/bin/env python3
"""Independent round-32 sweep audit (seat R32-O09..O10).

Re-runs the recorded round-31 final-sweep surface — the 50 green-surface
commands plus the 13 filed-red historical controls, read row-for-row from the
filed round-31 receipt — as two sequential full passes. Records per command:
argv, timestamps, seconds, tmpdir, exit code, SHA-256 of stdout and stderr.
Cross-compares the two passes, cross-checks the filed round-31 receipt, and —
when the round-32 builders' sweep artifacts exist — cross-checks against those
too.

Run: python3 -B reports/round-32/sweep-audit.py

Writes only its own three files (sweep-audit-O09.json, sweep-audit-O10.json,
sweep-audit-O09O10.json). The round-32 builders' artifacts (sweep receipt,
final-sweep.md) and the orchestrator-owned round runner (run-validation.py)
are read-only inputs here; the runner is never executed by this audit.
"""
from __future__ import annotations

import concurrent.futures
import datetime as dt
import difflib
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
HERE = ROOT / "reports/round-32"
SCRIPT = "reports/round-32/sweep-audit.py"
COMMAND = f"python3 -B {SCRIPT}"
BASELINE = "17e90b9047b289d7a63180a1dc1bebb074137e29"
R31_RECEIPT = ROOT / "reports/round-31/sweep/sweep-receipt.json"
R31_FINAL_SWEEP_MD = ROOT / "reports/round-31/final-sweep.md"
R32_RECEIPT = ROOT / "reports/round-32/sweep/sweep-receipt.json"
R32_FINAL_SWEEP_MD = ROOT / "reports/round-32/final-sweep.md"
R32_VALIDATION = ROOT / "reports/round-32/run-validation.py"
EXTERNAL_TMP = "/var/tmp/kotodama-r32-sweepaudit"
SCRATCH_TMP = str(ROOT / ".scratch")
TIMEOUT_S = 240
MAX_WORKERS = 8
# Rows whose stdout legitimately embeds run stamps (r31 audit findings F1/F2;
# the round validators' NONDETERMINISTIC_STDOUT whitelist, keyed by row id):
# cross-pass and cross-receipt comparisons are exit-only for these rows, and a
# digest mismatch on them is recorded as expected-volatile, not a finding.
VOLATILE_ROWS = {"battery", "pin-repoint-selftest"}
# Mirror-safety replay legs (r31 sweep §4): the replay tool refuses a mirror
# inside the repo, so every replay-frozen invocation gets the external tmpdir.
REPLAY_TOOLS = {"tools/replay-frozen.py"}
# The 13 filed-red control codes as recorded in the filed r31 final-sweep.md
# §3 table (order = that table's order); cross-checked against the receipt at
# load time so a receipt/table disagreement is itself a finding.
FILED_CONTROL_CODES = {
    "control-round-3": 2,
    "control-round-3-attempt-1": 2,
    "control-round-11": 2,
    "control-round-18": 1,
    "control-round-18-repin-d2": 2,
    "control-round-20-repin-d2": 2,
    "control-round-22-d4-repin": 2,
    "control-round-23-repin-d2": 2,
    "control-round-25-gate-input": 2,
    "control-round-26-gate-input": 1,
    "control-round-26-post-register": 1,
    "control-r27-post": 1,
    "control-r28-post": 1,
}
# Runtime inputs of the audited surface: hashed before and after the passes.
SNAPSHOT_BASES = (
    "tools",
    "examples",
    "corpus/knowledge",
    "reports/round-26/remainders",
    "reports/round-28/ceiling",
    "reports/round-31/sweep/frozen",
    "reports/round-17/tests/frozen",
)


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(path: Path) -> str | None:
    try:
        return digest(path.read_bytes())
    except OSError:
        return None


def load_matrix():
    receipt = json.loads(R31_RECEIPT.read_text())
    rows = []
    for row in receipt["rows"]:
        argv = shlex.split(row["command"])
        if argv[:2] != ["python3", "-B"]:
            raise SystemExit(f"unexpected command shape in r31 receipt: {row['command']}")
        rows.append({
            "id": row["id"],
            "argv": argv[2:],
            "tool": argv[2],
            "class": row.get("class", "sweep"),
            "expect_exit": row.get("expect_exit", 0),
        })
    controls = [r for r in rows if r["class"] == "historical-control"]
    for c in controls:
        if FILED_CONTROL_CODES[c["id"]] != c["expect_exit"]:
            raise SystemExit(
                f"receipt/final-sweep.md control-code disagreement at {c['id']}: "
                f"receipt {c['expect_exit']} vs filed table {FILED_CONTROL_CODES[c['id']]}")
    return receipt, rows


def run_one(spec, leg):
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TMPDIR"] = EXTERNAL_TMP if spec["tool"] in REPLAY_TOOLS else SCRATCH_TMP
    argv = ["python3", "-B", *spec["argv"]]
    started = utc()
    t0 = time.monotonic()
    try:
        result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True,
                                text=True, errors="replace", timeout=TIMEOUT_S)
        code, out, err = result.returncode, result.stdout, result.stderr
    except (OSError, subprocess.TimeoutExpired) as exc:
        code, out, err = None, "", f"{type(exc).__name__}: {exc}"
    return {
        "id": spec["id"],
        "command": shlex.join(argv),
        "class": spec["class"],
        "leg": leg,
        "date": started[:10],
        "started_at_utc": started,
        "finished_at_utc": utc(),
        "seconds": round(time.monotonic() - t0, 3),
        "tmpdir": env["TMPDIR"],
        "exit_code": code,
        "expect_exit": spec["expect_exit"],
        "expected_exit_matches": code == spec["expect_exit"],
        "volatile_tool": spec["id"] in VOLATILE_ROWS,
        "stdout_sha256": digest(out.encode()),
        "stderr_sha256": digest(err.encode()),
        "stdout_bytes": len(out.encode()),
        "stderr_bytes": len(err.encode()),
        "stdout_head": out[:240],
        "stderr_head": err[:240],
        "_stdout": out,
    }


def source_snapshot():
    paths = {}
    for base in SNAPSHOT_BASES:
        root = ROOT / base
        if not root.is_dir():
            continue
        for p in root.rglob("*"):
            if p.is_file() and "__pycache__" not in p.parts:
                paths[str(p.relative_to(ROOT))] = digest(p.read_bytes())
    return paths


def execute_pass(specs, leg):
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = [pool.submit(run_one, spec, leg) for spec in specs]
        rows = [f.result() for f in futures]
    order = {spec["id"]: i for i, spec in enumerate(specs)}
    rows.sort(key=lambda r: order[r["id"]])
    return rows


def row_public(row):
    return {k: v for k, v in row.items() if k != "_stdout"}


def compare_passes(rows_a, rows_b):
    findings, expected_volatility = [], []
    by_a = {r["id"]: r for r in rows_a}
    by_b = {r["id"]: r for r in rows_b}
    for r_a in rows_a:
        r_b = by_b[r_a["id"]]
        if r_a["exit_code"] != r_b["exit_code"]:
            findings.append({"kind": "exit-mismatch-between-passes", "id": r_a["id"],
                             "pass_o09_exit": r_a["exit_code"], "pass_o10_exit": r_b["exit_code"]})
        for field in ("stdout_sha256", "stderr_sha256"):
            if r_a[field] != r_b[field]:
                entry = {"kind": f"{field.split('_')[0]}-digest-mismatch-between-passes",
                         "id": r_a["id"], "volatile_tool": r_a["volatile_tool"]}
                if r_a["volatile_tool"]:
                    if field == "stdout_sha256":
                        diff = list(difflib.unified_diff(
                            r_a["_stdout"].splitlines(), r_b["_stdout"].splitlines(),
                            "o09", "o10", lineterm="", n=0))
                        entry["diff_excerpt"] = diff[:12]
                    expected_volatility.append(entry)
                else:
                    findings.append(entry)
    return findings, expected_volatility


def cross_check_receipt(rows, receipt, label):
    """Row-for-row comparison of one audit pass against a filed receipt."""
    by_cmd = {r["command"]: r for r in receipt["rows"]}
    checked, exit_mismatch, digest_mismatch, expected_volatile_mismatch = [], [], [], []
    for mine in rows:
        theirs = by_cmd.get(mine["command"])
        if theirs is None:
            checked.append({"id": mine["id"], "match": "no-receipt-row"})
            continue
        if theirs["exit_code"] != mine["exit_code"]:
            exit_mismatch.append({"id": mine["id"], "audit_exit": mine["exit_code"],
                                  "receipt_exit": theirs["exit_code"]})
        elif mine["stdout_sha256"] != theirs.get("stdout_sha256"):
            if mine["volatile_tool"]:
                expected_volatile_mismatch.append({"id": mine["id"]})
            else:
                digest_mismatch.append({
                    "id": mine["id"], "audit_sha256": mine["stdout_sha256"][:16],
                    "receipt_sha256": (theirs.get("stdout_sha256") or "")[:16]})
        else:
            checked.append({"id": mine["id"], "match": "exit+stdout-digest"})
    return {
        "receipt": label,
        "rows_compared": len(rows),
        "rows_matched": sum(1 for c in checked if c["match"] == "exit+stdout-digest"),
        "no_receipt_row": [c["id"] for c in checked if c["match"] == "no-receipt-row"],
        "exit_mismatches": exit_mismatch,
        "stdout_digest_mismatches": digest_mismatch,
        "expected_volatile_digest_only": expected_volatile_mismatch,
    }


TABLE_ROW_RE = re.compile(
    r"^\|\s*(?P<id>\S+)\s*\|\s*(?P<family>[\w-]+)\s*\|\s*`(?P<command>[^`]+)`\s*\|"
    r"\s*(?P<exit>\d+)\s*\|\s*`(?P<sha16>[0-9a-f]{16})…`\s*\|", re.MULTILINE)


def cross_check_sweep_table(rows, text):
    """Diff the builders' filed sweep table (id | family | command | exit |
    stdout sha16…) against this audit's measured rows. Read-only: nothing from
    the table is executed here; volatile rows compare exit-only."""
    by_id = {r["id"]: r for r in rows}
    matched, exit_mismatches, digest_mismatches, absent = [], [], [], []
    seen = 0
    for m in TABLE_ROW_RE.finditer(text):
        seen += 1
        mine = by_id.get(m.group("id"))
        if mine is None:
            absent.append(m.group("id"))
            continue
        if int(m.group("exit")) != mine["exit_code"]:
            exit_mismatches.append({"id": mine["id"], "table_exit": int(m.group("exit")),
                                    "audit_exit": mine["exit_code"]})
        elif not mine["volatile_tool"] and not mine["stdout_sha256"].startswith(m.group("sha16")):
            digest_mismatches.append({"id": mine["id"], "table_sha16": m.group("sha16"),
                                      "audit_sha16": mine["stdout_sha256"][:16]})
        else:
            matched.append(mine["id"])
    return {"rows_in_table": seen, "rows_matched": len(matched),
            "exit_mismatches": exit_mismatches, "stdout_digest_mismatches": digest_mismatches,
            "absent_from_audit": absent,
            "volatile_rows_exit_only": sorted(
                r["id"] for r in rows if r["volatile_tool"] and r["id"] in
                {m.group("id") for m in TABLE_ROW_RE.finditer(text)})}


def extract_recorded_commands(text):
    commands = []
    for line in text.splitlines():
        stripped = line.strip().lstrip("`").rstrip("`").rstrip("\\")
        stripped = re.sub(r"^\d+\.\s*", "", stripped)
        stripped = re.sub(r"^-\s*", "", stripped)
        if re.match(r"^(python3(-B)?|sh|bash)\s+", stripped):
            commands.append(stripped.strip("`"))
    return commands


def verbatim_rerun(cmdline):
    """Re-run a recorded command line only when it cannot write another
    seat's artifact: tree tools and filed-round readers are executed; anything
    whose target script lives under reports/round-32 (the builders'/orchestra-
    tor's files) or any freeze/runner invocation is recorded but not executed."""
    argv = None
    try:
        argv = shlex.split(cmdline)
    except ValueError as exc:
        return {"command": cmdline, "executed": False,
                "reason": f"unparseable command line ({exc}); not executed"}
    if "`" in cmdline:
        return {"command": cmdline, "executed": False,
                "reason": "prose artifact (embedded backtick), not a recorded command; not executed"}
    script = next((a for a in argv if a.endswith(".py")), "")
    executable = bool(script) and not script.startswith("reports/round-32/")
    executable = executable and "run-sweep" not in script and "freeze" not in script
    if not executable:
        return {"command": cmdline, "executed": False,
                "reason": "writes-or-may-write-a-non-audit-seat-artifact; not executed"}
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TMPDIR"] = EXTERNAL_TMP if any(a.endswith("replay-frozen.py") for a in argv) else SCRATCH_TMP
    started = utc()
    t0 = time.monotonic()
    try:
        result = subprocess.run(["bash", "-c", cmdline], cwd=ROOT, env=env,
                                capture_output=True, text=True, errors="replace",
                                timeout=TIMEOUT_S)
        code, out = result.returncode, result.stdout
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"command": cmdline, "executed": True, "date": started[:10],
                "started_at_utc": started, "finished_at_utc": utc(),
                "exit_code": None, "error": f"{type(exc).__name__}: {exc}"}
    return {"command": cmdline, "executed": True, "date": started[:10],
            "started_at_utc": started, "finished_at_utc": utc(),
            "seconds": round(time.monotonic() - t0, 3), "tmpdir": env["TMPDIR"],
            "exit_code": code, "stdout_sha256": digest(out.encode())}


def main():
    r31_receipt, specs = load_matrix()
    # Adopt rows the round-32 builders added to the recorded green surface
    # (currently the r32 validation harness selftest). Executed like any green
    # row; the orchestrator-owned full runner (`run-validation.py`, unflagged)
    # is still never executed by this audit.
    r32_receipt = None
    adopted = []
    if R32_RECEIPT.is_file():
        r32_receipt = json.loads(R32_RECEIPT.read_text())
        known = {shlex.join(["python3", "-B", *s["argv"]]) for s in specs}
        for row in r32_receipt["rows"]:
            argv = shlex.split(row["command"])
            if row["command"] in known:
                continue
            if argv[:2] != ["python3", "-B"]:
                raise SystemExit(f"unexpected adopted command shape: {row['command']}")
            specs.append({"id": row["id"], "argv": argv[2:], "tool": argv[2],
                          "class": row.get("class", "sweep"),
                          "expect_exit": row.get("expect_exit", 0),
                          "provenance": "reports/round-32/sweep/sweep-receipt.json"})
            adopted.append(row["id"])
    audit = {
        "assignment": "R32-O09..O10 (sweep auditors x2): independent re-runs >=10 of the "
                      "r31 final-sweep surface; mismatches = findings",
        "counting_command": COMMAND,
        "date": utc()[:10],
        "baseline_revision": BASELINE,
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "tree_clean_at_start": subprocess.run(
            ["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True
        ).stdout.strip() == "",
        "matrix_provenance": {
            "source": "reports/round-31/sweep/sweep-receipt.json",
            "sha256": file_digest(R31_RECEIPT),
            "rows_loaded": len(specs),
            "green_rows": sum(1 for s in specs if s["class"] == "sweep"),
            "historical_controls": sum(1 for s in specs if s["class"] == "historical-control"),
            "control_codes_filed_table_agree": True,
            "adopted_from_r32_receipt": adopted,
        },
        "claims_json_sha256": file_digest(HERE / "claims.json"),
        "targets_json_sha256": file_digest(HERE / "targets.json"),
        "external_tmp_legs": sorted({s["tool"] for s in specs if s["tool"] in REPLAY_TOOLS}),
        "volatile_rows_whitelist": sorted(VOLATILE_ROWS),
        "passes": {},
    }
    sources_before = source_snapshot()
    pass_rows = {}
    for leg in ("O09", "O10"):
        started = utc()
        rows = execute_pass(specs, leg)
        pass_rows[leg] = rows
        green = [r for r in rows if r["class"] == "sweep"]
        controls = [r for r in rows if r["class"] == "historical-control"]
        audit["passes"][leg] = {
            "started_at_utc": started, "finished_at_utc": utc(),
            "commands_executed": len(rows),
            "green_rows": len(green),
            "green_exit0": sum(1 for r in green if r["exit_code"] == 0),
            "green_nonzero": [{"id": r["id"], "exit_code": r["exit_code"]}
                              for r in green if r["exit_code"] != 0],
            "controls_at_expected_code": sum(1 for r in controls if r["expected_exit_matches"]),
            "controls_off_code": [{"id": r["id"], "exit_code": r["exit_code"],
                                   "expect_exit": r["expect_exit"]}
                                  for r in controls if not r["expected_exit_matches"]],
        }
        (HERE / f"sweep-audit-{leg}.json").write_text(json.dumps({
            "assignment": "R32-O09..O10", "leg": leg, "counting_command": COMMAND,
            "date": audit["date"], "baseline_revision": BASELINE, "head": audit["head"],
            "results": [row_public(r) for r in rows],
        }, indent=1) + "\n")
    audit["cross_pass_findings"], audit["expected_cross_pass_volatility"] = \
        compare_passes(pass_rows["O09"], pass_rows["O10"])
    sources_after = source_snapshot()
    audit["source_drift_during_audit"] = sorted(
        p for p in sources_before.keys() | sources_after.keys()
        if sources_before.get(p) != sources_after.get(p))
    audit["r31_receipt_cross_check_o09"] = cross_check_receipt(
        pass_rows["O09"], r31_receipt, "reports/round-31/sweep/sweep-receipt.json")
    audit["r31_receipt_cross_check_o10"] = cross_check_receipt(
        pass_rows["O10"], r31_receipt, "reports/round-31/sweep/sweep-receipt.json")
    if R32_RECEIPT.is_file():
        r32_receipt = json.loads(R32_RECEIPT.read_text())
        audit["r32_receipt_sha256_at_comparison"] = file_digest(R32_RECEIPT)
        audit["r32_receipt_cross_check_o09"] = cross_check_receipt(
            pass_rows["O09"], r32_receipt, "reports/round-32/sweep/sweep-receipt.json")
        audit["r32_receipt_cross_check_o10"] = cross_check_receipt(
            pass_rows["O10"], r32_receipt, "reports/round-32/sweep/sweep-receipt.json")
        audit["r32_receipt_only_rows"] = sorted(
            r["command"] for r in r32_receipt["rows"] if r["command"] not in
            {m["command"] for m in pass_rows["O09"]})
        audit["audit_only_rows"] = sorted(
            m["command"] for m in pass_rows["O09"]
            if m["command"] not in {r["command"] for r in r32_receipt["rows"]})
    if R32_FINAL_SWEEP_MD.is_file():
        text = R32_FINAL_SWEEP_MD.read_text(errors="replace")
        recorded = extract_recorded_commands(text)
        audit["r32_final_sweep_md"] = {
            "present": True,
            "sha256": file_digest(R32_FINAL_SWEEP_MD),
            "table_cross_check_o09": cross_check_sweep_table(pass_rows["O09"], text),
            "table_cross_check_o10": cross_check_sweep_table(pass_rows["O10"], text),
            "recorded_command_lines": len(recorded),
            "verbatim_reruns": [verbatim_rerun(c) for c in recorded],
        }
    audit["r32_round_runner"] = (
        {"present": True, "sha256": file_digest(R32_VALIDATION),
         "executed_by_this_audit": False,
         "note": "orchestrator-owned counting command; not executed here so its "
                 "writes (validation.json) stay the integrating parent's"}
        if R32_VALIDATION.is_file() else
        {"present": False, "executed_by_this_audit": False,
         "note": "not landed at audit time; counting-command execution is "
                 "orchestrator-owned and recorded could-not-evaluate here"})
    (HERE / "sweep-audit-O09O10.json").write_text(json.dumps(audit, indent=1) + "\n")
    print(json.dumps({
        "counting_command": COMMAND,
        "matrix": audit["matrix_provenance"],
        "O09_green_exit0": audit["passes"]["O09"]["green_exit0"],
        "O10_green_exit0": audit["passes"]["O10"]["green_exit0"],
        "O09_controls_at_code": audit["passes"]["O09"]["controls_at_expected_code"],
        "O10_controls_at_code": audit["passes"]["O10"]["controls_at_expected_code"],
        "cross_pass_findings": audit["cross_pass_findings"],
        "expected_volatility_families": sorted(
            {e["id"] for e in audit["expected_cross_pass_volatility"]}),
        "source_drift": audit["source_drift_during_audit"],
        "r31_receipt_o09": audit["r31_receipt_cross_check_o09"],
        "r32_receipt_present": "r32_receipt_cross_check_o09" in audit,
        "r32_final_sweep_present": "r32_final_sweep_md" in audit,
        "r32_runner_present": audit["r32_round_runner"]["present"],
    }, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
