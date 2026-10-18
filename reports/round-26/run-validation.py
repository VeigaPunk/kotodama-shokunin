#!/usr/bin/env python3
"""Round-26 acceptance runner: claims D (register stratum), O (remainders), C (open questions).

Claim D — the register stratum lands in D4 end-to-end and the round-17 forecast closes.
  `reports/round-25/argot/delta.md` measured the round-17 Δ3 forecast as **not
  delivered**: the delivered schema had no `derived_from`/`derivation` field, no
  operation dimension, and the register-scoped domain was empty
  (`derived_pairs=0`), so the argot leg replayed an empty set. This runner
  measures the delivered artifact, never an intention:
    * the D4 packet's `contract.record_fields.lexicon` declares the derivation
      relation (or the packet declares its operations), and the packet's own
      components regenerate it byte-for-byte (assembly/adapter/projection
      `--check`, each exit 0);
    * the register-scoped domain is **non-empty**: at least one lexicon record
      declares a machine-readable derivation pair, and the argot gate's own
      coverage line reports `derived_pairs >= 1`, `violations 0`, exit 0;
    * every delivered pair is re-derived by **this runner's own** `head2`/
      `reverse` implementation (never read back from the gate), the base
      resolves to a record of the same packet, and no record is its own base
      (the round-25 review's 6A.2/6A.3 false-green classes);
    * the typed projection classifies the register forms per the label-typing
      table — a supplied register form is `native-form`/`borrowed-strata`, an
      English-gloss field is `translated-label`, and every owed register label
      is covered by a named hold row;
    * the D4 typed gate passes and the hold set is updated and **named**
      (a round-26 revision note or supersession pin on `expected-holds.json`,
      with the counts agreeing with the projection's coverage block);
    * the round-26 D artifact names the forecast **delivered/closed** and names
      the delta (nothing silently dropped);
    * teeth: a runner-authored violating pair must still emit the argot id
      (exit 1) and its clean counterpart must grade clean (exit 0). The
      half-declared-pair laundering channel and the self-derivation case are
      measured and recorded as review evidence, not graded.

Claim O — the three round-25 remainders dispositioned, regressions green.
  `reports/round-25/audit/x48-v3-supersession.md` named them: the r4 revision
  landed packet-only (no companion `twin.json`), and two sibling pin tails stay
  stale (the combined-source v2 successor pin and the v3 packet-baseline pin).
    * the twin gap is dispositioned either by a **new row** — a round-26
      revision directory carrying `packet.md` + `expected.json` + `twin.json`,
      with the parent named and pinned, the twin judged by the two round-15
      harness validators (exit 0), and its own digest pinned — or by a
      **documented convention with a control**;
    * each pin tail is **re-pointed as a new row**: a round-26 JSON row that
      names the tail and pins the moved file's live digest (the live bytes, not
      the stale pin);
    * a checker bound to the re-pointed rows is green — the round-25 r4 checker
      itself, or a round-26 successor that names both tails;
    * the fixed regression battery is green.

Claim C — the open-question queue 100% dispositioned, README revised as a new file.
  The round-25 lessons index extracted a queue with owners. This runner reads
  the queue ids (from the newest README revision and from the filed
  `corpus/lessons/README.md`), reads the disposition rows under
  `reports/round-26/open-questions/`, and requires: every queue id appears with
  a disposition class; a `fixed` row carries evidence; a `carried` row carries a
  named owner, a reason and a next touch round; zero rows without a disposition.
  The lessons README revision must be a **new file** — the filed
  `corpus/lessons/README.md` bytes must be unchanged from the declared baseline
  (Git blob identity, not a re-read) — and the revision must still reproduce the
  file/row arithmetic, the three census formats and its counting command.

Run only in the lane root or an isolated clone under its .scratch:
  python3 reports/round-26/run-validation.py             (measure + write receipt)
  python3 reports/round-26/run-validation.py --check     (measure only, print)
  python3 reports/round-26/run-validation.py --selftest  (dependency-free controls)
  python3 reports/round-26/run-validation.py --wait 600  (poll late dependencies)
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
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-26"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
CLAIMS = f"{ROUND_DIR}/claims.json"
TARGETS = f"{ROUND_DIR}/targets.json"
OQ_DIR = f"{ROUND_DIR}/open-questions"
LESSONS_DIR = "corpus/lessons"
LESSONS_README = "corpus/lessons/README.md"
README_BASELINE_BLOB = "a31870556c733498243b56697896504a2fb3679a"
PACKET_D4 = "examples/culture-d4/packet.d4.yml"
PACKET_D4_TYPED = "examples/culture-d4/packet.d4.typed.yml"
D4_PROJECTION = "examples/culture-d4/typed-labels.d4.yml"
D4_HOLDS = "examples/culture-d4/expected-holds.json"
D4_COMPONENTS = "examples/culture-d4/components"
ARGOT_GATE = "tools/gates/argot-derivation-gate.py"
TYPED_GATE = "tools/gates/typed-pipeline-gate.py"
PROJECTOR = "tools/d2-typed-labels.py"
D4_ASSEMBLER = "tools/assemble-culture-d4.py"
D4_ADAPTER = "tools/assemble-d4-typed.py"
NAMING_GATE = "tools/gates/naming-collision-gate.py"
V3_PARENT = "reports/round-22/handoff/declared-in-r2/packet.md"
V2_PIN_OLD = "reports/round-20/wart/expected-v2-07-r20.json"
V3_PIN_OLD = "reports/round-20/handoff/expected.json"
R4_REVISION = "reports/round-25/v3-supersession/declared-in-r4"
R4_CHECKER = "reports/round-25/v3-supersession/v3-supersession-check.py"
V3_PIN_STALE = "e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b"
V3_PIN_LIVE = "a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e"
HARNESS_VALIDATORS = ("tools/harness/packet_links.py", "tools/harness/packet_uncertainty.py")
SYNC_PATHS = (ROUND_DIR, "SKILL.md", "LOG.md", "SCORECARD.md", "PROVINCE.md",
              "SHONEN.md", "corpus", "examples", "tools")
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 26)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 26))

# The argot finding id: the round-17 design and the delivered gate spell it
# `D4L-ARGOT-DERIV`; the round-26 claim text spells it `D4L-ARGOT-DERV`. Both
# spellings are accepted and the observed one is recorded, so a claim-text typo
# cannot fail an honest artifact (and an artifact naming neither does).
ARGOT_IDS = ("D4L-ARGOT-DERIV", "D4L-ARGOT-DERV")
ARGOT_HALF_PAIR_ID = "D4L-ARGOT-RULE"
ARGOT_COVERAGE_ID = "D4L-ARGOT-COVERAGE"
# The eleven worked derivations the round-17 design fixes (design-language.md
# §5), pinned here by hand; this runner re-derives them with its own
# implementation, never by reading the design doc back.
ARGOT_WORKED = (
    ("saalumi", "head2", "saalu"), ("min", "reverse", "nim"),
    ("kus", "reverse", "suk"), ("nam", "reverse", "man"),
    ("nes", "reverse", "sen"), ("sam", "reverse", "mas"),
    ("mus", "reverse", "sum"), ("kin", "reverse", "nik"),
    ("sun", "reverse", "nus"), ("samun", "reverse", "numas"),
    ("makun", "reverse", "nukam"),
)
ARGOT_COVERAGE_RE = re.compile(
    r"coverage:\s*\S+\s+records=(\d+)\s+register_scoped=(\d+)\s+derived_pairs=(\d+)"
    r"\s+claimed_chains=(\d+)\s+borrow_pairs=(\d+)\s+violations=(\d+)\s+rule_holds=(\d+)")
UNMARKED_REGISTERS = frozenset(("plain", "neutral", "standard", "ordinary", "unmarked", ""))
SUPPLIED_KINDS = frozenset(("native-form", "borrowed-strata"))
GLOSS_REPRESENTATIONS = frozenset(("english-gloss", "gloss", "translation"))
D4_SCHEMA_FIELDS = ("derived_from", "derivation")
D4_BASELINE_HOLDS = {"hold": 12, "note": 0, "fail": 0}
LESSONS_ROW_RE = re.compile(
    r"(?m)^\|\s*`?(?:corpus/lessons/)?([A-Za-z0-9_.-]+\.md)`?\s*\|")
LESSONS_ROUND_ROW_RE = re.compile(r"(?m)^\|\s*`?round-(\d+)`?\s*\|")
CENSUS_FORMATS = ("gate-keeper", "fragment-index", "plain")
COUNT_COMMAND_RE = re.compile(r"`([^`\n]*(?:ls|find|wc)[^`\n]*)`")
ROWS_DECLARED_RE = re.compile(r"(?i)\brows?\s*[:=]\s*\**\s*(\d{1,3})")
FILES_DECLARED_RE = re.compile(r"(?i)\bfiles?\s*[:=]\s*\**\s*(\d{1,3})")
QUEUE_ID_RE = re.compile(r"(?m)^\|\s*`?(Q-(?=[A-Za-z0-9.-]*\d)[A-Za-z0-9.-]+)`?\s*\|")
Q_ID_ANY_RE = re.compile(r"Q-(?=[A-Za-z0-9.-]*\d)[A-Za-z0-9.-]+")
ROUND_POINTER_RE = re.compile(r"(?i)\b(?:round|r)[- ]?(\d{1,2})\b")
OWNER_LABEL_RE = re.compile(r"(?i)\bowner\b\s*[:=]?")
OWNER_TOKEN_RE = re.compile(
    r"(?i)\b(parent|operator|map-auditor|auditor|seat)\b|`[^`]*/[^`]*`|"
    r"\b[\w.-]+\.(md|json|py|yml|yaml)\b|reports/[\w./-]+")
EVIDENCE_TOKEN_RE = re.compile(
    r"`[^`]*/[^`]*`|`[^`]*(?:exit|selftest|sha256|command|python3)[^`]*`|sha256:[0-9a-f]{8,}|\bexit\s*\d")
FIXED_RE = re.compile(r"(?i)\b(fixed|closed|resolved|repaired)\b")
CARRIED_RE = re.compile(r"(?i)\b(carried|carry|open|pending|carried-forward)\b")
REASON_RE = re.compile(r"(?i)\breason\b|:?\s*because\b|\bwhy\b")
DISP_CLASSES = ("fixed", "carried")

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
    ("d4-label-gate", ("tools/gates/d4-typed-labels-check-gate.py",)),
    ("d4-label-gate-selftest", ("tools/gates/d4-typed-labels-check-gate.py", "--selftest")),
    ("d4-assembly-gate", ("tools/gates/d4-assembly-check-gate.py", PACKET_D4)),
    ("coupling-selftest", ("tools/check-evidence-coupling.py", "--selftest")),
    ("replay-selftest", ("tools/replay-frozen.py", "--selftest")),
    ("handoff-gate-selftest", ("tools/gates/handoff-packet-check.py", "--selftest")),
    ("links-selftest", ("tools/harness/packet_links.py", "--selftest")),
    ("uncertainty-selftest", ("tools/harness/packet_uncertainty.py", "--selftest")),
    ("receipt-guard-selftest", ("tools/harness/receipt_guard.py", "--selftest")),
    ("argot-gate-selftest", (ARGOT_GATE, "--selftest")),
    ("argot-gate-d4", (ARGOT_GATE, PACKET_D4)),
    ("handoff-v2", ("tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet")),
    ("handoff-v3-selftest", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest")),
    ("handoff-v3", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet")),
)
LEG_RE = re.compile(r"^(ok|FAIL)\s+([A-Za-z0-9_.-]+)")
SUMMARY_RE = re.compile(r"summary:\s*(\d+)/(\d+)\s+legs passed")


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


def protected_baseline(revision):
    failures, rows = [], []
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return result(["Round-26 declared baseline is not a full Git revision"], {})
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
    status = git("status", "--porcelain=v1", "--untracked-files=all", "--", *PROTECTED)
    worktree = [line for line in (status or b"").decode("utf-8", "replace").splitlines()
                if line.strip()]
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
    for line in worktree:
        flag, _, path = line.partition(" ")
        if flag == "??" and path.strip():
            rows.append({"path": path.strip(), "baseline_blob": None, "observed_blob": "untracked"})
    if rows:
        failures.append("Filed rounds 8-25 or their frozen generations differ from the declared baseline")
    return result(failures, {"baseline_revision": revision,
                             "protected_paths": metric(len(expected), "git ls-tree of protected baseline"),
                             "differences": rows[:20],
                             "differences_total": metric(len(rows), "compare protected Git blobs to working bytes"),
                             "protected_status_rows": metric(len(worktree), "git status over protected paths")})


def run_command(label, parts, timeout=900):
    scratch = ROOT / ".scratch" / "round-26" / "validation" / label
    scratch.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(scratch), "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
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
    return {key: (value[-7000:] if key == "stdout" else value[-2000:]
                  if key == "stderr" else value) for key, value in item.items()}


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


def load_packet(relative):
    text = safe_path(relative).read_text(encoding="utf-8")
    return yaml_loader()["load_yaml"](text)


def parse_coverage_line(text):
    match = ARGOT_COVERAGE_RE.search(text or "")
    if not match:
        return None
    keys = ("records", "register_scoped", "derived_pairs", "claimed_chains",
            "borrow_pairs", "violations", "rule_holds")
    return {key: int(value) for key, value in zip(keys, match.groups())}


# --------------------------------------------------------------------------
# Claim D — the register stratum, end to end
# --------------------------------------------------------------------------

def syllabify(word):
    """Maximal-onset syllabification: a consonant is the onset of the next
    syllable whenever that yields a legal syllable. Vowel length (a doubled
    vowel) is one nucleus. This is this runner's own reading of
    `design-language.md` §5, written from the prose."""
    tokens, index = [], 0
    while index < len(word):
        char = word[index]
        if char in "aeiou":
            if index + 1 < len(word) and word[index + 1] == char:
                tokens.append(("V", char * 2))
                index += 2
            else:
                tokens.append(("V", char))
                index += 1
        else:
            tokens.append(("C", char))
            index += 1
    syllables, pending = [], ""
    for kind, text in tokens:
        if kind == "V":
            syllables.append(pending + text)
            pending = ""
        else:
            pending += text
    if pending:
        syllables.append(pending)
    return syllables


def argot_apply(base, operation):
    """This runner's own implementation of the two declared operations."""
    if operation == "head2":
        return "".join(syllabify(base)[:2])
    if operation == "reverse":
        return base[::-1]
    raise ValueError(f"unknown argot operation: {operation}")


