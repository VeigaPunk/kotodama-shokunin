# Round 69 — kotodama (2026-10-24, hyaku run 6, L1 kotodama-r69 attempt 1)

Repair-first round after round 68 was rejected (`corpus/lessons/round-68-verifier-spotcheck.md`:
O failed on a structurally unreachable EXEC fixture; Ca's frozen rev-1 counter crashed on an
undefined `git_bytes`). This round declares NEW counters — the round-68 counters are not amended
(leg `R68FROZEN` in both new counters re-derives their sha256 against their own receipts) — and
every new counter carries a green pre-data control and a do-nothing control scored before data
(`reports/round-69/telemetry/controls.txt`, `controls-rev1.txt`).

## Gate

Candidates, admitted and rejected, with the access date and a located quote. One row was opened
this round; no external source was fetched (the round's only row is the lane's own re-runnable
check, kind `own-work`).

| id | source / command | opened | located quote (≤25 words) | grounds | verdict |
|---|---|---|---|---|---|
| S859 | repo path `tools/check-supersession-settlement.py`; command `python3 -B tools/check-supersession-settlement.py --selftest` (lane file blob `1ef2e965204f53f40ffbabf45abea3fae9f029a6` at revision `52b92a6b`) | 2026-10-24 | "A chain is *settled* when exactly one state holds" — `tools/check-supersession-settlement.py:6` (docstring); the command prints `SELFTEST: 7/7` | the lane's own re-runnable gate output is tier A for the settlement taxonomy (SOURCES contract v1, tier A: "the lane's own re-runnable gate output"); scope limited to the five chain states and their preconditions | **admitted** (mined); used-by `SKILL.md`, `corpus/lessons/round-69.md` |

Rejected this round: none. No source was opened and refused (the round opened exactly one
candidate, and it was admitted). The lane's rejected rows of earlier rounds (S047, S070, S125,
S047-family, S857, S858) stay rejected with their reasons and flip conditions untouched.

## Mistakes

