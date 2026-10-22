# Re-open review: S306 (Molina 1571) and S307 (Shanhaijing 1668)

Round-56 reviewer `KotodamaR56.ReviewRowsS306S307`, routed by `corpus/lessons/round-55-verifier-spotcheck.md` §5 item 4 (non-author row re-open; S306 and S307 were carried unreviewed). Re-opened 2026-10-22 by ordinary means: plain curl, direct GET, HTTP 200 on every URL touched; no challenge, no login, no browser. Page images read as images (PIL crops at 2x-5x); the shanhaijing `_djvu.txt` was sampled only to confirm the row's "unusable" claim (its opening bytes are garbage tokens — row is right). No tools installed.

## Sources actually opened

- `https://archive.org/download/vocabularioenlen00moli_0/page/n279_w1000.jpg` — direct, HTTP 200, 648496 B. Same bytes as `n279_w1600.jpg` (server returns the 1618×2184 derivative regardless of width). Item page `https://archive.org/details/vocabularioenlen00moli_0` HTTP 200. Metadata API confirms title/date/publisher "En Mexico : En casa de Antonio de Spinosa", call_number `buc f 00124`, contributor Fisher - University of Toronto — every bibliographic cell in the row verified.
  - leaf n279, right column, s.v. Auitzotl: "Auitzotl, cierto animalejo de agua como perrillo." — **comma after the headword** (verified at 5x: the mark descends and curves; every period on the same leaf, e.g. in "Auitzocalaqui.n." and "delagua.", sits square on the baseline). Print hyphenates `perri-llo` across the line break.
  - leaf n279, right column, s.v. Auitzocalaqui: "Auitzocalaqui.n.nadar debaxo delagua." — print has no spaces after full stops and fuses `delagua`; entry continues `Prete. onauitzocalac.`, so the row's quoted segment is a prefix of the entry.
  - leaf n279, running head: "A ANTE V, ET X." — matches the row's scope note. Nahuatl headwords with Spanish glosses → this is part two (mexicana y castellana), as the row states.
- `https://archive.org/download/shanhaijing01shan/page/n15.jpg` (and n16, n17, n18; n8 HEAD-checked) — all HTTP 200. Item page HTTP 200. Metadata: date 1668, publisher "[N.p.]", call DS707 .S4 1668a, contributor Cheng Yu Tung East Asian Library, Guo Pu associated — row's bibliographic cells verified. Fold margin on n18 reads 山海經 卷之一 — juan 1 confirmed.
  - n15, 招搖之山, main text (unpunctuated): "有獸焉其狀如禺而白耳伏行人走其名曰狌狌食之善走"
  - n17, 基山 entry: "其狀如羊九尾四耳其目在背其名曰猼訑佩之不畏" — the whole 基山 entry (`又東三百里曰基山` opener through the 鵸鵌 bird and the 青丘之山 header) sits on n17; the only insertion in the row's quote is the comma after 其狀如羊, i.e. no character deviation.
  - n18, 青丘之山, main text: "有獸焉其狀如狐而九尾其音如嬰兒能食人食者不蠱" — the full fox passage is on n18 (first column bottom continues into the second column); the 青丘之山 header alone is on n17.
  - n18, route summary: "其神狀皆鳥身而龍首" — and preceding "凡䧿山之首自招搖之山以至箕尾之山凡十山二千九百五十里"; the suspect character is 䧿 (隹 base, no 灬 claws — verified at 5x), matching the row. The leaf's last column ends `其祠`; the itemised sacrifice prescription continues onto n19 (not opened).

## Findings by severity

### M1 — S306: quoted headword separator is a period; the print has a comma (verbatim defect, one mark)

`corpus/SOURCES.md:335` (anchor cell) and `corpus/lessons/round-55.md:90` (Gate quote) both write `Auitzotl.` — the leaf prints `Auitzotl,`. Period and comma are distinct glyphs in this typeface and the print distinguishes them on the same leaf (`Auitzocalaqui.n.` uses periods). No claim or Grounds depends on the separator; this is a purity fix.

