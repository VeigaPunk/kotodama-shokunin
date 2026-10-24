#!/usr/bin/env python3
"""Generate claim-C entry mutants (round 68, MutEntryClass seat).

Positive control must satisfy every FILE/ONEID/RESTATE/ROWS leg; each mutant
changes exactly one behavior-bearing property of the entry so the caught leg
is attributable. Registry rows S833-S856 are shared by all variants.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY_PATH = "corpus/knowledge/culture-material/hair-grooming-codes.md"
IDS = [f"S{n}" for n in range(833, 857)]
KINDS = ["spec", "docs", "paper", "code", "tool", "dataset", "talk", "book",
         "community", "own-work"]


def rows_text():
    out = []
    for i, sid in enumerate(IDS):
        host = f"host{i + 1:02d}.example.org"
        out.append(
            f"| {sid} | Source {i + 1} on grooming codes — https://{host}/a{i + 1} "
            f"| {KINDS[i % len(KINDS)]} | {'A' if i % 2 == 0 else 'B'} | "
            f"hair grooming register {i + 1} | "
            f"\"quote{sid[1:]} alpha bravo charlie delta\" | "
            f"teaches{sid[1:]} echo foxtrot golf hotel india | "
            f"mined | 2026-10-24 | 90d | {ENTRY_PATH} |")
    return "\n".join(out) + "\n"


def header(topic=True):
    lines = ["# Hair and grooming codes", ""]
    if topic:
        lines += ["- topic: hair and grooming as a cross-cultural register of "
                  "cutting, dressing, oiling, colouring and covering hair", ""]
    lines += ["## Overview", "",
              "Hair is both a material and a claim about the person who wears it.",
              "", "## Claims", ""]
    return lines


def bullets():
    return [f"- Source {i + 1}: quote{sid[1:]} alpha bravo charlie delta "
            f"marks the register (S{sid[1:]})."
            for i, sid in enumerate(IDS)]


def base_lines():
    return header() + bullets() + [""]


def write(name, lines):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    base = base_lines()
    write("entry-base.md", base)
    # M1: no '- topic:' line at all
    write("entry-m1-no-topic.md", header(topic=False) + bullets() + [""])
    # M2: an H3 present
    h = header()
    h = h[:-1] + ["### Subheading", ""]
    write("entry-m2-h3.md", h + bullets() + [""])
    # M3: exactly 251 lines
    m3 = base[:]
    n = 0
    while len(m3) < 251:
        n += 1
        m3.append(f"- padding note {n}")
    assert len(m3) == 251, len(m3)
    write("entry-m3-251lines.md", m3)
    # M4: extra bullet citing a foreign (out-of-claim-set) registry id
    write("entry-m4-foreign-cite.md",
          base[:-1] + ["- Background on grooming is treated elsewhere (S832).", ""])
    # M5: extra foreign bullet that cites nothing at all
    write("entry-m5-uncited-bullet.md",
          base[:-1] + ["- Grooming practices are widely attested across cultures.", ""])
    # M6: no real topic line; '- topic:' only inside a fenced code block
    m6 = ["# Hair and grooming codes", "", "## Overview", "", "```",
          "- topic: hair and grooming", "```", "",
          "Hair is both a material and a claim about the person who wears it.",
          "", "## Claims", ""] + bullets() + [""]
    write("entry-m6-topic-in-fence.md", m6)
    # M7: foreign registry id mentioned bare, not as '(S###)'
    write("entry-m7-bare-foreign-id.md",
          base[:-1] + ["- See S832 for background on the register.", ""])
    with open(os.path.join(HERE, "registry-rows-S833-S856.md"), "w",
              encoding="utf-8") as fh:
        fh.write(rows_text())
    print("wrote variants:",
          sorted(f for f in os.listdir(HERE) if f.startswith("entry-")))


if __name__ == "__main__":
    main()
