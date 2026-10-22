# ReviewCHead: falsify attack on claim C

- Seat: `KotodamaR51a3.ReviewCHead` (leaf; read-only on the lane; no subagents, no background jobs).
- Item attacked: claim C, `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (223 lines). Scope: head block (lines 1–12), §14 Recheck (line 217–219), §15 Scope, all 52 cited rows S071–S122, the in-corpus anchors and `- couples:` paths, the landed `corpus/README.md` and `corpus/SOURCES.md` edits, and the declared counting and separability commands.
- Commits: base `bff83ba65bf9559af4d7567e81703059667a0005`; claim C landed at `da31d3c`; records at `9feb69e` (used only for separability; records not otherwise attacked here).
- Access date for every URL below: 2026-10-22.
- Scratch, outside the lane: clone `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewCHead` (detached checkouts of bff83ba, da31d3c, 9feb69e); downloaded source copies and `manifest.json` in `/fast/scratch/hyaku/kotodama-r51a3-falsify/src`.
- Lane writes: this report only. No git add, commit, stash, checkout, switch, reset, pull or push in the lane. No jj. No pacman.
- Tooling: no installs. Used pre-installed `curl 8.23.0`, `pdftotext` (poppler) 26.08.0, `python3` 3.14.8. No tool was installed or updated.
- Fleet header sentence taken from `corpus/knowledge/verification/header-conformance-readings.md:3,:18,:28`; the fleet root `CORPUS.md` was not opened (fleet repo is out of bounds).

## Verdict: HOLDS-WITH-FIXES

The declared measurements hold: 227 files, `sweep.py` exit 0 with footer total 227 and linguistics 26, both gap sweeps 0 and 0 at base, all 52 cited rows carry the entry path in `used-by`, no forbidden citation string, no in-corpus anchor drift, separability exit 0 at the records tip, claims-agree exit 0.

The sourcing does not hold as written. Three high and thirteen medium cell-level defects: several cells cite a row for a claim the row's text does not carry, and several cells cite a row I could not open. Fix H1–H3 and mark or re-cite M1–M13 before the entry clears QUALITY criteria 1 and 6. The measured claim itself is not falsified.

## 1. Commands run (all in clone or read-only on lane)

| # | Command (abridged) | Exit | Result |
|---|---|---|---|
| 1 | `git log --oneline -6; git status --short` (lane) | 0 | HEAD `9feb69e`; `da31d3c`, `35f0d49`, `1f97472`, `5ab3634`, `bff83ba` below; untracked `.ufo/waves/round-51/` |
| 2 | `grep` tool with relative path `corpus/SOURCES.md` | tool error | path not found; reran with absolute paths |
| 3 | read `corpus/SOURCES.md:1-30`; rows at `:100-156` (raw) | ok | S071–S124 read verbatim |
| 4 | read entry `:1-12` raw; sibling `syntax-typology.md:1-12` | ok | head fields compared |
| 5 | `git clone -q --shared` to scratch; `git checkout bff83ba`; `find corpus/knowledge -name '*.md' \| wc -l` | 0 | 226 |
| 6 | gap filename sweep at bff83ba (`find … -iname '*sign-lang*' -o …`) \| `wc -l` | 0 | 0 |
| 7 | gap topic sweep at bff83ba (`grep -rliP '^- topic:.*\b(gestur\|sign language\|…)'`) \| `wc -l` | 0 | 0 |
| 8 | `ls corpus/knowledge/linguistics/*.md \| wc -l` at bff83ba | 0 | 25 |
| 9 | checkout `da31d3c`; count; linguistics count | 0 | 227; 26 |
| 10 | `python3 -B reports/round-28/readme/sweep.py` at da31d3c | 0 | `rows 227 files 227`; `missing_from_index 0`; `topic_mismatch 0`; `orphan_rows 0`; `header_drift {}`; footer total 227, `footer_ok True`; linguistics 26 |
| 11 | both gap sweeps at da31d3c (post-landing) | 0 | **1 and 1**: entry matches its own filename and topic line (see M2) |
| 12 | same two sweeps with `grep -v 'sign-languages-manual-modality'` at da31d3c | 0 | 0 and 0 (proposed recheck form) |
| 13 | tool presence `command -v pdftotext curl python3`; `import pypdf, fitz` | 0 | pdftotext, curl, python3 present; pypdf and fitz absent (not needed) |
| 14 | `curl -sSL --max-time 90` on 52 cited URLs plus alternates (12-way parallel, via `_eval`) | per URL | see §3 |
| 15 | retries: `eric.ed.gov/?id=EJ124326`; PubMed `?format=abstract`; `doi.org/10.1126/science.1100199`; `doi.org/10.1515/9783110261325` | per URL | ERIC 200 on retry (first try reset); PubMed 203; science.org 403; degruyter 202 empty |
| 16 | Python text probes over fetched copies (pdftotext for PDFs; tag-strip for HTML/JSON/XML) | ok | §3 |
| 17 | `grep -o 'S[0-9][0-9][0-9]' entry \| sort -u`; registry set difference | 0 | S071–S122 all cited (52); S123 and S124 not cited; S070 outside range |
| 18 | used-by count, first run (unpadded `seq`, my loop bug) | 0 | 23 (artifact) |
| 19 | used-by count, rerun zero-padded | 0 | **52 of 52** rows name `sign-languages-manual-modality.md` |
| 20 | `grep -ci 'round.\?51\|round51\|lessons/round\|boundary-count\|pastoralism'` on entry | 0 | 0 forbidden strings |
| 21 | `git diff --name-only bff83ba da31d3c -- corpus/knowledge` plus the 14 anchor files | 0 | only `culture-material/pastoralism-animal-husbandry.md` and the C entry changed; no anchor file changed |
| 22 | `git show --stat da31d3c` | 0 | README +20/-, SOURCES +59/-, entry +223 (C commit touches only these three) |
| 23 | separability at da31d3c: `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` | 2 | `SEPARABILITY_INPUT_ERROR … corpus/lessons/round-51.md absent` (expected before records commit) |
| 24 | same at `9feb69e` | 0 | `SEPARABILITY: 0 findings`; `units=3 ordered_pairs=6 acceptance_runs=2` |
| 25 | `python3 -B reports/round-51/claims-agree.py` at `9feb69e` | 0 | `AGREE claims=['C','D']` |
| 26 | `python3 -B tools/check-readme-revisions.py` at bff83ba and da31d3c | 0, 0 | `findings 0`, one `REVISION-ORPHAN` warning (lines 112, 123), present at base too (not introduced by C) |
| 27 | sibling sweeps, read-only, over `/home/vgpnk/Projects/shokunin/*/corpus/knowledge` excluding the lane | 0 | 21 trees including the lane, so 20 siblings; 0 topic hits and 0 filename hits (see L15) |
| 28 | field counts over `corpus/knowledge` | 0 | topic 227; sources 227; source 159; couples 227; verified-at 227; recheck 227; scope 17; gap filled 34 |
| 29 | `grep -n -E` for `translation-protocol-fidelity.md` sign-language content | 1 (no match) | none; only generic "interpreter" mentions (L2) |
| 30 | base body-mention grep for sign-language terms over `corpus/knowledge` | 0 | 14 files; all others are "design language" false positives or generic (no unnamed sign-language owner) |
| 31 | exact line lookup for each finding (`grep -n -F`) | 0 | line numbers in §4 |
| 32 | read anchors: adornment `:1-4,:70-82`; syntax `:96-101`; numerals `:104-109`; phonetics `:198-204`; writing `:9-23`; politeness `:73-78,:99-120`; conlang `:34-45`; language-contact `:103-107`; language-shift `:46-50`; sacred `:26-30`; morphological `:11-15`; sociolinguistics `:48-52`; worldbible `:15-19`; calibration `:33-40`; sound-symbolism `:30-34,:122-126` | ok | §2 |
| 33 | S108 locator check on raw XML (milestone indices) | ok | `n="422e"` at 127827, hands passage at 128077, `n="423a"` at 128369 |
| 34 | S086 font-shifted intro decode (+29 on glyph codes) | ok | "All known village sign languages are endangered usually because of pressure from larger urban sign languages" |
| 35 | final probes S071, S083, S098, S099, S111 | ok | §3 |

## 2. Declared counts, partial owners, couples, recheck

- Counts: base 226 and 25; landed 227 and 26; `sweep.py` exit 0; matches the head's `verified-at` line. Declared counts hold.
- Gap sweeps: 0 and 0 at base (re-run, as required). Post-landing they read 1 and 1 (self-match). The recheck line cannot return 0 as written (M2).
- Partial owners named in the head: `adornment-body-codes.md:77,:79` (title includes "Gesture and Posture"; §7 at line 77), `syntax-typology.md:99` (the only sign-language remark in that file), `numerals-and-measures.md:107` (finger counting; no sign-language mention). All hold. No unnamed sign-language owner found by row 30.
- Anchors cited in §2 and the head: phonetics `:201` ✔ (lines 201–203 say sign-language phonology works without acoustics); writing-systems `:21` ✔, `:20-21` ✔, `:11` ✘ for "secondary notation" (L4); politeness `:75` ✔ (names of the dead; occupational bans), `:77` ✔, `:101` ✔, `:118` ✔ (hay-biter, Javanese-style grading); conlang `:36` ✔ (start from the society), `:43` ✔ (Damin); language-contact `:105` ✔ ("a creole is a language like any other"); language-shift `:48` ✔ ("badly documented … signed and minority languages"); sacred `:28` ✔ (the register definition); morphological `:13` ✔ (synthesis axis); sociolinguistics `:50` ✔ ("chosen per setting"); worldbible `:17` ✔ content, path ✘ from linguistics/ (L3); calibration-registry `:35–39` ✔ codes R, C, B, H, T as described; `:38` = H ✔; sound-symbolism `:32` ✔, `:124` ✔ (signed channels, Perniss et al. 2010 `(to-verify)`).
- Couples: all paths exist (`phonetics-phonology.md`, `syntax-typology.md`, `numerals-and-measures.md`, `writing-systems.md`, `politeness-taboo-euphemism.md`, `language-contact.md`, `conlang-methodology.md`, `translation-protocol-fidelity.md`, `../culture-material/adornment-body-codes.md`). One parenthetical is not backed (L2).
- Anchors are unchanged since base (row 21), so "corpus bytes equal to base" in the head holds.
- Recheck (head line 11 and §14 line 219): actionable except the two sweeps (M2) and the re-open instructions for S080 and S094, which cannot be executed today (M3).
- Separability: C's `exports` pattern covers S071+; no D identifier cited by C; separability exit 0 at tip.

## 3. Sources opened, access 2026-10-22

Legend: ✔ holds; ✘ does not hold; NR not readable today. Tier column is the row's tier as filed in `corpus/SOURCES.md`, with my verdict after the arrow.

| Row (SOURCES line) | URL opened | Result | Quote or claim at anchor | Tier and scope |
|---|---|---|---|---|
| S071 (:100) | https://archive.org/details/micro_IA41153455_0834 (200); full text `…/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt` (200) | ok | Introduction Purposes quote verbatim ✔; "tab, dez, and sig … tabula, designator, and **signation**" ✘ row and entry say "signification"; no statement that sign languages do not derive from spoken languages ✘ | A ✔ |
| S072 (:101) | https://doi.org/10.1515/9783110261325 → degruyterbrill html | **202, empty body** NR | cannot check "does not derive…" or "acquired natively" (H1) | B publisher description used for world-level claims ✘ |
| S073 (:102) | https://glottolog.org/resource/languoid/id/sign1238 (200) | "Pseudo Family: Sign Language" ✔ | genealogy only; cited for transmission ✘ (M13/L6) | A ✔ for genealogy |
| S074 (:103) | https://gupress.gallaudet.edu/Books/T/The-Signed-English-Starter (200) | 940 basic signs ✔; "14 sign markers" ✔; "manual English system" ✔; "word order" 0 hits ✘; bilingual education 0 hits ✘ | B publisher description ✔ for the work |
| S075 (:104) | https://pmc.ncbi.nlm.nih.gov/articles/PMC4821822/ (200) | sawmills ✔; monastic silence ✔; mourning taboo ✔; pantomime stage ✔; emblems ✔ | A ✔ |
| S076 (:105) | https://nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ (200) | term list ✔; "no longer accepted by most" ✔ | A ✔ term scope |
| S077 (:106) | https://www.un.org/en/observances/sign-languages-day (200) | "fully fledged natural languages" ✔; "more than 300" ✔; "pidgin … limited lexicon" ✔; "more than 70 million" ✔; "vital" ✔ | B ✔ |
| S078 (:107) | https://wfdeaf.org/resources/sign-language-rights/ (200) | "Each sign language has its own structure, grammar, and lexicon, equaling spoken languages in every respect" verbatim ✔; "Language and culture are inseparable" ✔ | B ✔ |
| S079 (:108) | https://voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement/ (200) | "structured like the early communication systems" ✔; "not a conventional system" for co-speech gesture ✘ (not on page) | **A ✘ → B** (author's own research summary) |
| S080 (:109) | https://pubmed.ncbi.nlm.nih.gov/15375269/ (203, cookie wall, 193 chars); `?format=abstract` (203); https://doi.org/10.1126/science.1100199 → science.org (403) | **NR** | "over about 25 years" and "regularized grammar" unverified (M3) | B abstract; cannot check |
| S081 (:110) | https://books.google.com/books/about/Sign_Languages_of_Aboriginal_Australia.html?id=Aa34NAEACAAJ (200) | "nine years" ✔; "first book-length study" ✔; speech ban, mourning, women 0 hits ✘ | B publisher text ✔ for the work only |
| S082 (:111) | https://gupress.gallaudet.edu/Books/M/Manual-Communication (200) | TOC: Signed English, Signing Exact English, Pidgin Sign (Contact Sign), Cued Speech ✔; "therapy" 0 hits ✘ | B ✔ |
| S083 (:112) | https://pure.hw.ac.uk/ws/portalfiles/portal/15283839/AT.pdf (200) | ASL and LIS one-handed ✔; "ISL is a one-handed system" ✔ (Irish SL, citing Cormier et al. 2008); BSL, Auslan, NZSL two-handed ✔; initialization linked to time constraints ✔; "contact traces" ✘; "word order" 0 hits ✘ | A ✔ |
| S084 (:113) | https://www.signwriting.org/ (200) | "Sign Languages are written languages!" ✔; country pages ✔ | A promotional site; narrow maintainer statement, borderline |
| S085 (:114) | https://www.nidcd.nih.gov/health/american-sign-language (200) | "ASL is a complete, natural language" ✔; "There is no universal sign language" ✔; fingerspelling ✔ | A official fact sheet ✔ |
| S086 (:115) | https://pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf (200, 18 MB; intro glyph-shifted, decoded by hand) | "All known village sign languages are endangered usually because of pressure from larger urban sign languages" ✔; shared between deaf and hearing ✔; alternate signing during mourning or hunting ✔; "nearly 130 deaf individuals" (Al-Sayyid) ✔ | A ✔ |
| S087 (:116) | https://linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf (200) | "several generations" ✔; Managua school 1977 ✔; "about 130 deaf" ✔; compounding ✔; "little or no inflectional morphology" ✔; "3–6 generations" ✘ (M4) | A ✔ |
| S088 (:117) | https://pages.ucsd.edu/~cpadden/files/Padden%20SL%20Geography.pdf (200) | "around 250,000" ✔; 1817 Hartford ✔; "two or three generations" ✔; "peer" 0 hits ✘ (M5); homesign only as a question ✘ | A but a draft chapter (L13) |
| S089 (:118) | https://www.routledge.com/The-Resilience-of-Language-…/p/book/9781841694368 (200) | description mentions gesture creation in deaf children ✔ (homesign term not probed) | B ✔ for the book |
| S090 (:119) | https://makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx (200) | "symbol" present ✔; row's quote not re-verified verbatim; "not a sign language proper" ✘ (row gloss) | **A ✘ → B** (organisation's self-description) |
| S091 (:120) | https://www.lotpublications.nl/Documents/151_fulltext.pdf (200) | "from 10% in 1971 to around 2%" and "more than 10% in 1961 … 2% in 2001" ✔; "only an estimated 5% of Deaf children are born to Deaf parents" ✔; "former chief … prohibited marriage between two deaf persons" ✔; "most adult members … acquired sign language only after entering school" ✔ (scope drift M6) | A ✔ |
| S092 (:121) | https://www.elararchive.org/dk0124 (200) | "at least seven generations" ✔; 48 deaf ✔; ~1,200 hearing ✔; Indonesian Sign Language ✔; marital patterns ✔ | A ✔ |
| S093 (:122) | https://www.hup.harvard.edu/books/9780674270411 (504 today); Wayback https://web.archive.org/web/20241210011800/https://www.hup.harvard.edu/books/9780674270411 (200, 2024 capture) | "extremely high rate of profound hereditary deafness" ✔; "Deaf people were included in all aspects of life" ✔ | B publisher description ✔ for the work; used for island fact at entry :75 (M13); live page 504 (L14) |
| S094 (:123) | https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls (403, Cloudflare) | **NR** (no bypass attempted) | "~45 primes", six-shape set, 1974 attribution unverified (H3) | A cannot check |
| S095 (:124) | https://discovery.ucl.ac.uk/id/eprint/10054130/1/Brentari_Sign%20Language%20Phonology.book.chapter.pdf (200) | "four major body regions … eight place distinctions" ✔; "syllable nucleus" ✔; orientation "minor parameter … fewer minimal pairs" ✔; nonmanual inventory ✘ (M10) | A ✔ |
| S096 (:125) | http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ (200) | minimal pairs ✔; "Battison (1978) proposed … palm orientation … fourth phonological parameter" ✔ (year 1978, conflicts with H3) | B ✔ |
| S097 (:126) | http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ (200) | "95.9% and 87%" ✔; "Battison (1978, p.33–35)" ✔; passive set lists seven incl. S ✘ vs entry's six (M11) | B ✔ |
| S098 (:127) | https://cnlse.es/antiguos/Nonmanuals.their%20grammatical%20and%20prosodic%20roles.pdf (200) | "the most common marker is a side-to-side headshake" ✔; eyebrow positions ✔; topics at left edge ✔; loci ✔; agreement ✔ | B ✔ (survey chapter) |
| S099 (:128) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3688355/ (200) | "the handshape which identifies the class of the referent" ✔; entity constructions ✔; "classifier" contested ✔ | A ✔ |
| S100 (:129) | https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ (200) | "subject precedes object (in all 32 cases)" ✔; S-O-V ✔; "In the space of one generation … systematic grammatical structure has emerged" ✔ | A ✔ |
| S101 (:130) | https://www.benjamins.com/catalog/gest.13.3.03pad (200) | "silent gesturers largely prefer a handling strategy" ✔; instrument ✔; "patterned iconicity" ✔; "three unrelated sign languages" ✔ | B abstract ✔ |
| S102 (:131) | https://eric.ed.gov/?id=EJ124326 (000 reset, then 200 on retry) | "a tendency for signs to change in the direction of arbitrariness" ✔ | B ✔ |
| S103 (:132) | https://assets.cambridge.org/97805217/70620/excerpt/9780521770620_excerpt.pdf (200) | "They are not mime or playacting" ✔; TREE in ASL, Danish, Chinese "equally iconic but different in form" ✔; "neither arbitrary nor predictable but rather motivated" ✔ | A ✔ |
| S104 (:133) | https://glottolog.org/resource/languoid/id/lsfi1234 (200) | LSFic pseudo-family ✔ | A ✔ |
| S105 (:134) | https://glottolog.org/resource/languoid/id/amer1248.json (200) | ASL classifies under LSFic ✔ | A ✔ (could carry H1) |
| S106 (:135) | https://glottolog.org/resource/languoid/id/bsli1234 (200) | BANZSL "argued by Adam Schembri and Kearsy Cormier …" ✔ | A ✔ |
| S107 (:136) | https://glottolog.org/resource/languoid/id/banz1243.json (200) | BANZSL children incl. BSL and NZSL ✔ | A ✔ |
| S108 (:137) | https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0059/tlg005/tlg0059.tlg005.perseus-grc2.xml (200) | "εἰ φωνὴν μὴ εἴχομεν … ταῖς χερσὶ καὶ κεφαλῇ καὶ τῷ ἄλλῳ σώματι" lies between milestones 422e and 423a ✔ | A ✔ |
| S109 (:138) | https://konferens.ht.lu.se/kendonsymposium2023/abstracts/ (200) | "predominantly used by hearing people as an alternative to speech when speech is either impractical or disallowed for cultural reasons" ✔; Warlpiri ✔ | B abstract ✔ |
| S110 (:139) | https://assets.cambridge.org/97805216/90300/excerpt/9780521690300_excerpt.pdf (200) | "Though now endangered" ✔; trade and alliances ✔; "Indian Sign Language Council, 1930" (ch. 5) ✔; "Plains Indian Sign Talk" 0 hits ✘ (L7) | B ✔ |
| S111 (:140) | https://www.archives.gov/research/guide-fed-records/groups/106.html (200) | film project "(13 reels)" and "ca. 1930-31" ✔; council 0 hits ✘ (L7) | A ✔ |
| S112 (:141) | https://assets.cambridge.org/97805211/23938/excerpt/9780521123938_excerpt.pdf (200) | "1078 or shortly thereafter (Bernard) and 1079–1084 (Ulrich)" ✔; "to the end of the twelfth century … widespread" ✔; "necessary for the operation of the abbey" ✔ | B ✔ |
| S113 (:142) | https://wfdeaf.org/wp-content/uploads/Perspectives-on-the-Concept-and-Definition-of-IS_Mesch-FINAL.pdf (200) | "Most of the respondents don't agree International Sign is a pidgin or a Creole" ✔; "no native users of IS as a first language" ✔; conventionalisation critical ✔ | A ✔ |
| S114 (:143) | https://wfdeaf.org/position-paper-on-the-right-of-deaf-people-to-choose-and-access-international-sign-interpretation-services/ (200) | right to choose between IS and national sign languages ✔; "unregulated" ✔; "universal" 0 hits ✘; "substitute" 0 hits ✘ (M8) | A policy statement; descriptive reuse ✘ |
| S115 (:144) | http://www.cslds.org/apsl-consortium/sign-linguistics/4-sign-phonetics-and-phonolgy-stokoes-notation-symbol/ (200) | "location (tab), handshape (dez), and movement (sig)" ✔ | B ✔ |
| S116 (:145) | https://www.sign-lang.uni-hamburg.de/dgs-korpus/hamnosys-97.html (200) | "phonetic" transcription ✔; "current version 4" ✔; "does not refer to national diversified finger spelling and therefore can be applied internationally" ✔ | A ✔ |
| S117 (:146) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10622114/ (200) | "Fingerspelling is a critical component of many sign languages … manual representation of orthographic code" ✔ | A ✔ (cited at entry :190) |
| S118 (:147) | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/deafed/enp026&resultType=core&format=json (200, JSON) | abstract: "a utopia in the eyes of many Deaf people" ✔ | B abstract ✔ |
| S119 (:148) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6818964/ (200) | split at age 12 ✔; "decades of experience" only in a quoted case ✘ (M9) | A ✔; the B-coded claim is mis-scoped |
| S120 (:149) | https://www.ethnologue.com/subgroup/2/ (200) | "Subgroup of 161 languages"; "Deaf community sign language 131"; "Shared sign language 29"; International Sign under "Sign language" ✔ | A ✔ |
| S121 (:150) | https://wfdeaf.org/contact/faqs/ (200) | "200+ national sign languages … only 40% … legally recognised" ✔; "These terms are not acceptable. The preferred term is 'deaf'" ✔; "more than 70 million deaf people belong to signing deaf communities" ✔ | B ✔ |
| S122 (:151) | https://link.springer.com/article/10.1186/1477-7517-9-16 (200, "Client Challenge" page, 3 KB) | **NR** | capital-D claim unverified (M3) | A cannot check; paper's subject is clinical and education policy, so the terminology use needs its own scope note |

Rows S123 and S124 are queued, not cited, and were not opened.

## 4. Findings

Severity: high = a cited row does not carry the claim, or a cell cannot be checked and is asserted; medium = scope, terminology or tier defect that changes what a reader would conclude; low = anchor, format or wording.

### High

- **H1. Master claim cites rows that do not carry it.** `sign-languages-manual-modality.md:16` (also `:19`): "does not derive from any spoken language (S071; S072)". S072 (`SOURCES.md:101`) is not readable today (202, empty body) and is a publisher description used for a world-level claim, which QUALITY criterion 6 does not license. S071 (`SOURCES.md:100`) has no statement of independence; searches for derive, derivative and not-English phrasings returned eight hits, none on point. *Smallest fix:* cite S104–S105 for the genealogy clause (`SOURCES.md:133–134`: ASL classifies under LSFic) and remove S072 from that cell, or mark the clause `(to-verify)`.
- **H2. S074 cited for claims it does not contain.** `sign-languages-manual-modality.md:26` ("a designed code that keeps the spoken word order (S074)"), `:157` ("arranges a borrowed sign vocabulary in English word order (S074)" and "not ASL-English bilingual education (S074)"). S074 (`SOURCES.md:103`) describes 940 signs, 14 sign markers and "a manual English system"; "word order" and bilingual education each have zero hits in the fetched page. *Smallest fix:* delete the three clauses, or cite a source that states them and mark `(to-verify)` until it is opened.
- **H3. Four S094 cells rest on an unreadable row whose year conflicts with readable sources.** `sign-languages-manual-modality.md:83` (palm orientation), `:87` ("~45 handshape primes", S094), `:90` ("Battison added it as a fourth parameter (S094)"), `:92` (six-shape passive set, S097 and S094), `:93` (minimal-pair list, S094). S094 (`SOURCES.md:123`) returns 403 (Cloudflare). Readable S096 (`SOURCES.md:125`) attributes the fourth-parameter proposal to "Battison (1978)"; readable S097 (`SOURCES.md:126`) attributes the Symmetry Condition to "Battison (1978, p.33–35)". The 1974 row may still be right; it cannot be checked today. *Smallest fix:* add a Battison 1978 row (superseding wording in the registry) and cite it where S096/S097 do; mark the ~45 count and the minimal-pair list `(to-verify)` until the 1974 paper is opened. See L12 on how that row was accessed.

### Medium

- **M1. Stokoe's term and an unsupported adjective.** `:16` "signification (movement)" should be "signation (sig)": S071 says "Tab, dez, and sig are shortened forms of the terms tabula, designator, and signation" and "the action of the sign (siqnation, or sig)". `SOURCES.md:100` repeats the error; the registry allows only a superseding row for teaches text. Also `:16` "first brought" — "first" is not in S071. *Smallest fix:* entry → "signation (sig)", drop "first"; add a row "supersedes S071 — …".
- **M2. Recheck cannot return 0 after landing.** `:11` and `:219`: "re-run the two gap sweeps" returns 1 and 1 at `da31d3c`, both on this entry (row 11). *Smallest fix:* append `| grep -v 'sign-languages-manual-modality'` to each sweep; this returns 0 and 0 (row 12).
- **M3. Unreadable rows carry cells with no declared status.** S072 (`SOURCES.md:101`; cells at `:16,:19`); S080 (`:109`; cells at `:126` "over about 25 years" and `:131` "regularized grammar"; PubMed 203 cookie wall, DOI 403); S094 (`:123`; cells at `:83–:93`); S122 (`:151`; cell at `:211`, "capital D is the scholarly convention", unverified). *Smallest fix:* mark each dependent cell `(to-verify)` inline; record the access failure and error text in each row's recheck column (status and recheck may change in place per the registry header).
- **M4. Numeric range not in the source.** `:59` "3–6 generations (S087)" (`SOURCES.md:116`). S087 gives "several generations", "five generations (about 75 years ago)" for one founding family, and "four generations … exist simultaneously" for the Israeli deaf community. *Smallest fix:* restate in the source's terms or drop the range.
- **M5. Transmission terms not in S088.** `:58` "generational plus peer-to-peer among unrelated signers (S088)"; `:60` "mostly peer-to-peer, seeded by homesign (S088)". The fetched S088 text has zero "peer" hits and poses the homesign contribution as a question. *Smallest fix:* drop "peer-to-peer"; mark the homesign seeding `(H)` or cite a row that states it.
- **M6. Population drift.** `:76` "most Deaf children learn their sign language only after entering school". S091 (`SOURCES.md:120`) says "most adult members of the large Deaf communities acquired sign language only after entering school". *Smallest fix:* restore "adult members … acquired".
- **M7. S083 cells say more than the paper says.** `:154` "as contact traces (S083)" — the paper ties initialization to time constraints in TV interpreting; "contact traces" is the registry gloss (`SOURCES.md:112`). `:154` "evidence that signed grammar mirrors spoken word order (S083)" — the paper has no word-order claim. *Smallest fix:* replace with the paper's account; delete the word-order clause.
- **M8. A rights position restated as practice.** `:156` "deaf people choose it alongside national sign languages (S114)" — S114 (`SOURCES.md:143`) is a position paper on "the right of deaf people to choose"; `:156` "a universal sign language or a substitute for a national sign language (S114)" — neither word appears in S114. *Smallest fix:* "WFD holds that deaf people have the right to choose International Sign or a national sign language (S114)"; drop "substitute" unless sourced.
- **M9. A B-coded claim mis-scoped.** `:208` "late first-language exposure lowers ultimate attainment, even after decades of signing (S119)". In S119 (`SOURCES.md:148`) "decades of experience" occurs only inside a quoted case report. The B code (`calibration-registry.md:37`) requires population and exception qualifiers the cell lacks. *Smallest fix:* drop "even after decades of signing", or quote the case with attribution and add population and exception qualifiers.
- **M10. Nonmanual inventory cited to the wrong row.** `:91` "eyebrows, gaze, mouth, head tilt (S095)". S095 (`SOURCES.md:124`) defers nonmanuals to Pfau & Quer 2010; eyebrows and head tilt are not in it. S098 (`SOURCES.md:127`) supports eyebrows and headshake. *Smallest fix:* cite S098 for the inventory.
- **M11. Passive-hand set does not match the cited row.** `:92` "(A, B, 5, G, C, O) (S097, S094)". S097 (`SOURCES.md:126`) lists seven: "A, S, B, 5, G (i.e., 1), C and O". *Smallest fix:* use S097's seven, or the S094 six once S094 is verified, and name the source.
- **M12. Speech-ban, mourning and women cited to S081.** `:40` and `:135` ("speech is banned (S081)"); `:139` "(S081, S109)"; `:190` "mourning alternate sign used by hearing women (S081)". S081 (`SOURCES.md:110`) mentions none of speech, mourning or women. S109 (`SOURCES.md:138`) and S075 (`SOURCES.md:104`, "a taboo on speaking during mourning") carry the content. *Smallest fix:* drop S081 from those cells.
- **M13. Tier and criterion 6.** S079 (`SOURCES.md:108`) and S090 (`:119`) are filed tier A but are self-descriptions (a principal investigator's research summary; a charity's own page). S090's teaches text says "not a sign language proper", which is the lane's gloss, not the page's. Publisher descriptions carry world-level claims: S093 at `:75` (Martha's Vineyard island history), S110 at `:140` (council), S074 and S081 as above. *Smallest fix:* superseding rows re-tiering S079 and S090 to B; cite the book's text or S118 for island facts; remove the gloss from S090's teaches.

### Low

- **L1. Head fields.** `:5–:12`. The entry carries both `- sources:` (`:5`) and a separate singular `- source:` (`:9`). `header-conformance-readings.md:4` records the lane shard protocol as "plural `- sources:` is the source leg, no separate singular line added"; the fleet sentence (`header-conformance-readings.md:3,:28`) asks for `source:`, `verified-at:`, `recheck:` at the opening, and the entry's order (topic, gap filled, sources, couples, source, verified-at, recheck, scope) does not open with them. Not a measured falsifier. *Fix:* route to the integrator; no change under claim C.
- **L2. Coupling parenthetical unsupported.** `:8`: "translation-protocol-fidelity.md (… interpreting between signed and spoken languages is one live case)". The file has no sign-language or signed-language content (row 29). *Fix:* drop the parenthetical or cite a real anchor.
- **L3. Unresolvable relative path.** `:50`: `worldbible-integration-contract.md:17` (bare). The file is in `synthesis/`. *Fix:* `../synthesis/worldbible-integration-contract.md:17`.
- **L4. Anchor does not say what the cell says.** `:27`: "a writing system: a secondary notation of a language (writing-systems.md:11)". Line 11 is the Daniels typology opener and does not say "secondary notation". *Fix:* cite a line that says it, or drop "secondary".
- **L5. Uncited inference inside a cited paragraph.** `:112`: "a young sign language reads more iconic than an old one" follows S102 and S103, neither of which says it. *Fix:* mark `(H)` per `calibration-registry.md:38`, or cite.
- **L6. Terms not on the cited pages.** `:63` "therapy settings" (S082, `SOURCES.md:111`; no "therapy" on the page); `:64` "information-bearing but not a conventional system (S079)" (not on the page; the page says gestures "play a role in how we think and talk"). *Fix:* drop "therapy settings"; cite S089 or drop the phrase.
- **L7. Council and label attribution.** `:140`: "a 1930 council was filmed to record it (S111)" — the council is in S110 (`SOURCES.md:139`, "The Indian Sign Language Council, 1930"); S111 (`:140`) has no "council". "Plains Indian Sign Talk" is not the excerpt's name (zero hits for "Sign Talk"). *Fix:* cite (S110, S111); attribute the label or use the excerpt's term.
- **L8. NON-CANON example launders a source.** `:190`: "congenital deafness concentrated in two kindreds (S086)" cites a real source for an invented choice. The NON-CANON label is present. *Fix:* mark the choice as design `(H)` or drop the citation.
- **L9. Ambiguous abbreviation.** `:153` "one-handed (ASL, LIS, ISL)". The claim holds: S083 uses ISL for Irish Sign Language and says it is one-handed. S087 (`SOURCES.md:116`) and S100 use ISL for Israeli Sign Language. *Fix:* write "Irish Sign Language (ISL)" on first use.
- **L10. "Register" in several senses.** `:14` heading "The register property"; `:33` "keeps its own register"; `:135` "a manual register"; `:139` "lexicon-swap register"; `:156` "meeting/interpreting register". The sociolinguistic sense is at `sociolinguistics-registers.md:50`. *Fix:* "system" or "code" for manual systems; reserve "register" for the sociolinguistic sense.
- **L11. Unlabelled design rules in §10.** `:153–:158`. §9 says its design column is H (`:145`); §10 does not. *Fix:* state the same label in §10.
- **L12. Access basis of S094.** `SOURCES.md:123` says the row was "opened via headless browser" past a Cloudflare gate. The lane's access rule forbids paywall or bot-gate bypass. I did not repeat it. *Fix:* confirm the access basis; if it was a bypass, re-tier the row as unverified.
- **L13. Draft tiered as A.** `SOURCES.md:117` (S088): "draft chapter", filed A. *Fix:* superseding row at B, or cite the 2011 published chapter.
- **L14. Live page down, capture used.** `SOURCES.md:122` (S093): the live URL returned 504 on 2026-10-22; the evidence is a 2024 Wayback capture. *Fix:* state the capture date in the row.
- **L15. Sibling count wording.** Claim C's gap evidence says "21 sibling lanes"; my read-only count is 20 siblings (21 corpus/knowledge trees including the lane). Both sweeps return 0 in all 20. *Fix:* wording only, in `reports/round-51/claims.json`.

## 5. Residual risk and verification gaps

- Not readable today: S072, S080, S094, S122 (table §3). Cells that depend on them are unverified, not refuted. Access is not bypassed.
- S093 was read from a 2024 Wayback capture; the live page returned 504.
- S086 intro was decoded by hand from a glyph-shifted PDF (offset +29); the quoted sentence is clear in the decode but a page image check would be stronger.
- Not checked: the round lesson's Gate quotes (`corpus/lessons/round-51.md`), which the head's line 7 relies on; the S101 and S112 full wording; S087 "everyone acquires from birth" (`:59`); S088 "generational" element; S120 "Plains and Australian" filing; §12 invented facts beyond the NON-CANON label.
- Falsifier "a non-author review finding that the entry restates an existing owner's register": none found. §3 gesture-boundary row (`:64`) and §1 emblem handling sit beside `adornment-body-codes.md` §7 but defer to it; I did not treat them as restatement.
- Canon and clinical scope: no in-world decision found. The clinical-adjacent statements are S122's subject (not used beyond the capitalisation point) and the B-coded critical-period row (M9). No clinical, education-policy or legal ruling found; the rights statement at `:156` is M8.

## 6. Unrun checks

- `python3 -B reports/round-51/boundary-count.py` (claim D): not run; not my item.
- `tools/source-audit-inventory.py` and the gate battery: not run; not in claim C's declared commands.
- Sibling-lane gates: not run; read-only topic and filename sweeps only (row 27).
- Lesson Gate quotes and the records' mistakes list: not checked (see §5).
- S072, S080, S094, S122: could not be opened (see §3).
- Lane writes: this file only. No lane git or jj state changed.
