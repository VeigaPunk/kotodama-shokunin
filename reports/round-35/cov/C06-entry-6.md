- Seat: C06 | executor | claim C (coverage) | date 2026-10-19 | baseline 4a7aede

## 1. What this seat produced

**Draft for culture-material entry 6 of 6** (claim C, coverage). Intended landing path: `corpus/knowledge/culture-material/fire-fuel-light.md`. The full entry bytes are the single fenced block in §3 — this seat wrote no corpus file, no tool, no README; the integrator applies the block verbatim.

Draft measurements (author-side): **47669 bytes, 174 lines, 12 numbered sections**, sha256 `481cf1c24734c1251879f3e2928fb9d470db7eae11a375982786602ed74c6558` over the exact bytes inside the fence below. That digest is of the draft as checked in §4; the integrator's landing copy should reproduce it byte-for-byte or the checks below do not carry.

## 2. Gap evidence (no-filler check)

The partition has 18 committed files at HEAD 4a7aede (`ls corpus/knowledge/culture-material/*.md | wc -l` → 18). No file owns fire/fuel/light; the sweep found only incidental mentions, and the boundary is stated inside the entry (§1) so nothing bleeds:

```
grep -ril -e hearth -e rushlight -e tallow -e beeswax -e "lamp oil" -e fire-making -e firelight corpus/knowledge/culture-material/
  → architecture-settlement-lexicon.md (heating lexicon, :49), cuisine-food-lexicon.md (cottage hearth, :26),
    vessel-container-lexicon.md (firing vocabulary, :97)
grep -ril -e ignition -e tinder -e candlestick -e lamplighter -e curfew -e "fire mark" corpus/knowledge/culture-material/
  → no matches
ls corpus/knowledge/*/fire* corpus/knowledge/*/fuel* corpus/knowledge/*/light*  → no such file (no slug collision)
```

The three incidental-mention files are named as boundaries in the entry's `- couples:` and §1: architecture owns *where heat sits in a building* (`architecture-settlement-lexicon.md:49`), vessel owns *cookware and kiln firing* (`vessel-container-lexicon.md:33,97,163`), cuisine owns *what is cooked* (`cuisine-food-lexicon.md:26,42`). The new file owns the fire itself.

## 3. The entry bytes (draft — integrator applies verbatim)

