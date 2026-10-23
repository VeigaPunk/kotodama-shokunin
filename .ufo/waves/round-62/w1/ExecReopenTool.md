# ExecReopenTool — claim O build item (tools/reopen-row.py)

## Scope

BUILD item of wave 1, claim **O** (operability, capability acquisition): author the lane tool
`tools/reopen-row.py` to the contract written in the docstring of
`reports/round-62/accept-o.py` (sha256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`).

Per the seat brief the tool is **not** written into the lane; it is delivered at

    /fast/scratch/hyaku/kotodama-r62/ExecReopenTool/reopen-row.py
    sha256 1aeb175bce9203f8273ac6b1280f05642480df281e5dc9845c3280d0cd00797f   (817 lines)

for the L1 to copy into the lane as `tools/reopen-row.py`. Nothing else was written in
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` except this report; nothing in
`/home/vgpnk/Projects/shokunin`. No git/jj commands were run. No installs or updates were made
(no package was needed; the tool is stdlib-only Python 3).

**I did not run `reports/round-62/accept-o.py` against the tool.** The brief reserves that first
data run for the L1; the counter would also judge the very object this wave delivers. To validate
the tool without consuming that run, I wrote my own independent harness from the contract text
(`/fast/scratch/hyaku/kotodama-r62/ExecReopenTool/contract_probe.py`, sha256
`f22ce5e19c5f0fe7ec9d7ae6d6afb83514cf4516b84fef42310c136aab720a09`) — see *Independent contract
probe* below.

## Contract as implemented

Read from the counter's docstring; the tool's own module docstring restates it in its own words.

- **CLI**: `reopen-row.py [--registry PATH] [--passes N] [--gap SECONDS] [--allow-private] [--selftest] ID...`
  Default registry `corpus/SOURCES.md` relative to the working directory; default `--passes 3`,
  `--gap 60`.
- **Row reading**: a registry row is a line starting `| S`; split on `|` → cell 2 is the source
  cell, cell 6 the anchor cell. URLs are the http(s) URLs of the source cell in order, with
  trailing `.,;:'` and an unbalanced `)` trimmed. The quote is the first double-quoted span
  (straight or curly) of the anchor cell.
- **Text match**: NFKC → casefold → every run of non-word characters or `_` folded to one space;
  the quote's normalised words must occur as one contiguous whole-word run in the page's words.
- **HTML split**: BODY = text nodes outside script/style/noscript/template/figcaption and outside
  any element whose class or id contains `caption` (case-insensitive), descendants of caption
  elements included in that exclusion; CAPTION = figcaption and caption class/id text, plus the
  values of `alt`, `title`, `aria-label`, `content` and every `data-*` attribute. Script/style text
  is neither. A non-HTML body (text/plain, JSON) is BODY text whole.
- **Fetch**: GET, 30 s timeout. Transient = HTTP 429, any 5xx, timeout, connection error; retried
  up to 3 attempts per URL per pass, waiting `min(gap, 5)` s between attempts. Any other HTTP error
  ends that URL for the pass after one attempt. Without `--allow-private`, a URL whose host is or
  resolves to loopback/private/link-local/reserved/unspecified, or that does not resolve, is
  refused **without a request**.
- **Passes**: a pass tries the row's URLs in order and stops at the first BODY match. Pass verdict
  LOCATED > CAPTION_ONLY > ABSENT > REFUSED > UNREACHABLE; another pass runs after `gap` seconds
  only when the pass was not LOCATED and some URL ended on a transient result; the row verdict is
  the best pass verdict, ranked LOCATED > CAPTION_ONLY > ABSENT > UNREACHABLE > REFUSED.
- **Output**: one line per ID in argument order, `ROW <ID> <VERDICT> attempts=<n> url=<url or ->`
  (n = HTTP requests + connection attempts over all passes; url = the URL that gave the verdict's
  match), then `REOPEN: <k>/<m> located`. Exit 0 when every row is LOCATED, 1 otherwise, 2 on an
  input error with a `REOPEN_ERROR` line and no traceback.

Implementation notes where the contract left a choice, all covered by the probe:

- A row with no quoted span, a quote under 8 normalised words, or no URL yields `NO_QUOTE` with
  **zero** requests; an unknown ID yields `NO_ROW` with zero requests.
- The URL printed for a verdict is the URL that produced that verdict's match (the BODY-match URL
  for LOCATED, the CAPTION-match URL for CAPTION_ONLY); `-` when the verdict has no match.
