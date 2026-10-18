#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
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

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-22"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
RETRO = f"{ROUND_DIR}/loop2-retrospective.md"
RESOLUTIONS = f"{ROUND_DIR}/routed-resolution.json"
PROJECTOR = "tools/d2-typed-labels.py"
D4_PROJECTION = "examples/culture-d4/typed-labels.d4.yml"
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 22)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 22))
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
POINTER_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|examples|corpus)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)\b")
COMMAND_RE = re.compile(r"\b(?:python3?|sha256sum|git|date|test|diff|cmp|rg|grep)\s+\S+")
ROUTE_PATTERNS = {
    "declared_in": r"declared[_ -]in|edge[- ](?:payload|field).*loss",
    "candidate_selection": r"mtime|tie[- _]break|non[- ]hermetic|candidate[- _]selection",
    "malformed_alias": r"malformed[- _]?(?:tag|alias)|alias.*coer|coer.*alias|alias.*fail[- ]open",
    "r17_snapshot": r"r17|round[- ]?17|clone[- _]snapshot",
    "r18_supersession": r"r18|round[- ]?18|replay.*supersess|supersess.*replay",
    "baseline_binding": r"baseline[- _]binding|baseline.*drift|binding.*drift",
}
REGRESSIONS = (
    ("battery-selftest", ("tools/check-gate-battery.py", "--selftest")),
    ("battery", ("tools/check-gate-battery.py",)),
    ("craft-selftest", ("tools/check-craft-exercise.py", "--selftest")),
    ("craft", ("tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json")),
    ("d2-assembly-selftest", ("tools/assemble-d2.py", "--selftest")),
    ("d2-assembly", ("tools/assemble-d2.py", "--check")),
    ("d2-adapter-selftest", ("tools/assemble-d2-typed.py", "--selftest")),
    ("d2-adapter", ("tools/assemble-d2-typed.py", "--check")),
    ("d3-assembly-selftest", ("tools/assemble-culture-d3.py", "--selftest")),
    ("d3-assembly", ("tools/assemble-culture-d3.py", "--check")),
    ("d4-assembly-selftest", ("tools/assemble-culture-d4.py", "--selftest")),
    ("d4-assembly", ("tools/assemble-culture-d4.py", "--check")),
    ("d4-adapter-selftest", ("tools/assemble-d4-typed.py", "--selftest")),
    ("d4-adapter", ("tools/assemble-d4-typed.py", "--check")),
    ("projector-selftest", (PROJECTOR, "--selftest")),
    ("d2-projection", (PROJECTOR, "--check")),
    ("d4-projection", (PROJECTOR, "--packet", "examples/culture-d4/packet.d4.yml", "--check", D4_PROJECTION)),
    ("typed-pipeline-selftest", ("tools/gates/typed-pipeline-gate.py", "--selftest")),
    ("typed-pipeline-generalized-selftest", ("tools/gates/typed-pipeline-gate.py", "--selftest-generalized")),
    ("d2-gate", ("tools/gates/typed-pipeline-gate.py",)),
    ("d4-gate", ("tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.yml")),
    ("d4-label-gate", ("tools/gates/d4-typed-labels-check-gate.py",)),
    ("d4-assembly-gate", ("tools/gates/d4-assembly-check-gate.py",)),
    ("coupling-selftest", ("tools/check-evidence-coupling.py", "--selftest")),
    ("replay-selftest", ("tools/replay-frozen.py", "--selftest")),
    ("handoff-v2", ("tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet")),
    ("handoff-v3-selftest", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest")),
    ("handoff-v3", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet")),
)


def today():
    return dt.date.today().isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def metric(value, operation):
    return {"value": value, "command": f"{COMMAND} ({operation})", "date": today()}


def safe_path(relative):
    if not isinstance(relative, str) or not relative:
        raise ValueError("evidence path must be a nonempty string")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise ValueError(f"not an in-repository path: {relative}")
    resolved = ROOT / path
    for ancestor in (resolved, *resolved.parents):
        if ancestor == ROOT:
            break
        if ancestor.is_symlink():
            raise ValueError(f"symlink evidence path refused: {relative}")
    if not resolved.resolve().is_relative_to(ROOT):
        raise ValueError(f"evidence path escapes repository: {relative}")
    return resolved


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

    def text(self, relative):
        try:
            data = safe_path(relative).read_bytes()
            self.inputs[relative] = sha(data)
            return data.decode("utf-8")
        except (OSError, UnicodeError, ValueError) as error:
            self.missing.add(relative)
            self.errors.append(f"{relative}: {error}")
            return ""

    def document(self, relative):
        text = self.text(relative)
        try:
            return strict_json(text) if text else None
        except (ValueError, TypeError) as error:
            self.errors.append(f"{relative}: {error}")
            return None


def result(failures, measurement, missing=()):
    return {"passed": not failures, "failures": failures,
            "measurement": measurement, "missing_dependencies": sorted(set(missing))}


def git(*argv, timeout=60):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1")
    try:
        proc = subprocess.run(["git", *argv], cwd=ROOT, capture_output=True,
                              timeout=timeout, env=env)
        return proc.stdout if proc.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def protected_inventory():
    raw = git("ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", *PROTECTED)
    if raw is None:
        raise ValueError("cannot inventory protected paths with git ls-files")
    inventory = {}
    for relative in sorted(set(os.fsdecode(item) for item in raw.split(b"\0") if item)):
        path = safe_path(relative)
        if path.is_file():
            inventory[relative] = sha(path.read_bytes())
        else:
            inventory[relative] = None
    return inventory


def protected_baseline(revision):
    failures, rows = [], []
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return result(["Round-22 declared baseline is not a full Git revision"], {})
    raw = git("ls-tree", "-r", "-z", revision, "--", *PROTECTED)
    if raw is None:
        return result([f"Cannot inspect protected baseline {revision}"], {})
    expected = {}
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split()
        if kind != "blob" or mode not in ("100644", "100755"):
            failures.append(f"Protected baseline has a nonregular entry: {os.fsdecode(name)}")
        expected[os.fsdecode(name)] = oid
    try:
        observed = protected_inventory()
    except (OSError, ValueError) as error:
        return result([str(error)], {})
    for relative in sorted(set(expected) | set(observed)):
        before = expected.get(relative)
        after = None
        if observed.get(relative) is not None:
            data = safe_path(relative).read_bytes()
            algorithm = hashlib.sha256 if before and len(before) == 64 else hashlib.sha1
            after = algorithm(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        if before != after:
            rows.append({"path": relative, "baseline_blob": before, "observed_blob": after})
    if rows:
        failures.append("Filed rounds 8-21 or their frozen generations differ from the declared baseline")
    return result(failures, {"baseline_revision": revision,
                            "protected_paths": metric(len(expected), "git ls-tree of protected baseline"),
                            "differences": rows,
                            "differences_total": metric(len(rows), "compare protected Git blobs to working bytes")})


def run_command(label, parts, timeout=900, tmpdir=None):
    scratch = Path(tmpdir) if tmpdir is not None else ROOT / ".scratch" / "round-22" / "validation" / label
    scratch.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(scratch), "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    item = {"label": label, "command": shlex.join(["python3", *parts]),
            "argv": ["python3", *parts], "date": today()}
    try:
        source = safe_path(parts[0])
        item["tool_sha256"] = sha(source.read_bytes())
        proc = subprocess.run([sys.executable, *parts], cwd=ROOT, capture_output=True,
                              timeout=timeout, env=env)
        item.update(exit=proc.returncode, stdout=proc.stdout.decode("utf-8", "replace"),
                    stderr=proc.stderr.decode("utf-8", "replace"),
                    stdout_sha256=sha(proc.stdout), stderr_sha256=sha(proc.stderr))
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error), timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def run_receipt(item):
    return {key: (value[-7000:] if key == "stdout" else value[-2000:]
                  if key == "stderr" else value) for key, value in item.items()}


def measure_regressions():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        items = list(pool.map(lambda pair: run_command(*pair), REGRESSIONS))
    failures = [f"Regression failed: {item['command']} (exit {item.get('exit')}, {item['date']})"
                for item in items if item.get("exit") != 0]
    return result(failures, {"runs_total": metric(len(items), "fixed regression command inventory"),
                             "runs": [run_receipt(item) for item in items]}), {
                                 item["label"]: item for item in items}


def rows_from(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("items", "resolutions", "routed_items", "routed", "routes", "entries", "rows"):
            if isinstance(payload.get(key), list):
                return payload[key]
            if isinstance(payload.get(key), dict):
                return [{"id": name, **value} if isinstance(value, dict) else value
                        for name, value in payload[key].items()]
    return []


def route_identity(row):
    preferred = " ".join(str(row.get(key, "")) for key in (
        "id", "route_id", "item", "title", "topic", "issue", "description", "finding", "problem"))
    for text in (preferred, json.dumps(row, ensure_ascii=False)):
        matches = [name for name, pattern in ROUTE_PATTERNS.items() if re.search(pattern, text, re.I)]
        if len(matches) == 1:
            return matches[0]
        for name in ("declared_in", "candidate_selection", "malformed_alias", "baseline_binding"):
            if name in matches:
                return name
    return None


def row_disposition(row):
    value = row.get("disposition", row.get("status", ""))
    if isinstance(value, dict):
        value = value.get("class", value.get("type", value.get("status", "")))
    return re.sub(r"[ _]+", "-", str(value).strip().lower())


def cited_evidence(row, evidence):
    serialized = json.dumps(row, ensure_ascii=False)
    references = sorted(set(POINTER_RE.findall(serialized)) - {RESOLUTIONS, OUTPUT, f"{ROUND_DIR}/claims.json"})
    texts, missing = [], []
    for relative in references:
        text = evidence.text(relative)
        if text:
            texts.append(text)
        else:
            missing.append(relative)
    return serialized + "\n" + "\n".join(texts), references, missing


def evaluate_resolutions(payload, evidence):
    failures, missing, evaluated = [], [], []
    rows = rows_from(payload)
    if len(rows) != 6:
        failures.append(f"Routed-resolution ledger must contain exactly six items, observed {len(rows)}")
    identities = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            failures.append(f"Routed item {index} is not an object")
            continue
        identity = route_identity(row)
        identities.append(identity)
        disposition = row_disposition(row)
        combined, references, absent = cited_evidence(row, evidence)
        missing.extend(absent)
        row_failures = []
        if identity is None:
            row_failures.append("cannot identify the declared routed issue")
        if disposition not in ("fixed-with-control", "resolved-by-documentation"):
            row_failures.append(f"unlicensed disposition {disposition!r}")
        if identity in ("candidate_selection", "malformed_alias") and disposition != "fixed-with-control":
            row_failures.append("this executable defect requires a fix with a control")
        if not references or not any(path.startswith(f"{ROUND_DIR}/") for path in references):
            row_failures.append("no resolvable new round-22 evidence pointer")
        if absent:
            row_failures.append("referenced evidence is absent: " + ", ".join(absent))
        if not DATE_RE.search(combined) or not COMMAND_RE.search(combined):
            row_failures.append("evidence does not carry both a command and an ISO date")
        if disposition == "fixed-with-control":
            for name, pattern in (
                    ("before", r"\bbefore\b|pre[- _]?fix|negative[- ](?:controls?|checks?|probes?)|regression[- ]control|\bbaseline\b"),
                    ("after", r"\bafter\b|post[- _]?fix|positive[- ](?:controls?|checks?|probes?)|valid[- ]control|source repair"),
                    ("control", r"\bcontrols?\b|selftest|self-test|regression")):
                if not re.search(pattern, combined, re.I):
                    row_failures.append(f"fix lacks a named {name} witness")
        if disposition == "resolved-by-documentation" and not re.search(
                r"\breason\b|\bcause\b|supersed|attribut|limitation|disposition|snapshot|baseline", combined, re.I):
            row_failures.append("documentation does not explain its bounded disposition")
        failures.extend(f"Routed item {identity or index}: {item}" for item in row_failures)
        evaluated.append({"id": row.get("id", row.get("route_id", index)),
                          "issue": identity, "disposition": disposition,
                          "evidence": references, "passed": not row_failures})
    census = collections.Counter(identities)
    for name in ROUTE_PATTERNS:
        if census[name] != 1:
            failures.append(f"Routed-resolution coverage for {name} is {census[name]}, expected one")
    return result(failures, {"ledger": RESOLUTIONS,
                            "resolved_items": metric(sum(row["passed"] for row in evaluated),
                                                     "six unique routed dispositions with controls/evidence"),
                            "required_items": metric(6, "round-22 claim O six-item inventory"),
                            "rows": evaluated}, missing)


def measure_alias_controls():
    failures, runs = [], []
    work = ROOT / ".scratch" / "round-22" / "validation" / "alias-controls" / "culture-d4"
    work.mkdir(parents=True, exist_ok=True)
    original = safe_path("examples/culture-d4/packet.d4.yml").read_text(encoding="utf-8")
    if re.search(r"(?m)^era_aliases:", original):
        return result(["Alias CLI control cannot append a unique era_aliases key"], {})
    cases = (("valid", '"E0"', False), ("list", "[1, 2]", True),
             ("boolean", "true", True), ("null", "null", True),
             ("malformed-string", '"not-an-era-tag"', True))
    for label, value, malformed in cases:
        packet = work / f"{label}.yml"
        output = work / f"{label}.projection.json"
        packet.write_text(original + f'\nera_aliases:\n  era-9: {value}\n', encoding="utf-8")
        output.unlink(missing_ok=True)
        relative = packet.relative_to(ROOT).as_posix()
        item = run_command(f"alias-{label}", (PROJECTOR, "--packet", relative,
                                              "--emit", output.relative_to(ROOT).as_posix()), 120)
        emitted = strict_json(output.read_text(encoding="utf-8")) if output.is_file() else None
        if malformed:
            passed = item.get("exit") == 2 and emitted is None and "Traceback" not in item.get("stderr", "")
        else:
            block = emitted.get("era_reconciliation", {}) if isinstance(emitted, dict) else {}
            rows = block.get("alias_rows", []) if isinstance(block, dict) else []
            passed = item.get("exit") in (0, 1) and any(
                row.get("source") == "era-9" and row.get("tag") == "E0"
                and row.get("status") == "confirmed" for row in rows if isinstance(row, dict))
        if not passed:
            failures.append(f"Alias full-CLI {'negative' if malformed else 'positive'} control failed: {label}")
        runs.append({**run_receipt(item), "control_passed": passed, "malformed": malformed,
                     "emitted_projection_sha256": sha(output.read_bytes()) if output.is_file() else None})
    return result(failures, {"controls": runs,
                            "controls_total": metric(len(runs), "one valid and four malformed full-CLI alias fixtures")})


def new_manifests():
    base = ROOT / "tools/gates/frozen/round-22"
    if not base.is_dir():
        return []
    return [path.relative_to(ROOT).as_posix() for path in sorted(base.rglob("MANIFEST.tsv"))
            if path.is_file()]


def measure_successor_replays():
    manifests = new_manifests()
    failures, runs = [], []
    if not manifests:
        failures.append("No new round-22 frozen successor manifest exists")
    def replay(index, relative):
        if relative == "tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv":
            return run_command(f"successor-{index}",
                               (f"{ROUND_DIR}/bleed/replay.py", "--require-live"), tmpdir=ROOT / ".scratch")
        return run_command(f"successor-{index}", ("tools/replay-frozen.py", relative, "--json"),
                           tmpdir=ROOT.parent / ".scratch" / "round-22-replay-mirrors")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(replay, index, relative) for index, relative in enumerate(manifests)]
        for relative, future in zip(manifests, futures):
            item = future.result()
            payload = None
            try:
                payload = strict_json(item.get("stdout", ""))
            except (TypeError, ValueError):
                pass
            replay_payload = payload.get("replay", payload) if isinstance(payload, dict) else {}
            summary = replay_payload.get("summary", {}) if isinstance(replay_payload, dict) else {}
            total = summary.get("rows")
            passed = (item.get("exit") == 0 and type(total) is int and total > 0
                      and summary.get("reproduced") == total and summary.get("mismatch") == 0
                      and summary.get("could_not_evaluate") == 0 and summary.get("exit") == 0)
            if not passed:
                failures.append(f"Round-22 frozen successor replay failed: {relative}")
            runs.append({**run_receipt(item), "manifest": relative, "passed": passed,
                         "observed": payload})
    return result(failures, {"manifests_total": metric(len(manifests), "new round-22 frozen generations only"),
                            "replays": runs})


def measure_selection_control():
    item = run_command("content-selection", (f"{ROUND_DIR}/fixes/tie-break.py", "--root", ".", "--selftest"))
    try:
        payload = strict_json(item.get("stdout", ""))
    except (TypeError, ValueError):
        payload = {}
    controls = payload.get("selftest", {}) if isinstance(payload, dict) else {}
    total = controls.get("total_controls")
    passed = (item.get("exit") == 0 and payload.get("passed") is True
              and controls.get("passed") is True and type(total) is int and total > 0
              and controls.get("passed_controls") == total
              and payload.get("filed_rounds_8_21_changes") == [])
    return result([] if passed else ["Content-based successor selection/inverted-mtime controls failed"],
                  {"run": run_receipt(item), "observed": payload})


def measure_operability(evidence, regressions):
    payload = evidence.document(RESOLUTIONS)
    resolutions = evaluate_resolutions(payload, evidence)
    if payload is None:
        resolutions["missing_dependencies"].append(RESOLUTIONS)
        resolutions["failures"].append(f"Missing or malformed {RESOLUTIONS}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        pending = [pool.submit(operation) for operation in (
            measure_alias_controls, measure_successor_replays, measure_selection_control)]
        aliases, successors, selection = [future.result() for future in pending]
    failures = resolutions["failures"] + aliases["failures"] + successors["failures"] + selection["failures"] + regressions["failures"]
    return result(failures, {"routed_resolution": resolutions["measurement"],
                            "alias_cli_controls": aliases, "successor_replays": successors,
                            "content_selection": selection,
                            "regressions": regressions}, resolutions["missing_dependencies"])


