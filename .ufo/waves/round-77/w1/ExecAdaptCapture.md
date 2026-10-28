# ExecAdaptCapture — round-77 evidence capture tool (wave 1)

Seat: `ExecAdaptCapture` (executor, leaf). Lane: `kotodama-shokunin`, base
`211f9526800906e0c585d878d265c37e5e090c15`. Assigned: build the round-77
`capture-evidence.py` (live URL + same-page Wayback capture, UA→response binding,
located quote window with window-scope/sha256/bytes/verbatim flag, self-check,
PDF kept), plus one dry run on a public fixture page. **No lane writes.**

Verdict: **delivered**. Adapted tool + fixture dry run + two real
archive-backed runs + a real D2/S898 capture whose window sits on PDF p. 4
(§5b) all pass their own `VERIFY OK` / `CAPTURE OK`; the round-77 evidence
grammar is a strict superset of round 76's (0 round-76 keys lost).

## Files written (all under my stage dir, plus this report)

```
capture-block-rehearsal.json         rehearsal claims doc (capture block for the freeze)
capture-evidence.py                  the adapted tool  (3233 lines)
dry-run.py                           loopback fixture driver (live page + replay path)
fixture-page.html                    the public fixture page (13045 bytes)
dryrun/DRY-FIXTURE-LIVE.txt          evidence, window from the live page
dryrun/DRY-FIXTURE-WAYBACK.txt       evidence, window from the capture
dryrun/dry-fixture-live.log          verbatim stdout/stderr of that run
dryrun/dry-fixture-wayback.log       "
dryrun/dry-run-summary.log           the driver's `DRY RUN OK: 2/2 runs exit 0` line
dryrun/REAL-EXAMPLE-CAPTURE.txt      real archive run, window from the capture
dryrun/REAL-EXAMPLE-LIVE.txt         real archive run, window from the live page
dryrun/real-example-capture.log      verbatim stdout/stderr of that run
dryrun/real-example-live.log         "
dryrun/S898-P4.txt                   real D2 PDF capture, window on PDF p. 4 / journal p. 114
dryrun/s898-p4.log                   verbatim stdout/stderr of that run
dryrun/S898-P4-5W.txt                same window, quote = 5-word verbatim span, anchor = 17-word form
dryrun/s898-p4-5w.log                verbatim stdout/stderr of that run
dryrun/s898-p4-measure.py            page sweep over the fetched D2 PDF (tool's own extractor)
dryrun/s898-p4-measure.log           its output: 13 pages, p.4 = journal 114, quote on p.4
```

```
$ LC_ALL=C find <stage> -type f | LC_ALL=C sed "s|<stage>/||" | LC_ALL=C sort
capture-block-rehearsal.json
capture-evidence.py
dry-run.py
dryrun/DRY-FIXTURE-LIVE.txt
dryrun/DRY-FIXTURE-WAYBACK.txt
dryrun/REAL-EXAMPLE-CAPTURE.txt
dryrun/REAL-EXAMPLE-LIVE.txt
dryrun/S898-P4-5W.txt
dryrun/S898-P4.txt
dryrun/dry-fixture-live.log
dryrun/dry-fixture-wayback.log
dryrun/dry-run-summary.log
dryrun/real-example-capture.log
dryrun/real-example-live.log
dryrun/s898-p4-5w.log
dryrun/s898-p4-measure.log
dryrun/s898-p4-measure.py
dryrun/s898-p4.log
fixture-page.html
```
`<stage>` = `.ufo/waves/round-77/w1/stage/ExecAdaptCapture/`.

Digests — `sha256sum <stage>/{capture-evidence.py,dry-run.py,fixture-page.html,capture-block-rehearsal.json,dryrun/s898-p4-measure.py}`:

```
bab5ca44f78540059b07f22c1ee2254ae310075c865355841b24c0d49030f8b5  capture-evidence.py
ce3763308d480e062b34dc4e4d4f75d9ad2a66c43387f73d9934aa4faa1b1674  dry-run.py
910ba24d5907f369c6bebd18918f2ffd00163934d9927a3a0cf2dbd1e704ab3b  fixture-page.html
3a313fb69443c348982432e61add3b4e1ec294bf770ace17b236496a65047a34  capture-block-rehearsal.json
7b62265950b41988d71cd905ab998f6892a32261e2e0134af7015bf9e6485303  dryrun/s898-p4-measure.py
```
3233 lines — `wc -l <stage>/capture-evidence.py` (round-76 source: 2531 — same command).

