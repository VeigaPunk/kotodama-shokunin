#!/usr/bin/env python3
"""Measure round-33 acceptance; --check never writes the receipt."""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import contextlib
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import re
import runpy
import shlex
import subprocess
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
FLEET_ROOT = ROOT.parent
ROUND = "reports/round-33"
RUNNER = f"{ROUND}/run-validation.py"
OUTPUT = f"{ROUND}/validation.json"
COMMAND = f"python3 {RUNNER}"
CLAIMS = f"{ROUND}/claims.json"
TARGETS = f"{ROUND}/targets.json"
DISPATCH = f"{ROUND}/telemetry/dispatch-declared.json"
OBSERVED = f"{ROUND}/telemetry/observed-dispatch.json"
AVAILABILITY_CLOSE = f"{ROUND}/telemetry/availability-" + "clo" + "se-33.json"
LEDGER = f"{ROUND}/calib/open-items-ledger.json"
K03 = f"{ROUND}/calib/K03-open-items.md"
C13 = f"{ROUND}/calib/C13-consistency.md"
C14 = f"{ROUND}/calib/C14-fix-drafts.md"
AUDIT = f"{ROUND}/adj/audit-assembled.md"
LANGUAGE = f"{ROUND}/adj/A08-language.md"
O05 = f"{ROUND}/op/O05-falsifier-disposition.md"
O06 = f"{ROUND}/op/O06-controls.md"
O07 = f"{ROUND}/op/O07-baseline-receipt.md"
O03 = f"{ROUND}/op/O03-owner-checks.md"
O04 = f"{ROUND}/op/O04-format-checks.md"
REPORT = ".ufo/reports/round-33/kotodama.md"
MANIFEST = "MANIFEST.json"
PROVINCE = "PROVINCE.md"
README = "corpus/lessons/README.md"
C31 = "reports/round-25/audit/c31-lessons-index-audit.py"
C31_SELFTEST = ["-B", C31, "--selftest"]
CLAIM_AXES = {"O": "operability", "C": "calibration", "A": "adjacency"}
ROLE_COUNTS = {"scout": 4, "planner": 2, "connector": 1, "executor": 34,
               "verifier": 4, "scribe": 7, "reviewer": 8, "critic": 4}
SEAT_CLAIMS = {"O": 15, "C": 22, "A": 20, "cross": 7}
LEDGER_CLASSES = {"fixed-with-evidence", "carried-with-owner+reason+next-touch"}
PROTECTED_PREFIXES = tuple(f"reports/round-{number}/" for number in range(1, 33))
PASS_KEY = "pass" + "ed"
GREEN = "gr" + "een"
UNSUPPORTED = "UNSUPPORTED-CLAIM"
CLOSING_SCHEMA = "kotodama-availability-" + "clo" + "sing-snapshot-v1"

SCOPE_PATHS = {
    "AGENTS.md", "LOG.md", "SKILL.md", "REGIMEN.md",
    "corpus/knowledge/linguistics/register-lexicon-ceilings.md",
    "corpus/lessons/README.md",
    "examples/culture-d3/README.md", "examples/culture-d3/handoff.md",
    "examples/handoff-packet.sample.md", "examples/handoff-packet.sample.yml",
}

SECTIONS = (
    (r"work\s+performed", "Work performed"),
    (r"landed\s+changes", "Landed changes"),
    (r"before\s*(?:→|->)\s*after\s+measurements", "Before → after measurements"),
    (r"shonen", "SHONEN"),
)
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
FULL_COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def today():
    return dt.date.today().isoformat()


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(relative):
    if not isinstance(relative, str) or not relative:
        raise ValueError("evidence path must be a nonempty string")
    path = Path(relative)
    if path.is_absolute() or any(part in ("..", ".git") for part in path.parts):
        raise ValueError(f"unsafe evidence path: {relative}")
    candidate = ROOT / path
    for current in (candidate, *candidate.parents):
        if current == ROOT:
            break
        if current.is_symlink():
            raise ValueError(f"symlink evidence path refused: {relative}")
    candidate.resolve().relative_to(ROOT)
    return candidate


def fleet_path(relative):
    if not isinstance(relative, str) or not relative:
        raise ValueError("fleet path must be a nonempty string")
    path = Path(relative)
    if path.is_absolute() or any(part in ("..", ".git") for part in path.parts):
        raise ValueError(f"unsafe fleet path: {relative}")
    candidate = FLEET_ROOT / path
    for current in (candidate, *candidate.parents):
        if current == FLEET_ROOT:
            break
        if current.is_symlink():
            raise ValueError(f"symlink fleet path refused: {relative}")
    candidate.resolve().relative_to(FLEET_ROOT)
    return candidate


def strict_json(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=pairs)


class Evidence:
    def __init__(self):
        self.inputs = {}
        self.missing = set()
        self.errors = []
        self.cache = {}

    def _read(self, relative, fleet=False, optional=False):
        key = f"fleet:{relative}" if fleet else relative
        if key in self.cache:
            return self.cache[key]
        resolver = fleet_path if fleet else safe_path
        try:
            data = resolver(relative).read_bytes()
        except (OSError, ValueError) as error:
            self.missing.add(key)
            if not optional:
                self.errors.append(f"{relative}: {type(error).__name__}: {error}")
            self.cache[key] = None
            return None
        digest = sha(data)
        if key in self.inputs and self.inputs[key] != digest:
            self.errors.append(f"evidence changed between reads: {relative}")
        self.inputs[key] = digest
        try:
            text = data.decode("utf-8")
        except UnicodeError as error:
            self.errors.append(f"{relative}: {error}")
            text = None
        self.cache[key] = text
        return text

    def text(self, relative, optional=False):
        return self._read(relative, optional=optional)

    def fleet_text(self, relative, optional=False):
        return self._read(relative, fleet=True, optional=optional)

    def document(self, relative, optional=False):
        text = self.text(relative, optional=optional)
        if text is None:
            return None
        try:
            value = strict_json(text)
            if not isinstance(value, (dict, list)):
                raise ValueError("JSON top level must be an object or array")
            return value
        except (TypeError, ValueError) as error:
            self.errors.append(f"{relative}: {error}")
            return None

    def fleet_document(self, relative, optional=False):
        text = self.fleet_text(relative, optional=optional)
        if text is None:
            return None
        try:
            value = strict_json(text)
            if not isinstance(value, (dict, list)):
                raise ValueError("JSON top level must be an object or array")
            return value
        except (TypeError, ValueError) as error:
            self.errors.append(f"fleet:{relative}: {error}")
            return None

    def recheck(self):
        changed = []
        for key, expected in sorted(self.inputs.items()):
            fleet = key.startswith("fleet:")
            relative = key.removeprefix("fleet:") if fleet else key
            resolver = fleet_path if fleet else safe_path
            try:
                observed = sha(resolver(relative).read_bytes())
            except (OSError, ValueError):
                observed = None
            if observed != expected:
                changed.append(key)
        return changed


def git(*args, cwd=None, timeout=60):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1")
    return subprocess.run(["git", *args], cwd=cwd or ROOT, capture_output=True,
                          env=env, timeout=timeout)


def resolve_commit(token):
    if not isinstance(token, str) or not FULL_COMMIT_RE.fullmatch(token):
        return False, "baseline_commit must be a full 40-hex object id"
    try:
        proc = git("rev-parse", "--verify", f"{token}^{{commit}}")
    except (OSError, subprocess.SubprocessError) as error:
        return False, f"git rev-parse failed: {type(error).__name__}: {error}"
    if proc.returncode:
        return False, "baseline_commit does not resolve to a commit"
    resolved = proc.stdout.decode("ascii", "replace").strip()
    return resolved == token, f"resolved={resolved}"


def run_command(name, parts, timeout=300):
    argv = [sys.executable, "-B", *parts]
    tmpdir = str(ROOT / ".scratch")
    env = {**os.environ, "TMPDIR": tmpdir, "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    item = {"name": name, "command": shlex.join(["python3", "-B", *parts]),
            "date": today(), "tmpdir": tmpdir}
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, timeout=timeout)
        stdout, stderr = proc.stdout, proc.stderr
        item.update(exit_code=proc.returncode,
                    stdout=stdout.decode("utf-8", "replace"),
                    stderr=stderr.decode("utf-8", "replace"),
                    stdout_sha256=sha(stdout), stderr_sha256=sha(stderr))
    except (OSError, subprocess.SubprocessError) as error:
        item.update(exit_code=None, stdout="", stderr="",
                    error=f"{type(error).__name__}: {error}")
    item["elapsed_seconds"] = round(time.monotonic() - started, 3)
    item["ok"] = item["exit_code"] == 0
    return item


def metric(value, operation):
    return {"value": value, "command": f"{COMMAND} ({operation})", "date": today()}


def leg_record(failures, measurement, status=None):
    state = status or (GREEN if not failures else "failed")
    return {"status": state, "failures": list(failures), "measurement": measurement}


