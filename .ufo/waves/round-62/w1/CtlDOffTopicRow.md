# CtlDOffTopicRow — pre-data control for claim D, off-topic new-row leg

Seat: KotodamaR62.CtlDOffTopicRow (leaf executor). Scope: the "off-topic real row for line 93"
control of `reports/round-62/claims.json` `controls_required_before_data.D[5]`, against the frozen
counter `reports/round-62/accept-d.py`. Lane revision measured: `f0173481047a93c46798f90b68d71d4f169d2642`
(my clone at `/fast/scratch/hyaku/kotodama-r62/CtlDOffTopicRow/clone`).

**Verdict: CONTROL-MET — the frozen counter accepts an off-topic but real, located, tier-B row for
line 93.** `ACCEPT-D-62: PASS`, exit 0, with S693's quote naming `Hermes` in the sense "a proposed
French crewed spaceplane" and its body text carrying no footwear word at all. No leg stops it. The
smallest change that would stop it is one extra clause in the **SOLE** leg (the quote must also be on
the footwear subject); the labelled PROBE copy implementing exactly that clause stops this fixture
and still admits an honest talaria row (both receipts below).

## Files changed

- **Lane:** this report only —
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-62/w1/CtlDOffTopicRow.md`.
  Nothing else in the lane repo was written; no git/jj write ran in the lane or in
  `/home/vgpnk/Projects/shokunin`.
- **Scratch (all fixtures and instruments),** `/fast/scratch/hyaku/kotodama-r62/CtlDOffTopicRow/`:
  - `clone/` — `git clone` of the lane repo, checked out exactly `f0173481047a93c46798f90b68d71d4f169d2642`
    (BASE `d42ffb890a54c8431fa891380b6c38bb608b8362` verified present and an ancestor of the tip).
  - `build.py` — the off-topic fixture generator (four lines + S693 row + S687 used-by cleared).
  - `build-honest.py` — the honest on-topic calibration fixture generator (same four lines, S693 =
    Wikipedia *Talaria*).
  - `check-lines.py` — evaluates lines 63/74/75/93 against the **frozen counter's own** `lcs`,
    `longest_run`, `STOP` and the locator's `normalise`/`QUOTE`, so LINK/COPY arithmetic is the
    counter's, not a re-implementation. Read-only.
  - `accept-d-probe.py` — labelled PROBE copy of the frozen counter (one change; diff below).
  - `fixture-entry.md`, `fixture-sources.md` — the off-topic fixture's two files, byte-copied.
  - page snapshots `spaceplane.html`, `talaria.html`, `wh.html`, `wikt.html`, `moth.html`, `hx.html`,
    `airbus.html`, `ntrs*.json`, `ld*.html`, `lat.html`, `raw.txt`, `spaceplane.raw.txt` — the
    fetched bytes behind every quote and every locator verdict quoted below.
  - the clone was returned to pristine (`git status --porcelain` empty) after the last run.

**No tool was installed or updated.** Nothing was needed: the frozen locator and counter are
stdlib-only and Python 3 is present (`python3 -B` throughout). No pacman/uv/npm action was taken.

## The off-topic source (real page, ordinary means, located, captured)

`https://en.wikipedia.org/wiki/Hermes_(spaceplane)` — the English Wikipedia article on the
**Hermes spaceplane**, a proposed French crewed spaceplane. Its `Hermes` is the spacecraft's name,
not the god's footwear: the article's body text says nothing about sandals, boots, talaria or any
footwear.

- **Live page:** `GET https://en.wikipedia.org/wiki/Hermes_(spaceplane)` with the lane locator's own
  User-Agent → HTTP 200, 262 628 bytes. The wikitext is a redirect (`#REDIRECT [[Hermes (spacecraft)]]`)
  to `Hermes (spacecraft)`; the rendered body was read from the returned HTML.
- **Verbatim body-text quote (16 words):**

  > Hermes was a proposed spaceplane designed by the French Centre National d'Études Spatiales (CNES) in 1975

  Present verbatim in the rendered body text of the page (checked against the tag-stripped
  `mw-content-text` block of the fetched `spaceplane.html`).
- **Wayback capture of the same page:** `https://web.archive.org/web/20260703060717id_/https://en.wikipedia.org/wiki/Hermes_(spaceplane)`
  (timestamp from the Wayback availability API for that exact URL; the page is a
  `#REDIRECT [[Hermes (spacecraft)]]`, so the capture replays the redirect target). CDX for
  `en.wikipedia.org/wiki/Hermes_(spacecraft)` also lists 200-status captures
  (e.g. `20260130154343`, `20260901182140`); the `20260703060717` capture of the *spaceplane* URL is
  the one used, because it is the capture of the URL the row lists.
