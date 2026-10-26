# Toponymy: how place names are built, layered, governed, renamed and rendered — a design system for worldbuilders

- topic: place names (toponyms) as a linguistic-cultural design system: what a place name is built from (generic and specific elements, feature words, suffix position), how names stratify by language layer and survive the languages that coined them, why river-names are treated as the deepest layer and how far that holds, endonyms, half-translations and outsider respellings, who standardises names and by which principles (local usage, Indigenous-first priority, duplicate avoidance, settlement-locked names, derogatory-name removal, heritage criteria), renaming as politics and as restoration, romanization by donor-country proposal, street names under council policy, and folk etymology kept at its measured rarity.
- gap filled: at the claim base no file under `corpus/knowledge` is named for toponymy (`git ls-tree -r --name-only 80f48c2c corpus/knowledge | grep -ciE 'topon|place-?name|placename|onomast'` → 0). The overview owner is `naming-systems.md` §3 (functions, strata, politics: seven lines) and §5 (endonym/exonym); this entry owns the place-specific decisions that overview does not make (element grammar, naming-authority principles, renaming operations, romanization procedure, street naming, folk-etymology calibration) and repeats none of its examples as new.
- sources:
  - External shelf: rows opened this round (2026-10-23) by ordinary means (plain requests to official, institutional and open-access pages), registered in `corpus/SOURCES.md` in claim C's reserved block (round 58) with a located anchor quote each. Every factual sentence below cites its row; uncited lines are this entry's own design method.
  - In-corpus anchors: the §2 boundary table (pointers only, no row cited there).
- couples: linguistics — `naming-systems.md` (name-system overview, §3 toponymy, §5 endonym/exonym), `historical-linguistics.md` (comparative method for strata), `language-contact.md` (contact outcomes), `language-shift-obsolescence-revival.md` (reclaimed names); synthesis — `naming-canon-workflow.md` (name records, proposal envelope); myth-symbol — `sacred-topography-pilgrimage.md` (sacred sites and routes); culture-material — `architecture-settlement-lexicon.md`, `agrarian-field-system-lexicon.md`.
- source: lane-side authority is the external rows plus the §2 pointer list. Design method: fix the place and its users first (§3), build the name from elements (§4), assign its layer (§5-§6), then choose who governs it (§7), how it may change (§8) and how it is written for outsiders (§9).
- verified-at: 2026-10-23 — written against claim base `80f48c2c`; pre-entry `find corpus/knowledge -type f | wc -l` → 233; post-entry 234.
- recheck: see §14.
- scope: reference method for the linguistics partition. It describes real naming practice so a worldbuilder can design a fictional system; it decides no world's names (lore-shokunin owns the names recorded on landed entities, §13). Living communities' names are described only through the naming authorities and scholars that publish them.

## 1. Calibration key

These are this entry's own reading labels: **B** carried by the cited row at its stated strength; **H** the row itself hedges it ("postulated", "often", "usually"); **D** design method of this entry, not a historical finding. A sentence without a row id is **D**.

## 2. One-owner boundary

| Neighbour | What it owns | This entry's boundary |
|---|---|---|
| `linguistics/naming-systems.md` §3, §5 | overview of place-name functions, strata, critical toponymy, endonym/exonym definitions and craft rules | points there for the overview; owns the decisions below and does not re-teach its examples |
| `linguistics/historical-linguistics.md` | comparative method, sound laws, relative chronology | uses that method for name strata (§5); no second method |
| `linguistics/language-contact.md` | borrowing, calque and substrate outcomes | applies them to names only |
| `synthesis/naming-canon-workflow.md` | name records, meaning versus evidence ledger, proposal envelope to lore | place proposals travel in that envelope (§13); no second ledger |
| `myth-symbol/sacred-topography-pilgrimage.md` | sacred sites, routes and their institutions | owns the naming of places, not the cult of them |
| `culture-material/architecture-settlement-lexicon.md`, `agrarian-field-system-lexicon.md` | settlement and field vocabularies | supplies the naming rules those vocabularies feed |

