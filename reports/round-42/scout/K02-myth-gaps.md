- Seat: K02 | scout | C | date 2026-10-19 | baseline ac47c78

# K02 — myth-symbol gap scout: 23 entries inventoried, four gap-named topic recommendations (one slot already taken mid-wave), plus an independent confirmation of C08's README-vector defect

**Mission** (`reports/round-42/targets.json` seat `K02`, verbatim): *"Myth-symbol gap scout: the 23
entries' topics + gap analysis + 4 recommendations with sources (mirror r39's K01 method)."* Out path:
this file only.

**Method / boundary.** All measurements read-only, lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD `ac47c78`
(`ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`), `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`. No filed byte edited; no `reports/round-*/run-validation.py` executed
anywhere; no corpus byte staged; no re-freeze; no packet-surface change; no git/install/network
action. The one filed instrument executed is `reports/round-28/readme/sweep.py`, run **read-only**
against the live tree (its own docstring states it has no write path inside the lane).

**Method source.** The inventory-plus-absence-sweep shape mirrors r39's K01
(`reports/round-39/scout/K01-verification-gaps.md:1-234`), whose four recommendations all landed in
round 40 (`corpus/README.md:8-12`, rev 2.3). Its numbers are **not** inherited here: the partition
moved since (verification 20 → 24, linguistics 21 → 25), so every count below was re-measured at
`ac47c78`.

**Verdict in one line.** The partition is dense on *narrative genres*, *symbol registers* and
*ritual grammar*, and has been **frozen for seven rounds** while other partitions grew; four domains
have heavy in-corpus demand with **zero or incidental topic-ownership**, and the lapidary is the
sharpest because a sibling entry names it as part of the method it imitates and never builds it. One
of the four (purity) was drafted concurrently by seat C02 before this fragment landed — §4.4
dispositions that slot rather than re-recommending it.

---

## 1. Baseline state (measured, not asserted)

