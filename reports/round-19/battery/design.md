# Round-19 battery integration — design (R29-O01..O06, battery integration)

- **Seat:** R29-O01..O06, battery-integration shard. **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **Date:** 2026-10-18 (local clock UTC-03:00; every command below is stamped UTC).
- **Claim:** `reports/round-19/claims.json` claim O, after-state: "Battery default run covers the D4
  gates (7 structural + 2 D4 = 9/9) with selftest controls; the D4 family carries committed
  expected.json baselines under the standard layout; battery + craft + all typed/assembly selftests
  green; no gate behavior changes without documented reason."
- **Counting command:** `python3 reports/round-19/run-validation.py` (runner-owner surface; not
  invoked from this seat).
- **Write scope:** `tools/check-gate-battery.py`, `reports/round-19/battery/*`. No gate script, no
  baseline, no filed round-8..18 byte touched. No git mutation.
- **Baseline binding:** declared `baseline_revision e5718945a1ab0a0c3db955338d2cae77d68fd348`;
  declare commit `169c616613899f7ba86b8fb58ed808bdfd4b5ccd`. Every "before" reading below is taken
  from `git show e571894:…`, never from memory.

## 1. What the pre-state actually was (measured, not asserted)

Two independent readings of the round-18 tool, both taken 2026-10-18T11:40Z:

| Reading | Command | Observed |
|---|---|---|
| pre-state source digest | `git show e571894:tools/check-gate-battery.py \| sha256sum` | `7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574` — the digest the round-18 lesson filed at `corpus/lessons/round-18.md:58` |
| pre-state source names no D4 gate | `git show e571894:tools/check-gate-battery.py \| grep -c 'd4-'` | `0` |

The pre-state tool therefore had two blind spots, and they fail in opposite directions:

1. **Silent** — over a round-18-shaped root set (the standard root with the two D4 baseline
   directories removed, plus `tools/gates/frozen/` and `reports/round-9/baselines/`): exit **0**,
   `pass 7`, seven gate ids, `baselines_found 15`, `pinned 15`, `gates_uncovered []`. The battery was
   green while the D4 family had no committed baseline at all — the family was not merely uncovered,
   it was unnameable (transcript `.scratch/r19-o01/prestate-r18-tree.txt`).
