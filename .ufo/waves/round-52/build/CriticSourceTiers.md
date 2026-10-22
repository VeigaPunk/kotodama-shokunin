# CriticSourceTiers — round 52, claim C sourcing pre-attack

Seat: KotodamaR52.CriticSourceTiers (critic, leaf). Assigned item: pre-attack the C entry's
(`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`) candidate sources and give a
tier plan the L1 can apply at integration. Author-lane advice, not admission. Access date for every
fetch below: 2026-10-22. All fetches were plain `curl` requests with curl's default user agent,
Wayback `id_` captures, Europe PMC REST, HAL, OhioLINK and OpenEdition. No headless browser, no
challenge solved, no login. Installs: none.

## 1. Result in one paragraph

Six of the eleven named sources can be opened by ordinary means for the scope C needs:
Stern 1957 (Wayback capture of Wiley's Free Access PDF), Seifart et al. 2018 (PMC, CC BY),
Poss 2012 (OhioLINK ETD PDF), Akinbo 2021 and its corrigendum (Frontiers full text), the UNESCO
records for Silbo Gomero and Turkish whistled language (clean Wayback captures only; the live pages
serve a CAPTCHA), plus Akinbo 2019 (OpenEdition). For Meyer, the 2008 JIPA paper is unopenable, but
two of his author copies on HAL are open: the 2021 Annual Review accepted manuscript and a 2007
preprint. Meyer 2015 and Busnel & Classe 1976 are publisher pages only, so tier B for claims about
the work. Güntürkün et al. 2015 is abstract only, so also tier B. Unopenable: Sebeok & Umiker-Sebeok
1976, Carrington 1949, Sicoli 2016, Meyer 2008, and the full texts of Meyer 2015 and Busnel & Classe
1976. Their claims must be relayed through an opened source and labelled as such, or marked
`(to-verify)`. Neither popular claim has an opened primary source: there is no "bush telegraph"
range or speed figure, and no stable worldwide count of whistled languages (Meyer's own figure moves
from 30 to more than 80 across his papers).

## 2. Tier plan (apply at integration)

Tier codes follow `corpus/SOURCES.md:14-19` and QUALITY criterion 6 (`corpus/QUALITY.md:29`).
"Relay" means the opened source reports another author's claim; tier B for that claim, and the
entry text names both authors ("Meyer 2021, citing Busnel & Classe 1976").

| candidate | opened? route | tier A scope (only this) | tier B scope | must be `(to-verify)` or cut |
|---|---|---|---|---|
| Stern 1957, *Am. Anthropologist* 59(3):487–506 | yes — Wayback `20210922200143` of `anthrosource.onlinelibrary.wiley.com/doi/pdf/10.1525/aa.1957.59.3.02a00070` (live URL: HTTP 403 Cloudflare "Just a moment..."; capture 20210929043039 of the abs page labels it "Free Access") | Stern's classification: encoding vs abridgment vs lexical ideograph; Morse code as encoding (the signal-code boundary); contraction and enphrasing; his Chin whistle and gong-xylophone observations | relay of Carrington 1949:33 n.1 on tone over stress (p. 499); other relayed ethnographies (Nekes, Witte, Schneider) | — |
| Sebeok & Umiker-Sebeok 1976, *Speech Surrogates* (Mouton, 2 vols) | no — archive.org `speechsurrogates0000unse_pt.1/pt.2` are print-disabled lending only (login); degruyterbrill.com search returned HTTP 202 with an empty body (bot wall); reviews exist (doi 10.2307/413047, 10.1017/s0047404500006370, 10.1525/aa.1978.80.3.02a00600) but were not opened | — | the bibliographic fact that it is a 1976 two-part compendium can be relayed via Meyer 2021 p. 5 | any content claim |
| Meyer 2008, *JIPA* 38(1):69–94 | no — cambridge.org HTTP 429 "Too many automated requests"; no Wayback capture of the article page | — | — | every "Meyer 2008" claim. Do NOT relabel HAL `halshs-00133192` (2007 preprint, different title) as Meyer 2008 |
| Meyer 2007 preprint, HAL `halshs-00133192` | yes — https://shs.hal.science/halshs-00133192/file/MeyerWhistledSpeech.pdf | Meyer's 2007 position only (dated); preprint, not peer-reviewed version | — | — |
| Meyer 2021, *Annu. Rev. Linguist.* 7:493–510 | yes — author accepted manuscript, HAL `hal-03058925` https://hal.science/hal-03058925/file/MainTextAnnualReviewMeyer2020.pdf (version of record not opened) | Meyer's typology (pitch-based vs formant-based strategies; tonal vs non-tonal), his 2021 counts (reported vs attested), forest range 10–500 m as his statement | relays: Busnel & Classe range 8 km; "ten times" shouted-speech range; Busnel's Turkish recognition rates; Sicoli 2016 repair finding | page numbers: cite manuscript page plus section heading, never journal pages |
| Meyer 2015, *Whistled Languages* (Springer) | publisher page only — https://link.springer.com/book/10.1007/978-3-662-45837-2 (not open access; chapters paywalled) | — | claims about the book: scope, chapter list | any content claim. The archive.org "community" uploads of this book are almost certainly unauthorised; do not use them as a "public copy" |
| Busnel & Classe 1976, *Whistled Languages* (Springer) | publisher page only — https://link.springer.com/book/10.1007/978-3-642-46335-8 | — | claims about the book: whistled systems "function in exactly the same way as speech" (the authors' stated thesis); chapter "Physics of the Signal; Range" pp. 32–43 exists | range numbers except through the Meyer 2021 relay. Same unauthorised-upload warning as Meyer 2015 |
| Seifart, Meyer, Grawunder & Dentel 2018, *R. Soc. Open Sci.* 5:170354 | yes — Europe PMC `PMC5936885` full text XML (CC BY); royalsocietypublishing.org itself returns HTTP 403 Cloudflare | Bora manguaré corpus results: four rhythmic units, V-to-V intervals, two tones carry few lexical contrasts; drum construction; message types | its uncited background sentences: "up to 20 km away" (§1.4), every adult Bora man can drum (§1.4), drummed speech attested on four continents (§1.1) | — |
| Güntürkün, Güntürkün & Hahn 2015, *Curr. Biol.* 25(16):R706–R708 | abstract only — Europe PMC REST (DOI 10.1016/j.cub.2015.06.067; not open access); cell.com HTTP 403 Cloudflare; no Wayback capture | — | claims about the study as the abstract states them (symmetric hemispheric contributions in whistled Turkish) | methods, sample size, effect sizes |
| UNESCO ICH 00172, Silbo Gomero (RL, 2009) | yes, via Wayback only — capture `20260830052642` is clean; capture `20260822120925` is itself the CAPTCHA page; the live page is a CAPTCHA | UNESCO's own inscription record: list, year, nomination description, schooling since 1999 | — | the phonology sentence ("two distinct whistles replace the five Spanish vowels...") conflicts with Meyer 2021 p. 22; never use it for phonology |
| UNESCO ICH 00658, Whistled language, Turkey (USL, 2017) | yes, via Wayback only — capture `20260312095851` is clean; capture `20260922232938` is the CAPTCHA page | UNESCO's own record: Urgent Safeguarding listing, stated threats (mobile phones), transmission statement | — | — |
| Carrington 1949, *The Talking Drums of Africa* | no — archive.org `talkingdrumsofaf00carr` (1969 reprint) is lending only (login); the 1971 *Scientific American* article (doi 10.1038/scientificamerican1271-90) and the reprint as chapter 30 of Sebeok & Umiker-Sebeok (doi 10.1515/9783110804423-001) were not opened | — | one relay via Stern 1957 p. 499 (tone is "the real basis of the drum language broadcast", Lokele) | every other Carrington claim, including range, relay speed and publisher |
| Sicoli 2016, *Language* 92(2):411–432 | no — muse.jhu.edu redirects to "Verification required"; doi resolves to cambridge.org, HTTP 429; OpenAlex `oa_status: closed`, no repository copy; no Wayback capture | — | relay via Meyer 2021 p. 14: repair in whistled speech shares the same sequence organization as repair in spoken speech | repair-format details beyond the relay |
| Akinbo 2021, *Front. Commun.* 6:650382, "The Language of Gángan, A Yorùbá Talking Drum" + corrigendum 6:773156 | yes — frontiersin.org full text (HTTP 200, article body present) | Yorùbá gángan/dùndún: tension-cord pitch, H/M/L drum tones, grammatical tones, one strike per CV syllable | its relay of Stern, which misquotes Stern's term (see §4.3) | — ; cite the corrected abstract (corrigendum) |
| Akinbo 2019, *Linguistique et langues africaines* 5:11–23, doi 10.4000/lla.347 | yes — https://journals.openedition.org/lla/347 | gángan tone representation from five drummers in Nigeria | — | — ; NOTE the brief calls this "Akinbo 2021"; the 2021 work is the Frontiers paper |
| Poss 2012, PhD dissertation, Ohio State | yes — OhioLINK ETD `osu1332472729` PDF https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1332472729&disposition=inline | Hmong raj listener experiments; his descriptions of qeej, raj, ncas (jaw harp), nplooj (leaf) and their uses | relay of Agnew 1939 on leaf-blown courtship and clan summons (p. 27) | — |
| Meyer, World Map of Attested Whistled Languages, HAL `hal-04912578v4` (2026 PDF) | yes — https://hal.science/hal-04912578/file/WorldMapOfAttestedWhistledLanguages-2026.pdf | which languages Meyer's map labels (figure only) | — | never derive a count by counting map labels; labels include drum-system groups (e.g. Lokele), so a label count is not a whistled-language count |

UNESCO element coverage. I ran a Wayback CDX prefix search over `ich.unesco.org/en/` for URLs
containing whistl, drum, surrogat or talking (status 200, collapsed by urlkey). It finds exactly two
speech-surrogate elements, 00172 (RL, Silbo Gomero) and 00658 (USL, Turkey). The drum hits are dance
and ritual drumming elements (00161, 00352, 00843, 00989, 01011, 01196, 01208, 01696) and the
Candombe "drum calls" assistance (00555); none describes drum speech. Do not cite them as surrogate
evidence. Limit: the index only covers captured URLs, so a recent inscription with no capture would
not show up. Any third "UNESCO-listed whistled language" stays `(to-verify)` unless a source seat
opens it.

## 3. Draft registry rows (11 columns; ids for the L1 to renumber S134+)

Quotes are verbatim, at most 25 words, located as stated. Status `queued` until C's used-by is set.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-CriticSourceTiers-1 | Stern 1957, Drum and Whistle "Languages": An Analysis of Speech Surrogates, American Anthropologist 59(3):487–506 — https://anthrosource.onlinelibrary.wiley.com/doi/pdf/10.1525/aa.1957.59.3.02a00070 (live URL served a Cloudflare JS challenge; read via Wayback capture 20210922200143 of the Free Access PDF) | paper | A | Stern's classification of speech surrogates (encoding, abridgment, lexical ideograph) and his Chin observations; relays of older ethnographies are B | Section I, p. 487 (a. Encoding; b. Abridgment); p. 489 (2. Lexical ideograph) | "Thus in Morse code, sequences of dot and dash are conventionally assigned to the letters of the alphabet." (p. 487); "Abridgment: Each transmitted sign exhibits significant resemblance to a corresponding sound of the base message." (p. 487) | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-2 | Meyer 2021, Environmental and Linguistic Typology of Whistled Languages, Annual Review of Linguistics 7:493–510 — author accepted manuscript, HAL hal-03058925, https://hal.science/hal-03058925/file/MainTextAnnualReviewMeyer2020.pdf | paper | A | Meyer's own typology and 2021 counts (reported vs attested); his relays of Busnel & Classe and Sicoli are B | manuscript p. 4, section "Geographic Locations and Language Families", para. 1; p. 5 para. 1; p. 10; p. 13; p. 14; p. 22 (Vowels) | "More than eighty languages with whistled speech have been reported … around forty of them have been attested by studies or published recordings." (p. 4) | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-3 | Meyer 2007, Acoustic strategy, phonetic comparison and perceptive cues of whistled languages, preprint, HAL halshs-00133192 — https://shs.hal.science/halshs-00133192/file/MeyerWhistledSpeech.pdf | paper | A | Meyer's 2007 count only, as a dated datum for the count-drift row; not the 2008 JIPA paper | Abstract, sentence 1 (preprint p. 1) | "Whistled speech is a complementary natural style of speech to be found in more than 30 languages of the world." | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-4 | Seifart, Meyer, Grawunder & Dentel 2018, Reducing language to rhythm: Amazonian Bora drummed language exploits speech rhythm for long-distance communication, R. Soc. Open Sci. 5:170354 — https://europepmc.org/article/PMC/PMC5936885 (publisher page served a Cloudflare JS challenge; read via Europe PMC full text, CC BY) | paper | A | Bora manguaré corpus results; background statements (range, who drums) are B | Abstract; §1.1 "Emulated speech systems and drummed speech"; §1.4 "Bora manguaré drumming" | "Rhythm thus appears to crucially contribute to the intelligibility of drummed Bora." (Abstract); "They are used for communication within and across communities, up to 20 km away." (§1.4) | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-5 | Güntürkün, Güntürkün & Hahn 2015, Whistled Turkish alters language asymmetries, Current Biology 25(16):R706–R708 — abstract via Europe PMC REST, DOI 10.1016/j.cub.2015.06.067 (publisher page served a Cloudflare JS challenge; full text not opened) | paper | B | claims about the study as stated in its abstract | Abstract, sentence 7 | "We discovered that whistled language comprehension relies on symmetric hemispheric contributions" | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-6 | UNESCO ICH, Whistled language of the island of La Gomera (Canary Islands), the Silbo Gomero (element 00172) — https://ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 (live page CAPTCHA; read via Wayback capture 20260830052642) | docs | A | UNESCO's own 2009 inscription record and nomination description; not phonology | Description, sentence 2; sentence 6 | "it is the only whistled language in the world that is fully developed and practised by a large community (more than 22,000 inhabitants)" | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-7 | UNESCO ICH, Whistled language (Turkey, element 00658) — https://ich.unesco.org/en/USL/whistled-language-00658 (live page CAPTCHA; read via Wayback capture 20260312095851) | docs | A | UNESCO's own 2017 Urgent Safeguarding record and description | inscription line; Description, sentence 6 | "One of the key threats to the practice is the use of mobile phones." | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-8 | Akinbo 2021, The Language of Gángan, A Yorùbá Talking Drum, Frontiers in Communication 6:650382 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.650382/full; corrigendum 6:773156 | paper | A | Yorùbá gángan drum speech (lexical and grammatical tones); its Stern relay is not used | §8 "Summary, Discussion and Conclusion", para. 1 | "By varying the compression of the tension cords, the drummers represented the tones of the words." | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-9 | Akinbo 2019, Representation of Yorùbá Tones by a Talking Drum. An Acoustic Analysis, Linguistique et langues africaines 5:11–23 — https://journals.openedition.org/lla/347 | paper | A | gángan tone and syllable representation | English abstract, sentence 2 | "the number of syllables in a word directly corresponds to the number of strikes on the drum membrane" | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-10 | Poss 2012, Hmong Music and Language Cognition: An Interdisciplinary Investigation, PhD dissertation, Ohio State University — https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1332472729&disposition=inline | thesis | A | Hmong raj listener cognition and Poss's own descriptions of Hmong instruments; Agnew 1939 relay is B | Abstract p. ii; §2.4 "Hmong musical instruments" p. 28; p. 30; p. 31 | "The common traditional Hmong instruments include qeej (a free-reed mouth organ), raj (a family of flutes and free-reed pipes), ncas (guimbardes), nplooj (leaves)" (p. 28) | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-11 | Meyer 2015, Whistled Languages: A Worldwide Inquiry on Human Whistled Speech, Springer — https://link.springer.com/book/10.1007/978-3-662-45837-2 | book | B | claims about the book (scope, chapters) from the publisher page | "About this book", sentence 1 | "The main focus of this monograph on whistled speech is the result of a worldwide inquiry primarily based on the author's unprecedented fieldwork" | queued | 2026-10-22 | 365d | — |
| NEW-CriticSourceTiers-12 | Busnel & Classe 1976, Whistled Languages (Communication and Cybernetics 13), Springer — https://link.springer.com/book/10.1007/978-3-642-46335-8 | book | B | claims about the book (the authors' thesis, chapter list) from the publisher page | "About this book", sentence 3 | "they are much more than mere codes or conventional systems of signals; they function in exactly the same way as speech" | queued | 2026-10-22 | 365d | — |

More quotes held for the entry's sections, all verbatim and at most 25 words:

- Stern 1957 p. 489: "the lexical ideograph has no reference to the phonemic structure of the base language but symbolizes directly the sememe (concept) it represents" (encoding and ambiguity section).
- Stern 1957 p. 488: "the situational context must resolve the ambiguity" (a Sizang whistled tone pattern shared by two messages).
- Stern 1957 p. 499, relaying Carrington 1949:33 n. 1: "But tone is more important than stress and is the real basis of the drum language broadcast." (B, relay).
- Meyer 2021 p. 5: "mentioning fewer than a dozen attested whistled languages (Busnel & Classe 1976; Sebeok & Umiker-Sebeok 1976)".
- Meyer 2021 p. 10: "Whistled communications are used from about 10 meters and up to about 500 meters, depending on the density of vegetation." (forest; A as Meyer's statement).
- Meyer 2021 p. 10, relay: "carry the signal up to, sometimes, about 8 kilometers (Busnel et Classe 1976)" (B).
- Meyer 2021 p. 13: tonal and non-tonal languages "follow either pitch-based or formant- based whistling strategies".
- Meyer 2021 p. 14, Sicoli relay: "repair in whistled speech shares the same universal sequence organization as repair in spoken speech" (B).
- Meyer 2021 p. 22: "/i/ has a high pitch, /e/ lower, /a/ even lower, and /o/ is among the lowest possible whistled frequencies".
- Seifart 2018 §1.4: "In principle, every adult Bora man can use the drums and every community member can understand manguaré messages" (who-may-speak section; B, background).
- Seifart 2018 §1.1: "Such systems have also been called 'speech surrogates' [4] or 'speech substitutes' [19] in the older literature."
- UNESCO 00172: "Taught in schools since 1999" (transmission section).
- UNESCO 00658: "whistled language is still transmitted from generation to generation in the context of parent-child relations through both formal and informal methods" (24 words).
- Poss 2012 p. 30: "Untrained listeners cannot understand the encoded words, which, in the case of funerals, are directed at the soul of the deceased person" (qeej; who-may-speak).
- Poss 2012 p. 31: "The ncas, a guimbarde that is most commonly associated with courtship, is performed using the mouth as a resonator." (jaw harp).
- Poss 2012 p. 27, Agnew 1939 relay: "The leaf is predominantly used in love-making." (B).
- Poss 2012 p. ii: "investigates speech surrogate cognition from the perspective of Hmong culture to find out how listeners understand verbal messages encoded in performances on aerophones called raj".

Channel coverage check against the planned section 3 typology: whistles (Meyer, UNESCO, Stern), drums
(Seifart, Akinbo, Stern), reed pipes and mouth organ (Poss: raj, qeej), jaw harp (Poss: ncas),
leaves (Poss, relaying Agnew), slit-gong xylophone and gongs (Stern pp. 487, 501; this covers Chin and
relays Carrington 1953 on Congo gongs), signal codes (Stern p. 487, Morse as encoding). **Horns have
no opened source.** Akinbo 2021 §1 names "Kaminski, 2008 on Asante ivory trumpet", which is only a
lead. Horns therefore stay `(to-verify)` or are named without a factual claim.

## 4. Counterexamples and traps (with evidence)

1. **A Wayback "200" can be the CAPTCHA page.** The CDX lists both UNESCO pages with status 200, but
   `20260822120925` (Silbo) and `20260922232938` (Turkey) contain "What code is in the image?"; only
   `20260830052642` and `20260312095851` carry the description. Correction: the anchor cell names the
   exact capture id that was read, and the integrator re-fetches that id before admitting the row.
   `tools/check-source-access.py` cannot detect this (its `BYPASS` regex at
   `tools/check-source-access.py:32-33` only scans row text).
2. **The checker's honest-note false positive.** `BYPASS` matches the bare words `headless` and
   `bypass(ed|ing)` anywhere in the source, anchor or teaches cells
   (`tools/check-source-access.py:32-33,53`). An honest note such as "not bypassed" or "no headless
   browser used" fails criterion 10's check (exit 1). Correction: write access notes as "(live page
   served a Cloudflare JS challenge; read via Wayback capture <id>)" or "(live page CAPTCHA; read via
   Wayback capture <id>)". These match the selftest controls at `tools/check-source-access.py:111-112`.
3. **Relay misquote.** Akinbo 2021 §1 says Stern called the second class "lexical ideogram"; Stern
   1957 p. 489 says "Lexical ideograph". Correction: cite Stern directly (row 1), never through
   Akinbo.
4. **Year mislabel in the brief.** "Akinbo 2021" in the assignment matches two works: the Frontiers
   *Gángan* paper (2021, with a corrigendum to its abstract) and the LLA acoustic paper (2019, doi
   10.4000/lla.347). Correction: cite the year of the paper actually opened, and quote the corrected
   abstract wording for the Frontiers paper.
5. **Count drift (popular "N whistled languages" claim).** Meyer's own figures: "more than 30" (2007
   preprint, abstract), "more than eighty … reported … around forty … attested" (2021 manuscript
   p. 4), and "fewer than a dozen attested" in the 1976 surveys (2021 p. 5). No opened source gives
   any rounder figure (for example "about 70"). Correction: C states the number as dated and split
   into reported and attested ("Meyer 2021 reports more than 80 reported, about 40 attested"). It
   never gives a bare count, and never counts the HAL map's labels.
6. **Bush telegraph range and speed (popular claim).** No opened source gives a relay speed or a
   multi-village range for African drum networks. The only drum range opened is Seifart 2018 §1.4,
   "up to 20 km away", an uncited background sentence about Bora. Carrington, the usual source, is
   unopenable. Correction: put the claim in the calibration bank with status T (unresolved
   provenance; `(to-verify)`, never load-bearing; `corpus/knowledge/verification/calibration-registry.md:39`).
   The only number C may carry is Bora's "reported range up to 20 km (Seifart et al. 2018,
   background)" (B).
