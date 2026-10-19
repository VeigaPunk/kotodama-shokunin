- Seat: P01 | planner | claim C | date 2026-10-19 | baseline 4a7aede

# Claim C execution plan — ten sourced entries across the two thinnest partitions

Scope: claim C as declared in `reports/round-35/claims.json` (six culture-material
18 → 24, four myth-symbol 19 → 23, total 201 → 211). The plan is built from live
bytes at lane HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`git rev-parse
HEAD`), from the two C scouts, and from this seat's own re-runs of every decisive
command. **K01 and K02 were absent at seat start** (no `reports/round-35/scout/`
directory existed); they landed during this seat's run and have now been read and
reconciled — §0.6 records exactly what changed and what was adopted. Everything
below is a plan; **this seat wrote no tree bytes outside this file**.

## 0. Load-bearing findings (things the C block must not build on wrongly)

0.1 **The declared frontmatter field name `scope` does not exist in the live
corpus.** This seat's count (`grep -rl "^- $f:" corpus/knowledge --include='*.md'`
for `topic sources couples verified-at recheck source scope`) → `201 201 201 201
201 134 0`. K02 §2.3 re-measured head-block-scoped: `scope` **0/201**,
`source` (singular) 131/201, `verified-at`/`recheck` 198/201, and it resolves the
claim's "4/4 or documented 3/4" reading: the house profile is the five fields
`topic / sources / couples / verified-at / recheck` plus a `- gap:` head field
(2/201 live exemplars), and "scope-bearing" is a property of the `verified-at`
line (`reports/round-10/coverage/review-C04.md:19`). **P01 pins the bar here:**
new entries carry the five fields + `- gap:`; the validator (S04/O08) must not
require a literal `- scope:`. The three-file tail deviation
(`verification/citation-format-and-source-registry.md`,
`myth-consistency-gate.md`, `provenance-audit-ledger-format.md` — K01 §1.3, K02
§2.3/D6) is the documented pre-existing class, not a new defect.

