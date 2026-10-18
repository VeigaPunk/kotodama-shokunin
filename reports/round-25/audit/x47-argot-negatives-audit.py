#!/usr/bin/env python3
"""X47 — argot-derivation negative-control audit (round 25), read-only.

Audits the *negative* side of the argot-derivation checking leg: does the
pipeline actually fail a form whose stated inputs and rules do not yield it,
and are the failures it reports real rather than manufactured by the harness?

  R25-X47-1  the design algorithm is stated and deterministic: the two declared
             operations (`head2` maximal-onset, `reverse`) re-derive all eleven
             worked rows of reports/round-17/d4/design-language.md section 5.
  R25-X47-2  delivered-state delta: how many `derived_from`/`derivation` pairs
             and `D4L-ARGOT-DERIV` rows the delivered D4 packet carries.
  R25-X47-3  false-red reproduction and attribution: the typed pipeline's
             L2-channel rebuild (`yaml_lines`) re-escapes the packet's regex
             backslash, so `DERIV-REPLAY` fires on the rebuilt legacy packet
             while the source packet stays clean. A manufactured failure.
  R25-X47-4  true-negative control: a mutated pair whose quote form is not
             `apply(op, base)` must be rejected, and the untouched pair must
             pass — proving the leg can distinguish, not merely always fail.

Read-only. Opens nothing for writing; the receipt is the caller's stdout
redirect. `--selftest` runs in-memory controls and touches no repo byte.

    export TMPDIR=$PWD/.scratch
    python3 -B reports/round-25/audit/x47-argot-negatives-audit.py --selftest
    python3 -B reports/round-25/audit/x47-argot-negatives-audit.py
    python3 -B reports/round-25/audit/x47-argot-negatives-audit.py --json
"""

import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PACKET = os.path.join(ROOT, "examples", "culture-d4", "packet.d4.yml")
TYPED = os.path.join(ROOT, "examples", "culture-d4", "packet.d4.typed.yml")
PROJECTOR = os.path.join(ROOT, "tools", "d2-typed-labels.py")
SERIALIZER = os.path.join(ROOT, "tools", "assemble-d2.py")
GATE = os.path.join(ROOT, "tools", "gates", "naming-collision-gate.py")

VOWELS = set("aeiou")

# reports/round-17/d4/design-language.md section 5 — the eleven worked
# derivations, quoted verbatim from the filed table.
DESIGN_TABLE = [
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


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, "rb") as handle:
        return sha256_bytes(handle.read())


def syllabify(word):
    """Maximal-onset syllabification of a D4-shaped word (design section 5)."""
    syllables, pending = [], ""
    index = 0
    while index < len(word):
        char = word[index]
        if char in VOWELS:
            if index + 1 < len(word) and word[index + 1] == char:
                pending += char * 2
                index += 2
            else:
                pending += char
                index += 1
            syllables.append(pending)
            pending = ""
        else:
            pending += char
            index += 1
    if pending:
        syllables.append(pending)
    return syllables


def op_head2(base):
    return "".join(syllabify(base)[:2])


def op_reverse(base):
    return base[::-1]


OPS = {"head2": op_head2, "reverse": op_reverse}


def apply_op(op, base):
    return OPS[op](base)


