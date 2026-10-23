# ScoutOwners — claim C footwear partial owners

Seat: KotodamaR61.ScoutOwners. Recon only. No lane edits except this report. No installs.

Axes: (1) partial-owner coverage, false hits dropped; (2) header contract fidelity to `masks-masquerade.md` lines 1–12; (3) README index arithmetic (section header, filename-order row, totals line, counts footer).

Revision pin named by the wave: `78ad4b176695e9fcd490ab607cb8218e2ce62738`. `reports/round-61/claims.json` `round_base` is `942abdf4f94f82a8372c5b550adb8241aa79c467`. This seat did not re-run `find` or `source-audit-inventory.py`.

## Ownership verdict

No file under `corpus/knowledge` owns footwear as a cross-cultural system.

- Filename: `corpus/knowledge/culture-material/` lists 29 files; none is `footwear` / `shoe` / `sandal`. A name-fragment glob over `corpus/knowledge` returned no match. Not a `git ls-tree` recount. Claim C's unmoved command is still the counter's job.
- Topic line: `^- topic:.*(shoe|sandal|boot|footwear|clog|moccasin|geta|zori|slipper)` hit only `myth-symbol/plant-symbolism.md:4`, and that hit is the substring `geta` inside `vegetation-deity`. Word-boundary re-read of that line: no footwear word. **Zero topic-line owners.**

Word-boundary content sweep (`\b(shoes?|sandals?|boots?|footwear|clogs?|moccasins?|geta|z[oō]ri|slippers?|heels?|…)\b`, case-insensitive) over `corpus/knowledge`: 45 files, then filtered. **55 real hits** below. Zero hits in `linguistics/`, `verification/`, `dress-through-eras.md`, `textile-technology.md`, `adornment-body-codes.md`.

## Excluded (not footwear dossiers)

- `culture-material/craft-artisan-lexicon.md:37` — chisel *heel* is tool anatomy.
- `culture-material/garment-lexicon-crosslinguistic.md:46` — German *Handschuh* 'hand-shoe' is a glove calque. Same file's `:76` is real and kept.
- `culture-material/warrior-material-culture.md:53` — "spurs hacked from his heels" is the anatomical heel in a degradation rite, not a shoe dossier.
- `myth-symbol/plant-symbolism.md:4` — `geta` inside `vegetation`.
- `reboot` / `bootstrap` / `wheel` do not match `\bboot\b` / `\bheel\b`. Not listed.

## Real hits (path:line — six-word gist)

Paths relative to `corpus/knowledge/`.

### civilizations/ (38)

- `akan.md:126` — court sandals join gold display
- `akan.md:150` — sandals stage performance of office
- `algonquian.md:167` — hide moccasins for winter travel
- `algonquian.md:169` — notched moccasin patterns differ locally
- `algonquian.md:170` — floral moccasin-front is personal repertoire
- `anatolia-hittite.md:135` — relief gods wear characteristic footwear
- `anatolia-hittite.md:143` — footwear materials left to-verify
- `ancestral-puebloan.md:14` — NPS gallery documents yucca sandals
- `ancestral-puebloan.md:151` — winter reconstruction includes warm footwear
- `ancestral-puebloan.md:152` — yucca sandals linked to cordage
- `burma.md:132` — dress checklist slot includes footwear
- `china-qing.md:131` — one shoe cannot settle ancestry
- `china-tang.md:137` — riding styles include trousers boots
- `egypt-ancient.md:152` — do not erase Egyptian footwear
- `etruria.md:117` — archaic images show distinctive footwear
- `etruria.md:136` — calcei repandi names upturned footwear
- `germanic-norse.md:155` — calfskin shoes specify ceremonial dress
- `greece-classical.md:138` — dress grammar ends in footwear
- `greece-classical.md:153` — hoplite kit includes repair footwear
- `haudenosaunee.md:123` — hide garments include moccasins leggings
- `india-classical-sanskrit.md:55` — northwestern coats boots stay regional
- `india-mughal.md:168` — visible-feature list includes footwear
- `inuit.md:152` — kamik names the skin boot
- `israel-ancient-hebrew.md:123` — household prompts include mantles sandals
- `japan-edo.md:90` — geta zōri waraji by occasion
- `korea-three-kingdoms-goryeo.md:164` — costume minimum records footwear separately
- `lakota-plains.md:134` — moccasins need dated Lakota objects
- `mamluk.md:151` — belt boots arms support warrior
- `mongol.md:123` — UNESCO caftan includes hat boots
- `newar-nepal.md:148` — chronicle restricts caps shoes gold
- `parthia.md:139` — Shami figure description includes footwear
- `persia-achaemenid.md:135` — riding dress includes soft footwear
- `persia-achaemenid.md:136` — delegations differ by their footwear
- `persia-sasanian.md:167` — represented dress includes coats boots
- `scythian-saka.md:123` — burial archive includes leather footwear
- `slavs-early.md:158` — design method separates cut footwear
- `sogdian-silk-road.md:128` — pictorial corpus shows high boots
- `thrace-dacia.md:155` — Herodotus lists fawnskin footwear coverings
- `turkic-steppe.md:146` — riding ensemble includes coat boots

