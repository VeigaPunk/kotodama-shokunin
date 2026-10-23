# CtlCJunkRow — claim C (accept-c.py) junk-row controls

Round 63, wave 1, seat `CtlCJunkRow` (leaf). 2026-10-23.

- Clone: `/fast/scratch/hyaku/kotodama-r63/CtlCJunkRow/clone`, checked out at
  `80d53ffde7788299b69dbb0bd0436b2b7ddddb95`, local branch `main` carrying the
  control fixture as commit `1ca5f8a7dce50a37a3fd79271a76a9ee79572777`
  (parent 80d53ffe). Nothing written in the lane or the fleet repo except this file.
- Counter run: `reports/round-63/accept-c.py`, sha256
  `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca` (matches the
  tasking's frozen hash; never edited, no probe copy needed).
- No installs (no pacman: transactions are paused host-wide; no uv/npx/binary
  installs were needed).

## The fixture

A candidate tree was built inside the clone that satisfies every machine leg
without doing the claimed work: an entry of 36 lines whose 24 bullets are a
template (`Control clause records X then Y then Z from the page (S###)`), and 24
registry rows S694-S717 over **Wikipedia lead sentences** — every quote is a real
9-14-word body-text sentence (so LIVE can pass), every capture URL is fabricated
(`https://web.archive.org/web/20200101000000id_/<live url>`), and the first five
pages are pure homographs of the headword (**dental crown, crown ether, crown
currency, crown botany, crown heraldry**), not headgear as rank/ritual/identity.
README row + section count + totals line + counts footer were updated so SWEEP is
green. The entry's own topic line says, verbatim, that every row is an off-topic
homograph page — the counter cannot read that as a defect.

Baseline receipt (FULL stdout):

```
FILE PASS exists lines=36 h1=1 h2=2 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

Direct locator check on the off-topic live row (not the counter): 
`python3 -B reports/round-61/reopen-quote.py --row S694` → `LOCATED https://en.wikipedia.org/wiki/Dental_crown`, exit 0.

Fabricated capture evidence: `web.archive.org` is unreachable from this host
(`Failed to connect to web.archive.org:443`), and the Wayback availability API
for the S694 live URL returns closest capture `20200314185156`, not the row's
`20200101000000`; no leg ever fetches a capture (LIVE stops at the first URL
that locates), so a capture URL that names no existing capture passes.

## Cases run (each = one mutation of the baseline, then the frozen counter)

Mutation (a-live): S694 → `https://en.wikipedia.org/wiki/Headdress` with the
invented quote `crown dental type invented phrase not carried by the page at all
here` (locator on that URL+quote: `NOT_LOCATED ... quote-absent`, exit 1); the
S694 bullet regenerated to match so RESTATE is not what fails.

```
FILE PASS exists lines=36 h1=1 h2=2 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:NOT_LOCATED https://en.wikipedia.org/wiki/Headdress quote-ab']
ACCEPT-C-63: FAIL
exit=1
```

Mutation (a-nonlive): the **same invented quote** on the **same invented page**,
placed at S695 (outside the six-row LIVE subset; ids S694/S695 swapped in the
entry and the registry so no other leg moves).

```
FILE PASS exists lines=36 h1=1 h2=2 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

Mutation (b-live): S694 → real page `Headgear` (Wikipedia redirect to Headdress)
carrying the real sentence from a **different** page,
`a crown is a traditional form of head adornment or hat worn by monarchs`
(taken from `Crown_(headgear)`; locator on Headdress + that quote:
`NOT_LOCATED ... quote-absent`), bullet regenerated for RESTATE.

```
FILE PASS exists lines=36 h1=1 h2=2 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:NOT_LOCATED https://en.wikipedia.org/wiki/Headdress quote-ab']
ACCEPT-C-63: FAIL
exit=1
```

Mutation (c): S694 keeps the dental-crown live URL and quote but its capture
embeds a **different page** (`.../web/20200101000000id_/https://en.wikipedia.org/wiki/Coronet`).

```
FILE PASS exists lines=36 h1=1 h2=2 h3=0 topic=True
ROWS FAIL bad=['S694:capture_original_mismatch'] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK FAIL bad=['S699:registry_hits=2']
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

(LINK fails only because the mismatched original is another row's live URL; it is
a side effect of URL reuse, not a capture check.)

Mutation (d): S694 → `https://www.gutenberg.org/ebooks/2701` with that page's
`<meta name="description">` text, `moby dick or the whale by herman melville free
ebook digitized and proofread by volunteers` (locator on URL+quote:
`NOT_LOCATED ... quote-absent`, exit 1; the Getty collection page's meta
description is likewise `NOT_LOCATED`).

```
FILE PASS exists lines=36 h1=1 h2=2 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:NOT_LOCATED https://www.gutenberg.org/ebooks/2701 quote-abse']
ACCEPT-C-63: FAIL
exit=1
```

Mutation (e): the baseline itself — S694 is the dental-crown page (dental
restoration, an off-topic homograph of "crown"), S695 crown ether, S696 crown
(currency), S697 crown (botany), S698 crown (heraldry). Receipt = baseline above:
`ACCEPT-C-63: PASS`, exit 0.

## Receipts

One line per case (`counter-sha256` is the frozen counter run in every case):

```
RECEIPT CtlCJunkRow/baseline counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCJunkRow/a-live counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=LIVE
RECEIPT CtlCJunkRow/a-nonlive counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCJunkRow/b-live counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=LIVE
RECEIPT CtlCJunkRow/c-capture-other-page counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=ROWS,LINK
RECEIPT CtlCJunkRow/d-meta-description counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=LIVE
RECEIPT CtlCJunkRow/e-offtopic-homograph counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
```

## Verdicts

```
CONTROL-MET e-offtopic-homograph (also baseline, a-nonlive): a 36-line template entry over 24 Wikipedia lead sentences, five of them pure homographs (dental crown, crown ether, crown currency, crown botany, crown heraldry), fabricated Wayback captures, passes all nine legs including LIVE (S694 = dental crown, in the LIVE subset, printed LOCATED). No leg reads subject matter, sense, or the entry's own admission that the pages are off-topic. Smallest counter change that stops it: a SENSE leg requiring, per new row, at least two content words of the anchor quote to appear in the entry's `- topic:` line in the declared scope vocabulary (a dental quote holds only "crown"), or equivalently promoting the blind per-row SUPPORT judgment from review-only to a leg. Neither is cheap in the sense of removing the semantic review; the cheap lexical version stops this fixture but not a junk author who composes quotes from topic words.
CONTROL-MET a-nonlive: one invented quote on one real page at S695 passes the whole frozen predicate, because LIVE re-opens only six of the 24 new rows ((n-693)%4==1). Smallest counter change that stops it: `LIVE_IDS = NEW_IDS` (24 locates instead of 6); cost is 18 more ordinary fetches and the same 3-attempt budget.
NONE-MET for a-live, b-live, d-meta and c at a LIVE-subset row: each is stopped by LIVE (a/b/d) or ROWS (c). c is a unit leg: ROWS compares the capture's embedded original string to the live URL, so a fabricated capture whose embedded original equals the live URL (baseline) passes all nine legs; stopping that needs a CDX-existence check of the 24 capture URLs (24 cheap API calls), which no current leg performs.
```

## Cross-cutting notes

- 18 of 24 rows are never fetched by the machine predicate; the entry's other 18
  claims rest entirely on the review-only blind SUPPORT seats, which the claim
  explicitly excludes from the predicate.
- Quote provenance: the locator ignores attribute values (`<meta name="description">`,
  `og:*`), so a metadata quote cannot locate, but `<title>`/heading text is a text
  node and does locate — the "verbatim body-text" row rule is therefore enforced
  only against attributes, not against titles or navigation/TOC text (the first
  extraction pass of this fixture produced 14-word TOC strings that located).
- Capture freshness: no leg compares the capture's timestamp with any capture the
  archive actually holds; `20200101000000id_/...` passed all nine legs for 24 rows.
- Environment: `web.archive.org:443` was unreachable from this host for the whole
  session (plain connection failure), so no capture was ever fetched here; live
  fetches of the fixture rows succeeded (Wikipedia 200 in ~0.5 s). Britannica,
  Etymonline, Merriam-Webster, Collins, Met, LoC and SI answered 403/429 to an
  ordinary UA; no challenge was routed around and no headless browser was used.

## Restoration evidence

Every mutation was applied to the working tree only, then
`git -C clone checkout -- .` restored it; the baseline commit was never amended
after the runs. Final state:

- `git status --porcelain` → empty; `git diff --stat HEAD` → empty.
- `corpus/SOURCES.md` sha256 `b6a2881e545512971c1cde8bac12cc9d1ac0176582904c585554a9cebf025888`
  (working tree = `git show HEAD:corpus/SOURCES.md`), 643 `| S` rows.
- `corpus/knowledge/culture-material/headgear-head-covering-codes.md` sha256
  `8fe41944dbb13e94da29e56ed919e94c4fee160086f63a9c48bbca1207ccfe41`
  (working tree = `git show HEAD:...`).
- `corpus/README.md` sha256 `c31b37fb060b1e8f53eb1a66238fb881a34729a45df9a0d560f8e947db9c9b75`.
- HEAD `1ca5f8a7dce50a37a3fd79271a76a9ee79572777`; the lane repo and the fleet
  repo were not touched.
