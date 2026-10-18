# Round-19 battery integration — regression and routing (R29-O01..O06)

- **Seat:** R29-O01..O06 (battery integration). **Date:** 2026-10-18. Lane root, `TMPDIR=$PWD/.scratch`
  unless stated; the frozen-replay leg needs `TMPDIR` outside the repo by the tool's own design and
  ran under `/tmp/r19-o01-outside`.
- **Revision binding:** the readings in §1–§2 were taken at 2026-10-18T12:37Z against the working tree
  where `tools/check-gate-battery.py` is
  `sha256 cd8c0ec291b6b986744ff132991abff717cbc085a86f095378189e15d6df13e5`; the selftest-leg readings
  in §1 are unchanged by the 11:38–12:35Z intermediate revision. A green at this revision authorises
  no later bytes.

## 1. The green suite (own readings, not quoted from another seat)

| Command | Exit | Summary line |
|---|---|---|
| `python3 tools/check-gate-battery.py` | 0 | `pass 7`, `coverage 9/9`, `preserved true` (30 files), `findings []` |
| `python3 tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 35/35 controls behaved as expected` |
| `python3 tools/check-craft-exercise.py --selftest` | 0 | `CLI-SELFTEST OK 18/18 cases passed` |
| `python3 tools/check-evidence-coupling.py --selftest` | 0 | `"selftest_passed": true` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | `selftest: 12/12 checks passed` |
| `python3 tools/assemble-d2-typed.py --selftest` | 0 | `selftest: 11/11 checks passed` |
| `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed` |
| `TMPDIR=/tmp/r19-o01-outside python3 tools/replay-frozen.py --selftest` | 0 | `selftest: 79/79 checks passed` |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | 0 | `selftest: 39/39 checks passed` |
| `python3 tools/gates/costume-era-consistency-gate.py --selftest` | 0 | `self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs` |
| `python3 tools/gates/handoff-packet-check.py --selftest` | 0 | `selftest: OK — fixture findings 11 across 9 ids` |
| `python3 tools/gates/lexicon-coverage-audit.py --selftest` | 0 | `selftest: 14/14 checks passed` |
| `python3 tools/gates/myth-consistency-gate.py --selftest` | 0 | `selftest: OK — fixture exit 1; planted IDs present: MC-P01…` |
| `python3 tools/gates/naming-collision-gate.py --selftest` | 0 | `selftest: OK — fixture findings 12 across 11 ids` |
| `python3 tools/gates/phonology-sanity-gate.py --selftest` | 0 | `selftest: fixture exit 1; 15/15 planted finding IDs present; 29 control cases passed` |
| `python3 tools/gates/provenance-audit.py --selftest` | 0 | `SELFTEST OK: 7 fixture file(s)…` |

The seven structural legs above are exactly the battery's duty-1 legs run by hand, so the battery's
`pass` count and these lines are the same measurement made twice.

## 2. The two counters, and why they are read separately

```text
$ python3 tools/check-gate-battery.py
exit 0   pass 7   fail 0   unevaluable 0   coverage 9/9   gates_registered 9   preserved true
```

`pass 7` is the selftest surface (the seven structural gates, executed in the mirror). `coverage 9/9`
is the baseline surface (nine registered gates, each with a committed `pinned` baseline). Reading the
first as the second is the pre-state's failure mode; the report prints both, plus the denominator, so
that misreading is no longer available. Neither counter is derived from the other, and a reader who
wants the D4 adapters' runtime behavior has to go to the round-18 frozen rows or the adapters' own
`--selftest` — this battery does not execute them.

**End-to-end check against the round's own instrument** (2026-10-18T12:41Z, transcript
`.scratch/r19-o01/runner-predicates.txt`): this seat read the shipped battery's report and evaluated
`run-validation.py`'s claim-O O1/O2 predicates against it — `pass ∈ (7, 9)`, `pass == len(gate_ids)`,
`fail`/`unevaluable` 0, `coverage == "9/9"`, `gates_registered == 9`, `gates_uncovered` empty,
`baseline_exit == 0`, both D4 gates covered *and* in `baseline_gates`, the battery `--selftest` green
(`SELFTEST OK 35/35`), and at least one D4 gate with a green live `--selftest` (typed-labels 0;
assembly 2, which no predicate requires). Result: `none - every runner O1/O2 predicate satisfied`. The
script is `.scratch/r19-o01/runner-predicates.py`; it does not invoke the runner, and it is a
predicate replay, not the runner's own verdict.

## 3. The withdrawn 9-leg variant and what it measured

