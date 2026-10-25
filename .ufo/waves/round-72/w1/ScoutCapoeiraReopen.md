# ScoutCapoeiraReopen — K71-8 ground truth: the Capoeira UNESCO element re-opened

Seat: `L1Kotodama72.ScoutCapoeiraReopen` (scout, leaf) · wave round-72 / w1 · probe date **2026-10-25**
Scratch dir for all downloads: `/tmp/scoutcapoeira/` (fleet root and lane root untouched except this report file).

## VERDICT (one line)

**The round-71 reject reason "no Wayback capture under that URL" is FALSE.**
The live element returns **HTTP 200 with the full narrative** under both slugs, and the Wayback CDX API lists
**135 captures with status 200** under the canonical slug `ich.unesco.org/en/RL/capoeira-circle-00892`
(earliest `20170513162348`, `20171120140510`, `20171208155324`; latest `20260602141520`, `20260710075531`,
`20260907015854`), and the 2017-12-08 capture **serves the narrative text**.
The reject was caused by probing the **non-canonical slug** `capoeira-00892` (which has **0** captures of any
status) and by reading a wildcard query that surfaced only stub URLs. The flip to Flamenco remains a legitimate
editorial choice; the *stated ground* is what was falsified.

---

## 1. Live fetches — HTTP status, challenge wall, exact sentence

### 1a. Command

```bash
cd /tmp/scoutcapoeira
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
for u in capoeira-00892 capoeira-circle-00892; do
  echo "=== $u ==="
  curl -sS -D "hdr-$u.txt" -A "$UA" -o "body-$u.html" \
    -w "http_code=%{http_code} size=%{size_download} time=%{time_total} redirect=%{redirect_url}\n" \
    "https://ich.unesco.org/en/RL/$u"
done
```

### 1b. Output

```
=== capoeira-00892 ===
http_code=200 size=154205 time=1.590357 redirect=
=== capoeira-circle-00892 ===
http_code=200 size=154208 time=2.137228 redirect=
```

Both URLs return **HTTP 200** with **no redirect** (`redirect=` empty; the server serves both slugs directly).
Response headers (`hdr-capoeira-circle-00892.txt`) show an ordinary Varnish-cached origin response —
`HTTP/1.1 200 OK`, `X-Fresh: 1`, `X-Backend: DEFAULT`, `X-Cache: HIT`, `Content-Type: text/html; charset=UTF-8`,
plus F5 `TS…` cookies — **no** Cloudflare/Imperva challenge headers, no `__cf_chl`, no `503`, no `403`.

### 1c. Challenge wall — the finding is UA-dependent (important correction to the round-71 premise)

The round-71 seat recorded that "ich.unesco.org live pages … return the 'testing whether you are a human visitor'
CAPTCHA frame (curl with browser UA and read both confirmed)". That premise does **not** reproduce with a browser
UA today; what actually happens is the opposite of the round-71 note:

```bash
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
for i in 1 2 3 4 5; do curl -sS -A "$UA" -o "b$i.html" -w "run$i http=%{http_code} size=%{size_download}\n" \
  "https://ich.unesco.org/en/RL/capoeira-circle-00892"; done
for i in 1 2 3 4 5; do curl -sS -o "d$i.html" -w "run$i http=%{http_code} size=%{size_download}\n" \
  "https://ich.unesco.org/en/RL/capoeira-circle-00892"; done
for f in b1 b2 b3 b4 b5 d1 d2 d3 d4 d5; do
  printf "%s phrase=%s challenge=%s\n" "$f" \
    "$(grep -c 'simultaneously a fight and a dance' $f.html)" "$(grep -ci 'human visitor' $f.html)"; done
```

```
run1 http=200 size=154208
run2 http=200 size=154208
run3 http=200 size=154208
run4 http=200 size=154208
run5 http=200 size=154208
run1 http=200 size=46475
run2 http=200 size=45691
run3 http=200 size=47887
run4 http=200 size=41719
run5 http=200 size=41423
b1 phrase=3 challenge=0
b2 phrase=3 challenge=0
b3 phrase=3 challenge=0
b4 phrase=3 challenge=0
b5 phrase=3 challenge=0
d1 phrase=0 challenge=1
d2 phrase=0 challenge=1
d3 phrase=0 challenge=1
d4 phrase=0 challenge=1
d5 phrase=0 challenge=1
```

