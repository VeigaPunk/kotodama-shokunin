#!/usr/bin/env python3
"""Round-18 validator — the round's counting command (claims O, D and C).

Claim O (operability) — the typed-pipeline gate's assembler-identity leg is
generalized to accept a **declared** assembler pin (packet-declared or flag),
with the default D2 path byte-identical in behaviour, and the re-pin cascade
lands: the round-11 frozen generation keeps its filed bytes (its typed row now
reads `gate_digest_mismatch` — the recorded pin names the pre-generalization
gate), a NEW round-18 frozen generation replays green under
`tools/replay-frozen.py`, the round-9 baseline pins still hold, the round-16
`expected-v2-07.json` pins are re-checked, and every re-pinned surface has its
before/after digests recorded in a round-18 record. Battery, craft, the
coupling verifier and the frozen replays are re-run as regressions.

Claim D (depth) — the generalized gate runs over `examples/culture-d4/`
directly and its emitted findings equal the D4 expected hold set exactly
(15 holds + the declared note set, 0 fails): set equality keyed
`(id, severity, where)`, declared counts, non-null details pinned; the
expected file's pre-declared ids are reconciled against the emitted set; the
D4 typed packet rebuilds byte-identically (determinism); a round-18 frozen
manifest replays green; interop re-verifies the typed packet's strict parse,
its assembly pins and the five culture gates; and the D2 path stays green and
untouched.

Claim C (coverage) — a round-18 civ-map revision applies the round-17 patch
(12 row replacements: 11 `stale-documented -> stale-fixed`, `rome -> current`)
with fix-evidence pointers, re-verifies the attempt-documented rows, carries
date+command on every transitioned row, and reproduces 94 through its counting
command; the filed round-16 map and rounds 8-17 bytes stay byte-identical.

Method is the lane standard: stdlib only, read-only over every artifact, fail
closed on filed-round contact, executes only fixed check/selftest commands
plus this runner's own `.scratch` fixtures, and never takes a command from an
evidence file. The one frozen-replay subprocess runs with `TMPDIR` outside the
repo because `tools/replay-frozen.py` refuses an in-repo mirror root by
design. The runner writes only its own receipt (`reports/round-18/
validation.json`); it measures, it does not certify truth, canon, lore
receipt, source freshness, or any real-world clearance.

    python3 reports/round-18/run-validation.py             # full run + receipt
    python3 reports/round-18/run-validation.py --check      # print, no write
    python3 reports/round-18/run-validation.py --selftest   # in-memory controls
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
import shlex
import subprocess
import sys
import tarfile
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND = 18
ROUND_DIR = "reports/round-18"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
GUARD = "tools/harness/receipt_guard.py"

GATE = "tools/gates/typed-pipeline-gate.py"
ADAPTER = "tools/assemble-d2-typed.py"
PROJECTOR = "tools/d2-typed-labels.py"
SERIALIZER = "tools/assemble-d2.py"
D4_ASSEMBLER = "tools/assemble-culture-d4.py"
D2_DIR = "examples/culture-d2"
D3_DIR = "examples/culture-d3"
D4_DIR = "examples/culture-d4"
D2_PACKET = f"{D2_DIR}/packet.d2.yml"
D2_PROJECTION = f"{D2_DIR}/typed-labels.d2.yml"
D2_TYPED = f"{D2_DIR}/packet.d2.typed.yml"
D2_EXPECTED = f"{D2_DIR}/expected-holds.json"
GATE_NAMES = (
    "naming-collision-gate.py",
    "phonology-sanity-gate.py",
    "costume-era-consistency-gate.py",
    "lexicon-coverage-audit.py",
    "myth-consistency-gate.py",
)
R11_MANIFEST = "tools/gates/frozen/round-11/MANIFEST.tsv"
R11_RECEIPT = "tools/gates/frozen/round-11/typed-pipeline/run-receipt.json"
R11_TYPED = "tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml"
R11_TYPED_ROW_OUT = "tools/gates/frozen/round-11/typed-pipeline/run.log"
R9_BASELINES = "reports/round-9/baselines"
R9_EXPECTED = "tools/gates/expected"
R16_MAP = "reports/round-16/civ-map.json"
R16_V207 = "reports/round-16/handoff/expected-v2-07.json"
R17_PATCH = "reports/round-17/civ/map-patch.json"
R17_FRAGMENT = "reports/round-17/d4/expected-holds.fragment.json"
R17_D4_DESIGN = "reports/round-17/d4"
R17_D4_MANIFEST = "reports/round-17/tests/frozen/MANIFEST.tsv"
TYPED_PIPELINES = "tools/gates/typed-pipelines.json"
D4_ADAPTER_FALLBACK = "tools/assemble-d4-typed.py"
CIV_DIR = "corpus/knowledge/civilizations"
CIV_COUNT_COMMAND = "ls corpus/knowledge/civilizations/*.md | wc -l"
TYPED_SCHEMA = "kotodama-typed-packet-v1"
HOLDS_SCHEMA = "kotodama-typed-pipeline-holds-v1"
STATUS_VOCAB = ("current", "stale-fixed", "stale-documented")
MAP_CONTAINER_KEYS = ("rows", "entries", "civilizations", "map", "records")
ENTRY_KEY_CANDIDATES = ("entry", "civilization", "file", "name", "id", "path", "basename")
STATUS_KEY_CANDIDATES = ("status", "staleness", "state", "receipt", "verdict")
TEXT_SUFFIXES = (".yml", ".yaml", ".json", ".md", ".txt", ".tsv")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
COMMAND_RE = re.compile(r"\b(?:python3?|git|sha256sum|shasum|curl|wget|ls|command)\b", re.I)
HEX_RE = re.compile(r"\b[0-9a-f]{8,64}\b")
BASELINE_RE = re.compile(r"[0-9a-f]{40,64}")
ATTEMPT_RE = re.compile(
    r"(?i)\b(attempt(?:ed|ing|s)?|re-?probed|reprobed|could not|couldn't|not fixed|"
    r"unfixed|unresolved|blocked|no live replacement|no replacement|dead locator|"
    r"left stale|still stale|kept|sweeps?)\b")
# The pre-round-18 gate's recorded behaviour pins (baseline revision 3dd3754):
# the round-11 frozen row's stdout is a filed receipt; the default-path stdout
# is measured from the baseline mirror at run time. Only the frozen row's
# digest is a constant here because it is a FILED value; everything else is
# re-measured and compared, never copied from a printed verdict.
R11_TYPED_ROW_STDOUT_SHA = (
    "9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606")
# Filed in reports/round-11/validation.json (the --json rerun row) and quoted by
# rounds 12/14/15 regressions; the generalized gate must still reproduce it.
R11_JSON_STDOUT_SHA = (
    "19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62")
# The default-path stdout sha recorded by the round-18 gate seats (R18-O11,
# reports/round-18/gate/tests-1.md) at the pre-change revision; corroboration
# only — the required proof is byte-identity against the baseline mirror.
DEFAULT_STDOUT_SHA_OBSERVED = (
    "15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b")
PINNED_TOOL_SURFACES = (GATE, ADAPTER, PROJECTOR, SERIALIZER)
FILED = tuple(f"reports/round-{number}" for number in range(8, 18))
FROZEN_GLOBS = (
    "tools/gates/frozen/round-18*",
    "tools/gates/frozen/round-18*/MANIFEST.tsv",
    "tools/gates/frozen/round-18*/**/MANIFEST.tsv",
    "tools/gates/frozen/round-18/**/MANIFEST.tsv",
    f"{ROUND_DIR}/**/MANIFEST.tsv",
    f"{D4_DIR}/**/MANIFEST.tsv",
    f"{ROUND_DIR}/**/*frozen*",
)
OUTSIDE_TMP_CANDIDATES = (Path("/var/tmp/kotodama-r18-validation"),
                          Path("/tmp/kotodama-r18-validation"))
STDOUT_SHA_KEYS = ("stdout_sha256", "output_sha256")


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


def outside_tmp():
    """A writable temp root outside the repo (replay-frozen.py refuses in-repo)."""
    for candidate in OUTSIDE_TMP_CANDIDATES:
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            probe = candidate / ".write-probe"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
            return candidate
        except OSError:
            continue
    return None


def scratch_dir(name):
    path = ROOT / ".scratch" / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def run(parts, timeout=300, tmpdir=None, cwd=None, source_root=None):
    """Run one fixed read-only command; record source digests and stdout sha."""
    base = Path(source_root) if source_root is not None else ROOT
    argv = [sys.executable, *parts]
    child_env = dict(os.environ)
    child_env.update(TMPDIR=str(tmpdir or (ROOT / ".scratch")),
                     PYTHONDONTWRITEBYTECODE="1")
    item = {"command": shlex.join(["python3", *parts]), "date": today(),
            "argv": ["python3", *parts]}
    try:
        source = safe_path(parts[0]) if base == ROOT else (base / parts[0]).resolve()
        item["source_sha256_before"] = sha(source.read_bytes())
        proc = subprocess.run(argv, cwd=str(cwd or ROOT), capture_output=True,
                              timeout=timeout, env=child_env)
        item["source_sha256_after"] = sha(source.read_bytes())
        item["source_unchanged"] = (item["source_sha256_before"]
                                    == item["source_sha256_after"])
        item.update(exit=proc.returncode if item["source_unchanged"] else None,
                    stdout_sha256=sha(proc.stdout), stderr_sha256=sha(proc.stderr),
                    stdout=proc.stdout.decode("utf-8", "replace"),
                    stdout_tail=proc.stdout.decode("utf-8", "replace")[-1600:],
                    stderr_tail=proc.stderr.decode("utf-8", "replace")[-1600:])
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


def baseline_sha(rev, relative):
    try:
        blob = git("cat-file", "blob", f"{rev}:{relative}")
    except ValueError:
        return None
    return sha(blob)


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


def baseline_mirror(revision, prefixes, name):
    """A `.scratch` mirror of the baseline revision's `prefixes` (git archive)."""
    target = scratch_dir(name)
    if not (target / ".mirror-revision").is_file() or \
            (target / ".mirror-revision").read_text(encoding="utf-8").strip() != revision:
        if target.exists():
            for child in sorted(target.iterdir()):
                if child.is_dir():
                    import shutil
                    shutil.rmtree(child)
                else:
                    child.unlink()
        payload = git("archive", "--format=tar", revision, "--", *prefixes)
        with tarfile.open(fileobj=__import__("io").BytesIO(payload)) as archive:
            archive.extractall(target)
        (target / ".mirror-revision").write_text(revision + "\n", encoding="utf-8")
    return target


