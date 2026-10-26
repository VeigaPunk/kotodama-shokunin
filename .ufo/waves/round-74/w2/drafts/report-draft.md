# kotodama round 74 — worldbuilding-setting-practice assimilation + calibration ledger

Lane: kotodama-shokunin · base `f7104cbce186bc2e1522abf0cfd619cc834628bb` · lane main / HEAD
`1d7add3f7b9eaf6f3349c56c36f6d06325d74236` (`git ls-remote origin refs/heads/main` prints the same) · 2026-10-25,
hyaku run 7, L1 KotodamaR74, attempt 1. Round shape: two v1 waves — w1 42 seats + w2 44 seats = 86 seats (policy
v1, band 32–64 per wave; `.ufo/waves/round-74/w1/w1-results.json` `seats` = 42, `.ufo/waves/round-74/w2/dispatch.json`
`counts.total` = 44). Planner seat = the L1.

## Work performed

Declared claims (2, frozen pre-data at `reports/round-74/claims.json`, operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`): **C** (coverage, assimilation-sourced — shokuknow
`merge/kotodama` worldbuilding-setting-practice theme: four rows mined, one row reused in place, two entries) and
**Ca** (calibration, records — a 13-pair self-assessment-vs-repo ledger over the round-73 routed counter defects).
Lowest-axis obligation: `SCORECARD.md` holds no numeric scores (SCORECARD.md:13-15) and freshness axis-move claims
stay paused under the open L0 row `kotodama | round-11` (`.ufo/l0-questions.md:47`); no nudge waiver is claimed.
Sixteen `pre_data_corrections` (F1/F2/F3-F4/F5/F6-F19/F7/F8-F10/F11-F12/F13/F14/F15-F17/F16-F18/A1/A2/A3/E1) are
recorded in `claims.json` and applied before data.

- **Wave 1 (42 seats)** — 12 scout, 10 executor, 6 scribe, 6 critic, 3 reviewer, 2 connector, 1 mutation-tester,
  1 sentinel, 1 simplifier (`w1/w1-results.json` role tally). All 42 report files exist under
  `.ufo/waves/round-74/w1/` (44 `*.md` there = 42 reports + the two `*.postwave.md` relocation files); dead seats:
  none. The wave re-opened all five documents live, drafted the two entries, the four registry rows and the S877
  cell change, the README index rows and footer, the lesson, QUALITY 25 and the SKILL gate rows, built both
  counters plus the junk-fixture generator, and attacked the draft claims. Evidence pointer:
  `.ufo/waves/round-74/w1/` (per-seat reports; scouts carry the fetch lines, UA and sha256).
- **Freeze chain** — `de93d91` (first freeze: claims, ledger, both counters, control inputs, six inherited round-73
  w2 files, wave-1 evidence) → `3595c919` (ledger tokens normalized, LC-01 annotated, LC-09 de-pinned, Ca counter
  patched) → `00c408a` (operative freeze: Ca counter redacts lane ids and family literals from its own output; adds
  the empty-tree pin exemption). Three freezes, not one, are disclosed as R74-M9 in `corpus/lessons/round-74.md`.
  Selftest receipts at the operative freeze: `SELFTEST: 69/69 scenarios` (`telemetry/selftest-c.txt`) and
  `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0` (`telemetry/selftest-ca.txt`).
- **Claim Ca landing `5e4796c`** — `SCORECARD.md` `## Corrections — round 74` (12 ANNOTATE rows, +19 lines, zero
  removed), the one REPAIR pair LC-09 (`SKILL.md:594` civilizations `94`→`95`), the six inherited round-73 w2 files
  tracked with pinned blob ids, `SKILL.md` gate rows for both round-74 counters plus a three-part correction note
  for the round-73 rows, QUALITY 25, and the do-nothing/junk control inputs. Round-73 counters re-executed at their
  own lands `2d1cd914`: `ACCEPT-C-73: PASS legs=11/11`, `ACCEPT-CA-73: PASS legs=9/9`
  (`telemetry/accept-c-73-at-lands.txt`, `accept-ca-73-at-lands.txt`).
