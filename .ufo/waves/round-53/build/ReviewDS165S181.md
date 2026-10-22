# ReviewDS165S181: claim D falsifier, entry lines 121 and 176

- Reviewer: KotodamaR53.ReviewDS165S181 (leaf seat; no subagents, no background jobs)
- Date: 2026-10-22
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin. HEAD 60f1d2a. Working copy at my run: `M corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`; untracked `.ufo/waves/round-53/`, `corpus/lessons/round-53.md`, `reports/round-53/final-measures.py`. `corpus/SOURCES.md` unmodified.
- Scope: entry lines 121 and 176 only, checked against registry rows S164, S165, S166, S181, S182 and the pages behind them.

## Verdict

Not cleared. Both lines still state things their sources do not carry. The counter `reports/round-53/d-count.py` printed `OPEN 6` at my run, not `OPEN 0`. The routed fix for line 176 targets a quote the page does contain ("primitive peoples"), and it misses the claims the page does not support: "runners", "non-Western" and "colonial-era".

Terms used below: a "row" is an entry in `corpus/SOURCES.md`; "the counter" is `d-count.py`; a "leg" is one check inside the counter; "over-read" means the wording claims more than its source says.

## Findings by severity

### High

1. **Line 121: "in Akan (Ghana) practice a master drummer is ... at seventeen (S165)".** The clause generalizes one teacher's biography into a practice. The S165 row's own teaches column says the page supports "the appointment and the course, not the wider Akan institution" (`SOURCES.md:194`, teaches cell). The page's appointment sentence contains no "Akan". "Akan" appears once, on the Adowa genre (Brown page, Videos section). Source: corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:121.

2. **Line 176: "used in 1958 for a relay of human runners (S182)".** The TIME article has no "runner", no "relay" and no "drum". Its wording is "they got native chieftains to pass the word by jungle telegraph" (paragraph beginning "Working both sides of the stream"). The S182 row's teaches cell says "a relay of human runners in the Congo, not a drum code" (`SOURCES.md:211`). The row over-reads and the entry copies it. The phrase "as by runners" comes from the S181 definition, not from S182 [INFERENCE: the likely source of the error].

3. **Line 176: "senses frame non-Western people as ..."**. "Non-Western" is on neither the S181 page nor the S181 row. The page's Australian sense 1 is about "criminals, originally bushrangers" and police, which is not a non-Western framing at all.

4. **Counter leg OVER6 is a false positive that rewards the wrong fix.** OVER6 (`d-count.py:37`) flags the string "primitive peoples" on line 176. That phrase is on the S181 page verbatim (Collins, British, sense 1). The round-52 routed item that says otherwise (`corpus/lessons/round-52-verifier-spotcheck.md:81`, repeated at :136) is wrong for this page. Clearing OVER6 by deleting the phrase would remove a correct quote and leave the real over-reads in place.

5. **Status: the counter does not print OPEN 0.** At my run it printed `OPEN 6`: OVER1 and OVER2 at line 54, OVER3 at line 76, OVER4 at line 79, OVER5 at line 121, OVER6 at line 176; `SID_BAD 0 [] cited 50`; exit 1. The FRAG and WROW legs printed nothing, so they are clear. The entry was still being edited during my review: lines 174, 177, 179 and 181 differed between my first read and my last one. Lines 121 and 176 did not change.

### Medium

6. **Line 176: "a colonial-era English idiom".** The only support is the S181 row's gloss, "its colonial-era wording" (`SOURCES.md:210`, scope cell). The page does not say "colonial". Its example sentences show present-day figurative uses: a New Yorker sentence from 2015 ("La bola, Cuba's bush telegraph, transmits news around the island long before it is covered by state media.") and a Wall Street Journal sentence from 2016 ("the bush telegraph of root systems."). The page also has one undated "Time Magazine Archive" example that names Limbe. The date and senses support "idiom, first recorded 1875–80"; "colonial-era" is [INFERENCE].

