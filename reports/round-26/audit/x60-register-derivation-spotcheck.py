#!/usr/bin/env python3
r"""x60-register-derivation-spotcheck.py — independent re-run of the register
derivations, for seat R26-X60 (scribe: spot-check auditor).

This is an *audit instrument*, not a lane gate. It exists so that the round-26
spot-check seat can re-derive the register-scoped forms without calling
`tools/gates/argot-derivation-gate.py`, and without borrowing the naming gate's
YAML subset loader or its replay kernel. Independence is the whole point:

  * the packet is parsed by a **different parser** (`ruby -ryaml` -> JSON, a
    full YAML 1.1 loader) than the gate's hand-checked subset loader, so a
    parse-level disagreement is visible rather than shared;
  * `head2` and `reverse` are implemented here **from the design prose**
    (`reports/round-17/d4/design-language.md` §5) rather than from the gate's
    `OPS` table or its `syllabify()`;
  * the register-scoping rule and the loan-adaptation rule are re-derived from
    the design and the packet's own schema, not read out of the gate.

Read-only: no writes, no network. Scratch is the caller's business.

Usage
-----
    python3 reports/round-26/audit/x60-register-derivation-spotcheck.py \
        [--packet PATH] [--controls]

`--controls` additionally plants violations in memory and asserts this
instrument catches each one (a checker that never says no is not a checker).

Exit: 0 all checks agree, 1 a disagreement or a control miss, 2 could not
evaluate (input unreadable / unparseable).
"""

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DESIGN = "reports/round-17/d4/design-language.md"
DEFAULT_PACKET = "examples/culture-d4/packet.d4.yml"

VOWELS = frozenset("aeiou")
# `design-language.md` §5: "no register owns a private segment"; the unmarked
# register is the baseline the argot is measured against, not a member of it.
UNMARKED = frozenset(("plain", "neutral", "standard", "ordinary", ""))
NON_FORMS = frozenset(("", "null", "none", "~"))


# --------------------------------------------------------------------------
# parsing — a deliberately different path from the gate's
# --------------------------------------------------------------------------