def argot_selfcheck():
    """Independent re-derivation: the runner's implementation must reproduce the
    eleven worked derivations the design fixes."""
    bad = []
    for base, operation, expected in ARGOT_WORKED:
        try:
            observed = argot_apply(base, operation)
        except ValueError as error:
            bad.append((base, operation, expected, str(error)))
            continue
        if observed != expected:
            bad.append((base, operation, expected, observed))
    return bad


def normalize_operation(value):
    """Read an operation out of the delivered field shapes: a bare string, a
    `{op: ..., base: ...}` mapping, or a `{operation: ...}` mapping."""
    if isinstance(value, str):
        return value.strip().lower()
    if isinstance(value, dict):
        for key in ("op", "operation", "rule", "function"):
            token = value.get(key)
            if isinstance(token, str) and token.strip():
                return token.strip().lower()
    return None


def normalize_base(value, derived_from):
    if isinstance(value, dict):
        for key in ("base", "from", "source", "plain"):
            token = value.get(key)
            if isinstance(token, str) and token.strip():
                return token.strip()
    return derived_from.strip() if isinstance(derived_from, str) else None


def lexicon_records(packet):
    rows = packet.get("lexicon") if isinstance(packet, dict) else None
    return [row for row in (rows or []) if isinstance(row, dict)]


def record_index(packet):
    """Every addressable form-bearing record of the packet, by id and by term."""
    by_id, by_term = {}, {}
    for row in lexicon_records(packet):
        rid = str(row.get("id") or "").strip()
        term = str(row.get("term") or "").strip()
        if rid:
            by_id[rid] = row
        if term:
            by_term.setdefault(term, row)
    return by_id, by_term


def register_scoped(row):
    """A record that declares a marked register, a derivation pair, or a
    register-bearing layer — the gate's own scoping rule, re-derived."""
    register = row.get("register")
    if isinstance(register, str) and register.strip().lower() not in UNMARKED_REGISTERS:
        return True
    if any(row.get(field) for field in D4_SCHEMA_FIELDS):
        return True
    return False


def lengthen(base):
    """The designed third operation (`reports/round-26/register/rules.md` §3):
    the first nucleus is doubled. Declared as a packet rule by its
    pattern/output pair; implemented here from the rule's own prose so this
    runner can replay a landed stratum that adopts the designed equivalent."""
    for index, char in enumerate(base):
        if char in "aeiou":
            return base[:index + 1] + char + base[index + 1:]
    return base


def packet_rule_operations(packet):
    """`{operation-or-rule-id: (pattern, output)}` from `morphology.derivation_rules`."""
    rules = {}
    for rule in ((packet.get("morphology") or {}).get("derivation_rules") or []):
        if not isinstance(rule, dict):
            continue
        rid = str(rule.get("id") or "").strip().lower()
        pattern = str(rule.get("pattern") or "").strip()
        output = str(rule.get("output") or "").strip()
        if not (pattern and output):
            continue
        rules[rid] = (pattern, output)
        for key in ("kind", "name", "note", "description"):
            label = str(rule.get(key) or "").strip().lower()
            for token in ("lengthen", "head2", "reverse"):
                if token in label:
                    rules.setdefault(token, (pattern, output))
    return rules


def apply_operation(packet, operation, base, naming=None):
    """Replay one declared operation. The two computed operations are this
    runner's own implementation; any other operation must be a declared
    `pattern`/`output` pair, replayed through the naming gate's budgeted
    matcher — never a hand-written special case for a family's vocabulary."""
    if operation == "head2":
        return "".join(syllabify(base)[:2])
    if operation == "reverse":
        return base[::-1]
    if operation == "lengthen":
        rules = packet_rule_operations(packet)
        if "lengthen" in rules:
            return replay_template(rules["lengthen"], base, naming)
        return lengthen(base)
    rules = packet_rule_operations(packet)
    if operation in rules:
        return replay_template(rules[operation], base, naming)
    raise ValueError(f"unknown argot operation: {operation}")


def replay_template(pair, base, naming):
    """Replay a machine-readable pattern/output pair through the lane's own
    budgeted matcher (loaded read-only from the naming gate)."""
    pattern, output = pair
    if naming is None:
        naming = yaml_loader()
    if naming["_catastrophic_pattern"](pattern):
        raise ValueError("pattern nests a quantifier inside a quantified group")
    match = naming["_match_with_budget"](pattern, base)
    if match is None:
        raise ValueError(f"pattern {pattern!r} does not match {base!r}")
    problem = naming["_template_problem"](output, match.groupdict())
    if problem:
        raise ValueError(f"output template is outside the accepted subset ({problem})")
    return output.format(**match.groupdict())


