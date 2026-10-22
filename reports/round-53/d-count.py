#!/usr/bin/env python3
"""Round-53 claim D counter: open instances of the defects the round-52 closure routed
against corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
(corpus/lessons/round-52-verifier-spotcheck.md, "Defects found" and routed defect 1).

Run from the lane root:  python3 -B reports/round-53/d-count.py [--root DIR]

Legs (each instance counts 1 while open):
  FRAG   every `, -N` draft-id token (regex ', -[0-9]+\\b'), one per token
  WROW1  the line quoting "working their farms" does not cite S162
  WROW2  the line naming the mobile-phone decline does not cite S159, or still cites S163
  OVER1  "force fixed formulas" (line 54, Suruí two tones)
  OVER2  "(Laos, Thailand, United States) (S135)" (line 54, Hmong countries cited to S135 alone)
  OVER3  /b/ stated as merging with /k/ (line 76; S147 states it for [p] only)
  OVER4  "learned young" (line 79)
  OVER5  "in Akan (Ghana) practice" (line 121, one drummer's biography)
  OVER6  the string "primitive peoples" (line 176 sub-quote)
A routed phrase that is gone counts 0: this counter shows the routed wording is gone,
not that the replacement is true; the replacement's support is a review question.

Second figure, SID_BAD: S-ids the entry cites that are not a corpus/SOURCES.md row naming
the entry in its used-by cell. Prints `OPEN <n>`, one line per open instance, and
`SID_BAD <n> [...]`; exit 0 only when both are 0, 1 otherwise, 2 if a file is unreadable.
"""
import argparse
import os
import re
import sys

ENTRY = "corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md"
PHRASES = [
    ("OVER1", re.compile(r"force fixed formulas")),
    ("OVER2", re.compile(r"\(Laos, Thailand, United States\) \(S135\)")),
    ("OVER3", re.compile(r"/b/[^|]*merg\w* with /k/")),
    ("OVER4", re.compile(r"learned young")),
    ("OVER5", re.compile(r"in Akan \(Ghana\) practice")),
    ("OVER6", re.compile(r"primitive peoples")),
]
FRAG = re.compile(r", -[0-9]+\b")
SID = re.compile(r"\bS\d{3}\b")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    try:
        with open(os.path.join(args.root, ENTRY), encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        with open(os.path.join(args.root, "corpus/SOURCES.md"), encoding="utf-8") as fh:
            rows = {}
            for line in fh:
                if re.match(r"^\| S\d{3} ", line):
                    cells = line.split("|")
                    rows[cells[1].strip()] = cells[11] if len(cells) > 11 else ""
    except OSError as error:
        print(f"D_COUNT_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    open_items = []
    for no, text in enumerate(lines, 1):
        for match in FRAG.finditer(text):
            open_items.append(f"FRAG {ENTRY}:{no} '{match.group(0)}'")
        for name, rx in PHRASES:
            if rx.search(text):
                open_items.append(f"{name} {ENTRY}:{no}")
    farms = [i for i, t in enumerate(lines, 1) if "working their farms" in t]
    if not farms or any("S162" not in lines[i - 1] for i in farms):
        open_items.append(f"WROW1 {ENTRY}:{farms or 'absent'} 'working their farms' not cited to S162")
    phones = [i for i, t in enumerate(lines, 1) if re.search(r"mobile phone", t)]
    if not phones or any("S159" not in lines[i - 1] or "S163" in lines[i - 1] for i in phones):
        open_items.append(f"WROW2 {ENTRY}:{phones or 'absent'} mobile-phone decline not cited to S159 alone")
    cited = sorted(set(SID.findall("\n".join(lines))))
    bad = [s for s in cited if s not in rows or ENTRY not in rows[s]]
    print(f"OPEN {len(open_items)}")
    for item in open_items:
        print(f"  {item}")
    print(f"SID_BAD {len(bad)} {bad} cited {len(cited)}")
    return 0 if not open_items and not bad else 1


if __name__ == "__main__":
    sys.exit(main())
