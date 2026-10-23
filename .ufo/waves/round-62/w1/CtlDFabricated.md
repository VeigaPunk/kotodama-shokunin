# CtlDFabricated — Claim D pre-data fabricated-quote control (Round 62 wave 1)

## Result

**Fabricated quote on a real page: NONE-MET.** The frozen counter rejects it. The invented
16-word talaria sentence is absent from both the live on-topic page and that page's own Wayback
capture; the frozen `accept-d.py` scored `LOCATE FAIL` after all three passes and printed
`ACCEPT-D-62: FAIL` (exit 1). No counter change is needed for this control.

**Real live URL + capture of a DIFFERENT page carrying the quote: CONTROL-MET.** The frozen
counter **passes** this row (`ACCEPT-D-62: PASS`, exit 0). The row's live URL
(`https://www.theoi.com/Olympios/Hermes.html`) does **not** carry the quote; the quote is carried
only by the archive capture of an unrelated page
(`…/20260325014456id_/https://www.theoi.com/Olympios/HermesTreasures.html`). Every other leg —
SET, ONEID, NOMARK, OPEN, HEDGE, CAPTION, SOLE, ROWS, APPEND, LINK, COPY, ACCESS, LINT — passes,
because none of them relates the capture to the live URL. The smallest stopping change is a
structural ROWS check; measured below.

Axes: **depth** (does a fabricated or mis-sourced row survive the sourced-claim predicate?),
**calibration** (both directions: a true negative and a true positive on the same counter),
**operability/isolation** (bounded frozen-counter replay, byte-identical fixture inputs).
These are probe dimensions, not lane-axis admission judgments.

## Scope and detector

- Seat: `KotodamaR62.CtlDFabricated`; leaf, no delegation, no background jobs, no swarm.
- Isolated scratch root: `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlDFabricated`.
- Clone: `git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin …/clone && git -C …/clone
  checkout -q f0173481047a93c46798f90b68d71d4f169d2642`, with `GIT_DIR`, `GIT_WORK_TREE` and
  `GIT_INDEX_FILE` unset. `git cat-file -e d42ffb89^{commit}` → `BASE_OK` (the counter's
  `git show BASE:<path>` lookups work in the fixtures).
- Read first: `reports/round-62/claims.json` (claims, legs, `controls_required_before_data`),
  `corpus/lessons/round-61-verifier-spotcheck.md` section 7, `/home/vgpnk/.omp/agent/RULES.md`,
  `skill://godspeed`.
