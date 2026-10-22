# ScribeDOverreads — claim D, over-reads (5 lines, 6 instances)

- Seat: `KotodamaR53.ScribeDOverreads` (scribe, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch main, jj-colocated.
- Assigned item: the six over-reads routed by `corpus/lessons/round-52-verifier-spotcheck.md:75-81` and `:136` (soften or re-source the over-reads on lines 54, 76, 79 and 121, and the "primitive peoples" sub-quote) against `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`.
- Scope note: D may cite only existing rows S001–S186 and must not cite S187 or above. Every replacement below cites rows S135–S166 only. No S-id ≥ S187 appears in the entry (`grep -o -E '\bS1[89][0-9]\b'` → no match; highest cited id is S184).
- All five sources re-opened this session by ordinary means (plain `curl`, no browser, no challenge worked around). Access date for every open below: **2026-10-22**.
- No tool was installed or upgraded this session (no install needed; `pdftotext` from poppler was already present).
- The L1 landed a first repair of these five lines in commit `374ae5a` ("round-53: claim D …"). This report gives my independent re-open, a replacement line for each over-read, the carrying quote with its printed location, and where the landed text differs from my draft or still over-reads.

## Result in one line

All six over-reads are removed at HEAD (`python3 -B reports/round-53/d-count.py` → `OPEN 0`, `SID_BAD 0`, exit 0), and every surviving clause of the five lines is carried by a page I opened this session — **except** that one routed premise was itself wrong (the "primitive peoples" sub-quote *is* on S181's page) and three residual over-reads/registry slips survive on the same lines (F1–F6 below).

---

## 1. Line 54 — two over-reads (OVER1 "force fixed formulas", OVER2 Hmong countries)

### What the opened page carries

S135 — Julien Meyer, David Díaz Reyes, Andre Batchelder-Schwab and Bernard Gautheron 2025, "Whistled Languages and Whistled Speech", *Encyclopedia of Language and Linguistics* (Elsevier), author-hosted copy.
URL `http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf` · route: direct (plain curl, HTTP 200, 1,439,365 bytes, PDF 1.7, 17 pages) · tier **B** (book / publisher encyclopedia, author-hosted copy) · opened 2026-10-22.

Carrying quotes, printed p. 7 of 17 (PDF p. 7 of 17; running foot "Whistled Languages and Whistled Speech 7"), Body Text, the intelligibility paragraph:

- "seven to eight contour tones" (5 words) — "this informational load is much higher in Hmong (seven to eight contour tones, depending on the dialect) than in Suruí (two level tones)".
- "two level tones" (3 words) — same sentence.
- "whistled sentences are more formulaic and therefore more predictable" (9 words) — "For this reason, in tonal languages with low informational load on spoken pitch, whistled sentences are more formulaic and therefore more predictable".
- "high levels of intelligibility can be reached in unpredictable sentences" (10 words) — same paragraph continues "…while high levels of intelligibility can be reached in unpredictable sentences in tonal languages with rich tonal systems for lexical load, such as Chinantec".

Chinantec, Hmong and Suruí are all named as whistled languages by the same source: the Figure 3 language map, printed p. 4 (PDF p. 4), lists "Chinantec", "Hmong, Akha" and "Tupari Suruí Karajá"; the p. 7 paragraph names Chinantec and Suruí in prose.

S135 does **not** name the Hmong's countries anywhere (`grep -c -i 'oaxaca\|laos\|thailand\|united states' s135.txt` → no "Laos", no "Oaxaca"; "United States" occurs only in an author affiliation) and does **not** place Chinantec in Oaxaca. So both the original "two tones (Suruí) force fixed formulas" and the original "Hmong (Laos, Thailand, United States) (S135)" were over-reads.

Rows that do carry the Hmong's dispersion, both already cited by this entry:
- S144 (Rialland 2005, *Phonology* 22(2), author manuscript, `http://www.silbo-gomero.com/wlanguages.pdf`, direct, HTTP 200, 793,306 bytes, 34 PDF pages, tier A), §2.2 "Notes on the Hmong whistled language", PDF p. 24: "widely dispersed in China, Vietnam, Laos, Thailand, Burma, continental France and French Guiana and the USA" (19 words).
- S141 (Morrison 1998, Hmong qeej, `https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf`, direct, HTTP 200, 233,242 bytes, tier B), printed p. 7 ¶[19]: "In current times, in Laos and Thailand, interested boys who are eight to ten years old begin to learn the note-fingering of the qeej" (24 words); printed p. 9 ¶[23]: "Hmong men continue to learn the qeej in the United States" (11 words).
- S155 (Sicoli 2016 abstract, Crossref record `https://api.crossref.org/works/10.1353/lan.2016.0028`, direct API, HTTP 200, tier B, abstract only) carries the Chinantec place name: "San Pedro Sochiapam Chinantec of Oaxaca, Mexico" (7 words).

### Replacement line (ready to paste, table columns kept)

```
| Whistled speech, tonal language | Lexical tone carried by whistle pitch, segmental cues in the amplitude envelope; the tonal inventory is the budget (S135) | Same whistle physics, but what a listener can take from a whistled sentence depends on the tone load: Hmong carries "seven to eight contour tones", Suruí "two level tones", so where the load is low "whistled sentences are more formulaic and therefore more predictable", while a rich tonal system (Chinantec) reaches "high levels of intelligibility can be reached in unpredictable sentences" (S135) | Chinantec (Oaxaca, Mexico) (S155); Hmong (dispersed in China, Vietnam, Laos, Thailand, Burma, continental France and French Guiana) (S144); Suruí (S135); hook map at `corpus/knowledge/linguistics/sound-symbolism.md:121` | Decide how many tones the surrogate keeps before deciding its vocabulary; detail in §4 |
```

Variant if the L1 prefers the landed geography-free example cell (also fully supported, and the minimum edit):

```
| Whistled speech, tonal language | Lexical tone carried by whistle pitch, segmental cues in the amplitude envelope; the tonal inventory is the budget (S135) | Same whistle physics, but what a listener can take from a whistled sentence depends on the tone load: Hmong carries "seven to eight contour tones", Suruí "two level tones", so where the load is low "whistled sentences are more formulaic and therefore more predictable", while a rich tonal system (Chinantec) reaches "high levels of intelligibility can be reached in unpredictable sentences" (S135) | Chinantec, Hmong and Suruí (S135); hook map at `corpus/knowledge/linguistics/sound-symbolism.md:121` | Decide how many tones the surrogate keeps before deciding its vocabulary; detail in §4 |
```

### Landed text at HEAD (commit `374ae5a`, line 54)

```
| Whistled speech, tonal language | Lexical tone carried by whistle pitch, segmental cues in the amplitude envelope; the tonal inventory is the budget (S135) | Same whistle physics, but what a trained listener can take from a whistled sentence depends on the tone load: Hmong has "seven to eight contour tones", Suruí "two level tones", and where the load is low "whistled sentences are more formulaic and therefore more predictable" (S135) | Chinantec, Hmong and Suruí (S135); hook map at `corpus/knowledge/linguistics/sound-symbolism.md:121` | Decide how many tones the surrogate keeps before deciding its vocabulary; detail in §4 |
```

Assessment: every clause is carried by S135 p. 7 / p. 4 as quoted above. The landed text **drops** the supported Chinantec half of the original reach cell ("a rich tone system (Chinantec) allows unpredictable sentences", carried by "high levels of intelligibility can be reached in unpredictable sentences … such as Chinantec"). Not false, but a depth loss; my draft restores it. The landed text also drops the Hmong countries outright, which is permitted ("either cut or cited to a row that lists them"); the S144/S141 rows above allow the geography to stay with a row that carries it.

## 2. Line 76 — /b/ merging with /k/ (OVER3)

### What the opened page carries

S147 — Meyer, Julien 2007, "Whistled Turkish: Statistical analysis of vowel distribution and consonant modulations", ICPhS XVI (Saarbrücken), paper 1286.
URL `http://www.icphs2007.de/conference/Papers/1286/1286.pdf` · route: direct (plain curl, HTTP 200, 337,860 bytes, PDF, 4 pages = printed pp. 837–840) · tier **A** (primary, measured, conference paper) · opened 2026-10-22.

Printed p. 839 (PDF p. 3 of 4), §3 "Consonants", right column:

- "very similar to [k] in whistles" (6 words) — "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles." The same paragraph says the fixed lips make "the labial articulation of [m], [p] and [b]" use a glottal occlusion, but the "very similar to [k]" claim is made for **[p] only**.
- Printed p. 839, §3.1.1 "Typical frequency shapes", left column: "bear intermediate positions between two of these categories, like [n], [b], [v] and [f]" (15 words) — i.e. [b] is a harder-to-classify intermediate case, not merged with [k].

Also on printed p. 838, §2.1 "Vocalic groups": "Such a complex vocalic system of eight whistled frequency intervals highlights four groups" — the support for "eight vowels as eight pitch bands in four groups" in the same row.

### Replacement line (ready to paste)

```
| Whistled Turkish (Kuşköy, Görele valley, Black Sea; village and summer high-plateau herders) | eight vowels as eight pitch bands in four groups, disambiguated by vowel harmony; consonants as frequency and amplitude modulations, silence for stops (S147; S146) | band overlap between vowels, and the occlusive [p], which the paper says is "very similar to [k] in whistles" (S147); [b] bears "intermediate positions between two of these categories, like [n], [b], [v] and [f]" (S147) | Black Sea mountains: the whistle takes over where speech fails, from about 40 to 100 m depending on the terrain; valleys carry it kilometres (S148; S149) |
```

### Landed text at HEAD (line 76)

```
| Whistled Turkish (Kuşköy, Görele valley, Black Sea; village and summer high-plateau herders) | eight vowels as eight pitch bands in four groups, disambiguated by vowel harmony; consonants as frequency and amplitude modulations, silence for stops (S147; S146) | band overlap between vowels, and the occlusive /p/ whistled "very similar to [k]" (S147) | Black Sea mountains: the whistle takes over where speech fails, from about 40 to 100 m depending on terrain; valleys carry it kilometres (S148; S149) |
```

Assessment: supported. Two nits: (a) the cell writes "/p/" in phonemic slashes while the source writes the phonetic "[p]" and the quoted fragment keeps the bracket — one convention per cell is cleaner; (b) the landed text discards a fact the page does carry about [b] (the intermediate-category sentence), which is the natural place to keep [b] without over-reading it.

## 3. Line 79 — "learned young" (OVER4)

### What the opened page carries

S151 — The Language Archive, Max Planck Institute for Psycholinguistics, deposit CAM20459, "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam".
URL `https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0` · route: direct (plain curl, HTTP 200, 29,619 bytes) · tier **A** (dataset, primary deposit) · opened 2026-10-22.

Carrying quote, deposit title and Description block (14 words): "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam". The page also carries: collection "Sochiapam Chinantec Whistled Speech", Country "Mexico (1)", collection path "mesoamerica / Otomanguean", persistent identifier `https://hdl.handle.net/1839/00-0000-0000-0016-B509-0`. It carries **no** acquisition-age statement, so "learned young" was an inference and is now marked `(to-verify)`.

Two more facts about the same row, checked while re-reading it:

- "Oaxaca" for San Pedro Sochiápam is carried by **S155** ("San Pedro Sochiapam Chinantec of Oaxaca, Mexico"), not by S151 (S151 says "Mexico" and "mesoamerica", never "Oaxaca"). S151's own registry cell also says "made with children of the village", which the page does not say — it says "children in San Pedro Sochiápam".
- The "discourse length" cell says "whistles stay short, single-clause, with simple repairs (S135)". S135 printed p. 7 says "whistled sentences tend to be simple with single-clause utterances and equally simple conversational repairs" (14 words) — the page says "simple with single-clause utterances", never "short". This is a residual over-read on the same routed line (F4).

### Replacement line (ready to paste)

```
| Chinantec (Sochiapam Chinantec, San Pedro Sochiápam, Oaxaca) | lexical tone: a rich tone system carries unpredictable sentences (S135) | discourse length: whistled sentences tend to be simple, single-clause, with equally simple conversational repairs (S135) | Oaxaca (S155); an archive deposit records spoken and whistled Chinantec elicited from children in San Pedro Sochiápam (S151); the age at which the register is learned is (to-verify) |
```

### Landed text at HEAD (line 79)

```
| Chinantec (Sochiapam Chinantec, San Pedro Sochiápam, Oaxaca) | lexical tone: a rich tone system carries unpredictable sentences (S135) | discourse length: whistles stay short, single-clause, with simple repairs (S135) | Oaxaca; an archive deposit records spoken and whistled Chinantec elicited from children in San Pedro Sochiápam (S151); the age at which the register is learned is (to-verify) |
```

Assessment: the routed over-read ("learned young") is repaired correctly and the inference is explicitly marked `(to-verify)`. Two residual items on the same line: the leading "Oaxaca" carries no row of its own (S155 does), and "whistles stay short" is not S135's wording (F4).

## 4. Line 121 — one drummer's biography stated as "Akan practice" (OVER5)

### What the opened page carries

S165 — Brown University, Department of Music, "Ghanaian Drumming".
URL `https://music.brown.edu/music-making/ensembles/ghanaian-drumming` · route: direct (plain curl, HTTP 200, 80,416 bytes) · tier **B** (university department page) · opened 2026-10-22.

"About" section, biographical paragraph on Kwaku Kwaakye (Martin) Obeng (19 words): "by seventeen he was appointed Royal Court Drummer to the high chief of the Aburi-Akuapim region of Eastern Ghana". The page's only other Akan statement is the ensemble note (23 words): "Adowa is a popular Akan dance-drumming genre from Ghana. The atumpan (talking drum) serves as the master drum in the ensemble." So the appointment is one man's biography; the page supports it as such, and its Akan link is the Adowa genre, not a court-office practice. The S165 registry scope cell already says as much: "the page supports the appointment and the course, not the wider Akan institution".

S166 — Gelfand, "Rhythms of Power: Royal Drumming in Aburi-Akuapem, Ghana", PhD dissertation, University of Illinois, 2000, item 87159.
URL `https://www.ideals.illinois.edu/items/87159` · route: **live page returned HTTP 403 Forbidden to a plain fetch on 2026-10-22; the abstract was read through the Wayback capture 20260311033125** (`http://web.archive.org/web/20260311033125/https://www.ideals.illinois.edu/items/87159`, HTTP 200, 26,200 bytes) · tier **B** (abstract only; the full text is restricted and was not opened) · opened 2026-10-22 via that capture.

Carrying quote, Abstract, Chapter III sentence (21 words): "who fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context". The same abstract calls them "Aburi court drummers".

### Replacement line (ready to paste)

```
| court and royal office | Yorùbá (south-west Nigeria) drumming families carry the hereditary title *baale* or *aare onilu* (chief drummer) in patronage with *oba* (sacred king) families (S164); in Ghana, one master drummer's biography says he was "appointed Royal Court Drummer to the high chief of the Aburi-Akuapim region of Eastern Ghana" at seventeen (S165), and Aburi court drummers are described as people "who fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context" (S166) | make the channel an office with a title, a patron and a duty of announcement; an unnamed skill has nobody to answer for it, and a court posting can be lost |
```

### Landed text at HEAD (line 121)

```
| court and royal office | Yorùbá (south-west Nigeria) drumming families carry the hereditary title *baale* or *aare onilu* (chief drummer) in patronage with *oba* (sacred king) families (S164); in Ghana, one master drummer's biography says "by seventeen he was appointed Royal Court Drummer to the high chief of the Aburi-Akuapim region" (S165), and Aburi court drummers are described as people "who fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context" (S166) | make the channel an office with a title, a patron and a duty of announcement; an unnamed skill has nobody to answer for it, and a court posting can be lost |
```

Assessment: supported. The landed quote truncates the source at "region" and drops "of Eastern Ghana"; using the full 14-word fragment is one word more and removes the truncation. The Yorùbá clause (S164) is unchanged by this repair; I re-opened S164 (`https://international.ucla.edu/africa/article/113707`, direct, HTTP 200) and it carries "Drumming families that carry the hereditary title of baale or aare onilu (chief drummer) maintain generations-old patronage relationships with families of Yorùbá obas (sacred kings)" — that clause stands.

## 5. Line 176 — the "primitive peoples" sub-quote (OVER6): the routed premise is wrong

### What the opened page carries

S181 — Dictionary.com, "bush telegraph" (Random House Unabridged; Collins; American Heritage Idioms).
URL `https://www.dictionary.com/browse/bush-telegraph` · route: direct (plain curl, HTTP 200, 72,425 bytes; fetched twice, with and without a browser user-agent, same bytes) · tier **B** (dictionary page) · opened 2026-10-22.

Carrying quotes and their locations on the page:

- Etymology block: "First recorded in 1875–80" (5 words).
- Sense 1 (the "American" variant): "any system of communication in which the natives of a jungle or bush region transmit news rapidly, as by runners, drum codes, or smoke signals" (24 words) → entry fragments "the natives of a jungle or bush region" (8 words) and "by runners, drum codes, or smoke signals" (7 words).
- The "British" variant, credited in the page's own footer to "Collins English Dictionary — Complete & Unabridged, 2012 Digital Edition": "a means of communication between primitive peoples over large areas, as by drum beats" (14 words).

**The string "primitive peoples" IS on S181's page.** It is the British/Collins sense, and the lane's own S181 row already quotes it in its anchor cell ("Collins: 'a means of communication between primitive peoples over large areas, as by drum beats'") and in its `teaches` cell. The round-52 closure's line 81 statement — "the sub-quote 'primitive peoples' is not on S181's page" — is therefore not reproducible on the page as served on 2026-10-22. Recorded verbatim for the canonical judge (F1). The closure appears to have read only the "American" sense; the same page's `EGRAPH` metadata also carries the sense-1 wording, which may be what was searched.

S182 — TIME, "Medicine: Live Virus in the Jungle" (11 Aug 1958), read through the registered Wayback copy `https://web.archive.org/web/20110131180047/http://www.time.com/time/magazine/article/0,9171,825425,00.html` (HTTP 200, 61,465 bytes; tier B; opened 2026-10-22). Carrying quote, ¶ beginning "Working both sides of the stream" (16 words): "Working both sides of the stream, they got native chieftains to pass the word by jungle telegraph". (In the raw HTML the phrase is broken across a line break, "jungle \ntelegraph"; after whitespace normalisation it reads as above. A grep for the unbroken string on the raw HTML returns 0 — the visible text is the same.)

### Replacement line (ready to paste)

```
| 'Jungle telegraph' / 'bush telegraph' is a neutral technical name | R | it is an English idiom, "First recorded in 1875–80", whose dictionary sense speaks of "the natives of a jungle or bush region" sending news "by runners, drum codes, or smoke signals" (S181); a 1958 TIME report says a medical team "got native chieftains to pass the word by jungle telegraph" (S182) — name the community's own system instead |
```

Alternative if the L1 restores the colonial-framing sense and amends the counter's OVER6 leg accordingly (both senses are on the page, so either is truthful; only the counter's literal-string test forbids the second):

```
| 'Jungle telegraph' / 'bush telegraph' is a neutral technical name | R | it is an English idiom, "First recorded in 1875–80"; its American sense speaks of "the natives of a jungle or bush region" sending news "by runners, drum codes, or smoke signals", and its British (Collins) sense of "a means of communication between primitive peoples over large areas, as by drum beats" (S181); a 1958 TIME report says a medical team "got native chieftains to pass the word by jungle telegraph" (S182) — name the community's own system instead |
```

### Landed text at HEAD (line 176)

```
| 'Jungle telegraph' / 'bush telegraph' is a neutral technical name | R | it is an English idiom, "First recorded in 1875–80", whose dictionary sense speaks of "the natives of a jungle or bush region" sending news "by runners, drum codes, or smoke signals" (S181); a 1958 TIME report says a medical team "got native chieftains to pass the word by jungle telegraph" (S182) — name the community's own system instead |
```

Assessment: identical to my first replacement. Every clause is carried by the pages opened above (S181 Etymology and sense 1; S182 ¶). The landed text drops the Collins sense, which the counter's OVER6 leg requires; the fact that the dropped clause was itself on the page is F1.

---

## Findings for the L1 (author-lane advice; nothing here is an admission)

**F1 — the routed OVER6 premise does not reproduce.** `corpus/lessons/round-52-verifier-spotcheck.md:81` reads "line 176: the sub-quote 'primitive peoples' is not on S181's page." On 2026-10-22, plain `curl https://www.dictionary.com/browse/bush-telegraph` (HTTP 200) shows the British/Collins variant "a means of communication between primitive peoples over large areas, as by drum beats", and `corpus/SOURCES.md` row S181 already quotes that string in its anchor and `teaches` cells. The landed line 176 is true either way; the closure's note (and any lesson text repeating it) should say the string is present under the British variant, and `reports/round-53/d-count.py`'s OVER6 leg counts a page-supported phrase as an open defect purely by literal match. The counter's own docstring concedes this ("this counter shows the routed wording is gone, not that the replacement is true").

**F2 — S166's route is not recorded in its row.** The live repository page `https://www.ideals.illinois.edu/items/87159` answered HTTP 403 to a plain fetch on 2026-10-22; the abstract was read through Wayback capture 20260311033125. The S166 row's `anchor` cell says only "item 87159, Abstract, Chapter III sentence" and the `opened` cell gives a date, with no route. Recommend adding the capture id to the anchor cell, in the same spirit as the routed S157 captcha note (`corpus/lessons/round-52-verifier-spotcheck.md:144`).

**F3 — the registry still carries three of the over-reads this round repaired in the entry.** These are `corpus/SOURCES.md` cells, outside D's landing set, so they are for the L1 or the C seat:
- S147 `teaches`: "lip-locked /p/, /b/ approach /k/" — S147 states the "very similar to [k]" claim for [p] only (printed p. 839).
- S151 `teaches`: "made with children of the village — the register is transmitted young" — the deposit title says "children in San Pedro Sochiápam"; the page carries no transmission-age claim.
- S135 `anchor`: "Abstract and 'Body Text', PDF pp. 1–2 of 17" — the passage the entry now quotes is on printed p. 7 of 17 (the informational-load paragraph); the anchor cell should reach it.

**F4 — two residual over-reads remain on the routed lines 54/79.**
- Line 79's leading "Oaxaca" has no row of its own; S155's abstract carries it ("San Pedro Sochiapam Chinantec of Oaxaca, Mexico").
- Line 79's "whistles stay short" is not S135's wording; S135 p. 7 says "whistled sentences tend to be simple with single-clause utterances and equally simple conversational repairs".
Both are small, both sit on lines D already touches, and neither is counted by the counter.

**F5 — depth lost on line 54.** The original reach cell's Chinantec half ("a rich tone system (Chinantec) allows unpredictable sentences") was carried by S135 p. 7 ("high levels of intelligibility can be reached in unpredictable sentences … such as Chinantec") and was dropped in the landing. Restoring it costs nothing and strengthens the depth axis, which is D's axis.

**F6 — access notes.** S140 (`https://www.lddjournal.org/article/id/2939/`) served an Anubis bot-challenge interstitial ("Making sure you're not a bot!", JS required, HTTP 200 with no article text) to a plain curl on 2026-10-22: challenge met, not passed. I did not route around it and used it for nothing. S140 is cited by the entry (lines 58, 61 and others) but not by any of the five lines in this seat's scope. S166 is reachable only through the Wayback capture (F2).

## Evidence and commands run (read-only)

- `python3 -B reports/round-53/d-count.py` at HEAD `374ae5a` → `OPEN 0` / `SID_BAD 0 [] cited 50`, exit 0.
- `grep -o -E '\bS[0-9]{3}\b' corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md | sort -u` → 50 ids, highest S184; no S187+.
- Re-opens (plain `curl`, no browser): S135 (HTTP 200, 1,439,365 B, 17 pp.), S147 (200, 337,860 B, 4 pp.), S151 (200, 29,619 B), S165 (200, 80,416 B), S181 (200, 72,425 B, twice), plus S166 via Wayback capture 20260311033125 (200), S182 via the registered capture 20110131180047 (200), S144 (200, 793,306 B), S141 (200, 233,242 B), S155 via the Crossref API (200, 2,968 B), S164 (200).
- `pdftotext -layout` used on the S135, S141, S144 and S147 PDFs for page-accurate quotes; per-page extraction confirmed printed pagination (S135 foot "… Speech 7"; S147 foot "www.icphs2007.de 839"; S141 foot "Hmong Studies Journal Page 7 of 17").

## Unrun checks

- No claim-D acceptance script, README sweep or `accept-c.py` was run by this seat (out of scope; the L1's gate).
- The full text of S147, S141, S144 and S166 was not read (respectively: only the sections cited; S166 is abstract-only by the row's own scope, the full text being restricted; S141 only the pages holding the two quoted paragraphs; S144 only §2.2 and its vicinity).
- The S135 PDF's 17 pages were read as text with `pdftotext`; figures were not inspected as images.
- I did not attempt to open S140 beyond the challenge interstitial (F6).

## Files touched

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-53/build/ScribeDOverreads.md` — this report (new file, seat's own report path).
- No corpus file, SOURCES row, judge or script was edited, committed, pushed or published by this seat; the five replacement lines above are drafted text for the L1 to paste.
