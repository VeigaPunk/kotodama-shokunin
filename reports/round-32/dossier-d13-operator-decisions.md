# R32-D13 — operator decision materials (the regimen's close)

- **Seat:** D13 (dossier leg 3 of 3), round 32 — the regimen's final round.
  Claim **D** / depth, `reports/round-32/claims.json`.
- **Date:** 2026-10-18. Declared baseline
  `17e90b9047b289d7a63180a1dc1bebb074137e29`; lane HEAD at evidence cut `4d50050`.
- **Non-author declaration:** this seat authored none of the cited artifacts.
  **Write scope:** this file only. No git commit/push, no edits to filed
  rounds 8-31. Scratch: `TMPDIR=$PWD/.scratch`.
- **Standing rule of this dossier:** it claims **no promotion and no closure
  verdict**. Per the claim letter: "the dossier claims no promotion, it IS the
  decision's evidence." Every decision below is the operator's; each section
  states the decision, the evidence for and against, and what would change it.

## Decision 1 — promotion of kotodama-shokunin (the SHONEN marks)

**The decision:** whether `SHONEN.md`'s four boxes may be marked `[x]`
(promoted) or stay `[~]`/unmarked.

**What the gates require** (`SHONEN.md:10-11`): `[~]` is asserted by the lane
itself with an evidence pointer; `[x]` requires **a named non-author verifier
per promotion gate**. No box currently carries any mark.

**Evidence for a promotion decision:**

- The only non-author verification pass ever filed is r24's
  (`reports/round-24/promotion-review.md`): boxes 1-4 each
  **verified-with-conditions** by 10+ named non-author swarm seats, 18 traced
  conditions, zero box failures, zero unconditional verifies.
- The regimen's subsequent evidence (r25-r31) strengthened every box's
  substance: register program r26→r30, law gate 10/10 in the battery, the r31
  final sweep 50/50 green + 13 filed-red controls at their codes, the closure
  ledger 32/32 rounds / 22/22 commit-ancestor-valid, the jin'i-ryu falsifiable
  self-check. Full per-box state at HEAD: `dossier-d11-shonen-boxes.md`
  (this round).
- **What is still unmet for `[x]`:**
  1. The r24 conditions that remain open at HEAD, re-confirmed by this round's
     byte checks: box-1 conditions 2/3/4 (three citation-level defects:
     `SKILL.md:486/:488` stale loanword-dating pointers; `SKILL.md:501/:128`
     contract-`:183` mis-cite; dangling anchors `TL-01`/`TL-02`/`FIELD_DEFAULTS`
     /`fictional-coordinate`/`descriptive-gloss` — 0 hits in
     `tools/d2-typed-labels.py`, checked 2026-10-18); box-3 N1 (no expected
     -verdict errata for the round-5/6/7 acceptance re-runs), N4/N5/N7.
  2. The post-r24 deltas (Register-craft subsection, register program, closure
     ledger, jin'i-ryu rule) have **never had a non-author promotion-grade
     verification pass** — r24's reviewers verified the r24 tree, not today's.
     Box-1's inventory condition is the exception: closed by r30's landed
     survey and re-verified this round (28/28 at `79fe91d3…`, exit 0).
  3. Box 2's demonstrated chain carries named design debts by design (12 D4
     garment-form holds; empty `head2` proper domain; the RL-3 ceiling
     constraint) — promotion need not clear them, but the marks should be read
     with them on record.

**Options, with what each rests on:**

- **(a) Promote now** — rests on r24's non-author verdicts + the regimen's
  subsequent green evidence; accepts that conditions 1 remain open as recorded
  errata-class debt and that post-r24 deltas were verified only by author-side
  admission runs (`reports/round-{25..31}/validation.json`, all acceptance true)
  plus r29's/r31's independent audits.
- **(b) One bounded condition-clearing pass, then promote** — the open set is
  small and pointer-level: 3 box-1 citation fixes + N1 errata + (optionally)
  N4/N5 wording + a fresh-context pass over the r25-r31 deltas. This is the
  smallest known path to unconditionally-clean `[x]` evidence.
- **(c) Hold** — keep `[~]`; re-run a verify round in a future regimen. Costs:
  the evidence ages; the regimen is closing now.

**What would change the decision:** a non-author verifier naming any box's
substance unverifiable; a control flipping its filed code in the r32 sweep (a
moved filed byte or shared gate — by the sweep's own contract, a named finding,
never silently re-blessed); any new bleed class in an adjacency audit.

## Decision 2 — freshness threshold ratification (the F-claim pause)

**The decision:** ratify, amend, or retire the freshness threshold and the
F-claim pause that has held since round 8.

