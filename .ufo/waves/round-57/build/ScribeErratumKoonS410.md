# ScribeErratumKoonS410 — routed defects 3 and 4

Axes: **coverage** (source access and non-duplicative registry evidence) and **calibration** (correcting the koon1244 rationale and reporting current S410 access exactly).

## Findings

### 1. koon1244 was quotable; omission was redundancy

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-56.md:83` records: `not registered: its only quotes are RDF triples with no quotable passage`. Do not rewrite that filed line.
- Opened both serializations by ordinary GET: `.json` returned HTTP 200, 4,774 bytes, `application/json`; `.n3` returned HTTP 200, 28,017 bytes, `text/n3; charset=utf-8`. The JSON includes `"level": "language"`, `"name": "South-Central Koongo"`, and the classification chain includes `kiko1235`; S379 at `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:408` already covers the Kikongo Language Cluster classification. No koon1244 URL was found in `SOURCES.md` (`functions.grep`: no matches).
- Ordinary-GET commands and outcomes:
  - `curl -sS -o /dev/null -w 'HTTP %{http_code}; bytes %{size_download}; content-type %{content_type}\n' 'https://glottolog.org/resource/languoid/id/koon1244.json'` → `HTTP 200; bytes 4774; content-type application/json`.
  - `curl -sS -o /dev/null -w 'HTTP %{http_code}; bytes %{size_download}; content-type %{content_type}\n' 'https://glottolog.org/resource/languoid/id/koon1244.n3'` → `HTTP 200; bytes 28017; content-type text/n3; charset=utf-8`.
  - `functions.grep(pattern='glottolog\.org/resource/languoid/id/koon1244', path='/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md')` → `No matches found`.
- Exact correction: `not registered: its only quotes are RDF triples with no quotable passage` → `not registered because the relevant Kikongo Language Cluster classification is already represented by S379; the opened JSON and N3 records do contain quotable fields.`
- Locator quote (8 whitespace-delimited words): `gold:Language ; rdfs:label "South-Central Koongo"@en ; lexvo:iso639P3PCode "kng"^^xsd:string`
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://glottolog.org/resource/languoid/id/koon1244.n3' 'gold:Language ; rdfs:label "South-Central Koongo"@en ; lexvo:iso639P3PCode "kng"^^xsd:string'`
  - `LOCATED https://glottolog.org/resource/languoid/id/koon1244.n3`
- Draft round-57 lesson erratum line (filed round-56 bytes unchanged):
  ```text
  - Erratum to round-56.md:83 (filed bytes unchanged): Glottolog koon1244 was opened in .json and .n3 and contains quotable fields, including `gold:Language ; rdfs:label "South-Central Koongo"@en ; lexvo:iso639P3PCode "kng"^^xsd:string`. It was left unregistered because its relevant Kikongo Language Cluster classification is already represented by S379, not because it lacked a quotable passage.
  ```

### 2. S410 direct content route and superseding row

- Existing row: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:439`; filed Gate line: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-56.md:75`.
- Exact URL correction: `https://open.bu.edu/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/download` → `https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content`.
- Current ordinary GET evidence:
  - `curl -sS -D - -o /dev/null -w '\nFINAL %{url_effective}; HTTP %{http_code}; bytes %{size_download}; content-type %{content_type}\n' 'https://open.bu.edu/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/download'` → HTTP 302, 113 bytes, `text/plain; charset=utf-8`; `Location` is the effective `/server/api/core/bitstreams/.../content` URL.
  - `curl -sS -D - -o /dev/null -w '\nFINAL %{url_effective}; HTTP %{http_code}; bytes %{size_download}; content-type %{content_type}\n' 'https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content'` → HTTP 200, 487,698 bytes, `application/pdf;charset=UTF-8`.
  - Following the old URL with `curl -sS -L -o /dev/null -w 'HTTP %{http_code}; bytes %{size_download}; content-type %{content_type}\n' 'https://open.bu.edu/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/download'` → HTTP 200, 487,698 bytes, `application/pdf;charset=UTF-8`.
