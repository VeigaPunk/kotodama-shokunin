# CriticCalibrationBank56: attack on kongo-kingdom.md §1 and §13

Seat: KotodamaR56.CriticCalibrationBank56 (critic, read-only leaf). Target: `corpus/knowledge/civilizations/kongo-kingdom.md` as landed at `767040e` (lines 14-19 and 136-147). The working tree does not change the entry or rows S359-S412: `git diff 767040e -- corpus/SOURCES.md` touches only S292, S293 and S309. Codes are as defined in `corpus/knowledge/verification/calibration-registry.md:35-39`: R rejected, C contested, B bounded, H heuristic, T to-verify. The second opinion is `.ufo/waves/round-56/build/CriticCalibrationKongo.md` (below, "the build critic").

## Verdict

**Not carried as landed.** Of the 14 items checked, 5 are CARRIED, 2 are WRONG-LOCATOR, 2 are OVER-READ, 2 are UNSUPPORTED and 3 are DEFECT. Every failure has a text-only fix inside rows the entry already cites. No new S-id is needed, so C's acceptance legs (RANGE, STATUS, USEDBY) are untouched.

The four findings that matter most:

- **The Afonso R contradicts its own cited source.** The bank line codes "Afonso I tried to abolish the slave trade" as R. But the July 1526 letter, which the entry cites from S359 elsewhere, says Afonso's will was that his kingdoms have no slave trade.
- **The cosmogram C is too broad.** None of the cited rows contests the reading inside Kongo itself, and the only dating is one museum's hedge. So "ancient" is T, not C.
- **"Mostly through hostile priests" has no row.** The wording is the build critic's unregistered Thornton (1998) source, routed through §3, which does not say it. That is false provenance.
- **§1 cites the wrong capture.** It quotes "Kongo peoples" from S400, but that wording is on S395. S395 and S400 are two Wayback captures of the same Met object (2008.30) with different culture and date labels.

