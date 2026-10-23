# ScribeReportFrag — round-64 wave 1, lane report skeleton

## Behavior and axes

Axes judged: **coverage**, **operability**, **calibration**.

This seat produced the **round-64 lane report skeleton**: the full ordered
section frame of the fleet report contract (`Work performed` → `Landed
changes` → `Before → after measurements` → `Sources & frontier` → `Trend
verdicts` → `SHONEN` → `Stale-lane` → tool-install line), with every slot
filled from committed lane bytes where possible and every unfillable slot
marked `TBD-<what>`.

Skeleton path (scratch, outside the lane repo):
`/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReportFrag/report-skeleton.md`

Structure was modelled on the round-63 lane report
(`/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotodama.md`), the
fleet report template (`/home/vgpnk/Projects/shokunin/templates/round-prompt.md`
§4), `SHONEN.md` (four boxes), `corpus/lessons/round-63-verifier-spotcheck.md`
(the round-63 SHONEN one-line-per-box defect), and the round-64 wave-2 lesson
draft `.ufo/waves/round-64/w2/B2ScribeLesson.md`.

## Section coverage delivered (in order)

1. **Work performed** — opens with the three declared claims **C (coverage)**,
   **O (operability)**, **Ca (calibration)** as declared in
   `reports/round-64/claims.json`, each with its axis, frozen predicate,
   command, leg list, lands and exports.
2. **Landed changes** — commit-keyed table; only `097c21d` (declaration +
   instruments) exists in the lane repo, every claim-land and records row is
   `TBD-<commit>`.
3. **Before → after measurements** — one per claim, each with a counting
   command, the before value measured over committed bytes, and the measured
   commit:
   - C — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
     → before **643** at `ff30a205`; after `TBD-claim-c-registry-landing`
     (declared target 675). Supporting committed counts at `ff30a205`: corpus
     entries 237, linguistics 29, filename owners 0, topic-line owners 0.
   - O — `python3 -B reports/round-64/accept-o.py --root .`; before measured at
     the round-63 records tip `80ff34c`: 15 legs, **0** `EDGE_`/`DRIP` legs;
     after `TBD-claim-o-counter-landing-and-run`.
   - Ca — `python3 -B reports/round-64/accept-ca.py --root .`; before measured
     at `ff30a205` and recorded in the committed receipt
     `reports/round-64/telemetry/dry-run-ca.txt`: every leg FAIL, `exit=1`;
     after `TBD-claim-ca-repair-landing-and-run`.
4. **Sources & frontier** — rows before 643 → after `TBD` (target 675) with
   the counting command; the census command from `CORPUS.md` §Census and the
   two wave-1 receipts; rows added by tier (staged artifacts: mined
   A = 17 / B = 9 over `S718`–`S743`; disposition A = 1 / B = 4 / C = 1 over
   `S744`–`S749`, 3 rejected + 3 queued); rows touched old→new
   (**S687 `mined → queued`**, the only tolerated in-place change); frontier
   rows advanced (the six disposition re-tests, three rejections standing and
   three contradicted).
5. **Trend verdicts** — `expansion` / `quality` / `discernment`, each with the
   evidence that will settle it and an explicit `TBD-<acceptance-outcome>`
   marker; no verdict is asserted ahead of the committed run.
6. **SHONEN** — one line per `SHONEN.md` box (four boxes), each `[~]` with a
   resolvable pointer (`SKILL.md:20/:468/:522`; the `LOG.md` round-64 heading;
   the per-claim command/predicate in `claims.json`; `PROVINCE.md` + the
   skeleton §10 handoff + the 21-lane province scan).
7. **Stale-lane line** — respawn-per-round driver; no other mission of this
   lane is open.
8. **Tool-install line** — none installed; pacman paused host-wide; nothing
   beyond the Python 3 stdlib and `git`/`grep`/`awk` was needed.

## Gates and exact outcomes

No acceptance predicate was executed by this seat and no predicate result is
claimed. The committed dry-run receipts were **read**, not rerun:
`reports/round-64/telemetry/dry-run-c.txt` (ACCEPT-C-64 FAIL, `exit=1`) and
`reports/round-64/telemetry/dry-run-ca.txt` (ACCEPT-CA-64 FAIL, `exit=1`),
both committed at `097c21d`.

Read-only commands run by this seat (all read-only; no lane file mutated):

