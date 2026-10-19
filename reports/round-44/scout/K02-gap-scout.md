# K02 — gap scout (claim C): a fresh absence sweep at 223

- Seat: K02 | role: scout | claim: C | date 2026-10-19
- Baseline: HEAD `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`; `git status --porcelain` → only `?? reports/round-44/`
- Out path: `reports/round-44/scout/K02-gap-scout.md` (this file)
- Mission: run a FRESH absence sweep at the 223 total across all six partitions; name ONE genuinely unowned gap, verified by a topic-line + filename sweep at HEAD (not carried from any prior round); recommend partition + topic + source shelf; report commands and outputs.

**Result in one line:** the corpus has no entry that owns **cartography / mapmaking** — no filename, no `- topic:` line, and only by-product mentions (the sharpest being `cosmology-cosmography.md:71`, which explicitly distinguishes T-O symbolic diagrams from "survey maps"). Recommended landing: `corpus/knowledge/culture-material/cartography-and-mapmaking.md`, total 223 → 224.

---

## 1. Baseline measured (not asserted)

Commands run from the lane root on 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
c9f4eaa707b6e977ff6e1616463e91f4b8afea5d
$ git status --porcelain
?? reports/round-44/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
```

The round's own index sweep (read-only; its only writes are to disposable `.scratch` mirrors for its planted controls, `reports/round-28/readme/sweep.py:257,397`):

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

The independent inventory agrees: `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `"totals": {"files": 223, ...}`.

So the premise of claim C is true at baseline: **223 entries, six partitions, index green 223 == 223**.

---

## 2. Method — the ownership test, then the demand test

Two tests decide ownership, exactly as the claim words it:

1. **Filename test** — does any basename carry the domain's vocabulary?
2. **Topic-line test** — does any entry's single `- topic:` line name the domain as its subject?

A third, supporting test measures *demand* (how many files mention the domain in the body), but a body mention is **not** an owner: the corpus's own precedent is `mineral-stone-symbolism.md:3`, which landed the lithic register over 6 mineral and 24 lithic body mentions because every hit was a by-product or false-positive class, and `plant-symbolism.md:3`, which landed the flora register while fauna was owned. This report follows that precedent and dispositions every hit rather than treating a count as a verdict.

A candidate is disqualified as **carried** if any prior round's scout/gap/plan registry already named it. The registries read: `reports/round-19/gaps.md` (R19-C11..C20), `reports/round-35/scout/K01-coverage-census.md` (CM-1..CM-9, MS-1..MS-9), `reports/round-39/scout/K01-verification-gaps.md` (verification G1-G4), `reports/round-40/scout/K03-gaps.md` (linguistics E1-E4 + alternates), `reports/round-42/scout/K02-myth-gaps.md` (R1-R4 + alternates), the r36/r37/r38/r41/r43 scouts, and a global grep across `reports/`.

### 2.1 Candidate screen — what was eliminated, and why

| Candidate | Filename owner | Topic-line owner | Prior-round status | Verdict |
|---|---|---|---|---|
| Medicine / healing | 0 | 0 (3 incidental "medicine" phrases) | **named** r35 CM-4 (`K01-coverage-census.md:216`) and planned `medicine-healing-material` | **carried — reject** |
| Pastoralism / husbandry | 0 | 0 | **named** r35 CM-2 | **carried — reject** |
| Games / play / gambling | 0 | 0 | **named** r35 slot `games-and-play-material-culture` (`P01-c-plan.md:92`) | **carried — reject** |
| Intoxicants | 0 | 0 | **named** r35 CM-8 | **carried — reject** |
| Warfare logistics / siege | 0 | 0 | **named** r35 CM-7 | **carried — reject** |
| Incense / aromatics | 0 | 0 | **named** r35 slot 5 (`P01-c-plan.md:92`) | **carried — reject** |
| Dream / vision / trance | 0 | 1 (divination owns the reading technology) | **named** r42 R2 | **carried — reject** |
| Lithic / mineral | 0 (now 1) | 0 (now 1) | **landed r42** (`mineral-stone-symbolism.md`) | **owned — reject** |
| Pilgrimage / sacred geography | 0 | 1 | **landed r42** (`sacred-topography-pilgrimage.md`) | **owned — reject** |
| Purity / pollution | 0 | 1 | **landed r42** (`purity-pollution-boundary-systems.md`) | **owned — reject** |
| Law / dispute resolution | 1 (`sumptuary-law-rank-display.md`, dress law only) | 0 as a system | not named as a gap; high body coverage | viable alternate, but boundary-heavy (§7.2) |
| Rhetoric / oratory | 0 | 0 | not named | viable alternate, adjacent to `linguistic-anthropology.md` |
| Hunting / foraging | 0 | 0 | not named (r40 C01 used "hunting-manual" in an example only) | viable alternate, adjacent to agrarian/animal |
| **Cartography / mapmaking** | **0** | **0** | **not named in any registry; 7 global report hits, none a proposal** | **SELECTED** |

