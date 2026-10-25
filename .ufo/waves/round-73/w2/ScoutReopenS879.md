# ScoutReopenS879 — wave 2 FALSIFY, row S879 (lane rev 0316b8883b4f8d44b8efd720140e7f52f734a102)

Fetched files: /tmp/ScoutReopenS879/ (live-browser.html, live-curl.html, rep1/rep2.html, wb-browser-id_.html [gzip], wb-id_-decoded.html, wb-browser-wrapped.html, wb-curl.html, pdf-Mozi.pdf, pdf-curl.pdf, body.txt, cdx-*.txt). No lane/fleet write other than this file. No tool installed.

## VERDICT: ADMIT-FAILS — failing field: the `scope` cell (durability clause "the one Wayback capture (20261025222414) is a 23443-byte shell that does not carry the span and is not an anchor") and, with it, the lesson-Gate/`claims.json` "live leg only" statements. The quote, anchor cell, 11-cell parse, tier, recheck, used-by all stand.

## BLOCKER-1 — the "shell" capture is NOT a shell; it carries the span (false admitted statement)

The row (line 834), lesson `round-73.md` lines 36-40 and claims.json "fix" (line 66) all say capture 20261025222414 is a 23443-byte shell without the span, deliberately not named as an anchor.

Reproduction (browser UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, 2026-10-25 ~23:07 GMT):

```
GET https://web.archive.org/web/20261025222414id_/https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike
status=200 size_download=23443        # = the row's "23443 bytes"
content-type: text/html; charset=utf-8 ; content-encoding: gzip ; first bytes 1f 8b 08 00
python gzip.decompress -> 23443 -> 97656 bytes
decoded sha256 00ebfa2d9f06528247e1c529390d7c6e3e64e9b8169c37e6ba7770bc494c08ce
whitespace-collapsed text: quote in body = True; 'Personal languages' True; 'Auxlangs' True
title = «КЛАССИФИКАЦИИ КОНЛАНГОВ В СОВРЕМЕННОЙ ИНТЕРЛИНГВИСТИКЕ – тема научной статьи …»
```
The 23443 is the gzip wire size (curl without --compressed saved the compressed stream; reading it as text gives mojibake and no hit — that is how the "shell" verdict arises [INFERENCE: the seat read the undecoded gzip]). Same result with plain `curl/8.7.1 --compressed`: wire 23443 B, decoded file sha256 identical (00ebfa2d…), `grep -c 'Personal languages'` = 1. The Wayback-wrapped replay `/web/20261025222414/https://…` (no id_) returned 200, 101579 B, quote True. Context in the capture: "…Arëndron Майкла Рептона. 2.2. Personal languages Это личные, или персональные, языки, т. е. вымышленные языки, проектируемые отдельными энтузиастами лингвоконструирования или группами авторов…".

Consequence: a dated Wayback capture carrying the verbatim span EXISTS (made this round). The row therefore (a) wrongly says live-only durability, (b) wrongly refuses an available anchor (QUALITY 18 used backwards), (c) the lesson/claims statements "capture whose body lacks the quote" are false. Fix: name the capture in the source cell and anchor, restate durability (capture 20261025222414, live + capture). Severity BLOCKER (an admitted statement is wrong); the quote and row stay admissible once corrected.

The live-only durability caveat is therefore NOT honest — it understates durability (conservative, but false, and it hides the only archival anchor).