- **Claim C landing `d7a3840`, fixes `c4bf61a`** — entries
  `corpus/knowledge/culture-material/worldbuilding-setting-practice.md` (267 lines) and
  `.amend-2026-10-23.md` (91 lines), registry rows S881–S884 (804 → 808), S877's `used-by` cell in place,
  `corpus/README.md` index rows + round-74 landing block + `Counts checked` footer (247 → 249 files),
  `corpus/lessons/round-74.md` (211 lines, zero removed), `telemetry/census-end.txt`. The `c4bf61a` fix pass cleared
  the entry header template tokens and the lesson counts sentence.
- **Controls and receipts `1d7add3`** — junk-landing receipts `telemetry/junk-c.txt` (J1, J2, J3, J9) and
  `telemetry/junk-ca.txt` (J4, J4b, J5, J6, J7, J8, J9); round-74 counters reject every one, and the round-73
  survivors J3, J4b, J5, J6, J7 are carried as the measured red-before. The same commit adds the measured receipts
  at each claim's own landing (`measures-c.txt` stamped `c4bf61a`, `measures-ca.txt` stamped `5e4796c`).
- **Wave 2 (44 seats)** — 9 critic, 8 reviewer, 8 executor, 6 scout, 6 mutation-tester, 2 connector, 2 scribe,
  1 simplifier, 1 revenger, 1 sentinel. At drafting time 18 of 44 reports are written (`CritAppendOnly`,
  `CritFactAmend1`, `CritFactAmend2`, `CritScopeProvince`, `CritTrendFinal`, `ExecCensusEnd`, `ExecWaveLedger`,
  `RevEntryAmendFinal`, `RevFrozenChain`, `RevQuality25`, `RevReadmeIndex`, `ScoutRejectProbes`,
  `ScoutReopenS877`/`S881`/`S882`/`S883`/`S884`, `ScribeLogScorecard`). What they establish so far: census and freeze
  chronology survive their attacks (`ExecCensusEnd` F1/F2 are MEDIUM/LOW and the census PASS reproduces against a
  planted control; `RevFrozenChain` Q4 — `claims.json`/`ledger.json` byte-identical at freeze, both lands and main —
  passes, and both counters reproduce their PASS lines in its own clone); the surviving defects are the QUALITY 25
  blockers below, the ledger's unlanded SHONEN repair, the frozen control prose, and per-entry content errors
  (amendment `gap filled:`/scope/reader sentences, README index order and the "0 registry rows" claim, the S895/S899/
  S900 reject reasons). The other 26 seats are `W2-PENDING:<seat>`; the registry
  `.ufo/waves/round-74/w2/swarm-registry.json` is the record.
- **Evidence pointers** — `corpus/lessons/round-74.md` (`## Gate`, `## Quarantine`, `## Mistakes` R74-M1..R74-M10,
  `## Frontier-step`, `## Routed to round 75`), `reports/round-74/` (claims, ledger, both counters,
  `telemetry/`, `evidence/`), `.ufo/waves/round-74/w1/`, `w2/`, `assimilation/`.

## Landed changes