## 1. What the adaptation changes (each delta has a failing selftest scenario)

1. **Two fetches per receipt (QUALITY 18).** The tool fetches the live URL *and*
   its replay URL; `window-source: live|wayback` says which body the window was
   cut from and which fetch the top-level `http-status:`/`bytes:`/`sha256:`/
   `ua:`/`final-url:`/`fetched:` atoms describe. Falls back to the capture
   whenever the live fetch cannot be cited or does not carry the quote; the
   auto-choice is recorded, never assumed. Failing scenarios: `live-window`,
   `wayback-window`, `live-wall-capture-window`, `challenge-live-clean-capture`.
2. **Same-page is proven, not asserted.** `wayback_parts()` reads the captured
   page out of the replay path (`/web/<ts>[id_|if_]/<original>`); the original is
   compared with the live URL under `norm_url()` (scheme, a leading `www.`, a
   default port, a trailing slash dropped). `wayback-original`,
   `wayback-same-page`, `wayback-final-original`, `wayback-final-same-page`
   record it. A capture of another page is refused (exit 7, nothing written).
   Failing scenarios: `capture-pair-refusals` (wrong page), `round77-pair`.
   Real-world wrinkle the normalisation exists for: the replay of
   `https://example.com/` redirects to `.../http://www.example.com/` — recorded
   as `wayback-final-original: http://www.example.com/`,
   `wayback-final-same-page: yes` (see `dryrun/REAL-EXAMPLE-CAPTURE.txt`).
3. **UA→response binding (QUALITY 22).** One line per fetch pairs the exact UA
   sent with the response that request got:
   `response-bind-live: ua="Mozilla/5.0 …" -> http=200 bytes=577 sha256=… final-url=…`
   and the same for the capture plus `memento=…`. `--wayback-ua` lets the two
   differ and still be bound. `verify_file()` checks the bind line carries the
   recorded UA, status and sha256 for *each* fetch. Failing scenario:
   `pair-graded` (a tampered bind line fails verification).
4. **A capture must be datable.** `wayback-memento-datetime` (from
   `Memento-Datetime`) and `wayback-timestamp-matches: yes|nearest|-`; a 200
   capture that serves no memento is refused. Failing scenario:
   `capture-pair-refusals` (no-memento route). Live example of `nearest`: the
   real run asked for `20240111092427`, the archive redirected to
   `20240111092827` and the file says so.
5. **The row pair is a refusal, not a warning.** A capture that is not HTTP 200
   for the live page's URL is refused before writing. Failing scenario:
   `capture-pair-refusals` (uncaptured route).

Unchanged from round 76 (same code paths, same meanings): extraction, folding
tiers, window + digest rule, `window-scope` rule, anchor binding (`R75-M2`),
PDF `--find`/page window, challenge detector, `window-sha256` recomputation,
claims-driven constants, no literal scratch root.

## 2. Grammar compatibility (measured, not asserted)

Round-77 evidence is a strict key-superset of round-76 evidence:

```
$ python3 -c '…keys(reports/round-76/evidence/S894.txt) vs keys(<stage>/dryrun/REAL-EXAMPLE-CAPTURE.txt)…'
round-76 keys: 49 round-77 keys: 91
present in r76 and missing from r77: []
added by round 77: 42
```
The 42 added keys are the `window-source`/`window-fetch`, `wayback-*`, `live-*`,
`response-bind-*` families plus `quote-page`/`anchor-page` (the page each cited
span sits on; see §5b). Every round-76 key keeps its R76 position and
meaning (the selftest's `key-order` clause checks the first 11 keys are still in
round-76 order).