def dated_command(text):
    return bool(DATE_RE.search(text) and COMMAND_RE.search(text))


def markdown_paths():
    directory = ROOT / ROUND_DIR
    return [path.relative_to(ROOT).as_posix() for path in sorted(directory.rglob("*.md"))
            if path.is_file()]


def evaluate_retrospective(text, scorecard, receipts):
    failures = []
    if not text:
        failures.append(f"Missing loop-2 retrospective: {RETRO}")
    if not dated_command(text):
        failures.append("Loop-2 retrospective lacks dated counting commands")
    historical = {}
    for number in range(17, 22):
        receipt = receipts.get(number)
        acceptance = receipt.get("acceptance_checks_passed") if isinstance(receipt, dict) else None
        expected = number != 17
        historical[str(number)] = acceptance
        if acceptance is not expected:
            failures.append(f"Filed round-{number} acceptance is not the declared historical {expected}")
        if f"reports/round-{number}/validation.json" not in text:
            failures.append(f"Retrospective lacks the final receipt pointer for round {number}")
        lines = [line for line in text.splitlines()
                 if re.search(rf"\b(?:r|round[- ]*)?{number}\b", line, re.I)]
        pattern = r"reject|not admitted|D\s+(?:FAIL|false)" if number == 17 else r"admit|acceptance[^|]*(?:true|pass)"
        if not any(re.search(pattern, line, re.I) for line in lines):
            failures.append(f"Retrospective does not state the final {'rejection' if number == 17 else 'admission'} of round {number}")
    requirements = {
        "honest r17/r18 repair arc": r"r17|round[- ]?17",
        "repair assessment": r"\brepair|\brepaired|generaliz",
        "non-retroactive limit": r"not retroactiv|does not retroactiv|never retroactiv|no retroactiv|not.*(?:fully|all).*verif|not equivalent|not.*blanket|bounded.*repair",
        "conformance defect classes": r"conformance",
        "defect dispositions": r"disposition",
        "provider substitution": r"provider.*substitut|substitut.*provider|\bhyper\b",
        "operator amendments": r"operator.*amend|amend.*operator",
        "freshness question": r"freshness",
        "freshness threshold": r"threshold|stability budget|denominator",
        "operator authority remains pending": r"pending|operator.*decid|operator.*ruling|no.*threshold.*select",
        "loop-2 freshness data": r"7\s*(?:fixed|fixes)|5\s*(?:attempt|unresolved)|12\s*(?:stale|entr)|stale[- ]documented",
    }
    for name, pattern in requirements.items():
        if not re.search(pattern, text, re.I | re.S):
            failures.append(f"Retrospective omits {name}")
    rows = [line for line in scorecard.splitlines()
            if line.lstrip().startswith("|") and re.search(r"loop\s*2|rounds?\s*17\s*[-–]\s*21", line, re.I)]
    summary = next((line for line in rows if RETRO in line and re.search(r"4\s*(?:admi|accept)", line, re.I)
                    and re.search(r"1\s*(?:reject|rejection)", line, re.I)), None)
    if summary is None:
        failures.append("SCORECARD.md lacks an evidence-linked loop-2 summary row with four admissions and one rejection")
    return result(failures, {"filed_acceptance": historical, "scorecard_summary_row": summary,
                            "rounds_total": metric(len(historical), "filed round-17 through round-21 receipt census"),
                            "admissions": metric(sum(value is True for value in historical.values()), "filed acceptance true flags"),
                            "rejections": metric(sum(value is False for value in historical.values()), "filed acceptance false flags")})


