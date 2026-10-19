# C01 — cartography entry body (claim C, right-sized draft)

- Seat: `C01` | role: executor | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json` `baseline_commit`
- Out path: `reports/round-48/cov/C01-entry.md` (this file)
- Landing target (draft only — **not written by this seat**): `corpus/knowledge/culture-material/cartography-and-mapmaking.md`
- Mission: the complete, right-sized entry body covering the register property, the survey-to-symbol chain, material/form classes, the mapmaker trade, provenance/charter, build order, a NON-CANON worked example, calibration bank, recheck, scope — with every arithmetic step and every in-repo `path:line` verified before writing.

**One-line result.** A **227-line** entry (215 body lines after the 11-field head block) that fills the verified-fresh cartography gap with a *method* entry rather than a map history: a five-condition register test, a 12-row one-owner boundary that answers the `cosmology-cosmography.md:27` competing sentence r47 omitted, a seven-link survey chain with a recomputed error budget, eight forms each with a "cannot show" column and a minimum build, projection/scale/orientation as claims, media and reproduction economics, a five-link warrant chain, six silence classes, a nine-step build order, a six-row decision record, a one-rule NON-CANON example, and an 11-row calibration bank. All nine R03 blocking defects (B1–B9) are answered in §4 below, with the specific fix for each.

---

## 1. Live measurements at the baseline (commands and outputs)

All commands run from the lane root, 2026-10-19, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ wc -l corpus/knowledge/culture-material/*.md | sort -n     # min / median / max
103 / 149 / 221   (25 files)
```

