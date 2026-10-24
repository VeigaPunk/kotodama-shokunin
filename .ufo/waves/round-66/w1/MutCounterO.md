# MutCounterO — mutation probe of `reports/round-66/accept-o.py` (ACCEPT-O-66)

Seat: mutation-tester, wave w1, round 66 (hyaku run 5). Lane base `94209e8f8096…b8616`.
Target: `reports/round-66/accept-o.py`, revision sha256 `681743e3850b8281fb4ae9ecaef7e10b595750ee79201ce96b6c9cc7ede9d409` — the revision whose self-sha is printed in the frozen pre-data receipt `reports/round-66/telemetry/dry-run-o.txt` (`# counter sha256 (self): 681743e3…`). Mutant copies live only under `.ufo/waves/round-66/stage/mut-o-counter/`; the lane file was never edited by this seat (see *Integrity* and *Restoration*).

## Detector (identical on pristine and mutant bytes)

`python3 -B <counter-copy> --root <controlled root>` — the counter's own full leg suite (SELFTEST, DIFF, OPTIONS, BOUND, STATIC, MAXRUNS, JOBS, MUT, FIXTURES), same argv, same env, full stdout/stderr/rc captured. Only `--root` differs from the claim's own command form; the counter resolves `tool_abs`, `mut_dir` and the DIFF commit from it. The committed file is never executed from a mutable path, and no counter copy was ever written outside `stage/mut-o-counter/`.

Controlled roots (all under `.ufo/waves/round-66/stage/mut-o-counter/`):

- `root/` — composite world (all three controls violated at once): `tools/check-claim-separability.py` = frozen tool + two patches (`if "--jobs" in sys.argv: time.sleep(95)` after `args = ap.parse_args(argv)`, so the harness wall crosses 180 s; success print `% (passed, total)` → `% (passed, total + 1)`, so `--selftest` prints `63/64 checks passed` and still exits 0), sha256 `229390d7243c…e7ca`; `stage/mut-o/` = four byte-identical copies of that same tool under the four pinned mutant names (four *survivors*). `.git` is a `gitdir: <lane>/.git` file so the DIFF leg resolves BASE against the scratch worktree — verified `rev-parse --show-toplevel` = root, DIFF `diff_lines=435`, and the lane index untouched (`.git/index` sha256 `b5b742f8…cb02` identical before/after, mtime unchanged).
- `roots/m1/`, `roots/m2/`, `roots/m3/` — single-violation worlds, each carrying the real stage mutants (so MUT stays PASS): m1 tool = the real tool (`5c728e96…f4d98`, survivors only in `stage/mut-o`); m2 tool = real tool + sleep patch (`16be2890…7714b`); m3 tool = real tool + count patch (`8e6f863d…27de0`).
- Production root: the lane itself, all four counter variants, run consecutively (legs byte-identical; wall 6.5 s).

Runs: pristine and each mutant were launched concurrently (4-way; 6-way for the single-violation worlds) so the detector is byte-for-byte the same invocation in every cell. Receipts: `runs/{pristine,mut1_always_true,mut2_bound_9999,mut3_selftest_relaxed}.{out,err,rc,ms}`, `runs/prod-*.out`, `runs/world-*.out`; every stderr is 0 bytes.

Baseline direction: on the composite world the pristine counter correctly prints `ACCEPT-O-66: FAIL` (SELFTEST, MUT, FIXTURES). On production bytes it prints `ACCEPT-O-66: PASS` with `wall=6.5s` (frozen receipt: `6.3s`). So the violations are deliberate adversarial controls, not a claim that the instrument is broken on today's data — and a mutant that *stops seeing* a control is a coverage loss, not a repair.

## Mutant table

