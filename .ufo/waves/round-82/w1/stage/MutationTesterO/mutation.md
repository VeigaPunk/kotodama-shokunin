# MutationTesterO — round-82 claim-O mutation run

Seat: `MutationTesterO` (leaf, godspeed). Date: 2026-11-04.
Target instrument (claim O's counter): `reports/round-82/accept-o82.py`
sha256 `77b8c19d61cdcae5a9d10fc2e089d772455014bb210a90577b72b1c10d313030` (25355 B) — hash recorded before any run and re-verified after all runs (see `hashes.txt`; the lane file was never writable by this seat).
Bounded detector: the counter's own `--selftest` (12 checks over a synthetic git fixture whose embedded reference tool encodes the contract predicates).
Baseline (pristine): `python3 -B pristine.py --selftest --work wd-pristine` → `SELFTEST-O82: PASS (12 checks)`, rc=0. All five mutants are single-line diffs of the pristine copy (proof: `mutant-diffs.txt`).

## Part 1 — five counter mutants

| # | File | One-line change (pristine line) | Detector verdict | Verdict line (pasted) | Caught by check(s) | Result |
|---|------|--------------------------------|------------------|-----------------------|--------------------|--------|
| M1 | `m1.py` | tally L125 `elif d <= as_of:` → `elif d < as_of:` | rc=0, all 12 ok | `SELFTEST-O82: PASS (12 checks)` | none | **SURVIVED** |
| M2 | `m2.py` | tally L127 `elif d <= as_of + datetime.timedelta(days=window):` → `elif d < ...` | rc=0, all 12 ok | `SELFTEST-O82: PASS (12 checks)` | none | **SURVIVED** |
| M3 | `m3.py` | tally L124 `exempt += 1` → `due += 1` (on-release counted as due) | rc=1, 3 checks FAIL | `SELFTEST-O82: FAIL (12 checks)` | `clean fixture PASS`; `QUEUE compares against the counter's own parse`; `MODULAR passes on a population-neutral append` | **KILLED** |
| M4 | `m4.py` | L43 `SUMMARY = re.compile(r"^RECHECK-QUEUE: (\d+) due / (\d+) upcoming / (\d+) on-release / (\d+) rows$")` → rows group optional `(?: / (\d+) rows)?` | rc=0, all 12 ok | `SELFTEST-O82: PASS (12 checks)` | none | **SURVIVED** |
| M5 | `m5.py` | MODULAR L333 `ok1 = g1[0] == t0[0] and ... and g1[3] == t0[3] + 1` → `ok1 = True` | rc=0, all 12 ok | `SELFTEST-O82: PASS (12 checks)` | none | **SURVIVED** |

M3 killing evidence (from `selftest-m3.log`):

```
SELFTEST FAIL clean fixture PASS 3d3b41246308d614bfe
LEG FAIL QUEUE (2026-11-04: tool (0, 1, 1, 3) != counter (1, 1, 0, 3); 2027-11-01: tool (2, 0, 1, 3) != counter (3, 0, 0, 3))
LEG FAIL MODULAR (neutral +1 row -> (0, 1, 1, 4); due +1 row -> (1, 1, 1, 4); frozen (1, 1, 0, 3))
ACCEPT-O-82: FAIL legs=5/7
SELFTEST-O82: FAIL (12 checks)
```

Why each survivor survived (all are fixture-shape facts, not detector bugs):

- **M1/M2 (boundary operators).** The selftest fixture registry has 3 rows: S001 `2026-10-19 | 365d` (due 2027-10-19), S002 `2026-10-19 | 30d` (due 2026-11-18), S003 `on-release`. The graded as-of dates are 2026-11-04 and 2027-11-01; MODULAR's due row is `opened=2026-01-01, recheck=<as-of − 1 day>`. No fixture due date ever equals an as-of date or `as_of + 90`, so `<=` vs `<` never changes a bucket. The QUEUE leg compares the counter's tally against the *unmutated* embedded reference tool, and MODULAR's expectations derive from the counter's own tally — every number stays equal.
- **M4 (rows-optional summary regex).** Every summary the counter parses in selftest comes from the counter-owned fixture tool (or the junk canned printer), which always prints `/ 3 rows`, so the optional group never binds and behavior is byte-identical. No check ever feeds the counter a rows-less summary. Latent hazard worth recording: if a deviant tool ever printed a summary without `/ N rows`, `int(None)` on the unmatched group would raise TypeError inside `main()`'s unguarded leg loop and crash the counter mid-grade instead of failing the leg cleanly.
- **M5 (MODULAR neutral expectation trivial).** Selftest never negative-tests MODULAR: no fixture makes the neutral append move due/upcoming/on-release, so `ok1 = True` still yields `LEG PASS MODULAR` and check 3 still sees a PASS (`ok2` is intact and the fixture neutral row is genuinely neutral).

Symmetric note: the same boundary gap covers the embedded reference tool string inside `selftest()` — mutating its `if d<=asof` / `d<=asof+...window` lines would survive for the identical missing-boundary reason.

**Mutation score (counter, killed/5): 1/5** (M3 killed; M1, M2, M4, M5 survived).

## Part 2 — tool-contract mutation vs the QUEUE leg (real registry)

Stub: `tool-stub-mutated.py` — the exact claim-O contract (`--registry` default `corpus/SOURCES.md`, `--as-of`, `--window` default 90, `--selftest`, `RECHECK-QUEUE:`/`DUE`/`RECHECK-ERROR` shapes, exit 2 without traceback on malformed rows/cadences, frozen shape markers present) with ONE predicate mutation: an `NNd` recheck cell means `opened + N*30 days` (contract: `opened + N days`). Its `--selftest` is self-consistent with the mutated predicate (8 checks), so a lying self-declared selftest cannot be distinguished from an honest one by the SELFTEST leg. Control: `tool-stub-control.py`, identical minus the mutation.

Fixture (scratch, created per seat spec; `git rev-parse --show-toplevel` asserted == fixture dir before first commit): real registry blob from base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` (991457 B, 827 rows) + real `reports/round-82/claims.json` with its `base` field re-pointed at the fixture's own base commit (the counter grades ancestry/SEPARABLE from that field). Driver: `fixture_driver.py` (full transcript `queue-probe.log`).

Counter's own independent tally of the real blob (run through `pristine.py`'s `tally`):

```
tally as-of 2026-11-04 window 90 -> (0, 18, 14, 827, 0)
tally as-of 2027-11-01 window 90 -> (813, 0, 14, 827, 0)
```

These equal the frozen claims.json "after" numbers (0/18/14/827 and 813/0/14/827), so the QUEUE comparison in the runs below is the exact comparison the leg would print in the real grade.

Mutated stub vs counter (`python3 -B pristine.py --root <fx> --lands 1a7d3cb5... --freeze 08e3bbeb... --work wd-mutated`):

```
LEG PASS FROZENCFG / TOOL / SELFTEST (SELFTEST: PASS (8 checks))
LEG FAIL QUEUE (2026-11-04: tool (0, 0, 14, 827) != counter (0, 18, 14, 827); 2027-11-01: tool (154, 0, 14, 827) != counter (813, 0, 14, 827))
LEG FAIL MODULAR (neutral +1 row -> (0, 0, 14, 828); due +1 row -> (1, 0, 14, 828); frozen (0, 18, 14, 827))
ACCEPT-O-82: FAIL legs=5/7   (rc=1)
```

The stub's own summaries on the same blob: `RECHECK-QUEUE: 0 due / 0 upcoming / 14 on-release / 827 rows` (as-of 2026-11-04) and `154 due / ... / 827 rows` (as-of 2027-11-01) — every `NNd` row (392×365d, 249×180d, 18×90d) is pushed +30 years and leaves the window; the 154 ISO rows are unaffected, which is why 154 due remain at projection while the counter expects 813.

Control stub vs counter (lands `bcce2809...`):

```
LEG PASS QUEUE (2026-11-04: 0/18/14/827 ok; 2027-11-01: 813/0/14/827 ok)
ACCEPT-O-82: PASS legs=7/7   (rc=0)
```

**Verdict: the QUEUE leg catches an `NNd`-semantics mutation against the real registry** — the counter's independent parse is the load-bearing check; a self-consistent `--selftest` does not shield a wrong cadence predicate. MODULAR also failed on the mutated run, but only collaterally: its frozen baseline `t0` is the counter's own tally, and its neutral probe row is a `365d` cadence whose due date (+1y vs +30y) is far-future under either interpretation — so MODULAR's catch is via the baseline mismatch, not via its population probe.

## Honest gaps (predicates no selftest check covers)

1. `due` boundary: `due_date <= as_of` vs `<` — no fixture row due exactly on a graded as-of (M1 survived).
2. `upcoming` boundary: `due_date <= as_of + window` vs `<` — no fixture row at exactly `as_of + window` (M2 survived).
3. MODULAR neutral-row expectation — no negative probe; trivializing `ok1` passes all 12 checks (M5 survived).
4. `SUMMARY` strictness (the `/ N rows` field is part of the tool contract) — no deviant-output probe; a rows-less summary would crash the counter with TypeError rather than fail the leg (M4 survived).

A fixture adding one row due exactly on each graded as-of and one at exactly `as_of+window`, plus one junk tool that prints a rows-less summary and one MODULAR-negative append, would close all four without touching the leg logic.

## Postscript — counter upgraded at freeze time (after this run)

All probes above graded the counter bytes as handed to this seat (sha256 `77b8c19d…`, 25355 B, 12 checks; mtime before 08:36). During report write-up the lane file at `reports/round-82/accept-o82.py` was replaced by the L1 freeze (sha256 `3b339c5049c861579c04d649c2badf84ae4baf0561ab6479a4c8cd6c53579908`, 30105 B, mtime 2026-11-04 08:40:10). Evidence: `diff -u <lane file> stage/MutationTesterO/m1.py` (pristine + the M1 line), captured in the seat transcript. The frozen delta:

- new `due_ids()` + QUEUE now requires **exactly one** summary line and compares the tool's `DUE` lines to the counter's own due set;
- MODULAR gains an **NNd boundary probe** (rows due exactly on as_of, one inside, one at exactly as_of+window, one outside) with `ok3` gating;
- selftest fixture tool emits `DUE` lines; two new junk checks: junk5 double-summary, junk6 NNd arithmetic shifted one day.

Consequence for the gaps ([INFERENCE] from the diff — no mutants were re-run against the frozen bytes, per the L1 wrap-up order):

- Gap 1 (M1 class) and Gap 2 (M2 class): **closed** — the boundary probe rows sit exactly on the two boundaries, so `<` vs `<=` in either direction now mismatches tool vs counter tally.
- Gap 4 (M4 class): **closed for the double-summary shape** by the exactly-one check (junk5). The `int(None)` crash on a *rows-less* summary remains latent ([INFERENCE]: the frozen QUEUE still builds `tuple(int(x) for x in m.groups())` under a rows-optional regex; no junk tool emits a rows-less summary).
- Gap 3 (M5 class): **still open** — no negative probe for the neutral-append expectation (`ok1` trivially true still yields PASS with `ok2` and the boundary `ok3` intact).
- The NNd→N×30 stub mutation would now be caught by QUEUE (as measured) *and* by the MODULAR boundary probe ([INFERENCE]).

Measured score stands for the graded bytes: **1/5**. Against the frozen bytes the inferred score is 4/5 with gap 3 (and the latent rows-less crash) remaining.

## Files (all under `.ufo/waves/round-82/w1/stage/MutationTesterO/`)

`m1.py`–`m5.py` (the five counter mutants), `tool-stub-mutated.py`, `tool-stub-control.py`, `selftest-m1.log`–`selftest-m5.log` (detector runs incl. rc), `queue-probe.log` (fixture driver transcript), `mutant-diffs.txt` (one-line diff proofs), `hashes.txt` (lane-before/after + artifact hashes + verdict lines). Scratch dir `/fast/scratch/hyaku/kotodama-r82/MutationTesterO` removed after capture; nothing was installed; lane, lane git/jj state, and fleet untouched.