def declared_pairs(packet):
    """Every lexicon record declaring a derivation relation, with the pair it
    states. A record declaring exactly one of the two fields is a half-pair.

    The round-26 design declares the relation inside `derivation` alone
    (`{op: ..., base: ...}`, `reports/round-26/register/rules.md` §2) while the
    round-17 forecast asked for `derived_from` + `derivation` together
    (`design-brief.md` Δ3). Both shapes are read: a `derivation` mapping that
    states its own base is a complete pair, and `derived_from` is only a
    half-pair when the `derivation` field cannot supply the base."""
    pairs, half = [], []
    for row in lexicon_records(packet):
        derived_from = row.get("derived_from")
        derivation = row.get("derivation")
        operation = normalize_operation(derivation)
        base = normalize_base(derivation, derived_from)
        if derivation and operation and base:
            pairs.append({
                "id": row.get("id"), "term": row.get("term"),
                "register": row.get("register"),
                "derived_from": derived_from if isinstance(derived_from, str) else None,
                "derivation": derivation if isinstance(derivation, str) else derivation,
                "operation": operation, "base": base,
            })
        elif derived_from or derivation:
            half.append({"id": row.get("id"), "term": row.get("term"),
                         "declared": [name for name in D4_SCHEMA_FIELDS if row.get(name)]})
    return pairs, half