**Evidence:** freshness was historically the lowest non-retired axis and has
been paused since r8 (operator pause; zero live-fetch axis moves in rounds
9-31 — every round's SCORECARD row reads "pause in force"). The full-regimen
data is in `reports/round-30/loop3-retrospective.md`: comparable raw replay
**147/189 = 0.7778** and **147/192 = 0.765625**, both below the 0.95 threshold
(r30 retrospective audit command
`python3 -B reports/round-30/retrospective-audit-C23-C25.py --numbers --selftest`,
exit 0, 2026-10-18). The retrospective's recommendation is **not to lower 95%**
to fit the result: pilot a settled-tree, pinned full-closure replay over **all
preregistered rows**, 100% accounted coverage, zero unexplained semantic
regressions, with authorized build-change accounting kept separate. The r30
SCORECARD row records this as "the operator's" and r30's admission note
confirms: "the freshness-threshold ruling remains the operator's."

**What would change the decision:** a replay design that makes the denominator
honest at scale (the r30 pilot sketch) — or an operator ruling that the axis
stays retired-with-pause, which is the de facto state.

## Decision 3 — regimen closure bookkeeping

**The decision:** accept the regimen's closing state as recorded.

**The record:** three loops complete. Loop 1 (r8-r16): 7 admitted / 1 rejected
(r11) / 1 operator-skipped (r13). Loop 2 (r17-r24): 6 / 2 (r17, r22) / 0.
Loop 3 (r25-r31): 6 / 0 / 0, with r32 the close. Totals through r31: **20
admitted / 3 rejected / 1 operator-skip across 24 fleet rounds**; the r31
closure ledger audits 32/32 lane rounds with zero missing and 22/22 filed
reports commit-ancestor-valid, two honest findings on record (`reports/round-31/closure-ledger.json`).
Operator amendments 1-6 are logged (`LOG.md:3048,3065,3340,3435`): expand
rounds cancelled, GLM rounds pinned, devin provider for loop 3, grok expand
reaffirmed-skipped, sol→luna preference recorded for any **future** regimen
(closed rounds are never re-dispatched).

**Provider viability readings carried forward** (availability telemetry,
`reports/round-*/telemetry/`): opencode-go and hyper slow per-worker (17-30/64
completions); devin slower but carried heavy seats (24-26/64; telemetry
durability defect fixed by the r30 convention); zai flash and codex
sol/luna the strongest per-seat completion rates (12-20 per 16-32/64 batch);
the devin availability leg itself is documented could-not-evaluate (r29), the
counters that survive being the durable records only.

**What would change the decision:** the r32 completion audit (sibling C-lane)
finding any round's report non-content-valid or any commit-hash citation
non-ancestor — that is exactly what it exists to catch.

## Decision 4 — the open-debt inventory (nothing here blocks closure)

Design and process debts named on the record, owner unassigned (operator's
call: future regimen, manual pass, or accepted-as-recorded):

| debt | on record since | where |
|---|---|---|
| 12 D4 garment-form holds + owed slots | r18 (design debt by design) | `reports/round-24/box2-d4.md:104-108` |
| `head2` empty proper domain | r26 | `reports/round-26/register/` named gaps |
| RL-3 register-lexicon ceiling (constraint, not defect) | r27/r28 | ceilings knowledge entry |
| box-1 citation conditions 2-4 | r24 (re-confirmed r32) | `promotion-review.md:71-88`; D11 |
| cold-run N1/N4/N5/N7 | r24 | `promotion-review.md:176-196`; D11 |
| lore-owned: bilateral read + L0 contract-digest ratification | r8/r15 | L0 queue; handoff contract |
| calibrated numeric rubric undefined | r5 | `SCORECARD.md` header |
| devin availability could-not-evaluate | r29 | `reports/round-29/recount/` |
| r18 D4-adapter baseline supersession semantics (pins green, content ages) | r31 sweep §5 | `final-sweep.md` |

## Method and limits

Sources read: `SHONEN.md`, `PROVINCE.md`, `reports/round-24/promotion-review.md`,
`reports/round-30/loop3-retrospective.md` (via the r30 report + SCORECARD rows),
`reports/round-31/closure-ledger.json`, `reports/round-31/final-sweep.md`,
SCORECARD round tables, LOG.md `:3031-3483`. All byte-level re-measurements are
this seat's, dated 2026-10-18, commands recorded in D11. This dossier exercises
no operator authority: it marks nothing, recommends no option, and its every
"open"/"closed" is either a prior round's filed verdict or a dated command from
this round. The r32 sibling artifacts (completion audit, sweep re-run, counting
validator) were not yet landed at this seat's cut and are cited at their claimed
paths.
