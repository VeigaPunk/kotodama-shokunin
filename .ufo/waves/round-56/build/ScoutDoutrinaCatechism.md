# ScoutDoutrinaCatechism — the 1624 Kikongo catechism: the book's own credits and the linguists' valuation

- seat: `KotodamaR56.ScoutDoutrinaCatechism` (scout, claim C ground: civilizations / Kingdom of Kongo)
- round: kotodama 56 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `b4b7db91a38447bb2c07b0ef436fc9654dcec89c`, claim base `052f145cbcff6996c153d460d81ce346ce74bfbc`
- assignment: the 1624 Kikongo catechism *Doutrina Christaa* (Mateus Cardoso's edition of Marcos Jorge's catechism, Lisbon 1624), the oldest surviving printed Kikongo text — date, authorship and value for historical Kikongo from open sources, aimed at the design decisions named in the wave brief
- draft ids used below: `NEW-ScoutDoutrinaCatechism-1` and `-2`; the L1 assigns the final `S` ids at integration
- likely overlap: the Ghent chapter in row 2 is also the obvious source for the language-classification and early-dictionary seats; if another seat opens the same file, one registry row can carry several used-by entries

## Route summary

Everything below was opened by ordinary means: plain `curl`, no browser, no archive capture, no login, and no
challenge was met. The 1624 book was read from the holding library's own public scan; its title page was read as a
page image, because the scan's OCR layer is unusable for this typeface. Access date for both works: 2026-10-22.

| work | file actually read | route | size |
|---|---|---|---|
| *Doutrina christaã*, Lisbon 1624 (BNP RES-268-V) | `https://purl.pt/29608/4/res-268-v_PDF/res-268-v_PDF_24-C-R0150/res-268-v_0000_1-286_t24-C-R0150.pdf` | record page `https://purl.pt/29608` (HTTP 200) → public-copy link `https://purl.pt/29608/4` (HTTP 200, an HTML meta-refresh page) → PDF (HTTP 200, `application/pdf`); title page read as image at scan PDF p. 5 | 18,008,918 bytes, 286 PDF pages |
| Bostoen and de Schryver 2018, ch. 3 | `https://biblio.ugent.be/publication/8586729/file/8586730.pdf` | record page `https://biblio.ugent.be/publication/8586729` (HTTP 200, marked Open Access) → PDF download (HTTP 200, `application/pdf`) | 3,729,268 bytes, pp. 60-102 |

The 1624 scan prints long s (ſ); quotations below normalise it to `s`, and `nouo` is kept as the page prints it
(the page does not print `novo`). The five candidate Bostoen quotations, including the p. 77 passage used in a draft
sentence, were re-checked as substrings of the extracted text after whitespace normalisation, all five matching
(`/fast/scratch/hyaku/kotodama-r56/ScoutDoutrinaCatechism/verify_quotes.py`, exit 0). The book quotations were read from the page image at 300 dpi and are given after the long-s
normalisation; nothing else was changed.

---

### NEW-ScoutDoutrinaCatechism-1

citation: Jorge, Marcos (1525-1571), with additions by Inácio Martins (1530-1598); translation ordered by Mateus Cardoso (ca 1584-ca 1625). *Doutrina christaã*. Lisbon: Geraldo da Vinha, 1624. [4], 134, [2] fols., 8º (20 cm). Biblioteca Nacional de Portugal, RES-268-V; digitized copy in Biblioteca Nacional Digital, PURL 29608.

url: https://purl.pt/29608/4/res-268-v_PDF/res-268-v_PDF_24-C-R0150/res-268-v_0000_1-286_t24-C-R0150.pdf

route: direct plain request (curl), HTTP 200, `application/pdf`, 2026-10-22; reached from the BND record page `https://purl.pt/29608` (HTTP 200) through the public-copy link `https://purl.pt/29608/4`, an HTML page whose meta refresh points to the PDF; no challenge, no login, no browser

kind: book

tier: A — the printed book itself, authoritative for its own title page, imprint, dedication and stated credits. Not authoritative for the accuracy of its Kikongo or for Kongo history; the collation is the catalogue's, not a collation made by this seat.

scope: what the title page states: the work is composed by Marcos Jorge and augmented by Inácio Martins, the translation into the language of the Kingdom of Congo was made by order of Mateus Cardoso, the book is addressed to the King of Congo dom Pedro Affonso II, and it was printed at Lisbon by Geraldo da Vinha in 1624. Supports the entry's naming of the book, its credit chain, its language label and its royal addressee. Does not support any claim about the translation's quality, the identity of its Kongolese translators, or the book's contents beyond the title page.

quotes:
- title page (scan PDF p. 5): "De nouo traduzida na lingoa do Reyno de Congo, por ordem do P. Mattheus Cardoso Theologo"
- title page (scan PDF p. 5): "Ao muito poderoso, & catholico Rey de Congo dom Pedro Affonso segundo deste nome."
- title page, imprint (scan PDF p. 5): "LISBOA. Por Geraldo da Vinha. 1624."

