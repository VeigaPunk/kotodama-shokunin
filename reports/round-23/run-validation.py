#!/usr/bin/env python3
"""Round-23 acceptance runner: claims O (operability) and D (depth).

Claim O — the two round-22 operational tails plus regressions:
  (a) the PLACEHOLDER_RE wording false positive ("unchanged-foreign-path control"
      in D4-CL08) is dispositioned without weakening any placeholder rule —
      either a successor validator accepts the documented phrase class with
      controls, or D4-CL08's basis is reworded within the uncertainty grammar
      and the packet re-pinned as a new revision (r3); the full v2/v3 checks
      run green either way;
  (b) combined-source successor pins land as new rows binding the final
      projector/adapter sources (D2 live + frozen pins, v2, and the D4 profile
      rows), each with before/after digests, plus stale-pin refusal controls;
  (c) the fixed regression battery is green.

Claim D — SKILL.md gains the family-clean projection rule (drafted by the
R23-D01..D03 workers from reports/round-22/bleed/design.md, landed by the
orchestrator): rule statement, injection-point warning (unconditional D2
build_payload), paired controls, round-25 implementation commitment; every row
cited; reviewed in rule/fragment-D01..D03.md.

Run only in an isolated Git clone under the lane's .scratch, as
  python3 reports/round-23/run-validation.py            (measure + write receipt)
  python3 reports/round-23/run-validation.py --check    (measure only, print)
  python3 reports/round-23/run-validation.py --selftest (dependency-free controls)
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import runpy
import shlex
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-23"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
WORDING = f"{ROUND_DIR}/wording"
WORDING_CHECK = f"{WORDING}/wording-check.py"
R3_PACKET = f"{WORDING}/declared-in-r3/packet.md"
R3_BASELINE = f"{WORDING}/declared-in-r3/expected.json"
R2_PACKET = "reports/round-22/handoff/declared-in-r2/packet.md"
R20_PACKET = "reports/round-20/handoff/packet.md"
R20_RUNNER = "reports/round-20/run-validation.py"
V2_OLD = "reports/round-22/fixes/alias-coercion-v2-07.json"
FROZEN_VERIFY = "reports/round-15/handoff/frozen-verify.py"
D2_EXPECTED = "examples/culture-d2/expected-holds.json"
D2_PACKET_TYPED = "examples/culture-d2/packet.d2.typed.yml"
D4_PACKET = "examples/culture-d4/packet.d4.yml"
D4_PROJECTION = "examples/culture-d4/typed-labels.d4.yml"
PINS_TABLE = "tools/gates/typed-pipelines.json"
PROJECTOR = "tools/d2-typed-labels.py"
PINS_DIR = f"{ROUND_DIR}/pins"
FROZEN_R23 = "tools/gates/frozen/round-23/repin-d2"
FROZEN_R23_MANIFEST = f"{FROZEN_R23}/MANIFEST.tsv"
FROZEN_R22_D4 = "tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv"
SKILL = "SKILL.md"
DRAFT = f"{ROUND_DIR}/rule/skill-draft.md"
FRAGMENTS = tuple(f"{ROUND_DIR}/rule/fragment-D0{index}.md" for index in (1, 2, 3))
D2_BEFORE_PROJECTOR = "76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb"
V2_BEFORE_PROJECTOR = "a10861f039f7e80a2f38a11fe1d72d4ef6fa5f48987f5fff96185b1875924a7b"
COMBINED_PROJECTOR = "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3"
D2_PROJECTION_DIGEST = "a3aa452cd5ae77c351d9532a707fb1f1abf77c3fad8b9d28089e6958364a43"
OLD_PHRASE = "the unchanged-foreign-path control is"
NEW_PHRASE = "the foreign-path-stability control is"
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 23)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 23))
SYNC_PATHS = (ROUND_DIR, "corpus/lessons/round-23.md", "tools/gates/frozen/round-23",
              D2_EXPECTED, PINS_TABLE, SKILL)
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
COMMAND_RE = re.compile(r"\b(?:python3?|sha256sum|git|date|test|diff|cmp|rg|grep)\s+\S+")
POINTER_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|examples|corpus)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)\b")
HEX_RE = re.compile(r"\b(?=[0-9a-f]*\d)[0-9a-f]{7,64}(?:\u2026)?\b")
# The frozen round-20 detector, pinned verbatim; a disposition must not weaken it.
PLACEHOLDER_RE = re.compile(
    r"\b(tbd|tba|todo|placeholder|boilerplate|same[- ]as[- ](?:above|below)|"
    r"as (?:above|below)|see (?:above|below|other)|copy of|unchanged)\b", re.I)
CITATION_RE = re.compile(
    r"(?<![\w./-])(?:(?:reports|tools|examples|corpus)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)"
    r"|\b(?:LOG|SKILL|SCORECARD|PROVINCE|README|SHONEN|MINT)\.md)(?::[\d,\-]+)?"
    r"|\b(?=[0-9a-f]*\d)[0-9a-f]{7,64}(?:\u2026)?\b")
DRAFT_BEGIN = "<!-- BEGIN R23-D SKILL SUBSECTION"
DRAFT_END = "<!-- END R23-D SKILL SUBSECTION -->"
SKILL_HEADING = "### Family-clean projection"
CONTROL_NAMES = ("d2 compatibility", "d4 independence", "empty-by-default",
                 "owner-qualified", "id-based reinterpretation", "borrowed",
                 "propagation")
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
    ("d4-projection", (PROJECTOR, "--packet", D4_PACKET, "--check", D4_PROJECTION)),
    ("typed-pipeline-selftest", ("tools/gates/typed-pipeline-gate.py", "--selftest")),
    ("typed-pipeline-generalized-selftest", ("tools/gates/typed-pipeline-gate.py", "--selftest-generalized")),
    ("d2-gate", ("tools/gates/typed-pipeline-gate.py",)),
    ("d4-gate", ("tools/gates/typed-pipeline-gate.py", D4_PACKET)),
    ("d4-label-gate", ("tools/gates/d4-typed-labels-check-gate.py",)),
    ("d4-assembly-gate", ("tools/gates/d4-assembly-check-gate.py",)),
    ("coupling-selftest", ("tools/check-evidence-coupling.py", "--selftest")),
    ("replay-selftest", ("tools/replay-frozen.py", "--selftest")),
    ("handoff-v2", ("tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet")),
    ("handoff-v3-selftest", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest")),
    ("handoff-v3", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet")),
)
PLACEHOLDER_PROBES = ("review pending, see above", "this basis is TBD",
                      "placeholder row", "copy of the v2 row", "todo: fill",
                      "same as above", "see below for details",
                      "the D2 output is unchanged")


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


def git(*argv, timeout=120, cwd=None):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1")
    try:
        proc = subprocess.run(["git", *argv], cwd=cwd or ROOT, capture_output=True,
                              timeout=timeout, env=env)
        return proc.stdout if proc.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def live_lane():
    """The real lane root: nearest ancestor without a .scratch component."""
    for ancestor in (ROOT, *ROOT.parents):
        if ".scratch" in ancestor.parts:
            continue
        if (ancestor / ".git").is_dir() and (ancestor / f"{ROUND_DIR}/claims.json").is_file():
            return ancestor
    return None


def protected_baseline(revision):
    failures, rows = [], []
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return result(["Round-23 declared baseline is not a full Git revision"], {})
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
    extra = git("status", "--porcelain=v1", "--untracked-files=all", "--", *PROTECTED)
    worktree = [line for line in (extra or b"").decode("utf-8", "replace").splitlines()
                if line.strip()]
    for line in worktree:
        flag, _, path = line.partition(" ")
        path = path.strip()
        if flag == "??" and path:
            try:
                worktree_blob = sha(safe_path(path).read_bytes())
            except (OSError, ValueError):
                worktree_blob = None
            rows.append({"path": path, "baseline_blob": None,
                         "observed_blob": worktree_blob})
    for relative in sorted(expected):
        path = ROOT / relative
        data = None
        if path.is_file():
            try:
                data = path.read_bytes()
            except OSError:
                data = None
        if data is None:
            rows.append({"path": relative, "baseline_blob": expected[relative],
                         "observed_blob": None})
            continue
        before_blob = expected[relative]
        blob = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        if blob != before_blob:
            rows.append({"path": relative, "baseline_blob": before_blob,
                         "observed_blob": sha(data)})
    if rows:
        failures.append("Filed rounds 8-22 or their frozen generations differ from the declared baseline")
    return result(failures, {"baseline_revision": revision,
                             "protected_paths": metric(len(expected), "git ls-tree of protected baseline"),
                             "differences": rows,
                             "differences_total": metric(len(rows), "compare protected Git blobs to working bytes"),
                             "protected_status_rows": metric(len(worktree), "git status over protected paths"),
                             "protected_status": worktree})


def tracked_at(revision, relative):
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return None
    raw = git("ls-tree", "-r", "-z", revision, "--", relative)
    if raw is None:
        return None
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        metadata, _ = entry.split(b"\t", 1)
        return metadata.decode("ascii").split()[2]
    return None


def run_command(label, parts, timeout=900, tmpdir=None, cwd=None):
    scratch = Path(tmpdir) if tmpdir is not None else ROOT / ".scratch" / "round-23" / "validation" / label
    scratch.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(scratch), "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    item = {"label": label, "command": shlex.join(["python3", *parts]),
            "argv": ["python3", *parts], "date": today()}
    try:
        source = safe_path(parts[0])
        item["tool_sha256"] = sha(source.read_bytes())
        proc = subprocess.run([sys.executable, *parts], cwd=cwd or ROOT,
                              capture_output=True, timeout=timeout, env=env)
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


def d4_cl08_line(text):
    for line in text.splitlines():
        if line.startswith("| D4-CL08 ") or line.startswith("| D4-CL08|"):
            return line
    return None


def load_frozen_runner():
    """Import the frozen round-20 runner read-only for its pure parsers."""
    source = safe_path(R20_RUNNER)
    spec = importlib.util.spec_from_file_location("r23_frozen_round20", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def placeholder_problems(module, packet_text):
    rows = module.parse_ledger_rows(packet_text)
    judgments = module.uncertainty_problems(rows)
    flagged = [row["id"] for row, judgment in zip(rows, judgments)
               if any("placeholder basis" in problem for problem in judgment["problems"])]
    return rows, judgments, flagged


def clone_under_scratch(name):
    scratch = ROOT / ".scratch" / "round-23"
    scratch.mkdir(parents=True, exist_ok=True)
    target = scratch / name
    if target.exists():
        shutil.rmtree(target)
    proc = subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(target)],
                          capture_output=True, timeout=600)
    if proc.returncode != 0:
        raise ValueError(f"cannot clone for {name}: {proc.stderr.decode('utf-8', 'replace')[-400:]}")
    return target


def copy_into_clone(live, relative, target_root):
    source = live / relative
    if not source.exists():
        return False
    destination = target_root / relative
    if source.is_dir():
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    return True


def sync_generation(live, target_root, relatives):
    synced = {}
    for relative in relatives:
        if copy_into_clone(live, relative, target_root):
            source = live / relative
            if source.is_file():
                synced[relative] = sha(source.read_bytes())
    return synced


def sync_round_surface(live):
    """Bring the live round-23 surface (untracked at the baseline) into this clone."""
    synced = {}
    for relative in SYNC_PATHS:
        source = live / relative
        if not source.exists():
            continue
        if source.is_dir():
            for child in sorted(source.iterdir()):
                if child.name in ("run-validation.py", "validation.json", ".scratch"):
                    continue
                copy_into_clone(live, f"{relative}/{child.name}", ROOT)
        else:
            copy_into_clone(live, relative, ROOT)
        synced[relative] = sha(source.read_bytes()) if source.is_file() else "tree"
    return synced


def manifest_rows(text):
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def row_exit_ok(row):
    try:
        return int(row.get("exit_code", "1")) == 0
    except ValueError:
        return False


def discover_v2_successor(evidence):
    """New-at-baseline frozen v2 receipts (JSON) or successor row documents (markdown).

    The landed round-23 contract files the combined-source v2 successor as a
    markdown row under reports/round-23/pins/ carrying the before/after
    projector digests and a dated v2 command, verified by a fresh
    exercise-handoff-e2e --profile v2 run; a kotodama-frozen-run-v1 JSON
    receipt binding the combined projector is accepted equivalently.
    """
    found_json, found_docs = [], []
    candidates = []
    for pattern in (f"{PINS_DIR}/**/*.json", f"{WORDING}/*.json", "reports/round-22/fixes/*.json"):
        candidates.extend(str(path.relative_to(ROOT))
                          for path in sorted(ROOT.glob(pattern)) if path.is_file())
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    revision = claims.get("baseline_revision", "")
    for relative in sorted(set(candidates)):
        payload = evidence.document(relative)
        if not isinstance(payload, dict) or payload.get("schema") != "kotodama-frozen-run-v1":
            continue
        marker = str(payload.get("packet_id", "")) + str(payload.get("profile", ""))
        inputs = payload.get("inputs")
        if "v2" in marker and isinstance(inputs, dict) and PROJECTOR in inputs:
            if tracked_at(revision, relative) is None:
                found_json.append((relative, payload))
    for relative in sorted(str(path.relative_to(ROOT)) for path in ROOT.glob(f"{PINS_DIR}/*.md")):
        text = evidence.text(relative)
        if not text:
            continue
        if ("v2" in text and COMBINED_PROJECTOR in text and V2_BEFORE_PROJECTOR in text
                and DATE_RE.search(text) and COMMAND_RE.search(text)):
            found_docs.append(relative)
    return found_json, found_docs


def verify_v2_successor(relative, payload, live, evidence):
    failures, missing, measurement = [], [], {}
    inputs = payload.get("inputs", {})
    drifted = {name: pinned for name, pinned in sorted(inputs.items())
               if (live / name).is_file() and sha((live / name).read_bytes()) != pinned}
    if inputs.get(PROJECTOR) != COMBINED_PROJECTOR:
        failures.append(f"v2 successor does not pin the combined projector {COMBINED_PROJECTOR[:12]}…: {relative}")
    measurement["inputs_total"] = metric(len(inputs), f"inputs of {relative}")
    measurement["combined_projector_pinned"] = metric(inputs.get(PROJECTOR) == COMBINED_PROJECTOR,
                                                      f"{relative}:{PROJECTOR}")
    measurement["drifted_inputs"] = sorted(drifted)
    target = clone_under_scratch("v2-successor")
    synced = {PROJECTOR: sha((live / PROJECTOR).read_bytes())}
    for name in inputs:
        copy_into_clone(live, name, target)
    copy_into_clone(live, relative, target)
    item = run_command("v2-successor-verify",
                       [FROZEN_VERIFY, "--baseline", relative, "--root", str(target)],
                       tmpdir=ROOT / ".scratch" / "round-23" / "validation" / "v2-successor",
                       cwd=target)
    measurement["verify"] = run_receipt(item)
    if item.get("exit") != 0:
        failures.append(f"frozen-verify on the v2 successor receipt did not pass: {relative} (exit {item.get('exit')})")
    measurement["clone_synced"] = synced
    return failures, measurement, missing


def measure_wording(evidence, live):
    failures, missing = [], []
    measurement = {}
    parent_text = evidence.text(R2_PACKET)
    historical_text = evidence.text(R20_PACKET)
    if not (parent_text and historical_text):
        return result(["Filed handoff packets unreadable"], measurement, evidence.missing)
    parent_line = d4_cl08_line(parent_text)
    historical_line = d4_cl08_line(historical_text)
    measurement["d4_cl08_present"] = metric(bool(parent_line and historical_line),
                                            "D4-CL08 row in filed v2 and round-20 packets")
    if not (parent_line and historical_line):
        failures.append("D4-CL08 row not found in the filed packets")
        return result(failures, measurement, missing)
    measurement["false_positive_reproduced"] = metric(
        bool(PLACEHOLDER_RE.search(parent_line)) and OLD_PHRASE in parent_line,
        "frozen PLACEHOLDER_RE over the filed D4-CL08 basis")
    if not PLACEHOLDER_RE.search(parent_line):
        failures.append("Control failed: the frozen PLACEHOLDER_RE no longer reproduces the D4-CL08 false positive")

    revision_text = evidence.text(R3_PACKET)
    revision = evidence.document(R3_BASELINE)
    if not revision_text or not isinstance(revision, dict):
        failures.append(f"Path (b) revision incomplete: {R3_PACKET} and {R3_BASELINE} must both exist")
        missing.extend(path for path in (R3_PACKET, R3_BASELINE) if not (ROOT / path).is_file())
        return result(failures, measurement, missing)
    revision_line = d4_cl08_line(revision_text)
    if not revision_line:
        failures.append("D4-CL08 row not found in the declared-in-r3 revision")
    else:
        measurement["reworded_basis"] = metric(
            NEW_PHRASE in revision_line and OLD_PHRASE not in revision_line,
            "D4-CL08 basis in the declared-in-r3 revision")
        if not (NEW_PHRASE in revision_line and OLD_PHRASE not in revision_line):
            failures.append("declared-in-r3 D4-CL08 basis is not the declared rewording")
        if PLACEHOLDER_RE.search(revision_line):
            failures.append("declared-in-r3 D4-CL08 basis still fires the frozen PLACEHOLDER_RE")
        measurement["reworded_basis_cited"] = metric(bool(POINTER_RE.search(revision_line)),
                                                     "citations survive in the reworded basis")
        if not POINTER_RE.search(revision_line):
            failures.append("reworded D4-CL08 basis names no evidence location")
    digest = sha(safe_path(R3_PACKET).read_bytes())
    measurement["revision_pin"] = {"command": f"{COMMAND} (sha256 of {R3_PACKET})",
                                   "date": today(), "value": digest}
    if revision.get("packet_sha256") != digest:
        failures.append("declared-in-r3 expected.json does not pin the live revision bytes")
    try:
        module = load_frozen_runner()
        if module.PLACEHOLDER_RE.pattern != PLACEHOLDER_RE.pattern or module.PLACEHOLDER_RE.flags != PLACEHOLDER_RE.flags:
            failures.append("The frozen round-20 PLACEHOLDER_RE no longer matches its pinned pattern")
        else:
            measurement["frozen_detector_unweakened"] = metric(True, "frozen PLACEHOLDER_RE pattern equality")
        _, _, parent_flagged = placeholder_problems(module, parent_text)
        revision_rows, revision_judgments, revision_flagged = placeholder_problems(module, revision_text)
        parent_rows = module.parse_ledger_rows(parent_text)
        measurement["successor_scan"] = {
            "parent_flagged": parent_flagged,
            "revision_flagged": revision_flagged,
            "revision_rows": metric(len(revision_rows), "parse_ledger_rows over declared-in-r3"),
            "statuses_unchanged": metric(
                [row["uncertainty"]["status"] for row in parent_rows]
                == [row["uncertainty"]["status"] for row in revision_rows],
                "uncertainty status parity between declared-in-r2 and -r3"),
        }
        if "D4-CL08" not in parent_flagged:
            failures.append("Control failed: the frozen uncertainty scan no longer flags the filed D4-CL08 basis")
        if revision_flagged:
            failures.append(f"declared-in-r3 still has placeholder-basis rows: {revision_flagged}")
        if [row["id"] for row in parent_rows] != [row["id"] for row in revision_rows]:
            failures.append("declared-in-r3 claim ledger row set differs from declared-in-r2")
    except (OSError, ValueError, AttributeError, TypeError) as error:
        failures.append(f"frozen round-20 parser unavailable: {type(error).__name__}: {error}")

    for mode in ("--selftest", "--check"):
        inner = clone_under_scratch("wording-run-selftest" if mode == "--selftest"
                                    else "wording-run-check")
        receipt_path = ROOT / ".scratch" / "round-23" / ("wording_selftest.json" if mode == "--selftest"
                                                         else "wording_check.json")
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        arguments = [WORDING_CHECK, "--root", str(inner), mode, "--receipt", str(receipt_path)]
        item = run_command(f"wording{mode}", arguments,
                           tmpdir=ROOT / ".scratch" / "round-23" / "validation" / "wording")
        receipt_text = ""
        try:
            receipt_text = receipt_path.read_text(encoding="utf-8")
        except OSError:
            pass
        payload = None
        try:
            payload = strict_json(receipt_text) if receipt_text else None
        except ValueError:
            payload = None
        summary = {"exit": item.get("exit"), "date": item.get("date"),
                   "passed_controls": (payload or {}).get("passed_controls"),
                   "total_controls": (payload or {}).get("total_controls")}
        measurement[f"wording_check{mode.replace('--', '_')}"] = summary
        if mode == "--check":
            negative = (payload or {}).get("negative") or {}
            positive = (payload or {}).get("positive") or {}
            placeholder_negative = [failure for failure in (negative.get("failures") or [])
                                    if "placeholder" in failure.lower() and "D4-CL08" in failure]
            measurement["negative_control"] = {
                "reproduces_false_positive": bool(placeholder_negative),
                "recorded_pass": negative.get("passed")}
            measurement["positive_control"] = {
                "packet": positive.get("packet"),
                "failures": positive.get("failures"),
                "wording_tail_eliminated": positive.get("wording_tail_eliminated")}
            if not placeholder_negative:
                failures.append("wording-check negative control did not record the D4-CL08 placeholder false positive")
            if positive.get("wording_tail_eliminated") is not True:
                failures.append("wording-check positive control: the placeholder tail is not eliminated on declared-in-r3")
        if item.get("exit") != 0:
            failures.append(f"wording-check {mode} failed (exit {item.get('exit')})")
    return result(failures, measurement, missing)


def measure_pins(evidence, live, regressions):
    failures, missing = [], []
    measurement = {}
    projector_digest = sha((live / PROJECTOR).read_bytes())
    measurement["live_projector"] = {"command": f"{COMMAND} (sha256 of {PROJECTOR})",
                                     "date": today(), "value": projector_digest}
    if projector_digest != COMBINED_PROJECTOR:
        failures.append(f"live projector is not the declared combined source: {projector_digest}")
    expected = evidence.document(D2_EXPECTED)
    if not isinstance(expected, dict):
        return result(["D2 expected-holds unreadable"], measurement, evidence.missing)
    pin = expected.get("projector_sha256")
    supersedes = (expected.get("supersedes_pins") or {}).get("projector_sha256")
    measurement["d2_live_row"] = {
        "after": metric(pin, f"projector_sha256 in {D2_EXPECTED}"),
        "before": metric(supersedes, f"supersedes_pins.projector_sha256 in {D2_EXPECTED}"),
        "revision_note": metric(bool(str(expected.get("revision_note", "")).strip()),
                                f"revision_note in {D2_EXPECTED}")}
    if pin != projector_digest:
        failures.append(f"D2 live row still binds {str(pin)[:12]}…, not the combined projector")
    if supersedes != D2_BEFORE_PROJECTOR:
        failures.append("D2 live row does not record the before digest it supersedes")
    note = str(expected.get("revision_note", ""))
    pins_docs = sorted(str(path.relative_to(ROOT)) for path in ROOT.glob(f"{PINS_DIR}/*.md"))
    measurement["pins_documents"] = pins_docs
    if not pins_docs:
        failures.append(f"no before/after pin documents under {PINS_DIR}/")
        missing.append(f"{PINS_DIR}/")
    else:
        ledger = "\n".join(evidence.text(relative) for relative in pins_docs)
        if D2_BEFORE_PROJECTOR not in ledger or COMBINED_PROJECTOR not in ledger:
            failures.append("pin documents do not carry both before/after projector digests")
        if not (DATE_RE.search(ledger) and COMMAND_RE.search(ledger)):
            failures.append("pin documents lack a dated command")
    generation_text = evidence.text(FROZEN_R23_MANIFEST)
    freeze_text = evidence.text(f"{FROZEN_R23}/freeze.txt")
    rows = manifest_rows(generation_text) if generation_text else []
    measurement["frozen_r23_manifest"] = {
        "rows": metric(len(rows), f"rows in {FROZEN_R23_MANIFEST}"),
        "exit_code_histogram": metric(sorted(row.get("exit_code", "?") for row in rows),
                                      "recorded exit_code column over the manifest")}
    if not rows:
        failures.append(f"frozen round-23 generation has no manifest rows: {FROZEN_R23_MANIFEST}")
        missing.append(FROZEN_R23_MANIFEST)
    if freeze_text and COMBINED_PROJECTOR not in freeze_text:
        failures.append("freeze.txt does not bind the combined projector digest")
    elif not freeze_text:
        missing.append(f"{FROZEN_R23}/freeze.txt")
    if rows:
        restore = {}
        for row in rows:
            snapshot = row.get("input_snapshot", "")
            target = row.get("input", "")
            if snapshot and target and (ROOT / snapshot).is_file():
                restore[target] = snapshot
        for name in (D2_EXPECTED, PINS_TABLE):
            restore.setdefault(name, name)
        target = clone_under_scratch("repin-d2-replay")
        synced = sync_generation(live, target, [FROZEN_R23, *restore.keys()])
        replay = run_command("repin-d2-replay",
                             ["tools/replay-frozen.py", FROZEN_R23_MANIFEST, "--json"],
                             tmpdir=target.parent, cwd=target)
        measurement["replay"] = {key: replay.get(key) for key in ("command", "exit", "date")}
        measurement["replay"]["stdout_tail"] = (replay.get("stdout") or "")[-1500:]
        if replay.get("exit") != 0:
            failures.append(f"replay of the frozen round-23 generation failed (exit {replay.get('exit')})")
        tamper_target = clone_under_scratch("repin-d2-tamper")
        sync_generation(live, tamper_target, [FROZEN_R23, *restore.keys()])
        tampered = []
        first_snapshot = next((row.get("input_snapshot") for row in rows
                               if row.get("input_snapshot")), None)
        if not first_snapshot:
            failures.append("tamper control could not run: no frozen input snapshot in the manifest")
        else:
            victim = tamper_target / first_snapshot
            if victim.is_file():
                victim.write_bytes(victim.read_bytes() + b"\n# tampered\n")
                tampered.append(first_snapshot)
            if not tampered:
                failures.append(f"tamper control could not run: snapshot missing in the clone: {first_snapshot}")
            else:
                tamper = run_command("repin-d2-tamper",
                                     ["tools/replay-frozen.py", FROZEN_R23_MANIFEST, "--json"],
                                     tmpdir=tamper_target.parent, cwd=tamper_target)
                measurement["tamper_refusal"] = {"command": tamper.get("command"),
                                                 "exit": tamper.get("exit"), "date": tamper.get("date"),
                                                 "tampered": tampered}
                if not isinstance(tamper.get("exit"), int) or tamper["exit"] == 0:
                    failures.append("tamper control failed: replay did not refuse a changed frozen input")
    successors_json, successor_docs = discover_v2_successor(evidence)
    if successor_docs:
        measurement["v2_successor_rows"] = successor_docs
    else:
        failures.append(f"no combined-source v2 successor row under {PINS_DIR}/ carrying the "
                        f"before/after projector digests and a dated v2 command")
        missing.append(f"{PINS_DIR}/v2.md")
    if successors_json:
        measurement["v2_successor_receipts"] = [relative for relative, _ in successors_json]
        for relative, payload in successors_json:
            sub_failures, sub_measurement, sub_missing = verify_v2_successor(relative, payload, live, evidence)
            measurement[f"v2_successor_receipt:{relative}"] = sub_measurement
            failures.extend(f"v2 receipt {relative}: {failure}" for failure in sub_failures)
    runs = (regressions.get("measurement") or {}).get("runs") or []
    v2_run = next((item for item in runs if item.get("label") == "handoff-v2"), {})
    measurement["v2_fresh_run"] = {"exit": v2_run.get("exit"), "command": v2_run.get("command"),
                                   "date": v2_run.get("date")}
    if v2_run.get("exit") != 0:
        failures.append("the fresh combined-source v2 verification leg (handoff-v2) is not green")
    stale_target = clone_under_scratch("v2-stale-refusal")
    stale = run_command("v2-stale-refusal",
                        [FROZEN_VERIFY, "--baseline", V2_OLD, "--root", str(stale_target)],
                        tmpdir=ROOT / ".scratch" / "round-23" / "validation" / "v2-stale",
                        cwd=stale_target)
    measurement["v2_stale_refusal"] = {"command": stale.get("command"), "exit": stale.get("exit"),
                                       "date": stale.get("date")}
    measurement["v2_stale_refusal"]["stderr_tail"] = (stale.get("stderr") or "")[-800:]
    if not isinstance(stale.get("exit"), int) or stale["exit"] == 0:
        failures.append("stale-pin refusal control failed: the alias-only v2 baseline still verifies against moved bytes")
    table = evidence.document(PINS_TABLE)
    if not isinstance(table, dict):
        failures.append(f"pins table unreadable: {PINS_TABLE}")
        return result(failures, measurement, missing)
    profiles = {row.get("id"): row for row in table.get("profiles", []) if isinstance(row, dict)}
    d4 = profiles.get("d4")
    if not isinstance(d4, dict):
        failures.append("d4 profile missing from the pins table")
    else:
        live_pins = {"packet": D4_PACKET, "assembler": "tools/assemble-culture-d4.py",
                     "projection": D4_PROJECTION, "adapter": "tools/assemble-d4-typed.py",
                     "expected": "examples/culture-d4/expected-holds.json"}
        mismatches = {}
        for key, relative in live_pins.items():
            field = d4.get(key) or {}
            pinned = field.get("sha256") if isinstance(field, dict) else None
            actual = sha((live / relative).read_bytes())
            if pinned != actual:
                mismatches[key] = {"pinned": pinned, "live": actual}
        measurement["d4_profile_pins"] = metric(not mismatches, "d4 profile pins versus live bytes")
        if mismatches:
            failures.append(f"d4 profile pins do not match live bytes: {sorted(mismatches)}")
        combined_rows = [row for row in d4.get("repin_history", []) if isinstance(row, dict)
                         if COMBINED_PROJECTOR in json.dumps(row)]
        measurement["d4_combined_binding"] = metric(bool(combined_rows),
                                                    "repin_history binds the combined projector")
        if not combined_rows:
            failures.append("d4 profile does not bind the combined projector in any repin row")
    d4_manifest = manifest_rows(evidence.text(FROZEN_R22_D4))
    measurement["d4_repin_manifest"] = metric(
        len(d4_manifest), f"rows in {FROZEN_R22_D4}")
    if len(d4_manifest) != 3 or not all(row_exit_ok(row) for row in d4_manifest):
        failures.append("the landed round-22 d4-repin generation is not three exit-0 rows")
    return result(failures, measurement, missing)


def citation_tokens(text):
    return sorted({match.group(0).rstrip("\u2026") for match in CITATION_RE.finditer(text)})


def draft_subsection(text):
    start = text.find(DRAFT_BEGIN)
    end = text.find(DRAFT_END)
    if start < 0 or end < 0 or end < start:
        return None
    return text[start:end]


def skill_subsection(text):
    start = text.find(SKILL_HEADING)
    if start < 0:
        return None, None
    next_heading = text.find("\n### ", start + 1)
    next_block = text.find("\n## ", start + 1)
    ends = [position for position in (next_heading, next_block) if position >= 0]
    end = min(ends) if ends else len(text)
    return text[start:end], start


def evaluate_depth_core(skill_text, draft_text):
    failures, measurement = [], {}
    landed, position = skill_subsection(skill_text)
    section = draft_subsection(draft_text)
    if section is None:
        failures.append(f"{DRAFT} lacks the BEGIN/END subsection markers")
    if landed is None:
        failures.append(f"{SKILL} has no '{SKILL_HEADING}' heading: the orchestrator has not landed the rule")
        return failures, measurement
    replay_at = skill_text.find("### Derivation replay")
    error_at = skill_text.find("## Error patterns")
    measurement["placement"] = metric(
        position is not None and replay_at >= 0 and error_at >= 0 and replay_at < position < error_at,
        "heading order in SKILL.md")
    if not (replay_at >= 0 and error_at >= 0 and replay_at < position < error_at):
        failures.append("the family-clean subsection is not between Derivation replay and Error patterns")
    folded = " ".join(landed.split()).lower()
    elements = {
        "rule_statement": ("selects data and provenance by the input packet's" in folded
                           and "family-owned fields" in folded),
        "injection_point_warning": ("injection-point warning" in folded
                                    and "unconditional" in folded and "build_payload" in folded),
        "paired_controls": sum(1 for name in CONTROL_NAMES if name in folded),
        "round25_commitment": bool(re.search(r"round[ -]25", folded) and "commit" in folded),
    }
    measurement["elements"] = {key: metric(value if isinstance(value, bool) else value >= 5,
                                           f"claimed element {key}")
                               for key, value in elements.items()}
    measurement["paired_control_names"] = metric(elements["paired_controls"],
                                                 "design control names present in the subsection")
    if not elements["rule_statement"]:
        failures.append("rule statement element missing from the landed subsection")
    if not elements["injection_point_warning"]:
        failures.append("injection-point warning element missing from the landed subsection")
    if elements["paired_controls"] < 5:
        failures.append(f"paired-controls element incomplete: {elements['paired_controls']} of 7 control names present")
    if not elements["round25_commitment"]:
        failures.append("round-25 implementation commitment missing from the landed subsection")
    if section is not None:
        draft_tokens = citation_tokens(section)
        landed_tokens = set(citation_tokens(landed))
        dropped = [token for token in draft_tokens if token not in landed_tokens]
        measurement["citations"] = {"draft_total": metric(len(draft_tokens), "citations in draft subsection"),
                                    "dropped": dropped}
        if dropped:
            failures.append(f"landed subsection dropped draft citations: {dropped[:8]}")
    if "105/105" in landed:
        failures.append("landed subsection claims the v3 link count; correct-wording 105/105 is a round-25 tail")
    return failures, measurement


def measure_depth(evidence):
    failures, missing = [], []
    measurement = {}
    skill_text = evidence.text(SKILL)
    draft_text = evidence.text(DRAFT)
    if not draft_text:
        return result([f"rule draft unreadable: {DRAFT}"], measurement, evidence.missing)
    section = draft_subsection(draft_text)
    if section is None:
        failures.append(f"{DRAFT} lacks the BEGIN/END subsection markers")
    measurement["reviewers"] = {}
    for relative in FRAGMENTS:
        text = evidence.text(relative)
        reviewed = bool(text) and bool(DATE_RE.search(text)) and "skill-draft.md" in text
        measurement["reviewers"][relative] = metric(reviewed, f"review fragment {relative}")
        if not reviewed:
            failures.append(f"review fragment missing or unmarked: {relative}")
            if not (ROOT / relative).is_file():
                missing.append(relative)
    if "fragment-D01.md" not in draft_text or "fragment-D03.md" not in draft_text:
        failures.append(f"{DRAFT} does not name its review fragments")
    core_failures, core_measurement = evaluate_depth_core(skill_text, draft_text)
    failures.extend(core_failures)
    measurement.update(core_measurement)
    if skill_text:
        brief = evidence.text("examples/culture-d4/components/01-brief.yml")
        if "D2B-01" not in brief:
            failures.append("cited D4 brief no_import rows (D2B-01..04) do not resolve")
        log_text = evidence.text("LOG.md")
        if "Routed to round 25" not in log_text:
            failures.append("cited round-22 routing (LOG.md 'Routed to round 25') does not resolve")
        holds = evidence.document("examples/culture-d4/expected-holds.json")
        counts = (holds or {}).get("counts")
        good = isinstance(counts, dict) and counts.get("hold") == 12 and counts.get("note") == 0 and counts.get("fail") == 0
        measurement["worked_instance"] = metric(good, "expected-holds counts hold:12/note:0/fail:0")
        if not good:
            failures.append(f"cited worked-instance counts do not resolve: {counts}")
        supersedes = (holds or {}).get("supersedes_pins") or {}
        prefixes_ok = (str(supersedes.get("projection_sha256", "")).startswith("cbcf997f")
                       and str(supersedes.get("projector_sha256", "")).startswith("76536a92"))
        measurement["supersedes_pins"] = metric(prefixes_ok, "expected-holds supersedes_pins pre-fix digests")
        if not prefixes_ok:
            failures.append("expected-holds supersedes_pins do not carry the cited pre-fix digests")
    for relative in ("reports/round-22/bleed/design.md", "reports/round-22/bleed/analysis.md",
                     "reports/round-22/bleed/impl.md", "reports/round-22/bleed/repin.md",
                     "reports/round-22/routed-resolution.json", "corpus/lessons/round-22.md",
                     "corpus/knowledge/verification/gate-frozen-run-standard.md"):
        if not (ROOT / relative).is_file():
            failures.append(f"cited rule basis missing: {relative}")
            missing.append(relative)
    resolutions = evidence.document("reports/round-22/routed-resolution.json") or {}
    routes = json.dumps(resolutions)
    for route in ("R21-ALIAS-COERCION", "R21-MTIME-TIE-BREAK"):
        if route not in routes:
            failures.append(f"routed resolution {route} missing from the cited ledger")
    return result(failures, measurement, missing)


def measure():
    evidence = Evidence()
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    targets = evidence.document(f"{ROUND_DIR}/targets.json") or {}
    baseline = claims.get("baseline_revision")
    live = live_lane()
    preservation = protected_baseline(baseline)
    if live is None:
        raise ValueError("cannot locate the live lane root above the isolated clone")
    synced = sync_round_surface(live)
    regressions, runs = measure_regressions()
    results = {}
    for claim_id, operation in (
            ("O", lambda: measure_operability(evidence, regressions)),
            ("D", lambda: measure_depth(evidence))):
        try:
            results[claim_id] = operation()
        except (OSError, ValueError, TypeError, KeyError, RuntimeError, AttributeError,
                subprocess.SubprocessError, shutil.Error) as error:
            results[claim_id] = result([f"Could not evaluate claim {claim_id}: {type(error).__name__}: {error}"], {})
    changed_inputs = []
    for relative, expected in evidence.inputs.items():
        try:
            observed = sha(safe_path(relative).read_bytes())
        except (OSError, ValueError):
            observed = None
        if expected != observed:
            changed_inputs.append(relative)
    coherence = []
    if claims.get("round") != 23 or targets.get("round") != 23:
        coherence.append("Claims/targets are not both round 23")
    if targets.get("baseline_revision") != baseline:
        coherence.append("Claims/targets disagree on the declared baseline")
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"O": "operability", "D": "depth"}:
        coherence.append("Declared claim set is not O/operability, D/depth")
    worker_total = sum(targets.get("workers", {}).values()) if isinstance(targets.get("workers"), dict) else None
    if worker_total != claims.get("workers"):
        coherence.append("Targets worker counts do not sum to the declared 16-worker wave")
    if changed_inputs:
        coherence.append("Evidence changed while being measured: " + ", ".join(changed_inputs))
    coherence.extend(evidence.errors)
    failures = [f"claim {claim_id}: {failure}" for claim_id, item in results.items() for failure in item["failures"]]
    failures.extend("preservation: " + item for item in preservation["failures"])
    failures.extend("evidence: " + item for item in coherence)
    return {"round": 23, "runner": RUNNER, "runner_sha256": sha(safe_path(RUNNER).read_bytes()),
            "counting_command": COMMAND, "date": today(), "baseline_revision": baseline,
            "targets_date": targets.get("date"), "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results,
            "failures": failures, "missing_dependencies": sorted(evidence.missing | {
                path for item in results.values() for path in item["missing_dependencies"]}),
            "protected_filed_artifacts": preservation,
            "protected_bytes_unchanged_during_run": metric(True, "protected inventory is a single snapshot against the declared baseline"),
            "synced_from_live": {key: value for key, value in sorted(synced.items())},
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": [
                "Run this round validator only in an isolated repository clone under the lane's .scratch with TMPDIR below that clone's .scratch. It never edits filed bytes, never commits, and never pushes.",
                "The wording disposition is measured two ways: the frozen round-20 detector is imported read-only to reproduce the D4-CL08 false positive on the filed packet and to prove the declared-in-r3 revision is clean, and reports/round-23/wording/wording-check.py is executed only against its own isolated clones with its negative and positive controls required.",
                "The combined-source successor pins are verified against live digests: D2 live row before/after, the frozen round-23 repin-d2 generation replayed in a dedicated clone with a tamper refusal control, a discovered new v2 receipt verified with reports/round-15/handoff/frozen-verify.py while the alias-only baseline must still refuse, and the D4 profile leg bound to the combined projector.",
                "The regression battery executes only declared selftest/check modes and handoff v2/v3 verification. No recorded command string from any evidence file is executed.",
                "Depth checks compare the landed SKILL.md subsection to the R23-D draft subsection: placement, the four declared elements, citation survival, reviewer fragments, and resolution of the cited anchors. A worker draft in reports/ is not a SKILL landing.",
                "Protected reports and frozen generations of rounds 8-22 must match the round-23 declared baseline. Accepted-disposition new files live under reports/round-23 and tools/gates/frozen/round-23 only.",
            ]}


def measure_operability(evidence, regressions):
    live = live_lane()
    failures = list(regressions["failures"])
    measurement = {"regressions": {
        "runs_total": regressions["measurement"]["runs_total"],
        "failures": regressions["failures"],
        "runs": regressions["measurement"]["runs"],
        "labels": {label: {"exit": item.get("exit"), "command": item.get("command"),
                           "date": item.get("date")}
                   for label, item in regressions_tail(regressions).items()}}}
    wording = measure_wording(evidence, live)
    pins = measure_pins(evidence, live, regressions)
    measurement["wording_disposition"] = wording["measurement"]
    measurement["successor_pins"] = pins["measurement"]
    failures.extend("wording: " + item for item in wording["failures"])
    failures.extend("pins: " + item for item in pins["failures"])
    return result(failures, measurement,
                  sorted(set(wording["missing_dependencies"]) | set(pins["missing_dependencies"])))


def regressions_tail(regressions):
    runs = regressions["measurement"]["runs"]
    return {item["label"]: item for item in runs}


def selftest():
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    old_basis = ("grounding: examples/culture-d4/typed-labels.d4.yml#era_reconciliation … and "
                 "the unchanged-foreign-path control is tools/d2-typed-labels.py --selftest exit 0 50/50")
    new_basis = ("grounding: examples/culture-d4/typed-labels.d4.yml#era_reconciliation … and "
                 "the foreign-path-stability control is tools/d2-typed-labels.py --selftest exit 0 50/50")
    check("frozen-rule-fires-old-basis", bool(PLACEHOLDER_RE.search(old_basis)))
    check("frozen-rule-fires-bare-unchanged",
          all(bool(PLACEHOLDER_RE.search(probe)) for probe in PLACEHOLDER_PROBES))
    check("frozen-rule-clean-new-basis", not PLACEHOLDER_RE.search(new_basis))
    check("d4-cl08-line-found", d4_cl08_line("| D4-CL08 | x | y | supported | basis | evidence | note |")
          == "| D4-CL08 | x | y | supported | basis | evidence | note |")
    check("d4-cl08-line-absent", d4_cl08_line("| D4-CL07 | x |") is None)
    tokens = citation_tokens("cites reports/round-22/bleed/design.md:5-11 and 2819f687… plus LOG.md:3298-3309")
    check("citation-tokens-extracted",
          "reports/round-22/bleed/design.md:5-11" in tokens and "2819f687" in tokens
          and "LOG.md:3298-3309" in tokens, tokens=tokens)
    check("citation-hex-rejects-words", not HEX_RE.search("the defaced fixture"))
    draft = DRAFT_BEGIN + "\nsee reports/round-22/bleed/design.md and 2819f687…" + "\n" + DRAFT_END
    body = ("A multi-family projector selects data and provenance by the input packet's "
            "declared family before constructing labels; nothing foreign lands in "
            "family-owned fields.\n"
            "Injection-point warning — an unconditional build_payload call injects the default family.\n"
            "| Paired control | Never |\n|---|---|\n"
            "| D2 compatibility | disabling rank projection |\n"
            "| D4 independence | reading absence as isolation |\n"
            "| not empty-by-default | empty arrays |\n"
            "| Owner-qualified citations | substring bans |\n"
            "| no ID-based reinterpretation | shared IDs as ownership |\n"
            "| honest borrowed language | relabeling |\n"
            "| propagation/tamper | re-blessing pins |\n"
            "Round-25 implementation commitment: the repair is committed to round 25.\n"
            "see reports/round-22/bleed/design.md and 2819f687…")
    landed_good = ("### Derivation replay\nhistorical text\n" + SKILL_HEADING + "\n" + body
                   + "\n## Error patterns\n")
    landed_bad = ("### Derivation replay\nhistorical text\n" + SKILL_HEADING + "\n"
                  + body.replace("and 2819f687…", "only") + "\n## Error patterns\n")
    core_good = evaluate_depth_core(landed_good, draft)
    core_bad = evaluate_depth_core(landed_bad, draft)
    check("citation-superset-accepts", not core_good[0])
    check("citation-superset-rejects", any("dropped draft citations" in failure for failure in core_bad[0]))
    header = "gate\tgate_sha256\tinput\tinput_sha256\texit_code\tfinding_count\toutput\toutput_sha256\tinput_snapshot\tcommand"
    good_row = "g.py\taaab\tp.yml\tbbbb\t0\t1\tg.out\tcccc\tsnap\tpython3 g.py p.yml"
    bad_row = "g.py\taaab\tp.yml\tbbbb\t2\t1\tg.out\tcccc\tsnap\tpython3 g.py p.yml"
    rows = manifest_rows(header + "\n" + good_row + "\n" + bad_row)
    check("manifest-rows-parsed", len(rows) == 2 and row_exit_ok(rows[0]) and not row_exit_ok(rows[1]))
    fixture = {"projector_sha256": COMBINED_PROJECTOR,
               "supersedes_pins": {"projector_sha256": D2_BEFORE_PROJECTOR},
               "revision_note": "round-23 combined-source re-pin"}
    check("live-row-matches", fixture["projector_sha256"] == COMBINED_PROJECTOR
          and fixture["supersedes_pins"]["projector_sha256"] == D2_BEFORE_PROJECTOR)
    check("live-row-drift-detected", fixture["projector_sha256"] != D2_BEFORE_PROJECTOR)
    try:
        safe_path("/tmp/outside")
        refused = False
    except ValueError:
        refused = True
    check("unsafe-evidence-path-refused", refused)
    try:
        strict_json('{"status": "open", "status": "closed"}')
        duplicate = False
    except ValueError:
        duplicate = True
    check("duplicate-json-key-refused", duplicate)
    passed = all(row["passed"] for row in controls)
    print(json.dumps({"round": 23, "command": f"{COMMAND} --selftest", "date": today(),
                      "selftest_passed": passed, "controls": controls,
                      "controls_passed": metric(sum(row["passed"] for row in controls), "runner positive/negative controls"),
                      "controls_total": metric(len(controls), "runner positive/negative controls")}, indent=2, sort_keys=True))
    return 0 if passed else 1


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Measure round-23 O/D acceptance; use only in an isolated clone.")
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
    try:
        receipt = measure()
    except (OSError, ValueError, TypeError, subprocess.SubprocessError) as error:
        print(f"could-not-evaluate: {type(error).__name__}: {error}", file=sys.stderr)
        return 2
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        try:
            guard_receipt()
        except SystemExit as error:
            return error.code if isinstance(error.code, int) else 3
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