- **Locator verdicts** (`timeout 300 python3 -B reports/round-61/reopen-quote.py URL QUOTE`, run from
  the clone, exit 0 = LOCATED):

  ```
  LOCATED https://en.wikipedia.org/wiki/Hermes_(spaceplane)                                        exit=0
  LOCATED https://web.archive.org/web/20260703060717id_/https://en.wikipedia.org/wiki/Hermes_(spaceplane)  exit=0
  ```

  The quote is 16 words, above the locator's `MIN_WORDS = 8` floor, and it is body text of the
  article's lead paragraph (not a caption, not an attribute).

**Tier note (honest register).** The row was written **tier B** as the assignment specifies. The
lane's own precedent (registry row S178, "Wikipedia, Guanche language") treats Wikipedia as
**tier C**, "encyclopedia lead only". This is a curation objection to the fixture, not to the
counter, and it is exactly why the tier-C variant was also scored: with the tier cell set to `C`
the frozen counter stops the same off-topic row at **SOLE** (receipt `offtopic-tierC` below). The
counter cannot see the tier-curation dispute; it reads the cell.

## The fixture (off-topic row, honest repairs of 63/74/75)

`build.py` writes into the clone exactly four entry lines and one registry row.

Entry (`corpus/knowledge/culture-material/footwear-codes-terminology.md`), lines 63/74/75/93 only —
line 63 keeps the source's open country list, line 74 names the caption, line 75 keeps the hedge,
line 93 cites S693 and restates the off-topic quote:

```
63  - A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, Belgium, etc. (S692)
74  - The caption of a 17th-century Persian image states that the heel was not a European invention but originated in Western Asia for horseback riding. (S665)
75  - The earliest evidence we have of someone wearing heels comes from a 10th-century Persian bowl (S666)
93  - Hermes was a proposed spaceplane designed by France's Centre National d'Études Spatiales in 1975. (S693)
```

Registry (`corpus/SOURCES.md`), S693 inserted after S692, S687's used-by cell changed to `—`
(the entry no longer cites it), every base line untouched:

