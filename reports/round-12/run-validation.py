#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-12"
CLAIMS = f"{ROUND_DIR}/claims.json"
TARGETS = f"{ROUND_DIR}/targets.json"
OUTPUT = f"{ROUND_DIR}/validation.json"
RUNNER = f"{ROUND_DIR}/run-validation.py"
R8_R11 = (8, 9, 10, 11)
LICENSED_DISPOSITIONS = ("environmental", "legitimate-change", "defect")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")


def today():
    return dt.date.today().isoformat()


def command_name(argv):
    if not isinstance(argv, (list, tuple)) or not argv:
        return None
    parts = [str(value) for value in argv]
    if parts[0] in ("python", "python3", sys.executable):
        if parts[0] == sys.executable:
            parts[0] = "python3"
        return shlex.join(parts)
    if parts[0].endswith(".py"):
        return shlex.join(["python3", *parts])
    return None


def normalized_command(value):
    if isinstance(value, (list, tuple)):
        return command_name(value)
    if not isinstance(value, str):
        return None
    text = " ".join(value.split()).strip().strip("`")
    text = re.sub(r"(\.py)\s+\([^()]*\)$", r"\1", text)
    try:
        parts = shlex.split(text)
    except ValueError:
        return None
    if not parts:
        return None
    if parts[0] in ("python", "python3", sys.executable):
        if parts[0] == sys.executable:
            parts[0] = "python3"
        return shlex.join(parts)
    if parts[0].endswith(".py"):
        return shlex.join(["python3", *parts])
    return None


def command_segments(value):
    if isinstance(value, (list, tuple)):
        return [value]
    if not isinstance(value, str):
        return []
    try:
        lexer = shlex.shlex(value, posix=True, punctuation_chars=";")
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        return []
    segments, current = [], []
    for token in tokens:
        if token == ";":
            if current:
                segments.append(current)
                current = []
        else:
            current.append(token)
    if current:
        segments.append(current)
    return segments


def read_json(relative):
    path = ROOT / relative
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None


def read_text(relative):
    try:
        return (ROOT / relative).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def digest(relative):
    path = ROOT / relative
    if not path.is_file():
        return None
    value = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1 << 16), b""):
                value.update(chunk)
    except OSError:
        return None
    return value.hexdigest()


