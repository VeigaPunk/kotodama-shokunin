# CriticClaimC56: falsify claim C as a whole (Kongo entry, rows S359-S412)

Seat: critic (leaf), read-only. Target: `767040e0d8b9f9fe9e69b9a7ab8bc75a93b33b6b`, base `045f458`. Every command below ran in a sandbox clone checked out at `767040e` (`/fast/scratch/hyaku/kotodama-r56-falsify/CriticClaimC56/lane`), from the lane root, with `E=corpus/knowledge/civilizations/kongo-kingdom.md`. Axes: coverage and calibration. No installs. No git or jj writes in the lane.

Note: while this seat ran, the lane worktree copy of the entry changed. The L1 is editing §14 (the handoff) and has not committed it. Every verdict below is on the `767040e` blob. The two F12/F14 lines marked "worktree" were re-run on the edited copy, for information only.

## Verdict

- **The 231 -> 232 count is not hollow.** `accept-c.py` exits 0 with all seven legs passing. Every one of the 54 cited S-ids appears in the body, the header cites none, and 37 of the 54 are cited two or more times. The entry is 170 lines in 16 sections, and the only file C touches under `corpus/knowledge` is the entry itself. Even with the rows that are not about the kingdom set aside (diaspora, museum and late-Kongo-peoples rows), more than 30 kingdom-period rows remain, so FLOOR's 20 does not depend on padding. **Coverage is carried.**
- **Calibration has fixable defects. None of them is a tradeoff the judge must reject.**
  - F12 fails: four of the eight required one-way pointers are missing. The worst case is the diaspora bullet, which is headed "One-way pointer" but points to no file.
  - Five sentences over-read their rows. One is a founder "line" that turns a father-in-law into an ancestor. One is a heading that asserts an absence the source calls unknown. Two put late-nineteenth-century museum objects into kingdom-era sections without their dates or place. One draws a general rule from a single compound word.
  - One museum sentence on a belief has no stated speaker.
  - Six of the twelve era rows record political events only. The section is not dates-only: it has a "What changes" column. But half its rows decide nothing about language, titles, objects or naming.
  - One date (1665) is presented as settled although a cited row disagrees with it.
  - One handoff locator is wrong. The L1's uncommitted worktree edit already replaces it.
- **Must-not list.**
  - No citations sit only in the header.
  - The era section is not dates-only, but it is partly a chronicle (finding E1).
  - Museum and dictionary material is counted as kingdom material in two sentences (findings M1 and M2). The dictionary material is witness-tagged.
  - No publisher page is used for a belief without attribution. One museum essay is cited for a belief in a passive sentence that names no speaker (finding M3).
  - C made no edits to neighbouring files.

## Falsifiers F1-F18 (from `.ufo/waves/round-56/build/CriticGapPremise56.md:160-248`)

