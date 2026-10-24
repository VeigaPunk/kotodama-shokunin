# exec-counter-smoke O — ACCEPT-O-66 counter run, legs and defects

Seat: L1-kotodama-r66.ExecCounterSmokeO (leaf, build). Counter under test:
`reports/round-66/accept-o.py` (self sha256 `681743e3850b8281fb4ae9ecaef7e10b595750ee79201ce96b6c9cc7ede9d409`).
Predicate: ACCEPT-O-66. No counter or tool bytes were edited by this seat.

## 1. Measured run (lane root, as the claim's command specifies)

Command: `python3 -B reports/round-66/accept-o.py --root .` (cwd = repo root)
Wall: 6.46 s. **Exit code: 0.**

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

Every leg (9/9) prints PASS; verdict line `ACCEPT-O-66: PASS`; exit 0. Reproduces
`reports/round-66/telemetry/dry-run-o.txt` line-for-line except `wall=6.4s` vs `6.3s`
(a measured timing echo, not an asserted value).

## 2. `--help` behaviour

`python3 -B reports/round-66/accept-o.py --help` → **does not crash**, exit 0:

```
usage: accept-o.py [-h] [--root ROOT]
options:
  -h, --help   show this help message and exit
  --root ROOT
```

`--bogus` → argparse error, exit 2 (correct). No defect here. (The counter's own surface is
`--root` only; the option surface under test, `--jobs/--budget/--max-runs/--static-only`, is
probed on the *tool* by the OPTIONS leg and is listed correctly.)

## 3. Defects, crashes, ambiguities (path:line + minimal fix)

### D-O1 MED — "measured revision (lane main)" is cwd-dependent and ungated
`reports/round-66/accept-o.py:109-113`
`subprocess.run(["git", "rev-parse", "main"], ...)` has **no `-C root` / `cwd=root`**, and
stderr is swallowed; the value is then printed as `# measured revision (lane main)`.
Observed: `cd /tmp && python3 -B <lane>/reports/round-66/accept-o.py --root <lane>` prints
`# measured revision (lane main): unresolvable` and still ends `ACCEPT-O-66: PASS`, exit 0
(all 9 legs PASS). So the receipt's only provenance line can be blank/misleading while the
predicate passes; nothing in the counter fails when the revision cannot be resolved.
Minimal fix: `["git", "-C", root, "rev-parse", "main"]`, and add
`leg("REVISION", mv.returncode == 0 and bool(mv.stdout.strip()), ...)`.
Do **not** gate on `== BASE`: the same counter is meant to run post-integration, when the tip
legitimately differs from BASE. Resolvability is the honest bound.

### D-O2 MED — hard crash instead of a FAIL verdict; crash exit code collides with FAIL
`reports/round-66/accept-o.py:98-101` (`run_tool`, `timeout=200` → uncaught
`subprocess.TimeoutExpired`), `:46-56` (`git()` raises `RuntimeError`) called from
`make_lane` `:67-84`, and `:109` (`FileNotFoundError` when `git` is not on PATH).
`main()` has no try/except (`:104-252`). Observed:
`env PATH=/var/empty /usr/bin/python3 -B reports/round-66/accept-o.py --root .` →
traceback `FileNotFoundError: ... 'git'`, **exit 1, no `ACCEPT-O-66:` line**.
Exit 1 is also the predicate-FAIL code, so a consumer keying on exit status cannot tell a
counter crash from a genuine FAIL, and one keying on the verdict line gets nothing at all.
Minimal fix: wrap the fixture/MUT block in `try/except Exception as exc:
leg("FIXTURES", False, f"crash: {exc!r}")`, and always print the verdict line in a
`finally` (or use a distinct crash exit, e.g. 3).

### D-O3 LOW — SELFTEST pins the literal string "63/63" twice
`reports/round-66/accept-o.py:124` and the detail expression `:125` (mirrored in
`claims.json` claim O leg 1). Adding one assertion to the tool's selftest (a healthy change)
flips the counter to FAIL; conversely a tool that prints a stale `63/63` is accepted.
Minimal fix: `m = re.search(r"count=(\d+)/(\d+)", st.stdout)` and require
`m and m.group(1) == m.group(2) and int(m.group(1)) >= 63`; keep the claim leg string in sync.