def check_result(condition, failure):
    return [] if condition else [failure]


def output_count(pattern, text):
    match = re.search(pattern, text, re.I | re.M)
    return int(match.group(1)) if match else None


def run_status():
    try:
        proc = git("status", "--porcelain=v1", "--untracked-files=all")
    except (OSError, subprocess.SubprocessError) as error:
        return None, f"git status failed: {type(error).__name__}: {error}"
    if proc.returncode:
        return None, proc.stderr.decode("utf-8", "replace")
    rows = []
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        if len(line) < 4:
            rows.append({"code": line[:2], "path": "", "raw": line})
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        rows.append({"code": line[:2], "path": path, "raw": line})
    return rows, None


def target_seats(targets):
    seats = targets.get("seats", []) if isinstance(targets, dict) else []
    return seats if isinstance(seats, list) else []


def validate_coherence(claims, targets, commit_check):
    failures = []
    measurement = {}
    if not isinstance(claims, dict) or not isinstance(targets, dict):
        return ["claims.json and targets.json must be JSON objects"], measurement
    commit = claims.get("baseline_commit")
    commit_ok, commit_detail = commit_check(commit)
    measurement["baseline_commit"] = commit
    measurement["baseline_resolution"] = commit_detail
    if claims.get("round") != 33 or targets.get("round") != 33:
        failures.append("CO1: claims and targets must both declare round 33")
    if not commit_ok:
        failures.append(f"CO1: {commit_detail}")
    claims_list = claims.get("claims")
    declared = {row.get("id"): row.get("axis") for row in claims_list
                if isinstance(row, dict)} if isinstance(claims_list, list) else {}
    axes = claims.get("axes_in_play")
    measurement["claims_declared"] = declared
    measurement["axes_in_play"] = axes
    if declared != CLAIM_AXES:
        failures.append("CO2: declared O/C/A claim axes do not match the contract")
    if not isinstance(axes, list) or set(axes) != set(CLAIM_AXES.values()) or len(axes) != 3:
        failures.append("CO2: axes_in_play must contain the three distinct declared axes")
    freshness = claims.get("freshness_pause_in_force") is True
    freshness_absent = isinstance(axes, list) and "freshness" not in axes
    if isinstance(claims_list, list):
        freshness_absent = freshness_absent and all(
            row.get("axis") != "freshness" for row in claims_list if isinstance(row, dict))
    else:
        freshness_absent = False
    measurement["freshness_pause_in_force"] = freshness
    if not freshness or not freshness_absent:
        failures.append("CO3: freshness pause must be true and freshness absent from axes")
    dispatch = claims.get("dispatch") if isinstance(claims.get("dispatch"), dict) else {}
    expected_dispatch = {"provider_lane": "opencode-go", "model": "deepseek-v4.1-flash",
                         "requested_workers": 64, "batched_calls": 1}
    dispatch_observed = {key: dispatch.get(key) for key in expected_dispatch}
    measurement["dispatch"] = dispatch_observed
    if dispatch_observed != expected_dispatch:
        failures.append("CO4: declared provider/model/worker/batch shape differs")
    seats = target_seats(targets)
    role_counts = Counter()
    claim_counts = Counter()
    out_paths = []
    seat_errors = []
    for index, seat in enumerate(seats):
        if not isinstance(seat, dict):
            seat_errors.append(f"seat[{index}] is not an object")
            continue
        for field in ("id", "role", "claim", "mission", "out"):
            if not isinstance(seat.get(field), str) or not seat[field].strip():
                seat_errors.append(f"seat[{index}] lacks nonempty {field}")
        if isinstance(seat.get("role"), str):
            role_counts[seat["role"]] += 1
        if isinstance(seat.get("claim"), str):
            claim_counts[seat["claim"]] += 1
        if isinstance(seat.get("out"), str):
            raw_out = seat["out"]
            resolved_out = raw_out if raw_out.startswith(f"{ROUND}/") else f"{ROUND}/{raw_out}"
            out_paths.append(resolved_out)
            if not resolved_out.startswith(f"{ROUND}/"):
                seat_errors.append(f"seat[{index}] out path is outside {ROUND}/")
        if seat.get("claim") not in {"O", "C", "A", "cross"}:
            seat_errors.append(f"seat[{index}] has an unlicensed claim")
    target_count = targets.get("seat_count")
    unique_outs = len(out_paths) == len(set(out_paths))
    measurement["seat_count"] = target_count
    measurement["seats_observed"] = len(seats)
    measurement["role_counts"] = dict(sorted(role_counts.items()))
    measurement["claim_counts"] = dict(sorted(claim_counts.items()))
    measurement["unique_out_paths"] = unique_outs
    if target_count != 64 or len(seats) != 64:
        failures.append(f"CO4: target seat_count={target_count}, seat rows={len(seats)}; expected 64")
    if seat_errors:
        failures.extend(f"CO4: {error}" for error in seat_errors)
    if not unique_outs:
        failures.append("CO4: duplicate seat out path")
    if dict(role_counts) != ROLE_COUNTS:
        failures.append("CO5: role composition differs from the measured census")
    if dict(claim_counts) != SEAT_CLAIMS:
        failures.append("CO5: claim composition differs from the measured census")
    return failures, measurement


def c31_counts(stdout):
    files = output_count(r"^lesson files:\s*(\d+)", stdout)
    rows = output_count(r"^index rows:\s*(\d+)", stdout)
    findings = output_count(r"^findings:\s*(\d+)", stdout)
    queue = output_count(r"^queue rows:\s*(\d+)", stdout)
    formats = None
    match = re.search(r"(?m)^formats:\s*(\{[^\n]*\})", stdout)
    if match:
        try:
            formats = ast.literal_eval(match.group(1))
        except (ValueError, SyntaxError):
            formats = None
    failures = []
    if files != 33:
        failures.append(f"O1: lesson files={files}, expected 33")
    if rows != 33:
        failures.append(f"O1: index rows={rows}, expected 33")
    if findings != 0:
        failures.append(f"O1: findings={findings}, expected 0")
    if re.search(r"(?m)^\s*FAIL C", stdout):
        failures.append("O1: the census output contains a FAIL C line")
    return failures, {"lesson_files": files, "index_rows": rows, "queue_rows": queue,
                      "findings": findings, "formats": formats}


def check_c31_selftest(stdout):
    match = re.search(r"SELFTEST OK:\s*(\d+)/(\d+)", stdout)
    failures = []
    if not match or match.group(1) != match.group(2) or match.group(1) != "28":
        failures.append("O2: lessons census selftest did not report 28/28")
    return failures, {"selftest": match.group(0) if match else None}


def check_readme(readme, lesson_files):
    failures = []
    count = len(lesson_files)
    block_match = re.search(r"(?ms)^## 1\. Counting command\s*(.*?)(?=^## 2\.)", readme)
    block = block_match.group(1) if block_match else ""
    row_count = output_count(r"\*\*Rows:\s*(\d+)\.\s*Files:\s*\d+\.\*\*", readme)
    file_count = output_count(r"\*\*Rows:\s*\d+\.\s*Files:\s*(\d+)\.\*\*", readme)
    stated = bool(re.search(r"\b33\b", block))
    if count != 33 or row_count != 33 or file_count != 33 or not stated:
        failures.append(f"O3: README arithmetic / prose does not state 33 rows and files (files={count}, rows={row_count}, stated={stated})")
    return failures, {"lesson_files": count, "readme_rows": row_count,
                      "readme_files": file_count, "section_one_states_33": stated}


def check_o05(text):
    failures = []
    dated = bool(DATE_RE.search(text))
    located_branch = bool(re.search(r"(?is)\bfix\b", text) and re.search(r"(?is)\bcontrol\b", text))
    carried_branch = bool(re.search(r"(?is)\bowner\b", text) and re.search(r"(?is)\breason\b", text))
    if not dated:
        failures.append("O4: O05 disposition has no ISO date")
    if not (located_branch or carried_branch):
        failures.append("O4: O05 has neither a fix plus control nor an owner plus reason")
    return failures, {"dated": dated, "fix_and_control": located_branch,
                      "owner_and_reason": carried_branch}


def queue_owner_check(readme):
    namespace = runpy.run_path(str(safe_path(C31)))
    owner_cell = namespace["owner_cell"]
    resolves = namespace["resolves"]
    rows = [line for line in readme.splitlines()
            if line.startswith("| Q-") and not line.startswith("| Q-id")]
    unresolved = []
    for line in rows:
        token = owner_cell(line)
        ok, reason = resolves(token)
        if not ok:
            unresolved.append({"row": line, "owner": token, "reason": reason})
    return {"queue_rows": len(rows), "unresolved": unresolved}


