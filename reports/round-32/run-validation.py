#!/usr/bin/env python3
"""Measure round-32 completion acceptance (the regimen's final round); --check never publishes a receipt."""
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
import runpy
import shlex
import subprocess
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
FLEET_ROOT = ROOT.parent
ROUND = "reports/round-32"
RUNNER = f"{ROUND}/run-validation.py"
OUTPUT = f"{ROUND}/validation.json"
COMMAND = f"python3 {RUNNER}"
CLAIMS = f"{ROUND}/claims.json"
TARGETS = f"{ROUND}/targets.json"
AUDIT = f"{ROUND}/completion-audit.md"
LEDGER = f"{ROUND}/completion-ledger.json"
DOSSIER = f"{ROUND}/final-dossier.md"
SWEEP = f"{ROUND}/final-sweep.md"
SWEEP_RECEIPT = f"{ROUND}/sweep/sweep-receipt.json"
SWEEP_COMMANDS = f"{ROUND}/sweep/commands.txt"
PRIOR_RECEIPT = "reports/round-31/sweep/sweep-receipt.json"
LOG = "LOG.md"
SCORECARD = "SCORECARD.md"
AGENTS = "AGENTS.md"
SKILL = "SKILL.md"
PROVINCE = "PROVINCE.md"
FLEET_REPORT = ".ufo/reports/round-{n}/kotodama.md"
FLEET_MANIFEST = "MANIFEST.json"
LANE = "kotodama"
CLOSED = tuple(range(8, 32))
REGIMEN = tuple(range(8, 33))
RETRO = tuple(range(1, 8))
REJECTED = (11, 17, 22)
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 32)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 32))
SECTIONS = (
    (r"work\s+performed", "Work performed"),
    (r"landed\s+changes", "Landed changes"),
    (r"before\s*(?:→|->)\s*after\s+measurements", "Before → after measurements"),
    (r"shonen", "SHONEN"),
)
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
SHA256_RE = re.compile(r"\b[0-9a-f]{64}\b")
FULL_COMMIT_RE = re.compile(r"\b[0-9a-f]{40}\b")
CMD_RE = re.compile(r"(?m)^\s*(?:\$\s*)?(python3(?:\s+-B)?\s+\S[^\n]*)$")
SWEEP_TABLE_ROW_RE = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]{8,64})[^`|]*`\s*\|")
MIN_GREEN_ROWS = 50
MIN_CONTROLS = 13
MIN_RED_CODE_1 = 5
MIN_RED_CODE_2 = 8
RUNNER_RE = re.compile(r"reports/round-32/run-validation\.py\b")


def today():
    return dt.date.today().isoformat()


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def metric(value, operation):
    return {"value": value, "command": f"{COMMAND} ({operation})", "date": today()}


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

    def _read(self, resolver, relative, key):
        try:
            data = resolver(relative).read_bytes()
            digest = sha(data)
            if key in self.inputs and self.inputs[key] != digest:
                self.errors.append(f"evidence changed between reads: {relative}")
            self.inputs.setdefault(key, digest)
            return data.decode("utf-8")
        except (OSError, ValueError, UnicodeError) as error:
            self.missing.add(key)
            self.errors.append(f"{relative}: {error}")
            return ""

    def text(self, relative):
        return self._read(safe_path, relative, relative)

    def fleet_text(self, relative):
        return self._read(fleet_path, relative, f"fleet:{relative}")

    def document(self, relative):
        text = self.text(relative)
        try:
            return strict_json(text) if text else None
        except (TypeError, ValueError) as error:
            self.errors.append(f"{relative}: {error}")
            return None

    def fleet_document(self, relative):
        text = self.fleet_text(relative)
        try:
            return strict_json(text) if text else None
        except (TypeError, ValueError) as error:
            self.errors.append(f"fleet:{relative}: {error}")
            return None


def result(failures, measurement):
    return {"passed": not failures, "date": today(), "command": COMMAND,
            "failures": failures, "measurement": measurement}


def git(*args):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1")
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, env=env, timeout=60)


def commit_status(token):
    if not isinstance(token, str) or not re.fullmatch(r"[0-9a-f]{7,40}", token):
        return {"exists": False, "ancestor": False, "reason": "not a hex commit token"}
    resolve = git("rev-parse", "--verify", f"{token}^{{commit}}")
    if resolve.returncode:
        return {"exists": False, "ancestor": False, "reason": "git rev-parse refused the commit"}
    full = resolve.stdout.decode().strip()
    ancestor = git("merge-base", "--is-ancestor", full, "HEAD")
    return {"exists": True, "ancestor": ancestor.returncode == 0, "resolved": full}


def protected_snapshot(revision):
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return result(["declared baseline must be a full Git revision"], {})
    proc = git("ls-tree", "-r", "-z", revision, "--", *PROTECTED)
    if proc.returncode:
        return result(["cannot enumerate protected baseline"], {})
    expected = {}
    changes = []
    for item in proc.stdout.split(b"\0"):
        if not item:
            continue
        metadata, name = item.split(b"\t", 1)
        _mode, kind, oid = metadata.decode("ascii").split()
        if kind == "blob":
            expected[os.fsdecode(name)] = oid
    for relative, oid in expected.items():
        try:
            data = safe_path(relative).read_bytes()
            observed = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        except (OSError, ValueError):
            observed = None
        if observed != oid:
            changes.append({"path": relative, "baseline_blob": oid, "observed_blob": observed})
    status = git("status", "--porcelain=v1", "--untracked-files=all", "--", *PROTECTED)
    if status.returncode:
        return result(["cannot inspect protected path status"], {})
    additions = [line[3:] for line in status.stdout.decode("utf-8", "replace").splitlines()
                 if line.startswith("?? ") or line.startswith("A ") or line.startswith(" A")]
    # sanctioned retroactive act (AGENTS.md "Close what you open", landed 2026-10-18):
    # closing snapshots are NEW append-only files under the filed rounds' telemetry/.
    additions = [a for a in additions
                 if not (a.startswith("reports/round-") and "/telemetry/availability-close-" in a)]
    failures = ["filed rounds 8-31 or their frozen generations changed"] if changes or additions else []
    return result(failures, {"baseline_revision": revision,
                             "protected_files": metric(len(expected), "git ls-tree of filed report/frozen paths"),
                             "differences": changes, "new_protected_paths": additions})