def git_output(*args):
    try:
        proc = subprocess.run(("git", *args), cwd=ROOT, capture_output=True,
                              text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    return proc.stdout if proc.returncode == 0 else None


def git_status(paths):
    result = git_output("status", "--short", "--", *paths)
    return result.strip() if result is not None else None


def command_run(argv, timeout=300):
    rendered = " ".join(shlex.quote(str(part)) for part in argv)
    env = os.environ.copy()
    env["TMPDIR"] = str(ROOT / ".scratch")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    item = {"command": rendered, "date": today(), "argv": list(argv)}
    try:
        proc = subprocess.run(argv, cwd=ROOT, capture_output=True,
                              timeout=timeout, env=env)
    except subprocess.TimeoutExpired as error:
        item.update({"exit": None, "timeout": True,
                     "stdout_tail": (error.stdout or b"").decode(
                         "utf-8", "replace")[-300:],
                     "stderr_tail": (error.stderr or b"").decode(
                         "utf-8", "replace")[-300:]})
        return item
    except (OSError, subprocess.SubprocessError) as error:
        item.update({"exit": None, "error": str(error)[:300]})
        return item
    item.update({
        "exit": proc.returncode,
        "stdout_sha256": hashlib.sha256(proc.stdout).hexdigest(),
        "stderr_sha256": hashlib.sha256(proc.stderr).hexdigest(),
        "stdout_tail": proc.stdout.decode("utf-8", "replace")[-300:],
        "stderr_tail": proc.stderr.decode("utf-8", "replace")[-300:],
    })
    return item


def command_sources():
    found = {}
    for round_number in R8_R11:
        validation_path = f"reports/round-{round_number}/validation.json"
        validation = read_json(validation_path)
        round_claims = read_json(f"reports/round-{round_number}/claims.json")
        if not isinstance(validation, dict):
            validation = {}
        if not isinstance(round_claims, dict):
            round_claims = {}
        source_date = (validation.get("date") or round_claims.get("date")
                       or "unknown")
        top_command = normalized_command(validation.get("counting_command"))
        if top_command:
            found.setdefault((round_number, top_command), set()).add(
                f"{validation_path}:counting_command@{source_date}")
        declared_claims = round_claims.get("claims", [])
        if isinstance(declared_claims, list):
            for claim in declared_claims:
                if not isinstance(claim, dict):
                    continue
                for index, segment in enumerate(
                        command_segments(claim.get("counting_command"))):
                    command = normalized_command(segment)
                    if command:
                        claim_id = claim.get("id", "unknown")
                        found.setdefault((round_number, command), set()).add(
                            f"reports/round-{round_number}/claims.json:claims.{claim_id}.counting_command[{index}]@{source_date}")

        def visit(value, pointer):
            if isinstance(value, dict):
                for key, child in value.items():
                    child_pointer = f"{pointer}.{key}"
                    if key in ("command", "command_line", "argv",
                               "recheck_command"):
                        command = normalized_command(child)
                        if command:
                            found.setdefault((round_number, command), set()).add(
                                f"{validation_path}:{child_pointer}@{source_date}")
                    visit(child, child_pointer)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    visit(child, f"{pointer}[{index}]")

        claims = validation.get("claims")
        if isinstance(claims, dict):
            for claim_id, claim in claims.items():
                measurement = claim.get("measurement") if isinstance(
                    claim, dict) else None
                if measurement is not None:
                    visit(measurement, f"claims.{claim_id}.measurement")
    return found


def rows_from(payload, keys):
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in keys:
            if isinstance(payload.get(key), list):
                return [item for item in payload[key] if isinstance(item, dict)]
        for key in keys:
            if isinstance(payload.get(key), dict):
                return [item for item in payload[key].values()
                        if isinstance(item, dict)]
    return []


def row_round(row):
    value = row.get("round", row.get("source_round", row.get("round_number")))
    try:
        return int(value)
    except (TypeError, ValueError):
        match = re.search(r"round[- ]?(8|9|10|11)\b", json.dumps(row), re.I)
        return int(match.group(1)) if match else None


def disposition_details(value):
    if isinstance(value, dict):
        rendered = json.dumps(value, ensure_ascii=False, sort_keys=True)
        klass = str(value.get("class", value.get("type", value.get(
            "cause_class", value.get("kind", ""))))).lower()
        evidence = value.get("evidence", value.get("reason", value.get(
            "cause", value.get("note", ""))))
    elif isinstance(value, list):
        rendered = json.dumps(value, ensure_ascii=False, sort_keys=True)
        klass = rendered.lower()
        evidence = rendered
    else:
        rendered = str(value or "")
        klass = rendered.lower()
        evidence = rendered
    disposition_text = re.sub(r"[\s_]+", "-", f"{klass} {evidence}".lower())
    accepted = next((name for name in LICENSED_DISPOSITIONS
                     if name in disposition_text), None)
    return accepted, str(evidence or rendered).strip(), rendered


def receipt_disposition(row):
    classes = [row.get(key) for key in
               ("drift_class", "disposition_class", "cause_class", "drift_cause")]
    evidence = [row.get(key) for key in
                ("drift_evidence", "evidence", "semantics_reproduced", "verdict")]
    rendered_class = " ".join(str(value) for value in classes if value)
    rendered_evidence = " ".join(str(value) for value in evidence if value)
    return disposition_details({"class": rendered_class,
                                "evidence": rendered_evidence})


def recount_disposition_details(row):
    value = row.get("disposition")
    if value and not (isinstance(value, str)
                      and value.strip().lower() in ("disposition", "match", "mismatch")):
        return disposition_details(value)
    classes = [row.get(key) for key in ("disposition_class", "cause_class", "cause")]
    evidence = [row.get(key) for key in ("evidence", "reason", "note", "cause")]
    return disposition_details({
        "class": " ".join(str(item) for item in classes if item),
        "evidence": " ".join(str(item) for item in evidence if item),
    })


def scalar_values(value):
    if isinstance(value, dict):
        return [item for child in value.values() for item in scalar_values(child)]
    if isinstance(value, list):
        return [item for child in value for item in scalar_values(child)]
    return [value]


def scalar_equal(left, right):
    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is type(right) and left == right
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        tolerance = 0.0001 * max(abs(left), abs(right), 1)
        return abs(left - right) <= tolerance
    return type(left) is type(right) and left == right


def recorded_values_present(recorded, observed):
    if recorded == observed:
        return True
    wanted = scalar_values(recorded)
    available = scalar_values(observed)
    if not wanted:
        return recorded == observed
    for value in wanted:
        match = next((index for index, candidate in enumerate(available)
                      if scalar_equal(value, candidate)), None)
        if match is None:
            return False
        available.pop(match)
    return True


def disposition_classes(text):
    normalized = re.sub(r"[\s_]+", "-", str(text).lower())
    return [name for name in LICENSED_DISPOSITIONS if name in normalized]


def read_recount_dispositions():
    relative = f"{ROUND_DIR}/recount/dispositions.md"
    text = read_text(relative)
    ledger_entries = {}
    round11_rows = {}
    ledger_section = text.split("## Round-11 drift-row dispositions", 1)[0]
    ledger_headers = list(re.finditer(
        r"(?m)^\s*\d+\.\s+\*\*Round\s+(\d+),\s+ledger entry\s+(\d+)\s+—\s+(.+?)\*\*",
        ledger_section))
    for index, header in enumerate(ledger_headers):
        end = (ledger_headers[index + 1].start()
               if index + 1 < len(ledger_headers) else len(ledger_section))
        round_number = int(header.group(1))
        entry_number = int(header.group(2))
        label = header.group(3)
        ledger_entries[entry_number] = {
            "round": round_number,
            "classes": disposition_classes(label),
            "label": label,
            "evidence": ledger_section[header.start():end].strip(),
        }
    drift_section = text.split("## Round-11 drift-row dispositions", 1)
    if len(drift_section) == 2:
        row_section = drift_section[1].split("## ", 1)[0]
        row_headers = list(re.finditer(
            r"(?m)^\s*-\s+\*\*Row\s+(\d+)\s+—\s+(.+?)\*\*",
            row_section))
        for index, header in enumerate(row_headers):
            end = (row_headers[index + 1].start()
                   if index + 1 < len(row_headers) else len(row_section))
            row_number = int(header.group(1))
            label = header.group(2)
            round11_rows[row_number] = {
                "classes": disposition_classes(label),
                "label": label,
                "evidence": row_section[header.start():end].strip(),
            }
    return {"path": relative, "text": text,
            "ledger_entries": ledger_entries, "round11_rows": round11_rows}


def measure_round11_f():
    failures = []
    receipts_dir = ROOT / "reports/round-11/recheck"
    receipts = []
    if receipts_dir.is_dir():
        for path in sorted(receipts_dir.glob("row-*.json")):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                failures.append(f"Unreadable round-11 receipt: {path.relative_to(ROOT)}")
                continue
            if isinstance(payload, dict):
                receipts.append(payload)
    ledger = read_json("reports/round-10/drift/ledger.json")
    ledger_rows = rows_from(ledger, ("rows", "entries", "ledger", "commands"))
    disposition_notes = read_recount_dispositions()
    if not disposition_notes["text"]:
        failures.append(f"Missing round-11 disposition evidence: {disposition_notes['path']}")
    stable, comparable, unreproducible, dispositioned = 0, 0, 0, 0
    licensed_dispositioned = 0
    unreproducible_by_construction = 0
    disposition_records = []
    row_issues = []
    for row in receipts:
        index = row.get("row")
        try:
            index = int(index)
        except (TypeError, ValueError):
            row_issues.append("receipt without integer ledger row")
            continue
        command = next((row.get(key) for key in
                        ("command_as_recorded", "command", "command_at_run",
                         "command_as_run", "executed_form")
                        if isinstance(row.get(key), str) and row.get(key).strip()), "")
        if index < 0 or index >= len(ledger_rows):
            row_issues.append(f"receipt row {index} is outside the round-10 ledger")
            continue
        prior = row.get("prior_hash")
        recorded_command = ledger_rows[index].get("command")
        if prior != ledger_rows[index].get("output_sha256"):
            row_issues.append(f"receipt row {index} prior hash differs from its ledger row")
        if not isinstance(recorded_command, str) or not command or \
                " ".join(command.strip().strip("`").split()) != \
                " ".join(recorded_command.strip().strip("`").split()):
            row_issues.append(f"receipt row {index} command differs from its ledger row")
        new_hash = row.get("new_hash")
        note = disposition_notes["round11_rows"].get(index, {})
        note_classes = note.get("classes", [])
        receipt_class, evidence, _ = receipt_disposition(row)
        primary_class = note_classes[0] if note_classes else receipt_class
        if isinstance(new_hash, str) and SHA256_RE.fullmatch(new_hash):
            comparable += 1
            hash_match = new_hash == prior
            if row.get("stable") is not hash_match:
                row_issues.append(f"receipt row {index} stable flag contradicts its hashes")
            if hash_match:
                stable += 1
            else:
                if primary_class and evidence:
                    dispositioned += 1
                    licensed_dispositioned += 1
                    disposition_records.append({
                        "row": index, "class": primary_class,
                        "documented_classes": note_classes,
                        "receipt_class": receipt_class,
                        "source": disposition_notes["path"] if note else "receipt",
                        "evidence": evidence,
                    })
                else:
                    row_issues.append(f"receipt row {index} hash mismatch has no licensed disposition")
        else:
            unreproducible += 1
            nonliteral = (row.get("drift_class") == "non-literal-command-text"
                          and row.get("verdict") == "pin-unreproducible-semantics-reproduced"
                          and row.get("semantics_reproduced") and row.get("evidence"))
            if nonliteral and primary_class and evidence:
                dispositioned += 1
                licensed_dispositioned += 1
                unreproducible_by_construction += 1
                disposition_records.append({
                    "row": index, "class": primary_class,
                    "documented_classes": note_classes,
                    "receipt_class": receipt_class,
                    "source": disposition_notes["path"] if note else "receipt",
                    "evidence": evidence,
                })
            else:
                row_issues.append(f"receipt row {index} has no named disposition")
    failures.extend(row_issues)
    ratio = stable / comparable if comparable else None
    total_rows = len(receipts)
    if (len(receipts), comparable, stable, unreproducible, dispositioned,
            licensed_dispositioned, unreproducible_by_construction) != \
            (192, 189, 147, 3, 45, 45, 3):
        failures.append(
            "Round-11 F recount does not reproduce 192 receipts, 189 comparable, "
            "147 stable, 3 unreproducible (including 3 non-literal commands), "
            "and 45 licensed dispositions"
        )
    old_validation = read_json("reports/round-11/validation.json") or {}
    old_f = ((old_validation.get("claims") or {}).get("F") or {}).get(
        "measurement", {})
    old_summary = read_json("reports/round-11/recheck/summary.json") or {}
    summary_rows = old_summary.get("rows_reckecked", old_summary.get("rows_rechecked"))
    try:
        summary_ratio = float(old_summary.get("stability"))
    except (TypeError, ValueError):
        summary_ratio = None
    reported_ratio = old_f.get("stability")
    if old_f.get("stable") != stable or old_f.get("ledger_rows") != len(ledger_rows):
        failures.append("Round-11 validation F stable/ledger row numbers differ from the independent recount")
    if not isinstance(reported_ratio, (int, float)) or abs(reported_ratio - (147 / 189)) > 0.0005:
        failures.append("Round-11 validation F stability does not reproduce 147/189")
    if summary_rows != 192 or old_summary.get("stable") != 147 or old_summary.get("unstable") != 45:
        failures.append("Round-11 recheck summary counts do not reproduce 147 stable and 45 dispositions out of 192")
    if summary_ratio is None or abs(summary_ratio - (147 / 192)) > 0.0005:
        failures.append("Round-11 summary all-receipt ratio does not reproduce 147/192")
    return {
        "passed": not failures,
        "failures": failures,
        "recount": {
            "value": {"receipts": total_rows, "comparable": comparable,
                      "stable": stable, "unreproducible": unreproducible,
                      "unreproducible_by_construction": unreproducible_by_construction,
                      "licensed_dispositioned": licensed_dispositioned,
                      "dispositioned": dispositioned,
                      "comparable_stability": ratio,
                      "all_receipt_stability": stable / total_rows
                      if total_rows else None},
            "command": "python3 reports/round-12/run-validation.py (independent computation over reports/round-11/recheck/row-*.json and reports/round-12/recount/dispositions.md)",
            "date": today(),
            "disposition_source": disposition_notes["path"],
            "disposition_rows": disposition_records,
        },
        "recorded": {
            "validation": {"value": {"stable": old_f.get("stable"),
                                       "ledger_rows": old_f.get("ledger_rows"),
                                       "stability": reported_ratio},
                            "command": "python3 reports/round-11/run-validation.py",
                            "date": old_validation.get("date") or "2026-10-17"},
            "summary": {"value": {"rows": summary_rows,
                                    "stable": old_summary.get("stable"),
                                    "dispositioned": old_summary.get("unstable"),
                                    "stability": summary_ratio},
                        "command": "python3 reports/round-11/run-validation.py (reports/round-11/recheck/summary.json)",
                        "date": old_summary.get("date", "2026-10-17")},
            "denominator_note": "The 0.778 value is 147/189 byte-comparable receipts; the summary's 147/192 value includes three no-hash, non-literal-command receipts whose output hashes are unreproducible by construction. The 45 dispositions comprise 42 hash-unstable receipts and those 3 no-hash receipts; all 45 receive environmental, legitimate-change, or defect classifications from reports/round-12/recount/dispositions.md. Both ratios are preserved, not substituted.",
        },
        "failures": failures,
    }


def measure_c():
    failures = []
    expected = command_sources()
    ledger_path = f"{ROUND_DIR}/recount/ledger.json"
    disposition_notes = read_recount_dispositions()
    missing_dependencies = []
    payload = read_json(ledger_path)
    if payload is None:
        missing_dependencies.append(ledger_path)
        failures.append(f"Missing or unparseable recount ledger: {ledger_path}")
    if not disposition_notes["text"]:
        missing_dependencies.append(disposition_notes["path"])
        failures.append(f"Missing recount disposition register: {disposition_notes['path']}")
    elif not DATE_RE.search(disposition_notes["text"]):
        failures.append(f"Recount disposition register lacks an ISO date: {disposition_notes['path']}")
    ledger_rows = rows_from(payload, ("commands", "rows", "entries", "ledger"))
    seen = {}
    evaluated = []
    for ledger_index, row in enumerate(ledger_rows):
        raw_command = row.get("command")
        command = normalized_command(raw_command)
        if not command and isinstance(raw_command, str):
            command = " ".join(raw_command.strip().split())
        round_number = row_round(row)
        if not command or round_number not in R8_R11:
            failures.append("Recount row is missing a command or source round 8-11")
            continue
        key = (round_number, command)
        seen.setdefault(key, []).append(row)
        recorded, observed = row.get("recorded"), row.get("observed")
        row_date = row.get("date", row.get("recount_date", row.get("observed_date")))
        if not isinstance(row_date, str) or not DATE_RE.search(row_date):
            failures.append(f"Recount row for {command} lacks an ISO date")
        raw_equal = recorded == observed
        status = str(row.get("status", row.get("verdict", row.get("result", "")))).lower()
        equal = recorded_values_present(recorded, observed) and status not in (
            "disposition", "mismatch")
        explicit_match = row.get("match") is True or status in ("match", "matched")
        disposition_evidence = None
        disposition_class = None
        ledger_disposition_class = None
        disposition_source = None
        disposition_note = disposition_notes["ledger_entries"].get(ledger_index + 1)
        if disposition_note and disposition_note.get("round") != round_number:
            failures.append(f"Disposition note round differs from ledger entry {ledger_index + 1}")
        if equal:
            if not explicit_match:
                failures.append(f"Recount values match but row is not marked match: {command}")
            if row.get("disposition") or status in ("disposition", "mismatch"):
                failures.append(f"Matching recount was given a discrepancy disposition: {command}")
        else:
            ledger_disposition_class, disposition_evidence, _ = recount_disposition_details(row)
            documented_classes = disposition_note.get("classes", []) if disposition_note else []
            disposition_class = documented_classes[0] if documented_classes else ledger_disposition_class
            if documented_classes:
                disposition_source = f"{disposition_notes['path']} ledger entry {ledger_index + 1}"
                if not disposition_evidence:
                    disposition_evidence = disposition_note.get("evidence")
            elif ledger_disposition_class:
                disposition_source = "ledger cause/disposition"
            if not disposition_class or not disposition_evidence:
                failures.append(f"Recount mismatch has no licensed cause and evidence: {command}")
            if explicit_match:
                failures.append(f"Recount mismatch is marked as a match: {command}")
        evaluated.append({"round": round_number, "command": command,
                          "date": row_date if isinstance(row_date, str) else None,
                          "receipt": row.get("receipt"),
                          "source_command": key in expected,
                          "recorded": recorded, "observed": observed,
                          "raw_equal": raw_equal, "match": equal,
                          "ledger_disposition_class": ledger_disposition_class,
                          "documented_disposition_classes": disposition_note.get("classes", []) if disposition_note else [],
                          "disposition_class": disposition_class,
                          "disposition_source": disposition_source,
                          "disposition_evidence": disposition_evidence})
    missing = [key for key in expected if key not in seen]
    for round_number, command in missing:
        sources = ", ".join(sorted(expected[(round_number, command)]))
        failures.append(f"No recount ledger row for {command} (round {round_number}; source {sources})")
    additional_commands = [
        {"round": round_number, "command": command}
        for round_number, command in sorted(seen) if (round_number, command) not in expected
    ]
    duplicate_commands = [
        {"round": round_number, "command": command, "rows": len(rows)}
        for (round_number, command), rows in sorted(seen.items()) if len(rows) > 1
    ]
    audited_files = []
    audited_commands = set()
    for path in sorted((ROOT / f"{ROUND_DIR}/recount").glob("**/*.md")):
        if not re.search(r"audit|auditor", path.name, re.I):
            continue
        text = read_text(path.relative_to(ROOT).as_posix())
        normalized_text = " ".join(text.split())
        matched = {command for _, command in expected
                   if " ".join(command.split()) in normalized_text}
        audited_commands.update(matched)
        audit_row = {"path": path.relative_to(ROOT).as_posix(),
                     "date": sorted(set(DATE_RE.findall(text))),
                     "commands_referenced": sorted(matched),
                     "reported_findings": sorted(set(re.findall(
                         r"(?i)\bFinding\s+([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\b",
                         text)))}
        audited_files.append(audit_row)
        if not audit_row["date"]:
            failures.append(f"Recount auditor file lacks a date: {audit_row['path']}")
        if re.search(r"(?i)\b(?:unresolved|undispositioned|unclassified)\s+(?:independent\s+)?mismatches?\b|\bmismatches?\s+(?:remain|are)\s+(?:unresolved|undispositioned|unclassified)\b", text):
            failures.append(f"Recount auditor leaves a mismatch unresolved: {audit_row['path']}")
    if len(audited_commands) < 8:
        failures.append("Independent recount auditors cover fewer than eight source commands")
    f_reproduction = measure_round11_f()
    failures.extend(f_reproduction["failures"])
    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "source_commands": [{"round": rnd, "command": command,
                                 "date": sorted({source.rsplit("@", 1)[-1]
                                                  for source in sources}),
                                 "sources": sorted(sources)}
                                for (rnd, command), sources in sorted(expected.items())],
            "source_command_total": {"value": len(expected),
                                     "command": "python3 reports/round-12/run-validation.py (extract claims.json claim counting_command and validation.json top-level counting_command plus command, command_line, argv, and recheck_command leaves in claims[*].measurement for reports/round-8..11)",
                                     "date": today()},
            "missing_source_commands": [
                {"round": round_number, "command": command,
                 "sources": sorted(expected[(round_number, command)])}
                for round_number, command in missing],
            "additional_ledger_commands": additional_commands,
            "duplicate_command_rows": duplicate_commands,
            "recounted_rows": {"value": len(evaluated),
                               "command": "python3 reports/round-12/run-validation.py (reports/round-12/recount/ledger.json)",
                               "date": today()},
            "matched_rows": {"value": sum(1 for row in evaluated if row["match"]),
                             "command": "python3 reports/round-12/run-validation.py (compare recorded and observed ledger values)",
                             "date": today()},
            "dispositioned_rows": {"value": sum(1 for row in evaluated if not row["match"] and row["disposition_class"]),
                                   "command": "python3 reports/round-12/run-validation.py (compare recorded and observed ledger values with the disposition register)",
                                   "date": today()},
            "disposition_register": {"path": disposition_notes["path"],
                                     "ledger_entries": len(disposition_notes["ledger_entries"]),
                                     "dated": bool(DATE_RE.search(disposition_notes["text"])),
                                     "command": "python3 reports/round-12/run-validation.py (parse one-based ledger-entry dispositions)",
                                     "date": today()},
            "rows": evaluated,
            "auditors": {"files": audited_files,
                         "independent_commands": {"value": len(audited_commands),
                                                  "command": "python3 reports/round-12/run-validation.py (audit markdown command coverage)",
                                                  "date": today()}},
            "round11_f_reproduction": f_reproduction,
        },
        "missing_dependencies": sorted(set(missing_dependencies)),
    }