```
| S693 | Hermes (spacecraft), English Wikipedia, 2026-10-23 — https://en.wikipedia.org/wiki/Hermes_(spaceplane) ; capture https://web.archive.org/web/20260703060717id_/https://en.wikipedia.org/wiki/Hermes_(spaceplane) | docs | B | the proposed Hermes crewed spaceplane and its CNES and ESA origins |  Lead paragraph, first sentence: "Hermes was a proposed spaceplane designed by the French Centre National d'Études Spatiales (CNES) in 1975" | The article describes Hermes as a proposed French crewed spaceplane, first designed by CNES and later by ESA. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

The URL is new (`grep -c wikipedia corpus/SOURCES.md` at BASE = 1, the S178 Guanche row); the row
has 11 columns / 13 split cells, `mined`, opened `2026-10-23`, used-by the entry, live URL then the
Wayback capture of that same page — the shapes ROWS wants.

LINK/COPY arithmetic for the four lines, computed with the **frozen counter's own functions**
(`check-lines.py`, importing `accept-d.py`'s `lcs`/`longest_run`/`STOP` and the locator's
`normalise`/`QUOTE`):

```
line 63 S692: content=12 shared=10 lcs=9/5 run=12 LINK=PASS COPY=PASS
line 74 S665: content=14 shared=8  lcs=8/6 run=7  LINK=PASS COPY=PASS
line 75 S666: content=10 shared=9  lcs=9/4 run=9  LINK=PASS COPY=PASS
line 93 S693: content=9  shared=8  lcs=8/4 run=7  LINK=PASS COPY=PASS
```

## Which leg (if any) stops an off-topic but real, located row

**None.** Under the frozen counter the off-topic tier-B row reaches `ACCEPT-D-62: PASS`, exit 0 —
all fourteen legs PASS. The mechanism, read off the frozen source:

- **SOLE** (`accept-d.py:201-203`) is the only leg that looks at the new row's *content*. It requires
  the anchor quote to match `\b(talaria|hermes)\b` — the word **or**, not **and**. A page about a
  French spacecraft called Hermes satisfies it exactly as a page about the god's winged sandals
  would. `hermes` alone carries no footwear sense.
- **LINK** requires the entry line to restate *its own row's* quote (≥5 content words, ≥3 shared,
  LCS ≥ max(4, 0.4 × content)). A line that honestly restates the off-topic quote therefore passes
  LINK — LINK measures fidelity to the row, never the row's *subject*.
- **COPY** (≤12 consecutive words) is the same story.
- **LOCATE** only asks whether the quote is present on the page. The quote **is** present, in body
  text, on a page reachable by ordinary means with a Wayback capture. LOCATE passes.
- **ROWS**, **APPEND**, **ACCESS**, **LINT** are shape/registry checks. They pass.
- No leg reads the page's subject, the article title, the row's `scope`/`teaches`, or the entry
  file's own subject. Round 61's counter had a `TOPIC` leg for exactly this
  (`reports/round-61/accept-c.py:84-110`, `TOPIC_WORDS`/`WEAK`/`CONTEXT`); round 62's
  `accept-d.py` has **no TOPIC leg**, and the topic-bearing clause of the claim statement
  ("line 93 cites one new tier A/B row … whose quote names talaria or Hermes") is satisfied by the
  disjunction.

Two further fixtures isolate where the gap bites:

- `offtopic-tierC` — the same off-topic row with the tier cell set to `C` (the honest curation for
  an encyclopedia lead): **stopped at SOLE**. The counter only reads the cell, so a curator's tier
  dispute is the *only* thing that incidentally stops this row, and only if the row is tiered
  honestly — which is a curation decision, not a check.
- `offtopic-line93-kept` — the same off-topic row, but line 93 keeps the footwear wording
  ("Hermes' talaria were winged leather boots. (S693)") instead of restating the off-topic quote:
  **stopped at LINK** (`93:content=5 shared=1 order=1/4`). This is the *honest* line 93, and it is
  stopped only because the line no longer matches its own off-topic row — a coincidence of wording,
  not a subject check. An author who wrote the line to match the off-topic row (as fixture
  `offtopic-tierB` does) walks straight through.

## The smallest change that would stop it

One extra clause in the **SOLE** leg: the new row's anchor quote must also be on the footwear
subject. Implemented in the labelled PROBE copy `accept-d-probe.py` — the frozen counter plus
round 61's own lexicon constants (`TOPIC_WORDS`, `WEAK`, `CONTEXT`, verbatim from
`reports/round-61/accept-c.py:84-92`) and one added condition in SOLE:

```diff
--- clone/reports/round-62/accept-d.py
+++ accept-d-probe.py
@@ -1,5 +1,5 @@
 #!/usr/bin/env python3
-r"""Round-62 claim D acceptance (depth, sourced): the four footwear-entry lines the round-61 closure
+r"""PROBE COPY of reports/round-62/accept-d.py with ONE change: the SOLE leg additionally requires the new row's anchor quote to be on the footwear subject (talaria, or a strong footwear lexicon word, or a footwear CONTEXT word). Round-62 claim D acceptance (depth, sourced): the four footwear-entry lines the round-61 closure
@@ -75,6 +75,15 @@
 ORDER_MIN = 4
 ORDER_SHARE = 0.4
 SID = re.compile(r"\bS\d{3,}\b")
+TOPIC_WORDS = frozenset("""
+shoe shoes shod unshod barefoot footwear sandal sandals boot boots clog clogs moccasin moccasins
+slipper slippers heel heels sole soles insole insoles geta zori zōri waraji tabi chopine chopines
+poulaine poulaines patten pattens sabot sabots lapti opanak opanci caliga caligae kamik kamiks kamiit
+mukluk mukluks paduka padukas shoemaker shoemakers shoemaking cordwainer cordwainers cobbler cobblers
+footgear brogue brogues buskin buskins talaria
+""".split())
+WEAK = frozenset("boot boots sole soles slipper slippers tabi".split())
+CONTEXT = frozenset("wear wears wore worn wearing wearer foot feet leather pair pairs walk walking".split())
 SPACED = re.compile(r"\bS\s+(\d{3,})\b")
@@ -198,9 +207,13 @@
 
     s93 = next(iter(ids[93])) if len(ids[93]) == 1 else ""
     c93 = cells(s93) if s93 else None
