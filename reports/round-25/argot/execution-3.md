# R25-D13 — argot-derivation leg, execution 3: the delivered-vs-forecast delta

- **Seat:** R25-D13 (argot execution 3 of 4), round 25, loop 3 build 1 of 4,
  claim **D** `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only; scratch under `.scratch/r25-d11/` only.
- **Canon:** NON-CANON engineering evidence.

The claim requires the delta be **written, not silently dropped**: "any forecast
element not delivered is named." This file is that record. It consumes the
forecast enumeration (`reports/round-25/argot/forecast.md`, seats R25-D01..D04)
and the delivered-state measurement (`reports/round-25/argot/current-state.md`),
and it does not re-derive either.

## 1. The forecast, and the root cause of the delta

The round-17 forecast (Δ3, `reports/round-17/d4/design-brief.md:296-310`) was
written against a **weigh-court quote-register** D4 — COUNT × QUOTE, argot loans
`AL-01..06`, owed plain doublets, `head2`/`reverse` derivations. The delivered
D4 is the **furnace-league** — FIRE × MARK
(`examples/culture-d4/components/01-brief.yml:59,79,85`; `examples/culture-d4/brief.md:15-18`).

Round 17 carried **mutually divergent design documents**, and the round-17
brief seat itself recorded the divergence without resolving it
(`design-brief.md:596-670`, the status table and the three reconciliation paths
A/B/C — "the parent's decision; this seat implements none"). Path **A** was
taken: the landed furnace-league component registry (`01-brief.yml`, FIRE × MARK)
shipped. The weigh-court culture, and with it the argot, was not built.

This is why the delta is not "an unimplemented leg on a built culture" — it is
**a whole register-scoped culture that never shipped**. Every forecast element
that depends on the register/quote surface is therefore absent *by design of the
shipped culture*, not by an oversight in the argot leg.

## 2. Element-by-element delta

Forecast ids F-1..F-8 are the enumeration in `forecast.md` §2 (from
`design-brief.md:296-310`); the neighbouring rows are `forecast.md` §4.

| # | forecast element | delivered? | delivered-side evidence |
|---|---|---|---|
| F-1 | quote forms derived from a plain base by one of two declared operations | **NOT DELIVERED** | no `derived_from`/`derivation` field anywhere (`forecast.md` §2; `current-state.md` §3); the two operations are absent (`grep -c "head2\|reverse"` over packet/components → 0, `current-state.md` §1) |
| F-2 | the two operations `head2` (first two syllables, maximal-onset) and `reverse` (string reversal) | **NOT DELIVERED** | `04-lexicon.yml` declares only CX-01/02/03 (compound + two suffixes); the design-language algorithms are not in any delivered byte (`current-state.md` §1, §4) |
| F-3 | the check fields `derived_from` + `derivation` | **NOT DELIVERED** | `grep -c "derived_from"` over packet → 0 (`current-state.md` §3); the only `derivation` tokens are `morphology.derivation_rules`/`derivation_note` |
| F-4 | a relation between **two records of the same packet** | **PARTIALLY MET — in a different form** | the delivered packet *does* carry cross-record derivation: the 4 lexicon records with `bases`+`construction` (L-45..L-48) and the 8 names with `formation` (NM-01..08). But the relation is *base → compound/suffixed form*, not *plain base → quote form*; there is no `<id>#plain` / `<id>#quote` pair and no `doublet_of` (`current-state.md` §2) |
| F-5 | every derived quote form's check passes, **zero fails** | **VACUOUSLY SATISFIED, not delivered** | trivially true: there are no derived quote forms and no leg, so no fail can exist. Not a delivery. The nearest delivered surface (base→form derivations) *is* clean — execution 1: 12/12 replay, 0 violations — but it is not the forecast's surface |
| F-6 | coverage block reports `derived_forms` / `derived_ok` counts that agree | **NOT DELIVERED** | `grep -c "derived_forms\|derived_ok"` → 0 in packet and tools (`current-state.md` §4) |
| F-7 | control: quote form ≠ `apply(op, base)` → FAIL id **`D4L-ARGOT-DERIV`** (control-only) | **DELIVERED LATE by a peer gate; absent from D4's own bytes** | as measured at 17:31Z, `D4L-ARGOT-DERIV` occurred 0 times in `examples/` and 0 times in `tools/`, 2 files under `reports/round-17/` only (`current-state.md` §5.1). **Superseding note (17:36Z):** a peer landed `tools/gates/argot-derivation-gate.py`, which now emits `D4L-ARGOT-DERIV` on four controls this seat ran (`execution-4.md` §2.1). The *delivered D4 packet* still carries no such row and no register-scoped derivation pair (`derived_pairs=0`), so F-7's element — a D4 byte carrying the id — remains undelivered; only the producer now exists |
| F-8 | required-controls battery row C-02 (the same control, restated) | **NOT DELIVERED** | same as F-7; `design-brief.md:456` is design text, not a live control |
| Δ1-class2 | register-scoped slots: a supplied, inventory-clean quote form admissible only in a quote slot; `D4L-REGISTER-UNRESOLVED` per owed plain slot | **NOT DELIVERED** | no `registers`/`doublets` key, no `register:` on a lexicon record, no `#plain`/`#quote` slot, no `slot_ref`/`doublet_of` (`current-state.md` §2); `D4L-REGISTER-UNRESOLVED` 0 files in `examples/`, 0 in `tools/` |
| Δ2 | slot cardinality: exactly one supplied form per `(owner, slot_ref)`; `doublet_of` pair fact; two forms in one slot → exit 2 `D4L-DATA` | **NOT DELIVERED** | `doublet_of` 0; `D4L-DATA` 0 files in `examples/`, 0 in `tools/` (`current-state.md` §5.1) |
| AL-01..AL-06 | the six argot loans (AL-02 three-field donor; AL-03 `ultimate: null`, held) | **NOT DELIVERED** | `AL-0` occurs once in the packet, inside `CAL-01`; the loan forms are not delivered (`current-state.md` §4.1) |
| name-side argot | eight plain bases whose **quote names** are their `reverse`s, used only in the quote register | **NOT DELIVERED** | no `quote` key on any name record; the eight quote names occur 0 times (`current-state.md` §4.1) |
| — | the 11 worked derivations (`saalumi→saalu`, `min→nim`, … `makun→nukam`) | **NOT DELIVERED** | every base/quote pair absent from the delivered lexicon (`current-state.md` §4.1; independently re-derived by `reports/round-25/audit/x47-argot-negatives-audit.py` R25-X47-1 → 11/11 reproduce, 0 delivered) |

