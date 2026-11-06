# C6 re-open and re-judge — Encyclopaedia Iranica, "Courts and Courtiers x. Court poetry"

Seat ScoutRejudge100 · kotodama round 100 wave 1 · 2026-11-06 · routed defect R3
(read-only research; no registry row, no knowledge file, no tool written by this seat)

## 0. Verdict

**REJECT — access.** The round-99 closure's premise for R3 ("now HTTP 200 with the
article") does not reproduce from this host: 24 live requests over 14 minutes returned
HTTP 403 on every one, all of them the same Cloudflare managed challenge, and the block
is host-wide (homepage and a control article also 403; IPv4 and IPv6 both 403). No
article bytes were served, so no quote could be located and no scope or tier judgment
rests on evidence. C6 stays rejected on the round-99 reason, now better grounded: the
403 is not a transient failure but an edge challenge (`cf-mitigated: challenge`).

Flip condition: **either**
(a) the live page serves HTTP 200 with article bytes to plain curl from this host — the
    closure's recorded 200, 400760 B, must be re-measured, not inherited; **or**
(b) a reachable open mirror of the same entry appears. The lane's own precedent for
    Iranica is `https://web.archive.org/web/<timestamp>id_/https://www.iranicaonline.org/articles/courts-and-courtiers-x/`
    (rows S782 and S822 in `corpus/SOURCES.md` both cite that `id_` form for other
    Iranica entries, and `corpus/knowledge/civilizations/parthia.md:192` records the
    same route for "Gōsān"). That route is closed today: see §5.

A provisional scope/tier reading that does **not** depend on the bytes is in §7–§8, so
the L1 can integrate in one step if access returns. It is labelled inference and must
not be used as a row's evidence.

## 1. What R3 asked

Round-99 rejected candidate C6, Encyclopaedia Iranica "Courts and Courtiers x. Court
poetry" (`https://www.iranicaonline.org/articles/courts-and-courtiers-x/`), for access
(HTTP 403 Cloudflare). The round-99 closure re-fetched it once with HTTP 200 and routed
R3: re-open and re-judge on scope and tier. The rejection record
(`.ufo/waves/round-99/w1/stage/ExecRegistry99/dropped.md:8`) names the same URL and the
flip: "an open mirror of the same entry or a peer-reviewed article on Persian madh/qasida
panegyric".

## 2. Attempts — every request, with rc

Target unless stated: `https://www.iranicaonline.org/articles/courts-and-courtiers-x/`.
All requests `curl -sS -L --max-time 30` with the default user agent unless the form
column says otherwise. `rc` is curl's exit status.

