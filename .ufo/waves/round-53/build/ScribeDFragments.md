# ScribeDFragments — round 53, claim D: the ten `, -N` draft-id fragments and the two wrong-row citations

- Seat: `KotodamaR53.ScribeDFragments` (leaf; no subagent dispatch, no background jobs, no lane mutation).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. **Nothing in the lane was edited except this report file.** The target entry was read, never written; no SOURCES row was touched; no `jj`/`git` write command was run in the lane.
- Assigned item: map each `, -N` draft-id fragment in `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` to its registered S-id, and draft the verbatim replacement text for every affected line.
- Result: **all 10 fragments mapped; 7 replacement lines drafted verbatim; S159 and S162 re-opened by ordinary means in this session with carrying passages quoted.** Two of the mapped S-ids (S163 on line 113, and the row-anchor label of S159) need an L1 decision that is outside the entry; both are flagged verbatim in §6.

---

## 1. Axes named

| axis | state at the start | evidence |
|---|---|---|
| citation stability | 10 bare `, -N` tokens remain on 7 lines; a bare draft id is not a stable id (QUALITY criterion 1) | `grep -o -E ', -[0-9]+\b'` → 10 hits on lines 106, 107, 113, 174, 177, 179, 181 (§3) |
| row attribution | 2 cells cite a row that does not carry the quoted fact (line 106 "working their farms"; line 113 mobile-phone decline) | `corpus/lessons/round-52-verifier-spotcheck.md:74` (wrong-row bullet) and the re-opened sources in §4 |
| source freshness | S159 and S162 had to be re-opened before any replacement could be justified | §4, HTTP 200 for both, no challenge met |
| scope containment | every replacement cites an existing row ≤ S186; no S187+, no new gesture entry, no `corpus/lessons/round-53.md` | §5, §6 |

No axis was harmed: the mapping reuses rows that the round-52 closure already confirmed (`S162, S159, S174, S175, S176, S157, S180` — its fragment bullet, `round-52-verifier-spotcheck.md:73`), and no quoted wording was altered.

---

## 2. Files read (lane worktree, read-only)