- `REFUSED` requires that *every* URL of the row was refused; a row with one refused and one
  fetchable URL is not REFUSED.
- Host resolution is cached per host per run, so a refused host costs no request and no repeat
  lookup.

## Tool self-test (offline, `--selftest`)

The tool carries its own `--selftest` with a local `http.server` fixture server covering body,
plain text, split markup, three caption kinds (figcaption, attribute, caption class), script-only
text, absent, transient-then-200, dead-then-archive, 404, a closed port, no-quote, short-quote,
private-host refusal and five bad-input cases. Full output:

```text
-- selftest: verdicts --
ok   verdict S1: ('LOCATED', 'attempts=1')
ok   verdict S10: ('LOCATED', 'attempts=2')
ok   verdict S11: ('UNREACHABLE', 'attempts=1')
ok   verdict S12: ('UNREACHABLE', 'attempts=9')
ok   verdict S13: ('NO_QUOTE', 'attempts=0')
ok   verdict S14: ('NO_QUOTE', 'attempts=0')
ok   verdict S2: ('LOCATED', 'attempts=1')
ok   verdict S3: ('LOCATED', 'attempts=1')
ok   verdict S4: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S5: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S6: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S7: ('ABSENT', 'attempts=1')
ok   verdict S8: ('ABSENT', 'attempts=1')
ok   verdict S9: ('LOCATED', 'attempts=3')
ok   summary: True
ok   exit code: 1
ok   no row: ('NO_ROW', 'attempts=0')
-- selftest: retry bound --
ok   transient hits: 3
ok   transient verdict: ('LOCATED', 'attempts=3')
-- selftest: private refusal --
ok   refused verdict: True
ok   refused hits: 0
ok   refused exit: 1
-- selftest: bad inputs --
REOPEN_ERROR: no row ids given
ok   no ids exit: 2
REOPEN_ERROR: cannot read registry /tmp/reopen-row-selftest-s32i6m57/nope.md: [Errno 2] No such file or directory: '/tmp/reopen-row-selftest-s32i6m57/nope.md'
ok   missing registry exit: 2
REOPEN_ERROR: --passes must be an integer >= 1
ok   passes zero exit: 2
REOPEN_ERROR: --gap must be a number >= 0
ok   gap not a number exit: 2
REOPEN_ERROR: unknown option --nope
ok   unknown option exit: 2
REOPEN_ERROR: registry /tmp/reopen-row-selftest-s32i6m57/BAD.md is not valid UTF-8: 'utf-8' codec can't decode byte 0xff in position 7: invalid start byte
ok   bad utf-8 exit: 2
-- selftest: 28 checks, 0 failures --
exit=0
```

(`S12` is the closed-port row: 3 attempts × 3 passes = 9 attempts, UNREACHABLE, as the contract's
bounded retry requires.)

## Independent contract probe (my own harness, not the frozen counter)

`contract_probe.py` rebuilds the documented fixture classes on a local server with random ids,
paths, vocabulary and quotes, then checks verdict, attempt counts, per-path request counts,
argument order, exit codes, private refusal and input errors. It is independent of the frozen
counter file; it was written from the contract text. Full output:

```text
GEN: wrong=0 summary_ok=True exit=1
ORDER: ok
BOUND: bad=none
EXIT: exit=0 summary_ok=True
PRIV: exit=1 rows=[('S6421', 'REFUSED', 0, '-'), ('S7306', 'REFUSED', 0, '-'), ('S1990', 'REFUSED', 0, '-')] hits=[0, 0, 0]
DEFAULT: rows=[('S7516', 'UNREACHABLE', 9, '-')] wall=150.2s hits=9
ERR: bad=none
PROBE FAILURES: 0 []
exit=0
```

Mapping to the counter's legs: GEN (verdicts, attempts, summary, exit), ORDER, BOUND (per-path
request counts), EXIT, PRIV and ERR all pass on this build; DEFAULT reproduces the nine-request
bounded retry and a 150 s wall time inside the contract's 100–600 s window. A second probe run
against a handler with the counter's exact HTTP/1.0 semantics (404 with no `Content-Length`)
returned `ROW S1 LOCATED attempts=1`, exit 0, one server hit — the tool tolerates that response
shape.

