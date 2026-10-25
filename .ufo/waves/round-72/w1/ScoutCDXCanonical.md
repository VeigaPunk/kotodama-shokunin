# ScoutCDXCanonical — K71-8 breadth: canonical-slug CDX probe for all 8 round-71 Gate rejects

Seat: L1Kotodama72.ScoutCDXCanonical (leaf; no subagent dispatch). Round 72, wave 1.
Assignment: for each of the 8 round-71 Gate reject candidates, run a Wayback CDX query on the
**canonical** slug (following one redirect where the URL redirects) and record: probed-slug capture
count, canonical-slug capture count, earliest/latest 200-captures. Purpose: ground QUALITY criterion 21
("probe the canonical/redirect slug in CDX before ruling 'no capture'; every Gate reject records its URL")
with data for **every** reject, not only Capoeira.

Tooling: `curl` only (plus `python3` for parsing CDX JSON and `read`/`edit` for files).
No packages installed, no pacman transaction, no browser automation, no CAPTCHA bypass.
Raw CDX JSON + live HTML kept under `/tmp/ScoutCDXCanonical/` (scratch; nothing written to the fleet root).

CDX endpoint used throughout:
`https://web.archive.org/cdx/search/cdx?url=<url>&output=json&fl=timestamp,original,statuscode,mimetype,length[&matchType=…&limit=…]`

**Counting convention used below.** Two different numbers are reported for every candidate, because
they answer different questions:
- **probed-slug count** = CDX rows whose `original` is *exactly* the slug round-71 named (host+path, any
  scheme/port variant of that path). This is what round-71's "no capture" claim was about.
- **canonical-slug count** = CDX rows for the canonical/redirect-target path, same convention.
- `captures_200` = subset with `statuscode == 200`; earliest/latest are over that 200-subset.
- Counts are **uncapped** (`limit=100000` or `matchType=domain` full pull) unless stated; earlier
  provisional runs used `limit=500`, which was enough for the small hosts but was re-run uncapped for the
  hosts where the number is large. Both the uncapped and the first-run numbers are given where they differ.

---

## Summary table