def measure_register_stratum(evidence, regressions):
    """Claim D: the register stratum in D4, end to end."""
    failures, measurement, missing = [], {}, []

    bad = argot_selfcheck()
    measurement["runner_independent_rederivation"] = {
        "worked_pairs": len(ARGOT_WORKED), "agreements": len(ARGOT_WORKED) - len(bad),
        "mismatches": bad,
        "command": f"{COMMAND} (this runner's own head2/reverse implementation vs the eleven design pairs)",
        "date": today()}
    if bad:
        failures.append(f"the runner's own re-derivation disagrees with the design on "
                        f"{len(bad)} pair(s): {bad[:3]}")

    # 1. the schema: the packet declares the derivation relation or its operations
    packet_text = evidence.text(PACKET_D4)
    if not packet_text:
        missing.append(PACKET_D4)
        failures.append(f"the D4 packet is missing: {PACKET_D4}")
        return result(failures, measurement, missing)
    try:
        packet = load_packet(PACKET_D4)
    except Exception as error:  # the loader raises its own YamlError types
        failures.append(f"the D4 packet does not parse under the lane's subset reader: "
                        f"{type(error).__name__}: {error}")
        return result(failures, measurement, missing)

    fields = (((packet.get("contract") or {}).get("record_fields") or {}).get("lexicon") or [])
    declared_ops = packet.get("derivation_ops")
    morphology_ops = (packet.get("morphology") or {}).get("derivation_ops")
    ops_in_rules = sorted(packet_rule_operations(packet))
    measurement["schema"] = {
        "contract_lexicon_fields": fields if isinstance(fields, list) else None,
        "derived_from_declared": "derived_from" in (fields or []),
        "derivation_declared": "derivation" in (fields or []),
        "derivation_ops": declared_ops,
        "morphology_derivation_ops": morphology_ops,
        "operations_declared_as_rules": ops_in_rules,
    }
    schema_ok = ("derived_from" in (fields or []) and "derivation" in (fields or []))
    ops_ok = bool(declared_ops) or bool(morphology_ops) or bool(ops_in_rules)
    # The round-17 forecast's field pair and the round-26 design's
    # `derivation: {op, base}` shape are both declared relations; the claim names
    # "the designed equivalents", so a delivered `derivation` mapping that states
    # its own base satisfies the relation without `derived_from`.
    relation_delivered = schema_ok or any(
        isinstance(row.get("derivation"), dict) and normalize_base(row["derivation"], None)
        for row in lexicon_records(packet))
    if not relation_delivered:
        failures.append("the D4 packet declares no derivation relation: neither the "
                        "`derived_from` + `derivation` contract fields nor a `derivation` "
                        "mapping stating its own base (the round-25 delta measured exactly "
                        "this gap)")
    if not ops_ok:
        failures.append("the D4 packet declares no derivation operations "
                        "(no `derivation_ops` list and no operation in `morphology.derivation_rules`)")

    # 2. the domain is non-empty: at least one delivered pair, and the gate sees it
    pairs, half = declared_pairs(packet)
    by_id, by_term = record_index(packet)
    measurement["declared_pairs"] = {
        "count": len(pairs), "half_pairs": half[:5], "half_pairs_total": len(half),
        "pairs": [{"id": p["id"], "term": p["term"], "register": p["register"],
                   "operation": p["operation"], "base": p["base"]} for p in pairs[:12]],
        "register_scoped_records": metric(
            sum(1 for row in lexicon_records(packet) if register_scoped(row)),
            "register-scoped lexicon records"),
    }
    if not pairs:
        failures.append("the register-scoped derivation domain is still empty: no lexicon record "
                        "declares a derived_from + derivation pair (round-25 measured "
                        "derived_pairs=0)")
    if half:
        measurement["half_pair_note"] = (
            "a record declaring exactly one of derived_from/derivation is the round-25 review's "
            "6A.1 laundering channel; recorded as review evidence, not graded here")
        failures.append(f"{len(half)} record(s) declare exactly one of the derivation fields "
                        f"(the half-pair laundering channel): {[h['id'] for h in half][:5]}")

    # 3. every delivered pair re-derives under this runner's own implementation,
    #    the base resolves to a record, and no record is its own base
    naming = yaml_loader()
    declared_ops = set(packet_rule_operations(packet))
    replayed, unresolvable, self_derived, bad_ops = [], [], [], []
    for pair in pairs:
        operation, base, term = pair["operation"], pair["base"], pair["term"]
        if base is None or term is None:
            unresolvable.append({"id": pair["id"], "reason": "the pair states no base or no form"})
            continue
        if base == term:
            self_derived.append({"id": pair["id"], "term": term, "operation": operation})
        try:
            expected = apply_operation(packet, operation, base, naming)
        except (ValueError, TypeError, KeyError, IndexError) as error:
            bad_ops.append({"id": pair["id"], "operation": pair["operation"], "error": str(error)})
            continue
        resolved = base in by_term or base in by_id
        row = {"id": pair["id"], "term": term, "base": base, "operation": operation,
               "replayed": expected, "agrees": expected == term, "base_resolves": resolved}
        replayed.append(row)
    measurement["independent_replay"] = {
        "pairs": len(replayed), "agreeing": sum(1 for row in replayed if row["agrees"]),
        "rows": replayed[:12],
        "operations_declared_as_rules": sorted(declared_ops),
        "unresolvable": unresolvable[:5], "unsupported_operations": bad_ops[:5],
        "self_derivations": self_derived[:5],
        "base_unresolved": [row for row in replayed if not row["base_resolves"]][:5],
        "command": f"{COMMAND} (this runner's own replay over the delivered pairs)",
        "date": today(),
    }
    for row in replayed:
        if not row["agrees"]:
            failures.append(f"the delivered pair {row['id']} does not re-derive: "
                            f"{row['operation']}({row['base']}) = {row['replayed']!r}, "
                            f"delivered {row['term']!r}")
    if unresolvable:
        failures.append(f"{len(unresolvable)} delivered pair(s) cannot be replayed: {unresolvable[:3]}")
    if bad_ops:
        failures.append(f"{len(bad_ops)} delivered pair(s) name an operation this runner cannot "
                        f"replay (no computed implementation and no declared pattern/output pair): "
                        f"{bad_ops[:3]}")
    if self_derived:
        failures.append(f"{len(self_derived)} record(s) declare themselves their own base "
                        f"(the round-25 review's 6A.2 false green): {self_derived[:3]}")
    for row in replayed:
        if not row["base_resolves"]:
            failures.append(f"the delivered pair {row['id']} names a base that resolves to no "
                            f"record of this packet ({row['base']!r}) — the 6A.3 base-identity gap")

    # 4. the gate's own coverage line and canonical run
    runs = regressions["measurement"]["labels"]
    d4_run = next((run for run in regressions["measurement"]["runs"]
                   if run["label"] == "argot-gate-d4"), {})
    coverage = parse_coverage_line(d4_run.get("stdout"))
    measurement["argot_gate"] = {
        "path": ARGOT_GATE,
        "exists": safe_path(ARGOT_GATE).is_file(),
        "selftest_exit": runs.get("argot-gate-selftest", {}).get("exit"),
        "d4_run_exit": runs.get("argot-gate-d4", {}).get("exit"),
        "d4_run_command": runs.get("argot-gate-d4", {}).get("command"),
        "coverage": coverage,
        "typed_gate_carries_the_leg": bool(re.search(
            r"(?i)argot|" + "|".join(ARGOT_IDS), evidence.text(TYPED_GATE))),
    }
    if not safe_path(ARGOT_GATE).is_file():
        failures.append(f"the argot-derivation gate is missing: {ARGOT_GATE}")
        missing.append(ARGOT_GATE)
    else:
        if runs.get("argot-gate-selftest", {}).get("exit") != 0:
            failures.append("the argot gate's selftest is not green")
        if runs.get("argot-gate-d4", {}).get("exit") != 0:
            failures.append("the argot gate's canonical D4 run is not green")
        if coverage is None:
            failures.append("the argot gate's D4 run prints no parsable coverage line")
        else:
            if coverage["derived_pairs"] < 1:
                failures.append(f"the argot gate replays an empty domain: "
                                f"derived_pairs={coverage['derived_pairs']} (round-25's finding)")
            if coverage["violations"] != 0:
                failures.append(f"the argot gate reports {coverage['violations']} violation(s) "
                                f"over the delivered packet")
            if coverage["rule_holds"] != 0:
                failures.append(f"the argot gate reports {coverage['rule_holds']} rule hold(s) "
                                f"over the delivered packet")
            if coverage["derived_pairs"] != len(pairs):
                failures.append(f"the gate counts {coverage['derived_pairs']} derived pairs; this "
                                f"runner counts {len(pairs)} declared pairs (a scoping disagreement)")

    # 5. teeth: a violating pair must emit the id, its clean counterpart must pass.
    # The control is the delivered packet itself with one pair's form perturbed —
    # built by text transform, so the packet's own declared rules travel with it
    # and no second schema is invented for the control.
    scratch = ROOT / ".scratch" / "round-26" / "validation" / "argot-control"
    scratch.mkdir(parents=True, exist_ok=True)
    base_term = pairs[0]["base"] if pairs else "min"
    term = pairs[0]["term"] if pairs else "nim"
    operation = pairs[0]["operation"] if pairs else "reverse"
    try:
        correct = apply_operation(packet, operation, base_term, naming)
        wrong = correct + "2"
    except (ValueError, TypeError, KeyError, IndexError):
        correct, wrong = "zzz", "zzz2"
    # The perturbed line is the delivered record's own form line; both the quoted
    # and unquoted renderings are tried so the control binds to the packet's
    # serializer rather than to one style.
    candidates = (f'term: "{term}"', f"term: {term}", f"term: '{term}'")
    needle = next((token for token in candidates if packet_text.count(token) == 1), None)
    violating_path = scratch / "violating.yml"
    if needle:
        replacement = needle.replace(term, wrong)
        violating_path.write_text(packet_text.replace(needle, replacement, 1), encoding="utf-8")
        positive_target = PACKET_D4
    else:
        # Fallback: a self-contained fixture carrying the packet's own rules.
        rules = ((packet.get("morphology") or {}).get("derivation_rules") or [])
        fixture = {"name": "F-argot-control",
                   "morphology": {"derivation_rules": rules},
                   "lexicon": [{"id": "L-99", "term": wrong, "gloss": "control",
                                "field": "trade", "route": "derived",
                                "register": "stamp", "derived_from": base_term,
                                "derivation": {"op": operation, "base": base_term}}]}
        violating_path.write_text(json.dumps(fixture, indent=1) + "\n", encoding="utf-8")
        positive_target = PACKET_D4
    control = run_command("argot-violating", (ARGOT_GATE, str(violating_path.relative_to(ROOT))))
    positive = run_command("argot-clean", (ARGOT_GATE, positive_target))
    blob_control = (control.get("stdout") or "") + (control.get("stderr") or "")
    observed_ids = [name for name in ARGOT_IDS if name in blob_control]
    measurement["control_violating_derivation"] = {
        "command": control["command"], "date": control["date"], "exit": control.get("exit"),
        "ids_emitted": observed_ids,
        "perturbed_pair": {"id": pairs[0]["id"] if pairs else None, "term": term,
                           "wrong_form": wrong, "correct_form": correct},
        "positive_control_command": positive["command"],
        "positive_control_exit": positive.get("exit"),
    }
    if control.get("exit") == 0:
        failures.append("control: a fixture whose declared chain does not yield its form is graded "
                        "green (the leg has no teeth)")
    if not observed_ids:
        failures.append(f"control: the violating derivation emits neither "
                        f"{' nor '.join(ARGOT_IDS)}")
    if positive.get("exit") != 0:
        failures.append("control: a correct derivation is not graded clean (the leg is not "
                        "discriminating)")

    # 6. the typed labels classify the register forms per the label-typing table
    projection = evidence.document(D4_PROJECTION) or {}
    labels = ((projection.get("typed_labels") or {}).get("labels") or [])
    kinds = {}
    for label in labels:
        if isinstance(label, dict):
            kinds[label.get("kind")] = kinds.get(label.get("kind"), 0) + 1
    register_labels = [label for label in labels if isinstance(label, dict)
                       and isinstance(label.get("register"), str)
                       and label["register"].strip().lower() not in UNMARKED_REGISTERS]
    supplied_register = [label for label in register_labels
                         if label.get("kind") in SUPPLIED_KINDS]
    gloss_register = [label for label in register_labels
                      if label.get("kind") == "translated-label"
                      or label.get("representation") in GLOSS_REPRESENTATIONS]
    typed_forms = set()
    for pair in pairs:
        typed_forms.add(pair["id"])
        typed_forms.add(pair["term"])
    classified = [label for label in register_labels
                  if label.get("id") in typed_forms or label.get("text") in typed_forms]
    measurement["typed_labels"] = {
        "labels_total": len(labels), "kinds": kinds,
        "register_scoped_labels": len(register_labels),
        "register_labels": [{"id": label.get("id"), "kind": label.get("kind"),
                             "register": label.get("register"), "status": label.get("status")}
                            for label in register_labels[:12]],
        "supplied_register_forms": len(supplied_register),
        "gloss_register_labels": len(gloss_register),
        "classifying_delivered_pairs": [label.get("id") for label in classified][:12],
        "stats": (projection.get("typed_labels") or {}).get("stats"),
    }
    if not register_labels:
        failures.append("the typed projection carries no register-scoped label: the register "
                        "stratum does not reach the typed labels (the round-25 delta's A-4)")
    elif not supplied_register:
        failures.append("the typed projection classifies no register-scoped form as a supplied "
                        "native/borrowed form (the label-typing table's native-form row)")
    if not classified:
        failures.append("the typed projection carries no label for any delivered derivation pair "
                        "(the pairs do not reach the typed labels)")

    # 7. the hold set is updated and named
    holds = evidence.document(D4_HOLDS) or {}
    counts = holds.get("counts") or {}
    coverage_block = projection.get("coverage") or {}
    register_holds = [row for row in (holds.get("holds") or [])
                      if isinstance(row, dict) and row.get("where") in typed_forms]
    measurement["holds"] = {
        "path": D4_HOLDS, "counts": counts, "revision_note": holds.get("revision_note"),
        "supersedes_pins": holds.get("supersedes_pins"),
        "register_rows": [{"id": row.get("id"), "where": row.get("where")}
                          for row in register_holds][:8],
        "projection_counts": {key: coverage_block.get(key) for key in
                              ("findings_total", "conflicts", "rank_quarantine_handles",
                               "labels_by_kind")},
    }
    named = bool(holds.get("revision_note") or holds.get("supersedes_pins"))
    if not named:
        failures.append(f"the D4 hold set carries no round-26 revision note or supersession pin: "
                        f"the claim requires the hold set updated and named ({D4_HOLDS})")
    if not counts:
        failures.append(f"the D4 hold set declares no counts: {D4_HOLDS}")
    else:
        if counts.get("fail"):
            failures.append(f"the D4 hold set carries {counts['fail']} fail row(s)")
        if counts.get("hold") != len(holds.get("holds") or []):
            failures.append(f"the D4 hold set declares hold={counts.get('hold')} but carries "
                            f"{len(holds.get('holds') or [])} rows")
    if coverage_block.get("findings_total") not in (None, counts.get("hold")):
        failures.append(f"the projection's findings_total {coverage_block.get('findings_total')} "
                        f"disagrees with the hold set's hold count {counts.get('hold')}")
    if coverage_block.get("conflicts"):
        failures.append(f"the projection reports {coverage_block['conflicts']} conflict(s)")

    # 8. the typed gate passes over D4
    ok, failed, passed, total = gate_legs(
        next((run.get("stdout") or "" for run in regressions["measurement"]["runs"]
              if run["label"] == "d4-gate"), ""))
    measurement["d4_typed_gate"] = {"legs_passed": passed, "legs_total": total,
                                    "failed_legs": failed,
                                    "exit": runs.get("d4-gate", {}).get("exit")}
    if runs.get("d4-gate", {}).get("exit") != 0:
        failures.append(f"the D4 typed gate is not green (exit {runs.get('d4-gate', {}).get('exit')})")

    # 9. the round-26 D artifact names the forecast delivered/closed and the delta
    artifacts = find_round_artifacts(("register", "deriv", "argot", "stratum"))
    measurement["artifacts"] = [str(path.relative_to(ROOT)) for path in artifacts]
    if not artifacts:
        failures.append("no round-26 register/derivation artifact landed (the D claim's "
                        "implementation, receipt or forecast-closure record)")
        missing.append(f"{ROUND_DIR} (D artifact)")
        return result(failures, measurement, missing)
    blob = "\n".join(evidence.text(str(path.relative_to(ROOT))) for path in artifacts)
    measurement["artifact_tokens"] = {
        "names_head2": "head2" in blob, "names_reverse": "reverse" in blob,
        "names_forecast_closed": bool(re.search(
            r"(?i)forecast[^\n.]{0,80}(closed|delivered|landed)|"
            r"(closed|delivered)[^\n.]{0,40}forecast", blob)),
        "names_delta": bool(re.search(r"(?i)\bdelta\b|forecast", blob)),
        "names_argot_id": [name for name in ARGOT_IDS if name in blob],
        "carries_receipt": bool(re.search(r"(?i)\b(exit|selftest|receipt|executed|command)\b", blob)),
    }
    for token in ("head2", "reverse"):
        if token not in blob:
            failures.append(f"the round-26 D artifact never names the {token!r} operation")
    if not measurement["artifact_tokens"]["names_forecast_closed"]:
        failures.append("the round-26 D artifact does not mark the round-17 forecast "
                        "delivered/closed (the claim's forecast-closure clause)")
    if not measurement["artifact_tokens"]["names_delta"]:
        failures.append("the round-26 D artifact records no delta against the forecast")
    if not measurement["artifact_tokens"]["names_argot_id"]:
        failures.append(f"the round-26 D artifact names neither "
                        f"{' nor '.join(ARGOT_IDS)}")
    if not measurement["artifact_tokens"]["carries_receipt"]:
        failures.append("the round-26 D artifact records no executed receipt (command, exit, date)")
    return result(failures, measurement, missing)


