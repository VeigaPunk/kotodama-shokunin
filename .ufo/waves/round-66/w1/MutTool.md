# MutTool — mutation probe of `tools/check-claim-separability.py` (round 66, claim O)

Seat: `L1-kotodama-r66.MutTool` (mutation-tester, leaf). Milestone r66-v2.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `94209e8f80969dbac48d56c5d0e2e623635b8616`.
Scope: three mutants **beyond** the four committed under `.ufo/waves/round-66/stage/mut-o/`.
Verdicts below are stated with the detector revision that produced them.

## Target bytes and detector revision

| artifact | sha256 |
|---|---|
| `tools/check-claim-separability.py` (pristine, lane working tree) | `5c728e96dbe39b0ded511158679dc0cb10d362982809a2411959eef0985f4d98` |
| `reports/round-66/accept-o.py` used by every run below | `681743e3850b8281fb4ae9ecaef7e10b595750ee79201ce96b6c9cc7ede9d409` |
| `reports/round-66/accept-o.py` **as it is on disk now** (changed by another seat mid-probe, see F5) | `f08ff6e8fb22e3399519d4d87815b9ce9badc16bb9682ed5afcfb787da276199` |
| mutant 1 (default timeout) | `d8b179e35d93b07951de41c28f9cc469549d5cbb7d3e1566c307cbbf2737974d` |
| mutant 2 (UNRESOLVED then exit 0) | `7004a6847551d9c5301de6f735aa7a37432f21128238d3db992e5e9fb68bb301` |
| mutant 3 (unsorted UNRESOLVED) | `90b0ecaaa54778162d246c50f7fc743879def9ca256e3e2e516533b18103b5a4` |

Every accept-o run prints `# counter sha256 (self)`; all five runs recorded `681743e3…`, so the whole
matrix is one detector revision. Each mutant is a **one-line** delta from pristine (`diff -u` verified,
all compile), applied only to a throwaway `git clone --shared --no-checkout` of the lane at
`/tmp/muttool-r66/root` (tool + the four committed mutants copied in); the lane's own tool file was
never written. Run command, identical for all rows:

```
cd <lane> && python3 -B reports/round-66/accept-o.py --root /tmp/muttool-r66/root
```

## Results

| # | mutant (single line changed) | expected detector | observed | verdict |
|---|---|---|---|---|
| 0 | pristine | ACCEPT-O-66 PASS | `ACCEPT-O-66: PASS` exit 0, 9/9 legs, `FIXTURES wall=6.4s` | baseline good |
| 1 | `DEFAULT_TIMEOUT = 600.0` → `99999.0` | a leg pins the per-run default | **`ACCEPT-O-66: PASS` exit 0**, all 9 legs | **SURVIVED** (coverage finding F1) |
| 2 | `return EXIT_INPUT` → `return EXIT_OK if unresolved else EXIT_INPUT` (report, line 837) | exit-code contract for a partial verdict | `SELFTEST FAIL exit=1 selftest: 59/63`, `BOUND FAIL exit=0`, `STATIC FAIL exit=0`, `MAXRUNS FAIL exit=0`, `ACCEPT-O-66: FAIL` exit 1 | **KILLED** (4 legs) |
| 3 | `for line in sorted(unresolved)` → `for line in unresolved` (line 826) | a fixture with ≥2 UNRESOLVED lines asserts order | **`ACCEPT-O-66: PASS` exit 0**, all 9 legs | **SURVIVED** (coverage finding F2) |

Mutants are at `.ufo/waves/round-66/w1/MutTool-scratch/mutants/`, raw captures at
`…/MutTool-scratch/logs/accept-o-{baseline,mut1,mut2,mut3}.txt`.

## Mutant 1 — per-run default timeout raised 600 s → 99999 s: SURVIVED

Point: `DEFAULT_TIMEOUT = 600.0` (line 100) feeds `--timeout`'s argparse default and therefore
`subprocess.run(..., timeout=timeout)` in `_run_acceptance` (line 561-565), the only wall bound that
exists when `--budget` is absent (`_Budget.__init__`: `self._deadline = None if budget is None`).

Full detector output on the mutant (copy: `logs/accept-o-mut1.txt`):

```
SELFTEST PASS exit=0 count=63/63
DIFF PASS diff_lines=430          # baseline was 428: only "non-empty" is asserted
OPTIONS PASS missing=[]           # only the four option NAMES are asserted
BOUND PASS exit=2 partial=True unresolved=True
STATIC PASS exit=2
MAXRUNS PASS exit=2
JOBS PASS j1=1 j4=1 eq=True
MUT PASS mutants=4 failing=[]
FIXTURES PASS lanes=2 wall=6.5s
ACCEPT-O-66: PASS
```