def run_command(name, parts, tmpdir=None):
    argv = [sys.executable, "-B", *parts]
    if tmpdir is None:
        tmpdir = str(ROOT / ".scratch")
    env = {**os.environ, "TMPDIR": tmpdir, "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    item = {"name": name, "command": shlex.join(["python3", "-B", *parts]),
            "date": today(), "tmpdir": tmpdir}
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, timeout=300)
        item.update(exit_code=proc.returncode, stdout=proc.stdout.decode("utf-8", "replace"),
                    stderr=proc.stderr.decode("utf-8", "replace"),
                    stdout_sha256=sha(proc.stdout), stderr_sha256=sha(proc.stderr))
    except (OSError, subprocess.SubprocessError) as error:
        item.update(exit_code=None, stdout="", stderr="", error=f"{type(error).__name__}: {error}")
    item["elapsed_seconds"] = round(time.monotonic() - started, 3)
    item["passed"] = item["exit_code"] == 0
    return item


EXTERNAL_TMP_RE = re.compile(r"replay-frozen|freeze-r\d+")


def rerun_tmpdir(command):
    return "/var/tmp" if EXTERNAL_TMP_RE.search(command) else None


def sections_of(report_text):
    headings = set()
    for line in report_text.splitlines():
        arrow = line.replace("->", "→")
        for pattern, name in SECTIONS:
            if re.fullmatch(r"\s*#{1,6}\s+" + pattern + r"\s*", arrow, re.I):
                headings.add(name)
    return headings


def koto_entries_by_round(manifest):
    index = {}
    for entry in manifest.get("rounds", []):
        if not isinstance(entry, dict):
            continue
        blob = json.dumps(entry, ensure_ascii=False)
        if LANE not in blob:
            continue
        round_no = entry.get("round")
        if isinstance(round_no, int):
            index.setdefault(round_no, []).append(entry)
    return index


def lane_round_entries(index, round_no):
    rows = []
    for entry in index.get(round_no, []):
        lanes = entry.get("lanes")
        lane_rounds = entry.get("lane_rounds")
        tagged = ((isinstance(lanes, dict) and lanes.get(LANE))
                  or (isinstance(lane_rounds, dict) and lane_rounds.get(LANE) is not None))
        if tagged or entry.get("type") in ("retroactive-closure", "closure", "mint"):
            rows.append(entry)
    return rows


def closure_entries(index, round_no):
    return [entry for entry in lane_round_entries(index, round_no)
            if entry.get("type") == "closure"]


def skipped_rounds(index):
    skipped = set()
    for number in CLOSED:
        for entry in closure_entries(index, number):
            verdicts = entry.get("verdicts")
            if verdicts is None and entry.get("operator_skipped") is not False:
                skipped.add(number)
    return skipped


def scorecard_round_heading(number):
    return re.compile(rf"(?m)^##\s+Axes\s+[—-]\s+round\s+{number}\b")


def scorecard_section(text, number):
    match = scorecard_round_heading(number).search(text)
    if not match:
        return None
    nxt = re.search(r"(?m)^##\s+", text[match.end():])
    return text[match.end():match.end() + nxt.start()] if nxt else text[match.end():]


def scorecard_capabilities(text):
    rows = []
    in_section = False
    for line in text.splitlines():
        if re.match(r"(?m)^#{1,6}\s+", line):
            in_section = bool(re.fullmatch(r"#{1,6}\s+Capabilities\s*", line.strip()))
            continue
        if in_section and line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[0] and cells[0].lower() != "name" \
                    and not set(cells[0]) <= set(":- "):
                rows.append(cells[0])
    return rows


def battery_check(run):
    try:
        document = strict_json(run.get("stdout", ""))
    except (TypeError, ValueError):
        document = {}
    baselines = document.get("baselines", {}).get("summary", {})
    summary = document.get("summary", {})
    text = json.dumps(document)
    passed = (run.get("exit_code") == 0 and baselines.get("coverage") == "10/10"
              and not baselines.get("gates_uncovered")
              and isinstance(baselines.get("pinned"), int) and baselines["pinned"] > 0
              and baselines.get("pinned") == baselines.get("baselines_found")
              and not summary.get("fail") and not summary.get("unevaluable")
              and "register-law-gate.py" in text)
    return {"passed": passed, "summary": summary, "baselines": baselines,
            "command": run.get("command"), "date": run.get("date")}


def parse_sweep_table(text):
    records = []
    for line in text.splitlines():
        match = SWEEP_TABLE_ROW_RE.match(line)
        if match:
            identifier, family, command, exit_cell, sha16 = match.groups()
            records.append({"id": identifier.strip(), "family": family.strip(),
                            "command": command.strip(), "exit": int(exit_cell),
                            "sha16": sha16, "dated": DATE_RE.search(line) is not None})
    return records


def parse_final_sweep(text):
    records = []
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = CMD_RE.match(line)
        if not match:
            continue
        command = match.group(1).strip()
        window = "\n".join(lines[max(0, index - 3):index + 4])
        records.append({
            "line": index + 1, "command": command,
            "exit0": bool(re.search(r"(?i)\bexit(?:_code)?\s*[:=]?\s*0\b|\brc\s*=\s*0\b|exit 0", window)),
            "dated": bool(DATE_RE.search(window)),
            "sha_recorded": bool(SHA256_RE.search(window)),
        })
    return records


def command_target(tokens):
    rest = list(tokens)
    if not rest or rest[0] != "python3":
        return None
    rest = rest[1:]
    if rest and rest[0] == "-B":
        rest = rest[1:]
    if not rest:
        return None
    if rest[0] == "-c":
        return "stdin-code"
    return rest


def whitelist_rerun(record):
    try:
        tokens = shlex.split(record["command"])
    except ValueError:
        return "refused"
    rest = command_target(tokens)
    if rest in (None, "stdin-code"):
        return "skipped-stdin-code" if rest == "stdin-code" else "refused"
    target = rest[0]
    if not (target.startswith("tools/") or target.startswith("examples/")
            or re.fullmatch(r"reports/round-\d+/[A-Za-z0-9_./\-]+\.py", target)) or ".." in target:
        return "refused"
    if RUNNER_RE.fullmatch(target) and "--selftest" not in rest[1:]:
        return "refused-recursive-runner"
    if any(not re.fullmatch(r"[A-Za-z0-9_@=/:.,+\-]+", token) for token in rest[1:]):
        return "refused"
    return "allowed"


