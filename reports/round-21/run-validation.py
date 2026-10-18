#!/usr/bin/env python3
from __future__ import annotations

import collections
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-21"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
ROUNDS = (17, 18, 19, 20)
LOCKED_ROUNDS = tuple(range(8, 21))
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
LICENSED_DISPOSITIONS = ("environmental", "legitimate-change", "defect")
COMMAND_KEYS = {"command", "command_line", "argv", "recheck_command"}


def today():
    return dt.date.today().isoformat()


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    try:
        return sha_bytes(Path(path).read_bytes())
    except OSError:
        return None


def safe_path(relative):
    candidate = Path(str(relative))
    if candidate.is_absolute() or ".." in candidate.parts or ".git" in candidate.parts:
        raise ValueError(f"not an in-repository path: {relative}")
    resolved = (ROOT / candidate).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError(f"path escapes repository: {relative}")
    return resolved


def read_json(relative):
    try:
        return json.loads(safe_path(relative).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return None


def read_text(relative):
    try:
        return safe_path(relative).read_text(encoding="utf-8", errors="replace")
    except (OSError, ValueError):
        return ""


def git_output(*args, cwd=ROOT, timeout=60):
    try:
        proc = subprocess.run(["git", *map(str, args)], cwd=cwd,
                              capture_output=True, timeout=timeout,
                              env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"})
    except (OSError, subprocess.SubprocessError):
        return None
    return proc.stdout if proc.returncode == 0 else None


def git_status(paths):
    output = git_output("status", "--short", "--", *paths)
    return output.decode("utf-8", "replace").strip() if output is not None else None


def command_text(value):
    if isinstance(value, (list, tuple)):
        parts = [str(item) for item in value]
        if not parts:
            return None
        text = shlex.join(parts)
    elif isinstance(value, str):
        text = " ".join(value.split()).strip().strip("`")
    else:
        return None
    text = re.sub(r"(\.py)\s+[\"']?\(.*\)[\"']?$", r"\1", text)
    try:
        parts = shlex.split(text)
    except ValueError:
        return None
    if not parts:
        return None
    if parts[0] in (sys.executable, "python", "python3"):
        if parts[0] == sys.executable:
            parts[0] = "python3"
        return shlex.join(parts)
    if parts[0].endswith(".py"):
        return shlex.join(["python3", *parts])
    if parts[0] in {"bash", "sh", "git", "ls", "find", "sha256sum", "shasum",
                    "diff", "cmp", "wc", "grep", "rg", "stat", "date", "test",
                    "curl", "wget", "command"}:
        return shlex.join(parts)
    if parts[0] == "cd" and "&&" in parts:
        split_at = parts.index("&&")
        if split_at >= 2 and split_at + 1 < len(parts):
            return shlex.join(parts[:split_at]) + " && " + shlex.join(parts[split_at + 1:])
    return None


def command_segments(value):
    if isinstance(value, (list, tuple)):
        return [value]
    if not isinstance(value, str):
        return []
    if ";" not in value:
        return [value]
    try:
        lexer = shlex.shlex(value, posix=True, punctuation_chars=";")
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        return []
    result, current = [], []
    for token in tokens:
        if token == ";":
            if current:
                result.append(current)
                current = []
        else:
            current.append(token)
    if current:
        result.append(current)
    return result


def command_sources():
    found = collections.defaultdict(list)
    for number in ROUNDS:
        validation_path = f"reports/round-{number}/validation.json"
        claims_path = f"reports/round-{number}/claims.json"
        validation = read_json(validation_path) or {}
        claims = read_json(claims_path) or {}
        source_date = validation.get("date") or claims.get("date") or "unknown"

        def add(value, source, date):
            for segment_index, segment in enumerate(command_segments(value)):
                normalized = command_text(segment)
                if normalized:
                    found[(number, normalized)].append({
                        "source": f"{source}[{segment_index}]",
                        "source_date": date,
                    })

        add(validation.get("counting_command"), f"{validation_path}:counting_command", source_date)
        add(validation.get("rerun_at_close"), f"{validation_path}:rerun_at_close", source_date)
        for claim in claims.get("claims", []) if isinstance(claims.get("claims"), list) else []:
            if isinstance(claim, dict):
                add(claim.get("counting_command"),
                    f"{claims_path}:claims.{claim.get('id', 'unknown')}.counting_command",
                    source_date)

        def visit(value, pointer):
            if isinstance(value, dict):
                if "command" in value:
                    add(value.get("command"), f"{validation_path}:{pointer}.command",
                        value.get("date", source_date))
                for key in ("command_line", "argv", "recheck_command"):
                    if key in value:
                        add(value.get(key), f"{validation_path}:{pointer}.{key}",
                            value.get("date", source_date))
                for key, child in value.items():
                    visit(child, f"{pointer}.{key}")
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    visit(child, f"{pointer}[{index}]")

        visit(validation, "root")
    return {key: rows for key, rows in sorted(found.items())}


def rows_from(payload, keys):
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if isinstance(payload, dict):
        for key in keys:
            value = payload.get(key)
            if isinstance(value, list):
                return [row for row in value if isinstance(row, dict)]
        for key in keys:
            value = payload.get(key)
            if isinstance(value, dict):
                return [row for row in value.values() if isinstance(row, dict)]
    return []


def row_round(row):
    value = row.get("round", row.get("source_round", row.get("round_number")))
    try:
        return int(value)
    except (TypeError, ValueError):
        match = re.search(r"round[- ]?(17|18|19|20)\b", json.dumps(row), re.I)
        return int(match.group(1)) if match else None


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
        return abs(left - right) <= 0.0001 * max(abs(left), abs(right), 1)
    return type(left) is type(right) and left == right


def recorded_values_present(recorded, observed):
    if recorded == observed:
        return True
    wanted, available = scalar_values(recorded), scalar_values(observed)
    if not wanted:
        return recorded == observed
    for value in wanted:
        match = next((i for i, candidate in enumerate(available)
                      if scalar_equal(value, candidate)), None)
        if match is None:
            return False
        available.pop(match)
    return True


def disposition_details(row):
    explicit = row.get("disposition")
    if isinstance(explicit, dict):
        kind = explicit.get("class", explicit.get("type", explicit.get("cause_class", "")))
        evidence = explicit.get("evidence", explicit.get("reason", explicit.get("cause", "")))
    else:
        kind = " ".join(str(row.get(key, "")) for key in
                         ("disposition_class", "cause_class", "drift_class", "cause"))
        evidence = " ".join(str(row.get(key, "")) for key in
                             ("evidence", "reason", "note", "drift_evidence"))
        if isinstance(explicit, str) and explicit.strip().lower() not in (
                "match", "matched", "mismatch", "disposition"):
            kind += " " + explicit
    normalized = re.sub(r"[\s_]+", "-", f"{kind} {evidence}".lower())
    cause = next((item for item in LICENSED_DISPOSITIONS if item in normalized), None)
    return cause, evidence.strip()


def explicit_match(row):
    status = str(row.get("status", row.get("verdict", row.get("result", "")))).lower()
    return row.get("match") is True or status in ("match", "matched", "reproduced")


def audit_recount():
    failures, missing = [], []
    sources = command_sources()
    ledger_path = f"{ROUND_DIR}/recount/ledger.json"
    payload = read_json(ledger_path)
    if payload is None:
        missing.append(ledger_path)
        failures.append(f"Missing or unparseable recount ledger: {ledger_path}")
    ledger_rows = rows_from(payload, ("commands", "rows", "entries", "ledger"))
    by_key = collections.defaultdict(list)
    evaluated = []
    for index, row in enumerate(ledger_rows):
        raw_command = row.get("command")
        command = command_text(raw_command)
        number = row_round(row)
        if not command or number not in ROUNDS:
            failures.append(f"Recount row {index} has no normalized command or source round 17-20")
            continue
        key = (number, command)
        by_key[key].append(row)
        date = row.get("date", row.get("recount_date", row.get("observed_date")))
        if not isinstance(date, str) or not DATE_RE.search(date):
            failures.append(f"Recount row {index} lacks an ISO recount date: {command}")
        if "recorded" not in row or "observed" not in row:
            failures.append(f"Recount row {index} lacks recorded/observed values: {command}")
            continue
        recorded, observed = row.get("recorded"), row.get("observed")
        equal = recorded_values_present(recorded, observed)
        matched = explicit_match(row)
        status = str(row.get("status", row.get("verdict", row.get("result", "")))).lower()
        cause, evidence = disposition_details(row)
        if equal and not matched:
            failures.append(f"Recount values match but the row is not marked match: {command}")
        elif not equal and (matched or not cause or not evidence):
            failures.append(f"Recount mismatch lacks a licensed disposition and evidence: {command}")
        if equal and (row.get("disposition") or status in ("mismatch", "disposition")):
            failures.append(f"Matching recount is marked discrepant: {command}")
        evaluated.append({"round": number, "command": command, "date": date,
                          "match": equal, "disposition": cause,
                          "source_count": len(sources.get(key, []))})
    missing_commands = [key for key in sources if key not in by_key]
    for number, command in missing_commands:
        failures.append(f"No recount row for source command in round {number}: {command}")
    extra = [{"round": number, "command": command}
             for number, command in by_key if (number, command) not in sources]
    duplicates = [{"round": number, "command": command, "rows": len(rows)}
                  for (number, command), rows in by_key.items() if len(rows) > 1]
    for row in extra:
        failures.append(f"Recount ledger has an unrecorded source command: {row['command']}")
    for row in duplicates:
        failures.append(f"Duplicate recount rows for {row['command']}")

    disposition_path = f"{ROUND_DIR}/recount/dispositions.md"
    disposition_text = read_text(disposition_path)
    if not disposition_text:
        missing.append(disposition_path)
        failures.append(f"Missing recount disposition evidence: {disposition_path}")
    elif not DATE_RE.search(disposition_text):
        failures.append(f"Recount disposition register lacks an ISO date: {disposition_path}")

    audit_files, audit_commands = [], set()
    recount_dir = ROOT / f"{ROUND_DIR}/recount"
    if recount_dir.is_dir():
        for path in sorted(recount_dir.rglob("*.md")):
            if not re.search(r"audit|auditor", path.name, re.I):
                continue
            relative = path.relative_to(ROOT).as_posix()
            text = read_text(relative)
            covered = [command for _, command in sources if command in text]
            audit_commands.update(covered)
            row = {"path": relative, "dates": sorted(set(DATE_RE.findall(text))),
                   "commands_referenced": sorted(set(covered))}
            audit_files.append(row)
            if not row["dates"]:
                failures.append(f"Recount auditor has no date: {relative}")
            if re.search(r"(?i)\b(unresolved|undispositioned|unclassified)\s+mismatches?\b|"
                         r"\bmismatches?\s+(?:remain|are)\s+(?:unresolved|undispositioned|unclassified)", text):
                failures.append(f"Recount auditor leaves a mismatch unresolved: {relative}")
    if not audit_files:
        missing.append(f"{ROUND_DIR}/recount/*audit*.md")
        failures.append("No filed independent recount auditor report found")
    if len(audit_commands) < min(8, len(sources)):
        failures.append(f"Independent recount auditors cover only {len(audit_commands)} source commands")
    for number in ROUNDS:
        if not any(re.search(rf"round[- ]?{number}\b", text, re.I)
                   for item in audit_files for text in [read_text(item["path"])]):
            failures.append(f"No independent recount auditor identifies round {number}")

    historical_runs, historical_discrepancies = run_historical_validators()
    for item in historical_runs:
        recorded = item.get("recorded_acceptance")
        observed = item.get("observed_acceptance")
        if not item.get("receipt_updated"):
            failures.append(f"Isolated round-{item['round']} validator did not update its scratch-clone receipt")
        if item.get("receipt_refresh_required") and not item.get("receipt_refresh_granted"):
            failures.append(f"Isolated round-{item['round']} committed receipt refresh was not explicitly granted")
        if item.get("exit") is None or not isinstance(recorded, bool) or not isinstance(observed, bool):
            failures.append(f"Isolated round-{item['round']} validator rerun did not produce a comparable acceptance receipt")
            continue
        if recorded != observed:
            historical_discrepancies.append({"round": item["round"],
                                             "recorded": recorded,
                                             "observed": observed})
            key = (item["round"], f"python3 reports/round-{item['round']}/run-validation.py")
            row = next(iter(by_key.get(key, [])), None)
            cause, evidence = disposition_details(row or {})
            if not cause or not evidence:
                failures.append(f"Round-{item['round']} acceptance changed without a licensed recount disposition")

    repair = reproduce_r18_repair()
    failures.extend(repair["failures"])
    measured_commands = len(evaluated)
    matches = sum(row["match"] for row in evaluated)
    dispositioned = sum(bool(row["disposition"]) for row in evaluated)
    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "source_commands": [{"round": number, "command": command,
                                 "sources": rows}
                                for (number, command), rows in sources.items()],
            "source_command_total": {"value": len(sources),
                                     "command": "python3 reports/round-21/run-validation.py (discover counting_command and command/argv leaves in rounds 17-20 claims and validation measurements)",
                                     "date": today()},
            "recounted_rows": {"value": measured_commands,
                               "command": "python3 reports/round-21/run-validation.py (reports/round-21/recount/ledger.json)",
                               "date": today()},
            "matched_rows": {"value": matches,
                             "command": "python3 reports/round-21/run-validation.py (compare independent recorded and observed recount values)",
                             "date": today()},
            "dispositioned_rows": {"value": dispositioned,
                                   "command": "python3 reports/round-21/run-validation.py (validate licensed cause and evidence for recount differences)",
                                   "date": today()},
            "missing_source_commands": [{"round": number, "command": command}
                                        for number, command in missing_commands],
            "additional_ledger_commands": extra,
            "duplicate_command_rows": duplicates,
            "auditors": {"files": audit_files,
                         "independently_referenced_commands": {"value": len(audit_commands),
                             "command": "python3 reports/round-21/run-validation.py (independent auditor markdown coverage)",
                             "date": today()}},
            "historical_validator_reruns": historical_runs,
            "historical_acceptance_discrepancies": historical_discrepancies,
            "round18_repair_reproduction": repair["measurement"],
        },
        "missing_dependencies": sorted(set(missing)),
    }


