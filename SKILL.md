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

## Using the evidence

Read each entry's appended errata before using earlier tables. Source rechecks
are claim-specific: `corpus/lessons/supplement-opencode-1/sources/` records
supported, contradicted and unresolved claims with passage and access limits.
A catalogue record establishes catalogue metadata, not the unread book's
contents. A disappearing uncertainty marker is not a verified claim.

| Finding or observation | Response | Evidence |
|---|---|---|
| `A-NEUTRAL` REVIEW | Keep the contextual reanalysis and witnesses; do not call a typological warning a linguistic impossibility | `reports/supplement-opencode-1/21-phonology-review.md` |
| English garment labels fail the D2 phoneme inventory | Separate translated labels from native forms; missing native forms remain a gap, not cleared names | `reports/supplement-opencode-1/22-label-representation.md` |
| A name violates the declared coda rule | Repair the derivation in the owner ledger and propagate actual references, preserving the rejected form as historical evidence | `reports/supplement-opencode-1/04-name-correction.md` |
| A clean myth/costume verdict with omitted ledgers | Report unexercised checks; a clean supplied subset does not establish coverage or authenticity | `reports/supplement-opencode-1/23-myth-coverage.md`, `24-costume-coverage.md` |
| `CROSS-HOLD` or missing lore receipt | Retain the hold; author-side tests do not supply cultural clearance or canon authority | `reports/supplement-opencode-1/25-handoff-boundary.md` |
| Frozen replay exits 0 with recorded findings | The red verdict reproduced; the culture did not become clean | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` |

## Gates and probes

Normal gate runs map 0 to clean, 1 to findings and 2 to could-not-evaluate.
`provenance-audit` reads corpus entries; `handoff-packet-check` reads the
Markdown handoff envelope; the other five read culture packets. The seven
legacy selftests pass, but five regenerate their fixture files in place
(phonology, lexicon, myth, costume, provenance). Run that battery in an
isolated repo export; byte equality after a run does not prove no writes.
See `reports/supplement-opencode-1/29-local-boundaries.md`.

The replay tool validates SHA-256 pins and executes snapshots, never the
manifest command string. Its exit 0 means reproduction, including expected
red verdicts; 1 means mismatch and 2 means could-not-evaluate, including
`snapshot_tampered`. The round-3 TSV recording is replayable; this does not
retrofit the protocol's separate per-gate `expected.json` layout. Round-4
output files alone remain unpinned legacy evidence.

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| phonology-sanity-gate | gate | `python3 tools/gates/phonology-sanity-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/phonology-sanity-gate.{yml,expected} | selftest rewrites own fixtures | kotodama-shokunin |
| lexicon-coverage-audit | gate | `python3 tools/gates/lexicon-coverage-audit.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/lexicon-coverage-audit.{yml,expected} | selftest rewrites own fixtures | kotodama-shokunin |
| myth-consistency-gate | gate | `python3 tools/gates/myth-consistency-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/myth-consistency-gate.{yml,expected} | selftest rewrites own fixtures | kotodama-shokunin |
| costume-era-consistency-gate | gate | `python3 tools/gates/costume-era-consistency-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/costume-era-consistency-gate.{yml,expected} | selftest rewrites own fixtures | kotodama-shokunin |
| naming-collision-gate | gate | `python3 tools/gates/naming-collision-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` | tools/gates/fixtures/naming-collision-gate.{yml,expected} | read-only | kotodama-shokunin |
| provenance-audit | gate | `python3 tools/gates/provenance-audit.py <corpus-paths>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/provenance/ | selftest rewrites own fixtures | kotodama-shokunin |
| handoff-packet-check | gate | `python3 tools/gates/handoff-packet-check.py <packet.md>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` | tools/gates/fixtures/handoff-packet-check.{md,expected} | read-only | kotodama-shokunin |
| frozen-replay | gate | `python3 tools/replay-frozen.py <MANIFEST.tsv>` | 0 recorded verdict reproduced / 1 mismatch / 2 could-not-evaluate | `--selftest` | manifest gate/input/output SHA-256 pins; selftest constants in script | auto-cleaned scratch only | kotodama-shokunin |
| uncertainty-inventory | probe | `python3 tools/source-audit-inventory.py --json` | 0 inventory produced, not scholarship verified / 2 could-not-evaluate | `--selftest` | exact-count fixture constants in script | read-only; selftest scratch | kotodama-shokunin |
| D2 assembly drift | gate | `python3 tools/assemble-d2.py --check` | 0 byte-identical / 1 drift / 2 could-not-evaluate | `--selftest` | committed packet, component hashes and synthetic controls in script | default mode regenerates packet; check read-only; selftest scratch | kotodama-shokunin |
| contrastive craft example | gate (bounded example) | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 checks pass / 1 findings / 2 could-not-evaluate for declared input errors | `--selftest` (committed example plus isolated subprocess controls; foreign cwd supported) | committed exercise and tamper/CLI expectations in script | read-only, including optional `--report <existing-report.md>` | kotodama-shokunin |
| isolated legacy selftest battery | gate | `python3 tools/check-gate-battery.py` | 0 seven selftests pass / 1 recognized selftest failure / 2 could-not-evaluate | `--selftest` (isolated synthetic children) | fixed seven-gate list and control expectations in script | disposable copied scripts/fixtures; optional retained mirror only when requested | kotodama-shokunin |

