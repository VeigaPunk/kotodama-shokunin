# R29 O19–O20 regression run

**Result: NOT GREEN.** The gate battery and craft checker pass, but the full regression set does not: the corrected Round 27 sweep selftest is red, several historical lesson-audit selftests have stale live-tree expectations, the Round 28 ceiling selftest crashes, and multiple frozen manifests do not reproduce against the current tree.

## Measurement boundary

- Measured 2026-10-18 in an isolated copy rooted at `e923d6ecaf5fd9d256e4b377745bd3d24f5e2d47`; `reports/round-29/claims.json` declares baseline `3b13a2f2821ed6f8ac1217842ab6830d592c7935`. The snapshot driver copied 2,503 source files with no copy-source drift; its 1,851 locked historical paths had zero changes (`.scratch/r29-o19-o20-regression/run/snapshot.json`). The commands and streams are recorded in `run/results.json` and neighboring `run/*.stdout.txt` / `run/*.stderr.txt` files.
- The first matrix ran 133 commands, 101 with exit 0; it invoked 79 `--selftest` commands, including 48 additional discovered entrypoints. Several invocations needed correction (required `--root`/`--source-root`, or a usable `/dev` in bubblewrap); corrected outcomes are called out below rather than treating setup failures as test verdicts.
- At matrix end, the snapshot driver detected a concurrent change to `reports/round-29/rerun.json`; this worker did not write that file. No Round 8–28 source paths changed. The only copied-path mutations were the Round 27 and Round 28 gate-test receipts inside the isolated clone.

## Passing checks

- `python3 tools/check-gate-battery.py` — 2026-10-18: exit 0; 7 pass, 0 fail, 0 unevaluable. Coverage was 9/9 gates and 19/19 baseline pins; the battery hashed 32 original inputs before and after with zero changes. `python3 tools/check-gate-battery.py --selftest` — same date: 35/35. The battery verifies coverage and pins; its per-baseline `verdict_replay` is explicitly `not-run`, so this is not a claim that every frozen gate verdict is green. Evidence: `run/battery.stdout.txt`, `run/battery-selftest.stdout.txt`.
- `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --report reports/supplement-opencode-1/32-craft-exercise.md` — 2026-10-18: exit 0, all checker validations passed (`audits=7`, `mech_cases=11`, `derivations=9`, `approx_checks_runner=37`). Its counts command found 7 claims: 5 supported, 2 unresolved, 0 contradicted, and 1 blocked retrieval. `python3 tools/check-craft-exercise.py --selftest` — same date: 10/10 tamper controls and 18/18 CLI controls. Evidence: `run/craft.stdout.txt`, `run/craft-counts.stdout.txt`, `run/craft-selftest.stdout.txt`.
- `python3 tools/replay-frozen.py --selftest` — 2026-10-18: 79/79 controls. Evidence: `run/frozen-selftest.stdout.txt`.
- Corrected invocation of `python3 reports/round-25/v3-supersession/v3-supersession-check.py --root <isolated clone> --selftest` — 2026-10-18: 44/44. The first discovered invocation omitted its required `--root`; it was not counted as a test result. Evidence: `run/r25-supersession-rerun.stdout.txt`.
- `python3 reports/round-26/remainders/r4-twin/build-twin.py --selftest --source-root <pinned source clone>` — 2026-10-18: 12/12, using the pinned-source checkout at `1ad491a1a4b0aef9ebdc1861dfb8237727503825`. `python3 reports/round-26/remainders/r4-twin/verify-twin.py --root <isolated selftest clone> --source-root <isolated pinned-source clone> --selftest` — same date: 22/22; its controls checked the 58-entry manifest and both filed twin reproductions. Evidence: `run/r26-builder-pinned-final.stdout.txt`, `run/r26-twin-verify-pinned-final.stdout.txt`.
- With `TMPDIR` and the `/var/tmp` bind under lane `.scratch`, and `bwrap --dev-bind /dev /dev`, `python3 reports/round-28/sweep/sweep.py --selftest` — 2026-10-18: 12/12. It reproduced the current Round 28 generation 4/4 and classified both Round 27 rows as mismatches (superseded). Evidence: `run/r28-devbind.stdout.txt`.

## Regressions and stale controls