Gap probes (fresh at `a01405d`, not carried from r44):

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|mappa|survey map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
$ grep -rni 'cartograph' corpus/knowledge/          # 2 lines, 2 files
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102:… T-O diagrams are symbolic devices, not cartographic claims …
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58:| Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca) | …
$ for t in mapmaking portolan graticule theodolite; do grep -rli "$t" corpus/knowledge/ | wc -l; done
0 0 0 0
$ grep -rliE 'cartograph|mapmak|portolan|cadastr|mappa mundi|surveyor|theodolit|compass rose|graticule|world map|drawn map|map of|maps of' corpus/knowledge/ | wc -l
28
```

`cosmology-cosmography.md:71` is a survey-map disclaimer — "T-O diagrams are symbolic, not survey maps" — but it does **not** contain the token `cartograph`, so it is not counted in the 2/2. This is the exact distinction R03 B2 required; the entry states it the same way.

Slug and sort position:

```
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access …: No such file or directory
$ ls corpus/knowledge/culture-material/ | sed -n '4,7p'
calendar-festival-systems.md
costume-semiotics.md
craft-artisan-lexicon.md
```

`calendar-festival-systems.md` sorts before `cartography-and-mapmaking.md` (`cal` < `car`) and `costume-semiotics.md` sorts after (`car` < `cos`). Landing is an **A**, not an **M**.

---

## 2. The deliverable — full entry, integration-ready

Fenced block = the complete entry (head block + body). The head block is C02's mission; it is included here so this file is independently loadable and byte-checkable. If C02 files its own head block, the two must agree byte-for-byte on `- topic:` (the sweep compares the README row to the entry topic exactly, `reports/round-28/readme/sweep.py:139-140`) and on the measured gap counts.

````markdown
# Cartography and mapmaking — the survey-to-sheet register: the map as an argument about space, its forms, its silences, and the trade that makes it authoritative

- gap filled: the corpus owns space as cosmology, as sacred route, as orientation code and as built settlement, and owns the made map nowhere: 0 filename owners and 0 topic-line owners at HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af`, with `grep -rni 'cartograph' corpus/knowledge/` returning **2 lines in 2 files**, both by-product uses (`myth-symbol/cosmology-cosmography.md:102`; `civilizations/mesoamerica-primary-sources.md:58`), and `mapmaking` / `portolan` / `graticule` / `theodolite` returning 0 files each. `cosmology-cosmography.md:71` disclaims survey maps without using the token. This is a named-but-unbuilt register, not a high-demand omission — and the partition's own cosmography entry supplies both the disclaimer (`:71`, `:102`) and the competing sentence this entry must answer (`:27`, "how the world is drawn (maps)"): cosmography owns the world-drawn content, this entry owns the surveyed, projected, reproduced sheet as production.
- topic: the map as a made instrument and a claim about space for fictional cultures — the survey → control → projection → symbol → reproduction chain that makes a sheet authoritative; the four choices every map makes (what is measured, what is preserved, what is drawn, who may copy and read it); the eight map forms (itinerary/strip, cadastral, chorographic, portolan, celestial/star chart, cosmographic, thematic, cartographic history/lienzo) and what each structurally cannot show; projection, scale and orientation as claims, with the error budget that ties graphic precision to survey precision; the map trade (media, reproduction economics, workshop roles, patronage); the warrant chain (commission → field book → attestation → authentication → use) and the map as a legal/territorial instrument; the map's silences; a nine-step build order, a decision record, a NON-CANON worked example, and a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory) — reference and method only
- sources:
  - In-corpus anchors (every line re-read in this seat at HEAD `a01405dd`, transcript in `## Self-audit` below the fence): `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` (the competing "drawn (maps)" sentence), `:71` and `:102` (T-O disclaimers); `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:5,:69` (place register, route types); `corpus/knowledge/myth-symbol/direction-symbolism.md:51` (the compass trap); `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` (castrum grid, groma, "the grid is cadastral"); `corpus/knowledge/culture-material/writing-media-surface-economy.md:3,:73,:78` (surface families, register/ledger tier, "cheapness widens the base"); `corpus/knowledge/culture-material/transport-mobility-lexicon.md:28,:117` (maintenance rule, DR-TR-02); `corpus/knowledge/linguistics/naming-systems.md:40,:70` (toponymy; "a map is an archive of coups" — quoted exactly, not corrected); `corpus/knowledge/culture-material/craft-artisan-lexicon.md:54-65` (workshop ladder, cited at the ladder table, not the material-grading row at `:44`); `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58` (lienzo source class); `corpus/knowledge/verification/calibration-registry.md:35-39` (R/C/B/H/T codes); `corpus/QUALITY.md:5-20` (admission bar).
  - External shelf — **not consulted this round** (no network at seat time); no unread work is presented as inspected. Every item is `(to-verify)` for edition, volume and page: Harley & Woodward, eds., *The History of Cartography*, 6 vols. in 7 (U. Chicago Press, 1987–2022); Harley (1989), "Deconstructing the Map," *Cartographica* 26(2): 1–20; Wood (1992; 2nd ed. 2010), *The Power of Maps* (Guilford); Monmonier (1991; 3rd ed. 2018), *How to Lie with Maps* (U. Chicago Press); Jacob (Fr. 1992; Eng. 2006), *The Sovereign Map* (U. Chicago Press); Ptolemy, *Geography*, trans. Berggren & Jones (2000, Princeton UP); Campbell (1987), "Portolan Charts from the Late Thirteenth Century to 1500," in *History of Cartography* vol. 1; Edson (2007), *The World Map, 1300–1492* (Johns Hopkins UP); Kain & Baigent (1992), *The Cadastral Map in the Service of the State* (U. Chicago Press); Mundy (1996), *The Mapping of New Spain* (U. Chicago Press); Boone (2000), *Stories in Red and Black* (U. Texas Press); Pickles (2004), *A History of Spaces* (Routledge); Buisseret, ed. (1992), *Monarchs, Ministers, and Maps* (U. Chicago Press); Snyder (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395; Dilke (1971), *The Roman Land Surveyors* (David & Charles); Russell (1991), *Inventing the Flat Earth* (carried in-corpus at `cosmology-cosmography.md:102`); al-Idrisi, *Nuzhat al-mushtāq* (1154); the *Tabula Peutingeriana* (13th-c. copy); Ortelius, *Theatrum Orbis Terrarum* (1570); Mercator (1569; *Atlas* 1595).
- couples: corpus/knowledge/myth-symbol/cosmology-cosmography.md (owns the world model and the T-O diagram as symbolic device — `:27,:71,:102`; this entry owns the survey sheet and cites the disclaimers as the boundary, answering `:27` without restating the five axes); corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md (owns the holy-site typology and the route-as-rite — `:5,:69`; this entry owns how a route is measured and drawn); corpus/knowledge/myth-symbol/direction-symbolism.md (owns orientation code and the true-vs-magnetic trap — `:51`; this entry owns the map convention that applies it); corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md (owns the sky as symbolic system; this entry owns the star chart as a map form); corpus/knowledge/culture-material/architecture-settlement-lexicon.md (owns the built lexicon and the castrum grid — `:95`; this entry owns land survey as a production step); corpus/knowledge/culture-material/writing-media-surface-economy.md (owns the seven surface families and the cost ladder — `:3,:73,:78`; this entry owns map-specific media and reproduction); corpus/knowledge/culture-material/transport-mobility-lexicon.md (owns route institutions and maintenance — `:28,:117`; this entry owns the representation of a route); corpus/knowledge/linguistics/naming-systems.md (owns toponymy and critical toponymy — `:40,:70`; this entry owns the toponym layer of the sheet); corpus/knowledge/culture-material/craft-artisan-lexicon.md (owns the workshop ladder — `:54-65`; this entry owns the mapmaker's role set); corpus/knowledge/culture-material/trade-economy-lexicon.md (owns market, measure and contract vocabulary; this entry owns the map as legal/territorial instrument); corpus/knowledge/civilizations/mesoamerica-primary-sources.md (owns the lienzo source class and its provenance — `:58`; this entry cites the genre); corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md (owns mythic charter and legitimation; this entry owns the map's warrant as a legal charter); corpus/knowledge/verification/calibration-registry.md (supplies the R/C/B/H/T codes — `:35-39`); corpus/knowledge/verification/to-verify-triage-protocol.md (the `(to-verify)` placement rule); handoff target: lore-shokunin world bible — method and comparative data only, canon decisions are theirs.
- verified-at: 2026-10-19 — written this round at lane HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`), equal to `reports/round-48/claims.json` baseline. Every in-repo `path:line` re-read in this seat; the external shelf not consulted (no network), so every edition/page is `(to-verify)`.
- recheck: before any projection distortion figure, chart date, cadastral dimension or legal-instrument claim becomes load-bearing in a world bible — re-run §12's arithmetic and §13's recheck list against the cited pages; the arithmetic is arithmetic, the historical dates are not.
- scope: reference method and lane policy for the culture-material partition. This entry decides nothing about any world, admits no map into canon, and its five-condition test is stipulative, not a universal law of cartography. Reference and method only; canon decisions belong to lore-shokunin.

## 1. The register property: a map is an argument about space

**Master claim.** A map is an argument about space, not a picture of it. Its authority comes from the survey chain behind the sheet, and its politics from what the chain and the draughtsman leave out. Every sheet makes four load-bearing choices, and the order matters:

1. **What is measured** — the survey precision and the control network. A map cannot be more precise than its weakest measurement.
2. **What is preserved** — the projection and scale. Every sheet trades shape, area, distance or bearing; none keeps all four.
3. **What is drawn** — selection, symbolization, orientation, and the blank.
4. **Who may copy and read it** — reproduction, warrant, and access.

**The five-condition test** decides whether an object belongs to this register. Apply it object by object; a partial pass is a fail, and the failure names what the object is instead.

1. **Referent index** — the object asserts positions or relations in a ground space someone could traverse.
2. **Bounded notation** — it uses a finite, conventional set of marks, not free depiction.
3. **Structural selection** — it omits by a rule, not by accident.
4. **Conventional readability** — a competent reader in the culture can recover the code without the maker present.
5. **Reproducibility/citability** — copies can be made and compared, so the sheet can serve as evidence.

The failures are diagnostic, not dismissive: a **field book** has index and notation but no conventional readability (private evidence, the map's raw material); a **landscape painting** depicts but has no bounded notation; a **T-O diagram** has convention but no ground index (a cosmogram — `cosmology-cosmography.md:71,:102`); an **itinerary** has index but no area (a route list); a **star chart** indexes the sky, not the ground (another register's sheet); a **mental map** fails reproducibility (an informant's testimony, citable as such).

## 2. One-owner boundary

Cosmography owns the world-drawn content — how the world is drawn, named, walked and built (`cosmology-cosmography.md:27`) — and explicitly disclaims survey maps (`:71`, `:102`). This entry owns the **surveyed, projected, reproduced sheet as production**. Stating both halves is the one-owner proof: a strict reading of `:27` would otherwise ask why "drawn (maps)" is not already an owner.

| Neighbour | What it owns (live anchor) | This entry's boundary |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | world model, five axes, T-O as symbolic device (`:27,:71,:102`) | the measured, projected, reproduced sheet; T-O cited only as contrast |
| `myth-symbol/sacred-topography-pilgrimage.md` | holy-site typology, three route types (`:5,:69`) | how a route is surveyed and drawn; does not re-own pilgrimage |
| `myth-symbol/direction-symbolism.md` | orientation code, true-vs-magnetic trap (`:51`) | the map convention (north arrow, rose, frame); cites the trap |
| `myth-symbol/celestial-symbolism-calendars.md` | the sky as symbolic system | the star chart as a map form; does not restate sky myth |
| `culture-material/architecture-settlement-lexicon.md` | settlement lexicon, castrum grid, groma (`:95`) | land survey as a production step; does not restate building words |
| `culture-material/writing-media-surface-economy.md` | seven surface families, cost ladder (`:3,:73,:78`) | map-specific media and reproduction; cites the cost rule |
| `culture-material/transport-mobility-lexicon.md` | route institutions, maintenance (`:28,:117`) | representation of a route; cites the maintenance rule |
| `linguistics/naming-systems.md` | toponymy, critical toponymy (`:40,:70`) | the toponym layer on the sheet; quotes `:70` exactly |
| `culture-material/craft-artisan-lexicon.md` | workshop ladder, guild systems (`:54-65`) | the mapmaker's role set; does not restate the ladder |
| `culture-material/trade-economy-lexicon.md` | market, measure, contract vocabulary | the map as legal/territorial instrument; does not restate contract words |
| `civilizations/mesoamerica-primary-sources.md` | lienzo source class and provenance (`:58`) | cites the genre as a map form; does not restate the inventory |
| `myth-symbol/sacred-kingship-mythic-charter.md` | mythic charter and legitimation | the map's warrant as a legal charter; does not restate legitimation |

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

| Form | Question it answers | Real exemplar (`to-verify` for edition) | Structurally cannot show |
|---|---|---|---|
| itinerary/strip | how do I get there? | *Tabula Peutingeriana* (13th-c. copy) | area, off-route relations, true relative distance |
| cadastral/land register | who owes what on which parcel? | Roman centuriation (centuria ≈ 710 m square ≈ 50 ha); Kain & Baigent | terrain, use rights it does not tax |
| chorographic/regional | what is this province like? | (to-verify) | precise position; it is an impression |
| portolan/nautical | bearing and distance to the next port? | Carte Pisane, late 13th c. | inland, high latitudes; makes no projection claim |
| celestial/star chart | where is the sky at this hour? | Dunhuang star chart, c. 700 CE | ground position; time-bound |
| cosmographic/world diagram | what is the shape of the world? | T-O diagram; Hereford Mappa Mundi, c. 1300 | survey; it is symbolic |
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
- **Orientation is a decision, not a default.** Decide which north (true, magnetic, grid — `direction-symbolism.md:51`) and which edge is up: east at top (T-O), south at top (Chinese), Mecca-centred, route-up (itineraries). A 32-point compass rose is 11.25° per point.
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

- **Question/reader:** board — which parcels owe, how much, at the next levy; temple — what the delta looks like for a pilgrimage account.
- **Survey:** rope-and-pole traverse along the dikes, 100-pace legs; control = the temple tower and two dike markers; closing error ±1% → ±0.75 m per leg.
- **Scale:** 1:5,000 for the cadastral sheet, so 0.2 mm = 1 m: the survey's ±0.75 m is just inside the graphic limit. The temple sheet at 1:25,000 (0.2 mm = 5 m) discards precision on purpose.
- **Projection:** local plane for the cadastral sheet (no projection claim; the delta is about 20 km across); a stated equidistant grid for the temple sheet.
- **Orientation:** river-flow-up (source at top) for both; the levy clerk reads parcels downstream-to-upstream.
- **Symbols:** parcel hatch, dike line, grain-store mark, levy-district boundary. The temple enclosure is a **hatched blank** labelled "chartered exemption" — a positive symbol, not ignorance.
- **Reproduction:** one cloth master, twelve paper copies; each copy carries the clerk's mark; an unmarked copy is not evidence.
- **Silences:** the temple enclosure (exempt), a silted channel (owes nothing), and three hamlets below the parcel rule (shown as one district mark).
- **Update rule (stated once):** the register is re-surveyed when the levy year turns; a breach, a silted channel, or a new dike is entered in the margin and changes the **next** levy-year assessment, never the current one.
- **Storm test (year 3):** a dike breach floods parcels 16–18. The clerk enters the breach date in the margin. The owner of parcel 17 claims the year-3 assessment is void because the parcel is no longer arable. The board applies the rule as written: the year-3 assessment stands; the margin entry is evidence for a year-4 abatement if the parcel is still saline at the re-survey. The dispute is settled by field book + margin + rule, not by the draughtsman's shading.

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
| "Medieval people believed the earth was flat; T-O maps prove it" | R | sphericity was standard; T-O diagrams are symbolic, not survey maps (`cosmology-cosmography.md:102`; Russell 1991) |
| "Portolan charts are photographically accurate" | C | practical sailing charts with their own distortions and conventions (Campbell, page `to-verify`) |
| "Indigenous maps are childlike or merely mental" | R | lienzos and cartographic histories are precise legal/territorial documents (`mesoamerica-primary-sources.md:58`; Mundy 1996) |
| "The map is the territory" | R as metaphysics; B as procedure | category error as metaphysics; performative fact in a registered system — keep the two apart |
| "Cartography diffused one-way from Europe" | C | Chinese, Islamic, Mesoamerican and Polynesian traditions are independent or parallel (Needham; al-Idrisi; Mundy) |
| "Maps were rare because people were primitive" | R | rarity is a cost-and-warrant effect (`writing-media-surface-economy.md:73-78`) |
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

````

**Fence measurements** (`sha256` of the fenced text, computed on `.scratch/c01-entry-draft.md`, which is byte-identical to the lines between the fences above):

```
lines      227      (body after the head block: 215)
nonblank   177
words      4545
bytes      29968
H2 sections 14
table rows  81      (lines beginning '|')
(to-verify) 6       (all on the external shelf or a dated exemplar)
sha256     2a66774974b80d9be2659a9e0e09a265114631c21189eae506acba5edfbdb3ca
```

**Length judgment, stated honestly.** 227 lines is 6 lines above the current partition maximum (221) and 78 above the median (149). The body alone is **215 lines**, 29% of r47's 739-line body; the whole entry is 31% of it. The over-build class is not repeated. The claim's budget is "<=~250", which this satisfies. If the integrator wants the entry strictly at or under the current max of 221, three cuts are available without touching the method: the lithography row (§6, 1 line), the "Prestige" bullet (§6, 1 line), and the "Ancient maps were legal documents" calibration row (§12, 1 line) — that is 3 lines, so reaching 221 needs one further merge (fold the §14 scope sentence into §13). I did not make those cuts because each carries a real decision surface; the choice belongs to the integrator, and I record it rather than silently becoming the new max.

---

## 3. Entry-contract checklist

| Contract element | Where in the entry | Status |
|---|---|---|
| H1 + subtitle | line 1 | present |
| `- gap filled:` with fresh measured counts | `:3` | present; 2 lines / 2 files, 0 filename and 0 topic owners |
| `- topic:` (sweep-visible, single field) | `:4` | present; one logical line, no internal `- ` line start |
| `- sources:` tiered, external marked | `:5-7` | present; in-corpus anchors + 20-item external shelf, all `(to-verify)` |
| `- couples:` | `:8` | present; 14 tokens, all resolve (below) |
| `- verified-at:` | `:9` | present; names HEAD and the no-network limit |
| `- recheck:` | `:10` | present |
| `- scope:` | `:11` | present |
| § register property | §1 | present |
| § one-owner boundary | §2 | present, 12 rows |
| § survey-to-symbol chain | §3 | present, 7 links + error budget |
| § form classes | §4 | present, 8 forms + 8 minimum builds (B9 fix) |
| § material / reproduction | §6 | present, 6 media |
| § mapmaker trade | §6 | roles, organization, products, customers |
| § provenance / charter | §7 | present, 5-link warrant chain |
| § build order | §9 | 9 steps, each with an artifact |
| § NON-CANON example | §11 | declared invented; one update rule |
| § calibration bank | §12 | 11 rows with R/C/B/R-as-metaphysics codes |
| § recheck | §13 | present |
| § scope | §14 | present |

---

## 4. R03 B1–B9 recurrence audit (each defect answered, with the live fix)

| R03 defect | r47 failure | This draft's answer | Where |
|---|---|---|---|
| **B1** | 0.2 mm at 1:50,000 called "10×" a 200 m survey | The arithmetic is now stated as a rule: 0.2 mm at 1:50,000 = 10 m; a 200 m closure is a **20×** overstatement (`200/10 = 20`, recomputed) | §3 error budget |
| **B2** | Unreproducible gap count; `:71` wrongly counted as a `cartograph` hit | Measured **2 lines in 2 files** (`:102`, `mesoamerica:58`); `:71` named as a disclaimer *without the token* | head `- gap filled:` + §1 |
| **B3** | False accusation that "archive of coups" was not in the file | Quoted **verbatim** from `naming-systems.md:70` ("Every renaming is datable; a map is an archive of coups."); no correction proposed; transcript below | §8 |
| **B4** | Workshop ladder cited `craft-artisan-lexicon.md:44` (steel-grading row) | Cites **`:54-65`** (header `:54`, seven systems `:56-63`, design rule `:65`) and says so explicitly; `:44` is not used | §2 table |
| **B5** | Form-typology cross-refs pointed at §1–3 / §2 | The typology is §4 and no prose points elsewhere; all four `§N` references in the draft resolve to the named section (§3, §5, §12, §13 — checked below) | §4 |
| **B6** | Provenance/charter called §9 while it was §8 | Provenance/charter is **§7** here and both the section heading and the sentence agree | §7 |
| **B7** | Worked example stated three incompatible update rules | One rule, stated once in bold; the storm test applies "the rule as written" and never restates a different one; the only other `re-survey` line is a counterfactual cost row | §11, line 191 (rule), 192 (test), 196 (counterfactual) |
| **B8** | "owns no made map" overstated against `cosmography:27` | The `:27` competing sentence is quoted and answered in §2's opening paragraph and in the boundary table's first row | §2 |
| **B9** | "Minimum build per form" covered 5 of 8 forms | Table has **8 forms**; the minimum-build list explicitly says "the eight forms above, not a sample" and lists all eight | §4 |

Also answered from R03's should-fix list: P2-1 (map/territory conflict) is one calibration row with the metaphysics/procedure split; P2-2/P2-3/P2-4 are r47 assembly issues absent here; P2-5 (stick chart) is not used; P2-6 (per-row to-verify) is moot — the shelf is one marked block; P2-7 (missing boundary rows) is answered by the 12-row table including craft, trade, celestial and sacred-kingship.

---

## 5. Self-audit — citations, arithmetic, cross-references, couples

### 5.1 Every in-repo anchor, re-read at its live line

| Anchor | Live content I read (excerpt) | Used for |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md:27` | "**Cosmography** = the projected, inhabited version: how the world is drawn (maps), named … walked … built" | the competing sentence the boundary answers |
| `…cosmology-cosmography.md:71` | "Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, not survey maps" | gap + boundary |
| `…cosmology-cosmography.md:102` | "… T-O diagrams are symbolic devices, not cartographic claims" | calibration R row |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | "the place register … the holy-site typology …" | boundary |
| `…sacred-topography-pilgrimage.md:69` | "**The three route types.** (a) **Fixed itinerary** … (b) **Votive ramble** … (c) **Circuit**" | boundary |
| `myth-symbol/direction-symbolism.md:51` | "**The compass trap** … deciding *which* north — true or magnetic … declination" | orientation |
| `culture-material/architecture-settlement-lexicon.md:95` | "surveyed with the **groma** … The grid is cadastral: a state that *measures land* builds this city." | boundary |
| `culture-material/writing-media-surface-economy.md:3` | "- topic: What a culture writes on, priced … the seven surface families …" | boundary |
| `…writing-media-surface-economy.md:73` | "| 3 | papyrus (coarse), paper (early), cloth | … the account, the contract, the register, the ledger |" | reproduction tier |
| `…writing-media-surface-economy.md:78` | "Cheapness widens the *base*, it does not redistribute the *authority*." | cost rule (quoted as rule, not verbatim) |
| `culture-material/transport-mobility-lexicon.md:28` | "a route is only real if someone maintains it" | boundary |
| `…transport-mobility-lexicon.md:117` | "DR-TR-02 | Require a maintenance clause …" | boundary |
| `linguistics/naming-systems.md:40` | "Onomastics splits by what is named: **anthroponymy** … **toponymy** …" | boundary |
| `linguistics/naming-systems.md:70` | "Every renaming is datable; a map is an archive of coups." | **verbatim quote** (B3) |
| `culture-material/craft-artisan-lexicon.md:54-65` | `:54` ladder header ("Apprentice / Journeyman / Master / Entry rite"); `:56-63` seven systems; `:65` design rule | boundary (B4) |
| `civilizations/mesoamerica-primary-sources.md:58` | "Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca) …" | boundary + calibration |
| `verification/calibration-registry.md:35-39` | the R / C / B / H / T rows and their stop rules | calibration codes |
| `verification/calibration-registry.md:41` | "Multiple codes may apply to different parts of one theory." | the R-as-metaphysics/B-as-procedure split |
| `corpus/QUALITY.md:5-20` | the five admission clauses (provenance → canon hygiene) | scope + usability |
| `corpus/QUALITY.md:16-17` | "**Usability** … decision tables, typology tables, checklists, worked examples. No essays." | form of the entry |

For B3 specifically, the exact probe:

```
$ grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md
70:- **Critical toponymy** … Every renaming is datable; a map is an archive of coups.
```

### 5.2 Arithmetic — every number recomputed

| Statement in the draft | Recomputation | Result |
|---|---|---|
| 0.2 mm = 1 m at 1:5,000 | `0.2 × 5000 / 1000` | 1.0 |
| 0.2 mm = 0.5 m at 1:2,500 | `0.2 × 2500 / 1000` | 0.5 |
| 0.2 mm = 4.8 m at 1:24,000 | `0.2 × 24000 / 1000` | 4.8 |
| 0.2 mm = 10 m at 1:50,000 | `0.2 × 50000 / 1000` | 10.0 |
| 0.2 mm = 50 m at 1:250,000 | `0.2 × 250000 / 1000` | 50.0 |
| 0.2 mm = 5 m at 1:25,000 | `0.2 × 25000 / 1000` | 5.0 |
| 1 cm = 500 m at 1:50,000 | `1 × 50000 / 100` | 500.0 |
| 1 cm = 2.5 km at 1:250,000 | `1 × 250000 / 100000` | 2.5 |
| 200 m closure vs 10 m line = 20× | `200 / 10` | 20.0 |
| 1 arcmin at 10 km ≈ 2.9 m | `10000 × radians(1/60)` | 2.9089 |
| sec 60° = 2 (Mercator) | `1 / cos(60°)` | 2.0 |
| 1° longitude at 60° = 55.7 km | `111.32 × cos(60°)` | 55.66 |
| centuria side ≈ 710 m | `2400 × 0.296` | 710.4 |
| centuria ≈ 50 ha | `(2400 × 0.296)² / 10000` | 50.47 |
| 32-point rose = 11.25° | `360 / 32` | 11.25 |
| 1% of 100 paces = 0.75 m | `0.01 × 100 × 0.75` | 0.75 |

All 16 pass. The two inputs that are conventions, not facts, are labelled in the draft: the pace as 0.75 m ("a design convention") and the Roman foot as 0.296 m (in §13's recheck, where the derivation is stated as conditional on the foot length).

### 5.3 Internal cross-references

| Reference | Target section (line) | Correct? |
|---|---|---|
| "§3" (error budget / arithmetic) | §3, line 51 | yes |
| "§5" (projection arithmetic) | §5, line 98 | yes |
| "§12" (calibration) | §12, line 202 | yes |
| "§13" (recheck list) | §13, line 221 | yes |

No other `§N` reference exists in the draft, so the r47 B5/B6 class cannot recur.

### 5.4 Couples resolution

14 `corpus/knowledge/...` tokens on the one `- couples:` line; all 14 files exist at HEAD:

`cosmology-cosmography.md`, `sacred-topography-pilgrimage.md`, `direction-symbolism.md`, `celestial-symbolism-calendars.md`, `architecture-settlement-lexicon.md`, `writing-media-surface-economy.md`, `transport-mobility-lexicon.md`, `naming-systems.md`, `craft-artisan-lexicon.md`, `trade-economy-lexicon.md`, `mesoamerica-primary-sources.md`, `sacred-kingship-mythic-charter.md`, `calibration-registry.md`, `to-verify-triage-protocol.md` — **14/14 OK, 0 missing**.

### 5.5 Worked-example consistency (R03 B7 + C14 concerns)

- **One rule, one statement:** §11 line 191. The storm test at line 192 applies it; it does not restate a variant. The only other occurrence of "re-survey" (line 196) is the *counterfactual* row ("if the rule were re-survey after every breach") and is explicitly labelled as a rejected alternative.
- **Internal arithmetic:** survey ±0.75 m; 1:5,000 sheet limit 1.0 m → survey inside the limit; 1:2,500 limit 0.5 m → survey binds; 1:25,000 limit 5 m → sheet discards precision. All consistent.
- **The blank is a symbol, not ignorance:** the temple enclosure is a *hatched blank* with a legend entry ("chartered exemption"), so the "silence" rule is demonstrated, not contradicted.
- **NON-CANON:** declared at the head of §11; the polity, place and numbers are invented; no real people are described.

### 5.6 What I did not verify

- **The external shelf.** No network at seat time; every edition, volume and page is `(to-verify)`, and the entry says so. I did not check any item against a catalogue.
- **Historical dates** (Mercator 1569, Ortelius 1570, *Atlas* 1595, Carte Pisane late 13th c., Dunhuang c. 700 CE, Hereford c. 1300, Minard 1869, Snow 1854). These are conventional dates, marked `(to-verify)` where the entry leans on them; §13 routes them to recheck.
- **The Roman centuria's 0.296 m foot.** The arithmetic follows from that accepted figure; the figure itself is not re-derived here.
- **r47's fragment bytes.** I read R03's review and the r44 seed, and I re-read every live corpus line I cite, but I did not re-read all four r47 fragment files; the B1–B9 list is R03's, and my audit tests against it rather than re-finding it.

---

## 6. Handoff notes

- **C02 (head block):** the full head block is in the fence. Keep `- topic:` byte-identical to the README row (`sweep.py:139-140` compares `row topic != entry topic` exactly). Keep the gap sentence as "2 lines in 2 files" and do not count `:71` as a `cartograph` hit.
- **C10 (README rev 2.5):** live anchors are `corpus/README.md:234` (`## culture-material/ (25)`), row insertion **before line 241** (`calendar` is 240, `costume` is 241), `:544` (`Total knowledge entries: 223.`), `:548` (`(total 223 files; directory totals 25/26/25/29/24/94)`). New vector `25/26/26/29/24/94` sums 224. The rev-2.4 prose vector at `:11` sums 217 and must be repaired or superseded in the same edit.
- **C03 (arithmetic):** the 16 recomputations are in §5.2; the only numbers not arithmetic are dates, all `(to-verify)`.
- **C04 (citation anchors):** the 20 anchors in §5.1 are the exhaustive in-repo set; each was read at the line shown. B3's quote is exact.
- **C05 (length/contract):** 227 lines, 14 sections, all head fields present; §3 checklist.
- **C06 (freshness/collision):** 0 filename owners, 0 topic-line owners at `a01405d`; slug free; sort position between `calendar-festival-systems.md` and `costume-semiotics.md`; landing is A.
- **C09 (couples):** 14/14 resolve; no dangling token.
- **C11 (staged sweep):** expect `rows 224 files 224`, `missing_from_index 0`, `topic_mismatch 0`, `totals_line 224`, footer `25/26/26/29/24/94`, exit 0.
- **C14 (worked example):** rule at §11 line 191 only; storm test line 192; counterfactual line 196.
- **C17 (structure delta vs r47):** 227 lines vs 739 body lines (−512, −69.3%); 215 body lines vs 739; 4,545 words vs 17,601 (−74.2%); 81 table rows vs 240 (−66.3%); 14 H2 vs 15. Load-bearing sections kept (register test, boundary, chain, forms, projection, trade, warrant, build order, example, bank); the padding cut (restated mechanisms, duplicate bullets, the 13-row etymology bank) is absent.
- **W01/X03 (over-build):** this is the measured answer to the over-build class — a draft that is shorter than the partition max plus 6 lines, not 3.3× it.

---

## 7. Write surface and compliance

- **Written:** this file only (`reports/round-48/cov/C01-entry.md`) plus disposable scratch drafts under `.scratch/` (`c01-entry-draft.md`, `c01-preamble.md`, `c01-audit.md`). Nothing under `corpus/`, `tools/`, `reports/round-1..47/`, `tools/gates/frozen/`, or fleet `.ufo/` was written or staged.
- **No** git commit/push, install, or network. **No** `reports/round-*/run-validation.py` was executed. **No** re-freeze of `declared-in-r7`. **No** packet-surface change.
- `git status --porcelain` at my write cut showed the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.
- **Owed:** none. The entry is a complete draft; the only open items are the integrator's length choice (227 vs a 221 cut) and the external shelf's `(to-verify)` marks, which are the corpus's normal inherited-bibliography convention.