def declared_matrix(evidence):
    receipt = evidence.document(SWEEP_RECEIPT)
    rows = [row for row in (receipt or {}).get("rows", [])
            if isinstance(row, dict) and row.get("expect_exit") == 0
            and isinstance(row.get("command"), str)]
    if rows:
        matrix = []
        for row in rows:
            try:
                tokens = shlex.split(row["command"])
            except ValueError:
                continue
            if command_target(tokens) not in (None, "stdin-code"):
                matrix.append((str(row.get("id") or Path(tokens[-1]).name), tokens))
        if matrix:
            return matrix, f"receipt:{SWEEP_RECEIPT}", []
    prior = evidence.document(PRIOR_RECEIPT)
    matrix = []
    for row in (prior or {}).get("rows", []):
        if isinstance(row, dict) and row.get("expect_exit") == 0 and isinstance(row.get("command"), str):
            try:
                tokens = shlex.split(row["command"])
            except ValueError:
                continue
            if command_target(tokens) not in (None, "stdin-code"):
                matrix.append((str(row.get("id") or "prior-row"), tokens))
    matrix.append(("r32-runner-selftest", ["python3", "-B", RUNNER, "--selftest"]))
    return matrix, f"fallback:{PRIOR_RECEIPT}+{RUNNER} --selftest", [
        "declared sweep matrix fell back to the settled r31 green surface plus this runner's selftest"]


def measure_completion(evidence, claims):
    failures = []
    audit_text = evidence.text(AUDIT)
    if not audit_text:
        return result([f"{AUDIT} missing (C-completion seat dependency)"], {})
    ledger = evidence.document(LEDGER)
    if not ledger:
        return result(failures + [f"{LEDGER} missing or unparseable (C-closure seat dependency)"], {})
    findings = {}
    for finding in ledger.get("findings", []) if isinstance(ledger.get("findings"), list) else []:
        if isinstance(finding, dict) and isinstance(finding.get("round"), int):
            findings.setdefault(finding["round"], []).append(finding)

    def covered(number, keyword):
        blob = json.dumps(findings.get(number, []), ensure_ascii=False)
        return bool(DATE_RE.search(blob) and re.search(keyword, blob, re.I))
    if not DATE_RE.search(audit_text):
        failures.append("completion audit carries no date")
    for label, pattern in (
            ("criterion coverage 8-31", r"8\s*[-–—]\s*31|rounds?\s+8.{0,40}31"),
            ("r32 by-construction closure path", r"(?i)by\s+construction|same\s+integration\s+pass"),
            ("r11/r17/r22 rejections on record", r"(?i)11|17|22"),
            ("retro rows 1-7", r"(?i)1\s*[-–—]\s*7|retro")):
        if not re.search(pattern, audit_text):
            failures.append(f"completion audit lacks {label}")
    rejection_numbers = {int(n) for n in re.findall(r"\b(11|17|22)\b", audit_text)}
    if not set(REJECTED) <= rejection_numbers:
        failures.append("completion audit does not name every rejected round 11/17/22")

    manifest = evidence.fleet_document(FLEET_MANIFEST)
    if not manifest:
        return result(failures + ["fleet MANIFEST.json unreadable"], {})
    index = koto_entries_by_round(manifest)
    skip = skipped_rounds(index)

    retro_ok = 0
    for number in RETRO:
        entries = [entry for entry in index.get(number, [])
                   if entry.get("type") in ("retroactive-closure", "closure")]
        if entries:
            retro_ok += 1
        else:
            failures.append(f"retro round {number}: no kotodama closure/retroactive entry in fleet MANIFEST")

    reports_present = full_sections = ancestry_ok = verdict_rows = 0
    cited_stats = Counter()
    for number in CLOSED:
        closures = closure_entries(index, number)
        if not closures:
            failures.append(f"round {number}: no kotodama closure entry in fleet MANIFEST")
            continue
        verdicts = closures[-1].get("verdicts")
        if number in skip:
            if verdicts:
                failures.append(f"round {number}: classified skipped but carries per-axis verdicts")
            if fleet_path(FLEET_REPORT.format(n=number)).is_file():
                failures.append(f"round {number}: fleet report exists for an operator-skipped round")
            continue
        verdict_rows += 1
        if not isinstance(verdicts, dict) or not verdicts:
            failures.append(f"round {number}: closure entry carries no per-axis verdicts")
        report_text = evidence.fleet_text(FLEET_REPORT.format(n=number))
        if not report_text:
            failures.append(f"round {number}: fleet report missing at {FLEET_REPORT.format(n=number)}")
            continue
        reports_present += 1
        headings = sections_of(report_text)
        if headings == {name for _pattern, name in SECTIONS}:
            full_sections += 1
        elif covered(number, r"landed[ -]?changes|section|heading"):
            pass  # deviation recorded honestly in the completion ledger (e.g. F-C32-1)
        else:
            failures.append(f"round {number}: fleet report carries {len(headings)}/4 required sections "
                            "with no dated ledger finding covering the deviation")
        tokens = sorted(set(FULL_COMMIT_RE.findall(report_text)))[:10]
        cited_stats["cited"] += len(tokens)
        bad = []
        for token in tokens:
            status = commit_status(token)
            if not (status["exists"] and status["ancestor"]):
                bad.append(token)
        cited_stats["invalid"] += len(bad)
        if bad:
            failures.append(f"round {number}: cited commit(s) fail existence/ancestry: {bad[:3]}")
        else:
            ancestry_ok += 1

    scorecard_text = evidence.text(SCORECARD)
    for number in CLOSED:
        if number in skip:
            if not re.search(rf"(?i)\bround\s+{number}\b", scorecard_text):
                failures.append(f"SCORECARD records no operator-skip row for round {number}")
            continue
        section = scorecard_section(scorecard_text, number)
        if section is None:
            failures.append(f"SCORECARD has no 'Axes — round {number}' section")
        elif not re.search(r"→|->", section):
            failures.append(f"SCORECARD round {number} section has no before → after measurement row")

    log_text = evidence.text(LOG)
    log_headings = re.findall(r"(?m)^##\s+(.+)$", log_text)
    log_gaps = []
    for number in CLOSED:
        if any(re.search(rf"(?i)\bround\s*{number}\b", heading) for heading in log_headings):
            continue
        if number in skip or covered(number, r"\bLOG\b"):
            continue  # operator-skip disposition, or a dated ledger finding records the gap
        log_gaps.append(number)
    if log_gaps:
        failures.append(f"LOG.md has no entry heading for round(s) {log_gaps} and no dated ledger "
                        "finding records the gap (the ledger's own falsification text names a "
                        "missing LOG record as verdict-falsifying)")

    for number in REJECTED:
        rejected = (any(re.search(rf"(?i)reject|not admitted", json.dumps(entry, ensure_ascii=False))
                        for entry in index.get(number, []))
                    or re.search(rf"(?mi)^#+.*round\s+{number}\b.*(reject|not admitted)", scorecard_text)
                    or re.search(rf"(?mi)^##\s+.*round\s+{number}\b.*(REJECT|NOT admitted)", log_text))
        if not rejected:
            failures.append(f"round {number}: rejection not on record in MANIFEST/SCORECARD/LOG")

    slot_report = fleet_path(FLEET_REPORT.format(n=32))
    if slot_report.is_file():
        failures.append("round-32 fleet report already exists (audit covers it by construction, "
                        "the report lands in the same integration pass that admits this round)")
    if closure_entries(index, 32):
        failures.append("round 32 already carries a MANIFEST closure entry (pending-by-construction)")
    if not re.search(r"(?i)round\s*32|by\s+construction", audit_text):
        failures.append("completion audit does not document the round-32 closure path")
    if ledger.get("zero_missing_rows") is not True:
        failures.append("completion ledger does not assert zero missing rows")
    verdict_doc = ledger.get("claim_C_verdict", {})
    if not str(verdict_doc.get("status", "")).startswith("verify") \
            or not str(verdict_doc.get("falsification", "")).strip():
        failures.append("claim_C_verdict lacks a verify-status and a falsification statement")
    for number, rows in sorted(findings.items()):
        for finding in rows:
            if not DATE_RE.search(json.dumps(finding, ensure_ascii=False)) \
                    or not str(finding.get("evidence_command", "")).strip():
                failures.append(f"finding {finding.get('id')!r} for round {number} lacks a date or "
                                "an evidence command")

    auditors = []
    candidates = sorted(safe_path(ROUND).glob("completion-audit-*.md"))
    candidates += sorted(safe_path(ROUND).glob("audit/*.md")) + sorted(safe_path(ROUND).glob("completion-audit/*.md"))
    for path in candidates:
        relative = path.relative_to(ROOT).as_posix()
        if relative == AUDIT:
            continue
        text = evidence.text(relative)
        rounds_named = len({int(n) for n in re.findall(r"\b(\d{1,2})\b", text)
                            if 8 <= int(n) <= 31})
        reverified = bool(re.search(r"(?i)re-?verif|PASS|recount|zero mismatch", text))
        verdict = bool(re.search(r"(?im)^(?:#{1,6}.*verdict|`?verify`?\s*[—-])", text))
        auditors.append({"path": relative, "dated": bool(DATE_RE.search(text)),
                         "rounds_named": rounds_named, "reverifies": reverified,
                         "verdict": verdict,
                         "passed": bool(DATE_RE.search(text) and rounds_named >= 5
                                        and reverified and verdict)})
    inline_auditor = bool(re.search(r"(?im)^#{1,6}\s*auditor", audit_text)) and \
        len(re.findall(r"(?i)re-?verif|recount", audit_text)) >= 2
    if not any(row["passed"] for row in auditors) and not inline_auditor:
        failures.append("no dated independent completion-audit artifact re-verifies filed rounds "
                        "(auditor seat dependency)")
    return result(failures, {
        "audit_sha256": evidence.inputs.get(AUDIT),
        "ledger_sha256": evidence.inputs.get(LEDGER),
        "claim_C_verdict_status": verdict_doc.get("status"),
        "ledger_findings": metric(len(findings), "dated completion-ledger findings"),
        "log_gaps_uncovered": log_gaps,
        "retro_rows_reconfirmed": metric(retro_ok, "retro rounds 1-7 with fleet-MANIFEST rows"),
        "closure_rows_8_31": metric(len(CLOSED), "rounds requiring a MANIFEST closure row"),
        "per_axis_verdict_rows": metric(verdict_rows, "rounds 8-31 with per-axis verdicts"),
        "fleet_reports_present": metric(reports_present, "independent fleet-report recount"),
        "sections_fully_valid": metric(full_sections, "independent 4-section recount"),
        "commit_citations_checked": metric(cited_stats["cited"],
                                           "full commit citations re-verified for existence+ancestry"),
        "commit_citations_invalid": metric(cited_stats["invalid"], "citations failing ancestry"),
        "reports_with_valid_ancestry": metric(ancestry_ok, "fleet reports whose citations all verify"),
        "operator_skipped_rounds": metric(sorted(skip), "verdict-less closure rows"),
        "rejected_rounds_on_record": metric(list(REJECTED), "rejections re-confirmed"),
        "round_32_slot": {"fleet_report_exists": slot_report.is_file(),
                          "manifest_closure_entries": len(closure_entries(index, 32))},
        "independent_auditors": auditors,
        "qualified_auditors": metric(sum(row["passed"] for row in auditors),
                                     "dated independent completion auditors"),
        "inline_auditor_section": inline_auditor,
    })