def audit_verdict(text):
    for line in reversed(text.splitlines()):
        cleaned = line.strip().lstrip("#>*- ").replace("**", "").replace("`", "")
        if re.match(r"(?i)^PASS for retrospective SHA-256 [0-9a-f]{64}\b", cleaned):
            return True, line
        if re.match(r"(?i)(?:(?:final|audit|overall|pointer|numeric|text|consolidated|C07|C08)\s+){0,4}(?:verdict|conclusion|result|status)\s*[:—–-]", cleaned):
            if re.search(r"\bFAIL(?:ED)?\b|\bBLOCK(?:ED|ER)\b|\bPENDING\b|not (?:yet )?pass", cleaned, re.I):
                return False, line
            if re.search(r"\bPASS(?:ED)?\b", cleaned, re.I):
                return True, line
    return False, None


def recheck_retrospective_pointers(text, evidence):
    failures, seen, ranges = [], set(), 0
    pattern = re.compile(
        r"(?<![\w/])((?:reports|tools|corpus|examples)/[A-Za-z0-9_./{}*,\[\]-]+|"
        r"(?:LOG|SCORECARD|SKILL|SHONEN|PROVINCE)\.md)(?::([0-9][0-9, -]*))?")
    for match in pattern.finditer(text):
        relative, locator = match.groups()
        relative = relative.rstrip(".,")
        if any(char in relative for char in "{}*[") or "round-N/" in relative:
            continue
        key = relative, locator
        if key in seen:
            continue
        seen.add(key)
        try:
            path = safe_path(relative)
            if not path.exists():
                failures.append(f"Missing retrospective pointer: {relative}")
            elif path.is_file():
                source = evidence.text(relative)
                if locator:
                    ranges += 1
                    if not all(1 <= int(number) <= len(source.splitlines()) for number in re.findall(r"\d+", locator)):
                        failures.append(f"Out-of-range retrospective pointer: {relative}:{locator}")
        except (OSError, ValueError) as error:
            failures.append(f"Unsafe retrospective pointer: {relative}: {error}")
    revisions = sorted(set(re.findall(r"`([0-9a-f]{7,40})`", text)))
    for revision in revisions:
        if git("cat-file", "-e", revision + "^{commit}") is None:
            failures.append(f"Unresolvable retrospective revision: {revision}")
    for number in range(17, 22):
        for filename in ("claims.json", "validation.json", "run-validation.py"):
            if not safe_path(f"reports/round-{number}/{filename}").is_file():
                failures.append(f"Missing expanded per-round retrospective pointer: round-{number}/{filename}")
    return result(failures, {"citations": metric(len(seen), "independent literal retrospective path/range replay"),
                            "ranges": metric(ranges, "independent retrospective line-range replay"),
                            "revisions": metric(len(revisions), "git cat-file retrospective revision replay")})


