# CriticGapPremise56 — round 56, claim C premise (Kingdom of Kongo entry)

Seat: critic (leaf), read-only. Lane HEAD `456f5ad` (pre-dispatch receipts), declaration `b4b7db9`. The claim base is `045f458` (`reports/round-56/claims.json:5`). The goal text names `052f145`, but that commit is the first instruments commit, which `045f458` revises. Paths are relative to `corpus/knowledge/` unless prefixed. Axes judged: **coverage** (is the ground uncovered in substance?) and **calibration** (do scope, status and attribution match the sources and the neighbouring entries?). No installs. Scratch: `/fast/scratch/hyaku/kotodama-r56/CriticGapPremise56/`.

## Verdict

- **The premise holds on ownership.** No file owns the Kongo kingdom. A case-insensitive sweep for `kongo|kikongo|koongo|nkisi|minkisi|kimbangu|bundu dia|antonian|kimpa vita|nzimbu|mbanza` over `corpus/` finds only one knowledge hit, `linguistics/language-contact.md:93` (a list item reading "Haitian Creole (French/Gbe-Kikongo)"). Separate sweeps for `raffia`, `cowrie`, shell money, `cosmogram` in a Kongo sense, `dikenga`, `yowa`, `power figure` and `nail figure` find nothing about Kongo. `civilizations/africa-primary-sources.md:158` names the gap itself: "Congo-basin … source inventories are not supplied."
- **The premise is weaker than its framing in three places.** All three are fixable, and none is a tradeoff the judge must reject.
  1. **The word "Kongo" changes identity across the topic list.** "Kingdom of Kongo" names a polity centred on Mbanza Kongo/São Salvador. Museum minkisi records, the cosmogram literature and the 19th–20th-century dictionaries mostly describe the **Kongo-speaking peoples** of the wider Lower Congo and Loango coast, often from after the partition (counterexample A).
  2. **The "early grammars" do not record the court speech of Mbanza Kongo.** Bentley (1887) argues that Brusciotto's grammar describes the dialect of Soyo, and Laman (1936) is a multi-dialect dictionary built for a future standard language (counterexample B).
  3. **The era endpoint and the handoff need tightening** (counterexamples C and D).
- **Province fit is good, and a civilization profile is the right form.** A thematic entry would split four existing mechanism owners (section 2).

## 1. Would a new entry split an existing owner? Where the line falls

No file owns **Kongo as a polity-specific coupling record**: its language varieties and their witnesses, titles and succession, Kongo Christianity as an institution, regalia, cloth and shell money, naming, and eras. That is the entry's own ground. Each row below is a mechanism that already has an owner. The entry should point to these one way and not restate them.