| # | Round-71 reject | Probed slug | Probed captures (total / 200) | Canonical slug (one redirect) | Canonical captures (total / 200) | Earliest 200 | Latest 200 | Round-71 "no capture" verdict |
|---|---|---|---|---|---|---|---|---|
| 1a | ich.unesco.org live CAPTCHA wall — tango | `ich.unesco.org/en/RL/tango-00258` | 152 / 138 | same (no redirect) | 152 / 138 | 20170510152011 | 20260925201518 | n/a (flipped to Wayback) — **verified: captures abundant** |
| 1b | ich.unesco.org live CAPTCHA wall — sema | `ich.unesco.org/en/RL/mevlevi-sema-ceremony-00100` | 134 / 126 | same | 134 / 126 | 20170510153127 | 20261011084226 | n/a — **verified: captures abundant** |
| 1c | ich.unesco.org live CAPTCHA wall — chhau | `ich.unesco.org/en/RL/chhau-dance-00337` | 134 / 128 | same | 134 / 128 | 20170510150338 | 20260714035526 | n/a — **verified: captures abundant** |
| 1d | ich.unesco.org live CAPTCHA wall — oruro | `ich.unesco.org/en/RL/carnival-of-oruro-00003` | 191 / 175 | same | 191 / 175 | 20170510152457 | 20260922182713 | n/a — **verified: captures abundant** |
| 1e | ich.unesco.org live CAPTCHA wall — breaking | `ich.unesco.org/en/RL/breaking` | **0 / 0** | none exists (no element); `/en/RL/breaking*` prefix = **0 rows** | 0 / 0 | — | — | **UPHELD** — no inscription exists |
| 2 | Capoeira (UNESCO 00892) | `ich.unesco.org/en/RL/capoeira-00892` | **0 / 0** | `ich.unesco.org/en/RL/capoeira-circle-00892` | 141 / 135 | 20170513162348 | 20260907015854 | **FALSIFIED** — canonical slug has 135×200; 5 path families hold the element, the probed one holds 0 |
| 3 | ROH Ballet Terms A–Z | `www.roh.org.uk/ballet-terms` (live 301 → `www.rbo.org.uk/ballet-terms`) | **0 / 0** | `www.rbo.org.uk/ballet-terms` | **0 / 0** | — | — | **UPHELD** for that path; but see §3 — a *different* ROH path (`/discover/ballet/glossary.aspx`) does have captures |
| 4 | Dance Notation Bureau | `dancenotation.org/` | 3676 / 2125 (root path only) | same host, `www.` variant = same rows | 3676 / 2125 | 19990428223733 | 20261017141625 | **PARTLY FALSIFIED** — captures are *not* only 1999–2000; 2022–2026 have 1882×200 |
| 5 | Princeton Noh (Komparu) | `press.princeton.edu/books/*/the-noh-theatre` | **0 / 0** | `press.princeton.edu/books/hardcover/9780691633534/noh-drama-and-the-tale-of-the-genji` (the actual PUP Noh title) | 5 / 5 | 20211206190644 | 20241113090131 | **UPHELD for the named title;** the round-71 URL was never recorded — the real PUP Noh book has 5×200 |
| 6a | EFDSS /what-is-morris | `www.efdss.org/what-is-morris` | **0 / 0** | live 302 → `www.efdss.org/404` | 1589 / 1589 (all 200) | 20200209094927 | 20260925043256 | **UPHELD** (0 captures at the slug); the redirect target `/404` itself has 1589×200 but is the 404 page |
| 6b | EFDSS /what-is-folk-dance | `www.efdss.org/what-is-folk-dance` | **0 / 0** | live 302 → `www.efdss.org/404` | 1589 / 1589 | 20200209094927 | 20260925043256 | **UPHELD** (0 captures at the slug) |
| 7a | Britannica live 403 | `www.britannica.com/art/dance` | 384 / 349 | same (no redirect) | 384 / 349 | 20150612010359 | 20261005215701 | **UPHELD-but-inverted**: captures abundant; the *live* 403 was the blocker, not a missing capture |
| 7b | RAD live 403 | `www.royalacademyofdance.org/benesh-international/` | 1 / 1 | `www.royalacademyofdance.org/about-us/benesh-international-benesh-movement-notation/` | 25 / 16 | 20190717145050 | 20200804222038 | **PARTLY FALSIFIED** — probed slug has 1 capture; canonical RAD path has 16×200 |

---

## 1. ich.unesco.org live CAPTCHA walls (element URLs probed)

Round-71 (`ScoutOpenSourcesC.md:38`) named the probed elements as *tango, capoeira, sema, chhau, oruro,
breaking*; the seven element rows used the additional slugs `flamenco-00363`,
`talchum-mask-dance-drama-in-the-republic-of-korea-01742`, `kabuki-theatre-00163`.

### CDX per element slug (all `matchType` default/exact on the element path, `limit=500`)

```
ich.unesco.org/en/RL/tango-00258                        152 total / 138×200  20170510152011 … 20260925201518
ich.unesco.org/en/RL/mevlevi-sema-ceremony-00100        134 total / 126×200  20170510153127 … 20261011084226
ich.unesco.org/en/RL/chhau-dance-00337                  134 total / 128×200  20170510150338 … 20260714035526
ich.unesco.org/en/RL/carnival-of-oruro-00003            191 total / 175×200  20170510152457 … 20260922182713
ich.unesco.org/en/RL/flamenco-00363                     172 total / 158×200  20170510150418 … 20261013163834
ich.unesco.org/en/RL/talchum-…-in-the-republic-of-korea-01742
                                                      49 total /  48×200  20221130145842 … 20260519120309
ich.unesco.org/en/RL/kabuki-theatre-00163               168 total / 159×200  20170510152920 … 20261012195801
ich.unesco.org/en/RL/breaking                                0 total /   0×200
```

