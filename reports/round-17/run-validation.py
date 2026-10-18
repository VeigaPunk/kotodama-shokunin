#!/usr/bin/env python3
"""Round-17 validator — the round's counting command (claims D, C and O).

Claim D (depth) — `examples/culture-d4/` built end-to-end through the typed
pipeline. This runner discovers the D4 artifacts by schema, not by name alone
(canonical names: the D2 convention with a `d4` suffix), then measures:
hold-set equality (the typed packet's emitted findings equal the expected hold
set keyed `(id, severity, where)`, counts and details pinned), determinism
(the d4 assembler's `--check` regenerates byte-identically; two fresh adapter
builds are byte-identical and reproduce the delivered typed packet), replay
(a round-17 frozen manifest replays green under `tools/replay-frozen.py`),
interop (the typed packet strict-parses, its `assembly` pins re-verify, and
the five culture gates run over the D4 packet without exit 2), d2/d3
untouched-and-green (example bytes equal the baseline revision; the D2 typed
pipeline gate and every d2/d3 `--check` exit 0), NON-CANON (the tree declares
it and carries no affirmative clearance/acceptance claim), and pre-declared
holds (the expected hold set is named in the round-17 design docs, and the
claim was declared before dispatch).

Claim C (coverage) — the 12 `stale-documented` entries of the round-16 map
each carry a disposition with evidence: **fixed** (a replacement locator that
is actually present in the corpus entry's bytes and absent from the baseline
bytes, with a dated, command-carried fragment keeping the round-16 reason
trail) or **attempted** (the fragment names the replacement attempt and why
it did not land). Pass per the claim: all 12 dispositioned and
(fixed >= 6 or every non-fixed entry names its attempt). Corpus edits are
permitted only for these 12 named entries; every other civilizations byte
change against the baseline fails C.

Claim O (operability) — `tools/assemble-culture-d4.py` exists and its
`--check` and `--selftest` (positive / tamper / malformed / missing fixture
controls) exit 0; the three pre-existing d2/d3 assemblers are byte-unchanged
from the baseline and stay green.

Filed rounds 8-16 are compared against the declared baseline revision and
must be byte-identical (this round's corrections are NEW files under
reports/round-17/); any difference fails closed. Only fixed read-only
check/selftest commands and this runner's own `.scratch` fixtures are
executed; no command is ever taken from an evidence file. The frozen replay
subprocess alone runs with `TMPDIR` outside the repo, because
`tools/replay-frozen.py` refuses an in-repo mirror root by design. This
runner writes only its own receipt (`reports/round-17/validation.json`); it
measures, it does not certify truth, canon, lore receipt, source freshness,
or any real-world clearance.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
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
ROUND_DIR = "reports/round-17"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
GUARD = "tools/harness/receipt_guard.py"

CIV_DIR = "corpus/knowledge/civilizations"
CIV_MAP_R16 = "reports/round-16/civ-map.json"
CIV_MAP_R17 = f"{ROUND_DIR}/civ-map.json"
CIV_EVIDENCE_DIR = f"{ROUND_DIR}/civ"

D4_DIR = "examples/culture-d4"
D4_DESIGN_DIR = f"{ROUND_DIR}/d4"
D4_ASSEMBLER = "tools/assemble-culture-d4.py"
D2_DIR = "examples/culture-d2"
D3_DIR = "examples/culture-d3"
D2_ASSEMBLER = "tools/assemble-d2.py"
D2_ADAPTER = "tools/assemble-d2-typed.py"
D3_ASSEMBLER = "tools/assemble-culture-d3.py"
PROJECTOR = "tools/d2-typed-labels.py"
TYPED_GATE = "tools/gates/typed-pipeline-gate.py"
GATE_NAMES = (
    "naming-collision-gate.py",
    "phonology-sanity-gate.py",
    "costume-era-consistency-gate.py",
    "lexicon-coverage-audit.py",
    "myth-consistency-gate.py",
)
PINNED_D2D3 = (D2_DIR, D3_DIR, D2_ASSEMBLER, D2_ADAPTER, D3_ASSEMBLER)
FILED = tuple(f"reports/round-{number}" for number in range(8, 17))
MANIFEST_GLOBS = (
    "tools/gates/frozen/round-17*/MANIFEST.tsv",
    f"{ROUND_DIR}/**/MANIFEST.tsv",
    f"{D4_DIR}/**/MANIFEST.tsv",
)
TYPED_SCHEMA = "kotodama-typed-packet-v1"
HOLDS_SCHEMA = "kotodama-typed-pipeline-holds-v1"
STATUS_VOCAB = ("current", "stale-fixed", "stale-documented")
MAP_CONTAINER_KEYS = ("rows", "entries", "civilizations", "map", "records")
ENTRY_KEY_CANDIDATES = ("entry", "civilization", "file", "name", "id", "path", "basename")
STATUS_KEY_CANDIDATES = ("status", "staleness", "state", "receipt", "verdict")
TEXT_SUFFIXES = (".yml", ".yaml", ".json", ".md", ".txt")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
COMMAND_RE = re.compile(r"\b(?:python3?|git|sha256sum|shasum|curl|wget|command)\b", re.I)
URL_RE = re.compile(r"https?://[^\s\"'<>()\[\],]+")
POINTER_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|corpus|examples)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)\b")
SHA_RE = re.compile(r"\b[0-9a-f]{64}\b")
BASELINE_RE = re.compile(r"[0-9a-f]{40,64}")
ATTEMPT_RE = re.compile(
    r"(?i)\b(attempt(?:ed|ing|s)?|could not|couldn't|not fixed|unfixed|unresolved|"
    r"blocked|no live replacement|no replacement|dead locator|hard-?fail|404|deferred|"
    r"left stale|still stale)\b")
TRAIL_STOPWORDS = {
    "locator", "status", "receipt", "evidence", "verification", "pointer", "dated",
    "reports", "round", "corpus", "knowledge", "civilizations", "locator", "sweep",
    "deferred", "breakage", "reproduction", "distinct", "exists", "cited", "sample",
    "independent", "three", "hard", "fail", "never", "swept", "freshness", "pause",
    "defers", "not", "names", "with", "hits", "gap", "main", "lexical", "host",
    "in-repo", "replacement", "routed", "content", "by", "and", "for", "its",
}
SELFTEST_COUNT_RE = re.compile(r"(\d+)\s*/\s*(\d+)\s+checks?\s+passed", re.I)
CLEARANCE_FORBIDDEN = (
    re.compile(r"(?i)\bcanon_status\s*:\s*(accepted|approved|canon)\b"),
    re.compile(r"(?i)\b(cultural permission (?:is )?(?:granted|obtained)|"
               r"rights (?:are )?cleared|clearance (?:is )?granted|"
               r"authenticity (?:is )?certified)\b"),
    re.compile(r"(?i)\b(approved by lore|accepted by lore|lore[- ]accepted)\b"),
)
NONCANON_RE = re.compile(r"(?i)non-?canon")


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


def id_boundary(text, token):
    return re.search(r"(?<![\w/-])" + re.escape(token) + r"(?![\w-])", text) is not None


def normalize_status(value):
    return re.sub(r"[\s_]+", "-", str(value).strip().lower()) if value is not None else None


def normalize_entry(value):
    name = str(value or "").strip().strip("`")
    name = re.sub(r"^corpus/knowledge/civilizations/", "", name)
    name = re.sub(r"\.md$", "", name)
    return Path(name).stem if name else ""


def map_rows(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in MAP_CONTAINER_KEYS:
            value = payload.get(key)
            if isinstance(value, list):
                return value
    return None


def row_entry(row):
    if not isinstance(row, dict):
        return ""
    for key in ENTRY_KEY_CANDIDATES:
        if row.get(key):
            return normalize_entry(row[key])
    return ""


def row_status(row):
    if not isinstance(row, dict):
        return None
    for key in STATUS_KEY_CANDIDATES:
        if row.get(key):
            return normalize_status(row[key])
    return None


def row_reason(row):
    if not isinstance(row, dict):
        return ""
    for key in ("reason", "note", "detail", "evidence", "evidence_path"):
        if row.get(key):
            return str(row[key])
    return ""


class Evidence:
    def __init__(self):
        self.inputs = {}
        self.missing = set()
        self.errors = []

    def bytes(self, relative):
        try:
            data = safe_path(relative).read_bytes()
            self.inputs[relative] = sha(data)
            return data
        except (OSError, ValueError) as error:
            self.missing.add(relative)
            self.errors.append(f"{relative}: {error}")
            return b""

    def text(self, relative):
        data = self.bytes(relative)
        try:
            return data.decode("utf-8")
        except UnicodeError as error:
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


def run_command(parts, timeout=300, tmpdir=None):
    argv = [sys.executable, *parts]
    child_env = dict(os.environ)
    child_env.update(TMPDIR=str(tmpdir or (ROOT / ".scratch")),
                     PYTHONDONTWRITEBYTECODE="1")
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
                    stdout_tail=run.stdout.decode("utf-8", "replace")[-1600:],
                    stderr_tail=run.stderr.decode("utf-8", "replace")[-1600:])
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error),
                    timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def git(*args, data=None):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    proc = subprocess.run(["git", "--literal-pathspecs", *args], cwd=ROOT,
                          input=data, capture_output=True, timeout=120, env=env)
    if proc.returncode:
        raise ValueError(f"git {shlex.join(args)}: "
                         f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout


def baseline_blobs(revision, prefix):
    """{relative: bytes} for every blob under prefix at revision."""
    blobs = {}
    records = git("ls-tree", "-r", "-z", revision, "--", prefix).split(b"\0")
    wanted = []
    for record in records:
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, kind, oid = metadata.split()
        if kind != b"blob":
            continue
        wanted.append((raw_path.decode("utf-8"), oid))
    if not wanted:
        return blobs
    payload = git("cat-file", "--batch", data=b"".join(oid + b"\n" for _, oid in wanted))
    offset = 0
    for relative, oid in wanted:
        end = payload.index(b"\n", offset)
        header = payload[offset:end].split()
        if len(header) != 3 or header[0] != oid or header[1] != b"blob":
            raise ValueError(f"unexpected Git blob reply for {relative}")
        size = int(header[2])
        blobs[relative] = payload[end + 1:end + 1 + size]
        offset = end + size + 2
    return blobs


def worktree_files(prefix):
    base = ROOT / prefix
    files = []
    if base.is_file():
        return [prefix]
    if not base.is_dir():
        return []
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or ".scratch" in path.parts:
            continue
        if path.suffix == ".log":
            continue  # git-ignored scratch logs (.gitignore *.log) are not filed bytes
        files.append(path.relative_to(ROOT).as_posix())
    return files


def scan_files(prefix, suffixes=TEXT_SUFFIXES):
    return [relative for relative in worktree_files(prefix)
            if Path(relative).suffix.lower() in suffixes]


def preservation_kind(relative, old, new):
    if old == new:
        return "byte-identical"
    if new.startswith(old) and relative.endswith(".md"):
        return "append-only"
    return "violation"


# ------------------------------------------------------------------ claim D


def classify_d4_file(relative, text):
    """Semantic identity of a candidate D4 artifact; name only breaks ties."""
    name = Path(relative).name.lower()
    if TYPED_SCHEMA in text or f'"{TYPED_SCHEMA}"' in text:
        return "typed"
    if name.startswith("expected-holds") or (name.startswith("expected") and
                                             '"holds"' in text and relative.endswith(".json")):
        return "expected"
    if name.startswith("typed-labels") or ('"typed_labels"' in text and '"label_kinds"' in text):
        return "projection"
    if name.startswith("packet.") or (name.startswith("packet") and relative.endswith((".yml", ".yaml"))):
        return "packet" if "typed" not in name else "typed"
    if "brief" in name:
        return "brief"
    return "other"


def d4_discovery(base=None):
    root = Path(base) if base is not None else ROOT / D4_DIR
    root_rel = root.relative_to(ROOT).as_posix() if root.is_relative_to(ROOT) else str(root)
    info = {"base": root_rel, "files": [], "components": [], "brief": None,
            "packet": None, "typed": None, "projection": None, "expected": None,
            "design_docs": []}
    design_docs = []
    design_dir = ROOT / D4_DESIGN_DIR
    if design_dir.is_dir():
        design_docs.extend(path.relative_to(ROOT).as_posix()
                           for path in sorted(design_dir.rglob("*.md"))
                           if "__pycache__" not in path.parts)
    round_dir = ROOT / ROUND_DIR
    if round_dir.is_dir():
        for path in sorted(round_dir.rglob("*.md")):
            relative = path.relative_to(ROOT).as_posix()
            if "__pycache__" in path.parts or relative in design_docs:
                continue
            if "/civ/" in relative:
                continue  # claim-C receipts, not D4 design surface
            design_docs.append(relative)
    design_docs.extend(relative for relative in scan_files(D4_DIR, (".md",))
                       if relative not in design_docs)
    info["design_docs"] = sorted(design_docs)
    if not root.is_dir():
        return info
    for path in sorted(root.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.as_posix()
        info["files"].append(relative)
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        if "/components/" in relative:
            info["components"].append(relative)
            continue
        kind = classify_d4_file(relative, text)
        if kind == "other":
            continue
        if kind == "typed":
            if info["typed"] is None or Path(relative).name.startswith("packet."):
                info["typed"] = relative
        elif kind in ("packet", "brief", "expected", "projection"):
            if info[kind] is None:
                info[kind] = relative
    if info["brief"] is None:
        # the D2 convention keeps the brief as the registry component
        # (components/01-brief.yml); accept that when no top-level brief file
        # exists, without dropping it from the component count.
        for relative in info["components"]:
            if "brief" in Path(relative).name.lower():
                info["brief"] = relative
                break
    return info


def holds_key(items):
    return {(str(item.get("id")), str(item.get("severity")), str(item.get("where")))
            for item in items if isinstance(item, dict)}


def with_severity(items, severity):
    """Expected rows may omit the severity field; their container names it."""
    return [dict(item, severity=item.get("severity") or severity)
            for item in items if isinstance(item, dict)]


def compare_holds(findings, expected_doc):
    holds = with_severity(expected_doc.get("holds") or [], "hold")
    notes = with_severity(expected_doc.get("notes") or [], "note")
    fails = with_severity(expected_doc.get("fails") or [], "fail")
    expected_items = holds + notes + fails
    observed = holds_key(findings)
    expected = holds_key(expected_items)
    observed_counts = {severity: sum(1 for item in observed if item[1] == severity)
                       for severity in ("hold", "note", "fail")}
    expected_counts = {severity: sum(1 for item in expected if item[1] == severity)
                       for severity in ("hold", "note", "fail")}
    declared_counts = expected_doc.get("counts") if isinstance(expected_doc, dict) else None
    details = {(str(item.get("id")), str(item.get("where"))): item.get("detail")
               for item in expected_items}
    detail_mismatch = []
    details_pinned = 0
    for finding in findings:
        key = (str(finding.get("id")), str(finding.get("where")))
        if key in details and details[key] is not None:
            details_pinned += 1
            if details[key] != finding.get("detail"):
                detail_mismatch.append(key)
    return {
        "observed": sorted(observed), "expected": sorted(expected),
        "missing": sorted(expected - observed), "extra": sorted(observed - expected),
        "observed_counts": observed_counts, "expected_counts": expected_counts,
        "declared_counts": declared_counts, "detail_mismatch": sorted(detail_mismatch),
        "details_pinned": details_pinned,
    }


def load_strict(packet_text):
    namespace = runpy.run_path(str(ROOT / PROJECTOR))
    return namespace["load_packet_strict"](packet_text)


def adapter_for(typed_doc):
    pins = typed_doc.get("assembly") or typed_doc.get("typed_assembly") or {}
    digest = pins.get("adapter_sha256")
    if isinstance(digest, str) and (ROOT / D2_ADAPTER).is_file():
        if sha((ROOT / D2_ADAPTER).read_bytes()) == digest:
            return D2_ADAPTER
    if isinstance(digest, str):
        for relative in worktree_files("tools"):
            if relative.endswith(".py") and "assemble" in Path(relative).name:
                if sha((ROOT / relative).read_bytes()) == digest:
                    return relative
    return D2_ADAPTER


def d4_gates_over_packet(packet_relative):
    records = []
    for name in GATE_NAMES:
        gate = f"tools/gates/{name}"
        if not (ROOT / gate).is_file():
            records.append({"gate": gate, "exit": None, "error": "gate missing"})
            continue
        run = run_command([gate, packet_relative])
        records.append({"gate": gate, "exit": run.get("exit"),
                        "stdout_tail": run.get("stdout_tail", "")[-400:],
                        "error": run.get("error")})
    return records


def measure_d(evidence, claims):
    failures, missing = [], set()

    def fail(message):
        failures.append(message)

    discovery = d4_discovery()
    for key in ("packet", "typed", "projection", "expected", "brief"):
        if discovery[key] is None:
            missing.add(f"{D4_DIR}/{key}")
            fail(f"D4 {key} artifact not found under {D4_DIR}")
    components = discovery["components"]
    if len(components) < 12:
        fail(f"D4 components: {len(components)} found, 12 required")
    for relative in discovery["files"]:
        evidence.bytes(relative)
    for relative in discovery["design_docs"]:
        evidence.text(relative)

    typed_doc, typed_error = None, None
    findings_key = None
    if discovery["typed"]:
        text = evidence.text(discovery["typed"])
        try:
            loaded = load_strict(text)
            typed_doc = loaded.get("packet")
            if typed_doc is None:
                typed_error = f"strict loader refused the typed packet: {loaded.get('findings', [])[:1]}"
        except Exception as error:  # peer loader is fail-closed by design
            typed_error = f"strict loader raised: {error}"
    expected_doc = evidence.document(discovery["expected"]) if discovery["expected"] else None
    if discovery["expected"] and expected_doc is None:
        fail("D4 expected hold set is not strict JSON")
    if expected_doc is not None and expected_doc.get("schema") not in (None, HOLDS_SCHEMA):
        fail(f"D4 expected hold set schema is {expected_doc.get('schema')!r}")

    # D2 hold-set equality -------------------------------------------------
    comparison = None
    if typed_doc is not None and expected_doc is not None:
        findings_key = "pipeline_findings" if typed_doc.get("pipeline_findings") is not None \
            else "findings"
        findings = [item for item in (typed_doc.get(findings_key) or [])
                    if isinstance(item, dict)]
        comparison = compare_holds(findings, expected_doc)
        if comparison["missing"]:
            fail(f"D4 hold set missing findings: {comparison['missing'][:4]}")
        if comparison["extra"]:
            fail(f"D4 hold set carries extra findings: {comparison['extra'][:4]}")
        if comparison["observed_counts"] != comparison["expected_counts"]:
            fail(f"D4 hold counts differ: observed {comparison['observed_counts']} "
                 f"vs expected {comparison['expected_counts']}")
        if comparison["declared_counts"] and \
                comparison["declared_counts"] != comparison["observed_counts"]:
            fail(f"D4 expected file declares counts {comparison['declared_counts']} "
                 f"but the packet emits {comparison['observed_counts']}")
        if comparison["detail_mismatch"]:
            fail(f"D4 hold details differ from the expected file: "
                 f"{comparison['detail_mismatch'][:3]}")
        # routing consistency for FORM-UNRESOLVED-style holds, when present
        routing = [row for row in (typed_doc.get("typed_channel") or []) if isinstance(row, dict)]
        off_records = sorted(str(row.get("record")) for row in routing if row.get("record"))
        owed = sorted(str(item.get("where")) for item in findings
                      if str(item.get("id")).endswith("FORM-UNRESOLVED"))
        if owed or off_records:
            if owed != off_records:
                fail(f"D4 routing mismatch: owed holds {owed[:4]} vs routed {off_records[:4]}")
        # pins embedded in the expected file, when present
        for pin_key, relative in (("packet_sha256", discovery["packet"]),
                                  ("projection_sha256", discovery["projection"]),
                                  ("projector_sha256", PROJECTOR),
                                  ("adapter_sha256", None)):
            declared = expected_doc.get(pin_key)
            if not isinstance(declared, str):
                continue
            if relative is None:
                relative = adapter_for(typed_doc)
            if not (ROOT / relative).is_file():
                fail(f"D4 expected file pins {pin_key} but {relative} is missing")
                continue
            if sha((ROOT / relative).read_bytes()) != declared:
                fail(f"D4 expected file pin {pin_key} does not match {relative}")
    elif typed_error:
        fail(typed_error)

    # determinism ----------------------------------------------------------
    determinism = {}
    if (ROOT / D4_ASSEMBLER).is_file():
        check_run = run_command([D4_ASSEMBLER, "--check"])
        determinism["assembler_check"] = {key: check_run.get(key)
                                          for key in ("command", "exit", "stdout_tail",
                                                      "stderr_tail", "date")}
        if check_run.get("exit") != 0:
            fail(f"{D4_ASSEMBLER} --check exit {check_run.get('exit')}")
    if typed_doc is not None and discovery["packet"] and discovery["projection"]:
        adapter = adapter_for(typed_doc)
        scratch = ROOT / ".scratch"
        scratch.mkdir(exist_ok=True)
        first = scratch / "round-17-d4-typed-a.yml"
        second = scratch / "round-17-d4-typed-b.yml"
        build_runs = []
        for target in (first, second):
            run = run_command([adapter, "--packet", discovery["packet"],
                               "--projection", discovery["projection"],
                               "--emit", target.relative_to(ROOT).as_posix()])
            build_runs.append({"target": target.relative_to(ROOT).as_posix(),
                               "exit": run.get("exit"), "stderr_tail": run.get("stderr_tail", "")[-400:],
                               "command": run.get("command"), "date": run.get("date")})
        determinism["adapter_builds"] = build_runs
        if any(item["exit"] != 0 for item in build_runs):
            fail("D4 typed adapter build did not exit 0 on both fresh builds")
        elif first.read_bytes() != second.read_bytes():
            fail("D4 typed adapter builds are not byte-identical")
        else:
            delivered = (ROOT / discovery["typed"]).read_bytes()
            if first.read_bytes() != delivered:
                fail("D4 delivered typed packet is not reproduced byte-identically "
                     "by the adapter build")
            determinism["twice_identical"] = True
            determinism["matches_delivered"] = first.read_bytes() == delivered
        for target in (first, second):
            target.unlink(missing_ok=True)

    # replay ---------------------------------------------------------------
    manifests = []
    for pattern in MANIFEST_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            relative = path.relative_to(ROOT).as_posix()
            if relative not in manifests:
                manifests.append(relative)
    replay_rows = []
    round17_green = False
    for manifest in manifests:
        run = run_command(["tools/replay-frozen.py", manifest], tmpdir="/tmp")
        row = {"manifest": manifest, "exit": run.get("exit"),
               "stdout_tail": run.get("stdout_tail", "")[-600:],
               "command": run.get("command"), "date": run.get("date")}
        replay_rows.append(row)
        if row["exit"] == 0:
            round17_green = True
    if not manifests:
        missing.add("round-17 frozen manifest")
        fail("no round-17 frozen manifest found for the D4 replay")
    elif not round17_green:
        fail("no round-17 frozen manifest replayed green")
    regression_replay = run_command(["tools/replay-frozen.py",
                                     "tools/gates/frozen/round-11/MANIFEST.tsv"],
                                    tmpdir="/tmp")

    # interop --------------------------------------------------------------
    interop = {"gates": [], "typed_schema": None, "routing_rows": None}
    if typed_doc is not None:
        interop["typed_schema"] = typed_doc.get("schema")
        interop["routing_rows"] = len(typed_doc.get("typed_channel") or [])
        if typed_doc.get("schema") != TYPED_SCHEMA:
            fail(f"D4 typed packet schema is {typed_doc.get('schema')!r}")
        if not interop["routing_rows"]:
            fail("D4 typed packet carries no typed_channel routing rows")
        pins = typed_doc.get("assembly") or typed_doc.get("typed_assembly") or {}
        pin_map = (("packet_sha256", discovery["packet"]),
                   ("projection_sha256", discovery["projection"]),
                   ("adapter_sha256", adapter_for(typed_doc)))
        for pin_key, relative in pin_map:
            if not isinstance(pins.get(pin_key), str) or relative is None:
                continue
            if not (ROOT / relative).is_file():
                fail(f"D4 typed packet pins {pin_key} but {relative} is missing")
            elif sha((ROOT / relative).read_bytes()) != pins[pin_key]:
                fail(f"D4 typed packet pin {pin_key} does not match {relative}")
    if discovery["packet"]:
        interop["gates"] = d4_gates_over_packet(discovery["packet"])
        for record in interop["gates"]:
            if record["exit"] not in (0, 1):
                fail(f"D4 interop: {record['gate']} exit {record['exit']} "
                     f"({record.get('error') or record.get('stdout_tail', '')[-120:]})")

    # d2/d3 untouched and green -------------------------------------------
    pinned = pinned_untouched(claims.get("baseline_revision"))
    if pinned["failures"]:
        failures.extend(pinned["failures"])
    greens = {}
    green_commands = (
        ("typed_pipeline_gate", [TYPED_GATE]),
        ("d2_assembler_check", [D2_ASSEMBLER, "--check"]),
        ("d2_adapter_check", [D2_ADAPTER, "--check"]),
        ("projector_check", [PROJECTOR, "--check"]),
        ("d3_assembler_check", [D3_ASSEMBLER, "--check"]),
    )
    for key, parts in green_commands:
        run = run_command(parts)
        greens[key] = {"command": run.get("command"), "exit": run.get("exit"),
                       "date": run.get("date")}
        if run.get("exit") != 0:
            fail(f"d2/d3 regression: {' '.join(parts)} exit {run.get('exit')}")

    # NON-CANON ------------------------------------------------------------
    noncanon = {"marker_files": [], "forbidden": []}
    for relative in discovery["files"]:
        if Path(relative).suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = evidence.text(relative)
        if NONCANON_RE.search(text):
            noncanon["marker_files"].append(relative)
        for pattern in CLEARANCE_FORBIDDEN:
            match = pattern.search(text)
            if match:
                noncanon["forbidden"].append({"path": relative, "match": match.group(0)})
    if not noncanon["marker_files"]:
        fail("no NON-CANON declaration found under examples/culture-d4/")
    if noncanon["forbidden"]:
        fail(f"clearance/acceptance claim found: {noncanon['forbidden'][:3]}")

    # hold set pre-declared in design docs ---------------------------------
    predeclared = {"design_docs": discovery["design_docs"], "hold_ids_missing": [],
                   "wheres_missing": [], "claims_state": claims.get("state")}
    if expected_doc is not None:
        design_text = "\n".join(evidence.text(relative) for relative in discovery["design_docs"])
        if not discovery["design_docs"]:
            fail("no round-17 D4 design docs found (hold set not pre-declared in design)")
        else:
            expected_items = ((expected_doc.get("holds") or []) + (expected_doc.get("notes") or [])
                              + (expected_doc.get("fails") or []))
            ids = sorted({str(item.get("id")) for item in expected_items if isinstance(item, dict)})
            wheres = sorted({str(item.get("where")) for item in expected_items
                             if isinstance(item, dict)})
            predeclared["hold_ids_missing"] = [item for item in ids
                                               if not id_boundary(design_text, item)]
            # a compact range ("GD-01..GD-06") is a legitimate way to name the
            # set, so each id needs at least one of its locations present, not
            # every one; the full where list is still recorded.
            covered = set()
            for item in expected_items:
                if isinstance(item, dict) and id_boundary(design_text, str(item.get("where"))):
                    covered.add(str(item.get("id")))
            predeclared["ids_without_named_location"] = [item for item in ids
                                                         if item not in covered]
            predeclared["wheres_missing"] = [item for item in wheres
                                             if not id_boundary(design_text, item)]
            if predeclared["hold_ids_missing"]:
                fail(f"design docs do not name hold ids: {predeclared['hold_ids_missing'][:4]}")
            if predeclared["ids_without_named_location"]:
                fail("design docs name no hold location for: "
                     f"{predeclared['ids_without_named_location'][:4]}")
    if claims.get("state") != "declared-before-dispatch":
        fail(f"claims.json state is {claims.get('state')!r}, not declared-before-dispatch")

    measurement = {
        "discovery": discovery,
        "hold_comparison": comparison,
        "findings_key": findings_key,
        "determinism": determinism,
        "replay": {"manifests": replay_rows, "round17_green": round17_green,
                   "round11_regression": {"command": regression_replay.get("command"),
                                          "exit": regression_replay.get("exit"),
                                          "date": regression_replay.get("date")}},
        "interop": interop,
        "pinned_d2d3": pinned["measurement"],
        "greens": greens,
        "noncanon": noncanon,
        "predeclared": predeclared,
        "typed_error": typed_error,
        "components_count": metric(len(components), "count examples/culture-d4 components"),
    }
    return result(failures, measurement, missing)


def pinned_untouched(baseline):
    """Bytes of the pinned d2/d3 paths must equal the baseline revision."""
    failures, rows = [], []
    if not isinstance(baseline, str) or not BASELINE_RE.fullmatch(baseline):
        return result(["claims.json has no full baseline revision"],
                      {"baseline_revision": baseline, "paths": rows})
    try:
        for prefix in PINNED_D2D3:
            baseline_files = baseline_blobs(baseline, prefix)
            worktree = worktree_files(prefix)
            for relative in sorted(set(baseline_files) | set(worktree)):
                old = baseline_files.get(relative)
                new = (ROOT / relative).read_bytes() if (ROOT / relative).is_file() else None
                disposition = ("byte-identical" if old is not None and new == old else
                               "new" if old is None else
                               "missing" if new is None else "changed")
                rows.append({"path": relative,
                             "baseline_sha256": sha(old) if old is not None else None,
                             "current_sha256": sha(new) if new is not None else None,
                             "disposition": disposition})
                if disposition != "byte-identical":
                    failures.append(f"pinned d2/d3 path {disposition}: {relative}")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"cannot establish d2/d3 preservation: {error}")
    return result(failures, {"baseline_revision": baseline, "paths": rows,
                             "checked": metric(len(rows), "compare pinned d2/d3 bytes with baseline")})


# ------------------------------------------------------------------ claim C


def round16_targets(evidence):
    payload = evidence.document(CIV_MAP_R16)
    rows = map_rows(payload) if payload is not None else None
    targets = []
    if rows:
        for row in rows:
            if row_status(row) == "stale-documented":
                entry = row_entry(row)
                if entry:
                    reason = row_reason(row)
                    shard = re.search(r"reports/round-16/civ/[\w.-]+\.md", reason)
                    targets.append({"entry": entry, "reason": reason,
                                    "shard": shard.group(0) if shard else None})
    return targets


def trail_token_match(text, reason):
    tokens = {token.lower() for token in re.findall(r"[A-Za-z][A-Za-z0-9_.-]{5,}", reason)}
    tokens = {token for token in tokens if token not in TRAIL_STOPWORDS}
    return any(token in text.lower() for token in tokens)


def attribution_rank(relative, entry, text):
    """How strongly a fragment speaks for one entry: canonical name first,
    then a fragment naming the entry path, then any fragment mentioning it."""
    if Path(relative).name == f"{entry}.md":
        return 0
    if f"{CIV_DIR}/{entry}.md" in text:
        return 1
    return 2


def rank2_line_support(text, entry):
    """A mere listing mention only counts when the entry's own line carries the
    attempt vocabulary — a shared sweep's index row does not disposition it."""
    for line in text.splitlines():
        if id_boundary(line, entry) and ATTEMPT_RE.search(line):
            return True
    return False