def defect_rows(payload):
    return rows_from(payload, ("defects", "findings", "rows", "items", "entries", "queue"))


def measure_regressions():
    failures, runs = [], []
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    base_roots = ["tools/gates/frozen", "tools/gates/expected",
                  "reports/round-9/baselines"]
    gates = {path.stem for path in (ROOT / "tools/gates").glob("*.py")}
    round_dir = ROOT / f"{ROUND_DIR}/defects"
    if round_dir.is_dir():
        for path in sorted(round_dir.rglob("expected.json")):
            if path.parent.name in gates:
                relative = path.parent.parent.relative_to(ROOT).as_posix()
                if relative not in base_roots:
                    base_roots.append(relative)
    commands = [
        [sys.executable, "tools/check-gate-battery.py", "--selftest"],
        [sys.executable, "tools/check-gate-battery.py", *sum(
            (["--baselines-root", root] for root in base_roots), [])],
        [sys.executable, "tools/check-craft-exercise.py", "--selftest"],
        [sys.executable, "tools/check-craft-exercise.py",
         "examples/supplement-opencode-1/sound-change-vs-taboo.json"],
        [sys.executable, "tools/assemble-d2.py", "--selftest"],
        [sys.executable, "tools/assemble-d2.py", "--check"],
        [sys.executable, "tools/d2-typed-labels.py", "--selftest"],
        [sys.executable, "tools/assemble-culture-d3.py", "--selftest"],
        [sys.executable, "tools/assemble-culture-d3.py", "--check"],
        [sys.executable, "tools/check-evidence-coupling.py", "--selftest"],
    ]
    for argv in commands:
        result = command_run(argv, timeout=600)
        runs.append(result)
        if result.get("exit") != 0:
            failures.append(f"Regression command failed: {result['command']} (date {result['date']})")
    return {"passed": not failures, "failures": failures,
            "runs": runs, "date": today()}


