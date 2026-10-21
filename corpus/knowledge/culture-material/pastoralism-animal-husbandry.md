# Pastoralism and animal husbandry — herding as an argument about grass, water, animals and movement: the herd as living capital, mobility as the production logic, tenure, exchange and the herd's ritual ledger

- topic: herding and animal husbandry as a production register for fictional cultures — the standing herd as living capital; species portfolios and ecology; mobility systems (nomadic, transhumant, agro-pastoral, enclosed); the herd lexicon and ownership marks; primary and secondary products; herd wealth, loans, bridewealth and raiding; pasture tenure and commons; pastoral–sedentary interdependence; the ritual ledger of the flock; and the calibration traps (stage ladders, the "pure nomad", the cattle complex, the universal tragedy of the commons)
- gap filled: no file in the corpus owns the pastoral **production system** as a cross-cultural method. Filename sweep `find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l` → **0**; word-bounded topic sweep `grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l` → **0** (both run 2026-10-21 at `4ad2683`; the un-bounded form also hits "sherd" at `writing-media-surface-economy.md:3`, a non-owner). Partial owners keep their pieces and are cited one-way in §2: the agropastoral row (`agrarian-field-system-lexicon.md:62`), the pastoral vocabulary field (`semantic-fields-lexicon-building.md:70,:105`), cattle-root money words (`trade-economy-lexicon.md:69`), dung fuel (`fire-fuel-light.md:37`), wool (`textile-technology.md:27`), draught and pack animals (`transport-mobility-lexicon.md:95`), livestock-as-wealth idiom (`animal-symbolism.md:73,:110`). Round 44's gap scout carried pastoralism as a rejected candidate (`reports/round-44/scout/K02-gap-scout.md:73`); round 50 is its first deliberate revival. No sibling lane owns the register (round-50 connector sweep of all `*-shokunin` topic lines: 0).
- sources:
  - In-corpus anchors (repo-relative `path:line`, each re-read at `4ad2683` on 2026-10-21): `culture-material/hunting-foraging-subsistence.md:27,:36,:116,:117,:137-146,:170-172,:195`; `culture-material/agrarian-field-system-lexicon.md:56,:62,:80`; `culture-material/trade-economy-lexicon.md:69`; `culture-material/fire-fuel-light.md:37`; `culture-material/textile-technology.md:27`; `culture-material/transport-mobility-lexicon.md:95`; `culture-material/cuisine-food-lexicon.md:67,:86`; `linguistics/semantic-fields-lexicon-building.md:70,:105`; `myth-symbol/animal-symbolism.md:73,:110`; `myth-symbol/symbolism-synthesis-method.md:69`; `myth-symbol/sacred-kingship-mythic-charter.md:65`; `myth-symbol/ritual-liminality.md:63`; `myth-symbol/celestial-symbolism-calendars.md:28`; `civilizations/mongol.md:40`; `civilizations/turkic-steppe.md:148,:193,:194`; `civilizations/scythian-saka.md:70`; `civilizations/finnic-sami.md:140,:150`; `civilizations/dine-navajo.md:125`; `civilizations/inca.md:128`; `verification/calibration-registry.md:35-39,:142`.
  - External shelf — **opened this round (2026-10-21)**, registered in `corpus/SOURCES.md` rows **S048–S069**, each row carrying its URL, access date, tier scope and anchor: S048 FAO 2001 *Pastoralism in the new millennium* (typology); S049 same, social institutions and tenure; S050 Zeder 2008 *PNAS* (herd management before morphology); S051 Marciniak 2011 (secondary-products critique); S052 Evans-Pritchard 1940 *The Nuer*; S053 Eczet 2020 (the "cattle complex" label and its critique); S054 Hardin 1968; S055 Ostrom 2009 Nobel lecture; S056 Khazanov 2019 (non-autarky); S057 Salzman 2004 (publisher description); S058 Schareika 2003 (WoDaaBe movement); S059 Sametinget *Renmärken* (earmarks); S060 Ahearn 2018 (Mongolian "five snouts"); S061 Wiener et al. 2003 *The Yak* ch. 8; S062 UNESCO Mongol ger element; S063 UNESCO Bedu cultural space; S064 ETCSL *Debate between Sheep and Grain*; S065 AHD *peku-*; S066 D-PLACE EA004; S067 Librado et al. 2021 (domestic horse origins); S068 Yacobaccio 2021 (South American camelid domestication); S069 UNESCO ICH decision 14.COM 10.b.2 (transhumance element).