Each landing is tied to the round-74 `LOG.md` entry **draft** — `.ufo/waves/round-74/w2/drafts/log-entry.md`
(`ScribeLogScorecard`) — and to its commit. **`LOG.md` is not yet appended at main**:
`git log --oneline f7104cb..main -- LOG.md` prints nothing, so a `LOG.md:NNNN` pointer cannot be filed until L1
appends the draft. `W2-PENDING:ScribeLogScorecard` (draft written; append is the L1's).

| commit | what landed | LOG entry bullet |
|---|---|---|
| `de93d91` | claims, ledger, both counters, control inputs, six inherited round-73 w2 files, wave-1 evidence | Freeze |
| `3595c919` | ledger token normalization, LC-01 annotation, LC-09 de-pin, Ca counter patch | Freeze |
| `00c408a` | operative freeze: counter redaction, empty-tree pin exemption | Freeze |
| `5e4796c` | SCORECARD `## Corrections — round 74`, SKILL gate rows + LC-09 repair, QUALITY 25, round-73 PASS receipts | Claim Ca — landing |
| `d7a3840` | two entries, rows S881–S884, S877 `used-by`, README index/footer, lesson, census-end | Claim C — landing |
| `c4bf61a` | entry header template tokens, lesson counts sentence | Claim C — fixes |
| `1d7add3` | junk-landing receipts, measured receipts at each claim's own landing, wave-2 builder | Controls |

Lane pushed: `1d7add3f7b9eaf6f3349c56c36f6d06325d74236` (local `main`, worktree HEAD and `git ls-remote origin
refs/heads/main` agree).

## Before → after measurements

- **C** — before (base `f7104cb`): `git show f7104cb:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`
  = **804** rows (last id S880); `git show f7104cb:corpus/SOURCES.md | grep -cE 'litmemo\.com|tuduku\.space|chinawriter\.com\.cn'`
  = **0**; `git ls-tree -r --name-only f7104cb corpus/knowledge | grep -c '\.md$'` = **247**;
  `git ls-tree -r --name-only f7104cb corpus/knowledge | grep -ci 'worldbuilding-setting'` = **0**;
  `git grep -lE '設定ノート|世界観|世界观' f7104cb -- corpus/knowledge | wc -l` = **0**
  (`reports/round-74/telemetry/gap-sweep.txt` re-derives all five at the pinned tree).
  After (`c4bf61a`, re-measured at `1d7add3`): the same registry command at the lands tree = **808** rows;
  `find corpus/knowledge -type f -name '*.md' | wc -l` = **249**;
  `find corpus/knowledge -iname '*worldbuilding-setting*' | wc -l` = **2**. Counter:
  `python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin`
  → `ACCEPT-C-74: PASS legs=13/13` (exit 0; committed receipt `telemetry/measures-c.txt`, re-established by
  `ScribeLogScorecard` at the same lands, and by this seat at `1d7add3` → `PASS legs=13/13`, exit 0).
- **Ca** — before (base `f7104cb`): 13 ledger pairs, every one red (`BASEMISMATCH red=13 min=10`, ids
  LC-01/02/03/06/07/08/09/11/12/15/16/17/18); six round-73 w2 files unlanded (five tracked-but-modified plus
  `RevengerOrigins.md` untracked); `git grep -c -E '^ACCEPT-(C|CA)-73: PASS' f7104cb -- reports/round-73/telemetry`
  returns no line. After (`5e4796c`):
  `python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin`
  → `ACCEPT-CA-74: PASS legs=11/11` (exit 0; committed receipt `telemetry/measures-ca.txt` — `REPAIR green=['LC-09']`,
  `ANNOTATE rows=14 annotate-pairs=12 unannotated=0`, `TRACKED paths=6 problems=[]`, `RECEIPTS rev=2d1cd9140d3a
  receipts=['accept-c-73=50c60bb67f16','accept-ca-73=864c94192854']`, `STAMP stamped=evaluated=measured=5e4796c0cb6a`).
  Do-nothing controls: `lands == freeze` → `ACCEPT-C-74: FAIL legs=4/13` and `ACCEPT-CA-74: FAIL legs=7/11`;
  `lands == base` → refused, `FAIL legs=0/13` / `FAIL legs=0/11` (`telemetry/controls-c.txt`,
  `controls-ca.txt`).
- **Honest limits (measured, not inferred).**
  1. Claim Ca is green at its own landing only. At the round tip `1d7add3` the same command returns
     `ACCEPT-CA-74: FAIL legs=9/11`, `LEG FAIL APPENDONLY — problems=['corpus/SOURCES.md: changed lines outside
     REPAIR stated_at lines [832]']`: claim C's required in-place `used-by` edit on S877 is not a Ca REPAIR
     `stated_at` line, so the two frozen claims conflict in one tree. Disclosed verbatim in
     `telemetry/junk-ca.txt` (`# NOTE (L1, 2026-10-25)`) and left unamended — frozen claims stand.
  2. `QUALITY 25 (b)` is false for its own round on four counts (`RevQuality25` F1, BLOCKER): the freeze carries no
     `counters/junk-fixtures.py` — the generator lives at `.ufo/waves/round-74/counters/junk-fixtures.py`; `junk-c.txt`
     and `junk-ca.txt` are absent at `00c408a` (`git ls-tree -r --name-only 00c408a | grep -E 'round-74/telemetry/(junk|controls)'`
     lists only the two controls) and are added at `1d7add3`, after both claim landings; no single commit adds the six
     named artifacts (`de93d91` claims/ledger/counters/generator, `3595c91` the controls, `1d7add3` the junk receipts);
     and the receipts name generator sha256 `ce6505fc…` while the freeze's generator bytes hash to `d4789c39…`.
     `RevQuality25` F2 (BLOCKER) adds that J4 and J4b never fail on their named leg — they fail `FROZENCFG`, not
     `LEDGER` — and F3 that J6/J7 are not differential (their legs are already red in the clean reference landing T0).
  3. The frozen claims' `do_nothing_control` prose does not match the committed receipts: claim C names
     ENTRIES/ROWS/GATE/EVIDENCE/REJECTS/INDEX red while the receipt shows nine red (adds REPOINTED, CITEDLINES,
     SCRATCHMIRROR); claim Ca names REPAIR/ANNOTATE/RECEIPTS red while the receipt shows REPAIR/ANNOTATE/NOSTUB/
     SEPARABLE red and RECEIPTS green (`ScribeLogScorecard` F1, `RevFrozenChain` F2 — the latter HIGH). The C
     control's own numbers are right (`controls-c.txt`: `FAIL legs=4/13` at `--lands == --freeze == 00c408a`).
  4. The amendment's `gap filled:` line (`… does not say which part is built first, which part is derived from
     which …`) is contradicted by its own parent (`## §4 Build order`, parent line 72). No erratum is landed at
     `1d7add3` (`grep -n 'Erratum' corpus/knowledge/culture-material/worldbuilding-setting-practice*.md` → no
     match). Until the erratum lands and claim C is re-run and re-stamped, the quality trend cannot be filed
     `unchanged` (see Trend verdicts).
  5. The frozen Ca ledger carries normative repair residue for a repair that did not land (`CritAppendOnly` F1,
     HIGH): `ledger.json:99/737` and `repair_edits[LC-01]` say `SHONEN.md:6` is rewritten to "804 rows …", but
     `git diff --numstat base..main -- SHONEN.md` is empty and line 6 still reads "412 rows after round 56"; the
     same frozen APPENDONLY rule rejects that edit (`SHONEN.md: changed lines outside REPAIR stated_at lines [6]`).
     The pair's disposition is ANNOTATE, so no leg reads `repair_edits` and it survived grading.
  6. Counter-shape holes a caller can reach, both measured by wave-2 seats and neither claim-falsifying:
     `accept-c.py` returns `ACCEPT-C-74: PASS legs=13/13` when a landing commit is passed as its own `--freeze`
     (`RevQuality25` F4, HIGH — Ca refuses that shape, C has no guard), and the Ca `RECEIPTS` leg is
     materialization-prefix dependent (`RevFrozenChain` F1, HIGH: `normalize_receipt` masks only `/tmp` and `/var/tmp`
     paths, so the same bytes fail when the clone is materialized outside them). `RevQuality25` F5-F9 additionally
     record refusal-line, chain-check, `# frozen legs:` and receipt-enumeration deviations from the criterion text.
  7. The frozen status sentence "no seat has scored landed data" is unqualified and false under the plain git sense
     of "landed": the re-freeze that rewrote two claim legs and two ledger entries (`3595c91`) followed a seat's
     scoring of the landed first-freeze commit (`RevFrozenChain` F3, MEDIUM). Nothing in the claims makes the
     "frozen before any seat scored landed data" guard false where it is tested; the sentence needs the qualifier
     the claim itself uses ("landed data" = post-freeze claim data).
  8. Wave-1 attack share is 10/42 = 23.8%, below the prompt's own ≥25% floor and unrecorded in any landed byte
     (`ExecWaveLedger` F1, HIGH); its F3 (HIGH) adds that R74-M10's seat-name list is not the collision set (26 names
     collide, 2 of the 10 listed exist in no round-71..73 artifact).

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`:
exit 0 at start (**804** rows, `telemetry/census-start.txt`) and at end (**808** rows, `telemetry/census-end.txt`).
Row count command, both ends: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
(804 at `git show f7104cb:corpus/SOURCES.md`, 808 at main). Rows added: **4** — by tier **B ×1 (S883)** and
**C ×3 (S881, S882, S884)**; all mined, `opened 2026-10-25`, cadence-only recheck `180d`, 11 cells, map URL
verbatim in the source cell. Census warnings: W04 ×28 at both ends (standing duplicate-URL class) and W01 ×3 at the
end (S881, S882, S884 — the tier-C rows; status-neutral).
Rows touched old→new: **S877** only, `used-by` old
`corpus/knowledge/linguistics/conlang-scholarship.md` → new
`corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`,
every other cell byte-identical (recorded in the lesson, not in the row). Frontier ground entered:
**setting-practice**. Assimilation: **ADOPTED one theme** (worldbuilding-setting-practice, CJK practitioner craft:
two Japanese writing-app pages and two 中国作家网 pieces) with **two entries** and five rows touched (four appended,
S877 in place); triage 2 adopted / 4 path-present with differing bytes / 34 refused of the 40 staged files;
staged S882 not appended (existing row S877), staged S895's folded passage dropped, register S816/S817 stay REFUSED
as staged under the four clearing conditions. `considerthese`: **absent for this lane** (`ls considerthese` → no
such directory), so no proposal is mined and no ledger row is added. README carries the landed disclosures: the
`## culture-material/ (36)` heading is named stale (live directory 40 files, section 38 rows) and the two
`heritage-taxonomy` files are named unindexed rather than claimed closed.