def measure_calibration(evidence):
    text = evidence.text(RETRO)
    retrospective_sha = sha(text.encode("utf-8")) if text else None
    receipts = {number: evidence.document(f"reports/round-{number}/validation.json") for number in range(17, 22)}
    evaluated = evaluate_retrospective(text, evidence.text("SCORECARD.md"), receipts)
    pointer_recheck = recheck_retrospective_pointers(text, evidence)
    failures, audits = list(evaluated["failures"]) + pointer_recheck["failures"], []
    for relative in markdown_paths():
        if not re.search(r"audit|consisten|review", Path(relative).name, re.I):
            continue
        candidate = evidence.text(relative)
        digest_bound = retrospective_sha is not None and retrospective_sha in candidate
        if (RETRO not in candidate and not digest_bound) or not re.search(r"loop[- ]?2|retrospective", candidate, re.I):
            continue
        passed, verdict = audit_verdict(candidate)
        parent_pointer_condition = ("complete evidence audit with one explicitly blocked parent integration condition" in candidate
                                    and RESOLUTIONS in candidate)
        pointer_condition_cleared = parent_pointer_condition and pointer_recheck["passed"]
        pointers = sorted(set(POINTER_RE.findall(candidate)))
        historic = {path for path in pointers if re.match(r"reports/round-(?:17|18|19|20|21)/", path)}
        valid = (passed or pointer_condition_cleared) and digest_bound and dated_command(candidate) and len(historic) >= 2
        if not valid:
            failures.append(f"Retrospective auditor lacks a dated, current-digest-bound PASS or independently cleared parent-pointer condition: {relative}")
        audits.append({"path": relative, "passed": valid, "recorded_verdict": verdict,
                       "parent_pointer_condition_independently_cleared": pointer_condition_cleared,
                       "current_retrospective_digest_bound": digest_bound,
                       "historical_evidence": sorted(historic)})
    if len(audits) < 2:
        failures.append(f"Need at least two independent retrospective auditors; observed {len(audits)}")
    return result(failures, {**evaluated["measurement"], "retrospective": RETRO,
                            "retrospective_sha256": retrospective_sha, "pointer_recheck": pointer_recheck,
                            "auditors": audits, "auditors_total": metric(len(audits), "independent retrospective audit artifacts")},
                  [RETRO] if not text else [])


