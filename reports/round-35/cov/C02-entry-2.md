- Seat: C02 | executor | claim C | date 2026-10-19 | baseline 4a7aede

# C02 — culture-material entry 2 of 6 (draft bytes for the integrator)

Mission (verbatim, `reports/round-35/targets.json` seat C02): *"Author entry 2 (culture-material) with the same contract."* Out path: `reports/round-35/cov/C02-entry-2.md`.

Dependency status (updated at final verification): `plan/P01-c-plan.md` is **still absent** (`ls reports/round-35/plan` → `P02-oa-plan.md` only); `scout/K01-coverage-census.md` **landed during this pass** and is folded in below (§1 second-reader bullet; `## Owed`). The first check of this pass ran before this write (`ls reports/round-35/cov reports/round-35/scout reports/round-35/plan` → all three: No such file or directory). Per the missing-dependency rule this seat selected its own topic from a live census (below) and drafted the entry; K01 §2.3 independently ranks the same register as candidate gap CM-1 (mentions 21, topic-owners 0), and the topic remains owed to P01 for confirmation (see `## Owed`).

Contract applied — derived from live corpus bytes, not from memory: the two newest entries (`transport-mobility-lexicon.md`, `plant-symbolism.md`) plus the round-19 audit instrument `reports/round-19/audit/entry-audit.py:25-31` define the field set and the mechanical checks. Its regexes were replicated inline (never executed in-tree from a filed round path) and run against this draft; results in §Self-audit. Two contract deviations are filed as findings in §Findings.

**Proposed target path (integrator applies):** `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md`

---