`--verify` on a round-76 file is *not* claimed: `_declared_round()` makes a file
that names round 76 fail against a round-77 configuration ("names round 76 but
the frozen configuration is round 77") — a round-76 receipt belongs to that
round's counter. Not run: verifying any `reports/round-76/evidence/*.txt` under
the round-77 config (expected exit 5 by design, no receipt taken).

## 3. Selftest — 36 scenarios

```
$ python3 -B <stage>/capture-evidence.py --selftest --work /fast/scratch/hyaku/kotodama-r77/ExecAdaptCapture
SELFTEST OK: 36 scenarios
```
Scenario coverage (all in-process; a loopback server stands in for the live site
and for archive.org's replay path, recording the UA of every request):

`no-tmp-literal`, `claims-git-read` (round 77, `git show <rev>:reports/round-77/claims.json`),
`claims-constant-refusal`, `claims-variant-constants` (min_window 8192 honoured),
`claims-missing-round`, `live-window` (25 clauses incl. key order, digest, pad,
anchor binding, verdicts), `round77-pair` (16 clauses: same-page, memento,
bind lines, both UAs actually sent), `wayback-window`,
`live-wall-capture-window` (live 403 → capture window), `challenge-live-clean-capture`,
`challenge-detected` (both halves walls → exit 6), `anchor-absent-document`,
`anchor-outside-window`, `anchor-fold-refused`, `anchor-required`,
`wayback-required`, `quote-missing`, `extract-visible`, `anchor-wrapped-argument`,
`window-edge`, `window-whole-document`, `whole-document-guard` (truncated +
forged scope both exit 5), `verify-mode` (stripped anchor / edited window /
forged digest), `pair-graded` (tampered bind, tampered `live-bytes`),
`capture-pair-refusals` (wrong page 7, uncaptured 7, no memento 7),
`wayback-timestamp-builds-url`, `http-fetch`, `fetch-retry`,
`fetch-retry-gives-up`, `http-not-200` (exit 4), `guard`s (min-window/pad/empty),
`claims-file-rehearsal`, and PDF `pdf-find-required` / `pdf-find-page`
(`find-page: 5`, `window-pages` covers 5, `quote-page: 5`, `anchor-page: 5`,
`page-count >= 5`) / `pdf-find-first-occurrence` (exit 7) / `pdf-page-facts`
(a `quote-page` outside `window-pages`, or a non-numeric page, exits 5).

PDF legs ran: `pdftotext` present — `which pdftotext` → `/usr/bin/pdftotext`; no
scenario reported `SKIPPED: pdftotext absent`.

Fixture git repos: the selftest builds one throwaway repo per claims document and
asserts `git rev-parse --show-toplevel` equals that repo before the first commit;
commits use `-c user.name=fixture -c user.email=fixture@invalid`.

Static check (pyflakes 4.0.3, `~/.local/bin/pyflakes`, already installed —
`uv tool install pyflakes` printed ``` `pyflakes` is already installed ```):

```
$ pyflakes <stage>/capture-evidence.py <stage>/dry-run.py ; echo rc=$?
rc=0
```

## 4. Dry run — local public fixture page

`dry-run.py` serves `fixture-page.html` (13045 bytes) at
`/fixture-page.html` and at the archive-shaped
`/web/20260101000000id_/http://127.0.0.1:<port>/fixture-page.html` (200 +
`Memento-Datetime: Thu, 01 Jan 2026 00:00:00 GMT`), then runs the tool twice.

```
$ cd <stage> && python3 -B dry-run.py --work /fast/scratch/hyaku/kotodama-r77/ExecAdaptCapture
DRY RUN OK: 2/2 runs exit 0
```
`dryrun/dry-fixture-live.log` (verbatim, truncated to the receipt lines):

```
EVIDENCE DRY-FIXTURE-LIVE: quote-found=yes verbatim=yes anchor-in-window=yes window-source=live live-http=200 wayback-http=200 wayback-same-page=yes memento=Thu, 01 Jan 2026 00:00:00 GMT bytes=13045 sha256=910ba24d5907f369 window-chars=4102 window-scope=excerpt window-sha256=f25d3481948e9c86 find-page=- -> <stage>/dryrun/DRY-FIXTURE-LIVE.txt
VERIFY OK: … window-bytes=4102 window-chars=4102 quote-in-window=yes anchor-in-window=yes window-source=live wayback-same-page=yes wayback-memento=Thu, 01 Jan 2026 00:00:00 GMT
ACCEPT-C-77: CAPTURE OK: … window-source=live wayback-same-page=yes wayback-memento=Thu, 01 Jan 2026 00:00:00 GMT claims-frozen=no
exit=0
evidence: dryrun/DRY-FIXTURE-LIVE.txt bytes=10359 sha256=73352eb2709d24fcd653727157bb1b7cce2bbcd54a79eb50f829da308662bbab
```
`dryrun/dry-fixture-wayback.log` is the same capture with
`--window-from wayback`: `window-source=wayback`, same `window-sha256`
(`f25d3481948e9c86…`), `exit=0`,
`evidence: dryrun/DRY-FIXTURE-WAYBACK.txt bytes=10500 sha256=7b6ab4c6673774b1e465584c2a1589acd8614bee85d4551673ec3bcd20f8e5a8`.
Both runs record `claims-frozen=no`: they read `capture-block-rehearsal.json`
via `--claims-file`, because **`reports/round-77/claims.json` does not exist
yet** (`ls reports/round-77/` → `telemetry` only; the freeze creates it).

## 5. Dry run — real public page and real archive capture

Same tool, no fixture server: live `https://example.com/` and the real replay
`https://web.archive.org/web/20240111092427id_/https://example.com/`.

Real behaviour this proves (and that the fixture cannot): the live page changed
since the capture (577 bytes today vs 1256 archived), and the archive redirected
the replay to `http://www.example.com/` at `09:28:27` — both are facts in the file.

```
$ cd <stage> && python3 -B capture-evidence.py --claims-file capture-block-rehearsal.json \
    --id REAL-EXAMPLE-CAPTURE --url https://example.com/ \
    --wayback-url https://web.archive.org/web/20240111092427id_/https://example.com/ \
    --quote 'This domain is for use in illustrative examples in documents.' \
    --anchor-quote 'You may use this domain in literature without prior coordination or asking for permission.' \
    --locator 'example.com, capture 2024-01-11, second paragraph' \
    --out dryrun/REAL-EXAMPLE-CAPTURE.txt --work <scratch>
exit=0
```
(from `dryrun/real-example-capture.log`) `window-source=wayback` — the live page no
longer carries the quote — `live-http=200 wayback-http=200 wayback-same-page=yes
memento=Thu, 11 Jan 2024 09:28:27 GMT bytes=1256 window-chars=187
window-scope=whole-document`, and `wayback-timestamp-matches: nearest`
(asked 09:24:27, served 09:28:27). `CAPTURE OK`.

```
$ cd <stage> && python3 -B capture-evidence.py --claims-file capture-block-rehearsal.json \
    --id REAL-EXAMPLE-LIVE --url https://example.com/ \
    --wayback-url https://web.archive.org/web/20240111092427id_/https://example.com/ \
    --quote 'This domain is for use in documentation examples without needing permission.' \
    --anchor-quote 'This domain is for use in documentation examples without needing permission.' \
    --locator 'example.com, live 2026-10-27, first paragraph' \
    --out dryrun/REAL-EXAMPLE-LIVE.txt --work <scratch>
exit=0
```
`window-source=live`, `bytes=577`, `wayback-bytes=1256`, `wayback-quote-found: no`
(the capture predates the rewording), `live-quote-found: yes`, `CAPTURE OK`.

The bind lines as written in `dryrun/REAL-EXAMPLE-CAPTURE.txt`:

```
response-bind-live: ua="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> http=200 bytes=577 sha256=25ddf2c883e0d1958ea971d279a7e4f0fd446724ee3db7db19dadabd4a62e484 final-url=https://example.com/
response-bind-wayback: ua="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> http=200 bytes=1256 sha256=ea8fac7c65fb589b0d53560f5251f74f9e9b243478dcb6b3ea79b5e36449c8d9 final-url=https://web.archive.org/web/20240111092827id_/http://www.example.com/ memento=Thu, 11 Jan 2024 09:28:27 GMT
```

## 5b. D2 / S898 — the window must reach PDF p. 4 (the routed p5/p115 defect)

The peer question (`KotodamaR77`, 23:0x): the attributed 88-term quote is on
journal p. 114 / PDF p. 4, but the S898 evidence window said p5/p115. This is a
*build* question for the tool, not a wording question: the window must be cut by
a locator that first occurs on p. 4, and the file must let a counter check the
page the quote itself sits on. Both are now true, and one key was added for it.

**Measured with the tool's own extractor** on the live PDF (`s898-p4-measure.log`;
the PDF is the one `s898-p4.log` fetched: 417093 bytes,
`sha256 5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc`,
identical to the `20260901045105id_` capture — `sha256sum d2-live.pdf d2-wb.pdf`
printed one digest twice):

```
pdf sha256: 5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc
page-count: 13
page  4: 114 Irena Kałużyńska Liu (1996, p. 46) stated: “Flowers, plants and trees are also frequently used t
page  5: FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA  115 data: 2,500 characters occurred in the na
17-word-quote: found=True verbatim=False tier=folded start=10433 pages=[]
locator: found=True verbatim=True tier=verbatim start=10433 pages=[4]
raw around the locator: 'and trees in China.\nAccording to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms\ndenoting plants, flowers and trees (general terms, species or the parts of flowers or trees) among the '
pdftotext -layout page 4: 17-word occurrences=0
```
So: PDF p. 4 is journal p. 114 (page head `114   Irena Kałużyńska`), the locator
`According to Kałużyńska (2008, pp. 223, 232)` occurs **verbatim exactly once,
at char 10433, on p. 4**, and the 17-word quote starts at that same char on p. 4.

**The real capture produced from it** (`dryrun/S898-P4.txt`, run log
`dryrun/s898-p4.log`, exit 0, `VERIFY OK`, `CAPTURE OK`):

```
$ python3 -B capture-evidence.py --claims-file capture-block-rehearsal.json --id S898-P4 \
    --url https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/ \
    --wayback-url https://web.archive.org/web/20260901045105id_/https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/ \
    --quote 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees' \
    --anchor-quote '<the same 17-word form>' \
    --find 'According to Kałużyńska (2008, pp. 223, 232)' \
    --locator '§3 ¶1 second sentence, journal p. 114 / PDF p. 4' \
    --out dryrun/S898-P4.txt --work <scratch>
exit=0
find: According to Kałużyńska (2008, pp. 223, 232) (first occurrence at char 10433 of 33690)
find-page: 4
find-hits: 1
page-count: 13
window-pages: 3..5
quote-page: 4
anchor-page: 4
quote-found: yes
quote-found-verbatim: no
window-scope: excerpt   (window-chars=4098, window-sha256=fb65bae17dc50fe3c3b25b1ebe234e024fdb501819314a253a93ee18717e52a5)
window-source: live   (wayback-http 200, memento Tue, 01 Sep 2026 04:51:05 GMT, wayback-timestamp-matches: yes)
```

**What changed in the tool for this:** `quote-page:` and `anchor-page:` (the page
each cited span sits on, computed from the document's own form feeds) are now
recorded — the counter cannot recompute them from the stored window, because the
window is whitespace-collapsed and drops the form feeds. `verify_file()` grades
them: a PDF evidence file whose `quote-page`/`anchor-page` falls outside
`window-pages`, or is not a page number, fails EVIDENCE (selftest
`pdf-page-facts`). That is what makes "the window reached p. 4" a checkable fact
instead of prose.

**One finding the Gate must not paper over:** the 17-word form is *not*
`quote-found-verbatim` in this PDF. The source wraps the sentence after
`88 terms`, so it matches only at the folded tier (`matched=folded`) — and the
same is true under `pdftotext -layout` (`17-word occurrences=0` on p. 4). The
stage file `stage/ScoutDocS898/evidence.txt` records
`quote-found-verbatim: yes` and `normalise: … matched=verbatim` for that span;
that is not reproducible with either extraction mode, and its own stored window
line is already whitespace-folded.

**Recommended split — quote = 5 words verbatim, anchor = the 17-word sentence
(measured: `dryrun/S898-P4-5W.txt`).** The fragment
`there were altogether 88 terms` occurs exactly once, **verbatim**, at char
10479 on PDF p. 4 (`count=1 verbatim=True tier=verbatim pages=[4]`,
`s898-p4-measure.log`); the 17-word attribution-bearing sentence *contains* it
and matches at the folded tier. Capturing with `--quote` = the 5-word span and
`--anchor-quote` = the 17-word form gives, in one file:

```
quote-found: yes        quote-found-verbatim: yes      matched=verbatim
quote-words: 5          quote-chars: 30
anchor-quote-chars: 111 anchor-found: yes  anchor-in-window: yes
quote-in-anchor: yes    quote-anchor-distance: 46
find-page: 4   window-pages: 3..5   quote-page: 4   anchor-page: 4
window-chars: 4098  window-sha256: fb65bae17dc50fe3c3b25b1ebe234e024fdb501819314a253a93ee18717e52a5
window-source: live  wayback-http: 200  memento Tue, 01 Sep 2026 04:51:05 GMT
exit=0   VERIFY OK   CAPTURE OK
```
That keeps the Gate quote exact and verbatim while the same evidence file binds
it *inside* the attribution-bearing sentence (`quote-in-anchor: yes`), so the
entry body carries "According to Kałużyńska (2008, pp. 223, 232), there were
altogether 88 terms…" without the receipt asserting a verbatim 17-word span.
If the row instead wants the full sentence as the quote, that is the folded
option (§7) and must be graded as located-at-fold.

**Access date: keep `2026-10-27`.** The fetches ran at `2026-10-28T02:0xZ` UTC,
which is still 2026-10-27 locally (`date '+%F %T %z'` →
`2026-10-27 23:01:29 -0300`, America/Sao_Paulo). Round 76 recorded exactly this
pairing: all three committed evidence files say `access-date: 2026-10-27` while
their `fetched:` lines say `2026-10-28T00:11:57Z` / `00:20:25Z` / `00:12:00Z`,
and round 76's claims say `frozen: 2026-10-27`. So the claims' access date stays
the round's local date and the file's `fetched:` line carries the UTC second; no
change is needed, and the tool refuses an `--access-date` that differs from the
claims' date.

## 6. What the L1 needs at the freeze (handoff, not done here)

1. **Freeze `reports/round-77/claims.json` with a `capture` block.** The tool
   reads `round`, `base`, `access_date` and the capture constants through
   `git show <freeze>:reports/round-77/claims.json`; `capture-block-rehearsal.json`
   is the block I dry-ran against (`--print-config` shows every key and its
   provenance: `round 77`, `verdict_prefix ACCEPT-C-77`,
   `evidence_dir reports/round-77/evidence`, `min_window 4096`, `min_pad 400`,
   `default_pad 400`, `wayback_prefix https://web.archive.org/web`,
   `access_date 2026-10-27`).
2. **`accept-c.py` EVIDENCE leg must read the round-77 keys.** The grammar is
   additive (§2), so a round-76-shaped reader still parses the file; the new
   facts a counter should grade are `window-source`, `wayback-same-page`,
   `wayback-memento-datetime`, `wayback-http`, and the two `response-bind-*`
   lines (the tool's own `verify_file()` is the reference implementation and is
   exercised by `--verify` in the selftest).
3. **Invocation shape for the two rows** (S897 = D1 cssn 403 wall → capture is
   the window; S898 = D2 Onomastica PDF → `--find` required):
   ```
   capture-evidence.py --repo . --freeze <freeze> --id S897 \
     --url http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml \
     --wayback-url https://web.archive.org/web/20240111092427id_/http://lishisuo.cssn.cn/… \
     --quote-file <row quote> --anchor-quote-file <row anchor> --locator "…" \
     --out reports/round-77/evidence/S897.txt
   capture-evidence.py --repo . --freeze <freeze> --id S898 \
     --url https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/ \
     --wayback-url https://web.archive.org/web/20260901045105id_/https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/ \
     --quote-file <the 5-word verbatim span: "there were altogether 88 terms"> \
     --anchor-quote-file <the 17-word attribution-bearing form> \
     --find 'According to Kałużyńska (2008, pp. 223, 232)' \
     --locator '§3 ¶1 second sentence, journal p. 114 / PDF p. 4' \
     --out reports/round-77/evidence/S898.txt
   ```
   The S898 argv above is not a sketch: it is the `dryrun/S898-P4-5W.txt` run of
   §5b (`quote-found-verbatim: yes`, `quote-in-anchor: yes`, `find-page: 4`,
   `quote-page: 4`, `window-pages: 3..5`, `CAPTURE OK`) — the L1 can install that
   file as `reports/round-77/evidence/S898.txt` once the claims are frozen (the
   only difference is `--repo/--freeze` instead of `--claims-file`, so
   `claims-frozen` becomes `yes`). `dryrun/S898-P4.txt` is the same window with
   the 17-word form as both quote and anchor (`matched=folded`), kept for
   comparison. **D1/S897 was not fetched or captured by this seat** (out of
   scope), so its invocation is a shape, not a receipt.

## 7. Risks / open points

- **Window `whole-document` on short pages.** Both real example.com runs are
  `whole-document` (187 / 156 visible chars < 4096) — correct by the rule, and
  refused by the verifier if it were claimed for a long text. A real row on a
  long article will be `excerpt`.
- **`wayback-timestamp-matches: nearest` is allowed** (archive redirects an
  uncaptured second to the nearest capture and the memento states the truth).
  A counter that wants exact-match must reject `nearest` explicitly; the tool
  records the fact rather than hiding it.
- **`live-challenge` on the non-window fetch is allowed** when the window came
  from the capture (D1's shape). If the freeze wants a live-wall row refused
  outright, that is a one-line change in `_verify_round77`; I left it allowed
  because the claims draft names D1 as "live 403 wall, capture 200".
- **`--allow-file` remains for local fixtures only**; graded captures must be
  HTTP 200 and `verify` refuses `file` without the flag.
- **D2's 17-word form is folded, not verbatim (measured, §5b).** The PDF wraps
  the sentence after `88 terms`, so a 17-word quote can only be
  `quote-found-verbatim: no` / `matched=folded` — under `pdftotext -layout` the
  form does not occur on p. 4 at all. The recommended receipt therefore quotes
  the 5-word verbatim span and binds it inside the 17-word sentence via
  `anchor-quote` (`quote-in-anchor: yes`); a Gate row must not claim verbatim for
  the full sentence.
- **Extraction mode is part of the grammar.** The tool extracts PDFs with
  `pdftotext -enc UTF-8` (no `-layout`), round-76's mode. A hand-rolled
  `-layout` extraction (as in `stage/ScoutDocS898/evidence.txt`) is a different
  text and can disagree about `verbatim`; the counter reads the tool's mode.
- **`find-page` and `quote-page` can differ legitimately** (a locator may be a
  heading on the previous page); both are graded only against `window-pages`, not
  against each other.

## 8. Discipline notes

- Writes: only `<stage>/**` (listed above) and this report. No lane file, no
  `reports/round-77/**` write (that dir is the L1's), no fleet-repo write, no git
  state touched in the lane (read-only `git show` of the base by the tool's
  claims loader was not exercised here — the dry runs used `--claims-file`).
- Scratch `/fast/scratch/hyaku/kotodama-r77/ExecAdaptCapture/` was used for the
  selftest temp dirs and the tool's `--work`, and was deleted after the receipts
  were copied into `<stage>/dryrun/`. No `/tmp` path is cited as evidence.
- Installs: none. `uv tool install pyflakes` reported ``` `pyflakes` is already
  installed ``` (4.0.3, `~/.local/bin/pyflakes`); no pacman call was made.
- Not run (reported as unrun): the round-76 evidence files were not re-verified
  under the round-77 configuration; **D1/S897 was not fetched or captured**; the
  tool's `git show`-based claims path was exercised only inside the selftest's
  fixture repos, not against the lane (both real runs used `--claims-file`).
- D2/S898 *was* fetched (live + `20260901045105id_` capture) for §5b; the PDF
  itself lives only in scratch and is identified by
  `sha256 5d1bfa5a…` in `dryrun/s898-p4-measure.log`, so the receipt survives the
  scratch deletion. `reports/round-77/evidence/S898.txt` was **not** written: the
  run that proves the p. 4 window wrote `dryrun/S898-P4.txt` inside my stage.
