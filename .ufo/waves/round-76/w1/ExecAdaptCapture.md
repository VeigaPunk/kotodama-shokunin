# ExecAdaptCapture — round 76, wave 1 (BUILD, stage only)

Verdict: **BUILD COMPLETE — stage-only, nothing installed, no lane path touched.**
`capture-evidence.py` is adapted from round 75 with the two routed fixes, all constants
read from the frozen claims document, and its whole test surface green (28 selftest
scenarios, a live capture of the round-75 S885 page whose window is byte-identical to
the round-75 file, and a compatibility check that runs round-75's own EVIDENCE
functions over the new file).

## 1. Files delivered (all under `.ufo/waves/round-76/w1/stage/ExecAdaptCapture/`)

```
$ find .ufo/waves/round-76/w1/stage/ExecAdaptCapture -type f | sort     (after removing __pycache__)
capture-evidence.py                 # the adapted counter (2531 lines, 119540 B)
check-r75-leg.py                    # compatibility check: round-75 accept-c EVIDENCE leg
demo-fixes.py                       # raw receipts for both fixes through the CLI
claims.json                         # the `capture` block the freeze should carry (rehearsal)
evidence/S885.txt                   # live capture of the round-75 S885 page
receipts/*.txt                      # 15 raw command receipts (see §5-§8)
```

`git status --porcelain -- .ufo/waves/round-76/w1/stage/ExecAdaptCapture` →
`?? .ufo/waves/round-76/w1/stage/ExecAdaptCapture/` — an untracked stage directory, and
that is the only path this seat wrote. No `reports/round-76`, no tracked lane file, no
fleet path, no jj/git mutation (`git -C <lane> show` and `git status` are the only git
calls).

Install record: **none.** No tool was installed or upgraded (no pacman, no uv, no npx).

## 2. What the adapted counter does differently from round 75

Round-75 source: `.ufo/waves/round-75/counters/capture-evidence.py` (1598 lines, read in
full before adapting). The fetch, decode, extractor, folding tiers, challenge detector,
digest/scope rules and self-verification are the round-75 code paths, unchanged.

**Fix 1 — anchor binding (R75-M2).** New required argument `--anchor-quote` (or
`--anchor-quote-file`): the registry row's ANCHOR span. The run locates it in the decoded
text, cuts the window (around the quote, or around `--find`), and then **refuses — exit 7,
no file written — when the anchor span is absent from the stored window after
NFKC+whitespace folding**. This is the S888/S892 shape from the round-75 lesson
(`corpus/lessons/round-75.md:313`, `:349`): a window cut at the head cannot reach an
anchor on p. 3. The refusal names the anchor's character offset and the window's range, so
the caller's next move is visible. The file records `anchor-quote:`,
`anchor-quote-chars:`, `anchor-quote-words:`, `anchor-found:`, `anchor-in-window:` (the
graded fact), `anchor-char:`, `quote-in-anchor:` and `quote-anchor-distance:`.
`verify_file`/`--verify` re-derive all of it from the stored bytes: a file whose anchor
line is stripped, or whose `anchor-in-window:` is not `yes`, fails (exit 5).

**Fix 2 — PDFs windowed by the page the locator names.** `--find` (or `--find-file`) is a
locator string; the window is cut around **its first occurrence in the whole decoded
document**, never the head. A PDF capture without `--find` is refused (exit 7). PDF text
keeps `pdftotext`'s form feeds (the round-75 `line.rstrip()` ate them, which is why no
page fact could be stated), so the file carries its own `find:`, `find-char:`,
`find-page:`, `find-hits:`, `page-count:` and `window-pages:`. `--verify` requires those
keys on a PDF file, requires `find-page` inside `window-pages: a..b`, and rejects a PDF
file whose `find:` is `(none supplied)`.

**Fix 3 — no byte count is canonical.** Every file carries its own `fetch:` and
`window-sha256:` (both were already there) plus a `bytes-rule:` line: *"bytes:/sha256:
describe THIS fetch only; a byte count is not canonical across fetches (one URL served
three counts in round 75)"*. §5 shows the same URL producing two different digests at the
same byte count inside this hour.

