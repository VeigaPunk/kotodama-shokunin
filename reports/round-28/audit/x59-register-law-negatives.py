#!/usr/bin/env python3
"""R28-X59 — register-law negative auditor (independent instrument, round 28).

Seat R28-X59 (SCRIBE X59: shard auditor — law negatives) for round 28, claim D
`register-law-replay` (`reports/round-28/claims.json`). NON-CANON audit
evidence, not a lane gate. Deliberately built on different machinery from the
lane's gates, so an agreement between this tool and a lane gate is a
cross-check rather than inheritance:

    dimension            the lane gates                       this instrument
    YAML parsing         a hand-checked subset loader         `ruby -ryaml -rjson`
                         (runpy by path)                      (a full YAML 1.1 loader)
    reverse / lengthen   the gate's OP_FUNCTIONS + the         re-implemented here from
                         packet's pattern/output pair         the design prose
    kernel dependency    loads a peer gate by path            none — no lane code imported

Round 27 left two standing HOLDs against the register law (recorded in
`reports/round-27/audit/x59-register-law-negatives.md`, `X59-F2` and `X59-F3`):

    RL-1  the law has no replay leg — a tampered law row (`force: 'no-such-force'`)
          emitted the same 12 projector findings as a clean one;
    RL-4  the `register_law` block is declared in neither `PACKET_KEYS` nor
          `RECORD_FIELDS`, so the assembler's validator has no field list for it
          and a malformed row assembles exit 0 (measured: `id: None`).

Round 28's claim D asks that BOTH be closed: the law gains a replay/checking
leg (speaker classes resolve against delivered records, forces against a
declared vocabulary, consequences against the roll/rank machinery) so that **a
tampered row is a named finding (D4L-LAW-* class)**; and RL-4 is fixed (the
components declare `packet_keys`, the records reach the packet, the named-holds
set updated honestly).

This instrument therefore re-tests the two HOLDs, each with its own negative
control, against whatever tree is on disk. It reports what the bytes do; it
adjudicates no round.

Laws audited (the register-law surface):

    L1   REGISTER-BLOCK    the packet declares `registers:` with QREG-01..04
    L2   UNMARKED-SET      `plain` is declared unmarked; no plain record scoped
    L3   OPERATION-RULE    every stamp record's op equals its axis's selection
                           and replays under THIS instrument's own operations
    L4   ERA-LAW           every stamp record is staged E1 or later
    L5   ADMISSIBILITY     every stamp record rides a STAMP-* construction
    L6   LAW-ROWS          the speech-act law rows exist on the packet
    L6b  LAW-TEETH (RL-1)  a tampered law value IS a named finding in a
                           delivered gate (round 27 measured: it was not)
    L7   OATH-VOID         no stamp form sits in the religion field
    L8   DOUBLET-RESOLVES  every stamp record's refs resolve on the tree
    L9   LAW-WIRING (RL-4) the assembler declares the block; a malformed row is
                           refused (round 27 measured: it was not)
    L10  LAW-REPLAY (new)  the law's own fields replay: speaker classes resolve
                           against delivered records, `force` values against a
                           declared vocabulary, consequences against the roll
                           /rank machinery

Usage:

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-28/audit/x59-register-law-negatives.py --controls
    python3 -B reports/round-28/audit/x59-register-law-negatives.py --json
    python3 -B reports/round-28/audit/x59-register-law-negatives.py --packet PATH

Exit: 0 clean, 1 findings, 2 could-not-evaluate.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_PACKET = "examples/culture-d4/packet.d4.yml"
UNMARKED = ("plain", "neutral", "standard", "ordinary")
VOWELS = "aeiou"
STAGE_ORDER = {"E0": 0, "E1": 1, "E2": 2, "E3": 3, "E4": 4}
AXIS_OP = {"mark": "reverse", "fire": "lengthen"}

# The D claim names the finding class the replay leg must emit. A tampered row
# that produces a finding NOT carrying this token is not the named finding the
# claim asks for; it is an anonymous complaint.
NAMED_CLASS = "D4L-LAW"

# Where a delivered gate that could own the enforcement leg may live. The audit
# looks for the NAMED finding token in the source, not for a particular file, so
# a new gate location is discovered rather than missed — but only an instrument
# whose own source can EMIT the named class is a candidate for the replay leg.
GATE_GLOBS = ("tools/gates/*.py", "tools/*.py")  # retained for the read-only source scan


# --------------------------------------------------------------------------
# independent load + independent operations
# --------------------------------------------------------------------------


def load_packet(path):
    """Load a YAML packet through ruby's full YAML loader, as JSON."""
    proc = subprocess.run(
        ["ruby", "-ryaml", "-rjson", "-e",
         "puts JSON.generate(YAML.load_file(ARGV[0]))", str(path)],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError("ruby yaml load failed: %s" % proc.stderr.strip()[:300])
    return json.loads(proc.stdout)


def op_reverse(base):
    return base[::-1]


def op_lengthen(base):
    """Double the first nucleus — re-implemented from the design prose, not the
    gate's OP_FUNCTIONS and not the packet's pattern/output pair."""
    for i, ch in enumerate(base):
        if ch in VOWELS:
            return base[: i + 1] + ch + base[i + 1:]
    return base


OPS = {"reverse": op_reverse, "lengthen": op_lengthen}


# --------------------------------------------------------------------------
# the laws
# --------------------------------------------------------------------------


def text_of(value):
    if isinstance(value, str):
        return value
    if value is None:
        return ""
    return str(value)


def lexical_records(packet):
    out = []
    for entry in packet.get("lexicon") or []:
        if isinstance(entry, dict) and text_of(entry.get("id")).strip():
            out.append(entry)
    return out


def stamp_records(packet):
    return [r for r in lexical_records(packet)
            if text_of(r.get("register")).strip().casefold() == "stamp"]


def register_block(packet):
    block = packet.get("registers")
    return block if isinstance(block, list) else []


def law_block(packet):
    block = packet.get("register_law")
    return block if isinstance(block, list) else []


def law_rows(packet):
    """Every law-bearing row, whatever shape the tree used across rounds."""
    rows = []
    for row in list(register_block(packet)) + list(law_block(packet)):
        if isinstance(row, dict) and (
                text_of(row.get("speech_act")).strip()
                or text_of(row.get("force")).strip()
                or text_of(row.get("consequence")).strip()
                or text_of(row.get("act")).strip()
                or text_of(row.get("holder")).strip()):
            rows.append(row)
    return rows


def _run_gate_for_findings(cmd, timeout=120):
    """Run a delivered gate and return (exit, stdout+stderr)."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              cwd=str(ROOT), timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")
    except Exception as exc:  # noqa: BLE001
        return None, "could-not-run: %s" % exc


def _finding_tokens(exit_code, output):
    """Extract candidate finding tokens from a gate's output.

    A NAMED finding is any token matching the D claim's class prefix, or a
    stable `FINDING ...` / `D4L-LAW-...` line. Anonymous failure is not a named
    finding, so this deliberately does not count a bare nonzero exit.
    """
    if exit_code is None:
        return []
    toks = set()
    for line in output.splitlines():
        for m in re.finditer(r"\bD4L-LAW-[A-Z0-9-]+\b", line):
            toks.add(m.group(0))
        for m in re.finditer(r"(?i)\bFINDING[:\s]+([A-Z0-9-]{3,})", line):
            toks.add(m.group(1))
    return sorted(toks)


def _packet_consuming_instruments():
    """Delivered instruments that read a packet path argument, discovered live.

    The two the round's own runner probes are `tools/d2-typed-labels.py` (the
    projector) and `tools/gates/typed-pipeline-gate.py` (the typed gate); both
    take a packet path as their argument. Discovered, not hardcoded, so a new
    delivered instrument is included automatically — but only a file whose
    source mentions the law surface or the packet is a candidate.
    """
    out = []
    candidates = [
        (ROOT / "tools" / "d2-typed-labels.py", ["--packet", "{packet}"]),
        (ROOT / "tools" / "gates" / "typed-pipeline-gate.py", ["{packet}"]),
    ]
    for extra in sorted((ROOT / "tools" / "gates").glob("*.py")):
        if extra.resolve() in {p.resolve() for p, _ in candidates}:
            continue
        try:
            src = extra.read_text(errors="replace")
        except Exception:  # noqa: BLE001
            continue
        if NAMED_CLASS in src and "--packet" in src:
            candidates.append((extra, ["--packet", "{packet}"]))
    for path, argv in candidates:
        if path.is_file():
            out.append((path, argv))
    return out


def _tamper_law_text(text):
    """Rewrite the first law `force`/`speaker`/`consequence` value in place.

    Textual, so the file keeps its shape and only the value changes — a YAML
    round-trip could reorder keys or requote scalars and confound the reading.
    Returns (tampered_text, note) or (None, reason).
    """
    for field in ("force", "speaker", "consequence"):
        pattern = re.compile(r"(?m)^(\s*)%s:\s*(.+)$" % field)
        m = pattern.search(text)
        if m and m.group(2).strip():
            return (text[:m.start(2)] + '"no-such-value-zzz"'
                    + text[m.end(2):], "tampered `%s`" % field)
    return None, "no `force`/`speaker`/`consequence` field found to tamper"


def findings_for(packet):
    """Return (findings, counters). Each finding is (law_id, level, message)."""
    out = []
    counters = {}

    records = lexical_records(packet)
    stamps = stamp_records(packet)
    block = register_block(packet)
    law_raw = law_block(packet)
    ids = {text_of(r.get("id")).strip() for r in records}
    counters["records"] = len(records)
    counters["stamp_records"] = len(stamps)

    # L1 — the register block and its identity rows.
    block_ids = {text_of(e.get("id")).strip() for e in block if isinstance(e, dict)}
    counters["register_rows"] = len(block)
    if not block:
        out.append(("L1", "FAIL", "the packet declares no `registers:` block: the "
                    "register identity has no owning packet surface"))
    for wanted in ("QREG-01", "QREG-02", "QREG-03", "QREG-04"):
        if wanted not in block_ids:
            out.append(("L1", "FAIL", "the register block does not declare %s" % wanted))

    # L2 — the unmarked set.
    plain_rows = [e for e in block if isinstance(e, dict)
                  and text_of(e.get("register")).strip().casefold() == "plain"]
    if not plain_rows:
        out.append(("L2", "FAIL", "no register row declares the unmarked baseline `plain`"))
    for row in plain_rows:
        if text_of(row.get("class")).strip().casefold() != "unmarked":
            out.append(("L2", "FAIL", "register row %s declares `plain` but not class "
                        "`unmarked`" % text_of(row.get("id")).strip()))
    scoped_plain = [r for r in records
                    if text_of(r.get("register")).strip().casefold() in UNMARKED]
    counters["plain_records"] = len(scoped_plain)
    if scoped_plain:
        out.append(("L2", "FAIL", "%d record(s) declare an unmarked register and must not be "
                    "graded as register-scoped: %s"
                    % (len(scoped_plain), ", ".join(text_of(r.get("id")).strip()
                                                     for r in scoped_plain[:6]))))

    # L3 — the operation rule (axis -> op) and the arithmetic.
    bad_rule, bad_math = [], []
    for rec in stamps:
        rid = text_of(rec.get("id")).strip()
        axis = text_of(rec.get("axis")).strip().casefold()
        deriv = rec.get("derivation")
        if not isinstance(deriv, dict):
            bad_rule.append("%s (no derivation pair)" % rid)
            continue
        op = text_of(deriv.get("op")).strip().casefold()
        base = text_of(deriv.get("base")).strip()
        form = text_of(rec.get("term")).strip()
        want = AXIS_OP.get(axis)
        if want is None:
            bad_rule.append("%s (axis %r selects no declared operation)" % (rid, axis))
            continue
        if op != want:
            bad_rule.append("%s (axis %r selects %r, record declares %r)"
                            % (rid, axis, want, op))
            continue
        fn = OPS.get(op)
        if fn is None:
            bad_rule.append("%s (operation %r is not one this instrument implements)" % (rid, op))
            continue
        if fn(base) != form:
            bad_math.append("%s (%s(%r)=%r, delivered %r)"
                            % (rid, op, base, fn(base), form))
    counters["rule_checked"] = len(stamps)
    if bad_rule:
        out.append(("L3", "FAIL", "the axis->operation rule does not hold for: %s"
                    % "; ".join(bad_rule[:6])))
    if bad_math:
        out.append(("L3", "FAIL", "the declared pair does not replay to the delivered form "
                    "under this instrument's own operations: %s" % "; ".join(bad_math[:6])))

    # L4 — the era law.
    early = [text_of(r.get("id")).strip() for r in stamps
             if STAGE_ORDER.get(text_of(r.get("stage")).strip(), 0) < STAGE_ORDER["E1"]]
    counters["era_checked"] = len(stamps)
    if early:
        out.append(("L4", "FAIL", "stamp record(s) staged before E1: %s"
                    % ", ".join(early[:8])))

    # L5 — admissibility (a stamp form rides a STAMP-* construction).
    stray = [text_of(r.get("id")).strip() for r in stamps
             if not text_of(r.get("construction")).strip().startswith("STAMP-")]
    counters["admissibility_checked"] = len(stamps)
    if stray:
        out.append(("L5", "FAIL", "stamp record(s) not carried by a STAMP-* construction: %s"
                    % ", ".join(stray[:8])))

    # L6 — the speech-act law surface. Three landing shapes accepted (rounds
    # 26 and 27 used all three): RGL-0n rows inside `registers:`, QREG-05..
    # speech-act rows inside `registers:`, or a top-level `register_law:` block.
    speech_act_rows = law_rows(packet)
    rgl_rows = sorted(i for i in block_ids if re.fullmatch(r"RGL-0[1-9]", i or ""))
    rgl_rows += sorted(text_of(e.get("id")).strip() for e in law_raw
                       if isinstance(e, dict)
                       and re.fullmatch(r"RGL-0[1-9]", text_of(e.get("id")).strip() or ""))
    qreg_act_rows = sorted(i for i in block_ids if re.fullmatch(r"QREG-0[5-9]", i or ""))
    law_ids = sorted(set(rgl_rows) | set(qreg_act_rows))
    counters["law_rows"] = len(law_ids)
    counters["speech_act_rows"] = len(speech_act_rows)
    counters["register_law_block"] = len(law_raw)
    if not law_ids:
        out.append(("L6", "HOLD", "no speech-act law surface on the packet: the "
                    "`registers:` block carries only the identity rows (QREG-01..04), "
                    "there is no top-level `register_law:` block, and no row carries "
                    "`speech_act`/`speaker`/`force`/`consequence`. What may be said "
                    "in-register, by whom, and with what record consequence is not on "
                    "the delivered packet surface"))
    elif not speech_act_rows:
        out.append(("L6", "FAIL", "law rows %s exist but none carries a speech-act field "
                    "(`speech_act`/`act`/`holder`/`force`/`consequence`): the row is a "
                    "title, not a law" % ", ".join(law_ids[:6])))

    # L6b — RL-1: teeth. A tampered law value must be a NAMED finding in a
    # DELIVERED instrument (the projector or the typed gate — the two the round's
    # own runner probes), not merely in the round's runner. This is the round-28
    # claim's core clause; round 27 measured the opposite (identical finding
    # sets). The probe tampers the packet TEXTUALLY, preserving the file's shape,
    # because a YAML round-trip can change byte shape and confound the reading.
    # An anonymous nonzero exit is NOT teeth: the claim names the class.
    if speech_act_rows:
        tampered_text, tamper_note = _tamper_law_text(
            (ROOT / DEFAULT_PACKET).read_text(errors="replace"))
        if tampered_text is None:
            out.append(("L6b", "HOLD", "no law field to tamper with: the enforcement "
                        "leg cannot be measured (%s)" % tamper_note))
        else:
            cands = _packet_consuming_instruments()
            counters["law_replay_candidates"] = len(cands)
            clean_toks, tamper_toks = set(), set()
            used = []
            scratch = ROOT / ".scratch" / "x59"
            scratch.mkdir(parents=True, exist_ok=True)
            tmp = scratch / "packet.tamper-law.yml"
            tmp.write_text(tampered_text)
            for path, argv in cands:
                rel = path.relative_to(ROOT)
                for label, target in (("clean", DEFAULT_PACKET),
                                      ("tampered", str(tmp.relative_to(ROOT)))):
                    cmd = [sys.executable, str(rel)] + [
                        (target if a == "{packet}" else a) for a in argv]
                    code, outp = _run_gate_for_findings(cmd)
                    toks = set(_finding_tokens(code, outp))
                    if label == "clean":
                        clean_toks |= toks
                    else:
                        tamper_toks |= toks
                    used.append("%s/%s:exit=%s" % (rel.stem, label, code))
            counters["law_replay_runs"] = len(used)
            new_named = sorted(t for t in (tamper_toks - clean_toks)
                               if NAMED_CLASS in t)
            counters["named_law_findings"] = len(new_named)
            counters["law_findings_clean"] = len(clean_toks)
            counters["law_findings_tampered"] = len(tamper_toks)
            if not new_named:
                out.append(("L6b", "HOLD",
                            "RL-1 still open at this tree: tampering a law field "
                            "(`force`/`speaker`/`consequence`) did not produce a NEW "
                            "named `%s-*` finding in any delivered packet-consuming "
                            "instrument (candidates: %s; runs: %d; named findings "
                            "clean=%d tampered=%d). The law is a declaration with no "
                            "teeth in the delivered tools."
                            % (NAMED_CLASS,
                               ", ".join(str(p.relative_to(ROOT)) for p, _ in cands) or "none",
                               len(used), len(clean_toks), len(tamper_toks))))

    # L7 — an oath spoken in stamp is void (RGL-02 / RLAW-03).
    oath = [text_of(r.get("id")).strip() for r in stamps
            if text_of(r.get("field")).strip().casefold() == "religion"]
    counters["oath_checked"] = len(stamps)
    if oath:
        out.append(("L7", "FAIL", "stamp record(s) in the religion field (an oath spoken in "
                    "stamp is void per RGL-02): %s" % ", ".join(oath[:8])))

    # L8 — doublet_of and base resolve.
    dangling = []
    for rec in stamps:
        rid = text_of(rec.get("id")).strip()
        ref = text_of(rec.get("doublet_of")).strip()
        if ref and ref not in ids:
            dangling.append("%s.doublet_of->%s" % (rid, ref))
        deriv = rec.get("derivation")
        if isinstance(deriv, dict):
            base = text_of(deriv.get("base")).strip()
            if base and base not in {text_of(r.get("term")).strip() for r in records}:
                dangling.append("%s.base->%s" % (rid, base))
    counters["refs_checked"] = len(stamps)
    if dangling:
        out.append(("L8", "FAIL", "register reference(s) do not resolve on the delivered "
                    "tree: %s" % "; ".join(dangling[:8])))

    # L9 — RL-4: the law block's own wiring, measured against the ASSEMBLER (the
    # component that would have to refuse a malformed row). Round 27 measured:
    # `register_law` in neither PACKET_KEYS nor RECORD_FIELDS, so stripping an
    # `id` assembled exit 0 and landed `id: None`. Round 28's claim fixes this.
    if law_raw:
        idless = [i for i, row in enumerate(law_raw)
                  if isinstance(row, dict) and not text_of(row.get("id")).strip()]
        counters["law_wiring_checked"] = len(law_raw)
        if idless:
            out.append(("L9", "FAIL", "%d register_law row(s) carry no `id`: %s"
                        % (len(idless), ", ".join(str(i) for i in idless))))
        else:
            assembler = ROOT / "tools" / "assemble-culture-d4.py"
            declared = assembler.read_text(errors="replace") if assembler.is_file() else ""
            if "register_law" not in declared:
                out.append(("L9", "HOLD",
                            "RL-4 still open at this tree: the `register_law` block is "
                            "landed and every row carries an `id`, but the assembler "
                            "(`tools/assemble-culture-d4.py`) declares it in neither "
                            "`PACKET_KEYS` nor `RECORD_FIELDS`, so its record validator "
                            "has no field list for the block. Measured (round 27, scratch "
                            "clone): stripping an `id` from a `register_law` row assembled "
                            "exit 0 and landed `id: None`; the same edit to a `lexicon` "
                            "row refused exit 2."))

    # L10 — the replay leg's own arithmetic (new for round 28). The D claim
    # names three sub-legs: speaker classes resolve against delivered records;
    # forces against a declared vocabulary; consequences against the roll/rank
    # machinery. Each is measured independently of any lane gate.
    if speech_act_rows:
        counters["replay_rows"] = len(speech_act_rows)
        # (a) speaker classes resolve against delivered records: every token in
        # a `speaker`/`holder` field that looks like an id (XX-00) must resolve.
        # Three resolutions are legitimate and are kept apart rather than merged:
        #   * a delivered packet record id;
        #   * a delivered law row id (RGL-0n — a law row may cite another law);
        #   * a token the row itself annotates `component-only`, i.e. a class the
        #     component declares but the packet does not deliver (RGL-01 cites
        #     `OR-02, component-only`). Such a token is *declared* out of packet
        #     scope, so it is recorded as an annotation, not a dangling FAIL.
        delivered_ids = set(ids)
        for extra in ("costumes", "materials", "rank_rules", "names", "symbols"):
            for row in packet.get(extra) or []:
                if isinstance(row, dict):
                    delivered_ids.add(text_of(row.get("id")).strip())
        law_row_ids = {text_of(r.get("id")).strip() for r in speech_act_rows}
        delivered_ids |= law_row_ids
        unresolved, annotated = [], []
        for row in speech_act_rows:
            rid = text_of(row.get("id")).strip() or "?"
            for key in ("speaker", "holder"):
                field = text_of(row.get(key))
                for tok in re.findall(r"\b([A-Z]{2,4}-[0-9]{2,})\b", field):
                    if tok in delivered_ids:
                        continue
                    if re.search(r"\b%s\b[^)]*component-only" % re.escape(tok), field):
                        annotated.append("%s.%s->%s" % (rid, key, tok))
                        continue
                    unresolved.append("%s.%s->%s" % (rid, key, tok))
        counters["speaker_tokens_checked"] = len(speech_act_rows) * 2
        counters["speaker_component_only"] = len(annotated)
        if unresolved:
            out.append(("L10", "FAIL", "law speaker/holder class reference(s) do not resolve "
                        "against delivered records or law rows: %s"
                        % "; ".join(unresolved[:8])))
        # (b) forces against a declared vocabulary: if the packet declares a
        # force vocabulary anywhere, every law `force` must draw on it. If no
        # vocabulary is declared, that is itself the RL-3-ceiling-shaped gap and
        # is reported as a HOLD rather than invented.
        forces = {text_of(row.get("force")).strip() for row in speech_act_rows
                  if text_of(row.get("force")).strip()}
        vocab = _force_vocabulary(packet)
        counters["forces_seen"] = len(forces)
        counters["force_vocabulary"] = len(vocab)
        if not vocab:
            out.append(("L10", "HOLD", "the law states %d distinct `force` value(s) but the "
                        "packet declares no `force` vocabulary for them to draw on, so "
                        "'forces against a declared vocabulary' has no vocabulary to "
                        "check against" % len(forces)))
        else:
            stray_forces = sorted(f for f in forces
                                  if not _force_in_vocab(f, vocab))
            if stray_forces:
                out.append(("L10", "FAIL", "law `force` value(s) outside the declared "
                            "vocabulary: %s" % "; ".join(stray_forces[:8])))
        # (c) consequences against the roll/rank machinery: a consequence that
        # names a roll must name a delivered roll/rank surface.
        roll_terms = ("roll", "rank", "stamp-roll", "furnace roll")
        for row in speech_act_rows:
            cons = text_of(row.get("consequence")).lower()
            if any(t in cons for t in roll_terms):
                if not any(isinstance(packet.get(k), list) and packet.get(k)
                           for k in ("rank_rules", "costumes")):
                    out.append(("L10", "FAIL", "law row %s names a roll/rank consequence "
                                "but the packet delivers no `rank_rules`/`costumes` "
                                "surface for it to bind" % text_of(row.get("id")).strip()))
                    break

    # L11 — RL-4 proper: the two components the round-28 claim names must
    # declare `packet_keys` covering the blocks their records live in, and those
    # record ids must reach the packet. Round 27 measured this as RL-4's core
    # (OR-01..03, LI-01..03, EN-01..02 absent from the packet). Measured here
    # against the components' own declarations and the assembled packet, not
    # against the round's runner.
    rl4 = _rl4_components()
    counters["rl4_components_checked"] = len(rl4)
    rl4_missing_ids, rl4_bad_keys = [], []
    packet_text = (ROOT / DEFAULT_PACKET).read_text(errors="replace")
    for comp, blocks in rl4.items():
        path = ROOT / comp
        if not path.is_file():
            rl4_bad_keys.append("%s (component missing)" % comp)
            continue
        keys = _declared_packet_keys(path.read_text(errors="replace"))
        for block in blocks:
            if block not in keys:
                rl4_bad_keys.append("%s (declares %s, not `%s`)" % (comp, keys or "nothing", block))
        for block in blocks:
            for rid in _record_ids_in_component(path.read_text(errors="replace"), block):
                if rid not in packet_text:
                    rl4_missing_ids.append("%s.%s->%s" % (comp.split("/")[-1], block, rid))
    counters["rl4_keys_ok"] = len(rl4) - len(rl4_bad_keys)
    counters["rl4_ids_missing"] = len(rl4_missing_ids)
    if rl4_bad_keys:
        out.append(("L11", "FAIL", "RL-4 component `packet_keys` gap: %s"
                    % "; ".join(rl4_bad_keys[:6])))
    if rl4_missing_ids:
        out.append(("L11", "FAIL", "RL-4 records do not reach the packet: %s"
                    % "; ".join(rl4_missing_ids[:8])))

    return out, counters


def _rl4_components():
    """The components the RL-4 gap names, and the blocks their records live in.

    Read from the round's own declaration when it is present, so the audit
    tracks the claim's own definition of RL-4 rather than a snapshot of it.
    """
    declared = {}
    runner = ROOT / "reports" / "round-28" / "run-validation.py"
    if runner.is_file():
        text = runner.read_text(errors="replace")
        m = re.search(r"RL4_COMPONENTS\s*=\s*\{(.*?)\}", text, re.S)
        if m:
            for cm in re.finditer(r'f?"([^"]+)"\s*:\s*\(([^)]*)\)', m.group(1)):
                comp = cm.group(1)
                blocks = tuple(b.strip().strip('"').strip("'")
                               for b in cm.group(2).split(",") if b.strip())
                declared[comp] = blocks
    if declared:
        return declared
    # Fallback: the round-27 finding's own two components.
    return {
        "examples/culture-d4/components/03-orthography.yml": ("records", "literacy_institutions"),
        "examples/culture-d4/components/09-costumes.yml": ("enforcement",),
    }


def _declared_packet_keys(text):
    """The component's own top-level `packet_keys:` list, as a tuple."""
    m = re.search(r"(?m)^packet_keys:\s*\[([^\]]*)\]", text)
    if not m:
        return ()
    return tuple(k.strip().strip('"').strip("'") for k in m.group(1).split(",") if k.strip())


