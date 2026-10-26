# Cartography and mapmaking — the map as an argument about space: the survey chain, projection and scale, symbol grammar, reproduction, and the map's silences

- topic: the map as an instrument and a claim for fictional cultures — the survey → projection → drawing → reproduction chain that makes a map authoritative; the map-form typology (itinerary/strip, cadastral, chorographic, portolan, celestial, cosmographic, thematic, and the cartographic history/lienzo); projection and scale as claims about what matters; the symbol grammar (orientation, compass rose, scale bar, legend, boundary, blank); the reproduction economics (manuscript, woodblock, copperplate, the atlas); the map's silences and its use as a legal/territorial instrument; a build order, a decision record, a NON-CANON worked example, and a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory)
- gap filled: the corpus owns the world-picture, the sacred route, the orientation code and the built plan, and owns no made map. The boundary is the partition's own: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` defines cosmography as "the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)" — cosmography owns that world-drawn content; `:71` distinguishes the T-O diagram from "survey maps"; `:102` calls T-O diagrams "not cartographic"; `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:5` owns "sacred-geography mapping … as a diagram" and the route types; `corpus/knowledge/myth-symbol/direction-symbolism.md:51` owns the orientation register and the true-vs-magnetic "compass trap"; `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` owns the castrum grid and names the groma as the survey step. This entry owns the surveyed, projected, reproduced sheet as production — the chain from measured ground to an authoritative copy — and restates none of those registers. Fresh absence sweep, run 2026-10-19 from the lane root at HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (223 files; partitions 94/25/25/26/29/24): filename probe `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l` → **0**; slug `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → **No such file**; topic-owner probe `grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l` → **0** (the one wider-probe hit, `itinerar` in `sacred-topography-pilgrimage.md:5`, is a route type, not map production); term counts `mapmaking` 0, `portolan` 0, `graticule` 0, `theodolite` 0, `cartograph` **2 files / 2 lines** (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`), `cadastr` **2 files / 2 lines** (`architecture-settlement-lexicon.md:95`, `japan-medieval-sengoku.md:157`), `survey map` 1 line (`cosmology-cosmography.md:71`, the disclaimer). Demand is honestly low: this is a named-but-unbuilt register, not a high-demand omission. **Not carried:** the only prior proposal is `reports/round-44/scout/K02-gap-scout.md` (its §3.6 checked every prior registry); `reports/round-44/validation.json:9` records "the fresh gap (cartography, K02) has no entry body. No corpus delta"; `reports/round-45/` is absent and `reports/round-46/` has 0 cartography hits. The topic was re-confirmed FRESH by the r48 freshness gate at declaration (`reports/round-48/claims.json:21-24`).
- sources:
  - In-corpus anchors (repo-relative `path:line`, each re-read at HEAD `a01405d` on 2026-10-19; sha256 pinned for the eleven load-bearing files):
    - `corpus/knowledge/myth-symbol/cosmology-cosmography.md` (sha256 `165f292b95852459842900a091c6a40e1cd39b209b8fe2d84e62ecad6266ed2e`): `:27` "how the world is drawn (maps)" — the competing-definition sentence this entry must disposition; `:71` the T-O row, "symbolic, not survey maps"; `:102` "not cartographic". The world-model typology is **not** restated.
    - `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` (sha256 `241113b5a1259b04de889ebc458736ab8860e015b9afa9f74479bcc8bc165459`): `:5` "sacred-geography mapping … as a diagram" — the place register and route types, cited as map *content*, not re-owned.
    - `corpus/knowledge/myth-symbol/direction-symbolism.md` (sha256 `5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426`): `:51` the "compass trap" (true vs magnetic north, declination); `:26` in-world direction codes are "never … a compass rose with a legend" — the sheet's compass rose is designer tooling, and this entry cites the register rather than restating it.
    - `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` (sha256 `9af04e751206c32bc1ca38a73ef16a27a3e2e4a696454dd1bb5e22ed27bada9f`): `:95` the castrum grid "surveyed with the groma", "the grid is cadastral". The settlement vocabulary stays there; this entry owns land survey as a production step.
    - `corpus/knowledge/culture-material/writing-media-surface-economy.md` (sha256 `f039e6e120ed050ff16adebc0ad5cd9cff7965337799fe7cbc725ba0823d4601`): `:3` the seven surface families. This entry owns map-specific media and reproduction (parchment, paper, cloth, copperplate; manuscript vs print; the atlas) and cites the economy rather than restating it.
    - `corpus/knowledge/culture-material/transport-mobility-lexicon.md` (sha256 `86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70`): `:28` "a route is only real if someone maintains it". This entry owns the *representation* of a route, not the route institution.
    - `corpus/knowledge/culture-material/craft-artisan-lexicon.md` (sha256 `fd678d82fcc5134f5c5c0a65b15106b35cabe67bfd935d45df4fa16524f30288`): the workshop ladder at `:54-65` (`:54` the header; `:56-63` the systems; `:65` the design rule) — **not `:44`**, which is the steel-grading row (the r47 B4 miscite). `:3` is the topic-line summary only.
    - `corpus/knowledge/culture-material/trade-economy-lexicon.md` (sha256 `760a9df61364916b69e91c4d7f21ee4bff6bf138af6643f585afdcb10f05f277`): `:92` the Exchequer tally's stock/foil split; `:121` split-object authentication (`symbolon`, chirograph). The boundary case for the map as a legal instrument.
    - `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` (sha256 `d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530`): `:58` the lienzo / cartographic-history source class. Cited as a genre; the manuscript inventory is not restated.
    - `corpus/knowledge/linguistics/naming-systems.md` (sha256 `d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d`): `:70` "Every renaming is datable; a map is an archive of coups" — quoted **verbatim**; it is not paraphrased and no "correction" is owed (the r47 B3 false accusation is not repeated).
    - `corpus/knowledge/verification/calibration-registry.md` (sha256 `cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c`): `:50` the CAL-03 row; `:78-88` the strong-Whorf section. The calibration posture for a "maps determine thought" claim.
  - External standard shelf — **not consulted this round** (no network at seat time); author/year/title/publisher at book level, every edition, volume and page locator `(to-verify)`; no unread work is presented as inspected: Harley & Woodward (eds.), *The History of Cartography* (University of Chicago Press, 1987–) `(to-verify)`; Harley (1989), "Deconstructing the Map," *Cartographica* 26(2):1–20 `(to-verify)`; Wood (1992; 2nd ed. 2010), *The Power of Maps* (Guilford) `(to-verify)`; Monmonier (1991; 3rd ed. 2018), *How to Lie with Maps* (University of Chicago Press) `(to-verify)`; Jacob (French 1992; Eng. trans. 2006), *The Sovereign Map* (University of Chicago Press) `(to-verify)`; Ptolemy, *Geography*, trans. Berggren & Jones (2000, Princeton University Press) `(to-verify)`; Campbell (1987), "Portolan Charts from the Late Thirteenth Century to 1500," in *The History of Cartography* vol. 1 `(to-verify)`; Kain & Baigent (1992), *The Cadastral Map in the Service of the State* (University of Chicago Press) `(to-verify)`; Snyder (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395 `(to-verify)`; Dilke (1971), *The Roman Land Surveyors* (David & Charles) `(to-verify)`; Mundy (1996), *The Mapping of New Spain* (University of Chicago Press) `(to-verify)`; Needham (1959), *Science and Civilisation in China* vol. 3 (Cambridge University Press) `(to-verify)`; al-Idrisi (1154), *Tabula Rogeriana* / *Nuzhat al-mushtaq* `(to-verify)`; Russell (1991), *Inventing the Flat Earth* (Praeger) `(to-verify)`.
- couples: myth-symbol — `../myth-symbol/cosmology-cosmography.md` (owns the world model and the world-drawn/cosmogram content — `:27,:71,:102`; this entry owns the surveyed sheet and cites the disclaimer as its charter); myth-symbol — `../myth-symbol/sacred-topography-pilgrimage.md` (owns the holy-site typology and route-as-rite — `:5`; this entry owns how a route is measured and drawn); myth-symbol — `../myth-symbol/direction-symbolism.md` (owns the orientation register and the compass trap — `:51`; this entry owns the map convention: orientation choice, compass rose, north arrow); culture-material — `architecture-settlement-lexicon.md` (owns the built plan and the groma sentence — `:95`; this entry owns land survey as a map-production step); culture-material — `writing-media-surface-economy.md` (owns the surface families and cost ladder — `:3`; this entry owns map-specific media and reproduction); culture-material — `transport-mobility-lexicon.md` (owns route institutions and the maintenance rule — `:28`; this entry owns the representation of a route); culture-material — `craft-artisan-lexicon.md` (owns the workshop register and the ladder — `:54-65`; the mapmaker's shop is a craft case in those terms); culture-material — `trade-economy-lexicon.md` (owns measures, weights, contract vocabulary and split-object authentication — `:92,:121`; this entry owns the map as a legal/territorial instrument); culture-material — `timekeeping-instruments.md` (owns the instrument families, including `:50` longitude at sea; this entry owns the coordinate problem the map inherits); culture-material — `material-culture-inference-method.md` (owns the perishability constraint `:69` and the anti-determinism guard `:76`; applied here to map survival and to "the map caused the state"); culture-material — `vessel-container-lexicon.md` (owns containers as documents and chronometers — `:115`; the map roll and archive chest are storage, cited at the boundary); linguistics — `../linguistics/naming-systems.md` (owns toponymy — `:70`; the map's place-names are that file's assignment, not this entry's); civilizations — `../civilizations/mesoamerica-primary-sources.md` (owns the lienzo source class — `:58`; cited as genre, inventory not restated); civilizations — `../civilizations/japan-medieval-sengoku.md` (owns the Edo-cadastral periodization caution — `:157`); civilizations — `../civilizations/polynesia-navigation.md` (owns horizon compass and steering-star operations — `:52`; navigation is explicitly not a chart); myth-symbol — `../myth-symbol/celestial-symbolism-calendars.md` (owns the sky as a symbolic system — `:3`; the star chart is a map form here, not sky myth); myth-symbol — `../myth-symbol/sacred-kingship-mythic-charter.md` (owns mythic charter and legitimation — `:70`; the map's warrant is cited as a legal charter); verification — `../verification/calibration-registry.md` (owns the calibration posture — `:50` CAL-03; a "maps determine thought" claim is braked with the same test); verification — `../verification/real-world-inspiration-boundaries.md` and `../verification/myth-consistency-gate.md` (own the restricted-knowledge boundary; every living tradition's restricted map or songline is routed there before any table is filled); synthesis — `../synthesis/worldbible-integration-contract.md` (handoff target; this entry records nothing in canon).
- source: lane-side authority is the in-corpus `path:line` anchor list above (each re-read at HEAD `a01405d`, 2026-10-19) plus the absence-sweep commands recorded in `- gap filled:`; the external frameworks are the shelf above, **none fetched or inspected this run** (no network at seat time), so every edition, volume and page locator carries `(to-verify)` — the shelf supports mechanisms, never a claim about any fictional world. The four-choice spine (what is measured / what is preserved / what is drawn / who may copy and read), the form typology, the symbol grammar and the build order are this lane's design method assembled from those sources.
- verified-at: 2026-10-19 — draft written at HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`; equal to `reports/round-48/claims.json` `baseline_commit` `a01405d`). Measured with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: `find corpus/knowledge -name '*.md' | wc -l` → **223**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **25**; `python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, missing 0, topic_mismatch 0, orphan_rows 0, header_drift {}, totals_line 223, footer `25/26/25/29/24/94`, exit 0; `corpus/README.md` sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`. Every in-corpus `path:line` in this head block was checked mechanically in this seat: **23/23** needle-in-line assertions passed over 22 distinct anchors, and **19/19** `- couples:` targets resolve relative to `corpus/knowledge/culture-material/`. The slug is unused; the README sort position is between `calendar-festival-systems.md` (5th) and `costume-semiotics.md` (6th). **Not claimed:** any portolan accuracy figure, any projection-distortion value, any print-run or price, any survival percentage, any external edition, volume or page.
- recheck: before any map, survey or territorial claim becomes load-bearing — re-run §3's and §5's arithmetic (the sec φ / cos φ / error-budget figures are arithmetic; the exemplar dates are not) and re-read `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102` before repeating any flat-earth/T-O calibration and `:71` before letting a symbolic diagram stand in for a survey map; re-read `:27` before claiming cosmography does not own "how the world is drawn"; re-read `corpus/knowledge/myth-symbol/direction-symbolism.md:51` (and `:26`, which denies the compass rose as an emic direction code) before fixing true north, magnetic north or an east-at-top convention; re-read `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` before treating a castrum grid as a survey (the grid is a plan; the groma is the chain); re-read `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58` before citing a lienzo as evidence of a cartographic practice; re-read `corpus/knowledge/culture-material/material-culture-inference-method.md:69` before treating a surviving map as evidence of its own importance (parchment and vellum survive; cloth and bark do not); re-read `corpus/knowledge/culture-material/transport-mobility-lexicon.md:28` before drawing a route no institution maintains; and route every living tradition's restricted map or songline through `corpus/knowledge/verification/real-world-inspiration-boundaries.md:6` and `corpus/knowledge/verification/myth-consistency-gate.md:34` before filling any table. Corrections to this entry are a new section or a new entry, never a rewrite.
- scope: reference method and lane policy for the culture-material partition. This entry owns the map as a made instrument and a claim — the survey chain, projection and scale, symbolization, reproduction, and the map's silences. It does not own the world model or the cosmogram (`../myth-symbol/cosmology-cosmography.md`), the holy-site typology and route-as-rite (`../myth-symbol/sacred-topography-pilgrimage.md`), the direction register (`../myth-symbol/direction-symbolism.md`), the settlement vocabulary (`architecture-settlement-lexicon.md`), the writing-surface economy (`writing-media-surface-economy.md`), the vehicle-and-road system (`transport-mobility-lexicon.md`), or toponymy (`../linguistics/naming-systems.md`). It decides nothing about any world — no border, charter or survey is authorized by this file — and issues no verdict about any round, record or artifact. Canon recording and consistency verification belong to lore-shokunin; the entry ends at the handoff.

## 1. The register property: a map is an argument about space

**Master claim.** A map is an argument about space, not a picture of it. Its authority comes from the survey chain behind the sheet, and its politics from what the chain and the draughtsman leave out. Every sheet makes four load-bearing choices, and the order matters:

1. **What is measured** — the survey precision and the control network. A map cannot be more precise than its weakest measurement.
2. **What is preserved** — the projection and scale. Every sheet trades shape, area, distance or bearing; none keeps all four.
3. **What is drawn** — selection, symbolization, orientation, and the blank.
4. **Who may copy and read it** — reproduction, warrant, and access.

**The five-condition test** decides whether an object belongs to this register. Apply it object by object; a partial pass is a fail, and the failure names what the object is instead.

1. **Referent index** — the object asserts positions or relations in a referent space under a declared correspondence — terrestrial or celestial; the space need not be traversable.
2. **Bounded notation** — it uses a finite, conventional set of marks, not free depiction.
3. **Structural selection** — it omits by a rule, not by accident.
4. **Conventional readability** — a competent reader in the culture can recover the code without the maker present.
5. **Reproducibility/citability** — copies can be made and compared, so the sheet can serve as evidence.

The failures are diagnostic, not dismissive: a **field book** has index and notation but no conventional readability (private evidence, the map's raw material); a **landscape painting** depicts but has no bounded notation; an **itinerary list** has index but no area (a route list — the strip map drawn from it is the form that passes); a **star chart** passes here (the sky is a referent space under a declared coordinate frame); a **T-O diagram / cosmogram** passes here too — but only as a **boundary form**, admitted to §4 because its correspondence is doctrinal, not measured (`cosmology-cosmography.md:71,:102`); a **mental map** fails reproducibility (an informant's testimony, citable as such).

## 2. One-owner boundary

Cosmography owns the world-drawn content — how the world is drawn, named, walked and built (`cosmology-cosmography.md:27`) — and explicitly disclaims survey maps (`:71`, `:102`). This entry owns the **surveyed, projected, reproduced sheet as production**. Stating both halves is the one-owner proof: a strict reading of `:27` would otherwise ask why "drawn (maps)" is not already an owner.

| Neighbour | What it owns (live anchor) | This entry's boundary |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | world model, five axes, T-O as symbolic device (`:27,:71,:102`) | the measured, projected, reproduced sheet; T-O cited only as contrast |
| `myth-symbol/sacred-topography-pilgrimage.md` | holy-site typology, three route types (`:5,:69`) | how a route is surveyed and drawn; does not re-own pilgrimage |
| `myth-symbol/direction-symbolism.md` | orientation code, true-vs-magnetic trap (`:51`) | the map convention (north arrow, rose, frame); cites the trap |
| `myth-symbol/celestial-symbolism-calendars.md` | the sky as symbolic system (`:3`) | the star chart as a map form; does not restate sky myth |
| `culture-material/architecture-settlement-lexicon.md` | settlement lexicon, castrum grid, groma (`:95`) | land survey as a production step; does not restate building words |
| `culture-material/writing-media-surface-economy.md` | seven surface families, cost ladder (`:3,:73,:78`) | map-specific media and reproduction; cites the cost rule |
| `culture-material/transport-mobility-lexicon.md` | route institutions, maintenance (`:28,:117`) | representation of a route; cites the maintenance rule |
| `linguistics/naming-systems.md` | toponymy, critical toponymy (`:40,:70`) | the toponym layer on the sheet; quotes `:70` exactly |
| `culture-material/craft-artisan-lexicon.md` | workshop ladder, guild systems (`:54-65`) | the mapmaker's role set; does not restate the ladder |
| `culture-material/trade-economy-lexicon.md` | market, measure, contract vocabulary (`:92,:121`) | the map as legal/territorial instrument; does not restate contract words |
| `civilizations/mesoamerica-primary-sources.md` | lienzo source class and provenance (`:58`) | cites the genre as a map form; does not restate the inventory |
| `myth-symbol/sacred-kingship-mythic-charter.md` | mythic charter and legitimation (`:70`) | the map's warrant as a legal charter; does not restate legitimation |

## 3. The survey-to-symbol chain

Seven links. Each can fail the whole sheet; the sheet's authority is its weakest link, not its best instrument.

| Link | Question | Artifact | Failure mode |
|---|---|---|---|
| 1 select | what is the map for, and who reads it? | question brief | a sheet answering no question |
| 2 measure | what is measured, to what precision? | field book | precision the survey cannot deliver |
| 3 control | tied to what fixed points? | control sketch | a sketch with no frame |
| 4 reduce | how do observations become positions? | computation book | error propagation unrecorded |
| 5 project | what is preserved? | projection note | a projection claim the sheet cannot support |
| 6 symbolize | what does each mark mean? | legend/key | private notation |
| 7 reproduce | who copies, and how faithfully? | production spec | copies that drift or cannot be compared |

- **Control first.** A survey tied to nothing is a sketch. The control network — trig points, towers, dike markers, known gates — is the political infrastructure of the map: whoever owns the fixed points owns the frame.
- **Error budget.** State the error at the scale the map is read. A traverse closing to 1% on 100-pace legs carries ±0.75 m (a pace taken here as 0.75 m, a design convention); a 1:5,000 sheet's 0.2 mm line is 1 m of ground, so the survey is just inside the graphic limit, while at 1:2,500 (0.2 mm = 0.5 m) the survey becomes the binding error. Angular work: 1 arcminute at 10 km is ≈2.9 m of position. A survey closing to 200 m cannot support a 1:50,000 sheet whose 0.2 mm line is 10 m: the sheet would assert 10 m from evidence good to 200 m, a **20× overstatement**.
- **Field book vs fair copy.** The field book is evidence (dated observations, instrument, observer); the fair copy is the claim. A map without its field book has warrant without record.
- **Instruments map to forms, not to progress:** groma (right angles, centuriation), dioptra (sightlines, level), astrolabe/cross-staff (altitude → latitude), plane table (direct plotting), chain/rope (distance), compass (bearing), theodolite (angles at scale). Instrument histories are `(to-verify)`.

## 4. Form follows the question: eight map forms

The form is chosen by what the reader must decide, not by the era. One polity can make a cadastral sheet and a cosmogram in the same century.

| Form | Question it answers | Real exemplar (`to-verify` for edition and date) | Structurally cannot show |
|---|---|---|---|
| itinerary/strip | how do I get there? | *Tabula Peutingeriana* (13th-c. copy) | area, off-route relations, true relative distance |
| cadastral/land register | who owes what on which parcel? | Roman centuriation (centuria ≈ 710 m square ≈ 50 ha); Kain & Baigent | terrain, use rights it does not tax |
| chorographic/regional | what is this province like? | (to-verify) | precise position; it is an impression |
| portolan/nautical | bearing and distance to the next port? | Carte Pisane, late 13th c. | inland, high latitudes; its construction is contested — it makes no *stated* projection claim |
| celestial/star chart | where is the sky at this hour? | Dunhuang star chart, c. 700 CE | ground position; time-bound |
| cosmographic/world diagram | what is the shape of the world? | T-O diagram; Hereford Mappa Mundi, c. 1300 | survey; it is symbolic — a boundary form whose correspondence is doctrinal, not measured |
| thematic | where is the thing I care about? | Minard 1869; Snow 1854 | the base it suppresses |
| cartographic history/lienzo | what is our claim and our route? | Quauhquechollan, 16th c. | neutral position; it is a legal/memory document |

**Minimum credible build per form** (the eight forms above, not a sample):

- itinerary: stations + distances + a direction convention; can skip area and scale.
- cadastral: parcel geometry + tenure + a levy rule; can skip terrain.
- chorographic: a selection rule + one scale bar; can skip trig control.
- portolan: named ports + bearings + a distance convention; can skip projection.
- celestial: an epoch + a coordinate frame + a star list; can skip ground.
- cosmographic: a world shape + a center + a convention; can skip survey entirely.
- thematic: one variable + a base + a classing rule; can skip everything not the theme.
- lienzo: a claim + a route + witnesses; can skip neutral position.

**Rule:** choose the form by what you are willing to lose. The "cannot show" column is the design tool — a form that claims everything is a form with no question.

## 5. Projection, scale, orientation: three claims the sheet makes

| Projection | Preserves | Distorts | Use |
|---|---|---|---|
| equirectangular | a simple lat/long grid | area by cos φ (a degree of longitude is 111.3 km at the equator, 55.7 km at 60°) | small-scale index sheets |
| Mercator | rhumb bearings | area; scale factor sec φ = 2 at 60°, so a 1:1,000,000 chart is effectively 1:500,000 there | navigation |
| stereographic | local angles/shape | area away from the touch point | polar work |
| azimuthal equidistant | distance from one center | everything else | one-center claims (capital, pole) |
| local plane / portolan | nothing beyond short distances | distance and bearing with range | a delta, a harbour, a parish |

- **Scale is three numbers:** representative fraction, scale bar, and the ground precision it implies. At 0.2 mm graphic resolution: 1:24,000 = 4.8 m; 1:50,000 = 10 m; 1:250,000 = 50 m. A 1 cm bar at 1:50,000 is 500 m; at 1:250,000, 2.5 km.
- **Scale is political.** The scale decides which settlements exist on the sheet: a 1:250,000 map cannot show a hamlet, which is a selection rule with a budget behind it.
- **Orientation is a decision, not a default.** Decide which north (true, magnetic, grid — `direction-symbolism.md:51`) and which edge is up: east at top (T-O), south at top (Chinese — `to-verify`), Mecca-centred, route-up (itineraries). A 32-point compass rose is 11.25° per point.
- **The blank is a class.** Unknown interior, chartered exemption, taboo site, rival claim — each blank needs a legend entry or it is indistinguishable from ignorance. The legend is the sheet's constitution: it declares what a mark commits you to.

## 6. Material, reproduction, and the map trade

| Medium | Preparation | Copy economics | Failure mode |
|---|---|---|---|
| parchment/vellum | skin, scraping, pounce | each copy a new draught; expensive, durable, reusable by scraping (palimpsest) | costly error; scraped-away evidence |
| rag paper | beating, sizing | cheaper; hand or block copies | water damage; copy drift |
| cloth | sizing, painting | lienzo and portolan practice; portable | folds and crease wear |
| woodblock | relief carve | one block, many impressions | coarse line; block wear |
| copperplate | intaglio engrave/etch | expensive plate, cheap impressions, fine line | plate wear and reworking |
| lithography (19th c.) | grease on stone | cheap large runs | tone replaces line; dateable as industrial |

- **Reproduction rule:** manuscript copying makes each copy a new error; printing makes one error exactly repeatable. The first makes drift visible; the second makes it authoritative.
- **Workshop roles:** surveyor, computer/reducer, draughtsman, engraver, printer, colourist, publisher. **Organization:** court atelier, monastic scriptorium, commercial print house, state survey office. **Products:** single sheet, atlas, globe, cadastral register. **Customers:** state, merchant, church, army, gentleman.
- **Cost rule:** cheapening reproduction widens the base, not the authority (`writing-media-surface-economy.md:78`). A cheap map can be everywhere and still be the state's map.
- **Prestige:** the atlas, the dedication, the cartouche; a title claiming to be a "theatre" of the world is a completeness claim, not a description (`to-verify`).

## 7. Provenance and charter: who says the map is true

| Link | Question | Artifact |
|---|---|---|
| warrant | who ordered this sheet, for what use? | commission/order |
| record | what observations stand behind it? | field book, control sketch |
| attestation | who signs that the record is theirs? | surveyor's oath/signature |
| authentication | how does a reader know the copy is authorized? | seal, registration, licence, clerk's mark |
| use | what may this sheet decide? | statute, levy roll, treaty, sailing instruction |

- **Authority ladder** (high to low): state survey > chartered company > municipal survey > licensed pilot's chart > private sketch. A sheet used above its rung is a provenance failure, not a drafting failure.
- **Failure classes:** forged sheet; copied error made repeatable by print; outdated sheet still in use; unauthorized copy; use outside warrant (a harbour chart deciding a boundary).
- **Contest rule:** when two maps disagree, the better warrant chain wins, not the more beautiful sheet. A dated field book beats a copperplate.
- **Performative map:** as metaphysics the map is not the territory; in a registered system the registered sheet *is* the legal fact until reopened. Keep the two apart — a category error as metaphysics, a performative fact as procedure.
- **Charter questions:** who may make a map, who may copy it, who may read it? A state that restricts survey restricts the frame; a guild that owns the field book owns the coast.

## 8. The map's silences and the legal instrument

Six silence classes: (1) unmeasured interior; (2) settlement below the scale threshold; (3) route omitted because unofficial or unmaintained; (4) replaced toponym — "Every renaming is datable; a map is an archive of coups" (`naming-systems.md:70`); (5) distorted boundary, where the line is a claim rather than a survey; (6) suppressed feature the authority does not want found.

- The boundary line is the clearest case: a treaty map creates the line it describes, and a cadastral map creates the parcel it taxes. The map is a legal instrument before it is an illustration.
- **Design lever:** for each silence, ask who benefits and who can detect it. A blank everyone can see is a convention; a blank only the surveyor knows is a secret.

## 9. Build order (nine steps, each writes an artifact)

1. Fix the question and the reader → question brief.
2. Fix the precision and control → precision statement + control sketch.
3. Fix projection and scale, and state what they distort → projection note.
4. Fix orientation → orientation note.
5. Fix the symbol set and the blank rule → legend/key.
6. Fix the medium and reproduction path → production spec.
7. Decide the silences and who benefits → silence schedule.
8. Write the warrant chain and the access rule → warrant docket.
9. Run the calibration audit and name what the map cannot show → audit sheet.

Steps 1–2 are the survey; 3–5 the sheet; 6 the trade; 7–8 the politics; 9 the honesty check.

## 10. Decision record

| ID | Decision | Trigger | Failure if skipped |
|---|---|---|---|
| DR-CM-01 | state the question and reader before the form | any new map | form chosen by fashion |
| DR-CM-02 | state precision and the scale it supports | any measured sheet | graphic precision exceeds evidence |
| DR-CM-03 | name the projection and its distortion | any sheet covering more than a day's walk | area/bearing claims silently wrong |
| DR-CM-04 | name the orientation convention | any sheet with a north arrow or rose | true/magnetic confusion |
| DR-CM-05 | classify every blank | any sheet with an empty area | ignorance reads as claim, or claim as ignorance |
| DR-CM-06 | attach the warrant chain and copy rule | any sheet used as evidence | a beautiful sheet loses to a field book |

## 11. NON-CANON worked micro-example

**NON-CANON.** The culture, place and numbers below are invented to demonstrate the method; nothing here is a claim about a real people.

The Vessa delta, a grain-growing polity of about 40,000 people, levies a tenth of stored grain each levy year. The levy board commissions one cadastral sheet; the temple archive commissions a chorographic sheet from the **same** survey.

- **Question/reader (DR-CM-01):** board — which parcels owe, how much, at the next levy; temple — what the delta looks like for a pilgrimage account.
- **Survey (DR-CM-02):** rope-and-pole traverse along the dikes, 100-pace legs; control = the temple tower and two dike markers; closing error ±1% → ±0.75 m per leg.
- **Scale (DR-CM-02):** 1:5,000 for the cadastral sheet, so 0.2 mm = 1 m: the survey's ±0.75 m is just inside the graphic limit. The temple sheet at 1:25,000 (0.2 mm = 5 m) discards precision on purpose.
- **Projection (DR-CM-03):** local plane for the cadastral sheet (no projection claim; the register is a multi-sheet set — at 1:5,000 a 20 km delta spans several sheets, not one); a stated equidistant grid for the temple sheet.
- **Orientation (DR-CM-04):** river-flow-up (source at top) for both; the levy clerk reads parcels downstream-to-upstream.
- **Symbols (DR-CM-05):** parcel hatch, dike line, grain-store mark, levy-district boundary. The temple enclosure is a **hatched blank** labelled "chartered exemption" — a positive symbol, not ignorance.
- **Reproduction (DR-CM-06):** one cloth master per register sheet, twelve paper copies; each copy carries the clerk's mark; an unmarked copy is not evidence.
- **Silences (DR-CM-05):** the temple enclosure (exempt), a silted channel (owes nothing), and three hamlets below the parcel rule (shown as one district mark).
- **Update rule (stated once):** the register is re-surveyed when the levy year turns; a breach, a silted channel, or a new dike is entered in the margin and changes the **next** levy-year assessment, never the current one.
- **Storm test (year 3):** a dike breach floods parcels 16–18. The clerk enters the breach date in the margin. The owner of parcel 17 claims the year-3 assessment is void because the parcel is no longer arable. The board applies the rule as written (DR-CM-05, DR-CM-06): the year-3 assessment stands; the margin entry is evidence for a year-4 abatement if the parcel is still saline at the re-survey. The dispute is settled by field book + margin + rule, not by the draughtsman's shading.

| If the rule were… | Cost | Dispute effect |
|---|---|---|
| re-survey after every breach | survey team on permanent standby | every storm invites a claim |
| no margin entry | cheap | breach evidence lost; the board guesses |
| assessment void on breach | cheap | incentive to breach the dike |

The same survey produced two forms because the questions differ; the blank is a legal symbol; the update rule, not the drawing, decides the dispute.

## 12. Calibration bank

| Claim | Status (`calibration-registry.md:35-39`) | What to say instead |
|---|---|---|
| "A map is a neutral, objective picture of space" | R | selection, projection, orientation and omission are constitutive (Harley 1989; Wood 1992) |
| "Medieval people believed the earth was flat; T-O maps prove it" | R | sphericity was standard; T-O diagrams are symbolic, not survey maps (`cosmology-cosmography.md:71,:102`; Russell 1991) |
| "Portolan charts are photographically accurate" | C | practical sailing charts with their own distortions and conventions (Campbell, page `to-verify`) |
| "Indigenous maps are childlike or merely mental" | R | lienzos and cartographic histories are precise legal/territorial documents (`mesoamerica-primary-sources.md:58`; Mundy 1996) |
| "The map is the territory" | R as metaphysics; B as procedure | category error as metaphysics; performative fact in a registered system — keep the two apart |
| "Cartography diffused one-way from Europe" | C | Chinese, Islamic, Mesoamerican and Polynesian traditions are independent or parallel (Needham; al-Idrisi; Mundy) |
| "Maps were rare because people were primitive" | R | rarity is a cost-and-warrant effect (`writing-media-surface-economy.md:67-78`) |
| "The map was always a state monopoly" | R | varies by period and form; pilot's charts and estate maps are private |
| "Cheap printing democratized map knowledge" | R | cheapness widens the base, not the authority (`writing-media-surface-economy.md:78`) |
| "A registered map cannot be wrong" | R | registration authenticates a copy, not its observations |
| "Ancient maps were legal documents" | B | true of cadastral and treaty maps, not of every sheet — carry the genre |

- **Living-practice flag:** indigenous cartographic sovereignty — a community's map is its legal record, not a design motif. Describe the genre; do not appropriate the specific.
- **Precision trap:** every number in this entry is a design range until page-checked. The arithmetic in §3 and §5 is arithmetic; the historical dates are `(to-verify)`.

## 13. Recheck

Before any of the following becomes load-bearing: re-run the projection figures (the sec φ and cos φ relations are arithmetic; the exemplar dates are not); the centuria dimensions (2400 Roman feet at 0.296 m ≈ 710 m ≈ 50 ha — arithmetic once the foot length is accepted); the chart dates (Carte Pisane late 13th c.; Dunhuang c. 700 CE; Hereford c. 1300); the claim that a named historical map served as a legal instrument; and any etymology quoted from a neighbour without re-reading its line.

## 14. Scope

Reference method and lane policy for the culture-material partition. This entry decides nothing about any world, admits no map into canon, and its typology is stipulative, not a universal law. Handoff: lore-shokunin owns which maps exist in-world, their content and their legal force. Reference and method only.