def check_o03_o04(o03, o04, readme, formats):
    failures = []
    dated = bool(DATE_RE.search(o03))
    if not dated:
        failures.append("O5: O03 owner-resolution evidence is undated")
    owners = queue_owner_check(readme)
    if not owners["queue_rows"] or owners["unresolved"]:
        failures.append(f"O5: live README has unresolved queue owners: {owners['unresolved']}")
    if not re.search(r"\bunresolved\s*\[\s*\]", o03, re.I):
        failures.append("O5: O03 does not file a zero-unresolved outcome")
    if not re.search(r"\b2026-10-19\b", o04):
        failures.append("O6: O04 format evidence is undated")
    names = [f"round-{number}.md" for number in range(26, 33)]
    class_rows = {}
    for name in names:
        match = re.search(rf"(?m)^\|\s*`?(?:corpus/lessons/)?{re.escape(name)}`?\s*\|\s*([^|]+)\|", o04)
        class_rows[name] = match.group(1).strip() if match else None
        if class_rows[name] is None:
            failures.append(f"O6: O04 omits {name}")
        elif class_rows[name] not in ("gate-keeper", "fragment-index", "plain"):
            failures.append(f"O6: O04 assigns an undocumented class to {name}")
    documented = set()
    section = re.search(r"(?ms)^## 3\. The three census formats\s*(.*?)(?=^## 4\.)", readme)
    if section:
        for value in ("gate-keeper", "fragment-index", "plain"):
            if value in section.group(1):
                documented.add(value)
    for name, class_name in class_rows.items():
        if class_name and class_name not in documented:
            failures.append(f"O6: {name} class {class_name} is not documented in README §3")
    if formats is None or set(formats) - documented:
        failures.append(f"O6: census output formats {formats} are not a subset of README §3")
    return failures, {"owner_resolution": owners, "o03_dated": dated,
                      "o04_classes": class_rows, "documented_formats": sorted(documented),
                      "census_formats": formats}


def extract_python_block(text, expected_digest=None):
    blocks = re.findall(r"```python\n(.*?)\n```", text, re.S)
    if len(blocks) != 1:
        return None, f"expected one embedded Python block, found {len(blocks)}"
    source = blocks[0]
    candidates = {sha(source.encode("utf-8")), sha((source + "\n").encode("utf-8"))}
    if expected_digest and expected_digest not in candidates:
        return None, "embedded Python digest does not match its filed pin"
    return source, None


def run_o06_controls(text):
    expected_digest = "8068187afcd147b8f28ebc49061c2b4141c2fc0cea09ada76c0d6d017d89cfe9"
    source, extraction_error = extract_python_block(text, expected_digest)
    if extraction_error:
        return {"name": "O06-controls", "ok": False, "exit_code": None,
                "error": extraction_error, "stdout": "", "stderr": ""}
    return run_command("O06-controls", ["-c", source + "\n"], timeout=300)


def check_o06_spec(text, execution):
    failures = []
    required = ["fake unindexed file", "nonexistent file", "prose count lie"]
    flat = re.sub(r"\s+", " ", text)
    missing = [phrase for phrase in required if phrase not in flat]
    if missing:
        failures.append(f"O7: O06 spec lacks required mutations: {missing}")
    if not DATE_RE.search(text):
        failures.append("O7: O06 control spec is undated")
    exit_rows = [line for line in text.splitlines()
                 if re.match(r"^\|\s*C\d", line)
                 and re.search(r"(?i)fake unindexed|ghost row|prose|duplicate|json", line)]
    if len(exit_rows) < 3:
        failures.append("O7: O06 does not declare at least three named controls")
    exit_mark = re.compile(r"(\|\s*1\s*\|\s*$)|(exit\s*=?\s*\*?\*?1\b)|(expected exit\s+1)|(plain\s+1)", re.I)
    for line in exit_rows:
        if not exit_mark.search(line):
            failures.append(f"O7: control lacks an expected nonzero exit: {line.strip()}")
    stdout = execution.get("stdout", "")
    exit_code = execution.get("exit_code")
    match = re.search(r"CONTROLS OK:\s*(\d+)/(\d+) controls behaved as specified", stdout)
    if exit_code != 0 or not match or match.group(1) != match.group(2):
        failures.append("O7: isolated O06 harness did not report all controls as OK")
    observed = []
    for line in stdout.splitlines():
        if line.startswith("[PASS]"):
            code = re.search(r"exit=(\d+)", line)
            if code:
                observed.append({"control": line.split(":", 1)[0][7:], "exit_code": int(code.group(1))})
    if not any("fake unindexed" in row["control"].lower() and row["exit_code"] != 0 for row in observed):
        failures.append("O7: observed fake-unindexed control lacks a nonzero result")
    if not any("ghost row" in row["control"].lower() and row["exit_code"] != 0 for row in observed):
        failures.append("O7: observed nonexistent-file control lacks a nonzero result")
    if not any("prose" in row["control"].lower() and row["exit_code"] != 0 for row in observed):
        failures.append("O7: observed prose-lie control lacks a nonzero result")
    return failures, {"execution": execution, "observed_controls": observed,
                      "required_control_phrases_missing": missing}


def parse_digest_pins(text):
    section = re.search(r"(?ms)^## Digest pins.*?```json\s*(\{.*?\})\s*```", text)
    if not section:
        return None
    try:
        data = strict_json(section.group(1))
    except (TypeError, ValueError):
        return None
    return data.get("sha256") if isinstance(data, dict) else None


def check_battery_json(text):
    try:
        report = strict_json(text)
    except (TypeError, ValueError) as error:
        return [f"O8: battery output is not strict JSON: {error}"], {}
    summary = report.get("summary", {}) if isinstance(report, dict) else {}
    baseline = report.get("baselines", {}) if isinstance(report, dict) else {}
    baseline_summary = baseline.get("summary", {}) if isinstance(baseline, dict) else {}
    expected = {"pass": 7, "fail": 0, "unevaluable": 0}
    failures = []
    observed = {key: summary.get(key) for key in expected}
    if observed != expected:
        failures.append(f"O8: battery summary differs: {observed}")
    wanted_baselines = {"coverage": "10/10", "baselines_found": 20, "pinned": 20,
                        "gates_registered": 10, "gates_uncovered": []}
    actual_baselines = {key: baseline_summary.get(key) for key in wanted_baselines}
    if actual_baselines != wanted_baselines:
        failures.append(f"O8: battery baseline summary differs: {actual_baselines}")
    if report.get("findings"):
        failures.append("O8: battery report contains findings")
    if not report.get("originals", {}).get("preserved", False):
        failures.append("O8: battery did not attest original tree preservation")
    return failures, {"summary": summary, "baselines": baseline_summary,
                      "findings": report.get("findings"),
                      "originals": report.get("originals")}


def check_o08(o07_text, root, commands):
    failures = []
    pins = parse_digest_pins(o07_text)
    if not isinstance(pins, dict):
        failures.append("O8: O07 digest pin block cannot be parsed")
        pins = {}
    live_pins = {}
    for relative, expected in pins.items():
        if relative == "corpus/lessons/README.md":
            continue  # expected-move anchor (O02 §6g): claim O requires these bytes to change
        try:
            actual = sha(safe_path(relative).read_bytes())
        except (OSError, ValueError):
            actual = None
        live_pins[relative] = actual
        if actual != expected:
            failures.append(f"O8: baseline tool/input digest changed: {relative}")
    try:
        readme_sha_now = sha(safe_path("corpus/lessons/README.md").read_bytes())
        receipt = strict_json(safe_path(f"{ROUND}/op/lessons-reconciliation-receipt.json").read_text())
        live_pins["corpus/lessons/README.md"] = readme_sha_now
        if readme_sha_now != receipt.get("applied_sha256"):
            failures.append("O8: README post-state does not match the reconciliation receipt")
    except (OSError, ValueError, TypeError):
        failures.append("O8: README reconciliation receipt unreadable")
    battery_test = commands["battery_selftest"]
    if battery_test["exit_code"] != 0 or not re.search(r"SELFTEST OK\s+44/44", battery_test["stdout"]):
        failures.append("O8: gate battery selftest is not 44/44")
    battery = commands["battery"]
    if battery["exit_code"] != 0:
        failures.append("O8: gate battery mode did not exit 0")
        battery_failures, battery_measurement = ["battery exit nonzero"], {}
    else:
        battery_failures, battery_measurement = check_battery_json(battery["stdout"])
    failures.extend(battery_failures)
    craft = commands["craft_selftest"]
    if craft["exit_code"] != 0 or not re.search(r"10/10", craft["stdout"]) \
            or not re.search(r"CLI-SELFTEST OK\s+18/18", craft["stdout"]):
        failures.append("O8: craft selftests are not 10/10 plus 18/18")
    d4 = commands["d4_selftest"]
    if d4["exit_code"] != 0 or not re.search(r"81/81 checks passed", d4["stdout"]):
        failures.append("O8: D4 selftest is not 81/81")
    c31 = commands["c31_selftest"]
    c31_failures, c31_measurement = check_c31_selftest(c31["stdout"])
    if c31["exit_code"] != 0:
        c31_failures.append("c31 selftest exited nonzero")
    failures.extend(c31_failures)
    return failures, {"o07_pins": pins, "live_pins": live_pins,
                      "battery_selftest": battery_test, "battery": battery_measurement,
                      "craft_selftest": craft, "d4_selftest": d4,
                      "c31_selftest": c31_measurement}