| # | Command (abridged) | Output | Verdict |
|---|---|---|---|
| F1 header-only | `python3 -B -c "...set(header S-ids)-set(body S-ids)"` | `[]`; header S-ids `[]` | CARRIED |
| F2 thin carry | count body S-ids cited exactly once | `distinct 54 once 17` (S363, S367, S368, S370, S372, S373, S379, S388, S395, S396, S398, S399, S405-S409) | CARRIED (17 of 54, under half) |
| F3 size and shape | `wc -l`; `grep -c '^## '`; `awk 'length>600'` | `170`; `16`; `4` (lines 8: 775, 85: 807, 97: 645, 99: 699 characters) | CARRIED; four long lines reported, none hides length (170 is well under 230) |
| F4 unit tag | `grep -niE 'nkisi\|minkisi\|nkondi\|mangaaka\|...\|Chiloango' $E` | 17 hits; §9 closes with "nineteenth-century objects of Kongo peoples, not kingdom-era court objects" (`:91`) | CARRIED for §9. The cap sentence `:97` misses the filter (finding M1) |
| F5 witness tag | `grep -niE 'Brusciotto\|Doutrina\|Cardoso\|Bentley\|Laman\|...' $E` | 8 hits; each names its witness, and each has a date in §3 or on the line | CARRIED. The italic title forms at `:61` carry no witness or date (finding W1) |
| F6 Kituba | `grep -niE 'Kituba\|Munukutuba\|ya leta' $E` | no output (rc=1) | CARRIED (no merger possible) |
| F7 cosmogram | `grep -niE 'cosmogram\|dikenga\|yowa\|...' $E` | `:92` attributes each reading (Gundaker, Steen, Cleveland, Met); `:142` codes it C; pointer `direction-symbolism.md` at `:8` | CARRIED |
| F8 living practice | `grep 'Bundu dia\|BDK\|Ne Muanda Nsemi'`; `grep Kimbangu`; `grep 'today\|present-day\|nganga\|Palo\|Vodou...'` | none; 2 Kimbangu hits (`:19` scope exclusion; `:85` the place Kimbangu, not the church); 5 hits, all scope lines or attributed scholarship, no procedure | CARRIED. `:85` spells the place "Kimbangu" but `:113` spells it "Kibangu" (S392 p. 24 prints "Kimbângu"); one spelling with the variant noted would avoid a false Kimbanguism hit |
| F9 exoticizing words | `grep -niE 'fetish\|idol\|...\|empire' $E` | 6 hits: `:83` (Bentley's gloss, flagged as missionary choice), `:89`, `:133`, `:144` (quoted and negated), `:90` ("banganga", which matched `nganga`), `:145` ("empire" quoted, coded H) | CARRIED |
| F10 era endpoint | `grep -niE '1884\|1885\|Berlin\|partition' $E` | `:117` "does not itself partition Africa"; table header `What changes`; era runs to 1914 and the 1923 titular king | CARRIED; the partition is not given as the end |
| F11 founding hedge | `grep -niE 'Lukeni\|Nimi\|found(ed\|ing\|er)\|origin' $E` | `:108` hedged ("later constitutional statements"); `:63` "The founder's line is given as..." | OVER-READ at `:63` (finding T1) |
| F12 pointers | `grep -c` for each of 8 owners | africa-primary-sources 3; language-contact 3; **sacred-kingship 0**; direction or cosmology 1; **real-world-inspiration-boundaries 0**; worldbible-contract 4; **glossary-registry or sacred-registers 0**; **fon-dahomey 0** (worktree: the same four are still 0) | **DEFECT** (finding P1) |
| F13 restatement | three `grep \| grep -v` pipelines | no output | CARRIED |
| F14 handoff | §14 has the contract (3 hits) and "real-world reference" (1); `grep "kind: ...\|as a faction..."` | prints `:151` "...so a real polity never enters as a faction or place..." | CARRIED in substance: the hit is a negation, so this is a false positive of the command. Locator defect H1 |
| F15 old keys | `grep -nE 'KTD-S-\|\[(CO\|CARE\|AJ\|RAI\|BEN)\]\|\[S[0-9]{1,3}\]' $E` | no output | CARRIED |
| F16 neighbour edits | `git diff --name-only 045f458..767040e -- corpus/knowledge` | only `corpus/knowledge/civilizations/kongo-kingdom.md`; `git diff --numstat 7576fd4..767040e`: README 12/3, SOURCES 54/0, entry 170/0 | CARRIED. SOURCES is append-only. No S413-S418 row exists at the commit, in the worktree SOURCES or in the lesson, so the export rule holds. The worktree edits to `masks-masquerade.md` and `motif-index-usage.md` are uncommitted records items that mention no Kongo material |
| F17 tier honesty | sentences citing tier-B or museum and exhibition rows, read against the rows | S383 `:82`, `:141` "Thornton argues" (carried); S394 `:82` "The Met's essay says" (carried); S409 `:99` (carried); S395 `:90` passive (finding M3) | one DEFECT |
| F18 author-year | regex, then a check of each hit line for an S-id in the block | 10 hits (`:44 :45 :55 :82 :85 :98 :111 :118 :140 :146`), all `in-block-S-id`; no unregistered author-year | CARRIED |

Acceptance re-run at `767040e`: `SET PASS count=232 ... removed=[]`, `SWEEP PASS ... rows 232 files 232 missing_from_index 0`, `FLOOR PASS cited=54`, `RANGE PASS bad=[] range_notation=[]`, `STATUS PASS`, `USEDBY PASS`, `ACCESS PASS exit=0`, then `accept-c exit=0`. The script also prints a non-failing `SyntaxWarning: "\|" is an invalid escape sequence` from `reports/round-56/accept-c.py:18`, which is a docstring cosmetic. Base check: `git grep -il kongo 045f458 -- corpus/knowledge` returns only `linguistics/language-contact.md`, matching the entry's `:4`.

## Findings (one line per item; quotes are at most 25 words)

- **T1 `kongo-kingdom.md:63`, S390. OVER-READ.**
  - What the source says: Cavazzi's 1687 report, as the authors give it, names Nsaku Lau as the *father of the bride*, so he is not in the line of descent. "Founder" is also hedged in the source.
  - Quote: "the descendants of Nsaku Lau, father of the bride of Nimi a Nzima, himself father of Lukeni lua Nimi or Ntinu Wene, who is traditionally seen as the founder" (S390, PDF text p. 73).
  - p. 74 adds: "It is not unimaginable that Lukeni lua Nimi was not the founder of the Kongo kingdom itself".
  - Replacement: "Cavazzi (1687), as Bostoen and colleagues report it, makes Nsaku Lau the father of the bride of Nimi a Nzima, whose son Lukeni lua Nimi, also called Ntinu Wene, is traditionally seen as the founder of Kongo (S390, p. 73)."
- **S1 `kongo-kingdom.md:72`, S412 p. 36. OVER-READ.** The heading asserts an absence, but the source says the matter is unknown.
  - Quote, located at printed p. 36 (PDF page 4): "it is not even known whether slaves were brought to Mbanza Kongo or whether they were collected elsewhere in the Kingdom".
  - Replace `**No slave yard at the palace.**` with `**Slave trade at the capital unknown.**`. The rest of the line is carried.
- **M1 `kongo-kingdom.md:97`, S397. OVER-READ (museum material staged as kingdom material).**
  - The record was re-opened through the open-access API (HTTP 200). Date "late 1800s–early 1900s"; culture "Kongo-style maker, possibly Yombe subgroup".
  - Quote: "Known since at least 1607 in the former Loango Kingdom, as well as the adjacent Kongo Kingdom".
  - The entry drops Loango and the object's date, inside a bullet about Christian nobility of about 1500-1800.
  - Replacement for the Cleveland sentence: "Cleveland's late-1800s cap, by a Kongo-style maker possibly of the Yombe subgroup, gives *mpu*, plural *zimpu*, and *mpu ngola* for the long high-status cap; the museum says such caps are known since at least 1607 in the Loango Kingdom and the adjacent Kongo Kingdom (S397, Description)."
- **M2 `kongo-kingdom.md:84`, S399. OVER-READ (unit and office).**
  - The row's anchor gives one 19th-century staff "used as an insignia of office by a Kongo chief".
  - The entry generalizes it to all staffs and files them under Church offices.
  - Replacement: "A nineteenth-century Met staff topped by a brass Saint Anthony of Padua was used as an insignia of office by a Kongo chief, uniting religious and secular power (S399, Overview label, object 318318)."
- **M3 `kongo-kingdom.md:90`, S395. DEFECT (F17: the belief has no speaker).** "Mangaaka is described as..." does not say who describes it.
  - Replacement: "The Met's essay identifies the figure with Mangaaka, the preeminent force of jurisprudence, and reads its metals as records of vows sealed and treaties signed (S395, essay, first and second paragraphs)."
- **L1 `kongo-kingdom.md:57`, S361. OVER-READ.** The rule ": rank is built by compounding" is drawn from one compound; the row anchors only the two glosses ("free man, nobleman, gentleman"; "queen, chief- tainess, lady").
  - Replacement: delete ": rank is built by compounding", so the sentence ends "...*mfumu ankento* as queen, lady (S361, pp. 348-349)."
- **W1 `kongo-kingdom.md:61`, S390 and S410. DEFECT (must-not 2: every form carries its witness).** The italic royal titles carry no witness and no date.
  - Replacement opening: "In Bostoen and colleagues' 2013 reading, *Ngangula a Kongo*, 'blacksmith of Kongo', co-existed with *ntinu* and *ntotila* (S390, p. 55). Thornton (2025) writes that higher political orders were called *wene*..."
- **P1 F12. DEFECT.** Four owners get no pointer:
  - `sacred-kingship-mythic-charter.md`. The entry covers election (§5) and lost regalia (§10), but row 4 at `:66` and row 8 at `:70` own those channels.
  - `real-world-inspiration-boundaries.md:97,107`. The entry has an out-of-scope line at `:19` but cites no rule.
  - `glossary-registry-format.md:222`. The §3 witness table needs its bias-notes owner.
  - `fon-dahomey.md:65`. The bullet at `:93` is headed "One-way pointer to the diaspora" but points to no file.
  - Smallest correction, three new rows in the §2 table:
    - `myth-symbol/sacred-kingship-mythic-charter.md:66,70` | Election and regalia as legitimation channels | Kongo's electors and regalia as dated instances (§5, §10); no new typology
    - `verification/real-world-inspiration-boundaries.md:97,107` | Restricted and unknown-status sacred material | Minkisi procedures and living practice withheld (§1, §9)
    - `synthesis/glossary-registry-format.md:222` | Bias notes for missionary grammars and museum labels | The §3 witness table
  - Then append to `:93`: "Diaspora traditions are historically connected but separately developed, not a survival manual for kingdom religion (`civilizations/fon-dahomey.md:65`)."
- **E1 `kongo-kingdom.md:109-114,117`, era table. OVER-READ of the hollow test (calibration).** Six of twelve rows are political events with no language, title, object or naming consequence: 1482-1491, 1506-1543, 1665, 1667-1709, 1709-1715 and 1884-1885. Smallest correction, using only rows and pages the entry already cites:
  - 1665: append "; the European-style crown is lost, and Pedro IV is crowned in 1696 with a hat bearing the royal arms" and add `S384 (p. 23)` to the Rows cell.
  - 1667-1709: append "; kings are proclaimed or elected by their supporters at Bula or Kibangu, so a royal title needs its seat", with S392 p. 24 already cited.
  - 1482-1491: append "; from the baptism each king carries a Kikongo name and a baptismal name" and add `S371 (p. 175)`.
- **D1 `kongo-kingdom.md:112`, S391 and S392. DEFECT (a contested date given as settled).**
  - The row gives "29 October". But S392, which the entry cites, gives the first clash as "por volta das 9 horas de 27 de Outubro de 1665" (p. 19).
  - Replacement cell: "battle at Ulanga near Ambuila, 29 October in Randles (Batsîkama dates the first clash 27 October); the nobility destroyed". Add `S392 (p. 19)` to Rows. Add 1665 to the disputed dates listed in §15.
- **B1 `kongo-kingdom.md:115`, S362. Calibration DEFECT.** The row's tier note says the currency dates "are his own testimony and are not corroborated by a second source here". The era row states them without attribution.
  - Replacement opening: "by Bentley's 1895 account, currency moves from palm-cloth mats to red glass beads (about 1830)..."
- **H1 `kongo-kingdom.md:155`, handoff. WRONG-LOCATOR.** The entry cites `check_bible.py:27,156-161` for "lore selects fictional names". Lines 156-161 check that each claim has a `statement` and `source_id`: "expected nonempty statement and source_id" (`lore-shokunin/corpus/fixtures/check_bible.py:159`).
  - The L1's uncommitted worktree edit already changes this to `check_bible.py:27; lore-shokunin/PROVINCE.md:28`. Carry that edit.
  - The other handoff anchors were re-read and carry their use: `check_bible.py:7`, `:27-30`; `PROVINCE.md:3,9,28`; `reference-ledger.md:3,10-12`; contract `:43,96,103,167`.
- **CARRIED spot checks (re-opened by plain request):**
  - S412 `:82`: "Nzinga Nkuwu converted to Catholicism in 1491, taking the name of Joao I, while maintaining traditional religious" (ICOMOS p. 35).
  - S366 `:118`, regalia to Luanda: "devendo as chamadas Regalias do Trono ser enviadas para Loanda" (p. 94 n. 209).
  - S393 `:99`: "diplomatic missives sent by Kongo sovereigns to their European counterparts ... raffia cloths" (exhibition text, second paragraph; Wayback 20150728085134).
  - In-lane anchors of the §2 table (12 of 12) and `calibration-registry.md:35-39` (codes R, C, B, H, T) were re-read at `045f458` and exist as cited.
- **Header `kongo-kingdom.md:7`, "numbers 359 to 418". CARRIED.** This describes the reserved block in words, not an S-id range, so RANGE's no-range rule is not evaded.

## Impacted axes and the hollowness judgment

- **Coverage: not hollow.**
  - 54 rows are used in the body. FLOOR's 20 is met by kingdom-period rows alone, including the language, title, church, regalia, chronology and capital rows (S359-S364, S371-S375, S378, S380-S384, S386-S392, S404, S410-S412).
  - Rows that are not about the kingdom are each scoped in their sentences: S408 as Lele and Babunda "not Kongo", S369 and S370 as North American archaeology, S385 as Cuba, S377 as 20th-21st-century Luanda, and S393-S402 as 19th-century Kongo-peoples objects (`:91`).
  - The two exceptions are M1 and M2.
- **Calibration: impacted** by T1, S1, M1, M2, M3, L1, W1, D1, B1, E1 and P1. Each has a sentence-level fix above, and none needs a new source row or changes the count.

## Unrun or unopened

- **S364 was not re-opened as HTML.** `journals.openedition.org/cea/2225` returned an Anubis proof-of-work challenge page. The challenge was met, not passed, and was not routed around. The Glasgow PDF (HTTP 200) has a text layer with missing digit glyphs, so its section numbers (§7, §22, §32) could not be checked. The regalia clause is carried by S366 instead.
- **Row-by-row checks of all 54 rows are not mine.** Those belong to the ReviewRows seats. I opened only S390, S412, S364, S366, S397 and S393, for the structural findings above.
- **No mutation of `accept-c.py`.** That belongs to the RerunAcceptC56 and RerunControls56 seats.