The r43 failure mode is explicitly screened here: the r43 lithic claim was blocked because `mineral-stone-symbolism.md` already owned its topic. Every candidate above was re-measured at the live 223 tree, not carried from the r43 premise.

---

## 3. The named gap: cartography and mapmaking

### 3.1 The claim

**The corpus owns space as cosmology, space as sacred route, and space as orientation code — but it does not own the made map: the survey chain, the projection, the drawing, the reproduction, and the map's use as a claim.** A map is not a picture of space; it is an argument about space made with a measuring chain, a projection, and a silence. That system has no file.

### 3.2 Filename test — zero owners

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0

$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
```

The only basenames that even brush the vocabulary are three false positives:

| basename | why it is not an owner |
|---|---|
| `synthesis/dialect-faction-map-workflow.md` | "map" is a **verb** — map dialect features onto networks; its `- topic:` (`:2`) is a lect workflow, not cartography |
| `myth-symbol/sacred-topography-pilgrimage.md` | "topography" is the **place register** (holy sites, routes), not map production |
| `myth-symbol/sacred-kingship-mythic-charter.md` | false positive on the substring `chart` inside "charter" |

### 3.3 Topic-line test — zero owners, eleven hits all dispositioned

```
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/
```

| Entry:line | The hit | Disposition |
|---|---|---|
| `linguistics/sound-symbolism.md:3` | "the three-way **map** (arbitrariness / iconicity / systematicity)" | metaphor — a conceptual schema, not a map |
| `linguistics/dialect-register-consistency.md:3` | "a built **dialect map**'s internal consistency" | metaphor — a lect inventory |
| `linguistics/sacred-registers-liturgical-language.md:3` | "how ritual events **map** to the competences" | verb |
| `myth-symbol/number-symbolism.md:3` | "a variance **survey**" | "survey" in the statistical sense |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | "purity is … a **boundary map**" | metaphor — the master claim of that entry |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | "sacred-geography **mapping** … as a diagram: radial, quartered, linear-corridor, or archipelago" | **nearest neighbour**; owns the sacred *place register* and the route, not the map-making chain (§3.5) |
| `culture-material/ritual-garments.md:3` | "the b.Arakhin 16a **atonement map**" | metaphor |
| `synthesis/dialect-faction-map-workflow.md:2` | "**Map** dialect features … onto travel networks" | verb |
| `civilizations/finnic-sami.md:3` | "gákti as an **identity map**" | metaphor |
| `civilizations/mesoamerica-primary-sources.md:3` | "a reference **map** for the four Mesoamerican bases" | metaphor |
| `civilizations/africa-primary-sources.md:2` | "a bounded **source map**" | metaphor |

**No entry names mapmaking as its subject.** Eleven hits, zero owners.

### 3.4 Body/demand test — every genuine cartographic mention is by-product

A tight vocabulary sweep over all 223 entries:

```
$ python3 - <<'PY'   # tight pattern, not the noisy bare "map"
pat = (cartograph|mapmak|portolan|cadastr|mappae|mappa mundi|surveyor|
       theodolit|compass rose|graticule|hereford mappa|lienzos?|
       stick chart|star chart|world map|map of|maps of|drawn map)
