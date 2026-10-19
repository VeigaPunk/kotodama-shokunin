- Seat: X01 | critic | cross | date 2026-10-19 | baseline fd55e1f

Trade hunter + conformance critic. Critique target: the round's declared
claims (`reports/round-40/claims.json`), seat missions
(`reports/round-40/targets.json`), and the repo state measured at baseline
`fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` (HEAD at my cut). The wave runs
concurrently: sibling fragments (scout/plan/cov/calib/adj/review/scribe) were
not yet landed at my cut except the telemetry declaration, so seat-output-level
review is R01/R02's lane plus the integrator's validation leg — I critique the
plan and the measured state. Every number below is a command output or a
file:line read; nothing reconstructed.

## Trades

### T1 — C coverage vs pin cascade: NO TRADE (verified clean)

Gained: coverage (linguistics 21→25). Hypothesized cost: new corpus bytes or a
README revision breaking the v3 handoff digest pins. Measured: the declared-in-r7
read set digest-pins corpus files (`reports/round-34/handoff/declared-in-r7/expected.json:125`
pins `corpus/knowledge/synthesis/worldbible-integration-contract.md` at
`5f4c02bf…`), but `grep -c README` on that expected.json = **0**,
`grep -c linguistics` = **0**, and the r30 declared-in-r6 default baseline also
has **0** README hits. New linguistics entries and the README rev-2.3 delta
break no pin; precedent: r39 landed four corpus entries after the r34 freeze and
validated exit 0 (`SCORECARD.md` r39 row). Condition that keeps this a no-trade:
C06's delta must edit only `corpus/README.md` and C01–C04's drafts must create
only new `corpus/knowledge/linguistics/*.md` paths.

### T2 — C in-wave verifiability vs no-direct-corpus-write: ACCEPTED TRADE (declared)

The C after-state (linguistics 25, total 220, README rev 2.3, "sweep green
220==220", `claims.json` C `after_required`) is only measurable after the
integrator applies the fenced bytes; seats are barred from staging corpus bytes
(`targets.json` shared_rules). The round trades seat-side final verification for
corpus-write safety. Compensating controls exist: C05 pre-landing audit + C07
independent verify + the validation leg. Consequence for wording: seat fragments
should claim "delta pre-verified against a 21+4 arithmetic", not "sweep green" —
green belongs to the integrator's post-apply run of
`python3 -B reports/round-28/readme/sweep.py` (the runner-ban in T6 does not
cover sweep.py; r35/36/39 SCORECARD rows cite seats running it).

### T3 — Ca next-touch alignment vs round roles: ACTION REQUIRED

Ca01's mission: "align next-touches with loop-1 positions 41-46"
(`targets.json` Ca01). Round 46 is a **read-only audit** — "git commit/push/
merge correctness audit — read-only audit + report; performs no pushes/merges"
(`REGIMEN.md` schedule row 14). No carried defect may receive next-touch r46
for implementation work; fixes belong at r42–45 (build positions) or r41
(verify rounds have bounded-fix precedent: r37's O claim created and bounded-
fixed the 24-row queue), or carry to loop 2 with owner. A v2 row whose
next-touch is r46-as-fixer is internally contradictory on arrival.

### T4 — Ca queue-v2 vs stale authority: ACTION REQUIRED

v2 supersedes `reports/round-37/op/defect-queue.json` (measured: schema
`kotodama-defect-queue-v1`, `rows: 24`, `census_coverage` explicitly
"carried, not claimed"). Two requirements follow. (a) The integrator's
SCORECARD/LOG row must name `defect-queue-v2.json` as the queue's current
revision — supersession-as-new-row discipline (r23/r26 precedent) — else future
rounds cite the stale v1. (b) The claim already requires census_coverage
completed or carried-with-owner (`claims.json` Ca); the v2 must state which,
because the r37 file itself disclaims set-equality.

### T5 — A audit scope vs wave concurrency: ACTION REQUIRED (labeling)

Claim A's before/after speak of "rounds 37-40" surfaces
(`claims.json` A), but r40's own artifacts land mid-wave — at any seat's cut
the r40 slice of the census is partial by construction. A01 must time-stamp its
r40 rows with the observation window and mark the residual
to-be-closed-by-the-validation-leg; otherwise the claim overstates
completeness. Rounds 37–39 surfaces are fully auditable now (all filed).

### T6 — Declared counting commands vs the in-tree runner ban: CONFORMANCE HAZARD

`claims.json` lists `python3 reports/round-40/run-validation.py` as the
counting command for **both** Ca and A — but `targets.json` shared_rules:
"never run reports/round-*/run-validation.py in-tree (the r39 isolation-replay
protocol governs any replay)", and r36 records the precedent incident (in-tree
r35 runner execution, restored — `SCORECARD.md` r36 row). These counting
commands are therefore integrator-only, executed in an isolated copy at close.
No seat (including verifiers Ca02/Ca04/A03) may "pre-run" the round-40 runner
to help. The C counting commands (`ls … | wc -l`, sweep.py) are seat-runnable.

