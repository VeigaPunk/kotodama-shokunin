# examples/culture-d4 — the D4 furnace-league drill (NON-CANON)

This directory is a **non-canon design drill**: a fourth example culture built
end-to-end through the lane's typed pipeline (round 17, loop 2 build 1 of 4).
It is **not canon and not a world-bible entry**; canon decisions belong to
lore-shokunin (`PROVINCE.md`) and no lore acceptance is claimed or implied. No real-world
community, language, craft tradition, or script is described, cited, or
approximated anywhere in it; every name, rule, form, and route is invented for
this drill. No real-language clearance, cultural permission, community
consultation, rights/attribution ruling, or ancient authenticity is claimed,
performed, or granted. Era tags E0–E3 are fixture-relative, not BCE/CE dates.

## What D4 is

A furnace-league culture: towns of smiths on a forested upland basin, working
bog-ore with charcoal; terraced valley grain and a small wool flock; the
furnace, not the field, is the civic institution. Its spine is two axes —
**FIRE** (transformation: furnace, charge, quench, ash, smoke) and **MARK**
(attestation by impression: stamp, mold-mark, count-mark, name-mark). Records
are stamped before they are written: E0 tally-stamps on ingots become a native
stamp-derived script at the E0/E1 seam.

The brief, seed parameters, spine, registry, and coupling contract are
component `01-brief` below; this file is the tree-level summary and the pointer
to the record, not a second design.

## Registry (12 components)

| # | component | packet keys | duty |
|---|---|---|---|
| 01 | `components/01-brief.yml` | `contract` | seed, spine, registry, contract, named hold set |
| 02 | `components/02-phonology.yml` | `phonology` | inventory, phonotactics, stress, allophony, sound changes |
| 03 | `components/03-orthography.yml` | `orthography` | stamp-mark script, sign inventory, orthography rules |
| 04 | `components/04-lexicon.yml` | `lexicon`, `constructions`, `layers` | seven-field lexicon and the loan layers |
| 05 | `components/05-naming.yml` | `names`, `cross_culture_review` | name slots, formation, license |
| 06 | `components/06-myth.yml` | `pantheon`, `roles`, `motifs`, `narratives` | powers, roles, narratives, motifs |
| 07 | `components/07-symbolism.yml` | `symbols` | signs with medium, audience, holder, era |
| 08 | `components/08-eras.yml` | `eras`, `era_dates`, `named_eras`, `era_records` | era tags, named eras, dates, era records |
| 09 | `components/09-costumes.yml` | `costumes`, `materials`, `cloth_sources`, `rank_rules` | garments, materials, cloth sources, rank rules |
| 10 | `components/10-ritual-calendar.yml` | `calendar`, `festivals`, `rites` | furnace calendar, festivals, rites |
| 11 | `components/11-contact-history.yml` | `contact`, `routes` | contact layers, roads, events |
| 12 | `components/12-provenance.yml` | `provenance` | evidence ledger and open questions |

## Named hold set (pre-implementation)

`01-brief.yml` `contract.hold_set_declaration` names the finding set the typed
run is expected to emit, before the packet existed: **6 holds, 0 notes,
0 fails** — `D4L-FORM-UNRESOLVED` at `GAR-01`…`GAR-06` (six garment glosses
routed off the sound-and-identity channel whose `LEX-GAR-nn` form slots stay
owed). The committed record is `expected-holds.json`; every hold is open design
debt, never a clearance.

## Provenance and reproduction

The component fragments are authored by the round-17 component seats under
`reports/round-17/d4/components/` and landed here by the round-17 integrator;
`packet.d4.yml`, `typed-labels.d4.yml`, and `packet.d4.typed.yml` are generated
artifacts — never hand-edited. `ASSEMBLY.md` records the exact commands,
digests, and observed verdicts. Round-17 design documents (including divergent
design proposals from sibling seats) live under `reports/round-17/d4/`; the
landed components, not those documents, are what this tree contains.