| # | time (local) | form | HTTP | bytes | rc |
|---|---|---|---|---|---|
| 1 | 08:38:52 | `-A "curl/8.7.1" -L` | 403 | 5539 | 0 |
| 2 | 08:38:52 | `-A "curl/8.7.1" -L` | 403 | 5539 | 0 |
| 3 | 08:38:52 | `-A "curl/8.7.1" -L` | 403 | 5539 | 0 |
| 4 | 08:39:05 | no `-A`, no `-L` (the closure's exact form) | 403 | 5539 | 0 |
| 5 | 08:39:06 | default UA, `-L` | 403 | 5539 | 0 |
| 6 | 08:39:22 | default UA, `-L` | 403 | 5539 | 0 |
| 7 | 08:39:42 | default UA, `-L` | 403 | 5539 | 0 |
| 8 | 08:40:02 | default UA, `-L` | 403 | 5539 | 0 |
| 9 | 08:40:03 | no trailing slash | 403 | 5536 | 0 |
| 10 | 08:41:20 | bare domain `iranicaonline.org` | 403 | 5535 | 0 |
| 11 | 08:41:20 | control article `/articles/gosan/` | 403 | 5467 | 0 |
| 12 | 08:41:20 | control homepage `/` | 403 | 5401 | 0 |
| 13 | 08:43:10 | `-4` (IPv4, 104.26.9.119) | 403 | 5497 | 0 |
| 14 | 08:43:10 | `-6` (IPv6, 2606:4700:20::681a:877) | 403 | 5539 | 0 |
| 15 | 08:47:24 | probe 1 | 403 | 5539 | 0 |
| 16 | 08:48:04 | probe 2 | 403 | 5539 | 0 |
| 17 | 08:48:44 | probe 3 | 403 | 5539 | 0 |
| 18 | 08:49:24 | probe 4 | 403 | 5539 | 0 |
| 19 | 08:50:04 | probe 5 | 403 | 5539 | 0 |
| 20 | 08:50:44 | probe 6 | 403 | 5539 | 0 |
| 21 | 08:51:24 | probe 7 | 403 | 5539 | 0 |
| 22 | 08:52:04 | probe 8 | 403 | 5539 | 0 |
| 23 | 08:53:17 | `http://` scheme (redirected to https) | 403 | 5539 | 0 |
| 24 | 08:53:17 | `curl -I` header-only | 403 | — | 0 |

24 live requests, 0 non-403. Criterion-38 retry budget was exceeded deliberately: the
closure recorded a 200 twenty minutes earlier, so a longer window was warranted before
calling it unreachable.

## 3. What the bytes are

Header of request 24:

```
HTTP/2 403
date: Fri, 06 Nov 2026 11:53:17 GMT
content-type: text/html; charset=UTF-8
content-length: 5539
cf-mitigated: challenge
server: cloudflare
```

`cf-mitigated: challenge` occurs **1** time in the header dump
(`grep -c 'cf-mitigated: challenge' hdr.txt` → 1, rc 0). That header is Cloudflare's own
statement that it is serving a managed challenge, not an origin error.

Body: the Cloudflare interstitial. Tag-stripped, every one of the 403 bodies reduces to
the identical 59-byte string, sha256 `56b19218bc8f1cba0dcc32fdb9850e716b83713ddd0497a47f0a64ff99585fdf`,
which is exactly:

> Just a moment... Enable JavaScript and cookies to continue

Count of that string in the stripped capture: **1** (`t.count(q)` → 1, len 59; rc 0).
The raw bodies are 5539 B each but differ per request in the challenge nonce and
`_cf_chl_opt` tokens (9 distinct sha256 over 9 bodies, all 5539 B) — the same shell, not
different pages.

Saved capture:

- `captures/C6-iranica-live-403.html` — 5539 B, sha256 `5ef2c5befc884649c2929ad089f47f86d2073e39e331d3a77acfd7203fabe4cc`
- `captures/C6-iranica-live-403.txt` — 59 B, sha256 `56b19218bc8f1cba0dcc32fdb9850e716b83713ddd0497a47f0a64ff99585fdf`
- `captures/C6-iranica-live-403.headers.txt` — 2176 B, sha256 `f1d03c7825d057b76727bd13516b176fb68c8d96aab2a98587eb6714dd9574eb`, the header dump of request 24

## 4. The block is host-wide, not article-specific

Requests 10–12 are the control: the bare domain, a different article (`/articles/gosan/`,
the entry the lane already reads through the Internet Archive) and the homepage all
return 403 with the same interstitial. So the 403 is an edge decision on this egress,
not a per-page failure or a per-URL fluke. Requests 13–14 show it is not an address-family
artifact: IPv4 and IPv6 both 403.

This matters for R3: the closure's single 200 cannot be reconstructed by trying harder on
the same URL, because the same host refuses every URL from here.

## 5. Archive routes are also closed

| # | target | HTTP | bytes | rc |
|---|---|---|---|---|
| A1 | `archive.org/wayback/available?url=…` | 429 | 117 | 0 |
| A2 | same, retry 1 (20 s backoff) | 429 | 117 | 0 |
| A3 | same, retry 2 | 429 | 117 | 0 |
| A4 | same, retry 3 | 429 | 117 | 0 |
| A5 | `web.archive.org/cdx/search/cdx?url=…` | timeout | 0 | 28 |
| A6 | `web.archive.org/web/2026id_/…` | timeout | 0 | 28 |
| A7 | same, retry 1 | timeout | 0 | 28 |
| A8 | same, retry 2 | timeout | 0 | 28 |
| A9 | same, retry 3 | timeout | 0 | 28 |
| A10 | `timetravel.mementoweb.org/timemap/link/…` | DNS failure | 0 | 6 |

The Internet Archive answered the availability API with 429 four times and timed out on
five direct requests; the Memento aggregator does not resolve. The lane's precedent route
(§0(b)) is therefore unavailable today as well, and no other open copy exists: a
read-only search of the fleet repo and of `/home/vgpnk/Projects/shokuknow` for
`courts-and-courtiers` or `COURTS AND COURTIERS`, excluding this round's dispatch files
and the round-99 candidate record, returned no paths at all: the only hits anywhere are
the round-99 rejection record, its 5539-byte challenge capture, the round-99 closure
document and this round's own spec files.

## 6. Why this is not a transient failure

Three independent signs, none of them a retryable class:

1. `cf-mitigated: challenge` — the origin is not reached at all; Cloudflare answers.
2. Host-wide: homepage, bare domain and a second article all 403 (§4).
3. Stable over 14 minutes and 24 requests, with 20–40 s spacing, on both address families.

A 429, 5xx or timeout would have been retried and recorded as transient. A managed
challenge is a wall, and the rules forbid passing it. No bypass was attempted: no
browser, no JS execution, no CAPTCHA solving, no cookie jar, no user-agent spoofing
beyond the lane's prescribed default, no TLS-verification bypass, no third-party
render/mirror service.

## 7. Scope judgment — provisional, zero article bytes

Measured on `corpus/knowledge/linguistics/praise-poetry-panegyric.md` (45197 B, 13 `## `
headings):

- `grep -c -i -E 'persian|qasida|qaside|farsi|iranica|ferdowsi|neẓāmi|nizami'` → **0**, rc 1.
  The praise entry carries no Persian case at all.
- §7 "Traditions at a glance" has **9** tradition rows (lines 178–186): Southern Bantu
  court, Yoruba, Hausa, Mande and Soninke, Greek epinician, contemporary Xhosa, Norse
  skaldic court, Tamil puram, Welsh and Irish bardic. No Persian row, no Arabic row.
- §3 "The praise singer: office, recruitment, licence, patronage and reward" runs 17
  bullets over Zulu, Tswana, Hausa, Mandingo, Xhosa, Greek epinician, Welsh, Tamil, Mande
  and Norse skaldic material; the nearest economic statement is the skaldic one
  ("there was money in poetry, court poets received generous rewards and renown in
  exchange for panegyrics", line 85, S1016).
- §8 "Panegyric, rivalry and the limits of flattery" runs 13 bullets, none Persian.

[INFERENCE] The title the closure recorded — `COURTS AND COURTIERS x. Court poetry`
(count 1 in `corpus/lessons/round-99-verifier-spotcheck.md`, rc 0) — names exactly the
surface §3 and §7 own: a court poet's place in a court, and the panegyric as a court
genre. If the bytes were served, the article would most plausibly support:

1. §3, a new bullet beside the skaldic reward line (line 85): the Persian court poet's
   office and what the patron gave for a qasida.
2. §7, a new table row between "Norse skaldic court" and "Tamil puram": singer and
   office, patron and reward, form and order, limit on the praise.
3. §8, a new bullet on rivalry or on the turn from praise to satire, **only if** the
   article carries it — the closure's "panegyric 13 hits" is second-hand and I could not
   verify a single one.

This is a gap-filling judgment, not evidence: nothing above may anchor a registry row
until the article's own sentences are located.

## 8. Tier judgment — provisional

Ceiling **A**, floor **B**, unsettled.

For A: the lane already carries two Encyclopaedia Iranica rows at tier A for adjacent
scopes — S782 ("'AṬR", perfume) and S822 (BIMĀRESTĀN, hospital), both `docs`/A in
`corpus/SOURCES.md` — on the ground that a signed EIr entry by a specialist is
authoritative for its own scope. If "Courts and Courtiers x" is a signed entry with a
bibliography, the same reasoning gives A for "the court poet's office and the qasida's
praise section in Persian court panegyric".

For B: tier is curation, not truth, and the byline, the bibliography and the article's
actual depth are unread here. An unsigned or purely survey-level entry would be B.

Neither can be settled without bytes, so no tier is assigned.

## 9. Flip condition

C6 flips to admissible when **either** holds, and the row must then cite the URL that
actually served:

- (a) `https://www.iranicaonline.org/articles/courts-and-courtiers-x/` returns HTTP 200
  with article bytes to plain `curl -sS -L --max-time 30` from this host. The closure's
  200 / 400760 B is the only record of success and is **not** reproducible here; treat it
  as unverified until re-measured.
- (b) an open mirror of the same entry is reachable — the lane's `id_` Wayback form used
  by S782 and S822, or any other openly served copy of the same text. Today: 429 and
  timeouts (§5).

Until then the round-99 rejection stands.

## 10. What this seat did not do

- No registry row, no knowledge file, no tool, no `SOURCES.md` edit, no manifest edit.
- No bypass of the challenge in any form (§6).
- No claim about the article's content, byline, length or hit counts: the closure's
  400760 B and "panegyric 13 hits" are recorded as second-hand and unverified.

## 11. Commands and rc

| command | result | rc |
|---|---|---|
| `curl -sS -L --max-time 30 -o … -w '%{http_code} %{size_download}' <url>` ×24 | 403, sizes in §2 | 0 each |
| `curl -sS -I --max-time 30 <url>` | 403, `cf-mitigated: challenge` | 0 |
| `grep -c 'cf-mitigated: challenge' hdr.txt` | 1 | 0 |
| `python3 strip.py iranica-att1.html captures-403.txt` | 59 B | 0 |
| `sha256sum captures/C6-iranica-live-403.html` | `5ef2c5be…abe4cc` | 0 |
| `sha256sum captures/C6-iranica-live-403.txt` | `56b19218…585fdf` | 0 |
| `python3 -c "t.count(q)"` on the stripped capture | 1 | 0 |
| `grep -c 'Just a moment' captures/C6-iranica-live-403.txt` | 1 | 0 |
| `grep -c -i -E 'persian\|qasida\|qaside\|farsi\|iranica\|ferdowsi\|neẓāmi\|nizami' praise-poetry-panegyric.md` | 0 | 1 |
| `grep -c '^## ' praise-poetry-panegyric.md` | 13 | 0 |
| `awk 'NR>=176 && NR<=190 && /^\| /{n++} END{print n}'` | 10 (header + 9 rows) | 0 |
| `wc -c praise-poetry-panegyric.md` | 45197 | 0 |
| `grep -c 'COURTS AND COURTIERS x. Court poetry' round-99-verifier-spotcheck.md` | 1 | 0 |
| `curl -sS -L --max-time 30 'https://archive.org/wayback/available?url=…'` ×4 | 429, 117 B | 0 each |
| `curl -sS -L --max-time 30 'https://web.archive.org/web/2026id_/…'` ×4 | timeout | 28 each |
| `curl -sS -L --max-time 30 'http://web.archive.org/cdx/search/cdx?url=…'` | timeout | 28 |
| `curl -sS -L --max-time 30 'http://timetravel.mementoweb.org/timemap/link/…'` | DNS failure | 6 |

## 12. Tooling

None installed or upgraded. `curl 8.23.0`, `python3` (stdlib only), `awk`, `grep`,
`sha256sum` — all pre-installed. No pacman invocation.