def classify_fragment(text, corpus_text, baseline_text):
    landed = []
    for locator in URL_RE.findall(text) + POINTER_RE.findall(text):
        locator = locator.rstrip(".,;:)]}\"'`")
        if locator.startswith("reports/"):
            continue  # round evidence trails are provenance, not source locators
        if locator and locator in corpus_text and locator not in baseline_text:
            landed.append(locator)
    if landed:
        return "fixed", sorted(set(landed))
    if ATTEMPT_RE.search(text):
        return "attempted", []
    return "unclassified", []


def measure_c(evidence, claims):
    failures, missing = [], set()
    targets = round16_targets(evidence)
    if len(targets) != 12:
        failures.append(f"round-16 map yields {len(targets)} stale-documented targets, 12 expected")
    target_entries = {item["entry"] for item in targets}

    fragments = []
    for relative in scan_files(CIV_EVIDENCE_DIR):
        fragments.append((relative, evidence.text(relative)))

    updated_map = evidence.document(CIV_MAP_R17) if (ROOT / CIV_MAP_R17).is_file() else None
    updated_rows = map_rows(updated_map) if updated_map is not None else None
    patch_rel = f"{CIV_EVIDENCE_DIR}/map-patch.json"
    patch_doc = evidence.document(patch_rel) if (ROOT / patch_rel).is_file() else None
    patch_rows = patch_doc.get("rows") if isinstance(patch_doc, dict) else None
    patch_from_mismatch = []
    updated_status = {}
    if updated_rows:
        for row in updated_rows:
            entry = row_entry(row)
            if entry:
                updated_status[entry] = row_status(row)
    elif isinstance(patch_rows, list):
        filed_rows = {}
        filed = evidence.document(CIV_MAP_R16)
        for row in (map_rows(filed) or []):
            entry = row_entry(row)
            if entry:
                filed_rows[entry] = row
        for row in patch_rows:
            if not isinstance(row, dict):
                continue
            entry = row_entry(row)
            to = row.get("to") if isinstance(row.get("to"), dict) else {}
            if entry and to.get("status"):
                updated_status[entry] = normalize_status(to["status"])
            source = row.get("from_") if isinstance(row.get("from_"), dict) else None
            filed_row = filed_rows.get(entry)
            if source is not None and filed_row is not None:
                if normalize_status(source.get("status")) != row_status(filed_row) or \
                        source.get("reason") != row_reason(filed_row):
                    patch_from_mismatch.append(entry)
    if patch_from_mismatch:
        failures.append("map-patch from_ rows do not match the filed round-16 map: "
                        f"{sorted(patch_from_mismatch)[:4]}")

    baseline_entries = {}
    try:
        baseline_entries = baseline_blobs(claims.get("baseline_revision", ""), CIV_DIR)
    except (ValueError, subprocess.SubprocessError) as error:
        failures.append(f"cannot read baseline civilizations blobs: {error}")

    rows, fixed, attempted, unclassified = [], [], [], []
    for target in targets:
        entry = target["entry"]
        naming = [(relative, text) for relative, text in fragments
                  if text and id_boundary(text, entry)]
        row = {"entry": entry, "fragments": [relative for relative, _ in naming],
               "disposition": None, "landed_locators": [], "evidence": None,
               "trail": None, "shard": target["shard"]}
        corpus_relative = f"{CIV_DIR}/{entry}.md"
        corpus_text = evidence.text(corpus_relative)
        baseline_text = baseline_entries.get(corpus_relative, b"").decode("utf-8", "replace")
        if not naming:
            failures.append(f"C target {entry}: no evidence fragment names the entry")
            row["disposition"] = "missing"
            rows.append(row)
            continue
        best = None
        for relative, text in naming:
            disposition, landed = classify_fragment(text, corpus_text, baseline_text)
            attribution = attribution_rank(relative, entry, text)
            if disposition == "attempted" and attribution == 2 and \
                    not rank2_line_support(text, entry):
                continue  # a shared sweep's index row is not a disposition
            rank = {"fixed": 2, "attempted": 1, "unclassified": 0}[disposition]
            key = (rank, -attribution)
            if best is None or key > best[0]:
                best = (key, disposition, landed, relative, text)
        if best is None:
            failures.append(f"C target {entry}: only shared-sweep index mentions found; "
                            "a per-entry disposition fragment is required")
            row["disposition"] = "mention-only"
            rows.append(row)
            continue
        _, disposition, landed, relative, text = best
        row["disposition"] = disposition
        row["landed_locators"] = landed
        row["chosen_fragment"] = relative
        row["attribution"] = attribution_rank(relative, entry, text)
        dated = bool(DATE_RE.search(text)) and any(
            value in DATE_RE.findall(text) for value in accepted_round_dates())
        commanded = bool(COMMAND_RE.search(text))
        trail = ("round-16" in text) and (
            (target["shard"] is not None and target["shard"] in text)
            or trail_token_match(text, target["reason"]))
        row["evidence"] = {"dated": dated, "command_carried": commanded, "fragment": relative}
        row["trail"] = trail
        if not (dated and commanded):
            failures.append(f"C target {entry}: chosen fragment {relative} lacks a "
                            "round-date and an access command")
        if not trail:
            failures.append(f"C target {entry}: chosen fragment {relative} does not keep "
                            "the round-16 reason trail")
        if disposition == "fixed":
            fixed.append(entry)
        elif disposition == "attempted":
            attempted.append(entry)
        else:
            unclassified.append(entry)
            failures.append(f"C target {entry}: fragment {relative} neither lands a "
                            "replacement locator nor records an attempt")
        rows.append(row)

    if unclassified:
        failures.append(f"C targets without a disposition: {unclassified}")
    if not (len(fixed) >= 6 or len(fixed) + len(attempted) == len(targets)):
        failures.append(f"C disposition bar not met: {len(fixed)} fixed, {len(attempted)} "
                        f"attempted of {len(targets)} (need >=6 fixed or every non-fixed "
                        "entry naming its attempt)")

    # corpus edits are permitted only for the 12 named entries -----------------
    corpus_rows, violations = [], []
    try:
        baseline_all = baseline_blobs(claims.get("baseline_revision", ""), CIV_DIR)
        for relative in sorted(set(baseline_all) | set(worktree_files(CIV_DIR))):
            old = baseline_all.get(relative)
            new = (ROOT / relative).read_bytes() if (ROOT / relative).is_file() else None
            stem = Path(relative).stem
            changed = old is None or new is None or old != new
            disposition = ("byte-identical" if not changed else
                           "new" if old is None else "missing" if new is None else "changed")
            corpus_rows.append({"path": relative, "disposition": disposition,
                                "baseline_sha256": sha(old) if old is not None else None,
                                "current_sha256": sha(new) if new is not None else None})
            if changed and stem not in target_entries:
                violations.append(relative)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"cannot audit civilizations edits: {error}")
    if violations:
        failures.append(f"civilizations bytes changed outside the 12 named entries: "
                        f"{violations[:5]}")

    # landed fixes must be visible in the corpus bytes -------------------------
    for entry in fixed:
        relative = f"{CIV_DIR}/{entry}.md"
        old = baseline_entries.get(relative)
        new = (ROOT / relative).read_bytes() if (ROOT / relative).is_file() else None
        if old is not None and new == old:
            failures.append(f"C target {entry}: classified fixed but the corpus entry "
                            "bytes are unchanged from the baseline")

    # cross-check the updated map, when one landed -----------------------------
    map_consistency = None
    if updated_status:
        contradictions = []
        for entry in fixed:
            if updated_status.get(entry) == "stale-documented":
                contradictions.append(entry)
        stale_after = sorted(entry for entry in target_entries
                             if updated_status.get(entry) == "stale-documented")
        map_consistency = {"stale_after": stale_after,
                           "contradictions": sorted(contradictions),
                           "source": CIV_MAP_R17 if updated_rows else patch_rel}
        if contradictions:
            failures.append(f"updated map still marks fixed entries stale-documented: "
                            f"{contradictions}")
        if len(stale_after) > len(targets) - 6 and len(fixed) < 6 and len(attempted) < len(targets) - len(fixed):
            failures.append("updated map stale count did not drop by 6 and non-fixed "
                            "entries do not all name attempts")

    measurement = {
        "targets": targets, "rows": rows,
        "fixed": sorted(fixed), "attempted": sorted(attempted),
        "unclassified": sorted(unclassified),
        "fragments": metric(len(fragments), "count evidence fragments under reports/round-17/civ"),
        "corpus_edits": corpus_rows,
        "corpus_out_of_scope": violations,
        "map_consistency": map_consistency,
        "map_r17_present": updated_rows is not None,
        "map_patch_present": isinstance(patch_rows, list),
        "fixed_count": metric(len(fixed), "count stale entries fixed with landed locators"),
        "attempted_count": metric(len(attempted), "count stale entries with recorded attempts"),
    }
    return result(failures, measurement, missing)