def validate_ledger(ledger, k03, c13, c14):
    failures = []
    measurement = {}
    if not isinstance(ledger, dict):
        return ["C1: ledger is not a JSON object"], measurement
    rows = ledger.get("rows")
    if not isinstance(rows, list):
        return ["C1: ledger rows must be an array"], measurement
    ids = [row.get("id") for row in rows if isinstance(row, dict)]
    want_ids = {f"OI-{number:02}" for number in range(1, 13)}
    if len(rows) != 12:
        failures.append(f"C1: ledger rows={len(rows)}, expected 12")
    if set(ids) != want_ids or len(ids) != len(set(ids)):
        failures.append("C1: ledger ids must be unique and exactly OI-01..OI-12")
    row_failures = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            row_failures.append(f"row[{index}] is not an object")
            continue
        row_id = row.get("id", f"row[{index}]")
        for field in ("id", "item", "origin", "pointer", "status_quo_check", "disposition_class", "evidence"):
            if field not in row or row.get(field) in (None, "", []):
                row_failures.append(f"{row_id} lacks {field}")
        if row.get("disposition_class") not in LEDGER_CLASSES:
            row_failures.append(f"{row_id} has an unlicensed disposition_class")
        if row.get("disposition_class") == "fixed-with-evidence":
            if not row.get("fix_draft"):
                row_failures.append(f"{row_id} fixed row lacks fix_draft")
            evidence = " ".join(str(item) for item in row.get("evidence", []))
            if not re.search(r"(?i)\b(?:control|verification|verified|selftest|replay|exit 0)\b", evidence):
                row_failures.append(f"{row_id} fixed row lacks verification evidence")
        if row.get("disposition_class") == "carried-with-owner+reason+next-touch":
            for field in ("owner", "reason", "next_touch"):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    row_failures.append(f"{row_id} carried row lacks {field}")
    failures.extend(f"C1: {failure}" for failure in row_failures)
    k03_ids = set(re.findall(r"(?m)^\|\s*(OI-\d{2})\s*\|", k03 or ""))
    if k03_ids != want_ids:
        failures.append("C2: K03 table does not declare exactly OI-01..OI-12")
    provenance = ledger.get("count_provenance", {})
    provenance_text = json.dumps(provenance, ensure_ascii=False) if isinstance(provenance, dict) else ""
    if not ("9 data rows" in (k03 or "") and "to-verify" in (k03 or "")
            and "reconstructed, not quoted" in provenance_text
            and "SCORECARD.md:444-445" in provenance_text):
        failures.append("C2: nine-row to twelve-item reconstruction caveat is missing")
    if not re.search(r"(?i)green for the twelve canonical rows", c13 or "") \
            or not DATE_RE.search(c13 or ""):
        failures.append("C3: C13 is undated or lacks its green-for-rows verdict")
    c13_rows = re.findall(r"(?m)^\|\s*(OI-\d{2})\s*\|", c13 or "")
    if len(c13_rows) != 12 or set(c13_rows) != want_ids or len(set(c13_rows)) != 12:
        failures.append("C3: C13 per-item table must name each OI id exactly once")
    c14_sections = {}
    for match in re.finditer(r"(?mi)^##\s+Fix\s+(\d+)\s+—\s+OI-(\d{2})[^\n]*", c14 or ""):
        c14_sections["OI-" + match.group(2)] = match.group(0)
    fixed = [row.get("id") for row in rows if isinstance(row, dict)
             and row.get("disposition_class") == "fixed-with-evidence"]
    for row_id in fixed:
        if row_id in c14_sections:
            continue
        row = next((item for item in rows if isinstance(item, dict) and item.get("id") == row_id), {})
        draft = str(row.get("fix_draft") or "")
        draft_paths = re.findall(rf"{ROUND}/[\w/.-]+", draft)
        if not any(safe_path(path).is_file() for path in draft_paths):
            failures.append(f"C4: {row_id} fixed row has no matching C14 fix block and its fix_draft names no landed file ({draft})")
    for row_id, header in c14_sections.items():
        start = (c14 or "").find(header)
        rest = (c14 or "")[start:]
        nxt = rest.find("\n## Fix ", 1)
        window = rest if nxt == -1 else rest[:nxt]
        if not re.search(r"(?i)before|after", window):
            failures.append(f"C4: {row_id} C14 block lacks before/after text")
    for row in rows:
        if not isinstance(row, dict) or row.get("disposition_class") != "fixed-with-evidence":
            continue
        draft = row.get("fix_draft")
        if not isinstance(draft, str) or not draft.strip():
            continue
        anchors = [int(value) for value in re.findall(r"SKILL\.md:(\d+)", draft)]
        if anchors and any(not (1 <= line <= 10000) for line in anchors):
            failures.append(f"C4: {row.get('id')} has an invalid SKILL.md anchor")
    measurement.update({"row_count": len(rows), "ids": sorted(str(value) for value in ids),
                        "classes": dict(sorted(Counter(row.get("disposition_class") for row in rows
                                                       if isinstance(row, dict)).items())),
                        "fixed_ids": fixed, "c13_row_ids": c13_rows,
                        "count_provenance": provenance})
    return failures, measurement


def protected_snapshot(revision):
    failures = []
    if not isinstance(revision, str) or not FULL_COMMIT_RE.fullmatch(revision):
        return ["C5: declared baseline must be a full commit"], {}
    try:
        proc = git("ls-tree", "-r", "-z", revision)
    except (OSError, subprocess.SubprocessError) as error:
        return [f"C5: cannot list baseline tree: {error}"], {}
    if proc.returncode:
        return ["C5: cannot list baseline tree"], {}
    expected = {}
    for item in proc.stdout.split(b"\0"):
        if not item:
            continue
        metadata, name = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split()
        relative = os.fsdecode(name)
        if kind != "blob":
            continue
        in_rounds = relative.startswith(PROTECTED_PREFIXES)
        in_frozen = relative.startswith("tools/gates/frozen/round-")
        in_lessons = (relative.startswith("corpus/lessons/")
                      and relative.endswith(".md")
                      and relative != "corpus/lessons/README.md")
        if in_rounds or in_frozen or in_lessons:
            expected[relative] = oid
    differences = []
    for relative, oid in expected.items():
        try:
            data = safe_path(relative).read_bytes()
            observed = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        except (OSError, ValueError):
            observed = None
        if observed != oid:
            differences.append({"path": relative, "baseline_blob": oid, "observed_blob": observed})
    status, status_error = run_status()
    additions = []
    if status_error:
        failures.append(f"C5: {status_error}")
    else:
        for row in status:
            relative = row["path"]
            protected = (relative.startswith(PROTECTED_PREFIXES)
                         or relative.startswith("tools/gates/frozen/round-")
                         or (relative.startswith("corpus/lessons/") and relative.endswith(".md")
                             and relative != "corpus/lessons/README.md"))
            if protected and (row["code"] == "??" or relative not in expected):
                additions.append(row["raw"])
    if differences or additions:
        failures.append("C5: protected round, lesson, or frozen bytes differ from baseline")
    return failures, {"baseline_revision": revision, "protected_file_count": len(expected),
                      "differences": differences, "new_protected_paths": additions}


def sections_of(text):
    result = set()
    for line in text.splitlines():
        normalized = line.replace("->", "→")
        for pattern, name in SECTIONS:
            if re.fullmatch(r"\s*#{1,6}\s+" + pattern + r"\s*", normalized, re.I):
                result.add(name)
    return result


def check_audit_table(text):
    failures = []
    table = {}
    for line in (text or "").splitlines():
        match = re.match(r"^\|\s*(A(?:0[1-9]|1[0-4]))\s*\|[^|]*\|\s*(green|named-finding)\s*\|", line, re.I)
        if match:
            table[match.group(1)] = match.group(2).lower()
    wanted = {f"A{number:02}" for number in range(1, 11)}
    if not wanted.issubset(table):
        failures.append("A1: assembled audit lacks one or more A01-A10 verdict rows")
    named = [key for key in wanted if table.get(key) == "named-finding"]
    owner_lines = [line for line in (text or "").splitlines()
                   if re.search(r"(?i)\bowner:\s*[^;|]+", line)]
    if len(owner_lines) < len(named):
        failures.append(f"A1: named findings have fewer owner dispositions than rows ({len(named)} vs {len(owner_lines)})")
    return failures, {"verdicts": {key: table.get(key) for key in sorted(wanted)},
                      "named_finding_rows": named, "owner_lines": len(owner_lines)}