+    q93 = locator.normalise(quote_of(s93)).split() if s93 else []
+    topic_ok = bool(re.search(r"\btalaria\b", " ".join(q93))) or bool(
+        set(q93) & (TOPIC_WORDS - WEAK)) or bool(set(q93) & CONTEXT)
     leg("SOLE", bool(s93) and new_id(s93) and c93 is not None and len(c93) == 13
-        and c93[4].strip() in ("A", "B") and re.search(r"\b(talaria|hermes)\b", locator.normalise(quote_of(s93))) is not None,
-        f"id={s93 or '-'} tier={c93[4].strip() if c93 and len(c93) > 4 else '-'}")
+        and c93[4].strip() in ("A", "B")
+        and re.search(r"\b(talaria|hermes)\b", locator.normalise(quote_of(s93))) is not None and topic_ok,
+        f"id={s93 or '-'} tier={c93[4].strip() if c93 and len(c93) > 4 else '-'} topic={topic_ok}")
```

Probe counter SHA-256 `cfa62fb0055b431b1cffad0f428ec90794a03f81c16a435b13d9a36d41d00b19`; frozen
counter SHA-256 `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` (unchanged
throughout; the clone's copy is byte-identical to the lane's).

**Calibration of the probe (no false negative).** The honest positive fixture `build-honest.py`
uses the real on-topic page `https://en.wikipedia.org/wiki/Talaria` with the verbatim body-text
quote *"The Talaria of Mercury ( Latin : tālāria ) or The Winged Sandals of Hermes"* (located live
and in the capture `https://web.archive.org/web/20251105004958id_/https://en.wikipedia.org/wiki/Talaria`,
both `LOCATED`, exit 0), and the same honest repairs of lines 63/74/75. It **PASSES both the frozen
counter and the probe** (`SOLE PASS id=S693 tier=B topic=True`). So the probe clause separates the
off-topic row from an on-topic row without failing an honest talaria row.

A narrower variant of the same fix — requiring the quote to contain `talaria` specifically instead
of `talaria` **or** `hermes` — would also stop this fixture, but it would reject an honest row whose
quote says "Hermes' winged sandals" without the Latin word; the lexicon form above is the version
that keeps both. (Round 61's `CtlCOffTopic` already showed that a bare lexicon token filter is
defeated by homonyms — `sole` = only, `boot` = computer start-up — so the clause should be read as
a cheap subject filter, not a proof of subject.)

## Receipts

Counter hashes: frozen `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`
(unchanged), probe `cfa62fb0055b431b1cffad0f428ec90794a03f81c16a435b13d9a36d41d00b19`.
Every run: `cd /fast/scratch/hyaku/kotodama-r62/CtlDOffTopicRow/clone && timeout 900 python3 -B
reports/round-62/accept-d.py` (frozen) or `python3 -B ../accept-d-probe.py --root .` (probe).
Full stdout is reproduced below, unabridged, with the real exit codes.

### base (clone unchanged) — frozen

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:18Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### offtopic-tierB (S693 tier B, line 93 restates the off-topic quote) — frozen

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
LOCATE PASS located=1 cited=1 at=2026-10-23T11:19Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

### offtopic-tierC (same off-topic row, tier cell C) — frozen

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE FAIL id=S693 tier=C
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:28Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### offtopic-line93-kept (off-topic row, line 93 keeps the footwear wording) — frozen

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
LINK FAIL bad=['93:content=5 shared=1 order=1/4']
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:19Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### offtopic-tierB — probe (the proposed one-clause fix)

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE FAIL id=S693 tier=B topic=False
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:24Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### honest-ontopic (Wikipedia *Talaria*, on-topic row) — frozen

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
LOCATE PASS located=1 cited=1 at=2026-10-23T11:27Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

### honest-ontopic — probe (the proposed fix must not fail an honest row)

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B topic=True
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:27Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

```
RECEIPT CtlDOffTopicRow/base counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
RECEIPT CtlDOffTopicRow/offtopic-tierB counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlDOffTopicRow/offtopic-tierC counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE
RECEIPT CtlDOffTopicRow/offtopic-line93-kept counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=LINK
RECEIPT CtlDOffTopicRow/offtopic-tierB-probe counter-sha256=cfa62fb0055b431b1cffad0f428ec90794a03f81c16a435b13d9a36d41d00b19 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 probe=FAIL stopped-by=none (frozen); SOLE (probe)
RECEIPT CtlDOffTopicRow/honest-ontopic counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlDOffTopicRow/honest-ontopic-probe counter-sha256=cfa62fb0055b431b1cffad0f428ec90794a03f81c16a435b13d9a36d41d00b19 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 probe=PASS stopped-by=none
```