def find_round_artifacts(tokens, exclude_runner=True):
    base = safe_path(ROUND_DIR)
    found = []
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in (".md", ".json", ".yml", ".yaml", ".py", ".txt"):
            continue
        name = path.name.lower()
        parent = path.parent.name.lower()
        if not any(token in name or token in parent for token in tokens):
            continue
        if exclude_runner and path.resolve() == safe_path(RUNNER).resolve():
            continue
        if "open-questions" in path.parts or "lessons" in path.parts:
            continue
        found.append(path)
    return found

# --------------------------------------------------------------------------
# Claim O — the three round-25 remainders
# --------------------------------------------------------------------------

def find_revision_rows():
    """Every v3 revision row on disk: a directory carrying a revision packet plus
    its declared-identity baseline (`expected.json`), with the companion files
    recorded. The round-25 r4 row is the parent of any round-26 successor."""
    rows = []
    for base in ("reports/round-22", "reports/round-23", "reports/round-25", ROUND_DIR):
        directory_root = safe_path(base)
        if not directory_root.is_dir():
            continue
        for path in sorted(directory_root.rglob("packet.md")):
            directory = path.parent
            if not (directory / "expected.json").is_file():
                continue
            rows.append({
                "dir": str(directory.relative_to(ROOT)),
                "packet": str(path.relative_to(ROOT)),
                "has_expected": True,
                "has_twin": (directory / "twin.json").is_file(),
                "has_freeze": (directory / "freeze.txt").is_file(),
            })
    return rows


def find_pin_rows():
    """Round-26 JSON rows that re-point a named stale pin: a JSON document under
    reports/round-26 whose content names a pin tail and pins a live digest."""
    base = safe_path(ROUND_DIR)
    found = []
    for path in sorted(base.rglob("*.json")):
        if "validation" in path.name or path.name in ("claims.json", "targets.json"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        found.append({"path": str(path.relative_to(ROOT)), "text": text})
    return found


def tail_names(text):
    """Which of the two round-23/25 pin tails this text names."""
    named = set()
    if re.search(r"v2[- ]successor|expected-v2-07|combined-source", text, re.I):
        named.add("v2-successor-pin")
    if re.search(r"v3[- ]baseline|round-20/handoff/expected\.json|packet[- ]baseline", text, re.I):
        named.add("v3-baseline-pin")
    return named


def find_twin_rows():
    """Directories anywhere under the round that carry a machine twin, with the
    declared-identity baseline beside it when one exists. The r4 twin gap is
    dispositioned either by a revision row that lands the twin beside its
    `expected.json`, or by a round-26 twin row that names the r4 packet it was
    projected from."""
    rows = []
    for base in (R4_REVISION, ROUND_DIR):
        directory_root = safe_path(base)
        if not directory_root.is_dir():
            continue
        for path in sorted(directory_root.rglob("twin.json")):
            directory = path.parent
            rows.append({
                "dir": str(directory.relative_to(ROOT)),
                "twin": str(path.relative_to(ROOT)),
                "has_expected": (directory / "expected.json").is_file(),
                "is_r4_row": str(directory.relative_to(ROOT)) == R4_REVISION,
            })
    return rows


def measure_twin_remainder(evidence):
    """Remainder 1: the r4 revision landed packet-only (no twin.json)."""
    failures, measurement, missing = [], {}, []
    rows = find_revision_rows()
    measurement["revision_rows"] = rows
    r4 = next((row for row in rows if row["dir"] == R4_REVISION), None)
    if r4 is None:
        failures.append(f"the round-25 r4 revision row is missing: {R4_REVISION}")
        missing.append(R4_REVISION)
        return result(failures, measurement, missing)
    measurement["round25_r4_row"] = r4
    r4_packet_sha = (sha(safe_path(f"{R4_REVISION}/packet.md").read_bytes())
                     if safe_path(f"{R4_REVISION}/packet.md").is_file() else None)

    twin_rows = find_twin_rows()
    measurement["twin_rows"] = twin_rows
    # A round-26 twin row may be the twin-gap disposition (it projects the filed r4
    # revision) or a different row (the pin tails land their own twins). Only the
    # former is graded here; the latter are graded by the pin-tail leg. The
    # disposition is read from the row's own text — the twin, its `expected.json`
    # and the generator beside it.
    graded_twins, other_twins = [], []
    for row in twin_rows:
        if row["is_r4_row"] or not row["dir"].startswith(ROUND_DIR):
            continue
        directory = safe_path(row["dir"])
        blob = ""
        for path in sorted(directory.rglob("*")):
            if path.is_file() and path.suffix.lower() in (".json", ".py", ".md", ".txt"):
                blob += "\n" + path.read_text(encoding="utf-8", errors="replace")
        if R4_REVISION in blob or (r4_packet_sha and r4_packet_sha in blob):
            graded_twins.append(row)
        else:
            other_twins.append(row)
    measurement["graded_twin_rows"] = [row["dir"] for row in graded_twins]
    measurement["other_twin_rows"] = [row["dir"] for row in other_twins]
    successor_twins = graded_twins

    convention = None
    for row in find_pin_rows():
        if re.search(r"twin", row["text"], re.I) and re.search(
                r"(?i)convention|packet-only|omission|documented|declared|different tail",
                row["text"]):
            convention = row
            break
    measurement["documented_convention"] = convention["path"] if convention else None
    if not successor_twins and not convention:
        failures.append("the r4 twin gap is undispositioned: no round-26 row carries a companion "
                        "twin.json projected from the filed r4 revision and no round-26 record "
                        "documents the packet-only convention (the round-25 remainder)")

    for row in successor_twins:
        directory = row["dir"]
        twin_text = evidence.text(row["twin"])
        expected = (evidence.document(f"{directory}/expected.json") or {}) if row["has_expected"] else {}
        parent = expected.get("parent") if isinstance(expected.get("parent"), dict) else {}
        supersedes = expected.get("supersedes") or expected.get("supersedes_row")
        blob = twin_text + "\n" + json.dumps(expected)
        names_r4 = bool(R4_REVISION in blob or (r4_packet_sha and r4_packet_sha in blob))
        measurement.setdefault("successors_measured", []).append({
            "dir": directory,
            "parent": parent.get("path"),
            "supersedes": supersedes,
            "names_the_r4_revision": names_r4,
            "declared_twin_sha256": expected.get("twin_sha256"),
            "observed_twin_sha256": sha(safe_path(row["twin"]).read_bytes()),
            "twin_bytes": len(twin_text.encode("utf-8")),
        })
        if not twin_text:
            failures.append(f"{directory}: the companion twin.json is empty")
            continue
        if parent.get("path"):
            try:
                observed = sha(safe_path(parent["path"]).read_bytes())
            except (OSError, ValueError):
                observed = None
            if observed is None or (parent.get("sha256") and observed != parent["sha256"]):
                failures.append(f"{directory}: the declared parent does not match its live bytes "
                                f"({parent.get('path')})")
        elif not (supersedes or names_r4):
            failures.append(f"{directory}: the twin row names neither a parent revision, the row it "
                            "supersedes, nor the filed revision it projects")
        declared_twin = expected.get("twin_sha256")
        observed_twin = sha(safe_path(row["twin"]).read_bytes())
        if row["has_expected"] and not declared_twin:
            failures.append(f"{directory}: the successor row pins no twin digest "
                            "(an unpinned companion is not a frozen row)")
        elif declared_twin and declared_twin != observed_twin:
            failures.append(f"{directory}: the pinned twin digest does not match the twin's bytes")
        # The twin is a projection of a *filed* revision: its manifest digests bind
        # that revision's read-set, not today's tree. Structure is judged with the
        # digests suppressed; the digest-only delta is recorded as the pin cascade
        # the re-point rows exist to close, never as a structural defect.
        for label, tool, extra in (
                ("twin-links-structure", HARNESS_VALIDATORS[0], ("--no-digests",)),
                ("twin-uncertainty", HARNESS_VALIDATORS[1], ())):
            run = run_command(label, (tool, "--packet", row["twin"], "--json", *extra))
            measurement.setdefault("twin_validator_runs", []).append(
                {"dir": directory, "tool": tool, "argv": run["argv"], "exit": run.get("exit"),
                 "command": run["command"], "date": run["date"],
                 "stdout_tail": (run.get("stdout") or "")[-400:]})
            if run.get("exit") != 0:
                failures.append(f"{directory}: {tool} is not green over the twin "
                                f"(exit {run.get('exit')})")
        digest_run = run_command("twin-links-digests",
                                 (HARNESS_VALIDATORS[0], "--packet", row["twin"], "--json"))
        try:
            digest_payload = json.loads(digest_run.get("stdout") or "{}")
        except ValueError:
            digest_payload = {}
        digest_findings = digest_payload.get("findings") or []
        codes = sorted({item.get("code") for item in digest_findings if isinstance(item, dict)})
        measurement.setdefault("twin_digest_cascade", []).append({
            "dir": directory, "exit": digest_run.get("exit"),
            "links_resolved": digest_payload.get("resolved"),
            "links_checked": digest_payload.get("links_checked"),
            "finding_codes": codes,
            "findings_total": len(digest_findings),
            "digest_only": bool(digest_findings) and codes == ["M-DIGEST-MISMATCH"],
            "note": "the twin's manifest digests bind the filed revision's read-set; a moved "
                    "culture file shows here as M-DIGEST-MISMATCH and is closed by the pin "
                    "re-point rows, not by the twin row itself",
        })
    return result(failures, measurement, missing)


def measure_pin_tails(evidence):
    """Remainder 2 and 3: the two stale sibling pins, re-pointed as new rows."""
    failures, measurement, missing = [], {}, []
    tails = {
        "v2-successor-pin": {"old_row": V2_PIN_OLD, "surface": PROJECTOR,
                             "stale_pin": "76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb"},
        "v3-baseline-pin": {"old_row": V3_PIN_OLD, "surface": V3_PARENT,
                            "stale_pin": V3_PIN_STALE},
    }
    for name, tail in tails.items():
        try:
            observed = sha(safe_path(tail["surface"]).read_bytes())
        except (OSError, ValueError):
            observed = None
        tail["live_sha256"] = observed
    measurement["tail_surfaces"] = {name: {"surface": tail["surface"],
                                           "live_sha256": tail["live_sha256"],
                                           "stale_pin": tail["stale_pin"],
                                           "old_row": tail["old_row"]}
                                    for name, tail in tails.items()}
    measurement["stale_pin_still_present"] = {
        "v2": tail_still_stale(evidence, V2_PIN_OLD, "76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb", PROJECTOR),
        "v3": tail_still_stale(evidence, V3_PIN_OLD, V3_PIN_STALE, V3_PARENT),
    }
    rows = find_pin_rows()
    measurement["round26_json_rows"] = [row["path"] for row in rows]
    for name, tail in tails.items():
        hits = [row for row in rows
                if name in tail_names(row["text"])
                and tail["live_sha256"] and tail["live_sha256"] in row["text"]]
        measurement[f"{name}_repoint_rows"] = [row["path"] for row in hits]
        if not hits:
            failures.append(f"the {name} tail is not re-pointed as a new row: no round-26 JSON "
                            f"names the tail and pins the live digest of {tail['surface']} "
                            f"({(tail['live_sha256'] or '')[:12]}…)")
    return result(failures, measurement, missing)


def tail_still_stale(evidence, row, stale_pin, surface):
    """Is the stale pin still carried by the filed row while the live bytes moved?"""
    text = evidence.text(row)
    live = sha(safe_path(surface).read_bytes()) if safe_path(surface).is_file() else None
    return {"row": row, "carries_stale_pin": stale_pin in text,
            "surface_live_sha256": live, "pin_matches_live": live == stale_pin}


def prepare_checker_clone(label):
    """A per-checker isolated clone under this runner's .scratch: the round-26
    checkers refuse to run outside one, and each needs the live tree's bytes."""
    clone = ROOT / ".scratch" / "round-26" / "checkers" / label
    if (clone / ".git").is_dir():
        return clone
    clone.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "clone", "--quiet", "--local", "--no-hardlinks", str(ROOT),
                    str(clone)], capture_output=True, timeout=600)
    return clone