def _record_ids_in_component(text, block):
    """The record ids declared under a top-level `block:` mapping in a component.

    A deliberately simple indentation scan (the components are hand-authored and
    flat); it is a coverage probe, not a YAML parser, so it may over-report and
    never under-reports a missing id.
    """
    lines = text.splitlines()
    ids, inside = [], False
    for line in lines:
        if re.match(r"^%s:\s*$" % re.escape(block), line):
            inside = True
            continue
        if inside:
            if line and not line[0].isspace():
                inside = False
                continue
            m = re.search(r"\bid:\s*([A-Z][A-Z0-9]{1,5}-[0-9]{1,3})\b", line)
            if m:
                ids.append(m.group(1))
    return ids


def _force_vocabulary(packet):
    """Discover any declared force vocabulary on the packet (any shape)."""
    vocab = set()
    for key in ("forces", "force_vocabulary", "illocutionary_forces", "register_law_forces"):
        val = packet.get(key)
        if isinstance(val, list):
            for item in val:
                if isinstance(item, str):
                    vocab.add(item.strip())
                elif isinstance(item, dict) and text_of(item.get("id")).strip():
                    vocab.add(text_of(item.get("id")).strip())
                    if text_of(item.get("force")).strip():
                        vocab.add(text_of(item.get("force")).strip())
    # a law row may also declare the vocabulary itself
    for row in list(register_block(packet)) + list(law_block(packet)):
        if isinstance(row, dict):
            for key in ("declared_forces", "force_vocabulary", "forces"):
                val = row.get(key)
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, str):
                            vocab.add(item.strip())
    return vocab