- **Partition = 23 files**: `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **23** (2026-10-19,
  lane root). Corpus totals **220** = civilizations 94 + culture-material 25 + linguistics 25 +
  myth-symbol 23 + synthesis 29 + verification 24 (per-directory `ls … | wc -l` sweep; matches the
  `footer_live` vector `25/23/25/29/24/94` read live by `reports/round-28/readme/sweep.py`).
- **The index is green at baseline**, so the 23 count is not a stale reading:
  `python3 -B reports/round-28/readme/sweep.py` → `rows 220 files 220`, `missing_from_index 0`,
  `orphan_rows 0`, `topic_mismatch 0`, `header_drift {}`, `totals_line 220 totals_ok True`,
  `footer_ok True`, **exit 0**; `readme_sha256
  d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f` (equals a fresh
  `sha256sum corpus/README.md`).
- **The partition has been closed to additions since round 35**: `git log --diff-filter=A
  --format="%h %ad %s" --date=short --name-only -- corpus/knowledge/myth-symbol` returns exactly
  three landings — `ce103bf` 2026-10-19 (round-35, **4** entries:
  `binding-speech-complex.md`, `death-afterlife-eschatology.md`,
  `eschatology-world-end-systems.md`, `sacred-kingship-mythic-charter.md`), `94ca098` 2026-10-17
  (round-10, **3**: `direction-symbolism.md`, `divination-omen-systems.md`,
  `plant-symbolism.md`), and `76c105b` 2026-10-17 (mint wave, **16**). Rounds 36–41 added nothing
  here while culture-material moved 18 → 25 and verification 20 → 24. The "thinnest partition"
  premise of claim C is confirmed by git history, not by a single count — and the freeze is the
  reason the gap list below is long.
- **Header contract is uniform but not identical**: 23/23 carry `- topic:` / `- sources:` /
  `- couples:` / `- source:` / `- verified-at:` / `- recheck:`; five additionally carry a gap field
  (`binding-speech-complex.md:3`, `eschatology-world-end-systems.md:4`,
  `sacred-kingship-mythic-charter.md:4`, `death-afterlife-eschatology.md:3`,
  `plant-symbolism.md:3`). Four of those five are the round-35 landings — i.e. the gap field is the
  *new-entry* convention, which is what C01–C04 are writing.

## 2. The 23 existing entries' topics

| # | entry | domain it owns (one line) |
|---|---|---|
| 1 | `animal-symbolism.md` | fauna register: totemism archive, seven binding mechanisms, guardian animals, food law, zodiac day-signs, heraldry, the serpent's double ledger |
| 2 | `binding-speech-complex.md` | oath / curse / blessing / name-power as one machinery + the enforcement ledger |
| 3 | `celestial-symbolism-calendars.md` | sky objects, planet-as-god chains, eclipse omen systems, calendar anchoring |
| 4 | `color-symbolism.md` | what colors mean (valence, carrier, institution); the anti-porting rule |
| 5 | `comparative-frameworks.md` | the four etic toolkits (Campbell, Eliade, Lévi-Strauss, Propp/Dundes) with calibration |
| 6 | `cosmology-cosmography.md` | world models: center / layers / direction-code / shape / age-doctrine |
| 7 | `creation-myths-taxonomy.md` | the seven cosmogony types + creation-by-speech |
| 8 | `death-afterlife-eschatology.md` | the four death-doctrine questions, survival typology, judgment machines, the unquiet dead |
| 9 | `direction-symbolism.md` | the direction/spatial register: frames, cardinal coinage, left/right, rotation |
| 10 | `divination-omen-systems.md` | divination as designed technology: techniques, interpretive engine, licence institutions, word-omen channel |
| 11 | `eschatology-world-end-systems.md` | how a world ENDS: scopes, six-axis ending grammar, seven-tradition typology |
| 12 | `flood-traditions.md` | flood myths as charters, not hydrology |
| 13 | `hero-journey-variants.md` | hero pattern families (monomyth, Rank/Raglan, dragon-slaying, female arcs, twins) |
| 14 | `motif-index-usage.md` | Thompson Motif-Index + ATU type index as coherence tools |
| 15 | `myth-folktale-genres.md` | Bascom's four forms; the house genre rules |
| 16 | `myth-ritual-theories.md` | classical origin theories and their real scholarly status |
| 17 | `number-symbolism.md` | why numbers go sacred; counting-base constraint |
| 18 | `pantheon-archetypes.md` | divine-role archetypes, Dumézil with calibration, build protocol |
| 19 | `plant-symbolism.md` | flora register: world trees, sacred groves, flower codes, botanical design |
| 20 | `ritual-liminality.md` | rites of passage, liminality/communitas, gift, sacrifice typology, calendrical rites |
| 21 | `sacred-kingship-mythic-charter.md` | the eight legitimation channels, failing-king devices, the royal register |
| 22 | `symbolism-synthesis-method.md` | the core generation method: five registers, alignment matrix, audit checklist |
| 23 | `trickster.md` | the trickster figure class, typology, design protocol |

**Shape of the coverage.** Three clusters and one hole.

- **Narrative genres** (7, 11, 12, 13, 14, 15, 16, 23) — dense, well-calibrated.
- **Symbol registers** (1, 3, 4, 9, 17, 19) — dense: color, animal, number, celestial, direction,
  flora. The register family is the partition's most self-aware list
  (`symbolism-synthesis-method.md:23` names the five; `plant-symbolism.md:3` names itself as the
  flora sixth).
- **Ritual / institution grammar** (2, 8, 20, 21) — dense, all four landed round-35 or earlier.
- **The hole.** Everything above is a *system with an owner*. What the partition lacks is a set of
  domains that the corpus **uses everywhere, cites by name, and leaves unowned** — §3 measures four,
  and §4 sources them.

## 3. Unnamed gaps — absence sweeps (commands run 2026-10-19 at `ac47c78`, lane root)

Two sweeps per candidate, mirroring the ownership test at
`reports/round-35/scout/K01-coverage-census.md:178-205`: (a) a **demand sweep** — regex over the
full text of all 220 entries, counting distinct files that mention the domain; (b) a **topic-ownership
test** — the same regex over each entry's single `- topic:` line, so a hit means some entry *names*
that domain as its subject. A candidate is a gap signal when demand is high and topic-owners are
zero, or the owners are civilization bases / by-product mentions only.

Scripts: `.scratch/k02/sweep.py` and `.scratch/k02/sweep2.py` (gitignored scratch, reproducible from
the patterns printed below).

| candidate | demand (files of 220) | topic-owners | who the owners are |
|---|---|---|---|
| **lithic / mineral / gem register** | 39 | **0** | — none |
| **dream / vision / trance** | 58 | 2 | `civilizations/mongol.md`, `myth-symbol/divination-omen-systems.md` (owns the *reading technology*, not the experience) |
| **pilgrimage / sacred geography** | 69 | 3 | `civilizations/arabia-pre-islamic.md` (a civilization base), `culture-material/architecture-settlement-lexicon.md` (sacred *buildings*), `myth-symbol/plant-symbolism.md` (sacred *groves*) |
| **purity / pollution / unclean** | 54 | 3 | `culture-material/bathing-and-body-hygiene.md` (hygiene split), `myth-symbol/color-symbolism.md` (colour's purity valence), `myth-symbol/death-afterlife-eschatology.md` (a mourning window) |
| spirit / demon / other-than-human class | 164 | 6 | civilization bases + `animal-symbolism.md` / `plant-symbolism.md` (spirits *of* animals/plants) — incidental |
| monster / adversary / terato | 23 | 0 | — none (but `dragon` / `chaoskampf` are rows inside `hero-journey-variants.md` and `creation-myths-taxonomy.md`) |
| marriage / alliance | 86 | 5 | `furniture-interior-lexicon.md`, `ritual-garments.md`, `sumptuary-law-rank-display.md` — all material-culture by-product |

**Topic-line scoped sweeps** (`grep -rlEi -- "^- topic:.*\b<term>" corpus/knowledge/*/*.md | wc -l`,
the stricter form used at `binding-speech-complex.md:3` and `divination-omen-systems.md:32`):
`mineral` **0**, `gem` **0**, `lapidary` **0**, `lithic` **0**, `precious` **0**, `trance` **0**,
`ecsta` **0**, `purif` **0**, `pollution` **0**, `defile` **0**, `monster` **0**, `monstrous` **0**,
`microcosm` **0**, `altered state` **0**, `sacred space` **0**, `sacred place` **0**, `bogey` **0**.

**The absence is named by the partition's own method file.** The sharpest single piece of evidence is
not a zero count but a sibling's own sentence:

> `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:29` — "**The medieval Latin package**:
> bestiary + **lapidary** + numerology + heraldic code — a closed code that is manufacturable,
> teachable, and checkable (White 1954; Hopper 1938; Fox-Davies 1909)."

The method entry names four components of the closed code it tells worldbuilders to imitate. Three
have owners: **bestiary** → `animal-symbolism.md:90` (White 1954 already registered there),
**numerology** → `number-symbolism.md` (Hopper 1938 already registered at
`symbolism-synthesis-method.md:9`), **heraldic code** → `animal-symbolism.md` §7 (`:84-91`,
Fox-Davies 1909 at `:13`). The **lapidary has no file** — and the only in-partition hit for the word
is that very line. That is the "machinery everyone couples to and nobody owns" shape that
`plant-symbolism.md:3` used to justify its own landing.

**Second named hook, same shape.** `divination-omen-systems.md:64` prints a two-column table whose
pole A is *divinatio naturalis* = "**frenzy, dreams, oracular possession**", and whose §8 boundary
table (`:147-160`) enumerates what every neighbouring entry owns — sky objects, direction codes, tale
indexing, sacrifice typology, name magic — while never claiming the inspired state itself. The entry
uses dreams as one cell of a grid and one row of a technique typology (`:89` dream-oracle &
incubation; `:126` the dream-sanctuary institution). No entry owns dream/vision/trance as a system.

## 4. Four topic recommendations (gap-named, sourced)

Each recommendation gives the gap, the internal decision surfaces, the source shelf, and the couples.
**External sources are taken only from already-registered, in-corpus material** — no new bibliography
is invented, and where a work is already carried by another entry it is cited **by path**, not
re-fetched (no network at seat time; this seat's `verified-at` status is *in-corpus locators
re-read, external works inherited*). Executors must still re-check editions at authoring time per
`corpus/QUALITY.md:3-8` and mark anything unretrieved `(to-verify)` inline.

### R1 — Lithic / mineral register: stone, gem and metal as symbol, prestige and material grammar

- **Gap.** The register family is closed at color/animal/number/celestial/direction
  (`symbolism-synthesis-method.md:23`) plus flora (`plant-symbolism.md:3`), and
  `symbolism-synthesis-method.md:29` names the **lapidary** as the fourth component of the medieval
  package it imitates — but **no entry owns stone**. Demand sweep 39/220 files, **0 topic-owners**;
  topic-line sweep for `mineral`/`gem`/`lapidary`/`lithic`/`precious` → **0 files each**.
- **The corpus already uses it as by-product, in exactly the places a register file would systematize:**
  `culture-material/ritual-garments.md:59` (the choshen's 12 gemstones, one per tribe, with the
  zodiac reading attributed to Philo and Josephus); `civilizations/maya-classic.md:10` and `:127`
  (Taube 2005 on jade ↔ maize, centrality, rulership, breath — with the calibration that not every
  jade object carries all associations); `civilizations/china-shang-zhou.md:106` (Fu Hao's tomb
  jades, including Neolithic objects in a later burial — the heirloom rule); `civilizations/maori.md:13-14`
  (pounamu as inalienable *taonga*, with the Ngāi Tahu kaitiaki protocol); `civilizations/siam-thai.md:126`
  (the Emerald Buddha as dynastic palladium); `culture-material/funerary-material-culture.md:22`
  (Pliny *Naturalis Historia* 36.27 — the *sarcophagus* stone of Assos, a **material property that
  becomes a container's name**); `culture-material/vessel-container-lexicon.md` (Pliny 36.27 again,
  the same mechanism for vessels).
- **Internal decision surfaces:** `myth-symbol/symbolism-synthesis-method.md:23,29` (the register
  grammar and the package this fills a slot of); `myth-symbol/color-symbolism.md` (the sibling
  register — and its **dye-scarcity economics**, the exact analogue of gem scarcity, is the model for
  a stone-scarcity economics); `myth-symbol/animal-symbolism.md:84-91` (heraldic tincture law —
  stones enter heraldry as charges); `myth-symbol/plant-symbolism.md:15` (the *stationary/ownable*
  property argument, which applies to a quarry or a mine even more sharply than to a grove);
  `culture-material/craft-artisan-lexicon.md` (the lapidary as a trade with a ladder and marks);
  `culture-material/trade-economy-lexicon.md` (gem grades as value language);
  `culture-material/sumptuary-law-rank-display.md` (who may wear which stone — the enforcement side);
  `culture-material/material-culture-inference-method.md` (what stone survives deposition, and what
  does not — the inference caveat); `myth-symbol/direction-symbolism.md` and
  `myth-symbol/cosmology-cosmography.md` (stones as axis/corner markers);
  `civilizations/*.md` (the per-culture stone data, cited not restated).
- **Sources (all already in-corpus).** Pliny the Elder, *Naturalis Historia* **book 37** (the
  classical lapidary spine) — the corpus already carries Pliny at books 2, 9, 13, 16.95, 18, 28.18,
  28.191, 31.41, 36.27 and 36.71–72, so book 37 is a same-edition extension, and
  `funerary-material-culture.md:22` already demonstrates the book-37-adjacent reading style;
  White (1954) *The Book of Beasts* — registered at `animal-symbolism.md:13` and named at
  `symbolism-synthesis-method.md:29`; Hopper (1938) *Mediaeval Number Symbolism*, Columbia UP —
  registered at `symbolism-synthesis-method.md:9`; Fox-Davies (1909) *A Complete Guide to Heraldry*,
  Nelson — registered at `animal-symbolism.md:13`; Karl A. Taube (2005), "The Symbolism of Jade in
  Classic Maya Religion," *Ancient Mesoamerica* 16(1):23–50, doi:10.1017/S0956536105050017 —
  registered **with a DOI and an inspected abstract** at `civilizations/maya-classic.md:10`;
  Te Rūnanga o Ngāi Tahu, "Pounamu" (read 2026-10-17) and Basil Keane, "Pounamu – jade or
  greenstone," *Te Ara* (retrieved 2026-10-17) — registered at `civilizations/maori.md:13-14`;
  *choshen* gemstones at `ritual-garments.md:59`. **Living-practice caution applies**: pounamu is
  restricted material and the entry must follow `verification/real-world-inspiration-boundaries.md`
  and `maori.md:20`'s named-knowledge-holder rule, not extract it.
- **Couples:** myth-symbol — `symbolism-synthesis-method.md`, `color-symbolism.md`,
  `animal-symbolism.md`, `plant-symbolism.md`, `cosmology-cosmography.md`, `direction-symbolism.md`;
  culture-material — `craft-artisan-lexicon.md`, `trade-economy-lexicon.md`,
  `sumptuary-law-rank-display.md`, `ritual-garments.md`, `funerary-material-culture.md`,
  `material-culture-inference-method.md`; verification — `real-world-inspiration-boundaries.md`,
  `myth-consistency-gate.md`.
- **Filename:** `mineral-stone-symbolism.md`. **Sorts cleanly** into the current set (verified:
  `sort -c` on the 23 existing names plus this one passes; it lands between
  `hero-journey-variants.md` and `motif-index-usage.md`).

### R2 — Dream, vision and trance: the altered-state complex and the institutions that license it

- **Gap.** `divination-omen-systems.md:64` puts "frenzy, dreams, oracular possession" in a table
  cell and `:89`/`:126` use dream-oracles and dream-sanctuaries as one technique row and one
  institution row — but its own §8 boundary table (`:147-160`) lists every neighbouring entry's
  property and **claims none of these**; the entry owns the *reading technology*, not the experience
  or its social machinery. Demand sweep 58/220, topic-owners 2 (a civilization base and divination
  itself). Topic-line sweep: `trance` **0**, `ecsta` **0**, `vision` **0**, `altered state` **0**.
- **Internal decision surfaces:** `myth-symbol/divination-omen-systems.md:64,89,126,135,186` (the
  natural/artificial axis, the dream-oracle row, the dream-sanctuary institution, the
  "medicine from incubation cases" by-product rule, and the Dodds calibration);
  `myth-symbol/animal-symbolism.md:53` (Eliade's shaman's assisting animal-spirits, plus
  Hallowell's bear ceremonialism — the spirit-helper holder slot); `myth-symbol/ritual-liminality.md:111`
  (the permanent liminal specialist list already includes "shaman"); `myth-symbol/pantheon-archetypes.md`
  (the oracular/possession deity slot); `culture-material/music-instrument-lexicon.md:96` (the
  shaman's drum as riding animal and world-model — the material carrier);
  `linguistics/politeness-taboo-euphemism.md` and `linguistics/register-strata-attestation.md`
  (the possession register and its attestation law); `verification/real-world-inspiration-boundaries.md`
  (**the binding constraint** — possession and trance material is the most restricted knowledge in
  the corpus; the entry must mark access boundaries, not fill tables).
- **Sources (all already in-corpus).** Eliade (1951; trans. Trask 1964) *Shamanism: Archaic
  Techniques of Ecstasy*, Pantheon — registered at `animal-symbolism.md:8` and
  `cosmology-cosmography.md:5`; the same author's *The Sacred and the Profane* (1957; trans. 1959)
  and *The Myth of the Eternal Return* (1949) — registered at `cosmology-cosmography.md:5` and
  `comparative-frameworks.md:9`; Turner (1967) *The Forest of Symbols* and (1969) *The Ritual
  Process* — registered at `ritual-liminality.md:6`; van Gennep (1909) *Les rites de passage* —
  registered at `ritual-liminality.md:5`; Artemidorus, *Oneirocritica* (2nd c. CE; trans. White 1975),
  Gardiner (1935) *Hieratic Papyri in the British Museum* 3rd series (Papyrus Chester Beatty III),
  and Oppenheim (1956) "The Interpretation of Dreams in the Ancient Near East," *TAPS* 46(3) — all
  three registered at `divination-omen-systems.md:12`; Dodds (1951) *The Greeks and the Irrational*
  ch. 4 — registered **with its calibration already written** at `divination-omen-systems.md:186`
  ("its developmental sequence … is a mid-century evolutionism; use the material, label the frame");
  Harner (1980) *The Way of the Shaman* — registered at `animal-symbolism.md:8` and flagged there as
  a calibration item. Note: `Vitebsky`, `Bourguignon`, `Winkelman`, `Schieffelin`, `Lambek` and
  `Csordas` are **not** registered anywhere in the corpus (measured: 0 files each) — they are the
  obvious scholarly shelf for this topic, so an author choosing this entry must either register them
  from outside (impossible at seat time, no network) or build the entry on the in-corpus shelf above.
  **This is R2's main risk and is the reason it ranks below R1.**
- **Couples:** myth-symbol — `divination-omen-systems.md`, `ritual-liminality.md`,
  `pantheon-archetypes.md`, `comparative-frameworks.md`, `cosmology-cosmography.md`;
  culture-material — `music-instrument-lexicon.md`; linguistics —
  `politeness-taboo-euphemism.md`, `register-strata-attestation.md`; verification —
  `real-world-inspiration-boundaries.md`, `myth-consistency-gate.md`.
- **Filename:** `dream-vision-trance.md`. Sorts cleanly (between `divination-omen-systems.md` and
  `eschatology-world-end-systems.md`).

### R3 — Pilgrimage and sacred geography: route as rite, the shrine network, and sacred-precinct law

- **Gap.** `direction-symbolism.md` owns orientation, `plant-symbolism.md` owns sacred *groves* as
  objects, and `architecture-settlement-lexicon.md` owns sacred *buildings* as vocabulary
  (`:67-84`, temple/church/shrine/mosque as distinct institutional concepts) — but **no entry owns
  place as a register**: the holy-site typology, the route-as-rite, the shrine network, festival
  geography, and sacred-precinct law. Demand sweep 69/220; topic-owners 3, and each owns a different
  adjacent thing (a civilization base, sacred buildings, sacred groves). Topic-line sweep:
  `pilgrim` → 1 file (a civilization base); `sacred place` / `sacred space` → **0**.
- **Internal decision surfaces:** `myth-symbol/ritual-liminality.md:110,111,118` (the pilgrimage
  caravan as the communitas generator, the pilgrim as a permanent liminal specialist, and "site the
  communitas: pilgrimage road …" — the entry explicitly *uses* pilgrimage as an example and does not
  own it); `myth-symbol/cosmology-cosmography.md:36` (mountain as the sky-meets-earth site temples
  replicate — the axis-mundi-to-architecture interface, with Kramrisch and Mannikka already
  registered at `:9`); `myth-symbol/plant-symbolism.md:15,`§4 (the grove as a *legal object* —
  owned, fenced, taxed — which is the property argument a sacred-precinct entry extends);
  `culture-material/architecture-settlement-lexicon.md:67-84` (the building vocabulary a precinct
  entry couples to rather than restates); `myth-symbol/direction-symbolism.md` (orientation of
  prayer and institutions: qibla, axiality, mountainward temples);
  `myth-symbol/divination-omen-systems.md:126` (the sanctuary as an institution with an archive);
  `culture-material/transport-mobility-lexicon.md` (the route as a material system — ROUTE is
  literally its first layer); `culture-material/calendar-festival-systems.md` (festival geography
  and the annual cycle that times a pilgrimage); `verification/real-world-inspiration-boundaries.md`
  (living-practice rule — the Hajj is a living rite).
- **Sources (all already in-corpus).** Turner & Turner (1978) *Image and Pilgrimage in Christian
  Culture*, Columbia UP — **registered at `ritual-liminality.md:6`**, the single most on-point work
  for this entry and already carried in-lane; Turner (1969) *The Ritual Process* (communitas) and
  (1974) *Dramas, Fields, and Metaphors* — `ritual-liminality.md:6`; van Gennep (1909) —
  `ritual-liminality.md:5`; Kramrisch (1946) *The Hindu Temple*, 2 vols., U Calcutta, and Mannikka
  (1996) *Angkor Wat: Time, Space, and Kingship*, U Hawaiʻi Press — both registered at
  `cosmology-cosmography.md:9`; Pliny *Naturalis Historia* 28.18 (the *evocatio* of an enemy city's
  tutelary god — a place's deity as a transferable object) — registered via
  `divination-omen-systems.md`'s Pliny family; the Hajj/ihram row at `ritual-liminality.md:85`.
  The obvious modern shelf (`Eade & Sallnow`, *Contesting the Sacred*; Coleman & Elsner) is **not**
  registered in-corpus (measured 0 files) — an author must build on the Turner & Turner spine and
  the in-corpus civilization bases, or mark the rest `(to-verify)`.
- **Couples:** myth-symbol — `ritual-liminality.md`, `cosmology-cosmography.md`,
  `plant-symbolism.md`, `direction-symbolism.md`, `divination-omen-systems.md`,
  `calendar-festival-systems` (cross-partition); culture-material —
  `architecture-settlement-lexicon.md`, `transport-mobility-lexicon.md`,
  `calendar-festival-systems.md`; verification — `real-world-inspiration-boundaries.md`.
- **Filename:** `pilgrimage-sacred-geography.md`. Sorts cleanly (between
  `pantheon-archetypes.md` and `plant-symbolism.md`).

### R4 — Purity, pollution and the unclean: the boundary machinery — **SLOT ALREADY TAKEN, dispositioned not re-recommended**

This is the strongest gap on the pure demand-to-ownership evidence (54/220 files; three owners, none
of which owns the *code system*), and it was r35's MS-2
(`reports/round-35/scout/K01-coverage-census.md:228`). **Seat C02 drafted it concurrently, before
this fragment landed**, under the missing-dependency rule, as
`reports/round-42/cov/C02-entry-2.md` → proposed path
`corpus/knowledge/myth-symbol/purity-pollution-systems.md`. This seat therefore **confirms rather
than re-recommends** it, and records the collision check so the integrator does not receive two
drafts of one topic.

- **The gap, independently confirmed.** The partition *uses* Douglas everywhere and *owns* the
  system nowhere: `symbolism-synthesis-method.md:40` carries the Douglas row ("anomaly becomes
  pollution (1966) — where the grammar is violated the culture generates ritual response … **take
  the anomaly engine only**; her grid/group sociology is a separate theory"), `:68` states "**The
  anomaly picks your taboo** (Leach 1964; Douglas 1966): the animal that crosses a category boundary
  carries the pollution load", and `plant-symbolism.md:20` says the machinery transfers with a
  changed trigger and "**Do not re-derive the machinery**; couple to that file and change the
  trigger". Topic-ownership: `color-symbolism.md`
  owns colour's purity *valence* (its §4 white/mourning/purity braid at `:49-65`),
  `bathing-and-body-hygiene.md:48-52` owns the **status vs contamination split** and explicitly hands
  the status half on ("Ritual purity is about *status* … hygiene is about *contamination* …
  the leaks are the design work"), and `death-afterlife-eschatology.md` has a mourning/pollution
  window. None owns the code.
- **Collision check on C02's draft.** It declares its target path, its `- gap filled:` field and its
  couples in `reports/round-42/cov/C02-entry-2.md:3-21`, and it is a fenced draft (no corpus byte
  staged) — conforming to the shared rules. Its slug
  `purity-pollution-systems.md` does **not** collide with any of the 23 existing filenames
  (`sort -c` on the extended set passes) and does not collide with R1–R3 above. Its cited anchors
  (`symbolism-synthesis-method.md:40,:48,:68`; `animal-symbolism.md:9,:14,:46,:69,:75`;
  `plant-symbolism.md:20`) all resolve on disk at `ac47c78` — spot-checked this seat at `:40`, `:48`
  and `:68` and all three read as C02 says. **Recommendation: the integrator admits C02's draft for
  this slot and does not commission a second purity entry.**
- **Source shelf for the audit (already in-corpus).** Douglas (1966) *Purity and Danger*, Routledge
  — registered at `symbolism-synthesis-method.md:8`, `animal-symbolism.md:9`,
  `linguistics/politeness-taboo-euphemism.md:22`, `culture-material/bathing-and-body-hygiene.md:5`,
  and `synthesis/consistency-verification-checklist.md:3` (**five independent registrations**);
  Milgrom (1991) *Leviticus 1–16*, Anchor Bible — the rival non-hygienic reading, registered at
  `bathing-and-body-hygiene.md:5` and `cuisine-food-lexicon.md:8`, and the corpus already runs the
  Douglas/Milgrom calibration pair for dietary law at `cuisine-food-lexicon.md:6`; Steiner (1956) and
  Radcliffe-Brown (1939) "Taboo" (the Frazer Lecture, CUP) — registered together at
  `politeness-taboo-euphemism.md:21-22`, with the Steiner "charged, not forbidden" and
  Radcliffe-Brown "what is ritually dangerous is ritually significant" formulations at `:73`;
  Leach (1964) "Anthropological Aspects of Language: Animal Categories and Verbal Abuse" —
  registered at `animal-symbolism.md:9`; Harris (1974/1985) and Simoons (1961; 2nd ed. 1994) —
  `animal-symbolism.md:9`; Evans-Pritchard (1940) *The Nuer* — `animal-symbolism.md:9`.

### Alternates (ranked behind the four, one line each)

For C01/C03/C04 if the integrator rejects any of R1–R3, or if a fifth is wanted:

- **Spirit / demon / other-than-human taxonomy** (demand 164/220, 6 topic-owners but all
  incidental — spirit *helpers* in `animal-symbolism.md:53`, the *hau* in `ritual-liminality.md:47`,
  civilization bases). Highest raw demand of any candidate; the risk is that it overlaps
  `death-afterlife-eschatology.md`'s unquiet-dead section (`:95` D8 "the unquiet dead are a *status*,
  not a species") and `divination-omen-systems.md`'s possession cell — a draft would need a sharp
  boundary table. Sources in-corpus: Evans-Pritchard (1956) *Nuer Religion* at
  `binding-speech-complex.md:20`; the *jinn* vocabulary at `civilizations/arabia-pre-islamic.md:2`.
- **Monster / adversary catalogue** (demand 23/220, **0 topic-owners** for
  `monster`/`monstrous`/`terato`/`ogre`; `dragon` and `chaoskampf` are rows inside
  `hero-journey-variants.md:11-13` and `creation-myths-taxonomy.md`). Sources in-corpus: Watkins
  (1995) *How to Kill a Dragon*, OUP — registered **four times**
  (`hero-journey-variants.md:11`, `pantheon-archetypes.md:8`, `binding-speech-complex.md:12`,
  `linguistics/naming-systems.md:18`); Fontenrose (1959) *Python* is **not** registered (only his
  1978 *Delphic Oracle* is, at `divination-omen-systems.md:19`); Thompson Motif-Index B11 / ATU 300
  at `hero-journey-variants.md:12`; the combat-myth corpus (Enuma Elish, *Rigveda* 1.32,
  *Theogony* 820–880, the Bremner-Rhind papyrus) at `hero-journey-variants.md:13`. Thin demand —
  rank last.
- **Marriage / alliance symbolism** (demand 86/220, 5 owners, all material-culture by-product:
  `furniture-interior-lexicon.md`, `ritual-garments.md`, `sumptuary-law-rank-display.md`).
  `linguistics/kinship-terminology.md` owns the *terms* and
  `sacred-kingship-mythic-charter.md:4` touches "marriage-alliance into the divine line", but no
  entry owns marriage as a myth-symbolic institution. Source shelf thin in-corpus — would need
  outside registration.

## 5. Entry-contract inputs for the executors (C01–C04)

- **Head block, in filed order** (measured across all 23 at `ac47c78`): `# <Title> — <subtitle
  naming the payload>`; then `- gap:` or `- gap filled:` (new entries carry it — the four round-35
  landings all do); `- topic:` (**one long line**, the byte-source of the README row);
  `- sources:` as a nested bullet list (`  - `), not a single line; `- couples:` (ends with the
  handoff-target sentence naming lore-shokunin and disclaiming canon); `- source:` (locator summary —
  myth-symbol carries this, 23/23); `- verified-at:` (**prose, not a bare date** — names each item
  re-checked live, the tool used, and what was *not* re-consulted); `- recheck:` (names the trigger,
  not a date).
- **Body:** decision tables / typology tables / a build protocol / a numbered **decision record**
  section / a **calibration** section naming contested and discredited readings per
  `corpus/QUALITY.md:9-11`.
- **Admission bar** (`corpus/QUALITY.md:3-23`, five legs): provenance (to-verify inline, never
  laundered), calibration, coupling, usability, canon hygiene.
- **Hard constraints the wave has already tripped on:** every backticked repo path must resolve on
  disk or be marked `(to-verify)` on the same line; the `- couples:` field must be **single-line**
  (the wrapped-field hazard this round's claim O exists to fix); no canon writes; **fenced drafts
  only** — C01–C04 write `.md` fragments under `reports/round-42/cov/` and the integrator stages the
  bytes into `corpus/knowledge/myth-symbol/`.
- **README row:** the row text must be the entry's own `- topic:` text **byte-equal**
  (the rev-2.0/2.1/2.3 convention, `corpus/README.md:33-42`), added in **filename order**.
- **Filename sorting, verified.** R1–R3 plus C02's slug, merged with the 23 existing names, pass
  `sort -c` → a clean 27-name ordering. Proposed insertions:
  `dream-vision-trance.md` after `divination-omen-systems.md`;
  `mineral-stone-symbolism.md` after `hero-journey-variants.md`;
  `pilgrimage-sacred-geography.md` after `pantheon-archetypes.md`;
  `purity-pollution-systems.md` after `plant-symbolism.md`.

## 6. Index implications for C06 — and an independent confirmation of C08's vector defect

**The correct rev-2.4 delta.**

| object | before (measured at `ac47c78`) | after (4 landings) |
|---|---|---|
| `ls corpus/knowledge/myth-symbol/*.md \| wc -l` | 23 | **27** |
| corpus total | 220 | **224** |
| `## myth-symbol/` header | `(23)` at `corpus/README.md:196` | `(27)` |
| totals line | `Total knowledge entries: 220.` at `corpus/README.md:532` | `224` |
| footer | `(total 220 files; directory totals 25/23/25/29/24/94)` at `corpus/README.md:534-536` | `(total 224 files; directory totals 25/27/25/29/24/94)` |
| rows added | — | 4, in filename order, `- topic:` byte-equal |

**FINDING (this seat's own reading) — the declared vector is wrong, confirming C08 §5 D1
independently.** `reports/round-42/targets.json` (seat `C06` mission) declares the rev-2.4 vector as
`25/23/27/25/24/94`. Read in the **README's own section order** — which is what the footer is in, and
what the sweep enforces — that literal string is wrong twice:

```
PARTS = ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]
```
(`reports/round-28/readme/sweep.py:50-57`; confirmed live by that instrument's `footer_live.order`
field this seat.)

- slot 3 is **culture-material**, not myth-symbol. The literal vector moves culture-material
  25 → 27 and leaves myth-symbol at 23 — contradicting the same sentence's own *"myth-symbol 27"*.
- the literal vector sums to **218**, not the declared **224**.

The section-order-correct vector is **`25/27/25/29/24/94`**, which sums to 224 and matches the
section-order rule the sweep reads. **Recommendation to C06/integrator:** emit
`25/27/25/29/24/94`, not the literal `targets.json` string. This is a declaration defect in
`targets.json`, not a corpus defect — no filed byte needs editing, and this seat did not edit any.

**Verification path.** The claim's counting command is
`python3 -B reports/round-28/readme/sweep.py`, which at baseline returns exit 0 with
`rows 220 files 220` and `footer_ok True`; post-landing it must return `rows 224 files 224`,
`totals_line 224`, footer `(total 224 files; directory totals 25/27/25/29/24/94)`, exit 0. Second
counting command: `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 27. **Both are read-only; the
integrator runs them, not this seat** — and no `reports/round-*/run-validation.py` may be executed
in-tree.

## Owed

- **External source retrieval for R2 and R3 is owed, not done.** No network at seat time, so the
  scholarly shelf a *strong* dream/trance entry and a *strong* pilgrimage entry would want
  (Vitebsky, Bourguignon, Winkelman, Schieffelin, Lambek, Csordas for R2; Eade & Sallnow, Coleman &
  Elsner for R3) is **not registered anywhere in the corpus** — measured 0 files each. This seat
  could not register it and did not invent it. If C01/C03/C04 select R2 or R3, the author must
  either build on the in-corpus shelf this fragment names or mark the rest `(to-verify)` inline; the
  integrator should treat an R2/R3 entry built *without* that shelf as carrying a provenance debt
  under `corpus/QUALITY.md:3-6`. R1 (lithic) has **no such debt** — its whole shelf is already
  registered in-corpus, which is why it ranks first.
- **The purity slot's disposition is a recommendation to the integrator, not a decision this seat
  can make.** This seat confirms C02's draft is a fenced, collision-free, anchor-resolving draft for
  a confirmed gap; whether it is *admitted* is the integrator's and the auditors' call. At this
  seat's close `reports/round-42/cov/C08-verify.md` and `reports/round-42/cov/C07-verify.md` exist
  (C08 already carries FINDING D1, independently reproduced in §6); `reports/round-42/cov/C05-audit.md`
  and `reports/round-42/cov/C06-delta-receipt.md` were **not yet landed** — cited here as the
  prospective audit and delta seats, not as read artifacts.
- **The `targets.json` vector defect is reported, not repaired.** This seat writes only its own out
  path; the declaration correction belongs to C06/integrator. No filed byte was edited.
- Nothing else owed.

## Citations

- **Baseline**: `git rev-parse HEAD` → `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` (== declared
  baseline `ac47c78`, `reports/round-42/claims.json:7`); `git status --porcelain` at seat close →
  `?? reports/round-42/` only.
- **Partition counts**: `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 23; per-directory
  `ls corpus/knowledge/<d>/*.md | wc -l` → civilizations 94, culture-material 25, linguistics 25,
  myth-symbol 23, synthesis 29, verification 24 (sum 220).