- Detector for every receipt: `timeout 900 python3 -B reports/round-62/accept-d.py`, run from the
  fixture root (the counter's default `--root .`). Every process was awaited; stdout and the exit
  code are pasted in full below. Full stdout, no truncation.
- Frozen counter SHA-256 in both fixtures and in the clone:
  `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` (unchanged in every run).
- Frozen base locator (`reports/round-61/reopen-quote.py`) SHA-256:
  `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390` (never edited).
- Two **labelled** PROBE copies of the counter were used and their diffs are shown below:
  `accept-d.PROBE.py` (PASSES 3→1, GAP 60→0; iteration only, no receipt taken from it),
  `accept-d.TIME.py` (adds a `[t+…s]` stamp to each leg line, predicate untouched) and
  `accept-d.PROBE-samepage.py` (one added ROWS check; used to measure the smallest counter change).
  All receipts below come from the **frozen, unmodified** `accept-d.py`.
- No lane source file was written. This report is the only lane write; every fixture byte lives
  under the isolated scratch root.
- Installs/updates: **none** (no pacman, no uv, no npm; the analysis used only `python3`,
  `curl`, `git`, `sha256sum`, all preinstalled).

## Fixture construction

Both fixtures are the clone at `f0173481…` with exactly two files changed: the footwear entry
(four lines) and `corpus/SOURCES.md` (one appended S693 row after the S692 row). The three
round-61 repairs (lines 63, 74, 75) are identical in both fixtures, so the only variable is the
new row's source cell, its quote, and line 93.

Shared repairs (both fixtures):

```text
63: - A sabot is a shoe hollowed out of one wooden block, worn by farmers and workers in the Netherlands, France, Belgium, etc. (S692)
74: - A heel was not a European invention but originated in Western Asia centuries ago for horseback riding, as a 17th-century Persian image caption records. (S665)
75: - The earliest evidence we have of someone wearing heels comes from a 10th-century Persian bowl. (S666)
```

`fxA` — fabricated quote on a real on-topic page plus **that page's own** capture. The quote is
16 words and names talaria, so SOLE, ROWS, LINK and COPY all pass and only LOCATE can catch it:

```text
| S693 | Hermes, Greek Mythology, Theoi Greek Mythology (author and date not shown) — https://www.theoi.com/Olympios/Hermes.html ; capture https://web.archive.org/web/20261008022232id_/https://www.theoi.com/Olympios/Hermes.html | docs | A | Hermes' winged boots in the Theoi Hermes overview |  WINGED BOOTS section, opening sentences: "Hermes was granted winged talaria by Zeus, sandals that carried him swiftly above the restless earth." | The Theoi overview presents Hermes' talaria as winged sandals that carried him above the restless earth. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

```text
93: - Hermes' talaria were winged sandals granted by Zeus that carried him swiftly above the restless earth. (S693)
```

`fxB` — same repairs; the live URL is real and on-topic but the capture is of a **different**
page that does carry the quote:

```text
| S693 | Hermes, Greek Mythology, Theoi Greek Mythology (author and date not shown) — https://www.theoi.com/Olympios/Hermes.html ; capture https://web.archive.org/web/20260325014456id_/https://www.theoi.com/Olympios/HermesTreasures.html | docs | A | Hermes' winged boots and the Greek and Roman names |  WINGED BOOTS & CAP OF HERMES section, first sentence: "Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria." | Theoi names Hermes' winged leather boots pteroeis pedila in Greek and talaria in Latin. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

```text
93: - Hermes' winged leather boots were called pteroeis pedila by the Greeks and talaria by the Romans. (S693)
```

Fixture hashes (before and after every detector run — unchanged):

```json
{
  "clone/pristine-entry": "eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72",
  "clone/pristine-sources": "eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2",
  "fxA/entry": "cdd5af4fdefae2c2d4d7885e194bf67b9c6b3881b9655510ed327e5b8318c037",
  "fxA/sources": "cbf77d99c72dfd4b08688c9ab05d3626a77102613ca505245ff76855fdb38608",
  "fxB/entry": "79732a186a8323a31ed36666e61318fb52577176e4aa0e43228455f7fd93d944",
  "fxB/sources": "ab4038b5e9ed4dd8cffb384b36288bb97b6578b00d489f74b3321c898a564f54"
}
```

## Independent verification that the fxA quote is fabricated (not a locator failure)

Both the live page and its own capture were downloaded independently (curl, HTTP 200) and searched
after tag-stripping, character-reference decoding and the locator's own NFKC/casefold
normalisation (`re.sub(r"[\W_]+", " ", …)`):

| file | normalised length | `talaria` | `granted` | `swiftly` | `restless` | `zeus` | invented quote present |
|---|---|---|---|---|---|---|---|
| `theoi_hermes.html` (live page, 200) | 34 850 | 0 | 1 | 0 | 0 | 30 | **False** |
| `cap_hermes.html` (capture `20261008022232id_`, 200) | 5 758 | 0 | 0 | 0 | 0 | 0 | **False** |

The live page mentions "winged" 7 times and "zeus" 30 times, so the miss is not a page-not-found
miss: the page is the right page and simply does not carry the invented sentence. The capture of
the same page likewise does not carry it.

For `fxB`, a direct per-URL locator probe (`reopen-quote.py`'s own `fetch`/`locate_in`, same
Firefox UA) shows which of the two URLs carries the quote:

```text
NOT_LOCATED https://www.theoi.com/Olympios/Hermes.html (0.1s)
LOCATED https://web.archive.org/web/20260325014456id_/https://www.theoi.com/Olympios/HermesTreasures.html (12.1s)
```

The live page of the `fxB` row has `talaria` 0 and `pteroeis` 0 in its normalised text; the quote
lives only on the other page's capture. `fxB` therefore asserts a quote its own cited live source
does not support.

## LOCATE verdicts and timings

The frozen leg retries up to three passes 60 s apart (so a failing row costs ≈120 s of sleeping
alone). Timings come from the labelled `accept-d.TIME.py` copy (predicate logic untouched; only a
timestamp is appended to each leg line):

| fixture | LOCATE verdict | LOCATE leg ended at | whole run | note |
|---|---|---|---|---|
| `fxA` | **FAIL** — `located=0 cited=1 (passes=3)` | t+175.3 s | 176.6 s | both URLs `quote-absent` |
| `fxB` | **PASS** — `located=1 cited=1` | t+103.0 s | 104.1 s | located via the mismatched capture |

The `fxB` pass is not instantaneous: the live URL was tried first and did not carry the quote, so
the leg spent one failed pass (including the archive's 429 retries) plus the frozen 60 s gap
before the second pass located the quote at the capture. In the frozen (uninstrumented) runs the
same two fixtures took 165 s (`fxA`) and 166 s (`fxB`) wall-clock.

## Environment hazard found while measuring (affects the real claim-D run)

`web.archive.org` intermittently answers the locator's own Firefox User-Agent with **HTTP 429**
(X-RL: 0, edge "Claro"), while a `curl/8.7.1` UA gets 200 for the same URL at the same moment.
Interleaved measurements, same URL, same instant, alternating UA:

```text
HermesTreasures.html firefox-UA ['429', '429', '429', '429']
HermesTreasures.html curl-UA    ['200', '200', '200', '200']
Hermes.html        firefox-UA ['429', '429', '200', '429']
Hermes.html        curl-UA    ['200', '200', '200', '200']
```

A second interleaved run on the `Hermes.html` capture: `firefox=200`, then `firefox=429`, then
`firefox=URLError`, with `curl=200` on all three rounds. The frozen locator retries 429 three
times per URL with 8 s waits, so it often recovers (this is why one `fxA` LOCATE run reports
`quote-absent` for the capture and another reports `HTTPError` for the same URL). Consequences
for the L1: an honest row whose quote is reachable **only** through a capture can fail LOCATE for
transport reasons, and a row's LOCATE verdict can differ between two runs of the same bytes. The
per-URL fetch with a plain curl UA is 200 in every measurement taken, so this is a UA-specific
throttle, not an archive outage.

## Labelled PROBE counters (diffs)

`accept-d.PROBE.py` (iteration only — no receipt taken from it; diff against the frozen file):

```diff
--- fxA/reports/round-62/accept-d.py
+++ fxA/reports/round-62/accept-d.PROBE.py
@@ -67,8 +67,8 @@
 PASSES = 3
-GAP = 60
+PASSES = 1
+GAP = 0
```

`accept-d.TIME.py` (timestamps only):

```diff
+import time as _t0mod
 def main():
+    global _T0
+    _T0=_t0mod.time()
@@
     def leg(name, ok, detail):
         legs.append(ok)
-        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
+        import time as _t
+        print(f"{name} {'PASS' if ok else 'FAIL'} {detail} [t+{_t.time()-_T0:.1f}s]")
```

`accept-d.PROBE-samepage.py` (the smallest stopping change; one added ROWS check):

```diff
+        if not live or not wb or min(wb) < min(live):
             bad.append(f"{sid}:urls")
+        else:
+            # PROBE (labelled): each capture must be a capture OF the row live URL
+            import urllib.parse as _up
+            def _orig(u):
+                m = re.search(r"web\.archive\.org/web/\d+(?:id_)?/(.+)$", u)
+                return _up.unquote(m.group(1)) if m else ""
+            live_set = {_up.unquote(urls[i]) for i in live}
+            for i in wb:
+                if _orig(urls[i]) not in live_set:
+                    bad.append(f"{sid}:capture-not-of-live-page")
```

## Why fxB passes the frozen counter

`accept-d.py` classifies the source cell's URLs with a bare substring test
(`re.search(r"web\.archive\.org/web/", u)`) and requires only that a non-archive URL exists and
that the first archive-looking URL comes after the first live URL. It never compares the capture's
embedded original URL with the live URL. `LOCATE` then hands the row's whole URL list to the
locator, which returns located as soon as **any one** of up to four URLs locates the quote. So a
row whose live page does not carry the quote is vouched for by an unrelated page's capture, and
`LINK`/`COPY` are satisfied against that quote. `fxB` is that row, and the frozen predicate passes
it.

Sibling overlap: seat `KotodamaR62.CtlDCaptureShapes` independently reports the same survivor
under the name `different-page` (capture embedding a different page than the live URL). This
seat's finding is the same defect seen from the quote-verification side, with the additional
measurement that the *live* page of the row carries none of the quoted words.

## Smallest counter change that stops fxB

Require, in the ROWS leg, that every listed capture be a capture **of** the row's live URL: parse
`web.archive.org/web/<timestamp>id_/<original>` and require the embedded original to equal one of
the row's live URLs (the labelled `accept-d.PROBE-samepage.py` above). Measured effect:

- on `fxB`: `ROWS FAIL … bad=['S693:capture-not-of-live-page']` → `ACCEPT-D-62: FAIL`, exit 1;
- on `fxA` (same-page capture, the honest shape): `ROWS PASS` — the check does not false-positive
  on a well-formed row.

The check is structural and needs no network request. An alternative, larger change would be to
require LOCATE to succeed **at the live URL** rather than at any URL in the cell; that would also
kill `fxB` but touches the network leg and the pass budget.

## Complete counter receipts

Each block is the entire stdout of the run plus its exit code. Stderr was empty.

### fxA — fabricated quote, frozen counter

Fixture root: `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlDFabricated/fxA`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:11Z not_located=['S693: https://www.theoi.com/Olympios/Hermes.html quote-absent; https://web.archive.org/web/20261008022232id_/https://www.theoi.com/Olympios/Hermes.html HTTPError (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
RECEIPT KotodamaR62.CtlDFabricated/fabricated-quote counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=LOCATE
```

Wall clock 165 s (frozen leg: three passes 60 s apart).

### fxB — real live URL + capture of a different page, frozen counter

Fixture root: `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlDFabricated/fxB`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:11Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT KotodamaR62.CtlDFabricated/live-real-capture-other-page counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Wall clock 166 s.

### fxA — labelled TIME copy (LOCATE timing)

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93] [t+0.1s]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693'] [t+0.1s]
NOMARK PASS marked=[] [t+0.1s]
OPEN PASS ids=['S692'] [t+0.1s]
HEDGE PASS ids=['S666'] [t+0.1s]
CAPTION PASS ids=['S665'] [t+0.1s]
SOLE PASS id=S693 tier=A [t+0.1s]
ROWS PASS cited=['S693'] registry=['S693'] bad=[] [t+0.1s]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693'] [t+0.1s]
LINK PASS bad=[] [t+0.1s]
COPY PASS bad=[] [t+0.1s]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:15Z not_located=['S693: https://www.theoi.com/Olympios/Hermes.html quote-absent; https://web.archive.org/web/20261008022232id_/https://www.theoi.com/Olympios/Hermes.html quote-absent (passes=3)'] [t+175.3s]
ACCESS PASS exit=0 [t+176.3s]
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s) [t+176.4s]
ACCEPT-D-62: FAIL
exit=1 elapsed=177s
```

This second `fxA` LOCATE run fetched the capture successfully and still reported `quote-absent` —
independent of the 429 flakiness, the invented quote is genuinely not on the page.

### fxB — labelled TIME copy (LOCATE timing)

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93] [t+0.1s]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693'] [t+0.1s]
NOMARK PASS marked=[] [t+0.1s]
OPEN PASS ids=['S692'] [t+0.1s]
HEDGE PASS ids=['S666'] [t+0.1s]
CAPTION PASS ids=['S665'] [t+0.1s]
SOLE PASS id=S693 tier=A [t+0.1s]
ROWS PASS cited=['S693'] registry=['S693'] bad=[] [t+0.1s]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693'] [t+0.1s]
LINK PASS bad=[] [t+0.1s]
COPY PASS bad=[] [t+0.1s]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:14Z not_located=[] [t+103.0s]
ACCESS PASS exit=0 [t+103.9s]
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s) [t+104.0s]
ACCEPT-D-62: PASS
exit=0 elapsed=104s
```

### fxB — labelled PROBE-samepage copy (measures the smallest stopping change)

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS FAIL cited=['S693'] registry=['S693'] bad=['S693:capture-not-of-live-page']
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:17Z not_located=['S693: https://www.theoi.com/Olympios/Hermes.html quote-absent; https://web.archive.org/web/20260325014456id_/https://www.theoi.com/Olympios/HermesTreasures.html HTTPError (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### fxA — labelled PROBE-samepage copy (no false positive on the honest same-page shape)

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:21Z not_located=['S693: https://www.theoi.com/Olympios/Hermes.html quote-absent; https://web.archive.org/web/20261008022232id_/https://www.theoi.com/Olympios/Hermes.html HTTPError (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1 elapsed=176s
```

### Iteration-only PROBE (PASSES=1, GAP=0) — no receipt taken from it

`fxA`:

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:05Z not_located=['S693: https://www.theoi.com/Olympios/Hermes.html quote-absent; https://web.archive.org/web/20261008022232id_/https://www.theoi.com/Olympios/Hermes.html HTTPError (passes=1)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

`fxB`:

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:05Z not_located=['S693: https://www.theoi.com/Olympios/Hermes.html quote-absent; https://web.archive.org/web/20260325014456id_/https://www.theoi.com/Olympios/HermesTreasures.html HTTPError (passes=1)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

Both PROBE rows above are reproduced here only to document the iteration; the receipts for the two
cases are the frozen-counter runs above.

## Per-item control verdicts

NONE-MET KotodamaR62.CtlDFabricated/fabricated-quote fixture=`/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlDFabricated/fxA`; Already stopped by LOCATE (the invented talaria sentence is absent from the live page and from that page's own capture — verified independently of the locator); no counter change needed.
CONTROL-MET KotodamaR62.CtlDFabricated/live-real-capture-other-page fixture=`/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlDFabricated/fxB`; Require each capture URL's embedded original URL to equal one of the row's live URLs (parse `web.archive.org/web/<ts>id_/<original>`), i.e. add the labelled `accept-d.PROBE-samepage.py` ROWS check — measured: ROWS FAIL on this fixture, ROWS still PASS on the honest same-page shape.

These are recommended predicate changes only; nothing in the frozen counter, the locator or the
lane was modified.

## Risks and blockers for the L1

1. **A capture of an unrelated page vouches for the row.** `fxB` passes the whole frozen
   predicate while the row's live URL carries none of the quoted words (`talaria` 0, `pteroeis` 0
   in its normalised text). Any new row should name the live URL of the page that actually carries
   the quote, with that same page's own capture; the proposed ROWS equality check makes the
   mismatch a hard FAIL.
2. **The archive throttles the locator's own User-Agent.** `web.archive.org` returns HTTP 429 to
   the Firefox UA (with `curl/8.7.1` returning 200 at the same instant, 4/4 each way in the
   interleaved measurements above). A row whose quote is reachable only through a capture can
   therefore fail LOCATE for transport reasons, and two runs of identical bytes can disagree.
   Mitigation for the lane: prefer a live URL that carries the quote outright (the frozen locator
   tries the live URL first — the live Theoi `HermesTreasures.html` page locates its talaria
   sentence directly, `LOCATED … exit=0`); keep the capture as the QUALITY-13 fallback, not as the
   primary evidence.
3. **The frozen predicate's repair legs are word-level.** OPEN/HEDGE/CAPTION are satisfied by
   regexes (`belgium,? (etc|…)`, `\bwe have\b`, `\bcaption\b`) and LINK/COPY compare normalised
   word bags. A repaired line that satisfies those patterns while misstating the source is not
   caught; only LOCATE and the review-only clauses can catch it. The `fxA`/`fxB` lines were
   written to satisfy every mechanical leg while the sourcing was wrong or unsupported — that is
   the point of the control.
4. Not a blocker, for the record: the claim's own new row should be checked with the frozen
   locator against **both** its live URL and its capture before landing, because the capture leg
   is the flaky one.

## Files changed

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-62/w1/CtlDFabricated.md` —
  this report (the only lane write).
- No lane source, counter, locator, registry or entry file was modified; `git status --porcelain`
  in the lane shows only the untracked `.ufo/waves/round-62/` report directory.
- All fixture bytes, probe counters, captures and probe scripts live under
  `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlDFabricated/` (`clone`, `fxA`, `fxB`,
  `mkfx.py`, `cap_*.html`, `theoi_hermes.html`, `brit.html`).
