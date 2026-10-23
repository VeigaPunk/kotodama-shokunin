# ReviewCarriedS396S399 — round 57 build seat (carried row findings, round-56 spot-check §5 item 5)

Scope: the three carried findings named for this seat — **S396** (wrong anchor locator; hedge-stripping entry sentence), **S397** (entry narrows the object's date range), **S399** (entry over-read resolved at base; ** object-number metadata defect). Round-56 falsify seats: `ReviewRowsS395toS397.md`, `ReviewRowsS398toS400.md`, `CriticClaimC56.md`, `ReviewSectionsObjectsDress.md`, `ReviewSectionsCapitalKinFaith.md`, `ReviewGateLines56.md`.

Method: each source re-opened this session by ordinary means only — S396 from the live Met page and from its recorded Wayback capture `20230529091312id_` (HTTP 200, 204,151 bytes); S397 from the live Cleveland open-access API (HTTP 200, 8,764 bytes); S399 from its recorded Wayback capture `20260314181520id_` (HTTP 200, 232,310 bytes) and live Met page. Text read from the raw served bytes; every quote below was located with the round-57 locator `python3 -B reports/round-57/reopen-quote.py '<url>' '<quote>'` and its one-line output is pasted. Scratch: `/fast/scratch/hyaku/kotodama-r57/ReviewCarriedS396S399/`. No tool installs. No lane writes except this report.

## S396 — two findings

### S396-a (registry anchor cell): the "Knots and the act of tying" anchor is in the essay's **third** paragraph, not the fourth — VERDICT: AGREE

Re-opened evidence: the recorded capture `20230529091312id_` serves the object's intro description as one `<p>` with `<br/><br/>` block separators. The served blocks (verbatim):

1. "This work was the product of an intense collaboration between a sculptor and the initiated priest "nganga," who controlled its use in his professional practice. After an artist completed carving the artifact, … The term "nkisi" may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, as well as the carved wood sculptures studied by art historians. …"
2. "Among the many amulets and bound bundles attached to this "nkisi," … The cross alludes to the division between the land of the living and the land of the dead …"
3. "Cloth and tied bundles, like those seen in abundance on this "nkisi," have multiple interpretations. **Knots and the act of tying are associated with the binding and capturing of a spirit.** …"

So the fourth anchor sentence sits in the third block ("Cloth and tied bundles"), exactly as `ReviewRowsS395toS397.md` found. The registry anchor cell (`corpus/SOURCES.md:425`, column 7) labels it `essay, fourth paragraph`; that cell is wrong and the registry is append-only → a superseding row is drafted below.

Locator lines (paste as filed evidence):

- `python3 -B reports/round-57/reopen-quote.py 'https://www.metmuseum.org/art/collection/search/312342' 'This work was the product of an intense collaboration between a sculptor and the initiated priest'` → `LOCATED https://www.metmuseum.org/art/collection/search/312342`
- `python3 -B reports/round-57/reopen-quote.py 'https://www.metmuseum.org/art/collection/search/312342' 'Knots and the act of tying are associated with the binding and capturing of a spirit.'` → `LOCATED https://www.metmuseum.org/art/collection/search/312342`
- `python3 -B reports/round-57/reopen-quote.py 'https://www.metmuseum.org/art/collection/search/312342' 'may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels'` → `LOCATED https://www.metmuseum.org/art/collection/search/312342`

(Note: plain `curl` gets HTTP 429 from the Met's checkpoint; the locator's plain GET with retries succeeded on the same live URL, so the live page serves the essay text. The Wayback capture `20230529091312id_` also serves the same text; the second locator run on that capture id failed with a transient URLError, not a quote absence.)

### S396-b (entry over-read at kongo-kingdom.md:89): the hedge "may relate to" was stripped — VERDICT: AGREE

Current entry (`corpus/knowledge/civilizations/kongo-kingdom.md:89`):

- old: `The Met says the term covers cloth packets and filled vessels as well as carved wood (S396, essay, first paragraph).`
- new: `The Met says the term nkisi may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, as well as carved wood sculptures (S396, essay, first paragraph).`

The served first paragraph says "The term "nkisi" may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, as well as the carved wood sculptures studied by art historians." The old sentence drops the "may relate to" hedge and says "covers"; the replacement restores the source's strength.

## S397 — one finding (entry over-read at kongo-kingdom.md:97): object date range narrowed — VERDICT: AGREE

Current entry (`corpus/knowledge/civilizations/kongo-kingdom.md:97`):

- old: `a late-1800s cap by a maker possibly Yombe`
- new: `an object dated late 1800s–early 1900s by a Kongo-style maker, possibly Yombe`

Re-opened evidence (live Cleveland API, object 159880, HTTP 200): `creation_date` = `late 1800s–early 1900s`; culture = `Kongo-style maker, possibly Yombe subgroup`; tombstone = "Prestige Cap (mpu ngola), late 1800s–early 1900s. Africa, Central Africa, Democratic Republic of Congo, Republic of Congo, or Cabinda (Angola), Kongo-style maker, possibly Yombe subgroup. …"

Locator line:

- `python3 -B reports/round-57/reopen-quote.py 'https://openaccess-api.clevelandart.org/api/artworks/159880' 'Prestige Cap (mpu ngola), late 1800s–early 1900s. Africa, Central Africa, Democratic Republic of Congo, Republic of Congo, or Cabinda (Angola), Kongo-style maker, possibly Yombe subgroup'` → `LOCATED https://openaccess-api.clevelandart.org/api/artworks/159880`

(the API serves tombstone text without inline markup; the description anchors contain `<em>` tags whose escaped form blocks exact normalized matching in the locator, so the tombstone is the correct locateable quote.)

## S399 — two findings

### S399-a (entry over-read at kongo-kingdom.md:84): already resolved in the base entry — VERDICT: AGREE with the original finding; no further entry change required except the locator correction in S399-b

The round-56 finding `ReviewRowsS398toS400.md` flagged plural over-read "Staffs topped by Saint Anthony of Padua served as insignia of office". The base entry (`corpus/knowledge/civilizations/kongo-kingdom.md:84`) already reads singular and scoped: `A Kongo chief's staff topped by Saint Anthony of Padua, held by the Met, served as an insignia of office (S399, Overview label, object 318318).` The carried fix landed in the round-56 closure (`c8af23f`), consistent with the round-56 lesson §4 "the falsify fixes from six critics landed in c8af23f". No over-read remains.

### S399-b (registry citation cell at corpus/SOURCES.md:428): "object number 318318" is wrong — VERDICT: AGREE

The served record (Wayback capture `20260314181520id_`) shows `Object Number: 1999.295.2` and title "Staff with Saint Anthony of Padua" with artist "Kongo artist"; `318318` is the collection-search record id, not the Met object number. Registry cell `corpus/SOURCES.md:428` column 3 currently reads `"Staff with Saint Anthony of Padua," object number 318318, Kongo artist` — wrong cell, append-only → superseding row drafted below. The two anchor locators `Overview label, object 318318` are corrected to `Overview label, record 318318` in the same row (entry locator corrected in the entry line below, and the round-56 lesson line 64 gets an erratum companion, filed bytes untouched).

Entry locator fix (`corpus/knowledge/civilizations/kongo-kingdom.md:84`):

- old: `(S399, Overview label, object 318318)`
- new: `(S399, Overview label, record 318318)`

Locator lines (paste as filed evidence):

- `python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318' 'Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief.'` → `LOCATED https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318`
- `python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318' 'At its summit is a brass pendant of St. Anthony of Padua, one of the most beloved saints in Kongo Christianity'` → `LOCATED https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318`
- `python3 -B reports/round-57/reopen-quote.py 'https://www.metmuseum.org/art/collection/search/318318' 'Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief.'` → `LOCATED https://www.metmuseum.org/art/collection/search/318318`

## Drafted superseding rows (11 columns; id left as S4xx for the L1; `teaches` opens `supersedes S### — `; same URLs and anchor quotes as the superseded rows so FRESH is unaffected; status/recheck/used-by carried)

### S4xx (supersedes S396) — anchor locator correction only

```
| S4xx | The Metropolitan Museum of Art. *Male Power Figure (Nkisi)*, late 19th–mid-20th century, Kongo peoples, Democratic Republic of the Congo; artist credited as Kongo artist and nganga. Object record 312342, accession 1979.206.127. — https://www.metmuseum.org/art/collection/search/312342 (Wayback capture 20230529091312 (HTTP 200, 54,094 bytes), object essay and detail fields read.) | docs | A | what the word nkisi covers, the nganga's role, the crossroads cross and its double reading, and binding and cloth as technique and payment. (tier note: A — the holding museum's record and essay for this exact object; authoritative for the Met's description.) | essay, first paragraph: "This work was the product of an intense collaboration between a sculptor and the initiated priest"; essay, first paragraph: "may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels"; essay, second paragraph: "The cross alludes to the division between the land of the living and the land of the dead"; essay, third paragraph: "Knots and the act of tying are associated with the binding and capturing of a spirit." | supersedes S396 — The Met describes nkisi as a class of receptacles activated by an nganga, with binding knots, cloth offerings and a crossroads cross carrying spirit and transaction. | mined | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Gate line (for the L1's lesson table; locator line below):

```
- S4xx — https://www.metmuseum.org/art/collection/search/312342 — accessed 2026-10-22 — essay, first paragraph: "This work was the product of an intense collaboration between a sculptor and the initiated priest". Grounds: supersedes S396 — The Met describes nkisi as a class of receptacles activated by an nganga, with binding knots, cloth offerings and a crossroads cross carrying spirit and transaction. Seat: ReviewCarriedS396S399.
```

### S4xx (supersedes S399) — citation-cell object number and anchor locator corrections

```
| S4xx | The Metropolitan Museum of Art. No date printed. "Staff with Saint Anthony of Padua," object record 318318, object number 1999.295.2, Kongo artist, 19th century, brass, wood and iron; Gift of Ernst Anspach, 1999. Collection record. — https://www.metmuseum.org/art/collection/search/318318 (live page returned HTTP 429 behind a Vercel Security Checkpoint (challenge met, not passed); record read from Wayback capture 20260314181520id_ of the same URL, HTTP 200, 50,167 bytes; access date 2026-10-22) | docs | A | the prestige staff as an insignia of office held by a Kongo chief, its brass Saint Anthony pendant and the saint's attributes, and the museum's identification of Saint Anthony as one of the most loved saints in Kongo Christianity. (tier note: A — the holding museum's own record and gallery label for the object it holds.) | Overview label, record 318318: "Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief."; Overview label, record 318318: "At its summit is a brass pendant of St. Anthony of Padua, one of the most beloved saints in Kongo Christianity." | supersedes S399 — A Kongo prestige staff is an insignia of office topped with a brass Saint Anthony, joining religious and secular authority in one carried object. | mined | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Gate line (for the L1's lesson table; locator line below):

```
- S4xx — https://www.metmuseum.org/art/collection/search/318318 — accessed 2026-10-22 — Overview label, record 318318: "Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief.". Grounds: supersedes S399 — A Kongo prestige staff is an insignia of office topped with a brass Saint Anthony, joining religious and secular authority in one carried object. Seat: ReviewCarriedS396S399.
```

## Residual risk and verification gaps

- S396's paragraph numbering is from the recorded Wayback capture's served blocks (`<br/><br/>` separators inside the intro `<p>`); the live page serves the same text (three locator runs confirmed) but the capture is the row's recorded route, and my count is the one the finding used.
- S399's live Met page answers HTTP 429 to plain `curl`; the locator's GET succeeded and located the first anchor on the live URL, and both anchors are located on the recorded capture — the live 429 is recorded as challenge met, not passed, matching the row's note.
- The S397 description anchors contain `<em>` markup; the locator cannot match quotes crossing escaped tags in the JSON body, so the tombstone quote (contains the date and culture exactly) is the evidence quote. The anchors themselves were already carried by round-56 `ReviewRowsS395toS397.md`.
- Advisory: the S396 teaches cell (and hence the lesson Grounds) still states "as a class of receptacles" while the served text hedges "may relate to a wide spectrum of physical receptacles". The carried finding did not flag the teaches cell; if the L1 wants the hedge at row level too, it can prepend the same hedge to the teaches of the S4xx row above (same text as the entry fix). Not part of this seat's finding set.
- The round-56 lesson lines 61 (S396 gate locator "fourth paragraph") and 64 (S399 "object 318318") carry the same stale labels; per §5 item 3's erratum convention those filed bytes get appendix errata, which I do not write.

No further actionable finding in scope: all three named rows checked against served text, verdicts given, exact fixes drafted (entry lines 89, 97, 84 + two superseding rows + Gate lines with locator lines).