def make_clone(name, revision="HEAD"):
    base = ROOT / ".scratch" / "round-21" / name
    if base.exists():
        shutil.rmtree(base)
    base.parent.mkdir(parents=True, exist_ok=True)
    command = ["git", "clone", "--shared", "--no-checkout", "--quiet", str(ROOT), str(base)]
    env = {**os.environ, "TMPDIR": str(ROOT / ".scratch" / "round-21" / "tmp"),
           "GIT_OPTIONAL_LOCKS": "0", "PYTHONDONTWRITEBYTECODE": "1"}
    Path(env["TMPDIR"]).mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, timeout=300, env=env)
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace")[-600:])
    checkout = subprocess.run(["git", "checkout", "--force", "--detach", revision],
                              cwd=base, capture_output=True, timeout=120, env=env)
    if checkout.returncode:
        raise RuntimeError(checkout.stderr.decode("utf-8", "replace")[-600:])
    return base


def clone_environment(clone, label):
    temp = ROOT / ".scratch" / "round-21" / "tmp" / label
    temp.mkdir(parents=True, exist_ok=True)
    (clone / ".scratch").mkdir(parents=True, exist_ok=True)
    return {**os.environ, "TMPDIR": str(temp), "PYTHONDONTWRITEBYTECODE": "1",
            "GIT_OPTIONAL_LOCKS": "0"}


