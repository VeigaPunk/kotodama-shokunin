Restored in round 83 from those committed receipts: `reports/round-82/telemetry/counter-r1-redbefore.txt`, `reports/round-82/telemetry/counter-r2-caught.txt`, `reports/round-82/telemetry/lands-o82-graded-r2.txt`, `reports/round-82/telemetry/lands-o82-graded-r3.txt`, `reports/round-82/telemetry/selftest-o82-r2.txt`, `reports/round-82/telemetry/selftest-o82-r3.txt` and `reports/round-82/telemetry/counter-r3-mutation.txt`, with the row set from `corpus/lessons/round-82.md` `## Mistakes` R82-M6. The round-82 report's citation was honest: the record it named had committed bytes, which were then truncated to 0 bytes later in the round (see Provenance).

# Counter revisions — round 82

QUALITY 23: a leg or scenario changed after the freeze is a recorded counter revision with its red-before. The freeze commit `25907323` carries r1; the two revisions below land after the claims were first graded, and no claim predicate moved.

## Provenance

The r1→r2 record was committed in `696835ee5a8f8361031262f02d88299ea775ff1a` (3439 B at `reports/round-82/counter-revisions.md`) and the r3 extension in `ea667212554f7062650ee6942d559bdd35736c05` (5205 B). The path was then truncated to 0 bytes in `d1129213` (the round-82 claim-D counter r2 commit), and it is 0 bytes at base `3088bd7fe2a55a123214abba7008dcddf12b301c`. This file is the round-83 restoration from the committed receipts above. Where the earlier committed text quoted a `QUEUE` failure line that the committed `counter-r2-caught.txt` does not print, this text states only what that receipt prints.

## `reports/round-82/accept-o82.py` — r1 → r2 (claim O)

Commit `696835ee5a8f8361031262f02d88299ea775ff1a`.

| | |
|---|---|
| r1 sha256 (at freeze `25907323`) | `77b8c19d61cdcae5a9d10fc2e089d772455014bb210a90577b72b1c10d313030` |
| r2 sha256 | `3b339c5049c861579c04d649c2badf84ae4baf0561ab6479a4c8cd6c53579908` |
| leg set | unchanged — `FROZENCFG, TOOL, SELFTEST, QUEUE, MODULAR, ERROR, SEPARABLE` (LEGCOUNT unaffected) |
| frozen config | unchanged (`reports/round-82/claims.json` at the freeze) |

**Why.** Two wave seats attacked the frozen instrument and both found the same class: the counter under-enforced its own contract. Wave evidence: `.ufo/waves/round-82/w1/CriticClaimO.md` §3–§4 (control receipts pass 7/7 with the `DUE <id> <date>` lines removed, with a decoy summary line, and with a one-day-shifted NNd arithmetic invisible to every leg) and `.ufo/waves/round-82/w1/MutationTesterO.md` (one of five counter-predicate mutants killed).

**What changed — three contract limbs and one selftest addition, no predicate moved:**

1. **QUEUE now checks the DUE set, not only the four counts.** Each graded run's `DUE <id> <iso>` lines are compared, in order, with the counter's own `due_ids()` parse of the same blob. At the projection date that is 813 lines matched id-for-id (`reports/round-82/telemetry/lands-o82-graded-r2.txt`, `813 DUE ok`).
2. **QUEUE requires exactly one summary line** per run; a decoy line before the real one is a failure, not a last-match-wins pass.
3. **MODULAR gains an NNd boundary probe.** Four synthetic `NNd` rows are appended whose due dates land exactly on as-of, as-of+1, as-of+window and as-of+window+1; the tool's counts and DUE set must equal the counter's own parse. `reports/round-82/telemetry/lands-o82-graded-r2.txt` records `NNd boundary ok (1/20/14/831, 1 DUE)`.
4. **The selftest gains two proving scenarios** (14 checks, was 12): a doubled summary line must fail QUEUE, and a one-day-shifted NNd arithmetic must fail MODULAR — both were green under r1 (`reports/round-82/telemetry/selftest-o82-r2.txt`, `SELFTEST-O82: PASS (14 checks)`).