## 3. Fix the place, its users and the authority before the name

| Question | Decision | Record |
|---|---|---|
| Which feature? | a settlement, river, mountain, lake, street, field or district | feature class and extent; a settlement named from a river is a second place |
| Who speaks of it? | every language community that names it | one name record per community and era |
| Who governs the written form? | none, a local council, a national board, a settlement agreement | the rule the authority applies (§7) |
| Who reads it from outside? | neighbours, mapmakers, foreign states | the outsider form and how it was made (§6, §9) |

## 4. Element grammar: what a place name is built from

- The UN naming glossary defines the specific element of a toponym as the part that is not the generic term and that distinguishes it from others of the same feature class (S500). Design rule: give every name a generic (the feature word) and a specific (the distinguisher), and decide which comes first.
- The Institute for Name-Studies describes place-name elements as the words names are built from, and says these elements reflect the rich diversity of England's linguistic history (S514). Design rule: each element of a name belongs to a language layer, so a map's element inventory is its linguistic history.
- English village and town names frequently refer to particular people, social and administrative activities, landscape, birds and animals, crops and vegetation (S515). Use these five motive families as the specific-element menu for an agrarian landscape.
- Most Japanese geographical names are written in kanji, and the character that expresses the geographical feature is usually added to the end of the name (S531). Generic position is a language-level rule: Japanese names put the feature word last.
- Two early Celtic river-names, Don and Ness, are combined with words for a river-mouth in the city names Aberdeen and Inverness (S519). A settlement name can wrap an older river-name inside a newer generic element.
- In Welsh lake names the generic llyn is commonly omitted at the beginning of other lake names that already contain it, such as Glaslyn and Gloywlyn (S523). Decide whether your language drops a generic that the name already carries.

| Construction | Real pattern (row) | Fictional use |
|---|---|---|
| specific + feature word last | Japanese kanji feature character at the end of the name (S531) | fix one generic position per language |
| river-name + newer generic | Don and Ness inside Aberdeen and Inverness (S519) | a city name that keeps a lost river word |
| generic dropped when repeated | llyn omitted before lake names containing it (S523) | a standardiser's spelling rule |

## 5. Layers: names outlive the languages that coined them

- In many cases geographical names are the only surviving elements of extinct languages, the UN standardization manual states (S502). A worldbuilder can let a vanished people survive only as place names.
- Name scholars postulate Old European origins for names, above all river-names, that recur widely within the Indo-European world (S518, H: "postulated"). Treat the deepest river-names as a hypothesis layer, not a proven people.
- A late eleventh-century History of St Cuthbert shows the pre-English river-name Coquet transformed into an English-looking Cocwudu, "cock wood" (S542). An old river-name can be reshaped into a newer language's words rather than replaced.
- In an Irish townland the English name Mountbell is a much later addition to the area's toponymy, a reference to the local Big House (S525). Estate and gentry layers sit on top of older native names.
- Many Canadian place names keep Indigenous heritage only in the form where European settlers tried to transpose the words they were hearing into English or French (S513). A settler layer can hold a native name in a mishearing.
- The Alemanni founded a large number of new settlements with place names ending in -ingen, -ikon, -dorf and -wil (S526). A newcomer layer is recognisable by a small set of settlement endings.
- A study of Slavic-German contact names finds that the processes of historical settlement are reflected in the historical documentation of place names (S529). Read a contact zone's settlement history from its dated name forms, parallel names and hybrids.
- Fellows-Jensen reads numerous Scandinavian place-names in -bý in one district as pointing to the survival of an enclave of Danes there (S516). A dense cluster of one people's settlement ending can mark where that people stayed.
- So-called Grimston- or Toton-hybrids are Anglo-Scandinavian place-names generally held to be an Old Norse personal name plus Old English tūn (S517). A hybrid joins a newcomer's personal name to the older language's generic.

Stratum-reading procedure (D): (1) collect the dated spellings of one place; (2) split each into generic and specific; (3) assign each element to a language layer; (4) test the competing readings — retained, translated, half-translated, reshaped, replaced; (5) keep "unknown" as a valid result.