- couples: culture-material — `agrarian-field-system-lexicon.md` (owns the field and the agropastoral parcel/manure contract, `:62`; this entry owns the herd's movement logic and composition); culture-material — `hunting-foraging-subsistence.md` (owns wild acquisition; its wild-source test `:36` excludes herded stock, which lands here); culture-material — `cuisine-food-lexicon.md` (owns the dish and milk+meat law, `:67,:86`); culture-material — `textile-technology.md` (owns fibre-to-cloth, `:27`); culture-material — `transport-mobility-lexicon.md` (owns route, load and draught capacity, `:95`); culture-material — `trade-economy-lexicon.md` (owns money words, `:69`); culture-material — `fire-fuel-light.md` (owns dung as fuel, `:37`); linguistics — `semantic-fields-lexicon-building.md` (owns the pastoral vocabulary field, `:70,:105`); myth-symbol — `animal-symbolism.md`, `sacred-kingship-mythic-charter.md`, `ritual-liminality.md` (own the herd's signs, the shepherd-king office and sacrifice typology); civilizations — `mongol.md`, `turkic-steppe.md`, `scythian-saka.md`, `finnic-sami.md`, `dine-navajo.md`, `inca.md` (regional cases, cited never restated); lore-shokunin (canon: which herds, routes, marks and raids exist in-world).
- source: lane-side authority is the in-corpus anchor list above plus the external rows opened this round: **S048–S069** in `corpus/SOURCES.md`, each with URL, access date 2026-10-21, tier scope and the round lesson's located quote.
- verified-at: 2026-10-21 — written against base `4ad26836552462d28a946ca3b067cab0b5ce3532` (`git rev-parse main`); pre-entry `find corpus/knowledge -name '*.md' | wc -l` → **225**, `ls corpus/knowledge/culture-material/*.md | wc -l` → **27**; post-entry **226** and **28**; `python3 -B reports/round-28/readme/sweep.py` → rows 226 files 226, topic_mismatch 0, exit 0.
- recheck: before any in-world herd becomes load-bearing — re-run the gap sweeps above; re-open S050/S067 before quoting a domestication date (aDNA moves fast); re-open S054 and S055 together before writing a commons rule; open the Herskovits 1926 text before quoting him (only S053's attribution is opened); re-read `finnic-sami.md:140,:150` before writing any reindeer-herding people.
- scope: reference method and lane policy for the culture-material partition. This entry owns herding as a **production system** — species portfolio, mobility, herd management, products, herd wealth and transfer, pasture tenure, pastoral–sedentary exchange — at comparative-method level; it hands the field, the hunt, the dish, the cloth, the road, the market, the lexicon field, the animal sign and every canon decision to their owners (§2, §15).

## 1. The register property: pastoralism is an argument about grass, water, animals and movement

**Master claim.** A pastoral culture is not "herders who lack fields". It reads rangeland as a moving schedule and holds the herd as living capital: a stock that breeds, is culled, lent, given and walked. Where the hunting register argues about the patch (`hunting-foraging-subsistence.md:27`) and the agrarian register about the field, this one argues about forage, water and the animal that turns both into milk, wealth and movement. FAO's synthesis defines the register by its conditions — where hunting-gathering is easy, "there is little or no impetus to herd animals" (S048) — and herd management is legible archaeologically before any change in the animals' bodies (S050).

| Test | Pass when | Fails as (owner) |
|---|---|---|
| **Herded capital** | stock is bred, held and culled as a standing store; culling keeps females, harvests young males (S050) | a hunt: wild source, "not planted, herded or owned" (`hunting-foraging-subsistence.md:36`) |
| **Mobility tracks forage** | movement is the production logic, timed to vegetation and season (S058) | a fixed mixed farm: `agrarian-field-system-lexicon.md:62` owns the agropastoral row |
| **Labour-capped herd** | household labour, not pasture alone, sets the herd a family can hold (S049) | enclosed ranching with wage herders (§3 last row) |
| **Distribution by rule** | animals move as gift, loan, bridewealth and raid (§7) | market sale only: `trade-economy-lexicon.md` |

Dependence varies: the Ethnographic Atlas codes only a small minority of its societies as near-totally dependent on animal husbandry (S066) — design a **dial**, not a type.

## 2. One-owner boundary

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `agrarian-field-system-lexicon.md:56,:62` | parcel, plough, stubble grazing, manure contract | herd calendar, transhumance movement logic, herd composition |
| `hunting-foraging-subsistence.md:36,:116` | wild acquisition; meat-for-crops at a farming edge | the herded counterpart only |
| `cuisine-food-lexicon.md:67,:86` | yogurt lineages, milk+meat law, Harris's cattle economy (contested) | milking, churning and the dairy chain up to the product |
| `transport-mobility-lexicon.md:95` | draught capacity chain, route class, load figures | husbandry of riding and pack animals (feed, training, herd share) |
| `trade-economy-lexicon.md:69` | cattle-root money words | herd-as-wealth composition and transfer rules |
| `textile-technology.md:27` | fibre-to-cloth chain | flock management, shearing season, fleece selection |
| `semantic-fields-lexicon-building.md:70,:105` | the pastoral vocabulary field and the steppe field-bundle | the herd facts the field lexicalizes (§5 supplies inputs) |
| `fire-fuel-light.md:37` | dung as fuel versus manure | the herd as dung source |
| `civilizations/` regional entries | Mongol, Turkic, Scythian, Sámi, Diné, Inca cases and their warnings | general method only; regional herds are cited, never restated |

## 3. Pastoral systems typology: mobility as the design dial

"Any classification of this type must be treated as a simplification" (S048): read the rows as dials inside one economy, never a ladder (`mongol.md:40`).

| System | Mobility | Settlement | Labour | Risk strategy |
|---|---|---|---|---|
| Nomadic | household and herd move on a forage cycle | portable dwelling — the ger is "light enough for nomads to carry" (S062) | household herding; splitting by species and age | species mix and movement are the hedge (S060) |
| Semi-nomadic | part of household travels; a base is held | village or winter camp plus satellite camps | base keeps the old, young and crop plot `(to-verify)` | the base is store and drought fallback |
| Transhumant | seasonal movement of people with their livestock; horizontal in plains or plateaus, vertical in mountains (S069) | two bases; the route is infrastructure | a herd party travels, households stay; herd splitting (S048) | route access is the exposure |
| Agro-pastoral | short moves on stubble and fallow, return to village | fixed village with fields | herd calendar collides with the ploughing peak (`agrarian-field-system-lexicon.md:62`) | crop and herd buffer each other |
| Enclosed / ranching | fenced, individually owned land (S048); stored feed replaces movement `(to-verify)` | ranch headquarters | hired stockmen | market and tenure exposure |

Political organisation is a **second axis**, not a mobility row: segmentary tribes, tribal chiefdoms and peasant pastoralists (S057). Do not merge the two axes.

## 4. Species and ecology decision table

| Species | Ecology | Products | Mobility and labour | Calibration |
|---|---|---|---|---|
| Cattle | grass and reliable water; managed in the upper Euphrates c. 11,000–10,000 BP (S050) | milk, meat, hide, blood, traction | follows water and grass; age-grade herd labour | social idiom in Nilotic ethnography (S052) is regional, not a law |
| Sheep / goat | arid-tolerant small stock; goats first in the Zagros, sheep in SE Anatolia (S050) | meat, milk, wool, hair, dung | short to long moves; fast herd rebuilding | species order is regional (S050) |
| Camel | hot and cold deserts | milk, meat, hair, carrying | caravan and long-range moves; "camel husbandry" as a named skill (S063) | dates of domestication `(to-verify)` |
| Horse | steppe grassland; winter grazing through snow `(to-verify)` | milk (summer), riding, traction | riding multiplies herd range | modern domestic horses do not descend from the Botai lineage (S067): **C** on Botai-as-origin |
| Yak | high plateau; summer herds "on pastures at high elevations" (S061) | milk, butter, dung fuel, fibre, pack | vertical seasonal camps | cultural claims bounded to the FAO synthesis (S061) |
| Reindeer | taiga and tundra lichen pasture | meat, hide, transport | migration with the herd; earmark institutions (S059) | herding status ≠ Sámi identity (`finnic-sami.md:140,:150`) |
| Llama / alpaca | Andean puna; the only domesticated ungulates and pre-Hispanic pastoral societies of the Americas (S068) | fibre, pack, meat | puna pasture plus valley exchange `(to-verify)` | "all wool, all alpaca" is too simple (`inca.md:128`) |

Fix ecology → species → mobility → products → labour → symbol; a herd with no forage line fails §11 step 1. The Mongolian "five snouts" — horses, yaks/cattle, camel, goats and sheep — is an emic portfolio term (S060): a culture may name its herd as one set.

## 5. Herd lexicon and ownership marks

A herd vocabulary is a property index: each term answers what an owner must count, value, lend, recover or read at a distance (`semantic-fields-lexicon-building.md:70`).

| Dimension | Attested pattern | Conlang design rule |
|---|---|---|
| Colour × distribution | Nuer cow names follow "its colours and the way in which they are distributed on its body" (S052, ch. I §VIII) | base colour roots + a placement affix set, not a flat list |
| Age × sex | Nuer separate bull, cow, ox, heifer and calf terms (S052) | an age × sex grid of prefixes |
| Ownership mark | a Sámi earmark is a combination of cuts in both ears and names the owner (S059) | mark = lineage + cut + side; a mark change is a dated event |
| Species set | "five snouts" as one collective term (S060) | one collective noun; species stay separate roots |
| Livestock → wealth | PIE *peku- glossed "wealth, movable property" (S065); Latin *pecūnia* (`trade-economy-lexicon.md:69`) | model as a documented change path; never print the root as settled social history |

Counts of herd terms in ethnographies are estimates, not lexicon sizes: write "a very large set", never a number.

## 6. Products: meat, milk, fibre, traction, dung

| Product | Taken from | Design rule |
|---|---|---|
| Meat, hide, bone, blood | the dead animal (one harvest) | the culling rule decides the herd's shape (S050) |
| Milk and dairy | living females, repeatable | dairy needs pails, a curd/butter chain and storage; yak butter is the main milk product in most places (S061) |
| Wool and hair | living animals, shorn or plucked | flock management lives here; cloth stays in `textile-technology.md:27` |
| Traction and carrying | castrated adults | cite `transport-mobility-lexicon.md:95` for loads |
| Dung | any herd | one dung per season: fuel or field (`fire-fuel-light.md:37`) |

Sherratt's "secondary products revolution" — "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction" (S051) — is **C**: the review finds adoption regional and staged, not one horizon (S051). Write product sequences per region.

## 7. Herd as wealth and exchange

A herd works as marriage currency, loanable capital and risk buffer at once; design each transfer by what moves, who gains rights and what it insures.

| Transfer | What moves / who gains | Design rule |
|---|---|---|
| Bridewealth | stock from groom's kin to bride's kin; rights in wives and children | descent and herd size set the scale `(to-verify)` per culture; do not import a Nilotic figure |
| Stock loan / partnership | an animal lent; the borrower keeps some offspring | a loan network is insurance and alliance at once `(to-verify)`: herd wealth tracks household labour (S049) |
| Herd splitting | animals spread across kin and pastures | risk spread against local disaster; transhumance splits the herd (S048) |
| Raid | stock taken to rebuild after loss | raids target the form of wealth: animals and people, not grain (§9) |

Evans-Pritchard wrote that "Nuer tend to define all social processes and relationships in terms of cattle" (S052): a 1940 outsider's functionalist claim, **B** to that people and period.

## 8. Tenure, commons and mobility rights

A herd move claims three things: a route, a water point and a pasture. Each is a rule with an owner, not a landscape feature. Tenure "is thus divided by both ecology and the potential for agriculture" (S049).

| Model | Proposition | Status | Design use |
|---|---|---|---|
| Hardin 1968 | "Picture a pasture open to all" (S054) — an unregulated parable | **R** as a law of pastoral life; **B** for genuinely open access | a designed collapse only where no rule exists |
| Ostrom 2009 | design principles for long-surviving institutions "developed by the users of a resource" (S055) | mainstream as diagnosis; C as a predictive law | rotas, fines, monitors and nested authority as in-world institutions |
| Earmark institutions | a Sámi earmark is personal, usually inherited and registered for use in one herding community; unmarked reindeer are that community's collective property (S059) | B — one legal system | write who may herd where, and how a mark is inherited |

State settlement, privatisation and route closure are local history, never a fixed endpoint of mobility (`finnic-sami.md:150`; `dine-navajo.md:125`).

## 9. Pastoral–sedentary relations

A herding economy is non-autarkic by construction: steppe nomads "always experienced a need for external agricultural and handicraft products" (S056). Every relation is a designed exchange with a power term attached.

| Relation | What moves, who holds the lever | Design check |
|---|---|---|
| Interdependence | livestock, wool, hides out; grain, metal, crafts in | who carries the goods and sets the price? |
| Trade under pressure | the sedentary state licenses markets; nomads force them open (S056) | the licence and its price are the plot |
| Tribute and tolls | dependent cultivators pay; caravans buy passage | tribute is an income line, not a one-off |
| Conquest state | a mobile empire taxes transit and fields | name the external rival it forms against `(to-verify)` |

Bias flags: Chinese dynastic histories are indispensable and not neutral (`turkic-steppe.md:193`); reject any ladder from "raider" to "state" (`turkic-steppe.md:194`); "barbarian" is a calibration defect. Pastoral is not isolation (`turkic-steppe.md:148`), and pastoralism is not absence of farming (`scythian-saka.md:70`).

## 10. Ritual, myth and symbol of the herd

One flock is ledger, offering and metaphor at once: write the rite from the herd's books outward (`ritual-liminality.md:63`).

| Register | Mechanism | Anchor |
|---|---|---|
| Herd accounting as poetry | the farmer taunts the herder: "Every night your count is made and your tally-stick put into the ground" (S064) | the count is a literary fact before it is a ritual one |
| Rival economies | the Sumerian disputation sets Sheep against Grain as rival sisters (S064) | a theological ranking, not evidence of practice |
| Shepherd-king | the ruler as shepherd, audited by the gods (`sacred-kingship-mythic-charter.md:65`) | self-presentation, not administration |
| Sacrifice economy | offerings drawn from the herd's surplus males | an animal taboo implies a rite (`symbolism-synthesis-method.md:69`) |
| Sky figures | pastoralists read milk and river figures (`celestial-symbolism-calendars.md:28`) | a subsistence input to sky lore, not a creed |

The herd's signs belong to `animal-symbolism.md:73,:110`; this entry supplies the ledger they rest on.

## 11. Decision table and build order

| # | Build step | Decide before moving on | Check |
|---|---|---|---|
| 1 | Ecology | rainfall, forage patchiness, water points | dung, fuel and water tied in (`fire-fuel-light.md:37`) |
| 2 | Species | two to four species and their shares (S048) | each species row has forage and labour (§4) |
| 3 | Mobility | nomadic / semi-nomadic / transhumant / agro-pastoral / enclosed; splitting rule | §3; S058 for a named-move system |
| 4 | Tenure | who grazes, waters and crosses where; fixed or fluid claims | §8; never default to Hardin's open pasture |
| 5 | Wealth | herd ceiling set by labour and disease; loan and gift networks | §7; S049 |
| 6 | Lexicon | age, sex, colour, condition, mark terms from rows 2–5 | §5; `semantic-fields-lexicon-building.md:105` |
| 7 | Relations | the sedentary neighbour, its power and the exchange form | §9; S056 |
| 8 | Ritual | each taboo written with its rite | §10; `symbolism-synthesis-method.md:69` |

| Error pattern | Why it fails | Code |
|---|---|---|
| Pastoralism as the stage between foraging and farming | FAO reports the evolutionary-stage reading refuted (S048); `calibration-registry.md:142` | R |
| The frozen "traditional" herder | herd sizes and routes change with veterinary care, markets and states `(to-verify)`; pastoral is not isolation (`turkic-steppe.md:148`) | R as a static type |
| "Last nomads" doom framing | mobile pastoralism coexists with other production (`mongol.md:40`) | R as forecast |
| Herding status read as ethnic identity | `finnic-sami.md:140` | R |

## 12. NON-CANON worked micro-example

**NON-CANON.** The people, valley, flocks and numbers below are invented to demonstrate the method; canon belongs to lore-shokunin.

The **Ketrun** keep sheep, goats and a few yaks on a vertical round: valley pens in winter, a western pass in spring, high meadows in summer, back over the pass in autumn. Applying §11: ecology — a dry valley and wet high meadows; species — sheep and goats for wool and cheese, yaks only above the tree line; mobility — transhumant with herd splitting (the yaks summer apart); tenure — pass rights held by lineages, meadow turns by lot, a fine for grazing out of turn (Ostrom-style, S055); wealth — lambs lent between lineages after a hard winter; lexicon — sheep named by fleece colour and its placement; relations — cheese and wool traded down-valley for grain at a market the farmers license; ritual — the first lamb of the pass is counted aloud before the herd moves. The Ketrun are a different economy from the valley farmers, not an earlier stage of them.

## 13. Calibration bank

Codes per `calibration-registry.md:35-39` (R rejected, C contested, B bounded, H heuristic, T to-verify).

| Claim | Status | What to say instead |
|---|---|---|
| Nomadism is a rung on a ladder (hunting → herding → farming → state) | R — S048 reports the evolutionary-stage reading refuted; `calibration-registry.md:142` | mobility is one strategy inside a herd economy; sedentarization is a response, not a later rung |
| The "pure nomad" lives on the herd alone | R as description — S056: nomads always needed external grain and crafts | write the dependence dial per culture |
| Herskovits' "cattle complex": herders hoard cattle for prestige | C — S053 attributes the label to Herskovits 1926 and criticises its analyst vocabulary; the 1926 text is unopened `(to-verify)` | herd size answers labour, risk and tenure; prestige is an input, not a pathology |
| Hardin's tragedy describes pastoral commons | R as universal; B for unmanaged open access — S054 vs S055 | choose the rule set first: open access, group, state or private |
| Sherratt's secondary products arrived as one revolution | C — S051 | regional, staged product sequences |
| Herd management begins when bones get smaller | R — S050: management precedes morphological change | date herding by culling profile, not body size |
| Botai horses are the ancestors of domestic horses | C → R for modern horses — S067 | treat early horse use and modern horse origins as different questions |
| "Nuer define everything through cattle" generalises to herders | B — S052, one 1940 ethnography | quote place and date; never a pastoral universal |
| The publisher's summary of a book is the book's argument | B — S057 is a description only (QUALITY criterion 6) | cite programme and scope, not conclusions |

**Living-practice flag.** Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice (S058, S059, S063). Write fictional herds *like* these mechanics, never *as* these peoples (`hunting-foraging-subsistence.md:195`).

**Precision traps.** "Nomad" names a mobility strategy and "pastoralist" a livelihood; neither names a stage or a people. "Transhumance" is a fixed seasonal cycle, not any movement.

## 14. Recheck

Before relying on any §13 row, re-check its row id in `corpus/SOURCES.md`; open Herskovits 1926 and Ostrom 1990 before quoting them (only S053 and S055 are opened); re-open S050 and S067 before quoting a date; re-run the head's gap sweeps before claiming the gap is still fresh.

## 15. Scope

Reference method and lane policy for the culture-material partition. This entry owns the herding register — species portfolio, mobility, herd management, products, herd wealth and transfer, tenure, pastoral–sedentary exchange and the herd's ritual ledger — at comparative level, and hands the field, the hunt, the dish, the cloth, the road, the market, the lexicon field, the animal sign and the shepherd-king to their owners (§2). Handoff to lore-shokunin: which herds, routes, marks, raids and rites exist in a world is canon, decided there; the lore intake of the integration contract is still pending, so every handoff is a candidate, not an import.
