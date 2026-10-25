# ScribeMistakes — round 74, wave 1 (kotodama, hyaku run 7)

Seat: `ScribeMistakes` (leaf). Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`. Drafted 2026-10-25.
Wrote only: `.ufo/waves/round-74/drafts/mistakes.md` (new; sha256 `fbd87865c82c15d23dc7dfa40d3266d5a810d88a94fb7f8912f5249f959b5370`, 31 lines, 1359 words) and this report. No fleet write, no claims/lesson/SCORECARD/LOG/QUALITY edit, no git index change, no installs, no live fetches, no `/tmp` scratch.

## Behavior

Drafted the lesson's `## Mistakes` section per `CORPUS.md` §"Rules added from the kaika campaign" — one row per mistake with `class · evidence pointer · captured-by · fix`, classes from the `.ufo/waves/kaika-w1/mistakes.md` §5 vocabulary, and each fix carrying a named red-before. Four rows, one per ticketed mistake:

| id | class | derivation |
|---|---|---|
| R74-M1 | `landing` | Six wave-2 seat files' post-push bytes never landed; the pushed tree holds five at older bytes and lacks the sixth. |
| R74-M2 | `landing` | Derived over the rejected alternative `vacuous`: the PASS was reproducible (`ExecRerunC.md:76,113`; `ExecRerunCa.md:91,105`), so the check could fail; what never landed is the receipt at the declared path (`reports/round-73/telemetry/`). |
| R74-M3 | `survivor` | Four channels passed the round-73 counters: junk landings (8/12 probes), graded-tree config, constant-printer ledger observes, SEPARABLE wider than the frozen sentence. |
| R74-M4 | `number-drift` | Prose `9 scenarios` vs the committed receipt's `SELFTEST OK: 10 scenarios`. |

Every row's state is `pending landing`; no fix is claimed landed and no red-before exists yet. The draft names the round's declared telemetry families for each red-before (`controls-ca.txt`; `junk-*.txt`; `selftest-c.txt`/`selftest-ca.txt`) and states each required observable (FAIL leg name at base, PASS at lands with the fix as the only delta).

