#!/usr/bin/env python3
"""Measure round-30 O/C/D acceptance; --check never publishes a receipt."""
from __future__ import annotations

import argparse
from collections import Counter
import concurrent.futures
import datetime as dt
import difflib
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
ROUND = "reports/round-30"
RUNNER = f"{ROUND}/run-validation.py"
OUTPUT = f"{ROUND}/validation.json"
COMMAND = f"python3 {RUNNER}"
CLAIMS = f"{ROUND}/claims.json"
RESOLUTION = f"{ROUND}/routed-resolution.json"
RETRO = f"{ROUND}/loop3-retrospective.md"
PACKET = "examples/culture-d4/packet.d4.yml"
LAW = "tools/gates/register-law-gate.py"
CEILINGS = "corpus/knowledge/linguistics/register-lexicon-ceilings.md"
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 30)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 30))
ROUTES = {
    "qreg-dangles": r"QREG|DANGLING.*(?:DESIGN|RECORD)|DESIGN.*DANGL",
    "law-battery": r"BATTERY|ABSENT-FROM-REGRESSION|GATE.*REGISTR",
    "x63-f2": r"X63[- ]?F2|ABSENCE.*(?:SWEEP|CEILING)",
    "speaker-tail": r"SPEAKER|TAMPER[- ]?TAIL",
    "telemetry-durability": r"TELEMETRY|AVAILABILITY.*DURAB",
}
PATH_RE = re.compile(r"\b(?:reports|corpus|tools|examples)/[A-Za-z0-9_./-]+\.(?:md|py|json|ya?ml|txt|tsv)\b")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
CMD_RE = re.compile(r"\b(?:python3?|journalctl|sha256sum|git (?:show|diff|grep|ls-tree)|comm |rg |grep |find |ls tools|Path\()")
FINDING_RE = re.compile(r"^FINDING\s+(D4L-LAW-[A-Z-]+):", re.M)
REGRESSIONS = (
    ("battery-selftest", "tools/check-gate-battery.py", "--selftest"),
    ("battery", "tools/check-gate-battery.py"),
    ("d2-assembly", "tools/assemble-d2.py", "--check"),
    ("d2-adapter", "tools/assemble-d2-typed.py", "--check"),
    ("d3-assembly", "tools/assemble-culture-d3.py", "--check"),
    ("d4-assembly-selftest", "tools/assemble-culture-d4.py", "--selftest"),
    ("d4-assembly", "tools/assemble-culture-d4.py", "--check"),
    ("d4-adapter-selftest", "tools/assemble-d4-typed.py", "--selftest"),
    ("d4-adapter", "tools/assemble-d4-typed.py", "--check", "examples/culture-d4/packet.d4.typed.yml"),
    ("projector-selftest", "tools/d2-typed-labels.py", "--selftest"),
    ("d2-projection", "tools/d2-typed-labels.py", "--check"),
    ("d4-projection", "tools/d2-typed-labels.py", "--packet", PACKET, "--check", "examples/culture-d4/typed-labels.d4.yml"),
    ("typed-selftest", "tools/gates/typed-pipeline-gate.py", "--selftest"),
    ("typed-generalized-selftest", "tools/gates/typed-pipeline-gate.py", "--selftest-generalized"),
    ("typed-d2", "tools/gates/typed-pipeline-gate.py"),
    ("typed-d4", "tools/gates/typed-pipeline-gate.py", PACKET),
    ("typed-d4-typed", "tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.typed.yml"),
    ("d4-label-gate", "tools/gates/d4-typed-labels-check-gate.py", "examples/culture-d4/typed-labels.d4.yml"),
    ("d4-assembly-gate", "tools/gates/d4-assembly-check-gate.py", PACKET),
    ("argot-selftest", "tools/gates/argot-derivation-gate.py", "--selftest"),
    ("argot-d4", "tools/gates/argot-derivation-gate.py", PACKET),
    ("law-selftest", LAW, "--selftest"),
    ("replay-selftest", "tools/replay-frozen.py", "--selftest"),
    ("handoff-v2", "tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet"),
    ("handoff-v3-selftest", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest"),
    ("handoff-v3", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet"),
    ("craft-selftest", "tools/check-craft-exercise.py", "--selftest"),
    ("craft", "tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json"),
    ("links-selftest", "tools/harness/packet_links.py", "--selftest"),
    ("uncertainty-selftest", "tools/harness/packet_uncertainty.py", "--selftest"),
)


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
            digest = sha(data)
            if relative in self.inputs and self.inputs[relative] != digest:
                self.errors.append(f"evidence changed between reads: {relative}")
            self.inputs.setdefault(relative, digest)
            return data.decode("utf-8")
        except (OSError, ValueError, UnicodeError) as error:
            self.missing.add(relative)
            self.errors.append(f"{relative}: {error}")
            return ""

    def document(self, relative):
        text = self.text(relative)
        try:
            return strict_json(text) if text else None
        except (TypeError, ValueError) as error:
            self.errors.append(f"{relative}: {error}")
            return None


def result(failures, measurement):
    return {"passed": not failures, "date": today(), "command": COMMAND,
            "failures": failures, "measurement": measurement}


def git(*args):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1")
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, env=env, timeout=60)


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
    failures = ["filed rounds 8-29 or their frozen generations changed"] if changes or additions else []
    return result(failures, {"baseline_revision": revision,
                            "protected_files": metric(len(expected), "git ls-tree of filed report/frozen paths"),
                            "differences": changes, "new_protected_paths": additions})


def run_command(name, parts):
    argv = [sys.executable, "-B", *parts]
    tmpdir = "/var/tmp" if name == "replay-selftest" else str(ROOT / ".scratch")
    env = {**os.environ, "TMPDIR": tmpdir, "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    item = {"name": name, "command": shlex.join(["python3", "-B", *parts]),
            "date": today(), "tmpdir": tmpdir}
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, timeout=180)
        item.update(exit_code=proc.returncode, stdout=proc.stdout.decode("utf-8", "replace"),
                    stderr=proc.stderr.decode("utf-8", "replace"),
                    stdout_sha256=sha(proc.stdout), stderr_sha256=sha(proc.stderr))
    except (OSError, subprocess.SubprocessError) as error:
        item.update(exit_code=None, stdout="", stderr="", error=f"{type(error).__name__}: {error}")
    item["elapsed_seconds"] = round(time.monotonic() - started, 3)
    item["passed"] = item["exit_code"] == 0
    return item