7. **Whistled range figures are relays.** "About 8 km" (Canaries) and "ten times greater than shouted
   speech" reach C only through Meyer 2021 citing Busnel & Classe 1976 and Meyer 2008. Both are B
   relays; Meyer's own forest figure (10–500 m) is A.
8. **UNESCO used beyond its scope.** The Silbo record's phonology ("two distinct whistles replace the
   five Spanish vowels, and there are four whistles for consonants") conflicts with Meyer 2021 p. 22,
   where Spanish whistled vowels sit at graded pitch levels for /i/, /e/, /a/ and /o/. Its "only
   whistled language … fully developed … large community" claim is a 2009 nomination statement.
   Correction: the UNESCO rows' scope is the inscription record only (as the base already does for
   S062 at `corpus/SOURCES.md:91`). Phonology and uniqueness are attributed to UNESCO as claims, or
   go in the calibration bank.
9. **"Whistled language is processed by the right hemisphere" (popular claim).** The opened abstract
   says "symmetric hemispheric contributions", meaning a relative shift, not a right-hemisphere
   takeover. Correction: quote the abstract (B) and put the stronger version in the calibration bank.
10. **Unauthorised public copies.** archive.org items
    `whistled-languages-a-worldwide-inquiry-on-human-whistled-speech-2015`,
    `julienmeyerauth.whistledlanguages…springerv` and
    `communicationandcybernetics13professorreneguybusneldr.andreclasseauth.whistledla` are
    "community" uploads of in-copyright Springer books. They pass criterion 10's letter but are false
    provenance and liable to takedown, so a fresh session cannot rely on them. Correction: treat Meyer
    2015 and Busnel & Classe 1976 full texts as unopened.
