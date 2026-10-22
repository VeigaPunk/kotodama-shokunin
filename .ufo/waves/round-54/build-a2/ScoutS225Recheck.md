# ScoutS225Recheck — S225 and S237 re-check (round-54 routed defect 3, spotcheck :112 and :177)

Access date 2026-10-22. Every status and quote below was produced in this session by a plain
HTTP request (`curl`, no browser, no challenge-solving). Lane read-only; no file outside this
report was written.

## What was run

| request | status | body | note |
|---|---|---|---|
| `curl https://benjamins.com/catalog/gest.20034.bro` (curl default User-Agent) | **HTTP 403** | 5,805 bytes, `text/html`; body text: "Sorry, you have been blocked / You are unable to access benjamins.com"; `server: cloudflare`, `cf-ray` present | Cloudflare managed block. Not a paywall: it is the security-service interstitial. |
| `GET https://web.archive.org/web/20260106191949/https://benjamins.com/catalog/gest.20034.bro` | **HTTP 200** | 411,949 bytes, `text/html`; `memento-datetime: Tue, 06 Jan 2026 19:19:49 GMT` | exact capture id matched, no redirect |
| `curl https://cornerstone.lib.mnsu.edu/cgi/viewcontent.cgi?article=1000&context=ctamj` | **HTTP 403** | 5,828 bytes, `text/html`; body text: "Just a moment... Enable JavaScript and cookies to continue" | Cloudflare JS challenge. **Challenge met, not passed** — no route was attempted against it. |
| `GET https://web.archive.org/web/20261014222628/https://cornerstone.lib.mnsu.edu/cgi/viewcontent.cgi?article=1000&context=ctamj` | **HTTP 200** | `application/pdf`, 232,283 bytes, 14 PDF pages; `memento-datetime: Wed, 14 Oct 2026 22:26:28 GMT`; `x-archive-orig-content-disposition: inline; filename="Communication is 93% Nonverbal: An Urban Legend Proliferates.pdf"` | the offprint itself, archived |
| `curl https://cornerstone.lib.mnsu.edu/ctamj/vol34/iss1/2/` (landing page) | **HTTP 200** | 36,978 bytes | bepress record; `bepress_citation_doi = 10.56816/2471-0032.1000`, volume 34, issue 1, date 2007, ISSN 2471-0032 |

Text extraction: `pdftotext` (poppler, already installed) on the archived offprint; page breaks
kept with `\f`, page 5 re-read with `-raw` to confirm there is no hyphenation join across the
quote.

## S225 — status answers the two asked questions