```markdown
# Fire, fuel, and light — the hearth as an institution, the fuel ladder, ignition, lamp and candle, and the fire-risk apparatus a built world owes

- gap: the fire/fuel/light register is absent from culture-material — the partition owns what is cooked (`cuisine-food-lexicon.md`), the vessels that take fire (`vessel-container-lexicon.md`), where heat sits in a building (`architecture-settlement-lexicon.md:49`), and what the forge produces (`craft-artisan-lexicon.md:96,100`), but no file owns the fire itself: how it is struck and kept, what a culture burns and what that costs it, how it is turned into light, and the institutions it forces into being (watch, curfew, insurance, hearth tax, sweeper). Sweep, run 2026-10-19 from the lane root over the committed 18-file partition: `grep -ril -e hearth -e rushlight -e tallow -e beeswax -e "lamp oil" -e fire-making -e firelight corpus/knowledge/culture-material/` → 3 files, all incidental (`architecture-settlement-lexicon.md` heating lexicon, `vessel-container-lexicon.md` firing/cooking, `cuisine-food-lexicon.md` the cottage hearth); `grep -ril -e ignition -e tinder -e candlestick -e lamplighter -e curfew -e "fire mark" corpus/knowledge/culture-material/` → no matches. This entry fills that gap.
- topic: fire as the material system a culture is organized around — the hearth as an institution rather than a fixture (household unit, tax unit, cult center, the smoke it forces into architecture), the fuel ladder (wood → charcoal → peat → turf-dung → coal → oil → gas, each rung moving the fuel further from the household and closer to a trade that owns it), ignition (drill, saw, strike-a-light, fire piston, sulphur splint, phosphorus match) and the kept-embers economy, the light ladder (rushlight, tallow, beeswax, oil lamp, gas, kerosene) with light quality as a rank code, and the fire-risk apparatus — night watch and *vigiles*, curfew as a fire ordinance that became a time ordinance, firebreaks and building codes, the fire engine, the fire mark and the insurance brigade, the hearth tax that turned fireplaces into documents, the chimney sweep — plus the fire word-bank, the archaeological signature of fire (ash, charcoal, rubefaction, destruction layers), a build order, a decision record, and the calibration shelf; boundary stated in §1 (the ritual meaning of fire belongs to myth-symbol, the cookware to `vessel-container-lexicon.md`, the building's heating design to `architecture-settlement-lexicon.md`).
- sources:
  - Forbes (1955–1964), *Studies in Ancient Technology*, 9 vols, E. J. Brill — the standard survey of ancient heat, fuel and lighting practice; cited here for the technology inventory, volume/plate locators not re-opened this round (see `- verified-at:`) (`to-verify`: vol. and page for each specific item).
  - Biringuccio (1540), *De la pirotechnia*, trans. Smith & Gnudi (1942; repr. 1990), MIT Press — the first printed handbook of pyrotechnology (furnaces, fuels, alloys, fire assays); used as the period voice for what a workshop fire was expected to do.
  - Agricola (1556), *De re metallica*, trans. Hoover (1912), Mining Magazine — mine and smelter fire practice, fuel and ventilation; the *De natura fossilium* (1546) is the usual attribution for the coining of *petroleum* (`to-verify`: exact first-use page).
  - Nef (1932), *The Rise of the British Coal Industry*, 2 vols, George Routledge — the classic thesis of an early-modern English timber-to-coal substitution; Hatcher (1993), *The History of the British Coal Industry*, vol. 1: *Before 1700*, Oxford UP — the later, more granular reading; Wrigley (1988), *Continuity, Chance and Change*, Cambridge UP — the qualified demographic/energy reading. House rule: the "timber crisis" is a debated magnitude, not a settled crisis (see §11).
  - Schivelbusch (1988; Eng. trans. Davies 1988/1995), *Disenchanted Night: The Industrialization of Light in the Nineteenth Century*, Berg — street lighting, the gasworks, and the social reading of artificial night.
  - O'Dea (1958), *The Social History of Lighting*, Routledge & Kegan Paul — domestic lighting materials and their class distribution (`to-verify`: edition/pages for the tallow-versus-wax cost claims).
  - Craddock (1995), *Early Metal Mining and Production*, Edinburgh UP / Smithsonian — charcoal-hungry smelting as a landscape industry; already the citation behind `material-culture-inference-method.md:66`.
  - Eliade (1956; 2nd ed. 1978), *The Forge and the Crucible*, U Chicago Press — fire, smithing and initiation, already cited at `craft-artisan-lexicon.md:9`; and Kapp, Kapp & Yoshihara (1987), on the Japanese *tatara* smelt with its purity rules and multi-day fire, already cited at `craft-artisan-lexicon.md:100`.
  - Sahagún, *Florentine Codex*, Bk VII (trans. Anderson & Dibble 1950–82), U Utah Press — the New Fire account; Helmke, Nielsen & Rivera Guzmán (2023) — the contested uniform-schedule reading, as carried at `mexica-aztec.md:123-124`.
  - Schippmann (1971) and Boyce (1975) — Sasanian fire-sanctuary evidence and its limits, as carried at `persia-sasanian.md:110,112`; Tahmasbi (2012), *Sasanika Archaeology* 8 — sacred fire shielded from direct sunlight, carried at `persia-sasanian.md:19`.
  - In-corpus retrievable cross-references, re-checked by grep this round (each resolves): `culture-material/architecture-settlement-lexicon.md:33` (ger *toono*, the smoke hole directly above the hearth), `:49` (heating lexicon: hypocaust/ondol/kang/Kachelofen/glória), `:98` (teramachi temple districts relocated as firebreaks), `:124` (hearth as *focus*; Latin *focus* 'hearth' → fr. *foyer*, sp. *hogar*), `:140,144` (where the heat is; firebreak districts encode what the state fears); `culture-material/vessel-container-lexicon.md:33` (cooking vessels, round-bottomed for hearths, flat for stoves), `:97` (firing vocabulary), `:163` (if there is no kiln, name what the fire is — open hearth, pit); `culture-material/cuisine-food-lexicon.md:26,42` (the cottage hearth; Lévi-Strauss's roasted-on-open-fire slot); `culture-material/material-culture-inference-method.md:66` (energy & fuel row: "what burns, who owns the fuel"); `culture-material/textile-technology.md:12` (vat dyes need a fermenting vat — a heat and fuel demand on the dye house); `culture-material/calendar-festival-systems.md:40,48` (signal fires as legal acts; speech and light); `myth-symbol/ritual-liminality.md:63,83,88,93` (agnihotra daily fire oblation; Holi's bonfire of Holika; Obon *mukaebi*/*okuribi*; the Aztec New Fire, hearths killed and relit from drilled fire, last performed 1507, Codex Borbonicus); `myth-symbol/celestial-symbolism-calendars.md:143,170` (the Calendar Round closed by re-lighting every hearth; New Fire firegear); `myth-symbol/cosmology-cosmography.md:124` (the New Fire drilled on a captive's breast at Huixachtécatl; every hearth relit from it); `myth-symbol/creation-myths-taxonomy.md` (fire-rain destruction slots in the Five Suns sequence, at `cosmology-cosmography.md:85`); `civilizations/rome.md:58` (Janus, Vesta — beginnings, hearth, priesthood); `civilizations/israel-ancient-hebrew.md:153` (temple lamp, household lamp and communal emblem need separate evidence records); `civilizations/java-majapahit.md:108` (the *blencong* lamp as a staging technology); `civilizations/austronesia-philippines-taiwan.md:161` (ritual lamps named in a 1589 description, with the translation caveat attached); `civilizations/japan-heian.md:103,108` and `civilizations/china-han.md:72,78` (Fire as a five-phase slot and its generating/conquest sequences — correlative, not causal); `civilizations/mexica-aztec.md:120-124,175` (xiuhmolpilli terminology; the 1507 observance; the contested schedule; renewed fire distributed from ceremonial centers to households); `civilizations/persia-sasanian.md:19,110,112` (fire-sanctuary architecture cautions; the fire grades not to be back-projected).
- couples: culture-material/architecture-settlement-lexicon.md (that file owns where heat sits in the building — hypocaust, ondol, kang, the smoke hole; this file owns what feeds it and what it costs), culture-material/vessel-container-lexicon.md (that file owns the cookware and kiln firing; this file owns the fire that the pot sits in and the rule at its `:163`), culture-material/cuisine-food-lexicon.md (the raw/cooked axis is that file's; the hearth that performs the transformation is this one), culture-material/craft-artisan-lexicon.md (the forge as a craft deity's workplace is its `:96,100`; the fuel, draught and fire-tending that make the forge possible are here), culture-material/textile-technology.md (vat dyeing's heat demand is the coupling point), culture-material/material-culture-inference-method.md (shared substrate-inventory contract at its `:92`; this file expands its `:66` energy-and-fuel row into a register), culture-material/trade-economy-lexicon.md (fuel and light are commodities with measures, monopolies and smuggling; whale oil and kerosene are trade objects), culture-material/calendar-festival-systems.md (fire festivals and signal-fire law sit in its festival arcs; the fire apparatus they move is here), culture-material/era-periodization-models.md (an energy transition — open hearth to chimney to coal to gas to grid — is one of the cleanest era seams a material culture offers), culture-material/costume-semiotics.md (the fire mark, the lantern duty, the sweep's badge: risk institutions manufacture legible signs), culture-material/sumptuary-law-rank-display.md (beeswax versus tallow, and who may burn what, is a display law with a fuel bill), culture-material/ritual-garments.md (candle-bearing processions, fire-gear, and the vestments that must not burn), culture-material/warrior-material-culture.md (incendiaries, fire arrows, the fire ship, gunpowder — the weapons side is that file's; this file stops at the fuel), culture-material/transport-mobility-lexicon.md (beacon chains, harbour lights and lighthouse fuel are route institutions with a fire bill), myth-symbol/ritual-liminality.md (the rite grammar of fire — calendrical fires, oblation, the New Fire, festival bonfires — is that file's `:63,83,88,93`; this file supplies the apparatus and the fuel), myth-symbol/celestial-symbolism-calendars.md (sky-anchored fire rites and the firegear they require), myth-symbol/cosmology-cosmography.md (§8's New Fire and the hearth-relighting that closes a world-age), myth-symbol/creation-myths-taxonomy.md (fire-rain and fire-death in cosmogonic sequences), myth-symbol/symbolism-synthesis-method.md (fire as a cross-register carrier: colour, direction, number and animal readings all ride on it — the register rules stay that file's), myth-symbol/color-symbolism.md (flame colours, ember reds, the light/dark axis), linguistics/politeness-taboo-euphemism.md (fire names in avoidance and ritual registers; the hearth god addressed by circumlocution), linguistics/semantics-pragmatics.md (the fire/light lexical fields and their metaphoric drift), linguistics/naming-systems.md (lamp and light in personal names and place names), linguistics/language-contact.md (fuel and lighting loans as dated contact strata: *kerosene*/*paraffin*, *matchi*, *chandelier*), linguistics/historical-linguistics.md (etymology chains for *focus*, *ignis*, *candela*, *pyr*), linguistics/semantic-fields-lexicon-building.md (fire and light as a field brief with borrowability strata), linguistics/sociolinguistics-registers.md (the fire-tender's and lamplighter's trades as speech communities), synthesis/worldbible-integration-contract.md (handoff route), synthesis/loanword-material-dating.md (the word-entry clock for a lamp name is not the lamp's arrival clock), synthesis/contact-scenario-builder.md (imported lamps, oil and lampsmiths as contact objects), synthesis/era-language-staging.md (lighting vocabulary as a stratified register across staged eras), synthesis/coupling-model.md (the fire system as a coupled sub-system with its own rate of change), verification/citation-format-and-source-registry.md (citation profile used here), verification/to-verify-triage-protocol.md (the marks carried below), civilizations/rome.md (Vesta, the civic hearth), civilizations/israel-ancient-hebrew.md (the lamp's evidence problem), civilizations/persia-sasanian.md (fire-sanctuary calibration), civilizations/java-majapahit.md (the *blencong*), civilizations/japan-heian.md and civilizations/china-han.md (Fire as a phase), civilizations/mexica-aztec.md and civilizations/egypt-ancient.md (New Fire and the temple-fire economies), civilizations/inuit.md and civilizations/tibet.md (lamp-based domestic heat and light — couple before claiming, this file supplies no culture-specific lamp form), handoff target: lore-shokunin receives the hearth/fuel/light tables, the risk-institution list and the word-bank as era-anchored options with calibration flags — which fire is sacred, who owns the fuel, and who may carry a light are canon decisions and stay lore's.
- source: the works and in-repo receipts listed above; the tables and craft rules are this lane's synthesis, not quotations from the cited works.
- verified-at: 2026-10-19 — offline seat (no network this round): every in-corpus path:line citation above was re-checked by grep at HEAD 4a7aede and resolves; the partition gap sweep was run this round and its command is recorded in `- gap:`. External works are cited bibliographically and were **not** re-fetched or re-opened this round — no page, plate or edition was inspected, so every item whose exact locator or number matters is marked `(to-verify)` inline and listed in §11. The New Fire, Sasanian fire-sanctuary, *tatara*, forge-deity, five-phase Fire and *blencong* material are carried from sibling entries whose own verification lines govern them; this entry re-uses them as couplings, not as fresh verification. No admission, no promotion, no canon.
- recheck: before putting any date, statute, cost ratio, or attribution from §3–§5 into a world bible as fact — the match chronology, the curfew's royal attribution, the vigiles' numbers, the engine and gas-lighting dates, the hearth-tax window, the sweep acts, the beeswax liturgical requirement, the kerosene/*paraffin* naming split — re-open the cited work and the period source; before reusing any lamp form (qulliq, butter lamp, *andon*) culture-specifically, couple to the civilization entry and obtain a dated object catalogue; before stating a "timber crisis" or an "energy transition", name which thesis is being followed (§11).

## 1. The frame: fire is three systems, and none of them is the flame

- **Three systems.** FIRE-PRODUCTION (how a culture strikes and keeps fire: §3), FIRE-CONSUMPTION (what it burns and what that costs: §2, §4), and FIRE-CONSEQUENCE (the institutions the risk of fire forces into being: §5). The flame is the interface; the culture is in the other three.
- **Boundaries, stated so nothing bleeds.** The meaning of fire in a rite belongs to `myth-symbol/ritual-liminality.md` (calendrical fires, oblation, festival bonfires at its `:63,83,88,93`); the cookware and the kiln belong to `culture-material/vessel-container-lexicon.md` (its `:33,97,163`); where heat sits in a building belongs to `culture-material/architecture-settlement-lexicon.md` (its `:49` heating lexicon, `:33` smoke hole); the forge's products and its deities belong to `culture-material/craft-artisan-lexicon.md` (`:96,100`); the incendiary weapon belongs to `culture-material/warrior-material-culture.md`. This entry owns the fire itself: the hearth as a social and fiscal unit, the fuel, the light, and the risk apparatus.
- **The master craft claim.** A culture's fire system is a *dependency ladder*: every rung upward (wood → charcoal → coal → oil → gas → grid) moves the fire further from the household and closer to a trade, an owner, and a price — so the history of fire is the history of a household function becoming an infrastructure. Write the ladder and you have written the economy.
- **Second craft claim.** Fire is the only material a culture buys *by the hour*. Every other material good is bought as an object; light is bought as time (a candle-hour, a lampful, a gas meter). That is why lighting is the cleanest class marker in any material culture, and why curfews are so easy to write (§5).

## 2. The fuel ladder

| Rung | What it costs | What it yields | What it changes |
|---|---|---|---|
| Gathered wood | labor, land access, drying time | smoke, variable heat, a fire that needs tending | the hearth is a *labor* institution; children and the old tend it |
| Managed wood (coppice, wood-lot law) | an owner, a rotation of years, a right of estovers | predictable supply | fuel becomes *property*; the wood-lot and the right to deadfall are legal objects |
| Charcoal | a kiln or mound, a collier's trade, days of controlled smothering | roughly double the heat per weight of the wood it came from, far less smoke, and a fuel that can be *transported* | the first manufactured fuel; smelting becomes possible away from the forest — `material-culture-inference-method.md:66`: "charcoal-hungry smelting and mining as landscape industry (Craddock 1995)" |
| Peat / turf | wet land, cutting season, stacking and drying | a long, slow, low flame; heavy ash | a seasonal labor calendar tied to the bog, and a distinct regional taste in smoke |
| Dried dung | the herds' output, and therefore the fields' | a hot, fast, smoky fire | a real trade-off against manure; fuel-poor pastoral cultures pay for it in soil |
| Coal | a mine, a chimney, a grate, and a willingness to smell sulphur | dense heat, near-permanence, industrial scale | architecture changes to fit the fuel (chimney, grate, flue); the household fire becomes a *delivery* |
| Oil / gas / grid | a refinery, a pipe network, a utility | light and heat at a switch | the fire leaves the house entirely; what remains at the hearth is a *bill* |

- **The ladder is not a progress sequence.** It is a *cost* sequence, and cultures sit on different rungs for different jobs at the same time: charcoal for the smelter, dung for the winter hearth, beeswax for the altar, tallow for the kitchen, oil for the street. Give a fictional culture a rung per job, not one fuel.
- **Craft rule (fuel is geography).** Ask of a fictional culture: what can it burn without a mine, without a bog, without a forest? Its fuel map is its ecology map, and whoever owns that map owns the winter. Write the fuel *map* before the fuel *ladder*.
- **Craft rule (the collier is a liminal trade).** The charcoal burner lives outside the settlement, in the woods, on a multi-day fire that must not be allowed to flame — a documented pattern of social distance (couple `myth-symbol/ritual-liminality.md` on liminal occupations, and `craft-artisan-lexicon.md` on craft outsiders).
- **The "timber crisis" is a debated magnitude, not a settled fact.** The Nef (1932) thesis of an early-modern English wood shortage driving the coal switch has been qualified by later work (Hatcher 1993; Wrigley 1988): relative prices, transport costs, urban scale and the coal's own disamenities all carry part of the explanation. Write the *switch* as an era seam; do not write the *crisis* as a number without naming the thesis (§11).

## 3. Ignition: the fire-kit and the kept fire

| Method | Apparatus | Skill / cost | Cultural signature |
|---|---|---|---|
| Hand drill, bow drill | spindle, hearth board, tinder | a trained wrist; minutes of work; tinder must be bone-dry | fire as *labor*; the drill as a tool with its own name and taboos |
| Fire saw, fire plough | split cane / soft wood, friction groove | fast where the material suits; regional | a technique that dates a material ecology, not a technology level |
| Fire piston | sealed cylinder, piston, tinder | a made instrument; needs a good fit | a prestige fire-kit; ignition as a *device* |
| Flint and steel (strike-a-light) | steel striker, flint or pyrite, char cloth / amadou (*Fomes fomentarius*) / birch bark | a kit carried on the person; seconds once the tinder is dry | the fire-kit as personal equipment, worn like a purse; strike-a-lights enter grave inventories |
| Sulphur splint / tinderbox | splint dipped in sulphur, tinderbox with a damper | a household object, kept on the mantel | fire becomes *household furniture*, not a skill |
| Phosphorus match | stick + a combustible head | a chemical industry, a factory, and a regulation problem | ignition is *bought in boxes*; the chemistry's harms become a labour scandal |

- **The match chronology (mark to-verify per item, §11).** The friction match is credited to John Walker of Stockton-on-Tees, 1826; the white-phosphorus match that followed caused *phossy jaw* in the match factories and was the object of the Berne white-phosphorus ban of 1906; the "safety" match (red phosphorus on a separate striking surface) is credited to the Lundström/Pasch line in Sweden, 1844. Every one of these dates is a *checkable* claim and none was re-opened this round.
- **The kept fire is the default, not the fallback.** Where striking is slow or tinder unreliable, the household's real technology is *keeping*: banking the embers under ash overnight, the covered hearth, the neighbourly "borrowed fire" carried in a pot. Design the fire's *night rule* — what the culture does between the last banking and the first relighting — and you have designed its morning.
- **The kept fire has an institutional ceiling: the perpetual fire.** Where the fire must never go out — the temple, the palace, the civic hearth — the keeping becomes an office with a budget and a scandal (a fire that dies is an omen; a keeper who lets it die is punished). Roman Vesta is the in-corpus anchor for the civic case (`civilizations/rome.md:58`); the Aztec New Fire is the opposite design — the whole culture lets the fire die on purpose, on a schedule (§6).
- **Craft rule (ignition is gendered labor before it is chemistry).** The cheaper the strike, the less the household spends on keeping — and the labor saved is normally the labor of the people who tended it. Write the fire-kit change as a household-labor change, and the era seam writes itself (couple `culture-material/era-periodization-models.md`).

## 4. Light: what burns, what it smells like, and who can afford it

| Source | Fuel | Light quality | Signature | Class reading |
|---|---|---|---|---|
| Rushlight / splint | rush dipped in grease, held in a nipper | a few minutes of dim, smoky light | the cheapest possible light; a *task* light, not an evening light | the poor's light; the length of the rush is the length of the evening |
| Tallow candle | rendered animal fat, cotton/hemp wick | yellow-dim, rancid smoke, frequent snuffing | the chandler's trade; the smell is the tell | household light with a smell you can read from the doorway |
| Beeswax candle | beeswax, plaited wick | bright, sweet-smelling, slow, clean | the altar's light; often *required* by liturgical rule (`to-verify` per rite) | the light of the institution and of those who can pay for sweetness |
| Oil lamp | olive, sesame, castor, fish, whale, nut oil; floating or drawn wick | steady, controllable, needs filling and trimming | the lamp is a *vessel* — shape, spout, handle, and a god's name on it | the urban light; oil is a commodity with a price and a supply route |
| Gas | coal gas, later natural gas; a burner and a pipe | bright, hard, flickering, hot | the gasworks, the lamplighter, the meter | light becomes a *utility bill* and a municipal service |
| Kerosene / paraffin lamp | distilled petroleum | bright, portable, cheap | the 19th-c. rural light revolution; the naming split *kerosene* (US) / *paraffin* (UK) is a dated contact marker (`to-verify`: first-use dates) | light reaches the farmhouse; the oil trade becomes global |

- **Light forms worth stealing.** The open saucer lamp with a floating wick (cheapest possible oil light); the closed lamp with a spout (the light becomes a *container*); the hollow circular wick with a chimney, which is the technical break that made lamp light bright (Argand, 1780s — `to-verify`); the pressure lamps that came after (`to-verify`); the soapstone oil lamp of the Arctic and the butter lamp of Inner Asian Buddhist practice — **couple to `civilizations/inuit.md` and `civilizations/tibet.md` before naming either culture-specifically: this file asserts no lamp form for any culture**; the Javanese *blencong* as a *staging* technology, already carried at `civilizations/java-majapahit.md:108`.
- **The lamp is a document.** A lamp's shape, spout count, handle and stamp are datable; a lamp found in a grave is an object biography (couple `culture-material/vessel-container-lexicon.md` for the container logic and `material-culture-inference-method.md` for the biography method). Where a culture stamps its lamps, the stamp is an administrative fact.
- **Craft rule (light is bought by the hour).** Write the lighting budget per class: how many candle-hours a household can afford per night, and what happens when the budget runs out (early sleep, the common room, the neighbour's fire). The curfew (§5) is often just the moment a town stops paying for light.
- **Craft rule (smell is a rank code).** Tallow's rancid smoke versus beeswax's sweetness is a *legible* difference at a distance — the cheapest possible way to stage rank in a scene without a single line of exposition. Couple `culture-material/sumptuary-law-rank-display.md` (who may burn what) and `culture-material/costume-semiotics.md` (what a smell tells a visitor).
- **Street lighting as governance.** Lighting a street is a claim about who owns the night: the lantern duty on householders, the hired lamplighter with his ladder and his hour, the gasworks and its mains, and the recurring argument that light reduces crime (Schivelbusch 1988/1995). For a fictional city, decide *who pays* — the household, the guild, the municipality, the utility — and the politics of the night are decided with it.

## 5. The fire-risk apparatus: what the risk of fire builds

- **The night watch.** Rome's *vigiles* — a corps raised under Augustus (traditionally 6 CE) as a night fire-and-police force (`to-verify`: cohort count, strength, legal status); the medieval *watch and ward* as a rotating household duty; the watchman's call as the town's clock. Design rule: a fire watch is the cheapest way to give a pre-modern city a *night institution* — a set of people who are awake, licensed, and expected to shout.
- **Curfew.** *Couvre-feu* means, literally, "cover the fire": a fire ordinance — bank the hearth, cover the embers, go in — that hardened into a time ordinance and then into a bell. The popular attribution of the English curfew to William the Conqueror is repeated in general sources and is thin in evidence — treat it as the classic *law-that-is-really-a-story* and mark it (`to-verify`, §11). Craft use: the curfew bell is the easiest way to make a town's clock *audible*, and its abolition is an era seam.
- **Firebreaks and building law.** Temple districts relocated to a city's edge as firebreaks are already carried at `architecture-settlement-lexicon.md:98` (the *teramachi* case); the general rule is that a fire code is written in *materials* (tile instead of thatch, stone instead of timber, plaster over lath), in *gaps* (the firebreak street, the empty lot), and in *rights* (the authority to enter and demolish a burning building — a real, and resented, legal power). `architecture-settlement-lexicon.md:144` states the reading rule: firebreak districts encode what the state fears.
- **Firefighting technology.** The bucket chain (a *labor* answer: neighbours, a line, a river); the hand squirt; the leather-and-brass pump engine (Jan van der Heyden's engine and his 1690 book are the standard attribution — `to-verify`); the Newsham engine (1721) — `to-verify`; the steam fire engine (1829) — `to-verify`; the fire pole and the horse-drawn steamer — `to-verify`. Each step converts the answer from *people* to *capital*, which is the same move the fuel ladder makes (§2).
- **Insurance and the fire mark.** After the Great Fire of London (1666) the fire office appears as a commercial answer to a municipal failure (the Fire Office, 1680; the Hand in Hand, 1696 — `to-verify` per firm), and with it two durable institutions: the **fire mark** — a metal plaque on the wall showing which office insures the building, and therefore which private brigade will fight the fire — and the *insured-versus-uninsured* asymmetry, where a brigade may stand by and watch a rival's building burn. The fire mark is one of the purest examples of a material culture object that exists only because of a risk economics: couple `culture-material/costume-semiotics.md` and `sumptuary-law-rank-display.md` for the sign-reading logic, and `culture-material/era-periodization-models.md` for the transition to a municipal brigade.
- **The hearth tax: the fireplace as a document.** Where a state taxes hearths, the fireplace stops being furniture and becomes an administrative fact: the hearth tax returns are, in effect, a *household census* keyed to the chimney (England & Wales, 1662–1689 — `to-verify` the exact window and the exemption rules; the Scottish hearth tax is later, `to-verify`). Two worldbuilding yields: (1) the tax makes a *building feature* legally visible, so the number of chimneys becomes a status and evasion game (blocked hearths, hidden flues, the assessor's visit); (2) the records it leaves are the best list of households a fictional archive can hold. Couple `culture-material/trade-economy-lexicon.md` for the fiscal vocabulary and `culture-material/architecture-settlement-lexicon.md` for the building.
- **The chimney and its trade.** The chimney that coal requires also requires *sweeping*, and sweeping requires someone small enough to climb it: the climbing boy is the institution's human cost, and its regulation (a series of 19th-c. acts, `to-verify` per act, the 1875 Act among them) is a clean example of a technology producing a labor scandal that law eventually ends. Design rule: for every fuel rung above wood, name the *maintenance trade* it creates — collier, sweep, lamplighter, stoker, meter-reader.
- **Fire as a weapon — the boundary.** Incendiaries, fire arrows, fire ships, "Greek fire" (whose composition is unrecovered; every claimed formula is a reconstruction — a calibration item, §11), and gunpowder belong to `culture-material/warrior-material-culture.md`. This file supplies only the fuel, the light, and the risk apparatus; a siege-fire doctrine should be filed to that entry, not here.
- **Fire as record destruction.** The deliberate burning of archives, registers or books is a political act with a material signature (the scorched roll, the burnt layer, the gap in a series). It is the cheapest way to write a *hole* into a fictional archive — and the archaeologist's counterpart is §8.

## 6. Fire and time: the schedule the fire keeps

- **Boundary first.** The *rite grammar* of fire is `myth-symbol/ritual-liminality.md`'s (`:63,83,88,93`); what this file owns is the apparatus and the schedule those rites move — which hearths, which lamps, whose fire, relit from where, at whose cost.
- **The New Fire (the strongest in-corpus fire institution).** The Aztec 52-year cycle: fires extinguished, a vigil, a fire drilled on a sacrificed captive's breast at Huixachtécatl, and fire redistributed from ceremonial centers to every household (`myth-symbol/cosmology-cosmography.md:124`; `myth-symbol/celestial-symbolism-calendars.md:143`; `myth-symbol/ritual-liminality.md:93`, last performed 1507, Codex Borbonicus). The calibration is already filed at `civilizations/mexica-aztec.md:120-124`: keep *xiuhmolpilli* as bundle/cycle terminology distinct from the verb forms, and do not state a uniform immutable 52-year schedule everywhere — Helmke, Nielsen & Rivera Guzmán (2023) contrast uniform colonial schedules with varied monument dates. And `civilizations/mexica-aztec.md:175` gives the design rule: renewed fire is a *scarce ritual resource distributed through institutions to households* — the best single model in the corpus for a fire that is also a polity.
- **Perpetual and graded fire.** Roman Vesta (`civilizations/rome.md:58`); the Zoroastrian fire grades — with the caution already carried at `civilizations/persia-sasanian.md:112` (do not back-project the modern Ātaš Bahrām/Ādarān/Dādgāh classification and consecration procedures onto every Sasanian sanctuary), the *čahārṭāq* caution at `:110` (a four-arched form is not automatically a fire temple), and the period detail at `:19` (sacred fire shielded from direct sunlight, Tahmasbi 2012). Design rule: a graded fire system — a highest fire that only a capital may keep, regional fires, household fires — is a *jurisdiction* map written in flame.
- **Daily fire as an obligation.** The Vedic *agnihotra*, the daily milk oblation into the fire, is already carried at `myth-symbol/ritual-liminality.md:63` as a calendrical/maintenance rite: fire-tending as the calendar's smallest repeating unit. Any fictional temple economy can be built on a daily fire with a named fire-tender and a fuel budget.
- **Festival fire.** Holi's bonfire of Holika (`ritual-liminality.md:83`); Obon's *mukaebi* welcome fires and the *okuribi* send-off (Kyoto's Daimonji) at `:88`; the signal fires that make an intercalation proclamation a legal act at `culture-material/calendar-festival-systems.md:40,48` ("speech and light as legal acts"). Craft rule: a festival fire has a *fuel bill* and a *tender*, and both are places to hang plot.
- **Fire as oath and ordeal.** The trial by fire and the oath sworn over fire are widely attested patterns and are **not** verified here — mark any specific procedure `to-verify` and couple `myth-symbol/ritual-liminality.md` for the rite grammar rather than inventing a procedure.
- **Fire as an era boundary in the calendar itself.** Where the fire is relit on a schedule, the fire *is* the epoch: the New Fire is the corpus's worked example, and `culture-material/era-periodization-models.md` owns the periodization side.

## 7. The fire word-bank

| Slot | Real forms | What the form carries |
|---|---|---|
| The hearth | Latin *focus* 'hearth' → English *focus*; fr. *foyer*; sp. *hogar*; Gk. *hestia*; the "hearth and home" pairing | the hearth as the *center* of a household and of attention; the metaphor outlived the object (`architecture-settlement-lexicon.md:124`) |
| Fire itself | Gk. *pyr* πῦρ → *pyre*, *pyrotechnic*, *empyrean*; L. *ignis* → *ignition*, *igneous* | fire words split between the *flame* and the *act of lighting*; the ritual register usually keeps the older root |
| Light | L. *lux* / *lumen*; the fire/light conflation in languages where one word covers both (Japanese *hi* 火, with *akari* 明かり for illumination — `to-verify` the fine semantics) | whether a culture *separates* fire from light is a lexical fact with a design consequence: a fused word cannot easily say "a light with no fire" |
| The lamp | L. *lucerna*; Gk. *lychnos* λύχνος; Arabic *misbāḥ* / *qindīl*; Japanese *tōrō* 灯籠, *andon* 行灯, *chōchin* 提灯; Javanese *blencong* (`civilizations/java-majapahit.md:108`) | the lamp's name usually says *shape*, *function*, or *material*, never "lamp" — the same naming grammar as vessels (`vessel-container-lexicon.md`) |
| The candle | L. *candela* → *candle*, *chandler*, *candelabra*, *chandelier* | the word travels with the wax trade and outlives the tallow it named |
| The fuel | *charcoal* / *collier* / *coal* (the same root family, the manufactured fuel named after the natural one); *peat* / *turf* (a regional split); *kerosene* (US) vs *paraffin* (UK) — a dated transatlantic split; *petroleum* (L. *petra* + *oleum*, 'rock oil', coined in the 16th c. — `to-verify`: Agricola, *De natura fossilium* 1546) | fuel words are the most *technical* and the least metaphoric — they stay literal while light words drift |
| The match | fr. *allumette* ('little match'); Ger. *Streichholz* ('strike-wood'); Japanese *matchi* マッチ | the naming shows the *action* the culture sees in the object: light, strike, or borrowed trade word |
| The risk words | *curfew* < *couvre-feu* 'cover the fire'; *fire mark*; *hearth money* / *chimney money*; *watch and ward* | risk vocabulary is *ordinance* vocabulary: every word here is a rule with a bell attached |

- **Craft rule (light words drift, fuel words stay).** Metaphor harvests the *light* family (enlighten, spotlight, shine, lamp of wisdom, beacon) far faster than the *fuel* family, which stays technical. Use the split as an era-drift fingerprint: an archaic-sounding metaphor built on a fuel word is a much later coinage than it sounds (couple `synthesis/era-language-staging.md` and `linguistics/historical-linguistics.md`).
- **Craft rule (the avoidance register).** Where a hearth fire is a household god or an ancestral presence, its name may be spoken only in circumlocution — the fire named by what it does, not what it is. This is a *claim about a pattern*, not about a specific culture: mark any instance `to-verify` and hand the register mechanics to `linguistics/politeness-taboo-euphemism.md`.

## 8. What fire leaves: the archaeologist's fire

- **The signature set.** Ash, charcoal fragments, burnt daub, scorched floors, heat-reddened earth under a hearth (`to-verify`: the technical term *rubefaction* and its identification criteria), fire-cracked rock, and the burnt *layer* itself. A hearth is the most reliable anchor of an *occupation* unit in a domestic ruin, and the burnt layer is the stratigrapher's free boundary marker (couple `culture-material/material-culture-inference-method.md` for formation processes).
- **Fire as a dating instrument.** Charcoal is the radiocarbon sample; a hearth's remanent magnetism is a dating method (`to-verify`: archaeomagnetic dating's applicability conditions); the burnt layer is the stratigraphic seam. In a fictional ruin, a hearth gives a *date* and a *meal* at once — the cheapest two facts a ruin can be made to carry.
- **Fire as an era seam.** Destruction layers are how excavators write period boundaries; in-world, a burnt layer is how a *fictional* archive says "the old city ended here" (couple `culture-material/era-periodization-models.md`).
- **Craft rule (the forged fire).** Because ash, charcoal and a scorched layer are *easy* to fake and *hard* to date precisely, a burnt archive is the ideal object for an in-world forgery plot — the destruction is the alibi (couple `culture-material/material-culture-inference-method.md` on deposition and formation processes).
- **Cremation, briefly and by boundary.** The *rite* is `myth-symbol/ritual-liminality.md`'s; the *material* fact this file contributes is that cremation is a **fuel-intensive** operation whose cost scales with the body and the pyre's construction — a real economic constraint on a rite (`to-verify`: any specific fuel-load figure). Write cremation as a fuel decision and the rite acquires a class gradient.

## 9. Build order — designing a fictional culture's fire system

1. **Fix the fuel map (§2)**: what the ecology gives (forest, bog, pasture, mine, coast) and who owns it. Then write the fuel ladder per job, not one fuel per culture.
2. **Fix the ignition kit (§3)**: what a household actually strikes with, how long it takes, and what the *night rule* is. If striking is cheap, the fire is let out; if it is expensive, the fire is kept and tended.
3. **Fix the hearth's legal status (§1, §5)**: is the fireplace a tax unit, a cult center, a room's furniture, or a utility connection? Whose name is on it — the household's, the lineage's, the landlord's, the utility's?
4. **Fix the light budget (§4)**: what burns for light, what it smells like, how many hours a class can afford, and who owns the street's light.
5. **Fix the risk apparatus (§5)**: who watches the night, what the curfew is (and whether it is a fire rule or a time rule), what the fire code is written in, and who is insured — with the fire mark as the visible sign.
6. **Fix the maintenance trades (§5)**: collier, sweep, lamplighter, stoker — one per fuel rung above wood. A fuel system with no maintenance trade is a description, not an institution.
7. **Fix the fire's calendar (§6)**: the daily tending, the annual fire festival, and — if the culture is bold enough — the scheduled extinction (the New Fire move), with the redistribution institution named.
8. **Fix the word-bank (§7)**: the hearth word, the fire/light split (fused or separate), the lamp-naming grammar, the fuel words, and one risk-ordinance word with a bell attached.
9. **Run the coupling check**: does the fire system contradict the building vocabulary (`architecture-settlement-lexicon.md`), the vessel inventory (`vessel-container-lexicon.md`), the textile dye house (`textile-technology.md:12`), and the rite calendar (`myth-symbol/ritual-liminality.md`)? A culture with chimneys and no sweep, or with a vat dye house and no fuel budget, is a hole the reader will find.

## 10. Decision record

| ID | Decision | Trigger / condition | Evidence | Status |
|---|---|---|---|---|
| DR-FF-01 | Write the fire system as three subsystems (production / consumption / consequence) and never as a single "fire" entry | any worldbuilding pass that touches fire | this file §1; the boundary list against five sibling entries | adopted — the frame is the entry's spine |
| DR-FF-02 | Choose a fuel *per job*, not per culture, and name the owner of each fuel's source | any culture with more than one hearth use | §2 table; `material-culture-inference-method.md:66` ("what burns, who owns the fuel") | adopted — the fuel map is written before the ladder |
| DR-FF-03 | Give every fuel rung above gathered wood a maintenance trade and a labor cost | any fuel system that has advanced past wood | §5 (collier, sweep, lamplighter, stoker) | adopted — no rung without a trade |
| DR-FF-04 | Treat the "timber crisis" as a debated magnitude and cite the thesis, not the number | any claim that a culture switched fuels *because* it ran out | §2; Nef (1932) vs Hatcher (1993)/Wrigley (1988); §11 | adopted — name the thesis when writing the switch |
| DR-FF-05 | State the fire/light lexical split (fused word or separate words) before coining any lighting vocabulary | any coinage in the light field | §7; `linguistics/semantic-fields-lexicon-building.md` | adopted — a fused word cannot say "light without fire" |
| DR-FF-06 | File siege-fire, incendiaries and gunpowder to `warrior-material-culture.md`; this file carries only fuel and apparatus | any request to write a fire weapon from this entry | boundary at §1 and §5; `culture-material/warrior-material-culture.md` | adopted — hand off, do not absorb |
| DR-FF-07 | Mark every date, statute, cost ratio and attribution from §3–§5 `to-verify` until re-opened against the cited work | any number entering a world bible from this file | `- verified-at:` (offline seat, 2026-10-19); §11 | adopted — the marks are the entry's honesty |

## 11. Calibration shelf

| Claim | Status | Safe use |
|---|---|---|
| The English curfew was imposed by William the Conqueror | Repeated in general sources, thin in the record (`to-verify`) | a story a fictional town tells about its own bell |
| The "timber crisis" caused the coal switch | Contested magnitude (Nef 1932 vs Hatcher 1993, Wrigley 1988) | an era seam written as a *price and transport* story, not a scarcity fable |
| The Great Fire of London (1666) "invented" fire insurance | The fire office as an institution follows it, but earlier schemes exist and the firms' founding dates differ (`to-verify` per firm) | write the fire *mark* and the private brigade, not the invention claim |
| Hearth tax = the first census of households | The returns are a household list keyed to hearths, with exemptions and evasion (`to-verify` the English window and exemption rule) | a fictional archive's household register; never a population figure without the exemption rule |
| Greek fire's composition | Unrecovered; every published formula is a reconstruction | an in-world lost-weapon legend with rival claimants (filed to `warrior-material-culture.md`) |
| Match chronology (Walker 1826; safety match 1844; white-phosphorus ban 1906) | Standard but not re-opened here (`to-verify` each) | a chemistry-led labour scandal, not a dated sequence |
| Vigiles numbers and legal status (6 CE, seven cohorts, freedmen) | Standard textbook figures, not re-opened here (`to-verify`) | a night-watch institution with a fire brief |
| Gas lighting dates (Murdoch's demonstrations; Pall Mall 1807; the Gas Light and Coke Company 1812) | Standard but not re-opened (`to-verify` each) | the *transition* from lantern to utility, with the dates marked |
| Steam fire engine (1829) and the fire pole | Popularly dated, not re-opened (`to-verify`) | capital replacing labour in fire response |
| Argand's hollow circular wick (1780s) | Widely credited, not re-opened (`to-verify`) | the technical break that made lamp light bright |
| *petroleum* coined by Agricola (1546) | Standard attribution, not re-opened (`to-verify`) | a rock-oil vocabulary with an early-modern date stamp |
| A uniform, immutable 52-year New Fire schedule | Contested — Helmke, Nielsen & Rivera Guzmán (2023) as carried at `civilizations/mexica-aztec.md:124` | varied schedules and adjustments, per the in-corpus calibration |
| The Sasanian fire grades (Ātaš Bahrām/Ādarān/Dādgāh) apply to every sanctuary | Warned against at `civilizations/persia-sasanian.md:112`; *čahārṭāq* ≠ fire temple at `:110` | a graded-fire jurisdiction map, built from the period evidence and not back-projected |
| Lamp forms (qulliq, butter lamp, *andon*) as generic "traditional lamps" | Not verified here; this file asserts no culture-specific lamp form (`to-verify`, couple the civilization entry first) | a design slot, filled only after the civilization entry is read |

## 12. Canon boundary and handoff

- **Recipient**: lore-shokunin, via `synthesis/worldbible-integration-contract.md`.
- **This entry supplies**: the three-subsystem frame; the fuel ladder with its cost and ownership columns; the ignition-kit typology and the kept-fire rules; the light ladder with its class readings; the fire-risk institution list (watch, curfew, fire code, engine, insurance and fire mark, hearth tax, sweep); the fire word-bank; the archaeological signature set; a nine-step build order; and a decision record (DR-FF-01..07).
- **What stays with lore**: which fire is sacred and to whom; who owns the forest, the bog or the mine; who may carry a light in public; whether a culture's fire is a household god, an ancestor, or a utility; and whether any in-world doctrine claims a fire "revolution" the evidence only supports as a transition. Those are canon decisions and belong to lore-shokunin.
- **Known limits**: this seat ran offline on 2026-10-19 — no external work was re-fetched or re-opened, every numeric or dated claim from §3–§5 carries `to-verify`, and the in-corpus couplings were re-checked by grep only. The entry is a design instrument and a source map, not a verified history of fire.
```