def measure_sweep(evidence, claims, runs):
    failures = []
    matrix, matrix_source, matrix_failures = declared_matrix(evidence)
    failures.extend(matrix_failures)
    for row in runs:
        if not row["passed"]:
            failures.append(f"final-sweep matrix command {row['name']} exited {row['exit_code']}")
    battery = battery_check(next((row for row in runs if "battery" in row["name"]
                                  and "selftest" not in row["name"]), {}))
    if not battery["passed"]:
        failures.append("gate battery is not 10/10 with the law gate registered")
    sweep_text = evidence.text(SWEEP)
    sweep_present = bool(sweep_text)
    if not sweep_present:
        failures.append(f"{SWEEP} missing (O-sweep seat dependency)")
    table = parse_sweep_table(sweep_text) if sweep_present else []
    lines = parse_final_sweep(sweep_text) if sweep_present else []
    receipt = evidence.document(SWEEP_RECEIPT) if sweep_present else None
    if sweep_present and not receipt:
        failures.append(f"{SWEEP_RECEIPT} missing or unparseable (machine receipt leg)")
    receipt_rows = {row.get("id"): row for row in (receipt or {}).get("rows", [])
                    if isinstance(row, dict)}
    green_rows = [record for record in table if record["exit"] == 0]
    if sweep_present and len(green_rows) < MIN_GREEN_ROWS:
        failures.append(f"final-sweep table carries {len(green_rows)} green rows, expected >= "
                        f"{MIN_GREEN_ROWS} (the r31 50-command matrix plus this round's harness)")
    runner_in_sweep = any(RUNNER_RE.search(record["command"]) and "--selftest" in record["command"]
                          for record in table + lines)
    if sweep_present and not runner_in_sweep:
        failures.append(f"the sweep does not exercise this round's own validation harness ({RUNNER} --selftest)")
    bound, unbound = 0, []
    for record in green_rows:
        row = receipt_rows.get(record["id"])
        if not row:
            unbound.append(record["id"])
            continue
        if (row.get("exit_code") == 0 and row.get("passed") is True
                and DATE_RE.search(str(row.get("date", "")))
                and str(row.get("stdout_sha256", "")).startswith(record["sha16"])):
            bound += 1
        else:
            unbound.append(record["id"])
    if sweep_present and green_rows and unbound:
        failures.append(f"{len(unbound)} final-sweep green row(s) do not bind to dated exit-0 "
                        f"receipt rows with matching output digests: {unbound[:6]}")
    expected_families = set()
    for _name, tokens in matrix:
        target = command_target(tokens)
        if isinstance(target, list):
            expected_families.add(Path(target[0]).name)
    covered = set()
    for record in green_rows:
        try:
            tokens = shlex.split(record["command"])
        except ValueError:
            continue
        paths = [token for token in tokens if "/" in token]
        if paths:
            covered.add(Path(paths[0]).name)
    for record in lines:
        if not record["exit0"]:
            continue
        try:
            tokens = shlex.split(record["command"])
        except ValueError:
            continue
        paths = [token for token in tokens if "/" in token]
        if paths:
            covered.add(Path(paths[0]).name)
    missing_families = sorted(expected_families - covered)
    if sweep_present and missing_families:
        failures.append("final-sweep records no dated exit-0 command for: "
                        + ", ".join(missing_families))
    controls = [row for row in receipt_rows.values()
                if row.get("expect_exit") not in (0, None)]
    deviating = [row.get("id") for row in controls
                 if row.get("exit_code") != row.get("expect_exit")]
    if sweep_present and receipt and len(controls) < MIN_CONTROLS:
        failures.append(f"fewer than {MIN_CONTROLS} declared historical replay controls in the "
                        f"receipt ({len(controls)})")
    if deviating:
        failures.append("historical control rows deviate from their expected filed-red codes: "
                        + ", ".join(deviating))
    code_counts = Counter(row.get("expect_exit") for row in controls)
    if sweep_present and receipt and (code_counts.get(1, 0) < MIN_RED_CODE_1
                                      or code_counts.get(2, 0) < MIN_RED_CODE_2):
        failures.append("filed-red code distribution regressed: expected >= 8 controls at exit 2 "
                        f"and >= 5 at exit 1, observed {dict(code_counts)}")
    prior = evidence.document(PRIOR_RECEIPT) or {}
    prior_controls = {row.get("id") for row in prior.get("rows", [])
                      if isinstance(row, dict) and row.get("expect_exit") not in (0, None)}
    current_controls = {row.get("id") for row in controls}
    if sweep_present and receipt and prior_controls and not prior_controls <= current_controls:
        failures.append("historical control set shrank vs the r31 receipt: "
                        + ", ".join(sorted(prior_controls - current_controls))[:200])
    rerun = []
    if sweep_present:
        commands = [line.strip() for line in evidence.text(SWEEP_COMMANDS).splitlines()
                    if line.strip() and not line.strip().startswith("#")]
        if not commands:
            failures.append(f"{SWEEP_COMMANDS} manifest missing or empty (re-runnable leg)")
        for command in commands:
            disposition = whitelist_rerun({"command": command})
            if disposition == "allowed":
                parts = command_target(shlex.split(command))
                item = run_command("sweep:" + Path(parts[0]).name, parts,
                                   tmpdir=rerun_tmpdir(command))
                item["recorded"] = True
                if not item["passed"]:
                    failures.append(f"recorded sweep command does not reproduce: {command[:90]}")
                rerun.append(item)
            else:
                rerun.append({"command": command, "rerun": disposition,
                              "date": today(),
                              "passed": disposition == "skipped-stdin-code"})
                if disposition != "skipped-stdin-code":
                    failures.append(f"recorded command not re-runnable under the safety whitelist: "
                                    f"{command[:90]} ({disposition})")
        reran = [row for row in rerun if row.get("exit_code") is not None]
        if sweep_present and commands and not reran:
            failures.append("no recorded sweep command was re-executed")
    audits = []
    for path in sorted(safe_path(ROUND).glob("sweep-audit-O*.json")):
        relative = path.relative_to(ROOT).as_posix()
        document = evidence.document(relative)
        if not document:
            continue
        rows = document.get("results") or []
        red = [row.get("name") for row in rows if row.get("passed") is False]
        audits.append({"path": relative, "date": document.get("date"), "rows": len(rows),
                       "failed_rows": red,
                       "passed": bool(DATE_RE.search(str(document.get("date", "")))) and not red})
    for audit in audits:
        if not audit["passed"]:
            failures.append(f"independent sweep-audit leg reports red rows or lacks a date: "
                            f"{audit['path']} {audit['failed_rows'][:4]}")
    return result(failures, {
        "matrix_source": matrix_source,
        "matrix_size": metric(len(matrix), "declared final-sweep matrix size"),
        "matrix_green": metric(sum(row["passed"] for row in runs), "matrix commands exiting 0"),
        "battery_registration": battery,
        "final_sweep_present": sweep_present,
        "recorded_green_table_rows": metric(len(green_rows), "green table rows parsed from final-sweep.md"),
        "receipt_bound_rows": metric(bound, "final-sweep rows bound to dated green receipt rows"),
        "receipt_rows": metric(len(receipt_rows), "sweep-receipt rows"),
        "historical_controls": metric(len(controls), "expected-red replay control rows"),
        "control_code_distribution": metric(dict(code_counts), "filed-red exit-code distribution"),
        "historical_control_set_preserved": metric(len(prior_controls & current_controls),
                                                   "r31 controls preserved in the r32 receipt"),
        "families_covered": metric(len(covered & expected_families), "sweep families re-recorded"),
        "recorded_manifest_commands": metric(len([row for row in rerun if row.get("recorded")]),
                                             "commands.txt commands re-executed"),
        "recorded_reruns": rerun,
        "independent_audits": audits,
    })