PY
TIGHT DEMAND: files=29 lines=35
```

Most of the 29 are the metaphor class already dispositioned above ("map of languages", "map of labor", "not a neutral map"). The **genuine cartographic footprint is seven files / nine lines**, and every one is a by-product or an explicit handoff:

| Entry:line | What it says | Why it is not ownership |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md:71` | T-O row: "Hereford Mappa Mundi c. 1300; T-O diagrams are **symbolic, not survey maps** (§10)" | **The partition's own disclaimer of the survey-map register.** Cosmography owns world models; it explicitly does not own survey maps |
| `myth-symbol/cosmology-cosmography.md:102` | "T-O diagrams are symbolic devices, **not cartographic**" | Same disclaimer, in the flat-earth calibration |
| `civilizations/mesoamerica-primary-sources.md:58` | "Lienzos and **cartographic histories** (Quauhquechollan, Tlaxcala, Coixtlahuaca) — cloth maps/migration-conquest accounts" | Owns the **source-survival/provenance** class; one row in a manuscript inventory |
| `culture-material/architecture-settlement-lexicon.md:95` | Roman castrum grid "surveyed with the **groma** … The grid is **cadastral**: a state that *measures land* builds this city" | Owns the **built city plan**; one sentence names the survey step as a handoff |
| `civilizations/japan-medieval-sengoku.md:157` | "a neat Edo **cadastral map** must not be treated as a direct Sengoku map" | A periodization caution, not a cartographic treatment |
| `myth-symbol/direction-symbolism.md:51` | "The **compass trap**: an abstract north requires deciding *which* north — true or magnetic … declination" | Owns **orientation coding**; the map's compass rose is a different object |
| `civilizations/polynesia-navigation.md:52,63,72,74` | horizon compass, steering-star sequence, sky mnemonic, **latitude**/landfall clue | Owns **navigation**; explicitly distinguishes these operations from a chart |
| `culture-material/timekeeping-instruments.md:50` | "**longitude at sea**" as an application of the minute | One cell in a timekeeping table |

Term-level counts (the honest small numbers):

```
cartograph     files=2  lines=2      # cosmography:71,102 + mesoamerica-primary-sources:58 (the word itself)
mapmaking      files=0  lines=0
portolan       files=0  lines=0
cadastral      files=2  lines=2      # architecture:95, japan-sengoku:157
mappa          files=2  lines=2      # cosmography:71 (Hereford Mappa Mundi), :102
survey map     files=1  lines=1      # cosmography:71 — the disclaimer
compass rose   files=1  lines=1      # direction-symbolism (orientation context)
graticule      files=0  lines=0
theodolite     files=0  lines=0
lienzo         files=1  lines=4      # mesoamerica-primary-sources only
```

**The demand is low in raw mentions — this is stated, not hidden.** The gap is not a high-demand omission like medicine or pastoralism (both r35-named and therefore carried); it is a **structurally named but unbuilt register**, the same shape as the r42 lithic gap: a partition's own method file draws a distinction and leaves one side unowned. Here the distinction is `cosmology-cosmography.md:71/:102` — symbolic world diagrams are owned; survey maps are explicitly *not*. The corpus also owns every adjacent production system (writing surfaces, instruments, measurement, route maintenance) but never the map that combines them.

### 3.5 Nearest-neighbour boundaries (binding for C01)

The new entry must **couple to, not restate**, these five:

| Neighbour | What it owns (cited) | The new entry's boundary |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | the five world-model axes (center / layer-count / direction-code / world-shape / age-doctrine); the T-O diagram as a **symbolic** device (`:71`, `:102`) | The new entry owns the **survey map** — the measured, projected, reproduced sheet. It cites the T-O row as the contrast case; it does not restate the world-model typology or the flat-earth calibration |
| `myth-symbol/sacred-topography-pilgrimage.md` | the holy-site typology, the route-as-rite, the three route types (fixed itinerary / votive ramble / circuit), the votive economy (`:5`, `:66-69`, `:124`) | The new entry owns **how the route is measured and drawn**; it cites the route types as content a map may carry, and does not re-own pilgrimage |
| `myth-symbol/direction-symbolism.md` | orientation frames, cardinal coinage, the true-vs-magnetic "compass trap" (`:51`) | The new entry owns the **map convention** (orientation choice, compass rose, north arrow) and cites `:51`; it does not restate the direction register |
| `culture-material/architecture-settlement-lexicon.md` | the city-plan lexicon, the Roman castrum grid and the groma sentence (`:95`) | The new entry owns **land survey as a map-production step**; it cites `:95` and does not restate the settlement vocabulary |
| `culture-material/writing-media-surface-economy.md` | the seven surface families and the cost ladder (`:3`) | The new entry owns **map-specific media and reproduction** (parchment/paper/cloth/copperplate; manuscript vs print; the atlas); it cites the surface economy and does not restate it |
| `civilizations/mesoamerica-primary-sources.md` | the lienzo/cartographic-history **source class** and its provenance (`:58`) | The new entry cites the genre; it does not restate the manuscript inventory |
| `culture-material/transport-mobility-lexicon.md` | routes, maintenance, the four-layer mobility system (`:28`, `:35`, `:117`) | The new entry owns the **representation** of routes; it cites the maintenance rule |

### 3.6 Prior-round non-carriage — measured, not assumed