def findings_from_stdout(text):
    """The gate's plain-text finding lines as (id, severity, where, detail)."""
    rows = []
    for line in text.splitlines():
        match = re.match(r"^(FINDING|NOTE) ([^:]+): \[([^\]]+)\] (\S+) — (.*)$", line)
        if match:
            rows.append((match.group(2).strip(), match.group(3).strip(),
                         match.group(4).strip(), match.group(5).strip()))
    return rows


def findings_from_json(text):
    """The gate's --json document's findings as (id, severity, where, detail)."""
    try:
        document = strict_json(text)
    except (ValueError, TypeError):
        return None, "not JSON"
    rows = []
    for item in document.get("findings") or []:
        if not isinstance(item, dict):
            return None, "finding is not a mapping"
        rows.append((str(item.get("id")), str(item.get("severity")),
                     str(item.get("where")), str(item.get("detail", ""))))
    return rows, None


def holds_key(items):
    return {(str(item.get("id")), str(item.get("severity")), str(item.get("where")))
            for item in items if isinstance(item, dict)}


def with_severity(items, severity):
    """Expected rows may omit the severity field; their container names it."""
    return [dict(item, severity=item.get("severity") or severity)
            for item in items if isinstance(item, dict)]


def compare_findings(observed, expected_doc):
    holds = with_severity(expected_doc.get("holds") or [], "hold")
    notes = with_severity(expected_doc.get("notes") or [], "note")
    fails = with_severity(expected_doc.get("fails") or [], "fail")
    expected_items = holds + notes + fails
    observed_key = holds_key([{"id": row[0], "severity": row[1], "where": row[2]}
                              for row in observed])
    expected_key = holds_key(expected_items)
    observed_counts = {severity: sum(1 for item in observed_key if item[1] == severity)
                       for severity in ("hold", "note", "fail")}
    expected_counts = {severity: sum(1 for item in expected_key if item[1] == severity)
                       for severity in ("hold", "note", "fail")}
    details = {(str(item.get("id")), str(item.get("where"))): item.get("detail")
               for item in expected_items}
    detail_mismatch, details_pinned = [], 0
    for row in observed:
        key = (row[0], row[2])
        if key in details and details[key] is not None:
            details_pinned += 1
            if str(details[key]) != row[3]:
                detail_mismatch.append(key)
    return {
        "observed": sorted(observed_key), "expected": sorted(expected_key),
        "missing": sorted(expected_key - observed_key),
        "extra": sorted(observed_key - expected_key),
        "observed_counts": observed_counts, "expected_counts": expected_counts,
        "declared_counts": expected_doc.get("counts") if isinstance(expected_doc, dict) else None,
        "detail_mismatch": sorted(detail_mismatch), "details_pinned": details_pinned,
    }


def load_strict(text):
    import runpy
    namespace = runpy.run_path(str(ROOT / PROJECTOR))
    return namespace["load_packet_strict"](text)


def replay_manifest(manifest, tmpdir, timeout=300):
    """Run tools/replay-frozen.py --json over one manifest; parse the receipt."""
    argv = ["tools/replay-frozen.py", str(manifest), "--json"]
    item = run(argv, timeout=timeout, tmpdir=tmpdir)
    item["manifest"] = str(manifest)
    try:
        document = strict_json(item.get("stdout") or "")
    except (ValueError, TypeError):
        document = None
    item["receipt"] = document
    if document:
        summary = document.get("summary") or {}
        item.update(rows_total=summary.get("rows"), reproduced=summary.get("reproduced"),
                    mismatch=summary.get("mismatch"),
                    could_not_evaluate=summary.get("could_not_evaluate"),
                    rows=[{"line": row.get("line"), "gate": row.get("gate"),
                           "status": row.get("status"), "reason": row.get("reason"),
                           "detail": row.get("detail")}
                          for row in (document.get("rows") or [])])
    return item


def frozen_manifests():
    """Every candidate round-18 frozen manifest (new generation), deduplicated."""
    found = []
    for pattern in FROZEN_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            if path.is_file() and path.name == "MANIFEST.tsv":
                relative = path.relative_to(ROOT).as_posix()
                if relative.startswith("tools/gates/frozen/round-11"):
                    continue  # the filed round-11 generation, replayed separately
                if relative not in found:
                    found.append(relative)
    return found


def sha256_of(path):
    return sha(Path(path).read_bytes())


def scan_all_files(prefixes):
    """Every text file under the prefixes (relative paths, sorted)."""
    out = []
    for prefix in prefixes:
        for relative in scan_files(prefix):
            if relative not in out:
                out.append(relative)
    return out


def text_mentions(text, digest):
    """A digest is named by its 64-hex form or a >=8-hex prefix."""
    if not digest:
        return False
    for length in (64, 40, 16, 12, 8):
        if len(digest) >= length and digest[:length] in text:
            return True
    return False


# ------------------------------------------------------------------ claim O


def d2_invocations(root, tmpdir, source_root):
    """The D2-path invocations claim O pins, measured at `root`."""
    return {
        "default": run([GATE], tmpdir=tmpdir, cwd=root, source_root=source_root),
        "json": run([GATE, "--json"], tmpdir=tmpdir, cwd=root, source_root=source_root),
        "frozen-row": run([GATE, R11_TYPED], tmpdir=tmpdir, cwd=root,
                          source_root=source_root),
        "selftest": run([GATE, "--selftest"], tmpdir=tmpdir, cwd=root,
                        source_root=source_root),
    }


def run_verdict(item):
    return {"command": item.get("command"), "exit": item.get("exit"),
            "stdout_sha256": item.get("stdout_sha256"),
            "error": item.get("error")}


def selfcheck_verdict(item):
    text = (item.get("stdout") or "") + (item.get("stderr_tail") or "")
    match = re.search(r"(\d+)\s*/\s*(\d+)\s+checks? passed", text)
    return {"exit": item.get("exit"),
            "passed": int(match.group(1)) if match else None,
            "total": int(match.group(2)) if match else None}


def gate_flags(help_item):
    """The CLI switches the live gate advertises (`--help`)."""
    return sorted(set(re.findall(r"--[a-z][a-z-]+", help_item.get("stdout") or "")))


def d4_discovery(base=None, evidence=None):
    """Semantic discovery of the D4 artifacts (name only breaks ties)."""
    root = Path(base) if base is not None else ROOT / D4_DIR
    info = {"base": D4_DIR, "files": [], "components": [], "brief": None,
            "packet": None, "typed": None, "projection": None, "expected": None}
    if not root.is_dir():
        return info
    for path in sorted(root.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) \
            else path.as_posix()
        info["files"].append(relative)
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if evidence is not None:
            text = evidence.text(relative)
        else:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue
        name = Path(relative).name.lower()
        if "/components/" in relative:
            info["components"].append(relative)
            continue
        if TYPED_SCHEMA in text and name.startswith("packet"):
            info["typed"] = info["typed"] or relative
        elif name.startswith("expected-holds") or (name.startswith("expected")
                                                   and '"holds"' in text
                                                   and relative.endswith(".json")):
            info["expected"] = info["expected"] or relative
        elif name.startswith("typed-labels") or ('"typed_labels"' in text
                                                 and '"label_kinds"' in text):
            info["projection"] = info["projection"] or relative
        elif name.startswith("packet.") and relative.endswith((".yml", ".yaml")):
            info["packet"] = info["packet"] or relative
        elif "brief" in name:
            info["brief"] = info["brief"] or relative
    if info["brief"] is None:
        for relative in info["components"]:
            if "brief" in Path(relative).name.lower():
                info["brief"] = relative
                break
    return info