## 4. Checks run on the draft (author-side evidence; not admission, not independent verification)

| Check | Command | Result (2026-10-19, HEAD 4a7aede) |
|---|---|---|
| Provenance gate | `python3 -B tools/gates/provenance-audit.py .scratch/c06/fire-fuel-light.md` | `INFO to-verify-count: 39 mark(s) on 34 line(s)`; `INFO scan: files=1 marks=39 mark-lines=34 findings=0 blocked=0`; exit 0 |
| Header fields | `awk '/^## /{exit} /^- [a-z-]+:/'` | 7 fields, each exactly once: `gap`, `topic`, `sources`, `couples`, `source`, `verified-at`, `recheck` |
| Couples targets | regex over the `- couples:` line vs `corpus/knowledge/` | 44 distinct targets, **0 missing** |
| All path tokens | regex over the whole entry | 45 distinct `partition/file.md` tokens, **0 missing** |
| Path:line citations | regex `file.md:NN[,NN-NN]`, each resolved against the file's line count | 24 citation sites, **0 bad** (no missing file, no out-of-range line) |
| Section refs | `§(\d+)` extraction vs `^## (\d+)\.` headings | refs used 1,2,3,4,5,6,7,8,11 — all resolve; 12 sections, no gap |
| Table integrity | trailing-pipe scan of every `|` row | 0 malformed rows |
| Slug collision | `ls corpus/knowledge/*/fire*|fuel*|light*` | no match |
| Text reuse | 8-gram body-shingle Jaccard vs the 18 committed culture-material entries | top-3: 0.0017 `transport-mobility-lexicon.md`, 0.0005 `craft-artisan-lexicon.md`, 0.0004 `material-culture-inference-method.md` — no reuse near any duplicate threshold |
| `to-verify` census | `grep -c to-verify` | 34 lines carry marks (39 occurrences); every numeric/dated external claim from §3–§5 is marked and re-listed in the entry's §11 |
| Bleed-language scan | `grep -n -i canon|promot|clearance|closure|admitted|approved` | 4 hits, all boundary/negation: the `- couples:` handoff clause, the `- verified-at:` "No admission, no promotion, no canon", the §12 heading, and the §12 "Those are canon decisions and belong to lore-shokunin" |

