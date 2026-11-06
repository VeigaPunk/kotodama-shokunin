# kotodama round 97 — lesson

Round: kotodama round 97, attempt 1 (L1 KotodamaR97). Base `1ffc5a83d2c70e3bc581594efbcf32c562ba2569`.
Freeze `24eac1e91688d8aa0696a07eff17beeacd407763` (`reports/round-97/claims.json`, counter
`reports/round-97/predispatch.py`, do-nothing control `reports/round-97/predispatch-base.txt` FAIL legs=4/13,
sha-only forgery control `reports/round-97/controls/forgery-sha-only.txt` FAIL legs=5/13, sweep control
`reports/round-97/sweep-control.txt` rc 0). Wave `w1`: 12 seats, one v1 wave.

Claims (frozen in `reports/round-97/claims.json`):

- **O — operability (grader v8 → v9).** Close the seven CriticO96 classes still open on v8 (measured before
  freeze: `reports/round-97/controls/critic96-on-v8.txt`, `CRITIC-O96 survivors=7`): CR1, US1, OGH1, IS1, NUL1
  (verdict-token controls and spaces), CM1, CMW2 (combining marks in headings). Frozen predicate: battery97
  `survivors=0 unnamed=0 refused=31`, selftest ≥154, mutation97 killed == total ≥118 with 0 survived and 0
  broken-pattern, REG lines of reg-v5 byte-identical; both drivers sha-bound to a pin AND to a receipt written at
  their first measurement (round-96 closure routed defect 2).
- **C — coverage (frontier → core).** New entry `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md`
  on a surface with no topic-line or heading owner at base (frozen content sweep, leg C8), plus ≥3 new tier A|B
  registry rows opened 2026-11-05.

## Counter revisions before freeze (no seat had run)

1. The round-96 C1 table counter accumulated data rows across separate tables (`rows` was never reset when a
   table ended). The round-97 counter resets per table, so "a table ≥5 data rows" means one table.
2. The first C8 sweep scanned topic lines, headings and table data rows. Its first base run flagged
   `myth-symbol/trickster.md:25` for the table cell "flyting at Ægir's feast" (owners=1). A table-cell
   mention is not ownership, so the sweep was narrowed to topic lines and headings; the round-96 replay still
   finds 2 owners (`binding-speech-complex.md`, `sacred-kingship-mythic-charter.md`) and the round-97 base 0.
   Both runs were made by the L1 before the freeze commit; the narrowed version is the frozen one.

## Measured before → after (frozen counter `reports/round-97/predispatch.py`)

| leg | base `1ffc5a83` (control) | landed tree (tool v9 `1021dc9d…`) |
|---|---|---|
| O0 tool sha ≠ v8 | FAIL (sha = v8) | PASS |
| O1 selftest | FAIL 147/147 < 154 | PASS 155/155 |
| O2 battery97 | FAIL driver missing (control over v8: survivors=7 unnamed=0 refused=24) | PASS survivors=0 unnamed=0 refused=31, driver = pin = receipt |
| O3 mutation97 | FAIL driver missing (red-before on v8: 111/121, 10 broken-pattern) | PASS 121/121 killed, 0 survived, driver = pin = first receipt |
| O4 REG | FAIL no battery output | PASS 34/34 identical |
| C1 entry | FAIL absent | PASS 36739 B, 13 h2, table 7×6, 6/6 phrases, topic equal |
| C2 registry | FAIL 908 rows, highest S984 | PASS 917 rows, highest S993, 8 qualifying |
| C3 append-only | PASS (guard) | PASS added=9 removed=0 |
| C4 census | PASS (guard) | PASS rc 0 |
| C5 index | PASS (guard, 268) | PASS 269/269/0 |
| C6 ids cited | FAIL | PASS 8/8 |
| C7 captures | FAIL | PASS 8/8 |
| C8 content sweep | PASS (guard, owners 0) | PASS owners 0 of 269 |

