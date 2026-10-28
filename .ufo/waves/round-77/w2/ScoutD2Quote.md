# ScoutD2Quote — independent reopen of D2 (S898) live + capture; quote/anchor/page verification

Seat: `ScoutD2Quote` (scout, leaf). Lane `kotodama-shokunin`, base
`211f9526800906e0c585d878d265c37e5e090c15`. Named W1 item attacked: the D2 claim
on CLAIMS-DRAFT line 15 (`staged S903 → lane S898`, Kałużyńska 2025, Onomastica
LXIX, DOI 10.17651/ONOMAST.69.7) — specifically its Gate quote mechanics, the
verbatim/folded status, PDF p.4 / journal p.114, quote-page/window-pages and
same-page capture, against W1 artifacts
`w1/ScoutDocS898.md` + `w1/stage/ScoutDocS898/evidence.txt` and
`w1/ExecAdaptCapture.md` + `w1/stage/ExecAdaptCapture/dryrun/S898-P4{,-5W}.txt`.

**Verdict: NOT FALSIFIED on the claim wording itself — every D2 mechanical
assertion in CLAIMS-DRAFT line 15 reproduces independently (new live fetch +
capture fetch 2026-10-27 local, own tool run, own measurement).** One stale
W1 artifact carries a false verbatim fact (below); the current draft already
records the corrected wording.

## Receipts (my own run, all numbers observed)

Fetch (plain `curl/8.23.0`, no `-A`; tool runs below use its browser UA):

```
$ curl -sS -L --compressed --connect-timeout 20 --max-time 90 -o d2-live.pdf -D live.headers \
    -w "live http=%{http_code} url=%{url_effective} bytes=%{size_download} wall=%{time_total}\n" \
    "https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/"
live http=200 url=https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/ bytes=417093 wall=2.826021
$ curl -sS -L --connect-timeout 20 --max-time 120 -o d2-wb.pdf -D wb.headers \
    -w "wayback http=%{http_code} url=%{url_effective} bytes=%{size_download} wall=%{time_total}\n" \
    "https://web.archive.org/web/20260901045105id_/https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/"
wayback http=200 url=https://web.archive.org/web/20260901045105id_/https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/ bytes=417093 wall=3.448868
$ sha256sum d2-live.pdf d2-wb.pdf && cmp -s d2-live.pdf d2-wb.pdf
5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc  d2-live.pdf
5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc  d2-wb.pdf
cmp: BYTE-IDENTICAL
```

`wb.headers`: `memento-datetime: Tue, 01 Sep 2026 04:51:05 GMT`,
`x-archive-orig-date: Tue, 01 Sep 2026 04:51:05 GMT`,
`content-disposition: attachment; filename="574-Article Text-3204-3-10-20260417.pdf"`.
`live.headers`: `content-type: application/pdf`, `content-length: 417093`,
same content-disposition filename. `pdfinfo`: Title `Onomastica 69_07`,
Author `Irena Kałużyńska`, Pages 13. `pdftotext -v`: 26.08.0.
Live sha256 matches W1's recorded digest exactly — same document re-served.

Same-page capture proven by the tool's own normalisation, not asserted:
`wayback-original == wayback-final-original ==
https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/`,
`wayback-same-page: yes`, `wayback-final-same-page: yes`,
`wayback-timestamp-matches: yes` (asked 20260901045105, served that second).

## Tool runs — staged capture-evidence.py, rehearsal claims (freeze not yet landed)

`reports/round-77/` holds only `telemetry/` → no `claims.json`; runs used
`--claims-file …/w1/stage/ExecAdaptCapture/capture-block-rehearsal.json`
(`sha256 3a313fb6…`), same as W1. Tool file
`w1/stage/ExecAdaptCapture/capture-evidence.py`,
`sha256 bab5ca44f78540059b07f22c1ee2254ae310075c865355841b24c0d49030f8b5`.

