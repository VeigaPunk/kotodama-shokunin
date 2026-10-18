#!/usr/bin/env python3
"""Round-28 acceptance runner: claims D (law replay leg + RL-4 fix), O (final pin
sweep + regressions), C (the register-lexicon ceiling as craft knowledge).

Claim D — the register law gains a replay leg, and the packet_keys gap closes.
  Round 27 landed the register law (`examples/culture-d4/components/13-register-law.yml`,
  packet block `register_law:`, rows `RGL-01..RGL-05`) and its own review named the
  two defects this claim repairs:
    * **RL-1** — the law has no replay leg. Measured by the round-27 review: a row
      whose `force` is `no-such-force` produced **the same 12 findings** as a clean
      row, so the law was "a declaration with no teeth". This runner requires the
      delivered tree to carry a **checking leg** that names a `D4L-LAW-*` finding on
      a tampered row, and it measures that by **behaviour, not by shape**: it builds
      three tampered packets of its own (an unknown force, an unresolvable speaker,
      a consequence that names no delivered roll/rank machinery), runs the delivered
      leg on each, and requires each tamper to add a named `D4L-LAW-*` finding **line**
      the clean packet does not produce. The clean packet's own findings are reported,
      never required to be zero: the delivered law has real defects and the D seat's
      design measures six honest findings on the clean bytes, two of whose classes are
      saturated — so the delta is taken over finding lines, not class ids. It also
      **re-derives the resolutions itself** (this runner's own reader of the law) so
      the delivered leg is graded against an independent reading of what each tamper
      should break.
    * **RL-4** — `03-orthography.yml` and `09-costumes.yml` declare no `packet_keys`
      covering their record blocks, so `OR-01..03`, `LI-01..03` and `EN-01..02` never
      reach the packet. The fix is measured two ways: the components must declare the
      keys, and the records must be **present in the packet as records** (a list block
      row carrying the id), not merely as prose cross-references. The named-holds set
      must be revised honestly to name the round-28 landing.
    * the D4 typed gate, the argot gate and the three assemblers/adapter/projector
      must be green, and the RL-3 ceiling must be recorded as a design constraint in
      the knowledge entry (measured under claim C).

Claim O — the final build-round pin sweep, and regressions.
  The RL-4 packet change moves the D4 packet surface once more. This runner sweeps
  **every row that pins a D4 surface** — the frozen manifests, the battery baselines
  (`tools/gates/expected/**`, `tools/gates/frozen/**`), the typed-pipeline profile,
  the hold set, the v3 read-set baseline and the historical round-20/22/26/27 rows —
  and classifies each declared digest as `green` (equal to the live bytes) or `drift`.
  Every drifted row must be re-pinned by a **NEW round-28 row** naming the surface and
  carrying the live digest; filed rounds 8-27 stay byte-identical. The battery must
  read `pass 7 / fail 0 / unevaluable 0` with `coverage 9/9` and every registered
  baseline pinned, the frozen-verdict replay and the handoff profiles must be green,
  and the fixed regression inventory must pass.

Claim C — the ceiling as craft knowledge.
  The RL-3 ceiling (a register's derivation operation constrains which semantic fields
  it can natively spell: the delivered `stamp` register's five legal/institutional
  abstractions all refuse `reverse`) is recorded in **two** places: as an amendment
  entry in `corpus/knowledge/linguistics/register-strata-attestation.md` — a **new
  section**, citing the round-27 measurements, with every earlier section header still
  present (an amendment, never an in-place rewrite) — and as a **new sourced knowledge
  entry** on register-lexicon ceilings, absent from the declared baseline revision by
  Git blob identity, frontmatter-complete, gap-named, decision-record carrying, grounded
  in round-27 artifacts and dated external sources, and making no canon claim.
  `corpus/README.md` must carry a new revision indexing the new entry whose partition
  headers reproduce the measured tree.

Run only in the lane root or an isolated clone under its .scratch:
  python3 reports/round-28/run-validation.py             (measure + write receipt)
  python3 reports/round-28/run-validation.py --check     (measure only, print)
  python3 reports/round-28/run-validation.py --selftest  (dependency-free controls)
  python3 reports/round-28/run-validation.py --wait 600  (poll late dependencies)
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
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
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-28"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
CLAIMS = f"{ROUND_DIR}/claims.json"
TARGETS = f"{ROUND_DIR}/targets.json"

D4_DIR = "examples/culture-d4"
D4_COMPONENTS = f"{D4_DIR}/components"
PACKET_D4 = f"{D4_DIR}/packet.d4.yml"
PACKET_D4_TYPED = f"{D4_DIR}/packet.d4.typed.yml"
D4_PROJECTION = f"{D4_DIR}/typed-labels.d4.yml"
D4_HOLDS = f"{D4_DIR}/expected-holds.json"
D4_ASSEMBLER = "tools/assemble-culture-d4.py"
D4_ADAPTER = "tools/assemble-d4-typed.py"
PROJECTOR = "tools/d2-typed-labels.py"
ARGOT_GATE = "tools/gates/argot-derivation-gate.py"
TYPED_GATE = "tools/gates/typed-pipeline-gate.py"
NAMING_GATE = "tools/gates/naming-collision-gate.py"
D4_LABEL_GATE = "tools/gates/d4-typed-labels-check-gate.py"
D4_ASSEMBLY_GATE = "tools/gates/d4-assembly-check-gate.py"
BATTERY = "tools/check-gate-battery.py"
REPLAY = "tools/replay-frozen.py"
HANDOFF = "tools/exercise-handoff-e2e.py"
TYPED_PROFILES = "tools/gates/typed-pipelines.json"
V3_BASELINE_FALLBACK = f"{ROUND_DIR}/pinsweep/v3-baseline-r28/expected.json"
KNOWLEDGE_DIR = "corpus/knowledge"
LINGUISTICS_DIR = f"{KNOWLEDGE_DIR}/linguistics"
CORPUS_README = "corpus/README.md"
R27_REGISTER_ENTRY = f"{LINGUISTICS_DIR}/register-strata-attestation.md"
R27_LAW_DIR = "reports/round-27/law"
R27_REGISTER_DIR = "reports/round-26/register"

SYNC_PATHS = (ROUND_DIR, "SKILL.md", "LOG.md", "SCORECARD.md", "PROVINCE.md",
              "SHONEN.md", "corpus", "examples", "tools")
# Round 27 is now a filed round: its artifacts are protected exactly as rounds 8-26
# were in round 27. Round-28 additions live under reports/round-28, corpus/knowledge
# and corpus/README.md.
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 28)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 28))

# --------------------------------------------------------------------------
# constants read off the delivered tree and the round-27 named gaps
# --------------------------------------------------------------------------

# The two components RL-4 names, and the blocks their `packet_keys` must cover
# for their records to reach the packet.
RL4_COMPONENTS = {
    f"{D4_COMPONENTS}/03-orthography.yml": ("records", "literacy_institutions"),
    f"{D4_COMPONENTS}/09-costumes.yml": ("enforcement",),
}
# Every record id the RL-4 fix must land in the packet as a *record*.
RL4_RECORD_IDS = ("OR-01", "OR-02", "OR-03", "LI-01", "LI-02", "LI-03", "EN-01", "EN-02")
# The blocks those ids live in, per the delivered components.
RL4_BLOCK_OF = {
    "OR-": ("records", f"{D4_COMPONENTS}/03-orthography.yml"),
    "LI-": ("literacy_institutions", f"{D4_COMPONENTS}/03-orthography.yml"),
    "EN-": ("enforcement", f"{D4_COMPONENTS}/09-costumes.yml"),
}

# The law's own vocabulary. `force` must name a Searle class (the design's
# reports/round-27/law/design.md section 3 vocabulary) or the literal `none`;
# the modifiers are the ones the landed rows use to qualify it.
LAW_FORCE_CLASSES = ("assertive", "directive", "commissive", "expressive", "declarative")
LAW_FORCE_MODIFIERS = ("binding", "refused", "not-rollable", "none", "attested",
                       "witnessed", "naming", "constraint")
# A consequence must name delivered roll/rank machinery, not an abstraction that
# no record carries. These are the stems the delivered packet supplies.
LAW_CONSEQUENCE_STEMS = ("roll", "rk-", "rank", "tally", "rite", "rit-", "entry",
                         "written", "record", "void", "binds", "binding", "no entry")
# The axis vocabulary the packet's own spine declares.
LAW_AXES = ("mark", "fire", "cloth", "wind", "word", "knot", "water")
LAW_KIND_DEFAULT = ("admissibility", "exclusion", "asymmetry", "no-segment", "era",
                    "enforcement", "procedure")
LAW_ID_RE = re.compile(r"\b(?:RGL|QREG|REG|RL)-\d{2}\b")
LAW_FINDING_RE = re.compile(r"D4L-LAW-[A-Z][A-Z-]*")
# An *emitted* finding line, in the lane's finding format (`FINDING <ID>: ...`).
# The prefix is required: a class id in prose or in a report table is not a
# finding, and the delta is taken over emitted lines.
LAW_FINDING_LINE_RE = re.compile(r"(?i)\bFINDING\s+D4L-LAW-[A-Z][A-Z-]*")
# The five law rows the delivered block declares. Their presence is resolved by
# `D4L-LAW-ROW`; a row silently dropped is the class the round-27 review called
# "a declaration with no teeth".
LAW_DECLARED_ROWS = ("RGL-01", "RGL-02", "RGL-03", "RGL-04", "RGL-05")
# An agent token in a law row: a bare name, or `name (ID)` where ID is a delivered
# record id. This is the shape RL-4's `mold-keeper (OR-02, component-only)` takes.
AGENT_ID_RE = re.compile(r"\(\s*([A-Z]{2,4}-\d{2,3})\b")
RECORD_ID_RE = re.compile(r"^[A-Z]{2,4}-\d{2,3}$")

COVERAGE_RE = re.compile(
    r"coverage:\s*\S+\s+records=(\d+)\s+register_scoped=(\d+)\s+derived_pairs=(\d+)"
    r"\s+claimed_chains=(\d+)\s+borrow_pairs=(\d+)\s+violations=(\d+)\s+rule_holds=(\d+)")
LEG_RE = re.compile(r"^(ok|FAIL)\s+([A-Za-z0-9_.-]+)")
SUMMARY_RE = re.compile(r"summary:\s*(\d+)/(\d+)\s+legs passed")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
PATHLIKE = re.compile(r"^[\w./-]+\.(?:ya?ml|json|py|md|txt)$")
PARTITION_HEADER_RE = re.compile(r"(?m)^##\s+([a-z-]+)/\s*\((\d+)\)")
REVISION_RE = re.compile(r"(?m)^revision:\s*([0-9]+\.[0-9]+)\s*—")
SECTION_RE = re.compile(r"(?m)^##\s+(.+?)\s*$")
FRONTMATTER = {
    "topic": re.compile(r"(?m)^-\s*topic:"),
    "sources": re.compile(r"(?m)^-\s*sources:"),
    "verified-at": re.compile(r"(?m)^-\s*verified-at:"),
    "recheck": re.compile(r"(?m)^-\s*recheck:"),
    "couples": re.compile(r"(?m)^-\s*couples:"),
}
DECISION_RECORD_RE = re.compile(r"(?i)decision record|decision table|\bdecision\b[^\n]{0,40}\|")
GAP_NAMED_RE = re.compile(r"(?i)\bgap\b|unfilled|not in the corpus|absent from|fills\b")
SOURCE_CITATION_RE = re.compile(r"\b(?:19|20)\d{2}\b")
ROUND_ARTIFACT_RE = re.compile(r"reports/round-2[678]/[\w./-]+")
CANON_CLAIM_RE = re.compile(r"(?i)\bis canon|canoniz(?:ed|es)\b|adopted as canon")
# The ceiling the round-27 review measured (RL-3) and claim C must record.
CEILING_RE = re.compile(
    r"(?i)\bceiling\b|\bLL-1\b|\bLL-2\b|reverse-?illegal|refuse[sd]?\s+reverse"
    r"|cannot\s+spell|material-presence base")

REGRESSIONS = (
    ("battery-selftest", (BATTERY, "--selftest")),
    ("battery", (BATTERY,)),
    ("craft-selftest", ("tools/check-craft-exercise.py", "--selftest")),
    ("craft", ("tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json")),
    ("d2-assembly-selftest", ("tools/assemble-d2.py", "--selftest")),
    ("d2-assembly", ("tools/assemble-d2.py", "--check")),
    ("d2-adapter-selftest", ("tools/assemble-d2-typed.py", "--selftest")),
    ("d2-adapter", ("tools/assemble-d2-typed.py", "--check")),
    ("d3-assembly-selftest", ("tools/assemble-culture-d3.py", "--selftest")),
    ("d3-assembly", ("tools/assemble-culture-d3.py", "--check")),
    ("d4-assembly-selftest", (D4_ASSEMBLER, "--selftest")),
    ("d4-assembly", (D4_ASSEMBLER, "--check")),
    ("d4-adapter-selftest", (D4_ADAPTER, "--selftest")),
    ("d4-adapter", (D4_ADAPTER, "--check", PACKET_D4_TYPED)),
    ("projector-selftest", (PROJECTOR, "--selftest")),
    ("d2-projection", (PROJECTOR, "--check")),
    ("d4-projection", (PROJECTOR, "--packet", PACKET_D4, "--check", D4_PROJECTION)),
    ("typed-pipeline-selftest", (TYPED_GATE, "--selftest")),
    ("typed-pipeline-generalized-selftest", (TYPED_GATE, "--selftest-generalized")),
    ("d2-gate", (TYPED_GATE,)),
    ("d4-gate", (TYPED_GATE, PACKET_D4)),
    ("d4-label-gate", (D4_LABEL_GATE,)),
    ("d4-label-gate-selftest", (D4_LABEL_GATE, "--selftest")),
    ("d4-assembly-gate", (D4_ASSEMBLY_GATE, PACKET_D4)),
    ("coupling-selftest", ("tools/check-evidence-coupling.py", "--selftest")),
    ("replay-selftest", (REPLAY, "--selftest")),
    ("handoff-gate-selftest", ("tools/gates/handoff-packet-check.py", "--selftest")),
    ("links-selftest", ("tools/harness/packet_links.py", "--selftest")),
    ("uncertainty-selftest", ("tools/harness/packet_uncertainty.py", "--selftest")),
    ("receipt-guard-selftest", ("tools/harness/receipt_guard.py", "--selftest")),
    ("argot-gate-selftest", (ARGOT_GATE, "--selftest")),
    ("argot-gate-d4", (ARGOT_GATE, PACKET_D4)),
    ("handoff-v2", (HANDOFF, "--profile", "v2", "--quiet")),
    ("handoff-v3-selftest", (HANDOFF, "--profile", "v3", "--selftest")),
    ("handoff-v3", (HANDOFF, "--profile", "v3", "--quiet")),
)


def today():
    return dt.date.today().isoformat()


def now_utc():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


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

    def bytes(self, relative):
        try:
            data = safe_path(relative).read_bytes()
            self.inputs[relative] = sha(data)
            return data
        except (OSError, ValueError) as error:
            self.missing.add(relative)
            self.errors.append(f"{relative}: {error}")
            return b""

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
    """The real lane root: nearest ancestor without a .scratch path component."""
    for ancestor in (ROOT, *ROOT.parents):
        if ".scratch" in ancestor.parts:
            continue
        if (ancestor / ".git").is_dir() and (ancestor / CLAIMS).is_file():
            return ancestor
    return None


def baseline_paths(revision):
    """Every protected path at the declared baseline revision, as
    `{path: git_blob_sha1}`, plus the untracked/modified working rows."""
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return None, ["Round-28 declared baseline is not a full Git revision"]
    raw = git("ls-tree", "-r", "-z", revision, "--", *PROTECTED)
    if raw is None:
        return None, [f"Cannot inspect protected baseline {revision}"]
    expected = {}
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        _mode, kind, oid = metadata.decode("ascii").split()
        if kind != "blob":
            continue
        expected[os.fsdecode(name)] = oid
    return expected, []


def protected_baseline(revision):
    expected, problems = baseline_paths(revision)
    failures, rows = list(problems), []
    if expected is None:
        return result(failures, {})
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
        blob = git_blob_sha(data)
        if blob != expected[relative]:
            rows.append({"path": relative, "baseline_blob": expected[relative],
                         "observed_blob": sha(data)})
    status = git("status", "--porcelain=v1", "--untracked-files=all", "--", *PROTECTED)
    worktree = [line for line in (status or b"").decode("utf-8", "replace").splitlines()
                if line.strip()]
    for line in worktree:
        flag, _, path = line.partition(" ")
        if flag == "??" and path.strip():
            rows.append({"path": path.strip(), "baseline_blob": None, "observed_blob": "untracked"})
    if rows:
        failures.append("Filed rounds 8-27 or their frozen generations differ from the declared baseline")
    return result(failures, {"baseline_revision": revision,
                             "protected_paths": metric(len(expected), "git ls-tree of protected baseline"),
                             "differences": rows[:20],
                             "differences_total": metric(len(rows), "compare protected Git blobs to working bytes"),
                             "protected_status_rows": metric(len(worktree), "git status over protected paths")})


def run_command(label, parts, timeout=900, env_extra=None):
    scratch = ROOT / ".scratch" / "round-28" / "validation" / label
    scratch.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(scratch), "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    env.update(env_extra or {})
    item = {"label": label, "command": shlex.join(["python3", *parts]),
            "argv": ["python3", *parts], "date": today()}
    try:
        item["tool_sha256"] = sha(safe_path(parts[0]).read_bytes())
        proc = subprocess.run([sys.executable, *parts], cwd=ROOT, capture_output=True,
                              timeout=timeout, env=env)
        item.update(exit=proc.returncode, stdout=proc.stdout.decode("utf-8", "replace"),
                    stderr=proc.stderr.decode("utf-8", "replace"),
                    stdout_sha256=sha(proc.stdout), stderr_sha256=sha(proc.stderr))
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error), timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def run_receipt(item):
    """The receipt row: the full stdout up to a generous cap (the battery prints
    a ~29 KB JSON document the O leg parses, so a tight cap would truncate the
    very bytes being read), the stderr tail, and the parsed document when the
    stdout is JSON."""
    receipt = {key: (value[:40000] if key == "stdout" else value[-2000:]
                     if key == "stderr" else value) for key, value in item.items()}
    try:
        receipt["stdout_json"] = strict_json(item.get("stdout") or "")
    except (ValueError, TypeError):
        receipt["stdout_json"] = None
    return receipt


def gate_legs(stdout):
    """(ok legs, failed legs, passed, total) parsed off a gate run."""
    ok, failed = [], []
    for line in stdout.splitlines():
        match = LEG_RE.match(line.strip())
        if not match:
            continue
        (ok if match.group(1) == "ok" else failed).append(match.group(2))
    summary = SUMMARY_RE.search(stdout)
    passed, total = (int(summary.group(1)), int(summary.group(2))) if summary else (len(ok), len(ok) + len(failed))
    return ok, failed, passed, total


def measure_regressions():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        items = list(pool.map(lambda pair: run_command(*pair), REGRESSIONS))
    failures = [f"Regression failed: {item['command']} (exit {item.get('exit')}, {item['date']})"
                for item in items if item.get("exit") != 0]
    measurement = {"runs_total": metric(len(items), "fixed regression command inventory"),
                   "labels": {item["label"]: {"exit": item.get("exit"), "command": item["command"],
                                              "date": item["date"]} for item in items},
                   "runs": [run_receipt(item) for item in items]}
    return result(failures, measurement)


def label_run(regressions, label):
    return next((run for run in regressions["measurement"]["runs"] if run["label"] == label), {})


# --------------------------------------------------------------------------
# YAML subset loading (the naming gate's loader, read-only by path — the same
# reader the argot gate and the assembler use; no third-party dependency)
# --------------------------------------------------------------------------

_LOADER = None


def yaml_loader():
    global _LOADER
    if _LOADER is None:
        _LOADER = runpy.run_path(str(safe_path(NAMING_GATE)))
    return _LOADER


def load_yaml_text(text):
    return yaml_loader()["load_yaml"](text)


def load_packet(relative):
    return load_yaml_text(safe_path(relative).read_text(encoding="utf-8"))


def parse_coverage_line(text):
    match = COVERAGE_RE.search(text or "")
    if not match:
        return None
    keys = ("records", "register_scoped", "derived_pairs", "claimed_chains",
            "borrow_pairs", "violations", "rule_holds")
    return {key: int(value) for key, value in zip(keys, match.groups())}


# --------------------------------------------------------------------------
# Claim D, part 1 — the law, its replay leg, and this runner's own law reader
# --------------------------------------------------------------------------

def law_rows(packet):
    """Every law row the packet carries: the `register_law` speech-act rows and
    the `registers` identity rows. Both are graded; the replay leg is measured
    over the speech-act rows, which are the ones that carry `force`."""
    block = packet.get("register_law") if isinstance(packet, dict) else None
    speech = [row for row in (block or []) if isinstance(row, dict)]
    regs = packet.get("registers") if isinstance(packet, dict) else None
    identity = [row for row in (regs or []) if isinstance(row, dict)]
    return identity, speech


def packet_record_ids(packet):
    """Every id carried by a *record* in the packet: a list block whose rows are
    mappings with an `id`. This is the resolver's ground truth — an agent token
    naming an id not in this set is unresolvable (RL-4's `mold-keeper (OR-02)`)."""
    ids = set()
    if not isinstance(packet, dict):
        return ids
    for key, value in packet.items():
        if not isinstance(value, list):
            continue
        for row in value:
            if isinstance(row, dict):
                rid = str(row.get("id") or "").strip()
                if rid:
                    ids.add(rid)
    return ids


def register_names(packet):
    """The register *names* the packet declares: `registers[].register` (the value
    a law row's `register` field actually carries, e.g. `plain`/`stamp`) plus the
    row ids, so either spelling resolves."""
    regs = packet.get("registers") if isinstance(packet, dict) else None
    names = set()
    for row in (regs or []):
        if not isinstance(row, dict):
            continue
        for key in ("id", "register", "title"):
            token = str(row.get(key) or "").strip()
            if token:
                names.add(token)
    return names


def law_check(packet, force_vocabulary=None):
    """This runner's own reader of the law — the independent reading the delivered
    replay leg is graded against. Three resolutions, one per clause the claim names:

      * **speaker** — every agent token `Name (ID)` in `speaker`/`holder` must
        resolve to an id the packet carries as a *record*; an unresolvable id is
        `D4L-LAW-SPEAKER`.
      * **force** — every `force` value must name a declared illocutionary class
        (or the literal `none`); a value naming none is `D4L-LAW-FORCE`.
      * **consequence** — every consequence of a *binding* act must name delivered
        roll/rank machinery; one naming nothing the packet supplies is
        `D4L-LAW-CONSEQUENCE`. A row that declares `force: none` is by its own
        terms not a speech act (RGL-04's sound-channel and RGL-05's dating
        constraints), so its `consequence` is a constraint statement and is not
        resolved as a record consequence.

    Plus four structural resolutions: `register` must name a declared register,
    `axis` must be in the spine's axis vocabulary, every `design_row` token must
    name a delivered record (`D4L-LAW-DANGLING`), and the declared law rows must
    all be present (`D4L-LAW-ROW`).
    """
    findings = []
    record_ids = packet_record_ids(packet)
    registers = register_names(packet)
    identity, speech = law_rows(packet)
    declared_forces = set(force_vocabulary or ())
    present = [str(row.get("id") or "").strip() for row in speech]
    for want in LAW_DECLARED_ROWS:
        if want not in present:
            findings.append({"class": "D4L-LAW-ROW", "row": want,
                             "reason": "a declared law row is absent from the block"})

    for row in speech:
        rid = str(row.get("id") or "?").strip()
        force = str(row.get("force") or "").strip().lower()
        binding_act = True
        if force:
            classes = [name for name in LAW_FORCE_CLASSES if name in force]
            tokens = {token for token in re.split(r"[^a-z-]+", force) if token}
            modifier_ok = any(m in force for m in LAW_FORCE_MODIFIERS)
            # `none` alone is a declared non-force (a sound-channel or dating
            # constraint, as RGL-04/RGL-05 carry it); it needs no class.
            none_only = "none" in tokens and not classes
            binding_act = not none_only
            declared_ok = bool(declared_forces & tokens)
            if not ((classes and modifier_ok) or none_only or declared_ok):
                findings.append({"class": "D4L-LAW-FORCE", "row": rid, "value": force,
                                 "reason": "force names no declared illocutionary class"})
        for field in ("speaker", "holder"):
            value = str(row.get(field) or "")
            for token in AGENT_ID_RE.findall(value):
                if token not in record_ids:
                    findings.append({"class": "D4L-LAW-SPEAKER", "row": rid, "field": field,
                                     "agent": token,
                                     "reason": "agent id resolves to no delivered record"})
        consequence = str(row.get("consequence") or "").lower()
        if consequence and binding_act and not any(stem in consequence
                                                   for stem in LAW_CONSEQUENCE_STEMS):
            findings.append({"class": "D4L-LAW-CONSEQUENCE", "row": rid,
                             "value": consequence[:120],
                             "reason": "consequence names no delivered roll/rank machinery"})
        register = str(row.get("register") or "").strip()
        if register and registers and register not in registers:
            findings.append({"class": "D4L-LAW-REGISTER", "row": rid, "value": register,
                             "reason": "register names no declared register"})
        axis = str(row.get("axis") or "").strip().lower()
        if axis and axis not in LAW_AXES:
            findings.append({"class": "D4L-LAW-AXIS", "row": rid, "value": axis,
                             "reason": "axis is outside the spine's axis vocabulary"})
        for field in ("design_row", "design_rows"):
            value = row.get(field)
            tokens = value if isinstance(value, list) else ([value] if value else [])
            for token in tokens:
                token = str(token).strip()
                if token and RECORD_ID_RE.match(token) and token not in record_ids:
                    findings.append({"class": "D4L-LAW-DANGLING", "row": rid, "token": token,
                                     "reason": f"{field} names no delivered record"})
    return findings, {"record_ids": len(record_ids), "registers": sorted(registers),
                      "law_rows": len(speech), "identity_rows": len(identity)}


def law_finding_ids(text):
    return sorted(set(LAW_FINDING_RE.findall(text or "")))


def tamper_law_text(packet_text, mutation):
    """A tampered copy of the packet bytes, produced by a textual rewrite of the
    FIRST law row's named field. A textual rewrite (not a re-serialisation) is
    what keeps the control honest: it changes exactly one value and leaves every
    other byte as the assembler wrote it."""
    if mutation == "force":
        pattern = re.compile(r"(?m)^(\s*)force:\s*(.+)$")
        return pattern.sub(lambda m: f'{m.group(1)}force: "no-such-force"', packet_text, count=1)
    if mutation == "speaker":
        pattern = re.compile(r"(?m)^(\s*)speaker:\s*(.+)$")
        return pattern.sub(lambda m: f'{m.group(1)}speaker: "nobody-nowhere (ZZ-99)"',
                           packet_text, count=1)
    if mutation == "consequence":
        pattern = re.compile(r"(?m)^(\s*)consequence:\s*(.+)$")
        return pattern.sub(lambda m: f'{m.group(1)}consequence: "the act evaporates silently"',
                           packet_text, count=1)
    raise ValueError(f"unknown law mutation: {mutation}")


def law_finding_lines(text):
    """The distinct *emitted finding* lines carrying the `D4L-LAW-*` class, in the
    lane's finding format (`FINDING <ID>: ...` — the form the argot gate prints).

    The `FINDING ` prefix is required on purpose: a class id can appear in prose,
    in a report table, or in a checker's own help text, and none of those is a
    finding. A class-id set is also too coarse a delta — the D seat's design shows
    two classes already firing on the clean packet (saturated), so a tamper in a
    saturated class adds a line without adding a class. The emitted line is the
    unit that actually moves.
    """
    lines = []
    for line in (text or "").splitlines():
        if LAW_FINDING_LINE_RE.search(line):
            lines.append(" ".join(line.split()))
    return sorted(set(lines))


def law_replay_probe(evidence, packet_text, scratch_root):
    """Run the **delivered** checking leg on the clean packet and on three
    tampered copies, and measure the *line-level* delta per tamper.

    The claim's teeth test is the one round 27's RL-1 failed: a tampered row must
    produce a named `D4L-LAW-*` finding the clean packet does NOT produce. The
    clean packet's own findings are reported, never required to be zero — the D
    seat's design measures six honest findings on the clean bytes (four dangling
    `design_row` ids, two non-act consequences), and a leg that fired on nothing
    would be the defect, not the fix. Two of the six classes are saturated on the
    clean packet, so the delta is taken over finding *lines*, not class ids.

    The leg is discovered, not named. Every delivered instrument that names the
    class the claim itself names is invoked under both plausible argv shapes; the
    one that actually **emits** finding lines on the clean packet is the leg that
    is measured. An instrument that names the class but never emits it (a battery
    that needs a subcommand, a witness that only counts) is recorded as an attempt
    and not chosen. When no instrument emits, the run is reported as the RL-1
    state — a declared class with no firing leg — rather than as a failed tamper.
    """
    producers = law_finding_producers()
    runs = {}

    def attempts_for(label, path):
        out = []
        for relative in producers:
            for argv in ((relative, str(path)), (relative, "--packet", str(path))):
                item = run_command(label + "-" + Path(relative).stem + "-" + str(len(out)),
                                   argv, timeout=600)
                text = (item.get("stdout") or "") + (item.get("stderr") or "")
                out.append({"leg": relative, "argv": list(argv),
                            "ids": law_finding_ids(text), "lines": law_finding_lines(text),
                            "exit": item.get("exit"), "command": item["command"],
                            "text_head": text[:6000]})
        return out

    def invoke(label, path):
        attempts = attempts_for(label, path)
        firing = [item for item in attempts if item["lines"]]
        chosen = max(firing, key=lambda item: len(item["lines"])) if firing else None
        if chosen is None:
            return {"leg": None, "argv": None, "ids": [], "lines": [], "exit": None,
                    "command": None, "text_head": "",
                    "attempts": [{"leg": item["leg"], "argv": item["argv"],
                                  "lines": len(item["lines"]), "exit": item["exit"]}
                                 for item in attempts]}
        return {**chosen,
                "attempts": [{"leg": item["leg"], "argv": item["argv"],
                              "lines": len(item["lines"]), "exit": item["exit"]}
                             for item in attempts]}

    clean = invoke("law-replay-clean", safe_path(PACKET_D4))
    runs["clean"] = clean
    for mutation in ("force", "speaker", "consequence"):
        tampered = tamper_law_text(packet_text, mutation)
        target = scratch_root / f"packet.tamper-{mutation}.yml"
        target.write_text(tampered, encoding="utf-8")
        if clean.get("leg") is None:
            # No leg emitted on the clean packet: there is nothing to grade a
            # tamper against, and re-running every instrument three more times
            # would only restate the RL-1 reading.
            runs[mutation] = {"path": str(target), "changed": tampered != packet_text,
                              "leg": None, "argv": None, "ids": [], "lines": [],
                              "exit": None, "command": None, "text_head": "", "attempts": []}
            continue
        # Grade the tamper with the SAME instrument that emitted on the clean
        # packet, so the delta is one leg's reading and not two tools' outputs.
        # The packet path is the last argv element under both discovered shapes
        # (`LEG PATH` and `LEG --packet PATH`), so it is the element replaced.
        argv = [*clean["argv"][:-1], str(target)]
        item = run_command(f"law-replay-{mutation}", tuple(argv), timeout=600)
        text = (item.get("stdout") or "") + (item.get("stderr") or "")
        runs[mutation] = {"path": str(target), "changed": tampered != packet_text,
                          "leg": clean["leg"], "argv": argv,
                          "ids": law_finding_ids(text), "lines": law_finding_lines(text),
                          "exit": item.get("exit"), "command": item["command"],
                          "text_head": text[:6000], "attempts": []}
    return runs


def law_finding_producers():
    """Every delivered tool that names the `D4L-LAW-*` class the claim names.

    Both delivery roots are walked, because this lane delivers instruments in
    both: `tools/` (the gates, the assemblers, the projector) and the round's own
    `reports/round-NN/` directory (round 27's law instrument and its gate-tests
    battery live there, and round 28's D seat designs a standalone leg the same
    way). A class id in prose is not a producer — the file must carry the class
    the claim names.
    """
    found = []
    roots = (safe_path("tools"), safe_path(ROUND_DIR))
    runner = safe_path(RUNNER).resolve()
    for base in roots:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.py")):
            if "__pycache__" in path.parts:
                continue
            if path.resolve() == runner:
                continue  # this runner names the class in its own code, not as a leg
            try:
                if LAW_FINDING_RE.search(path.read_text(encoding="utf-8", errors="replace")):
                    found.append(str(path.relative_to(ROOT)))
            except OSError:
                continue
    return found


def measure_law_replay(evidence, regressions):
    failures, measurement, missing = [], {}, []

    packet_text = evidence.text(PACKET_D4)
    if not packet_text:
        missing.append(PACKET_D4)
        failures.append(f"the D4 packet is missing: {PACKET_D4}")
        return result(failures, measurement, missing)
    try:
        packet = load_packet(PACKET_D4)
    except Exception as error:
        failures.append(f"the D4 packet does not parse under the lane's subset reader: "
                        f"{type(error).__name__}: {error}")
        return result(failures, measurement, missing)

    identity, speech = law_rows(packet)
    # ---- 1. the law block exists, is component-owned, and is machine-readable
    owners = []
    for path in component_files():
        keys, document = component_packet_keys(path)
        if not keys:
            continue
        for name in ("registers", "register_law"):
            if name in keys and isinstance(document, dict) and document.get(name):
                owners.append({"path": str(path.relative_to(ROOT)), "block": name,
                               "packet_keys": keys, "rows": len(document.get(name) or [])})
    contract_fields = ((packet.get("contract") or {}).get("record_fields") or {})
    measurement["law_blocks"] = {
        "registers": {"rows_total": len(identity),
                      "ids": [row.get("id") for row in identity][:12]},
        "register_law": {"rows_total": len(speech),
                         "ids": [row.get("id") for row in speech][:12],
                         "kinds": sorted({str(row.get("kind")) for row in speech if row.get("kind")})},
        "declaring_components": owners,
        "contract_record_fields": {name: contract_fields.get(name)
                                   for name in ("registers", "register_law")},
        "command": f"{COMMAND} (packet law blocks vs component packet_keys)",
        "date": today()}
    if not speech:
        failures.append("the D4 packet carries no `register_law` speech-act rows: the law the "
                        "replay leg is supposed to check is absent")
        missing.append(f"{PACKET_D4} (register_law block)")
    if not identity:
        failures.append("the D4 packet carries no `registers` identity rows")
    for name in ("registers", "register_law"):
        if not (identity if name == "registers" else speech):
            continue
        if not any(item["block"] == name for item in owners):
            failures.append(f"no component declares `{name}` in its own `packet_keys`: the law is "
                            f"not wired into the packet deterministically")
        if not contract_fields.get(name):
            failures.append(f"the packet contract declares no `record_fields.{name}`")

    # ---- 2. this runner's own reading of the law, on the delivered bytes.
    # A finding here is a *measurement*, not a verdict: the delivered law is a
    # NON-CANON design statement, and the D seat's own design measures honest
    # findings on the clean bytes (dangling `design_row` ids, non-act
    # consequences). The runner records its reading and the delivered leg's,
    # and grades on the tamper *delta* (below) — the teeth test RL-1 failed.
    own_findings, own_context = law_check(packet)
    measurement["runner_law_reader"] = {
        "findings_total": metric(len(own_findings), "this runner's own law reader over the delivered packet"),
        "findings": own_findings[:20],
        "context": own_context,
        "command": f"{COMMAND} (this runner's own speaker/force/consequence/design_row resolutions, never read back from the delivered leg)",
        "date": today()}

    # ---- 3. the replay leg: the tamper DELTA is the teeth test
    producer_files = law_finding_producers()
    measurement["law_finding_producers"] = producer_files
    if not producer_files:
        failures.append("no delivered instrument names a `D4L-LAW-*` finding id: the law has no "
                        "replay leg (round-27 RL-1)")

    scratch_root = ROOT / ".scratch" / "round-28" / "law-replay"
    scratch_root.mkdir(parents=True, exist_ok=True)
    replay = law_replay_probe(evidence, packet_text, scratch_root)
    clean_lines = set(replay["clean"].get("lines") or ())
    clean_ids = sorted(set(replay["clean"].get("ids") or ()))
    measurement["law_replay"] = {
        "leg": replay["clean"].get("leg"),
        "clean": {"ids": clean_ids, "lines": len(clean_lines),
                  "exit": replay["clean"].get("exit"),
                  "command": replay["clean"].get("command"),
                  "attempts": replay["clean"].get("attempts")},
        "tampers": {},
        "command": f"{COMMAND} (clean packet vs three tampered copies, run through the delivered checking leg; graded on the line-level delta)",
        "date": today()}
    leg_fires = bool(clean_lines)
    if producer_files and not leg_fires:
        failures.append(f"{len(producer_files)} delivered instrument(s) name the `D4L-LAW-*` class "
                        f"but none of them emits a `FINDING D4L-LAW-*` line on the clean packet: "
                        f"the class is declared and no leg fires it (round-27 RL-1)")
    for name in ("force", "speaker", "consequence"):
        row = replay[name]
        added = sorted(set(row.get("lines") or ()) - clean_lines)
        added_ids = sorted(set(row.get("ids") or ()) - set(clean_ids))
        measurement["law_replay"]["tampers"][name] = {
            "leg": row.get("leg"), "ids": row.get("ids"), "added_over_clean": added_ids,
            "added_lines": added, "lines_total": len(row.get("lines") or ()),
            "exit": row.get("exit"), "changed": row.get("changed"),
            "command": row.get("command")}
        if not leg_fires:
            continue  # the RL-1 reading is already recorded once, above
        if not row.get("changed"):
            failures.append(f"the {name} tamper did not change the packet bytes: the control is inert")
            continue
        if not added:
            failures.append(f"the {name} tamper adds no `D4L-LAW-*` finding line over the clean "
                            f"packet (clean lines={len(clean_lines)}, tampered lines="
                            f"{len(row.get('lines') or ())}): the law still has no teeth for that "
                            f"resolution (round-27 RL-1)")

    # ---- 4. the three byte-identical regenerations
    runs = regressions["measurement"]["labels"]
    deterministic = {label: runs.get(label, {}).get("exit") for label in
                     ("d4-assembly", "d4-adapter", "d4-projection")}
    measurement["deterministic_regeneration"] = deterministic
    for label, code in deterministic.items():
        if code != 0:
            failures.append(f"the D4 {label} regeneration is not byte-identical (exit {code})")

    # ---- 5. the gates are green
    coverage = parse_coverage_line(label_run(regressions, "argot-gate-d4").get("stdout"))
    ok, failed, passed, total = gate_legs(label_run(regressions, "d4-gate").get("stdout"))
    measurement["gates"] = {
        "argot_selftest_exit": runs.get("argot-gate-selftest", {}).get("exit"),
        "argot_d4_exit": runs.get("argot-gate-d4", {}).get("exit"),
        "argot_coverage": coverage,
        "typed_gate_legs": f"{passed}/{total}",
        "typed_gate_failed_legs": failed,
        "typed_gate_exit": runs.get("d4-gate", {}).get("exit"),
        "d4_label_gate_exit": runs.get("d4-label-gate", {}).get("exit"),
        "d4_assembly_gate_exit": runs.get("d4-assembly-gate", {}).get("exit"),
    }
    for label in ("argot-gate-selftest", "argot-gate-d4", "d4-gate", "d4-label-gate",
                  "d4-assembly-gate"):
        if runs.get(label, {}).get("exit") != 0:
            failures.append(f"{label} is not green (exit {runs.get(label, {}).get('exit')})")
    if coverage is None:
        failures.append("the argot gate's D4 run prints no parsable coverage line")
    else:
        if coverage["derived_pairs"] < 1:
            failures.append(f"the argot gate replays an empty domain: derived_pairs={coverage['derived_pairs']}")
        if coverage["violations"] != 0:
            failures.append(f"the argot gate reports {coverage['violations']} violation(s)")
        if coverage["rule_holds"] != 0:
            failures.append(f"the argot gate reports {coverage['rule_holds']} rule hold(s)")

    # ---- 6. RL-4: the packet_keys gap closed, measured on the records themselves
    rl4 = measure_rl4(evidence, packet)
    measurement["rl4"] = rl4["measurement"]
    failures.extend(rl4["failures"])
    missing.extend(rl4["missing_dependencies"])

    # ---- 7. the named-holds set revised honestly
    holds = evidence.document(D4_HOLDS) or {}
    counts = holds.get("counts") or {}
    revision_note = str(holds.get("revision_note") or "")
    supersedes = holds.get("supersedes_pins") or {}
    measurement["holds"] = {
        "path": D4_HOLDS, "counts": counts,
        "revision_note_head": revision_note[:260],
        "names_round_28": bool(re.search(r"(?i)round[- ]?28|r28", revision_note)),
        "names_the_fix": bool(re.search(r"(?i)packet_keys|orthography|costumes|enforcement|"
                                        r"literacy|records\b|RL-4", revision_note)),
        "supersedes_pins": supersedes,
        "holds_rows": len(holds.get("holds") or []),
    }
    if not revision_note:
        failures.append(f"the D4 hold set carries no revision note ({D4_HOLDS})")
    else:
        if not measurement["holds"]["names_round_28"]:
            failures.append("the D4 hold set's revision note does not name the round-28 landing")
        if not measurement["holds"]["names_the_fix"]:
            failures.append("the D4 hold set's revision note does not name the RL-4 packet_keys fix")
    if counts.get("fail"):
        failures.append(f"the D4 hold set carries {counts['fail']} fail row(s)")
    if counts.get("hold") != len(holds.get("holds") or []):
        failures.append(f"the D4 hold set declares hold={counts.get('hold')} but carries "
                        f"{len(holds.get('holds') or [])} rows")
    if not supersedes:
        failures.append("the D4 hold set carries no `supersedes_pins`: the round-27 pin is not "
                        "recorded as superseded (a re-pin is a NEW row)")

    # ---- 8. the round-28 D artifact names the landing and carries a receipt
    artifacts = find_round_artifacts(("law", "replay", "register", "rl4", "packet"))
    measurement["artifacts"] = [str(path.relative_to(ROOT)) for path in artifacts]
    if not artifacts:
        failures.append(f"no round-28 law/replay artifact landed under {ROUND_DIR}")
        missing.append(f"{ROUND_DIR} (D artifact)")
        return result(failures, measurement, missing)
    blob = "\n".join(evidence.text(str(path.relative_to(ROOT))) for path in artifacts)
    tokens = {
        "names_the_replay_leg": bool(re.search(r"(?i)replay|checking leg|D4L-LAW", blob)),
        "names_rl1": bool(re.search(r"RL-1|no teeth|no replay leg", blob)),
        "names_rl4": bool(re.search(r"RL-4|packet_keys", blob)),
        "names_the_tamper_control": bool(re.search(r"(?i)tamper|no-such-force|invisible", blob)),
        "carries_receipt": bool(re.search(r"(?i)\b(exit|selftest|receipt|executed|command)\b", blob)),
    }
    measurement["artifact_tokens"] = tokens
    for name, present in tokens.items():
        if not present:
            failures.append(f"the round-28 D artifact never records {name}")
    return result(failures, measurement, missing)


def measure_rl4(evidence, packet):
    """RL-4: the components declare the keys AND the records reach the packet."""
    failures, missing = [], []
    declared = {}
    for relative, blocks in RL4_COMPONENTS.items():
        keys, document = component_packet_keys(safe_path(relative))
        declared[relative] = {"packet_keys": keys,
                              "missing_blocks": [block for block in blocks
                                                 if not keys or block not in keys]}
    # Where the packet actually carries each record id: a list block row with an id.
    found = {}
    for rid in RL4_RECORD_IDS:
        located = None
        for key, value in (packet or {}).items():
            if not isinstance(value, list):
                continue
            for row in value:
                if isinstance(row, dict) and str(row.get("id") or "").strip() == rid:
                    located = key
                    break
            if located:
                break
        found[rid] = located
    absent = [rid for rid, where in found.items() if where is None]
    # The skipped-keys ledger must no longer route these blocks away.
    skipped = ((packet or {}).get("assembly") or {}).get("skipped_keys") or {}
    still_skipped = {}
    for rid in RL4_RECORD_IDS:
        for key, value in skipped.items():
            if not isinstance(value, list):
                continue
            if any(rid in str(token) for token in value):
                still_skipped.setdefault(rid, []).append(key)
    measurement = {
        "component_packet_keys": declared,
        "record_locations": found,
        "records_absent": absent,
        "still_skipped": still_skipped,
        "command": f"{COMMAND} (component packet_keys vs the packet's own record rows; the "
                   f"assembly skipped_keys ledger)",
        "date": today()}
    for relative, row in declared.items():
        if row["missing_blocks"]:
            failures.append(f"{relative} still declares no packet_keys for {row['missing_blocks']}: "
                            f"the record block never reaches the packet (RL-4)")
    if absent:
        failures.append(f"{len(absent)} record id(s) still reach the packet as prose only, not as "
                        f"records: {absent}")
        missing.append(f"{PACKET_D4} (RL-4 records)")
    if still_skipped:
        failures.append(f"the assembly still routes these ids away under skipped_keys: "
                        f"{sorted(still_skipped)}")
    return result(failures, measurement, missing)


def component_files():
    base = safe_path(D4_COMPONENTS)
    if not base.is_dir():
        return []
    return sorted(path for path in base.iterdir()
                  if path.is_file() and path.suffix.lower() in (".yml", ".yaml"))


def component_packet_keys(path):
    try:
        document = load_yaml_text(path.read_text(encoding="utf-8"))
    except Exception:
        return None, None
    if not isinstance(document, dict):
        return None, None
    keys = document.get("packet_keys")
    return (list(keys) if isinstance(keys, list) else None), document


def find_round_artifacts(tokens, exclude_runner=True):
    base = safe_path(ROUND_DIR)
    found = []
    if not base.is_dir():
        return found
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in (".md", ".json", ".yml", ".yaml", ".py", ".txt"):
            continue
        if path.name in ("claims.json", "targets.json", "validation.json"):
            continue
        name = path.name.lower()
        parent = path.parent.name.lower()
        if not any(token in name or token in parent for token in tokens):
            continue
        if exclude_runner and path.resolve() == safe_path(RUNNER).resolve():
            continue
        found.append(path)
    return found


# --------------------------------------------------------------------------
# Claim O — the final pin sweep
# --------------------------------------------------------------------------

PIN_SCAN_GLOBS = (
    "tools/gates/expected/**/*.json",
    "tools/gates/frozen/**/*.json",
    "tools/gates/frozen/**/*.tsv",
    "reports/round-20/**/*.json",
    "reports/round-22/**/*.json",
    "reports/round-26/**/*.json",
    "reports/round-27/**/*.json",
    TYPED_PROFILES,
    D4_HOLDS,
)


def is_d4_surface(path):
    return isinstance(path, str) and path.startswith(D4_DIR + "/") and PATHLIKE.match(path)


def digest_pairs(node, context=""):
    """(path, digest) pairs from any nested mapping: a key that names a repo
    path whose sibling value (or a `sha256`/`digest`/`hash` sub-key) is a sha256."""
    found = []
    if isinstance(node, dict):
        for key, value in node.items():
            if isinstance(key, str) and PATHLIKE.match(key):
                if isinstance(value, str) and HEX64.match(value):
                    found.append((key, value))
                elif isinstance(value, dict):
                    for sub in ("sha256", "digest", "hash"):
                        token = value.get(sub)
                        if isinstance(token, str) and HEX64.match(token):
                            found.append((key, token))
                            break
            found.extend(digest_pairs(value, context))
    elif isinstance(node, list):
        for item in node:
            found.extend(digest_pairs(item, context))
    return found


def manifest_pairs(path):
    """(input, input_sha256) pairs off a frozen MANIFEST.tsv."""
    pairs = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return pairs
    if not lines:
        return pairs
    header = lines[0].split("\t")
    try:
        input_at = header.index("input")
        digest_at = header.index("input_sha256")
    except ValueError:
        return pairs
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) <= max(input_at, digest_at):
            continue
        pairs.append((cells[input_at], cells[digest_at]))
    return pairs