Captured-by assignments: M1 `none` (PROTOCOL `landed means committed` binds the report; round-73 Ca's TRACKED leg listed round-72 files only); M2 `none` (QUALITY 23 binds the selftest verdict only; 17/19 pin a receipt's revision/run place, not its existence); M3 **QUALITY 11** (stand-in predicates; QUALITY 23's shipped selftest was blind to the class, `ExecSelftestAll.md:506,509-512`); M4 `none` (no rule compares a prose restatement with the receipt it restates).

## Gates exercised (all run at base over committed bytes)

| # | command | outcome |
|---|---|---|
| 1 | `git status --porcelain` (lane) | `M` ×5 (`.ufo/waves/round-73/w2/CritEntryAmendFinal.md`, `ExecSelftestAll.md`, `ScribeLogScorecard.md`, `SimplifierEntries.md`, `drafts/log-entry.md`) + `?? .ufo/waves/round-73/w2/RevengerOrigins.md` — reproduces `round-73-verifier-spotcheck.md:13` |
| 2 | per-file `git cat-file -e f7104cb:<path>` and `git show f7104cb:<path> \| sha256sum` vs `sha256sum <path>` | five present, worktree bytes differ (yes ×5); `RevengerOrigins.md` absent from the pushed tree |
| 3 | `git ls-tree --name-only f7104cb reports/round-73/telemetry/` | 13 files; no lands verdict receipt |
| 4 | `git grep 'ACCEPT-C-73: PASS\|ACCEPT-CA-73: PASS' f7104cb -- reports/round-73/telemetry/` | 0 lines both forms |
| 5 | `grep -n 'ACCEPT-C-73\|ACCEPT-CA-73' .ufo/waves/round-73/w2/{ExecRerunC,ExecRerunCa,CritAppendOnly}.md` | PASS only in seat reports: `ExecRerunC.md:76,113`; `ExecRerunCa.md:91,105`; `CritAppendOnly.md:153,162`; in-round flags `ExecRerunC.md:398` (m1), `ExecRerunCa.md:42` (F7) |
| 6 | `grep -o 'SELFTEST OK: [0-9]* scenarios' reports/round-73/telemetry/selftest-r3.txt` | `SELFTEST OK: 10 scenarios` (line 6) |
| 7 | `grep -c 'Ca 9 scenarios' LOG.md` / same on fleet report / `grep -c 'scenarios' SCORECARD.md` / `grep -c 'SELFTEST OK: 10 scenarios' SKILL.md` | 1 (`LOG.md:4297`) / 1 (fleet report `:10`) / **0** / 1 (`SKILL.md:704`) |
| 8 | `grep -n 'SEPARABLE' reports/round-73/claims.json` (worktree and `git show f7104cb:`) | line **173**; 171 is the APPENDONLY leg |
| 9 | `awk` pipe count on draft table rows | 7 delimiters per row, 8 raw on the M1 row (one escaped `\|` inside a code span) — table parses |

Not run (and not claimed): any round-74 counter (`reports/round-74/accept-c.py`, `accept-ca.py`, `ledger.json` do not exist at draft time), any round-73 counter re-run, any live fetch, any junk fixture.

## Findings for the round (reported, not edited)

1. **Claim Ca's "SCORECARD" attribution for the 9-scenarios pair is unverified.** `grep -c 'scenarios' SCORECARD.md` → 0 at base; the stale token lives in `LOG.md:4297` and the fleet report `.ufo/reports/round-73/kotodama.md:10`. The ledger pair must cite those two; a pair asserting SCORECARD would be red for the wrong reason (`claims.json` Ca before cell names "report/LOG/SCORECARD").
2. **The six leftover files are not uniformly "absent from the pushed tree"** (claim Ca before cell). Measured: five present at older bytes (worktree sha differs), one untracked. The pair's observe command must be "path untracked, or worktree bytes differ from `f7104cb`", not "absent".
3. **M2's fix has no declared red-before leg.** Claim Ca's after-state requires committed PASS-at-lands receipts, but its `do_nothing_control` and `--selftest` list name no receipt leg (they name stub-row, append-only removal, in-place-outside-allowed, shell-string/interpreter argv, constant-printer, min-pairs gate, config-edited-in-graded-tree). Under the CORPUS rule (*a fix is shown able to fail before it counts*) the freeze must add that leg, or M2 can never flip.
4. **Pointer drift in a cited seat report.** `CritAppendOnly.md:121` locates the frozen SEPARABLE text at `reports/round-73/claims.json:171`; measured at base, `:171` is the APPENDONLY leg and SEPARABLE is `:173`. The draft cites 173; the lesson should not copy the seat's 171.
5. **`RevengerOrigins.md` is substantive, not debris**: 25.4K, wave-2 falsify findings, and it independently records the uncommitted-corrections state it was itself a symptom of. Spot-check item 1's "commit or discard" should resolve as *commit*.

## Touched surfaces

- Written: `.ufo/waves/round-74/drafts/mistakes.md` (created the `drafts/` directory), `.ufo/waves/round-74/w1/ScribeMistakes.md` (this report).
- Read-only: lane committed bytes at `f7104cb` and the worktree; round-73 wave-2 reports; `corpus/QUALITY.md`, `corpus/lessons/round-73*.md`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `reports/round-74/claims.json`; `/home/vgpnk/Projects/shokunin/{CORPUS.md,PROTOCOL.md,.ufo/reports/round-73/kotodama.md,.ufo/waves/kaika-w1/mistakes.md}`.

## Out of scope (untouched)

- `reports/round-74/claims.json` (no edit; findings 1-3 are for the L1/ExecLedger), `reports/round-74/ledger.json` (does not exist), both round-74 counters, `corpus/lessons/round-74.md` (does not exist yet), QUALITY 25 draft (sibling seat), SCORECARD/LOG/QUALITY/SKILL/SOURCES/knowledge/lessons bytes, the six inherited round-73 wave-2 files, fleet root, sibling lanes, jj/git state.
