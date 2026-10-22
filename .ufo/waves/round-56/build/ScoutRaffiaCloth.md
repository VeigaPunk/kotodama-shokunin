# ScoutRaffiaCloth — Kongo raffia cloth as currency, rank and gift

- seat: `KotodamaR56.ScoutRaffiaCloth` (scout, claim C ground: civilizations / Kingdom of Kongo)
- round: kotodama 56 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim base `052f145cbcff6996c153d460d81ce346ce74bfbc`, declaration `b4b7db91a38447bb2c07b0ef436fc9654dcec89c`
- assignment: claim C source item — Kongo raffia cloth as currency, rank and gift, from museum records of early-modern Kongo textiles and one open scholarly source on cloth as money and status in West Central Africa; aimed at what a worldbuilder must decide
- draft ids used below: `NEW-ScoutRaffiaCloth-1` … `-3`; the L1 assigns the final `S` ids at integration from the reserved block S359–S418
- access date for every source below: 2026-10-22. Every quotation in the three rows, and every page-carried string listed under Findings, was substring-checked against the saved bytes (0 misses, whitespace-normalised only; the PDF was read in `pdftotext` flow order, not `-layout`, because two-column layout order breaks sentences across the gutter)

## Route summary

| row | file actually read | route | bytes |
|---|---|---|---|
| 1 | `https://journals.flvc.org/athanor/article/download/126740/126293/207658` (article PDF; landing page `https://journals.flvc.org/athanor/article/view/126740`, journal self-description `https://journals.flvc.org/athanor/about`) | direct plain `curl`, HTTP 200, `application/pdf`, 9 pages, text via `pdftotext` (flow order); landing and about pages HTTP 200; no challenge, no login | 731695 |
| 2 | `https://web.archive.org/web/20220523145743/https://www.britishmuseum.org/collection/object/E_Af1951-04-118` | live URL HTTP 403 with a Cloudflare interstitial titled "Just a moment..." (5542-byte block page) — challenge met, not passed; record read from Wayback capture `20220523145743`, HTTP 200 | 136201 |
| 3 | `https://web.archive.org/web/20151110063110/http://www.metmuseum.org/exhibitions/listings/2015/kongo/blog/posts/kongo-textiles-renaissance-european-collections` | live URL HTTP 429 (rate-limit response page, 34223 bytes) on two plain requests; read from Wayback capture `20151110063110` (mobile rendering of the same URL), HTTP 200 | 34702 |

Two cautions for reviewers, recorded before the rows.

- **Pagination.** The Athanor PDF's own printed folios run 83–91 (page 2 carries "84", page 9 carries "91"). The journal's record for the same article declares `citation_firstpage` 93 and `citation_lastpage` 101. The locators below use the printed folios visible in the file that was read, so a reviewer checking page 84 will find the passage; a reviewer checking page 93 will not.
- **Tier honesty.** Athanor is not a peer-reviewed research journal in the strong sense. Its own About page says it "features student papers from the annual Art History Graduate Symposium hosted by the Department of Art History at Florida State University." That is why row 1 is B and not A, and why its Kongo background rests on Vansina (1998), Martin (1986) and Dapper (1686) in the author's own translation.

---

### NEW-ScoutRaffiaCloth-1

citation: Forbes, Carlee S. 2014. *Creativity in the Congo Free State: Nineteenth and Twentieth-Century Funerary Mats*. *Athanor* 32: 83–91 (printed folios in the PDF; the journal record declares pp. 93–101). ISSN 0732-1619 (print), 2690-0181 (online). DOI/stable id: none assigned; stable article URL `https://journals.flvc.org/athanor/article/view/126740`, PDF `126740/126293`.

url: https://journals.flvc.org/athanor/article/download/126740/126293/207658

route: direct plain request (curl), HTTP 200, `application/pdf`, 731695 bytes, 9 pages, read with `pdftotext` in flow order; no challenge, no login, 2026-10-22

kind: paper