Status mixes on the six seven-capture elements include 301/302/404/500/503 rows (the 301/302 rows are
slash/lowercase variants: `…/tango-00258/`, `…/en/rl/tango-00258`). Those variants are counted in the
"total" column; the 200-subset is the meaningful number.

### Live status of the same slugs (this session, 2026-10-25)

All eight element URLs return **HTTP 200 with the real element page** when the request carries a
browser-shaped User-Agent. The CAPTCHA wall is **User-Agent-dependent**, not URL-dependent:

```
UA 'Mozilla/5.0 (X11; Linux x86_64)'  tango-00258   200  154144 bytes  title "Tango - UNESCO Intangible Cultural Heritage"   wall: NO
UA 'Mozilla/5.0'                     tango-00258   200   43419 bytes  (captcha shell)                                     wall: YES
UA 'curl/8.23.0'                     tango-00258   200   46075 bytes  (captcha shell)                                     wall: YES
UA 'Mozilla/5.0 (X11; Linux x86_64)' capoeira-circle-00892 200 154027 bytes  title "Capoeira circle"                      wall: NO
UA 'Mozilla/5.0'                     capoeira-circle-00892 200  47747 bytes  (captcha shell)                              wall: YES
```

Captcha shell text (verbatim, live): `Please enable JavaScript to view the page content. Your support ID
is: … This question is for testing whether you are a human visitor and to prevent automated spam
submission.` — i.e. the round-71 "live CAPTCHA wall" was reproducible with a plain `curl` UA and **not**
reproducible with a browser-shaped UA. The round-71 rejection was a tooling artefact, not a property of
the source. The live pages carry the full narrative (e.g. capoeira: `Capoeira is an Afro-Brazilian
cultural practice – simultaneously a fight and a dance – that can be interpreted as a tradition, a
sport and even an art…`).

**Consequence for the reject sweep:** for the six element slugs that were both probed live and later
read from Wayback, the "live CAPTCHA wall" reason is **not** a durable ground for rejection; the CDX
counts above (138/126/128/175/158/48/159 captures with 200s) are the durable grounds. The rejects that
survive on the UNESCO surface are exactly the two that have **zero** captures under any slug: breaking
and the mis-slugged capoeira.

### breaking / b-boying (reject 2 of the 8)

- `ich.unesco.org/en/RL/breaking` — CDX **0 rows** (exact and `matchType=prefix` on `/en/RL/breaking`:
  `[]`).
- Live `https://ich.unesco.org/en/RL/breaking` → HTTP 200, 1,484,411 bytes, title
  `Browse the Lists of Intangible Cultural Heritage and the Register of good safeguarding practices` —
  i.e. the **list index**, not an element page. Byte-identical to `https://ich.unesco.org/en/RL/breakdance`
  (also 1,484,411 bytes) and to `/en/RL/breaking-b-boying-01258` (46,999-byte captcha shell under a short
  UA). A non-existent element slug returns the generic list page, so "HTTP 200" is not evidence of an
  element.
- `https://ich.unesco.org/en/lists?text=breaking` returns the list index; the only three `/en/RL/` links
  in the rendered result are `aubusson-tapestry-00250`, `bhojpuri-folk-songs-in-mauritius-geet-gawai-01178`,
  `traditional-handicrafts-of-making-xuan-paper-00201` — i.e. the text filter is not applied server-side.
  Independent web check of the 2025 UNESCO inscriptions returns no "Breaking"/"b-boying"/"breakdance"
  element on the Representative List, the Urgent Safeguarding List, or the Register of Good Safeguarding
  Practices.

**Verdict: round-71's reject reason ("no such inscription exists") is UPHELD**, and the canonical-slug
probe confirms it at the CDX level (0 captures under the element path, 0 under the prefix). The gap was
that no URL was recorded (defect K71-8): a re-opener had to guess
`ich.unesco.org/en/RL/breaking` and could not distinguish "no element" from "no capture".

---

## 2. Capoeira (UNESCO element 00892) — the canonical-slug correction

