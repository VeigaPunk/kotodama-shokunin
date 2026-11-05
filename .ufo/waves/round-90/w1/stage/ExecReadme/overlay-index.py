#!/usr/bin/env python3
"""Overlay the claim-C corpus index row + counts onto the staged mirror.

Read-only w.r.t. the lane: operates on $S/mirror only.
The entry file created here is a TOPIC-FIELD FIXTURE, not the production entry
(the production body is ScribeEntry's); it exists so the index tool's
MISSING_ROW/GHOST_ROW legs can be exercised on the row itself.
"""
import json
import pathlib
import sys

TOPIC = ("petitionary address and votive formulae: vocative address to deities, "
         "petition mood (imperative, optative, precative), the conditional vow, "
         "votive inscription grammar, prayer-register archaism and parallelism, "
         "design procedure and failure modes")
FILENAME = "petitionary-and-votive-formulae.md"
ROW = "- `%s` — %s" % (FILENAME, TOPIC)
ANCHOR = "- `orality-formulaic-language.md`"
LANDING = """

## Round 90 petitionary and votive entry (2026-11-04)

`knowledge/linguistics/petitionary-and-votive-formulae.md` adds a dedicated
entry on petitionary address and votive formulae: vocative address to deities,
the petition mood (imperative, optative, precative), the conditional vow,
votive inscription grammar, prayer-register archaism and parallelism, and the
design procedure with its failure modes. At base the surface existed only as
sub-sections of six entries and no knowledge filename carried
prayer|petition|votive|supplicat. Sources %s were opened this round.
This is coverage, not freshness: no older registry row is re-verified,
re-dated or repaired.

Total knowledge entries: 262.

Counts checked 2026-11-04 from the repo root:
`python3 -B tools/check-corpus-index.py --root .`
(total 262 files; directory totals 35/36/43/29/24/95).
"""


def main():
    root = pathlib.Path(sys.argv[1])
    ids = " ".join(sys.argv[2:]) or "S942 S943 S944"
    readme = root / "corpus/README.md"
    text = readme.read_text(encoding="utf-8")

    # 1. row, in filename order inside the linguistics span
    anchor_idx = text.index(ANCHOR)
    line_end = text.index("\n", anchor_idx) + 1
    text = text[:line_end] + ROW + "\n" + text[line_end:]

    # 2. partition header 34 -> 35
    assert text.count("## linguistics/ (34)\n") == 1
    text = text.replace("## linguistics/ (34)\n", "## linguistics/ (35)\n")

    # 3. new round section: total line + live footer (supersedes the r89 block)
    text = text.rstrip("\n") + "\n" + (LANDING % ids)

    readme.write_text(text, encoding="utf-8")

    # 4. topic-field fixture entry (production body is not mine to write)
    entry = root / "corpus/knowledge/linguistics" / FILENAME
    # the `- sources:` line is load-bearing for the tool: TOPIC_RE terminates the
    # topic block only at a following `- <word>` field, so a bare topic line reads
    # as NO_TOPIC_FIELD (measured: that was the first overlay run's single finding).
    entry.write_text("- topic: " + TOPIC + "\n- sources: " + ids + "\n",
                     encoding="utf-8")

    print("overlay: row inserted after", ANCHOR.strip())
    print("overlay: header 34 -> 35; appended r90 landing block (total 262, footer 35/36/43/29/24/95)")
    print("overlay: fixture entry", entry.relative_to(root))


if __name__ == "__main__":
    main()