`thrace-dacia.md:155` gist is 6 content words over a slash: the cell says "fawnskin footwear/leg covering".

### culture-material/ (11)

- `architecture-settlement-lexicon.md:29` — doma bay is where shoes stay
- `architecture-settlement-lexicon.md:125` — genkan shoe-lines stage threshold rites
- `bathing-and-body-hygiene.md:24` — thermae staff cell names bath-sandals
- `costume-semiotics.md:86` — class readable via fit shoes
- `craft-artisan-lexicon.md:104` — Crispin Crispinian are shoemaker saints
- `furniture-interior-lexicon.md:47` — floor regime: shoes off boundary
- `garment-lexicon-crosslinguistic.md:76` — Korean pair classifier for shoes
- `ritual-garments.md:27` — separation rite sheds shoes off
- `ritual-garments.md:42` — Shinto jōe paired with asagutsu
- `sumptuary-law-rank-display.md:77` — Mexica law graded cloaks sandals
- `transport-mobility-lexicon.md:20` — cites dress entry's riding boot

`transport-mobility-lexicon.md:20` does not describe a shoe. The visible clause attributes "riding clothes as an era seam: hem, split skirt, boot" to `dress-through-eras.md`. That word `boot` is **not** in `dress-through-eras.md` (direct sweep: no match).

### myth-symbol/ (4)

- `amulets-talismans-apotropaic-marks.md:103` — concealed shoes: luck, not proven apotropaic
- `myth-folktale-genres.md:19` — Rhodopis sandal story cited exemplar
- `myth-folktale-genres.md:62` — lost golden shoe dates Cinderella
- `trickster.md:106` — Hermes kit includes winged sandals

### synthesis/ (2)

- `conlang-blueprint-template.md:161` — lexicon slot 268 is footwear
- `consistency-verification-checklist.md:133` — garment check compares layers footwear

## One-way pointers (8)

The new entry should point here and not restate. Claim C `review_only` names `adornment-body-codes.md` and civilization entries; adornment is **not** in this eight, because it has no footwear line to cite.

| File | Cite | It owns | Footwear entry must not restate |
|---|---|---|---|
| `culture-material/costume-semiotics.md` | `:86` | dress as a sign system; shoes as a class-readable detail | the legibility dial |
| `culture-material/garment-lexicon-crosslinguistic.md` | `:76` | wardrobe naming; Korean `켤레` treats shoes as a pair | garment-name typology; ignore `:46` glove calque |
| `culture-material/ritual-garments.md` | `:27`, `:42` | garment-as-office; shoes-off separation; Shinto asagutsu | vesting order and office theology |
| `culture-material/sumptuary-law-rank-display.md` | `:77` | dress law as an assayable sign; Mexica graded sandals | the statute-formula machine |
| `culture-material/craft-artisan-lexicon.md` | `:104` | workshop speech; Crispin & Crispinian as shoemaker saints | tool anatomy (`:37` is not footwear) |
| `culture-material/architecture-settlement-lexicon.md` | `:29`, `:125` | built threshold: doma where shoes stay; genkan shoe-lines | house-part lexicon |
| `civilizations/japan-edo.md` | `:90` | geta / zōri / waraji by task, weather, road, occasion | the Edo costume dossier |
| `civilizations/ancestral-puebloan.md` | `:14`, `:152` | yucca-fiber sandals tied to cordage and basketry | the Pueblo textile dossier |

