# R18-O15..O20 — regression + review: post-cascade battery, craft, validators, frozen replays, d2/d3 assemblers, evidence-coupling

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers on
  `opencode-go-2/deepseek-v4.1-flash`) · shard: **O15..O20** (regression+review ×6,
  claim O `gate-generalization`) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R18-O15..O20 (regression+review x6): battery, craft,
  validators, frozen replays (round-11 + round-3 isolated), d2/d3 assemblers,
  evidence-coupling — all green post-cascade; adversarial reviews of the
  generalization (bypass paths, pin-confusion); reports/round-18/gate/{regression,reviews}.md."
- date: 2026-10-18. Baseline revision `3dd3754207032cb81f5fb3e202fe85cf79211339`
  (`reports/round-18/claims.json`); declared HEAD `c66ac3c…`; the working tree moved
  under this seat throughout the window (the O/D/C seats were still landing).
- canon: NON-CANON engineering evidence. A reproduced red verdict stays red; exit 0
  is never a clearance, a canon record, or a real-world rights statement.
- writes: **this file and `reports/round-18/gate/reviews.md`** plus gitignored scratch
  under `.scratch/r18o/**`. No tool, gate, packet, baseline, manifest, receipt or
  earlier-round byte is edited by this seat. No commit, no push.

## 1. Revision under test, and why every reading below carries a stamp

`tools/gates/typed-pipeline-gate.py` moved five times inside this seat's window:

| stamp (UTC) | gate sha256 (first 16) | note |
|---|---|---|
| 10:22Z (pre-cascade) | `d102fd1dd1bae3cc` | the round-17/round-11 frozen revision |
| 10:33Z | `ea95e2a1452ef51d` | first complete generalization (flags + `--selftest-generalized`) |
| 10:39Z / 10:40Z | `84dc177e7968…`, `a201afeeb5fa…` | implementer iterations |
| **10:41Z–10:43Z (readings in this file)** | **`286d6e82711427ea`** | re-pin manifest pins this sha and replays 11/11 |

The gate may move again after this stamp. The one-line re-check is
`python3 tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv`
(with `TMPDIR` outside the repo) plus `python3 reports/round-18/run-validation.py`;
if the gate sha changed, the repin manifest must be re-frozen by its owner before
any green claim. (The re-pin manifest was authored at
`reports/round-18/repin/MANIFEST.tsv` and moved to the path above by its owner at
~10:45Z; same bytes, sha `85d75c9a…`.)

**Method / scratch rules actually used.** All scratch writes ran with
`TMPDIR=$PWD/.scratch`. The two `replay-frozen` legs alone ran with
`TMPDIR=/var/tmp/kotodama-r18-replay` because `tools/replay-frozen.py` refuses an
in-repo mirror root by design (`tools/gates/frozen/round-11/README.md`). Isolated
validator copies must **not** sit under any path containing a `.scratch` component:
the round-17 runner skips such paths as "git-ignored scratch logs, not filed bytes",
so a copy under `.scratch/` reads as an empty tree and fails spuriously (measured
10:33Z; the seat moved its copies accordingly). `tools/harness/receipt_guard.py`
refuses in-place rewrite of a committed receipt (exit 3) unless `REFRESH_RECEIPTS=1`;
no historical validator was run against the live tree.

## 2. The six legs — pre-cascade vs post-cascade

All commands from the lane root, 2026-10-18. Pre readings 10:22–10:30Z (gate
`d102fd1d…`); post readings 10:41–10:43Z (gate `286d6e82…`).

