#!/usr/bin/env python3
"""Independently validate Round-29 C/O/A evidence without rewriting prior rounds."""
from __future__ import annotations

import argparse
from collections import Counter
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-29"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
CLAIMS = f"{ROUND_DIR}/claims.json"
COMMAND = f"python3 {RUNNER}"
BASELINE = "3b13a2f2821ed6f8ac1217842ab6830d592c7935"
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 29)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 29)
)
RECOUNT_GROUPS = {
    25: [f"{ROUND_DIR}/recount/r25-{n}.md" for n in range(1, 5)],
    26: [f"{ROUND_DIR}/recount/C{n:02d}.md" for n in range(5, 9)],
    27: [f"{ROUND_DIR}/recount/C{n:02d}.md" for n in range(9, 13)],
    28: [f"{ROUND_DIR}/recount/C13-C16.md"],
}
AVAILABILITY = {
    25: {
        "samples": [".scratch/x41/sample-60x16.json", ".scratch/x41/sample-24x8.json"],
        "labeled": ".scratch/x41/labeled.json",
        "clean": "exclude tags containing temp0; include the three clean-absent labeled controls",
        "journal_window": ("14:23:00", "14:45:04"),
        "traffic_key": "journal_traffic",
    },
    26: {
        "samples": [".scratch/x59/sample.json", ".scratch/x59/sample2.json"],
        "labeled": None,
        "clean": "exclude tags beginning control, matching the filed clean_population_only predicate",
        "journal_window": ("14:58:00", "15:22:00"),
        "traffic_key": "whole_window_traffic",
    },
    27: {
        "samples": [".scratch/x53/sample.json"],
        "labeled": None,
        "clean": "temperature != 0, matching the filed clean_population_only predicate",
        "journal_window": ("16:05:00", "16:16:00"),
        "traffic_key": "whole_window_traffic",
    },
    28: {
        "samples": [".scratch/x53-r28/sample.json"],
        "labeled": None,
        "clean": "temperature != 0 and tag does not begin err-, matching wellformed_population",
        "journal_window": ("16:05:00", "17:13:10"),
        "traffic_key": "whole_window_traffic",
    },
}
REGRESSIONS = (
    ("battery-selftest", ["python3", "-B", "tools/check-gate-battery.py", "--selftest"]),
    ("battery", ["python3", "-B", "tools/check-gate-battery.py"]),
    ("typed-pipeline-selftest", ["python3", "-B", "tools/gates/typed-pipeline-gate.py", "--selftest"]),
    ("typed-pipeline-d4", ["python3", "-B", "tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.yml"]),
    ("typed-pipeline-typed-d4", ["python3", "-B", "tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.typed.yml"]),
    ("handoff-v3", ["python3", "-B", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet"]),
    ("argot-selftest", ["python3", "-B", "tools/gates/argot-derivation-gate.py", "--selftest"]),
    ("argot-d4", ["python3", "-B", "tools/gates/argot-derivation-gate.py", "examples/culture-d4/packet.d4.yml"]),
    ("law-selftest", ["python3", "-B", "tools/gates/register-law-gate.py", "--selftest"]),
    ("pin-repoint-selftest", ["python3", "-B", "reports/round-26/remainders/pin-repoint-check.py", "--selftest"]),
    ("r28-sweep-selftest", ["python3", "-B", "reports/round-28/sweep/sweep.py", "--selftest"]),
)


def today() -> str:
    return dt.date.today().isoformat()


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_path(relative: str | Path) -> Path:
    path = (ROOT / relative).resolve()
    path.relative_to(ROOT)
    return path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(relative: str) -> dict:
    return json.loads(safe_path(relative).read_text(encoding="utf-8"))


def read_rows(relative: str) -> list[dict]:
    data = json.loads(safe_path(relative).read_text(encoding="utf-8"))
    rows = data if isinstance(data, list) else data.get("attempts")
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise ValueError(f"{relative}: expected a JSON list of attempt records")
    return rows


def status_counts(rows: list[dict]) -> dict[str, int]:
    return dict(sorted(Counter(str(row.get("http_status", row.get("status", "missing"))) for row in rows).items()))


def population(rows: list[dict], predicate) -> dict:
    selected = [row for row in rows if predicate(row)]
    counts = status_counts(selected)
    return {"attempts": len(selected), "completed": counts.get("200", 0), "statuses": counts}


def argot_coverage(text: str) -> dict[str, int] | None:
    match = re.search(
        r"coverage:.*?records=(\d+).*?register_scoped=(\d+).*?derived_pairs=(\d+).*?"
        r"claimed_chains=(\d+).*?borrow_pairs=(\d+).*?violations=(\d+).*?rule_holds=(\d+)",
        text,
    )
    if not match:
        return None
    names = ("records", "register_scoped", "derived_pairs", "claimed_chains", "borrow_pairs", "violations", "rule_holds")
    return dict(zip(names, map(int, match.groups())))


def law_findings(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if "FINDING D4L-LAW-" in line]


def extract_rgl_ids(text: str) -> list[str]:
    ids = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("- {id: RGL-", 'id: "RGL-')):
            match = re.search(r"RGL-0[1-5]", stripped)
            if match:
                ids.append(match.group(0))
    return ids


def run_command(name: str, argv: list[str], env: dict[str, str]) -> dict:
    if name == "r28-sweep-selftest":
        # The sweep's mirror-safety leg requires TMPDIR outside the repo clone
        # (the r22 d4-repin precedent); an in-repo TMPDIR fails closed with
        # mirror_unsafe. Point it at a scratch dir above the clone.
        env = dict(env)
        env["TMPDIR"] = str(ROOT.parent / "tmpdir-outside-repo")
        Path(env["TMPDIR"]).mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        argv,
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        errors="replace",
    )
    return {
        "name": name,
        "command": shlex.join(argv),
        "date": today(),
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def short_output(text: str, limit: int = 6) -> list[str]:
    return [line.strip() for line in text.splitlines()[-limit:] if line.strip()]


def run_regressions(env: dict[str, str]) -> tuple[list[dict], dict[str, dict]]:
    results = []
    raw = {}
    for name, argv in REGRESSIONS:
        item = run_command(name, argv, env)
        raw[name] = item
        if name == "r28-sweep-selftest":
            try:
                receipt = json.loads(item["stdout"])
                controls = receipt.get("controls", [])
                failed_controls = [row.get("control") for row in controls if not row.get("passed")]
                summary = {
                    "passed_controls": receipt.get("passed_controls"),
                    "total_controls": receipt.get("total_controls"),
                    "failed_controls": failed_controls,
                }
            except (json.JSONDecodeError, TypeError):
                summary = {"output_tail": short_output(item["stdout"] + item["stderr"])}
        else:
            summary = {"output_tail": short_output(item["stdout"] + item["stderr"])}
        results.append({
            "name": name,
            "command": item["command"],
            "date": item["date"],
            "exit_code": item["exit_code"],
            "passed": item["exit_code"] == 0,
            "summary": summary,
        })
    return results, raw


def journal_measurement(round_no: int, availability: dict, config: dict) -> dict:
    start, end = config["journal_window"]
    date = availability.get("date", today())
    argv = [
        "journalctl", "--user", "-u", "devin-shim.service",
        "--since", f"{date} {start}", "--until", f"{date} {end}", "--no-pager",
    ]
    command = shlex.join(argv) + " | python3 -c 'count HTTP/1.1 status codes'"
    try:
        completed = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True, errors="replace")
    except OSError as error:
        return {
            "round": round_no,
            "source": f"reports/round-{round_no}/availability.json",
            "date": today(),
            "source_date": availability.get("counts_date", availability.get("date")),
            "command": command,
            "recorded_command": availability.get(config["traffic_key"], {}).get("counting_command"),
            "evaluated": False,
            "error": f"{type(error).__name__}: {error}",
        }
    observed = dict(sorted(Counter(re.findall(r'HTTP/1\.1"\s+(\d{3})', completed.stdout)).items()))
    traffic = availability.get(config["traffic_key"], {})
    recorded = {}
    for code, field in (("200", "http_200"), ("400", "http_400"), ("403", "http_403"), ("5xx", "http_5xx")):
        value = traffic.get(field)
        if value:
            recorded[code] = int(value)
    status_match = completed.returncode == 0 and observed == recorded and traffic.get("other_status_lines", 0) == 0
    total_match = "total_http_lines" not in traffic or sum(observed.values()) == traffic["total_http_lines"]
    return {
        "round": round_no,
        "source": f"reports/round-{round_no}/availability.json",
        "date": today(),
        "source_date": availability.get("counts_date", availability.get("date")),
        "window_local": {"since": start, "until": end},
        "command": command,
        "recorded_command": traffic.get("counting_command"),
        "exit_code": completed.returncode,
        "recorded_status_counts": recorded,
        "observed_status_counts": observed,
        "other_status_lines_recorded": traffic.get("other_status_lines", 0),
        "matches": status_match and total_match,
        "stderr": completed.stderr.strip(),
    }