## 5. Frontmatter reading (for the C12/C13/C14/C17 auditors — measured, so the count is adjudicable)

Claim C asks for "frontmatter 4/4 or documented 3/4 class" and names the four fields as *source / verified-at / recheck / scope*. Measured over all 201 committed entries this round:

```
python3 -B (field-presence census over corpus/knowledge/*/*.md)
  total 201; source+verified-at+recheck+scope = 0; source+verified-at+recheck = 134;
  topic+sources+couples = 201; "- gap:" = 2
```

So **no committed entry carries a literal `- scope:` line** (0/201): the fourth field must be read as the entry's *scope statement*, which in this corpus is the `- topic:` line. Under that reading this draft is 4/4 (`source`, `verified-at`, `recheck`, `topic`-as-scope) and also 3/3 under the gate's own profile (`topic`, `sources`, `couples`, gate exit 0). Under a literal-`- scope:` reading the draft is the documented 3/4 class and so is all 201 of the corpus — the auditors should state which reading they applied.

## 6. Note for X00 / R08 (the freeze read-set question, answered for this slice)

Read-set membership reading, not a freeze run (no freeze was executed; declared-in-r7 bytes stay pinned):

```
python3 -B (regex over reports/round-34/handoff/declared-in-r7/twin.json and expected.json)
  corpus paths in the read-set: corpus/knowledge/synthesis/worldbible-integration-contract.md
    + corpus/lessons/round-6-sources/{03,05,09,13}.json
```

