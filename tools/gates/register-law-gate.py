#!/usr/bin/env python3
r"""register-law-gate.py — the register law's replay leg.

Spec: `reports/round-27/law/design.md` section 3 (the law's three clauses: what
may be said in-register, by whom, with what record consequence),
`reports/round-27/law/rules.md` sections 1-6 (the rule registry RLAW-01..06, the
closed `force` set RU-L2, the declared limits RU-L1..L6), and
`reports/round-28/claims.json` claim D: "speaker classes resolve against
delivered records, forces against a declared vocabulary, consequences against
the roll/rank machinery — a tampered row is a named finding (D4L-LAW-* class)".

Why this gate exists
--------------------
Round 27 landed the register law as component 13 (`register_law`, rows
RGL-01..RGL-05) and its own review named the defect this gate closes as **RL-1**:
a row whose `force` was `no-such-force` emitted *the same 12 findings* as a clean
one, so the law was "a declaration with no teeth"
(`reports/round-27/law/review.md` section 2, measured there with the
`.scratch/r27-law/A/culture-d4/packet.tamper.yml` probe). Nothing in the delivered
tree resolved a law row's own fields against anything.

This gate is that resolution. It reads the law rows off the packet and replays
each clause against the packet's *other* blocks:

    speaker      every speaker/holder clause must name a declared expression
                 and its delivered records; explicit `Name (ID)` tokens
                 must independently resolve to delivered records
    force        every value must name a declared illocutionary class and a
                 declared modifier (or the literal `none`, which the design's
                 sound-channel and dating constraints carry)
    consequence  a *binding* act's consequence must name delivered roll/rank
                 machinery; a row declaring `force: none` is by its own terms not
                 a speech act, so its consequence is a constraint statement
    register     must name a register the `registers` block declares
    axis         must be in the spine's axis vocabulary
    kind         must be in the declared rule-kind set
    design_row   every token must name a delivered record
    rows         every declared law row (RGL-01..RGL-05) must be present

Finding ids
-----------
    D4L-LAW-DATA         input could not be evaluated                    [exit 2]
    D4L-LAW-ROW          a declared law row is absent from the block      [HOLD]
    D4L-LAW-SPEAKER      a clause or its record references do not resolve [FAIL]
    D4L-LAW-FORCE        a force value names no declared class            [FAIL]
    D4L-LAW-CONSEQUENCE  a binding act's consequence names no machinery   [FAIL]
    D4L-LAW-REGISTER     a register names no declared register            [FAIL]
    D4L-LAW-AXIS         an axis is outside the spine's vocabulary        [FAIL]
    D4L-LAW-KIND         a kind is outside the declared rule-kind set     [HOLD]
    D4L-LAW-DANGLING     a design_row token names no delivered record     [HOLD]
    D4L-LAW-COVERAGE     the packet declares no law block to replay       [HOLD]

Output:  one finding per line, `FINDING <id>: <LEVEL> — <message>`, then one
         `coverage:` line and one `dependency:` line. Exit 0 clean / 1 findings
         / 2 could-not-evaluate.

Calibration (craft policy, declaring what this implementation does)
-------------------------------------------------------------------
- **The vocabulary is the gate's own declared closed set**, quoted from the
  design and named as such. The packet declares no `force` vocabulary (round-28
  audit X59-F5 measured `force_vocabulary=0`), so a leg that resolved `force`
  against the packet alone could not fire at all. The set is stated here, cited,
  and is a *closed* list: a fifth class would be a rule change (RU-L2).
- **A clean packet may carry findings.** At round-28 landing, `design_row`
  tokens `QREG-05..08` named proposed records that had not landed, giving four
  `D4L-LAW-DANGLING` HOLDs. Round 30 adds those records rather than rewriting the
  filed law rows. The selftest accepts either evaluated baseline and measures a
  tamper's delta over emitted finding lines. Exit 0 means every resolution this
  gate performs found nothing to report, not that the law is complete
  (`reports/round-27/law/review.md` section 9).
- **This gate is not wired into the typed pipeline**, and that is a declared
  choice: `tools/gates/typed-pipeline-gate.py` is byte-pinned GREEN in the filed
  round-26 manifests, so adding a sibling invocation would drift a replay surface
  the O seat's sweep has already frozen. The leg is discovered by the round
  runner, which walks every `tools/**/*.py` naming the class. Recorded as a limit
  in the round-28 fragments, not left implicit.
- Scope limits, declared rather than silently skipped:
  * speaker resolution uses a declared closed clause vocabulary and record
    existence, not arbitrary prose interpretation or utterance admissibility;
  * `consequence` is free prose (RU-L3) and is resolved by stem, so a consequence
    that names machinery in words this list does not carry reads as a finding —
    the list is the gate's contract, printed in `coverage:`;
  * only the `register_law` speech-act rows carry `force`; the `registers`
    identity rows (QREG-01..04) are read for the declared register set only.
"""
from __future__ import annotations