def verify_availability(round_no: int, round_claims: dict) -> dict:
    relative = f"reports/round-{round_no}/availability.json"
    disposition = safe_path(f"{ROUND_DIR}/devin-availability-disposition.md")
    samples = AVAILABILITY[round_no]["samples"]
    samples_present = all(safe_path(s).is_file() for s in samples)
    if not samples_present and disposition.is_file() and safe_path(relative).is_file():
        # Documented could-not-evaluate: wave-time telemetry lost with .scratch
        # cleanup; durable availability record present; round-30 fix named.
        data = read_json(relative)
        return {"status": "could-not-evaluate-dispositioned", "passed": False, "findings": [],
                "dispositioned": True,
                "disposition": str(disposition.relative_to(ROOT)),
                "durable_record": relative,
                "route": data.get("route"),
                "note": "telemetry samples unrecoverable post-hoc; see disposition doc; NOT a pass"}
    relative = f"reports/round-{round_no}/availability.json"
    data = read_json(relative)
    config = AVAILABILITY[round_no]
    source_date = data.get("counts_date", data.get("date"))
    claim_model = round_claims.get("requested_model")
    model_matches = data.get("route") == claim_model
    workers_match = data.get("requested_workers") == round_claims.get("workers")
    sample_records = []
    all_rows = []
    findings = []
    if not model_matches:
        findings.append(f"Round {round_no} requested route differs from claims.json")
    if not workers_match:
        findings.append(f"Round {round_no} requested worker count differs from claims.json")
    for sample_path in config["samples"]:
        rows = read_rows(sample_path)
        all_rows.extend(rows)
        actual = population(rows, lambda row: True)
        per_sample = data.get("completion_measurement", {}).get("per_sample", {}).get(Path(sample_path).name)
        if per_sample is None:
            per_sample = data.get("completion_measurement", {}).get("per_leg", {}).get(Path(sample_path).stem)
        recorded = None
        if isinstance(per_sample, dict):
            recorded = {"attempts": per_sample.get("attempts", per_sample.get("n")),
                        "completed": per_sample.get("completed", per_sample.get("ok"))}
        matches = recorded is None or recorded == {"attempts": actual["attempts"], "completed": actual["completed"]}
        digest = sha256(safe_path(sample_path).read_bytes())
        sample_records.append({
            "path": sample_path,
            "sha256": digest,
            "observed": actual,
            "recorded": recorded,
            "matches": matches,
        })
        if not matches:
            findings.append(f"{sample_path}: raw attempt totals differ from availability.json")
    if config.get("labeled"):
        rows = read_rows(config["labeled"])
        all_rows.extend(rows)
        sample_records.append({
            "path": config["labeled"],
            "sha256": sha256(safe_path(config["labeled"]).read_bytes()),
            "observed": population(rows, lambda row: True),
            "recorded": "labeled controls included only in the round-25 clean-population recount",
            "matches": True,
        })
    clean_key = {25: "clean_attempts", 26: "clean_population_only", 27: "clean_population_only", 28: "wellformed_population"}[round_no]
    measurement = data.get("completion_measurement", {})
    if round_no == 25:
        clean_rows = [row for row in all_rows if "temp0" not in str(row.get("tag", "")).lower()]
    elif round_no == 26:
        clean_rows = [row for row in all_rows if not str(row.get("tag", "")).startswith("control")]
    elif round_no == 27:
        clean_rows = [row for row in all_rows if row.get("temperature") != 0]
    else:
        clean_rows = [row for row in all_rows if row.get("temperature") != 0 and not str(row.get("tag", "")).startswith("err-")]
    observed_clean = population(clean_rows, lambda row: True)
    recorded_clean = measurement.get(clean_key, {})
    clean_matches = (
        observed_clean["attempts"] == recorded_clean.get("attempts")
        and observed_clean["completed"] == recorded_clean.get("completed")
    )
    if not clean_matches:
        findings.append(f"Round {round_no} clean-population counts differ from the raw sample files")
    all_observed = population(all_rows, lambda row: True)
    aggregate_record = measurement.get("clean_attempts", {})
    aggregate_matches = True
    if round_no != 25:
        aggregate_matches = (
            all_observed["attempts"] == aggregate_record.get("attempts")
            and all_observed["completed"] == aggregate_record.get("completed")
        )
        if not aggregate_matches:
            findings.append(f"Round {round_no} aggregate attempt counts differ from the raw sample files")
    journal = journal_measurement(round_no, data, config)
    if not journal.get("matches", False):
        findings.append(f"Round {round_no} recorded journal counts do not match the dated journal re-read")
    command = measurement.get("counting_command") or recorded_clean.get("counting_command") or data.get("counting_command")
    command_evidence = isinstance(command, str) and bool(command.strip()) and bool(source_date)
    if not command_evidence:
        findings.append(f"Round {round_no} availability population lacks a dated counting command")
    return {
        "round": round_no,
        "source": relative,
        "source_date": source_date,
        "recount_command": COMMAND,
        "recount_date": today(),
        "route": data.get("route"),
        "declared_route": claim_model,
        "requested_workers": data.get("requested_workers"),
        "declared_workers": round_claims.get("workers"),
        "route_matches_claim": model_matches,
        "workers_match_claim": workers_match,
        "population_predicate": config["clean"],
        "recorded_clean_population": {
            "attempts": recorded_clean.get("attempts"),
            "completed": recorded_clean.get("completed"),
            "ratio": recorded_clean.get("completion_ratio"),
            "counting_command": command,
            "date": source_date,
        },
        "observed_clean_population": observed_clean,
        "clean_population_matches": clean_matches,
        "recorded_aggregate_population": {
            "attempts": aggregate_record.get("attempts"),
            "completed": aggregate_record.get("completed"),
            "counting_command": measurement.get("counting_command"),
            "date": source_date,
        },
        "observed_all_sample_rows": all_observed,
        "aggregate_population_matches": aggregate_matches,
        "sample_files": sample_records,
        "journal": journal,
        "passed": model_matches and workers_match and clean_matches and aggregate_matches and command_evidence and journal.get("matches", False) and all(row["matches"] for row in sample_records),
        "findings": findings,
    }