| # | leg | command | pre | post | evidence |
|---|---|---|---|---|---|
| 1 | battery | `python3 tools/check-gate-battery.py` | exit 0, 7 pass / 0 fail / 0 unevaluable, baselines 8 pinned / 0 uncovered | **exit 0**, 7/7 pass, **15 pinned / 7 gates covered / 0 uncovered**, `originals preserved` (28 hashed, 0 modified) | `.scratch/r18o/battery.pre.txt`, `.scratch/r18o/final/battery.txt`, `.scratch/r18o/final/battery-3root.txt` |
| 1b | battery selftest | `… --selftest` | 29/29 controls | 29/29 controls | `.scratch/r18o/final/battery-selftest.txt` |
| 1c | battery 3-root | `… --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines` | — | exit 0, 15 pinned / 0 uncovered | `.scratch/r18o/final/battery-3root.txt` |
| 2 | craft | `python3 tools/check-craft-exercise.py --selftest` | exit 0 (10/10 + 18/18) | exit 0, `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18` | `.scratch/r18o/final/craft-selftest.txt` |
| 2b | craft positive | `… examples/supplement-opencode-1/sound-change-vs-taboo.json` | exit 0 | exit 0 (`audits=7, mech_cases=11, derivations=9`) | `.scratch/r18o/final/craft-positive.txt` |
| 3 | validators | `python3 reports/round-18/run-validation.py --check` (no receipt written) | (runner did not exist) | **O5 regression block 12/12 exit 0**; claim C pass; claims D/O still red at the stamp (§5) | `.scratch/r18o/final/r18-validator-check.txt` |
| 4 | frozen replay, round-11 | `TMPDIR=/var/tmp/… python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | 11/11 reproduced | **10/11 reproduced, 1 `gate_digest_mismatch`** (row 1: the filed row pins `d102fd1d…`, the live gate is `286d6e82…`) | `.scratch/r18o/replay-r11.pre.txt`, `.scratch/r18o/final/replay-r11-live.txt` |
| 4b | frozen replay, round-11 **isolated at the filed pin** | iso tree with `tools/gates/typed-pipeline-gate.py` restored from `HEAD` (`d102fd1d…`) + the filed frozen tree, `--repo-root <iso>` | — | **11/11 reproduced, exit 0** | `.scratch/r18o/iso-r11`, reading 10:37Z |
| 4c | frozen replay, round-18 re-pin generation | `… tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | — | **11/11 reproduced, exit 0** (pins `286d6e82…`); the same file's sha `85d75c9a…` read 11/11 at 10:43:09Z while it still lived at `reports/round-18/repin/MANIFEST.tsv` (its owner moved it at ~10:45Z — the reading, not the bytes, is what moved) | 10:43:09Z and 10:46:00Z, `.scratch/r18o/final/replay-r18.txt` |
| 4d | frozen replay, round-18 D4 rows | `… tools/gates/frozen/round-18/MANIFEST.tsv` | — | **2/2 reproduced, exit 0** | 10:43:09Z |
| 4e | frozen replay, round-3 **isolated** | iso tree with the six gates restored from `291c714` (all six hash to the filed pins) + committed frozen tree, `--repo-root <iso>`; both `round-3/MANIFEST.tsv` and `round-3/attempt-1/MANIFEST.tsv` | — | **7/7 + 7/7 reproduced, exit 0** (live tree reads 7/7 `gate_digest_mismatch` — the round-10 documented historical-pin class, not a regression) | `.scratch/r18o/iso-r3`, readings 10:36Z and 10:39Z |
| 4f | replay selftest | `TMPDIR=/var/tmp/… python3 tools/replay-frozen.py --selftest` | — | exit 0, `79/79 checks passed` | `.scratch/r18o/final/replay-selftest.txt` |
| 5 | d2/d3 assemblers | `assemble-d2.py --check` / `--selftest`; `assemble-culture-d3.py --check` / `--selftest`; `assemble-culture-d4.py --check` / `--selftest`; `assemble-d2-typed.py --check` / `--selftest` | all exit 0 | **all exit 0** | `.scratch/r18o/final/d{2,3,4}-*.txt`, `d2typed-*.txt` |
| 6 | evidence-coupling | `python3 tools/check-evidence-coupling.py --selftest`; `… examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | exit 0 both | **exit 0 both** (`selftest_passed: true`) | `.scratch/r18o/final/evc-selftest.txt`, `evc-frozen.txt` |

## 3. The claim-O core: the default D2 path is byte-identical

This is the regression the generalization had to preserve, measured on the same
committed inputs before and after:

| command | pre (10:22Z, `d102fd1d…`) | post (10:41Z, `286d6e82…`) | reading |
|---|---|---|---|
| `python3 tools/gates/typed-pipeline-gate.py` | exit 0, stdout sha256 `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` | exit 0, **same sha256** | byte-identical |
| `… --json` | `19765ddf2c36a7dbd71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62` (constant set unchanged) | **same sha256** | byte-identical |
| `… --selftest` | 12/12 checks | 12/12 checks | green |
| `… tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` (the frozen build product) | — | stdout sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` == the filed `typed-pipeline/run.log` | the recorded verdict is reproduced; 13/13 legs |
| `… --selftest-generalized` | (flag absent) | exit 0, `14/14 checks passed` (default-resolution, declared-family, tamper/drift/self-pin/missing-expected/stale-pin controls) | green |

The same default-path sha256 was also reproduced at the intermediate revision
`ea95e2a1` (10:33Z), i.e. the byte-identity held across the whole edit window that
this seat observed, not only at the endpoints.

