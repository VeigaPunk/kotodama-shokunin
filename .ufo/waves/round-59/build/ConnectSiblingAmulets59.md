# ConnectSiblingAmulets59 — sibling-lane overlap scan for claim C

Seat: `KotodamaR59.ConnectSiblingAmulets59` (leaf, read-only outside my report).
Lane HEAD observed (read-only `git rev-parse HEAD`): `5ed5b8e0aaacb146ac8cee027ac9bf50bc691b17`
("round-59: freeze dry-run receipt at ff802cc3 and build wave spec (before any data seat)").
Installs: none. Processes: none left running.

## 0. What was scanned (read-only)

Every sibling lane under `/home/vgpnk/Projects/shokunin/*-shokunin` except `kotodama-shokunin`
(20 lanes: audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku,
kotoba, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi).

```
grep -rniE '\b(amulets?|talismans?|apotropaic|phylacter\w*|charm|charms|fetish|relics?|magic(al)?|spells?|enchant\w*|ward(ing)?|curse[sd]?|blessed|sacred|ritual|superstit\w*|taboo|omen|divination|items?|inventory|equipment)\b' \
  <lane>/corpus/knowledge <lane>/PROVINCE.md <lane>/SKILL.md
grep -rliE 'amulet|talisman|apotropai|phylacter' --include='*.md' --include='*.json' --include='*.py' --include='*.ts' --include='*.js' <lane>/
grep -rniE 'religio|folklore|mytholog' */corpus/knowledge   (siblings only)
```

Result: **no sibling lane owns the topic.** All non-zero hits are vocabulary homonyms, inspected
and ruled out (§1.2). The only boundary-bearing neighbours own *containers* (canon records, engine
fixtures, research method), not *content* about protective objects.

Lane status at scan start (`git status --porcelain`, read-only): ` M corpus/SOURCES.md` and
`?? .ufo/waves/round-59/build/` — not mine; I wrote only this report file. `SOURCES.md` was already
modified when I began, so row ids/anchors cited here are the ones I read, not the landed set.

## 1. Cross-lane overlaps and the boundary rule each imposes

### 1.1 Neighbours that carry a real boundary

| Overlap (path:line) | What that lane owns | Boundary rule the amulets entry should state |
|---|---|---|
| `lore-shokunin/PROVINCE.md:3` — "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification" | which named item exists in a world, its relations, its chronology | kotodama owns the **design grammar** of a protective object (type word, threat class, material logic, placement, maker authority, inscription class, change over time); lore owns **which amulet exists, who bore it, and when**. The entry never asserts a specific world's amulet. |
| `lore-shokunin/corpus/knowledge/seed.md:9` — "`entities.json` — every entity: {id, kind (character\|place\|faction\|item), name, first_appearance (source id), claims: [{statement, source_id}]}" and `:15-16` — "Every claim carries a source_id; a claim without one is flagged `invented` and must never be presented as canon." | the entity schema and the `invented` flag | hand **slots and rules, not filled claims**. A sentence shipped as a `claims[]` statement without an in-world `source_id` is not merely out of province — lore's own gate pre-marks it fabricated. |
| `lore-shokunin/corpus/knowledge/r87-provenance-chain-decision-table.md:39` — "`provenance` on a non-item entity \| `entities[0].provenance: only valid on item entities`" | the custody/acquisition chain (`provenance` only on `kind: item`) | the entry may state that a transfer of custody can carry the power claim; it hands the chain to lore and never invents acquisition events. |
| `lore-shokunin/corpus/README.md:73` — "CM-g \| intake of kotodama handoff packets \| uncovered" and `:79` — "contract `kotodama-lore-adjacency` sits at unacknowledged digest 5f4c02bf… and lore holds zero durable-surface acknowledgement records." | the intake gate, which is **uncovered** | do not write "lore records this" or imply a live channel. Use the heraldry formula: submission, delivery and silence are never acceptance (`synthesis/worldbible-integration-contract.md:129`), and name CM-g as uncovered. |
| `lore-shokunin/corpus/knowledge/r88-sourced-inspiration-decision-table.md:12` — "A real-world work, tradition, or specific historical/mythological claim" (R8/R9 admission rows) | the path by which a real-world work becomes admissible inspiration | this entry's real-world amulet evidence stays **row evidence in kotodama's registry**; it reaches canon only through lore's R8/R9 path. No real-world amulet becomes an in-world one by citation. |
| `game-dev-2d-shokunin/PROVINCE.md:3` — "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." + `:10` refuses "asset rights clearance (art-east-asian-design)" + `:31-32` "narrative canon → lore" | mechanics, verified by fixtures | the entry supplies **no stat, slot, drop table or buff**. If a world turns an amulet into an item, the mechanics belong to game-dev-2d and the canon to lore; kotodama stops at the symbolic rule. |
| `game-dev-3d-shokunin/PROVINCE.md:3-12` (3D mechanics, Godot/Unity/Unreal/three.js, "headless determinism") + `:34` refuses "asset rights clearance" | 3D mechanics and engine fixtures (incl. Unreal GAS toolset coverage) | no ability-system, GAS or spell-effect design. The entry's "what it protects against" is a cultural claim, not a mechanic. |
| `chousa-shokunin/PROVINCE.md:5-8` — "Owns: question framing; source hierarchy (primary / secondary / aggregator / unsourced); citation chaining and hop resolution; claim-vs-source verification; search-strategy taxonomy" | research method | the entry cites at row level under kotodama's own `corpus/SOURCES.md` + FETCH-59 discipline and **teaches no source hierarchy**. A row's tier is evidence about that row, not method instruction. |
| `lore-shokunin/PROVINCE.md:29` — "game-dev-2d — mechanics verification, refused by this lane" (same refusal at `game-dev-2d-shokunin/PROVINCE.md:10`) | the two-way refusal already in force | do not re-open mechanics or canon in this entry; the adjacent contract is one-way, kotodama → lore, and it is load-bearing (`PROVINCE.md:22-25`). |
| `kotodama-shokunin/PROVINCE.md:16-20` — "Refuses: claiming or recording canon … real-world rights/attribution rulings on reference works; game mechanics (game-dev-2d/3d); general source-research method (chousa); web publishing (kake)" | the lane's own refusal list | the entry's boundary section is a **restatement of refusals with named destinations**, not a new claim of authority. |