def measure_o():
    failures, missing = [], []
    defects_dir = ROOT / f"{ROUND_DIR}/defects"
    sweeps = [f"{ROUND_DIR}/defects/sweep-r{n}.md" for n in R8_R11]
    for relative in sweeps:
        if not (ROOT / relative).is_file():
            missing.append(relative)
            failures.append(f"Missing conformance sweep: {relative}")
    ledger_rel = f"{ROUND_DIR}/defects/ledger.json"
    ledger = read_json(ledger_rel)
    if ledger is None:
        missing.append(ledger_rel)
        failures.append(f"Missing or unparseable consolidated defect ledger: {ledger_rel}")
    rows = defect_rows(ledger)
    serialized = json.dumps(ledger, ensure_ascii=False).lower() if ledger is not None else ""
    categories = {
        "out_of_lane_writes": len(re.findall(r"out[- ]of[- ]lane|out of province|out-of-scope write", serialized)) if ledger is not None else None,
        "filed_receipt_rewrite": int(bool(re.search(r"filed.{0,30}receipt.{0,30}(rewrite|rewrit|edit|chang)|receipt.{0,30}rewrite", serialized))) if ledger is not None else None,
        "availability_gaps": int(bool(re.search(r"availability.{0,30}(gap|gaps|fail|failure)|gap.{0,30}availability", serialized))) if ledger is not None else None,
    }
    if ledger is not None:
        if categories["out_of_lane_writes"] < 2:
            failures.append("Consolidated ledger does not enumerate both out-of-lane write defects")
        if not categories["filed_receipt_rewrite"]:
            failures.append("Consolidated ledger omits the filed-receipt rewrite defect")
        if not categories["availability_gaps"]:
            failures.append("Consolidated ledger omits the availability-gap defect")
    bounded = 0
    routed = 0
    for index, row in enumerate(rows):
        text = json.dumps(row, ensure_ascii=False).lower()
        status = str(row.get("status", row.get("disposition", row.get("decision", "")))).lower()
        if any(word in status for word in ("fixed", "repaired", "bounded-fix")):
            bounded_flag = row.get("bounded") is True or "bounded" in status or bool(row.get("fix_scope"))
            before = row.get("before", row.get("control_before", row.get("pre_fix")))
            after = row.get("after", row.get("control_after", row.get("post_fix")))
            control = row.get("control", row.get("control_evidence", row.get("test", row.get("evidence"))))
            if not bounded_flag or before is None or after is None or not control:
                failures.append(f"Fixed defect row {index} lacks bounded scope and before/after control evidence")
            else:
                bounded += 1
        else:
            owner = row.get("owner", row.get("route_owner", ""))
            note = row.get("owner_note", row.get("note", row.get("reason", "")))
            if not re.search(r"round[- ]?14|integrate", text) or not owner or not note:
                failures.append(f"Unfixed defect row {index} is not routed to round 14 with an owner note")
            else:
                routed += 1
    if not rows:
        failures.append("Consolidated defect ledger has no finding rows")
    if rows and bounded == 0:
        failures.append("No bounded fix has demonstrated before/after controls")
    routed_rel = f"{ROUND_DIR}/defects/routed.md"
    routed_text = read_text(routed_rel)
    if not routed_text:
        missing.append(routed_rel)
        failures.append(f"Missing round-14 routing note: {routed_rel}")
    elif not re.search(r"round[- ]?14|integrate", routed_text, re.I) or \
            not re.search(r"owner", routed_text, re.I):
        failures.append("Round-14 routing note lacks an owner or destination")
    route_section = routed_text.split("## Open items — round 14", 1)
    open_routes = (route_section[1].split("## Findings not routed as open", 1)[0]
                   if len(route_section) == 2 else "")
    route_blocks = re.findall(r"(?ms)^### .+?(?=^### |^## |\Z)", open_routes)
    routed_items_with_owners = sum(
        bool(re.search(r"(?im)^\*\*Round-14 owner:\*\*\s*\S", block))
        for block in route_blocks)
    if route_blocks and routed_items_with_owners != len(route_blocks):
        failures.append("Round-14 routing note has an open item without an owner note")
    fix_relatives = [f"{ROUND_DIR}/defects/fix-{number:02d}.md"
                     for number in range(9, 17)]
    fix_receipts = []
    for relative in fix_relatives:
        path = ROOT / relative
        if not path.is_file():
            missing.append(relative)
            failures.append(f"Missing assigned defect disposition: {relative}")
            continue
        text = read_text(relative)
        if re.search(r"fixed-with-control", text, re.I):
            disposition = "fixed-with-control"
            before = bool(re.search(r"(?im)^## Before controls?\s*$", text))
            after = bool(re.search(r"(?im)^## After controls?\s*$", text))
            if not before or not after:
                failures.append(f"Fixed disposition lacks before/after controls: {relative}")
            finding_ids = re.findall(
                r"(?i)\bfindings?\s+([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)",
                next((line for line in text.splitlines()
                      if line.lower().startswith("- sweep source:")), ""))
            for finding_id in finding_ids:
                matching_blocks = [block for block in route_blocks
                                   if re.search(rf"\b{re.escape(finding_id)}\b", block)]
                if any(re.search(r"(?i)\*\*Status:\*\*[^.\n]*\bopen\b|pending\s+round[- ]?14",
                                 block) for block in matching_blocks):
                    failures.append(
                        f"Fix receipt {relative} says fixed-with-control but routed.md keeps {finding_id} open")
            fix_receipts.append({"path": relative, "disposition": disposition,
                                 "before_control": before, "after_control": after,
                                 "finding_ids": finding_ids})
        elif re.search(r"not fixed;\s*route to round[- ]?14", text, re.I):
            fix_receipts.append({"path": relative, "disposition": "routed-to-round-14",
                                 "before_control": False, "after_control": False,
                                 "finding_ids": []})
        else:
            failures.append(f"Defect disposition is not explicit: {relative}")
            fix_receipts.append({"path": relative, "disposition": "unclassified"})
    receipt_bounded = sum(1 for item in fix_receipts
                          if item["disposition"] == "fixed-with-control"
                          and item.get("before_control") and item.get("after_control"))
    regressions = measure_regressions()
    failures.extend(regressions["failures"])
    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "sweeps": sweeps,
            "defect_ledger": ledger_rel,
            "finding_rows": {"value": len(rows), "ledger_present": ledger is not None,
                             "command": "python3 reports/round-12/run-validation.py (reports/round-12/defects/ledger.json)",
                             "date": today()},
            "known_defect_categories": {key: {"value": value,
                                               "command": "python3 reports/round-12/run-validation.py (cross-round conformance ledger review)",
                                               "date": today()}
                                         for key, value in categories.items()},
            "bounded_fixes": {"value": bounded if ledger is not None else None,
                              "fix_receipt_controls": {"value": receipt_bounded,
                                                       "command": "python3 reports/round-12/run-validation.py (reports/round-12/defects/fix-09.md through fix-16.md)",
                                                       "date": today()},
                              "command": "python3 reports/round-12/run-validation.py (before/after control evidence in defect ledger)",
                              "date": today()},
            "round14_routes": {"value": routed if ledger is not None else None,
                               "routing_note_items": len(route_blocks),
                               "items_with_owners": routed_items_with_owners,
                               "command": "python3 reports/round-12/run-validation.py (owner-routed defect ledger rows and routed.md)",
                               "date": today()},
            "fix_receipts": fix_receipts,
            "regressions": regressions,
        },
        "missing_dependencies": sorted(set(missing)),
    }


