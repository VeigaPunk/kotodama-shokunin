# Falsify round 56 — review rows S368–S370 (seat ReviewRowsS368toS370)

Verdict: NO DEFECT FOUND. All three rows re-opened by plain request this session (2026-10-22); every anchor quote and every Gate quote is verbatim on the reopened page, 25 words or fewer, at the stated locator; each Gate Grounds is byte-equal to its row's teaches cell; tiers fit QUALITY.md:29 (criterion 6) for each row's scope; both entry sentences citing these rows are carried at the strength stated. No fix required; no replacement text proposed.

Re-open record (ordinary means only): Springer chapter fetched with curl, 303 to the standard no-cookie URL then HTTP 200, text/html, 497,811 bytes, no challenge; both Illinois PDFs fetched by plain GET, HTTP 200, application/pdf, byte counts 314,251 and 323,457, exactly as the rows record. Text extracted with system pdftotext; no tools installed (system curl, pdftotext, python3 already present).

## Checked items

- corpus/SOURCES.md:397 (S368 anchor 1) — CARRIED. Section 2.5 ("The Berlin Conference of 1884-1885 and the First Partition") contains verbatim: "The Berlin Conference essentially consisted of a series of negotiations starting on 15 November 1884" (15 words).
- corpus/SOURCES.md:397 (S368 anchor 2) — CARRIED. Section 2.5 contains verbatim: "The final acts of the conference were agreed on 26 February 1885" (12 words).
- corpus/SOURCES.md:397 (S368 anchor 3) — CARRIED. Section 2.5 contains verbatim, with the curly quotes: "Africa was not ‘partitioned’ there, although various, previously concluded, bilateral agreements were ratified in Berlin" (15 words).
- corpus/SOURCES.md:397 (S368 anchor 4) — CARRIED. Section 2.5 contains verbatim: "The Acts of the Berlin Conference did not include an article about Leopold, the AIC or about the Congo Free State" (21 words).
- corpus/lessons/round-56.md:14 (S368 Gate quote) — CARRIED. Verbatim in section 2.5, 15 words, locator §2.5 correct.
- corpus/lessons/round-56.md:14 (S368 Gate Grounds) — CARRIED. Byte-equal to the row's teaches cell ("Berlin set rules and dates, not a map: ... not one decree.").
- corpus/SOURCES.md:397 (S368 tier B) — CARRIED. Open-access peer-reviewed survey chapter; tier definitions list "survey" under B (strong secondary); criterion 6 reserves A for primary or scope-authoritative sources; the row's own tier note states the scope limit.
- corpus/knowledge/civilizations/kongo-kingdom.md:117 (S368 leg) — CARRIED. Section 2.5 carries "the Berlin conference ratifies agreements made elsewhere and does not itself partition Africa" via anchors 3 and 4 above; the after-1885 clause of that cell cites S367, not this row.
- corpus/SOURCES.md:397 (S368 access cell) — CARRIED. Reopened by plain request, no challenge; row records HTTP 200 text/html full open-access chapter, which matches the observed final response.
- corpus/SOURCES.md:398 (S369 anchors, p. 176 quotes) — CARRIED. Printed page validated by running head "176 Grey Gundaker" on PDF page 2: "The sign is thus the tip of a philosophical iceberg" (10 words) and "above and below the Kalunga waters" (6 words) verbatim, same paragraph.
- corpus/SOURCES.md:398 (S369 anchor, p. 178 quote) — CARRIED. Running head "178 HISTORICAL ARCHAEOLOGY 45(2)" on PDF page 4; verbatim: "The “simpler” cross-mark form of the dikenga, the yowa, figures in initiation and badges of membership in the Lemba therapeutic association" (21 words), in the yowa paragraph.
- corpus/lessons/round-56.md:15 (S369 Gate quote and locator) — CARRIED. Quote verbatim on printed p. 176, and the heading "Finding Cosmograms" precedes it on that page, so "p. 176, section 'Finding Cosmograms'" is exact.
- corpus/lessons/round-56.md:15 (S369 Gate Grounds) — CARRIED. Byte-equal to the row's teaches cell.
- corpus/SOURCES.md:398 (S369 tier A) — CARRIED. Original peer-reviewed article in an SHA-authorized copy, authoritative for how the cosmogram is used in historical archaeology, the row's declared scope; not cited for Kikongo meanings or Kongo political history.
- corpus/knowledge/civilizations/kongo-kingdom.md:92 (S369 sentence) — CARRIED. Page 176 carries "all map complex, dynamic, relational systems of knowledge" and "the dikenga is not a unitary symbol analogous to a Christian cross or national flag"; page 178 carries the yowa-as-simpler-cross-mark claim. Paraphrase stays inside the source; no over-read.
- corpus/SOURCES.md:399 (S370 anchors, p. 169 quotes) — CARRIED. All three verbatim in the paragraph naming Joseph and Ferguson: the "no direct, unambiguous evidence" sentence (17 words), "That does not mean it is not true, but at this stage it is simply an idea, a theory" (19 words), and "The evidence they have marshaled is always prefaced by “maybe,” “might be,” and “could be”" (15 words).
- corpus/SOURCES.md:399 (S370 anchor, p. 170 quote) — CARRIED. "Secret meanings cannot be recovered, this writer would argue." (9 words) verbatim in the paragraph on the B. F. Landrum and John Landrum sites.
- corpus/lessons/round-56.md:16 (S370 Gate quote and locator) — CARRIED. Quote verbatim, 17 words, printed p. 169, inside the Joseph and Ferguson paragraph, exactly as the locator states.
- corpus/lessons/round-56.md:16 (S370 Gate Grounds) — CARRIED. Byte-equal to the row's teaches cell, including "Steen calls the attribution a theory, not a finding", which page 169 supports ("simply an idea, a theory").
- corpus/SOURCES.md:399 (S370 tier A) — CARRIED. Original peer-reviewed article, SHA-authorized copy, authoritative for the critique of cross-mark attribution in the United States South, the row's declared scope.
- corpus/knowledge/civilizations/kongo-kingdom.md:92 (S370 sentence) — CARRIED. The quoted fragment is verbatim on p. 169; "North American cross marks" matches Steen's own frame: p. 166 calls the reading "a sign of a secret, undocumented (in North America), African belief system", and p. 169 generalizes past the two named authors ("Archaeologists will never know"), with p. 170's "Secret meanings cannot be recovered". No over-read at the stated strength.
- corpus/SOURCES.md:398-399 (page-map and cover-page cells) — CARRIED. Gundaker: 9 PDF pages, cover on PDF page 1, printed 176 to 179 on PDF pages 2 to 5, confirmed by running heads. Steen: 11 PDF pages, cover on PDF page 1, printed 168 to 170 on PDF pages 4 to 6, confirmed by running heads.
- corpus/SOURCES.md:397-399 (status and used-by cells) — CARRIED. All three rows are mined with used-by naming the entry, consistent with the entry's citations found at kongo-kingdom.md lines 92 and 117 and nowhere else.

## Not run (out of my slice)

- No mutation testing of tools/check-gate-quotes.py or any claim-O instrument (claim O has its own seats; my assignment is the three rows).
- Did not run reports/round-56/accept-c.py, tools/check-source-access.py or the sweep (claim-level legs; other seats cover them).
- Other cited rows in entry lines 92 and 117 (S367, S385, S393, S394, S398, S402) belong to sibling seats.
