# RevCounterO — attack on `reports/round-66/accept-o.py` (claim O)

Seat: L1-kotodama-r66.RevCounterO · 2026-10-24 · lane `kotodama-shokunin` · base `94209e8f`
Artifact attacked: the frozen counter `reports/round-66/accept-o.py`, its MUT fixtures
(`.ufo/waves/round-66/stage/mut-o/`), and the tool it grades (`tools/check-claim-separability.py`).
No installs, no repo/jj/index writes; probes ran in `/tmp/r66o` against copies.

## Verdict

`ACCEPT-O-66: PASS` on the frozen content, sha256 `681743e3850b8281fb4ae9ecaef7e10b595750ee79201ce96b6c9cc7ede9d409`
(preserved at `.ufo/waves/round-66/stage/mut-o-counter/pristine/accept-o.py`, identical sha).
Observed run: 10/10 legs PASS, wall 6.70 s, `MUT PASS mutants=4 failing=[]`, `FIXTURES PASS lanes=2`.
No live leg fails. What follows is false-pass surface, not a red leg — except F7, which is live.

## Direct answers

**(1) Does the MUT table cover every mutant in `mut-o/`? Can any survive?**
Today: yes, complete — the directory holds exactly the four pinned `.py` files, each pin is
discriminating against a pristine copy (verified: pristine fails all four expectations; each
mutant satisfies only its own pin). No file survives *today*. Survivors exist as classes:

- **Non-`.py` or nested mutants are neither executed nor flagged.** The extra-file guard is
  `if fname.endswith(".py") and fname not in mut_expect` (accept-o.py:238) over a flat
  `os.listdir`. Demonstrated with the literal loop on a synthetic dir: `mut5_no_jobs.py.orig`,
  `mut6_static.py.bak`, `nested/mut7_timeout.py` → `scan flags: []`, all three "present but
  undetected". A `.patch`/`.orig`/`*.py.bak`/subdir mutant passes the leg silently.
- **Mutants that do not run count as kills at two of four pins.** `mut3` expects
  `"skipped=0" in stderr or "skipped=" not in stderr`; `mut4` expects `"UNRESOLVED" not in stdout`.
  A `SyntaxError` copy and a `ModuleNotFoundError` copy placed at those names produced
  `killeval={'mut3': True, 'mut4': True}` (empty stdout/stderr, rc=1) — a file that never
  executes is scored as killing the pinned leg. Fix: require `rc == 2` **and**
  `SEPARABILITY_PARTIAL` in each of those two expectations.
- **No freshness/content binding.** Nothing asserts a mutant is derived from the current
  `tools/check-claim-separability.py`; and the name→behavior map is unverified (a file named
  `mut1_*` that emits PARTIAL but breaks a different flag still passes). Currently the four
  do differ from the tip tool (sha `5c728e96…`) by exactly one hunk each
  (accept-o.py:833, 734, 697, 823 of the tool) — verified now, ungated.
- **Unpinned behaviors:** there is no mutant for `--jobs`, `--static-only`, or `--timeout`,
  though claim O names all three. Combined with F2/F5, those flags have no mutation evidence.

**(2) Is BOUND's `sleep 1.5` vs `budget 0.5` deterministic, or racy under load?**
Deterministic, in the pass/fail direction. 14/14 runs on the loaded host: `rc=2`,
`bound_ok=True`, wall 1.55–1.56 s, skip always at `repair attempt skipped`, never `<base>`.
Load can only *advance* expiry (never lengthen the 1.5 s sleep), and a budget sweep
0.02/0.05/0.08/0.12/0.2/0.3/0.5 s shows the first `take()` still precedes expiry even at
0.02 s (setup between `_Budget.__init__` and the first run is <20 ms), so load cannot even
turn the leg vacuous today. The `unevaluated` guard in the tool (`if not repairs and not
unevaluated`, tool:737) also means a >10 s stall that degrades the run to a timeout still
yields UNRESOLVED/partial rather than a fabricated `<base>` finding — the leg tolerates it.
Residual (see F1): BOUND *cannot tell* the intended path ("budget cut a running acceptance")
from "budget expired before any run" — the always-expired mutant produces the same PASS with
`acceptance_runs=0`. It is deterministic but not evidence of budget accounting.