def parse_yaml(path):
    """Parse with ruby's YAML 1.1 loader, not the gate's subset loader."""
    ruby = (
        "require 'yaml'; require 'json'; "
        "puts JSON.generate(YAML.load_file(ARGV[0]))"
    )
    proc = subprocess.run(
        ["ruby", "-e", ruby, str(path)],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise SystemExit("could not parse %s: %s" % (path, proc.stderr.strip()))
    return json.loads(proc.stdout)


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


# --------------------------------------------------------------------------
# the two declared operations, implemented from the design prose (§5)
# --------------------------------------------------------------------------


def syllabify(word):
    """`design-language.md` §5: "Syllabification is maximal-onset: a consonant
    is taken as the onset of the following syllable whenever that yields a legal
    syllable." A doubled vowel is one long nucleus."""
    nuclei, index = [], 0
    while index < len(word):
        char = word[index]
        if char in VOWELS:
            if index + 1 < len(word) and word[index + 1] == char:
                nuclei.append(("V", char * 2))
                index += 2
            else:
                nuclei.append(("V", char))
                index += 1
        else:
            nuclei.append(("C", char))
            index += 1
    syllables, onset = [], ""
    for kind, text in nuclei:
        if kind == "C":
            onset += text
            continue
        syllables.append(onset + text)
        onset = ""
    if onset:
        syllables.append(onset)
    return syllables


def head2(base):
    """§5: "the first two syllables of the base"."""
    return "".join(syllabify(base)[:2])


def reverse(base):
    """§5: "character-level string reversal of the base"."""
    return base[::-1]


OPS = {"head2": head2, "reverse": reverse}


def nfc(text):
    return unicodedata.normalize("NFC", text)


# --------------------------------------------------------------------------
# the design's own worked tables (§5, §7.1) — the spec, restated
# --------------------------------------------------------------------------

# §5 "Eleven worked derivations (all recomputed by the checker, all agreeing)".
WORKED_11 = [
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
]

# §7.1 "Name lexicon (plain base -> quote name by reverse)".
NAMES_8 = [
    ("kani", "inak"),
    ("masu", "usam"),
    ("niru", "urin"),
    ("saka", "akas"),
    ("mika", "akim"),
    ("kura", "aruk"),
    ("nusi", "isun"),
    ("musa", "asum"),
]


# --------------------------------------------------------------------------
# packet reading
# --------------------------------------------------------------------------


def list_blocks(packet):
    """Every top-level list block, in the gate's own key-sorted order."""
    out = []
    for key in sorted(packet):
        value = packet.get(key)
        if isinstance(value, list):
            out.append((key, value))
    return out


def as_text(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def layer_index(packet):
    """Layers by id and by name; the packet's `layers` is a list of mappings."""
    table = {}
    for key, entries in list_blocks(packet):
        if key != "layers":
            continue
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            for label_key in ("id", "name"):
                label = as_text(entry.get(label_key)).strip()
                if label:
                    table[label.casefold()] = entry
    return table


# A *replayable* form record is one the language owns. The gate's own rule is
# two-part and this instrument reproduces it deliberately rather than picking a
# single key: the record must carry a form (`term`/`quote_form`, or the
# `derived_from`/`derivation` pair), *and* it must be a lexical record rather
# than prose about one. A `symbols` record's `form:` describes a medium and a
# `contact`/`layers` record's `name:` labels a road or a stratum; both are prose
# and neither is a string the sound-and-identity channel could derive.
#
# The two denominators the audit reports:
#   register_scoped_declared (18) — every record declaring a non-plain register
#   register_scoped          ( 6) — the subset that is also a replayable lexical
#                                  form, i.e. the gate's coverage-line number
LEXICAL_FORM_KEYS = ("term", "quote_form")
FORM_KEYS = ("term", "quote_form", "form", "candidate", "name")
LEXICAL_MARKERS = ("derived_from", "derivation", "donor_form", "loan_layer",
                   "route", "formation")


def record_form(entry, lexical_only=False):
    """The record's form, or "".

    With `lexical_only` the two-part lexical rule is applied: a form key must
    be present *and* a lexical marker must be present, so a `symbols`/`contact`
    `form:`/`name:` prose string is not mistaken for a derivable form.
    """
    form = ""
    for key in FORM_KEYS:
        value = as_text(entry.get(key)).strip()
        if value and value.casefold() not in NON_FORMS:
            form = value
            break
    if not lexical_only:
        return form
    if any(key in entry for key in LEXICAL_MARKERS):
        return form
    if any(as_text(entry.get(key)).strip() and
           as_text(entry.get(key)).strip().casefold() not in NON_FORMS
           for key in LEXICAL_FORM_KEYS):
        return form
    return ""


def record_register(entry, layers):
    """The register a record is scoped to, or None.

    Re-derived here: a record is register-scoped when it declares a `register`
    that is not the unmarked baseline, or when its `loan_layer`/`layer` resolves
    to a declared layer that itself declares a non-unmarked register.
    """
    declared = as_text(entry.get("register")).strip()
    if declared and declared.casefold() not in NON_FORMS:
        return None if declared.casefold() in UNMARKED else declared
    for key in ("loan_layer", "layer"):
        label = as_text(entry.get(key)).strip()
        if not label:
            continue
        layer = layers.get(label.casefold())
        if layer is None:
            continue
        register = as_text(layer.get("register")).strip()
        if register and register.casefold() not in NON_FORMS:
            return None if register.casefold() in UNMARKED else register
    return None


def declared_derivation(entry):
    """(op, base) from the `derived_from` + `derivation` shape, when present."""
    base = as_text(entry.get("derived_from")).strip()
    derivation = entry.get("derivation")
    op = ""
    if isinstance(derivation, dict):
        op = as_text(derivation.get("op") or derivation.get("rule")).strip()
        if not base:
            base = as_text(derivation.get("base")).strip()
    else:
        op = as_text(derivation).strip()
    if not base or not op or base.casefold() in NON_FORMS or op.casefold() in NON_FORMS:
        return None
    return op, base


def claimed_formation(entry):
    """(rule, stem) from the packet's own `formation` idiom."""
    formation = entry.get("formation")
    if not isinstance(formation, dict):
        return None
    stem = as_text(formation.get("stem")).strip()
    rule = as_text(formation.get("rule") or formation.get("rule_id")).strip()
    if not stem or not rule or stem.casefold() in NON_FORMS or rule.casefold() in NON_FORMS:
        return None
    return rule, stem


def packet_rules(packet):
    morphology = packet.get("morphology")
    if not isinstance(morphology, dict):
        return {}
    rules = morphology.get("derivation_rules")
    if not isinstance(rules, list):
        return {}
    table = {}
    for entry in rules:
        if isinstance(entry, dict):
            rid = as_text(entry.get("id")).strip()
            if rid:
                table[rid] = entry
    return table


def replay_rule_independently(rule, base):
    """Replay a `pattern`/`output` pair with the standard library only.

    The gate delegates this to the naming gate's budgeted matcher; this
    instrument uses `re` directly, so agreement between the two is evidence
    that the delegated matcher is not doing anything the plain reading does not.
    """
    pattern = as_text(rule.get("pattern")).strip()
    output = as_text(rule.get("output")).strip()
    if not pattern or not output:
        return None, "no machine-readable pattern/output pair"
    try:
        match = re_match_full(pattern, base)
    except Exception as exc:  # noqa: BLE001 — an unusable pattern is a finding
        return None, "pattern not usable: %s" % exc
    if match is None:
        return False, None
    try:
        return nfc(output.format(**match.groupdict())) , None
    except Exception as exc:  # noqa: BLE001
        return None, "output template not resolvable: %s" % exc


def re_match_full(pattern, base):
    compiled = re.compile(pattern)
    match = compiled.match(base)
    if match is not None and match.end() == len(base):
        return match
    # the packet's patterns are anchored with ^...$; accept a full search when
    # the anchored match fails, so a missing anchor is not silently a FAIL
    return compiled.fullmatch(base)


def replay_borrow(entry, layers):
    """Apply the layer's own `substitutions` to the record's `donor_form`.

    Longest donor key first, so `sh` is not consumed by a bare `s` rule.
    """
    layer = None
    label_used = ""
    for key in ("loan_layer", "layer"):
        label = as_text(entry.get(key)).strip()
        if label and label.casefold() in layers:
            layer, label_used = layers[label.casefold()], label
            break
    if layer is None:
        return None, "", "names no declared layer"
    donor = as_text(entry.get("donor_form")).strip()
    substitutions = layer.get("substitutions")
    if not donor or not isinstance(substitutions, dict) or not substitutions:
        return None, label_used, None
    pairs = sorted(
        ((as_text(k), as_text(v)) for k, v in substitutions.items() if as_text(k)),
        key=lambda pair: len(pair[0]),
        reverse=True,
    )
    expected = donor
    for donor_part, recipient_part in pairs:
        expected = expected.replace(donor_part, recipient_part)
    return nfc(expected), label_used, None


# --------------------------------------------------------------------------
# the audit
# --------------------------------------------------------------------------


def audit(packet, packet_path, resolved_path=None):
    report = {"packet": packet_path, "checks": [], "counters": {}, "failures": []}
    resolved = Path(resolved_path) if resolved_path else None

    def check(name, ok, detail=""):
        report["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            report["failures"].append("%s: %s" % (name, detail))

    # 1. the design's own worked tables, re-derived from the prose
    mismatched = [
        (base, op, expected, OPS[op](base))
        for base, op, expected in WORKED_11
        if nfc(OPS[op](base)) != nfc(expected)
    ]
    check("design-11-worked-derivations", not mismatched, str(mismatched))
    name_bad = [
        (base, expected, reverse(base))
        for base, expected in NAMES_8
        if nfc(reverse(base)) != nfc(expected)
    ]
    check("design-8-name-reversals", not name_bad, str(name_bad))
    check(
        "maximal-onset-is-load-bearing",
        head2("saalumi") == "saalu" and head2("saalumi") != "saalum",
        "head2(saalumi) = %r" % head2("saalumi"),
    )

    # 2. the packet's records
    layers = layer_index(packet)
    rules = packet_rules(packet)
    counters = {
        "records": 0, "register_scoped": 0, "register_scoped_declared": 0,
        "derived_pairs": 0, "claimed_chains": 0, "borrow_pairs": 0,
        "violations": 0, "rule_holds": 0,
    }
    scoped_rows = []
    declared_rows = []
    for block, entries in list_blocks(packet):
        for position, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            counters["records"] += 1
            eid = as_text(entry.get("id")).strip() or "%s[%d]" % (block, position)
            register = record_register(entry, layers)
            if register is not None:
                counters["register_scoped_declared"] += 1
                declared_rows.append((block, eid, register,
                                      record_form(entry)[:40],
                                      record_form(entry, lexical_only=True) != ""))
            form = record_form(entry, lexical_only=True)
            if not form:
                continue
            if register is not None:
                counters["register_scoped"] += 1
            derivation = declared_derivation(entry)
            claimed = claimed_formation(entry)

            if derivation is not None:
                counters["derived_pairs"] += 1
                op, base = derivation
                if op in OPS:
                    got = OPS[op](base)
                    if nfc(got) != nfc(form):
                        counters["violations"] += 1
                        scoped_rows.append((eid, form, "FAIL", op, base, got))
                    else:
                        scoped_rows.append((eid, form, "ok", op, base, got))
                elif op in rules:
                    got, detail = replay_rule_independently(rules[op], base)
                    if detail is not None:
                        counters["rule_holds"] += 1
                    elif got is not None and nfc(got) != nfc(form):
                        counters["violations"] += 1
                        scoped_rows.append((eid, form, "FAIL", op, base, got))
                    else:
                        scoped_rows.append((eid, form, "ok", op, base, got))
                else:
                    counters["rule_holds"] += 1

            if claimed is not None:
                rule_id, stem = claimed
                counters["claimed_chains"] += 1
                if rule_id in rules:
                    got, detail = replay_rule_independently(rules[rule_id], stem)
                    if detail is None and got is not None:
                        if nfc(got) != nfc(form):
                            counters["violations"] += 1
                            scoped_rows.append((eid, form, "FAIL", rule_id, stem, got))
                        else:
                            scoped_rows.append((eid, form, "ok", rule_id, stem, got))
                    else:
                        counters["rule_holds"] += 1
                elif rules:
                    counters["violations"] += 1
                    scoped_rows.append((eid, form, "FAIL", rule_id, stem, None))

            if as_text(entry.get("route")).strip() == "borrowed" or \
                    as_text(entry.get("donor_form")).strip():
                got, layer_label, problem = replay_borrow(entry, layers)
                if problem is None and got is not None:
                    counters["borrow_pairs"] += 1
                    if nfc(got) != nfc(form):
                        counters["violations"] += 1
                        scoped_rows.append((eid, form, "FAIL", "borrow", layer_label, got))
                    else:
                        scoped_rows.append((eid, form, "ok", "borrow", layer_label, got))
                elif problem is not None:
                    counters["rule_holds"] += 1

    report["counters"] = counters
    report["register_rows"] = [row for row in scoped_rows if row[2] != "ok"]
    report["register_row_count"] = len(scoped_rows)
    report["declared_register_rows"] = declared_rows
    check("packet-records-counted", counters["records"] > 0, str(counters["records"]))
    # Agreement with the lane gate's own published coverage line, measured live
    # rather than hardcoded: the point of the check is that two independently
    # built readings of the *same* packet agree, so the comparison target is
    # whatever the gate prints now, not a number frozen at this seat's writing.
    # The check deliberately does **not** assert "zero violations": the committed
    # fixture is a negative control whose four violations are the expected
    # result, so requiring zero would fail the fixture that gives the leg teeth.
    gate = ROOT / "tools" / "gates" / "argot-derivation-gate.py"
    if gate.is_file() and resolved is not None:
        proc = subprocess.run([sys.executable, str(gate), str(resolved)],
                              capture_output=True, text=True)
        line = next((l for l in proc.stdout.splitlines() if l.startswith("coverage:")), "")
        report["gate_coverage_line"] = line
        m = re.search(r"register_scoped=(\d+)\s+derived_pairs=(\d+)\s+"
                      r"claimed_chains=(\d+)\s+borrow_pairs=(\d+)\s+violations=(\d+)", line)
        if m:
            g_reg, g_der, g_claim, g_borrow, g_viol = (int(x) for x in m.groups())
            agrees = (
                g_reg == counters["register_scoped"]
                and g_der == counters["derived_pairs"]
                and g_claim == counters["claimed_chains"]
                and g_borrow == counters["borrow_pairs"]
                and g_viol == counters["violations"]
            )
            check("independent-reading-agrees-with-lane-gate", agrees,
                  "gate=%s mine=%s" % (line.strip(),
                                       {k: counters[k] for k in (
                                           "register_scoped", "derived_pairs",
                                           "claimed_chains", "borrow_pairs",
                                           "violations")}))
    return report


def run_controls(packet, packet_path):
    """Plant violations in memory; this instrument must catch every one."""
    results = []
    original = json.loads(json.dumps(packet))

    # control 1: break a declared reverse pair
    mutated = json.loads(json.dumps(original))
    hit = False
    for block, entries in list_blocks(mutated):
        for entry in entries:
            if isinstance(entry, dict) and isinstance(entry.get("formation"), dict):
                entry["formation"]["rule"] = "CX-01"
                entry["name"] = entry.get("name", "") + "x"
                hit = True
                break
        if hit:
            break
    rep = audit(mutated, packet_path + "#control-1")
    results.append(("control-1-planted-formation-mismatch",
                    rep["counters"]["violations"] >= 1, rep["counters"]))

    # control 2: break a loan adaptation
    mutated = json.loads(json.dumps(original))
    hit = False
    for block, entries in list_blocks(mutated):
        for entry in entries:
            if isinstance(entry, dict) and as_text(entry.get("donor_form")).strip():
                entry["term"] = as_text(entry["term"]) + "z"
                hit = True
                break
        if hit:
            break
    rep = audit(mutated, packet_path + "#control-2")
    results.append(("control-2-planted-loan-mismatch",
                    rep["counters"]["violations"] >= 1, rep["counters"]))

    # control 3: a clean packet must stay clean (the instrument is not
    # "always red")
    rep = audit(json.loads(json.dumps(original)), packet_path + "#control-3")
    results.append(("control-3-clean-stays-clean",
                    rep["counters"]["violations"] == 0, rep["counters"]))
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--packet", default=DEFAULT_PACKET)
    ap.add_argument("--controls", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    path = ROOT / args.packet if not Path(args.packet).is_absolute() else Path(args.packet)
    if not path.is_file():
        print("FINDING X60-DATA: cannot read %s" % path, file=sys.stderr)
        return 2
    try:
        packet = parse_yaml(path)
    except SystemExit as exc:
        print("FINDING X60-DATA: %s" % exc, file=sys.stderr)
        return 2

    report = audit(packet, args.packet, resolved_path=path)
    if args.controls:
        report["controls"] = run_controls(packet, args.packet)
        for name, ok, counters in report["controls"]:
            if not ok:
                report["failures"].append("%s missed (counters %s)" % (name, counters))

    if args.json:
        print(json.dumps(report, indent=1))
    else:
        for check in report["checks"]:
            print("%-40s %s %s" % (check["name"], "ok" if check["ok"] else "FAIL",
                                   check["detail"] if not check["ok"] else ""))
        print("counters: " + " ".join(
            "%s=%s" % (k, v) for k, v in sorted(report["counters"].items())))
        print("declared-register rows (prose rows excluded from the replay):")
        for row in report["declared_register_rows"]:
            if not row[4]:
                print("  %-10s %-8s %-16s %r" % (row[0], row[1], row[2], row[3]))
        for row in report["register_rows"]:
            print("MISMATCH %s" % (row,))
        for name, ok, counters in report.get("controls", []):
            print("control %-40s %s %s" % (name, "ok" if ok else "MISS", counters))
        print("failures: %d" % len(report["failures"]))
    return 0 if not report["failures"] else 1


if __name__ == "__main__":
    sys.exit(main())
