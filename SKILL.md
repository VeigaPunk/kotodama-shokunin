---
name: kotodama-shokunin
description: "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems, era staging, costume/material-culture lexicon, and the coupling between them, feeding the world bible. Triggers: 'design a language', 'conlang', 'culture for this world', 'mythology of', 'symbolism of', 'naming system', 'costume/dress terms', 'era language stages', 'word for this concept'. Anti-trigger: NOT world-bible canon recording or consistency verification (lore-shokunin), NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin), NOT real-world rights/attribution rulings. Rank: shonen."
---

# kotodama-shokunin — linguistic-cultural systems (言霊)

Domain: the generative craft that connects languages, cultures, myths,
symbolisms, and eras to their linguistics and costumes for a fictional
world — and hands the resulting systems to the world bible. 言霊
(kotodama, "word-spirit") names the core premise: a culture's language is
not decoration on its world; it is evidence of it. Myth shapes vocabulary,
era shapes register, costume carries a lexicon, and symbols fossilize into
words.

This repo is the craft's home. The world bible itself — entities, relations,
timeline, canon consistency — belongs to lore-shokunin; this lane supplies
languages and cultural systems to it, never edits it.

## Decision table

| Intent | Correct surface | Never | Expected output |
|---|---|---|---|
| Design a language for a culture | conlang-methodology → phonology/typology → lexicon by semantic field → pragmatics | starting from a cipher of English with no culture brief | a language sketch tied to the culture brief |
| Give a culture a mythology | comparative frameworks → creation/hero/trickster taxonomies → symbolism synthesis | pasting a real-world pantheon with renamed gods | a mythic system with internal logic, tied to language |
| Name entities (people, places, gods, items) | naming-systems → phonotactics + morphology of the naming language | unpronounceable or collision-prone names with no derivational logic | names with etymologies and a derivation pipeline |
| Stage language across eras | era-language-staging → historical-linguistics (sound change, grammaticalization) | one static language across millennia | period registers / daughter languages with change laws |
| Dress a culture | dress-through-eras + costume-semiotics → garment lexicon (crosslinguistic) | costume with no rank/rite/era semantics | costume system + its terminology + signaling table |
| Check a world hangs together | consistency-verification-checklist (synthesis) | silently resolving contradictions into canon | a findings list; canon rulings go to lore |

## Error patterns

| Observation | Reading |
|---|---|
| language is a relex of the author's native language | the culture brief never reached the lexicon; rebuild from semantic fields |
| every culture shares one symbolic color code | cross-cultural variance ignored; check color-symbolism variance table |
| static language across deep time | missing diachronic staging; apply sound-change and grammaticalization paths |
| costume described with modern garment words | era/register lexicon mismatch; derive terms from textile technology and cut |
| names with no derivational morphology | naming-systems pipeline skipped; names should carry etymology |
| myth that explains nothing in daily life | myth is detached from ritual, calendar, and taboo; re-couple via ritual-liminality |

## Boundaries (hard)

- **Refuses canon authority.** Recording what IS true in the world, and
  consistency verification of the world bible, is lore-shokunin. This lane
  generates systems and hands them off; it never edits the world bible or
  a sibling repo.
- **Refuses real-world rights/attribution rulings** on reference works
  (attribution, rights, training permission stay distinct questions).
- **Refuses game mechanics** (game-dev-2d/3d) and **publishing** (kake).
- **Refuses general research method** — that is chousa-shokunin; this lane
  consumes cited sources, it does not own the method.
- Out-of-province evidence → report, never absorb.

## Checklist (executable)

- [ ] Every language system cites its typological basis (which real
      language family it draws on and why).
- [ ] Every mythic/symbolic claim names its framework and its calibration
      status (mainstream / contested / discredited — see
      synthesis/source-discipline-calibration.md).
- [ ] Every costume/era claim couples to a term, a material, and a rule of
      who may wear it.
- [ ] Every handoff to the world bible names the recipient (lore) and the
      open questions; canon decisions are never made here.

## Corpus map

- `corpus/knowledge/linguistics/` — the language side: phonology through
  pragmatics, historical linguistics, writing, naming, contact, registers.
- `corpus/knowledge/myth-symbol/` — the mythic side: comparative frameworks,
  creation/hero/trickster taxonomies, cosmology, color/animal/number/celestial
  symbolism, ritual, folktale indexing.
- `corpus/knowledge/culture-material/` — the material side: dress through
  eras, costume semiotics, textiles, food, architecture, trade, calendars,
  craft, music, adornment.
- `corpus/knowledge/synthesis/` — the coupling (THE NICHE): decision
  tables, matrices, pipelines, the lore handoff contract, the worked
  example, source discipline.
- `corpus/knowledge/verification/` — the honesty layer: gate
  specifications, citation/provenance formats, the calibration registry,
  to-verify triage, real-world-inspiration boundaries.
- `corpus/knowledge/civilizations/` — 92 earlier-civilization bases, each
  coupling that tradition's language, writing, myth, symbols, era model,
  costume, and naming, with provenance cautions.

## Gates

Registry per the fleet gate standard (fleet `PROTOCOL.md` §Gate
standard). Common interface: exit 0 clean / 1 findings / 2
could-not-evaluate; `--selftest` runs committed fixtures with planted
violations; input is a culture packet (schema in
`corpus/knowledge/verification/`); corpus reads are read-only. All
selftests green at round-1 close (2026-10-17).

| name | kind | entry command | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|
| phonology-sanity-gate | gate | `python3 tools/gates/phonology-sanity-gate.py <packet.yml>` | `--selftest` | tools/gates/fixtures/phonology-sanity-gate.{yml,expected} | none outside report | kotodama-shokunin |
| lexicon-coverage-audit | gate | `python3 tools/gates/lexicon-coverage-audit.py <packet.yml>` | `--selftest` | tools/gates/fixtures/lexicon-coverage-audit.{yml,expected} | none outside report | kotodama-shokunin |
| myth-consistency-gate | gate | `python3 tools/gates/myth-consistency-gate.py <packet.yml>` | `--selftest` | tools/gates/fixtures/myth-consistency-gate.{yml,expected} | none outside report | kotodama-shokunin |
| costume-era-consistency-gate | gate | `python3 tools/gates/costume-era-consistency-gate.py <packet.yml>` | `--selftest` | tools/gates/fixtures/costume-era-consistency-gate.{yml,expected} | none outside report | kotodama-shokunin |
| naming-collision-gate | gate | `python3 tools/gates/naming-collision-gate.py <packet.yml>` | `--selftest` | tools/gates/fixtures/naming-collision-gate.{yml,expected} | none outside report | kotodama-shokunin |
| provenance-audit | gate | `python3 tools/gates/provenance-audit.py <corpus-files…>` | `--selftest` | tools/gates/fixtures/provenance/ | none outside report | kotodama-shokunin |
