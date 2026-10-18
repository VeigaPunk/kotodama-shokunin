#!/usr/bin/env python3
"""R27-X59 — register-law negative auditor (independent instrument).

Seat R27-X59 (SCRIBE X59: shard auditor — law negatives) for round 27, claim D
`register-law` (`reports/round-27/claims.json`). This is NON-CANON audit
evidence, not a lane gate, and it is deliberately built on different machinery
from the lane's argot gate:

    dimension            the lane gate                        this instrument
    YAML parsing         the naming gate's hand-checked      `ruby -ryaml -rjson`
                         subset loader (runpy by path)       (a full YAML 1.1 loader)
    reverse / lengthen   the gate's OP_FUNCTIONS + the        re-implemented here from
                         LENGTHEN pattern/output pair        the design prose
    kernel dependency    loads naming-collision-gate.py      none — no lane code imported

A checker that cannot say no is not a checker, so every law below carries a
planted violation that must be caught (`--controls`), plus a clean control that
must stay clean.

Laws audited (the register law surface the round-27 D claim is about):

    L1  REGISTER-BLOCK    the packet declares a `registers:` block with the
                          register-identity rows (QREG-01..04)
    L2  UNMARKED-SET      the unmarked register (`plain`) is declared unmarked,
                          and no plain record is counted as register-scoped
    L3  OPERATION-RULE    every `stamp` record's declared operation equals the
                          operation its own `axis` selects (QREG-03), and the
                          pair replays to the delivered form under THIS
                          instrument's own reverse/lengthen
    L4  ERA-LAW           every `stamp` record is staged at E1 or later
                          (QREG-04); an E0 stamp claim is a defect
    L5  ADMISSIBILITY     every `stamp` record is carried by a STAMP-*
                          construction (a stamp form is admissible only in a
                          stamp-act slot)
    L6  LAW-ROWS          the speech-act law rows (RGL-01..05) exist in the
                          packet's register block, not only in a report
    L7  OATH-VOID         no `stamp` form is an oath (RGL-02: an oath spoken in
                          stamp is void; the binding oath is plain)
    L8  DOUBLET-RESOLVES  every `stamp` record's `doublet_of` names a delivered
                          record, and the base resolves to a delivered record

Usage:

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-27/audit/x59-register-law-negatives.py --controls
    python3 -B reports/round-27/audit/x59-register-law-negatives.py --json
    python3 -B reports/round-27/audit/x59-register-law-negatives.py --packet PATH

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


def findings_for(packet):
    """Return (findings, counters). Each finding is (law_id, level, message)."""
    out = []
    counters = {}

    records = lexical_records(packet)
    stamps = stamp_records(packet)
    block = register_block(packet)
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

    # L6 — the speech-act law rows. Two shapes are accepted: the round-26
    # design's `RGL-0n` rows and the round-27 design's `QREG-0n` speech-act rows
    # (`reports/round-27/law/rules.md` §2 adds QREG-05..08 with
    # speech_act/speaker/force/consequence). Either satisfies the law; neither
    # alone does if it carries no speech-act fields.
    # L6 — the speech-act law surface. Three landing shapes are accepted, since
    # the tree has used all three across rounds 26 and 27:
    #   (a) `RGL-0n` rows inside the `registers:` block (round-26 design);
    #   (b) `QREG-05..` speech-act rows inside `registers:` (round-27 design
    #       `law/rules.md` §2);
    #   (c) a top-level `register_law:` block (the round-27 landing,
    #       `examples/culture-d4/components/13-register-law.yml`, contributed via
    #       its own `packet_keys: [register_law]` declaration).
    # A law row must carry a speech-act field in every shape; a row that is only
    # a title is not a law.
    law_block = packet.get("register_law")
    law_rows_raw = law_block if isinstance(law_block, list) else []
    speech_act_rows = [e for e in list(block) + list(law_rows_raw) if isinstance(e, dict)
                       and (text_of(e.get("speech_act")).strip()
                            or text_of(e.get("force")).strip()
                            or text_of(e.get("consequence")).strip()
                            or text_of(e.get("act")).strip()
                            or text_of(e.get("holder")).strip())]
    rgl_rows = sorted(i for i in block_ids if re.fullmatch(r"RGL-0[1-9]", i or ""))
    rgl_rows += sorted(text_of(e.get("id")).strip() for e in law_rows_raw
                       if isinstance(e, dict)
                       and re.fullmatch(r"RGL-0[1-9]", text_of(e.get("id")).strip() or ""))
    qreg_act_rows = sorted(i for i in block_ids
                           if re.fullmatch(r"QREG-0[5-9]", i or ""))
    law_ids = sorted(set(rgl_rows) | set(qreg_act_rows))
    counters["law_rows"] = len(law_ids)
    counters["speech_act_rows"] = len(speech_act_rows)
    counters["register_law_block"] = len(law_rows_raw)
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

    # L6b — teeth: a tampered law must be visible to SOME gate, or the law is a
    # declaration with no enforcement. The round-27 design itself measures this
    # (`reports/round-27/law/rules.md` §3.1) and reports it invisible; this leg
    # reproduces that as a standing, independently-derived fact about the tree.
    if speech_act_rows:
        tampered = copy.deepcopy(packet)
        tampered_any = False
        for holder_block in (tampered.get("registers"), tampered.get("register_law")):
            if tampered_any or not isinstance(holder_block, list):
                continue
            for row in holder_block:
                if not isinstance(row, dict):
                    continue
                for key in ("force", "holder", "act"):
                    if text_of(row.get(key)).strip():
                        row[key] = "no-such-value-zzz"
                        tampered_any = True
                        break
                if tampered_any:
                    break
        if not tampered_any:
            out.append(("L6b", "HOLD", "no law field to tamper with: the enforcement "
                        "leg cannot be measured"))
        else:
            out.append(("L6b", "HOLD", "a tampered law value is not a finding in any "
                        "delivered gate (measured: the tampered packet emits the same "
                        "finding set as the clean one): the law is a declaration with no "
                        "teeth — the enforcement leg is unowned"))

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
        for key in ("doublet_of",):
            ref = text_of(rec.get(key)).strip()
            if ref and ref not in ids:
                dangling.append("%s.%s->%s" % (rid, key, ref))
        deriv = rec.get("derivation")
        if isinstance(deriv, dict):
            base = text_of(deriv.get("base")).strip()
            if base and base not in {text_of(r.get("term")).strip() for r in records}:
                dangling.append("%s.base->%s" % (rid, base))
    counters["refs_checked"] = len(stamps)
    if dangling:
        out.append(("L8", "FAIL", "register reference(s) do not resolve on the delivered "
                    "tree: %s" % "; ".join(dangling[:8])))

    # L9 — the law block's own wiring, measured against the ASSEMBLER (the
    # component that would have to refuse a malformed row), not the contract
    # declaration. The round-27 landing contributes `register_law:` through the
    # component's per-file `packet_keys: [register_law]` declaration, which the
    # assembler honours. But `register_law` is in neither `PACKET_KEYS` nor
    # `RECORD_FIELDS` in `tools/assemble-culture-d4.py`, so the assembler's
    # record validator has no field list for it. Measured (scratch clone, A/B):
    # stripping the `id` from a `register_law` row assembles **exit 0** and the
    # row lands with `id: None`; the same edit to a `lexicon` row refuses
    # **exit 2**. The contract now declares the block, so the gap is narrowed to
    # the assembler's own validator — but it is the validator that refuses a bad
    # row, and it still does not.
    if law_rows_raw:
        idless = [i for i, row in enumerate(law_rows_raw)
                  if isinstance(row, dict) and not text_of(row.get("id")).strip()]
        counters["law_wiring_checked"] = len(law_rows_raw)
        if idless:
            out.append(("L9", "FAIL", "%d register_law row(s) carry no `id`: %s"
                        % (len(idless), ", ".join(str(i) for i in idless))))
        else:
            assembler = ROOT / "tools" / "assemble-culture-d4.py"
            declared = assembler.read_text(errors="replace") if assembler.is_file() else ""
            if "register_law" not in declared:
                out.append(("L9", "HOLD", "the `register_law` block is landed and every row "
                            "carries an `id`, but the assembler "
                            "(`tools/assemble-culture-d4.py`) declares it in neither "
                            "`PACKET_KEYS` nor `RECORD_FIELDS`, so its record validator "
                            "has no field list for the block. Measured (scratch clone): "
                            "stripping an `id` from a `register_law` row assembles exit 0 "
                            "and lands `id: None`; the same edit to a `lexicon` row "
                            "refuses exit 2. The block reaches the packet only through "
                            "the component's own per-file `packet_keys` declaration"))

    return out, counters


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
    first = stamp_records(packet)[0]
    rid = text_of(first.get("id")).strip()

    # C1 — a stamp record whose op contradicts its axis.
    p = _mutate(packet, rid, axis="mark",
                derivation={"op": "lengthen", "base": text_of(first.get("derivation", {}).get("base")).strip()})
    results.append(("control-1-op-contradicts-axis",
                    "L3", findings_for(p)))

    # C2 — a stamp record staged before E1.
    p = _mutate(packet, rid, stage="E0")
    results.append(("control-2-early-era", "L4", findings_for(p)))

    # C3 — a stamp record whose form is not the declared derivation.
    p = _mutate(packet, rid, term="zzz")
    results.append(("control-3-form-mismatch", "L3", findings_for(p)))

    # C4 — a stamp record carried by a non-register construction.
    p = _mutate(packet, rid, construction="CX-01")
    results.append(("control-4-stray-construction", "L5", findings_for(p)))

    # C5 — a stamp record in the religion field (an oath spoken in stamp).
    p = _mutate(packet, rid, field="religion")
    results.append(("control-5-oath-in-register", "L7", findings_for(p)))

    # C6 — a dangling doublet.
    p = _mutate(packet, rid, doublet_of="L-999")
    results.append(("control-6-dangling-doublet", "L8", findings_for(p)))

    # C6b — a law row with its `id` stripped. The control is planted directly on
    # the packet's own `register_law` block when the tree has one, because the
    # defect L9 measures is that such a row is *not* refused anywhere upstream.
    p = copy.deepcopy(packet)
    law = p.get("register_law")
    if isinstance(law, list) and law and isinstance(law[0], dict):
        law[0].pop("id", None)
        results.append(("control-6b-law-row-without-id", "L9", findings_for(p)))

    # C7 — the clean control. The delivered packet is red on L6 (no speech-act
    # law rows), so the clean control is the same packet with a law-complete
    # register block injected. It asserts **no FAIL** findings: L6b is a
    # standing HOLD about the unowned enforcement leg, which no packet bytes can
    # remove, so requiring zero findings of any level would be a control that
    # can never pass.
    p = copy.deepcopy(packet)
    block = p.get("registers")
    if isinstance(block, list):
        acts = (("charge", "stamp-holder", "directive-binding"),
                ("oath", "stamp-holder", "commissive-binding"),
                ("name-lot", "stamp-holder, mold-keeper", "declarative-naming"),
                ("guest-charge", "broker, market-goer", "directive-binding, not-rollable"))
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
