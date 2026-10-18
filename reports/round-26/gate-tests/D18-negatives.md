# R26-D18 — negatives: a rule that does not derive its form reads D4L-ARGOT-DERIV

- **Seat:** R26-D18 (gate+tests 2 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum`. Assignment verbatim: *"negatives (a rule that does not
  derive its form must be D4L-ARGOT-DERV)"*.
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **Write scope:** `reports/round-26/gate-tests/fixtures/**` and this fragment,
  plus gitignored scratch. No tool, gate, packet, pin or filed 8-25 byte written.
- **Canon:** NON-CANON fixtures. Every form below is a planted mutation of a
  round-17 design row or a self-invented probe; none is a claim about a language.

## 0. Verdict

**A rule that does not derive its form reads `D4L-ARGOT-DERIV`, on three
independent routes, and the leg is shown discriminating (a corrected fixture
grades clean).** The seat header's id spelling `D4L-ARGOT-DERV` is **not
implemented anywhere** — the design authority and the gate both spell it
`D4L-ARGOT-DERIV`; that one-letter variant is recorded as a delta, never
asserted as the id.

Eight fixtures, first measured at 2026-10-18T18:09Z and re-measured unchanged
after the register stratum landed at 18:19:48Z (the fixtures are self-contained,
so the packet move does not touch them; `TMPDIR=$PWD/.scratch`):

| fixture | what it plants | exit | finding id(s) |
|---|---:|---:|---|
| `n1-maximal-coda.yml` | `saalum` declared as `head2(saalumi)` — the design's own named trap (`design-language.md` §5) | 1 | `D4L-ARGOT-DERIV` |
| `n2-rule-mismatch.yml` | a packet `derivation_rules` entry (`CX-99`) whose pattern/output pair yields `mesar`, form delivered as `mesen` | 1 | `D4L-ARGOT-DERIV` |
| `n4-unknown-rule.yml` | a declared derivation naming a rule the packet does not declare (`CX-77`) | 1 | `D4L-ARGOT-RULE` |
| `n5-borrow-mismatch.yml` | a register-scoped loan `rezh` whose layer substitutions yield `res` | 1 | `D4L-ARGOT-DERIV` |
| `n6-coverage-hold.yml` | operations and register-scoped forms declared, no derivation pair delivered | 1 | `D4L-ARGOT-COVERAGE` |
| `n7-malformed.yml` | unparsable input | 2 | `D4L-ARGOT-DATA` |
| `n8-lengthen-mismatch.yml` | the register design's **own** operation: a packet `LENGTHEN` rule (double the stressed vowel, `reports/round-26/register/rules.md` §3) declared with an undoubled form | 1 | `D4L-ARGOT-DERIV` |
| `n3-positive-control.yml` | the same two shapes with the form corrected (`saalu`, `mesar`) | **0** | *none* |

The exact-id comparison is by **set**, so a fixture that emits an extra finding
fails; the fixture set is checked into
`reports/round-26/gate-tests/fixtures/` and re-run by the battery on every run.

## 1. The specific control the claim names

`n1` and `n2` are two independent routes into `D4L-ARGOT-DERIV`:

- **`n1` — a declared argot operation.** `saalum` is what `head2` yields under
  the **maximal-coda** reading of `saalumi` (`saa.lum.i`); the design fixes
  **maximal-onset** (`saa.lu.mi` → `saalu`) precisely because the two readings
  disagree on this one row. The gate emits:

  ```
  FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form N1-01 'saalum'
    (register 'quote'): declared chain 'head2' applied to 'saalumi' yields
    'saalu'; the stated inputs and rules do not yield the candidate
  ```

- **`n2` — a packet-declared pattern/output rule.** The packet declares
  `CX-99` (`^(?P<stem>.+)$` → `{stem}ar`, i.e. `mes → mesar`); the record
  delivers `mesen`. The gate replays the declared pair through the naming
  gate's budgeted matcher and emits the same id.

- **`n8` — the register design's own operation.** The landing design
  (`reports/round-26/register/rules.md` §3) adds a fourth
  `morphology.derivation_rules` entry, `LENGTHEN`
  (`^(?P<onset>[^aeiou]*)(?P<vowel>[aeiou])(?P<rest>.*)$` →
  `{onset}{vowel}{vowel}{rest}`, i.e. `tum → tuum`). N8 declares that exact rule
  and delivers `tik` for a `LENGTHEN(tik)` chain — the leg reads
  `D4L-ARGOT-DERIV` on `N8-01`, while the correctly doubled `tuum` row replays
  clean. **The design's chosen operation is therefore already graded by the leg
  the design relies on; the register landing needs no gate change** — which
  matches the design's own §5 ("the gate already replays
  `derived_from`/`derivation`; nothing to write").

All three are exit 1 with **exactly** that one id, and `n3` (the same two rows
with `saalu`/`mesar`) is exit 0 with **no** findings — so the leg discriminates
rather than being always-red.

## 2. The id spelling — recorded, not resolved by assertion

The assignment header (and `reports/round-26/claims.json:15`) spell the id
`D4L-ARGOT-DERV`. The **design authority** spells it `D4L-ARGOT-DERIV`:

- `reports/round-17/d4/design-brief.md:308` — *"a fixture whose quote form ≠
  `apply(op, base)` → FAIL, id `D4L-ARGOT-DERIV`"*
- `reports/round-17/d4/design-brief.md:456` — required control C-02, expected
  `FAIL D4L-ARGOT-DERIV`

The implemented gate (`tools/gates/argot-derivation-gate.py`) emits
`D4L-ARGOT-DERIV`; `grep -rn "D4L-ARGOT-DERV"` over `tools/` and `examples/`
returns **0** files (measured 2026-10-18). Round 25 already recorded this delta
in `reports/round-25/argot/impl-3.md:60-66` and `impl-6.md:91-93`; this seat
re-records it as a new row and asserts the **design's** spelling.

The round-26 runner takes the same position, accepting both spellings
(`reports/round-26/run-validation.py:122-126`, `ARGOT_IDS`) so a claim-text typo
cannot fail an honest artifact — but the artifact it measures must name one of
them. This seat's fixtures and receipt name `D4L-ARGOT-DERIV`.

## 3. Limits

- **The fixtures are probes, not the delivered packet.** A green run here says
  the leg rejects a planted non-derivation; it says nothing about the register
  stratum's completeness (that is D17's and the register seats' question).
- **`n6` fires on the current tree shape.** `D4L-ARGOT-COVERAGE` is the HOLD the
  leg emits when the argot relation is *declared, not delivered* — the exact
  round-25 finding. It is a fixture here, but it is also what a packet carrying
  operations and no derivation pair would read.
- **The fixtures live in `reports/`, not `tools/gates/fixtures/`.** The committed
  gate fixture (`tools/gates/fixtures/argot-derivation-gate.yml`) belongs to the
  gate's own selftest (21/21); these are the round-26 battery's, deliberately
  separate so neither pins the other.