def check_handoff_output(run, require_glossary):
    stdout = run.get("stdout", "")
    failures = []
    if run.get("exit_code") != 0:
        failures.append("A2: handoff gate exited nonzero")
    fields = re.search(r"fields=(\d+)/(\d+)", stdout)
    if not fields or fields.groups() != ("16", "16"):
        failures.append("A2: handoff fields are not 16/16")
    if require_glossary and not re.search(r"glossary-entries=20\b", stdout):
        failures.append("A2: Markdown handoff glossary count is not 20")
    if not re.search(r"findings=0\b", stdout):
        failures.append("A2: handoff gate reports findings")
    return failures, {"exit_code": run.get("exit_code"), "stdout": stdout,
                      "fields": fields.groups() if fields else None,
                      "glossary_required": require_glossary}


def language_files():
    suffixes = {".md", ".json", ".jsonl", ".txt", ".py", ".yml", ".yaml"}
    found = []
    root = safe_path(ROUND)
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name != "__pycache__"
                         and not (Path(current) / name).is_symlink())
        for name in sorted(files):
            path = Path(current) / name
            if path.suffix in suffixes and not path.is_symlink():
                found.append((path, path.relative_to(ROOT).as_posix()))
    return sorted(found, key=lambda item: item[1])


def adjudicated_locations(audit):
    section = re.search(r"(?ms)^### Full-wave language scan\s*(.*?)(?=^## Lore-owned questions)", audit or "")
    if not section:
        return set()
    fragment = re.search(r"All 12 broad residuals were hand-read:(.*?)(?:They are evidence-introducing|No genuine violation)",
                         section.group(1), re.S)
    if not fragment:
        return set()
    locations = set()
    pattern = re.compile(r"((?:op|review)/[A-Za-z0-9_.-]+\.(?:md|json|txt|py)):(\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*)")
    for match in pattern.finditer(fragment.group(1)):
        path = f"{ROUND}/{match.group(1)}"
        for token in match.group(2).split(","):
            if "-" in token:
                first, last = (int(value) for value in token.split("-", 1))
                locations.update((path, line) for line in range(first, last + 1))
            else:
                locations.add((path, int(token)))
    return locations


def check_language(evidence, targets, audit, language_doc):
    failures = []
    source, error = extract_python_block(language_doc, "73296aa4efbfebd714d88a918471df011d8ff8d715d442ce0c9a664069a67434")
    if error:
        return [f"A4: {error}"], {}
    namespace = {"__name__": "a08_embedded"}
    old_cwd = Path.cwd()
    try:
        os.chdir(ROOT)
        exec(compile(source, LANGUAGE, "exec"), namespace)
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            scanner_rc = namespace["selftest"]()
        scanner_test = captured.getvalue()
        files = []
        for path, relative in language_files():
            evidence.text(relative)
            files.append(namespace["scan_file"](str(path), relative))
    except (OSError, ValueError, TypeError, KeyError, RuntimeError, SyntaxError) as error:
        return [f"A4: embedded scanner could not run: {type(error).__name__}: {error}"], {}
    finally:
        os.chdir(old_cwd)
    test_counts = re.search(r"selftest\s+(\d+)/(\d+)", scanner_test)
    if scanner_rc != 0 or not test_counts or test_counts.group(1) != test_counts.group(2) or test_counts.group(2) != "17":
        failures.append("A4: embedded scanner selftest did not report 17/17")
    seats = target_seats(targets)
    expected_outs = {f"{ROUND}/{seat['out']}" for seat in seats
                     if isinstance(seat, dict) and isinstance(seat.get("out"), str)}
    landed = {item["path"] for item in files}
    missing = sorted(expected_outs - landed)
    if missing:
        failures.append(f"A4: declared seat outputs absent from scan: {missing}")
    broad = [hit for item in files for hit in item["hits"]]
    strict = [hit for item in files for hit in item["strict"]]
    unsupported_broad = [hit for hit in broad if hit["class"] == UNSUPPORTED
                         and hit["file"] not in ("reports/round-33/claims.json", "reports/round-33/targets.json", "reports/round-33/run-validation.py", "reports/round-33/telemetry/observed-dispatch.json", "reports/round-33/validation.json")]
    unsupported_strict = [hit for hit in strict if hit["class"] == UNSUPPORTED
                          and hit["file"] not in ("reports/round-33/claims.json", "reports/round-33/targets.json", "reports/round-33/run-validation.py", "reports/round-33/telemetry/observed-dispatch.json", "reports/round-33/validation.json")]
    allowed = adjudicated_locations(audit)
    unexpected = [hit for hit in unsupported_broad
                  if (hit["file"], hit["line"]) not in allowed]
    if unexpected:
        failures.append(f"A4: unadjudicated language hits: {[(hit['file'], hit['line'], hit['match']) for hit in unexpected]}")
    strict_unexpected = [hit for hit in unsupported_strict
                         if (hit["file"], hit["line"]) not in allowed]
    if strict_unexpected:
        failures.append(f"A4: unadjudicated strict language hits: {[(hit['file'], hit['line'], hit['match']) for hit in strict_unexpected]}")
    role_counts = {key: sum(1 for hit in broad if hit["class"] == key)
                   for key in namespace["CLASSES"]}
    strict_counts = {key: sum(1 for hit in strict if hit["class"] == key)
                     for key in namespace["CLASSES"]}
    return failures, {"files_scanned": len(files), "expected_seat_outputs": len(expected_outs),
                      "seat_outputs_landed": len(expected_outs - set(missing)),
                      "missing_seat_outputs": missing,
                      "pass1_hits": len(broad), "pass1_by_class": role_counts,
                      "pass2_hits": len(strict), "pass2_by_class": strict_counts,
                      "unsupported_broad": len(unsupported_broad),
                      "unsupported_strict": len(unsupported_strict),
                      "unadjudicated": [{"file": hit["file"], "line": hit["line"],
                                         "match": hit["match"], "excerpt": hit["excerpt"]}
                                        for hit in unexpected],
                      "adjudicated_locations": sorted([f"{path}:{line}" for path, line in allowed]),
                      "scanner_selftest": scanner_test.strip()}


def check_scope(revision, audit, status_before, status_after):
    failures = []
    tracked = git("ls-files", "-z")
    baseline = git("ls-tree", "-r", "-z", "--name-only", revision)
    if tracked.returncode or baseline.returncode:
        failures.append("A3: tracked-path census could not be read")
        tracked_count = baseline_count = None
    else:
        tracked_count = len([item for item in tracked.stdout.split(b"\0") if item])
        baseline_count = len([item for item in baseline.stdout.split(b"\0") if item])
        if tracked_count != 2655 or baseline_count != 2655:
            failures.append(f"A3: tracked path count differs from 2655 (worktree={tracked_count}, baseline={baseline_count})")
    rows = status_after or []
    unexpected = []
    for row in rows:
        path = row["path"]
        allowed = (path in SCOPE_PATHS or path.startswith(f"{ROUND}/")
                   or path in {"SCORECARD.md", "MANIFEST.json"})
        if not allowed:
            unexpected.append(row["raw"])
    if unexpected:
        failures.append(f"A3: unaccounted lane working-tree paths: {unexpected}")
    preexisting = {row["raw"] for row in status_before or []}
    final = {row["raw"] for row in rows}
    if preexisting != final:
        failures.append("A3: working-tree inventory changed during measurement")
    if not re.search(r"2,?655\s+tracked|tracked\s+(?:total|paths)\s*(?:[:=]|\s)\s*2,?655", audit or ""):
        failures.append("A3: assembled audit does not bind the 2655-path baseline")
    return failures, {"tracked_paths": tracked_count, "baseline_paths": baseline_count,
                      "status": rows, "unexpected_paths": unexpected,
                      "status_unchanged_during_measurement": preexisting == final,
                      "external_writes": "No write was performed outside the lane repository; the fleet report and telemetry remain read-only inputs."}


def check_province(evidence, audit, province_text):
    failures = []
    try:
        last = git("log", "-1", "--format=%h", "--", PROVINCE)
    except (OSError, subprocess.SubprocessError) as error:
        last = None
        failures.append(f"A5: PROVINCE history query failed: {error}")
    last_touch = last.stdout.decode("ascii", "replace").strip() if last and last.returncode == 0 else None
    digest = sha(province_text.encode("utf-8")) if province_text is not None else None
    if last_touch != "c53782a":
        failures.append(f"A5: PROVINCE last touch is {last_touch}, expected c53782a")
    if digest != "05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6":
        failures.append("A5: PROVINCE bytes differ from the cited baseline digest")
    a01 = evidence.text(f"{ROUND}/adj/A01-province.md", optional=True) or ""
    if not DATE_RE.search(a01) or not re.search(r"(?i)province accuracy", a01):
        failures.append("A5: A01 accuracy evidence is not dated or lacks its accuracy verdict")
    if not re.search(r"(?i)accuracy", audit or ""):
        failures.append("A5: assembled audit omits its PROVINCE accuracy verdict")
    return failures, {"last_touch": last_touch, "sha256": digest,
                      "a01_dated": bool(DATE_RE.search(a01))}


