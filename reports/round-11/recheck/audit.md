# R11-F11 — independent recheck audit (kotodama-shokunin, round 11)

- seat: **R11-F11** (freshness recheck auditor). Assignment: independently re-run >=5 of the
  rows the round-11 rerunners rechecked; a mismatch against a recheck receipt is a finding.
  This file is this seat's only write. No earlier-round byte, ledger row, receipt, tool or
  fixture was edited. The round-10 drift ledger and the 192 `row-NNN.json` receipts were read
  only.
- date: 2026-10-17. Measurement window `22:01:52Z`–`22:13Z` UTC (local UTC-03:00 =
  `19:01:52`–`19:13`). Lane HEAD at every run:
  `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (round-11 declare; baseline `94ca098`).
- isolation: `export TMPDIR=$PWD/.scratch` for every command. Raw receipts in
  `.scratch/f11/`: `rerun.sh` (verbatim commands copied from the ledger), `out/row-NNN.{out,err,exit}`,
  `my-hashes.json`, `rerun-vs-ledger.json`. Scratch is untracked, disposable evidence — not a
  deliverable.
- method: 17 ledger rows picked across **all eight** rerunner slices (`0,5 | 24,30,47 | 56 |
  72,89 | 105 | 128,137 | 158,162 | 176,177,190,191`). Every command re-run 1:1 from the lane
  root with the exact ledger command text. Captured stdout and stderr separately; hashed both
  ways for comparison, because the rerunner seats declared two capture conventions:
  combined stdout+stderr (F04) and stdout-only (F02/F05/F07/F08). All 192 receipts existed at
  comparison time (`22:11:39Z`).

## 1. Comparison table — my re-run vs recheck receipt

`prior` = ledger `output_sha256` (12 hex). `mine` = my re-run hash (16 hex; the convention that
matched the receipt is named). `receipt` = the seat's `new_hash`. Exit compared too.

| row | shard (ledger) | command (short) | prior | mine | receipt new | exit (mine/rec) | verdict |
|---|---|---|---|---|---|---|---|
| 0 | shard-01 | `sed -n '1,20p' SKILL.md` | `926bd7557ccf` | `926bd7557ccf1d6d` | `926bd7557ccf1d6d` | 0/0 | identical (combined) |
| 5 | shard-01 | `git log -1 … -- SKILL.md` | `3789dbc4059b` | `3fc9b521eb70bc04` | `3fc9b521eb70bc04` | 0/0 | identical (combined); note F11-3 |
| 24 | shard-03 | `sha256sum …/naming-collision-gate.out` | `c95330e1a84a` | `c95330e1a84a00b9` | `c95330e1a84a00b9` | 0/0 | identical (combined) |
| 30 | shard-06 | `ls …real-world-inspiration-boundaries.md` | `282bb3058d35` | `282bb3058d35a85a` | `282bb3058d35a85a` | 0/0 | identical (combined) |
| 47 | shard-08 | `ls corpus/knowledge/civilizations/*.md \| wc -l` | `e3d6c4d4599e` | `6fc16b03d8c15b98` (raw) | `6fc16b03d8c15b98` | 0/0 | identical; prior is a stripped-newline recording — F11-4 |
| 56 | shard-08 | `sed -n '141,160p' SKILL.md \| sha256sum` | `1389ae565fce` | `1389ae565fceaf52` | `1389ae565fceaf52` | 0/0 | identical (combined) |
| 72 | shard-10 | `phonology-sanity-gate.py <fixture>` | `b3843b2a5f50` | `b3843b2a5f50809f` | `b3843b2a5f50809f` | 1/1 | identical (combined); 16 findings/15 IDs |
| 89 | shard-10 | `replay-frozen.py --selftest` | `4d6aaea127ad` | `4d6aaea127ad9973` | `4d6aaea127ad9973` | 0/0 | identical (combined) |
| 105 | shard-11 | `replay-frozen.py …/attempt-1/MANIFEST.tsv` | `409db5ab8b68` | `409db5ab8b68ebc3` | `409db5ab8b68ebc3` | 2/2 | identical (stdout=combined; stderr empty) |
| 128 | R10-F15-battery | `check-gate-battery.py` | `8bf71a029a2f` | `97fde47d00c8…` | `bdf31b3928de…` | 2/2 | hash differs — **expected nondeterminism**, F11-1 |
| 137 | R10-F15-battery | `phonology-sanity-gate.py <fixture>` | `b3843b2a5f50` | `b3843b2a5f50809f` | `b3843b2a5f50809f` | 1/1 | identical (combined) |
| 158 | shard-12 | `replay-frozen.py --selftest` | `4d6aaea127ad` | `4d6aaea127ad9973` | `4d6aaea127ad9973` | 0/0 | identical (combined) |
| 162 | shard-12 | `check-gate-battery.py` | `9b382adf80ab` | `3d5e57ad6f8f…` | `0ddd69d23b66…` | 2/2 | hash differs — **expected nondeterminism**, F11-1 |
| 176 | fix-17 | `ls corpus/knowledge/civilizations/*.md \| wc -l` | `6fc16b03d8c1` | `6fc16b03d8c15b98` | `6fc16b03d8c15b98` | 0/0 | identical (combined) |
| 177 | fix-21 | control battery (3 roots) | `c164b1e2c386` | `e88831550b4f…` | `66eff40524cf…` | 0/0 | hash differs — **expected nondeterminism** (F11-1); exit later flipped 0→2 mid-wave (F11-2) |
| 190 | R10-F15-battery | `source-audit-inventory.py --json --summary --root…` | `0d096bef3698` | `d4c29a95a9f2969b` | `d4c29a95a9f2969b` | 0/0 | **identical**; unstable by corpus growth — see below |
| 191 | integrator | `assemble-culture-d3.py --selftest` | `91a0653948d4` | `91a0653948d48a10` | `91a0653948d48a10` | 0/0 | identical (combined) |

Tally: **14/17 my hashes are byte-identical to the receipts' `new_hash`** (rows where the
receipt marks `stable:false` for non-nondeterministic causes are still byte-identical: rows 5
and 190 — both sides measured the same new bytes). 3/17 (128, 162, 177) hash-differ for the
battery nondeterminism class; see F11-1. **Exit codes agree on all 17** (receipt exit fields
vary in name: `new_exit` 168×, `exit` 24×; both were looked up).

## 2. Findings

### F11-1 — the 3 hash-diffs are the documented nondeterminism class, independently corroborated (no recheck defect)

`python3 tools/check-gate-battery.py` (any variant) prints a random temp-mirror token
(`.scratch/gate-battery-<rand>`) and per-gate wall-clock `"seconds"` floats. My own repeats:
row 128 → `97fde47d…`, `ec519e0e…`, `9286bb07…` (3 runs, 3 hashes); row 177 → `e8883155…`,
`d26b7c4d…` (plus the exit-flip pair below, `1b01506c…`, `235e1eab…`). Structural comparison of
my runs after masking the token and the `seconds` values → **0 differing JSON leaf paths**
(both 128 pairs and the 177 pair). The receipts state the same class with their own numbers:
row 128 (`repeatability: nondeterministic`, masked sha `15e16034…`), row 162 (`three live runs
… three distinct raw hashes`, normalized `2c21e573…`), row 177 (`four re-runs … four hashes`,
`substance_unchanged: true`). Conclusion: the mismatch between my single re-run and the
receipt's single `new_hash` is the expected signature of this class; the receipts' `stable:false`
verdicts are correct. F12's stability statistic must exclude/normalize these rows, or they read
as drift. (Related ledger note: the same command family already carried 3 distinct round-10
hashes — rows 65/128/162.)

### F11-2 — control-battery exit flipped 0→2 mid-audit from concurrent in-flight artifacts (to-verify at wave close)

`python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines`:
my first run (19:03:34 local) exit **0**, matching ledger row 177 and the row-177 receipt
(`new_exit: 0`). My runs at 19:11:55 and ~19:12 gave exit **2** with the new content:
`baselines_found 9` (was 8), `pinned 8`, `fail 0`, and
`BASELINE-GATE-UNKNOWN — declared gate None is not one of the seven registered gates`
against `expected/handoff-exercise/r11/expected.json`. Cause is visible in the tree: the
round-11 D/O seats created `tools/gates/expected/handoff-exercise/` at **19:08:52**, plus
`tools/typed-gate-flow.py` 19:12:52, `tools/exercise-handoff-e2e.py` 19:12:43,
`examples/culture-d2/packet.d2.typed.yml` 19:11:56 (all untracked, in flight). The receipt
snapshot (19:03:48+) predates those files, so receipt and my later runs legitimately disagree.
**Disposition: in-flight, to-verify** — the round's final validation must confirm the control
returns exit 0 once the new baseline is complete; if it stays exit 2 after the wave, that is a
wave-close defect for the D/O seats, not for the recheck receipts.

### F11-3 — row 5 drift is a legitimate history change; my re-run matches the receipt exactly

My re-run and F01's receipt both read `94ca098b 2026-10-17 round-10: admit C/F/O…` — the
round-10 admit commit edited `SKILL.md` (+31/-17) **after** shard-01 measured at `e3a1ec9`;
reconstructed old output hashes to the ledger's prior (`3789dbc4059b…` = sha256 of
`"e1694bad… round-8: admit F/O/D — freshness receipts, harness+gate repairs, d2-typed-labels\n"`).
Receipt classification "legitimate change" corroborated.

### F11-4 — ledger capture-convention inconsistency on rows 47/48 (data-quality note; F02 handled it right)

Ledger row 47 **and** row 48 hash `"94"` **without** the trailing newline (`e3d6c4d4599e…` =
sha256(`"94"`)), while rows 45/176 — the identical command — hash `"94\n"`
(`6fc16b03d8c15b98…`). Verified computationally: `printf '94' | sha256sum` → `e3d6c4d4599e…`;
raw stdout → `6fc16b03d8c15b98…`. F02's receipt classifies row 47 `stable-capture-convention`
with the same proof. Anyone diffing row 47/48 by raw hash will see false drift; the F12
summary should count them stable.

### F11-5 — filed bytes observed modified in the worktree (out of this seat's scope — reported, not absorbed)

`git status` during my runs: `reports/round-10/coverage/index-update-22.md` (M, post-filing
appendix) and `reports/round-{5,6,7,8,9}/validation.json` (M). F08's receipt independently
records the same season: "a sibling round-11 seat rewrote the filed
`reports/round-{5,6,7,8,9}/validation.json` in the lane tree at 19:03:00–19:03:17 local
(858 deletions vs HEAD)" — none of the recheck commands read those files. Rounds 8 and 9
are among this round's explicitly filed rounds; whether regenerated receipts are intended
(runners rewrite their own `validation.json` on every invocation) or need restoring is the
orchestrator/scribe's call. Recorded here with evidence so it is not lost.

### F11-6 — receipt schema variance (minor; for F12/X03 consumers)

Field names differ across rerunner slices (`new_exit` vs `exit`; `hash_stream` /
`hash_convention_matched` / `recheck_context.hash_method`; `stable` on all 192). A consumer
that reads only one shape silently loses exits for 24 rows. My comparison handles both; noted
so the summary/runner authors do likewise.

## 3. Verdict

- Requirement "independently re-run >=5 rechecked commands": **17 re-run**, spanning all eight
  slices (3.4x the minimum).
- Genuine mismatches found: **0**. The 3 hash-diffs are the battery nondeterminism class,
  independently reproduced by my repeats and matching the receipts' own analyses; the 1 exit
  flip is a concurrent in-flight artifact (F11-2), dispositioned to-verify at wave close.
- Context: 192/192 receipts present; the receipts' own census at audit time was 149 stable /
  43 unstable (F12's summary owns the final counts).
- All evidence is re-runnable from `.scratch/f11/rerun.sh` and the receipt files named above.

## 4. Evidence index

| artifact | path |
|---|---|
| runner script (verbatim ledger commands) | `.scratch/f11/rerun.sh` |
| raw captures (stdout/stderr/exit) | `.scratch/f11/out/row-NNN.{out,err,exit}` |
| my hash registry | `.scratch/f11/my-hashes.json` |
| first-run vs ledger diff | `.scratch/f11/rerun-vs-ledger.json` |
| receipts cross-checked | `reports/round-11/recheck/row-{000,005,024,030,047,056,072,089,105,128,137,158,162,176,177,190,191}.json` |
| ledger | `reports/round-10/drift/ledger.json` (192 rows, sha256 read-only) |