SOURCES.md:335, inside the anchor cell —
old: `"Auitzotl. cierto animalejo de agua como perrillo."`
new: `"Auitzotl, cierto animalejo de agua como perrillo."`

round-55.md:90, Gate line —
old: `"Auitzotl. cierto animalejo de agua como perrillo."`
new: `"Auitzotl, cierto animalejo de agua como perrillo."`

### L1 — S306: silent spacing/fusion normalisation in the Auitzocalaqui quote

Print: `Auitzocalaqui.n.nadar debaxo delagua.` (no space after full stops; `del agua` printed fused). Row and quoting practice normalise to `Auitzocalaqui. n. nadar debaxo del agua.` Recommend either the literal form or a "(spacing normalized)" parenthesis. The `perri-llo` → `perrillo` dehyphenation across the line break is standard and needs no note beyond what is here.

### L2 — S307: modern punctuation added to all quotes without disclosure

The 1668 woodblock prints no punctuation; all four registry quotes and the Gate quote supply `，` and `。`. Every *character* in every quote was verified against the leaves (above). Recommend appending `(modern punctuation supplied)` to the row's access note — not stripping the marks, which aid reading.

### L3 — S307: route-summary quote is borderline under the ≤25-words cap

`凡䧿山之首，自招搖之山以至箕尾之山，凡十山，二千九百五十里。其神狀皆鳥身而龍首` = 35 hanzi; inside the cap by word-counting (~20), outside if hanzi count. Optional tightening (all verbatim on n18): `自招搖之山以至箕尾之山，凡十山，二千九百五十里。` (21 hanzi) and `其神狀皆鳥身而龍首` (9).

### Observations, no fix needed

- No printed folio number is legible on n279; the row's scope already says "scan leaf 279", which is the working locator.
- The citing claim "the sacrifice owed" (line 71) is carried: n18's last column opens the prescription with `其祠`; the itemised sacrifice list runs onto n19. If a future reader wants the list visible, n19 is the leaf.
- Both Gate lines are free of HTML entities (the §5 item-6 defect concerns other rows), and both quotes are within the cap: 7 words (S306), 23 hanzi (S307).
- Tier **A** for both rows is correct under QUALITY criterion 6: a dated 1571 primary dictionary and a dated 1668 print of the text itself, each read from the holding library's scan.
- Carriage verified: line 60 (dictionary gloss "only"), line 61 (基山 sheep anatomy), line 71 (route distance phrasing `又東三百里曰堂庭之山`, `又東三百八十里曰猨翼之山`, `又東三百五十里曰箕尾之山` + closing spirit/sacrifice), line 103 (fox `能食人食者不蠱`) — all supported by the opened leaves. Gate Grounds for both rows carried.
- Anchors verified live: `n279_w1000.jpg` 200, item page 200, `n15.jpg` 200, item page 200, `n8`/`n16`/`n17`/`n18` 200, both `_djvu.txt` 200.

## Verdicts

- **S306 — agrees with one required fix (M1):** change `Auitzotl.` → `Auitzotl,` in `corpus/SOURCES.md:335` and `corpus/lessons/round-55.md:90`; log old→new in the round-56 lesson as a routed registry cell correction.
- **S307 — agrees:** all four quotes character-verbatim against the leaves, every locator correct, no required change; L2/L3 are polish.

## Residual risk and unrun checks

- No `lsp` device exists in this seat's tool inventory; verification was by primary-source image inspection, which is the stronger check for quote fidelity.
- n19 (sacrifice-item continuation) was not opened; not required by any quoted claim.
- Molina part one (Castellan→Mexican) was not consulted; the entry's "only" is about the part-two headword's single gloss, which is what the leaf shows.
- The comma finding rests on a printed-glyph judgement (shape + baseline position vs. same-leaf periods); independent eyes at 5x zoom would confirm — pixels preserved under `/fast/scratch/hyaku/kotodama-r56/ReviewRowsS306S307/` (`v_mol_ab.jpg`).
- Rows checked at lane working-copy tip, not against the claim base commit; S306/S307 are round-55 records whose bytes the current review should keep unless the fix lands.
