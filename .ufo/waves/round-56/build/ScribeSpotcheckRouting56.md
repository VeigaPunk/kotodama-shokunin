# ScribeSpotcheckRouting56 — round-55 outside check routed into round 56

Scope: read `corpus/lessons/round-55-verifier-spotcheck.md` in full and route §5 items 1-6, the §2 Gaps note and the §6 SHONEN note into the round-56 lesson, one route per row, with the lane evidence I could check without running an acceptance command. No lane file was edited; no git or jj write ran; no subagent was dispatched; no background job started.

Axis (godspeed): calibration. This seat's whole output is the intake table — the place where a closure's findings acquire an owner and a landing form. Coverage and operability appear only because two routes land in them: claim O's checker and the registry corrections below S359.

Read at 2026-10-22T21:31Z. Lane HEAD `456f5adc021346e7e9e7ce17a50d4bb1d208abbc`; declaration `b4b7db91a38447bb2c07b0ef436fc9654dcec89c`; `reports/round-56/claims.json` `base` is `045f458ceaa35d40baa7c56727c346d60ae210bf`. Lineage by read-only `git log`: `052f145` instruments, `045f458` revised instruments, `b4b7db9` declaration, `456f5ad` pre-dispatch receipts. The wave context calls `052f145` the claim base; `claims.json` calls `045f458` the base. Both are ancestors of HEAD.

## Draft for `corpus/lessons/round-56.md`

The block below is paste-ready. Its Route cells stay inside the six allowed values; item 4's cell names the three review seats that split the eight rows, and each of them is a `routed fix, seat` route.

```markdown
## Spot-check intake (round-55 outside verifier)

Drafted by ScribeSpotcheckRouting (`.ufo/waves/round-56/build/ScribeSpotcheckRouting56.md`) before the build seats reported; the status column is as the scribe found it at 2026-10-22T21:31Z (lane HEAD `456f5ad`), and a status is a route, not a verdict.

| Item (round-55-verifier-spotcheck.md:line) | Finding | Route | Status |
|---|---|---|---|
| `:119` (§5 item 1) | `reports/round-55/separability-manifest.json:14` declares C's export as `\bS(28[5-9]\|29[0-9]\|[3-9][0-9][0-9])\b`, whose three alternatives reach S285 to S358 and also S900 to S999, so the record-unit row S358 and the fixture ids S900 and S901 read as C's export and the declared separability command exits 1 at the landed tree (R55-M5) | this round's manifest (exact block) | done in the declaration: `reports/round-56/separability-manifest.json:9-11` reads `"\bS(359\|3[6-9][0-9]\|40[0-9]\|41[0-8])\b"`, O exports nothing, and `claims.json` `export_rule` says unused ids of the block stay unassigned. Boundary checked by hand on the two patterns: S358, S419, S900 and S951 do not match the new one, S359, S400 and S418 do; on the old pattern the tested S285, S357, S358, S900, S901 and S999 all match, and its alternatives cover S285-S358 and S900-S999 by construction |
| `:120` (§5 item 2) | the round-55 calibration row counts "mistakes R55-M1 to R55-M4" while `corpus/lessons/round-55.md:227-232` carries R55-M1 to R55-M6, and the capability and operability rows cite selftest 24/24 without the revision that measured it | routed fix, seat ScribeScorecardNits | routed, not landed: `SCORECARD.md:1070` still reads the M1-M4 count, `SCORECARD.md:55` reads `--selftest` (24/24) and names `454a2dc` only beside accept-o's exit 0, and `:1069` reads selftest 24/24 with no revision for it, while the round-55 tip `2935c47` measured 27/27 (spot-check §2 committed evidence). The landing form is an appended row, never an in-place edit (`:120`, and `SCORECARD.md:1062` opens the round-55 section the row would follow); seat report pending at `.ufo/waves/round-56/build/` |
| `:121` (§5 item 3) | `reports/round-55/telemetry/final-measures.txt` and `declaration-dry-run.txt` carry a timestamp but no commit hash, so a verdict cannot name the revision it measured | revision-naming dry-run (reports/round-56/dry-run.py) | landed in the instrument: `reports/round-56/dry-run.py:7` documents the required `# measured-revision <full hash>` line, `:37` is the pattern, `:66` resolves the revision, `:80` prints the line, and `check` (`:100-108`) returns 1 when no revision line is found. The declared receipt already carries it: `reports/round-56/telemetry/declaration-dry-run.txt:2`. Both round-55 files hold zero such lines (`grep -c measured-revision` returns 0 for each) |
| `:122` (§5 item 4) | eight rows still have no row-level non-author re-open: S290, S292, S293, S306, S307, S320, S323 and S356; the closure re-opened only S291, S294, S305, S308, S309, S321, S322, S324, S355, S357 and S358 | routed fix, seat ReviewRowsS290to293, ReviewRowsS306S307, ReviewRowsS320S323S356 | routed, not landed: the three prompts name exactly S290/S292/S293, S306/S307 and S320/S323/S356, each asking for a verbatim ordinary-means re-open, the 25-word cap, the locator, the tier for scope, and the citing sentences in `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md`. Reports pending; `.ufo/waves/round-56/build/` held only `swarm-registry.json` and `ConnectLoreHandoff.md` at read time. `corpus/lessons/round-55.md:241` carries the cancelled slices as a class, not these eight rows, so this lesson is the first committed place that can name them |
| `:123` (§5 item 5) | the S309 row records the Princeton book page as reachable, but it answered HTTP 403 (Cloudflare) to plain curl on 2026-10-22 while the linked PDF answered 200 | routed fix, seat ReviewS309Access | routed, not landed: `corpus/SOURCES.md:338` (S309) still reads inside its citation cell "direct, HTTP 200 for both the book page and the 265 KB PDF, read 2026-10-22", and the seat is asked for the exact old -> new note (challenge met, not passed; the quotes come from the PDF) plus a verbatim check of the Gate quote. The cell edit is a registry fix below S359, so it lands in the records commit after C and must keep C's ACCESS leg and the census green (`claims.json` `records_not_claims`) |
| `:124` (§5 item 6) | six Gate Grounds carry HTML entities where the registry `teaches` cell carries decoded marks, and the checker's whole-teaches comparison does not decode them | claim O | in progress: `tools/check-gate-quotes.py` at HEAD `456f5ad` has no `html.unescape` (a grep for `unescape` or `html` returns nothing), so the class is unbuilt until O lands. `reports/round-56/accept-o.py:74-76` pins the 16 (line, S-id) html-entity pairs and its ENTITY leg requires each exactly once, with NOFALSE keeping other classes out of the round-55 run. The 16 erratum lines and the six-cell proof are seat ScribeErrataEntities55's; the six are S288, S305, S326, S341, S343 and S348, which `corpus/lessons/round-55-verifier-spotcheck.md:107` says become equal to their registry cells under `html.unescape` |
| `:60` (§2 Gaps) | the round-55 receipt files do not name the revision they measured and identify it only as "lane worktree after falsify fixes" and "pre-landing" | revision-naming dry-run (reports/round-56/dry-run.py) | same defect as `:121`, no separate work: this round's receipt pairs the prose line with `# measured-revision` (`reports/round-56/telemetry/declaration-dry-run.txt:1-2`), and the `check` mode fails any receipt that lacks the line |
| `:128` (§6 SHONEN note) | all four boxes stay `[~]`; the closure exercised no end-to-end reviewer execution for boxes 2 and 3 and does not recommend promotion | not routed: operator-owned | recorded, no lane action: promotion belongs to the operator, and this lesson keeps the four boxes at `[~]` unless the operator changes them. The confirmation the closure did make is box 1's counts (358 rows; 313/35/10) by non-author measurement |

