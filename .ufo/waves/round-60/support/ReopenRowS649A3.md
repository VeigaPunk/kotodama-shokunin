HOLDS

Re-open of source row S649 at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (HEAD is that revision; the worktree S649 and S616 rows are byte-identical to that revision). No tools installed. Sandbox only under `/fast/scratch/hyaku/kotodama-r60a3/ReopenRowS649A3/`.

Axes attacked: (1) the anchor quote locates, by `reopen-quote.py`, on the first URL and on the listed Wayback capture; (2) the capture body is byte-identical to `reports/round-60/captures/S649.bin` and to manifest sha256; (3) the access note matches a plain GET; (4) tier A and the scope match the page that was actually read; (5) S649's first URL is the same page as S616's; (6) every clause of the amulets entry line that cites S649 is carried by a sentence on that page.

## Row (frozen `corpus/SOURCES.md:604`)

Columns: id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by.

- kind `docs`, tier `A`, status `mined`, opened `2026-10-23`, recheck `2027-10-23`, used-by `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md`.
- scope: `the Met record's statement that hematite was believed to stop blood flow and was a favorite medium for amulets related to female reproductive health and menstrual problems`
- anchor quote (first quoted span of the anchor cell, 24 normalised words): `Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems`
- teaches: `supersedes S616 — Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems.`
- first URL: `https://www.metmuseum.org/art/collection/search/464456`
- capture URL: `https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456`
- access note: live plain GET, HTTP 429, 34222 bytes, 2026-10-23; Vercel Security Checkpoint challenge met, not passed. Capture HTTP 200, 246282 bytes, 2026-10-23.

S616 (`corpus/SOURCES.md:571`) has the same bibliographic gloss, the same first URL, the same capture URL, and the same anchor quote. Its teaches is a different sentence (`Hematite was a favourite medium for amulets against menstrual and reproductive complaints because the stone was thought to staunch bleeding.`). `url_refusal` is empty for both of S649's URLs (the path contains `search`, but there is no query, so it is not `search-url`).

## Commands and output

Pinned blob vs manifest (`reports/round-60/captures/manifest.json` key `S649`: sha256 `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea`, 246282 bytes, `text/html; charset=utf-8`, URL the capture above). `git show 47f27bd0…:reports/round-60/captures/S649.bin` and the worktree file are the same bytes.

```
pin_bytes 246282
pin_sha256 945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea
QUOTE Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems
QUOTE_WORDS 24
to_text_chars 3664
locate_in True
raw_contains_quote True
raw_idx 33239
last_script_open_before 29516 last_script_close_before 29696 inside_script False
TEXT hematite was believed to stop the flow of blood True
TEXT favorite medium for amulets related to female reproductive health and menstrual problems True
TEXT stop the flow of blood True
TEXT stop blood flow False
TEXT female reproductive health True
TEXT menstrual problems True
```

The quote sits in a text node, not in a skipped `script`/`style`. Surrounding HTML: `…Woman with the Issue of Blood (Mark 5:25–34; Luke 8:43–48). On the reverse a woman stands in the orant (prayer) pose. Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems.</div>…`

First plain GET of the live URL (curl, script UA, no challenge solving):

```
curl_http_code=429
curl_size=34228
curl_content_type=text/html; charset=utf-8
curl_url_effective=https://www.metmuseum.org/art/collection/search/464456
curl_redirects=0
CURL_EXIT:0
```

Body 34228 bytes, sha256 `1fc741413828daf56bc532776867230500b19adfecc6a6afd9bb5488e70b1ddb`, `<title>Vercel Security Checkpoint</title>`, body contains `Vercel Security Checkpoint` and `Enable JavaScript`, not the hematite sentence. Headers:

```
HTTP/2 429
cache-control: private, no-store, max-age=0
content-type: text/html; charset=utf-8
server: Vercel
x-vercel-challenge-token: 2.1792741987.60.OTgxMGQwNzgyM2YwYTVlZGE1MmVlYmY2OGFlNzhhM2I7Y2M3MjE5NDc7ZjI5NjViYjZkOTI4Yjg0MWM0Zjg4ODQ4YTRlZWQ5YTlmY2M2YTYzNzszOz09JScSu0DHRTChXs+ZQjY5iqGFvhJ6eaulOBhRpj6+1S/jJ27THjy6RMlWtAo=.87d22b8bed7a3b6cc0edaeb26bae3098
x-vercel-id: gru1::1792741987-2rwu1To2fAbKg3Xay2wzxsqkWsH4Tq1x
x-vercel-mitigated: challenge
date: Fri, 23 Oct 2026 07:53:07 GMT
```

The full `x-vercel-id` value is inside that body, so the challenge HTML is per-request. 34228 versus the note's 34222 is that variance, not a different page. Challenge met, not passed.

Wayback `id_` capture, first attempt `curl: (7) Failed to connect` (exit 7). Retry:

```
curl_http_code=200
curl_size=246282
curl_content_type=text/html; charset=utf-8
curl_url_effective=https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456
curl_redirects=0
CURL_EXIT:0
```

```
wayback_bytes 246282
wayback_sha256 945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea
pin_sha256 945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea
bytes_equal True
```