| Neighbour (anchor re-read) | What it already owns | Where the entry's line falls |
|---|---|---|
| `civilizations/africa-primary-sources.md:104-120` (§6) | The colonial-archive filter table (administrative purpose, interpreter and copyist invisibility, harmful metadata) | Point to it for reading Portuguese, Capuchin and Jesuit records. Do not build a second filter table. |
| `civilizations/africa-primary-sources.md:158,163` | Names the Congo-basin gap and lists ten companion profiles, without Kongo | The entry fills part of that gap. Updating `:163` is a **records item**: editing it inside C would add a fourth path to C's lands. |
| `linguistics/language-contact.md:93,98-105` | Kikongo as a creole substrate (Haitian), Kituba as a creole with an indigenous lexifier, and the debate over how creoles arise | Point to it. The entry must not argue the substrate question, and must not merge Kituba into Kikongo. |
| `synthesis/glossary-registry-format.md:222` | Missionary grammars and colonial dictionaries as biased witnesses, with the `bias_notes` field | Point to it when the entry discusses the 1624 catechism, Brusciotto, Bentley and Laman. |
| `linguistics/sacred-registers-liturgical-language.md` §5 and §8 (`:93,:125,:129`) | Vernacular instruction under a retained high register, and the reform path | Kongo catechism practice is an instance of this. Point to it; do not build a second competence model. |
| `myth-symbol/sacred-kingship-mythic-charter.md:66` (channel 4, "election / acclamation"), `:70` (regalia as title-deed), `:100` (interregnum) | The legitimation typology | Kongo succession and regalia are exemplars of these channels. Point to them; do not build a new typology. |
| `myth-symbol/direction-symbolism.md:70-88` (§4, anti-porting rule `:88`), `myth-symbol/cosmology-cosmography.md:27` | Closed partitions such as the quincunx and the Mexica cosmogram, the rule against porting colour and direction pairs between cultures, and the cosmology/cosmography split | The cosmogram is discussed only as a **contested reading**, with attribution. Do not add it as a historical closed partition beside the Maya or Mexica rows. |
| `synthesis/contact-scenario-builder.md:31,196` (Stewart and Shaw) | Syncretism and anti-syncretism as contested labels | Any "syncretism" framing of Kongo Christianity points here, and the label stays contested. |
| `civilizations/fon-dahomey.md:65`, `civilizations/yoruba.md:157` | The lane's diaspora rule: traditions are "historically connected but separately developed", and no transparent survival manual exists | Kongo-diaspora lines adopt this rule by pointing, not by deriving it again. |
| `culture-material/trade-economy-lexicon.md:12,45` | The drift from weighing to money, and the "Moneta move" (money named after its guarantor) | Nzimbu and cloth money are new substance, because the money owner is Eurasian and metal-based. Point to these lines for the general mechanism. |
| `linguistics/kinship-terminology.md:37,53` | Matrilineal and Crow-type rows | Do not assign a terminology type (Crow or another) to Kongo kinship unless an opened row states one. |
| `verification/real-world-inspiration-boundaries.md:97-107`, `verification/myth-consistency-gate.md:34`, `myth-symbol/divination-omen-systems.md:159` | Red lines for sacred material, the rule "unknown restriction → `(to-verify)`, withhold", and treating living divination traditions as living practice | Governs section 3 below. |

**Decision.** The entry splits no owner if it keeps to the coupling record and treats these rows as pointers. It **would** split owners if it:
- builds its own colonial-source filter (owned by africa-primary-sources);
- argues creole genesis (owned by language-contact);
- issues a legitimation typology (owned by sacred-kingship);
- adds the cosmogram as a historical closed partition (owned by direction-symbolism).

### Counterexample A — "Kongo" names a polity in the claim but a people and a style in the museum records (identity change)

I opened the Met collection API by plain request on 2026-10-22 (the `v1` search returned 410 and is retired; `v1.1` returned 200). The two nkisi nkondi records are:

| Met object | `culture` field | Date | Place |
|---|---|---|---|
| `https://collectionapi.metmuseum.org/public/collection/v1/objects/320053` ("Mangaaka Power Figure (Nkisi N’Kondi)", 2008.30) | "Kongo peoples" | "ca. 1880–1900" | "Republic of the Congo or Cabinda, Angola", river "Chiloango River" |
| `…/objects/312221` ("Nkisi N’Kondi (power figure)") | "Kongo peoples" | "19th–mid-20th century" | "Democratic Republic of the Congo" |

Neither record names the kingdom. One places the object on the Chiloango, north of the Congo River mouth and far from Mbanza Kongo, and dates it to the partition decades. Laman's preface (below) likewise treats Loango-coast varieties as a separate "royaume de Nguunu, branche de l'ancien Ntotila". That is Laman's tradition claim, not established fact.

**Impact.** This affects coverage (an entry titled "Kingdom of Kongo" would quietly cover a different and wider unit) and calibration. A worldbuilder could build a 16th-century court using objects from the 1880s coast.

**Smallest correction.** The scope section declares three units and tags every claim with one of them:
- (a) the **Kongo kingdom**, the polity at Mbanza Kongo/São Salvador with provinces such as Soyo and Mbata;
- (b) the **Kongo-speaking peoples and region**, including the Loango coast, Yombe, Vili, Woyo and Manianga;
- (c) **"Kongo" as a museum or art-history label**.

