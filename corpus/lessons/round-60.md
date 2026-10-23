# Round 60 lesson — the amulets entry re-entered under a new pre-data freeze (claim D)

Round 60, hyaku phase 4. Attempt 1 (`KotodamaR60`) and attempt 2 (`KotodamaR60A2`) died with the orchestrator process (05:25:25Z, 06:19:06Z); attempt 3 is L1 `KotodamaR60A3`. Lane base `9c82a6eb`. Instruments: revision 0 `b60e6d4e`, revision 1 `0e494ff2`/`819bf084`, revisions 2-4 `1f04b2d7`, `35de1f9c`, `f39e5ea2` (attempt 2), revision 5 `14e64138`, revisions 6-7 `b9faed93` (attempt 3); claim D build `1cd9db7c`. Attempt 2's uncommitted build (entry edits, SOURCES rows S648-S651, captures, 35 wave reports) was treated as untrusted scratch: the captures were re-fetched byte-identical (`reports/round-60/telemetry/captures-refetch.txt`) and every entry line was re-audited by 16 fresh seats before the build commit; attempt 2's wave reports are not cited.

## Spot-check intake (round-59 outside verifier)

| Item (round-59-verifier-spotcheck.md §5) | Route | Status |
|---|---|---|
| 1 post-verdict narrowing of C | SCORECARD correction table (`SCORECARD.md` round-59 correction rows), LOG correction entry, claim D re-enters the amulets entry under this freeze; QUALITY criterion 14 | done |
| 2 lost run-2 legs; fetch treatment | round-59 erratum "Final-measures run 2"; every round-60 counter run captured in full; FETCH-60 (no network leg) in `reports/round-60/claims.json` | done |
| 3 separability false positive | LOG and SCORECARD correction rows; round-60 separability runs on a counter with no network leg (ExecSeparabilityA3: `unshare -rn` runs byte-identical, 0 `connect`) | done |
| 4 R59-M5 contradicted | round-59 erratum; caches removed 04:57:02Z and 07:04:21Z (`reports/round-60/telemetry/pycache-removed*.txt`); ExecPycacheA3 shows `-B`/`PYTHONDONTWRITEBYTECODE` runs write none | done |
| 5 CtlKeyedLabels59 never scored | dropped from round 59's list with its reason (round-59 erratum); round 60 scored CtlKeyedLabelA3 (met revision 6, forced revision 7) and CtlLaneReaderA3 | done |
| 6 registry label ~03:40Z | round-59 erratum "Support registry label" | done |

## Pre-data control waves and revisions 5-7

Wave 1 (40 seats, `.ufo/waves/round-60/w1-a3/`, validated under policy v1) scored revision 5 at `14e64138` before any data seat. Results that changed the counter:

- CtlNarrowA3: CONTROL-MET under the SESSIONS-only probe — dropping the dissenting registry member, or adding a 25th, passed. Revision 6: exact 24-seat roster; dissent scanned over every frozen seat in its lane report and its session file.
- CtlKeyedLabelA3: CONTROL-MET under the probe — a packet-only program marked 48/48 planted occurrences NOT-SUPPORTED and 141/141 real occurrences SUPPORTED without reading a page or the lane. Revision 7: EVIDENCE — a SUPPORTED verdict counts only when it quotes >= 10 words of the row's pinned page text that its packet block lacks (47 pages pinned, `reports/round-60/captures/pages/`).
- DryRunHonestAA3, DryRunHonestBA3, CtlHonestConfineA3, MutConfineA3: honest calls falsely voided by revision 5's CONFINED (closing-tag regexes, a quoted bootstrap path, `:raw` read selectors, `.find("cd")`/`.find("eval")`). Revisions 6-7 fix them.
- CtlEchoA3 (e) and CtlJunkA3 (lorem) passed only under the probe with fabricated support seats: PINNED cannot tell captured from self-made bytes without a network leg; the guard is the blind SUPPORT leg plus PROVENANCE (recorded review-only).
- NONE-MET under revision 5: CtlDoNothingA3, CtlAllFalseA3, CtlRubberStampA3 (honest-shaped positive PASS under the probe), CtlNoReaderA3, CtlOldWordA3 (synonymised over-reach is stopped only by SUPPORT, as expected), CtlGenericA3 (quote-copy line stopped only by SUPPORT), MutLegsA3 (one redundant survivor, M02).
- Hold: CtlKeyedLaneA3 refused (`cyber_policy`); not retried, rerouted or rephrased; a differently designed lane-reader control (CtlLaneReaderA3) was scored in the residual call.