def run_historical_validator(number):
    result = {"round": number, "command": f"python3 reports/round-{number}/run-validation.py",
              "date": today(), "clone": f".scratch/round-21/validator-r{number}",
              "receipt_refresh_required": number in (17, 18, 20)}
    try:
        clone = make_clone(f"validator-r{number}")
        if number == 18:
            ignored_log = "tools/gates/frozen/round-11/typed-pipeline/run.log"
            expected_log_sha = "9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606"
            source_log = ROOT / ignored_log
            if digest(source_log) != expected_log_sha:
                raise RuntimeError("round-11 ignored R18 input is missing or has an unexpected digest")
            clone_log = clone / ignored_log
            clone_log.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_log, clone_log)
            if digest(clone_log) != expected_log_sha:
                raise RuntimeError("round-11 ignored R18 input copy failed digest verification")
            result["ignored_r18_input"] = {
                "source": ignored_log,
                "clone": f"{result['clone']}/{ignored_log}",
                "sha256": expected_log_sha,
            }
            runner = clone / "reports/round-18/run-validation.py"
            text = runner.read_text(encoding="utf-8")
            old = ('OUTSIDE_TMP_CANDIDATES = (Path("/var/tmp/kotodama-r18-validation"),\n'
                   '                          Path("/tmp/kotodama-r18-validation"))')
            safe_tmp = ROOT / ".scratch" / "round-21" / "r18-outside-clone"
            replacement = f'OUTSIDE_TMP_CANDIDATES = (Path({str(safe_tmp)!r}),)'
            if old not in text:
                raise RuntimeError("could not redirect round-18 external temp candidate in isolated clone")
            runner.write_text(text.replace(old, replacement, 1), encoding="utf-8")
        env = clone_environment(clone, f"validator-r{number}")
        env["REFRESH_RECEIPTS"] = "1"
        receipt_path = clone / f"reports/round-{number}/validation.json"
        try:
            receipt_mtime_before = receipt_path.stat().st_mtime_ns
        except OSError:
            receipt_mtime_before = None
        receipt_sha_before = digest(receipt_path)
        proc = subprocess.run([sys.executable, f"reports/round-{number}/run-validation.py"],
                              cwd=clone, capture_output=True, timeout=900, env=env)
        try:
            receipt_mtime_after = receipt_path.stat().st_mtime_ns
        except OSError:
            receipt_mtime_after = None
        try:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            receipt = {}
        original = read_json(f"reports/round-{number}/validation.json") or {}
        result.update({"exit": proc.returncode, "stdout_tail": proc.stdout.decode("utf-8", "replace")[-500:],
                       "stderr_tail": proc.stderr.decode("utf-8", "replace")[-500:],
                       "receipt_sha256_before": receipt_sha_before,
                       "receipt_sha256": digest(receipt_path),
                       "receipt_updated": receipt_mtime_before is not None and receipt_mtime_after is not None and receipt_mtime_before != receipt_mtime_after,
                       "receipt_refresh_granted": b"[RECEIPT-GUARD-REFRESH]" in proc.stderr,
                       "recorded_acceptance": original.get("acceptance_checks_passed"),
                       "observed_acceptance": receipt.get("acceptance_checks_passed"),
                       "isolated": True})
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        result.update({"exit": None, "error": str(error)[:500], "isolated": True})
    return result


def run_historical_validators():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        runs = list(pool.map(run_historical_validator, ROUNDS))
    return runs, []


