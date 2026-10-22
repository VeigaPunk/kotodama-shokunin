# Round 54 pre-dispatch — claim C clause list (seat CriticClauseList, non-author)

Read at lane commit 1ec84db. Probes ran on a `git archive 1ec84db` copy under /fast/scratch/hyaku/kotodama-r54/CriticClauseList/. Each probe is the declared GREEN builder (`criterion11-controls.py` `green()`) plus one change, run with the declared argv `python3 -B reports/round-54/accept-c.py`. Probe script: `.../CriticClauseList/probe.py`. Nothing was installed.

## Findings

1. **Fix before dispatch: C-one-new-file is wider than SET.** The statement (claims.json:17) says "the one file added under corpus/knowledge". SET only walks `*.md` files (accept-c.py:56-57). Probe NONMD adds `culture-material/masks-masquerade.notes.txt` to GREEN, and accept-c exits 0. The removal half is fully covered: there are 0 non-`.md` files under corpus/knowledge at base. Smallest fix: drop the `.endswith(".md")` filter for the added/removed sets (the base list stays valid because base has only `.md` files). Alternative: change the statement to "the one `*.md` file added".
2. **Fix before dispatch: "every cited S-id" / "every cited row" misses range citations.** `\bS\d{3}\b` (accept-c.py:75) reads `S258–S260` as two IDs, so the row in between is never checked. The lane has done this before: round 53's entry says "the full set is rows S187–S238" (gesture-co-speech-pointing.md:7). That range includes S233, which is `rejected` with used-by `—` and never appears on its own in the entry (0 matches), so accept-c never saw it. Probe RANGECITE adds rows S259 (`queued`, used-by `—`) and S260 (mined), plus the line "the full set is rows S258–S260": exit 0. This affects C-range, C-status and C-usedby. Smallest fix: expand `S\d{3}\s*[–—-]\s*S?\d{3}` ranges into the cited set (or fail the entry on any range form), and add a red control for it.
3. **Fix before dispatch: a duplicate S-id row hides a non-mined row.** `table[...] = cells` keeps the last row for each id (accept-c.py:76-79). Probe DUP puts a `queued` S250 row with used-by `—` before the mined S250 row: exit 0. This is realistic because parallel build seats each register rows. Affects C-range, C-status and C-usedby. Smallest fix: RANGE fails any cited id that has more than one SOURCES row.
4. **Fix before dispatch: C-count has no control where the count is false.** Its `red_control` (claims.json:20) points to RED-SET, but the receipt shows RED-SET keeps `count=230` (criterion11-controls.txt:19). So the count clause is never made false. Under QUALITY:39, "a clause with no control is unverified". The code does catch it: probe COUNT231 (entry plus a second `.md`, nothing removed) gives `SET FAIL count=231`, exit 1. Fix: add a RED-COUNT control, with the README row and totals adjusted so SWEEP stays PASS. Or merge C-count into C-one-new-file and say it is implied by a 229-path base list (checked by hand: the base list matches `git ls-tree 4b2299b` `.md` paths, 229).
5. **Fix before dispatch: half of C-range has no control.** "is a corpus/SOURCES.md row" has no red; RED-RANGE only tests the `<S239` half. Probe UNREG (cites S259, which has no row): exit 1 with only RANGE failing. The code passes; only the control is missing. Add it to the receipt.
6. **Note:** STATUS and USEDBY skip ids that RANGE already rejected (accept-c.py:86). That is why RED-RANGE's S238 (used by the gesture entry) shows USEDBY PASS. Whenever RANGE fails, the "every cited row" legs print PASS without checking those rows. The overall exit is still 1, so this is not a hole.
7. **Note:** FLOOR counts any `S\d{3}` token in the file, including mentions that are not citations. Padding is limited because each token must also pass RANGE, STATUS and USEDBY. USEDBY is a substring test (accept-c.py:89), so a cell containing `...masks-masquerade.md.old` would pass. A row with an unescaped `|` shifts the columns; `len<13` only catches rows with too few cells. All 238 base rows have 13 cells.
8. **Note:** accept-c.py's docstring (lines 20-21) lists 2 review-only items; claims.json lists 5. This is wording drift only.

## Statement phrase → coverage

| statement phrase | covered by |
|---|---|
| Knowledge files go from 229 to 230 | C-count / SET. Before value checked by hand (229). No red with the count false (finding 4) |
| the one file added ... is masks-masquerade.md | C-one-new-file / SET, for `.md` files only (finding 1) |
| and no file is removed | C-one-new-file / SET. Fully covered (no non-`.md` files at base) |
| accept-c.py exits 0, with its seven legs passing | the declared command itself. GREEN exit 0 with 7 legs |
| SET (... 229 paths ... plus the entry) | C-one-new-file. Tested as worded |
| SWEEP (run on its own exits 0, rows 230 files 230, missing_from_index 0) | C-index. Exit status read directly (accept-c.py:66). Tested as worded |
| FLOOR (at least 20 distinct S-ids) | C-floor. Tested (note 7) |
| RANGE (every cited S-id ≥S239 and a SOURCES row) | C-range. "every" incomplete (findings 2, 3); row half has no control (finding 5) |
| STATUS (every cited row is mined) | C-status. "every" incomplete (findings 2, 3) |
| USEDBY (every cited row names the entry) | C-usedby. "every" incomplete (findings 2, 3) |
| ACCESS (check-source-access.py exits 0) | C-access. Tested as worded |
| entry topic implied by the path; "admitted knowledge on uncovered ground" | review_only 1 and 5 |

Review-only entries: no stand-in predicate covers any of them.
- review_only 1 explicitly says the sweep's topic-equality check is not a topic check.
- review_only 3 says ACCESS reads only marker words.
- The `- topic:` grep in `gap_evidence_at_base` is used only as gap evidence; review_only 5 keeps "uncovered in substance" as a review judgment. Its numbers reproduce: 0 filenames, 1 topic line (siam-thai.md), 41 files with mentions.
- review_only 2 and 4 have no mechanical stand-in.
- Note: the date half of review_only 3 ("opened this round") could be checked mechanically against the `opened` cell. Leaving it review-only is allowed but weaker.

Every clause `words` field appears verbatim in the statement (checked by script).

## Verdict

CLAUSES UNCOVERED C-one-new-file (non-`.md` addition), C-range / C-status / C-usedby ("every cited" misses range citations and duplicate rows), C-count (no red control with the count false), C-range row-existence half (no red control)