11. **Base defect C must not inherit (route; outside D and C lands).**
    `corpus/knowledge/culture-material/music-instrument-lexicon.md:98` and
    `corpus/knowledge/linguistics/orality-formulaic-language.md:124` attach "Yoruba dùndún" to
    Carrington 1949. Carrington's documented work is Lokele, Congo (Stern 1957 p. 499; the same row
    names "Lokele drum-speech"). The publisher also conflicts at base: International African
    Institute (`music-instrument-lexicon.md:4`) vs Carey Kingsgate (`orality-formulaic-language.md:24`).
    C cites these owners one way only and must not repeat "Yoruba dùndún (Carrington 1949)". The
    Yorùbá claim belongs to Akinbo (rows 8–9). Route the base fix to a later round's repair list.
12. **"Meyer 2008" at base.** `corpus/knowledge/linguistics/phonetics-phonology.md:198` rests Silbo,
    Kuşköy and Chinantec on Meyer 2008, which cannot be opened by ordinary means this round. C must not
    cite Meyer 2008 by year. Use Meyer 2021 (row 2) or mark `(to-verify)`.

## 5. Smallest safe corrections for the L1

- Admit only rows 1–12 above, or equivalents a source seat opened, at the tiers shown. Every
  Sebeok & Umiker-Sebeok, Carrington, Sicoli and Meyer 2008 claim is a named relay (B) through
  rows 1 or 2, or carries `(to-verify)`.
