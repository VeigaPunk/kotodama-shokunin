#!/usr/bin/env python3
"""Round-27 acceptance runner: claims D (register law + syllabify), O (D4 pin sweep), C (register-strata entry).

Claim D — the register law lands and the syllabify disagreement is fixed.
  `reports/round-26/register/review.md` named two structural gaps: **RL-6**,
  the register *law* (admissibility, oath-only-plain, the guest asymmetry) is
  specified but owned by no delivered component, and **RD-4**, the delivered
  gate's `syllabify` is a simple maximal onset that never checks legality and
  therefore disagrees with `design-language.md:191-196`'s stated
  legality-constrained maximal onset. This runner measures the delivered
  artifact, never an intention:
    * the D4 packet carries a `registers` block that is **component-owned** —
      a component file declares `registers` in its own `packet_keys` and the
      packet's rows are that component's rows, id for id and law for law (the
      "wired into the packet deterministically" clause);
    * the law is **machine-readable and covers the three clauses the claim
      names** — what may be said in-register (admissibility), by whom (agent),
      with what record consequences (consequence) — and every law row carries
      the universal record fields (`id`, `axis`, `evidence`, `follows`);
    * the amendment is deterministic: the assembler, the typed adapter and the
      projector each regenerate their artifact byte-for-byte (`--check`, exit 0);
    * the **syllabify fix**: this runner implements the design's stated
      algorithm itself (legality-constrained maximal onset, written from the
      `design-language.md` §5 prose and the packet's own inventory) and requires
      the delivered gate's `syllabify` to agree with it on **every** delivered
      form, to reproduce the design's one worked `head2` row (`saalumi` ->
      `saalu`), and never to emit an illegal syllable (a bare consonant run, an
      onset cluster, or an illegal coda);
    * the argot gate, the typed gate (with the register leg) and the two D4
      adapter gates are green, and the hold set carries a round-27 revision note
      whose counts agree with the projection's coverage block;
    * the round-27 D artifact names the law landing, the syllabify fix and the
      disagreement count it closed, and carries an executed receipt.

Claim O — the D4 pin sweep, and regressions.
  The round-26 register landing moved the D4 packet surface; this runner sweeps
  **every row that pins a D4 surface** as a single pass — the frozen manifests
  (`MANIFEST.tsv`), the battery baselines (`tools/gates/expected/**`,
  `tools/gates/frozen/**`), the typed-pipeline profile, the hold set, the v3
  read-set baseline and the historical round-20/22/26 rows — and classifies
  each declared digest as `green` (equal to the live bytes) or `drift`. Every
  drifted row must be re-pinned by a **NEW round-27 row** that names the
  surface and carries the live digest; the filed rounds stay byte-identical.
  The battery must read `pass 7 / fail 0 / unevaluable 0` with `coverage 9/9`
  and every registered baseline pinned, the frozen-verdict replay and the three
  handoff profiles must be green, and the fixed regression inventory must pass.

Claim C — the register-strata knowledge entry and the corpus README.
  `corpus/knowledge/linguistics/` gains a **new** entry on register strata for
  attestation speech: absent from the declared baseline revision (Git blob
  identity, not a re-read), frontmatter-complete (`topic`, `sources`,
  `verified-at`, `recheck`, `couples`), gap-named, decision-record carrying,
  grounded in the round-26/27 artifacts and in cited external sources, and
  making no canon claim. `corpus/README.md` must carry a new revision whose
  linguistics row names the entry and whose partition arithmetic reproduces the
  measured tree.

Run only in the lane root or an isolated clone under its .scratch:
  python3 reports/round-27/run-validation.py             (measure + write receipt)
  python3 reports/round-27/run-validation.py --check     (measure only, print)
  python3 reports/round-27/run-validation.py --selftest  (dependency-free controls)
  python3 reports/round-27/run-validation.py --wait 600  (poll late dependencies)
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
ROUND_DIR = "reports/round-27"
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
V3_BASELINE_FALLBACK = f"{ROUND_DIR}/pinsweep/v3-baseline-r27/expected.json"
KNOWLEDGE_DIR = "corpus/knowledge"
LINGUISTICS_DIR = f"{KNOWLEDGE_DIR}/linguistics"
CORPUS_README = "corpus/README.md"
QUALITY = "corpus/QUALITY.md"
DESIGN_LANGUAGE = "reports/round-17/d4/design-language.md"
R26_REGISTER = "reports/round-26/register"

SYNC_PATHS = (ROUND_DIR, "SKILL.md", "LOG.md", "SCORECARD.md", "PROVINCE.md",
              "SHONEN.md", "corpus", "examples", "tools")
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 27)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 27))

# --------------------------------------------------------------------------
# constants read off the delivered tree and the round-26 named gaps
# --------------------------------------------------------------------------

# The design's one worked `head2` row (`design-language.md` §5). It is the only
# head2 value the design fixes by name, so it is the anchor the two algorithms
# must agree on.
DESIGN_WORKED_HEAD2 = ("saalumi", "saalu")
# Legality-forced splits: the old gate read `tikmes` as `ti.kme.s` (an onset
# cluster it never validated); the design's law reads it `tik.mes`. These are
# this runner's own controls, not design quotes. `head2` joins the first *two*
# syllables, so a two-syllable word's head2 is the whole word.
SYLLABLE_CONTROLS = (("tikmes", ["tik", "mes"]), ("kalker", ["kal", "ker"]),
                     ("tumhai", ["tum", "ha", "i"]), ("haitun", ["ha", "i", "tun"]),
                     ("saalumi", ["saa", "lu", "mi"]))
# The eleven worked derivations the round-17 design fixes (design-language §5),
# pinned here by hand; this runner re-derives them with its own implementation.
ARGOT_WORKED = (
    ("saalumi", "head2", "saalu"), ("min", "reverse", "nim"),
    ("kus", "reverse", "suk"), ("nam", "reverse", "man"),
    ("nes", "reverse", "sen"), ("sam", "reverse", "mas"),
    ("mus", "reverse", "sum"), ("kin", "reverse", "nik"),
    ("sun", "reverse", "nus"), ("samun", "reverse", "numas"),
    ("makun", "reverse", "nukam"),
)
ARGOT_IDS = ("D4L-ARGOT-DERIV", "D4L-ARGOT-DERV")
UNMARKED_REGISTERS = frozenset(("plain", "neutral", "standard", "ordinary", "unmarked", ""))
D4_SCHEMA_FIELDS = ("derived_from", "derivation")
# Every D4 surface a pin row can name. The sweep walks pin rows; this list is
# the surface set a re-pin row must name (with its live digest) to close a drift.
D4_SURFACES = (f"{PACKET_D4}", f"{PACKET_D4_TYPED}", f"{D4_PROJECTION}", f"{D4_HOLDS}",
               *(f"{D4_COMPONENTS}/{name}" for name in (
                   "01-brief.yml", "02-phonology.yml", "03-orthography.yml", "04-lexicon.yml",
                   "05-naming.yml", "06-myth.yml", "07-symbolism.yml", "08-eras.yml",
                   "09-costumes.yml", "10-ritual-calendar.yml", "11-contact-history.yml",
                   "12-provenance.yml", "13-register-law.yml")))

# The three speech-act clauses the D claim names, as observable token sets. A
# law block must reach all three; which tokens reached each is recorded.
LAW_CLAUSES = {
    "admissibility": re.compile(
        r"(?i)\badmissib|may be said|only in|in-register|stamp-act|\bslot\b"),
    "agent": re.compile(
        r"(?i)\bby whom|who may|speaker|\bholder\b|\bbroker\b|\bguest\b|stamp-holder"),
    "consequence": re.compile(
        r"(?i)\bvoid\b|\bbinding\b|\bbinds?\b|\brecord\b|consequence|\bkeeps?\b|furnace roll"),
}
REGISTER_LAW_ID_RE = re.compile(r"\b(?:RGL|QREG|REG|RL)-\d{2}\b")

COVERAGE_RE = re.compile(
    r"coverage:\s*\S+\s+records=(\d+)\s+register_scoped=(\d+)\s+derived_pairs=(\d+)"
    r"\s+claimed_chains=(\d+)\s+borrow_pairs=(\d+)\s+violations=(\d+)\s+rule_holds=(\d+)")
LEG_RE = re.compile(r"^(ok|FAIL)\s+([A-Za-z0-9_.-]+)")
SUMMARY_RE = re.compile(r"summary:\s*(\d+)/(\d+)\s+legs passed")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
PATHLIKE = re.compile(r"^[\w./-]+\.(?:ya?ml|json|py|md|txt)$")
PARTITION_HEADER_RE = re.compile(r"(?m)^##\s+([a-z-]+)/\s*\((\d+)\)")
REVISION_RE = re.compile(r"(?m)^revision:\s*([0-9]+\.[0-9]+)\s*—")
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
ROUND_ARTIFACT_RE = re.compile(r"reports/round-2[67]/[\w./-]+")
CANON_CLAIM_RE = re.compile(r"(?i)\bis canon|canoniz(?:ed|es)\b|adopted as canon")

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
        return None, ["Round-27 declared baseline is not a full Git revision"]
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
        failures.append("Filed rounds 8-26 or their frozen generations differ from the declared baseline")
    return result(failures, {"baseline_revision": revision,
                             "protected_paths": metric(len(expected), "git ls-tree of protected baseline"),
                             "differences": rows[:20],
                             "differences_total": metric(len(rows), "compare protected Git blobs to working bytes"),
                             "protected_status_rows": metric(len(worktree), "git status over protected paths")})


def run_command(label, parts, timeout=900):
    scratch = ROOT / ".scratch" / "round-27" / "validation" / label
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
    """The receipt row: the full stdout up to a generous cap (the battery prints
    a ~29 KB JSON document that the O leg parses, so a tight cap would truncate
    the very bytes being read), the stderr tail, and the parsed document when
    the stdout is JSON."""
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
# Syllabification — this runner's own reading of the design's stated algorithm
# --------------------------------------------------------------------------

def form_items(word, vowels):
    """`word` as (kind, text) items: a nucleus is one vowel or one doubled
    vowel (vowel length is one nucleus), a consonant run is one item."""
    items, index = [], 0
    while index < len(word):
        char = word[index]
        if char in vowels:
            count = 2 if index + 1 < len(word) and word[index + 1] == char else 1
            items.append(("V", word[index:index + count]))
            index += count
        else:
            end = index
            while end < len(word) and word[end] not in vowels:
                end += 1
            items.append(("C", word[index:end]))
            index = end
    return items


def simple_syllables(word, vowels):
    """The pre-fix gate's reading: every consonant run before a nucleus is that
    nucleus's onset, and a trailing run becomes a syllable of its own. Kept here
    only as the control the fix is measured against."""
    syllables, pending = [], ""
    for kind, text in form_items(word, vowels):
        if kind == "V":
            syllables.append(pending + text)
            pending = ""
        else:
            pending += text
    if pending:
        syllables.append(pending)
    return syllables


def lawful_syllables(word, consonants, vowels, codas, onset_clusters=None):
    """The design's stated maximal-onset rule, legality-constrained
    (`design-language.md` §5: "a consonant is taken as the onset of the
    following syllable whenever that yields a legal syllable").

    The longest legal onset wins; the remainder closes the previous syllable
    when it is a legal coda; a word-final run closes the last syllable (a bare
    consonant is not a syllable). Written here from the prose and the packet's
    own inventory, never read back from the gate.
    """
    def onset_ok(run):
        if not run:
            return True
        if run in consonants:
            return True
        return bool(onset_clusters) and run in set(onset_clusters)

    def coda_ok(run):
        return not run or (len(run) == 1 and run in codas)

    items = form_items(word, vowels)
    syllables, pending = [], ""
    for position, (kind, text) in enumerate(items):
        if kind == "V":
            syllables.append(pending + text)
            pending = ""
            continue
        if position == len(items) - 1:
            if syllables:
                syllables[-1] += text
            else:
                pending += text
            continue
        split = None
        for cut in range(0, len(text) + 1):
            onset, tail = text[cut:], text[:cut]
            if onset_ok(onset) and coda_ok(tail):
                split = (tail, onset)
                break
        if split is None:
            split = ("", text)
        tail, onset = split
        if tail:
            if syllables:
                syllables[-1] += tail
            else:
                pending += tail
        pending += onset
    if pending:
        syllables.append(pending)
    return syllables


def inventory(packet):
    """(consonants, vowels, codas, onset_clusters) off the packet's own
    phonology block; empty sets when the block is absent."""
    phonology = packet.get("phonology") if isinstance(packet, dict) else None
    phonology = phonology if isinstance(phonology, dict) else {}
    consonants = {str(item) for item in (phonology.get("consonants") or [])}
    vowels = {str(item) for item in (phonology.get("vowels") or [])}
    codas = {str(item) for item in (phonology.get("coda") or [])}
    onset_clusters = phonology.get("onset_clusters")
    if isinstance(onset_clusters, list):
        onset_clusters = [str(item) for item in onset_clusters]
    elif onset_clusters in (True, False, None):
        onset_clusters = [] if not onset_clusters else None
    return consonants, vowels, codas, onset_clusters


def illegal_syllables(syllables, consonants, vowels, codas):
    """Every syllable that is not a legal D4 syllable: no nucleus, an onset
    cluster, or an illegal coda."""
    bad = []
    for syllable in syllables:
        core = "".join(char for char in syllable if char in vowels)
        if not core:
            bad.append({"syllable": syllable, "reason": "no nucleus"})
            continue
        start = syllable.index(core)
        onset = syllable[:start]
        tail = syllable[start + len(core):]
        if onset and onset not in consonants:
            bad.append({"syllable": syllable, "reason": f"illegal onset {onset!r}"})
        if tail and (len(tail) != 1 or tail not in codas):
            bad.append({"syllable": syllable, "reason": f"illegal coda {tail!r}"})
    return bad


# --------------------------------------------------------------------------
# Argot replay — this runner's own implementation of the declared operations
# --------------------------------------------------------------------------

def argot_apply(base, operation):
    if operation == "head2":
        return base
    if operation == "reverse":
        return base[::-1]
    raise ValueError(f"unknown argot operation: {operation}")


def argot_selfcheck():
    bad = []
    for base, operation, expected in ARGOT_WORKED:
        if operation == "reverse":
            observed = argot_apply(base, operation)
        else:
            observed = None  # head2 needs an inventory; checked in measure()
        if observed is not None and observed != expected:
            bad.append((base, operation, expected, observed))
    return bad


def normalize_operation(value):
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


def name_records(packet):
    rows = packet.get("names") if isinstance(packet, dict) else None
    return [row for row in (rows or []) if isinstance(row, dict)]


def record_index(packet):
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
    register = row.get("register")
    if isinstance(register, str) and register.strip().lower() not in UNMARKED_REGISTERS:
        return True
    return any(row.get(field) for field in D4_SCHEMA_FIELDS)


def lengthen(base):
    for index, char in enumerate(base):
        if char in "aeiou":
            return base[:index + 1] + char + base[index + 1:]
    return base


def packet_rule_operations(packet):
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


def replay_template(pair, base):
    pattern, output = pair
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


def apply_operation(packet, operation, base, consonants=None, vowels=None):
    if operation == "head2":
        if consonants is None:
            consonants, vowels, _codas, clusters = inventory(packet)
        else:
            _c, _v, _codas, clusters = inventory(packet)
        return "".join(lawful_syllables(base, consonants, vowels, _codas, clusters)[:2])
    if operation == "reverse":
        return base[::-1]
    rules = packet_rule_operations(packet)
    if operation in rules:
        return replay_template(rules[operation], base)
    if operation == "lengthen":
        return lengthen(base)
    raise ValueError(f"unknown argot operation: {operation}")


def declared_pairs(packet):
    pairs, half = [], []
    for row in lexicon_records(packet):
        derived_from = row.get("derived_from")
        derivation = row.get("derivation")
        operation = normalize_operation(derivation)
        base = normalize_base(derivation, derived_from)
        if derivation and operation and base:
            pairs.append({"id": row.get("id"), "term": row.get("term"),
                          "register": row.get("register"), "operation": operation, "base": base,
                          "stage": row.get("stage")})
        elif derived_from or derivation:
            half.append({"id": row.get("id"), "term": row.get("term"),
                         "declared": [name for name in D4_SCHEMA_FIELDS if row.get(name)]})
    return pairs, half


# --------------------------------------------------------------------------
# Claim D — the register law lands, the syllabify disagreement is fixed
# --------------------------------------------------------------------------

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


def law_clause_coverage(text):
    return {name: bool(pattern.search(text or "")) for name, pattern in LAW_CLAUSES.items()}


def measure_register_law(evidence, regressions):
    failures, measurement, missing = [], {}, []

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
    consonants, vowels, codas, clusters = inventory(packet)

    # ---- 1. the runner's own re-derivation of the design's eleven worked rows
    bad_reverse = argot_selfcheck()
    head2_rows = []
    for base, operation, expected in ARGOT_WORKED:
        if operation != "head2":
            continue
        observed = apply_operation(packet, "head2", base, consonants, vowels)
        head2_rows.append({"base": base, "expected": expected, "observed": observed,
                           "agrees": observed == expected})
    bad_head2 = [row for row in head2_rows if not row["agrees"]]
    measurement["runner_independent_rederivation"] = {
        "worked_pairs": len(ARGOT_WORKED),
        "reverse_mismatches": bad_reverse,
        "head2_rows": head2_rows,
        "command": f"{COMMAND} (this runner's own head2/reverse implementation vs the eleven design pairs)",
        "date": today()}
    if bad_reverse:
        failures.append(f"the runner's own reverse disagrees with the design on {len(bad_reverse)} "
                        f"pair(s): {bad_reverse[:3]}")
    if bad_head2:
        failures.append(f"the runner's own lawful head2 disagrees with the design's worked row(s): "
                        f"{bad_head2[:3]}")

    # ---- 2. the law blocks exist and are component-owned
    # The claim names one law; the delivered tree carries it as two blocks — the
    # `registers` declaration (the marked register and its operation/era rules)
    # and the `register_law` speech-act rows (what may be said, by whom, with
    # what record consequence). Both are graded, and each must be owned by a
    # component that declares it in its own `packet_keys`.
    block_rows = {}
    for name in ("registers", "register_law"):
        value = packet.get(name)
        block_rows[name] = [row for row in (value or []) if isinstance(row, dict)]
    rows = block_rows["registers"]
    owners = []
    for path in component_files():
        keys, document = component_packet_keys(path)
        if not keys:
            continue
        for name in ("registers", "register_law"):
            if name in keys and document.get(name):
                owners.append({"path": str(path.relative_to(ROOT)), "block": name,
                               "packet_keys": keys, "rows": len(document.get(name) or [])})
    measurement["law_blocks"] = {
        "registers": {"present": isinstance(packet.get("registers"), list),
                      "rows_total": len(rows),
                      "ids": [row.get("id") for row in rows][:12],
                      "classes": sorted({str(row.get("class")) for row in rows if row.get("class")})},
        "register_law": {"present": isinstance(packet.get("register_law"), list),
                         "rows_total": len(block_rows["register_law"]),
                         "ids": [row.get("id") for row in block_rows["register_law"]][:12],
                         "kinds": sorted({str(row.get("kind")) for row in
                                          block_rows["register_law"] if row.get("kind")})},
        "declaring_components": owners,
        "command": f"{COMMAND} (packet law blocks vs component packet_keys)",
        "date": today()}
    if not rows:
        failures.append(f"the D4 packet carries no `registers` block: the register law is still "
                        f"unowned (round-26 RL-6)")
        missing.append(f"{PACKET_D4} (registers block)")
        return result(failures, measurement, missing)
    if not block_rows["register_law"]:
        failures.append("the D4 packet carries no `register_law` block: the speech-act rows "
                        "(act / holder / consequence) are still unowned (RL-6)")
    for name in ("registers", "register_law"):
        if not block_rows[name]:
            continue
        owner = next((item for item in owners if item["block"] == name), None)
        if owner is None:
            failures.append(f"no component declares the `{name}` block in its own `packet_keys` and "
                            f"carries the rows: the law is not wired in deterministically (RL-6)")
            continue
        try:
            component_document = load_yaml_text(
                safe_path(owner["path"]).read_text(encoding="utf-8"))
        except Exception as error:
            component_document = None
            failures.append(f"the declaring component {owner['path']} does not parse: {error}")
        component_rows = [row for row in ((component_document or {}).get(name) or [])
                          if isinstance(row, dict)]
        packet_ids = [str(row.get("id")) for row in block_rows[name]]
        component_ids = [str(row.get("id")) for row in component_rows]
        by_id = {str(row.get("id")): row for row in component_rows}
        fields_match = all(
            all(str(by_id.get(str(row.get("id")), {}).get(key) or "") == str(row.get(key) or "")
                for key in row)
            for row in block_rows[name])
        measurement.setdefault("component_ownership", {})[name] = {
            "component": owner["path"], "component_rows": len(component_rows),
            "packet_ids": packet_ids, "component_ids": component_ids,
            "ids_equal": packet_ids == component_ids, "rows_equal": fields_match}
        if packet_ids != component_ids:
            failures.append(f"the packet's {name} rows are not the declaring component's rows: "
                            f"packet={packet_ids} component={component_ids}")
        if not fields_match:
            failures.append(f"the packet's {name} rows are not the component's rows field for "
                            f"field (the assembly is not a pure function of the component)")

    # ---- 3. the law is machine-readable and covers the three named clauses
    all_rows = rows + block_rows["register_law"]
    block_text = "\n".join(
        " ".join(str(row.get(key) or "") for key in
                 ("id", "title", "register", "class", "kind", "law", "operation_rule", "era_rule",
                  "act", "speaker", "holder", "force", "consequence", "slot", "agent", "clauses",
                  "note"))
        for row in all_rows)
    clauses = law_clause_coverage(block_text)
    marked = [row for row in rows
              if str(row.get("class") or "").strip().lower() not in ("", "unmarked")]
    rule_ids = sorted(set(REGISTER_LAW_ID_RE.findall(block_text)))
    universal = ("id", "axis", "evidence", "follows")
    rows_with_universal = [row for row in all_rows if all(key in row for key in universal)]
    measurement["register_law"] = {
        "clauses": clauses,
        "marked_rows": len(marked),
        "rule_ids": rule_ids,
        "rows_with_universal_fields": len(rows_with_universal),
        "rows_total": len(all_rows),
        "law_text_bytes": len(block_text.encode("utf-8")),
        "speech_act_rows": len(block_rows["register_law"]),
    }
    missing_clauses = [name for name, present in clauses.items() if not present]
    if missing_clauses:
        failures.append(f"the register law does not reach the claim's clause(s): "
                        f"{missing_clauses} (admissibility / by-whom / record consequence)")
    if not marked:
        failures.append("the registers block declares no marked register class")
    if not rule_ids:
        failures.append("the register law carries no rule ids (RGL-*/QREG-*/REG-*): the law is "
                        "prose, not a machine-readable rule set")
    if len(rows_with_universal) != len(all_rows):
        failures.append(f"{len(all_rows) - len(rows_with_universal)} law row(s) omit one of the "
                        f"universal record fields {universal}")
    contract_fields = ((packet.get("contract") or {}).get("record_fields") or {})
    measurement["register_contract_fields"] = {name: contract_fields.get(name)
                                               for name in ("registers", "register_law")}
    for name in ("registers", "register_law"):
        if not block_rows[name]:
            continue
        if not contract_fields.get(name):
            failures.append(f"the packet contract declares no `record_fields.{name}`: the law block "
                            f"is outside the declared record contract")

    # ---- 4. the amendment is deterministic: three byte-identical regenerations
    runs = regressions["measurement"]["labels"]
    deterministic = {label: runs.get(label, {}).get("exit") for label in
                     ("d4-assembly", "d4-adapter", "d4-projection")}
    measurement["deterministic_regeneration"] = deterministic
    for label, code in deterministic.items():
        if code != 0:
            failures.append(f"the D4 {label} regeneration is not byte-identical (exit {code})")

    # ---- 5. the syllabify fix: one algorithm, forms re-verified
    gate_path = safe_path(ARGOT_GATE)
    gate_namespace = None
    if gate_path.is_file():
        try:
            gate_namespace = runpy.run_path(str(gate_path))
        except Exception as error:
            failures.append(f"the argot gate does not load: {type(error).__name__}: {error}")
    else:
        missing.append(ARGOT_GATE)
        failures.append(f"the argot gate is missing: {ARGOT_GATE}")

    forms = [(str(row.get("id")), str(row.get("term"))) for row in lexicon_records(packet)
             if row.get("term")]
    forms += [(str(row.get("id")), str(row.get("name"))) for row in name_records(packet)
              if row.get("name")]
    disagreements, illegal, design_rows = [], [], []
    if gate_namespace and "syllabify" in gate_namespace:
        gate_syllabify = gate_namespace["syllabify"]
        for fid, form in forms:
            try:
                observed = gate_syllabify(form)
            except Exception as error:
                disagreements.append({"id": fid, "form": form, "error": str(error)})
                continue
            expected = lawful_syllables(form, consonants, vowels, codas, clusters)
            if list(observed) != expected:
                disagreements.append({"id": fid, "form": form,
                                      "gate": list(observed), "lawful": expected})
            for item in illegal_syllables(list(observed), consonants, vowels, codas):
                illegal.append({"id": fid, "form": form, **item})
        base, expected_head2 = DESIGN_WORKED_HEAD2
        observed_head2 = "".join(gate_syllabify(base)[:2])
        design_rows.append({"form": base, "expected": expected_head2, "observed": observed_head2,
                            "agrees": observed_head2 == expected_head2})
        controls = [{"form": form, "expected": expected,
                     "observed": list(gate_syllabify(form)),
                     "agrees": list(gate_syllabify(form)) == expected}
                    for form, expected in SYLLABLE_CONTROLS]
        measurement["syllabify_fix"] = {
            "gate": ARGOT_GATE,
            "algorithm_declared": str(gate_namespace.get("syllabify", {}).__doc__ or "")[:200]
            if hasattr(gate_namespace.get("syllabify"), "__doc__") else None,
            "forms_checked": len(forms),
            "disagreements": len(disagreements),
            "disagreement_rows": disagreements[:15],
            "illegal_syllables": len(illegal),
            "illegal_rows": illegal[:10],
            "design_worked_row": design_rows,
            "controls": controls,
            "command": f"{COMMAND} (this runner's own lawful syllabifier vs the delivered gate's syllabify, every delivered form)",
            "date": today()}
        if disagreements:
            failures.append(f"the delivered gate's syllabify still disagrees with the design's "
                            f"stated algorithm on {len(disagreements)} of {len(forms)} delivered "
                            f"form(s): {disagreements[:3]}")
        if illegal:
            failures.append(f"the delivered gate emits {len(illegal)} illegal syllable(s) "
                            f"(no nucleus, onset cluster, or illegal coda): {illegal[:3]}")
        if not all(row["agrees"] for row in design_rows):
            failures.append(f"the gate does not reproduce the design's worked head2 row "
                            f"{DESIGN_WORKED_HEAD2[0]!r} -> {DESIGN_WORKED_HEAD2[1]!r}: {design_rows}")
        if not all(row["agrees"] for row in controls):
            failures.append(f"the gate does not reproduce this runner's legality-forced splits: "
                            f"{[row for row in controls if not row['agrees']]}")
    else:
        measurement["syllabify_fix"] = {"forms_checked": len(forms), "gate_loaded": False}
        failures.append("the argot gate exposes no `syllabify`: the algorithm cannot be verified")

    # ---- 6. the gates are green, the register leg among them
    coverage = parse_coverage_line(label_run(regressions, "argot-gate-d4").get("stdout"))
    ok, failed, passed, total = gate_legs(label_run(regressions, "d4-gate").get("stdout"))
    measurement["gates"] = {
        "argot_selftest_exit": runs.get("argot-gate-selftest", {}).get("exit"),
        "argot_d4_exit": runs.get("argot-gate-d4", {}).get("exit"),
        "argot_coverage": coverage,
        "typed_gate_legs": f"{passed}/{total}",
        "typed_gate_failed_legs": failed,
        "typed_gate_exit": runs.get("d4-gate", {}).get("exit"),
        "register_leg_present": bool(re.search(
            r"(?i)argot|register|" + "|".join(ARGOT_IDS), evidence.text(TYPED_GATE))),
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
    if not measurement["gates"]["register_leg_present"]:
        failures.append("the typed gate carries no argot/register leg")

    # ---- 7. the hold set carries a named round-27 revision and agrees with the projection
    holds = evidence.document(D4_HOLDS) or {}
    counts = holds.get("counts") or {}
    projection = evidence.document(D4_PROJECTION) or {}
    coverage_block = projection.get("coverage") or {}
    revision_note = str(holds.get("revision_note") or "")
    measurement["holds"] = {
        "path": D4_HOLDS, "counts": counts,
        "revision_note_head": revision_note[:220],
        "names_round_27": bool(re.search(r"(?i)round[- ]?27|r27", revision_note)),
        "supersedes_pins": bool(holds.get("supersedes_pins")),
        "projection_counts": {key: coverage_block.get(key) for key in
                              ("findings_total", "conflicts", "labels_by_kind")},
    }
    if not (holds.get("revision_note") or holds.get("supersedes_pins")):
        failures.append(f"the D4 hold set carries no revision note or supersession pin ({D4_HOLDS})")
    elif not measurement["holds"]["names_round_27"]:
        failures.append("the D4 hold set's revision note does not name the round-27 landing "
                        "(the claim requires the named holds updated)")
    if not counts:
        failures.append(f"the D4 hold set declares no counts ({D4_HOLDS})")
    else:
        if counts.get("fail"):
            failures.append(f"the D4 hold set carries {counts['fail']} fail row(s)")
        if counts.get("hold") != len(holds.get("holds") or []):
            failures.append(f"the D4 hold set declares hold={counts.get('hold')} but carries "
                            f"{len(holds.get('holds') or [])} rows")
    if coverage_block.get("conflicts"):
        failures.append(f"the projection reports {coverage_block['conflicts']} conflict(s)")

    # ---- 8. the round-27 D artifact names the landing, the fix and the delta
    artifacts = find_round_artifacts(("register", "law", "syllab", "argot", "stratum"))
    measurement["artifacts"] = [str(path.relative_to(ROOT)) for path in artifacts]
    if not artifacts:
        failures.append(f"no round-27 register/law/syllabify artifact landed under {ROUND_DIR}")
        missing.append(f"{ROUND_DIR} (D artifact)")
        return result(failures, measurement, missing)
    blob = "\n".join(evidence.text(str(path.relative_to(ROOT))) for path in artifacts)
    tokens = {
        "names_law": bool(re.search(r"(?i)register law|speech-act|RGL-\d|admissib", blob)),
        "names_syllabify": bool(re.search(r"(?i)syllabif", blob)),
        "names_disagreement": bool(re.search(r"(?i)\b\d+\s+of\s+\d+\b|disagree", blob)),
        "names_rl6": "RL-6" in blob,
        # The round-26 gap is filed under three ids (RD-4 in the design review,
        # RL-3 in the design's limits, RL-5 in the round-27 law review); any one
        # of them, or a citation of the round-26 review itself, names the gap.
        "names_the_round26_gap": bool(
            re.search(r"RD-4|\bRL-3\b|\bRL-5\b|reports/round-26/register/review", blob)),
        "carries_receipt": bool(re.search(r"(?i)\b(exit|selftest|receipt|executed|command)\b", blob)),
    }
    measurement["artifact_tokens"] = tokens
    for name, present in tokens.items():
        if not present:
            failures.append(f"the round-27 D artifact never records {name}")
    return result(failures, measurement, missing)


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
# Claim O — the D4 pin sweep
# --------------------------------------------------------------------------

PIN_SCAN_GLOBS = (
    "tools/gates/expected/**/*.json",
    "tools/gates/frozen/**/*.json",
    "tools/gates/frozen/**/*.tsv",
    "reports/round-20/**/*.json",
    "reports/round-22/**/*.json",
    "reports/round-26/**/*.json",
    TYPED_PROFILES,
    D4_HOLDS,
)


def is_d4_surface(path):
    return isinstance(path, str) and path.startswith(D4_DIR + "/") and PATHLIKE.match(path)


def digest_pairs(node, context=""):
    """(path, digest) pairs from any nested mapping: a key that names a repo
    path whose sibling value (or a `sha256`/`digest`/`hash` sub-key) is a
    sha256."""
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
    document = None
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


def round27_repin_rows():
    """Round-27 records that can close a drift: a structured row (JSON/YAML/TSV)
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

    repins = round27_repin_rows()
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
        failures.append(f"{len(drifted_surfaces)} D4 surface(s) drifted and no round-27 structured "
                        f"re-pin row landed: {drifted_surfaces[:6]}")
    elif unrepinned:
        failures.append(f"{len(unrepinned)} drifted D4 surface(s) are not re-pinned by a round-27 "
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

    # ---- the v3 baseline the tool actually reads, and the newest round-27
    # successor row. The tool's default is a constant inside it; read it live so
    # a re-point that moves the default is measured, not assumed.
    tool_text = evidence.text(HANDOFF)
    default_match = re.search(r'V3_BASELINE_DEFAULT\s*=\s*"([^"]+)"', tool_text)
    default_path = default_match.group(1) if default_match else V3_BASELINE_FALLBACK
    measurement["v3_baseline_default"] = {"path": default_path,
                                          "declared_in_tool": bool(default_match)}
    baseline = evidence.document(default_path)
    live_packet = sha(safe_path(PACKET_D4).read_bytes())
    if baseline is None:
        measurement["v3_baseline"] = {"path": default_path, "present": False,
                                      "live_packet_sha256": live_packet}
    else:
        declared = baseline.get("packet_sha256")
        measurement["v3_baseline"] = {
            "path": default_path, "present": True,
            "declared_packet_sha256": declared, "live_packet_sha256": live_packet,
            "reading": "green" if declared == live_packet else "drift",
            "profile": baseline.get("profile"),
        }
    successors = sorted(str(path.relative_to(ROOT)) for path in
                        safe_path(ROUND_DIR).rglob("**/expected.json")
                        if "v3" in path.parent.name or "handoff" in str(path.parent))
    measurement["v3_successor_rows"] = successors[:12]
    if not successors:
        failures.append("no round-27 v3 successor baseline row landed: the D4 law landing moved "
                        "the packet and the tool's default baseline is not re-pointed")
    # A red v3 replay names its own read-set drift; carry that verbatim so the
    # blocker is actionable rather than just "exit 1".
    v3_run = label_run(regressions, "handoff-v3")
    drift_lines = [line for line in ((v3_run.get("stdout") or "") +
                                     (v3_run.get("stderr") or "")).splitlines()
                   if "input-digest" in line or "E2E-DIGEST" in line]
    measurement["v3_replay"] = {
        "exit": v3_run.get("exit"),
        "default_baseline": default_path,
        "drift_lines": drift_lines[:10],
        "blocker": ("the tool's default v3 baseline is not re-pointed to a post-law successor "
                    "row" if v3_run.get("exit") != 0 else None),
    }
    # The successor row the sweep landed is replayed against its own baseline: a
    # green successor with a stale default is a re-point that was written but not
    # wired, and the difference is exactly what the O seat still owes.
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
        failures.append("the v3 replay is red and no round-27 successor baseline replays green: "
                        "the re-point is missing, not merely unwired")
    elif v3_run.get("exit") != 0:
        failures.append(f"the tool's default v3 baseline ({default_path}) is not re-pointed to the "
                        f"green round-27 successor {green_successors[0]}: the default pointer is the "
                        f"remaining O surface")

    # ---- auditors: the round-27 independent audit seats on the sweep surface.
    # The O claim's acceptance names auditors; a sweep with no independent
    # reading of its own completeness is an assertion, not a measured surface.
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
        "rows_total": metric(len(auditors), "round-27 audit reports on the sweep surface"),
        "rows": auditors[:12],
    }
    sweep_auditors = [row for row in auditors if row["names_a_sweep"] and row["carries_a_receipt"]]
    measurement["auditors"]["sweep_auditors"] = len(sweep_auditors)
    if not sweep_auditors:
        failures.append(f"no round-27 auditor report reads the sweep surface under {ROUND_DIR}/audit "
                        f"(the O acceptance names auditors)")

    # ---- regressions
    measurement["regressions"] = regressions["measurement"]
    failures.extend(regressions["failures"])
    return result(failures, measurement, missing)


# --------------------------------------------------------------------------
# Claim C — the register-strata knowledge entry and the corpus README
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


def measure_register_entry(evidence):
    failures, measurement, missing = [], {}, []

    claims = evidence.document(CLAIMS) or {}
    baseline_revision = claims.get("baseline_revision")
    baseline_names = baseline_entry_names(baseline_revision)
    live_entries = sorted(path.name for path in safe_path(LINGUISTICS_DIR).glob("*.md"))
    measurement["baseline"] = {
        "revision": baseline_revision,
        "linguistics_entries_at_baseline": len(baseline_names) if baseline_names is not None else None,
        "linguistics_entries_live": len(live_entries),
    }
    if baseline_names is None:
        failures.append("cannot read the declared baseline's linguistics partition "
                        "(the entry's newness cannot be established)")
        missing.append(f"{LINGUISTICS_DIR} (baseline)")

    new_entries = []
    for name in live_entries:
        if baseline_names is not None and f"{LINGUISTICS_DIR}/{name}" not in baseline_names:
            new_entries.append(name)
    measurement["new_entries"] = new_entries
    if not new_entries:
        failures.append(f"no new entry landed under {LINGUISTICS_DIR} (absent from the declared "
                        f"baseline): the register-strata craft is still only in round artifacts")
        missing.append(f"{LINGUISTICS_DIR} (new entry)")
        return result(failures, measurement, missing)

    # The entry that carries the register-strata subject: scored by the subject
    # tokens in its own frontmatter and body.
    def subject_score(name):
        text = evidence.text(f"{LINGUISTICS_DIR}/{name}")
        head = text[:4000].lower()
        score = sum(token in head for token in
                    ("register", "stamp", "attestation", "speech-act", "stratum", "strata"))
        return score, text

    scored = sorted(((subject_score(name)[0], name, subject_score(name)[1])
                     for name in new_entries), key=lambda item: item[0])
    score, entry_name, text = scored[-1]
    relative = f"{LINGUISTICS_DIR}/{entry_name}"
    measurement["entry"] = {
        "path": relative, "bytes": len(text.encode("utf-8")), "subject_score": score,
        "sha256": sha(safe_path(relative).read_bytes()) if safe_path(relative).is_file() else None,
    }
    if score == 0:
        failures.append(f"the new entry {relative} never names the register/attestation subject")

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
        failures.append(f"the entry {relative} names no round-26/27 artifact: it is not grounded in "
                        f"the work it records")
    if len(citations) < 3:
        failures.append(f"the entry {relative} carries {len(citations)} dated source token(s); a "
                        f"sourced entry needs cited external sources")
    if not GAP_NAMED_RE.search(text):
        failures.append(f"the entry {relative} does not name the gap it fills")
    if not DECISION_RECORD_RE.search(text):
        failures.append(f"the entry {relative} carries no decision record")
    if CANON_CLAIM_RE.search(text):
        failures.append(f"the entry {relative} makes a canon claim (out of province for this lane)")

    # ---- the corpus README reconciled
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
        "total_files": sum(counts.values()),
    }
    if not revisions:
        failures.append(f"{CORPUS_README} carries no `revision:` line")
    if entry_name not in readme:
        failures.append(f"{CORPUS_README} does not index the new entry {entry_name}")
    if mismatches:
        failures.append(f"{CORPUS_README}'s partition headers disagree with the tree: {mismatches}")
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


