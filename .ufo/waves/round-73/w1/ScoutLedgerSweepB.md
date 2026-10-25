# ScoutLedgerSweepB — calibration ledger sweep, part B (round-73 w1)

Seat: `ScoutLedgerSweepB` (leaf, godspeed). No subagents, no background jobs, no installs
(no tool installed; RULES.md not consulted because nothing was installed). No live fetches
were performed — all evidence below is local repo bytes (no UA records needed). Lane:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Read sources: `SKILL.md`, `SCORECARD.md`
(rounds 68–72), `.ufo/reports/round-72/kotodama.md` (incl. appended errata 1–5),
`reports/round-72/telemetry/*`, `.ufo/waves/round-72/w1/{swarm-registry,dispatch}.json`,
`corpus/SOURCES.md`, `corpus/README.md`. Current HEAD = `8841ad3` (round-72 verifier
spot-check), which equals the round-73 claims base (claims.json `base` = `8841ad3`).

Legend: mismatch **Y** = stated text disagrees with observed bytes now; **N** = agrees.
Flag: **repairable** = repo state can be fixed / line corrected (append-only correction row);
**annotate** = filed bytes must stay, needs a correction/pointer row, or the claim needs a
committed receipt to back it.

## Mismatches (first)

| # | stated_at | verbatim stated text | observe command | observed value now | mismatch | flag |
|---|---|---|---|---|---|---|
| M1 | SCORECARD.md:1401 | `ACCEPT-CA-72 PASS legs=12/12 at the measured revision` | `cat reports/round-72/telemetry/measures-ca.txt` | `ACCEPT-CA-72: FAIL legs=12/12`; `exit=1`; `LEG FAIL REPORTCORR` (fleet-rev=MISSING), `LEG FAIL REPORTLAST` (commits=10 report-names-lands=False); receipt stamps revision `21ad3088` — the same revision the row cites | Y | repairable (commit a post-report rerun PASS receipt at the stamped revision, or an ANNOTATE row naming the pair id + stated token + observed token per claims Ca) |
| M2 | .ufo/reports/round-72/kotodama.md:27 | `at ac0d18ee 10/12 legs PASS — the two failing legs (REPORTCORR, REPORTLAST) evaluate this fleet report and pass on the post-report rerun at the same revision (verified after filing: both counters re-run, REPORTCORR+REPORTLAST PASS)` | `cat reports/round-72/telemetry/measures-ca.txt`; `ls reports/round-72/telemetry/` | The committed receipt still reads `LEG FAIL REPORTCORR`, `LEG FAIL REPORTLAST`, `ACCEPT-CA-72: FAIL legs=12/12`. No post-report rerun receipt exists anywhere under `reports/round-72/telemetry/` (only measures-ca.txt, measures-c.txt, controls-ca.txt, census-start/end.txt) | Y | annotate (the after-filing rerun PASS is unbacked by any committed receipt; file one) |
| M3 | SCORECARD.md:1407 | `16/32 attack roles = 50%` | python: load `.ufo/waves/round-72/w1/swarm-registry.json`, count roles | 32 members; attack roles (reviewer+critic+mutation-tester) = 6+5+3 = **14/32 = 43.75%**; non-attack 18/32 (scout 7, executor 4, scribe 3, sentinel 1, connector 1, revenger 1, simplifier 1). The round-72 fleet report itself contains **no** role tally (only 32 seats, 26/32 returned, dead list) — the 16/32 figure is not derivable from the report | Y | repairable (append a correction row recording observed 14/32; SCORECARD is append-only, so an in-place rewrite is excluded) |
| M4 | SKILL.md §Gates and probes registry (lines 662–697) — absence | no registry rows for `accept-c-71`, `accept-c-72`, `accept-ca-71`, `accept-ca-72` while the gates exist | `grep -n 'accept-ca-7\|accept-c-7' SKILL.md` → no match; `ls reports/round-7*/accept-*.py` | files exist: `reports/round-71/accept-c.py`, `reports/round-71/accept-ca.py`, `reports/round-71/accept-d.py`, `reports/round-72/accept-c.py`, `reports/round-72/accept-ca.py` — registry gap for the four 71/72 counter gates | Y | repairable (add the four rows) |
| M5 | claims.json (round-73) Ca `before` — R3 | `SKILL.md §Gates and probes registry has no rows for accept-ca-70..72 / accept-c-70..72 although those gates exist` | `ls reports/round-70/` | round-70 has **no** `accept-*.py` files (only claims.json, corrections-r69.md, telemetry/) — the premise "those gates exist" is false for round-70, true for 71/72 | Y | annotate (narrow the pair to 71/72; no round-70 gate needs a row) |
| M6 | corpus/README.md:732 | `Total knowledge entries: 243.` | `find corpus/knowledge -type f -name '*.md' \| wc -l` | **245** (`grep -c '^| S[0-9]' corpus/SOURCES.md` = 799 rows; knowledge file count 245) | Y | repairable (append a dated correction line per round-20 README convention) |
| M7 | claims.json (round-73) Ca `before` — R1 / untracked check | `two round-72 w1 seat files untracked (git ls-files --others --exclude-standard .ufo/waves/round-72 lists ScoutMergeScan.md and ScribeLesson.md)` | `git -C … ls-files --others --exclude-standard` | `.ufo/waves/round-72/w1/ScoutMergeScan.md` and `.ufo/waves/round-72/w1/ScribeLesson.md` are still untracked (30 of 32 w1 seat .md files tracked). Remaining untracked items are round-73 pre-freeze drafts (claims.json, telemetry/census-start.txt, w1 wave files) — expected pre-freeze | Y | repairable (git add the two w1 reports) |
| M8 | .ufo/reports/round-72/kotodama.md:27 | `at base b60c7b1 do-nothing control FAILS (reports/round-72/telemetry/controls-ca.txt, 9/12 fail)` | `cat reports/round-72/telemetry/controls-ca.txt`; `git show a7ab3bd:reports/round-72/telemetry/controls-ca.txt` | committed controls-ca.txt at HEAD = **8 fail / 4 pass** (QUAL20, W2FILES, LOGCORR, LESSONCORR, MAPCORR, CASTAMP, QUAL21, CAPOEIRA FAIL; REPORTCORR, APPENDONLY, REPORTLAST, NOHARM PASS). At freeze `a7ab3bd` and at `82e9e680^` it was 12/12 FAIL. No committed version reads 9/12 (the post-landing refresh at `82e9e680` superseded the earlier count) | Y | annotate (the refresh superseded the number; record old→new: 9/12 claim → 8/12 at HEAD, 12/12 pre-refresh) |

