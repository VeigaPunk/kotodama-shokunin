#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import copy
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-14"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
GUARD = "tools/harness/receipt_guard.py"
FILED = tuple(f"reports/round-{number}" for number in range(8, 13))
EXPECTED_STATES = {8: "admitted", 9: "admitted", 10: "admitted",
                   11: "rejected", 12: "admitted", 13: "skipped"}
ROUTED_IDS = ("R9-BATROOT", "R8-AUDCNT", "R10-F04", "R10-F05",
              "R10-RUNHASH", "R10-IXCLS", "R10-STATCONFL", "R11-DRAFT")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}(?=T|\b)")
POINTER_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|corpus|examples)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv)\b"
    r"|(?<![\w./-])(?:SCORECARD|LOG|SHONEN|PROVINCE)\.md\b")
REGRESSIONS = (
    ("tools/check-gate-battery.py", "--selftest"),
    ("tools/check-gate-battery.py",),
    ("tools/check-craft-exercise.py", "--selftest"),
    ("tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json"),
    ("tools/assemble-d2.py", "--selftest"),
    ("tools/assemble-d2.py", "--check"),
    ("tools/d2-typed-labels.py", "--selftest"),
    ("tools/d2-typed-labels.py", "--check"),
    ("tools/assemble-culture-d3.py", "--selftest"),
    ("tools/assemble-culture-d3.py", "--check"),
    ("tools/check-evidence-coupling.py", "--selftest"),
    ("tools/assemble-d2-typed.py", "--check"),
    ("tools/gates/typed-pipeline-gate.py", "--json"),
)


def today():
    return dt.date.today().isoformat()


def metric(value, operation):
    return {"value": value, "command": f"{COMMAND} ({operation})", "date": today()}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise ValueError(f"not an in-lane evidence path: {relative}")
    resolved = (ROOT / path).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError(f"evidence path escapes lane: {relative}")
    return resolved


