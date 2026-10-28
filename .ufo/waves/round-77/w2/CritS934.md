# CritS934 — Attack on the S934 "misdescribed duplicate" refusal

## Scope

Named item: the refusal of S934 (`naming-systems.amend-2026-10-24.md`, staged row
`/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` line 82), refused per
CLAIMS-DRAFT line 19 as "misdescribed duplicate D2 S934 — the captured PDF is Kałużyńska, not
the staged Słon Poland title". W1 grounding: `w1/ScoutIdMap.md` (live-URL fetch) and
`w1/ScoutHeldEntries.md` (Wayback unwrap; flip condition "S934 is a different document than D2").

Attack plan: the W1 byte-level check fetched only the *live* URL, but the row explicitly stages a
**Wayback capture** (`…/web/20251231111748id_/…`) and asserts "the live article path no longer
serves this text; the archived capture does". If the capture actually serves the Słon paper, the
"misdescribed duplicate" reason is false on the tested URL and the refusal's core evidence fails.

## Verdict: counterexample FAILED — refusal stands, corroborated on the exact staged artifact

The staged Wayback capture itself serves the **Kałużyńska PDF** — the same D2 document.
The refusal's stated reason is verified directly on the artifact the row names, not merely on the
live URL it marks "withdrawn".

### Byte evidence

| fetch | size | sha256 | identity |
|---|---|---|---|
| staged capture `https://web.archive.org/web/20251231111748id_/https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/` | 546,440 B | `1b4c60f2…8a2ff9` | Kałużyńska, DOI `10.17651/ONOMAST.69.7`, *Onomastica* LXIX 2025, "FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA" |
| live `https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/` | 417,093 B | `5d1bfa5a…8d29bc` | identical first-page block, same DOI/title; `pdfinfo` Author "Irena Kałużyńska", Title "Onomastica 69_07" |

Both PDFs: 13 pages, same DOI, same title block; `diff` of full text = 290 changed lines, all
cosmetic (opening-quote glyph `‘`→`‛`, line reflows, `p. 77`→`p.77` style, minor typo fixes).
The live galley is a regenerated revision (CreationDate 2026-03-23) of the **same article**
— same document, later version. OJS landing page `article/view/574` metadata:
`citation_title` "Flowers, plants and trees in female naming in China",
`citation_author` "Irena Kałużyńska", `citation_doi` "10.17651/ONOMAST.69.7",
`citation_pdf_url` = the same `/download/574/763` path.

### Sharpenings the refusal record should carry (no disposition flip)

1. **Row's "withdrawn original" claim is false**: the live path still serves the same article
   (newer galley revision). Both CDX captures of the URL (2025-12-31 and 2026-09-01) returned
   HTTP 200 `application/pdf` — the article was never swapped for the described Słon paper.
2. **The row's own located quote convicts it**: the staged «standard given names with lexemes
   reflecting feminine softness and female aesthetic associations» span is verbatim inside the
   Kałużyńska payload (extracted line ~145: "According to Kałużyńska (2008, pp. 160, 222) …
   'female aesthetic values'"), in a passage **about Chinese names**, not Poland. The row's
   embedded recheck (`curl … | pdftotext | grep -c 'standard given names…'` → expects 1)
   therefore self-verifies on the wrong document — an independent misdescription proof that
   does not depend on bibliographic identity at all. (Row also misquotes "values" as
   "associations".)
3. **The described document does not exist as cited**: Crossref query `author="Słoń"` over ISSN
   0078-4648 → total-results 0; title search for "Names and the named: gender, femininity and
   given names in Poland" → no hit anywhere. The real near-match is **Adam Siwiec**, "Personal
   names in Polish in relation to gender / Imiona osobowe w polszczyźnie wobec kategorii płci",
   *Onomastica* 68 (2024), DOI `10.17651/ONOMAST.68.5`, OJS article/view/**498** — a *different
   URL* than the one staged. So the row is not a fixable wrong-URL row: even replacing the URL
   with Siwiec's would orphan the quoted span, which belongs to Kałużyńska.

### Fixable defect vs judge-rejectable

No counterexample survives. The refusal is factually correct on the strongest test available
(the exact staged capture bytes). The only nit is evidentiary completeness: W1's byte check
targeted the live URL rather than the staged capture; this report closes that gap with the
capture itself — the outcome is unchanged. The DRAFT flip precondition ("S934 is a different
document than D2") is disproved; the refusal as written requires no correction.

## Impacted axes

GROUND / REJECTS / CITEDLINES / GATE: unchanged — attack yields no counterclaim. Evidence added:
capture-byte identity (sha256 above), row-quote-in-payload overlap, nonexistence of the cited
Słon record in Crossref.

## Raw commands (all run from `/fast/scratch/hyaku/kotodama-r77/CritS934`, since deleted)

```
curl -sSL -D s934-wayback.headers -o s934-wayback.bin -w 'HTTP %{http_code} | %{size_download}B | %{content_type} | final=%{url_effective}\n' --max-time 120 \
  'https://web.archive.org/web/20251231111748id_/https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/'
  → HTTP 200 | 546440B | application/pdf

curl -sSL -D s934-live.headers -o s934-live.bin -w 'HTTP %{http_code} | %{size_download}B | %{content_type} | final=%{url_effective}\n' --max-time 120 \
  'https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/'
  → HTTP 200 | 417093B | application/pdf

curl -sSL 'http://web.archive.org/cdx/search/cdx?url=onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/&output=text&limit=50'
  → 2 captures: 20251231111748 (200, pdf, 426128 compressed) and 20260901045105 (200, pdf, 406446 compressed)

pdftotext -f 1 -l 1 s934-wayback.bin -   → "https://doi.org/10.17651/ONOMAST.69.7 / Onomastica LXIX, 2025 / IRENA KAŁUŻYŃSKA / FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA"
pdftotext -f 1 -l 1 s934-live.bin -     → identical block
pdfinfo s934-*.bin                      → both 13 pages, Adobe PDF Library 17.0; live CreationDate 2026-03-23, Author "Irena Kałużyńska"
diff wb.txt lv.txt                      → 290 changed lines, all cosmetic

curl -sSL 'https://onomastica.ijppan.pl/index.php/ONOM/article/view/574' | grep citation_
  → citation_title "Flowers, plants and trees in female naming in China"; citation_author "Irena Kałużyńska"; citation_doi "10.17651/ONOMAST.69.7"

curl -sSL 'https://api.crossref.org/works?query.author=S%C5%82o%C5%84&filter=issn:0078-4648&rows=10'  → total-results 0
curl -sSL 'https://api.crossref.org/journals/0078-4648/works?filter=from-pub-date:2024-01-01,until-pub-date:2025-06-30&rows=100'
  → vol 68 list includes 10.17651/onomast.68.5 Siwiec "Imiona osobowe w polszczyźnie wobec kategorii płci"; no Słon/Słoń anywhere
```

Retained receipts (live bytes, headers, CDX, extracted text):
`.ufo/waves/round-77/w2/stage/CritS934/` — `s934-wayback.pdf` (546,440 B, sha256
`1b4c60f2d1ba56cde6e1209d610f00f4899234416fdf7c64bcf14be43b8a2ff9`),
`s934-live.pdf` (417,093 B, sha256 `5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc`),
`s934-wayback.headers`, `s934-live.headers`, `cdx-763.txt`, `wb.txt`, `lv.txt`, `SHA256SUMS`.

Tooling: no installs — system binaries only (`curl`, `pdftotext`/`pdfinfo` from poppler,
`file`, `python3`); pacman not run (paused).
