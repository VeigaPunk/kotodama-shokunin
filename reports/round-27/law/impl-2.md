# R27-D06 — the register law, row by row: the five rows and the acts they govern

- **Seat:** R27-D06 (D axis, register law implementation 2 of 8). Round 27, loop
  3 build 3 of 4, claim **D** `register-law`. Integrator: `impl-1.md` (R27-D05).
- **Date:** 2026-10-18. Baseline `4f09c990…`; declaration commit `b95fca1`.
- **Write scope:** this file only; scratch under `.scratch/r27-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. The landed rows, verbatim from the component

`examples/culture-d4/components/13-register-law.yml`
(sha256 `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`)
declares `packet_keys: [register_law]` and five rows. Field for field:

| id | kind | act | speaker | force | design_row |
|---|---|---|---|---|---|
| RGL-01 | admissibility | a charge at the weigh-stone, a lot named as it is sealed, or an oath attested before the stamp-holder | stamp-holder, furnace-master (RK-03), mold-keeper (OR-02, component-only) | `directive-binding`; `declarative-naming` | QREG-05, QREG-07 |
| RGL-02 | exclusion | an oath | stamp-holder only — no master, no delegate | `commissive-binding refused` | QREG-06 |
| RGL-03 | asymmetry | a guest broker's charge, lot-naming or attested oath | broker, market-goer (RK-04), at market days | `directive-binding, not-rollable` | QREG-08 |
| RGL-04 | no-segment | any form in the register | any speaker admitted by RGL-01 or RGL-03 | none — sound-channel constraint | — |
| RGL-05 | era | any form in the register | any speaker admitted by RGL-01 or RGL-03 | none — dating constraint | — |

## 2. Why the clause fields are what they are

The claim's `after_required` names three clauses: **what may be said in-register**
(admissibility), **by whom** (agent), and **with what record consequences**. The
lane runner grades exactly those three (`run-validation.py`'s
`law_clause_coverage` over the rows' own text) and this seat measured them
present:

```
$ python3 reports/round-27/run-validation.py   # claim D measurement
"clauses": {"admissibility": true, "agent": true, "consequence": true}
"rows_with_universal_fields": 5, "rows_total": 5
```

- `act` states what may be said. It is prose because the acts are prose — no
  delivered record enumerates speech acts.
- `speaker` states who may say it, and it is the **sibling design's** field name
  (`design.md` §3). `holder` carries the round-26 `forms.md` §5 spelling of the
  same fact, so a reader arriving from either artifact resolves the row.
- `consequence` states what the act makes true and what it writes. This is the
  load-bearing clause for a **record** culture: an act that leaves no record is
  not an act here (`design.md` §1).
- `force` is the illocutionary value the sibling design fixes and round 26 left
  unstated. The sibling review measured its absence in the first revision of this
  component and named why it matters (`review.md` §9a): the guest asymmetry
  (`RGL-03`) is a **force** difference, not a holder difference. Revision 2 adds
  it.

## 3. RGL-04 and RGL-05 carry no design row, and that is stated

The sibling design's four acts (`QREG-05..08`) are acts performed *in* the
register. `RGL-04` (the register owns no segment) and `RGL-05` (available from
E1) are **constraints on the register**, not acts. They therefore carry
`design_row: []` and `force: none — … constraint, not a speech act`, rather than
being forced into an act row they do not belong to. Stated, not left as an empty
column a reader has to interpret.

## 4. The law binds the delivered rank rules, and says so

Three of the five rows name an in-packet institution as their authoriser, and
the component's `law_binding` block records which:

| row | authorising record | in the packet? |
|---|---|---|
| RGL-01 | `RK-03` the stamp-house | yes (`rank_rules`) |
| RGL-02 | `RK-03` + the plain oath word `L-30 gis` | yes (`rank_rules`, `lexicon`) |
| RGL-03 | `RK-04` the league charter | yes (`rank_rules`) |
| RGL-01 (`mold-keeper`) | `OR-02` | **no** — `03-orthography.yml` declares no `packet_keys`, so its `records` block never reaches the packet (sibling review `RL-4`, `LL-8`) |

The fourth is a named defect inherited from the design, not repaired here: the
office is legal in the component and invisible to every gate that reads the
packet. It is why `RGL-01`'s `speaker` marks `mold-keeper` as
`(OR-02, component-only)` inline rather than asserting it as a packet fact.

## 5. Measured

```
$ python3 tools/assemble-culture-d4.py --check
packet.d4.yml: byte-identical deterministic assembly          # exit 0
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml | grep -o 'findings_total=[0-9]*'
findings_total=12                                             # unchanged from round 22
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
summary: 20/20 legs passed
```

The law lands at **zero new holds** — the sibling design's central prediction
(`review.md` §9a: "the law lands at zero new holds, exactly as this review
predicted"), reproduced by this seat's own run.

## 6. Controls (this facet)

| # | control | result |
|---|---|---|
| C-1 | `RGL-01.force` → `no-such-force` | `findings_total=12`, identical to clean: the law has no replay leg |
| C-2 | `RGL-05` row dropped | `findings_total=12`, identical: same gap, structural mutation |
| C-2b | `RGL-01.kind` stripped | `findings_total=12`, identical |

Both mutations were run **in place** with the live packet restored
byte-for-byte afterwards (verified by `cmp`). The identical counts are the
honest result and are reported as a **gap**, not a pass: the rows are a
declaration the delivered gates cannot execute (`LL-3`, `RL-1`). The
`law_clause_coverage` leg reads the rows' text, so a row stripped of `act` or
`consequence` **would** be caught by the lane runner — the missing leg is
enforcement, not schema coverage.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
grep -c 'id: "RGL-' examples/culture-d4/packet.d4.yml
python3 -c "import json;d=json.load(open('reports/round-27/validation.json'));print(d['claims']['D']['measurement']['register_law'])"
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml | grep -o 'findings_total=[0-9]*'
sha256sum examples/culture-d4/components/13-register-law.yml
```
