# Monsters and hybrid beings — the monster as a cultural category: what a culture names a monster, how its body is composed, where it lives on the world's map, who records it, and what it is for

- topic: monsters and hybrid beings as a cultural category: what a culture names a monster, composite anatomy, where monsters live on the world's map, bestiaries and wonder catalogues, the monster as omen, guardian or moral, and restricted beings, as a worldbuilding method
- gap filled: at the claim base no file under `corpus/knowledge` owns monsters as a category. Filename sweep `git ls-tree -r --name-only <base> corpus/knowledge | grep -ciE 'monster|bestiar|hybrid|yokai|creature'` → 0; passing mentions: `grep -ril monster corpus/knowledge` → 10 files, `grep -ril bestiar corpus/knowledge` → 7 files. The build-wave critic found further partial owners that the word sweep misses (composite-being rows in civilization entries, the anomaly engine in `myth-symbol/purity-pollution-boundary-systems.md`, the hundred-year rule in `culture-material/craft-artisan-lexicon.md`); §2 points to the nearest ones one-way. This entry owns the classification: the act of naming a being a monster, and the record a culture keeps of it.
- sources:
  - In-corpus anchors (`corpus/knowledge/`-relative `path:line`, re-read at the lane worktree on 2026-10-22): see the §2 table and §10.
  - External shelf — opened this round (2026-10-22) by ordinary means only (plain requests, public copies and Wayback captures; a challenge met was not passed), registered in `corpus/SOURCES.md` as this round's new rows (S285 and above), each row carrying its URL, access date, tier scope, anchor and located quotes. Each sentence below cites its row and locator.
- couples: myth-symbol — `animal-symbolism.md` (owns the animal register and its composite fauna; this entry owns the act of classing a being as monstrous), `divination-omen-systems.md` (owns omen reading; this entry owns which beings a culture reads as signs), `hero-journey-variants.md` (owns the slayer plot), `cosmology-cosmography.md` (owns the world model), `purity-pollution-boundary-systems.md` (owns pollution); linguistics — `naming-systems.md` and `semantic-fields-lexicon-building.md` (own naming and field building; this entry owns the monster word, §1); synthesis — `worldbible-integration-contract.md` (owns the handoff format, §11); verification — `real-world-inspiration-boundaries.md` (owns the restricted-material prohibition, §10)
- source: lane-side authority is the in-corpus anchor list in §2 plus the external rows opened this round and registered in `corpus/SOURCES.md`. Design method: decide what the word for the being asserts first, then how its body departs from the known, then where it is placed, then who records it and in what book, then what it is for.
- verified-at: 2026-10-22 — written against the lane worktree at the round-55 claim base `f4015e7` (declaration `8eda954`); pre-entry `find corpus/knowledge -type f | wc -l` → **230**; post-entry count **231**, measured at landing by `python3 -B reports/round-55/accept-c.py`.
- recheck: see §15.
- scope: reference method and lane policy for the myth-symbol partition: monsters and hybrid beings as a cultural category. Restricted beings are treated only through the holding community's own public statements (§10); this entry gives no anatomy, ceremony or procedure for them. It decides nothing about what exists in any world; canon stays with lore-shokunin (§11).

## 1. What the word asserts

Decide the culture's word before the creature. The opened lexicons and texts show that a monster word usually names a function — a sign, a verdict, a force — and only later a body.

