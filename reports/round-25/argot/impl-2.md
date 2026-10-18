# R25-D05 — argot-derivation leg, impl 2 of 6: scope, and the false-positive class it closed

- **Seat:** R25-D05, round 25, claim **D**. Date 2026-10-18.
- **Write scope:** this file only (the gate it describes is `impl-1`'s).
- **Canon:** NON-CANON engineering evidence.

## 1. The problem this leg must not create

The claim's O-sibling states the lane's own hazard verbatim: the gate "manufacture[s]
findings" when fed input it was not designed to read, and the fix must be
"fail closed and honestly". A new leg that reads the wrong fields manufactures
exactly that class at a new address. Two measured near-misses, both caught
before landing:

### 1.1 `symbols[*].form:` and `contact[*].name:` are not language forms

A first cut selected any record with a `form`/`name` key. On the live D4 packet
that read **14** extra records:

```
$ python3 - <<'EOF'   # first-cut scope probe, 2026-10-18
… for key in sorted(doc): if isinstance(doc[key], list) …
EOF
contact CT-01 | form= the salt road          | reg= trade
contact CT-02 | form= the north ore road     | reg= craft
symbols SYM-01 | form= a stamped impression from the mold's own | reg= craft and law
symbols SYM-02 | form= the banked fire's visible flame at the f… | reg= public
symbols SYM-03 | form= the direction and density of the column   | reg= public, ambiguous
symbols SYM-04 | form= the burst of steam when a hot cast enter  | reg= craft, in-ward
symbols SYM-05 | form= the year's ash gathered at the yard's ed  | reg= ritual
symbols SYM-06 | form= counted stacks of ingots at the weigh-st… | reg= trade
symbols SYM-07 | form= the paired bellows and their rhythm       | reg= craft
symbols SYM-08 | form= the furnace mouth and its stone lintel    | reg= public
layers LY-01/LY-02 | form= the layer name                      | reg= trade/craft
```

`SYM-01`'s `form:` describes a *medium* ("a stamped impression from the mold's own
geometry") and `CT-01`'s `name:` labels a *road*. Neither is a string the
sound-and-identity channel could check. Grading them would have manufactured
findings out of prose — the same class the O claim repairs.

**Rule landed:** a form record must carry a lexical form field (`term`,
`quote_form`), or a lexical marker (`derived_from`, `derivation`, `donor_form`,
`loan_layer`, `route`, `formation`). `form:`/`name:` alone are not a language
form. `symbols` and `contact` blocks are therefore out of scope by construction,
and the fixture carries a `symbols` row with `register: quote` and `form:` prose
precisely as the scope control (see `impl-4`).

### 1.2 `register: plain` is not an argot register

`plain` (and `neutral`, `standard`, `ordinary`) is the **unmarked** register —
the baseline the argot is measured against. Treating it as scoped would make a
plain form's stated derivation an argot obligation. The rule landed:
`UNMARKED_REGISTERS = ("plain", "neutral", "standard", "ordinary")` are reported
as unscoped, and the fixture carries one `register: plain` row as the control.

## 2. Measured effect of the scope rules

| run | command (2026-10-18, `TMPDIR=$PWD/.scratch`) | records | register_scoped | findings |
|---|---|---:|---:|---|
| first cut, over-broad | `.scratch/r25-d05/scope-probe.py` (scratch) | 156 | 20 | 14 manufactured rows |
| landed | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 156 | **6** | **0** |
| landed, D2 | `… examples/culture-d2/packet.d2.yml` | 138 | **0** | **0** |

The six are exactly `L-49..L-54`. D2 reads 0 register-scoped records: its
lexicon carries no `register`, its layers are declared without a `register`
key, and it has no `derived_from`/`derivation` pair — so the leg is silent on D2
by measurement, not by a hard-coded family check.

## 3. Control

The fixture (`impl-4`) carries the two scope controls as planted rows whose
*absence* from the expected finding set is the assertion: a `symbols` record with
`form:` prose and `register: quote`, and a `lexicon` record with
`register: plain` and a declared `reverse` derivation that is deliberately wrong.
Neither may emit a finding; the fixture's pinned id set is four
`D4L-ARGOT-DERIV` + one `D4L-ARGOT-RULE`, and `selftest` asserts the exact set.