### Items that need the L1

1. Hold C's export at the declared block `\bS(359|3[6-9][0-9]|40[0-9]|41[0-8])\b` through the declaration; if the entry's id set changes, re-declare the block, never widen it (R55-M5: the old pattern reached S999 and swept in the record-unit row S358 and the fixtures S900/S901).
2. Append the SCORECARD correction rows that ScribeScorecardNits drafts — the calibration row's mistake count (R55-M1 to R55-M6, not M1 to M4) and the selftest 24/24 attribution (24/24 at `454a2dc`, 27/27 at the tip `2935c47`) — as a new row, not as an edit of `SCORECARD.md:55`, `:1069` or `:1070`.
3. Keep `# measured-revision <40-hex>` on every round-56 receipt, including any hand-written final-measures style file; `reports/round-56/dry-run.py check` refuses a receipt without it.
4. Name the eight un-reviewed rows (S290, S292, S293, S306, S307, S320, S323, S356) in this lesson's Frontier until the three review seats report, then record each verdict and any old -> new fix; registry corrections below S359 land after C in the records commit.
5. Land the S309 access-path correction from ReviewS309Access in the row's citation or recheck cell, recording the 403 on the book page and the 200 on the PDF as "challenge met, not passed", and keep C's ACCESS leg and the census green.
6. Land O's checker from ExecGateEntity and file the 16 entity erratum lines from ScribeErrataEntities55; O passes only when all eight legs pass at the landed tip, ENTITY reporting the 16 pairs once each and NOFALSE staying clean.
7. Keep all four SHONEN boxes at `[~]`; the operator alone promotes them, and this spot-check does not recommend promotion.
```

## Gates I ran, and what they showed

- `nl -ba corpus/lessons/round-55-verifier-spotcheck.md`: §5 items at `:119`-`:124`, the Gaps note at `:60`, the six-cell mechanical check at `:107`, the SHONEN note at `:128`. These are the locators in the table.
- Pattern test in `python3` over the two export regexes verbatim from the manifests: old pattern matches S285, S357, S358, S900, S901, S999; new pattern matches S359, S400, S418 only, and none of S358, S419, S900, S951. This is my own check of the declared bound, not an acceptance run.
- `grep -n exports -A2 reports/round-55/separability-manifest.json` → `:14` holds the too-broad pattern; `cat reports/round-56/separability-manifest.json` → C's `exports` at lines 9-11 is the exact block, O's is empty, and the REC unit carries none.
- `grep -c measured-revision` on `reports/round-55/telemetry/final-measures.txt` and `declaration-dry-run.txt` → 0 and 0; `sed -n 1,6p` on each shows a timestamp line and no hash.
- `sed -n 1,3p reports/round-56/telemetry/declaration-dry-run.txt` → line 2 is `# measured-revision b4b7db91a38447bb2c07b0ef436fc9654dcec89c (sandbox clone ...)`.
- `grep -n "measured-revision\|REVLINE\|rev-parse" reports/round-56/dry-run.py` → lines 7, 18, 22, 37, 66, 80, 106; reading `check` shows `return 1 if missing or extra or not revisions else 0`.
- `grep -n "R55-M" SCORECARD.md corpus/lessons/round-55.md` → `SCORECARD.md:1070` says M1-M4, the lesson's mistake table at `:227`-`:232` has six rows, `SCORECARD.md:55` and `:1069` cite 24/24.
- `grep -n "unescape\|html" tools/check-gate-quotes.py` → no output at HEAD, so the current checker does not decode.
- Token scan of the 16 Gate lines of `corpus/lessons/round-55.md` (72, 82, 88, 89, 93, 96, 110, 113, 125, 127, 131, 132, 134, 138, 140, 141): every line carries at least one `&...;` token; line 140 (S356) carries the numeric references for the opening and closing double quote, the rest carry named references such as the quote entity and the ampersand entity.
- `grep -n "^| S309 " corpus/SOURCES.md` → the row is `:338`; its citation cell contains "direct, HTTP 200 for both the book page and the 265 KB PDF, read 2026-10-22".
- `grep -n "Row slices S290" corpus/lessons/round-55.md` → `:241`, a class-level bullet, no ids.
- Read-only `git status --porcelain` at the lane → only the untracked `.ufo/waves/round-56/` build files; read-only `git log --oneline -4` → the four commits named in the header.
- `.ufo/waves/round-56/build/` listing at 2026-10-22T21:31Z → `swarm-registry.json` and `ConnectLoreHandoff.md` only, so every routed seat's report is pending.