teaches: The 1624 Lisbon catechism credits Marcos Jorge with the text, Inácio Martins with additions and Mateus Cardoso with ordering its translation into the language of the Kingdom of Congo.

draft sentences:
- The book's own title page gives a credit chain a worldbuilder can reuse: composed by Marcos Jorge, augmented by Inácio Martins, and translated into the language of the Kingdom of Congo by order of Mateus Cardoso (NEW-ScoutDoutrinaCatechism-1, title page).
- The title names the target speech only as the lingoa do Reyno de Congo, so the title page gives the polity's name rather than a separate language name for a worldbuilder to borrow (NEW-ScoutDoutrinaCatechism-1, title page).
- The dedication addresses the Rey de Congo dom Pedro Affonso segundo deste nome, so the entry can name the king the book is addressed to rather than leave the addressee vague (NEW-ScoutDoutrinaCatechism-1, title page).
- The imprint, LISBOA. Por Geraldo da Vinha. 1624., fixes the place, printer and year, so the entry should place the making of the earliest surviving Kikongo book in Lisbon (NEW-ScoutDoutrinaCatechism-1, title page).

---

### NEW-ScoutDoutrinaCatechism-2

citation: Bostoen, Koen, and Gilles-Maurice de Schryver. 2018. "Seventeenth-Century Kikongo Is Not the Ancestor of Present-Day Kikongo." In *The Kongo Kingdom: The Origins, Dynamics and Cosmopolitan Culture of an African Polity*, edited by Koen Bostoen and Inge Brinkman, 60-102. Cambridge: Cambridge University Press. DOI 10.1017/9781108564823.004. Open-access PDF, Ghent University repository record 8586729.

url: https://biblio.ugent.be/publication/8586729/file/8586730.pdf

route: direct plain request (curl), HTTP 200, `application/pdf`, 2026-10-22, from the Ghent record `https://biblio.ugent.be/publication/8586729` (HTTP 200, marked Open Access); no challenge, no login, no browser

kind: book

tier: A — a peer-reviewed research chapter by the KongoKing project's historical linguists, authoritative for the place of the 1624 text among seventeenth-century Kikongo sources and for the variety it documents. Not a critical edition: for the text's wording use row 1 and, if opened later, Bontinck and Ndembe Nsasi 1978.

scope: the status of the *Doutrina Christãa* in the surviving seventeenth-century Kikongo corpus (one of three surviving works; the set called the earliest surviving book-length sources in a Bantu language), its character as an interlinear Portuguese–Kikongo catechism translated under Cardoso's leadership, the variety its Kikongo most likely represents (the central South Kikongo subunit, the capital Mbanza Kongo), the contrast with the 1650s sources linked to Soyo, and the finding that seventeenth-century Kikongo is not ancestral to the whole Kikongo Language Cluster. Not the text's translation choices, its theology, or Kongo political history.

quotes:
- p. 60: "an interlinear Portuguese–Kikongo catechism from 1624 translated under the leadership of the Portuguese Jesuit Mateus Cardoso"
- p. 60: "they are also the earliest (surviving) book-length sources ever written in a Bantu language"
- p. 76: "most likely represent the variety that was spoken in the kingdom’s capital at that time"
- p. 100: "The Kikongo found in the Doutrina Christãa (1624), the Vocabularium Congense (1652) and the Regulae quaedam (1659) is thus not ancestral to the entire KLC"

teaches: Bostoen and de Schryver treat the 1624 catechism as one of three surviving seventeenth-century Kikongo sources and as evidence for the court variety of Mbanza Kongo.

draft sentences:
- Bostoen and de Schryver call the *Doutrina Christãa* an interlinear Portuguese–Kikongo catechism of 1624 translated under Mateus Cardoso's leadership, so the earliest surviving Kikongo book is a bilingual instrument, not a monolingual composition (NEW-ScoutDoutrinaCatechism-2, p. 60).
- They count the catechism among only three surviving seventeenth-century works in Kikongo and call that set the earliest surviving book-length sources in a Bantu language, which is the defensible form of the "oldest Kikongo book" claim (NEW-ScoutDoutrinaCatechism-2, p. 60).
- The chapter places the catechism's Kikongo in the central South Kikongo subunit and says the old sources most likely represent the variety spoken in the kingdom's capital, so the entry can present its vocabulary as Mbanza Kongo court usage with that hedge (NEW-ScoutDoutrinaCatechism-2, p. 76).
- Earlier scholars read the 1650s sources' <r> against the catechism's <d> as evidence that those texts recorded Soyo rather than the Mbanza Kongo court; the chapter reports that reading but cautions that the variation is not systematic, so an outsider's dialect label must not be taken at face value (NEW-ScoutDoutrinaCatechism-2, p. 77).
- The chapter concludes that the catechism's Kikongo is not ancestral to the whole Kikongo Language Cluster and that only later Kisikongo counts as its direct descendant, so a worldbuilder should stage 1624 as one court variety, not as the ancestor of all Kikongo speech (NEW-ScoutDoutrinaCatechism-2, p. 100).