The landing path `corpus/knowledge/culture-material/fire-fuel-light.md` is **not** in that read-set, so a re-freeze would see no drift from this entry. (Same reading holds for the r6 packet at `reports/round-30/handoff/declared-in-r6/`.) This is a membership reading of the packet's own manifests; X00/R08 own the consolidated answer across all ten entries.

## 7. Note for C11 (README delta inputs)

- Filename: `fire-fuel-light.md` (partition `culture-material`, 18 → 19 for this entry alone; the +6 aggregate is the integrator's).
- The index row must be the entry's own `- topic:` text **byte-equal** (the round-20 sweep rule: rows are compared verbatim against the file's `- topic:` line). The line is inside the fence in §3; it is the second header line, prefixed `- topic: `.
- Index row placement: `## culture-material/ (18)` → `(24)` after all six land; row inserted in filename order (`fire-fuel-light.md` sorts after `dress-through-eras.md` and before `garment-lexicon-crosslinguistic.md`).
- The entry is written against the `## culture-material/` section's existing row style; the totals line and the counts footer move per the C11/C15 reconciliation.

## 8. Not claimed

No admission, no promotion verification, no canon decision, no commit, no corpus write, no README write. Author-side checks only; the independent auditors (C13/C14/C17) and the adversarial reviewers (R01/R02) have not yet read this draft. This fragment is a draft for the integrator, not a filed artifact of the round.

