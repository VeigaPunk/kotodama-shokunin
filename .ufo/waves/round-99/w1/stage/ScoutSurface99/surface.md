# ScoutSurface99 — coverage surface and adjacency for claim C (round 99, w1)

Seat: ScoutSurface99 (leaf, read-only). Lane: kotodama-shokunin. Date: 2026-11-06.
Assignment: confirm the claim-C coverage surface **by content**, map adjacency, propose the
entry skeleton, and hold the bounded planning data-walk (partition counts).

Nothing in this file is canon, a gate verdict, or a registry edit. I wrote only under
`.ufo/waves/round-99/w1/stage/ScoutSurface99/`. No network source was opened (not this
seat's item; capture mining belongs to the registry seat). No tool installed or upgraded.

Base: `527df3fee305b3454446946e6779ece45456307e`. All counts below were taken from the
working tree at the time of this sweep; every count names its command and its rc.

---

## 1. Sweep outputs (exact commands, rc)

### 1.1 Broad body sweep — the command the item names, verbatim

```
grep -rn -i -E 'praise|panegyr|oríkì|oriki|izibongo|imbongi|griot|jeli|bard|encomi|eulog|madih|madīḥ|qasida|qaṣīda|filid|fili|skald|drápa|drapa|kenning|epithet|genealog' corpus/knowledge
```
Result: **1084 matches in 190 files, rc 0** (`grep: 1084 matches in 190 files`).

This surface is dominated by two noisy stems. `genealog` alone accounts for the bulk
(language genealogy, descent claims, kin charts), and unbounded `fili` matches
*filiation / filial*, unbounded `bard` matches the **Bard Graduate Center** publisher in
`civilizations/dine-navajo.md:20-26`. The broad sweep is therefore a *screen*, not a census.

### 1.2 Word-bounded high-signal sweep (the discriminating pass)

```
grep -rnP -i '\b(praise|panegyr|oríkì|oriki|izibongo|imbongi|griot|jeli|bard|encomi|eulog|madih|madīḥ|qasida|qaṣīda|fili|filid|skald|drápa|drapa|kenning)\b' corpus/knowledge
```
Result: **206 matches in 50 files, rc 0**. Per-file counts (`grep -rcP … | grep -v ':0$' | sort -t: -k2 -rn`, rc 0), top of the list:

| file | matches | class |
|---|---|---|
| `civilizations/yoruba.md` | 22 | substantive (case owner) |
| `linguistics/orality-formulaic-language.md` | 19 | **substantive (nearest owner)** |
| `civilizations/mali-songhai.md` | 19 | substantive (case owner) |
| `linguistics/funerary-lament-dirge-formulae.md` | 12 | substantive (neighbour genre) |
| `civilizations/zimbabwe-shona.md` | 12 | substantive (case owner) |
| `civilizations/germanic-norse.md` | 10 | substantive (case owner) |
| `civilizations/india-tamil-sangam.md` | 9 | substantive (case owner) |
| `civilizations/fon-dahomey.md` | 9 | substantive (case owner) |
| `civilizations/dine-navajo.md` | 7 | **false positive** — all 7 are "Bard Graduate Center" (`grep -nP -i '\bbard\b' …`, rc 0) |
| `synthesis/deity-name-derivation-pipeline.md` | 6 | substantive (divine-epithet owner) |
| `myth-symbol/sacred-kingship-mythic-charter.md` | 6 | substantive (royal register) |
| `civilizations/india-vedic.md` | 6 | case (divine praise) |
| `civilizations/india-mughal.md`, `igbo.md`, `celts.md`, `arabia-pre-islamic.md` | 4 each | case / passing |
| `myth-symbol/hero-journey-variants.md`, `culture-material/costume-semiotics.md`, `malagasy-madagascar.md`, `khmer-angkor.md`, `india-classical-sanskrit.md` | 3 each | mixed |
| `synthesis/worked-example-mini-culture.md`, `linguistics/speech-surrogates-whistled-drummed.md`, `linguistics/sound-symbolism.md`, `linguistics/linguistic-anthropology.md` | 2 each | passing / boundary |

`dine-navajo.md` is the one file whose entire high-signal count is a bibliographic false
positive: its praise content is **0**, and it is dropped from the adjacency set.

### 1.3 The six frozen phrases — whole-corpus occurrence count

```
for p in 'praise poetry' 'praise singer' 'panegyric' 'genealogical recitation' 'praise epithet' 'praise performance'; do n=$(grep -r -o -i -F "$p" corpus/knowledge | wc -l); echo "$p=$n"; done
```
rc 0. Result:

| phrase | occurrences | where (file:line) |
|---|---|---|
| praise poetry | **5** | `java-majapahit.md:198`, `zimbabwe-shona.md:23` (a **book title**, Hodza & Fortune 1979 *Shona Praise Poetry*), `orality-formulaic-language.md:60`, `orality-formulaic-language.md:148`, `speech-surrogates-whistled-drummed.md:110` |
| praise singer | **0** | — (a free surface) |
| panegyric | **4** | `byzantium.md:7`, `:55`, `:90` ("panegyrical"), `india-tamil-sangam.md:105` |
| genealogical recitation | **1** | `inca.md:151` (table data row) |
| praise epithet | **1** | `yoruba.md:161` |
| praise performance | **2** | `fon-dahomey.md:42` (table data row), `zimbabwe-shona.md:104` |

13 occurrences in 9 files, **all in prose or table cells**.

### 1.4 The C8 owner test, run exactly as the frozen counter defines it

`reports/round-99/predispatch.py:160-173` (`sweep_owners` docstring) and `:581-587` (leg C8)
define ownership as: the file's `- topic:` line **or any markdown heading** carries the
phrase; prose and table cells are *mentions, not ownership*, and are not scanned; the entry
path itself is excluded.

```
for p in …; do n=$(grep -r -i -F "$p" corpus/knowledge --include='*.md' | grep -cE '^[^:]+:[0-9]+:(- topic:|#)'); echo "$p owners=$n"; done
```
rc 0. Result: **owners=0 for all six phrases** (`praise poetry`, `praise singer`,
`panegyric`, `genealogical recitation`, `praise epithet`, `praise performance`).

Cross-check by hand: the four h2 headings in the whole corpus that contain "praise" are
`yoruba.md:78` ("Oríkì: praise, memory, and an economy of recognition"),
`zimbabwe-shona.md:87` ("…and praise address"), `funerary-lament-dirge-formulae.md:133`
("…praise of the dead…"), `orality-formulaic-language.md:56` ("Epithets and praise-names").
None is a frozen phrase. **The claim-C surface is unowned by content, not merely by
filename** — this confirms the claim's `before` cell independently.

### 1.5 Planner data-walk: knowledge entries per partition

```
find corpus/knowledge -name '*.md' | awk -F/ '{print $(NF-1)}' | sort | uniq -c | sort -rn
```
rc 0. Result:

| partition | entries |
|---|---|
| civilizations | 95 |
| linguistics | **43** |
| culture-material | 43 |
| myth-symbol | 36 |
| synthesis | 29 |
| verification | 24 |
| **total** (`find … | wc -l`, rc 0) | **270** |

Matches the committed footer vector in `corpus/README.md` (`directory totals
43/36/43/29/24/95`, total 270), so the base is internally consistent and the landing
arithmetic below is safe.

### 1.6 Registry census (the rows claim C must extend)

```
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md          # 930, rc 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md   # 0, rc 0
awk -F'|' … tier … corpus/SOURCES.md    # A=556 B=345 C=29, rc 0
awk -F'|' … status … corpus/SOURCES.md  # mined=821 queued=60 rejected=49, rc 0
grep -oE '^\|[[:space:]]*S[0-9]+' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort -V | tail -1   # S1006, rc 0
grep -E '^\|[[:space:]]*S10(0[7-9]|[1-9][0-9])[[:space:]]*\|' corpus/SOURCES.md                 # no output, rc 1
```
So: 930 rows, 0 malformed, highest **S1006**, and **S1007 upward is entirely free** (rc 1 =
no match). The claim's `registry rows >= 934, highest >= S1010` needs four new rows
S1007–S1010 at minimum, and nothing blocks that id range.

Row shape (11 columns → 13 awk fields): `id | source | kind | tier | scope | anchor |
teaches | status | opened | recheck | used-by`. `kind` is constrained by census command 6 to
`spec|docs|paper|code|tool|dataset|talk|book|community|own-work`; tier to `A|B|C`; status to
`queued|mined|rejected`; and census command 7 requires every `used-by` path to exist on
disk. The anchor cell convention in the newest rows (S1000–S1006) is
`body text; reports/round-98/evidence/S10xx.txt; exact locator: "<quote>"` — which is
exactly what leg C7 binds (`quote inside the row's anchor cell`).

### 1.7 Index insertion point and landing arithmetic

```
ls corpus/knowledge/linguistics/ | sort | grep -n -A2 -B2 'politeness\|proverbs'
```
rc 0 → `25:politeness-taboo-euphemism.md`, `26:proverbs-riddles-attestation-solutions.md`.
`praise-poetry-panegyric.md` sorts **between them** (pol < pra < pro). The README row is
added in filename order with the entry's `- topic:` text verbatim (the house pattern:
revisions 2.22–2.24 in `corpus/README.md:1-20`).

