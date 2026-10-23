# ReviewSupersedeC58 — superseding rows S566 (→ S440) and S567 (→ S445)

Round-57 residual Falsify findings under review (corpus/lessons/round-57.md Falsify list,
".ufo/waves/round-57/residual/KotodamaR57.ReopenRowsB57.md" F4, "ReopenRowsC57.md" F3):
S440's scope cell is truncated; S445's second anchor quote differs from the served sentence
by truncation (the routed wording's "apostrophe" half belongs to S452 — S445 has no
apostrophe drift, verified below). Both rows are cited by
corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md (S440 at :98, S445 at :59),
so both superseding rows are `mined` with that used-by. The registry is append-only:
nothing below edits S440 or S445 in place.

## S440 → S566 — verdict: agree, fix = restore the truncated scope ending

Re-opened by ordinary means, 2026-10-23.

- `https://collections.vam.ac.uk/item/O1053476/` — direct GET, HTTP 200, text/html,
  48,480 bytes, byte-identical to the count the row's access cell records.
- Both anchor quotes are verbatim on the served page, including the apostrophe: the page
  serves `merchant's mark` with a plain ASCII apostrophe (0x27, in the meta description and
  the object-details table), exactly as the stored row spells it. No apostrophe drift.
- The scope cell (`corpus/SOURCES.md:469`) is truncated mid-clause:
  `…and the commemorative context of a merchant about.` — the sentence cannot end there.
  Agree with B57's F4. The proposed completion `of a merchant's tomb.` is faithful to the
  row itself (its teaches cell says "on his tomb brass"), to the citing entry sentence
  (:98 "a sheriff's memorial brass"), and to the page's own Summary: "Monumental brasses
  are commemorative plaques that served as effigies and were most commonly found in
  churches". S566 restores the scope cell in full; every other cell stands.
- Second quote also verbatim: `Brass rubbing of a brass shield containing a merchant's
  mark and carding comb.` (served in Physical description).

Registry row (append; teaches opens `supersedes S### — `):

| S566 | Victoria and Albert Museum, London. Object record E.3632-1927 (Print Department, PDP): "Print (brass rubbing), from the brass of John Jay, Sheriff, ca. 1480, St. Mary Redcliffe, Bristol". V&A Explore the Collections. — https://collections.vam.ac.uk/item/O1053476/ (direct GET, HTTP 200, text/html, 48,480 bytes; re-opened live 2026-10-23, served count unchanged from the cell's record.) | docs | A | what a merchant's mark was placed on (a shield on a monumental brass in a church), that it could be paired with a trade instrument (carding comb), and the commemorative context of a merchant's tomb. | served text: "Rubbing of a shield with a merchant's mark from the brass of John Jay, Sheriff, dated ca. 1480, in St. Mary Redcliffe, Bristol"; served text: "Brass rubbing of a brass shield containing a merchant's mark and carding comb." | supersedes S440 — scope only: restores S440's truncated scope ending ("of a merchant about." → "of a merchant's tomb."); both anchor quotes, the served text, tier and source verify unchanged. A merchant's mark could be shown on a shield, alongside a tool of the merchant's trade, on his tomb brass. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |

Gate line:

- S566 — https://collections.vam.ac.uk/item/O1053476/ — accessed 2026-10-23 — served text: “Rubbing of a shield with a merchant's mark from the brass of John Jay, Sheriff, dated ca. 1480, in St. Mary Redcliffe, Bristol”. Grounds: supersedes S440 — scope only: restores S440's truncated scope ending ("of a merchant about." → "of a merchant's tomb."); both anchor quotes, the served text, tier and source verify unchanged. Content as S440: a merchant's mark could be shown on a shield, alongside a tool of the merchant's trade, on his tomb brass. Seat: ReviewSupersedeC58.

Locator output (all runs this session, `python3 -B reports/round-58/reopen-quote.py '<url>' '<quote>'`):

```
Q: Rubbing of a shield with a merchant's mark from the brass of John Jay, Sheriff, dated ca. 1480, in St. Mary Redcliffe, Bristol
LOCATED https://collections.vam.ac.uk/item/O1053476/
exit=0
Q: Brass rubbing of a brass shield containing a merchant's mark and carding comb.
LOCATED https://collections.vam.ac.uk/item/O1053476/
exit=0
```

## S445 → S567 — verdict: agree, fix = restore the full served sentence in quote 2

Re-opened by ordinary means, 2026-10-23.

- `https://heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf` — direct
  GET, HTTP 200, application/pdf, 87,655 bytes; text extracted with pdftotext (raw mode).
- Quote 2 is truncated in the row. Served bytes (`Råd nr 3`): "Fargene bør velges blant
  metallene gull (gult) eller sølv (hvitt), kombinert med fargene rødt, blått, svart,
  grønt eller purpur, eventuelt med stiliserte pelsverk (hermelin eller gråverk)." — the
  stored span closes at `purpur."`, fabricating a terminal period where the source has a
  comma and continues. Agree with C57's F3; S567 carries the full served sentence.
- The "apostrophe" clause of the routed wording does not apply to S445: the stored spans
  match the PDF text exactly and contain no apostrophes at all (that drift is S452's,
  reviewed by ReviewSupersedeD58 → S568).