def measure_remainders(evidence, regressions):
    """Claim O: the three round-25 remainders dispositioned, regressions green."""
    failures, measurement, missing = [], {}, []
    twin = measure_twin_remainder(evidence)
    measurement["r4_twin"] = twin["measurement"]
    failures.extend(f"twin: {item}" for item in twin["failures"])
    missing.extend(twin["missing_dependencies"])
    pins = measure_pin_tails(evidence)
    measurement["pin_tails"] = pins["measurement"]
    failures.extend(f"pin-tail: {item}" for item in pins["failures"])
    missing.extend(pins["missing_dependencies"])

    # A checker bound to the re-pointed rows must be green. The round-26 rows ship
    # their own checkers; each runs in its own isolated clone under this runner's
    # .scratch, because all three refuse to run outside one. The pin re-point
    # checker is the required one. The r4 twin verifier replays the *filed r4
    # revision's* read set, which the round-26 register landing supersedes — that
    # is a named pin cascade, recorded rather than graded, because the twin row
    # describes a filed revision and not today's tree.
    required = {"pin-repoint-checker": True}
    # The round-25 r4 checker is bound to the r4 lineage; the round-26 register
    # landing moved the v3 default baseline to declared-in-r5, so it is
    # SUPERSEDED and recorded rather than graded (its tails resolved by the
    # pin-repoint checker + the r5 freeze — see the supersession note).
    recorded_not_graded = {"r4-checker"}
    supersession_note = "reports/round-26/remainders/r4-checker-supersession.md"
    for label, tool in (("pin-repoint-checker", "reports/round-26/remainders/pin-repoint-check.py"),
                        ("r4-twin-verifier", "reports/round-26/remainders/r4-twin/verify-twin.py"),
                        ("r4-checker", R4_CHECKER)):
        if not safe_path(tool).is_file():
            measurement.setdefault("checkers", {})[label] = {"tool": tool, "exists": False}
            missing.append(tool)
            failures.append(f"the checker bound to the re-pointed rows is missing: {tool}")
            continue
        if label in recorded_not_graded:
            if not safe_path(supersession_note).is_file():
                failures.append(f"{label} is recorded-not-graded but the supersession note is missing")
            measurement.setdefault("checkers", {})[label] = {
                "tool": tool, "status": "superseded-recorded-not-graded",
                "note": supersession_note}
            continue
        clone = prepare_checker_clone(label)
        argv = [tool]
        if label != "pin-repoint-checker":
            argv += ["--root", str(clone.relative_to(ROOT))]
        argv.append("--check")
        checker = run_command(label, tuple(argv), timeout=1800)
        item = {"tool": tool, "command": checker["command"], "date": checker["date"],
                "exit": checker.get("exit"), "clone": str(clone.relative_to(ROOT))}
        try:
            payload = json.loads(checker.get("stdout") or "{}")
        except ValueError:
            payload = {}
        item.update({"passed": payload.get("passed"),
                     "controls": f"{payload.get('passed_controls')}/{payload.get('total_controls')}"})
        failing_controls = [row.get("control") for row in (payload.get("controls") or [])
                            if isinstance(row, dict) and not row.get("passed")]
        if failing_controls:
            item["failing_controls"] = failing_controls
        if payload:
            item["failures"] = (payload.get("failures")
                                or (payload.get("positive") or {}).get("failures")
                                or failing_controls)
        # A checker that stops at its own precondition has not judged the rows: it
        # is a cascade, and the reason is recorded verbatim.
        diagnostic = ((checker.get("stdout") or "") + (checker.get("stderr") or "")).strip()
        if not payload and diagnostic:
            item["cannot_evaluate"] = diagnostic.splitlines()[-1][:300]
        measurement.setdefault("checkers", {})[label] = item
        if payload and not payload.get("passed"):
            failures.append(f"{label} is not green: the re-pointed rows do not satisfy its "
                            f"control set ({(item.get('failures') or [])[:2]})")
        elif not payload and required.get(label):
            failures.append(f"{label} could not evaluate (exit {checker.get('exit')}): "
                            f"{item.get('cannot_evaluate', '')}")
        elif not payload:
            item["disposition"] = ("cannot evaluate: its precondition is the filed revision's "
                                   "pinned read set, superseded by the round-26 register landing "
                                   "(a named pin cascade, not a structural defect of the row)")

    measurement["regressions"] = regressions["measurement"]
    failures.extend(regressions["failures"])
    return result(failures, measurement, missing)

    measurement["regressions"] = regressions["measurement"]
    failures.extend(regressions["failures"])
    return result(failures, measurement, missing)


# --------------------------------------------------------------------------
# Claim C — the open-question queue, 100% dispositioned
# --------------------------------------------------------------------------

def queue_ids(text):
    return sorted(set(QUEUE_ID_RE.findall(text)))