def selftest():
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    cons = {"p", "t", "k", "m", "n", "s", "r", "l", "h"}
    vows = {"a", "e", "i", "o", "u"}
    codas = {"n", "m", "s", "k", "l", "r", "t", "d"}

    # the lawful algorithm: the design's stated rule, legality-constrained
    check("lawful-saalumi-is-saa-lu-mi",
          lawful_syllables("saalumi", cons, vows, codas) == ["saa", "lu", "mi"],
          observed=lawful_syllables("saalumi", cons, vows, codas))
    check("lawful-head2-saalumi-is-saalu",
          "".join(lawful_syllables("saalumi", cons, vows, codas)[:2]) == "saalu")
    check("lawful-tikmes-splits-by-legality",
          lawful_syllables("tikmes", cons, vows, codas) == ["tik", "mes"],
          observed=lawful_syllables("tikmes", cons, vows, codas))
    check("lawful-kalker-splits-by-legality",
          lawful_syllables("kalker", cons, vows, codas) == ["kal", "ker"])
    check("lawful-final-coda-closes-the-syllable",
          lawful_syllables("tum", cons, vows, codas) == ["tum"],
          observed=lawful_syllables("tum", cons, vows, codas))
    check("lawful-doubled-vowel-is-one-nucleus",
          lawful_syllables("tuum", cons, vows, codas) == ["tuum"])
    check("lawful-never-emits-a-bare-consonant",
          not any(len(syllable) == 1 and syllable not in vows
                  for syllable in lawful_syllables("kalker", cons, vows, codas)))
    check("simple-syllables-is-the-old-reading",
          simple_syllables("tikmes", vows) == ["ti", "kme", "s"],
          observed=simple_syllables("tikmes", vows))
    check("simple-vs-lawful-differ-on-a-legal-word",
          simple_syllables("tikmes", vows) != lawful_syllables("tikmes", cons, vows, codas))
    check("illegal-syllable-detector-finds-a-cluster",
          illegal_syllables(["ti", "kme", "s"], cons, vows, codas)
          and all(item["reason"] for item in illegal_syllables(["ti", "kme", "s"], cons, vows, codas)),
          observed=illegal_syllables(["ti", "kme", "s"], cons, vows, codas))
    check("illegal-syllable-detector-finds-a-bare-consonant",
          any(item["reason"] == "no nucleus"
              for item in illegal_syllables(["s"], cons, vows, codas)))
    check("illegal-syllable-detector-passes-a-legal-word",
          not illegal_syllables(["saal", "um", "i"], cons, vows, codas))

    # argot operations
    check("argot-reverse-makun", argot_apply("makun", "reverse") == "nukam")
    check("argot-reverse-agrees-with-design", not argot_selfcheck(), mismatches=argot_selfcheck()[:3])
    check("argot-unknown-operation-refused", _raises(argot_apply, "min", "nope"))
    check("operation-string-normalizes", normalize_operation("REVERSE") == "reverse")
    check("operation-mapping-normalizes",
          normalize_operation({"op": "head2", "base": "saalumi"}) == "head2")
    check("operation-unknown-is-none", normalize_operation({"weird": 1}) is None)
    check("base-from-mapping", normalize_base({"base": "min"}, "min") == "min")

    coverage = parse_coverage_line(
        "coverage: examples/x.yml records=170 register_scoped=14 derived_pairs=8 "
        "claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0")
    check("coverage-line-parse", coverage == {"records": 170, "register_scoped": 14,
                                              "derived_pairs": 8, "claimed_chains": 8,
                                              "borrow_pairs": 6, "violations": 0,
                                              "rule_holds": 0}, observed=coverage)
    check("coverage-line-absent-is-none", parse_coverage_line("no coverage here") is None)

    # the law clause detector: each clause fires on its own text and not on the others
    clause = law_clause_coverage("admissible only in a stamp-act slot")
    check("law-clause-admissibility", clause["admissibility"] and not clause["agent"]
          and not clause["consequence"], observed=clause)
    clause = law_clause_coverage("a guest broker may speak stamp under a stamp-name")
    check("law-clause-agent", clause["agent"] and not clause["admissibility"], observed=clause)
    clause = law_clause_coverage("an oath spoken in stamp is void; the plain word binds")
    check("law-clause-consequence", clause["consequence"] and not clause["agent"], observed=clause)
    check("law-clause-none-on-empty", not any(law_clause_coverage("").values()))
    check("law-rule-id-recognised", REGISTER_LAW_ID_RE.findall("RGL-01 QREG-02 REG-03"))

    # pin-row digest extraction
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

    # frontmatter / README parsers
    entry = ("# X\n- topic: t\n- sources: A 2010\n- verified-at: 2026-10-18\n"
             "- recheck: y\n- couples: z\n")
    check("frontmatter-complete", all(pattern.search(entry) for pattern in FRONTMATTER.values()))
    check("frontmatter-detects-a-miss",
          not FRONTMATTER["recheck"].search("# X\n- topic: t\n"))
    check("partition-header-parsed",
          PARTITION_HEADER_RE.findall("## linguistics/ (19)\n## synthesis/ (29)\n")
          == [("linguistics", "19"), ("synthesis", "29")])
    check("revision-parsed", REVISION_RE.findall("revision: 1.6 — Round-27\n") == ["1.6"])
    check("round-artifact-path-parsed",
          ROUND_ARTIFACT_RE.findall("see reports/round-26/register/impl.md") ==
          ["reports/round-26/register/impl.md"])
    check("canon-claim-detected", bool(CANON_CLAIM_RE.search("this is canon now")))
    check("canon-claim-absent-on-a-design-record", not CANON_CLAIM_RE.search("a NON-CANON design"))

    check("legs-parsed-off-a-gate-run", gate_legs(
        "ok   L3-build\nFAIL L3-routing-consistency\nsummary: 1/2 legs passed\n")
        == (["L3-build"], ["L3-routing-consistency"], 1, 2))
    check("protected-covers-round-26", "reports/round-26" in PROTECTED)
    check("protected-stops-at-round-26", "reports/round-27" not in PROTECTED)

    passed_controls = sum(1 for item in controls if item["passed"])
    for item in controls:
        print(("ok   " if item["passed"] else "FAIL ") + item["control"]
              + ("" if item["passed"] else f" — {item}"))
    print(f"selftest: {passed_controls}/{len(controls)} checks passed — the runner's own lawful "
          "syllabifier against the design's stated rule and its worked row, the pre-fix reading as "
          "the control, the argot operations, the law-clause and pin-row parsers, the frontmatter "
          "and partition-header readers; no file opened for writing")
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
            ("D", lambda: measure_register_law(evidence, regressions)),
            ("O", lambda: measure_pin_sweep(evidence, regressions)),
            ("C", lambda: measure_register_entry(evidence))):
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
    if claims.get("round") != 27 or targets.get("round") != 27:
        coherence.append("Claims/targets are not both round 27")
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
    return {"round": 27, "runner": RUNNER, "runner_sha256": sha(safe_path(RUNNER).read_bytes()),
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
                "Claim D is measured from the delivered bytes: the packet's `registers` block and its declaring component, the law's clause coverage and rule ids, the three byte-identical regenerations, this runner's own lawful syllabifier against the delivered gate's `syllabify` on every delivered form (never read back from the gate as the source of truth), the design's one worked head2 row, the gate exits, the hold set's named revision, and the round-27 artifact's receipt. The delivered implementation's shape (which component owns the law, which field names each clause) is deliberately not pinned beyond what the claim names.",
                "The syllabifier is graded against this runner's own reading of `design-language.md` §5 (legality-constrained maximal onset) and the packet's own inventory. If a landing implements a different but equivalent algorithm it still passes as long as it agrees on every delivered form, reproduces the design's worked row, and never emits an illegal syllable; a disagreement is reported form by form.",
                "Claim O is measured as one sweep over every row that pins a D4 surface: the frozen manifests, the battery baselines, the typed-pipeline profile, the hold set, the v3 read-set baseline and the historical round-20/22/26 rows. A declared digest equal to the live bytes reads `green`; a mismatch reads `drift` and must be re-pinned by a NEW round-27 row that names the surface and carries the live digest. Filed rounds 8-26 stay byte-identical; a drift in a filed historical row is recorded, never repaired in place.",
                "Claim O's pin surface is baseline-relative and the tree moves under it: a row re-pinned before a later landing goes stale again. The sweep reports the drift it measured at measurement time; it does not assert that no drift will appear later.",
                "Claim C requires a NEW linguistics entry: absent from the declared baseline revision by Git blob identity. The entry must be frontmatter-complete, name the gap, carry a decision record, be grounded in round-26/27 artifacts and dated external sources, and make no canon claim. corpus/README.md must index it and its partition headers must reproduce the measured tree.",
                "Protected reports and frozen generations of rounds 8-26 must match the round-27 declared baseline; new round-27 files live under reports/round-27, corpus/knowledge and corpus/README.md.",
            ]}


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def dependencies_ready():
    """The artifacts the three claims depend on. Used only by --wait."""
    wanted = [f"{ROUND_DIR}/register", f"{ROUND_DIR}/pins", f"{ROUND_DIR}/sweep",
              f"{ROUND_DIR}/entries"]
    return [path for path in wanted if not (safe_path(path).exists())]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Measure round-27 D/O/C acceptance; run in the lane root or an isolated clone.")
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