7. **Line 121: "resisting change of repertoire" drops the counter-clause.** The S166 row carries "while accepting new performance contexts" (`SOURCES.md:195`, teaches cell). The abstract says the drummers "fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context". The entry keeps the resistance and drops both "fiercely" and the acceptance. The abstract frames the chapter as "seemingly conflicting attitudes", so the one-sided sentence misstates the chapter.

8. **The counter's OVER5 leg is a literal string test.** It searches for "in Akan (Ghana) practice" (`d-count.py:36`). A rewrite such as "in Akan (Ghana) court practice" clears it and keeps the over-read. The counter's own docstring says a cleared leg "shows the routed wording is gone, not that the replacement is true" (`d-count.py:18-19`).

### Low

9. Row S164 says "titles baale and aare onilu" (`SOURCES.md:193`, teaches cell). The page says "baale or aare onilu" (paragraph beginning "Of particular importance"). The entry's "or" is correct; the row is wrong.
10. Row S165 scope says "Akan (Ghana) court drumming as an appointment" (`SOURCES.md:194`). That contradicts its own teaches cell. The teaches cell says "at seventeen"; the page says "by seventeen".
11. Entry line 121 says "drumming families carry the hereditary title". The page says "Drumming families that carry the hereditary title". The restrictive "that carry" is dropped (minor).
12. Row S166 cites `items/87159` only. The item page's own permalink, in the 2025 capture, is https://hdl.handle.net/2142/85878.

## 1. Sources re-opened

| Row | Route and date | What the page says (verbatim, with location) | Row check |
|---|---|---|---|
| S164 UCLA, Ruskin, 1 Feb 2010 | https://international.ucla.edu/africa/article/113707. Plain request, raw HTML, 2026-10-22. The reader view returned only meta tags, so the body came from the raw HTML. | Paragraph beginning "Of particular importance": "Drumming families that carry the hereditary title of baale or aare onilu (chief drummer) maintain generations-old patronage relationships with families of Yorùbá obas (sacred kings)." Paragraph beginning "The Yorùbá dùndún, known in English as": "Free from many of the restrictions that traditionally govern older Yorùbá drums, the talking drum has long been used in a variety of sacred and secular contexts throughout southwestern Nigeria." Paragraph beginning "The initial phase of field research": "I conducted interviews with the traditional heads of drumming families in the towns of Iragbiji, Ede, Ila-Orangun, and Erin-Osun." | Quotes match. The row's "baale and aare onilu" differs from the page's "or" (item 9). |
| S165 Brown, Ghanaian Drumming | https://music.brown.edu/music-making/ensembles/ghanaian-drumming. Plain request, reader text, 2026-10-22. | "About", first paragraph: "Born in Ghana, West Africa, Kwaku began drumming at the age of five, and by seventeen he was appointed Royal Court Drummer to the high chief of the Aburi-Akuapim region of Eastern Ghana." Same paragraph: "Kwaku Kwaakye (Martin) Obeng is a composer, master drummer, dancer and educator who has worked internationally for the past 25 years." Videos, "Adowa": "Adowa is a popular Akan dance-drumming genre from Ghana." | The page is one teacher's biography. "Akan" is not attached to the appointment. |
| S166 Gelfand, PhD 2000, Illinois | https://www.ideals.illinois.edu/items/87159. Live plain request: HTTP 403, no body returned. Archive copy used: https://web.archive.org/web/20250121173716/https://www.ideals.illinois.edu/items/87159 (capture 2025-01-21, reached through the web/2024 redirect). This is a challenge or refusal met and not passed. I changed no headers and used no browser. | Abstract: "Chapter III explores the seemingly conflicting attitudes toward innovation and conservation displayed by Aburi court drummers, who fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context." Abstract: "Chapter II presents an overview of musical activity in Aburi and explains the mechanics of Akan speech surrogates." Access note: "This item is only available for download by members of the University of Illinois community." Permalink on the same page: https://hdl.handle.net/2142/85878 | The row quote matches the abstract. The entry drops the counter-clause the row carries (item 7). |
| S181 Dictionary.com, "bush telegraph" | https://www.dictionary.com/browse/bush-telegraph. Plain request, full entry returned, 2026-10-22. | Noun, sense 1 (Random House): "any system of communication in which the natives of a jungle or bush region transmit news rapidly, as by runners, drum codes, or smoke signals." Under the heading "bush telegraph British", Collins sense 1: "a means of communication between primitive peoples over large areas, as by drum beats". Etymology: "First recorded in 1875–80". Australian sense 1: "any chain of communications by which criminals, originally bushrangers, are warned of police movements." Example, New Yorker, Jul. 20, 2015: "La bola, Cuba's bush telegraph, transmits news around the island long before it is covered by state media." | Every quote in the row matches. The page contains no "colonial", "non-Western", "technical" or "neutral". Nothing differs from the plain-request text the row cites. |
| S182 TIME, "Medicine: Live Virus in the Jungle" | Archive copy https://web.archive.org/web/20110131180047/http://www.time.com/time/magazine/article/0,9171,825425,00.html, read 2026-10-22. Same capture as the row. | Dateline: "Monday, Aug. 11, 1958". Paragraph beginning "Working both sides of the stream": "Working both sides of the stream, they got native chieftains to pass the word by jungle telegraph." Same paragraph: "At their chieftains' bidding, 215,504 men, women and children trooped down to rally points where the doctors were waiting with jugs of ice-cold Chat." Paragraph beginning "To combat epidemics": "... in the Belgian Congo ...". The article is about a live-virus polio vaccine trial. | The phrase and the date are carried. No "runner", "relay" or "drum" appears in the text I read in full. The row's "relay of human runners ... not a drum code" is not on the page. |