---

## Findings for the entry's design decisions

| design decision | what these sources show | evidence |
|---|---|---|
| what the book is and who is credited with it | A Lisbon print of 1624 by Geraldo da Vinha. Its title page credits Marcos Jorge with the catechism, Inácio Martins with additions, and Mateus Cardoso with ordering the translation into the language of the Kingdom of Congo; it is addressed to dom Pedro Affonso II. The BNP record gives the collation and shelfmark RES-268-V. | row 1, title page and imprint; BND record page |
| what the language is called, and whose variety the book carries | The book calls it the *lingoa do Reyno de Congo*, naming the speech after the polity. Bostoen and de Schryver call the text interlinear Portuguese–Kikongo and place its Kikongo in the central South Kikongo subunit, most likely the variety of the capital, Mbanza Kongo. | row 1, title page; row 2, p. 60 and p. 76 |
| why the book matters for historical Kikongo | Of the dozen or so seventeenth-century works in Kikongo, only three survive; the chapter calls those three of exceptional scientific value and the earliest surviving book-length sources in a Bantu language. The catechism supplies 53 basic vocabulary items to the KongoKing phylogenetic comparison. | row 2, p. 60 and p. 75 |
| what changed between periods | The chapter concludes that the catechism's Kikongo is not ancestral to the whole Kikongo Language Cluster, and not even to all of South Kikongo; only later Kisikongo is its direct descendant. It also argues that the coastal, central and eastern South Kikongo dialect areas already existed in the seventeenth century, rather than resulting from the kingdom's later collapse. | row 2, p. 100-101 |
| where an outsider's record over-reads or misnames | The title page says Cardoso ordered the translation, not that he made it alone; the chapter says "under the leadership of" Cardoso, so a sentence crediting him with the Kikongo text over-reads the evidence. Earlier scholars read the 1650s sources' <r> against the catechism's <d> as proof that those texts recorded Soyo rather than the court, and the chapter qualifies that inference as not systematic. | row 1, title page; row 2, p. 60, p. 77 |
| what these sources do not establish | Neither source names a Kongolese translator; no Kikongo passage from the scan was transcribed or quoted by this seat, so no vocabulary or gloss is offered; the 1556 catechism said to precede the 1624 print was not opened and is not used. | rows 1-2; unopened list |

### Caveats the L1 should carry into the rows or the entry

- Quote `nouo`, not `novo`: the title page prints "De nouo traduzida". Modernising it would break the verbatim rule.
- The title page is set in capitals and long s; the quotations normalise ſ to s. Do not present the normalised spelling as a diplomatic transcript.
- The book's title is cited from the BNP record as *Doutrina christaã*; the title page prints the words in capitals, and this seat did not settle the diacritic from the image, so the entry should not quote the title line as evidence for a spelling.
- The chapter is not a critical edition and does not print the catechism's text. If the entry needs Kikongo wording or a verified gloss, the right source is Bontinck and Ndembe Nsasi 1978, which was not opened here.
- The scan's OCR layer is unusable for the Kikongo portions (old type, long s); the title page was read from the page image, but no body page was transcribed. Do not infer vocabulary from the OCR dump.
- The chapter's "KLC" is the Kikongo Language Cluster; expand the abbreviation on first use in the entry.
- "Oldest surviving printed Kikongo text" is defensible in the form the chapter supports: the catechism is the earliest of the three surviving seventeenth-century Kikongo works, and the set is the earliest surviving book-length material in a Bantu language. The chapter does not date this copy or collate it; the BNP record does.

## Not run

No lane command was run: this is a read-only scouting seat, the entry does not exist yet, and the acceptance
command would only re-measure the base. No file in the lane was created or modified except this report. No tool
was installed or upgraded (nothing was needed; `curl`, `pdftotext`, `pdftoppm`, `tesseract` and `python3` were
already present).

unopened: the IIIF viewer `https://purl.pt/29608/6` and the JPG set `https://purl.pt/29608/1` were not opened — the public PDF copy already gave the title page and the derivatives were unnecessary; the HathiTrust catalogue record of Bontinck and Ndembe Nsasi 1978, *Le catéchisme kikongo de 1624: réédition critique* (`https://catalog.hathitrust.org/Record/101994610`), was seen only in a search result and not opened — it would be the right source for the Kikongo text itself, but the assignment's question was answered by the book and the open chapter, and its access status was not tested; Thornton's Boston University page on the Kikongo sermon (`https://www.bu.edu/afam/people/faculty/john-thornton/roboredo-kikongo-sermon/`) and the Dialnet PDFs surfaced in the same search were not opened — tier-C leads for this question, superseded by the two works above; no source for the 1556 catechism was opened, so the claim that an earlier printed catechism preceded the 1624 book is not used anywhere in this report.