def _force_in_vocab(force, vocab):
    """A force value matches if it is the vocab term, or contains it as a
    hyphen token (the law writes compound values like `directive-binding,
    not-rollable`)."""
    parts = [p.strip() for p in re.split(r"[,\s]+", force) if p.strip()]
    for part in parts:
        if part in vocab:
            return True
        for v in vocab:
            if v and v in part:
                return True
    return False


def _dump_yaml(obj):
    """Write a dict back to YAML via ruby (the same loader, inverse direction),
    so a tampered copy is a real file the delivered gates can read. Kept as the
    round-trip cross-check against the textual tamper, not the primary route."""
    payload = json.dumps(obj)
    proc = subprocess.run(
        ["ruby", "-ryaml", "-rjson", "-e",
         "obj=JSON.parse(STDIN.read); puts YAML.dump(obj)", ],
        input=payload, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError("ruby yaml dump failed: %s" % proc.stderr.strip()[:200])
    return proc.stdout


# --------------------------------------------------------------------------
# controls
# --------------------------------------------------------------------------


def _mutate(packet, rid, **fields):
    out = copy.deepcopy(packet)
    for rec in out.get("lexicon") or []:
        if isinstance(rec, dict) and text_of(rec.get("id")).strip() == rid:
            rec.update(fields)
            return out
    raise RuntimeError("no such record to mutate: %s" % rid)


def run_controls(packet):
    """Every law must be able to say no. Each control plants one violation."""
    results = []
    stamps = stamp_records(packet)
    if not stamps:
        return results
    first = stamps[0]
    rid = text_of(first.get("id")).strip()

    p = _mutate(packet, rid, axis="mark",
                derivation={"op": "lengthen",
                            "base": text_of(first.get("derivation", {}).get("base")).strip()})
    results.append(("control-1-op-contradicts-axis", "L3", findings_for(p)))

    p = _mutate(packet, rid, stage="E0")
    results.append(("control-2-early-era", "L4", findings_for(p)))

    p = _mutate(packet, rid, term="zzz")
    results.append(("control-3-form-mismatch", "L3", findings_for(p)))

    p = _mutate(packet, rid, construction="CX-01")
    results.append(("control-4-stray-construction", "L5", findings_for(p)))

    p = _mutate(packet, rid, field="religion")
    results.append(("control-5-oath-in-register", "L7", findings_for(p)))

    p = _mutate(packet, rid, doublet_of="L-999")
    results.append(("control-6-dangling-doublet", "L8", findings_for(p)))

    # C6b — a law row with its `id` stripped (the RL-4 defect L9 measures).
    p = copy.deepcopy(packet)
    law = p.get("register_law")
    if isinstance(law, list) and law and isinstance(law[0], dict):
        law[0].pop("id", None)
        results.append(("control-6b-law-row-without-id", "L9", findings_for(p)))

    # C8 — RL-4 (L11): a component that declares no `packet_keys` for the block
    # its records live in. Planted on synthetic component text, because L11 reads
    # the components and the packet from disk (planting on a scratch clone would
    # test the clone, not the law). The helpers are pure functions on text, so
    # this control exercises the exact code path L11 uses. The control passes
    # only when the planted gap IS detected — a detector that cannot see a
    # missing `packet_keys` entry is not a detector.
    planted_text = "component: x\ncostumes:\n  - {id: GAR-01}\n"
    planted_keys = _declared_packet_keys(planted_text)
    planted_ids = _record_ids_in_component(planted_text, "costumes")
    gap_seen = "enforcement" not in planted_keys and planted_ids == ["GAR-01"]
    results.append(("control-8-rl4-gap-detected", "L11",
                    ([("L11", "FAIL", "planted RL-4 gap")] if gap_seen else [], {})))

    # C7 — clean stays clean. The delivered packet may be red on L6b/L9/L10
    # (standing HOLDs about unowned legs), so the control asserts **no FAIL**:
    # a control requiring an empty finding list could never pass on a tree that
    # honestly reports a HOLD.
    p = copy.deepcopy(packet)
    block = p.get("registers")
    if isinstance(block, list):
        acts = (("charge", "stamp-holder", "directive-binding"),
                ("oath", "stamp-holder", "commissive-binding"),
                ("name-lot", "stamp-holder, mold-keeper", "declarative-naming"),
                ("guest-charge", "broker, market-goer", "directive-binding"))
        for n, (act, speaker, force) in enumerate(acts, start=5):
            block.append({"id": "QREG-0%d" % n, "title": "the %s" % act,
                          "register": "stamp", "class": "marked",
                          "speech_act": act, "speaker": speaker, "force": force,
                          "consequence": "a row in the furnace roll",
                          "era_rule": "E1", "axis": "mark",
                          "evidence": "design-choice", "follows": ["F-2"],
                          "law": "the %s, spoken only as the law allows" % act})
    results.append(("control-7-clean-stays-clean", "no-FAIL", findings_for(p)))

    return results


# --------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packet", default=DEFAULT_PACKET)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--controls", action="store_true")
    args = ap.parse_args(argv)

    try:
        packet = load_packet(args.packet)
    except Exception as exc:  # noqa: BLE001 — this tool's job is to report, not to crash
        print("could-not-evaluate: %s" % exc)
        return 2

    if args.controls:
        rows = run_controls(packet)
        failures = 0
        for name, law, (found, _counters) in rows:
            if law is None:
                ok = not found
            elif law == "no-FAIL":
                ok = not any(f[1] == "FAIL" for f in found)
            else:
                ok = any(law == f[0] for f in found)
            if not ok:
                failures += 1
            print("%-34s %s  law=%s  findings=%d"
                  % (name, "ok" if ok else "MISS", law or "clean", len(found)))
        print("controls: %d/%d caught" % (len(rows) - failures, len(rows)))
        return 0 if failures == 0 else 1

    found, counters = findings_for(packet)
    if args.json:
        print(json.dumps({"packet": args.packet, "counters": counters,
                          "findings": [{"law": a, "level": b, "message": c}
                                       for a, b, c in found]}, indent=2))
    else:
        for law, level, message in found:
            print("FINDING %s-%s: %s" % (law, level, message))
        print("counters: " + " ".join("%s=%s" % kv for kv in sorted(counters.items())))
        print("failures: %d" % len(found))
    return 0 if not found else 1


if __name__ == "__main__":
    sys.exit(main())