CDX probes (all `https://web.archive.org/cdx/search/cdx?url=<X>&output=txt&fl=…`; UA noted):
| UA | X | result |
|---|---|---|
| browser | cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike | HTTP 200: `20261025222414 https://cyberleninka.ru/…interlingvistike 200 text/html 24482 KISPYG6AZ5ITJO6HOWZ6JBOZHSC5EPIU` (24482 = CDX compressed record length; replay wire size 23443) |
| browser | same + `/` | same single row |
| browser | www.cyberleninka.ru/… | same single row (CDX canonicalises www) |
| curl/8.7.1 | http://cyberleninka.ru/… | same single row |
| curl/8.7.1 | …interlingvistike* (prefix) | HTTP 200, 0 bytes |
| curl/8.7.1 | …interlingvistike/pdf | HTTP 200, 0 bytes |
| curl/8.7.1 | cyberleninka.ru/article/n/klassifikatsii-konlangov* | HTTP 200, 0 bytes (the empty wildcard results contradict the exact hit [INFERENCE: wildcard path unreliable/rate-limited]; not relied on) |
Several browser-UA probes (http://…, *-prefix) hit `curl: (7) Failed to connect to web.archive.org:443` — connection throttle; retried later under curl/8.7.1 (rows above). Only one capture exists in the CDX for the slug; "no earlier capture" (lesson line 36) is consistent with it.

## Checks that PASS (each with output)

- Live fetch: `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike`, final URL same, HTTP/2 200, Cloudflare. Browser UA: 97588 B sha256 8c1797fb…f29; curl/8.7.1: 97656 B sha256 22c76673…ec0c; repeats (browser UA ×2): 97588 B (529e9610…) and 97656 B (6e5a9074…). Neither equals the evidence line (97622 B, sha256 709e186b…). Not UA-gated; both UAs serve the article.
- sha256 verdict: DRIFT, and by construction non-reproducible — the diff of two fetches is only Cloudflare `data-cfemail` tokens (re-randomised per request) and `hl to-search` highlight spans (`diff <(tr '>' '>\n' …)` shows lines 651, 790, 798 only). MINOR-1: the row/evidence "97622 bytes / sha256" can never be matched; it identifies one rendering, not the content. The pinned content identity should be the PDF (below) or the capture's decoded text.
- Quote verbatim in fresh body (tags→space, entities unescaped, whitespace collapsed): found in all four live fetches (char offset 34365–34367 of ~50,060); also in the capture (above). Quote word count 16 (`python len(q.split())`; evidence says 16) ≤ 25. Evidence file `quote-found-verbatim: yes` — confirmed.
- Row cells: `awk -F'|' '{print NF}'` on line 834 → 13 (= 11 cells + 2 pipe edges); cells: id S879, source, kind paper, tier B, scope, anchor, teaches, status mined, opened 2026-10-25, recheck 180d, used-by `corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md`. Anchor cell contains the evidence quote verbatim (string compare of the «…» span to the evidence quote: same).
- Source cell: only one URL (the cyberleninka slug) + DOI text; live resolves 200 (above). The row names NO Wayback URL in the source cell (the "named capture" is only a timestamp inside the scope cell — and wrongly disqualified).
- Locator: heading is served as «сОпОсТАВЛЕНИЕ КЛАссИФИКАцИИ д. питерсона с типологиями современных отечественных ЛИНГВИсТОВ» (OCR-case-mangled); the row's «Сопоставление классификации Д. Питерсона с типологиями современных отечественных лингвистов» is a case-folded match, not byte-verbatim (MINOR-2; the amendment itself discloses the mangling at its line 4, the row/evidence do not). Item 2.2 follows items 1, 2.1, 2.1.1, 2.1.2 inside it.
- "PDF p. 5 = printed p. 32": publisher PDF `…/pdf` fetched (HTTP 200, 630227 B, sha256 cc9a91c5…643f, identical under both UAs, 7 pp.); `pdftotext -f 5 -l 5` shows "2.2. Personal languages" and page footer 32; pp. 1–7 = 28–34. Confirmed. MINOR-3: that PDF URL is not in the source cell, and the PDF text layer splits the quote across columns/hyphenation («вымыш-ленные»), so the PDF page is checkable but not byte-matchable; the amendment (line 56) calls the page "(to-verify)" while the row asserts it — internal inconsistency in how firmly the page is stated. The stable PDF is a better anchor than the HTML and is unnamed.
- Tier/scope overclaim: scope says content of the Шувалова/Сидорова classification "as a later peer-reviewed article restates it" (Auxlangs; вымышленные языки в широком смысле incl. Artlangs; Personal languages) — all three present at offsets 33226/33516/34371 with attribution [Шувалова, Сидорова, 2006]; Tier B with the stated reason (one review article reporting another's classification) is not overclaimed. "peer-reviewed": journal is ВАК-listed (page: «ВАК»); peer review itself is not stated on the page — I did not verify review process [could not check]. "teaches … says which of the compared typologies is most detailed": text «Наиболее детализированной классификацией, по всей видимости, является типология Д. Питерсона» (10 tokens, present) — supported, hedged by the article ("по всей видимости").
- recheck 180d / used-by: `opened` 2026-10-25 + 180d; used-by names the amend file, which cites S879 at its lines 4,36–56,74,90 (`git show 0316b88:…amend-2026-10-23.md | grep -n S879`); base entry conlang-scholarship.md not listed — I did not verify whether the base entry cites S879 [not checked]. Row text sits at SOURCES.md line 834 and lesson Gate row at line 21 of round-73.md; the Gate row's date/quote/locator/evidence/status fields are consistent with the evidence file.

## Not checked
- Whether Wayback capture 20261025222414 was created by the round's own Save-Page-Now call (CDX shows it, timestamp 2026-10-25 22:24:14, but I did not see the SPN request).
- Whether claim C's `accept-c.py` legs depend on the "live leg only" wording (grepped only: no S879-specific durability assertion found in its first 20 hits; not run).
- Peer-review status of the journal beyond the ВАК tag on the page; whether the base entry cites S879.
- Wildcard CDX results are unreliable (0 rows despite an exact hit).