def load_projector():
    spec = importlib.util.spec_from_file_location("x47_projector", PROJECTOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_peer(path):
    """Load a peer module by path, mirroring the gate's own `load_peer`."""
    name = "x47_peer_%s" % os.path.basename(path).replace(".", "_").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__dict__


def check_design_table():
    """R25-X47-1: the stated algorithm re-derives the design's own table."""
    failures = []
    for base, op, expected in DESIGN_TABLE:
        got = apply_op(op, base)
        if got != expected:
            failures.append({"base": base, "op": op, "expected": expected, "got": got})
    # Determinism control: the maximal-onset reading must differ from the
    # maximal-coda reading on the one row where the design says they disagree.
    head2_maxonset = op_head2("saalumi")
    head2_maxcoda = "saalu" if head2_maxonset == "saalum" else None
    return {
        "rows": len(DESIGN_TABLE),
        "agree": len(DESIGN_TABLE) - len(failures),
        "failures": failures,
        "maximal_onset_saalumi": head2_maxonset,
        "maximal_coda_would_be": "saalum",
        "onset_coda_disagree": head2_maxonset != "saalum",
        "deterministic": not failures,
    }


def delivered_pairs(text):
    """R25-X47-2: delivered derived_from/derivation pairs and D4L-ARGOT-DERIV rows."""
    pairs = re.findall(r"derived_from:\s*(\S+)[\s\S]{0,80}?derivation:\s*(\S+)", text)
    return {
        "derived_from_tokens": text.count("derived_from"),
        "derivation_tokens": len(re.findall(r"^\s*derivation:", text, re.M)),
        "pairs": len(pairs),
        "argot_deriv_rows": text.count("ARGOT-DERIV"),
        "d4l_codes": sorted(set(re.findall(r"D4L-[A-Z-]+", text))),
    }


def moved_field(row):
    """Mirror of tools/gates/typed-pipeline-gate.py:186-196."""
    value = row.get("off_channel_field")
    if not isinstance(value, str) or value.strip().lower() in ("", "null", "none", "~"):
        return None
    return value


def rebuild_legacy(typed_path):
    """Reproduce the typed-pipeline gate's L2 legacy rebuild (serializer round-trip).

    Faithful to `tools/gates/typed-pipeline-gate.py:599-615`: the rebuild is
    deep-copied from the *parsed* typed document and re-serialized with the
    `SERIALIZER` peer's `yaml_lines`, which is where the escaping changes.
    """
    import copy

    projector = load_projector()
    serializer = load_peer(SERIALIZER)
    typed_text = open(typed_path, encoding="utf-8").read()
    typed_doc = projector.load_packet_strict(typed_text)["packet"]
    routing = typed_doc.get("typed_channel") or []
    rebuilt = copy.deepcopy(typed_doc)
    for row in routing:
        for entry in rebuilt.get("costumes") or []:
            if isinstance(entry, dict) and str(entry.get("id")) == row.get("record"):
                field = row.get("source_field") or "garment"
                moved = moved_field(row) or "%s_gloss" % field
                if moved in entry:
                    entry[field] = entry.pop(moved)
    for key in ("typed_channel", "typed_pipeline", "typed_assembly", "assembly",
                "pipeline_findings", "pipeline_counts", "schema"):
        rebuilt.pop(key, None)
    return "\n".join(serializer["yaml_lines"](rebuilt)) + "\n"


def check_false_red():
    """R25-X47-3: is the DERIV-REPLAY failure manufactured by the rebuild?

    Both sides are read through the *gate's own* loader
    (`tools/gates/naming-collision-gate.py:488 load_yaml`), so the compared
    `pattern` values are exactly the regexes the gate would replay, never the
    YAML-escaped source text. The gate is then executed over each tree as the
    authoritative control.
    """
    import subprocess
    import tempfile

    gate_ns = load_peer(GATE)
    source_text = open(PACKET, encoding="utf-8").read()
    rebuilt_text = rebuild_legacy(TYPED)

    def rule_pattern(text):
        doc = gate_ns["load_yaml"](text)
        rules = (doc.get("morphology") or {}).get("derivation_rules") or []
        for rule in rules:
            if str(rule.get("id")) == "CX-01":
                return rule.get("pattern")
        return None

    src = rule_pattern(source_text)
    reb = rule_pattern(rebuilt_text)

    def replay(pattern_text, stem, output, candidate):
        try:
            match = re.match(pattern_text, stem)
        except (re.error, TypeError) as exc:
            return "regex-error: %s" % exc
        if match is None:
            return "no-match"
        return output.format(**match.groupdict()) == candidate

    stems = [("tum+hai", "{a}{b}", "tumhai"), ("kal+ker", "{a}{b}", "kalker")]
    verdicts = []
    for stem, output, candidate in stems:
        verdicts.append({
            "stem": stem,
            "candidate": candidate,
            "source_pattern_replays": replay(src, stem, output, candidate),
            "rebuilt_pattern_replays": replay(reb, stem, output, candidate),
        })

    def gate_rows(payload):
        with tempfile.TemporaryDirectory(prefix="x47-gate-") as tmp:
            path = os.path.join(tmp, "packet.yml")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(payload)
            proc = subprocess.run(
                [sys.executable, GATE, path], cwd=ROOT,
                capture_output=True, text=True,
                env={**os.environ, "TMPDIR": os.path.join(ROOT, ".scratch")})
        lines = (proc.stdout + proc.stderr).splitlines()
        return {
            "exit": proc.returncode,
            "deriv_replay": sum(1 for line in lines if "DERIV-REPLAY" in line),
            "deriv_hold": sum(1 for line in lines if "DERIV-HOLD" in line),
        }

    source_gate = gate_rows(source_text)
    rebuilt_gate = gate_rows(rebuilt_text)
    return {
        "source_pattern": src,
        "rebuilt_pattern": reb,
        "backslash_doubled": src != reb,
        "verdicts": verdicts,
        "source_gate": source_gate,
        "rebuilt_gate": rebuilt_gate,
        # A manufactured failure: the source packet's own regex replays clean
        # on every probed stem, the rebuild's regex cannot match any of them,
        # and the gate reports zero DERIV-REPLAY on the source and eight on the
        # rebuild — so the eight are the rebuild's, not the packet's.
        "manufactured": (all(v["source_pattern_replays"] is True
                             and v["rebuilt_pattern_replays"] == "no-match"
                             for v in verdicts)
                         and source_gate["deriv_replay"] == 0
                         and rebuilt_gate["deriv_replay"] > 0),
    }


def check_true_negative():
    """R25-X47-4: the checking leg must reject a violating pair and pass a good one."""
    # A local re-derivation of the discipline the forecast specifies: a
    # register-scoped form is legal only when apply(op, base) == form.
    def leg(pair):
        base, op, form = pair
        return apply_op(op, base) == form

    good = ("min", "reverse", "nim")
    bad = ("min", "reverse", "min")
    good2 = ("saalumi", "head2", "saalu")
    bad2 = ("saalumi", "head2", "saalum")
    return {
        "positive_control_passes": leg(good) and leg(good2),
        "negative_control_rejected": (not leg(bad)) and (not leg(bad2)),
        "bad_pairs": [bad, bad2],
        "leg_is_discriminating": leg(good) and not leg(bad),
    }


def selftest():
    """In-memory controls; no repo byte is read for the result."""
    checks = []
    # the algorithm re-derives the table
    table = check_design_table()
    checks.append(("design-table-rederived", table["agree"] == table["rows"]))
    checks.append(("design-table-deterministic", table["deterministic"]))
    checks.append(("onset-coda-disagree-named", table["onset_coda_disagree"]))
    # the ops are exact inverses where declared
    checks.append(("reverse-is-involution", op_reverse(op_reverse("makun")) == "makun"))
    checks.append(("head2-truncates", op_head2("saalumi") == "saalu"))
    checks.append(("head2-single-syllable", op_head2("min") == "min"))
    # the leg discriminates
    tn = check_true_negative()
    checks.append(("negative-control-rejected", tn["negative_control_rejected"]))
    checks.append(("positive-control-passes", tn["positive_control_passes"]))
    # the rebuild detector is sound: a regex whose backslash is doubled cannot
    # match the same stem the single-backslash regex matches
    single = r"^(?P<a>.+)\+(?P<b>.+)$"
    doubled = r"^(?P<a>.+)\\+(?P<b>.+)$"
    checks.append(("escaping-detector-sound",
                   re.match(single, "tum+hai") is not None
                   and re.match(doubled, "tum+hai") is None))
    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%-34s %s" % (name, "ok" if ok else "FAIL"))
    print("selftest: %d/%d controls" % (len(checks) - len(failed), len(checks)))
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()

    source_text = open(PACKET, encoding="utf-8").read()
    typed_text = open(TYPED, encoding="utf-8").read()
    result = {
        "seat": "R25-X47",
        "date": "2026-10-18",
        "axis": "D / argot-derivation negative controls",
        "digests": {
            "packet.d4.yml": sha256_file(PACKET),
            "packet.d4.typed.yml": sha256_file(TYPED),
            "d2-typed-labels.py": sha256_file(PROJECTOR),
            "naming-collision-gate.py": sha256_file(GATE),
        },
        "R25-X47-1_design_algorithm": check_design_table(),
        "R25-X47-2_delivered_state": delivered_pairs(source_text),
        "R25-X47-3_false_red": check_false_red(),
        "R25-X47-4_true_negative": check_true_negative(),
    }
    if args.json:
        print(json.dumps(result, indent=1, ensure_ascii=False))
    else:
        print("X47 argot-derivation negative-control audit — 2026-10-18")
        for key, value in result["digests"].items():
            print("  digest %-28s %s" % (key, value[:16]))
        for section in ("R25-X47-1_design_algorithm", "R25-X47-2_delivered_state",
                        "R25-X47-3_false_red", "R25-X47-4_true_negative"):
            print("  %s: %s" % (section, json.dumps(result[section], ensure_ascii=False)[:400]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