def run_in_clone(clone, argv, label, timeout=180):
    env = clone_environment(clone, label)
    command = shlex.join(["python3", *map(str, argv)])
    item = {"command": command, "date": today(), "argv": ["python3", *map(str, argv)]}
    try:
        proc = subprocess.run([sys.executable, *map(str, argv)], cwd=clone,
                              capture_output=True, timeout=timeout, env=env)
        stdout, stderr = proc.stdout.decode("utf-8", "replace"), proc.stderr.decode("utf-8", "replace")
        item.update({"exit": proc.returncode, "stdout_sha256": sha_bytes(proc.stdout),
                     "stderr_sha256": sha_bytes(proc.stderr), "stdout_tail": stdout[-1800:],
                     "stderr_tail": stderr[-600:]})
    except (OSError, subprocess.SubprocessError) as error:
        item.update({"exit": None, "error": str(error)[:500],
                     "timeout": isinstance(error, subprocess.TimeoutExpired)})
    return item


def reproduce_r18_repair():
    failures, measurement = [], {}
    r18_claims, r19_claims = read_json("reports/round-18/claims.json") or {}, read_json("reports/round-19/claims.json") or {}
    before, after = r18_claims.get("baseline_revision"), r19_claims.get("baseline_revision")
    measurement["revisions"] = {"before_round18": before, "after_round18": after}
    if not before or not after:
        return {"failures": ["Cannot bind round-18 repair revisions from claims.json"],
                "measurement": measurement}
    try:
        clone = make_clone("r18-repair")
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        return {"failures": [f"Could not create isolated round-18 repair clone: {error}"],
                "measurement": measurement}
    d2_runs = {}
    for label, revision in (("before", before), ("after", after)):
        checkout = subprocess.run(["git", "checkout", "--force", "--detach", revision],
                                  cwd=clone, capture_output=True, timeout=120,
                                  env=clone_environment(clone, f"r18-checkout-{label}"))
        if checkout.returncode:
            failures.append(f"Cannot check out round-18 {label} revision {revision}")
            continue
        d2_runs[label] = run_in_clone(clone, ["tools/gates/typed-pipeline-gate.py"],
                                      f"r18-d2-{label}")
    identity = (d2_runs.get("before", {}).get("exit") == d2_runs.get("after", {}).get("exit")
                and d2_runs.get("before", {}).get("stdout_sha256")
                == d2_runs.get("after", {}).get("stdout_sha256"))
    if not identity:
        failures.append("Round-18 D2 default gate output/exit is not byte-identical before vs after the repair")
    measurement["d2_byte_identity"] = {
        "value": identity,
        "command": "python3 tools/gates/typed-pipeline-gate.py (run at round-18 before/after Git revisions in an isolated clone)",
        "date": today(), "runs": d2_runs,
    }
    checkout = subprocess.run(["git", "checkout", "--force", "--detach", after],
                              cwd=clone, capture_output=True, timeout=120,
                              env=clone_environment(clone, "r18-checkout-d4"))
    gate = None
    if checkout.returncode == 0:
        gate = run_in_clone(clone, ["tools/gates/typed-pipeline-gate.py",
                                    "examples/culture-d4/packet.d4.yml"], "r18-d4-gate")
    else:
        failures.append(f"Cannot restore post-round-18 revision for D4 gate: {after}")
    summary = re.search(r"summary:\s*(\d+)/(\d+) legs passed", (gate or {}).get("stdout_tail", ""))
    counts = [int(summary.group(1)), int(summary.group(2))] if summary else None
    reproduced = bool(gate and gate.get("exit") == 0 and counts == [19, 19])
    if not reproduced:
        failures.append(f"Round-18 D4 repair did not reproduce gate 19/19: {counts}, exit {(gate or {}).get('exit')}")
    measurement["d4_gate"] = {"value": counts, "reproduced_19_of_19": reproduced,
                               "command": "python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml (post-round-18 revision in isolated clone)",
                               "date": today(), "run": gate}
    return {"failures": failures, "measurement": measurement}


def run_live_command(argv, label, timeout=600):
    scratch = ROOT / ".scratch" / "round-21" / "regressions" / label
    scratch.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(scratch), "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    item = {"command": shlex.join(["python3", *argv]), "date": today(),
            "argv": ["python3", *argv]}
    try:
        proc = subprocess.run([sys.executable, *argv], cwd=ROOT, capture_output=True,
                              timeout=timeout, env=env)
        item.update({"exit": proc.returncode, "stdout_sha256": sha_bytes(proc.stdout),
                     "stderr_sha256": sha_bytes(proc.stderr),
                     "stdout_tail": proc.stdout.decode("utf-8", "replace")[-700:],
                     "stderr_tail": proc.stderr.decode("utf-8", "replace")[-500:]})
    except (OSError, subprocess.SubprocessError) as error:
        item.update({"exit": None, "error": str(error)[:500],
                     "timeout": isinstance(error, subprocess.TimeoutExpired)})
    return item


REGRESSIONS = [
    ["tools/check-gate-battery.py", "--selftest"],
    ["tools/check-gate-battery.py"],
    ["tools/check-craft-exercise.py", "--selftest"],
    ["tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json"],
    ["tools/assemble-d2.py", "--selftest"],
    ["tools/assemble-d2.py", "--check"],
    ["tools/assemble-d2-typed.py", "--selftest"],
    ["tools/assemble-d2-typed.py", "--check"],
    ["tools/assemble-culture-d3.py", "--selftest"],
    ["tools/assemble-culture-d3.py", "--check"],
    ["tools/assemble-culture-d4.py", "--selftest"],
    ["tools/assemble-culture-d4.py", "--check"],
    ["tools/d2-typed-labels.py", "--selftest"],
    ["tools/d2-typed-labels.py", "--check"],
    ["tools/gates/typed-pipeline-gate.py", "--selftest"],
    ["tools/gates/typed-pipeline-gate.py"],
    ["tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.yml"],
    ["tools/check-evidence-coupling.py", "--selftest"],
    ["tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest"],
    ["tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet"],
]


def measure_regressions():
    failures, runs = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(run_live_command, argv, f"{index:02d}", 900)
                   for index, argv in enumerate(REGRESSIONS, 1)]
        runs = [future.result() for future in futures]
    for item in runs:
        if item.get("exit") != 0:
            failures.append(f"Regression failed: {item['command']} (date {item['date']}, exit {item.get('exit')})")
    return {"passed": not failures, "failures": failures, "runs": runs,
            "date": today()}


def defect_status(row):
    return str(row.get("status", row.get("disposition", row.get("decision", "")))).lower()


def defect_evidence(row, keys):
    for key in keys:
        value = row.get(key)
        if value not in (None, "", [], {}):
            return value
    return None


