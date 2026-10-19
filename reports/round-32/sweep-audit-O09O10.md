# R32-O09..O10 — final-sweep audit: independent re-runs (sweep auditors x2)

- **Seat:** R32-O09..O10 (sweep auditors x2), round 32 — the regimen's final
  round (operator: loop 3, GLM round 2 of 2).
- **Date:** 2026-10-19 (UTC observation windows; local 2026-10-18 evening).
- **Assignment:** independent re-runs >=10 sweep commands; mismatches =
  findings (`reports/round-32/claims.json`, claim **O** `operability`).
- **Counting command:** `python3 -B reports/round-32/sweep-audit.py` (date
  2026-10-19). Baseline revision
  `17e90b9047b289d7a63180a1dc1bebb074137e29`; lane HEAD at measurement
  `4d500501a286d96f2eea8a6188c649255581301a` (baseline→HEAD adds only the
  round-32 declaration JSON: `claims.json` sha256 `043dcc6c5aa8cc56…`,
  `targets.json` `906c23a2e1dfdbe8…` — no runtime input moved).
- **Full digests:** `sweep-audit-O09.json`
  (`c29c387f66413911…`), `sweep-audit-O10.json` (`7e6aa95e7d3a1ccb…`),
  `sweep-audit-O09O10.json` (combined + cross-checks, `c114f21be4580615…`).
  Audit runner itself: sha256 `ee1f199ff555acfd…`.
- **Writes:** this file + the three JSONs above. No filed round-8..31 byte was
  written; no git commit, no push. The builders' artifacts (their receipt,
  their `final-sweep.md`, the orchestrator's `run-validation.py`) are
  read-only inputs here.

## 0. Verdict