### 1.2 Ruled out — no overlap despite matching words

| Lane / path:line | Why it is not an owner |
|---|---|
| `kaidoku-shokunin/.../libsigrokdecode-0.5.3/decoders/amulet_ascii/pd.py`, `.../site-packages/pip/_vendor/rich/_emoji_codes.py` | "Amulet" is a **serial protocol** in a signal decoder; the emoji table is Unicode data. Fleet-wide `grep -ril amulet` finds these first — a naive sweep would report phantom owners. |
| `game-dev-2d-shokunin/corpus/knowledge/2026-10-12-production-checklist.md:13` ("canvas item updates") | Godot `CanvasItem` API, not an inventory item. |
| `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/*` ("inventory", "spells every path", "Gameplay Ability System") | a **tool census** of the Unreal MCP surface; no item or magic doctrine. |
| `kumitate-shokunin/corpus/knowledge/cost-and-profile.md:311-313` ("charm-hyper") | a model alias. |
| `kama-shokunin/corpus/knowledge/alias-endpoint-normalization.md:11` ("charm-hyper/deepseek-v4.1-flash:max") | same alias in a routing table. |
| `mori-shokunin/.../drift-pin-r10.md:235`, `kake-shokunin/.../keeper-timer-inert.md:182` | "admission ritual" = process rite; "inventory" = file census. |
| `kaidoku-shokunin/PROVINCE.md` (52 hits) | "artifact", "magic" (file magic bytes), "symbols" (ELF symbols) in reverse engineering. |
| `kengaku`, `kotoba`, `tabi`, `tameshi`, `tsukuroi`, `audio`, `souji`, `revenger`, `kagi`, `mado`, `kasegi` | their hits are "N-item checklist", "inventory" in the census sense, or model data. No religious or protective-object content. |

### 1.3 The absent owner — do not add a fourth pointer

Three lanes delegate a rights question to a lane that does not exist in the roster:

- `lore-shokunin/PROVINCE.md:9` — "real-world rights claims (art-east-asian-design)", corrected at `:33` — "the refusal line above names `art-east-asian-design`, a lane absent from the fleet roster — from the fleet root, `grep -c 'art-east-asian' MANIFEST.json` → 0."
- `game-dev-2d-shokunin/PROVINCE.md:10`, `:32`.
- `game-dev-3d-shokunin/PROVINCE.md:34`.

I re-ran the census: `grep -c 'art-east-asian' MANIFEST.json` → **0**.

