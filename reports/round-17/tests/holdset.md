# R17-D29 — hold set: the named set is carried and matches the legacy flag set exactly; the typed-run equality is blocked

- round: 17 (operator loop 2 of 3, build round 1 of 4) · shard: **D29** (tests ×4,
  claim D `culture-d4-assembly`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "D4 R17-D26..D29 (tests x4): determinism (two assemblies
  byte-identical); replay-frozen over D4 artifacts; interop (assemble-d2/d3
  --check + battery + craft green); gate findings == named hold set exactly.
  reports/round-17/tests/{determinism,replay,interop,holdset}.md."
- date: 2026-10-18. Baseline revision
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; working-tree HEAD `9b49a4a`.
- canon: NON-CANON engineering evidence. A hold set is open design debt, never a
  clearance, and nothing here is a canon record.
- writes: **this file only** plus gitignored scratch under `.scratch/r17-tests/`
  (receipt: `.scratch/r17-tests/holdset/receipt.json`). No tool, gate, packet,
  component or earlier-round byte is edited. No commit, no push.
- **status: measured, with one named gap.** The delivered named hold set is
  carried, its declared counts are true of its own rows, and it corresponds
  **exactly** to the six records the legacy gate flags — but the strict
  typed-run equality ("gate findings == named hold set") is **not evaluable**
  because no typed artifact exists (§4). The divergence between the three
  competing namings is reported, not repaired (§5).

## 1. The named hold set (delivered, pre-implementation)

`examples/culture-d4/packet.d4.yml:121-159` carries
`contract.hold_set_declaration`, the landed component registry's declaration
(source: `examples/culture-d4/components/01-brief.yml:195-205`, seat R17-D05),
"named at 2026-10-18, before implementation of the packet" (line 122). Observed
by this shard (2026-10-18, reader = the costume gate's parser via
`runpy.run_path`):

| field | observed |
|---|---|
| rows | 6 — `D4L-FORM-UNRESOLVED` hold at `GAR-01` … `GAR-06` |
| declared counts (`counts:`, line 155) | `{hold: 6, note: 0, fail: 0}` |
| counts observed from the rows | `{hold: 6, note: 0, fail: 0}` — equal |
| artifact target (line 123) | `examples/culture-d4/expected-holds.json` (schema `kotodama-typed-pipeline-holds-v1`) |
| reason per row | `label_id LEX-GAR-0n has no supplied native/borrowed form` — the garment gloss is a translated label, off-channel |

The declared counts are true of the declared rows; the target artifact
(`expected-holds.json`) **has not landed** (sweep 2026-10-18:
`ls examples/culture-d4/` → `ASSEMBLY.md brief.md components packet.d4.yml
README.md`).

## 2. The gate finding set over the same packet (legacy run)

Five legacy culture gates over `examples/culture-d4/packet.d4.yml` (82635 bytes,
sha256 `2776d85c…335d72`), 2026-10-18, `TMPDIR=$PWD/.scratch`: **9 findings** —
naming gate exit 1 with 8, phonology exit 1 with 1, costume/lexicon/myth exit 0
with 0 each. The naming gate's `PHON-INVENTORY` lines name exactly
`GAR-01`…`GAR-06`, one per gloss, each quoting the English gloss as a surface
form (`FINDING PHON-INVENTORY: FAIL — name GAR-0n '<gloss>': symbol /…/ … is
not in the declared inventory`).

## 3. Correspondence (measured, both directions)

| check | observed |
|---|---|
| named `where` keys | `GAR-01 … GAR-06` |
| records named by a legacy finding | `GAR-01 … GAR-06` |
| bijection | **true** — `named_without_legacy_finding = []` |
| legacy findings outside the named set | exactly 2: `NAME-NEAR` (REVIEW — `NM-05`/`PAN-01` one edit apart) and `CROSS-HOLD` (HOLD — no bounded cross-cultural review; no clearance claimed) |

Reading: the named set is the six form-owed records the legacy run already
flags; the two remaining legacy findings name entities and clearance, not form
slots, so they are correctly outside the set. This is a **correspondence**
between the named set and the legacy flag set — it is *not* the typed-run
equality, and it is not presented as one.

## 4. The typed-run equality leg: not evaluable (named gap)

The strict leg — the typed packet's emitted finding set keyed
`(id, severity, where)` equal to the named set in both directions with counts and
details pinned (`reports/round-17/scope.md:105-109`) — needs a typed packet, and
none exists. Measured here, 2026-10-18:

- `ls examples/culture-d4/` → no `packet.d4.typed.yml`, no `typed-labels.d4.yml`,
  no `expected-holds.json`;
- `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json`
  → **exit 2**, stderr `d2-typed-labels error: packet.eras: expected a non-empty
  list of era tags` (stable diagnostic, no traceback, no stdout) — the projector
  family is D2-bound, as `reports/round-17/d4/typed-support-1.md` §4 measured
  before the packet existed;
- `python3 reports/round-17/run-validation.py --check` (07:04 local, read-only)
  → claim D fails on exactly three artifacts: `typed`, `projection`, `expected`;
  claims C and O pass.

So the answer to "gate findings == named hold set exactly" is: **exactly** holds
for the named-set ↔ legacy-flag bijection (§3), and **could not be evaluated**
for the typed run. The blocking cause is another seat's recorded finding
(`reports/round-17/d4/typed-run.md` §0), reported here with its own receipt, not
absorbed and not repaired.

## 5. Divergence reported, not absorbed

Three mutually inconsistent hold-set namings exist in the round-17 tree; the
parent must reconcile them:

| source | rows | counts |
|---|---|---|
| `reports/round-17/d4/design-brief.md:389` (§7.1, seat R17-D01) | `GD-01..06`, `AL-01#plain..06#plain`, `AL-03`, `RG-02`, `RG-05#a\|RG-07#a`, `RG-06#a\|RG-09#a`, `SM-03`, `QN-01` + note `RG-08#a\|RG-08#b` | 18 holds / 1 note / 0 fails |
| `reports/round-17/d4/expected-holds.fragment.json` (seat R17-D19, amendment A-19-1) | same family with the `D4L-NATIVE` row dropped | 17 holds / 1 note / 0 fails |
| landed registry `01-brief.yml:195-205` → packet `contract.hold_set_declaration` | `D4L-FORM-UNRESOLVED` `GAR-01..06` | 6 holds / 0 notes / 0 fails |

This shard tests against the **landed registry's** declaration, because it is the
pre-implementation record carried by the delivered packet for the delivered
components (and `examples/culture-d4/ASSEMBLY.md:56-60` reports the same
divergence). Which naming is authoritative for the freeze is a parent/lore
decision; the `GAR-*` ids belong to the landed furnace-league components, while
the `GD/AL/RG/SM/QN` ids belong to the weigh-court design family — a set keyed on
one family's ids cannot be emitted by the other family's packet.

## 6. Limits

- Equality is claimed **only** for the named-set ↔ legacy-flag bijection, with
  the exact commands above; the typed-run equality is explicitly unevaluated.
- Detail strings are compared only where both sides carry one; the declared rows
  carry `reason` prose, the gate lines carry their own prose, and no
  detail-for-detail identity between the two is claimed.
- Nothing here certifies the culture, the glosses, or the hold severities as
  correct design; severities are the design's own, and a hold is open debt.

## 7. Reproduce

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r17-tests/holdset-receipt.py     # writes .scratch/r17-tests/holdset/receipt.json
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | grep '^FINDING'
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json; echo "exit=$?"   # exit 2, blocked
```
