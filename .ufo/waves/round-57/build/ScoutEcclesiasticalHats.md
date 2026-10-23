# ScoutEcclesiasticalHats — round 57, claim C source report

Ecclesiastical heraldry: the clerical hat (galero) with its tassels by rank, and the 1969 instruction *Ut sive sollicite*. TWO sources filed, both NEW to the lane (host-level greps against corpus/SOURCES.md print 0), both opened this session by ordinary GET, every offered quote verified live with `python3 -B reports/round-57/reopen-quote.py` before filing. No tool installs (used curl, plain python3, and `uv run --with pypdf==5.4.0`, the same pypdf path the locator itself uses).

Facts of the pair, for the entry editor: the tassel-ladder tradition (colour + tassel rows by rank) comes from the heraldic reference (source 2); the 1969 reform text (source 1) suppresses the red hat as worn dress, keeps a black hat admissible of red-and-gold cords and tassels, re-permits arms, and requires them simple and clear. The mitre-and-crozier removal from arms is carried by source 2's sentence about the same 1969 instruction (source 1's Latin span for that clause is OCR-damaged, see Rejected).

## Sources

### NEW-ScoutEcclesiasticalHats-1
citation: Sacra Secretaria Status (Hamleto I. Card. Cicognani a publicis Ecclesiae negotiis), "Instructio circa vestes, titulos et insignia generis Cardinalium, Episcoporum et Praelatorum ordine minorum — Ut sive sollicite", 31 March 1969, in *Acta Apostolicae Sedis* 61 (1969), pp. 334–340; official gazette scan served by vatican.va (PDF pp. 334–341 of the 939-page 1969 volume; printed p. 336 = PDF page index 335, printed p. 339 = PDF index 338).
url: https://www.vatican.va/archive/aas/documents/AAS-61-1969-ocr.pdf
route: direct plain GET (curl and the round locator), HTTP 200, `application/pdf`, content-length and body both 4,095,490 bytes, no challenge
kind: record
tier: A — the Holy See's own official publication of the instruction, the rule's own Latin words; OCR layer of 1970s vintage, so spans were chosen clear of OCR gaps
scope: what the instruction itself prescribes — §9 abolishing the cardinals' red hat (galerus) and red plush hat as dress and retaining a black hat that may carry cords and tassels of red and gold; §28 permitting a coat of arms to cardinals and bishops, to be drawn to the norms of armorial art, simple and clear. Not the older tassel-count ladder (not in this text), not dress of bishops' hats beyond §14–17, not post-1969 practice.
quotes:
- AAS p. 336 §9: "Ruber galerus et petasus e rubro item gausapo abolentur"
  `LOCATED https://www.vatican.va/archive/aas/documents/AAS-61-1969-ocr.pdf`
- AAS p. 336 §9: "In usu autem permanet petasus e nigro gausapo, qui, si casus ferat, chordulis flocculisque rubri et flavi coloris"
  `LOCATED https://www.vatican.va/archive/aas/documents/AAS-61-1969-ocr.pdf`
- AAS p. 339 §28: "Sive Patribus Cardinalibus, sive Episcopis conceditur, ut generis insigne adhibere possint"
  `LOCATED https://www.vatican.va/archive/aas/documents/AAS-61-1969-ocr.pdf`
- AAS p. 339 §28: "insignium delineandus erit, idemque simplex atque perspicuus sit oportet"
  `LOCATED https://www.vatican.va/archive/aas/documents/AAS-61-1969-ocr.pdf`
