# CtlDCaptureShapes — Claim D pre-data capture-shape control

## Result

**CONTROL-MET.** Three malformed capture shapes passed both ROWS and the entire frozen ACCEPT-D-62 predicate: a different-page capture, the bare Wayback `/web/` URL, and a capture dated in 2099. Four mutants were killed (the three other requested shapes plus a title-placement variant). No mutant was inconclusive: the calibrated pristine fixture and every exact fixture restoration passed all legs.

Axes: **depth** (QUALITY 13 same-page archived-copy semantics), **calibration** (positive baseline and honest false-positive receipts), **operability/isolation** (bounded frozen-counter replay and exact-byte restoration). These are probe dimensions, not lane-axis admission judgments.

## Scope and detector

- Seat: `KotodamaR62.CtlDCaptureShapes`; leaf, no delegation, no background jobs.
- Isolated scratch root: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes`.
- Clone made from the lane and checked out at `f0173481047a93c46798f90b68d71d4f169d2642`, with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset.
- Read first: `reports/round-62/claims.json`, round-61 verifier spot-check section 7, operator rules, Godspeed skill; also read the applicable Shokunin skill and axes.
- Detector command for every receipt below, from the isolated clone: `timeout 900 python3 -B reports/round-62/accept-d.py`; actual return codes are recorded. The harness awaited each process, killed the process group on timeout/error, and captured full stdout/stderr without filtering.
- Frozen counter SHA-256: `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`.
- Base locator SHA-256: `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390`.
- Neither counter nor locator was edited. No PROBE counter, mocks, import hooks, hostname overrides, or changed retry constants were used.
- Only the new S693 source cell varied between mutants. The same four entry-line repairs, quote, tier, dates, metadata, and registry append position were held fixed. Every mutant was followed by byte-identical fixture restoration and another complete detector run.
- No lane source was written. This report is the sole lane write; all fixture evidence remains under the isolated scratch root.
- Installs/updates: **none**.

## Positive fixture and ordinary-source calibration

The S693 row is explicitly a CONTROL FIXTURE. Its B tier is a test input, not a proposed or admitted classification of Wikipedia. It is not a candidate row for integration.

Live page: [Talaria](https://en.wikipedia.org/wiki/Talaria). A registry search for that candidate live URL returned no matches before insertion. The 12-word lead-body quotation is:

> are winged sandals, a symbol of the Greek messenger god Hermes

Ordinary CDX query: [last five successful Talaria captures](https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTalaria&output=json&limit=-5&filter=statuscode%3A200). Returned timestamps: `20260525014053`, `20260623070127`, `20260717052712`, `20260817161110`, `20261011232751`. The last capture supplied the positive fixture shape. A direct archived re-open nevertheless returned HTTPError; no challenge was bypassed and no archived-copy availability is asserted. The positive predicate passed because the unchanged locator found the quote at the live URL first.

Locator command (from the clone), `timeout 300 python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Talaria "are winged sandals, a symbol of the Greek messenger god Hermes"`, full stdout and exit:

```text
LOCATED https://en.wikipedia.org/wiki/Talaria
exit=0
```

Archive calibration command used the same locator and quote with `https://web.archive.org/web/20261011232751id_/https://en.wikipedia.org/wiki/Talaria`, full stdout and exit:

```text
NOT_LOCATED https://web.archive.org/web/20261011232751id_/https://en.wikipedia.org/wiki/Talaria HTTPError
exit=1
```

Positive source row:

```text
| S693 | Talaria — Wikipedia, fixture accessed 2026-10-23 — https://en.wikipedia.org/wiki/Talaria ; capture https://web.archive.org/web/20261011232751id_/https://en.wikipedia.org/wiki/Talaria | docs | B | CONTROL FIXTURE: winged sandals of Hermes; tier is a test input, not an admitted classification | lead body paragraph: "are winged sandals, a symbol of the Greek messenger god Hermes" | Talaria are winged sandals associated with Hermes. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

Positive entry-line replacements:

```text
63: - A sabot is a hollowed wooden shoe, especially worn by farmers and workers in the Netherlands, France, Belgium, etc. (S692)
74: - The caption traces the heel to Western Asia, centuries ago, for horseback riding rather than Europe. (S665)
75: - The BBC reports the earliest evidence we have for wearing heels: a Persian bowl from the 10th century. (S666)
93: - Talaria are winged sandals that symbolize the Greek messenger god Hermes. (S693)
```

## Mutants and expected detector

Expected for each deliberately invalid capture shape: **ROWS FAIL**, with frozen predicate FAIL. Kill/survive is based on the passing calibrated fixture, never on the untouched, unrepaired checkout. All restored-fixture runs passed.

| Case | Mutation | ROWS | Frozen predicate / exit | Verdict |
|---|---|---|---|---|
| `no-capture` | No capture URL | FAIL | FAIL / 1 | killed |
| `capture-first` | Capture before live URL | FAIL | FAIL / 1 | killed |
| `only-wayback` | Only a Wayback URL | FAIL | FAIL / 1 | killed |
| `different-page` | Capture embeds /wiki/Hermes, live URL is /wiki/Talaria | PASS | PASS / 0 | survived |
| `bare-web-path` | Bare https://web.archive.org/web/ after the live URL | PASS | PASS / 0 | survived |
| `future-timestamp` | Capture timestamp 20990101000000 | PASS | PASS / 0 | survived |
| `title-only-archive` | Bare https://web.archive.org/web/ inside the title, before live URL | FAIL | FAIL / 1 | killed |

The title-placement case failed because the archive-looking URL occurs before the live URL. In contrast, exactly the same bare archive-looking URL placed after the live URL passed. This is an ordering check, not capture-syntax validation.

## Per-item control verdicts and smallest stopping changes

NONE-MET CtlDCaptureShapes/no-capture fixture=`/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/no-capture.fixture.json`; Already stopped by ROWS; no counter change needed.
NONE-MET CtlDCaptureShapes/capture-first fixture=`/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/capture-first.fixture.json`; Already stopped by ROWS ordering; no counter change needed.
NONE-MET CtlDCaptureShapes/only-wayback fixture=`/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/only-wayback.fixture.json`; Already stopped by ROWS for lacking a live URL; no counter change needed. LOCATE also failed after all three passes.
CONTROL-MET CtlDCaptureShapes/different-page fixture=`/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/different-page.fixture.json`; Extract the embedded original URL from a structurally valid capture and require equality with an earlier live URL.
CONTROL-MET CtlDCaptureShapes/bare-web-path fixture=`/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/bare-web-path.fixture.json`; Require a complete capture path with a 14-digit timestamp, id_ modifier and a nonempty embedded HTTP(S) original URL, rather than a substring.
CONTROL-MET CtlDCaptureShapes/future-timestamp fixture=`/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/future-timestamp.fixture.json`; Parse and validate the capture timestamp and reject timestamps later than the measurement UTC time.
NONE-MET CtlDCaptureShapes/title-only-archive fixture=`/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/title-only-archive.fixture.json`; Already stopped by ROWS ordering; this does not demonstrate capture-syntax validation.

These are recommended predicate changes only; none was implemented or measured. A combined minimal repair belongs at `accept-d.py` lines 213–224: replace the substring-only Wayback classification with structural capture parsing, compare its embedded original URL against an earlier live URL, and validate its timestamp. No network request is needed for these three shape checks.

## Why the survivors pass

`accept-d.py` currently derives `wb` only with `re.search(r"web\.archive\.org/web/", u)` and rejects URLs only when no live URL exists, no such substring exists, or the first archive-looking URL precedes the first live URL. It never checks the embedded page, a capture timestamp, or even the existence of a capture path after `/web/`. LOCATE can succeed at the first live URL without reading the listed capture. Therefore the successful LOCATE legs do not stop these ROWS false positives.

## Restoration evidence

- Original frozen-checkout hashes, measured before fixture construction and again after final cleanup:

```json
{
  "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
  "entry": "eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72",
  "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
  "sources": "eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2"
}
```

- Calibrated positive-fixture hashes:

```json
{
  "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
  "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
  "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
  "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
}
```

- All seven restored-positive fixture runs reproduce the pristine positive input hashes and PASS all legs: `True`.
- All detector runs leave their input hashes unchanged: `True`.
- Counter and locator remain at their frozen SHA-256 values in all sixteen runs: `True`.
- After removing S693 and restoring all four original entry lines, final original-byte hashes equal the pre-fixture values: `True`.
- The final original-byte detector run correctly fails because the original claim repairs are absent. It is restoration evidence only, not a failed calibration baseline and not evidence of killing any mutant.
- All subprocesses started by the detector harness completed and were awaited; no service or background job was started.

## Complete counter receipts

Each section includes the entire counter stdout and its exit code. Stderr was empty for every counter run. JSON fixtures record the complete S693 row, four relevant entry lines, and input hashes; stdout artifacts retain full output and the receipt. The final original-byte fixture has no S693 row.

### pristine-positive

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/pristine-positive.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/pristine-positive.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/pristine-positive counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### no-capture

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/no-capture.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/no-capture.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS FAIL cited=['S693'] registry=['S693'] bad=['S693:urls']
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
RECEIPT CtlDCaptureShapes/no-capture counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ROWS
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "e2bd4d74a9f823b0c96f2be664cb397969a32303598bd689e5db6796e21f35cd"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "e2bd4d74a9f823b0c96f2be664cb397969a32303598bd689e5db6796e21f35cd"
  }
}
```