**Delivered in its place (not a forecast element, but the surface the leg could
be built on):** the CX-01/02/03 machine-readable rule table
(`examples/culture-d4/components/04-lexicon.yml:192-196`;
`packet.d4.yml:205-226`), the 4 derived/compound lexicon records, the 8 named
`formation` records, and the naming gate's live Gate C replay leg. This is what
executions 1 and 2 exercise — it is *real* and *replayable*, and it is *not the
forecast's argot relation*.

## 3. What "not delivered" means here, precisely

Three distinct non-deliveries, named separately so none is absorbed into another:

1. **The culture did not ship.** The weigh-court/quote-register D4 was not built;
   the furnace-league D4 shipped (round-17 design-brief reconciliation path A).
   Every register/quote surface above is absent for this reason.
2. **The id was never wired.** `D4L-ARGOT-DERIV` exists only as design text; no
   engine emits it (`current-state.md` §5.1). So even the control the forecast
   named has no producer.
3. **The operation class is not representable in the live engine.** The
   lexicon-coverage audit's replay model is **concatenation only** (substitute
   `B1`…, strip `+`/`-`); a correct `reverse` derivation and a wrong one produce
   the *same* finding under it, and the correct one is a false FAIL
   (`current-state.md` §6.2, controls N-2/N-3). So "add `reverse` to
   `constructions`" would *manufacture* a red row, not implement the leg.

Item 3 is the load-bearing one for this claim's scope: implementing the
argot-derivation leg honestly requires a replay engine that carries an
**operation field with alternate operations**, which no live tool has. The leg
this seat could deliver is the one that *is* representable — the stated
`pattern`/`output` replay over the delivered derivation surface (executions 1
and 2) — and the register half is named as not-delivered rather than faked.

## 4. Independent corroboration of the delta

- `reports/round-25/audit/x47-argot-negatives-audit.py` R25-X47-2 (run
  2026-10-18T17:31Z): `derived_from_tokens: 0, derivation_tokens: 0, pairs: 0,
  argot_deriv_rows: 0, d4l_codes: ["D4L-FORM-UNRESOLVED"]` — the delivered D4
  carries exactly one `D4L-*` id, and it is not the argot one.
- `reports/round-19/knowledge/analyst-3.md:87-105,152-158` (the first post-hoc
  read, a prior round): "no delivered D4 byte carries a `D4L-ARGOT-DERIV` row or
  an `ARGOT` token"; §6 puts the argot derivations under "Forecast (mark
  `(to-verify)`)". This seat re-measured the same claim and agrees.
- `reports/round-25/argot/delta.md` (R25-D03, the peer delta file, landed
  2026-10-18T17:30Z) disposes the same F-1..F-8 element set independently and
  reaches the same verdict on every row. Its sharper phrasing of two rows is
  adopted here: **F-5 is "vacuously satisfied", not "not delivered"** (there is
  no form and no leg, so no fail can exist), and the delta is a **schema +
  engine + gate** delta, not a gate delta alone — the delivered schema has no
  field for a two-record derivation relation and the delivered `constructions`
  registry has no operation dimension.

## 5. Limits

- This file reports the delta; it does not choose the reconciliation path. The
  round-17 brief seat already named the choice as the parent's
  (`design-brief.md:653-663`), and this seat implements none of A/B/C.
- The delta is measured against the delivered tree at the digests in
  `current-state.md` §0 and this seat's `execution-1.md` §2; a later edit to the
  packet or a landed register surface is a re-read event.
