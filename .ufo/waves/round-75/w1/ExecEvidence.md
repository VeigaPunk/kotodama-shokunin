# ExecEvidence — round 75 (hyaku run 10), claim C evidence-capture tool

**Seat:** ExecEvidence (executor, leaf)
**Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
**Base revision:** `f556d1049fe651d3d63975600b13acd9fb686f15`
**Deliverable:** `.ufo/waves/round-75/counters/capture-evidence.py` (+ `README.md`, `fixtures/`)

---

## 1. What was built

The claim-C evidence-capture tool at
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75/counters/capture-evidence.py`
— 1598 lines, mode 755, sha256 `eee5f3d1b0425ecb4f489956cb45263bc306cc96a7a3930235f03b8ac43866c8`.
Python3 stdlib only, plus `curl` (http/https) and `pdftotext` (PDF bodies); no third-party Python.

**Provenance: this is the round-74 tool carried forward, not a rewrite.**
`.ufo/waves/round-74/counters/capture-evidence.py` (1367 lines, committed at base) already
implements exactly this grammar and is the established repo pattern for it. The round-75
file is that tool with this round's numbers (`ROUND = 75`, `ACCESS_DATE = 2026-10-27`,
output directory `reports/round-75/evidence/`) plus five deliberate round-75 changes, each
listed with its reason in §5. One grammar serves every round, so a counter reads any
round's evidence file the same way.

**Files written (only these):**

| path | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-75/counters/capture-evidence.py` | 74073 | `eee5f3d1b0425ecb4f489956cb45263bc306cc96a7a3930235f03b8ac43866c8` |
| `.ufo/waves/round-75/counters/README.md` | 5136 | `155e1c5feb1d1a08db2cd52c0aa7bf9cf5e1925cc1870fa35fad47cc11a180b1` |
| `.ufo/waves/round-75/counters/fixtures/r75-fixture.html` | 22278 | `9e53fbf0a0abff17bfb01319fae78d1daeea4b7e633ed1ff4fb5d024863b508e` |
| `.ufo/waves/round-75/counters/fixtures/r75-edge.html` | 14546 | `554fcff52276211f49666e6ee4e8d3250c97a6c8a0f11a95b0d0d3445ec6f226` |
| `.ufo/waves/round-75/counters/fixtures/r75-short.html` | 186 | `799ea4cf4f172a25e3191eb048b5c5c26811b8f2a74af9d82b32c20254d1dff3` |
| `.ufo/waves/round-75/counters/fixtures/r75-challenge.html` | 221 | `92b882824e9e884c96f788aafdd48e1798ed025aed7c7dad32ad223d8d9d7dc4` |
| `.ufo/waves/round-75/counters/probe-receipts/` | dir | the seven real captures + the raw curl headers + the selftest receipt, copied out of scratch before it was deleted (§4) |
| `.ufo/waves/round-75/w1/ExecEvidence.md` (this report) | — | — |

Nothing was written under `/home/vgpnk/Projects/shokunin/**` outside the lane repo; no
git/jj mutation was performed; the DRAFT `claims.json` and `ledger.json` were read only.

---

## 2. Grammar written

Round-74 grammar, in the round-75 key order the seat spec names:

```
# evidence <id> — claim C GATE (round 75)
url:            requested URL
ua:             exact User-Agent sent (verbatim)
http:           HTTP status, or `file` for a local path
bytes:          length of the stored body in bytes
sha256:         64-hex digest of those bytes
fetched:        UTC ISO-8601 second of the fetch
quote-found:    yes | no   (after NFKC/NFKD + whitespace folding)
quote-words:    whitespace tokens, `wc -w` reading
quote-chars:    characters, `wc -m` reading
visible-chars:  characters of the whole extracted visible text, collapsed
window-scope:   excerpt | whole-document
window:         chars=<n> min=<n> pad=<n> before=<n> after=<n>
window-sha256:  sha256 of the stored window line
window-bytes:   byte length of that same string
window-rule:    the hashing rule, restated inside the file
quote-found-verbatim: yes | no
challenge:      none | js-challenge | captcha | login-wall | consent-wall | geo-wall | empty-body
challenge-detail: what in the body named the challenge
content-type: / final-url: / extract:
fetch: / user-agent: / access-date: / http-status: / content-length:
transferred-bytes: / fetch-attempts: / fetch-command: / locator: / normalise: / quote:
--- window ---
<ONE line: >=4096 chars of extracted visible text around the quote>
--- quote ---
<the quote as supplied>
```

`ua:`/`user-agent:` and `http:`/`http-status:` stay deliberately duplicated: the
round-73/round-74 parser keys are `user-agent` and `http-status` and read the first
occurrence of each name, so both spellings must appear as their own lines.