def entry_changes():
    claims = read_json(CLAIMS) or {}
    baseline = claims.get("baseline_revision")
    r11_claims = read_json("reports/round-11/claims.json") or {}
    r11_baseline = r11_claims.get("baseline_revision")
    paths = set()
    r10 = read_json("reports/round-10/validation.json") or {}
    c_measurement = (((r10.get("claims") or {}).get("C") or {}).get(
        "measurement") or {})
    origins = c_measurement.get("entry_origins", {})
    if isinstance(origins, dict):
        paths.update(origins)
    git_commands = []
    for before, after in ((r11_baseline, baseline), (baseline, None)):
        if not before:
            continue
        args = ["diff", "--name-status", before]
        if after:
            args.append(after)
        args.extend(("--", "corpus/knowledge"))
        output = git_output(*args)
        command = "git " + " ".join(args)
        git_commands.append({"command": command, "date": today(),
                             "exit": 0 if output is not None else None})
        if output:
            for line in output.splitlines():
                bits = line.split("\t")
                relative = bits[-1] if len(bits) > 1 else ""
                if relative.startswith("corpus/knowledge/") and relative.endswith(".md"):
                    paths.add(relative)
    untracked = git_output("ls-files", "--others", "--exclude-standard", "--", "corpus/knowledge")
    git_commands.append({"command": "git ls-files --others --exclude-standard -- corpus/knowledge",
                         "date": today(), "exit": 0 if untracked is not None else None})
    if untracked:
        paths.update(line.strip() for line in untracked.splitlines()
                     if line.strip().startswith("corpus/knowledge/") and
                     line.strip().endswith(".md"))
    return sorted(paths), git_commands