Closest alternates, not the eight: `furniture-interior-lexicon.md:47` (same shoes-off fact as a seating-regime consequence — point at architecture, mention furniture in that boundary sentence); `inuit.md:152` (kamik); `akan.md:126` and `:150` (sandals as office display); `china-qing.md:131` (shoe vs ancestry); `amulets-talismans-apotropaic-marks.md:103` (concealed shoes). `adornment-body-codes.md`: claim-named neighbor, **zero** footwear hits — a body-code boundary only, with no path:line. Do not point at `dress-through-eras.md` or `textile-technology.md` as if they contained a boot or fiber passage; they do not.

## Header shape (observed, `masks-masquerade.md:1-12`)

Blank line after the H1. Then exactly these bullets, in this order:

1. `- topic:` — one line; this text, after the prefix `- topic: `, is what the README row must copy byte-equal.
2. `- gap filled:` — filename sweep count, topic-line sweep count, who the partial owners are, "points … one-way."
3. `- sources:` plus two indented sub-bullets: in-corpus `path:line` anchors (the §2 table), then the external shelf (round date, ordinary means, new `SOURCES.md` rows, each sentence cites its row).
4. `- couples:` — one bullet; partitions separated by semicolons; each neighbour named as `` `file.md` (owns X; this entry takes only Y) ``.
5. `- source:` — lane-side authority (in-corpus §2 plus this round's registry rows) and a one-sentence design method.
6. `- verified-at:` — date, claim-base rev, pre-entry `find corpus/knowledge -type f | wc -l`, post-entry count, the round's `accept-c.py`.
7. `- recheck:` — `see §N.`
8. `- scope:` — partition method, what is withheld, PROVINCE.md non-decision, "nothing about what is true in any world."

Masks' own numbers, not this round's: topic-line sweep found 1 file; pre-entry **229**, post-entry **230**, `reports/round-54/accept-c.py`, verified-at 2026-10-22, base `260c68d`.

## README index (observed)

Section header, with a blank line before the first row (unlike `## myth-symbol/ (29)`, which has no blank line):

```
## culture-material/ (29)
```

`corpus/README.md:355`. Row shape, `README.md:373`, byte-equal to masks `- topic:` after the prefix:

```
- `masks-masquerade.md` — masks and masquerade as worn object, embodied presence and licensed voice — …
```

Pattern: `- `<filename>` — <topic value>`. Filename order. `footwear-codes-terminology.md` sorts after `fire-fuel-light.md` (`README.md:368`) and before `funerary-material-culture.md` (`README.md:369`).

Present-tense totals (`README.md:670-674`), dated 2026-10-23 in the file, not re-measured here:

```
Total knowledge entries: 235.

Counts checked 2026-10-23 from the repo root:
`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
(total 235 files; directory totals 29/29/29/29/24/95).
```

Vector order is section order: linguistics 29 / myth-symbol 29 / culture-material 29 / synthesis 29 / verification 24 / civilizations 95. Sum 235. One new culture-material file, if the tree matches this footer: section `(29)` → `(30)`, totals line 235 → **236**, vector `29/29/29/29/24/95` → `29/29/30/29/24/95`. Claim C's "236 files" matches that arithmetic. Re-measure at landing; do not edit a historical revision block.

## Ready-to-fill header skeleton

```markdown
# Footwear codes and terminology — shoes, sandals, boots and clogs as terms, status signs, rites and made objects: who may wear, remove, grade and make them, and where a worldbuilder decides

- topic: <ONE LINE. After `- topic: `, this exact text is the README row. Suggested spine, edit before byte-copy: footwear as terms, status signs, rites and made objects — what a shoe is said to be (term, pair, status mark, rite token, made thing), the complex (object, last, sole, fastening, wearer, maker), access rules for making, grading, wearing, removing and concealing, ritual and rank occasions, and the calibration traps of reading one footwear word as a universal costume>
- gap filled: at the claim base no file under `corpus/knowledge` owns footwear as a cross-cultural system. Filename sweep `<command>` → 0; topic-line sweep `<command>` → 0 real owners (`plant-symbolism.md:4` is `geta` inside `vegetation`). Partial owners are the culture-material sign, naming, vestment, sumptuary, workshop and threshold entries, plus single-tradition civilization dossiers (§2). This entry owns the comparative method and points to those owners one-way.
- sources:
  - In-corpus anchors (`corpus/knowledge/`-relative `path:line`, re-read at the lane worktree on 2026-10-23): see the §2 table.
  - External shelf — opened this round (2026-10-23) by ordinary means only (plain requests, public copies and Wayback captures; a challenge met was not passed), registered in `corpus/SOURCES.md` as this round's new rows (S652–S699, at least 20 distinct ids), each row carrying its URL, access date, tier scope, anchor and located quotes in the registry itself. Each bullet below cites exactly one row.
- couples: culture-material — `costume-semiotics.md` (owns dress as a sign system; this entry takes only what a footwear word adds), `garment-lexicon-crosslinguistic.md` (owns wardrobe naming and the pair classifier; `:46` hand-shoe is a glove), `ritual-garments.md` (owns garment-as-office, shoes-off separation, asagutsu), `sumptuary-law-rank-display.md` (owns assayable dress law, including graded sandals), `craft-artisan-lexicon.md` (owns workshop speech, including shoemaker saints), `architecture-settlement-lexicon.md` (owns the built threshold where shoes stay; `furniture-interior-lexicon.md:47` is the seating-regime consequence, not a second dossier); civilizations — `japan-edo.md` (geta / zōri / waraji) and `ancestral-puebloan.md` (yucca-fiber sandals), plus the other single-tradition lines in §2; myth-symbol — `amulets-talismans-apotropaic-marks.md` (concealed shoes) only if a bullet needs that boundary.
- source: lane-side authority is the in-corpus anchor list in §2 plus the external rows opened this round and registered in `corpus/SOURCES.md`. Design method: decide what the footwear is said to be first, then who may wear or remove it, then what status it assays, then who makes it and when it is shed.
- verified-at: 2026-10-23 — written against the lane worktree at <claim-base rev>; pre-entry `find corpus/knowledge -type f | wc -l` → **<re-measure; README footer says 235>**; post-entry count **<236 if footer holds>**, measured at landing by `python3 -B reports/round-61/accept-c.py`.
- recheck: see §<N>.
- scope: reference method and lane policy for the culture-material partition: footwear codes and terminology as a worldbuilding method. Single-tradition dossiers stay with their civilization entries (§2). It decides nothing about any real-world ownership or display question (PROVINCE.md), and nothing about what is true in any world.
```

README row to insert between `fire-fuel-light.md` and `funerary-material-culture.md`, topic value byte-equal:

```markdown
- `footwear-codes-terminology.md` — <exact text after `- topic: `>
```

## Confidence and gaps

- High: line list, excluded false hits, masks field order, README header/row/footer text, filename-order slot.
- Medium: six-word gists on lines not re-read raw. Load-bearing lines re-read raw: masks `:1-12`, `japan-edo.md:90`, `china-qing.md:131`, `bathing-and-body-hygiene.md:24`, `plant-symbolism.md:4`.
- Not done: live file count, `git ls-tree` filename count, opening neighbor files beyond the matching lines, any SOURCES.md URL check.
