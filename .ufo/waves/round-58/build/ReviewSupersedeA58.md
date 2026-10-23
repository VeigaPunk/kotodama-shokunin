# ReviewSupersedeA58 — superseding rows S560–S562 (S413, S417, S421)

Round 58 records seat, 2026-10-23. Scope: the three named findings (round-57-verifier-spotcheck.md §5 item 4 bullet 1 and round-57.md Frontier item 1 / Falsify ReopenRowsA57). Every named source re-opened this session by plain GET (curl / reopen-quote.py, ordinary means, no challenge solving). Verdicts follow; three superseding rows proposed for the append-only registry. Claim C row rules (TOPIC, RELEVANCE) not applied — these are records rows.

## Findings

### 1. S413 (Fox-Davies 1909) — cadency quote punctuation: served ` ; ` vs commas — **AGREE**

Re-opened: `https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt` (direct, HTTP 200, `text/plain`, 1,875,872 bytes, fetched 2026-10-23). The served text (djvu.txt lines 24771–24774) reads:

> The other marks of difference are : For the second son a crescent ; for the third son a mullet ; for the fourth son a martlet ; for the fifth son an annulet ; for the sixth son a fleur-de-lis ; …

The row's cadency anchor has commas ("For the second son a crescent, for the third son a mullet, for the fourth son a martlet, for the fifth son an annulet") where the scan prints ` ; `. ReopenRowsA57's finding reproduces exactly. LOCATE passes today only because the locator normalises ` ; ` and `,` alike; the cell is not a byte copy of the served text.

Exact fix: superseding row **S560** carrying the cadency anchor with served semicolons. I re-verified all ten anchor quotes of S413 against this one scan this session: the other nine are faithful (Q2's "an infraction" and Q8's "one inheritance" de-hyphenate served `in-`/`inherit-` line breaks, which the locator joins; Q5 correctly stops at "indicating sovereignty" where the served list continues "dominion, alliance, descent, or pretension"). All other anchors, tier and scope stand, so S560 carries them unchanged. S560 cites only the foxduoft scan — all ten quotes locate in it, so the superseded row's three further scan URLs are no longer needed.

### 2. S417 (Boutell 1894) — scope says 'domination' for 'Dominion' — **AGREE**

Re-opened: `https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt` (direct, HTTP 200, `text/plain`, 667,163 bytes, fetched 2026-10-23). The served glossary (djvu.txt lines 5873–5874) reads:

> Arvis of Dominion, Borne by Sovereign Princes, being also the arms of the realms over which they rule.

