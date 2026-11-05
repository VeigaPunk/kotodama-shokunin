# Round 91 verifier spot-check — kotodama

author: hyaku closure (non-author integrator, @m_zfl)
date: 2026-11-05 · base `d39434b3bc8458e1b66edd2d0d0fea9ea32f3331` · tip `40774461631ce9ed15982650f6b0a81650c08551`
Report: `.ufo/reports/round-91/kotodama.md` · prompt: `.ufo/prompts/kotodama-round-91.md`

## 1. Step-1 conformance

| check | command | observed | verdict |
|---|---|---|---|
| report committed by lane identity | `git log --format='%an <%ae> %H' -- .ufo/reports/round-91/kotodama.md` (fleet repo) | `kotodama-shokunin <kotodama@shokunin.local>` on `7b1848bb` / `76d8a256`, both on fleet `main` | pass |
| SHONEN heading, one line per box | read report `## SHONEN`; `grep '^- \[' SHONEN.md` | 4 `[~]` lines matching the 4 SHONEN.md boxes; no `[x]`; SHONEN diff base→tip touches evidence pointers only | pass |
| cited lane commits exist and are ancestors | `git merge-base --is-ancestor <hash> refs/heads/main` (jj-colocated; branch ref, not `@{u}`) | `d39434b3`, `691aebf2`, `6656cef3`, `4e0d5f9b`, `28057e09`, `b71f348c` all ancestor-ok | pass |
| lane repo clean and pushed | `scripts/hyaku/jj-lane.sh state kotodama-shokunin`; `git status --porcelain` | `branch=main local=40774461 remote=40774461 ahead=0 behind=0`; porcelain empty | pass |
| prompt carries template contract | diff vs `templates/round-prompt.md`; MISSION §L2 | mission/axes binding, 1–3 claims, L2 floor ≥8 in one batched call (matches MISSION.md line 55), report contract with path + SHONEN heading + hash citation (lines 106–107), commit-then-push, push scope, write scope (line 448), L0 side channel, hyaku addendum §6 | pass |
| lane write scope respected | `git diff --stat d39434b3 40774461` | only lane repo paths + the fleet report | pass |

Marker rule: the report names real committed round work (six commits, receipts, LOG entry) — a real report, not a marker.

Dispatch digest (from `.ufo/watchdog.log`, driver-mutable; this copy is the record):
```
2026-11-05T02:11:43-03:00 launch kotodama round=91 pgid=1952907 driver=hyaku-inline attempt=3
2026-11-05T02:12:13-03:00 lane-dead-no-report kotodama round=91; retry same round (hyaku-inline attempt=3: L1 ended without a landed report: FAIL report_of (missing, unchanged, no SHONEN heading, or < 400B): .ufo/reports/round-91/kotodama.md)
2026-11-05T02:17:40-03:00 launch kotodama round=91 pgid=1990599 driver=hyaku-inline attempt=1
2026-11-05T02:18:15-03:00 lane-dead-no-report kotodama round=91; retry same round (hyaku-inline attempt=1: …)
2026-11-05T02:18:16-03:00 launch kotodama round=91 pgid=1994550 driver=hyaku-inline attempt=2
2026-11-05T02:18:49-03:00 lane-dead-no-report kotodama round=91; retry same round (hyaku-inline attempt=2: …)
2026-11-05T02:18:51-03:00 launch kotodama round=91 pgid=1996207 driver=hyaku-inline attempt=3
2026-11-05T02:19:29-03:00 lane-dead-no-report kotodama round=91; retry same round (hyaku-inline attempt=3: …)
2026-11-05T07:31:38-03:00 launch kotodama round=91 pgid=123471 driver=hyaku-inline attempt=1
2026-11-05T09:14:17-03:00 complete kotodama round=91; hyaku-inline attempt=1
```
Four provider-failure deaths early on 02:11–02:19; the 07:31 attempt completed 09:14:17 and inherited the verified freeze (`691aebf2`) — the report discloses the inheritance and lists what was re-verified vs re-produced. Conformance defect class: none (respawns are driver behavior, not lane debt); the report's disclosure satisfies the landed-means-committed rule.

## 2. Per-claim re-check