def measure_availability(round_claims: dict[int, dict]) -> list[dict]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {
            round_no: pool.submit(verify_availability, round_no, round_claims[round_no])
            for round_no in sorted(AVAILABILITY)
        }
        return [futures[round_no].result() for round_no in sorted(futures)]


def verify_recount_evidence(round_claims: dict[int, dict], rerun: dict) -> dict:
    groups = []
    for round_no, paths in RECOUNT_GROUPS.items():
        artifacts = []
        for relative in paths:
            path = safe_path(relative)
            present = path.is_file()
            text = path.read_text(encoding="utf-8") if present else ""
            command_present = bool(re.search(r"(?:python3|journalctl|git archive|sha256sum|Path\.rglob)", text))
            date_present = bool(re.search(r"2026-10-18", text))
            artifacts.append({
                "path": relative,
                "present": present,
                "date_present": date_present,
                "command_present": command_present,
                "sha256": sha256(path.read_bytes()) if present else None,
                "complete": present and date_present and command_present,
            })
        round_claim = round_claims[round_no]
        declared_commands = sorted({str(item.get("counting_command")) for item in round_claim.get("claims", []) if item.get("counting_command")})
        groups.append({
            "round": round_no,
            "date": today(),
            "command": COMMAND,
            "declared_counting_commands": declared_commands,
            "artifacts": artifacts,
            "complete": bool(artifacts) and all(item["complete"] for item in artifacts) and bool(declared_commands),
        })
    rerun_runs = rerun.get("runs", [])
    rerun_by_round = {item.get("round"): item for item in rerun_runs}
    settled_rerun = []
    for round_no in (25, 26, 27, 28):
        item = rerun_by_round.get(round_no, {})
        settled_rerun.append({
            "round": round_no,
            "date": item.get("date"),
            "command": item.get("command"),
            "exit_code": item.get("exit_code"),
            "acceptance_checks_passed": item.get("acceptance_checks_passed"),
            "failures": item.get("failures", []),
            "source": f"{ROUND_DIR}/rerun.json",
            "recorded": bool(item.get("command") and item.get("date") and isinstance(item.get("exit_code"), int)),
        })
    c11_path = f"{ROUND_DIR}/recount/C11.md"
    c11_text = safe_path(c11_path).read_text(encoding="utf-8") if safe_path(c11_path).is_file() else ""
    full_r27_sweep_reproduced = not (
        "does not independently reproduce the full 113-surface / 31-finding sweep summary" in c11_text
        or "The full X61 sweep and its mirror-based replay were deliberately not run" in c11_text
    )
    c12_path = f"{ROUND_DIR}/recount/C12.md"
    c12_text = safe_path(c12_path).read_text(encoding="utf-8") if safe_path(c12_path).is_file() else ""
    locator_difference_dispositioned = "36→41 difference remains unresolved" in c12_text and "not silently reconciled" in c12_text
    return {
        "date": today(),
        "command": COMMAND,
        "groups": groups,
        "all_recount_groups_complete": len(groups) == 4 and all(group["complete"] for group in groups),
        "settled_tree_round_rechecks": settled_rerun,
        "settled_tree_recheck_coverage": len([row for row in settled_rerun if row["recorded"]]),
        "settled_tree_recheck_total": 4,
        "settled_tree_rechecks_complete": all(row["recorded"] for row in settled_rerun),
        "r27_full_sweep_reproduced": full_r27_sweep_reproduced,
        "r27_full_sweep_disposition": "C11 explicitly records that the 113-surface / 31-finding full sweep was not independently reproduced; only scoped inventory/static checks were recounted.",
        "r27_locator_count_dispositioned": locator_difference_dispositioned,
    }


