# ReviewShonenScorecard — round 53 calibration count (SHONEN + SCORECARD r51/r52)

Assigned item: calibrate every checkable assertion in `SHONEN.md` and the round-51 and
round-52 sections of `SCORECARD.md` (from line 1006) against observed state at the lane
worktree; output a mismatch table and the count; draft the appended correction for routed
defect 3 (`corpus/lessons/round-52-verifier-spotcheck.md:138-140`). Author-lane advice,
never admission. No file written except this report. Tools installed: none. No LSP server
answers `.md` here; every check below is a re-measurement (awk/counter commands, read-only
git, two scratch runs in a `/tmp` clone), not semantic-server output.

**Mismatch count: 4** — 1 real filing error (M2, the routed defect), 3 stale-against-worktree
values (M1, M3, M4), each true at its own measurement commit and drifted by the round-53
prerequisite `9ae5af9` (adds SOURCES rows S184 mined, S185 queued, S186 queued; re-cites
speech-surrogates line 104 to S184).

## Table A — mismatches

| # | Assertion (file:line) | Observed | Command |
|---|---|---|---|
| M1 | `SHONEN.md:6` — "sources registered in `corpus/SOURCES.md` (**183 rows** after round 52 — **142 mined, 33 queued, 8 rejected** …)" | At the round-52 close (`2eb489fb`) exactly 183 / 142 / 33 / 8 — as filed. At today's worktree: **186 rows — 143 mined, 35 queued, 8 rejected** (S184 mined; S185, S186 queued; prereq `9ae5af9`). Stale, not wrong. | `awk -F'\|' '/^\| S[0-9]/{s=$9; gsub(/ /,"",s); c[s]++} END{for(k in c) print k, c[k]}' corpus/SOURCES.md` → 143/35/8, rows 186; same on `git show 2eb489fb:corpus/SOURCES.md` → 183/142/33/8 |
| M2 | `SCORECARD.md:1017` — round-51 frontier "(**S071–S122 mined**, S123–S125 and S127–S131 queued, S126 mined)" — the routed defect 3 | At the round-51 tip `2b956d7`, **S081 is `queued`**, so S071–S131 = **52 mined, 9 queued** (queued: S081, S123–S125, S127–S131; mined: S071–S122 *minus S081*, plus S126). The stale line and the S081 flip landed in the *same* records commit `10f433c` (its message lists both "S081 status change" and "SCORECARD"). Correction text drafted below. | `git show 2b956d7:corpus/SOURCES.md \| awk -F'\|' '/^\| S(07[1-9]\|08[0-9]\|09[0-9]\|1[0-2][0-9]\|130\|131)/{s=$9; gsub(/ /,"",s); c[s]++} END{for(k in c) print k, c[k]}'` → mined 52, queued 9; `git log --format='%h %s' -n 1 10f433c` |
| M3 | `SCORECARD.md:1028` — r52 coverage row "C acceptance exit 0 (**49 cited S-ids**, all S134 or above, each with the entry in `used-by`)" | True as measured at `7cee23b` (receipt `reports/round-52/telemetry/final-measures.txt`: `C_SID_BAD 0 [] cited 49`). At today's worktree the entry cites **50** distinct S-ids, lowest S134 — prereq `9ae5af9` re-cited line 104 to S184 — and all 50 rows exist with the entry in `used-by`, so the row's *quality* clauses still hold; only the count is stale. | awk distinct-cited/used-by join over `corpus/SOURCES.md` + `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` → `distinct_cited 50 lowest_id S134 problems 0` |
| M4 | `SCORECARD.md:1030` — r52 frontier "`corpus/SOURCES.md` **131 → 183 rows** (S132 rejected, S133 queued, S134–S183 opened this round with S178 rejected)" | 131 → 183 true at `2eb489fb`; at the worktree **186 rows** (M1's cause). Status clauses verify at head: S132 `rejected`, S133 `queued`, S178 `rejected`; S134–S183 = 49 mined + S178 rejected = 50. | rows+split at head and at `2eb489fb`; `awk` status of S132/S133/S178 and S134–S183 range |

## Table B — assertions verified green (assertion → observed → command, condensed)

1. `SHONEN.md:5-6` — `SKILL.md:20` Decision table, `:468` Error patterns, `:522` Checklist → headings at exactly 20 / 468 / 522 (`grep -n '^## (Decision table|Error patterns|Checklist)' SKILL.md`).
2. `SHONEN.md:6` — "census exit 0 in `reports/round-52/telemetry/final-measures.txt`" → receipt ends `kotodama ok … exit 0` (file read).
3. `SHONEN.md:6` — "S094 rejected via S132" → S094 `rejected`, S132 `rejected` at head (awk $9, header `corpus/SOURCES.md:28`).
4. `SHONEN.md:8` — corrected split "52 mined, 9 queued at `2b956d7`: S081, S123–S125 and S127–S131 queued" → measured 52/9 at `2b956d7`; the 9 queued ids confirmed.
5. `SHONEN.md:8` — "the build wave admitted 54" → `da31d3c` = 124 rows = 70 + 54; "the falsify wave added S125–S131" → 124 → 131; S081 still `mined` at `da31d3c`, flipped by `10f433c` (S081 at `364eeff` = mined, at `2b956d7` = queued; change log `corpus/lessons/round-51.md:127`).
6. `SHONEN.md:8` — receipts `reports/round-51/telemetry/{declaration-dry-run,final-measures}.txt` exist; LOG round-51 entry at `LOG.md:4040`; receipt header pins `worktree=364eeff`.
7. `SHONEN.md:10` — commits `1923bfe`, `4ad2683` exist, type commit. The "re-run in fresh clones" process clause was not re-executed (historical; artifacts only).
8. `SHONEN.md:12` — sign entry §15 hands canon to lore (`sign-languages-manual-modality.md:222-224`); §2 one-owner boundary table with 14 one-way neighbour rows (`:31-50`); `.ufo/waves/round-51/build/ConnectSiblingSign.md` :17 "No sibling lane owns or partly owns any part of claim C's scope", unowned signed web accessibility named at :70 and :92; 0 `*sign-lang*` files at `bff83ba`.
9. Every cited hash is type `commit` (20 checked): `bff83ba 1f97472 35f0d49 e6b6629 da31d3c 364eeff 9feb69e 1923bfe 4ad2683 2b956d7 147cfde d9f73c8 dea5ece 5b7ecfb 7cee23b 2eb489fb c3297ff 6524184 9ae5af9… a9cf95f…` (`git cat-file -t` loop).
10. `SCORECARD.md:1008` — r51 preamble: all six hashes exist; receipts exist; "build 36 seats, falsify 41; round total 77" → dispatch `counts.spawn` 36/41; on disk 36 + 41 report `.md` files.
11. r51 depth row (`:1010`) — `rows=15 resolved=15 distinct=15` exit 0 at `364eeff` (clone) and at head; before-value `rows=11 resolved=11 distinct=11` exit 0 (bff83ba entry transplanted into the 364eeff scratch clone). Evidence files `ReviewDRow{Celestial,Numerals,Symbolism,Ritual}.md`, `RerunDCounter.md`, `CriticDRepairScope.md` exist.
12. r51 coverage row (`:1011`) — 226 → 227, linguistics 25 → 26 (`git ls-tree -r` counts at `bff83ba`/`364eeff`); sweep at `364eeff`: `rows 227 files 227`, `missing_from_index 0`, exit 0, footer total 227 (scratch clone run).
13. r51 calibration row (`:1012`) — separability self-application **0 findings, exit 0 at `9feb69e` and at `364eeff`**, both reproduced in the scratch clone (`SEPARABILITY: 0 findings`). R51-M1, R51-M5 exist (`corpus/lessons/round-51.md:100,134`). At head the same command exits 1 (manifest's C leg still expects 227 files) — expected point-in-time behavior, matches the row's scoping.
14. r51 frontier (`:1017`) — `70 → 131` rows (`bff83ba` 70; `364eeff`/`2b956d7` 131); census exit 0 in r51 receipt.
15. `SCORECARD.md:1021` — r52 preamble: `147cfde d9f73c8 dea5ece 5b7ecfb 7cee23b` all commit; both r52 receipts exist; "one build wave of 35 seats" → `counts.total` 35; no `falsify/` dir under `.ufo/waves/round-52/`.
16. r52 depth row (`:1022`) — S094 lines 5 at `147cfde` → 0 at head (awk); evidence `ReviewDLines.md`, `CriticClaimD.md` exist.
17. r52 coverage row (`:1023`) — 227 → 228, linguistics 26 → 27 (`ls-tree` at `147cfde`/`2eb489fb`); sweep at head: `rows 228 files 228`, `missing_from_index 0`, `totals_ok True`, exit 0; every cited id ≥ S134 with the entry in `used-by` (M3's join, problems 0).
18. r52 calibration row (`:1024`) — QUALITY criterion 10 exists (`corpus/QUALITY.md:37`); checker shown able to fail (`prereq-access-check.txt` committed, receipt quotes 6 findings / exit 1 at base, 2 flagged rows / 0 findings after); seat findings M1, M2 exist (`.ufo/waves/round-52/build/ReviewShonenScorecard.md:34-35`); R52-M1..M3 at `corpus/lessons/round-52.md:137-139`.
19. r52 frontier (`:1030`) — 131 → 183 at `2eb489fb`; S132/S133/S178 statuses as stated; census exit 0 in receipt.
20. "No non-author verifier on record" (all four SHONEN boxes) — still true; both SCORECARD sections say "pending non-author closure" and name none.

## Routed defect 3 — drafted appended correction (paste after `SCORECARD.md:1017`; the filed line is not rewritten)

```markdown
> **Correction (appended round 53, 2026-10-22; round-52 closure routed defect 3,
> `corpus/lessons/round-52-verifier-spotcheck.md:138-140`).** The frontier line above was
> filed in the round-51 records commit `10f433c` — the same commit that flipped S081
> `mined → queued` (status change log, `corpus/lessons/round-51.md:127`) — and was not
> updated to match. At the round-51 tip `2b956d7` the observed split for S071–S131 is
> **52 mined, 9 queued**: the mined set is S071–S122 *minus S081*, plus S126; the queued
> set is S081, S123–S125 and S127–S131. Re-measure:
> `git show 2b956d7:corpus/SOURCES.md | awk -F'|' '/^\| S(07[1-9]|08[0-9]|09[0-9]|1[0-2][0-9]|130|131)/{s=$9; gsub(/ /,"",s); c[s]++} END{for(k in c) print k, c[k]}'`
> → mined 52, queued 9. The filed line stays as filed; this note is the correction, and
> `SHONEN.md:8` already carries the corrected split.
```

## Residual risk and verification gaps

- **Round-52 wave: 35 dispatched, 34 reports.** `.ufo/waves/round-52/build/` holds 34 report `.md` files; the seat `ScribeSec02Boundary` has no report file anywhere (`residual/` is empty). No SCORECARD/SHONEN assertion depends on the report count (both cite the dispatch total 35, which verifies), but one seat's output is unaccounted for.
- **Process clauses verified via artifacts only**: "the build wave admitted 54" and "counting commands re-run in fresh clones of `1923bfe` and `4ad2683`" are corroborated by committed state (`da31d3c` row count; hash existence), not by re-executing the historical process.
- **Round-51 receipt ends red by design**: `reports/round-51/telemetry/final-measures.txt` last line is `MISSING_FROM_RECEIPT ['D', 'C']` (criterion-9 two-way check as filed). Disclosed in `corpus/lessons/round-51.md:129` and R51-M5; SCORECARD/SHONEN never assert that receipt is clean, but SHONEN:8 cites the file — a reader should see its last line.
- **Not re-observed at base**: the "0 topic-line owners" halves of the r51/r52 gap claims (filename half verified at `bff83ba`: 0 hits); the r51 falsify seats' individual re-openings.
- `git archive`-based reproduction of the r51 separability run exits 2 outside a git repo; the `/tmp` shared-clone runs (exit 0 at both commits) are the authoritative reproduction used above. Scratch clone left at `/tmp/k53cal` (no lane or fleet file touched).