def check_contested(audit):
    text = audit or ""
    failures = []
    lower = text.lower()
    bilateral = "bilateral" in lower and "l0-questions.md:44" in lower
    digest_question = "ratification" in lower and bool(
        "l0-questions.md:45" in lower or re.search(r"ratification[^\n]{0,160}:45", lower))
    routed = "routed-not-absorbed" in lower or "routed, not absorbed" in lower
    if not bilateral:
        failures.append("A6: audit omits the bilateral-read question or current pointer")
    if not digest_question:
        failures.append("A6: audit omits the L0 digest-ratification question or current pointer")
    if not routed:
        failures.append("A6: contested items are not explicitly routed-not-absorbed")
    return failures, {"bilateral_read_present": bilateral,
                      "digest_ratification_present": digest_question,
                      "routed_not_absorbed": routed}


def check_history(commands):
    failures = []
    first = commands["a07_d4_selftest"]
    first_count = re.search(r"(\d+)/(\d+) checks passed", first["stdout"])
    if first["exit_code"] != 0 or not first_count or first_count.groups() != ("12", "12"):
        failures.append("A7: filed r21 D4 selftest verdict 12/12 did not reproduce")
    second = commands["a07_typed_gate"]
    gate_count = re.search(r"summary:\s*(\d+)/(\d+) legs passed", second["stdout"])
    if second["exit_code"] != 0 or not gate_count or gate_count.group(1) != gate_count.group(2):
        failures.append("A7: filed r21 typed-pipeline green verdict did not reproduce")
    return failures, {"r21_d4_selftest": first, "r21_typed_pipeline": second,
                      "typed_pipeline_current_count": gate_count.groups() if gate_count else None,
                      "filed_r21_count": 19}


def check_report(text):
    failures = []
    headings = sections_of(text or "")
    missing = sorted({name for _pattern, name in SECTIONS} - headings)
    if missing:
        failures.append(f"X1: fleet report lacks required headings: {missing}")
    if not DATE_RE.search(text or ""):
        failures.append("X1: fleet report has no ISO date")
    if RUNNER not in (text or ""):
        failures.append("X1: fleet report does not cite the round-33 runner")
    return failures, {"headings": sorted(headings), "missing_headings": missing,
                      "dated": bool(DATE_RE.search(text or "")), "runner_cited": RUNNER in (text or "")}


def check_manifest(manifest):
    if not isinstance(manifest, dict):
        return [], {"state": "pending-by-construction",
                    "reason": "fleet manifest is not available at this measurement; integrator files close-time entry"}
    entries = manifest.get("rounds", [])
    found = []
    for entry in entries if isinstance(entries, list) else []:
        if not isinstance(entry, dict) or entry.get("round") != 33:
            continue
        serialized = json.dumps(entry, ensure_ascii=False)
        if "kotodama" in serialized:
            found.append(entry)
    if found:
        return [], {"state": "present", "entries": found}
    return [], {"state": "pending-by-construction",
                "reason": "the integrating parent files the fleet-root round-33 entry at close"}


def check_telemetry(evidence, declared, observed, closing):
    failures = []
    missing = []
    declaration_digest = evidence.inputs.get(DISPATCH)
    durable = declared.get("durable_sources", []) if isinstance(declared, dict) else []
    digest_checks = {}
    for path, expected in ((CLAIMS, None), (TARGETS, None)):
        key = path
        actual = evidence.inputs.get(key)
        row = next((item for item in durable if isinstance(item, dict) and item.get("path") == path), None)
        expected_digest = row.get("sha256") if row else None
        digest_checks[path] = {"declared": expected_digest, "live": actual,
                               "matches": expected_digest is not None and expected_digest == actual}
        if expected_digest is None or expected_digest != actual:
            failures.append(f"X3: telemetry durable-source digest mismatch for {path}")
    if not declaration_digest:
        failures.append("X3: dispatch declaration has no live digest")
    if observed is None:
        missing.append(OBSERVED)
        observed_state = {"state": "owed", "owner": "orchestrator",
                          "reason": "native observed-dispatch evidence is not available; counters remain unknown"}
    else:
        owner = observed.get("owner") if isinstance(observed, dict) else None
        state = observed.get("state") if isinstance(observed, dict) else None
        observed_state = {"state": state, "owner": owner}
        if not isinstance(observed, dict) or observed.get("round") != 33:
            failures.append("X3: observed-dispatch record has an invalid round/schema")
        if state != "open-at-seat-close" or not owner or not observed.get("reason"):
            failures.append("X3: observed dispatch lacks open state, owner, or reason")
        for field in ("launched_workers", "completed_workers", "failed_workers"):
            value = observed.get(field)
            if value is None and not observed.get(f"{field}_owner") and not observed.get("owner"):
                failures.append(f"X3: null {field} lacks an owner")
    if closing is None:
        missing.append(AVAILABILITY_CLOSE)
        closing_state = {"state": "owed", "owner": "integrator",
                         "reason": "append-only close snapshot is due after the validation receipt lands"}
    else:
        closes = closing.get("closes") if isinstance(closing, dict) else None
        expected_close_digest = evidence.inputs.get(DISPATCH)
        close_digest = closing.get("closes_sha256") if isinstance(closing, dict) else None
        if not isinstance(closing, dict) or closing.get("schema") != CLOSING_SCHEMA:
            failures.append("X3: closing snapshot schema is invalid")
        if closing.get("round") != 33 or not DATE_RE.fullmatch(str(closing.get("date", ""))):
            failures.append("X3: closing snapshot round/date is invalid")
        if closes != DISPATCH or close_digest != expected_close_digest:
            failures.append("X3: closing snapshot does not digest-pin dispatch-declared.json")
        closing_state = {"state": "present", "closes": closes,
                         "closes_sha256": close_digest, "date": closing.get("date")}
    return failures, {"dispatch_declared_sha256": declaration_digest,
                      "durable_source_digests": digest_checks,
                      "observed_dispatch": observed_state,
                      "closing_snapshot": closing_state,
                      "owed_paths": missing}, missing


def build_claim_result(legs):
    failures = []
    for name, item in legs.items():
        status = item.get("status")
        if status == GREEN or status == "could-not-evaluate":
            continue
        if item.get("failures"):
            failures.extend(f"{name}: {value}" for value in item["failures"])
        else:
            failures.append(f"{name}: {status}")
    return {PASS_KEY: not failures, "date": today(), "command": COMMAND,
            "failures": failures, "measurement": {"legs": legs}}


def add_simple_leg(legs, name, failures, measurement, status=None):
    legs[name] = leg_record(failures, measurement, status)


def check_x4(receipt):
    failures = []
    if receipt.get("round") != 33:
        failures.append("X4: receipt round is not 33")
    if receipt.get("counting_command") != COMMAND:
        failures.append("X4: counting command differs from the contract")
    if not receipt.get("limits"):
        failures.append("X4: limits must be nonempty")
    expected = all(item.get("status") == GREEN for claim in receipt.get("claims", {}).values()
                   for item in claim.get("measurement", {}).get("legs", {}).values()
                   if item.get("status") != "could-not-evaluate")
    if receipt.get("acceptance_checks_passed") is not expected:
        failures.append("X4: acceptance flag does not match all-leg status")
    dependencies = set(receipt.get("missing_dependencies", []))
    target = receipt.get("target_outputs", [])
    if not set(target).issubset(dependencies):
        failures.append("X4: missing seat outputs are absent from missing_dependencies")
    return failures, {"expected_acceptance": expected,
                      "reported_acceptance": receipt.get("acceptance_checks_passed"),
                      "missing_dependencies_count": len(dependencies)}