def measure_dossier(evidence, claims):
    failures = []
    anchor = evidence.text(DOSSIER)
    text = anchor
    if not anchor:
        return result([f"{DOSSIER} missing (D-dossier seat dependency)"], {})
    fragments = []
    for path in sorted(safe_path(ROUND).glob("dossier-*.md")):
        relative = path.relative_to(ROOT).as_posix()
        fragment = evidence.text(relative)
        if fragment:
            fragments.append({"path": relative, "sha256": evidence.inputs.get(relative)})
            text += "\n\n" + fragment
    if not DATE_RE.search(text):
        failures.append("final dossier carries no date")
    boxes_surveyed = len(re.findall(r"(?i)\bbox\s*[1-4]\b|box\s*#?\s*[1-4]", text))
    if boxes_surveyed < 4:
        failures.append(f"final dossier re-surveys {boxes_surveyed}/4 SHONEN boxes")
    if not re.search(r"(?i)register[ -]?craft|round\s*30", text):
        failures.append("box 1 closure does not cite the r30 Register-craft survey")
    if not re.search(r"(?i)round\s*24|promotion[ -]?review", text):
        failures.append("boxes 2-4 do not restate their r24 promotion-review verdicts")
    if not re.search(r"(?i)rounds?\s*(2[5-9]|3[01])\b", text):
        failures.append("boxes 2-4 lack the regimen's subsequent evidence (rounds 25-31)")
    scorecard_text = evidence.text(SCORECARD)
    capabilities = scorecard_capabilities(scorecard_text)
    command_re = re.compile(r"`[^`]*(?:python3|tools/|corpus/|reports/|examples/)[^`]*`")
    chunks = re.split(r"\n\s*\n", text)
    inventory = []
    for name in capabilities:
        named = False
        commanded = False
        for match in re.finditer(re.escape(name), text, re.I):
            named = True
            window = text[max(0, match.start() - 80):match.end() + 500]
            if re.search(command_re, window):
                commanded = True
                break
        if not commanded:
            tokens = [t for t in re.split(r"[^a-z0-9]+", name.lower()) if len(t) >= 2]
            for chunk in chunks:
                low = chunk.lower()
                if tokens and all(t in low for t in tokens) and re.search(command_re, chunk):
                    named = True
                    commanded = True
                    break
        inventory.append({"capability": name, "named": named, "command_shown": commanded})
    missing_inventory = [row["capability"] for row in inventory
                         if not row["named"] or not row["command_shown"]]
    if capabilities and missing_inventory:
        failures.append(f"capability inventory incomplete for {len(missing_inventory)}/{len(capabilities)} "
                        f"SCORECARD capabilities (no named command): {missing_inventory[:4]}")
    if not re.search(RUNNER_RE, text):
        failures.append("final dossier does not cite the counting command " + COMMAND)
    if not re.search(r"(?i)no promotion|not (?:a )?promotion|promotion (?:is|has) not|"
                     r"does not (?:claim|decide|determine|make)[^\n]{0,40}promotion|"
                     r"non-?canonical|decision'?s? (?:evidence|materials)", anchor):
        failures.append("final dossier anchor lacks the explicit no-promotion / "
                        "decision-evidence statement")
    if re.search(r"(?i)(?:all (?:four|4)|4/4)\s+(?:boxes|shonen|promotion)[^\n]{0,60}"
                 r"(?:pass|satisf|complete|cleared|\[x\])", text):
        failures.append("FALSIFIER FIRED: the dossier presents the promotion checklist as complete")
    return result(failures, {
        "dossier_sha256": evidence.inputs.get(DOSSIER),
        "dossier_fragments": fragments,
        "boxes_surveyed": metric(boxes_surveyed, "SHONEN boxes re-surveyed"),
        "box1_closure_cited": bool(re.search(r"(?i)register[ -]?craft|round\s*30", text)),
        "r24_verdicts_restated": bool(re.search(r"(?i)round\s*24|promotion[ -]?review", text)),
        "capabilities_total": metric(len(capabilities), "SCORECARD capability rows"),
        "capabilities_inventoried": metric(len(capabilities) - len(missing_inventory),
                                           "capabilities with a demonstrated command in the dossier"),
        "capability_gaps": missing_inventory,
        "promotion_claimed": False,
    })