def accepted_round_dates():
    now_utc = dt.datetime.now(dt.timezone.utc)
    accepted = {dt.date.today().isoformat(), now_utc.date().isoformat()}
    try:
        claims = strict_json((ROOT / ROUND_DIR / "claims.json").read_text(encoding="utf-8"))
        if isinstance(claims.get("date"), str):
            accepted.add(claims["date"])
    except (OSError, ValueError, UnicodeError):
        pass
    return accepted


# ------------------------------------------------------------------ claim O


def measure_o(evidence, claims):
    failures, missing = [], set()
    checks = {}
    if not (ROOT / D4_ASSEMBLER).is_file():
        missing.add(D4_ASSEMBLER)
        failures.append(f"{D4_ASSEMBLER} does not exist")
        return result(failures, {"checks": checks}, missing)
    evidence.bytes(D4_ASSEMBLER)
    for key, parts in (("check", [D4_ASSEMBLER, "--check"]),
                       ("selftest", [D4_ASSEMBLER, "--selftest"])):
        run = run_command(parts)
        checks[key] = {"command": run.get("command"), "exit": run.get("exit"),
                       "date": run.get("date"),
                       "stdout_tail": run.get("stdout_tail", "")[-800:],
                       "stderr_tail": run.get("stderr_tail", "")[-400:]}
        if run.get("exit") != 0:
            failures.append(f"{D4_ASSEMBLER} --{key} exit {run.get('exit')}")
    selftest_text = checks.get("selftest", {}).get("stdout_tail", "")
    tokens = {token: bool(re.search(token, selftest_text, re.I))
              for token in ("positive|clean", "tamper", "malformed", "missing")}
    count_match = SELFTEST_COUNT_RE.search(selftest_text)
    checks["selftest_controls"] = {
        "tokens": tokens, "count": count_match.groups() if count_match else None}
    if not (all(tokens.values()) or (count_match and int(count_match.group(1)) >= 4)):
        failures.append("d4 assembler --selftest does not evidence the fixture controls "
                        "(positive/tamper/malformed/missing)")

    pinned = pinned_untouched(claims.get("baseline_revision"))
    if pinned["failures"]:
        failures.extend(pinned["failures"])
    greens = {}
    for key, parts in (("d2_assembler_check", [D2_ASSEMBLER, "--check"]),
                       ("d2_assembler_selftest", [D2_ASSEMBLER, "--selftest"]),
                       ("d2_adapter_check", [D2_ADAPTER, "--check"]),
                       ("d3_assembler_check", [D3_ASSEMBLER, "--check"]),
                       ("d3_assembler_selftest", [D3_ASSEMBLER, "--selftest"])):
        run = run_command(parts)
        greens[key] = {"command": run.get("command"), "exit": run.get("exit"),
                       "date": run.get("date")}
        if run.get("exit") != 0:
            failures.append(f"d2/d3 assembler regression: {' '.join(parts)} exit {run.get('exit')}")

    measurement = {"checks": checks, "pinned_d2d3": pinned["measurement"], "greens": greens,
                   "assembler_sha256": evidence.inputs.get(D4_ASSEMBLER)}
    return result(failures, measurement, missing)


