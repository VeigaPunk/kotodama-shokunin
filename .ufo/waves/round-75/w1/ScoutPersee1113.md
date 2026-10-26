# ScoutPersee1113 — Barthes / Persée per-page transcription check

Checked the round-75 draft claims and ledger first; neither was edited. Read the staged base entry, amendments `narrative-structure-frameworks.amend-2026-10-23.md`, `...-2026-10-23c.md`, `...-2026-10-24.md`, and staged `SOURCES.append.md` rows S876, S885, S917, S921 from the read-only shokuknow tree. Lane base pin used for QUALITY rules: `f556d1049fe651d3d63975600b13acd9fb686f15:corpus/QUALITY.md`. No tools installed.

## Findings

- **Notice and p. 1 are machine-readable.** The notice URL returned 200 with bibliographic/notice HTML and a `div.text[itemprop="articleBody"]` that contains the printed p. 1 transcription. The extracted body is 2,804 characters and 5 paragraphs; the direct p. 1 page URL produces the same 2,804 characters. It includes the author/title, the opening paragraph beginning “Innombrables…”, the next paragraph, and a footnote—not just the first phrase. Thus the base entry's narrow citation to the notice plus opening phrase is supported, but S876's assertion that only the notice and first paragraph are machine-readable is an under-description: more of p. 1 is readable. This is not evidence that all 27 pages are embedded in the notice.
- **Page URL shape discovered from the notice HTML:** `https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_NNNN_0000`; the notice itself links to page 1's rendered image and article-body text.
- **Pages 5, 6, 11, 26 are actual transcriptions**, not a JS-only viewer shell: each response has an image block plus `<div class="text" itemprop="articleBody">` with French paragraphs. All 27 page URLs `T1_0001_0000` through `T1_0027_0000` returned HTTP 200; `T1_0028_0000` returned 404 (0 bytes). Plain curl requests; no browser automation, login, challenge, or access control used.
- **OCR quality is usable for locating short passages, not clean copy-text.** Observed OCR defects include p. 1 `l'bomme` and `proit`; p. 5 `V analyse`, `Yelocutio`, and a footnote marker rendered `K`; p. 6 `Préfetoi'` and spacing/hyphenation; p. 11 `Vanalyse` and `semble- t-il`; p. 26 `Y art`, `V imagination`, `V homme`, and `boitement`. The located short quoted spans below themselves match after NFKC + whitespace folding. Longer substantive quotations should be checked against the page image or a reliable edition; the OCR is not uniformly verbatim.

## Claim-by-claim location and quote audit

All staged spans checked against extracted visible body text after Unicode NFKC and whitespace folding. Every listed span is **verbatim: YES**; no replacement quote is needed.

| Staged claim | Result / location | Located short quote and count |
|---|---|---|
| S876 | Notice body and direct page 1 both contain the opening; body also contains the following paragraph and a footnote. | “Innombrables sont les récits du monde” — notice/page 1, opening paragraph; 6 words, 37 characters. YES. |
| S885 | p. 5 carries the niveau-de-description paragraph and hierarchy explanation; p. 26 carries the concluding horizontal/vertical integration discussion. | p. 5 “Ce concept est celui de niveau de description” — 8 words, 45 characters. p. 26 “la dystaxie oriente une lecture « horizontale »” — 8 words, 47 characters; “l'intégration lui superpose une lecture « verticale »” — 8 words, 53 characters. YES for the staged p. 5 and p. 26 spans. |
| S921 | p. 6 carries the named-level paragraph, including attributions to Propp/Bremond, Greimas and Todorov. The full staged opening sentence matches. | “On propose de distinguer dans l’œuvre narrative trois niveaux de description” — p. 6, 11 words, 76 characters. YES. |
| S917 | p. 11 carries the closing classification paragraph: “Noyaux et catalyses, indices et informants … les premières classes entre lesquelles on peut répartir les unités du niveau fonctionnel.” It also says units can belong to two classes at once. | To stay below 80 chars for the compact Gate quote: “premières classes entre lesquelles on peut répartir” — p. 11, 7 words, 51 characters. The longer staged span “les premières classes entre lesquelles on peut répartir les unités du niveau fonctionnel” also matches after NFKC/whitespace folding (13 words, 88 characters). YES. |

The S885 page-26 text specifically says the dystaxie orients a horizontal reading and integration superposes a vertical reading; it then says each unit is perceived in its surface and depth. The S921 level list is **three** levels in the printed p. 6 transcription. The p. 11 list and unit-classification claim are present at the cited location. These are primary-text claims, not evidence that the methods are field consensus.

## Fetch commands and raw results

UA for all requests in this report: `Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0`.

Exact fetch form used for each body: `curl -sS -A "$UA" -o "$out" -w '%{http_code}' "$url"`; then `wc -c < "$out"` and `sha256sum "$out"`. Raw result lines:

```text
notice | https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 | HTTP 200 | bytes=109621 | sha256=9fa1dcdee545e85131af6c74716ade3340170f9716ecfccf7e1e907ea824c436
p01 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0001_0000 | HTTP 200 | bytes=3231 | sha256=0dccc5391de7fa06b140a4b32ca0e5825a650df0527e2bb6a12df80cf15edbf3
p05 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0005_0000 | HTTP 200 | bytes=4286 | sha256=8998f55ea7e913d0a82fbed9aacbf312d3fbdb3b1a33066288688c102834fbdf
p06 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0006_0000 | HTTP 200 | bytes=3811 | sha256=efee74ba5aaa3723f32e2fe2f983467645d0db3c6db7ec223194c82cd2f0348d
p11 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0011_0000 | HTTP 200 | bytes=4061 | sha256=9cbf7c9485a6683c709a6f94d72d0251f5c746028f5a233b72cadd1ecd885143
p26 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0026_0000 | HTTP 200 | bytes=4390 | sha256=fbe16353fb945c97811db21b9f5d414c04f39f0c1be513e67668fe32b356807b
```

Raw staged-recheck outputs (performed with the UA above):

```text
S876: curl -fsSL -A "$UA" 'https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113' | grep -c 'Innombrables' -> 1
S885: curl -fsSL -A "$UA" 'https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0005_0000' | grep -c 'niveau de description' -> 1
S917: curl -fsSL -A "$UA" 'https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0011_0000' | grep -c 'les premières classes entre lesquelles on peut répartir les unités du niveau fonctionnel' -> 1
S921: curl -fsSL -A "$UA" 'https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0006_0000' | grep -c 'trois niveaux de description' -> 1
```

## Wayback CDX canonical-slug probe (QUALITY 21/24)

The live notice HTML's canonical link is exactly `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`; an ordinary live request had effective URL unchanged, HTTP 200, 0 redirects. Probed that canonical slug, plus each page-level URL whose quoted text is used, and a positive control in the same CDX query shape. UA was the same exact UA above. Query template: `https://web.archive.org/cdx/search/cdx?url=<URL-encoded-probed-URL>&output=json&filter=statuscode%3A200&fl=timestamp%2Coriginal%2Cstatuscode%2Cmimetype%2Cdigest&collapse=digest&limit=1`; command: `curl -sS -A "$UA" -w '\nHTTP=%{http_code}\n' "$endpoint"` (body saved/hashed separately).

• Canonical notice URL probed: `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`. Raw compact response: HTTP 200, 193 bytes, sha256 `b64416aefe8bc2176b9e88752a0269d2c066e44d18da470cf4c6b71df5e11d12`:

```text
[["timestamp","original","statuscode","mimetype","digest"],
["20170301225114","http://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","text/html","VL44NXFEOCPALP7EWASI5JMZQKMLDBWZ"]]
```

The un-limited canonical query returned multiple status-200 captures, including HTTPS originals from 2019 onward.
- Page-level probed URLs, verbatim: `https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0005_0000`; same path ending `T1_0006_0000`; `T1_0011_0000`; `T1_0026_0000`. Each same-shape CDX request returned HTTP 200, raw body `[]` (3 bytes), sha256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. This is no capture for those page endpoints under this query, not a refusal of the live source: all four live pages served the located text.
- Positive control URL: `https://www.persee.fr/`, same query shape. Raw response HTTP 200, 160 bytes, sha256 `3a2ea3101892907f50c4da8c70547d6863aa1ccb56f1a38ce4cc037453855d22`; `[["timestamp","original","statuscode","mimetype","digest"],\n["20050129090047","http://www.persee.fr:80/","200","text/html","3RZCMVBVPZH3UJKYGX6JW7TNOBJCSNFU"]]`. Thus the CDX query shape returns a positive capture; empty page-endpoint responses are not a malformed-query artifact.

## Proposed lane registry row

Proposed row for the full-text method claim; no pipe character appears inside any cell:

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S885 | Roland Barthes, “Introduction à l’analyse structurale des récits”, Communications 8 (1966), pp. 1–27; Persée per-page transcription p. 5 https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0005_0000 and p. 26 https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0026_0000 | paper | A | Tier A only for the primary article’s own wording and method on these pages; not for field consensus or universal validity | p. 5 T1_0005_0000 “Ce concept est celui de niveau de description” (8 words, 45 chars); p. 26 T1_0026_0000 “la dystaxie oriente une lecture « horizontale »” (8 words, 47 chars) | Barthes’s levels-of-description premise and the horizontal/vertical articulation of levels | mined | 2026-10-27 | 180d — re-run curl and grep on the named p. 5 URL for “niveau de description” -> 1 (ran 2026-10-27) | corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md |

**Tier rationale:** A is appropriate for these exact claims because this is Barthes’s own primary text, directly transcribed from the 1966 article and the quote is located on the named pages. This does not make the article an authority for consensus, and does not extend the scope to claims it does not make. Community material is not part of this source; community remains C, never A.

## Verdict

**ADMIT** the p. 5, p. 6, p. 11 and p. 26 page-level transcription claims and the located quoted spans. Reopen with ordinary requests; the service is directly readable and all 27 page endpoints were available on this run. Preserve the OCR caveat and cite the specific page endpoints for each claim. The S876 notice/opening citation itself is supported, but its “only the notice and first paragraph are machine-readable” framing should be corrected to note the notice embeds more of p. 1. The page-level endpoints have no CDX capture in the tested query, while the canonical notice slug does; do not describe the page endpoints as archived.

**Flip condition:** if a fresh ordinary request stops returning the page-body transcription or the relevant span no longer matches after NFKC/whitespace folding, mark the affected row UNVERIFIABLE (or REFUSE if a verified access-control barrier blocks ordinary access); reconsider only after an ordinary public copy or same-page archive capture restores quote-level evidence.