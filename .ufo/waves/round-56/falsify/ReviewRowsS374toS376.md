# Falsify review: claim C rows S374, S375, S376

## Verdict

Rows S374 and S375 CARRIED in full: every anchor quote and every Gate-line
quote is verbatim on the opened page at the stated locator, the tiers fit
QUALITY criterion 6, the entry sentences that cite them are carried at the
stated strength, and each Gate Grounds equals the row's teaches cell.

Row S376's quotes are verbatim but its page locators are systematically off
by one in the SOURCES row, in the lesson Gate line, and in the entry's three
citations (S376 items are on PDF/print pages 9, 10, 12, not 10, 11, 13).
One further transcription typo in the S374 SOURCES row imprint quote
("Geralda" should read "Geraldo"). Both need the replacement text below.

## Checked items

### S374 (Doutrina Christãa, 1624, BNP RES-268-V scan PDF)

- S374 Gate quote, lessons/round-56.md:20: CARRIED. Verbatim on scan PDF
  p. 5, 16 words: "De nouo traduzida na lingoa do Reyno de Congo, por ordem
  do P. Mattheus Cardoso Theologo". Locator "title page (scan PDF p. 5)"
  confirmed by pdfinfo (286 pages) and pdftotext -f 5 -l 5; glyph reading
  via rendered title-page image confirms "Reyno" and "Cardoso" (the PDF's
  embedded OCR text garbles them to "Rcyno"/"Cardolb", a scan artifact, not
  the printed text).
- S374 anchor quote 2, SOURCES.md:403: CARRIED. Verbatim on scan PDF p. 5,
  13 words: "Ao muito poderoso, & catholico Rey de Congo dom Pedro Affonso
  segundo deste nome." Same page and glyph check.
- S374 anchor quote 3 (imprint), SOURCES.md:403: DEFECT (transcription typo
  in the row). The printed title page reads "LISBOA. Por Geraldo da Vinha.
  1624." (image-verified: round "o" in Geraldo, dotted i in Vinha); the row
  quotes "LISBOA. Por Geralda da Vinha. 1624." Replacement: "Por Geralda da
  Vinha" -> "Por Geraldo da Vinha". The entry's shelf table (kongo-kingdom.md
  :44) already writes "Geraldo da Vinha" correctly.
- S374 tier: CARRIED. Tier A (the printed book itself, authoritative for its
  own title page, imprint and stated credits) fits criterion 6; the row's
  scope limits it to title-page facts and the entry stays within that scope.
- S374 Grounds = teaches: CARRIED. Lesson Gate Grounds text equals the row's
  teaches cell verbatim.
- S374 entry sentences (kongo-kingdom.md :44, :55, :111, :146): CARRIED.
  Title page carries: credit chain (Composta pelo P. Marcos Iorge,
  Acrescentada pelo Padre Ignacio Martinz), translation by order of Mateus
  Cardoso, royal addressee dom Pedro Affonso segundo, and the Lisbon 1624
  imprint. The entry's "dedicated to King Pedro Afonso II" is carried by
  "dom Pedro Affonso segundo deste nome"; "names its target only as the
  lingoa do Reyno de Congo" is carried (no other language is named on the
  title page).

### S375 (Bostoen & de Schryver 2018, The Kongo Kingdom, pp. 60-102)

- S375 Gate quote, lessons/round-56.md:21: CARRIED. Verbatim on print page
  60, 16 words: "an interlinear Portuguese–Kikongo catechism from 1624
  translated under the leadership of the Portuguese Jesuit Mateus Cardoso".
  The Ghent PDF is the full book file; the chapter occupies extract pages
  1-43 (folios 60-102), and locators are extract page + 59.
- S375 anchor quotes, SOURCES.md:404: all three CARRIED verbatim at their
  stated locators. p. 60: "they are also the earliest (surviving) book-length
  sources ever written in a Bantu language" (17 words). p. 76: "most likely
  represent the variety that was spoken in the kingdom's capital at that
  time" (15 words). p. 100: "The Kikongo found in the Doutrina Christãa
  (1624), the Vocabularium Congense (1652) and the Regulae quaedam (1659)
  is thus not ancestral to the entire KLC" (24 words). All within 25 words.