- Calibration bank candidates (C's §12; codes from `calibration-registry.md:35-39`): bush telegraph
  speed and range, T; "N whistled languages worldwide" without a date and the attested/reported
  split, B (bounded: Meyer 2021, dated, split); "Silbo is the only fully developed whistled
  language", C (UNESCO nomination claim vs Meyer's Turkish, Greek and other whistled forms); "the
  right hemisphere processes whistling", R as stated, with the abstract's symmetric-contribution
  finding as the bounded B reading; "talking drums need a tone language", C (Stern p. 501 relays
  Schneider on Sangvi drumming of a non-tonal language; a B relay, so contested, not refuted).
- Access-note wording per §4.2; anchor cells carry the exact Wayback capture id per §4.1.
- Horns: no opened source; `(to-verify)` with Kaminski 2008 as a lead only.

## 6. Unrun checks (main agent should run)

- `python3 -B tools/check-source-access.py` after the C rows land (status leg and cited leg).
- Re-fetch the two clean UNESCO captures (`20260830052642`, `20260312095851`) at integration to
  confirm each is not a CAPTCHA page.
- C's acceptance, separability and dry-run commands from `reports/round-52/claims.json`.
- Not attempted: De Gruyter chapter pages for Sebeok & Umiker-Sebeok and Carrington, beyond the
  202 bot wall; the *Scientific American* 1971 Carrington article; the version of record of Meyer
  2021; the Meyer 2015 and Busnel & Classe front-matter preview PDFs.