The residual call (6 reviewer/critic seats, `.ufo/waves/round-60/resid-a3/`) re-scored the changed controls at `1cd9db7c` before any data seat; see `## Blind support review` for its outcome and the freeze.

## Build audit (pre-freeze, attempt 3)

Sixteen audit seats (AuditA3R01-R16) re-opened all 47 pages and judged every citing line as a blind seat would. Entry lines rewritten before the freeze: S608, S609, S612, S614, S622, S624 (two lines), S625, S629 (two lines), S638, S640 (two lines), S642, S644, and S648 (attribution to "The IDD article", line and teaches; the PDF does not print the author). Registry teaches cells the audits found over-reaching but that the append-only registry and the fixed cited-id set keep unchanged this round: S601, S608, S614, S624, S636, S640, S641 (each a superseding-row candidate for the next round; disclosed before data).

## Gate

New rows opened this round (accessed 2026-10-23; quotes located in the committed captures by PINNED; first URL equals the superseded row's first URL):

- S648 | https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf | 2026-10-23 | "P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers." | supersedes S602
- S649 | https://www.metmuseum.org/art/collection/search/464456 (live 429 Vercel challenge met, not passed; capture https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456) | 2026-10-23 | "Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems" | supersedes S616
- S650 | https://footwearresearchnetwork.org/articles/concealed-shoes-revealed | 2026-10-23 | "currently suggests less and less that they were specifically apotropaic items, ones that have the power to avert evil influences or bad luck" | supersedes S623
- S651 | https://collections.vam.ac.uk/item/O87367/ | 2026-10-23 | "was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil." | supersedes S643

## Status and used-by change log

- S648, S649, S650, S651: new rows, status `mined`, used-by the amulets entry (no prior state).
- S602, S616, S623, S643: unchanged (`rejected`, used-by `—`, since round 59).

## Mistakes

| id | class | evidence | captured-by | fix (shown able to fail) |
|---|---|---|---|---|
| R60-M1 | post-verdict narrowing (round 59) | `corpus/lessons/round-59-verifier-spotcheck.md` §2 | none mechanical (the kill rule was prose) | `tools/check-judged-object.py` prints `JUDGED_OBJECT: FAIL` on round 59's own bytes (`reports/round-60/telemetry/judged-object-r59.txt`; ReviewJudgedToolA3 re-ran it and killed a mutant); QUALITY criterion 14 |
| R60-M2 | blindness by deny-list | revision 4 BLIND matched literal strings only; a glob or relative read of the lane named none | none | revision 5 CONFINED allow-list; rejected shapes in MutConfineA3 and the L1's own test set |
| R60-M3 | planted controls readable from packet text | CtlKeyedLabelA3: 48/48 planted found, 0/141 real false-NOT, no page read | none (planted design dates from round 58) | revision 7 EVIDENCE (re-scored by RescoreKeyedLabelA3) |
| R60-M4 | mutable registry as the dissent authority | CtlNarrowA3 e/f/f2 | none | revision 6 roster and full dissent scan (re-scored by RescoreNarrowA3) |
| R60-M5 | over-reach that blind seats passed | 15 base lines and 7 teaches cells flagged by AuditA3R01-R16 had been SUPPORTED by two round-59 seats each | round-59 SUPPORT (2 seats per row) did not catch them | 3 seats per row this round, pre-freeze strict audits; teaches cells routed as superseding rows |