def baseline_pin_sweep(evidence, roots):
    """Every baseline pin in `roots` re-verified against the live bytes."""
    rows, problems = [], []
    for path in roots:
        relative = path.relative_to(ROOT).as_posix()
        evidence.bytes(relative)
        try:
            document = strict_json(path.read_text(encoding="utf-8"))
        except (ValueError, OSError, TypeError) as error:
            problems.append(f"{relative}: unreadable baseline: {error}")
            continue
        gate = str(document.get("gate") or "")
        gate_path = f"tools/gates/{gate}" if gate.endswith(".py") else f"tools/gates/{gate}.py"
        live_gate = sha256_of(ROOT / gate_path) if (ROOT / gate_path).is_file() else None
        gate_ok = live_gate == document.get("gate_sha256")
        if not gate_ok:
            problems.append(f"{relative}: gate_sha256 names {str(document.get('gate_sha256'))[:12]} "
                            f"but {gate_path} hashes {str(live_gate)[:12]}")
        inputs_ok, input_rows = True, []
        for key, digest in sorted((document.get("inputs") or {}).items()):
            candidate = path.parent / key
            if not candidate.is_file():
                candidate = ROOT / key
            live = sha256_of(candidate) if candidate.is_file() else None
            row_ok = live == digest
            inputs_ok = inputs_ok and row_ok
            input_rows.append({"key": key, "recorded": str(digest)[:12],
                               "live": str(live)[:12] if live else None, "ok": row_ok})
            if not row_ok:
                problems.append(f"{relative}: input {key} recorded {str(digest)[:12]} "
                                f"live {str(live)[:12] if live else 'missing'}")
        rows.append({"baseline": relative, "gate": gate, "gate_pin_ok": gate_ok,
                     "inputs_ok": inputs_ok, "inputs": input_rows})
    return rows, problems


def v207_pin_sweep(evidence, baseline_rev):
    """The round-16 expected-v2-07 helper pins re-checked; filed bytes pinned."""
    relative = R16_V207
    document = evidence.document(relative)
    filed_ok = None
    before = baseline_sha(baseline_rev, relative)
    if (ROOT / relative).is_file():
        filed_ok = (before == sha256_of(ROOT / relative))
    rows, problems, drifted = [], [], []
    for key, digest in sorted(((document or {}).get("inputs") or {}).items()):
        candidate = ROOT / key
        live = sha256_of(candidate) if candidate.is_file() else None
        ok = live == digest
        rows.append({"path": key, "recorded": str(digest)[:12],
                     "live": str(live)[:12] if live else None, "ok": ok})
    return {"filed_byte_identical": filed_ok, "pins": rows, "problems": problems}, \
        [row["path"] for row in rows if not row["ok"]]


def pin_ledger(changed_surfaces, texts):
    """Which round-18 record names each changed surface's before and after digests."""
    ledger = {}
    for path, surface in sorted(changed_surfaces.items()):
        naming = sorted(relative for relative, text in texts.items()
                        if text_mentions(text, surface["baseline_sha256"])
                        and text_mentions(text, surface["live_sha256"]))
        ledger[path] = {"before": surface["baseline_sha256"],
                        "after": surface["live_sha256"], "recorded_in": naming}
    return ledger


