# ScoutJstageJcss — S865 re-open

## Fetch and conversion (observed)

Scratch was `/fast/scratch/hyaku/kotodama-r75/ScoutJstageJcss/`.

Command:
```sh
curl -sS -L -D headers.txt -A "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" -o s865.pdf "https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf" -w "HTTP %{http_code} bytes=%{size_download} final_url=%{url_effective}\\n"
```
Raw output:
```text
HTTP 200 bytes=1085244 final_url=https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf
```
Command: `sha256sum s865.pdf; file s865.pdf`
Raw output:
```text
fdf60d276b3f31cded2a40b8a12085f4b88e7f645062e3e2c9d9f8c647072b58  s865.pdf
s865.pdf: PDF document, version 1.6, 10 page(s)
```
UA for the PDF request: `Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0`.

Command: `pdftotext -layout s865.pdf s865.txt && wc -c s865.txt`
Raw output: `115506 s865.txt`. `pdftotext` emitted repeated `Syntax Warning: Invalid Font Weight` warnings; extracted Japanese text is readable. The archived capture `https://web.archive.org/web/20240904135913if_/https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf` was also fetched with the same UA: HTTP 200, 1,085,244 bytes, SHA-256 `fdf60d276b3f31cded2a40b8a12085f4b88e7f645062e3e2c9d9f8c647072b58` (identical to live PDF).

The staged recheck command was independently reproduced on extracted text:
```sh
grep -c 'narratology of narrative generation' s865.txt
```
Raw output: `3`.

## Verified claims / discrepancy

The staged row and base entry are read-only source material at `/home/vgpnk/Projects/shokuknow/merge/kotodama/`. Staged row S865 names Ogata Takashi, *Cognitive Studies* 25(2), 200–217 (June 2018), and describes the article as 解説. The PDF text itself begins `Cognitive Studies, 25(2), 200-217. (June 2018)`, shows the spaced heading `解    説`, the title `物語生成の物語論あるいはポストナラトロジー`, and author `小方 孝` (also identified in English as Takashi Ogata). These details are present.

The article is 10 PDF pages, journal pp. 200–217. Section headings found in extracted text include `1. ま え が き` (PDF p.1 / journal p.200), `2. 「物語」とは何か―複数の視点から―`, `3. 物語生成システム`, `4. 物語生成の物語論のための構図`, `4.1 情報物語論モデルの概要` (PDF p.8 / journal p.207), and `5. あ と が き`. There is no section titled `序説`; occurrences of that string are in bibliographic titles of other works. The staged S865 anchor says `「解 説」 heading + the 序説 section + ...`, and the entry source line says `「解 説」序説 + ...`. The heading and model passage locate, but the claimed named section does not. The intro is `1. まえがき`.

On PDF p.8 / journal p.207, the passage reads (spacing preserved from extraction):
```text
筆者単独の理論的枠組みは多重物語構造モデル (小方, 2003a; 小方・金井, 2010; Ogata, 2014, 2016a) であるが
```
This supports the staged scope qualifier “for the author's own framework only.” The English abstract says the article presents “narratology of narrative generation,” calls it “post-narratology,” and ranges across narratology, information sciences (including AI and cognitive science), and social sciences such as economics. That supports the entry's broad claim about narrative generation across disciplines.

**Prompt conflation:** the task prompt parenthetical “three-layer machine-writable description format (ストーリー / クエスト / シーン with キャラクター hierarchical sub-layer)” is the neighboring staged S866 claim (村井源), not S865. In S865's PDF, `クエスト` and `シーン` are absent; `ストーリー` occurs, but in ordinary narrative-generation contexts, not the claimed three-layer spec. The staged entry's own §6 explicitly cites S866 for that format, while §7 narrative generation cites S865. Do not attribute S866's format to this S865 source.

## Located quote

> “The narratology of narrative generation is also called “post-narratology””

Location: English abstract, PDF p.1 / journal p.200. Extracted-text whitespace-folded quote is verbatim; 9 whitespace-delimited words, 73 characters. The English abstract is part of the opened PDF. A second short Japanese locator is `筆者単独の理論的枠組みは多重物語構造モデル` at PDF p.8 / journal p.207, 1 whitespace-delimited token, 21 characters.

## Wayback CDX canonical-slug probe