- `reports/round-19/gaps.md` — ten declared gaps, all verification/synthesis; **no cartography row**.
- `reports/round-35/scout/K01-coverage-census.md` — CM-1..CM-9 (agriculture, pastoralism, mining, medicine, fuel/light, funerary, warfare logistics, intoxicants, bathing) and MS-1..MS-9 (afterlife, purity, spirit taxonomy, pilgrimage, sacred kingship, dream, ancestors, apocalypse, iconography); **no cartography row**.
- `reports/round-39/scout/K01-verification-gaps.md` — verification G1-G4; **no cartography**.
- `reports/round-40/scout/K03-gaps.md` — linguistics E1-E4 (taboo lifecycle, dialect consistency, translation fidelity, sacred registers) plus alternates (era-drift, epistolary); **no cartography**.
- `reports/round-42/scout/K02-myth-gaps.md` — R1 lithic, R2 dream/vision, R3 pilgrimage, R4 purity, plus alternates (spirit taxonomy, monster, marriage); **no cartography**.
- `reports/round-43/scout/K01-resolver-scout.md`, `K02-landing-scout.md` — operability claim only; **no C gap**.
- Global grep `grep -rniE '(cartograph|mapmak|portolan|cadastr|mappa|stick chart|world map)' reports/ --include='*.md'` → **7 hits**, all either copies of `mesoamerica-primary-sources.md` inside `reports/supplement-opencode-1/scratch/...` or the inherited-bibliography line at `reports/round-42/cov/C04-entry-4.md:62`; **none is a gap proposal**.
- Root lane docs (`LOG.md`, `MINT.md`, `SKILL.md`, `SHONEN.md`, `REGIMEN.md`, `SCORECARD.md`, root `README.md`, `AGENTS.md`, `PROVINCE.md`): no cartography mention; the one `LOG.md:1587` grep hit is the word "remappable", a false positive.
- `corpus/lessons/` — no rejected or proposed mapmaking entry.

**Conclusion: the gap is fresh at HEAD c9f4eaa and is not carried from any prior round.**

---

## 4. Recommendation

### 4.1 Partition and path

| Field | Recommendation |
|---|---|
| Partition | `culture-material/` (the partition that owns made systems: writing media, timekeeping, vessels, textiles, transport, craft) |
| Filename | `cartography-and-mapmaking.md` |
| Sort position | between `calendar-festival-systems.md` and `costume-semiotics.md` (verified: `ls corpus/knowledge/culture-material/` → calendar at position 5, costume at 6) |
| Count effect | culture-material 25 → **26**; total 223 → **224** |

`culture-material` is chosen over `synthesis` because this is a **made object system with a production chain and a vocabulary**, not a workflow; over `myth-symbol` because the map's symbolic content is already served by cosmography/sacred topography/direction, and the missing object is the instrument and the sheet; over `linguistics` because the map is not a language system, though its toponymy and legend grammar couple to `naming-systems.md`.

### 4.2 Topic seed (C01 may refine; the README row must stay byte-equal)

```text
- topic: the map as an instrument and a claim for fictional cultures — the survey → projection → drawing → reproduction chain that makes a map authoritative; the map-form typology (itinerary/strip, cadastral, chorographic, portolan, celestial, cosmographic, thematic, and the cartographic history/lienzo); projection and scale as claims about what matters; the symbol grammar (orientation, compass rose, scale bar, legend, boundary, blank); the reproduction economics (manuscript, woodblock, copperplate, the atlas); the map's silences and its use as a legal/territorial instrument; a build order, a decision record, a NON-CANON worked example, and a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory)
```

### 4.3 Craft claim and section outline

**Master claim:** *a map is an argument about space, not a picture of it — its authority comes from the survey chain behind it, and its politics from what it omits.* The map is the output of four load-bearing choices: **what is measured** (survey precision), **what is preserved** (projection and scale), **what is drawn** (selection and symbolization), and **who may copy and read it** (reproduction and access). The form follows the question, not the era: itinerary for the traveller, cadastral for the tax office, portolan for the pilot, cosmographic for the temple, thematic for the reformer.

Suggested sections (each ends in a design lever or a decision row, per `corpus/QUALITY.md:16-20`):

