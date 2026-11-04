# Counter revisions — round 82

QUALITY 23: a leg or scenario changed after the freeze is a recorded counter
revision with its red-before. The freeze commit `25907323` carries r1; the
revision below lands after the claims were first graded, and no claim predicate
moved.

## `reports/round-82/accept-o82.py` — r1 → r2 (claim O)

| | |
|---|---|
| r1 sha256 (at freeze `25907323`) | `77b8c19d61cdcae5a9d10fc2e089d772455014bb210a90577b72b1c10d313030` |
| r2 sha256 | `3b339c5049c861579c04d649c2badf84ae4baf0561ab6479a4c8cd6c53579908` |
| leg set | unchanged — `FROZENCFG, TOOL, SELFTEST, QUEUE, MODULAR, ERROR, SEPARABLE` (LEGCOUNT unaffected) |
| frozen config | unchanged (`reports/round-82/claims.json` at the freeze) |

**Why.** Two wave seats attacked the frozen instrument and both found the same
class: the counter under-enforced its own contract. Wave evidence:
`.ufo/waves/round-82/w1/CriticClaimO.md` §3–§4 (controls B and C pass 7/7 with
the `DUE <id> <date>` lines removed and with a decoy summary line; an NNd
±1-day arithmetic is invisible to every leg) and
`.ufo/waves/round-82/w1/stage/MutationTesterO/` (four of five counter-predicate
mutants survive).

**What changed — three limbs, no predicate moved:**

1. **QUEUE now checks the DUE set, not only the four counts.** Each graded run's
   `DUE <id> <iso>` lines are compared, in order, with the counter's own
   `due_ids()` parse of the same blob. At the projection date that is 813 lines
   matched id-for-id.
2. **QUEUE requires exactly one summary line** per run (a decoy line before the
   real one is a failure, not a last-match-wins pass).
3. **MODULAR gains an NNd boundary probe.** Four synthetic `NNd` rows are
   appended whose due dates land exactly on as-of, as-of+1, as-of+window and
   as-of+window+1; the tool's counts and DUE set must equal the counter's own
   parse. A shifted day-count arithmetic moves exactly those rows.
4. **The selftest gains two proving scenarios** (14 checks, was 12): a doubled
   summary line must fail QUEUE, and a one-day-shifted NNd arithmetic must fail
   MODULAR — both were green under r1.

**Red-before (measured, `telemetry/counter-r1-redbefore.txt`).** A fixture clone
whose tool lands a one-day-shifted NNd arithmetic with a self-reported green
selftest is graded **`ACCEPT-O-82: PASS legs=7/7`** by r1.
**Red-after (`telemetry/counter-r2-caught.txt`).** The same fixture is graded
`FAIL legs=5/7` by r2: `LEG FAIL QUEUE (… DUE lines 813 != counter due set 813
(first diff (('S005','2027-04-18'), ('S005','2027-04-17'))))` and
`LEG FAIL MODULAR (… NNd boundary FAIL (tool (0,20,14,831) vs counter
(1,20,14,831); due 0 vs 1))`.

**Re-grade at the real lands (`telemetry/lands-o82-graded-r2.txt`).**
`ACCEPT-O-82: PASS legs=7/7`, exit 0, at `41c6de89` with freeze `25907323`; the
receipt now shows `813 DUE ok` and `NNd boundary ok (1/20/14/831, 1 DUE)`.
The r1 graded receipt (`telemetry/lands-o82-graded.txt`) is kept as history.

**Residual, stated.** The SELFTEST floor remains self-reported (the counter
trusts the tool's printed check count); it binds runnability, not the count's
truth. A tool that prints a green selftest it did not run passes that leg — the
MODULAR and QUEUE limbs are what catch arithmetic and output lies. The
`--registry` and `--window` defaults are still never exercised, and a registry
row shaped like a registry row inside prose would be counted (file-wide regex).
