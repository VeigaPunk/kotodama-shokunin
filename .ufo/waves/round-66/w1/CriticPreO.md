# CriticPreO — pre-data attack on claim O (accept-o.py vs tools/check-claim-separability.py)

Scope: reports/round-66/accept-o.py + tools/check-claim-separability.py, lane
`kotodama-shokunin`. Instrument reviewed live at three successive hashes
(`681743e3…` → `f08ff6e8…` → `89033f8d…`); findings below are against the
latest sealed-looking revision `89033f8d`, verified by running it end-to-end
(`ACCEPT-O-66: PASS`, wall 6.4 s). Receipt `telemetry/dry-run-o.txt` records
self-sha `681743e3` — honest at capture time, now stale vs the live counter.

## (1) Is the FIXTURES 180 s bound reachable cold? — YES, with ~28× headroom

Evidence: two end-to-end runs of the counter on this box (load ~4, 32 cores):
`wall=6.3s` and `wall=6.4s`; the receipt reports 6.3 s. The 180 s window
(`t_start` before SELFTEST) covers the tool's own `--selftest` (~4.3 s measured,
which itself builds ~30 temp git lanes), 2 fixture `make_lane` builds (each
init + base commit + 2 detached-checkout/commit cycles, ~40 git invocations
total), and 9 tool subprocesses plus 4 mutant subprocesses, one of which
sleeps 1.5 s. Even a 10× cold-cache penalty (fresh interpreter imports, cold
page cache for git binaries) lands under 70 s. Reachable.

Residual risks on the bound itself:

- `run_tool(timeout=200)` exceeds the 180 s FIXTURES window. A single hung
  subprocess raises `TimeoutExpired` uncaught — the counter dies with no
  `ACCEPT-O-66` line. Fail-closed, but the judge gets a crash, not a verdict;
  leg-level diagnostics are lost. Smallest fix: `timeout=120` or wrap each
  leg in try/except that records FAIL.
- Docstring (line 20) still says "built 3 temp git lanes"; the code builds
  exactly 2 (`f1`, `f2`) and `fixtures_built >= 2` is really `== 2`. Cosmetic
  stale claim; a reader checking the instrument against its own doc will
  flag it.

## (2) Does BOUND's 'no `<base>`' check survive a mutant naming UNRESOLVED + exit 2? — PARTIALLY; demonstrated bypass

BOUND asserts: exit 2 + `SEPARABILITY_PARTIAL` + `SEPARABILITY_UNRESOLVED` +
absence of the literal string `SEPARABILITY_DEPENDENCY C-><base>`. That pins
the exact `<base>` fabrication (mut2, verified on disk: `if True:` forces the
`<base>` branch) but nothing else.

**Counterexample, run live.** I built a mutant that prints
`SEPARABILITY_DEPENDENCY C->S via acceptance fabricated` on a skipped repair
run — a run that never executed — and ran it against a real fixture lane
with `--max-runs 1`:

```
SEPARABILITY_UNRESOLVED C->S via acceptance [...]: repair attempt skipped
SEPARABILITY_DEPENDENCY C->S via acceptance fabricated
SEPARABILITY: 0 findings
SEPARABILITY_PARTIAL 1 run(s) skipped
SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=1 skipped=1
EXIT=2
```

Every BOUND/MAXRUNS assertion passes: exit 2, PARTIAL, UNRESOLVED, `skipped=1`,
and no literal `C-><base>` — while the tool asserts a dependency whose repair
run never ran. JOBS does not catch it either: the leg compares `findings1 ==
findings4` across `--jobs 1/4`, pinning **consistency, not content** — a
deterministically fabricated line (or a direction-reversal mutant) is
identical under both job counts. STATIC asserts no DEPENDENCY-absence at all.
No leg anywhere pins the expected finding `SEPARABILITY_DEPENDENCY C->S` on
the unbounded run, so a mutant emitting `S->C` or `C->bogus` survives every
dynamic leg; MUT only runs the 4 pinned mutants. Also fragile-by-literal:
`C-> <base>` or any non-exact `<base>` spelling evades the substring check.