def measure_operability():
    failures, missing = [], []
    defects_dir = ROOT / f"{ROUND_DIR}/defects"
    ledger_rel = f"{ROUND_DIR}/defects/ledger.json"
    ledger = read_json(ledger_rel)
    if ledger is None:
        missing.append(ledger_rel)
        failures.append(f"Missing or unparseable consolidated defect ledger: {ledger_rel}")
    rows = rows_from(ledger, ("defects", "findings", "rows", "items", "entries", "queue"))
    serialized = json.dumps(ledger, ensure_ascii=False).lower() if ledger is not None else ""
    categories = {
        "route_capacity": bool(re.search(r"route.{0,60}capacity|capacity.{0,60}route", serialized)),
        "scribe_seat_failures": bool(re.search(r"scribe.{0,80}seat.{0,80}(fail|failure|unavailable)|seat.{0,80}scribe.{0,80}(fail|failure|unavailable)", serialized)),
        "fragment_index_collision": bool(re.search(r"fragment[- _]index.{0,60}colli|colli.{0,60}fragment[- _]index", serialized)),
        "mirror_faithfulness_wart": bool(re.search(r"mirror.{0,80}faithful|faithful.{0,80}mirror", serialized)),
    }
    for name, present in categories.items():
        if not present:
            failures.append(f"Consolidated defect ledger omits required loop-2 defect class: {name}")
    if not rows:
        failures.append("Consolidated defect ledger has no structured defect rows")

    sweeps = {}
    if defects_dir.is_dir():
        for path in sorted(defects_dir.rglob("*.md")):
            if "sweep" not in path.name.lower():
                continue
            relative = path.relative_to(ROOT).as_posix()
            text = read_text(relative)
            for number in ROUNDS:
                if re.search(rf"round[- ]?{number}\b|\br{number}\b", text, re.I):
                    sweeps.setdefault(number, []).append(relative)
            if not DATE_RE.search(text):
                failures.append(f"Defect sweep lacks ISO date: {relative}")
    for number in ROUNDS:
        if number not in sweeps:
            missing.append(f"{ROUND_DIR}/defects/sweep-r{number}.md")
            failures.append(f"No dated conformance sweep found for round {number}")

    ledger_date = ledger.get("date") if isinstance(ledger, dict) else None
    if not isinstance(ledger_date, str) or not DATE_RE.search(ledger_date):
        failures.append(f"Consolidated defect ledger lacks an ISO date: {ledger_rel}")
    fixed = routed = 0
    covered_rounds = set()
    row_summaries = []
    for index, row in enumerate(rows):
        number = row_round(row)
        if number in ROUNDS:
            covered_rounds.add(number)
        else:
            failures.append(f"Defect ledger row {index} has no source round 17-20")
        status = defect_status(row)
        bounded = row.get("bounded") is True or bool(row.get("fix_scope")) or "bounded" in status
        before = defect_evidence(row, ("before", "control_before", "pre_fix", "before_control"))
        after = defect_evidence(row, ("after", "control_after", "post_fix", "after_control"))
        control = defect_evidence(row, ("control", "control_evidence", "test", "evidence", "receipt"))
        closed = bool(re.search(r"\b(fixed|repaired|closed)\b", status))
        if closed:
            if not bounded or before is None or after is None or not control:
                failures.append(f"Closed defect row {index} lacks bounded scope and before/after controls")
            else:
                fixed += 1
            row_summaries.append({"id": row.get("id", row.get("finding_id")),
                                  "round": number, "disposition": "closed-with-control"})
        else:
            owner = row.get("owner", row.get("route_owner", row.get("owner_name", "")))
            note = defect_evidence(row, ("owner_note", "route_note", "note", "reason"))
            destination = row.get("route_round", row.get("destination", row.get("target_round", "")))
            routed_to_22 = str(destination).strip().lower() in ("22", "r22", "round-22")
            if not routed_to_22:
                failures.append(f"Open defect row {index} is not routed to round 22")
            if not owner or not note:
                failures.append(f"Open defect row {index} lacks a round-22 owner note")
            if owner and note and routed_to_22:
                routed += 1
            row_summaries.append({"id": row.get("id", row.get("finding_id")),
                                  "round": number, "disposition": "routed-to-round-22"})
    for number in ROUNDS:
        if number not in covered_rounds:
            failures.append(f"Defect ledger has no finding row sourced from round {number}")
    if fixed == 0:
        failures.append("No bounded fix has before/after controls")
    if routed == 0:
        failures.append("No open defect has an owner-routed round-22 disposition")

    regressions = measure_regressions()
    failures.extend(regressions["failures"])
    return {"passed": not failures, "failures": failures,
            "missing_dependencies": sorted(set(missing)),
            "measurement": {
                "sweeps": {str(number): paths for number, paths in sorted(sweeps.items())},
                "defect_ledger": ledger_rel,
                "ledger_date": ledger_date,
                "finding_rows": {"value": len(rows), "command": "python3 reports/round-21/run-validation.py (reports/round-21/defects/ledger.json)", "date": today()},
                "required_defect_classes": {key: {"value": value,
                    "command": "python3 reports/round-21/run-validation.py (cross-round defect ledger coverage)", "date": today()}
                    for key, value in categories.items()},
                "bounded_fixes": {"value": fixed, "command": "python3 reports/round-21/run-validation.py (closed ledger rows with bounded scope and before/after controls)", "date": today()},
                "round22_routes": {"value": routed, "command": "python3 reports/round-21/run-validation.py (open defect rows with owner notes and route_round 22)", "date": today()},
                "rows": row_summaries,
                "regressions": regressions,
            }}


def path_list(directory):
    base = ROOT / directory
    if not base.is_dir():
        return []
    return [path.relative_to(ROOT).as_posix() for path in sorted(base.rglob("*"))
            if path.is_file() and "__pycache__" not in path.parts and ".scratch" not in path.parts]


def changed_corpus_entries():
    claims = read_json("reports/round-19/claims.json") or {}
    revision = claims.get("baseline_revision")
    command = f"git diff --name-only {revision} HEAD -- corpus/knowledge"
    if not revision:
        return [], {"command": command, "date": today(), "exit": None}, "round-19 baseline missing"
    output = git_output("diff", "--name-only", revision, "HEAD", "--", "corpus/knowledge")
    if output is None:
        return [], {"command": command, "date": today(), "exit": None}, "git diff failed"
    paths = sorted(line for line in output.decode("utf-8", "replace").splitlines()
                   if line.startswith("corpus/knowledge/") and line.endswith(".md"))
    return paths, {"command": command, "date": today(), "exit": 0}, None