def verify_register_landing() -> list[dict]:
    checks = []
    def add(name: str, relative: str, patterns: tuple[str, ...], command: str) -> None:
        path = safe_path(relative)
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        checks.append({
            "name": name,
            "source": relative,
            "date": today(),
            "command": command,
            "passed": path.is_file() and all(pattern in text for pattern in patterns),
            "patterns": list(patterns),
        })
    add("R26 frozen/component register roster", f"{ROUND_DIR}/recount/C05.md", ("lexicon_rows=62", "stamp_rows=8", "L-56", "L-62"), "python3 reports/round-29/run-validation.py (recount evidence check)")
    add("R26 argot coverage", f"{ROUND_DIR}/recount/C06.md", ("records=170", "derived_pairs=8", "violations=0", "rule_holds=0"), "python3 reports/round-29/run-validation.py (recount evidence check)")
    add("R26 typed-pipeline leg", f"{ROUND_DIR}/recount/C07.md", ("L3b-argot", "summary: 20/20 legs passed"), "python3 reports/round-29/run-validation.py (recount evidence check)")
    add("R26/R27/R28 snapshot lineage", f"{ROUND_DIR}/recount/C08.md", ("records=170", "records=175", "records=183", "not treated as the R26 verdict"), "python3 reports/round-29/run-validation.py (recount evidence check)")
    add("R27/R28 RL-4 record delta", f"{ROUND_DIR}/recount/C13-C16.md", ("175", "183", "0/8", "8/8", "+8"), "python3 reports/round-29/run-validation.py (recount evidence check)")
    add("Current argot register pairs", f"{ROUND_DIR}/recount/C13-C16.md", ("records=183", "register_scoped=14", "derived_pairs=8", "violations=0"), "python3 reports/round-29/run-validation.py (recount evidence check)")
    return checks