Counting command: `python3 -B reports/round-97/predispatch.py --root . --work <scratch> --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569`.
Landed-tree output `reports/round-97/predispatch-lands.txt` (PASS 13/13). The first L1 lands run died in O3 on
host ENOSPC (`/fast` 100%, 256 KiB free, another tenant) and is kept as `predispatch-lands-enospc.txt`; it was
re-run with `--work` on `/home` and passed. ExecGraderV9 and ReviewerO97 each ran the same counter independently:
PASS 13/13. No seat died.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R97-M1 | ownership premise from file names (round-96 claim C "zero owned knowledge file at base") | `.ufo/waves/round-96/w1/stage/ScoutSurface96/surface.md` §1 (filename sweep); `corpus/lessons/round-96-verifier-spotcheck.md` claim C, routed defect 1 (`binding-speech-complex.md` §4 already teaches oath formula anatomy; its topic line carries "self-imprecation") | none — no frozen leg checked content ownership | frozen leg C8 (`sweep_owners` in `reports/round-97/predispatch.py`) and QUALITY criterion 39. Shown able to fail: `python3 -B reports/round-97/sweep-control.py --root .` → `R96-REPLAY … owners=2`, rc 0 (`reports/round-97/sweep-control.txt`) |
| R97-M2 | entry sentence contradicts its own cited source (scribe draft) | `.ufo/waves/round-97/w1/stage/ReviewerC97/review.md` §4 rows 11, 12, 15 and table cells: S986 "carried on for days" (source: "years"), "named office"/"judge inside the contest" (source: the most heartily applauded singer wins), "Polar Eskimos" misattributed, quoted "judgement" absent from the capture (count 0), S990 "next round" (source: "final round") | the frozen counter (C1–C8) checks quote presence by row and id citation, not sentence support; ReviewerC97 and CriticC97 caught it | L1 repair before landing (lines 68, 95, 97, 135, table §8 with *(design)* marks, grounding line S985); every quoted fragment adjacent to an id recounted: 25/25 count 1 after normalising whitespace (L1 recount, see Gate) |
| R97-M3 | frontier sentence contradicts its source (Thrênoi) | ReviewerC97 §4 row F: the added funerary sentence called the Maniat dirge leader a "professional leader" "of Epirus"; S993 says the modern Maniat dirge "holds no association with professional mourners" and places it in Inner Mani | none (outside the frozen counter) | sentence rewritten (`funerary-lament-dirge-formulae.md` line 70) to state the leader-without-profession reading with two located quotes (count 1 each); the new S993 registry row's teaches cell corrected the same way (row added this round, not a base line) |
| R97-M4 | copied boundary prose (duplicate authority on the canon-boundary paragraphs) | CriticC97 F4: 294 shared 8-grams with `oath-blessing-curse-formulae.md`, top span 44 tokens, plus the same invented salt-trading people in the micro-example | none (C8 measures topic and heading ownership, not prose copying) | §1 marking paragraph, §12 limits/calibration/canon/handoff paragraphs and the micro-example rewritten in new words with a different invented people; L1 8-gram recount: 35 of 6181 shared (header boilerplate, the cited slot list and the §12 heading) |
| R97-M5 | manifest file names that do not exist | ReviewerC97 §2: `manifest.json` `captures[].file` named scout keys (`pagliai_2009.txt` …) not the landed `S98x.*` files; C7 passed by id prefix only | C7 matches by id prefix, not by manifest name | manifest repointed by sha256 match to the landed files (30 fields, all resolved) |

Sweep for the R97-M2 class on the round-96 entry (route only): the round-96 closure sampled S983/S978 and agreed;
no sentence-support table exists for `oath-blessing-curse-formulae.md` — routed to round 98.

## Gate

Rows admitted this round (`corpus/SOURCES.md`, appended after S984; opened 2026-11-05 by plain curl `-L
--max-time 30`, default user agent; each quote re-counted by ExecRegistry97 and by ReviewerC97/CriticC97 on the
capture text; QUALITY criterion 38 attempts recorded in `reports/round-97/evidence/manifest.json`):

