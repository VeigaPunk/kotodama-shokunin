# Footwear — what the foot wears, who may wear it and where it comes off: shoes, sandals, boots and clogs as a worldbuilding surface

- topic: footwear as costume and material culture for fictional cultures — the shoe as made object (material, construction, maker), as rank and law (height, toe, colour), as rule of place (thresholds where shoes come off), as gesture (the shown or thrown sole) and as myth object (winged sandals, the slipper test), with one opened source per cited line
- gap filled: at the round base `942abdf4` no file under `corpus/knowledge` owns footwear. Filename sweep `git ls-tree -r --name-only 942abdf4 corpus/knowledge | grep -ciE 'footwear|shoe|sandal'` → 0; topic-line sweep `grep -rlE '^- topic:.*(footwear|shoe|sandal)' corpus/knowledge` → 0. Partial mentions in other entries are pointed to one-way in §1.
- sources: external shelf opened this round (2026-10-23) by ordinary means only (plain requests, public copies and Wayback captures; a challenge met was not passed), registered in `corpus/SOURCES.md` as round-61 rows; every cited bullet in §3 carries exactly one row id and restates only what that row's quoted passage says.
- couples: culture-material — `costume-semiotics.md` (owns dress as a sign system; this entry takes only the foot), `dress-through-eras.md` (owns period silhouettes), `sumptuary-law-rank-display.md` (owns rank law in general; this entry keeps only rules that name footwear), `adornment-body-codes.md` (owns marks on the body itself), `ritual-garments.md` (owns garment-as-office), `warrior-material-culture.md` (owns armour and kit), `craft-artisan-lexicon.md` (owns workshop registers in general); synthesis — `worldbible-integration-contract.md` (the lore handoff).
- source: lane-side authority is the row list in §3. Design method: decide what the ground and climate demand first, then who makes the shoe and from what, then what it says about rank, then where it must come off, then what a shown or thrown sole means, and last which shoe the culture's stories remember.
- verified-at: 2026-10-23 — written against the lane worktree on the round-61 instruments `78ad4b17`; pre-entry knowledge files 235, post-entry 236, measured by `python3 -B reports/round-61/accept-c.py`.
- recheck: 180 days, per row (`corpus/SOURCES.md` recheck cells).
- scope: reference method and lane policy for the culture-material partition. It records what the cited pages say about real footwear as design anchors; it decides nothing about what is true in any world (canon belongs to lore-shokunin) and makes no ruling on any real-world collection, ownership or display question (PROVINCE.md).

## 1. Partial owners (pointed to one-way)

One-way pointers (this entry restates none of them; ScoutOwners, `.ufo/waves/round-61/w1/ScoutOwners.md`):

- `culture-material/costume-semiotics.md` — dress as a sign; shoes appear as a class detail.
- `culture-material/garment-lexicon-crosslinguistic.md` — wardrobe naming; shoes counted as a pair.
- `culture-material/ritual-garments.md` — vestments, including shoes-off separation at sacred places.
- `culture-material/sumptuary-law-rank-display.md` — rank law in general; graded footwear appears inside it.
- `culture-material/craft-artisan-lexicon.md` — workshop registers, including the shoemaker's.
- `culture-material/architecture-settlement-lexicon.md` — the house threshold where shoes come off.
- `civilizations/japan-edo.md` and `civilizations/ancestral-puebloan.md` — single-tradition footwear notes.

## 2. Six design decisions

| decision | question the culture answers | what to record for the handoff |
|---|---|---|
| ground and climate | which surfaces the foot meets (sand, snow, mud, stone floors, paddy) and in which season | the default shoe per terrain and the barefoot exceptions |
| material and making | who makes footwear, from what (bark, fibre, hide, wood, textile), and how it is assembled | the maker's title, the material chain and the construction words |
| rank and law | whether height, toe length, colour or material is reserved to a rank, office or sex | each reserved feature, its holder and its penalty, if any |
| rules of place | which thresholds require shoes to come off (house, shrine, palace) and where they are left | the threshold list and the storage place |
| gesture | what showing, throwing or touching with a sole means | the gesture, its insult level and who may answer it |
| story objects | which shoes the culture's myths, tales or rites remember | the object, its owner in the story and what it proves or grants |

## 3. Attested anchors (one source per line)

### Oldest shoes, materials and making