def strict_json(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(text, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(
                          ValueError(f"non-finite JSON number: {value}")))


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

    def pointers(self, text):
        records = []
        for relative in sorted(set(POINTER_RE.findall(text))):
            try:
                path = safe_path(relative)
                if path.is_file():
                    data = path.read_bytes()
                    self.inputs[relative] = sha(data)
                    records.append({"path": relative, "sha256": sha(data), "exists": True})
                else:
                    records.append({"path": relative, "exists": False})
            except (OSError, ValueError) as error:
                records.append({"path": relative, "exists": False, "error": str(error)})
        return records


def result(failures, measurement, missing=()):
    return {"passed": not failures, "failures": failures,
            "measurement": measurement, "missing_dependencies": sorted(set(missing))}


def run_command(parts, timeout=300, env=None):
    argv = [sys.executable, *parts]
    child_env = dict(os.environ if env is None else env)
    child_env.update(TMPDIR=str(ROOT / ".scratch"), PYTHONDONTWRITEBYTECODE="1")
    item = {"command": shlex.join(["python3", *parts]), "date": today(),
            "argv": ["python3", *parts]}
    try:
        source = safe_path(parts[0])
        item["source_sha256_before"] = sha(source.read_bytes())
        run = subprocess.run(argv, cwd=ROOT, capture_output=True,
                             timeout=timeout, env=child_env)
        item["source_sha256_after"] = sha(source.read_bytes())
        item["source_unchanged"] = item["source_sha256_before"] == item["source_sha256_after"]
        item.update(exit=run.returncode if item["source_unchanged"] else None,
                    stdout_sha256=sha(run.stdout), stderr_sha256=sha(run.stderr),
                    stdout_tail=run.stdout.decode("utf-8", "replace")[-1000:],
                    stderr_tail=run.stderr.decode("utf-8", "replace")[-1000:])
        try:
            item["json"] = strict_json(run.stdout.decode("utf-8"))
        except (ValueError, UnicodeError):
            pass
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error), timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def git(*args, data=None):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    proc = subprocess.run(["git", "--literal-pathspecs", *args], cwd=ROOT,
                          input=data, capture_output=True, timeout=90, env=env)
    if proc.returncode:
        raise ValueError(f"git {shlex.join(args)}: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout


def json_extends(old, new):
    if isinstance(old, dict):
        return isinstance(new, dict) and all(
            key in new and json_extends(value, new[key]) for key, value in old.items())
    if isinstance(old, list):
        return isinstance(new, list) and len(new) >= len(old) and all(
            json_extends(value, new[index]) for index, value in enumerate(old))
    return type(old) is type(new) and old == new


def preservation_kind(relative, old, new):
    if old == new:
        return "byte-identical"
    if new.startswith(old):
        if relative.endswith(".json"):
            try:
                strict_json(new.decode("utf-8"))
            except (ValueError, UnicodeError):
                return "violation"
        return "append-only"
    if relative.endswith(".json"):
        try:
            unchanged_values = json_extends(strict_json(old.decode("utf-8")),
                                            strict_json(new.decode("utf-8")))
            remaining = iter(new)
            if unchanged_values and all(byte in remaining for byte in old):
                return "append-only-json-entries"
        except (ValueError, UnicodeError):
            pass
    return "violation"


def filed_snapshot():
    snapshot = {}
    for directory in FILED:
        for path in sorted((ROOT / directory).rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                relative = path.relative_to(ROOT).as_posix()
                try:
                    snapshot[relative] = sha(safe_path(relative).read_bytes())
                except (OSError, ValueError) as error:
                    snapshot[relative] = f"ERROR: {error}"
    return snapshot


def filed_preservation(baseline):
    failures, rows = [], []
    try:
        if not isinstance(baseline, str) or not re.fullmatch(r"[0-9a-f]{40,64}", baseline):
            raise ValueError("claims.json has no full baseline revision")
        entries = []
        for record in git("ls-tree", "-r", "-z", baseline, "--", *FILED).split(b"\0"):
            if not record:
                continue
            metadata, raw_path = record.split(b"\t", 1)
            mode, kind, oid = metadata.split()
            if kind != b"blob" or mode not in (b"100644", b"100755"):
                raise ValueError(f"non-regular filed entry: {raw_path!r}")
            entries.append((raw_path.decode("utf-8"), oid))
        if not entries:
            raise ValueError("no filed round-8..12 blobs at the declared baseline")
        objects = git("cat-file", "--batch", data=b"".join(oid + b"\n" for _, oid in entries))
        offset = 0
        for relative, oid in entries:
            end = objects.index(b"\n", offset)
            header = objects[offset:end].split()
            if len(header) != 3 or header[0] != oid or header[1] != b"blob":
                raise ValueError(f"unexpected Git blob reply for {relative}")
            size = int(header[2])
            old = objects[end + 1:end + 1 + size]
            offset = end + size + 2
            try:
                new = safe_path(relative).read_bytes()
                disposition = preservation_kind(relative, old, new)
            except (OSError, ValueError) as error:
                new, disposition = b"", "violation"
                failures.append(f"Filed artifact unreadable: {relative}: {error}")
            rows.append({"path": relative, "baseline_sha256": sha(old),
                         "current_sha256": sha(new), "preservation": disposition})
            if disposition == "violation":
                failures.append(f"Filed bytes changed other than append-only: {relative}")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"Cannot establish filed-byte preservation: {error}")
    return result(failures, {"baseline_revision": baseline, "files": rows,
                            "checked": metric(len(rows), "compare baseline Git blobs with filed worktree bytes"),
                            "violations": metric(sum(row["preservation"] == "violation" for row in rows),
                                                 "count non-append-only filed changes")})


def markdown_receipt(text):
    dated = bool(DATE_RE.search(text))
    commanded = bool(re.search(r"\b(?:python3?|git|sha256sum|command|commands)\b", text, re.I))
    label = r"(?:overall(?: result| verdict)?|final(?: audit)?(?: result| verdict)|result|verdict|status|conclusion)"
    entries = [(match.start(), match.group(1)) for match in re.finditer(
        rf"(?im)^\s*(?:[-*]\s+)?(?:\*\*)?{label}(?:\*\*)?\s*[:—-]\s*(.+)$", text)]
    entries.extend((match.start(), match.group(1)) for match in re.finditer(
        rf"(?i)\*\*{label}\s*:\s*(.+?)\*\*", text))
    verdicts = [value for _, value in sorted(entries)]
    states = []
    for value in verdicts:
        value = value.lstrip(" *`_")
        if re.match(r"FAIL(?:ED)?\b|NOT GREEN\b|BLOCKED\b|INCOMPLETE\b|PENDING\b", value, re.I):
            states.append(False)
        elif (re.search(r"\bPASS(?:ED)?\b|\bGREEN\b", value, re.I)
              or re.search(r"positive evidence citations resolve.*claim coverage is complete", value, re.I)):
            states.append(True)
    return {"dated": dated, "command_carried": commanded,
            "verdicts": verdicts, "passed": dated and commanded and bool(states) and states[-1]}


def json_receipt(payload):
    if not isinstance(payload, dict):
        return {"passed": False}
    text = json.dumps(payload, ensure_ascii=False)
    dated = bool(DATE_RE.search(text))
    commanded = bool(payload.get("command") or payload.get("counting_command"))
    passed = payload.get("passed", payload.get("selftest_passed", payload.get("acceptance_checks_passed"))) is True
    total = payload.get("controls_total")
    complete = total is None or (isinstance(total, int) and not isinstance(total, bool)
                                and total > 0 and payload.get("controls_passed") == total)
    return {"dated": dated, "command_carried": commanded,
            "passed": dated and commanded and passed and complete}


def evidence_group(evidence, relatives, minimum, label):
    rows, failures = [], []
    for relative in sorted(set(relatives)):
        text = evidence.text(relative)
        payload = None
        if relative.endswith(".json"):
            try:
                payload = strict_json(text)
            except ValueError as error:
                failures.append(f"Invalid {label}: {relative}: {error}")
            checked = json_receipt(payload)
        else:
            checked = markdown_receipt(text)
        if isinstance(payload, dict) and payload.get("guard_sha256"):
            if payload["guard_sha256"] != sha((ROOT / GUARD).read_bytes()):
                failures.append(f"{label} binds stale guard bytes: {relative}")
        rows.append({"path": relative, "sha256": evidence.inputs.get(relative), **checked})
        if not checked["passed"]:
            failures.append(f"{label} lacks a dated, command-carried green result: {relative}")
    if len(rows) < minimum:
        failures.append(f"Missing {label}: need {minimum}, found {len(rows)}")
    return result(failures, {"receipts": rows, "count": metric(len(rows), f"inventory {label}")},
                  [f"{ROUND_DIR}/<{label}>" ] if len(rows) < minimum else ())


def round14_evidence():
    return [path.relative_to(ROOT).as_posix() for path in sorted((ROOT / ROUND_DIR).rglob("*"))
            if path.is_file() and path.suffix in (".md", ".json")]


def resolution_rows(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("items", "resolutions", "routed_items", "entries", "dispositions", "routed_resolution"):
            value = payload.get(key)
            if isinstance(value, list):
                return value
            if isinstance(value, dict):
                return [dict(row, id=key) if isinstance(row, dict) else row
                        for key, row in value.items()]
    return []


def canonical_route(row):
    identity = str(row.get("id", row.get("finding_id", row.get("source_id", ""))))
    if identity in ROUTED_IDS:
        return identity
    match = re.fullmatch(r"(?:R14-)?O0?([1-8])", identity, re.I)
    if match:
        return ROUTED_IDS[int(match.group(1)) - 1]
    text = json.dumps(row, ensure_ascii=False)
    matching = [name for name in ROUTED_IDS if name in text]
    return matching[0] if len(matching) == 1 else None


def check_resolution(payload, evidence):
    failures, checked, seen = [], [], set()
    rows = resolution_rows(payload)
    for row in rows:
        if not isinstance(row, dict):
            failures.append("Routed resolution row is not an object")
            continue
        route = canonical_route(row)
        if route is None or route in seen:
            failures.append(f"Unknown or duplicate routed resolution: {row.get('id')}")
            continue
        seen.add(route)
        failures_before = len(failures)
        status = str(row.get("disposition", row.get("status", ""))).strip().lower()
        if status not in ("applied-with-control", "resolved-by-documentation"):
            failures.append(f"{route}: disposition must be applied-with-control or resolved-by-documentation")
        serialized = json.dumps(row, ensure_ascii=False)
        pointers = evidence.pointers(serialized)
        own_pointers = [item for item in pointers if item["path"].startswith(ROUND_DIR + "/")]
        if not own_pointers or any(not item["exists"] for item in pointers):
            failures.append(f"{route}: missing or broken evidence pointers")
        texts = [evidence.text(item["path"]) for item in own_pointers if item["exists"]]
        combined = serialized + "\n" + "\n".join(texts)
        if not DATE_RE.search(combined) or not re.search(r"\b(?:python3?|git|sha256sum|command)\b", combined, re.I):
            failures.append(f"{route}: evidence lacks command/date")
        if not re.search(r"(?<!with-)\bcontrols?\b", combined, re.I):
            failures.append(f"{route}: no demonstrated control")
        if not re.search(re.escape(status), "\n".join(texts), re.I):
            failures.append(f"{route}: disposition disagrees with its evidence")
        checked.append({"id": route, "disposition": status, "pointers": pointers,
                        "passed": len(failures) == failures_before})
    for route in ROUTED_IDS:
        if route not in seen:
            failures.append(f"Missing routed disposition: {route}")
    if len(rows) != 8:
        failures.append(f"Routed resolution must contain exactly eight rows, found {len(rows)}")
    return result(failures, {"rows": checked,
                            "required": metric(8, "declared O routed-item threshold"),
                            "dispositioned": metric(sum(row["passed"] for row in checked),
                                                   "known routed IDs with licensed disposition and evidence controls")})


def measure_o(evidence, paths, regressions):
    relative = f"{ROUND_DIR}/routed-resolution.json"
    payload = evidence.document(relative)
    resolution = check_resolution(payload, evidence)
    verifiers = evidence_group(evidence, [path for path in paths
        if re.search(r"verif", Path(path).name, re.I)
        and "/guard/" not in path and "retrospective" not in path], 4, "operability verifiers")
    regression_receipts = evidence_group(evidence, [path for path in paths
        if "regression" in Path(path).name.lower() and "/guard/" not in path], 1, "regression receipts")
    failures = [*resolution["failures"], *verifiers["failures"], *regression_receipts["failures"]]
    failures.extend(f"Regression failed: {item['command']} (exit {item.get('exit')})"
                    for item in regressions if item.get("exit") != 0)
    return result(failures, {"resolution": resolution, "verifiers": verifiers,
                            "regression_receipts": regression_receipts,
                            "regressions": {"runs": regressions,
                                "green": metric(sum(item.get("exit") == 0 for item in regressions),
                                                "execute read-only regression commands"),
                                "total": metric(len(REGRESSIONS), "required regression command inventory")}},
                  ([relative] if payload is None else []) + verifiers["missing_dependencies"]
                  + regression_receipts["missing_dependencies"])


def guard_preflight():
    spec = importlib.util.spec_from_file_location("round14_receipt_guard", ROOT / GUARD)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import receipt guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)
    except Exception as error:
        if isinstance(error, getattr(module, "ReceiptGuardError", ())):
            print(str(error), file=sys.stderr)
            raise SystemExit(3) from error
        raise


def measure_d(evidence, paths, guard_run, preservation):
    guard_text = evidence.text(GUARD)
    design = evidence.text(f"{ROUND_DIR}/guard/design.md")
    negatives = evidence_group(evidence, [path for path in paths if "/guard/" in path
        and re.search(r"neg(?:ative|s|[-_.])", Path(path).name, re.I)], 2, "guard negative receipts")
    retro_tests = evidence_group(evidence, [path for path in paths if "/guard/" in path
        and path.endswith(".json") and re.search(r"retro|historical", Path(path).name, re.I)],
        1, "guard retro-test receipts")
    errata = []
    for path in (ROOT / "reports/round-12/defects").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if re.search(r"receipt.guard|REFRESH_RECEIPTS", text, re.I) and re.search(r"round.?14|R14", text):
            relative = path.relative_to(ROOT).as_posix()
            evidence.text(relative)
            errata.append(relative)
    ledger = evidence.document("reports/round-12/defects/ledger.json")
    ledger_text = json.dumps(ledger, ensure_ascii=False)
    if re.search(r"receipt.guard|REFRESH_RECEIPTS", ledger_text, re.I):
        errata.append("reports/round-12/defects/ledger.json")
    failures = [*negatives["failures"], *retro_tests["failures"], *preservation["failures"]]
    if not guard_text or not design:
        failures.append("Receipt guard implementation or design is missing")
    payload = guard_run.get("json", {})
    if guard_run.get("exit") != 0 or not isinstance(payload, dict) or payload.get("selftest_passed") is not True:
        failures.append("Receipt guard selftest did not report an explicit green result")
    if not errata:
        failures.append("No append-only round-12 defect-ledger exposure erratum cites the receipt guard")
    source = evidence.text(RUNNER)
    tree = ast.parse(source)
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Name) and node.func.id == "guard_preflight"]
    if len(calls) < 2:
        failures.append("Runner does not guard both the measurement and publication boundaries")
    return result(failures, {"guard_selftest": guard_run, "negatives": negatives,
                            "retro_tests": retro_tests, "filed_bytes": preservation,
                            "exposure_errata": errata,
                            "guard_call_sites": metric(len(calls), "AST count guard preflight calls")},
                  negatives["missing_dependencies"] + retro_tests["missing_dependencies"]
                  + ([GUARD] if not guard_text else []))