- **A sign first.** Greek *τέρας* names a divine sign or wonder first; the creature sense (the Gorgon's head, Typhoeus, Cerberus, the Sphinx) is a concrete use of it, a further sense covers monstrous birth, and the plural also names incredible statements (S285, senses I, II, II.2, III). Latin *monstrum* begins as a divine omen of misfortune; Lewis and Short derive it from *moneo* and quote Festus that it is so called because it warns of something future, and the transferred sense covers persons, the sea, the Trojan horse and the ship Argo (S286, senses I, II.A, II.B).
- **Two derivations, not one.** Cicero pairs the four omen nouns with four verbs of showing — *ostendunt, portendunt, monstrant, praedicunt* → *ostenta, portenta, monstra, prodigia* — so his *monstra* are things that point out, not things that warn (S287, 1.93). A standard English rendering of the passage gives "manifestations", "portents", "intimations" and "prodigies", and the word "monster" never appears (S288, 1.93). Isidore derives all four words from foretelling (S289, XI.3 §2).
- **A category defined by negation.** Hesiod's category word is *πέλωρον*, applied to Echidna as a whole and to her snake half, and her nature is "οὐδὲν ἐοικὸς" to mortals or gods (S290, lines 295–299).
- **A verdict and a measure of force at once.** Old English *aglǽca* is glossed "wretch, miscreant, monster, fierce combatant", with *monstrum* and *bellator immanis* as its Latin pair, and the lemma's etymology runs back to a noun of misery and torment (S291, lemma ag-lǽca). The same word is used of the dragon fight in which Beowulf is one of the pair, and a separate noun, *aglǽc-wíf*, names Grendel's mother (S292, lemmata ag-lǽc-wíf, ag-lǽcea).
- **A road danger.** Lane's *ghūl* is a being that appears to men in the desert, assumes various forms and leads travellers from the way; the entry records that the Prophet denied this account, and that some read the denial as rejecting the shape-changing rather than the existence of such beings (S293, p. 2311).
- **A range wider than "monster".** Te Aka glosses *taniwha* as water spirit, monster, dangerous water creature, powerful creature, chief, powerful leader, something or someone awesome (S294, taniwha, sense 1). Nichibunken quotes Komatsu describing *yōkai* as ambiguous and dividing the term into three domains: incidents or phenomena, supernatural entities or presences, and depictions (S295, What is Yōkai Culture?). Wengrow drops "monsters" for "composites" because the older word carries connotations he finds unwarranted (S296, p. 154).

Rule: give each culture its own monster word with its senses in order, and let the English gloss follow. A world that translates every such word as "monster" has already made a moral claim (S292, lemma ag-lǽc-wíf).

## 2. One-owner boundary

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `myth-symbol/animal-symbolism.md:89` | Engineered composite fauna within the animal and heraldic register | Own the act of classing a being as monstrous; do not repeat its composite-beast list |
| `myth-symbol/symbolism-synthesis-method.md:24` | Registers, base partitions, alignment matrices and era tables | Use that grammar; build no competing register for creatures |
| `myth-symbol/trickster.md:13` | The institutional slot of a licensed boundary-crosser | A monster designation need not imply a trickster |
| `myth-symbol/hero-journey-variants.md:82` | Functions of dragon combat | Describe the adversary's classification and form, not another slayer plot |
| `myth-symbol/cosmology-cosmography.md:29` | World centre, layers, directional code | Locate attributed beings within a world model; do not redraw it |
| `myth-symbol/sacred-topography-pilgrimage.md:17,81-93` | Holy places, journeys, custody and access | Record a being's reported dwelling or guardianship; shrine institutions stay there |
| `myth-symbol/divination-omen-systems.md:86` | Omen compendia, sign spaces and scribal readers | Record when a being is treated as a sign; do not duplicate the reading apparatus |
| `myth-symbol/motif-index-usage.md:91` | The index as a finding aid | Use motif numbers for retrieval only (§7) |
| `myth-symbol/eschatology-world-end-systems.md:60` | World-ending agents and sequence | The creature's category belongs here; its world-ending role stays there |
| `myth-symbol/purity-pollution-boundary-systems.md:16` | Pollution as a culture's boundary map | Do not equate hybridity with impurity |
| `culture-material/masks-masquerade.md:18` | Concealment versus transformation in masking | A represented being is not its worn portrayal |
| `verification/real-world-inspiration-boundaries.md:97` | The prohibition on reproducing restricted material | Point to the public boundary; supply no clearance (§10) |

## 3. Sign before body: the monster as omen

- **A state record, not a beast.** Livy's notice of one winter's prodigies allows either that they happened or that, once minds were stirred to religion, many were reported and lightly believed; it lists them at named places — Rome's markets, Lanuvium, Amiternum, Picenum, Caere, Gaul — sends the decemvirs to the books and closes with rites said to have relieved the city's fear (S297, 21.62.1–11). The notice lists an ox climbing to a third storey and the appearance of ships in the sky among the prodigies: a category violation, not a sewn body (S297, 21.62.2–5).
- **Against known nature.** Isidore denies that portents are against nature and says they are against the nature that is known, so a culture's knowledge sets the edge of the monstrous (S289, XI.3 §1–§2). He reads a birth with a dead human upper half and a living beast lower half as a sign of a king's murder (S289, XI.3 §5).
- **Two words against each other.** Paré calls monsters things that appear against the course of nature and usually signs of some misfortune to come, and lists thirteen causes of monsters, from the glory and wrath of God through seed, imagination, the womb, a blow, heredity and mixed seed to beggars' fraud and demons (S298, book II, opening definition and ch. I). A 2014 study groups Paré's causes by divine, physiological, imaginary and demonic explanations, and places this scheme in a cultural and ideological transition (S299, pp. 118–124).
- **A sign in a modern catalogue.** In its Glossary, Nichibunken says that in premodern Japan "anomalies" occurred because of cosmic unbalance or societal disorder and were considered omens, warnings, or punishment (S295, Glossary 怪異).

Decide for each being whether it is read, expiated or fought, and who is licensed to read it: Cicero names the Etruscans the most practised interpreters (S287, 1.93).

## 4. Composite anatomy

The opened records build bodies in a few repeatable ways. Name the method before the parts.

- **Ratio.** Echidna is "half a nymph … and half again a huge snake" (S300, lines 300–303).
- **Slots.** The Chimera is built by position — lion in front, serpent behind, goat in the middle (S290, line 323). The British Museum's Hunefer record quotes the inscription beside Ammit: "Her front is a crocodile, her rear a hippopotamus, her middle a lion" (S301, Curator's comments, ¶2); the Ani record's Description gives the same three animals in a different arrangement and never names the monster (S302, Description; the record's Associated names field indexes "Representation of: Ammit").
- **Donor list.** The Aberdeen Bestiary's leocrota is an ass in size with a stag's hindquarters, a lion's chest and legs and a continuous jaw for teeth (S303, commentary, Illustration). The Met's curator lists Pazuzu's clawed human arms, two pairs of wings, scorpion's tail and snarling canine mouth (S304, § "The exception seems to be Pazuzu").
- **One diagnostic joint.** The Florentine Codex's ahuitzotl is a dog-sized, short-furred water animal whose tail ends in "a hand, like a person's hand" (S305, fol. 70v), while Molina's 1571 dictionary glosses *auitzotl* only as a little water animal like a small dog (S306, leaf 279). Keep the dictionary register and the narrated register apart.
- **Edited familiar animal.** The *Shanhaijing* names a sheep with nine tails, four ears and eyes on its back (S307, juan 1, 基山).
- **Accretion.** Te Ara records Tūtaeporoporo, the taniwha of the Whanganui River, beginning as a shark and taking on spiky skin, bat-like wings, a lizard-like tail, webbed feet and hawk-like claws while keeping shark's teeth (S308, Sharks — Tūtaeporoporo).
- **Classes of departure.** Isidore sorts monstrous bodies into whole-body size, excess or defect of parts, parts cut away, parts transformed, and mixture of kind (S289, XI.3 §7–§11).