- `git log --oneline -8`, `git status --short`, `git rev-parse HEAD` →
  HEAD `097c21d0eba5023cfd38b767fb41d59409eef125`.
- `git show ff30a205:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 643.
- `git ls-tree -r --name-only ff30a205 corpus/knowledge | grep -c '\.md$'` → 237;
  `… corpus/knowledge/linguistics | grep -c '\.md$'` → 29.
- `git grep -c -i "^- topic:.*socializ" ff30a205 -- corpus/knowledge` → no
  match (0 topic-line owners); `git ls-tree -r --name-only ff30a205
  corpus/knowledge | grep -ci "socialization\|acquisition"` → 0 filename owners.
- `git show ff30a205:corpus/SOURCES.md | awk -F'|' '…'` status histogram →
  mined 567, queued 57, rejected 19.
- `git show 80ff34c:reports/round-63/accept-o.py | grep -cE 'leg\("(EDGE_|DRIP)'` → 0;
  unique leg names → 15.
- `grep -o 'leg("[A-Z_0-9]*"' reports/round-64/accept-o.py | sort -u | wc -l`
  → 23 distinct leg names (working tree, untracked).
- `grep -o 'leg("[A-Z_0-9]*"' reports/round-64/accept-ca.py | sort -u` → 7 legs
  (working tree, revision 1); `git show 097c21d:reports/round-64/accept-ca.py`
  → 6 legs (revision 0, committed).
- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`
  → `CHECK-ROWS: 32/32 clean` (all 26 mined + 6 disposition row artifacts
  present and clean; the inherited attempt-1 gaps S723 and S740 are now filled).
- `ls reports/round-64/mutants/` → empty; `ls reports/round-64/telemetry/` →
  `census-start.txt`, `census-wave1.txt`, `dry-run-c.txt`, `dry-run-ca.txt`,
  `dry-run-o.txt`, `dry-run-o-baseline-copy.txt`, `final-measures-o.txt`;
  `mut-o.txt`, `edge-o.txt`, `control-o.txt`, `controls-c.txt` absent.
- `jj log -r 'main | @'` (read-only) → main tip `qmxornppsppv` = `097c21d`.

## Findings (verbatim evidence for the canonical judge)

1. **The claim-O receipt does not establish the predicate.** The untracked
   `reports/round-64/telemetry/final-measures-o.txt` has 22 lines, all
   `PASS`: TOOL, INDEP, GEN, ORDER, BOUND, EXIT, PRIV, DEFAULT, ERR,
   REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT, EDGE_SCHEMEREL, EDGE_USERINFO,
   EDGE_HTTPS, EDGE_MALTARG, EDGE_SLASHLESS, EDGE_308, EDGE_5TH200, DRIP.
   There is **no `MUT` line** and **no `ACCEPT-O-64:` verdict line**, while
   `reports/round-64/claims.json` declares 23 legs for O including MUT.
   `grep -c "ACCEPT-O-64" reports/round-64/telemetry/final-measures-o.txt` → 0.
2. **Claim-O lands are missing.** `reports/round-64/accept-o.py` is untracked
   (`git ls-files --error-unmatch` → "Did you forget to 'git add'?"), the
   mutants directory `reports/round-64/mutants/` is empty, and three of the
   five declared lands (`telemetry/mut-o.txt`, `telemetry/edge-o.txt`,
   `telemetry/control-o.txt`) do not exist.
3. **Committed `accept-ca.py` rev0 prints 6 legs, `claims.json` declares 7.**
   `git show 097c21d:reports/round-64/accept-ca.py | grep -o 'leg("[A-Z_0-9]*"'
   | sort -u` → CANONLOG, DISPO, HISTOGRAM, NITS, PTRS, R63SEP — **REVNAMES
   absent**. The committed dry-run receipt `dry-run-ca.txt` shows the same six
   legs, all FAIL, `exit=1`. The uncommitted working-tree revision 1 adds
   `leg("REVNAMES", rev_ok, …)` with the comment "revision 1 (pre-data): the
   docstring declared REVNAMES but the rev-0 code computed rev_ok and never
   printed or counted it (dry-run receipt shows 6 legs against 7 declared in
   reports/round-64/claims.json)". Per the round-64 rule, this seat did not
   edit the counter; the defect is recorded here for the integrator.