### restored-no-capture

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-no-capture.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-no-capture.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/restored-no-capture counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### capture-first

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/capture-first.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/capture-first.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS FAIL cited=['S693'] registry=['S693'] bad=['S693:urls']
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
RECEIPT CtlDCaptureShapes/capture-first counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ROWS
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "0941c10373be2cbd88a637778e1d43fd950943d30d04cd0d35012e9090eecab2"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "0941c10373be2cbd88a637778e1d43fd950943d30d04cd0d35012e9090eecab2"
  }
}
```

### restored-capture-first

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-capture-first.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-capture-first.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/restored-capture-first counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### only-wayback

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/only-wayback.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/only-wayback.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS FAIL cited=['S693'] registry=['S693'] bad=['S693:urls']
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:03Z not_located=['S693: https://web.archive.org/web/20261011232751id_/https://en.wikipedia.org/wiki/Talaria HTTPError (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
RECEIPT CtlDCaptureShapes/only-wayback counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ROWS,LOCATE
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "ae863a2088895436a6f050b94053d854e81972e561ae457d43885e75286a5e03"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "ae863a2088895436a6f050b94053d854e81972e561ae457d43885e75286a5e03"
  }
}
```

### restored-only-wayback

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-only-wayback.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-only-wayback.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:03Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/restored-only-wayback counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### different-page

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/different-page.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/different-page.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/different-page counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "48e6af1b27a35155be46f05fd21b07378f9bcd67403b096187bca672b7634567"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "48e6af1b27a35155be46f05fd21b07378f9bcd67403b096187bca672b7634567"
  }
}
```

### restored-different-page

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-different-page.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-different-page.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/restored-different-page counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### bare-web-path

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/bare-web-path.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/bare-web-path.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/bare-web-path counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "79c3ac276d0d644b7d04c63e3204b522874614dd9f9d0b05954716dbc63042bf"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "79c3ac276d0d644b7d04c63e3204b522874614dd9f9d0b05954716dbc63042bf"
  }
}
```

### restored-bare-web-path

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-bare-web-path.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-bare-web-path.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/restored-bare-web-path counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### future-timestamp

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/future-timestamp.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/future-timestamp.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/future-timestamp counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "e3a3378432796350c5ef44eabb30ba6a1091d8f2f63ada616f53c8d52eef7236"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "e3a3378432796350c5ef44eabb30ba6a1091d8f2f63ada616f53c8d52eef7236"
  }
}
```

### restored-future-timestamp

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-future-timestamp.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-future-timestamp.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/restored-future-timestamp counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### title-only-archive

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/title-only-archive.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/title-only-archive.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS FAIL cited=['S693'] registry=['S693'] bad=['S693:urls']
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
RECEIPT CtlDCaptureShapes/title-only-archive counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ROWS
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "81ea564019139dfbdd49d22b04e89f2f53863106b180fbf418d9e27d9e40c352"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "81ea564019139dfbdd49d22b04e89f2f53863106b180fbf418d9e27d9e40c352"
  }
}
```

### restored-title-only-archive

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-title-only-archive.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/restored-title-only-archive.stdout.txt`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
RECEIPT CtlDCaptureShapes/restored-title-only-archive counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "e2d0095109d7d1d246b4c88731b31ed5fe32d8547893a110caee0026171ef600",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "916fce1299b4febb46fbd5649482a5cd2ecec029323dea4b82de2859609a9518"
  }
}
```

### final-frozen-bytes-restored

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/final-frozen-bytes-restored.fixture.json`.

Output: `/fast/scratch/hyaku/kotodama-r62/CtlDCaptureShapes/final-frozen-bytes-restored.stdout.txt`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:06Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
RECEIPT CtlDCaptureShapes/final-frozen-bytes-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

Before/after SHA-256:

```json
{
  "after": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2"
  },
  "before": {
    "counter": "3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4",
    "entry": "eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72",
    "locator": "39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390",
    "sources": "eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2"
  }
}
```

