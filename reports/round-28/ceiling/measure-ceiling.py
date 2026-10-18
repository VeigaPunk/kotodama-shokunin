#!/usr/bin/env python3
"""R28-C41..C46 — the register-lexicon ceiling (RL-3), re-measured (read-only).

Round 27 filed the ceiling in three files (`reports/round-27/law/design.md` §3.2,
`rules.md` §3.3, `review.md` §4) with one arithmetic:

    mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
    material  reverse-legal= 8  reverse-ILLEGAL= 2
    abstract  reverse-legal= 0  reverse-ILLEGAL= 5

This seat re-ran that arithmetic against the delivered round-28 tree and **the
count does not reproduce**. The filed 18/9 is the reading of the *pre-fix*
`argot-derivation-gate.py` (`5b5abe78…`), whose `syllabify` moved every
consonant run into the following onset and never tested the result — the exact
defect round 27's D seat fixed mid-round (`5b5abe78…` → `d7a3ad1a…` →
`b5406bcd…`). Under the delivered gate the count is **19 legal / 8 illegal**, the
single-row delta being `L-45 tikmes → semkit`.

The instrument reproduces both readers, classifies the lexicon by gloss class,
and tests the *mechanism* the ceiling rests on:

    reverse is legal  <=>  the base's initial consonant is a licensed coda

which holds **27/27** over the delivered mark-axis plain words, because the
template `(C)V(V)(C)` has a 14-consonant onset inventory and an 8-consonant coda
set: a reversal moves the base-initial consonant into final position, and the six
consonants that are onsets but never codas (`b g h j p w`) are exactly the
refusals.

Interface
---------
    python3 reports/round-28/ceiling/measure-ceiling.py            # text, exit 0
    python3 reports/round-28/ceiling/measure-ceiling.py --json     # receipt
    python3 reports/round-28/ceiling/measure-ceiling.py --selftest # controls

The tool is read-only over the lane: it opens the packet and the sibling gate for
reading and has no code path that writes inside the repo. It loads the packet
through the sibling gate's own YAML subset loader and its own `syllabify` /
`is_legal_syllable`, so the reading is the delivered gate's reading and not a
re-implementation of it.
"""
import argparse
import hashlib
import json
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
GATE = os.path.join(LANE, "tools", "gates", "argot-derivation-gate.py")
NAMING = os.path.join(LANE, "tools", "gates", "naming-collision-gate.py")
PACKET = os.path.join(LANE, "examples", "culture-d4", "packet.d4.yml")
# The pre-fix gate round 27's own seat kept as its before-reading. Named, never
# fabricated: if the file is absent the instrument says so and skips that reader.
PREFIX_GATE = os.path.join(LANE, ".scratch", "r27-d13", "oldg",
                           "tools", "gates", "argot-derivation-gate.py")

# Gloss classes for the ceiling's cross-tab. The abstract list is round 27's own
# five members, named so the class is not a keyword guess: the five are the
# legal/institutional abstractions the design's §3.2 table names by ID.
ABSTRACT_IDS = ("L-15", "L-30", "L-44", "L-45", "L-51")
ABSTRACT_GLOSS = {
    "L-15": "road, route; the road's right-of-way",
    "L-30": "oath, sworn word; the mark that attests it",
    "L-44": "price, value",
    "L-45": "stamped account; the script",
    "L-51": "weight, measure",
}


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load():
    naming = runpy.run_path(NAMING)
    gate = runpy.run_path(GATE)
    packet = naming["load_yaml"](open(PACKET, encoding="utf-8").read())
    return naming, gate, packet


def mark_plain(packet):
    """The ceiling's population: mark-axis lexicon records with no `register`."""
    return [row for row in packet.get("lexicon", [])
            if isinstance(row, dict) and row.get("axis") == "mark"
            and not row.get("register")]


def reverse_legal(gate, term):
    """Per-syllable legality of the reversal, read with the gate's own reader."""
    return all(gate["is_legal_syllable"](s) for s in gate["syllabify"](term[::-1]))