### T7 — Breadth vs depth on the same wave: NOTED TRADE

r40 claims C/Ca/A; depth is unclaimed and stays at 3 regimen-2 claims while
coverage/calibration/adjacency each move to 4 after this round — depth becomes
the sole least-claimed non-paused axis for r41–46 (claim census in F1). That is
a legitimate midpoint-consolidation allocation, but the integrator should weigh
a depth claim (or the recorded stagnation consideration) when declaring r41+.

## Conformance findings

**F1 — lowest-axis reasoning arithmetic imprecise (minor; no admission impact).**
`claims.json` lowest_axis_reasoning: "Adjacency is the least-claimed non-paused
axis (3); coverage and calibration follow (3-4)". Measured regimen-2 claim
counts from the SCORECARD tables: depth 3 (r34/r36/r38), coverage 3
(r35/r36/r39), adjacency 3 (r33/r35/r37), calibration 4 (r33/r36/r37/r39),
operability 5 (r33/r34/r35/r37/r38). Coverage **ties** adjacency at 3 (not
"3-4"), and depth ties at 3 unmentioned. Claiming A still satisfies the r33
"lowest non-paused axis" precedent; the cited arithmetic is what is off.

**F2 — C before-state verified exactly as declared.** Measured at HEAD:
linguistics 21, total 216, partitions 94/25/21/23/29/24 (civ/CM/ling/MS/synth/
verif), README `revision: 2.2` (line 5), totals line "Total knowledge entries:
216." (line 518), footer vector 21/23/25/29/24/94 (line 522). This is exactly
claims.json C's `before` and C06's delta baseline — no drift between the
declaration and the tree.

**F3 — freshness pause respected.** axes_in_play = coverage/calibration/
adjacency (`claims.json` line 10); non_goals exclude freshness; REGIMEN pause
in force (operator ruling pending since r11). Clean.

**F4 — dispatch and telemetry declaration conform.** 24 requested workers,
1 batched call (`claims.json` dispatch) — inside REGIMEN position 7–8's 16–32
band on zai glm-5.3-flash. `telemetry/dispatch-declared.json` names owner and
declared time, keeps allocation separate from observed (no observed numbers
claimed), pins durable sources by sha256, and marks
`closing_snapshot: "open-at-seat-close: owed once validation.json lands"` —
exactly the AGENTS.md "close what you open" posture. That closing snapshot is a
parent obligation once validation.json lands; it is already self-declared, so
round admission must not proceed while it is owed.

**F5 — seat missions keep corpus writes fenced.** C01–C04 "fenced bytes,
round-35/36/39 contract"; C06 "delta draft + receipt draft"; no mission stages
under corpus/. The r39 stray-staging incident (recorded in SCORECARD r39) is
the watch-item: R01/R02 should re-check `git status` for any corpus/ entry at
close and the integrator must apply, not stage.