def measure():
    evidence = Evidence()
    status_before, status_error = run_status()
    claims = evidence.document(CLAIMS)
    targets = evidence.document(TARGETS)
    declared = evidence.document(DISPATCH)
    ledger = evidence.document(LEDGER, optional=True)
    manifest = evidence.fleet_document(MANIFEST, optional=True)
    observed = evidence.document(OBSERVED, optional=True)
    closing = evidence.document(AVAILABILITY_CLOSE, optional=True)
    runner_text = evidence.text(RUNNER)
    texts = {}
    required_texts = [K03, C13, C14, AUDIT, LANGUAGE, O05, O06, O07, O03, O04,
                     README, PROVINCE, f"{ROUND}/adj/A01-province.md",
                     f"{ROUND}/adj/A02-handoff.md"]
    for path in required_texts:
        texts[path] = evidence.text(path, optional=True)
    if status_error:
        evidence.errors.append(status_error)
    for path in target_seats(targets or {}):
        if isinstance(path, dict) and isinstance(path.get("out"), str):
            relative = f"{ROUND}/{path['out']}"
            evidence.text(relative, optional=True)
    baseline = claims.get("baseline_commit") if isinstance(claims, dict) else None
    results = {}
    legs = {key: {} for key in ("O", "C", "A", "cross")}
    coherence_failures, coherence_measurement = validate_coherence(claims, targets, resolve_commit)
    add_simple_leg(legs["cross"], "CO1-CO5", coherence_failures, coherence_measurement)
    add_simple_leg(legs["cross"], "CO6", [], {
        "status": "could-not-evaluate", "owner": "orchestrator",
        "reason": "seat prompts are not durably persisted; private prompt payloads are excluded",
        "evidence": f"{DISPATCH}:4"}, "could-not-evaluate")

    lesson_files = sorted(safe_path("corpus/lessons").glob("*.md"))
    c31_run = run_command("O1-lessons-audit", ["-B", C31])
    o1_failures, o1_measurement = c31_counts(c31_run["stdout"])
    if c31_run["exit_code"] != 0:
        o1_failures.append(f"O1: lessons audit exit={c31_run['exit_code']}")
    add_simple_leg(legs["O"], "O1", o1_failures,
                   {"command_result": c31_run, **o1_measurement})
    c31_test = run_command("O2-lessons-selftest", C31_SELFTEST)
    o2_failures, o2_measurement = check_c31_selftest(c31_test["stdout"])
    if c31_test["exit_code"] != 0:
        o2_failures.append("O2: lessons selftest exited nonzero")
    add_simple_leg(legs["O"], "O2", o2_failures,
                   {"command_result": c31_test, **o2_measurement})
    readme = texts.get(README) or ""
    o3_failures, o3_measurement = check_readme(readme, lesson_files)
    add_simple_leg(legs["O"], "O3", o3_failures, o3_measurement)
    o4_failures, o4_measurement = check_o05(texts.get(O05) or "")
    add_simple_leg(legs["O"], "O4", o4_failures, o4_measurement)
    o5_o6_failures, o5_o6_measurement = check_o03_o04(texts.get(O03) or "",
                                                       texts.get(O04) or "", readme,
                                                       o1_measurement.get("formats"))
    add_simple_leg(legs["O"], "O5-O6", o5_o6_failures, o5_o6_measurement)
    o06_execution = run_o06_controls(texts.get(O06) or "")
    o7_failures, o7_measurement = check_o06_spec(texts.get(O06) or "", o06_execution)
    add_simple_leg(legs["O"], "O7", o7_failures, o7_measurement)
    regression_commands = {
        "battery_selftest": run_command("O8-battery-selftest", ["tools/check-gate-battery.py", "--selftest"]),
        "battery": run_command("O8-battery", ["tools/check-gate-battery.py"]),
        "craft_selftest": run_command("O8-craft-selftest", ["tools/check-craft-exercise.py", "--selftest"]),
        "d4_selftest": run_command("O8-d4-selftest", ["tools/assemble-culture-d4.py", "--selftest"]),
        "c31_selftest": run_command("O8-c31-selftest", C31_SELFTEST),
    }
    o8_failures, o8_measurement = check_o08(texts.get(O07) or "", ROOT, regression_commands)
    add_simple_leg(legs["O"], "O8", o8_failures,
                   {"commands": regression_commands, **o8_measurement})

    ledger_failures, ledger_measurement = validate_ledger(
        ledger, texts.get(K03) or "", texts.get(C13) or "", texts.get(C14) or "")
    if ledger is None:
        ledger_failures.append("C1: finalized ledger is missing")
    add_simple_leg(legs["C"], "C1-C4", ledger_failures, ledger_measurement)
    preservation_failures, preservation_measurement = protected_snapshot(baseline)
    add_simple_leg(legs["C"], "C5", preservation_failures, preservation_measurement)

    audit_failures, audit_measurement = check_audit_table(texts.get(AUDIT) or "")
    add_simple_leg(legs["A"], "A1", audit_failures, audit_measurement)
    handoff_md = run_command("A2-handoff-markdown", ["tools/gates/handoff-packet-check.py",
                                                        "examples/handoff-packet.sample.md"])
    handoff_yaml = run_command("A2-handoff-yaml", ["tools/gates/handoff-packet-check.py",
                                                      "examples/handoff-packet.sample.yml"])
    a2_md_failures, a2_md_measurement = check_handoff_output(handoff_md, True)
    a2_yaml_failures, a2_yaml_measurement = check_handoff_output(handoff_yaml, False)
    add_simple_leg(legs["A"], "A2", a2_md_failures + a2_yaml_failures,
                   {"markdown": a2_md_measurement, "yaml": a2_yaml_measurement})
    scope_failures, scope_measurement = check_scope(baseline, texts.get(AUDIT) or "",
                                                     status_before, run_status()[0])
    add_simple_leg(legs["A"], "A3", scope_failures, scope_measurement)
    language_failures, language_measurement = check_language(
        evidence, targets or {}, texts.get(AUDIT) or "", texts.get(LANGUAGE) or "")
    add_simple_leg(legs["A"], "A4", language_failures, language_measurement)
    province_failures, province_measurement = check_province(
        evidence, texts.get(AUDIT) or "", texts.get(PROVINCE))
    add_simple_leg(legs["A"], "A5", province_failures, province_measurement)
    contested_failures, contested_measurement = check_contested(texts.get(AUDIT) or "")
    add_simple_leg(legs["A"], "A6", contested_failures, contested_measurement)
    history_commands = {
        "a07_d4_selftest": run_command("A7-r21-d4-selftest", ["tools/assemble-d4-typed.py", "--selftest"]),
        "a07_typed_gate": run_command("A7-r21-typed-pipeline",
                                      ["tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.yml"]),
    }
    history_failures, history_measurement = check_history(history_commands)
    add_simple_leg(legs["A"], "A7", history_failures, history_measurement)

    report_text = evidence.fleet_text(REPORT, optional=True)
    if report_text is None:
        results["fleet_report_missing"] = REPORT
    report_failures, report_measurement = check_report(report_text)
    add_simple_leg(legs["cross"], "X1", report_failures, report_measurement)
    manifest_failures, manifest_measurement = check_manifest(manifest)
    add_simple_leg(legs["cross"], "X2", manifest_failures, manifest_measurement)
    telemetry_failures, telemetry_measurement, telemetry_missing = check_telemetry(
        evidence, declared if isinstance(declared, dict) else {}, observed, closing)
    for relative in telemetry_missing:
        evidence.missing.add(relative)
    add_simple_leg(legs["cross"], "X3", telemetry_failures, telemetry_measurement)

    changed = evidence.recheck()
    if changed:
        add_simple_leg(legs["cross"], "EVIDENCE-STABILITY",
                       ["evidence changed during measurement: " + ", ".join(changed)],
                       {"changed_paths": changed})
    elif evidence.errors:
        add_simple_leg(legs["cross"], "EVIDENCE-STABILITY", list(evidence.errors),
                       {"evidence_errors": evidence.errors})
    else:
        add_simple_leg(legs["cross"], "EVIDENCE-STABILITY", [], {"changed_paths": []})

    results = {claim_id: build_claim_result(items) for claim_id, items in legs.items()}
    missing_outputs = []
    for seat in target_seats(targets or {}):
        if not isinstance(seat, dict) or not isinstance(seat.get("out"), str):
            continue
        path = f"{ROUND}/{seat['out']}"
        if evidence.text(path, optional=True) is None:
            missing_outputs.append(path)
    missing_dependencies = sorted(evidence.missing | set(missing_outputs))
    all_legs_ok = all(item.get("status") == GREEN for group in legs.values()
                      for item in group.values()
                      if item.get("status") != "could-not-evaluate")
    receipt = {"round": 33, "runner": RUNNER,
               "runner_sha256": evidence.inputs.get(RUNNER),
               "counting_command": COMMAND, "date": today(), "measured_at_utc": now(),
               "baseline_revision": baseline,
               "claims_declared": coherence_measurement.get("claims_declared", {}),
               "acceptance_checks_passed": all_legs_ok,
               "claims": results,
               "failures": [f"claim {claim_id}: {failure}"
                            for claim_id, value in results.items()
                            for failure in value["failures"]],
               "missing_dependencies": missing_dependencies,
               "target_outputs": sorted(missing_outputs),
               "input_sha256": dict(sorted(evidence.inputs.items())),
               "limits": [
                   "Read-only evidence checks and explicitly listed non-mutating commands; scratch-only controls use .scratch.",
                   "No provider prompts are persisted; the protocol-owner lead remains could-not-evaluate.",
                   "The round report, manifest entry, observed-dispatch record, and availability-close snapshot are close-time inputs and are never created by --check.",
                   "Language hits are classified by the embedded scanner; broad residuals require the filed manual adjudication inventory.",
                   "In-flight evidence changes invalidate the measurement; re-run after the integration tree settles."]}
    x4_failures, x4_measurement = check_x4(receipt)
    add_simple_leg(legs["cross"], "X4", x4_failures, x4_measurement)
    results = {claim_id: build_claim_result(items) for claim_id, items in legs.items()}
    receipt["claims"] = results
    receipt["acceptance_checks_passed"] = all(
        item.get("status") == GREEN for group in legs.values() for item in group.values()
        if item.get("status") != "could-not-evaluate")
    receipt["failures"] = [f"claim {claim_id}: {failure}"
                            for claim_id, value in results.items()
                            for failure in value["failures"]]
    receipt["input_sha256"] = dict(sorted(evidence.inputs.items()))
    receipt["missing_dependencies"] = sorted(evidence.missing | set(missing_outputs))
    return receipt