def foreign_reference(value):
    return isinstance(value, str) and bool(re.search(
        r"examples/culture-d2/|\bD2 (?:design drill|typed labels)|^d2-roman$|"
        r"(?:^|[/\s])(?:05-lexicon|11-costumes|12-rank-rules|13-naming)(?:\.yml)?(?:$|[#:\s])",
        value, re.I))


def projection_boundary(projection):
    failures, foreign = [], []
    if not isinstance(projection, dict):
        return result(["D4 typed projection is not a JSON object"], {})
    typed = projection.get("typed_labels")
    labels = typed.get("labels") if isinstance(typed, dict) else None
    if not isinstance(labels, list) or not labels:
        failures.append("D4 projection has no owned typed labels")
    def walk(value, pointer):
        if isinstance(value, dict):
            for key, child in value.items():
                walk(child, f"{pointer}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{pointer}[{index}]")
        elif foreign_reference(value):
            negative_method_note = pointer.startswith("root.era_reconciliation.basis[") and re.search(
                r"not read|never (?:read|import)|not imported", value, re.I)
            if not negative_method_note:
                foreign.append({"field": pointer, "value": value})
    walk(projection, "root")
    if foreign:
        failures.append("D4 projection still carries foreign D2 ownership or record citations; the selected D4 no-import design also forbids borrowed-fixture relabeling")
    return result(failures, {"foreign_owned_fields": foreign,
                            "labels": metric(len(labels) if isinstance(labels, list) else 0, "D4-owned typed label census"),
                            "foreign_owned_fields_total": metric(len(foreign), "source/citation scan allowing only explicit negative method notes")})


