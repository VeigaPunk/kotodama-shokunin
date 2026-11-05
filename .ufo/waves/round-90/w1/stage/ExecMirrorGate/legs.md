# ExecMirrorGate — legs (claim C pre-check on a staged mirror)

Mirror: `git archive d0b6f2a7f9cc36272682749a9b047b739406f0c8` → `<scratch>/mirror`.
ScribeEntry packet: **absent** (0 files at `<stage>/ScribeEntry/`). Legs marked
`[FIXTURE]` ran on the grader's own selftest positive-entry fixture, not on landing bytes.

## Legs

| # | leg | status | exact observed text |
|---|---|---|---|
| 1 | MATERIALIZE | PASS | `corpus/knowledge` 261 `.md`, `linguistics` 34 files, `SOURCES.md` 865 rows; no `corpus/lessons/round-90.md`, no `reports/round-90/evidence/` — equals claims.json C.before |
| 2 | ENTRY (grader entry mode, real bytes) | FAIL | `ADVANCE-EVIDENCE_ERROR: unreadable <mirror>/corpus/knowledge/linguistics/petitionary-and-votive-formulae.md: No such file or directory` (rc 2) |
| 3 | ENTRY [FIXTURE] at real registry scale (868 rows, C thresholds) | FAIL (fixture text) | `LEG FAIL ENTRY expected=>=12000B, >=6 h2, header keys observed=1377 bytes < 12000` |
| 4 | SHAPE [FIXTURE] | PASS | `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean` |
| 5 | TOPIC [FIXTURE] | FAIL (fixture text) | `LEG FAIL TOPIC expected=>=10 shared content words with the declared topic observed=entry shares 7 content words with the declared topic < 10` |
| 6 | NEWIDS [FIXTURE] | PASS | `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-04 and cited observed=clean` |
| 7 | GATE [FIXTURE] | PASS | `LEG PASS GATE expected=each new id has a located gate line observed=clean` |
| 8 | CAPTURE [FIXTURE] | PASS | `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean` |
| 9 | ENTRY all six [FIXTURE, fixture thresholds] | PASS | `ENTRY-EVIDENCE: PASS legs=6/6` (rc 0) — proves the CLI path, not the claim |
| 10 | INDEX (bare mirror) | PASS | `CORPUS-INDEX: OK files=261 rows=261 findings=0` (rc 0) |
| 11 | INDEX (rehearsal: entry + 3 rows + README moves) | PASS | `CORPUS-INDEX: OK files=262 rows=262 findings=0` (rc 0) |
| 12 | INDEX control (entry added, README untouched) | FAIL (control) | `CORPUS-INDEX: FINDINGS files=262 rows=261 findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT` (rc 1) |
| 13 | APPENDONLY (rehearsal, grader's own registry parser) | PASS | `base rows 865 lands rows 868 dup [] changed [] removed [] new ['S942','S943','S944']`; each new row `tier A status mined opened 2026-11-04 used corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` |
| 14 | CENSUS (bare mirror) | PASS | rc 0, last line `file ok <mirror>/corpus/SOURCES.md` (W04 duplicate-url warnings only) |
| 15 | CENSUS (rehearsal) | PASS | rc 0, `file ok <rehearsal>/corpus/SOURCES.md`, no line naming S942/S943/S944 |
| 16 | CENSUS control (rows appended after `## Paths`) | FAIL (control) | `file E12 S942 row outside Registry section` (also S943, S944), rc 1 |
| 17 | ROW-FRAGMENTS (lane default `--rows .ufo/waves/round-65/rows`) | PASS, vacuous | `FRAG: 0 finding(s) in 26 file(s)` (rc 0) |
| 18 | ROW-FRAGMENTS (round-90 stage dir) | PASS, vacuous | `FRAG: 0 finding(s) in 0 file(s)` (rc 0) — tool scans only `row-*.txt` with `ROW:` labels |
| 19 | Control: capture = graded file [FIXTURE] | FAIL (control) | `LEG FAIL CAPTURE … observed=S942: capture outside reports/round-90/evidence: corpus/lessons/round-90.md` |
| 20 | Control: quote absent from capture [FIXTURE] | FAIL (control) | `LEG FAIL CAPTURE … observed=S942: quote absent from capture: reports/round-90/evidence/S942.txt` |
| 21 | Control: archive stamp 2025 in a new row's source cell [FIXTURE] | FAIL (control) | `LEG FAIL GATE … observed=S942: gate line does not name the row url` (entry mode does not itself reject the year; advance mode's `surface_error` does) |
| 22 | Control: gate quote echoes the `teaches` cell [FIXTURE] | PASS (hazard) | `LEG PASS GATE … clean` + `LEG PASS CAPTURE … clean` — entry mode has no self-quote check |
| 23 | Control: one sentence twice in the entry [FIXTURE] | PASS (hazard) | SHAPE `clean`; the filler threshold is `worst > 2` |

Receipts: the real-bytes run refused at rc 2 before writing a receipt (text in
`<stage>/legs-run.log`); `<stage>/receipts/entry-receipt-fixture-C.txt`, `…-fixture-own.txt`, `…-rehearsal.txt`,
`<stage>/receipts/census-mirror.txt`, `…-rehearsal.txt`, `<stage>/legs-run.log`.

## Top three things L1 must fix before landing

1. **Put the rows inside `## Registry`, not at the file's end, and leave every base row
   byte-identical.** Census refuses an appended block after `## Paths` with
   `E12 S942 row outside Registry section` (rc 1), and the counter's APPENDONLY leg compares
   all 865 base ids cell-by-cell (`changed [] removed []` is the only clean answer).
2. **Move the README's four coupled numbers with the row.** Adding the entry alone gives
   `findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT`;
   the landing needs the row text equal to the entry's `- topic:` line verbatim,
   `## linguistics/ (34)→(35)`, `Total knowledge entries: 261→262`, and the footer
   `(total 261 files; directory totals 34/36/43/29/24/95)` → `(total 262 files; directory totals 35/36/43/29/24/95)`.
3. **Bind each gate line to the row's registry URL verbatim and to a quote that lives in its
   capture.** Observed failures: `gate line does not name the row url` (an archive-URL row
   must be named by its archive URL), `quote absent from capture`, and the manifest rules
   `sha256`/`http_status` 2xx/`fetched_at` local ISO dated 2026-11-04. The quote must be
   20+ normalized chars and ≤25 words, and its capture must sit under
   `reports/round-90/evidence/` and must not be a `--graded` file.

Caveat carried to the report: legs 22–23 show entry mode does not refuse a self-quote or a
two-fold repetition, and it does not check a Wayback stamp's year — those classes are
refused by advance mode only, so the independent re-fetch seats carry them for claim C.