# -------------------------------------------------------------- validation


def guard_preflight():
    spec = importlib.util.spec_from_file_location("round17_receipt_guard", ROOT / GUARD)
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


def filed_snapshot():
    snapshot = {}
    for directory in FILED:
        for relative in worktree_files(directory):
            try:
                snapshot[relative] = sha(safe_path(relative).read_bytes())
            except (OSError, ValueError) as error:
                snapshot[relative] = f"ERROR: {error}"
    return snapshot


def filed_preservation(claims):
    failures, rows = [], []
    baseline = claims.get("baseline_revision")
    if not isinstance(baseline, str) or not BASELINE_RE.fullmatch(baseline):
        return result(["claims.json has no full baseline revision"],
                      {"baseline_revision": baseline, "files": rows})
    try:
        for directory in FILED:
            baseline_files = baseline_blobs(baseline, directory)
            worktree = worktree_files(directory)
            for relative in sorted(set(baseline_files) | set(worktree)):
                old = baseline_files.get(relative)
                new = (ROOT / relative).read_bytes() if (ROOT / relative).is_file() else None
                disposition = ("byte-identical" if old is not None and new == old else
                               "new" if old is None else
                               "missing" if new is None else
                               preservation_kind(relative, old, new))
                rows.append({"path": relative,
                             "baseline_sha256": sha(old) if old is not None else None,
                             "current_sha256": sha(new) if new is not None else None,
                             "preservation": disposition})
                if disposition != "byte-identical":
                    failures.append(f"Filed round 8-16 artifact not byte-identical: "
                                    f"{relative} ({disposition})")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"Cannot establish filed-byte preservation: {error}")
    return result(failures, {"baseline_revision": baseline, "files": rows,
                             "checked": metric(len(rows), "compare filed round-8..16 bytes with baseline")})