def dependencies_ready():
    pending = []
    for relative in (AUDIT, DOSSIER, SWEEP, SWEEP_RECEIPT, SWEEP_COMMANDS):
        if not safe_path(relative).is_file():
            pending.append(relative)
    auditors = list(safe_path(ROUND).glob("completion-audit-*.md")) \
        + list(safe_path(ROUND).glob("audit/*.md")) + list(safe_path(ROUND).glob("completion-audit/*.md"))
    if not auditors:
        pending.append(f"{ROUND}/ completion-audit auditor artifacts")
    return pending


def runtime_paths():
    paths = set()
    for directory in ("tools", "examples"):
        paths.update(path.relative_to(ROOT).as_posix() for path in safe_path(directory).rglob("*")
                     if path.is_file() and path.suffix in (".py", ".json", ".yml", ".yaml")
                     and "__pycache__" not in path.parts)
    return paths


def measure():
    evidence = Evidence()
    claims = evidence.document(CLAIMS) or {}
    targets = evidence.document(TARGETS) or {}
    for relative in (RUNNER, AGENTS, SKILL, PROVINCE, LOG, SCORECARD, AUDIT, DOSSIER,
                     SWEEP, SWEEP_RECEIPT, SWEEP_COMMANDS):
        evidence.text(relative)
    runtime_before = runtime_paths()
    baseline = claims.get("baseline_revision")
    before = protected_snapshot(baseline)
    matrix, _source, _fallback = declared_matrix(evidence)

    def matrix_run(row):
        name, tokens = row
        parts = command_target(tokens)
        if not isinstance(parts, list):
            return {"name": name, "command": shlex.join(tokens), "date": today(),
                    "passed": False, "exit_code": None, "error": "command not re-runnable"}
        return run_command(name, parts, tmpdir=rerun_tmpdir(shlex.join(tokens)))

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        runs = list(pool.map(matrix_run, matrix))
    after = protected_snapshot(baseline)
    preservation = result(before["failures"] + after["failures"], {"before": before, "after": after})
    results = {}
    for claim_id, operation in (
            ("C", lambda: measure_completion(evidence, claims)),
            ("O", lambda: measure_sweep(evidence, claims, runs)),
            ("D", lambda: measure_dossier(evidence, claims))):
        try:
            results[claim_id] = operation()
        except (OSError, ValueError, TypeError, KeyError, RuntimeError, AttributeError,
                subprocess.SubprocessError) as error:
            results[claim_id] = result([f"could-not-evaluate: {type(error).__name__}: {error}"], {})
    coherence = []
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"C": "calibration", "O": "operability", "D": "depth"}:
        coherence.append("declared claims must be C/calibration, O/operability, D/depth")
    if claims.get("round") != 32 or targets.get("round") != 32 \
            or targets.get("baseline_revision") != baseline:
        coherence.append("claims and targets disagree on round or baseline")
    if sum(targets.get("workers", {}).values()) != claims.get("workers"):
        coherence.append("target worker allocation does not sum to the declared wave")
    runtime_after = runtime_paths()
    if runtime_before != runtime_after:
        coherence.append("runtime input path set changed during measurement: "
                         + ", ".join(sorted(runtime_before ^ runtime_after)))
    changed = []
    for relative, digest in evidence.inputs.items():
        resolver = fleet_path if relative.startswith("fleet:") else safe_path
        try:
            observed = sha(resolver(relative.removeprefix("fleet:")).read_bytes())
        except (OSError, ValueError):
            observed = None
        if observed != digest:
            changed.append(relative)
    if changed:
        coherence.append("evidence changed during measurement: " + ", ".join(sorted(changed)))
    coherence.extend(evidence.errors)
    if not preservation["passed"]:
        coherence.extend(preservation["failures"])
    failures = [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                for failure in item["failures"]]
    failures.extend("evidence: " + failure for failure in coherence)
    return {"round": 32, "runner": RUNNER, "runner_sha256": evidence.inputs.get(RUNNER),
            "counting_command": COMMAND, "date": today(), "measured_at_utc": now(),
            "baseline_revision": baseline, "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results, "failures": failures,
            "missing_dependencies": sorted(evidence.missing | set(dependencies_ready())),
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": ["Read-only evidence checks plus re-execution of the declared green sweep; "
                       "not a canon or promotion decision.",
                       "The completion audit is re-verified from raw sources (fleet reports under the "
                       "fleet root, fleet MANIFEST.json, SCORECARD.md, LOG.md, lane git); filed prose "
                       "is not trusted without an independent recount.",
                       "The declared sweep matrix is loaded from this round's sweep receipt; a load "
                       "failure falls back to the settled r31 green surface plus this runner's "
                       "selftest and is reported.",
                       "Recorded sweep commands are re-executed only under a strict whitelist; "
                       "python3 -c snippets are parsed but not re-executed; this runner is never "
                       "re-invoked except as --selftest. Exit codes arbitrate the green sweep.",
                       "The 13 filed-red historical replay controls are checked at their recorded "
                       "codes; a reproduced red verdict stays red.",
                       "Every matrix and rerun command is recorded with date, tmpdir, exit and output "
                       "digests; replay legs use the authorized /var/tmp mirror-safety storage.",
                       "The final dossier is decision evidence for the operator, not a promotion "
                       "verdict; the dossier claiming the SHONEN checklist complete is a live "
                       "falsifier.",
                       "In-flight evidence changes invalidate acceptance; rerun after the orchestrator "
                       "finishes landing."]} 