```markdown
# Agrarian Field-System Lexicon — Land, Plough, Water, Crop Labor, and the Words the Harvest Leaves Behind

- gap: the agrarian register is absent from culture-material — the partition owns food-as-meal, containers, textiles, mobility, trade, and the built environment, but no entry owns the field system itself (parcel, plough, water delivery, rotation, harvest labor, storage, tenure); the census in §1 shows the register's core terms returning zero files corpus-wide while the two nearest siblings explicitly push the reader elsewhere — the gap this entry fills
- topic: the field system as the substrate under every other material register — the FOUR INSTITUTIONS (parcel, implement, water, claim) that any fictional agrarian economy must name, and the vocabulary each one generates. Master claim: a culture's agrarian lexicon is generated at the seams where three quantities (yield per unit area, water control, labor calendar) meet four institutions, so an author who fixes the peak-labor month, the water source, and the harvest claim first gets the field, plough, measure, and status words almost for free. The entry supplies: a ten-system field typology with labor/tenure/lexical signatures; the plough family (ard, coultered mouldboard, wheeled) as a capacity chain, not a progress ladder; the water chain (source → lift → deliver → right) with the baray/qanat/acequia/paddy cases; rotation and crop-loanword clocks; the harvest tool-and-share vocabulary; the work-unit land measures (jugerum, morgen, acre, hide, carucate); a calibration shelf of the framework's contested claims (heavy-plough revolution, plough→gender, hydraulic despotism, rice culture); and a decision record for authors
- sources:
  - In-repo anchors (resolve on disk at baseline 4a7aede; every line re-read in this pass): `corpus/knowledge/culture-material/material-culture-inference-method.md:13,:33,:61,:66,:73,:75,:105` — constraint→form spine, "constraints, not causes", the plough→gender exemplar chain and its mechanism critique; `corpus/knowledge/culture-material/cuisine-food-lexicon.md:17,:26,:27,:157` — staple skeleton (wet-rice water control and terraces, wheat milling, maize nixtamalization), FAO 2026 FAOSTAT ~40% calorie share, potato-as-era-seam (Nunn & Qian 2011), rice-culture calibration row; `corpus/knowledge/culture-material/calendar-festival-systems.md:52,:116,:167` — the Egyptian three-season agricultural year, the autumn-harvest festival row (harvest stored → tithes, debts, assembly), the festival-arc build step; `corpus/knowledge/culture-material/textile-technology.md:11,:21,:76` — the fiber gate ("what the land raises"), flax/hemp as field crops with their retting chains, the stink-trade euphemism seam; `corpus/knowledge/culture-material/trade-economy-lexicon.md:17` — measures drawn from body, measured substance, the action ("a day's plowing"), container; `corpus/knowledge/culture-material/transport-mobility-lexicon.md:29,:88-98` — mobility-as-capacity rule and the draft/wheel capacity chain; `corpus/knowledge/culture-material/vessel-container-lexicon.md:34` — the STORAGE job (bulk, pests, damp; buried-to-the-shoulder forms); `corpus/knowledge/civilizations/austronesia-philippines-taiwan.md:109-126` — the Ifugao *muyong–uma–payo* land-use complex with tenure and labor attached to each term; `corpus/knowledge/civilizations/khmer-angkor.md:146-149` — Old Khmer water/ricefield vocabulary (*dik¹*, *travāṅ*, *taṭāka*, *sre*) and the warning that one word does not identify irrigation scale; `corpus/knowledge/civilizations/nazca.md:37,:105` — puquio construction as a dated technological horizon, and the underground-water map as a contested overreading control
  - Inherited bibliography (standard works, cited through the in-repo entries above or as standard reference; **not re-fetched in this seat — no network at seat time**): Boserup (1965) *The Conditions of Agricultural Growth*, Aldine (via `material-culture-inference-method.md:13`); Alesina, Giuliano & Nunn (2013), "On the Origins of Gender Roles: Women and the Plough", *QJE* 128(2) (via same line); Vu (2025), CAMA Working Paper 11/2025 and Giuliano & Nunn (2021), *RES* 88 (via `:105`); Steward (1955) *Theory of Culture Change* (via `:14`, constraints-not-causes); Wittfogel (1957), *Oriental Despotism* (to-verify — critique cited from standard literature, not re-read here); White (1962), *Medieval Technology and Change* (to-verify — same); Sherratt (1981), "Plough and pastoralism: aspects of the secondary products revolution" (to-verify — same); Zeder (2006), "Central questions in the domestication of plants and animals", *Evolutionary Anthropology* 15 (to-verify — founder-crop list not re-read here); Bray (1984), *Science and Civilisation in China* 6.2 *Agriculture* (to-verify — rice-farming detail not re-read here); Cato *De agri cultura*, Varro *Rerum rusticarum*, Columella *De re rustica*, Pliny *Naturalis Historia* 18 (Roman field practice — inherited, editions to-verify); Hesiod *Works and Days* 383–617 (the farmer's almanac — inherited, to-verify); Deut 25:4 (ox not muzzled while treading — textual, to-verify against a critical edition); Bloch (1931) *Les caractères originaux de l'histoire rurale française* / English trans. *French Rural History* (open fields, to-verify); Hopkins (1978) *Conquerors and Slaves* (Roman latifundia and slave estates, to-verify); Scott (2017) *Against the Grain* (grain state, tax and legibility, to-verify); Talhelm et al. (2014), *Science* (rice theory — via `cuisine-food-lexicon.md:157`)
- couples: culture-material/cuisine-food-lexicon.md (that file owns food-as-meal, taboo, and the staple skeleton; this file owns the field that produces the staple — the split is stated at its §1 and its calibration shelf is the model for §10 here); culture-material/calendar-festival-systems.md (the agrarian year is its raw material — harvest assembly and sowing-month rows; this file supplies the labor calendar behind them); culture-material/textile-technology.md (fiber crops are field crops — flax/hemp retting and the fiber gate are the same land decision as the food crop); culture-material/transport-mobility-lexicon.md (draft animals, yoking, and the capacity-chain rule are shared; that file owns the road, this one the field the road drains); culture-material/trade-economy-lexicon.md (measures come from the action "a day's plowing" — this file supplies the action, that file the market); culture-material/vessel-container-lexicon.md (STORAGE job: the granary/pit/rick inventory is that file's container typology applied to bulk); culture-material/architecture-settlement-lexicon.md (granary, threshing floor, and field-ward settlement siting couple the dwelling file to the field system); culture-material/material-culture-inference-method.md (this file takes its plough→gender and constraint→form rows and gives them the partition's full treatment; shared substrate-inventory contract); linguistics/semantic-fields-lexicon-building.md (agrarian fields are a high-elaboration semantic field; the borrowability strata govern crop and implement loans); linguistics/naming-systems.md (field names and microtoponyms are the densest toponym layer a rural culture has; critical toponymy applies to land reform); linguistics/language-contact.md (crop and implement loan chains are contact receipts — date referent and word separately); linguistics/politeness-taboo-euphemism.md (manure, night-soil, and the stink trades sit downstream of euphemism, as textile-technology.md:76 already notes for retting); myth-symbol/ritual-liminality.md (first-furrow, first-fruits, and harvest-home are rites of passage for the year and for the crop); myth-symbol/plant-symbolism.md (the flora register's sacred plants are cultivated plants — that file owns the symbol, this one the cultivation); myth-symbol/divination-omen-systems.md (weather and flood omens are the agrarian risk layer); civilizations/austronesia-philippines-taiwan.md + civilizations/khmer-angkor.md + civilizations/nazca.md (three worked land-use systems with their own vocabularies — exemplars, not transplants); synthesis/coupling-model.md (this file's four institutions are a coupling contract for era/lexicon work); synthesis/worldbible-integration-contract.md (handoff route); recipient: lore-shokunin (reference-only, no canon writes — AGENTS.md)
- source: in-corpus locators are the anchor list in `- sources:` above (each `path:line` resolves at baseline 4a7aede; re-checked this pass, command in §Self-audit of the seat fragment) plus the inherited bibliography carried by those entries. No URL was fetched in this seat (no network at seat time), so this entry is a **source map, not a verified history** — every external work above carries `(to-verify)` on any figure or date that this seat could not re-read
- verified-at: 2026-10-19 — round-35 authoring pass, seat C02, baseline 4a7aede: every in-repo `path:line` anchor re-read live in this pass and each cited line number re-checked against the file (census commands and their outputs reproduced in §1 and §11); **no network in this seat**, so no external source was re-fetched and every external figure, date, or equivalence below is flagged `(to-verify)` and must not be canonized before a fetch pass lands
- recheck: before fixing a plough type, a rotation, a yield ratio, a team size, a water-right term, or a land-measure equivalence as in-world fact — re-run §10 against the claim, then re-derive the culture's labor calendar from §9 rather than importing a real one

## 1. The gap this entry fills — census, and what the two nearest siblings do not own

- Live census at baseline 4a7aede, whole corpus (files matching, case-insensitive) — command: `for t in "three-field" "open field" "chinampa" "qanat" "shaduf" "noria" "acequia" "fallow" "granary" "Geoponica" "Columella" "mouldboard" "carucate" "virgate" "tribulum" "flail" "swidden" "paddy" "Hesiod"; do printf "%-12s %s\n" "$t" "$(grep -ril "$t" corpus/knowledge/ | wc -l)"; done`; output, term → files:

| term | files | term | files |
|---|---|---|---|
| three-field | 0 | Geoponica | 0 |
| open field | 0 | Columella | 0 |
| chinampa | 0 | mouldboard | 0 |
| qanat | 1 | carucate | 0 |
| shaduf | 0 | virgate | 0 |
| noria | 0 | tribulum | 0 |
| acequia | 1 | flail | 0 |
| fallow | 3 | swidden | 1 |
| granary | 3 | paddy | 2 |
| Hesiod | 8 | (blank cell — no second term) | — |

- Second reader for the same gap: `reports/round-35/scout/K01-coverage-census.md` §2.3 ranks **CM-1 agriculture / subsistence system — field, plough, irrigation, fallow/rotation, crop calendar, land tenure** as the first culture-material candidate gap (mentions 21 of 201 files, topic-owners **0**, first hits `civilizations/amazigh-berber.md:146`, `civilizations/bali.md:14`, `civilizations/carthage.md:63`), and §2.5 names the agriculture/subsistence slot first in the claim-C allocation. This entry's own keyword sweep above is the re-run K01 §2.2 requires of the author; the two counts differ in method (different keyword sets) and both read the register as unowned.

- The words exist in the culture's mouth, not in the corpus: the lane has a food entry, a container entry, a textile entry, a mobility entry, a market entry, and a built-environment entry, and **no entry that owns the land itself**. The nearest siblings hand the reader away rather than absorbing the register — `cuisine-food-lexicon.md:26` names the ecological constants (wet-rice water control and terraces; wheat's milling and oven chain; maize's nixtamalization) as *constants behind* the foodway, and `textile-technology.md:11` states the fiber gate as "what the land raises" before moving to cloth. Both presuppose a field system this partition does not describe.
- What this entry does not take from its siblings, stated as the partition rule: **food-as-meal, taboo, and fermentation stay in `cuisine-food-lexicon.md`; the granary's containers stay in `vessel-container-lexicon.md`; fiber processing stays in `textile-technology.md`; haulage stays in `transport-mobility-lexicon.md`.** This file owns parcel, implement, water, rotation, harvest, storage-as-bulk, and tenure.

## 2. Frame: four institutions, three quantities, one derivation order

- Three quantities set every agrarian system: **yield per unit area** (what the land returns per hectare per year, and how much of it is seed returned to the ground), **water control** (who delivers water, when, and who may be denied it), and **labor calendar** (how many hands are needed in which month, and what those hands eat in the other months).
- Four institutions turn the quantities into words:

| Institution | What it decides | Vocabulary it generates |
|---|---|---|
| PARCEL | who holds the ground, by what right, owing what | field names, boundary words, tenure words, land measures |
| IMPLEMENT | what breaks the soil, and what it costs upstream | plough/hoe words, team and yoking words, repair and iron words |
| WATER | where it comes from, how it is lifted, who gets the turn | source/lift/channel words, water-right and water-office words |
| CLAIM | who takes a share of the harvest, and how it is enforced | tithe/rent/tax words, storage words, status words (free/owing) |

- Master claim, in one line: **name the peak-labor month and the harvest claim first; the parcel, implement, and water words then fall out of them.** A culture with a single labor peak (paddy transplanting; the Nile flood's basin sowing) gets cooperative labor words and a communal water office; a culture with a spread calendar (dryland grain plus herd) gets household strips and a private plough team.
- The derivation is a cost gradient, not a destiny: material constraints "set cost gradients inside which the culture's optimization function selects" (`material-culture-inference-method.md:61`), and a chain with zero named choices "is a deterministic trap, not a culture" (`:76`). Every table below therefore ends in a design question, not an answer.

## 3. Field-system typology — ten systems, their labor signatures and the words they make

| System | Land form | Labor signature | Water regime | Tenure trace | Vocabulary generated | Real exemplar / anchor |
|---|---|---|---|---|---|---|
| swidden / shifting | forest or scrub, felled and burned | heavy felling work, long fallow (the field rests longer than it works) | rain only | usufruct, lineage-held, no permanent parcel | felling/burning words; an old-field vs new-burn pair | standard; `swidden` appears once corpus-wide (census §1) |
| rain-fed dryland (ard) | open plain, light soils | household + one plough team; ploughing and sowing peaks | rain only, drought risk | household strips, redistributed by inheritance or lot | fallow, stubble, glean(ing) | Lev 19:9–10 gleaning (textual, to-verify) |
| heavy-plough open field | heavy clay, needs drainage | plough team (the critical scarce input), communal herding after harvest | rain + drainage ditches | strips in furlongs, common pasture rights, manor court | furlong, selion, headland, "plough-land" | Bloch (to-verify); `carucate`/`virgate` absent corpus-wide (census §1) |
| flood-basin irrigation | river plain with levees and basins | dredging and dike corvée at the flood, then sowing as water recedes | basin flooding + canal gates | state or temple granary against a grain tax | season names, canal names, "the water's turn" | `calendar-festival-systems.md:52` — Egyptian Akhet/Peret/Shemu (inundation/emergence/harvest) |
| qanat / underground channel | piedmont fan, dry surface | tunnel maintenance by specialist guild; water arrives without lifting | gravity tunnel from an aquifer, mother well upstream | water shares traded apart from land (to-verify per region) | channel, mother-well, share-of-water words | `qanat` 1 file, `noria` 0 (census §1); detail to-verify |
| terrace | stepped hillside | terrace-wall maintenance as a permanent labor tax; ponding and drainage | captured rainfall + spring diversion, field-to-field flow | lineage or ward tenure; labor obligations attach to the wall, not only the plot | terrace-level names; land-use tiers | `austronesia-philippines-taiwan.md:109-126` — Ifugao *muyong* (forest) / *uma* (swidden) / *payo* (wet terrace), tenure and labor per term |
| raised field / chinampa | lake margin, canals between platforms | muck-lifting from canal to field, then cropping | canal water + lifted mud | ward/kin held, highly productive small parcels | canal, platform, mud words | Mesoamerican chinampa — `chinampa` 0 files (census §1); detail to-verify |
| paddy rice | level, bunded fields | transplanting and harvest peaks; dense cooperative labor and water control | bunded water, gravity or lifted, shared headworks | tax in grain; communal water office | bund, paddy, seedbed, water-of-X | `cuisine-food-lexicon.md:26` (wet-rice water control); `paddy` 2 files (census §1) |
| agropastoral | fields + pasture + transhumance routes | ploughing peak plus herd calendar; manure contracts | rain + wells | mixed: grain parcels + herd rights; manure-for-stubble exchange | fold, transhumance, stubble-right | standard; manure/night-soil euphemism seam — `textile-technology.md:76` |
| plantation / cash crop | monocrop blocks | imported or coerced gangs; single crop, single calendar | engineered (canal or rain) | estate; crop-lien and debt | estate, gang, "the crop is the rent" | standard colonial form; use as a designed rupture, not a default |

- Design question per row: *which of these is the culture's default, and which one is the one it remembers leaving?* The transition (swidden → terrace, dryland → basin) is where origin myths about land hunger are made.
- The table's vocabulary column is the deliverable: **each system generates a different word class first.** A terrace culture names levels and walls before it names fields; a qanat culture names shares of water before it names plots.

## 4. The plough family — a capacity chain, never a progress ladder

| Implement | Soils it opens | Team | Upstream requirements | Vocabulary generated | Calibration |
|---|---|---|---|---|---|
| digging stick / hoe | any, slowly | household | none beyond wood/stone/iron edge | dibble, hoe, seed-lip | hoe cultures are not "pre-plough" failures — they are labor-rich, capital-poor systems (design framing; to-verify against any regional literature before stating) |
| ard / scratch plough | light, dry, stoneless | 1–2 oxen | a trained team + yoke + a smith for the share | ard, share, sole, yoke, goad | symmetric, does not invert the furrow — the plough that the Mediterranean and the Near East actually used for millennia |
| coultered mouldboard plough | heavy, wet, weed-heavy | larger team (figures like 6–8 oxen circulate — **(to-verify)**; never quote unflaggged) | iron for coulter + board, strong team, fodder base, repair smith | coulter, mouldboard, furrow, plough-iron, ploughman | its spread and its causal role in a "medieval agricultural revolution" are **contested** — White (1962) thesis vs later economic/harness accounts (to-verify) |
| wheeled plough variant | same as above | same, with a wheeled fore-carriage | adds wheelwright work | wheel-plough, fore-carriage | regional; treat as a design choice, not a stage |
| horse-drawn ploughing | same, where fodder and harness allow | horses | collar harness, fodder surplus, larger farms | harness words, "horse-plough" | horse-vs-ox is an economics decision (fodder, speed, soil) — the "collar revolution" narrative is contested (to-verify) |

- **The capacity-chain rule** (shared with `transport-mobility-lexicon.md:29`): no implement appears without its upstream chain. A mouldboard plough needs iron, a smith, a fodder base, and a team — name all four or the plough is scenery. A culture with no draft animal of the right build simply does not have the heavy plough, whatever its era label says.
- **Plough → gender roles**: the hypothesis that plough agriculture shifted women out of field work (and thus out of the public sphere) is the partition's worked constraint→form exemplar (`material-culture-inference-method.md:13,:75`), and its mechanism is explicitly contested — the cross-country association replicates, the intergenerational-transmission evidence is sample-sensitive (`:105`, citing Vu 2025 and Giuliano & Nunn 2021). **Design rule:** use it as a generator with two rival in-world doctrines, never as a stated law (DR-AG-04).
- **Secondary-products revolution** (Sherratt 1981: traction, milk, wool, manure arriving after domestication) — a generator for "the animal that became a machine"; contested as a single horizon (to-verify).
- Vocabulary note: plough words are among the most conservative in a lexicon and among the most borrowed — the implement arrives with the loanword and often outlives it (`linguistics/language-contact.md`).

## 5. Water — the chain from source to right, and the four words every system needs

| Link | Options | What it demands | Words it generates |
|---|---|---|---|
| SOURCE | rain, river flood, spring, aquifer tunnel, lake, well, snowmelt | a seasonality the calendar must name | flood words, spring names, "the water's coming" |
| LIFT | none (gravity), shaduf-style lever, chain-of-pots wheel, waterwheel, bucket brigade, pump | a lift word and its operator; a lift-right | shaduf, saqiya/noria class words, "the lifting" |
| DELIVER | ditch, canal, qanat tunnel, aqueduct, bund/field-to-field, pipe | maintenance labor and a boundary word | channel, head, tail, breach, "the ditch's name" |
| RIGHT | rotation ("turns"), priority by seniority, measured shares, state allocation, market | an office and an enforcement procedure | turn, share, water-master/ditch-rider, first-water | 

- **Worked system, Khmer**: the in-repo vocabulary shows the split the table predicts — Old Khmer *dik¹* covers water/liquid and channels together, *travāṅ* is standing water/pond/reservoir, *taṭāka* is a Sanskrit loan for pond/reservoir, and *sre* is "ricefield, conventionally glossed as irrigated ricefield" — with the file's own warning that **one word does not identify the source or scale of irrigation**, and that the royal reservoir question ("only irrigation" vs "only cosmic ocean") has no automatic answer (`civilizations/khmer-angkor.md:146-149`).
- **Worked system, Ifugao**: land-use tiers carry their own obligations — *payo* (wet terrace) attaches irrigation, maintenance labor, tenure, and differential access; *uma* (swidden) is not a superseded stage but a parallel cultivation mode (`civilizations/austronesia-philippines-taiwan.md:115-116`).
- **Worked control, Nazca**: puquio construction is dated as a technological horizon in one phase model, and the file marks "a literal map of all underground water" as a **contested extrapolation** — spatial correlation does not establish intention (`civilizations/nazca.md:37,:105`). Use the same guard on any in-world "the ancients engineered all the water" doctrine.
- **Calibration row:** Wittfogel's "hydraulic despotism" (1957) — the claim that large-scale irrigation *causes* despotic state power — is rejected as a law in the standard literature (state formation precedes large works in several cases; see also the constraints-not-causes rule at `material-culture-inference-method.md:61`). Keep it as an **in-world ideology** that a bureaucracy tells about itself (to-verify the specific counter-cases before naming them in a draft).
- Water vocabulary design lever: a culture's water office is the cheapest place to hang a faction — the ditch rider who decides the turn is a character, not a table.

## 6. Rotation, crop suite, and the word the crop brings

- **Rotation is a clock the lexicon tells time by.** Systems worth naming: two-field (winter grain / fallow), three-field (winter grain / spring grain / fallow), ley with legumes, paddy double-crop, and the swidden cycle. The three-field form is regional and late in its European career — **do not universalize it** (flag; to-verify against the rural-history literature before dating it).
- **The crop suite is an inheritance with a map.** The southwest-Asian founder package (emmer and einkorn wheat, barley, lentil, pea, chickpea, bitter vetch, flax) is the standard list (Zeder 2006 — to-verify; list carried here as a design template, not a date claim). Its design consequence: a founder package is a **compatible set** — the legume in it fixes nitrogen and feeds the household, so the rotation and the diet are the same decision.
- **Referent time vs word time**: date the crop's arrival separately from its word's arrival, exactly as `transport-mobility-lexicon.md` does for vehicles (its DR-TR-03). A crop can arrive without its name (a borrowed food with a native word) or a name without the crop (a prestige term for something the culture does not grow). The in-repo anchor for the pattern is `textile-technology.md:83` — Arabic *quṭn* → *cotton / algodón / algodão*.
- Loan chains usable as templates (all intermediate steps **(to-verify)** before use in a draft): sugar (Sanskrit *śarkarā* → Arabic *sukkar* → medieval Latin *succarum* → the European sugar words), rice (Greek *oryza* and its westward chain), maize and potato (contact-era referents whose words spread with the plant — the potato's economic seam is `cuisine-food-lexicon.md:27`, Nunn & Qian 2011), wheat/trigo family, and the already-in-repo cotton chain.
- Design rule: give the culture **one staple with a native word, one with a loan, and one failed introduction** — the failed crop is where famine lore and agricultural extension satire live.

## 7. Harvest — the tool, the act, and the share

| Stage | Implement / practice | Vocabulary generated | Anchor |
|---|---|---|---|
| reaping | sickle (flint-bladed sickles leave cereal-silica gloss — the use-wear signature), later scythe | sickle, reap, "the reaping" | `material-culture-inference-method.md:33` (flint sickles with cereal-silica gloss, L2 function tier) |
| threshing | flail; threshing sledge with flint teeth; oxen treading | flail, threshing floor, treading, "the ox's share" | Deut 25:4 (ox not muzzled while treading — textual, to-verify) |
| winnowing | fork and basket, thrown into the wind | winnow, chaff, "the wind's help" | standard; to-verify any regional term before use |
| storage | granary, underground pit, rick, tithe barn, state horrea | granary, pit, rick, "the keeping" | `vessel-container-lexicon.md:34` — STORAGE job: bulk, pests, damp; large immobile forms "often buried to the shoulder" |
| the claim | tithe (a tenth), rent in kind, tax in grain, sharecropping | tithe, rent, share, gleaning right | `calendar-festival-systems.md:116` — harvest stored → tithes, debts, assembly |

- **The harvest is the year's only synchronization event**: it sets the labor peak, the debt calendar, the festival, and the tax simultaneously — the in-repo harvest row puts "harvest stored → tithes, debts, assembly" in one cell (`calendar-festival-systems.md:116`), and the festival-arc build step asks for "one harvest assembly" among the four civic festivals (`:167`).
- **Gleaning is a right, not charity** in several legal traditions (Lev 19:9–10; Ruth — textual, to-verify): a culture's gleaning rule is a legible statement about who may be poor without being criminal.
- **Storage words name the loss they prevent** (DR-AG-07): damp, pest, theft, fire, and the seed reserve that must not be eaten. A granary word that names no loss is a warehouse, not a granary.

## 8. Land tenure and the words it makes

- **Work-unit measures**: the field measured by what it takes to work it is the most widespread agrarian metrological pattern, and this lane already owns the general rule — measures come from "the body, the substance measured, the action, and the container", with "a day's plowing" named as an action-measure (`trade-economy-lexicon.md:17`). The agrarian instances (each equivalence **(to-verify)**): Roman *jugerum* (a yoke's day), German *morgen* ("morning" — a day's work), French *arpent*, English *acre* (< OE *æcer*, from the same field-root as Latin *ager* and Greek *agros*, hence *agriculture*).
- **Ploughland measures**: the land named by the team it supports — English *hide* (a household's land; not a fixed acreage — to-verify), *virgate* (a quarter hide), *carucate* (ploughland, Danelaw), *oxgang/bovate* (one ox's share in a team). These words are the **status system in disguise**: to hold a virgate is to owe a fraction of a plough team's work.
- **The claim layer** turns land into obligation: tithe, rent in kind, sharecropping (*métayage*; Roman *coloni* arrangements), corvée/statute labor (the Inca *mita* is the in-repo case, via `transport-mobility-lexicon.md`'s road entry), and debt against the standing crop. Each generates a status word pair — the one who owes and the one who receives.
- **Design rule:** give the culture **one measure from the body, one from the seed, one from the day's work** (`trade-economy-lexicon.md:17`), then let the tenure word be a compound of the work word. That is how a parcel word ends up meaning a social class.
- Field names are the densest toponym layer in a rural culture and the first thing land reform rewrites — couple `linguistics/naming-systems.md` (toponymy; critical toponymy on renaming as power).

## 9. The agrarian calendar and the ritual layer

- Build the year from the labor peaks outward: flood or monsoon arrival, ploughing window, sowing, the hungry gap (the pre-harvest months when the old store runs low), harvest, threshing, and the storage/assembly moment. Then place one rite at each seam: first-furrow, rain or flood petition, first-fruits, harvest-home, and a threshing-floor rite.
- In-repo couplings to use rather than reinvent: the festival-arc step asks for "one inversion festival, one season-of-the-dead, one harvest assembly, one founding-act civic cycle" (`calendar-festival-systems.md:167`); the harvest row already carries the assembly semantics (`:116`); the ritual grammar (separation / liminality / incorporation) for first-furrow and first-fruits belongs to `myth-symbol/ritual-liminality.md`; the sacred-plant side belongs to `myth-symbol/plant-symbolism.md`; weather and flood omens belong to `myth-symbol/divination-omen-systems.md`.
- The stink layer: manure, night-soil, retting, and rendering sit downstream of euphemism and taboo — the partition already flags this for retting (`textile-technology.md:76`); the agrarian version is that a culture's fertilizer words are the most euphemized words in its lexicon, and its soil words may be honorifics (a "fat" field, a "weeping" field).

## 10. Calibration shelf — contested, overrepeated, or discredited; flag before anything reaches the bible

| Claim | Status | Safe use |
|---|---|---|
| The heavy plough caused a medieval agricultural revolution | Contested (White 1962 thesis vs later economic and harness accounts — to-verify) | two rival in-world doctrines of why the north ploughed deeper |
| Plough agriculture pushed women out of field work, shaping gender norms | Statistical regularity; mechanism contested (`material-culture-inference-method.md:75,:105`) | a regularity an in-world reformer can preach, with the counter-evidence in the room |
| Large irrigation works cause despotism (hydraulic despotism) | Rejected as a law; usable as ideology (to-verify counter-cases) | a bureaucracy's self-description; a rebel's accusation |
| Rice farming makes cultures collectivist | Published and contested; correlational, mechanisms argued (`cuisine-food-lexicon.md:157`) | an in-world determinist sermon; never a world fact |
| Malthusian collapse is the default fate of farming | One model among several; Boserup's intensification-by-population-pressure is the rival (`material-culture-inference-method.md:13`, Boserup 1965) | two economic doctrines in conflict inside the fiction |
| "Traditional" farming was sustainable/static | Romantic; rotation, terracing, and irrigation are interventions with failure modes (see §3, §5) | a nostalgic in-world school of thought, and its critics |
| Three-field rotation is the medieval default | Regional and late; do not universalize (to-verify) | one region's system, contrasted with a two-field neighbor |
| Ancient yields of "X-fold" | Figures circulate wildly and are rarely comparable (seed:yield vs land:yield, different soils) | never quote a ratio unflagged — coin the culture's own ratio and mark it as designed |
| The plough was invented once and spread | Multiple independent and near-independent origins are the standard picture (to-verify) | rival origin myths inside the fiction |
| Peasants were self-sufficient | Markets, rent, and tax integrate them by definition (see §8; `trade-economy-lexicon.md`) | a self-sufficiency myth the characters tell about themselves |

## 11. Decision record

| ID | Decision | Trigger / condition | Evidence | Status |
|---|---|---|---|---|
| DR-AG-01 | Name the peak-labor month and the harvest claim before naming any implement or parcel word | any entry assigns the culture a crop | `calendar-festival-systems.md:116,:167` (harvest = storage + tithe + assembly); `cuisine-food-lexicon.md:26` (staple labor signatures) | adopted — the derivation order in §2 |
| DR-AG-02 | Every field term carries a tenure tag (who holds it, what they owe) | any parcel or field name is coined | `trade-economy-lexicon.md:17` (measures from the action); `civilizations/khmer-angkor.md:149` (*sre* carries land-transfer and supply obligations) | adopted |
| DR-AG-03 | Plough claims ship as capacity chains (soil, team, iron, fodder, repair), never as era labels | any plough or "agricultural revolution" claim | `transport-mobility-lexicon.md:29` (capacity, not virtue); `material-culture-inference-method.md:61` (cost gradients) | adopted |
| DR-AG-04 | The plough→gender hypothesis is generator material with two rival in-world doctrines | any gender-norm claim tied to farming | `material-culture-inference-method.md:75,:105` | adopted |
| DR-AG-05 | Water vocabulary splits into source / lift / deliver / right — four words, not one | any irrigation or water-right term is coined | `civilizations/khmer-angkor.md:146-149` (one water word does not fix the source or scale); `civilizations/nazca.md:37` (dated horizon) | adopted |
| DR-AG-06 | Date the crop referent's arrival separately from its word's arrival | any crop or implement loanword enters the lexicon | `textile-technology.md:83` (cotton loan chain); `transport-mobility-lexicon.md` DR-TR-03 (same rule for vehicles) | adopted |
| DR-AG-07 | Storage words name the loss they prevent (damp, pest, theft, fire, seed reserve) | any granary/pit/rick word is coined | `vessel-container-lexicon.md:34` (STORAGE job definition) | adopted |
| DR-AG-08 | No yield ratio, team size, or dated "revolution" ships unflagged | any figure reaches a draft or the bible | `cuisine-food-lexicon.md:157` (the FAO 42%→40% correction pattern); `material-culture-inference-method.md:105` | adopted |
| DR-AG-09 | Refuse hydraulic despotism as a law; keep it as an in-world ideology | any causal claim linking water works to state power | §5 calibration row (Wittfogel 1957, to-verify counter-cases) | adopted |
| DR-AG-10 | Hand off as design instrument; no canon assignment | any handoff to lore | lane rule (`AGENTS.md`; `SKILL.md` boundaries) | adopted — handoff names recipient and open questions |

## 12. Build order and handoff note (non-canon)

- **Build order for a fictional agrarian culture:**
  1. Fix the climate and the water source; name the flood/rain season and the dry season (§5 SOURCE).
  2. Choose the default field system from §3; name the one the culture left behind.
  3. Fix the peak-labor month; derive the cooperative-vs-household labor word split.
  4. Choose the implement from §4 and pay for its whole capacity chain; name the team and the yoke.
  5. Build the rotation clock (§6); give one staple a native word, one a loan, one a failure.
  6. Write the harvest kit: tool, act, share, storage, and the gleaning rule (§7).
  7. Set the tenure layer: one body measure, one seed measure, one work measure, and the claim that rides them (§8).
  8. Place the four rites at the four seams (§9); hand the omen layer to the divination file.
  9. Run the §10 shelf over every number in the draft; flag or coin, never import silently.
- **Recipient**: lore-shokunin, via `synthesis/worldbible-integration-contract.md`.
- **This entry supplies**: the four-institution frame, the ten-system field typology with lexical signatures, the plough capacity chain with the gender-hypothesis calibration, the water chain (source → lift → deliver → right) with three worked in-corpus systems, the rotation and crop-loan clocks, the harvest/storage/claim vocabulary, the work-unit land-measure pattern, and the decision record above.
- **Open questions this lane does not decide**: which system is the culture's default; who owns water; whether the plough is native or borrowed; what the harvest claim costs; whether any in-world doctrine claims a revolution the evidence only supports as contested. Those belong to the world, and to lore-shokunin.
- **Known limits**: every external work in this entry is an inherited citation (no network at authoring time), so all figures, dates, and equivalences marked **(to-verify)** must be fetched and re-read before canonization; the entry is a design instrument and a source map, not a verified history of agriculture.
```