def measure_a():
    failures, missing = [], []
    adjacency_dir = ROOT / f"{ROUND_DIR}/adjacency"
    ledger_rel = f"{ROUND_DIR}/adjacency/ledger.json"
    ledger = read_json(ledger_rel)
    if ledger is None:
        missing.append(ledger_rel)
        failures.append(f"Missing or unparseable adjacency ledger: {ledger_rel}")
    rows = rows_from(ledger, ("entries", "rows", "checks", "items", "audits"))
    ledger_text = json.dumps(ledger, ensure_ascii=False).lower() if ledger is not None else ""
    required_entries, discovery_commands = entry_changes()
    for relative in required_entries:
        if relative not in ledger_text:
            failures.append(f"Adjacency ledger has no row for new/changed corpus entry: {relative}")
    if not required_entries:
        failures.append("No round-10 or round-11/12 corpus-entry inventory could be derived")
    if not rows:
        failures.append("Adjacency ledger contains no structured entry rows")
    checked_rows = []
    unfiled_bleed = 0
    for row in rows:
        text = json.dumps(row, ensure_ascii=False).lower()
        entry = row.get("path", row.get("entry", row.get("file", row.get("source", ""))))
        state = str(row.get("status", row.get("verdict", row.get("result", row.get("bleed", ""))))).lower()
        is_bleed = row.get("bleed") is True or row.get("out_of_province") is True or \
            bool(re.search(r"(?<!no[- ])\b(bleed|out[- ]of[- ]province|canon claim|rights ruling|game mechanics)\b", state))
        filed = row.get("filed_path", row.get("finding_path", row.get("evidence_path", row.get("report", ""))))
        candidate = str(filed).strip().strip("`")
        bleed_filed = bool(is_bleed and candidate and (ROOT / candidate).exists())
        if is_bleed and not bleed_filed:
            unfiled_bleed += 1
            failures.append(f"Adjacency bleed finding for {entry or 'entry'} is not filed at an existing report path")
        checked_rows.append({"entry": entry, "status": state,
                             "out_of_province": bool(is_bleed),
                             "bleed_filed": bleed_filed})
    unfiled_declaration = re.search(
        r"unfiled[_ -]?bleed\s*[:=]\s*([1-9]\d*|true)", ledger_text)
    if unfiled_declaration:
        failures.append("Adjacency ledger declares unfiled bleed")
        declared = unfiled_declaration.group(1)
        unfiled_bleed = max(unfiled_bleed,
                            int(declared) if declared.isdigit() else 1)
    if re.search(r"unreported[_ -]?(?:bleed|finding)\s*[:=]\s*(?:[1-9]\d*|true)", ledger_text):
        failures.append("Adjacency ledger declares an unreported finding")
    handoff_texts = []
    for path in sorted(adjacency_dir.glob("**/*.md")) if adjacency_dir.is_dir() else []:
        handoff_texts.append((path.relative_to(ROOT).as_posix(), read_text(
            path.relative_to(ROOT).as_posix())))
    handoff_report = next(((relative, text) for relative, text in handoff_texts
                           if "worldbible-integration-contract" in text.lower()
                           and "round-11/handoff" in text.lower()), None)
    if handoff_report is None:
        failures.append("Adjacency handoff audit does not compare the contract with the round-11 exercise packet")
    else:
        relative, text = handoff_report
        if not re.search(r"lore", text, re.I):
            failures.append(f"Handoff audit lacks lore-boundary notes: {relative}")
        contract = read_text("corpus/knowledge/synthesis/worldbible-integration-contract.md")
        expected = read_json("reports/round-11/handoff/expected.json") or {}
        contract_fields = set()
        in_envelope = False
        for line in contract.splitlines():
            if line.startswith("## 4."):
                in_envelope = True
                continue
            if in_envelope and line.startswith("## "):
                break
            if in_envelope and line.startswith("|"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) < 2:
                    continue
                for field in re.findall(r"`([^`]+)`", cells[0]):
                    contract_fields.update(token.strip() for token in field.split(",")
                                           if token.strip())
        packet_fields = set((expected.get("field_digests") or {}).keys())
        if contract_fields != packet_fields or not packet_fields:
            failures.append("Round-11 packet fields differ from the contract's declared handoff envelope")
    province_rel = f"{ROUND_DIR}/adjacency/province.md"
    province_text = read_text(province_rel)
    if not province_text:
        missing.append(province_rel)
        failures.append(f"Missing PROVINCE accuracy review: {province_rel}")
    else:
        if "province.md" not in province_text.lower():
            failures.append("PROVINCE accuracy review does not cite PROVINCE.md")
        accurate = bool(re.search(r"(?i)\baccurate\b|\bstill accurate\b|\bno drift\b", province_text))
        finding_text = (province_text.split("## Finding", 1)[1].split("\n## ", 1)[0]
                        if "## Finding" in province_text else province_text)
        correction = bool(re.search(
            r"(?i)\b(?:corrected|drift (?:was )?found|correction (?:was )?(?:applied|made|filed|logged|recorded|proposed|required|needed|recommended))\b",
            finding_text))
        no_correction = bool(re.search(
            r"(?i)\bno\b[^.\n]{0,100}\b(?:province-related )?(?:scope )?drift\b|\bno correction\b",
            finding_text))
        if no_correction:
            correction = False
        if not accurate and not correction:
            failures.append("PROVINCE review has no accuracy verdict")
        if correction and not re.search(r"(?i)LOG\.md|reports/round-12", province_text):
            failures.append("PROVINCE correction review does not cite a logged correction entry")
        if not re.search(r"(?i)round[- ]?8|round[- ]?9|round[- ]?10|round[- ]?11", province_text):
            failures.append("PROVINCE review does not cover the four audited rounds")
    result = {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "required_entries": {"value": required_entries,
                                 "command": "python3 reports/round-12/run-validation.py (round-10 entry origins plus round-11/12 corpus diff)",
                                 "date": today(), "discovery_commands": discovery_commands},
            "entry_rows": {"value": len(rows),
                            "command": "python3 reports/round-12/run-validation.py (reports/round-12/adjacency/ledger.json)",
                            "date": today()},
            "checked_rows": checked_rows,
            "handoff_contract_fields": {"contract": sorted(contract_fields) if handoff_report else [],
                                         "packet": sorted(packet_fields) if handoff_report else [],
                                         "command": "python3 reports/round-12/run-validation.py (parse contract §4 and reports/round-11/handoff/expected.json)",
                                         "date": today()},
            "handoff_audit": handoff_report[0] if handoff_report else None,
            "province_review": province_rel if province_text else None,
            "unfiled_bleed": {"value": unfiled_bleed if ledger is not None else None,
                               "ledger_present": ledger is not None,
                               "rows_evaluated": len(rows),
                               "command": "python3 reports/round-12/run-validation.py (count unfiled flagged rows and ledger declaration)",
                               "date": today()},
        },
        "missing_dependencies": sorted(set(missing)),
    }
    return result