1. **The map's question** — what the map is for (navigation, taxation, ownership, pilgrimage, cosmology, war, memory, propaganda); the question fixes the form.
2. **Map-form typology** — itinerary/strip; cadastral/land register; chorographic/regional; portolan/nautical; celestial/star chart; cosmographic/world diagram; thematic (disease, resources, route); the cartographic history/lienzo as a genre. One real exemplar per form.
3. **The survey chain** — pacing, rope and chain, groma, dioptra, astrolabe, compass, cross-staff, plane table, theodolite, triangulation; line vs angle vs position; the error budget; the control network. Rule: a map can only show what the survey can measure at its scale.
4. **Projection and scale** — the sphere-on-plane problem; equirectangular, stereographic, Mercator, polar azimuthal, local plane; what each preserves and distorts; scale as a political decision; the legend of the omitted.
5. **Drawing and symbolization** — orientation (east/top, south/top, Mecca-centred, route-up), compass rose, scale bar, legend, boundary line, blank, monster, vignette; the map as a text to be read.
6. **Reproduction and the map trade** — manuscript vs woodblock vs copperplate vs lithography; cost per copy; the atlas as a commercial product; state monopoly, pirate copy, and the map as a legal instrument (treaty map, cadastral register, tithe map).
7. **The map's silences** — the unnamed village, the path that is not a road, the omitted sacred site, the replaced toponym; the blank as a licence; Harley/Wood on the map as a claim.
8. **Calibration bank** — "maps are neutral/objective" (discredited); "medieval maps were flat-earth" (discredited; T-O diagrams are symbolic, not survey maps — `cosmography-cosmography.md:102`); "portolan charts are photographically accurate" (overclaim); "indigenous maps are childlike/mental only" (discredited — lienzos are legal documents); "the map is the territory" (category error); "cartography diffused one-way from Europe" (contested; Chinese, Islamic, Mesoamerican and Polynesian traditions are independent/parallel).
9. **Build order** — (1) fix the question and the reader; (2) fix the survey precision; (3) fix projection/scale; (4) fix orientation; (5) fix the symbol set and legend; (6) fix the medium and reproduction; (7) decide the silences; (8) write the authority claim (who made it, for whom, by what warrant); (9) run the calibration audit.
10. **Decision record + NON-CANON worked example** — e.g. a river-delta culture's tax map: rope-and-groma survey, cadastral parcels, the blank where temple land is exempt, orientation to the river's flow, a cloth copy, and the dispute it settles. Table rows `DR-CM-01..` with reason and failure mode.

**What the entry must NOT do:** restate the cosmography five-axis typology; restate the pilgrimage route types; restate the direction register; restate the city-plan lexicon; restate the seven writing surfaces; restate the Mesoamerican provenance table; become a general history of cartography with no decision surface.

### 4.4 Source shelf

**Tier A — already registered in-corpus (reuse, cite by path:line):**

| Source | In-corpus registration |
|---|---|
| Smith, J. Z. (1987), *To Take Place*; Wheatley (1971), *The Pivot of the Four Quarters* | `cosmology-cosmography.md` `- sources:` block (the critique of universal centre claims) |
| Needham (1959), *Science and Civilisation in China*, vol. 3 (gaitian/huntian/xuanye; Kaogongji) | `cosmology-cosmography.md` `- sources:` |
| Horowitz (1998), *Mesopotamian Cosmic Geography* (Imago Mundi BM 92687, the Babylonian world map) | `cosmology-cosmography.md` `- sources:` |
| Russell (1991), *Inventing the Flat Earth* | `cosmology-cosmography.md:102` |
| Egeria, *Itinerarium*; Petrarch, *Itinerarium*; Ibn Jubayr, *Riḥla*; Ibn Baṭṭūṭa, *Riḥla* | `sacred-topography-pilgrimage.md:167-168` (editions marked `to-verify` there) |
| Rykwert (1976); Kostof (1991); Steinhardt (1990) | `architecture-settlement-lexicon.md:95-97` (surveyed city/grid context) |
| The [LIEN] lienzo record (UFM Quauhquechollan) and the cartographic-history row | `mesoamerica-primary-sources.md:28,58` |
| Navigation sources (horizon compass, star sequence, latitude) | `polynesia-navigation.md:52-74` |
| Surface-economy sources (media, cost, reproduction) | `writing-media-surface-economy.md:3` and its `- sources:` block |

**Tier B — external standard shelf (author/year/title confident; editions, volumes and page ranges `to-verify` at authoring — no network at seat time):**

