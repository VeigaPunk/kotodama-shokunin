# ScoutReopenS880 — wave 2 FALSIFY, row S880 (round 73, lands 0316b8883b4f8d44b8efd720140e7f52f734a102)

## Verdict: ADMIT-STANDS

No field of the S880 row, its evidence capture or its Gate row failed. Every re-open check passed against the fresh bytes. Five MINOR findings are listed below; none changes a claim leg or an admitted statement.

All fetches were made on 2026-10-25 with plain `curl -L`. Downloads are in /tmp/ScoutReopenS880/. Nothing was written to the lane or the fleet.

## Re-open (UA recorded per request)

| request | UA | status | bytes | sha256 |
|---|---|---|---|---|
| GET https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | 200, application/pdf, no redirect | 193610 | 26dbcf2c0fab6d75214df6285e5c7dab92544f598d81a063df91fb4995a0d535 |
| same URL | `curl/8.7.1` | 200 | 193610 | 26dbcf2c0fab6d75214df6285e5c7dab92544f598d81a063df91fb4995a0d535 |
| GET https://web.archive.org/web/20240801224643id_/http://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf | browser UA | 200 | 193610 | 26dbcf2c…a0d535 |
| same capture URL | `curl/8.7.1` | 200 | 193610 | 26dbcf2c…a0d535 |

- The evidence file's sha256 line is `26dbcf2c0fab6d75214df6285e5c7dab92544f598d81a063df91fb4995a0d535`, equal to all four fetches, so there is no drift.
- Evidence bytes are 193610 (equal), http-status 200 (equal), and `pdfinfo` reports 9 pages (equal to the "9-page PDF" in the brief).
- The live PDF and the Wayback capture are `cmp`-identical.
- The live page is not UA-gated in either direction.
- `curl -I http://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` returns `301` with `Location: https://…` (the http→https upgrade).

## Quote

Quote: "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level."

- `echo -n "$Q" | wc -w` prints 25. The cap is ≤25, so it passes at the limit.
- In the fresh body (`pdftotext -enc UTF-8`, whitespace-collapsed), `grep -c -F` prints 1 for both the live PDF and the capture, with exactly one occurrence.
- Per-page extraction hits only page 5 (p1–p4 and p6–p9 print 0).
- In `pdftotext -layout`, the quote starts on page-5 line 15 ("typology. One innovation of this work…") and ends on line 16 ("part of a course even at the introductory level.").
- The section heading is "3. These papers" (body line 137). The row's locator "§3 These papers, p. 5" is correct.
- `grep -ci semester` on both the live body and the capture body prints 0, so "semester-long" is absent.
- The row's own "semester-long" mention is the negative statement in the scope cell ("it does not carry the token semester-long").

## Row parse

- Row 835 of corpus/SOURCES.md at 0316b88: `awk -F'|' '{print NF}'` prints 13, so there are 11 cells.
- Cells are id, source, kind=paper, tier=B, scope, anchor, teaches, status=mined, opened=2026-10-25, recheck=180d, used-by.
- Anchor cell contains the evidence quote: Python `Q in cell` is True. It also begins with `§3 These papers, p. 5:`, which matches the evidence locator.
- Source-cell URLs: exactly two (`https://sanders…pdf` and the `…20240801224643id_/http://sanders…pdf` capture), and both resolve with 200 (table above).
- Quote found in the capture body: yes, grep count 1.
- Used-by: `corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` is correct. S880 appears 10 times there and 0 times in `conlang-scholarship.md`.
- Recheck 180d matches S876–S879, which are also 180d.
- Gate row (corpus/lessons/round-73.md line 22): URL, date 2026-10-25, quote, locator, evidence path, HTTP 200, 193610 B and sha prefix `26dbcf2c0fab6d75…` all match what I measured.

## Capture 20240801224643 and QUALITY 18