The contrastive checker is example-specific, not a general culture validator.
Its subprocess controls complement the ten domain mutations and a real positive
example run; they do not prove arbitrary nested schemas correct. `--counts`
returns the exercise's declared audit-count block after checks, not a new
independent source inventory. Its embedded historical counting-command string
points to ignored scratch and is not an executable instruction; use the public
entry command above. The LAW-ORDER early-return coverage limitation remains
recorded in `reports/round-5/15-cli-review.md`.

The battery runs trusted repo scripts in a copied working directory; it is not
an operating-system sandbox. Byte preservation does not prove no writes took
place. Copying contains the five fixture-writing legacy selftests but does not
repair their independent-expected-value or parser-coverage conformance debts.
Round-scoped acceptance is re-runnable with
`python3 reports/round-5/run-validation.py`; it records the two declared claims
and writes its own validation receipt. It is an orchestration check, not a new
general culture or scholarship-certification gate.

## Source-to-system constraints — round 5

| Retrieved evidence | Worldbuilding decision | Scope and pointer |
|---|---|---|
| Radiocarbon ranges change with bark-paper cleaning protocol | Separate support manufacture, painting, later use and depicted dress before assigning an era | Publisher abstract for meso-13; `corpus/lessons/round-5-sources/08.json`, `reports/round-5/parent-source-spotchecks.json` |
| Lowie gives borrowed kin terms not tied to a social institution | Borrowed relationship words alone do not establish marriage law, descent or a dowry-transfer mechanism | Lowie Chapter V passage re-fetched in parent spotchecks; combined KIN-A07/A08 residuals stay unresolved |
| A smaller avoidance vocabulary can express the same content | Model many-to-one paraphrase and register-triggered use, not one native synonym for every ordinary word | Haviland's Dixon quotation, SR-REG-07; parent spotchecks distinguish secondary quotation from unread primary pages |
| An earlier thesis supports parts of a later-book attribution | Carry version and passage scope into the design source ledger; do not merge editions into one verified claim | TIB-A12/A16 in `reports/round-5/parent-reconciliation.json` |
| A venue record corrects a phonetics citation | Repair the bibliography without treating that correction as support for an era-to-anatomy causal rule | PHON-A11 and appended erratum in `corpus/knowledge/linguistics/phonetics-phonology.md` |

## Source-to-system constraints — round 6

| Retrieved evidence | Worldbuilding decision | Scope and pointer |
|---|---|---|
| UT Lesson 2 spells IṢ-BAT as an Akkadogram but gives the Hittite reading ēpta | Store written form, reading language, copy horizon and cult provenance separately; a borrowed sign does not determine spoken language or deity genealogy | R6-05-A, parent P04; `reports/round-6/parent-reconciliation.json` keeps Hattic affiliation legs partial |
| Louvre E 12026 is catalogued as pleated linen before the New Kingdom | Reject an exclusively New Kingdom pleating date-marker for this object; require a separate pattern/technique witness before reconstructing its cut | R6-03-B, parent P02; museum technical fields and excavation-context attribution, not independent re-dating |
| Gobhila II.8.8 names ten nights, a hundred nights or one year; §14 has a translator's emendation | Model discrete school-specific timing options and keep grammatical labels edition-bound; do not implement an arbitrary “any time after ten nights” rule | R6-13-A, parent P03; exact capture and appended `india-vedic.md` erratum; Sanskrit and parallel schools unread |
| Śatapatha III.2.1 spreads skins on the ground but attaches a horn to a garment | Give ritual surfaces and worn attachments separate slots; attach school variants to their reported witnesses instead of merging a universal cloak | R6-13-B, parent P01; Kāṇva detail is Eggeling's footnote report, not an independently read recension |
| ARTA 2007.001 p. 9 describes a practical Old Persian administrative isolate and limits generalization | Allow an attested exception to a display-only register rule without turning it into general everyday usage; distinguish royal display, transaction and household language | R6-09-A, parent P05; appended `persia-achaemenid.md` erratum; Behistun cross-version and Hallock legs remain partial |

Re-run this round's receipt/count/preservation checks with
`python3 reports/round-6/run-validation.py`. The five parent readings are
separate from the twenty qualifying worker main passages; neither count
certifies whole cultures, ancient pronunciation or cultural permission.
