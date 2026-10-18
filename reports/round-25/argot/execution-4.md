# R25-D14 — argot-derivation leg, execution 4: the register-form replay, and the leg's honest scope

- **Seat:** R25-D14 (argot execution 4 of 4), round 25, loop 3 build 1 of 4,
  claim **D** `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only; scratch under `.scratch/r25-d11/` only.
- **Canon:** NON-CANON engineering evidence.

Executions 1–3 measured the positive replay, the negatives, and the delta. This
one runs the **register-form** half the assignment names — replaying the
register-scoped forms against their stated inputs — and records what the leg
can and cannot honestly claim.

## 1. The register-form replay, attempted

The forecast's register surface (Δ1 class 2 / Δ3) is a `<id>#quote` slot holding
a supplied form derived from a `<id>#plain` base by `head2` or `reverse`. A
replay of register forms therefore needs three things present in the packet:

1. a register-scoped slot pair (`<id>#plain` / `<id>#quote`, or `slot_ref`);
2. a `derived_from` pointer naming the base record;
3. a `derivation` naming the operation (`head2` / `reverse`).

Measured over the delivered D4 packet (`examples/culture-d4/packet.d4.yml`,
sha256 `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3`):

```
grep -c "derived_from"      examples/culture-d4/packet.d4.yml   → 0
grep -c "head2"             examples/culture-d4/packet.d4.yml   → 0
grep -c "#plain\|#quote"    examples/culture-d4/packet.d4.yml   → 0
grep -c "slot_ref\|doublet_of" examples/culture-d4/packet.d4.yml → 0
grep -c "derivation:"       (line-anchored)                      → 0
```

**Result: zero register forms to replay.** The register-form leg has no input on
the delivered tree. This is not a leg failure — there is no register surface for
it to grade, and the absence is the delta execution-3 records.

The replay that *does* have input is the delivered base→form surface, and it is
green: execution 1, 12/12 rows, 0 violations; independent corroboration
`reports/round-25/audit/x47-argot-negatives-audit.py` R25-X47-1 (11/11 design
rows reproduce, deterministic) and R25-X47-4 (the leg is discriminating: the
untouched pair passes, a mutated pair is rejected).

## 2. Why the register leg cannot be switched on through the *existing* engines

A naive implementation — add `head2`/`reverse` to the packet's `constructions`
and let the existing lexicon engine replay them — **manufactures a false FAIL on
a correct packet**. The live lexicon replay engine is concatenation-only: it
substitutes `B1`…`Bn` into `construction.pattern`, strips `+`/`-`, and compares
to the record's `term`. Under that model a correct `reverse` derivation and a
wrong one produce the *same* finding, and the correct one is red.

This is measured, not asserted — the peer audit's controls N-2 and N-3
(`reports/round-25/argot/current-state.md` §6.2):

| fixture | form | engine's verdict |
|---|---|---|
| N-2 | `nim` derived from `min` by `reverse` (**correct**) | `D-form-mismatch … (expected 'min')`, exit 1 |
| N-3 | `min2` derived from `min` by `reverse` (**wrong**) | identical `D-form-mismatch … (expected 'min')`, exit 1 |

So the register-form leg needs an engine that carries an **operation field with
alternate operations**. The two live *lexicon/name* engines do not; a **third,
purpose-built gate does** — and it landed while this seat was writing (see §2.1).

### 2.1 The late-landing register gate (found at 17:36Z, after this seat's first draft)

`tools/gates/argot-derivation-gate.py` is a peer-landed, flagless, read-only
gate that implements **exactly** the leg this file's §1 measured as absent. It
is **under active edit by its author while this seat works**: this seat observed
its sha256 move `82f48649…` → `8528ad77…` → `55f83442…` between 17:36Z and
17:39Z, and its own `register_scoped` count over D4 move `18` → `6`. The
measurements below are pinned to the runs named, not to a live sha. This seat
ran it (first run, 17:37Z):

```
export TMPDIR=$PWD/.scratch
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
→ coverage: … records=156 register_scoped=18 derived_pairs=0 borrow_pairs=6 violations=0 rule_holds=0
→ exit 0
```

It carries an explicit `OPS` table for the two forecast operations with the
design's maximal-onset algorithm (`op_head2('saalumi')` → `saalu`;
`op_reverse('makun')` → `nukam`), plus a `DESIGN_TABLE` of the 11 worked rows,
plus three rule sources (the built-in argot ops, a packet
`morphology.derivation_rules` entry, and a borrowed record's layer
`substitutions` over its `donor_form`).

**Its `D4L-ARGOT-DERIV` FAIL path is real and discriminating** — this seat's own
controls over its `POSITIVE_CONTROL` fixture, one mutation each:

| control | injected change | gate output |
|---|---|---|
| positive | none | `violations=0`, exit 0 |
| `head2-wrong` | `saalu` → `saalum` | `D4L-ARGOT-DERIV: FAIL … 'head2' applied to 'saalumi' yields 'saalu'`, exit 1 |
| `reverse-wrong` | `nim` → `min` | `D4L-ARGOT-DERIV: FAIL … 'reverse' applied to 'min' yields 'nim'`, exit 1 |
| `rule-wrong` | `sunel` → `sunell` | `D4L-ARGOT-DERIV: FAIL … 'CX-01' applied to 'su+nel' does not yield …`, exit 1 |
| `borrow-wrong` | `donor_form resh` → `ressh` | `D4L-ARGOT-DERIV: FAIL … layer 'West layer' substitutions applied to donor form 'ressh' yield 'ress'`, exit 1 |
| `coverage` | ops declared, no `derived_from` pair | `D4L-ARGOT-COVERAGE: HOLD — the forecast derivation relation is declared, not delivered`, exit 1 |
| D4 loan tamper | `L-50 donor_form khar` → `kharx` | `D4L-ARGOT-DERIV: FAIL … layer 'Salt-road trade layer' substitutions applied to donor form 'kharx' yield 'karx'`, exit 1 |

**This changes §1's conclusion in one respect.** The leg is **no longer only a
scratch harness**: a lane gate exists that produces `D4L-ARGOT-DERIV`, replays
the two forecast operations, and holds `D4L-ARGOT-COVERAGE` when the relation is
declared but not delivered. What §1 measured — that the *delivered D4 packet*
carries no register-scoped `derived_from`/`derivation` pair — is unchanged and
still true (`derived_pairs=0` over D4, `violations=0`): the gate finds nothing to
fail on D4 because D4's register forms were never built (execution 3). So the
gate's exit 0 over D4 is a **structural pass on an empty register domain**, not a
clearance — the gate's own docstring says exactly that ("a capability plus a
replay, not a clearance").

Two limits of the late-landing gate, measured by this seat at 17:37–17:39Z: its
`--selftest` currently fails while its fixtures land — the first run reported
`fixture unreadable: … fixtures/argot-derivation-gate.yml` (the `.yml` was not on
disk), and a later run reported the `.expected` companion missing instead, so the
fixture pair was arriving during this seat's window; and the gate is being edited
in place (sha moving, `register_scoped` count moving `18` → `6`). Both are the O
claim's and the gate's author's to close; this seat reports them, does not repair
them.

## 3. What this seat delivered, and its status

| leg | status | evidence |
|---|---|---|
| base→form replay over D4's stated inputs (the representable half) | **DELIVERED and measured** | `execution-1.md` §2: 12/12 rows, 0 violations, command + digest |
| violations named on tampered input | **DELIVERED and measured** | `execution-2.md` §1-§2: two controls, one violation each, message names record + rule + values |
| false-red attribution (the O hazard on the argot surface) | **DELIVERED and measured** | `execution-2.md` §3: source clean, typed-direct clean, L2-rebuilt mirror manufactures 8 `DERIV-REPLAY` rows by doubling the regex backslash |
| register-form replay | **NO INPUT ON THE DELIVERED TREE** | this file §1: 0 register slots, 0 `derived_from`, 0 operations — unchanged; the register gate now exists (§2.1) but D4 carries nothing for it to replay |
| delivered-vs-forecast delta | **WRITTEN, elements named** | `execution-3.md` §2: F-1..F-8, Δ1-class2, Δ2, AL-01..06, name-side argot, the 11 derivations |
| `D4L-ARGOT-DERIV` producer in an engine | **LANDED BY A PEER at 17:36Z, not by this seat** | `tools/gates/argot-derivation-gate.py` §2.1: emits the id on 4 controls; 0 occurrences in D4's own bytes (the delivered relation is still absent) |

Per the SKILL's honest-stop rule (`SKILL.md:60-66`), the half this seat did not
build is reported as such and not forced. The claim's after_required says "the
delivered-vs-forecast delta recorded (any forecast element not delivered is
named, not silently dropped)" — satisfied by `execution-3.md`; and "the leg
implemented and executed on D4" — now satisfied by the peer gate (§2.1) plus
this seat's execution over the delivered derivation surface (execution 1). This
file is the scope statement that keeps each half from being read as more than it
is.

## 4. The growth path (named, not taken)

For a later round that chooses to build the register half, in order:

1. **The culture decision first.** The register surface belongs to the
   weigh-court D4 (round-17 reconciliation path C), not the shipped
   furnace-league D4 (path A). Building register slots onto the furnace-league
   packet without that decision would be a silent culture absorption — the
   round-17 brief seat already named this as the parent's call
   (`design-brief.md:653-663`).
2. **Then the engine.** A replay engine that carries an `operation` field with
   `head2`/`reverse` as alternates, plus a `derived_from` pointer resolved to a
   base record — the lexicon-coverage audit's leg D (`tools/gates/lexicon-coverage-audit.py:740-880`)
   is the natural host, and its concatenation-only model is the thing to extend.
3. **Then the id.** `D4L-ARGOT-DERIV` as a FAIL class, emitted in the control
   only, with the packet's own debt set free of it (`design-brief.md:308-310`).
4. **Then the controls.** The battery's C-02 (`design-brief.md:456`) plus a
   positive control, so the leg is shown discriminating — the shape
   `x47` R25-X47-4 already demonstrates for the design algorithm.

None of steps 1–4 is taken here; step 1 is not this seat's to take.

## 5. Limits

- This file makes no claim that the register leg is implemented, and no claim
  that the delivered replay leg substitutes for it. It is a different relation
  on a different culture.
- The counts in §1 are of the delivered packet at the digest above; the counts
  in §2 are the peer audit's, re-cited not re-run.
- The false-red mechanism (execution-2 §3) is named as the O claim's repair
  target; this seat does not patch the rebuild and claims no repair.