Recorded here because it is the reason the shipped design registers the D4 family for coverage rather
than executing it (`design.md` §3), and because it is the only claim-O failure the round's own receipt
recorded.

**Reading** (2026-10-18T11:40:19Z–11:59:20Z, twenty poll ticks, revision `83d9e3e5…`):

```text
$ python3 tools/gates/d4-assembly-check-gate.py --selftest
assembly error: [Errno 2] No such file or directory: '--selftest'      # exit 2
$ sha256sum tools/gates/d4-assembly-check-gate.py
df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a
$ python3 tools/check-gate-battery.py
exit 2   pass 8   fail 0   unevaluable 1   coverage 9/9
```

The adapter's `main` takes `argv[1]` as the input path unconditionally, so `--selftest` is read as a
filename; the same invocation for `d4-typed-labels-check-gate.py` exits 0 (`39/39`) only because that
adapter forwards its argv to `tools/d2-typed-labels.py`, which carries the control matrix.

**Why it was not fixed from this seat.** (a) The brief forbids changing gate behavior. (b) A gate edit
invalidates `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json`, whose `gate_sha256`
is the digest above — an edit without a re-pin turns `pinned` into `gate_revised` and adds a red on the
coverage duty, i.e. the fix would make the round worse before better. (c) That baseline is another
seat's file (one writer per shared file), and `run-validation.py` §O4 would require a before/after
digest ledger entry for the change.

**Why the variant was withdrawn rather than left in place.** The round's counting command defines
claim O on the coverage surface: `reports/round-19/run-validation.py` (`sha256 ffee0643…`, rewritten
by the runner owner at 12:33Z) reads "the battery's duty-2 baseline coverage reads 9/9: seven
structural gates plus the two D4 adapters, with the battery's own `--selftest` controls green", and
its O1 check accepts `pass` of 7 or 9 while rejecting an incoherent 8
(`the battery executed 9 gates but passed 8`). The 12:33Z receipt
(`reports/round-19/validation.json`) records exactly that rejection, and nothing else on claim O:

```text
"claim O: the battery default run exited 2 (expected 0)"
"claim O: the battery default run passes 8 gate selftests, neither 7 (structural) nor 9 (all)"
"claim O: the battery executed 9 gates but passed 8"
"claim O: the battery default run reports unevaluable=1"
```

with `changed_gates: []`, `gate_change_ledger: {}` and `d4_baselines.problems: []` — the D4 baselines,
their pins and the nine gate surfaces were already green, and the 8-pass battery state was the sole
claim-O blocker. The shipped revision removes that blocker without touching a gate.

**Follow-up for a later round (not this one).** If the lane wants the adapters *executed* rather than
*covered*, the two moves are: add a `--selftest` mode to `tools/gates/d4-assembly-check-gate.py` that
runs its own control matrix (a positive byte-identical build, a one-byte negative, a missing-input
could-not-evaluate, a missing-assembler could-not-evaluate, a usage case, determinism, and a
no-side-effect check), and freeze a **new** baseline row pinning the new `gate_sha256` — never an
in-place edit of `r19-pre` — with the before/after digests recorded per §O4. Then the battery can run
nine legs coherently, and `pass` and `coverage` would both read nine.

## 4. Adjacent observation, outside this seat's surface

`python3 tools/assemble-d4-typed.py --selftest` → **exit 1** (`selftest: 4/11 checks passed` per the
R29-O13/O14 regression seat's capture, `.scratch/r19-regression/results.json`, 08:38 local). This seat
changed nothing in that tool and does not diagnose it; it is recorded because the claim-O text names
"all typed/assembly selftests green" and this leg is not green at this revision. Reported, not
absorbed.

## 5. Regression discipline applied here

- The seven structural legs run exactly as before (mirror, `--selftest`, same argv shape, same cwd,
  same classifier); their green is unchanged, and the mirror copy check still covers only the seven
  scripts + fixtures.
- The D4 registration is additive: no structural gate was dropped from any surface, and the
  preservation snapshot only *grew* (28 → 30 files, the nine registered gate scripts + fixtures).
- No frozen receipt, baseline, fixture or filed round-8..18 byte was edited by this seat
  (`git status --porcelain` shows only ` M tools/check-gate-battery.py` plus this round's new files).
- The battery is fail-closed on a live-tree edit during its own run; in a 64-worker wave that means a
  re-run may read `GATE-BYTES-CHANGED`. Re-run rather than quoting a stale line.
- `reports/round-19/validation.json` (12:33Z) still carries the withdrawn variant's readings; it is
  the runner owner's file and needs their re-run to record the shipped revision.