def regressions():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        return list(pool.map(lambda spec: run_command(spec[0], list(spec[1:])), REGRESSIONS))


def law_findings(text):
    return sorted(set(" ".join(line.split()) for line in text.splitlines()
                      if FINDING_RE.match(line)))


def mutate_law(text, field, value):
    match = re.search(r"(?m)^register_law:\s*$", text)
    if not match:
        raise ValueError("packet has no expanded register_law block")
    tail = text[match.end():]
    following = re.search(r"(?m)^[A-Za-z_][A-Za-z0-9_-]*:", tail)
    end = match.end() + following.start() if following else len(text)
    block = text[match.end():end]
    pattern = re.compile(r"(?m)^([ \t]+)" + re.escape(field)
                         + r":[^\n]*(?:\n\1[ \t]+[^\n]*)*")
    block, count = pattern.subn(lambda item: item.group(1) + field + ": " + value, block, count=1)
    if count != 1:
        raise ValueError(f"cannot change exactly one law {field} field")
    return text[:match.end()] + block + text[end:]


def law_probes(evidence):
    text = evidence.text(PACKET)
    clean = run_command("law-clean", [LAW, "--packet", PACKET])
    clean_lines = law_findings(clean["stdout"])
    specs = (
        ("force", "force", '"no-such-force"', "D4L-LAW-FORCE"),
        ("speaker-token", "speaker", '"nobody-nowhere (ZZ-99)"', "D4L-LAW-SPEAKER"),
        ("speaker-tokenless", "speaker", '"nobody-nowhere"', "D4L-LAW-SPEAKER"),
        ("consequence", "consequence", '"the act evaporates silently"', "D4L-LAW-CONSEQUENCE"),
        ("dangling", "design_row", "[QREG-99]", "D4L-LAW-DANGLING"),
        ("kind", "kind", '"unknown-kind"', "D4L-LAW-KIND"),
    )
    with tempfile.TemporaryDirectory(prefix="r30-x33-law-", dir=ROOT / ".scratch") as temporary:
        work = Path(temporary)
        prepared = []
        for name, field, value, expected_class in specs:
            try:
                mutated = mutate_law(text, field, value)
                target = work / f"{name}.yml"
                target.write_text(mutated, encoding="utf-8")
                prepared.append((name, target, expected_class, mutated != text))
            except ValueError as error:
                prepared.append((name, None, expected_class, str(error)))
        def invoke(spec):
            name, target, expected_class, changed = spec
            if target is None:
                return {"name": name, "passed": False, "error": changed, "date": today(), "command": COMMAND}
            item = run_command(f"law-control-{name}", [LAW, "--packet", str(target)])
            added = sorted(set(law_findings(item["stdout"])) - set(clean_lines))
            item.update(expected_finding=expected_class, changed=changed, added_finding_lines=added)
            item["passed"] = (changed is True and item["exit_code"] == 1
                              and any(line.startswith(f"FINDING {expected_class}:") for line in added))
            return item
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            controls = list(pool.map(invoke, prepared))
    return {"clean": clean, "clean_findings": clean_lines,
            "clean_finding_count": metric(len(clean_lines), "emitted clean law finding lines"),
            "controls": controls}