**(3) Can FIXTURES pass while the tool's verdict is silently wrong elsewhere?**
Yes, and it is vacuous by construction: `leg("FIXTURES", fixtures_built >= 2 and wall < 180)`
(accept-o.py:247) only counts `make_lane` calls and total script wall time (`t_start` is set
before SELFTEST at :114, so it is not a fixture-harness bound), while its own leg text claims
"3 temp git lanes" and the observed value is `lanes=2`. More broadly: **no leg of ACCEPT-O-66
requires a positive verdict** (exit 0, `skipped=0`) on a genuinely independent dynamic
manifest; the only exit-0 scenarios live inside the tool's self-graded `--selftest`, and one
of those (:1186, "`--jobs` leaves the verdict unchanged") is exactly what doing nothing
satisfies. Proven end-to-end below (F1, F2).

## Findings by severity

### HIGH — F1. `--budget` passes the whole predicate when implemented as "always expired"
Mutant: `self._deadline = None if budget is None else 0.0` (tool:685; value ignored).
Measured, with the harness's own argv and fixtures:
- `--selftest` → rc 0, `selftest: 63/63 checks passed` (SELFTEST PASS).
- BOUND argv (`--budget 0.5 --timeout 10`, lane 1) → rc 2, `SEPARABILITY_PARTIAL`,
  `SEPARABILITY_UNRESOLVED C acceptance never ran`, `acceptance_runs=0 skipped=1` →
  `bound_ok=True`. i.e. **zero acceptance runs**, and the leg still passes.
- STATIC/MAXRUNS/JOBS/OPTIONS → True (they never pass `--budget`; executed, not inferred).
- DIFF/FIXTURES unaffected; MUT runs `mut-o/*`, not TOOL → PASS.
No positive budget control exists anywhere: `--budget` is only ever exercised with a value
that *must* expire (accept-o BOUND; selftest:1209-1219). A tool that treats any budget as
exhausted — reporting every budgeted run as partial with 0 runs — prints
`ACCEPT-O-66: PASS`. That is precisely the "returns a verdict inside a round's budget"
capability collapsing to a no-op, i.e. a false stamp of the round-65 fix.
Suggested leg: generous `--budget` (e.g. 30) on the fast lane must equal the no-budget verdict
(same findings, same exit, `skipped=0`); plus the selftest scenario the tool lacks.

### HIGH — F2. `--jobs` has no positive evidence; a serial tool passes everything
Mutant: `if True: return [task() for _, task in tasks]` (tool:811; parallel branch removed).
Measured: JOBS leg inputs → `j1 rc=1 j4 rc=1 eq=True`, findings non-empty → JOBS PASS; and
`--selftest` → `rc=0`, 63/63. So the "`--jobs` parallelizes unit tasks" half of claim O is
asserted only as *verdict equality*, which an ignored flag satisfies exactly. The round-65
root cause (serial dynamic leg exceeding the 600 s cap) can therefore remain entirely unfixed
while ACCEPT-O-66 passes. Suggested leg: observable parallelism — N units each sleeping ~1 s
with `--jobs N` must finish well under `N × sleep`, with `acceptance_runs=N`; and a
jobs-ignored mutant pinned in MUT.

### MEDIUM — F3. `--timeout` semantics has no external assertion
`want_opts` (accept-o.py:135) omits `--timeout`, BOUND only passes `--timeout 10` against a
1.5 s acceptance, and no fixture exceeds its timeout. A tool that accepts and ignores
`--timeout` passes all 10 legs; only the self-graded selftest (:1113, "timeout after 1s") would
notice, and F1/F2 show that self-grading is not load-bearing. Claim O explicitly says
"per-run `--timeout` unchanged", so this leg is load-bearing for the claim.

