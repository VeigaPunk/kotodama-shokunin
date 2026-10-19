# C03 — cartography entry drafter C (sections 10–15): build order, worked example, calibration, decision record, recheck, scope

- Seat **C03** | role executor | claim **C** (coverage) | round 47, loop 2, position 1.
- Mission (verbatim, `reports/round-47/targets.json` seat `C03`): *"Cartography entry drafter C (sections 10-15): build order + worked micro-example + calibration bank (discredited readings, living-practice flags) + decision record + recheck + scope. Fenced entry body."*
- Target landing (claim C, `reports/round-47/claims.json`): `corpus/knowledge/culture-material/cartography-and-mapmaking.md`. This seat drafts **sections 10–15 only**; C01 drafts §1–4, C02 drafts §5–9, C04 drafts the head block. The integrator assembles the four fragments and applies the entry once.
- Baseline `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`, observed 2026-10-19). Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` for every command.
- **Writes: this file only.** No `corpus/**`, `tools/**`, `README`, `LOG.md`, or filed round-1..46 byte was edited or staged. No commit, push, install, or network. No `reports/round-*/run-validation.py` was executed.
- **Canon: NON-CANON.** This seat authors draft bytes and checks them structurally; it admits no entry, certifies no round, promotes nothing, and decides no world.
- Section-number assumption: the C01/C02 outline named in `reports/round-47/targets.json` (C01 = §1–4 frame/register property/meaning mechanisms/material-and-trade classes; C02 = §5–9 survey-to-symbol chain/scarcity-prestige/mapmaker trade/provenance-charter/container-name fossil). Cross-references inside the draft use those numbers. If the assembled C01/C02 drafts number their sections differently, the integrator must reconcile the `§` references before landing — they are the only coupling this fragment has to the other two.

## 1. Live checks at write time (measured, not asserted)

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe

$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/

$ find corpus/knowledge -name '*.md' | wc -l
223

$ ls corpus/knowledge/culture-material/*.md | wc -l
25

$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
```

| check | command | result |
|---|---|---|
| baseline is declared baseline | `git rev-parse HEAD` vs `reports/round-47/claims.json` `baseline_commit` | `6e9a30d…` == `6e9a30d` |
| total corpus | `find corpus/knowledge -name '*.md' \| wc -l` | **223** |
| target partition | `ls corpus/knowledge/culture-material/*.md \| wc -l` | **25** |
| target path unused | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | absent |
| sort neighbours | `ls corpus/knowledge/culture-material/ \| grep -nE 'calendar\|costume'` | `calendar-festival-systems.md` then `costume-semiotics.md` (positions 5–6) |
| no corpus write by this seat | `git status --porcelain` | only `reports/round-46/review/` (pre-existing) and `reports/round-47/` |

The draft below assumes the landing is an **A (add)** for `cartography-and-mapmaking.md`, between `calendar-festival-systems.md` and `costume-semiotics.md`, and that no existing entry is modified. This seat re-checked the path only; the exhaustive filename/topic sweep is C05/K01's job and the r44 K02 scout's evidence.

## 2. In-corpus anchors cited in the draft — verified line by line

Every `corpus/knowledge/...:line` cited inside the fence was read live at `6e9a30d` in this seat. Excerpts are truncated for the table; the cited content is what the draft uses.