def parse_packet_claim_rows(text):
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if re.match(r"#{1,6}\s", line) and "claim" in line.lower() and "ledger" in line.lower():
            start = index + 1
            break
    if start is None:
        return []
    end = len(lines)
    for index in range(start, len(lines)):
        if re.match(r"#{1,6}\s", lines[index]) and "claim" not in lines[index].lower():
            end = index
            break
    body = lines[start:end]
    header = None
    for line in body:
        if line.strip().startswith("|"):
            cells = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
            if any(cell in ("id", "claim", "claim id", "claim_id") or "claim_id" in cell for cell in cells):
                header = cells
                break
    if not header:
        return []
    id_index = next((i for i, cell in enumerate(header)
                     if cell in ("id", "claim", "claim id", "claim_id") or "claim_id" in cell), 0)
    status_index = next((i for i, cell in enumerate(header)
                         if "uncertainty_status" in cell or cell == "uncertainty status"), None)
    basis_index = next((i for i, cell in enumerate(header)
                        if "uncertainty_basis" in cell or cell == "uncertainty basis"), None)
    legacy_index = next((i for i, cell in enumerate(header)
                         if "uncertainty" in cell and i not in (status_index, basis_index)), None)
    evidence_index = next((i for i, cell in enumerate(header)
                           if "evidence_status" in cell or cell == "evidence status"), None)
    rows, separator_seen = [], False
    for line in body:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", cell) for cell in cells if cell):
            separator_seen = True
            continue
        if not separator_seen or len(cells) < len(header):
            continue
        claim_id = re.sub(r"[`*]", "", cells[id_index]).strip()
        status, basis = None, ""
        if status_index is not None:
            status_match = re.search(r"\b(supported|partial|unresolved)\b", cells[status_index], re.I)
            status = status_match.group(1).lower() if status_match else None
            basis = cells[basis_index] if basis_index is not None else ""
        elif legacy_index is not None:
            cell = cells[legacy_index]
            status_match = re.search(r"\b(supported|partial|unresolved)\b", cell, re.I)
            status = status_match.group(1).lower() if status_match else None
            basis_match = re.search(r"basis\s*[:\-—]\s*(.+)", cell, re.I)
            basis = basis_match.group(1) if basis_match else cell
        evidence = cells[evidence_index] if evidence_index is not None else ""
        rows.append({"claim_id": claim_id, "evidence_status": evidence,
                     "uncertainty": {"status": status,
                                     "basis": re.sub(r"<br\s*/?>", " ", basis, flags=re.I).strip().strip("` ")}})
    return rows


def run_handoff_uncertainty(packet_path, rows):
    scratch = ROOT / ".scratch" / "round-21" / "handoff"
    scratch.mkdir(parents=True, exist_ok=True)
    claims_path = scratch / "packet-claims.json"
    claims_path.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
    temp = scratch / "tmp"
    temp.mkdir(parents=True, exist_ok=True)
    argv = ["tools/harness/packet_uncertainty.py", "--claims-json",
            claims_path.relative_to(ROOT).as_posix(), "--json"]
    env = {**os.environ, "TMPDIR": str(temp), "PYTHONDONTWRITEBYTECODE": "1"}
    item = {"command": shlex.join(["python3", *argv]), "date": today(), "argv": ["python3", *argv]}
    try:
        proc = subprocess.run([sys.executable, *argv], cwd=ROOT, capture_output=True,
                              timeout=120, env=env)
        item.update({"exit": proc.returncode, "stdout": proc.stdout.decode("utf-8", "replace")[-2000:],
                     "stderr_tail": proc.stderr.decode("utf-8", "replace")[-500:],
                     "stdout_sha256": sha_bytes(proc.stdout)})
        try:
            item["json"] = json.loads(proc.stdout.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError):
            item["json"] = None
    except (OSError, subprocess.SubprocessError) as error:
        item.update({"exit": None, "error": str(error)[:500]})
    return item


def required_adjacency_paths():
    corpus, discovery, error = changed_corpus_entries()
    paths = set(corpus)
    paths.update(f"reports/round-20/entries/R20-D{number}.md" for number in range(21, 25))
    paths.update((
        "corpus/lessons/round-20.md",
        "reports/round-20/handoff/packet-v3-16.md",
        "reports/round-20/handoff/packet.md",
        "reports/round-20/handoff/capability-draft.md",
        "reports/round-20/handoff/frozen.md",
        "reports/round-20/handoff/v3.md",
        "reports/round-20/handoff/claims-map.md",
        "reports/round-20/handoff/design.md",
        "examples/culture-d4/",
        "components/12-provenance.yml",
    ))
    return sorted(paths), discovery, error


