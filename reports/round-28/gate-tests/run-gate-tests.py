#!/usr/bin/env python3
r"""run-gate-tests.py — round-28 gate+tests battery (seats R28-D13..D16).

Four seats, four questions, one runner. Round 27 asked whether the law could be
*read*; round 28 asks whether it can be *replayed* — so every seat here is
stated against a tamper, and every tamper is graded on the amended packet:

  D13  the argot gate is green on the amended packet (register block + RL-4
       records present + coverage + determinism + selftest)
  D14  the typed gate and BOTH assemblers are green on the amended packet
       (live counts == frozen hold set; both adapters; the projector)
  D15  negative: a tampered register-law row is caught — `force` and `speaker`
       each planted into a clone, each required to raise a NAMED `D4L-LAW-*`
       finding the clean tree does not carry (round 27's RL-1: neither did)
  D16  the RL-4 fix is *present* (OR/LI/EN records reach the packet by id) and
       the standing argot regression detector still discriminates (the design's
       eleven worked rows + the filed syllabify reading pair)

Usage
-----
    python3 reports/round-28/gate-tests/run-gate-tests.py            # measure + write receipt
    python3 reports/round-28/gate-tests/run-gate-tests.py --check    # measure only, print
    python3 reports/round-28/gate-tests/run-gate-tests.py --selftest # dependency-free controls

Design rules this runner works inside
-------------------------------------
* Every measurement names its command, its exit code and its date. A battery
  that cannot say which bytes it ran is not evidence.
* The teeth control plants into a **clone**, never the lane worktree: a control
  that moves the tree it measures is not a control.
* A negative is only a negative if a **named instrument** catches it, and only a
  control if the clean tree passes the same instrument. Where the round-28 law
  surface has no owning lane gate, that is recorded as a named gap rather than
  papered over with a private checker.
* The law instrument is **discovered, not hardcoded**: round 28's claim D lands
  the replay leg in a file this battery does not own, and a battery that named
  the path in advance would pass on a tree where the path exists but the leg
  does not. Discovery is by content (the `D4L-LAW` class token or the
  `register_law` block) over the delivered trees.
* No file outside `reports/round-28/gate-tests/` and `.scratch/` is written.
  Read-only over `examples/`, `tools/`, `corpus/` and every filed round-8..27
  byte.

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
SCRATCH = ROOT / ".scratch" / "r28-d13"
FIXTURES = HERE / "fixtures"
R27_FIXTURES = ROOT / "reports" / "round-27" / "gate-tests" / "fixtures"

ARGOT_GATE = ROOT / "tools/gates/argot-derivation-gate.py"
TYPED_GATE = ROOT / "tools/gates/typed-pipeline-gate.py"
D4_ASM_GATE = ROOT / "tools/gates/d4-assembly-check-gate.py"
D4_TYPED_GATE = ROOT / "tools/gates/d4-typed-labels-check-gate.py"
ASM_D4 = ROOT / "tools/assemble-culture-d4.py"
ASM_D4_TYPED = ROOT / "tools/assemble-d4-typed.py"
PROJECTOR = ROOT / "tools/d2-typed-labels.py"
NAMING = ROOT / "tools/gates/naming-collision-gate.py"

D4_SOURCE = "examples/culture-d4/packet.d4.yml"
D4_TYPED = "examples/culture-d4/packet.d4.typed.yml"
D4_PROJECTION = "examples/culture-d4/typed-labels.d4.yml"
D4_EXPECTED = ROOT / "examples/culture-d4/expected-holds.json"
D4_COMPONENT = "examples/culture-d4/components/04-lexicon.yml"
LAW_COMPONENT = "examples/culture-d4/components/13-register-law.yml"
ORTH_COMPONENT = "examples/culture-d4/components/03-orthography.yml"
COSTUME_COMPONENT = "examples/culture-d4/components/09-costumes.yml"

# The law class the round-28 claim D names. A finding is only "named" if a
# delivered instrument emits a token in this class; a bare nonzero exit is not
# a name.
LAW_CLASS = "D4L-LAW"

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

# The register block's own identity rows. The amended packet must carry them.
REQUIRED_REGISTER_ROWS = ("QREG-01", "QREG-02", "QREG-03", "QREG-04")

# RL-4's substance: the records the round-27 review measured as never reaching
# the packet. OR-01..03 are 03-orthography's `records`; LI-01..03 its
# `literacy_institutions`; EN-01..02 09-costumes' `enforcement`. Round 28 fixes
# the components' `packet_keys`; this battery checks the records **by id**,
# wherever the fix homes them, so a fix that renames the block is not a false
# red and a fix that declares the key but drops the records is not a false green.
RL4_RECORD_IDS = ("OR-01", "OR-02", "OR-03", "LI-01", "LI-02", "LI-03",
                  "EN-01", "EN-02")
# The component-only keys the round-27 review named. The fix must move these out
# of `assembly.skipped_keys`; a key still skipped is still invisible.
RL4_KEYS = ("records", "literacy_institutions", "enforcement")

# The plants. Each is a (label, component, from, to, law) row: the anchor is the
# delivered text, the replacement is the same text with one law value moved.
# Anchors name the ROW, not a bare field value, so a plant cannot land in a
# neighbouring record — `force:` appears five times in the component.
#
# The `speaker` plant keeps an `(ID)` parenthetical on purpose. The delivered leg
# resolves a speaker by the id in `Name (ID)`, so a plant that strips the id
# entirely gives the leg nothing to resolve and is invisible for a *different*
# reason than the one under test — this seat measured that mistake before fixing
# it (§2 of the D15 artifact). The plant therefore moves the id to an
# unresolvable one (`ZZ-99`), which is the shape the round's own acceptance
# runner uses and the shape the design's own C-3 control uses.
LAW_PLANTS = (
    ("force", LAW_COMPONENT,
     'force: "directive-binding for the charge; declarative-naming for the lot\'s name"',
     'force: "no-such-force"',
     "RGL-01: `force` is the illocutionary value; a value outside the declared "
     "vocabulary is a defect (RL-1's tamper, round 27 measured it invisible)"),
    ("speaker", LAW_COMPONENT,
     'mold-keeper (OR-02, component-only)',
     'mold-keeper (ZZ-99)',
     "RGL-01: `speaker` is who may speak the act; an agent id that resolves to "
     "no delivered record is a defect (the round-28 claim's second named "
     "negative; the design's C-3 control shape)"),
)

# Discovery. Two surfaces, kept separate because they answer different
# questions:
#
#   LEG_GLOBS   — where a *delivered* law-replay leg may live: the lane's tool
#                 and gate trees. The round-28 claim's clause is "no tool under
#                 `tools/` names a `D4L-LAW-*` finding id", so this is the
#                 surface the D15 negative is graded on.
#   AUDIT_GLOBS — the round's own audit/scribe tools. They are recorded as
#                 corroborating readers (a second opinion is evidence), but they
#                 are *not* the delivered leg: an audit tool that catches a
#                 tamper does not give the law teeth in the pipeline, and the
#                 round's acceptance runner lives under `reports/round-28/` and
#                 takes a `--round` argument, not a packet.
LEG_GLOBS = ("tools/gates/*.py", "tools/*.py")
AUDIT_GLOBS = ("reports/round-28/audit/*.py", "reports/round-28/scribe/*.py",
               "reports/round-28/law/*.py", "reports/round-28/replay/*.py")

# The clone's read set. The lane's own gates resolve ROOT from their file
# position, so a clone needs the trees they read; `corpus/` is included because
# the provenance gates read it and a law replay may cite a knowledge entry.
CLONE_TREES = ("tools", "examples", "corpus")


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


def run(argv, cwd=None, env=None, timeout=300):
    try:
        proc = subprocess.run(
            [str(item) for item in argv],
            capture_output=True, text=True, cwd=str(cwd or ROOT),
            env=env or child_env(), check=False, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return 2, "could-not-run: timeout after %ss" % timeout, " ".join(
            str(item) for item in argv)
    except OSError as error:
        return 2, "could-not-run: %s" % error, " ".join(str(item) for item in argv)
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


def law_tokens(text):
    """Every named `D4L-LAW-*` token a tool's output carries.

    A NAMED finding is a token in the claim's class; an anonymous failure (a
    bare nonzero exit, a traceback) is deliberately NOT counted, because the
    claim names the class and a battery that accepted any red would pass on a
    tool that crashed rather than one that checked.
    """
    tokens = set()
    for line in text.splitlines():
        for match in re.finditer(r"\bD4L-LAW-[A-Z0-9-]+\b", line):
            tokens.add(match.group(0))
    return sorted(tokens)


def load_packet(path):
    """Load a packet through the lane's own reader (read-only, runpy by path)."""
    import runpy
    namespace = runpy.run_path(str(NAMING))
    return namespace["load_yaml"](Path(path).read_text(encoding="utf-8"))


