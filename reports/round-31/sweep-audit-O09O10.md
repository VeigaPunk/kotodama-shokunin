# R31-O09..O10 — final-sweep audit: independent re-run (sweep auditors x2)

- **Seat:** R31-O09..O10 (sweep auditors x2)
- **Date:** 2026-10-18
- **Assignment:** independent re-run of >=10 sweep commands; mismatches = findings
- **Counting command:** `python3 -B reports/round-31/sweep-audit.py` (date 2026-10-18)
- **Baseline revision:** `71cd9d376ebd144e94e4f12d997f73e5d2839aa9`; **lane HEAD at audit:** `e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c` (baseline→HEAD adds only round-31 declaration JSON: `git diff --stat 71cd9d3..e8d2d0d` = `reports/round-31/claims.json`, `reports/round-31/targets.json`)
- **Full digests:** `reports/round-31/sweep-audit-O09.json`, `reports/round-31/sweep-audit-O10.json` (per-leg), `reports/round-31/sweep-audit-O09O10.json` (combined + cross-pass)

## Method (independent of the round-30 runner)

`sweep-audit.py` is a fresh implementation, not an import of
`reports/round-30/verify-operability.py`. It re-declares the recorded sweep
surface — the 40 current-tree commands of the round-30 REGRESSIONS matrix plus
its `--selftest-generalized` addition — and executes each command as
`python3 -B <tool> <args>` from the repo root with `PYTHONDONTWRITEBYTECODE=1`
and `TMPDIR=$PWD/.scratch`, except the two recorded external-tmp legs
(`frozen-replay-selftest`, `r28-sweep-selftest`) which get `/var/tmp`
(mirror-safety legs), timeout 240 s per command. Two sequential full passes
(leg O09 22:51:16–22:51:54Z, leg O10 22:51:54–22:52:35Z, third post-fix set
filed) each record per command: argv, start/finish UTC, seconds, tmpdir, exit
code, and SHA-256 of stdout and stderr. A source snapshot over every tool,
fixture packet and audited-input file is taken before and after; it did not
move (`source_drift_during_audit: []` in the combined JSON), so both passes
ran on a byte-identical tree.

## Result: 40/40 exit 0 on both legs

| command | O09 exit | O10 exit | O09 stdout sha256 (16) | digest across legs |
|---|---|---|---|---|
| python3 -B tools/check-gate-battery.py --selftest | 0 | 0 | `1ba4d2a8040dd767` | same |
| python3 -B tools/check-gate-battery.py | 0 | 0 | `44ed05a811efe245` | VOLATILE (F1) |
| python3 -B tools/check-craft-exercise.py --selftest | 0 | 0 | `77d408e10a494fa5` | same |
| python3 -B tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json | 0 | 0 | `18128adfc703fd26` | same |
| python3 -B tools/harness/packet_links.py --selftest | 0 | 0 | `ff9712c316dadd65` | same |
| python3 -B tools/harness/packet_uncertainty.py --selftest | 0 | 0 | `a374464322a4f255` | same |
| python3 -B tools/assemble-d2.py --check | 0 | 0 | `2fa0c8c197459f54` | same |
| python3 -B tools/assemble-d2.py --selftest | 0 | 0 | `a81294c0347660d9` | same |
| python3 -B tools/assemble-d2-typed.py --check | 0 | 0 | `e3b16d3bae56cce5` | same |
| python3 -B tools/assemble-d2-typed.py --selftest | 0 | 0 | `00303b7724983160` | same |
| python3 -B tools/assemble-culture-d3.py --check | 0 | 0 | `e20620fabdf28532` | same |
| python3 -B tools/assemble-culture-d3.py --selftest | 0 | 0 | `91a0653948d48a10` | same |
| python3 -B tools/assemble-culture-d4.py --check | 0 | 0 | `293bf19f7e6e9c70` | same |
| python3 -B tools/assemble-culture-d4.py --selftest | 0 | 0 | `0182f7178e24616d` | same |
| python3 -B tools/assemble-d4-typed.py --check | 0 | 0 | `692d476ad07f1ca6` | same |
| python3 -B tools/assemble-d4-typed.py --selftest | 0 | 0 | `4945c941cd243734` | same |
| python3 -B tools/d2-typed-labels.py --selftest | 0 | 0 | `9b492600f5627480` | same |
| python3 -B tools/d2-typed-labels.py --check | 0 | 0 | `17064af53c48304d` | same |
| python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml | 0 | 0 | `1c8add321259a9f0` | same |
| python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml | 0 | 0 | `1c8add321259a9f0` | same |
| python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml | 0 | 0 | `c60820a54742ecaa` | same |
| python3 -B tools/gates/typed-pipeline-gate.py --selftest | 0 | 0 | `35b344fce7daa4ed` | same |
| python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml | 0 | 0 | `15cdfbda73cd56cb` | same |
| python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | 0 | 0 | `865bb03e1694dc0f` | same |
| python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml | 0 | 0 | `a1c055b6fe994291` | same |
| python3 -B tools/gates/typed-pipeline-gate.py --selftest-generalized | 0 | 0 | `4bc6817850c6b6be` | same |
| python3 -B tools/gates/argot-derivation-gate.py --selftest | 0 | 0 | `ce3a07fdb8155351` | same |
| python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | 0 | 0 | `cff8995c0466b096` | same |
| python3 -B tools/gates/register-law-gate.py --selftest | 0 | 0 | `8cca1efe9454eed5` | same |
| python3 -B tools/gates/register-law-gate.py --packet examples/culture-d4/packet.d4.yml | 0 | 0 | `be9e054d7b4e8dd7` | same |
| python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet | 0 | 0 | `9aa7ea349cd8177f` | same |
| python3 -B tools/exercise-handoff-e2e.py --profile v2 --selftest --quiet | 0 | 0 | `9aa7ea349cd8177f` | same |
| python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet | 0 | 0 | `b4c57165a3bf0545` | same |
| python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest --quiet | 0 | 0 | `49110716cba565e0` | same |
| python3 -B tools/check-evidence-coupling.py --selftest | 0 | 0 | `cf62bc50e303b793` | same |
| python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json | 0 | 0 | `e282a06884980341` | same |
| python3 -B tools/replay-frozen.py --selftest | 0 | 0 | `4d6aaea127ad9973` | same |
| python3 -B reports/round-26/remainders/pin-repoint-check.py --selftest | 0 | 0 | `b0f1657b217b1a02` | VOLATILE (F2) |
| python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest | 0 | 0 | `2e044f8d87b154dd` | same |
| python3 -B reports/round-28/ceiling/measure-ceiling.py | 0 | 0 | `62b19f53bf599d55` | same |

