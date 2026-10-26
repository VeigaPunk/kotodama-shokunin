# ScoutPersee1114 — Greimas / Persée 1114

## Finding

**Verdict: ADMIT**, scoped to Greimas's 1966 article and the structural description claims below. Direct plain-HTTP requests to the public notice and page transcription endpoints returned full article text for the relevant pages (no challenge or access control encountered). The staged two-isotopy/two-reading claim is supported; the equivalence paraphrase is supported on p. 31, not in the p. 29–30 anchor alone. The simple-semantic-structure claim is supported on p. 29. Do not imply that Greimas says the two readings are simply identical: his text specifies an equivalence to establish between discursive lexemes/utterances and corresponding structural content articulations.

Flip to REFUSE if the page-level text becomes inaccessible except by bypassing an access control, or if a re-opened transcription no longer contains these located passages; retain only UNVERIFIABLE if ordinary public copies cease to expose text.

## Source, retrieval, and exact outputs

User-Agent used for every request below: `Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0`.

Commands (run from `/fast/scratch/hyaku/kotodama-r75/ScoutPersee1114/fetches`):

```sh
UA='Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
curl -sS -D notice.headers -o notice.html -A "$UA" -w 'HTTP %{http_code} %{size_download} bytes\n' 'https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114'
for pg in 0028 0029 0030; do
  url="https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1114/comm_0588-8018_1966_num_8_1_T1_${pg}_0000"
  curl -sS -D "page_${pg}.headers" -o "page_${pg}.html" -A "$UA" -w "page_${pg}: HTTP %{http_code} %{size_download} bytes\\n" "$url"
done
sha256sum notice.html page_0028.html page_0029.html page_0030.html
```

Raw outputs:

```text
HTTP 200 116911 bytes
page_0028: HTTP 200 2573 bytes
page_0029: HTTP 200 3451 bytes
page_0030: HTTP 200 3737 bytes
bf434c044a11d4290bab55ed1a3c35bd015aa7eeb643500b655c1709274f9255  notice.html
0048d6218f642d0359ee97a7223d25a289e6be7d868066ee6a1bdd3f79036d68  page_0028.html
84557aef3cac190d5f838e03aa2d1abcf24420e51b4c99c5671c48afe6e42773  page_0029.html
2502768202dbd0e0b17f6310ad4b0c6cfe7e3d1edbd490efab5f7c4f71fe082f  page_0030.html
```

Further ordinary requests, same UA: pages 31–36 all returned HTTP 200: p.31 3856 bytes, p.32 3814, p.33 4077, p.34 3752, p.35 3460, p.36 3511. Page-URL shape was discovered in the notice HTML `data-content-url`: `https://www.persee.fr/doc/page/<notice-slug>/<T1_page_slug>`. Notice metadata confirms title *Éléments pour une théorie de l'interprétation du récit mythique*, author Greimas, Algirdas Julien, journal *Communications*, pp. 28–59; the notice contains 32 T1 slugs T1_0028 through T1_0059.

Text extraction was from the fetched HTML's `<div class="text" itemprop="articleBody">` paragraph contents, with tags stripped and HTML entities decoded. The page endpoints returned transcription text alongside page-image metadata. No challenge, login, paywall or other access control appeared.

## Located quotes and claim check

1. **Two isotopies / two readings, p. 30, transcription page `T1_0030_0000`:** “deux lectures différentes, l'une sur le plan discursif, l'autre, sur le plan structurel.” Count: 13 whitespace words, 82 characters including spaces and punctuation. To keep within the 80-character gate, use this shorter exact located quote instead: **“deux lectures différentes”** — 3 whitespace words, 24 characters. The surrounding source sentence says the message “se situe, lui aussi, sur deux iso- topies à la fois” and gives rise to two readings, one discursive and the other structural; the visible transcription hyphenates `isotopies` as `iso- topies` across a line break. Staged recheck command's target phrase occurs exactly once on p. 30 (`grep -c 'deux lectures différentes' page_0030.txt` → `1`).
2. **Simple semantic structure, p. 29, `T1_0029_0000`:** “comme une structure sémantique simple” — 6 whitespace words, 39 characters. Full sentence: “Le récit, pour avoir un sens, doit être un tout de signification et se présente, de ce fait, comme une structure sémantique simple.” This supports the staged claim about the récit as a simple semantic structure, not the stronger unqualified English phrase “single semantic structure.”
3. **Equivalence, p. 31, `T1_0031_0000`:** “celui de l'équivalence à établir” — 4 whitespace words, 31 characters. The longer sentence locates the equivalence to establish between the lexemes and utterances constituting narrative sequences and corresponding structural articulations of content. This supports the amendment's paraphrase, though the staged registry anchor should include p. 31 if it retains that point.
4. p. 31 also qualifies the dual-isotopy account: one isotopy may be the discursive manifestation of the other, while myths may interweave sequences situated on both isotopies in one narration. Avoid flattening this distinction into “two identical readings.”

## Tier and proposed registry row

Assign **A**: this is Greimas's original scholarly article, primary for the article's own proposed semantic/narrative method and terminology, and the passages were read directly in the French text. Tier A is claim-scoped under lane `corpus/SOURCES.md:14–18` (original paper is A). This is not a community source; community is never A. This is not merely the Persée notice/abstract (which would not justify A for substantive claims).

PROPOSED row (11 cells; no cell contains `|`):

| S887 | Greimas, A. J. (1966), «Éléments pour une théorie de l'interprétation du récit mythique», Communications 8, pp. 28–59 — https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 | paper | A | Greimas's own model of mythic narrative, two isotopies and their discursive/structural correspondence | p. 30 T1_0030_0000: “deux lectures différentes”; p. 29 T1_0029_0000: “comme une structure sémantique simple”; p. 31 T1_0031_0000: “l'équivalence à établir” | A mythic message is readable on two isotopies, discursive and structural; interpretation must establish correspondence/equivalence between narrative sequences and structural content articulations | mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md |

## Wayback CDX canonical-slug probe

Positive control: Barthes article in the same issue, `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`, returned HTTP 200 with many 200 captures (35 CDX records in the response), demonstrating the CDX query is live. Target canonical and bare-host probes both returned HTTP 200, 2732-byte identical responses, with 22 successful target captures. First target capture `20180605223046`; newest listed `20261006095414`. The tested URLs were:

- `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114`
- `www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114`
- positive control: `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`

Exact CDX command form (UA as above):

```sh
curl -sS -A "$UA" -w '\nHTTP %{http_code} bytes=%{size_download}\n' \
 'https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.persee.fr%2Fdoc%2Fcomm_0588-8018_1966_num_8_1_1114&output=json&fl=timestamp,original,statuscode,digest&filter=statuscode:200&collapse=digest'
```

Observed raw status/bytes: canonical target `HTTP 200 bytes=2732`; bare-host target `HTTP 200 bytes=2732`; positive control `HTTP 200 bytes=4439`. Canonical and bare-host outputs were byte-identical (SHA-256 `28c54caf3693c027df133779cdbc5b65d77a17db753da187572e53d339706890`); positive control SHA-256 `ac865aa3afd6517595e63a95945e5fdd05645fa5d5571bc34c6225499d097c18`. The CDX probe is for archival availability only; the source was opened directly, not via a Wayback workaround.