- Harley, J. B., & Woodward, David (eds.), *The History of Cartography*, 6 vols. in 7, University of Chicago Press, 1987–2022 — the standard reference; vol. 1 (1987) for portolan charts and medieval maps, vol. 3 (2007) for the European Renaissance.
- Harley, J. B. (1989), "Deconstructing the Map," *Cartographica* 26(2): 1–20 — the map-as-claim argument.
- Wood, Denis (1992; 2nd ed. 2010), *The Power of Maps*, Guilford Press.
- Monmonier, Mark (1991; 3rd ed. 2018), *How to Lie with Maps*, University of Chicago Press.
- Jacob, Christian (French 1992; Eng. trans. 2006), *The Sovereign Map: Theoretical Approaches in Cartography throughout History*, University of Chicago Press.
- Ptolemy, *Geography*, trans. J. Lennart Berggren & Alexander Jones (2000), Princeton University Press — the projection/coordinate tradition.
- Campbell, Tony (1987), "Portolan Charts from the Late Thirteenth Century to 1500," in *The History of Cartography*, vol. 1 (page range `to-verify`).
- Edson, Evelyn (2007), *The World Map, 1300–1492: The Persistence of Tradition and Transformation*, Johns Hopkins University Press.
- Kain, Roger J. P., & Baigent, Elizabeth (1992), *The Cadastral Map in the Service of the State: A History of Property Mapping*, University of Chicago Press.
- Mundy, Barbara E. (1996), *The Mapping of New Spain: Indigenous Cartography and the Maps of the Relaciones Geográficas*, University of Chicago Press.
- Boone, Elizabeth Hill (2000), *Stories in Red and Black: Pictorial Histories of the Aztecs and Mixtecs*, University of Texas Press.
- Pickles, John (2004), *A History of Spaces: Cartographic Reason, Mapping and the Geo-Coded World*, Routledge.
- Buisseret, David (ed.) (1992), *Monarchs, Ministers, and Maps: The Emergence of Cartography as a Tool of Government in Early Modern Europe*, University of Chicago Press.
- Snyder, John P. (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395 — the projection families and their distortions.
- Dilke, O. A. W. (1971), *The Roman Land Surveyors*, David & Charles — the groma/centuriation chain.
- al-Idrisi, *Nuzhat al-mushtāq fī ikhtirāq al-āfāq* (1154) — edition/translation `to-verify`.
- *Tabula Peutingeriana* and the *Antonine Itinerary* — editions `to-verify`.
- Ortelius, *Theatrum Orbis Terrarum* (1570); Mercator's atlas — editions `to-verify`.

Every Tier B item must be marked `(to-verify)` for direct quotation/page reference in the entry, following the corpus's inherited-bibliography convention (e.g. `mineral-stone-symbolism.md:9`).

### 4.5 Calibration bank (the entry must flag each)

| Claim | Status | Why |
|---|---|---|
| "A map is a neutral, objective picture of space" | **discredited** | selection, projection, orientation, and omission are constitutive (Harley 1989; Wood 1992) |
| "Medieval people believed the earth was flat; T-O maps prove it" | **discredited** | sphericity was standard; T-O diagrams are symbolic, not survey maps (`cosmology-cosmography.md:102`; Russell 1991) |
| "Portolan charts are photographically accurate" | **overclaim** | they are practical sailing charts with their own distortions and conventions (Campbell; `to-verify` page-level) |
| "Indigenous maps are childlike or merely mental" | **discredited** | lienzos and cadastral histories are precise legal/territorial documents (Mundy 1996; Boone 2000) |
| "The map is the territory" | **category error** | a representation, not the thing; use as a design lever, not a metaphysics |
| "Cartography diffused one-way from Europe" | **contested** | Chinese, Islamic, Mesoamerican, and Polynesian traditions are independent or parallel (Needham; al-Idrisi; Mundy) |

---

## 5. Index and count implications (for C02 / C05 / X00)

Measured against the live README:

| Anchor | Current | After the landing |
|---|---|---|
| `corpus/README.md:234` | `## culture-material/ (25)` | `## culture-material/ (26)` |
| `corpus/README.md:240-241` | calendar row, then costume row | new row inserted between them, in filename order |
| `corpus/README.md:544` | `Total knowledge entries: 223.` | `Total knowledge entries: 224.` |
| `corpus/README.md:548` | `(total 223 files; directory totals 25/26/25/29/24/94)` | `(total 224 files; directory totals 25/26/26/29/24/94)` |
| `corpus/README.md:5` | revision 2.4 block at top | new revision 2.5 block above it, naming the r44 landing and the re-measurement |
| Post-landing sweep | `rows 223 files 223`, exit 0 | must read `rows 224 files 224`, 0 missing, 0 topic mismatch, `totals_line 224`, footer `25/26/26/29/24/94`, exit 0 |

**Pre-existing rev-2.4 prose defect, flagged for C02:** `corpus/README.md:11` reads "the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**". That vector sums to **217**, not 223, and it moves the myth-symbol +3 into the culture-material slot while cutting synthesis 29→25. The live footer (`:548`, measured by the sweep) is the correct `25/26/25/29/24/94`, which sums to 223. C02 should repair or explicitly supersede the rev-2.4 prose vector in the same edit if touched, and the rev-2.5 line must use the corrected `25/26/26/29/24/94`.

**Cross-claim ordering note (for X00/P01):** claim O's census artifact is measured on the **223-entry tree** (threshold 2556+166+0+7=2729 + 1 glob = 2730). Claim C's landing adds one file, making the tree 224. The O artifact should record `baseline_commit: c9f4eaa` and its 223-file denominator, and the round record should state that C's +1 entry is a **separate post-census delta** — do not silently re-run O's census over a 224 tree and present the numbers as the same measurement. If the integrator lands C before filing O's artifact, the artifact must say so and give both counts.

---

## 6. Handoff notes

### 6.1 C01 — entry drafter

- Use the scope boundaries in §3.5 and the outline in §4.3. The master claim and the nine-step build order are the entry's spine.
- Re-run the absence sweep on the **final keyword set** and record the counts in the entry's `- gap filled:` line, per the r35/r40 convention (`reports/round-35/scout/K01-coverage-census.md:200-205`). A claim of "no owner" without the fresh counts is the r43 defect.
- Make the `- topic:` line byte-equal to the README row description; the sweep compares them (`reports/round-28/readme/sweep.py`, `topic_mismatch`).
- Keep the entry reference/method only: no canon, no real-world clearance, no lore ruling (`corpus/QUALITY.md:18-20`; `PROVINCE.md` "Refuses").
- Do not restate the neighbours in §3.5; cite them by path:line and state the boundary.

### 6.2 C02 — README rev 2.5

- Header `:234` 25→26; row at `:241`; total `:544` 223→224; footer `:548` vector `25/26/26/29/24/94`; new revision block at `:5`.
- Repair or supersede the rev-2.4 prose-vector defect at `:11` (sums 217).
- Row description = the entry's `- topic:` text byte-for-byte.

### 6.3 C03 — source audit

- Audit every backticked path in the draft at HEAD c9f4eaa; my §3.4/§3.5/§4.4 citations are the starting set.
- Tier B editions/pages are `to-verify`; do not let the draft present them as inspected.
- The `cosmology-cosmography.md:71/:102` disclaimer is the single most load-bearing citation for the gap; re-read it live.

### 6.4 C04 — contract audit

- QUALITY clauses: provenance (every factual claim sourced; `to-verify` inline), calibration (the six-row bank in §4.5), coupling (the boundary table), usability (typology + decision tables + worked example), canon hygiene (handoff, no world decision).
- The gap is genuinely unowned per this sweep; the entry must preserve one-owner-per-topic by not absorbing cosmography/pilgrimage/direction/architecture.

### 6.5 C05 — collision verifier

- Independently enumerate `corpus/knowledge/culture-material/` at HEAD; confirm `cartography-and-mapmaking.md` is unused and no second entry owns the topic.
- Confirm the landing changes no other corpus file and no README row other than the one added.
- Confirm the sort position between `calendar-festival-systems.md` and `costume-semiotics.md`.

### 6.6 A01 — scope verifier

- The entry is a material-culture system entry, reference/method only; no canon, no lore decision, no packet surface, no culture profile. No new source of real-world rights/permission claims.

---

## 7. Risks and open items

1. **Adjacency to cosmography.** The T-O row is the nearest symbolic-map content. The boundary is explicit at `cosmology-cosmography.md:71` ("symbolic, not survey maps") and `:102` ("not cartographic"); C01 must quote it and not restate the five-axis typology. This is the main collision risk and it is answerable.
2. **Adjacency to sacred topography's "sacred-geography mapping … as a diagram"** (`:5`). The boundary: sacred topography owns the *place register and route*; the new entry owns the *survey → sheet* chain. The new entry may use the route types as map content, not re-own them.
3. **Low raw demand.** 29 files/35 lines with the broad pattern, but only 7 files/9 lines with genuine cartographic vocabulary, and several of those are disclaimers. This is stated honestly: the gap is a named-but-unbuilt register, not a high-demand omission. If the integrator prefers a high-demand gap, the ranked alternates are law/dispute resolution (0 owners, 56 "law" topic-line hits, but boundary-heavy), hunting/foraging (0 owners, 0 topic hits, adjacent to agrarian/animal), and rhetoric/oratory (0 owners, 0 topic hits, adjacent to `linguistic-anthropology.md`). All three would need their own fresh sweep and boundary table.
4. **Source editions.** No network at seat time; Tier B editions/volumes/pages are `to-verify`. The draft must not quote a page it has not inspected.
5. **Census ordering.** O's 223-denominator census and C's +1 landing must be recorded as two measurements, not one silently re-run number (§5).

## 8. Divergence with K04 and C01 — one gap must be chosen; the drafted one is carried

At my write cut the wave had already filed an independent second gap scout (K04) and a C01 entry draft. They diverge from this seat, and the divergence is material to claim C's text, so I record it rather than leave it to be discovered at integration.

| Artifact | Gap named | Status |
|---|---|---|
| `reports/round-44/scout/K02-gap-scout.md` (this file) | cartography / mapmaking | **fresh**; 0 prior-round proposals (§3.6) |
| `reports/round-44/scout/K04-gap-verify.md:10` | dream / vision / trance, `myth-symbol/dream-vision-trance.md` | **carried**: named by r42's K02 as R2 |
| `reports/round-44/cov/C01-entry-draft.md:1` | drafts K04's dream entry | a spare by its own terms (`C01-entry-draft.md:9`) |
| `reports/round-44/cov/C05-collision.md:10` | clears K04's dream slug | collision-clean ≠ fresh |

**The carried-gap evidence.** `reports/round-42/scout/K02-myth-gaps.md:216` is a headed recommendation: "### R2 — Dream, vision and trance: the altered-state complex and the institutions that license it". K04's own report acknowledges this at `reports/round-44/scout/K04-gap-verify.md:163`: "r42's K02 proposed R2 at `reports/round-42/scout/K02-myth-gaps.md:216-260`; the r42 landing set was the other three …". So the dream gap is not a fresh discovery at 223; it is a prior round's named gap that did not land. It is unowned — but it is **carried**.

**The claim's text is explicit.** `reports/round-44/claims.json:39`: "a gap with NO current owner (verified by a fresh absence sweep at the 223 total, **not carried from a prior round**)". The r43 defect this claim re-scopes was a stale premise; a carried gap is the same failure class, even when the ownership half happens to remain true.

**Decision for the integrator (one entry, not two).**

- If claim C lands **cartography** (this report): C01 must redraft to `culture-material/cartography-and-mapmaking.md`; C05 must re-clear that path and topic; C02 uses the culture-material vector `25/26/26/29/24/94` (§5). This satisfies the "not carried" clause on the evidence in §3.6.
- If claim C lands **dream/vision/trance** (K04/C01): the round record must name an exception to "not carried from a prior round" and justify it. On the claim's wording it does not qualify; C05's PASS is a collision result, not a freshness result. C02 would use myth-symbol 26 → 27 and vector `25/27/25/29/24/94`.
- **Do not land both.** Claim C's `after_required` is one entry, total 224 (`claims.json:41`); two landings would be 225 and would break both the claim and the README arithmetic.

K04's candidate table (`K04-gap-verify.md:61-71`) does not include cartography, so the two scouts are not in conflict on ownership — they tested different candidate sets. This seat's sweep is the only one that tested cartography; K04's is the only one that tested dream. The integrator has both.

## Owed

- none for this seat. The recommendation is a single gap with a measured zero-owner result, a source shelf, a boundary table, and a handoff. The only `to-verify` items are the Tier B editions/pages and the exact Campbell page range, which belong to C01/C03 at authoring time.

---

## Appendix — command transcript (trimmed)

```text
$ git rev-parse HEAD
c9f4eaa707b6e977ff6e1616463e91f4b8afea5d
$ git status --porcelain
?? reports/round-44/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/{civilizations,culture-material,linguistics,myth-symbol,synthesis,verification}/*.md | wc -l   # 223 (sum of partitions)
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; missing 0; topic_mismatch 0; orphan_rows 0; totals 223; footer 25/26/25/29/24/94; exit 0
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
totals.files 223

# filename ownership
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0

# topic-line ownership
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/
11 hits, all metaphor/verb/handoff — table §3.3

# genuine cartographic vocabulary
cartograph 2 files/2 lines; mapmaking 0; portolan 0; cadastral 2/2; mappa 2/2;
survey map 1/1; compass rose 1/1; graticule 0; theodolite 0; lienzo 1/4

# target path
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
No such file or directory
$ ls corpus/knowledge/culture-material/ | grep -nE 'calendar|costume'
5:calendar-festival-systems.md
6:costume-semiotics.md

# prior-round non-carriage
$ grep -rniE '(cartograph|mapmak|portolan|cadastr|mappa|stick chart|world map)' reports/ --include='*.md' | wc -l
7   # supplement scratch copies + one inherited-bibliography line; no proposal
```