## Matches

| # | stated_at | verbatim stated text | observe command | observed value now | mismatch | flag |
|---|---|---|---|---|---|---|
| N1 | SCORECARD.md:1402 | `ACCEPT-C-72 PASS legs=10/10` | `cat reports/round-72/telemetry/measures-c.txt` | `ACCEPT-C-72: PASS legs=10/10`, `exit=0`, 10/10 legs PASS | N | — |
| N2 | .ufo/reports/round-72/kotodama.md:28 | `ACCEPT-C-72: PASS legs=10/10 (measures-c.txt)` | same | same | N | — |
| N3 | .ufo/reports/round-72/kotodama.md:31 / SCORECARD.md:1405 | `registry 797 → 799 rows (S874, S875 mined, used-by exactly the admitted entries)` | `grep -c '^| S[0-9]' corpus/SOURCES.md`; `grep -n '^| S874\|^| S875' corpus/SOURCES.md` | 799 data rows; S874 at line 829, S875 at line 830, both referencing the two admitted heritage-taxonomy entries | N | — |
| N4 | .ufo/reports/round-72/kotodama.md:32 | `census exit 0 at round start (797 rows) and round end (799 rows)` | `cat reports/round-72/telemetry/census-start.txt; cat …/census-end.txt` | both end with `kotodama ok …/corpus/SOURCES.md` (exit 0). Caveat: the two receipts are **byte-identical** (`diff` = IDENTICAL) and print no row counts, so the 797→799 delta is not evidenced inside the receipts themselves | N | annotate (note only) |
| N5 | .ufo/reports/round-72/kotodama.md:47 | `26 of 32 seat reports returned (dead/settled-late: ScoutCDXCanonical, ScoutMergeScan, ScoutRegisterMap, SimplifierRows, RevEntryQuality→returned, RevSeparability, ScribeLesson — recorded, none replaced)` | `git ls-files '.ufo/waves/round-72/w1/*.md' \| wc -l`; glob w1 | 32 seat .md files on disk, 30 tracked (2 untracked → M7); `RevSeparability.md` absent (never returned) — consistent with the dead list; RevEntryQuality present ("→returned") | N | — |
| N6 | .ufo/reports/round-72/kotodama.md:3 | `base b60c7b1 · final lane HEAD 11a41fbf (round work graded at ac0d18ee)` | `git cat-file -e <c>^{commit}` | `b60c7b1`, `ac0d18e`, `11a41fb` all exist; later commits `334d79d`, `82e9e68`, `4cc0dd8`, `2cf4da7`, `3adbd4a`, `8841ad3` follow (HEAD) | N | — |
| N7 | .ufo/reports/round-72/kotodama.md:51-53 (erratum 2) | `Fixed at lane f0a4e98 … the hygiene commit is 82e9e680 (the hash named above was provisional)` | `git cat-file -e` | `f0a4e98` MISSING, `82e9e680` EXISTS — the correction is accurate | N | — |
| N8 | .ufo/reports/round-72/kotodama.md:9 | `the seven round-71 w2 seat files committed (Filler30, RevReceipts modified; CritTrends, Filler28, Filler36, RevCounterCa, RevEntry untracked)` | `git ls-files '.ufo/waves/round-71/w2/*'` | all seven named files are tracked (44 w2 files tracked incl. Filler30.md, RevReceipts.md, CritTrends.md, Filler28.md, Filler36.md, RevCounterCa.md, RevEntry.md) | N | — |
| N9 | .ufo/reports/round-72/kotodama.md:9 | `QUALITY criterion 20 committed (was worktree-only …) … criterion 21 committed` | `grep -c '^20\. ' corpus/QUALITY.md`; `grep -c '^21\. ' corpus/QUALITY.md` | 20 → 1; 21 → 1 | N | — |
| N10 | claims.json (round-73) `base` | `8841ad3b896a0227674fa0725b818c999118046f` | `git rev-parse HEAD` | HEAD = `8841ad3b896a0227674fa0725b818c999118046f` — claims frozen exactly at current HEAD | N | — |
| N11 | .ufo/reports/round-72/kotodama.md:14 | `two entries admitted … heritage-taxonomy-models.md + .amend-2026-10-24-r13.md` | `ls corpus/knowledge/culture-material/heritage-taxonomy-models*.md` | both files exist (8748 B / 3367 B) | N | — |
| N12 | SCORECARD.md:1407 | `one v1 wave of 32 seats (policy v1, band 32-64 …)` | python: `dispatch.json` policy | `counts.spawn=32`; policy schema `ufo-swarm-wave-dispatch-v1`; `waveMinLanes=32`, `waveMaxLanes=64` → band 32–64 confirmed (only the attack-role fraction fails, M3) | N | — |