def require_summary(run, pattern, expected, name):
    match = re.search(pattern, run.get("stdout", ""))
    observed = tuple(int(value) for value in match.groups()) if match else None
    passed = run.get("exit") == 0 and observed == expected
    return {"passed": passed, "observed": observed, "expected": expected,
            "command": run.get("command"), "date": run.get("date", today()),
            "name": name}


def measure_source_isolation():
    namespace = runpy.run_path(str(safe_path(PROJECTOR)))
    pipeline = namespace["run_pipeline"]
    globals_ = pipeline.__globals__
    serialize = namespace["serialize"]
    packet = safe_path("examples/culture-d4/packet.d4.yml")
    original = pipeline(packet)["projection"]
    original_bytes = serialize(original)
    old_rank = globals_["build_payload"]
    def poisoned_rank():
        raise RuntimeError("R22-D2-FIXTURE-POISON")
    globals_["build_payload"] = poisoned_rank
    try:
        independent = serialize(pipeline(packet)["projection"]) == original_bytes
        try:
            pipeline(safe_path("examples/culture-d2/packet.d2.yml"))
            poison_active = False
        except RuntimeError as error:
            poison_active = str(error) == "R22-D2-FIXTURE-POISON"
    finally:
        globals_["build_payload"] = old_rank
    old_load = globals_["load_packet_file"]
    def mutated_load(path):
        loaded = old_load(path)
        if Path(path).resolve() == packet.resolve() and loaded.get("packet") is not None:
            loaded = strict_json(json.dumps(loaded))
            loaded["packet"]["rank_rules"][0]["authority"] = "R22 local authority control"
        return loaded
    globals_["load_packet_file"] = mutated_load
    try:
        changed = pipeline(packet)["projection"]
    finally:
        globals_["load_packet_file"] = old_load
    original_rows = original["rank_rules"]["normalized_rules"]
    changed_rows = changed["rank_rules"]["normalized_rules"]
    changed_ids = [row["id"] for row, other in zip(changed_rows, original_rows) if row != other]
    local_sensitive = (len(changed_rows) == len(original_rows) == 4
                       and changed_ids == [original_rows[0]["id"]]
                       and changed_rows[0]["authority"] == "R22 local authority control"
                       and changed["typed_labels"] == original["typed_labels"])
    checks = {"D4_ignores_poisoned_D2_fixture": independent,
              "D2_fixture_poison_is_active": poison_active,
              "D4_local_rank_mutation_is_observed": local_sensitive,
              "production_projection_matches_source": original_bytes == safe_path(D4_PROJECTION).read_bytes()}
    return result([name for name, passed in checks.items() if not passed],
                  {"controls": {name: metric(passed, "in-memory projector poison/local-rank counterfactual")
                                for name, passed in checks.items()}})


def measure_depth(evidence, runs, baseline):
    failures = []
    projection = evidence.document(D4_PROJECTION)
    boundary = projection_boundary(projection)
    failures.extend(boundary["failures"])
    isolation = measure_source_isolation()
    failures.extend("Source isolation control failed: " + name for name in isolation["failures"])
    old_tool = git("show", f"{baseline}:{PROJECTOR}") if isinstance(baseline, str) else None
    current_tool = evidence.text(PROJECTOR)
    source_changed = old_tool is not None and sha(old_tool) != sha(current_tool.encode("utf-8"))
    if not source_changed:
        failures.append("D4 boundary repair is not bound to a changed projector source from the declared baseline")
    summaries = (
        require_summary(runs.get("d4-gate", {}), r"summary:\s*(\d+)/(\d+) legs passed", (19, 19), "D4 gate"),
        require_summary(runs.get("d4-adapter-selftest", {}), r"selftest:\s*(\d+)/(\d+) checks passed", (12, 12), "D4 adapter"),
        require_summary(runs.get("handoff-v3", {}), r"links=(\d+)/(\d+)", (105, 105), "handoff v3 links"),
        require_summary(runs.get("handoff-v3", {}), r"fields=(\d+)/(\d+)\s+glossary=(\d+)/(\d+)\s+findings=(\d+)", (16, 16, 20, 20, 0), "handoff v3 gate"),
    )
    for item in summaries:
        if not item["passed"]:
            failures.append(f"{item['name']} summary did not reproduce {item['expected']}: {item['observed']}")
    for label in ("projector-selftest", "d4-projection", "d4-adapter", "d4-label-gate", "d4-assembly-gate"):
        if runs.get(label, {}).get("exit") != 0:
            failures.append(f"D4 source/determinism control failed: {label}")
    drafts = []
    for relative in markdown_paths():
        if "skill" not in Path(relative).name.lower():
            continue
        text = evidence.text(relative)
        valid = bool(re.search(r"draft", text, re.I) and re.search(r"\bD4\b", text)
                     and re.search(r"famil|no[- ]import|foreign", text, re.I)
                     and (PROJECTOR in text or "SKILL.md" in text) and DATE_RE.search(text))
        drafts.append({"path": relative, "rule_present": valid})
    if not drafts or not any(row["rule_present"] for row in drafts):
        failures.append("Missing dated SKILL.md draft containing the D4 family-boundary rule")
    bleed_controls = []
    for relative in markdown_paths():
        if not re.search(r"bleed|boundary", relative, re.I):
            continue
        text = evidence.text(relative)
        if dated_command(text) and re.search(r"before|pre[- ]fix", text, re.I) and re.search(r"after|post[- ]fix", text, re.I):
            bleed_controls.append(relative)
    if not bleed_controls:
        failures.append("No dated source-level bleed fix report carries before/after controls")
    return result(failures, {"projection": D4_PROJECTION, "boundary": boundary,
                            "source_isolation": isolation,
                            "projector_source_changed": metric(source_changed, "compare declared baseline projector bytes with current source"),
                            "gate_summaries": list(summaries), "skill_drafts": drafts,
                            "bleed_control_evidence": bleed_controls},
                  [f"{ROUND_DIR}/<skill-draft>.md"] if not drafts else [])


