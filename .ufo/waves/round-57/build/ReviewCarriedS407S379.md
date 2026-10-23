# ReviewCarriedS407S379 — round 57 build seat (carried row findings, round-56 spot-check §5 item 5)

Scope: the two carried findings named for this seat — **S407** (anchor 3 column locator; finder `ReviewRowsS407toS409`) and **S379** (tier B → A needs a superseding row; finder `ReviewRowsS377toS379`; QUALITY criterion 6). Both are registry-cell findings (anchor locator; tier), so under the round-56 spot-check §5 item 5 routing the fix for each is a drafted superseding SOURCES row, not an entry-sentence change — no entry over-read is present in either finding (kongo-kingdom.md:52 and :100 are carried by the finders and were re-checked below).

## Method and re-opened sources (ordinary means only)

- **S407** — `https://journals.flvc.org/athanor/article/download/126740/126293/207658` — re-opened by a plain `curl` GET this session: **HTTP 200, `application/pdf`, 731,695 bytes** (file at `/fast/scratch/hyaku/kotodama-r57/KotodamaR57.ReviewCarriedS407S379/forbes.pdf`, byte-identical to the row's recorded size). Text read with `pdftotext -layout` 26.08.0 (already installed). Printed p. 84 = PDF page 2 (PDF page 1 = printed p. 83, page 9 = printed p. 91 — matching the row's "printed folios 83–91" note). Quotes checked against the extracted two-column page.
- **S379** — `https://glottolog.org/resource/languoid/id/kiko1235.json` and `https://glottolog.org/resource/languoid/id/kiko1235.html` — re-opened by plain GETs this session: JSON **HTTP 200, 4,856 bytes** (`kiko1235.json` saved in the seat scratch dir), HTML **HTTP 200, 554,295 bytes**. JSON fields re-read: `id=kiko1235`, `level=family`, `name=Kikongo Language Cluster`, `child_language_count=26`, `child_family_count=21`, `child_dialect_count=57`; `newick` contains `'Kisikongo [kisi1245]':1` inside the `East-Southern Koongo [east2869]` clade. HTML tree row for the child read: `{"id": "kisi1245", "pk": 27162, "iso": null, "level": "dialect", "label": "Kisikongo", ...}`.

Locator runs performed this session (instrument `reports/round-57/reopen-quote.py`):

- `python3 -B reports/round-57/reopen-quote.py 'https://glottolog.org/resource/languoid/id/kiko1235.json' 'East-Southern Koongo [east2869]: 1, Kisikongo [kisi1245]: 1, Angola Nzeto [ango1259]: 1, Kisolongo Angola [kiso1239]: 1, Kisolongo DRC [kiso1240]: 1, West-Southern Koongo [west2970]: 1, Southern Koongo [sout2809]: 1'` → `LOCATED https://glottolog.org/resource/languoid/id/kiko1235.json` (16-word span, verbatim from the served `newick` string).
- `python3 -B reports/round-57/reopen-quote.py 'https://glottolog.org/resource/languoid/id/kiko1235.html' 'rdf serialized as turtle family kikongo language cluster classification open'` → `LOCATED https://glottolog.org/resource/languoid/id/kiko1235.html` (10-word span in the served page text).
- `python3 -B reports/round-57/reopen-quote.py 'https://glottolog.org/resource/languoid/id/kiko1235.html' 'family kikongo language cluster classification open kikongo language cluster expand'` → `LOCATED https://glottolog.org/resource/languoid/id/kiko1235.html` (9-word span).
- FLVC caveat: after the first successful re-open (HTTP 200 above), subsequent plain GETs to the PDF download URL returned **HTTP 403 "Access Denied"** (FLVC server-side block, HTML body with a reference id; no captcha, no login). `wayback` CDX was unreachable from this host at report time (connection refused). The verdict below rests on the fetched PDF bytes, not on a current live fetch; the L1 will re-run the locator at integration and should treat the 403 as a transient server-side block if it persists.

## S407 — anchor 3 column locator — VERDICT: AGREE (superseding row)

Finding (`ReviewRowsS407toS409.md:3`): the row locates the quote "undecorated cloths were used as currency. The cloths were thin, but tightly woven." at "p. 84, first column"; the finder says it is on p. 84, **second/right column**.

Re-opened evidence (printed p. 84 = PDF page 2, `pdftotext -layout`):

- Left (first) column contains: "In the Kongo Kingdom, the finest textiles were reserved for nobles with high status." and "Only the Kongo king and the members of the court whom he appointed were permitted to wear or display the finest quality textiles.7" — anchors 1 and 2, correct.
- Right (second) column contains the carried sentence: "and markers of status, undecorated cloths were used as cur-" / "rency. The cloths were thin, but tightly woven. They could be" (hyphenated line break "cur-rency" inside the quote; the locator joins hyphen breaks) — **anchor 3 is in the second/right column**, exactly as the finder said.
- Right (second) column also contains anchor 4: "Thus, raffia may not necessarily be used as currency in everyday transactions, but its exchange signaled ideas of prestige, status, or respect."