Memento headers: `memento-datetime: Wed, 10 Jun 2026 07:07:27 GMT`; `content-length: 246282`; `x-archive-orig-date: Tue, 09 Jun 2026 19:28:45 GMT`; `x-archive-orig-server: Vercel`; `x-archive-orig-x-matched-path: /[locale]/art/collection/search/[objectID]`; `link` original `https://www.metmuseum.org/art/collection/search/464456`. That is the capture the row names, and it is the pinned file.

Locator, from the lane root, `PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/reopen-quote.py --row S649`:

```
LOCATED https://www.metmuseum.org/art/collection/search/464456
EXIT:0
```

It located on the live URL (the script retries HTTP 429). Three following urllib GETs with the same UA, each a non-challenge 200, identical to each other and not to the June capture:

```
attempt 1 code=200 bytes=208088 ctype='text/html; charset=utf-8' final=https://www.metmuseum.org/art/collection/search/464456 sha=5f73db09be0de2bf243055569843e4c1b749ede8fb30f65baf81136f538fb3c9 located=True checkpoint=False
attempt 2 code=200 bytes=208088 … sha=5f73db09… located=True checkpoint=False
attempt 3 code=200 bytes=208088 … sha=5f73db09… located=True checkpoint=False
```

208088 is the size S616 recorded for its 2026-10-23 plain 200. Visible-text diff of that 200 against the pin: same description sentence and the same object facts; the pin still has the 9–11 June Dendur-closure banner and a different related-works carousel; the live page adds a "Content Notice". Neither difference touches the sentence or the labelled object fields.

`first_url_equal True` and `capture_url_equal True` against S616. `quotes_equal True`.

## What the page says

Visible text on both the pin and the live 200 (parser = `reopen-quote.py` `to_text`, scripts dropped):

- Title: Amulet Carved in Intaglio (Incised). Culture: Byzantine (Egypt). Geography line: Made in Byzantine Egypt. Date: 6th–7th century.
- Medium: Hematite, silver mount. Dimensions: Overall: 1 15/16 x 1 7/16 x 3/8 in. (5 x 3.7 x 1 cm). Also Hematite: (4.8 x 3.6 x 1 cm), which the row does not cite.
- Credit Line: Gift of J. Pierpont Morgan, 1917. Object Number: 17.190.491.
- Description: "Inscriptions identify the subject of this amulet as the Woman with the Issue of Blood (Mark 5:25–34; Luke 8:43–48). On the reverse a woman stands in the orant (prayer) pose. Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems."
- The page calls itself "this object record". `464456` is not in the visible text; it is the URL objectID (`[objectID]` on the archived matched path). The row's "object 464456" names that URL id, not the printed Object Number. Not a false accession.

## Tier, scope, access

- Tier A. Preamble: A is primary or authoritative for the row's scope (official docs included); tier is scoped, not global. `QUALITY.md` criterion 6 makes publisher descriptions tier B for substantive claims about a work. This scope is the Met's own statement on its own object record, and the entry only reports what that record says. The museum is authoritative for that wording. A does not over-claim the historical belief apart from the label. The entry's `**C**` is the line's confidence mark, not the registry tier.
- Scope. Both conjuncts are the description sentence. "stop blood flow" is a compression of "stop the flow of blood" (the exact trigram is absent; the proposition is not). The scope does not add S616's "because" / "staunch", and it does not take in the Mark/Luke identification, which is a different sentence on the page. Scope matches what was read.
- Access. Live plain GET did return HTTP 429 with title "Vercel Security Checkpoint" and `x-vercel-mitigated: challenge`, and the challenge was not passed. Byte count moves with the embedded request id (34228 here, 34222 in the note). The listed capture returned HTTP 200, 246282 bytes, `text/html; charset=utf-8`, sha256 equal to the pin. A later unchallenged live 200 (208088 bytes) also contains the quote and the same object fields, so the note's "not passed" is the challenged response, not a claim that the URL never serves the record.

## Entry line and clauses

`corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:82` at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (only citing line; `git grep` at that revision):

`- The Met's record says hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems (S649). **C**`

Page sentence carrying the line: "Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems."

| Clause | Page sentence |
|---|---|
| The Met's record says this | Carried. The sentence is the description on The Metropolitan Museum of Art object record for this amulet (the page's own words: "this object record"). |
| hematite was believed to stop the flow of blood | Carried by that sentence. |
| [hematite] was a favorite medium for amulets related to female reproductive health and menstrual problems | Carried by the same sentence. |

No clause is `NOT CARRIED`. `**C**` is the entry's confidence mark, not a claim read off the page.

Attacked and not broken: the quote living only inside a Next.js script (it is a text node; `locate_in` is true on the pin, the refetch, and the live 200); the capture drifting from `S649.bin` (byte-identical, including sha256); the live URL being a different page from S616 (same URL string, same capture URL, same object record); S616's causal "because … staunch bleeding" surviving into this line (it is not in the page sentence, not in S649's teaches, and not in the entry); the gospel-miracle sentence being smuggled into the S649 line (it is on the page and is not a clause of this line); tier A as a publisher-blurb inflation (the scope is the museum's own statement, which the line attributes).
