# R26-D15 — argot execution 3: the delivered-vs-design delta, element by element

- **Seat:** R26-D15 (D axis, argot execution 3 of 4), round 26, loop 3 build 2 of 4,
  claim **D** `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`. Stamps UTC.
- **Write scope:** `reports/round-26/register/execution-{1..4}.md` only; scratch
  under `.scratch/r26-d13/` only. No tool, gate, packet, component or filed
  rounds 8–25 byte written; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

Executions 1 and 2 measured the replay and its controls. This one measures
**what is on disk against what the round-26 register design specifies**, so that
no element of the design is silently absorbed into a green reading. The
authority for the design side is `reports/round-26/register/{design,forms,rules}.md`
(this round); the authority for the forecast side is
`reports/round-25/argot/delta.md` (F-1..F-8, Δ1-class2, Δ2) and
`reports/round-17/d4/design-brief.md` Δ3/Δ5.

## 1. The headline: the stratum's data did not land

Measured at 2026-10-18T18:12:57Z, after the design files landed:

| surface | command | result |
|---|---|---|
| packet digest | `sha256sum examples/culture-d4/packet.d4.yml` | `e7ecd204…` — **byte-still since round 25** |
| lexicon component | `sha256sum examples/culture-d4/components/04-lexicon.yml` | `74c2561b…` — byte-still |
| register data in components | `grep -c "STAMP\|register: stamp" examples/culture-d4/components/04-lexicon.yml` | **0** |
| a register-contract component | `ls examples/culture-d4/components/06-register-contract.yml` | **absent** |
| register packet keys | `grep -c "^registers:" examples/culture-d4/packet.d4.yml` | **0** |
| the register hold id | `grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/ \| wc -l` | **0** |
| the leg's own coverage | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`, exit 0 |

The six `register_scoped` records the gate finds on the delivered packet are
**pre-existing trade/craft loans**, not register forms — measured by this seat's
census (`argot-census.py`) with the gate's own scoping rule:

```
L-49 sal  register=trade     L-52 res  register=trade
L-50 kar  register=trade     L-53 gal  register=craft
L-51 gul  register=trade     L-54 mar  register=craft
```

So `violations=0` over the delivered packet is, exactly as round 25 left it, a
clean verdict over a domain with **no register derivation to replay**.

## 2. Element-by-element: the round-26 design against the delivered tree

| # | design element (source) | delivered? | delivered-side evidence |
|---|---|---|---|
| E-1 | 8 register-scoped lexicon records `RF-01..RF-08` with `register: stamp`, `derived_from`, `derivation` (`forms.md` §1) | **NOT DELIVERED** | `grep -c "register: stamp"` over components → **0**; `derived_from` over `examples/culture-d4/` → **0** as a record field (one unrelated comment in `handoff-packet.sample.yml`) |
| E-2 | the `LENGTHEN` rule row in `morphology.derivation_rules` (`rules.md` §3) | **NOT DELIVERED** | `grep -c "LENGTHEN" examples/culture-d4/packet.d4.yml` → **0**; the registry carries exactly `CX-01/02/03` |
| E-3 | `derived_from`/`derivation`/`register` in `contract.record_fields.lexicon` (`design.md` §6) | **NOT DELIVERED** | the delivered field list is `id, term, gloss, field, route, bases, construction, layer, stage, axis, evidence, follows` — none of the three |
| E-4 | a `registers:` packet block declaring `plain`/`stamp` (`rules.md` §1) | **NOT DELIVERED** | `grep -c "^registers:"` → **0**; the one `registers` substring is prose in `provenance` (`packet.d4.yml:2211`) |
| E-5 | the register **law** rows RGL-01..RGL-05 (`forms.md` §5) | **NOT DELIVERED** | no component owns it (`design.md` §6, RL-6); the delivered tree has no register-contract component |
| E-6 | the era rule `REGISTER-ERA-01` (`rules.md` §5) | **SPECIFIED, UNIMPLEMENTED** | the gate has no era concept; the design's own `ctrl-early-era.yml` produces **no era finding** (re-run by this seat at 18:11Z: exit 1 from the 6 `lengthen` HOLDs, no `D4L-ERA`) |
| E-7 | the inventory check `C-INV` (`rules.md` §7) | **SPECIFIED, UNIMPLEMENTED** | same as E-6; the design records it as ❌ |
| E-8 | the derived-vs-forecast addressability fix (`design.md` §1, `review.md` RD-1) | **DELIVERED as design** | the re-host onto FIRE × MARK is designed and measured; the `AL-*`/`GD-*`/`D4-X*` forecast keys remain absent (they name records that never shipped) |