- S375 tier: CARRIED. Tier A (peer-reviewed research chapter by the
  KongoKing historical linguists) fits criterion 6 for the exact scope; the
  row's scope and limits are respected by the entry.
- S375 Grounds = teaches: CARRIED. Identical text in lesson Gate and row
  teaches cell.
- S375 entry sentences (kongo-kingdom.md :44, :55, :56): CARRIED. The
  p. 60 abstract supports "only three surviving seventeenth-century Kikongo
  works" and "earliest book-length sources in a Bantu language"; p. 76
  supports the court-variety placement; p. 100 supports "not ancestral to the
  whole cluster"; p. 77 supports "the chapter cautions that the spelling
  variation behind the Soyo reading is not systematic" (exact wording on
  p. 77: "the use of <r> in front of i is systematic in neither Van Gheel
  (1652) (VG) nor Brusciotto (1659) (Br)"). The hedges are kept.

### S376 (MacGaffey 2003, symposium paper, 15 pages)

- S376 Gate quote, lessons/round-56.md:22: quote CARRIED verbatim (10 words:
  "kanda means "group or category," as in makanda ma nza"), but locator
  WRONG. The quote is on print page 9 (folio "9" on extract page 9), inside
  the section "Matrilineal Descent as Political Process" (heading on page 8).
  The Gate line and the row both cite "p. 10, section 'Matrilineal Descent
  as Political Process'". Replacement: "p. 10, section" -> "p. 9, section".
- S376 anchor quotes, SOURCES.md:405: all CARRIED verbatim, but all four
  page locators off by one. "the term ngudi a nkazi, "mother's brother," can
  refer to a man who is not a member of the speaker's matrilineal clan" is on
  p. 10 (row says p. 11); "to belong to the kingdom, one acquired a title in
  exchange for tribute, and equipped oneself with appropriate insignia" is on
  p. 12 (row says p. 13); the block quote "I have already paid for the title,
  so let it be given to my sister's son Na Mpyoso Nsakala Nangudi." is on
  p. 12 (row says p. 13). Replacements: "p. 11" -> "p. 10"; "p. 13" ->
  "p. 12" (both occurrences).
- S376 entry sentences (kongo-kingdom.md :78): CARRIED in substance, three
  locators off by one. "kanda means group or category" is on p. 9 (cited
  p. 10); "patrilateral links between matrilineal nodes" is on p. 10 (cited
  p. 11); "a title could be acquired for tribute and equipped with insignia"
  is on p. 12 (cited p. 13). Replacements: "(S376, p. 10)" -> "(S376,
  p. 9)"; "(S376, p. 11)" -> "(S376, p. 10)"; "(S376, p. 13)" ->
  "(S376, p. 12)".
- S376 tier: CARRIED. Tier B (specialist conference paper, not peer-reviewed,
  contested position) fits criterion 6; the row's scope note correctly rules
  out royal chronology, provinces, mani titles and the sixteenth-century
  court, and the entry does not use it for those.
- S376 Grounds = teaches: CARRIED. Identical text in lesson Gate and row
  teaches cell.

## Re-runs

- reports/round-56/accept-c.py re-run at the current worktree: exit 0, all
  seven legs PASS (SET count=232, SWEEP rows 232 files 232, FLOOR cited=54,
  RANGE/STATUS/USEDBY/ACCESS clean). Note: the script emits a SyntaxWarning
  ("\|" invalid escape sequence) at accept-c.py:18; cosmetic today but a
  future-Python breakage risk.
- tools/check-gate-quotes.py against lessons/round-56.md: exit 0, 0 findings.
- Re-opened URLs (ordinary curl, no challenges): S374 purl.pt PDF (18 MB,
  HTTP 200), S375 Ghent PDF (3.7 MB, HTTP 301 -> backoffice.biblio.ugent.be
  download, then 200), S376 ZMO PDF (159 KB, HTTP 200).

## Unrun checks

None. All four per-row checks were executed for the three rows; no tools were
mutated in this seat (mutation of the O claim's tools is handled by the
dedicated mutation seats).