Impacted axes: calibration (code fit, and following each code's stop rule), sourced-claim correctness, and provenance (the S395/S400 duplicate; the unregistered wording).

## Checked items

1. `kongo-kingdom.md:16` S400: **WRONG-LOCATOR**.
   - The sentence says "The Met's power-figure records name "Kongo peoples" and a nineteenth-century Chiloango River workshop" and cites (S400, object label, first paragraph).
   - The S400 capture (20251207060528) gives Culture "Kongo" and Geography "Republic of the Congo or Cabinda, Angola, Chiloango River". These are record fields. The words "Kongo peoples" do not appear on that page. Its label's first paragraph reads: "attributed to the atelier of a master active along the coast of Congo and Angola at the end of the nineteenth century".
   - "Kongo peoples, Yombe group" and "Chiloango River region" are on S395's capture 20210208082447 (Culture and Geography fields). That is the same object, accession 2008.30, dated there "19th century" rather than "ca. 1880–1900".
   - Two rows for one object is a duplicate-authority issue for the L1. It is also the strongest evidence for this rule's third sense: the label itself changed between captures. A further counterexample worth adding: Cleveland files a late-1800s to early-1900s crucifix under "Africa, Central Africa, Kongo Kingdom, Kongo-style maker(s)" (S398, culture field). So a museum label that names the kingdom is still the third sense.
   - Replacement (the smallest fix is the two parenthetical citations):

     > The Met's Mangaaka record names "Kongo peoples, Yombe group" and the Chiloango River region (S395, Culture and Geography fields) and an atelier active on the Congo and Angola coast at the end of the nineteenth century, not the kingdom (S400, object label, first paragraph); a later capture of the same record reads only "Kongo" (S400, Culture field), so labels move too. A Cleveland cap is credited to a Kongo-style maker, possibly Yombe (S397, Culture field).

2. `kongo-kingdom.md:16` S397: **CARRIED**. Culture field: "Kongo-style maker, possibly Yombe subgroup" (openaccess-api.clevelandart.org, artwork 159880, HTTP 200).

3. `kongo-kingdom.md:17` S411: **CARRIED**. Brief synthesis, sentence 1: "one of the largest constituted states of Southern Africa, which was active from the 14th to the 19th century".

4. `kongo-kingdom.md:18`, "Most early pages were written by Portuguese officials, Capuchin missionaries and European collectors": **UNSUPPORTED**.
   - No row is cited for this sentence.
   - Counterexample: Thornton (1998), publisher's excerpt, PDF p. 3, which is not a C row: "notably the first half of the sixteenth century, are almost wholly presented in documents written by Kongolese". The S359 volume (1471–1531) is itself largely that Kongolese record.
   - Replacement: "Many early pages were written by Portuguese officials, Capuchin missionaries and European collectors; §3 names each witness's vantage."

5. `kongo-kingdom.md:18` S359 (doc. 142, p. 469): **CARRIED** for "a royal voice". The letter is in the king's first person: "nosso Reyno se vay a perder" (OCR line 19482). Its limit (an archive copy in Portuguese) stays with §3 and the row's scope cell.

6. `kongo-kingdom.md:138`, the registry pointer: **CARRIED**. `calibration-registry.md:35-39` are exactly the R, C, B, H and T rows.

7. `kongo-kingdom.md:140`, "R as aim, B as text: Afonso I tried to abolish the slave trade": **OVER-READ**.
   - The October evidence holds. Doc. 147, p. 489 names three officials, dom Pedro Manipunzo, dom Manuel Manissaba and Gonçalo Pires, "pera veré as ditas peças, se sam catiuos, se forros", and cleared captives may be shipped ("as poderam leuar e embarquar").
   - But the same row's July letter states the aim the bank calls R. Doc. 142, pp. 469-470: "porque nossa vontade hé que nestes Reynos nam aja trato de esprauos nem sayda pera elles". That translates as "our will is that there be no slave trade in these kingdoms, nor any export of slaves". The line cites only October, so "B as text" points at nothing.
   - The S360 sentence's "it" is also off. Vainfas and Mello e Souza describe an undated complaint about nobles "capturados em guerras interprovinciais" ("captured in wars between provinces"). They do not discuss the October inspection rule, and the row itself says "The article does not date the complaint".
   - Replacement:

     > **R as a standing aim, B for the July 1526 request — "Afonso I tried to abolish the slave trade."** In July 1526 he asked that no traders be sent, saying his will was that his kingdoms have no slave trade (S359, doc. 142, pp. 469-470); by October 1526 he sent each sale to three court officials who judged captive or free, and cleared captives could be shipped (S359, doc. 147, p. 489). Vainfas and Mello e Souza read his complaint as a defence of royal control and the royal monopoly in a trade long practised there (S360, section "Conversão e catolização").

   - Also add to S359's quotes: `doc. 142, pp. 469-470: "nossa vontade hé que nestes Reynos nam aja trato de esprauos nem sayda pera elles"`.

8. `kongo-kingdom.md:141`, "C: Kongo Christianity was a thin veneer": **DEFECT**.
   - The code is right, and the cited locator carries the dispute. S383, Extract, para. 1 (Wayback 20260203111247): "Scholarly opinion on the conversion of the Kingdom of Kongo to Christianity has generally been that it was superficial, diplomatically oriented, impure".
   - But the line cites only the two sources against the "veneer" view. That breaks C's stop rule ("do not report one reading as settled"). It also clashes with `kongo-kingdom.md:132`, where DR-KGO-06 lists "veneer" as a failure.
   - S383's own quotes leave out the opposing sentence. The phrase "accepted as the country's religion" is carried: "widely accepted both in Kongo and in Europe as being the religion of the country".
   - Replacement:

     > **C — "Kongo Christianity was a thin veneer."** Thornton names the older scholarly opinion that the conversion was "superficial, diplomatically oriented, impure" and argues instead for an African church accepted as the country's religion (S383, Extract, para. 1); UNESCO says the kingdom adopted Christianity while retaining Kongo custom (S411, Criterion (iii), sentence 3). Keep both readings and date the practice (§8).

   - Add the opposing sentence to S383's quotes, as `Extract, para. 1:` followed by the quote above.
   - Optional, at line 132, the failure cell: ""veneer" or "replacement" stated as settled (§8)".

9. `kongo-kingdom.md:142`, "C: the cosmogram is an ancient universal Kongo symbol": **OVER-READ**.
   - The line points to §9, whose rows carry less than a C for the whole claim:
     - Gundaker (S369) is a proponent of the cosmogram reading. What she disputes is only the "symbol" form: "the dikenga is not a unitary symbol analogous to a Christian cross or national flag" (p. 176).
     - Steen tests only North American cross marks: "There is no direct, unambiguous evidence for their conclusion" (S370, p. 169). His row says it does not test "the existence or meaning of the dikenga in Kongo".
     - The only dating is Cleveland's hedge, "This likely pre-Christian symbol diagrams the life cycle's four points" (S398, Description). The Met's "The Kongo icon, called the Four Moments of the Sun, is a circle around a Roman cross" (S394, essay, third paragraph) gives no date.
   - So "ancient" has no discriminating evidence. It is T, not C. The line also cites no S-id.
   - Replacement:

     > **C for the reading, T for "ancient" — "the cosmogram is an ancient universal Kongo symbol."** Gundaker calls the dikenga "not a unitary symbol" (S369, p. 176), and Steen finds no direct evidence for reading North American cross marks as cosmograms (S370, p. 169); the only dating in an opened row is Cleveland's hedged "likely pre-Christian" (S398, Description) (to-verify). Attribute every reading (§9).

10. `kongo-kingdom.md:143`, "B: Kikongo is one language": **WRONG-LOCATOR**.
    - p. 87 (the abstract) carries "a disparate continuum of closely related Bantu languages" but no subgroups. The subgroups are on p. 146: "The core KLC further fragments into four neat subgroups".
    - Minimal fix: change "(S378, p. 87)" to "(S378, pp. 87, 146)".
    - Code advisory (a tradeoff for the L1, not a defect): as worded, the classification claim is rejected by S378's abstract. B fits only the bounded claim about one named variety. Suggested wording:

      > **R as a classification, B for a named variety — "Kikongo is one language."** A disparate continuum of closely related languages in four subgroups (S378, pp. 87, 146); name the variety, such as the capital variety of the 1624 catechism (S375, p. 76).

11. `kongo-kingdom.md:144`, "R: nkisi = fetish": **CARRIED**.
    - Mack (S403, p. 54, which is PDF p. 3 of the reprint): "an entirely spurious external view which classifies objects regardless of indigenous understanding".
    - Pitt Rivers (S401, What is Mavungu?): "in the past was inadequately glossed as a 'nail fetish'". Also: "makes the term 'fetish' a particularly poor notion" (closing paragraph of that section).
    - The strongest counterexamples are the period glosses themselves: Bentley's "fetish" (S361, p. 383, already in §8), and the line Mack quotes from Fagg, "others are true fetishes" (S403, PDF p. 7), which Mack argues against. Neither supports the equivalence, so R stands.

12. `kongo-kingdom.md:145`, "H: empire": **CARRIED**, with one uncited clause (**DEFECT**, minor).
    - Lopes, p. 42: "though they still retain the titles of all those regions now governed by others". Lopes, p. 43: "This kingdom is divided into six provinces". Both are carried.
    - "UNESCO's 14th–19th-century frame" has no S-id in this line.
    - Two counterexamples support H as a label choice, and neither is cited:
      - Lopes himself writes "the Empire of Monomotapa" (S404, Book II, ch. VIII, about p. 115). For Kongo he writes "kingdom", and he says "formerly the ancestors of this prince ruled over many neighbouring countries" (p. 42).
      - Bentley's 1887 title page: "the Ancient Capital of the Old Kongo Empire" (S361, title page; archive.org OCR head, HTTP 206 range request).
    - Replacement:

      > **H — "empire."** UNESCO's 14th–19th-century frame (S411, Brief synthesis, sentence 1) and Lopes's six provinces support a kingdom with provinces and claimed titles over regions governed by others (S404, Book I, ch. VIII, pp. 42-43); Bentley's 1887 title still calls San Salvador the capital of "the Old Kongo Empire" (S361, title page), so "empire" is a label choice.

13. `kongo-kingdom.md:146`, "R: no writing, so no history": the R code and the S374 and S359 evidence are **CARRIED**. The clause "known mostly through hostile priests (§3)" is **UNSUPPORTED**.
    - §3 (line 45) says only that the Capuchins were "missionaries hostile to the Antonians". None of the 54 C rows contains "mostly" or an equivalent.
    - The wording matches Thornton (1998), excerpt PDF p. 3: "At present, however, we learn of the movement mostly through Italian priests". That source sits only in the build critic's file, as NEW-CriticCalibrationKongo-12. Pointing at §3 for it is false provenance.
    - Replacement:

      > **R — "no writing, so no history."** The 1624 book and the 1526 royal letters exist (S374, title page; S359, doc. 142, p. 469); for the Antonian years the opened accounts are hostile Capuchin relations (§3).

    - Alternative: register the Thornton excerpt as a new row in C's block, but only if the L1 rules that the declared rule "ids of the block C leaves unused stay unassigned" allows a C-owned fix.

14. `kongo-kingdom.md:147`, "T: exact day and place of Kimpa Vita's execution (§8)": **DEFECT**.
    - §8 (line 85) calls the date and place "contested", and its rows disagree with each other. That is C under the registry ("preserve alternatives... discriminating evidence").
    - T's stop rule requires an inline "(to-verify)". The entry has none (searched; zero hits).
    - Discriminating evidence found this session:
      - Gallo, in Barletta's translation (S380): "Then, on Sunday, the first of July, 1706". But 1 July 1706 was a Thursday in the Gregorian calendar, and 12 July Gregorian, the Julian 1 July, was a Monday (computed with Python `datetime`).
      - Batsîkama: "no dia 2 de julho de 1706, numa sexta-feira" ("on 2 July 1706, a Friday"), and 2 July 1706 was a Friday (S392, p. 27, PDF p. 21).
      - So the translated Gallo date and weekday cannot both be right. [INFERENCE: this assumes the Capuchins used the Gregorian calendar; the Italian original (Filesi 1971) was not opened.]
    - Also in §8: the "2 July at Kimbangu" on S392 p. 32 is inside a block quotation credited to Randles 2002 (the row says so). It should read "Batsîkama, quoting Randles".
    - Replacement:

      > **C — exact day and place of Kimpa Vita's execution** (§8): Gallo's translated "Sunday, the first of July, 1706" names a weekday that does not fit that date, while Batsîkama's 2 July falls on the Friday he gives (S380, relatione para. 136; S392, p. 27).

    - Smallest alternative: keep T and add " (to-verify)" after "date and place stay contested" at line 85.

## Disagreements with the build critic (CriticCalibrationKongo.md)

- **Afonso (trap 1).** I agree with the build critic's split: R as a general abolitionist aim, B for the July request. The landed line kept the R but dropped the July letter, which is the build critic's own Attack 1 counterexample.
- **Access route to S359 (provenance; for the L1 to decide).** The build critic declined the archive.org item `monumentamissionariaafricana` as "an in-copyright series uploaded by a user, not treated as an ordinary public copy". S359 is that same item, at tier A. I re-opened it by plain request (HTTP 200, 896,693 bytes, no login, no challenge). So nothing was routed around. Whether a user-uploaded copy of the 1952 edition counts as an "ordinary public copy" under QUALITY criterion 10 is the L1's call. The two seats disagree on it.
- **Cosmogram (trap 3).**
  - I agree with C for the reading and T for any early date.
  - I disagree that the entry can carry R for the word "cosmogram" (a 1970 coinage) or B for the diagram (attested in the nineteenth century "if not before"). Both rest only on MacGaffey (2016, note 21), which is not a C row. Coding them now would give the codes no source. It is a coverage gap, not a defect.
- **Christianity (trap 2).** We agree on C. The build critic quoted the older-opinion sentence; the landed row and line dropped it.
- **Kikongo (trap 4).** We agree the label means a cluster; we both coded B. I now advise an R/B split, because S378's abstract rejects the classification as worded. The build critic used Glottolog where the entry uses S378 and S379; both carry the cluster.
- **Fetish (trap 5).** We agree on R.
- **Empire (trap 6).** We agree H for the word. The build critic's R for "ruling Central Africa" is not needed, because the landed claim is just "empire". The build critic's scholarly-use witness (Hendrickx) is not a C row, but Bentley's title (S361) and Lopes's "Empire of Monomotapa" (S404) carry the same point from existing rows.
- **No writing (trap 8).** We agree on R. The build critic's limit sentence came from Thornton (1998); the entry kept its wording without the row (item 13).
- **Joan of Arc (trap 7).** It is omitted by the entry. That is not a defect, since the bank may choose its traps.
- **Execution T.** It is in the entry only; the build critic has no such trap. I recommend C (item 14).

## Sources re-opened this session (2026-10-22, plain curl, desktop User-Agent; no challenge met)

- **Direct plain requests (HTTP 200)**:
  - archive.org: S359, S404, and the S361 head as a range request (HTTP 206)
  - www2.historia.uff.br: S360
  - biblio.ugent.be: S378
  - vincentbarletta.com: S380
  - revistas.usp.br: S392
  - openaccess-api.clevelandart.org: S397, S398
  - prm.web.ox.ac.uk: S401
  - arthistoriography.wordpress.com: S403
  - whc.unesco.org: S411
  - histarch.illinois.edu: S369, S370
  - assets.cambridge.org: the Thornton (1998) excerpt, used as a counterexample only
- **Wayback captures (HTTP 200)**:
  - S400: 20251207060528id_
  - S395: 20210208082447
  - S383: 20260203111247
  - S394: 20250815185121
- **Pacing**: requests to the same host were spaced 10 s apart.
- **Scratch**: `/fast/scratch/hyaku/kotodama-r56-falsify/CriticCalibrationBank56/`.

## Unrun checks

- S374: the scanned title page (286-page PDF) was not re-opened; I relied on the row's quotes.
- S361, p. 383 and S362 were not re-opened beyond S361's title head.
- Gallo's Italian (Filesi 1971) was not opened, so the weekday mismatch is not traced to Gallo or to the translator.
- S380 paragraph 136: the row's paragraph count was not reproduced; my text split differs.
- MacGaffey (2016) was not re-opened.
- Pigafetta page images: OCR only.
- `python3 -B reports/round-56/accept-c.py` was not run; this seat does not verify.

Installs: none. Tools: curl, pdftotext, python3, and grep/awk on scratch copies only.
