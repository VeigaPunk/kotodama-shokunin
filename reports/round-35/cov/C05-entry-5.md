- Seat: C05 | executor | C | date 2026-10-19 | baseline 4a7aede

# C05 — claim C, culture-material entry 5: full draft bytes

**Proposed target path (the integrator decides; P01's assignment was not received):**
`corpus/knowledge/culture-material/furniture-interior-lexicon.md`

**Claim C (binding):** +6 culture-material (18 → 24), +4 myth-symbol; each entry gap-named,
frontmatter-complete, decision-record carrying, source-resolving; README reconciled.
This fragment is one of the six culture-material drafts.

**Entry-contract derivation (no scout fragment existed when this seat ran).** The contract
applied here was read off the delivered tree, not invented: head-block fields and their exact
regexes from `reports/round-27/run-validation.py:179-187` (`^-\s*(topic|sources|verified-at|recheck|couples):`),
the `gap filled` field and the "extended, never restated" house rule from
`corpus/knowledge/linguistics/register-strata-attestation.md:3-5`, the admission bar from
`corpus/QUALITY.md:1-22`, and the shape of the partition's newest committed entries
(`corpus/knowledge/culture-material/vessel-container-lexicon.md`, read in full: gap sweep §1 →
typology → naming grammar → material ladder → calibration → decision-record table → build order →
handoff note).

**Topic choice method (what K01 was chartered to do).** Per-partition absence sweep at HEAD
`4a7aede`, run 2026-10-19 from the lane root. Furniture and the interior came back as the
cleanest unnamed domain in the partition: the two files nearest to it point at it explicitly
without filling it — `architecture-settlement-lexicon.md:49` ("the kang platform and the matted
zashiki are social architecture, **not furniture**") and `dress-through-eras.md:13` ("keep it
consistent with its furniture (chairs vs. floors vs. cushions), since seating and dress evolve
together"), plus `dress-through-eras.md:126` ("commit seating, posture, and architecture to
match"). The sweep and its characterisation are in §1 of the entry itself.

## Absence sweep — commands and results (run 2026-10-19, HEAD 4a7aede)

Partition scope: `corpus/knowledge/culture-material/*.md` = 18 files (census re-run:
`ls corpus/knowledge/culture-material/*.md | wc -l` → 18; the whole-corpus vector re-run →
linguistics 21 / myth-symbol 19 / culture-material 18 / synthesis 29 / verification 20 /
civilizations 94 = 201, matching `reports/round-35/claims.json` `before.partition_counts`).

`for kw in furniture chair stool bench seat throne cushion mattress bedstead canopy screen cabinet chest table desk; do printf "%-10s " "$kw"; grep -ril "$kw" corpus/knowledge/culture-material/*.md 2>/dev/null | wc -l; done`

| keyword | files (of 18) | what the hits are (each checked, not assumed) |
|---|---|---|
| furniture | 5 | all figurative or passing: "kiln furniture" (`vessel-container-lexicon.md:97`), "threshold furniture" (`architecture-settlement-lexicon.md:34`), "Government is furniture" (`architecture-settlement-lexicon.md:121`), "furniture → finance" (`trade-economy-lexicon.md:87`), the dress pointer (`dress-through-eras.md:13`) |
| chair | 3 | `architecture-settlement-lexicon.md:80` (*kathédra* "the bishop's seat"); `adornment-body-codes.md:81` (curule chair, "who may sit"); `dress-through-eras.md:13` (chairs vs. floors vs. cushions) |
| seat | 3 | `architecture-settlement-lexicon.md:80`; `dress-through-eras.md:126` ("commit seating"); `trade-economy-lexicon.md:110` (*za* 座 'seat' = guild — an institution word, not furniture) |
| bench | 2 | `architecture-settlement-lexicon.md:121` (the Bench as council); `trade-economy-lexicon.md:87` (*banca rotta* 'broken bench' → bankrupt) |
| throne | 2 | `adornment-body-codes.md:81` (Byzantine mechanical throne, passing); `era-periodization-models.md:56` (a passing use) |
| cushion | 2 | `architecture-settlement-lexicon.md:121` ("the Cushions" as a council name); `dress-through-eras.md:13` |
| screen | 2 | `architecture-settlement-lexicon.md:30` (*yingbi* 影壁 screen wall); `era-periodization-models.md` (an unrelated use) |
| cabinet | 1 | `era-periodization-models.md:6,31` — the Japanese cabinet as a constitutional organ; **no storage-furniture sense anywhere in the partition** |
| stool, mattress, bedstead, canopy, desk | 0 | — |
| chest | 8 | body part ("hand height chest → nose → brow"), `-chester` place-name suffix, and unrelated substrings — **no chest/coffer sense** |
| table | 108 occurrences | 2 are "decision table"; 16 are in `cuisine-food-lexicon.md` §6 "the table as grammar" (the eating institution, not the object); the remainder are markdown table syntax (793 pipe-rows in the partition) |

Corpus-wide corroboration: `stool`, `mattress`, `bedstead`, `canopy`, `desk`, `bedstede`,
`box-bed`, `charpoy`, `klismos`, `sella curulis`, `byobu` return 0 across
`corpus/knowledge/*/*.md`; `curule` returns 3 (all passing), `triclinium` 2, `shoin` 1,
`tatami` 1 — i.e. the partition's one heated-platform sentence
(`architecture-settlement-lexicon.md:49`) is the whole of the corpus's seating-posture material.

## The entry bytes

Integrator: write the fenced block below verbatim to the target path. The `- topic:` line is the
README row source (the README row must be byte-equal to the topic text after `- topic: `, per
the revision notes in `corpus/README.md:1-40`); a generator command for the row is in the
"README delta aid" section at the end of this fragment.

````markdown
# Furniture and the Interior — Seating Posture, the Chair's Rank Career, Sleeping, Tables and Storage Furniture, and the Room as a Social Machine

- topic: furniture and the interior as a cultural system for fictional cultures — the gap this entry fills, since the partition owns buildings (`architecture-settlement-lexicon.md`) and dress (`dress-through-eras.md`) but no file owns what people sit on, sleep in, eat off, or keep things in; the master claim is that the **seating regime is chosen first** — floor, platform, or chair — and it silently decides table height, room proportions, garment cut, servant posture, and the grammar of rank, so it must be fixed before any furniture is named; the three-regime typology with real exemplars (Japanese tatami and seiza, Korean ondol, Indian āsana and the charpoy, the Islamic majlis cushion line, the Greek klismos/diphros/klinai, the Roman triclinium and late stibadium, the Chinese huchuang 胡床 folding stool and the Tang–Song turn to chair-and-table sitting); the chair's rank career (sella curulis and thronos/solium, kathédra → cathedral, the seat as office: chairman, the Chair, the bench, the electoral seat, the Japanese *za* 座, the Scottish stool of repentance); sleeping (the bed as rank object and semi-public stage — the state bed and the *ruelle*, the box-bed and Dutch *bedstede*, the folded futon, the kang 炕 platform, the Great Bed of Ware and the "second best bed with the furniture" as furniture in law); tables (boards and trestles, the table's institutional children — room and board, board of directors, the Lord's Table, the Covenanters' Tables, the Exchequer's checkered cloth cross-read from `trade-economy-lexicon.md`); storage furniture as document (the chest/coffer as archive and dowry record, cabinet and wardrobe as rooms that became departments of state and then pieces of furniture, the closet as privacy institution); screens, hangings and canopies as privacy technology; the un-sittable seat (the Asante Golden Stool, Luba caryatid stools) and the vacant seat as a holder for an absent guest; the calibration shelf of standing myths (crude-medieval furniture, chair = authority everywhere, the ancient fixed dining table, the private bed, furniture as trivia); a decision-record table; a build order and one non-canon worked micro-example. Reference and method only; canon decisions are lore-shokunin's.
- gap: the furniture/interior domain is absent from culture-material — this entry fills it. Measured absence sweep at HEAD `4a7aede`, 2026-10-19, over the 18 committed culture-material files (`for kw in furniture chair stool bench seat throne cushion mattress bedstead canopy screen cabinet chest table desk; do printf "%-10s " "$kw"; grep -ril "$kw" corpus/knowledge/culture-material/*.md 2>/dev/null | wc -l; done` → furniture 5 / chair 3 / stool 0 / bench 2 / seat 3 / throne 2 / cushion 2 / mattress 0 / bedstead 0 / canopy 0 / screen 2 / cabinet 1 / chest 8 / table 108 occurrences / desk 0) and every hit was read and classified in §1: the five "furniture" hits are figurative (kiln furniture, threshold furniture, "Government is furniture", "furniture → finance", the dress pointer), the "cabinet" hit is the Japanese constitutional organ, the "chest" hits are the body part and `-chester` place names, the "table" hits are markdown tables plus `cuisine-food-lexicon.md` §6's eating institution. The two nearest siblings point at this domain and do not fill it: `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:49` ("the kang platform and the matted zashiki are social architecture, not furniture") and `corpus/knowledge/culture-material/dress-through-eras.md:13` ("seating and dress evolve together") with `:126` ("commit seating, posture, and architecture to match"). Division of labour: the container typology stays with `corpus/knowledge/culture-material/vessel-container-lexicon.md`; room and building vocabulary stays with `architecture-settlement-lexicon.md`; dress cut stays with `dress-through-eras.md`; table etiquette stays with `cuisine-food-lexicon.md` §6; the measure→money chain stays with `trade-economy-lexicon.md`; this entry owns the objects a body rests on and the furniture that is also an office, an archive, or a privacy machine.
- sources:
  - Seating and the classical repertoire: Richter (1966), *The Furniture of the Greeks, Etruscans and Romans*, Phaidon — the standard corpus for *klismos*, *diphros*, *kline*, *thronos*, and the Roman *lectus*; Dunbabin (2003), *The Roman Banquet: Images of Conviviality*, Cambridge UP (reclining dining, the *triclinium* and the late *stibadium*); OED 3rd edn (online), s.vv. *curule*, *throne*, *chair*, *stool*, *bench* (etymology legs only; not re-consulted this round).
  - Egypt and the ancient Near East: Killen (1980; 1994), *Ancient Egyptian Furniture*, vols. I–II, Aris & Phillips / Oxbow — chairs, stools, beds, and the joinery that survives in tomb furniture (record-level citation this round).
  - China and Inner Asia: Handler (2001), *Austere Luminosity of Chinese Classical Furniture*, University of California Press — the floor-to-chair transition, the *huchuang* 胡床 folding stool, the platform bed; Ruitenbeek (1993), *Carpentry and Building in Late Imperial China: A Study of the Fifteenth-Century Carpenter's Manual Lu Ban jing*, Brill (Sinica Leidensia 23) — the carpenter's own vocabulary and measures (record-level citation; the entry's dating claims are marked below).
  - Japan and Korea: Nishi & Hozumi (1983), *What Is Japanese Architecture?*, Kodansha International, and Itoh (1972), *Traditional Domestic Architecture of Japan*, Weatherhill — both already cited in `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:3`; the tatami room, the built-in *tsuke-shoin* desk and shelves, and sleeping on folded bedding; the ondol/kang platform is cross-read from `architecture-settlement-lexicon.md:49`, not restated.
  - Interior life, privacy and the bed: Thornton (1978), *Seventeenth-Century Interior Decoration in England, France and Holland*, Yale UP (bed-hangings, the alcove, the *ruelle*); Girouard (1978), *Life in the English Country House: A Social and Architectural History*, Yale UP (the hall as dormitory, the withdrawal of privacy, the closet, the state bed); Woolgar (1999), *The Great Household in Late Medieval England*, Yale UP (boards and trestles, household bedding, accounts); Rybczynski (1986), *Home: A Short History of an Idea*, Viking, and Rybczynski (2016), *Now I Sit Me Down: From Klismos to Plastic Chair: A Natural History*, Farrar, Straus and Giroux (the chair's slow domestic diffusion — a trade book, usable as orientation, not as a source of record).
  - Regalia and the seat as office: Rattray (1923), *Ashanti*, Clarendon Press, and Wilks (1975), *Asante in the Nineteenth Century*, Cambridge UP — the Golden Stool (Sika Dwa Kofi), never sat upon, and the Akan stool as the name of an office; Roberts & Roberts, eds. (1996), *Memory: Luba Art and the Making of History*, Museum for African Art / Prestel — Luba caryatid stools as title objects.
  - Furniture in law and language: Shakespeare's will (1616), "my second best bed with the furniture" — the word *furniture* still meaning the bed's equipment, not the object; OED s.vv. *furniture*, *board*, *cabinet*, *wardrobe*, *closet*, *divan*, *sofa*, *hammock* (etymology legs only, not re-consulted this round); V&A collection record for the Great Bed of Ware (object record; dimensions cited below are marked `to-verify`).
  - In-repo pointers resolved by command this round (all paths read or grepped at HEAD `4a7aede`): `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:30,49,80,121,125` (screen wall, "not furniture", "authority is a chair", "Government is furniture", threshold rites); `corpus/knowledge/culture-material/dress-through-eras.md:13,126`; `corpus/knowledge/culture-material/adornment-body-codes.md:81`; `corpus/knowledge/culture-material/trade-economy-lexicon.md:87,89,92,110`; `corpus/knowledge/culture-material/cuisine-food-lexicon.md:18,90,92,129,150`; `corpus/knowledge/culture-material/ritual-garments.md:21`; `corpus/knowledge/myth-symbol/ritual-liminality.md:21,30`; `corpus/knowledge/culture-material/era-periodization-models.md:6,31`; `corpus/knowledge/verification/to-verify-triage-protocol.md`; `reports/round-9/metadata/v10-culture.md` (partition census receipt cited by `vessel-container-lexicon.md:4`); `reports/round-10/run-validation.py` (the acceptance contract this entry's head-block shape is written against).
- couples: corpus/knowledge/culture-material/architecture-settlement-lexicon.md (that file owns rooms, roofs and settlement; this entry owns what stands inside them — it is the "not furniture" clause at `:49` filled in, and its threshold-furniture lever at `:34` is where the two meet), corpus/knowledge/culture-material/dress-through-eras.md (the seating regime decides garment cut and drape; that file's `:13` and `:126` point here), corpus/knowledge/culture-material/vessel-container-lexicon.md (containers on, in and under furniture: the table as a serving surface, the chest as a container at furniture scale — its "container systems at building scale" boundary stops where furniture begins), corpus/knowledge/culture-material/cuisine-food-lexicon.md (§6 "the table as grammar" owns etiquette and service sequence — cross-read, not restated; the table object is here), corpus/knowledge/culture-material/trade-economy-lexicon.md (its furniture→institution rows at `:87` bench→bank, `:89` checkered cloth→Exchequer, `:92` tally stock/foil, `:110` *za* 座 'seat'→guild are the money side of this entry's office side — cited, not repeated), corpus/knowledge/culture-material/transport-mobility-lexicon.md (the litter, palanquin and sedan chair are furniture that is transport; the saddle is the nomad's chair), corpus/knowledge/culture-material/warrior-material-culture.md (camp furniture, the folding stool of command, and the tent as a room), corpus/knowledge/culture-material/sumptuary-law-rank-display.md (a seating law is a semiotic machine like a dress law: who may sit, on what, in whose presence), corpus/knowledge/culture-material/craft-artisan-lexicon.md (the joiner/cabinetmaker/upholsterer trades, tool and material grading, and the maker's mark on furniture), corpus/knowledge/culture-material/textile-technology.md (upholstery, bedding and hangings are the textile industry's second customer after dress), corpus/knowledge/culture-material/adornment-body-codes.md (posture gradients at `:81` are performed *on* furniture — the bow's geometry changes when the bowing body is seated), corpus/knowledge/culture-material/era-periodization-models.md (furniture styles as era evidence; the cabinet as a modern constitutional organ at `:6,31`), corpus/knowledge/linguistics/semantic-fields-lexicon-building.md (the furniture field as a semantic field: part-naming, borrowability strata, core vocabulary), corpus/knowledge/linguistics/historical-linguistics.md (furniture words drift by metonymy: board→food, cabinet→council, wardrobe→office), corpus/knowledge/linguistics/language-contact.md (chair/stool/sofa/divan loan strata date contact), corpus/knowledge/myth-symbol/ritual-liminality.md (thresholds and the marriage threshold at `:21,:30`; the bed, the threshold and the vestry are the smallest liminal rooms a world can stage), corpus/knowledge/culture-material/ritual-garments.md (the vestry and its furniture: the unvested body in a liminal room at `:21`), corpus/knowledge/verification/to-verify-triage-protocol.md (every `(to-verify)` mark below routes through that procedure); handoff target: lore-shokunin world bible — reference knowledge, tables and method only; canon decisions are theirs (lane rule, AGENTS.md).
- verified-at: 2026-10-19 — this draft was written under round-35 with **no network access**: every in-repo pointer above was resolved by command at HEAD `4a7aede` (existence check plus the cited line read; the sweep commands and counts are in the `- gap:` field and §1), and every external work is a **record-level citation only** — no page, catalogue or object record was fetched this round, and each specific that depends on one carries `(to-verify)` in place. Not re-consulted: Richter 1966, Killen 1980/1994, Handler 2001, Ruitenbeek 1993, Thornton 1978, Girouard 1978, Woolgar 1999, Rybczynski 1986/2016, Rattray 1923, Wilks 1975, Roberts & Roberts 1996, Dunbabin 2003, the OED entries named above, and the V&A object record for the Great Bed of Ware.
- recheck: before printing any chair-arrival date for China, any dimension or date for the Great Bed of Ware, any claim about the Golden Stool's ritual status or the 1921 replica, any seating-order rule as universal, any OED etymology (*sofa*, *divan*, *cabinet*, *wardrobe*, *closet*, *furniture*, *board*) as settled, any health claim about floor-sitting versus chair-sitting, and before letting one furniture set stand for a whole culture.

## 1. The gap this entry fills — the interior had no owner

- **Gap filled: the furniture/interior domain.** Absence sweep run 2026-10-19 from the lane root over the 18 committed partition files (`for kw in furniture chair stool bench seat throne cushion mattress bedstead canopy screen cabinet chest table desk; do printf "%-10s " "$kw"; grep -ril "$kw" corpus/knowledge/culture-material/*.md 2>/dev/null | wc -l; done`):

| keyword | files (of 18) | what the hits actually are (each read, not assumed) |
|---|---|---|
| furniture | 5 | all figurative or passing: "kiln furniture" (`vessel-container-lexicon.md:97`), "threshold furniture" (`architecture-settlement-lexicon.md:34`), "Government is furniture" (`architecture-settlement-lexicon.md:121`), "furniture → finance" (`trade-economy-lexicon.md:87`), the dress pointer (`dress-through-eras.md:13`) |
| chair | 3 | *kathédra* "church of the (bishop's) seat" (`architecture-settlement-lexicon.md:80`); the curule chair, "who may sit" (`adornment-body-codes.md:81`); "chairs vs. floors vs. cushions" (`dress-through-eras.md:13`) |
| seat | 3 | the bishop's seat (`architecture-settlement-lexicon.md:80`); "commit seating, posture" (`dress-through-eras.md:126`); *za* 座 'seat' = guild (`trade-economy-lexicon.md:110`) |
| bench | 2 | "the Bench" as a council (`architecture-settlement-lexicon.md:121`); *banca rotta* 'broken bench' → bankrupt (`trade-economy-lexicon.md:87`) |
| throne | 2 | the Byzantine mechanical throne, passing (`adornment-body-codes.md:81`); one passing use in `era-periodization-models.md` |
| cushion | 2 | "the Cushions" as a council name (`architecture-settlement-lexicon.md:121`); `dress-through-eras.md:13` |
| screen | 2 | *yingbi* 影壁 screen wall (`architecture-settlement-lexicon.md:30`); one unrelated use |
| cabinet | 1 | the Japanese cabinet as a constitutional organ (`era-periodization-models.md:6,31`) — no storage-furniture sense in the partition |
| stool, mattress, bedstead, canopy, desk | 0 | — |
| chest | 8 | the body part ("hand height chest → nose → brow"), the `-chester` place-name suffix, unrelated substrings — no chest/coffer sense |
| table | 108 occurrences | 2 are "decision table"; 16 sit in `cuisine-food-lexicon.md` §6 "the table as grammar" (the eating institution); the rest are markdown table syntax (793 pipe-rows partition-wide) |

- Corpus-wide corroboration: `stool`, `mattress`, `bedstead`, `canopy`, `desk`, `bedstede`, `box-bed`, `charpoy`, `klismos`, `sella curulis`, `byobu` return 0 over `corpus/knowledge/*/*.md`; `curule` 3 (all passing), `triclinium` 2, `tatami` 1, `shoin` 1 — the partition's single heated-platform sentence (`architecture-settlement-lexicon.md:49`) is the whole of the corpus's seating-posture material.
- **Division of labour against the siblings** (so this entry extends, never restates): `architecture-settlement-lexicon.md` owns rooms, roofs, settlement and the threshold; `dress-through-eras.md` owns garment cut; `vessel-container-lexicon.md` owns the container typology; `cuisine-food-lexicon.md` §6 owns table etiquette and service sequence; `trade-economy-lexicon.md` owns the measure→money→institution chain, including its furniture→finance rows, which this entry cites at `:87,:89,:92,:110` and does not repeat. This entry owns **the objects a body rests on, and the furniture that is also an office, an archive, or a privacy machine**.
- **Boundary — what this entry does not own** (routed, not absorbed): light, fuel and the hearth economy belong to a separate domain (a sibling draft in this wave owns fire/fuel/light); bathing, sanitation and water supply belong to another; this entry takes the surfaces, seats, beds, tables, storage and screens, and cites the heated-platform sentence in `architecture-settlement-lexicon.md:49` rather than re-covering heating. Where a sibling entry lands in this wave, its subject wins and this entry's clause is the boundary.
- **Method statement** (partition house rule): everything below is reference knowledge and craft method. Nothing here decides what is true in any world; the handoff is at §11.

## 2. Choose the seating regime first — the three-regime frame

A culture's furniture follows from one prior decision: **where the pelvis goes.** Three regimes, each with a consequence chain. Pick one per culture (and one per class inside it), then derive.

| Regime | Seat object | Posture | Consequences that follow automatically |
|---|---|---|---|
| FLOOR | mat, rug, cushion, tatami, heated stone platform | cross-legged, kneeling (*seiza*), side-sitting | low or absent tables; rooms proportioned to the mat; bedding folded away by day; shoes off at the boundary; servants kneel to serve; garments must not need knee-room — drape and hem become the design problem |
| PLATFORM | raised divan, *kang* 炕, bench-bed, charpoy, dais | seated above the floor line, legs often folded or dangling | heat or height carries rank ("who gets the platform"); the platform is bed, sofa and throne at once; the room's furniture count stays low; the platform's edge is a social boundary |
| CHAIR | back-rest seat with legs, stool for the low ranks | thighs horizontal, feet down | tables rise to the seat; the chair becomes a rank instrument (arms, back height, cushion count); the room gains movable furniture and loses multi-purpose floor space; standing becomes a distinct posture with its own etiquette |

- **Real anchors.** FLOOR: the Japanese tatami room with its *shoin* built-ins (Nishi & Hozumi 1983; Itoh 1972 — both already in `architecture-settlement-lexicon.md:3`); Korean *ondol* heated-floor sitting, cross-read from `architecture-settlement-lexicon.md:49`; the Indian *āsana* and the low string bed; the Islamic *majlis* cushion line, whose name is "place of sitting" (`architecture-settlement-lexicon.md:31`). PLATFORM: the North Chinese *kang*, the Persian/Turkish *divan* (a raised cushioned bench, whence the council), the West African bed-platform. CHAIR: the Greek *klismos* and *diphros*, the Roman *lectus* and *cathedra* (Richter 1966), the Chinese chair after the Tang–Song turn (Handler 2001), the European domestic chair (Rybczynski 2016).
- **The chair is the exception, not the rule.** For most of most people's history the chair was a rank object, not household furniture: Egypt gave chairs to the elite and stools to everyone else (Killen 1980/1994); in Homeric and archaic Greece the chair and the stool were the seating, while the dining couch belonged to the symposium (Richter 1966; Dunbabin 2003); in China the back-rest seat and the high table become ordinary only after the Tang, with the *huchuang* 胡床 folding stool arriving first as an Inner Asian object with a "barbarian" name (Handler 2001 — **the pace of this transition is debated; print no date without checking, to-verify**); in Japan and Korea the chair never displaced the floor. The chair's global spread is largely a nineteenth- and twentieth-century story.
- **Design lever**: state the regime in one line per culture and let it discipline everything downstream — table height, room height, the servant's posture, the shape of the formal greeting (a bow performed from a chair and a bow performed from a kneeling position are different gestures), and the cut of the clothes (`dress-through-eras.md:13,:126`). A culture that sits on the floor and owns a high table has a design error, not a quirk.

## 3. The chair's rank career — from magistrate's seat to household object

- **The chair as office before it was furniture.** The Roman *sella curulis* — the folding ivory chair of magistrates holding *imperium* — is the clean case: the object *is* the jurisdiction, and the same grammar recurs in the *thronos*/*solium*, the bishop's *kathédra* (which names the cathedral — `architecture-settlement-lexicon.md:80`), and the judge's bench. The Greek and Roman dining couch likewise assigned status by position (middle couch, left side) rather than by furniture type (Dunbabin 2003).
- **The word-chain that proves the point** (all senses in OED, not re-consulted this round — etymology legs **to-verify**): *chair* → "chairman" and the parliamentary "the Chair"; *bench* → the judiciary and, in the corpus's own rows, a council named after its furniture (`architecture-settlement-lexicon.md:121`); *seat* → an electoral seat and, in Japanese, *za* 座 'seat' naming a guild (`trade-economy-lexicon.md:110`); *stool* → the Scottish kirk's "stool of repentance" (cutty stool), a piece of furniture used as a public-penance instrument (**to-verify before printing any detail**).
- **The un-sittable seat.** The Asante Golden Stool (Sika Dwa Kofi) is never sat upon: it is the nation's soul, not a seat, and the 1900 war against Governor Hodgson's demand to sit on it is the proof (Rattray 1923; Wilks 1975 — the 1921 replica made to permit Prempeh I's exile is **to-verify**). Luba caryatid stools are title objects kept as memory rather than furniture (Roberts & Roberts 1996). The design rule: **a seat can be a constitutional object**, and once it is, sitting on it becomes an act of state.
- **The vacant seat.** Furniture can hold an absent person: the chair of Elijah at a circumcision, the cup of Elijah at the Seder, the empty chair in modern mourning practice (all **to-verify** for specifics; the design pattern is the point). A culture's vacant chair tells you what it expects to return.
- **Design levers**: (a) decide whether your culture's chairs descend from the magistrate's seat or the household bench — the first produces chairs as offices with sumptuary rules, the second produces chairs as comfort; (b) give one rank the *right to a back* (chair vs. stool vs. floor) and let the difference be visible at ten metres; (c) let one reform invert it — the chair democratised is a datable event in furniture history.

## 4. Sleeping — the bed as rank object, as room, and as legal fact

- **The bed is the room in most of the pre-modern world.** In the medieval hall the household slept in the common space; privacy was withdrawn slowly and by class (Girouard 1978; Woolgar 1999). The enclosed bed — box-bed, wall-bed, Dutch *bedstede*, Breton *lit clos* — is a room compressed into furniture, with doors and hangings, and it survives in cold climates into the twentieth century (**regional distribution to-verify**).
- **The bed as a stage.** The early modern state bed with its canopy and hangings is a piece of theatre; the *ruelle* — the narrow space between the bed and the wall — became the Parisian salon's site, so that conversation itself was furniture-shaped (Thornton 1978). The Great Bed of Ware (oak, c. 1590; a tourist attraction in its own century and mentioned by Shakespeare) shows the bed as public spectacle rather than private retreat (V&A object record; dimensions **to-verify**).
- **Furniture in law.** Shakespeare's will (1616) leaves his wife "my second best bed with the furniture" — where *furniture* still means the equipment that goes with a thing (hangings, bedding), not movable goods in general; the word's narrowing is itself a datable piece of furniture history (OED s.v. *furniture* — **to-verify**). "Bed and board" survives as the legal formula for marriage and for separation from it; the "best bed" bequest is a standard feature of early modern wills (**to-verify** at document level).
- **Sleeping outside the bed-frame.** The Japanese futon folded away by day makes the bedroom a room only at night (Itoh 1972); the *kang* and *ondol* platform is a heated sleeping and sitting surface at once (`architecture-settlement-lexicon.md:49`); the hammock, a Caribbean loan into European maritime practice, hangs the sleeper from the ship's structure (OED s.v. *hammock* — **to-verify**); nomadic bedding is a roll and a saddle-blanket, with the saddle as the day's chair (couple: `transport-mobility-lexicon.md`).
- **Design levers**: (a) decide who shares a bed — the bed's width is a kinship statement, and the "bed-sharing map" of a household is a plot engine; (b) decide whether the bed is furniture or architecture (a platform, a niche, a hanging); (c) make one bed a legal object (the heir's bed, the widow's bed, the guest's bed) and the household's whole inheritance politics becomes visible in one room.

## 5. Tables — the board that becomes an institution

- **Boards and trestles first.** For most of European history the dining table was boards laid on trestles and taken down after the meal; "board" survives in "room and board" and "board of directors", and the fixed table with matching chairs is an early modern development tied to the service transition from service *à la française* to *à la russe* (`cuisine-food-lexicon.md:18`; Girouard 1978; Woolgar 1999 — **the exact sequence is to-verify**).
- **The table as institution is already partly in this corpus, and is cited rather than restated**: the checkered counting cloth of the Norman Exchequer gave English its "exchequer", "check" and "cheque" (`trade-economy-lexicon.md:89`), and the split tally on that table gave *stock* its name (`trade-economy-lexicon.md:92`). This entry adds the furniture side: **the table is where a culture puts its arithmetic**, so the table's shape is an accounting decision before it is a dining one.
- **More institutional children** (each **to-verify** for date and detail): the Lord's Table as the communion table and its political furniture history; the Covenanters' "Tables" of 1637–38, committees named for the tables they sat at; the round table as an equality claim (and its myth); the negotiating "green table".
- **Posture and the table's height are one decision** (§2). A floor-sitting culture's table is a low tray or none at all; a chair culture's table rises to the thigh; a standing culture's table is a counter. Greek and Roman dining reclined on couches around a low table, with the table serving the couches rather than the sitters (Dunbabin 2003); the Chinese high table and chair arrive together (Handler 2001 — **dating to-verify**).
- **Design lever**: choose the table's *function stack* — one culture may use the same board for eating, counting, judging and sacrificing, and another may forbid any one of those uses on the eating table. The prohibition list is the culture's ontology, and it is cheap to write.

## 6. Storage furniture — the chest, the cabinet, the wardrobe, the closet

- **The chest is the first and last furniture of the poor and the nomad.** A chest is simultaneously container, seat, table, wardrobe and archive; the dowry chest (Italian *cassone*, the "hope chest") is a marriage contract in wood, and the parish chest holds the documents that make a community legal (**the chest-as-archive pattern is general; per-case citations to-verify**).
- **Three words that were rooms before they were furniture** — the partition's "Government is furniture" row (`architecture-settlement-lexicon.md:121`) has a storage-side twin, and this entry supplies it:
  - **cabinet** — a small private room, then the room where a ruler took counsel (hence the Cabinet as a constitutional organ; the modern Japanese cabinet 内閣 is a "cabinet" of the same lineage, visible in this corpus at `era-periodization-models.md:6,31`), and only later a chest of drawers (OED — **to-verify**).
  - **wardrobe** — a room for keeping clothes, then an office of the royal household (the Great Wardrobe as a department of state), then the piece of furniture (OED — **to-verify**).
  - **closet** — a small closed room for private counsel and prayer (the KJV's "enter into thy closet", Matt 6:6), then, much later, the storage sense (OED — **to-verify**).
- **Design lever**: give every culture one storage word that has **drifted from room to object to office**, and let an in-world etymologist argue about which sense came first. The drift is attested three times over in English alone, so it is a cheap, high-credibility texture — and it links furniture to government without touching canon.
- **Storage furniture is also where the house keeps its secrets**: the locked chest, the strongbox, the escritoires with secret drawers, the seal kept in a box. Couple to `craft-artisan-lexicon.md` (the cabinetmaker, the joiner, the locksmith's marks) and to `trade-economy-lexicon.md` (the strongbox as a bank's ancestor).

## 7. Screens, hangings and canopies — furniture that makes privacy

- **The screen is architecture that moves.** The *yingbi* 影壁 screen wall inside the gate (`architecture-settlement-lexicon.md:30`) is the fixed, architectural form; the folding screen (Japanese *byōbu*, Chinese *pingfeng*), the curtain, the hanging and the bed canopy are the movable ones. Their job is always the same: to create a boundary where no wall exists.
- **The canopy is rank made vertical**: the bed canopy, the throne's baldachin, the processional umbrella. A canopy says "this space is not ordinary" without any wall; it is the cheapest sacred/regal enclosure a world can build, and it couples directly to `myth-symbol/ritual-liminality.md:21,:30` (thresholds and the marriage threshold) and to `ritual-garments.md:21` (the vestry as a liminal room).
- **Design levers**: (a) decide what may be screened — the body, the face, the bed, the altar, the corpse — and the culture's privacy theory is written; (b) give the screen one forbidden use (a screen that may not be placed between a ruler and the people is a constitutional fact); (c) let one screen be a document (a painted screen as a genealogy or a treaty record).

## 8. Calibration — the standing myths

- **"Medieval furniture was crude."** A nineteenth-century myth: the surviving furniture of the period is sophisticated joinery, and the *scarcity* of fixed furniture was a choice about portability and multi-use, not poverty of skill (Girouard 1978; Thornton 1978 — **status: discredited as a general claim**).
- **"Chair = authority, everywhere."** False as a universal. In floor-sitting cultures authority sits on platforms, thrones of other shapes, or cushions; the chair's link to office is a Mediterranean-European lineage that later travelled (Richter 1966; Handler 2001). **Status: contested if stated as a human universal; sound if pinned to a lineage.**
- **"The dining table and chair set is ancient."** The fixed table with individual chairs is an early modern arrangement in Europe; before it, boards on trestles, benches, and shared vessels (`cuisine-food-lexicon.md:92` on Elias's place-setting history; Flandrin via `:18`). **Status: discredited as a general claim.**
- **"The bed was private."** Beds were staged, shared, and shown; the state bed and the Great Bed of Ware are public objects (Thornton 1978; V&A record — **to-verify**).
- **"Furniture is trivia."** Furniture carries law (the best bed, bed and board), office (the curule chair, the stool of repentance, the *za*), and money (the bench that became a bank — `trade-economy-lexicon.md:87`). **Status: discredited as a design premise.**
- **Health claims about posture** (floor-sitting cultures have better joints; chairs ruin the back) are popular and **unproven** — treat as in-world belief, never as design fact.
- **One furniture set per culture is a pastiche error.** Furniture varies by class and century inside a single culture: the poor had a chest, a bench and bedding; the rich had types. The variable to design is the *inventory of types per class*, not a national style.

## 9. Decision record — the furniture decisions this entry fixes

Each row is a decision a worldbuilder (or a later reviser of this file) must take *explicitly*; the rejected column names the option that must not be taken silently. Ids are stable so later rounds can amend rows without rewriting the file.

| ID | Decision | Why | Rejected alternative | Evidence |
|---|---|---|---|---|
| DR-FUR-01 | Fix the **seating regime** (floor / platform / chair) per culture *and per class* before naming any furniture | it silently determines table height, room proportions, garment cut, servant posture and greeting geometry | letting furniture accumulate with no regime behind it | §2; `dress-through-eras.md:13,:126` |
| DR-FUR-02 | Decide who may have a **back** (chair / stool / floor) and make the difference visible at distance | the chair is a rank instrument before it is comfort | chairs for everyone in a pre-modern setting | §3; Richter 1966; Killen 1980/1994 |
| DR-FUR-03 | Give at most **one** seat constitutional status (a throne, a golden stool, an empty chair) and write what sitting on it means | a seat that is an office converts a gesture into an act of state | several sacred seats competing | §3; Rattray 1923; Wilks 1975 |
| DR-FUR-04 | Decide whether the bed is **furniture or architecture** (frame, niche, platform, hanging) | it decides whether the bedroom exists as a room | assuming a framed bed as the default | §4; Itoh 1972; `architecture-settlement-lexicon.md:49` |
| DR-FUR-05 | Publish the **bed-sharing map** (who sleeps with whom, who sleeps alone, who sleeps in the common room) | the bed's occupancy is the household's kinship statement | one bed per person as the norm | §4; Girouard 1978; Woolgar 1999 |
| DR-FUR-06 | Pick the **table's function stack** (eating / counting / judging / sacrificing) and its prohibition list | the table is where a culture puts its arithmetic; prohibitions are the ontology | a table that does everything with no rules | §5; `trade-economy-lexicon.md:89,:92` |
| DR-FUR-07 | Choose whether tables are **fixed or struck** (boards on trestles vs. permanent furniture) | portability decides room use, servant labour and the meal's duration | the fixed dining set as the unmarked default | §5; `cuisine-food-lexicon.md:18,:92` |
| DR-FUR-08 | Give the culture **one storage word that drifted room → object → office**, and date the drift | the drift is attested (cabinet, wardrobe, closet) and links furniture to government cheaply | storage vocabulary with no history | §6; `architecture-settlement-lexicon.md:121`; OED (**to-verify**) |
| DR-FUR-09 | Decide what may be **screened** (body, face, bed, altar, corpse) and one forbidden screen use | the screen is the movable boundary; its rules are the privacy theory | screening with no rules | §7; `architecture-settlement-lexicon.md:30`; `ritual-liminality.md:21` |
| DR-FUR-10 | Set the **inventory of types per class** (what a poor household owns vs. a rich one) | furniture varies by class inside a culture; a single national style is a pastiche error | one furniture set for the whole culture | §8; Girouard 1978 |
| DR-FUR-11 | Mark every **dimension, date and etymology** as a range or as `to-verify` before it reaches the bible | furniture numbers are almost always reconstructions (bed widths, chair dates, loan etymologies) | printing a single figure as *the* standard | §4; §8; `recheck` above |
| DR-FUR-12 | Route every unresolved item through the corpus's `to-verify` triage rather than laundering it into prose | corpus rule: unverifiable claims are marked, never asserted | writing a confident sentence and moving on | `corpus/knowledge/verification/to-verify-triage-protocol.md`; `corpus/QUALITY.md` item 1 |

## 10. Applying it to a fictional culture — build order

1. **Fix the regime** (§2, DR-FUR-01) for each class in the culture; write one line of justification each — ecological, economic, or political, never "it's traditional".
2. **Assign the backs** (DR-FUR-02): who sits on what, and what a wrong seat costs.
3. **Name the seat that is an office** (DR-FUR-03) and write its sitting rules (who may sit, on what, in whose presence, and what a refusal means).
4. **Choose bed-as-furniture or bed-as-architecture** (DR-FUR-04) and publish the bed-sharing map (DR-FUR-05).
5. **Fix the table** (DR-FUR-06/07): height from the regime, function stack, prohibitions, fixed or struck.
6. **Build the storage chain** (DR-FUR-08): chest → cabinet/wardrobe/closet equivalents, with one word that drifted from room to object to office; add the locked box and the seal.
7. **Write the screening rules** (DR-FUR-09) and place one forbidden screen.
8. **Set the class inventories** (DR-FUR-10) — a poor-house list and a rich-house list, deliberately different.
9. **Couple and check**: run the furniture list through the sibling tables — garment cut against `dress-through-eras.md`, container scale against `vessel-container-lexicon.md`, etiquette against `cuisine-food-lexicon.md` §6, office words against `trade-economy-lexicon.md:87,:89,:110`, the litter against `transport-mobility-lexicon.md`, posture gradients against `adornment-body-codes.md:81`.
10. **Calibrate before handoff** (§8): strike any universal claim about chairs, tables, beds or privacy; mark remaining doubts `(to-verify)`.

**Worked micro-example (NON-CANON — a demonstration, not a world decision).** A highland culture (working label only) sits on a heated stone platform in winter and on the floor in summer, so its only raised furniture is the bed-platform and the storage chest; its status marker is **the cushion count** (three cushions = household head, one = adult, none = child or guest of low standing), which makes every room's seating readable at a glance; its table is a low board used for eating and for counting wool, and the same board may not be used for the ancestor offerings — that prohibition is where its ontology is written; its chest is called by a word that once meant "the sealed room", now means the box itself, and the clan's charter is kept in it, which is why the chest is also the seat of the clan court. Every consequence above was derived from DR-FUR-01, -02, -06 and -08; none of it is a canon claim.

## 11. Handoff note

- This entry ends at the handoff. It supplies: the three-regime frame, the chair's rank career, the bed/table/storage/screen systems, the calibration shelf, and the decision-record rows. It decides nothing about any world.
- **To lore-shokunin**: the receiving bible should take (a) the regime per class, (b) the seat-as-office rules, (c) the bed-sharing map, (d) the table's function stack and prohibitions, (e) the storage drift word, and (f) any `(to-verify)` items still open — those must not be treated as world-fact until resolved through `corpus/knowledge/verification/to-verify-triage-protocol.md`.
- **Known limits of this entry**: no drawings and no typological key; external works are record-level citations only (no page or object record fetched this round — see `verified-at`); the Chinese chair transition, the Great Bed of Ware's dimensions, the Golden Stool's replica history, the Scottish stool of repentance and every OED etymology named above are marked `(to-verify)` and need a resolution pass before in-world use.
````

## Pointer resolution record (in-repo, resolved by command 2026-10-19)

Every in-repo path the draft cites was resolved at HEAD `4a7aede` (the tree is otherwise clean:
`git status --porcelain` → only `?? reports/round-35/`). Resolutions used, verbatim:

- `for kw in ...; do grep -ril "$kw" corpus/knowledge/culture-material/*.md | wc -l; done` — the
  sweep table in §1 and in `gap filled` (numbers reproduced above).
- `grep -rn -i "chair\|furniture\|stool\|bed " corpus/knowledge/culture-material/*.md` and the
  per-word runs — the characterisations in §1 (`furniture` 5 files, `chair` 3, `seat` 3,
  `bench` 2, `throne` 2, `cushion` 2, `screen` 2, `cabinet` 1, `stool|mattress|bedstead|canopy|desk` 0).
- `sed -n '47,51p' corpus/knowledge/culture-material/architecture-settlement-lexicon.md` — line 49
  "the kang platform and the matted zashiki are social architecture, not furniture".
- `sed -n '30p;80p;125p' corpus/knowledge/culture-material/architecture-settlement-lexicon.md` —
  lines 30 (*yingbi*), 80 (*kathédra* row), 125 (threshold rites); line 121 read directly.
- `sed -n '13p;126p' corpus/knowledge/culture-material/dress-through-eras.md` — the two seating pointers.
- `sed -n '85,95p' corpus/knowledge/culture-material/trade-economy-lexicon.md` — lines 87, 89, 92;
  `grep -n -i "seat\|cushion\|throne" ...` — line 110 (*za* 座 'seat').
- `grep -n -i "fork\|reclin\|triclinium\|table\|etiquette" corpus/knowledge/culture-material/cuisine-food-lexicon.md` —
  lines 18, 90, 92, 129, 150.
- `grep -n -i "threshold\|doorway" corpus/knowledge/myth-symbol/ritual-liminality.md` — lines 21, 30.
- `grep -rn -i "exchequer\|curule" corpus/knowledge/*/*.md` — `trade-economy-lexicon.md:89` (checkered
  cloth), `adornment-body-codes.md:81` (curule chair).
- `ls corpus/knowledge/verification/to-verify-triage-protocol.md`, `ls reports/round-10/run-validation.py`,
  `ls reports/round-9/metadata/v10-culture.md` — all exist (the draft's two report pointers).
- `grep -n "FRONTMATTER" -A 12 reports/round-27/run-validation.py` — the head-block field regexes
  the draft's frontmatter is written against.
- `ls corpus/knowledge/culture-material/*.md | wc -l` → 18; whole-corpus vector → 21/19/18/29/20/94 = 201.

**External pointers: none resolved this round** (no network in this seat's contract). Every external
work is therefore a record-level citation, and every specific that depends on one carries `(to-verify)`
in place — see the entry's `verified-at` and `recheck` lines. No external source is asserted as read.

## README delta aid (for C11 / the integrator — not a filed artifact)

The README row must be byte-equal to the entry's own `- topic:` text after the em-dash prefix
(the convention recorded in `corpus/README.md` revision notes, e.g. revision 1.9). Generate it from
the landed entry rather than retyping it:

```
python3 -B -c "import re,pathlib;p=pathlib.Path('corpus/knowledge/culture-material/furniture-interior-lexicon.md');m=re.search(r'(?m)^- topic: (.*)$',p.read_text());print('- \`'+p.name+'\` — '+m.group(1))"
```

- Partition header delta for this one entry: `## culture-material/ (18)` → `## culture-material/ (19)`
  (the final `(24)` is C11's arithmetic once all six drafts land; the totals line moves 201 → 211).
- Row placement: filename order inside the `## culture-material/ (…)` section.
- Suggested filename: `furniture-interior-lexicon.md` (partition style: `vessel-container-lexicon.md`,
  `architecture-settlement-lexicon.md`). The integrator may rename; if renamed, the README row
  generator above uses `p.name`, so it stays byte-consistent.

## Contract alignment after the scout batch (applied)

`reports/round-35/scout/K01-coverage-census.md`, `scout/K02-entry-audit-method.md` and
`cov/C12-audit-runbook.md` landed **after** this draft was written; they were read afterwards and
the draft was aligned to them. Deltas applied to the fenced bytes:

- **Gap field renamed** `- gap filled:` → **`- gap: the furniture/interior domain is absent from
  culture-material — this entry fills it`**, the form K01 §3.1/§2.3 recommends and C12's family 4
  blocker leg accepts (`- gap:` is recognised; the measured sweep stays in §1 as K01 §2.3 requires
  a C-author to re-run and record). K01's exemplar order puts `- gap:` first; this draft keeps it
  after `- topic:` — **named deviation**: no instrument reads order (C12 families 1–4 and the
  round-10 legs read field presence anywhere in the file).
- **Boundary clause added to §1** (routed, not absorbed — K01 §3.2 "boundaries are routed"):
  light/fuel/hearth belongs to the fire-fuel-light domain of this wave, bathing/sanitation/water to
  another; no path is cited for either, so the draft creates no dangling pointer (K01 §2.1's one
  corpus-wide dangling ref is `linguistics/phonology-sanity.md`; this draft adds none — checked by
  command over all in-fence repo-path tokens).
- **Stale cross-reference fixed**: §1's method statement pointed at "§12" for the handoff; the entry
  has eleven sections and the handoff note is §11.
- **Dangling in-repo pointer fixed**: a bare `corpus/knowledge/era-periodization-models.md` token
  (the file lives under `culture-material/`) — the only unresolved token of 22 found inside the
  fence; now `corpus/knowledge/culture-material/era-periodization-models.md:6,31`.

Self-reading against C12's runbook families (structural, not a verdict — C12 §1: "a green reading
is a structural reading of the bytes, never a verdict on the scholarship"): 1a/1b five-field
frontmatter present with `couples` satisfying the scope leg; 1c `verified-at` carries an ISO date
and no field is empty; 2 every in-fence repo-path token resolves; 3 `## 9. Decision record — …`
heading present with body; 4 `- gap:` present; 5 no unnegated promotion/clearance/closure words
(word-boundary scan); 6 canon boundary named ("canon decisions are lore-shokunin's", "NON-CANON").

**De-collision evidence (claim C, culture-material, read from the sibling fragments at this seat's
close and re-checked after the later landings):** C01 → mortuary material culture
(`mortuary-material-culture.md`); C02 → agrarian field systems (`agrarian-field-system-lexicon.md`);
C03 → writing media and surface economy; C06 → fire/fuel/light (`fire-fuel-light.md`). None owns
furniture or the interior, so this draft does not duplicate a landed sibling. At this seat's final
re-check, C04 (culture-material) and C09 (myth-symbol) had still not landed — the collision check
must be re-run by the integrator against the final ten drafts.

## Owed

1. **`reports/round-35/plan/P01-c-plan.md` — MISSING at the time this seat ran and still absent
   after the scout batch landed** (checked; `reports/round-35/plan/` contains only `P02-oa-plan.md`).
   P01 owns the 10-topic assignment list and the per-topic gap justification. This seat therefore
   chose its own topic by the K01 method and recorded the choice in the `- gap:` field and §1.
2. **Topic-collision reconciliation (P01 or integrator).** C01–C06 ran in parallel with no shared
   plan. De-collision evidence against the landed siblings is in "Contract alignment" above (C01
   mortuary, C02 agrarian, C03 writing media, C06 fire/fuel/light — none furniture/interior); C04
   was still unlanded at this seat's final re-check. If another culture-material seat authored a
   furniture/interior entry, or if P01's plan assigns this slot a different topic, the integrator
   must keep exactly one entry for this slot and re-route the other — do not land two entries with
   the same domain.
3. **K01/K02/C12 landed mid-run and were read after this draft was written; alignment applied**
   (see "Contract alignment" above). `reports/round-35/review/R09-cross-review.md` independently
   parsed this draft's entry block and counted 31 raw `to-verify` occurrences / 5 parenthesized
   markers (its §2.6 table) — no finding against this fragment was filed by R09 or R02. At
   authoring time both scouts were absent, so this seat ran its
   own absence sweep (§1, commands recorded) and derived the contract from
   `reports/round-27/run-validation.py:179-187`, `corpus/QUALITY.md`, and the committed entries named
   in the fragment header. Residual item: C12's runbook was drafted before these bytes existed, so
   C13/C14 should run its families against the landed entry rather than against C12 §6's per-slot
   expectations.
4. **External-source resolution pass.** No network in this seat's contract, so the record-level
   citations (Richter 1966, Killen, Handler, Ruitenbeek, Thornton, Girouard, Woolgar, Rybczynski,
   Rattray, Wilks, Roberts & Roberts, Dunbabin, OED entries, the V&A Great Bed of Ware record) are
   unresolved and every dependent specific is marked `(to-verify)`. A network-enabled seat
   (C13/C14/R01/R02 auditors or the integrator) should resolve or leave marked.
5. **README row + counts (C11)** — the generator command above; not executed by this seat because
   `corpus/README.md` is not this seat's write target and the entry has not landed.

## Citations

- `reports/round-35/claims.json` (claim C: before-counts, after_required, thresholds, non_goals).
- `reports/round-35/targets.json` (seat C05: mission "Author entry 5 (culture-material) with the
  same contract"; `out: cov/C05-entry-5.md`; `shared_rules`).
- `REGIMEN.md` (round contract, per-round rules, scope).
- `AGENTS.md` (lane rules: in-repo only, no fabricated sources, canon decisions are lore-shokunin's).
- `corpus/QUALITY.md:1-22` (the admission bar: provenance, calibration, coupling, usability, canon hygiene).
- `reports/round-27/run-validation.py:179-187,1556-1561` (FRONTMATTER regexes; the
  "not frontmatter-complete" failure text) and `:186-190` (decision-record, gap-named,
  source-citation, canon-claim regexes).
- `corpus/knowledge/linguistics/register-strata-attestation.md:1-10` (head-block shape: `topic`,
  `gap filled`, `sources` with per-locator sha256, then `couples`/`verified-at`/`recheck`).
- `corpus/knowledge/culture-material/vessel-container-lexicon.md` (read in full: the partition's
  section shape, gap-sweep table, decision-record table, handoff note).
- `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:3,30,34,49,80,121,125`
  (sources line; *yingbi*; threshold furniture; the "not furniture" clause; *kathédra*; "Government
  is furniture"; threshold rites).
- `corpus/knowledge/culture-material/dress-through-eras.md:13,126` (seating and dress evolve together;
  commit seating/posture/architecture).
- `corpus/knowledge/culture-material/adornment-body-codes.md:81` (curule chair; "who may sit").
- `corpus/knowledge/culture-material/trade-economy-lexicon.md:87,89,92,110` (bench→bank;
  checkered cloth→Exchequer; tally→stock; *za* 座 'seat'→guild).
- `corpus/knowledge/culture-material/cuisine-food-lexicon.md:18,90,92,129,150` (service transition;
  §6 the table as grammar; Elias place settings; commensality *com+mensa*; fork-legend calibration).
- `corpus/knowledge/culture-material/vessel-container-lexicon.md:4,97` (its in-repo receipts and
  the "kiln furniture" use).
- `corpus/knowledge/culture-material/era-periodization-models.md:6,31` (the Japanese cabinet as a
  constitutional organ).
- `corpus/knowledge/culture-material/ritual-garments.md:21` (the vestry as a liminal room).
- `corpus/knowledge/myth-symbol/ritual-liminality.md:21,30` (threshold phases; the marriage threshold).
- `corpus/knowledge/verification/to-verify-triage-protocol.md` (exists; the routing procedure for
  every mark in the draft).
- `reports/round-9/metadata/v10-culture.md` and `reports/round-10/run-validation.py` (exist; the
  in-repo receipts the draft points at).
- Commands (all run 2026-10-19 in the lane root, HEAD `4a7aede`): the partition sweep loop;
  `grep -ril` per-keyword file lists; `grep -o -i "table"` counts (108 partition-wide, 16 in
  cuisine); `grep -c "^|"` (793 pipe-rows); `sed -n` reads of the lines listed in the pointer
  resolution record; `ls` checks; `git rev-parse --short HEAD` → `4a7aede`;
  `git status --porcelain` → `?? reports/round-35/` only.
- Post-scout alignment reads (2026-10-19, after this draft was written; used by the "Contract
  alignment" section): `reports/round-35/scout/K01-coverage-census.md` (§1.3 header-block census,
  §1.4 README reconciliation rules, §2.2 ownership test + limits, §2.3 culture-material candidate
  gaps, §3.1–3.6 entry shape contract), `reports/round-35/scout/K02-entry-audit-method.md`
  (§2.1 the round-10 legs, §2.3 head-field census and the "no literal `- scope:`" reading, §3
  defect classes D1–D8, §4.2 README delta anchors), `reports/round-35/cov/C12-audit-runbook.md`
  (§1 check families 1–6 and their tiers, §2 the scope-leg ruling), and the sibling draft heads
  `reports/round-35/cov/C02-entry-2.md`, `cov/C03-entry-3.md`, `cov/C06-entry-6.md`,
  `cov/C11-readme-delta.md` (de-collision and row-convention cross-check).
