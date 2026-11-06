# ScoutSources97 — candidates for the verbal-duelling entry (round 97, wave 1)

Access date for every candidate: 2026-11-05. All fetches: plain `curl -L -sS --max-time 30`, default user agent, no login, no CAPTCHA passing, no `-k`. Registry dedup before every open: `grep -c -F` on the full URL and on host+path against `corpus/SOURCES.md` — all 16 URLs checked returned `full=0 hostpath=0` (16 new sources; `gutenberg.org` host appears 18× in the registry, this path is new; `archive.org` host appears 278×, both item paths are new). Registry rows at check: `grep -c -E '^\| S[0-9]+' corpus/SOURCES.md` → 908, rc 0.

## Admitted candidates (8: 7 tier A, 1 tier B)

| key | url | tier | bytes | sha256 (capture) | quote (located, count == 1) | supports |
|---|---|---|---|---|---|---|
| pagliai_2009 | https://journal.oraltradition.org/wp-content/uploads/files/articles/24i/04_24.1.pdf | A | 269331 | 5799114d2e3fac10d9372a78637ef47605ac429b1fcde5a2b11855cfa119fd63 | "A common view of verbal duels posits that they are a cathartic expression of aggression" (C1_pagliai.txt, count 1, 15 w) | worldwide survey; rejects the catharsis view; contests negotiate social order before audiences |
| hoebel_1954 | https://archive.org/details/in.gov.ignca.2688 (capture from https://archive.org/download/in.gov.ignca.2688/2688_djvu.txt) | A | 844105 | d786726a8213030a822f916747e357f25dc52fef23909c9cb429c771469eb16d | "Among the East Greenlanders song duels may be carried on for" (count 1, 11 w) | Inuit nith-song duels as juridical dispute settlement; prestige the sole stake |
| lokasenna_bellows | https://en.wikisource.org/wiki/The_Poetic_Edda_(tr._Bellows)/Lokasenna | A | 307750 | 5f3353dce7d2583786f287495adacfac428bb98fc79e5656345ff3e5ee4f2f2b | "Then Loki went into the hall, but when they who were there saw who had entered, they were all silent." (raw HTML bytes, count 1, 20 w) | primary text of the senna: Loki demands a seat at Aegir's feast; the insult contest frame |
| dunbar_kennedie_murphy | http://www.clanstrachan.org/history/Flyting_of_Dunbar_and_Kennedy.pdf | B | 390354 | d12852cea4cac0eab4a3c99396cd0800828359a1ce86cc9f73f98c5cd4142737 | "The flyting was a verbal competition in which the participants vied in heaping abuse of⏎all sorts on each other, some of it quite gross." (C4_flyting_murphy.txt, count 1, 25 w) | flyting defined: verbal competition, heaped abuse, at least in part a literary game; the Scots flyting text |
| ruszkiewicz_2020 | https://repo.ignatianum.edu.pl/pl/file_records/866/download | A | 130290 | 8a59f531d9e6eace014db8f512ffe043148c5153c4c5401c5b182fe56eda4292 | "the Scottish genre of flyting, whose main⏎purpose was to humiliate the opponent" (C5_flyting_ignatianum.txt, count 1, 13 w) | peer-reviewed flyting definition; Anglo-Saxon context; poetic agon (Prace Filologiczne 10(13) 2020, DOI 10.32798/pflit.575, CC BY) |
| garzia_2007 | https://journal.oraltradition.org/wp-content/uploads/files/articles/22ii/8_garzia3.pdf | A | 370994 | b7f8247b890ec1ef9fb444209fa7903ccd81d3b28dac52037a6e5c0d66aa3052 | "the references to the verbal combats between bertsolaris and the social importance that such⏎ad hoc compositions appeared to have had at the time." (C9_garzia_bertso.txt, count 1, 24 w) | Basque bertsolaritza: verbal combats, ad hoc verse, championships with judges' panels |
| nadera_2019 | https://ojie.um.edu.my/index.php/SARE/article/download/19055/10299 | A | 229711 | 6e5ab013b2436459789bacb21af3193b2ab578bd5c49954c3205096589ce02bd | "Balagtasan is an indigenous form of competitive Filipino debate poetry in the Tagalog language" (C8_balagtasan_sare.txt, count 1, 14 w) | balagtasan: moderator (lakandiwa), adjudication, duplo ancestry, fliptop descendant (SARE 56(1) 2019) |
| nicholson_1907 | https://www.gutenberg.org/files/37985/37985-0.txt | A | 1203657 | (see candidates.json) | "Soon these 'Flytings' (_Naqá’iḍ_) were recited⏎everywhere, and each poet had thousands of enthusiastic partisans who⏎maintained that he was superior to his rival." (count 1, 24 w) | the Naqaid of Jarir and Farazdaq: public scolding-match (muhajat), recited before thousands of partisan judges |