## 3. What the forecast asked for, and what now answers it

The round-25 delta (`reports/round-25/argot/delta.md` §2) disposed F-1..F-8,
Δ1-class2, Δ2, the six loans and the name-side argot as **not delivered**. Round
26 changes the disposition of exactly **one** of those rows — and only in
principle, because the data did not land:

| forecast row | round-25 disposition | round-26 disposition |
|---|---|---|
| F-1 quote forms derived from a plain base by a declared operation | NOT DELIVERED | **design delivered, data not landed** (`forms.md` §1 + §2 fix the two operations) |
| F-2 the two operations `head2` / `reverse` | NOT DELIVERED | **partially re-scoped**: `reverse` kept; `head2` **dropped** and replaced by `lengthen`, because `head2` has no proper domain over the delivered tree (`rules.md` §3.2, RL-2) |
| F-3 the check fields `derived_from` + `derivation` | NOT DELIVERED | **specified** (`design.md` §6); not on disk |
| F-4 a relation between two records of the same packet | PARTIALLY MET (base→compound, not plain→quote) | **specified in the forecast's own shape**; the register forms are exactly plain-base → register-form pairs |
| F-5 zero fails | VACUOUSLY SATISFIED | still vacuous on the delivered packet; **non-vacuous on the candidate** (execution 1) |
| F-6 coverage block `derived_forms`/`derived_ok` | NOT DELIVERED | **not designed**; the leg reports `derived_pairs`/`violations` instead. The forecast's exact counters remain undelivered and are named here |
| F-7 control-only id `D4L-ARGOT-DERIV` | producer landed round 25; 0 in D4's bytes | **unchanged**: the id still occurs 0 times under `examples/`; the candidate's clean run emits none, its controls emit it |
| F-8 required-controls row C-02 | NOT DELIVERED | **met on controls** (execution 2 §5) |
| Δ1-class2 register slots / `D4L-REGISTER-UNRESOLVED` | NOT DELIVERED | **not designed in this form**: the round-26 design carries a register *field* + a `registers:` block, not `<id>#plain`/`<id>#quote` slots, and defines **no** owed-doublet hold. Named as a deliberate divergence, not a silent drop |
| Δ2 slot cardinality / `doublet_of` | NOT DELIVERED | **not designed**: no `doublet_of` in the round-26 design; the `doublets` packet key the assembler already admits (`tools/assemble-culture-d4.py:81,118`) is unused |
| AL-01..AL-06 loans; name-side argot | NOT DELIVERED | **re-hosted**: the round-26 design replaces them with the 8 `RF-*` forms (RD-1) |

**Three forecast elements are therefore formally closed as "superseded by
re-host"** (the `AL-*`/name-side argot, Δ1-class2's slot shape, Δ2's cardinality
shape) and **one is closed as "not designed"** (F-6's counters). Every other row
is a data landing still owed. Nothing is silently dropped.

## 4. The delta that is *this round's*, not the forecast's

Execution 1 measured a defect the design itself carries and no earlier file
names: the rule's op token is `lengthen` in `rules.md` §2 and `LENGTHEN` in
`rules.md` §3's registry entry. A landing that copies both literally produces 6
`D4L-ARGOT-RULE` HOLDs and a red gate (execution 1 §2, Run A). This is a
**cross-file consistency requirement on the landing**, and it is the round-26
delta the parent should carry forward if the stratum lands in a later round.

## 5. Limits

- This file disposes elements; it lands none. The design explicitly refuses to
  write the forms into `examples/culture-d4/` (`design.md` §0), and this seat
  does not either.
- The "NOT DELIVERED" rows are measured against the digests in execution 4 §5;
  the stratum landing is a re-read event.
