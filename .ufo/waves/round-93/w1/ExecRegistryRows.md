# ExecRegistryRows — round-93 w1 registry verification (2026-11-05)

## Files written (all inside stage /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/ExecRegistryRows/)
- `SOURCES.new.md` — patched registry, 1054848 B, base corpus/SOURCES.md + exactly 4 rows
- `SOURCES.diff` — unified diff against base, 4700 B, 1 hunk (@@ -914,6 +914,10 @@), 4 insertions(+), 0 deletions(-)
- `search-log-note.md` — 906 B prose note for the Search log section
- this report

## Registry checks
- Last registry row in base `corpus/SOURCES.md`: `| S960 |` at line 916 (of 1064); table ends there, `## Paths` follows at line 918. Insertion point: directly after line 916.
- Cell counts per proposed row (awk -F'|', NF-2): S961 11 cells, S962 11 cells, S963 11 cells, S964 11 cells — identical to base S960 (13 fields). NF==13 also proves no cell text contains a pipe.
- Ids S961–S964 unused in base: `grep -c 'S96[1-4]' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` → 0 (2026-11-05). Sequential after S960.
- Each id occurs exactly once in `SOURCES.new.md` (`grep -c` per id: 1,1,1,1).

## Census
- Scratch tree `/fast/scratch/hyaku/kotodama-r93/ExecRegistryRows/tree/`: full copy of lane `corpus/` + `SKILL.md` + `tools/ledger-token-guard.py`, `corpus/SOURCES.md` replaced by the patched file, stub `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md` created.
- Command: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /fast/scratch/hyaku/kotodama-r93/ExecRegistryRows/tree/corpus/SOURCES.md` → **rc 0** (2026-11-05), final line `ok <file>`.
- E-findings: **0**. No finding names S961–S964.
- W-findings (all pre-existing base rows, not introduced by the patch): 29 × W04 duplicate-url across scopes (S127–S133, S185, S186, S358, S482–S490, S561–S573, S648–S651, S830, S927, S928) and 5 × W01 tierC mined used-by (S881, S882, S884, S893, S907).
- First probe on a SOURCES.md-only tree gave rc 1 with E11 "missing used-by" flood — the documented tree-completeness false positive (counter-revisions.md); not a patch defect. Resolved by materializing the full tree; recorded here for the lesson.

## Diff stat
- `diff -u base-SOURCES.md SOURCES.new.md`: 1 file changed, 4 insertions(+), 0 deletions(-); single hunk at line 917.

## Search-log note
- Written to `search-log-note.md`: DOAJ query "greeting formulas", 2026-11-05; identified 14, screened 10 (first page), included 4 across the round, rest excluded with reasons in the lesson's Gate; stop rationale first-page saturation. No S-id in the note.

## Commands run (rc)
- `grep -c 'S96[1-4]' <lane>/corpus/SOURCES.md` → 0, rc 0
- `awk -F'|'` cell counts on source-rows.md rows and patched rows → 13 fields each, rc 0
- `bash scripts/sources-census.sh validate --file <tree>/corpus/SOURCES.md` → rc 0 (probe-only rc 1 run documented above)
- `diff -u` base vs new → rc 1 (differences found, as expected)

## Risks / notes for L1
- None on the rows themselves. The E11 tree-completeness trap: any validator run must point `--file` at a SOURCES.md living in a tree that contains every used-by target (full corpus/ plus SKILL.md and tools/ledger-token-guard.py).
- Scratch `/fast/scratch/hyaku/kotodama-r93/ExecRegistryRows` deleted before yield.