Result: the intake draft above is ready to paste; the eight rows carry one route each and point at real lane bytes. No acceptance command was run, so nothing here upgrades a route into a landed or passing state.

## Touched surfaces

- Wrote this file only: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScribeSpotcheckRouting56.md`.
- No other lane file created, edited or deleted; nothing written under `/home/vgpnk/Projects/shokunin/.ufo` or the fleet root; no scratch clone needed; no tool installed or upgraded.

## Out of scope, not run

- `python3 -B reports/round-56/accept-c.py`, `reports/round-56/accept-o.py`, `claims-agree.py`, `tools/check-claim-separability.py`, `reports/round-56/dry-run.py check`, and `scripts/sources-census.sh`: these are the L1's and the falsify wave's gates, and a scribe run would not be evidence.
- No external source was re-opened. The row verdicts belong to the three review seats and to ScribeErrataEntities55; the closure already re-opened its eleven.
- Did not read `corpus/lessons/round-56.md`, because it does not exist yet (checked); the L1 creates it.

## Findings for the L1

1. Item 1's risk is a later widening, not the current bytes. The declaration and the manifest already carry the exact block, and my pattern test shows S358 and S900 fall outside it; a re-widened export would read a record-unit row and O's fixtures as C's again. The lesson row should stay worded as a rule, because there is nothing left to fix.
2. Item 6 is two halves with different owners. O owns decoding and reporting in `tools/check-gate-quotes.py`; the six Grounds need no registry edit, because `:107` states they equal their `teaches` cells once unescaped, and the entity-bearing text sits in the already filed round-55 Gate lines, which are not rewritten (round-54 precedent). The fix for that half is lesson text: 16 erratum lines with the decoded reading.
3. Item 4's carry has no committed artifact yet. `corpus/lessons/round-55.md:241` names the slices, not the eight rows; the ids exist only in the spot-check. If the round-56 Frontier omits them, the carry survives only in shipped reports.
4. Item 5's correction is a registry cell below S359, so under `claims.json` `records_not_claims` it lands after C and must keep C's ACCESS leg and the census green; the old -> new text belongs in the lesson's registry-fix log.
5. Lineage wording, not a defect: the wave context's claim base string (`052f145`) and `claims.json`'s `base` (`045f458`) are different commits, one instruments revision apart, and both are ancestors of HEAD `456f5ad`. The lesson's header should cite `claims.json`'s value for the base and name `052f145` as the first instruments commit.
6. The round-55 receipts' missing revision line (`:121`) and the Gaps note (`:60`) are one defect written twice. The round-56 receipt shows the fix in use, so the lesson can mark `:60` as satisfied by the instrument rather than opening a second action.

Artifact: `.ufo/waves/round-56/build/ScribeSpotcheckRouting56.md` (this file).
