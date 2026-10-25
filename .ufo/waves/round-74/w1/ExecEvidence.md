# ExecEvidence — claim-C evidence-capture tool (round 74 / hyaku run 7)

Seat: executor, leaf. Wave 1. Base revision `f7104cbce186bc2e1522abf0cfd619cc834628bb`.
Round-74 `reports/round-74/claims.json` read as DRAFT and not edited. No delegation, no
background services of mine (one transient shell job was auto-backgrounded by the harness;
recorded where it matters in §5). No tool installed (curl 8.23.0, pdftotext 26.08.0 and
python 3.14.8 were already present); `pacman` never run.

Files written, and nothing else:

| path | what |
|---|---|
| `.ufo/waves/round-74/counters/capture-evidence.py` | the deliverable (984 lines, 42374 B, `sha256 4e06fb52aab070139bdebad26a5a27313a59c9fb0942b88c413731c96b8f4f55`, mode 755) |
| `.ufo/waves/round-74/w1/ExecEvidence.md` | this report |
| `/tmp/ExecEvidence/**` | scratch: dry-run captures, controls, compat harnesses, fixtures |

No evidence file was written into the lane: the four candidate captures are dry runs in
`/tmp/ExecEvidence/evidence/`, as the seat item requires. The fleet repo, `shokuknow`, the
lane's git state, `.ufo/state`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `corpus/**`,
`reports/round-74/claims.json` and the six inherited round-73 w2 seat files are untouched
(`git status --porcelain` shows only the pre-existing round-73 w2 modifications and the
untracked `round-74` trees that other seats are filling).

## 1. What the tool does

One command turns a URL plus a quote into the evidence file the claim-C EVIDENCE leg reads:

```
python3 -B .ufo/waves/round-74/counters/capture-evidence.py \
  --id S881 --url <url> --quote-file /tmp/q-S881.txt \
  --out reports/round-74/evidence/S881.txt --locator "<heading / paragraph>"
```

- **Fetch.** `curl -sS -L --compressed --connect-timeout 20 --max-time 90 -A "<browser UA>"`,
  with the round's browser-shaped UA as the default (`Mozilla/5.0 (X11; Linux x86_64)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`), `-w` for status /
  effective URL / transfer size, `-D` for headers. Transport failures (curl exit
  7/18/28/35/52/55/56) are retried with backoff; HTTP failures are not. `file://` and bare
  paths are read directly (recorded as `http: file`).
- **Record.** The requested URL, status, body byte length, sha256 of the body, UTC fetch
  second, the exact UA string, Content-Type, effective URL, Content-Length (or `-`), the
  wire size, the attempt count and the literal curl argv go into the header.
- **Extract.** HTML → visible text with `html.parser` only (comments and
  `script/style/noscript/template/svg/head` dropped, block tags → newline, entities decoded,
  blank lines dropped, intra-line ASCII spaces collapsed). Charset from Content-Type, then
  `<meta charset>`, then BOM, then a UTF-8 → GB18030 → Big5 → Shift_JIS → EUC-JP → CP1251 →
  CP1252 ladder. PDF bodies go through `pdftotext -enc UTF-8`. CJK needs no word
  segmentation; the extractor never inserts a separator between an inline tag's neighbours,
  so `<strong>勢力図・人間関係の構造</strong>：…` stays one contiguous string.
- **Locate.** Tiers, strongest first: exact substring; NFKC per character with whitespace
  runs folded to one space; the same with all whitespace removed (a source line break inside
  a Japanese or Chinese run must not stop a match); then the two folded tiers under NFKD.
  The fold carries an index map back to source offsets, so the window is cut from the
  undecorated text, not from the folded copy.
- **Write.** The window is `pad=400` characters each side of the located quote, cut verbatim
  from the extracted text, plus the quote itself. `quote-found`, `quote-found-verbatim` and
  `normalise:` say which tier matched, so a reader can tell a verbatim hit from a normalised
  one from a whitespace-insensitive one.

Exit codes: `0` found and written; `2` fetch/extract/usage error (no file written); `3`
written but the quote is absent from the extracted text; `4` written but HTTP ≠ 200. On 3 and
4 the file is still written — a failing capture is evidence too — and stderr says the capture
is not citable. `--pad` below the grammar's 400 minimum is refused.

## 2. Grammar written

