# C01 — cartography entry drafter A: sections 1–4 (fenced body)

- Seat: **C01**, role executor, claim **C** (`reports/round-47/targets.json`, seat C01).
- Round 47, loop 2, position 1; baseline `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` == `reports/round-47/claims.json` `baseline_commit` (`6e9a30d`).
- Out path: `reports/round-47/cov/C01-entry-a.md` (this file only).
- Writes: this file only. **No `corpus/**` byte is staged or edited.** The entry below is a fenced DRAFT for integrator application.
- Canon: **NON-CANON** engineering evidence. This seat drafts; it admits nothing, certifies no round, and decides nothing about any world.
- Section ownership: C01 = §1–4. C02 = §5–9 (survey-to-symbol chain, scarcity/prestige, mapmaker trade, provenance/charter, container-name fossil). C03 = §10–15 (build order, worked micro-example, calibration bank, decision record, recheck, scope). C04 = the head block. This fragment ends at §4 and does not write another seat's sections; cross-references to §5–§15 are to that division.

## A. Live re-verification of the gap and the partition at HEAD `6e9a30d`

All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

**A.1 Baseline and worktree state**

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
```

Only untracked report directories. No `corpus/` byte is dirty, so the partition measured below is the committed tree, not a half-edited worktree.

**A.2 Partition counts**

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
```

**A.3 Filename ownership — zero cartography owners**

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' -o -iname '*map*'
corpus/knowledge/synthesis/dialect-faction-map-workflow.md
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
```

The single `*map*` hit is a **verb**: its `- topic:` line (`synthesis/dialect-faction-map-workflow.md:2`) reads "Map dialect features and situational registers onto travel networks…" — a lect workflow, not cartography. No basename carries `cartograph`, `mapmaking`, `portolan`, or `cadastr`.

**A.4 Topic-line ownership — 13 broad hits, zero owners**

```
$ grep -rilE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bchart)' corpus/knowledge/ | wc -l
13
$ grep -rilE '^- topic:.*(cartograph|mapmak|portolan|cadastr|graticule|surveyor)' corpus/knowledge/ | wc -l
0
```

The 13 broad hits are all metaphor, verb, or an adjacent register. The three nearest are dispositioned in the boundary table (§1.1): `myth-symbol/sacred-topography-pilgrimage.md:5` (sacred-geography *mapping as a diagram* — the place register, not the survey sheet), `synthesis/dialect-faction-map-workflow.md:2` (verb), `myth-symbol/number-symbolism.md:3` ("a variance **survey**" — statistics, not land).

**A.5 Term-level demand — measured, small, and stated as such**

```
cartograph=2  mapmaking=0  portolan=0  cadastr=2  graticule=0  theodolite=0
compass rose=1  mappa mundi=1  survey map=1  lienzo=1  plane table=0  scale bar=0  prime meridian=0
```

The two `cartograph` hits are the partition's own disclaimer (`myth-symbol/cosmology-cosmography.md:71,:102`) and one source-class row (`civilizations/mesoamerica-primary-sources.md:58`). The two `cadastr` hits are `culture-material/architecture-settlement-lexicon.md:95` and `civilizations/japan-medieval-sengoku.md:157` (a periodization caution). The demand is low; this is a **named-but-unbuilt register**, not a high-demand omission — the same shape K02 documented at r44 and the shape `mineral-stone-symbolism.md:3` used for the lithic landing. The entry must not pretend the demand is large.

**A.6 Sort position and collision**

```
$ ls corpus/knowledge/culture-material/ | grep -nE 'calendar|costume'
5:calendar-festival-systems.md
6:costume-semiotics.md
```

`cartography-and-mapmaking.md` sorts between them. No existing entry is overwritten; the landing is an **A** (add), never an **M** (modify).

**A.7 Freshness at landing**

The r44 K02 scout (`reports/round-44/scout/K02-gap-scout.md` §3.6) found **0 prior-round proposals** for cartography; the r47 claim's own `before` line asserts the same and this seat re-measured ownership, not carriage. C05 (`cov/C05-freshness.md`) is the independent landing-time check. This fragment records its own reading only.

## B. Fenced entry body — sections 1–4

The bytes between the ` ```markdown ` opening fence line and the closing ` ``` ` line are the draft body. C04's head block precedes it; C02's §5 follows it. No triple-backtick fence appears inside the body.

```markdown
## 1. The frame: what this entry owns, and where the siblings stop