Landing arithmetic for the index footer (`tools/check-corpus-index.py` requires six
partitions, fails duplicates, and refuses to fall back past a malformed final dated footer):

- `## linguistics/` 43 → **44**
- total 270 → **271**
- footer vector `43/36/43/29/24/95` → `44/36/43/29/24/95`
- new revision 2.25 at the head of `corpus/README.md`, dated 2026-11-06.

---

## 2. Hit classification (owner / substantive section / passing mention)

"Owner" = `- topic:` line or heading (the C8 test). "Substantive section" = a whole h2 that
owns a neighbouring surface and must be deferred to. "Passing" = a cell, a bibliography
entry, or a single sentence.

### 2.1 Owners: none

No file owns any of the six frozen phrases by topic line or heading (§1.4). The nearest
thing to an owner is `orality-formulaic-language.md:56` `## 3. Epithets and praise-names:
the formula lexicon`, which owns **praise-names as formula lexicon** — the boundary the
claim names explicitly.

### 2.2 Substantive sections (defer; do not restate)

| file:line | section | what it owns |
|---|---|---|
| `linguistics/orality-formulaic-language.md:56-62` | §3 Epithets and praise-names | Parry epithet sets, makura-kotoba, **"Praise poetry as social formula: Yoruba oríkì … Nguni izibongo"** (`:60`), and the 5-step epithet build order (`:62`) |
| `linguistics/orality-formulaic-language.md:73-81` | §5 Kennings, heiti | myth-locked diction |
| `linguistics/orality-formulaic-language.md:99-127` | §8 the singer's speech | the 12-item register checklist, whose item 10 already names "performer licensing: hereditary guild (jeli)" and "competitive forms (Scottish flyting; Lokasenna-style senna)" |
| `linguistics/funerary-lament-dirge-formulae.md:15` | §1 scope | the four things the lament owns, incl. "the praise of the dead" |
| `linguistics/funerary-lament-dirge-formulae.md:56-84` | §3 professional keeners | the three-way office split (professional / kin / mixed), payment media, gendered licence |
| `linguistics/funerary-lament-dirge-formulae.md:133-153` | §6 formulaic grief content | **praise of the dead** as compartment 1 of four, plus the sequence rule |
| `linguistics/verbal-duelling-ritual-insult.md:18` | §1 scope | the word-contest, and the routing of satire-with-legal-force to binding speech |
| `linguistics/verbal-duelling-ritual-insult.md:110-124` | §6 the boast formula | claim / warrant / wager slots, calibration of plausible overclaim |
| `linguistics/verbal-duelling-ritual-insult.md:124-146` | §7 audience adjudication | judges, uptake, outcome |
| `linguistics/toast-drinking-speech-formulae.md:122-171` | §5 toastmaster + order of a sequence | the office that runs a sequence, the 7-part order, and the three order rules (every turn has a caller; the reply quotes the theme; the order must be checkable) |
| `linguistics/sacred-registers-liturgical-language.md:26-40` | §1 ownership table | the six neighbouring surfaces and what this entry adds |
| `linguistics/sacred-registers-liturgical-language.md:101-108` | §6 recitation norms and chant | recitation accuracy as a competence, chant |
| `linguistics/linguistic-anthropology.md:9-28` | §1 SPEAKING grid | the speech-event unit; already names "praise poem" as a G value and "the funeral praise" as a native genre name |
| `linguistics/linguistic-anthropology.md:91-138` | §5 special languages | ritual/avoidance/argot registers |
| `linguistics/naming-systems.md:44-63` | §2 anthroponymy | name slots incl. Arabic `laqab` (honorific byname) and the `nasab` chain glossed "genealogy as memory" |
| `linguistics/naming-systems.md:87-108` | §6 name taboo | name magic, erasure, renaming |
| `synthesis/deity-name-derivation-pipeline.md:69-88` | §4 Epithet systems | **divine** epithet grammar: head + modifier + jurisdiction, cult epithet vs poetic occurrence, "a shared epithet is not a unique identifier" (`:86`) |
| `linguistics/speech-surrogates-whistled-drummed.md:28-47` | §2 one-owner boundary | the channel; `:110` already routes "praise poetry itself stays with orality-formulaic-language.md:124" |
| `linguistics/kinship-terminology.md:153` | §Calibration | genealogies as present-serving charters (Bohannan 1952) |
| `linguistics/kinship-terminology.md:137` | §design step 7 | "a genealogy recited at court" as a stress-test scene |
| `linguistics/oath-blessing-curse-formulae.md:20-38` | §1 scope | the binding formula; satire with legal force is a curse and routes here |
| `myth-symbol/sacred-kingship-mythic-charter.md:142-155` | §8 the royal register | the seven-part royal register; item 5 `:150` **"Praise-recitation as performed pedigree"** — the charter is publicly auditable, and an omitted title is a political statement |
| `myth-symbol/heraldry-emblems-identity-marks.md:18-33` | §2 one-owner boundary | 12 neighbours and the split of entitlement vs meaning |
| `myth-symbol/heraldry-emblems-identity-marks.md:35-48` | §3 the bearer unit | the eight bearer units (person / crest / clan / office / affinity / community / property / hereditary right) |
| `myth-symbol/heraldry-emblems-identity-marks.md:63-71` | §5 blazon grammar | the closed verbal register that governs a granted design |
| `civilizations/polynesia-navigation.md:142-161` | Oral genealogy | whakapapa-style precision axes, branch selection ("a shorter performance is not automatically a corrupted longer one", `:146`), the reciter/custodian/audience/access field set (`:157`), restricted genealogies (`:161`), no chronometry (`:150`) |
| `civilizations/yoruba.md:78-94` | Oríkì | the oríkì case and the four-relation **oríkì economy** table, "praise is not necessarily bland flattery", the epithet-dossier exercise |
| `civilizations/mali-songhai.md:50-70` | Jeli oral archives | the six register tags (genealogical recognition / public praise / epic narration / mediation / peer-facing status / admonitory court performance) and the Ibn Battuta Dugha anchor |
| `civilizations/zimbabwe-shona.md:87-107` | Mutupo | mutupo/chidawo, praise address, the emblem table, and `:104` praise performance making ancestry present |
| `civilizations/fon-dahomey.md:118-143` | Palace registers, royal names | royal praise performance (`:42`), dynastic memory, `:164` "distinguish royal praise from neighborhood satire" |
| `civilizations/india-tamil-sangam.md:49-65` | Akam/puram | puram as the public field of "praise, appeal, admonition, lament"; `:57` "Praise is interested speech" |
| `civilizations/parthia.md:165-183` | Gōsān | the bardic-institution evidence calibration and `:183` the design move "specify repertoire ownership, payment, permissible mockery, commemorative duty, and audience competence before inventing a bard's formal title" |
| `civilizations/germanic-norse.md:72-86` | Eddic/skaldic verse economy | dróttkvætt as "dense praise, recollection, verbal display", named poets and patrons |
| `civilizations/germanic-norse.md:87-100` | Kenning tradition | base + determinant + referent + required story |
| `civilizations/celts.md:43-62` | Druidic oral transmission | `:50` Diodorus 5.31: praise/satire singers called bards, druids, diviners — three roles, not one class |
| `civilizations/arabia-pre-islamic.md:61-78` | Qaṣīdah | the mode table: `:69` fakhr (self/group praise), `:70` **madīḥ (praise of another)** |
| `civilizations/india-classical-sanskrit.md:45,158,176` | praśasti | patronage → poets → praśasti chain; titles vs praise formula; "royal praśastis are interested eulogies, not neutral annals" |
| `civilizations/india-vedic.md:31,88-89,97,162,174,184` | divine praise | Vedic praise relations, henotheism as "an interpretive label for some praise strategies" |
| `civilizations/malagasy-madagascar.md:176-179` | naming practices | self-praise in *Ibonia*, praise-name performance at life stages, the four design slots |