## 6. Insider names, outsider names and half-translations

- Scotland's Gaelic naming partnership counts as a Gaelic place-name any name used by Gaelic speakers when speaking Gaelic, whatever its linguistic origin (S520). A community's name is defined by who uses it, not by where the word came from.
- An Driseachán is the official name of a County Galway village known in English by the half-translation Brierfield (S524). Design a bilingual map with official native forms and half-translated outsider forms side by side.
- In 2000 the Ordnance Survey recognised that some Gaelic place-names on its maps were incorrect (S521). A national mapping agency can print a minority language's names wrongly, and correcting them needs a standing body.
- Germany's toponymic guidelines say Sorbian geographical names have to be used alongside the German names (S528). A minority-language name can be required next to the majority name on official maps.

## 7. Naming authorities and their principles

- In 1890 the United States Board on Geographic Names was created by executive order of President Benjamin Harrison (S501). A national names board is an act of the state with a founding date.
- The Board on Geographic Names is the federal body tasked with naming geographic places, and in 2021 it was ordered to implement procedures to remove a derogatory term from federal usage (S506).
- The Board then voted on final replacement names for nearly 650 geographic features that carried the term (S507). Derogatory-name removal is a slow, feature-by-feature naming operation, not one decree.
- Canada's Geographical Names Board recognizes the need to prioritize the identification and adoption of Indigenous names when naming or renaming geographical features (S512).
- New Zealand's Geographic Board tested a mountain's name change against its naming criteria, including prioritising the original Māori name and avoiding duplication of place names (S508).
- Once official, a Treaty settlement place name in New Zealand can only be changed with written consent from the trustees of the relevant settlement group (S509). Some names are locked by agreement, not by the naming board alone.
- The US naming board's proposal guidance says that once named, a feature in the Geographic Names Information System can never be "unnamed", only changed to another name (S504). Official names can be replaced but never deleted.
- Northern Territory guidelines prefer Aboriginal names for geographic or topographic features where a place does not have a name that was previously registered (S510).
- Victoria's Aboriginal place-naming guidance says these features are defined differently to western concepts of place, and their Aboriginal names are just as important to preserve (S511). A naming system can carry a different idea of what counts as a place.
- The Welsh place-names standardisation panel gives consideration to the meaning, history and etymology of place-names as well as their current usage (S522).
- A UN naming conference resolution of 2012 recommended criteria to establish and evaluate geographical names as cultural heritage (S503). Heritage status is a judgment an authority makes by criteria.

| Principle | Real authority (row) | Decision it forces in a fictional state |
|---|---|---|
| national board by executive act | US Board on Geographic Names, 1890 (S501) | who founded the board and when |
| Indigenous names first | Geographical Names Board of Canada (S512) | whose names win a tie |
| original native name, no duplicates | New Zealand Geographic Board criteria (S508) | the board's test for a change |
| settlement-locked names | Treaty settlement names, trustee consent (S509) | which names no board can change alone |
| derogatory term removed | Board on Geographic Names, replacement names for ~650 features (S507) | the cost and length of a purge |
| meaning and history weighed with usage | Welsh standardisation panel (S522) | what counts besides usage |
| heritage criteria | UN conference resolution X/3, 2012 (S503) | which names a state protects |

## 8. Renaming: politics, restoration and invention

- Ukraine reported that, as a result of the renaming of settlements, more than 300 historical names have been restored (S538). A purge of regime names can restore an older layer instead of coining new names.
- Ukrainian decommunization legislation provides no strict instructions about the new place-names that should replace the removed ones (S539). A renaming law can say what must go and leave the replacement to local choice.
- The retributive and politicized nature of street renaming has been particularly evident in South African cities (S541). Street renaming after a regime change can act as retribution against the old order.
- The US naming board adopted a policy in the 1960s that it would not consider geographic name issues that were the subject of pending congressional legislation (S505). A legislature can freeze a renaming simply by keeping a bill pending.
- In Japan's Heisei mergers many new municipal names were generated from names of wider areas, natural features or old province names (S530). Merged towns take a neutral, wider or revived name rather than one partner's name.
- Ukraine's 2025 report to the UN names experts says that in 2023-2024 there was a massive renaming of place names of settlements (S536). A renaming wave reaches far below city names, down to the small names of a settlement.
- India's report to the UN names experts says the process of changing geographical names follows a structured procedure to ensure accuracy and standardization (S537). A federal state can make renaming a fixed chain of approvals rather than a single decree.