- R68-M9 | the round-68 report's pointer to a mistake row that was never written | class: landing (a routed mistake never got its row) | evidence: `.ufo/reports/round-68/kotodama.md:35` reads "`## Mistakes` R68-M1..M8 (+M9 in LOG)" and `:11` reads "Ca fails as declared (R68-M9)", while `grep -c 'R68-M9' LOG.md corpus/lessons/round-68.md` → 0 before this round — the crash itself is real (`reports/round-68/telemetry/final-measures-ca.txt`, `NameError: name 'git_bytes' is not defined` at `accept-ca.py:224`) | captured-by: QUALITY criterion 11 (a green control must exist for every mechanical clause before data) plus the report's own pointer discipline; the row was never filed | fix: **this row** (appended in this lesson and named in the `LOG.md` round-69 entry) — the lesson now carries R68-M1..R68-M9, so the filed pointer resolves; the crashed counter stays unamended and its repair is the new counter `reports/round-69/accept-ca.py`
- R69-M1 | the round-69 operability counter judged the new harness by the harness's own printed lines | class: instrument defect (a do-nothing control could reach the declared target) | evidence: `.ufo/waves/round-69/w1/CritO1.md` probe C — a no-op harness that only prints `FIXTURE: 3/3` and `LANE: pending=0 missing_paths=0` reached `ACCEPT-O-69: PASS 7/7` without running a single fixture; the seat's leg-anchor table shows FIXTURE, NEGCASE and the harness half of LANE adjudicated on the harness's self-report | captured-by: the wave's falsifier seat (CritO1), before any data landed | fix: counter revision 1 (recorded in `reports/round-69/claims.json` `counter_revisions` with the forcing receipt): the predicate sentence, the seven leg names and the 7/7 target are unchanged, but no leg trusts the harness's self-report any more — the counter builds its own lane-shaped fixtures, runs the base checker itself, scans the lane root itself, and uses the harness only as a cross-check on a fixture the counter built (`NEGPROBE`). The spoof now fails: `reports/round-69/telemetry/controls-rev1.txt` shows SPOOF FIXTURE FAIL (6/7) as required
- R69-M2 | the round-69 operability counter's own do-nothing control was incomplete at declaration | class: claim sizing (the cheapest control that skips the claimed work did not include the spoof class) | evidence: the declared control (`claims.json`, `do_nothing_control`) covered deletion only; the spoof class was found by the wave, not by the declaration | captured-by: the wave's falsifier seat (CritO1), before any data landed | fix: revision 1 adds a third control — the SPOOF FIXTURE — so the declared do-nothing set now covers deletion, breakage and spoofing; `reports/round-69/telemetry/controls-rev1.txt` records all three
- R69-M3 | eleven of thirty-two wave seats died | class: provider (rate wall, not a lane defect) | evidence: `.ufo/waves/round-69/w1/settle.tsv` — nine seats ended with `provider.rate_limit: 429 Rate limit reached for requests` (CritD5, MutO1, RevC2, RevO1, RevO2, RevO7, ScoutFrontier, Scribe1, Scribe2) and two (CritO3, RevO4) were killed by the 1200 s per-seat timeout while still working; 21 seats returned reports | captured-by: the lane's own dispatch receipt (the error text is retained this time, unlike round 68's R68-M7) | fix: the per-seat error text is now kept (`.ufo/waves/round-69/w1/stdout/*.err`); dead seats are reported, never replaced. The already-filed weekly-quota L0 (kotoba r67) covers this host condition
- R69-M4 | the base checker swallows malformed registry rows | class: instrument gap (surfaced by the wave, not introduced here) | evidence: `.ufo/waves/round-69/w1/CritO2.md` D2 — a row that does not split into exactly 11 cells is marked malformed and skipped from both chain classification and used-by existence checks, so the `SETTLEMENT` summary reports `chains=0` and the debt is invisible; live today 0 malformed rows | captured-by: none in the round-69 instruments (the round-69 counters do not claim a malformed-row check) | fix: routed to round 70 — the round-69 fixture harness and counters are not extended, because the claim's surface is the missing-used-by class only; the honest scope limit is recorded in the report
- R69-M5 | the base checker's `used-by` check is existence-only | class: instrument gap (surfaced by the wave) | evidence: `.ufo/waves/round-69/w1/CritO2.md` D3 — the docstring's `STALE-USED-BY` class names a containment check (the file must contain the row's own id) that no committed code path implements; the fixture's used-by file content is decorative | captured-by: the wave's attack seat (CritO2) | fix: routed to round 70; recorded here because it bears on the new S859 row (its `used-by` names `SKILL.md`, and nothing verifies the file literally cites `S859` — review work, not gate work)
- R69-M6 | the base checker counts `missing_paths` per (row, path) pair, not per unique file | class: instrument gap (surfaced by the wave) | evidence: `.ufo/waves/round-69/w1/CritO2.md` D5 — the live registry has five comma-separated multi-path cells (S002 lists 11 paths); the fixture only ever uses single-path cells | captured-by: the wave's attack seat (CritO2) | fix: routed to round 70 (a multi-path fixture case); the round-69 claim does not claim the multi-path class
- R69-M7 | the round-69 calibration claim's after-state is unsatisfiable | class: claim sizing (an after-state that requires rewriting frozen bytes) | evidence: `claims.json` Ca2 `after` requires every declared pair's observation to be **consistent** *and* a correction row to exist, while the round-68 filed texts are frozen and never rewritten; the counter's implemented closure is annotation-only, so 4 of 5 pairs print `live=True` and the frozen `kill_rule` ("any declared pair that is live or uncovered -> the claim fails as declared") triggers under a green predicate. Full argument + counterexample: `.ufo/waves/round-69/w2-verify/CritCa2.md` | captured-by: the residual verification seat CritCa2, post-data | fix: not repairable without editing a frozen counter or rewriting frozen round-68 bytes — Ca2 is reported **FAILED AS DECLARED**; the split (predicate met / kill rule triggered) becomes a QUALITY bar routed to round 70: a claim's kill rule must be satisfiable by the counter's own legs
- R69-M8 | the operability counter's NEGPROBE leg adjudicates a constant | class: instrument defect (a spoof still passes by printing one token) | evidence: `.ufo/waves/round-69/w2-verify/CritAnchoring.md` — the rev-0 spoof with `LANE: pending=0 missing_paths=1` reaches `ACCEPT-O-69: PASS 7/7`; `accept-o.py:224-227` reads the harness exit code, `FIXTURE:` line and green run into the detail string and tests none of them; a directory-keyed detector also scores 7/7 | captured-by: residual seat CritAnchoring | fix: routed to round 70 (differential cross-check across the green and negative fixtures plus rc equality; counters are frozen post-data and are not edited)
- R69-M9 | the new harness has four surviving mutation classes | class: capability quality | evidence: `.ufo/waves/round-69/w2-verify/MutHarness.md` — 5/9 mutations killed; survivors are harness rc forced 0, malformed-row swallow (`if False and len(c) != 11`), closed<->retired label swap, and a weakened negative assertion | captured-by: residual seat MutHarness | fix: routed to round 70; the acquired capability is real for the used-by class (M1 killed by NEGCASE + NEGPROBE) but not mutation-effective
- R69-M10 | both STAMP legs are vacuous under the canonical `--root .` invocation | class: instrument defect (a file compared to itself) | evidence: `.ufo/waves/round-69/w2-verify/RevRerun.md` F2 — appending one comment line to `accept-o.py` / `accept-d.py` still prints `STAMP PASS` with the new sha, 7/7 and 8/8 | captured-by: residual seat RevRerun | fix: routed to round 70 (anchor to the receipt's `# counter sha256 (self)` line or to `git cat-file blob <measured-rev>:…`)
- R69-M11 | `accept-d.py --selftest` became non-reproducible after the data landed | class: instrument defect (fixture seeded from the live bytes it is supposed to lack) | evidence: `.ufo/waves/round-69/w2-verify/RevRerun.md` F1 and `CritDepth.md` — at `9e82c7b` the selftest prints `DO-NOTHING FIXTURE: PASS (unexpected)`, `SELFTEST: 1/2`, exit 1 against the committed pre-data `1/8`, `2/2`, exit 0; `build_fixture_root()` seeds from `LANE/SKILL.md` | captured-by: residual seats RevRerun and CritDepth | fix: routed to round 70 (seed the do-nothing fixture from `793f797:SKILL.md`); the data predicate is unaffected and stays 8/8
- R69-M12 | the D2 decision table carried five statements its own code contradicts | class: content correctness (the counter adjudicates headings, not content) | evidence: `.ufo/waves/round-69/w2-verify/CritDepth.md` — settled-closed "successor is live … rule `keep-reject`" is false for 10 of the 12 live closed chains (S570>S135 rules `keep-successor`, ledger `:78`); settled-active "used-by naming a real corpus path" vs the existence-only check; pending "write the row, then apply it" is refused by the validator (`activate_but_status=queued`, `:207-208`); malformed rows fail silently; four signatures are review-only; a 5-row filler table scores 8/8 | captured-by: residual seat CritDepth, post-data | fix: **repaired in attempt 2** — the false clauses, the malformed-row caution and the review-only marking land in `SKILL.md`; `accept-d.py` re-run gives 8/8 (`reports/round-69/telemetry/final-measures-d-attempt2.txt`)
- R69-M13 | the lesson's Quarantine claim that S859 lies outside the staged id set is false | class: record accuracy | evidence: `.ufo/waves/round-69/assimilation/staged-ids:1` reads `S859` (package `merge/kotodama/SOURCES.append.md:7`, GB/T 33661-2017); CritCa2, ScoutItem10 and RevRecords agree; the committed `collisions` = 0 is honest only for the pre-S859 782-id snapshot | captured-by: residual seats ScoutItem10 and RevRecords | fix: corrected in the `## Quarantine` addendum below; the collision is routed to the next adoption round (the package row must be renumbered in scratch before any append)
- R69-M14 | two round-69 record figures are wrong | class: record accuracy | evidence: `.ufo/waves/round-69/w2-verify/RevRecords.md` — `telemetry/census-start.txt` carries no `exit=` line although the records claim exit 0 (re-derived at base: exit 0, 28 `W04` warnings, `telemetry/census-start-recheck.txt`), and `grep -c 'R68-M9' LOG.md corpus/lessons/round-68.md corpus/lessons/round-69.md` prints 4 matched lines in 2 files, not 3 | captured-by: residual seat RevRecords | fix: corrected in `## Corrections (round 69 attempt 2)`
- R69-M15 | attempt 1 died before filing the fleet report, and the round sat unreported for ~4 h | class: provider/session (session died 2026-10-24 ~23:30 -03) | evidence: `.ufo/watchdog.log:03:23:08-03:00 lane-dead-no-report kotodama round=69; retry same round`; the lane itself was clean and pushed (tip `9e82c7b`, tracked=0 untracked=0, ahead=0), so no work was lost | captured-by: the driver's lane-dead line | fix: attempt 2 re-ran the three counters in a fresh clone, attacked them with seven residual seats and filed the report; no lane repair was needed

## Attempt 2 — residual verification (2026-10-25, inherited work re-verified)

Attempt 1's work was fully committed and pushed before its session died (`9e82c7b`); attempt 2
inherited **no uncommitted lane output** (`git status --porcelain` empty, `jj-lane.sh state` →
`ahead=0 behind=0 tracked=0 untracked=0`). One residual `task` call of seven seats attacked the
landed measures — reviewer ×2 (fresh-clone re-run; record arithmetic), critic ×3 (O2 anchoring,
Ca2 kill rule, D2 content), mutation-tester ×1 (harness), scout ×1 (item-10 re-derivation). All
seven returned; none died. Evidence: `.ufo/waves/round-69/w2-verify/*.md`.

| claim | frozen predicate, re-run | residual attack | verdict |
|---|---|---|---|
| O2 | PASS 7/7, byte-identical to the receipt (`RevRerun.md`) | anchoring falsified (constant NEGPROBE spoof, dir-keyed detector), 4/9 mutations survive, STAMP vacuous | **verified on its frozen predicate**; capability partial — R69-M8..M10 routed |
| Ca2 | PASS 8/8, `unannotated=0` over 5 pairs, 4 live (`CritCa2.md`) | the frozen `kill_rule` fires on the 4 live pairs; stub correction rows also pass | **FAILED AS DECLARED** — R69-M7; the after-state cannot be satisfied without rewriting frozen bytes |
| D2 | PASS 8/8 (`RevRerun.md`) | five content statements false, EVIDENCE path-only, do-nothing selftest non-reproducible post-data | **verified on its frozen predicate after a content repair** (R69-M12), 8/8 re-measured |

Item-10 guard proof landed for the first time: `.ufo/waves/round-69/assimilation/guard-proof/`
(indented-only fixture `  | S002 |` → column-zero pattern 0 ids, 0-3-space pattern 1 id; full
base registry with the column-zero S002 removed and an indented S002 added → old 0, new 1 collision).
Adoption stays CLOSED (wave-4 quarantine-first).

## Corrections (round 68, append-only)

Both status-neutral defects the round-68 closure routed are corrected here by appended rows; the
filed round-68 bytes are not rewritten. The full table with the re-derivation commands is
`reports/round-69/corrections-r68.md`; the counter that measures it is `reports/round-69/accept-ca.py`.

| class | surface | filed text | observed | correction |
|---|---|---|---|---|
| LEGCOUNT | `SCORECARD.md` round-68 operability row | `ACCEPT-O-68 9/10 legs PASS at A_c` | the committed receipt prints 9 legs — 8 PASS and 1 FAIL (EXEC) | appended correction row in the `SCORECARD.md` round-69 corrections table and in the `LOG.md` round-69 entry |
| LEGCOUNT | `LOG.md` round-68 entry | `ACCEPT-O-68 prints 9/10 legs PASS at A_c` | the same receipt: 9 legs, 8 PASS, EXEC FAIL | appended correction in the `LOG.md` round-69 entry |
| LEGCOUNT | `.ufo/reports/round-68/kotodama.md` (fleet repo) | `ACCEPT-O-68 prints 9/10 legs PASS` and `9/10 legs PASS, exit 1` | the same receipt | appended correction in the `LOG.md` round-69 entry and here; the fleet report is outside the lane's write scope and is NOT edited |
| DEADPOINTER | `.ufo/reports/round-68/kotodama.md` (fleet repo) | `R68-M1..M8 (+M9 in LOG)` and `Ca fails as declared (R68-M9)` | no R68-M9 row existed in `LOG.md` or `corpus/lessons/round-68.md` | **this lesson's `## Mistakes` R68-M9 row** (appended) plus the `LOG.md` round-69 entry; the fleet report is NOT edited |
| OVERREACH | `SCORECARD.md` round-68 calibration row | `\| calibration \| improved (claim Ca, records) \|` | the committed receipt carries a `NameError` traceback and never prints `ACCEPT-CA-68: PASS` — the claim did not verify | appended correction row in the `SCORECARD.md` round-69 corrections table and in the `LOG.md` round-69 entry |

## Corrections (round 69 attempt 2, append-only)

Found by the residual seats after attempt 1 filed its records; the faulty bytes are named, not
rewritten, and each row carries its own re-derivation.

| class | surface | filed text | observed | correction |
|---|---|---|---|---|
| CENSUS-EXIT | `reports/round-69/telemetry/census-start.txt` and the records built on it | the census "exits 0 at round start" | the receipt is 29 lines (28 `W04` + `ok`) with no `exit=` line, unlike the end receipt (`:32 exit=0`) | the fact is re-derived at base `793f797`: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, same 28 `W04`; receipt `reports/round-69/telemetry/census-start-recheck.txt` |
| MISTAKE-COUNT | `SCORECARD.md` round-69 corrections table, `LOG.md` round-69 entry, R68-M9 row | `grep -c 'R68-M9' …` → 3 matched lines | the documented command prints 2 + 0 + 2 = 4 matched lines in 2 files (10 occurrences); the substantive claim (0 before this round) holds | the corrected figure is 4 matched lines in 2 files, 10 occurrences; `grep -c` over a single file reads `LOG.md` 2 and `corpus/lessons/round-69.md` 2 |
| STAGED-IDS | this lesson's `## Quarantine` paragraph | "the lane's own new row is S859, which is outside the staged id set" | false: `.ufo/waves/round-69/assimilation/staged-ids:1` is `S859` (package `merge/kotodama/SOURCES.append.md:7`) | the inverse reading holds — see the Quarantine addendum below; the package state is 132 staged ids today (123 at the round-69 snapshot), so the 123-id set is a snapshot of an unversioned input |
| POINTER | `SCORECARD.md` round-69 coverage/freshness/adjacency row | `reports/round-69/w1/ScoutAdj.md` | that lane-relative path never existed; the seat report is `.ufo/waves/round-69/w1/ScoutAdj.md` | pointer corrected in place in the same round-69 row (no evidence value changed) |

## Quarantine — shokuknow absent-defect register, kotodama slice (item 10, wave-4 quarantine-first)

**Adoption CLOSED this round; nothing was adopted, appended or renumbered from the package.** The
lane's slice was re-derived at round time with the addendum's own recipe (read-only; nothing in
`/home/vgpnk/Projects/shokuknow` was written or run): **21 data rows**, matching the round-68
count (`.ufo/waves/round-69/assimilation/quarantine-slice`). The round-68 per-row verdicts (9
present, 8 refused, 4 unverifiable — `corpus/lessons/round-68.md` `## Quarantine`) still stand on
their committed fetch evidence; this round re-derives the slice and the id-collision check but
does not re-fetch, so it claims no new verdicts.

Id-collision check (scratch, before any append): `reg-ids` 782 ids, `staged-ids` 123 ids,
`collisions` **0** — `.ufo/waves/round-69/assimilation/{reg-ids,staged-ids,collisions}`. The lane's
own new row is S859, which is outside the staged id set; the package's own ids remain the
campaign's namespace and were not adopted, so no renumbering was needed.

`considerthese/` is **absent** for this lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese/`
does not exist (recorded, not invented; the addendum lists kotodama among the lanes with no such
directory).

### Correction to the id-collision paragraph (attempt 2, append-only)

The sentence "the lane's own new row is S859, which is outside the staged id set" is **false** and
is corrected here, not rewritten. `staged-ids:1` reads `S859` (the package's GB/T 33661-2017 row at
`/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md:7`), so the lane's own settlement
row and the package's first staged row share an id. The committed `collisions` = 0 is honest only
for its own snapshot: it was computed against the pre-S859 registry (`reg-ids`, 782 ids, base
`793f797`) whose last id is S858, so a zero was forced. Re-running the same recipe against the
current registry (783 ids, S859 present) yields **1 collision: S859** (`.ufo/waves/round-69/w2-verify/ScoutItem10.md`
§2, `RevRecords.md` defect 3). `staged-ids` is a snapshot of an unversioned input: it holds 123 ids,
the package holds 132 today and 104 at shokuknow `HEAD`.

Consequence for the next adoption round, not this one: adoption stays CLOSED (wave-4
quarantine-first), and any future append of the package's S859 must be renumbered **by document**
in scratch before it lands — the lane's registry keeps its own S859 (append-only, CORPUS.md rule 2).

Guard proof committed for the first time (the addendum requires it, and attempt 1 committed none):
`.ufo/waves/round-69/assimilation/guard-proof/{guard-proof.txt,note.txt}` — an indented-only
fixture `  | S002 |` yields 0 ids under the column-zero pattern and 1 id under the 0–3-space
pattern; the full base registry with its column-zero S002 removed and an indented S002 added
yields 0 collisions under the old pattern and 1 (S002) under the contract pattern.