```
# evidence <id> — claim C GATE (round 74)
url: ua: http: bytes: sha256: fetched: content-type: final-url: extract:
quote-found: yes|no   quote-words:   quote-chars:   quote-found-verbatim: yes|no
window: pad=400 before=<n> after=<n>
fetch: GET <url>          user-agent: <exact UA>     access-date: <local YYYY-MM-DD>
http-status: <status>     content-length: <n|->      transferred-bytes: <wire size>
fetch-attempts: <n>       fetch-command: <literal curl argv, body/header paths elided>
locator: <caller string>  normalise: <form>+whitespace-fold; matched=<tier>
quote: <quote on one line>
--- window ---
<extracted body text, >=400 chars each side of the quote, verbatim>
--- quote ---
<the quote as supplied>
```

`ua:`/`user-agent:` and `http:`/`http-status:` are deliberately duplicated: the round-73
parser keys `user-agent`, `http-status` and `quote` and takes the first occurrence of each
name, while claim C's new keys are the short spellings. `quote:` (one line) is kept beside the
`--- quote ---` block for the same reason. No key is a self-attestation: every value except
`locator` is derived from the one fetched body.

## 3. Selftest receipt

```
$ python3 -B .ufo/waves/round-74/counters/capture-evidence.py --selftest
SELFTEST OK: 14 scenarios
$ echo $?
0
```

Fixtures are built in a `tempfile.mkdtemp()` directory and removed afterwards; nothing in the
lane is touched. Scenarios, each asserting on the written file's parsed fields:

| scenario | what it pins |
|---|---|
| `file-cjk` | `file://` capture of a CJK fixture: exit 0, `quote-found`/`quote-found-verbatim` yes, `before>=400 and after>=400`, the quote inside `--- window ---`, `--- quote ---` equal to the quote, every round-74 key and every round-73 key present, 64-hex sha256, `quote-chars` == character count |
| `nfkc-fold` | body `ＡＢＣ１２３`, quote `ABC123`: found yes, verbatim **no** (NFKC tier only) |
| `whitespace-collapse` | Latin sentence broken by a newline and a doubled space: found yes, verbatim no, `matched=folded` |
| `cjk-linebreak` | CJK run broken by a source newline: found yes, verbatim no, `matched=folded-no-space`, window still holds the surrounding text |
| `quote-missing` | absent quote: file written, `quote-found: no`, empty window block, quote block intact, exit 3, stderr "not citable" |
| `extract-visible` | `script`/`style`/comment text absent from the output, `<head>` title absent, `&amp;`→`&`, `&lt;tag&gt;`→`<tag>` |
| `window-edge` | quote at the very start of the text: `before=0` recorded honestly, `after>=400`, exit 0 |
| `http-fetch` | `http.server` fixture: status 200, the server received exactly the browser UA, `bytes`/`sha256` equal the served body, `fetch: GET <url>`, `content-length` recorded, `fetch-attempts: 1` |
| `fetch-retry` | a body shorter than its Content-Length (curl exit 18) on the first request: exit 0, `fetch-attempts: 2` |
| `fetch-retry-gives-up` | retries exhausted: exit 2, no file written, stderr names `curl exit 18 after 2 attempt(s)` |
| `http-not-200` | 404 page: file written, `http: 404`, exit 4, "not citable" |
| `pdf-extract` | a hand-built one-page PDF (xref offsets computed) through `pdftotext`: quote found, `extract:` names pdftotext (skips cleanly if pdftotext is absent) |
| `charset-gb18030` | GB18030 bytes declared only in `<meta charset="gb18030">`: detected, Chinese quote found verbatim, window holds it |
| `guards` | `--pad 40` refused (no file); an all-whitespace quote refused with exit 2 (no file) |

## 4. Dry run — the four candidate pages (placeholders only, `/tmp/ExecEvidence/evidence/`)

Each quote below is a <=25-token string the wave-1 scouts verified on its page; they are
**placeholders for a dry run**, not Gate selections. `--id` is the seat's own label, not a
lane id.

