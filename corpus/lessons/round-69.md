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