## 2. Line 121 clause audit (court and royal office, attested-case cell)

Entry text, verbatim: "Yorùbá (south-west Nigeria) drumming families carry the hereditary title *baale* or *aare onilu* (chief drummer) in patronage with *oba* (sacred king) families (S164); in Akan (Ghana) practice a master drummer is "appointed Royal Court Drummer to the high chief of the Aburi-Akuapim" at seventeen (S165), and Aburi-Akuapem court drummers are described as resisting change of repertoire (S166)"

| Clause | Does the row carry it? (column) | Does the page carry it? | Verdict |
|---|---|---|---|
| Yorùbá (south-west Nigeria) dùndún drumming | Yes, S164 scope | Yes ("southwestern Nigeria") | Carried |
| drumming families carry the hereditary title | Yes, S164 teaches ("hereditary titles") | Yes, but the page says "Drumming families that carry" | Carried; restrictive "that carry" dropped (item 11) |
| *baale* or *aare onilu* | No. The row says "baale and aare onilu" | Yes, "or" | Entry correct; row wrong (item 9) |
| (chief drummer) | Yes, S164 scope ("chief-drummer titles") | Yes | Carried |
| in patronage with *oba* (sacred king) families | Yes, S164 teaches ("generations-old patronage to oba families") | Yes | Carried |
| in Akan (Ghana) practice | Scope cell only: "Akan (Ghana) court drumming as an appointment". The teaches cell says the page supports only "the appointment and the course, not the wider Akan institution". | No. The appointment sentence has no "Akan". "Akan" appears only on the Adowa genre. | **Not carried. Contradicted by the same row.** (item 1) |
| a master drummer is ... | The teaches cell uses the phrase for the one person in the anchor. | One biography: "a composer, master drummer, dancer and educator". | **Not carried as a practice claim.** Carried only as one person's biography (item 1). |
| "appointed Royal Court Drummer to the high chief of the Aburi-Akuapim" (quoted) | Yes, S165 teaches (without "the") | Yes, verbatim substring | Carried |
| at seventeen | Yes, S165 teaches | No. The page says "by seventeen". | Carried by the row; row and entry say "at", not "by" (item 10) |
| Aburi-Akuapem court drummers are described as resisting change of repertoire | S166 teaches: "fiercely resisting change in repertoire and performance practice while accepting new performance contexts" | Abstract: "fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context" | **Partly carried.** Drops "fiercely" and the acceptance clause (item 7). |

