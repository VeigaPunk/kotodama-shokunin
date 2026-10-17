# R8-F07 freshness receipt — Shang oracle-bone residual (prior row R6-06-A)

- **Receipt:** R8-F07 (targets.json `freshness[6]`), round 8, 2026-10-17
- **Prior row:** R6-06-A, prior ledger `corpus/lessons/round-6-sources/06.json`, raw prior label **partial-support** (preserved untouched)
- **Entry:** `corpus/knowledge/civilizations/china-shang-zhou.md` — sha256 `905710ba79bb8c7ceae7f42562d5ae8177f14988d2f7c78ce0a14b619dfccb0b` (unchanged; no corpus bytes written)
- **Residual question:** Check the entry's oracle-bone language, divination and royal-ancestor coupling using an inscription/corpus or scholarly passage; do not turn one archive's genre into all Shang speech or belief.

**Prior limits being rechecked:** (1) the DB99 broad earliest-records wording does not independently establish the entry's earliest-securely-readable superlative; (2) "not a myth handbook" is a methodological inference; (3) no graphs or physical provenance inspected.

## Method

Live HTTP retrievals on 2026-10-17 with `curl -sS -L --max-time 40 -A '<browser UA>' -o <file> -w '%{http_code}' <url>` (UA: Chrome 126 string). Scratch in `/tmp/r8f07` (outside the repo). Quotes are whitespace-normalized; omissions are marked `[...]`; page-level ellipses are noted. Passage support is kept separate from whole-claim support.

## Fresh retrievals with substantive passages (9)

### R8F07-01 — entry-cited main source, fresh 200 re-fetch
- URL: https://afe.easia.columbia.edu/main_pop/ps/ps_china-oracle-bone-general.htm — **HTTP 200** — primary-text (DB99 reproduction, Columbia UP permission)
- Location: page introduction paragraph; excerpt inscription no. 8
- Quotes:
  - "The inscriptions give us a highly selective record of some of the concerns and events that were relevant to the elite class of the Shang kingdom."
  - "Through such divinations, the Shang hoped to discover the causes of events, the will of their ancestors and of their highest deity, Di, and the correct course of action to take when faced with difficult decisions."
  - "Discovered and translated beginning only in 1899, these oracle bones are the earliest written records of Chinese civilization."
  - "However, the only such Shang dynasty oracle bones discovered have been from the reigns of Wu Ding (r.1198-1189 BCE) and his successors."
  - "A hot bronze rod was applied, producing cracks, which were interpreted as answers to questions (often expressed as a pair of two possible outcomes) that the king and/or his diviner had posed."
  - Inscription no. 8: "Crack-making on yiwei (day 32), Gu divined: 'Father Yi (the twentieth Shang king, Xiao Yi, the father of Wu Ding) is harming the king.'"
- Supports: divination technique; royal-ancestor coupling; archive-selectivity limit (highly selective, elite, Wu Ding-and-successors only); broad "earliest written records" wording. Does not support: the strong "securely readable" form, "not a myth handbook" as a direct assertion, graphs/provenance.

### R8F07-02 — UNESCO World Heritage Centre, Yinxu
- URL: https://whc.unesco.org/en/list/1114/ — **HTTP 200** — repository/authoritative (description CC-BY-SA IGO 3.0)
- Location: "Outstanding Universal Value" section; "Yin Xu" summary
- Quotes:
  - "Numerous pits within the Palace area contained inscribed oracle bones considered to carry the earliest evidence of the Chinese written language." (Outstanding Universal Value)
  - "Inscriptions on oracle bones found in Yin Xu bear invaluable testimony to the development of one of the world's oldest writing systems, ancient beliefs and social systems." (Yin Xu summary)
- Supports: the "earliest" half of the entry's superlative, independent of DB99.

### R8F07-03 — Xinhua relay via State Council Information Office (2017-12-27)
- URL: http://english.scio.gov.cn/chinavoices/2017-12/27/content_50168640.htm — **HTTP 200** — news relay (tertiary; corroboration only)
- Location: body paragraph under the headline on the UNESCO Memory of the World inscription
- Quotes:
  - "Oracle bones are pieces of ox scapula or turtle plastron, which were used for divination during the late Shang Dynasty (1600-1046 B.C.)."
  - "They bear the earliest significant corpus of ancient Chinese writing and contain important historical information about the Shang."
  - "Around 160,000 pieces of oracle bone have been found so far, but of the 4,300 characters inscribed on them, only 1,600 have been decoded."
- Supports: superlative wording; **decipherment limit** (1,600 of 4,300 decoded) — a direct qualifier on "securely readable".