## Observations relevant to the round-73 Ca ledger

- The two round-72 w1 untracked files (M7), the `ACCEPT-CA-72` PASS-vs-FAIL split (M1/M2),
  the SKILL registry gap for 71/72 (M4/M5), and the README 243-vs-245 count (M6) replicate the
  round-73 claims Ca R1–R4 pair set exactly as drafted; they are live pre-data mismatches.
- `measures-ca.txt` header note ("PASS on the post-report rerun at this revision") contradicts
  the file's own verdict line (`FAIL legs=12/12`) — the note is a claim, the verdict is the
  recorded result (M1/M2).
- `controls-ca.txt` history: `a7ab3bd` 12/12 FAIL → `82e9e680` refresh 8/12 FAIL; the fleet
  report's "9/12 fail" matches no committed version (M8).
- No tool installs performed; nothing fetched; no RULES.md consultation needed.

## Acceptance of the assignment's required checks

1. SCORECARD round-72 calibration row `ACCEPT-CA-72 PASS legs=12/12` vs `measures-ca.txt` → **mismatch** (M1).
2. SKILL.md registry rows vs `ls reports/round-7*/accept-*.py tools/gates` → **mismatch** for 71/72 rows (M4); round-70 premise false (M5); `tools/gates` listing confirmed.
3. SCORECARD round-72 shape `16/32 attack roles = 50%` vs report's own seat tally → **no role tally in the report**; dispatch registry shows 14/32 (M3).
4. `git ls-files --others --exclude-standard` → 2 round-72 w1 seat files + round-73 pre-freeze drafts untracked (M7).
