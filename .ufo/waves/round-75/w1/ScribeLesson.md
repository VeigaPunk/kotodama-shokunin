# ScribeLesson — round 75 wave 1 (kotodama, hyaku run 10)

Seat: scribe. Assignment: draft `corpus/lessons/round-75.md` at `.ufo/waves/round-75/drafts/lesson.md` with
header, `## Gate` (one row per candidate S885–S893, ≥1 admit and ≥1 reject with reason+flip), `## Mistakes`
(seeded with R75-M1/R75-M2), `## Quarantine` (standing register verdicts re-derived) and `## Corrections`
(L75-05/06 reclassification + routed-on items). Leaf seat: no delegation, no background jobs, no mutation of the
lane's git state, no edits to claims.json/ledger.json.

## Behavior

1. Read the DRAFT claims and ledger (`reports/round-75/claims.json`, `reports/round-75/ledger.json`), the round-74
   lesson (Gate, Mistakes R74-M1–M10, Routed to round 75), the round-71 quarantine verdicts, and the wave-1
   roster (`w1/spec.json`, 42 seats).
2. Fetched all nine candidate documents by ordinary means (one plain `curl -L` per URL, browser UA, no automation,
   no challenge passing), extracted text (stdlib HTML text extraction; `pdftotext -enc UTF-8`), and located one
   quote per row after NFKC + whitespace folding. Quote lengths measured: 38/48/72/21/64/77/68/51/39 characters;
   6/9/11/1/9/12/9/10/1 whitespace tokens.
3. Tested whether the persee page-level transcription is open (it is: three page URLs, HTTP 200, article text, no
   login) — which retires the staged entry's "JavaScript viewer" caveat.
4. Probed the two refusal classes on candidates S891 (live anti-bot shell) and S892 (live HTTP 403 Cloudflare),
   and re-opened both through same-page Wayback captures.
5. Re-tested staged S870's register span on its own page (absent, 0 hits on four probes) and located a fresh quote
   for the same document (lane id S893).
6. Re-derived the L75-05/L75-06 re-derivation commands at base (`git grep -c` → 1 and 1) and the quarantine tally
   (10/7/4 = 21 rows).
7. Measured the 40 staged files against the lane tree: 2 adopted / 6 path-present-differing / 32 refused, with
   sha256 pairs, and re-derived the L75-02/L75-03/L75-04 defects (README:344 "30" vs 32; README:407 "36" vs 40;
   `sweep.py:108` reads the first footer, total 243, while the last footer, total 249, is correct).

## Fetch records (QUALITY 22 — each User-Agent bound to the response that request got)

UA for every request below: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0
Safari/537.36`. `automation: none` (plain `curl`, no browser automation, no solved captcha, no bypassed block).
All requests 2026-10-27, local time (UTC−3); one request per URL.

| row | URL | HTTP | bytes | sha256 | local | note |
|---|---|---|---|---|---|---|
| S885 | https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 | 200 | 111487 | `9be2c68d1b969364f581d6bed2648dc1289b6ad42cc05b8a25f455605a780f26` | 13:56:19 | notice page body carries the opening paragraph |
| S886 | https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 | 200 | 111234 | `70e5327944e34654e1f73b09f9237e61c9bf7fe5e134ed604c6c4f6bd6a127ac` | 13:56:22 | notice page body |
| S887 | https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 | 200 | 116879 | `71ab57f04ba1ed8af3bd81abcccc0b83685968a0185f3e100cac1ae3c2f44a8b` | 13:56:25 | notice page body |
| S888 | https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf | 200 | 225123 | `62a13e92e23d764c88d1e58f64cde00eb90a6aee900d52fa431bde9ca89334d1` | 13:56:30 | PDF, 5 pages; quote on p. 3 |
| S889 | https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf | 200 | 1085244 | `fdf60d276b3f31cded2a40b8a12085f4b88e7f645062e3e2c9d9f8c647072b58` | 13:56:44 | PDF, 18 pages; quote p. 1 |
| S890 | https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf | 200 | 697092 | `1dccf9d1427defb0e07e99461301cfd0ef5b5734716783a8ba0bb782de422272` | 13:56:53 | PDF, 6 pages; quote p. 1 |
| S891 live | https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html | 200 | 46013 | `c08372f1b186bb4e7e5b981076d01a9714cca74762ea065b0e700fe713dab96f` | 13:56:55 | **anti-bot challenge shell** (`bobcmn` script, "is your a human visitor" code prompt) — met, not passed, nothing attempted |
| S891 capture | https://web.archive.org/web/20041220223357/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html | 200 | 5693 | `be01bc0e40a00f8bc9168abf54fdd409e6631e87b869cb0a7a9174599b56d9e4` | 13:58:17 | archived fiche body; five-codes paragraph located |
| S892 live | https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf | 403 | 5867 | `92a72928ed748f265a87170be519d05954616de1bac0040d14ea7a27703f7a81` | 13:56:57 | Cloudflare interstitial (`<title>Just a moment...</title>`) — met, not passed |
| S892 capture | https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf | 200 | 763802 | `8c0303670ff5db8625d034be958ad5729a2c79fa77f3642efc5f6341fb25a19a` | 13:58:19 | PDF, 25 pages; quote on p. 7 |
| S893 | https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | 200 | 45238 | `51251e22c617617af797d164684e8927dc792a06140ff35fbaebc158515415f0` | 13:56:57 | 世界观 section located; register span absent (0 hits) |
| persee p.11 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0011_0000 | 200 | 4061 | `9cbf7c9485a6683c709a6f94d72d0251f5c746028f5a233b72cadd1ecd885143` | 13:59:03 | plain HTML text, no login; noyaux/catalyses paragraph |
| persee p.139 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1120/comm_0588-8018_1966_num_8_1_T1_0139_0000 | 200 | 3939 | `16992c94b5e8b314afc2fb8c4ccc297cdc3199855d6fff68f518006b4e17d724` | 13:59:03 | temporal-deformation paragraph |
| persee p.30 | https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1114/comm_0588-8018_1966_num_8_1_T1_0030_0000 | 200 | 3737 | `2502768202dbd0e0b17f6310ad4b0c6cfe7e3d1edbd490efab5f7c4f71fe082f` | 13:59:04 | Greimas sequence/isotopy paragraph |

No install or upgrade was made this round (no tool needed: `curl`, `pdftotext`, stdlib Python).

## Gates drafted

`## Gate` carries nine candidate rows S885–S893, all **admitted**, each with URL, access date 2026-10-27, a located
quote ≤25 tokens and ≤80 characters, locator, capture pointer and the seat fetch's byte count + sha256. Three
**reject** rows carry reason + re-test output + flip:

1. staged S870 (as staged): register span absent from the served 45238 B body — `grep -c '作品中的人物名字和地名'` → 0
   and three shorter fragments → 0, against 1 hit for the page's own 世界观 section. Flip: document re-opened as
   S893 with a fresh located quote (done).
2. S891's live URL: anti-bot challenge shell — refused as a live-only anchor; flip = the 2004 Wayback capture.
3. S892's live URL: HTTP 403 Cloudflare — refused as a live-only anchor; flip = the 2025 Wayback capture.

Capture pointers name `reports/round-75/evidence/<id>.txt`, to be written by `ExecEvidence` from its own fetch. The
seat fetches above are the independent observation, not the committed capture: **the draft does not claim any
committed evidence window exists yet.**

## Findings

- **F1 (pre-freeze, claim C):** `reports/round-75/claims.json` row_set is S885–S892 (8 ids) while the seat scope,
  `ScoutChinawriter2023` and this Gate name S893. If the freeze keeps 8 rows, the ROWS leg ("adds exactly the frozen
  row_set") cannot admit S893 and the entries cannot cite it. Fix: freeze adds S893 and the map entry
  `staged S870 → S893` joined by document. Messaged to Main; R75-M4 in the draft.
- **F2 (claim C kill rule / entry scope):** the persee page-level transcription service answers a plain
  browser-UA request with HTTP 200 and article text (p. 11 / p. 139 / p. 30: 4061 / 3939 / 3737 B, no login,
  paywall or challenge), so (a) the claim's kill-rule clause about "access control" is not triggered by citing
  page-level locators, and (b) the staged entry's caveat that the French text is "served through a JavaScript
  viewer" and that Western claims rest "on the notice and the opening paragraph only" is false (R75-M5). The
  entries can cite the deeper locators with their own captures.
- **F3 (Mistakes seed):** R75-M1 is grounded in a live instance, not only in the round-74 class: `round-72.md:31`
  names "register S787" for an observation made on the china writer page, while lane S787 at base is the Koiso
  fragrance paper (`corpus/SOURCES.md:741`) and register S787 in the quarantine table is the China Writers page.
- **F4:** R75-M2 grounded in code: `reports/round-28/readme/sweep.py:108` (`FOOTER_RE.search`) reads the first
  footer (`README.md:751-753`, total 243, dirs 30/29/36/29/24/95) and not the last (`:815`, total 249,
  32/29/40/29/24/95); `README.md:344` says 30 against 32 linguistics files, `:407` says 36 against 40
  culture-material files.
- **F5:** round 74's triage said "2 adopted / 4 path-present / 34 refused"; at round-75 base **6** staged files are
  path-present with differing bytes (the two worldbuilding files round 74 adopted also differ). Counts: 2 adopted /
  6 path-present-differing / 32 refused = 40.
- **F6:** staged recheck cells are still unverifiable in the same way round 74 documented:
  `narrative-structure-frameworks.md:34` records `S870 → 1` for a span whose fetch count is 0 (R75-M3).

## Touched surfaces

- Wrote `.ufo/waves/round-75/drafts/lesson.md` (draft lesson; 154 lines).
- Wrote this report, `.ufo/waves/round-75/w1/ScribeLesson.md`.
- Nothing else: no repo code, no claims/ledger, no registry, no README index, no QUALITY/SKILL/LOG/SCORECARD, no
  git index or jj state, no fleet-root file, no shokuknow write.
- Scratch `/fast/scratch/hyaku/kotodama-r75/ScribeLesson/` holds the fetched bodies and extracted texts; it is
  deleted before yielding, so its paths are not citable and are not cited as evidence in the draft.

## Out of scope / limits

- The draft is pre-freeze and pre-data: quotes are seat observations, the committed evidence windows do not exist
  yet, and the freeze revision is not known to this seat.
- The counters (`accept-c.py`, `accept-ca.py`), the row map, and the evidence tool belong to other seats; nothing
  here was run against them.
- Entry text (base/amend), README index rows, QUALITY 27 text and SCORECARD correction rows are other seats' work;
  this seat only names what they must satisfy.
- The two-way challenge record is a *fetch* record, not a row's `status` cell: the rows themselves are drafted by
  `ExecEvidence`/the row-map seats.