The probes were ordinary HTTPS requests to the CDX endpoint with the above UA; HTTP port 80 was refused by this host. The first successful HTTPS batch returned:

1. Probed `www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf` using `https://web.archive.org/cdx/search/cdx?url=www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf&output=json&filter=statuscode:200&limit=10`:
```json
[["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["jp,go,jst,jstage)/article/jcss/25/2/25_200/_pdf","20201212045824","https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf","application/pdf","200","W2T7YMAP64LUDKUXLUSRVU64V3H5UWBP","1072509"],
["jp,go,jst,jstage)/article/jcss/25/2/25_200/_pdf","20240904135913","https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf","application/pdf","200","W2T7YMAP64LUDKUXLUSRVU64V3H5UWBP","1069488"]]
```
Both captures embed the exact canonical original URL, satisfy status 200 and are PDF captures. A separate query with explicit `https://` in the `url=` value returned the same two rows.

2. Probed `www.jstage.jst.go.jp/article/jcss/25/2/25_200/_article` with `https://web.archive.org/cdx/search/cdx?url=www.jstage.jst.go.jp/article/jcss/25/2/25_200/_article&output=json&filter=statuscode:200&limit=10`: `[]`.
3. Probed bare stem `www.jstage.jst.go.jp/article/jcss/25/2/25_200` with the same query shape: `[]`.
4. Prefix enumeration `url=www.jstage.jst.go.jp/article/jcss/25/2/25_200*` returned the Internet Archive “Temporarily Offline” HTML page, not CDX JSON. Subsequent retries also failed intermittently to connect to web.archive.org:443; HTTP port 80 failed consistently.
5. Positive control, same endpoint/query shape: `https://web.archive.org/cdx/search/cdx?url=example.com&output=json&filter=statuscode:200&limit=3` returned the header and 200 captures beginning:
```json
[["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["com,example)/","20020120142510","http://example.com:80/","text/html","200","HT2DYGA5UKZCPBSFVCV3JOBXGW2G5UUA","1792"],
["com,example)/","20020328012821","http://www.example.com:80/","text/html","200","UY3I2DT2AMWAY6DECFCFYMT5ZOTFHUCH","481"]]
```

Live direct checks for the cited `/_pdf` URL and `/_article` URL returned HTTP 200 without redirects; `_article` response was 118,418 bytes. Therefore no live redirect target was discovered to probe. CDX distinguishes the archived canonical PDF slug from the landing/bare stem.

## Proposed lane row, tier, verdict

Proposed row (11 columns; no embedded pipe characters):

| S889 | 小方 孝,「物語生成の物語論あるいはポストナラトロジー」, *Cognitive Studies* 25(2), 200–217 (June 2018), 解説 article — https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf | paper | B | One author's Japanese-language narrative-generation theory and own 多重物語構造モデル; not a consensus result | PDF title block and 解説 heading, abstract, §4.1 情報物語論モデルの概要, PDF pp.1 and 8 (journal pp.200 and 207); article served 2026-10-27 | narrative-generation research spans narratology, information sciences including AI and cognitive science, and social sciences; the author's own framework is 多重物語構造モデル | mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/narrative-structure-frameworks.md |

**Tier B**: this is a scholarly-journal expository article by one author presenting that author's own framework, not consensus authority for narratology generally. Lane `corpus/SOURCES.md` defines B as strong secondary; its QUALITY criterion 6 explicitly says publisher descriptions and abstracts are B for substantive claims even when accurate and reserves A for primary/authoritative exact-scope sources. The full paper is primary for what Ogata's own model says, but the row's proposed scope is appropriately limited to that model and the paper's stated approach; B avoids overclaiming authority for general narrative structure. This is not community material.

**Verdict: REFUSE as currently staged; flip to ADMIT after correcting the anchor/source-line locator from `序説 section` to the actual `1. まえがき` (and/or English abstract), while retaining the located §4.1 passage.** Reason: the live and archived PDF agree, and most staged S865 claims are supported, but the staged anchor's named section cannot be located on its own document. The prompt's three-layer-format parenthetical is not S865 evidence and should remain assigned to S866. The article and quote are otherwise accessible by ordinary requests; no challenge or access-control bypass was involved. The row should be re-opened on 2026-10-27 if amended, with evidence captured from that fetch.