| file | lines read | used for |
|---|---|---|
| `corpus/lessons/round-52-verifier-spotcheck.md` | `:1-83`, `:99-154` | the routed defect text, the wrong-row verdict, the fragment list |
| `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | `:95-120`, `:160-195` (raw), plus the grep sweep over the whole file | the exact current wording of every affected line |
| `corpus/SOURCES.md` | rows S157–S186 (`grep '^\| S1(5[7-9]|6[0-9]|7[0-9]|8[0-4]) \|'`) | registry status, tier, `used-by` of every candidate row |
| `corpus/lessons/round-52.md` | `:30-125` | the integrator's Gate lines (which carry the seat that opened each row) and the mapping note at `:39` |
| `.ufo/waves/round-52/build/ScribeSec08Ecology.md` | whole file | the seat's own draft-id → source table for §6/§7 of the entry |
| `.ufo/waves/round-52/build/ScribeSec14Calibration.md` | whole file | the seat's own draft-id → source table for §10 of the entry |

Base for every in-corpus line reference: the lane worktree as read on 2026-10-22 (entry head line 10 records `verified-at: 2026-10-22 — written against dea5ece`; the round-53 prerequisite is `9ae5af9`).

---

## 3. The fragment sweep (exact, whole file)

```
$ grep -n -o -E ', -[0-9]+' corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
106:, -6
107:, -6
113:, -4
174:, -5
177:, -5
177:, -6
177:, -7
179:, -12
181:, -2
181:, -12
```

Count: **10 tokens on 7 lines** (the round-52 closure counted 11 on 8 lines; its line-104 token was already repaired by the round-53 prerequisite, which re-cited line 104 to **S184**, the new UNESCO nomination-file row for element 00172 — no fragment remains on line 104). A wider sweep for any other draft-id shape (`[,(] ?-[0-9]+`) returns exactly the same 10 hits.

---

## 4. Per-fragment mapping table

Seat draft ids are the round-52 seats' own `NEW-<SeatName>-<n>` ids: section 6 of the entry (lines 100–113) came from `ScribeSec08Ecology`, section 10 (lines 164–181) from `ScribeSec14Calibration`. Each seat's report carries its own id → source table, and `corpus/lessons/round-52.md` Gate lines carry the assigned S-id with the opening seat named. Both agree, row for row.

| line | token | seat draft id | S-id | evidence |
|---|---|---|---|---|
| 106 | `, -6` | `NEW-ScribeSec08Ecology-6` | **S162** | `ScribeSec08Ecology.md` §4 row 6 = the Cloarec-Heiss 1999 PDF (`Article-F.Cloarec-Heiss.pdf`); `round-52.md` Gate line "S162 — https://regroupement-rcms.org/…/Article-F.Cloarec-Heiss.pdf … Seat: ScribeSec08Ecology"; `SOURCES.md` row S162 = Cloarec-Heiss, tier A, `mined`. The passage "working their farms" is at `S162.txt` §2.2.2 "Informative units" (PDF p. 7 = printed p. 152). |
| 107 | `, -6` | `NEW-ScribeSec08Ecology-6` | **S162** | same row. "someone gets lost in the bush" is at `S162.txt` §2.1.2 "Sociolinguistic circumstances" (the sentence the Gate line quotes). |
| 113 | `, -4` | `NEW-ScribeSec08Ecology-4` | **S159** | `ScribeSec08Ecology.md` §4 row 4 = UNESCO nomination form 00658 (`https://ich.unesco.org/doc/src/36234-EN.doc`); `round-52.md` Gate line "S159 — … 36234-EN.doc … Seat: ScribeSec08Ecology"; `SOURCES.md` row S159 = that nomination form, tier A, `mined`. The mobile-phone decline is in it at §2 "Need for urgent safeguarding": "One of the most important threats to this element is the increase in the use of mobile phones." (re-opened this session, §4 below). |
| 174 | `, -5` | `NEW-ScribeSec14Calibration-5` | **S174** | `ScribeSec14Calibration.md` §2 row 5 = McPherson 2019, "Musical adaptation as phonological evidence" (NSF copy `par.nsf.gov/servlets/purl/10166941`); `round-52.md` Gate line "S174 — https://par.nsf.gov/servlets/purl/10166941 … Seat: ScribeSec14Calibration"; `SOURCES.md` row S174, tier B, `mined`. Its §4, p. 13 carries "Speech surrogates are found all around the world on a wide variety of instruments." |
| 177 | `, -5` | `NEW-ScribeSec14Calibration-5` | **S174** | same row as above (instruments behind drum-speech). |
| 177 | `, -6` | `NEW-ScribeSec14Calibration-6` | **S176** | `ScribeSec14Calibration.md` §2 row 6 = Gleick, "Drums That Talk" (PEN America, `pen.org/drums-that-talk/`); Gate line "S176 — https://pen.org/drums-that-talk/ … Seat: ScribeSec14Calibration"; `SOURCES.md` row S176, tier B, `mined`. Its row's own `teaches` cell carries the formulaic expansion ("single-word messages expand into conventionalised set phrases"). |
| 177 | `, -7` | `NEW-ScribeSec14Calibration-7` | **S175** | `ScribeSec14Calibration.md` §2 row 7 = TIME 1942 "Science: Drum Telegraphy" reporting Albert Irwin Good (Wayback copy of `time.com/archive/6771186/science-drum-telegraphy/`); Gate line "S175 — … Seat: ScribeSec14Calibration"; `SOURCES.md` row S175, tier B, `mined`. Its row's `teaches` cell: "messages are a code of about a dozen sentences". |
| 179 | `, -12` | `NEW-ScribeSec14Calibration-12` | **S180** | `ScribeSec14Calibration.md` §2 row 12 = Meyer 2017, "The Fascinating Art of Whistled Speech" (CNRS News, `news.cnrs.fr/opinions/the-fascinating-art-of-whistled-speech`); Gate line "S180 — … Seat: ScribeSec14Calibration"; `SOURCES.md` row S180, tier B, `mined`. Its lede: "Unesco has just included a whistled language unique to Turkey on the List of Intangible Cultural Heritage in Need of Urgent Safeguarding." |
| 181 | `, -2` | `NEW-ScribeSec14Calibration-2` | **S157** | `ScribeSec14Calibration.md` §2 row 2 = UNESCO element 00172 (Silbo Gomero); Gate line "S157 — … Seat: ScribeSec14Calibration" with the quote "replicates the islanders' habitual language (Castilian Spanish) with whistling"; `SOURCES.md` row S157, tier B, `mined` (superseded for access notes by S186, which is an access note only). |
| 181 | `, -12` | `NEW-ScribeSec14Calibration-12` | **S180** | same row as line 179 (the survey count whose counting standard the trap names). |

**Cross-check (independent of my derivation).** `corpus/lessons/round-52-verifier-spotcheck.md:73` states that the fragments "map to registered rows (S162, S159, S174, S175, S176, S157, S180) through the committed seat reports". The distinct S-id set my table produces is exactly `{S162, S159, S174, S175, S176, S157, S180}`. The two derivations agree.

**No fragment's S-id is already cited on its own line**, so every fragment is replaced by an S-id and no fragment is dropped. The only removal is the wrong-row citation `S163` on line 113 (§5, and §6 item 1).

---

## 5. Replacement lines, verbatim (ready to paste)

Each block below is the **whole line** as it must stand after the repair. The unchanged parts of each line are byte-identical to the current file.

**Line 106** (S159 for the shepherds quote, S162 for "working their farms"):

```
| Herding and farming at distance | Turkish whistling now survives in "a few words spoken by shepherds" (S159); Banda-Linda drums reach people "working their farms" (S162) | Give the channel a working vocabulary (weather, livestock, harvest) before any elegance; the register link itself is owned by phonetics-phonology.md:197-199 |
```

**Line 107** (S160 for the hunting-accident event, S162 for "lost in the bush"):

```
| Hunting | Drum messages organise "assistance after a hunting accident" and carry instructions when "someone gets lost in the bush" (S160, S162) | Write the emergency set as fixed formulae; a free-text channel fails under panic |
```

**Line 113, option A (recommended — the mobile-phone decline is S159's, and S163 leaves the entry):**

```
The typical failure is a surrogate designed for the wrong distance: built for the village it breaks in the ravine, built for the ravine it dies when the settlement concentrates, as the Turkish whistled language lost its daily function once mobile phones arrived (S159).
```

**Line 113, option B (if the L1 wants S163 to stay in the entry's `used-by`, splitting the clause):**

```
The typical failure is a surrogate designed for the wrong distance: built for the village it breaks in the ravine, built for the ravine it dies when the settlement concentrates, as the Turkish whistled language lost its daily function (S163) once mobile phones arrived (S159).
```

**Line 174** (S179 for the named Yorùbá community, S174 for the instrument spread):

```
| Every tonal-language culture drums its language | R | drum-speech is documented in a small set of named communities and instruments (S179, S174); most tonal languages have none; tone is at most a favourable coding condition — the coupling stays at `phonetics-phonology.md:199-200` |
```

**Line 177** (S179 tone/prosody, S174 instruments, S176 formulaic relay, S175 set-phrase code):

```
| A talking drum is a lossless code | R | the drum encodes tone and prosody, not segments, and adds formulaic redundancy (S179, S174, S176, S175) — say a bounded tone-and-prosody code with set phrases |
```

**Line 179** (S183 for the transmission and inscription, S180 for the 2017 listing):

```
**Living-practice flag.** These are living practices of named communities — Gomeran whistlers on La Gomera (silbo gomero, taught in schools since 1999, S157), the whistled language of the Black Sea region of Türkiye (transmitted parent-child, inscribed 2017 on the Urgent Safeguarding List, S183, S180), Yorùbá dùndún/gángan drummers (S179) — a fictional culture borrows mechanisms, never a community's identity; this lane rules on no heritage or legal question.
```

**Line 181** (S157 for the Silbo register, S180 for the count):

```
**Precision traps.** Whistled speech is a register of a named spoken language, not a second language (S173, S157); audibility is not intelligibility (S175); counts depend on the counting standard (S173, S180).
```

**Cited-id ceiling.** Every id introduced above is an existing registered row (S157, S159, S160, S162, S173, S174, S175, S176, S179, S180). **No S187 or above is used**; the new gesture entry and `corpus/lessons/round-53.md` are not touched.

---

## 6. Re-opened sources (this session, ordinary means only)

Both fetches were plain `curl` requests with an ordinary browser User-Agent from a private sandbox (`/fast/scratch/hyaku/kotodama-r53/ScribeDFragments/`). No headless browser, no captcha solving, no paywall or login bypass; **no challenge was met on either route**, so nothing is reported as "challenge met, not passed".

### S159 — UNESCO nomination form 00658, "Whistled language" (Türkiye), English

- URL: `https://ich.unesco.org/doc/src/36234-EN.doc`
- Route: **Wayback capture** of exactly that URL — `https://web.archive.org/web/2020id_/https://ich.unesco.org/doc/src/36234-EN.doc`
- Receipt: `http=200 size=236544`; `file` reports `Composite Document File V2 Document … Number of Pages: 17, Number of Words: 8824`. Text extracted read-only with `soffice --headless --convert-to txt` (same method the round-52 seat used; the file is a Word 97 binary, so section and paragraph names are cited instead of page numbers, exactly as the seat's own note requires).
- Access date: 2026-10-22.

Carrying passages (verbatim):

1. **"few words spoken by shepherds"** — §D "Geographical location and range of the element", last paragraph: *"It's identified that until 50 years ago, it was being spoken in certain districts, especially in Trabzon, Rize, Ordu, Artvin and Bayburt; although, it has now either disappeared or is limited to a few words spoken by shepherds."* (28 words; the fragment actually quoted by the entry is "a few words spoken by shepherds").
2. **mobile-phone decline** — §2 "Need for urgent safeguarding", paragraph 2: *"One of the most important threats to this element is the increase in the use of mobile phones. Prior to mobile phones, whistled language was being learned from a very early age and was a communication tool commonly used by almost all members of the community. Today, however, it is about to lose its communication function."* The last sentence is the entry's "lost its daily function"; the first is the entry's "once mobile phones arrived". Both are in S159.
3. (context for the row already cited on lines 105 and 109) §1 "Identification and definition of the element": *"The steep mountains and rugged topography of the region have resulted in houses being built that are remote and inaccessible from one another"* (line 105's "remote and inaccessible from one another"), and *"to exchange short dialogues for warning and SOS or calling for help, such as "There is a forest fire!""* (line 109).

### S162 — Cloarec-Heiss, France. 1999, "From Natural Language to Drum Language" (Banda-Linda)

- URL: `https://regroupement-rcms.org/wp-content/uploads/2016/08/Article-F.Cloarec-Heiss.pdf`
- Route: **direct**, no archive needed.
- Receipt: `http=200 size=4410976`; `file` reports `PDF document, version 1.6, 13 page(s)`. Text extracted with `pdftotext -layout`.
- Access date: 2026-10-22.

Carrying passages (verbatim):

1. **"working their farms"** — §2.2.2 "Informative units", paragraph beginning *"Wa a-yi-kindi kindi "oh farmers!"…"* (PDF p. 7; the running footer on that page reads "152 FROM NATURAL LANGUAGE TO DRUM LANGUAGE", i.e. printed p. 152 of the volume): *"indicate messages sent by the village chief to all people who are somewhere outside the village (working their farms, hunting, or gathering)."*
2. **"lost in the bush"** — §2.1.2 "Sociolinguistic circumstances": *"These situations include traditional social events (such as birth, death, inauguration of a chief, inaugural ceremonies for new drums), accidents (e.g., on hunting expeditions or when someone gets lost in the bush)"*.
3. (context for the row already cited on line 111) Introduction, first page (printed p. 145): *"These tones contribute to the 'mysteriousness' of drum language for those who are unacquainted with it"*.

So the round-52 verdict is confirmed by fresh reads, not merely asserted: **"working their farms" is in S162, not S159; the mobile-phone decline is in S159, not S163.**

---

## 7. Findings for the L1 (no lane file was changed by this seat)

1. **Line 113 loses its only S163 citation.** `S163` occurs exactly once in the whole entry — on line 113 (`grep -c S163` → 1). If the L1 takes option A, S163 becomes uncited by this entry, and `corpus/SOURCES.md` row S163 (`used-by` = `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`) must be set to `—`, the same treatment S178 received in round 52. That is a `corpus/SOURCES.md` edit and therefore outside claim D's stated scope ("D lands ONLY that entry"); the L1 must either authorise it or take option B, which keeps S163 cited while attributing the mobile-phone fact to S159 only.
2. **S159's registry anchor label is inaccurate against the document it points at.** The row's `anchor` cell reads *§D "Brief textual description of the nominated element"*, but the opened `.doc` has no such heading (`grep -i 'brief textual'` → no hit). The document's own headings are "D. Geographical location and range of the element", "1. Identification and definition of the element" and "2. Need for urgent safeguarding". The quoted sentences sit in **§1** ("remote and inaccessible from one another"; "warning and SOS … There is a forest fire!"), **§D** ("limited to a few words spoken by shepherds") and **§2** (the mobile-phone paragraph). A registry-anchor correction for S159 is likewise outside D's entry scope; it is reported, not made.
3. **No new row is needed for D's repairs.** All ten fragments resolve to rows that already exist and are `mined` with this entry in `used-by` (S157, S159, S160, S162, S173, S174, S175, S176, S179, S180 — `corpus/SOURCES.md:186-212` region and the round-52 closure's census: "All 49 rows are `mined` with the entry in `used-by`"). Line 104's range was already repaired onto the new S184 row by the round-53 prerequisite; D adds no row and no id above S186.
4. **The provenance gate still does not flag `, -N`.** The round-52 closure routed "Replace all 11 `, -N` draft-id fragments with S-ids, **and teach the provenance gate to flag them**". This seat repairs the fragments only; the gate change is a tool change under `reports/round-53/`, not an entry edit, and is left to the L1 or an executor seat.

---

## 8. Unrun checks and limits

- I did **not** run `python3 -B reports/round-53/d-count.py` or `reports/round-53/accept-c.py`; both are lane gates over the *edited* entry, and this seat did not edit it. The mapping above is the input those gates need.
- I did not run the README sweep (`reports/round-28/readme/sweep.py`); it is unaffected by these repairs (no file added, no index row changed).
- No `corpus/SOURCES.md` row was added, changed or deleted; no `corpus/README.md` row was touched; no lesson file was written except this report.
- The `.doc` for S159 was converted to text with LibreOffice; no page-image verification of the original Word layout was performed, so page numbers are not cited for that row (section and paragraph names are used, as the round-52 seat did).
- `SOURCES.md` cell contents for S157–S186 were read through the `grep` tool with truncation at 512 bytes per line; the fields used here (id, source, kind, tier, `used-by`, status) are visible in those lines, but the long `scope`/`teaches` cells were not read in full.
- Tier judgements are the registry's, not mine; I did not re-litigate them.
- The mapping rests on two independent records (each seat's own id table, and the integrator's Gate lines) that agree row for row, plus the round-52 closure's independent fragment list. No judgment call was needed.

---

## 9. Tooling record

- No installs and no updates. No pacman transaction was run (host-wide pacman pause observed); nothing was installed.
- Tools used, all pre-existing: `curl` (plain requests), `pdftotext` (poppler), `soffice`/LibreOffice (read-only `.doc` → text conversion), `grep`, `file`.
- Scratch copies live only under `/fast/scratch/hyaku/kotodama-r53/ScribeDFragments/` (`S162.pdf`, `S162.txt`, `S159.doc`, `S159.txt`, `S163.html`). Nothing was written into the fleet repo `/home/vgpnk/Projects/shokunin` outside the lane, and nothing was written in the lane except this report.