- **Master claim.** A map is an argument about space, not a picture of it. Its authority comes from the survey chain behind it; its politics from what it omits. The sentence this entry adds to the partition: **a map is a citation in cartographic form — the survey supplies its precision, the convention supplies its readability, the patron supplies its warrant, and the sheet pays for all three with the omissions it cannot show.**
- **The four load-bearing choices.** Every map answers four questions before it draws a line: **what is measured** (the survey's precision and its blind spots), **what is preserved** (the projection and the scale — angle, area, distance and bearing cannot all be preserved at once), **what is drawn** (selection and symbolization, including the boundary line and the blank), and **who may copy and read it** (reproduction, access, and the legal force of the copy). The four are one system: change the survey and the projection's distortions become visible; change the patron and the silences move.
- **What the corpus already owns, and why the sheet is still missing.** The corpus owns space as **world model** (`myth-symbol/cosmology-cosmography.md:71,:102`), as **sacred route and place register** (`myth-symbol/sacred-topography-pilgrimage.md:5,:69`), as **orientation code** (`myth-symbol/direction-symbolism.md:51`), as **built plan** (`culture-material/architecture-settlement-lexicon.md:95`), as **maintained route** (`culture-material/transport-mobility-lexicon.md:28,:117`), and as **name** (`linguistics/naming-systems.md:70` — "a map is an archive of coups"). No entry owns the **made map**: the sheet that composes those systems into a measured, projected, reproduced claim. That is this entry's object, and only that.

### 1.1 The boundary table — coupling, not restating

| Neighbour | What it owns (cited) | What this entry takes, and what it must not restate |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | the world-model axes (center / layer-count / direction-code / world-shape / age-doctrine); the T-O diagram as a symbolic device (`:71`, `:102`); toponyms as cosmographic claims (`:133`) | the **contrast case**: T-O is a cosmographic register, not a survey map. This entry cites `:71`/`:102` and owns the measured sheet; it does not restate the five axes, the flat-earth calibration, or the cosmogram typology |
| `myth-symbol/sacred-topography-pilgrimage.md` | holy-site typology, the route-as-rite, the three route types (`:5,:69`), the votive economy, the shrine institution | the **representation** of a route on a sheet, and the map as a pilgrimage document (itinerary, souvenir sheet, badge-map). The route grammar and the site typology stay there |
| `myth-symbol/direction-symbolism.md` | the direction register, cardinal coinage, the true-vs-magnetic "compass trap" (`:51`), circumambulation | the **sheet convention**: which way is up, the compass rose, the north arrow, the graticule. This entry cites `:51` for the declination problem and does not re-own the direction register |
| `culture-material/architecture-settlement-lexicon.md` | the city-plan lexicon, the Roman castrum grid and the groma sentence (`:95`), the sacred precinct | **land survey as a map-production step** and the plan as a cadastral object. This entry cites `:95` and does not restate the settlement or precinct vocabulary |
| `culture-material/writing-media-surface-economy.md` | the seven surface families and the cost ladder (`:3`) | the **map-specific media choice** (vellum, cloth, paper, copperplate, wall) as a use class and a trade class. This entry cites the surface economy and does not restate the seven families or their preparation chains |
| `civilizations/mesoamerica-primary-sources.md` | the lienzo / cartographic-history **source class** and its provenance rules (`:58`) | the genre as a map form and its legal-document status. The manuscript inventory and the copy-chain provenance rule stay there |
| `culture-material/transport-mobility-lexicon.md` | the route and its maintenance institution (`:28`), DR-TR-02 (`:117`) | **how a route is drawn** — the line, the stage, the toll, the impassable season. This entry cites the maintenance rule and does not re-own transport |
| `linguistics/naming-systems.md` | toponymy, critical toponymy as the inscription of power (`:40,:70,:97`) | the **toponym layer of the sheet** and the map as a naming archive. The name derivation table and the taboo machinery stay there |

- **One-owner statement.** The map is a **composition register**, not a symbolic register. The five canonical symbol registers (`myth-symbol/symbolism-synthesis-method.md:23`) own what a direction, color, number, animal or celestial body *means*; this entry owns only the **syntax of the sheet** — which register may occupy which cartographic slot, and what a blank means. That is why the entry belongs in `culture-material`: a map is a made object with a production chain, not a value system. It is also why the entry can be complete without owning any of its components.
- **Method statement (the partition's standing rule).** Everything below is reference knowledge and craft method. Nothing here decides what is true in any world. The handoff is to lore-shokunin, and the canon boundary is restated at the entry's close.
- **Why the object is load-bearing for fiction.** A map is the cheapest way to make power visible. It is also the cheapest way to make a *wrong* claim durable: the river that moved, the village that was not drawn, the boundary that was surveyed by the winning side. Scenes that need it are common — the treaty signed over a sheet, the cadastral dispute, the pilot's chart, the archive copy that contradicts the displayed copy.

## 2. What makes a map a register — the five-condition test

- **Definition used here.** A map is a **finite, conventional, ground-indexed selection of a referent space, made to answer a question, and legible as evidence to a reader who holds the convention.** "Ground-indexed" means the marks are declared to denote positions or features in a referent space under a stated correspondence — survey provenance, scale, and, where the culture has one, projection. The referent space need not be the earth: a star chart is a map of the sky under the same test.
- **Why the definition is a test and not a slogan.** Each clause excludes a different object that is often confused with a map. The test is useful precisely because most objects fail one clause, and the failure tells the designer what the object actually is.

| # | condition | what it requires | test question | fails when |
|---|---|---|---|---|
| 1 | **Ground index** | marks denote positions or features in a referent space under a declared correspondence (survey, scale, projection) | "what does this mark denote, and by what measurement?" | painting, diagram, cosmogram, mental image |
| 2 | **Bounded notation** | a finite, conventional mark vocabulary (point / line / area / text) with combination rules — the legend | "can I list the symbol set and its grammar?" | photograph, unkeyed sketch, private doodle |
| 3 | **Structural selection** | the sheet is finite at its scale; omission is constitutive, not accidental | "what is below the threshold, and who set it?" | survey field book, census table, sensor log |
| 4 | **Conventional readability** | a trained reader who holds the convention (orientation, scale, legend) | "who can read this without being told?" | cipher, private notation, ritual object |
| 5 | **Reproducibility / citability** | copies can be made and the sheet used as evidence in an argument | "can this be copied and cited in a dispute?" | unique ritual object, memory map, performative gesture |

### 2.1 The conjunction, object by object

| Object | 1 ground | 2 notation | 3 selection | 4 readable | 5 citable | Verdict |
|---|---|---|---|---|---|---|
| survey field book | yes | partial | **no** — records every measurement | yes (surveyor) | no | **not a map**: the map is the selection made from it |
| panel painting / landscape | **no** | yes | yes | partial | no | not a map: no declared ground index |
| T-O world diagram | **no** — no survey claim | yes | yes | yes | yes | not a survey map; a **cosmographic register**, owned by `cosmology-cosmography.md:71,:102` |
| itinerary list (stations, stages) | partial — route positions, no areal claim | yes | yes | yes | yes | a **route register**; becomes a strip map only when the list is given a spatial line |
| portolan chart | yes | yes | yes | yes (pilot) | yes | **map** |
| cadastral plan | yes | yes | yes | yes (clerk) | yes | **map** |
| star chart | yes (sky) | yes | yes | yes | yes | **map of a non-terrestrial referent** — the test is ground-indexed, not earth-indexed |
| Marshallese stick chart | **no** — swell and bearing, not position | yes | yes | yes | yes | **not a map under this test**: a navigation instrument that encodes swell interference, not a positional ground index (to-verify) |
| mental map | yes | yes | yes | yes | **no** | not a register artifact; the thing the sheet externalizes |

- **Read "partial" as a fail.** A partial on any clause is a fail for map status: the object is a neighbouring register (a route list, a survey record, a navigation instrument), and the table names what it is instead. The test admits maps and their neighbours, not partial maps.

- **The conjunction is the property.** The field book has a ground index but no selection; the painting has selection but no ground index. A map is the **conjunction** — and the conjunction is what gives it two powers at once: it can be *checked* against the ground, and it can be *tendentious* in its selection. Neither power is available to an object that fails one clause. That is what makes the map a register rather than a picture, a diagram, or a list.

### 2.2 Three consequences, and the one-owner rule

- **Consequence 1 — a map can be wrong.** Because it declares a ground index, a map can contradict the world: the river on the wrong side, the distance short, the boundary through a field. A cosmogram cannot be wrong in this way, because it claims no measurement. The checkable map is a fiction engine: the survey that was wrong, the copy that was corrected, the map that was right ten years ago.
- **Consequence 2 — no neutral map.** Because selection is constitutive, every map is an argument. The "neutral map" is a calibration item, not a design option (the calibration bank at §12 handles it; the axiom is enough here). The designer's question is never "should this map be tendentious?" but "whose interest does this selection serve, and does the culture admit it?"
- **Consequence 3 — the map is a legal instrument.** Because it is reproducible and citable, the sheet can be deposited, copied, signed, and produced in a dispute. The copy chain becomes evidence — the corpus's Mesoamerican source class states the rule exactly: "the copy chain is the evidence — record which copy you cite" (`civilizations/mesoamerica-primary-sources.md:58`). A map culture without a copy institution (archive, chancery, guild, library) has maps as objects, not maps as evidence.
- **The register-of-registers rule (one-owner discipline).** The sheet composes four registers it does not own: **direction** (orientation, the rose), **name** (toponymy), **number** (scale, coordinates, the graticule), and, where the culture has a color code, **color** (political fill). The map owns the *slot grammar*: which register may appear where, and what the absence of a mark means. A designer who needs a direction word goes to `direction-symbolism.md`; a place-name derivation to `naming-systems.md`; a measure to `numerals-and-measures.md` and `trade-economy-lexicon.md`. This entry never coins a component register; it only composes them.
- **The register audit — five questions before a sheet is called a map.**
  1. What referent space does it claim, and what is the stated correspondence? (ground index)
  2. What is the symbol set, and where is its grammar written? (notation)
  3. What is below the scale threshold, and who decided? (selection)
  4. Who can read it without being taught, and who must be taught? (competence)
  5. Can it be copied, and what does a copy certify? (citability)
- **The "map is the territory" error (and its design use).** The sentence is a category error, and the corpus should keep it as one: a map is a representation under a declared correspondence, not the referent. Its design use is diagnostic — a culture that *believes* the sentence, or a character who does, is making a claim about its own epistemology, and the plot consequence is the moment the ground disagrees with the sheet. Do not ship the sentence as a theory of maps; ship it as a belief a character can hold.

## 3. The map-meaning mechanisms — six decisions before a line is drawn

- The six mechanisms below are not a style menu; they are the decisions that give the sheet its meaning. They interact: the projection changes what the selection can show, the scale sets the omission threshold, the orientation sets the reader's first inference, and the cartouche claims the warrant for all of it. A designer who sets only the symbol set has drawn a decoration, not a map.

### 3.1 Selection — the first cut is an omission

- A map's first act is not to draw but to leave out. Three classes of omission are always present, and they are not the same decision:
  - **Below threshold** — the feature is too small for the scale (a hamlet on a 1:1,000,000 sheet). This is an engineering consequence, honest only if the scale is stated.
  - **Outside the frame** — the feature is beyond the sheet's extent (the neighbouring kingdom, the sea beyond the strait). The frame is a claim about relevance.
  - **Suppressed** — the feature is known and deliberately not drawn (the prohibited road, the village that pays no tax, the sacred site whose name may not be written). This is the political class, and it is where the map's silences become evidence.
- **The blank has three readings.** A blank may mean *unknown*, *empty*, or *forbidden*. The culture's convention must choose one per context, or the reader will choose for it — and the choice is a plot fact. A map that leaves the interior blank because it is unsurveyed is a different object from a map that leaves it blank because the survey was forbidden.
- **Design lever.** Write the three omissions and the reason for each. A map with no stated omissions claims completeness, and completeness is itself a political statement. The omission list is the map's thesis statement in negative.

### 3.2 Projection — the sphere-on-plane problem

- A sphere cannot be flattened without distortion. Every projection is a choice of what to preserve, and the choice is a claim about what matters. The standard families and their trade-offs:

| Family | Preserves | Distorts | Typical use | Real anchor |
|---|---|---|---|---|
| equirectangular (plate carrée) | a simple coordinate-to-grid mapping; latitude and longitude as straight rulings | area, angle and distance away from the standard parallels | world diagrams, thematic basemaps, teaching | standard family; Snyder 1987 (to-verify) |
| Mercator | angles and local shape (conformal); a constant bearing is a straight line | area, severely at high latitude; distance | navigation, sea charts | Mercator 1569 (to-verify) |
| stereographic | angles (conformal); circles map to circles | area and distance away from the center | polar maps, star charts, hemisphere diagrams | standard family; Snyder 1987 (to-verify) |
| azimuthal equidistant | distance and bearing from the center | area and shape away from the center | radio and aviation, polar strategy, "all distances from the capital" maps | standard family; Snyder 1987 (to-verify) |
| local plane / no formal projection | local shape and bearing over a small area | everything at scale; accumulating error | portolan charts, city plans, estate maps | portolan tradition (Campbell, to-verify) |

- **The pre-modern rule.** A map without a named projection is not a failed modern map; it is a different correspondence. The portolan chart's rhumb-line net is a **bearing** technology, not a projection; the strip map's line is a **sequence** technology, not a plane; the T-O diagram is a **doctrine**, not a survey. Ask what correspondence the sheet declares, not which projection it lacks.
- **Design lever.** Name what the map preserves and what it distorts, in the culture's own words if it has them. If the map is used for navigation or war, the distortion is a plot fact: the fleet that trusted the wrong grid, the border drawn on a projection that made a mountain range look like a straight line.

### 3.3 Scale — the ratio, the threshold, the error budget

- Scale is three numbers, not one: the **representative fraction** (1:50,000), the **smallest feature the sheet can carry** (a hamlet, a spring, a boundary stone), and the **largest positional error the survey can tolerate** (the width of a line, the thickness of a wall). The three are linked: a finer scale demands a finer survey, and a finer survey demands a more expensive chain.
- **The survey ceiling.** A map can only show what the survey can measure at its scale. If the culture surveys by pacing and rope, the sheet cannot honestly carry a parcel boundary finer than the pacing error; if it surveys by triangulation, it can. The production chain is the subject of §5–§9; here the rule is enough: **the scale is a promise the survey must be able to keep.**
- **The political scale.** A cadastral sheet at 1:2,500 makes the parcel visible and the province invisible; a strategic sheet at 1:1,000,000 makes the province visible and the parcel disappears. The scale decides which claims are *representable*, and therefore which claims can be made in the medium at all. A state that wants to tax parcels and a state that wants to move armies need different sheets, and a state that has only one will use it for the wrong purpose.
- **Design lever.** Choose the scale before the symbol set. The scale will delete the village; decide whether that deletion is the point.

### 3.4 Orientation — which way is up

- The frame's first claim is orientation. It is a convention, not a fact, and every convention carries a cosmology:
  - **East-up** — the T-O convention, with Jerusalem at the center (`cosmology-cosmography.md:71`); the direction of paradise and the rising sun.
  - **South-up** — attested in some Islamic and Chinese map traditions (to-verify for the specific cases); the qibla or the imperial axis can override it.
  - **Route-up** — the strip map's convention: the line runs in the direction of travel, and "up" means "onward" (to-verify; the *Tabula Peutingeriana* is the standard case).
  - **Centre-up** — the sheet organizes around a capital, a sanctuary, or the mapmaker's own city; the center is the claim.
  - **North-up** — the modern default, and a convention like any other; it became dominant with the print atlas and the marine chart (to-verify for the dating).
- **The compass trap.** If the culture has a compass, "north" is ambiguous: true north and magnetic north differ by declination, which is latitude- and era-dependent (`direction-symbolism.md:51`). A map that does not say which north it uses is not wrong — it is under-specified, and the under-specification is a scene: the pilots' north and the priests' north stop agreeing.
- **Design lever.** State the orientation and its reason. A map with east-up in a north-up culture is a dated object, a sectarian object, or both — and the reader can date it by the frame alone.

### 3.5 Symbolization — the legend is the contract

- The legend is where the map admits its conventions. A sheet without a legend is not necessarily illegible, but it is **unaccountable**: the reader must infer the grammar, and the inference is where meaning leaks.
- **The mark types.** Point (a settlement, a well, a shrine), line (a road, a river, a boundary), area (a province, a field, a sea), and text (a name, a number, a note). The combination rules are the map's syntax: a point inside an area is a settlement in a province; a line crossing a line is a crossing, a ford, or a dispute.
- **The boundary line is the most political mark on the sheet.** Solid, dashed, dotted, or absent; a line with a name or a line with no name; a line along a river or through it. The convention must be stated, because the same stroke can mean "the limit of surveyed land", "the limit of claimed land", and "the limit of land we admit exists".
- **The edge of knowledge.** The blank, the monster, the vignette, the "unknown" word, the question mark: each is a convention for uncertainty, and each says something different about the culture's attitude to the unknown. The monster is not a mistake; it is the map's way of marking that the survey stopped.
- **Color and fill.** Where the culture has a color code, the map may borrow it (political areas, grades of land, zones of danger). The map does not own the code; it cites `color-symbolism.md` and must not invent a color meaning the register does not license. A fill that contradicts the culture's color code is a legible error — useful, but only if the code is stable enough to be contradicted.
- **Design lever.** Write the legend as **rules**, not a list: "a point is a settlement only if it has a name; an unnamed point is a camp." The rules are what a reader can use, and what a forger can violate.

### 3.6 The authority claim — the cartouche, the signature, the warrant

- Every map makes a claim about itself, and the claim is usually written in the cartouche: who made it, when, for whom, by what warrant, and from what survey. The cartouche is the map's *cited* authority, and it is the first thing a reader should read.
- **The signature** is a maker's mark, and the corpus already owns the typology (`craft-artisan-lexicon.md:76`, the six-type mark taxonomy). The cartographer's signature can certify authorship, assay, license, or registry — the same types apply; this entry does not restate them.
- **The warrant** is the institutional claim: "surveyed by order of the king", "from the records of the cadastral office", "by the pilot who has sailed the strait for twenty years". A map without a warrant is a report; a map with a false warrant is a forgery; a map with a strong warrant is a legal instrument.
- **The map as a legal instrument.** The treaty map, the cadastral register, the tithe map, the boundary map: in each, the deposited copy is the legal object and the displayed map is the claim. The copy chain is the evidence (`mesoamerica-primary-sources.md:58`), and the archive that holds the copy holds the power.
- **Design lever.** Write the cartouche as a political sentence: who ordered the survey, by what right, against whom, and what the sheet is intended to settle. The sentence will generate the map's silences more reliably than any list of symbols.

### 3.7 The mechanisms are one system

- Projection changes what selection can show; scale sets the omission threshold; orientation sets the first inference; the legend admits the convention; the cartouche claims the warrant. A change in any one moves the others. The common design failure is to treat them as independent knobs — a beautiful projection with no survey behind it, a legend that promises a precision the chain cannot deliver, a cartouche that claims a warrant the archive cannot support.

### 3.8 Reading protocol — eight questions for any sheet

| # | Question | What it reveals |
|---|---|---|
| 1 | What is the frame, and what lies outside it? | the extent claim, and the first omission |
| 2 | What does the cartouche say, and who benefits from it? | the warrant and the patron |
| 3 | What is the scale, and what is below its threshold? | the precision claim and the second omission |
| 4 | Which way is up, and which north? | the orientation convention and its cosmology |
| 5 | What is the legend, and what is missing from it? | the symbol grammar and its gaps |
| 6 | What is shown, and at what density? | the selection's center of attention |
| 7 | What is blank, and which kind of blank? | the third omission — unknown, empty, or forbidden |
| 8 | Who reads it, and what do they do with it? | the use class, and the map's real genre |

## 4. Material and trade classes — the map-object typology

- **Form follows the question, not the era.** A culture does not "progress" from itinerary to atlas; it produces the sheet its institutions need. The eight forms below are a typology of *questions*, and the material and trade columns are what each question costs. A world with three forms and their institutions is richer than a world with eight forms and no reason for any of them.

### 4.1 The eight forms

| Form | The question it answers | The survey that feeds it | Typical medium | Who pays / who uses | Real exemplar | What it structurally cannot show |
|---|---|---|---|---|---|---|
| **Itinerary / strip map** | what comes next, and how far? | pacing, day-stages, landmarks, road stations | scroll, strip, road book | state post, pilgrim, merchant | *Tabula Peutingeriana*; the Antonine Itinerary (to-verify) | area, true direction, anything off the line |
| **Cadastral / land register** | who holds which parcel, and what is owed? | chain and rope, groma, boundary markers, assessor's roll | register book + plan | state, temple, estate | Roman cadastral grid (`architecture-settlement-lexicon.md:95`); Kain & Baigent's cadastral state (to-verify) | anything not taxable; the blank is an exemption |
| **Chorographic / regional** | what is in this region? | route traverse, compass, landmark triangulation, local report | printed sheet, atlas | state, publisher, learned society | Ortelius, *Theatrum* 1570 (to-verify) | micro-topography; often derivative from other maps |
| **Portolan / nautical** | what bearing, what hazard, what depth? | compass bearings, lead line, dead reckoning, observed latitude | vellum chart, later print | maritime city, pilot guild, chart-maker | late-13th-c. portolan charts (Campbell, to-verify) | inland; a formal graticule; positions it did not sail |
| **Celestial / star chart** | what is where in the sky? | angular observation, armillary, astrolabe, star catalogue | manuscript, print, globe | observatory, court, temple | Ptolemy's catalogue; Dunhuang star map (to-verify) | the ground; it is a map of a different referent |
| **Cosmographic / world diagram** | what is the shape of the whole? | doctrine, inherited report, and authority (no fresh survey) | manuscript, mosaic, print | temple, court, school | T-O diagram (`cosmology-cosmography.md:71,:102`) | anything measured — it makes no survey claim; the form belongs to `cosmology-cosmography.md` and is cited here as the contrast case, never restated |
| **Thematic** | where does X vary? | census, tax rolls, disease reports, geology, trade returns | printed sheet, colored | state, reformer, company, scholar | Snow's Broad Street map 1854; Minard 1869 (to-verify) | causation — it shows covariation, not cause |
| **Cartographic history / lienzo** | what is our claim, and what is our route? | memory, itinerary, boundary knowledge, colonial commission | cloth, painted sheet, codex | community, litigant, colonial court | Quauhquechollan, Tlaxcala (`mesoamerica-primary-sources.md:58`) | nothing European scale conventions can read directly; it is a legal document first |

- **The mixed forms are the normal case.** A cadastral sheet may carry an itinerary inset; a portolan may carry a cosmographic vignette; a lienzo may carry a European-style boundary line imposed by a colonial court. The typology is a set of questions, not a set of boxes, and the mixed object is evidence of a mixed institution.
- **What the typology is for.** It lets a designer ask "which question does my culture need answered?" before choosing a material. The answer fixes the survey, the medium, the patron, and the silences — and it prevents the common failure of giving a culture a *chart* when it needs a *register*.

### 4.2 The material classes — the sheet is a use class

- The map's medium is not decoration; it is a use class. The same information drawn on cloth, vellum, paper, a wall, or a copperplate is a different object with a different public:
  - **Cloth** — foldable, portable, durable, communal; the map that travels with a caravan or a community — the material fact behind the cloth-map word fossil that §9 owns.
  - **Vellum / parchment** — expensive, erasable, unique; the chart corrected by hand and kept by a guild.
  - **Paper** — cheap, copyable, ephemeral; the printed sheet and the pocket road book.
  - **Copperplate** — the plate is capital; reprints, corrections, and piracy are the trade's real history.
  - **Wall / floor** — monumental, public, non-portable; the map as state display, not tool.
  - **Clay / stone / metal** — durable, immobile; the boundary marker, the cadastral marker, the treaty plate.
- The surface economy is the sibling's subject (`writing-media-surface-economy.md:3`); this entry takes only the map-specific consequence: **the medium decides who can carry the map, who can correct it, and what survives to be copied.**

### 4.3 The trade classes — what a map is as an object of exchange

| Trade class | What is sold or held | Reproduction | Who can own or read | What the copy certifies | Failure mode |
|---|---|---|---|---|---|
| **Unique chart** | one manuscript copy, hand-corrected | none | guild, state, pilot | the maker's own survey | loss = knowledge loss; copying = espionage |
| **Printed sheet** | many copies, priced | press | public sale, literate buyer | the edition and the date | piracy; outdated copies outlive the correction |
| **Atlas** | a bound collection, sold by subscription | press | wealthy, learned, institutional | the collection's completeness | the atlas outlives its data — the fossil problem |
| **Globe** | a luxury instrument, hand-assembled | gores, hand-mounting | court, college, merchant prince | the maker's authority and the patron's taste | fragile; repairs are visible and datable |
| **Monumental map** | a wall, floor, or ceiling | none | public or elite viewers | the state's own claim | non-portable; becomes a monument, not a tool |
| **Pocket road book** | an ephemeral guide | press | traveller | the route's current state | worn out; low survival rate |
| **Cadastral register / plan** | an official record; certified copies | clerk copying | state, archive, litigant | the state's measurement | the copy is the legal object; the original stays in the archive |
| **Treaty / boundary map** | a signed instrument; deposited copies | few, certified | chancery, archive, signatories | the signature and the deposit | ambiguity is the point; the map is a weapon |

- **Access is the politics.** A map that only the palace can read is a different institution from a map sold at the fair. The trade class sets the readership, the readership sets the silences that can be maintained, and the silences set what the map can be used to do.

### 4.4 Design rules for the object typology

- **R1 — Pick the question first.** The form, the survey, the medium, and the patron follow from the question. A culture that needs a tax register and gets a sea chart has a decoration.
- **R2 — Match the material to the use.** A chart that gets wet needs vellum or cloth; a plan that gets annotated needs paper and margin; a boundary that must survive a dispute needs stone or a deposited copy.
- **R3 — Let the trade class set the access.** The copy institution is part of the map system: an archive, a chancery, a guild, a library, or a fair. Without one, maps do not accumulate and there is no map culture to speak of.
- **R4 — Two or three forms with institutions beat eight as decoration.** A culture with an itinerary, a cadastral register, and a cosmographic diagram has a complete spatial apparatus; a culture with all eight forms and no institution has a prop closet.
- **R5 — State the mixed forms.** The interesting objects are the hybrids — the cadastral plan with a pilgrimage inset, the lienzo with a European boundary line — and the hybrid is evidence of two institutions in contact.
```

End of C01's body. C02 continues at §5 (the survey-to-symbol chain). C03 owns §10–15.

## C. Handoff notes

### C.1 To C02 (§5–9)

- My §3.2 and §3.3 define the **promise** the production chain must keep (projection choice, scale as survey ceiling). §5 can take that as the spec and build the chain: instrument → measurement → control network → the sheet. Do not restate the projection families or the scale rule; cite §3.2/§3.3.
- My §4.1 gives the form typology and the survey-feed column. The **mapmaker trade** (§8) should treat the trade classes in my §4.3 as the object side and add the maker side: workshop, apprenticeship, guild, plate ownership, secrecy, and the chart-maker's liability. The division: I own *what the object is*, you own *who makes and sells it*.
- My §4.2 names the material classes and hands the surface economy to `writing-media-surface-economy.md:3`. The **container-name fossil** (§9) is yours; I deliberately did not write the *mappa* / *charta* etymology, though §4.2's cloth row is the material fact it will rest on.
- **Provenance/charter (§9)** should cite `mesoamerica-primary-sources.md:58` for the copy-chain rule and my §2.2 consequence 3 for the legal-instrument argument. The charter is the institutional form of the warrant I describe in §3.6.

### C.2 To C03 (§10–15)

- My §3 is the **mechanism inventory** the build order should sequence. Suggested mapping (you own the final order): question (§4.1) → survey ceiling (§3.3) → projection (§3.2) → orientation (§3.4) → symbol set and legend (§3.5) → medium and trade class (§4.2–4.3) → silences (§3.1) → cartouche/warrant (§3.6) → audit.
- My §2 is the **register test** the calibration bank should use for the "map = picture" and "neutral map" items. The five-condition test is also the audit instrument: a draft map that fails a clause is not a map, and the failure names what it is instead.
- The **worked micro-example** (§11) should use §4.1's form table and §4.3's trade class to place the example object; do not invent a ninth form.
- **Calibration bank (§12)** should carry at minimum: "maps are neutral/objective" (discredited), "medieval maps were flat-earth" (discredited; cite `cosmology-cosmography.md:102`), "portolan charts are photographically accurate" (overclaim), "indigenous maps are childlike/merely mental" (discredited; cite `mesoamerica-primary-sources.md:58`), "the map is the territory" (category error; my §3.6/§2.2), "cartography diffused one-way from Europe" (contested). I state the axioms; you own the bank and the status labels.

### C.3 To C04 (head block)

- The `- topic:` line should summarise §1's master claim, §2's register test, §3's six mechanisms, and §4's form/trade typology, in the culture-material house style (compare `writing-media-surface-economy.md:3`, `timekeeping-instruments.md:3`). Do not claim the entry owns cosmography, pilgrimage, direction, architecture, transport, writing media, Mesoamerican provenance, or toponymy.
- The `- gap filled:` line must carry the measured sweep, not an assertion. Use §A of this fragment: total 223, culture-material 25, filename owners 0, topic owners 0, 13 broad topic hits all dispositioned, term counts as listed, sort position between `calendar-festival-systems.md` and `costume-semiotics.md`, no existing entry overwritten.
- The `- couples:` line should name the eight neighbours in §1.1 plus, at minimum, `myth-symbol/symbolism-synthesis-method.md` (the five-register family this entry composes but does not join), `linguistics/numerals-and-measures.md` (measures), `culture-material/trade-economy-lexicon.md` (measure/money ladder), `culture-material/craft-artisan-lexicon.md` (maker's marks at `:76`), and `verification/to-verify-triage-protocol.md` (the to-verify routing). Every path must resolve at HEAD; C13 verifies.
- The `- sources:` block should register the Tier A in-corpus anchors I cite and the Tier B shelf from `reports/round-44/scout/K02-gap-scout.md` §4.4, each Tier B item marked `(to-verify)` for edition/page. **No external work was consulted in this seat**; do not let the header imply otherwise.
- The `- verified-at:` line should state the baseline `6e9a30d`, the commands in §A, and the no-network limit.
- The `- recheck:` line should trigger before any projection claim, any scale/accuracy figure, any orientation convention asserted as universal, any trade-class price, and any real-world map date.
- The `- scope:` line should state: map production and use only; no canon; the boundary table in §1.1 is binding.

### C.4 What I deliberately did not write

- No header fields (C04).
- No §5–9 production chain, scarcity/prestige, mapmaker trade, provenance/charter, or container-name fossil (C02).
- No build order, worked example, calibration bank, decision record, recheck, or scope section (C03).
- No README row, no revision block, no sweep staging (C09/C10).
- No DR-CM numbering. I use "design lever" and "R1–R5" only; C03's decision record should mint the DR-CM ids so the entry does not carry two numbering systems.
- No claim that the entry is a sixth *symbolic* register. §1's one-owner statement explicitly makes it a **composition** register in `culture-material`, not a member of the five-register family in `myth-symbol`.

## D. Citation self-audit

Every `path:line` in the fenced body was read live at HEAD `6e9a30d` in this seat. The table records what each citation says, so C06 can re-check rather than trust.

| Citation | Read at HEAD | What the line actually says / why it is cited |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md:71` | yes | T-O row: "east at top, Jerusalem center… Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, not survey maps (§10)" |
| `myth-symbol/cosmology-cosmography.md:102` | yes | "sphericity was standard… T-O diagrams are symbolic devices, not cartographic claims" |
| `myth-symbol/cosmology-cosmography.md:133` | yes | "Toponyms are cosmographic claims… A fictional map is a set of etymological arguments" |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | yes | the place-register topic line, including "sacred-geography mapping … as a diagram" |
| `myth-symbol/sacred-topography-pilgrimage.md:69` | yes | "The three route types" (fixed itinerary / votive ramble / circuit) |
| `myth-symbol/direction-symbolism.md:51` | yes | "The compass trap: an abstract north requires deciding *which* north — true or magnetic… declination" |
| `culture-material/architecture-settlement-lexicon.md:95` | yes | castrum grid "surveyed with the groma… The grid is cadastral: a state that *measures land* builds this city" |
| `culture-material/writing-media-surface-economy.md:3` | yes | the seven surface families and the cost ladder |
| `civilizations/mesoamerica-primary-sources.md:58` | yes | the lienzo/cartographic-history row; "the copy chain is the evidence — record which copy you cite" |
| `culture-material/transport-mobility-lexicon.md:28` | yes | "a route is only real if someone maintains it" |
| `culture-material/transport-mobility-lexicon.md:117` | yes | DR-TR-02, the maintenance clause for every named route and bridge |
| `linguistics/naming-systems.md:40` | yes | onomastics: anthroponymy, toponymy, theonymy, endonym/exonym |
| `linguistics/naming-systems.md:70` | yes | critical toponymy; "a map is an archive of coups" |
| `linguistics/naming-systems.md:97` | yes | place-name spelling shifted by a royal name taboo |
| `myth-symbol/symbolism-synthesis-method.md:23` | yes | the five canonical registers (color, animal, number, celestial body, direction) |
| `culture-material/craft-artisan-lexicon.md:76` | yes | the six-type signature/maker's-mark typology heading |

**Machine checks run this seat (output in §A):** `git rev-parse HEAD`; `git status --porcelain`; `find … | wc -l` (223); `ls … | wc -l` (25); the filename sweep; the topic-line sweeps (13 broad / 0 exact); the 13-term vocabulary count; the sort-neighbour listing; the target-path absence check. No command wrote outside this fragment; `TMPDIR` and `PYTHONDONTWRITEBYTECODE` were exported for every run; no `reports/round-*/run-validation.py` was executed.

## E. Known limits and open items

- **No network in this seat.** Every Tier B work (Snyder 1987, Mercator 1569, Campbell 1987, Ortelius 1570, Kain & Baigent 1992, Ptolemy, the *Tabula Peutingeriana*, Snow 1854, Minard 1869, the Dunhuang star map, the south-up and north-up dating claims, the Marshallese stick chart) is `(to-verify)` for edition and page. The body states the mechanisms the works document; it does not claim an inspected passage.
- **Projection mathematics is stated as mathematics**, not as a source claim: conformality of Mercator and stereographic, the area/distance distortion of equirectangular and azimuthal equidistant, and the impossibility of preserving angle, area, distance and bearing at once are geometric facts. Snyder is cited as the standard treatment, not as the origin of the facts.
- **The demand is low and the entry says so.** 2 `cartograph` files, 0 `mapmaking`, 0 `portolan`, 2 `cadastral`, and several of those are disclaimers. This is a named-but-unbuilt register, not a high-demand omission. If the integrator prefers a high-demand gap, the r44 K02 ranked alternates are law/dispute resolution, hunting/foraging, and rhetoric/oratory — each needing its own fresh sweep and boundary table. This seat did not test them.
- **Adjacency risk remains at cosmography.** The T-O row is the nearest symbolic-map content. My §1.1 and §2.1 make the split explicit and quote the disclaimer; the entry restates none of the five-axis typology. This is the main collision risk and it is answered by citation, not by silence.
- **Cross-reference numbering (§5–§15) assumes the C02/C03 division in `targets.json`.** If the assembler renumbers, the references in §3.3, §3.6 and §4.1 need a mechanical pass. The content does not depend on the numbers.
- **No collision found; the landing is an add.** `cartography-and-mapmaking.md` does not exist at HEAD; the sort position is between `calendar-festival-systems.md` and `costume-semiotics.md`; no existing file is modified by this draft. The integrator must still apply the entry as a new file and let C10's staged sweep confirm 224 == 224.