def round_section(text, number):
    headers = list(re.finditer(r"(?im)^#{1,6}\s+[^\n]*\bround[ -]+(8|9|10|11|12|13)\b[^\n]*$", text))
    for index, header in enumerate(headers):
        if int(header.group(1)) == number:
            end = headers[index + 1].start() if index + 1 < len(headers) else len(text)
            return text[header.start():end]
    rows = re.findall(rf"(?im)^\|\s*(?:round[ -]*)?{number}\s*\|[^\n]+$", text)
    return "\n".join(rows)


def measure_c(evidence, paths):
    relative = f"{ROUND_DIR}/loop1-retrospective.md"
    text = evidence.text(relative)
    failures, states, thresholds = [], [], []
    pointers = evidence.pointers(text)
    broken = [item["path"] for item in pointers if not item["exists"]]
    if broken:
        failures.append("Retrospective has broken in-lane pointers: " + ", ".join(broken))
    for number, expected in EXPECTED_STATES.items():
        section = round_section(text, number)
        found = bool(re.search(rf"\b{expected}\b", section, re.I))
        if not found:
            failures.append(f"Retrospective omits round {number} final state {expected}")
        states.append({"round": number, "expected": expected, "stated": found})
        if number == 13:
            if not re.search(r"operator|cancel", section, re.I):
                failures.append("Round-13 skip lacks operator attribution")
            continue
        claim_path = f"reports/round-{number}/claims.json"
        receipt_path = f"reports/round-{number}/validation.json"
        claims = evidence.document(claim_path) or {}
        receipt = evidence.document(receipt_path) or {}
        if receipt.get("acceptance_checks_passed") is not (expected == "admitted"):
            failures.append(f"Filed round-{number} acceptance contradicts expected final state")
        if not any(item["path"] in (claim_path, receipt_path) for item in pointers):
            failures.append(f"Retrospective lacks a round-{number} claim/receipt evidence pointer")
        for claim in claims.get("claims", []):
            claim_id = claim.get("id")
            axis = claim.get("axis", "")
            documented = bool(re.search(rf"\b(?:{re.escape(str(claim_id))}|{re.escape(axis)})\b", section, re.I)
                              and re.search(r"threshold|honou?red|met|pass|fail|verified|satisfied|declared", section, re.I))
            thresholds.append({"round": number, "claim": claim_id, "documented": documented,
                               "filed_passed": (receipt.get("claims", {}).get(claim_id) or {}).get("passed")})
            if not documented:
                failures.append(f"Round {number} claim {claim_id} threshold disposition is missing")
    r11 = round_section(text, 11)
    for pattern, description in ((r"95\s*%|0\.95", "unchanged 95% threshold"),
                                  (r"147\s*[/÷]\s*189|147[^\n]{0,30}189", "147/189 comparable ratio"),
                                  (r"147\s*[/÷]\s*192|147[^\n]{0,30}192", "147/192 all-row ratio"),
                                  (r"\bfail(?:ed|ure)?\b", "failed freshness claim")):
        if not re.search(pattern, r11, re.I):
            failures.append(f"Round-11 retrospective omits {description}")
    if not (re.search(r"operator", text, re.I) and re.search(r"calibrat|recalibrat", text, re.I)
            and re.search(r"question|pending|ruling|\?", text, re.I)):
        failures.append("Retrospective does not restate the operator freshness-calibration question")
    classes = {
        "out-of-lane": r"out[- ]of[- ]lane",
        "filed-receipt": r"filed[- ]receipt|receipt[^\n]{0,40}(?:clobber|rewrit)",
        "availability": r"availability|402|late[- ](?:worker|seat)",
        "scratch": r"inode|/tmp|scratch",
        "baseline-layout": r"baseline[^\n]{0,50}(?:root|layout)",
        "report-reconciliation": r"draft|report.reconcil|ratio.documentation",
        "schema-or-count": r"schema|transcription|misclassif|audit.count|count.erratum",
    }
    class_rows = []
    for name, pattern in classes.items():
        matched = bool(re.search(pattern, text, re.I))
        class_rows.append({"class": name, "enumerated": matched})
    if sum(item["enumerated"] for item in class_rows) < 6 or not re.search(
            r"disposition|resolved|routed|carried|documented", text, re.I):
        failures.append("Retrospective does not enumerate six conformance-defect classes and dispositions")
    auditors = evidence_group(evidence, [path for path in paths
        if re.search(r"retrospective.*audit|audit.*retrospective", Path(path).name, re.I)], 2, "retrospective auditors")
    failures.extend(auditors["failures"])
    for audit in auditors["measurement"]["receipts"]:
        if text and sha(text.encode("utf-8")) not in evidence.text(audit["path"]):
            failures.append(f"Retrospective auditor does not bind the current retrospective SHA-256: {audit['path']}")
    scorecard = evidence.text("SCORECARD.md")
    if not re.search(r"loop[- ]?1[^\n]{0,100}(?:summary|retrospect)|(?:summary|retrospect)[^\n]{0,100}loop[- ]?1", scorecard, re.I):
        failures.append("SCORECARD lacks the loop-1 summary row")
    if relative not in scorecard:
        failures.append("SCORECARD does not point to the loop-1 retrospective")
    if not text or not DATE_RE.search(text):
        failures.append("Retrospective is missing or undated")
    return result(failures, {"retrospective": relative, "final_states": states,
                            "thresholds": thresholds, "pointers": pointers,
                            "conformance_classes": class_rows, "auditors": auditors,
                            "admitted": metric(4, "expected round-8/9/10/12 final admissions"),
                            "rejected": metric(1, "expected round-11 final rejection"),
                            "skipped": metric(1, "expected round-13 operator skip")},
                  ([relative] if not text else []) + auditors["missing_dependencies"])