Minkisi rows carry the holding museum's own culture, place and date fields and are tagged (b) or (c), never (a), unless an opened row places the practice at the court.

### Counterexample B — the "early grammars" are not one variety, and two of the dictionaries are not from the kingdom's era

Opened by plain request on 2026-10-22 (archive.org, HTTP 200):

- **Bentley 1887, preface.** `https://archive.org/download/dictionarygramma00bent/dictionarygramma00bent_djvu.txt`, preface pp. xi–xii (text-layer lines 390–404).
  - "the dialect to which they refer is not that of the court of Kongo, but that of Sonyo or St. Antonio". "They" are Brusciotto's "Rules" of 1659.
  - The 1624 Doutrina was "translated" by "the priests at the court of Kongo, with the aid of Fr. Matheus Cardoso (Jesuit)".
  - The work's own title reads "as spoken at San Salvador, the ancient capital of the old Kongo empire". "Empire" is the source's word.
- **Laman 1936, preface.** `https://archive.org/download/dictionnairekikongofrancais/Hum.Sc.(IRCB)_T.II,1_LAMAN K.-E._Dictionaire Kikongo-Français _1936_djvu.txt`, preface (text-layer lines 284–372).
  - The subtitle describes "les dialectes les plus importants de la langue dite kikongo".
  - The preface aims at "la création d'une langue nationale".
  - It treats Vili, Kunyi and Bembe among other dialects.

**Impact on calibration.** "Kikongo and its early grammars" cannot supply 16th–17th-century court speech as one thing:
- Brusciotto may be Soyo/Solongo speech. This is Bentley's argument, so it must be attributed to him.
- The Doutrina is court work by Kongo priests with a Jesuit.
- Bentley records São Salvador speech in the 1880s.
- Laman's work is a 1930s multi-dialect lexicon with a standardizing aim.

Using a form from Laman or Bentley as "what the king's court said" collapses both the variety and the era. ScoutBrusciottoGrammar, ScoutBentleyDictionary, ScoutLamanDictionary and ScoutDoutrinaCatechism should each record their source's variety and date.

**Smallest correction.** Add a witness table with these columns: `witness | date | variety/locality as the source states it | compiler and institution | what it can support | what it cannot`. Every Kikongo form the entry cites carries its witness tag. The entry points to `glossary-registry-format.md:222` for bias notes.

### Counterexample C — the era endpoint is "colonial partition", but the kingdom did not end there

The goal stages eras "through Portuguese contact (1483) to the colonial partition". The partition divided Kongo-speaking territory among the European claimants. That the kingship continued under Portuguese overrule into the 20th century is [INFERENCE] from general knowledge; I opened no source for it, and ScoutColonialPartition owns it. If the era table's last row reads as "end of the kingdom", that is a false endpoint.

**Smallest correction.** The last era row says what the partition changed (borders, colonial administrations, mission fields) and states that what happened to the kingship afterwards is outside this entry or carried by ScoutColonialPartition's row. It must not say the kingdom ended in 1884–85.

### Counterexample D — the handoff has no Kongo-shaped slot in lore, and must not become one

Lore's checker defines `KINDS = {'character', 'place', 'faction', 'item'}` at `lore-shokunin/corpus/fixtures/check_bible.py:7` (re-read this session). Round 55 met the same wall (`.ufo/waves/round-55/build/CriticGapPremise.md`, counterexample B). A real polity handed off as a `faction` or `place` would import a real people into a fictional world as canon.

**Smallest correction.** The handoff section routes through `synthesis/worldbible-integration-contract.md` and labels its outputs with that contract's claim kinds at `:96`: **real-world reference** and **generative rule**. Any in-world material is a proposal labelled **attributed in-world belief**. The entry never proposes "Kongo" or a Kongo title, office or place as a world record or `kind`.

## 2. Province fit; civilization profile or thematic entry