def measure_o(evidence, claims, common):
    failures, missing = [], set()

    def fail(message):
        failures.append(message)

    base = common["baseline_rev"]
    outside = common["outside_tmp"]
    d4 = common["d4"]
    measurement = {}

    # ---- O1 the generalization landed, on the pinned surfaces -------------
    surfaces = {}
    for path in PINNED_TOOL_SURFACES:
        before = baseline_sha(base, path)
        live = sha256_of(ROOT / path) if (ROOT / path).is_file() else None
        surfaces[path] = {"baseline_sha256": before, "live_sha256": live,
                          "changed": before != live}
    measurement["surfaces"] = surfaces
    changed_surfaces = {path: surface for path, surface in surfaces.items()
                        if surface["changed"]}
    if not changed_surfaces:
        fail("no pinned tool surface changed: the assembler-identity generalization "
             "did not land on the gate/adapter/projector/serializer")

    # ---- O2 default D2 behaviour byte-identical vs the baseline mirror ----
    mirror = baseline_mirror(base, ("tools", D2_DIR), "x03-baseline-mirror")
    before_runs = d2_invocations(mirror, ROOT / ".scratch", mirror)
    after_runs = d2_invocations(ROOT, outside or (ROOT / ".scratch"), ROOT)
    behaviour = {}
    for name in ("default", "json", "frozen-row", "selftest"):
        before_item, after_item = before_runs[name], after_runs[name]
        behaviour[name] = {"before": run_verdict(before_item),
                           "after": run_verdict(after_item),
                           "stdout_identical": before_item.get("stdout_sha256")
                           == after_item.get("stdout_sha256"),
                           "exit_identical": before_item.get("exit") == after_item.get("exit"),
                           "self_check": selfcheck_verdict(after_item)}
    measurement["d2_path"] = behaviour
    for name in ("default", "frozen-row"):
        item = behaviour[name]
        if not item["stdout_identical"]:
            fail(f"default D2 behaviour is not byte-identical for the {name} invocation: "
                 f"baseline stdout {item['before']['stdout_sha256']}, live "
                 f"{item['after']['stdout_sha256']}")
        if item["after"]["exit"] != 0:
            fail(f"{name} invocation exited {item['after']['exit']} (expected 0)")
    if behaviour["frozen-row"]["after"]["stdout_sha256"] != R11_TYPED_ROW_STDOUT_SHA:
        fail("the frozen-row invocation no longer reproduces the round-11 filed stdout pin "
             f"{R11_TYPED_ROW_STDOUT_SHA[:12]}")
    if not behaviour["default"]["exit_identical"] or behaviour["default"]["after"]["exit"] != 0:
        fail("default D2 gate invocation is not green at exit 0")
    json_before = findings_from_json(before_runs["json"].get("stdout") or "")
    json_after = findings_from_json(after_runs["json"].get("stdout") or "")
    json_ok = (json_after[0] is not None and json_before[0] is not None
               and {tuple(row) for row in json_before[0]} == {tuple(row) for row in json_after[0]}
               and after_runs["json"].get("exit") == 0)
    measurement["json_findings_identical"] = json_ok
    if not json_ok:
        fail("the --json document's finding set/exit changed for the default D2 path")
    if after_runs["json"].get("stdout_sha256") != R11_JSON_STDOUT_SHA:
        fail("the default --json run no longer reproduces the round-11 filed stdout pin "
             f"{R11_JSON_STDOUT_SHA[:12]}")
    measurement["default_stdout_matches_round18_receipt"] = (
        after_runs["default"].get("stdout_sha256") == DEFAULT_STDOUT_SHA_OBSERVED)
    if behaviour["selftest"]["after"]["exit"] != 0:
        fail(f"gate --selftest exited {behaviour['selftest']['after']['exit']}")
    measurement["gate_flags"] = gate_flags(
        run([GATE, "--help"], tmpdir=ROOT / ".scratch"))
    # the round-17 D4 manifest (5 rows over the D4 packet) must still replay green
    r17_d4 = replay_manifest(R17_D4_MANIFEST, outside)
    measurement["round17_d4_replay"] = {key: r17_d4.get(key) for key in
                                        ("exit", "rows_total", "reproduced", "mismatch",
                                         "could_not_evaluate")}
    if r17_d4.get("receipt") is None:
        missing.add(R17_D4_MANIFEST)
        fail(f"no round-17 D4 manifest receipt: {r17_d4.get('error')}")
    elif r17_d4.get("exit") != 0 or (r17_d4.get("reproduced") or 0) != \
            (r17_d4.get("rows_total") or -1):
        fail(f"the round-17 D4 manifest no longer replays green: exit "
             f"{r17_d4.get('exit')}, {r17_d4.get('reproduced')}/"
             f"{r17_d4.get('rows_total')} reproduced")

    # ---- O3 the declared assembler pin is accepted, and fails closed ------
    declared = {}
    if d4["packet"]:
        declared["packet-run"] = run([GATE, d4["packet"]], tmpdir=outside,
                                     cwd=ROOT)
    if d4["typed"]:
        declared["typed-run"] = run([GATE, d4["typed"]], tmpdir=outside, cwd=ROOT)
    flag_parts = [GATE]
    for flag, key in (("--assembler", "assembler"), ("--projection", "projection"),
                      ("--expected", "expected")):
        if flag in measurement["gate_flags"]:
            if key == "assembler":
                flag_parts += [flag, D4_ASSEMBLER]
            elif key == "projection" and d4["projection"]:
                flag_parts += [flag, d4["projection"]]
            elif key == "expected" and d4["expected"]:
                flag_parts += [flag, d4["expected"]]
    if d4["packet"] and len(flag_parts) > 1:
        declared["flag-run"] = run([*flag_parts, d4["packet"]], tmpdir=outside, cwd=ROOT)
    measurement["declared_runs"] = {name: run_verdict(item)
                                    for name, item in declared.items()}
    if d4["packet"]:
        if declared["packet-run"].get("exit") != 0:
            fail("the generalized gate does not accept the D4 packet at exit 0: "
                 f"{declared['packet-run'].get('exit')} "
                 f"{(declared['packet-run'].get('stdout_tail') or '')[-240:]}")
        if "flag-run" in declared and declared["flag-run"].get("exit") != 0:
            fail("the flag-declared assembler path is not green at exit 0")
    else:
        missing.add(f"{D4_DIR}/packet.d4.yml")

    # negative control 1: a forged assembler self-pin must fail closed
    if d4["packet"]:
        text = evidence.text(d4["packet"])
        forged_path = scratch_dir("x03") / "forged-assembler-pin.yml"
        match = re.search(r"(assembler_sha256:\s*)([0-9a-f]{64})", text)
        if match:
            forged = text.replace(match.group(2), "0" * 64, 1)
            forged_path.write_text(forged, encoding="utf-8")
            forged_run = run([GATE, forged_path.relative_to(ROOT).as_posix()],
                             tmpdir=outside, cwd=ROOT)
            measurement["forged_assembler_pin"] = run_verdict(forged_run)
            if forged_run.get("exit") == 0:
                fail("a forged assembler self-pin was accepted (exit 0)")
        else:
            measurement["forged_assembler_pin"] = {
                "note": "the D4 packet carries no assembly.assembler_sha256 self-pin; the "
                        "declared-generator negative (control 2) covers the identity leg"}

    # negative control 2: a wrong generator must fail closed
    if d4["packet"]:
        text = evidence.text(d4["packet"])
        wrong_path = scratch_dir("x03") / "wrong-generator.yml"
        wrong = re.sub(r"(generator:\s*)(\S*assemble-culture-d4\.py)",
                       lambda m: m.group(1) + '"tools/assemble-d2.py"', text, count=1)
        if wrong != text:
            wrong_path.write_text(wrong, encoding="utf-8")
            wrong_run = run([GATE, wrong_path.relative_to(ROOT).as_posix()],
                            tmpdir=outside, cwd=ROOT)
            measurement["wrong_generator"] = run_verdict(wrong_run)
            if wrong_run.get("exit") == 0:
                fail("a packet declaring the wrong assembler was accepted (exit 0)")
        else:
            fail("the D4 packet carries no generator declaration to tamper")

    # negative control 3: a tampered expected set (flag form) must fail closed
    if d4["expected"] and d4["packet"] and "--expected" in measurement["gate_flags"]:
        document = evidence.document(d4["expected"])
        if document:
            tampered = {key: value for key, value in document.items() if key != "counts"}
            holds = [dict(item) for item in (document.get("holds") or [])]
            if holds:
                holds[0]["where"] = "GAR-99"
            tampered["holds"] = holds
            tampered_path = scratch_dir("x03") / "tampered-expected.json"
            tampered_path.write_text(json.dumps(tampered, indent=1, sort_keys=True) + "\n",
                                     encoding="utf-8")
            tampered_run = run([GATE, "--expected", tampered_path.relative_to(ROOT).as_posix(),
                                d4["packet"]], tmpdir=outside, cwd=ROOT)
            measurement["tampered_expected"] = run_verdict(tampered_run)
            if tampered_run.get("exit") == 0:
                fail("a tampered expected hold set passed the gate (exit 0)")

    # ---- O4 the re-pin cascade -------------------------------------------
    filed_pins = {}
    for path in (R11_MANIFEST, R11_RECEIPT, R11_TYPED, R11_TYPED_ROW_OUT):
        before = baseline_sha(base, path)
        live = sha256_of(ROOT / path) if (ROOT / path).is_file() else None
        tracked = before is not None
        filed_pins[path] = {"baseline_sha256": before, "live_sha256": live,
                            "tracked_in_baseline": tracked,
                            "filed_byte_identical": (before == live) if tracked else None}
        if tracked:
            if before != live:
                fail(f"filed round-11 pin bytes changed: {path}")
        else:
            filed_pins[path]["note"] = ("git-ignored (.log): the recorded stdout pin "
                                        f"{R11_TYPED_ROW_STDOUT_SHA[:12]} is its receipt")
            if live != R11_TYPED_ROW_STDOUT_SHA:
                fail(f"the untracked frozen run log {path} no longer hashes the recorded "
                     f"round-11 stdout pin")
    measurement["round11_filed_pins"] = filed_pins

    r11 = replay_manifest(R11_MANIFEST, outside)
    measurement["round11_replay"] = {key: r11.get(key) for key in
                                     ("exit", "manifest", "rows_total", "reproduced",
                                      "mismatch", "could_not_evaluate", "rows")}
    if r11.get("receipt") is None:
        fail(f"round-11 replay produced no JSON receipt: {r11.get('error')} "
             f"{(r11.get('stderr_tail') or '')[-200:]}")
    else:
        typed_rows = [row for row in (r11.get("rows") or []) if row.get("gate") == GATE]
        other_rows = [row for row in (r11.get("rows") or []) if row.get("gate") != GATE]
        if not typed_rows:
            fail("round-11 replay found no typed-pipeline-gate row")
        for row in other_rows:
            if row.get("status") != "reproduced":
                fail(f"round-11 row {row.get('line')} ({row.get('gate')}) no longer "
                     f"reproduces: {row.get('status')}/{row.get('reason')}")
        gate_changed = surfaces[GATE]["changed"]
        for row in typed_rows:
            if gate_changed and row.get("status") == "reproduced":
                fail("the round-11 typed row still reproduces although the gate bytes "
                     "changed: the filed pin no longer separates the generations")
            if gate_changed and row.get("reason") not in ("gate_digest_mismatch",):
                fail(f"the round-11 typed row's cascade reading is "
                     f"{row.get('status')}/{row.get('reason')} (expected "
                     f"could-not-evaluate/gate_digest_mismatch)")
            if not gate_changed and row.get("status") != "reproduced":
                fail("the round-11 typed row does not reproduce although the gate "
                     "bytes are unchanged")

    manifests = frozen_manifests()
    measurement["round18_manifests"] = manifests
    if not manifests:
        missing.add("tools/gates/frozen/round-18*/MANIFEST.tsv")
        fail("no round-18 frozen generation was found to carry the new pins")
    for manifest in manifests:
        replay = replay_manifest(manifest, outside)
        measurement.setdefault("round18_replays", {})[manifest] = {
            key: replay.get(key) for key in ("exit", "rows_total", "reproduced",
                                             "mismatch", "could_not_evaluate")}
        if replay.get("exit") != 0 or (replay.get("reproduced") or 0) != \
                (replay.get("rows_total") or -1):
            fail(f"round-18 frozen manifest does not replay green: {manifest} "
                 f"(exit {replay.get('exit')}, {replay.get('reproduced')}/"
                 f"{replay.get('rows_total')} reproduced)")

    # the before/after ledger: a round-18 record must name each re-pinned surface
    ledger_prefixes = [ROUND_DIR, *(Path(manifest).parent.as_posix()
                                    for manifest in manifests)]
    texts = {}
    for relative in scan_all_files([p for p in ledger_prefixes
                                    if (ROOT / p).is_dir()]):
        if relative in (RUNNER, OUTPUT):
            continue
        if "/civ/" in relative and relative.endswith(".md"):
            continue  # civ receipts are claim-C evidence, not the pin ledger
        texts[relative] = evidence.text(relative)
    ledger = pin_ledger(changed_surfaces, texts)
    measurement["pin_ledger"] = ledger
    for path, entry in ledger.items():
        if not entry["recorded_in"]:
            fail(f"no round-18 record names the before/after digests of the re-pinned "
                 f"surface {path}")

    # the round-9 baseline pins still hold, and the round-18 revision re-pins verify
    r9_roots = sorted(ROOT.glob(f"{R9_BASELINES}/**/expected.json")) + \
        sorted(ROOT.glob(f"{R9_EXPECTED}/**/expected.json"))
    r9_rows, r9_problems = baseline_pin_sweep(evidence, r9_roots)
    measurement["round9_pins"] = {"baselines": len(r9_rows), "problems": r9_problems,
                                  "rows": r9_rows}
    for problem in r9_problems:
        fail(f"round-9 baseline pin broken: {problem}")
    if not r9_rows:
        missing.add(R9_BASELINES)
        fail("no round-9 baseline pins were found to re-verify")
    post_roots = sorted(ROOT.glob("tools/gates/frozen/*/r18*/expected.json")) + \
        sorted(ROOT.glob(f"{ROUND_DIR}/**/r18*/expected.json"))
    post_rows, post_problems = baseline_pin_sweep(evidence, post_roots)
    measurement["round18_revision_pins"] = {"baselines": len(post_rows),
                                            "problems": post_problems, "rows": post_rows,
                                            "roots": [path.relative_to(ROOT).as_posix()
                                                      for path in post_roots]}
    for problem in post_problems:
        fail(f"round-18 baseline revision pin broken: {problem}")
    if not post_rows:
        missing.add("tools/gates/frozen/*/r18-post/expected.json")
        fail("the round-9 re-pin landed no round-18 baseline revision to verify")

    # the round-16 v2-07 pins re-check, with a re-pin record for drifted helpers
    v207, drifted = v207_pin_sweep(evidence, base)
    measurement["round16_v207"] = v207
    if v207["filed_byte_identical"] is False:
        fail(f"filed {R16_V207} bytes changed")
    if drifted:
        regeneration = [relative for relative in (measurement.get("round18_manifests") or [])
                        if "v2" in relative or "handoff" in relative]
        covered = []
        for path in drifted:
            before = baseline_sha(base, path)
            live = sha256_of(ROOT / path) if (ROOT / path).is_file() else None
            if (before, live) == (None, None):
                continue
            hit = [relative for relative, text in texts.items()
                   if text_mentions(text, before) and text_mentions(text, live)]
            if hit:
                covered.append({"path": path, "recorded_in": hit[:3]})
        measurement["round16_v207_repin"] = {"drifted": drifted, "covered": covered,
                                             "regenerated_manifests": regeneration}
        for path in drifted:
            if not any(entry["path"] == path for entry in covered):
                fail(f"round-16 v2-07 pin drift on {path} has no round-18 re-pin record")

    # ---- O5 regressions ---------------------------------------------------
    regressions = {
        "battery": run(["tools/check-gate-battery.py"], tmpdir=ROOT / ".scratch"),
        "battery-3root": run(["tools/check-gate-battery.py",
                              "--baselines-root", "tools/gates/expected",
                              "--baselines-root", "tools/gates/frozen",
                              "--baselines-root", R9_BASELINES],
                             tmpdir=ROOT / ".scratch"),
        "battery-selftest": run(["tools/check-gate-battery.py", "--selftest"],
                                tmpdir=ROOT / ".scratch"),
        "craft-selftest": run(["tools/check-craft-exercise.py", "--selftest"],
                              tmpdir=ROOT / ".scratch"),
        "evidence-coupling-selftest": run(["tools/check-evidence-coupling.py", "--selftest"],
                                          tmpdir=ROOT / ".scratch"),
        "replay-frozen-selftest": run(["tools/replay-frozen.py", "--selftest"],
                                      tmpdir=outside),
        "assemble-d2-check": run([SERIALIZER, "--check"], tmpdir=ROOT / ".scratch"),
        "adapter-check": run([ADAPTER, "--check"], tmpdir=ROOT / ".scratch"),
        "projector-check": run([PROJECTOR, "--check"], tmpdir=ROOT / ".scratch"),
        "d3-check": run(["tools/assemble-culture-d3.py", "--check"],
                        tmpdir=ROOT / ".scratch"),
        "d4-check": run([D4_ASSEMBLER, "--check"], tmpdir=ROOT / ".scratch"),
        "adapter-selftest": run([ADAPTER, "--selftest"], tmpdir=ROOT / ".scratch"),
    }
    measurement["regressions"] = {name: run_verdict(item)
                                  for name, item in regressions.items()}
    for name, item in regressions.items():
        if item.get("exit") != 0:
            fail(f"regression {name} exited {item.get('exit')}: "
                 f"{(item.get('stdout_tail') or item.get('error') or '')[-200:]}")

    measurement["changed_surfaces"] = sorted(changed_surfaces)
    measurement["counts"] = metric(len(changed_surfaces),
                                   "sha256 the pinned surfaces against the baseline blobs")
    return result(failures, measurement, missing)