def measure_adjacency():
    failures, missing = [], []
    adjacency_rel = f"{ROUND_DIR}/adjacency/entries.md"
    adjacency_text = read_text(adjacency_rel)
    if not adjacency_text:
        missing.append(adjacency_rel)
        failures.append(f"Missing adjacency audit: {adjacency_rel}")
    elif not DATE_RE.search(adjacency_text):
        failures.append(f"Adjacency audit lacks an ISO evidence date: {adjacency_rel}")

    required, discovery, discovery_error = required_adjacency_paths()
    if discovery_error:
        failures.append(f"Cannot derive loop-2 corpus entry inventory: {discovery_error}")
    audit_lower = adjacency_text.lower()
    uncovered = [path for path in required if path.lower() not in audit_lower]
    for path in uncovered:
        failures.append(f"Adjacency audit does not cite required content path: {path}")

    r19_entry_paths = [f"reports/round-19/entries/R19-C{number}.md" for number in range(11, 21)]
    r20_entry_paths = [f"reports/round-20/entries/R20-D{number}.md" for number in range(21, 25)]
    r19_entries_present = [path for path in r19_entry_paths if safe_path(path).is_file()]
    r20_entries_present = [path for path in r20_entry_paths if safe_path(path).is_file()]
    if len(r19_entries_present) != 10 or "R19-C{i}" not in adjacency_text:
        failures.append("Adjacency audit does not verify the complete R19-C11..C20 entry inventory")
    if len(r20_entries_present) != 4:
        failures.append("Adjacency audit inventory is missing one or more R20-D21..D24 fragments")
    r19_inventory = bool(re.search(r"R19 author fragments:\s*10\s+10", adjacency_text))
    r20_inventory = bool(re.search(r"R20 author fragments:\s*4\s+4", adjacency_text))
    if not r19_inventory or not r20_inventory:
        failures.append("Adjacency audit does not record matching R19/R20 author-fragment inventory counts")

    d4_full_tree_scan = bool(re.search(r"examples/culture-d4/.*full-tree lexical scan|full-tree lexical scan.*examples/culture-d4/", adjacency_text, re.I | re.S))
    if not d4_full_tree_scan:
        failures.append("Adjacency audit does not document the D4 full-tree lexical scan")
    boundary_verdicts = {
        claim: bool(re.search(rf"\*\*{claim}[^|]*\*\*\s*\|\s*\*\*PASS\b", adjacency_text))
        for claim in ("A01", "A02", "A03", "A04")
    }
    if not all(boundary_verdicts.values()) or "no bleed found" not in audit_lower:
        failures.append("Adjacency audit does not file PASS/no-bleed conclusions for A01-A04")
    unfiled = 0 if all(boundary_verdicts.values()) and "no bleed found" in audit_lower else 1
    checked = [{"path": path, "cited": path.lower() in audit_lower} for path in required]

    handoff_packet = "reports/round-20/handoff/packet-v3-16.md"
    packet_text = read_text(handoff_packet)
    if not packet_text:
        missing.append(handoff_packet)
        failures.append(f"Missing handoff v3 packet: {handoff_packet}")
    packet_rows = parse_packet_claim_rows(packet_text)
    census = collections.Counter(row["uncertainty"].get("status") for row in packet_rows)
    expected_census = {"supported": 16, "partial": 7, "unresolved": 4}
    census_ok = len(packet_rows) == 27 and dict(census) == expected_census
    if not census_ok:
        failures.append(f"Handoff v3 uncertainty census is {len(packet_rows)} / {dict(census)}, expected 27 / {expected_census}")
    d4_claim_count = sum(str(row.get("claim_id", "")).startswith("D4-") for row in packet_rows)
    if d4_claim_count != 12:
        failures.append(f"Handoff v3 D4 claim count is {d4_claim_count}, expected 12")
    unresolved = [row["claim_id"] for row in packet_rows
                  if row["uncertainty"].get("status") == "unresolved"]
    oq_match = re.search(r"(?im)^#{1,6}\s+open_questions\b(.*?)(?=^#{1,6}\s|\Z)", packet_text, re.S)
    oq_text = oq_match.group(1) if oq_match else ""
    missing_oq = [claim_id for claim_id in unresolved if claim_id not in oq_text]
    if missing_oq:
        failures.append(f"Unresolved handoff claims missing from open_questions: {missing_oq}")

    link_run = run_live_command(["tools/harness/packet_links.py", "--packet",
                                 "reports/round-20/handoff/twin.json"], "handoff-links", 180)
    live_link_match = re.search(r"links=(\d+)\s+resolved=(\d+)\s+findings=(\d+)",
                                link_run.get("stdout_tail", ""))
    filed_link_match = re.search(r"links=(\d+)\s+resolved=(\d+)\s+findings=(\d+)",
                                 packet_text)
    live_links = tuple(map(int, live_link_match.groups())) if live_link_match else None
    filed_links = tuple(map(int, filed_link_match.groups())) if filed_link_match else None
    if link_run.get("exit") != 0 or not live_links or live_links[0] != live_links[1] or live_links[2] != 0:
        failures.append(f"Current handoff twin link replay failed: exit {link_run.get('exit')}, result {live_links}")
    link_discrepancy = bool(live_links and filed_links and live_links != filed_links)
    link_disposition_filed = False
    if link_discrepancy:
        ledger_payload = read_json(f"{ROUND_DIR}/defects/ledger.json") or {}
        link_row = next((row for row in rows_from(ledger_payload, ("defects", "entries", "rows"))
                         if row.get("id") == "R20-HANDOFF-LINK-COUNT"), {})
        recount_note = read_text(f"{ROUND_DIR}/recount/r20-2.md")
        link_row_text = json.dumps(link_row, ensure_ascii=False)
        link_disposition_filed = bool(
            str(link_row.get("status", "")).lower() == "open"
            and str(link_row.get("route_round", "")) == "22"
            and link_row.get("owner") and link_row.get("owner_note")
            and filed_links and live_links
            and str(filed_links[0]) in link_row_text and str(live_links[0]) in link_row_text
            and str(filed_links[0]) in recount_note and str(live_links[0]) in recount_note
            and re.search(r"cause is unknown", recount_note, re.I))
        if not link_disposition_filed:
            failures.append("Handoff link-count discrepancy is not preserved and owner-routed in the R20 recount/defect ledger")

    packet_gate = run_live_command(["tools/gates/handoff-packet-check.py", handoff_packet], "handoff-gate", 180)
    gate_stdout = packet_gate.get("stdout_tail", "")
    fields = re.search(r"fields=(\d+)/(\d+)", gate_stdout)
    glossary = re.search(r"glossary-entries=(\d+)", gate_stdout)
    findings = re.search(r"findings=(\d+)", gate_stdout)
    handoff_gate_ok = bool(packet_gate.get("exit") == 0 and fields and
                           tuple(map(int, fields.groups())) == (16, 16) and glossary and
                           int(glossary.group(1)) == 20 and findings and int(findings.group(1)) == 0)
    if not handoff_gate_ok:
        failures.append("Handoff v3 contract gate did not reproduce fields=16/16, glossary=20, findings=0")

    uncertainty_run = run_handoff_uncertainty(handoff_packet, packet_rows)
    uncertainty_output = uncertainty_run.get("json")
    uncertainty_findings = uncertainty_output.get("findings") if isinstance(uncertainty_output, dict) else None
    uncertainty_ok = uncertainty_run.get("exit") == 0 and uncertainty_findings == []
    if not uncertainty_ok:
        failures.append(f"Handoff v3 independent uncertainty checker did not pass: exit {uncertainty_run.get('exit')}, findings {uncertainty_findings}")

    audit_v3_rel = "reports/round-20/handoff/audit-v3.md"
    audit_v3 = read_text(audit_v3_rel)
    if not audit_v3 or "pass" not in audit_v3.lower() or not DATE_RE.search(audit_v3):
        failures.append("Missing dated passing v3 contract audit")
    interop_rel = "reports/round-20/handoff/interop.md"
    interop_text = read_text(interop_rel)
    known_divergence = "F-INT-1" in audit_v3 and Path(ROOT / interop_rel).is_file() and "F-INT-1" in interop_text
    if "F-INT-1" in audit_v3 and not known_divergence:
        failures.append("Known handoff markdown/twin divergence is not filed in interop evidence")

    province_rel = f"{ROUND_DIR}/adjacency/province.md"
    province_text = read_text(province_rel)
    province_ok = bool(province_text and re.search(r"(?i)\baccurate\b|\bstill accurate\b|\bno drift\b", province_text)
                       and re.search(r"(?i)round[- ]?19|round[- ]?20|rounds? 17[-–]20", province_text)
                       and DATE_RE.search(province_text))
    if not province_text:
        missing.append(province_rel)
        failures.append("No adjacency review explicitly concludes PROVINCE.md remains accurate")
    elif not province_ok:
        failures.append(f"Dated PROVINCE review does not conclude the loop-2 scope remains accurate: {province_rel}")

    return {"passed": not failures, "failures": failures,
            "missing_dependencies": sorted(set(missing)),
            "measurement": {
                "adjacency_audit": {"path": adjacency_rel, "date_present": bool(DATE_RE.search(adjacency_text)),
                    "command": "python3 reports/round-21/run-validation.py (read and verify reports/round-21/adjacency/entries.md)", "date": today()},
                "required_paths": {"value": required, "count": {"value": len(required),
                    "command": "python3 reports/round-21/run-validation.py (round-19 baseline diff plus named R20/handoff/D4 references)", "date": today()},
                    "command": discovery["command"], "date": discovery["date"],
                    "discovery_exit": discovery["exit"]},
                "uncovered_paths": uncovered,
                "reviewed_paths": checked,
                "entry_inventory": {
                    "r19_author_fragments": {"value": len(r19_entries_present),
                        "expected": 10, "command": "python3 reports/round-21/run-validation.py (check reports/round-19/entries/R19-C11..C20 and filed inventory command)", "date": today()},
                    "r20_author_fragments": {"value": len(r20_entries_present),
                        "expected": 4, "command": "python3 reports/round-21/run-validation.py (check reports/round-20/entries/R20-D21..D24 and filed inventory command)", "date": today()},
                    "r19_corpus_entries": {"value": len([path for path in required if path.startswith("corpus/knowledge/")]),
                        "command": discovery["command"], "date": discovery["date"]}},
                "d4_full_tree_scan": {"value": d4_full_tree_scan,
                    "command": "python3 reports/round-21/run-validation.py (verify documented full-tree lexical scan in adjacency audit)", "date": today()},
                "boundary_verdicts": {"value": boundary_verdicts,
                    "command": "python3 reports/round-21/run-validation.py (parse A01-A04 verdict matrix in adjacency audit)", "date": today()},
                "unfiled_bleed": {"value": unfiled,
                    "command": "python3 reports/round-21/run-validation.py (verify filed A01-A04 no-bleed conclusion)", "date": today()},
                "handoff_gate": {"value": {"passed": handoff_gate_ok,
                    "fields": tuple(map(int, fields.groups())) if fields else None,
                    "glossary_entries": int(glossary.group(1)) if glossary else None,
                    "findings": int(findings.group(1)) if findings else None},
                    "command": packet_gate["command"], "date": packet_gate["date"], "run": packet_gate},
                "handoff_link_counts": {"filed": filed_links, "replayed": live_links,
                    "delta": live_links[0] - filed_links[0] if live_links and filed_links else None,
                    "discrepancy_preserved_and_routed": link_disposition_filed if link_discrepancy else True,
                    "command": link_run["command"], "date": link_run["date"], "run": link_run},
                "uncertainty_census": {"value": {"claims": len(packet_rows), "d4_claims": d4_claim_count,
                    "statuses": dict(census), "unresolved_missing_open_question": missing_oq,
                    "checker_passed": uncertainty_ok},
                    "command": uncertainty_run["command"], "date": uncertainty_run["date"],
                    "run": {key: value for key, value in uncertainty_run.items() if key != "json"}},
                "contract_audit": {"path": audit_v3_rel if audit_v3 else None,
                    "dated": bool(DATE_RE.search(audit_v3)),
                    "handoff_divergence_filed": known_divergence,
                    "command": "python3 reports/round-21/run-validation.py (read reports/round-20/handoff/audit-v3.md and interop.md)", "date": today()},
                "province_review": {"path": province_rel if province_text else None,
                    "verdict": "accurate" if province_ok else None,
                    "command": "python3 reports/round-21/run-validation.py (read dated PROVINCE review against PROVINCE.md)", "date": today()},
            }}