- **Province.** `PROVINCE.md:3-14` names the `civilizations` partition and limits it to supporting "linguistic-cultural coupling". It excludes "historical truth certification" and canon. The topic fits if every section ends in a coupling decision: language ↔ title ↔ object ↔ era. It does not fit if it becomes a history of the kingdom.
- **Pattern.** The partition has 94 files:
  - 92 were added in the mint wave `49ac1a5`, one in round 3 (`c610e0a`) and one in round 4 (`fe34faa`). The last civilization entry was added in round 4; "before round 18" in the brief is true but understated.
  - Lengths run from 164 lines (`korea-joseon.md`) to 231 lines (`inuit.md`), at about 195 on average (18,375 lines across 94 files).
  - Six African profiles share one skeleton (`fon-dahomey`, `benin`, `akan`, `zimbabwe-shona`, `swahili-coast`, `yoruba`):
    - a header with `topic, sources, couples, source, verified-at, recheck`;
    - then Scope and calibration; language family and writing; mythic or religious core; symbolic system; era staging; costume and material; naming; what a worldbuilder can take; provenance cautions;
    - 13 to 16 `##` sections.
- **A thematic entry would serve worse.** The candidate themes are:
  - missionary grammars and catechisms (owned by `glossary-registry-format.md:222` and `sacred-registers-liturgical-language.md`);
  - elective kingship (owned by `sacred-kingship-mythic-charter.md:66`);
  - shell or cloth money (`trade-economy-lexicon.md`);
  - power objects (no owner, but this theme is the most sensitive one; see section 3).

  Each theme already has a mechanism owner, so a thematic file would split it. The gap is **polity-specific substance**, and the profile is the one place that couples these facets for one polity. The profile is the right form, provided it uses the skeleton above and points to the owners in section 1.
- **One new feature.** This will be the first civilization entry to cite registry S-ids rather than author-year citations or local keys. That is fine, but the entry must not also carry author-year citations (for example "Thornton 1983") for works that have no S row opened this round. Such citations look provided-for but break the round's rule that a source counts only if it was opened this round.

## 3. Traditions the entry may treat only through the community's own public statements, or must leave out

**Rule.** Present-day religious and political practice stays out unless the round has opened a community-authored or community-authorised public statement. Where none is opened, the entry may at most name the boundary and point to the in-lane rules: `real-world-inspiration-boundaries.md:97,107`, `myth-consistency-gate.md:34` and `divination-omen-systems.md:159`. Nothing in the round's seat list opens such a statement: no seat is briefed on Kimbanguism or Bundu dia Kongo, and the minkisi and diaspora seats are briefed on museums and scholarship.