### 2.3 Passing mentions (no boundary work; cite at most)

`civilizations/dine-navajo.md:20-26` (7× "Bard Graduate Center" — false positive),
`civilizations/inca.md:151` (rival histories row: "competing praise names, genealogical
recitations, and authorized versions" — a good *rivalry* citation, still a cell),
`civilizations/akan.md:57,94`, `civilizations/rome.md:59`,
`civilizations/greece-classical.md:78,181` (cult epithet → divine-epithet owner),
`civilizations/byzantium.md:7,55,90,138`, `civilizations/india-mughal.md`,
`civilizations/igbo.md`, `civilizations/khmer-angkor.md`, `civilizations/java-majapahit.md:198`,
`myth-symbol/hero-journey-variants.md`, `myth-symbol/death-afterlife-eschatology.md`,
`culture-material/funerary-material-culture.md:101,130` (epitaph as document),
`culture-material/costume-semiotics.md`, `culture-material/warrior-material-culture.md:52-54`
(blazon as closed register), `synthesis/contact-scenario-builder.md:94,101,156` (epithet
translation under contact), `synthesis/religion-language-co-evolution.md:99`,
`synthesis/urban-rural-register-ecology.md:48`, `synthesis/worked-example-mini-culture.md:74,79`,
`linguistics/sound-symbolism.md`, `linguistics/petitionary-and-votive-formulae.md:21-56`
(vocative address and litanic parallelism — a real shared surface with praise, but it owns
the petition grammar), `linguistics/greeting-leave-taking-formulae.md`,
`linguistics/register-strata-attestation.md` (register law, cited by oath).

---

## 3. Adjacency table — the boundary the new entry must respect

The rule throughout: **cite the owner's anchor, state the one-line difference, add nothing
that file already teaches.** Six collisions are sharp enough to need an explicit sentence in
the entry's §1 boundary table; they are marked **⚠**.

| # | neighbour (anchor) | what it owns | boundary the new entry must respect |
|---|---|---|---|
| 1 | ⚠ `linguistics/orality-formulaic-language.md:56-62` | praise-names as **formula lexicon**: epithet sets, metrical slots, the 5-step epithet build order, "praise poetry as social formula" (`:60`) | The claim's named boundary. The new entry may cite `:60` once and must **never restate** the formula machinery, the slot logic, or the "praise-name = compressed genealogy + history + political claim" formulation. It owns the *institution* (office, patronage, sequence, audience, rivalry, bearer-binding), not the diction. |
| 2 | ⚠ `linguistics/funerary-lament-dirge-formulae.md:56-84,133-153` | the professional-mourner office (three-way split, payment media, gendered licence) and **praise of the dead** as one of four grief compartments | Do not re-derive the licensed-performer split or re-own mourning. Cite §3 as the parallel office case and §6 as a compartment this entry does not touch; the difference is one line: the praise office is patron-facing and competitive, the mourning office is death-facing and duty-bound. |
| 3 | ⚠ `linguistics/verbal-duelling-ritual-insult.md:110-146` | the boast formula (claim/warrant/wager), audience adjudication, and the routing of legally binding satire to binding speech | The new entry's "rivalry, satire and the limits of flattery" section must defer the contest grammar and the boast slots. It owns only *praise-genre* rivalry: rival panegyrists, competing recensions of one lineage, the patron's choice between them, and flattery's genre limits. |
| 4 | ⚠ `linguistics/toast-drinking-speech-formulae.md:122-171` | the office that runs an ordered sequence and the three order rules (caller; reply quotes theme; order checkable) | The "order of a praise performance" section must cite these three rules and apply them, not re-derive a general theory of ordered speech. Its own contribution is the praise-specific slot inventory (invocation → genealogy → epithet chain → deed → patron → close), which must not be a relabelled toast table. |
| 5 | ⚠ `synthesis/deity-name-derivation-pipeline.md:69-88` | **divine** epithet grammar: head + modifier + jurisdiction, cult epithet vs poetic occurrence, one epithet may qualify several gods | The sharpest collision with the phrase "praise epithet". The new entry owns **human** praise epithets (person / lineage / office / place) and routes every divine epiclesis here. State the split; do not import `head+modifier` as the human-epithet grammar. |
| 6 | ⚠ `myth-symbol/sacred-kingship-mythic-charter.md:142-155` (item 5, `:150`) | the royal register and "praise-recitation as performed pedigree": the charter is publicly auditable, an omitted title is a political statement | Do not re-own royal legitimation or the seven-part register. Cite `:150` for the audit principle; the new entry owns the genre mechanics that make the audit possible, not the charter theory. |
| 7 | `myth-symbol/heraldry-emblems-identity-marks.md:35-48` | the eight **bearer units** and the grant/registration/transmission of marks | This is the analogue the new entry borrows for "epithets stay tied to their bearers": cite §3's bearer-unit table as the model, do not restate mark transmission, and do not re-teach blazon (§5). |
| 8 | `civilizations/polynesia-navigation.md:142-161` | whakapapa-style recitation precision, branch selection, the reciter/custodian/audience/access fields, restricted genealogies, no chronometry | Defer the whole case. The new entry may cite `:146` ("a recitation may select an appropriate line") as the one-line principle for lineage selection inside a praise performance, with the pointer; it must not build a second genealogy-precision model. |
| 9 | `linguistics/kinship-terminology.md:153` | genealogies as present-serving charters (Bohannan 1952) | Cite the charter critique; do not re-argue it, and do not re-teach kin-term typology. |
| 10 | `civilizations/yoruba.md:78-94` | the oríkì case and the four-relation **oríkì economy** table | Cite, never rebuild. The new entry's economy section must not re-derive the kin / ruler / devotee / performer rows; it may use them as the comparative axis in a table that routes to this file. |
| 11 | `civilizations/mali-songhai.md:50-70` | the jeli register tags and the Dugha anchor | Cite the tags as *analytical* tags (the file says so); do not relabel them as a universal genre taxonomy, and do not re-tell the Ibn Battuta episode. |
| 12 | `civilizations/zimbabwe-shona.md:87-107` | mutupo/chidawo, praise address, emblem inference limits, permission caution (`:104`) | Cite; do not restate clan-emblem inference limits or the permission rule. |
| 13 | `civilizations/fon-dahomey.md:42,118-143,164` | royal praise performance, palace registers, "authorized speaker / addressee / audience / material credential" | Cite `:164`'s "royal praise vs neighborhood satire" as a design lever with the pointer; do not rebuild the palace-register system. |
| 14 | `civilizations/india-tamil-sangam.md:49-65,105,117` | akam/puram, "praise is interested speech", bardic praise, panegyric abundance ≠ economic output | Cite puram as the public-praise field; do not re-teach the akam/puram taxonomy. |
| 15 | `civilizations/parthia.md:165-183` | gōsān evidence calibration and the `:183` checklist (repertoire ownership, payment, permissible mockery, commemorative duty, audience competence) | Nearest **method** neighbour for the office section. Either cite `:183` as the source of that checklist, or state a genuinely different procedure; do not present the same five items as new. |
| 16 | `civilizations/germanic-norse.md:72-100` | dróttkvætt as court praise with named poets/patrons; kenning decoding | Cite the court-praise economy; do not re-teach meter or kennings (orality §5 owns kennings too). |
| 17 | `civilizations/celts.md:43-62` (`:50`) | Diodorus 5.31: bards (praise/satire singers), druids, diviners as three roles | Cite `:50` for the panegyrist-and-satirist role split; do not re-argue the writing taboo. |
| 18 | `civilizations/arabia-pre-islamic.md:61-78` (`:69-70`) | qaṣīdah components; fakhr and **madīḥ** | Cite madīḥ as the panegyric mode; do not re-teach the ode's components or the nasīb→raḥīl sequence. |
| 19 | `civilizations/india-classical-sanskrit.md:45,158,176` | praśasti as interested eulogy; titles vs praise formula | Cite; do not re-teach the patronage→poets→kāvya chain. |
| 20 | `civilizations/india-vedic.md:31,88-89,97,162,174,184` | Vedic divine praise, henotheism as praise strategy | Cite; the new entry does not own divine hymnody. |
| 21 | `civilizations/malagasy-madagascar.md:176-179` | self-praise in *Ibonia*; the four naming slots | Cite; do not restate the Malagasy naming slots. |
| 22 | `linguistics/linguistic-anthropology.md:9-28` | the SPEAKING grid and the speech-event unit | Apply the grid in §2; do not re-teach it. |
| 23 | `linguistics/naming-systems.md:44-63,87-108` | name slots (incl. `laqab`, `nasab`), name taboo | The praise epithet is **not** a name slot; distinguish it from byname/laqab/regnal name and route the slot system here. |
| 24 | `linguistics/speech-surrogates-whistled-drummed.md:28-47,110` | the channel; `:110` already routes praise poetry to `orality:124` | Do not own the channel. If a praise tradition is drummed or whistled, route here. (The existing routing target is a *mention*; no edit is in scope this round — see §6.) |
| 25 | `linguistics/sacred-registers-liturgical-language.md:101-108` | recitation accuracy as a competence; chant | Do not treat praise recitation as liturgical recitation; where a praise genre is also liturgical, route here and to the relevant civilization file. |
| 26 | `linguistics/oath-blessing-curse-formulae.md:20-38` | the binding formula; satire with legal force = curse | Route the binding side of satire here; own only the contest-free rivalry. |
| 27 | `linguistics/petitionary-and-votive-formulae.md:21-56` | vocative address, petition mood, litanic parallelism | Praise and petition share the vocative and parallelism; the new entry must not re-teach either. |
| 28 | `synthesis/contact-scenario-builder.md:94,101,156` | epithet translation across contact | Route epithet translation here. |
| 29 | `culture-material/funerary-material-culture.md:101,130` | the epitaph as the document class | Passing; the new entry does not own mortuary text. |
| 30 | `myth-symbol/binding-speech-complex.md` | the four binding channels and enforcement | Cited only through `oath-blessing-curse-formulae.md`; not rebuilt. |

**One structural note for the entry author.** `speech-surrogates-whistled-drummed.md:110`
currently routes "praise poetry" to `orality-formulaic-language.md:124`. That is a *mention*
and it does not fail C8, but it means the corpus will have two pointers for one phrase. The
new entry should not try to fix it (the file is another owner's), and the L1 should decide
in a later round whether that row's pointer gains the new path.

---

## 4. Proposed entry skeleton

Target path: `corpus/knowledge/linguistics/praise-poetry-panegyric.md`.
House shape copied from the sibling speech-act entries (`funerary-lament-dirge-formulae.md`
51,055 B / 12 h2; `toast-drinking-speech-formulae.md` 47,760 B / 13 h2;
`verbal-duelling-ritual-insult.md` 36,743 B / 13 h2 — `wc -c`, rc 0). Claim C's floor is
12,000 B; the sibling norm is 2–4× that, and the h2 norm is 8–15
(`for f in corpus/knowledge/linguistics/*.md; do grep -c '^## ' …`, rc 0).

Front matter (byte-equal `- topic:` is a C1 leg):

```
# Praise poetry and panegyric: the praise singer's office, the praise epithet, and the order of a praise performance

- source: corpus/SOURCES.md (the registry rows below, one id per line)
- sources:
  - S1007 … (four or more, tier A|B, opened 2026-11-06/07, used-by exactly this path)
- verified-at: 2026-11-06
- recheck: 180d
- topic: praise poetry and panegyric: praise as a public speech act that builds a person, lineage, office or place — the praise singer's office, patronage and reward; the praise epithet and the genealogical recitation; the order of a praise performance and its audience; rivalry, satire and the limits of flattery; and the design procedure for a fictional praise tradition whose epithets stay tied to their bearers, singers, patrons and occasions
- couples: … (the §3 adjacency list, one pointer per neighbour)
```

### 4.1 The fourteen h2, with the frozen phrases placed

| # | h2 | frozen phrase | defers to |
|---|---|---|---|
| 1 | `## 1. Scope: the praise surface this entry owns, and the six it defers` | — | the §3 adjacency table, reproduced as a one-owner table (house pattern: heraldry §2, speech-surrogates §2) |
| 2 | `## 2. Praise as a public speech act: what it builds and who may build it` | — | `linguistic-anthropology.md:9-28` (apply SPEAKING, don't teach it) |
| 3 | `## 3. The praise singer: office, recruitment, licence and the patron` | **praise singer** | `funerary-lament:56-84` (office analogue), `mali-songhai:50-70` (jeli), `parthia:183` (the five-item checklist) |
| 4 | `## 4. The praise epithet: keeping the name tied to its bearer` | **praise epithet** | `orality:56-62` (formula lexicon — cite, never restate), `deity-name-derivation-pipeline:69-88` (divine split), `heraldry:35-48` (bearer unit), `naming-systems:44-63` (slot vs epithet) |
| 5 | `## 5. Genealogical recitation: the lineage spine and its access rules` | **genealogical recitation** | `polynesia-navigation:142-161`, `kinship-terminology:153`, `inca:151` (rival versions) |
| 6 | `## 6. The order of a praise performance: slots, turns and the caller` | **praise performance** | `toast:122-171` (the three order rules), `sacred-registers:101-108` (recitation competence) |
| 7 | `## 7. Audience, uptake and the economy of recognition` | — | `yoruba:78-94` (oríkì economy), `mali:60` (public praise), `fon:164` |
| 8 | `## 8. Rivalry, satire and the limits of flattery` | — | `verbal-duelling:110-146`, `oath-blessing-curse:20-38`, `mali:64` (admonitory court performance), `celts:50` (bard/satirist) |
| 9 | `## 9. Panegyric: praise of the office, the dynasty and the place` | **panegyric** | `sacred-kingship:150`, `arabia:70` (madīḥ), `india-classical-sanskrit:45,176` (praśasti), `byzantium:55`, `germanic-norse:72-86` (dróttkvætt), `tamil:105` |
| 10 | `## 10. Praise poetry as a genre system: verse, register and transmission` | **praise poetry** | `orality:56-62,73-81,99-127` (meter, kennings, register — cite only), `speech-surrogates:110` (channel) |
| 11 | `## 11. Design procedure: a fictional praise tradition with bound epithets` | — | the ten-step procedure (below) |
| 12 | `## 12. Error patterns: praise traditions that fail as speech acts` | — | — |
| 13 | `## 13. Calibration, limits and the handoff to the lore world bible` | — | house pattern |
| 14 | `## 14. Inference ledger` | — | house pattern (verbal-duelling §13, toast §13) |

**Frozen-phrase landing: 6 of 6 in h2 headings** (§3, §4, §5, §6, §9, §10), against a floor
of 4. All six are also natural table cells if the author prefers redundancy — e.g. a §10
"genre at a glance" table whose first column is the genre name (`praise poetry`,
`panegyric`, `praise performance`, `genealogical recitation`) and whose other columns are
bearer unit / singer's office / reward / occasion / owner-file. That table is the safest
place to double-cover the phrases, and it is also the ≥5-row × ≥3-col table C1 wants.

### 4.2 The two tables that carry the argument

**Table A — §1 one-owner boundary** (≥6 rows × 3 cols). Columns: `Neighbour (anchor)` |
`What it owns` | `This entry's boundary`. Rows: orality §3, funerary §3/§6, verbal-duelling
§6, toast §5, deity-name §4, sacred-kingship §8.5, polynesia §Oral genealogy, heraldry §3.
This single table discharges the "defer, never restate" requirement in the form the corpus
already uses (heraldry §2, speech-surrogates §2).

**Table B — §9 panegyric institutions at a glance** (≥6 rows × 5 cols). Columns: `tradition`
| `genre name` | `bearer unit` | `singer's office and reward` | `owner file / registry id`. Every
row routes to its civilization file and adds **no new case detail** — the discipline
`verbal-duelling §8` ("Contest genres at a glance") and `toast §12` already use.

### 4.3 The design procedure (§11), and what makes it non-duplicative

Ten steps, each phrased as a decision the designer must make, none of them a re-run of
`orality §3`'s epithet build order:

1. Fix the **bearer unit** the tradition praises (person / lineage / office / place) and
   whether one performance may address several (borrow heraldry §3's unit list by citation).
2. Fix the **singer's office**: hereditary, appointed, or self-made; who licenses; who pays;
   in what medium (the `parthia:183` five-item checklist is cited, not re-invented).
3. Fix the **epithet binding rule**: each epithet stores `{bearer, source event, authorized
   utterer, permitted occasion, public/private version, expected response}` — the Yoruba
   `:94` dossier is cited as the model, and the divine-epithet grammar stays with
   `deity-name-derivation-pipeline`.
4. Fix the **genealogy depth and access**: which line, how far back, who may hear it, and
   what a shorter recitation means (cite `polynesia:146`).
5. Fix the **sequence** and its caller (the three order rules of `toast:127-171`).
6. Fix the **audience's required uptake** (silence, response, gift, acclaim) and what
   happens when uptake is withheld.
7. Fix the **reward** and its direction (gift, cloth, office, exemption) — and whether the
   reward is obligatory or competitive.
8. Fix the **rivalry rules**: who may answer a praise, whether a rival may praise the same
   patron, and what a contested recension does to the lineage's claim.
9. Fix the **limits of flattery**: which claims are checkable, which are licensed hyperbole,
   and which are actionable insults (cite `tamil:57` and `verbal-duelling:122`).
10. Fix the **failure consequences**: a wrong epithet, a wrong lineage, a wrong occasion, an
    unauthorized singer — each with its own sanction.

---

## 5. Planner data-walk: why `linguistics/`

### 5.1 Partition counts

95 civilizations / **43 linguistics** / 43 culture-material / 36 myth-symbol / 29 synthesis /
24 verification = 270 (§1.5, rc 0). Linguistics is the second-largest partition and exactly
tied with culture-material; a 44th entry moves it to the largest after civilizations.

### 5.2 Justification

1. **Shape match.** The entry is a speech-act/genre institution plus a design procedure —
   the exact shape of seven existing linguistics entries (funerary-lament, toast,
   verbal-duelling, greeting, oath, petitionary, orality). Every one of them is a
   "scope → attested cases → master table → design procedure → error patterns → handoff →
   inference ledger" file. No civilization entry has that shape; they are reference bases
   with era/costume/name sections.
2. **Nearest owners are all in linguistics.** The five sharpest deferrals (orality §3,
   funerary §3/§6, verbal-duelling §6, toast §5, linguistic-anthropology §1) are linguistics
   files. Putting the entry elsewhere would split the deferral cluster.
3. **The frozen phrases are genre terms, not case names.** "praise poetry", "praise singer",
   "panegyric", "praise performance" are genre/institution words; the corpus files genre
   institutions under linguistics and case instances under civilizations.
4. **Civilizations would collide.** The case owners (yoruba, mali-songhai, zimbabwe-shona,
   fon-dahomey, tamil-sangam, germanic-norse, arabia, celts, parthia) each own one
   tradition; a civilizations-partition entry would have to become a comparative survey and
   would either duplicate them or pick a favourite. Linguistics lets the entry own the
   *comparison and the procedure* while every case stays with its owner.
5. **Index mechanics agree.** `check-corpus-index.py` requires the six partitions and a
   filename-ordered row with the `- topic:` text verbatim; the insertion point is
   `politeness-taboo-euphemism.md` → `praise-poetry-panegyric.md` →
   `proverbs-riddles-attestation-solutions.md` (§1.7, rc 0).

### 5.3 Registry and evidence preconditions (measured, for the registry seat)

- 930 rows, 0 malformed, A=556 / B=345 / C=29, mined=821 / queued=60 / rejected=49 (§1.6).
- Highest id **S1006**; **S1007 upward free** (`grep` rc 1 = no match).
- Four new rows S1007–S1010 minimum; `opened` 2026-11-06 or 2026-11-07; `used-by` exactly
  `corpus/knowledge/linguistics/praise-poetry-panegyric.md`; tier A or B; `kind` from the
  census whitelist; anchor cell carrying the `reports/round-99/evidence/S10xx.txt` path and
  an `exact locator: "<quote>"`.
- `reports/round-99/evidence/` **does not exist yet** (`ls -la … ; rc 2`), so the captures
  and `manifest.json` are still to be created by the owning seat.
- C7 binds capture sha256 + a quote of 1–25 words occurring exactly once in the named
  capture, inside the row's anchor cell. C9 needs ≥3 qualifying ids re-opened by
  ReviewerC99 on fresh bytes with count 1.

### 5.4 A lead worth passing to the registry seat

`zimbabwe-shona.md:23` cites **Hodza & Fortune 1979, _Shona Praise Poetry_** (Oxford:
Clarendon) as its praise-genre reference. It is the canonical monograph for the izibongo/
Shona praise-poetry surface and a natural tier-A/B target — but the row must be *opened
this round with a capture*, so a book without an open text is a lead, not a commitment.

---

## 6. Residual unknowns and out-of-scope flags

1. **No unknown blocks the surface.** The six phrases are unowned by topic line and heading
   (rc 0, §1.4), and the claim's `before` cell (owners=0) is independently confirmed.
2. **`speech-surrogates:110` routes "praise poetry" to `orality:124`.** A mention, not an
   owner; no C8 risk. Whether that pointer should later gain the new entry path is an L1
   decision, not this seat's edit.
3. **`dine-navajo`'s 7 high-signal hits are all "Bard Graduate Center".** Any future sweep
   that reports it as a praise file is wrong; the bounded regex is the one to reuse.
4. **`zimbabwe-shona:23` is a book title**, so a naive exact-phrase count over the corpus
   will always show ≥1 "praise poetry" that is a citation. C1 counts the *entry's* headings
   and table rows, so this does not interfere, but a whole-corpus phrase census should say
   so.
5. **Divine vs human epithet is the one boundary most likely to be missed** in drafting.
   `deity-name-derivation-pipeline.md:69-88` owns the divine grammar; the entry's §4 must
   say so in its first paragraph.

---

## 7. Files read (all read-only)

Sweeps: `corpus/knowledge/**` (206 bounded high-signal matches, 50 files; 1084 broad
matches, 190 files), `corpus/SOURCES.md`, `corpus/README.md:1-63` + tail,
`reports/round-99/claims.json`, `reports/round-99/predispatch.py` (C8 legs `:160-173`,
`:581-587`), `reports/round-49/run-validation.py` (census command list),
`tools/check-corpus-index.py` (header), `tools/gates/lexicon-coverage-audit.py` (header).

Read in full or in the cited ranges: `linguistics/orality-formulaic-language.md`
(1-12, 56-130, 151-172), `linguistics/funerary-lament-dirge-formulae.md` (1-18, 15-33,
56-84, 133-155), `linguistics/verbal-duelling-ritual-insult.md` (18-33, 110-124),
`linguistics/toast-drinking-speech-formulae.md` (122-175), `linguistics/oath-blessing-curse-formulae.md`
(20-39), `linguistics/sacred-registers-liturgical-language.md` (26-56),
`linguistics/linguistic-anthropology.md` (9-30), `linguistics/naming-systems.md` (38-65,
87-109), `linguistics/speech-surrogates-whistled-drummed.md` (14-49),
`linguistics/kinship-terminology.md` (1-6, 137, 153),
`myth-symbol/sacred-kingship-mythic-charter.md` (57-74, 142-156),
`myth-symbol/heraldry-emblems-identity-marks.md` (18-50, 63-72),
`civilizations/yoruba.md` (78-95), `civilizations/mali-songhai.md` (50-71),
`civilizations/zimbabwe-shona.md` (87-108), `civilizations/polynesia-navigation.md` (142-165),
`civilizations/india-tamil-sangam.md` (49-66), `civilizations/celts.md` (43-63),
`civilizations/germanic-norse.md` (72-101), `civilizations/arabia-pre-islamic.md` (61-79),
`civilizations/inca.md` (145-158), `civilizations/malagasy-madagascar.md` (172-182),
`synthesis/deity-name-derivation-pipeline.md` (headings, epithet lines),
plus the grep-classified files in §2.3.

No file outside `.ufo/waves/round-99/w1/stage/ScoutSurface99/` was written. Scratch
`/fast/scratch/hyaku/kotodama-r99/ScoutSurface99/` was created empty and removed before
yield.