Every admitted quote satisfies: exact substring of the capture text (for PDFs, of the `pdftotext -layout` extraction stored alongside the capture; `⏎` marks the real newline inside the byte-exact substring), ≤ 25 words, byte count == 1 (verified in `python3`: `capture.read_bytes().count(quote.encode()) == 1`, asserted for all 8).

PDF text extractions (sha256): C1_pagliai.txt 967e3cd4a33b2cc4e77bff6927b308bd417ce143a1188112c19f468960b9578b; C4_flyting_murphy.txt aa06f258d8cac7be3bac9534e8f175cac0315fb211e70dbe3dd7b360f1264efd; C5_flyting_ignatianum.txt 3cae64e59e7938ecfb8067b3f24fe3063eb3f5413a79c17bae8e5b966a5f0472; C8_balagtasan_sare.txt fab38ff4b650c10bc77dc66527393a2d9f40838e5a284ae63c5d0114375edc50; C9_garzia_bertso.txt 01f7f2180616ababbace1a49c0026bb1c9d08e9b66ddbc593d5e99c8d88b9ba9.

## Opened but not admitted (quote uniqueness unattainable)

| key | url | what happened |
|---|---|---|
| bevan_nakaid_edition | https://archive.org/details/pt1nakaidofjarir01jarr | HTTP 200. Three captures: details page 277031 B (bf0d0a0aa7df5bd82a42de6043c359db45a680a149fc43bb9e87463b4565fa4d); vol. 1 pt. 1 djvu OCR 1237048 B (80283e64fb190b6d72fccec9eb69da96fb0bef5d4fb7ccdad41490fb11d5da89; attempt 1 rc=28 timeout, attempt 2 200); vol. 3 djvu OCR 767675 B (item nakaid-jarir-farazdak-G). Arabic OCR carries no clean English ("the " count 0; vol. III preface garbled); details page repeats its title string 6× and none of 6 probed spans is unique. Flip: a scan whose OCR carries clean English front matter, or a scholarly translation of the Naqaid. |
| labov_chapter | https://link.springer.com/chapter/10.1007/978-1-349-25582-5_37 | HTTP 200, 228734 B (c9b3e41e2793a265cd110fa8b1055cfd19af7c89fb85d18f00704440b65ff6e1). Publisher page (no login) mirrors the preview in metadata: "A great variety of terms describe this activity" count 6; "the dozens, sounding and signifying are three of the most common" count 5; 11 spans probed, none unique. Labov self-bibliography https://www.ling.upenn.edu/~wlabov/WL.BIB.pdf → 403 (118 B), attempt 1. Flip: authorized open copy of the chapter, or a page rendering the preview exactly once. Interim for the entry: Pagliai 2009 covers the same ground openly. |

## Rejects — walls (UNREACHABLE), recorded with every attempt