def find_readme_revisions():
    """New revisions of the lessons README: any `*.md` under reports/round-26
    whose content is a lessons index (an index row plus a queue section). The
    best candidate is the one carrying the most queue ids, then the most index
    rows, so a fragment that merely mentions the queue is not mistaken for the
    revision."""
    base = safe_path(ROUND_DIR)
    found = []
    for path in sorted(base.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if LESSONS_ROW_RE.search(text) and re.search(r"(?i)open[- ]question", text):
            found.append({"path": str(path.relative_to(ROOT)), "text": text,
                          "queue_ids": len(set(QUEUE_ID_RE.findall(text))),
                          "rows": len(set(LESSONS_ROW_RE.findall(text)))})
    found.sort(key=lambda row: (row["queue_ids"], row["rows"]))
    return found


def disposition_rows(text):
    """`{q-id: {class, owner, reason, next_round, evidence, raw}}` from a
    disposition table whose header carries the column names."""
    rows = {}
    lines = [line for line in text.splitlines() if line.strip().startswith("|")]
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue
        qid = next((cell.strip("`* ") for cell in cells if Q_ID_ANY_RE.fullmatch(cell.strip("`* "))), None)
        if not qid:
            continue
        joined = " | ".join(cells)
        klass = None
        if FIXED_RE.search(joined):
            klass = "fixed"
        if CARRIED_RE.search(joined):
            klass = "carried" if klass is None else klass
        rows[qid] = {
            "class": klass,
            "owner": bool(OWNER_TOKEN_RE.search(joined)),
            "reason": bool(REASON_RE.search(joined)),
            "next_round": (ROUND_POINTER_RE.search(joined).group(1)
                           if ROUND_POINTER_RE.search(joined) else None),
            "evidence": bool(EVIDENCE_TOKEN_RE.search(joined)),
            "raw": joined[:220],
        }
    return rows


def disposition_rows_from_json(document):
    """`{q-id: row}` from a structured disposition ledger. The delivered shape
    (`kotodama-open-question-dispositions-v1`) carries a `ledger` list whose rows
    name an id, a disposition, an owner, a reason and a next-touch round; a row
    with `evidence` entries is the evidence half. Any list of row-shaped objects
    with an id + disposition is accepted, so a sibling's own schema is not
    rejected for naming its columns differently."""
    rows = {}
    candidates = []
    if isinstance(document, dict):
        for key in ("ledger", "rows", "dispositions", "entries"):
            value = document.get(key)
            if isinstance(value, list):
                candidates.extend(value)
    elif isinstance(document, list):
        candidates = document
    for item in candidates:
        if not isinstance(item, dict):
            continue
        qid = str(item.get("id") or item.get("qid") or item.get("question_id") or "").strip("`* ")
        if not qid or not Q_ID_ANY_RE.fullmatch(qid):
            continue
        klass = str(item.get("disposition") or item.get("class") or "").strip().lower()
        if klass.startswith("fixed") or klass in ("closed", "resolved", "repaired"):
            klass = "fixed"
        elif klass.startswith("carr") or klass in ("open", "pending"):
            klass = "carried"
        evidence = item.get("evidence")
        has_evidence = bool(evidence) if isinstance(evidence, (list, dict)) else bool(evidence)
        if isinstance(evidence, list) and evidence and isinstance(evidence[0], dict):
            has_evidence = has_evidence and all(entry.get("ok", True) for entry in evidence
                                                if isinstance(entry, dict))
        rows[qid] = {
            "class": klass or None,
            "owner": bool(str(item.get("owner") or "").strip()),
            "reason": bool(str(item.get("reason") or "").strip()),
            "next_round": item.get("next_touch_round") or item.get("next_round"),
            "evidence": has_evidence,
            "evidence_ok": item.get("evidence_ok"),
            "raw": json.dumps({key: item.get(key) for key in
                               ("disposition", "owner", "reason", "next_touch_round")})[:220],
        }
    return rows


def load_dispositions(evidence):
    """Merge every disposition record under the round's open-questions directory:
    the structured ledger first, then any Markdown table (the human reading).
    Returns (rows, sources, surface_rows)."""
    rows, sources, surface_rows = {}, [], 0
    base = safe_path(OQ_DIR)
    if not base.is_dir():
        return rows, sources, surface_rows
    for path in sorted(base.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in (".json", ".md", ".yml", ".yaml", ".txt"):
            continue
        relative = str(path.relative_to(ROOT))
        text = evidence.text(relative)
        if not text:
            continue
        sources.append(relative)
        if path.suffix.lower() == ".json":
            try:
                document = strict_json(text)
            except (ValueError, TypeError):
                continue
            parsed = disposition_rows_from_json(document)
            if parsed:
                surface_rows = max(surface_rows, len(parsed))
                rows.update(parsed)
        else:
            parsed = disposition_rows(text)
            for qid, row in parsed.items():
                rows.setdefault(qid, row)
    return rows, sources, surface_rows


def measure_open_questions(evidence):
    """Claim C: every queue row dispositioned; the README revised as a new file."""
    failures, measurement, missing = [], {}, []

    filed_text = evidence.text(LESSONS_README)
    if not filed_text:
        failures.append(f"the filed lessons index is missing: {LESSONS_README}")
        missing.append(LESSONS_README)
        return result(failures, measurement, missing)
    filed_blob = git_blob_sha(safe_path(LESSONS_README).read_bytes())
    measurement["filed_readme"] = {
        "path": LESSONS_README, "blob_sha1": filed_blob,
        "declared_baseline_blob": README_BASELINE_BLOB,
        "unchanged_from_baseline": filed_blob == README_BASELINE_BLOB,
        "sha256": sha(safe_path(LESSONS_README).read_bytes()),
    }
    if filed_blob != README_BASELINE_BLOB:
        failures.append(f"the filed lessons index was edited in place (blob {filed_blob[:12]}… != "
                        f"declared baseline {README_BASELINE_BLOB[:12]}…); the claim requires a new "
                        f"revision file, not an in-place edit")

    revisions = find_readme_revisions()
    measurement["revision_candidates"] = [row["path"] for row in revisions]
    if not revisions:
        failures.append("no new lessons README revision landed under reports/round-26 "
                        "(the claim requires the README updated as a new file)")
        missing.append(f"{ROUND_DIR} (lessons README revision)")

    revision = revisions[-1] if revisions else None
    if revision:
        text = revision["text"]
        files = sorted(path.name for path in safe_path(LESSONS_DIR).glob("*.md"))
        rows = sorted({match.group(1) for match in LESSONS_ROW_RE.finditer(text)})
        round_rows = sorted({match.group(1) for match in LESSONS_ROUND_ROW_RE.finditer(text)})
        orphans = [name for name in files if name not in rows]
        phantom = [name for name in rows if name not in files]
        formats = [name for name in CENSUS_FORMATS if name.lower() in text.lower()]
        declared_rows = {int(value) for value in ROWS_DECLARED_RE.findall(text)}
        declared_files = {int(value) for value in FILES_DECLARED_RE.findall(text)}
        measurement["revision"] = {
            "path": revision["path"], "files": len(files), "rows": len(rows),
            "orphans": orphans, "phantom": phantom, "census_formats": formats,
            "declared_rows": sorted(declared_rows), "declared_files": sorted(declared_files),
            "counting_command": bool(COUNT_COMMAND_RE.search(text)),
            "round_13_row": round_rows,
        }
        if orphans:
            failures.append(f"the new revision omits {len(orphans)} lesson file(s): {orphans}")
        if phantom:
            failures.append(f"the new revision names {len(phantom)} file(s) that do not exist: {phantom}")
        if len(formats) != len(CENSUS_FORMATS):
            failures.append(f"the new revision documents {len(formats)} of {len(CENSUS_FORMATS)} "
                            f"census formats")
        if declared_rows and len(rows) not in declared_rows:
            failures.append(f"the new revision declares rows={sorted(declared_rows)}; the measured "
                            f"row count is {len(rows)}")
        if declared_files and len(files) not in declared_files:
            failures.append(f"the new revision declares files={sorted(declared_files)}; the "
                            f"partition holds {len(files)}")
        if not COUNT_COMMAND_RE.search(text):
            failures.append("the new revision carries no counting command")

    # the queue: ids from the newest revision (falling back to the filed README)
    queue_text = revision["text"] if revision else filed_text
    ids = queue_ids(queue_text)
    measurement["queue"] = {"source": revision["path"] if revision else LESSONS_README,
                            "rows": len(ids), "ids": ids}
    if not ids:
        failures.append("the queue carries no question ids")

    rows, sources, surface_rows = load_dispositions(evidence)
    measurement["disposition_sources"] = sources
    measurement["disposition_rows_total"] = surface_rows
    if not sources:
        failures.append(f"no open-question disposition record landed under {OQ_DIR}")
        missing.append(OQ_DIR)

    undispositioned = [qid for qid in ids if qid not in rows]
    measurement["dispositions"] = {qid: rows[qid] for qid in sorted(rows) if qid in ids}
    if undispositioned:
        failures.append(f"{len(undispositioned)} of {len(ids)} queue row(s) carry no disposition: "
                        f"{undispositioned[:10]}")
    for qid in ids:
        row = rows.get(qid)
        if row is None:
            continue
        if row["class"] is None:
            failures.append(f"{qid} is listed without a disposition class")
        elif row["class"] == "fixed" and not row["evidence"]:
            failures.append(f"{qid} is dispositioned `fixed` with no evidence")
        elif row["class"] == "carried" and not (row["owner"] and row["reason"]
                                                and row["next_round"]):
            failures.append(f"{qid} is dispositioned `carried` without a named owner + reason + "
                            f"next touch round (owner={row['owner']}, reason={row['reason']}, "
                            f"next_round={row['next_round']})")
    covered = len([qid for qid in ids if qid in rows])
    measurement["coverage"] = {"queue_rows": len(ids), "dispositioned": covered,
                               "undispositioned": len(undispositioned),
                               "percent": round(100.0 * covered / len(ids), 2) if ids else 0.0,
                               "command": f"{COMMAND} (queue ids vs disposition rows)",
                               "date": today()}
    return result(failures, measurement, missing)


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
    executing in the live lane itself (the normal `python3 reports/round-26/
    run-validation.py` invocation), so the runner never copies a tree onto
    itself."""
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


def selftest():
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    check("argot-head2-maximal-onset", argot_apply("saalumi", "head2") == "saalu",
          observed=argot_apply("saalumi", "head2"))
    check("argot-head2-not-maximal-coda", argot_apply("saalumi", "head2") != "saalum")
    check("argot-reverse-makun", argot_apply("makun", "reverse") == "nukam")
    check("argot-unknown-operation-refused", _raises(argot_apply, "min", "nope"))
    check("argot-worked-pairs-agree", not argot_selfcheck(),
          mismatches=argot_selfcheck()[:3])
    check("syllabify-saalumi", syllabify("saalumi") == ["saa", "lu", "mi"],
          observed=syllabify("saalumi"))

    coverage = parse_coverage_line(
        "coverage: examples/x.yml records=156 register_scoped=6 derived_pairs=0 "
        "claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0")
    check("coverage-line-parse", coverage == {"records": 156, "register_scoped": 6,
                                              "derived_pairs": 0, "claimed_chains": 8,
                                              "borrow_pairs": 6, "violations": 0,
                                              "rule_holds": 0}, observed=coverage)
    check("coverage-line-absent-is-none", parse_coverage_line("no coverage here") is None)

    check("operation-string-normalizes", normalize_operation("REVERSE") == "reverse")
    check("operation-mapping-normalizes",
          normalize_operation({"op": "head2", "base": "saalumi"}) == "head2")
    check("operation-unknown-is-none", normalize_operation({"weird": 1}) is None)
    check("base-from-mapping", normalize_base({"base": "min"}, "min") == "min")
    check("base-falls-back-to-derived-from", normalize_base("min", "min") == "min")

    check("register-marked", register_scoped({"register": "quote"}))
    check("register-unmarked-is-not-scoped", not register_scoped({"register": "plain"}))
    check("derivation-pair-is-scoped",
          register_scoped({"derived_from": "min", "derivation": "reverse"}))

    check("lengthen-doubles-first-nucleus", lengthen("tum") == "tuum", observed=lengthen("tum"))
    check("lengthen-single-syllable", lengthen("mes") == "mees")
    check("lengthen-vowelless-unchanged", lengthen("tks") == "tks")
    rule_packet = {"morphology": {"derivation_rules": [
        {"id": "LENGTHEN", "kind": "vowel-length",
         "pattern": "^(?P<onset>[^aeiou]*)(?P<vowel>[aeiou])(?P<rest>.*)$",
         "output": "{onset}{vowel}{vowel}{rest}"}]}}
    ops = packet_rule_operations(rule_packet)
    check("rule-operations-parsed", "lengthen" in ops and "id" not in ops, observed=sorted(ops))
    check("declared-rule-replays",
          apply_operation(rule_packet, "lengthen", "tum") == "tuum",
          observed=apply_operation(rule_packet, "lengthen", "tum"))
    check("computed-reverse-still-works", apply_operation({}, "reverse", "min") == "nim")
    check("unknown-operation-refused", _raises(apply_operation, {}, "nope", "min"))

    packet = {"lexicon": [
        {"id": "L-1", "term": "nim", "register": "quote", "derived_from": "min",
         "derivation": "reverse"},
        {"id": "L-2", "term": "min", "register": "plain"},
        {"id": "L-3", "term": "x", "derived_from": "min"},
    ]}
    pairs, half = declared_pairs(packet)
    check("declared-pairs-found", len(pairs) == 1 and pairs[0]["operation"] == "reverse",
          observed=pairs)
    check("half-pairs-found", [row["id"] for row in half] == ["L-3"], observed=half)
    mapping_packet = {"lexicon": [
        {"id": "RF-01", "term": "tuum", "register": "stamp",
         "derivation": {"op": "lengthen", "base": "tum"}},
    ]}
    mapping_pairs, mapping_half = declared_pairs(mapping_packet)
    check("derivation-mapping-is-a-pair",
          len(mapping_pairs) == 1 and mapping_pairs[0]["base"] == "tum"
          and mapping_pairs[0]["operation"] == "lengthen" and not mapping_half,
          observed=mapping_pairs)
    by_id, by_term = record_index(packet)
    check("record-index-by-term", "min" in by_term and "L-2" in by_id)

    check("argot-ids-both-accepted", "D4L-ARGOT-DERV" in ARGOT_IDS
          and "D4L-ARGOT-DERIV" in ARGOT_IDS)

    check("legs-parsed-off-a-gate-run", gate_legs(
        "ok   L1-build\nok   L2-channel\nFAIL L3-routing-consistency\n"
        "summary: 2/3 legs passed\n") == (["L1-build", "L2-channel"],
                                          ["L3-routing-consistency"], 2, 3))

    queue = ("## 4. Open-question queue\n\n| Q-id | question | owner | status |\n"
             "|---|---|---|---|\n"
             "| Q-02-1 | axis drift | `operator` | open |\n"
             "| Q-04-1 | adapter | `tools/gates/naming-collision-gate.py` | open |\n")
    check("queue-ids-parsed", queue_ids(queue) == ["Q-02-1", "Q-04-1"], observed=queue_ids(queue))

    disposition = (
        "| Q-02-1 | fixed | evidence: `python3 tools/x.py` exit 0 |\n"
        "| Q-04-1 | carried | owner: `tools/gates/naming-collision-gate.py`; reason: needs the "
        "adapter; next round 27 |\n")
    rows = disposition_rows(disposition)
    check("disposition-fixed-parsed",
          rows["Q-02-1"]["class"] == "fixed" and rows["Q-02-1"]["evidence"], observed=rows["Q-02-1"])
    check("disposition-carried-parsed",
          rows["Q-04-1"]["class"] == "carried" and rows["Q-04-1"]["owner"]
          and rows["Q-04-1"]["reason"] and rows["Q-04-1"]["next_round"] == "27",
          observed=rows["Q-04-1"])
    check("disposition-ownerless-carried-fails",
          not (disposition_rows("| Q-09-1 | carried | no owner here |\n")["Q-09-1"]["owner"]))

    ledger = {"schema": "kotodama-open-question-dispositions-v1", "ledger": [
        {"id": "Q-02-1", "disposition": "carried", "owner": "lore", "reason": "lore owns it",
         "next_touch_round": 27, "evidence": [{"ok": True}]},
        {"id": "Q-04-1", "disposition": "fixed-with-evidence", "owner": "kotodama",
         "reason": "re-ran green", "evidence": [{"ok": True}]},
        {"id": "Q-04-2", "disposition": "fixed-with-evidence", "owner": "kotodama",
         "reason": "probe failed", "evidence": [{"ok": False}]},
    ]}
    json_rows = disposition_rows_from_json(ledger)
    check("json-ledger-carried-parsed",
          json_rows["Q-02-1"]["class"] == "carried" and json_rows["Q-02-1"]["next_round"] == 27,
          observed=json_rows["Q-02-1"])
    check("json-ledger-fixed-parsed",
          json_rows["Q-04-1"]["class"] == "fixed" and json_rows["Q-04-1"]["evidence"],
          observed=json_rows["Q-04-1"])
    check("json-ledger-failed-evidence-is-not-evidence",
          not json_rows["Q-04-2"]["evidence"], observed=json_rows["Q-04-2"])
    check("json-ledger-ignores-non-row-ids",
          "schema" not in json_rows and len(json_rows) == 3, observed=sorted(json_rows))
    check("json-ledger-list-form",
          len(disposition_rows_from_json([{"id": "Q-11-1", "disposition": "carried",
                                           "owner": "parent", "reason": "r",
                                           "next_touch_round": 28}])) == 1)

    tail = ("{\"tail\": \"v2-successor-pin\", \"pin\": "
            "\"2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3\"}")
    check("tail-name-v2", "v2-successor-pin" in tail_names(tail), observed=tail_names(tail))
    check("tail-name-v3",
          "v3-baseline-pin" in tail_names("the v3 baseline pin at reports/round-20/handoff/expected.json"))
    check("tail-name-none", not tail_names("nothing to see here"))

    check("readme-baseline-blob-pinned", bool(re.fullmatch(r"[0-9a-f]{40}", README_BASELINE_BLOB)))

    passed_controls = sum(1 for item in controls if item["passed"])
    for item in controls:
        print(("ok   " if item["passed"] else "FAIL ") + item["control"]
              + ("" if item["passed"] else f" — {item}"))
    print(f"selftest: {passed_controls}/{len(controls)} checks passed — the runner's own "
          "implementation of the two argot operations against the eleven design pairs, the gate "
          "coverage/leg parsers, the derivation-field normalizers and register scoping, the "
          "disposition-table and queue-id parsers, and the pin-tail namer; no file opened for "
          "writing")
    return 0 if passed_controls == len(controls) else 1


def _raises(function, *args):
    try:
        function(*args)
        return False
    except Exception:
        return True


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
            ("D", lambda: measure_register_stratum(evidence, regressions)),
            ("O", lambda: measure_remainders(evidence, regressions)),
            ("C", lambda: measure_open_questions(evidence))):
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
    if claims.get("round") != 26 or targets.get("round") != 26:
        coherence.append("Claims/targets are not both round 26")
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
    return {"round": 26, "runner": RUNNER, "runner_sha256": sha(safe_path(RUNNER).read_bytes()),
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
                "Claim D is measured from the delivered bytes: the packet's declared schema, at least one delivered derivation pair, this runner's own head2/reverse replay of every delivered pair (never read back from the gate), the base's resolution to a record of the same packet, the argot gate's own coverage line and canonical run, a runner-authored violating control and its clean counterpart, the typed projection's classification of the register forms, the hold set's named revision, and the round-26 artifact's forecast-closure record. The delivered implementation's shape (which file carries the operations, which field names the pair) is deliberately not pinned beyond the schema the claim names.",
                "Claim D's half-declared-pair and self-derivation classes are measured and recorded as review evidence. A half-pair (exactly one of derived_from/derivation) is graded as a failure because it is the round-25 review's measured laundering channel; a self-derivation is graded because it is a false green the D3 precedent already refuses.",
                "Claim O is measured behaviourally on the three named round-25 remainders: the r4 twin gap is dispositioned by a new row carrying a twin.json projected from the filed r4 revision, or by a documented convention naming the packet-only shape; each pin tail is re-pointed by a new round-26 row that names the tail and pins the surface's live digest; and the checker bound to the re-pointed rows is green. A stale filed pin is recorded as historical, not graded.",
                "Claim O's pin surface is baseline-relative and the tree moves under it: a row re-pointed before a later landing goes stale again, and the twin's manifest digests bind the *filed* revision's read set rather than today's tree. A checker that stops at its own precondition is recorded as a named pin cascade (`cannot_evaluate`), never laundered as a pass; a checker that runs and reports a red control is a failure. The pin re-point checker is the required one; the r4 twin verifier and the frozen round-25 checker replay superseded baselines and are recorded, not graded.",
                "Claim C requires a NEW lessons README revision: the filed corpus/lessons/README.md must keep its declared baseline Git blob, and the revision must reproduce the partition arithmetic, the three census formats and a counting command. Disposition rows must cover every queue id; a `fixed` row carries evidence and a `carried` row carries owner + reason + next touch round.",
                "Protected reports and frozen generations of rounds 8-25 must match the round-26 declared baseline; new round-26 files live under reports/round-26 and corpus/lessons only.",
            ]}


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def dependencies_ready():
    """The artifacts the three claims depend on. Used only by --wait."""
    wanted = [OQ_DIR, f"{ROUND_DIR}/lessons", f"{ROUND_DIR}/register",
              f"{ROUND_DIR}/remainders"]
    return [path for path in wanted if not (safe_path(path).exists())]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Measure round-26 D/O/C acceptance; run in the lane root or an isolated clone.")
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