**Boundary rule:** the amulets entry must **not** write "rights/permission → art-east-asian-design". Protective objects carry living formulae and living community marks (Ketef Hinnom's priestly-blessing wording, dhāraṇī, khamsa pendants). Handle the rights question inline, in the shape
`myth-symbol/heraldry-emblems-identity-marks.md:154` already uses — the entry goes no further than what holding museums and publishers state, and adjudicates nothing. Adding a fourth dangling lane pointer would be a new defect, not an adjacency.

## 2. In-lane partial owners the entry must point to one-way (§2 table, paste-ready)

Format copied from `myth-symbol/heraldry-emblems-identity-marks.md:18-34` (`## 2. One-owner boundary`).
Every anchor below was re-read at lane HEAD `5ed5b8e`.

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `myth-symbol/mineral-stone-symbolism.md:5` (lithic register) and `:175` ("Precious stones are universal talismans" \| **discredited** as a universal) | stone meanings and the lapidary form | owns stone as **one material slot**; never a virtue list, never a universal stone power |
| `culture-material/adornment-body-codes.md:20` (Roman *bulla* as a freeborn boy's amulet; jewelry-as-document) | body codes, portable wealth, signet/intaglio | owns the wealth/rite ledger and the body substrate; the entry owns the protective function and its removal rule |
| `culture-material/ritual-garments.md:118` (bulla doffed at the toga virilis) | lifecycle dress and its changes | owns the lifecycle garment; the entry owns the amulet's own surrender point |
| `myth-symbol/binding-speech-complex.md:164` (*voces magicae*, counter-curse and defense) | efficacy of the spoken/written word | owns the word's force; the entry owns the object that carries words |
| `culture-material/warrior-material-culture.md:110` (bonji seed-syllables lacquered on armor, "apotropaic grammar on the body") | war gear and its inscriptions | owns combat carriers; the entry compares and returns there for armour |
| `culture-material/craft-artisan-lexicon.md:121` (the hidden build-curse, "apotropaic or hostile") | who builds, guilds and craft rites | owns the maker trade; the entry owns **maker authority as a design role** |
| `culture-material/writing-media-surface-economy.md:112` (seal matrix vs impression) | authentication and writing surfaces | owns authentication; the entry owns the class of protective text, not its legal force |
| `culture-material/vessel-container-lexicon.md:90` (Egyptian faience "NOT clay"; "Egyptian amulets and vessels") | material identity of containers | owns the material name; the entry does not re-derive faience |
| `myth-symbol/number-symbolism.md:60` (Luoshu 3×3 magic square, "every line sums 15") | the arithmetic square | owns the square as number form; the entry owns its **apotropaic use** and does not restate the sums |
| `myth-symbol/sacred-topography-pilgrimage.md:90` (site "souvenir-taking") | pilgrimage sites, custodianship, site souvenirs | owns site souvenirs and custodian change; the entry owns **amulets as commodities** generally |
| `myth-symbol/color-symbolism.md:79` ("China, the luck/protective complex") | colour meanings by term and carrier | owns hue meanings; the entry owns colour only as a **material choice** in a cited direction |
| `myth-symbol/divination-omen-systems.md:102` ("Prescription as the output") | omen reading and its prescribed action | owns the reading and the action; the entry owns the object manufactured after it |
| `myth-symbol/death-afterlife-eschatology.md:91` (the unclean dead) | the dead, their classes and treatments | owns the dead; the entry owns the object used against them |
| `myth-symbol/purity-pollution-boundary-systems.md:29` (`inside / outside \| crossing the group's threshold \| … \| gates, thresholds, and a boundary office`) | the purity boundary map and the boundary office | owns the boundary/danger frame and who polices it; the entry owns the **physical mark and object** placed at the threshold |
| `synthesis/symbolism-consistency-rules.md:154` ("Check carriers and access: … wearer authorization, counterfeit recognition, and reader knowledge remain separate") | the audit of rendering, authorization, counterfeit | supplies amulet inputs to that audit; **no second checklist** |
| `synthesis/worldbible-integration-contract.md:129` ("Submission, delivery, and silence are never acceptance") | the handoff contract | §14 hands off; lore decides which amulet exists |
| `myth-symbol/heraldry-emblems-identity-marks.md:18` | the one-owner table **shape** | copy the shape, not the content; no emblem rules restated |

Dated local instances (cite as contrast, never as the rule): `civilizations/israel-ancient-hebrew.md:108`
(Ketef Hinnom silver amulets, "protective inscriptions containing the divine name"),
`civilizations/egypt-ancient.md:96` (wedjat, "amulet manufacture"),
`civilizations/amazigh-berber.md:100` (hand pendants, khamsa),
`civilizations/germanic-norse.md:65` (protective formula / inscribed amulet),
`civilizations/china-tang.md:126` (sutra copying, dhāraṇī, Daoist talismans),
`civilizations/burma.md:72` (Spiro's "apotropaic" category),
`civilizations/carthage.md:143` (amulets in urn processing; "a deposition is not a complete outfit").

### 2.1 Coverage facts that force first ownership (not pointers)

Verified at HEAD `5ed5b8e` with `grep -rilF` over `corpus/knowledge`:

- `evil eye` → **no files**; `evil-eye`, `nazar`, `omamori`, `ofuda`, `mezuz`, `tawiz`,
  `incantation bowl` → **no files**. `hamsa` appears only at `civilizations/amazigh-berber.md:100`
  (as *khamsa*) and as a homonym in `culture-material/cuisine-food-lexicon.md`.
- `magic square` → `myth-symbol/number-symbolism.md:60` only; `souvenir` →
  `myth-symbol/sacred-topography-pilgrimage.md:90` only.

Consequence: the evil-eye complex, the inscription-class ladder and the commodification arc have
**no partial owner in the lane**. They must be carried by the entry's own §rows (S600-S659); pointing
at a non-existent owner would fail a blind reviewer on the teaches cell.

## 3. Affected axes

- **C — coverage (primary).** The §2 table converts 17 "passing mentions" into a declared boundary,
  which is what the blind SUPPORT reviewer reads against "never overgeneralise one culture's practice
  into a universal". It adds no rows, no sources, no files.
- **Adjacency (judged).** Every neighbour named here is a real file at a verified line; the two
  documented refusals (canon, mechanics) are restated with their owning lanes instead of absorbed.
- **D — depth: untouched.** D's targets are `corpus/knowledge/civilizations/kongo-kingdom.md`
  (14 sentence replacements) and `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`
  (5 id remaps S135→S570 … S159→S574, `reports/round-59/d-fixes.json`). Nothing in §2 above points
  into either file — see risk R2 for why that is deliberate.

## 4. Proposed move (one, bounded)

**Make §14 a payload table keyed to lore's real schema, whose unit is the decision slot and whose
carrier is never the inscription's wording.**

Paste-ready shape (compare `myth-symbol/heraldry-emblems-identity-marks.md:156-168`):

| Payload | Packet field and lore's reserved decision |
|---|---|
| what the object is called | a name candidate for `entities[].name`; lore sets the in-world word (`seed.md:9`) |
| what it protects against | a design statement for `scope`, **never** a `claims[]` entry — an unsourced claim is flagged `invented` (`seed.md:15-16`) |
| material and colour logic | the rule and its exceptions, with the row that grounds them; lore decides the actual object |
| placement (body, child, threshold, animal, vehicle) | the placement slots; lore decides which building, animal or person |
| who makes, blesses or sells | role names and the authority relation; lore decides which institution exists and what it may enforce |
| inscription class (name, verse, square, seal, mark) | the **class only**; the wording itself is not transferred. If a world needs words, they come from lore's in-world `sources.json` document or the lane's conlang surface — never from a real-world source's text |
| custody and transfer | nothing; `provenance` is valid only on item entities (`r87…:39`) and lore owns the chain |
| change over time (reform, commodification, souvenir) | an era-scoped design note; lore decides when it changed in-world |

Then one sentence: *Submission, delivery and silence are never acceptance
(`synthesis/worldbible-integration-contract.md:129`); lore's intake gate CM-g is uncovered with no
acknowledgement record (`lore-shokunin/corpus/README.md:73,79`), so this section transfers nothing.*

Why this is the non-obvious move rather than a copy of heraldry: heraldry's payload rows are
*bearer-shaped* (who bears, who grants). An amulet's payload is *word-shaped*, and the lane's evidence
for protective inscriptions is real-world published translations of living sacred text. Shipping the
words would (a) put an in-copyright translation into canon, (b) trip lore's `invented` flag for every
sentence kotodama cannot source in-world, and (c) create a fourth dangling pointer if the rights
question is delegated. Keying the table to `seed.md:9` / `r87…:39` / `contract:129` turns all three
into one refusal sentence with a named destination.

## 5. Risks

- **R1 — the refusal can read as a rights ruling.** "Do not transfer the wording" is a scope refusal,
  not a legal opinion; lore `PROVINCE.md:9` refuses rights claims and that lane does not exist for
  them anyway (`:33`). Phrase it as *this entry does not carry the text*, and cite heraldry's
  holding-museum sentence (`:154`, §13 "Restricted and living marks") as precedent.
- **R2 — same-wave anchor hazard (C vs D).** C and D land in one wave. `kongo-kingdom.md` takes 14
  sentence replacements and `speech-surrogates-whistled-drummed.md` takes 5 id remaps
  (`S135→S570`, `S141→S571`, `S147→S572`, `S151→S573`, `S159→S574`). Any `path:line` or `S1xx`
  written into the amulets entry before D applies can go stale. The §2 set above deliberately avoids
  both files; if the entry wants the "word as protection" comparison it points at
  `myth-symbol/binding-speech-complex.md:164`, which D does not touch.
- **R3 — anchor drift on the 17 in-lane rows.** Every line was read at `5ed5b8e`; a later landing
  revision shifts them. Re-read the anchor set immediately before writing the entry (cheap: the
  checker in §6), or cite the section heading instead of `:line` where the line is not load-bearing.
- **R4 — gap-filled sweep must be lane-scoped.** A fleet-wide `grep -ril amulet|talisman` returns
  only vendored noise: sigrok's `amulet_ascii` decoder (4 files under `kaidoku-shokunin/.ufo/…`),
  pip's `_emoji_codes.py`, `solc/soljson.js`, `graphemer/lib/Graphemer.js` — never a sibling
  `corpus/knowledge` file. A fleet-wide sweep would print those as phantom owners. Keep the
  sweep that the predicate and the header use:
  `git ls-tree -r --name-only <base> corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` → 0.
- **R5 — do not promise a channel.** The handoff section must not say lore "will record" anything;
  CM-g is uncovered and the contract digest is unacknowledged (`lore-shokunin/corpus/README.md:79`).
- **R6 — breadth vs decision.** 17 anchors look like authority but only the ones that would otherwise
  duplicate (stone, body, word, maker, number, colour, site souvenir, audit) carry a decision; the
  dated civilization rows are contrast only. Keep them in a separate sentence so a reviewer does not
  read them as ownership.

## 6. Verification (what the L1 can run)

```
# 1. gap proof, lane-scoped (must print 0 for each)
grep -rilF 'evil eye' corpus/knowledge; grep -rilF 'nazar' corpus/knowledge
grep -rilF 'omamori' corpus/knowledge; grep -rilF 'ofuda' corpus/knowledge
grep -rilF 'mezuz' corpus/knowledge; grep -rilF 'incantation bowl' corpus/knowledge

# 2. anchor table integrity — every path:line must still contain its phrase
python3 - <<'PY'   # run from the lane root
import re,sys
rows=[("myth-symbol/mineral-stone-symbolism.md",175,"discredited"),
      ("culture-material/adornment-body-codes.md",20,"bulla"),
      ("culture-material/ritual-garments.md",118,"bulla amulet doffed"),
      ("myth-symbol/binding-speech-complex.md",164,"Counter-curse and defense"),
      ("culture-material/warrior-material-culture.md",110,"Worn speech"),
      ("culture-material/craft-artisan-lexicon.md",121,"hidden build-curse"),
      ("culture-material/writing-media-surface-economy.md",112,"seal / impression"),
      ("culture-material/vessel-container-lexicon.md",90,"Faience"),
      ("myth-symbol/number-symbolism.md",60,"magic square"),
      ("myth-symbol/sacred-topography-pilgrimage.md",90,"souvenir-taking"),
      ("myth-symbol/color-symbolism.md",79,"luck/protective complex"),
      ("myth-symbol/divination-omen-systems.md",102,"Prescription as the output"),
      ("myth-symbol/death-afterlife-eschatology.md",91,"unclean dead"),
      ("synthesis/symbolism-consistency-rules.md",154,"Check carriers and access"),
      ("synthesis/worldbible-integration-contract.md",129,"never acceptance"),
      ("civilizations/israel-ancient-hebrew.md",108,"Ketef Hinnom"),
      ("civilizations/egypt-ancient.md",96,"Wedjat"),
      ("civilizations/amazigh-berber.md",100,"khamsa"),
      ("civilizations/germanic-norse.md",65,"Protective formula"),
      ("civilizations/china-tang.md",126,"dh"),
      ("civilizations/burma.md",72,"apotropaic"),
      ("civilizations/carthage.md",143,"Amulets/small objects")]
bad=[f"{p}:{n}" for p,n,s in rows
     if s not in open("corpus/knowledge/"+p,encoding="utf-8").read().splitlines()[n-1]]
print("ANCHORS FAIL" if bad else "ANCHORS PASS", bad)

# 3. no dangling art-lane pointer introduced
grep -c 'art-east-asian' corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md   # expect 0

# 4. no pointer into D's two files
grep -nE 'kongo-kingdom|speech-surrogates' corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md  # expect none
```

The frozen predicate itself (`python3 -B reports/round-59/accept-c.py`) stays the L1's run; nothing
in this report changes a row, a URL, a tier or the entry path.
