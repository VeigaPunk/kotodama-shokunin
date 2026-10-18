# R25-D05 — argot-derivation leg, impl 6 of 6: execution receipt, regressions, and the runner

- **Seat:** R25-D05 (integrator for the touched files), round 25, claim **D**.
  Date 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  worktree HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only. All commands below ran at the lane root with
  `export TMPDIR=$PWD/.scratch`; the runner ran in an isolated clone.
- **Canon:** NON-CANON engineering evidence.

## 1. Artifacts landed by this seat

| path | sha256 | state |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` | new, flagless, read-only |
| `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` | new fixture |
| `tools/gates/fixtures/argot-derivation-gate.expected` | `38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018` | new pinned id set |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | round-25 binding added (a call, not a re-implementation) |
| `reports/round-25/argot/impl-1.md` … `impl-6.md` | this fragment set | new |

No packet, component, projector, adapter, pin file or filed round-8–24 byte was
touched. No commit, no push.

## 2. Execution receipt (2026-10-18, `TMPDIR=$PWD/.scratch`)

| command | exit | observed |
|---|---:|---|
| `python3 tools/gates/argot-derivation-gate.py --selftest` | 0 | `selftest: 21/21 checks passed` |
| `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | `records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| `python3 tools/gates/argot-derivation-gate.py examples/culture-d2/packet.d2.yml` | 0 | `records=138 register_scoped=0 … claimed_chains=8 violations=0` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | `19/19 checks passed` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | 0 | `16/16 checks passed` (was 14/14; the two new controls name the argot leg) |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | `20/20 legs passed` (was 19/19), output sha256 `d36a9f9b…` |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 0 | `17/17 legs passed` (was 16/16), output sha256 `df1bb53b…` |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml` | 0 | `16/16`, output sha256 `15cdfbda…` = the frozen pin, **byte-identical** |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml` | 0 | `13/13`, output sha256 `9a69985a…` = the frozen pin, **byte-identical** |
| `python3 tools/gates/typed-pipeline-gate.py` (flagless D2 default) | 0 | `16/16`, unchanged |
| `python3 tools/gates/naming-collision-gate.py --selftest` | 0 | unchanged (12 findings / 11 ids) |
| `python3 tools/check-gate-battery.py` | 0 | `coverage 9/9`, `pass 7`, `preserved: true`, `modified 0` |
| `python3 tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 35/35` |
| `python3 tools/assemble-d2.py --check` | 0 | `byte-identical deterministic assembly` |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 0 | `byte-identical deterministic projection` |
| `python3 reports/round-25/run-validation.py --check` (isolated clone) | 0 | **O PASS, D PASS, C PASS**; `acceptance_checks_passed: true`; `missing_dependencies: []` |

### 2.1 The negative controls

| control | command | expected | observed |
|---|---|---|---|
| fixture, four planted violations + one unreplayable declaration | `… argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml` | exit 1, ids = `D4L-ARGOT-DERIV`×4 + `D4L-ARGOT-RULE`×1 | as expected (`fixture-counts-pinned`) |
| broken loan adaptation | `… c1-bad-donor.yml` (D4 with `donor_form: "rash"`) | exit 1, `D4L-ARGOT-DERIV` | exit 1, 1 violation |
| the design's own head2 trap | `… c2-bad-derivation.yml` (adds `Q-99 saalum` head2←`saalumi`) | exit 1, `D4L-ARGOT-DERIV` | exit 1, 1 violation |
| a clean pair added to the same packet | `… c3-good-derivation.yml` | exit 0 | exit 0, 0 violations |
| declared-but-undelivered relation | `… c4-declared-not-delivered.yml` | exit 1, `D4L-ARGOT-COVERAGE` | exit 1, as expected |
| the runner's own violating probe | `… typed-pipeline-gate.py .scratch/round-25/validation/argot-control/violating.d4.yml` | non-green, names `argot` | exit 2, `argot|deriv` matched, `argot_id_emitted: true` |
| malformed inputs | three probes in `selftest` | exit 2, `D4L-ARGOT-DATA`, no traceback | as expected |

Controls ran in `.scratch/r25-d05/controls/` and
`.scratch/r25-d05/typed-controls/`; never against the delivered tree.

## 3. Runner state at this seat's close

```
$ cd .scratch/r25-d05/clone && python3 reports/round-25/run-validation.py --check
claim C passed= True
claim D passed= True
claim O passed= True
acceptance_checks_passed: True   missing_dependencies: []
```

The D measurement now reports `argot_gate.typed_gate_carries_the_leg: true`,
`selftest_exit: 0`, `selftest_summary: "selftest: 21/21 checks passed"`,
`d4_run_exit: 0`, `control_violating_derivation.argot_id_emitted: true`, and the
runner's independent re-derivation agrees on 11/11 design pairs.

## 4. What remains, and who owns it

1. **The frozen round-25 row for the typed gate is now stale.**
   `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` pins
   `typed-pipeline-gate.py` at `879d40bf…` with the D4 outputs
   `b064da28…`/`38dc76dc…` (19/19, 16/16). The live gate is `b749ad07…` with
   `d36a9f9b…`/`df1bb53b…` (20/20, 17/17). A re-pin is a **new row** owned by
   the round-25 scribe (R25-D19); no filed MANIFEST was edited here. The D2 rows
   are unaffected and still reproduce byte-for-byte.
2. **`tools/gates/frozen/round-22/d4-repin/freeze-receipt.json`** pins
   `typed-pipeline-gate.py` at `04ad4bb4…`; that generation is round-22's and is
   not re-pinned by this round's work — the round-25 row supersedes it for the
   live surface.
3. **The forecast's specific register-scoped relation is still not delivered**
   (`derived_pairs=0`). The leg grades the two derivation relations the landed
   furnace-league tree actually states and names the gap in a HOLD; closing it
   would require the schema + `constructions` + engine delta that `delta.md`
   enumerates, which is a design decision above this seat.
4. **The id spelling** `D4L-ARGOT-DERIV` (design + `claims.json`) vs
   `D4L-ARGOT-DERV` (this assignment's header) is recorded in `impl-3` §4.

## 5. Limits

- Every measurement binds to its stated snapshot; the round-25 tree was moving
  throughout and the parent must re-run the runner on the final settled tree.
- The sibling loads `tools/gates/naming-collision-gate.py` by path: if that
  file's private helpers are renamed, the leg reads exit 2 with a named
  diagnostic rather than silently degrading — but the coupling is real and is
  declared in the gate's own docstring with the digest printed per run.
- No acceptance, canon standing, source-freshness certification, or lore handoff
  is asserted by any file in this set.