## Trend verdicts

Per `CritTrendFinal` (wave-2, landed) against `LEARNING.md:33-35` and QUALITY 20:

- **expansion: improved** — 247 → 249 knowledge files, two entries on ground with 0 filename owners, 0 topic-line
  owners and 0 registry host hits at base, both entries carrying `source:` lines to mined rows
  (S877, S881–S884). Caveat: base + amendment is **one ground**, and the novelty sentence must be the narrowed one
  (*a second practitioner register adding disclosure timing and the premise→laws→ladder derivation*), not
  "fills gaps the parent lacks" (`CritTrendFinal` F1/F4/F5).
- **quality: unchanged — conditional.** `git diff --stat base..lands -- corpus/knowledge` is two additions, zero
  modifications: no existing entry re-verified, deepened or superseded. The condition: the amendment's falsified
  `gap filled:`/`ground:` sentences must be marked (an appended `## Erratum` naming the parent `## §4` and `:53`)
  and claim C re-run/re-stamped before filing; filed unmarked, LEARNING.md:34's "an entry is found false … and left
  unmarked" fires and quality is **harmed** — which with `expansion: improved` is a trade and "never admitted"
  (LEARNING.md:37-38).
- **discernment: unchanged at filing** — no outside spot-check of round 74 exists in any tree; QUALITY 25 is
  instrument-class and QUALITY 20's preamble bars instrument work from this observable. Flip condition: the
  non-author closure samples ≥1 admit and ≥1 evidence-based reject, records agree/disagree with reasons, and
  independently re-runs QUALITY 25's red-before; on agreement an appended erratum may move it to `improved`
  (`CritTrendFinal` F2/F3).