- **Index green at baseline**: `python3 -B reports/round-28/readme/sweep.py` → `parts
  {"civilizations":94,"culture-material":25,"linguistics":25,"myth-symbol":23,"synthesis":29,
  "verification":24}`, `rows 220 files 220`, `missing_from_index 0 []`, `topic_mismatch 0 []`,
  `orphan_rows 0 []`, `header_drift {}`, `totals_line 220 totals_ok True`, `footer_ok True`,
  `readme_sha256 d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f`, **EXIT=0**;
  matches `sha256sum corpus/README.md`.
- **Add-history (the freeze)**: `git log --diff-filter=A --format="%h %ad %s" --date=short
  --name-only -- corpus/knowledge/myth-symbol` → `ce103bf` 2026-10-19 (round-35, 4 entries),
  `94ca098` 2026-10-17 (round-10, 3), `76c105b` 2026-10-17 (mint, 16).
- **Absence sweeps**: `.scratch/k02/sweep.py` (demand + topic-ownership over all 220 entries) and
  `.scratch/k02/sweep2.py` (topic-owners + first-hit lines), patterns printed in §3; plus
  `grep -rlEi -- "^- topic:.*\b<term>" corpus/knowledge/*/*.md | wc -l` for the term list in §3.
- **The lapidary hook**: `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:29` (bestiary +
  lapidary + numerology + heraldic code; White 1954, Hopper 1938, Fox-Davies 1909); the three
  owned components at `animal-symbolism.md:90` (bestiary), `number-symbolism.md:4` (numerology),
  `animal-symbolism.md:84-91` (heraldry); Hopper registered at `symbolism-synthesis-method.md:9`,
  White and Fox-Davies at `animal-symbolism.md:13`.