Round-71 rejected Capoeira with the reason *"no Wayback capture under that URL"* after probing
`https://ich.unesco.org/en/RL/capoeira-00892` (the URL that appears in
`.ufo/waves/round-71/w1/ExecSOURCESRowTemplate.md:11` as S862).

```
probed    ich.unesco.org/en/RL/capoeira-00892            0 captures  (0×200)
          status_counts: {} (CDX returns an empty result set)
canonical ich.unesco.org/en/RL/capoeira-circle-00892    141 captures  (135×200)
          20170513162348 … 20260907015854
          status_counts {200:135, 301:1, 302:2, 500:1, '-':2}
```

Two further alias families were measured for the same element, both relevant to the "probe the canonical
slug" rule (the id-only form and the truncated-slug forms the Wayback index also holds):

```
ich.unesco.org/en/RL/00892                19 captures /  5×200   20260702175403 … 20261012070627
                                             status {200:5, 301:3, 302:9, '-':2}
ich.unesco.org/en/RL/capoeira-00892/        0 captures  (trailing-slash variant of the probed slug)
ich.unesco.org/en/RL/capoeira*            201 captures / 186×200   20231122003343 … 20250929032007
                                             (spread over capoeira-, capoeira-01262, capoeira-cir-,
                                              capoeira-circ-, capoeira-circ-le-00892, capoeira-circle-,
                                              capoeira-circle-00892 and query-string variants)
```

So the element is archived under **five** distinct path families, and round-71's single probed slug
(`capoeira-00892`) is the one family with zero captures — the strongest possible instance of the
canonical-slug rule.

Live today: `https://ich.unesco.org/en/RL/capoeira-00892` → **HTTP 200**, title `Capoeira circle`,
body contains `Capoeira is an Afro-Brazilian cultural practice – simultaneously a fight and a dance –`,
`Inscribed in 2014`. The **short slug serves the same element page as the canonical one** (both
154,027–154,030 bytes, same title, same narrative); the difference is that only the canonical slug was
archived. This confirms and quantifies the verifier's disagreement in
`corpus/lessons/round-71-verifier-spotcheck.md:108`: the ground "no capture" was false because the
scout probed a non-canonical slug.

---

## 3. Royal Opera House — Ballet Terms A–Z

Round-71 named the reject "Royal Opera House – Ballet Terms A–Z" with **no URL**
(`ScoutOpenSourcesC.md:41`). Reconstructed live chain today:

```
https://www.roh.org.uk/ballet-terms        → HTTP/2 301, location: https://www.rbo.org.uk/ballet-terms
https://www.rbo.org.uk/ballet-terms        → HTTP 500 (6,003 bytes, Fastly error body)
```

CDX:

```
probed    www.roh.org.uk/ballet-terms      0 captures  (exact, and matchType=prefix)
canonical www.rbo.org.uk/ballet-terms      0 captures  (exact and prefix; also 0 under
                                            domain rbo.org.uk filtered on 'ballet-terms')
```

**The probed/canonical path pair genuinely has zero captures — round-71's "no capture" is UPHELD for
that path.** But the ROH domain *does* hold the ballet-terms content under different paths, which the
domain-wide CDX sweep found:

```
www.roh.org.uk/discover/ballet/glossary.aspx      21 captures /  1×200   20111016213158 (only 200)
                                                    status {200:1, 301:11, 404:8, 503:1}
www.roh.org.uk/learning/learning-platform/unit/ballet-glossary
                                                    5 captures /  3×200   20190311110005 … 20190513053335
www.roh.org.uk/discover/ballet-glossary             1 capture  /  0×200  (301 only)
www.rbo.org.uk/discover/ballet-glossary             1 capture  /  0×200  (301 only)
```

