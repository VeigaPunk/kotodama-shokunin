# Round 55 falsify — ReviewRowsS315toS319

Verdict: claim C carries rows S315, S317, S318, S319 at the stated strength; row S316 is cited by the knowledge entry with one clause the page does not carry, and row S315's knowledge and gate sentences convert the study's claim into a stronger one. Two substantive findings, one minor locator finding.

Verification method: ordinary means only. S315 PDF fetched plain from uva.theopenscholar.com (HTTP 200, 6.35 MB), text extracted with `pdftotext -layout`, page mapping by running heads (printed page = PDF page − 55). S316 fetched plain (HTTP 200). S317 read from the cited Wayback capture 20250329180841 (id_ raw, `--compressed`; a plain live request gets HTTP 403). S318: plain request to sacred-texts.com/book/the-prose-edda/gylfaginning currently returns Cloudflare HTTP 403; a normal user-agent request returned the reader page (387,542 bytes, same as the row's session size), text read from it and cross-checked against the Wayback capture of the legacy page sacred-texts.com/neu/pre/pre04.htm (20211015001432). S319 fetched plain from Gutenberg (HTTP 200, 955,837 bytes). No installs were made (curl, pdftotext, python3 already present).

## Findings

### S315 — Dorofeeva-Lichtmann 1995, BEFEO 82 (PDF)
- S315 p. 59 route quote: CARRIED. "It includes 26 lists of mountains. Each list is perceived as forming a route." verbatim on printed p. 59 (PDF page 4).
- S315 p. 59 triad quote: CARRIED. "The text specifies the location, appearance and function of these beings and things" verbatim on p. 59.
- S315 p. 86 quote: CARRIED. "These sections constitute a spiritual landscape, or a geography of divine influences." verbatim on printed p. 86 (PDF page 31).
- S315 p. 87 quote: CARRIED. "the main purpose for the casting of the tripods was that they enabled people to distinguish the local spirits" verbatim on printed p. 87 (PDF page 32).
- knowledge/myth-symbol/monsters-hybrid-beings.md:71 "A 1995 study reads the book's creatures as marks of the divine powers holding each stretch of land (S315, pp. 59, 86).": OVER-READ. The study says terrain features and terrains are perceived as "homes" of deities, spirits and supernatural creatures, and that creatures "can hardly be distinguished clearly from divinities" (p. 59), and that "each terrestrial section submits to a particular group of deities" (p. 86). It never reads creatures as "marks of the divine powers". Replacement: "A 1995 study reads the book's creatures as inseparable from the divine powers holding each stretch of land (S315, pp. 59, 86)."
- Gate line lessons/round-55.md S315 grounds, final clause "read as marks of the divine powers holding each stretch of land": OVER-READ (same reason). Replacement: "Beings are filed by route, described by a fixed triad, and read as inseparable from the divine powers holding each stretch of land."

### S316 — Walters MS W.593 description —- S316 Abstract quote: CARRIED. "one hundred eighty-one paintings of different sizes" verbatim in the record's description paragraph.
- S316 fol. 32a title: CARRIED. "A fabulous creature in Sind that appears at a fire-temple" verbatim.
- S316 fol. 44b title: CARRIED. "Divers in the Sea of ʿUmān save themselves by feeding the fish and monsters" verbatim.
- S316 fol. 178a title: CARRIED. "A bird like a peacock with a lion's head" verbatim (curly apostrophe matches).
- knowledge/myth-symbol/monsters-hybrid-beings.md:71 "…and make sea monsters a toll on a named crossing (S316, fols. 44b, 52b).": UNSUPPORTED. All 173 titled paintings on the page were listed; none shows a toll or crossing. Fol. 44b is divers feeding fish and monsters (not a toll); fol. 52b is "First half of a map of the world". The page also contains zero occurrences of "island", so "named town, sea and island" over-claims. Replacement: "Al-Qazwīnī's illustrated copies index beings by named town and sea, include a world map, and compose hybrids from two named animals (S316, fols. 44b, 52b, 178a)."
- Gate line lessons/round-55.md S316 grounds "spreads its 181 paintings across named towns, islands and seas": DEFECT on "islands" (no island reference on the page). Replacement: "A sixteenth-century Persian copy spreads its 181 paintings across named towns and seas, includes a world map, and composes hybrids from two named animals." (The SOURCES.md S316 statement cell carries the same "islands" over-claim.)

### S317 — British Museum object 1850,1228.2 (Wayback capture,20250329180841)
- S317 Description field quote: CARRIED. "Gypsum wall-panel relief: winged human headed bull facing left; protective spirit; guarded entrance into what may have been the king's private apartments; inscription." verbatim.
- S317 Curator's comments label quotes: CARRIED. "This protective spirit guarded the entrance into what may have been the king's private apartments.", "The pair to it is in the Metropolitan Museum, New York.", "Room S, door e, panel 1" all verbatim under Curator's comments.
- S317 Production date "865BC-860BC", Ruler "Ashurnasirpal II", Excavator "Sir Austen Henry Layard", Height 309 centimetres / Length 315 centimetres: all CARRIED verbatim.
- knowledge line 72 ("protective spirit that guarded the entrance … with its pair now in New York"): CARRIED.

### S318 — Brodeur's Gylfaginning (sacred-texts reader)
- Gate quote, ch. XXXIII: CARRIED. "he is named Loki or Loptr, son of Fárbauti the giant; his mother was Laufey or Nál" verbatim (the "was" form is correct). The {p. 41}, {p. 42}, {p. 45} markers bound the cited passages as labeled; {p. 78} precedes the ch. LI material.
- All eleven row anchor quotes (three children; serpent placement; Hel's placement; Hel's hall furniture; the hand pledge; the tightening band; the sword gag; the not-killing reason; "there he lies till the Weird of the Gods"; ch. LI jaw-to-earth-and-heaven) CARRIED verbatim.
- knowledge line 74 and line 80 (wolf "brought up at home" among the Æsir; serpent in the sea; Hel in Niflheim; "would not stain it with the Wolf's blood"; fetter/pledge/sword binding): CARRIED.

### S319 — Gutenberg pg9700.txt (Harrison & Sharp 4th ed.)
- Gate quote, lines 102–104: CARRIED. "wäs se grimma gäst Grendel hâten, mære mearc-stapa, se þe môras heóld, fen and fästen; fîfel-cynnes eard" verbatim in the file (line 534–536; the file prints "fen and fästen", matching the quote).
- S319 anchors lines 107, 111–113, 162–163: CARRIED verbatim (file lines 539, 543–545, 598–599).
- knowledge line 79 ("derives Grendel from the kin of Cain … eotenas, ylfe, orcnêas, gigantas"): CARRIED (S319, lines 107–113).
- knowledge line 99 "Grendel comes from the moor bearing God's wrath (S319, line 711).": content CARRIED, locator WRONG-LOCATOR by one line. In this edition poem line 711 is "Þâ com of môre under mist-hleoðum" and line 712 is "Grendel gongan, godes yrre bär." (the edition's own glossary cites "com gongan, 711"). Replacement: "Grendel comes from the moor bearing God's wrath (S319, lines 711–712)."

## Residual risk and verification gaps
- S318: the live URL now answers 403 to a plain request; I verified against the reader page fetched with a normal browser user-agent and against the archived legacy page. Identical quote wording in both.
- S315: page numbers were mapped by running heads; PDF pages 4, 31 and 32 are printed pages 59, 86 and 87 respectively, and every quote matched the mapped page.
- S316: painting-count check was exhaustive (all 173 titled entries on the page reviewed), so absence of any toll/crossing/island item is established for this record.
- No unrun checks remain for the slice.