| # | byte change (`diff -u` vs pristine copy) | sha256 | leg relaxed | expected detector | pristine output | mutant output | verdict |
|---|---|---|---|---|---|---|---|
| M1 | 4 lines: `lambda r: <pin>` → `lambda r: True` (lines 219–222) | `ebaf1ffd…6d7c` | MUT | MUT leg must report each pinned mutant that survives its pin | `MUT FAIL mutants=4 failing=['mut1_no_partial_exit.py:survives', 'mut2_unresolved_to_base.py:survives', 'mut3_silent_skip.py:survives', 'mut4_suppress_unresolved.py:survives']` | `MUT PASS mutants=4 failing=[]` | **SURVIVED** |
| M2 | one line: `(time.monotonic() - t_start) < 180` → `< 9999` (line 247) | `add14cc6…0dadb6` | FIXTURES | FIXTURES must fail when the harness wall exceeds its budget | `FIXTURES FAIL lanes=2 wall=196.5s` | `FIXTURES PASS lanes=2 wall=196.6s` | **SURVIVED** |
| M3 | one line: `st.returncode == 0 and "63/63" in st.stdout` → `st.returncode == 0` (line 121) | `d893132d…5ae3f` | SELFTEST | SELFTEST must pin the tool's reported check count, not just its exit | `SELFTEST FAIL exit=0 selftest: 63/64 checks passed …` | `SELFTEST PASS exit=0` (count still `63/64`) | **SURVIVED** |

Isolation (composite world, one control violated per line shared across runs): M1 flips only MUT; M2 flips only FIXTURES; M3 flips only SELFTEST; BOUND/STATIC/MAXRUNS/JOBS/DIFF/OPTIONS stay `PASS` in all four runs and the stderr of all four is empty. Each mutant is therefore pinned to one leg, and each flip is caused by its own mutation.

Verdict meaning: **SURVIVED** = the weakened counter still prints `PASS` for the leg whose control is violated, and nothing in the round's instrument set catches that. In each single-violation world the effect reaches the claim verdict itself:

| world (only this control violated) | pristine | weakened mutant |
|---|---|---|
| m1: four pinned-name survivors in `stage/mut-o` | `ACCEPT-O-66: FAIL` (only `MUT FAIL`) | M1 → `ACCEPT-O-66: PASS` (`MUT PASS`), rc 0 |
| m2: tool sleeps 95 s per `--jobs` run (wall 196.5 s) | `ACCEPT-O-66: FAIL` (only `FIXTURES FAIL`) | M2 → `ACCEPT-O-66: PASS` (`FIXTURES PASS wall=196.5s`), rc 0 |
| m3: tool selftest prints `63/64`, exits 0 | `ACCEPT-O-66: FAIL` (only `SELFTEST FAIL`) | M3 → `ACCEPT-O-66: PASS` (`SELFTEST PASS exit=0`), rc 0 |

On production data all three mutants are **behaviorally silent**: `prod-pristine`, `prod-mut1`, `prod-mut2`, `prod-mut3` print byte-identical leg lines (`SELFTEST PASS … 63/63`, `MUT PASS mutants=4 failing=[]`, `FIXTURES PASS lanes=2 wall=6.5s`, `ACCEPT-O-66: PASS`, rc 0). The three relaxations are undetectable from the frozen lane data alone — only a controlled root exposes them.

## Kill descriptions (the control that should trip each leg, and what the round lacks)

- **M1 — MUT.** Kill control: a stage directory whose pinned-name entries are known survivors (I used four no-op copies of one tool; their expectations all fail). The leg's *only* oracle is the mutant bytes it receives: it never checks that a mutant differs from the tool, nor that the mutant's pinned output is the negative of the tool's. A copy/paste or rebuild that leaves `stage/mut-o/*.py` byte-identical to the tool turns the leg into a rubber stamp — and the counter cannot notice. Kill would need an independent expectation derivation (e.g. a counter `--selftest` that plants one survivor and asserts `MUT FAIL`), or per-mutant sha pins.
- **M2 — FIXTURES.** Kill control: a lane whose aggregate wall exceeds 180 s (two 95 s `--jobs` runs → 196.5 s). The bound is otherwise unreachable from real data (production wall 6.5 s, 28× under). Note the reachable window is only 180–200 s, because `run_tool` sets `timeout=200` per run and `subprocess.TimeoutExpired` is uncaught: a single run that actually approached the bound would raise a traceback instead of a leg line, so no verdict is printed at all. Raising the bound to 9999 removes the only wall guard in the instrument.
- **M3 — SELFTEST.** Kill control: a tool whose `--selftest` exits 0 while reporting `63/64` (one control failing but not fatal). The leg trusts the tool's *self-report*: it only greps for `63/63` in stdout and never inspects stderr for `FAIL`/`FAILED` lines, so even the pristine pin is satisfied by any tool that prints the literal string. Dropping the count check leaves only `returncode == 0`, which the tool sets independently of the count.