### R8F07-04 — peer-reviewed: Scientific Data 11:976 (2024)
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11379903/ — **HTTP 200** — peer-reviewed (Wang et al., doi:10.1038/s41597-024-03807-x)
- Location: Abstract; "Background & Summary"; Fig. 1 caption
- Quotes:
  - "Oracle bone script, one of the earliest known forms of ancient Chinese writing, presents invaluable research materials for scholars studying the humanities and geography of the Shang Dynasty, dating back 3,000 years." (Abstract)
  - "Oracle bone script, etched onto turtle shells and animal bones, stands as one of the earliest forms of writing discovered in China (see Fig. 1)." (Background & Summary)
  - "The content encompasses a range of topics including astrology, meteorology, animal husbandry, religion, and ritual practices." (Background & Summary)
  - "Of the 160,000 pieces unearthed, they reveal more than 4,600 distinct OBCs, yet only about a thousand of these have been deciphered, with their meanings and corresponding modern Chinese characters confirmed." (Background & Summary)
  - "They were all unearthed at the Huayuanzhuang East in Yinxu, China, and are currently housed at the Anyang workstation of the Institute of Archaeology, Chinese Academy of Social Sciences. These oracle bones date back to the reign of King Wu Ding of the Shang Dynasty." (Fig. 1 caption)
- Supports: superlative (weaker "one of the earliest known forms"), decipherment limit (~1,000 of >4,600 confirmed), physical provenance (excavation and curation). Not the exclusive ranking claim.

