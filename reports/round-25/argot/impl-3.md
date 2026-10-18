# R25-D05 — argot-derivation leg, impl 3 of 6: the delivered-vs-forecast delta

- **Seat:** R25-D05, round 25, claim **D**. Date 2026-10-18.
- **Write scope:** this file only.
- **Canon:** NON-CANON engineering evidence.

The claim requires the delta to be **named, not silently dropped**. The sibling
analysis (`forecast.md`, `current-state.md`, `delta.md`, seats R25-D01..D04)
established the wide delta; this fragment records the *measured* narrow delta the
implemented leg binds to its own numbers, and it is the delta the runner's
`measure_argot` reads.

## 1. What the forecast asked for, and what the leg measures

| forecast element (`design-brief.md` Δ3, `:300-310`; control C-02 `:456`) | delivered? | measured by the leg |
|---|---|---|
| two declared operations `head2`, `reverse` with exact algorithms | **algorithm yes, applied forms no** | `head2`/`reverse` embedded as an explicit table; the 11 worked design rows re-derive in `selftest` (`design-table-rederived-11`) |
| every derived quote form's check passes (zero fails) | **no such forms exist** | `derived_pairs=0` on the delivered D4 packet |
| `derived_from` + `derivation` fields between two records of the same packet | **no such field in the schema** | the leg reads the shape when present; 0 present on D4 |
| coverage block reports `derived_forms`/`derived_ok` agreeing | **not delivered** | the leg's own `coverage:` line reports `derived_pairs`/`violations`; it does not claim the projector's block exists |
| control: a fixture whose quote form ≠ `apply(op, base)` → FAIL `D4L-ARGOT-DERIV` | **delivered** | the committed fixture plants four such rows; `selftest` asserts the exact id set |
| the D4 typed gate grows the leg with selftest controls | **delivered** | the typed gate invokes the sibling and names it in `--selftest-generalized` (`impl-5`) |

## 2. The substitution the leg actually grades — and it is not a silent swap

The delivered D4 is the **furnace league** (FIRE × MARK), not the forecast's
weigh-court quote register; `design-brief.md:596-670` records the eight-seat
divergence and path A (keep the landed tree) was taken. Δ3 therefore has no
quote-register domain to grade. The leg does **not** invent one. It grades the
two derivation relations the delivered tree *does* state:

1. **the eight name formations** `NM-01..NM-08` against `CX-01` (a real,
   delivered derivation relation between stated inputs and a delivered form);
2. **the six loan adaptations** `L-49..L-54` against their declared layers'
   `substitutions` (a real, delivered derivation relation of the same
   `apply(op, base) == form` shape).

So `D4L-ARGOT-DERIV` is live and has teeth on the delivered tree, while the
forecast's *specific* register-scoped relation is named as **not delivered** in
three places: `derived_pairs=0` in the coverage line, the `D4L-ARGOT-COVERAGE`
HOLD when a packet declares the operations but ships no pair, and this table.

## 3. The delta's own control

A packet that declares the argot operations and ships no `derived_from` pair
reads `D4L-ARGOT-COVERAGE` HOLD rather than silence — asserted in `selftest` as
`coverage-hold-fires`, and measured on a mutated D4 in `impl-5`:

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r25-d05/controls/c4-declared-not-delivered.yml
FINDING D4L-ARGOT-COVERAGE: HOLD — packet declares the argot operation(s) head2, reverse and 6 register-scoped form(s), but no record carries a derived_from/derivation pair; the forecast derivation relation is declared, not delivered
exit 1
```

That is the honest reading of the delivered tree: the relation is *declared*
(by the design and, under mutation, by a packet) and **not delivered**, and the
leg says so in a named HOLD instead of grading an empty set as clean.

## 4. Spelling delta (recorded, not resolved)

The claim text says `D4L-ARGOT-DERIV`; this assignment's header says
`D4L-ARGOT-DERV`. The round-17 design (`design-brief.md:308,456`) and
`claims.json:22` both say **`D4L-ARGOT-DERIV`**, and that is the id implemented
and asserted. The one-letter variant in the assignment is recorded here as a
delta for the integrator; nothing else in the lane emits either spelling.