def selftest():
    controls = []
    def check(name, condition):
        controls.append({"control": name, "passed": bool(condition)})
    class FixtureEvidence:
        def text(self, relative):
            return ("2026-10-18 python3 tools/d2-typed-labels.py --selftest "
                    "before negative-control after positive-control disposition reason")
    fixtures = [
        {"id": name, "title": title,
         "disposition": "fixed-with-control" if name in ("declared_in", "candidate_selection", "malformed_alias") else "resolved-by-documentation",
         "evidence": [f"{ROUND_DIR}/controls/{name}.md"]}
        for name, title in (
            ("declared_in", "v3 declared_in loss"),
            ("candidate_selection", "mtime tie-break"),
            ("malformed_alias", "malformed alias coercion"),
            ("r17_snapshot", "r17 clone snapshot"),
            ("r18_supersession", "r18 replay supersession"),
            ("baseline_binding", "baseline-binding drift"))]
    check("six distinct evidence-bound resolutions accepted", evaluate_resolutions(fixtures, FixtureEvidence())["passed"])
    check("five resolutions rejected", not evaluate_resolutions(fixtures[:-1], FixtureEvidence())["passed"])
    check("duplicate resolution rejected", not evaluate_resolutions(fixtures[:-1] + [fixtures[0]], FixtureEvidence())["passed"])
    changed = [dict(row) for row in fixtures]
    changed[1]["disposition"] = "resolved-by-documentation"
    check("mtime executable defect cannot be documentation-only", not evaluate_resolutions(changed, FixtureEvidence())["passed"])
    changed = [dict(row) for row in fixtures]
    changed[2]["disposition"] = "open"
    check("open malformed alias rejected", not evaluate_resolutions(changed, FixtureEvidence())["passed"])
    changed = [dict(row) for row in fixtures]
    changed[0]["evidence"] = []
    check("unwitnessed fixed claim rejected", not evaluate_resolutions(changed, FixtureEvidence())["passed"])
    class MissingEvidence:
        def text(self, relative):
            return ""
    check("missing control files rejected", not evaluate_resolutions(fixtures, MissingEvidence())["passed"])
    clean = {"name": "D4 typed labels", "typed_labels": {"labels": [{"source": {"component": "04-lexicon.yml"}, "scheme": "D4-roman-1"}]}}
    check("family-clean labels accepted", projection_boundary(clean)["passed"])
    check("empty D4 labels rejected", not projection_boundary({"typed_labels": {"labels": []}})["passed"])
    check("D2 rank citation rejected", not projection_boundary({**clean, "rank_rules": {"cite": "examples/culture-d2/components/12-rank-rules.yml#RR-01"}})["passed"])
    check("short D2 rank citation rejected", not projection_boundary({**clean, "rank_rules": {"cite": "12-rank-rules.yml#RR-01"}})["passed"])
    check("foreign label owner rejected", not projection_boundary({"typed_labels": {"labels": [{"owner": "05-lexicon"}]}})["passed"])
    check("borrowed-fixture renaming cannot evade chosen no-import rule", not projection_boundary({**clean, "borrowed_references": {"source": "examples/culture-d2/components/12-rank-rules.yml"}})["passed"])
    check("negative method note is not fixture import", projection_boundary({**clean, "era_reconciliation": {"basis": ["examples/culture-d2/components/11-costumes.yml is not read for D4"]}})["passed"])
    check("positive audit verdict accepted", audit_verdict("Verdict: PASS — controls reproduced")[0])
    check("pending audit verdict rejected", not audit_verdict("Verdict: PENDING; historical PASS only")[0])
    check("failing audit mentioning historical pass rejected", not audit_verdict("Verdict: FAIL (old receipt PASS)")[0])
    check("latest audit disposition supersedes initial pending", audit_verdict("Status: PENDING\nFinal pointer verdict: PASS")[0])
    receipts = {number: {"acceptance_checks_passed": number != 17} for number in range(17, 22)}
    retro = ("2026-10-18 python3 controls.py; bounded repair is not retroactive; "
             "conformance disposition; provider substitution; operator amendments; "
             "freshness threshold pending; 7 fixed\n") + "\n".join(
                 f"| {number} | {'REJECTED' if number == 17 else 'admitted'} | reports/round-{number}/validation.json |"
                 for number in range(17, 22))
    score = f"| loop 2 | 4 admitted / 1 rejected | {RETRO} |"
    check("evidence-bound historical retrospective accepted", evaluate_retrospective(retro, score, receipts)["passed"])
    check("unlanded SCORECARD summary rejected", not evaluate_retrospective(retro, "", receipts)["passed"])
    bad_receipts = {**receipts, 17: {"acceptance_checks_passed": True}}
    check("retroactive R17 admission rejected", not evaluate_retrospective(retro, score, bad_receipts)["passed"])
    check("missing freshness question rejected", not evaluate_retrospective(retro.replace("freshness", "topic"), score, receipts)["passed"])
    check("summary exit zero alone insufficient", not require_summary({"exit": 0, "stdout": "summary: 18/19 legs passed"}, r"(\d+)/(\d+) legs", (19, 19), "test")["passed"])
    check("19/19 nonzero exit rejected", not require_summary({"exit": 1, "stdout": "summary: 19/19 legs passed"}, r"(\d+)/(\d+) legs", (19, 19), "test")["passed"])
    check("duplicate JSON keys rejected", duplicate_key_control())
    for relative in ("/tmp/outside", "reports/../outside", ".git/config"):
        try:
            safe_path(relative)
            refused = False
        except ValueError:
            refused = True
        check(f"unsafe evidence path rejected: {relative}", refused)
    passed = all(row["passed"] for row in controls)
    print(json.dumps({"round": 22, "command": f"{COMMAND} --selftest", "date": today(),
                      "selftest_passed": passed, "controls": controls,
                      "controls_passed": metric(sum(row["passed"] for row in controls), "runner positive/negative controls"),
                      "controls_total": metric(len(controls), "runner positive/negative controls")}, indent=2, sort_keys=True))
    return 0 if passed else 1