4. **Committed `accept-c.py` rev0 REJECTS leg is narrower than the landed
   dispositions.** Rev0 requires `cs[7] != "rejected"` → reject and
   `teaches.startswith("REJECTED:")`. Three of the six staged disposition rows
   are `queued` with a `QUEUED-CANDIDATE:` cell because the re-test
   contradicted the prior rejection ground (`S746` catalogue wording
   locatable; `S748` LacusCurtius Corona `TEST: 200` + `TEST2: LOCATED`;
   `S749` Wikipedia headgear `TEST: 200` + `TEST2: LOCATED`). Rev0 would
   score those three as failures; the working-tree revision 1 widens the leg
   to `cs[7] not in ("rejected", "queued")` and
   `teaches.startswith(("REJECTED:", "QUEUED-CANDIDATE:"))`. Not edited here.
5. **Registry landing has not happened.** `corpus/SOURCES.md` still measures
   643 rows; the entry file
   `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
   does not exist; `corpus/README.md` has no index row for it and its footer
   still reads "Total knowledge entries: 237" with directory totals
   29/29/31/29/24/95; the S687 `mined → queued` flip is not applied; and
   `corpus/lessons/round-64.md` does not exist.
6. **Claim-Ca repairs are working-tree only.** `LOG.md`, `SCORECARD.md` and
   `corpus/LOG.md` carry the repair as uncommitted modifications
   (`git diff --stat` → LOG.md 11 lines, SCORECARD.md 11, corpus/LOG.md 6), and
   `reports/round-63/telemetry/revisions.txt` (the REVNAMES land) is untracked.
7. **Row staging is complete now.** `check-rows.py` → 32/32 clean. The two
   rows missing in the inherited attempt-1 state (S723, S740) both have
   artifacts. Mined tier split over the 26 rows: **A = 17, B = 9**; the six
   disposition rows: A = 1, B = 4, C = 1, statuses 3 `rejected`
   (`S744`, `S745`, `S747`) and 3 `queued` (`S746`, `S748`, `S749`).
8. **`SHONEN.md` box 1 carries a superseded figure.** Its parenthetical
   "412 rows after round 56 — 367 mined, 35 queued, 10 rejected" is a dated
   historical reading; the registry measures **643** rows (567 mined, 57
   queued, 19 rejected) at `ff30a205`. The round-63 spot-check flagged the
   equivalent SHONEN defect (only two of four boxes answered); the skeleton
   answers all four boxes, one line each.
9. **Seat-report coverage is incomplete in both wave-1 specs.** The 45-seat
   `w1-spec.json` names seats with no report file yet in
   `.ufo/waves/round-64/w1/` (e.g. `ExecIntegrate`, `ExecCaRepair`,
   `ExecOCounter`, `ScribeLessonDraft`, `RevengerFrontier`, `ScoutLocatorRecon`,
   `ScoutRegistryRecon`, `ConnectorSiblings`, `CriticClaimSizing`,
   `ReviewerPredicates`, and ten `ScribeRowS7xx` seats); the 32-seat
   `nw1-spec.json` names nine still missing (`ExecRowS740`, `ExecIntegrate`,
   `ExecCounterO`, `ScribeLesson`, `ScribeReportFrag`, `ReviewerCounterC`,
   `ReviewerCounterO2`, `ReviewerSeparability`, `ScribeGateQuotes`).

## Touched surfaces and out-of-scope items

Written by this seat (two files, both new):

- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReportFrag/report-skeleton.md`
  (scratch skeleton, outside the lane repo).
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w1/ScribeReportFrag.md`
  (this report).

Nothing else was created, edited, committed, pushed, published or deployed.
No product code, registry, knowledge entry, counter, lesson, LOG, SCORECARD,
`claims.json` or telemetry receipt was modified. No acceptance counter was
edited and no acceptance counter was executed. No sibling repo, fleet repo,
lane jj state or lane git index was touched; no commit was made.

Out of scope for this seat by assignment: writing the entry, appending the
registry rows, running or repairing the counters, committing the wave-1
artifacts, and the authoritative before→after and acceptance runs (integrator
work).

## Limits

- No acceptance predicate was run or claimed. Every "after" value in the
  skeleton is `TBD-…`; the skeleton never states that a leg passed.
- The skeleton is a skeleton: the integrator fills the `TBD-` slots from the
  committed final state and owns the authoritative receipts.
- Working-tree state was read (read-only) to describe what is staged; it is
  reported as staged, never as landed.
- No tool was installed or upgraded; pacman stayed untouched (host-wide pause).