# ------------------------------------------------------------------ claim D


def d4_profile(evidence, d4):
    """The sha-pinned pipeline profile matching the D4 packet, if one landed."""
    document = evidence.document(TYPED_PIPELINES) if (ROOT / TYPED_PIPELINES).is_file() \
        else None
    profiles = []
    if isinstance(document, dict):
        for key in ("profiles", "pipelines", "families"):
            value = document.get(key)
            if isinstance(value, dict):
                profiles = list(value.values())
                break
            if isinstance(value, list):
                profiles = value
                break
    chosen, adapter = None, None
    for profile in profiles:
        if not isinstance(profile, dict):
            continue
        matches = json.dumps(profile)
        matched = (str(profile.get("id") or "").lower().startswith("d4")
                   or "culture-d4" in matches
                   or str(profile.get("expected") or "") == str(d4.get("expected"))
                   or str((profile.get("expected") or {}).get("path") if
                          isinstance(profile.get("expected"), dict) else "")
                   == str(d4.get("expected")))
        if matched and chosen is None:
            chosen = profile
    if isinstance(chosen, dict):
        value = chosen.get("adapter") or chosen.get("typed_adapter")
        if isinstance(value, dict):
            value = value.get("path")
        if isinstance(value, str) and value:
            adapter = value
    if adapter is None and (ROOT / D4_ADAPTER_FALLBACK).is_file():
        adapter = D4_ADAPTER_FALLBACK
    return {"profile_file": TYPED_PIPELINES, "schema": (document or {}).get("schema")
            if isinstance(document, dict) else None,
            "profiles": len(profiles), "chosen": chosen, "adapter": adapter}


def d4_typed_pins(typed_doc, d4, evidence, adapter=None):
    """Re-verify the delivered D4 typed packet's embedded digests against bytes."""
    pins = {}
    for container in ("assembly", "typed_assembly", "typed_pipeline"):
        block = typed_doc.get(container)
        if isinstance(block, dict):
            pins.update({key: value for key, value in block.items()
                         if isinstance(value, str) and len(value) == 64})
    adapter = adapter or ((d4.get("profile") or {}).get("adapter"))
    checks = {}
    live = {
        "packet_sha256": sha256_of(ROOT / d4["packet"]) if d4["packet"] else None,
        "projection_sha256": sha256_of(ROOT / d4["projection"]) if d4["projection"] else None,
        "assembler_sha256": sha256_of(ROOT / D4_ASSEMBLER),
        "generator_sha256": sha256_of(ROOT / D4_ASSEMBLER),
    }
    if adapter and (ROOT / adapter).is_file():
        live["adapter_sha256"] = sha256_of(ROOT / adapter)
    for key, value in pins.items():
        if key in live:
            checks[key] = {"pinned": value, "live": live[key], "ok": value == live[key]}
    return pins, checks