**Observed:** with a **browser UA** → HTTP 200, 154 KB, narrative present, **no challenge wall** (5/5 runs).
With the **default curl UA** → HTTP 200 but a **45 KB TSPD/F5 "Please enable JavaScript to view the page content …
This question is for testing whether you are a human visitor"** interstitial (5/5 runs), narrative absent.
Also confirmed: an *empty* User-Agent header (`curl -H "User-Agent:"`) returns the full 154 KB page with the
narrative (phrase count 3, no challenge marker), so the trigger is the *default curl token*, not "no UA".

Challenge-wall text, verbatim from the default-UA body (`/tmp/scoutcapoeira/body-defaultua.html`):

> Please enable JavaScript to view the page content. Your support ID is: 5619449045451605053.
> This question is for testing whether you are a human visitor and to prevent automated spam submission.

(The interstitial also carries `window["bobcmn"] = "…TSPD…"` / `window["failureConfig"]` — F5 Shape/TSPD bot
defense. The full 154 KB pages also contain two `TSPD` strings inside the CSP/script preamble, but they are the
*real* document, not the interstitial.)

**Consequence for the correction:** the Capoeira reject is *not* a challenge-wall case at all. The challenge wall
is real but **UA-gated**, and it is bypassed by a browser UA. The round-71 reject reason under review
("no Wayback capture under that URL") is falsified on the CDX side (below) *and* the live side is readable.

### 1d. Canonical slug (the root cause)

```bash
grep -o '<link rel="canonical"[^>]*>' body-capoeira-00892.html body-capoeira-circle-00892.html
```

```
body-capoeira-00892.html:   <link rel="canonical" href="https://ich.unesco.org/en/RL/capoeira-circle-00892" />
body-capoeira-circle-00892.html: <link rel="canonical" href="https://ich.unesco.org/en/RL/capoeira-circle-00892" />
```

Both slugs serve the identical document and **both declare the canonical URL as
`https://ich.unesco.org/en/RL/capoeira-circle-00892`** (title `Capoeira circle - UNESCO Intangible Cultural
Heritage` on both). A `diff` of the two live bodies shows only locale-string differences in the site nav
("Online (-)" vs "En línea (-)", "Athens, Greece" vs "Grecia"); the element narrative is byte-identical.

### 1e. The exact sentence containing "simultaneously a fight and a dance"

Extracted from the `<p class="wiki-text">` element of the live page:

> **Capoeira is an Afro-Brazilian cultural practice – simultaneously a fight and a dance – that can be interpreted
> as a tradition, a sport and even an art form.**