import hashlib
import re
import runpy
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
NAMING = HERE / "naming-collision-gate.py"

EXIT_CLEAN = 0
EXIT_FINDINGS = 1
EXIT_UNEVALUATED = 2

# The five law rows `reports/round-27/law/impl-1.md` landed as component 13.
# Declared here so a silently dropped row is a finding, not a smaller domain.
LAW_DECLARED_ROWS = ("RGL-01", "RGL-02", "RGL-03", "RGL-04", "RGL-05")

# The illocutionary vocabulary. Classes are Searle's five, which
# `reports/round-27/law/design.md` section 3 fixes; modifiers are the ones the
# landed rows use to qualify a class. `none` is the declared non-force the
# sound-channel (RGL-04) and dating (RGL-05) constraints carry. Closed set:
# `reports/round-27/law/rules.md` RU-L2 — "a fifth force would be a rule change".
DECLARED_FORCE_CLASSES = ("assertive", "directive", "commissive", "expressive",
                          "declarative")
DECLARED_FORCE_MODIFIERS = ("binding", "refused", "not-rollable", "none",
                            "attested", "witnessed", "naming", "constraint")

# The rule kinds the landed block carries (`design.md` section 3, `impl-2.md`
# section 1). A new kind is a design addition, so an unknown one reads HOLD.
DECLARED_KINDS = ("admissibility", "exclusion", "asymmetry", "no-segment", "era",
                  "enforcement", "procedure")

# The spine's axis vocabulary (`01-brief.yml`; the packet's own declared spine is
# FIRE + MARK, with the sibling families' axes carried for cross-family use).
SPINE_AXES = ("mark", "fire", "cloth", "wind", "word", "knot", "water", "both",
              "neutral")

# The delivered roll/rank machinery a binding act's consequence must name. Stems,
# not exact strings, because `consequence` is free prose (RU-L3).
CONSEQUENCE_STEMS = ("roll", "rk-", "rank", "tally", "rite", "rit-", "entry",
                     "written", "record", "void", "binds", "binding", "no entry")

# An agent token in a law row: `Name (ID)` where ID is a delivered record id.
# Closed clauses: components/13-register-law.yml RGL-01..05; record bindings:
# components/09-costumes.yml RK-03/RK-04, components/03-orthography.yml OR-02.
DECLARED_SPEAKER_CLAUSES = {
    "stamp-holder": ("RK-03",),
    "furnace-master": ("RK-03",),
    "mold-keeper": ("OR-02",),
    "broker": ("RK-04",),
    "market-goer": ("RK-04",),
    "stamp-holder, furnace-master, mold-keeper": ("RK-03", "OR-02"),
    "stamp-holder only — no master, no delegate": ("RK-03",),
    "broker, market-goer, at market days": ("RK-04",),
    "any speaker admitted by rgl-01 or rgl-03": ("RGL-01", "RGL-03"),
    "a stamp-holder, or a speaker the stamp-holder is attesting": ("RK-03",),
    "none — the register admits no binding oath": (),
    "a guest broker, speaking under a stamp-name": ("RK-04",),
}
AGENT_ANNOTATION_RE = re.compile(
    r"\s*\(\s*[A-Z]{2,4}-\d{2,3}(?:\s*,\s*component-only)?\s*\)")