def documents(evidence):
    resolution = evidence.document(RESOLUTION) if safe_path(RESOLUTION).is_file() else {}
    referenced = set(PATH_RE.findall(json.dumps(resolution, ensure_ascii=False)))
    found = {}
    for path in sorted(safe_path(ROUND).rglob("*.md")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix()
        relevant = (relative in referenced or relative == RETRO
                    or any(f"/{directory}/" in relative for directory in ("fixes", "craft", "retro"))
                    or bool(re.search(r"(?i)retrospective|craft.*review|review.*craft|box[-_ ]?1", path.name)))
        if relevant:
            found[relative] = evidence.text(relative)
    return found


def row_list(document):
    if isinstance(document, list):
        return document
    if isinstance(document, dict):
        for name in ("items", "entries", "resolutions", "routed_items", "routes"):
            if isinstance(document.get(name), list):
                return document[name]
    return []


def classify_route(row):
    if not isinstance(row, dict):
        return []
    identity = " ".join(str(row.get(key, "")) for key in
                        ("id", "route", "routed_id", "source_id"))
    identified = [name for name, pattern in ROUTES.items() if re.search(pattern, identity, re.I)]
    if identified:
        return identified
    head = " ".join(str(row.get(key, "")) for key in ("item", "title", "summary", "issue"))
    return [name for name, pattern in ROUTES.items() if re.search(pattern, head, re.I)]


def dated_command(text):
    return bool(DATE_RE.search(text) and CMD_RE.search(text))


def route_status(row):
    value = str(row.get("status", row.get("disposition", ""))).strip().lower().replace("_", "-")
    if value in ("fixed-with-control", "fixed", "resolved", "closed", "applied-with-control"):
        return "fixed-with-control"
    if value in ("documented", "documented-with-owner", "documented-with-owner-and-reason", "deferred", "routed"):
        return "documented"
    return None


def validate_resolution(document, docs):
    rows = row_list(document)
    failures, measured = [], []
    covered = Counter()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            failures.append(f"routed row {index + 1} is not an object")
            continue
        families = classify_route(row)
        if len(families) != 1:
            failures.append(f"routed row {index + 1} identifies {len(families)} routed items, expected one")
            continue
        family = families[0]
        covered[family] += 1
        status = route_status(row)
        blob = json.dumps(row, ensure_ascii=False)
        refs = sorted(set(PATH_RE.findall(blob)))
        missing_refs = [relative for relative in refs if not safe_path(relative).is_file()]
        supporting = "\n".join(docs.get(relative, "") for relative in refs)
        dated = dated_command(blob + "\n" + supporting)
        control = bool(row.get("control") or row.get("controls") or
                       re.search(r"(?i)\b(?:negative|paired|tamper|control)\b", supporting))
        owner = row.get("owner")
        reason = row.get("reason", row.get("owner_note", row.get("rationale")))
        valid = bool(status and refs and not missing_refs and dated)
        if status == "fixed-with-control":
            valid = valid and control
        elif status == "documented":
            valid = valid and bool(owner) and bool(reason)
        if not valid:
            failures.append(f"{family}: no supported dated disposition with control, or owner + reason")
        measured.append({"item": family, "id": row.get("id"), "status": status, "passed": valid,
                         "references": refs, "missing_references": missing_refs,
                         "dated_command": dated, "control_named": control, "owner": owner})
    if set(covered) != set(ROUTES) or any(count != 1 for count in covered.values()) or len(rows) != 5:
        failures.append("routed-resolution must identify exactly the five declared items once each")
    return result(failures, {"source": RESOLUTION, "rows": measured,
                            "dispositioned": metric(sum(row["passed"] for row in measured), "supported routed rows"),
                            "required": metric(5, "round-30 declared routed queue")})


def append_only_amendment(before, after):
    changes = difflib.SequenceMatcher(a=before.splitlines(keepends=True),
                                    b=after.splitlines(keepends=True), autojunk=False).get_opcodes()
    return (all(tag in ("equal", "insert") for tag, *_ in changes)
            and any(tag == "insert" for tag, *_ in changes))


def telemetry_check(evidence):
    rules = evidence.text("AGENTS.md")
    convention = bool(re.search(r"reports/round-\s*(?:N|<N>|\{N\}|\d+)[^\n]{0,50}/telemetry/", rules, re.I)
                      and re.search(r"(?i)durab|persist|never[^\n]*scratch|not[^\n]*scratch", rules))
    files = []
    directory = safe_path(f"{ROUND}/telemetry")
    if directory.is_dir():
        for path in sorted(directory.rglob("*")):
            if path.is_file() and path.suffix.lower() in (".json", ".jsonl", ".txt", ".md", ".log", ".csv", ".tsv"):
                relative = path.relative_to(ROOT).as_posix()
                text = evidence.text(relative)
                files.append({"path": relative, "bytes": len(text.encode("utf-8")),
                              "dated_command": dated_command(text),
                              "measurement": bool(re.search(r"(?i)attempt|http|status|sample|completion|route|worker", text))})
    passed = convention and any(row["bytes"] and row["dated_command"] and row["measurement"] for row in files)
    return {"passed": passed, "convention_present": convention, "files": files,
            "durable_files": metric(len(files), "round-30 durable telemetry files")}


def battery_check(run):
    try:
        document = strict_json(run.get("stdout", ""))
    except (TypeError, ValueError):
        document = {}
    baselines = document.get("baselines", {}).get("summary", {})
    summary = document.get("summary", {})
    registered = baselines.get("gates_registered")
    if isinstance(registered, list):
        names = registered
    else:
        names = document.get("baselines", {}).get("gates_registered", [])
    text = json.dumps(document)
    passed = (run.get("exit_code") == 0 and baselines.get("coverage") == "10/10"
              and not baselines.get("gates_uncovered")
              and baselines.get("pinned") == baselines.get("baselines_found")
              and isinstance(baselines.get("pinned"), int) and baselines["pinned"] > 0
              and not summary.get("fail") and not summary.get("unevaluable")
              and "register-law-gate.py" in text)
    return {"passed": passed, "summary": summary, "baselines": baselines, "registered_names": names,
            "command": run.get("command"), "date": run.get("date")}


def battery_omission_control():
    module = runpy.run_path(str(safe_path("tools/check-gate-battery.py")))
    registered = tuple(module["REGISTERED_GATE_NAMES"])
    with tempfile.TemporaryDirectory(prefix="r30-x33-battery-", dir=ROOT / ".scratch") as temporary:
        base = Path(temporary)
        for name in registered:
            if name == "register-law-gate.py":
                continue
            directory = base / name
            directory.mkdir()
            data = b"round-30 independent omitted-law-baseline control\n"
            (directory / "packet.txt").write_bytes(data)
            baseline = {"schema": "kotodama-frozen-run-v1", "gate": name,
                        "gate_sha256": sha(safe_path(f"tools/gates/{name}").read_bytes()),
                        "inputs": {"packet.txt": sha(data)},
                        "expected": {"exit": 0, "class": "clean", "findings": []}}
            (directory / "expected.json").write_text(json.dumps(baseline), encoding="utf-8")
        row = run_command("battery-law-baseline-omitted",
                          ["tools/check-gate-battery.py", "--baselines-root", str(base)])
        try:
            summary = strict_json(row["stdout"])["baselines"]["summary"]
        except (ValueError, TypeError, KeyError):
            summary = {}
        row.update(registered_gates=list(registered), coverage=summary.get("coverage"),
                   gates_uncovered=summary.get("gates_uncovered"))
        row["passed"] = (len(registered) == len(set(registered)) == 10
                         and "register-law-gate.py" in registered and row["exit_code"] == 2
                         and summary.get("coverage") == "9/10"
                         and summary.get("gates_uncovered") == ["register-law-gate.py"])
        return row


def measure_operability(evidence, claims, docs, runs, probes, preservation):
    disposition = validate_resolution(evidence.document(RESOLUTION), docs)
    failures = list(disposition["failures"])
    statuses = {row["item"]: row["status"] for row in disposition["measurement"]["rows"] if row["passed"]}
    checks = {}
    fixed = lambda name: statuses.get(name) == "fixed-with-control"
    if fixed("qreg-dangles"):
        clean = probes["clean"]
        checks["qreg-dangles"] = clean["exit_code"] == 0 and not probes["clean_findings"]
        checks["dangling-control"] = next((row["passed"] for row in probes["controls"]
                                           if row["name"] == "law-control-dangling"), False)
    battery = battery_check(next((row for row in runs if row["name"] == "battery"), {}))
    battery["omission_control"] = battery_omission_control()
    if fixed("law-battery"):
        checks["law-battery"] = battery["passed"] and battery["omission_control"]["passed"]
    amendment = {}
    if fixed("x63-f2"):
        revision = claims.get("baseline_revision")
        before = baseline_text(revision, CEILINGS)
        after = evidence.text(CEILINGS)
        sources = next(row["references"] for row in disposition["measurement"]["rows"]
                       if row["item"] == "x63-f2")
        companions = [relative for relative in sources if relative.startswith(ROUND + "/")
                      and relative.endswith(".md") and "X63-F2" in docs.get(relative, "")]
        inserted = after[len(before):] if after.startswith(before) else ""
        correction = inserted + "\n" + "\n".join(docs[relative] for relative in companions)
        new_files = [relative for relative in companions
                     if git("ls-tree", "--name-only", revision, "--", relative).stdout == b""]
        witness = baseline_text("6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede",
                                "corpus/knowledge/linguistics/sound-symbolism.md")
        hits = [number for number, line in enumerate(witness.splitlines(), 1)
                if "which semantic fields" in line.lower()]
        amendment = {"history_preserved": after == before or append_only_amendment(before, after),
                     "new_section_or_file": bool(new_files) or bool(re.search(r"(?m)^#{2,6}\s+", inserted)),
                     "names_defect": bool(re.search(r"X63[- ]?F2", correction, re.I)),
                     "qualified_correction": all(token in correction for token in
                                                 ("sound-symbolism.md", "which semantic fields", "ideophone"))
                                             and bool(re.search(r"(?i)withdraw|supersed|false|errat", correction)),
                     "negative_false_zero_control": bool(hits), "baseline_matching_lines": hits,
                     "companion_amendments": new_files,
                     "baseline_sha256": sha(before.encode()), "live_sha256": sha(after.encode())}
        checks["x63-f2"] = all(amendment[key] for key in
                               ("history_preserved", "new_section_or_file", "names_defect",
                                "qualified_correction", "negative_false_zero_control"))
    if fixed("speaker-tail"):
        checks["speaker-tail"] = next((row["passed"] for row in probes["controls"]
                                       if row["name"] == "law-control-speaker-tokenless"), False)
    telemetry = telemetry_check(evidence)
    if fixed("telemetry-durability"):
        checks["telemetry-durability"] = telemetry["passed"]
    for name, passed in checks.items():
        if not passed:
            failures.append(f"fixed route lacks its independent live control: {name}")
    for row in runs:
        if not row["passed"]:
            failures.append(f"regression {row['name']} exited {row['exit_code']}")
    for row in probes["controls"]:
        if row["name"] == "law-control-speaker-tokenless" and not fixed("speaker-tail"):
            continue
        if not row["passed"]:
            failures.append(f"law replay control failed: {row['name']}")
    if not preservation["passed"]:
        failures.extend(preservation["failures"])
    return result(failures, {"routed_resolution": disposition, "live_fix_controls": checks,
                            "battery_registration": battery, "x63_amendment": amendment,
                            "telemetry_durability": telemetry, "law_replay": probes,
                            "regressions": runs, "all_regressions_green": all(row["passed"] for row in runs),
                            "regression_runs": metric(len(runs), "fixed regression inventory"),
                            "protected_filed_artifacts": preservation})


def local_references(text):
    paths = sorted(set(PATH_RE.findall(text)))
    templates, declared_absent, missing = [], [], []
    for relative in paths:
        if re.search(r"round-(?:N|NN)/", relative):
            templates.append(relative)
        elif not safe_path(relative).is_file():
            paragraphs = [paragraph.replace(relative, "") for paragraph in text.split("\n\n")
                          if relative in paragraph]
            if any(re.search(r"(?i)\babsent\b|does not exist|no (?:lane.local |final |validation )*receipt", paragraph)
                   or (re.search(r"(?i)NONEXISTENT|__.*missing", relative)
                       and re.search(r"(?i)control|phantom|negative", paragraph))
                   for paragraph in paragraphs):
                declared_absent.append(relative)
            else:
                missing.append(relative)
    return {"paths": [relative for relative in paths if relative not in templates + declared_absent],
            "templates": templates, "declared_absent": declared_absent, "missing": missing}


def audit_candidates(docs, subject):
    found = []
    for relative, text in docs.items():
        if not re.search(r"(?i)audit|review", relative):
            continue
        if not re.search(subject, text, re.I):
            continue
        refs = local_references(text)
        verdict = bool(re.search(r"(?i)\b(?:verdict|PASS|FAIL|verified|findings?|conditions?|controls?|accept|reject|hold)\b", text))
        receipt = dated_command(text)
        found.append({"path": relative, "dated_command": receipt, "verdict_present": verdict,
                      "references": refs, "passed": receipt and verdict and bool(refs["paths"]) and not refs["missing"]})
    return found


def retrospective_features(text):
    return {
        "dated_commands": dated_command(text),
        "per_round_states": all(bool(re.search(rf"(?i)(?:round[- ]*|R){number}\b", text))
                                 for number in range(25, 30)),
        "final_state_language": bool(re.search(r"(?i)final|ADMITTED|REJECTED|admission|rejection", text)),
        "five_stage_program": all(re.search(pattern, text, re.I) for pattern in
                                  (r"forecast", r"\bleg\b", r"strat(?:um|a)", r"\blaw\b", r"replay")),
        "round17_forecast": bool(re.search(r"(?i)round[- ]*17|R17\b|reports/round-17/", text)),
        "delta_named": bool(re.search(r"(?i)\bdelta\b|weigh.court|furnace.league", text)),
        "three_loops": all(re.search(rf"(?i)loop[- ]*{number}\b", text) for number in (1, 2, 3)),
        "regimen_dispositions": all(re.search(pattern, text, re.I) for pattern in
                                    (r"admi(?:t|ss)", r"reject", r"skip", r"substitut", r"amend")),
        "full_regimen_bounds": bool(re.search(r"(?i)rounds?[^\n]{0,30}\b8\b[^\n]{0,20}\b32\b|R08[^\n]{0,20}R32", text)),
        "future_rounds_not_results": bool(re.search(r"(?i)(?:31|32)[^\n]{0,140}(?:future|pending|not.yet|scheduled|unrun|not.run|forecast)|(?:future|pending|scheduled|unrun)[^\n]{0,140}(?:31|32)", text)),
        "freshness_question": bool(re.search(r"(?i)freshness", text) and re.search(r"(?i)threshold", text)),
        "concrete_recommendation": bool(re.search(r"(?i)recommend", text) and re.search(r"\d+\s*(?:%|/|days?|hours?|rounds?)", text)),
    }


def measure_calibration(evidence, docs):
    text = evidence.text(RETRO)
    features = retrospective_features(text)
    refs = local_references(text)
    audits = audit_candidates(docs, r"retrospective|three.loop|freshness.threshold|regimen.summary")
    digest = sha(text.encode())
    for row in audits:
        row["current_retrospective_hash_bound"] = digest in docs[row["path"]] and RETRO in docs[row["path"]]
        row["passed"] = row["passed"] and row["current_retrospective_hash_bound"]
    good = [row for row in audits if row["passed"]]
    failures = [f"retrospective missing {name}" for name, present in features.items() if not present]
    if not refs["paths"] or refs["missing"]:
        failures.append("retrospective has missing or no resolving repository citations")
    if len(good) < 2:
        failures.append("fewer than two dated retrospective auditor reports bound to the current document hash")
    return result(failures, {"source": RETRO, "sha256": digest, "features": features, "references": refs,
                            "auditors": audits, "qualified_auditors": metric(len(good), "hash-bound retrospective auditors")})


def register_section(text):
    match = re.search(r"(?im)^(#{2,6})\s+(?:\d+[.)]?\s+)?Register craft\b[^\n]*", text)
    if not match:
        return ""
    level = len(match.group(1))
    tail = text[match.end():]
    following = re.search(r"(?m)^#{1," + str(level) + r"}\s+", tail)
    return text[match.start():match.end() + following.start()] if following else text[match.start():]


def craft_features(section):
    return {"register_stratum": bool(re.search(r"(?i)strat(?:um|a)", section)),
            "axis_conditioned": bool(re.search(r"(?i)axis", section) and re.search(r"(?i)deriv", section)),
            "operation_selection": bool(re.search(r"(?i)operation", section) and re.search(r"(?i)select|rule|mark.*reverse|fire.*lengthen", section)),
            "speech_acts": bool(re.search(r"(?i)speech.act|illocution|speaker.*force", section)),
            "replay": bool(re.search(r"(?i)replay", section)),
            "ceiling_constraint": bool(re.search(r"(?i)ceiling", section) and re.search(r"(?i)constraint|domain|limit", section)),
            "label_typing": bool(re.search(r"(?i)label.typ|translated-label|native-form", section)),
            "typed_pipeline": bool(re.search(r"(?i)typed.pipeline|L3b-argot|L1-profile", section))}


def craft_rows(section):
    rows = []
    in_table = False
    for number, line in enumerate(section.splitlines(), 1):
        if not line.lstrip().startswith("|"):
            in_table = False
            continue
        if re.fullmatch(r"[\s|:\-]+", line):
            in_table = True
            continue
        if in_table:
            rows.append({"section_line": number, "cited": bool(PATH_RE.search(line)
                         or re.search(r"\[[^\]]+\]\([^)]*\)|\[[A-Za-z0-9_-]+\]", line))})
    return rows


def executable_inventory(skill):
    paths = sorted(path.relative_to(ROOT).as_posix() for directory in
                   (ROOT / "tools", ROOT / "tools/gates", ROOT / "tools/harness")
                   for path in directory.glob("*.py") if path.is_file())
    unnamed = [relative for relative in paths if relative not in skill]
    return {"paths": paths, "unnamed": unnamed,
            "live_executables": metric(len(paths), "tools, tools/gates, tools/harness Python files"),
            "unnamed_executables": metric(len(unnamed), "exact executable paths absent from SKILL.md")}


def measure_depth(evidence, docs):
    skill = evidence.text("SKILL.md")
    section = register_section(skill)
    features = craft_features(section)
    refs = local_references(section)
    rows = craft_rows(section)
    drafts = []
    for relative, text in docs.items():
        if re.search(r"(?i)draft|synth|skill", relative) and not re.search(r"(?i)audit|review", relative):
            candidate = register_section(text)
            if candidate:
                features_draft = craft_features(candidate)
                drafts.append({"path": relative, "features": features_draft,
                               "passed": all(features_draft.values()) and not local_references(candidate)["missing"]})
    reviewers = [row for row in audit_candidates(
        docs, r"Register craft|register.craft.*synth|synth.*register.craft|craft/skill-draft\.md")
        if "/craft/" in row["path"] or re.search(r"(?i)craft.*review|review.*craft", row["path"])]
    inventory = executable_inventory(skill)
    digest = sha(skill.encode())
    box_reports = []
    for relative, text in docs.items():
        if not re.search(r"(?i)box[-_ ]?1", relative):
            continue
        refs_box = local_references(text)
        bound = bool(section) and digest in text
        box_reports.append({"path": relative, "dated_command": dated_command(text),
                            "names_inventory": bool(re.search(r"(?i)unnamed|executables?|inventory", text)),
                            "post_landing_digest": bound,
                            "references": refs_box,
                            "passed": dated_command(text) and bool(re.search(r"(?i)unnamed|executables?|inventory", text))
                            and bound and not refs_box["missing"]})
    failures = [f"landed Register craft subsection missing {name}" for name, present in features.items() if not present]
    if not section:
        failures.append("SKILL.md has no unified Register craft subsection (orchestrator landing remains required)")
    if not refs["paths"] or refs["missing"]:
        failures.append("Register craft subsection has missing or no resolving repository citations")
    if not rows or any(not row["cited"] for row in rows):
        failures.append("Register craft table has absent or uncited craft rows")
    if not any(row["passed"] for row in drafts):
        failures.append("no complete Register craft synthesis draft landed")
    if sum(row["passed"] for row in reviewers) < 2:
        failures.append("fewer than two dated Register craft reviewer reports with resolving evidence")
    if not any(row["passed"] for row in box_reports):
        failures.append("box-1 executable re-survey has no dated receipt pinned to the post-landing SKILL.md bytes")
    return result(failures, {"synthesis_drafts": drafts, "reviewers": reviewers,
                            "skill_sha256": digest, "landed_features": features,
                            "references": refs, "table_rows": rows, "box1_resurveys": box_reports,
                            "executable_inventory": inventory,
                            "scope_note": "Box 1 is re-surveyed, not automatically promoted; remaining unnamed executables are reported, not silently cleared."})


def dependencies_ready():
    pending = [relative for relative in (RESOLUTION, RETRO) if not safe_path(relative).is_file()]
    md_paths = list(safe_path(ROUND).rglob("*.md"))
    if not any(re.search(r"(?i)audit|review", str(path)) for path in md_paths):
        pending.append(f"{ROUND}/ (independent auditors/reviewers)")
    if not any(re.search(r"(?i)box[-_ ]?1", path.name) for path in md_paths):
        pending.append(f"{ROUND}/ (box-1 re-survey)")
    if not register_section(safe_path("SKILL.md").read_text(encoding="utf-8")):
        pending.append("SKILL.md (orchestrator-owned Register craft landing)")
    if not safe_path(f"{ROUND}/telemetry").is_dir():
        pending.append(f"{ROUND}/telemetry/")
    return pending


def runtime_paths():
    paths = set()
    for directory in ("tools", "examples/culture-d2", "examples/culture-d3", "examples/culture-d4"):
        paths.update(path.relative_to(ROOT).as_posix() for path in safe_path(directory).rglob("*")
                     if path.is_file() and path.suffix in (".py", ".json", ".yml", ".yaml")
                     and "__pycache__" not in path.parts)
    return paths


def measure():
    evidence = Evidence()
    claims = evidence.document(CLAIMS) or {}
    targets = evidence.document(f"{ROUND}/targets.json") or {}
    evidence.text(RUNNER)
    evidence.text("SKILL.md")
    evidence.text("AGENTS.md")
    runtime_before = runtime_paths()
    for relative in sorted(runtime_before):
        evidence.text(relative)
    docs = documents(evidence)
    baseline = claims.get("baseline_revision")
    before = protected_snapshot(baseline)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        regression_future = pool.submit(regressions)
        probe_future = pool.submit(law_probes, evidence)
        runs, probes = regression_future.result(), probe_future.result()
    after = protected_snapshot(baseline)
    preservation = result(before["failures"] + after["failures"], {"before": before, "after": after})
    results = {}
    for claim_id, operation in (
            ("O", lambda: measure_operability(evidence, claims, docs, runs, probes, preservation)),
            ("C", lambda: measure_calibration(evidence, docs)),
            ("D", lambda: measure_depth(evidence, docs))):
        try:
            results[claim_id] = operation()
        except (OSError, ValueError, TypeError, KeyError, RuntimeError, AttributeError, subprocess.SubprocessError) as error:
            results[claim_id] = result([f"could-not-evaluate: {type(error).__name__}: {error}"], {})
    coherence = []
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"O": "operability", "C": "calibration", "D": "depth"}:
        coherence.append("declared claims must be O/operability, C/calibration, D/depth")
    if claims.get("round") != 30 or targets.get("round") != 30 or targets.get("baseline_revision") != baseline:
        coherence.append("claims and targets disagree on round or baseline")
    if sum(targets.get("workers", {}).values()) != claims.get("workers"):
        coherence.append("target worker allocation does not sum to the declared wave")
    runtime_after = runtime_paths()
    if runtime_before != runtime_after:
        coherence.append("runtime input path set changed during measurement: "
                         + ", ".join(sorted(runtime_before ^ runtime_after)))
    changed = []
    for relative, digest in evidence.inputs.items():
        try:
            observed = sha(safe_path(relative).read_bytes())
        except (OSError, ValueError):
            observed = None
        if observed != digest:
            changed.append(relative)
    if changed:
        coherence.append("evidence changed during measurement: " + ", ".join(sorted(changed)))
    coherence.extend(evidence.errors)
    failures = [f"claim {claim_id}: {failure}" for claim_id, item in results.items() for failure in item["failures"]]
    failures.extend("evidence: " + failure for failure in coherence)
    return {"round": 30, "runner": RUNNER, "runner_sha256": evidence.inputs.get(RUNNER),
            "counting_command": COMMAND, "date": today(), "measured_at_utc": now(),
            "baseline_revision": baseline, "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results, "failures": failures,
            "missing_dependencies": sorted(evidence.missing | set(dependencies_ready())),
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": ["Read-only evidence checks and actual CLI controls, not a canon or promotion decision.",
                       "No historical acceptance runner is launched; rounds 8-29 are checked against the declared Git baseline.",
                       "Every regression and law tamper command is recorded with date, exit and captured output. Validator controls auto-clean under .scratch; the replay selftest uses authorized /var/tmp mirror-safety storage.",
                       "Textual retrospective/craft coverage checks are backed by independent auditor reports; they do not independently certify the merits of every prose claim.",
                       "A documented route needs owner + reason and evidence; it is not mislabeled as a verified fix.",
                       "In-flight evidence changes invalidate acceptance; rerun after the orchestrator finishes landing."]}