Verification mode: plain measurements I ran over committed bytes (grep/wc/git), plus committed-evidence verification of the lane-owned gate (PROTOCOL §Gate standard, Closure consequence: the integrator verifies self-test tally, frozen-run verdict, revision measured — it does not execute a sibling's gate). No gate or counter was executed by this closure.

### Claim O / operability — **verified** (evidence-verified + surface re-measured)

- Tool pins re-derived myself: `git show 691aebf2:tools/check-advance-evidence.py | sha256sum` → `88597a66` (freeze pin `88597a66…` ✓); `git show d39434b3:tools/…` → `121888f0` (claimed base sha ✓).
- Committed frozen-run receipt `reports/round-91/final/lands-O-final.txt` (commit `b71f348c`, measured at lands `28057e09`): `LEG PASS TOOL … observed=88597a66c791…1093` (full sha match), `SELFTEST PASS 77/77`, `OKCOUNT 77 ok lines`, `REFUSALS all ok (9/9)`, `MUTATION-SCORE: 53/53 killed, 0 survived, 0 broken-pattern`, `STUB … ok lines=22; 0/53 killed, 53 broken-pattern`, `MEASURE91-O: PASS legs=7/7`.
- Freeze-time mutation receipt `reports/round-91/mutation-score.txt` (`691aebf2`): `MUTATION-SCORE: 53/53 killed, 0 survived, 0 broken-pattern` ✓.
- Before-state receipt `reports/round-91/controls/before-v1-entry.txt` (`6656cef3`): base v1 entry mode `ENTRY-EVIDENCE: PASS legs=6/6` on the topic-line-padded bakery fixture with shared URL; frozen v2 on the same fixture `LEG FAIL TOPIC … phrase anchors 0/6` and `LEG FAIL UNIQUENESS … url shared by S998,S999` (GATE FAIL per report/LOG). Receipt is explicitly labelled post-freeze, not backdated — matches ReviewerFreeze D1 handling.

### Claim C / coverage — **verified** (re-measured; every number reproduced)

| measurement (my run) | reported | observed |
|---|---|---|
| `git show 40774461:corpus/knowledge/linguistics/secret-and-ludic-languages.md \| wc -c` | 21,472 B | 21472 |
| entry at base | absent | absent |
| `git ls-tree -r --name-only <rev> corpus/knowledge/linguistics \| wc -l` | 35 → 36 | 35 → 36 |
| `… corpus/knowledge \| grep -Eic '(secret\|ludic\|argot\|slang\|cant\|jargon)'` | 0 → 1 | 0 → 1 |
| registry rows `grep -cE '^\|\s*S[0-9]{3,}\s*\|'` | 875 → 880 | 875 → 880 |
| last registry id | S951 → S956 | S951 → S956 |
| `git diff --numstat d39434b3 40774461 -- corpus/SOURCES.md` | 6 0 (append-only) | 6 0 |
| row statuses S952–S955 / S956 | mined ×4, rejected | mined ×4, rejected |
| committed receipt `final/lands-C-final.txt` | `MEASURE91-C: PASS legs=4/4`, `CORPUS-INDEX: OK files=263 rows=263 findings=0` | confirmed verbatim |

Known frozen-surface defect (ReviewerFreeze W1, disclosed in the report): `C.surface`'s "13 linguistics entries" is not reproducible (the same reading gives 3 at base); the operative unmoved command holds — status-neutral, recorded.

### No owned axis harmed

`git diff d39434b3 40774461 -- SCORECARD.md`: purely additive (planned/frozen, axes round-91, capabilities addendum). No axis score or verdict decreased; depth/freshness/adjacency explicitly unchanged (no old entry re-written, no old registry row touched, no sibling-owned file in the diff). `PROVINCE.md` untouched. Spot reads of the LOG round-91 entry and lesson confirm the tie-ins.

## 3. Per-axis verdicts (non-author)

| axis | verdict | reason |
|---|---|---|
| operability | improved | v2 grader verified against freeze pin; committed selftest 77/77, 9/9 named refusals, 53/53 mutation receipt, stub refused; before receipt shows v1 passing the same counterfeit 6/6 |
| coverage | improved | re-measured 0→1 filename owners on the secret/ludic/argot surface; entry landed with 4 new mined A/B rows cited; registry append-only |
| depth | unchanged | no existing entry deepened; corpus diff names only the new entry |
| freshness | unchanged | paused by open L0 `kotodama | round-11` and `round-89` (verified present, `.ufo/l0-questions.md` line 303); no regression; lowest-axis obligation neither met nor waived — honestly disclosed, routed |
| calibration | unchanged | ReviewerFreeze D1/D4/D5, W1–W3, R91-M6/M7/M8 recorded and routed, not repaired in place; no overreach observed in the claims as filed |
| adjacency | unchanged | canon stays lore's, research method chousa's; overlap scan names the adjacent owners; no sibling file touched |

## 4. Discernment spot-check (LEARNING.md, from outside)

Sample: 2 admits + 1 reject from `corpus/lessons/round-91.md` `## Gate`. Quotes first verified against committed captures (`reports/round-91/evidence/S95*.txt`, all found; word counts 17/21/15/8 ≤ 25), then sources re-opened live over plain HTTP on 2026-11-05.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S952 Polari overview (B, mined) | admit | https://www.lancaster.ac.uk/staff/bakerjp/polari/home.htm — HTTP 200 | agree | quote "Polari is a more recent spelling" + "Palari, Palare, Parlaree" both present in the live page; scholar-owned overview (Paul Baker, Lancaster) is a fair tier-B for the lexicon/history scope |
| S954 Harman, *A Caveat* (A, mined) | admit | https://leme.library.utoronto.ca/lexicons/109/ — HTTP 200 | agree | quote "leud lousey language" present live; LEME hosts the primary 1566 text — tier A (primary) is correct, and the gate line correctly limits the claim to the printed hostile framing, not community behavior |
| S956 Wikipedia *Argot* (C) | reject | https://en.wikipedia.org/wiki/Argot — HTTP 200 | agree | page live; rejection is tier/scope-based (community/C is never sole support per SOURCES contract), honestly recorded as "not absence of text", with a flip condition — a textbook evidence-of-taste rejection |

Census gate re-run: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → rc 0, final line `kotodama ok …/corpus/SOURCES.md` (W01/W04 warnings are pre-existing rows, none introduced by round 91 — the SOURCES diff adds 6 rows, changes none).

## 5. Trend verdicts (non-author)

- **expansion — improved.** Re-measured: dedicated entry lands on a surface with 0 prior filename owners; registry 875→880 with four mined rows cited by the new entry (`used-by` verified) and one registered rejection; adjacent owners named and not absorbed.
- **quality — improved.** The grader hardening is evidence-verified (77/77, 53/53, before-receipt showing the delta is real and finite); the new entry binds every cited line to one id with located quotes against committed captures; no admitted entry failed its re-check.
- **discernment — improved.** The round distrusts its own evidence on the record (missing before-receipt caught and produced labelled post-freeze, R91-M6; backtick-poisoned seat matching caught by an independent re-check, R91-M7; 21 quarantine rows dispositioned with nothing adopted); this closure's independent spot-check agrees with all three sampled gate decisions.

## 6. Routed defects (the lane must fix next round; status-neutral here)

1. ReviewerFreeze D4 — mutation receipt header prints the last mutant's first line beside a hardcoded `clean_rc: 0`; receipt not citable as a clean-run tally. Fix the header or drop it (frozen bytes stay unamended).
2. ReviewerFreeze D5 — no counter leg checks the "mutation receipt over every v2 sub-check" clause; next counter amendment should assert the receipt's existence, count and tool sha.
3. ReviewerFreeze W3 — `grade_c` APPENDONLY arm indexes cells without a column-count guard; malformed short row aborts instead of scoring. Refuse malformed rows as a leg FAIL.
4. CriticClaims91 survivors — seven entry-mode counterfeit classes still pass v2 rc 0 (lesson-channel dispositions behind blockquote/no dash, chrome quote as own sentence, `#fragment` shadow, heading stuffing, capture byte-copied from base registry, shared capture path); routed to round 92 with fixture ideas (`CriticClaims91/attacks.md`, R91-M8).
5. MutationTesterV2 — 6 real survivor gaps (NEWIDS non-mined status, GATE no-lesson-line, CAPTURE fetched-date, path-confinement, TOPIC table-cell source, graded auto-include); selftest does not isolate every arm.
6. Lowest-axis debt — freshness stays paused on open L0 `kotodama | round-11`/`round-89`; needs an operator ruling, not lane action. Named, not waived.
7. Frozen `claims.json` N1/N2 documentation debt (duplicate `legs` block; "9 v2 pairs" vs 53 triples) — documentation only.

## 7. Closure ruling

Both claims verify (O evidence-verified, C re-measured); no owned axis harmed; spot-check agrees 3/3; census rc 0 at tip; repo clean and pushed at `40774461`. **admitted.** SHONEN boxes remain `[~]`; they are now fully checkable by a non-author on the cited receipts — flagging for the operator that promotion review is possible (promotion is operator-owned; no `[x]` written by this closure).
