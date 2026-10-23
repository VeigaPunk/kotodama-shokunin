# ReSourceS729

## Axes and behavior

- **Coverage:** Replaced S729's duplicate Farran et al. source with an independent peer-reviewed, open-access study on infant-directed versus adult-directed speech and pragmatic contexts.
- **Calibration:** Tier A is scoped to Neer et al.'s own results; the scope and bullet bound those results to 60 North American English-speaking infants aged 3–20 months.
- **Operability:** Kept the same S729 topic slot and used-by path; added a located body quote and a verified same-page Wayback capture.

Only `.ufo/waves/round-64/rows/ScribeRowS729/row.txt` and this report were changed. No tools were installed.

## Old vs. new ROW

**Old**

```text
ROW: | S729 | Farran, Lee, Yoo & Oller, 2016 "Cross-Cultural Register Differences in Infant-Directed Speech: An Initial Study", PLOS ONE 11(3), e0151518 - https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518 ; capture https://web.archive.org/web/20261002073140id_/https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518 | paper | A | infant-directed speech utterance rates among Lebanese Arabic-speaking mothers compared with American mothers of infants aged 0–24 months | Results, paragraph on utterance rates: "with the Lebanese mothers using more IDS Utterances per Minute across both Registers than the American mothers" | Helps worldbuilders portray Lebanese mothers using more infant-directed speech per minute than the study's American comparison mothers. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md
```

**New**

```text
ROW: | S729 | Neer, Brahmbhatt, Walsh & Warlaumont, 2025, "Pitch characteristics of real-world infant-directed speech vary with pragmatic context, perceived adult gender, and infant gender", PLOS ONE 20(6):e0326569 - https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569 ; capture https://web.archive.org/web/20260617141044id_/https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569 | paper | A | relative frequencies of pragmatic contexts across infant-directed and adult-directed speech in daylong home recordings of 60 North American English-speaking infants aged 3–20 months | Results, Prevalence of pragmatic contexts section, para. 2: "Questions, Imperatives, Reading, Singing, Comfort, and Vocal Play were more frequent in the IDS register compared to the ADS register." | This study reports that home-recorded infant-directed speech included more questions, imperatives, reading, singing, comfort, and vocal play than adult-directed speech. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
```

## Evidence

- The old row matched S718's Farran et al. paper/title and finding; S718 already had the PMC URL for that same paper.
- PLOS identifies Neer et al. (2025), PLOS ONE 20(6):e0326569 as an **Open Access**, **Peer-reviewed**, **Research Article**. Its Results, “Prevalence of pragmatic contexts,” paragraph 2 contains the quoted finding.
- `python3 -B reports/round-61/reopen-quote.py 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569' 'Questions, Imperatives, Reading, Singing, Comfort, and Vocal Play were more frequent in the IDS register compared to the ADS register.'` returned `LOCATED https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569`.
- Wayback availability returned an available same-page capture at `20260617141044`; that archived PLOS article page was opened via `read`. `CAPTURE` and `ACCESS` in the row record it.
- Before editing, a search for the candidate DOI/PMCID/URL found no match in `corpus/SOURCES.md` or staged round-64 rows. Final `check-rows.py` also reported S729 OK, including staged-row URL deduplication.
- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` returned `CHECK-ROWS: 32/32 clean` after the repair.

## Risks and blockers

The replacement supports pragmatic-context frequency in a North American English-speaking home-recording sample; it does **not** support the old cross-cultural Lebanese-versus-American utterance-rate claim. The designated used-by file, `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, was not present when inspected (direct read returned not found and the linguistics directory listing did not include it). The required used-by value was retained; no out-of-scope entry file was created or changed. No implementation blocker remains for this row repair.