### MEDIUM — F4. MUT pin table accepts non-running mutants and misses non-`.py`/nested files
See answer (1) with observed evidence. Live risk is nil today (4 pinned `.py` files only);
the gate is name/extension-based, not content- or execution-based. Fix: recursive scan of
every file under `mut-o/`, and each expectation must assert a real verdict
(`rc == 2` + `SEPARABILITY_PARTIAL`) so a crash cannot count as a kill.

### LOW — F5. FIXTURES is a vacuous counter with a wrong descriptor
`lanes=2` observed vs "3 temp git lanes" in its own leg text (accept-o.py:9/247); the 180 s
bound covers the whole script. It asserts nothing about the tool's verdict (see answer 3).

### LOW — F6. SELFTEST pins the literal `63/63`
A legitimate tool change that adds a check fails the entire acceptance. Observed firing: peer
receipt `.ufo/waves/round-66/stage/mut-o-counter/runs/pristine.out` shows the frozen counter
printing `SELFTEST FAIL exit=0 selftest: 63/64 checks passed` against a tool at another
revision (lane tool today is still `5c728e96…`, `63/63`). Also drift: `claims.json`'s MUT leg
names three mutants; the code pins four (`mut4_suppress_unresolved` is unclaimed).

### HIGH (integrity) — F7. The frozen counter was mutated in place mid-wave and no longer parses
- Content I measured (PASS, 10 legs): sha256 `681743e3…` (self-printed by the counter).
- Live `reports/round-66/accept-o.py` at 2026-10-24 08:35:36 -0300: sha256 `f08ff6e8…`,
  11766 bytes, syntax error at line 117 —
  `legs = []")"]")` — plus an injected `REVISION` block that returns 2 when
  `git rev-parse main` is not a 40-hex sha. `python3 -c "ast.parse(...)"` → `SyntaxError`.
- `reports/round-66/` is untracked in git at base (`git status --porcelain` → `??`), so the
  only content pin is the printed self-sha; the pristine copy survives at
  `stage/mut-o-counter/pristine/` and `w1/mut-entry-scratch/`.
Consequence: the PASS receipt is valid **only** for `681743e3…`. If the L1 integrates the
current file, the predicate does not parse and claim O has no leg evidence at all; if the
`REVISION` leg is meant to be integrated, that is a new predicate revision (11 legs, new
exit-2 contract) and the pre-data revision-0 counter should be re-declared rather than edited
silently. Requirement for the receipt: bind `# counter sha256 (self): 681743e3…` and ship a
file with that sha.

## Residual risk / verification gaps

- **No end-to-end bounded run on the round's own manifest.** BOUND is a 2-unit micro-fixture;
  `reports/round-66/separability-manifest.json` was absent at probe time
  (`stage/separability-real-probe.txt` says `telemetry/separability-real.txt` is the REC
  seat's receipt). So even with F1/F2 fixed, ACCEPT-O-66 would prove boundedness on 2 units,
  not on the round-65 shape (N≈20 units, one full counter run ≫ 600 s). Dependency, not a
  judgement: the operability claim's decisive number is not produced by this counter.
- JOBS compares only `SEPARABILITY_DEPENDENCY` lines plus exit codes; parallel-mode
  differences in `skipped`/`acceptance_runs` (budget-vs-jobs interaction, i.e. the actual
  reason `--budget` exists) are invisible. `_Budget.take()` is lock-guarded, but no fixture
  runs `--budget` together with `--jobs > 1`.
- MUT pins are unbound to the tool's content (F4), so a stale mutant set would still grade.
- I did not read `accept-c.py`/`accept-ca.py` or any other lane artifact; scope was claim O's
  counter. Findings F1–F7 are reproducible from the commands quoted above (probe sources:
  `/tmp/r66o/probe*.py`, ephemeral; every observation is restated inline with its argv).