teaches: The 1969 instruction abolished cardinals' red and plush hats as dress, retained a black hat with optional red-and-gold cords and tassels, and re-licensed simple, clear arms for cardinals and bishops.
draft sentences:
- Paul VI's 1969 instruction abolishes the cardinals' red hat (galerus) and the red plush hat as dress, down to the object itself. (NEW-ScoutEcclesiasticalHats-1, AAS p. 336 §9)
- What survives in wear is a black hat that may, when the case requires, be adorned with cords and tassels of red and gold colour. (NEW-ScoutEcclesiasticalHats-1, AAS p. 336 §9)
- The same instrument grants that both cardinals and bishops may use a coat of arms — the emblem right is restated, not withdrawn. (NEW-ScoutEcclesiasticalHats-1, AAS p. 339 §28)
- Any such arms are to be drawn to the norms of the art of arms and must be simple and clear, a legibility rule written into the grant itself. (NEW-ScoutEcclesiasticalHats-1, AAS p. 339 §28)
- A worldbuilder can model on this edge case: one authority retires the worn badge while renewing the emblem in the same reform, so dress and device move on separate schedules. (NEW-ScoutEcclesiasticalHats-1, AAS p. 339 §28)

### NEW-ScoutEcclesiasticalHats-2
citation: Velde, François. "Catholic Heraldry", Heraldica.org ecclesiastical-heraldry reference page (undated page; site generator meta of 1990s vintage; page opens with a standing warning that some prescriptions described are out of date; cites the 1245 concession, the 1832 Ceremonial Congregation setting, decrees of 1644, 1915, 1951, and the 13 April 1969 instruction).
url: https://www.heraldica.org/topics/catholic.htm
route: direct plain GET (curl and the round locator), HTTP 200, `text/html`, 9,087 bytes, no challenge
kind: community
tier: B — specialist heraldry reference that names its decrees and dates, but community-maintained and self-flagged out of date; it counts tassel ROWS, not per-side tassel counts, and drafts must keep that strength
scope: the hat timbre (galero) ladder as the page reports it — cardinals red, tassels (fiocchi) in triangles of five rows; patriarchs, primates and archbishops green, four rows, with a patriarchal cross in pale behind the shield; bishops green, three rows, simple cross; generals of orders and abbots black, three rows; curates and parish priests black, one row; the 1832 central standardization of the cardinal's five rows; and its statement that the 13 April 1969 instruction abolished the crozier and mitre in arms. Not per-side counts (15/10/6 — the page does not give them), not prelates' purple-hat rows in full, not Orthodox practice.
quotes:
- §Cardinals: "From the hat hang a number of tassels (fiocchi), arranged so as to form triangles on both sides of the shield"
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- §Cardinals: "The number of rows of tassels increased steadily and was set at 5 in 1832."
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- §Cardinals: "The hat was conceded to cardinals in 1245, and they started placing it in their achievements in the late 14th c."
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- §Archbishops and Bishops: "Patriarchs. Primates, Archbishops: green hat with 4 rows, patriarchal cross in pale behind the shield"
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- §Archbishops and Bishops: "Bishops: green hat with 3 rows, simple cross."
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- §Archbishops and Bishops: "An instruction of April 13, 1969 abolished the use of the crozier and mitre."
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- §Orders: "Generals of orders and abbots use a black hat with 3 rows."
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- §Orders: "These rules were very loosely applied, and it is frequent to see them ignored in the 17th-18th centuries."
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
- top warning: "Warning: some of the heraldic prescriptions described here are out of date."
  `LOCATED https://www.heraldica.org/topics/catholic.htm`
