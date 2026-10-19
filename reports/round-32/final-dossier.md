# kotodama-shokunin — Round 32 final dossier (the regimen's close)

- **Round:** 32, the regimen's final round (operator: loop 3, GLM round 2 of 2;
  16 workers on zai-coding-plan/glm-5.3-flash-low, host-pinned MAX effort).
  Claim **D** / depth per `reports/round-32/claims.json` ("the dossier claims no
  promotion, it IS the decision's evidence").
- **Date:** 2026-10-18. Declared baseline
  `17e90b9047b289d7a63180a1dc1bebb074137e29`; lane HEAD at this dossier's
  evidence cut `4d50050` ("round-32: declare THE FINAL ROUND claims C/O/D").
- **Assembled by:** the D-lane seats D11/D12/D13; each fragment is filed beside
  this file and stands on its own:
  `dossier-d11-shonen-boxes.md` (§1),
  `dossier-d12-capability-inventory.md` (§2),
  `dossier-d13-operator-decisions.md` (§3).
- **Non-author declaration:** the D-lane seats authored none of the lane's
  artifacts before this round; everything cited was authored by other
  seats/rounds. **No promotion, canon, clearance, or closure verdict is claimed
  here.** No git commit/push; no filed round-8..31 byte written.
- **Evidence cut:** the sibling r32 artifacts — the completion audit
  (`completion-audit.md`, C-lane), the final sweep re-run (`reports/round-32/`
  O-lane), and the counting validator (`run-validation.py`) — were **not yet
  landed** when this dossier's byte checks ran (2026-10-18); they are cited at
  their claimed paths, not executed by the D-lane. Their landing is part of the
  same integration pass that admits this round.
- **Dated addendum (this seat's final read, 2026-10-18, later the same
  evening):** the sibling artifacts have now landed — `completion-audit.md`
  (audited 2026-10-18T21:40:13-03:00, lane HEAD `4d50050`; per-round table
  8-31 with r11/r17/r22 closed-rejected, r13 operator-skipped, r23
  closed-with-finding — matching this dossier's §1/§3 record),
  `completion-ledger.json`, `run-validation.py`, `scope.md`,
  `sweep/run-sweep.py` + `sweep-audit*.json`, and `telemetry/`. The sweep
  receipt (`sweep/sweep-receipt.json`) was **not yet filed** at this read; the
  sweep verdict belongs to its O-lane owners. This dossier cites the audit's
  headline without re-adjudicating it; the D-lane executed no sibling runner
  (it writes `validation.json`, not a D-lane file).

## §1 — the SHONEN boxes, re-surveyed post-Register-craft (D11)

Survey lineage: r23 survey → r24 non-author promotion review (all four boxes
verified-with-conditions) → r30 Register-craft landing + box-1 re-survey →
this final re-survey, which re-measured every open r24 condition at HEAD with
dated commands.

| box | r24 verdict | post-r24 delta | open at HEAD (2026-10-18) |
|---|---|---|---|
| 1 — decision tables, error patterns, checklists, cited sources | verified-with-conditions | Register-craft subsection landed (r30); **inventory condition CLOSED** — 28/28 named executables resolve, re-verified this round: `python3 -B reports/round-30/craft/box1-survey.py` exit 0 at SKILL sha `79fe91d3…` | conditions 2/3/4 — citation-level, re-confirmed: `SKILL.md:486/:488` stale loanword pointers (content at corpus `:63`/`:59`); `SKILL.md:501/:128` contract-`:183` mis-cite; `TL-01`/`TL-02`/`FIELD_DEFAULTS`/`fictional-coordinate`/`descriptive-gloss` = 0 hits in `tools/d2-typed-labels.py`. Condition 5 (duplicated block) reads closed by re-measurement (1 phrase occurrence) |
| 2 — end-to-end domain task, logged | verified-with-conditions | r24 misquote dispositioned by the r21 recount; register program r26→r30 (stratum → law → replay → QREG fix); chain green in the r31 final sweep (handoff v2/v3, typed-pipeline-d4, argot, law rows all exit 0) | none of the r24 conditions; standing design debts named: 12 D4 garment holds, empty `head2` domain, RL-3 ceiling constraint |
| 3 — executable without oral context | verified-with-conditions | N3 CLOSED (r25 input-class honesty, false red eliminated); N6 CLOSED (`--frozen` named, `SKILL.md:672`); receipt-guard documented (`SKILL.md:453`); r31 final sweep 50/50; jin'i-ryu audit item executable (`SKILL.md:710-715`) | N1 (no expected-verdict errata for round-5/6/7 acceptance re-runs), N4/N5/N7 — as filed, re-checked |
| 4 — no cross-domain bleed; PROVINCE accurate | verified-with-conditions | r21 + r29 consolidated adjacency audits: zero unfiled bleed; **PROVINCE.md byte-identical since `c53782a`** (pre-round-8; `git log -- PROVINCE.md`) | standing readings 3a/3b/3c (by-design interpretations, carried unchanged) |

The marks stay operator-owned (`SHONEN.md:10-11`): `[x]` requires a named
non-author verifier; the only non-author pass on file is r24's, which verified
the r24 tree. Full condition-level detail: `dossier-d11-shonen-boxes.md`.

## §2 — the post-regimen capability inventory (D12)

Base capabilities (rounds 1-supplement..5): structural gates, D2 assembly,
frozen replay, uncertainty inventory, source rechecks, craft exercise, corpus
audit, isolated battery, bounded typed CLI. Regimen addenda, each with its
demonstrated command (all rows exit 0 in the r31 final sweep, 50/50, plus 13
filed-red controls at their codes and battery 10/10):

- **Loop 1 (r8-r16):** `d2-typed-labels` (r8) · D3 admitted (`culture-d3
  -acceptance`, r9) · receipt-guard (r14) · handoff v2 + uncertainty grammar
  (r15) · civ-map 94/94 + validator hardening (r16). Freshness receipts r8/r9,
  paused since.
- **Loop 2 (r17-r24):** `assemble-culture-d4` + `assemble-d4-typed` (r17/r18) ·
  generalized typed-pipeline gate (r18) · handoff v3 with D4 claims (r20) ·
  battery registration of D4 gates (r19) · family-clean rule (r23) · the
  promotion-review dossier + SKILL staleness audit (r24).
- **Loop 3 (r25-r32):** `argot-derivation-check` (r25) · `register-stratum`
  (r26) · `register-law` (r27) · `register-law-replay` (r28, QREG resolved
  r30) · law gate in the battery 10/10 (r30) · Register-craft subsection +
  box-1 inventory closed (r30) · loop-3 retrospective + freshness
  recommendation (r30) · closure ledger + final green sweep (r31) · jin'i-ryu
  closure rule (r31) · r32: this dossier + the completion audit + the sweep
  re-run.

The full table — every capability with its exact demonstrated command — is
`dossier-d12-capability-inventory.md`. Standing limits, restated there: no
calibrated numeric rubric exists (SCORECARD header gap); freshness is paused,
not strong; green is integrity, never canon, clearance, or quality.

## §3 — the operator's decision materials (D13)

Four decisions, each with evidence, options, and falsifiers
(`dossier-d13-operator-decisions.md`):

1. **Promotion (SHONEN marks).** Evidence for: r24's non-author verdicts (all
   four boxes verified-with-conditions) + the regimen's subsequent green
   record. Unmet for `[x]`: box-1 conditions 2-4 and box-3 N1/N4/N5/N7 remain
   open at HEAD (re-confirmed this round), and the post-r24 deltas have had no
   non-author promotion-grade pass. Options: promote on the recorded evidence;
   run one bounded condition-clearing pass (3 citation fixes + N1 errata + a
   fresh-context pass over r25-r31 deltas — the smallest clean path); or hold.
   This dossier takes no option.
2. **Freshness threshold.** Paused since r8; full-regimen replay 147/189 =
   0.7778 and 147/192 = 0.765625, both < 0.95 (`reports/round-30/loop3
   -retrospective.md`, audit exit 0). The retrospective recommends NOT lowering
   95%: pilot a settled-tree pinned full-closure replay over all preregistered
   rows with build-change accounting separate. Ruling stays the operator's.
3. **Regimen closure bookkeeping.** Three loops complete: 7/1/1, 6/2/0, 6/0/0
   (+ r32 closing) = **20 admitted / 3 rejected / 1 operator-skip through r31**;
   closure ledger audits 32/32 rounds, 22/22 commit-ancestor-valid, two honest
   findings. Amendments 1-6 logged (grok skipped; sol→luna recorded for future
   regimens only). The r32 completion audit is the remaining gate.
4. **Open debts (nothing blocks closure).** Twelve named items tabled with
   origins and pointers — design debts (12 garment holds, head2, RL-3),
   the r24 citation/cold-run conditions, lore-owned items, the rubric gap,
   devin-telemetry could-not-evaluate, adapter-baseline supersession semantics.

## §4 — method, cut, and limits

Read in full: `SHONEN.md`, `PROVINCE.md`, `reports/round-24/promotion-review.md`,
`reports/round-31/final-sweep.md`, `reports/round-31/closure-ledger.json`,
`reports/round-32/claims.json`, SCORECARD round tables 5-31, LOG.md
`:3031-3483`, `reports/round-23/shonen-survey.md`. This round's own
measurements (all 2026-10-18, all inside the lane, commands recorded in the
fragments): the box-1 survey re-run (exit 0, 28/28), the loanword/contract line
checks, the anchor grep (0 hits), the status-phrase census (1 hit), `git log`
probes on `PROVINCE.md`/`SKILL.md`/the two corpus files. The D-lane re-graded
nothing it did not measure; verdicts are quoted as filed. NON-CANON engineering
evidence throughout: a pin is integrity, never truth; a reproduced red stays
red; lore owns canon (`PROVINCE.md`).

## Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
python3 -B reports/round-30/craft/box1-survey.py        # 28/28 named executables resolve; exit 0
git log --oneline -- PROVINCE.md                        # last touch: c53782a (pre-round-8)
sha256sum SKILL.md                                      # 79fe91d3… (HEAD bytes this dossier cites)
python3 reports/round-31/run-validation.py              # the r31 counting command (acceptance true, filed)
python3 reports/round-32/run-validation.py              # the r32 counting command (sibling-owned; this dossier's claim-D runner)
```
