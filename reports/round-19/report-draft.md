# Round 19 — report draft (SCRIBE X23..X25)

- **Round:** 19, operator loop 2 of 3, build round 3 of 4 (64 declared
  workers, provider `hyper/deepseek-v4.1-flash` per the operator
  substitution — `reports/round-19/claims.json`). **Date:** 2026-10-18.
- **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. **Baseline:**
  `e5718945a1ab0a0c3db955338d2cae77d68fd348` (round-18 admit). HEAD at draft
  time `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` (round-19 declare) —
  `git rev-parse HEAD^` = the baseline, so HEAD is the declaration commit and
  no round-19 byte is committed yet.
- **Claims:** D / depth (D4-derived SKILL.md decision tables + lessons);
  C / coverage (>=8 sourced entries across verification + synthesis);
  O / operability (battery default covers the D4 gates 9/9 + committed
  baselines).
- **Counting command:** `python3 reports/round-19/run-validation.py`
  (receipt: `reports/round-19/validation.json`).
- **Status of this draft:** NON-CANON engineering evidence. It admits
  nothing, certifies no canon, lore receipt, source freshness, or real-world
  clearance, and it is written by the X23..X25 scribe seats, not the
  integrator. The parent owns the final report and the LOG/SCORECARD append.

## 1. What landed and how it is measured

Round 19 was declared as a three-claim build: codify the round-17/18 D4 craft
into `SKILL.md` (register-scoped slot routing, derivation replay, the
2-labels-per-garment typed shape, the serializer round-trip corruption class);
expand the two thinnest corpus partitions (verification 15, synthesis 24);
and put the two D4 gates into the battery's default roots with committed
`expected.json` baselines.

The counting command is `reports/round-19/run-validation.py`, kept
stdlib-only, read-only over every artifact it grades, and fail-closed on
filed-round contact (rounds 8–18 must stay byte-identical to the baseline;
round-19 corrections live only under `reports/round-19/`). Its own controls
are green: `--selftest` → **26/26**, exit 0 (sha256
`92093b55e394bbe4f6e761f84ee98f3698a423cdbbecdc3bee206f46f4a992f6`).

**This draft was written against an in-flight tree.** The 20-minute
dependency window (`.scratch/x23-watch.jsonl`, 21 polls, 11:32:05Z–11:52:05Z)
closed with claim C settled and claims D and O not settled; a re-measurement
at 12:32:23Z found SKILL.md still byte-unchanged and the battery still exit 2.
Per the round-14/15 precedent the seat files the honest in-flight record
rather than waiting past its bound.

## 2. Claim C — coverage: **PASS** (measured)

Measured by `python3 reports/round-19/run-validation.py --check`
(2026-10-18T12:32:25Z): `claims.C.passed = true`, no failures.

- **10 new sourced entries, 5 per thin partition** (the claim required >=8
  total, >=3 each). Verification: `label-channel-routing-verification`,
  `pre-declared-hold-set-reconciliation`,
  `generated-artifact-roundtrip-verification`,
  `gate-battery-surface-verification`, `two-reader-interop-agreement`.
  Synthesis: `typed-label-routing-workflow`, `generated-artifact-lifecycle`,
  `hold-set-contract-in-brief`, `era-material-scoped-reconciliation`,
  `finding-disposition-workflow`.
- **Partition counts** re-measured 2026-10-18: verification **15 → 20**,
  synthesis **24 → 29** (linguistics 19, myth-symbol 19, culture-material 18,
  civilizations 94).
- **Every entry profiles complete:** the runner checks each new entry for a
  `- topic:` line, a `- gap filled:` line, a `- sources:` line, a `- couples:`
  line and a decision record — all ten pass all five checks
  (`claims.C.measurement.entry_profiles`).
- **Gap registry:** `reports/round-19/gaps.md` claims the ten gaps before
  authorship (collision-avoidance list), and each entry's `- gap filled:`
  names its gap.