def duplicate_key_control():
    try:
        strict_json('{"status": "open", "status": "fixed-with-control"}')
    except ValueError:
        return True
    return False


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def measure():
    evidence = Evidence()
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    targets = evidence.document(f"{ROUND_DIR}/targets.json") or {}
    baseline = claims.get("baseline_revision")
    preserved = protected_baseline(baseline)
    before = protected_inventory()
    regressions, runs = measure_regressions()
    results = {}
    for claim_id, operation in (
            ("O", lambda: measure_operability(evidence, regressions)),
            ("C", lambda: measure_calibration(evidence)),
            ("D", lambda: measure_depth(evidence, runs, baseline))):
        try:
            results[claim_id] = operation()
        except (OSError, ValueError, TypeError, KeyError, RuntimeError, AttributeError, subprocess.SubprocessError) as error:
            results[claim_id] = result([f"Could not evaluate claim {claim_id}: {type(error).__name__}: {error}"], {})
    after = protected_inventory()
    if before != after:
        preserved["failures"].append("Protected filed bytes changed during the current validation run")
        preserved["passed"] = False
    changed_inputs = []
    for relative, expected in evidence.inputs.items():
        try:
            observed = sha(safe_path(relative).read_bytes())
        except (OSError, ValueError):
            observed = None
        if expected != observed:
            changed_inputs.append(relative)
    coherence = []
    if claims.get("round") != 22 or targets.get("round") != 22:
        coherence.append("Claims/targets are not both round 22")
    if targets.get("baseline_revision") != baseline:
        coherence.append("Claims/targets disagree on the declared baseline")
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"O": "operability", "C": "calibration", "D": "depth"}:
        coherence.append("Declared claim set is not O/operability, C/calibration, D/depth")
    if changed_inputs:
        coherence.append("Evidence changed while being measured: " + ", ".join(changed_inputs))
    coherence.extend(evidence.errors)
    failures = [f"claim {claim_id}: {failure}" for claim_id, item in results.items() for failure in item["failures"]]
    failures.extend("preservation: " + item for item in preserved["failures"])
    failures.extend("evidence: " + item for item in coherence)
    return {"round": 22, "runner": RUNNER, "runner_sha256": sha(safe_path(RUNNER).read_bytes()),
            "counting_command": COMMAND, "date": today(), "baseline_revision": baseline,
            "targets_date": targets.get("date"), "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results,
            "failures": failures, "missing_dependencies": sorted(evidence.missing | {
                path for item in results.values() for path in item["missing_dependencies"]}),
            "protected_filed_artifacts": preserved,
            "protected_bytes_unchanged_during_run": metric(before == after, "before/after protected SHA-256 inventory"),
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": [
                "Run this round validator only in an isolated repository clone with TMPDIR below its .scratch. It never invokes an older round validator; historical verdicts are read from immutable filed receipts and newly filed dispositions.",
                "The fixed regression battery executes only declared selftest/check modes and handoff v2/v3 verification. The flagless D4 gate is checked through its supported packet interface, not an invented --selftest flag.",
                "Routed resolutions require six distinct issues, licensed dispositions, dated commands and resolvable round-22 controls. Malformed alias probes exercise the full CLI with one valid and four invalid packets; no recorded command string is executed.",
                "Retrospective and independent audit checks verify explicit historical states, source pointers, repair limits, conformance dispositions, pending operator calibration and the landed SCORECARD row. They do not establish canon, truth, worker attendance or external report filing.",
                "The selected D4 design forbids imported fixture data even under borrowed-reference names; negative method notes and legitimate linguistic borrow ledgers are not imports. Independent D2-fixture poison and D4-local rank-mutation controls complement the owned-field scan, dated SKILL draft and before/after source record.",
                "Protected reports and frozen generations from rounds 8-21 must match the round-22 declared Git baseline. New successor manifests are replayed only under the new round-22 generation; D4 replay verifies live peers against the full pinned snapshot through its require-live wrapper. Original historical rows remain untouched.",
                "The content-selection successor imports the digest-pinned historical round-20 module only in the isolated clone for selector/mtime controls, never its full validation/writer entrypoint. Generic replay mirrors are siblings of that clone, still inside the enclosing lane scratch directory.",
            ]}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Measure round-22 O/C/D acceptance; use only in an isolated clone.")
    parser.add_argument("--check", action="store_true", help="print the measured JSON without writing validation.json")
    parser.add_argument("--selftest", action="store_true", help="exercise runner positive/negative controls without dependencies")
    args = parser.parse_args(argv)
    if args.check and args.selftest:
        parser.error("--check and --selftest are mutually exclusive")
    if ".scratch" not in ROOT.parts or not (ROOT / ".git").is_dir():
        print("could-not-evaluate: run round validators only in an isolated Git clone under the lane's .scratch", file=sys.stderr)
        return 2
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    if args.selftest:
        return selftest()
    if not args.check:
        guard_receipt()
    try:
        receipt = measure()
    except (OSError, ValueError, TypeError, subprocess.SubprocessError) as error:
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
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