teaches: Ecclesiastical rank reads from the hat timbre — colour plus tassel rows: cardinals five, archbishops four, bishops and abbots three, priests one — standardized in 1832; 1969 removed crozier and mitre.
draft sentences:
- A cardinal's achievement is topped by a red hat whose tassels (fiocchi) hang in triangles on both sides of the shield, in five rows. (NEW-ScoutEcclesiasticalHats-2, §Cardinals)
- The ladder below reads by colour and rows: patriarchs, primates and archbishops green with four rows and a patriarchal cross in pale behind the shield. (NEW-ScoutEcclesiasticalHats-2, §Archbishops and Bishops)
- Bishops take the green hat with three rows and a simple cross, so cross form as well as tassel count separates an archbishop's arms from a bishop's. (NEW-ScoutEcclesiasticalHats-2, §Archbishops and Bishops)
- Generals of orders and abbots wear a black hat with three rows and parish priests one row — and the same page warns these rules were very loosely applied, often ignored in the seventeenth and eighteenth centuries. (NEW-ScoutEcclesiasticalHats-2, §Orders)
- The cardinal's five rows were fixed only in 1832 after a steady increase, so the page itself dates the readable ladder late; a worldbuilder should date-check any hat before reading rank off it. (NEW-ScoutEcclesiasticalHats-2, §Cardinals)
- Per this page, the 13 April 1969 instruction abolished the crozier and mitre from arms, which leaves the hat and its tassels as the rank timbre after the reform. (NEW-ScoutEcclesiasticalHats-2, §Archbishops and Bishops)

## Cross-checks and notes for the entry editor

- The Latin §9 pair and the English translation agree: cardinals' retained black hat takes red-and-gold cords and tassels; the bishops' retained black plush hat takes green cord and tassels (FIU translation §16, opened, not filed). Colour of cord-and-tassel is itself rank-bearing even after the 1969 simplification.
- Popular over-read to guard in the entry: (a) per-side tassel counts (15/10/6/1) are widely quoted but NOT carried by either filed source — the opened page gives rows only; (b) the hat ladder was loosely applied before 1832 and is flagged out of date by its own reference; (c) after 1969 a red galero in arms is archaizing — the wearing hat was abolished while arms continued under a simplicity rule.

### Rejected
- https://www.college-of-arms.gov.uk/resources/ecclesiastical-hats-roman-catholic-church — College of Arms page "Ecclesiastical Hats: Roman Catholic Church". Opened three times by ordinary means (reader tool, curl default, curl --http1.1 --retry 2): every attempt died with TCP connection reset (challenge met, not passed). Its per-side counts (cardinals red 15 per side, archbishops green 10, bishops green 6, priests black 1) are therefore NOT offered — no opened copy. Wayback fallback unavailable today (see next item).
- web.archive.org — "Internet Archive: Temporarily Offline" service page returned for CDX and would-be captures on 2026-10-22 (port 80 refused, https serves the outage page). All Wayback routes were down this session; both filed sources were reached direct.
- https://cardinals.fiu.edu/instruction69.htm — "The Cardinals of the Holy Roman Church" (Salvador Miranda, Florida International University), complete English translation of Ut sive sollicite digitized from AAS 61 (1969) 334–340, HTTP 200, 13,502 bytes. Opened and read in full; NOT filed as a row (two-row cap; the official Latin is filed as NEW-ScoutEcclesiasticalHats-1). Retained as a cross-check: its §9 ("The red cardinalitial hat ("galero") and the red plush hat are abolished. The black plush hat is retained. When appropriate, it can be adorned with the red and gold cord and tassels."), §16 (bishops' black plush hat with green cord and tassels retained) and §28 ("The use of coats-of-arms by Cardinals and Bishops is permitted... The use of the crozier and mitre in the coat-of-arms is suppressed.") match the Latin filed above.
- Guessed vatican.va HTML editions (rc_seg-st_doc_19690331/19690621_ut-sive-sollicite _en/_lt.html) — all HTTP 404; vatican.va currently serves the instruction as the AAS gazette scan only.
- NEW-ScoutEcclesiasticalHats-1 candidate quote "Ab huiusmodi autem insigni sive baculi pastoralis sive infulae effigies tollantur" (§28, the crozier-and-mitre removal clause) — NOT_LOCATED: the gazette's OCR layer reads "baculi pa\xad\nstorali", dropping a character of "pastoralis", so no verbatim span crosses that word. The clause is instead supported by NEW-ScoutEcclesiasticalHats-2's located 1969 sentence. Locator runs: 1 NOT_LOCATED (this), 15 LOCATED.
