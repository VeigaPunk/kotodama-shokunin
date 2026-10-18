# Round-19 coverage gaps — the C-author gap registry (R19-C11..C20)

- round: 19 (operator: loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`).
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  baseline revision `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`
  ("round-19: declare claims D/C/O").
- purpose: **the collision-avoidance list for the C entry authors.** The first
  author to land a gap writes its row here; later authors read this file before
  choosing a gap, and on collision with a row already listed they append `-b`
  to their own entry slug and say so in the entry's `- gap filled:` line.
- scope: this file claims gaps, not entries. It admits nothing, certifies no
  round, and is not canon.

## Declared gaps (slug → gap → partition → owner seat)

| slug | partition | gap it fills | seat |
|---|---|---|---|
| `label-channel-routing-verification` | verification | The partition carries the typed-label *kinds* (SKILL.md decision table) and the executable (`tools/d2-typed-labels.py`), but no entry states the **routing decision procedure** — which channel a form-bearing record's string is graded on, and what negative control proves the routing holds. | R19-C11 |
| `pre-declared-hold-set-reconciliation` | verification | No entry covers **pre-declaring an expected finding set before implementation** and reconciling the emitted set against it (declared-vs-emitted delta, disposition of each delta). | R19-C12 |
| `generated-artifact-roundtrip-verification` | verification | No entry covers **round-trip / serializer corruption verification** for generated artifacts: deterministic re-generation, `--check` byte-identity, and the class of drift a re-serialization can hide. | R19-C13 |
| `gate-battery-surface-verification` | verification | `gate-frozen-run-standard.md` covers frozen runs; no entry states what the **gate battery** actually covers (isolated mirror, originals-preserved measurement, baseline discovery) and what it does not (which gates are absent from its default roots). | R19-C14 |
| `two-reader-interop-agreement` | verification | No entry states the **interop/agreement check**: two independent readers of one artifact must agree, and how a divergence between them is dispositioned. | R19-C15 |
| `typed-label-routing-workflow` | synthesis | The synthesis partition has `glossary-registry-format.md` and `loanword-material-dating.md`, but no **design-side workflow** for routing every form-bearing record onto the correct channel *before* a gate reads it. | R19-C16 |
| `generated-artifact-lifecycle` | synthesis | No entry covers the **generated-artifact lifecycle** for a culture packet (authored components → generated packet → generated projection; never hand-edit; rebuild + check). | R19-C17 |
| `hold-set-contract-in-brief` | synthesis | No synthesis entry states the **hold-set declaration as a design contract**: the expected finding set is named in the brief before the packet exists. | R19-C18 |
| `era-material-scoped-reconciliation` | synthesis | `era-language-staging.md` stages language across eras; no entry states the **scoped era/material reconciliation** rule (resolve by declared row, never by label or by number). | R19-C19 |
| `finding-disposition-workflow` | synthesis | No synthesis entry covers turning a gate's findings into **design debt and triage** (fail/hold/note → disposition), and why a disposition is never a clearance. | R19-C20 |

## Collision log

- 2026-10-18 — first write. No prior rows; no collisions. All ten slugs above
  are claimed by R19-C11..C20 in the order listed.

## Grounding used across the ten gaps

Every row above is grounded in the same D4 surface: `examples/culture-d4/`
(`brief.md`, `ASSEMBLY.md`, `packet.d4.yml`, `typed-labels.d4.yml`,
`expected-holds.json`, `components/*.yml`), the round-18 receipts under
`reports/round-18/d4/` (`holds.md`, `determinism.md`, `manifest.md`,
`replay.md`, `gate-runs-*.md`, `interop-*.md`), and the lane tools
(`tools/d2-typed-labels.py`, `tools/gates/d4-*-check-gate.py`,
`tools/check-gate-battery.py`, `tools/replay-frozen.py`). None of it is canon.