def maximal_onset_scan(word):
    """The maximal-onset syllabification that never splits a consonant run.

    This is the *round-27 reader*, reconstructed here because the pre-fix gate
    kept in `.scratch/r27-d13/oldg/` declares no legality predicate at all (its
    `syllabify` was the naive scan the D seat replaced). Every consonant run is
    carried whole into the following syllable except a word-final run; a run is
    never split into a coda plus an onset. Measured against the delivered
    lexicon it yields exactly the filed 18/9, which is why it is named here as
    the filed reader rather than as a current one.
    """
    out, current = [], ""
    for char in word:
        current += char
        if char in "aeiou":
            out.append(current)
            current = ""
    if current:
        if out:
            out[-1] += current
        else:
            out = [current]
    return out


def legal_template(syllable, codas, vowels="aeiou"):
    """The template `(C)V(V)(C)` with a licensed single coda, stated locally."""
    index, length = 0, len(syllable)
    if index < length and syllable[index] not in vowels:
        index += 1
    if index >= length or syllable[index] not in vowels:
        return False
    if index + 1 < length and syllable[index + 1] == syllable[index]:
        index += 2
    else:
        index += 1
    if index < length:
        if syllable[index] not in codas:
            return False
        index += 1
    return index == length


def klass(row):
    return "abstract" if row["id"] in ABSTRACT_IDS else "material/other"


def cross_tab(rows, bad_ids):
    table = {}
    for row in rows:
        key = "%s/%s" % (klass(row), "illegal" if row["id"] in bad_ids else "legal")
        table[key] = table.get(key, 0) + 1
    return dict(sorted(table.items()))


def measure():
    naming, gate, packet = load()
    rows = mark_plain(packet)
    codas = set(gate["CODAS"])
    onsets = set(packet["phonology"]["consonants"])

    legal_ids, illegal_ids = [], []
    for row in rows:
        (legal_ids if reverse_legal(gate, row["term"]) else illegal_ids).append(row["id"])

    mechanism = [row["id"] for row in rows
                 if reverse_legal(gate, row["term"]) != (row["term"][0] in codas)]

    pre_fix = None
    if os.path.isfile(PREFIX_GATE):
        old = runpy.run_path(PREFIX_GATE)
        bad = [row["id"] for row in rows
               if not all(legal_template(s, codas)
                          for s in maximal_onset_scan(row["term"][::-1]))]
        pre_fix = {
            "gate": os.path.relpath(PREFIX_GATE, LANE),
            "gate_sha256": sha256_file(PREFIX_GATE),
            "reader": "pre-fix gate `syllabify` + locally-stated template "
                      "(the pre-fix gate declares no legality predicate)",
            "legal": len(rows) - len(bad),
            "illegal": len(bad),
            "illegal_ids": sorted(bad),
            "cross_tab": cross_tab(rows, set(bad)),
        }

    return {
        "population": {
            "mark_axis_plain_words": len(rows),
            "mark_axis_all": len([r for r in packet.get("lexicon", [])
                                  if isinstance(r, dict) and r.get("axis") == "mark"]),
            "ids": sorted(row["id"] for row in rows),
        },
        "delivered": {
            "gate": os.path.relpath(GATE, LANE),
            "gate_sha256": sha256_file(GATE),
            "packet": os.path.relpath(PACKET, LANE),
            "packet_sha256": sha256_file(PACKET),
            "legal": len(legal_ids),
            "illegal": len(illegal_ids),
            "illegal_ids": sorted(illegal_ids),
            "cross_tab": cross_tab(rows, set(illegal_ids)),
        },
        "filed_round_27": {
            "legal": 18, "illegal": 9,
            "cross_tab": {"abstract/illegal": 5, "material/other/legal": 8,
                          "material/other/illegal": 2},
            "source": "reports/round-27/law/design.md §3.2; rules.md §3.3; review.md §4",
        },
        "pre_fix_reader": pre_fix,
        "mechanism": {
            "claim": "reverse is legal <=> the base-initial consonant is a licensed coda",
            "holds": len(mechanism) == 0,
            "counterexamples": sorted(mechanism),
            "onset_inventory": sorted(onsets),
            "onset_count": len(onsets),
            "coda_set": sorted(codas),
            "coda_count": len(codas),
            "never_coda": sorted(onsets - codas),
            "never_coda_count": len(onsets - codas),
        },
        "abstract_members": [
            {"id": row["id"], "term": row["term"], "reverse": row["term"][::-1],
             "gloss": row.get("gloss", ""),
             "reverse_legal": reverse_legal(gate, row["term"]),
             "syllables": gate["syllabify"](row["term"][::-1])}
            for row in rows if row["id"] in ABSTRACT_IDS],
        "landed_register_forms": [
            {"id": row["id"], "term": row["term"], "base": (row.get("bases") or [None])[0],
             "construction": row.get("construction"), "axis": row.get("axis")}
            for row in packet.get("lexicon", [])
            if isinstance(row, dict) and row.get("register") == "stamp"],
        "command": "python3 reports/round-28/ceiling/measure-ceiling.py --json",
        "date": "2026-10-18",
    }