("Arvis" is the scan's OCR of "Arms"; the index, line 15620, concurs: `of Dominion, 102`.) Boutell's category is **Arms of Dominion**, not "arms of domination"; the scope cell's "arms-of-domination/community/office/pretension categories" misstates the book's term.

Exact fix: superseding row **S561** with the scope cell corrected to "arms-of-dominion/community/office/pretension categories", grounded by a new glossary anchor that avoids the OCR-garbled headword: "Borne by Sovereign Princes, being also the arms of the realms over which they rule" (LOCATED). Two additional deviations found during this re-open, fixed in the same row: the anchors ending "…persons of eminence." and "…a wreath, or a cap." carry invented terminal full stops where the served text has ` : ` ("…of eminence : they were attached…"; "…or a cap : but in our own Heraldry…"); S561 ends those two spans where the served punctuation ends. The fourth crest anchor ("…princely and noble rank.") is verbatim served, full stop included.

### 3. S421 (Court of the Lord Lyon, "Blazoning") — anchor drops the served commas — **AGREE**

Re-opened: `https://courtofthelordlyon.scot/blazoning.htm` (direct, HTTP 200, `text/html`, 41,791 bytes, fetched 2026-10-23). Served (page lines 83–84, two `<h3>` elements): `Basic rule - no metal on a metal, no ` + `colours on a colour.` The anchor "Basic rule - no metal on a metal no colours on a colour" drops that comma and the full stop. The spot-check's "commas" (plural) covers the whole anchor cell: checking all four served spans this session —

- BLAZ-1 drops 1 comma + full stop (above);
- BLAZ-2 served: "We try not to repeat ourselves, so of the First refers to the first colour given, Argent" — anchor drops two commas;
- BLAZ-3 served: "However, everyone of the same surname will usually have Arms based on similar "undifferenced" Arms (usually those of the Chief)." — anchor drops the comma, the parentheses, the quotation marks and the full stop;
- BLAZ-4 served: "There are no "family Coats of Arms" - all Arms are individual to a person." — anchor drops the quotation marks and the full stop.

Exact fix: superseding row **S562** with all four anchors restored to the served punctuation. Note on rendering: the served inner double quotes are written as single quotes inside the spans ("'undifferenced'", "'family Coats of Arms'"), the convention of the registered S419 row, so the straight-quote span delimiters stay unambiguous; the locator is quote-mark-blind and all four locate. First span (BLAZ-1) is machine-parsed and clean. Tier and scope stand.

Baseline: `reopen-quote.py --row S413` / `--row S417` / `--row S421` all print `LOCATED` today — the defects are cell fidelity, not location.

## Superseding rows (proposed; registry is append-only)

```
| S560 | Fox-Davies, Arthur Charles. 1909. *A Complete Guide to Heraldry*. London: T.C. & E.C. Jack. Internet Archive item completeguidetoh00foxduoft (Robarts Library, University of Toronto scan). — https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt (direct, HTTP 200, text/plain 1,875,872 bytes, fetched 2026-10-23.) | book | A | the row may support: the two metals (or gold, argent silver) and their depiction as yellow/white; the five colours (gules, azure, vert, purpure, sable) and the stains murrey/sanguine and tenne; the furs (ermine with ermines/erminois/pean variants, vair from the squirrel pelt, potent/counter-potent); the rule of tincture (no colour on colour, no metal on metal); its stated exceptions (furs, "proper" charges, composite charges, and the Jerusalem cross potent on argent which Woodward enumerated against 26 continental breaches); the hatching/tricking conventions for monochrome representation; jewellery/gem-name blazon conventions. | p. 85: "One of the earliest rules one learns in the study of armory is that colour cannot be placed upon colour, nor metal upon metal."; p. 85: "Many writers have gone so far as to say that the only case of an infraction of this rule will be found"; served text: "For the second son a crescent ; for the third son a mullet ; for the fourth son a martlet ; for the fifth son an annulet"; served text: "The eldest son bears this label during his father's lifetime, succeeding to the undifferenced shield on the death of his father"; served text: "THE science of marshalling is the conjoining of two or more coats of arms upon one shield for the purpose of indicating sovereignty"; served text: "The methods of marshalling are (i) dimidiation, (2) impalement, (3) quartering, (4) superimposition."; served text: "the same identical crest can be and regularly is granted to half-a-dozen people of as many different surnames"; served text: "The shield of arms was one inheritance, descending by known rules. The crest was another, but a separate inheritance"; ch. XI: "Lion rampant. — The animal is here depicted in profile, and erect, resting upon its sinister hind-paw"; ch. XI: "is represented in the act of walking, the dexter forepaw being raised, but all three others being upon the ground" | supersedes S413 — the marks-of-cadency anchor is restored to the served semicolons (a crescent ; a mullet ; a martlet ; an annulet); all other anchors, tier and scope stand. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |
```

```
| S561 | Boutell, Charles. 1894 (4th edn, revised by A. C. Fox-Davies). *English Heraldry*. London: Cassell & Company. — https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt (direct, HTTP 200, text/plain 667,163 bytes, fetched 2026-10-23.) | book | B | the row may support: crest definition (helm-top device, not the whole achievement), crest-coronet distinction, hereditary descent and cadency marks (roundle fifth son, annulet eighth son), arms-of-dominion/community/office/pretension categories, badges as non-shield devices, banner and bardings carriage, tincture names (metals/colours) and the "puerile" planet/gem name system, motto placement. | served text: "Crest. A figure or device originally worn upon a helm, and now generally represented above a Shield of arms."; served text: "Crests at first were ensigns of high honour, and their use was restricted to a few persons of eminence"; served text: "Crests are still represented standing upon either a coronet, a wreath, or a cap"; served text: "in our own Heraldry a crest-coronet must always be carefully distinguished from those coronets that are insignia of princely and noble rank."; glossary, s.v. Arms of Dominion: "Borne by Sovereign Princes, being also the arms of the realms over which they rule" | supersedes S417 — the scope cell's arms-of-domination is corrected to Boutell's Arms of Dominion (glossary: borne by Sovereign Princes, the arms of the realms they rule; the scan's OCR prints the headword "Arvis of Dominion"), and two invented terminal full stops are dropped from the crest anchors. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |
```

```
| S562 | Court of the Lord Lyon, 2018 (page © Court of the Lord Lyon MMXVIII; content note "© Bruce Durie & Court of the Lord Lyon"), "Blazoning", official website of the Court of the Lord Lyon (Scotland). — https://courtofthelordlyon.scot/blazoning.htm (direct, HTTP 200, text/html 41,791 bytes, fetched 2026-10-23.) | docs | A | may support the entry's claims on what the parts of a coat of arms are called (field, charge, tinctures, attitudes), the cardinal rule of tincture placement, the "no family coat of arms / arms are individual" correction, and how undifferenced arms relate to a surname group. | LYON-BLAZ-1: "Basic rule - no metal on a metal, no colours on a colour."; LYON-BLAZ-2: "We try not to repeat ourselves, so of the First refers to the first colour given, Argent"; LYON-BLAZ-3: "However, everyone of the same surname will usually have Arms based on similar 'undifferenced' Arms (usually those of the Chief)."; LYON-BLAZ-4: "There are no 'family Coats of Arms' - all Arms are individual to a person." | supersedes S421 — all four anchors are restored to the served punctuation (the Basic-rule comma and full stop, BLAZ-2's two commas, BLAZ-3's opening comma, parentheses and quotation marks, BLAZ-4's quotation marks and full stop); tier and scope stand. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |
```

Status `mined` with the superseded rows' used-by: all three are cited by `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md` (S413 at :42, :65, :66, :69, :76, :77, :79, :81, :140, :145, :147; S417 at :70, :133, :134; S421 at :41, :65, :66, :68, :69, :132 — verified this session).

## Locator lines (`python3 -B reports/round-58/reopen-quote.py '<url>' '<quote>'`, run 2026-10-23)

S560 — URL `https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt`, one run per anchor:

```
[S560-1 tincture rule, p. 85]          LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-2 infraction clause, p. 85]      LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-3 cadency marks (corrected ;)]   LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-4 eldest son label]              LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-5 marshalling defined]           LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-6 methods of marshalling]        LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-7 identical crest]               LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-8 two inheritances]              LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-9 lion rampant]                  LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
[S560-10 lion passant]                 LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt
```

S561 — URL `https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt`:

```
[S561-1 crest definition]              LOCATED https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt
[S561-2 ensigns of high honour]        LOCATED https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt
[S561-3 coronet, wreath or cap]        LOCATED https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt
[S561-4 crest-coronet distinction]     LOCATED https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt
[S561-5 Arms of Dominion glossary]     LOCATED https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt
```

S562 — URL `https://courtofthelordlyon.scot/blazoning.htm`:

```
[S562-1 LYON-BLAZ-1 (corrected ,)]     LOCATED https://courtofthelordlyon.scot/blazoning.htm
[S562-2 LYON-BLAZ-2 (corrected ,,)]    LOCATED https://courtofthelordlyon.scot/blazoning.htm
[S562-3 LYON-BLAZ-3 (corrected ,()"")] LOCATED https://courtofthelordlyon.scot/blazoning.htm
[S562-4 LYON-BLAZ-4 (corrected "".)]   LOCATED https://courtofthelordlyon.scot/blazoning.htm
```

Current-row baseline (first double-quoted span of each superseded row): `--row S413` → `LOCATED https://archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt`; `--row S417` → `LOCATED https://archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt`; `--row S421` → `LOCATED https://courtofthelordlyon.scot/blazoning.htm`.

## Handoff notes for the integration owner (L1)

- Entry `heraldry-emblems-identity-marks.md:66` embeds the comma-less string `Basic rule - no metal on a metal no colours on a colour` citing S421. When S562 lands, that citation should point at S562 (the corrected cell), or the inner quote brought to the served punctuation — integration owner's call; I do not edit the entry.
- S560 does not carry the superseded row's `djvu.txt:9122-9123` / `djvu.txt:9295-9298` line refs: today's foxduoft fetch serves the two beast quotes at lines 8912–8913 and 9088–9092, so the old refs do not match the cited scan; S560 drops line refs rather than assert wrong ones (locator normalisation is line-break-blind; all ten quotes LOCATE).
- No in-place cell edit of S413/S417/S421 is proposed anywhere; the three rows keep their cells, S560–S562 are appends.

## rejected

None — every source opened this session is offered in a row above (foxduoft_djvu.txt → S560; englishheraldry00bout_djvu.txt → S561; blazoning.htm → S562).

installs: none.