(Full paragraph continues: "Capoeira players form a circle at the centre of which two players engage with one
another. The movements require great bodily dexterity. The other players around the circle sing, chant, clap and
play percussive instruments. Capoeira circles are formed by a group of people of any gender, and comprise a master,
counter-master and disciples. …")

The same sentence also appears twice more on the live page: in `<META NAME="DESCRIPTION" CONTENT="…">` and in
`<meta property="og:description" content="…">` — i.e. **3 occurrences** on each live page. Note the dash is an
en dash `–` (U+2013), not a hyphen, and the sentence is the **first** sentence of the inscription narrative
paragraph.

Command used:

```bash
python3 - <<'EOF'
import re,html
s=open("body-capoeira-circle-00892.html",encoding="utf-8",errors="replace").read()
for m in re.finditer(r'<p[^>]*>([^<]*simultaneously a fight and a dance[^<]*)</p>', s, re.S):
    print(html.unescape(m.group(1)).strip())
EOF
```

---

## 2. Wayback CDX API — canonical slug

### 2a. Command (full listing, status 200)

```bash
curl -sS "http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/capoeira-circle-00892&output=text&fl=timestamp,original,statuscode,mimetype,digest&filter=statuscode:200" -o cdx-circle-all.txt -w "http_code=%{http_code}\n"
echo "total lines: $(wc -l < cdx-circle-all.txt)"
head -3 cdx-circle-all.txt; tail -3 cdx-circle-all.txt
cut -c1-4 cdx-circle-all.txt | sort | uniq -c
```

### 2b. Output

```
http_code=200
total lines: 135
--- FIRST 3 ---
20170513162348 https://ich.unesco.org/en/RL/capoeira-circle-00892 200 text/html LYTJEECQG6GWKFZMPBMOSHZKQSB2EV4R
20171120140510 https://ich.unesco.org/en/RL/capoeira-circle-00892 200 text/html CX57ENEA3QHQBKOZWATRDRRDJU2B4TUK
20171208155324 https://ich.unesco.org/en/RL/capoeira-circle-00892 200 text/html THPO4O4RXMLCS7VUAEH6TRS55NVNE2KA
--- LAST 3 ---
20260602141520 https://ich.unesco.org/en/RL/capoeira-circle-00892 200 text/html DS4FLUXDCQTY4W4GTI2QIPWSO6SV5EFB
20260710075531 https://ich.unesco.org/en/RL/capoeira-circle-00892 200 text/html WFUCGFPTNXHK7KGSE7O25R2CC34JIHWU
20260907015854 https://ich.unesco.org/en/RL/capoeira-circle-00892 200 text/html ZTJLZA344JDXKUKUMUF7OF6QAW6CDV3L
--- year histogram ---
      3 2017
      3 2018
      8 2019
      7 2020
     40 2021
     21 2022
     11 2023
     17 2024
     14 2025
     11 2026
```

**Earliest three status-200 captures:** `20170513162348`, `20171120140510`, `20171208155324`
**Latest three status-200 captures:** `20260602141520`, `20260710075531`, `20260907015854`
**Total status-200 captures under the canonical slug: 135** (2017 → 2026, continuous).

(CDX default ordering is already ascending by timestamp; a `sort` of the file reproduces the same head/tail, so
the "earliest three" are unambiguous.)

### 2c. The probed slug has zero captures — the root cause of the false reject

```bash
curl -sS "http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/capoeira-00892&output=text&fl=timestamp,original,statuscode&filter=statuscode:200" -o cdx-plain-all.txt
echo "total: $(wc -l < cdx-plain-all.txt)"
# and with NO status filter:
curl -sS "http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/capoeira-00892&output=text&fl=timestamp&limit=0" | wc -l
# and as a prefix (would catch capoeira-00892* variants):
curl -sS "http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/capoeira-00892&matchType=prefix&output=text&fl=timestamp,original,statuscode&limit=20"
```

```
total: 0
total-all: 0
(prefix query produced no rows)
```

`ich.unesco.org/en/RL/capoeira-00892` has **zero** captures of **any** status. So the round-71 statement
"no Wayback capture under that URL" was *literally true for the URL it probed* and *false for the element*.
That is exactly the failure class K71-8 names.

### 2d. Why the wildcard query misled the round-71 seat

The round-71 evidence (`corpus/lessons/round-71.md:36`; `.ufo/waves/round-71/w1/ScoutOpenSourcesC.md:40`) says:
"no Wayback capture under that URL; CDX wildcard only surfaces `capoeira-` stub captures and the 2017 Basel Carnival
page (element id collision 01262 ≠ capoeira)". Reproduced:

```bash
curl -sS "http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/capoeira*&output=text&fl=timestamp,original,statuscode&collapse=urlkey" | sort | head -14
```

```
20170513162348 https://ich.unesco.org/en/RL/capoeira-circle-00892 200
20170517012355 https://ich.unesco.org/en/RL/capoeira-circle-00892?include=film_inc.php&id=31116&width=700&call=film 200
20171122011704 https://ich.unesco.org/en/RL/capoeira-circle-00892?logout=1 200
20171122192651 https://ich.unesco.org/en/RL/capoeira-circle-00892?RL=00892 200
20171124053137 https://ich.unesco.org/en/RL/capoeira-circle-00892?logout=1&RL=00892 200
20230714203439 http://ich.unesco.org/en/RL/capoeira-circ-le-00892 301
20230714203516 https://ich.unesco.org/en/RL/capoeira-circ- 200
20231015130931 http://ich.unesco.org/en/RL/capoeira-cir- 302
20231025064922 https://ich.unesco.org/en/RL/capoeira-circle-00892Cadastro 200
20231121190436 http://ich.unesco.org/en/RL/capoeira- 302
20250126061949 https://ich.unesco.org/en/RL/capoeira-circle-01007 200
20250415233908 http://ich.unesco.org/en/RL/capoeira-circle- 302
20250625015345 https://ich.unesco.org/en/RL/capoeira-01262 200
20250927012515 http://ich.unesco.org/en/RL/capoeira-in-brazil-00892 302
```

The wildcard **does** contain the real element captures (`capoeira-circle-00892` × 5 rows, 2017), but they are
**interleaved** with stub/redirect rows and — critically — CDX's **default `limit`/ordering** put the 2023–2025
stub rows first, so a first-N-rows read sees only stubs and the Basel Carnival row. (CDX default ordering is
*ascending* by timestamp only within a `urlkey` collapse; with a wildcard the `collapse=urlkey` rows come back in
a different order, so the raw first page shows the stub cluster.) The round-71 seat's read of "only stub captures
and Basel Carnival" was a **truncated-wildcard artifact**, not evidence of absence.

Note `capoeira-01262` really is a different element: `curl https://ich.unesco.org/en/RL/capoeira-01262` returns
`<TITLE>Basel Carnival - UNESCO Intangible Cultural Heritage</TITLE>` — confirming the round-71 seat's
"element id collision 01262 ≠ capoeira" observation. That part was correct; the inference drawn from it was not.

### 2e. matchType=prefix cross-check

```bash
curl -sS --max-time 60 "http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/capoeira&matchType=prefix&output=text&fl=timestamp,original,statuscode&filter=statuscode:200&collapse=urlkey&limit=20"
```

```
20231122003343 https://ich.unesco.org/en/RL/capoeira- 200
20250625015345 https://ich.unesco.org/en/RL/capoeira-01262 200
20250629112335 https://ich.unesco.org/en/RL/capoeira-01262 200
20231015130940 https://ich.unesco.org/en/RL/capoeira-cir- 200
20230714203516 https://ich.unesco.org/en/RL/capoeira-circ- 200
20230714203548 https://ich.unesco.org/en/RL/capoeira-circ-le-00892 200
20250415233910 https://ich.unesco.org/en/RL/capoeira-circle- 200
20170513162348 https://ich.unesco.org/en/RL/capoeira-circle-00892 200
20170517012355 https://ich.unesco.org/en/RL/capoeira-circle-00892?include=film_inc.php&id=31116&width=700&call=film 200
20171122011704 https://ich.unesco.org/en/RL/capoeira-circle-00892?logout=1 200
20171124053137 https://ich.unesco.org/en/RL/capoeira-circle-00892?logout=1&RL=00892 200
20171122192651 https://ich.unesco.org/en/RL/capoeira-circle-00892?RL=00892 200
20231025064922 https://ich.unesco.org/en/RL/capoeira-circle-00892Cadastro 200
20260220102137 https://ich.unesco.org/en/RL/capoeira-circle-00892%7Ctitle=UNESCO 200
20250126061949 https://ich.unesco.org/en/RL/capoeira-circle-01007 200
20251208023606 https://ich.unesco.org/en/RL/capoeira-circle-of-brazil-01005 200
20250929032007 https://ich.unesco.org/en/RL/capoeira-in-brazil-00892 200
```

The prefix query independently surfaces `capoeira-circle-00892` at `20170513162348` with status 200 — a second,
independent confirmation that captures exist under the canonical slug.

---

## 3. Fetching a 2017 capture — narrative text serves

### 3a. Command

```bash
curl -sS -L -o wb-20171208155324.html \
  -w "http_code=%{http_code} size=%{size_download} final=%{url_effective}\n" \
  "https://web.archive.org/web/20171208155324/https://ich.unesco.org/en/RL/capoeira-circle-00892"
```

### 3b. Output

```
http_code=200 size=131006 final=https://web.archive.org/web/20171208155324/https://ich.unesco.org/en/RL/capoeira-circle-00892
```

### 3c. Content check

```bash
python3 - <<'EOF'
import re,html
s=open("wb-20171208155324.html",encoding="utf-8",errors="replace").read()
print("len",len(s)); print("phrase count:", s.count("simultaneously a fight and a dance"))
i=s.find("simultaneously a fight and a dance")
print(html.unescape(re.sub(r'<[^>]+>','',s[max(0,i-200):i+900])).strip())
print(re.search(r'<title>(.*?)</title>',s,re.S|re.I).group(1).strip())
EOF
```

```
len 130923
phrase count: 1
© IPHAN/Bossa Pro
Capoeira is an Afro-Brazilian cultural practice – simultaneously a fight and a dance – that can be interpreted as
a tradition, a sport and even an art form. Capoeira players form a circle at the centre of which two players engage
with one another. The movements require great bodily dexterity. The other players around the circle sing, chant,
clap and play percussive instruments. Capoeira circles are formed by a group of people of any gender, and comprise
a master, counter-master and disciples. The master is the bearer and guardian of the knowledge of the circle, and
is expected to teach the repertoire and to maintain the group's cohesion and its observance to a ritual code. …
Capoeira circle - intangible heritage - Culture Sector - UNESCO
```

**Confirmed:** the 2017-12-08 capture **serves the narrative** (phrase present once, in the narrative paragraph;
2017 title template `Capoeira circle - intangible heritage - Culture Sector - UNESCO`, before the 2026
`UNESCO Intangible Cultural Heritage` retitle). It is **not** a challenge frame and **not** a soft-404.

---

## 4. Grounding against the round-71 filed text (read-only)

| Location | Round-71 filed text | Status |
|---|---|---|
| `corpus/lessons/round-71.md:36` | "Capoeira (no capture; flip: Flamenco)" | **ground falsified** (135 captures exist under the canonical slug) |
| `.ufo/waves/round-71/w1/ScoutOpenSourcesC.md:40` | "no Wayback capture under that URL; CDX wildcard only surfaces `capoeira-` stub captures and the 2017 Basel Carnival page (element id collision 01262 ≠ capoeira). Unverifiable; flip: Flamenco" | **ground falsified**; the wildcard *does* contain `capoeira-circle-00892` captures — truncated-read artifact. The 01262-is-Basel-Carnival observation is correct but not load-bearing. |
| `.ufo/waves/round-71/w1/ExecSOURCESRowTemplate.md:11` | row template cites `https://ich.unesco.org/en/RL/capoeira-00892` as the URL | non-canonical slug (the live page's own `rel=canonical` is `capoeira-circle-00892`) |
| `corpus/lessons/round-71-verifier-spotcheck.md:108` | verifier already recorded the disagreement: "live returns HTTP 200 with the full narrative … and no challenge wall. CDX lists 200 captures under the canonical slug (20170513162348, 20171120140510, 20171208155324), and `web/20171208155324/…` serves the page." | **independently corroborated by this re-open** — every timestamp and the live 200 match exactly |
| `reports/round-72/claims.json` (claim Ca, leg CAPOEIRA) | expects the correction citing "live 200 + CDX captures under capoeira-circle-00892" | **evidence now supplied** |

---

## 5. Findings summary (observed vs inference)

**Observed facts**
- F1. `https://ich.unesco.org/en/RL/capoeira-00892` → HTTP 200, 154 205 B, no redirect, full narrative, `rel=canonical` = `…/capoeira-circle-00892`.
- F2. `https://ich.unesco.org/en/RL/capoeira-circle-00892` → HTTP 200, 154 208 B, full narrative, same canonical.
- F3. The narrative sentence is "Capoeira is an Afro-Brazilian cultural practice – simultaneously a fight and a dance – that can be interpreted as a tradition, a sport and even an art form." (3 occurrences live: paragraph + `<META DESCRIPTION>` + `og:description`).
- F4. Challenge wall is **UA-gated**: browser UA ⇒ no wall (5/5); default curl UA ⇒ F5 TSPD "testing whether you are a human visitor" frame (5/5); empty UA header ⇒ full page.
- F5. CDX, `url=ich.unesco.org/en/RL/capoeira-circle-00892&filter=statuscode:200` → **135 rows**; earliest three `20170513162348`, `20171120140510`, `20171208155324`; latest three `20260602141520`, `20260710075531`, `20260907015854`.
- F6. CDX, `url=ich.unesco.org/en/RL/capoeira-00892` → **0 rows** (no status filter, and 0 rows under `matchType=prefix`).
- F7. `web/20171208155324/https://ich.unesco.org/en/RL/capoeira-circle-00892` → HTTP 200, 131 006 B, narrative present, title "Capoeira circle - intangible heritage - Culture Sector - UNESCO".
- F8. `capoeira-01262` is "Basel Carnival" — the id collision the round-71 seat flagged is real.

**Inference (reasoned, labelled)**
- I1. The round-71 reject was caused by probing the **non-canonical** slug and by reading only the head of a truncated wildcard CDX listing, not by any property of the element. → matches the K71-8 general failure class (probe the canonical/redirect slug in CDX before ruling "no capture").
- I2. The 2023–2025 `capoeira-`/`capoeira-circle-` stub rows in CDX are truncated-URL redirect artefacts produced by the 2023 ich.unesco.org URL-structure change (partial-URL captures resolving to 301/302), which is why a wildcard read surfaced them first and masked the 2017 canonical captures.
- I3. The challenge wall's UA-gating means the round-71 blanket premise "ich.unesco.org live pages return the CAPTCHA frame (curl with browser UA and read both confirmed)" is likely **mis-transcribed or mis-attributed** in the round-71 evidence — a browser UA demonstrably gets the real page today (5/5). `[INFERENCE]` on the historical round-71 run; the current behaviour is directly observed.

**Remaining unknowns / gaps**
- U1. Whether the *original* round-71 seat's browser UA (unknown string) hit the wall at that time — cannot be reconstructed; the round-71 seat file records no UA, and the wall's behaviour is server-side and time-dependent.
- U2. The full 135-row CDX listing was captured to `/tmp/scoutcapoeira/cdx-circle-all.txt`; per-row content was not fetched (only the 2017 one), so "every capture serves the narrative" is **not** claimed here. (Round-71 evidence elsewhere notes some 2026 captures of *other* elements archived the CAPTCHA frame — for this element, the three 2026 rows were not fetched.)
- U3. Whether the flip to Flamenco should be reversed is an editorial decision outside this scout's remit; the round-72 dispatch itself already states "correction, the flip to Flamenco stands".

## 6. Evidence for claim Ca leg CAPOEIRA (paste-ready)

```
Live: https://ich.unesco.org/en/RL/capoeira-00892 → 200 (154205 B)
Live: https://ich.unesco.org/en/RL/capoeira-circle-00892 → 200 (154208 B)
Quote: "Capoeira is an Afro-Brazilian cultural practice – simultaneously a fight and a dance – that can be
interpreted as a tradition, a sport and even an art form."
CDX (canonical slug, status 200): 135 captures;
  earliest 20170513162348, 20171120140510, 20171208155324
  latest  20260602141520, 20260710075531, 20260907015854
Capture: web/20171208155324/https://ich.unesco.org/en/RL/capoeira-circle-00892 → 200, narrative serves
CDX (probed slug capoeira-00892): 0 captures — the false reject's root cause
```
Access date: **2026-10-25**. Re-open evidence supports claim Ca leg **CAPOEIRA** and the K71-8 routing.

## 7. Tooling

No tools installed or upgraded by this seat (no `pacman`, no `uv tool install`, no `cargo`/`npm -g`).
Only stock `curl`, `python3` (stdlib), `grep`, `diff`, `sort` were used. All artifacts under `/tmp/scoutcapoeira/`:
`body-capoeira-00892.html`, `body-capoeira-circle-00892.html`, `body-defaultua.html`, `body-nouser.html`,
`b1..b5.html`, `d1..d5.html`, `hdr-capoeira-00892.txt`, `hdr-capoeira-circle-00892.txt`,
`cdx-circle-all.txt` (135 rows), `cdx-circle-limit6.txt`, `cdx-plain-all.txt` (0 rows),
`wb-20171208155324.html`.
