# Round-75 claim-C counters

`capture-evidence.py` — the evidence-capture tool for claim C's EVIDENCE leg.
It fetches one URL with the recorded browser-shaped User-Agent, derives every
field of the evidence file from that one fetched body (fetch line, HTTP
status, byte count, sha256 of the body, the extracted visible text, the window
actually surrounding the located quote) and writes
`reports/round-75/evidence/<id>.txt`.

Provenance: the round-74 tool (`.ufo/waves/round-74/counters/capture-evidence.py`),
carried forward with this round's numbers — `ROUND = 75`, access date
`2026-10-27`, output directory `reports/round-75/evidence/`. The grammar, the
extraction, the folding tiers and the self-verification are unchanged, so one
grammar serves every round and a counter reads any round's evidence file the
same way.

## Use

```sh
# capture one page (writes reports/round-75/evidence/S885.txt)
python3 -B .ufo/waves/round-75/counters/capture-evidence.py \
    --id S885 \
    --url https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 \
    --quote "Introduction à l'analyse structurale des récits" \
    --out reports/round-75/evidence/S885.txt \
    --locator "page header, article title"

# re-check an evidence file without refetching
python3 -B .ufo/waves/round-75/counters/capture-evidence.py \
    --verify reports/round-75/evidence/S885.txt

# the fixture suite
python3 -B .ufo/waves/round-75/counters/capture-evidence.py --selftest
```

Dependencies: python3 stdlib, plus `curl` (http/https) and `pdftotext` (PDF
bodies). No third-party Python.

## Exit codes

| code | meaning |
|---|---|
| 0 | written and self-verified |
| 2 | fetch / extract / usage error — no file written |
| 3 | written, but the quote is not in the extracted text — not citable |
| 4 | written, but HTTP != 200 — not citable |
| 5 | written, but self-verification failed (window digest, window length, status, quote absent after NFKC+whitespace folding) |
| 6 | written, but the served body is a bot challenge or interstitial — the challenge was **met**, not passed, so the source is UNOPENED (QUALITY 10) |

A file is written on 3, 4, 5 and 6 on purpose: the failing capture is evidence
too.

## The window rule

The window is stored as ONE whitespace-collapsed line between the
`--- window ---` and `--- quote ---` markers, so "the window text" is
unambiguous.

- `window-scope: excerpt` — at least `--min-window` (4096) characters around
  the quote. The ordinary case.
- `window-scope: whole-document` — allowed only when the whole extracted
  visible text is shorter than 4096 characters; the stored window then IS that
  whole text, so its length must equal the recorded `visible-chars:`. A short
  window under a long `visible-chars:`, or a whole-document claim for a text
  that could have been excerpted, is a verification failure.

`window-sha256:` is the sha256 of the stored window bytes as UTF-8,
`window-bytes:` their length. Both are recomputed from the stored bytes; no
flag in the file is trusted.

## `challenge:` and `challenge-detail:`

QUALITY 10 requires the evidence to say what the server actually served. A body
that IS an interstitial (a JS proof-of-work wall, a captcha page, a login or
consent wall, a geo wall) is a challenge that was met, not one that was
passed: the source is UNOPENED and the capture is not citable.

Detection is two-tiered, because a raw-HTML keyword is not the same as a wall.
Strong markers are checked in the raw bytes; soft markers (`captcha`, `login`,
`consent`, `geo`) are checked in the **visible** text and only when that text
is short. A real article page may carry a hidden download widget or a
"Se connecter" nav link — neither makes the page a wall, so a keyword in the
raw HTML of a page with substantial visible text is NOT a challenge.

## Fixtures

`fixtures/` holds the committed HTML the selftest runs on, so the selftest
executes against bytes a reader can read rather than a generator hidden in the
source:

| file | what it exercises |
|---|---|
| `r75-fixture.html` | CJK body, full-width Latin, entities, a quote broken by a source line break, script/style/comment noise |
| `r75-edge.html` | the quote at the very start of the text (window slides forward) |
| `r75-short.html` | a document shorter than 4096 characters → `whole-document` scope |
| `r75-challenge.html` | a JS challenge interstitial → `challenge: js-challenge`, exit 6 |

## Known limits

- The window is extracted visible text, not raw HTML, and `<head>` is dropped,
  so a string that exists only in `<title>`/meta is not findable unless the
  page repeats it in the body.
- A body line beginning with `--- ` inside a window would truncate a naive
  block parse; the window is stored as one line, so this cannot occur in a
  file this tool writes.
- A quote that matches only the whitespace-free tier (a Japanese or Chinese
  sentence broken by a source line break, written without that space) is
  *found* and the file is written, but verification fails (exit 5), because
  the counter's fold would not confirm it: re-quote such a span rather than
  editing the evidence.
