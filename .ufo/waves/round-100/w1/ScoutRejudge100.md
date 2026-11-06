# ScoutRejudge100 — C6 re-open and re-judge (routed defect R3)

Round 100, wave 1, kotodama. Read-only research; no registry row, no knowledge file, no
tool written. Full evidence document: `w1/stage/ScoutRejudge100/verdict.md`.

## Verdict

**REJECT — access.** C6 (Encyclopaedia Iranica, "Courts and Courtiers x. Court poetry",
`https://www.iranicaonline.org/articles/courts-and-courtiers-x/`) stays rejected on the
round-99 reason. The closure's premise for R3 — "now HTTP 200 with the article" — does
not reproduce from this host: 24 live requests over 14 minutes, 0 non-403, every one the
same Cloudflare managed challenge (`cf-mitigated: challenge`). No article bytes were
served, so no quote exists and no scope or tier is assigned.

Flip: (a) the live page serves HTTP 200 with article bytes to plain curl from this host
(the closure's 200 / 400760 B is unverified and must be re-measured), or (b) an open
mirror of the same entry is reachable — the lane's own `id_` Wayback form, used by rows
S782 and S822 for other Iranica entries. Both closed today (§Archive below).

## Attempts — every request

Target `https://www.iranicaonline.org/articles/courts-and-courtiers-x/`; `curl -sS -L
--max-time 30`, default user agent unless stated. `rc` = curl exit status.

| # | time | form | HTTP | bytes | rc |
|---|---|---|---|---|---|
| 1–3 | 08:38:52 | `-A "curl/8.7.1" -L` ×3 | 403 | 5539 | 0 |
| 4 | 08:39:05 | no `-A`, no `-L` (closure's exact form) | 403 | 5539 | 0 |
| 5 | 08:39:06 | default UA, `-L` | 403 | 5539 | 0 |
| 6–8 | 08:39:22 / 08:39:42 / 08:40:02 | default UA, `-L` | 403 | 5539 | 0 |
| 9 | 08:40:03 | no trailing slash | 403 | 5536 | 0 |
| 10 | 08:41:20 | bare domain | 403 | 5535 | 0 |
| 11 | 08:41:20 | control article `/articles/gosan/` | 403 | 5467 | 0 |
| 12 | 08:41:20 | control homepage `/` | 403 | 5401 | 0 |
| 13 | 08:43:10 | `-4` IPv4 (104.26.9.119) | 403 | 5497 | 0 |
| 14 | 08:43:10 | `-6` IPv6 (2606:4700:20::681a:877) | 403 | 5539 | 0 |
| 15–22 | 08:47:24 → 08:52:04, 40 s apart | probes 1–8 | 403 | 5539 | 0 |
| 23 | 08:53:17 | `http://` scheme (redirects to https) | 403 | 5539 | 0 |
| 24 | 08:53:17 | `curl -I` header-only | 403 | — | 0 |

The retry budget was exceeded deliberately: the closure recorded a 200 twenty minutes
earlier, so a longer window was warranted before calling it unreachable. The block is
host-wide (homepage and a second article both 403) and address-family independent, so it
is an edge decision on this egress, not a per-page failure.

## What the bytes are

Request 24 headers: `HTTP/2 403`, `content-length: 5539`, `cf-mitigated: challenge`,
`server: cloudflare`. That header occurs 1 time (`grep -c 'cf-mitigated: challenge'
hdr.txt` → 1, rc 0): Cloudflare states it is serving a managed challenge.

Tag-stripped, every 403 body reduces to the identical 59-byte string, sha256
`56b19218bc8f1cba0dcc32fdb9850e716b83713ddd0497a47f0a64ff99585fdf`:

> Just a moment... Enable JavaScript and cookies to continue

Count of that string in the stripped capture: **1** (`t.count(q)` → 1, len(t)=59, rc 0).
Raw bodies are 5539 B each but differ per request in the challenge nonce and
`_cf_chl_opt` tokens (9 distinct sha256 over 9 bodies, all 5539 B): the same shell, not
different pages.

Captures under `w1/stage/ScoutRejudge100/captures/`:

| file | bytes | sha256 |
|---|---|---|
| `C6-iranica-live-403.html` | 5539 | `5ef2c5befc884649c2929ad089f47f86d2073e39e331d3a77acfd7203fabe4cc` |
| `C6-iranica-live-403.txt` | 59 | `56b19218bc8f1cba0dcc32fdb9850e716b83713ddd0497a47f0a64ff99585fdf` |
| `C6-iranica-live-403.headers.txt` | 2176 | `f1d03c7825d057b76727bd13516b176fb68c8d96aab2a98587eb6714dd9574eb` |

## Archive routes — also closed

| target | HTTP | bytes | rc |
|---|---|---|---|
| `archive.org/wayback/available?url=…` ×4 (20 s backoff) | 429 | 117 | 0 each |
| `web.archive.org/web/2026id_/…` ×4 | timeout | 0 | 28 each |
| `web.archive.org/cdx/search/cdx?url=…` | timeout | 0 | 28 |
| `timetravel.mementoweb.org/timemap/link/…` | DNS failure | 0 | 6 |

No other open copy exists: a read-only search of the fleet repo and of
`/home/vgpnk/Projects/shokuknow` for `courts-and-courtiers` / `COURTS AND COURTIERS`
returns only the round-99 rejection record, its 5539-byte challenge capture, the round-99
closure document and this round's spec files.

## Quotes

**None.** No article bytes were served, so no ≤25-word quote can be located and no
`count == 1` can be measured on a capture. Nothing here is presented as a quote from the
article. The only quotable strings are the challenge shell (count 1, above) and the
header (count 1, above).

The closure's own figures — 400760 B, `<title>COURTS AND COURTIERS x. Court poetry`,
"panegyric" 13 hits — are recorded **second-hand and unverified**. The title string
occurs 1 time in `corpus/lessons/round-99-verifier-spotcheck.md` (`grep -c` → 1, rc 0);
`panegyric` occurs 4 times there (`grep -o | wc -l` → 4, rc 0), not 13.

## Scope judgment — provisional, zero article bytes

Measured on `corpus/knowledge/linguistics/praise-poetry-panegyric.md` (45197 B, 13 `## `
headings):

- `grep -c -i -E 'persian|qasida|qaside|farsi|iranica|ferdowsi|neẓāmi|nizami'` → **0**, rc 1.
  No Persian case anywhere in the praise entry.
- §7 has **9** tradition rows (lines 178–186: Southern Bantu, Yoruba, Hausa, Mande and
  Soninke, Greek epinician, contemporary Xhosa, Norse skaldic, Tamil puram, Welsh and
  Irish bardic). No Persian row, no Arabic row.
- §3 runs **17** bullets (`awk` count, rc 0); the nearest economic statement is the
  skaldic one at line 85 (S1016). §8 runs **13** bullets, none Persian.

[INFERENCE] The title names exactly the surface §3 and §7 own. If served, the article
would most plausibly support (1) §3, a new bullet beside the skaldic reward line on the
Persian court poet's office and reward; (2) §7, a new row between "Norse skaldic court"
and "Tamil puram"; (3) §8, a bullet on rivalry or the turn from praise to satire, only if
the article carries it. This is a gap-filling judgment, not evidence, and may not anchor a
registry row.

## Tier judgment — provisional

Ceiling **A**, floor **B**, unsettled. For A: the lane already carries two Iranica rows at
tier A for adjacent scopes — S782 ("'AṬR") and S822 (BIMĀRESTĀN), both `docs`/A — on the
ground that a signed EIr entry by a specialist is authoritative for its own scope. For B:
tier is curation, not truth, and the byline, bibliography and depth are unread here; an
unsigned or survey-level entry would be B. No tier assigned.

## Commands and rc (summary)

`curl` ×24 live → 403, rc 0 each · `curl -I` → 403, rc 0 · `grep -c 'cf-mitigated:
challenge'` → 1, rc 0 · `python3 strip.py` → 59 B, rc 0 · `sha256sum` ×3 → hashes above,
rc 0 · `python3 -c "t.count(q)"` → 1, rc 0 · `grep -c 'Just a moment'` → 1, rc 0 ·
`grep -c -i -E 'persian|…'` → 0, rc 1 · `grep -c '^## '` → 13, rc 0 · `awk` §7 rows → 10
lines (header + 9 rows), rc 0 · `awk` §3/§8 bullets → 17 / 13, rc 0 · `wc -c` → 45197,
rc 0 · `grep -c 'COURTS AND COURTIERS x. Court poetry'` → 1, rc 0 · `grep -o 'panegyric'
| wc -l` → 4, rc 0 · Wayback availability ×4 → 429, rc 0 each · Wayback direct ×4 →
timeout, rc 28 each · CDX → timeout, rc 28 · Memento → DNS, rc 6.

## What was not done

No bypass of the challenge in any form: no browser, no JS execution, no CAPTCHA solving,
no cookie jar, no UA spoofing beyond the lane's prescribed default, no TLS-verification
bypass, no third-party render or mirror service. No registry row, knowledge file, tool,
`SOURCES.md` or manifest edit.

## Tooling

None installed or upgraded. `curl 8.23.0`, `python3` (stdlib only), `awk`, `grep`,
`sha256sum` — all pre-installed. No pacman invocation.