The design-consequence cell, "make the channel an office ... a court posting can be lost", is the lane's heuristic (labelled H). No row or page carries "a court posting can be lost" [INFERENCE: heuristic]. I did not count it as a source claim.

## 3. Line 176 clause audit (calibration row "'Jungle telegraph' / 'bush telegraph' is a neutral technical name")

Entry text, verbatim: "it is a colonial-era English idiom (first recorded 1875–80; senses frame non-Western people as "natives of a jungle"/"primitive peoples", S181), used in 1958 for a relay of human runners (S182) — name the community's own system and the relay"

| Clause | Does the row carry it? | Does the page carry it? | Verdict |
|---|---|---|---|
| it is an English idiom | S181 scope and anchor: idiom, dictionary credits | Yes: "Idioms from The American Heritage® Idioms Dictionary" credit; two English dictionaries | Carried |
| colonial-era | Gloss only: S181 scope cell "its colonial-era wording" | No. The page's examples show recent figurative uses (item 6). | **Not carried by any source text.** [INFERENCE] (item 6) |
| first recorded 1875–80 | Yes, S181 anchor and teaches | Yes: "First recorded in 1875–80" | Carried |
| senses frame non-Western people as | No. The teaches cell says only "senses carry 'natives of a jungle'/'primitive peoples' wording". | No. "Non-Western" is not on the page. The Australian sense concerns bushrangers and police. | **Not carried.** [INFERENCE] (item 3) |
| "natives of a jungle" | Yes, S181 anchor | Yes: "the natives of a jungle or bush region" (American, sense 1) | Carried |
| "primitive peoples" | Yes, S181 anchor and teaches | Yes: "a means of communication between primitive peoples over large areas, as by drum beats" (Collins, British, sense 1) | **Carried.** The routed claim that it is not on the page is wrong (item 4). |
| used in 1958 | Yes, S182 anchor | Yes: dateline "Monday, Aug. 11, 1958"; "pass the word by jungle telegraph" | Carried |
| for a relay of human runners | S182 teaches: "named a relay of human runners in the Congo, not a drum code" | No. No "runner", "relay" or "drum" in the article. The page says chieftains "pass the word". | **Not carried by the page. The row over-reads and the entry copies it.** (item 2) |
| (S182) as the source of the claim | As above | The page supports the phrase's use only | Partly supported |
| name the community's own system and the relay | Advice, not a claim | n/a | Not counted |

## 4. Direct answer: is "primitive peoples" on the S181 page?

Yes. It appears verbatim in the Collins (British) sense 1, under the "bush telegraph British" heading, in the plain-request text I read today. It is not in the Random House sense 1. The entry's sentence puts the two quoted phrases together under "senses", which is accurate, since both come from the page's definitions. The defect on line 176 is "non-Western" and "runners", not "primitive peoples".

## 5. Counter check

Command, run from the lane root, read-only: `python3 -B reports/round-53/d-count.py`. Exit 1.

Output at my run:
- `OPEN 6`
- OVER1 at line 54 ("force fixed formulas")
- OVER2 at line 54 (Hmong country list)
- OVER3 at line 76 (/b/ with /k/)
- OVER4 at line 79 ("learned young")
- OVER5 at line 121 ("in Akan (Ghana) practice")
- OVER6 at line 176 ("primitive peoples")
- `SID_BAD 0 [] cited 50`
- FRAG and WROW legs: no output, so clear.

Design points for the counter (items 4 and 8):
- OVER5 looks for the literal wording. A rewrite that keeps the over-read clears it.
- OVER6 requires the removal of a quote the page supports. Retire it, or re-target it to the real over-reads. Do not clear it by deleting the phrase.
- No leg checks "runners", "non-Western", "colonial-era", or a general "a master drummer is ... appointed" claim. These need a reviewer's check, not a string count.