- **The Douglas / purity hooks**: `symbolism-synthesis-method.md:40` (Douglas row, verbatim
  quoted in §4.4), `:68` (anomaly picks the taboo), `:48` (the polarity-axis menu incl.
  `pure/impure`); `plant-symbolism.md:20` (the machinery transfers with a changed trigger: "Do not
  re-derive the machinery; couple to that file and change the trigger");
  `color-symbolism.md:49-65` (the white/mourning/purity braid);
  `culture-material/bathing-and-body-hygiene.md:48-52` (status vs contamination, "the leaks are the
  design work"); `linguistics/politeness-taboo-euphemism.md:21-22,73` (Frazer/Radcliffe-Brown/Steiner/
  Douglas).
- **The dream/trance hook**: `divination-omen-systems.md:64` (the natural/artificial axis table —
  *divinatio naturalis* = "frenzy, dreams, oracular possession"), `:89` (dream-oracle & incubation
  row), `:126` (dream-sanctuary institution), `:135` (the by-product rule), `:186` (the Dodds
  calibration, verbatim quoted), `:147-160` (the §8 boundary table that claims none of it);
  `animal-symbolism.md:53` (Eliade's spirit helpers; Hallowell 1926);
  `ritual-liminality.md:111` (pilgrim/monk/shaman as permanent liminal specialists);
  `culture-material/music-instrument-lexicon.md:96` (shaman's drum).
- **The pilgrimage hook**: `ritual-liminality.md:110` (pilgrimage caravan as the communitas
  generator), `:111`, `:118` ("Site the communitas: pilgrimage road …"), `:85` (Hajj/ihram),
  `:6` (**Turner & Turner 1978 *Image and Pilgrimage in Christian Culture* registered**);
  `culture-material/architecture-settlement-lexicon.md:67-84` (sacred building vocabulary);
  `plant-symbolism.md:15` (groves as legal objects);
  `cosmology-cosmography.md:9` (Kramsch 1946 / Mannikka 1996), `:36` (mountain/axis interface);
  `culture-material/transport-mobility-lexicon.md` (ROUTE as its first layer).
- **Lithic by-product data**: `culture-material/ritual-garments.md:59` (choshen, 12 gemstones);
  `civilizations/maya-classic.md:10,127` (Taube 2005 with DOI); `civilizations/china-shang-zhou.md:106`
  (Fu Hao jades); `civilizations/maori.md:13-14,20` (pounamu, Ngāi Tahu kaitiaki protocol, named
  knowledge-holder rule); `civilizations/siam-thai.md:126` (Emerald Buddha);
  `culture-material/funerary-material-culture.md:22` (Pliny 36.27, *sarcophagus*);
  `culture-material/vessel-container-lexicon.md` (Pliny 36.27 again).
- **Entry contract**: all 23 myth-symbol head blocks read this seat
  (`grep -oE "^- (gap|gap filled|topic|sources|couples|source|verified-at|recheck):"`); gap-field
  carriers = `binding-speech-complex.md:3`, `eschatology-world-end-systems.md:4`,
  `sacred-kingship-mythic-charter.md:4`, `death-afterlife-eschatology.md:3`,
  `plant-symbolism.md:3`; body/calibration bar at `corpus/QUALITY.md:3-23`.
- **Prior scouts**: `reports/round-39/scout/K01-verification-gaps.md:1-234` (the method mirrored,
  whose four recommendations landed at `corpus/README.md:8-12`);
  `reports/round-35/scout/K01-coverage-census.md:178-205` (the ownership test and its stated
  limits), `:223-236` (r35's MS-1…MS-9, of which MS-1, MS-5, MS-8 landed in round 35 and MS-2 is
  the purity slot dispositioned above).
- **Concurrent seat artifacts read**: `reports/round-42/cov/C02-entry-2.md:3-21` (the purity draft,
  its target path, gap field and anchors), `:214` (its own note on C08's D1),
  `reports/round-42/cov/C08-verify.md:135-157` (FINDING D1, independently reproduced in §6),
  `reports/round-42/plan/P01-plan.md:303-400` (the planner's ranked set, superseded by this
  fragment for the slug choice per that file's own fallback clause), `reports/round-42/scout/K01-n6-scout.md`
  (the O-claim scout, read for the wrapped-`couples:` hazard noted in §5).
- **Vector arithmetic**: `reports/round-28/readme/sweep.py:50-57` `PARTS`;
  `reports/round-42/targets.json` seat `C06` mission string `25/23/27/25/24/94`;
  `python3 -c "print(sum([25,23,27,25,24,94]), sum([25,27,25,29,24,94]))"` → `218 224`.