def packet_record_ids(packet):
    """Every record id in every list block of a packet, with its block name."""
    found = {}
    for key, value in packet.items():
        if not isinstance(value, list):
            continue
        for record in value:
            if not isinstance(record, dict):
                continue
            record_id = record.get("id")
            if isinstance(record_id, str) and record_id:
                found.setdefault(record_id, []).append(key)
    return found


def discover_law_instruments(globs):
    """Find files under `globs` that could carry the law's replay leg.

    Discovered by content, not by path: a file that mentions the claim's own
    class token or the `register_law` block. The battery never asserts that a
    discovered file *is* the leg; it runs it and reads what it emits.
    """
    found = []
    seen = set()
    self_path = Path(__file__).resolve()
    for pattern in globs:
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file() or path in seen:
                continue
            seen.add(path)
            if path.resolve() == self_path:
                continue
            try:
                source = path.read_text(errors="replace")
            except OSError:
                continue
            if LAW_CLASS in source or "register_law" in source:
                found.append(path)
    return found


def law_instrument_shape(path, packet):
    """Which argument shape an instrument takes for its packet — **probed**, not
    read off `--help`.

    Three shapes exist in this lane: `--packet PATH` (the lane gates and the
    round-28 law auditor), a positional packet path, and no packet argument at
    all (the sweep auditors, which read the tree). The shape is established by
    **trying each** and keeping the first whose invocation is not an argparse
    usage error, because a help-text sniff mis-reads: `x60-sweep-completeness.py`
    takes no packet, yet its `--help` mentions the word "packet" in its prose,
    and a sniffer handed it a packet that it then rejected with exit 2 — which
    this battery would have recorded as "no named finding" and graded as a
    verdict. A usage error is not a verdict; the probe says so explicitly.
    """
    attempts = (
        ("--packet", [sys.executable, "-B", str(path), "--packet", str(packet)]),
        ("positional", [sys.executable, "-B", str(path), str(packet)]),
        ("none", [sys.executable, "-B", str(path)]),
    )
    detail = []
    for shape, argv in attempts:
        exit_code, out, _cmd = run(argv)
        usage_error = (exit_code == 2 and "usage:" in out
                       and ("error:" in out or "unrecognized arguments" in out))
        detail.append({"shape": shape, "exit": exit_code,
                       "usage_error": usage_error,
                       "tail": (out.strip().splitlines() or [""])[-1][:160]})
        if not usage_error:
            return shape, detail
    return None, detail