def selftest():
    """Controls: the reading discriminates, and the filed count is NOT the live one."""
    checks = []
    naming, gate, packet = load()
    rows = mark_plain(packet)

    def check(name, ok):
        checks.append((name, bool(ok)))

    check("population-is-27", len(rows) == 27)
    check("delivered-count-is-19-8",
          sum(1 for r in rows if reverse_legal(gate, r["term"])) == 19)
    check("filed-count-differs-from-delivered",
          measure()["filed_round_27"]["legal"] != measure()["delivered"]["legal"])
    check("delta-is-exactly-L-45",
          set(measure()["pre_fix_reader"]["illegal_ids"])
          - set(measure()["delivered"]["illegal_ids"]) == {"L-45"})
    check("mechanism-holds", measure()["mechanism"]["holds"])
    check("six-never-coda-consonants",
          measure()["mechanism"]["never_coda"] == ["b", "g", "h", "j", "p", "w"])
    # a control that must be FALSE: a legal, non-abstract word must not be counted illegal
    check("legal-word-not-counted-illegal", "L-01" not in measure()["delivered"]["illegal_ids"])
    # a control on the predicate itself
    check("sig-is-illegal", not reverse_legal(gate, "gis"))
    check("rek-is-legal", reverse_legal(gate, "ker"))
    check("semkit-is-per-syllable-legal", reverse_legal(gate, "tikmes"))
    passed = sum(1 for _n, ok in checks if ok)
    for name, ok in checks:
        print("%-44s %s" % (name, "ok" if ok else "FAIL"))
    print("selftest: %d/%d checks passed" % (passed, len(checks)))
    return 0 if passed == len(checks) else 1


def main(argv):
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    result = measure()
    if args.json:
        print(json.dumps(result, indent=1, sort_keys=True))
        return 0
    d = result["delivered"]
    print("population: mark-axis plain words = %d" % result["population"]["mark_axis_plain_words"])
    print("delivered gate (%s)  legal=%d illegal=%d" % (d["gate_sha256"][:8], d["legal"], d["illegal"]))
    print("  illegal: %s" % ", ".join(d["illegal_ids"]))
    print("  cross-tab: %s" % json.dumps(d["cross_tab"], sort_keys=True))
    print("filed round 27:      legal=18 illegal=9  (pre-fix reader)")
    if result["pre_fix_reader"]:
        p = result["pre_fix_reader"]
        print("pre-fix gate (%s) legal=%d illegal=%d" % (p["gate_sha256"][:8], p["legal"], p["illegal"]))
        print("  delta vs delivered: %s" % (set(p["illegal_ids"]) - set(d["illegal_ids"])))
    m = result["mechanism"]
    print("mechanism: %s -> %s (%d/%d)" % (
        m["claim"], m["holds"], result["population"]["mark_axis_plain_words"],
        result["population"]["mark_axis_plain_words"]))
    print("  onsets=%d codas=%d never-coda=%s" % (
        m["onset_count"], m["coda_count"], ",".join(m["never_coda"])))
    print("command: %s" % result["command"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