def validate():
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(exist_ok=True)
    evidence = Evidence()
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    targets = evidence.document(f"{ROUND_DIR}/targets.json") or {}
    before = filed_snapshot()
    paths = round14_evidence()
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(run_command, parts) for parts in REGRESSIONS]
        guard_future = pool.submit(run_command, (GUARD, "--selftest"))
        regressions = [future.result() for future in futures]
        guard_run = guard_future.result()
    preservation = filed_preservation(claims.get("baseline_revision"))
    results = {"O": measure_o(evidence, paths, regressions),
               "D": measure_d(evidence, paths, guard_run, preservation),
               "C": measure_c(evidence, paths)}
    after = filed_snapshot()
    changes = [{"path": path, "before": before.get(path), "after": after.get(path)}
               for path in sorted(before.keys() | after.keys()) if before.get(path) != after.get(path)]
    if changes:
        results["D"]["failures"].append("Filed round-8..12 bytes/path set changed during validation; rerun on a settled tree")
        results["D"]["passed"] = False
    declared = {claim.get("id"): claim.get("axis") for claim in claims.get("claims", [])
                if isinstance(claim, dict)}
    if declared != {"O": "operability", "D": "depth", "C": "calibration"}:
        results["C"]["failures"].append("Round-14 declared claims do not match O/D/C")
        results["C"]["passed"] = False
    if evidence.errors:
        results["C"]["failures"].extend(evidence.errors)
        results["C"]["passed"] = False
    return {
        "round": 14, "runner": RUNNER, "runner_sha256": sha((ROOT / RUNNER).read_bytes()),
        "counting_command": COMMAND, "date": today(),
        "baseline_revision": claims.get("baseline_revision"), "targets_date": targets.get("date"),
        "claims_declared": declared, "acceptance_checks_passed": all(item["passed"] for item in results.values()),
        "claims": results, "input_sha256": dict(sorted(evidence.inputs.items())),
        "failures": [f"claim {claim_id}: {failure}" for claim_id, item in results.items() for failure in item["failures"]],
        "missing_dependencies": sorted(evidence.missing | {path for item in results.values() for path in item["missing_dependencies"]}),
        "filed_rounds": {"baseline": preservation, "changed_during_validation": changes,
                         "snapshot_before": before, "snapshot_after": after,
                         "command": f"{COMMAND} (hash filed round-8..12 paths before/after checks)", "date": today()},
        "limits": [
            "Historical validators are never executed. Only fixed read-only check/selftest commands run; no command is executed from an evidence file.",
            "Filed artifacts are compared with the declared baseline: non-JSON additions must be suffix-only; JSON may gain keys/list entries only while preserving every original byte in order and every original value. Concurrent filed-path changes fail closed.",
            "Markdown controls and independent reviews are dated evidence, not automatically re-executed shell snippets. Green regression and guard-selftest measurements are fresh executions.",
            "Receipt publication checks the shared guard before measurements and immediately before writing. The guard is cooperative preflight, not race-proof locking or protection for historical runners that were never wired.",
            "Retrospective checks are structural and source-bound, not an oracle for factual truth or operator approval. Round 11 remains rejected and round 13 remains skipped.",
        ],
    }