Instrument findings do not move these three verdicts — QUALITY 20 bars counter/record work from the quality and
discernment observables — but they are not optional repairs: the QUALITY 25 blockers (`RevQuality25` F1/F2), the
`accept-c.py` self-graded do-nothing shape (F4), the unlanded SHONEN repair in the frozen ledger
(`CritAppendOnly` F1), the frozen control prose (`RevFrozenChain` F2) and the reject-reason falsifications
(`ScoutRejectProbes` F1/F2/F4) all need a lesson or correction record, and the closure's QUALITY 25 re-run should
exercise the filed receipts, not the criterion's shape-only one-liner (which `RevQuality25` F8 shows passes a decoy).

## SHONEN

- [~] **Box 1 — SKILL.md decision tables, error patterns, checklist; sources registered.** `SKILL.md:20`
  (Decision table), `:505` (Error patterns), `:564` (Checklist); pointers corrected in round 73. `corpus/SOURCES.md`
  now holds **808** rows (census exit 0), while `SHONEN.md:6` still reads "412 rows after round 56" — carried as
  ANNOTATE pair LC-01 in `SCORECARD.md` `## Corrections — round 74` (old 412 → new 804, re-derivation
  `git grep -c -E '^. S[0-9]{3}' f7104cb -- corpus/SOURCES.md`), not repaired; the frozen Ca ledger nevertheless
  carries normative repair residue asserting that rewrite (`repair_edits[LC-01]`, `ledger.json:99/737`), which the
  frozen APPENDONLY rule would reject if executed (`CritAppendOnly` F1, HIGH — no leg reads `repair_edits`, so it
  survived). No non-author verifier on record.
