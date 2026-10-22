# ReviewS309Access — routed defect 5 (S309 access path recheck)

Seat: KotodamaR56.ReviewS309Access. Scope: re-open the S309 book page and PDF by ordinary means, read the S309 SOURCES row, draft the old->new access-path note, confirm the Gate quote verbatim. Access date for everything below: 2026-10-22.

## Row under review

`corpus/SOURCES.md:338` — S309, Wengrow 2014, *The Origins of Monsters* (Princeton UP). Its access note currently reads: "(direct, HTTP 200 for both the book page and the 265 KB PDF, read 2026-10-22. ...)". Gate line: `corpus/lessons/round-55.md:93`.

## Re-open results

### 1. Book page — https://press.princeton.edu/books/hardcover/9780691159041/the-origins-of-monsters

- **Plain curl (default `curl` user-agent): HTTP 200** — `text/html; charset=UTF-8`, 151,766 bytes, `server: cloudflare`, `cf-cache-status: HIT`, `x-drupal-cache: MISS`. The served page is the real book page: `<title>The Origins of Monsters | Princeton University Press</title>`, and its "Download PDF" button still links the recorded URL `https://pup-assets.s3.amazonaws.com/public/onix/images/9780691159041/9780691202396.pdf` (`<a ... href="...9780691202396.pdf"><svg.../><span>Download PDF</span>`). Reproduced on a second request ~1 minute later, identical status and byte count.
- **Curl with a browser user-agent: HTTP 403, Cloudflare challenge** — `cf-mitigated: challenge`, `server: cloudflare`, `content-type: text/html; charset=UTF-8`, 5,792–5,899 bytes, `content-security-policy` pinning `challenges.cloudflare.com`, `__cf_bm` cookie, body titled "Just a moment...". Reproduced three times across two browser UAs (Firefox 131 Linux; Chrome 130 Windows). **Challenge met, not passed.**
- **Reading against the defect text:** the lesson's §5 item 5 says "plain curl" got 403, but its own §2 states sources were re-opened with "curl (browser UA)". The 403 is user-agent-dependent: default curl passes (200, cache HIT), browser UAs are challenged (403). The row's "direct, HTTP 200 for both" is therefore still literally true for a plain non-browser request, but it omits the UA sensitivity that the closure observed.
- **Wayback (ordinary copy, verified):** CDX lists 200-status captures including latest `20260501170301`. `https://web.archive.org/web/20260501170301/https://press.princeton.edu/books/hardcover/9780691159041/the-origins-of-monsters` answered **HTTP 200** (`text/html; charset=UTF-8`, 216,123 bytes served; `x-archive-orig-content-length: 36393`, `x-archive-orig-server: nginx`, Drupal 10). It is the real book page (no "Just a moment"), and its copy links the same PDF on the `pup-assets.imgix.net` host variant. Note: `archive.org/wayback/available` returned HTTP 429 twice to me; CDX worked.

### 2. Publisher PDF — https://pup-assets.s3.amazonaws.com/public/onix/images/9780691159041/9780691202396.pdf

- **HTTP 200**, `application/pdf`, `Content-Length: 265276` (the row's "265 KB" is correct), `Server: AmazonS3`, `Last-Modified: 2021-03-15`, `ETag: "ad19bfe0346c3abeb4252ea05b6dd91d"`. No challenge, no login, default UA. 10 PDF pages: front matter, complete Introduction (printed pp. 1-7) and Index — matching the row's description.

### 3. Gate quote verbatim check

Gate line 93 quotes Introduction p. 1: "The first age of mechanical reproduction belongs to Mesopotamia" (9 words). **Verbatim**: these are the opening words of the Introduction. Caveat for future automated matching: the 'T' is typeset as a drop cap, so `pdftotext` emits it alone on its own line followed by "he first age of mechanical reproduction belongs to Mesopotamia," — the quote is exact in print but string-matchers see a split.

All four anchor quotes in the SOURCES row re-verified verbatim in the PDF text:
- p. 1 (PDF p. 2): "The first age of mechanical reproduction belongs to Mesopotamia" — drop-cap T, as above.
- p. 1 (PDF p. 2): "a term that I will shortly do away with and replace with “composites,” which more accurately describes what I am interested in" (21 words).
- p. 1 (PDF p. 2): "isolating the limbs or other features of diverse species and recombining them to form images of beings that have no counterparts in the visible world" (24 words; `pdftotext` wraps the lines but the sequence is contiguous).
- p. 5 (PDF p. 6): "An ancient Egyptian would have reckoned with the possibility of really encountering a griffin" (14 words).

## Drafted repair for the SOURCES note (L1 to apply)

The row's access note is accurate only for a plain non-browser curl; the honest record needs both outcomes, matching the S308/S317 style.

**Old** (verbatim substring of the cell):

> (direct, HTTP 200 for both the book page and the 265 KB PDF, read 2026-10-22. The PDF carries the contents page, the complete Introduction (pp. 1-7) and the Index; the chapter bodies are not in it.)

**New:**

> (read 2026-10-22. The book page answered HTTP 200 (151,766 bytes, `server: cloudflare`, `cf-cache-status: HIT`) to a plain default-UA curl, but HTTP 403 (`cf-mitigated: challenge`, Cloudflare "Just a moment..." interstitial) to a browser user-agent — challenge met, not passed under that UA; latest Wayback capture `20260501170301` is a readable HTTP 200 copy. The PDF answered HTTP 200 direct, `application/pdf`, 265,276 bytes; all quotes come from that PDF. The PDF carries the contents page, the complete Introduction (pp. 1-7) and the Index; the chapter bodies are not in it.)

Optional extra clause, if the L1 wants the link-target drift on record: "(the `20260501170301` capture's copy links the same PDF on `pup-assets.imgix.net`; the live page still links the recorded S3 URL)".

## Gate row 93 (corpus/lessons/round-55.md)

No change strictly required: its "accessed 2026-10-22" remains true via plain curl, and its quote is verbatim in the PDF it names. If the L1 prefers full disclosure, append before the Grounds: "(book page 403s to browser user-agents; quote from the linked PDF)". Note the line's `&quot;` entities are the html-entity item already routed to claim O — do not hand-decode.

## Result

- Defect 5 partially superseded: the book page is still directly reachable by plain curl (HTTP 200 twice), so "challenge met, not passed" applies only to browser-UA requests; the drafted note records both paths plus the verified Wayback copy.
- Gate quote: verbatim confirmed.
- PDF: HTTP 200 direct, 265,276 bytes, unchanged.

## Unrun checks / residual risk

- Did not probe whether the 200-vs-403 split is UA-only or also cache-state-dependent (two `cf-cache-status: HIT` hits observed on default-UA requests; no MISS-vs-challenge correlation tested).
- `archive.org/wayback/available` 429'd; CDX `statuscode:200` listing used instead — a newer capture than `20260501170301` could exist if CDX ordering was truncated (I requested `limit=-8` and saw the newest eight).
- The imgix PDF variant URL seen in the Wayback capture was not re-opened; the recorded S3 URL is live, so nothing depends on it.
- No installs performed or needed.
