NONE-MET

# AuditA3R12 — pre-freeze wording audit, ids S637, S638, S639

Candidate object: `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md` (inherited build, rev `14e6413820d482913f723432b62d566967ccd1a6`). Counter sha256 `b6389454…` not run here (not this seat's assignment); hence NONE-MET above, no fixture reached the counter.

Method: grep of the candidate entry for `\bS63[789]\b` (all citing lines), SOURCES.md rows read at :592–:594, then each page re-fetched by ordinary means (`curl -sSL`, URL literal) and judged as the blind support seat will: quote verbatim in body text (not heading/caption/nav/promo/cookie), teaches cell carried, every clause of every citing line carried. No installs (pacman paused; nothing needed). No lane file touched except this report; no git/jj write commands; all shell work under `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R12/`; no processes left running.

## Findings by severity

- **HIGH (fix before the freeze): S638, candidate-entry line 54** — the danger-to-remedy table states a class-universal the source contradicts. `AUDIT S638 REWRITE` below.
- S637, S639: no finding. `OK`.
- Observation (not a defect scored by a support seat): lines 75 and 115 carry the same S638 proposition twice (§5 "Command" and §8 "Adjuration without scripture"). Both are carried by the page; the duplicate only widens attack surface before a freeze. Dedup is the L1's call — never mine post-verdict.

## AUDIT S637 OK

- Citing lines: candidate-entry.md:83 only — `- Jasper: Pliny reports that throughout the East it was the custom, it is said, to wear iaspis as an amulet (S637). **C**`
- Page: https://www.gutenberg.org/cache/epub/62704/pg62704-images.html — curl HTTP 200, 4,667,556 bytes, exactly the size recorded in SOURCES. No Wayback needed (the row itself records capture 20260831093908 lacks the chapter).
- Quote location: Book XXXVII, `CHAP. 37.—IASPIS; FOURTEEN VARIETIES OF IT. DEFECTS FOUND IN IASPIS.` (text line 13652); the quote is body prose inside numbered section (9.) at text lines 13694–13695: **"Throughout all the East, it is the custom, it is said, to wear iaspis by way of amulet."** Verbatim contiguous body text; not a heading, caption, nav or promo. Not boilerplate (mid-book, between the bezel-setting remark and the monogrammos variety).
- Clause carry (line 83): "throughout the East it was the custom" ← "Throughout all the East, it is the custom"; the hedge **"it is said" is kept verbatim**; "to wear iaspis as an amulet" ← "to wear iaspis by way of amulet" (same claim). No universal drawn from one object, no comparison, cause, date or place added.
- Teaches carried: eastern amulet custom ✓ (quote sentence); varieties ✓ (chapter title "FOURTEEN VARIETIES"; body lists Indian/azure/purple/terebenthine kinds); defects ✓ (chapter title "DEFECTS FOUND IN IASPIS"; body "all blue to a fault" etc.). "Pliny's lapidary lore" framing keeps the attribution.
- Round-59 mapping: no rejection maps to S637 (rejections were S602/S616/S623/S643, `corpus/lessons/round-59-verifier-spotcheck.md` §3). The as-reported hedge is intact; nothing reworded, nothing to narrow.

## AUDIT S638 REWRITE

- Citing lines: candidate-entry.md:54, :75, :115.
- Page: https://journals.iaepan.pl/sa/article/download/2498/2871 — curl HTTP 200, 9,410,020 bytes, application/pdf, exactly the size recorded in SOURCES (Wayback capture listed in the row). pdftotext extraction.
- Quote location: journal p. 350 (PDF p. 12; page markers "350" at text line 303, quote at 327–328), section "Published medieval lead amulets found in Central Europe": **"Other amulets do not cite the Gospels but use an apotropaic adjuration formula by which they banish evil spirits and diseases."** Verbatim body text; not heading/caption.
- Teaches carried: one 14th-century lead amulet ✓ (abstract: "lead amulet with an engraved Latin inscription"; Gothic-minuscule dating "second half of the 14th century"); "a long quotation from the Gospel of John followed by an apotropaic formula with magical words" ✓ (abstract, verbatim); compared with German and Bohemian lead amulets ✓ (abstract "similar finds from Germany and Bohemia from the 11th-13th centuries"; Halberstadt/Sachsen-Anhalt, Dřevíč "Central Bohemia", "altogether 23 lead amulets have been found in Germany", comparanda share "lead materiality"); attributed to monks and educated clerics ✓ ("Manufacture of similar amulets has been attributed mainly to monks (Bracha 1991…)"; "made prevalently by well-educated clerics").
- Line 115 OK: "some written amulets do not cite the Gospels but use an apotropaic adjuration formula by which they banish evil spirits and diseases" — the page's own subset quantifier ("Other amulets…"), rest near-verbatim.
- Line 75 OK: "other written amulets do not cite the Gospels but use an apotropaic adjuration formula that banishes evil spirits and diseases" — the contrast with Gospel-citing amulets is the page's own ("Other amulets…"; the paper's surrounding text describes Gospel-of-John amulets, John 1–14 "included in many amulets"); "that banishes" ≈ "by which they banish"; "written" is faithful to the paper's textual-amulet context.
- **Line 54 over-reach:** the remedy cell reads "written amulets use an apotropaic adjuration formula to banish evil spirits and diseases" — a universal over the class. The page quantifier is "Other amulets" (a subset), and the same page contradicts the universal: "The most documented type of amulet in Central Europe includes a combination of the incipit of the Gospel of John and an adjuration formula" and late-medieval amulets "mostly showed a preference for a more 'humble' prayer form". The registry teaches keeps the modal ("A written amulet **can** work by adjuration alone"); the table cell drops it. A strict support seat can return NOT-SUPPORTED on this line, and one NOT-SUPPORT fails the whole claim.
- Minimal narrowing the page carries (id kept, table structure kept):

