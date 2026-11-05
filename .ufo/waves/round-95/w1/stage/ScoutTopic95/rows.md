# Round-95 claim C source staging — funerary lament / dirge surface

Seat: ScoutTopic95. Date: 2026-11-05. Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.
Base: 19aa4dd03dfd37b435d0b8ea5b313635d9d51592. All captures staged in
`.ufo/waves/round-95/w1/stage/ScoutTopic95/evidence/` (S970.pdf/.txt … S980.pdf/.txt).

Every quote below was verified with `python3 -c "bytes.count(quote)"` against the staged
text capture and occurs **exactly once** (`count == 1`); every quote is **25 words or fewer**
(word counts given). Text renders are `pdftotext` (poppler, default layout) of the staged PDF.

---

## 1. Gap sweep — no filename owner for the lament/dirge sung-register surface

Command (run from the lane root, rc 0):

```
find corpus -name "*lament*" -o -name "*dirge*" -o -name "*keen*" -o -name "*moirolog*" -o -name "*funerary*" | sort
```

Output (1 line):

```
corpus/knowledge/culture-material/funerary-material-culture.md
```

So the whole corpus (all partitions, not only `linguistics/`) has **no** file owning the
lament/dirge **sung-speech register** surface. `funerary-material-culture.md` owns the
mortuary **material** apparatus (disposal / assemblage / monument / word layers) and touches
the lament only as an etymology item (`*dirge* < Latin *Dirige*`, Office of the Dead Matins
antiphon) and as a cross-reference to `linguistics/orality-formulaic-language.md`
(`corpus/knowledge/culture-material/funerary-material-culture.md:139`, `:39`).

Corpus prose grep, measured (rc 0):

```
grep -cniE "\b(dirge|keening|keener|eulog)" corpus/knowledge/linguistics/*.md   -> no file matches
grep -cniE "\blament" corpus/knowledge/linguistics/*.md                          -> 1 match, orality-formulaic-language.md
grep -rliE "\blament" corpus/knowledge --include=*.md | grep -v "/linguistics/"
```

So inside the linguistics partition the words *dirge*, *keening*, *keener* and *eulogy* occur
**nowhere**, and *lament* occurs **once**, as a type-scene card. Across the whole corpus the
word *lament* appears only in eight non-linguistics files (four civilization profiles, the
funerary and music culture-material files, and two myth-symbol files) — all as one-line
scene or genre references, never as an owned linguistic surface.

### The three closest existing entries (positioning anchors for the new entry)