def selftest():
    checks = []
    def check(name, value):
        checks.append({"control": name, "passed": bool(value)})
    def raises(function, *args):
        try:
            function(*args)
            return False
        except (ValueError, TypeError):
            return True
    check("duplicate-json-key-refused", raises(strict_json, '{"id": 1, "id": 2}'))
    check("absolute-path-refused", raises(safe_path, "/var/tmp/a"))
    check("traversal-path-refused", raises(safe_path, "reports/../a"))
    check("git-path-refused", raises(safe_path, ".git/config"))
    check("absolute-fleet-path-refused", raises(fleet_path, "/etc/hostname"))
    check("fleet-traversal-refused", raises(fleet_path, "../MANIFEST.json"))
    check("fleet-git-refused", raises(fleet_path, ".git/config"))
    check("normal-path-accepted", safe_path(CLAIMS) == ROOT / CLAIMS)
    four = ("# r\n## Work performed\n## Landed changes\n## Before → after measurements\n## SHONEN\n")
    three = ("# r\n## Work performed\n## Before -> after measurements\n## SHONEN\n")
    check("four-section-report-accepted", len(sections_of(four)) == 4)
    check("arrow-normalized-three-section-detected", sections_of(three)
          == {"Work performed", "Before → after measurements", "SHONEN"})
    check("prose-sections-not-headings", sections_of("Work performed\nSHONEN") == set())
    manifest = {"rounds": [
        {"round": 30, "type": "closure", "lanes": {"kotodama": "ok"},
         "lane_rounds": {"kotodama": 30}, "verdicts": {"depth": "improved"}},
        {"round": 13, "type": "closure", "lanes": {"kotodama": "skipped"}, "verdicts": None},
        {"round": 40, "type": "closure", "lanes": {"kaidoku": "ok"},
         "lane_rounds": {"kaidoku": 40}, "verdicts": {"depth": "improved"}},
    ]}
    index = koto_entries_by_round(manifest)
    check("koto-index-excludes-other-lanes", set(index) == {30, 13})
    check("closure-entry-filter", [entry["round"] for entry in closure_entries(index, 30)] == [30]
          and closure_entries(index, 40) == [])
    check("skipped-round-classifier", skipped_rounds(index) == {13})
    check("commit-token-classifier", commit_status("zzzz")["exists"] is False
          and commit_status("a" * 41)["exists"] is False)
    table_row = ("| d2-assembly-check | assemblers | `python3 -B tools/assemble-d2.py --check` "
                 "| 0 | `2fa0c8c197459f54…` |\n")
    parsed = parse_sweep_table(table_row)
    check("sweep-table-row-parsed", parsed == [{"id": "d2-assembly-check", "family": "assemblers",
          "command": "python3 -B tools/assemble-d2.py --check", "exit": 0,
          "sha16": "2fa0c8c197459f54", "dated": False}])
    check("sweep-table-row-without-digest-skipped",
          parse_sweep_table("| x | y | `python3 tools/a.py` | 0 |  | \n") == [])
    check("final-sweep-parses-records", parse_final_sweep(
        "```\n$ python3 -B tools/check-gate-battery.py --selftest\nexit 0\n2026-10-18 sha256 256"
        " chars omitted\n```\n")[0]["exit0"] is True)
    check("rerun-tmpdir-mirror-legs", rerun_tmpdir("python3 -B tools/replay-frozen.py m.tsv")
          == "/var/tmp" and rerun_tmpdir("python3 -B tools/assemble-d2.py --check") is None)
    check("whitelist-accepts-tool-command", whitelist_rerun(
        {"command": "python3 -B tools/check-gate-battery.py --selftest"}) == "allowed")
    check("whitelist-accepts-harness-selftest", whitelist_rerun(
        {"command": f"python3 -B {RUNNER} --selftest"}) == "allowed")
    check("whitelist-refuses-recursive-runner", whitelist_rerun(
        {"command": f"python3 -B {RUNNER}"}) == "refused-recursive-runner")
    check("whitelist-refuses-shell", whitelist_rerun(
        {"command": "python3 -B tools/x.py --check; rm -rf /"}) == "refused")
    check("whitelist-refuses-foreign-root", whitelist_rerun(
        {"command": "python3 ../elsewhere/tool.py"}) == "refused")
    check("whitelist-skips-stdin-code", whitelist_rerun(
        {"command": "python3 -c \"import glob\""}) == "skipped-stdin-code")
    fake_battery = {"gate": "register-law-gate.py", "summary": {"pass": 10, "fail": 0, "unevaluable": 0},
                    "baselines": {"summary": {"coverage": "10/10", "pinned": 10,
                                              "baselines_found": 10, "gates_uncovered": []}}}
    check("ten-of-ten-battery-accepted", battery_check(
        {"exit_code": 0, "stdout": json.dumps(fake_battery)})["passed"])
    fake_battery["baselines"]["summary"]["coverage"] = "9/10"
    check("nine-of-ten-battery-refused", not battery_check(
        {"exit_code": 0, "stdout": json.dumps(fake_battery)})["passed"])
    check("failed-battery-refused", not battery_check({"exit_code": 1, "stdout": "{}"})["passed"])
    controls = [{"expect_exit": 2}] * 8 + [{"expect_exit": 1}] * 5
    codes = Counter(row["expect_exit"] for row in controls)
    check("filed-red-distribution-accepted", codes.get(1, 0) >= MIN_RED_CODE_1
          and codes.get(2, 0) >= MIN_RED_CODE_2 and len(controls) >= MIN_CONTROLS)
    check("shrunken-control-set-refused", not ({f"c{i}" for i in range(13)}
          <= {"c1", "c2"}))
    capabilities_text = ("## Capabilities\n\n| name | demonstrated behavior | command | first |\n"
                         "|---|---|---|---|\n| gate battery | ten controls | `python3 tools/x.py` | r5 |\n"
                         "| frozen replay | digests | `tools/replay-frozen.py` | r3 |\n")
    check("capability-table-parsed", scorecard_capabilities(capabilities_text)
          == ["gate battery", "frozen replay"])
    check("capability-token-fallback-matches-paraphrase",
          all(t in "| bounded typed CLI (exit-2) | `python3 -B tools/check-craft-exercise.py x` |".lower()
              for t in ["bounded", "typed", "craft", "cli"])
          and bool(re.search(r"`[^`]*(?:python3|tools/)[^`]*`",
                             "| bounded typed CLI (exit-2) | `python3 -B tools/check-craft-exercise.py x` |")))
    check("capability-token-fallback-refuses-commandless-row",
          not re.search(r"`[^`]*(?:python3|tools/)[^`]*`",
                        "| bounded typed craft CLI | described only |"))
    check("scorecard-section-extractor", (scorecard_section(
        "## Axes — round 24 (2026-10-18)\n| depth | 3 → 4 |\n## Axes — round 25\n", 24)
        .count("→") == 1))
    dossier_ok = ("# Final dossier (2026-10-18)\nbox 1 closed by the r30 Register-craft survey; "
                  "boxes 2-4 restate the r24 promotion-review verdicts with rounds 25-31 evidence; "
                  "counting command `python3 reports/round-32/run-validation.py`; no promotion is "
                  "claimed here — this file is the operator's decision evidence.\n"
                  "| gate battery | `python3 tools/x.py` |\n")
    check("dossier-features-accepted",
          bool(DATE_RE.search(dossier_ok))
          and bool(re.search(r"(?i)no promotion", dossier_ok))
          and not re.search(r"(?i)(?:all (?:four|4)|4/4)\s+(?:boxes|shonen|promotion)[^\n]{0,60}"
                            r"(?:pass|satisf|complete|cleared|\[x\])", dossier_ok))
    dossier_bad = dossier_ok + "\nThe promotion checklist: all four boxes pass.\n"
    check("promotion-complete-falsifier-detected",
          bool(re.search(r"(?i)(?:all (?:four|4)|4/4)\s+(?:boxes|shonen|promotion)[^\n]{0,60}"
                         r"(?:pass|satisf|complete|cleared|\[x\])", dossier_bad)))
    check("protected-includes-round31", "reports/round-31" in PROTECTED
          and "tools/gates/frozen/round-26" in PROTECTED)
    check("current-round-not-protected", "reports/round-32" not in PROTECTED)
    passed = sum(row["passed"] for row in checks)
    receipt = {"command": f"{COMMAND} --selftest", "date": today(), "passed_controls": passed,
               "total_controls": len(checks), "passed": passed == len(checks), "controls": checks}
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["passed"] else 1


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="print measured JSON without publishing validation.json")
    mode.add_argument("--selftest", action="store_true", help="run dependency-free positive/negative acceptance controls")
    parser.add_argument("--wait", type=int, default=0, metavar="SECONDS",
                        help="poll late dependencies every 60s, at most 900s")
    args = parser.parse_args(argv)
    if args.wait < 0:
        parser.error("--wait must be nonnegative")
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    if args.selftest:
        return selftest()
    if not args.check:
        guard_receipt()
    if args.wait:
        deadline = time.monotonic() + min(args.wait, 900)
        while True:
            pending = dependencies_ready()
            remaining = deadline - time.monotonic()
            if not pending or remaining <= 0:
                break
            print("waiting on dependencies: " + ", ".join(pending), file=sys.stderr, flush=True)
            time.sleep(min(60, remaining))
    try:
        receipt = measure()
    except (OSError, ValueError, TypeError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"could-not-evaluate: {type(error).__name__}: {error}", file=sys.stderr)
        return 2
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        guard_receipt()
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        print(f"receipt: {OUTPUT}")
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
