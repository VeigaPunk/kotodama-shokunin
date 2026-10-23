# ScoutMerchantMarks — Claim C source scout (KotodamaR57)

Seat: source scout for house marks / merchants' marks / Hausmarken (non-noble identity marks on goods, seals and houses, medieval and early modern Europe). Godspeed axes: (a) claim-support coverage (vocabulary, bearers, placement, rules of passing/changing, over-read guard), (b) source quality (museum record + open scholarly source, both LOCATED), (c) freshness (URLs unused below S413).

Two sources reported: 1 open scholarly treatise (Michelsen 1853, *Die Hausmarke*), 1 museum record (V&A object E.3632-1927). All six quotes LOCATED by the round locator (`python3 -B reports/round-57/reopen-quote.py`). Tools installed: none (no installs needed).

---

### NEW-ScoutMerchantMarks-1

citation: Michelsen, Andreas Ludwig Jakob. 1853. *Die Hausmarke. Eine germanistische Abhandlung*. Jena: Fr. Frommann. Stable id: Internet Archive item `diehausmarke00michgoog` (Google scan, public domain).
url: https://archive.org/download/diehausmarke00michgoog/diehausmarke00michgoog_djvu.txt
route: direct GET, HTTP 302 -> 200 (dn711300.ca.archive.org), text/plain, 184,267 bytes; opened in this session (downloaded, 3,572 lines).
kind: book (19th-century legal-historical monograph)
tier: B — dedicated Germanistic monograph on Hausmarken as a legal institution; directly supports the claim's house-mark/identity-mark strand, though it is period scholarship.
scope: what a Hausmarke is and who used it (including non-nobles and serfs); where marks were placed (houses, cattle, goods, seals); use as a signature/seal substitute; legal force and rules for changing marks; and the later relation between marks and arms.
quotes:
- L1: "dass der des Schreibens unkundige Aussteller ein Handzeichen, statt eigenhändiger Unterschrift, unter die Schrift setzte; und solche Zeichen sind eben, wie wir sahen, unsere Hausmarken."
  LOCATED https://archive.org/download/diehausmarke00michgoog/diehausmarke00michgoog_djvu.txt
- L2: "Es sind hier die Hausmarken der Vorzeit noch heute an den Wohnhäusern gar keine Seltenheit"
  LOCATED https://archive.org/download/diehausmarke00michgoog/diehausmarke00michgoog_djvu.txt
- L3: "Ein Hauptmittel für diese Erkennbarkeit war die alte Hausmarke;"
  LOCATED https://archive.org/download/diehausmarke00michgoog/diehausmarke00michgoog_djvu.txt
- L4: "Die Merkzeichen sollen an den Ohren (eyma mörc) sein und keine anderen Zeichen, denn nur die Ohrenzeichen sind gesetzmässige Marken (lögmarc)"
  LOCATED https://archive.org/download/diehausmarke00michgoog/diehausmarke00michgoog_djvu.txt
- L5: "Noch heute ist das ritterliche Wappen der Freiherren v. Gagern nichts andres als dieselbe Marke"
  LOCATED https://archive.org/download/diehausmarke00michgoog/diehausmarke00michgoog_djvu.txt
teaches: A house mark was a simple sign any household could own, and it could serve in place of a written signature.
draft sentences:
- A mark may replace a signature: in medieval practice a writer who could not write set his house mark under a document as a hand-sign (NEW-ScoutMerchantMarks-1, L1).
- Marks lived on buildings: in Erfurt, house marks of earlier ages were still no rarity on dwelling houses in the nineteenth century (NEW-ScoutMerchantMarks-1, L2).
- Design for recognizability: the old house mark was the main means by which property could be recognized, so marks work best when they can be read at a glance (NEW-ScoutMerchantMarks-1, L3).
- Some laws made only certain mark positions lawful: under Icelandic rules only ear-marks counted as legal livestock marks, so a world can restrict which parts of a thing may bear its mark (NEW-ScoutMerchantMarks-1, L4).
- A house mark could climb into heraldry: the knightly arms of the Freiherren von Gagern were said to be nothing other than the family's former mark, so an inherited mark may later be borne on a shield (NEW-ScoutMerchantMarks-1, L5).

---

### NEW-ScoutMerchantMarks-2

citation: Victoria and Albert Museum, London. Object record E.3632-1927 (Print Department, PDP): "Print (brass rubbing), from the brass of John Jay, Sheriff, ca. 1480, St. Mary Redcliffe, Bristol". V&A Explore the Collections, accessed 2026-10-22.
url: https://collections.vam.ac.uk/item/O1053476/
route: direct GET, HTTP/2 200, text/html (48,480 bytes); opened in this session.
kind: record (museum object catalogue record)
tier: A — primary museum record of an existing object; names the mark's bearer, placement and date with object-level authority.
scope: what a merchant's mark was placed on (a shield on a monumental brass in a church), that it could be paired with a trade instrument (carding comb), and the commemorative context of a merchant about.
quotes:
- L6: "Rubbing of a shield with a merchant's mark from the brass of John Jay, Sheriff, dated ca. 1480, in St. Mary Redcliffe, Bristol"
  LOCATED https://collections.vam.ac.uk/item/O1053476/
- L7: "Brass rubbing of a brass shield containing a merchant's mark and carding comb."
  LOCATED https://collections.vam.ac.uk/item/O1053476/
teaches: A merchant's mark could be shown on a shield, alongside a tool of the merchant's trade, on his tomb brass.
draft sentences:
- A merchant's mark could be displayed heraldically: on the brass of John Jay, sheriff, a shield on the monument carries his mark (NEW-ScoutMerchantMarks-2, L6).
- Marks could pair with trade implements: the same shield contains both the merchant's mark and a carding comb, linking the sign to its owner's occupation (NEW-ScoutMerchantMarks-2, L7).
- A mark could mark a person after death: the record shows the mark on a church monument in Bristol, so marks may serve as grave and commemorative signs (NEW-ScoutMerchantMarks-2, L7).

---

### Rejected

- Girling, F. A., *English merchants' marks* (1964), archive.org item `englishmerchants00girl` — access-restricted (lending/printdisabled); archive.org borrow-only books do not count (QUALITY criterion 10).
- McIntosh, Pat, *The merchant's mark* (2006), archive.org item `merchantsmark00mcin` — fiction and access-restricted.
- *Handmerken in Drenthe* (1986), archive.org item `handmerkenindren0000unse` — access-restricted.
- British Museum collection search (`britishmuseum.org/collection/search`) — HTTP 403 to plain GET with browser UA; bot-challenge met, not passed (no Wayback reroute attempted for a non-essential alternative).
- Met collection API — `/public/collection/v1/search` retired 2026-10-01; `/v1.1/search` paginated endpoint responds, but no merchant-mark object surfaced in the first pages worth quoting; not used.
- London Museum collections page (londonmuseum.org.uk) — JS-driven; no static quotable record text on the landing pages fetched.
- Notes on brass-rubbing (1973), archive.org item `notesonbrassrubb0000ashm` — not opened beyond metadata; skipped as not on-topic enough.