def law_instrument_argv(path, packet, shape):
    """The argv that runs `path` over `packet` under the discovered `shape`."""
    if shape == "--packet":
        return [sys.executable, "-B", str(path), "--packet", str(packet)]
    if shape == "positional":
        return [sys.executable, "-B", str(path), str(packet)]
    return [sys.executable, "-B", str(path)]


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
    check("D13 the register domain is non-empty",
          fields.get("register_scoped", 0) > 0,
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
        "has_register_law_key": bool(re.search(r"^register_law:", packet_text, re.M)),
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
          "exit %d: %s" % (code, text.strip().splitlines()[-1:]))
    check("D13 the argot selftest reports its check count",
          "checks passed" in text, text.strip().splitlines()[-1:])
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
        check("D14 %s names the hold set" % label, bool(holds),
              "no [hold] FINDING line")
        check("D14 %s argot leg is ok" % label,
              any(line.startswith("ok") and "L3b-argot" in line
                  for line in out.splitlines()),
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
    for label, argv in (
            ("d4-assembly-check-gate", [sys.executable, D4_ASM_GATE, D4_SOURCE]),
            ("d4-typed-labels-check-gate",
             [sys.executable, D4_TYPED_GATE, D4_PROJECTION])):
        exit_code, out, command = run(argv)
        receipt["runs"].append({"label": label, "command": command, "date": now(),
                                "exit": exit_code,
                                "tail": (out.strip().splitlines() or [""])[-1]})
        check("D14 %s exits 0" % label, exit_code == 0,
              "exit %d: %s" % (exit_code, (out.strip().splitlines() or [""])[-1:]))

    # The projector's own check over the projection the adapter grades.
    exit_code, out, command = run([sys.executable, PROJECTOR, "--packet", D4_SOURCE,
                                   "--check", D4_PROJECTION])
    receipt["runs"].append({"label": "projector-check", "command": command,
                            "date": now(), "exit": exit_code,
                            "tail": (out.strip().splitlines() or [""])[-1]})
    check("D14 the projector --check exits 0", exit_code == 0,
          "exit %d: %s" % (exit_code, (out.strip().splitlines() or [""])[-1:]))
    return checks, failures


# --------------------------------------------------------------------------
# D15 — negative: a tampered register-law row is caught
# --------------------------------------------------------------------------


def measure_d15(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    leg = discover_law_instruments(LEG_GLOBS)
    auditors = [path for path in discover_law_instruments(AUDIT_GLOBS)
                if path not in leg]
    instruments = leg + auditors
    shapes = {}
    for path in instruments:
        shape, probe = law_instrument_shape(path, ROOT / D4_SOURCE)
        shapes[str(path.relative_to(ROOT))] = {"shape": shape, "probe": probe}
    receipt["law_instruments"] = [
        {"path": str(path.relative_to(ROOT)),
         "surface": "leg" if path in leg else "audit",
         "sha256": sha256_file(path) if path.is_file() else None,
         "packet_arg_shape": shapes[str(path.relative_to(ROOT))]["shape"]}
        for path in instruments]
    runnable = [path for path in instruments
                if shapes[str(path.relative_to(ROOT))]["shape"] is not None]
    # The D15 negative is graded on the **leg** surface: the claim's clause is
    # "no tool under `tools/` names a `D4L-LAW-*` finding id". The audit
    # instruments are run as corroborating readers and recorded, but a catch by
    # an audit tool is not teeth in the pipeline.
    leg_runnable = [path for path in runnable if path in leg]
    receipt["law_instrument_shapes"] = shapes

    # The clean baseline, on the lane tree, from every discovered instrument
    # whose packet-argument shape could be established. An instrument that
    # accepts no packet (the sweep auditors, which read the tree) is recorded as
    # such rather than run into a usage error and reported as "no finding" —
    # that would grade this battery's own typo as a verdict.
    baseline = {}
    for path in runnable:
        rel = str(path.relative_to(ROOT))
        exit_code, out, command = run(law_instrument_argv(
            path, ROOT / D4_SOURCE, shapes[rel]["shape"]))
        baseline[rel] = {"command": command, "date": now(), "exit": exit_code,
                         "tokens": law_tokens(out),
                         "findings": findings_of(out),
                         "crash": ("Traceback (most recent call last)" in out
                                   or exit_code not in (0, 1, 2)),
                         "tail": (out.strip().splitlines() or [""])[-1]}
    receipt["law_baseline"] = baseline
    for path in instruments:
        rel = str(path.relative_to(ROOT))
        if rel not in baseline:
            receipt.setdefault("gaps", []).append(
                "the discovered instrument %s accepts no packet argument in any "
                "of the three probed shapes (--packet PATH, positional PATH, no "
                "argument): it is recorded but not run, because handing it a "
                "packet measures an argparse error rather than a verdict"
                % path.relative_to(ROOT))

    check("D15 a delivered leg instrument exists on the `tools/` surface",
          bool(leg), "no file under tools/ mentions %s or register_law" % LAW_CLASS)
    if not runnable:
        receipt.setdefault("gaps", []).append(
            "no discovered instrument accepts a packet and mentions the `%s` "
            "class or the `register_law` block: the D15 negative is recorded as "
            "a named gap, not fabricated with a private checker" % LAW_CLASS)
        check("D15 a named law instrument exists", False,
              "no runnable instrument mentions %s" % LAW_CLASS)
        return checks, failures

    # The clone. A git clone would be the wrong baseline: the round-28 landing
    # is *uncommitted* at this stamp, so a clone of HEAD carries the pre-landing
    # tree and the baseline would not be the bytes this round grades. The
    # control copies the **working tree**, mutates the component there, and
    # rebuilds through the lane's own pipeline — so baseline and plant are
    # measured on the same tree, differing only in the plant.
    clone = SCRATCH / ("law-tree-%d" % os.getpid())
    if clone.exists():
        shutil.rmtree(clone)
    clone.mkdir(parents=True)
    for item in CLONE_TREES:
        source = ROOT / item
        if source.is_dir():
            shutil.copytree(source, clone / item,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    # The instruments must resolve their own ROOT inside the clone, so they are
    # copied at their own relative path, not into a scratch bin. Only the **leg**
    # surface is cloned: the audit tools read `reports/round-28/` (which is not
    # part of the clone's read set) and would differ from the baseline for that
    # reason rather than the plant's, so they are recorded on the lane tree and
    # not used as plant controls.
    for path in leg_runnable:
        target = clone / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    receipt["law_clone"] = {
        "path": str(clone.relative_to(ROOT)),
        "trees": [item for item in CLONE_TREES if (ROOT / item).is_dir()],
        "instruments": [str(path.relative_to(ROOT)) for path in leg_runnable],
        "audit_instruments_not_cloned": [str(path.relative_to(ROOT))
                                         for path in runnable
                                         if path not in leg_runnable],
    }
    check("D15 the working-tree copy is available", (clone / D4_COMPONENT).is_file(),
          "component missing from the copy")
    check("D15 the law component is in the copy", (clone / LAW_COMPONENT).is_file(),
          "law component missing from the copy")

    steps = (
        ("assemble", [sys.executable, "tools/assemble-culture-d4.py"], (0,)),
        ("project", [sys.executable, "tools/d2-typed-labels.py", "--packet", D4_SOURCE,
                     "--emit", D4_PROJECTION], (0, 1)),
        ("adapt", [sys.executable, "tools/assemble-d4-typed.py", "--emit", D4_TYPED],
         (0, 1)),
    )

    def rebuild(tree):
        ok = True
        for label, argv, ok_codes in steps:
            exit_code, out, _cmd = run(argv, cwd=tree)
            if exit_code not in ok_codes:
                ok = False
                check("D15 rebuild step %s" % label, False,
                      "exit %d (want %s): %s" % (exit_code, ok_codes, out[-200:]))
        return ok

    # The clean control: the *copy* of the unmutated tree must reproduce the
    # baseline verdict exactly. Without this, a difference at the plant could be
    # the copy rather than the plant.
    copy_rebuilt = rebuild(clone)
    check("D15 the copied tree rebuilds", copy_rebuilt, "a build step failed")
    clean_copy = {}
    for path in leg_runnable:
        rel = str(path.relative_to(ROOT))
        exit_code, out, command = run(law_instrument_argv(
            clone / rel, clone / D4_SOURCE, shapes[rel]["shape"]), cwd=clone)
        clean_copy[rel] = {"command": command, "date": now(), "exit": exit_code,
                           "tokens": law_tokens(out), "findings": findings_of(out)}
    receipt["law_clean_copy"] = clean_copy
    for rel, row in clean_copy.items():
        check("D15 the clean copy reproduces the baseline verdict (%s)"
              % Path(rel).name,
              row["tokens"] == baseline[rel]["tokens"]
              and row["exit"] == baseline[rel]["exit"],
              "copy %s/%s vs baseline %s/%s"
              % (row["exit"], row["tokens"], baseline[rel]["exit"],
                 baseline[rel]["tokens"]))

    # The plants, one at a time, each into its own fresh copy of the component
    # so the second plant is never measured on the first plant's bytes.
    component = clone / LAW_COMPONENT
    original = component.read_text(encoding="utf-8")
    planted_rows = []
    for label, _component, anchor, replacement, law in LAW_PLANTS:
        planted = original.replace(anchor, replacement, 1)
        landed = planted != original
        check("D15 the %s plant lands on the delivered bytes" % label, landed,
              "%r not found in %s" % (anchor[:60], LAW_COMPONENT))
        if not landed:
            continue
        component.write_text(planted, encoding="utf-8")
        rebuilt = rebuild(clone)
        check("D15 the %s plant rebuilds through the lane pipeline" % label, rebuilt,
              "a build step failed")
        verdicts = {}
        if rebuilt:
            for path in leg_runnable:
                rel = str(path.relative_to(ROOT))
                exit_code, out, command = run(law_instrument_argv(
                    clone / rel, clone / D4_SOURCE, shapes[rel]["shape"]), cwd=clone)
                added = sorted(set(law_tokens(out)) - set(baseline[rel]["tokens"]))
                verdicts[rel] = {
                    "command": command, "date": now(), "exit": exit_code,
                    "tokens": law_tokens(out), "added_named": added,
                    "findings": findings_of(out),
                    "lines": [line for line in out.splitlines()
                              if line.startswith("FINDING ")][:8]}
        # The leg surface decides the D15 verdict. Where the leg is empty (the
        # law is designed, not landed), the corroborating audit instruments are
        # consulted as a second opinion and their answer is recorded separately
        # — but a catch by an auditor is not teeth in the pipeline, so it does
        # not turn the leg check green.
        added_leg = sorted({token for row in verdicts.values()
                            for token in row["added_named"]})
        audit_verdicts = {}
        for path in runnable:
            if path in leg_runnable:
                continue
            rel = str(path.relative_to(ROOT))
            exit_code, out, command = run(law_instrument_argv(
                path, ROOT / D4_SOURCE, shapes[rel]["shape"]))
            audit_verdicts[rel] = {
                "command": command, "date": now(), "exit": exit_code,
                "tokens": law_tokens(out),
                "added_named": sorted(set(law_tokens(out))
                                      - set(baseline[rel]["tokens"]))}
        added_audit = sorted({token for row in audit_verdicts.values()
                              for token in row["added_named"]})
        caught = bool(added_leg)
        planted_rows.append({
            "label": label, "law": law, "anchor": anchor, "replacement": replacement,
            "landed": landed, "rebuilt": rebuilt, "verdicts": verdicts,
            "added_named": added_leg, "caught": caught,
            "audit_verdicts": audit_verdicts, "audit_added_named": added_audit,
            "date": now()})
        check("D15 the tampered `%s` is caught by a named %s finding" % (label, LAW_CLASS),
              caught,
              "no new named %s token on the leg surface; audit surface adds %s"
              % (LAW_CLASS, added_audit or "nothing"))
        # The plant must discriminate: restoring the component and rebuilding
        # returns the verdict to the baseline's exactly, so the added finding
        # was the plant's and nothing else. Where the leg surface is EMPTY this
        # check has nothing to compare, so it is recorded as vacuous rather than
        # reported as a pass — a green over an empty set is the same failure
        # mode as a probe that reads a usage error as a verdict.
        component.write_text(original, encoding="utf-8")
        rebuild(clone)
        reverted = {}
        for path in leg_runnable:
            rel = str(path.relative_to(ROOT))
            exit_code, out, _cmd = run(law_instrument_argv(
                clone / rel, clone / D4_SOURCE, shapes[rel]["shape"]), cwd=clone)
            reverted[rel] = {"exit": exit_code, "tokens": law_tokens(out)}
        if not leg_runnable:
            planted_rows[-1]["reverted_vacuous"] = True
            receipt.setdefault("gaps", []).append(
                "the D15 restore check for the `%s` plant is VACUOUS: the leg "
                "surface under `tools/` is empty, so there is no instrument whose "
                "verdict could return to the baseline. Recorded as vacuous, not "
                "reported as a pass." % label)
        check("D15 the restored tree returns to the baseline verdict (%s)" % label,
              bool(leg_runnable) and all(
                  reverted[rel]["tokens"] == baseline[rel]["tokens"]
                  and reverted[rel]["exit"] == baseline[rel]["exit"]
                  for rel in reverted),
              "%s" % reverted)
        planted_rows[-1]["reverted"] = reverted

    receipt["law_plants"] = planted_rows
    if planted_rows and not any(row["caught"] for row in planted_rows):
        receipt.setdefault("gaps", []).append(
            "RL-1 still open at this stamp: tampering a register-law row "
            "(`force`, `speaker`) produced no NEW named `%s-*` finding on the "
            "delivered leg surface (%d leg instrument(s) under `tools/`; %d "
            "corroborating auditor(s) also ran). The law is a declaration with "
            "no replay leg. The D15 checks above are red, not skipped, because "
            "the plant landed and rebuilt."
            % (LAW_CLASS, len(leg_runnable), len(audit_verdicts)))

    shutil.rmtree(clone, ignore_errors=True)
    return checks, failures


# --------------------------------------------------------------------------
# D16 — the RL-4 fix is present, and the standing regression detector still
#       discriminates
# --------------------------------------------------------------------------


def measure_d16(receipt):
    checks, failures = [], []

    def check(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s: %s" % (name, detail))

    # ---- RL-4 presence, by record id ------------------------------------
    packet = load_packet(ROOT / D4_SOURCE)
    ids = packet_record_ids(packet)
    present = [record_id for record_id in RL4_RECORD_IDS if record_id in ids]
    absent = [record_id for record_id in RL4_RECORD_IDS if record_id not in ids]
    skipped = (packet.get("assembly") or {}).get("skipped_keys") or {}
    still_skipped = sorted(key for key in RL4_KEYS if key in skipped)
    receipt["rl4"] = {
        "source": D4_SOURCE,
        "sha256": sha256_file(ROOT / D4_SOURCE),
        "date": now(),
        "required_ids": list(RL4_RECORD_IDS),
        "present_ids": present,
        "absent_ids": absent,
        "id_home_blocks": {record_id: ids.get(record_id) for record_id in present},
        "component_keys": {
            ORTH_COMPONENT: _declared_keys(ORTH_COMPONENT),
            COSTUME_COMPONENT: _declared_keys(COSTUME_COMPONENT),
        },
        "still_skipped_keys": still_skipped,
        "skipped_owners": {key: skipped.get(key) for key in RL4_KEYS},
    }
    check("D16 every OR/LI/EN record reaches the packet by id", not absent,
          "absent from the packet: %s" % absent)
    check("D16 the component-only keys left assembly.skipped_keys",
          not still_skipped,
          "still skipped: %s" % {key: skipped.get(key) for key in still_skipped})
    check("D16 the orthography component declares packet_keys",
          bool(receipt["rl4"]["component_keys"][ORTH_COMPONENT]),
          "03-orthography.yml declares no packet_keys")
    check("D16 the costumes component declares the enforcement key",
          "enforcement" in (receipt["rl4"]["component_keys"][COSTUME_COMPONENT] or []),
          "09-costumes.yml packet_keys=%s"
          % receipt["rl4"]["component_keys"][COSTUME_COMPONENT])

    # ---- RL-4 control: the presence check can say no ---------------------
    # A presence check that cannot fail is not a check. The control strips the
    # orthography component's `packet_keys` declaration in a clone, rebuilds
    # through the lane's own assembler, and requires the OR/LI records to leave
    # the packet. Measured in a clone, never the lane worktree.
    control = _rl4_control(receipt)
    check("D16 the RL-4 control lands (the declaration is strippable)",
          control.get("landed") is True, "%s" % control.get("detail"))
    check("D16 the RL-4 control reproduces the round-27 defect",
          control.get("reproduced") is True,
          "after stripping, absent ids=%s (want the OR/LI set)"
          % control.get("absent_after"))

    # ---- the standing argot regression detector -------------------------
    # The design's own eleven worked rows, re-derived through the delivered
    # gate. A regression that breaks any row is a regression against the
    # design, not against this battery's taste.
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

    # The filed reading pair (`reports/round-27/gate-tests/fixtures/`), run
    # read-only from the round-27 directory so this battery adds no fixture of
    # its own: exactly one reading of head2(tumkalker) may derive, so the leg
    # discriminates whichever side the fix lands on.
    pair = []
    for name in ("s1-head2-unconstrained.yml", "s2-head2-constrained.yml"):
        path = R27_FIXTURES / name
        exit_code, out, command = run([sys.executable, ARGOT_GATE, path])
        pair.append({"fixture": name, "command": command, "date": now(),
                     "exit": exit_code, "ids": findings_of(out)})
    receipt["syllabify_reading_pair"] = pair
    clean = [row for row in pair if row["exit"] == 0]
    check("D16 exactly one reading of head2(tumkalker) derives", len(clean) == 1,
          "%s" % [(row["fixture"], row["exit"]) for row in pair])
    check("D16 the non-deriving reading names %s" % DERIV_ID,
          all(DERIV_ID in row["ids"] for row in pair if row["exit"] != 0),
          "%s" % [(row["fixture"], row["ids"]) for row in pair if row["exit"] != 0])

    # The delivered gate must still agree with the design's own named row.
    gate_head2_saalumi = op_functions["head2"]("saalumi")
    receipt["syllabify_reading"] = {
        "gate_head2_saalumi": gate_head2_saalumi,
        "design_table_saalumi": "saalu",
        "gate_agrees_with_design_table": gate_head2_saalumi == "saalu",
    }
    check("D16 the gate agrees with the design's own worked row",
          gate_head2_saalumi == "saalu",
          "head2(saalumi)=%r want 'saalu'" % gate_head2_saalumi)

    # ---- the argot selftest, as a regression floor ----------------------
    exit_code, out, command = run([sys.executable, ARGOT_GATE, "--selftest"])
    receipt["runs"].append({"label": "argot-selftest-d16", "command": command,
                            "date": now(), "exit": exit_code,
                            "tail": out.strip().splitlines()[-1] if out.strip() else ""})
    check("D16 the argot selftest still passes", exit_code == 0,
          "exit %d" % exit_code)
    return checks, failures


def _declared_keys(relative):
    """A component's own top-level `packet_keys:` list, or None."""
    path = ROOT / relative
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^packet_keys:\s*\[(.*?)\]", text, re.M)
    if not match:
        return None
    return [item.strip() for item in match.group(1).split(",") if item.strip()]


def _rl4_control(receipt):
    """Strip the orthography `packet_keys` in a clone; the records must leave.

    The round-27 review measured exactly this defect on the delivered tree. The
    control re-measures it as a *control*: the same edit, through the same
    assembler, must still push OR-01..03 and LI-01..03 out of the packet. If it
    does not, the presence check in measure_d16 is not discriminating and its
    green is meaningless.
    """
    clone = SCRATCH / ("rl4-tree-%d" % os.getpid())
    if clone.exists():
        shutil.rmtree(clone)
    clone.mkdir(parents=True)
    for item in ("tools", "examples"):
        source = ROOT / item
        if source.is_dir():
            shutil.copytree(source, clone / item,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    component = clone / ORTH_COMPONENT
    result = {"clone": str(clone.relative_to(ROOT)), "date": now(),
              "component": ORTH_COMPONENT}
    if not component.is_file():
        result.update({"landed": False, "reproduced": False,
                       "detail": "component missing from the copy"})
        return result
    original = component.read_text(encoding="utf-8")
    # Strip the declaration, and any line-comment that documents it, so the
    # assembler falls back to the allowlist exactly as it did in round 27.
    planted = re.sub(r"^packet_keys:\s*\[.*?\]\s*$\n?", "", original, count=1,
                     flags=re.M)
    result["landed"] = planted != original
    if not result["landed"]:
        result["detail"] = "no top-level packet_keys line to strip"
        result["reproduced"] = False
        return result
    component.write_text(planted, encoding="utf-8")
    exit_code, out, command = run([sys.executable, "tools/assemble-culture-d4.py"],
                                  cwd=clone)
    result["command"] = command
    result["exit"] = exit_code
    result["tail"] = (out.strip().splitlines() or [""])[-1]
    packet_path = clone / D4_SOURCE
    result["packet_present"] = packet_path.is_file()
    if not packet_path.is_file():
        result["detail"] = "the assembler wrote no packet"
        result["reproduced"] = False
        return result
    try:
        packet = load_packet(packet_path)
    except Exception as error:  # noqa: BLE001
        result["detail"] = "the rebuilt packet could not be read: %s" % error
        result["reproduced"] = False
        return result
    ids = packet_record_ids(packet)
    absent = [record_id for record_id in RL4_RECORD_IDS if record_id not in ids]
    skipped = (packet.get("assembly") or {}).get("skipped_keys") or {}
    result["absent_after"] = absent
    result["skipped_after"] = sorted(key for key in RL4_KEYS if key in skipped)
    result["reproduced"] = bool(absent) and bool(result["skipped_after"])
    shutil.rmtree(clone, ignore_errors=True)
    return result


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
          coverage_fields("coverage: p records=175 register_scoped=14 violations=0")
          == {"records": 175, "register_scoped": 14, "violations": 0})
    check("coverage parser ignores the path token",
          "p" not in coverage_fields("coverage: p records=1"))
    check("the law class is the claim's spelling", LAW_CLASS == "D4L-LAW")
    check("the design's id is the DERIV spelling", DERIV_ID == "D4L-ARGOT-DERIV")
    check("the design table carries eleven rows", len(DESIGN_TABLE) == 11)
    check("the design table's head2 row is the named trap",
          ("saalumi", "head2", "saalu") in DESIGN_TABLE)
    check("the reading pair fixtures exist in the round-27 directory",
          all((R27_FIXTURES / name).is_file()
              for name in ("s1-head2-unconstrained.yml", "s2-head2-constrained.yml")))
    check("the RL-4 record id set is the eight named records",
          RL4_RECORD_IDS == ("OR-01", "OR-02", "OR-03", "LI-01", "LI-02", "LI-03",
                             "EN-01", "EN-02"))
    check("the RL-4 key set is the three skipped keys",
          RL4_KEYS == ("records", "literacy_institutions", "enforcement"))
    check("every law plant changes a value", all(row[2] != row[3] for row in LAW_PLANTS))
    check("every law plant names its row",
          all("RGL-01" in row[4] for row in LAW_PLANTS))
    check("the law plants are the two named negatives",
          sorted(row[0] for row in LAW_PLANTS) == ["force", "speaker"])
    # The speaker plant must keep an `(ID)` parenthetical: the delivered leg
    # resolves speakers by the id in `Name (ID)`, so a plant that strips the id
    # is invisible for the wrong reason (this seat measured that mistake).
    speaker_plant = [row for row in LAW_PLANTS if row[0] == "speaker"][0]
    check("the speaker plant keeps an (ID) parenthetical",
          bool(re.search(r"\([A-Z]{2,4}-\d{2,3}\)", speaker_plant[3])))
    check("the speaker plant moves the id to an unresolvable one",
          "ZZ-99" in speaker_plant[3])
    check("the speaker plant anchor is a single delivered occurrence",
          (ROOT / LAW_COMPONENT).read_text(encoding="utf-8").count(
              speaker_plant[2]) == 1)
    # The named-token reader: a class token is a name, an anonymous red is not.
    check("the named-token reader finds a class token",
          law_tokens("FINDING D4L-LAW-FORCE: FAIL — x") == ["D4L-LAW-FORCE"])
    check("the named-token reader ignores an anonymous red",
          law_tokens("Traceback (most recent call last):\nError: boom") == [])
    check("the named-token reader ignores a foreign class",
          law_tokens("FINDING D2L-RANK: [hold] x") == [])
    check("the named-token reader de-duplicates",
          law_tokens("FINDING D4L-LAW-A: x\nFINDING D4L-LAW-A: y") == ["D4L-LAW-A"])
    check("the clone read set names the three trees",
          CLONE_TREES == ("tools", "examples", "corpus"))
    # The argument-shape reader: the bug this runner shipped with once. A
    # `--packet`-shaped instrument gets the flag; a positional one gets a bare
    # path; a flagless one gets neither.
    check("the shape reader selects the --packet flag",
          law_instrument_argv("tool.py", "p.yml", "--packet")[-2:] == ["--packet", "p.yml"])
    check("the shape reader selects a positional path",
          law_instrument_argv("tool.py", "p.yml", "positional")[-1] == "p.yml")
    check("the shape reader never hands a flagless tool a --packet flag",
          "--packet" not in law_instrument_argv("tool.py", "p.yml", "positional"))
    check("the shape reader gives a packetless tool no argument",
          law_instrument_argv("tool.py", "p.yml", "none")[-1] == "tool.py")
    check("the shape reader's three shapes differ",
          len({tuple(law_instrument_argv("t.py", "p", shape))
               for shape in ("--packet", "positional", "none")}) == 3)
    # The usage-error reader: a probe that cannot tell an argparse rejection from
    # a verdict is the bug this runner shipped with. Measured against a real
    # flagless instrument on disk.
    probe_shape, probe_rows = law_instrument_shape(
        ROOT / "reports/round-28/audit/x60-sweep-completeness.py", ROOT / D4_SOURCE)
    check("the shape probe reads a flagless instrument as 'none'",
          probe_shape == "none")
    check("the shape probe tried all three shapes before giving up",
          len(probe_rows) == 3)
    check("the shape probe records a usage error as such, not as a verdict",
          any(row["usage_error"] for row in probe_rows))

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%-56s %s" % (name, "ok" if ok else "FAIL"))
    print("selftest: %d/%d checks passed" % (len(checks) - len(failed), len(checks)))
    return 1 if failed else 0


# --------------------------------------------------------------------------


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="measure only, print")
    parser.add_argument("--selftest", action="store_true",
                        help="dependency-free controls")
    args = parser.parse_args(argv[1:])

    if args.selftest:
        return selftest()

    SCRATCH.mkdir(parents=True, exist_ok=True)
    receipt = {"schema": "kotodama-r28-gate-tests-v1", "round": 28,
               "seats": ["R28-D13", "R28-D14", "R28-D15", "R28-D16"],
               "date": now(), "runs": [], "checks": [], "failures": [], "gaps": []}
    for item in (ARGOT_GATE, TYPED_GATE, D4_ASM_GATE, D4_TYPED_GATE, ASM_D4,
                 ASM_D4_TYPED, PROJECTOR, D4_EXPECTED, ROOT / D4_SOURCE,
                 ROOT / D4_TYPED, ROOT / D4_PROJECTION, ROOT / LAW_COMPONENT,
                 ROOT / ORTH_COMPONENT, ROOT / COSTUME_COMPONENT):
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