`old: | evil spirits and diseases | written amulets use an apotropaic adjuration formula to banish evil spirits and diseases | S638 (B) |`

`new: | evil spirits and diseases | some written amulets use an apotropaic adjuration formula to banish evil spirits and diseases | S638 (B) |`

## AUDIT S639 OK

- Citing line: candidate-entry.md:116 only — `- The grid: amulets believed to protect the owner against harm of all kinds were widely worn in the Islamic world, and the V&A record shows a silver amulet divided into a grid of single Arabic characters (S639). **B**`
- Page: https://collections.vam.ac.uk/item/O79669/ — curl HTTP 200, 47,443 bytes, exactly the size recorded in SOURCES.
- Quote location: verbatim in the record's Summary field (body of the catalogue record; not nav, cookie or promo): **"Amulets, which were believed to protect the owner against harm of all kind, were widely worn in the Islamic world."**
- Clause carry (line 116): (a) "amulets believed to protect the owner against harm of all kinds were widely worn in the Islamic world" ← Summary sentence verbatim; "kind"→"kinds" is the only normalization and the page's "believed" hedge is kept; (b) "the V&A record shows a silver amulet divided into a grid of single Arabic characters" ← Brief description "Square sheet silver amulet with inscribed Arabic characters in a grid, Lebanon, 1860-1870." + Physical description "Square of sheet silver with the front divided into 25 squares, each containing an Arabic character." ("single" = one character per square, as the page states it).
- Teaches carried: 25 squares of single Arabic characters ✓; "a small hole for suspension drilled in the centre of the top side" ✓; potency "derives from the way in which they are arranged… the letters form words or phrases with hidden meanings" ✓ (arrangement + hidden meanings).
- Round-59 mapping: no rejection maps to S639; the §3 spot-check re-opened this exact URL and agreed ("The quote is verbatim on the page (20 words, ≤25). The page also carries the entry's 25-square grid and the suspension hole."). Nothing reworded.

## Residual risk and verification gaps

- Scope was clause coverage of the lines citing S637/S638/S639 against their own pages. Cross-row consistency checks (e.g. S638's formula row vs S642's three-jobs row) are other seats' ids, not audited here.
- The 75/115 duplication is page-carried but untested against the support-seat packet builder; if the L1 dedups, that is a pre-freeze wording choice on its side.
- Byte equality with SOURCES holds at fetch time 2026-10-23; all three rows record fresh direct GETs of the same URLs, and S638/S639 list captures as fallback.
- LSP unavailable/irrelevant: audit is of prose bytes, so all checks are text-level against fetched page bytes; no code symbols involved.
- Kill-rule sensitivity: with the line-54 rewrite applied, all five citing lines are carried by their pages on today's fetches; without it, the claim carries one live NOT-SUPPORTED surface.