def measure_d(evidence, claims, common):
    failures, missing = [], set()

    def fail(message):
        failures.append(message)

    base = common["baseline_rev"]
    outside = common["outside_tmp"]
    d4 = common["d4"]
    measurement = {}

    for key in ("packet", "typed", "projection", "expected", "brief"):
        if not d4[key]:
            missing.add(f"{D4_DIR}/<{key}>")
            fail(f"D4 {key} artifact not found under {D4_DIR}")
    if not (ROOT / TYPED_PIPELINES).is_file():
        missing.add(TYPED_PIPELINES)
        fail(f"the declared-pipeline profile {TYPED_PIPELINES} is absent: the D4 "
             "flagless resolution channel (design §3) did not land")
    declared_adapter = (d4.get("profile") or {}).get("adapter")
    if declared_adapter and not (ROOT / declared_adapter).is_file():
        missing.add(declared_adapter)
        fail(f"the declared D4 adapter {declared_adapter} is absent: the gate cannot "
             "build the D4 typed packet (L1-build)")
    if len(d4["components"]) < 12:
        fail(f"D4 components: {len(d4['components'])} found, 12 required")
    measurement["discovery"] = {key: d4[key] for key in
                                ("packet", "typed", "projection", "expected", "brief")}
    measurement["components"] = len(d4["components"])
    for relative in d4["files"]:
        evidence.bytes(relative)

    # ---- D1 the generalized gate over the D4 packet ------------------------
    expected_doc = evidence.document(d4["expected"]) if d4["expected"] else None
    if d4["expected"] and expected_doc is None:
        fail("the D4 expected hold set is not strict JSON")
    if expected_doc is not None and expected_doc.get("schema") not in (None, HOLDS_SCHEMA):
        fail(f"D4 expected hold set schema is {expected_doc.get('schema')!r}")

    primary = json_run = None
    if d4["packet"]:
        primary = run([GATE, d4["packet"]], tmpdir=outside, cwd=ROOT)
        second = run([GATE, d4["packet"]], tmpdir=outside, cwd=ROOT)
        json_run = run([GATE, "--json", d4["packet"]], tmpdir=outside, cwd=ROOT)
        measurement["gate_runs"] = {"primary": run_verdict(primary),
                                    "second": run_verdict(second),
                                    "json": run_verdict(json_run)}
        measurement["determinism"] = metric(
            primary.get("stdout_sha256") == second.get("stdout_sha256"),
            "two gate runs over examples/culture-d4/packet.d4.yml, stdout sha256 compared")
        if primary.get("stdout_sha256") != second.get("stdout_sha256"):
            fail("two gate runs over the D4 packet are not byte-identical")
        if primary.get("exit") != 0:
            fail(f"the D4 gate run exited {primary.get('exit')}: "
                 f"{(primary.get('stdout_tail') or '')[-240:]}")
        stdout_rows = findings_from_stdout(primary.get("stdout") or "")
        json_rows, json_error = findings_from_json(json_run.get("stdout") or "")
        if json_error:
            fail(f"the D4 --json run produced no document: {json_error}")
        if json_rows is not None and stdout_rows:
            if sorted(json_rows) != sorted(stdout_rows):
                fail("the D4 --json finding set differs from the printed finding set")
        observed = json_rows if json_rows is not None else stdout_rows
        measurement["observed_findings"] = len(observed)
        if expected_doc is not None and observed:
            comparison = compare_findings(observed, expected_doc)
            measurement["hold_set"] = comparison
            if comparison["missing"]:
                fail(f"D4 hold set missing findings: {comparison['missing'][:4]}")
            if comparison["extra"]:
                fail(f"D4 hold set carries extra findings: {comparison['extra'][:4]}")
            if comparison["observed_counts"] != comparison["expected_counts"]:
                fail(f"D4 observed counts {comparison['observed_counts']} != expected "
                     f"{comparison['expected_counts']}")
            if comparison["declared_counts"] and \
                    comparison["observed_counts"] != comparison["declared_counts"]:
                fail(f"D4 observed counts {comparison['observed_counts']} != declared "
                     f"{comparison['declared_counts']}")
            if comparison["detail_mismatch"]:
                fail(f"D4 detail drift on {comparison['detail_mismatch'][:3]}")
            measurement["details_pinned"] = comparison["details_pinned"]
            if comparison["details_pinned"] < 1:
                fail("no D4 finding detail is pinned by the expected set")

    # ---- D2 the pre-declared ids reconciled --------------------------------
    fragment = evidence.document(R17_FRAGMENT)
    measurement["fragment"] = {"path": R17_FRAGMENT,
                               "holds": len((fragment or {}).get("holds") or []),
                               "notes": len((fragment or {}).get("notes") or [])}
    if fragment is None:
        missing.add(R17_FRAGMENT)
        fail("the round-17 expected-holds fragment is unreadable")
    reconciliation_texts = {}
    for relative in scan_all_files([R17_D4_DESIGN, ROUND_DIR, D4_DIR]):
        if relative in (RUNNER, OUTPUT):
            continue
        reconciliation_texts[relative] = evidence.text(relative)
    measurement["reconciliation_docs"] = len(reconciliation_texts)
    if fragment is not None and expected_doc is not None:
        fragment_key = holds_key(with_severity(fragment.get("holds") or [], "hold"))
        delivered_key = holds_key(with_severity(expected_doc.get("holds") or [], "hold"))
        delta = {"only_fragment": sorted(fragment_key - delivered_key),
                 "only_delivered": sorted(delivered_key - fragment_key)}
        measurement["fragment_delta"] = delta
        for id_value, where, _severity in delta["only_fragment"][:3]:
            named = [relative for relative, text in reconciliation_texts.items()
                     if id_boundary(text, id_value)]
            if not named:
                fail(f"dropped fragment id {id_value}@{where} is named in no round-17/18 record")
        disposition = sorted(relative for relative, text in reconciliation_texts.items()
                             if re.search(r"(?i)\b(amend(?:ment)?|delta|disposition|"
                                          r"reconcil)", text)
                             and (id_boundary(text, "D4L-") or "expected-holds" in text
                                  or "fragment" in text))
        measurement["delta_disposition_records"] = disposition[:6]
        if delta["only_fragment"] and not disposition:
            fail("the fragment -> delivered hold-set delta carries no round-18 "
                 "disposition record")
        named_ids = [id_value for id_value, _where, _severity in delivered_key
                     if not any(id_boundary(text, id_value)
                                for text in reconciliation_texts.values())]
        measurement["delivered_ids_unnamed"] = sorted(set(named_ids))
        if len(named_ids) > 0:
            fail(f"delivered hold ids named in no round-17/18 design doc: "
                 f"{sorted(set(named_ids))[:4]}")

    # ---- D3 determinism of the D4 typed packet ----------------------------
    profile = d4.get("profile") or {}
    adapter = profile.get("adapter") or (ADAPTER if not d4["typed"] else ADAPTER)
    measurement["profile"] = {key: profile.get(key)
                              for key in ("profile_file", "schema", "profiles", "adapter")}
    if d4["typed"] and d4["packet"] and d4["projection"]:
        emitted = scratch_dir("x03") / "d4-emitted.yml"
        emit_run = run([adapter, "--packet", d4["packet"], "--projection", d4["projection"],
                        "--emit", emitted.relative_to(ROOT).as_posix()],
                       tmpdir=ROOT / ".scratch")
        measurement["typed_emit"] = {**run_verdict(emit_run), "adapter": adapter}
        if emit_run.get("exit") != 0:
            check = run([adapter, "--packet", d4["packet"], "--projection", d4["projection"],
                         "--check", d4["typed"]], tmpdir=ROOT / ".scratch")
            measurement["typed_rebuild_check"] = run_verdict(check)
            if check.get("exit") != 0:
                fail(f"the D4 typed packet does not rebuild byte-identically: emit exit "
                     f"{emit_run.get('exit')}, check exit {check.get('exit')}")
        else:
            rebuilt = emitted.read_bytes()
            delivered = evidence.bytes(d4["typed"])
            measurement["typed_rebuild_byte_identical"] = rebuilt == delivered
            if rebuilt != delivered:
                fail("the adapter's fresh D4 build differs from the delivered typed packet")
    # strict parse + pins
    if d4["typed"]:
        typed_text = evidence.text(d4["typed"])
        try:
            loaded = load_strict(typed_text)
            typed_doc = loaded.get("packet")
            if typed_doc is None:
                fail(f"the D4 typed packet does not strict-parse: {loaded.get('findings', [])[:1]}")
        except Exception as error:  # the peer loader is fail-closed by design
            typed_doc = None
            fail(f"the D4 typed packet raised in the strict loader: {error}")
        if typed_doc is not None:
            if typed_doc.get("schema") != TYPED_SCHEMA:
                fail(f"D4 typed schema is {typed_doc.get('schema')!r}")
            if not typed_doc.get("typed_channel"):
                fail("the D4 typed packet carries no typed_channel routing")
            pins, pin_checks = d4_typed_pins(typed_doc, d4, evidence, adapter=adapter)
            measurement["typed_pins"] = pin_checks
            for key, record in pin_checks.items():
                if not record["ok"]:
                    fail(f"D4 typed pin {key} names {str(record['pinned'])[:12]} but live "
                         f"bytes hash {str(record['live'])[:12]}")

    # ---- D4 the resolution line names the declared assembler ---------------
    if primary is not None:
        live_assembler = sha256_of(ROOT / D4_ASSEMBLER)
        resolution = {"assembler_named": ("assemble-culture-d4.py"
                                          in (primary.get("stdout") or "")),
                      "assembler_sha_named": live_assembler[:12] in (primary.get("stdout") or "")
                      or live_assembler[:8] in (primary.get("stdout") or ""),
                      "assembler_sha256": live_assembler}
        measurement["resolution_line"] = resolution
        if not resolution["assembler_named"]:
            fail("the D4 gate run names no declared assembler in its resolution line")
        if not resolution["assembler_sha_named"]:
            fail("the D4 gate run names no assembler digest in its resolution line")

    # ---- D4 interop: the five gates over the D4 packets --------------------
    interop = {}
    for label, target in (("typed", d4["typed"]), ("packet", d4["packet"])):
        if not target:
            continue
        for name in GATE_NAMES:
            item = run([f"tools/gates/{name}", target], tmpdir=outside)
            interop[f"{label}:{name}"] = run_verdict(item)
            if item.get("exit") not in (0, 1):
                fail(f"gate {name} over the D4 {label} exited {item.get('exit')} "
                     f"(expected 0/1)")
    measurement["interop"] = interop

    # ---- D5 the D2 path untouched -----------------------------------------
    d2_untouched = {}
    for path in (D2_PACKET, D2_PROJECTION, D2_EXPECTED):
        before = baseline_sha(base, path)
        live = sha256_of(ROOT / path)
        d2_untouched[path] = {"baseline_sha256": before, "live_sha256": live,
                              "byte_identical": before == live}
        if before != live:
            fail(f"D2 contract artifact changed: {path}")
    if (ROOT / D2_TYPED).is_file():
        typed_doc = None
        try:
            typed_doc = load_strict((ROOT / D2_TYPED).read_text(encoding="utf-8"))["packet"]
        except Exception:
            typed_doc = None
        pin = str(((typed_doc or {}).get("assembly") or {}).get("adapter_sha256"))
        live_adapter = sha256_of(ROOT / ADAPTER)
        d2_untouched[D2_TYPED] = {"adapter_pin": pin[:12], "live_adapter": live_adapter[:12],
                                  "pin_ok": pin == live_adapter}
        if pin != live_adapter:
            fail("the D2 typed packet's adapter pin no longer matches the live adapter: "
                 "the D2 build product must be re-emitted in the same round it changes")
    measurement["d2_untouched"] = d2_untouched
    measurement["counts"] = metric(len(d4["files"]), "files discovered under the D4 tree")
    return result(failures, measurement, missing)


# ------------------------------------------------------------------ claim C


def r18_map_discovery(evidence):
    """The round-18 civ-map revision (name only breaks ties)."""
    candidates = []
    for pattern in (f"{ROUND_DIR}/civ-map*.json", f"{ROUND_DIR}/**/civ-map*.json",
                    f"{ROUND_DIR}/**/*map*.json"):
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file():
                continue
            relative = path.relative_to(ROOT).as_posix()
            if relative not in candidates:
                candidates.append(relative)
    best = None
    for relative in candidates:
        document = evidence.document(relative)
        rows = map_rows(document) if document else None
        if document and rows and (document.get("round") in (18, "18")
                                  or "r18" in Path(relative).name):
            best = relative
            break
    return best, candidates