def validate():
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(exist_ok=True)
    evidence = Evidence()
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    targets = evidence.document(f"{ROUND_DIR}/targets.json") or {}
    before = filed_snapshot()
    depth = measure_d(evidence, claims)
    coverage = measure_c(evidence, claims)
    operability = measure_o(evidence, claims)
    results = {"D": depth, "C": coverage, "O": operability}
    filed = filed_preservation(claims)
    if not filed["passed"]:
        for item in results.values():
            item["failures"].extend(filed["failures"])
            item["passed"] = False
    after = filed_snapshot()
    changes = [{"path": path, "before": before.get(path), "after": after.get(path)}
               for path in sorted(before.keys() | after.keys()) if before.get(path) != after.get(path)]
    if changes:
        for item in results.values():
            item["failures"].append("Filed round-8..16 bytes/path set changed during "
                                    "validation; rerun on a settled tree")
            item["passed"] = False
    declared = {claim.get("id"): claim.get("axis") for claim in claims.get("claims", [])
                if isinstance(claim, dict)}
    if declared != {"D": "depth", "C": "coverage", "O": "operability"}:
        results["D"]["failures"].append(f"Round-17 declared claims do not match D/C/O: {declared}")
        results["D"]["passed"] = False
    seat_total = sum(value for value in (targets.get("workers") or {}).values()
                     if isinstance(value, int))
    if evidence.errors:
        for error in evidence.errors:
            consumer = "C" if CIV_DIR in error or CIV_MAP_R16 in error else "D"
            results[consumer]["failures"].append(error)
            results[consumer]["passed"] = False
    return {
        "round": 17, "runner": RUNNER, "runner_sha256": sha((ROOT / RUNNER).read_bytes()),
        "counting_command": COMMAND, "date": today(),
        "baseline_revision": claims.get("baseline_revision"),
        "targets_date": targets.get("date"),
        "claims_declared": declared,
        "declaration": {"claims_workers": claims.get("workers"), "target_seats": seat_total,
                        "note": "claims.json declares 64 workers; targets.json allocates "
                                "60 seats (see reports/round-17/scope.md F-X02-1). "
                                "Informational: the counting contract does not fail on "
                                "declaration arithmetic."},
        "acceptance_checks_passed": all(item["passed"] for item in results.values()),
        "claims": results, "input_sha256": dict(sorted(evidence.inputs.items())),
        "failures": [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                     for failure in item["failures"]],
        "missing_dependencies": sorted({path for item in results.values()
                                        for path in item["missing_dependencies"]}),
        "filed_rounds": {"baseline": filed["measurement"],
                         "d2d3_pins": results["D"]["measurement"].get("pinned_d2d3", {}),
                         "command": f"{COMMAND} (compare filed round-8..16 bytes with the "
                                    "declared baseline, before and after checks)",
                         "date": today(),
                         "changed_during_validation": changes},
        "limits": [
            "Historical validators are never executed. Only fixed read-only "
            "check/selftest commands and this runner's own .scratch fixtures run; "
            "no command is executed from an evidence file.",
            "Filed rounds 8-16 are compared with the declared baseline and must be "
            "byte-identical: this round's corrections are NEW files under "
            "reports/round-17/, never edits of filed artifacts.",
            "The frozen replay subprocess runs with TMPDIR outside the repository "
            "because tools/replay-frozen.py refuses an in-repo mirror root by "
            "design; nothing is written into the lane by that subprocess.",
            "Claim C is a coverage/staleness disposition: a fixed entry's "
            "replacement locator must be present in the corpus entry's bytes and "
            "absent from the baseline bytes; an attempted entry names its "
            "replacement attempt. The freshness axis-move remains paused; no "
            "source freshness verdict, re-grade, or rank change is issued or "
            "implied by a disposition.",
            "D4 discovery is semantic (schema/filename) so a differently named "
            "artifact is still found; the canonical names are the D2 convention "
            "with a d4 suffix. Interop runs the five culture gates read-only and "
            "accepts exits 0/1 (findings are design output); exit 2 or a "
            "traceback fails the claim.",
            "All artifacts measured are NON-CANON; this receipt does not certify "
            "truth, canon, lore receipt, cultural permission, or any real-world "
            "clearance.",
        ],
    }