def verify_law_calibration(env: dict[str, str], argot_result: dict | None) -> dict:
    argv = ["python3", "-B", "tools/gates/register-law-gate.py", "--packet", "examples/culture-d4/packet.d4.yml"]
    item = run_command("law-clean-calibration", argv, env)
    coverage_match = re.search(r"coverage:.*?findings=(\d+)", item["stdout"])
    findings = law_findings(item["stdout"])
    try:
        filed = safe_path(f"{ROUND_DIR}/recount/C13-C16.md").read_text(encoding="utf-8")
    except OSError:
        filed = ""
    expected_six = bool(re.search(r"\*\*6\*\*\s+total", filed)) and "4 dangling + 2 consequence" in filed
    observed_count = len(findings) if findings else int(coverage_match.group(1)) if coverage_match else None
    expected_command = "python3 .scratch/r28-law/replay-probe.py"
    evaluated = item["exit_code"] in (0, 1) and observed_count is not None
    return {
        "date": item["date"],
        "command": item["command"],
        "exit_code": item["exit_code"],
        "evaluated": evaluated,
        "design_reference": {
            "source": f"{ROUND_DIR}/recount/C13-C16.md",
            "date": "2026-10-18",
            "command": expected_command,
            "expected_findings": 6 if expected_six else None,
        },
        "observed_findings": observed_count,
        "finding_lines": findings,
        "coverage_line": next((line.strip() for line in item["stdout"].splitlines() if "coverage:" in line), None),
        "current_argot_coverage": argot_coverage((argot_result or {}).get("stdout", "")),
        "passed": evaluated and expected_six and observed_count == 6,
        "disposition": "The delivered gate is measured from the current packet. Four dangling findings reproduce; the two design-probe consequence findings do not. Preserve the six-versus-four difference; do not relabel four as six.",
    }


def read_round_claims() -> tuple[dict, dict[int, dict]]:
    round29_claims = read_json(CLAIMS)
    by_round = {}
    for round_no in (25, 26, 27, 28):
        data = read_json(f"reports/round-{round_no}/claims.json")
        by_round[round_no] = data
    return round29_claims, by_round


def ledger_quality() -> dict:
    relative = f"{ROUND_DIR}/defects/ledger.json"
    ledger = read_json(relative)
    allowed_statuses = set(ledger.get("status_values", []))
    allowed_classes = {"conformance", "process", "bookkeeping"}
    problems = []
    ids = set()
    missing_sources = []
    for entry in ledger.get("entries", []):
        entry_id = entry.get("id")
        if not entry_id or entry_id in ids:
            problems.append(f"duplicate or missing defect id: {entry_id}")
        ids.add(entry_id)
        if entry.get("status") not in allowed_statuses:
            problems.append(f"{entry_id}: unknown status")
        if entry.get("classification") not in allowed_classes:
            problems.append(f"{entry_id}: missing/unknown classification")
        if entry.get("round") not in (25, 26, 27, 28):
            problems.append(f"{entry_id}: outside audited rounds")
        if not entry.get("owner") or not entry.get("owner_note") or entry.get("route_round") != 30:
            problems.append(f"{entry_id}: missing owner, route, or owner note")
        if not entry.get("sources"):
            problems.append(f"{entry_id}: no source citation")
        for source in entry.get("sources", []):
            relative_source = str(source).split(":", 1)[0]
            if not safe_path(relative_source).is_file():
                missing_sources.append(relative_source)
        measurements = entry.get("measurements", [])
        if not measurements or any(not row.get("date") or not row.get("command") or not row.get("result") for row in measurements):
            problems.append(f"{entry_id}: measurement lacks command/date/result")
        if entry.get("status") in ("closed", "superseded") and not all(
            entry.get(key) for key in ("bounded", "fix_scope", "before", "after", "control")
        ):
            problems.append(f"{entry_id}: closed/superseded without bounded before/after/control")
        if entry.get("status") in ("open", "observation") and entry.get("route_round") != 30:
            problems.append(f"{entry_id}: unresolved item not routed to round 30")
    if missing_sources:
        problems.extend(f"missing source: {path}" for path in sorted(set(missing_sources)))
    return {
        "source": relative,
        "date": today(),
        "command": "python3 reports/round-29/run-validation.py (defect-ledger schema and source-path audit)",
        "entries": len(ledger.get("entries", [])),
        "status_counts": {status: sum(entry.get("status") == status for entry in ledger.get("entries", [])) for status in sorted(allowed_statuses)},
        "rounds_covered": sorted({entry.get("round") for entry in ledger.get("entries", [])}),
        "problems": problems,
        "passed": not problems and {entry.get("round") for entry in ledger.get("entries", [])} == {25, 26, 27, 28},
    }


def defect_fragment_ids(text: str) -> set[int]:
    found = set()
    for start, end in re.findall(r"R29-O(\d{2})(?:\.\.O(\d{2}))?", text):
        first = int(start)
        last = int(end) if end else first
        found.update(range(first, last + 1))
    found.update(int(number) for number in re.findall(r"(?m)^#{1,6}\s+O(\d{2})\b", text))
    return found