AGENT_ID_RE = re.compile(r"\(\s*([A-Z]{2,4}-\d{2,3})\b")
RECORD_ID_RE = re.compile(r"^[A-Z]{2,4}-\d{2,3}$")
# The declared non-force: the literal `none`, optionally followed by a gloss
# separator. The landed rows carry it as their head word followed by an em-dash
# gloss (`none — a sound-channel constraint, not a speech act`). The separator is
# required, so a value that smuggles `none` alongside an unknown token
# (`none but wibble`) is NOT read as the declared non-force — otherwise the
# resolution would have a hole a tamper could walk through.
NON_FORCE_RE = re.compile(r"^\s*none\s*(?:[—–\-:,]|$)")
FINDING_PREFIX = "FINDING "


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_naming():
    """The sibling naming gate's loader, read-only, by path.

    Imported exactly as `tools/gates/argot-derivation-gate.py` loads its peer, so
    this gate parses the packet through the same stdlib YAML subset reader the
    rest of the family uses and prints that reader's live digest on every run.
    """
    return runpy.run_path(str(NAMING))


def finding(fid, level, message):
    return {"id": fid, "level": level, "message": message}


def format_finding(item):
    return "%s%s: %s — %s" % (FINDING_PREFIX, item["id"], item["level"],
                              item["message"])