def profile_pins():
    """(surface, digest) pairs off the typed-pipeline profile rows."""
    pairs = []
    try:
        document = strict_json(safe_path(TYPED_PROFILES).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return pairs
    for profile in (document.get("profiles") or []):
        if not isinstance(profile, dict):
            continue
        for key in ("packet", "projection", "expected", "adapter", "assembler"):
            block = profile.get(key)
            if isinstance(block, dict) and isinstance(block.get("path"), str) \
                    and isinstance(block.get("sha256"), str):
                pairs.append((block["path"], block["sha256"]))
    return pairs


def collect_pin_rows():
    """Every row that pins a D4 surface: `{row, surface, declared, live, reading}`."""
    rows = []
    seen = set()
    for pattern in PIN_SCAN_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file():
                continue
            relative = str(path.relative_to(ROOT))
            if path.suffix.lower() == ".tsv":
                pairs = manifest_pairs(path)
                kind = "frozen-manifest"
            else:
                try:
                    document = strict_json(path.read_text(encoding="utf-8", errors="replace"))
                except (OSError, ValueError):
                    continue
                pairs = digest_pairs(document)
                kind = "json-row"
            for surface, declared in pairs:
                if not is_d4_surface(surface):
                    continue
                key = (relative, surface)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({"row": relative, "kind": kind, "surface": surface,
                             "declared": declared})
    for surface, declared in profile_pins():
        if not is_d4_surface(surface):
            continue
        key = (TYPED_PROFILES, surface)
        if key in seen:
            continue
        seen.add(key)
        rows.append({"row": TYPED_PROFILES, "kind": "typed-profile", "surface": surface,
                     "declared": declared})
    for row in rows:
        try:
            live = sha(safe_path(row["surface"]).read_bytes())
        except (OSError, ValueError):
            live = None
        row["live"] = live
        row["reading"] = ("green" if live is not None and live == row["declared"]
                          else "drift" if live is not None else "absent")
    return rows


def round_repin_rows():
    """Round-28 records that can close a drift: a structured row (JSON/YAML/TSV)
    that names a D4 surface and carries that surface's live digest. A prose
    mention in a Markdown report is recorded but does not close a pin — a pin is
    a digest in a machine-readable row, not a sentence about one."""
    found = []
    base = safe_path(ROUND_DIR)
    if not base.is_dir():
        return found
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix not in (".json", ".md", ".yml", ".yaml", ".tsv", ".txt"):
            continue
        if path.name in ("claims.json", "targets.json", "validation.json"):
            continue
        relative = str(path.relative_to(ROOT))
        if path.resolve() == safe_path(RUNNER).resolve():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if not any(surface in text for surface in D4_SURFACES):
            continue
        structured = suffix in (".json", ".yml", ".yaml", ".tsv")
        found.append({"path": relative, "text": text, "structured": structured,
                      "kind": "named-repin" if re.search(
                          r"(?i)\bre-?pin|repoint|pin sweep|sweep\b", text) else "digest-row"})
    return found


D4_SURFACES = (PACKET_D4, PACKET_D4_TYPED, D4_PROJECTION, D4_HOLDS,
               *(f"{D4_COMPONENTS}/{name}" for name in (
                   "01-brief.yml", "02-phonology.yml", "03-orthography.yml", "04-lexicon.yml",
                   "05-naming.yml", "06-myth.yml", "07-symbolism.yml", "08-eras.yml",
                   "09-costumes.yml", "10-ritual-calendar.yml", "11-contact-history.yml",
                   "12-provenance.yml", "13-register-law.yml")))


def measure_pin_sweep(evidence, regressions):
    failures, measurement, missing = [], {}, []

    rows = collect_pin_rows()
    by_reading = {"green": [], "drift": [], "absent": []}
    for row in rows:
        by_reading[row["reading"]].append(row)
    drifted_surfaces = sorted({row["surface"] for row in by_reading["drift"]})
    measurement["sweep"] = {
        "rows_total": metric(len(rows), "every pin row naming a D4 surface"),
        "green": len(by_reading["green"]),
        "drift": len(by_reading["drift"]),
        "absent": len(by_reading["absent"]),
        "drifted_surfaces": drifted_surfaces,
        "drifted_rows": [{"row": row["row"], "surface": row["surface"],
                          "declared": (row["declared"] or "")[:16],
                          "live": (row["live"] or "")[:16]}
                         for row in by_reading["drift"][:20]],
        "row_inventory": sorted({row["row"] for row in rows}),
        "command": f"{COMMAND} (walk every pin row that names a D4 surface; compare declared digest to live bytes)",
        "date": today(),
    }
    if not rows:
        failures.append("the D4 pin sweep found no pin row at all: the sweep surface is empty")
        missing.append(f"{D4_DIR} (pin rows)")

    repins = round_repin_rows()
    measurement["repin_rows"] = [row["path"] for row in repins]
    structured_repins = [row for row in repins if row["structured"]]
    measurement["structured_repin_rows"] = [row["path"] for row in structured_repins]
    repinned = set()
    for row in structured_repins:
        for surface in drifted_surfaces:
            if surface in row["text"]:
                try:
                    live = sha(safe_path(surface).read_bytes())
                except (OSError, ValueError):
                    continue
                if live in row["text"]:
                    repinned.add(surface)
    measurement["repinned_surfaces"] = sorted(repinned)
    unrepinned = [surface for surface in drifted_surfaces if surface not in repinned]
    measurement["unrepinned_surfaces"] = unrepinned
    if drifted_surfaces and not structured_repins:
        failures.append(f"{len(drifted_surfaces)} D4 surface(s) drifted and no round-28 structured "
                        f"re-pin row landed: {drifted_surfaces[:6]}")
    elif unrepinned:
        failures.append(f"{len(unrepinned)} drifted D4 surface(s) are not re-pinned by a round-28 "
                        f"structured row carrying the live digest: {unrepinned[:6]}")

    # ---- battery: 7/7 selftests, 9/9 coverage, every registered baseline pinned
    battery_run = label_run(regressions, "battery")
    try:
        battery = strict_json(battery_run.get("stdout") or "{}")
    except ValueError:
        battery = {}
    summary = battery.get("summary") or {}
    baselines = (battery.get("baselines") or {}).get("summary") or {}
    measurement["battery"] = {
        "exit": battery_run.get("exit"),
        "summary": summary,
        "coverage": baselines.get("coverage"),
        "baselines_found": baselines.get("baselines_found"),
        "pinned": baselines.get("pinned"),
        "gates_registered": baselines.get("gates_registered"),
        "gates_uncovered": baselines.get("gates_uncovered"),
        "findings": battery.get("findings"),
        "baseline_findings": (battery.get("baselines") or {}).get("findings"),
    }
    if battery_run.get("exit") != 0:
        failures.append(f"the gate battery is not green (exit {battery_run.get('exit')})")
    if summary.get("pass") != 7 or summary.get("fail") or summary.get("unevaluable"):
        failures.append(f"the battery reports pass={summary.get('pass')} fail={summary.get('fail')} "
                        f"unevaluable={summary.get('unevaluable')} (expected 7/0/0)")
    if baselines.get("coverage") != "9/9":
        failures.append(f"the battery's registered-gate coverage is {baselines.get('coverage')}, "
                        f"not 9/9")
    if baselines.get("gates_uncovered"):
        failures.append(f"the battery reports uncovered registered gate(s): "
                        f"{baselines.get('gates_uncovered')}")
    if baselines.get("pinned") != baselines.get("baselines_found"):
        failures.append(f"the battery pinned {baselines.get('pinned')} of "
                        f"{baselines.get('baselines_found')} baselines")

    # ---- replays green
    replay = {label: label_run(regressions, label).get("exit") for label in
              ("replay-selftest", "handoff-v2", "handoff-v3-selftest", "handoff-v3")}
    measurement["replays"] = replay
    for label, code in replay.items():
        if code != 0:
            failures.append(f"replay {label} is not green (exit {code})")

    # ---- the v3 baseline the tool actually reads, and the newest round-28 successor
    tool_text = evidence.text(HANDOFF)
    default_match = re.search(r'V3_BASELINE_DEFAULT\s*=\s*"([^"]+)"', tool_text)
    default_path = default_match.group(1) if default_match else V3_BASELINE_FALLBACK
    measurement["v3_baseline_default"] = {"path": default_path,
                                          "declared_in_tool": bool(default_match)}
    baseline = evidence.document(default_path)
    # The v3 baseline's `packet_sha256` is the **handoff packet**'s digest
    # (`exercise-handoff-e2e.py` sets `self.packet_sha256 = sha256_text(self.packet)`,
    # the assembled handoff packet), NOT the D4 source packet's. Comparing it to
    # `examples/culture-d4/packet.d4.yml` is a category error that reads as a
    # permanent false `drift`; the like-for-like comparison is against the digest
    # the replay itself prints for the handoff packet it assembled.
    v3_run = label_run(regressions, "handoff-v3")
    v3_text = (v3_run.get("stdout") or "") + (v3_run.get("stderr") or "")
    live_handoff = re.search(r"packet_sha256=([0-9a-f]{64})", v3_text)
    live_packet = sha(safe_path(PACKET_D4).read_bytes())
    if baseline is None:
        measurement["v3_baseline"] = {"path": default_path, "present": False,
                                      "live_d4_packet_sha256": live_packet}
    else:
        declared = baseline.get("packet_sha256")
        live_handoff_sha = live_handoff.group(1) if live_handoff else None
        measurement["v3_baseline"] = {
            "path": default_path, "present": True,
            "declared_handoff_packet_sha256": declared,
            "live_handoff_packet_sha256": live_handoff_sha,
            "live_d4_packet_sha256": live_packet,
            "reading": ("green" if live_handoff_sha and declared == live_handoff_sha
                        else "drift" if live_handoff_sha else "not-comparable"),
            "compared_surface": "the assembled handoff packet (NOT the D4 source packet)",
            "profile": baseline.get("profile"),
        }
        if live_handoff_sha and declared != live_handoff_sha:
            failures.append(f"the v3 baseline {default_path} pins handoff packet {declared[:12]}… but "
                            f"the replay assembled {live_handoff_sha[:12]}…")
    successors = sorted(str(path.relative_to(ROOT)) for path in
                        safe_path(ROUND_DIR).rglob("**/expected.json")
                        if "v3" in path.parent.name or "handoff" in str(path.parent))
    measurement["v3_successor_rows"] = successors[:12]
    drift_lines = [line for line in v3_text.splitlines()
                   if "input-digest" in line or "E2E-DIGEST" in line]
    measurement["v3_replay"] = {
        "exit": v3_run.get("exit"),
        "default_baseline": default_path,
        "drift_lines": drift_lines[:10],
        "blocker": ("the tool's default v3 baseline is not re-pointed to a post-fix successor "
                    "row" if v3_run.get("exit") != 0 else None),
    }
    successor_replays = []
    for row in successors:
        run = run_command(f"v3-successor-{len(successor_replays)}",
                          (HANDOFF, "--profile", "v3", "--baseline", row, "--quiet"), timeout=600)
        successor_replays.append({"row": row, "exit": run.get("exit"), "command": run["command"],
                                  "stdout_tail": (run.get("stdout") or "")[-200:]})
    measurement["v3_successor_replays"] = successor_replays
    green_successors = [row["row"] for row in successor_replays if row["exit"] == 0]
    measurement["v3_green_successors"] = green_successors
    if v3_run.get("exit") != 0 and not green_successors:
        failures.append("the v3 replay is red and no round-28 successor baseline replays green: "
                        "the re-point is missing, not merely unwired")
    elif v3_run.get("exit") != 0:
        failures.append(f"the tool's default v3 baseline ({default_path}) is not re-pointed to the "
                        f"green round-28 successor {green_successors[0]}: the default pointer is the "
                        f"remaining O surface")

    # ---- auditors: the round-28 independent audit seats on the sweep surface.
    auditors = []
    audit_dir = safe_path(f"{ROUND_DIR}/audit")
    if audit_dir.is_dir():
        for path in sorted(audit_dir.iterdir()):
            if path.suffix.lower() != ".md" or not path.is_file():
                continue
            text = evidence.text(str(path.relative_to(ROOT)))
            auditors.append({
                "path": str(path.relative_to(ROOT)),
                "bytes": len(text.encode("utf-8")),
                "names_a_sweep": bool(re.search(r"(?i)sweep|pin|drift|re-?pin", text)),
                "carries_a_receipt": bool(re.search(
                    r"(?i)\b(exit|command|selftest|receipt|measured)\b", text)),
            })
    measurement["auditors"] = {
        "rows_total": metric(len(auditors), "round-28 audit reports on the sweep surface"),
        "rows": auditors[:12],
    }
    sweep_auditors = [row for row in auditors if row["names_a_sweep"] and row["carries_a_receipt"]]
    measurement["auditors"]["sweep_auditors"] = len(sweep_auditors)
    if not sweep_auditors:
        failures.append(f"no round-28 auditor report reads the sweep surface under {ROUND_DIR}/audit "
                        f"(the O acceptance names auditors)")

    # ---- regressions
    measurement["regressions"] = regressions["measurement"]
    failures.extend(regressions["failures"])
    return result(failures, measurement, missing)


# --------------------------------------------------------------------------
# Claim C — the RL-3 ceiling as craft knowledge
# --------------------------------------------------------------------------

def baseline_entry_names(revision):
    """Every `corpus/knowledge/linguistics/*.md` path at the declared baseline."""
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return None
    raw = git("ls-tree", "-r", "-z", revision, "--", LINGUISTICS_DIR)
    if raw is None:
        return None
    names = set()
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        _metadata, name = entry.split(b"\t", 1)
        names.add(os.fsdecode(name))
    return names


def partition_counts():
    base = safe_path(KNOWLEDGE_DIR)
    counts = {}
    if not base.is_dir():
        return counts
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        counts[directory.name] = len(list(directory.glob("*.md")))
    return counts


def measure_ceiling_entry(evidence):
    """Claim C: the ceiling recorded as craft knowledge — an amendment section in
    the round-27 register entry, a NEW sourced entry on register-lexicon ceilings,
    and the corpus README reconciled."""
    failures, measurement, missing = [], {}, []

    claims = evidence.document(CLAIMS) or {}
    baseline_revision = claims.get("baseline_revision")

    # ---- 1. the amendment: a new section in the round-27 entry, never a rewrite
    live_text = evidence.text(R27_REGISTER_ENTRY)
    if not live_text:
        failures.append(f"the round-27 register entry is missing: {R27_REGISTER_ENTRY}")
        missing.append(R27_REGISTER_ENTRY)
        return result(failures, measurement, missing)
    raw = git("show", f"{baseline_revision}:{R27_REGISTER_ENTRY}") if isinstance(
        baseline_revision, str) else None
    baseline_text = raw.decode("utf-8") if raw else None
    live_headers = SECTION_RE.findall(live_text)
    baseline_headers = SECTION_RE.findall(baseline_text) if baseline_text else None
    new_sections = [header for header in live_headers
                    if baseline_headers is None or header not in baseline_headers]
    lost_sections = [header for header in (baseline_headers or [])
                     if header not in live_headers]
    amendment_sections = [header for header in new_sections
                          if CEILING_RE.search(header) or
                          CEILING_RE.search(_section_body(live_text, header))]
    measurement["amendment"] = {
        "path": R27_REGISTER_ENTRY,
        "baseline_revision": baseline_revision,
        "baseline_sections": len(baseline_headers) if baseline_headers is not None else None,
        "live_sections": len(live_headers),
        "new_sections": new_sections,
        "lost_sections": lost_sections,
        "amendment_sections": amendment_sections,
        "prefix_preserved": bool(baseline_text) and live_text.startswith(baseline_text),
        "bytes_before": len(baseline_text.encode("utf-8")) if baseline_text else None,
        "bytes_after": len(live_text.encode("utf-8")),
        "names_the_ceiling": bool(CEILING_RE.search(live_text)),
        "names_the_round27_measurement": bool(re.search(
            r"(?i)reports/round-27/(law|audit|scribe)/|RL-3", live_text)),
        "command": f"{COMMAND} (baseline section headers vs live; new ceiling section)",
        "date": today()}
    if baseline_text is None:
        failures.append(f"cannot read {R27_REGISTER_ENTRY} at the declared baseline: the amendment "
                        f"cannot be distinguished from a rewrite")
        missing.append(f"{R27_REGISTER_ENTRY} (baseline)")
    else:
        if lost_sections:
            failures.append(f"the amendment removed {len(lost_sections)} baseline section(s): "
                            f"{lost_sections[:4]} — an amendment is a new section, not a rewrite")
        if not new_sections:
            failures.append(f"no new section was added to {R27_REGISTER_ENTRY}: the ceiling is not "
                            f"recorded as an amendment entry")
        elif not amendment_sections:
            failures.append(f"the new section(s) {new_sections[:3]} do not record the ceiling "
                            f"(no ceiling/LL-1/LL-2/reverse-illegal vocabulary)")
        if not measurement["amendment"]["names_the_round27_measurement"]:
            failures.append(f"the amendment cites no round-27 measurement of the ceiling")

    # ---- 2. the new sourced entry on register-lexicon ceilings
    baseline_names = baseline_entry_names(baseline_revision)
    live_entries = sorted(path.name for path in safe_path(LINGUISTICS_DIR).glob("*.md"))
    measurement["baseline"] = {
        "revision": baseline_revision,
        "linguistics_entries_at_baseline": len(baseline_names) if baseline_names is not None else None,
        "linguistics_entries_live": len(live_entries),
    }
    if baseline_names is None:
        failures.append("cannot read the declared baseline's linguistics partition "
                        "(the new entry's newness cannot be established)")
        missing.append(f"{LINGUISTICS_DIR} (baseline)")

    new_entries = [name for name in live_entries
                   if baseline_names is not None and f"{LINGUISTICS_DIR}/{name}" not in baseline_names]
    measurement["new_entries"] = new_entries
    if not new_entries:
        failures.append(f"no new entry landed under {LINGUISTICS_DIR} (absent from the declared "
                        f"baseline): the ceiling is still only in round artifacts")
        missing.append(f"{LINGUISTICS_DIR} (new ceiling entry)")
        return result(failures, measurement, missing)

    def subject_score(name):
        text = evidence.text(f"{LINGUISTICS_DIR}/{name}")
        head = text[:5000].lower()
        score = sum(token in head for token in
                    ("ceiling", "register", "reverse", "derivation", "semantic field",
                     "lexicon", "spell"))
        return score, text

    scored = sorted(((subject_score(name)[0], name, subject_score(name)[1])
                     for name in new_entries), key=lambda item: item[0])
    score, entry_name, text = scored[-1]
    relative = f"{LINGUISTICS_DIR}/{entry_name}"
    measurement["entry"] = {
        "path": relative, "bytes": len(text.encode("utf-8")), "subject_score": score,
        "sha256": sha(safe_path(relative).read_bytes()) if safe_path(relative).is_file() else None,
        "names_the_ceiling": bool(CEILING_RE.search(text)),
        "names_the_general_lesson": bool(re.search(
            r"(?i)derivation operation|operation.*constrain|constrain.*semantic field|"
            r"which semantic fields|native.*spell", text)),
    }
    if score == 0:
        failures.append(f"the new entry {relative} never names the register-lexicon-ceiling subject")
    if not measurement["entry"]["names_the_ceiling"]:
        failures.append(f"the new entry {relative} does not name the ceiling it records")
    if not measurement["entry"]["names_the_general_lesson"]:
        failures.append(f"the new entry {relative} states no general craft lesson (a register's "
                        f"derivation operation constrains which semantic fields it can spell)")

    missing_frontmatter = [key for key, pattern in FRONTMATTER.items() if not pattern.search(text)]
    measurement["frontmatter"] = {key: bool(pattern.search(text))
                                  for key, pattern in FRONTMATTER.items()}
    if missing_frontmatter:
        failures.append(f"the entry {relative} is not frontmatter-complete: missing "
                        f"{missing_frontmatter} (QUALITY.md's provenance/coupling bar)")

    grounded = ROUND_ARTIFACT_RE.findall(text)
    citations = SOURCE_CITATION_RE.findall(text)
    measurement["grounding"] = {
        "round_artifacts_named": sorted(set(grounded))[:12],
        "round_artifacts_total": len(set(grounded)),
        "citation_years": len(citations),
    }
    if not grounded:
        failures.append(f"the entry {relative} names no round-26/27/28 artifact: it is not grounded "
                        f"in the work it records")
    if len(citations) < 3:
        failures.append(f"the entry {relative} carries {len(citations)} dated source token(s); a "
                        f"sourced entry needs cited external sources")
    if not GAP_NAMED_RE.search(text):
        failures.append(f"the entry {relative} does not name the gap it fills")
    if not DECISION_RECORD_RE.search(text):
        failures.append(f"the entry {relative} carries no decision record")
    if CANON_CLAIM_RE.search(text):
        failures.append(f"the entry {relative} makes a canon claim (out of province for this lane)")

    # ---- 3. the corpus README reconciled
    readme = evidence.text(CORPUS_README)
    if not readme:
        failures.append(f"the corpus index is missing: {CORPUS_README}")
        missing.append(CORPUS_README)
        return result(failures, measurement, missing)
    revisions = REVISION_RE.findall(readme)
    counts = partition_counts()
    declared = {name: int(value) for name, value in PARTITION_HEADER_RE.findall(readme)}
    mismatches = {name: {"declared": value, "measured": counts.get(name)}
                  for name, value in declared.items() if counts.get(name) != value}
    measurement["corpus_readme"] = {
        "path": CORPUS_README,
        "revision_head": revisions[0] if revisions else None,
        "revisions": revisions[:4],
        "partition_headers": declared,
        "measured_partitions": counts,
        "mismatches": mismatches,
        "names_the_entry": entry_name in readme,
        "names_the_amendment": R27_REGISTER_ENTRY.split("/")[-1] in readme,
        "total_files": sum(counts.values()),
    }
    if not revisions:
        failures.append(f"{CORPUS_README} carries no `revision:` line")
    if entry_name not in readme:
        failures.append(f"{CORPUS_README} does not index the new entry {entry_name}")
    if mismatches:
        failures.append(f"{CORPUS_README}'s partition headers disagree with the tree: {mismatches}")
    return result(failures, measurement, missing)


def _section_body(text, header):
    """The body of the `## header` section: the bytes up to the next `## `."""
    match = re.search(r"(?m)^##\s+" + re.escape(header) + r"\s*$", text)
    if not match:
        return ""
    rest = text[match.end():]
    following = re.search(r"(?m)^##\s+", rest)
    return rest[:following.start()] if following else rest


# --------------------------------------------------------------------------
# Runner plumbing
# --------------------------------------------------------------------------

def copy_into_clone(live, relative, target_root):
    source = live / relative
    if not source.exists():
        return False
    destination = target_root / relative
    if source.is_dir():
        shutil.copytree(source, destination, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(".scratch", "__pycache__"))
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    return True


def sync_round_surface(live):
    """Copy the live lane's surfaces into this tree. A no-op when the runner is
    executing in the live lane itself."""
    synced = {}
    if live.resolve() == ROOT.resolve():
        for relative in SYNC_PATHS:
            source = live / relative
            if source.exists():
                synced[relative] = sha(source.read_bytes()) if source.is_file() else "tree"
        return synced
    for relative in SYNC_PATHS:
        source = live / relative
        if not source.exists():
            continue
        if source.is_dir():
            for child in sorted(source.iterdir()):
                if child.name in ("validation.json", ".scratch", "__pycache__"):
                    continue
                copy_into_clone(live, f"{relative}/{child.name}", ROOT)
        else:
            copy_into_clone(live, relative, ROOT)
        synced[relative] = sha(source.read_bytes()) if source.is_file() else "tree"
    return synced


def _raises(function, *args):
    try:
        function(*args)
        return False
    except Exception:
        return True


def selftest():
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    # ---- the law reader: each resolution fires on its own tamper and not on a clean row
    def law_packet(**overrides):
        rows = [{"id": f"RGL-0{n}", "register": "QREG-02", "axis": "mark",
                 "speaker": "stamp-holder, furnace-master (RK-03)",
                 "holder": "a stamp-holder",
                 "force": "directive-binding for the charge",
                 "consequence": "the spoken form binds and is entered on the stamp-roll",
                 "design_row": ["QREG-02"]}
                for n in range(1, 6)]
        rows[0].update(overrides)
        return {"registers": [{"id": "QREG-01", "register": "plain"},
                              {"id": "QREG-02", "register": "stamp"}],
                "rank_rules": [{"id": "RK-03"}, {"id": "RK-04"}],
                "records": [{"id": "OR-01"}, {"id": "OR-02"}],
                "register_law": rows}

    clean_packet = law_packet()
    findings, context = law_check(clean_packet)
    check("law-reader-clean-packet-is-silent", findings == [], observed=findings)
    check("law-reader-counts-records", context["record_ids"] == 11, observed=context["record_ids"])

    found = law_check(law_packet(design_row=["QREG-99"]))[0]
    check("law-reader-flags-a-dangling-design-row",
          any(item["class"] == "D4L-LAW-DANGLING" and item["token"] == "QREG-99" for item in found),
          observed=found)
    short = law_packet()
    short["register_law"] = short["register_law"][:4]
    check("law-reader-flags-a-missing-declared-row",
          any(item["class"] == "D4L-LAW-ROW" and item["row"] == "RGL-05"
              for item in law_check(short)[0]), observed=law_check(short)[0])

    bad = dict(clean_packet)
    bad["register_law"] = [dict(clean_packet["register_law"][0], force="no-such-force")]
    found = law_check(bad)[0]
    check("law-reader-flags-an-unknown-force",
          any(item["class"] == "D4L-LAW-FORCE" for item in found), observed=found)

    found = law_check(law_packet(force="no-such-force"))[0]
    check("law-reader-flags-an-unknown-force",
          any(item["class"] == "D4L-LAW-FORCE" for item in found), observed=found)

    found = law_check(law_packet(speaker="nobody-nowhere (ZZ-99)"))[0]
    check("law-reader-flags-an-unresolvable-speaker",
          any(item["class"] == "D4L-LAW-SPEAKER" and item["agent"] == "ZZ-99" for item in found),
          observed=found)

    found = law_check(law_packet(consequence="the act evaporates silently"))[0]
    check("law-reader-flags-a-consequence-with-no-machinery",
          any(item["class"] == "D4L-LAW-CONSEQUENCE" for item in found), observed=found)

    found = law_check(law_packet(axis="nonsense"))[0]
    check("law-reader-flags-an-out-of-vocabulary-axis",
          any(item["class"] == "D4L-LAW-AXIS" for item in found), observed=found)

    found = law_check(law_packet(register="no-register"))[0]
    check("law-reader-flags-an-undeclared-register",
          any(item["class"] == "D4L-LAW-REGISTER" for item in found), observed=found)

    # a single-row fixture, filtered to one class (the other classes are the
    # declared-row resolution firing, which is not what these controls test)
    def one_row(**row):
        base = {"id": "RGL-04", "axis": "fire",
                "force": "none — a sound-channel constraint",
                "consequence": "no phoneme is licensed"}
        base.update(row)
        return {"registers": [{"id": "QREG-01", "register": "plain"}], "register_law": [base]}

    check("law-reader-accepts-the-none-force",
          not [item for item in law_check(one_row())[0] if item["class"] == "D4L-LAW-FORCE"])
    check("law-reader-does-not-resolve-a-non-act-consequence",
          not [item for item in law_check(one_row())[0]
               if item["class"] == "D4L-LAW-CONSEQUENCE"],
          observed=law_check(one_row())[0])
    check("law-reader-resolves-a-binding-act-consequence",
          not [item for item in law_check(one_row(id="RGL-01", axis="mark",
                                                  force="directive-binding for the charge",
                                                  consequence="binds and is entered on the stamp-roll"))[0]
               if item["class"] == "D4L-LAW-CONSEQUENCE"])
    check("law-reader-accepts-the-register-name-not-only-the-id",
          not [item for item in law_check(
              {"registers": [{"id": "QREG-02", "register": "stamp"}],
               "register_law": [{"id": "RGL-01", "register": "stamp", "axis": "mark",
                                 "force": "directive-binding", "consequence": "entered on the roll"}]})[0]
              if item["class"] == "D4L-LAW-REGISTER"],
          observed=law_check({"registers": [{"id": "QREG-02", "register": "stamp"}],
                              "register_law": [{"id": "RGL-01", "register": "stamp"}]})[0])
    check("law-reader-accepts-a-declared-vocabulary",
          not [item for item in law_check(one_row(force="assertive-attested"),
                                          force_vocabulary=("assertive-attested",))[0]
               if item["class"] == "D4L-LAW-FORCE"])
    check("law-reader-rejects-an-undeclared-vocabulary",
          bool([item for item in law_check(one_row(force="wibble"))[0]
                if item["class"] == "D4L-LAW-FORCE"]))

    # ---- the tamper rewrite: textual, one value, byte-different, and reversible
    packet = ('register_law:\n  -\n    id: "RGL-01"\n'
              '    force: "directive-binding for the charge"\n'
              '    speaker: "stamp-holder (RK-03)"\n'
              '    consequence: "binds and is entered on the stamp-roll"\n')
    tampered = tamper_law_text(packet, "force")
    check("tamper-force-changes-the-bytes", tampered != packet)
    check("tamper-force-changes-one-value",
          tampered.count("no-such-force") == 1 and tampered.count("RGL-01") == 1, observed=tampered)
    check("tamper-force-leaves-the-other-fields",
          'speaker: "stamp-holder (RK-03)"' in tampered)
    check("tamper-speaker-changes-the-speaker",
          "nobody-nowhere (ZZ-99)" in tamper_law_text(packet, "speaker"))
    check("tamper-consequence-changes-the-consequence",
          "evaporates silently" in tamper_law_text(packet, "consequence"))
    check("tamper-unknown-mutation-refused", _raises(tamper_law_text, packet, "wibble"))

    # ---- the law finding id and record id parsers
    check("law-finding-ids-parsed",
          law_finding_ids("FINDING D4L-LAW-FORCE: RGL-01 force names no class") ==
          ["D4L-LAW-FORCE"], observed=law_finding_ids("FINDING D4L-LAW-FORCE: x"))
    check("law-finding-ids-empty-on-clean-text", law_finding_ids("12 findings, no law class") == [])
    check("law-finding-lines-carry-the-row-and-class",
          law_finding_lines("FINDING D4L-LAW-FORCE: [hold] RGL-01 — no-such-force") ==
          ["FINDING D4L-LAW-FORCE: [hold] RGL-01 — no-such-force"],
          observed=law_finding_lines("FINDING D4L-LAW-FORCE: [hold] RGL-01 — no-such-force"))
    check("law-finding-lines-are-deduped-and-sorted",
          law_finding_lines("FINDING D4L-LAW-ROW: RGL-05\nFINDING D4L-LAW-FORCE: x\n"
                            "FINDING D4L-LAW-FORCE: x\n") ==
          ["FINDING D4L-LAW-FORCE: x", "FINDING D4L-LAW-ROW: RGL-05"])
    check("law-finding-lines-require-the-finding-prefix",
          law_finding_lines("| D4L-LAW-CONSEQUENCE | RGL-04 | a table row, not a finding |\n"
                            "D4L-LAW-DANGLING: bare, no prefix\n") == [],
          observed=law_finding_lines("| D4L-LAW-CONSEQUENCE | RGL-04 | table |\n"))
    check("law-finding-lines-empty-on-clean-text", law_finding_lines("12 findings") == [])
    check("law-finding-lines-separate-a-saturated-class-from-a-new-line",
          set(law_finding_lines("FINDING D4L-LAW-CONSEQUENCE: RGL-04\n"
                                "FINDING D4L-LAW-CONSEQUENCE: RGL-05\n")) -
          set(law_finding_lines("FINDING D4L-LAW-CONSEQUENCE: RGL-04\n")) ==
          {"FINDING D4L-LAW-CONSEQUENCE: RGL-05"})
    check("agent-id-parsed", AGENT_ID_RE.findall("mold-keeper (OR-02, component-only)") == ["OR-02"])
    check("agent-id-absent-on-a-bare-name", AGENT_ID_RE.findall("stamp-holder") == [])
    check("record-id-shaped", bool(RECORD_ID_RE.match("OR-02")) and not RECORD_ID_RE.match("nope"))

    # ---- the ceiling vocabulary detector
    check("ceiling-detected-on-the-round27-phrasing",
          bool(CEILING_RE.search("the register cannot spell any legal abstraction (the ceiling)")))
    check("ceiling-detected-on-the-ll-ids", bool(CEILING_RE.search("declared as LL-1/LL-2")))
    check("ceiling-absent-on-an-unrelated-section",
          not CEILING_RE.search("## 4. The speech-act framework, as a designer's toolkit"))

    # ---- the amendment reader
    base = "## 1. One\nbody\n## 2. Two\nbody\n"
    amended = base + "## 10. The register-lexicon ceiling\nreverse-illegal, LL-1\n"
    base_headers = SECTION_RE.findall(base)
    live_headers = SECTION_RE.findall(amended)
    check("section-headers-parsed", base_headers == ["1. One", "2. Two"], observed=base_headers)
    check("new-section-detected",
          [h for h in live_headers if h not in base_headers] ==
          ["10. The register-lexicon ceiling"])
    check("lost-section-detected",
          [h for h in base_headers if h not in live_headers] == [])
    check("prefix-preserved-on-an-append", amended.startswith(base))
    check("prefix-not-preserved-on-a-rewrite", not "## 1. O\n" .startswith("## 1. One\n"))
    check("section-body-read",
          _section_body(amended, "10. The register-lexicon ceiling").strip() ==
          "reverse-illegal, LL-1", observed=_section_body(amended, "10. The register-lexicon ceiling"))

    # ---- pin-row digest extraction
    pairs = digest_pairs({"inputs": {"examples/culture-d4/packet.d4.yml": "a" * 64}})
    check("digest-pair-flat-map", pairs == [("examples/culture-d4/packet.d4.yml", "a" * 64)],
          observed=pairs)
    pairs = digest_pairs({"artifact_manifest": {"examples/culture-d4/packet.d4.yml":
                                                {"sha256": "b" * 64, "bytes": 1}}})
    check("digest-pair-nested-sha256", pairs == [("examples/culture-d4/packet.d4.yml", "b" * 64)],
          observed=pairs)
    check("digest-pair-ignores-non-hex", digest_pairs({"x.yml": "not-a-digest"}) == [])
    check("d4-surface-recognised", is_d4_surface("examples/culture-d4/packet.d4.yml"))
    check("non-d4-surface-refused", not is_d4_surface("examples/culture-d2/packet.d2.yml"))
    check("manifest-pairs-parsed", manifest_pairs.__doc__ is not None)

    # ---- frontmatter / README parsers
    entry = ("# X\n- topic: t\n- sources: A 2010\n- verified-at: 2026-10-18\n"
             "- recheck: y\n- couples: z\n")
    check("frontmatter-complete", all(pattern.search(entry) for pattern in FRONTMATTER.values()))
    check("frontmatter-detects-a-miss",
          not FRONTMATTER["recheck"].search("# X\n- topic: t\n"))
    check("partition-header-parsed",
          PARTITION_HEADER_RE.findall("## linguistics/ (21)\n## synthesis/ (29)\n")
          == [("linguistics", "21"), ("synthesis", "29")])
    check("revision-parsed", REVISION_RE.findall("revision: 1.8 — Round-28\n") == ["1.8"])
    check("round-artifact-path-parsed",
          ROUND_ARTIFACT_RE.findall("see reports/round-27/law/impl.md") ==
          ["reports/round-27/law/impl.md"])
    check("round-28-artifact-path-parsed",
          ROUND_ARTIFACT_RE.findall("see reports/round-28/law/impl.md") ==
          ["reports/round-28/law/impl.md"])
    check("canon-claim-detected", bool(CANON_CLAIM_RE.search("this is canon now")))
    check("canon-claim-absent-on-a-design-record", not CANON_CLAIM_RE.search("a NON-CANON design"))

    check("legs-parsed-off-a-gate-run", gate_legs(
        "ok   L3-build\nFAIL L3-routing-consistency\nsummary: 1/2 legs passed\n")
        == (["L3-build"], ["L3-routing-consistency"], 1, 2))
    check("protected-covers-round-27", "reports/round-27" in PROTECTED)
    check("protected-stops-at-round-27", "reports/round-28" not in PROTECTED)
    check("rl4-components-are-the-two-the-review-named",
          set(RL4_COMPONENTS) == {f"{D4_COMPONENTS}/03-orthography.yml",
                                  f"{D4_COMPONENTS}/09-costumes.yml"})
    check("rl4-ids-cover-or-li-en", set(RL4_RECORD_IDS) == {
        "OR-01", "OR-02", "OR-03", "LI-01", "LI-02", "LI-03", "EN-01", "EN-02"})

    passed_controls = sum(1 for item in controls if item["passed"])
    for item in controls:
        print(("ok   " if item["passed"] else "FAIL ") + item["control"]
              + ("" if item["passed"] else f" — {item}"))
    print(f"selftest: {passed_controls}/{len(controls)} checks passed — this runner's own law reader "
          "(speaker/force/consequence/register/axis/design_row/declared-row resolutions, each fired "
          "on its own tamper and silent on a clean row), the textual tamper rewrite, the "
          "law-finding-line/agent-id/record-id parsers, the ceiling vocabulary, the amendment section "
          "reader, the pin-row digest extractor and the frontmatter/partition readers; no file opened "
          "for writing")
    return 0 if passed_controls == len(controls) else 1


def measure():
    evidence = Evidence()
    claims = evidence.document(CLAIMS) or {}
    targets = evidence.document(TARGETS) or {}
    baseline = claims.get("baseline_revision")
    live = live_lane()
    if live is None:
        raise ValueError("cannot locate the live lane root above the isolated clone")
    synced = sync_round_surface(live)
    preservation = protected_baseline(baseline)
    regressions = measure_regressions()
    results = {}
    for claim_id, operation in (
            ("D", lambda: measure_law_replay(evidence, regressions)),
            ("O", lambda: measure_pin_sweep(evidence, regressions)),
            ("C", lambda: measure_ceiling_entry(evidence))):
        try:
            results[claim_id] = operation()
        except (OSError, ValueError, TypeError, KeyError, RuntimeError, AttributeError,
                subprocess.SubprocessError, shutil.Error) as error:
            results[claim_id] = result([f"Could not evaluate claim {claim_id}: "
                                        f"{type(error).__name__}: {error}"], {})
    changed_inputs = []
    for relative, expected in evidence.inputs.items():
        try:
            observed = sha(safe_path(relative).read_bytes())
        except (OSError, ValueError):
            observed = None
        if expected != observed:
            changed_inputs.append(relative)
    coherence = []
    if claims.get("round") != 28 or targets.get("round") != 28:
        coherence.append("Claims/targets are not both round 28")
    if targets.get("baseline_revision") != baseline:
        coherence.append("Claims/targets disagree on the declared baseline")
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"D": "depth", "O": "operability", "C": "coverage"}:
        coherence.append("Declared claim set is not D/depth, O/operability, C/coverage")
    worker_total = sum(targets.get("workers", {}).values()) if isinstance(targets.get("workers"), dict) else None
    if worker_total != claims.get("workers"):
        coherence.append("Targets worker counts do not sum to the declared worker wave")
    if changed_inputs:
        coherence.append("Evidence changed while being measured: " + ", ".join(changed_inputs))
    coherence.extend(evidence.errors)
    failures = [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                for failure in item["failures"]]
    failures.extend("preservation: " + item for item in preservation["failures"])
    failures.extend("evidence: " + item for item in coherence)
    return {"round": 28, "runner": RUNNER, "runner_sha256": sha(safe_path(RUNNER).read_bytes()),
            "counting_command": COMMAND, "date": today(), "measured_at_utc": now_utc(),
            "baseline_revision": baseline, "targets_date": targets.get("date"),
            "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results,
            "failures": failures, "missing_dependencies": sorted(evidence.missing | {
                path for item in results.values() for path in item["missing_dependencies"]}),
            "protected_filed_artifacts": preservation,
            "synced_from_live": {key: value for key, value in sorted(synced.items())},
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": [
                "Run this round validator in the lane root or an isolated clone under the lane's .scratch with TMPDIR below it. It never edits filed bytes, never commits, and never pushes.",
                "Claim D is measured from the delivered bytes and by behaviour: the law block and its declaring component, this runner's own law resolutions (speaker/force/consequence/design_row/declared-row) over the delivered packet, the presence of a `D4L-LAW-*` finding id under tools/, the delivered checking leg run on the clean packet AND on three tampered copies this runner writes itself (graded on the line-level delta), the three byte-identical regenerations, the gate exits, the RL-4 packet_keys/record-presence measurement, the hold set's revision, and the round-28 artifact's receipt. The delivered implementation's shape (which tool owns the leg, which field names each resolution) is deliberately not pinned beyond what the claim names.",
                "The tamper controls are this runner's own construction, not quotes: each rewrites exactly one named field of the first law row in the packet TEXT (never a re-serialisation, so every other byte is the assembler's). A tamper that fails to change the bytes is reported as an inert control rather than counted as a pass. The teeth test is the DELTA over finding lines, never the clean packet's silence: the delivered law has real defects and the D seat's own design measures six honest findings on the clean bytes, two of whose classes are saturated, so a class-id delta would mask a caught tamper.",
                "Claim D's law reader is this runner's own reading; a delivered leg that implements a different but equivalent resolution still passes as long as each tamper adds a `D4L-LAW-*` finding line over the clean packet. Where the two readings disagree the runner reports both rather than adjudicating silently.",
                "Claim O is measured as one sweep over every row that pins a D4 surface: the frozen manifests, the battery baselines, the typed-pipeline profile, the hold set, the v3 read-set baseline and the historical round-20/22/26/27 rows. A declared digest equal to the live bytes reads `green`; a mismatch reads `drift` and must be re-pinned by a NEW round-28 row that names the surface and carries the live digest. Filed rounds 8-27 stay byte-identical; a drift in a filed historical row is recorded, never repaired in place.",
                "Claim O's pin surface is baseline-relative and the tree moves under it: a row re-pinned before a later landing goes stale again. The sweep reports the drift it measured at measurement time; it does not assert that no drift will appear later.",
                "Claim C is measured as an amendment plus a new entry: every section header of `corpus/knowledge/linguistics/register-strata-attestation.md` at the declared baseline must still be present (an amendment adds a section, never rewrites), at least one new section must carry the ceiling vocabulary, and a NEW linguistics entry (absent from the declared baseline by Git blob identity) must be frontmatter-complete, name the gap, carry a decision record, be grounded in round-26/27/28 artifacts and dated external sources, state the general craft lesson, and make no canon claim. corpus/README.md must index it and its partition headers must reproduce the measured tree.",
                "Protected reports and frozen generations of rounds 8-27 must match the round-28 declared baseline; new round-28 files live under reports/round-28, corpus/knowledge and corpus/README.md.",
            ]}


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def dependencies_ready():
    """The artifacts the three claims depend on, measured as *readiness conditions*
    rather than guessed directory names — a seat may file its work under any
    subdirectory, and an empty directory is not a landing. Used only by --wait.

      * D: the law's replay leg is delivered (a tool under `tools/` names a
        `D4L-LAW-*` finding id) and a round-28 D artifact exists.
      * O: a round-28 structured re-pin row exists and a round-28 audit report
        exists.
      * C: the register entry carries a new section and a new linguistics entry
        exists (absent from the declared baseline).
    """
    pending = []
    producers = []
    for path in safe_path("tools").rglob("*.py"):
        try:
            if "D4L-LAW" in path.read_text(encoding="utf-8", errors="replace"):
                producers.append(path)
        except OSError:
            continue
    if not producers:
        pending.append("tools/ (a delivered D4L-LAW-* replay leg)")
    if not find_round_artifacts(("law", "replay", "register", "rl4", "packet")):
        pending.append(f"{ROUND_DIR}/ (a D artifact)")
    if not [row for row in round_repin_rows() if row["structured"]]:
        pending.append(f"{ROUND_DIR}/ (a structured re-pin row)")
    audit_dir = safe_path(f"{ROUND_DIR}/audit")
    if not (audit_dir.is_dir() and any(path.suffix.lower() == ".md"
                                       for path in audit_dir.iterdir() if path.is_file())):
        pending.append(f"{ROUND_DIR}/audit (an auditor report)")
    claims = None
    try:
        claims = strict_json(safe_path(CLAIMS).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        claims = None
    baseline = (claims or {}).get("baseline_revision")
    baseline_names = baseline_entry_names(baseline) if baseline else None
    if not (safe_path(R27_REGISTER_ENTRY).is_file()):
        pending.append(R27_REGISTER_ENTRY)
    else:
        live = safe_path(R27_REGISTER_ENTRY).read_text(encoding="utf-8", errors="replace")
        raw = git("show", f"{baseline}:{R27_REGISTER_ENTRY}") if baseline else None
        if raw is not None:
            base = raw.decode("utf-8", "replace")
            if not [header for header in SECTION_RE.findall(live)
                    if header not in SECTION_RE.findall(base)]:
                pending.append(f"{R27_REGISTER_ENTRY} (the ceiling amendment section)")
    if baseline_names is not None:
        new_entries = [path for path in safe_path(LINGUISTICS_DIR).glob("*.md")
                       if f"{LINGUISTICS_DIR}/{path.name}" not in baseline_names]
        if not new_entries:
            pending.append(f"{LINGUISTICS_DIR} (the ceiling entry)")
    return pending


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Measure round-28 D/O/C acceptance; run in the lane root or an isolated clone.")
    parser.add_argument("--check", action="store_true",
                        help="print the measured JSON without writing validation.json")
    parser.add_argument("--selftest", action="store_true",
                        help="exercise runner positive/negative controls without dependencies")
    parser.add_argument("--wait", type=int, default=0, metavar="SECONDS",
                        help="poll for late dependency artifacts (max 1200s) before measuring")
    args = parser.parse_args(argv)
    if args.check and args.selftest:
        parser.error("--check and --selftest are mutually exclusive")
    if not (ROOT / ".git").is_dir():
        print("could-not-evaluate: run round validators inside a Git checkout", file=sys.stderr)
        return 2
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    if args.selftest:
        return selftest()
    if args.wait:
        deadline = time.monotonic() + min(args.wait, 1200)
        while time.monotonic() < deadline:
            pending = dependencies_ready()
            if not pending:
                break
            print(f"waiting on {len(pending)} dependency path(s): {', '.join(pending)}",
                  file=sys.stderr)
            time.sleep(60)
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