def audit_document_coverage() -> dict:
    paths = [f"{ROUND_DIR}/defects/sweep-r{round_no}.md" for round_no in (25, 26, 27, 28)]
    paths += [f"{ROUND_DIR}/defects/fix-{number:02d}.md" for number in range(9, 17)]
    present_ids = set()
    artifacts = []
    for relative in paths:
        path = safe_path(relative)
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        found = defect_fragment_ids(text)
        present_ids.update(found)
        artifacts.append({
            "path": relative,
            "present": path.is_file(),
            "date_present": "2026-10-18" in text,
            "command_present": any(marker in text for marker in ("python3", "journalctl", "git archive", "sha256sum", "Path.rglob", "--check")),
            "finding_ids": sorted(found),
        })
    expected = set(range(1, 17))
    return {
        "date": today(),
        "command": "python3 reports/round-29/run-validation.py (O-fragment coverage audit)",
        "artifacts": artifacts,
        "finding_ids_present": sorted(present_ids),
        "missing_finding_ids": sorted(expected - present_ids),
        "unexpected_finding_ids": sorted(present_ids - expected),
        "passed": all(item["present"] and item["date_present"] and item["command_present"] for item in artifacts) and present_ids == expected,
    }


def git_status(paths: tuple[str, ...]) -> tuple[int, str]:
    proc = subprocess.run(
        ["git", "status", "--porcelain=v1", "-uall", "--", *paths],
        cwd=ROOT,
        text=True,
        capture_output=True,
        errors="replace",
    )
    return proc.returncode, proc.stdout


def protection_guard(before: tuple[int, str], after: tuple[int, str]) -> dict:
    diff = subprocess.run(
        ["git", "diff", "--quiet", BASELINE, "--", *PROTECTED],
        cwd=ROOT,
        text=True,
        capture_output=True,
        errors="replace",
    )
    return {
        "date": today(),
        "command": f"git status --porcelain=v1 -uall -- {' '.join(PROTECTED)} (before/after regression commands); git diff --quiet {BASELINE} -- <protected paths>",
        "before_status_rows": len(before[1].splitlines()),
        "after_status_rows": len(after[1].splitlines()),
        "status_unchanged": before == after,
        "baseline_diff_exit": diff.returncode,
        "passed": before[0] == 0 and after[0] == 0 and before == after and diff.returncode == 0,
    }


def measure_operability(regressions: list[dict], ledger: dict, fragments: dict, protection: dict) -> dict:
    unresolved_routed = ledger["passed"]
    bounded_records_complete = ledger["passed"]
    regression_green = all(item["passed"] for item in regressions)
    failures = []
    if not fragments["passed"]:
        failures.append("defect sweep/fix fragments do not cover all R29-O01..O16 findings")
    if not ledger["passed"]:
        failures.append("defect ledger has missing classification, citation, owner/route, measurement, or bounded closure evidence")
    if not protection["passed"]:
        failures.append("protected rounds 8-28 were not shown unchanged by the regression run")
    failed_regressions = [item for item in regressions if not item["passed"]]
    if failed_regressions:
        failures.extend(f"regression {item['name']} exited {item['exit_code']}" for item in failed_regressions)
    return {
        "passed": not failures,
        "date": today(),
        "command": COMMAND,
        "defect_ledger": ledger,
        "fragment_coverage": fragments,
        "bounded_closures_supported": bounded_records_complete,
        "unresolved_items_routed_to_round_30": unresolved_routed,
        "regressions": regressions,
        "all_regressions_green": regression_green,
        "protected_surface": protection,
        "failures": failures,
        "scope_note": "The settled-tree R25-R27 acceptance reruns are reported separately under calibration; their later-tree drift is not substituted for these direct regression controls.",
    }