def selftest():
    checks = []
    def check(name, value):
        checks.append({"control": name, "passed": bool(value)})
    def raises(function, *args):
        try:
            function(*args)
        except (ValueError, TypeError):
            return True
        return False
    check("duplicate-json-key-refused", raises(strict_json, '{"id": 1, "id": 2}'))
    check("absolute-path-refused", raises(safe_path, "/var/tmp/a"))
    check("traversal-path-refused", raises(safe_path, "reports/../a"))
    check("git-path-refused", raises(safe_path, ".git/config"))
    check("normal-path-accepted", safe_path(CLAIMS) == ROOT / CLAIMS)
    check("finding-prefix-required", law_findings("D4L-LAW-SPEAKER: prose") == [])
    check("saturated-class-line-delta", set(law_findings("FINDING D4L-LAW-SPEAKER: one\nFINDING D4L-LAW-SPEAKER: two"))
          - set(law_findings("FINDING D4L-LAW-SPEAKER: one")) == {"FINDING D4L-LAW-SPEAKER: two"})
    fixture = ('other:\n  speaker: "unchanged"\nregister_law:\n  -\n    id: "RGL-01"\n'
               '    speaker: "good (RK-03)"\n    force: "directive-binding"\nafter:\n  speaker: "unchanged-too"\n')
    mutated = mutate_law(fixture, "speaker", '"nobody-nowhere"')
    check("tokenless-tamper-changes-one-law-field", mutated.count('speaker: "nobody-nowhere"') == 1)
    check("tamper-does-not-touch-another-block", 'speaker: "unchanged"' in mutated and 'speaker: "unchanged-too"' in mutated)
    check("missing-field-tamper-refused", raises(mutate_law, fixture, "missing", "a"))
    check("missing-law-block-refused", raises(mutate_law, "other: value\n", "speaker", "a"))
    check("append-only-amendment-accepted", append_only_amendment("one\ntwo\n", "one\ntwo\n## Amendment\n"))
    check("rewritten-history-refused", not append_only_amendment("one\ntwo\n", "one\nchanged\n## Amendment\n"))
    check("identical-not-an-amendment", not append_only_amendment("one\n", "one\n"))
    check("all-five-route-families-exact", [classify_route({"id": token}) for token in
          ("QREG-dangles", "law-battery", "X63-F2", "speaker-tail", "telemetry-durability")]
          == [[name] for name in ROUTES])
    check("empty-queue-refused", not validate_resolution({"items": []}, {})["passed"])
    check("unknown-status-refused", route_status({"status": "verified-ish"}) is None)
    check("documented-not-fixed", route_status({"status": "documented"}) == "documented")
    check("control-without-command-refused", not dated_command("2026-10-18 control passed"))
    check("command-without-date-refused", not dated_command("python3 tool.py --selftest"))
    check("dated-command-recognized", dated_command("2026-10-18 python3 tool.py --selftest"))
    check("empty-retrospective-refused", not all(retrospective_features("").values()))
    check("future-rounds-not-implicitly-observed", not retrospective_features("rounds 8-32")["future_rounds_not_results"])
    section = "### Register craft\n| Rule | Citation |\n|---|---|\n| x | `tools/check-gate-battery.py` |\n#### Detail\nbody\n### Next\nnot included\n"
    check("register-subsection-boundary", "not included" not in register_section(section) and "Detail" in register_section(section))
    check("unified-subsection-must-be-named", register_section("### Derivation replay\nbody") == "")
    check("cited-table-row-detected", craft_rows(register_section(section)) == [{"section_line": 4, "cited": True}])
    check("uncited-table-row-refused", craft_rows("| A | B |\n|---|---|\n| x | y |\n")[0]["cited"] is False)
    check("empty-battery-refused", not battery_check({"exit_code": 0, "stdout": "{}"})["passed"])
    check("protected-round29-included", "reports/round-29" in PROTECTED)
    check("current-round-not-protected", "reports/round-30" not in PROTECTED)
    nested = 'register_law:\n  -\n    design_row:\n      - "QREG-05"\n      - "QREG-07"\n    speaker: "stamp-holder"\n'
    changed = mutate_law(nested, "design_row", "[QREG-99]")
    check("nested-design-row-list-replaced-as-one-field", "QREG-05" not in changed and "QREG-07" not in changed
          and 'design_row: [QREG-99]\n    speaker: "stamp-holder"' in changed)
    check("route-id-not-contaminated-by-control-description",
          classify_route({"id": "R30-LAW-BATTERY", "summary": "QREG and speaker controls"}) == ["law-battery"])
    queue = [{"id": name, "status": "fixed-with-control", "evidence": [CLAIMS],
              "control": "paired positive and negative", "date": "2026-10-18", "command": COMMAND}
             for name in ROUTES]
    check("complete-five-route-queue-accepted", validate_resolution({"resolutions": queue}, {})["passed"])
    check("missing-route-refused", not validate_resolution({"resolutions": queue[:-1]}, {})["passed"])
    check("duplicate-route-refused", not validate_resolution({"resolutions": queue[:-1] + [queue[0]]}, {})["passed"])
    no_control = [{key: value for key, value in row.items() if key != "control"} for row in queue]
    check("fix-without-control-refused", not validate_resolution({"resolutions": no_control}, {})["passed"])
    documented = [{**row, "status": "documented", "owner": "operator", "reason": "explicit bounded dependency"}
                  for row in queue]
    check("five-owned-documented-routes-accepted", validate_resolution(documented, {})["passed"])
    check("documented-route-without-owner-refused", not validate_resolution(
        [{key: value for key, value in row.items() if key != "owner"} for row in documented], {})["passed"])
    check("round-template-not-positive-evidence", local_references("reports/round-N/run-validation.py")["templates"]
          == ["reports/round-N/run-validation.py"])
    missing_path = "reports/round-30/__x33_missing_control__.json"
    check("undisclosed-missing-positive-citation-refused", local_references(missing_path)["missing"] == [missing_path])
    check("disclosed-absence-not-a-positive-citation", local_references(missing_path + " is absent")["declared_absent"] == [missing_path])
    fake_battery = {"gate": "register-law-gate.py", "summary": {"pass": 7, "fail": 0, "unevaluable": 0},
                    "baselines": {"summary": {"coverage": "10/10", "pinned": 10, "baselines_found": 10,
                                               "gates_uncovered": []}}}
    check("ten-covered-pinned-gates-accepted", battery_check({"exit_code": 0, "stdout": json.dumps(fake_battery)})["passed"])
    fake_battery["baselines"]["summary"]["coverage"] = "9/10"
    check("nine-of-ten-is-not-complete", not battery_check({"exit_code": 0, "stdout": json.dumps(fake_battery)})["passed"])
    fake_battery["baselines"]["summary"]["coverage"] = "10/10"
    fake_battery["baselines"]["summary"]["gates_uncovered"] = ["register-law-gate.py"]
    check("coverage-label-cannot-hide-uncovered-law", not battery_check({"exit_code": 0, "stdout": json.dumps(fake_battery)})["passed"])
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
    parser.add_argument("--wait", type=int, default=0, metavar="SECONDS", help="poll late dependencies every 60s, at most 1200s")
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
        deadline = time.monotonic() + min(args.wait, 1200)
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