2. **Uninformative red** — over today's tree, where the D4 baselines exist: exit **2**, `pass 7`,
   `baselines_found 17`, `pinned 15`, readings `{"no baseline": 2, "pinned": 15}`, and still
   `gates_uncovered []`. The two D4 rows are rejected as `BASELINE-GATE-UNKNOWN` ("not one of the
   seven registered gates") and the coverage summary cannot express the gap
   (transcript `.scratch/r19-o01/prestate-default-run.txt`).

The lesson the design takes from this: *a gate set is not coverage*. Registering a gate makes the
battery ask for its baseline; executing a gate is a different claim; and a coverage counter that only
counts the names it was told about will always report a full house.

## 2. The design decision: the D4 adapters join the **coverage** duty, not the selftest duty

The battery has two duties. The D4 adapters are thin, read-only entry points over peers outside
`tools/gates/`:

- `tools/gates/d4-typed-labels-check-gate.py` resolves `ROOT` from `__file__` and runs
  `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check <input>`.
- `tools/gates/d4-assembly-check-gate.py` resolves `ROOT` from `__file__`, `runpy`-loads
  `tools/assemble-culture-d4.py`, and byte-compares its build against the input path.

Neither can be a mirror leg: a mirror of `tools/gates/` holds neither the peers nor
`examples/culture-d4/`, so a mirrored `--selftest` launch could only report could-not-evaluate. The
design therefore splits by *what each duty can honestly measure*:

| Surface | Gate set | Mechanism | What it is evidence of |
|---|---|---|---|
| duty 1, selftest legs | `GATE_NAMES` (7 structural) | disposable mirror of `tools/gates/`, `cwd = mirror` | capability: these gates can fail |
| duty 2, coverage | `REGISTERED_GATE_NAMES` (9) | read-only over the baseline roots | conformance: every registered gate has a committed, pinned baseline |

The two D4 adapters are registered in duty 2 only. `REGISTERED_GATE_NAMES` is what the coverage
check asks for, so a missing D4 baseline now reads `BASELINE-GATE-UNCOVERED`, exit 2 — the family is
inside the battery's requirement surface. Their *capability* evidence is their own `--selftest` where
they carry one (`d4-typed-labels-check-gate.py` exits 0 through its peer's 39-check matrix) and their
round-18 frozen row otherwise; the battery neither fabricates a leg for them nor substitutes another
gate's check.

**Rejected alternatives.**

- *Run the D4 adapters as battery selftest legs from their live paths.* Implemented, measured, then
  withdrawn — see §3. It needs a gate change this seat's brief forbids, and it makes the round's own
  claim-O reading red.
- *Substitute the peer's selftest for an adapter that has no `--selftest`.* Rejected as a laundering
  channel of the round-18 kind: a leg reporting a green from a different gate's control matrix is not
  capability evidence for the gate under test.
- *Mirror the whole repository so the adapters can run in isolation.* Rejected: the mirror would then
  hold the corpus and the examples, and "the mirror holds the bytes under test" stops being checkable
  by a reader.

## 3. The 9-leg variant: tried, measured, withdrawn (recorded because it is the reason for §2)

Between 11:38Z and 12:35Z this seat implemented and measured the stronger reading — a third leg group
running both D4 adapters' `--selftest` from their live paths, with the preservation snapshot widened
to 32 files (nine gate scripts, the fixture tree, both adapters' peer tools). Readings at that
revision (`sha256 83d9e3e5…`, transcript `.scratch/r19-o01/battery-9leg.json`):

```text
$ python3 tools/gates/d4-assembly-check-gate.py --selftest
assembly error: [Errno 2] No such file or directory: '--selftest'      # exit 2, 20 poll ticks 11:40–11:59Z
$ python3 tools/check-gate-battery.py
exit 2   pass 8   fail 0   unevaluable 1   coverage 9/9
```

Two independent reasons retired that variant:

1. **It cannot be made green inside this seat's brief.** The only missing piece is a `--selftest`
   mode on `d4-assembly-check-gate.py`, i.e. a gate behavior change — forbidden here, and one that
   would orphan that gate's freshly frozen `r19-pre` baseline (its `gate_sha256` pin would read
   `gate_revised`) unless another seat re-pinned it.
2. **The round's counting command defines claim O the other way.** The runner owner rewrote
   `reports/round-19/run-validation.py` at 12:33Z (`sha256 ffee0643…`); its claim-O docstring now
   reads: "This round registers them (the battery's duty-2 baseline coverage reads 9/9: seven
   structural gates plus the two D4 adapters, with the battery's own `--selftest` controls green)",
   and its O1 check accepts `pass` of 7 or 9 — and rejects an incoherent 8
   (`the battery executed 9 gates but passed 8`). The 12:33Z receipt
   (`reports/round-19/validation.json`) records exactly that rejection, with `changed_gates: []` and
   `d4_baselines.problems: []`: the D4 baselines and gate surfaces were already green, and the
   battery's 8-pass state was the sole claim-O failure.

The withdrawn variant left one real gain behind, kept in the shipped tool: the preservation snapshot
now covers all **nine** registered gate scripts (30 files, was 28), because duty 2 hashes every
registered gate against its baseline's `gate_sha256` pin, so those bytes are read by the battery and
belong under its "originals preserved" measurement. The peer tools were dropped from the snapshot
along with the live legs: the battery does not read them, and keeping them would make an unrelated
peer edit read as a live-tree change.

## 4. What "9/9" means in the report, in two counters

- `summary.pass` — the executed selftest legs: seven (the structural gates). Named in the report, not
  inferred.
- `baselines.summary.coverage` — `"<covered>/<registered>"`, newly emitted by this round: `"9/9"`.
- `baselines.summary.gates_registered` — the denominator, emitted so a reader never has to derive it
  from the covered list's length.

They are deliberately separate and neither is derived from the other, because the pre-state's failure
mode was exactly this conflation: `pass: 7` was readable as "the lane's gates are covered" when the
constant was the only thing being counted. The C-seat entry
`corpus/knowledge/verification/gate-battery-surface-verification.md` §4 left the control of that
growth explicitly open ("a growing constant silently changes what '7/7' means"); emitting the
denominator and the ratio beside the list is this seat's answer, and the entry now needs a successor
(§6).

## 5. Boundary — what this design does not claim

- Not a clearance: `pass` counts selftest legs, not design quality; `pinned` means digests and pins
  hold, never that a verdict was compared.
- Not canon, not lore receipt, no real-world rights ruling.
- The D4 adapters are **not executed** by the battery. A reader who wants their runtime behavior has
  the round-18 frozen rows (`tools/gates/frozen/round-18/MANIFEST.tsv`) and the adapters' own
  `--selftest` where it exists — not this report.
- The preservation snapshot covers `tools/gates/*` (nine scripts + fixtures); it does not cover the
  corpus or `examples/`, and a rewrite with identical bytes still passes.

## 6. Cross-seat dependency this change creates (for the integrator)

`corpus/knowledge/verification/gate-battery-surface-verification.md` (a C-seat entry landed this
round) describes the battery in the present tense as "the seven legacy gate selftests … it does not
cover gates outside its seven-name constant", and its §4 decision record lists as **open
(to-verify)**: "whether the D4 family should join the battery's constant, and if so how the constant's
growth is itself controlled … Owner: this lane's O axis; not disposed here."

This seat's change answers that open question, which makes the entry's present-tense claims a
pre-state reading. The entry's own `recheck` clause requires the successor to be a **new entry**,
never a rewrite — so it is routed to the C axis rather than edited here. Not fixed by this seat; no
byte of that entry was touched.
