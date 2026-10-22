# Residual review — claim C, rows S247–S254 (KotodamaR54a2.ReviewRows247to254)

2026-10-22. Canonical object: the committed blob at lane commit `6a658ca4fe9230f70eaa3b421e6c9d78da5c1633` (HEAD when reviewed; worktree carries uncommitted sibling edits — see Drift). Every row S247–S254 re-opened by me by ordinary means (plain `curl`, no browser automation; no challenge met on any of the 11 fetches; S252 answered HTTP 429 once, then HTTP 200 — exactly the behavior its row records). Byte sizes matched the rows' own cells for S247 (589,212), S248 (14,024), S249 (201,497), S251 (88,214). No tool installs (used preinstalled curl, pdftotext, python3); scratch files under `/fast/scratch/hyaku/kotodama-r54-a2/KotodamaR54a2.ReviewRows247to254/`.

The only corpus file citing S247–S254 is `corpus/knowledge/culture-material/masks-masquerade.md` (each row's `used-by` cell agrees); `SOURCES.md` and `lessons/round-54.md` carry the same rows as registry/lesson records, not citations. Entry line numbers below are committed-blob lines; after line 65 the live worktree is one line lower (sibling edit), with identical S-locator text.

## Findings

### S247 — Chen Limin 2020, Nanfeng Nuo (paper, B)

1. **OVER-READ (mild)** — `corpus/knowledge/culture-material/masks-masquerade.md:49`. Row S247 (SOURCES.md:276). Page p. 477: "During the Spring Festival, dozens of Nuo masks are worshipped at the altar. There is a small attic on the altar to store the holy box and props" — worship, altar, attic all carried; the entry's tail "for the rest of the year" is not on the page (it is entailed only by combining the p. 476 calendar). Smallest fix: drop the clause or add "S247, p. 476" as its locator. The same line's second sentence — "hereditary system of the headman, who … is in charge of the main affairs of Nuo troupe" (p. 476) — carries "hereditary Wu-family headman runs the troupe" exactly.
2. **CARRIED** — `masks-masquerade.md:85`. Page p. 476: "From the lunar new year to the 20th day of the first month" (Shiyou) and, same page, "From the first day of the first month to the 19th day of the first month" (Shanggan, sentence ends immediately before the p. 476 footer). "Nineteenth or twentieth day" is a correct synthesis of both villages; both locators on p. 476.

### S248 — China Culture portal, Guichi (docs, B)

3. **WRONG-LOCATOR** — `masks-masquerade.md:49`, locator "(S248, Guichi section, ¶2)". Row S248 (SOURCES.md:277). Page: "A specially designated person arranges the sacred nuo masks in a prescribed manner." is Guichi ¶2 ✓, but "After the performance, the masks are carefully and cautiously counted and placed back into the trunk." is Guichi **¶3** (third paragraph after the section heading). The entry cites ¶2 for both clauses. Smallest fix: "(S248, Guichi section, ¶2–¶3)" or split the locators. Row defect: the row's own anchor cell files the counting quote under "para. 2" as well — same correction needed there (append-only: via a superseding correction, not an in-place anchor edit).

### S249 — Zhang Jiahao 2025, Pingxiang (paper, B)

4. **CARRIED** — `masks-masquerade.md:51` (p. 101). Page p. 101: "When performers don them, they temporarily take on divine agency" and "To practitioners, these symbols are not metaphors but active participants in reshaping cosmic order" — both clauses verified on p. 101; "figures … participants acting on cosmic order" is a fair paraphrase of "symbols … active participants in reshaping cosmic order".
5. **CARRIED** — `masks-masquerade.md:62` (p. 100). Page p. 100: "entire lineage groups were responsible for maintaining Nuo temples, sponsoring festivals, and training performers."
6. **CARRIED** — `masks-masquerade.md:65` (p. 99). Page p. 99, Scope and Limitations: "some sacred rituals were not fully accessible due to restrictions." Printed pages of the PDF run 98–103; all three cited page numbers (99/100/101) verified against the page footers.
7. **CARRIED** — `masks-masquerade.md:87` (p. 101). Page p. 101: "Through the acts of invitation, exorcism, performance, and dismissal, participants symbolically restore balance between humans and the spirit world."

### S250 — Museum of Cultural History, Oslo (docs, A, B sub-scope for ritual summaries)

8. **CARRIED** — `masks-masquerade.md:51`, "(S250, Kōlam Theatre section)". Page, Kōlam Theatre section: "The presence of Garā Yakā is believed to bring success, purification, and prosperity to the humans present."
9. **CARRIED** — `masks-masquerade.md:64`, "(S250, Sanniyäkuma section)". Page, Sanniyäkuma section: "there are only two masked dances in which the dancers reveal their actual face by removing the mask in front of the patient."
10. **CARRIED (locator note)** — `masks-masquerade.md:107`, "(S250, Hagenbeck section)". The "Ethnic Shows"/"Human Zoo" clause is inside the section ("…exhibiting native cultures in 'Ethnic Shows,' the 'Human Zoo,' and the 'Carl Hagenbeck Circus'"), but the sentence the entry leads with — "The presence of many of the earliest Sinhalese ritual dance masks in European collections originated from the business ventures of Carl Hagenbeck." — sits in the collection-overview paragraph immediately **before** the "Hagenbeck in Ceylon" heading. Smallest fix: locator "collection overview, ¶ before 'Hagenbeck in Ceylon'".
11. **CARRIED** — `masks-masquerade.md:142`, "(S250, Sanniyäkuma section)". Page: "Representations of these Yaǩku in masks do not happen in all regional traditions in the same way."

### S251 — Rubin Museum, cham (docs, B)

12. **WRONG-LOCATOR** — `masks-masquerade.md:52`, "(S251, Body, ¶4)". The page has **no "Body" section**. Page, "Watch a Cham Dance", ¶2, last sentence: "the dancers have to be strong and well-trained, as the masks are heavy and the ritual dances must be performed precisely." Content carried; locator names a section that does not exist and a paragraph that does not. Smallest fix: "(S251, Watch a Cham Dance, ¶2)".
13. **WRONG-LOCATOR** — `masks-masquerade.md:62`, "(S251, Body, ¶4)" again. Page, same ¶2, first sentence: "Monks and nuns perform the dance in the central courtyard of a Buddhist community's monastery." Same fix. (The row's own anchor cell says "Watch a Cham Dance section" — the defect is entry-side only.)
14. **CARRIED** — `masks-masquerade.md:90`, "(S251, History)". Page, History section, last sentence: "They are not meant as entertainment, though they are amazing spectacles to observe."

### S252 — Science Museum Group, object A19437 (docs, A)

15. **CARRIED** — `masks-masquerade.md:52`, "(S252, Measurements)". Page, Measurements field: "overall: 210 mm x 155 mm x 100 mm, .28 kg" ("face-sized" is a fair gloss of the dimensions).
16. **CARRIED** — `masks-masquerade.md:107`, "(S252, Category)". Page, Details: "Category: Asian Medicine"; description reads "worn during Sanni Yakuma exorcism ritual", so "a sanni mask" is fair.
17. **CARRIED** — `masks-masquerade.md:144` (calibration use; the record is exactly a holding-museum object record and nothing more).

### S253 — V&A, W.60-1929 (docs, A, hedged identification)

18. **OVER-READ (mild)** — `masks-masquerade.md:53`, "(S253, Materials and techniques; Object history)". Both locators right, and the page does say of this mask: "This mask would have been moulded over a wooden form." — but the record hedges ("would have been"), and the entry asserts "was moulded over a wooden form". Smallest fix: restore the hedge. "Another mask, taken from the same mould, was recorded as being in the Mariano Andreu Collection" (Object history) carries the second clause exactly.
19. **CARRIED** — `masks-masquerade.md:144`. Page, Brief description: "Moulded leather mask … probably the Commedia dell'Arte character Pulcinella." — the "probably" hedge the entry cites is verbatim on the page.

### S254 — U'mista Cultural Society (community, B)

20. **CARRIED** — `masks-masquerade.md:59`, three locators. Page Potlatch page: "The right to wear, use, and display certain regalia and objects that indicate leadership" (PURPOSES list, third sub-item of the second bullet) ✓; "a time for showing the masks and dances owned by the Chief or host giving the potlatch" — it is ¶3 **of the "English Translation of Potlatch Means 'To Give'" section**; the entry's compressed "Potlatch page, ¶3" is correct only under that within-section counting and omits the section name (routing weakness; smallest fix: name the section). "They are witnesses who are 'paid' with gifts for acknowledging a family's inheritance" = CONTEMPORARY POTLATCH ¶1 ✓. Come Home page, "Return of the Collection" ¶3: "Each family decided where their regalia was to be held" ✓ (entry paraphrase "would be held").
21. **CARRIED** — `masks-masquerade.md:106`, "(S254, Our Masks Come Home page, film transcript ¶3)". Page transcript ¶3 (as the page renders it, three paragraphs): "The objects in the Potlatch Collection have been arranged in this big house space, more or less in the order that they would appear in a potlatch, and they're not in cases." Note: the linked 937 B transcript `.txt` is a single block; "¶3" holds only against the page's paragraph rendering.

- **Row defects (S254, SOURCES.md:283), no entry misquotation**: (a) the scope cell carries contradictory tier text — "(tier note: A — …)" followed by "(tier B: community statement filed as kind community…)"; the tier cell B is the correct one per the SOURCES preamble ("community is never A") and QUALITY criterion 6 — smallest fix: superseding row normalizing the note; (b) the anchor cell records no locator for either Come Home quote the entry cites ("¶3", "film transcript ¶3") — both verified by me on the live page, but the anchor cell should carry them.

## Kind and tier cells vs QUALITY.md criterion 6

All eight rows conform; no tier correction row is required. S247/S249 paper-B, S248 docs-B, S251 docs-B (exactly the criterion-6 secondary-description case), S252/S253 docs-A (holding museums on their own objects, with the rows' own notes scoping interpretive text to B, which the entry respects), S254 community-B (community never A). S250 is filed docs-A with an in-cell note scoping ritual summaries to B; every entry sentence citing S250's ritual content is attributive ("states", "records"), so the note does the work — acceptable as filed.

## Drift note

Between my first and second reads a sibling edited the worktree entry (uncommitted): line 53's tail, line 65 "normal"→"possible", and line 85 lost its S267 clause; lines after 65 shift by one. No S247–S254 locator or quoted content differs between the committed blob and the worktree, so all verdicts above hold for both states. Verdicts and line numbers cite the committed blob at `6a658ca`.

## Counts

21 citing locator-items over 8 rows: **CARRIED 16 · OVER-READ 2 (both mild hedge/gloss drops: S247 timing clause, S253 "would have been") · WRONG-LOCATOR 3 (S248 counting clause ¶2→¶3; S251 "Body, ¶4" ×2 — section does not exist) · NOT-OPENED 0.** Row-level defects: 3 (S248 anchor cell repeats the ¶2 error; S254 anchor cell missing two citing locators; S254 scope cell contradictory tier text). All pages opened by ordinary means; no challenge met or passed anywhere.

## Unrun checks

Did not re-run `accept-c.py`, the census, or any acceptance command (attack-only, read-only). Did not verify the S254 Kwak'wala transcripts or the V&A API record beyond the HTML page + API fetch (both 200). Did not follow the sibling's uncommitted edits to their landing. Did not check rows outside S247–S254 or citing lines outside the masks entry (none exist per `used-by` and a corpus-wide grep).
