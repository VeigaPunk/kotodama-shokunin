# B2ReviewRowS726 — falsification review of inherited draft

Draft under review: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS726/row.txt` (wave-1, unverified).
Counter rules applied: `reports/round-64/accept-c.py` legs ROWS and RESTATE (rev 0).

## Fetches (verbatim)

- Live: `curl -sL --max-time 90 ... 'https://eric.ed.gov/?id=ED252065'` → first attempt `HTTP 000` (connection reset, curl/7 default UA over IPv6 path); retry with browser UA `LIVE_HTTP 200 https://eric.ed.gov/?id=ED252065 size=13576`. A plain default-UA `curl -4` also returns `200`. Body: `body_live.html`.
- Capture: `CAPTURE_HTTP 200 https://web.archive.org/web/20240914111851id_/https://eric.ed.gov/?id=ED252065 size=11729`. Body: `body_capture.html`.
- Wayback availability API confirms the capture: `"timestamp": "20240914111851"` for this URL — matches the row's capture verbatim.
- Access note: eric.ed.gov discriminates by client string — `curl/8.x` default UA GETs 200, while the locator's Firefox UA (`Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0`) and a Python urllib Chrome-UA request get the connection reset/timed out. No challenge/captcha was met or passed; ordinary GETs succeed.

## Quote search (normaliser = counter's: NFKC, casefold, `[\W_]+`→space)

- Live body, tag-stripped text: HIT at normalised index 769.
  Context: `… ochs elinor schieffelin bambi b two claims are made concerning the interrelationship of language acquisition and socialization processes 1 the process of acquiring language is deeply affected by the process of becoming a competent member of a society and 2 the process of becoming a competent member of society is realized to a large extent through language and through acquiring knowledge of its functions social distribution and interpretations in …`
- Placement: inside the visible `<div class="abstract">` text node (also duplicated in `<meta name="description">`/`citation_abstract`, but present in body text proper — admissible).
- Capture body: same HIT at index 750, same context.
- Normalised quote length: 19 words (rule: 8–25).

## Lane locator (re-run by reviewer)

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://eric.ed.gov/?id=ED252065' 'the process of acquiring language is deeply affected by the process of becoming a competent member of a society'`

First line, three attempts (~30–55 s each, incl. one after 25 s cooldown):
- `NOT_LOCATED https://eric.ed.gov/?id=ED252065 ConnectionResetError`
- `NOT_LOCATED https://eric.ed.gov/?id=ED252065 ConnectionResetError`
- `NOT_LOCATED https://eric.ed.gov/?id=ED252065 ConnectionResetError`

The draft's `VERIFY: LOCATED` line is therefore NOT currently reproducible: the locator's pinned Firefox UA is refused by eric.ed.gov (ConnectionResetError before/within the TLS+GET exchange), while the same GET under other client strings succeeds. S726 is not in the counter's frozen LIVE_IDS subset `{S718,S723,S728,S733,S738,S743}`, so the LIVE leg does not probe it; the reset is a provenance/environmental caveat, not a row-content defect. Content truth is established independently via the successful plain GET and the same-page capture.

## Verdict table

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| row shape | 11 cells, `\| S726 \| …` | YES | split on `\|` → 11 cells; no `\|` inside cells | none |
| live URL | `https://eric.ed.gov/?id=ED252065` | YES | `LIVE_HTTP 200 https://eric.ed.gov/?id=ED252065 size=13576` | none |
| capture | `…/web/20240914111851id_/https://eric.ed.gov/?id=ED252065` | YES | `CAPTURE_HTTP 200`; availability API `"timestamp": "20240914111851"` | none |
| capture = same page | yes | YES | norm_url strips `?id=…` → `https://eric.ed.gov/` both sides; same record body returned | none |
| kind | `paper` | YES | peer-working-paper record; `citation_pdf_url` full text offered | none |
| tier | `A` | YES (defensible) | page is the work's own bibliographic record carrying the authors' verbatim abstract + full-text PDF link (`files.eric.ed.gov/fulltext/ED252065.pdf`); "source's own record" for this scope | none |
| scope | `Ochs and Schieffelin's foundational language acquisition/socialization paradigm` | YES | record abstract opens: `Two claims are made concerning the interrelationship of language acquisition and socialization processes` — the paradigm itself | none |
| anchor quote | `the process of acquiring language is deeply affected by the process of becoming a competent member of a society` | YES | verbatim, contiguous, visible abstract div; 19 normalised words; present in live 200 and capture 200 | none |
| citation: authors | `Ochs, Elinor & Schieffelin, Bambi B.` | YES | `citation_author` ×2 identical; body shows `Ochs, Elinor; Schieffelin, Bambi B.` | none |
| citation: year | `1982` | YES | title/`citation_publication_date` = `1982/11` (`1982-Nov`) | none |
| citation: title | `Language Acquisition and Socialization: Three Developmental Stories and Their Implications` | YES | `citation_title` identical + `Sociolinguistic Working Paper Number 105` matches draft's `No. 105` | none |
| teaches | `Helps learners connect speech development to the social roles of joining a community` | YES | glosses claim (1) faithfully; no overreach | none |
| status/opened/recheck/used-by | `mined / 2026-10-23 / 180d / corpus/knowledge/…md` | YES (shape) | matches ROWS leg constants | none |
| bullet clause | `The process of acquiring language is linked to social membership, giving worldbuilders community-based learner arcs. (S726)` | YES | content_words=12 (≥5); in-order quote hits=3 (`process, acquiring, language`); longest verbatim run=6 (≤12); novel words present (`linked, membership, worldbuilders, community, learner, arcs, …`). Restates only what claim (1) asserts — "linked to social membership" ≈ "deeply affected by becoming a competent member of a society"; no invented number | none |
| draft `VERIFY:` line | `LOCATED https://eric.ed.gov/?id=ED252065` | NOT REPRODUCIBLE | locator ×3 → `NOT_LOCATED … ConnectionResetError`; host resets the locator's Firefox UA while default-UA GETs return 200 | none to row content; provenance caveat — if the locator must re-establish this row later it will fail until the host stops refusing that UA (S726 is outside the LIVE leg subset) |

## RESTATE arithmetic (counter-simulated)

- `content_words(clause)` = 12 ≥ 5; in-order hits vs quote = 3 ≥ 3; novel content words present; max copied run = 6 ≤ 12 → RESTATE-clean for this row's bullet.

VERDICT: CLEAN — quote verbatim in live body and capture, citation/tier/bullet all verified; only caveat is environmental: the lane locator's Firefox UA is reset by eric.ed.gov, so the draft's `LOCATED` line is not reproducible today (S726 not probed by the LIVE leg).