1. **Status of the live Benjamins page to a plain request: HTTP 403.** The body is the
   Cloudflare block page, so the round-53 access note ("the live catalogue page returned HTTP
   403 to a plain request") *reproduces*; it is not stale. Disclosure: a second request with a
   normal browser `User-Agent` string returned HTTP 200 and the same abstract
   (`citation_abstract` and `og:description` metas). That 200 is recorded for accuracy only and
   is **not** used as evidence: the block is a bot heuristic, so the live page must not be
   re-baselined as open, and the row's support continues to rest on the Wayback capture.
2. **Wayback 20260106191949 carries the asked quote: yes, exactly, in four places.**
   `grep` of the capture finds the literal string `We asked 14 Korean and 14 Catalan
   participants` four times: the `citation_abstract` meta, the `og:description` meta, the
   `description` meta, and the visible Abstract paragraph under the author block (University of
   Birmingham affiliation line). The live 200 body carries the identical abstract text.

Metadata the same page supplies (both live 200 body and capture): title "Gestures are modulated
by social context: A study of multimodal politeness across two cultures", journal *Gesture*,
`citation_volume` 21, `citation_issue` 2-3, pages 167–200, doi 10.1075/gest.20034.bro, authors
Brown, Lucien; Kim, Hyunji; Hübscher, Iris; Winter, Bodo. Visible text: "Article published In:
Gesture Vol. 21:2/3 (2022) ► pp. 167 – 200" and "Published online: 10 January 2023". The row's
year 2023 is therefore the online-publication year; the volume year on the page is 2022. Also
still visible: the download area's "authorization required" label, so the full text remains
gated exactly as the row's scope says.

Quotes (Wayback 20260106191949, Abstract paragraph, sentences 2 and 3):

- sentence 2: "We asked 14 Korean and 14 Catalan participants to retell a cartoon, once to an
  unknown superior and once to a close friend." (23 words)
- sentence 3: "Participants in both languages curtail gestures when interacting with a socially
  distant superior." (13 words)

The round-53 spotcheck quoted these two sentences joined with an ellipsis into one fragment
(spotcheck :112). They are separate sentences on the page and must be given as separate quotes
under the ≤25-word rule; the erratum line below keeps them apart.

## S237 — page and verbatim text of the Gate quote

The quoted sentence is on **printed page 11** (page header "CTAMJ Summer 2007    11"), which is
**PDF page 5 of 14** in the archived offprint; printed pagination runs 7–19, matching the row's
"34: 7–19". Verbatim, with the surrounding sentence so the truncation is visible:

> wrote, “Please remember that all my findings on inconsistent or redundant communications deal
> with communications of FEELINGS AND ATTITUDES.” So, it has never been Mehrabian’s

Full sentence as printed, 18 words:

"Please remember that all my findings on inconsistent or redundant communications deal with
communications of FEELINGS AND ATTITUDES."

Two facts the Gate line does not currently carry:

- The sentence is **Lapakko quoting Mehrabian**, not Lapakko's own finding: the immediately
  preceding words are "(A. Mehrabian, personal communication, September 21, 1995), he confirmed
  this goal when he wrote". So what the row supports is Mehrabian's own statement *as reported
  second hand by Lapakko*, not a Mehrabian publication.
- The round-53 excerpt "all my findings …" is an exact substring and is not a join of two
  fragments, but it starts mid-sentence; the whole sentence is 18 words and fits the cap, so
  there is no reason to truncate.

## Erratum lines, ready to paste

Replace the `anchor`-cell access note in the S225 row (`corpus/SOURCES.md:254`, the text from
"Abstract, catalogue page Access note (round 54, 2026-10-22):" onward):

```
Abstract, catalogue page Access note (round 54, 2026-10-22, re-checked 2026-10-22): the live catalogue page returned HTTP 403 to a plain request (Cloudflare "Sorry, you have been blocked", not a paywall), so the live page is not a plain-request source; Wayback capture 20260106191949 (HTTP 200) carries the abstract, "We asked 14 Korean and 14 Catalan participants to retell a cartoon, once to an unknown superior and once to a close friend." (Abstract, sentence 2) and "Participants in both languages curtail gestures when interacting with a socially distant superior." (Abstract, sentence 3). The page states Gesture Vol. 21:2/3 (2022), pp. 167-200, "Published online: 10 January 2023", doi 10.1075/gest.20034.bro; full text behind the "authorization required" label.
```

Replace the S237 Gate line in `corpus/lessons/round-53.md:182` (the URL was the landing page
while the quote is from the offprint):

```
- S237 — https://cornerstone.lib.mnsu.edu/cgi/viewcontent.cgi?article=1000&context=ctamj (offprint PDF; the plain request returned an HTTP 403 Cloudflare JS challenge, which was met and not passed; read from Wayback capture 20261014222628, HTTP 200, application/pdf, 14 pages, printed pp. 7-19; landing page https://cornerstone.lib.mnsu.edu/ctamj/vol34/iss1/2/ HTTP 200 supplied the abstract) — accessed 2026-10-22 — printed p. 11 (PDF page 5), Lapakko quoting Mehrabian's letter of 21 September 1995: "Please remember that all my findings on inconsistent or redundant communications deal with communications of FEELINGS AND ATTITUDES." Grounds: how the figure spread and what the author of the numbers said about it, as Lapakko reports it second hand. Seat: ScribeSec12Calibration.
```

## What this changes for the L1

- S225's live page is still a 403 to a plain request, so no row edit is needed for access; the
  existing note is confirmed, and the only corrections are the split quotes and the fact that
  the 403 is a Cloudflare block rather than an authorization wall.
- S237's quote location was already right (printed p. 11); the defect was the URL, fixed in the
  line above, plus the second-hand attribution, which the entry must not turn into "Mehrabian
  published this in 1967".
- Neither source has any bearing on the masks and masquerade entry (claim C); both are
  gesture/communication rows from round 53.

## unopened

- Benjamins full text: behind the "authorization required" download label; not attempted.
- The live `cornerstone.lib.mnsu.edu` offprint: HTTP 403 Cloudflare JS challenge, met and not
  passed; not retried through any browser or solver. The archived copy was used instead.
- Crossref record for doi 10.1075/gest.20034.bro: not fetched (the catalogue page carried the
  same metadata).

## Tools

No install or upgrade was made. `pdftotext` 26.08.0 (poppler, already installed) was used for
text extraction only; the requests were made with `curl` 8.23.0.