tier: B — a student paper in a departmental art-history symposium journal, so a strong secondary write-up with reproducible citations rather than an authority; its Kongo textile background rests on Vansina (1998) and Martin (1986) and on Dapper (1686) in the author's translation, and it is authoritative only for its own reading of the objects it studies. Not C: it quotes its sources with page numbers and its translation choices are visible. Not A: nothing here is a primary Kongo voice or a peer-reviewed study.

scope: the article's own distinction between Kongo with a K and the modern states; the grade order of Kongo textiles and who may wear or display the finest; that undecorated cloth served as currency in a qualified sense; the tribute-tax, marriage and friendship uses; the mpu cap as a decorated-cloth form; the labour time of a fine piece; Dapper's four-kinds passage as an outsider's account; the execution rule for unauthorised sale of a high-grade cloth. It does **not** establish a Kikongo vocabulary for cloth or grades, a price list, or the internal organisation of weaving.

quotes:
- p. 84, first column: "In the Kongo Kingdom, the finest textiles were reserved for nobles with high status."
- p. 84, first column (sentence ends with footnote marker 7 in the file, omitted here): "Only the Kongo king and the members of the court whom he appointed were permitted to wear or display the finest quality textiles"
- p. 84, first column: "undecorated cloths were used as currency. The cloths were thin, but tightly woven."
- p. 84, second column: "Thus, raffia may not necessarily be used as currency in everyday transactions, but its exchange signaled ideas of prestige, status, or respect."

teaches: Forbes describes a graded Kongo textile order reserved to the king and his appointees, with undecorated cloth used as currency, tribute, marriage and friendship exchange rather than everyday money.

draft sentences:
- Grade the cloth before you grade its wearer: in the Kongo Kingdom the finest textiles were reserved for nobles with high status, so a garment states a rank before it states a taste (NEW-ScoutRaffiaCloth-1, p. 84).
- Give a person, not a market, the right to license the best cloth: only the Kongo king and the members of the court whom he appointed were permitted to wear or display the finest quality textiles (NEW-ScoutRaffiaCloth-1, p. 84).
- Run two economies on one fibre: decorated cloth marks rank, while undecorated cloths were used as currency, so decide which cloth each class of person may wear and which may pay with (NEW-ScoutRaffiaCloth-1, p. 84).
- Hedge the word money: the page says raffia may not necessarily be used as currency in everyday transactions, but that its exchange signaled ideas of prestige, status, or respect (NEW-ScoutRaffiaCloth-1, p. 84).
- Give plain cloth a small and a large unit: the cloths could be single units, or sewn into books by attaching several cloths in the corner, so the bundle rather than the coin is the large denomination (NEW-ScoutRaffiaCloth-1, p. 84).
- Let tribute and kinship move the cloth: there is evidence that the cloth could be collected as a tribute tax, and the same page records textiles exchanged in a marriage agreement or as a sign of friendship (NEW-ScoutRaffiaCloth-1, p. 84).

---

### NEW-ScoutRaffiaCloth-2

citation: The British Museum. Collection online record, museum number Af1951,04.118, object type "cloth; currency", made by Lele and Babunda, made in and found/acquired in the Democratic Republic of Congo, raffia palm leaf, woven, lengths 100 cm and 63 cm without fringes, purchased from Miss M Tew, acquisition date 1951, Department of Africa, Oceania and the Americas; curator's comments quoting Register 1951 with a 1982 CDMS correction.

url: https://web.archive.org/web/20220523145743/https://www.britishmuseum.org/collection/object/E_Af1951-04-118

route: live URL returned HTTP 403 with a Cloudflare interstitial titled "Just a moment..." (5542-byte block page) — challenge met, not passed; the record was read from Wayback capture `20220523145743` of the same URL, HTTP 200, 136201 bytes, 2026-10-22

kind: record

tier: A — the holding museum's own catalogue record for its own object, and the museum's own curatorial comment on the currency use; authoritative for what this object is and for what the museum asserts about cloth money. Scoped hard: the object is Lele and Babunda work from the Congo, **not** a Kongo object, so it is not authoritative for Kongo practice and must never be cited as a Kongo example.