## Owed

- `reports/round-35/plan/P01-c-plan.md` — **the binding dependency for this seat's topic.** Absent at seat start (`find reports/round-35 -type f` → `claims.json`, `targets.json`, `telemetry/*` only). Per the missing-dependency rule this seat chose entry 6's topic itself (fire / fuel / light) and produced the gap evidence for it (§2). Integrator: if P01 assigns entry 6 a different topic, reconcile — the draft is a complete entry either way, and the gap evidence stands or is replaced by P01's.
- `reports/round-35/scout/K01-coverage-census.md` and `reports/round-35/scout/K02-entry-audit-method.md` — **the entry-shape and audit-method contracts.** Absent at seat start. The shape used here was derived from two committed exemplars read in full (`corpus/knowledge/culture-material/calendar-festival-systems.md`, `corpus/knowledge/culture-material/transport-mobility-lexicon.md`), `corpus/QUALITY.md`, and the provenance gate's own field profile (`tools/gates/provenance-audit.py:75-76` FIELD_NAMES = topic/sources/couples). If K01/K02 land with a different contract (e.g. a literal `- scope:` field), the integrator applies the delta to the fenced block and re-runs §4.
- `reports/round-35/cov/C12-audit-runbook.md` is the instrument the C13/C14/C17 audits will use; this seat did not have it and ran the gate directly (§4) rather than the runbook. No blocking dependency.