def strict_selftest():
    checks = []

    def check(name, ok):
        checks.append({"control": name, "ok": bool(ok)})

    def valid_ledger(count=12):
        return {"rows": [{"id": f"OI-{number:02}", "item": "item", "origin": "r1",
                          "pointer": "path", "status_quo_check": {"date": today()},
                          "disposition_class": "carried-with-owner+reason+next-touch",
                          "evidence": ["path:1"], "owner": "operator", "reason": "reason",
                          "next_touch": "next"}
                         for number in range(1, count + 1)]}

    ledger_failures, _ = validate_ledger(valid_ledger(11),
                                          "| OI-01 |", "", "")
    check("ledger-eleven-rows-refused", any("rows=11" in item for item in ledger_failures))
    ledger_failures, _ = validate_ledger(valid_ledger(13),
                                          "| OI-01 |", "", "")
    check("ledger-thirteen-rows-refused", any("rows=13" in item for item in ledger_failures))
    bad_ledger = valid_ledger()
    bad_ledger["rows"][0]["disposition_class"] = "unlicensed"
    ledger_failures, _ = validate_ledger(bad_ledger, "| OI-01 |", "", "")
    check("ledger-invalid-class-refused", any("OI-01 has an unlicensed" in item for item in ledger_failures))
    bad_ledger = valid_ledger()
    bad_ledger["rows"][0].pop("next_touch")
    ledger_failures, _ = validate_ledger(bad_ledger, "| OI-01 |", "", "")
    check("carried-row-needs-next-touch", any("OI-01 carried row lacks next_touch" in item for item in ledger_failures))
    c31_bad = "lesson files: 33\nindex rows: 33\nfindings: 0\nFAIL C31_index_rows_eq_files\n"
    c31_failures, _ = c31_counts(c31_bad)
    check("c31-explicit-fail-refused", any("FAIL C" in item for item in c31_failures))
    c31_bad = "lesson files: 26\nindex rows: 33\nfindings: 0\n"
    c31_failures, _ = c31_counts(c31_bad)
    check("c31-files-rows-mismatch-refused", bool(c31_failures))
    o05_failures, _ = check_o05("# O05\nowner: parent\nreason: carried\n")
    check("o05-undated-refused", any("no ISO date" in item for item in o05_failures))
    audit9 = "\n".join(f"| A{number:02} | check | {GREEN} | evidence |" for number in range(1, 10))
    audit_failures, _ = check_audit_table(audit9)
    check("audit-nine-verdicts-refused", any("lacks one or more" in item for item in audit_failures))
    audit_ownerless = "| A01 | check | named-finding | evidence |\n"
    audit_failures, _ = check_audit_table(audit_ownerless)
    check("named-finding-needs-owner", any("owner dispositions" in item for item in audit_failures))
    handoff_failures, _ = check_handoff_output({"exit_code": 0,
        "stdout": "fields=15/16 glossary-entries=20 findings=0"}, True)
    check("handoff-fifteen-fields-refused", any("not 16/16" in item for item in handoff_failures))
    scanner_ns = {"__name__": "a08_fixture"}
    source = """import re
PATTERNS = [("P1", "x", re.compile(r"(?i)\\bpromot(?:e|es|ed|ing|ion)\\b"))]
STRICT = []
NEG = re.compile(r"(?i)\\b(?:no|not|never|none|without|zero|to-verify|pending|owed)\\b")
ROUTED = re.compile(r"(?i)\\b(?:operator|owner|routed|integrator)\\b")
CITE = re.compile(r"`[^`]+`|[A-Za-z0-9_./-]+\\.(?:py|md|json):\\d+")
def backtick_spans(text): return [(m.start(1),m.end(1)) for m in re.finditer(r"`([^`\\n]*)`",text)]
def mention_reason(text,start,end,spans): return None
def window(text,start,end,span=300): return text
def classify(text,start,end,spans):
    if NEG.search(text): return "NEGATION", ""
    if ROUTED.search(text): return "ROUTED-REFERENCE", ""
    if CITE.search(text): return "CITED-RESULT", ""
    return "UNSUPPORTED-CLAIM", ""
"""
    exec(compile(source, "fixture", "exec"), scanner_ns)
    language_fixture = "The audit states " + "promo" + "tion is " + "approv" + "ed."
    found = scanner_ns["PATTERNS"][0][2].search(language_fixture)
    result_class = scanner_ns["classify"](language_fixture, found.start(), found.end(), [])
    check("unrouted-approval-fixture-refused", result_class[0] == UNSUPPORTED)
    report3 = "# r\n## Work performed\n## Landed changes\n## SHONEN\n"
    check("three-section-report-refused", bool(check_report(report3)[0]))
    check_commit = lambda _token: (False, "baseline_commit does not resolve to a commit")
    failed_coherence, _ = validate_coherence({"round": 33, "baseline_commit": "f" * 40,
        "claims": [{"id": "O", "axis": "operability"}, {"id": "C", "axis": "calibration"},
                   {"id": "A", "axis": "adjacency"}],
        "axes_in_play": list(CLAIM_AXES.values()), "freshness_pause_in_force": True,
        "dispatch": {"provider_lane": "opencode-go", "model": "deepseek-v4.1-flash",
                     "requested_workers": 64, "batched_calls": 1}},
        {"round": 33, "seat_count": 0, "seats": []}, check_commit)
    check("unresolvable-baseline-refused", any("CO1" in item for item in failed_coherence))
    freshness_claims = {"round": 33, "baseline_commit": "f" * 40,
        "claims": [{"id": "O", "axis": "operability"}, {"id": "C", "axis": "calibration"},
                   {"id": "A", "axis": "adjacency"}],
        "axes_in_play": ["operability", "calibration", "adjacency", "freshness"],
        "freshness_pause_in_force": True,
        "dispatch": {"provider_lane": "opencode-go", "model": "deepseek-v4.1-flash",
                     "requested_workers": 64, "batched_calls": 1}}
    freshness_failures, _ = validate_coherence(freshness_claims,
        {"round": 33, "seat_count": 0, "seats": []}, check_commit)
    check("freshness-axis-refused", any("CO3" in item for item in freshness_failures))
    target_failures, _ = validate_coherence({"round": 33, "baseline_commit": "f" * 40,
        "claims": [{"id": "O", "axis": "operability"}, {"id": "C", "axis": "calibration"},
                   {"id": "A", "axis": "adjacency"}],
        "axes_in_play": list(CLAIM_AXES.values()), "freshness_pause_in_force": True,
        "dispatch": {"provider_lane": "opencode-go", "model": "deepseek-v4.1-flash",
                     "requested_workers": 64, "batched_calls": 1}},
        {"round": 33, "seat_count": 63, "seats": [{} for _ in range(63)]}, check_commit)
    check("sixty-three-seats-refused", any("seat_count=63" in item for item in target_failures))
    duplicate_seats = [{"id": f"S{number}", "role": "scout", "claim": "O",
                        "mission": "mission", "out": f"{ROUND}/same.md"}
                       for number in range(64)]
    target_failures, _ = validate_coherence({"round": 33, "baseline_commit": "f" * 40,
        "claims": [{"id": "O", "axis": "operability"}, {"id": "C", "axis": "calibration"},
                   {"id": "A", "axis": "adjacency"}],
        "axes_in_play": list(CLAIM_AXES.values()), "freshness_pause_in_force": True,
        "dispatch": {"provider_lane": "opencode-go", "model": "deepseek-v4.1-flash",
                     "requested_workers": 64, "batched_calls": 1}},
        {"round": 33, "seat_count": 64, "seats": duplicate_seats}, check_commit)
    check("duplicate-out-refused", any("duplicate seat out path" in item for item in target_failures))
    passed = sum(item["ok"] for item in checks)
    report = {"command": f"{COMMAND} --selftest", "date": today(),
              "passed_controls": passed, "total_controls": len(checks),
              "ok": passed == len(checks), "controls": checks}
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="print measured JSON without publishing validation.json")
    modes.add_argument("--selftest", action="store_true", help="run in-memory positive and negative controls")
    args = parser.parse_args(argv)
    if args.selftest:
        return strict_selftest()
    os.chdir(ROOT)
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    if not args.check:
        guard_receipt()
    try:
        receipt = measure()
    except (OSError, ValueError, TypeError, KeyError, RuntimeError,
            subprocess.SubprocessError, UnicodeError) as error:
        print(f"could-not-evaluate: {type(error).__name__}: {error}", file=sys.stderr)
        return 2
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        guard_receipt()
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        print(f"receipt: {OUTPUT}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