- **Conflict with recorded observations:** the assignment says the `/download` URL now serves an HTML shell, and round-56 spot-check §3 records a 755-byte shell. The S410 registry row still describes a direct HTTP 200 PDF response of 487,689 bytes. This session's plain curl instead observed HTTP 302, 113-byte `text/plain` with a direct API `Location`; following it served the PDF at HTTP 200, 487,698 bytes. No HTML shell was observed in these GETs; retain both the earlier observation and this current result.
- S410 Gate quote locator on the effective URL:
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content' 'traditions of origin in Kongo changed much more substantially over time.'`
  - `LOCATED https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content`
- Additional S410 locator commands and exact outcomes:
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content' 'I proposed that the “origin of Kongo” should be reconceptualized as the “conquest of Mpemba.”'` → `LOCATED https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content`.
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content' 'They were not, as Cuvelier had originally proposed, ancient entities that existed before Kongo emerged.'` → `LOCATED https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content`.
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content' 'These two accounts represent constitutional statement that evolved alongside the kingdom itself.'` → `NOT_LOCATED https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content quote-absent`.
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content' 'These two accounts rep- resent constitutional statement that evolved alongside the kingdom itself.'` → `NOT_LOCATED https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content quote-absent`.
- Two of the three remaining S410 anchor quotes located on the effective URL (p. 6 Mpemba; p. 8 kanda); the exact commands and outcomes are above. The other p. 2 anchor quote, `These two accounts represent constitutional statement that evolved alongside the kingdom itself.`, returned `NOT_LOCATED https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content quote-absent`; the page-extracted `rep- resent` spelling also returned `quote-absent`. Omitted from the proposed row rather than silently carried forward.

Draft replacement row (11 columns; `S4xx` reserved for L1 assignment; status queued):

```text
| S4xx | Thornton, John. 2025. "The Emergence of Social and Political Complexity in West Central Africa." *The Journal of African History* 66: e25, 1–16. DOI 10.1017/S0021853725100662. Open access, CC BY 4.0. Boston University OpenBU handle 2144/52852. — https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content (direct GET 2026-10-22: HTTP 200, 487,698 bytes, application/pdf;charset=UTF-8; the former /bitstreams/.../download route redirects here with HTTP 302) | paper | A | Thornton's revised origin thesis (conquest of an older Mpemba), changing origin narratives as constitutional statements, Kongo titles and settlement terms, and the late date of kanda clans. | p. 2, historiography: "traditions of origin in Kongo changed much more substantially over time."; p. 6: "I proposed that the “origin of Kongo” should be reconceptualized as the “conquest of Mpemba.”"; p. 8: "They were not, as Cuvelier had originally proposed, ancient entities that existed before Kongo emerged." | supersedes S410 — effective URL: https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content; directs readers to Thornton's account of Kongo's changing origin traditions and its Mpemba conquest thesis. | queued | 2026-10-22 | 365d | — |
```

Draft round-57 Gate line (Grounds matches the row's `teaches` cell):

```text
- S4xx — https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content — accessed 2026-10-22 — p. 2, on the historiography of origin traditions: “traditions of origin in Kongo changed much more substantially over time.” Grounds: supersedes S410 — effective URL: https://open.bu.edu/server/api/core/bitstreams/ad5455af-f3b2-49ec-bedb-b4dd9b15d3af/content; directs readers to Thornton's account of Kongo's changing origin traditions and its Mpemba conquest thesis. Seat: ScribeErratumKoonS410.
```

## Gates, surfaces, and limits

- Passed only the live source-locator calls quoted above and ordinary GETs. No ACCEPT-C-57 / ACCEPT-O-57 claim gates, builds, tests, or lint runs were performed.
- Read surfaces: `corpus/lessons/round-56.md:83`, `corpus/lessons/round-56-verifier-spotcheck.md:129,163-164`, `corpus/SOURCES.md:408,439`, and `reports/round-57/reopen-quote.py`.
- Wrote only this report. No product code, lesson, or registry row was edited; no source was registered. No browser, access-control bypass, install, or other runtime was used.
- Artifact: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-57/build/ScribeErratumKoonS410.md`.