0.2 **The partition-specific `source:` ruling (K02 §2.3, this seat's count).**
`- source:` (singular) is myth-symbol convention **19/19** and culture-material
convention **0/18**. Requiring it of culture-material would fail all six new
culture-material entries at birth. Ruling: myth-symbol drafts carry it; the six
culture-material drafts must not be failed for its absence (they may carry it —
this seat counted 134 files corpus-wide with it anywhere, vs K02's 131
head-block-scoped; the 3-file delta is the documented verification class above).

0.3 **Census reproduced three ways, so the before-numbers stand.** This seat:
`for p in linguistics myth-symbol culture-material synthesis verification
civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → `21 19 18 29 20 94`;
`ls corpus/knowledge/*/*.md | wc -l` → `201`. K01 §1.1–1.2 reproduces the same
vector and cross-checks with `tools/source-audit-inventory.py --json --summary`
→ `totals.files 201`, `totals.lines 36395`. K02 §4.4 reproduces both again and
adds the README reading (rows 201 / files 201, footer clean, `readme_sha256
053966a2147e5e71…`). After-landing requirement: culture-material 24, myth-symbol
23, total 211.

0.4 **The README is a five-part artifact, and the delta arithmetic is fixed.**
`corpus/README.md:147` `## myth-symbol/ (19)`; `:169` `## culture-material/ (18)`;
`:469` `Total knowledge entries: 201.`; `:471-473` the dated counts footer with
vector `21/19/18/29/20/94`; plus a newest-first revision block at `:3`
(revision 1.9). K02 §4.2 gives the exact anchors and the after-state
(`(23)` / `(24)` / 211 / `21/23/24/29/20/94`, footer re-dated, a fourth dated
index re-measure line). Row text must be the entry's own `- topic:` text
byte-equal, continuation lines space-joined (the revision 1.5 repair,
`corpus/README.md:69-93`; K01 §1.4 rule 1; K02 §4.1). Section order is fixed
`linguistics, myth-symbol, culture-material, synthesis, verification,
civilizations` and the footer vector is compared in that order (K02 §4.2/§4.3).
K02 §4.3 also states the limit: **the round-28 sweep has no row-order leg** —
row order is convention-only; if round 35 wants it enforced that is a new
control, stated as such.

0.5 **The gap-declaration form is pinned by the round-10 checker's actual
regexes.** K01 §1.5, from `reports/round-10/coverage/audit-filler.md:104-115`:
the filed runner's gap leg accepted only (a) a `gap …:` clause with
*filled/addressed/served* or a bare colon, or (b) a heading containing "gap" —
and it **false-failed `plant-symbolism.md`** because the gap was named in prose
under a heading without the word "gap". Draft rule for C01–C10 (belt-and-braces):
header `- gap: <domain> absent from <partition> … — this entry fills it` **and** a
`## 1.` section whose heading contains the word "gap" (the
`vessel-container-lexicon.md:9` form). K02 §2.1 gives the round-10 legs
(`reports/round-10/run-validation.py:349-377`) and §5 the audit recipe; the bar
for this round is **the round-10 legs applied to the ten new entries**, not
`reports/round-19/audit/entry-audit.py` (K02 §2.2: that instrument is red by
construction on this corpus — `quality_bar 15/201`, `gap_named 27/201`).

0.6 **Reconciliation with K01/K02 (what changed when they landed).** K01 §2.5
recommended the allocation below; this seat re-ran the decisive sweeps with
bounded patterns and its own topic-owner test, and **adopts K01's 6 + 4**:
agriculture, pastoralism, extraction, medicine, fuel/lighting/water, funerary;
afterlife/eschatology, purity/pollution, spirit/demon taxonomy,
pilgrimage/sacred geography. Corroboration and one correction: this seat's
bounded owner tests reproduce the zero-owner readings (pastoralism 0, extraction
0, aromatics 0, magic 0, sacred-kingship 0, bathing 0) and the partial ones
(purity 1 = `color-symbolism`; spirit classes 4, all incidental or
civilization-base); the loose-pattern runs that returned high owner counts
(e.g. `games` 15, `timekeeping` 5) were **substring pollution** (`play` in
display, `grave` in engrave, `possession` = inalienable possessions,
`onsen` in consensus) and are reported here as method evidence, not as owners.
**What this plan drops from its own first draft** — timekeeping-instruments,
games-and-play, incense-aromatics, magic-and-witchcraft, sacred-kingship,
bathing-hygiene — is recorded in §7 as evidence-carrying alternates with swap
rules, not deleted. K01's CM-9 note on bathing (0 keyword hits, "lowest-yield")
applies to it as an alternate; the same critique is why this plan does not lead
with zero-demand topics.

## 1. Census at HEAD — the plan's baseline

| partition | files now | after | delta |
|---|---|---|---|
| culture-material | 18 | 24 | +6 |
| myth-symbol | 19 | 23 | +4 |
| linguistics | 21 | 21 | — |
| synthesis | 29 | 29 | — |
| verification | 20 | 20 | — |
| civilizations | 94 | 94 | — |
| **total** | **201** | **211** | **+10** |

Commands: `for p in linguistics myth-symbol culture-material synthesis
verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` →
`21 19 18 29 20 94`; `python3 tools/source-audit-inventory.py --json --summary
--root corpus/knowledge` → `totals.files 201` (K01 §1.2, K02 §4.4 corroborate).

## 2. Entry-shape contract (what C01–C10 must produce)

In order of authority:

1. `corpus/QUALITY.md` items 1–5 (provenance; calibration labels; `- couples:`
   naming the systems it connects; usability — tables/checklists/worked
   examples, no essays; canon hygiene — ends at the handoff).
2. The header block, in filed order (K01 §3.1): `# H1 title — subtitle`;
   `- gap:` (finding 0.5 form); `- topic:` (one long line, the byte-source of
   the README row); `- sources:` (nested `  - ` bullets; web entries carry
   `(fetched YYYY-MM-DD)`; tertiary relays declared as such); `- couples:`
   ending with the handoff-target sentence naming lore-shokunin and disclaiming
   canon; `- source:` **only for myth-symbol** (finding 0.2); `- verified-at:`
   as a prose record (what was re-checked live, with what, what was *not*
   re-consulted, access failures); `- recheck:` naming the trigger.
3. A `## 1.` section whose heading contains "gap" (finding 0.5), a
   decision-record section with stable ids and an evidence column
   (K01 §3.3: `DR-TR-01`… / `DR-1`… / `D1`… forms), a calibration section for
   contested frameworks, and a canon-boundary/handoff note (K01 §3.5).
4. Sources resolve: cited repo paths exist (K01 §2.1: one dangling pointer
   already exists corpus-wide — `linguistics/phonology-sanity.md`, referenced
   from two files — **new entries must not create a second**); cited commands
   re-run; URLs carry an access attempt. Unresolvable sources are marked
   `(to-verify)` in-file with the reason — never invented (`AGENTS.md`;
   `corpus/QUALITY.md` item 1).
5. No cross-domain bleed: no promotion/canon/clearance/closure language outside
   negations; canon stays lore-shokunin's.
6. Section band 7–14 `##` sections (K01 §1.3), line band ≥100 lines for these
   partitions (min live: 103), current house scale 36–43 KB
   (`wc -c`: `plant-symbolism.md 43150`, `vessel-container-lexicon.md 43056`,
   `register-lexicon-ceilings.md 36139`).

## 3. The ten topics

Selection: K01 §2.3/§2.4 ranked candidates by mention count with topic-owners
zero or civilization-only; this seat re-ran the sweeps (bounded) and the
topic-owner test. `K01 mentions/owners` are K01's readings (its §2.3/§2.4);
`P01 re-run` is this seat's bounded pattern. Every author re-runs their own
row's sweep and cites their own counts in `- gap:` and `## 1.`.

| seat | slug | partition | K01 mentions/owners | P01 re-run (bounded) |
|---|---|---|---|---|
| C01 | `agriculture-subsistence-systems` | culture-material | 21 / 0 | 65 / 0 |
| C02 | `pastoralism-husbandry-lexicon` | culture-material | 23 / 0 | 36 / 0 |
| C03 | `extractive-industry-lexicon` | culture-material | 17 / 0 | 22 / 0 (one loose hit, `real-world-inspiration-boundaries`) |
| C04 | `medicine-healing-material` | culture-material | 13 / 0 | 38 / 0 (`materia medica\|pharmacopoeia\|humoral\|bonesetter` → **0 files**) |
| C05 | `fuel-lighting-water-utilities` | culture-material | 11 / 0 | 26 / 0 (`\bcandle` → 0, `tallow\|rushlight` → 0, `lamps?` → 4) |
| C06 | `funerary-material-culture` | culture-material | 40 / 4 (2 civs + 2 extension rows) | 95 / 4 (same class) |
| C07 | `afterlife-eschatology-symbolism` | myth-symbol | 39 / 2 civs, 0 in-partition | 39 / 1 civ (`china-han`) |
| C08 | `purity-pollution-codes` | myth-symbol | 42 / 1 (`color-symbolism`, partial) | 42 / 1 (same) |
| C09 | `spirit-demon-taxonomy` | myth-symbol | 40 / 1 civ | 159 / 4 (all incidental/civ) |
| C10 | `pilgrimage-sacred-geography` | myth-symbol | 28 / 2 civs, 0 in-partition | 84 / 5 (boundary mentions only) |

Method note (honesty, per X04): loose patterns inflate. `games` with `play` →
15 "owners" (display/player); `timekeeping` with `hour` → 5; `spirit` with
`possession` → 7 (inalienable possessions); `onsen` alone → 74 (consensus).
Authors must use bounded patterns, state the bounding, and report first hits,
not just counts (K01 §2.2 limits, adopted verbatim).

### 3.1 C01 — `agriculture-subsistence-systems` (culture-material)

- **Owns**: the farm as a material system — field regimes (dry/bunded/terraced,
  fallow and rotation), the plough and traction complex, irrigation and
  water-lifting as institutions, the sowing/harvest labor calendar and its
  vocabulary, granary/storage and the storage-loss problem, land tenure and its
  material marks (boundary stones, plot names, field books), the crop-complex
  choice (staple vs mixed) and its risks.
- **Extends, never restates**: `cuisine-food-lexicon` (owns food as culture
  system — meal grammar, fermentation, dietary law; this entry owns
  *production*, not the table); `calendar-festival-systems` (owns the calendar;
  this entry owns the agricultural year's labor demands that couple to it);
  `material-culture-inference-method.md:66` (the constraint table — the
  plough→gender chain is calibrated there; cite, do not re-derive);
  `architecture-settlement-lexicon` (owns settlement form).
- **Couples (minimum)**: `cuisine-food-lexicon`, `calendar-festival-systems`,
  `material-culture-inference-method`, `architecture-settlement-lexicon`,
  `transport-mobility-lexicon` (surplus movement), `trade-economy-lexicon`
  (grain markets, measures), `vessel-container-lexicon` (storage vessels —
  couple), `textile-technology` (fiber crops), `myth-symbol/plant-symbolism`
  (crop codes), `myth-symbol/ritual-liminality` (first-fruits, harvest rites),
  `linguistics/semantic-fields-lexicon-building` (the field lexicon).
- **Decision record**: staple choice and why; water regime; tenure form; storage
  form; the failure year (what the culture does when the harvest fails).
- **Calibration**: Boserup's intensification cited; the plough-gender thesis
  labelled with its replication caveat (already calibrated at
  `material-culture-inference-method.md` §4 — cite it); terraces/irrigation
  histories cited per case; no Malthusian determinism.

### 3.2 C02 — `pastoralism-husbandry-lexicon` (culture-material)

- **Owns**: the herd as an economy — herd species and their product chains
  (dairy/meat/fiber/dung/traction), transhumance and pasture law, breeding and
  castration vocabulary, fodder and wintering, herd disease and its remedies
  (couples C04), the pastoral/settled interface (markets, tribute, raid, the
  "nomad" label as etic), herd markers and identity, herd counting as numeracy.
- **Extends, never restates**: `transport-mobility-lexicon.md:64-70` (the draft
  animal as a vehicle power source — couple); `cuisine-food-lexicon` (meat and
  dairy at the table); `trade-economy-lexicon` (livestock markets);
  `myth-symbol/animal-symbolism` (the herd animal's symbolic load — that file
  owns the symbol register).
- **Couples (minimum)**: `transport-mobility-lexicon`, `cuisine-food-lexicon`,
  `trade-economy-lexicon`, `textile-technology` (wool), `material-culture-inference-method`
  (substrate/constraints), `myth-symbol/animal-symbolism`,
  `myth-symbol/ritual-liminality` (sacrifice of herd animals — couple),
  `linguistics/semantic-fields-lexicon-building` (pastoral lexicon),
  `linguistics/numerals-and-measures` (herd counting).
- **Decision record**: species chosen and why; mobility regime; who owns the
  herd; the bad year; the settled/pastoral boundary rule.
- **Calibration**: transhumance typologies cited; "nomad" as a category labelled
  etic; no desert/savanna determinism; pastoral-wealth figures only with
  sources.

### 3.3 C03 — `extractive-industry-lexicon` (culture-material)

- **Owns**: the extraction chain — ore and stone, shafts and adits, drainage and
  ventilation, charcoal as the industry's binding constraint (couples C05),
  smelting/refining as the workshop's upstream, quarrying and stone transport,
  the mining settlement and its labor regimes (corvée, debt, specialist crews),
  mineral rights and the mining claim as law.
- **Extends, never restates**: `craft-artisan-lexicon` (owns the workshop and
  its marks — this entry owns what feeds it); `warrior-material-culture` (owns
  the fighting body); `material-culture-inference-method.md` (Andean
  metallurgy as a technology-style exemplar — cite the exemplar, do not re-run
  the framework); `vessel-container-lexicon` §6 (the ceramic material ladder).
- **Couples (minimum)**: `craft-artisan-lexicon`, `warrior-material-culture`,
  `trade-economy-lexicon` (metal as money-stuff), `fuel-lighting-water-utilities`
  (charcoal competition), `architecture-settlement-lexicon` (stone),
  `material-culture-inference-method` (Craddock, chaîne opératoire),
  `myth-symbol/ritual-liminality` (mine/forge taboos, smithcraft ritual),
  `linguistics/semantic-fields-lexicon-building` (extraction lexicon).
- **Decision record**: which ores/stones the culture works; who works them; who
  owns the rights; the fuel answer; the export/hoard decision.
- **Calibration**: Craddock cited; "lost technologies" labelled; pre-industrial
  output figures only with sources; no "metal = civilization" ladders.

### 3.4 C04 — `medicine-healing-material` (culture-material)

- **Owns**: the healing kit and its institutions — materia medica
  (plant/animal/mineral pharmacy) and its trade routes; emic pharmacy systems
  (humoral and others) labelled as doctrine; the apothecary's stock and
  vocabulary; surgical instrument families; bone-setting, midwifery, and their
  practitioner slots; infirmaries/hospitals as buildings and institutions;
  plague response as material logistics (quarantine, the plague-doctor kit).
- **Extends, never restates**: `cuisine-food-lexicon` (food as culture system —
  this entry owns the *medicinal* use of the same substrates);
  `material-culture-inference-method` (constraint→form spine);
  `myth-symbol/divination-omen-systems.md:112,126` (diagnosis as *reading* —
  the boundary is: that file owns the reading, this one the stock).
- **Couples (minimum)**: `cuisine-food-lexicon`, `vessel-container-lexicon`
  (pharmacy jars, flask families), `trade-economy-lexicon` (drug routes and
  prices), `craft-artisan-lexicon` (instrument-making registers),
  `textile-technology` (bandages/ligatures), `myth-symbol/plant-symbolism`
  (plant codes), `myth-symbol/ritual-liminality` (healing rites),
  `myth-symbol/divination-omen-systems`, `linguistics/semantic-fields-lexicon-building`
  (the healing field's strata).
- **Decision record**: what the culture can treat, with what, by whom; the
  practitioner licence; the failure-mode table (what it cannot treat and who is
  blamed).
- **Calibration**: humoral medicine as emic doctrine, not physiology; primary
  texts (Hippocratic corpus, Galen, Bencao gangmu) cited as documents; plague
  figures only with sources.

### 3.5 C05 — `fuel-lighting-water-utilities` (culture-material)

- **Owns**: the energy-and-utility layer — the fuel ladder (firewood, charcoal,
  peat, dung, oil, wax; coal/gas only if era-appropriate) with its cost gradient
  and its **competition between uses** (cooking, heating, lighting, smelting,
  dyeing); lighting devices (lamps, candles, rushlights, torches) and light as
  status and as time; water supply (wells, cisterns, aqueducts, carrying as
  labor) and sanitation (drains, cesspits, night-soil economy) — the utilities
  no other entry owns.
- **Extends, never restates**: `cuisine-food-lexicon` (hearth as cooking —
  `vessel-container-lexicon.md:33` owns the cooking-vessel side);
  `architecture-settlement-lexicon.md:140` (where the heat is — couple);
  `material-culture-inference-method.md:66` (the `energy & fuel` constraint row
  — cite); `myth-symbol/ritual-liminality.md:93` (Aztec New Fire — couple).
- **Couples (minimum)**: `cuisine-food-lexicon`, `architecture-settlement-lexicon`,
  `vessel-container-lexicon` (lamp families as containers), `trade-economy-lexicon`
  (oil/wax/firewood markets), `craft-artisan-lexicon` (chandlery, charcoal
  burning), `extractive-industry-lexicon` (charcoal competition — couple C03),
  `myth-symbol/ritual-liminality` (fire rites), `myth-symbol/color-symbolism`
  (light/dark values), `linguistics/numerals-and-measures` (night divisions).
- **Decision record**: the fuel ladder and who bears the carrying labor; who has
  light at night; the sanitation answer; the fire-keeping duty.
- **Calibration**: lamp-family histories cited; "candles were clocks" claims
  need the dated record; smoke-pollution and health claims only with sources.

### 3.6 C06 — `funerary-material-culture` (culture-material)

- **Owns**: the mortuary assemblage and its production — body-treatment
  materials (shrouds, resins, coffins), container typology
  (coffin/sarcophagus/urn/ossuary), grave-good classes and their production,
  the cemetery as institution (plot law, markers, necropolis geography),
  secondary burial's material logistics, the mortuary workshop's trade.
- **Extends, never restates**: `myth-symbol/ritual-liminality.md:24,32,61` (owns
  the *rites* — Hertz double funeral, retainer substitution arc; cite, do not
  re-run); `vessel-container-lexicon.md:38` (the urn as a container-extension
  row — couple); `ritual-garments` (mourning dress — couple);
  `material-culture-inference-method` §5 (grave-goods-as-résumé already
  calibrated — cite).
- **Couples (minimum)**: `myth-symbol/ritual-liminality`,
  `myth-symbol/afterlife-eschatology-symbolism` (the assemblage ↔ destination
  coupling is deliberate), `vessel-container-lexicon`,
  `textile-technology` (shrouds), `ritual-garments`, `architecture-settlement-lexicon`
  (tomb forms), `trade-economy-lexicon` (grave-good trade),
  `material-culture-inference-method` (Parker Pearson burial-politics caution),
  `linguistics/semantic-fields-lexicon-building` (mortuary lexicon).
- **Decision record**: body treatment; container; assemblage; cemetery form; who
  pays; what is destroyed vs kept.
- **Calibration**: Carthage tophet debate labelled (already at
  `ritual-liminality.md:68`); "retainer sacrifice" magnitudes only with sources;
  no grave-good résumé readings.

### 3.7 C07 — `afterlife-eschatology-symbolism` (myth-symbol)

- **Owns**: the otherworld as a designed place plus end-times doctrine —
  underworld/afterlife geography (descent topographies, rivers, gates, ferries,
  tolls), soul concepts and their plurality, judgment scenes and their criteria,
  ancestor destinations and the ancestor category, post-mortem institutions
  (guides, psychopomps, offering regimes), and eschatology (world-ending types,
  renewal cycles, judgment-day, millennial movements) as doctrine to design.
- **Extends, never restates**: `ritual-liminality.md:24,32,61` (the *rite* side);
  `cosmology-cosmography.md:35,49,51,56` (underworld mentions inside world
  models, the 7-heavens row at `:51` — this entry owns the land-of-the-dead *as
  a system*); `pantheon-archetypes.md:47` (death gods — couple);
  `flood-traditions` (the anti-type: this entry owns the ending, that one the
  reset-by-water).
- **Couples (minimum)**: `ritual-liminality`, `cosmology-cosmography`,
  `pantheon-archetypes`, `creation-myths-taxonomy` (cosmogony/eschatology
  symmetry), `myth-ritual-theories` (Frazer's dying-god labelled discredited),
  `direction-symbolism` (direction of the dead — `direction-symbolism.md` names
  Egyptian west/Greek Oceanus; couple), `number-symbolism` (judgment numbers),
  `culture-material/ritual-garments` (mourning dress),
  `culture-material/funerary-material-culture` (the assemblage — couple C06),
  `culture-material/era-periodization-models` (world-ages),
  `linguistics/naming-systems` (ancestor naming).
- **Decision record**: where the dead go (one place or many); who judges; what
  the living owe; how the world ends (or that it does not).
- **Calibration**: no universal "afterlife = underworld"; 2012/millennial
  movements as modern movements; Ragnarök/Revelation read as dated documents;
  K01's `ainu.md:16` first-hit is a bibliography line — the author must read the
  actual treatment, not the hit.

### 3.8 C08 — `purity-pollution-codes` (myth-symbol)

- **Owns**: the purity system — the anomaly engine as generator (category
  violation → pollution), the code layer (what is pure/impure and why: blood,
  death, birth, sex, food, strangers), purification technologies (water, fire,
  blood, time, confession, exile), purity policing institutions (inspection,
  exclusion, oath/vow, the purity officer), and the owned distinction between
  ritual purity (temporary, rite-scoped) and moral purity (standing).
- **Extends, never restates**: `color-symbolism.md` (owns color's purity
  valence — the partial owner K01/this seat both measured);
  `symbolism-synthesis-method.md` (Douglas cited there as a framework);
  `cuisine-food-lexicon` (kashrut/halal as calibration cases — this entry owns
  the *code*, not the food law); `animal-symbolism.md:34` (other-than-human
  persons and anomalous animals — the anomaly *picks* live there);
  `ritual-liminality` (cleansing/reversal rites — couple).
- **Couples (minimum)**: `symbolism-synthesis-method`, `color-symbolism`,
  `animal-symbolism`, `cuisine-food-lexicon`, `ritual-liminality`,
  `afterlife-eschatology-symbolism` (the dead as pollution — couple C07),
  `culture-material/architecture-settlement-lexicon` (bathhouse/precinct forms),
  `culture-material/textile-technology` (washing, purity of cloth),
  `culture-material/trade-economy-lexicon` (purity of goods, market rules),
  `linguistics/politeness-taboo-euphemism` (the verbal purity register),
  `linguistics/naming-systems` (polluted names).
- **Decision record**: the culture's pollution inventory; the purification
  answers; who polices; what happens to the permanently impure.
- **Calibration**: Douglas (1966) cited; her grid/group sociology labelled
  separate; ecological reductions of food law (Harris) labelled contested
  (already flagged at `cuisine-food-lexicon`); no "primitive hygiene" ladders.

### 3.9 C09 — `spirit-demon-taxonomy` (myth-symbol)

- **Owns**: the spirit class system — taxonomy of other-than-human persons
  (ghosts, the lineage dead, demons, local spirits, jinn analogues,
  possession-causing classes), the classes' properties (visibility, appetite,
  contractability, danger), possession and its handling (boundary: divination
  owns the *reading*), exorcism/propitiation as a technology, spirit
  institutions (shrines, mediums, spirit festivals, the licensed handler), and
  the spirit inventory as a closed code with register discipline.
- **Extends, never restates**: `animal-symbolism.md:34` (other-than-human
  *animals* and Hallowell's reframing — couple); `pantheon-archetypes` (god
  roles — this entry owns the non-god classes); `ritual-liminality` (exorcism
  and propitiation as rites — couple); `divination-omen-systems.md:147`
  (`## 8. Boundary — what this entry does not own` — couple, do not absorb).
- **Couples (minimum)**: `pantheon-archetypes`, `animal-symbolism`,
  `ritual-liminality`, `divination-omen-systems`,
  `symbolism-synthesis-method` (the spirit register), `myth-folktale-genres`
  (spirit tales), `culture-material/architecture-settlement-lexicon` (shrine
  forms), `culture-material/adornment-body-codes` (amulets worn — couple),
  `linguistics/naming-systems` (spirit names),
  `linguistics/politeness-taboo-euphemism` (naming taboos).
- **Decision record**: the spirit classes; their properties; the handling
  procedure; who may treat with them; what they want.
- **Calibration**: no "animism" as an evolutionary stage (Tylor/Frazer
  evolutionism labelled); possession ethnography cited per case; the jinn
  comparandum cited to scholarship (the civilization base
  `arabia-pre-islamic.md` holds the per-culture detail).

### 3.10 C10 — `pilgrimage-sacred-geography` (myth-symbol)

- **Owns**: the landscape as myth plus the pilgrimage institution — sacred place
  types (mountains, springs, caves, groves — extend, do not restate), place-
  origin myths and toponymic charter, the sacred map a culture can draw,
  pilgrimage as machine (vow, route, relic cult, shrine economy, merit,
  hospitality, the pilgrim's legal status), the pilgrimage vocabulary and its
  registers.
- **Extends, never restates**: `cosmology-cosmography` (axis mundi, ritual
  architecture interfaces), `plant-symbolism.md:56` (sacred groves and tree
  institutions — couple), `direction-symbolism.md:202` (exclusions routed —
  orientation belongs there), `ritual-liminality.md:110,111` (pilgrim caravan
  as communitas, pilgrim as liminal character — couple, do not re-derive),
  `celts.md:182` (layered sacred landscapes as the per-culture exemplar class).
- **Couples (minimum)**: `cosmology-cosmography`, `plant-symbolism`,
  `direction-symbolism`, `ritual-liminality`,
  `culture-material/transport-mobility-lexicon` (the road is theirs; the
  *sacred* route is this entry's), `culture-material/architecture-settlement-lexicon`
  (shrine forms), `culture-material/trade-economy-lexicon` (shrine economy),
  `culture-material/ritual-garments` (pilgrim dress),
  `linguistics/naming-systems` (place names as charter),
  `myth-folktale-genres` (foundation legends).
- **Decision record**: the culture's sacred map (3–7 named places); who may go
  and how; what a completed pilgrimage does to status; the shrine's economy.
- **Calibration**: hajj/Camino/Kumbh/Shikoku comparanda cited; no "all religions
  have pilgrimage" universal; relic-cult claims dated.

## 4. Author assignments and write order

| order | seat | slug | partition | writes |
|---|---|---|---|---|
| 1 | C01 | `agriculture-subsistence-systems` | culture-material | `cov/C01-entry-1.md` |
| 2 | C02 | `pastoralism-husbandry-lexicon` | culture-material | `cov/C02-entry-2.md` |
| 3 | C03 | `extractive-industry-lexicon` | culture-material | `cov/C03-entry-3.md` |
| 4 | C04 | `medicine-healing-material` | culture-material | `cov/C04-entry-4.md` |
| 5 | C05 | `fuel-lighting-water-utilities` | culture-material | `cov/C05-entry-5.md` |
| 6 | C06 | `funerary-material-culture` | culture-material | `cov/C06-entry-6.md` |
| 7 | C07 | `afterlife-eschatology-symbolism` | myth-symbol | `cov/C07-entry-7.md` |
| 8 | C08 | `purity-pollution-codes` | myth-symbol | `cov/C08-entry-8.md` |
| 9 | C09 | `spirit-demon-taxonomy` | myth-symbol | `cov/C09-entry-9.md` |
| 10 | C10 | `pilgrimage-sacred-geography` | myth-symbol | `cov/C10-entry-10.md` |

Rules for authors:

- Each draft contains the **full entry bytes as one fenced markdown block**,
  plus a short non-fenced preamble stating slug, target path
  (`corpus/knowledge/<partition>/<slug>.md`), the author's re-run absence sweep
  (command + output + date), the `- topic:` line verbatim (so C11 can lift it
  byte-equal), and any `(to-verify)` items. The integrator copies the fenced
  bytes to the target path; authors never write `corpus/knowledge/**`.
- Slugs are fixed by this table; an author who finds their slug already claimed
  in another draft appends `-b` and says so in `- gap:` (round-19 collision
  rule, `reports/round-19/gaps.md:4-11`; K01 §2.5).
- Every path a draft cites is resolved with `grep`/`ls` before filing (K01
  §2.1: do not create a second dangling pointer). `- couples:` targets resolve
  from the entry's own directory or the lane root.
- No draft may restate a neighbour's owned content — the per-topic briefs above
  name the ownership boundaries; violations are the audit's first defect class.
- No freeze bytes move; the r7 read-set is not touched (X00/R08 own the
  collision matrix — authors flag, never decide).

## 5. Audit and reconciliation sequence (ordered, with owners)

1. **Drafts land** (C01–C10) with their re-run sweeps and `- topic:` lines.
2. **Runbook** (C12) fixes the per-entry check list on the round-10 legs (K02
   §2.1/§5): frontmatter five fields (head-block scoped for the tail pair; the
   partition `source:` ruling of finding 0.2), `- gap:` clause + "gap" heading
   (finding 0.5), decision-record heading, `couples:` resolution, no-bleed scan,
   `(to-verify)` census, size floor; expected results for the 10 drafts stated.
3. **Audit 1–5** (C13) and **audit 6–10** (C14) — two independent auditors, two
   instrument instances (K02 §5.7: round-19 precedent = a second process of the
   read-only tool plus one manual re-read); every check with observed result,
   defects severity-ranked against K02 §3's classes D1–D8 (phantom `couples:`
   target; paraphrase README row; stale footer; checker-regex false-negative
   D4 — a red leg with the substance present is D4, not a content defect; D6
   missing tail; D8 instrument false-negative).
4. **Third sample audit** (C17) — 3 of 10 by lot (state the choice) + README
   delta numbers re-derived.
5. **Adversarial reviews** (R01/R02/R03) — source-pointer resolution re-checked
   independently, no-fabrication hunt, runbook adequacy.
6. **README delta** (C11) — exact before/after blocks for the five README parts
   (finding 0.4 anchors: `:147`, `:169`, rows, `:469`, `:471-473`, new revision
   block above `:3`), rows byte-equal to each entry's `- topic:` text, in
   filename order. Integrator applies; authors never do.
7. **Integrator applies** all ten entries + README delta; nothing else.
8. **Reconcile and recount** (integrator, with C15/C16/S01 receipt material):
   census → inventory → README equality (`rows == files == 211`, 0
   missing/ghosts/dupes/mismatches/drift, `totals_line 211`, `footer_ok True`,
   record `readme_sha256`). Any mismatch is a defect, not a rounding.
9. **Validation legs** (O08/S04 define, integrator implements in
   `reports/round-35/run-validation.py` — never executed in-tree by a seat):
   partition counts 24/23/211; ten entry files present with the five fields +
   `- gap:`; README equality; inventory total 211; preservation of the 201
   baseline bytes (no filed-round or existing-entry byte changes).

## 6. Counting commands and thresholds (mapped to `claims.json`)

- `for p in linguistics myth-symbol culture-material synthesis verification
  civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → expect
  `21 23 24 29 20 94`.
- `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → expect `totals.files 211`.
- `python3 reports/round-35/run-validation.py` → exit 0 (implemented per §5.9;
  not run in-tree by seats).
- Thresholds (claim C): 10/10 new entries audited clean by two independent
  auditors (C13/C14, with C17 sampling); README counts == live census;
  inventory total 211; zero fabricated sources (every citation resolves or is
  marked `(to-verify)` in-file).

## 7. Risks, alternates, and swap rules

- **Held alternates with evidence** (named, not hidden; swap rule below):
  `magic-and-witchcraft-systems` (`witchcraft|sorcery|sympathetic magic` → 6
  mentions, **0 owners**; `divination-omen-systems.md:147` routes it out by
  name) · `timekeeping-instruments` (`sundial|gnomon|clepsydra|water
  clock|hourglass` → 0 files, 0 owners; `calendar-festival-systems` is the
  partial owner of time machinery) · `games-and-play-material-culture`
  (bounded `board game|chess|patolli|senet` → 3 incidental; 0 owners) ·
  `incense-and-aromatics` (17 mentions, 0 owners) · `sacred-kingship`
  (15 mentions, 0 owners; `benin.md:1` is the per-culture class) ·
  `bathing-and-body-hygiene` (K01 CM-9: 0 keyword hits — lowest yield) ·
  K01's CM-7 warfare-logistics, CM-8 intoxicants, MS-6 dream/vision, MS-7
  ancestor veneration, MS-8 apocalypse, MS-9 iconography (all in K01 §2.3/§2.4
  with first-hit citations).
- **Swap rule**: if an author's own re-run sweep or boundary read shows their
  assigned topic restating an existing entry (a D-class defect), the seat
  reports it and takes the next alternate in the order listed above, recording
  the swap and the evidence in `- gap:` — the integrator reconciles the
  allocation and C11's README delta to the swapped slug. No silent
  substitutions.
- **Highest-overlap watch item**: C06 (funerary) and C08 (purity) sit nearest
  existing content (4 and 1 partial owners respectively). Their briefs carry the
  strictest boundaries; their auditors should run the duplication check (K02
  §5.4: slug/title overlap vs the 201 pre-existing titles, fewer than four
  shared content terms of length > 3).
- **The lowest-axis rule is satisfied**: coverage has zero regimen-2 claims
  (`claims.json` lowest_axis_reasoning) and this plan is the coverage block's
  spine.
- **What this plan does not do**: it admits nothing, certifies no round, decides
  no canon, writes no corpus bytes, and does not answer X00/R08's freeze-drift
  question (they own it; authors only flag).
- **Honesty note**: the sweep counts in §3 are dated readings (2026-10-19, HEAD
  `4a7aede`); K01's are its own; authors and auditors re-run and cite their own
  — a count that differs is a finding, not a correction.

## Owed

- K01/K02 reconciliation — **done by this seat** when they landed mid-run (§0.6);
  the integrator owes only a spot-check that the ten slugs in §3/§4 match the
  drafts actually written, and that no author silently re-slugged.
- `reports/round-35/cov/C12-audit-runbook.md` — owed by seat C12 (per
  `targets.json`); this plan feeds it the bar (§0.1, §0.5, §5.2) and K02 §5 the
  recipe.
- `reports/round-35/run-validation.py` — absent at K02's measurement; its C legs
  will fix the exact README/entry criteria; re-check §5.9/§6 against it when it
  lands (owner: integrator/O08).

## Citations

- `reports/round-35/claims.json` (claim C, thresholds, counting commands,
  baseline `4a7aede`, lowest-axis reasoning); `reports/round-35/targets.json`
  (seat P01 mission, out path, shared_rules); `REGIMEN.md`; `AGENTS.md`;
  `corpus/QUALITY.md`.
- Command `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`.
- Command `for p in …; do ls corpus/knowledge/$p/*.md | wc -l; done` →
  `21 19 18 29 20 94`; `ls corpus/knowledge/*/*.md | wc -l` → `201`.
- Command `for f in topic sources couples "verified-at" recheck source scope; do
  grep -rl "^- $f:" corpus/knowledge --include='*.md' | wc -l; done` →
  `201 201 201 201 201 134 0`.
- Command `grep -rl '^- gap filled:' corpus/knowledge --include='*.md' | wc -l`
  → `13`; `grep -rl '^## .*[Dd]ecision record' corpus/knowledge --include='*.md'
  | wc -l` → `22`.
- Absence sweeps: §3's table patterns run as
  `grep -rilE --include='*.md' -e "<pattern>" corpus/knowledge | wc -l` and the
  topic-owner test `grep -rlEi --include='*.md' "^[-*] ?topic:.*(<pattern>)"
  corpus/knowledge | wc -l` (2026-10-19, HEAD `4a7aede`); pollution checks:
  `onsen` → 74 false positives, `bathing` → 6 incidental, `bathhouse|hammam` → 0.
- `reports/round-35/scout/K01-coverage-census.md` §1.1–1.5, §2.2–2.5, §3.1–3.6
  (census; gap triage with first-hit citations; allocation; entry-shape contract;
  gap-form rule from `reports/round-10/coverage/audit-filler.md:104-115`).
- `reports/round-35/scout/K02-entry-audit-method.md` §2.1–2.3 (round-10 legs;
  instrument false negatives; field census and the `scope` reading), §3 (defect
  classes D1–D8), §4.1–4.4 (README convention, delta arithmetic, sweep limits,
  counts), §5 (audit recipe).
- `corpus/README.md:3` (revision 1.9), `:69-93` (revision 1.5 row-text repair),
  `:147`, `:169`, `:469`, `:471-473`.
- Verified line refs used in §3: `culture-material/material-culture-inference-method.md:66,92`;
  `culture-material/vessel-container-lexicon.md:9,33,38,137,139`;
  `culture-material/transport-mobility-lexicon.md:3,20`;
  `culture-material/cuisine-food-lexicon.md:43`;
  `culture-material/architecture-settlement-lexicon.md:140`;
  `myth-symbol/ritual-liminality.md:24,32,61,68,93,110,111`;
  `myth-symbol/cosmology-cosmography.md:35,49,51,56`;
  `myth-symbol/divination-omen-systems.md:112,147`;
  `myth-symbol/animal-symbolism.md:34`; `myth-symbol/plant-symbolism.md:3,13,56,162`;
  `myth-symbol/direction-symbolism.md:202`; `myth-symbol/pantheon-archetypes.md:47`;
  `myth-symbol/myth-ritual-theories.md:85`;
  `linguistics/register-lexicon-ceilings.md:250`;
  `civilizations/bali.md:14`; `civilizations/amazigh-berber.md:146`;
  `civilizations/mamluk.md:37`; `civilizations/fon-dahomey.md:56`;
  `civilizations/etruria.md:65`; `civilizations/celts.md:182`;
  `civilizations/benin.md:1`.
- Command `wc -c` on `plant-symbolism.md`, `vessel-container-lexicon.md`,
  `register-lexicon-ceilings.md` → `43150 43056 36139`.
- `reports/round-19/gaps.md:4-11` (slug→gap→seat registry + collision log);
  `reports/round-19/audit-1.md` (audit criteria); `reports/round-10/coverage/review-C04.md:19`
  (`verified-at` scope-bearing, per K02 §2.3).
- `reports/round-34/plan/P01-d-plan.md` (fragment header/format precedent).
- `ls reports/round-35/` at seat start (no `scout/` or `plan/` dir);
  `ls reports/round-28/readme/` → `reconcile.md sweep.py verify.md`.