**VERDICT off-topic real row for line 93: CONTROL-MET** — the fixture
`/fast/scratch/hyaku/kotodama-r62/CtlDOffTopicRow/build.py` (S693 = Wikipedia *Hermes (spaceplane)*,
tier B, real live URL + Wayback capture, quote located live and in the capture, honest repairs of
lines 63/74/75, line 93 restating that quote) reaches `ACCEPT-D-62: PASS`, exit 0, under the
**frozen** counter with no change at all: **no leg stops an off-topic but real, located, tier-B
row.** The smallest change that would stop it is one extra clause in **SOLE** — the new row's
anchor quote must also be on the footwear subject (round 61's own `TOPIC_WORDS`/`WEAK`/`CONTEXT`
lexicon) — implemented and calibrated in the labelled PROBE copy
`accept-d-probe.py` (SHA-256 `cfa62fb0055b431b1cffad0f428ec90794a03f81c16a435b13d9a36d41d00b19`),
which stops this fixture at SOLE and still passes the honest Wikipedia-*Talaria* fixture.

## Risks and limits

- **This is a counter-coverage finding, not a claim verdict.** The frozen counter passed a fixture
  whose new row says nothing about footwear. No lane file was changed; the counter was not edited;
  no claim was judged. Whether to revise `accept-d.py` before its first run on the real claimed
  object is the L1's call (the claims' predicate rule allows a revision only before the first run
  of that counter on the claimed object, committed with the control receipt that forced it).
- **The off-topic source is Wikipedia, and the lane treats Wikipedia as tier C** (precedent S178).
  The row was written tier B as instructed; the `offtopic-tierC` receipt shows the frozen counter
  stops it at SOLE purely because the cell says C. That is a curation decision, not a check, so it
  does not generalise: any off-topic source an author is willing to label B (a news article about
  the Hermes spaceplane, a space agency's project page, the Hermes parcel company, a moth genus)
  walks through the counter unchanged. A tier-B-labelled, non-encyclopedia off-topic row was not
  built here — the reachable candidates (esa.int, nasa.gov, ntrs.nasa.gov, hermesworld.com,
  airbus.com) either 404'd, 403'd, 429'd or served JS-only shells in the time box; that variant
  would strengthen the finding but does not change it, since the counter never reads the publisher.
- **The probe's topic filter is a cheap token test**, not a subject proof: round 61's
  `CtlCOffTopic` showed the same lexicon admits homonyms (`sole` = only, `boot` = computer
  start-up). It is the smallest thing that stops this fixture without failing the honest one.
- **Wikipedia text and Wayback availability move.** The off-topic quote and the honest quote were
  located at the timestamps recorded above (LOCATE stamps 11:19Z, 11:24Z, 11:27Z, 11:28Z on
  2026-10-23); several Wayback captures of the same pages returned transient `HTTPError` during
  this session (e.g. `20251112122429id_`, `20260811224745id_` for worldhistory.org/Hermes) and were
  retried, as QUALITY criterion 13 anticipates. All quotes used here are pinned to the recorded
  captures, not to the live pages.
- **The honest calibration uses Wikipedia too**, so it is not an independent tier-A/B calibration of
  the lane's real S693; it calibrates only that the probe clause does not reject an on-topic talaria
  quote. `ScribeTalariaMW` and `ScribeTalariaRef` are landing the real tier-A/B rows.
- No blockers. All runs were `timeout`-capped and synchronous; no background process, no service
  and no install was started; the clone was left pristine.

## Retained evidence (paths)

- `/fast/scratch/hyaku/kotodama-r62/CtlDOffTopicRow/clone/` — the pinned clone (pristine at the end).
- `build.py`, `build-honest.py`, `check-lines.py`, `accept-d-probe.py` — the fixture generators,
  the LINK/COPY arithmetic helper and the labelled PROBE counter.
- `fixture-entry.md`, `fixture-sources.md` — the off-topic fixture's exact bytes.
- `spaceplane.html`, `talaria.html`, `wikt.html`, `wh.html`, `hx.html`, `moth.html`, `airbus.html`,
  `ntrs.json`, `ntrs2.json`, `ntrs.html`, `ld.html`, `ld2.html`, `lat.html`, `raw.txt`,
  `spaceplane.raw.txt` — the fetched page bytes behind every quote and every locator verdict.
- Page snapshots are scratch evidence only; none of them is proposed as lane content.
