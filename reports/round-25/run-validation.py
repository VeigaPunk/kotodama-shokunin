#!/usr/bin/env python3
"""Round-25 acceptance runner: claims O (operability), D (depth), C (coverage).

Claim O — the two round-24 cold-run hazards plus regressions:
  (a) **gate-input honesty.** The round-24 cold run measured that feeding the
      gate its own derived artifact (`examples/culture-d4/packet.d4.typed.yml`)
      exits 1 with 14/16 legs and realistic-looking failures — eight
      `DERIV-REPLAY` FAILs on `L2-channel` and a false
      `L3-routing-consistency` FAIL whose "routing" list is six `null`s
      (`reports/round-24/cold-run-conditions.md` C2). The typed artifact is the
      chain's *output*, not a gate input, so that red is manufactured, not
      found. The fix must make the gate fail closed and honestly on derived
      input: either a named input-class diagnostic (exit 2), or L2/L3 handling
      a nullish routing scalar correctly — either way feeding the typed packet
      back can no longer manufacture a finding. This runner measures the
      behaviour, not an implementation: the typed-packet invocation must land
      in {0, 2}, must emit no `DERIV-REPLAY` FAIL and no
      `L3-routing-consistency` FAIL, and — the teeth — the documented
      source-packet entry must still pass its canonical leg count while a
      tampered expectation and a corrupted packet must still be refused.
  (b) **v3 supersession.** Handoff v3's claim prose still described the
      removed D4 rank passengers (D4-CL05/06/07/09; OQ-V3-05), while the live
      D4 projection is family-clean (12 holds / 0 notes / 0 conflicts / 0
      quarantine handles / 0 unresolved rank items). A superseding revision
      must land as a **new row** with the corrected prose; the filed round-20
      and round-22 bytes stay untouched. This runner locates the new row,
      re-reads the four claim rows and the OQ, and fails on any surviving
      stale passenger description unless the row explicitly marks it
      superseded/historical.
  (c) the fixed regression battery is green.

Claim D — the round-17 argot-derivation forecast, delivered or its delta named.
  `reports/round-17/d4/design-brief.md` §6 Δ3 (`:296-315`) forecast
  derivation-checked quote forms: two declared operations, `head2` (first two
  syllables, maximal-onset) and `reverse` (character reversal), checked as a
  relation between two records of the same packet, with a violating form
  yielding `D4L-ARGOT-DERIV` (control-only; the delivered packet carries no
  such row). `reports/round-19/knowledge/analyst-3.md` §3 marked it
  design-forecast, not delivered. The claim requires the leg implemented and
  executed on D4 and any forecast element not delivered **named** rather than
  silently dropped. Delivered shape (measured 2026-10-18): the leg landed as a
  standalone sibling gate `tools/gates/argot-derivation-gate.py` (selftest
  18/18, canonical D4 run exit 0), *not* inside `tools/gates/typed-pipeline-gate.py`;
  the delivered D4 packet declares no `derived_from`/`derivation` pair, so the
  leg replays the register-scoped and borrowed records it does have. This runner
  measures the artifact, the gate's own selftest, the canonical D4 run, a
  runner-authored violating-form control and its clean counterpart, and the
  delta's naming of the sibling-gate substitution — and, independently from its
  own implementation, replays the two declared operations against the eleven
  worked derivations the design fixes.

Claim C — `corpus/lessons/README.md` reconciled. The lessons partition holds
  24 Markdown files across three census formats (gate-keeper surveys, X24/X28
  fragment indexes, plain lessons) and no index. The README must carry a
  per-file row, the open-question queue with an owner per item, the three
  formats documented, and a counting command that reproduces the file count.

Run only in an isolated Git clone under the lane's .scratch, as
  python3 reports/round-25/run-validation.py            (measure + write receipt)
  python3 reports/round-25/run-validation.py --check    (measure only, print)
  python3 reports/round-25/run-validation.py --selftest (dependency-free controls)
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

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-25"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
CLAIMS = f"{ROUND_DIR}/claims.json"
TARGETS = f"{ROUND_DIR}/targets.json"
ARGOT_DIR = f"{ROUND_DIR}/argot"
LESSONS_README = "corpus/lessons/README.md"
LESSONS_DIR = "corpus/lessons"
GATE = "tools/gates/typed-pipeline-gate.py"
D4_SOURCE = "examples/culture-d4/packet.d4.yml"
D4_TYPED = "examples/culture-d4/packet.d4.typed.yml"
D4_HOLDS = "examples/culture-d4/expected-holds.json"
D4_PROJECTION = "examples/culture-d4/typed-labels.d4.yml"
V3_TWIN_OLD = "reports/round-22/handoff/declared-in-r2/twin.json"
SYNC_PATHS = (ROUND_DIR, "SKILL.md", "LOG.md", "SCORECARD.md", "PROVINCE.md",
              "SHONEN.md", "corpus", "examples", "tools")
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 25)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 25))

# The stale passenger prose the round-22 bleed review named as wrong in the
# filed v3 claim map (reports/round-22/bleed/repin.md:26-37) and the live
# family-clean values that supersede it (measured 2026-10-18). A token is only
# a defect when it sits in a sentence that neither marks the state as
# superseded/historical nor negates it — the corrected prose legitimately
# quotes the old numbers to say they are gone.
STALE_PASSENGER_TOKENS = (
    "16 findings", "15 hold-or-fail", "15 are hold-or-fail", "15 holds",
    "three d2l-rank holds", "one d2l-rank note", "d2l-rank rows",
    "13 unresolved rank", "three quarantine handles", "four conflicts",
)
SUPERSEDED_MARKERS = ("superseded", "pre-fix", "historical", "former revision",
                      "pre-repair", "pre-family-clean", "no longer", "removed",
                      "erratum", "not resolved", "stay open", "were not resolved",
                      "inherited", "generation", "rather than", "instead of")
CLEAN_ANCHORS = ("12 holds", "hold 12", "note 0", "0 notes", "findings_total 12",
                 "12 findings", "zero")
CLEAN_HOLDS = {"hold": 12, "note": 0, "fail": 0}
CLEAN_COVERAGE = {"findings_total": 12, "conflicts": 0, "rank_quarantine_handles": 0,
                  "rank_rules_unresolved_items": 0, "reconciliation_records": 6,
                  "typed_labels": 74, "findings_hold_or_fail": 12, "label_findings_fail": 0}
ARGOT_ID = "D4L-ARGOT-DERIV"
# design-language.md section 5, the eleven worked derivations, pinned by hand
# (this runner re-derives them from its own implementation, never from the doc).
ARGOT_WORKED = (
    ("saalumi", "head2", "saalu"), ("min", "reverse", "nim"),
    ("kus", "reverse", "suk"), ("nam", "reverse", "man"),
    ("nes", "reverse", "sen"), ("sam", "reverse", "mas"),
    ("mus", "reverse", "sum"), ("kin", "reverse", "nik"),
    ("sun", "reverse", "nus"), ("samun", "reverse", "numas"),
    ("makun", "reverse", "nukam"),
)
LESSONS_ROW_RE = re.compile(
    r"(?m)^\|\s*`?(?:corpus/lessons/)?([A-Za-z0-9_.-]+\.md)`?\s*\|")
LESSONS_ROUND_ROW_RE = re.compile(r"(?m)^\|\s*`?round-(\d+)`?\s*\|")
CENSUS_FORMATS = ("gate-keeper", "fragment-index", "plain")
OWNER_RE = re.compile(r"(?i)\bowner\b\s*[:=]?\s*`?([A-Za-z0-9][\w./ -]{0,60})")
COUNT_COMMAND_RE = re.compile(r"`([^`\n]*(?:ls|find|wc)[^`\n]*)`")
ROWS_DECLARED_RE = re.compile(r"(?i)\brows?\s*[:=]\s*\**\s*(\d{1,3})")
FILES_DECLARED_RE = re.compile(r"(?i)\bfiles?\s*[:=]\s*\**\s*(\d{1,3})")

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
    ("d4-adapter", ("tools/assemble-d4-typed.py", "--check", D4_TYPED)),
    ("projector-selftest", ("tools/d2-typed-labels.py", "--selftest")),
    ("d2-projection", ("tools/d2-typed-labels.py", "--check")),
    ("d4-projection", ("tools/d2-typed-labels.py", "--packet", D4_SOURCE,
                       "--check", D4_PROJECTION)),
    ("typed-pipeline-selftest", (GATE, "--selftest")),
    ("typed-pipeline-generalized-selftest", (GATE, "--selftest-generalized")),
    ("d2-gate", (GATE,)),
    ("d4-gate", (GATE, D4_SOURCE)),
    ("d4-label-gate", ("tools/gates/d4-typed-labels-check-gate.py",)),
    ("d4-label-gate-selftest", ("tools/gates/d4-typed-labels-check-gate.py", "--selftest")),
    ("d4-assembly-gate", ("tools/gates/d4-assembly-check-gate.py", D4_SOURCE)),
    ("coupling-selftest", ("tools/check-evidence-coupling.py", "--selftest")),
    ("replay-selftest", ("tools/replay-frozen.py", "--selftest")),
    ("handoff-gate-selftest", ("tools/gates/handoff-packet-check.py", "--selftest")),
    ("links-selftest", ("tools/harness/packet_links.py", "--selftest")),
    ("uncertainty-selftest", ("tools/harness/packet_uncertainty.py", "--selftest")),
    ("receipt-guard-selftest", ("tools/harness/receipt_guard.py", "--selftest")),
    ("argot-gate-selftest", ("tools/gates/argot-derivation-gate.py", "--selftest")),
    ("argot-gate-d4", ("tools/gates/argot-derivation-gate.py", D4_SOURCE)),
    ("handoff-v2", ("tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet")),
    ("handoff-v3-selftest", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest")),
    ("handoff-v3", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet")),
)
LEG_RE = re.compile(r"^(ok|FAIL)\s+([A-Za-z0-9_.-]+)")
SUMMARY_RE = re.compile(r"summary:\s*(\d+)/(\d+)\s+legs passed")


def today():
    return dt.date.today().isoformat()


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
        return result(["Round-25 declared baseline is not a full Git revision"], {})
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
        failures.append("Filed rounds 8-24 or their frozen generations differ from the declared baseline")
    return result(failures, {"baseline_revision": revision,
                             "protected_paths": metric(len(expected), "git ls-tree of protected baseline"),
                             "differences": rows[:20],
                             "differences_total": metric(len(rows), "compare protected Git blobs to working bytes"),
                             "protected_status_rows": metric(len(worktree), "git status over protected paths")})


def run_command(label, parts, timeout=900):
    scratch = ROOT / ".scratch" / "round-25" / "validation" / label
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
# Claim O — gate-input honesty, v3 supersession
# --------------------------------------------------------------------------

def measure_gate_input(evidence):
    """The typed-packet invocation must not manufacture findings; the canonical
    source entry must still pass, and the gate must still refuse bad input."""
    failures, measurement, missing = [], {}, []

    src = run_command("gate-source", (GATE, D4_SOURCE))
    typed = run_command("gate-typed", (GATE, D4_TYPED))
    measurement["source_packet"] = {"command": src["command"], "date": src["date"],
                                    "exit": src.get("exit")}
    measurement["derived_packet"] = {"command": typed["command"], "date": typed["date"],
                                     "exit": typed.get("exit")}
    if src.get("exit") != 0:
        failures.append(f"the documented source-packet entry no longer passes: "
                        f"{src['command']} exit {src.get('exit')}")
        missing.append(D4_SOURCE)
    else:
        ok, failed, passed, total = gate_legs(src.get("stdout") or "")
        measurement["source_packet"].update(legs_passed=passed, legs_total=total, failed_legs=failed)
        if failed or passed != total or total < 16:
            failures.append(f"the source-packet entry reports {passed}/{total} legs "
                            f"(failed: {failed})")

    ok, failed, passed, total = gate_legs(typed.get("stdout") or "")
    text = (typed.get("stdout") or "") + (typed.get("stderr") or "")
    deriv = [line.strip() for line in (typed.get("stdout") or "").splitlines()
             if "DERIV-REPLAY" in line]
    measurement["derived_packet"].update(legs_passed=passed, legs_total=total,
                                         failed_legs=failed,
                                         deriv_replay_lines=len(deriv),
                                         nullish_routing=bool(re.search(r"routing \[[^\]]*'null'", text)))
    if typed.get("exit") not in (0, 2):
        failures.append(f"feeding the derived packet back still exits {typed.get('exit')} "
                        f"({passed}/{total} legs): the gate reports a red it did not find")
    if deriv:
        failures.append(f"the derived-packet run still manufactures {len(deriv)} DERIV-REPLAY "
                        f"FAIL line(s): {deriv[0][:100]!r}")
    if "L3-routing-consistency" in failed:
        failures.append("the derived-packet run still fails L3-routing-consistency "
                        "(a nullish routing scalar read as a mismatch)")
    if typed.get("exit") == 2 and not re.search(r"(?i)input|derived|typed packet|source packet|"
                                                r"grade the source|could-not-evaluate", text):
        failures.append("the derived-packet run exits 2 without a named input-class diagnostic")

    # Teeth: a corrupted packet and a tampered expectation must still be refused.
    scratch = ROOT / ".scratch" / "round-25" / "validation" / "gate-controls"
    scratch.mkdir(parents=True, exist_ok=True)
    broken = scratch / "broken.d4.yml"
    source_bytes = safe_path(D4_SOURCE).read_bytes()
    broken.write_bytes(b"\n".join(source_bytes.splitlines()[:40]) + b"\n")
    control_broken = run_command("gate-broken", (GATE, str(broken.relative_to(ROOT))))
    measurement["control_corrupted_packet"] = {"command": control_broken["command"],
                                               "date": control_broken["date"],
                                               "exit": control_broken.get("exit")}
    if control_broken.get("exit") == 0:
        failures.append("control: a truncated packet is graded green (the gate lost its teeth)")

    # A tampered expectation (a hold detail changed) must move the verdict.
    holds = evidence.document(D4_HOLDS) or {}
    tamper_dir = scratch / "tamper"
    tamper_dir.mkdir(parents=True, exist_ok=True)
    holds_path = tamper_dir / "expected-holds.json"
    mutated = json.loads(json.dumps(holds))
    rows = mutated.get("holds") or []
    if rows:
        rows[0]["detail"] = str(rows[0].get("detail", "")) + " [runner tamper control]"
    holds_path.write_text(json.dumps(mutated, indent=1) + "\n", encoding="utf-8")
    control_tamper = run_command(
        "gate-tamper", (GATE, "--expected", str(holds_path.relative_to(ROOT)), D4_SOURCE))
    measurement["control_tampered_expectation"] = {"command": control_tamper["command"],
                                                   "date": control_tamper["date"],
                                                   "exit": control_tamper.get("exit")}
    if control_tamper.get("exit") == 0:
        failures.append("control: a tampered expected-holds file still grades green")
    if not rows:
        failures.append(f"cannot build the tamper control: {D4_HOLDS} carries no holds")

    return result(failures, measurement, missing)


def find_v3_successor():
    """The new superseding v3 row: a directory under reports/round-25 carrying a
    revision packet plus its declared-identity baseline. The round-25 row is a
    claim-prose revision (`declared-in-r4/packet.md` + `expected.json`); the
    renderer-emitted twin row shape is also accepted."""
    base = safe_path(ROUND_DIR)
    candidates = []
    for path in sorted(base.rglob("packet.md")):
        directory = path.parent
        if (directory / "expected.json").is_file():
            candidates.append(directory)
    return candidates


def _sentences(text):
    return re.split(r"(?<=[.;:])\s+", text)


def stale_sentences(text):
    """Stale passenger prose that no sentence marks superseded.

    The corrected prose legitimately quotes the removed numbers to say they are
    gone; a sentence that marks the state as superseded/historical/pre-repair
    is exonerate. Only an *undispositioned* sentence — a stale token with no
    such marker — is a defect.
    """
    bad = []
    for sentence in _sentences(text):
        low = sentence.lower()
        hits = [token for token in STALE_PASSENGER_TOKENS if token.lower() in low]
        if not hits:
            continue
        if any(marker in low for marker in SUPERSEDED_MARKERS):
            continue
        bad.append({"tokens": hits, "sentence": sentence.strip()[:200]})
    return bad


def stale_tokens_in(text):
    return sorted({token for item in stale_sentences(text) for token in item["tokens"]})


def claim_rows_from_packet(text):
    """Markdown ledger rows keyed by claim id (the renderer's delivered shape)."""
    rows = {}
    for match in re.finditer(r"(?m)^\|\s*(D[24]-CL\d\d)\s*\|.*$", text):
        rows[match.group(1)] = match.group(0)
    return rows


def measure_v3_supersession(evidence):
    failures, measurement, missing = [], {}, []
    live_holds = evidence.document(D4_HOLDS) or {}
    live_projection = evidence.document(D4_PROJECTION) or {}
    counts = live_holds.get("counts") or {}
    coverage = live_projection.get("coverage") or {}
    measurement["live_family_clean_state"] = {"expected_holds_counts": counts,
                                              "projection_coverage": coverage,
                                              "command": f"{COMMAND} (live D4 family-clean read)",
                                              "date": today()}
    if counts != CLEAN_HOLDS:
        failures.append(f"the live D4 expectation is not the family-clean state: {counts} != {CLEAN_HOLDS}")
    for key, value in CLEAN_COVERAGE.items():
        if coverage.get(key) != value:
            failures.append(f"the live D4 projection {key} is {coverage.get(key)!r}, expected {value}")

    old_text = evidence.text(V3_TWIN_OLD)
    if not old_text:
        missing.append(V3_TWIN_OLD)
    old_stale = stale_tokens_in(old_text)
    measurement["filed_predecessor"] = {"path": V3_TWIN_OLD,
                                        "stale_tokens_present": old_stale,
                                        "note": "filed bytes stay as filed; staleness here is historical, not a failure"}

    candidates = find_v3_successor()
    measurement["successor_candidates"] = [str(path.relative_to(ROOT)) for path in candidates]
    if not candidates:
        failures.append("no superseding v3 row landed under reports/round-25 "
                        "(expected a directory with a revision packet.md + expected.json)")
        missing.append(f"{ROUND_DIR} (successor v3 row)")
        return result(failures, measurement, missing)

    directory = candidates[-1]
    packet_text = evidence.text(str((directory / "packet.md").relative_to(ROOT)))
    expected = evidence.document(str((directory / "expected.json").relative_to(ROOT))) or {}
    rows = claim_rows_from_packet(packet_text)
    watched = ("D4-CL05", "D4-CL06", "D4-CL07", "D4-CL09")
    measurement["successor_row"] = {"path": str(directory.relative_to(ROOT)),
                                    "revision": expected.get("revision"),
                                    "packet_sha256": expected.get("packet_sha256"),
                                    "parent": expected.get("parent"),
                                    "claims_seen": len(rows)}
    if not rows:
        failures.append("the successor revision packet carries no claim ledger rows")
    per_row = {}
    for claim_id in watched:
        row = rows.get(claim_id)
        if row is None:
            failures.append(f"the successor revision carries no {claim_id} row")
            continue
        bad = stale_sentences(row)
        clean = any(anchor in row.lower() for anchor in CLEAN_ANCHORS)
        per_row[claim_id] = {"undispositioned_stale_sentences": bad[:3],
                             "states_family_clean_value": clean}
        for item in bad:
            failures.append(f"{claim_id} still states the removed passengers "
                            f"({', '.join(item['tokens'])}) in an undispositioned sentence: "
                            f"{item['sentence'][:120]!r}")
        if not clean:
            failures.append(f"{claim_id} states no family-clean value "
                            f"(one of {CLEAN_ANCHORS[:4]}…)")
    measurement["claim_rows"] = per_row

    for claim_id, row in rows.items():
        if claim_id in watched:
            continue
        if not claim_id.startswith("D4-"):
            continue  # the stale-passenger prose is a D4-ownership question; D2's own
            #           live bytes legitimately carry 16 findings / 15 hold-or-fail
        for item in stale_sentences(row):
            failures.append(f"{claim_id} carries undispositioned passenger prose "
                            f"({', '.join(item['tokens'])})")

    oq_match = re.search(r"(?m)^-\s*OQ-V3-05:.*$", packet_text)
    measurement["oq_v3_05"] = None
    if oq_match:
        bad = stale_sentences(oq_match.group(0))
        measurement["oq_v3_05"] = {"undispositioned_stale_sentences": bad[:3],
                                   "disposition_marked": bool(SUPERSEDED_MARKERS and any(
                                       marker in oq_match.group(0).lower()
                                       for marker in SUPERSEDED_MARKERS))}
        for item in bad:
            failures.append(f"OQ-V3-05 still carries the removed passengers "
                            f"({', '.join(item['tokens'])}) without a disposition: "
                            f"{item['sentence'][:120]!r}")
    else:
        measurement["oq_v3_05"] = {"disposition": "absent from the successor packet (dropped as resolved)"}

    # The revision must be a new row: its own digest, a named parent, and the
    # parent's bytes unchanged.
    parent = expected.get("parent") or {}
    if not isinstance(parent, dict) or not parent.get("path"):
        failures.append("the successor row declares no parent revision (a supersession names its parent)")
    else:
        parent_path = parent["path"]
        try:
            observed = sha(safe_path(parent_path).read_bytes())
        except (OSError, ValueError):
            failures.append(f"the successor row's declared parent does not resolve: {parent_path}")
            observed = None
        measurement["parent_binding"] = {"path": parent_path,
                                         "declared_sha256": parent.get("sha256"),
                                         "observed_sha256": observed}
        if observed is not None and parent.get("sha256") and observed != parent["sha256"]:
            failures.append("the successor row's parent digest does not match the parent's live bytes "
                            "(the filed parent must stay untouched and pinned)")
    successor_sha = expected.get("packet_sha256")
    observed_successor = sha(safe_path(str((directory / "packet.md").relative_to(ROOT))).read_bytes())
    measurement["successor_pin"] = {"declared": successor_sha, "observed": observed_successor}
    if successor_sha and successor_sha != observed_successor:
        failures.append("the successor row pins a packet digest that does not match its own bytes")
    return result(failures, measurement, missing)


def measure_operability(evidence, regressions):
    failures, measurement, missing = [], {}, []
    gate_input = measure_gate_input(evidence)
    measurement["gate_input_honesty"] = gate_input["measurement"]
    failures.extend(f"gate-input: {item}" for item in gate_input["failures"])
    missing.extend(gate_input["missing_dependencies"])
    supersession = measure_v3_supersession(evidence)
    measurement["v3_supersession"] = supersession["measurement"]
    failures.extend(f"v3-supersession: {item}" for item in supersession["failures"])
    missing.extend(supersession["missing_dependencies"])
    measurement["regressions"] = regressions["measurement"]
    failures.extend(regressions["failures"])
    return result(failures, measurement, missing)


# --------------------------------------------------------------------------
# Claim D — the argot-derivation checking leg
# --------------------------------------------------------------------------

def syllabify(word):
    """Maximal-onset syllabification: a consonant is the onset of the next
    syllable whenever that yields a legal syllable. Vowel length (a doubled
    vowel) is one nucleus."""
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


def find_argot_artifacts():
    base = safe_path(ROUND_DIR)
    found = []
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in (".md", ".json", ".yml", ".yaml", ".py", ".txt"):
            continue
        name = path.name.lower()
        parent = path.parent.name.lower()
        if "argot" in name or "deriv" in name or parent in ("argot",):
            if path.resolve() == safe_path(RUNNER).resolve():
                continue
            found.append(path)
    return found


def measure_argot(evidence, regressions):
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

    artifacts = find_argot_artifacts()
    measurement["artifacts"] = [str(path.relative_to(ROOT)) for path in artifacts]
    if not artifacts:
        failures.append("no argot-derivation artifact landed under reports/round-25 "
                        "(the D claim's implementation/receipt/delta)")
        missing.append(ARGOT_DIR)

    blob = ""
    for path in artifacts:
        blob += "\n" + evidence.text(str(path.relative_to(ROOT)))

    if artifacts:
        for token in ("head2", "reverse"):
            if token not in blob:
                failures.append(f"the argot artifact never names the {token!r} operation")
        if ARGOT_ID not in blob:
            failures.append(f"the argot artifact never names {ARGOT_ID}")
        if not re.search(r"(?i)\bdelta\b|forecast", blob):
            failures.append("the argot artifact records no delivered-vs-forecast delta")
        if not re.search(r"(?i)machine-readable|pattern|output", blob):
            failures.append("the argot artifact declares no machine-readable pattern/output pairs")
        if not re.search(r"(?i)\b(exit|selftest|receipt|executed)\b", blob):
            failures.append("the argot artifact records no executed receipt (command, exit, date)")

    # The gate that carries the leg, its selftest controls, and its canonical
    # D4 run. The round-17 forecast put the leg in the D4 typed gate; the
    # delivered implementation is a standalone sibling gate — the delta must
    # name that substitution rather than assert it away.
    argot_gate = "tools/gates/argot-derivation-gate.py"
    typed_gate_has_leg = bool(re.search(
        r"(?i)argot|" + ARGOT_ID, evidence.text(GATE)))
    selftest = regressions["measurement"]["labels"].get("argot-gate-selftest", {})
    source = regressions["measurement"]["labels"].get("argot-gate-d4", {})
    selftest_out = ""
    for run in regressions["measurement"]["runs"]:
        if run["label"] == "argot-gate-selftest":
            selftest_out = run.get("stdout") or ""
    selftest_summary = re.search(r"selftest:[^\n]*", selftest_out)
    measurement["argot_gate"] = {
        "path": argot_gate,
        "exists": safe_path(argot_gate).is_file(),
        "typed_gate_carries_the_leg": typed_gate_has_leg,
        "selftest_exit": selftest.get("exit"),
        "selftest_summary": selftest_summary.group(0) if selftest_summary else None,
        "d4_run_exit": source.get("exit"),
        "d4_run_command": source.get("command"),
    }
    if not safe_path(argot_gate).is_file():
        failures.append(f"the argot-derivation gate is missing: {argot_gate}")
        missing.append(argot_gate)
    else:
        if selftest.get("exit") != 0:
            failures.append(f"the argot gate's selftest is not green (exit {selftest.get('exit')}): "
                            f"{selftest_out.strip().splitlines()[-1][:120] if selftest_out.strip() else ''}")
        if source.get("exit") != 0:
            failures.append("the argot gate's canonical D4 run is not green")

    # The delta must name the forecast elements not delivered — including the
    # substitution of a sibling gate for the typed-gate leg the forecast asked for.
    if artifacts:
        if not re.search(r"(?i)not delivered|undelivered|vacuous|replanned|not reproducible",
                         blob):
            failures.append("the argot delta names no forecast element as not delivered "
                            "(a silent drop)")
        if not typed_gate_has_leg and not re.search(
                r"(?i)(sibling|standalone|separate)[^\n]{0,80}gate|typed gate[^\n]{0,80}"
                r"(not|no|did not|is not)", blob):
            failures.append("the forecast put the leg in the D4 typed gate; the delivered leg is a "
                            "sibling gate and the delta does not name that substitution")

    # A violating form must be reported: probe the gate with a fixture whose
    # declared chain does not yield the candidate, and require D4L-ARGOT-DERIV.
    scratch = ROOT / ".scratch" / "round-25" / "validation" / "argot-control"
    scratch.mkdir(parents=True, exist_ok=True)
    violating = scratch / "violating.yml"
    violating.write_text(
        'name: "F-argot-violating"\nlexicon:\n  -\n    id: "L-99"\n    term: "min2"\n'
        '    gloss: "one (quote)"\n    field: "trade"\n    route: "root"\n'
        '    register: "quote"\n    derived_from: "min"\n'
        '    derivation: {op: "reverse", base: "min"}\n', encoding="utf-8")
    clean = scratch / "clean.yml"
    clean.write_text(
        'name: "F-argot-clean"\nlexicon:\n  -\n    id: "L-98"\n    term: "nim"\n'
        '    gloss: "one (quote)"\n    field: "trade"\n    route: "root"\n'
        '    register: "quote"\n    derived_from: "min"\n'
        '    derivation: {op: "reverse", base: "min"}\n', encoding="utf-8")
    control = run_command("argot-violating", (argot_gate, str(violating.relative_to(ROOT))))
    positive = run_command("argot-clean", (argot_gate, str(clean.relative_to(ROOT))))
    blob_control = (control.get("stdout") or "") + (control.get("stderr") or "")
    measurement["control_violating_derivation"] = {
        "command": control["command"], "date": control["date"], "exit": control.get("exit"),
        "argot_id_emitted": ARGOT_ID in blob_control,
        "positive_control_command": positive["command"], "positive_control_exit": positive.get("exit"),
    }
    if control.get("exit") == 0:
        failures.append("control: a fixture whose declared chain does not yield its form is graded "
                        "green (the leg has no teeth)")
    if ARGOT_ID not in blob_control:
        failures.append(f"control: the violating derivation does not emit {ARGOT_ID}")
    if positive.get("exit") != 0:
        failures.append("control: a correct derivation is not graded clean (the leg is not "
                        "discriminating)")
    return result(failures, measurement, missing)


def measure_depth(evidence, regressions):
    failures, measurement, missing = [], {}, []
    argot = measure_argot(evidence, regressions)
    measurement["argot_derivation"] = argot["measurement"]
    failures.extend(f"argot: {item}" for item in argot["failures"])
    missing.extend(argot["missing_dependencies"])
    return result(failures, measurement, missing)


# --------------------------------------------------------------------------
# Claim C — the reconciled lessons index
# --------------------------------------------------------------------------

def queue_owners(block):
    """Owners from the open-question queue table's `owner` column (the delivered
    shape), falling back to inline `owner:` fields when no table is present."""
    lines = [line.strip() for line in block.splitlines() if line.strip().startswith("|")]
    if lines:
        header = [cell.strip().strip("`*") for cell in lines[0].strip().strip("|").split("|")]
        if "owner" in header:
            index = header.index("owner")
            owners = []
            for line in lines[2:]:
                cells = [cell.strip().strip("`*") for cell in line.strip().strip("|").split("|")]
                if index < len(cells) and cells[index] and cells[index] not in ("—", "-", "–"):
                    owners.append(cells[index])
            return sorted(set(owners))
    return sorted({match.group(1).strip(" `*") for match in OWNER_RE.finditer(block)})


def measure_lessons(evidence):
    failures, measurement, missing = [], {}, []
    text = evidence.text(LESSONS_README)
    if not text:
        failures.append(f"the reconciled lessons index is missing: {LESSONS_README}")
        missing.append(LESSONS_README)
        return result(failures, measurement, missing)
    files = sorted(path.name for path in safe_path(LESSONS_DIR).glob("*.md"))
    rows = sorted({match.group(1) for match in LESSONS_ROW_RE.finditer(text)})
    round_rows = sorted({match.group(1) for match in LESSONS_ROUND_ROW_RE.finditer(text)})
    measurement["partition"] = {"files": metric(len(files), f"ls {LESSONS_DIR}/*.md"),
                                "index_rows": metric(len(rows), "rows parsed from the index"),
                                "command": f"{COMMAND} (lessons partition census)", "date": today()}
    orphans = [name for name in files if name not in rows]
    phantom = [name for name in rows if name not in files]
    if orphans:
        failures.append(f"the index omits {len(orphans)} lesson file(s): {orphans}")
    if phantom:
        failures.append(f"the index names {len(phantom)} file(s) that do not exist: {phantom}")
    measurement["round_13_row"] = {"round": "13", "rows": round_rows,
                                   "note": "a row may exist for a skipped round provided it says so"}
    if round_rows:
        line = next((line for line in text.splitlines()
                     if re.match(r"(?m)^\|\s*`?round-" + round_rows[0] + r"`?\s*\|", line)), "")
        if not re.search(r"(?i)no lesson file|skipped|operator", line):
            failures.append(f"the index carries a round-{round_rows[0]} row without saying the "
                            "round has no lesson file")

    formats = [name for name in CENSUS_FORMATS if name.lower() in text.lower()]
    measurement["census_formats"] = {"documented": formats,
                                     "expected": list(CENSUS_FORMATS)}
    if len(formats) != len(CENSUS_FORMATS):
        failures.append(f"the index documents {len(formats)} of {len(CENSUS_FORMATS)} census "
                        f"formats (missing: {[n for n in CENSUS_FORMATS if n not in formats]})")

    owners = []
    queue_section = re.search(r"(?ims)^#{1,6}[^\n]*open[- ]question[^\n]*$", text)
    queue_rows = []
    if queue_section:
        tail = text[queue_section.end():]
        stop = re.search(r"(?m)^#{1,6}\s", tail)
        block = tail[:stop.start()] if stop else tail
        queue_rows = [line.strip() for line in block.splitlines()
                      if line.strip().startswith(("|", "-", "*", "+"))]
        owners = queue_owners(block)
    measurement["open_question_queue"] = {"rows": len(queue_rows), "owners": owners[:12],
                                          "owner_count": len(owners)}
    if not queue_section:
        failures.append("the index carries no open-question queue section")
    elif not queue_rows:
        failures.append("the open-question queue carries no rows")
    elif not owners:
        failures.append("the open-question queue names no owner for any item")
    elif len(owners) < 2:
        failures.append(f"the open-question queue names only one owner ({owners[0]!r}); "
                        "the claim requires an owner per item across the standing queue")

    # The declared row/file counts must reproduce the measured partition.
    declared_rows = {int(value) for value in ROWS_DECLARED_RE.findall(text)}
    declared_files = {int(value) for value in FILES_DECLARED_RE.findall(text)}
    measurement["declared_counts"] = {"rows": sorted(declared_rows)[:6],
                                      "files": sorted(declared_files)[:6],
                                      "measured_rows": len(rows), "measured_files": len(files)}
    if declared_rows and len(rows) not in declared_rows:
        failures.append(f"the index declares rows={sorted(declared_rows)}; the measured row count is {len(rows)}")
    if declared_files and len(files) not in declared_files:
        failures.append(f"the index declares files={sorted(declared_files)}; the partition holds {len(files)}")
    if not COUNT_COMMAND_RE.search(text):
        failures.append("the index carries no counting command")
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
    synced = {}
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

    legs = ("ok   L1-build\nok   L2-channel\nFAIL L3-routing-consistency\n"
            "summary: 2/3 legs passed\n")
    ok, failed, passed, total = gate_legs(legs)
    check("gate-legs-parse", (ok, failed, passed, total) ==
          (["L1-build", "L2-channel"], ["L3-routing-consistency"], 2, 3))

    check("stale-token-detected",
          bool(stale_tokens_in("the committed D4 hold set is 15 holds and 1 note")))
    check("stale-token-negated-passes",
          not stale_tokens_in("the pre-repair prose reported 15 holds and 1 note; the live bytes "
                              "carry 12 holds and 0 notes"))
    check("stale-token-cleared-passes",
          not stale_tokens_in("the committed D4 hold set is 12 holds, 0 notes and 0 fails"))
    check("supersession-marker-detected",
          any(marker in "this row is superseded by the family-clean revision".lower()
              for marker in SUPERSEDED_MARKERS))

    check("syllabify-saalumi", syllabify("saalumi") == ["saa", "lu", "mi"],
          observed=syllabify("saalumi"))
    check("syllabify-min", "".join(syllabify("min")) == "min", observed=syllabify("min"))

    lessons = ("| `corpus/lessons/round-10.md` | gate-keeper | 2 | pointer | pin |\n"
               "| `corpus/lessons/round-5.md` | plain | 0 | pointer | pin |\n"
               "| `round-13` | — | — | no lesson file exists | — |\n\n"
               "## 4. Open-question queue\n\n"
               "| Q-id | question | owner | status |\n|---|---|---|---|\n"
               "| Q-02-1 | axis drift | `operator` | open |\n"
               "| Q-05-1 | freshness | `corpus/QUALITY.md` | open |\n\n"
               "Rows: 26. Files: 26. `ls corpus/lessons/*.md | wc -l` → 26\n")
    rows = {match.group(1) for match in LESSONS_ROW_RE.finditer(lessons)}
    check("lessons-row-parse", rows == {"round-10.md", "round-5.md"}, observed=sorted(rows))
    check("lessons-round13-row-parse",
          {match.group(1) for match in LESSONS_ROUND_ROW_RE.finditer(lessons)} == {"13"})
    check("lessons-count-command", bool(COUNT_COMMAND_RE.search(lessons)))
    check("lessons-owner-scan",
          queue_owners(lessons.split("## 4. Open-question queue")[1]) ==
          ["corpus/QUALITY.md", "operator"], observed=queue_owners(lessons))
    check("lessons-declared-counts",
          {int(v) for v in ROWS_DECLARED_RE.findall(lessons)} == {26}
          and {int(v) for v in FILES_DECLARED_RE.findall(lessons)} == {26})

    passed_controls = sum(1 for item in controls if item["passed"])
    for item in controls:
        print(("ok   " if item["passed"] else "FAIL ") + item["control"]
              + ("" if item["passed"] else f" — {item}"))
    print(f"selftest: {passed_controls}/{len(controls)} checks passed — the runner's own "
          "implementation of the two argot operations against the eleven design pairs, the "
          "gate leg parser, the stale-passenger detector, the syllabifier, and the lessons "
          "row/owner/count-command parsers; no file opened for writing")
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
            ("O", lambda: measure_operability(evidence, regressions)),
            ("D", lambda: measure_depth(evidence, regressions)),
            ("C", lambda: measure_lessons(evidence))):
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
    if claims.get("round") != 25 or targets.get("round") != 25:
        coherence.append("Claims/targets are not both round 25")
    if targets.get("baseline_revision") != baseline:
        coherence.append("Claims/targets disagree on the declared baseline")
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"O": "operability", "D": "depth", "C": "coverage"}:
        coherence.append("Declared claim set is not O/operability, D/depth, C/coverage")
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
    return {"round": 25, "runner": RUNNER, "runner_sha256": sha(safe_path(RUNNER).read_bytes()),
            "counting_command": COMMAND, "date": today(), "baseline_revision": baseline,
            "targets_date": targets.get("date"), "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results,
            "failures": failures, "missing_dependencies": sorted(evidence.missing | {
                path for item in results.values() for path in item["missing_dependencies"]}),
            "protected_filed_artifacts": preservation,
            "synced_from_live": {key: value for key, value in sorted(synced.items())},
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": [
                "Run this round validator only in an isolated repository clone under the lane's .scratch with TMPDIR below that clone's .scratch. It never edits filed bytes, never commits, and never pushes.",
                "Claim O is measured behaviourally: the derived-packet invocation must land in {0, 2} with zero DERIV-REPLAY FAIL lines and no L3-routing-consistency FAIL, while the documented source-packet entry keeps its canonical leg count and the corrupted-packet and tampered-expectation controls must still be refused. The fix's implementation shape (named input-class diagnostic vs nullish-scalar handling) is deliberately not pinned.",
                "Claim O's v3 leg reads the superseding revision packet's claim ledger rows and its OQ-V3-05 line and fails on surviving stale passenger prose (D4-CL05/06/07/09, OQ-V3-05) in a sentence that carries no supersession marker. The revision must name and pin its parent, and its own declared packet digest must match its bytes. Filed round-20/round-22 bytes are protected and never rewritten; the predecessor's staleness is recorded as historical, not graded.",
                "Claim D is measured from the landed argot artifact plus the argot gate's own selftest, its canonical D4 run, a runner-authored violating-form control and its clean counterpart, and the delta's naming of any forecast element not delivered — including the substitution of the standalone sibling gate for the typed-gate leg the forecast asked for. The eleven worked derivations are re-derived by this runner's own head2/reverse implementation, never read back from the design doc. A silent substitution fails.",
                "Claim C is measured from corpus/lessons/README.md against the live partition: one row per file and no phantom rows, a skipped round row only if it says so, the three census formats documented, an open-question queue with owners (read from the queue table's owner column), a declared row/file count that reproduces, and a counting command present.",
                "Protected reports and frozen generations of rounds 8-24 must match the round-25 declared baseline; new round-25 files live under reports/round-25 and corpus/lessons only.",
            ]}


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Measure round-25 O/D/C acceptance; use only in an isolated clone.")
    parser.add_argument("--check", action="store_true",
                        help="print the measured JSON without writing validation.json")
    parser.add_argument("--selftest", action="store_true",
                        help="exercise runner positive/negative controls without dependencies")
    args = parser.parse_args(argv)
    if args.check and args.selftest:
        parser.error("--check and --selftest are mutually exclusive")
    if ".scratch" not in ROOT.parts or not (ROOT / ".git").is_dir():
        print("could-not-evaluate: run round validators only in an isolated Git clone under "
              "the lane's .scratch", file=sys.stderr)
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