The whole recorded sweep surface — the round-31 final sweep's 50 green-surface
commands + 13 filed-red historical controls (read row-for-row from the filed
round-31 receipt), plus one adopted round-32 row (the r32 validation harness
selftest, `python3 -B reports/round-32/run-validation.py --selftest`, imported
from the builders' receipt) — re-executed as two sequential full passes:

**64 commands x 2 legs = 128 re-executions; 51/51 green exit 0 and 13/13
controls at their filed codes on both legs; zero findings; zero source drift.**
The assignment's >=10 bar is exceeded 12.8x. Every re-execution is individually
dated, timed, and digested in the leg JSONs.

## 1. Method (independent of the round-32 builders' runner)

`sweep-audit.py` is a fresh implementation: it loads the recorded surface from
the filed receipts (no hand-transcribed matrix; the 13 control codes are
cross-checked at load time against the codes recorded in the filed r31
`final-sweep.md` §3 table, disagreement would abort), and executes each command
as `python3 -B <tool> <args>` from the repo root with
`PYTHONDONTWRITEBYTECODE=1`, timeout 240 s, 8 workers. TMPDIR policy per the
round-30/31 runner: `$PWD/.scratch` for scratch legs,
`/var/tmp/kotodama-r32-sweepaudit` for every mirror-safety `replay-frozen.py`
leg (13 controls + 2 green replays + the replay selftest). Two sequential
passes — leg O09 00:55:19–00:55:56Z, leg O10 00:55:56–00:56:34Z — each record
per command: argv, start/finish UTC, seconds, tmpdir, exit code, expected exit,
and SHA-256 of stdout and stderr. A source snapshot over every runtime-input
tree (`tools/`, `examples/`, `corpus/knowledge/`,
`reports/round-26/remainders/`, `reports/round-28/ceiling/`, both frozen
generations replayed) is taken before and after; it did not move
(`source_drift_during_audit: []`), so both passes ran on a byte-identical
runtime-input set.

Provenance note: the tree was not clean at audit start — sibling round-32
seats' untracked artifacts under `reports/round-32/` were landing concurrently.
None of them is a runtime input of the audited commands, and the runtime-input
snapshot above did not move during the audit.

## 2. The audited surface

| id | command | O09 exit | O10 exit | O09 stdout sha256 (16) | digest across legs |
|---|---|---|---|---|---|
| d2-assembly-check | `python3 -B tools/assemble-d2.py --check` | 0 | 0 | `2fa0c8c197459f54` | same |
| d2-assembly-selftest | `python3 -B tools/assemble-d2.py --selftest` | 0 | 0 | `a81294c0347660d9` | same |
| d2-adapter-check | `python3 -B tools/assemble-d2-typed.py --check` | 0 | 0 | `e3b16d3bae56cce5` | same |
| d2-adapter-selftest | `python3 -B tools/assemble-d2-typed.py --selftest` | 0 | 0 | `00303b7724983160` | same |
| d3-assembly-check | `python3 -B tools/assemble-culture-d3.py --check` | 0 | 0 | `e20620fabdf28532` | same |
| d3-assembly-selftest | `python3 -B tools/assemble-culture-d3.py --selftest` | 0 | 0 | `91a0653948d48a10` | same |
| d4-assembly-check | `python3 -B tools/assemble-culture-d4.py --check` | 0 | 0 | `293bf19f7e6e9c70` | same |
| d4-assembly-selftest | `python3 -B tools/assemble-culture-d4.py --selftest` | 0 | 0 | `0182f7178e24616d` | same |
| d4-adapter-check | `python3 -B tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | 0 | 0 | `692d476ad07f1ca6` | same |
| d4-adapter-selftest | `python3 -B tools/assemble-d4-typed.py --selftest` | 0 | 0 | `4945c941cd243734` | same |
| d4-projector-selftest | `python3 -B tools/d2-typed-labels.py --selftest` | 0 | 0 | `9b492600f5627480` | same |
| d4-projector-d2-check | `python3 -B tools/d2-typed-labels.py --check` | 0 | 0 | `17064af53c48304d` | same |
| d4-projector-d4-check | `python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 0 | 0 | `1c8add321259a9f0` | same |
| d4-label-gate | `python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | 0 | 0 | `1c8add321259a9f0` | same |
| d4-assembly-gate | `python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 | `c60820a54742ecaa` | same |
| typed-pipeline-selftest | `python3 -B tools/gates/typed-pipeline-gate.py --selftest` | 0 | 0 | `35b344fce7daa4ed` | same |
| typed-pipeline-generalized-selftest | `python3 -B tools/gates/typed-pipeline-gate.py --selftest-generalized` | 0 | 0 | `4bc6817850c6b6be` | same |
| typed-pipeline-d2 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml` | 0 | 0 | `15cdfbda73cd56cb` | same |
| typed-pipeline-d4 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 | `865bb03e1694dc0f` | same |
| typed-pipeline-d4-typed | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 0 | 0 | `a1c055b6fe994291` | same |
| selftest-naming-collision | `python3 -B tools/gates/naming-collision-gate.py --selftest` | 0 | 0 | `d3566a9cad69f956` | same |
| selftest-phonology-sanity | `python3 -B tools/gates/phonology-sanity-gate.py --selftest` | 0 | 0 | `3e9a1209afa35290` | same |
| selftest-costume-era | `python3 -B tools/gates/costume-era-consistency-gate.py --selftest` | 0 | 0 | `0c2ed631fb5809ad` | same |
| selftest-myth-consistency | `python3 -B tools/gates/myth-consistency-gate.py --selftest` | 0 | 0 | `80e7d9dc86a29cf5` | same |
| selftest-lexicon-coverage | `python3 -B tools/gates/lexicon-coverage-audit.py --selftest` | 0 | 0 | `fd731b1423443238` | same |
| selftest-provenance-audit | `python3 -B tools/gates/provenance-audit.py --selftest` | 0 | 0 | `972306c1269a7914` | same |
| selftest-handoff-packet-check | `python3 -B tools/gates/handoff-packet-check.py --selftest` | 0 | 0 | `be1ef058b2cfc67a` | same |
| argot-selftest | `python3 -B tools/gates/argot-derivation-gate.py --selftest` | 0 | 0 | `ce3a07fdb8155351` | same |
| argot-d4 | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 | `cff8995c0466b096` | same |
| law-selftest | `python3 -B tools/gates/register-law-gate.py --selftest` | 0 | 0 | `8cca1efe9454eed5` | same |
| law-d4-clean | `python3 -B tools/gates/register-law-gate.py --packet examples/culture-d4/packet.d4.yml` | 0 | 0 | `be9e054d7b4e8dd7` | same |
| handoff-v2 | `python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet` | 0 | 0 | `9aa7ea349cd8177f` | same |
| handoff-v2-selftest | `python3 -B tools/exercise-handoff-e2e.py --profile v2 --selftest --quiet` | 0 | 0 | `9aa7ea349cd8177f` | same |
| handoff-v3 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | 0 | 0 | `b4c57165a3bf0545` | same |
| handoff-v3-selftest | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest --quiet` | 0 | 0 | `49110716cba565e0` | same |
| battery | `python3 -B tools/check-gate-battery.py` | 0 | 0 | `ea8e4c483742cb49` | VOLATILE (F1) |
| battery-selftest | `python3 -B tools/check-gate-battery.py --selftest` | 0 | 0 | `1ba4d2a8040dd767` | same |
| craft-selftest | `python3 -B tools/check-craft-exercise.py --selftest` | 0 | 0 | `77d408e10a494fa5` | same |
| craft-exercise | `python3 -B tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 | 0 | `18128adfc703fd26` | same |
| links-selftest | `python3 -B tools/harness/packet_links.py --selftest` | 0 | 0 | `ff9712c316dadd65` | same |
| uncertainty-selftest | `python3 -B tools/harness/packet_uncertainty.py --selftest` | 0 | 0 | `a374464322a4f255` | same |
| coupling-selftest | `python3 -B tools/check-evidence-coupling.py --selftest` | 0 | 0 | `cf62bc50e303b793` | same |
| coupling-d3 | `python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | 0 | `e282a06884980341` | same |
| replay-selftest | `python3 -B tools/replay-frozen.py --selftest` | 0 | 0 | `4d6aaea127ad9973` | same |
| pin-repoint-selftest | `python3 -B reports/round-26/remainders/pin-repoint-check.py --selftest` | 0 | 0 | `522bc4e2e2aac6e4` | VOLATILE (F2) |
| ceiling-selftest | `python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest` | 0 | 0 | `2e044f8d87b154dd` | same |
| ceiling-measure | `python3 -B reports/round-28/ceiling/measure-ceiling.py` | 0 | 0 | `62b19f53bf599d55` | same |
| knowledge-inventory | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 0 | 0 | `38111cbcca965969` | same |
| replay-round-17 | `python3 -B tools/replay-frozen.py reports/round-17/tests/frozen/MANIFEST.tsv` | 0 | 0 | `4d5a7cf1b91c2ab1` | same |
| replay-r31-post | `python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | 0 | 0 | `893d829ec9150389` | same |
| control-round-3 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | 2 | `76c00a6b80d4539a` | same |
| control-round-3-attempt-1 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 2 | 2 | `409db5ab8b68ebc3` | same |
| control-round-11 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | 2 | 2 | `74c9e2972d48224c` | same |
| control-round-18 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv` | 1 | 1 | `bd28f916f9aefacb` | same |
| control-round-18-repin-d2 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | 2 | 2 | `b72737871acd0d72` | same |
| control-round-20-repin-d2 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` | 2 | 2 | `05ce45dea48bb6f6` | same |
| control-round-22-d4-repin | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 2 | 2 | `6a23e0ff0beb4cba` | same |
| control-round-23-repin-d2 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv` | 2 | 2 | `3b73147e42cb5fd5` | same |
| control-round-25-gate-input | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | 2 | 2 | `f4d0c8e155b77f75` | same |
| control-round-26-gate-input | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` | 1 | 1 | `e06e49967c9edef1` | same |
| control-round-26-post-register | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | 1 | 1 | `a5879db3f47def89` | same |
| control-r27-post | `python3 -B tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` | 1 | 1 | `fb811570eb30a511` | same |
| control-r28-post | `python3 -B tools/replay-frozen.py reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` | 1 | 1 | `cbe44cb076d580a2` | same |
| reports/round-32/run-validation.py † | `python3 -B reports/round-32/run-validation.py --selftest` | 0 | 0 | `ca212395c3426f46` | same |

† adopted from the builders' r32 receipt (the round-32 validation harness
selftest — the "plus round 32's own validation harness" addition of claim O;
the orchestrator's full runner `python3 reports/round-32/run-validation.py` is
**not executed by this audit**, so its writes stay the integrating parent's;
its presence and digest at measurement are recorded: sha256 `6fd1b96e682fde67…`).

The 13 controls are the sweep's integrity leg: every replay code equals its
filed code (2,2,2,1,2,2,2,2,2,1,1,1,1) on both legs — a filed-red control
flipping its code would have meant a moved filed byte or shared gate, and none
moved. A reproduced red verdict stays red.

## 3. Findings

**F1 — `battery` stdout is not byte-reproducible (mismatch class: volatile
output; known).** Cross-pass digest mismatch (`expected_cross_pass_volatility`
in the combined JSON, kind `stdout-digest-mismatch-between-passes`); the
recorded diff excerpt shows the only differences are the battery's random
scratch root echoed inside `stdout_head` and wall-clock `seconds` fields. Exit
0 both legs; verdict content identical. This independently reproduces r31 audit
finding F1 and both round validators' `NONDETERMINISTIC_STDOUT` whitelist — a
calibration confirmation, not a new defect.

**F2 — `pin-repoint-selftest` stdout is not byte-reproducible (same class;
known).** Only difference: the embedded `"date"` field. Same disposition as F1.

**F3 — no new findings.** Zero exit mismatches (across legs, across the r31
receipt, across the r32 receipt, across the r32 filed table), zero
non-volatile stdout/stderr digest mismatches, zero source drift, zero controls
off their filed codes. No unexpected reds anywhere.

## 4. Cross-checks (all read-only; pinned digests at comparison time)

- **vs the filed r31 receipt** (`reports/round-31/sweep/sweep-receipt.json`,
  sha256 `38ada3b6b3553131…`, the matrix source): both legs **61/63 of its rows
  byte-match** my measured exit + stdout digest; `battery` +
  `pin-repoint-selftest` digest-only (F1/F2); the adopted r32 row has no r31
  counterpart (recorded `no_receipt_row`); zero mismatches. The r31 sweep
  surface reproduces byte-for-byte across the round boundary — the settled
  tree's runtime inputs are unchanged, exactly as the baseline→HEAD diff
  claims.
- **vs the builders' r32 receipt** (`reports/round-32/sweep/sweep-receipt.json`,
  sha256 at comparison `f7ea154bc51a5cad…`, seat R32-O06..O08): both legs
  **62/64 rows byte-match**; F1/F2 digest-only; zero exit or digest mismatches;
  `audit_only_rows` and `r32_receipt_only_rows` both empty — the two runs
  cover the identical surface. Their three-pass cross-pass determinism claim
  (`digest_equal_across_passes`, exempting the same two rows) is consistent
  with my two-pass reading.
- **vs the builders' filed table** (`reports/round-32/final-sweep.md`, sha256
  at comparison `7dedafb55b0417f4…`): the table's 51 recorded rows (id |
  command | exit | stdout sha16) diffed against my measured rows on both legs
  — **51/51 matched on both legs**, zero exit or digest mismatches, zero rows
  absent. Their filed table is reproduced exactly by independent re-execution.
- **vs the r31 final-sweep.md table codes**: the 13 control codes recorded
  there are asserted equal to the receipt's `expect_exit` values at matrix
  load; they agree.
- **orchestrator-owned counting command** (`python3
  reports/round-32/run-validation.py`): present at measurement (sha256
  `6fd1b96e682fde67…`), **not executed by this audit** (it is the
  orchestrator's claim-counting surface and writes `validation.json`);
  recorded, not run. Its `--selftest` row is covered above (adopted row,
  byte-match).

## 5. The verbatim-table leg — recorded not-executed, with reasons

Five command-shaped lines extract from the builders' `final-sweep.md`; none is
executable by this seat without writing another round-32 seat's artifact:
one prose artifact (embedded backtick), one unparseable line (an apostrophe
inside a shell comment breaks shell tokenization — recorded with the parse
error), and three invocations of round-32-seat runners (`run-sweep.py`,
`run-validation.py`) whose execution would write the builders'/orchestrator's
files. Each is recorded individually with its reason in the combined JSON.
This costs nothing: every command the table records **is** my matrix, and the
table itself is digest-verified in §4. No line of the builders' table exercises
a tree tool outside my audited surface.

## 6. Scope notes — what this seat did not do

- **No filed round-8..31 byte was written**; only the four files named in the
  header were written (plus this report).
- **The round-32 runners were not executed** (`run-sweep.py`,
  `run-validation.py` full form, any freeze script): they are sibling seats'
  artifacts; re-running them would rewrite files this seat does not own.
- **A pin is integrity, never truth.** Digests assert these exact bytes graded
  by these exact tool revisions produced these exact verdicts — nothing about
  design quality or canon. A reproduced red verdict stays red.

## 7. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch    # mirror-safety replay legs: /var/tmp
python3 -B reports/round-32/sweep-audit.py
```

Re-running rewrites only the three audit JSONs (it re-checks the r32 artifacts
present at its own run time and pins their digests). Slowest command this run:
`handoff-v3-selftest` 36.3 s under 16-worker fleet load; the 240 s per-command
timeout was never approached.

## 8. Limits

- Byte-digest stability is asserted between two passes minutes apart on one
  machine and one runtime-input state; it is not a cross-platform
  determinism claim.
- The audit raced the builders' artifact landing three times (their receipt
  and table re-landed at 21:44, 21:49–21:50 and 21:51–21:53 local while this
  audit iterated); every cross-check pins the exact digest it compared
  against, and all three pins still match the files on disk at filing time —
  the numbers above describe one consistent snapshot
  (receipt `f7ea154b…`, table `7dedafb5…`, runner `6fd1b96e…`).
- The harness selftest row is audited as one more green row; the full
  round-validation run behind it is the orchestrator's to count and is not
  re-judged here.