scope: how a museum classifies a cloth as currency (object type carries both terms); that the record itself hedges the word currency with *Possibly*; the mechanics of strip money and sewn bundles; the range of obligations cloth paid (dues, fines, services, tributes) against areas where it also worked in market transactions; the record's own attribution history, including its correction of the 1951 register's spelling. It says nothing about Kongo grades, kingship or the Atlantic trade.

quotes:
- Description field: "Raffia woven cloth with a fringe on three sides. Possibly used as currency."
- Curator's comments, paragraph on cloth money: "Cloth made from raffia or pineapple leaf fibre was often used as currency in Congo."
- Curator's comments, same paragraph: "Strips of cloth would be used individually as smaller money or sewn together and become a more valuable unit."
- Curator's comments, Register 1951 quotation: "Typical of the Bambunda [sic; should be Babunda according to CDMS staff, 1982] tribe to the west of Lele territory."

teaches: The British Museum files a Lele and Babunda raffia cloth under both cloth and currency, and explains strips as small money and joined strips as a larger unit.

draft sentences:
- File a cloth under two object types at once, as the museum does: this record carries both cloth and currency, and its description reads raffia woven cloth with a fringe on three sides, possibly used as currency (NEW-ScoutRaffiaCloth-2, Description field).
- Build small change from strips and large money from seams: strips of cloth would be used individually as smaller money or sewn together and become a more valuable unit (NEW-ScoutRaffiaCloth-2, Curator's comments).
- Do not confine a cloth currency to one kingdom: the museum's comment says cloth made from raffia or pineapple leaf fibre was often used as currency in Congo, and that in some areas it paid dues, fines, services or tributes (NEW-ScoutRaffiaCloth-2, Curator's comments).
- Keep the record's own doubt in your prose: the description says possibly used as currency, and the comment generalises to Congo rather than to Kongo, so a possibility must not harden into a rule (NEW-ScoutRaffiaCloth-2, Description field).
- Expect the label to be corrected inside the record: the 1951 register calls the piece typical of the Bambunda and a 1982 note says this should be Babunda, while the record's own ethnic fields name Lele and Babunda (NEW-ScoutRaffiaCloth-2, Curator's comments).

---

### NEW-ScoutRaffiaCloth-3

**Optional third row.** This seat's assignment asked for one or two sources; rows 1 and 2 are the required pair. Row 3 is offered because it was opened anyway and it is the only one of the three that carries the European-collection and outsider-misnaming evidence the entry's section on where an outsider's record over-reads or misnames needs. Assign it an id only if the L1 wants that layer; otherwise leave the id unassigned.

citation: Thornton, Dora. 2015. *Made of Straw of Rare Beauty: Kongo Textiles in Renaissance European Collections*. Exhibition blog post, *Kongo: Power and Majesty*, The Metropolitan Museum of Art, posted 2 October 2015; author is Curator of Renaissance Europe and the Waddesdon Bequest, British Museum. No DOI; stable URL as captured.

url: https://web.archive.org/web/20151110063110/http://www.metmuseum.org/exhibitions/listings/2015/kongo/blog/posts/kongo-textiles-renaissance-european-collections

route: live URL answered HTTP 429 on two plain requests (rate-limit response page, 34223 bytes) — a throttle, not a challenge or a login; the post was read from Wayback capture `20151110063110` of the same URL (mobile rendering, same text), HTTP 200, 34702 bytes, 2026-10-22

kind: web

tier: B — a museum-published exhibition essay by a curator of the field, quotable for object identifications, for the collection history it reports and for the early-modern quotations it reproduces; it is an essay with no apparatus, its early-modern quotations are second-hand (it gives no page for Zuchelli or Pacheco Pereira), and it is not the exhibition catalogue. A only for the Pitt Rivers caption data it prints.