**Red-before (`reports/round-82/telemetry/counter-r1-redbefore.txt`).** A fixture clone whose tool lands a one-day-shifted NNd arithmetic with a self-reported green selftest is graded **`ACCEPT-O-82: PASS legs=7/7`** by r1.

**Red-after (`reports/round-82/telemetry/counter-r2-caught.txt`).** The same fixture is graded `ACCEPT-O-82: FAIL legs=5/7` by r2, with `LEG FAIL MODULAR (… NNd boundary FAIL (tool (0, 20, 14, 831) vs counter (1, 20, 14, 831); due 0 vs 1))`. The receipt prints five passing legs and MODULAR red; QUEUE is the other red leg by the 5/7 count, and the committed receipt does not print its detail line.

**Re-grade at the real lands (`reports/round-82/telemetry/lands-o82-graded-r2.txt`).** `ACCEPT-O-82: PASS legs=7/7`, exit 0, at `41c6de89` with freeze `25907323`; the receipt shows `813 DUE ok` and `NNd boundary ok`.

**Residual, stated.** The SELFTEST floor remains self-reported (the counter trusts the tool's printed check count); it binds runnability, not the count's truth. A tool that prints a green selftest it did not run passes that leg — the MODULAR and QUEUE limbs are what catch arithmetic and output lies. The `--registry` and `--window` defaults are never exercised, and a registry row shaped like a registry row inside prose is counted (file-wide regex).

## `reports/round-82/accept-o82.py` — r2 → r3 (same round, mutation closure)

Commit `ea667212554f7062650ee6942d559bdd35736c05`.

| | |
|---|---|
| r2 sha256 | `3b339c5049c861579c04d649c2badf84ae4baf0561ab6479a4c8cd6c53579908` |
| r3 sha256 | `07e4b2db136c213002ed80e5a15bd64a229d229aa675712931d95a03414422f1` |
| leg set | unchanged (7 legs) |

**Why.** `MutationTesterO` measured r1's mutation score at **1/5** and named four honest coverage gaps; r2 closed the two boundary gaps, r3 closes the rest.

**What changed — selftest only, no leg logic touched: two more scenarios (the commit message says `three more`, but the selftest count moves 14 → 16 and the diff adds the two below).** `junk: rows-less summary` (a `RECHECK-QUEUE: … on-release` line with the `/ N rows` field dropped) must fail QUEUE; `junk: due count grows with the population` (a tool correct on the frozen registry that adds one due when a 365d neutral row is appended) must fail MODULAR — this isolates the neutral-row expectation that a trivialised expectation would bypass. The doubled-summary and shifted-NNd scenarios added in r2 stay. Selftest 14 → 16 checks (`reports/round-82/telemetry/selftest-o82-r3.txt`, `SELFTEST-O82: PASS (16 checks)`).

**Mutation score.** Re-run of the five mutants the wave's seat ran against r1: **5/5 killed** under r3 (`reports/round-82/telemetry/counter-r3-mutation.txt`), against 1/5 under r1 (`MutationTesterO.md`). The r1→r2 boundary kills are recorded in `reports/round-82/telemetry/counter-r2-caught.txt`.

**Re-grade.** `reports/round-82/telemetry/lands-o82-graded-r3.txt`: `ACCEPT-O-82: PASS legs=7/7`, exit 0, at lands `41c6de89` with freeze `25907323`; `reports/round-82/telemetry/selftest-o82-r3.txt`: `SELFTEST-O82: PASS (16 checks)`.

**Residual, stated.** The SELFTEST floor is still self-reported (a tool printing a green selftest it did not run passes that leg — MODULAR and QUEUE are what catch output lies), and `--registry`/`--window` defaults plus the file-wide row regex remain unexercised gaps named by `CriticClaimO` §7.