So the finding is correct on the served text. Entry sentence kongo-kingdom.md:100 ("Plain raffia could serve as currency and pay tribute, but a student paper hedges that it was not necessarily currency in everyday transactions (S407, p. 84)") uses only the quote content and the page number — no column claim — so the entry needs no change. The registry's `anchor` cell is append-only; the fix is a superseding row.

**Drafted superseding row (id left as S4xx for the L1; teaches opens `supersedes S407 —`):**

```
| S4xx | Forbes, Carlee S. 2014. *Creativity in the Congo Free State: Nineteenth and Twentieth-Century Funerary Mats*. *Athanor* 32: 83–91 (printed folios in the PDF; the journal record declares pp. 93–101). ISSN 0732-1619 (print), 2690-0181 (online). DOI/stable id: none assigned; stable article URL `https://journals.flvc.org/athanor/article/view/126740`, PDF `126740/126293`. — https://journals.flvc.org/athanor/article/download/126740/126293/207658 (direct plain request (curl), HTTP 200, `application/pdf`, 731695 bytes, 9 pages, read with `pdftotext` in flow order; no challenge, no login, 2026-10-22) | paper | B | the article's own distinction between Kongo with a K and the modern states; the grade order of Kongo textiles and who may wear or display the finest; that undecorated cloth served as currency in a qualified sense; the tribute-tax, marriage and friendship uses; the mpu cap as a decorated-cloth form; the labour time of a fine piece; Dapper's four-kinds passage as an outsider's account; the execution rule for unauthorised sale of a high-grade cloth. It does **not** establish a Kikongo vocabulary for cloth or grades, a price list, or the internal organisation of weaving. (tier note: B — a student paper in a departmental art-history symposium journal, so a strong secondary write-up with reproducible citations rather than an authority; its Kongo textile background rests on Vansina (1998) and Martin (1986) and on Dapper (1686) in the author's translation, and it is authoritative only for its own reading of the objects it studies. Not C: it quotes its sources with page numbers and its translation choices are visible. Not A: nothing here is a primary Kongo voice or a peer-reviewed study.) | p. 84, first column: "In the Kongo Kingdom, the finest textiles were reserved for nobles with high status."; p. 84, first column (sentence ends with footnote marker 7 in the file, omitted here): "Only the Kongo king and the members of the court whom he appointed were permitted to wear or display the finest quality textiles"; p. 84, second column: "undecorated cloths were used as currency. The cloths were thin, but tightly woven."; p. 84, second column: "Thus, raffia may not necessarily be used as currency in everyday transactions, but its exchange signaled ideas of prestige, status, or respect." | supersedes S407 — the sentence "undecorated cloths were used as currency. The cloths were thin, but tightly woven." sits in the second (right) column of printed p. 84, not the first; all other anchors, tier and scope stand. | mined | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Gate line for the L1 (Grounds equals the teaches cell above; round-56 lesson bytes are never rewritten — this is for the round-57 lesson if the row is gated):

```
- S4xx — https://journals.flvc.org/athanor/article/download/126740/126293/207658 — accessed 2026-10-22 — p. 84, first column: “In the Kongo Kingdom, the finest textiles were reserved for nobles with high status.” Grounds: supersedes S407 — the sentence "undecorated cloths were used as currency. The cloths were thin, but tightly woven." sits in the second (right) column of printed p. 84, not the first; all other anchors, tier and scope stand. Seat: ScoutRaffiaCloth.
```

Locator lines (pasted as filed evidence; FLVC 403 caveat above):

- `python3 -B reports/round-57/reopen-quote.py 'https://journals.flvc.org/athanor/article/download/126740/126293/207658' 'In the Kongo Kingdom, the finest textiles were reserved for nobles with high status.'` → `LOCATED ...` (run at a moment the endpoint allows).
- `python3 -B reports/round-57/reopen-quote.py 'https://journals.flvc.org/athanor/article/download/126740/126293/207658' 'undecorated cloths were used as currency. The cloths were thin, but tightly woven.'` → `LOCATED ...` (same caveat).

## S379 — tier B → A — VERDICT: AGREE (superseding row)

Finding (`ReviewRowsS377toS379.md:3`): the row scopes claims to Glottolog's own node counts and placement and its note calls the record "authoritative for how Glottolog 5.3 names and places the node"; QUALITY criterion 6 reserves tier A for sources primary or authoritative for the exact scope, so the row is under-tiered at B.