| key | url | attempts | verdict | flip |
|---|---|---|---|---|
| hoebel1941_northwestern | https://scholarlycommons.law.northwestern.edu/cgi/viewcontent.cgi?article=3012&context=jclc | 4 (all 403) | UNREACHABLE wall (bpress blocks default-UA curl) | Hoebel 1954 open scan (admitted) |
| lokasenna_sacredtexts | https://sacred-texts.com/neu/poe/poe10.htm | 4 (all 403) | UNREACHABLE wall | Wikisource copy (admitted) |
| naqaid_utexas_chapter | https://repositories.lib.utexas.edu/server/api/core/bitstreams/73c4a4e2-73b2-44ba-85ba-fdfecdb11245/content | 1 (403) | UNREACHABLE wall (dSpace blocks default-UA curl) | Bevan scans + Nicholson (recorded/admitted) |
| zulu_gunner_soas | https://soas-repository.worktribe.com/output/415526/ukubonga-nezibongo-zulu-praising-and-praises | 1 (403) | UNREACHABLE wall (worktribe blocks default-UA curl) | another open Zulu praise primary (unresolved gap this round) |
| norse_lsu_thesis | https://repository.lsu.edu/cgi/viewcontent.cgi?article=4141&context=gradschool_theses | 1 (403) | UNREACHABLE wall | peer-reviewed flyting scholarship (ruszkiewicz_2020 admitted) |
| dundes_jstor | https://www.jstor.org/stable/pdf/538809.pdf | 1 | WALL: HTTP 200 but 3038-byte HTML access interstitial, not article bytes (login/JS shell); body kept in scratch only, never citable | authorized open copy; interim: pagliai_2009 capture |
| sonhuasteca_pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC8201493/pdf/fpsyg-12-648010.pdf | 1 | WALL: HTTP 200 but 1816-byte HTML block page, not the PDF | publisher version at frontiersin.org or Europe PMC |

## Search log (web_search; each query returned 8 results)

| # | query | results | kept |
|---|---|---|---|
| 1 | Dundes Leach Ozkok "verbal dueling" Turkish boys rhymes JAF pdf | 8 | pagliai_2009 discovered (journal.oraltradition.org 24i survey) |
| 2 | Labov "Rules for Ritual Insults" sounding pdf open access | 8 | labov_chapter probe (unadmitted) |
| 3 | "The Flyting of Dunbar and Kennedie" full text wikisource OR gutenberg OR archive.org | 8 | dunbar_kennedie_murphy, ruszkiewicz_2020 |
| 4 | Lokasenna Bellows translation online sacred-texts OR gutenberg Poetic Edda senna | 8 | lokasenna_bellows |
| 5 | Inuit Eskimo song duel nith songs juridical Hoebel "law of primitive man" pdf | 8 | hoebel_1954, hoebel1941_northwestern probe |
| 6 | Naqa'id Jarir Farazdaq Arabic invective poetry open access archive.org Wormhoudt | 8 | bevan_nakaid_edition, naqaid_utexas_chapter probe |
| 7 | Pagliai "verbal art" contest performative creation of social order verbal duel pdf | 8 | pagliai_2009 (confirmed identity + mospace mirror) |
| 8 | Unferth flyting Beowulf "verbal duel" scholarship open access pdf | 8 | norse_lsu_thesis probe; ruszkiewicz context |
| 9 | bertsolaritza improvised poetry contest Oral Tradition journal Garzia pdf | 8 | garzia_2007 |
| 10 | balagtasan Filipino poetic debate verbal duel scholarly article open access | 8 | nadera_2019 |
| 11 | contrapunteo copla Mexican verbal duel son huasteco scholarly pdf | 8 | sonhuasteca_pmc probe (wall) |
| 12 | Zulu izibongo praise poetry boasting insult open access pdf archive.org | 8 | zulu_gunner_soas probe (wall) |
| 13 | Nicholson "A Literary History of the Arabs" Jarir Farazdaq naqaid gutenberg OR archive.org | 8 | nicholson_1907 |

## Commands (rc noted)

- Dedup: `grep -c -F -- "<url>" corpus/SOURCES.md` and host+path form → 0 for all 16 URLs, rc 0 (each).
- Row count: `grep -c -E '^\| S[0-9]+' corpus/SOURCES.md` → 908, rc 0.
- PDF→text: `pdftotext -layout <cap>.pdf <cap>.txt` rc 0 for C1, C4, C5, C8, C9 (C12 failed: block page).
- Quote counts: `python3` `read_bytes().count(quote.encode())` → 1 for all 8 admitted quotes (asserted in the writer; run 2026-11-05).
- Hashes: `sha256sum` over captures/ (list also kept in scratch during work).

## Tools installed

None. `pdftotext` (poppler 26.10.0) was already present at /usr/bin/pdftotext.