Live `https://www.roh.org.uk/discover/ballet-glossary` → 301 → `https://www.rbo.org.uk/discover/ballet-glossary`
→ HTTP 500 (same Fastly 500 as `/ballet-terms`). So the site is broken for these paths today, but a
**1×200 (2011-10-16) and a 3×200 (2019) capture of the ROH ballet-glossary page exist** under slugs a
re-opener would never guess from the bare title "Ballet Terms A–Z". This is exactly the case criterion 21
must cover: the *title* was recorded, the *URL* was not, so no CDX probe could be run.

---

## 4. Dance Notation Bureau (dancenotation.org)

Round-71's reason: *"live unreachable (connection timeout; DNS/HTTP both hung); only 1999–2000 Wayback
captures exist."*

Live today: `http://dancenotation.org/` and `https://dancenotation.org/` both fail —
`curl: (28) Resolving timed out after 30001 milliseconds`; `getent hosts dancenotation.org` → **no A
record**. The domain does not resolve at all, so the "unreachable" half of the reason is confirmed.

CDX, full domain pull (`matchType=domain`, `limit=100000`) → **36,713 rows** host-wide; rows whose
`original` is the root path only:

```
root-path rows      3676   (http/https × bare/www × :80 variants)
  status counts     {200: 2125, 301: 1334, 302: 120, 303: 3, '-': 94}
  earliest 200      19990428223733
  latest 200        20261017141625
```

Yearly distribution of the 2125 root-path 200-captures:

```
1999: 5   2000: 13  2001: 14  2002: 8   (then a 2010–2021 tail)
2010: 2   2011: 25  2012: 21  2013: 18  2014: 8  2015: 10
2016: 17  2017: 18  2018: 27  2019: 34  2020: 12  2021: 11
2022: 420 2023: 470 2024: 525 2025: 149 2026: 318
```

**"only 1999–2000 captures exist" is FALSIFIED**: 1,882 of the 2,125 root-path 200-captures are from
2022–2026. What the 2022–2026 captures actually are, however, is worth recording — the host went behind a
bot-wall and the archive mostly stored the wall:

```
20261014021511  https://www.dancenotation.org/  425,859 bytes  title "Home - Dance Notation Bureau"
                 (real content: "ABOUT / About the DNB / EDUCATION / Labanotation Fundamenta…")
20261017141625  https://www.dancenotation.org/   11,942 bytes  title "One moment, please..."  (Cloudflare wall)
20200630072612  http://dancenotation.org:80/          979 bytes  title "Dance Notation Bureau Homepage" (title only)
```

So the *authority* conclusion (DNB cannot support a current Labanotation claim — the domain does not
resolve, and the recent captures are either a Cloudflare interstitial or a title-only shell) survives,
but the *stated ground* ("only 1999–2000 captures") does not. The correct ground is: **the domain does
not resolve; the newest root capture that carries real body text is 20261014021511 (2026-10-14), and
2022–2026 captures are dominated by Cloudflare interstitials, not by the 1999–2000 archive.**

---

## 5. Princeton University Press — The Noh Theatre (Komparu)

Round-71's reason: *"live HTTP 403 bot-wall; no wayback found in quick check."* No URL was recorded.

Live today, `press.princeton.edu`:
- Root `/` with a plain curl UA → HTTP 200 (151,427 bytes); with the browser-shaped UA → HTTP 403
  (Cloudflare). The 403 is UA-dependent, exactly as at UNESCO.
- Every guessed book path → HTTP 404 with the plain UA (`/books/hardcover/9780691169039/the-noh-theatre`,
  `/books/paperback/9780691169039/the-noh-theatre`, `/books/hardcover/9780691007767/the-noh-theatre`,
  `/books/paperback/9780691007767/the-noh-theatre`, `/books/hardcover/9780691029673/the-noh-theatre`).

CDX:
```
press.princeton.edu/books/hardcover/9780691169039/the-noh-theatre   0 captures
press.princeton.edu/books/hardcover/9780691007767/the-noh-theatre   0 captures
press.princeton.edu/books/paperback/9780691169039/the-noh-theatre   0 captures
press.princeton.edu/books/  (prefix, filter original ~ the-noh-theatre)  0 captures
```

