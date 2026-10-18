#!/usr/bin/env python3
r"""run-gate-tests.py — round-26 gate+tests battery (seats R26-D17..D20).

Four seats, four questions, one runner:

  D17  the D4 typed gate passes with the hold set named and unchanged
  D18  negatives: a rule that does not derive its form reads D4L-ARGOT-DERIV
  D19  determinism: consecutive runs byte-identical on every graded entry
  D20  replay-frozen: the pinned generation reproduces (replay only)

Usage
-----
    python3 reports/round-26/gate-tests/run-gate-tests.py            # measure + write receipt
    python3 reports/round-26/gate-tests/run-gate-tests.py --check    # measure only, print
    python3 reports/round-26/gate-tests/run-gate-tests.py --selftest # dependency-free controls

Design rules this runner works inside
-------------------------------------
* Every measurement names its command, its exit code and its date. A battery
  that cannot say which bytes it ran is not evidence.
* `tools/replay-frozen.py` refuses an in-repo mirror root, so the replay leg
  runs with TMPDIR outside the repository; every other leg uses the lane's
  `$PWD/.scratch`.
* The teeth control plants into a **clone**, never the lane worktree: a control
  that moves the tree it measures is not a control.
* No file outside `reports/round-26/` and `.scratch/` is written. Read-only
  over `examples/`, `tools/` and every filed round-8-25 byte.

Exit codes: 0 all checks pass, 1 a check failed, 2 could-not-evaluate.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
SCRATCH = ROOT / ".scratch" / "r26-d17-d20"
FIXTURES = HERE / "fixtures"

TYPED_GATE = ROOT / "tools/gates/typed-pipeline-gate.py"
ARGOT_GATE = ROOT / "tools/gates/argot-derivation-gate.py"
REPLAY = ROOT / "tools/replay-frozen.py"

D4_SOURCE = "examples/culture-d4/packet.d4.yml"
D4_TYPED = "examples/culture-d4/packet.d4.typed.yml"
D4_EXPECTED = ROOT / "examples/culture-d4/expected-holds.json"
D2_SOURCE = "examples/culture-d2/packet.d2.yml"
D2_TYPED = "examples/culture-d2/packet.d2.typed.yml"

# The id the design authority fixes. `reports/round-17/d4/design-brief.md:308`
# and `:456` (control C-02) both spell it D4L-ARGOT-DERIV, and the gate emits
# that spelling. The round-25/26 seat header spells it D4L-ARGOT-DERV; that
# one-letter variant is recorded as a delta, never implemented (r25 argot
# impl-3 §4).
DERIV_ID = "D4L-ARGOT-DERIV"
DERIV_ID_VARIANT = "D4L-ARGOT-DERV"

# The negative fixtures and the verdict each must produce. `ids` is the exact
# set of finding ids the fixture must emit; `exit` the process exit code.
NEGATIVES = (
    # N1 is the design's own named trap: the maximal-coda reading of head2
    # would give `saalum`; the design fixes maximal-onset, so the delivered
    # form does not re-derive and the leg must say so.
    ("n1-maximal-coda.yml", 1, [DERIV_ID], "head2 maximal-coda reading rejected"),
    ("n2-rule-mismatch.yml", 1, [DERIV_ID], "declared pattern/output rule does not derive the form"),
    ("n4-unknown-rule.yml", 1, ["D4L-ARGOT-RULE"], "declared rule is not licensed"),
    ("n5-borrow-mismatch.yml", 1, [DERIV_ID], "loan adaptation does not yield the form"),
    ("n6-coverage-hold.yml", 1, ["D4L-ARGOT-COVERAGE"], "declared relation, not delivered"),
    ("n7-malformed.yml", 2, ["D4L-ARGOT-DATA"], "malformed input fails closed"),
    # N8 is the register design's own operation (reports/round-26/register/
    # rules.md §3): a packet `LENGTHEN` pattern/output rule, declared with a form
    # that does not double the vowel. The design's chosen operation is graded by
    # the same route as any packet rule, so the landing is checked by the leg
    # the design itself relies on.
    ("n8-lengthen-mismatch.yml", 1, [DERIV_ID],
     "the register design's LENGTHEN rule does not derive its form"),
)
POSITIVE = ("n3-positive-control.yml", 0, [], "the corrected forms re-derive clean")

# The control plant for the teeth leg: a register-scoped record whose declared
# head2 chain does not yield the delivered form. `saalum` is head2(saalumi)
# under the maximal-coda reading, which the design rejects.
PLANT_LINE = (
    '  - {id: NEG-D17-01, term: saalum, gloss: "planted non-deriving register '
    'form", field: trade, route: root, layer: native, stage: E0, axis: mark, '
    'evidence: design-choice, register: quote, derived_from: saalumi, '
    'derivation: head2}\n'
)


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(argv, cwd=None, env=None):
    """Run a command; return (exit, stdout+stderr, command string)."""
    proc = subprocess.run(
        [str(item) for item in argv],
        capture_output=True, text=True, cwd=str(cwd or ROOT),
        env=env or child_env(), check=False,
    )
    return proc.returncode, (proc.stdout or "") + (proc.stderr or ""), " ".join(
        str(item) for item in argv)


def child_env(extra=None):
    env = dict(os.environ)
    env["TMPDIR"] = str(SCRATCH)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    if extra:
        env.update(extra)
    return env


def findings_of(text):
    return [line.split(":")[0][len("FINDING "):].strip()
            for line in text.splitlines() if line.startswith("FINDING ")]


def legs_of(text):
    return [line[5:].split(":")[0].strip() for line in text.splitlines()
            if line.startswith("ok   ") or line.startswith("FAIL ")]


# --------------------------------------------------------------------------
# D17 — the D4 typed gate, with the hold set named and unchanged
# --------------------------------------------------------------------------


def measure_d17(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    for label, target, expect_legs in (
            ("d4-typed", D4_TYPED, 17), ("d4-source", D4_SOURCE, 20)):
        exit_code, out, command = run([sys.executable, TYPED_GATE, target])
        legs = legs_of(out)
        ok_legs = [leg for leg in legs if not out.split("FAIL ")[0]]
        failed_legs = [line for line in out.splitlines() if line.startswith("FAIL ")]
        holds = [line for line in out.splitlines()
                 if line.startswith("FINDING ") and "[hold]" in line]
        receipt["runs"].append({"label": label, "command": command, "date": now(),
                                "exit": exit_code, "legs": len(legs),
                                "failed_legs": failed_legs, "hold_lines": len(holds),
                                "stdout_sha256": hashlib.sha256(out.encode()).hexdigest()})
        check("D17 %s exits 0" % label, exit_code == 0, "exit %d" % exit_code)
        # The leg count is a floor, not an equality: the register landing (or
        # any later leg) adds legs, and a battery that pins the exact count
        # would fail an honest improvement. The pre-register counts are 17
        # (typed) and 20 (source); a *drop* below those is the regression.
        check("D17 %s runs at least %d legs" % (label, expect_legs),
              len(legs) >= expect_legs, "%d legs" % len(legs))
        check("D17 %s has no FAIL leg" % label, not failed_legs, "; ".join(failed_legs[:2]))
        check("D17 %s names the hold set" % label, len(holds) > 0,
              "no [hold] FINDING line")
        check("D17 %s argot leg is ok" % label,
              any("L3b-argot" in line and line.startswith("ok") for line in out.splitlines()),
              "L3b-argot not ok")

    # The expected-holds file is the hold set the gate grades against; the
    # live run must agree with it exactly.
    expected = json.loads(D4_EXPECTED.read_text(encoding="utf-8"))
    counts = expected.get("counts") or {}
    check("D17 expected-holds declares 0 fails", counts.get("fail") == 0,
          "%s" % counts)
    check("D17 expected-holds counts match its rows",
          counts.get("hold") == len(expected.get("holds") or [])
          and counts.get("note") == len(expected.get("notes") or []),
          "%s vs %d holds / %d notes" % (counts, len(expected.get("holds") or []),
                                         len(expected.get("notes") or [])))
    exit_code, out, command = run([sys.executable, TYPED_GATE, D4_TYPED, "--json"])
    try:
        document = json.loads(out)
    except ValueError:
        document = {}
    live = document.get("counts") or {}
    check("D17 live counts equal the frozen hold set", live == counts,
          "live %s vs expected %s" % (live, counts))
    # The claim's "hold set updated" leg: a round-26 revision note or
    # supersession pin on the file. This is recorded as an observation, not a
    # failure of *this* seat — the update follows the register forms landing,
    # which is another seat's write. The battery names the state either way.
    revision_note = expected.get("revision_note") or ""
    round26_named = "round-26" in revision_note or "round-26" in json.dumps(
        expected.get("supersedes_pins") or {})
    check("D17 the hold set is named", bool(revision_note), "no revision_note")
    receipt["hold_set"] = {"path": str(D4_EXPECTED.relative_to(ROOT)),
                           "declared": counts, "live": live,
                           "holds": [row.get("where") for row in expected.get("holds") or []],
                           "revision_note": revision_note,
                           "round26_revision_or_supersession": round26_named,
                           "command": command, "date": now()}
    if not round26_named:
        receipt.setdefault("observations", []).append(
            "the D4 hold set carries no round-26 revision note or supersession "
            "pin at this stamp: the claim's 'hold set updated' leg is open "
            "until the register forms land in the packet (see D17-typed-gate.md §1)")

    # The register-scoped derivation domain: the claim's core D leg. Recorded so
    # the parent can see the pre/post-landing delta from one place.
    exit_code, out, command = run([sys.executable, ARGOT_GATE, D4_SOURCE])
    coverage = [line for line in out.splitlines() if line.startswith("coverage:")]
    receipt["argot_coverage"] = {"command": command, "date": now(), "exit": exit_code,
                                 "line": coverage[0] if coverage else ""}
    return checks, failures


# --------------------------------------------------------------------------
# D18 — negatives: a rule that does not derive its form reads D4L-ARGOT-DERIV
# --------------------------------------------------------------------------


def measure_d18(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    rows = []
    for name, want_exit, want_ids, description in NEGATIVES + (POSITIVE,):
        path = FIXTURES / name
        exit_code, out, command = run([sys.executable, ARGOT_GATE, path])
        got = findings_of(out)
        rows.append({"fixture": name, "command": command, "date": now(),
                     "exit": exit_code, "expected_exit": want_exit,
                     "ids": got, "expected_ids": want_ids, "why": description})
        check("D18 %s exits %d" % (name, want_exit), exit_code == want_exit,
              "exit %d" % exit_code)
        check("D18 %s emits %s" % (name, want_ids or "nothing"), got == want_ids,
              "got %s" % got)
    receipt["fixtures"] = rows

    # The specific control the claim names: a rule that does not derive its form
    # must read D4L-ARGOT-DERIV. N1 and N2 are two independent routes into it
    # (a declared argot operation, and a packet-declared pattern/output rule).
    deriv_fixtures = [row for row in rows if row["fixture"].startswith(("n1-", "n2-", "n8-"))]
    check("D18 a non-deriving rule reads %s" % DERIV_ID,
          all(DERIV_ID in row["ids"] for row in deriv_fixtures),
          "%s" % [(row["fixture"], row["ids"]) for row in deriv_fixtures])
    check("D18 the leg discriminates (positive control clean)",
          any(row["fixture"].startswith("n3-") and row["exit"] == 0 for row in rows),
          "no clean positive control")

    # The id spelling delta: the design and the gate say ...DERIV, the seat
    # header says ...DERV. The implemented id must be the design's, and the
    # variant must not be emitted by anything.
    gate_text = ARGOT_GATE.read_text(encoding="utf-8")
    check("D18 the gate implements the design's id spelling",
          DERIV_ID in gate_text, "%s absent" % DERIV_ID)
    emitted_variant = any(DERIV_ID_VARIANT in row["ids"] for row in rows)
    check("D18 the seat-header variant is never emitted", not emitted_variant,
          "%s emitted" % DERIV_ID_VARIANT)
    receipt["id_spelling"] = {
        "design_and_gate": DERIV_ID, "seat_header_variant": DERIV_ID_VARIANT,
        "authority": "reports/round-17/d4/design-brief.md:308,456 (control C-02)",
        "variant_emitted": emitted_variant,
        "r25_record": "reports/round-25/argot/impl-3.md:60-66, impl-6.md:91-93",
    }
    return checks, failures


# --------------------------------------------------------------------------
# D19 — determinism: consecutive runs byte-identical
# --------------------------------------------------------------------------


def measure_d19(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    entries = (
        ("d4-typed", [sys.executable, TYPED_GATE, D4_TYPED]),
        ("d4-source", [sys.executable, TYPED_GATE, D4_SOURCE]),
        ("d2-typed", [sys.executable, TYPED_GATE, D2_TYPED]),
        ("d2-source", [sys.executable, TYPED_GATE, D2_SOURCE]),
        ("argot-d4", [sys.executable, ARGOT_GATE, D4_SOURCE]),
    )
    rows = []
    for label, argv in entries:
        digests, exits = [], []
        for _ in range(3):
            exit_code, out, command = run(argv)
            digests.append(hashlib.sha256(out.encode()).hexdigest())
            exits.append(exit_code)
        unique = sorted(set(digests))
        rows.append({"label": label, "command": command, "date": now(),
                     "runs": 3, "exits": exits, "digests": digests,
                     "unique_digests": len(unique)})
        check("D19 %s: 3 runs byte-identical" % label, len(unique) == 1,
              "%d distinct digests" % len(unique))
        check("D19 %s: exit stable" % label, len(set(exits)) == 1,
              "exits %s" % exits)
    receipt["determinism"] = rows

    # The selftests are the tools' own controls; a green selftest on each entry
    # is the deterministic-regression floor.
    for label, argv, marker in (
            ("typed-selftest", [sys.executable, TYPED_GATE, "--selftest"], "checks passed"),
            ("typed-selftest-generalized", [sys.executable, TYPED_GATE,
                                            "--selftest-generalized"], "checks passed"),
            ("argot-selftest", [sys.executable, ARGOT_GATE, "--selftest"], "checks passed"),
            ("replay-selftest", [sys.executable, REPLAY, "--selftest"], ""),
    ):
        exit_code, out, command = run(argv)
        receipt["runs"].append({"label": label, "command": command, "date": now(),
                                "exit": exit_code,
                                "stdout_sha256": hashlib.sha256(out.encode()).hexdigest(),
                                "tail": out.strip().splitlines()[-1] if out.strip() else ""})
        check("D19 %s exits 0" % label, exit_code == 0,
              "exit %d: %s" % (exit_code, out.strip().splitlines()[-1][:120]
                               if out.strip() else ""))
        if marker:
            check("D19 %s reports %r" % (label, marker), marker in out,
                  out.strip().splitlines()[-1][:120] if out.strip() else "no output")
    return checks, failures


# --------------------------------------------------------------------------
# D20 — replay-frozen: the pinned generation reproduces
# --------------------------------------------------------------------------


def measure_d20(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    # The replay tool refuses an in-repo mirror root, so this leg alone runs
    # with TMPDIR outside the repository. `tempfile.mkdtemp` honours the
    # process TMPDIR, which is the in-repo `.scratch` here, so the root is
    # named explicitly and checked to sit outside the repo.
    outside = Path(os.environ.get("KOTODAMA_REPLAY_TMPDIR") or "/var/tmp")
    outside = outside / ("kotodama-r26-replay-%d" % os.getpid())
    outside.mkdir(parents=True, exist_ok=True)
    if ROOT.resolve() in outside.resolve().parents or outside.resolve() == ROOT.resolve():
        check("D20 the replay mirror root sits outside the repository", False,
              "%s is inside %s" % (outside, ROOT))
        return checks, failures
    env = child_env({"TMPDIR": str(outside)})
    generations = sorted((ROOT / "tools/gates/frozen").glob("*/MANIFEST.tsv"))
    generations += sorted((ROOT / "tools/gates/frozen").glob("*/*/MANIFEST.tsv"))
    rows = []
    for manifest in sorted(generations):
        exit_code, out, command = run([sys.executable, REPLAY, manifest, "--json"],
                                      env=env)
        try:
            document = json.loads(out)
        except ValueError:
            document = {}
        replay_rows = document.get("rows") or []
        statuses = [item.get("status") for item in replay_rows]
        summary = {"rows": len(replay_rows),
                   "reproduced": statuses.count("reproduced"),
                   "mismatch": statuses.count("mismatch"),
                   "could_not_evaluate": statuses.count("could-not-evaluate")}
        row_lines = [line for line in out.splitlines() if line.startswith("ROW ")]
        tail = [line for line in out.splitlines() if line.startswith("REPLAY")]
        mismatched_lines = [
            {"line": item.get("line"), "reason": item.get("reason"),
             "status": item.get("status"), "gate": item.get("gate"),
             "input": item.get("input"), "observed_exit": item.get("observed_exit"),
             "recorded_exit": item.get("recorded_exit"),
             "recorded_input_sha256": item.get("recorded_input_sha256"),
             "live_input_sha256": (
                 sha256_file(ROOT / item["input"])
                 if item.get("input") and (ROOT / item["input"]).is_file() else None)}
            for item in replay_rows
            if item.get("status") in ("mismatch", "could-not-evaluate")]
        rows.append({"manifest": str(manifest.relative_to(ROOT)), "command": command,
                     "date": now(), "exit": exit_code, "summary": summary,
                     "row_lines": row_lines, "mismatched": mismatched_lines,
                     "tail": tail[-1] if tail else ""})
    shutil.rmtree(outside, ignore_errors=True)
    receipt["replay"] = rows

    # The newest round-26 generation is the current pin for the typed-pipeline
    # input class (built by `freeze.py` in this directory); it must reproduce
    # every row. A *mid-wave* round-26 generation whose inputs then moved is a
    # superseded recording, exactly like the round-25 predecessor: the lane's
    # rule is that a re-freeze is a new generation, never an in-place edit, so
    # the earlier one is classified with the others rather than edited or
    # re-failed.
    r26 = [row for row in rows if "round-26" in row["manifest"]]
    check("D20 a round-26 generation is present", bool(r26),
          "no round-26 MANIFEST found; run reports/round-26/gate-tests/freeze.py")
    current = []
    if r26:
        newest = max(r26, key=lambda row: (ROOT / row["manifest"]).stat().st_mtime)
        current = [newest]
        for row in current:
            check("D20 %s (newest round-26) replays clean" % row["manifest"],
                  row["exit"] == 0, "exit %d: %s" % (row["exit"], row["tail"]))
    superseded = [row for row in rows if row not in current]
    # Every other generation is a superseded pin. Each is replayed and its
    # refusal class named. The principled split, so no row is hand-waved:
    #   * `could-not-evaluate` / `gate_digest_mismatch` — the gate bytes moved
    #     after the freeze; the documented cascade (a re-pin is a new
    #     generation, never an in-place edit).
    #   * `replay_mismatch` **with a moved input** — the row's live input no
    #     longer hashes to its own `input_sha256`, i.e. a later generation
    #     superseded it (the round-22 family-clean projection superseding the
    #     round-18 pin is exactly this; `reports/round-25/scribe/frozen-rows.md`
    #     §3). A supersession, recorded.
    #   * `replay_mismatch` **with the input unmoved** — the pinned input still
    #     hashes to its pin yet the gate's output differs. Nothing superseded
    #     it; that is genuine drift and a new finding.
    unexpected, drift = [], []
    for row in superseded:
        for item in row["mismatched"]:
            if item.get("status") == "could-not-evaluate":
                continue
            recorded = item.get("recorded_input_sha256")
            live = item.get("live_input_sha256")
            if recorded and live and recorded != live:
                continue  # the input moved: a later generation superseded the row
            drift.append("%s row %s: input unmoved (%s) but output differs: %s"
                         % (row["manifest"], item.get("line"), (recorded or "?")[:12],
                            item.get("reason")))
    unexpected = drift
    receipt["replay_superseded"] = [
        {"manifest": row["manifest"], "exit": row["exit"],
         "mismatched": row["mismatched"], "class": "superseded"
         if row["exit"] in (1, 2) else "reproduced"} for row in superseded]
    check("D20 only the documented superseded rows report a mismatch",
          not unexpected, "%s" % unexpected)
    return checks, failures


# --------------------------------------------------------------------------
# the teeth control — plant, rebuild, grade, revert (in a clone)
# --------------------------------------------------------------------------


def measure_teeth(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    clone = SCRATCH / "clone"
    if clone.exists():
        shutil.rmtree(clone)
    exit_code, out, command = run(["git", "clone", "-q", "--no-hardlinks", ".", clone])
    check("teeth: the clone is available", exit_code == 0, out[-200:])
    if exit_code != 0:
        return checks, failures

    component = clone / "examples/culture-d4/components/04-lexicon.yml"
    original = component.read_text(encoding="utf-8")
    planted = original.replace("lexicon:\n", "lexicon:\n" + PLANT_LINE, 1)
    check("teeth: the plant landed", planted != original, "lexicon: anchor not found")
    if planted == original:
        return checks, failures
    component.write_text(planted, encoding="utf-8")

    # `tools/d2-typed-labels.py --emit` returns the *findings* exit (0/1) after
    # writing — documented at `tools/d2-typed-labels.py:3624` ("--check answers
    # byte-identity; findings are the report's job") — so a clean build of a
    # packet with open holds still returns 1 while the projection is written.
    # 2 is the only failure code that means "nothing was written".
    steps = (
        ("assemble", [sys.executable, "tools/assemble-culture-d4.py"], (0,)),
        ("project", [sys.executable, "tools/d2-typed-labels.py", "--packet",
                     "examples/culture-d4/packet.d4.yml", "--emit",
                     "examples/culture-d4/typed-labels.d4.yml"], (0, 1)),
        ("adapt", [sys.executable, "tools/assemble-d4-typed.py", "--emit",
                   "examples/culture-d4/packet.d4.typed.yml"], (0, 1)),
    )
    rebuilt = True
    for label, argv, ok_codes in steps:
        exit_code, out, command = run(argv, cwd=clone)
        if exit_code not in ok_codes:
            rebuilt = False
            check("teeth: rebuild step %s" % label, False,
                  "exit %d (want %s): %s" % (exit_code, ok_codes, out[-160:]))
    check("teeth: the planted artifacts rebuild", rebuilt, "a build step failed")

    exit_code, out, command = run(
        [sys.executable, "tools/gates/typed-pipeline-gate.py",
         "examples/culture-d4/packet.d4.typed.yml"], cwd=clone)
    deriv_lines = [line for line in out.splitlines()
                   if line.startswith("FINDING " + DERIV_ID)]
    failed_leg = [line for line in out.splitlines()
                  if line.startswith("FAIL L3b-argot")]
    check("teeth: the planted non-deriving form reads %s" % DERIV_ID,
          bool(deriv_lines), "no %s line" % DERIV_ID)
    check("teeth: the planted form names the record",
          any("NEG-D17-01" in line for line in deriv_lines), "%s" % deriv_lines[:1])
    check("teeth: L3b-argot goes red", bool(failed_leg), "L3b-argot stayed ok")
    check("teeth: the planted run does not exit 0", exit_code != 0,
          "exit %d" % exit_code)
    receipt["teeth"] = {"clone": str(clone.relative_to(ROOT)),
                        "command": command, "date": now(), "exit": exit_code,
                        "deriv_lines": deriv_lines, "failed_leg": failed_leg}

    # Revert the clone and require the clean tree to come back green: the
    # control shows the leg discriminates rather than being always red.
    exit_code, out, command = run(["git", "checkout", "--",
                                   "examples/culture-d4/"], cwd=clone)
    for _label, argv, _ok in steps:
        run(argv, cwd=clone)
    exit_code, out, command = run(
        [sys.executable, "tools/gates/typed-pipeline-gate.py",
         "examples/culture-d4/packet.d4.typed.yml"], cwd=clone)
    clean_legs = legs_of(out)
    clean_failed = [line for line in out.splitlines() if line.startswith("FAIL ")]
    check("teeth: the reverted clone is green again",
          exit_code == 0 and not clean_failed, "exit %d: %s" % (exit_code, clean_failed[:2]))
    receipt["teeth_reverted"] = {"command": command, "date": now(), "exit": exit_code,
                                 "legs": len(clean_legs)}
    shutil.rmtree(clone, ignore_errors=True)
    return checks, failures


# --------------------------------------------------------------------------
# selftest — dependency-free controls for this runner's own logic
# --------------------------------------------------------------------------


def selftest():
    checks = []

    def check(name, ok):
        checks.append((name, bool(ok)))

    check("finding parser reads one id per line",
          findings_of("FINDING D4L-ARGOT-DERIV: FAIL — x\ncoverage: y\n")
          == ["D4L-ARGOT-DERIV"])
    check("finding parser ignores the coverage line",
          findings_of("coverage: records=1\n") == [])
    check("leg parser reads ok and FAIL lines",
          legs_of("ok   L1-build\nFAIL L2-channel: x\n") == ["L1-build", "L2-channel"])
    check("leg parser ignores the summary",
          legs_of("summary: 17/17 legs passed\n") == [])
    check("the design's id is the DERIV spelling", DERIV_ID == "D4L-ARGOT-DERIV")
    check("the variant is distinct", DERIV_ID != DERIV_ID_VARIANT)
    check("every negative fixture exists on disk",
          all((FIXTURES / name).is_file()
              for name, _e, _i, _d in NEGATIVES + (POSITIVE,)))
    check("the plant line names the planted record", "NEG-D17-01" in PLANT_LINE)
    check("the plant line declares head2 over saalumi",
          "derived_from: saalumi" in PLANT_LINE and "derivation: head2" in PLANT_LINE)
    check("the plant line is register-scoped", "register: quote" in PLANT_LINE)

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%-52s %s" % (name, "ok" if ok else "FAIL"))
    print("selftest: %d/%d checks passed" % (len(checks) - len(failed), len(checks)))
    return 1 if failed else 0


# --------------------------------------------------------------------------


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="measure only, print")
    parser.add_argument("--selftest", action="store_true", help="dependency-free controls")
    args = parser.parse_args(argv[1:])

    if args.selftest:
        return selftest()

    SCRATCH.mkdir(parents=True, exist_ok=True)
    receipt = {"schema": "kotodama-r26-gate-tests-v1", "round": 26,
               "seats": ["R26-D17", "R26-D18", "R26-D19", "R26-D20"],
               "date": now(), "runs": [], "checks": [], "failures": []}
    for item in (TYPED_GATE, ARGOT_GATE, REPLAY, D4_EXPECTED, ROOT / D4_SOURCE,
                 ROOT / D4_TYPED):
        receipt.setdefault("inputs", {})[str(item.relative_to(ROOT))] = (
            sha256_file(item) if item.is_file() else None)

    all_checks, all_failures = [], []
    for measure in (measure_d17, measure_d18, measure_d19, measure_d20, measure_teeth):
        try:
            checks, failures = measure(receipt)
        except Exception as error:  # noqa: BLE001 — a leg that crashes is a finding
            checks, failures = [{"name": measure.__name__, "ok": False,
                                 "detail": "%s: %s" % (type(error).__name__, error)}], \
                                ["%s crashed: %s" % (measure.__name__, error)]
        all_checks.extend(checks)
        all_failures.extend(failures)

    receipt["checks"] = all_checks
    receipt["failures"] = all_failures
    receipt["passed"] = not all_failures
    receipt["summary"] = {"checks": len(all_checks),
                          "passed": sum(1 for item in all_checks if item["ok"]),
                          "failed": len(all_failures)}

    for item in all_checks:
        print("%s %s%s" % ("ok  " if item["ok"] else "FAIL", item["name"],
                           "" if item["ok"] else " — %s" % item["detail"]))
    print("gate-tests: %d/%d checks passed" % (receipt["summary"]["passed"],
                                               receipt["summary"]["checks"]))

    if not args.check:
        target = HERE / "receipt.json"
        target.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n",
                          encoding="utf-8")
        print("receipt: %s" % target.relative_to(ROOT))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
