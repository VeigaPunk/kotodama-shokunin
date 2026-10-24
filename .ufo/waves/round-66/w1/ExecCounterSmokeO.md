# ExecCounterSmokeO — ACCEPT-O-66 counter smoke (build seat, round 66 / hyaku 5)

Lane: `kotodama-shokunin`, base `94209e8f80969dbac48d56c5d0e2e623635b8616` (jj tip == main == base at
run time). Scope: run the frozen O counter at base, record every leg + exit code, probe `--help`, and
list defects/crashes/ambiguities with path:line + minimal fix. **No counter, tool, or registry bytes were
edited by this seat.** Full detail: `.ufo/waves/round-66/stage/execcountersmokeo.md`.

## 1. Exact commands and results

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 -B reports/round-66/accept-o.py --root .        # 6.46 s wall, EXIT=0
```

```
# counter sha256 (self): 681743e3850b8281fb4ae9ecaef7e10b595750ee79201ce96b6c9cc7ede9d409
# measured revision (lane main): 94209e8f80969dbac48d56c5d0e2e623635b8616
SELFTEST PASS exit=0 count=63/63
DIFF PASS diff_lines=428
OPTIONS PASS missing=[]
BOUND PASS exit=2 partial=True unresolved=True
STATIC PASS exit=2
MAXRUNS PASS exit=2
JOBS PASS j1=1 j4=1 eq=True
MUT PASS mutants=4 failing=[]
FIXTURES PASS lanes=2 wall=6.4s
ACCEPT-O-66: PASS
```

- 9/9 legs PASS, verdict line `ACCEPT-O-66: PASS`, exit **0**.
- Reproduces the frozen pre-data receipt `reports/round-66/telemetry/dry-run-o.txt` line-for-line except
  `wall=6.4s` vs `6.3s` (a measured timing echo, not asserted).
- Byte-identical counter self-sha to the receipt (`681743e3…`), so the receipt was produced by these bytes.

`python3 -B reports/round-66/accept-o.py --help` → **does not crash**, exit 0, prints
`usage: accept-o.py [-h] [--root ROOT]` + `--root`. `--bogus` → argparse error, exit 2 (correct).

Instrument hygiene: two full runs left no lane residue — `git status --porcelain` shows only the
pre-existing ` M tools/check-claim-separability.py` and untracked `reports/round-66/`,
`.ufo/waves/round-66/`. The counter writes only inside `tempfile.TemporaryDirectory` and reads
`.ufo/waves/round-66/stage/mut-o/`.

## 2. Defects (all recorded with path:line + minimal fix in the stage file)

| id | sev | what |
|---|---|---|
| D-O1 | MED | `accept-o.py:109-113`: `git rev-parse main` has no `-C root`/`cwd=root`; from `/tmp` with `--root <lane>` it prints `measured revision (lane main): unresolvable` and **still PASSes exit 0**. Revision line is the receipt's only provenance and is ungated. Fix: `["git","-C",root,"rev-parse","main"]` + a `REVISION` leg requiring resolvability (not `== BASE`, since the same counter runs post-integration). |
| D-O2 | MED | `accept-o.py:98-101` (uncaught `TimeoutExpired`, `timeout=200`), `:46-56`+`:67-84` (`RuntimeError` from `git()`), `:109` (`FileNotFoundError`); `main()` `:104-252` has no try/except. Measured: `env PATH=/var/empty /usr/bin/python3 -B reports/round-66/accept-o.py --root .` → traceback, **exit 1, no verdict line** — crash is indistinguishable from predicate FAIL by exit code. Fix: wrap fixture/MUT in try/except → `leg("FIXTURES", False, "crash: …")`, always print the verdict line, or use exit 3 for crash. |
| D-O3 | LOW | `:124-125` pin the literal `"63/63"`; adding a healthy 64th tool selftest flips the counter to FAIL, a stale `63/63` passes. Fix: regex `count=(\d+)/(\d+)`, equal groups, `>= 63`. |
| D-O4 | LOW | `:160-168` BOUND (and STATIC `:190-193`) never time the run or assert `skipped=`; a tool that skips unconditionally whenever `--budget` is present passes 3 of 4 bound legs (only MAXRUNS `:196-200` and JOBS `:202-210` force a real verdict). Fix: assert `elapsed < 5.0` (fixture sleeps 1.5 s under `--budget 0.5`) and `skipped=1` in BOUND stderr. |
| D-O5 | LOW | `:221` (`"skipped=0" in r.stderr or "skipped=" not in r.stderr`) and `:222` (`"UNRESOLVED" not in r.stdout`) are vacuously satisfied by a mutant that dies on import. No false kill today: all four mutants are genuine single-point byte-mutants of the live tool (verified by `diff -u`: mut1 `return EXIT_INPUT` ~:836, mut2 `if True` ~:737, mut3 both `self.skipped += 1` ~:700/:703, mut4 unresolved print loop ~:826). Fix: add `"Traceback (most recent call last)" not in r.stderr` + require a `SEPARABILITY:` stdout line. |
| D-O6 | INFO | `:41` pins `TOOL`, so the counter cannot be aimed at pre-upgrade bytes; `telemetry/controls-o.txt` substitutes a manual `--help` probe and infers FAIL for 8 unprobed legs. Fix: `--tool PATH` for `run_tool`, keep DIFF hard-wired. |
| D-O7 | INFO | `:125` cosmetic `and/or/if` detail chain (never affects the verdict). |

Neither MED finding breaks ACCEPT-O-66 as frozen at base; both are provenance/honesty holes that a
future pre-data receipt could inherit silently.

## 3. Risks
- **Frozen receipts:** any counter edit changes the self-sha and invalidates `telemetry/dry-run-o.txt` and
  `controls-o.txt`. If the L1 applies D-O1/D-O2, both receipts must be regenerated in the same lands
  commit; a stale receipt is a false-stamp class defect.
- **Provenance:** post-integration receipts are only trustworthy if the counter was invoked with cwd ==
  lane root (D-O1); the claim command `--root .` is correct, any harness variant is not.
- Semantics not checked by this seat: whether the tool's `--jobs` actually parallelizes (only verdict
  equality is asserted), and performance beyond fixture sizes (already `review_only` in claims.json).

## 5. Live re-check after the L1's APPLY decision (counter amended in flight)

The counter changed under this seat: sha256 `681743e3…` (what section 1 measured and what
`telemetry/dry-run-o.txt` records) → `f08ff6e8…`. **The amended bytes do not compile**
(`reports/round-66/accept-o.py:117` = `legs = []")"]")` → `SyntaxError: unmatched ']'`, exit 1,
measured twice). D-O1's substance is present (`:109` `-C root`, `:114-117` 40-hex revision gate);
D-O2 is still absent (no `try/except` anywhere). Lines 118-121 are a stale duplicate of the
pre-patch `mv`+header block.

Validated minimal patch (on a throwaway copy, `py_compile` OK, copy deleted): drop :117-121, keep
`legs = []` + `t_start`, print `ACCEPT-O-66: FAIL` before the gate's `return 2`, and
`REVISION PASS main=<sha>` on success. Measured with that patch: `--root .` from the lane root →
`REVISION PASS main=94209e8f…`, 9/9 legs PASS, exit 0; same from `/tmp` (cwd-dependence gone);
`--root /tmp` (non-repo) → `REVISION FAIL`, `ACCEPT-O-66: FAIL`, exit 2. Details:
`.ufo/waves/round-66/stage/execcountersmokeo.md` §6.

## 6. Blockers
None. No missing artifacts, no installs required (nothing installed; pacman untouched). Nothing was
committed; lane jj/Git state untouched. The only writes by this seat are its two reports and two
throwaway copies under `.ufo/waves/round-66/stage/`, both removed.

Report: .ufo/waves/round-66/w1/ExecCounterSmokeO.md