| Tradition | What the entry may say | Must not |
|---|---|---|
| **Kimbanguism** (Church of Jesus Christ on Earth by His Messenger Simon Kimbangu) | Nothing, because it falls after the era endpoint. At most one pointer line saying it is out of scope. I tried the World Council of Churches member page (`oikoumene.org/member-churches/…simon-kimbangu`): HTTP 403, a Cloudflare challenge, **challenge met, not passed**. The Wayback availability API returned 429. No statement was opened. | Describe its doctrine, its founder's career, its sites (Nkamba) or its relation to the Kongo kingdom or to Kimpa Vita. Framing it as a "revival" of the Antonian movement is a scholarly comparison that needs a community statement or an opened row; I have opened neither [INFERENCE]. |
| **Bundu dia Kongo** (a present-day politico-religious movement in the DRC) | Nothing. It is contemporary partisan politics, outside both the province (`PROVINCE.md:16-20`) and the era. I tried the HRW 2008 report URL: 404. No source was opened. | Any mention, including as "the modern heir of the kingdom". Political and violent conflict claims must not enter a worldbuilding reference. |
| **Minkisi in present use** (banganga practice today) | Historical objects through the holding museum's own record fields (culture, place, date, as in counterexample A), and the meaning of *nkisi* through an opened specialist row such as MacGaffey, attributed. The present-tense line is: "practice continues; this entry describes museum-held objects and dated scholarship only". | Procedures for making or activating an nkisi, the medicines and contents of a named object, oath formulas, or "how it works" written as fact. Use "fetish" only inside a quotation, flagged as the source's word (for example a museum's historic label). The museum caption "power figure" is a museum convention, not a Kikongo gloss. |
| **Kongo-derived diaspora religions** (Palo Monte and Mayombe, Kongo rites in Haitian Vodou, Kongo heritage in Brazil) | One pointer paragraph through ScoutKongoDiaspora's opened rows that adopts `fon-dahomey.md:65`'s rule ("historically connected but separately developed"). | Any initiatory content (initiation rites, the nganga vessel's contents, signatures or firmas) or present-day ritual detail. Do not present these religions as preserved Kongo-kingdom religion. |
| **Cosmogram readings** (dikenga, yowa, the Kalunga line) | Attributed and contested: Thompson's and Fu-Kiau's readings and the critique, each with its row and the status the sources give (ScoutCosmogramCalibration). Fu-Kiau is a Kongo-born author; his reading is a named person's 20th-century teaching, not "the Kongo belief". | Present a timeless kingdom-wide doctrine, draw a design table from it, or give it as a closed partition (section 1). |
| **The Antonian movement and Kimpa Vita** | Historical, through ScoutKimpaVita's rows, with the hostile Capuchin witness marked as such (`africa-primary-sources.md` §6). | Present-day commemoration or veneration claims without a community or official statement. Do not use the "Kongolese Joan of Arc" framing as a description (CriticCalibrationKongo owns that trap). |

## 4. What would make the 231→232 count hollow

`reports/round-56/accept-c.py:84` collects every `\bS\d{3}\b` token anywhere in the file. The legs check no line cap, no use in the body, no restatement, no scope tags and no edits to neighbours. The count is hollow if any of the following holds:

1. **Header-only citations.** The `- sources:` block holds 20 or more S-ids while the body cites few of them. FLOOR still passes.
2. **A catalogue of dates.** The era section is a chronicle (1483, 1491, 1506, 1568, 1665, 1704–06, 1884–85) with no column that says what changes in language, titles, objects or naming at each stage. The lane's era owners require decisions, not dates (`culture-material/era-periodization-models.md`; the "several clocks" pattern at `civilizations/yoruba.md:146`).
3. **A thin profile.**
   - Fewer than about 160 lines would make it the thinnest of the 94 civilization files.
   - Fewer than 10 `##` sections, against 13 to 16 in the six African peers.
   - Very long lines that hide length beneath the 230 cap.
4. **The wrong unit.** Minkisi, cosmogram and dictionary material is cited as kingdom material (counterexamples A and B). The count rises, but the ground covered is not the ground claimed.
5. **Contact-centred substance.** Most sentences narrate what the Portuguese did (Cão, embassies, letters). Kongo offices, words and objects become a backdrop, and the entry's "linguistic-cultural" half goes missing.
6. **Restatement with new S-ids.** Any of the four splits in section 1 is cited again from new rows.
7. **Tier-B over-reading.** Publisher pages for Thornton, Fromont and LaGamma are used to carry sentences about what Kongo people believed, rather than what the book argues (QUALITY criterion 6).
8. **Neighbour edits.** For example, adding Kongo to `africa-primary-sources.md:163` inside C. The SET leg compares file names, not contents, so it cannot see this.

## Must-not list (for the L1 and the falsify wave)

1. Must not use "Kongo" without saying which unit it means: kingdom, Kongo-speaking peoples and region, or museum label. Must not present Loango-coast or post-1880 objects as artifacts of the kingdom's court.
2. Must not present Brusciotto, Bentley or Laman forms as 16th–17th-century court speech. Each Kikongo form carries its witness, variety and date. Bentley's Soyo attribution of Brusciotto stays attributed to Bentley.
3. Must not merge Kituba, Munukutuba or Kikongo ya leta into Kikongo. Point to `linguistics/language-contact.md:93`.
4. Must not say the kingdom ended at the colonial partition.
5. Must not hand off Kongo or any Kongo office, place or title as a lore record or `kind` (character, place, faction or item). Use the claim kinds at `worldbible-integration-contract.md:96` only.
6. Must not mention Bundu dia Kongo. Kimbanguism gets no more than a one-line scope exclusion.
7. Must not give a procedure, contents, an oath formula or a present-tense efficacy claim for any nkisi. Must not describe present-day banganga, Palo or Vodou practice.
8. Must not use "fetish", "idol", "pagan", "witch doctor", "tribe", "primitive" or "voodoo doll" except inside a quotation flagged as the source's word. "Empire" appears only as Bentley's quoted title.
9. Must not state the cosmogram as historical Kongo doctrine, and must not add it as a closed partition. Status: contested, with attribution.
10. Must not restate the colonial-archive filter, creole genesis, the legitimation typology or the syncretism debate. Point to the section-1 anchors instead.
11. Must not assign a kinship terminology type to Kongo without an opened row that states it.
12. Must not cite author-year works that have no S row opened this round. Must not write a pre-S359 S-id or a neighbour's local key (`KTD-S-`, `[CO]`, `[CARE]`, `[S95]`).
13. Must not edit any file under `corpus/knowledge` other than the entry. Route the `africa-primary-sources.md:163` companion-list update and its `:158` frontier note as records items.
14. Must not exceed 230 lines, hide length in very long lines, or fall under about 160 lines without saying why it is thin.
15. Must not date the founding traditions without the source's hedge ("by tradition", "according to").

## Falsifiers for the falsify wave

`E=corpus/knowledge/civilizations/kongo-kingdom.md`. Run at the landed tip from the lane root, with base `045f458`. A "hit" means the line must be reviewed against the named rule.

- **F1 header-only citations.** Must print `[]`:
  ```
  python3 -B -c "import re;t=open('$E').read();i=t.find('\n## ');h,b=t[:i],t[i:];print(sorted(set(re.findall(r'\bS\d{3}\b',h))-set(re.findall(r'\bS\d{3}\b',b))))"
  ```
- **F2 thin carry.** Count the cited S-ids that occur exactly once in the body. If more than half do, report the entry as thin. This is a report, not a failure.
- **F3 size and shape.** Three checks:
  - `wc -l < $E`: at most 230 lines; report it if under 160.
  - `grep -c '^## ' $E`: report it if under 10.
  - `awk 'length>600' $E | wc -l`: report the count.
- **F4 unit tag** (counterexample A). Every hit must carry a museum culture, place or date field, or a scope tag (peoples, region or label). No hit may attribute the object to the court or the kingdom without a row that says so.
  ```
  grep -niE 'nkisi|minkisi|nkondi|mangaaka|Yombe|Vili|Woyo|Loango|Kakongo|Ngoyo|Manianga|Chiloango' $E
  ```
- **F5 witness tag** (counterexample B). Every hit names the variety or locality and the date. Any Kikongo form in italics must sit on a line or table row that names its witness.
  ```
  grep -niE 'Brusciotto|Regulae|Doutrina|Cardoso|Bentley|Laman|Cannecattim|Gheel|Vocabularium' $E
  ```
- **F6 Kituba kept separate.** Each hit keeps Kituba distinct from Kikongo and points to `language-contact.md`:
  ```
  grep -niE 'Kituba|Munukutuba|ya leta' $E
  ```
- **F7 cosmogram status.** Each hit is attributed and coded contested (C). At least one hit points to `direction-symbolism.md` or `cosmology-cosmography.md`. No table row uses the cosmogram as a design key.
  ```
  grep -niE 'cosmogram|dikenga|yowa|kalunga|four moments|Fu-Kiau|Thompson' $E
  ```
- **F8 living and present-day** (section 3).
  - These must print nothing:
    ```
    grep -niE 'Bundu dia|\bBDK\b|Ne Muanda Nsemi' $E
    ```
  - Kimbangu hits number at most 1, and that one is a scope exclusion:
    ```
    grep -niE 'Kimbangu' $E
    ```
  - Each hit of the following is a pointer or a museum or scholarly attribution, with no procedure:
    ```
    grep -niE 'today|present-day|contemporary|still (used|practi)|nganga|Palo|Vodou|Candombl|firma' $E
    ```
- **F9 exoticizing words.** Each hit sits inside a quotation flagged as the source's word, or is negated:
  ```
  grep -niE 'fetish|idol|pagan|heathen|witch.?doctor|primitive|savage|tribe|tribal|voodoo|empire' $E
  ```
- **F10 era endpoint.** No hit may say the kingdom ended at the partition. The era section must contain a table whose header has a decision column ("changes", "decide", "use" or "field"):
  ```
  grep -niE '1884|1885|Berlin|partition' $E
  ```
- **F11 founding hedge.** Each founding or origin hit carries "by tradition", "according to" or a range stated by the source:
  ```
  grep -niE 'Lukeni|Nimi|found(ed|ing|er)|origin' $E
  ```
- **F12 one-way pointers.** Each of these must print at least 1:
  ```
  grep -c 'africa-primary-sources.md' $E
  grep -c 'language-contact.md' $E
  grep -c 'sacred-kingship-mythic-charter.md' $E
  grep -cE 'direction-symbolism.md|cosmology-cosmography.md' $E
  grep -c 'real-world-inspiration-boundaries.md' $E
  grep -c 'worldbible-integration-contract.md' $E
  grep -cE 'glossary-registry-format.md|sacred-registers-liturgical-language.md' $E
  grep -cE 'fon-dahomey.md' $E
  ```
- **F13 restatement without a pointer.** Each command must print nothing:
  ```
  grep -niE 'syncretis' $E | grep -v 'contact-scenario-builder.md'
  grep -niE 'relexif|substrat|bioprogram' $E | grep -v 'language-contact.md'
  grep -niE 'acclamation|legitimation channel' $E | grep -v 'sacred-kingship-mythic-charter.md'
  ```
- **F14 handoff.** The handoff section must contain `worldbible-integration-contract.md` and at least one of "real-world reference" or "generative rule". This command must print nothing:
  ```
  grep -niE "kind: *(faction|place|character|item)|as a faction|as a lore (place|faction)" $E
  ```
- **F15 old ids and local keys.** Must print nothing:
  ```
  grep -nE 'KTD-S-|\[(CO|CARE|AJ|RAI|BEN)\]|\[S[0-9]{1,3}\]' $E
  ```
- **F16 no neighbour edits.** Must list only the entry:
  ```
  git diff --name-only 045f458..<tip> -- corpus/knowledge
  ```
- **F17 tier honesty.** For every cited tier-B row (publisher or exhibition pages), each sentence citing it says what the work or page states, not what Kongo people believed.
- **F18 unregistered author-year support.** Each hit must sit on a line that also cites an S-id in S359–S418, or must be removed:
  ```
  grep -nE '\b[A-Z][a-z]+( and [A-Z][a-z]+)? \(?1[5-9][0-9]{2}|\b[A-Z][a-z]+ 20[0-2][0-9]\b' $E
  ```

## Unopened and unrun

- **Unopened sources.**
  - `oikoumene.org` Kimbanguist member page: HTTP 403, Cloudflare challenge, **challenge met, not passed**.
  - Wayback availability API: HTTP 429 on three lookups, not retried.
  - HRW 2008 DRC report URL: HTTP 404.
  - Met `v1/search`: HTTP 410 (retired); `v1.1/search` was used instead.
  - Laman's first-guessed text-layer URL: 404; the file listing gave the correct name.
- **Opened sources.** The Met records and the Bentley and Laman prefaces support counterexamples A and B. They are not seat source rows; a source seat must file them in the source shape if the L1 wants them cited.
- **Not run.** I ran no `accept-c.py`, `sweep.py`, `check-source-access.py` or falsifier, because the entry has not landed. The claim that the kingship continued after the partition (counterexample C) is [INFERENCE] from general knowledge.
