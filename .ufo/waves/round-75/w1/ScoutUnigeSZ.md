# ScoutUnigeSZ — S905 / proposed S891

## Result

**ADMIT** for `corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md`, supported by the readable 2004-12-20 Wayback capture of the cited University of Geneva page. The live page returned a bot challenge (challenge met, not passed); the five-codes paragraph is present on the ordinary archive copy. The staged English labels are a gloss, not a verbatim English quote: the French page names `herméneutique`, `sémique`, `symbolique`, `proaïrétique`, and `gnomique`. Its glosses match the staged descriptions, including `sémique (champ thématique)` and `gnomique (sagesse, savoir, code culturel)`. The amendment should preserve that terminology nuance rather than represent its English labels as the page's exact names.

**Flip condition:** REFUSE this specific source attribution if a readable ordinary copy of the same cited page contradicts the paragraph or its five-code glosses; if the archived copy cannot be retained as the evidence window, keep the row refused until another ordinary copy (e.g. library scan or accessible copy) locates the passage. Do not pass the live challenge.

## Fetches and raw outputs

UA for both requests: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. curl 8.23.0.

Command (live page):
```sh
cd /fast/scratch/hyaku/kotodama-r75/ScoutUnigeSZ && UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" && echo "UA: $UA" && curl -sS -A "$UA" -o unige-barth70.html -w "HTTP_STATUS=%{http_code}\nBYTES=%{size_download}\nCONTENT_TYPE=%{content_type}\nFINAL_URL=%{url_effective}\n" "https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html" && sha256sum unige-barth70.html
```
Raw output:
```text
UA: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
HTTP_STATUS=200
BYTES=45201
CONTENT_TYPE=text/html
FINAL_URL=https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html
6d9ea847751a88231e6f633d106ccedb25c85cf4f0a0c0cbb5ee3f5f3ca3ad3b  unige-barth70.html
```
The body was a challenge, not the article: visible text included “Please enable JavaScript to view the page content” and “This question is for testing whether you are a human visitor”; it also contained `captcha`. HTTP 200 alone is not evidence that the article opened. Challenge was met and not passed.

Command (Wayback capture):
```sh
cd /fast/scratch/hyaku/kotodama-r75/ScoutUnigeSZ && UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" && curl -sS -A "$UA" -o wayback-barth70.html -w "HTTP_STATUS=%{http_code}\nBYTES=%{size_download}\nFINAL_URL=%{url_effective}\n" "https://web.archive.org/web/20041220223357if_/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html" && sha256sum wayback-barth70.html
```
Raw output:
```text
HTTP_STATUS=200
BYTES=5694
FINAL_URL=https://web.archive.org/web/20041220223357if_/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html
f9a18d786b83400e1abba9a2c7f40956db54b681cbb40f3ac9319b2da2f6d6b8  wayback-barth70.html
```

## Located quote and verbatim test

Quote: **“cinq grands codes que vont rejoindre tous les signifiés du texte”** — 11 whitespace-separated words, 64 characters. It occurs in the page's `Fiche de lecture` main-text paragraph beginning `Par hasard, les premières lexies suscitent l'établissement…`, in the sentence enumerating the five codes; in the raw archived HTML it is inside a `<q>` element at byte-string offset 4180 (HTML accented characters are entities). The visible paragraph continues with the five descriptions. NFKC normalization plus whitespace folding retained the quote exactly.

The staged amendment's English comma-separated sequence does not occur verbatim (the document is French). The actual names and glosses on the page are: `code herméneutique (l'énigme à déchiffrer)`, `code sémique (champ thématique)`, `code symbolique (l'antithèse)`, `code proaïrétique (code des actions et des comportements)`, `code gnomique (sagesse, savoir, code culturel)`. Thus the cited paragraph and the staged substance locate; use the French wording / explicit gloss distinction in any exact-source account.

## Wayback CDX canonical-slug probe (QUALITY 21/24)

Canonical/front-door URL: `https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html`. Live fetch's final URL equalled the request (no redirect target). Canonical slug probed without scheme/`www`, which CDX normalized to `ch,unige)/lettres/framo/cernet/biblio/barth70.html`; this covers the same path and archive originals show `http://www.unige.ch:80/...`.

Exact command and raw output:
```sh
cd /fast/scratch/hyaku/kotodama-r75/ScoutUnigeSZ && UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" && curl -sS -A "$UA" "http://web.archive.org/cdx/search/cdx?url=unige.ch/lettres/framo/cernet/biblio/barth70.html&output=json&filter=statuscode:200&limit=20" -w "\nHTTP_STATUS=%{http_code}\n"
```
```text
[["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["ch,unige)/lettres/framo/cernet/biblio/barth70.html","20030908073936","http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html","text/html","200","J3LCWQ46LN7YBZJMDL5ANWA7ZUMC6IG4","1960"],
["ch,unige)/lettres/framo/cernet/biblio/barth70.html","20041220223357","http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html","text/html","200","J3LCWQ46LN7YBZJMDL5ANWA7ZUMC6IG4","1962"]]

HTTP_STATUS=200
```
Both CDX captures have the same digest; latest is 2004-12-20. Positive control, same query shape against `url=unige.ch`:
```sh
cd /fast/scratch/hyaku/kotodama-r75/ScoutUnigeSZ && UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" && curl -sS -A "$UA" "http://web.archive.org/cdx/search/cdx?url=unige.ch&output=json&filter=statuscode:200&limit=3" -w "\nHTTP_STATUS=%{http_code}\n"
```
```text
[["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["ch,unige)/","19970103015936","http://www.unige.ch:80/","text/html","200","LP23MBJVHYJTOXNOP3DAV7VLKKHSYNPI","1249"],
["ch,unige)/","19970607172216","http://www.unige.ch:80/","text/html","200","FQIUKWKEFYODE44DJZINZQXFRP3CKAL7","1224"],
["ch,unige)/","19970704112411","http://www.unige.ch:80/","text/html","200","LP23MBJVHYJTOXNOP3DAV7VLKKHSYNPI","1249"]]

HTTP_STATUS=200
```
Positive control returned status-200 captures, so the target's two-row result is not a malformed/empty-query artifact. No redirect target needed probing because the live URL did not redirect.

## Proposed registry row and tier

Proposed 11-column row (no cell contains a pipe):
```text
| S891 | University of Geneva CERNET, Barthes, S/Z fiche de lecture — https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html | docs | B | Barthes's five-code account in S/Z for narrative-structure design | Fiche de lecture, paragraph “Par hasard…”: “cinq grands codes que vont rejoindre tous les signifiés du texte”; readable copy https://web.archive.org/web/20041220223357if_/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html | five codes named herméneutique, sémique, symbolique, proaïrétique, gnomique, with the page's enigma, thematic-field, antithesis, action/behaviour, and knowledge/cultural glosses | mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md |
```

**Tier B:** the page is a university-hosted `Fiche de lecture` that summarizes/quotes *S/Z*, not the 1970 primary edition itself. It is strong secondary support for this narrowly scoped account, not A-tier primary evidence. The row kind `docs` matches its web reading-sheet format.

## Evidence / remaining limit

The fetched archive is an ordinary capture of the same page path and contains the exact quote in its visible text. The live page's present body could not be inspected without passing its challenge; no claim is made about content changes after the archived 2004 capture. No tools were installed.