def text_of(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def has_text(value):
    return isinstance(value, str) and value.strip() != ""


def law_rows(packet):
    """The law rows the packet carries: the `register_law` speech-act rows and the
    `registers` identity rows, in that order of interest."""
    block = packet.get("register_law") if isinstance(packet, dict) else None
    speech = [row for row in (block or []) if isinstance(row, dict)]
    regs = packet.get("registers") if isinstance(packet, dict) else None
    identity = [row for row in (regs or []) if isinstance(row, dict)]
    return identity, speech


def packet_record_ids(packet):
    """Every id a *record* carries: a list block whose rows are mappings with an
    `id`. This is the resolver's ground truth."""
    ids = set()
    if not isinstance(packet, dict):
        return ids
    for value in packet.values():
        if not isinstance(value, list):
            continue
        for row in value:
            if isinstance(row, dict):
                rid = text_of(row.get("id")).strip()
                if rid:
                    ids.add(rid)
    return ids


def declared_registers(packet):
    """The register *names* the packet declares: each `registers` row's id,
    `register` value and title, so either spelling resolves."""
    regs = packet.get("registers") if isinstance(packet, dict) else None
    names = set()
    for row in (regs or []):
        if not isinstance(row, dict):
            continue
        for key in ("id", "register", "title"):
            token = text_of(row.get(key)).strip()
            if token:
                names.add(token)
    return names


def evaluate_packet(packet):
    """Replay every clause of the law against the packet's other blocks."""
    findings = []
    counters = Counter()
    record_ids = packet_record_ids(packet)
    registers = declared_registers(packet)
    identity, speech = law_rows(packet)
    counters["record_ids"] = len(record_ids)
    counters["registers"] = len(registers)
    counters["identity_rows"] = len(identity)
    counters["law_rows"] = len(speech)

    if not speech:
        findings.append(finding(
            "D4L-LAW-COVERAGE", "HOLD",
            "the packet declares no `register_law` speech-act rows: there is no law "
            "for this leg to replay"))
        return findings, counters

    present = [text_of(row.get("id")).strip() for row in speech]
    for want in LAW_DECLARED_ROWS:
        if want not in present:
            findings.append(finding(
                "D4L-LAW-ROW", "HOLD",
                "declared law row %s is absent from the block: a row silently dropped "
                "is a law with a hole in it (reports/round-27/law/impl-1.md)"
                % want))

    for row in speech:
        rid = text_of(row.get("id")).strip() or "?"
        counters["rows_checked"] += 1

        force = text_of(row.get("force")).strip().lower()
        binding_act = True
        if force:
            classes = [name for name in DECLARED_FORCE_CLASSES if name in force]
            modifier_ok = any(m in force for m in DECLARED_FORCE_MODIFIERS)
            none_only = bool(NON_FORCE_RE.match(force)) and not classes
            binding_act = not none_only
            if not ((classes and modifier_ok) or none_only):
                counters["force_failures"] += 1
                findings.append(finding(
                    "D4L-LAW-FORCE", "FAIL",
                    "%s force %r names no declared illocutionary class or modifier; the "
                    "declared set is %s plus %s (reports/round-27/law/design.md section 3; "
                    "rules.md RU-L2)"
                    % (rid, force, "/".join(DECLARED_FORCE_CLASSES),
                       "/".join(DECLARED_FORCE_MODIFIERS))))

        for field in ("speaker", "holder"):
            if field == "holder" and field not in row:
                continue
            value = text_of(row.get(field))
            clause = " ".join(AGENT_ANNOTATION_RE.sub("", value).lower().split())
            required = DECLARED_SPEAKER_CLAUSES.get(clause)
            counters["speaker_clauses"] += 1
            if required is None:
                counters["speaker_failures"] += 1
                findings.append(finding(
                    "D4L-LAW-SPEAKER", "FAIL",
                    "%s %s clause %r is outside the declared speaker/holder vocabulary"
                    % (rid, field, value)))
            else:
                missing = sorted(set(required) - record_ids)
                if missing:
                    counters["speaker_failures"] += 1
                    findings.append(finding(
                        "D4L-LAW-SPEAKER", "FAIL",
                        "%s %s clause %r requires absent delivered records %s"
                        % (rid, field, value, "/".join(missing))))
            for token in AGENT_ID_RE.findall(value):
                counters["speaker_tokens"] += 1
                if token not in record_ids:
                    counters["speaker_failures"] += 1
                    findings.append(finding(
                        "D4L-LAW-SPEAKER", "FAIL",
                        "%s %s names agent id %s, which resolves to no delivered record: "
                        "the office is cited where the packet cannot see it (RL-4 class)"
                        % (rid, field, token)))

        consequence = text_of(row.get("consequence")).lower()
        if consequence and binding_act and not any(
                stem in consequence for stem in CONSEQUENCE_STEMS):
            counters["consequence_failures"] += 1
            findings.append(finding(
                "D4L-LAW-CONSEQUENCE", "FAIL",
                "%s consequence %r names no delivered roll/rank machinery; the resolved "
                "stems are %s (a record culture's act must leave a record — design.md "
                "section 1)" % (rid, consequence[:120],
                                "/".join(CONSEQUENCE_STEMS))))

        register = text_of(row.get("register")).strip()
        if register and registers and register not in registers:
            counters["register_failures"] += 1
            findings.append(finding(
                "D4L-LAW-REGISTER", "FAIL",
                "%s register %r names no register the `registers` block declares"
                % (rid, register)))

        axis = text_of(row.get("axis")).strip().lower()
        if axis and axis not in SPINE_AXES:
            counters["axis_failures"] += 1
            findings.append(finding(
                "D4L-LAW-AXIS", "FAIL",
                "%s axis %r is outside the spine's axis vocabulary %s"
                % (rid, axis, "/".join(SPINE_AXES))))

        kind = text_of(row.get("kind")).strip()
        if kind and kind not in DECLARED_KINDS:
            counters["kind_failures"] += 1
            findings.append(finding(
                "D4L-LAW-KIND", "HOLD",
                "%s kind %r is outside the declared rule-kind set %s: a new kind is a "
                "design addition, not a variant (rules.md RU-L2)"
                % (rid, kind, "/".join(DECLARED_KINDS))))

        for field in ("design_row", "design_rows"):
            value = row.get(field)
            tokens = value if isinstance(value, list) else ([value] if value else [])
            for token in tokens:
                token = text_of(token).strip()
                if token and RECORD_ID_RE.match(token) and token not in record_ids:
                    counters["dangling"] += 1
                    findings.append(finding(
                        "D4L-LAW-DANGLING", "HOLD",
                        "%s %s names %s, which no delivered record carries: the sibling "
                        "design row never landed as a packet record" % (rid, field, token)))

    findings.sort(key=lambda item: (item["id"], item["message"]))
    return findings, counters


def evaluate_text(text, naming):
    try:
        root = naming["load_yaml"](text)
    except naming["YamlError"] as exc:
        return EXIT_UNEVALUATED, [finding(
            "D4L-LAW-DATA", "FAIL", "input could not be evaluated: %s" % exc)], Counter()
    except RecursionError:
        return EXIT_UNEVALUATED, [finding(
            "D4L-LAW-DATA", "FAIL",
            "input could not be evaluated: flow nesting exceeds the supported depth")], Counter()
    if not isinstance(root, dict):
        return EXIT_UNEVALUATED, [finding(
            "D4L-LAW-DATA", "FAIL",
            "input could not be evaluated: root is not a mapping")], Counter()
    findings, counters = evaluate_packet(root)
    return (EXIT_CLEAN if not findings else EXIT_FINDINGS), findings, counters


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

def _packet(force="directive-binding for the charge",
            speaker="stamp-holder (RK-03)", consequence="binds and is entered on the stamp-roll",
            register="stamp", axis="mark", kind="admissibility", design_row="[RK-03]",
            rows=("RGL-01", "RGL-02", "RGL-03", "RGL-04", "RGL-05")):
    """A minimal law packet whose every clause can be moved by keyword."""
    lines = ["registers:", "  - {id: QREG-02, register: stamp}",
             "rank_rules:", "  - {id: RK-03}", "register_law:"]
    for index, rid in enumerate(rows):
        if index == 0:
            lines.append('  - {id: %s, register: %s, axis: %s, kind: %s, force: "%s", '
                         'speaker: "%s", consequence: "%s", design_row: %s}'
                         % (rid, register, axis, kind, force, speaker, consequence,
                            design_row))
        else:
            lines.append('  - {id: %s, register: stamp, axis: mark, kind: era, '
                         'force: "none — a dating constraint", speaker: "any speaker admitted by RGL-01 or RGL-03", '
                         'consequence: "a constraint statement", design_row: []}' % rid)
    return "\n".join(lines) + "\n"


def _classes(findings, name):
    return [item for item in findings if item["id"] == name]


def _tamper_law_field(text, field, value):
    block = re.search(r"(?m)^register_law:\n(?:[ \t]+[^\n]*(?:\n|$)|\n)*", text)
    if block is None:
        return text, 0
    pattern = r"(?m)^([ \t]+)%s:[ \t]*[^\n]*$" % re.escape(field)
    altered, count = re.subn(
        pattern, lambda match: '%s%s: "%s"' % (match.group(1), field, value),
        block.group(), count=1)
    return text[:block.start()] + altered + text[block.end():], count


def selftest():
    checks = []
    naming = load_naming()

    def run(text):
        return evaluate_text(text, naming)

    # ---- the clean synthetic row resolves, clause by clause
    code, findings, _ = run(_packet())
    checks.append(("clean-synthetic-emits-no-force",
                   not _classes(findings, "D4L-LAW-FORCE")))
    checks.append(("clean-synthetic-emits-no-speaker",
                   not _classes(findings, "D4L-LAW-SPEAKER")))
    checks.append(("clean-synthetic-emits-no-consequence",
                   not _classes(findings, "D4L-LAW-CONSEQUENCE")))
    checks.append(("clean-synthetic-emits-no-dangling",
                   not _classes(findings, "D4L-LAW-DANGLING")))

    # ---- each clause fires on its own tamper, and names the row
    _, tampered, _ = run(_packet(force="no-such-force"))
    fired = _classes(tampered, "D4L-LAW-FORCE")
    checks.append(("force-tamper-fires", len(fired) == 1))
    checks.append(("force-tamper-names-the-row", bool(fired) and "RGL-01" in fired[0]["message"]))
    checks.append(("force-tamper-names-the-value", bool(fired) and "no-such-force" in fired[0]["message"]))

    _, tampered, _ = run(_packet(speaker="stamp-holder (ZZ-99)"))
    fired = _classes(tampered, "D4L-LAW-SPEAKER")
    checks.append(("speaker-tamper-fires", len(fired) == 1))
    checks.append(("speaker-tamper-names-the-agent", bool(fired) and "ZZ-99" in fired[0]["message"]))

    clean_lines = {format_finding(item) for item in run(_packet())[1]}
    for name, value in (
        ("tokenless", "no-such-speaker"),
        ("mixed", "stamp-holder, no-such-speaker"),
        ("known-id", "no-such-speaker (RK-03)"),
        ("empty", ""),
    ):
        code, tampered, _ = run(_packet(speaker=value))
        fired = _classes(tampered, "D4L-LAW-SPEAKER")
        added = {format_finding(item) for item in tampered} - clean_lines
        checks.append(("speaker-class-%s-changes-finding-lines" % name,
                       code == EXIT_FINDINGS and len(fired) == 1
                       and "RGL-01 speaker" in fired[0]["message"]
                       and repr(value) in fired[0]["message"]
                       and added == {format_finding(item) for item in fired}))
    code, clean_class, _ = run(_packet(speaker="stamp-holder"))
    checks.append(("declared-tokenless-speaker-resolves",
                   code == EXIT_CLEAN and not clean_class))
    missing = _packet(speaker="stamp-holder").replace(
        "  - {id: RK-03}", "  - {id: RK-99}")
    fired = _classes(run(missing)[1], "D4L-LAW-SPEAKER")
    checks.append(("declared-speaker-requires-delivered-record",
                   len(fired) == 1 and "RK-03" in fired[0]["message"]
                   and "requires absent delivered records" in fired[0]["message"]))

    _, tampered, _ = run(_packet(consequence="the act evaporates silently"))
    fired = _classes(tampered, "D4L-LAW-CONSEQUENCE")
    checks.append(("consequence-tamper-fires", len(fired) == 1))

    # ---- the controls are not always-true: each tamper is silent on the clean row
    checks.append(("force-resolution-is-discriminating",
                   bool(_classes(run(_packet(force="no-such-force"))[1], "D4L-LAW-FORCE"))
                   and not _classes(run(_packet())[1], "D4L-LAW-FORCE")))
    checks.append(("speaker-resolution-is-discriminating",
                   bool(_classes(run(_packet(speaker="x (ZZ-99)"))[1], "D4L-LAW-SPEAKER"))
                   and not _classes(run(_packet())[1], "D4L-LAW-SPEAKER")))
    checks.append(("consequence-resolution-is-discriminating",
                   bool(_classes(run(_packet(consequence="evaporates"))[1], "D4L-LAW-CONSEQUENCE"))
                   and not _classes(run(_packet())[1], "D4L-LAW-CONSEQUENCE")))

    # ---- `none` is a declared non-force, and its consequence is not resolved
    _, nonact, _ = run(_packet(force="none — a sound-channel constraint",
                               consequence="no machinery is named here at all"))
    checks.append(("none-force-is-declared", not _classes(nonact, "D4L-LAW-FORCE")))
    checks.append(("non-act-consequence-not-resolved",
                   not _classes(nonact, "D4L-LAW-CONSEQUENCE")))
    checks.append(("none-force-with-a-class-still-checks",
                   bool(_classes(run(_packet(force="none but wibble"))[1], "D4L-LAW-FORCE"))))

    # ---- a declared row absent is a finding; a full set is not
    _, dropped, _ = run(_packet(rows=("RGL-01", "RGL-02", "RGL-03", "RGL-04")))
    checks.append(("absent-declared-row-fires",
                   bool(_classes(dropped, "D4L-LAW-ROW"))
                   and not _classes(run(_packet())[1], "D4L-LAW-ROW")))

    # ---- design_row resolution, both directions
    _, dangling, _ = run(_packet(design_row="[QREG-05]"))
    checks.append(("dangling-design-row-fires", bool(_classes(dangling, "D4L-LAW-DANGLING"))))
    checks.append(("resolved-design-row-is-silent",
                   not _classes(run(_packet(design_row="[RK-03]"))[1], "D4L-LAW-DANGLING")))
    checks.append(("empty-design-row-is-silent",
                   not _classes(run(_packet(design_row="[]"))[1], "D4L-LAW-DANGLING")))

    # ---- register, axis and kind resolutions
    checks.append(("undeclared-register-fires",
                   bool(_classes(run(_packet(register="no-such-register"))[1],
                                 "D4L-LAW-REGISTER"))))
    checks.append(("declared-register-name-is-silent",
                   not _classes(run(_packet(register="stamp"))[1], "D4L-LAW-REGISTER")))
    checks.append(("axis-outside-vocabulary-fires",
                   bool(_classes(run(_packet(axis="wibble"))[1], "D4L-LAW-AXIS"))))
    checks.append(("kind-outside-set-fires",
                   bool(_classes(run(_packet(kind="wibble"))[1], "D4L-LAW-KIND"))))

    # ---- a packet with no law block is a coverage finding, not a silent pass
    _, empty, _ = run("registers:\n  - {id: QREG-02, register: stamp}\n")
    checks.append(("no-law-block-fires-coverage",
                   bool(_classes(empty, "D4L-LAW-COVERAGE"))))

    # ---- exit codes
    checks.append(("exit-clean-on-a-clean-packet", run(_packet(design_row="[]"))[0] == EXIT_CLEAN))
    checks.append(("exit-findings-on-a-tampered-packet", run(_packet(force="wibble"))[0] == EXIT_FINDINGS))
    checks.append(("exit-unevaluated-on-garbage", run("\t- [unbalanced\n")[0] == EXIT_UNEVALUATED))
    checks.append(("unevaluated-names-the-data-class",
                   bool(_classes(run("\t- [unbalanced\n")[1], "D4L-LAW-DATA"))))

    # ---- the teeth control: the DELIVERED packet, tampered the way round 27 did
    live = ROOT / "examples/culture-d4/packet.d4.yml"
    if live.is_file():
        text = live.read_text(encoding="utf-8")
        base_code, base_findings, base_counters = run(text)
        base = {format_finding(item) for item in base_findings}
        original = naming["load_yaml"](text)
        checks.append(("delivered-packet-replays",
                       base_code in (EXIT_CLEAN, EXIT_FINDINGS)
                       and base_counters["law_rows"] == len(LAW_DECLARED_ROWS)))
        for name, field, value, fid in (
            ("force", "force", "no-such-force", "D4L-LAW-FORCE"),
            ("speaker", "speaker", "no-such-speaker", "D4L-LAW-SPEAKER"),
            ("speaker-id", "speaker", "stamp-holder (ZZ-99)", "D4L-LAW-SPEAKER"),
            ("consequence", "consequence", "the act evaporates silently",
             "D4L-LAW-CONSEQUENCE"),
        ):
            tampered_text, count = _tamper_law_field(text, field, value)
            actual = naming["load_yaml"](tampered_text)
            first = original["register_law"][0]
            expected = {**original, "register_law": [
                {**first, field: value}, *original["register_law"][1:]]}
            checks.append(("delivered-%s-changes-only-law-field" % name,
                           count == 1 and first.get("id") == "RGL-01"
                           and actual == expected))
            code, changed, _ = run(tampered_text)
            added = {format_finding(item) for item in changed} - base
            checks.append(("delivered-%s-tamper-adds-a-line" % name,
                           code == EXIT_FINDINGS and len(added) == 1
                           and all(line.startswith("FINDING %s:" % fid)
                                   and "RGL-01" in line for line in added)))
        checks.append(("delivered-unchanged-control-identical-lines",
                       {format_finding(item) for item in run(text)[1]} == base))
    else:
        checks.append(("delivered-packet-present", False))

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%-44s %s" % (name, "ok" if ok else "FAIL"))
    print("selftest: %d/%d checks passed" % (len(checks) - len(failed), len(checks)))
    return EXIT_FINDINGS if failed else EXIT_CLEAN


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv):
    args = list(argv[1:])
    if args and args[0] in ("--selftest", "--self-test"):
        return selftest()
    if len(args) == 2 and args[0] == "--packet":
        target = args[1]
    elif len(args) == 1 and not args[0].startswith("-"):
        target = args[0]
    else:
        sys.stderr.write(
            "usage: register-law-gate.py <culture-packet.yml> | --packet <path> | --selftest\n")
        return EXIT_UNEVALUATED
    if not NAMING.is_file():
        print(format_finding(finding(
            "D4L-LAW-DATA", "FAIL", "dependency missing: %s" % NAMING)))
        return EXIT_UNEVALUATED
    path = Path(target)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(format_finding(finding(
            "D4L-LAW-DATA", "FAIL", "input could not be evaluated: %s" % exc)))
        return EXIT_UNEVALUATED
    except UnicodeDecodeError as exc:
        print(format_finding(finding(
            "D4L-LAW-DATA", "FAIL",
            "input could not be evaluated: not UTF-8 text: %s" % exc)))
        return EXIT_UNEVALUATED

    naming = load_naming()
    code, findings, counters = evaluate_text(text, naming)
    for item in findings:
        print(format_finding(item))
    try:
        shown = str(path.resolve().relative_to(ROOT))
    except ValueError:
        shown = str(path)
    print("coverage: %s law_rows=%d identity_rows=%d record_ids=%d registers=%d "
          "speaker_tokens=%d force_failures=%d consequence_failures=%d dangling=%d "
          "findings=%d"
          % (shown, counters["law_rows"], counters["identity_rows"],
             counters["record_ids"], counters["registers"],
             counters["speaker_tokens"], counters["force_failures"],
             counters["consequence_failures"], counters["dangling"], len(findings)))
    print("dependency: %s sha256 %s" % (NAMING.relative_to(ROOT), sha256_file(NAMING)))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
