# Census — ScribeRows (S909-S912 inserted, S904/S905 used-by appended)

Command (from the seat's shell; lane root inferred by the script). The absolute forms below are the fleet root and
the lane root — not scratch; from the lane root the same invocation is
`../scripts/sources-census.sh validate --root .. kotodama`:
```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```
The `ok` line in the tail is the script's own output, which prints the lane registry's absolute path.

Exit code: **0** (clean; warnings only).

Tail (last 6 of 34 output lines, verbatim):
```
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	W01	S907 tierC mined used-by=corpus/knowledge/myth-symbol/guest-right-hospitality-law.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

Findings profile: 0 E-codes, 5 W01, 28 W04 (33 warning lines + the `ok` line = 34 lines).
Base comparison (read-only): `reports/round-82/telemetry/census-start.txt` carries 32 W-lines; the only new line is
`W01 S907 tierC mined used-by=corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`, which is a round-82 row
(S907 was filed tier C and mined after that census was taken), not a row this seat wrote. The four new rows add no
warning, no duplicate URL (each of S909-S912 opens a URL absent from the registry) and no E-code.

Cell shape check (every touched row re-parsed with `|` as the field separator):
```
S904 raw cells 13 content 11
S905 raw cells 13 content 11
S909 raw cells 13 content 11
S910 raw cells 13 content 11
S911 raw cells 13 content 11
S912 raw cells 13 content 11
```

Insertion point: the four rows sit at the end of the `## Registry` table, immediately before the `## Paths` heading
(lines 865-868, `## Paths` at 869) — not at end of file, so E12 (registry-shaped row outside the Registry section)
does not fire. The S913 superseding row is a draft at `.ufo/waves/round-83/w1/stage/ScribeRows/S913.row` and was NOT
inserted by this seat.