| id | page | http | bytes | sha256 | quote-found / verbatim | window: quote at / after | quote chars (`wc -w -m`) |
|---|---|---|---|---|---|---|---|
| `litmemo` | `https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 101615 | `441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64` | yes / yes | 400 / 400 | 43, 1 token |
| `tuduku` | `https://tuduku.space/column/novel-worldbuilding` | 200 | 17068 | `754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7` | yes / yes | 400 / 400 | 33, 1 token |
| `cw2025` | `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | 200 | 48536 | `a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d` | yes / yes | 400 / 400 | 32, 1 token |
| `cw2022` | `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | 200 | 62604 | `344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659` | yes / yes | 400 / 400 | 27, 1 token |

The four sha256 digests and byte counts are **identical to the wave-1 scouts' captures**
(`ScoutLitmemo.md` §1, `ScoutTuduku.md` §1, `ScoutChinawriter2025.md` §1,
`ScoutChinawriter2022.md` §1), which were taken without `--compressed`: the tool records the
decompressed body, so its digests are comparable with earlier rounds' evidence. Window
geometry from the written files: 843/833/832/827 characters total, quote at offset 400 in
each, 400 characters after.

Quotes used (all CJK, all verbatim in the extracted text):

- litmemo — `自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。`
- tuduku — `勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか`
- cw2025 — `整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。`
- cw2022 — `把它放在前面大概20章之内慢慢来，我觉得是问题不大的。`

Provenance of the four files, stated exactly: all four were produced by the final build
`4e06fb52aab070139bdebad26a5a27313a59c9fb0942b88c413731c96b8f4f55` — `litmemo` fetched
00:44:17Z, `cw2025` 00:44:59Z, `cw2022` 00:45:00Z, `tuduku` 00:47:32Z with
`fetch-attempts: 4` (three TLS resets before it, see §7). An earlier build one edit behind
(docstring wording and one unused import only) produced byte-identical captures; the stored
files are the final build's.

## 5. Compatibility receipts (both run against the dry-run files as written)

**5a — the round-73 EVIDENCE leg, lifted not re-typed.** `/tmp/ExecEvidence/compat-check.py`
pulls `_evidence` and `_wsnorm` out of the committed
`reports/round-73/accept-c.py` with `ast`, so the check reads round 73's own code, and runs
the leg's checks line for line (`access-date == 2026-10-25`, `http-status == 200`, 64-hex
sha256, UA startswith `Mozilla/5.0`, `quote-found-verbatim == yes`, quote non-empty and
<=25 tokens, quote in the r73 window view) plus claim C's new rule (quote inside
`--- window ---`, `pad>=400 before>=400 after>=400`):

```
cw2022   OK
cw2025   OK
litmemo  OK
tuduku   OK
RESULT: 0 file(s) bad
```

**5b — the landed round-74 counter's own parser.** `.ufo/waves/round-74/counters/accept-c.py`
was written by a sibling seat while this tool was being built; it sets
`EVIDENCE_DIR = "reports/round-74/evidence"` and reads `_window(text)` between
`--- window ---` and `--- quote ---` with `nfkc_ws` containment. `/tmp/ExecEvidence/compat-check-74.py`
lifts `_evidence`, `_window` and `nfkc_ws` from that file and runs the leg's checks over the
four captures:

```
cw2022   OK
cw2025   OK
litmemo  OK
tuduku   OK
RESULT: 0 bad
```

(`neg1`/`neg2` report "missing" there only because that harness lists every `q-*.txt` and
those two are control quotes whose captures live in `/tmp/ExecEvidence/controls/`, not
`evidence/`.) The tool therefore emits a superset of what the landed counter parses; its
extra keys are `transferred-bytes` and `fetch-attempts`.

## 6. Live falsifier controls — the tool separates a page from another page's quote

The round-68/71 REFUSED of staged S899/S900 was a URL↔quote mispairing, so the tool must be
able to say "this quote is not on this page" on a live page rather than merely print `yes`:

| control | URL | quote | result |
|---|---|---|---|
| `neg1` | chinawriter **2025** page | the 2022 page's answer span `这个我肯定考虑过。我自己就是资深读者，…` (register S816's span) | `quote-found: no`, exit 3, window empty |
| `neg2` | litmemo | the staged S883 anchor string `小説の世界観はどう作る？` | `quote-found: no`, exit 3 |
| `pos1` | chinawriter **2022** page | the same S816 span | `quote-found: yes` verbatim, exit 0 |

That reproduces the mispairing as a mechanical detection: the span is absent from the 2025
page and present on the 2022 page, which is exactly what rounds 68/71 needed and did not
have a tool for.

## 7. Environment findings a Gate seat should know