## 4. Re-pin cascade — verified from the outside (pin-confusion controls)

Every value below was re-hashed by this seat; nothing is quoted from a receipt.

| surface | before | after | filed byte moved? |
|---|---|---|---|
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063` (mtime 2026-10-17 19:27) | identical at 10:42:59Z | **no** |
| round-11 `run-receipt.json` / `run.log` | `c49ebc9e…` / `9a69985a…` | identical | **no** |
| re-pin generation `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (read as `reports/round-18/repin/MANIFEST.tsv` at 10:43Z; moved by its owner ~10:45Z, bytes unchanged `85d75c9a1a7c937de2860ad9fdf25f62e6a6b0be7f3b2650ee04230860b52c8c`) | (new) | row 1 pins gate `286d6e82…`, replay **11/11** at 10:43:09Z and again at 10:46:00Z | new file |
| round-9 `r9-pre` baselines | 8 files, gate pins equal the live reader gates | identical (0 pin values moved) | **no** |
| new revision `r18-post` | (new) | 7 new `tools/gates/frozen/<gate>/r18-post/` baselines; battery 8 → 15 files, all pinned | new dirs |
| `reports/round-16/handoff/expected-v2-07.json` | `dc75c5d7e347987e81efe6f6fe17314e8f6a2ce26a12a1ca7ec3567a21dcaad1` | identical | **no** |
| successor `reports/round-18/repin/expected-v2-07-r18.json` | (new) | `d5fda399490d47eb35be2d14f14d8652fe8fd071df46de0fb90fdc1567b899f9`; helper re-verify exit 0, 0 of 28 input pins moved | new file |
| filed rounds 8–17 | — | `git status --porcelain reports/round-{8..17}` → empty at 10:42Z | **no** |

So the cascade is append-only in the measured window: no filed receipt was rewritten,
and every moved pin is legible next to the old one.

## 5. What was **not** green at the reading stamp (stated, not rounded up)

The round-18 counting command was re-read at 10:47Z (gate `286d6e82…`, same revision
as §2–§4): `python3 reports/round-18/run-validation.py --check` → exit 1,
`acceptance_checks_passed: false`.

- claim **C** — pass (0 failures).
- claim **D** — fail, 5 items: "D4 typed artifact not found under `examples/culture-d4`";
  the D4 gate run exits 2 (`FAIL L1-build: adapter missing: tools/assemble-d4-typed.py`);
  "the D4 gate run names no declared assembler in its resolution line"; "… no assembler
  digest in its resolution line"; and `tools/gates/typed-pipelines.json: [Errno 2] No
  such file or directory` — the runner expects the reviewed design's sha-pinned
  registry file, which has not landed (the same absence `reviews.md` F1/F4 measures
  from the adversarial side).
- claim **O** — fail, 2 items: the D4 packet does not yet reach exit 0 (the missing D4
  adapter), and the flag-declared assembler path is not green. The earlier O failures
  about the frozen manifests and the missing re-pin record are **resolved** at this
  stamp: the re-pin generation replays 11/11 and the cascade table exists.

At the 10:41Z reading the same command also reported those two manifest items as
stale; they were re-frozen between 10:41Z and 10:43Z, which is the concrete
illustration of §1/§6 — the cascade's greens are revision-stamped, not timeless.

None of these are regressions of the default path; they are the D/O implementer legs
still in flight. **The six regression legs in §2 do not depend on them and were green
at the same revision.** They must be re-read after the final gate revision lands.

Historical validators (rounds 11/16/17) are not re-run against the live tree on
purpose: each is a writer of its own committed receipt, and `receipt_guard` refuses
(exit 3). The isolated-copy route is documented in §1, and the filed verdicts remain
the record for those rounds; the round-18 count is the current instrument.

## 6. Limits

- A snapshot, not a guarantee: with the gate still moving, a later edit invalidates
  the `repin` manifest pin (a new `gate_digest_mismatch`) and the above table must be
  re-measured. The append-only rule says the fix is a new re-pin, never an edit.
- Every exit 0 here asserts reproduction/consistency only. The D2 hold set (15 holds
  + 1 note) stays visible and red at the design level; the D4 tree is NON-CANON.
- The round-3 and round-11 live-tree mismatch readings are the documented
  historical-pin class (`reports/round-10/drift/fix-18.md`,
  `SKILL.md:236`), not drift introduced by round 18.
- `--check` on the round-18 runner wrote no receipt; the integrator's own run is the
  one that publishes `reports/round-18/validation.json`.