## Citations

In-repo paths and lines relied on (all re-checked by grep this round; each resolves):

- `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:33,49,98,124,140,144`
- `corpus/knowledge/culture-material/vessel-container-lexicon.md:33,97,163`
- `corpus/knowledge/culture-material/cuisine-food-lexicon.md:26,42`
- `corpus/knowledge/culture-material/craft-artisan-lexicon.md:9,96,100`
- `corpus/knowledge/culture-material/material-culture-inference-method.md:66,92`
- `corpus/knowledge/culture-material/textile-technology.md:12`
- `corpus/knowledge/culture-material/calendar-festival-systems.md:40,48`
- `corpus/knowledge/culture-material/transport-mobility-lexicon.md` (exemplar read in full; shape source)
- `corpus/knowledge/myth-symbol/ritual-liminality.md:63,83,88,93`
- `corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md:143,170`
- `corpus/knowledge/myth-symbol/cosmology-cosmography.md:85,124`
- `corpus/knowledge/civilizations/rome.md:58`
- `corpus/knowledge/civilizations/israel-ancient-hebrew.md:153`
- `corpus/knowledge/civilizations/java-majapahit.md:108`
- `corpus/knowledge/civilizations/austronesia-philippines-taiwan.md:161`
- `corpus/knowledge/civilizations/japan-heian.md:103,108`
- `corpus/knowledge/civilizations/china-han.md:72,78`
- `corpus/knowledge/civilizations/mexica-aztec.md:120,122,123,124,175`
- `corpus/knowledge/civilizations/persia-sasanian.md:19,110,112`
- `corpus/QUALITY.md` (admission bar: provenance / calibration / coupling / usability / canon hygiene)
- `corpus/README.md:169-188` (the `## culture-material/ (18)` section the entry's row will join)
- `tools/gates/provenance-audit.py:9-14,75-76,99-104` (field profile and finding ids used in §4/§5)
- `reports/round-34/handoff/declared-in-r7/twin.json`, `reports/round-34/handoff/declared-in-r7/expected.json` (read-set membership, §6)
- `reports/round-30/handoff/declared-in-r6/twin.json`, `reports/round-30/handoff/declared-in-r6/expected.json` (cross-check of §6)
- `reports/round-10/coverage/C06.md` (fragment-format precedent for an author seat in a coverage wave)

Commands run (all from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done   → 21/19/18/29/20/94
grep -ril -e hearth -e rushlight -e tallow -e beeswax -e "lamp oil" -e fire-making -e firelight corpus/knowledge/culture-material/   → 3 files (incidental)
grep -ril -e ignition -e tinder -e candlestick -e lamplighter -e curfew -e "fire mark" corpus/knowledge/culture-material/            → no matches
python3 -B tools/gates/provenance-audit.py .scratch/c06/fire-fuel-light.md    → findings=0 blocked=0, exit 0
python3 -B (couples/path/path:line/§-ref/table/slug/shingle/bleed checks)    → see §4 table
python3 -B (frontmatter field-presence census over corpus/knowledge/*/*.md)  → §5 numbers
python3 -B (regex over the r7 and r6 packet manifests)                       → §6 read-set
git log --oneline -3                                                         → 4a7aede (baseline), da68a6d, 139e3b6; `git status --porcelain` → only `?? reports/round-35/`
```

Draft location: the entry bytes were drafted at `.scratch/c06/fire-fuel-light.md` (scratch, per the mandated TMPDIR convention), gate-checked there, and embedded above as the round's artifact; no file outside `reports/round-35/cov/C06-entry-6.md` and `.scratch/` was written by this seat.