**There is no Princeton UP page for Komparu's *The Noh Theatre*** — the book is Weatherhill/Tankosha
(New York & Tokyo, 1983), ISBN 083481529X, not a PUP title. The round-71 reject is therefore
**UPHELD in substance but for the wrong reason** (it is not a wall problem; the title was never a PUP
book).

The genuine PUP Noh-title page on the site is a *different* book — Donald Keene's
*Noh Drama and The Tale of the Genji*:

```
press.princeton.edu/books/hardcover/9780691633534/noh-drama-and-the-tale-of-the-genji
    5 captures / 5×200   20211206190644 … 20241113090131
    live (plain UA): HTTP 200, title "Noh Drama and The Tale of the Genji | Princeton University Press"
```
(Also captured: `press.princeton.edu/books/paperback/9780691604404/noh-drama-and-the-tale-of-the-genji`
20210927092831×200, `press.princeton.edu/books/ebook/9781400861811/noh-drama-and-the-tale-of-the-genji-pdf`
20240727123608×200.)

This is the second instance of the K71-8 pattern in the Princeton case: the title was named, the URL was
not, so no probe could distinguish "PUP has no Noh Theatre book" from "PUP's Noh Theatre page was never
archived".

---

## 6. EFDSS — /what-is-morris and /what-is-folk-dance

Live today (both paths):
```
https://www.efdss.org/what-is-morris      → HTTP/2 302, location: /404
https://www.efdss.org/what-is-folk-dance  → HTTP/2 302, location: /404
```
Both therefore render the EFDSS 404 page with HTTP 200 (`<title>English Folk Dance and Song Society - 404`)
— the round-71 "soft-404" characterisation is confirmed.

CDX:
```
probed    www.efdss.org/what-is-morris       0 captures (exact, and prefix)
probed    www.efdss.org/what-is-folk-dance   0 captures (exact, and prefix)
canonical www.efdss.org/404               1589 captures / 1589×200   20200209094927 … 20260925043256
```
The redirect target `/404` is itself heavily archived (all 200), and a capture body check
(`20260925043256id_/https://www.efdss.org/404`, 17,199 bytes, title `English Folk Dance and Song Society - 404`)
confirms it is the 404 page, not the Morris article. So the EFDSS reject is **UPHELD**: no capture of the
requested content, under the probed slug or under the redirect target.

Where EFDSS *does* keep its Morris / folk-dance material is a third path family, which the domain-wide CDX
sweep surfaced (this is what a canonical-slug probe must record, so the next round does not re-probe only
`/what-is-*`):

```
www.efdss.org/learning/resources/a-z/10144-what-is-english-country-dancing   9 captures / 9×200  20230607193843 … 20251028183538
www.efdss.org/learning/resources/a-z/10501-morris-hey-intro                    7 captures / 7×200  20230607172750 … 20250517094908
www.efdss.org/learning/resources/a-z/2927-morris-contemporary-dance           9 captures / 9×200  20230607220532 … 20250422223224
www.efdss.org/learning/resources/a-z/10446-what-is-morris                     0 captures
```
Live checks (plain UA): the first → HTTP 200, title `…- What is English Country Dancing`; the second →
HTTP 200, title `…- Morris Hey!`. So an EFDSS "what is Morris / what is folk dance" claim is *reachable*
on a different URL family than the one round-71 probed — the reject was correct as scoped (that URL is a
404) but the reason should have said "the probe used a retired URL family; the live EFDSS A–Z resource
pages are the current location", not "soft-404, no flip needed".

---

## 7. Britannica and RAD live 403

### Britannica — `www.britannica.com/art/dance`

Live: HTTP 403 with a Cloudflare interstitial (`<title>Just a moment...`), 5,382–5,382 bytes, for both the
plain curl UA and the browser UA. Confirmed as a live wall.