## 6. Drafted replacement text (in-entry only; cites S164, S165, S166, S181, S182 only; no S187 or above)

Line 121. Replace the Akan clause and the Aburi clause with:

> ... in patronage with *oba* (sacred king) families (S164); the biography of one master drummer says that "by seventeen he was appointed Royal Court Drummer to the high chief of the Aburi-Akuapim region of Eastern Ghana" (S165); the abstract of an Aburi dissertation says that Aburi court drummers, who "fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context" (S166)

Optional Akan label, sourced to the thesis abstract rather than to S165:

> Chapter II of the same dissertation "explains the mechanics of Akan speech surrogates" (S166)

Line 176. Replace the claim cell with:

> it is an English idiom first recorded 1875–80 (S181); its recorded senses use the words "natives of a jungle or bush region" (American) and "primitive peoples" (Collins, British) (S181); in a 1958 TIME report on a polio vaccine trial, the team "got native chieftains to pass the word by jungle telegraph" (S182) — name the community's own system and the channel it used

Do not paste: "colonial-era", "non-Western people", or "relay of human runners". None is on the page. Keep any of them only with an [INFERENCE] label.

## 7. Routed items outside D's write set

D lands only the entry, so these go to the registry owner and the lessons owner.

- S164 row (`SOURCES.md:193`): "titles baale and aare onilu" becomes "title baale or aare onilu".
- S165 row (`SOURCES.md:194`): scope "Akan (Ghana) court drumming as an appointment" becomes "one master drummer's appointment (biography)", to match its own teaches cell. Teaches "at seventeen" becomes "by seventeen".
- S166 row (`SOURCES.md:195`): add the permalink https://hdl.handle.net/2142/85878. Record that the live item refused access on 2026-10-22 and that the abstract was read from the 2025-01-21 capture.
- S181 row (`SOURCES.md:210`): scope "its colonial-era wording" is deleted, or marked as the lane's inference.
- S182 row (`SOURCES.md:211`): teaches "named a relay of human runners in the Congo, not a drum code" is deleted. Keep only the phrase's use in 1958 and the Belgian Congo context.
- Lessons, `corpus/lessons/round-52-verifier-spotcheck.md:81` and :136: delete the "primitive peoples" item, which is wrong. Add "runners", "non-Western" and "colonial-era" as open items.
- `reports/round-53/d-count.py`: retire OVER6. Add checks for the new items. OVER5 needs a review step, not a literal check.

## 8. Verification

Run:
- Plain requests: S164 (raw HTML and reader), S165, S181.
- Archive copies: S166 (Wayback capture 2025-01-21), S182 (the row's own capture).
- Registry rows: `corpus/SOURCES.md:193-195` and `:210-211`, raw.
- Entry lines 119–126, 168–178, 121 and 176, raw.
- `python3 -B reports/round-53/d-count.py` (read-only).
- `git rev-parse --short HEAD` and `git status --short` (read-only).

Absence claims rest on full-text reads of the S181 and S182 pages. The grep tool returned partial hit lists on these URLs, so I did not rely on it for absence.

Not run:
- Live S166: HTTP 403 today; the archive copy only.
- lsp: not available to this seat. The file is Markdown with no code callers, so the checks were literal text reads.
- `accept-c.py` and the README sweep: C scope, not mine.
- Lines 54, 76 and 79: other seats.

Installs and upgrades: none.

## 9. Residual risk

- The entry is mid-edit in the working copy (`M`). Lines 54, 76 and 79 were still open at my run, and lines 174, 177, 179 and 181 changed while I was reviewing.
- The S166 abstract comes from a 2025-01-21 archive copy. The live page refused access today, so the abstract is not confirmed as of today.
- "Colonial-era" is a judgment, not a source statement. The S181 page's example sentences show recent figurative uses.
- The S164 claims rest on the author's own interviews in four named towns, plus one family in Ile-Ife. The row's scope says "as reported by the field researcher". The entry should not generalize beyond that.
- Line 124 and other lines were outside this scope and were not checked.