Wengrow defines composites as images combining incongruous elements of human or animal anatomy, finds them rarer in early art than accounts suggest, and ties their first wide visibility to the transition to urban life in the Near East (S296, pp. 154–160); his book frames the experiment as isolating the features of diverse species and recombining them (S309, Introduction, p. 1). Wengrow says sealing practices allowed complex, counter-intuitive images to be transmitted faithfully, while access to seal production gave specialised groups control over what was disseminated (S296, pp. 160–161).

## 5. Where monsters live: rims, routes, doors and water

- **The rim.** Herodotus places the one-eyed Arimaspians beyond the Issedones and the gold-guarding griffins beyond them (S310, 4.13), and reasons that the outermost lands are likely to hold what people think finest and rarest (S310, 3.116.3). Pliny files monstrous peoples as nations at the world's edges — the Astomi at "the very extremity of India" (S311, Book 7, ch. 2). The British Library's account of the *Marvels of the East* calls distance — beyond the borders of the known world — the one trait on which belief agreed (S312, ¶ "Belief in the existence of monstrous races").
- **A coordinate on the map.** The Hereford Mappa Mundi's official guide places a Blemmye with spear and shield in Africa and Sciapods in India and at the extreme southern edge of the inhabited world, and shows Alexander's wall restraining the Sons of Cain (S313, Strange Peoples of the World; Camp of Alexander the Great). The cathedral counts 33 plants, animals, birds and strange creatures in one number and 32 peoples in another (S314, drawings paragraph), so decide whether a hybrid is filed with fauna or with nations.
- **The route.** The *Shanhaijing* fixes each being to one mountain along a route, each mountain at a stated distance from the last, and closes each route with the spirit that governs it and the sacrifice owed (S307, juan 1, route summary). A 1995 study reads the book's creatures as inseparable from the divine powers holding each stretch of land (S315, pp. 59, 86). Al-Qazwīnī's illustrated copies index beings by named town and sea and include a world map; in one painting divers in the Sea of ʿUmān save themselves by feeding the fish and monsters (S316, fols. 44b, 52b).
- **The door.** The British Museum calls its Nimrud human-headed winged bull a protective spirit that guarded the entrance to what may have been the king's private apartments, with its pair now in New York (S317, Curator's comments). The unnamed monster sits on a mat behind Thoth in the Hall of Judgment (S302, Description); in the Hunefer record Ammit crouches below the balance (S301, Curator's comments, ¶2).
- **Water people already avoid.** Te Ara gives *rua taniwha* as deep pools, caves or dangerous waterways (S308, A creature of many forms); the ahuitzotl "lives in deep water springs" (S305, fol. 70v).
- **The world-ocean.** Snorri's gods cast the serpent "into the deep sea, where he lies about all the land" (S318, Gylfaginning ch. XXXIV).

## 6. Kin and lineage

- **A family register.** Hesiod's passage opens as a birth notice and ends with a colophon, "This is the offspring of Ceto and Phorcys"; slayers appear within the list — Heracles at 315–318 and 329–332, Bellerophon at 325 — and the passage closes with the snake at the earth's great bounds and the colophon (S300, lines 270–274, 315–332, 335–336). One link is marked as hearsay with *φασι* (S290, line 306).
- **One ancestor, many kinds.** *Beowulf* derives Grendel from the kin of Cain, and from Cain all the misbegotten kinds — *eotenas*, *ylfe*, *orcnêas*, *gigantas* (S319, lines 107–113).
- **A brood with separate addresses.** Snorri gives Loki's three children by one giantess three places — the wolf among the gods, the serpent in the sea, Hel in Niflheim — and the gods keep the wolf bound rather than stain their sanctuary with his blood (S318, Gylfaginning ch. XXXIV). In the *Poetic Edda* the brood is bred in Ironwood in the east, a place-name Bellows calls a conjectural emendation (S320, Völuspá 40; note to Grimnismol 39).

## 7. Who records the being, and in what book

The kind of book decides what a monster is for. Name it.

- **Moralised beast book.** The Aberdeen project says accurate and fabulous accounts carry the same weight in a bestiary, that it was never meant as a scientific text, and that its pictures were justified as a didactic tool (S321, What is a Bestiary?). The British Library quotes Elizabeth Morrison that the bestiary was not a single text but a series of changeable texts (S322, Function and origins, ¶2). The Getty shows a bestiary opening titled "Legendary Peoples" and creatures that "escaped" onto objects such as a lion aquamanile (S323, exhibition page; checklist).
- **Natural history.** Pliny calls his monstrous peoples nature's sport for herself and miracles for us, and hands the credit to named authorities (S324, VII §8, §32). Gellius buys cheap, filthy Greek wonder-books at Brundisium, notes some remarkable items from them, including monstrous peoples, and calls the writings worthless (S325, 9.4.3–5, 9.4.6–12).
- **Wonder literature.** Von Hees argues that *ʿajāʾib* names themes that evoke astonishment and mostly real phenomena, that marvel-beasts are marginal, and that the genre of "literature of marvels" does not exist as previously conceptualized (S326, pp. 102, 104–105). The Library of Congress record says al-Qazwīnī ends his work with a section on monsters and angels (S327, Summary).
- **Encyclopedia.** The Florentine Codex's Book XI includes the ahuitzotl passage (S305, fol. 70v), and the Library of Congress describes Book XI as a treatise on natural history whose discussion of animals draws on legends of real and mythical animals (S328, Summary).
- **Miscellany.** The *Marvels of the East* runs ff. 98v–106v of the Beowulf manuscript, between a homily and the Letter of Alexander (S329, Contents); its working entry is four facts — name, where found, appearance, diet (S312, ¶ "The text of the Marvels begins without preface").
- **Folklore database.** Nichibunken generally copies each designation from the pasted case, with stated exceptions, and card creators do not name beings as a rule; its representative-name search treats カッパ/ガッパ as the same for search but excludes カワタロウ/エンコ from カッパ results (S330, 凡例; 利用). Its Key Features section gives one example record, a three-legged fox in Kurosawa (S295, Key Features).
- **Picture book.** The National Diet Library records Sekien's 1776 *Gazu hyakki yagyō* as three small volumes in parts labelled 隂, 陽 and 風, with an alternative title (S331, 一般注記).
- **Motif index.** Thompson files mythical animals at B0–B99 and animals with human traits at B200–B299; B10–B90 list distinct subdivisions, from mythical beasts and hybrids through beast-men, bird-beasts, bird-men, fish-beasts and fish-men to other mythical animals, and the B0 entry cross-references guardian beasts of the four quarters at A417.1 (S332, General Synopsis; B0). His G chapter makes malevolence, not size, the mark of an ogre (S333, G100). Use these numbers to retrieve, never to define (`myth-symbol/motif-index-usage.md:91`).

## 8. What the being is for

- **Guardian by terror.** The Met says Pazuzu was frequently set up as a shield against Lamashtu, and that such beings appear largely amoral, open to appeasement with offerings and incantations (S304, § "To answer this question").
- **Verdict.** Ammit waits to consume the heart only if the dead man fails the weighing, while Thoth records the outcome and the dead man speaks spell 30B to his heart (S302, Description; S301, Curator's comments, ¶2).
- **Executioner.** Grendel comes from the moor bearing God's wrath (S319, lines 711–712).
- **Moral lesson.** The Aberdeen hyena is unclean because it is sometimes male and sometimes female; it also haunts tombs and imitates a voice to lure a man out, and the chapter closes with a scriptural identification; the project's modern commentary adds that it should not be eaten (S334, Of the hyena; Illustration).
- **Rain and rank.** The Cleveland Museum's Joseon jar record calls the dragon a creature believed to make rain, then a symbol of rulers whose image was used only for the king's paraphernalia (S335, description; did_you_know). On a Qing emperor's robe the five-clawed dragon is one of the Twelve Imperial Symbols of Sovereignty, under a colour rule (S336, Summary; Physical description). The Aberdeen dragon is instead born in Ethiopia and India and read as the Devil (S337, Of the dragon).
- **Guardian and man-eater in one class.** Te Ara records that in some traditions taniwha captured and ate people while others were *kaitiaki*, protectors of iwi and hapū, given karakia and offerings (S338, A creature of many forms).
- **Danger and use in one entry.** The *Shanhaijing*'s nine-tailed fox eats people while its flesh protects the eater (S307, juan 1, 青丘之山).
- **Place spirit, not monster.** Vinogradova's Polesye survey files leshy, vodyanoy and polevik as spirits of natural loci but finds them carried by scant, isolated evidence (S339, pp. 182, 193); the belief that a domovik must live in every house for the household to prosper is recorded mainly in Russian villages on Polesye's eastern edge, while in the west his presence is judged both harmful and useful (S339, pp. 182–183). Rusalki are the unquiet dead of improper burial, almost always believed to appear in Rusalia Week (S340, pp. 83–84). Filing these under "monster" loses the locus and the death that define them.
- **Fortune and the market.** The Smithsonian reads Mami Wata as "Mother Water" in a trade pidgin, a "capitalist" deity who can bring money, and part of an uncountable "school" of water spirits (S341, Introduction page).

## 9. Period drift

A monster is a dated record, not a species. Date every layer.

- **Imported images recompose an old being.** The Fowler, calling her wellsprings conjectural, dates layers of Mami Wata's look to Euro-African contact — a fifteenth-century medallion an African carver made from a Portuguese client's mermaid image, a circa-1887 Hamburg snake-charmer chromolithograph read as a water spirit in the Niger Delta by 1901 — and records her recast as a demon in Ghanaian film (S342, Sources and Currents, ¶2, ¶3, ¶6).
- **Literature re-enters custom.** Dynda calls the fish-tailed Russian mermaid for the most part a literary chimera, an image imposed in the nineteenth and twentieth centuries and then recorded as tradition (S340, p. 84 and n. 3).
- **Names travel apart from bodies.** Early griffin-like monsters were not labelled griffins in their own cultures (S343, section "Griffin origins"). Te Ara notes that others call taniwha dragons, since many looked like reptiles, had wings and ate people (S338, A creature of many forms).
- **Catalogues are dated counts.** Nichibunken's file covers the late Edo period to the present and gave 35,257 entries as of November 2023 (S295, Overview); the Walters' 1717 Ottoman Turkish version of al-Qazwīnī has 444 paintings (S344, record description). A later picture book, Kyōsai's, is dated 1890 after a posthumous 1889 first edition (S345, objectDate).
- **Images go out of use.** By Parthian times Pazuzu's image was almost out of use (S304, § "The grand buildings on the screen").

## 10. Restricted beings

Some communities restrict talk about the beings, places and material in their keeping; the statements opened here restrict a place (Uluṟu), a kind of talk (Diné witchery) and classes of material (S350), not a named being. The rule, not the content, is what a world document may take.

- **Publish the rule, withhold the content.** Sammy Wilson, the Aṉangu chair of the Uluṟu-Kata Tjuṯa board, writes that Aṉangu declared the climb closed, that it is a sacred place restricted by law, and that this is as much as can be said (S346, PDF p. 3, English translation). That is the ceiling: state that a restriction exists, who holds it and its scope, and stop.
- **Circulation norms have speakers.** Jennifer Denetdale, a Diné historian quoted in the *Navajo Times*, says "We don't talk about witchery" and places such conversations in the intimate circle (S347, § "Tourist gaze"). Record the norm with its speaker; never the content.
- **Place-tied beings enter ordinary law through their holders.** The park page calls the closure decision Tjukurpa and Australian law working together in joint management (S348, climb-closure page). Te Ara reports that in 2002 the Ngāti Naho hapū in Waikato objected that a highway would destroy the lair of their taniwha Karutahi and that Transit New Zealand eventually agreed to partially reroute it; that a Northland prison was built against objections over the taniwha Takauere; and that Māori disagreed over whether such concerns were genuine (S308, Taniwha today). Te Ara is reporting here; write these positions at that strength.
- **Do not launder outsider horror.** A 2020 student-journal study argues that horror literature strips the windigo of the Algonquian traditions that hold it, among them the Cree and the Ojibwe, and commodifies it, and that researchers built the "Windigo Psychosis" category from stories that do not match recorded cases (S349, pp. 101, 103, 104, 109). Flag such forms as pop-mythography on first use.
- **Custodian authority.** An Australian national arts protocol guide calls traditional motifs part of the cultural heritage of certain Indigenous groups, possibly unsuitable for mass dissemination and needing custodians' permission for each use (S350, printed p. 44), and says that wide circulation of sacred or secret material, or of works with gender restrictions, is not acceptable in Indigenous communities (S350, printed p. 47). A world document seeks no such permission; it designs an original being.
- **In-corpus policies.** The Haudenosaunee medicine-mask boundary is at `civilizations/haudenosaunee.md:132-141`, and the masks entry's access rules at `culture-material/masks-masquerade.md:55,69`; the access ledger column set (`feature | source/community/date | language/form/category | public/restricted/unknown | linked material or narrative practice | invention boundary | unresolved check`) is at `civilizations/algonquian.md:189`, and unknown access stays unknown, not "open" (`civilizations/algonquian.md:196`). Use that ledger; do not invent a second one. Copying a local ancestral being into a fantasy bestiary is ruled out at `civilizations/australia-aboriginal.md:45`; Diné public accessibility is not permission (`civilizations/dine-navajo.md:15`) and no altered-detail recipe is offered (`civilizations/dine-navajo.md:95`); kaitiakitanga is a relationship of care and authority (`civilizations/maori.md:111`).
- **Worked ledger row.** `Karutahi | Te Ara (S308), Ngāti Naho hapū, Waikato, 2002 | taniwha; lair-tied | unknown (no hapū statement opened) | highway-route objection | no body, lair or name reuse; design an original being | the hapū's own account`

Never design a real restricted being under a changed name; design an original being instead.

## 11. Handoff to lore

Lore-shokunin owns entity records and identity, approved names and places, chronology, canon decisions and bible-wide consistency (`synthesis/worldbible-integration-contract.md:17,42`; `lore-shokunin/PROVINCE.md:3,9,28`, fleet-relative). Its checker admits only `character`, `place`, `faction` and `item` (`lore-shokunin/corpus/fixtures/check_bible.py:7`) and reports any other kind as a violation (`:153-154`); the checker reads only sources, entities, relations, timeline and contradictions (`:25-32,43-45`), so lore has no bestiary or creature section, so whether a being enters as a `character`, as a claim on a `place`, or not at all is lore's decision. A being's existence travels by default as an attributed in-world belief, not a world-fact (`synthesis/worldbible-integration-contract.md:43,103`). Kotodama may propose dossiers as myth-symbol register payloads (`synthesis/worldbible-integration-contract.md:80`), each with a namespaced candidate ID, its scope (culture, region, language variety, period) and, per field, a claim kind and an evidence status, attested or invented (`:60-63,96-97`), carrying these fields:

| Field | Content | From |
|---|---|---|
| native name and gloss | original form, transliteration, literal gloss; aliases apart from identity | §1 |
| category word | who calls the being what, with local sense; "monster" is attributed, never a lore `kind` | §1 |
| body rule | method (ratio, slots, donor list, diagnostic joint, edited familiar animal, accretion, departure class) and parts | §4 |
| placement | rim, route, door or water; teller and source | §5 |
| lineage | parent, sibling or brood links between candidate IDs, each with its teller; a relation, not an identity | §6 |
| function | sign, guardian, verdict, lesson, place spirit; scoped to its telling | §3, §8 |
| source genre | book or object type, edition, locator; real-world references go to lore's reference ledger, not to the bible (`lore-shokunin/corpus/knowledge/reference-ledger.md:3,10-12`) | §7 |
| period layers | dated variants of name, body, place and role | §9 |
| access status | public / restricted / unknown, holder of authority | §10 |

Each dossier stays an unbound research packet and NON-CANON: binding needs lore's baseline bible reference and receipt surface (`synthesis/worldbible-integration-contract.md:58,69,126`), and canon needs a lore receipt that names approved bible IDs and the resulting bible revision (`:132`). Lore has not acknowledged this contract (`:15`) and lists kotodama packet intake as uncovered (`lore-shokunin/PROVINCE.md:19,28`); this section sends nothing.

## 12. Decision table and build order

| ID | Decision | Trigger | Failure if skipped |
|---|---|---|---|
| DR-MON-01 | Fix the monster word and its senses in order | any new being | the English gloss imports a moral verdict (§1) |
| DR-MON-02 | Sign, beast or both | the being appears in a record | omen beings get fought, beasts get expiated (§3) |
| DR-MON-03 | Name the body method | a composite body | an unreadable grotesque with no rule (§4) |
| DR-MON-04 | Rim, route, door or water | placement | a monster with no address on the culture's map (§5) |
| DR-MON-05 | Lineage or no lineage | more than one being | an unrelated menagerie (§6) |
| DR-MON-06 | The kind of book and its stance | any catalogue | every entry reads as zoology (§7) |
| DR-MON-07 | What the being is for | function | "monster" collapses into "evil" (§8) |
| DR-MON-08 | Date each layer | drift across periods | a timeless creature with no history (§9) |
| DR-MON-09 | Access status and holder | a real-world analogue exists | restricted material reproduced (§10) |

Build order: DR-MON-01 → 02 → 03 → 04 → 06 → 07, then 05, 08 and 09; then the dossier (§11).

## 13. NON-CANON worked micro-example

**NON-CANON** — illustration only; decides nothing in any world. A river people call any being met at a ford *tekh*, a word that also means "a stone set to mark a boundary". Their *tekh* are recorded only in the ferry-keepers' tally book, one line each: name as heard, which ford, what it took, which year. One *tekh* is a heron with a drowned man's hands; its line says "seen by the ferry-keeper's daughter, not by me". The tally book lists no cure; the ferry-keeper's office is to post a stone. Every element maps to an attested option above and copies no single tradition.

## 14. Calibration bank

Codes as in `../verification/calibration-registry.md:35-39`.

- **R — "every culture has dragons."** "Dragon" is a cover term for serpent- or lizard-like beings that some traditions treat as evil and others as beneficent (S351, article body, ¶1); Te Ara notes that others call taniwha dragons (S338, A creature of many forms). The count comes from the English label.
- **C — "griffins came from *Protoceratops* fossils."** Princeton presents Mayor's thesis that the legend sprang from tales told by Scythian gold-miners (S352, publisher's description, ¶2); Witton and Hing (2024) find the link uncompelling and call it an "ex post facto geomyth" (S343, Abstract). The published evaluation weighs against the thesis; do not state it as the griffin's origin.
- **B, as Latin word history only — "monster comes from *monere*, to warn."** Lewis and Short head *monstrum* with *moneo* and quote Festus that it is so called because it warns of something future (S286, sense I); Cicero instead ties *monstra* to *monstrant* (S287, 1.93). State both, each attributed; never use either to define what a taniwha, *yōkai* or *long* is. `myth-symbol/divination-omen-systems.md:72` carries the round-55 erratum.
- **C — "medieval people believed the monstrous races were real."** Augustine says Christians are not bound to believe all that is reported of them (S353, XVI.8, ¶1); Isidore asserts some races and calls other portents fictions to be interpreted (S289, XI.3 §28). Attribute belief author by author.
- **R for "unchanged" — "*yōkai* are ancient and unchanged."** Nichibunken's lead scholar calls *yōkai* an ambiguous term, and the database documents accounts from the late Edo period to the present (S295, What is Yōkai Culture?; Development of the Database). The word has an older record, so do not call it a modern invention either.
- **R as zoology — cryptids.** A faculty-refereed undergraduate paper separates hidden animals from frankly supernatural beings in cryptozoology's own literature and leaves the field "at best, a transitional field of research" (S354, printed pp. 8, 10); Columbia University Press describes Loxton and Prothero's book as testing science against pseudoscience in cryptozoology (S355, description). Present a cryptid as a modern legend with tellers, media and dates, never as a species.
- **R — "monster means evil."** Oni are not necessarily evil and can become kami if worshipped (S295, Glossary 鬼); some taniwha are protectors (S338, A creature of many forms); the Met's curator writes that such beings "seem to be presented as largely amoral", and Pazuzu served as a shield against Lamashtu (S304, § beginning "To answer this question").
- **H — Cohen's theses.** Cohen's "Monster Culture (Seven Theses)" is a heuristic set — the monster's body as a readable sign, the mixed category that resists classification, the border patrol at the edge of the official map (S356, Theses I, III, V) — not ethnography. A 2020 comment introducing an interdisciplinary collection names the field's working premises (S357, Introduction). Campbell and the Jungian "shadow" are flagged in `../verification/calibration-registry.md` and `myth-ritual-theories.md`.

## 15. Recheck

Re-run the two gap sweeps in the head before adding monster material elsewhere; re-open every cited row before repeating a number from it; re-read each §2 anchor before redrawing a seam; never add a restricted being's detail from a museum or encyclopedia record.

## 16. Scope

Monsters and hybrid beings as a cultural category in the myth-symbol partition. Single-tradition dossiers stay with their civilization entries; animal registers, omen reading, slayer plots, world models and pollution stay with their owners (§2). NON-CANON throughout.