def selftest():
    controls = []

    def check(name, value):
        controls.append({"control": name, "passed": bool(value)})

    old = b'{"rows": [{"id": 1}], "state": "filed"}\n'
    appended = b'{"rows": [{"id": 1}], "state": "filed", "errata": [{"id": "R14"}]}\n'
    check("filed-identical", preservation_kind("x.json", old, old) == "byte-identical")
    check("new-json-key-preserves-filed-bytes", preservation_kind("x.json", old, appended) == "append-only-json-entries")
    check("filed-value-rewrite-rejected", preservation_kind("x.json", old, old.replace(b'"filed"', b'"edited"')) == "violation")
    check("filed-row-rewrite-with-erratum-rejected", preservation_kind("x.json", old, appended.replace(b'"id": 1', b'"id": 2')) == "violation")
    check("filed-whitespace-removal-rejected", preservation_kind("x.json", old, old.replace(b" ", b"")) == "violation")
    check("markdown-suffix-allowed", preservation_kind("x.md", b"filed\n", b"filed\naddendum\n") == "append-only")
    check("markdown-insertion-rejected", preservation_kind("x.md", b"filed\n", b"new\nfiled\n") == "violation")
    for bad in ('{"x": 1, "x": 2}', '{"x": NaN}'):
        try:
            strict_json(bad)
        except ValueError:
            check("malformed-json-rejected-" + bad, True)
        else:
            check("malformed-json-rejected-" + bad, False)
    check("empty-resolution-rejected", not check_resolution({}, Evidence())["passed"])

    class MemoryEvidence:
        def __init__(self, *, exists=True, control=True):
            self.exists, self.control = exists, control

        def pointers(self, text):
            return [{"path": f"{ROUND_DIR}/fixture.md", "exists": self.exists}]

        def text(self, relative):
            return ("2026-10-17 command: python3 tool.py\nDisposition: applied-with-control\nControl: PASS\n"
                    if self.control else "Disposition: applied-with-control\n")

    complete = {"items": [{"id": route, "disposition": "applied-with-control"} for route in ROUTED_IDS]}
    check("eight-dispositions-accepted", check_resolution(complete, MemoryEvidence())["passed"])
    for name, mutation in (
        ("missing-route", lambda rows: rows.pop()),
        ("duplicate-route", lambda rows: rows.__setitem__(0, copy.deepcopy(rows[1]))),
        ("unknown-route", lambda rows: rows[0].__setitem__("id", "UNKNOWN")),
        ("unresolved-route", lambda rows: rows[0].__setitem__("disposition", "pending")),
    ):
        bad = copy.deepcopy(complete)
        mutation(bad["items"])
        check(name + "-rejected", not check_resolution(bad, MemoryEvidence())["passed"])
    check("broken-resolution-pointer-rejected", not check_resolution(complete, MemoryEvidence(exists=False))["passed"])
    check("undated-resolution-control-rejected", not check_resolution(complete, MemoryEvidence(control=False))["passed"])
    check("missing-evidence-rejected", not markdown_receipt("Result: PASS")["passed"])
    check("provisional-audit-not-green", not markdown_receipt(
        "2026-10-17 command: python3 audit.py\nSource controls PASS; retrospective pending")["passed"])
    check("iso-timestamp-receipt-accepted", markdown_receipt(
        "2026-10-18T00:00:00Z command: python3 guard.py\nResult: PASS")["passed"])
    check("negative-expected-refusal-not-failure", markdown_receipt(
        "2026-10-17 command: python3 guard.py\nExpected exit 3; control PASS\nResult: PASS")["passed"])
    check("final-red-verdict-rejected", not markdown_receipt(
        "2026-10-17 command: python3 guard.py\ncontrol PASS\nResult: FAIL")["passed"])
    check("expected-domain-failure-not-regression", markdown_receipt(
        "2026-10-17 command: python3 gate.py\nResult: PASS; expected domain FAIL remained visible")["passed"])
    green_json = {"command": "python3 tests.py", "started_at_utc": "2026-10-18T00:00:00Z",
                  "passed": True, "controls_total": 2, "controls_passed": 2}
    check("json-controls-accepted", json_receipt(green_json)["passed"])
    check("partial-json-controls-rejected", not json_receipt(dict(green_json, controls_passed=1))["passed"])
    check("false-json-controls-rejected", not json_receipt(dict(green_json, passed=False))["passed"])
    text = "## Round 8 — admitted\nF/O/D thresholds met\n## Round 11 — rejected\nF failed at 0.95\n"
    check("round-state-sections-do-not-bleed", "rejected" not in round_section(text, 8))
    for relative in ("../outside.md", "/outside.md", ".git/config"):
        try:
            safe_path(relative)
        except ValueError:
            check("unsafe-pointer-rejected-" + relative, True)
        else:
            check("unsafe-pointer-rejected-" + relative, False)
    for index, route in enumerate(ROUTED_IDS, 1):
        check("canonical-route-" + route, canonical_route({"id": f"R14-O{index:02d}"}) == route)
    payload = {"runner": RUNNER, "command": COMMAND + " --selftest", "date": today(),
               "selftest_passed": all(item["passed"] for item in controls), "controls": controls,
               "passed": metric(sum(item["passed"] for item in controls), "validator selftest controls"),
               "total": metric(len(controls), "validator selftest control inventory")}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["selftest_passed"] else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate round-14 O/D/C without rewriting historical receipts.")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--selftest", action="store_true", help="run in-memory validator controls, no receipt write")
    modes.add_argument("--check", action="store_true", help="run full acceptance and print JSON without writing validation.json")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.check:
        try:
            guard_preflight()
        except (OSError, RuntimeError, ImportError) as error:
            print(f"RECEIPT-GUARD-UNAVAILABLE: {error}", file=sys.stderr)
            return 3
    receipt = validate()
    if args.check:
        print(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        guard_preflight()
        (ROOT / OUTPUT).write_text(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