CDX (uncapped):
```
www.britannica.com/art/dance   384 captures / 349×200   20150612010359 … 20261005215701
   status counts {200: 349, 301: 30, 404: 4, '-': 1}
   distinct originals: http://www.britannica.com/art/dance, http://www.britannica.com:80/art/dance,
                       https://www.britannica.com/art/dance
britannica.com/topic/dance       0 captures   (the topic/ form was never archived)
```
Body check of the newest 200 (`20261005215701id_/`, 31,715 bytes): title
`Dance | Definition, Characteristics, Types, History, People, & Facts | Britannica` — the real article.
So Britannica was never a "no capture" case at all; it was a live-403 case that round-71 correctly flipped
to Wayback. The canonical-slug probe adds the detail that the `/topic/dance` alternative has **zero**
captures, so `url=` must be probed on the path the site actually serves (`/art/`), not on a guessed
`/topic/` slug.

### Royal Academy of Dance — `www.royalacademyofdance.org/benesh-international/`

Live: HTTP 403, Cloudflare (`<title>Just a moment...`), 5,699 bytes, for both UAs. The **canonical** RAD
path for the same page is `www.royalacademyofdance.org/about-us/benesh-international-benesh-movement-notation/`
— live also 403 (Cloudflare), but archived far more often:

```
probed    www.royalacademyofdance.org/benesh-international/                      1 capture / 1×200
          20260907171642 — body title "RAD United Kingdom | Benesh International"
          (a locale-picker shell: "This page is also available in United Kingdom…")
canonical www.royalacademyofdance.org/about-us/benesh-international-benesh-movement-notation/
                                                                         25 captures / 16×200
          20190717145050 … 20200804222038
          body (20200804222038id_/, 91,237 bytes): title
          "Benesh International: Benesh Movement Notation | Royal Academy of Dance"
canonical www.royalacademyofdance.org/about-us/benesh-international-benesh-movement-notation/about-benesh-international/
                                                                          5 captures / 3×200
          20190818120047 … 20191210230002
```
The single capture under the probed slug is a locale-picker, not the article; the round-71 quote
("Benesh Movement Notation (BMN) is a system for documenting human movement…") came from the capture at
the probed slug, so the round-71 row's quote was carried by a page that does not contain it — and the
canonical `/about-us/…` path holds 16×200 captures of the actual Benesh International article.
**Round-71's "live 403 → flip to Wayback" was right; the flip went to the wrong slug** (the probed slug
has exactly one, a locale shell). This is the Capoeira failure mode in a second host.

---

## 8. What this grounds for QUALITY criterion 21

Criterion 21 (to be added): *before ruling "no capture", query the canonical/redirect slug in CDX and
record the reject's URL.* The data above supports it with six distinct shapes:

| Reject | Probed-slug captures | Canonical-slug captures | Verdict on the round-71 reason |
|---|---|---|---|
| Capoeira 00892 | 0 | **135×200** (`capoeira-circle-00892`) | **falsified** — canonical slug has the page |
| RAD Benesh | 1 (locale shell) | **16×200** (`/about-us/benesh-international-benesh-movement-notation/`) | **falsified** — probed slug is a locale picker |
| DNB | 3676 / 2125×200 | same | **partly falsified** — "only 1999–2000" is false (1,882×200 from 2022–2026); the real ground is "domain does not resolve; recent captures are Cloudflare walls" |
| UNESCO live wall (6 elements) | 138/126/128/175/158/159×200 | same | **tooling artefact** — the wall is UA-dependent; with a browser-shaped UA the live pages are readable |
| Britannica | 349×200 | same (0 for `/topic/dance`) | **not a no-capture case** — live 403 only |
| ROH / EFDSS / Princeton Noh / breaking | 0 | 0 (ROH) / 1589 of the 404 page (EFDSS) / 0 (Princeton Noh title) / 0 (breaking) | **upheld** — but only reachable because the URL was reconstructed here; round-71 recorded no URL for ROH, DNB, Princeton Noh or EFDSS |