All 38 non-volatile commands produced byte-identical stdout and stderr digests
across the two back-to-back passes on an identical tree; stderr digests were
identical for all 40.

## Findings

**F1 — `battery` stdout is not byte-reproducible (mismatch class: volatile output).**
Cross-pass digest mismatch (`cross_pass_findings` in the combined JSON; kind
`stdout-digest-mismatch-between-passes`). Line-level diff of the two passes:
the only differences are (a) the battery's random scratch root,
`.scratch/gate-battery-bh_xgnun/…` vs `.scratch/gate-battery-3qeepsu3/…`,
echoed inside `stdout_head` and `root`, and (b) wall-clock `seconds` fields
(e.g. `0.02` vs `0.019`). Exit code and verdict content are identical. This
independently reproduces the round validator's own nondeterministic-stdout
whitelist (`NONDETERMINISTIC_STDOUT = {"battery", "pin-repoint-selftest"}` in
`reports/round-31/run-validation.py:93`) — a calibration confirmation, not a
new defect. Consequence for claim O's "output hashes recorded": a raw-stdout
SHA-256 recorded for `battery` cannot be re-verified byte-exactly by a later
re-run; the final sweep must record it volatile-normalized or annotated.

**F2 — `pin-repoint-selftest` stdout is not byte-reproducible (same class).**
Only difference across passes: the embedded `"date"` field
(`2026-10-18T22:46:51.072496+00:00` vs `2026-10-18T22:47:28.672950+00:00`).
Same disposition as F1; same validator whitelist entry.

**F3 — historical control reproduced (expected red stays red, both legs).**
`python3 -B reports/round-28/sweep/sweep.py --selftest` (external-tmp leg,
`/var/tmp`): exit 1 on leg O09 and leg O10, failed control
`r28-generation-replays-green` — byte-for-byte the disposition recorded by the
round-30 runner (immutable R28 selftest replays the superseded R28
generation; current typed-pipeline successor pins are covered by the
`typed-pipeline-*` rows above, all exit 0). Recorded under
`passes.*.historical_controls` in the combined JSON; excluded from leg
`results` (which carry the green-required current-tree matrix only).

**No exit mismatches, no source drift, no unexpected reds.** The assignment's
mismatch bar (>=10 commands) is exceeded: 40 current commands x 2 passes = 80
re-executions, plus the historical control twice (82 total), every one
individually dated and digested in the leg JSONs.

## Cross-check against `reports/round-31/final-sweep.md` — could-not-evaluate

The builders' `final-sweep.md` was not present at any poll from 22:51Z through
23:09Z (checks at 60 s intervals, 15-minute dependency budget exhausted;
background poller `bash-vt7l3km2` ran 600 s and final direct checks at
23:08:19Z and after the final pass found the file absent). The verbatim
re-run comparison of its recorded command lines therefore could not be
performed and is recorded `could-not-evaluate`; this report stands on its own
two passes. If `final-sweep.md` lands later, re-run
`python3 -B reports/round-31/sweep-audit.py` — it detects the file and appends
the verbatim re-run section (`final_sweep_md` in the combined JSON) — and
compare against this report; the two known-volatile families must be compared
exit-code-only, per F1/F2.

## Re-run

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR="$PWD/.scratch"
python3 -B reports/round-31/sweep-audit.py
```

Writes/rewrites only `reports/round-31/sweep-audit-O09.json`,
`reports/round-31/sweep-audit-O10.json`,
`reports/round-31/sweep-audit-O09O10.json`.

## Limits

- Byte-digest stability was asserted only between two passes minutes apart on
  one machine and one tree state; it is not a cross-platform determinism claim.
- The 240 s per-command timeout was never hit (slowest command 3.5 s,
  `handoff-v3`); no timeout behavior was exercised.
- The historical-control red is reproduced, not re-judged; its disposition is
  round-30's, cited above.
- Audit-runner exit codes/digests are recorded for the third (filed) pass set;
  the two earlier pass sets agreed on every exit code and on the same two
  volatile families.