def main():
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    filed_paths = [f"reports/round-{n}" for n in R8_R11]
    status_before = git_status(filed_paths)
    results = {"C": measure_c(), "O": measure_o(), "A": measure_a()}
    status_after = git_status(filed_paths)
    if status_before != status_after:
        results["A"]["failures"].append("Filed rounds 8-11 worktree status changed during validation")
        results["A"]["passed"] = False
    passed = all(result["passed"] for result in results.values())
    claims = read_json(CLAIMS) or {}
    targets = read_json(TARGETS) or {}
    missing = sorted({item for result in results.values()
                      for item in result.get("missing_dependencies", [])})
    receipt = {
        "round": 12,
        "runner": RUNNER,
        "runner_sha256": digest(RUNNER),
        "counting_command": "python3 reports/round-12/run-validation.py",
        "date": today(),
        "baseline_revision": claims.get("baseline_revision"),
        "targets_date": targets.get("date"),
        "claims_declared": {claim.get("id"): claim.get("axis")
                            for claim in claims.get("claims", [])
                            if isinstance(claim, dict)},
        "acceptance_checks_passed": passed,
        "claims": results,
        "failures": [f"claim {claim_id}: {failure}"
                     for claim_id in ("C", "O", "A")
                     for failure in results[claim_id]["failures"]],
        "missing_dependencies": missing,
        "filed_rounds_status": {"value_before": status_before,
                                "value_after": status_after,
                                "command": "git status --short -- reports/round-8 reports/round-9 reports/round-10 reports/round-11",
                                "date": today()},
        "limits": [
            "Round-8 through round-11 filed artifacts are read-only. This runner consumes recount receipts and does not invoke historical round runners, which would rewrite their validation.json files.",
            "C command discovery reads each prior claims.json claim counting_command (splitting semicolon-separated invocations), plus validation.json top-level counting_command and command, command_line, argv, or recheck_command leaves under claims[*].measurement. Each unique source-round/normalized-command is required once; every invocation site is listed as a source.",
            "O ledger-derived defect categories, fix counts and routed-row counts are unavailable when the consolidated ledger is absent. Individual fix receipts and the owner-routed markdown are reported separately and do not substitute for that ledger.",
            "A content/scope verdict is evidence-backed by the adjacency auditors, not decided by this validator. It checks entry coverage, source paths, declared handoff field names, the province verdict and flagged-issue filing; a missing adjacency ledger leaves zero-bleed unverified. It does not adjudicate historical truth, legal rights or canon.",
            "Regression commands are executed in read-only check/selftest modes with TMPDIR set to this repository's .scratch and bytecode generation disabled. No git commit or push is performed.",
        ],
    }
    out = ROOT / OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              ensure_ascii=False) + "\n", encoding="utf-8")
    for claim_id, result in results.items():
        print(f"claim {claim_id}: {'PASS' if result['passed'] else 'FAIL'}")
    print(f"acceptance_checks_passed: {passed}")
    if missing:
        print("missing_dependencies: " + ", ".join(missing))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