**Window scope.** `excerpt` requires ≥ 4096 characters around the quote. `whole-document`
is used only when the whole extracted visible text is shorter than 4096 characters; the
stored window then IS that whole text, so its length must equal the recorded
`visible-chars:`. A short window under a long `visible-chars:`, or a whole-document claim
for a text that could have been excerpted, is a verification failure. `window-sha256:` and
`window-bytes:` are recomputed from the stored bytes; no flag in the file is trusted.

**Quote matching** (5 tiers, both sides folded identically): exact substring → NFKC +
whitespace collapse → NFKC + all whitespace removed (a source line break inside a CJK run
must not stop a match) → the same two under NFKD. `normalise:` records the tier that
matched.

---

## 3. The selftest receipt

Fixture HTML is **committed** under `counters/fixtures/`, so the selftest runs against
bytes a reader can read rather than a generator hidden in the source. The four fixtures:

| file | what it exercises |
|---|---|
| `r75-fixture.html` | CJK body, full-width Latin, HTML entities, a quote broken by a source line break, script/style/comment noise |
| `r75-edge.html` | the quote at the very start of the text (the window slides forward) |
| `r75-short.html` | a document shorter than 4096 characters → `whole-document` scope |
| `r75-challenge.html` | a JS challenge interstitial → `challenge: js-challenge`, exit 6 |

