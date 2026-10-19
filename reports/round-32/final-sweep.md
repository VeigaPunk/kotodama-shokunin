# R32-O06..O08 — the final sweep, three passes over the settled tree

- **Seat:** R32-O06..O08 (round-32 final-sweep seat), round 32 (the regimen's final round), claim **O**
  `operability` (`reports/round-32/claims.json`).
- **Date:** 2026-10-18. Declared baseline revision
  `17e90b9047b289d7a63180a1dc1bebb074137e29` (round-32 declare); lane HEAD at
  measurement `4d500501a286d96f2eea8a6188c649255581301a`.
- **Writes:** `reports/round-32/sweep/` (the runner, per-pass receipts, the
  consolidated receipt, `commands.txt`) and this file. No filed round-8..31
  byte was written; no git commit, no push.
- **Canon:** NON-CANON engineering evidence. A pin is integrity, never truth
  and never clearance; a reproduced red verdict stays red.
- **Matrix provenance:** the 50-command matrix is imported by `runpy` from
  `reports/round-31/sweep/run-sweep.py` (the filed r31 bytes) — not copied — so it cannot drift.
- Machine receipts: per-pass `reports/round-32/sweep/receipt-*.json`;
  consolidated `reports/round-32/sweep/sweep-receipt.json`; flat manifest
  `commands.txt`.

## 0. Verdict

Three back-to-back full passes over the settled tree:
**51 green rows per pass — the r31 sweep's
50-command matrix plus round 32's own harness selftest (harness selftest green) —
all exit 0 (100%) in every pass**; **13
historical controls at their expected filed-red codes in every pass**;
runtime inputs unchanged during every pass. The gate battery reads
**10/10** (pinned 20,
uncovered none), law findings on the current packet:
0, and both current frozen generations replay
OK (r17: REPLAY OK: 5/5 rows reproduced the recorded verdicts (reproduction only: a reproduced red verdict stays red);
r31-post: REPLAY OK: 4/4 rows reproduced the recorded verdicts (reproduction only: a reproduced red verdict stays red)).

Cross-pass determinism, measured (not asserted): **64 rows
compared across the three passes; exits equal in
all passes**;
**62/64 rows
byte-identical** — the exceptions are the rows that embed run-stamps by
design (battery: 3 distinct digests over 3 passes; pin-repoint-selftest: 3 distinct digests over 3 passes);
their exits and semantic counters are the stable reading.

no unexpected variance.
Harness bytes across passes:
stable — all three passes exercised sha 6fd1b96e682fde67.

Claim-O counting command: `python3 reports/round-32/run-validation.py` (the
round runner, orchestrator-owned).

## 1. The consolidated sweep table (final pass: O08)

Every green row: the command exactly as re-runnable, its exit code, and the
SHA-256 of its stdout at the recorded stamp (final pass; the per-pass receipts
carry all three passes' digests). Re-run them from `commands.txt` alone.

| id | family | command | exit | stdout sha256 (first 16) |
|---|---|---|---:|---|
| d2-assembly-check | assemblers | `python3 -B tools/assemble-d2.py --check` | 0 | `2fa0c8c197459f54…` |
| d2-assembly-selftest | assemblers | `python3 -B tools/assemble-d2.py --selftest` | 0 | `a81294c0347660d9…` |
| d2-adapter-check | assemblers | `python3 -B tools/assemble-d2-typed.py --check` | 0 | `e3b16d3bae56cce5…` |
| d2-adapter-selftest | assemblers | `python3 -B tools/assemble-d2-typed.py --selftest` | 0 | `00303b7724983160…` |
| d3-assembly-check | assemblers | `python3 -B tools/assemble-culture-d3.py --check` | 0 | `e20620fabdf28532…` |
| d3-assembly-selftest | assemblers | `python3 -B tools/assemble-culture-d3.py --selftest` | 0 | `91a0653948d48a10…` |
| d4-assembly-check | assemblers | `python3 -B tools/assemble-culture-d4.py --check` | 0 | `293bf19f7e6e9c70…` |
| d4-assembly-selftest | assemblers | `python3 -B tools/assemble-culture-d4.py --selftest` | 0 | `0182f7178e24616d…` |
| d4-adapter-check | assemblers | `python3 -B tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | 0 | `692d476ad07f1ca6…` |
| d4-adapter-selftest | assemblers | `python3 -B tools/assemble-d4-typed.py --selftest` | 0 | `4945c941cd243734…` |
| d4-projector-selftest | assemblers | `python3 -B tools/d2-typed-labels.py --selftest` | 0 | `9b492600f5627480…` |
| d4-projector-d2-check | assemblers | `python3 -B tools/d2-typed-labels.py --check` | 0 | `17064af53c48304d…` |
| d4-projector-d4-check | assemblers | `python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 0 | `1c8add321259a9f0…` |
| d4-label-gate | typed-gates | `python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | 0 | `1c8add321259a9f0…` |
| d4-assembly-gate | typed-gates | `python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | `c60820a54742ecaa…` |
| typed-pipeline-selftest | typed-gates | `python3 -B tools/gates/typed-pipeline-gate.py --selftest` | 0 | `35b344fce7daa4ed…` |
| typed-pipeline-generalized-selftest | typed-gates | `python3 -B tools/gates/typed-pipeline-gate.py --selftest-generalized` | 0 | `4bc6817850c6b6be…` |
| typed-pipeline-d2 | typed-gates | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml` | 0 | `15cdfbda73cd56cb…` |
| typed-pipeline-d4 | typed-gates | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | `865bb03e1694dc0f…` |
| typed-pipeline-d4-typed | typed-gates | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 0 | `a1c055b6fe994291…` |
| selftest-naming-collision | gate-selftests | `python3 -B tools/gates/naming-collision-gate.py --selftest` | 0 | `d3566a9cad69f956…` |
| selftest-phonology-sanity | gate-selftests | `python3 -B tools/gates/phonology-sanity-gate.py --selftest` | 0 | `3e9a1209afa35290…` |
| selftest-costume-era | gate-selftests | `python3 -B tools/gates/costume-era-consistency-gate.py --selftest` | 0 | `0c2ed631fb5809ad…` |
| selftest-myth-consistency | gate-selftests | `python3 -B tools/gates/myth-consistency-gate.py --selftest` | 0 | `80e7d9dc86a29cf5…` |
| selftest-lexicon-coverage | gate-selftests | `python3 -B tools/gates/lexicon-coverage-audit.py --selftest` | 0 | `fd731b1423443238…` |
| selftest-provenance-audit | gate-selftests | `python3 -B tools/gates/provenance-audit.py --selftest` | 0 | `972306c1269a7914…` |
| selftest-handoff-packet-check | gate-selftests | `python3 -B tools/gates/handoff-packet-check.py --selftest` | 0 | `be1ef058b2cfc67a…` |
| argot-selftest | argot-law | `python3 -B tools/gates/argot-derivation-gate.py --selftest` | 0 | `ce3a07fdb8155351…` |
| argot-d4 | argot-law | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | `cff8995c0466b096…` |
| law-selftest | argot-law | `python3 -B tools/gates/register-law-gate.py --selftest` | 0 | `8cca1efe9454eed5…` |
| law-d4-clean | argot-law | `python3 -B tools/gates/register-law-gate.py --packet examples/culture-d4/packet.d4.yml` | 0 | `be9e054d7b4e8dd7…` |
| handoff-v2 | handoff | `python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet` | 0 | `9aa7ea349cd8177f…` |
| handoff-v2-selftest | handoff | `python3 -B tools/exercise-handoff-e2e.py --profile v2 --selftest --quiet` | 0 | `9aa7ea349cd8177f…` |
| handoff-v3 | handoff | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | 0 | `b4c57165a3bf0545…` |
| handoff-v3-selftest | handoff | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest --quiet` | 0 | `49110716cba565e0…` |
| battery | battery | `python3 -B tools/check-gate-battery.py` | 0 | `a66a3ef36446473b…` |
| battery-selftest | battery | `python3 -B tools/check-gate-battery.py --selftest` | 0 | `1ba4d2a8040dd767…` |
| craft-selftest | craft | `python3 -B tools/check-craft-exercise.py --selftest` | 0 | `77d408e10a494fa5…` |
| craft-exercise | craft | `python3 -B tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 | `18128adfc703fd26…` |
| links-selftest | validators | `python3 -B tools/harness/packet_links.py --selftest` | 0 | `ff9712c316dadd65…` |
| uncertainty-selftest | validators | `python3 -B tools/harness/packet_uncertainty.py --selftest` | 0 | `a374464322a4f255…` |
| coupling-selftest | validators | `python3 -B tools/check-evidence-coupling.py --selftest` | 0 | `cf62bc50e303b793…` |
| coupling-d3 | validators | `python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | `e282a06884980341…` |
| replay-selftest | validators | `python3 -B tools/replay-frozen.py --selftest` | 0 | `4d6aaea127ad9973…` |
| pin-repoint-selftest | validators | `python3 -B reports/round-26/remainders/pin-repoint-check.py --selftest` | 0 | `18341cd72cc4dc07…` |
| ceiling-selftest | validators | `python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest` | 0 | `2e044f8d87b154dd…` |
| ceiling-measure | validators | `python3 -B reports/round-28/ceiling/measure-ceiling.py` | 0 | `62b19f53bf599d55…` |
| knowledge-inventory | validators | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 0 | `38111cbcca965969…` |
| replay-round-17 | frozen-replays | `python3 -B tools/replay-frozen.py reports/round-17/tests/frozen/MANIFEST.tsv` | 0 | `4d5a7cf1b91c2ab1…` |
| replay-r31-post | frozen-replays | `python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | 0 | `893d829ec9150389…` |
| reports/round-32/run-validation.py | r32-harness | `python3 -B reports/round-32/run-validation.py --selftest` | 0 | `ca212395c3426f46…` |

Key readings carried in the receipt (`extras` per row): the battery row's
coverage/pin counters and registered-gate list (§2), the law row's finding
count, each handoff row's summary line, each replay row's REPLAY summary, and
the harness row's selftest counters.
stderr was empty (0 bytes total across
all green rows of the final pass).

**Pass ledger:** O06 2026-10-19T00:57:15+00:00→2026-10-19T00:58:24+00:00, O07 2026-10-19T00:58:24+00:00→2026-10-19T00:59:36+00:00, O08 2026-10-19T00:59:36+00:00→2026-10-19T01:00:49+00:00
(UTC). Per-pass receipts: `reports/round-32/sweep/receipt-O06.json`, `reports/round-32/sweep/receipt-O07.json`, `reports/round-32/sweep/receipt-O08.json`.

## 2. The battery reading (claim: 10/10)

`python3 -B tools/check-gate-battery.py` over the default roots
(`tools/gates/expected`, `tools/gates/frozen`, `reports/round-9/baselines`):
coverage **10/10**, pinned
20/20,
uncovered none, exit
0. Registered gates
(10):

- `costume-era-consistency-gate.py`
- `handoff-packet-check.py`
- `lexicon-coverage-audit.py`
- `myth-consistency-gate.py`
- `naming-collision-gate.py`
- `phonology-sanity-gate.py`
- `provenance-audit.py`
- `d4-typed-labels-check-gate.py`
- `d4-assembly-check-gate.py`
- `register-law-gate.py`

The battery's own selftest row (`battery-selftest`) is green in §1. The law
baseline pinning the settled round-30 packet lives at
`tools/gates/expected/register-law-gate/r30-post/` (round-30 integration).

## 3. The frozen-replay leg: two current generations, thirteen filed controls

The current generations are unchanged from round 31:
`reports/round-31/sweep/frozen/r31-post` (frozen at revision
`e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c`) and `reports/round-17/tests/frozen`. This seat
froze no new generation — the settled tree re-played the filed ones green, so
a new freeze would have asserted nothing new (append-only: freezing a
duplicate generation is not this seat's call).

| control (filed generation) | replay exit | expected | disposition |
|---|---:|---:|---|
| `tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | 2 | legacy refusal era: rows could-not-evaluate at their filed bytes |
| `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 2 | 2 | legacy refusal era: rows could-not-evaluate at their filed bytes |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | 2 | 2 | one row could-not-evaluate (replay precedence); the rest reproduce their recorded reds |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 1 | 1 | two rows mismatch: superseded by later D4 landings (recorded reds stay red) |
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | 2 | 2 | one row could-not-evaluate; the rest reproduce |
| `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` | 2 | 2 | one row could-not-evaluate; the rest reproduce |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 2 | 2 | D4-leg rows superseded by the amended packet (r28 sweep §3) |
| `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv` | 2 | 2 | one row could-not-evaluate; the rest reproduce |
| `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | 2 | 2 | six rows could-not-evaluate at their filed bytes |
| `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` | 1 | 1 | D4 rows superseded by post-r28 gate/packet movement |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | 1 | 1 | superseded when the register law moved the D4 tree after its freeze (r27/r28) |
| `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` | 1 | 1 | superseded by the RL-4 packet_keys landing (r28 sweep §2.1) |
| `reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` | 1 | 1 | superseded 4/4 by the r30 QREG landing; successor is sweep/frozen/r31-post |

The controls are the sweep's integrity leg, not failures: filed bytes are
immutable, so each replay code is deterministic. A control flipping its code
means a filed byte or a shared gate moved — a named finding for disposition,
never silently re-blessed. Their red verdicts stay red; reproduction is not
clearance.

## 4. The TMPDIR boundary (measured, inherited)

`tools/replay-frozen.py` refuses a mirror whose real path is inside the repo —
the designed boundary (r28 sweep §5). This sweep keeps the round-30/31
runner's policy: `.scratch` for scratch-writing legs,
`/var/tmp/kotodama-r32-sweep` for every mirror-safety replay leg. The
fleet-shared `/tmp` quota trap of round 28 is avoided by never using it.

## 5. Scope notes — what this seat did not do

- **No filed round-8..31 byte was written.** Everything new lives under
  `reports/round-32/sweep/` plus this file.
- **No new frozen generation.** The filed r31-post and round-17 generations
  replayed green on the settled tree; a new freeze is not this seat's surface.
- **The r32 validation harness is a sibling's/orchestrator's artifact.** This
  seat only exercises its selftest (`reports/round-32/run-validation.py
  --selftest`) as the added 51st green row; harness selftest green.
- **A pin is integrity, never truth.** The filed generations assert these
  exact bytes graded by these exact gate revisions produced these exact
  verdicts — nothing about design quality or canon.

## 6. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch    # scratch-writing legs (mirror-safety legs: /var/tmp)

python3 reports/round-32/sweep/run-sweep.py --selftest   # the runner's own controls
python3 reports/round-32/sweep/run-sweep.py --check      # receipt JSON without writing
python3 reports/round-32/sweep/run-sweep.py              # 3 passes + receipts + this table
python3 reports/round-32/run-validation.py               # claim-O counting command (orchestrator-owned)
```

`commands.txt` carries every green-surface command one per line, in manifest
order — the sweep is re-runnable from the recorded commands alone.

Receipt: `reports/round-32/sweep/sweep-receipt.json` (sha256
`864b2859b507c776…`). `reports/round-32/claims.json` digest at measurement:
`043dcc6c5aa8cc56…`.