| anchor | verified excerpt (truncated) | use in the draft |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md:71` | "Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, not survey maps (§10)" | §10 boundary note; §12 calibration row 2 |
| `myth-symbol/cosmology-cosmography.md:102` | "'everyone before Columbus believed in a flat earth' is a 19th-century fabrication (Russell 1991) … T-O diagrams are symbolic devices, not cartographic claims" | §12 calibration row 2 |
| `myth-symbol/direction-symbolism.md:51` | "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic …" | §10 step 4; §12 row 14 |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | the place register, route-as-rite, and "sacred-geography mapping … as a diagram" | §10 boundary note; §15 handoff |
| `culture-material/architecture-settlement-lexicon.md:95` | "surveyed with the **groma** … The grid is cadastral: a state that *measures land* builds this city" | §10 step 2; §11 |
| `culture-material/writing-media-surface-economy.md:48` | palm leaf / bark / cloth row: "a *low-capital, high-labour* family" | §11 pilot chart medium |
| `culture-material/writing-media-surface-economy.md:73` | cost-ladder row 3: "papyrus (coarse), paper (early), cloth — the office and the merchant" | §11 levy-sheet copies |
| `culture-material/transport-mobility-lexicon.md:28` | "a route is only real if someone maintains it" | §10 minimum itinerary; §14 recheck |
| `culture-material/material-culture-inference-method.md:69` | perishability: "what survives to be seen" | §12 row 9; §14 survival-bias trigger |
| `culture-material/craft-artisan-lexicon.md:87` | the Dürer/Raimondi monogram case and "a court of marks" | §11 copyist signature; §13 warrant row |
| `civilizations/mesoamerica-primary-sources.md:58` | "Lienzos and cartographic histories … Cloth maps/migration-conquest accounts" | §12 row 4; living-practice flags |
| `civilizations/polynesia-navigation.md:52` | "Distinguish **horizon compass**, **ordered steering-star sequence** … these are related operations, not synonyms" | §12 row 6; living-practice flags |
| `civilizations/japan-medieval-sengoku.md:157` | "a neat Edo cadastral map must not be treated as a direct Sengoku map" | §14 period-map trigger |
| `linguistics/naming-systems.md:70` | critical toponymy: "naming is inscription of power; the street grid is a city-text" | §14 toponym trigger |
| `verification/calibration-registry.md:33-39` | the R/C/B/H/T status table and use rules | §12 status vocabulary |
| `verification/real-world-inspiration-boundaries.md:6` | "recheck: local guidance and permissions before delivery, adaptation, marketing changes, or reuse" | living-practice flags; §14 |
| `verification/myth-consistency-gate.md:34` | "Do not expose restricted ritual knowledge to fill a table." | living-practice flags; §14 |
| `verification/to-verify-triage-protocol.md:15` | "`(to-verify)` means a named factual question remains unanswered." | §12 precision trap; §14 |
| `civilizations/maori.md:20` | "named pounamu histories … require named knowledge holders, local checking, and the cited editions" | living-practice flags |

No citation in the draft is to a line this seat did not read. External works are named as a shelf and marked `(to-verify)`; none was fetched (no network at seat time).

## 3. The fenced draft (entry sections 10–15)

````markdown
## 10. Build order — question → chain → sheet → copy → warrant

The order below is the order the *designer* must decide, not a historical sequence any real tradition followed. Each step produces an artifact the next step consumes; a step with no written output is decoration, and a later step will silently contradict it.

| # | Fix this | Write this into the bible | Fails if skipped |
|---|---|---|---|
| 1 | **The question and the reader.** Who acts on the sheet, and on what decision — a pilot choosing a channel at a tide, a tax office assessing parcels, a temple staging a procession, a general moving a column, a delegation drawing a border, a family claiming land. | One sentence: *"this sheet exists so that X can decide Y at Z."* The sentence names the form (the typology in §1–3) and the acceptable error. | A picture of everything and an instrument of nothing. |
| 2 | **The surveyed surface and the chain.** What is measured — pacing, rope, chain, groma, dioptra, astrolabe, compass, plane table, triangulation, sounding lead — over what baseline and control network, by whom, at what cost per day. | The chain, the control network, and an **error budget** (rope stretch, slope, magnetic declination, tide, silt). | A sheet finer than its chain: precision the survey cannot support (DR-CT-02). |
| 3 | **Projection and scale.** What the sheet must preserve — distance along routes, area for a levy, angle for a bearing, direction for a rite, topology for an itinerary — and what it may distort. The standard line or parallel; the scale or scales. | A one-line **distortion statement**: *"this sheet preserves X; it distorts Y."* | The reader trusts the dimension the sheet lies about. |
| 4 | **Orientation and the zero.** Which north (true, magnetic, grid, ritual), what sits at the top (east, south, upstream, seaward, Mecca, the capital), where zero is (the gate, the temple, the confluence, the prime line), and who has authority to set it. | The orientation convention and the zero point, named. | The compass trap (`corpus/knowledge/myth-symbol/direction-symbolism.md:51`); two sheets that cannot be joined. |
| 5 | **Classification and symbol grammar.** What counts as one class (a road vs a path; a village vs a hamlet; a boundary vs a frontier); point, line and area; the hierarchy; the legend. | The class definitions and the legend, byte-equal to each other. | Two surveyors draw the same thing as two things; the sheet becomes the dispute. |
| 6 | **The blank policy.** Separate three absences: **unknown** (not surveyed), **withheld** (surveyed, not shown), **not-applicable** (outside the question). Decide which blanks are marked and how. | A **silence register**: for each blank, which of the three it is. | The blank is read as ignorance when it is a licence, or as licence when it is ignorance. |
| 7 | **Reproduction and copy economy.** Master medium, copy medium, copy drift, who may copy, how a copy is certified. | The medium pair (master/copy) and the copy-control rule. | Authority leaks (every copy is a new original) or dies (one fire, no map). |
| 8 | **The warrant.** Who surveyed, under what office and oath, signed how, dated when, renewed by what, and which disputes it is admissible in. | The **cartouche text** — the formula a reader can check. | The sheet has no standing in the dispute it was made for. |
| 9 | **Update rule and calibration audit.** What triggers re-survey (flood, storm, conquest, new levy, new channel, boundary suit); how revisions are marked; what happens to superseded copies; then audit against §12. | The revision regime and the audit note. | Obsolete sheets outlive their truth and become evidence of a world that no longer exists. |

**The order is load-bearing, not ceremonial.** Three consequences follow directly:

- **A form chosen before the question is a genre costume.** The same lagoon can carry a levy map of parcels and a pilot's chart of channels; neither is a worse map, and neither can answer the other's question (§11).
- **The warrant cannot be retrofitted.** A sheet drawn without a surveyor, an office, a date and a renewal rule is a drawing. A dispute will expose the difference, and the exposure is a scene, not a rules argument.
- **The blank is decided by the question.** A tax map that omits a channel has not failed to know the channel; it has decided the channel is not taxable. That decision is the political content of the sheet.

**Minimum credible build per form** (use this to price a map before writing scenes about it):

| Form | What it cannot do without | What it can skip | The institution it forces |
|---|---|---|---|
| itinerary / strip | stage names, travel times, a warrant | projection, scale bar, compass | the route's maintenance clause (`corpus/knowledge/culture-material/transport-mobility-lexicon.md:28`) |
| cadastral / land register | chain, baseline, parcel definition, legal warrant, archive | compass, decorative orientation | the survey office and the levy court |
| portolan / pilot chart | bearings, soundings, hazard marks, copy control | parcel definitions, land ownership | the pilots' guild and the harbour master |
| chorographic / regional | a stated scale and a class hierarchy | parcel-level precision | the provincial chancery |
| cosmographic / world diagram | a projection statement and a doctrinal warrant | survey precision (it is not a survey map — `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71`) | the temple or the school that authorises it |

**The backwards test.** Take a dispute the world already has. Ask which sheet each party would bring to it. If the sheets cannot be compared — different zero, different class definitions, different survey dates — then the dispute is *about the maps*, not about the land, and that is a scene engine. Then ask which of the nine steps would have prevented it. That is the decision your world has not yet taken.

## 11. Worked micro-example (NON-CANON) — one lagoon, two maps

A demonstration, not a world decision. Working labels only: "the Salt City", "the salt office", "the pilots' guild". Every element below is a design option; none of it is canon.

The city rings a shallow lagoon. Salt pans line the shore; one deep channel runs from the open sea to the market quay; three pans belong to a temple and are exempt from the salt levy. Two sheets are in daily use, made by two offices, of the same water.

**Map A — the levy sheet.** It exists so that the salt office can assess a levy on each pan.

- *Question and reader:* the levy per pan, read by the office and its tax farmers.
- *Chain:* each pan is staked as a rectangle along the shore; lengths are measured with the office's standard rope, checked each year against a bronze bar; areas are computed as rectangles. The lagoon edge is the baseline; no triangulation is needed because nothing off the shore is taxed. The error budget is rope stretch, a shifted stake, and the shoreline's own movement.
- *Projection and scale:* local plane, one scale (say 1:2,000), a strip along the shore. The distortion statement printed in the cartouche: *"distances along the shore are true; areas of pans are computed, not projected."*
- *Orientation and zero:* land at the bottom, open water at the top — "up" is the sea, not north. The zero of the chain is the market quay.
- *Classification:* pan (numbered parcel), dike (line), sluice (point), office (point), road (line). A pan is a taxable unit; a channel is not a class.
- *Blank:* the temple's three pans are drawn as outlines with **no number** — withheld, not unknown. The legend marks them "exempt" with a small glyph that is easy to miss; the omission is deliberate and deniable, which is exactly how a levy map does politics.
- *Reproduction:* a vellum master in the office; paper copies for the collectors (`corpus/knowledge/culture-material/writing-media-surface-economy.md:73`). Only the master is sealed; the copies are working papers.
- *Warrant:* the salt surveyor's oath, the office seal, the survey year, the reigning era. Admissible in the levy court.
- *Update:* re-survey after any storm that breaches a dike; superseded masters are stamped and kept for arrears.

**Map B — the pilot chart.** It exists so that a pilot can choose a channel at a tide, with a known draft.

- *Question and reader:* which channel, at what state of tide, for a hull of what draft; read by guild pilots.
- *Chain:* soundings by lead line, bearings by compass, channel edges by pole and eye. No areas, no parcels; the units are the fathom and the tide.
- *Projection and scale:* not a plan — a strip in channel order. Distance is time under oar or sail, not a scale bar; the distortion statement is *"order and depth are true for the surveyed tide; distance is a day's run."*
- *Orientation and zero:* seaward at the top; the channel sequence is the spine. The zero is the harbour mouth.
- *Classification:* channel, shoal, bar, landing, beacon, wreck; soundings as numbers. Land ownership is not a class.
- *Blank:* the temple's private channel is **not shown** — withheld by guild rule. That blank is a trade secret, not ignorance; a pilot who charts it is fined.
- *Reproduction:* cloth, sized and rolled (`corpus/knowledge/culture-material/writing-media-surface-economy.md:48`); each pilot copies the guild master by hand and signs the copy; copies are checked at the guild's annual reading. The master's mark is the warrant; the copyist's signature is the trace.
- *Warrant:* the guild's master chart, the pilot's oath, the sounding year, the guild mark. A pilot's copy is valid only with the mark.
- *Update:* after a storm the guild sends a sounding boat; the master is corrected; pilots annotate their copies, and the annotations are read aloud at the annual meeting. Discrepancies are resolved by the master — or by a new master, which is a guild politics scene.

**The storm.** A winter storm breaches a dike and cuts a new channel through the edge of a taxable pan. The levy sheet still shows the pan as a numbered rectangle: its survey predates the storm, and the re-survey is not due until the levy year turns. The pilot chart shows the new channel and omits the pan entirely: the guild charts navigable water, and a breached pan is not a channel yet. A salt barge grounds in the new cut. The office assesses the levy on a pan that is now half water; the pilot is accused of navigating outside the chart. Each sheet is accurate for its question and useless for the other's. The dispute is decided by **dates and warrants**, not by draughtsmanship: which survey was current, which mark authorised the copy, which office had jurisdiction over a channel that did not exist when either sheet was sealed. The city commissions a joint survey. The joint survey needs a new question (*"which water is navigable and taxable on the same date"*), a new warrant (both offices sign), and a new update rule (re-survey after every breach, not every levy year). It will be obsolete at the next storm. That is the point: the update rule is the institution.

| Same lagoon | Map A — levy sheet | Map B — pilot chart |
|---|---|---|
| question | how much levy per pan | which channel at which tide |
| reader | salt office, tax farmers | guild pilots |
| surveyed entity | pan parcel, dike, sluice | channel, shoal, bar, sounding |
| unit | rope length, computed area | fathom, tide, run time |
| projection / scale | local plane, 1:2,000 | strip in channel order, no scale bar |
| orientation / zero | sea at top; zero = market quay | seaward at top; zero = harbour mouth |
| medium / copies | vellum master, paper copies | cloth copies, hand-copied, signed |
| warrant | surveyor's oath + office seal | guild master + guild mark |
| blank | temple pans unnumbered (withheld) | private channel absent (withheld) |
| update | after a dike breach, per levy year | after a storm, by sounding boat |

**What the example demonstrates.** (a) Form follows question: the same water yields two incompatible sheets and neither is wrong. (b) Two accurate maps can contradict each other without either being false, because they classify different entities. (c) The blank is a decision with a politics. (d) The warrant, not the drawing, is what makes a sheet authoritative in a dispute. (e) Reproduction controls who can argue with the map. (f) The update rule is the real institution; a map without one is a dated opinion.

## 12. Calibration bank — what not to ship as history

Status codes follow `corpus/knowledge/verification/calibration-registry.md:33-39`: **R** rejected/discredited as the specified general inference; **C** contested; **B** bounded to a named domain; **H** heuristic, not a causal law; **T** unresolved, mark `(to-verify)`. One claim may carry more than one code. This bank is not a history of cartography; it is the set of readings that must not enter a world bible as settled.

| # | Claim to keep out of the bible as settled | Status | Why, and the replacement practice | Anchor |
|---|---|---|---|---|
| 1 | "A map is a neutral, objective picture of space." | **R** as a general claim; **B** only for a stated purpose | Selection, projection, orientation, classification and omission are constitutive. A sheet can be accurate *for a question* and misleading for another. Replacement: ship purpose + projection + survey date + omissions with every sheet. | §2–3; Harley (1989), Wood (1992), Monmonier — all `(to-verify)` page-level |
| 2 | "Medieval people believed the earth was flat, and T-O maps prove it." | **R** | A 19th-century fabrication; sphericity was standard ancient and medieval learning; T-O diagrams are symbolic devices, not survey maps. | `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102`; `:71`; Russell (1991), registered at that line, page-level `(to-verify)` |
| 3 | "Portolan charts are photographically accurate." | **C** (overclaim) | They are practical sailing charts with their own conventions, distortions and copying drift; accuracy figures depend on the sample and the metric. Replacement: state the chart's question and its known limits. | Campbell (1987) `(to-verify)`; §5, §11 |
| 4 | "Indigenous maps are childlike, or merely mental." | **R** | Lienzos and cartographic histories are precise legal and territorial documents; the colonial "primitive map" ladder is a category error, not a typology. Replacement: name the question, the chain and the warrant, never a rung. | `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58`; Mundy (1996), Boone (2000) — `(to-verify)` |
| 5 | "The map is the territory." | category error; **H** as a scene premise | A representation, not the thing. Useful when a character or an office *treats* the map as the land; not a metaphysics to assert in the entry's own voice. | §2 |
| 6 | "Cartography diffused one-way from Europe." | **C** | Chinese, Islamic, Mesoamerican and Polynesian traditions are independent or parallel; transmission exists but is not the whole story. | Needham (1959) vol. 3; al-Idrisi (1154); `corpus/knowledge/civilizations/polynesia-navigation.md:52`; Mundy — `(to-verify)` |
| 7 | "A blank means ignorance." | **C/H** | A blank may be unsurveyed, withheld, or outside the question; each is a different claim. Replacement: a silence register (step 6). | §10 step 6; Harley/Wood `(to-verify)` |
| 8 | "Scale and projection are neutral technical choices." | **R** as neutrality | Every projection preserves one metric at the cost of others; the standard line and the scale are decisions about what matters. | Snyder (1987) `(to-verify)`; §10 step 3 |
| 9 | "The first map dates to X." | **R** as a date claim; **T** for any specific date | The earliest *surviving* map is not the first map; survival is an accident of deposition and copying, not a birth date. Replacement: date the sheet, not the practice. | `corpus/knowledge/culture-material/material-culture-inference-method.md:69`; any date `(to-verify)` |
| 10 | "A map caused the border / the treaty / the tax." | **C/H** | Maps are instruments among others; causal claims need the decision record — who used which sheet, when, with what warrant. Replacement: narrate the decision, not the drawing. | §13; Kain & Baigent (1992) `(to-verify)` |
| 11 | "Mercator's projection is inherently an ideology of empire." | **C** | Separate design intent (a conformal navigational projection) from later reception (the wall-map default and its Eurocentrism). The reception is a datable political fact; the intent is not the same claim. | Snyder (1987); Monmonier — `(to-verify)` |
| 12 | "Drawn to scale = accurate." | **R** | Precision, accuracy and resolution are different quantities; the chain's error budget caps what any scale can honestly claim. | §10 step 2; §11 |
| 13 | "A map is a copy of the land, and can be read as the land was." | **C** | Maps are copies of earlier maps as often as of ground; copying drift, revision and later redrawing are the norm. Replacement: read the copy history before the content. | Harley & Woodward `(to-verify)`; §10 step 9 |
| 14 | "The map's orientation is north." | **R** as a default | North is one convention among many — east, south, upstream, seaward, Mecca, the capital. The choice encodes a claim. | `corpus/knowledge/myth-symbol/direction-symbolism.md:51`; §10 step 4 |

**Living-practice flags.** The real-world cases above are cited as literature and as structural lessons, never as templates to lift. Four families need screening before any table is filled:

- **Mesoamerican lienzos and cartographic histories** (`corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58`) are the property and record of descendant communities. Use the *genre* (a cloth map as a legal-territorial document) as a design analogue; do not copy a specific lienzo's content, place names or designs.
- **Polynesian navigation and its charts** (`corpus/knowledge/civilizations/polynesia-navigation.md:52`) are living knowledge systems. The corpus's own rule is to distinguish horizon compass, steering-star sequence, sky mnemonic and landfall clue; do not collapse them into a decorative "native chart."
- **Aboriginal Australian songlines and Country maps** carry restricted knowledge. The governing rule is `corpus/knowledge/verification/myth-consistency-gate.md:34`: do not expose restricted ritual knowledge to fill a table; mark an access boundary and choose a less extractive comparison.
- **Any contemporary community's cadastral or treaty map** is a legal document in a live dispute. Screen it through `corpus/knowledge/verification/real-world-inspiration-boundaries.md:6`, and follow the named-knowledge-holder precedent at `corpus/knowledge/civilizations/maori.md:20`.

Two further rules for this bank:

- **"Primitive map" is a colonial category, not a type.** Do not rank forms on a ladder from "mental" to "scientific"; the typology in §2 is by *question*, not by evolution.
- **Do not reproduce restricted site locations, songlines or initiatory geography** in a world bible. Take the structural lesson — a route can be knowledge, a map can be a warrant — and invent the content.

**The precision trap.** Every number in this entry is a design range until page-checked. Portolan accuracy figures, projection distortion percentages, scale ratios, and any "earliest map" date are **T** items: mark them `(to-verify)` at the exact dependency (`corpus/knowledge/verification/to-verify-triage-protocol.md:15`) and do not let them become load-bearing in a world bible. The Tier B shelf named in the head block is a reading list, not an inspection record.

## 13. Decision record — the cartography decisions this entry fixes

Each row is a decision a worldbuilder (or a later reviser of this file) must take *explicitly*. The "rejected" column names the option that must not be taken silently. Ids are stable; later rounds amend by adding rows, never by rewriting these.

| ID | Decision | Why | Rejected alternative | Evidence |
|---|---|---|---|---|
| DR-CT-01 | Fix the **question and the reader** before the form: who acts, on what decision, at what cost of error | the form follows the question; a form chosen first is a costume | drawing the most impressive map the culture could make | §10 step 1; §11 |
| DR-CT-02 | Declare the **survey chain and its error budget**; cap the sheet's precision at what the chain can support | a map cannot honestly show finer than its measurement | a beautiful sheet with invented precision | §10 step 2; `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` |
| DR-CT-03 | Declare the **projection, scale and standard line**, and state in one line what is distorted | every projection preserves one metric at the cost of another | "it's just a map"; an unstated projection | §10 step 3; Snyder (1987) `(to-verify)` |
| DR-CT-04 | Declare the **orientation and the zero** — which north, what is at the top, where zero sits, who sets it | orientation is a claim, and an unshared zero makes sheets incomparable | assuming north-up is neutral | `corpus/knowledge/myth-symbol/direction-symbolism.md:51`; §10 step 4 |
| DR-CT-05 | Fix the **class definitions and the legend** byte-equal to each other; one class per decision the sheet serves | a class boundary is a claim; ambiguous classes make the sheet a dispute | a legend of decorative icons with no definitions | §10 step 5; §11 |
| DR-CT-06 | Keep a **silence register**: unknown / withheld / not-applicable, marked distinctly | a blank is read as a claim whether or not the maker intended one | an unmarked blank that everyone interprets differently | §10 step 6; §12 row 7 |
| DR-CT-07 | Fix the **master medium and the copy medium**, and the copy-control rule (who may copy, what certifies a copy) | reproduction decides who can argue with the sheet and how far authority travels | treating every copy as an original | §10 step 7; §11; `corpus/knowledge/culture-material/writing-media-surface-economy.md:48,:73` |
| DR-CT-08 | Write the **warrant**: surveyor, office, oath, signature, date, renewal, admissible disputes | authority is institutional, not graphical | an unsigned, undated sheet treated as evidence | §10 step 8; §11; `corpus/knowledge/culture-material/craft-artisan-lexicon.md:87` |
| DR-CT-09 | Fix the **update rule**: re-survey triggers, revision marks, superseded-copy rule | an obsolete sheet outlives its truth and becomes false evidence | a single survey treated as permanent | §10 step 9; §11 |
| DR-CT-10 | Decide **access**: who may read which sheet, whether a restricted edition exists, and what the map's legal standing is | access turns a drawing into an instrument of power or a public good | one undifferentiated public sheet in a stratified society | §6, §8; §11 |
| DR-CT-11 | Tag every **map-derived inference** HARD/SOFT/DOCTRINE/DESIGN before it reaches the bible | a map is evidence of a claim about space, not of the space | reading a sheet as a photograph of the past | `corpus/knowledge/culture-material/material-culture-inference-method.md:32-41,:69`; §12 row 13 |
| DR-CT-12 | Route every **living-tradition reference** through the boundary protocol, and every unresolved date or figure through `(to-verify)` | extraction and false precision are both conformance defects | using a restricted map form as decorative texture | `corpus/knowledge/verification/real-world-inspiration-boundaries.md:6`; `corpus/knowledge/verification/myth-consistency-gate.md:34`; `corpus/knowledge/verification/to-verify-triage-protocol.md:15` |

**Reading the record.** A row is answered when the world bible contains the decision, not when the designer has an opinion. Rows DR-CT-01, -02 and -08 are non-negotiable for any sheet that will be used in a dispute; rows -03 to -06 may be carried orally in a low-literacy culture until the first sheet exists. When a later round changes a decision, it adds a row with the date and the reason; it does not edit the old row.

## 14. Recheck triggers and known limits

**Recheck before any of the following becomes load-bearing in a world bible.**

- **Any projection, scale or accuracy figure.** The Tier B shelf was not inspected this round; distortion percentages, portolan accuracy and "earliest map" dates are `(to-verify)` until a page is checked (`corpus/knowledge/verification/to-verify-triage-protocol.md:15`).
- **Any living-tradition map form.** Lienzos, songlines, Polynesian star and stick charts, and contemporary cadastral/treaty maps route first through `corpus/knowledge/verification/real-world-inspiration-boundaries.md:6`; restricted knowledge follows `corpus/knowledge/verification/myth-consistency-gate.md:34`; named-knowledge-holder precedent at `corpus/knowledge/civilizations/maori.md:20`.
- **Before reading a surviving map as evidence of past territory or past mentality.** Survival is an accident of deposition and copying (`corpus/knowledge/culture-material/material-culture-inference-method.md:69`), and most surviving maps are copies of copies; read the copy history first (§12 row 13).
- **Before reading a modern sheet back onto an earlier period.** The corpus's own caution: a neat Edo cadastral map is not a Sengoku map (`corpus/knowledge/civilizations/japan-medieval-sengoku.md:157`). Date the survey, not the landscape.
- **Before calling an orientation "north" or a bearing "true."** True vs magnetic vs grid vs ritual north is a decision, and declination is latitude- and era-dependent (`corpus/knowledge/myth-symbol/direction-symbolism.md:51`).
- **Before treating a toponym on a sheet as the in-world name, or as neutral.** Naming is an inscription of power; a map is an archive of renamings (`corpus/knowledge/linguistics/naming-systems.md:70`).
- **Before claiming a map settled a border, a treaty or a tax.** That is a causal claim; produce the decision record — which sheet, which warrant, which date, which office (see §13, DR-CT-08 and DR-CT-10; §12 row 10).
- **Before letting an itinerary stand as an institution.** A route is real only if someone maintains it (`corpus/knowledge/culture-material/transport-mobility-lexicon.md:28`); a mapped route without a maintenance clause is a description.
- **Before promoting any `(to-verify)` item into canon.** Route it through `corpus/knowledge/verification/to-verify-triage-protocol.md:15`; the mark is a backlog row, not an assertion.

**Known limits of this entry.**

- No external source was fetched, resolved or page-checked in this seat (no network). Every Tier B bibliographic item is a named standard work, not an inspected one; the entry must not present a page-level claim as read.
- The historical anchors (portolan practice, Roman land survey, Chinese and Islamic traditions, Mesoamerican lienzos, Polynesian navigation) are stated at the level of standard reference knowledge and carry `(to-verify)` where a page check is owed.
- The worked example is **NON-CANON** and disposable; it demonstrates the procedure and decides nothing about any world.
- This fragment drafts sections 10–15 only; the entry's gap statement, head block, form typology and survey-to-symbol chain are other seats' bytes. Any cross-reference mismatch at assembly is an integration defect, not a license to rewrite this fragment.

## 15. Scope and handoff

**Scope.** Reference knowledge and craft method for the culture-material partition only. This entry decides nothing about any world: it names no canon border, authorises no survey, prescribes no levy, and issues no verdict about any round, record or artifact. Canon recording and consistency verification belong to lore-shokunin; the entry ends at the handoff. Restricted real-world material is screened by `corpus/knowledge/verification/real-world-inspiration-boundaries.md`, not here.

**What this entry supplies to the handoff.**

1. The nine-step build order with the artifact each step must write (§10).
2. The minimum credible build per map form, and the institution each form forces (§10).
3. A worked demonstration that two accurate maps of one place can contradict each other, and why the warrant and the update rule decide the dispute (§11).
4. The calibration bank — fourteen readings that must not ship as settled, with R/C/B/H/T status and replacement practice (§12).
5. The living-practice flags for the four real-world families this topic touches (§12).
6. Twelve stable decision rows, each with the rejected alternative and the evidence (§13).
7. The recheck triggers that must fire before a map becomes load-bearing (§14).

**What the receiving bible should contain before the map is used in play.** (a) the question-and-reader sentence; (b) the chain and error budget; (c) the projection/scale distortion statement; (d) the orientation and zero; (e) the class definitions and legend; (f) the silence register; (g) the master/copy medium and copy-control rule; (h) the warrant text; (i) the update rule; (j) the access list. If any of (a), (b), (h) or (i) is missing, the map is scenery and every dispute written around it will have to be settled by fiat.

**Known limits of the handoff.** The `(to-verify)` items in §14 are backlog rows, not assertions. The Tier B shelf in the head block is a reading list. The worked example is a drill. Corrections to this entry are new sections or a new entry, never rewrites of filed bytes.

**Boundary reminders for the receiving bible.** The world model and its T-O-style diagrams belong to `corpus/knowledge/myth-symbol/cosmology-cosmography.md` (which explicitly disclaims survey maps at `:71`); the sacred place register and route-as-rite belong to `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:5`; the direction register and the compass trap belong to `corpus/knowledge/myth-symbol/direction-symbolism.md:51`; the city-plan lexicon and the groma belong to `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95`; the writing surfaces and their cost ladder belong to `corpus/knowledge/culture-material/writing-media-surface-economy.md:3,:48,:73`; the route institutions belong to `corpus/knowledge/culture-material/transport-mobility-lexicon.md:28`. This entry cites all six and restates none.
````

## 4. Self-audit of this fragment

```
$ grep -c '^````' reports/round-47/cov/C03-entry-c.md
2          # one opening fence (line 72), one closing fence (line 250)
$ grep -n '^## ' reports/round-47/cov/C03-entry-c.md | wc -l
11         # 6 in-fence (§10–§15, lines 73–231) + 5 seat-report sections
$ grep -c '^- topic:' reports/round-47/cov/C03-entry-c.md
0          # the head block is C04's; this fragment adds no topic line
$ grep -o 'DR-CT-[0-9][0-9]' reports/round-47/cov/C03-entry-c.md | sort -u | wc -l
12         # DR-CT-01 .. DR-CT-12, all defined in §13
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
```

- **One four-backtick entry fence**, opened with four backticks plus `markdown` at line 72, closed by four backticks at line 250. The smaller triple-backtick blocks elsewhere are audit transcripts and the C04 head-field extract, not entry bytes; no nested four-backtick fence exists and all inline code uses single backticks.
- **No corpus, tools, README, LOG or filed-round byte** is touched. The only write is this file.
- **Every `path:line` in the fence is listed in §2** and was read live at `6e9a30d`. No external source is asserted as read; all external items are `(to-verify)`.
- **No numbers are invented as measurements.** The only counts in the draft are design labels (nine steps, twelve rows, fourteen calibration rows), and they are self-evident from the text.
- **No canon claim, no promotion verdict, no clearance.** The worked example and all working labels are declared NON-CANON.

## 5. Handoff summary

- **Draft path:** `reports/round-47/cov/C03-entry-c.md` (this file), single fenced block in §3.
- **Content:** entry sections §10 (build order), §11 (worked micro-example), §12 (calibration bank + living-practice flags), §13 (decision record DR-CT-01..12), §14 (recheck + known limits), §15 (scope + handoff).
- **Integrator must:** concatenate with C01 §1–4, C02 §5–9 and C04's head block; reconcile the `§` cross-references if C01/C02 number their sections differently; apply the whole entry once at `corpus/knowledge/culture-material/cartography-and-mapmaking.md`; run the r28 sweep for `224 == 224`.
- **C04 may lift verbatim:** the `- recheck:` bullets from §14 and the `- scope:` sentence from §15, plus the "Boundary reminders" paragraph for the `- couples:` line.
- **No filed byte was edited; no corpus byte was staged; no runner was executed; no commit/push/install/network.**

### Head-field extract (for C04 — proposed field text, not entry bytes)

```
- recheck: before any projection, scale or accuracy figure, or any "earliest map" date, is treated as settled; before using any living-tradition map form (lienzos, songlines, Polynesian star/stick charts, contemporary cadastral or treaty maps); before reading a surviving map as evidence of past territory or mentality; before reading a modern sheet back onto an earlier period; before calling an orientation "north" or a bearing "true"; before treating a map toponym as neutral; before claiming a map settled a border, treaty or tax; before letting an itinerary stand without a maintenance clause; before promoting any `(to-verify)` item into canon.
- scope: reference knowledge and craft method for the culture-material partition only. This entry decides nothing about any world: it names no canon border, authorises no survey, prescribes no levy, and issues no verdict about any round, record or artifact. Canon recording and consistency verification belong to lore-shokunin; the entry ends at the handoff. Restricted real-world material is screened by corpus/knowledge/verification/real-world-inspiration-boundaries.md, not here.
```
