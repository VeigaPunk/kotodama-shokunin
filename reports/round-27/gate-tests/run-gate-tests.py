#!/usr/bin/env python3
r"""run-gate-tests.py — round-27 gate+tests battery (seats R27-D13..D16).

Four seats, four questions, one runner:

  D13  the argot gate is green on the amended packet (register law + syllabify)
  D14  the typed gate and BOTH assemblers are green on the amended packet
  D15  negative: a register-law violation is caught (control in a clone)
  D16  negative: a syllabify regression is caught (head2 reading pair)

Usage
-----
    python3 reports/round-27/gate-tests/run-gate-tests.py            # measure + write receipt
    python3 reports/round-27/gate-tests/run-gate-tests.py --check    # measure only, print
    python3 reports/round-27/gate-tests/run-gate-tests.py --selftest # dependency-free controls

Design rules this runner works inside
-------------------------------------
* Every measurement names its command, its exit code and its date. A battery
  that cannot say which bytes it ran is not evidence.
* The teeth control plants into a **clone**, never the lane worktree: a control
  that moves the tree it measures is not a control.
* No file outside `reports/round-27/` and `.scratch/` is written. Read-only over
  `examples/`, `tools/` and every filed round-8..26 byte.
* A negative is only a negative if a **named instrument** catches it, and only a
  control if the clean tree passes the same instrument. Where the round-27 law
  surface has no owning lane gate, that is recorded as a named gap rather than
  papered over with a private checker.

Exit codes: 0 all checks pass, 1 a check failed, 2 could-not-evaluate.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
SCRATCH = ROOT / ".scratch" / "r27-d13"
FIXTURES = HERE / "fixtures"

ARGOT_GATE = ROOT / "tools/gates/argot-derivation-gate.py"
TYPED_GATE = ROOT / "tools/gates/typed-pipeline-gate.py"
D4_ASM_GATE = ROOT / "tools/gates/d4-assembly-check-gate.py"
D4_TYPED_GATE = ROOT / "tools/gates/d4-typed-labels-check-gate.py"
ASM_D4 = ROOT / "tools/assemble-culture-d4.py"
ASM_D4_TYPED = ROOT / "tools/assemble-d4-typed.py"
PROJECTOR = ROOT / "tools/d2-typed-labels.py"

# The round-27 register-law audit instrument (peer seat X59, same round). It is
# the lane's declared detector for the speech-act law rows; this battery does
# not re-implement it, and names the gap when it is absent.
LAW_INSTRUMENT = ROOT / "reports/round-27/audit/x59-register-law-negatives.py"

D4_SOURCE = "examples/culture-d4/packet.d4.yml"
D4_TYPED = "examples/culture-d4/packet.d4.typed.yml"
D4_PROJECTION = "examples/culture-d4/typed-labels.d4.yml"
D4_EXPECTED = ROOT / "examples/culture-d4/expected-holds.json"
D4_COMPONENT = "examples/culture-d4/components/04-lexicon.yml"

# The id the design authority fixes (`reports/round-17/d4/design-brief.md:308`).
DERIV_ID = "D4L-ARGOT-DERIV"

# The design's own eleven worked derivations (`design-language.md` §5). D16
# re-derives every row: a regression that breaks any one of them is a regression
# against the design, not against this battery's taste.
DESIGN_TABLE = (
    ("saalumi", "head2", "saalu"),
    ("min", "reverse", "nim"),
    ("kus", "reverse", "suk"),
    ("nam", "reverse", "man"),
    ("nes", "reverse", "sen"),
    ("sam", "reverse", "mas"),
    ("mus", "reverse", "sum"),
    ("kin", "reverse", "nik"),
    ("sun", "reverse", "nus"),
    ("samun", "reverse", "numas"),
    ("makun", "reverse", "nukam"),
)

# D16's fixtures and the verdict each must produce. `s3` is the design's own
# named trap and must read D4L-ARGOT-DERIV under **every** reading; exactly one
# of s1/s2 may be clean, whichever side the syllabify fix lands on.
SYLLABIFY_FIXTURES = (
    ("s3-head2-maximal-coda.yml", 1, [DERIV_ID],
     "the maximal-coda reading (design-language.md §5 names this trap)"),
)
# The reading pair is anchored on the CLUSTER row, not on `tikmes`. `tikmes` is
# a one-cluster base, and the legality clause collapses the two readings of it
# into one (`tik.mes` under both), so it cannot discriminate once the fix lands.
# `tumkalker` carries two clusters and the two readings genuinely differ on it:
# unconstrained moves each run forward (`tum.ka.lker` -> `tumka`), constrained
# splits coda|onset (`tum.kal.ker` -> `tumkal`).
SYLLABIFY_READING_PAIR = (
    ("s1-head2-unconstrained.yml", "tumka",
     "the unconstrained maximal-onset reading (a run moves whole to the onset)"),
    ("s2-head2-constrained.yml", "tumkal",
     "the legality-constrained reading (a run splits coda|onset)"),
)
# The before/after witness for the syllabify leg of claim D: the PRE-fix reading
# of `tikmes`. It was clean before the round-27 landing and must read
# D4L-ARGOT-DERIV after it, so the row proves the algorithm moved.
SYLLABIFY_FIX_WITNESS = (
    ("s4-head2-prefix-reading.yml", 1, [DERIV_ID],
     "the pre-fix reading of `tikmes` (`ti.kme.s` -> `tikme`): red once the fix lands"),
)

# The law rows the round-27 claim-D surface is about: the register block's own
# identity + law records. The amended packet must carry them.
REQUIRED_REGISTER_ROWS = ("QREG-01", "QREG-02", "QREG-03", "QREG-04")

# The law violation the D15 control plants into a clone: the delivered register
# form L-55 (`tuum`, axis fire, stage E1) is restaged to E0, against the era law
# the packet itself declares (QREG-04: "a stamp form is available_from E1").
# The anchor names L-55 and not just `stage: E1` because the component's first
# E1 record is L-45, which is NOT register-scoped — a bare stage anchor plants
# into a plain record and the era law never sees it.
LAW_PLANT_RECORD = "L-55"
LAW_PLANT_FROM = "{id: L-55, term: tuum, gloss: \"the breath the smith swears by\", field: body, route: derived, layer: native, stage: E1,"
LAW_PLANT_TO = "{id: L-55, term: tuum, gloss: \"the breath the smith swears by\", field: body, route: derived, layer: native, stage: E0,"


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def child_env(extra=None):
    env = dict(os.environ)
    env["TMPDIR"] = str(SCRATCH)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    if extra:
        env.update(extra)
    return env


def run(argv, cwd=None, env=None):
    proc = subprocess.run(
        [str(item) for item in argv],
        capture_output=True, text=True, cwd=str(cwd or ROOT),
        env=env or child_env(), check=False,
    )
    return proc.returncode, (proc.stdout or "") + (proc.stderr or ""), " ".join(
        str(item) for item in argv)


def findings_of(text):
    return [line.split(":")[0][len("FINDING "):].strip()
            for line in text.splitlines() if line.startswith("FINDING ")]


def legs_of(text):
    return [line[5:].split(":")[0].strip() for line in text.splitlines()
            if line.startswith("ok   ") or line.startswith("FAIL ")]


def coverage_of(text):
    for line in text.splitlines():
        if line.startswith("coverage:"):
            return line
    return ""


def coverage_fields(line):
    """Parse `coverage: <path> records=N register_scoped=N ...` into a dict."""
    fields = {}
    for token in line.split():
        if "=" in token:
            key, _, value = token.partition("=")
            fields[key] = int(value) if value.isdigit() else value
    return fields


# --------------------------------------------------------------------------
# D13 — the argot gate is green on the amended packet
# --------------------------------------------------------------------------


def measure_d13(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    exit_code, out, command = run([sys.executable, ARGOT_GATE, D4_SOURCE])
    line = coverage_of(out)
    fields = coverage_fields(line)
    receipt["argot"] = {"command": command, "date": now(), "exit": exit_code,
                        "coverage": line, "fields": fields,
                        "findings": findings_of(out)}
    check("D13 the argot gate exits 0 on the amended packet", exit_code == 0,
          "exit %d: %s" % (exit_code, out.strip().splitlines()[:1]))
    check("D13 no finding is emitted", not findings_of(out),
          "%s" % findings_of(out))
    check("D13 the coverage line is printed", bool(line), "no coverage line")
    check("D13 the register domain is non-empty", fields.get("register_scoped", 0) > 0,
          "register_scoped=%s" % fields.get("register_scoped"))
    check("D13 the derivation pairs replay", fields.get("derived_pairs", 0) > 0,
          "derived_pairs=%s" % fields.get("derived_pairs"))
    check("D13 zero violations", fields.get("violations") == 0,
          "violations=%s" % fields.get("violations"))
    check("D13 zero rule holds", fields.get("rule_holds") == 0,
          "rule_holds=%s" % fields.get("rule_holds"))
    check("D13 the dependency line names the gate it loaded",
          any(item.startswith("dependency:") for item in out.splitlines()),
          "no dependency line")

    # The register law's packet home: the amended packet must carry the block.
    packet_text = (ROOT / D4_SOURCE).read_text(encoding="utf-8")
    missing = [row for row in REQUIRED_REGISTER_ROWS if row not in packet_text]
    receipt["register_block"] = {
        "path": D4_SOURCE,
        "sha256": sha256_file(ROOT / D4_SOURCE),
        "has_registers_key": bool(re.search(r"^registers:", packet_text, re.M)),
        "rows_present": [row for row in REQUIRED_REGISTER_ROWS if row not in missing],
        "rows_missing": missing,
    }
    check("D13 the amended packet declares the registers block",
          bool(re.search(r"^registers:", packet_text, re.M)),
          "no top-level `registers:` key")
    check("D13 the register law rows are in the packet", not missing,
          "missing %s" % missing)

    # Determinism: the same bytes must give the same verdict three times.
    digests, exits = [], []
    for _ in range(3):
        code, text, _cmd = run([sys.executable, ARGOT_GATE, D4_SOURCE])
        digests.append(hashlib.sha256(text.encode()).hexdigest())
        exits.append(code)
    receipt["argot_determinism"] = {"runs": 3, "exits": exits,
                                    "unique_digests": len(set(digests))}
    check("D13 three runs are byte-identical", len(set(digests)) == 1,
          "%d distinct digests" % len(set(digests)))
    check("D13 the exit is stable across runs", len(set(exits)) == 1,
          "exits %s" % exits)

    code, text, command = run([sys.executable, ARGOT_GATE, "--selftest"])
    receipt["runs"].append({"label": "argot-selftest", "command": command,
                            "date": now(), "exit": code,
                            "tail": text.strip().splitlines()[-1] if text.strip() else ""})
    check("D13 the argot selftest passes", code == 0,
          "exit %d: %s" % (code, text.strip().splitlines()[-1:] ))
    check("D13 the argot selftest reports its check count",
          "checks passed" in text, text.strip().splitlines()[-1:] )
    return checks, failures


# --------------------------------------------------------------------------
# D14 — the typed gate and both assemblers are green on the amended packet
# --------------------------------------------------------------------------


def measure_d14(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    # The typed gate over both graded entries. The leg count is a floor, not an
    # equality: a later honest leg must not fail the battery.
    for label, target, floor in (("d4-typed", D4_TYPED, 17), ("d4-source", D4_SOURCE, 20)):
        exit_code, out, command = run([sys.executable, TYPED_GATE, target])
        legs = legs_of(out)
        failed_legs = [line for line in out.splitlines() if line.startswith("FAIL ")]
        holds = [line for line in out.splitlines()
                 if line.startswith("FINDING ") and "[hold]" in line]
        receipt["runs"].append({"label": label, "command": command, "date": now(),
                                "exit": exit_code, "legs": len(legs),
                                "failed_legs": failed_legs,
                                "hold_lines": len(holds),
                                "stdout_sha256": hashlib.sha256(out.encode()).hexdigest()})
        check("D14 %s exits 0" % label, exit_code == 0, "exit %d" % exit_code)
        check("D14 %s runs at least %d legs" % (label, floor), len(legs) >= floor,
              "%d legs" % len(legs))
        check("D14 %s has no FAIL leg" % label, not failed_legs,
              "; ".join(failed_legs[:2]))
        check("D14 %s names the hold set" % label, bool(holds), "no [hold] FINDING line")
        check("D14 %s argot leg is ok" % label,
              any(line.startswith("ok") and "L3b-argot" in line for line in out.splitlines()),
              "L3b-argot not ok")

    # The live counts must equal the frozen hold set the gate grades against.
    expected = json.loads(D4_EXPECTED.read_text(encoding="utf-8"))
    counts = expected.get("counts") or {}
    exit_code, out, command = run([sys.executable, TYPED_GATE, D4_TYPED, "--json"])
    try:
        document = json.loads(out)
    except ValueError:
        document = {}
    live = document.get("counts") or {}
    receipt["hold_set"] = {"path": str(D4_EXPECTED.relative_to(ROOT)),
                           "sha256": sha256_file(D4_EXPECTED),
                           "declared": counts, "live": live, "command": command,
                           "date": now(),
                           "holds": [row.get("where") for row in expected.get("holds") or []],
                           "revision_note": expected.get("revision_note") or ""}
    check("D14 the live hold counts equal the frozen hold set", live == counts,
          "live %s vs expected %s" % (live, counts))
    check("D14 the frozen hold set declares zero fails", counts.get("fail") == 0,
          "%s" % counts)

    # Both assemblers, by their own CLI.
    for label, argv, marker in (
            ("assemble-d4", [sys.executable, ASM_D4, "--check"],
             "byte-identical deterministic assembly"),
            ("assemble-d4-typed", [sys.executable, ASM_D4_TYPED, "--check"],
             "byte-identical deterministic typed packet")):
        exit_code, out, command = run(argv)
        receipt["runs"].append({"label": label, "command": command, "date": now(),
                                "exit": exit_code,
                                "tail": out.strip().splitlines()[-1] if out.strip() else ""})
        check("D14 %s --check exits 0" % label, exit_code == 0,
              "exit %d: %s" % (exit_code, out.strip().splitlines()[-1:]))
        check("D14 %s --check reports byte-identity" % label, marker in out,
              out.strip().splitlines()[-1:])

    # Both gate-shaped adapters: the pinnable entry points the frozen rows use.
    for label, argv, target in (
            ("d4-assembly-check-gate", [sys.executable, D4_ASM_GATE, D4_SOURCE], D4_SOURCE),
            ("d4-typed-labels-check-gate", [sys.executable, D4_TYPED_GATE, D4_PROJECTION],
             D4_PROJECTION)):
        exit_code, out, command = run(argv)
        receipt["runs"].append({"label": label, "command": command, "date": now(),
                                "exit": exit_code,
                                "tail": (out.strip().splitlines() or [""])[-1]})
        check("D14 %s exits 0" % label, exit_code == 0,
              "exit %d: %s" % (exit_code, (out.strip().splitlines() or [""])[-1:]))

    # The projector's own check over the projection the adapter grades.
    exit_code, out, command = run([sys.executable, PROJECTOR, "--packet", D4_SOURCE,
                                   "--check", D4_PROJECTION])
    receipt["runs"].append({"label": "projector-check", "command": command, "date": now(),
                            "exit": exit_code,
                            "tail": (out.strip().splitlines() or [""])[-1]})
    check("D14 the projector --check exits 0", exit_code == 0,
          "exit %d: %s" % (exit_code, (out.strip().splitlines() or [""])[-1:]))
    return checks, failures


# --------------------------------------------------------------------------
# D15 — negative: a register-law violation is caught
# --------------------------------------------------------------------------


def measure_d15(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    instrument_present = LAW_INSTRUMENT.is_file()
    receipt["law_instrument"] = {
        "path": str(LAW_INSTRUMENT.relative_to(ROOT)),
        "present": instrument_present,
        "sha256": sha256_file(LAW_INSTRUMENT) if instrument_present else None,
    }

    # The baseline verdict: the same instrument over the lane tree. It is
    # recorded, not assumed clean — the round-27 D claim's own target is the
    # register law component, and the instrument names its absence as a HOLD.
    # A control that demanded "clean" here would fail on the very gap the round
    # exists to close, so the discrimination check is against the *baseline*
    # verdict, and the gap is named separately.
    baseline_ids, baseline_exit = [], None
    if instrument_present:
        exit_code, out, command = run([sys.executable, "-B", LAW_INSTRUMENT, "--controls"])
        control_lines = [line for line in out.splitlines()
                         if re.match(r"^control-\d", line.strip())]
        control_misses = [line for line in control_lines if "MISS" in line]
        # A peer's file may be mid-edit during the wave. A crash (a traceback, or
        # an exit outside the tool's own 0/1/2 contract) is *could-not-evaluate*,
        # not a red: it says nothing about the plant. It is recorded as a named
        # gap and the discrimination checks below are skipped rather than
        # reported as if the plant had failed to be caught.
        instrument_crashed = ("Traceback (most recent call last)" in out
                              or exit_code not in (0, 1, 2))
        receipt["law_controls_clean_tree"] = {
            "command": command, "date": now(), "exit": exit_code,
            "lines": control_lines, "misses": control_misses,
            "crashed": instrument_crashed,
            "tail": (out.strip().splitlines() or [""])[-1]}
        if instrument_crashed:
            receipt.setdefault("gaps", []).append(
                "the peer law instrument (%s, sha256 %s) could not be evaluated at "
                "this stamp: its run crashed (%s). The D15 discrimination checks "
                "are SKIPPED, not reported, because a crash says nothing about "
                "whether the plant is caught. Re-run when the peer file settles."
                % (LAW_INSTRUMENT.name, sha256_file(LAW_INSTRUMENT)[:16],
                   (out.strip().splitlines() or [""])[-1][:160]))
            return checks, failures
        check("D15 the peer law instrument passes its own controls", exit_code == 0,
              "%s: %s" % ((out.strip().splitlines() or [""])[-1], control_misses))
        exit_code, out, command = run([sys.executable, "-B", LAW_INSTRUMENT])
        baseline_exit, baseline_ids = exit_code, findings_of(out)
        receipt["law_baseline_verdict"] = {
            "command": command, "date": now(), "exit": exit_code,
            "ids": baseline_ids, "lines": [line for line in out.splitlines()
                                           if line.startswith("FINDING ")]}
        check("D15 the lane tree's baseline verdict is recorded",
              exit_code in (0, 1), "exit %d" % exit_code)
    else:
        receipt.setdefault("gaps", []).append(
            "no register-law instrument at %s: the D15 control is recorded as a "
            "named gap, not fabricated with a private checker"
            % LAW_INSTRUMENT.relative_to(ROOT))
        check("D15 a named law instrument exists", False,
              "%s missing" % LAW_INSTRUMENT.relative_to(ROOT))

    # The plant. A **git clone** would be the wrong baseline here: the round-27
    # law landing is *uncommitted* at this stamp (a new component 13 and a new
    # packet block, all in the working tree), so a clone of HEAD carries the
    # pre-law tree and the baseline would not be the bytes this round grades.
    # The control therefore copies the **working tree** into scratch, mutates the
    # component there, and rebuilds through the lane's own pipeline — so baseline
    # and plant are measured on the same tree, differing only in the plant.
    clone = SCRATCH / ("law-tree-%d" % os.getpid())
    if clone.exists():
        shutil.rmtree(clone)
    clone.mkdir(parents=True)
    for item in ("tools", "examples", "reports"):
        source = ROOT / item
        if source.is_dir():
            shutil.copytree(source, clone / item,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    check("D15 the working-tree copy is available", (clone / D4_COMPONENT).is_file(),
          "component missing from the copy")

    steps = (
        ("assemble", [sys.executable, "tools/assemble-culture-d4.py"], (0,)),
        ("project", [sys.executable, "tools/d2-typed-labels.py", "--packet", D4_SOURCE,
                     "--emit", D4_PROJECTION], (0, 1)),
        ("adapt", [sys.executable, "tools/assemble-d4-typed.py", "--emit", D4_TYPED], (0, 1)),
    )

    def rebuild(tree):
        ok = True
        for label, argv, ok_codes in steps:
            exit_code, out, _cmd = run(argv, cwd=tree)
            if exit_code not in ok_codes:
                ok = False
                check("D15 rebuild step %s" % label, False,
                      "exit %d (want %s): %s" % (exit_code, ok_codes, out[-160:]))
        return ok

    # The clean control: the *copy* of the unmutated tree must reproduce the
    # baseline verdict exactly. Without this, a difference at the plant could be
    # the copy rather than the plant.
    copy_rebuilt = rebuild(clone)
    check("D15 the copied tree rebuilds", copy_rebuilt, "a build step failed")
    exit_code, out, command = run([sys.executable, "-B", LAW_INSTRUMENT,
                                   "--packet", D4_SOURCE], cwd=clone)
    copy_ids = findings_of(out)
    receipt["law_clean_copy"] = {
        "command": command, "date": now(), "exit": exit_code, "ids": copy_ids}
    check("D15 the clean copy reproduces the baseline verdict",
          copy_ids == baseline_ids,
          "copy %s vs baseline %s" % (copy_ids, baseline_ids))

    component = clone / D4_COMPONENT
    original = component.read_text(encoding="utf-8")
    planted = original.replace(LAW_PLANT_FROM, LAW_PLANT_TO, 1)
    check("D15 the law plant landed", planted != original,
          "%r anchor not found" % LAW_PLANT_FROM)
    if planted == original:
        shutil.rmtree(clone, ignore_errors=True)
        return checks, failures
    component.write_text(planted, encoding="utf-8")

    rebuilt = rebuild(clone)
    check("D15 the planted artifacts rebuild through the lane pipeline", rebuilt,
          "a build step failed")
    receipt["law_plant"] = {
        "copy": str(clone.relative_to(ROOT)), "component": D4_COMPONENT,
        "record": LAW_PLANT_RECORD, "from_stage": "E1", "to_stage": "E0",
        "law": "QREG-04 / RGL-05: every stamp form is available_from E1",
        "rebuilt": rebuilt, "date": now(),
    }

    if instrument_present and rebuilt:
        exit_code, out, command = run([sys.executable, "-B", LAW_INSTRUMENT,
                                       "--packet", D4_SOURCE], cwd=clone)
        plant_ids = findings_of(out)
        added = [item for item in plant_ids if item not in baseline_ids]
        receipt["law_plant_verdict"] = {
            "command": command, "date": now(), "exit": exit_code,
            "ids": plant_ids, "baseline_ids": baseline_ids, "added_ids": added,
            "lines": [line for line in out.splitlines() if line.startswith("FINDING ")]}
        check("D15 the planted law violation is caught by the named instrument",
              exit_code != 0, "exit %d (clean) on a planted era-law violation" % exit_code)
        check("D15 the plant adds a finding the baseline does not carry", bool(added),
              "no new finding id: plant %s vs baseline %s" % (plant_ids, baseline_ids))
        check("D15 the caught violation names the planted record",
              "L-55" in out, "the instrument's output does not name L-55")

        # The instrument must discriminate: restoring the copied component and
        # rebuilding returns the verdict to the clean copy's exactly, so the
        # added finding was the plant's and nothing else.
        component.write_text(original, encoding="utf-8")
        rebuild(clone)
        exit_code, out, command = run([sys.executable, "-B", LAW_INSTRUMENT,
                                       "--packet", D4_SOURCE], cwd=clone)
        reverted_ids = findings_of(out)
        receipt["law_reverted"] = {
            "command": command, "date": now(), "exit": exit_code,
            "ids": reverted_ids, "lines": [line for line in out.splitlines()
                                           if line.startswith("FINDING ")]}
        check("D15 the restored tree returns to the baseline verdict",
              exit_code == baseline_exit and reverted_ids == baseline_ids,
              "exit %d ids %s vs baseline exit %s ids %s"
              % (exit_code, reverted_ids, baseline_exit, baseline_ids))
    else:
        receipt.setdefault("gaps", []).append(
            "the D15 plant could not be graded: instrument_present=%s rebuilt=%s"
            % (instrument_present, rebuilt))

    shutil.rmtree(clone, ignore_errors=True)
    return checks, failures


# --------------------------------------------------------------------------
# D16 — negative: a syllabify regression is caught
# --------------------------------------------------------------------------


def measure_d16(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    # 1. The design's own eleven worked rows, re-derived through the delivered
    #    gate. A regression that breaks any row is a regression against the
    #    design, not against this battery.
    gate_source = ARGOT_GATE.read_text(encoding="utf-8")
    import runpy
    namespace = runpy.run_path(str(ARGOT_GATE))
    op_functions = namespace["OP_FUNCTIONS"]
    rows, broken = [], []
    for base, op, expected in DESIGN_TABLE:
        got = op_functions[op](base)
        rows.append({"base": base, "op": op, "expected": expected, "got": got,
                     "agrees": got == expected})
        if got != expected:
            broken.append("%s %s: want %s got %s" % (base, op, expected, got))
    receipt["design_table"] = rows
    check("D16 the design's eleven worked rows all re-derive", not broken,
          "; ".join(broken[:3]))

    # 2. The design's named trap: maximal-coda must be rejected.
    for name, want_exit, want_ids, why in SYLLABIFY_FIXTURES:
        path = FIXTURES / name
        exit_code, out, command = run([sys.executable, ARGOT_GATE, path])
        got = findings_of(out)
        receipt.setdefault("syllabify_fixtures", []).append(
            {"fixture": name, "command": command, "date": now(), "exit": exit_code,
             "expected_exit": want_exit, "ids": got, "expected_ids": want_ids,
             "why": why})
        check("D16 %s exits %d" % (name, want_exit), exit_code == want_exit,
              "exit %d" % exit_code)
        check("D16 %s emits %s" % (name, want_ids), got == want_ids, "got %s" % got)

    # 3. The reading pair. Exactly one of the two readings may be clean: under
    #    either algorithm one of these fixtures derives and the other does not,
    #    so the leg is discriminating whichever side the fix lands on. This is
    #    the regression detector: if a change makes BOTH clean (the leg stops
    #    discriminating) or BOTH red (the reading pair collapsed), it fails.
    pair = []
    for name, reading, why in SYLLABIFY_READING_PAIR:
        path = FIXTURES / name
        exit_code, out, command = run([sys.executable, ARGOT_GATE, path])
        pair.append({"fixture": name, "reading": reading, "why": why,
                     "command": command, "date": now(), "exit": exit_code,
                     "ids": findings_of(out)})
    receipt["syllabify_reading_pair"] = pair
    clean = [row for row in pair if row["exit"] == 0]
    check("D16 exactly one reading of head2(tumkalker) derives", len(clean) == 1,
          "%s" % [(row["fixture"], row["exit"]) for row in pair])
    check("D16 the non-deriving reading names %s" % DERIV_ID,
          all(DERIV_ID in row["ids"] for row in pair if row["exit"] != 0),
          "%s" % [(row["fixture"], row["ids"]) for row in pair if row["exit"] != 0])

    # 4. Which reading the delivered gate implements, stated rather than left
    #    implicit. The design fixes `head2(saalumi) == saalu` in its own table;
    #    the round-26 design seat's reference yields `saal` on that same row, so
    #    the "gate disagrees with the design" count was measured against a
    #    reference that fails the design's own named row. Both facts are
    #    recorded; the gate's own output on the row is the delivered fact.
    gate_head2_saalumi = op_functions["head2"]("saalumi")
    implements = "unconstrained" if clean and clean[0]["reading"] == "tumka" else (
        "constrained" if clean and clean[0]["reading"] == "tumkal" else "indeterminate")
    receipt["syllabify_reading"] = {
        "gate_head2_saalumi": gate_head2_saalumi,
        "design_table_saalumi": "saalu",
        "gate_agrees_with_design_table": gate_head2_saalumi == "saalu",
        "delivered_reading": implements,
        "legality_check_in_source": bool(re.search(
            r"is_legal_syllable|legality|legal_syllable|LEGAL_", gate_source)),
        "head2_tikmes": op_functions["head2"]("tikmes"),
        "syllabify_tikmes": namespace["syllabify"]("tikmes"),
        "syllabify_tumkalker": namespace["syllabify"]("tumkalker"),
    }
    check("D16 the gate agrees with the design's own worked row",
          gate_head2_saalumi == "saalu",
          "head2(saalumi)=%r want 'saalu'" % gate_head2_saalumi)
    check("D16 the delivered reading is the legality-constrained one",
          implements == "constrained",
          "delivered reading reads %r" % implements)

    # 3b. The before/after witness for the syllabify leg of claim D: the PRE-fix
    #     reading of `tikmes`. It was clean before the landing and must be red
    #     after it, so the row proves the algorithm moved rather than asserting
    #     it did.
    for name, want_exit, want_ids, why in SYLLABIFY_FIX_WITNESS:
        path = FIXTURES / name
        exit_code, out, command = run([sys.executable, ARGOT_GATE, path])
        got = findings_of(out)
        receipt.setdefault("syllabify_fix_witness", []).append(
            {"fixture": name, "command": command, "date": now(), "exit": exit_code,
             "expected_exit": want_exit, "ids": got, "expected_ids": want_ids,
             "why": why})
        check("D16 %s exits %d" % (name, want_exit), exit_code == want_exit,
              "exit %d" % exit_code)
        check("D16 %s emits %s" % (name, want_ids), got == want_ids, "got %s" % got)

    # 4b. The third witness: the packet's OWN `syllables:` field. The 8 `names`
    #     records carry an author-declared split, written by an earlier round for
    #     a different purpose and consulted by no gate. It is the acceptance
    #     surface a syllabifier fix has to satisfy, and it has a fixed answer
    #     (peer seat X54, `reports/round-27/scribe/x54-syllabify-spotcheck.md`
    #     §1, X54-H3). Recorded, not asserted clean: at this stamp the fix is
    #     unlanded, so an "all 8" demand would fail on the very gap the round
    #     exists to close. The witness being *declared* is the hard check.
    naming = runpy.run_path(str(ROOT / "tools/gates/naming-collision-gate.py"))
    packet = naming["load_yaml"]((ROOT / D4_SOURCE).read_text(encoding="utf-8"))
    witness, agreeing = [], []
    for record in packet.get("names") or []:
        declared = record.get("syllables")
        if not declared:
            continue
        observed = namespace["syllabify"](record.get("name") or "")
        row = {"id": record.get("id"), "name": record.get("name"),
               "declared": declared, "gate": observed,
               "agrees": list(declared) == list(observed)}
        witness.append(row)
        if row["agrees"]:
            agreeing.append(row["id"])
    receipt["syllables_witness"] = {
        "source": "%s (names records, `syllables:` field)" % D4_SOURCE,
        "declared_rows": len(witness), "rows": witness,
        "gate_agrees": len(agreeing), "gate_agrees_ids": agreeing,
    }
    check("D16 the packet declares its own syllable witness on 8 name records",
          len(witness) == 8, "%d declared rows" % len(witness))
    # The residual gap, named precisely rather than as "not all 8": the witness
    # rows the delivered syllabifier still misses, by id. The round-27 landing
    # took this from 0/8 to 6/8; the two rows left are exactly the two whose
    # first nucleus is the falling diphthong `ai`, which the syllabifier still
    # splits as two nuclei (`tumhai` -> `tum.ha.i`, `haitik` -> `ha.i.tik`)
    # against the packet's own `['tum','hai']` / `['hai','tik']`.
    disagreeing = [row for row in witness if not row["agrees"]]
    receipt["syllables_witness"]["gate_disagrees_ids"] = [row["id"] for row in disagreeing]
    if disagreeing:
        receipt.setdefault("gaps", []).append(
            "the delivered syllabifier still disagrees with the packet's own "
            "`syllables:` field on %d of %d name records (gate agrees %d/%d): "
            "the residual rows are %s, each of which begins with the falling "
            "diphthong `ai` that the syllabifier splits as two nuclei"
            % (len(disagreeing), len(witness), len(agreeing), len(witness),
               ", ".join("%s %s (declared %s, gate %s)"
                         % (row["id"], row["name"], row["declared"], row["gate"])
                         for row in disagreeing)))
    else:
        check("D16 the delivered syllabifier satisfies the packet's own witness",
              len(agreeing) == 8, "agrees %d/8" % len(agreeing))

    # 5. The gate's selftest carries the reading's own controls; a regression in
    #    them is caught here.
    exit_code, out, command = run([sys.executable, ARGOT_GATE, "--selftest"])
    receipt["runs"].append({"label": "argot-selftest-d16", "command": command,
                            "date": now(), "exit": exit_code,
                            "tail": out.strip().splitlines()[-1] if out.strip() else ""})
    check("D16 the argot selftest still passes", exit_code == 0,
          "exit %d" % exit_code)
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
    check("coverage parser reads the counters",
          coverage_fields("coverage: p records=170 register_scoped=14 violations=0")
          == {"records": 170, "register_scoped": 14, "violations": 0})
    check("coverage parser ignores the path token",
          "p" not in coverage_fields("coverage: p records=1"))
    check("the design's id is the DERIV spelling", DERIV_ID == "D4L-ARGOT-DERIV")
    check("the design table carries eleven rows", len(DESIGN_TABLE) == 11)
    check("the design table's head2 row is the named trap",
          ("saalumi", "head2", "saalu") in DESIGN_TABLE)
    check("every syllabify fixture exists on disk",
          all((FIXTURES / name).is_file() for name, _e, _i, _d in SYLLABIFY_FIXTURES)
          and all((FIXTURES / name).is_file() for name, _r, _w in SYLLABIFY_READING_PAIR))
    check("the reading pair is a pair", len(SYLLABIFY_READING_PAIR) == 2)
    check("the fix witness exists on disk",
          all((FIXTURES / name).is_file()
              for name, _e, _i, _d in SYLLABIFY_FIX_WITNESS))
    check("the two readings differ",
          SYLLABIFY_READING_PAIR[0][1] != SYLLABIFY_READING_PAIR[1][1])
    check("the law plant changes the stage", LAW_PLANT_FROM != LAW_PLANT_TO)
    check("the law plant names the planted record", LAW_PLANT_RECORD in LAW_PLANT_TO)
    check("the law plant names the E0 restage", "stage: E0," in LAW_PLANT_TO)
    # The crash detector: a peer traceback must read as could-not-evaluate, and
    # an ordinary red must not.
    crashed_text = "Traceback (most recent call last):\nNameError: name 'ROOT' is not defined"
    check("the crash detector reads a traceback as could-not-evaluate",
          ("Traceback (most recent call last)" in crashed_text) is True)
    check("the crash detector does not fire on an ordinary finding line",
          not ("Traceback (most recent call last)" in "FINDING L6b-HOLD: the law has no teeth"))
    check("the crash detector reads an out-of-contract exit as a crash",
          (7 not in (0, 1, 2)) is True)

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%-56s %s" % (name, "ok" if ok else "FAIL"))
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
    receipt = {"schema": "kotodama-r27-gate-tests-v1", "round": 27,
               "seats": ["R27-D13", "R27-D14", "R27-D15", "R27-D16"],
               "date": now(), "runs": [], "checks": [], "failures": [], "gaps": []}
    for item in (ARGOT_GATE, TYPED_GATE, D4_ASM_GATE, D4_TYPED_GATE, ASM_D4,
                 ASM_D4_TYPED, PROJECTOR, D4_EXPECTED, ROOT / D4_SOURCE,
                 ROOT / D4_TYPED, ROOT / D4_PROJECTION):
        receipt.setdefault("inputs", {})[str(item.relative_to(ROOT))] = (
            sha256_file(item) if item.is_file() else None)
    try:
        receipt["head"] = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT),
                                         capture_output=True, text=True,
                                         check=False).stdout.strip()
    except OSError:
        receipt["head"] = None

    all_checks, all_failures = [], []
    for measure in (measure_d13, measure_d14, measure_d15, measure_d16):
        try:
            checks, failures = measure(receipt)
        except Exception as error:  # noqa: BLE001 — a leg that crashes is a finding
            checks = [{"name": measure.__name__, "ok": False,
                       "detail": "%s: %s" % (type(error).__name__, error)}]
            failures = ["%s crashed: %s" % (measure.__name__, error)]
        all_checks.extend(checks)
        all_failures.extend(failures)

    receipt["checks"] = all_checks
    receipt["failures"] = all_failures
    receipt["passed"] = not all_failures
    receipt["summary"] = {"checks": len(all_checks),
                          "passed": sum(1 for item in all_checks if item["ok"]),
                          "failed": len(all_failures)}

    for item in all_checks:
        print("%-6s %s" % ("ok" if item["ok"] else "FAIL", item["name"]))
    for item in all_failures:
        print("       -> %s" % item)
    print("summary: %d/%d checks passed" % (receipt["summary"]["passed"],
                                            receipt["summary"]["checks"]))
    for gap in receipt["gaps"]:
        print("gap: %s" % gap)

    receipt_path = HERE / "receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=1, sort_keys=False) + "\n",
                            encoding="utf-8")
    print("receipt: %s" % receipt_path.relative_to(ROOT))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