- The Areni-1 shoe was stuffed with loose grass without clear orientation. (S652)
- Great Basin sandals were woven from sagebrush bark and other fibers. (S653)
- On Fort Rock sandals, interlocking loops at the sole edge near the heel formed the tie system. (S654)
- To keep his feet warm in the snow, the Iceman stuffed hay into his shoes. (S655)
- Ötzi’s shoes joined a bearskin sole to deerskin upper leather with a thin cowhide strap. (S656)
- Iron studs joined the leather layers making up a Roman shoe’s sole. (S657)
- Vindolanda's shoe collection includes tiny baby booties, elaborate summer sandals and marching boots. (S658)
- An Oklahoma Shawnee moccasin record lists elk hide, hide thong and paint, sewn and painted. (S671)
- Peasant bast shoes were woven from vine or linden bast. (S683)
- In Russia, woven birch-bark shoes are known as lapti. (S684)
- The museum’s collection includes an opančar workshop for making traditional leather opanci. (S679)
- A Serbian child's pair of opanci has soles attached to the uppers with knotted leather thongs. (S680)
- The museum presents clogmaking through specialized machinery dating from 1920. (S689)

### Terms and types

- Traditional Japanese footwear is roughly divided into zori sandals and geta wooden clogs. (S667)
- Geta, elevated relative to zori, became fashionable in urban areas during the Edo period. (S668)
- Northern Plains moccasins are both practical and stylish footwear. (S672)
- The caption lists Nêhiyawak moccasins dated 1920 as a gift of the Art Association of Montreal. (S673)
- A child's kamik made over 2,500 years ago is among the oldest footwear found in the Canadian Arctic. (S674)
- A wooden patten was an overshoe worn to raise the foot above ground in wet weather. (S685)
- A patten was worn over a pair of normal shoes. (S686)
- The word sabotage borrows from French, whose root sabot literally means a wooden shoe or clog. (S691)
- A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, and Belgium. (S692)
- A V&A ritual object also has the knobs of sandals (paduka) protruding between the toes. (S678)

### Rank, law and display

- A poulaine is a medieval man’s shoe with a long pointed toe. (S659)
- Sumptuary laws regulated how long a person's poulaines could be, according to their station. (S660)
- Higher chopines hidden under skirts required more dress cloth and signaled status. (S661)
- The high-platformed chopine had practical and symbolic functions and was especially popular among Venetian women. (S662)
- The red heels and soles of latchet shoes were associated with Louis XIV and his court. (S663)
- Louis XIV made red-heeled shoes the preserve of the nobility by regulation. (S664)
- A heel originated in Western Asia for horseback riding before Europeans adopted it. (S665)
- The earliest evidence of someone wearing heels comes from a 10th-century Persian bowl. (S666)
- A V&A pair of 19th-century shoes was made for bound feet and embroidered with a peach blossom motif. (S675)
- Dorothy Ko curated an exhibition about women’s shoes in Late Imperial China (S676)
- A bride might receive toe-knob paduka among the often extravagant presents. (S677)
- The clog museum shows bridal clogs, work clogs and church clogs from Hindeloopen dating back to 1675. (S690)

### Rules of place

- Japan's footwear-removal custom for entering a home extends to ryokan inns, temples, and restaurants with tatami-floored rooms. (S669)
- Mosque visitors are asked to remove their shoes before entering the prayer hall. (S670)

### Gesture: the shown sole

- In Arab culture it is considered rude even to display the sole of one's shoe to another person. (S681)
- Deliberately displaying shoe soles is considered indecent in Arab society. (S682)

### Story objects

- Hermes' talaria were winged leather boots. (S687)
- Mercury's sandals in art have wings fastened on each side above the ankles. (S688)

## 4. Craft checklist

- Name the default shoe of each social layer before naming any special shoe.
- Give every rank-marking shoe feature a holder, a rule and a way the rule is broken.
- Put at least one threshold where shoes come off, and decide who guards it.
- Keep the maker in the world: a title, a workshop and a material supply.
- Decide whether a sole is an insult before a scene shows one.
- Let one shoe carry a story, and keep its proof function (fit, flight, travel) explicit.

## 5. Lore handoff

This entry hands lore-shokunin design questions and real-world anchors only. Any footwear rule adopted in a world is recorded and checked by lore through `corpus/knowledge/synthesis/worldbible-integration-contract.md`; this entry never records it as canon.