### D-O4 LOW — BOUND/STATIC/MAXRUNS never assert that the budget is enforced, nor the skip count
`reports/round-66/accept-o.py:160-168` (BOUND) requires only exit 2 + `SEPARABILITY_PARTIAL`
+ `SEPARABILITY_UNRESOLVED` + absence of `SEPARABILITY_DEPENDENCY C-><base>`. It does not time
the subprocess (the fixture acceptance sleeps 1.5 s under `--budget 0.5`) and does not check
`skipped=` at all. A tool that unconditionally skips dynamic runs whenever `--budget` is
supplied passes BOUND, STATIC (`:190-193`) and MAXRUNS (`:196-200` is the only one that reads
`skipped=1`); only JOBS (`:202-210`) forces a real dynamic verdict, so a "skip-always under
budget" regression survives 3 of 4 bound legs.
Minimal fix: time the BOUND call and assert `elapsed < 5.0`, and require `skipped=1` (or
`skipped>=1`) in BOUND's stderr as STATIC/MAXRUNS already do.

### D-O5 LOW — MUT kill predicates are satisfiable by a mutant that merely crashes
`reports/round-66/accept-o.py:221` `"skipped=0" in r.stderr or "skipped=" not in r.stderr` and
`:222` `"UNRESOLVED" not in r.stdout` are both vacuously true for a mutant that dies on
import/syntax error (no `skipped=` text, empty stdout). Today all four mutants are genuine
single-point byte-mutants of the live tool — verified by `diff -u` against
`tools/check-claim-separability.py`: mut1 drops `if partial: return EXIT_INPUT` (~:836),
mut2 flips `if not repairs and not unevaluated:` → `if True:` (~:737), mut3 drops both
`self.skipped += 1` (~:700, :703), mut4 drops the unresolved print loop (~:826); none is a
stale replica. So no false kill in this wave; the hole opens for the next mutant added.
Minimal fix: add `"Traceback (most recent call last)" not in r.stderr` and require a
`SEPARABILITY:` verdict line in stdout to every `mut_expect` predicate.

### D-O6 INFO — the do-nothing control is not mechanized through the counter
`reports/round-66/accept-o.py:41` pins `TOOL = "tools/check-claim-separability.py"`, so the
counter cannot be aimed at the pre-upgrade tool bytes; `telemetry/controls-o.txt` therefore
substitutes a manual `--help` probe of `/tmp/sep-base.py` and asserts "every new leg is
anchored to the new surface" — that is an inference from 1 of 9 legs, not a measured counter
FAIL. (On base bytes DIFF would also fail: the tool diff is empty.) Minimal fix: add
`--tool PATH` defaulting to `TOOL`, use it for every `run_tool` call but keep DIFF hard-wired
to the constant path so `--tool` cannot weaken the landed-bytes leg; then record the control
as `accept-o.py --root . --tool /tmp/sep-base.py`.

### D-O7 INFO — cosmetic / receipts
`:125` builds the SELFTEST detail with an `and/or/if` chain whose value differs from the
asserted fragment on failure; it never affects the verdict. The counter writes only inside
`tempfile.TemporaryDirectory` and reads `MUT_DIR`, so it leaves no lane residue (verified:
`git status --porcelain` after two runs shows only the pre-existing
` M tools/check-claim-separability.py` plus untracked `reports/round-66/` and
`.ufo/waves/round-66/`). No installs were needed (no pacman/uv/npx used).

## 4. Risk note for the L1 before any counter edit
Any fix to D-O1..D-O6 changes the counter's self sha256 and therefore invalidates the frozen
pre-data receipt `telemetry/dry-run-o.txt` and `controls-o.txt`. If the L1 applies a fix, it
must regenerate both receipts in the same lands commit; leaving them stale is a false-stamp
class defect (receipt sha not matching the counter that produced it).