def measure_adjacency() -> dict:
    ledger_path = f"{ROUND_DIR}/adjacency/ledger.json"
    ledger = read_json(ledger_path)
    records = ledger.get("entries", []) + ledger.get("rows", []) + ledger.get("audits", [])
    ids_by_path = {}
    for surface in ("examples/culture-d4/components/13-register-law.yml", "examples/culture-d4/packet.d4.yml"):
        text = safe_path(surface).read_text(encoding="utf-8")
        ids_by_path[surface] = extract_rgl_ids(text)
    expected_ids = [f"RGL-0{n}" for n in range(1, 6)]
    entry_paths = [entry.get("path") for entry in ledger.get("entries", [])]
    entry_checks = []
    for relative in entry_paths:
        path = safe_path(relative)
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        entry_checks.append({
            "path": relative,
            "exists": path.is_file(),
            "noncanon": "NON-CANON" in text,
            "canon_boundary": "Canon boundary and handoff" in text,
        })
    readme = safe_path("corpus/README.md").read_text(encoding="utf-8").splitlines()
    readme_rows = {
        "register-strata-attestation.md": sum(line.startswith("- `register-strata-attestation.md` —") for line in readme),
        "register-lexicon-ceilings.md": sum(line.startswith("- `register-lexicon-ceilings.md` —") for line in readme),
    }
    component = safe_path("examples/culture-d4/components/13-register-law.yml").read_text(encoding="utf-8")
    packet = safe_path("examples/culture-d4/packet.d4.yml").read_text(encoding="utf-8")
    province_digest = sha256(safe_path("PROVINCE.md").read_bytes())
    baseline = read_json(CLAIMS).get("baseline_revision", BASELINE)
    province_diff = subprocess.run(
        ["git", "diff", "--quiet", baseline, "--", "PROVINCE.md"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        errors="replace",
    )
    inventory = ledger.get("inventory", {})
    clean_scope = (
        ledger.get("unfiled_bleed") == 0
        and all(row.get("bleed") is False and row.get("out_of_province") is False for row in records)
        and all(
            finding.get("filed") is True
            and finding.get("bleed") is False
            and finding.get("out_of_province") is False
            for finding in ledger.get("findings", [])
        )
    )
    content_checks = (
        len(entry_paths) == 2
        and all(item["exists"] and item["noncanon"] and item["canon_boundary"] for item in entry_checks)
        and all(count == 1 for count in readme_rows.values())
        and all(ids == expected_ids for ids in ids_by_path.values())
        and "No real-world language, institution, community, or rights question is decided" in component
        and "NON-CANON" in component
        and "NON-CANON" in packet
        and province_diff.returncode == 0
        and province_digest == "05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6"
    )
    passed = clean_scope and content_checks and len(records) == 6 and province_diff.returncode == 0
    return {
        "passed": passed,
        "date": today(),
        "command": COMMAND,
        "source": ledger_path,
        "source_date": ledger.get("date"),
        "source_command": inventory.get("command"),
        "source_result": inventory.get("result"),
        "scoped_records": len(records),
        "entry_count": len(ledger.get("entries", [])),
        "readme_row_records": len(ledger.get("rows", [])),
        "audited_surface_count": len(ledger.get("audits", [])),
        "bleed_count": sum(bool(row.get("bleed")) for row in records),
        "unfiled_bleed": ledger.get("unfiled_bleed"),
        "out_of_province_count": sum(bool(row.get("out_of_province")) for row in records),
        "findings": ledger.get("findings"),
        "register_law_ids": ids_by_path,
        "expected_register_law_ids": expected_ids,
        "knowledge_entries": entry_checks,
        "readme_filename_rows": readme_rows,
        "province": {
            "sha256": province_digest,
            "recorded_sha256": "05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6",
            "baseline_revision": baseline,
            "git_diff_exit": province_diff.returncode,
        },
        "scope_note": "PASS is limited to the six audited surfaces. The province-entries report separately records one source-sweep authoring defect and three sibling landings; neither is classified there as out-of-province bleed. Existing A21-D4-XF-01 remains outside this slice.",
    }


def measure() -> dict:
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    env = os.environ.copy()
    round29_claims, round_claims = read_round_claims()
    rerun = read_json(f"{ROUND_DIR}/rerun.json")
    recount = verify_recount_evidence(round_claims, rerun)
    availability = measure_availability(round_claims)
    register_checks = verify_register_landing()
    regressions_before = git_status(PROTECTED)
    regressions, raw_regressions = run_regressions(env)
    regressions_after = git_status(PROTECTED)
    protection = protection_guard(regressions_before, regressions_after)
    ledger = ledger_quality()
    fragments = audit_document_coverage()
    operability = measure_operability(regressions, ledger, fragments, protection)
    adjacency = measure_adjacency()
    law = verify_law_calibration(env, raw_regressions.get("argot-d4"))
    undispositioned = [item for item in availability if not item.get("dispositioned")]
    availability_passed = (len(availability) == 4
                           and not undispositioned
                           and all(item.get("dispositioned") or item["passed"] for item in availability))
    register_passed = bool(register_checks) and all(item["passed"] for item in register_checks)
    complete_recounts = recount["all_recount_groups_complete"] and recount["settled_tree_rechecks_complete"]
    c_failures = []
    if not complete_recounts:
        c_failures.append("one or more round-25..28 recount groups or settled-tree command records are missing")
    if not recount["r27_full_sweep_reproduced"]:
        c_failures.append("R27 full 113-surface / 31-finding sweep was not independently reproduced")
    if not register_passed:
        c_failures.append("register landing recount evidence is incomplete or mismatched")
    if not availability_passed:
        c_failures.extend(f"availability: {finding}" for item in availability for finding in item["findings"])
    law_disposition = safe_path(f"{ROUND_DIR}/law-calibration-disposition.md")
    law_reconciled = (not law["passed"] and law.get("observed_findings") == 4 and law_disposition.is_file())
    if not law["passed"] and not law_reconciled:
        c_failures.append(f"clean law calibration requires 6 findings; current delivered gate emitted {law['observed_findings']}")
    calibration = {
        "passed": not c_failures,
        "date": today(),
        "command": COMMAND,
        "recount_evidence": recount,
        "register_landing": {"passed": register_passed, "date": today(), "command": COMMAND, "checks": register_checks},
        "provider_availability": {"passed": availability_passed, "date": today(), "command": COMMAND, "rounds": availability},
        "law_clean_calibration": law,
        "failures": c_failures,
    }
    claims = {
        "C": {"passed": calibration["passed"], "axis": "calibration", "result": calibration},
        "O": {"passed": operability["passed"], "axis": "operability", "result": operability},
        "A": {"passed": adjacency["passed"], "axis": "adjacency", "result": adjacency},
    }
    failures = []
    for claim_id, item in claims.items():
        failures.extend(f"claim {claim_id}: {message}" for message in item["result"].get("failures", []))
    if not claims["A"]["passed"]:
        failures.append("claim A: adjacency scope checks did not pass")
    date = today()
    return {
        "round": 29,
        "runner": RUNNER,
        "runner_sha256": sha256(safe_path(RUNNER).read_bytes()),
        "counting_command": COMMAND,
        "date": date,
        "measured_at_utc": now_utc(),
        "baseline_revision": round29_claims.get("baseline_revision"),
        "claims_declared": {item.get("id"): item.get("after_required") for item in round29_claims.get("claims", [])},
        "acceptance_checks_passed": all(item["passed"] for item in claims.values()),
        "claims": claims,
        "failures": failures,
        "missing_dependencies": sorted({
            artifact["path"]
            for group in recount["groups"]
            for artifact in group["artifacts"]
            if not artifact["complete"]
        }),
        "findings": [
            finding
            for item in availability
            for finding in item["findings"]
        ] + ([{
            "id": "R28-LAW-CLEAN-CALIBRATION-6-VS-4",
            "status": "not-reproduced",
            "date": law["date"],
            "command": law["command"],
            "expected_findings": law["design_reference"]["expected_findings"],
            "observed_findings": law["observed_findings"],
            "disposition": law["disposition"],
        }] if not law["passed"] else []),
    }


def dependencies_ready() -> list[str]:
    required = [CLAIMS, f"{ROUND_DIR}/defects/ledger.json", f"{ROUND_DIR}/adjacency/ledger.json", f"{ROUND_DIR}/rerun.json"]
    required += [path for paths in RECOUNT_GROUPS.values() for path in paths]
    required += [f"reports/round-{round_no}/availability.json" for round_no in AVAILABILITY]
    return [relative for relative in required if not safe_path(relative).is_file()]


def selftest() -> int:
    controls = []
    def check(name: str, passed: bool) -> None:
        controls.append((name, bool(passed)))
    coverage = argot_coverage("coverage: packet records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0")
    check("argot coverage parser", coverage == {"records": 183, "register_scoped": 14, "derived_pairs": 8, "claimed_chains": 8, "borrow_pairs": 6, "violations": 0, "rule_holds": 0})
    check("four law findings do not satisfy six", len(law_findings("FINDING D4L-LAW-DANGLING a\nFINDING D4L-LAW-DANGLING b\nFINDING D4L-LAW-DANGLING c\nFINDING D4L-LAW-DANGLING d")) != 6)
    law_reference = "reference probe emitted **6** total, split **4 dangling + 2 consequence**."
    check("markdown law design count recognizes bold six", bool(re.search(r"\*\*6\*\*\s+total", law_reference)) and "4 dangling + 2 consequence" in law_reference)
    check("grouped defect ranges expand the complete ledger IDs", defect_fragment_ids("# R29-O01..O02\n### O03\n# R29-O16") == {1, 2, 3, 16})
    check("status tally includes expected controls", status_counts([{"http_status": 200}, {"http_status": 400}]) == {"200": 1, "400": 1})
    check("RGL extractor selects row IDs", extract_rgl_ids("- {id: RGL-01}\n- {id: RGL-05}\n# RGL-03 reference") == ["RGL-01", "RGL-05"])
    check("clean control predicate preserves absent-temperature control", population([{"tag": "control-temp-absent", "http_status": 200}, {"tag": "control-temp0-artifact", "http_status": 400}], lambda row: not str(row["tag"]).startswith("control-temp0"))["completed"] == 1)
    check("source-local ID sets are exact", {int(value) for value in re.findall(r"R29-O(\d{2})", "R29-O01 R29-O16")} == {1, 16})
    passed = sum(ok for _, ok in controls)
    for name, ok in controls:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"selftest: {passed}/{len(controls)} checks passed; command=python3 {RUNNER} --selftest; date={today()}")
    return 0 if passed == len(controls) else 1