def main():
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    (ROOT / ".scratch" / "round-21").mkdir(parents=True, exist_ok=True)
    locked_paths = [f"reports/round-{number}" for number in LOCKED_ROUNDS]
    status_before = git_status(locked_paths)
    results = {"C": audit_recount(), "O": measure_operability(), "A": measure_adjacency()}
    status_after = git_status(locked_paths)
    if status_before != status_after:
        results["A"]["failures"].append("Protected filed rounds 8-20 worktree status changed during validation")
        results["A"]["passed"] = False
    missing = sorted({item for result in results.values()
                      for item in result.get("missing_dependencies", [])})
    claims = read_json(f"{ROUND_DIR}/claims.json") or {}
    targets = read_json(f"{ROUND_DIR}/targets.json") or {}
    passed = all(result["passed"] for result in results.values())
    receipt = {
        "round": 21,
        "runner": RUNNER,
        "runner_sha256": digest(ROOT / RUNNER),
        "counting_command": "python3 reports/round-21/run-validation.py",
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
                                "command": "git status --short -- reports/round-8 through reports/round-20",
                                "date": today()},
        "limits": [
            "Historical round validators are invoked only in isolated clones under .scratch/round-21; REFRESH_RECEIPTS=1 is set only in those clones, the runner must prove its cloned receipt was updated, round 18 redirects its external replay temp candidate into repository scratch, and its ignored R11 log is copied into that clone only after digest verification.",
            "The recount inventory extracts each counting_command plus command, command_line, argv and recheck_command leaves from rounds 17-20. Each normalized source-round command must have one dated recorded/observed ledger row.",
            "Adjacency checks use the round-19 baseline diff, the named R20 handoff/entry surfaces, the R19-C11..C20 and R20-D21..D24 inventories, and the documented D4 full-tree scan; the D4 child tree is not required to be duplicated path-by-path in the audit.",
            "Adjacency checks are structural evidence checks, not a semantic determination of canon, historical truth or rights. The filed 102-link count and current replay are reported side-by-side; any difference remains a routed finding, not a normalized value.",
            "Regression checks use check/selftest modes or the v3 quiet exercise; TMPDIR is scoped beneath this repository's .scratch and Python bytecode is disabled. No commit or push is performed.",
        ],
    }
    output = ROOT / OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                      encoding="utf-8")
    for claim_id, result in results.items():
        print(f"claim {claim_id}: {'PASS' if result['passed'] else 'FAIL'}")
    print(f"acceptance_checks_passed: {passed}")
    if missing:
        print("missing_dependencies: " + ", ".join(missing))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