| Trigger (D) | Operation | Real case |
|---|---|---|
| regime change | remove, restore older names, leave replacements local | Ukrainian settlement renaming (S538, S539) |
| retribution | rename streets of the old order | South African street renaming (S541) |
| administrative merger | adopt a wider-area, natural-feature or old-province name | Heisei municipal mergers (S530) |
| derogatory term | replace feature names one by one | US replacement names (S507) |

## 9. Romanization: who decides how a name is written for outsiders

- Under the UN working group's mandate a romanization system for geographic names is proposed by a donor country, and the group's basic task is reaching agreement on it (S534).
- The UN working group's mandate states that its systems are for geographical names and should be proposed by a donor country (S533). The country that owns the script proposes; the international body agrees.
- The third UN naming conference recommended that the Chinese Phonetic Alphabet, Pinyin, be adopted as the international system for the romanization of Chinese geographical names (S532).
- Even a reversible system has gaps: in the UN Russian system the geographical name Bajuba is reconstituted as Байуба in the Cyrillic source script, not Баюба as might be expected (S535). Record the scheme with every romanized name, because conversion back is not always unique.

## 10. Street names and field names: the small scale

- Harrow's policy says new street or building names should not duplicate any similar name already in use in a postcode area (S540). A council's street-naming rule is a local anti-duplicate rule, distinct from a national board.
- Swiss Rüti toponyms, from clearing words, are considered evidence of the first phase of land expansion and large-scale cultivation (S527). Field and locality names record when land was cleared and farmed.

## 11. Folk etymology and calibration traps

- Examination of the toponym corpus of different regions shows that less than 1% of it was created by folk etymology (S543). Folk etymology is real but rare: use it for a few famous names, not as the source of a whole map.
- The Cocwudu reshaping of the river-name Coquet (S542) is the pattern: an opaque older name is reshaped into words the newer speakers know.
- Traps (D): "every name has a meaning" (opaque names are normal); "rivers are always the oldest" (S518 says postulated, and names can be transferred or revived); "a suffix proves a conquest" (borrowing, fashion and transfer compete); "one place, one name" (§6 shows official, half-translated and community names side by side).

## 12. Build order for a fictional toponymy (D)

1. Feature classes and their generic words, with position (§4).
2. Language layers in order, each with its element inventory (§5).
3. Which layer's names survive on rivers, mountains, settlements, fields (§5).
4. Insider, outsider and half-translated forms per community (§6).
5. The naming authority, its founding act and its principles (§7).
6. Renaming events with their triggers and operations (§8).
7. The romanization scheme each outsider uses, recorded with the name (§9).
8. Council rules for streets (§10) and a handful of folk-etymologized names (§11).

## 13. Handoff to lore

Lore-shokunin owns the names and dates recorded on landed entities and events; this entry supplies naming patterns, not canon. A place-name proposal travels in the `synthesis/naming-canon-workflow.md` envelope with: feature class, layer, element analysis, insider and outsider forms, governing authority and rule, romanization scheme, and any renaming history. Lore records an in-world renaming as a new event that supersedes the old record; it does not check aliases, so exonyms, half-translations and former names must be listed explicitly in the proposal. NON-CANON until lore records it.

## 14. Recheck

Recheck a row before a handoff that depends on a policy (§7, §9) or a figure (§7, §8, §11): naming-board policies and resolutions change. Re-run `python3 -B reports/round-58/rowcheck.py --row S5NN --entry corpus/knowledge/linguistics/toponymy-place-names.md` for any cited row after a source moves.