By the frozen predicate's letter ("never fabricated `<base>`") the instrument
is sound; by the claim's text ("honest partial verdicts") a fabricated
non-`<base>` verdict is the same dishonesty class. Impacted axis: operability.

**Smallest safe correction:** in BOUND, STATIC and MAXRUNS assert
`not any(l.startswith("SEPARABILITY_DEPENDENCY") for l in out.splitlines())`
(skipped runs must produce zero findings — the honest state), and pin JOBS's
`findings1` to the exact expected `C->S` line. Stronger still: run each
mutant's own `--selftest` and require failure — the selftest already asserts
finding content.

## (3) Is `63/63` a stable pin? — No: magic-count brittleness, but fail-closed

`selftest()` prints `selftest: 63/63 checks passed …` where `total =
len(results)` — the count is emergent (≈46 `scenario`/`verdict` calls plus the
`raw`/`malformed` block; the round-66 "bound:" controls added 8+). The leg
requires `rc == 0 and "63/63" in st.stdout`. Properties:

- **Fail-closed, not gameable upward**: `selftest()` returns `False` on any
  failed check (verified in source), so a mutant can't pass by printing
  `63/63` while a check fails — `rc` is already pinned. The literal adds only
  a count freeze.
- **Brittle to legitimate growth**: any new selftest check (a new bound flag,
  a new malformed case) changes `63/63` → SELFTEST fails spuriously and the
  counter plus its receipt must be re-cut for a non-regression. That is a
  maintenance hazard, not a soundness hole — call it a tradeoff the frozen
  predicate can accept, but it should be a recorded decision.
- Minor: `"63/63" in st.stdout` is a substring check (`163/163` contains it);
  irrelevant today since the count is real.

**Smallest safe correction:** pin `rc == 0` plus
`re.search(r"(\d+)/\1 checks passed", st.stdout)` — keeps the all-passed
guarantee (rc already enforces it) while surviving legitimate count changes;
or pin `int(m.group(1)) >= 63` to forbid silent removal while allowing growth.

## Additional findings (in-scope attack surface)

- **Counter churn under review**: `accept-o.py` changed hash 3× in ~7 min
  during this seat's run; the middle revision (`f08ff6e8`) had a live
  `SyntaxError` at line 117 (`legs = []")"]")` — a spliced REVISION leg —
  confirmed via `ast.parse`. It was repaired by `89033f8d`. Process finding:
  the instrument mutated while seats evaluate it; `dry-run-o.txt`'s
  self-sha `681743e3` no longer names the current bytes, so every receipt
  must be re-captured after the counter actually freezes. The self-hash
  mechanism itself is the right defense — it worked.
- **REVISION leg (new)**: asserts `git rev-parse main` resolves to a 40-hex —
  i.e., that the run can *name* a revision. Adequate for receipt provenance,
  but it does not relate `main` to `BASE` (any resolvable main passes). Fine
  as provenance, but do not read it as "the measured lane is the round lane".
- **`SEPARABILITY: 0 findings` coherence**: no leg checks that a printed
  DEPENDENCY line cannot coexist with a `0 findings` summary — my fabricated
  mutant produced exactly that incoherent pair. Same fix as (2).
- **mut1 pin `returncode != 2`**: accepts *any* non-2 exit (0 or 1) while
  PARTIAL prints. Correct for the pinned defect ("partial must exit 2"), but
  note a mutant exiting 1 on partial is still dishonest — it just happens to
  be counted "killed" anyway.
- **JOBS pins verdict-equality, not speed**: `--jobs 4` is asserted equal, not
  faster; a serial-ignoring-jobs mutant passes. Claim O only requires the
  option to exist and not corrupt the verdict — consistent with the frozen
  predicate; noted so nobody upgrades the claim retroactively.

## Verdict on the instrument

Acceptable against the frozen ACCEPT-O-66 predicate as written, with one
demonstrated residual hole (non-`<base>` fabrication on skipped runs) that a
3-line tightening fixes, one brittleness tradeoff (`63/63` literal) that
should be a conscious freeze decision, and a process dependency (receipt
staleness) since the counter was still churning during review.

Tools installed/updated: none (used system python3/git only).

Report: .ufo/waves/round-66/w1/CriticPreO.md