1. `corpus/knowledge/linguistics/orality-formulaic-language.md` — owns **lament as a
   type-scene card** in the epic inventory (`orality-formulaic-language.md:66`: "…feast,
   sacrifice, omen-taking, messenger speech, journey/underworld, **lament**, duel. Six to
   twelve cards cover most epic narrative"), plus ballad incremental repetition and the
   theme/thought-unit machinery. **Overlap to avoid**: the new entry must not re-teach the
   Parry–Lord composition theory or the type-scene list; it must *specialise* one card —
   lament — and treat it as a speech register.
2. `corpus/knowledge/linguistics/lullaby-child-song-formulae.md` — owns the **sung register
   as a distinct modality** (S965's Kanak *parler* vs *chanter*, S966's vocable chorus, S968's
   sung vs spoken counting-rhyme versions, S969's refrain/apostrophe). **Overlap to avoid**:
   the new entry borrows the *sung-vs-spoken* framing but must not re-teach lullaby form or
   child-song transmission; the mourning register is the adult, funeral, non-consolatory
   counterpart.
3. `corpus/knowledge/culture-material/funerary-material-culture.md` — owns the **death
   register and mourning economy** (WORD layer: avoidance terms, rite terms, office terms
   including Roman *praefica*, *libitinarius*, *pollinctor*, *designator*;
   `funerary-material-culture.md:36`; the mourning duration and enforcement law;
   the *dirge*/*requiem*/*elegy* etymology chain at `:37` and `:139`). **Overlap to avoid**:
   that file owns objects, offices, schedules and the word layer of death; the new entry owns
   the **sung utterance itself** — its performers, its structure, its formulaic content and
   its design procedure — and couples to that file rather than restating it.

Secondary neighbors, for completeness: `linguistics/sacred-registers-liturgical-language.md`
owns liturgical recitation and chant competence (the *hymn*/recitation event type, but not
mourning improvisation); `linguistics/register-strata-attestation.md:69` and
`linguistics/semantics-pragmatics.md:95` list *mourning formulas* only as an example of the
expressive speech-act class; `linguistics/greeting-leave-taking-formulae.md` is the
closest structural sibling in **shape** (a speech-act family with one predicate and a
situational formula pool) but is a different speech situation.

Registry state at base, measured (rc 0):

```
grep -cE '^\| S[0-9]+ ' corpus/SOURCES.md            -> 893
grep -oE '^\| S[0-9]+' corpus/SOURCES.md | sort | tail -1  -> S969
```

---

## 2. Candidate blocks (proposed registry rows S970–S981)

### S970 — Seto choral/anti/phone lament (facet: antiphonal lament; speech-vs-song boundary)

- **Title**: From Lament to Lamenting Song: Musical Models, Meanings and Expression in Seto Solo and Choral Funeral Laments
- **Author**: Žanna Pärtlas
- **Venue**: Journal of Ethnology and Folkloristics 19(1): 91–124 (2025). DOI 10.2478/jef-2025-0006
- **URL**: https://sciendo.com/pdf/10.2478/jef-2025-0006 (final: `https://reference-global.com/download/article/10.2478/jef-2025-0006.pdf`)
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for the Seto choral-lament genre and its antiphony
- **Scope**: the *antiphonal lament* facet and the speech-vs-song boundary for the same community (Seto laments of a deceased maiden are performed by a group of lamenters, not solo)
- **Anchor**: §2 (analysis of Seto choral lament) and abstract; published June 2025
- **Quote 1** (facet: antiphonal lament; 7 words): `the antiphonal way of performing Seto songs`
- **Quote 2** (facet: speech-vs-song boundary; 9 words): `the relationship between the genres of lament and song`
- **Capture**: `evidence/S970.txt` (text rendering) + `evidence/S970.pdf` (950971 bytes)
- **sha256**: text `dc7394e9862003b0b26e7631520e3dcb19832d25b19ddd4e6898cda06c371316`; pdf `e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e`
- **HTTP status**: 200

### S971 — Corsican *voceru* antiphony and gendered lament (facet: antiphonal lament; gendered mourning rules)

- **Title**: A Voice Like Thunder: Corsican Women's Lament as Cultural Work
- **Author**: Ruth Emily Rosenberg
- **Venue**: Current Musicology 78 (2004). DOI 10.7916/cm.v0i78.5043
- **URL**: https://journals.library.columbia.edu/index.php/currentmusicology/article/download/5043/2312/
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for Corsican voceru lament and its antiphonal/jural structure
- **Scope**: the *antiphonal lament* facet (antiphony as a record-keeping institution) and the gendered-mourning facet (lament as a predominantly feminine mode of expression)
- **Anchor**: abstract and §11–12 (footnote on antiphony); published 2004-09-06
- **Quote 1** (facet: antiphonal lament; 6 words): `The antiphonal nature of voceru performance`
- **Quote 2** (facet: gendered mourning rules; 4 words): `feminine mode of expression`
- **Capture**: `evidence/S971.txt` + `evidence/S971.pdf` (927824 bytes)
- **sha256**: text `656c45388dbfcab8f9de8a233eada5d8f8571647a1f04955605bff71cbc4a26a`; pdf `85b821c7233c85bf1d3907b5db5ce98d368d19f6a06cdacc029a7df628345fbe`
- **HTTP status**: 200

### S972 — Irish wake: the keen as a professional-occupation institution (facet: professional keeners)

- **Title**: Keening the Dead: Ancient History or a Ritual for Today?
- **Author**: Mary McLaughlin (University of Limerick)
- **Venue**: Religions 10(4): 235 (2019). DOI 10.3390/rel10040235
- **URL**: https://mdpi-res.com/d_attachment/religions/religions-10-00235/article_deploy/religions-10-00235.pdf
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for the Irish *keen* as a staged ritual with a professional role
- **Scope**: the *professional keeners* facet (the wake as a fixed sequence in which paid keeners take over from the family) and the speech-vs-song facet (the keen as improvised chant, not recitation)
- **Anchor**: abstract and §2 (the 18th-century wake sequence); published 29 March 2019
- **Quote 1** (facet: professional keeners; 4 words): `Professional keeners took over.`
- **Quote 2** (facet: speech-vs-song; 7 words): `the keen was a sacred improvised chant`
- **Capture**: `evidence/S972.txt` + `evidence/S972.pdf` (324233 bytes)
- **sha256**: text `d3ff0209b9d80418bcc9345535f5fd440a3fc8a2433da6982c42a65d777293ce`; pdf `1e0b0f8d8b529aae60ff2138d591aeb40465e778d11702b88b176d68334b30c8`
- **HTTP status**: 200

### S973 — The keening woman as an office and a gender role (facet: professional keeners; gendered mourning rules)

- **Title**: Vernacular Catholicism in Ireland: The Keening Woman
- **Authors**: Sean Williams (The Evergreen State College) and Lillis Ó Laoire (University of Galway)
- **Venue**: Religions 15(7): 879 (2024). DOI 10.3390/rel15070879
- **URL**: https://mdpi-res.com/d_attachment/religions/religions-15-00879/article_deploy/religions-15-00879.pdf
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for the *bean chaointe* office and its gendered rules
- **Scope**: the *professional keeners* facet (the female professional mourner as a ritual role) and the *gendered mourning rules* facet (postmenopausal status as a qualification; the keening woman as agent of transition)
- **Anchor**: abstract and §2–3 (the bean chaointe as office); published July 2024
- **Quote 1** (facet: professional keeners; 10 words): `was important in the role of the female professional mourner`
- **Quote 2** (facet: speech-vs-song boundary; 5 words): `hovers between singing and wailing`
- **Capture**: `evidence/S973.txt` + `evidence/S973.pdf` (1555760 bytes)
- **sha256**: text `e017b3958dac14b32ff08a11f1750638e997c5df43ec9674a91413f5c42cac76`; pdf `8750510347c20a3ef8a12112435cc917c2737a42a4ffeadab3f85b557720a5d9`
- **HTTP status**: 200

### S974 — Svan funeral dirge: refrain, praise of the dead, address to the dead (facet: lament refrain; praise of the dead)

- **Title**: Svan Funeral Dirges (Zär): Cultural Context
- **Authors**: Nana Mzhavanadze and Frank Scherbaum (Universität Potsdam)
- **Venue**: Musicologist 5(2): 133–165 (2021). DOI 10.33906/musicologist.906765
- **URL**: https://dergipark.org.tr/en/download/article-file/1673889
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for the Svan *zär* dirge performance and its refrain
- **Scope**: the *lament refrain* facet (the closing refrain exclamation and the answering sob) and the *praise of the dead* facet (the recitation praising the deceased and addressing him about the living)
- **Anchor**: abstract and §4 (performance description); published December 2021
- **Quote 1** (facet: lament refrain; 5 words): `ends with a refrain exclamation`
- **Quote 2** (facet: praise of the dead; 10 words): `Sima praises the good deeds and grace of the deceased`
- **Capture**: `evidence/S974.txt` + `evidence/S974.pdf` (1156987 bytes)
- **sha256**: text `251b4d3f420164baa4bdc6508e54736cb0d00a42bc66940363203c264060159d`; pdf `f1e4be9fd0868713bf363ea18b368a501dd48d87dc7bd3039e801f4954ad2672`
- **HTTP status**: 200

### S975 — Lament song as praise: the heroic *kleos* mode (facet: praise of the dead)

- **Title**: Lament Songs Glorifying Greek Soldiers Killed in Battle During the Balkan Wars (1912–1913)
- **Author**: Evangelos Avdikos (University of Thessaly)
- **Venue**: Folklore: Electronic Journal of Folklore 99 (2026). DOI 10.7592/FEJF2026.99.avdikos
- **URL**: https://www.folklore.ee/folklore/vol99/avdikos.pdf
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for the *glorifying* lament mode and the shift from dirge to epic praise
- **Scope**: the *praise of the dead* facet (a lament that praises rather than merely mourns, and the mode-switch into heroic *kleos*)
- **Anchor**: abstract and §2 (the question "when the lament song is used to praise"); published 2026
- **Quote 1** (facet: praise of the dead; 7 words): `the lament song is used to praise`
- **Quote 2** (facet: praise of the dead / heroic register; 10 words): `heroic kleos, that is, the glory that epic poetry grants`
- **Capture**: `evidence/S975.txt` + `evidence/S975.pdf` (276999 bytes)
- **sha256**: text `d6a08c21120ffdca8811c1a45c5ee18f0d85bc58c6c240c0f5061b2185e78835`; pdf `12c78b977924fe3190d198a85bd10decdb045bdf3b0df8c47868b1999c34bb05`
- **HTTP status**: 200

### S976 — Modern NW-Greek laments: semi-professional performers and therapeutic function (facet: professional keeners; gendered mourning rules)

- **Title**: Modern Laments in Northwestern Greece, Their Importance in Social and Musical Life and the "Making" of Oral Tradition
- **Author**: Athena Katsanevaki (University of Macedonia, Thessaloniki)
- **Venue**: Musicologist 1(1): 95–140 (2017). DOI 10.33906/musicologist.373186
- **URL**: https://dergipark.org.tr/en/download/article-file/753545
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary (fieldwork) for the semi-professional female lamenter and the lament-as-therapy role
- **Scope**: the *professional keeners* facet (the community-recognised semi-professional lamenter) and the *gendered mourning rules* facet (women as lament agents, protest as a general rather than gender-only function)
- **Anchor**: abstract and §4 (fieldwork interviews) and footnote 6; published December 2017
- **Quote 1** (facet: professional keeners; 6 words): `the women I interviewed were semi-professional`
- **Quote 2** (facet: gendered mourning rules / function; 6 words): `laments can function as music therapy`
- **Capture**: `evidence/S976.txt` + `evidence/S976.pdf` (8751711 bytes)
- **sha256**: text `151f00b755ab47912b452861ed55b3d8e9f4baa56a8a5cdab63cd2551251465f`; pdf `7022cd273a83118927e6b226be33000913fe051b1763aca62387aefb23c036c9`
- **HTTP status**: 200

### S977 — The lament as embodied learned practice, and the female default (facet: gendered mourning rules; speech-vs-song boundary)

- **Title**: Weeping out Loud: Embodiment in the Contemporary Lament Learning Process
- **Authors**: Elina Hytönen-Ng and Emilia Kallonen
- **Venue**: Journal of Somaesthetics 9(1): 148–162 (2024). DOI 10.54337/ojs.jos.v9i1/2.7916
- **URL**: https://journals.aau.dk/index.php/JOS/article/download/7916/6671
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for the contemporary transmission/learning of lament and its bodily technique
- **Scope**: the *speech-vs-song* facet (lamenting as bodily and vocal technique, crying while singing) and the *gendered mourning rules* facet (laments as predominantly women's oral tradition)
- **Anchor**: abstract and §Introduction (2024), pp. 148–162
- **Quote 1** (facet: gendered mourning rules; 8 words): `laments have predominantly been oral traditions among women`
- **Quote 2** (facet: speech-vs-song boundary; 5 words): `Lamenting is a bodily experience`
- **Capture**: `evidence/S977.txt` + `evidence/S977.pdf` (1113747 bytes)
- **sha256**: text `963ac4a256a9c2f023f95f22eb6ddd58d51d0e3ea8c0ca81502b35f08dedb60a`; pdf `ad5a2731b4b4c4d187dc511b5e8f0e839d500a1e42e532bd217fda9273e22507`
- **HTTP status**: 200

### S978 — Karelian/Lithuanian laments: female performance and improvised formulaic composition (facet: gendered mourning rules; formulaic grief content)

- **Title**: Reflections of Belief Systems in Karelian and Lithuanian Laments: Shared Systems of Traditional Referentiality?
- **Author**: Eila Stepanova
- **Venue**: Acta Baltica 15(1) (2011). DOI 10.15181/ab.v15i1.18
- **URL**: https://e-journals.ku.lt/journal/AB/article/1702/file/pdf
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary for Karelian/Lithuanian lament as improvised oral ritual poetry
- **Scope**: the *formulaic grief content* facet (laments as improvised works drawing on traditional language and motifs) and the *gendered mourning rules* facet (performance by women in ritual contexts)
- **Anchor**: abstract; published 2011
- **Quote 1** (facet: gendered mourning rules; 5 words): `usually performed by women during`
- **Quote 2** (facet: formulaic grief content; 9 words): `Laments are works of a special kind of improvisation`
- **Capture**: `evidence/S978.txt` + `evidence/S978.pdf` (616522 bytes)
- **sha256**: text `b816a70530a1ced0fed8d8de85822c79c6587b29513dc2aacb8a2f2e16a62cdb`; pdf `702d237193fc06fc316668faa365bf42c610d02f96f2f0e911fef9c3b545d162`
- **HTTP status**: 200

### S979 — Erzya lamentations as a surveyed genre with a professional trajectory (facet: professional keeners)

- **Title**: Natalia Ermakov Defended a Doctoral Thesis on Erzya Lamentations (News in Brief)
- **Author**: Natalia Ermakov / report in Folklore: Electronic Journal of Folklore 60 (2014)
- **URL**: https://www.folklore.ee/folklore/vol60/n02.pdf
- **Kind**: news brief / dissertation notice (peer-reviewed journal's News in Brief section) — **not** a research article
- **Tier**: **C** (lead only) — a news item about a dissertation, not a primary study; usable as a lead to Ermakov's dissertation, never as sole support for an entry claim
- **Scope**: the *professional keeners* facet, weakly — the trajectory from ritual lamentation to staged professional performance
- **Anchor**: whole item (1 page); published 2014
- **Quote** (facet: professional keeners; 9 words): `comprehensive survey of the history and role of the`
- **Capture**: `evidence/S979.txt` + `evidence/S979.pdf` (2375523 bytes)
- **sha256**: text `0561fba78bb0ac0c123a4a674e7b8b7809fc556774a63950629ca28d52f2056f`; pdf `1660525dc4f897b278248272bf7b1abf772f28657016a0751e1e35980abfe1dc`
- **HTTP status**: 200
- **Note for the L1**: tier C — do not cite as a supporting row for the entry; cite at most as a lead.

### S980 — Ingrian laments: questions, pleas and reproaches addressed to the dead (facet: address to the dead; formulaic grief content)

- **Title**: Suhde vainajaan inkeriläisissä kuolinitkuissa (The relation to the deceased in Ingrian death-laments)
- **Author**: Kaarina Koski
- **Venue**: ELORE 12(1) (2005) (Finnish Folklore Society journal)
- **URL**: https://journal.fi/elore/article/download/78499/39398
- **Kind**: paper (peer-reviewed journal article, in Finnish)
- **Tier**: **A** — peer-reviewed primary for the *address to the dead* content type in Ingrian death-laments (questions, pleas and reproach aimed at the deceased)
- **Scope**: the *formulaic grief content* facet, specifically the **address to the dead** sub-facet that no other candidate covers directly (questions, exhortations and reproach addressed to the corpse, e.g. being asked to rise from the grave)
- **Anchor**: abstract/opening section, pp. 1 ff.; published 2005
- **Quote** (facet: address to the dead; 6 words): `vainajille esitetään kysymyksiä, kehotuksia ja moitteita`
- **Capture**: `evidence/S980.txt` + `evidence/S980.pdf` (168933 bytes)
- **sha256**: text `369d694864a3a6c84a4e89307718e7b45771fcfcc5d9d5f1f3cb66ddfbfd21a9`; pdf `5120d34c053e5c44d267af340b7afc0d75e66123e503873ec7e62b883c4e3963`
- **HTTP status**: 200
- **Note for the L1**: source language is Finnish; the entry can carry the *structural* claim (that lament addresses the dead with questions, pleas and reproach) and cite the Finnish quote, but any rendering into English is the entry author's paraphrase and must be marked as such.

### S981 — Abanyole funeral poetry: named sub-genre, paid performers, gendered rules, praise (facet: professional keeners; praise of the dead; gendered mourning rules)

- **Title**: The Abanyole Dirge: "Escorting" the Dead with Song and Dance
- **Author**: Ezekiel Alembi
- **Venue**: Folklore: Electronic Journal of Folklore 38 (2008). DOI 10.7592/FEJF2008.38.alembi
- **URL**: https://www.folklore.ee/folklore/vol38/alembi.pdf
- **Kind**: paper (peer-reviewed journal article)
- **Tier**: **A** — peer-reviewed primary fieldwork on the Abanyole funeral-poetry system
- **Scope**: the *professional keeners* facet in a **non-European** tradition (performers who are rewarded with food, money and alcohol; specialists leading the most elaborate sub-genre), the *praise of the dead* facet (the songs praise the deceased's virtues and avoid the vices), the *gendered mourning rules* facet (the most elaborate sub-genre is reserved for morally upright men of the community) and the genre taxonomy the entry's design procedure needs (a named sub-genre with a fixed order of scenes)
- **Anchor**: §"Okhukoma performances and accompaniments" and §"Who performs?"; published 2008
- **Quote 1** (facet: praise of the dead; 12 words): `about the deceased: his or her virtues, relatives, friends and the village`
- **Quote 2** (facet: professional keeners / payment; 8 words): `reward the performers with food, money and alcohol`
- **Quote 3** (facet: gendered mourning rules; 12 words): `put up only for the morally upright male members of the community`
- **Quote 4** (facet: transmission / apprenticeship; 9 words): `no formal instruction of this art among the Abanyole`
- **Capture**: `evidence/S981.txt` + `evidence/S981.pdf` (320517 bytes)
- **sha256**: text `6dc403ae1d87eec240624186dd15c690c8d38e03b41a39052e9871fbbf7769b9`; pdf `8ce115500873f8a14112343ac0724baf6d63fded167cba66fc19b6ccf4b4de1a`
- **HTTP status**: 200

### Facet coverage of the proposed set (all six frozen sub-topics covered)

| frozen sub-topic | grounding rows |
|---|---|
| professional keeners | S972, S973, S976, S981 (A), S979 (C lead) |
| antiphonal lament | S970, S971 |
| lament refrain | S974 |
| praise of the dead | S974, S975, S981 |
| gendered mourning rules | S971, S973, S976, S977, S978, S981 |
| speech-vs-song boundary | S970, S972, S973, S977 |
| address to the dead (within "formulaic grief content") | S980, S974 |

Rows proposed: **12** (S970–S981), of which **11 tier A** and **1 tier C** (S979, lead only).
All twelve are opened by ordinary means and all twelve carry HTTP 200 and a verified
single-occurrence quote. The claim requires >= 3 qualifying rows; 11 tier-A rows are proposed.

With S981 the set now spans four cultural traditions for the professional-mourner facet
(Irish, Irish-gendered-office, modern NW Greek, and Kenyan Abanyole), so the non-European
gap that the first pass left open is closed.

---

## 3. Search log

All searching was by ordinary means only: plain `curl` / plain HTTPS API requests with the
default user agent, `-L`, `--max-time 30`. No headless browser, no CAPTCHA or challenge
passing, no login, no paywall circumvention, no TLS verification bypass. Date of every
query: **2026-11-05**.

Every row below was measured from the saved API JSON in the seat scratch
(`doaj*.json`, `oa*.json`, `cr*.json`), parsed with `json.load`. **identified** = the API's
own reported hit count; **screened** = records actually returned in the requested page and
read; **included** = candidates fetched and staged; **excluded** = screened − included.

| # | where | query | identified (API-reported) | screened (returned) | included | excluded |
|---|---|---|---|---|---|---|
| Q1 | DOAJ `/api/search/articles/` | `funeral lament` | 14 | 14 | 3 | 11 |
| Q2 | DOAJ | `ritual lament keening` | 0 | 0 | 0 | 0 |
| Q3 | DOAJ | `professional mourners dirge` | 0 | 0 | 0 | 0 |
| Q4 | DOAJ | `itkuviis` | 0 | 0 | 0 | 0 |
| Q5 | DOAJ | `moirologia` | 1 | 1 | 0 | 1 |
| Q6 | DOAJ | `weeping women lament folklore` | 0 | 0 | 0 | 0 |
| Q7 | DOAJ | `lament folklore journal` | 0 | 0 | 0 | 0 |
| Q8 | DOAJ | `antiphonal singing mourning` | 0 | 0 | 0 | 0 |
| Q9 | DOAJ | `itkuvirsi lament singing` | 0 | 0 | 0 | 0 |
| Q10 | DOAJ | `professional female mourners ritual` | 0 | 0 | 0 | 0 |
| Q11 | DOAJ | `dirge` | 32 | 25 | 0 | 25 |
| Q12 | DOAJ | `funeral songs mourning` | 2 | 2 | 0 | 2 |
| Q13 | Crossref `/works?query.bibliographic=&rows=15` | `antiphonal lament ritual mourning` | 62234 | 15 | 0 | 15 |
| Q14 | Crossref | `lament refrain formulaic` | 5301 | 15 | 0 | 15 |
| Q15 | Crossref | `professional mourners funeral song` | 1250496 | 15 | 0 | 15 |
| Q16 | Crossref | `dirge praise of the dead` | 85905 | 15 | 1 | 14 |
| Q17 | Crossref | `itkuviis lament refrain` | HTTP 429, empty body | 0 | 0 | 0 |
| Q18 | OpenAlex `/works?search=&per-page=25` | `funeral lament ritual` | 11837 | 25 | 2 | 23 |
| Q19 | OpenAlex | `professional keeners mourners` | 1878 | 25 | 2 | 23 |
| Q20 | OpenAlex | `itkuvirsi lament` | 36 | 25 | 3 | 22 |
| Q21 | OpenAlex | `Seto leelo` | 89 | 25 | 1 | 24 |
| Q22 | OpenAlex | `itkuviis` | 1 | 1 | 0 | 1 |
| Q23 | OpenAlex | `Maetagused lament Estonian ritual song` | 22 | 20 | 1 | 19 |
| Q24 | OpenAlex | `antiphonal lament dirge folklore` | 36 | 20 | 4 | 16 |
| Q25 | OpenAlex | `funeral lament formulae address to the dead` | 552 | 20 | 2 | 18 |
| Q26 | folklore.ee `/folklore/?s=lament` | site search | 1 | 1 | 0 | 1 |
| Q27 | folklore.ee volume index sweep (vol 20,25,30,35,40,45,50,55,60,65,70) | HTML index grep for lament/keening/dirge/mourn | 11 volumes scanned | 1 hit | 1 | 0 |

**Totals**: 27 query operations (25 API + 2 site); 263 API records returned and screened
(DOAJ 42 + OpenAlex 161 + Crossref 60), plus 2 site-search hits = **265 records screened**;
**12** direct captures included (11 tier A, 1 tier C); **253** excluded at screening.
A candidate may be returned by more than one query, so the per-query "included" counts sum
to more than 12 (Q1→3, Q16→1, Q18→2, Q19→2, Q20→3, Q21→1, Q23→1, Q24→4, Q25→2, Q27→1 = 20
query-candidate hits resolving to 12 distinct candidates).

Note on the Crossref and OpenAlex "identified" figures: they are the API's fuzzy-match
counts for the whole index (e.g. 1250496 for `professional mourners funeral song`), not the
size of a relevant set. Only the returned page was screened, so the screening burden is the
263 records actually read, not the API's headline totals.

### Exclusion reasons (per QUALITY criterion 37 — topic, access or scope; never title-only)

Fetched successfully at HTTP 200, read in full, and still excluded on **scope** (these are
the closest calls, and the reason each loses to a row already selected):

- Kama, Pikne (2017). "How old is runosong? Dating the motifs of burial-related folk songs by
  using archaeological material." Folklore: Electronic Journal of Folklore 68 —
  https://www.folklore.ee/folklore/vol68/kama.pdf (200, 8226843 bytes). Scope reason: the
  article is an **archaeological dating** argument about runosong motifs; it uses burial
  songs as a dating instrument and does not treat the lament as a speech register with
  performers, structure or content types.
- Jouste, Marko (2020). "Suonikylän kolttasaamelainen itkuperinne 1900-luvulla."
  Etnomusikologia — https://etnomusikologia.journal.fi/article/download/90118/57605 (200).
  Scope reason: an ethnographic inventory of one community's 20th-century repertoire; the
  register structure it documents overlaps S978's Karelian/Lithuanian comparative account,
  which is the stronger row for the same facet.
- Kalkun, Andreas (2014). "Seto Singing Tradition in Siberia: Songs and 'Non-Songs'."
  Folklore 58 — https://www.folklore.ee/folklore/vol58/kalkun_oras.pdf (200). Scope reason:
  Seto *leelo* performance in Siberia; a song tradition survey, not a lament register
  account, and S970 covers the Seto lament proper.
- Kalkun, Andreas (2017). "Introducing Setos on Stage: On the Early Performances of Seto
  Singing Culture." Folklore 68 — https://www.folklore.ee/folklore/vol68/kalkun.pdf (200).
  Scope reason: staged/performative Seto song history, not the mourning register.
- Korolëva, Svetlana (2018). "Cherdyn funeral laments: usage, ritual lexicon, the
  'letter-message' motif." Vestnik Permskogo universiteta, ser. Filologiia 10(2) —
  https://press.psu.ru/index.php/philology/article/download/1450/1082 (200). Scope reason:
  Russian-language study of one region's ritual lexicon and the *vestka* letter-message
  motif; the *address to the dead* facet it would serve is already grounded in English and
  Finnish by S980 and S974.
- "Lamentations in the Turkish culture and their functions in society — on the example of
  Kyrgyz." Uluslararası Türk Lehçe Araştırmaları Dergisi (2018) —
  https://dergipark.org.tr/tr/download/article-file/490587 (200). Scope reason: a general
  survey of lament function in one Turkic society; no distinct frozen sub-topic that the
  selected rows do not already cover.

Access exclusions (observed status):
- MDPI direct article pages and PDFs `https://www.mdpi.com/2077-1444/10/4/235`,
  `.../pdf`, `.../15/7/879`, `.../pdf`, `.../xml` → **HTTP 403** (bot wall) on every
  request, both with and without a trailing `?version=` query. Both MDPI candidates were
  recovered via the publisher's own asset host `https://mdpi-res.com/d_attachment/...`
  → HTTP 200, so neither is an exclusion in the final set.
- `https://minpaku.repo.nii.ac.jp/record/8716/files/SES105_14.pdf` (Gender Performativity
  in Burgenland Croatian Laments) → **HTTP 503** on two attempts. UNREACHABLE.
- `https://www.trad-culture.ru/sites/default/files/files_pdf/02_2026_...pdf` (Olonets
  Karelian prichitannye tradition) → **HTTP 404** on the URL as published by OpenAlex.
  UNREACHABLE at that locator.
- `https://durham-repository.worktribe.com/preview/1371952/20127.pdf` ("Pure Corpses,
  Dangerous Citizens", Transgressing the Boundaries between Experts and Mourners) →
  **HTTP 403**. UNREACHABLE.
- `https://doiserbia.nb.rs/img/doi/0350-0861/2012/0350-08611202139S.pdf` and the 2011
  sibling → connection **timed out** at 30 s on repeated attempts (host unreachable from
  here). UNREACHABLE. The same two titles were listed by DOAJ/Crossref but were not
  re-fetched from an alternative mirror, so they remain unsourced.
- `https://www.degruyterbrill.com/document/doi/10.2478/jef-2025-0006/pdf` →
  **HTTP 202 with 0 bytes** (challenge interstitial; no bytes served). UNREACHABLE at that
  route; the same article was obtained as HTTP 200 from `sciendo.com/pdf/...`.
- `https://journal.oraltradition.org/...` (Oral Tradition 23/2, "Thrênoi to Moirologia:
  Female Voices of Solitude, Resistance, and Solidarity") → **connection timed out** at 30 s
  on three separate attempts (site root, issue page and the PDF). UNREACHABLE. This was
  the single most on-point candidate for the *moirologia* / professional-mourner facet and
  it could not be captured, so no Oral Tradition row is proposed.
- `http://hdl.handle.net/10072/30483` ("Madwoman, Banshee, Shaman: Gender, Changing
  Performance Contexts and the Irish Wake Ritual") and `http://hdl.handle.net/1808/7785`
  ("Keening the Nation: The Bean Chaointe …") → **HTTP 200 but a JavaScript-only DSpace
  shell** (no article text in the served bytes). UNREACHABLE for a quote.
- `https://opus.bath.ac.uk/19457/1/Walter_Bt_Care_2008_27_3_p47.pdf` → HTTP 200 but the
  bytes are an HTML portal page, not a PDF. UNREACHABLE for a quote.
- `https://journals.openedition.org/efo/pdf/6912` and `https://journals.openedition.org/mondesanciens/729`
  → HTTP 200 but ~1.5 KB / 1.6 KB shells, not the article body. UNREACHABLE for a quote.
- `https://www.folklore.ee/tagused/mt2011.47.arukask.pdf` → **HTTP 404** (wrong filename
  pattern for Mäetagused).
- `https://www.folklore.ee/tagused/nr08/ing.pdf` → **HTTP 404**.
- `https://www.folklore.ee/folklore/vol58/kalkun.pdf` → **HTTP 404** (file is `kalkun_oras.pdf`).

Topic/scope exclusions (records identified but off-surface or already covered):
- Crossref: `Mourning Becomes Eclectic: Ritual Lament and the Problem of Continuity` (2005),
  `The Ritual Lament in Greek Tradition` (2002), `Antiphonal Lament Between Achilles and
  Briseis` (1997), `Thrēnos and Ritual Lament` (2010), `Do Brothers Weep? Male Grief…`
  (2017), `12 Virgilian Matres: From Maternal Lament to Female Sedition` (2020),
  `Radegund and Amalfrid in The Wife's Lament` (2021), `The Book of Ezekiel and
  Mesopotamian City Laments` (2011) — scope reason: literary-textual and historical
  scholarship on written/literary lament, not the **sung speech register** as a social
  institution with performers, refrain structure and design procedure; and no plain
  full-text OA capture was reachable.
- Crossref: `The Refrain in David's lament over Saul and Jonathan` (1972), `Refrain`
  (Oxford Music Online, 2001), `A Good Refrain Sells the Song` (2010), `A Nuclear Refrain`
  (2018), `Formulaic Language: An Overview` (2010) — scope reason: generic
  refrain/formulaic-theory chapters with no mourning-lament corpus and no OA capture.
- Crossref: `Funeral song poetry – source of the texts of funeral song collections`
  (2025), `Servile Mourning for the Powerful: … "Professional Mourners"` (2023),
  `Comforted But Not Compensated? …` (2015), `Mourners at Sir Philip Sidney's Funeral`
  (1941, three records) — scope reason: literary-historical or law-review treatment
  without an accessible full text; not usable for a quote under the ordinary-means rule.
- OpenAlex: `The Funeral Lament as an Anthropopoietical Ritual` (2018, hdl 11567/929623),
  `Of Commodified Grief and Emotions: Ghana's Itinerant Moirologists` (2025, Sage DOI),
  `A Witness to Death: The Journal of Emily Nash…` (2015, OhioLINK thesis), `Keening as a
  cross-cultural phenomenon` (1993, OhioLINK thesis), `Madwoman, Banshee, Shaman` (2009),
  `Pure Corpses, Dangerous Citizens` (2016), `Social Support in Perinatal Grief…` (2020) —
  access/scope reason: either the OA URL returned 403 or a JS-only shell, or the object is
  not about the lament register (perinatal grief support), or it is a thesis whose landing
  page carries no quotable body text.
- OpenAlex: `The Context and Structure of Funeral Oratory among the Bukusu` (2014),
  `Creative dynamism and religious syncretism in Igbo oral funeral songs` (2024),
  `The Therapeutic Dimensions of BaTonga Mourning Songs` (2025),
  `Modern Laments in Northwestern Greece` — the last one is **included** as S976; the
  others were excluded on topic/scope grounds (oratory rather than sung lament; Igbo
  syncretism; BaTonga therapeutic framing overlapping S972's clinical framing) with no
  capture made.
- folklore.ee site search `?s=lament` returned 1 hit, an unrelated "Estonian Parishes"
  article — scope reason.
- folklore.ee volume-index sweep of 11 volumes: only vol. 60 produced a lament-related
  record ("Defended a Doctoral Thesis on Erzya Lamentations"), included as S979 at tier C.

### Stop rationale
The stop was a **coverage** stop, not a volume stop. After 27 query operations and 265
screened records, all six frozen sub-topic phrases of the entry topic had at least one
tier-A primary capture with a verified single-occurrence quote:

- professional keeners → S972, S973, S976, S981 (four independent traditions: Irish wake,
  Irish gendered office, modern NW Greek, Kenyan Abanyole)
- antiphonal lament → S970 (Seto choral), S971 (Corsican voceru)
- lament refrain → S974 (Svan zär)
- praise of the dead → S974, S975, S981
- gendered mourning rules → S971, S973, S976, S977, S978, S981
- speech-vs-song boundary → S970, S972, S973, S977
- address to the dead → S980

Adding further candidates would have widened the sample without closing an unfilled
sub-topic, so the search stopped there. One gap was recorded rather than papered over and
then closed by a re-read: the first pass found no **non-European** professional-mourner
source (the Ghanaian *moirologists* article and the Oral Tradition *moirologia* article
were both UNREACHABLE), and S981 (Abanyole) closes it after a second read of an article
already fetched in the first pass.

Remaining gaps, recorded rather than hidden: the only captured source for the
*professional-mourner* facet outside Europe and Africa is a **news brief** (S979, tier C),
and no East-Asian or South-Asian professional-mourner tradition could be captured — the
Korean, Turkish and South-Asian candidates were either out of scope or on UNREACHABLE
hosts.

---

## 4. UNREACHABLE candidates (exact observed responses)

| candidate | URL | observed response |
|---|---|---|
| Thrênoi to Moirológia (Oral Tradition 23/2, 2008) | https://journal.oraltradition.org/wp-content/uploads/files/articles/23ii/07_23.2.pdf | curl exit 28, connection timed out after 30001 ms |
| Oral Tradition site root | https://journal.oraltradition.org/ | curl exit 28, connection timed out after 30001 ms |
| Oral Tradition issue page | https://oraltradition.org/index.php/23ii/ | curl exit 28, connection timed out after 30001 ms |
| MDPI Religions 10/235 article page | https://www.mdpi.com/2077-1444/10/4/235 | HTTP 403 |
| MDPI Religions 10/235 PDF | https://www.mdpi.com/2077-1444/10/4/235/pdf | HTTP 403 (408-byte body) |
| MDPI Religions 15/879 article page | https://www.mdpi.com/2077-1444/15/7/879 | HTTP 403 (400-byte body) |
| MDPI Religions 15/879 PDF | https://www.mdpi.com/2077-1444/15/7/879/pdf | HTTP 403 (408-byte body) |
| MDPI XML | https://www.mdpi.com/2077-1444/10/4/235/xml | HTTP 403 |
| Gender Performativity in Burgenland Croatian Laments | https://minpaku.repo.nii.ac.jp/record/8716/files/SES105_14.pdf | HTTP 503 (twice) |
| Olonets Karelian prichitannye tradition | https://www.trad-culture.ru/sites/default/files/files_pdf/02_2026_...95-108.pdf | HTTP 404 (25345-byte HTML error page) |
| Pure Corpses, Dangerous Citizens | https://durham-repository.worktribe.com/preview/1371952/20127.pdf | HTTP 403 (5486-byte body) |
| Shaping the pain (2012) | http://www.doiserbia.nb.rs/img/doi/0350-0861/2012/0350-08611202139S.pdf | curl exit 28, connection timed out after 30001 ms |
| Shaping the pain (2011) | http://www.doiserbia.nb.rs/img/doi/0350-0861/2011/0350-08611101071S.pdf | curl exit 28, connection timed out after 30001 ms |
| Seto lamenting song via De Gruyter | https://www.degruyterbrill.com/document/doi/10.2478/jef-2025-0006/pdf | HTTP 202, 0 bytes (challenge interstitial) |
| Seto lamenting song via De Gruyter (legacy host) | https://www.degruyter.com/document/doi/10.2478/jef-2025-0006/pdf | HTTP 202, 0 bytes |
| Madwoman, Banshee, Shaman | http://hdl.handle.net/10072/30483 | HTTP 200 but a DSpace JS-only shell (755 bytes, no article text) |
| Keening the Nation (Bean Chaointe) | http://hdl.handle.net/1808/7785 | HTTP 200 but a DSpace JS-only shell (827 bytes, no article text) |
| Mourners and mediums (Bath) | https://opus.bath.ac.uk/19457/1/Walter_Bt_Care_2008_27_3_p47.pdf | HTTP 200 but an HTML portal page, not a PDF (46859 bytes) |
| Semaine seto (OpenEdition) | https://journals.openedition.org/efo/pdf/6912 | HTTP 200 but a 1585-byte shell, no article body |
| Briséis et la plainte funèbre (OpenEdition) | https://journals.openedition.org/mondesanciens/729 | HTTP 200 but a 1585-byte shell, no article body |
| Mäetagused Arukask article | https://www.folklore.ee/tagused/mt2011.47.arukask.pdf | HTTP 404 (510 bytes) |
| Mäetagused Ing article | https://www.folklore.ee/tagused/nr08/ing.pdf | HTTP 404 (510 bytes) |
| Folklore vol. 58 Kalkun (wrong name) | https://www.folklore.ee/folklore/vol58/kalkun.pdf | HTTP 404 (510 bytes) |
| Crossref itkuviis query | https://api.crossref.org/works?query.bibliographic=itkuviis%20lament%20refrain | HTTP 429 (rate limited), empty body |

---

## 5. Manifest

| id | capture (staged) | bytes | sha256 | text sha256 | http |
|---|---|---|---|---|---|
| S970 | evidence/S970.pdf + S970.txt | 950971 / 118095 | e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e | dc7394e9862003b0b26e7631520e3dcb19832d25b19ddd4e6898cda06c371316 | 200 |
| S971 | evidence/S971.pdf + S971.txt | 927824 / 58596 | 85b821c7233c85bf1d3907b5db5ce98d368d19f6a06cdacc029a7df628345fbe | 656c45388dbfcab8f9de8a233eada5d8f8571647a1f04955605bff71cbc4a26a | 200 |
| S972 | evidence/S972.pdf + S972.txt | 324233 / 58354 | 1e0b0f8d8b529aae60ff2138d591aeb40465e778d11702b88b176d68334b30c8 | d3ff0209b9d80418bcc9345535f5fd440a3fc8a2433da6982c42a65d777293ce | 200 |
| S973 | evidence/S973.pdf + S973.txt | 1555760 / 59307 | 8750510347c20a3ef8a12112435cc917c2737a42a4ffeadab3f85b557720a5d9 | e017b3958dac14b32ff08a11f1750638e997c5df43ec9674a91413f5c42cac76 | 200 |
| S974 | evidence/S974.pdf + S974.txt | 1156987 / 80439 | f1e4be9fd0868713bf363ea18b368a501dd48d87dc7bd3039e801f4954ad2672 | 251b4d3f420164baa4bdc6508e54736cb0d00a42bc66940363203c264060159d | 200 |
| S975 | evidence/S975.pdf + S975.txt | 276999 / 66562 | 12c78b977924fe3190d198a85bd10decdb045bdf3b0df8c47868b1999c34bb05 | d6a08c21120ffdca8811c1a45c5ee18f0d85bc58c6c240c0f5061b2185e78835 | 200 |
| S976 | evidence/S976.pdf + S976.txt | 8751711 / 90907 | 7022cd273a83118927e6b226be33000913fe051b1763aca62387aefb23c036c9 | 151f00b755ab47912b452861ed55b3d8e9f4baa56a8a5cdab63cd2551251465f | 200 |
| S977 | evidence/S977.pdf + S977.txt | 1113747 / 49890 | ad5a2731b4b4c4d187dc511b5e8f0e839d500a1e42e532bd217fda9273e22507 | 963ac4a256a9c2f023f95f22eb6ddd58d51d0e3ea8c0ca81502b35f08dedb60a | 200 |
| S978 | evidence/S978.pdf + S978.txt | 616522 / 83658 | 702d237193fc06fc316668faa365bf42c610d02f96f2f0e911fef9c3b545d162 | b816a70530a1ced0fed8d8de85822c79c6587b29513dc2aacb8a2f2e16a62cdb | 200 |
| S979 | evidence/S979.pdf + S979.txt | 2375523 / 10004 | 1660525dc4f897b278248272bf7b1abf772f28657016a0751e1e35980abfe1dc | 0561fba78bb0ac0c123a4a674e7b8b7809fc556774a63950629ca28d52f2056f | 200 |
| S980 | evidence/S980.pdf + S980.txt | 168933 / 54041 | 5120d34c053e5c44d267af340b7afc0d75e66123e503873ec7e62b883c4e3963 | 369d694864a3a6c84a4e89307718e7b45771fcfcc5d9d5f1f3cb66ddfbfd21a9 | 200 |
| S981 | evidence/S981.pdf + S981.txt | 320517 / 32173 | 8ce115500873f8a14112343ac0724baf6d63fded167cba66fc19b6ccf4b4de1a | 6dc403ae1d87eec240624186dd15c690c8d38e03b41a39052e9871fbbf7769b9 | 200 |

Landing-page URLs for the L1's `corpus/SOURCES.md` URL column (the direct PDF URL is the one
actually fetched at HTTP 200):

- S970 https://sciendo.com/pdf/10.2478/jef-2025-0006 (doi:10.2478/jef-2025-0006)
- S971 https://journals.library.columbia.edu/index.php/currentmusicology/article/download/5043/2312/ (doi:10.7916/cm.v0i78.5043)
- S972 https://mdpi-res.com/d_attachment/religions/religions-10-00235/article_deploy/religions-10-00235.pdf (doi:10.3390/rel10040235)
- S973 https://mdpi-res.com/d_attachment/religions/religions-15-00879/article_deploy/religions-15-00879.pdf (doi:10.3390/rel15070879)
- S974 https://dergipark.org.tr/en/download/article-file/1673889 (doi:10.33906/musicologist.906765)
- S975 https://www.folklore.ee/folklore/vol99/avdikos.pdf (doi:10.7592/FEJF2026.99.avdikos)
- S976 https://dergipark.org.tr/en/download/article-file/753545 (doi:10.33906/musicologist.373186)
- S977 https://journals.aau.dk/index.php/JOS/article/download/7916/6671 (doi:10.54337/ojs.jos.v9i1/2.7916)
- S978 https://e-journals.ku.lt/journal/AB/article/1702/file/pdf (doi:10.15181/ab.v15i1.18)
- S979 https://www.folklore.ee/folklore/vol60/n02.pdf
- S980 https://journal.fi/elore/article/download/78499/39398
- S981 https://www.folklore.ee/folklore/vol38/alembi.pdf (doi:10.7592/FEJF2008.38.alembi)
