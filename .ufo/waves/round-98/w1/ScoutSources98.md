# ScoutSources98 — toast and drinking-speech sources (round 98, attempt 1)

Access date for every row: 2026-11-05. Fetch: plain `curl -sS -L --max-time 30` with the default user agent; transient failures (rc 28 timeout, 429, 5xx) retried 3 times with 20 s backoff; every attempt is in `fetch-attempts.log` (copied into this stage). No S-ids assigned. No login, bot-challenge or TLS bypass. Captures under `captures/`; sha256 of each file is in `candidates.json`.

Counts: 26 candidates opened or navigated; admitted 11 (tier A or B: 11); rejected 15 (duplicate-free: none of the admitted URLs appears in corpus/SOURCES.md; see the duplicate check below).

## Search log (web_search, limit 8 results each; hit counts are the returned result count)

| # | query | hits | kept |
|---|---|---|---|
| Q1 | Heimskringla Saga of Hakon the Good Odin's full Bragafull Laing Gutenberg | 8 | C1 (Gutenberg #598) |
| Q2 | Ynglinga saga bragafull oath Ingjald | 8 | C2 (ch. 41, wrong), C3 (ch. 36, found by navigation) |
| Q3 | Geoffrey of Monmouth Rowena wassail drinc hail Giles Gutenberg | 8 | C16 (melocki transcription of Giles 1842) |
| Q4 | Plato Symposium Jowett drinking Eryximachus Gutenberg | 8 | C9 (Gutenberg #1600) |
| Q5 | Xenophon Symposium Dakyns Gutenberg | 8 | C10 (Gutenberg #1181) |
| Q6 | Athenaeus Deipnosophists Yonge toast drinking healths | 8 | C11 (Gutenberg #66508, vol. 3) |
| Q7 | Tuite Georgian supra tamada autocrat of the banquet table pdf | 8 | C12 (umontreal PDF); DiVA copy of the same paper not separately opened |
| Q8 | Book of Rites district drinking ceremony Legge xiang yin jiu | 8 | C23 (sacred-texts, 403), C22 (ctext, challenge) |
| Q9 | Beowulf Wealhtheow cup Gummere Gutenberg | 8 | C13 (Gutenberg #981, pg981.txt); C14 (981-0.txt, 404) |
| Q10 | toast speech act anthropology drinking ethnography open access | 8 | C15 (Open Encyclopedia of Anthropology, Feasting) |
| Q11 | Legge Li Ki Hsiang Yin Kiu Yi sacred-texts Sacred Books of the East full text | 8 | C23/C24 (403); archive.org SBE 28 found |
| Q12 | Samuel Laing Heimskringla Ynglinga saga chapter bragarfull Gutenberg text vow Ingjald horn | 8 | none new; result claimed Gutenberg #598 holds Ynglinga — checked: it does not (C1 capture TOC) |
| Q13 | origin of the toastmaster office history toast order of toasts ritual drinking open access article | 8 | C19 (Leaves DOI, unreachable); Toastmasters.org, worldhistory.org, Merriam-Webster, FlatWorld, digitens (tier C, not opened) |
| Q14 | Critias Elegies Sparta drinking healths Athenaeus Gutenberg Yonge Book X | 8 | none new (Critias fragment is in C11 but about kottabos, not admitted) |
| Q15 | Geoffrey of Monmouth History of the Kings of Britain Giles translation full text archive.org | 8 | C16 (melocki); archive.org not opened (no hit with a text URL) |
| Q16 | Legge Li Ki Gutenberg ebook alternate host | 8 | C25 (archive.org djvu text) |
| Q17 | Toasting and Gender in Great Britain in the Eighteenth Century 250740 pdf Kyoto | 8 | C20, C21 (Kyoto landing/PDF returned HTML) |
| Q18 | Drinking and Toasting in Georgian Britain ... Leaves 2020 pdf | 8 | C26 (HAL deposit) |

## Candidate table

| key | url | http | tier | admitted | quote (count, quote_capture) | reason (short) |
|---|---|---|---|---|---|---|
| C1 | https://www.gutenberg.org/cache/epub/598/pg598.txt | 200 | A | yes | Then it was the custom of many to empty the brage-goblet (1, C1.txt) | Admitted: body text names the custom of emptying the brage-goblet after the sacrificial cups; endnote (1) 'The brage-goblet, over which vows were made.' is a se… |
| C2 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/41 | 200 | B | no | — | Rejected: chapter 41 ('Frá Ívari víðfaðma') contains no toast, oath or cup text (grep on capture); opened only to find the Ingjald vow; the chapter-41 url was r… |
| C3 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/36 | 200 | B | yes | strengdi hann þá heit að hann skyldi auka ríki sitt hálfu í hverja höfuðátt eða deyja ella (1, C3.txt) | Admitted at tier B: primary Old Norse wording, but the transcription names no critical edition in the capture, so it is not tier A. Located quote count 1 (17 wo… |
| C4 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/35 | 200 | B | no | — | Rejected: adjacent chapter used to locate ch. 36; no 'bragaf' or oath text (grep count 0 on capture).… |
| C5 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/37 | 200 | B | no | — | Rejected: adjacent chapter; no 'bragaf' or oath text (grep count 0).… |
| C6 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/38 | 200 | B | no | — | Rejected: battle chapter; no toast, cup or oath text (grep count 0 for 'bragaf').… |
| C7 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/39 | 200 | B | no | — | Rejected: no toast, cup or oath text (grep count 0 for 'bragaf').… |
| C8 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/40 | 200 | B | no | — | Rejected: the chapter narrates the burning of Ingjald's hall; no toast, cup or oath text.… |
| C9 | https://www.gutenberg.org/files/1600/1600.txt | 200 | A | yes | libations were offered, and after a hymn had been sung to the god, (1, C9.txt) | Admitted: located quote on libations at the opening of the drinking-party, count 1 (13 words). Second line 'they were all to drink only so much as they pleased.… |
| C10 | https://www.gutenberg.org/files/1181/1181-0.txt | 200 | A | yes | Quite right (said Callias), and we will pledge you. (1, C10.txt) | Admitted: located quote 'Quite right (said Callias), and we will pledge you.' count 1 (9 words) — a pledge exchange at the symposium. The cup-bearers' circuit l… |
| C11 | https://www.gutenberg.org/cache/epub/66508/pg66508-images.html | 200 | A | yes | the pledge-cup to the Good Deity (1, C11.txt) | Admitted: located quote 'the pledge-cup to the Good Deity' count 1 in the tag-stripped text (6 words). Context: the cup is handed round after the solid food and… |
| C12 | https://www.mapageweb.umontreal.ca/tuitekj/publications/Tuite-supra.pdf | 200 | B | yes | The order of toasts, especially in the opening phase of (1, C12.txt) | Admitted at tier B: a scholarly chapter in a conference volume, not tier A; located quote 'The order of toasts, especially in the opening phase of' count 1 (10 … |
| C13 | https://www.gutenberg.org/cache/epub/981/pg981.txt | 200 | A | yes | and the high-born lady handed the cup first to the East-Danes' heir and warden, (1, C13.txt) | Admitted at tier A: a primary translation of the Old English poem. The located quote (14 words, count 1) supports the order of a cup-round, not a named toast fo… |
| C14 | https://www.gutenberg.org/files/981/981-0.txt | 404 | A | no | — | Rejected: 404 at this path; the working Gutenberg URLs for the same translation are cache/epub/981/pg981.txt (C13, HTTP 200) and files/981/981-h/981-h.htm (HTTP… |
| C15 | https://www.anthroencyclopedia.com/entry/feasting | 200 | B | yes | Toasting, which links two uses of the mouth (communication and consumption) is a concrete expression of accord in mind and communion in body. (1, C15.txt) | Admitted at tier B: open-access reference entry (not a primary text). Located quote count 1 (23 words). The same capture also reads 'There could be twenty or mo… |
| C16 | https://www.melocki.org.uk/monmouth/History.html | 200 | B | yes | Your answer to her must be 'Drinc heil' (1, C16.txt) | Admitted at tier B: a transcription of a primary 1842 translation hosted on a personal site (not an institution). Located quote count 1 (8 words). Historical ca… |
| C17 | https://sk.sagepub.com/ency/edvol/download/the-sage-encyclopedia-of-alcohol-social-cultural-and-historical-perspectives/back-matter/d1678.pdf | 403 (redirect to sso.sagepub.com/connect/authorize, 13-byte  | B | no | — | UNREACHABLE: HTTP 403 with redirect to an SSO login page (captured 13-byte response). No login or paywall circumvention attempted. Search snippet quoted by sear… |
| C18 | https://digitalcommons.pace.edu/cgi/viewcontent.cgi?article=1326&context=pilr | 403 | B | no | — | UNREACHABLE: HTTP 403 (captured 5610-byte body). Not retried beyond the rule (403 is not transient).… |
| C19 | https://doi.org/10.21412/LEAVES_1003 | 302 then curl rc=28 timeout on all 4 attempts | B | no | — | UNREACHABLE: 4 attempts (1 + 3 retries with 20 s backoff) each timed out at --max-time 30 after the 302 to climas.u-bordeaux-montaigne.fr. No capture. The same … |
| C20 | https://doi.org/10.14989/250740 | 200 (landing page, 3058 bytes) | B | no | — | Rejected: the landing page carries no article text (JavaScript shell, 3058 bytes).… |
| C21 | https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/250740/1/zinbun_50_37.pdf | 200 but body is the 3058-byte landing HTML (redirected to /b | B | no | — | UNREACHABLE as a PDF: the server returned the HTML landing page with HTTP 200 for both the dspace and the non-dspace URL. Not treated as evidence. Recorded both… |
| C22 | https://ctext.org/liji/xiang-yin-jiu-yi | 200 (JavaScript challenge page, 2781 bytes) | A | no | — | UNREACHABLE: 'Checking the security of your connection' challenge page; no bypass attempted. Not evidence.… |
| C23 | https://sacred-texts.com/cfu/liki2/liki242.htm | 403 | A | no | — | UNREACHABLE: HTTP 403. The same translation is captured from archive.org (C25).… |
| C24 | https://sacred-texts.com/book/the-li-ki-the-book-of-rites-part-ii/xlii-hsiang-yin-kiu-i-or-the-meaning-of-the-drinking-festivity-in-the-districts | 403 | A | no | — | UNREACHABLE: HTTP 403.… |
| C25 | https://archive.org/stream/mlbd.sacredbooksofeas0000fmax.vol.28/mlbd.sacredbooksofeas0000fmax.vol.28_djvu.txt | 200 | A | yes | they bow when the cup is received, and when it is presented (in return) (1, C25.txt) | Admitted at tier A: primary translation (1885) in the OCR scan of the Motilal reprint. Located quote count 1 (14 words). Also: 'host and guests sharing it betwe… |
| C26 | https://hal.science/hal-01974763/document | 200 | B | yes | the toastmaster had to down a glass at one go after every toast (refusing to do so was a breach (1, C26.txt) | Admitted at tier B: institutional open archive, conference-paper text, not the Leaves print article. Located quote count 1 (20 words). Second line 'Refusing a t… |

Candidate rows with full fields (captures with sha256 and bytes; quote; quote_count; quote_capture; supports; reason; flip) are in `candidates.json`.

## Admitted (11; tier A 6, tier B 5)

- A: C1 (Laing 1844, Heimskringla, brage-goblet), C9 (Plato, Jowett, libation), C10 (Xenophon, Dakyns, pledge), C11 (Athenaeus, Yonge, pledge-cup), C13 (Gummere Beowulf, cup order; weaker fit), C25 (Legge 1885, cup reciprocity).
- B: C3 (Ynglinga ch. 36, Old Norse transcription), C12 (Tuite, order of toasts), C15 (OEA Feasting, toast as speech act), C16 (Giles 1842 via personal transcription, legendary toast formula), C26 (Duthille, HAL deposit; toastmaster penalty and refusal).

## Rejects (reason and flip condition)

- C2, C4–C8: Ynglinga chapters 41, 35, 37, 38, 39, 40 — no toast, cup or oath text (grep counts 0 for "bragaf" or "höfuðátt"). Flip: a located oath or toast line in any of them.
- C14: Gutenberg 981-0.txt, HTTP 404. Flip: none needed (working URLs used).
- C17: SAGE Encyclopedia of Alcohol "Toasting", HTTP 403 with SSO redirect. UNREACHABLE. Flip: a plain 200 copy.
- C18: Pace Law Review article, HTTP 403. UNREACHABLE.
- C19: Leaves article via doi.org/10.21412/LEAVES_1003: all 4 attempts timed out (rc 28) after a 302 to climas.u-bordeaux-montaigne.fr. UNREACHABLE. Flip: a successful fetch.
- C20: Kyoto handle landing page (3058 bytes): no article text.
- C21: Kyoto Zinbun PDF URL: HTTP 200 but the body is the 3058-byte HTML landing page. Not evidence. Flip: a real PDF.
- C22: ctext.org Liji: JavaScript bot-challenge page. UNREACHABLE. No bypass.
- C23, C24: sacred-texts.com Legge Li Ki ch. XLII (both URLs), HTTP 403. UNREACHABLE. The same translation is admitted only via archive.org (C25) as tier A.
- Not opened (search hits, tier C or off-scope): Toastmasters.org history, worldhistory.org, Merriam-Webster, FlatWorld textbook, digitens glossary, theday.com, Wellcome Athenaeus catalogue, Google Books hits, Academia.edu Manning chapter (not open access), Duranti 'ethnography of speaking' (general; not toast-specific), Strukowska speech-act review (general), MyNDIR Ynglinga (duplicate scope of C3), Gutenberg #65023 Athenaeus vol. 2 (same work as C11). Flip for each: a located toast, oath or pledge line on an opened page.

## Duplicate check against corpus/SOURCES.md (exact string count; `grep -c -F`)

Command: `grep -c -F -- "<url>" corpus/SOURCES.md` for each admitted URL and each rejected URL. All returned 0 except `hal.science` (2 hits, rows S143 and S173, different documents: a whistled-language paper and a landing page) and `anthroencyclopedia.com` (1 hit, S756 `/entry/sport`; `/entry/feasting` is not in the registry, so C15 is not a duplicate). No admitted URL is a duplicate. No knowledge file contains `toast`, `wassail`, `bragaf`, `toastmaster` or `health-drink` (checked by `grep -rliE` on corpus/knowledge; zero files).

## Commands and rc (representative; full log in fetch-attempts.log)

- `curl -sS -L --max-time 30 -o <raw> -w '%{http_code} %{size_download} %{url_effective}' <url>`: rc 0 for C1, C2, C3, C9, C10, C11, C12, C13, C15, C16, C25, C26 (HTTP 200); rc 0 with 403 for C17, C18, C23, C24; rc 0 with 404 for C14; rc 0 with 200 challenge body for C22; rc 0 with 200 landing body for C20, C21; rc 28 on all four attempts for C19.
- HTML to text: a Python html.parser strip (script/style dropped; block tags to newline) producing `.txt` for C2, C3, C4–C8, C11, C15, C16 (scratch conversion).
- PDF to text: `pdftotext` (no -layout) rc 0 for C12 and C26.
- Quote count: `python`: `ws(text).count(ws(quote))` with `ws = re.sub(r'\s+',' ',s).strip()`; rc 0; each admitted quote count 1 (counts recorded in candidates.json).
- Word count per quote: 6–23 words (all ≤ 25).

## Limits

- Tier A/B classification is by source type; referee status is not verified in the captures for C12, C26, C16, C15 (tier B by type).
- C13 supports the order of a cup-round in Beowulf, not a named toast formula; the entry's author should weigh that.
- Claim C coverage: 11 admitted, so the target of 6 tier A or B is met with 5 to spare.
- No knowledge entry or registry row is written by this seat (rule: research only).

## Outputs

- Stage: `.ufo/waves/round-98/w1/stage/ScoutSources98/` — `candidates.json`, `candidates.md`, `captures/` (all capture files with sha256 in candidates.json), `fetch-attempts.log`, `DONE`.
- Tooling: none installed; pdftotext (existing) used.
- Blockers: none for research. UNREACHABLE sources are listed above with their HTTP status; the Legge sacred-texts copies, the SAGE encyclopedia, the Pace article and the Leaves article were not obtained by plain HTTP.