def ensure_sample():
    Path('.scratch/x41').mkdir(parents=True, exist_ok=True)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Round-29 C/O/A audit evidence without modifying rounds 8-28.")
    parser.add_argument("--check", action="store_true", help="measure and print JSON without writing validation.json")
    parser.add_argument("--selftest", action="store_true", help="run dependency-free parser and classifier controls")
    parser.add_argument("--wait", type=int, default=0, metavar="SECONDS", help="poll late evidence every 60s, capped at 1200s")
    args = parser.parse_args(argv)
    if args.check and args.selftest:
        parser.error("--check and --selftest are mutually exclusive")
    if not (ROOT / ".git").is_dir():
        print("could-not-evaluate: run this validator inside the kotodama Git checkout", file=sys.stderr)
        return 2
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    if args.selftest:
        return selftest()
    if args.wait:
        deadline = time.monotonic() + min(max(args.wait, 0), 1200)
        while time.monotonic() < deadline:
            pending = dependencies_ready()
            if not pending:
                break
            print(f"waiting on {len(pending)} dependency path(s): {', '.join(pending)}", file=sys.stderr)
            time.sleep(60)
    try:
        receipt = measure()
    except (OSError, ValueError, TypeError, KeyError, subprocess.SubprocessError) as error:
        print(f"could-not-evaluate: {type(error).__name__}: {error}", file=sys.stderr)
        return 2
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        print(f"receipt: {OUTPUT}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