- [~] **Box 2 — at least one end-to-end domain task executed and logged.** Four rows re-opened and mined plus S877
  reused; two entries landed (`d7a3840`, `c4bf61a`) with five committed evidence captures in
  `reports/round-74/evidence/` (fetch line, browser UA, HTTP 200, bytes, body sha256, window); wave-1 scouts carry
  the live re-opens, wave-2 `CritFactAmend1/2`, `RevEntryAmendFinal`, `ScoutReopenS877/S881–S884` carry the
  independent re-open and per-sentence checks; `W2-PENDING:CritFactBase1`, `W2-PENDING:CritFactBase2`,
  `W2-PENDING:RevEntryBaseFinal`. `LOG.md` entry is drafted (`w2/drafts/log-entry.md`) but not yet appended. No
  non-author verifier on record.
- [~] **Box 3 — instructions executable by an agent without oral context.** Both counters run from a fresh clone with
  committed commands and receipts (`ACCEPT-C-74: PASS legs=13/13` at `c4bf61a` and again at `1d7add3`;
  `ACCEPT-CA-74: PASS legs=11/11` at `5e4796c`); `ScribeLogScorecard` re-ran both at their own landings in a
  disposable clone. Limits: the Ca counter is red at the combined tip (APPENDONLY) and its receipt set is missing at
  the freeze (see honest limits). No non-author verifier on record.
- [~] **Box 4 — no cross-domain bleed (PROVINCE.md still accurate).** Wave-1 sibling scan covered 20 lanes:
  `wb_files=0 cjk_files=0` everywhere, and the only PROVINCE worldbuilding mention is
  `kotoba-shokunin/PROVINCE.md:61` (adjacency naming kotodama, no ownership); lore owns world-bible *records*, not
  the craft of authoring settings (`reports/round-74/telemetry/gap-sweep.txt` §7). The entries name their partial
  one-way owners in README (`synthesis/coupling-model.md`, `synthesis/consistency-verification-checklist.md`,
  `synthesis/worldbible-integration-contract.md`, `culture-material/cartography-and-mapmaking.md`,
  `linguistics/naming-systems.md`) and restate none of them. `CritScopeProvince` (landed) judges both entries
  **IN-LANE** against `PROVINCE.md:9-11` and lore's record ownership, with two MEDIUM adjacency findings (the
  amendment lands the reader-facing side of an axis only lore's boundary document names, and states a handoff
  payload the contract does not define) and three LOW note-class findings.
  `W2-PENDING:ConnectorAdjacency`. No non-author verifier on record.

## Stale-lane · tool installs · open L0

Stale-lane: none (respawn-per-round driver; `git -C kotodama-shokunin worktree list` shows one worktree at
`1d7add3`, origin/main agrees, `.ufo/state/` holds only `kotodama.report-baseline`). Tool installs: none
(wave-1 seats record "no tool installed", e.g. `w1/ExecRenumber.md:206`, `w1/RevAssimilationContract.md:382`,
`w1/CritQuality25.md:309`; pacman not run; `W2-PENDING` for seats still writing). Open L0 questions: none filed
by this round — no round-74 row exists in `.ufo/l0-questions.md`; the standing `kotodama | round-11` freshness
pause remains open and unwaived.