- **README reconciled:** `corpus/README.md` revision **1.4** (Round-19 index
  refresh) — 199 rows, 0 missing, 0 topic mismatches; partition counts
  `19/19/18/29/20/94`. The runner's earlier `--check` failures ("README was
  not reconciled", "revision was not bumped") are cleared by this landing.
- **Filler audit:** the runner consumes independent filler auditors
  (`reports/round-19/audit/x26-spotcheck-entries.md`, `audit-1.md`,
  `audit-2.md`, `entries/review-C11.md`) that reject an entry naming no gap.
- **Freshness pause honored:** the freshness axis-move pause stands
  (`LOG.md:3028`); no re-grade or rank change is claimed. Every entry is
  NON-CANON.

## 3. Claim D — depth: **FAIL — not settled** (in-flight)

Measured by the same `--check` (2026-10-18T12:32:25Z): `claims.D.passed =
false`, two failures:

1. `SKILL.md did not change: the D4 decision-table subsection did not land`
2. `SKILL.md carries no new decision-table subsection covering the D4 craft`

- **Measured:** `SKILL.md` sha256 `e8d238a6377bc4135027c06b4320e3ab7b6937c1276164be986cf670db6d23f8`
  equals the declared baseline at every observation; `grep -c 'D4' SKILL.md`
  → 0 through 12:32Z.
- **What did land (the inputs for the landing):** the D4 craft drafts and
  reviews — `reports/round-19/knowledge/skill-draft-a.md`,
  `skill-draft-b.md`, `review-1.md`, `review-2.md`, `analyst-1.md` …
  `analyst-3.md`; the D4 lesson entry `reports/round-19/integration/d4-lessons-entry.md`;
  and `corpus/lessons/round-19.md` (the X21 gate-keeper survey). The runner's
  own `--selftest` control "a new D4 decision-table section is found" passes
  in-memory, so the measurement path is exercised code, not first-run code.
- **Remaining work is orchestrator/parent:** land the D4 decision-table
  subsection into `SKILL.md` from the drafts. The runner requires both a byte
  change vs the baseline **and** a new decision-table subsection covering the
  D4 craft with citations to D4 artifacts. Until then the claim cannot pass.
- **Named gap in the D tool:** `tools/assemble-d4-typed.py --selftest` exits
  **1** at the final observation, with three named control failures
  (`tamper: restored build passes`; `stale projection: exit 2 and the pin is
  named` — a missing `tools/assemble-d2.py` in the isolated fixture;
  `routing: the checked field is moved, not flagged`). Recorded, not edited
  by this seat. `--check` on the same tool exits 0.

## 4. Claim O — operability: **FAIL — not green** (in-flight, near)

Measured by the same `--check`: `claims.O.passed = false`, four failures:

1. `the battery default run exited 2 (expected 0)`
2. `the battery default run passes 8 gate selftests, neither 7 (structural) nor 9 (all)`
3. `the battery executed 9 gates but passed 8`
4. `the battery default run reports unevaluable=1`

- **What landed:** `tools/check-gate-battery.py` gained `D4_GATE_NAMES` and
  `REGISTERED_GATE_NAMES` (seven structural + two D4 adapters) and now runs
  nine selftest legs; the two D4 committed baselines landed under the standard
  layout — `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json`
  and `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json`
  (schema `kotodama-frozen-run-v1`, first baseline for each gate, recorded
  from HEAD `169c616`).
- **Coverage layer is 9/9:** the battery reports `coverage: 9/9`,
  `baselines_found 17`, `pinned 17`, `gates_uncovered []`, `unevaluable 0`.
  Both D4 gates are covered.
- **The remaining failure is the duty-1 selftest leg:**
  `d4-assembly-check-gate.py` ships **no `--selftest`**, so its leg reads
  `GATE-UNEVALUABLE-EXIT` (`detail: "selftest exited 2"`). Battery summary:
  `pass 8 / fail 0 / unevaluable 1`, and the battery exit is the worse of its
  two duties → **exit 2**. `corpus/README.md` revision 1.4 records this limit
  in the same words.