| id | URL | access | HTTP | tier | located quote (≤25 words) | capture sha256 | attempts |
|---|---|---|---|---|---|---|---|
| S985 | https://journal.oraltradition.org/wp-content/uploads/files/articles/24i/04_24.1.pdf | 2026-11-05 | 200 | A | “A common view of verbal duels posits that they are a cathartic expression of aggression” (15 words; count 1) | `967e3cd4a33b2cc4…` | 1 |
| S986 | https://archive.org/details/in.gov.ignca.2688 | 2026-11-05 | 200 | A | “Among the East Greenlanders song duels may be carried on for” (11 words; count 1) | `d786726a8213030a…` | 2 |
| S987 | https://en.wikisource.org/wiki/The_Poetic_Edda_(tr._Bellows)/Lokasenna | 2026-11-05 | 200 | A | “Then Loki went into the hall, but when they who were there saw who had entered, they were all silent.” (20 words; count 1) | `5f3353dce7d25837…` | 1 |
| S988 | http://www.clanstrachan.org/history/Flyting_of_Dunbar_and_Kennedy.pdf | 2026-11-05 | 200 | B | “The flyting was a verbal competition in which the participants vied in heaping abuse of all sorts on each other, some of it quite gross.” (25 words; count 1) | `aa06f258d8cac7be…` | 1 |
| S989 | https://repo.ignatianum.edu.pl/pl/file_records/866/download | 2026-11-05 | 200 | A | “the Scottish genre of flyting, whose main purpose was to humiliate the opponent” (13 words; count 1) | `3cae64e59e7938ec…` | 1 |
| S990 | https://journal.oraltradition.org/wp-content/uploads/files/articles/22ii/8_garzia3.pdf | 2026-11-05 | 200 | A | “the references to the verbal combats between bertsolaris and the social importance that such ad hoc compositions appeared to have had at the time.” (24 words; count 1) | `01f7f2180616abab…` | 1 |
| S991 | https://ojie.um.edu.my/index.php/SARE/article/download/19055/10299 | 2026-11-05 | 200 | A | “Balagtasan is an indigenous form of competitive Filipino debate poetry in the Tagalog language” (14 words; count 1) | `fab38ff4b650c10b…` | 1 |
| S992 | https://www.gutenberg.org/files/37985/37985-0.txt | 2026-11-05 | 200 | A | “Soon these 'Flytings' (_Naqá’iḍ_) were recited everywhere, and each poet had thousands of enthusiastic partisans who maintained that he was superior to his rival.” (24 words; count 1) | `e356cd7d2e57677d…` | 1 |
| S993 | https://journal.oraltradition.org/wp-content/uploads/files/articles/23ii/07_23.2.pdf | 2026-11-05 | 200 | A | “the antiphonal structure and style of lament performance contribute to social bonding among women; they mourn in a fugue.” (19 words; count 1) | `1e53dabf88057627…` | 1 |

S985–S992 are used-by the new entry (claim C). S993 is the Thrênoi to Moirológia row nominated in round 96
(`ReviewerThrenoi96` §5), written this round with used-by `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`
and cited by one sentence there (frontier curation, outside claim C's counts): **round-95 reject → round-96
nomination → round-97 admit** (status none → `mined`).

Rejected or not admitted (`.ufo/waves/round-97/w1/stage/ScoutSources97/candidates.md`, `ExecRegistry97/dropped.md`):
- Bevan, *The Naqāʾiḍ of Jarīr and al-Farazdaq* (archive.org, HTTP 200): reject, no unique English quote in the
  Arabic OCR; flip: a scan whose OCR carries clean English front matter or a scholarly translation.
- Labov, "Rules for ritual insults" (Springer chapter page, HTTP 200): reject, preview text repeated ≥5× in page
  metadata, no unique span in 11 probes; author self-bibliography HTTP 403 (attempt 1, non-transient). Flip: an
  authorised open copy.
- Seven wall rejects with every attempt recorded (403 ×4 Northwestern bepress, 403 ×4 sacred-texts, 403 UTexas,
  403 SOAS, 403 LSU; JSTOR Dundes interstitial 3038 B; PMC block page 1816 B) — 403 and login shells are
  non-transient under criterion 38.

Quote recount by the L1 after the repairs (every `"…" (Sxxx)` fragment in the entry, every grounding-list quote,
and the two S993 quotes in the funerary sentence): 25 + 15 fragments, 0 with count ≠ 1 on whitespace-normalised
capture text.

## Routed defects of round 96 (from `corpus/lessons/round-96-verifier-spotcheck.md` §5)

1. Content sweep — leg C8 and criterion 39 (above, R97-M1).
2. Mutation driver pin — the round-97 counter binds `mutants97.py` sha to `controls/mutants97.sha256` and to the
   `DRIVER-SHA256` line of `controls/mutation97-first.txt`; same for battery97 (`BATTERY-SHA256` in its v8 control).
3. CriticO96 on v8 — measured before freeze (`controls/critic96-on-v8.txt`, survivors=7); those seven are claim O.
4. Thrênoi row — written (S993), see Gate.
5. Registry rule behind R27: **one registry row per opened document (URL), not per edition.** Two passages of
   one edition served at two URLs are two rows when each is opened and captured separately; two passages of one
   URL are one row whose anchor names both locators. R27 (Manusmriti 8.109) was a different URL from S838 (2.35),
   so "registry duplicate of S838" was the wrong reason: the right check is the URL, and the rule is stated here.
6. v8 docstrings saying "v7" — corrected by ExecGraderV9 (no behaviour change; see its report).
7. Dead reviewer — this round's ReviewerC97 delivered a verdict (§ claim C below).

## Sources census

- Start: `.ufo/waves/round-97/census/census-start.txt`, rc 0.
- End: `.ufo/waves/round-97/census/census-end.txt` (written at landing).