- All three other anchors verbatim with genuine terminal periods: `Råd nr 2` ends
  `gjentatt. Enda flere…`; `Råd nr 9` ends `blasonering. Dette…` (pdftotext runs
  `fagspråket,blasonering` without a space — typographic only, normalizes identically);
  quote 4 ends `kjenne igjen. Senere ble…`. The first span remains the row's locator
  anchor and locates live.
- Scope, tier, kind and source cells verify unchanged; only the truncated quote is
  replaced.

Registry row (append):

| S567 | Hans Cappelen, 2017, "Gode råd om nye kommunevåpen" (Good advice on new municipal coats of arms), Norsk Heraldisk Forening (Norwegian Heraldry Society), PDF at heraldikk.no (recommended by KS in 2009 for municipal use rules; design advice authored by the society). — https://heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf (direct GET, HTTP 200, application/pdf, 87,655 bytes; re-opened live 2026-10-23.) | docs | A | what "kommunevåpen" (municipal coat of arms) is called and its parts (skjold 'shield', blasonering 'blazon'), the modern design rules (metal+colour rule, one/limited motif, simplicity, recognition at speed/distance/small size), why arms changed over time, and the distinction from logos/trademarks. | served text: "Våpenet bør helst ha bare to farger og en figur som eventuelt kan være gjentatt."; served text: "Fargene bør velges blant metallene gull (gult) eller sølv (hvitt), kombinert med fargene rødt, blått, svart, grønt eller purpur, eventuelt med stiliserte pelsverk (hermelin eller gråverk)."; served text: "Våpenet bør kunne beskrives i det heraldiske fagspråket, blasonering."; served text: "For riddere med skjold, i kampens hete, var det viktig å ha enkle våpenmerker som de raskt kunne kjenne igjen." | supersedes S445 — quote 2 only: restores the full served sentence (the stored span closed at "purpur." where the PDF continues ", eventuelt med stiliserte pelsverk (hermelin eller gråverk)."); all other anchors, the scope, tier and source verify unchanged. Norwegian municipal coats of arms are designed to be two-colour (one metal plus one colour) single-motif, stylized emblems blazoned verbally for recognition at a distance. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |

Gate line:

- S567 — https://heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf — accessed 2026-10-23 — served text: “Våpenet bør helst ha bare to farger og en figur som eventuelt kan være gjentatt.”. Grounds: supersedes S445 — quote 2 only: restores the full served sentence ending "eventuelt med stiliserte pelsverk (hermelin eller gråverk)." (the stored span stopped at "purpur."); all other anchors, the scope, tier and source verify unchanged. Content as S445: Norwegian municipal coats of arms are designed to be two-colour (one metal plus one colour) single-motif, stylized emblems blazoned verbally for recognition at a distance. Seat: ReviewSupersedeC58.

Locator output (all runs this session, `python3 -B reports/round-58/reopen-quote.py '<url>' '<quote>'`):

```
Q: Våpenet bør helst ha bare to farger og en figur som eventuelt kan være gjentatt.
LOCATED https://heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf
exit=0
Q: Fargene bør velges blant metallene gull (gult) eller sølv (hvitt), kombinert med fargene rødt, blått, svart, grønt eller purpur, eventuelt med stiliserte pelsverk (hermelin eller gråverk).
LOCATED https://heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf
exit=0
Q: Våpenet bør kunne beskrives i det heraldiske fagspråket, blasonering.
LOCATED https://heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf
exit=0
Q: For riddere med skjold, i kampens hete, var det viktig å ha enkle våpenmerker som de raskt kunne kjenne igjen.
LOCATED https://heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf
exit=0
```

## rejected:

None. Every source opened this session is offered above (the two row URLs, each live and
locating). Lane files consulted for the findings are not sources: corpus/SOURCES.md:469,
474; corpus/lessons/round-57.md Falsify; .ufo/waves/round-57/residual/KotodamaR57.
ReopenRowsB57.md F4 and ReopenRowsC57.md F3; the citing entry lines
corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md:59, :98.

## Notes for the L1

- Records-row rules: TOPIC/RELEVANCE/8-30-word teaches limits are claim-C legs and do not
  apply per the assignment; both rows keep the registry's records conventions (11 cells,
  `supersedes S### —` teaches, `mined` + the heraldry used-by since S440/S445 are cited,
  opened 2026-10-23, recheck 2027-10-23). No in-place edits proposed: S440 and S445 keep
  every cell (append-only); only status/recheck/used-by may ever be touched in place, and
  nothing here needs that.
- The entry's citations can keep naming S440/S445 or be repointed to S566/S567 at the
  integrator's option — the superseding rows are `mined` with the same used-by either way
  (S489/S490 precedent).
- Sources today were verified byte-level (pdftotext raw for the PDF; served HTML bytes for
  the V&A record), not merely normalized: the S445 fix carries the exact served words and
  comma; S440's quotes and apostrophes match served bytes one-for-one.

installs: none (pdftotext 26.08.0 already on the host; pypdf is invoked by
reopen-quote.py itself via `uv run --with pypdf==5.4.0`, ephemeral, no system install).