- **tuduku.space is intermittently hostile at the transport layer** (measured 2026-10-25/26):
  `Recv failure: Connection reset by peer` (curl 56) and `OpenSSL SSL_read: unexpected eof`
  (curl 55) on a plain browser-UA GET, while an immediate retry usually succeeds. Measured
  attempts on that one page: 1, then 4 (a 145 s run with three reset attempts before the
  fourth returned 200). `--retries` exists for that reason and `fetch-attempts:` records what
  it took. The page itself served HTTP 200 with a stable body (`754f504c…` on every
  successful attempt today, including the wave-1 scout's).
- **`--compressed` changes the wire, not the evidence.** litmemo serves gzip (31737 wire vs
  101615 body bytes), chinawriter serves `Transfer-Encoding: chunked` + gzip (21341/16723
  wire), and in those cases the response carries **no** `Content-Length` — the header line
  reads `-`. `bytes:`/`sha256:` are always the decompressed body and match the earlier
  uncompressed captures, so the recorded `transferred-bytes:` is the only line that moves.
- **`%{size_download}` is the wire size**, not the body size — 6260 for a 17068-byte tuduku
  body. A tool that recorded curl's own counter as "bytes" would record the wrong number;
  this one measures the saved body.
- All four pages answered 200 to the browser UA with no challenge wall; no Wayback fallback
  was needed, and no captcha or challenge was touched.

## 8. Limits, stated

- The window is **extracted visible text**, not raw HTML, and `<head>` is dropped: a string
  that exists only in `<title>` or a meta tag is not findable unless the page repeats it in
  the body. All four candidate pages repeat their headline in `<body>` (litmemo `h1`,
  tuduku `h1`, chinawriter `#newstit`), so any body or headline quote is capturable.
- A window is ~830 characters, so an evidence file proves the quote's neighbourhood, not the
  whole body; a counter cannot re-verify a different quote from the same file.
- A body line beginning with `--- ` inside a window would truncate a naive block parse. The
  extracted text of all four candidate pages has zero such lines (checked), and the landed
  counter's `_window` regex (`^-{2,}\s*window`) is unaffected by ordinary dashes.
- Per-character NFKC differs from whole-string NFKC only where composition crosses a
  character boundary; the NFKD retry covers decomposed bodies, and `quote-found-verbatim`
  plus the landed counter's whole-string `nfkc_ws` containment are what actually bind a Gate
  quote. No candidate page uses combining sequences.
- `access-date:` is the machine's **local** date. A capture run after local midnight carries
  the new date and will fail a Gate whose `access_date` is 2026-10-25 — correct behaviour,
  but a seat re-running late should read the line before assuming the Gate is wrong.
- The tool proves what one fetch returned at one instant. It cannot prove the page was the
  same when the staged package was read, and it does not (and must not) substitute a Wayback
  capture: that is a Gate seat's documented decision.

## 9. Not done, by intent or by blocker

- No evidence file was written into `reports/round-74/evidence/`: the seat item scopes this
  tool to a dry run outside the lane. The Gate seats own the real `<id>.txt` files.
- The landed counter's full EVIDENCE leg was **not** run end to end (it needs a lands tree
  carrying the Gate rows and the four registry rows, which do not exist yet); only its
  evidence helpers were exercised, per §5b.