def measure_c(evidence, claims, common):
    failures, missing = [], set()

    def fail(message):
        failures.append(message)

    base = common["baseline_rev"]
    measurement = {}

    revision, candidates = r18_map_discovery(evidence)
    measurement["candidates"] = candidates
    measurement["revision"] = revision
    if revision is None:
        missing.add(f"{ROUND_DIR}/civ-map*.json")
        fail("no round-18 civ-map revision was found")
        return result(failures, measurement, missing)

    document = evidence.document(revision)
    rows = map_rows(document) if document else None
    if not rows:
        fail(f"the round-18 map {revision} carries no rows")
        return result(failures, measurement, missing)
    by_file = {}
    for row in rows:
        entry = row_entry(row)
        if entry:
            by_file[entry] = row

    # ---- C1 the counting command reproduces 94 -----------------------------
    live_count = len([path for path in (ROOT / CIV_DIR).glob("*.md") if path.is_file()])
    declared_command = str(document.get("counting_command") or "")
    measurement["counting"] = {
        "declared_command": declared_command, "declared_count": document.get("count"),
        "live_count": live_count, "corpus_command": CIV_COUNT_COMMAND,
        "date": today()}
    if live_count != 94:
        fail(f"the civilizations counting command reproduces {live_count}, not 94")
    if document.get("count") not in (94, "94"):
        fail(f"the round-18 map declares count {document.get('count')!r}, not 94")
    if declared_command and "civilizations" not in declared_command:
        fail(f"the map's counting command does not count the civilizations tree: "
             f"{declared_command!r}")

    # ---- C2 the filed round-16 map is untouched ----------------------------
    before = baseline_sha(base, R16_MAP)
    live = sha256_of(ROOT / R16_MAP)
    measurement["round16_map"] = {"baseline_sha256": before, "live_sha256": live,
                                  "byte_identical": before == live}
    if before != live:
        fail(f"the filed round-16 map changed ({R16_MAP}): revisions must be new files")
    r16 = evidence.document(R16_MAP)
    r16_rows = map_rows(r16) if r16 else []
    r16_by_file = {row_entry(row): row for row in r16_rows if row_entry(row)}
    if len(r16_by_file) != 94:
        fail(f"the filed round-16 map no longer carries 94 rows ({len(r16_by_file)})")

    # ---- C3 the round-17 patch is applied exactly --------------------------
    patch = evidence.document(R17_PATCH)
    patch_rows = (patch or {}).get("rows") or []
    measurement["patch"] = {"path": R17_PATCH, "rows": len(patch_rows)}
    if patch is None or not patch_rows:
        missing.add(R17_PATCH)
        fail("the round-17 map patch is unreadable")
        return result(failures, measurement, missing)
    patch_sha = evidence.inputs.get(R17_PATCH)
    if patch_sha and document.get("applied_patch"):
        recorded = (document.get("applied_patch") or {}).get("sha256")
        measurement["patch_sha"] = {"live": patch_sha, "recorded_by_revision": recorded,
                                    "ok": recorded == patch_sha}
        if recorded and recorded != patch_sha:
            fail("the round-18 map records a different patch digest than the filed patch")
    transitions = {row_entry(row): row for row in (document.get("transitions") or [])}
    measurement["transitions"] = len(transitions)
    transitioned = set()
    attempts = []
    for row in patch_rows:
        entry = row_entry(row)
        transitioned.add(entry)
        target = by_file.get(entry)
        proposed = row.get("to") or {}
        if target is None:
            fail(f"the round-18 map drops the patched row for {entry}")
            continue
        mismatched = [key for key in ("status", "verified_at", "command", "evidence_path")
                      if key in proposed and str(target.get(key)) != str(proposed.get(key))]
        if mismatched:
            fail(f"row {entry} does not carry the round-17 patch: {mismatched} "
                 f"(map {[str(target.get(k))[:40] for k in mismatched]} vs patch "
                 f"{[str(proposed.get(k))[:40] for k in mismatched]})")
        if normalize_status(target.get("status")) not in STATUS_VOCAB:
            fail(f"row {entry} carries status {target.get('status')!r} outside "
                 f"{STATUS_VOCAB}")
        command = str(target.get("command") or "")
        recheck = ""
        transition_block = target.get("transition")
        if isinstance(transition_block, dict):
            recheck = str((transition_block.get("r18_recheck") or {}).get("command") or "")
        verified_r18 = str(target.get("verified_r18") or "")
        carrier = "\n".join([command, verified_r18, recheck])
        if not DATE_RE.search(str(target.get("verified_at") or "")) or \
                not COMMAND_RE.search(carrier):
            fail(f"row {entry}'s transitioned status carries no date+command "
                 f"(verified_at {target.get('verified_at')!r})")
        measurement.setdefault("command_carriers", {})[entry] = {
            "date": target.get("verified_at"),
            "carrier": ("command" if COMMAND_RE.search(command) else
                        "verified_r18" if COMMAND_RE.search(verified_r18) else
                        "transition.r18_recheck.command"),
            "patch_command_verbatim": str(proposed.get("command")) == command}
        pointer = target.get("evidence_path")
        if pointer and not (ROOT / str(pointer)).is_file():
            fail(f"row {entry}'s evidence pointer does not resolve: {pointer}")
        disposition = row.get("disposition") or {}
        if re.search(r"(?i)no replacement needed", str(disposition.get("kind") or "")):
            attempts.append(entry)
            fragment_text = ""
            if pointer and (ROOT / str(pointer)).is_file():
                fragment_text = evidence.text(str(pointer))
            if not (DATE_RE.search(fragment_text) and COMMAND_RE.search(fragment_text)
                    and ATTEMPT_RE.search(fragment_text)):
                fail(f"attempt-documented row {entry} carries no dated, command-carried "
                     f"attempt evidence in {pointer}")
        if entry in transitions:
            record = transitions[entry]
            if normalize_status(record.get("to_status")) != normalize_status(target.get("status")):
                fail(f"row {entry}: transitions[] and entries[] disagree on the landed status")
    measurement["attempt_rows"] = sorted(attempts)
    if len(attempts) != 5:
        fail(f"the round-17 patch documents {len(attempts)} attempt rows, not 5: {attempts}")

    # every other row must be carried verbatim from the round-16 map
    carried, drifted = 0, []
    for entry, row in sorted(r16_by_file.items()):
        if entry in transitioned:
            continue
        target = by_file.get(entry)
        if target is None:
            fail(f"the round-18 map drops the un-transitioned row {entry}")
            continue
        same = all(str(row.get(key)) == str((target or {}).get(key))
                   for key in ("status", "verified_at", "command", "evidence_path"))
        if same:
            carried += 1
        else:
            drifted.append(entry)
    measurement["rows_carried_verbatim"] = carried
    if drifted:
        fail(f"un-transitioned rows changed against the round-16 map: {drifted[:6]}")
    if carried != 82:
        fail(f"{carried} rows carried verbatim; the revision should carry 82 and "
             f"transition 12")
    if len(by_file) != 94:
        fail(f"the round-18 map carries {len(by_file)} rows, not 94")
    if document.get("complete") not in (True, "true"):
        fail("the round-18 map does not declare itself complete")
    measurement["counts"] = metric(len(by_file), "rows in the round-18 civ-map revision")
    return result(failures, measurement, missing)


# -------------------------------------------------------------- validation


def guard_preflight():
    spec = importlib.util.spec_from_file_location("round18_receipt_guard", ROOT / GUARD)
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
                    failures.append(f"Filed round 8-17 artifact not byte-identical: "
                                    f"{relative} ({disposition})")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"Cannot establish filed-byte preservation: {error}")
    return result(failures, {"baseline_revision": baseline, "files": rows,
                             "checked": metric(len(rows),
                                               "compare filed round-8..17 bytes with baseline")})


def corpus_preservation(baseline):
    """corpus/knowledge/** byte-identical; new corpus files are reported, not failed."""
    failures, rows, additions = [], [], []
    try:
        baseline_files = baseline_blobs(baseline, "corpus/knowledge")
        baseline_lessons = baseline_blobs(baseline, "corpus/lessons")
        for relative in sorted(baseline_files):
            current = ROOT / relative
            if not current.is_file():
                failures.append(f"corpus knowledge artifact missing: {relative}")
                continue
            live = sha(current.read_bytes())
            rows.append({"path": relative, "preservation":
                         "byte-identical" if live == sha(baseline_files[relative]) else "violation"})
            if live != sha(baseline_files[relative]):
                failures.append(f"corpus knowledge byte changed without a round-18 claim: "
                                f"{relative}")
        for relative in worktree_files("corpus/lessons"):
            if not (ROOT / relative).is_file():
                continue
            if relative not in baseline_files and relative not in baseline_lessons:
                additions.append(relative)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"Cannot establish corpus preservation: {error}")
    return result(failures, {"knowledge_files": len(rows), "rows": rows,
                             "lessons_additions": additions,
                             "checked": metric(len(rows),
                                               "compare corpus/knowledge bytes with baseline")})


def validate():
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(exist_ok=True)
    evidence = Evidence()
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    targets = evidence.document(f"{ROUND_DIR}/targets.json") or {}
    baseline = claims.get("baseline_revision")
    common = {"baseline_rev": baseline, "outside_tmp": outside_tmp(),
              "d4": d4_discovery(evidence=evidence)}
    common["d4"]["profile"] = d4_profile(evidence, common["d4"])
    for key in ("packet", "typed", "projection", "expected", "brief"):
        if common["d4"][key]:
            evidence.bytes(common["d4"][key])
    before = filed_snapshot()
    depth = measure_d(evidence, claims, common)
    coverage = measure_c(evidence, claims, common)
    operability = measure_o(evidence, claims, common)
    results = {"O": operability, "D": depth, "C": coverage}
    filed = filed_preservation(claims)
    corpus = corpus_preservation(baseline) if isinstance(baseline, str) else \
        result(["no baseline revision"], {})
    for check in (filed, corpus):
        if not check["passed"]:
            for item in results.values():
                item["failures"].extend(check["failures"])
                item["passed"] = False
    after = filed_snapshot()
    changes = [{"path": path, "before": before.get(path), "after": after.get(path)}
               for path in sorted(before.keys() | after.keys())
               if before.get(path) != after.get(path)]
    if changes:
        for item in results.values():
            item["failures"].append("Filed round-8..17 bytes/path set changed during "
                                    "validation; rerun on a settled tree")
            item["passed"] = False
    declared = {claim.get("id"): claim.get("axis") for claim in claims.get("claims", [])
                if isinstance(claim, dict)}
    if declared != {"O": "operability", "D": "depth", "C": "coverage"}:
        results["O"]["failures"].append(
            f"Round-18 declared claims do not match O/D/C: {declared}")
        results["O"]["passed"] = False
    seat_total = sum(value for value in (targets.get("workers") or {}).values()
                     if isinstance(value, int))
    if evidence.errors:
        for error in evidence.errors:
            consumer = "C" if CIV_DIR in error or R16_MAP in error else "D"
            results[consumer]["failures"].append(error)
            results[consumer]["passed"] = False
    # de-duplicate failures while keeping order
    for item in results.values():
        seen, unique = set(), []
        for failure in item["failures"]:
            if failure not in seen:
                seen.add(failure)
                unique.append(failure)
        item["failures"] = unique
        item["passed"] = item["passed"] and not unique
    return {
        "round": ROUND, "runner": RUNNER, "runner_sha256": sha((ROOT / RUNNER).read_bytes()),
        "counting_command": COMMAND, "date": today(),
        "baseline_revision": baseline,
        "targets_date": targets.get("date"),
        "claims_declared": declared,
        "declaration": {"claims_workers": claims.get("workers"), "target_seats": seat_total,
                        "note": "claims.json declares 64 workers; targets.json allocates "
                                "20 + 28 + 10 + 6 = 64 seats."},
        "acceptance_checks_passed": all(item["passed"] for item in results.values()),
        "claims": results, "input_sha256": dict(sorted(evidence.inputs.items())),
        "failures": [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                     for failure in item["failures"]],
        "missing_dependencies": sorted({path for item in results.values()
                                        for path in item["missing_dependencies"]}),
        "filed_rounds": {"baseline": filed["measurement"],
                         "corpus": corpus["measurement"],
                         "command": f"{COMMAND} (compare filed round-8..17 and "
                                    "corpus/knowledge bytes with the declared baseline, "
                                    "before and after checks)",
                         "date": today(),
                         "changed_during_validation": changes},
        "limits": [
            "Historical validators are never executed. Only fixed read-only "
            "check/selftest commands and this runner's own .scratch fixtures run; "
            "no command is executed from an evidence file.",
            "Filed rounds 8-17 and the round-16 civ map are compared with the "
            "declared baseline and must be byte-identical: this round's pins and "
            "revisions are NEW rows/files, never in-place edits of filed bytes.",
            "The frozen-replay subprocess runs with TMPDIR outside the repository "
            "because tools/replay-frozen.py refuses an in-repo mirror root by "
            "design; nothing is written into the lane by that subprocess.",
            "The round-11 generation's typed row is EXPECTED to read "
            "could-not-evaluate/gate_digest_mismatch once the gate is generalized: "
            "its recorded gate pin names the pre-generalization bytes, and the new "
            "pins live in the round-18 generation. The row's filed bytes are never "
            "edited.",
            "Claim C is a map revision over the round-17 dispositions: a "
            "transitioned row's evidence pointer must resolve and carry a dated, "
            "command-carried receipt; the freshness axis-move remains paused and no "
            "source freshness verdict, re-grade, or rank change is issued.",
            "D4 discovery is semantic (schema/filename) so a differently named "
            "artifact is still found; the canonical names are the D2 convention "
            "with a d4 suffix.",
            "All artifacts measured are NON-CANON; this receipt does not certify "
            "truth, canon, lore receipt, cultural permission, or any real-world "
            "clearance.",
        ],
    }