Run A — quote = the 5-word span, anchor = the 17-word sentence (claim's shape):

```
$ python3 -B <stage>/capture-evidence.py --claims-file <stage>/capture-block-rehearsal.json \
  --id D2Q-5W --url <live> --wayback-url <20260901045105id_ capture> \
  --quote "there were altogether 88 terms" \
  --anchor-quote "According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees" \
  --find "According to Kałużyńska (2008, pp. 223, 232)" \
  --locator "§3 ¶1 second sentence, journal p. 114 / PDF p. 4" \
  --out out/D2Q-5W.txt --work <scratch>
EVIDENCE D2Q-5W: quote-found=yes verbatim=yes anchor-in-window=yes window-source=live
  live-http=200 wayback-http=200 wayback-same-page=yes memento=Tue, 01 Sep 2026 04:51:05 GMT
  bytes=417093 sha256=5d1bfa5a5f01bee6 window-chars=4098 window-scope=excerpt
  window-sha256=fb65bae17dc50fe3 find-page=4  →  VERIFY OK  →  CAPTURE OK   exit=0
```

Evidence facts (out/D2Q-5W.txt): `quote-words: 5`, `quote-chars: 30`,
`quote-found-verbatim: yes`, `anchor-quote-words: 17`, `anchor-quote-chars: 111`,
`anchor-found: yes`, `anchor-in-window: yes`, `quote-in-anchor: yes`,
`quote-anchor-distance: 46`, `find-page: 4`, `find-hits: 1`, `page-count: 13`,
`window-pages: 3..5`, `quote-page: 4`, `anchor-page: 4`,
`window-sha256 fb65bae17dc50fe3c3b25b1ebe234e024fdb501819314a253a93ee18717e52a5`
(identical to W1's S898-P4-5W window sha256), `window-source: live`,
`wayback-quote-found: yes`, `wayback-quote-found-verbatim: yes`,
`access-date: 2026-10-27`, fetched `2026-10-28T02:13:19Z` UTC (local
`2026-10-27 23:13 -0300`).

Run B — quote = the 17-word sentence (verbatim probe; W1 S898-P4.txt shape):

```
EVIDENCE D2Q-17W: quote-found=yes verbatim=no … find-page=4 → VERIFY OK → CAPTURE OK
quote-words: 17  quote-chars: 111  quote-found-verbatim: no
window-pages: 3..5  quote-page: 4  anchor-page: 4
normalise: NFKC(per-character)+whitespace-fold; matched=folded
```

## Extractor measurement (tool's own `extract_text`/`locate`/`page_at`, my script)

`d2-verify.py` (`sha256 6c10d1fe…`, log `d2-verify-live.log`) imported the staged
tool and measured the fresh fetch:

```
pdf: d2-live.pdf bytes=417093
pdf sha256: 5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc
extract: pdftotext -enc UTF-8 BODY - …; 33690 chars, 13 page(s)
page 4 head: '114 Irena Kałużyńska Liu (1996, p. 46) stated: …'
page 5 head: 'FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA \x08 115 data: …'
Q5   'there were altogether 88 terms' :
     found=True verbatim=True tier=verbatim start=10479 raw-pages=[4] folded-page=4
Q17  'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees' :
     found=True verbatim=False tier=folded start=10433 raw-pages=[] folded-page=4
LOCATOR 'According to Kałużyńska (2008, pp. 223, 232)' :
     found=True verbatim=True tier=verbatim start=10433 raw-pages=[4]
raw around locator:
  '…in China.\nAccording to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms\n
   denoting plants, flowers and trees (general terms, …'
q5 raw offset=10479 page=4 (locator offset=10433, distance=46)
pdftotext -layout p4:   Q5 occurrences=1  Q17 occurrences=0
pdftotext -layout all:  Q5=1  Q17=0  LOCATOR=1
pdftotext nolayout all: Q5=1  Q17=0  LOCATOR=1  total-chars=33690
```

The wrap is exact: the PDF breaks after `88 terms` — `\n` between `terms` and
`denoting`. So the 17-word sentence never occurs verbatim in any extraction mode
(raw non-layout, raw layout); it exists only folded. The 5-word span ends before
the break → verbatim, unique (exactly 1 hit in whole document), on PDF p. 4.

Journal-page check: PDF p. 4 header text is `114 Irena Kałużyńska` and PDF p. 5
header is `… 115`, so PDF p. 4 = journal p. 114 ✓ (and the quote is on p. 4,
i.e. quote-page 4 ⊂ window-pages 3..5 — the routed p5/p115 defect is fixed and
re-checkable from the file).

Locator wording check: `d2-live.txt` grep — line 148 `3. THE MOST COMMON LEXEMES
DENOTING PLANTS, FLOWERS, AND TREES OCCURRING IN FEMALE NAMES`, line 150 ¶1 S1
`There are many terms denoting various species of plants and trees in China.`,
line 151 S2 = the anchor sentence → "§3 first paragraph, second sentence" ✓.

## Per-claim verdict table

| CLAIMS-DRAFT line-15 statement | observed | verdict |
|---|---|---|
| live URL returns the D2 PDF | HTTP 200, 417093 B, application/pdf | holds |
| same-page capture 20260901045105id_ byte-identical to live | same sha256, `cmp` identical, memento 2026-09-01T04:51:05Z | holds |
| Gate quote verbatim, 5 words | `quote-words 5`, `verbatim=yes`, `tier=verbatim`, unique hit, raw-pages=[4] | holds |
| anchor = the 17-word sentence, folded, NOT verbatim | `anchor-quote-words 17`, `verbatim=False`, `tier=folded` in both modes | holds — any verbatim claim for it is false |
| locator §3 ¶1 S2, journal 114 / PDF 4 | §3 heading → S1 → S2 at char 10433; p4 head `114` | holds |
| quote-page / window-pages | `quote-page: 4`, `anchor-page: 4`, `find-page: 4`, `window-pages: 3..5` (4 ∈ 3..5) | holds |
| count reported from the 2008 work, not re-counted | attribution inside the quoted sentence itself (`According to Kałużyńska (2008, pp. 223, 232),`) | consistent |

## Stale W1 artifact (a real defect, already corrected in the draft)

`w1/stage/ScoutDocS898/evidence.txt` — which used `pdftotext -layout` and a
hand-rolled window — asserts for the 17-word span `quote-found-verbatim: yes`,
`normalise: … matched=verbatim`, and inconsistent counts `quote-words: 10` /
`quote-chars: 65` (the span is 17 words / 111 chars; its own stored window line
is whitespace-folded). Under BOTH extraction modes the 17-word form has **zero**
verbatim occurrences. If that file were installed as the round-77 receipt it
would either fail verification (`verify_file` recomputes) or encode a false
verbatim claim — matching ExecAdaptCapture's §5b warning. The draft's chosen
shape (5-word verbatim quote + 17-word folded anchor, `S898-P4-5W` shape)
reproduces cleanly: `out/D2Q-5W.txt` sha256
`39542d7cc34bcb81e79c0179a856564619fc794a9cc8c3ae5f45b553f09f9390` vs
17-word probe `00e7b96bd9a08b06386dbd458c66d852d555f976ae88f7519753822b37459587`.

No attack vector remains open on the D2 quote mechanics: the claim's "folded,
not claimed verbatim" wording is exactly what the document supports.

## Discipline

- Tooling: none installed. `pdftotext` 26.08.0, `curl` 8.23.0, `python3`,
  `pdfinfo` already present; RULES.md not triggered (no install needed). pacman untouched.
- Reads: W1 stage/reports read-only; no lane/fleet/git mutations; `git` not invoked.
- Scratch: `/fast/scratch/hyaku/kotodama-r77/ScoutD2Quote/` held `d2-live.pdf`,
  `d2-wb.pdf`, headers, `d2-live.txt`, `d2-verify.py`, `d2-verify-live.log`,
  `out/D2Q-5W.txt`, `out/D2Q-17W.txt`, run logs — deleted before yield.
- Freeze state: `reports/round-77/` had no `claims.json` (telemetry only), so all
  tool runs used `--claims-file` (rehearsal); `claims-frozen: no` in both files.
- Verified facts are all from commands quoted above; hashes shown are observed output.