Why no leg can see it: `OPTIONS` (accept-o.py:~163) computes `missing = [o for o in want_opts if o not in h.stdout]`
— presence of `--timeout`-adjacent knobs only; `BOUND`/`MAXRUNS` pass `--timeout 10`/`--timeout 10`
explicitly; the tool's own selftest always passes `--timeout 1` explicitly where the value matters;
`DIFF` accepts any non-empty delta. Observable residue the mutant does leave:

```
$ pristine --help   →  --timeout TIMEOUT     seconds allowed per acceptance run (default 600)
$ mut1     --help   →  --timeout TIMEOUT     seconds allowed per acceptance run (default 99999)
```

Severity: the claim text for O says "**per-run `--timeout` unchanged**". This mutant violates the
statement while satisfying every frozen leg — the legs are strictly weaker than the statement.
Operationally it re-opens R65-D4 for any caller that omits `--budget`: a hung acceptance now burns
27.8 h per run instead of 10 min. The frozen manifest command passes `--timeout 120` explicitly, so
the round's own check is unaffected; the regression is latent for the next caller.

Minimal pin (one line, deterministic, no sleeping): in `OPTIONS`, also require the help text to name
the default, e.g. `"default 600" in h.stdout` (fails on mut1 with `missing=[]` untouched). A
behavioural pin is not practical in-round: at 600 s the difference is unobservable inside any 180 s
budget, so the honest pin is textual/structural (`DEFAULT_TIMEOUT == 600.0`), not functional.

## Mutant 2 — UNRESOLVED printed but exit 0: KILLED

Point: `report()` line 836-837, `if partial: return EXIT_INPUT` → `return EXIT_OK if unresolved else EXIT_INPUT`.
The partial text is still printed, so this is exactly the "honest message, dishonest code" mutant.

Detector output (`logs/accept-o-mut2.txt`): `SELFTEST FAIL 59/63`, `BOUND FAIL exit=0`,
`STATIC FAIL exit=0`, `MAXRUNS FAIL exit=0`, `ACCEPT-O-66: FAIL` exit 1. The four failing selftest
checks (`--selftest` on the mutant):

```
FAIL bound: --static-only skips the dynamic leg and exits 2: rc=0 want 2
FAIL bound: --max-runs 1 skips the repair attempts: rc=0 want 2
FAIL bound: --budget that expires skips runs: rc=0 want 2
FAIL bound: static-only counts one skipped run per dynamic unit: rc=0 want 2
```

So the report's exit-code contract is enforced at **four** independent points (one selftest check per
skip path, plus three accept-o legs). Note the mechanism: the legs hard-code `returncode == 2` per
scenario; there is no general "documented exit map ↔ behaviour" check, but every skip path that can
produce UNRESOLVED has a scenario, so the class is closed. My mutant adds no kill power beyond the
committed `mut1_no_partial_exit.py` — it is a second, independent byte-point on the same class.

## Mutant 3 — unresolved sort dropped: SURVIVED

Point: line 826 `for line in sorted(unresolved):`. The tool documents sorted *finding* lines only
(docstring: "Output: finding lines sorted"); the unresolved sort is an unnamed invariant, and this
mutant deletes it.

The frozen harness cannot see it: **every** accept-o fixture lane has exactly one acceptance unit
(lane 1: C has `acceptance`, S has `exports` only; lane 2: same; the MUT leg reuses lane 2), and the
tool's own two `--static-only` selftest scenarios likewise have exactly one dynamic unit. So every
UNRESOLVED list the harness can produce has one line, and the sort is unobservable; `STATIC`/
`MAXRUNS`/`BOUND` assert presence of the line, never order.

Order-sensitive probe (mine, absent from the harness) —
`.ufo/waves/round-66/w1/MutTool-scratch/probe_unresolved_order.py`: a temp lane with **two** dynamic
units declared `Z` then `A`, run `--static-only`, 5 repeats:

```
pristine: run=1..5 exit=2 unresolved=2 order=['A', 'Z'] sorted=True   PROBE PASS
mutant3 : run=1..5 exit=2 unresolved=2 order=['Z', 'A'] sorted=False  PROBE FAIL
```

Correction to the tasking's premise: the mutation is **not nondeterministic**. `unresolved` is
accumulated from `_run_unit_tasks`, whose `pool.map` preserves submission (manifest) order, and the
static-only branch builds the list in `dyn_units` order — so the mutant emits a *stable*
manifest-order list on every run (5/5 identical above). Nondeterminism would need `--jobs > 1` plus
set iteration; neither path does that. What the mutant actually breaks is the lexicographic output
order, i.e. a byte-level diff between a pristine and a mutated receipt of the same run — which is
precisely what a receipt-and-re-derive round (claim Ca, D2/D4) compares. Severity: low for the
verdict, non-zero for receipts; a repeat-N detector will *never* flag it as flaky.