- Wayback CDX for `url=http://…`, `url=https://…` and `url=sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` lists two captures, 20240620030845 and 20240801224643.
- Both have original `http://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf`, statuscode 200 and the same digest `N4WBAMHBQV42CBUVDHDCKFRZRQTBRDOV`. There is no https-original capture.
- Normalization:
  - The counter's `accept-c.py` `norm_url()` returns `(netloc.lower(), path)` and ignores scheme. The http origin and the https live URL normalize equal (Python prints True).
  - Same page: the `id_` replay is byte-identical to the live body, and http 301s to the https URL.
  - `tools/check-row-fragments.py` `norm_url()` keeps scheme (`return f"{scheme}://{host}{path}"`). Run on this pair it prints `https://… http://… False`, so that tool would flag `capture-url-mismatch`.
- QUALITY 18 says only "must normalize (query-aware) to the live URL" and does not mention scheme. The row passes under the counter's definition and fails under the stricter tool's, so the two identities disagree.
- Ruling: ADMIT-STANDS, because the capture is provably the same page.

## Findings (all MINOR)

1. **Scheme identity is inconsistent across the lane's two normalizers** (see QUALITY 18 above). If the criterion ever means scheme-sensitive, S880 fails on the capture leg. Fix: pin the definition in criterion 18, or add a note on the row.
2. **The Wayback leg is not in the committed evidence.** `reports/round-73/evidence/S880.txt` and the Gate row record only the live fetch. `git grep 20240801224643` over reports/round-73 and corpus/lessons/round-73.md returns nothing. The anchor cell's claim "capture 20240801224643 (same bytes), both carrying the span" therefore has no committed capture record (status, bytes, sha, quote hit). I confirmed it is true now (table above), but the claim leg cites it unevidenced. The `accept-c.py` EVIDENCE leg's quote check is self-referential: it tests the quote against the context window the same seat wrote. Only a fresh re-open, like this one, tests it against the PDF body.
3. **Two descriptors in the source cell are not in the cited bytes.**
   - "Canadian Journal of Linguistics" and "opening article of the special issue" are not in the PDF text. `grep -i 'canadian journal\|CJL\|cnj'` on the body finds only the other journal ("Canadian Journal for the Scholarship of Teaching and Learning", body lines 310 and 387). They are supported by the host index page `https://sanders.phonologist.org/`: "Canadian Journal of Linguistics 69(3): 276–284. DOI: 10.1017/cnj.2024.20". That page is not named in the row.
   - "PDF hosted by the Phonology Lab" has no support: `grep -ci 'phonology lab'` prints 0 on both `https://sanders.phonologist.org/` and `/Papers/`, and the index page's `<title>` is "Nathan Sanders". "Phonology Lab" appears only in the staging seat's prose (ScoutS901.md).
4. **The scope cell upgrades a modal.**
   - The PDF says the work "suggests that a multi-part, creative project *can be* part of a course even at the introductory level". The scope cell says the course had "a multi-part creative project placed even at the introductory level".
   - The PDF does not say the Sowers-Wills course itself was introductory.
   - `conlang-scholarship.amend-2026-10-23.md` line 80 ("at introductory level and inside a project-based course") inherits this. That file is outside my brief, so I did not attack it further.
5. **The 25-word cap holds only under whitespace tokenization.** With `re.findall(r"\w+")`, "multi-part" splits and the quote is 26 words; whitespace split and the hyphen-preserving regex give 25. QUALITY.md has no "25" cap text, so the cap definition lives only in the round brief and in `accept-c.py` (`len(q.split()) > 25`). It is consistent with `wc -w`, but zero margin.

## Not checked

- I did not run `scripts/sources-census.sh validate`. In my throwaway clone the counter reported 10 of 11 legs PASS and CENSUS FAIL ("census script not found"). That is because I did not pass `--fleet-root`; it is not a finding.
- I did not independently open the Sowers-Wills article. The row itself says it was not opened.
- Cambridge and DOI pages were not fetched.
- The 25-word cap's source text was not located. I found no definition in QUALITY.md.
- I did not review the amend-entry prose beyond S880 quote presence and the lines noted above.

## Tooling

Nothing installed. `curl`, `pdftotext`, `pdfinfo` and python3 were already present. The throwaway clone was /tmp/tmp.IJwMd1zmlU, detached at 0316b88, used only to run `accept-c.py` offline.