**F6 — C's "fourth per K03's gap scout" is well-formed, fabrication risk low
but nonzero.** r39's K01 scout names G1–G4 with G1 (contact-strata gate)
landed at r39; G2/G3/G4 match claims.json C's three named topics verbatim in
substance (`reports/round-39/scout/K01-verification-gaps.md:84,106,125,148`).
The fourth topic is K03's own r40 deliverable; C05's audit must resolve its
sources and run the linguistics collision check vs the 21 existing entries
(the mission already requires the collision check).

**F7 — G-space collision (cosmetic).** r38's "G5" is a frozen-row
self-consistency control leg (`reports/round-38/op/O03-verify.md:101`), a
different G-space from r39's gap IDs G1–G4. Fragments citing "G5" should
disambiguate.

**F8 — worktree observation (not a seat defect).** `git status` at my cut:
`M LOG.md` plus untracked `reports/round-40/`. LOG.md is parent-owned
bookkeeping (AGENTS.md wave rule: workers write only assigned fragments);
recorded so reviewers do not misattribute it to a seat.

## Owed

- Seat-fragment-level trade/conformance review (C05/Ca02/A03/R01/R02 outputs):
  impossible at this seat's cut in a concurrent wave; owed by R01/R02 + the
  integrator's validation leg.
- The r40 closing telemetry snapshot: owed by the parent once validation.json
  lands (self-declared in `telemetry/dispatch-declared.json:25`).

## Citations

- Baseline/HEAD: `git rev-parse HEAD` → `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106`; `git status` → `M LOG.md`, untracked `reports/round-40/`.
- Corpus before-state (measured): `ls corpus/knowledge/linguistics/*.md | wc -l` → 21; `ls corpus/knowledge/*/*.md | wc -l` → 216; partition census civ 94 / CM 25 / ling 21 / MS 23 / synth 29 / verif 24.
- `corpus/README.md:5` (revision 2.2), `:518` (Total knowledge entries: 216.), `:522` (footer vector 21/23/25/29/24/94).
- Pin scan: `grep -c README` → 0 and `grep -c linguistics` → 0 on `reports/round-34/handoff/declared-in-r7/expected.json`; README → 0 on `reports/round-30/handoff/declared-in-r6/expected.json`; digest-pin style at `reports/round-34/handoff/declared-in-r7/expected.json:125`.
- r37 queue: python read of `reports/round-37/op/defect-queue.json` → schema `kotodama-defect-queue-v1`, rows 24, `census_coverage` "carried, not claimed".
- r39 gaps: `reports/round-39/scout/K01-verification-gaps.md:84` (G1), `:106` (G2 taboo–euphemism lifecycle), `:125` (G3 dialect–faction/register-ecology), `:148` (G4 cultural-translation protocol fidelity).
- r38 controls: `reports/round-38/op/O03-verify.md:27,134` (guard row-blindness), `:101` (G5 leg).
- REGIMEN.md: schedule rows 7–8 (16–32 band, glm-5.3-flash) and 14 (round 46 read-only audit); per-round contract lines 27–33; freshness pause line 32.
- SCORECARD.md: r33 (`:588–590`), r34 (`:615–617`), r35 (`:640–642`), r36 (`:659–661`, incl. the in-tree-runner incident), r37 (`:676–678`), r38 (`:755–756`), r39 (`:773–774`) — basis for the F1 claim census and T6 precedent.
- `reports/round-40/claims.json` lines 8–11 (dispatch, axes, lowest-axis reasoning), 13–17 (C), 19–24 (Ca), 25–30 (A).
- `reports/round-40/targets.json` shared_rules lines 4–9; missions Ca01, A01, C01–C07.
- `reports/round-40/telemetry/dispatch-declared.json:4–5` (owner/time), `:15–24` (digest-pinned sources), `:25` (closing snapshot owed).