scope: the finishing technique described by a missionary; the comparison Europeans made with Italian silk velvet and the Pacheco Pereira judgement; the geometric pattern language and the curator's reading of it as meaningful rather than decorative; the European afterlife of these cloths in Kunstkammern from Prague in 1607 and in Sweden and Denmark; the Settala and Kircher annotations, including the Kircher description that puts the cloth in the Kingdom of Angola; one dated object caption (Pitt Rivers 1886.1.254.1, 17th–18th century, inventoried 1883). It carries **no** Kongo-side evidence: no maker, no price, no grade, no owner.

quotes:
- Body paragraph 2, on Zuchelli (1663–1716), Italian missionary to the Kongo, as the essay quotes him: "with a knife they cut the cloth in the proper spots and rub it well with their hands, so that it looks like patterned velvet"
- Body paragraph 2, as the essay quotes Duarte Pacheco Pereira (ca. 1460–1533): "that those made in Italy do not surpass them in workmanship"
- Body paragraph 3, on the design: "Bands of sophisticated geometric patterns spiral across the textile surfaces"
- Body paragraph 7, a description of 1709 quoted in the essay: "four mats made with admirable skill in the Kingdom of Angola"

teaches: A British Museum curator's Met exhibition essay describes Kongo raffia velvet finished by cutting and rubbing, and records such cloths in European Kunstkammern from Prague in 1607.

draft sentences:
- Describe the finish as a craft step rather than a material: an Italian missionary to the Kongo, Zuchelli, says the weavers cut the cloth in the proper spots and rub it well with their hands, so that it looks like patterned velvet (NEW-ScoutRaffiaCloth-3, body paragraph 2).
- Expect an outsider to price your cloth against his own luxury goods: Duarte Pacheco Pereira is quoted saying that those made in Italy do not surpass them in workmanship (NEW-ScoutRaffiaCloth-3, body paragraph 2).
- Put meaning in the pattern, not only skill in the weave: the essay says bands of sophisticated geometric patterns spiral across the textile surfaces, and that such repeating motifs were not merely decorative but had profound significance within Kongo society (NEW-ScoutRaffiaCloth-3, body paragraph 3).
- Plan for the cloth to end in a cabinet rather than on a body: Kongo luxury cloths were preserved in court and cabinet collections formed by rulers, princes, and urban elites, with the first two recorded examples in Prague in 1607 (NEW-ScoutRaffiaCloth-3, body paragraph 6).
- Expect the buyer's record to move the border: a description of 1709 quoted in the essay calls the pieces four mats made with admirable skill in the Kingdom of Angola, though the essay's subject is Kongo cloth (NEW-ScoutRaffiaCloth-3, body paragraph 7).

---

## Findings for the L1

### What these rows can carry, section by section