### R8F07-05 — Britannica topic page (pinned Wayback snapshot)
- URL: https://web.archive.org/web/20250125144009/https://www.britannica.com/topic/oracle-bone — **HTTP 200** — tertiary (corroboration only; direct URL 403, see failures)
- Location: excerpt under "Shang culture"
- Quote: "Shang is well known from oracle bones recovered from the site of the last Shang capital, near Anyang. The bones are turtle plastrons and ox scapulae with inscribed texts, used by the Shang kings in a highly regularized system of ritual divination and sacrifice aimed at securing the support of…" (the page's excerpt itself ends with a printed ellipsis)
- Supports: divination as regularized royal ritual; provenance near Anyang.

### R8F07-06 — Smarthistory "Oracle Bone, Shang Dynasty" (pinned Wayback snapshot)
- URL: https://web.archive.org/web/20241226155005/https://smarthistory.org/oracle-bone/ — **HTTP 200** — secondary-scholarly educational (direct URL 403, see failures)
- Location: object caption; essay opening paragraph; video transcript [0:04]–[3:34]
- Quotes:
  - Object caption: "Inscribed tortoise carapace (“oracle bone”), Anyang period, late Shang dynasty, c. 1300–1050 B.C.E., tortoise shell, China, 6.5 high x 10.8 x 2.3 cm (Arthur M. Sackler Gallery, Smithsonian Institution, Washington, D.C.: The Dr. Paul Singer Collection of Chinese Art of the Arthur M. Sackler Gallery, Smithsonian Institution, Washington, DC ; a joint gift of the Arthur M. Sackler Foundation, Paul Singer, the AMS Foundation for the Arts, Sciences, and Humanities, and the Children of Arthur M. Sackler, S2012.9.445)"
  - "The term “oracle bone” refers to ox scapulae (or shoulder blade bones) and tortoiseshells used by Shang rulers for divination. Oracle bones were said to offer a conduit to the spirits of royal ancestors, legendary figures from the past, nature deities, and other powerful spirits."
  - "Shang kings asked about natural events, illnesses, dreams, and forecasts for hunting and military endeavors."
  - Transcript [0:31]: "about 40 percent of them actually are decipherable"
- Supports: royal-ancestor coupling; divination; readability limit (~40%); **dated named object** (Sackler S2012.9.445). Text-only extraction; images not inspected.

### R8F07-07 — Wikipedia "Oracle bone" (tertiary; corroboration only)
- URL: https://en.wikipedia.org/wiki/Oracle_bone — **HTTP 200**
- Location: lead section; "Materials" section
- Quotes:
  - "Oracle bones bear the earliest known significant corpus of ancient Chinese writing, using an early form of Chinese characters." (lead)
  - "Diviners would submit questions to deities regarding weather, crop planting, the fortunes of members of the royal family, military endeavors, and similar topics." (lead)
  - "scholars have reconstructed the Shang royal genealogy from the cycle of ancestral sacrifices recorded on oracle bones" (lead)
  - "notations were often made on them recording their provenance (e.g., tribute of how many shells from where and on what date)" (Materials)
- Supports: corroboration for superlative, divination range, royal-ancestor coupling, shell provenance notations.

### R8F07-08 — Cambridge University Library Digital Library (WongAvery collection)
- URL: https://cudl.lib.cam.ac.uk/collections/wongavery — **HTTP 200** — repository
- Location: collection description paragraph
- Quote: "The collection includes oracle bones, the earliest known form of Chinese writing, offering a window into ancient Chinese divination practices and valuable insights into language development."
- Supports: superlative from a university repository; divination; collection provenance.

### R8F07-09 — Columbia University Libraries news (2017-09-05)
- URL: https://library.columbia.edu/about/news/libraries/2017/2017-09-05_Oracle_Bones.html — **HTTP 200** — library news
- Location: digitization-project paragraphs
- Quotes:
  - "Work to digitize the oracle bones, a collection that includes authentic, forged, and unconfirmed bones, began in 2015 and was completed last summer."
  - "The pieces were digitized using reflective transformation imaging (RTI), which captures the surface color and shape of the bone and allows users to \"re-light\" the bone from any direction, creating an interactive reproduction of each fragment."
  - "The original bones date to the Shang Dynasty, which reigned from 1600 to 1046 B.C.E., and will likely prove an invaluable resource to scholars of early Chinese history and language."
- Supports: physical provenance with an authenticity caveat (even curated collections include forged/unconfirmed pieces).

## Retrieved but no usable passage (2)

- Met "Shang and Zhou Dynasties" essay, Wayback snapshot 20241210055113 — HTTP 200, but the extracted text has no oracle-bone passage (its written-records sentence concerns ritual jades).
- British Library item `https://www.bl.uk/collection-items/oracle-bone` — HTTP 200 but JS-rendered: 231,063 bytes of HTML yield ~2.9 KB of extractable text with no object description.

## Access failures (6, with attempted command and status)

| URL | Status | Note |
|---|---|---|
| https://www.metmuseum.org/toah/hd/shzh/hd_shzh.htm | 429 | same as round 6 (twice); archived copy retrieved instead |
| https://www.britannica.com/topic/oracle-bone | 403 | direct blocked; archived copy retrieved instead |
| https://smarthistory.org/oracle-bone/ | 403 | direct blocked (consistent with round 6); archived copy retrieved instead |
| https://www.si.edu/search?edan_q=oracle%20bone%20shang | 403 | search blocked; not pursued |
| https://asia.si.edu/object/F1980.4/ | 403 | object probe blocked; accession unverified, abandoned rather than guessed |
| https://cudl.lib.cam.ac.uk/collections/oraclebones | 404 | guessed path wrong; corrected to /collections/wongavery (R8F07-08); also probed /collections/oracle_bones (404) and /view/MS-CUL-00001-00001 (500) |

Command form for all: `curl -sS -L --max-time 40 -A '<UA>' -o <file> -w '%{http_code}' <url>` on 2026-10-17.

## Passage-support summary

- **9 substantive fresh passages** (R8F07-01…09); **6 of 9 non-tertiary** (primary-text reproduction, UNESCO repository, peer-reviewed, secondary-scholarly archive, university repository, university library). Tertiary corroboration only: R8F07-03/05/07.
- Count basis: HTTP 200 retrievals with at least one extracted quotable passage in `/tmp/r8f07`, 2026-10-17.

## Prior-limit resolution

1. **Superlative** — *resolved in part.* Independent non-DB99 supports for "earliest": UNESCO "earliest evidence of the Chinese written language"; Xinhua "earliest significant corpus of ancient Chinese writing"; Cambridge UL "earliest known form of Chinese writing"; peer-reviewed "one of the earliest known forms". The **"securely readable" qualifier is qualified, not confirmed**: 1,600 of 4,300 characters decoded (Xinhua), ~1,000 of >4,600 confirmed (Scientific Data), ~40% decipherable (Smarthistory). Entry line 49's wording should carry a decode-limit note if revised (parent decision; no entry edit made here).
2. **"Not a myth handbook"** — *unresolved as a direct assertion.* Keyword sweep of all extracted texts (`grep` for "myth"/"literature", 2026-10-17) found no direct assertion; genre statements (ritual divination and sacrifice system; used for divination; highly selective record) are consistent with it. Remains a methodological inference (to-verify as a direct assertion).
3. **Graphs / physical provenance** — *resolved in part.* Dated named object now retrieved (Sackler S2012.9.445, c. 1300–1050 B.C.E.); institutional collections with authenticity caveat (Columbia RTI digitization); excavation/curation provenance (Huayuanzhuang East, Yinxu; CASS Anyang; Wu Ding reign). Still open: no oracle-graph image, rubbing or facsimile inspected — extraction was text-only.

## Whole-claim support (author-side; raw label untouched)

- Raw prior label preserved: **partial-support**. Author-side round-8 disposition: **partial-support (requested leg now satisfied; two residual limits)**.
- Basis: the requested inscription/corpus/scholarly-passage leg is now supplied by multiple independent sources including non-tertiary ones, plus a fresh 200 re-fetch of the entry-cited DB99 reproduction. The "do not generalize one archive's genre" instruction is now evidence-backed: the source's own selectivity wording and the Wu Ding-and-successors restriction independently reinforce it.
- Remaining limits: decode-limit note for "securely readable"; "not a myth handbook" direct assertion unverified; no graph/rubbing image inspected.
- No promotion claimed; this is an author-side recheck receipt, not independent promotion verification.

## Handoff notes

- Entry file not modified (sha256 unchanged). Scratch evidence retained at `/tmp/r8f07` (outside repo).
- For the parent: (a) if line 49 is revised, add the decode-limit qualifier rather than dropping the superlative, since "earliest extensive" is now multiply supported; (b) keep "not a myth handbook" flagged as inference or find a direct scholarly assertion; (c) pinned Wayback snapshots were required for Britannica/Smarthistory/Met — direct hosts returned 403/403/429 in both rounds.