# ---------------------------------------------------------------- selftest


def selftest():
    controls = []

    def check(name, value):
        controls.append({"control": name, "passed": bool(value)})

    check("status-normalized", normalize_status("Stale_Fixed") == "stale-fixed"
          and normalize_status("CURRENT") == "current")
    check("entry-paths-normalized",
          normalize_entry("corpus/knowledge/civilizations/ainu.md") == "ainu"
          and normalize_entry("ainu.md") == "ainu")
    check("map-containers-accepted",
          map_rows({"rows": [1]}) == [1] and map_rows([2]) == [2]
          and map_rows({"x": 1}) is None)
    check("id-boundary-precise",
          id_boundary("inuit.md is stale", "inuit")
          and not id_boundary("inuitx.md", "inuit"))
    good = {"holds": [{"id": "D4L-X", "severity": "hold", "where": "GAR-01",
                       "detail": "d"}],
            "notes": [], "counts": {"hold": 1, "note": 0, "fail": 0}}
    same = compare_holds([{"id": "D4L-X", "severity": "hold", "where": "GAR-01",
                           "detail": "d"}], good)
    check("holds-equality-accepts", not same["missing"] and not same["extra"]
          and not same["detail_mismatch"])
    drifted = compare_holds([{"id": "D4L-X", "severity": "hold", "where": "GAR-02",
                              "detail": "d"}], good)
    check("holds-equality-rejects-location", bool(drifted["missing"] and drifted["extra"]))
    laundered = compare_holds([{"id": "D4L-X", "severity": "note", "where": "GAR-01",
                                "detail": "d"}], good)
    check("holds-equality-rejects-laundering", bool(laundered["missing"] and laundered["extra"]))
    detail_drift = compare_holds([{"id": "D4L-X", "severity": "hold", "where": "GAR-01",
                                   "detail": "other"}], good)
    check("holds-equality-pins-details", detail_drift["detail_mismatch"] == [("D4L-X", "GAR-01")])
    null_detail = compare_holds(
        [{"id": "D4L-X", "severity": "hold", "where": "GAR-01", "detail": "observed"}],
        {"holds": [{"id": "D4L-X", "severity": "hold", "where": "GAR-01"}], "notes": [],
         "counts": {"hold": 1, "note": 0, "fail": 0}})
    check("null-detail-not-pinned",
          not null_detail["detail_mismatch"] and null_detail["details_pinned"] == 0)
    inferred = compare_holds(
        [{"id": "D4L-X", "severity": "note", "where": "W", "detail": "d"}],
        {"holds": [], "notes": [{"id": "D4L-X", "where": "W", "detail": "d"}],
         "counts": {"hold": 0, "note": 1, "fail": 0}})
    check("severity-inferred-from-container",
          not inferred["missing"] and not inferred["extra"]
          and inferred["details_pinned"] == 1)
    corpus = "see https://example.org/new-locator\n"
    baseline = "see https://example.org/dead-locator\n"
    fragment = ("2026-10-18. command: curl -sI https://example.org/new-locator. "
                "replaced dead locator; evidence reports/round-16/civ/037-047.md\n")
    disposition, landed = classify_fragment(fragment, corpus, baseline)
    check("fragment-fix-detected", disposition == "fixed" and landed == ["https://example.org/new-locator"])
    attempt = ("2026-10-18. command: curl -sI https://example.org/next. attempt: "
               "candidate 404, no live replacement; round-16 reason kept\n")
    check("fragment-attempt-detected",
          classify_fragment(attempt, corpus, baseline)[0] == "attempted")
    check("fragment-unclassified",
          classify_fragment("2026-10-18 python3 nothing here\n", corpus, baseline)[0]
          == "unclassified")
    check("trail-pointer-not-a-locator",
          classify_fragment("2026-10-18 python3 x; reports/round-16/civ/072-083.md\n",
                            "corpus: reports/round-16/civ/072-083.md\n", "")[0]
          == "unclassified")
    check("attribution-canonical-first",
          attribution_rank("reports/round-17/civ/rome.md", "rome", "") == 0
          and attribution_rank("reports/round-17/civ/sed77.md", "rome",
                               "corpus/knowledge/civilizations/rome.md") == 1
          and attribution_rank("reports/round-17/civ/sed77.md", "rome", "nothing") == 2)
    check("index-row-not-a-disposition",
          not rank2_line_support("→ persia-sasanian.md polynesia-navigation.md (7 files)\n",
                                 "persia-sasanian")
          and rank2_line_support("persia-sasanian: attempt recorded; candidate 404\n",
                                 "persia-sasanian"))
    check("trail-token-match",
          trail_token_match("mentions dorais and the shard", "Dorais 2010 PDF locator 404-stable")
          and not trail_token_match("nothing relevant", "Dorais 2010 PDF locator 404-stable"))
    check("url-extraction", URL_RE.findall("a https://x.org/y, b https://z.org.") ==
          ["https://x.org/y", "https://z.org."]
          and [url.rstrip(".") for url in URL_RE.findall("b https://z.org.")] == ["https://z.org"])
    old = b'{"rows": [{"id": 1}]}\n'
    check("filed-identical", preservation_kind("x.json", old, old) == "byte-identical")
    check("filed-md-append-allowed", preservation_kind("x.md", b"a\n", b"a\nb\n") == "append-only")
    check("filed-rewrite-rejected",
          preservation_kind("x.json", old, old.replace(b"1", b"2")) == "violation")
    check("typed-schema-detected",
          classify_d4_file("examples/culture-d4/packet.d4.typed.yml",
                           "schema: kotodama-typed-packet-v1\n") == "typed")
    check("packet-detected",
          classify_d4_file("examples/culture-d4/packet.d4.yml", "name: x\ncanon: non-canon\n")
          == "packet")
    check("expected-detected",
          classify_d4_file("examples/culture-d4/expected-holds.json",
                           '{"schema": "kotodama-typed-pipeline-holds-v1", "holds": []}')
          == "expected")
    for relative in ("../outside.md", "/outside.md", ".git/config"):
        try:
            safe_path(relative)
        except ValueError:
            check("unsafe-pointer-rejected-" + relative, True)
        else:
            check("unsafe-pointer-rejected-" + relative, False)
    sample = metric(12, "count stale targets")
    check("metric-carries-command-and-date",
          sample["command"].startswith(COMMAND) and sample["date"] == today()
          and sample["value"] == 12)
    check("selftest-count-parsed",
          SELFTEST_COUNT_RE.search("selftest: 38/40 checks passed (fixture)").groups()
          == ("38", "40"))
    check("clearance-claim-caught",
          any(pattern.search("canon_status: accepted") for pattern in CLEARANCE_FORBIDDEN)
          and any(pattern.search("cultural permission granted") for pattern in CLEARANCE_FORBIDDEN))
    check("negated-clearance-not-caught",
          not any(pattern.search("no real-language clearance or cultural permission is claimed")
                  for pattern in CLEARANCE_FORBIDDEN))
    check("noncanon-marker", bool(NONCANON_RE.search("NON-CANON design drill")))
    with tempfile.TemporaryDirectory(prefix="r17-selftest-", dir=str(ROOT / ".scratch")) as tmp:
        base = Path(tmp) / "culture-d4"
        (base / "components").mkdir(parents=True)
        for index in range(1, 13):
            (base / "components" / f"{index:02d}-part.yml").write_text("name: x\n", encoding="utf-8")
        (base / "brief.md").write_text("brief, NON-CANON, hold set: D4L-X at GAR-01\n",
                                       encoding="utf-8")
        (base / "packet.d4.yml").write_text("name: x\ncanon: non-canon\n", encoding="utf-8")
        (base / "typed-labels.d4.yml").write_text('{"typed_labels": {}, "label_kinds": []}\n',
                                                  encoding="utf-8")
        (base / "packet.d4.typed.yml").write_text(
            "schema: kotodama-typed-packet-v1\npipeline_findings: []\n", encoding="utf-8")
        (base / "expected-holds.json").write_text(
            '{"schema": "kotodama-typed-pipeline-holds-v1", "holds": [], "notes": [], '
            '"counts": {"hold": 0, "note": 0, "fail": 0}}\n', encoding="utf-8")
        found = d4_discovery(base)
        check("fixture-discovery-components", len(found["components"]) == 12)
        check("fixture-discovery-roles",
              found["typed"] and found["packet"] and found["projection"]
              and found["expected"] and found["brief"])
    payload = {"runner": RUNNER, "command": COMMAND + " --selftest", "date": today(),
               "selftest_passed": all(item["passed"] for item in controls),
               "controls": controls,
               "passed": metric(sum(item["passed"] for item in controls),
                                "validator selftest controls"),
               "total": metric(len(controls), "validator selftest control inventory")}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["selftest_passed"] else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate round-17 D/C/O without touching filed rounds 8-16.")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--selftest", action="store_true",
                       help="run in-memory validator controls, no receipt write")
    modes.add_argument("--check", action="store_true",
                       help="run full acceptance and print JSON without writing validation.json")
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
        (ROOT / OUTPUT).write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                              ensure_ascii=False) + "\n", encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