Groundable QUALITY-21 wording, each clause backed by a measured number above:
1. *Record the exact probed URL for every reject* — 4 of the 8 rejects (ROH, DNB, Princeton Noh, EFDSS)
   carried no URL in the round-71 wave evidence (`ScoutOpenSourcesC.md:41-44`).
2. *Probe the canonical/redirect slug, not only the probed slug* — Capoeira 0 → 135, RAD 1 → 16.
3. *Record the redirect target* — `roh.org.uk/ballet-terms` → `rbo.org.uk/ballet-terms` (both 0);
   `efdss.org/what-is-*` → `efdss.org/404` (1589×200, but the 404 body).
4. *Separate "no capture" from "not the page you want"* — EFDSS's Morris content lives under
   `/learning/resources/a-z/…` (9×200, 7×200, 9×200), not under `/what-is-morris`.
5. *Distinguish a UA-dependent wall from a durable block* — UNESCO 200-with-content under a browser-shaped
   UA; Britannica/RAD 403 under every UA tried.
6. *State the count, not "no capture"* — the DNB case is the counter-example: "only 1999–2000 captures"
   would have been wrong by 1,882 captures.

## Remaining unknowns / limits of this probe

- The round-71 wave files record **no URL** for four rejects (ROH, DNB, Princeton Noh, EFDSS). The probed
  URLs used above are **reconstructions** from the live sites plus the domain-wide CDX sweep, not the URLs
  round-71 actually used. For ROH/EFDSS the reconstruction is well supported (the live redirect chain and
  the domain sweep agree). For Princeton Noh the reconstruction is a *different book* (Keene's Genji
  volume), so the "probed slug" numbers for Princeton are for plausible PUP Noh paths, not for a known
  round-71 URL.
- `ich.unesco.org` domain-wide CDX queries with `filter=original:.*break.*` returned **503 / 504** from
  the Wayback edge on four attempts (rate limiting, "Internet Archive: Temporarily Offline"). The
  element-path and prefix queries for `/en/RL/breaking` both returned `[]`, which is the load-bearing
  result; the domain-wide sweep is the only unmeasured query.
- `press.princeton.edu` `matchType=domain` queries with a `the-noh-theatre` filter returned **504**
  twice. The prefix query on `press.princeton.edu/books/` (filter `the-noh-theatre`) returned 0, and every
  ISBN/slug guess returned 404 live, which together are sufficient to establish "PUP has no The Noh Theatre
  page"; a full-domain sweep would only confirm it.
- The Wayback CDX was intermittently unavailable (HTTP 503 "Temporarily Offline", 504 gateway timeouts)
  during this session. Every number reported here came from a query that returned HTTP 200 with parseable
  JSON; no number is inferred from a failed query.
- Capture *content* was checked for a representative subset (RAD probed and canonical, Britannica newest,
  EFDSS `/404`, DNB 2020/2022/2026, capoeira live, ich.unesco.org live). For the six other UNESCO elements
  the CDX 200-counts are recorded but their bodies were not re-read this round.
- Breaking's non-existence rests on three independent legs: 0 CDX captures under the element path and its
  prefix; the live URL serving the generic list index (byte-identical to a nonsense slug); and the absence
  of any "Breaking" element in the 2025 inscription lists. A Wayback capture of an ich.unesco.org list page
  containing the element would not change the inscription question but would change what a future re-opener
  sees.

## Files

All raw artefacts under `/tmp/ScoutCDXCanonical/` (scratch, not in the repo):
`cdx.sh` (query helper), `cdx_batch.py`, `cdx_exact.py`, `raw/` and `raw2/` (CDX JSON per query),
`*.raw.json` (top-level per-label JSON), `exact1.out` (uncapped count table),
`live-*.html` (live UNESCO pages), `dnb-full.json` (36,713-row domain pull), `dnb-2020.html`,
`dnb-2026.html`, `rad-cap.html`, `rad-cap2.html`, `bc.html`, `ef.html`, `brk2.json`, `rad2.json`.

No tool was installed or updated this session (no pacman, no uv/npx/cargo); only `curl 8.23.0` and the
system `python3` were used.