Minimal pin: add one accept-o leg (`ORDER`) = my probe, or fold a 2-dynamic-unit `--static-only`
scenario into the tool's selftest and assert `unresolved_lines == sorted(unresolved_lines)`.
Caveat for the L1: the selftest is pinned to `63/63` by accept-o's `SELFTEST` leg, so a selftest pin
forces a leg-text change; a separate accept-o leg avoids touching the `63/63` contract but changes
`claims.json`'s leg list — **I do not change the contract**, this is a flag for the integrator.

## Harness integrity observations (no action taken)

1. The MUT leg enumerates `stage/mut-o/*.py` and reports `unpinned` for any name outside
   `mut_expect`, so a mutation-tester cannot smuggle mutants into O's land without editing
   accept-o.py — good. My three mutants therefore live under `w1/MutTool-scratch/`, not in that dir.
2. `mut_expect` predicates are coarse (e.g. `mut1_no_partial_exit`: `"PARTIAL" in stdout and rc != 2`).
   A mutant that breaks PARTIAL *and* the findings would still satisfy that predicate. Second-order
   risk only: the predicates test "the pinned failure mode is present", not "only that mode is present".
3. `DIFF` accepts any non-empty delta (428 → 430 lines on mut1 still PASS), so it proves "a change
   landed", never "the intended change landed". That is what the behavioural legs are for; keep it
   that way and do not treat DIFF as a content pin.

## F5 (blocker, not mine to fix) — the detector changed mid-probe and does not compile

While this seat ran, `reports/round-66/accept-o.py` was rewritten by another seat
(mtime `2026-10-24 08:35:36.696987447 -0300`, sha `f08ff6e8…`, 265 lines). At snapshot time it has a
spliced half-patch and **no longer parses**:

```
  File "reports/round-66/accept-o.py", line 117
    legs = []")"]")
                ^
SyntaxError: unmatched ']'
```

The inserted block (lines ~117-122) splices a new `REVISION` guard and then re-declares `mv`,
`self_sha` and `legs = []`, with the corrupt `legs = []")"]")` line as the seam. Consequences:

- `ACCEPT-O-66` currently **cannot run at all**; stamping O on this file would be a fabricated PASS.
- My verdicts are pinned to `681743e3…` (every run recorded it; baseline PASS on it). Re-verification
  of mutants 1 and 3 against the current revision is **pending**: re-running it now yields the
  SyntaxError above, not a verdict. Frozen snapshot kept at
  `…/MutTool-scratch/logs/accept-o-current-broken-snapshot.py` for the integrator.
- Textually, the in-progress revision still contains no default-timeout pin and no unresolved-order
  assertion (grep: no `default 600`, no `ORDER` leg, no `sorted(unresolved)` check), so F1/F2 look
  un-closed there too — but that is a reading of non-executing bytes, not a verdict.

## Restoration evidence

| step | evidence |
|---|---|
| clone tool restored from lane pristine bytes | `5c728e96…` == lane `5c728e96…` == `mutants/pristine.py` `5c728e96…` |
| detector re-run on restored clone | `ACCEPT-O-66: PASS` exit 0, `MUT PASS mutants=4 failing=[]` (self sha `681743e3…`) |
| lane tool never written | sha unchanged `5c728e96…`; `git diff --stat BASE -- tools/check-claim-separability.py` identical before/after: `254 insertions(+), 39 deletions(-)` |
| lane detector not written by me | my only lane writes are under `.ufo/waves/round-66/w1/` (list below) |
| scratch clone | `/tmp/muttool-r66` removed after restoring |

Lane writes by this seat (all inside the wave dir, all additive):

```
.ufo/waves/round-66/w1/MutTool.md
.ufo/waves/round-66/w1/MutTool-scratch/mutants/{pristine,mut1_default_timeout,mut2_unresolved_exit0,mut3_unsorted_unresolved}.py
.ufo/waves/round-66/w1/MutTool-scratch/probe_unresolved_order.py
.ufo/waves/round-66/w1/MutTool-scratch/logs/{accept-o-baseline,accept-o-mut1,accept-o-mut2,accept-o-mut3,mut1-r2,mut3-r2}.txt
.ufo/waves/round-66/w1/MutTool-scratch/logs/accept-o-current-broken-snapshot.py
```

No tool installs or upgrades were needed (python3 + git only; pacman untouched).

## Bottom line for the L1

- Claim O's instrument is **not** mutant-complete on two points: the per-run timeout default (F1) and
  UNRESOLVED ordering (F2). Both survive all 9 legs and the tool's 63 selftest checks.
- The exit-code contract that F1/F2 sit next to **is** well covered: my "UNRESOLVED then exit 0"
  mutant dies at four independent points.
- Do not stamp O while `reports/round-66/accept-o.py` has the line-117 SyntaxError (F5); re-run
  mutants 1 and 3 against the integrated revision, and expect both to survive unless a pin is added.
- Cheapest closes: `"default 600" in h.stdout` inside the existing `OPTIONS` leg (F1), and a
  2-dynamic-unit `--static-only` instance asserting `unresolved == sorted(unresolved)` (F2, probe attached).