- With the same corrected bubblewrap device setup, `python3 reports/round-27/pinsweep/sweep.py --selftest` — 2026-10-18: exit 1, 8/10 controls. The control `known-green-generation-replays` instead got two mismatches, and `manifest-walker-finds-d4-rows` found 0. The direct frozen replay of `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` also measured 0/2 reproduced and 2/2 mismatches. Evidence: `run/r27-devbind.stdout.txt`, `run/frozen-replay-01.stdout.txt`.
- `python3 reports/round-28/ceiling/measure-ceiling.py --selftest` — 2026-10-18: crashes at `measure-ceiling.py:250` with `TypeError: 'NoneType' object is not subscriptable` while reading `measure()["pre_fix_reader"]["illegal_ids"]`. Evidence: `run/discovered-selftest-reports-round-28-ceiling-measure-ceiling-py.stderr.txt`.
- Four discovered lesson-audit selftests encode partition/orphan expectations from before the current Round 29 lesson file was present. Each command below ran 2026-10-18 and sees 29 live lesson files, not its pinned older partition:
  - `python3 reports/round-26/audit/x63-lessons-audit.py --selftest`: 17/20; expected 26 files, observed 29, plus the A and F live-byte checks failed.
  - `python3 reports/round-26/lessons/c51-revision-audit.py --selftest`: 10/15; expected 27 files, observed 29; row/file, pin, prose-arithmetic, and falsified-pin controls failed.
  - `python3 reports/round-27/audit/x57-lessons-audit.py --selftest`: 34/37; expected 27 files, observed 29, and the expected orphan sets omit current `round-27.md` / `round-28.md` rows.
  - `python3 reports/round-28/audit/x57-lessons-audit.py --selftest`: 47/52; expected 28 files, observed 29; its orphan sets and two Round 27 “newest/stale claim” expectations also disagree with the current tree.
  Raw controls: `run/discovered-selftest-reports-round-26-audit-x63-lessons-audit-py.stdout.txt`, `run/discovered-selftest-reports-round-26-lessons-c51-revision-audit-py.stdout.txt`, and the Round 27/28 `x57` stdout files in `run/`.
- `python3 reports/round-28/sweep/sweep.py --json --tmp-parent <lane scratch>` — 2026-10-18: exit 1, 39 findings over 121 surfaces. The findings include moved frozen-manifest inputs and stale digests; see `run/r28-sweep.stdout.txt`. The sweep selftest’s corrected 12/12 result does not clear these live inventory findings.

## Frozen replay matrix

All 14 copied manifests were run on 2026-10-18 with `python3 tools/replay-frozen.py <manifest> --json --repo-root <isolated clone>`. These are reproduction outcomes, not clean-verdict assertions:

- `reports/round-17/tests/frozen/MANIFEST.tsv`: 5/5 reproduced.
- `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv`: 0/2 reproduced; 2 mismatches.
- `reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv`: 4/4 reproduced.
- `tools/gates/frozen/round-11/MANIFEST.tsv`: 10/11 reproduced; 1 unevaluable (`gate_digest_mismatch`).
- `tools/gates/frozen/round-18/MANIFEST.tsv`: 0/2 reproduced; 2 mismatches.
- `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv`, `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv`, and `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv`: each 10/11 reproduced; 1 unevaluable (`gate_digest_mismatch`) each.
- `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv`: 0/3 reproduced; 2 mismatches and 1 unevaluable (`gate_digest_mismatch`).
- `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv`: 0/6 reproduced; all 6 unevaluable (`gate_digest_mismatch`).
- `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` and `round-26/post-register/MANIFEST.tsv`: each 4/6 reproduced; 2 mismatches each.
- `tools/gates/frozen/round-3/MANIFEST.tsv` and `round-3/attempt-1/MANIFEST.tsv`: each 0/7 reproduced; all 7 unevaluable (`gate_digest_mismatch`) each.

Per-manifest streams and full row details are `run/frozen-replay-00.stdout.txt` through `run/frozen-replay-13.stdout.txt`.

## Other nonzero checks and interpretation

- `python3 reports/round-26/remainders/pin-repoint-check.py --check` — 2026-10-18: 16/17; `new-v3-row-replays-green` fails because the newer live D4 component inputs no longer match the Round 26 frozen hashes. `python3 reports/round-26/gate-tests/run-gate-tests.py --check` — same date: 61/62; the sole failure is the Round 26 post-register manifest expected to replay clean. These align with later input supersession, not an unobserved green replay.
- These exact Round 26/27 v3 handoff-baseline commands were run on 2026-10-18 and each exited 1: `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-26/register/v3-baseline-r26/expected.json`, `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-26/remainders/v3-baseline-r26/expected.json`, and `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-27/pinsweep/v3-baseline-r27/expected.json`. The Round 28 comparator, `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-28/pinsweep/v3-baseline-r28/expected.json`, exited 0 on the same date. Treat the earlier baselines as superseded by the Round 28 tree.
- `python3 tools/gates/d4-assembly-check-gate.py --selftest` — 2026-10-18: exit 2; this is an inapplicable selftest invocation because the adapter is flagless. Its ordinary command, `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml`, exited 0 that date.
- `python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml` — 2026-10-18: exit 1 as the designed negative-control fixture. `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` — same date: exit 1 with four named dangling HOLDs for undelivered design rows.
- `python3 reports/round-22/fixes/tie-break.py --root . --check` — 2026-10-18: exit 1, the documented historical false positive. These are not green frozen replays.

No fixes were attempted: this assignment was regression measurement only. The initial `/dev/null` launch failures from the first confined Round 27/28 sweep attempts were replaced by the corrected device-bound reruns above; their earlier `could-not-evaluate` outputs are not treated as verdicts.