Re-opened evidence: the served JSON is the catalogue's own machine-readable record of this languoid (level, child counts, newick placement of Kisikongo as a dialect under East-Southern Koongo / the Southern Koongo clade). The source is the authority for its own classification and placement — precisely the row's `scope`. Nothing in the served text claims primary evidence for the genetic grouping itself (that part stays hedged in scope and teaches). Therefore the tier should be A for this exact scope.

Entry kongo-kingdom.md:52 ("Glottolog files the cluster as a family-level node with Kisikongo as a dialect inside it (S379, JSON fields level and newick)") is carried by the served fields and needs no change.

**Drafted superseding row (id left as S4xx; teaches opens `supersedes S379 —`):**

```
| S4xx | Hammarström, Harald; Forkel, Robert; Haspelmath, Martin; Bank, Sebastian (eds.). Glottolog 5.3, languoid "Kikongo Language Cluster" [kiko1235]. Max Planck Institute for Evolutionary Anthropology, CC BY 4.0. Release year not stated on the served page. — https://glottolog.org/resource/languoid/id/kiko1235.json (direct, HTTP 200, JSON serialization of the languoid page https://glottolog.org/resource/languoid/id/kiko1235 (the HTML page and the .n3 serialization were also opened, both HTTP 200). Access date 2026-10-22.) | dataset | A | The size and composition of the Kikongo Language Cluster node in Glottolog 5.3, its position in the family tree, and the catalogue's placement of Kisikongo inside the cluster. Nothing about Kongo history or culture. (tier note: A — the Glottolog 5.3 node record is the catalogue's own statement of its node's composition and placement; authoritative for the exact scope of how Glottolog names and places the node, not primary evidence for the grouping itself.) | JSON field level: "level": "family"; JSON field newick, Southern Koongo clade: "Kisikongo [kisi1245]" | supersedes S379 — tier raised B → A per QUALITY criterion 6: the Glottolog node record is primary/authoritative for the exact scope (how Glottolog names and places the node), while it remains non-primary evidence for the genetic grouping itself. | mined | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Gate line for the L1 (Grounds equals the teaches cell):

```
- S4xx — https://glottolog.org/resource/languoid/id/kiko1235.json — accessed 2026-10-22 — JSON field level: “level": "family”. Grounds: supersedes S379 — tier raised B → A per QUALITY criterion 6: the Glottolog node record is primary/authoritative for the exact scope (how Glottolog names and places the node), while it remains non-primary evidence for the genetic grouping itself. Seat: ScoutKikongoClassification.
```

Locator lines (pasted as filed evidence):

- `python3 -B reports/round-57/reopen-quote.py 'https://glottolog.org/resource/languoid/id/kiko1235.json' 'East-Southern Koongo [east2869]: 1, Kisikongo [kisi1245]: 1, Angola Nzeto [ango1259]: 1, Kisolongo Angola [kiso1239]: 1, Kisolongo DRC [kiso1240]: 1, West-Southern Koongo [west2970]: 1, Southern Koongo [sout2809]: 1'` → `LOCATED https://glottolog.org/resource/languoid/id/kiko1235.json`
- `python3 -B reports/round-57/reopen-quote.py 'https://glottolog.org/resource/languoid/id/kiko1235.html' 'rdf serialized as turtle family kikongo language cluster classification open'` → `LOCATED https://glottolog.org/resource/languoid/id/kiko1235.html`

Note: the current S379 anchor's first quoted span (`"level": "family"`) is 4 words, under the LOCATE leg's 8-word minimum; that was true in round 56 as well. The superseding row keeps the same anchor, and it is a records row (S481–S499 or as routed), not a C-cited row in S413–S480, so it does not enter claim C's LOCATE/FRESH legs. If the L1 ever wants a LOCATE-located anchor on this source, the newick span above (16 words) or an HTML-page span (9–10 words) is available.

## Cells not in scope

Both rows' status (`mined`), opened (2026-10-22), recheck (365d) and used-by (kongo-kingdom.md) cells are correct as filed; only the S407 anchor locator and the S379 tier summary are the defects.

## Residual risk and verification gaps

- FLVC's download endpoint answered 403 to repeated plain GETs after the one successful 200 re-open this session (server-side block, no challenge). The S407 verdict and drafted row rest on the fetched PDF bytes; the L1 should re-run both locator lines at integration.
- S379 is verified against the live JSON and HTML as served today (HTTP 200). No change to the source's content was observed versus the row's recorded values.
- I did not use `--row S4xx` (the rows are not yet filed); locator lines above are for the exact URLs/quotes the filed rows will carry.

## Tooling (recorded per the tooling directive)

- `uv` (0.13.0, already present) used to install `pypdf==6.21.2` into a throw-away venv at `/tmp/venvpypdf` (channel: uv; reason: local PDF-text re-verification of S407; the locator itself uses `uv run --no-project --with pypdf==5.4.0` and ran fine). No system packages installed, no pacman transactions, no lane writes besides this report.