- **No gate behavior changed silently:** `claims.O.measurement.changed_gates
  = []` and `gate_change_ledger = {}` — the gate surfaces hash equal to the
  baseline.
- **Fix needed (owner O):** give `d4-assembly-check-gate.py` a `--selftest`
  contract, or move the two D4 legs to a coverage-only duty, then re-run the
  battery to a green 9/9. Until then the claim cannot pass.

## 5. Independent rerun (this seat)

Full record in `reports/round-19/rerun.json`; payload
`.scratch/x23-measurements.json`; harness `.scratch/x23-rerun.py`.

- **Regression inventory:** 19 fixed read-only commands → **17 green / 19**.
  The two non-green are exactly the two O/D gaps above:
  `tools/check-gate-battery.py` (exit 2, the duty-1 D4 leg) and
  `tools/assemble-d4-typed.py --selftest` (exit 1, three named controls).
  All 13 round-14/15 baseline regressions plus the D4 assembler and both D4
  adapters are green (per-command exits and stdout sha256 in `rerun.json`).
- **Preservation control:** 821 files under `reports/round-8..18`
  (excluding `__pycache__` and `*.log`), manifest sha256
  `bd02b029999c12296cfa28ef65c059fa7bf04c02834c88185a5a68b89d35774e`
  **identical before and after** the whole inventory plus the runner
  selftest/check; 0 changed, 0 added, 0 removed. Filed bytes are untouched.
- **Runner:** `--selftest` → 26/26 exit 0; `--check` → exit 1, C pass,
  D fail (2), O fail (4), `missing_dependencies: [SKILL.md#<D4 decision-table
  subsection>]`.
- **Primary receipt:** `reports/round-19/validation.json` exists (320230
  bytes, runner sha `92093b55`) with the same verdicts; this seat did not
  write or overwrite it.
- **Runner revision churn (disclosed):** the runner's owner revised it again
  after this seat's final measurement — sha `92093b55` →
  `ffee0643b9a77780eab6e375f0186aca475b3293e495b2213b30c3ae420b5dd8`
  (2026-10-18T12:34:55Z), with the claim verdicts unchanged (C pass, D/O
  fail). Every measurement here stays bound to `92093b55`.

## 6. Limits

- All measured artifacts are NON-CANON. This draft does not certify truth,
  canon, lore acceptance, cultural permission, or any real-world rights
  position.
- C's PASS is a point-in-time measurement at runner sha `92093b55` on the
  delivered tree; a later entry edit needs a re-measurement, not an inherited
  PASS.
- D and O are blocked on integration artifacts (SKILL.md landing; a green
  battery), not on a measured defect of the landed C evidence. Their exact
  failures are named above.
- The runner and the battery were both revised inside the wave; every reading
  is hash-bound to the revision named and none is asserted settled.
- The 40-minute gap between the watcher's last poll and the final measurement
  is real wall-clock; the wave stayed in flight and neither D artifact landed
  in it.

## 7. Commands

- `python3 reports/round-19/run-validation.py --selftest` → 26/26, exit 0.
- `python3 reports/round-19/run-validation.py --check` → C pass, D fail,
  O fail; no write.
- `python3 tools/check-gate-battery.py` → exit 2, `9/9` coverage, 8 pass /
  1 unevaluable (`d4-assembly-check-gate.py`).
- `python3 .scratch/x23-rerun.py` → 17/19 regressions green; filed rounds
  8–18 preserved (821 files, digest `bd02b029…`).
- `grep -c 'D4' SKILL.md` → 0 (SKILL.md byte-unchanged through 12:32Z).
- `ls corpus/knowledge/verification/*.md | wc -l` → 20;
  `ls corpus/knowledge/synthesis/*.md | wc -l` → 29.