- No live PDF capture: the `pdftotext` path is fixture-tested only (the S877-class PDF is not
  one of this round's four pages).
- No tool installed, nothing upgraded, `pacman` not invoked. Nothing written under
  `/home/vgpnk/Projects/shokunin/**`, `shokuknow`, or any sibling lane.

## Post-wave update

Follow-up from the L1: the grammar was extended to the **frozen** claim-C EVIDENCE leg and the
five real captures were run into the lane. Where this section and §1-§9 differ, this section
wins. Tool now `sha256 bf1908f93e6cc30f8888734a94eb68480216da2e1767884e6945a2b810b2d07c`,
1279 lines, 57354 B, mode 755, same path.

### Grammar delta

New keys, all derived from the fetched body and the stored window: `window-sha256:` (sha256 of
the stored window text), `window-bytes:` (its byte length), `window-rule:` (the rule restated
inside the file). `window:` now reads `chars=<n> min=<n> pad=<n> before=<n> after=<n>`.
The `--- window ---` block is **one whitespace-collapsed line of at least 4096 characters**
(`--min-window`, default and floor 4096); the block is written as a single line so "the window
text, exactly as stored between the markers" is unambiguous — the lines between the two marker
lines, joined by newlines, no trailing newline, UTF-8. The word "verbatim" in the earlier
sections is superseded by "whitespace-collapsed": the stored window is the extracted visible
text with every whitespace run folded to one space (the claim's own wording).

New behaviour:

- **Self-verification after every write.** The tool re-reads its own file, extracts the window
  exactly as stored, recomputes sha256 and byte length, compares them with the header, requires
  one stored line of >= `--min-window`, and checks the quote in the window after *whole-string*
  NFKC + whitespace folding — the fold the counter uses, not the tool's own tiered matcher. Any
  failure prints `VERIFY FAIL` and exits **5** (the file stays on disk).
- **`--verify PATH`** re-runs that check on any evidence file later, no refetch: it re-checks the
  required keys, `http-status: 200`, `access-date: 2026-10-25`, the window digest and length, and
  quote-in-window. `--allow-file` relaxes only the status check and is for fixtures; a graded
  capture carries `http-status: 200` (verified: a `file://` capture without it exits 5).
- **PDF without `-layout`**, as instructed: `pdftotext -enc UTF-8 BODY -`; the `extract:` line
  names it, and the selftest asserts `-layout` is absent.
- Exit codes now: 0 verified, 2 fetch/extract/usage (no file), 3 quote absent, 4 HTTP != 200,
  5 verification failed.

Selftest receipt (16 scenarios, fixtures in `tempfile.mkdtemp`, removed after):

```
$ python3 -B .ufo/waves/round-74/counters/capture-evidence.py --selftest
SELFTEST OK: 16 scenarios
$ echo $?
0
```

Scenarios: `file-cjk-window` (full grammar, >=4096-char single-line window, digest recomputes,
quote in window after the counter's fold), `nfkc-fold`, `whitespace-collapse`,
`cjk-linebreak-refused`, `quote-missing`, `extract-visible`, `window-edge` (quote at text start,
`before=0`, window still 4098), `window-short` (short document -> exit 5), `http-fetch`,
`fetch-retry`, `fetch-retry-gives-up`, `http-not-200`, `pdf-extract` (96-line PDF, xref offsets
computed, pdftotext without `-layout`), `charset-gb18030`, `verify-mode` (good file passes; a
4-character window edit and a forged `window-sha256` both exit 5), `guards` (`--min-window 100`
and `--pad 40` refused, empty quote refused).

`cjk-linebreak-refused` is a deliberate negative: a Japanese/Chinese sentence broken by a source
line break, quoted without that space, is *found* by the tool's whitespace-free tier and the file
is written, but the counter's whole-string fold would not confirm it, so verification fails with
exit 5. Such a span must be re-quoted, never hand-edited into the evidence.

### The five captures (written into `reports/round-74/evidence/`)

Every row: browser-shaped UA, `http: 200`, ordinary fetch, `access-date: 2026-10-25`,
`pdftotext` without `-layout` for the PDF. `file` column = sha256 of the evidence file itself.

| id | URL | http | body bytes | body sha256 | file sha256 | quote-found-verbatim | window chars | window-sha256 | verify |
|---|---|---|---|---|---|---|---|---|---|
| S877 | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1055723 | `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9` | `29abd3c3de64e17f871faf3da3547384f917dc8833e049d5ee36ef551e9fbe02` | no (matched `folded`: the sentence is split by source line breaks) | 4098 | `0e006bfa636bca8f88d75bb0af28a4e2ccc6c421b1956160208fd31ac55f23a9` | OK |
| S881 | `https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 101615 | `441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64` | `94bdcad2313e15bbb2bde6886236872ae8d149b1de1d9ce0ce56ae9b02ce6dd9` | yes | 4098 | `83e313a946d1cbec38285d3712481c8e4ed864310b350659cd080eeffee28809` | OK |
| S882 | `https://tuduku.space/column/novel-worldbuilding` | 200 | 17068 | `754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7` | `21c4f2bcd717660db3f90f3c509bc5b16aecebb1191709891990aeaa249ed10c` | yes | **2953** | `a055a24ce2ced7714cea69b342cd2f40c09d85d14c985c3ddc30c1a74d82289f` | **FAIL (window < 4096)** |
| S883 | `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | 200 | 48536 | `a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d` | `e5cf328413bb9c8407f2c8ae592ec2af7489d7902e28f2f9a3016a24ddda2a4e` | yes | 4104 | `b38075d366952043671669222caa4673a6b8a93b072ea24de8633e09ab456c18` | OK |
| S884 | `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | 200 | 62604 | `344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659` | `3b9b8513cc7aa23d9f4edebb889b4bcdd2192e8be1d55bb03f672b8d3884ddb2` | yes | 4103 | `1618972ce51e2323740ebb609b2cf2af28b6368566948bfe63c832f175c0cf81` | OK |

All five bodies hash to the same digests as the wave-1 scouts' captures. Quotes are exactly the
five strings supplied by the L1, unaltered; the S877 string is recorded **without** the quoting
guillemets `«»` that wrapped it in the instruction (they are not page bytes, and the sentence is
contiguous on the page without them).

Re-verification, run over the landed files exactly as stored:

```
$ for id in S877 S881 S882 S883 S884; do python3 -B .../capture-evidence.py --verify reports/round-74/evidence/$id.txt; done
VERIFY OK: .../S877.txt window-sha256=0e006bfa... window-bytes=7558 window-chars=4098 quote-in-window=yes access-date=2026-10-25 http-status=200
VERIFY OK: .../S881.txt window-sha256=83e313a9... window-bytes=11709 window-chars=4098 quote-in-window=yes ...
VERIFY reports/round-74/evidence/S882.txt: window is 2953 characters (want >= 4096)
VERIFY FAIL: reports/round-74/evidence/S882.txt (1 problem(s))
VERIFY OK: .../S883.txt window-sha256=b38075d3... window-bytes=12184 window-chars=4104 quote-in-window=yes ...
VERIFY OK: .../S884.txt window-sha256=1618972c... window-bytes=12226 window-chars=4103 quote-in-window=yes ...
```

Independent receipt against the landed counter's own code (`/tmp/ExecEvidence/final-leg-check.py`
lifts `_evidence`, `_window`, `nfkc_ws` by AST from `.ufo/waves/round-74/counters/accept-c.py`
and applies the frozen rule: status, access date, 64-hex body sha256, browser UA, fetch line,
window >= 4096, `window-sha256` recomputed from `_window`, quote in window after `nfkc_ws`):

```
S877   OK  window=4098 window-sha256=0e006bfa636bca8f quote=108ch/15tok
S881   OK  window=4098 window-sha256=83e313a946d1cbec quote=43ch/1tok
S882   FAIL window=2953 window-sha256=a055a24ce2ced771 quote=33ch/1tok  -> window 2953 chars (<4096)
S883   OK  window=4104 window-sha256=b38075d366952043 quote=32ch/1tok
S884   OK  window=4103 window-sha256=1618972ce51e2323 quote=27ch/1tok
RESULT: 1 of 5 rows fail the final rule
```

### Two blockers the L1 must rule on (not mine to fix)

1. **S882 cannot satisfy `>= 4096` characters — the page is shorter than the window.** The served
   document is 17068 bytes and its entire visible text is **2953 characters**; the absolute
   ceiling, counting *every* text node including `<title>` and concatenating without collapse, is
   **3022**. Measured, not inferred:

   ```
   $ curl -A "<browser UA>" -o tuduku.html https://tuduku.space/column/novel-worldbuilding
   $ sha256sum tuduku.html   -> 754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7
   ceiling (all text nodes incl. head/title, collapsed): 3022
   ceiling (body only, collapsed): 2976
   $ curl ... https://tuduku.space/column/novel-worldbuilding.html  -> same sha256 (754f504c…)
   ```

   The tool stored the whole document as the window (no padding, no invented text): `window:
   chars=2953 min=4096 before=631 after=2289`, and `window-sha256`/`window-bytes` are correct for
   that text. The file is left on disk because it is the honest capture; it will fail the frozen
   EVIDENCE leg until either the leg's minimum is amended below ~2950, the row's source is
   replaced with a longer document, or S882 is dropped. No quote was altered and no text was
   fabricated.

2. **The S877 quote exceeds the frozen GATE leg's 80-character cap.** That leg allows "at most 25
   whitespace tokens and at most 80 characters"; the instructed sentence is **108 characters**
   (15 tokens), so a Gate row carrying it fails GATE. Measured contiguous substrings that are in
   the stored window and inside both caps, for the L1 to choose (nothing was changed):

   | candidate | characters | tokens | in stored window |
   |---|---|---|---|
   | `Язык – главный инструмент построения вымышленных миров` | 54 | 7 | yes |
   | `дающий названия для их природных и социальных реалий` | 52 | 8 | yes |
   | `Язык – главный инструмент построения вымышленных миров, дающий названия` | 71 | 9 | yes |
   | the instructed sentence (as captured) | 108 | 15 | yes (over the cap) |

   If a shorter span is adopted, only the Gate cell and the anchor cell need it; the evidence
   window already contains all of the above, so no re-capture is required.

### Honesty for this update

- Exercised: the 16-scenario selftest (exit 0), the five live captures (ordinary fetch, browser
  UA, no challenge wall, no Wayback substitution), `--verify` on all five, and the independent
  final-leg receipt above. `fetch-attempts: 1` on every one of the five.
- Not exercised: the landed counter's EVIDENCE leg end to end (still needs a lands tree with the
  Gate rows and the registry rows), a live PDF whose quote needs the NFKD tier, and a real capture
  with a gzip-negotiated `Content-Length` (the four HTML pages here serve chunked/gzip, so
  `content-length:` is `-` and `transferred-bytes:` carries the wire size, as documented).
- Writes: the tool, the five files above, and this report. `/tmp/ExecEvidence/**` holds the
  scratch (quote files `q-S87*/q-S88*.txt`, the compat and final-leg harnesses, the PDF probe).
  No tool installed, `pacman` not invoked, no sibling lane or fleet path touched.

## Post-wave update 2

Both L1 rulings applied; the five files were re-captured and re-verified. Tool now
`sha256 e510a40a67e8e483a259dc280c2c3225d7f7a1ea77ad648185efc4c65d919e4b`, 1367 lines,
62084 B, mode 755, same path.

### Ruling 1 — S877's Gate quote

The capture was re-run with `Язык – главный инструмент построения вымышленных миров`
(54 characters, 7 tokens, p.7), the string the L1 adopted; the tool was given it, nothing was
edited by hand. Because the window is cut *around* the located span, shortening the quote moved
the window cut: `window-sha256` is now `f63d6485…` (it was `0e006bfa…` for the 108-character
span), `window-bytes: 7558`, `window: chars=4098 min=4096 pad=400 before=2019 after=2025`, all
consistent with the stored line. `quote-words: 7`, `quote-chars: 54`, and the quote is inside
both GATE caps (<=25 tokens, <=80 characters). `quote-found-verbatim: no` still, for the honest
reason: the PDF text has source line breaks inside the sentence, so the match is the `folded`
tier, and the counter's NFKC+whitespace fold confirms it (`quote-in-window=yes`).

### Ruling 2 — the amended window rule, implemented and guarded

Two new header keys, both written by the same run from the same extraction:

- `window-scope: excerpt | whole-document` (`none` only on a file whose quote was not found).
- `visible-chars:` — characters of the **whole** extracted visible text after whitespace
  collapsing, i.e. the length the window would have if it were the entire document.

`--verify` (and the post-write self-check) now enforce the amended leg exactly:

| scope | required |
|---|---|
| `excerpt` | `len(window) >= 4096` **and** `len(window) <= visible-chars` |
| `whole-document` | `len(window) == visible-chars` **and** `visible-chars < 4096` |
| either | one stored line; `window-sha256` recomputed from the stored text; `window-bytes`; `http-status: 200`; `access-date: 2026-10-25`; quote in the window after whole-string NFKC + whitespace folding |

The second half of the `whole-document` rule is the anti-shortcut clause: a page long enough to
be excerpted cannot claim `whole-document` and store a few characters. A declared
`whole-document` whose stored text is shorter than `visible-chars` fails too. Both are pinned by
`whole-document-guard` in the selftest (forged scope on a 9.8k-character text -> "whole-document
claimed"; truncated window -> "but visible-chars says").

Selftest receipt:

```
$ python3 -B .ufo/waves/round-74/counters/capture-evidence.py --selftest
SELFTEST OK: 17 scenarios
$ echo $?
0
```

The `window-short` scenario became `window-whole-document` (a short document is now a *valid*
capture: exit 0, `window-scope: whole-document`, `visible-chars` equal to the stored length,
digest recomputed), and `whole-document-guard` was added; every other scenario is unchanged.

### The five files after the rulings

`file` = sha256 of the evidence file itself. All five: HTTP 200, browser-shaped UA,
`access-date: 2026-10-25`, `fetch-attempts: 1`, self-verified on write and re-verified with
`--verify`.

| id | body bytes | body sha256 | file sha256 | file bytes | quote (chars/tokens) | verbatim | scope | window chars | visible-chars | window-sha256 | verify |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S877 | 1055723 | `e512a20d…ca595a9` | `165951614548401672378ff8b4696f83b7581b17ecf30922e8edfa3c93acdf26` | 9664 | 54 / 7 | no (folded) | excerpt | 4098 | 492810 | `f63d6485cfb7e55036c7f20db66d725a36fcd753e535ad51db7a0d1600570a27` | OK |
| S881 | 101615 | `441fc921…34ca64` | `f22e223e39ed7a5fb8049e8e467cbe4d1f57dd330db5a24881c125ffce78c145` | 13762 | 43 / 1 | yes | excerpt | 4098 | 9855 | `83e313a946d1cbec38285d3712481c8e4ed864310b350659cd080eeffee28809` | OK |
| S882 | 17068 | `754f504c…62cfc1b7` | `e6030849c25eabb7ee742ba4f100977d8b02599191d21cf4c440d4b58e9f7da7` | 10399 | 33 / 1 | yes | **whole-document** | 2953 | **2953** | `a055a24ce2ced7714cea69b342cd2f40c09d85d14c985c3ddc30c1a74d82289f` | OK |
| S883 | 48536 | `a3b6640c…bee94d` | `6013c8258e52c34cd622de5021cfbf76302bc9d607c01d459ad841385533aa9c` | 14238 | 32 / 1 | yes | excerpt | 4104 | 8162 | `b38075d366952043671669222caa4673a6b8a93b072ea24de8633e09ab456c18` | OK |
| S884 | 62604 | `344de345…bdd3d659` | `68bede11dc8d1be3856deb4b61a34fd0886fb6f139eb1128dba41dc812948029` | 14183 | 27 / 1 | yes | excerpt | 4103 | 12270 | `1618972ce51e2323740ebb609b2cf2af28b6368566948bfe63c832f175c0cf81` | OK |

S882's window text is byte-identical to the pre-ruling capture (same `window-sha256`), because the
whole-document window *is* the whole text; only the two new header lines were added. The four
`excerpt` files keep their earlier window digests (unchanged cuts), and their `visible-chars` are
the measured full-text lengths, all larger than the stored windows.

Independent receipt, `/tmp/ExecEvidence/final-leg-check.py` updated for the amended rule and run
against the landed counter's own `_evidence`/`_window`/`nfkc_ws` (lifted by AST):

```
S877   OK  window=4098/excerpt window-sha256=f63d6485cfb7e550 quote=54ch/7tok
S881   OK  window=4098/excerpt window-sha256=83e313a946d1cbec quote=43ch/1tok
S882   OK  window=2953/whole-document window-sha256=a055a24ce2ced771 quote=33ch/1tok
S883   OK  window=4104/excerpt window-sha256=b38075d366952043 quote=32ch/1tok
S884   OK  window=4103/excerpt window-sha256=1618972ce51e2323 quote=27ch/1tok
RESULT: 0 of 5 rows fail the final rule
```

Quote integrity re-checked after the re-captures: each file's `--- quote ---` block equals the
supplied string byte for byte; the S877 file carries the L1's adopted 54-character clause, the
other four their unchanged strings.

### Residual, stated

- The landed `accept-c.py` EVIDENCE leg still has no `window-scope`/`visible-chars` handling and
  no 4096 check; the frozen claims text now permits the whole-document form, so that counter
  needs the same two-key rule before it grades. I did not touch it (another seat's file): the
  rule it needs is the table above, and my harness shows the exact check.
- Not run: the full EVIDENCE leg end to end (still needs the Gate rows and registry rows at a
  lands tree). `visible-chars` is self-reported by the capturing run, as are `bytes`/`sha256`;
  an offline counter cannot re-derive any of them without refetching, which the leg's own text
  already concedes.
- No tool installed, `pacman` not invoked, no sibling lane, fleet path or `shokuknow` touched.