---

## Self-audit (replicated checks, run at authoring time; no filed-round runner executed)

Method: the regexes of `reports/round-19/audit/entry-audit.py:25-31` and its couples resolver (`:74-96`) were replicated inline in `python3 -` and run against the fenced block above (extracted from this fragment); nothing under `reports/round-19/` was executed. Commands and results:

```
$ python3 - <<'PY'   # replicate HEADER_RE / GAP_RE / DECISION_RE / CALIB_RE / CANON_RE + couples resolution on the extracted block
header_fields: ['couples', 'gap', 'recheck', 'source', 'sources', 'topic', 'verified-at']
header_missing_required: []            (required = topic, sources, couples)
header_tail_ok: True                   (verified-at present; recheck present)
source_bullets: 2   source_bullets_with_locator: 2/2
gap_named: True                        (GAP_RE hit: "the gap this entry fills")
decision_record: True                  (DECISION_RE hit: "Decision record" + DR-AG-01..10)
calibration_flagged: True
canon_hygiene: True                    (lore-shokunin named)
couples_unresolved: []                 (all .md targets resolve on disk at 4a7aede)
quality_bar: True
PY
```

Counts observed in that run (recorded verbatim so C12/C13 can reproduce): header fields = 7 (`gap`, `topic`, `sources`, `couples`, `source`, `verified-at`, `recheck`); source bullets = 2, both carrying locators (bullet 1 carries backticked `path:line` repo locators — 25 expanded citations, all inside file bounds; bullet 2 carries named years and a `to-verify` flag on each unfetched work); couples targets resolved = 22, unresolved = 0 (resolver replicated with the entry's applied base dir `corpus/knowledge/culture-material/`, plus lane-root and `corpus/knowledge/` candidates, per `entry-audit.py:83-92`); gap phrase present; decision record present with 10 DR-AG rows; `(to-verify)` marks: 11 lines / 12 occurrences in the entry (measured with an inline `str.count` over the extracted block — a first draft of this line said 21, corrected here to the measured value); entry length, final revision: 180 lines / 37,793 bytes as staged by C12's instrument (12 `##` sections — inside K01's 7–14 section band; 3 lines above the culture-material line-band max of 177, noted rather than trimmed); the pre-revision figures for that same block were 187 lines / 36,617 chars, and the earlier inline counts in this paragraph were measured on that revision.

**Cross-instrument run — C12's audit instrument (post-landing revision of this fragment).** The instrument bytes were extracted from `reports/round-35/cov/C12-audit-runbook.md` §5 into `.scratch/c12/entry-audit-runbook.py` and proved against C12's published digest (`sha256sum` → `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`, 663 lines), then run read-only:

```
$ python3 -B .scratch/c12/entry-audit-runbook.py --selftest
SELFTEST PASS: 3 positive controls ... 4 negative controls ...   (exit 0)
$ python3 -B .scratch/c12/entry-audit-runbook.py --fragments .scratch/c12/drafts --stage .scratch/c12/stage
STAGED .scratch/c12/drafts/C02-entry-2.md -> .scratch/c12/stage/corpus/knowledge/culture-material/agrarian-field-system-lexicon.md (37793 bytes)
PASS/clean .../agrarian-field-system-lexicon.md 4of4=True 5f=True src=2/2 ptr=1/1 gap=True dec=True bleed=0/0
```

Readings from the JSON mode on the staged bytes (sha256 `e8ec74c89bd324a226186fbeca34cfecdfbe9a6ac5ec509d63c4d6b021497dba`, 37,793 bytes): `frontmatter_4of4: true` (legs `sources`, `verified-at`, `recheck`, `couples`-as-scope), `lane_profile_5f: true` (`topic, sources, verified-at, recheck, couples`), `gap_named: true`, `decision_record: true`, `canon_boundary_named: true`, `source_entries: 2` with `source_entries_with_locator: 2`, `pointers_unresolved: []`, `bleed_candidates: []`, `review_observations: []`, `contract_defects: []`, `pass: true`, `clean: true`.

Two revisions were required to reach that reading, both made **after** the first staging attempt and recorded here because they move the audited digest: (1) the entry's §1 census output was moved out of a nested three-backtick fence into a table, and (2) the outer fence was changed from four backticks to three, because C12's stager matches `^```(?:markdown|md)\s*$ … ^```\s*$` (`.scratch/c12/entry-audit-runbook.py:578`) and a nested fence or a four-backtick outer fence reads `CANNOT-EVALUATE: … no corpus target path or no fenced block`. (3) One bleed false positive was reworded — the swidden row's "cleared by fire" → "felled and burned" — after the instrument's strict-tier list flagged `cleared` (`.scratch/c12/entry-audit-runbook.py:105`); the agronomic sense is what the lane's no-bleed rule does not target.

**Independent audit already on record (C17).** `reports/round-35/cov/C17-audit-sample.md` §7.1 audits this draft at a pinned digest (`bff366523d7c9efb86cd2a4defb89d457f95f77007a89641b291de7181615797`) and records **"Defects against entry 2: none"** — legs L1–L9 pass, with agreement on the `(to-verify)` reading (11 lines / 12 occurrences), on the couples count (22 — C17's first reading of 20 was its regex's narrower token class), and on the §1 census (19/19 numbers re-derived identically). The digest moved after that audit (this fragment's later revisions), so this line is a pointer, not an inheritance: C17 or C13/C14 must re-run on the current bytes. C17's integrator note (i) — the README row for this entry must be the entry's full `- topic:` line — is recorded under `## Owed`.

In-repo anchor re-verification (each `path:line` in the sources block, re-read live in this pass):

```
$ python3 - <<'PY'   # assert needle-in-line for every cited path:line
OK material-culture-inference-method.md:13  (Boserup 1965; Alesina et al. 2013)
OK material-culture-inference-method.md:33  (flint sickles with cereal-silica gloss)
OK material-culture-inference-method.md:61  (constraints set cost gradients)
OK material-culture-inference-method.md:66  (energy & fuel row)
OK material-culture-inference-method.md:73  (seasonality row)
OK material-culture-inference-method.md:75  (plough→gender chain)
OK material-culture-inference-method.md:76  (deterministic-trap guard)   [cited in §2; see note]
OK material-culture-inference-method.md:105 (Vu 2025; Giuliano & Nunn 2021)
OK cuisine-food-lexicon.md:17   (FAO 2026 FAOSTAT ~40%)
OK cuisine-food-lexicon.md:26   (wet-rice water control; wheat; maize)
OK cuisine-food-lexicon.md:27   (Nunn & Qian 2011 potato)
OK cuisine-food-lexicon.md:157  (rice-theory calibration row)
OK calendar-festival-systems.md:52  (Akhet/Peret/Shemu)
OK calendar-festival-systems.md:116 (harvest → tithes, debts, assembly)
OK calendar-festival-systems.md:167 (harvest assembly in the festival arc)
OK textile-technology.md:11 (fiber gate "what the land raises")
OK textile-technology.md:21 (flax retting chain)
OK textile-technology.md:76 (stink trades / euphemism seam)
OK textile-technology.md:83 (cotton loan chain)
OK trade-economy-lexicon.md:17 (measures: body, substance, action, container)
OK transport-mobility-lexicon.md:29 (capacity, not virtue)
OK vessel-container-lexicon.md:34 (STORAGE job row)
OK austronesia-philippines-taiwan.md:109-126 (Ifugao land-use tiers)
OK khmer-angkor.md:146-149 (water/ricefield vocabulary)
OK nazca.md:37 (puquio horizon)
OK nazca.md:105 (underground-water overreading control)
PY
```

Note on `material-culture-inference-method.md:76`: the cited sentence ("a chain with zero choices is a deterministic trap, not a culture") is at `:76` in the live file; the block above lists it separately because the fragment's `- sources:` block cites the range `:61,:66,:73,:75,:105` and this line was added during drafting. If the integrator prefers a single contiguous citation list, add `:76` to the sources bullet.

## Findings (contract-level; for C12/C13/R03)

1. **`transport-mobility-lexicon.md` does not name its gap in any phrase the round-19 audit recognizes.** Replicating `reports/round-19/audit/entry-audit.py:26` (`GAP_RE`) over the filed entry: `gap_named: False`. Its `- gap:` field reads "… — this entry fills it", and the phrase set is `(residual gap|gap filled|the gap this entry fills|known gaps|missing from|no entry (covers|states)|not covered by)`. The sibling `plant-symbolism.md` passes because its topic line contains "the gap this entry fills". **Consequence for round 35:** if the claim-C audit applies `GAP_RE`, this draft passes (`gap_named: True`) but the round-34 entry would fail the same check — an auditor using that instrument should either accept the `- gap:` field's presence as the contract or file the r34 entry as a stale-check victim. Owner: C12 (runbook) / C13–C14 (auditors).
2. **No `- scope:` frontmatter field exists anywhere in the corpus.** `grep -rl "^- scope:" corpus/knowledge/` → 0 files (201 entries at baseline). `reports/round-35/claims.json:29` requires "frontmatter-complete (source / verified-at / recheck / scope)" for the ten new entries; the filed corpus uses `gap / topic / sources / couples / source / verified-at / recheck` and no `scope`. This draft follows the **filed** field set (7 fields) rather than the claim's four-name shorthand, and records the discrepancy here rather than inventing a field the partition does not use. If the operator wants a literal `- scope:` line, it can be added to all ten drafts in one pass — owner: integrator (P01/C12 decision).
3. **`- source:` (singular) is a live field** in the two newest entries (`plant-symbolism.md:7`) but is absent from `transport-mobility-lexicon.md`; the round-19 audit's `tail_ok` accepts `verified-at` + either `recheck` or `source`, so both shapes pass. This draft carries all three (`sources`, `source`, `verified-at`, `recheck`) — the superset that satisfies either reading.
4. **Staging fence shape breaks the auditors' own instrument for most drafts.** C12's instrument stages fragments with `re.findall(r"^```(?:markdown|md)\s*$([\s\S]*?)^```\s*$", …)` and takes `blocks[0]` (`.scratch/c12/entry-audit-runbook.py:578`). A four-backtick outer fence (```` ```markdown ````) is not matched at all, and a three-backtick block nested inside the entry truncates the staged bytes at the inner closing fence. At the first run of this pass, `--fragments .scratch/c12/drafts --stage …` printed `CANNOT-EVALUATE … no corpus target path or no fenced block` for C01, C02, C03 and C05 (C06 and C07 staged). This fragment was converted to the three-backtick form with no nested fence inside the entry and now stages cleanly (result above). R09's cross-review had already flagged the same hazard from the counting side (`reports/round-35/review/R09-cross-review.md` §2.6 note 1: five of six drafts four-backtick at that cut). Owner: each author (C01/C03/C05 still read CANNOT-EVALUATE against the current instrument) or the integrator, who must stage by hand if the auditors do not.
5. **Marker-count metric reconciliation, so no auditor mis-reads this fragment's numbers.** This fragment reports the literal `(to-verify)` token: 11 lines / 12 occurrences in the entry. R09's table counts the inventory tool's parenthesized-marker class (`\(to-verify[^)]*\)`, i.e. bare + detailed, `tools/source-audit-inventory.py:79-80`) and reads this draft as 20 (12 bare + 8 detailed), with 38 raw `to-verify` occurrences. Both are correct for their definitions; the difference is the `(to-verify: …)` / `(to-verify — …)` detail forms, which this entry uses deliberately. A verifier should state which metric it is quoting.

## Owed

- `reports/round-35/plan/P01-c-plan.md` — **still absent** at final verification (`ls reports/round-35/plan` → `P02-oa-plan.md` only). This seat selected the agrarian/field-system register from its own census because P01 had not landed; the mission text ("Author entry 2 (culture-material) with the same contract") fixes the partition and the entry slot, not the topic. If P01 lands with a different assignment for slot 2, this draft is re-numbered or superseded by the integrator.
- **Topic de-collision, re-checked after the sibling fragments landed** (not owed, but recorded here because the first version of this section could not rule it out): C01 = mortuary material culture, C03 = writing media and the surface economy, C05 = furniture and the interior, C06 = fire/fuel/light, C07 = eschatology/world-end, C08 = sacred kingship. None claims the agrarian register; C06 is K01's CM-5 (lighting/fuel/utilities) and C01 is CM-6, adjacent but distinct rows. **Residual risk: C04 has not landed** — if C04 claims CM-1 agriculture/subsistence or CM-2 pastoralism/husbandry, K01 §2.5's collision rule applies (the later author appends `-b` to the slug and says so in the entry's gap line). No central slug registry exists under `reports/round-35/` as of this pass (`grep -rln "registry" reports/round-35/` finds discussion, not a registry file), so this fragment's slug claim — `agrarian-field-system-lexicon` → CM-1 → culture-material → seat C02 — stands as the registry row the integrator can lift.
- **README row, for C11/integrator** (C17 §7.1 note (i), confirmed here): the index row for this entry must be emitted from the entry's own `- topic:` text, continuation-joined, byte-equal — the `- topic:` line is a single 1127-char line, so the generator can emit it directly; never paraphrase.
- **External-source fetch pass (network)**: every work in the inherited bibliography carrying `(to-verify)` needs a fetch/read before this entry could be admitted with its figures unflagged — owner: integrator or a verifier seat with network (this seat had none, per its dispatch).
- `reports/round-35/scout/K01-coverage-census.md` — **landed during this pass**; it independently ranks this register as candidate gap **CM-1** (mentions 21, topic-owners 0) and its §2.5 allocates the agriculture/subsistence slot first for claim C. The corroboration is folded into the entry's §1 (second-reader bullet) and the fragment's dependency note; the remaining P01 item above is unchanged.

## Citations

- `reports/round-35/claims.json:20-36` — claim C definition (partition counts, thresholds, counting commands).
- `reports/round-35/targets.json` — seat C02 object (`mission`, `out`), `shared_rules`.
- `REGIMEN.md:25-50` — per-round contract; `:60-69` scope.
- `corpus/QUALITY.md:1-23` — admission bar (provenance, calibration, coupling, usability, canon hygiene).
- `reports/round-19/audit/entry-audit.py:25-31,:45-96,:99-134` — replicated checks (`HEADER_RE`, `GAP_RE`, `DECISION_RE`, `CALIB_RE`, `CANON_RE`, `source_locators`, `couples_targets`); read only, not executed.
- `corpus/knowledge/culture-material/material-culture-inference-method.md:13,:33,:61,:66,:73,:75,:76,:105`
- `corpus/knowledge/culture-material/cuisine-food-lexicon.md:17,:26,:27,:157`
- `corpus/knowledge/culture-material/calendar-festival-systems.md:52,:116,:167`
- `corpus/knowledge/culture-material/textile-technology.md:11,:21,:76,:83`
- `corpus/knowledge/culture-material/trade-economy-lexicon.md:17`
- `corpus/knowledge/culture-material/transport-mobility-lexicon.md:1-6,:20-22,:29,:88-98` (frontmatter shape, gap-field wording, capacity rule, decision-record shape)
- `corpus/knowledge/culture-material/vessel-container-lexicon.md:34`
- `corpus/knowledge/culture-material/plant-symbolism.md` — sibling myth-symbol entry used for the `- source:` field shape (path under `corpus/knowledge/myth-symbol/plant-symbolism.md:1-9`).
- `corpus/knowledge/civilizations/austronesia-philippines-taiwan.md:109-126`; `corpus/knowledge/civilizations/khmer-angkor.md:146-149`; `corpus/knowledge/civilizations/nazca.md:37,:105`
- `reports/round-35/scout/K01-coverage-census.md` §2.3 (candidate gap CM-1: mentions 21, topic-owners 0, first hits `civilizations/amazigh-berber.md:146`, `civilizations/bali.md:14`, `civilizations/carthage.md:63`), §2.5 (slot allocation and the `-b` collision rule), §1.3 (field-set and line/section bands: culture-material 103–177 lines, 7–14 `##` sections), §3 (entry shape contract from three exemplars).
- `reports/round-35/cov/C12-audit-runbook.md` §5 (instrument bytes; digest `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`) — extracted to `.scratch/c12/entry-audit-runbook.py` and run read-only (selftest PASS; stage + JSON audit of this draft → `pass: true`, `clean: true`).
- `reports/round-35/cov/C17-audit-sample.md` §7.1 — independent audit of this draft at pinned digest `bff366523d7c9efb86cd2a4defb89d457f95f77007a89641b291de7181615797`: "Defects against entry 2: none", legs L1–L9 pass; §7.3 two-reader agreement ledger.
- `reports/round-35/review/R09-cross-review.md` §2.6 — fence-shape hazard note and the marker-count table this fragment reconciles in Finding 5.
- Commands run (outputs quoted in §1, §Self-audit, §Findings): the partition census `for t in ...; do grep -ril ...; done`; the per-line anchor assertion loop; `grep -rl "^- scope:" corpus/knowledge/ | wc -l` → 0; `ls reports/round-35/cov reports/round-35/scout reports/round-35/plan` → three "No such file or directory" at first run, then `P02-oa-plan.md` only in `plan/` at final verification; `sha256sum .scratch/c12/entry-audit-runbook.py`; `python3 -B .scratch/c12/entry-audit-runbook.py --selftest` → SELFTEST PASS (exit 0); `python3 -B .scratch/c12/entry-audit-runbook.py --fragments .scratch/c12/drafts --stage .scratch/c12/stage` → `PASS/clean … agrarian-field-system-lexicon.md 4of4=True 5f=True src=2/2 ptr=1/1 gap=True dec=True bleed=0/0`.