The spec's three required scenarios map to: **quote present** → `file-cjk-window`,
`cjk-narrative-quote`, `whitespace-collapse`; **quote absent** → `quote-missing` (exit 3,
file written, empty window) and `cjk-linebreak-refused` (exit 5, found only on the
whitespace-free tier the counter's fold cannot confirm); **whole-document scope** →
`window-whole-document` plus `whole-document-guard` (a truncated whole-document window
and a whole-document claim for a long text both fail verification); **CJK folding** →
`nfkc-fold` (full-width `ＡＢＣ１２３` vs ASCII `ABC123`), `cjk-linebreak-refused`,
`cjk-narrative-quote`.

Command and raw output:

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ python3 -B .ufo/waves/round-75/counters/capture-evidence.py --selftest
SELFTEST OK: 22 scenarios
EXIT=0
```

(The tool exits 0 and prints `SELFTEST OK: <n> scenarios`; a failure prints one
`SELFTEST FAIL: <name>: <detail>` line per failed scenario to stderr and
`SELFTEST FAIL: <passed>/<n>`, exit 1.)

Full scenario list: `file-cjk-window`, `r75-grammar-order`, `cjk-narrative-quote`,
`nfkc-fold`, `whitespace-collapse`, `cjk-linebreak-refused`, `quote-missing`,
`extract-visible`, `window-edge`, `window-whole-document`, `whole-document-guard`,
`http-fetch`, `fetch-retry`, `fetch-retry-gives-up`, `http-not-200`, `pdf-extract`,
`charset-gb18030`, `verify-mode`, `guards`, `challenge-detected`,
`challenge-none-on-clean-body`, `access-date-override`.

---

## 4. Real-network validation against this round's candidate rows

Every capture below was made by the tool, with the recorded UA, on 2026-10-27. **These
files live in the seat's scratch, not in `reports/round-75/evidence/`** — writing the
committed evidence directory is the L1's landing act (it carries the frozen row set and
the Gate quotes). They are proof the tool works on the round's actual documents.

| row | URL | http | bytes | sha256 (body) | scope | window-sha256 | quote |
|---|---|---|---|---|---|---|---|
| S885 | persee `..._num_8_1_1113` | 200 | 111486 | `2bcdd019ab1b2200…` | whole-document | `94acd2bac0cc946a…` | Introduction à l'analyse structurale des récits (6 w / 47 c) |
| S886 | persee `..._num_8_1_1120` | 200 | 109335 | `207ca821370928ca…` | whole-document | `7a7a196451f5cf1f…` | Les catégories du récit littéraire (5 w / 34 c) |
| S887 | persee `..._num_8_1_1114` | 200 | 118776 | `fbf48ad294cde358…` | whole-document | `792458eef629767d…` | Éléments pour une théorie de l'interprétation du récit mythique (9 w / 63 c) |
| S888 | jw.ucass.edu.cn `xushixue.pdf` | 200 | 225123 | `62a13e92e23d764c…` | excerpt | `1a593966ef00c5c2…` | 叙事学 (CJK, PDF via pdftotext) |
| S889 | jstage jcss `25_200/_pdf` | 200 | 1085244 | `fdf60d276b3f31cd…` | excerpt | `480205d800a5c957…` | narrative (PDF via pdftotext) |
| S890 | jstage jsik `32_2022_017/_pdf` | 200 | 697092 | `1dccf9d1427defb0…` | excerpt | `0b3a5e7b59bc4f31…` | 物語 (CJK, PDF via pdftotext) |
| S892 | wayback capture of iris.unipa.it PDF | 200 | 763802 | `8c0303670ff5db86…` | excerpt | `1fad732c9ebacfa0…` | HÉRITAGES ET CONTINUITÉS DE LA SÉMIOTIQUE TEXTUELLE (7 w / 51 c) |

Re-verification of the written files, all exit 0:

```
$ python3 -B .ufo/waves/round-75/counters/capture-evidence.py --verify <file>
VERIFY OK: …/S885.txt window-sha256=94acd2bac0cc946a9ec295633f40eaa7d1951ad5e945d6a0c5595dfc53958dc7 window-bytes=3852 window-chars=3720 quote-in-window=yes access-date=2026-10-27 http-status=200
VERIFY OK: …/S888.txt window-sha256=1a593966ef00c5c2b9723fea897c7c803f5b526f4d0313e34691a14fdfec3c52 window-bytes=6285 window-chars=4097 quote-in-window=yes access-date=2026-10-27 http-status=200
VERIFY OK: …/S892.txt window-sha256=1fad732c9ebacfa0c403c2cb59833c4e619717e5429db557ab24401c6d432ef7 window-bytes=4339 window-chars=4097 quote-in-window=yes access-date=2026-10-27 http-status=200
```

**Two findings the L1 needs (both are tool-level observations about this round's rows):**

1. **`https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html` (the S891 candidate)
   is served a JavaScript challenge, not the document.** HTTP 200, 6193 bytes, but the
   body is a JS proof-of-work interstitial (`window["bobcmn"] = …`,
   `Please enable JavaScript and cookies to continue`) and it yields **zero** visible
   text. The tool reports `challenge: js-challenge` and exits 6 — the challenge was met,
   not passed, so under QUALITY 10 the source is **UNOPENED**. The round-75 row_set lists
   this URL for S891; on the evidence gathered here it cannot be admitted as an opened
   source by this route. A wayback capture or another public copy would be the ordinary
   means that opens it; the flip condition should say so.
   Body sha256 `c799d5a4e567cdd6…`, content-type `text/html`, 6193 bytes.

2. **`https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014 marrone
   age dor---2.pdf` (the S892 candidate) returns HTTP 403** to the recorded UA
   (3373 bytes of HTML). The **Wayback capture opens it**: the CDX API
   (`http://web.archive.org/cdx/search/cdx?url=iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/*&output=json&filter=statuscode:200`)
   returns one 200 capture, `20251111222249`, mimetype `application/pdf`, length 759396;
   fetching `https://web.archive.org/web/20251111222249id_/<original>` through the tool
   gives HTTP 200, 763802 bytes, sha256 `8c0303670ff5db86…`, and `pdftotext` extracts
   69791 characters (the article *Héritages et continuités de la sémiotique textuelle*).
   The claim's row_set already says "via wayback capture" for S892 — this confirms that
   the wayback URL, not the iris URL, is the citable fetch, and the evidence file's
   `url:`/`fetch:` line must name the wayback URL.

Both are reported, not acted on: writing `reports/round-75/evidence/` and the Gate rows
is the L1's landing act.

**Interoperability check.** The round-74 counter's evidence parser
(`reports/round-74/accept-c.py::_evidence_core`) was run against round-75 output: it
accepts the round-75 file's `http-status`, `access-date`, `sha256`, `ua`, `window`,
`window-sha256`, `window-bytes`, `window-scope` and `visible-chars` without complaint
(the only reported item was the fetch-line/row-URL key match, which is the counter's
row-configuration concern, not the file's). The round-74 files `S877`/`S884` still verify
under the round-75 tool except for the access date (2026-10-25 vs this round's
2026-10-27), which is the expected round difference.

---

## 5. The five round-75 changes over the round-74 tool, with reasons

1. **Round constants and header order.** `ROUND = 75`, `ACCESS_DATE = 2026-10-27`, output
   default `reports/round-75/evidence/`; the header lines are emitted in the order the
   round-75 seat spec lists them (`url:`/`ua:`/`http:`/`bytes:`/`sha256:`/`fetched:`/
   `quote-found:`/`quote-words:`/`quote-chars:`/`visible-chars:`/`window-scope:`), with
   the round-73/round-74 keys kept after them so older-shaped parsers still read the
   file. The `r75-grammar-order` selftest scenario asserts the order.

2. **`challenge:` / `challenge-detail:` headers and exit code 6 (QUALITY 10).** New in
   round 75: the evidence file now says *what the server actually served*. A body that
   IS an interstitial is a challenge met, not passed — the source is UNOPENED and the
   capture is not citable. This is not speculative: it fired on a real row URL of this
   round (§4, finding 1). Detection is two-tiered because a raw-HTML keyword is not a
   wall — strong markers (`enable javascript and cookies to continue`,
   `cf-browser-verification`, …) are checked in the raw bytes; soft markers
   (`captcha`, `login`, `consent`, `geo`) are checked in the **visible** text and only
   when that text is short. **This matters here:** the persee pages carry a hidden
   `altcha-widget` (a PDF-download captcha) in their raw HTML — a raw-keyword detector
   would have wrongly refused three openable rows. The first detector version did exactly
   that and was corrected before the final selftest run; the tiered rule is what the
   delivered tool implements. `--verify` re-checks the challenge verdict, so a
   challenge-carrying file cannot pass verification later either.

3. **Committed fixtures.** The round-74 selftest generated its HTML inside the test. The
   round-75 fixtures are files under `counters/fixtures/`, so the selftest executes
   against bytes a reader can read. The inline generators remain as fallbacks so a copy
   of the tool outside the repo still self-tests.

4. **`--access-date YYYY-MM-DD`.** The recorded access date now defaults to the local
   date of the fetch but can be pinned explicitly. Reason: the round's access date is
   fixed at 2026-10-27 and `--verify` enforces it, so a capture made near local midnight
   would otherwise record a different date and fail its own verification. The override is
   validated (`YYYY-MM-DD` only) and recorded in the file. Selftest scenario
   `access-date-override` covers the pinned case and the malformed-date refusal.

5. **`challenge` is required only for round-75 files.** `REQUIRED_KEYS` stays the
   round-74 set so a round-74 evidence file still verifies under this tool; round-75
   files additionally must carry `challenge:` (the file's own title line decides which
   key set applies).

---

## 6. Dependencies, installs, scratch

- **No tool was installed.** `curl` (`/usr/bin/curl`), `pdftotext` (`/usr/bin/pdftotext`)
  and `python3` (3.14.8) were already present on the host; the tool uses nothing else.
  `pacman` was not run (host-wide pause).
- **Scratch discipline:** all scratch lives under
  `/fast/scratch/hyaku/kotodama-r75/ExecEvidence/` (probe bodies, headers, the seven
  real-capture evidence files, the wayback PDF). Nothing was written to `/tmp` outside
  the tool's own `tempfile.mkdtemp` working directories, which the tool removes in a
  `finally` block. The scratch directory was removed before this yield; the receipts
  quoted above are in this report.

---

## 7. Risks and blockers

- **The tool does not decide the row set.** It writes whatever evidence a seat asks
  for; the frozen row set and the Gate quotes belong to the L1's freeze commit. The
  counter (ExecCCounter's `reports/round-75/accept-c.py`) is the arbiter of whether an
  evidence file counts; the tool's own `--verify` implements the round-74 EVIDENCE-leg
  checks (status 200, access date, 64-hex sha256, browser-shaped UA, fetch line, window
  digest recomputed from the stored bytes, window-scope rule, quote present after NFKC +
  whitespace folding) so a seat can check its own file before committing it.
- **The round-75 counter may add a `challenge` requirement of its own.** This tool now
  writes `challenge: none` on every clean capture, so a counter that demands the key
  will find it; a counter that ignores it is unaffected. No coordination was needed
  because the key is additive.
- **Two row URLs of this round are not openable by ordinary means on the direct route**
  (§4). That is a sourcing fact, not a tool defect, and it is the L1's call whether
  S891 flips to a wayback/public copy and whether S892's row cites the wayback URL.
- **The `whole-document` scope is load-bearing for the three persee rows**: their
  extracted visible text is 3073–3720 characters, below the 4096 minimum, so the whole
  visible text is stored and `visible-chars:` equals the window length. The round-74
  counter's whole-document rule accepts exactly this shape. If the round-75 counter
  tightens the rule to require excerpts only, those three rows would need a fuller
  rendering (e.g. the PDF of the article) rather than the HTML landing page.

## 8. Checks the main agent should run

```
python3 -B .ufo/waves/round-75/counters/capture-evidence.py --selftest      # expect: SELFTEST OK: 22 scenarios, exit 0
python3 -m py_compile .ufo/waves/round-75/counters/capture-evidence.py     # expect: silent, exit 0
python3 -B .ufo/waves/round-75/counters/capture-evidence.py --verify reports/round-74/evidence/S884.txt
```