- **What was worn, and by whom.** Row 1 gives the rule in two steps: the finest textiles belong to nobles of high status, and within that, only the king and the court members he appoints may wear or display them (p. 84). The same page adds the sanction — "if a person was found selling a high-grade textile without the king’s permission, he or she could be executed" — and names the one Kongo word for a garment that these pages carry, the **mpu** cap, described as "One important form of the decorated cloths is the mpu cap worn by kings and chiefs". Design consequence: cloth is a grant from an office, and the offence is unauthorised *sale*, which tells you the cloth could be sold and that the crown's interest was in the trade as much as in the wearing.
- **What was paid, and in what units.** Row 1: undecorated cloths "were used as currency", thin and tightly woven, single units or sewn into books of several cloths at the corner. Row 2 gives the mechanics in a museum's words: strips as smaller money, sewn strips as a more valuable unit, and a list of obligations — "In some areas cloth was used to pay dues, fines, services or tributes" — with the counter-case that "in others it was also used in everyday transactions in the marketplace". Row 1 also records that "there is evidence that the cloth could be collected as a tribute tax". Design consequence: build the unit ladder (strip, cloth, book) and decide which obligations each rung discharges.
- **Where the cloth was a gift rather than a payment.** Row 1 is the only row here that names the non-commercial transfers: textiles in a marriage agreement, and as a sign of friendship, with the summary that its exchange "signaled ideas of prestige, status, or respect". Design consequence: the same object can be tribute (vertical), bridewealth (affinal) and gift (peer), and each channel needs its own rule about who may give and who may receive.
- **What was made, and how long it took.** Row 1 reports the labour: "it would take fifteen to eighteen days to create a textile that is about 20 x 20 inches", the piece being made on an upright loom with the design either embroidered in or piled and cut. Row 3 supplies the finishing description in a missionary's words and the outside judgement on it. Design consequence: a fine cloth is two to three weeks of one weaver's work for a square of about half a metre, which is a usable cost anchor for a pre-coin economy.
- **What changed between periods, as far as these rows go.** Row 1 spans the kingdom's own law and the nineteenth- and twentieth-century funerary use the article studies and states that after "the introduction of European cloth, the fine raffia textiles fell out of use". Row 3 dates the European side: Prague 1607 as the first two recorded examples, then Sweden and Denmark, the Milanese physician Settala's museum and Kircher's Musaeum Kircherianum in Rome, and the later dispersal that put one piece in Copenhagen's royal Kunstkammer by 1674 and then, deaccessioned, into the British Museum via Henry Christy. Design consequence: the same cloth is a royal garment at home and a curiosity abroad within one century, and the entry can stage that drift without inventing a decline date.
- **Where an outsider's record misnames.** Row 3's Kircher description of 1709 places the pieces "in the Kingdom of Angola", and the Settala drawing's annotation (page-carried, quoted in the list below) says "made in Angola or Congo". Row 2 shows a museum correcting its own register: the 1951 note's "Bambunda" is marked "[sic; should be Babunda according to CDMS staff, 1982]". Row 1 shows the article itself framing Dapper as "As an outsider, Olfert Dapper described in 1686". Design consequence: a worldbuilder can make the foreign catalogue a diegetic document with a wrong origin, and can make the correction a later hand in the same record.

### Disagreements to report, not harmonise

- **How much *currency* means.** Row 1 says undecorated cloths "were used as currency" and then immediately qualifies: "this was not necessarily a currency in the full sense of the term since it is unlikely that raffia was used in the buying and selling of goods" (page-carried). Row 2 says "often used as currency" and adds that in some areas it did serve market transactions. These are not contradictory but they are not the same strength. The entry should carry the stronger and the weaker claim with their sources, and the calibration bank should mark *raffia cloth was Kongo money* as bounded, not settled.
- **Whether the surviving pieces are Kongo at all.** The Met caption prints the museum's attribution — "Kongo peoples; Kongo Kingdom, Democratic Republic of the Congo, Republic of the Congo, or Angola" — and the other captioned piece is listed as "16th–17th century, inventoried 1674" with the same three possible modern countries. The British Museum record is Lele and Babunda. Treat every *Kongo* label on an early-modern cloth as the holding museum's attribution, not as the maker's statement.
- **Pagination of row 1.** Printed folios 83–91 in the file read; the journal's record says 93–101. A reviewer who cannot find p. 84 should search the PDF text for the quoted sentence rather than trusting the record's page numbers.

### Extra page-carried evidence the L1 may use in prose (verified present, not used as row quotes)

From row 1, p. 84:

- "The hierarchy of textiles and the regulations surrounding them were so important that if a person was found selling a high-grade textile without the king’s permission, he or she could be executed"
- "The Kongo people knew well and understood the differences between the different grades of textiles."
- "these textiles confirm and reaffirm the king’s spiritual and social power"
- "As an outsider, Olfert Dapper described in 1686" (the flow text carries a stray "3" after "1686", an OCR artifact, so quote no further on a Gate line)
- Dapper's four-kinds passage as the article translates it: "There are four kinds of cloths. The best and most refined has figures…it takes fifteen or sixteen days to make one. Only the king, and those whom he gives permission, may wear the cloth." (an ellipsis stands inside the source's own sentence; split the quotation before using it on a Gate line)
- "The second type is not as refined as the first, but the two types greatly resemble one another, and unless one is an expert, one may be fooled at first sight"
- "it would take fifteen to eighteen days to create a textile that is about 20 x 20 inches (50 x 50 cm)"
- "A report from the 1491 visit of Portuguese emissaries indicates that textiles were also hung on the wall, much like the tapestries that were displayed in Europe at that time."
- "In addition, these textiles were traded and presented to foreign dignitaries as objects of prestige."
- "there is evidence that the cloth could be collected as a tribute tax"
- "They could be single units, or sewn into “books” by attaching several cloths in the corner."
- "with the introduction of European cloth, the fine raffia textiles fell out of use" (the sentence continues: "and the production of other raffia materials (except for the funerary mats and mpu caps) declined as the Kingdom splintered in the late eighteenth century")
- "This study focuses on the funerary practices of the Kongo people" (the article's declared scope, and its warning not to confuse Kongo with Congo-Kinshasa or Congo-Brazzaville)

From row 2, Curator's comments and fields:

- "In some areas cloth was used to pay dues, fines, services or tributes, whereas in others it was also used in everyday transactions in the marketplace."
- "Cloth was a convenient means of exchange as it was portable, durable and divisible."
- Object type field reads "cloth ; currency"; ethnic fields read "Made by: Lele" and "Made by: Babunda"; materials field reads "raffia palm leaf"; technique "woven"; acquisition "Purchased from: Miss M Tew", 1951.
- The register's fibre note: the fibres came from a palm whose "native name" is given as "Mayanda", and the Lele and Bushongo weavers' own raffia textiles are called "Mambondu". **These are Lele and Babunda words on this record, not Kikongo; do not put them in a Kikongo word list.**

From row 3:

- "Such repeating motifs were not merely decorative but had profound significance within Kongo society."
- "the spiral movement is a visual metaphor for the path taken by the dead" (the essay reporting the exhibition curator Alisa LaGamma's catalogue chapter)
- "Kongo luxury cloths were preserved in court and cabinet collections formed by rulers, princes, and urban elites."
- "The first two recorded examples appear in Prague in 1607"
- "From Stockholm to Florence, London to Prague"
- "a small mat to make a cushion to sit on, made of straw of rare beauty" (the Settala drawing's annotation, as the essay quotes it; the annotation continues "made in Angola or Congo")
- "whose collection was to become the foundation of the British Museum in 1753" (Sloane)
- "It was first inventoried in the Royal Danish Kunstkammer in 1674 but was deaccessioned by the Nationalmuseet in Copenhagen and acquired by the Quaker and abolitionist Henry Christy (1810–1865), who gifted it to the British Museum."
- Object caption: "Luxury Cloth: Cushion Cover , 17th–18th century, inventoried 1883. Kongo peoples; Kongo Kingdom, Democratic Republic of the Congo, Republic of the Congo, or Angola. Raffia, pigment; 9 1/2 x 18 1/2 in. (24 x 47 cm). Pitt Rivers Museum, University of Oxford (1886.1.254.1)"
- The essay's own closing admission, usable as the honest limit of the European record: "the cultural, political, and trading exchanges in which textiles first changed hands in Kongo itself are still a mystery"

### Calibration notes for whoever writes the entry

- Row 1 is background, not the article's research. The Kongo textile passage sits in the introduction to a study of nineteenth- and twentieth-century funerary mats; cite it for what earlier scholarship holds (it footnotes Vansina 1998, pp. 9, 16–17, and Martin 1986, p. 2), never as a primary observation.
- The Dapper passage is a translation by Forbes of Dapper's *Description de l'Afrique* (1686), p. 324, and Dapper is an outsider compiler. Any sentence that says *Dapper reports* must not become *the Kongo held*.
- Row 2 is a **Lele and Babunda** object. Its value for the entry is the mechanism and the museum's classification language, plus one honest caution about how ethnic labels were assigned and later corrected. It must not be cited as evidence about the Kongo kingdom, and its *possibly used as currency* hedge must survive any paraphrase.
- Row 3 is an exhibition essay without apparatus. Its Zuchelli and Pacheco Pereira quotations are second-hand; if the entry needs their own words at tier A, the underlying printed accounts must be opened in a later round.
- None of these three sources gives a Kikongo term for cloth, for the grades, or for the bundles. The entry can name the **mpu** cap (row 1) and must otherwise say *cloth* or use a museum's English. Coinage such as *Kongo velvet* is the trade's English, not a Kikongo word; if the entry uses it, say so.
- The Met caption's three-country hedge ("Democratic Republic of the Congo, Republic of the Congo, or Angola") is the museum's own uncertainty about where a seventeenth-century Kongo-attributed cloth was made. Keep it as a hedge; it is a good model for how a worldbuilder should present a looted or decontextualised object.

## unopened

- **Pitt Rivers Museum record for 1886.1.254.1.** The accession number is known from the Met caption, but the museum's own object record was not reached: a guessed object URL (`https://objects.prm.ox.ac.uk/pages/PRMUID1886_1_254_1.html`) returned the museum's generic Collections online page (HTTP 200, 2406 characters of navigation only, no object fields), and the collections page exposed no object URL to a plain request. A later round should search the museum's public catalogue properly; that record is the tier-A replacement for row 3's caption.
- **British Museum live record** (`https://www.britishmuseum.org/collection/object/E_Af1951-04-118`) — HTTP 403 with a Cloudflare interstitial titled "Just a moment..." on two plain requests, one with a desktop user agent. Challenge met, not passed; read from Wayback capture `20220523145743`.
- **Met live post** — HTTP 429 on two plain requests (rate limit); read from Wayback capture `20151110063110`.
- **Vansina, Jan. *Raffia Cloth in West Central Africa, 1500–1800*.** In *Textiles: Production, Trade and Demand*, ed. Maureen Fennell Mazzaoui (Variorum, 1998), pp. 9–17 as row 1 cites them. No public copy located; the Taylor and Francis chapter page returned only a publisher preview of the opening sentences. This is the single most valuable next row for this topic.
- **Martin, Phyllis M. *Power, Cloth and Currency on the Loango Coast*.** *African Economic History* 15 (1986). Not opened (JSTOR); it is the natural tier-A companion for the Loango coast and the Vili kingdom, which the entry will need if it discusses cloth money beyond Kongo proper.
- **Dapper, Olfert. *Description de l'Afrique* (Amsterdam, 1686), p. 324.** Not opened in a public copy; the Dapper quotation in row 1 is Forbes's translation of that page, so the entry's Dapper sentence is second-hand by one step until a scan is read.
- **Museum Ulm's Kongo textile holdings.** Not attempted; no public record surfaced in the searches run here.
- **Nationalmuseet Copenhagen, object G.7406** (`https://samlinger.natmus.dk/es/object/73669`) — opened, HTTP 200, but the record carries only "tekstil", raffia, length 68 cm and width 63 cm, collected in Congo and given to the collection in 1964. It says nothing about rank, payment or date, so it was not used. The Copenhagen piece that matters for this topic is the one row 3 describes: inventoried in the Royal Danish Kunstkammer in 1674 and later deaccessioned to Henry Christy.
- **Pigafetta and Lopes (1591) and the nzimbu shell accounts.** Deliberately left to `ScoutNzimbuMoney`; the two money systems must not be merged into one paragraph without that seat's evidence.

## unrun checks

No lane command was run: claim C's acceptance (`reports/round-56/accept-c.py`), the README sweep and `tools/check-source-access.py` belong to the L1 at integration, and no corpus file was edited by this seat. No file was created or modified outside this report. No tool was installed or upgraded this session (`curl` and `pdftotext` were used as present; `pdftotext` is poppler's, version as shipped on the host). No git or jj command that writes was run anywhere.
