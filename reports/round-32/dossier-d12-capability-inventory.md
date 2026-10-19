# R32-D12 — post-regimen capability inventory (every SCORECARD capability + demonstrated command)

- **Seat:** D12 (dossier leg 2 of 3), round 32 — the regimen's final round.
  Claim **D** / depth, `reports/round-32/claims.json`.
- **Date:** 2026-10-18. Declared baseline
  `17e90b9047b289d7a63180a1dc1bebb074137e29`; lane HEAD at evidence cut `4d50050`.
- **Non-author declaration:** this seat authored none of the cited artifacts.
  **Write scope:** this file only. No git commit/push, no edits to filed
  rounds 8-31. Scratch: `TMPDIR=$PWD/.scratch`.
- **Canon:** NON-CANON engineering evidence. "Demonstrated" means: the command
  was executed green against the pinned tree in the r31 final sweep (every row
  re-executed, exits and stdout digests receipted in
  `reports/round-31/sweep/sweep-receipt.json`) and, where noted, re-executed by
  this seat. A green row is integrity and executability — never canon, truth,
  cultural clearance, or a quality score.

## 1. Inventory source and counting

Capabilities are the SCORECARD record: the base `## Capabilities` table (nine
rows, first working rounds 1-supplement through 5) plus the per-round
capabilities addenda (r7-r9, r14, r17-r20, r25-r28, r30-r31). Demonstrated
commands come from the r31 final green sweep — one deterministic pass over the
whole surface: **50 green rows, all exit 0 (100%); 13 filed-red historical
controls at their expected codes; battery 10/10** (`reports/round-31/final-sweep.md`,
2026-10-18; counting command of record:
`python3 reports/round-31/run-validation.py`, exit 0, receipt
`reports/round-31/validation.json`). Round 32's O-sweep re-runs the same matrix
over the settled tree (sibling-owned; in flight at this seat's cut).

## 2. The capability inventory

| capability (first working) | demonstrates | demonstrated command (exit 0, r31 sweep row) |
|---|---|---|
| structural domain checks (r1; handoff r2) | phonology, lexicon, myth, costume, naming, provenance verdicts on supplied inputs | `python3 -B tools/gates/naming-collision-gate.py --selftest` (and the other six `--selftest` rows) |
| reproducible culture assembly — D2 (r3) | source-hash-pinned D2 packet, byte-identical regeneration, positive/negative controls | `python3 -B tools/assemble-d2.py --check` · `--selftest` |
| reproducible culture assembly — D3 (admitted r9) | deterministic NON-CANON two-era D3 packet + evidence coupling | `python3 -B tools/assemble-culture-d3.py --check` · `--selftest`; `python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json` |
| reproducible culture assembly — D4 (r17/r18) | first culture with derivations; D4 packet + typed adapter (text-transform architecture) | `python3 -B tools/assemble-culture-d4.py --check` · `--selftest`; `python3 -B tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` · `--selftest` |
| d2-typed-labels (r8) | five-kind label typing by declaration, holds, borrow-ledger clocks, channel separation, typed projection | `python3 -B tools/d2-typed-labels.py --selftest`; `--check`; D4 packet check |
| typed pipeline gate, generalized (r11 → r18) | one gate, declared-assembler identity; D2 byte-identical default; D4 19/19 with findings == expected hold set | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml`; `examples/culture-d4/packet.d4.yml`; `packet.d4.typed.yml`; both selftests |
| frozen verdict replay (supplement-opencode-1) | snapshot/gate/output digests verified before re-execution; a reproduced red stays red | `python3 -B tools/replay-frozen.py --selftest`; `reports/round-17/tests/frozen/MANIFEST.tsv`; `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` (4/4) |
| uncertainty inventory (supplement-opencode-1) | deterministic lines/occurrences/marker inventory; never scholarship certification | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (179 entries, partitions 16/16/16/24/13/94) |
| contrastive craft exercise (supplement-opencode-1) | sound law vs register-limited avoidance vs borrowed garment strata, two eras; bounded typed CLI (exit-2 malformed class) | `python3 -B tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` · `--selftest` |
| isolated gate battery (r5 → 10/10 in r30) | copied-tree runner, stable failure/could-not-evaluate mapping, registered gates + pinned baselines | `python3 -B tools/check-gate-battery.py` (10/10 coverage, 20/20 pinned) · `--selftest` |
| receipt guard (r14) | committed-receipt overwrites refused without `REFRESH_RECEIPTS=1`; catches the r8/r9 clobber class | `python3 -B tools/harness/receipt_guard.py --selftest`; SKILL row `SKILL.md:453` |
| handoff e2e v2/v3 (r15/r20) | 16/16 + 20/20 envelope, claim-uncertainty grammar, claim-to-record links resolving, D4 claims | `python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet` · `--profile v3 --quiet` (+ both selftests) |
| argot-derivation-check (r25) | derivation replay for register-scoped forms; D4L-ARGOT-DERV finding class; real negatives | `python3 -B tools/gates/argot-derivation-gate.py --selftest`; `examples/culture-d4/packet.d4.yml` |
| register-stratum (r26) | the r17 forecast closed: 8 verified register forms, axis-to-operation rule (mark→reverse, fire→lengthen), derivation replay clean | `python3 reports/round-26/run-validation.py` (acceptance, exit 0); register rows in the D4 packet |
| register-law (r27) | RGL-01..05 law block; A/B route chosen by measured holds (0 new holds) | `python3 -B tools/gates/register-law-gate.py --selftest`; `--packet examples/culture-d4/packet.d4.yml` (0 findings on the settled packet) |
| register-law-replay (r28, resolved r30) | six D4L-LAW-* classes; substring trap designed out; surfaced 4 real dangling-design defects (QREG-05..08, fixed r30) | same law-gate rows + `tools/gates/expected/register-law-gate/r30-post/` baseline (battery row 10/10) |
| pin-repoint discipline (r23/r26) | stale rows replay red, new rows green, filed rows untouched | `python3 -B reports/round-26/remainders/pin-repoint-check.py --selftest` |
| ceiling measurement (r28) | the RL-3 register-lexicon ceiling recorded as a sourced constraint | `python3 -B reports/round-28/ceiling/measure-ceiling.py` · `--selftest` |
| packet validators (r15/r16) | link coverage, L-anchor collision, edge-source validation, uncertainty grammar | `python3 -B tools/harness/packet_links.py --selftest`; `python3 -B tools/harness/packet_uncertainty.py --selftest` |
| closure ledger (r31) | 32/32 lane rounds audited, 22/22 filed reports commit-ancestor-valid, two honest findings | `reports/round-31/closure-ledger.json`; `python3 reports/round-31/run-validation.py` |
| final green sweep (r31) | the whole surface in one deterministic pass + 13 filed-red controls at their codes | `python3 reports/round-31/sweep/run-sweep.py` (receipt `sweep/sweep-receipt.json`; commands alone in `sweep/commands.txt`) |
| jin'i-ryu closure rule (r31) | telemetry records filed open get append-only closing snapshots; audit leg falsifiable | checklist one-liner at `SKILL.md:710-715`; `reports/round-31/jinii/`; five snapshots under `reports/round-{19,25,26,27,28}/telemetry/` |
| historical source rechecks (supplement; r5+) | per-claim retrieved passages, access limits, contradictions; conservative reconciliation | `corpus/lessons/round-5-sources/`; `reports/round-{5,6,8,9}/freshness|parent-*` (freshness axis paused since r8) |
| corpus apparatus audit (r4) | declared metadata + ledger scope inspected without equating to truth | `corpus/lessons/round-4-audit/` (16 reports) |

## 3. Genealogy (one line per regimen loop)

- **Before the regimen (rounds 1-supplement..7):** six structural gates, D2
  assembly + replay, uncertainty inventory, craft exercise, battery, bounded
  typed CLI, handoff envelope; D3 attempted at r7 (closed failed, admitted r9).
- **Loop 1 (r8-r16):** d2-typed-labels; D3 admitted; freshness receipts
  (15+4 rows, then paused); receipt guard; handoff v2 + uncertainty grammar;
  civ-map 94/94; validator hardening (edge-source, L-anchors, link coverage).
- **Loop 2 (r17-r24):** D4 assembler + typed adapter; generalized typed
  pipeline; handoff v3 with D4 claims; family-clean projection rule; battery
  registration of D4 gates; the promotion-review dossier (non-author box
  verdicts) and the SKILL staleness audit.
- **Loop 3 (r25-r32):** argot leg; register stratum; register law; law replay
  (+ QREG fix); 24-entry defect queue resolved; Register-craft subsection +
  box-1 inventory closed; loop-3 retrospective + freshness recommendation;
  closure ledger + final sweep; jin'i-ryu closure rule; r32 = this dossier, the
  completion audit, and the final sweep re-run.

## 4. What this inventory does not claim

- **No calibrated numeric rubric exists.** The SCORECARD header's explicit
  protocol-conformance gap stands: verdicts and checkable observations, not
  scores; a raw file or marker count is not a quality score.
- **Freshness is paused, not strong.** The axis has not moved since r8/r9
  (operator pause); the threshold question is restated with a recommendation in
  `reports/round-30/loop3-retrospective.md` and stays operator-owned (D13).
- **Green ≠ canon or clearance.** Every replayed red control stays red; pins are
  integrity; lore owns canon; the lane hands off, never records canon
  (`PROVINCE.md`).
- **Provider/telemetry counts are not capability.** The devin availability leg
  is documented could-not-evaluate with durable records (r29); completion rates
  stay unlaimed where telemetry is lost.

## Method and limits

Sources read: SCORECARD base Capabilities table + addenda rows r7-r31
(`SCORECARD.md`), `reports/round-31/final-sweep.md` §1-§3 (commands copied
verbatim from the 50-row table), `reports/round-30/craft/box1-landed-survey.json`
+ this round's D11 re-run (28/28 at `79fe91d3…`), LOG.md `:3348-3483`. Commands
were not all re-executed by this seat — the r31 sweep receipt (sha
`38ada3b6b3553131…`) is the execution record of record, and r32's O-lane owns
the re-run; this seat re-executed only the box-1 survey and byte-level greps
recorded in D11. First-working attributions follow the SCORECARD rows; where a
capability was rejected-then-admitted (D3 at r7→r9; D4 at r17→r18) both rounds
are named.