**Fix 4 — constants from the frozen claims.** `round`, `base`, the access date, the
evidence directory and the verdict prefix are read from
`git show <freeze>:reports/round-76/claims.json` (default `--freeze HEAD`, `--repo` = the
tool's git top level). `round` and `base` are mandatory; an access date is mandatory
(capture block → claim C `access_date` → `opened YYYY-MM-DD` in claim C's prose →
top-level `frozen` date); the grammar floors (4096 / 400 / 400), the browser UA and the
window-rule text fall back to the grammar constants and the provenance says so.
`--print-config` prints every value with its source. `--verify` rejects a file whose round
marker is not the frozen round (receipt `verify-round75-file.txt`: the round-75 S885 file
under round-76 claims → `the file names round 75 but the frozen configuration is round
76`, exit 5).

Scratch: `--work`, else `$HYAKU_SCRATCH`, else `$TMPDIR`, else `tempfile`'s default —
removed when the run ends, and no literal scratch root in the source (§9).

## 3. The claims contract the L1 must freeze (so the counter resolves every token)

The reader accepts the block at top level `capture`, at `capture_config`/`config`, or
inside claim C, with the aliases listed in `CAPTURE_ALIASES`. The exact block used for the
live test (`stage/ExecAdaptCapture/claims.json`, sha256 `bec8e13e…`):

```json
"capture": {
 "access_date": "2026-10-27",
 "min_window": 4096,
 "min_pad": 400,
 "default_pad": 400,
 "evidence_dir": "reports/round-76/evidence",
 "verdict_prefix": "ACCEPT-C-76",
 "ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
 "anchor_required": true,
 "find_required_for_pdf": true
}
```
plus top-level `"round": 76` and `"base": "<40-hex>"` (both already in the round-75
schema). `window_rule` is deliberately NOT set: omitting it uses the round-75-identical
grammar text, so a round-76 file's `window-rule:` line stays byte-equal to round 75's.

## 4. Live test — the known-good Persée page, anchor `Innombrables sont les récits du monde.`

```
$ python3 capture-evidence.py --claims-file claims.json --id S885 \
    --url https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 \
    --quote "Innombrables sont les récits du monde." \
    --anchor-quote "Innombrables sont les récits du monde." \
    --locator "notice body, opening sentence (article p. 1)" \
    --out evidence/S885.txt --work /fast/scratch/hyaku/kotodama-r76/ExecAdaptCapture
EVIDENCE S885: quote-found=yes verbatim=yes anchor-in-window=yes http=200 bytes=111486
  sha256=8e8ed88ab6d1fe9d window-chars=3720 window-scope=whole-document
  window-sha256=94acd2bac0cc946a find-page=- -> evidence/S885.txt
VERIFY OK: evidence/S885.txt window-sha256=94acd2bac0cc946a9ec295633f40eaa7d1951ad5e945d6a0c5595dfc53958dc7
  window-bytes=3852 window-chars=3720 quote-in-window=yes anchor-in-window=yes
ACCEPT-C-76: CAPTURE OK: evidence/S885.txt ... claims-frozen=no
EXIT=0
```
(receipt `receipts/capture-s885.txt`; the file also re-verifies standalone —
`receipts/verify-r76-file.txt`, exit 0.)

`claims-frozen: no` is honest and expected: the round-76 claims document is not committed
yet (this wave builds against the unfrozen draft). The capture reads the same code path a
`--freeze` run uses; the only difference is the provenance line. **At the freeze the L1
should re-run one command** so the committed receipt says `claims-frozen: yes`:

```
python3 capture-evidence.py --repo <lane> --freeze <freeze> --id S885 \
  --url https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 \
  --quote "<Gate quote>" --anchor-quote "<the row's anchor cell>" \
  --locator "<locator>" --out reports/round-76/evidence/S885.txt
```

### 4.1 Grammar diff against `reports/round-75/evidence/S885.txt` (receipt `receipts/grammar-diff.txt`)

```
$ diff -u reports/round-75/evidence/S885.txt .ufo/waves/round-76/w1/stage/ExecAdaptCapture/evidence/S885.txt
@@ -1,20 +1,37 @@
-# evidence S885 — claim C GATE (round 75)
+# evidence S885 — claim C GATE (round 76)
 url: https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113
 ua: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
 http: 200
-bytes: 109588
-sha256: 20b571d7a6a9bc3835b1406079adeea4279dc2bc4c5e7134c1ce31dbf25de034
-fetched: 2026-10-27T19:48:02Z
+bytes: 111486
+sha256: 8e8ed88ab6d1fe9d31522266fe861914f620bf135fca813fc988caef88534c71
+fetched: 2026-10-27T21:46:28Z
 quote-found: yes
 quote-words: 6
 quote-chars: 38
 visible-chars: 3720
 window-scope: whole-document
-window: chars=3720 min=4096 pad=400 before=714 after=2968
+window: chars=3720 min=4096 pad=400 before=714 after=2968 anchor-before=714 anchor-after=2968
 window-sha256: 94acd2bac0cc946a9ec295633f40eaa7d1951ad5e945d6a0c5595dfc53958dc7
 window-bytes: 3852
 window-rule: sha256 of the single stored window line, UTF-8, no trailing newline
 quote-found-verbatim: yes
+anchor-quote: Innombrables sont les récits du monde.
+anchor-quote-chars: 38
+anchor-quote-words: 6
+anchor-found: yes
+anchor-in-window: yes
+anchor-char: 714
+quote-in-anchor: yes
+quote-anchor-distance: 0
+find: (none supplied)
+find-char: -
+find-page: -
+find-hits: 0
+page-count: -
+window-pages: -
+bytes-rule: bytes:/sha256: describe THIS fetch only; a byte count is not canonical across fetches (one URL served three counts in round 75)
+claims-source: file:.ufo/waves/round-76/w1/stage/ExecAdaptCapture/claims.json sha256=bec8e13e...
+claims-frozen: no
 challenge: none
 challenge-detail: (none)
 content-type: text/html;charset=UTF-8
 ...
-transferred-bytes: 109588
+transferred-bytes: 111486
```

Diff summary: **additive only.** The round-75 key set is preserved in the round-75 order;
17 keys are added; `window:` keeps its five graded fields and gains `anchor-before=`
`anchor-after=`; `window-rule:` text is byte-identical (no `window_rule` override in the
claims); the only changed values are the fetch-specific ones (`bytes`, `sha256`,
`fetched`, `transferred-bytes`) — which is exactly fix 3, and `window-sha256` is
**unchanged**, i.e. the stored window is byte-identical across every observation.

Key-set diff (receipt `receipts/key-diff.txt`): `diff k75.txt k76.txt` → 17 additions,
`16a17,33`, no deletions. Header keys: round-75 file 33, round-76 file 50.

### 4.2 Four observations of one URL in one hour (fix 3's evidence)

| observation | `bytes:` | `sha256:` | `window-sha256:` |
|---|---|---|---|
| round-75 committed file (`reports/round-75/evidence/S885.txt`) | 109588 | `20b571d7…` | `94acd2ba…` |
| this seat, `fetched: 2026-10-27T21:43:46Z` | 111486 | `4bf3575f…` | `94acd2ba…` |
| this seat, `fetched: 2026-10-27T21:46:05Z` | 109588 | `cdbcc09a…` | `94acd2ba…` |
| this seat, `fetched: 2026-10-27T21:46:28Z` (delivered) | 111486 | `8e8ed88a…` | `94acd2ba…` |

Two observations share `bytes: 109588` with different digests. A lesson that restates a
byte count as canonical is restating one fetch of an unstable page; the window digest is
the stable fact.

## 5. How the round-75 `accept-c.py` EVIDENCE leg was checked against the new file

`check-r75-leg.py` imports the **committed** counter
(`reports/round-75/accept-c.py` at base `98c486b`), replaces only `read_tree` (to serve the
new file for `reports/round-75/evidence/S885.txt` and the real `corpus/SOURCES.md` /
`corpus/lessons/round-75.md` from `git show 98c486b:…`), and then calls the counter's own
`_evidence`, `_window`, `_evidence_core`, `_evidence_fetch_names_row`, `_gate_admit_row`,
`_evidence_gate_quote_candidates`, `_evidence_fold` — no re-implementation.

```
$ python3 check-r75-leg.py
_evidence_core: PASS
fetch names the row's document: PASS
Gate admit row found: PASS
Gate quote candidates: ["Introduction à l'analyse structurale des récits", 'Innombrables sont les récits du monde.']
Gate quote inside the stored window: PASS
header keys: round-75 33, round-76 50, dropped [], added ['anchor-quote', 'anchor-quote-chars',
  'anchor-quote-words', 'anchor-found', 'anchor-in-window', 'anchor-char', 'quote-in-anchor',
  'quote-anchor-distance', 'find', 'find-char', 'find-page', 'find-hits', 'page-count',
  'window-pages', 'bytes-rule', 'claims-source', 'claims-frozen']
window digest: header '94acd2ba...58dc7', accept-c window 94acd2ba...58dc7
R75-EVIDENCE-LEG-READS-R76-FILE: PASS
EXIT=0
```
(receipt `receipts/check-r75-leg.txt`)

Meaning: the round-75 parser finds every key it requires, the scope rule holds, the fetch
line names the row's document, the Gate quote lands inside the stored window under the
counter's own fold, and **no round-75 key was dropped**. A round-76 `accept-c.py` can add
the anchor check without touching the parser.

## 6. Fix-1 receipts (anchor binding, exit 7 = refused, nothing written)

```
$ python3 capture-evidence.py --claims-file claims.json --id FAR --url file://.../far-anchor.html \
    --quote 世界観の作り方は、一つの場所に集めることです。 --anchor-quote この錨は窓の外にある遠い段落です。
ACCEPT-C-76: REFUSED FAR: the row's anchor span is absent from the stored window after
  NFKC+whitespace folding (the anchor sits at char 8194 and the window covers chars 0-4098):
  cut the window with --find on the anchor's page, or raise --pad
EXIT=7

$ ... --id ABS --url file://.../top.html --anchor-quote この錨はページに存在しません
ACCEPT-C-76: REFUSED ABS: the row's anchor span is absent from the extracted text
  (9752 characters decoded): the anchor is not on the opened document
EXIT=7
```
(receipts `anchor-outside-window.txt`, `anchor-absent-from-page.txt`; neither out path
exists after the run.) The selftest also refuses an anchor that matches only the
whitespace-free tier (`anchor-fold-refused`), a capture without `--anchor-quote`
(`anchor-required`), and a stripped anchor line on `--verify` (`verify-mode`).

## 7. Fix-2 receipts (PDF windowed by the locator's page)

```
$ ... --id PDF-no-find --url file://.../pages.pdf --quote "PDF fixture quote sentence." \
      --anchor-quote "PDF fixture anchor span."
ACCEPT-C-76: REFUSED PDF-no-find: a PDF capture needs --find: the window is cut by the
  locator's page (its first occurrence in the whole decoded document), never by the head
EXIT=7

$ ... --id PDF-p5 ... --find "LOCATOR-MARKER page five"
EVIDENCE PDF-p5: quote-found=yes verbatim=yes anchor-in-window=yes http=file bytes=20385
  sha256=a3014dbd01d8d347 window-chars=4102 window-scope=excerpt window-sha256=12be382ce05ddeb3
  find-page=5 -> .../PDF-p5.txt
VERIFY OK: ... window-sha256=12be382ce05ddeb3f4a77d78ef8e8be451204062f4f550644a2546a699291b74
ACCEPT-C-76: CAPTURE OK: ...
EXIT=0

$ ... --id PDF-p2 ... --find "LOCATOR-MARKER"        # marker's FIRST occurrence is p. 2
ACCEPT-C-76: REFUSED PDF-p2: the row's anchor span is absent from the stored window after
  NFKC+whitespace folding (the anchor sits at char 11437 and the window covers chars 1037-5141):
  cut the window with --find on the anchor's page, or raise --pad
EXIT=7
```
(receipts `pdf-no-find.txt`, `pdf-find-page5.txt`, `pdf-find-first-occurrence.txt`.) The
captured PDF file states its own page facts (`receipts/pdf-p5.txt`):

```
find: LOCATOR-MARKER page five (first occurrence at char 10988 of 15778)
find-char: 10988
find-page: 5
find-hits: 1
page-count: 6
window-pages: 4..5
bytes-rule: bytes:/sha256: describe this fetch only; ...
extract: pdftotext -enc UTF-8 BODY - (stdlib subprocess, form feeds kept for page numbers); 15778 chars, 6 page(s)
fetch: GET file:///.../pages.pdf
window-sha256: 12be382ce05ddeb3f4a77d78ef8e8be451204062f4f550644a2546a699291b74
```

## 8. Negative-side receipts

```
$ python3 capture-evidence.py --verify evidence/S885.txt        # no claims file / freeze
ERROR: cannot read reports/round-76/claims.json at HEAD in /home/vgpnk/Projects/shokunin/
  kotodama-shokunin: fatal: path 'reports/round-76/claims.json' does not exist in 'HEAD'
EXIT=2
```
(receipt `claims-absent-refusal.txt`.) A missing claims document is a loud refusal, never a
silent default.

```
$ python3 capture-evidence.py --claims-file claims.json --verify reports/round-75/evidence/S885.txt
ACCEPT-C-76: VERIFY FAIL: .../S885.txt (1 problem(s))
VERIFY ...: the file names round 75 but the frozen configuration is round 76
EXIT=5
```
(receipt `verify-round75-file.txt`.) Round-75 files do not silently pass as round-76.

## 9. Hygiene checks

```
$ grep -nE '"/tmp|/tmp/' capture-evidence.py
EXIT=1                                  # nothing printed (receipt receipts/no-tmp-literal.txt)
$ python3 -m py_compile capture-evidence.py && echo COMPILE-OK
COMPILE-OK
$ python3 capture-evidence.py --selftest --work /fast/scratch/hyaku/kotodama-r76/ExecAdaptCapture
SELFTEST OK: 28 scenarios               # (receipt receipts/selftest.txt)
```
The tool contains no literal scratch root; the selftest *also* asserts that (scenario
`no-tmp-literal`, needle composed so the check does not itself carry the literal). Scratch
used: `/fast/scratch/hyaku/kotodama-r76/ExecAdaptCapture/`, deleted before this report
(`rm -rf`; the parent `/fast/scratch/hyaku/kotodama-r76` and sibling seat dirs untouched).

Selftest scenarios (28): `no-tmp-literal`, `claims-git-read`, `claims-constant-refusal`,
`claims-variant-constants`, `claims-missing-round`, `file-cjk-window`, `anchor-absent-document`,
`anchor-outside-window`, `anchor-fold-refused`, `anchor-required`, `quote-missing`,
`extract-visible`, `anchor-wrapped-argument`, `window-edge`, `window-whole-document`,
`whole-document-guard`, `verify-mode`, `http-fetch`, `fetch-retry`,
`fetch-retry-gives-up`, `http-not-200`, `challenge-detected`, `pdf-find-required`,
`pdf-find-page`, `pdf-find-first-occurrence`, `pdf-bytes-rule`, `guards`,
`claims-file-rehearsal`. The claims fixtures are real throwaway git repos
(`git init`, one commit per claims variant, identity scoped to the commit via `-c
user.name/-c user.email`), and the constants are proven live: a claims variant with
`access_date 2026-11-01` and `min_window 8192` produces a file recording that date and an
8199-character window (`claims-variant-constants`).

## 10. Risks, limits, blockers

1. **Provenance is rehearsal-grade until the freeze.** `evidence/S885.txt` records
   `claims-frozen: no` because `reports/round-76/claims.json` does not exist at HEAD yet
   (`claims-absent-refusal.txt`). The L1 must install the counter and re-run the capture
   with `--freeze <freeze>` (§4) for a citable file. Everything else in the file is final.
2. **The claims block must exist in the frozen document.** `round` and `base` are
   mandatory; without an access date the counter refuses (exit 2) rather than guess. The
   block in §3 is the exact shape the live test used; `capture.access_date` is the one key
   I recommend copying verbatim.
3. **`--find` is mandatory for PDFs** and the window is anchored on the locator's FIRST
   occurrence. A row whose locator appears earlier on another page will be refused, not
   silently mis-windowed — that is the fix, but a seat must pick a locator unique to the
   anchor's page (e.g. a phrase from that page's own text).
4. **Anchor refusals write nothing.** A seat that hits exit 7 must copy the refusal output
   into its report as the record; there is no half-file to inspect. This is deliberate (a
   receipt whose binding cannot be proven must not be citable).
5. **Not run / out of scope:** no build/lint/formatter gate (the wave's parent owns
   post-integration checks); no `reports/round-76/**` write; no verification against a real
   round-76 claims.json (it does not exist); the other eight round-75 evidence pages were
   not refetched — only S885, the page the assignment named.

No blockers. The counter is installable at `reports/round-76/capture-evidence.py` (or
`.ufo/waves/round-76/counters/`), and it self-tests from either location (the fixture
HTML is inline with a `fixtures/` override, so no data file must be committed with it).