Independence check on the counter's INDEP leg: the tool's text names none of `reports/`,
`accept-o`, `round-62` (each grep count is 0). The tool also imports only the standard library
(`ipaddress`, `os`, `re`, `socket`, `sys`, `time`, `unicodedata`, `urllib.*`, `html.parser`).

## Live run (review evidence only — not a leg, and not the claim's data run)

Read-only, no registry mutation, run against the lane registry exactly as briefed:

```text
$ python3 -B reopen-row.py --registry /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --passes 2 --gap 30 S665 S671
ROW S665 LOCATED attempts=1 url=https://batashoemuseum.ca/standing-tall/
ROW S671 LOCATED attempts=2 url=https://web.archive.org/web/20250612214229id_/https://americanindian.si.edu/collections-search/object/NMAI_26904
REOPEN: 2/2 located
exit=0
```

Two observations worth passing to the L1, both about the round-61 findings this tool was built to
make runnable:

- **S671** — the live URL `https://americanindian.si.edu/collections-search/object/NMAI_26904`
  answers **HTTP 403** to an ordinary client (verified separately with curl: `live=403`), so the
  row's archived copy is what carries the quote. The tool's fallback reached the quote on the
  second attempt via the row's `; capture <wayback id_ URL>` — i.e. the archived-copy fallback
  works, and the row's live URL alone is not sufficient. This is the round-61 transient/miss
  territory (spot-check section 7, item 5).
- **S665** — the quote is present **twice** on the live page, and the tool reports LOCATED because
  of one occurrence while the other is caption material. Verbatim: the same sentence appears in a
  `data-img-description` attribute and in a `<p class="thumbnail-description">` element, both
  inside `<div class="thumbnail gallery-thumbnail clearfix row no-gutters">`. The
  `<p class="thumbnail-description">` is body text (the class contains no `caption` substring), so
  the contract's BODY/CAPTION split correctly classifies it as body. The sibling
  `<p class="thumbnail-caption">` element is empty. The round-61 note "S665's quote is a caption"
  is therefore **only true of the attribute occurrence**; the page also carries it in body text.
  Reviewing this by hand, the round-61 CAPTION defect on line 74 looks narrower than recorded —
  the L1 may want to re-read that routing item against this evidence before the D lines are
  reworded. This is a review observation, not a leg result, and I changed nothing.

## Risks and blockers

- **The claim's own data run is untouched.** `reports/round-62/accept-o.py` has not been executed
  against this tool; the L1 owns that run and its `ACCEPT-O-62: PASS|FAIL` line. My evidence for
  the legs is the independent probe above, not the frozen counter.
- **DEFAULT leg timing is sensitive to the contract's literal reading.** The nine-request bound
  requires 3 passes × 3 attempts with two 60 s gaps (150 s here). Any implementation that waits
  `gap` instead of `min(gap, 5)` between *attempts* would take ~3 min and could drift past the
  600 s ceiling; the tool uses `min(gap, 5)` between attempts and `gap` between passes, as written.
- **Live verdict of S671 depends on the live URL's 403**, which may be UA- or rate-dependent. The
  archived-copy fallback is what makes the row re-openable; a future live leg that only tries the
  live URL would be measuring the site's access policy, not the row's truth.
- **HTML splitting is heuristic by nature.** Class/id `caption` detection and the
  `noscript`/`template` exclusions follow the contract wording; a page that hides its caption in
  an unusual container could report CAPTION_ONLY where a reader would call it body text.
- **Not done, out of my seat's scope**: the tool is not yet in the lane (`tools/reopen-row.py`
  does not exist at `f0173481`), so the counter's TOOL leg cannot pass until the L1 copies it in.
- **No installs or updates** were performed; nothing was recorded for the tooling directive.

## Files changed

- `/fast/scratch/hyaku/kotodama-r62/ExecReopenTool/reopen-row.py` (new — the deliverable, to be
  copied by the L1 to `tools/reopen-row.py`)
- `/fast/scratch/hyaku/kotodama-r62/ExecReopenTool/contract_probe.py` (new — my independent
  validation harness)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-62/w1/ExecReopenTool.md`
  (new — this report; the only write in the lane)
