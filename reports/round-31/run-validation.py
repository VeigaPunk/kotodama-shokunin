#!/usr/bin/env python3
"""Measure round-31 C/O/D close-out acceptance; --check never publishes a receipt."""
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
import tempfile
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
FLEET_ROOT = ROOT.parent
ROUND = "reports/round-31"
RUNNER = f"{ROUND}/run-validation.py"
OUTPUT = f"{ROUND}/validation.json"
COMMAND = f"python3 {RUNNER}"
CLAIMS = f"{ROUND}/claims.json"
TARGETS = f"{ROUND}/targets.json"
LEDGER = f"{ROUND}/closure-ledger.json"
SWEEP = f"{ROUND}/final-sweep.md"
SWEEP_RECEIPT = f"{ROUND}/sweep/sweep-receipt.json"
SWEEP_COMMANDS = f"{ROUND}/sweep/commands.txt"
ANALYSIS = f"{ROUND}/jinii/analysis.md"
DRAFT = f"{ROUND}/jinii/draft.md"
SWEEP_AUDIT = f"{ROUND}/sweep-audit.py"
LOG = "LOG.md"
AGENTS = "AGENTS.md"
SKILL = "SKILL.md"
PROVINCE = "PROVINCE.md"
FLEET_REPORT = ".ufo/reports/round-{n}/kotodama.md"
FLEET_MANIFEST = "MANIFEST.json"
LANE = "kotodama"
REGIMEN = tuple(range(8, 32))
CLOSED = tuple(range(8, 31))
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 31)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 31))
SECTIONS = (
    (r"work\s+performed", "Work performed"),
    (r"landed\s+changes", "Landed changes"),
    (r"before\s*(?:→|->)\s*after\s+measurements", "Before → after measurements"),
    (r"shonen", "SHONEN"),
)
RULE_MARKER = "Close what you open"
CHECKLIST_MARKER = "closing snapshot"
OPEN_AT_DRAFT = {19, 25, 26, 27, 28}
POST_LANDING_OPEN = {31, 32}
VERDICT_COUNTS = {
    "closed-admitted": "closed_admitted",
    "closed-rejected": "closed_rejected",
    "closed-with-finding": "closed_with_finding",
    "skipped-operator": "operator_skipped",
}
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}")
SHA256_RE = re.compile(r"\b[0-9a-f]{64}\b")
HEX_COMMIT_RE = re.compile(r"\b[0-9a-f]{7,40}\b")
FULL_COMMIT_RE = re.compile(r"\b[0-9a-f]{40}\b")
CMD_RE = re.compile(r"(?m)^\s*(?:\$\s*)?(python3(?:\s+-B)?\s+\S[^\n]*)$")
BATTERY = "tools/check-gate-battery.py"
PACKET = "examples/culture-d4/packet.d4.yml"
FALLBACK_MATRIX = (
    ("battery-selftest", BATTERY, "--selftest"),
    ("battery", BATTERY),
    ("d2-assembly", "tools/assemble-d2.py", "--check"),
    ("d2-adapter", "tools/assemble-d2-typed.py", "--check"),
    ("d3-assembly", "tools/assemble-culture-d3.py", "--check"),
    ("d4-assembly", "tools/assemble-culture-d4.py", "--check"),
    ("d4-adapter", "tools/assemble-d4-typed.py", "--check", "examples/culture-d4/packet.d4.typed.yml"),
    ("d2-projection", "tools/d2-typed-labels.py", "--check"),
    ("d4-projection", "tools/d2-typed-labels.py", "--packet", PACKET, "--check", "examples/culture-d4/typed-labels.d4.yml"),
    ("typed-d2", "tools/gates/typed-pipeline-gate.py"),
    ("typed-d4", "tools/gates/typed-pipeline-gate.py", PACKET),
    ("d4-label-gate", "tools/gates/d4-typed-labels-check-gate.py", "examples/culture-d4/typed-labels.d4.yml"),
    ("d4-assembly-gate", "tools/gates/d4-assembly-check-gate.py", PACKET),
    ("argot-d4", "tools/gates/argot-derivation-gate.py", PACKET),
    ("law-clean", "tools/gates/register-law-gate.py", "--packet", PACKET),
    ("replay-selftest", "tools/replay-frozen.py", "--selftest"),
    ("handoff-v2", "tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet"),
    ("handoff-v3", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet"),
    ("craft", "tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json"),
    ("links-selftest", "tools/harness/packet_links.py", "--selftest"),
    ("uncertainty-selftest", "tools/harness/packet_uncertainty.py", "--selftest"),
)
EXTERNAL_TMP = {"frozen-replay-selftest", "replay-selftest"}
NONDETERMINISTIC_STDOUT = {"battery", "pin-repoint-selftest"}


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


def baseline_text(revision, relative):
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        raise ValueError("declared baseline must be a full Git revision")
    proc = git("show", f"{revision}:{relative}")
    if proc.returncode:
        raise ValueError(f"cannot read {relative} at baseline {revision}")
    return proc.stdout.decode("utf-8")


def protected_snapshot(revision):
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
    # sanctioned retroactive act (LOG.md 2026-10-18, the jin'i-ryu gate entry):
    # the telemetry finalization-closure rule's closing snapshots are NEW files
    # under the filed rounds' telemetry/ dirs — the rule's own retroactive act.
    additions = [a for a in additions
                 if not (a.startswith("reports/round-") and "/telemetry/availability-close-" in a)]
    failures = ["filed rounds 8-30 or their frozen generations changed"] if changes or additions else []
    return result(failures, {"baseline_revision": revision,
                            "protected_files": metric(len(expected), "git ls-tree of filed report/frozen paths"),
                            "differences": changes, "new_protected_paths": additions})


def run_command(name, parts, tmpdir=None):
    argv = [sys.executable, "-B", *parts]
    if tmpdir is None:
        tmpdir = "/var/tmp" if name in EXTERNAL_TMP else str(ROOT / ".scratch")
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


def load_matrix(evidence):
    try:
        namespace = runpy.run_path(str(safe_path(SWEEP_AUDIT)))
        matrix = tuple(tuple(row) for row in namespace["MATRIX"])
        external = frozenset(namespace.get("EXTERNAL_TMP", ()))
        return matrix, external, f"runpy:{SWEEP_AUDIT}", []
    except (OSError, ValueError, KeyError, TypeError) as error:
        return FALLBACK_MATRIX, frozenset(EXTERNAL_TMP), "fallback:run-validation.py", [
            f"sweep matrix fell back to the runner's copy: {SWEEP_AUDIT}: {error}"]


def sections_of(report_text):
    headings = set()
    for line in report_text.splitlines():
        arrow = line.replace("->", "→")
        for pattern, name in SECTIONS:
            if re.fullmatch(r"\s*#{1,6}\s+" + pattern + r"\s*", arrow, re.I):
                headings.add(name)
    return headings


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


SWEEP_TABLE_ROW_RE = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]{8,64})[^`|]*`\s*\|")


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


def rerun_tmpdir(command):
    return "/var/tmp" if re.search(r"replay-frozen|freeze-r31", command) else None


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


def whitelist_rerun(record):
    try:
        tokens = shlex.split(record["command"])
    except ValueError:
        return "refused"
    if not tokens or tokens[0] != "python3":
        return "refused"
    rest = tokens[1:]
    if rest and rest[0] == "-B":
        rest = rest[1:]
    if not rest:
        return "refused"
    if rest[0] == "-c":
        return "skipped-stdin-code"
    target = rest[0]
    if not (target.startswith("tools/") or target.startswith("examples/")
            or re.fullmatch(r"reports/round-\d+/[A-Za-z0-9_./\-]+\.py", target)) or ".." in target:
        return "refused"
    if any(not re.fullmatch(r"[A-Za-z0-9_@=/:.,+\-]+", token) for token in rest[1:]):
        return "refused"
    return "allowed"


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


def closure_entries(index, round_no, require_verdicts=True):
    return [entry for entry in lane_round_entries(index, round_no)
            if entry.get("type") == "closure"
            and (entry.get("verdicts") or not require_verdicts)]


def audit_artifacts(evidence):
    found = []
    for path in sorted(safe_path(ROUND).glob("closure-audit-*.md")):
        relative = path.relative_to(ROOT).as_posix()
        text = evidence.text(relative)
        passes = len(re.findall(r"(?m)^### round \d+ — PASS\s*$", text))
        found.append({"path": relative, "dated": bool(DATE_RE.search(text)),
                      "names_ledger": LEDGER in text, "pass_rows": passes,
                      "verdict": bool(re.search(r"(?m)^`?verify`?\s*[—-]", text)
                                      or re.search(r"(?im)^##\s*verdict\b", text)),
                      "passed": bool(DATE_RE.search(text) and LEDGER in text
                                     and passes >= 5 and re.search(r"(?im)^##\s*verdict\b", text))})
    return found


def ledger_rounds(ledger, key):
    rows = ledger.get(key)
    return {row.get("round"): row for row in rows if isinstance(row, dict)} if isinstance(rows, list) else {}


def recompute_counts(rows_closed):
    counts = Counter(VERDICT_COUNTS.get(row.get("verdict")) for row in rows_closed.values())
    counts.pop(None, None)
    return counts


def measure_closure(evidence, claims):
    failures = []
    ledger = evidence.document(LEDGER)
    if not ledger:
        return result([f"{LEDGER} missing or unparseable (C-closure seat dependency)"], {})
    for key in ("artifact", "claim", "audited_at", "auditor", "lane_head", "baseline_revision",
                "rounds_1_7", "rounds_8_31", "round_32", "findings", "counts_summary",
                "zero_missing_rows", "claim_C_verdict", "method"):
        if key not in ledger:
            failures.append(f"closure ledger missing key: {key}")
    if not str(ledger.get("auditor", "")).strip():
        failures.append("closure ledger names no auditor")
    if not DATE_RE.search(str(ledger.get("audited_at", ""))):
        failures.append("closure ledger audited_at carries no date")
    method_blob = json.dumps(ledger.get("method", {}), ensure_ascii=False)
    if not DATE_RE.search(method_blob) or "git " not in method_blob:
        failures.append("ledger method lacks dated audit commands")
    head = commit_status(str(ledger.get("lane_head", "")))
    if not (head["exists"] and head["ancestor"]):
        failures.append("ledger lane_head is not an ancestor of the current lane HEAD")
    if ledger.get("baseline_revision") != claims.get("baseline_revision"):
        failures.append("ledger baseline disagrees with claims.json")
    fleet_manifest = evidence.fleet_document(FLEET_MANIFEST)
    if not fleet_manifest:
        return result(failures + ["fleet MANIFEST.json unreadable"], {})
    index = koto_entries_by_round(fleet_manifest)

    retro = ledger_rounds(ledger, "rounds_1_7")
    if set(retro) != set(range(1, 8)):
        failures.append("retro rows must cover rounds 1-7 exactly")
    retro_ok = 0
    for number, row in sorted(retro.items()):
        entries = [entry for entry in index.get(number, [])
                   if entry.get("type") in ("retroactive-closure", "closure")]
        count = row.get("manfiest_entries_count", row.get("manifest_entries_count", 0))
        if row.get("row_present") and row.get("reconfirmed") and entries and count >= 1:
            retro_ok += 1
        else:
            failures.append(f"retro row round {number} not reconfirmed against fleet MANIFEST")
    findings = {finding.get("round"): finding for finding in ledger.get("findings", [])
                if isinstance(finding, dict)}

    rows_closed = {number: row for number, row in ledger_rounds(ledger, "rounds_8_31").items()
                   if number in CLOSED}
    if set(rows_closed) != set(CLOSED):
        failures.append("rounds 8-30 must each carry exactly one closure-ledger row")
    present, full_sections, ancestry_rows, workcommit_rows, manifest_rows = 0, 0, 0, 0, 0
    for number, row in sorted(rows_closed.items()):
        verdict = row.get("verdict")
        if verdict not in VERDICT_COUNTS:
            failures.append(f"round {number}: unknown ledger verdict {verdict!r}")
            continue
        skipped = verdict == "skipped-operator"
        closure = closure_entries(index, number, require_verdicts=not skipped)
        if not closure:
            failures.append(f"round {number}: no kotodama closure entry in fleet MANIFEST")
        else:
            manifest_rows += 1
        report_text = ""
        if skipped:
            finding = findings.get(number, {})
            finding_blob = json.dumps(finding, ensure_ascii=False)
            if row.get("report_exists") is not False:
                failures.append(f"round {number}: operator-skipped row must not claim a fleet report")
            if fleet_path(FLEET_REPORT.format(n=number)).is_file():
                failures.append(f"round {number}: fleet report exists for an operator-skipped round")
            if not (str(finding.get("finding", "")).strip() and DATE_RE.search(finding_blob)):
                failures.append(f"round {number}: operator skip lacks a dated finding")
        else:
            report_text = evidence.fleet_text(FLEET_REPORT.format(n=number))
            if not report_text:
                failures.append(f"round {number}: fleet report missing at {FLEET_REPORT.format(n=number)}")
            else:
                present += 1
                headings = sections_of(report_text)
                if headings == {name for _pattern, name in SECTIONS}:
                    full_sections += 1
                elif number == 23 and findings.get(23, {}).get("id") == "F-C31-1" \
                        and headings == {"Work performed", "Before → after measurements", "SHONEN"} \
                        and DATE_RE.search(json.dumps(findings[23], ensure_ascii=False)):
                    pass  # recorded finding F-C31-1, disposition recorded-not-repaired
                else:
                    failures.append(f"round {number}: fleet report carries {len(headings)}/4 required sections")
        cited = row.get("commits_cited_existing") or {}
        ok = bool(cited) and all(commit_status(token)["exists"] and commit_status(token)["ancestor"]
                                 for token in cited)
        if not skipped:
            ancestry_rows += ok
            if not ok:
                failures.append(f"round {number}: a cited commit fails existence/ancestry re-verification")
            if not row.get("commit_ancestry_ok"):
                failures.append(f"round {number}: ledger claims unverified commit ancestry")
        notes = " ".join(str(entry.get("notes", "")) for entry in closure)
        work = FULL_COMMIT_RE.search(notes)
        if work:
            workcommit_rows += 1
            token = work.group(0)
            status = commit_status(token)
            if not (status["exists"] and status["ancestor"]):
                failures.append(f"round {number}: MANIFEST work commit fails ancestry")
            if report_text and not any(form in report_text for form in
                                       (token, token[:7], token[:8], token[:12])):
                failures.append(f"round {number}: MANIFEST work commit is not cited in the fleet report")
    row31 = ledger_rounds(ledger, "rounds_8_31").get(31, {})
    if row31.get("verdict") != "in-flight" or not str(row31.get("expected_resolution", "")).strip():
        failures.append("round-31 row must be in-flight with an expected resolution")
    if fleet_path(FLEET_REPORT.format(n=31)).is_file():
        failures.append("round-31 fleet report exists while the ledger row is in-flight")
    if closure_entries(index, 31):
        failures.append("round 31 already carries a MANIFEST closure entry (in-flight)")
    slot32 = ledger.get("round_32") or {}
    if slot32.get("status") != "pending-by-construction":
        failures.append("round-32 slot must be pending-by-construction")
    if fleet_path(FLEET_REPORT.format(n=32)).is_file():
        failures.append("round-32 fleet report already exists")
    if closure_entries(index, 32):
        failures.append("round 32 already carries a MANIFEST closure entry")
    if ledger.get("zero_missing_rows") is not True:
        failures.append("ledger does not assert zero missing rows")
    counts = recompute_counts(rows_closed)
    summary = ledger.get("counts_summary", {})
    for verdict, key in VERDICT_COUNTS.items():
        if summary.get(key, {}).get("value") != counts[key]:
            failures.append(f"counts_summary.{key} disagrees with the ledger's own verdicts "
                            f"({summary.get(key, {}).get('value')} != {counts[key]})")
    if summary.get("rows_rounds_1_7_reconfirmed", {}).get("value") != retro_ok:
        failures.append("counts_summary retro row count disagrees with re-confirmation")
    if summary.get("rounds_8_30_audited", {}).get("value") != len(rows_closed):
        failures.append("counts_summary audited-round count disagrees with rows 8-30")
    if summary.get("fleet_reports_present", {}).get("value") != present:
        failures.append("counts_summary fleet-report count disagrees with the independent recount")
    if summary.get("sections_fully_valid", {}).get("value") != full_sections:
        failures.append("counts_summary full-section count disagrees with the independent recount")
    if summary.get("manifest_closure_entries_8_31", {}).get("value") != manifest_rows:
        failures.append("counts_summary MANIFEST closure-entry count disagrees with the recount")
    if summary.get("missing_rows", {}).get("value") != 0:
        failures.append("counts_summary missing_rows is not zero")
    verdict_doc = ledger.get("claim_C_verdict", {})
    if not str(verdict_doc.get("status", "")).startswith("verify") \
            or not str(verdict_doc.get("falsification", "")).strip():
        failures.append("claim_C_verdict lacks a verify-status and a falsification statement")
    auditors = audit_artifacts(evidence)
    if not any(row["passed"] for row in auditors):
        failures.append("no dated independent closure-audit artifact re-verifies ledger rows (auditor seat)")
    if not findings:
        failures.append("closure ledger records no findings")
    return result(failures, {
        "ledger_sha256": evidence.inputs.get(LEDGER),
        "lane_head": ledger.get("lane_head"), "lane_head_ancient_of_head": head,
        "retro_rows_reconfirmed": metric(retro_ok, "retro rows 1-7 re-confirmed"),
        "rounds_8_30_rows": metric(len(rows_closed), "ledger rows for rounds 8-30"),
        "verdict_counts": metric(dict(counts), "verdict recount"),
        "fleet_reports_present": metric(present, "independent fleet-report recount"),
        "sections_fully_valid": metric(full_sections, "independent 4-section recount"),
        "commit_ancestry_rows": metric(ancestry_rows, "rows whose cited commits re-verified"),
        "manifest_closure_entries_8_31": metric(manifest_rows, "independent MANIFEST closure-entry recount"),
        "round_31": {"verdict": row31.get("verdict"),
                     "expected_resolution_present": bool(row31.get("expected_resolution"))},
        "round_32_slot": slot32,
        "findings": metric(len(findings), "ledger findings"),
        "independent_auditors": auditors,
        "qualified_auditors": metric(sum(row["passed"] for row in auditors),
                                     "dated independent closure auditors"),
    })


def measure_sweep(evidence, claims, runs):
    failures = []
    matrix, external, matrix_source, matrix_failures = load_matrix(evidence)
    failures.extend(matrix_failures)
    expected_families = {Path(row[1]).name for row in matrix}
    green = [row for row in runs if row["passed"]]
    for row in runs:
        if not row["passed"]:
            failures.append(f"final-sweep matrix command {row['name']} exited {row['exit_code']}")
    battery = battery_check(next((row for row in runs if row["name"] == "battery"), {}))
    if not battery["passed"]:
        failures.append("gate battery is not 10/10 with the law gate registered")
    sweep_text = evidence.text(SWEEP)
    sweep_present = bool(sweep_text)
    if not sweep_present:
        failures.append(f"{SWEEP} missing (O builder seat dependency)")
    table = parse_sweep_table(sweep_text) if sweep_present else []
    lines = parse_final_sweep(sweep_text) if sweep_present else []
    receipt = evidence.document(SWEEP_RECEIPT) if sweep_present else None
    if sweep_present and not receipt:
        failures.append(f"{SWEEP_RECEIPT} missing or unparseable (machine receipt leg)")
    receipt_rows = {row.get("id"): row for row in (receipt or {}).get("rows", [])
                    if isinstance(row, dict)}
    bound, unbound = 0, []
    for record in table:
        row = receipt_rows.get(record["id"])
        if record["exit"] != 0:
            continue
        if not row:
            unbound.append(record["id"])
            continue
        if (row.get("exit_code") == 0 and row.get("passed") is True
                and DATE_RE.search(str(row.get("date", "")))
                and str(row.get("stdout_sha256", "")).startswith(record["sha16"])):
            bound += 1
        else:
            unbound.append(record["id"])
    if table and unbound:
        failures.append(f"{len(unbound)} final-sweep green row(s) do not bind to dated exit-0 "
                        f"receipt rows with matching output digests: {unbound[:6]}")
    covered = set()
    for record in table:
        if record["exit"] != 0:
            continue
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
    if sweep_present and receipt and len(controls) < 10:
        failures.append(f"fewer than 10 declared historical replay controls in the receipt "
                        f"({len(controls)})")
    if deviating:
        failures.append("historical control rows deviate from their expected filed-red codes: "
                        + ", ".join(deviating))
    rerun = []
    if sweep_present:
        commands = [line.strip() for line in evidence.text(SWEEP_COMMANDS).splitlines()
                    if line.strip() and not line.strip().startswith("#")]
        if not commands:
            failures.append(f"{SWEEP_COMMANDS} manifest missing or empty (re-runnable leg)")
        for command in commands:
            disposition = whitelist_rerun({"command": command})
            if disposition == "allowed":
                try:
                    tokens = shlex.split(command)
                except ValueError:
                    continue
                parts = tokens[1:]
                if parts and parts[0] == "-B":
                    parts = parts[1:]
                item = run_command("sweep:" + Path(parts[0]).name, parts,
                                   tmpdir=rerun_tmpdir(command))
                item["recorded"] = True
                if not item["passed"]:
                    failures.append(f"recorded sweep command does not reproduce: {command[:90]}")
                rerun.append(item)
            else:
                rerun.append({"command": command, "rerun": disposition,
                              "date": today(), "passed": disposition == "skipped-stdin-code"})
                if disposition != "skipped-stdin-code":
                    failures.append(f"recorded command not re-runnable under the safety whitelist: "
                                    f"{command[:90]}")
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
        audits.append({"path": relative, "date": document.get("date"), "leg": document.get("leg"),
                       "rows": len(rows), "failed_rows": red,
                       "passed": bool(DATE_RE.search(str(document.get("date", ""))))
                       and not red})
    cross = evidence.document(f"{ROUND}/sweep-audit-O09O10.json") or {}
    benign = all(re.search(r"digest-mismatch-between-passes", str(finding.get("kind", "")))
                 for finding in cross.get("cross_pass_findings", []))
    passes = cross.get("passes", {})
    cross_green = (passes.get("O09", {}).get("exit0_count") == passes.get("O10", {}).get("exit0_count")
                   == len(matrix))
    cross_ok = benign and cross_green and not cross.get("source_drift_during_audit")
    if len([row for row in audits if row["passed"]]) < 2:
        failures.append("fewer than two dated independent sweep-audit legs with zero red rows")
    if not cross_ok:
        failures.append("cross-pass sweep audit reports non-digest findings, source drift, "
                        "or unequal green counts")
    return result(failures, {
        "matrix_source": matrix_source,
        "matrix_size": metric(len(matrix), "canonical final-sweep matrix size"),
        "matrix_green": metric(len(green), "matrix commands exiting 0"),
        "battery_registration": battery,
        "final_sweep_present": sweep_present,
        "recorded_table_rows": metric(len(table), "green table rows parsed from final-sweep.md"),
        "receipt_bound_rows": metric(bound, "final-sweep rows bound to dated green receipt rows"),
        "receipt_rows": metric(len(receipt_rows), "sweep-receipt rows"),
        "historical_controls": metric(len(controls), "expected-red replay control rows"),
        "families_covered": metric(len(covered & expected_families), "sweep families re-recorded"),
        "recorded_manifest_commands": metric(len([row for row in rerun if row.get("recorded")]),
                                             "commands.txt commands re-executed"),
        "recorded_reruns": rerun,
        "independent_audits": audits,
        "cross_pass_ok": cross_ok,
        "cross_pass_digest_mismatches": [finding.get("command") for finding in
                                         cross.get("cross_pass_findings", [])],
        "nondeterministic_stdout_families": sorted(NONDETERMINISTIC_STDOUT),
    })



def open_availability_rows(evidence):
    rows = []
    for path in sorted(ROOT.glob("reports/round-*/availability*.json")):
        relative = path.relative_to(ROOT).as_posix()
        match = re.fullmatch(r"round-(\d+)", path.parent.name)
        try:
            document = strict_json(path.read_text(encoding="utf-8"))
        except (OSError, ValueError, UnicodeError):
            continue
        if not isinstance(document, dict) or document.get("state") != "open-at-seat-close":
            continue
        receipt = path.parent / "validation.json"
        # the landed closure rule (SKILL.md checklist, amended 2026-10-18): an
        # open-at-seat-close record whose telemetry closing snapshot exists is
        # CLOSED — the snapshot is the disposition, never an in-place edit
        closed_by_snapshot = (path.parent / "telemetry" / f"availability-close-{path.parent.name.split('-')[1]}.json").is_file()
        if closed_by_snapshot:
            continue
        rows.append({"path": relative, "round": int(match.group(1)) if match else None,
                     "completed_workers": document.get("completed_workers"),
                     "has_finalization_note": bool(document.get("finalization_note")),
                     "receipt_landed": receipt.is_file()})
    return rows


def closing_snapshots(evidence):
    checks = []
    for path in sorted(ROOT.glob("reports/round-*/telemetry/availability-close*.json")):
        relative = path.relative_to(ROOT).as_posix()
        try:
            document = strict_json(path.read_text(encoding="utf-8"))
        except (OSError, ValueError, UnicodeError) as error:
            checks.append({"path": relative, "passed": False, "error": str(error)})
            continue
        closes = document.get("closes")
        digest = document.get("closes_sha256")
        live = ""
        if isinstance(closes, str) and closes:
            try:
                live = sha(safe_path(closes).read_bytes())
            except (OSError, ValueError):
                live = ""
        tracked = git("show", f"HEAD:{closes}") if isinstance(closes, str) and closes else None
        unchanged = None
        if tracked is not None:
            unchanged = tracked.returncode == 0 and tracked.stdout == safe_path(closes).read_bytes()
        checks.append({"path": relative, "closes": closes, "state_before": document.get("state_before"),
                       "digest_matches_live": live == digest if digest else None,
                       "closed_record_unchanged_at_head": unchanged,
                       "passed": bool(document.get("date")) and digest == live and unchanged is not False})
    return checks


def log_round31_entries(text):
    entries = []
    for chunk in re.split(r"(?m)^##\s+", text)[1:]:
        heading = chunk.splitlines()[0]
        if re.search(r"round\s*31\b", heading, re.I):
            entries.append({"heading": heading, "body": chunk})
    return entries


def measure_jiniryu(evidence, claims):
    failures = []
    analysis = evidence.text(ANALYSIS)
    draft = evidence.text(DRAFT)
    if not analysis:
        failures.append(f"{ANALYSIS} missing (D-jinii seat dependency)")
    if not draft:
        failures.append(f"{DRAFT} missing (D-jinii seat dependency)")
    classes = {
        "availability": bool(re.search(r"(?i)availability", analysis)),
        "route": bool(re.search(r"(?i)\broute|devin\b", analysis)),
        "receipt-clobber": bool(re.search(r"(?i)receipt[ -]?clobber", analysis)),
        "pin-cascade": bool(re.search(r"(?i)re-?pin", analysis)),
        "tmpdir-mirror": bool(re.search(r"(?i)TMPDIR|mirror", analysis)),
    }
    if sum(classes.values()) < 3:
        failures.append("analysis does not ground the move in at least three telemetry classes")
    if not re.search(r"(?i)census|command", analysis) or not DATE_RE.search(analysis):
        failures.append("analysis lacks a dated census command")
    if not re.search(r"(?i)selected", analysis) or not re.search(r"(?m)^\*\*M1\b", analysis):
        failures.append("analysis does not record a scored selection with M1 chosen")
    draft_features = {
        "status_draft": bool(re.search(r"(?i)status\D{0,20}DRAFT", draft)),
        "orchestrator_lands": bool(re.search(r"(?i)orchestrator", draft)),
        "agents_target": bool(re.search(r"AGENTS\.md", draft)),
        "skill_target": bool(re.search(r"SKILL\.md", draft)),
        "province_unchanged": bool(re.search(r"(?i)PROVINCE\.md[^\n]{0,80}unchanged|unchanged[^\n]{0,80}PROVINCE", draft)),
        "proposed_bytes": len(re.findall(r"```markdown", draft)) >= 2,
        "falsification_section": bool(re.search(r"(?im)^##.*falsification", draft)),
        "falsifiers": len(re.findall(r"(?i)falsif", draft)) >= 4,
        "non_falsifiers": bool(re.search(r"(?i)non-?falsifier", draft)),
        "controls": len(re.findall(r"(?m)^\d+\.\s", draft)) >= 3,
        "audit_command": bool(re.search(r"python3 -c .*glob\.glob", draft, re.S)),
        "log_template": bool(re.search(r"(?i)LOG\.md entry text", draft)),
    }
    for name, present in draft_features.items():
        if not present:
            failures.append(f"jin'i-ryu draft missing feature: {name}")
    open_rows = open_availability_rows(evidence)
    open_rounds = {row["round"] for row in open_rows if row["receipt_landed"]}
    agents_text = evidence.text(AGENTS)
    skill_text = evidence.text(SKILL)
    landed = RULE_MARKER in agents_text and CHECKLIST_MARKER in skill_text
    if not landed:
        if open_rounds != OPEN_AT_DRAFT:
            failures.append("pre-landing census drifted: open+receipted availability records are "
                            f"{sorted(open_rounds)}, expected {sorted(OPEN_AT_DRAFT)}")
        if not all(row["completed_workers"] is None and row["has_finalization_note"]
                   for row in open_rows if row["receipt_landed"]):
            failures.append("a standing open record contradicts the drafted grounding (nulls + finalization note)")
    else:
        if open_rounds & POST_LANDING_OPEN:
            failures.append("FALSIFIER FIRED: a post-landing round's availability record still owes "
                            f"its closing snapshot: {sorted(open_rounds & POST_LANDING_OPEN)}")
        if open_rounds:
            failures.append("rule landed but pre-regimen open records were not closed by the "
                            f"retroactive closure act: {sorted(open_rounds)}")
    snapshots = closing_snapshots(evidence)
    for snapshot in snapshots:
        if not snapshot["passed"]:
            failures.append(f"closing snapshot integrity check failed: {snapshot['path']}")
    for target in (AGENTS, SKILL, PROVINCE):
        if not safe_path(target).is_file():
            failures.append(f"declared self-improvement target missing: {target}")
        if any(safe_path(target).is_relative_to(ROOT / protected) for protected in PROTECTED):
            failures.append(f"self-improvement target overlaps a protected filed surface: {target}")
    log_text = evidence.text(LOG)
    entries = log_round31_entries(log_text)
    qualified = [entry for entry in entries
                 if re.search(r"(?i)jin.?i.?ryu|jinii", entry["body"])
                 and re.search(r"(?i)falsif", entry["body"])
                 and re.search(r"AGENTS\.md|SKILL\.md", entry["body"])]
    if not qualified:
        failures.append("LOG.md has no round-31 jin'i-ryu entry naming the move and its "
                        "falsification condition (orchestrator landing)")
    return result(failures, {
        "telemetry_classes": classes,
        "draft_features": draft_features,
        "draft_sha256": evidence.inputs.get(DRAFT),
        "rule_landed": landed,
        "open_availability_records": metric(len(open_rows), "open-at-seat-close records on disk"),
        "open_with_landed_receipt": metric(sorted(open_rounds), "open records whose round receipt landed"),
        "closing_snapshots": snapshots,
        "log_round31_entries": [entry["heading"] for entry in entries],
        "qualified_log_entries": metric(len(qualified), "round-31 LOG entries naming delta + falsification"),
    })


def dependencies_ready():
    pending = []
    if not safe_path(LEDGER).is_file():
        pending.append(LEDGER)
    if not safe_path(DRAFT).is_file():
        pending.append(DRAFT)
    if not safe_path(SWEEP).is_file():
        pending.append(SWEEP)
    text = safe_path(LOG).read_text(encoding="utf-8") if safe_path(LOG).is_file() else ""
    if not log_round31_entries(text):
        pending.append(f"{LOG} round-31 entry (orchestrator)")
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
    for relative in (RUNNER, AGENTS, SKILL, PROVINCE, LOG, LEDGER, SWEEP, ANALYSIS, DRAFT,
                     SWEEP_AUDIT):
        evidence.text(relative)
    runtime_before = runtime_paths()
    baseline = claims.get("baseline_revision")
    before = protected_snapshot(baseline)
    matrix, external, _source, _fallback = load_matrix(evidence)
    def matrix_run(row):
        parts = list(row[1:])
        return run_command(row[0], parts)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        runs = list(pool.map(matrix_run, matrix))
    after = protected_snapshot(baseline)
    preservation = result(before["failures"] + after["failures"], {"before": before, "after": after})
    results = {}
    for claim_id, operation in (
            ("C", lambda: measure_closure(evidence, claims)),
            ("O", lambda: measure_sweep(evidence, claims, runs)),
            ("D", lambda: measure_jiniryu(evidence, claims))):
        try:
            results[claim_id] = operation()
        except (OSError, ValueError, TypeError, KeyError, RuntimeError, AttributeError,
                subprocess.SubprocessError) as error:
            results[claim_id] = result([f"could-not-evaluate: {type(error).__name__}: {error}"], {})
    coherence = []
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"C": "calibration", "O": "operability", "D": "depth"}:
        coherence.append("declared claims must be C/calibration, O/operability, D/depth")
    if claims.get("round") != 31 or targets.get("round") != 31 \
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
    return {"round": 31, "runner": RUNNER, "runner_sha256": evidence.inputs.get(RUNNER),
            "counting_command": COMMAND, "date": today(), "measured_at_utc": now(),
            "baseline_revision": baseline, "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results, "failures": failures,
            "missing_dependencies": sorted(evidence.missing | set(dependencies_ready())),
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": ["Read-only evidence checks plus re-execution of the declared green sweep; "
                       "not a canon or promotion decision.",
                       "The closure ledger is re-verified from raw sources (fleet reports under the "
                       "fleet root, fleet MANIFEST.json, lane git); the ledger's own byte claims are "
                       "not trusted without an independent recount.",
                       "The canonical sweep matrix is loaded from the audited round-31 sweep-audit "
                       "module; a load failure falls back to the runner's copy and is reported.",
                       "Recorded sweep commands are re-executed only under a strict whitelist; "
                       "python3 -c snippets are parsed but not re-executed and are reported as such. "
                       "Exit codes arbitrate the green sweep; byte-level stdout stability is "
                       "corroborated by the two-pass sweep audit except the known "
                       "nondeterministic-output commands (battery, pin-repoint-selftest).",
                       "Every matrix and rerun command is recorded with date, tmpdir, exit and output "
                       "digests; replay legs use the authorized /var/tmp mirror-safety storage.",
                       "The jin'i-ryu check enforces the drafted falsification condition live "
                       "(post-landing open records, closing-snapshot digest integrity), not prose only.",
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
    check("verdict-count-map-complete", set(VERDICT_COUNTS.values())
          == {"closed_admitted", "closed_rejected", "closed_with_finding", "operator_skipped"})
    rows = {8: {"verdict": "closed-admitted"}, 11: {"verdict": "closed-rejected"},
            13: {"verdict": "skipped-operator"}, 23: {"verdict": "closed-with-finding"}}
    check("verdict-recount", recompute_counts(rows) == Counter(
        {"closed_admitted": 1, "closed_rejected": 1, "operator_skipped": 1, "closed_with_finding": 1}))
    manifest = {"rounds": [
        {"round": 30, "type": "closure", "lanes": {"kotodama": "ok"},
         "lane_rounds": {"kotodama": 30}, "verdicts": {"depth": "improved"}, "notes": "work commit "
         + "a" * 40},
        {"round": 31, "type": "mint", "notes": "kotodama mention"},
        {"round": 40, "type": "closure", "lanes": {"kaidoku": "ok"},
         "lane_rounds": {"kaidoku": 40}, "verdicts": {"depth": "improved"}},
    ]}
    index = koto_entries_by_round(manifest)
    check("koto-index-excludes-other-lanes", set(index) == {30, 31})
    check("closure-entry-filter", [entry["round"] for entry in closure_entries(index, 30)] == [30]
          and closure_entries(index, 40) == [])
    check("lane-round-filter-accepts-retro-types",
          len(lane_round_entries(index, 31)) == 1)
    check("commit-token-classifier", commit_status("zzzz")["exists"] is False
          and commit_status("a" * 41)["exists"] is False)
    check("in-flight-row-detected", log_round31_entries("# x\n## 2026-10-18 — Round 31 admitted\n- falsif jin'i-ryu\n")
          and not log_round31_entries("## 2026-10-18 — Round 30 admitted\n"))
    check("final-sweep-parses-records", parse_final_sweep(
        "```\n$ python3 -B tools/check-gate-battery.py --selftest\nexit 0\n2026-10-18 sha256 256"
        " chars omitted\n```\n")[0]["exit0"] is True)
    table_row = ("| d2-assembly-check | assemblers | `python3 -B tools/assemble-d2.py --check` "
                 "| 0 | `2fa0c8c197459f54…` |\n")
    parsed = parse_sweep_table(table_row)
    check("sweep-table-row-parsed", parsed == [{"id": "d2-assembly-check", "family": "assemblers",
          "command": "python3 -B tools/assemble-d2.py --check", "exit": 0,
          "sha16": "2fa0c8c197459f54", "dated": False}])
    check("sweep-table-row-without-digest-skipped",
          parse_sweep_table("| x | y | `python3 tools/a.py` | 0 |  | \n") == [])
    check("rerun-tmpdir-mirror-legs", rerun_tmpdir("python3 -B tools/replay-frozen.py m.tsv")
          == "/var/tmp" and rerun_tmpdir("python3 -B tools/assemble-d2.py --check") is None)
    check("whitelist-accepts-tool-command", whitelist_rerun(
        {"command": "python3 -B tools/check-gate-battery.py --selftest"}) == "allowed")
    check("whitelist-accepts-round31-command", whitelist_rerun(
        {"command": "python3 reports/round-31/sweep-audit.py"}) == "allowed")
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
    empty = [{"line": 1, "command": "python3 tools/x.py", "exit0": False, "dated": False,
              "sha_recorded": False}]
    check("undated-record-detected", not empty[0]["dated"])
    check("rule-marker-absent-pre-landing", RULE_MARKER not in "placeholder AGENTS text")
    check("open-round-classifier", POST_LANDING_OPEN == {31, 32} and OPEN_AT_DRAFT == {19, 25, 26, 27, 28})
    check("matrix-fallback-nonempty", len(FALLBACK_MATRIX) >= 20)
    check("protected-includes-round30", "reports/round-30" in PROTECTED
          and "tools/gates/frozen/round-26" in PROTECTED)
    check("current-round-not-protected", "reports/round-31" not in PROTECTED)
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