## 5. Verdict
Counter is operable at base: 9/9 legs PASS, exit 0, 6.5 s wall, `--help` exits 0.
Findings are hardening items (2 MED, 3 LOW, 2 INFO), not failures of ACCEPT-O-66 as frozen.

## 6. Live re-check after the L1's APPLY decision (counter amended in place, in flight)

The counter bytes changed under this seat after section 1 was written. Section 1 describes
sha256 `681743e3…` (still what `telemetry/dry-run-o.txt` records). At re-check time the file was
sha256 `f08ff6e8fb22e3399519d4d87815b9ce9badc16bb9682ed5afcfb787da276199` and **does not
compile**:

```
$ python3 -B reports/round-66/accept-o.py --root .
  File ".../reports/round-66/accept-o.py", line 117
    legs = []")"]")
                ^
SyntaxError: unmatched ']'
EXIT=1
```

### 6a. D-O1 applied, D-O2 not yet, plus a botched paste (current defect)

`reports/round-66/accept-o.py:109-122` currently reads:

```
    mv = subprocess.run(["git", "-C", root, "rev-parse", "main"], stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    mv_rev = mv.stdout.decode().strip()
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# measured revision (lane main): {mv_rev or 'unresolvable'}")
    if not re.fullmatch(r"[0-9a-f]{40}", mv_rev):
        print("REVISION FAIL lane main unresolvable; a counter run must name a revision")
        return 2                                   # :116 — no `ACCEPT-O-66:` verdict line
    legs = []")"]")                                # :117 — SyntaxError, corrupted paste
    mv = subprocess.run(["git", "rev-parse", "main"], ...)   # :118-119 — stale duplicate
    print(f"# counter sha256 (self): {self_sha}")            # :120 — stale duplicate
    print(f"# measured revision ...: {mv.stdout...}")        # :121 — stale duplicate
    legs = []                                      # :122
```

Good: `-C root` and the 40-hex revision gate (D-O1) are in. Remaining defects:
1. **:117 SyntaxError** — the file cannot run at all (measured above, exit 1). Minimal fix:
   replace `legs = []")"]")` with `legs = []`.
2. **:118-121 stale duplicate block** — leftover of the pre-patch code (re-runs `git rev-parse`
   against the invocation cwd and re-prints the header). Minimal fix: delete lines 118-121.
3. **:114-117 gate path prints no verdict line** — a consumer keyed on `ACCEPT-O-66:` sees
   nothing while exit 2 collides with argparse's usage-error code. Minimal fix: add
   `print("ACCEPT-O-66: FAIL")` before `return 2`, and on success print
   `REVISION PASS main=<sha>` so happy-path receipts carry the provenance value.
4. **D-O2 still absent** — `grep -n "try:\|except"` finds none; a missing `git`, a tool
   timeout (`:98-101`) or a `git()` failure (`:46-56`) still yields a bare traceback.

### 6b. Validated minimal patch (measured on a throwaway copy, since deleted)

Applied to a copy of the broken bytes under
`.ufo/waves/round-66/stage/accept-o-fixcheck.py` (sha256 `bc5efe865038b20719996ec553853b76ab5caaf7325e5ac92314bb21606b8ef3`),
`python3 -m py_compile` OK, and:

- `--root .` from the lane root: `REVISION PASS main=94209e8f…`, then SELFTEST…FIXTURES all PASS,
  `ACCEPT-O-66: PASS`, exit 0, wall 13.2 s for both invocations together (6.6 s each).
- `--root <lane>` from `/tmp`: identical PASS output — the `-C root` fix removes the
  cwd-dependence measured in D-O1.
- `--root /tmp` (a non-repo, so `main` is unresolvable): header, `REVISION FAIL …`,
  `ACCEPT-O-66: FAIL`, exit 2 — the gate actually fires and is visible to verdict-line consumers.

Recommendation for the L1's lands commit: use the 6b shape (drop :117-121, add the FAIL/PASS
prints), and add D-O2's top-level wrapper in the same edit. claims.json's O `legs` list still
enumerates 9 legs; `REVISION PASS` is an informational precheck line, not a counted leg, so no
claims edit is needed for it (note it in the lesson if you want the receipt self-describing).