## Findings

1. **[MED] All three relaxations survive the frozen instrument set.** `accept-o.py` has no negative control for its own legs; `accept-c.py`/`accept-ca.py` do not read `accept-o.py` or its stage dir; the separability check verifies lands, not the counter's checking power. A shortened or weakened `accept-o.py` can still print `ACCEPT-O-66: PASS` — and, on a world that violates exactly the relaxed control, does so with exit 0 (table above). This is a coverage finding about the predicate, not a request to change the claim.
2. **[MED] `FIXTURES` bound unreachable except in a 20 s window** (180 s bound vs `run_tool`'s `timeout=200`, `TimeoutExpired` uncaught). Operability improvement for a future revision: catch `TimeoutExpired` into a `FAIL` leg, and set the per-run timeout below the wall bound.
3. **[LOW] `SELFTEST` is self-reported.** The counter never cross-checks the tool's count against stderr or against a known-failing invocation; a tool that prints `63/63` while failing a check passes today's leg too.
4. **[HIGH — integrity, not caused by this probe] The lane counter changed under the probe.** Observed hashes of `reports/round-66/accept-o.py`: `681743e3…` (frozen receipt / my baseline) → `f08ff6e8…` (mtime 08:35:36, 11766 B, **SyntaxError**: line 117 `legs = []")"]")`, verified with `py_compile`) → `89033f8d…` (mtime 08:37:49, 11479 B, compiles) → `b366c25b…` (mtime 08:43, still being rewritten as this report was written). Another seat wrote the path mid-wave; this seat only ever read it. The live `89033f8d…` revision still contains all three weak points, at lines 129 (`"63/63" in st.stdout`), 224–227 (the four pinned lambdas) and 252 (`< 180`), and adds a revision guard (`re.fullmatch(r"[0-9a-f]{40}", mv_rev)` → `return 2` when lane `main` is unresolvable). ACCEPT-O-66 must name one revision: the legs measured here are those of `681743e3…`; the three mutations apply textually unchanged to `89033f8d…`, but the revision guard is unexercised by both.

## Files and restoration evidence

- Pristine copy `stage/mut-o-counter/pristine/accept-o.py` sha256 `681743e3…9d409` = the receipt's self-sha = the file as first read.
- Mutants: `mut1_always_true` `ebaf1ffd…6d7c`, `mut2_bound_9999` `add14cc6…0dadb6`, `mut3_selftest_relaxed` `d893132d…5ae3f`; all four script copies compile (`py_compile`), full diffs are one line / four lines as tabulated.
- Bad-world assets: `root/tools/check-claim-separability.py` `229390d7…e7ca` (+ four identical `stage/mut-o` copies), `roots/m1|m2|m3` tools `5c728e96…f4d98`, `16be2890…7714b`, `8e6f863d…27de0`; each root's `.git` is a one-line `gitdir:` pointer, no worktree or ref created.
- Lane state untouched: `git status --porcelain` is ` M tools/check-claim-separability.py`, `?? .ufo/waves/round-66/`, `?? reports/round-66/` before and after the probe; `.git/index` sha256 `b5b742f8…cb02` and mtime `08:32:51` unchanged (checked around the only `git diff` path used); no commit, no jj operation, no ref or index write. The `reports/round-66/accept-o.py` writes in the timeline above are another seat's, not this seat's; this probe never opened that path for writing.
- Tooling: none installed or upgraded (Python 3.14.8, git 2.56.0, stdlib only). All writes are under `.ufo/waves/round-66/stage/mut-o-counter/` and this report.

Report: .ufo/waves/round-66/w1/MutCounterO.md