# ---------------------------------------------------------------- selftest


def selftest():
    """In-memory controls over the validator's own rules; no receipt is written."""
    controls = []

    def check(name, condition, detail=""):
        controls.append({"control": name, "passed": bool(condition),
                         "detail": "" if condition else str(detail)})

    expected = {"holds": [{"id": "X", "severity": "hold", "where": "A", "detail": "d1"},
                          {"id": "X", "severity": "hold", "where": "B", "detail": None}],
                "notes": [{"id": "N", "severity": "note", "where": "C", "detail": "d3"}],
                "counts": {"hold": 2, "note": 1, "fail": 0}}
    exact = [("X", "hold", "A", "d1"), ("X", "hold", "B", "d2"), ("N", "note", "C", "d3")]
    comparison = compare_findings(exact, expected)
    check("hold-set equality accepts the exact set",
          not comparison["missing"] and not comparison["extra"]
          and comparison["observed_counts"] == comparison["expected_counts"]
          and not comparison["detail_mismatch"], comparison)
    check("null expected details are not pinned", comparison["details_pinned"] == 2)
    missing = compare_findings(exact[:2], expected)
    check("a dropped hold is reported as missing", missing["missing"] == [("N", "note", "C")],
          missing["missing"])
    extra = compare_findings(exact + [("Z", "hold", "D", "d")], expected)
    check("an extra finding is reported", extra["extra"] == [("Z", "hold", "D")], extra["extra"])
    laundered = compare_findings(exact[:2] + [("N", "hold", "C", "d3")], expected)
    check("a note laundered into a hold fails the set equation",
          ("N", "note", "C") in laundered["missing"] and ("N", "hold", "C") in laundered["extra"],
          laundered)
    drift = compare_findings([("X", "hold", "A", "WRONG")] + exact[1:], expected)
    check("detail drift is caught", drift["detail_mismatch"] == [("X", "A")],
          drift["detail_mismatch"])
    inferred = with_severity([{"id": "X", "where": "A"}], "hold")
    check("severity is inferred from the container", inferred[0]["severity"] == "hold")
    stdout_rows = findings_from_stdout(
        "FINDING ID-1: [hold] WHERE-1 — detail one\n"
        "NOTE ID-2: [note] WHERE-2 — detail two\ngarbage\n")
    check("stdout finding lines parse", stdout_rows == [("ID-1", "hold", "WHERE-1", "detail one"),
                                                        ("ID-2", "note", "WHERE-2", "detail two")],
          stdout_rows)
    json_rows, json_error = findings_from_json(json.dumps(
        {"findings": [{"id": "I", "severity": "hold", "where": "W", "detail": "d"}]}))
    check("--json findings parse", json_error is None and json_rows == [("I", "hold", "W", "d")],
          (json_error, json_rows))
    check("--json non-documents are reported",
          findings_from_json("not json")[0] is None)
    check("digest naming matches full and truncated forms",
          text_mentions("sha 0123456789abcdef rest", "0123456789abcdef" + "0" * 48)
          and text_mentions("prefix 01234567 only", "0123456789abcdef")
          and not text_mentions("unrelated", "0123456789abcdef"))
    check("id boundary matching is not a substring test",
          id_boundary("D4L-RANK here", "D4L-RANK") and not id_boundary("XD4L-RANKY", "D4L-RANK"))
    check("status normalization collapses case and separators",
          normalize_status(" Stale_Fixed ") == "stale-fixed")
    check("entry normalization strips corpus prefixes",
          normalize_entry("corpus/knowledge/civilizations/inuit.md") == "inuit")
    check("map containers are found under their several key names",
          map_rows({"rows": [1]}) == [1] and map_rows({"entries": [2]}) == [2]
          and map_rows([{"file": "x"}]) == [{"file": "x"}] and map_rows({"nope": 1}) is None)
    check("row entry/status fall back across key names",
          row_entry({"civilization": "inuit.md"}) == "inuit"
          and row_status({"staleness": "stale-documented"}) == "stale-documented")
    try:
        strict_json('{"a": 1, "a": 2}')
        duplicate_rejected = False
    except ValueError:
        duplicate_rejected = True
    check("duplicate JSON keys are rejected", duplicate_rejected)
    for bad in ("/etc/passwd", "../outside", ".git/config"):
        try:
            safe_path(bad)
            refused = False
        except ValueError:
            refused = True
        check(f"unsafe evidence path refused: {bad}", refused)
    check("filed preservation classes", preservation_kind("a.md", b"x", b"x") == "byte-identical"
          and preservation_kind("a.md", b"x", b"xy") == "append-only"
          and preservation_kind("a.md", b"x", b"z") == "violation")
    check("attempt semantics are recognized",
          bool(ATTEMPT_RE.search("no replacement needed; locators kept"))
          and not bool(ATTEMPT_RE.search("locator replaced old->new")))
    check("date and command carriage are recognized",
          bool(DATE_RE.search("2026-10-18")) and bool(COMMAND_RE.search("curl probe"))
          and not bool(COMMAND_RE.search("in-repo battery")))
    tmp = outside_tmp()
    check("an outside-repo temp root is available",
          tmp is not None and not Path(tmp).resolve().is_relative_to(ROOT), tmp)
    synthetic = scratch_dir("x03-selftest") / "components"
    synthetic.mkdir(parents=True, exist_ok=True)
    (synthetic / "01-brief.yml").write_text("brief\n", encoding="utf-8")
    base_dir = synthetic.parent
    (base_dir / "packet.d4.yml").write_text('name: "selftest"\ncanon: "not canon"\n',
                                            encoding="utf-8")
    (base_dir / "typed-labels.d4.yml").write_text(
        '{"typed_labels": {}, "label_kinds": []}\n', encoding="utf-8")
    (base_dir / "expected-holds.json").write_text(
        '{"schema": "kotodama-typed-pipeline-holds-v1", "holds": [], "notes": [], '
        '"counts": {"hold": 0, "note": 0, "fail": 0}}\n', encoding="utf-8")
    (base_dir / "packet.d4.typed.yml").write_text(
        "schema: kotodama-typed-packet-v1\ntyped_channel: []\n", encoding="utf-8")
    found = d4_discovery(base_dir)
    check("D4 discovery classifies a synthetic tree",
          len(found["components"]) == 1 and found["packet"] and found["typed"]
          and found["projection"] and found["expected"] and found["brief"],
          {key: found[key] for key in ("packet", "typed", "projection", "expected", "brief")})
    help_run = run([GATE, "--help"], tmpdir=ROOT / ".scratch")
    check("run() records source stability and exit for a live tool",
          help_run.get("exit") == 0 and help_run.get("source_unchanged") is True
          and "typed-pipeline" in (help_run.get("stdout") or ""),
          {key: help_run.get(key) for key in ("exit", "source_unchanged", "error")})
    payload = {"runner": RUNNER, "command": f"{COMMAND} --selftest", "date": today(),
               "selftest_passed": all(item["passed"] for item in controls),
               "controls": controls,
               "passed": metric(sum(item["passed"] for item in controls),
                                "validator selftest controls"),
               "total": metric(len(controls), "validator selftest control inventory")}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["selftest_passed"] else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate round-18 O/D/C without touching filed rounds 8-17.")
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
