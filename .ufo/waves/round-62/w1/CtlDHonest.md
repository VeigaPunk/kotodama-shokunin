# CtlDHonest — claim D, honest-positive calibration

Seat: `KotodamaR62.CtlDHonest`. Scope: the HONEST POSITIVE fixture for claim D (accept-d.py).
Nothing was landed in the lane: the lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
is byte-unchanged by this seat (no git/jj write, no file edit). All fixture work is in scratch.

## 1. Fixture and how to reproduce

Clone (frozen revision, unmodified except the fixture edits):

```
/fast/scratch/hyaku/kotodama-r62/CtlDHonest/clone      # git checkout f0173481047a93c46798f90b68d71d4f169d2642
```

Files edited in that clone (fixture only, never landed):

- `corpus/knowledge/culture-material/footwear-codes-terminology.md` — lines 63, 74, 75, 93.
- `corpus/SOURCES.md` — S687's used-by cell set to `—`; one new row S693 appended after S692.

Frozen counter, unmodified, sha256 matches the pin in the assignment:

```
3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4  reports/round-62/accept-d.py
```

## 2. The four repaired lines (verbatim, in the fixture)

Line 63 — keeps the source's open country list (S692, dictionary.com sense 1 ends "Belgium, etc."):

```
- A sabot is a wooden shoe hollowed out of one block, worn especially by farmers and workers in the Netherlands, France, Belgium, and other countries. (S692)
```

Line 74 — names the caption it came from, since the Bata Shoe Museum page carries that sentence
only in the image's caption field (`data-img-description`), never in body text (S665):

```
- An image caption states that the heel was not a European invention but originated in Western Asia centuries ago for horseback riding. (S665)
```

Line 75 — keeps the BBC page's own hedge "we have" (S666):

```
- The earliest evidence we have of someone wearing heels comes from a 10th-century Persian bowl. (S666)
```

Line 93 — new tier A/B row, not S687 (S693):

```
- Hermes' talaria were small wings fixed to the ankles, reckoned among his attributes. (S693)
```

## 3. The new row S693 (verbatim)

```
| S693 | Smith, William, A Smaller Dictionary of Greek and Roman Antiquities, abridged from the author's Dictionary of Greek and Roman Antiquities, 12th edition, London: John Murray, 1884 — Project Gutenberg eBook 65909 — https://www.gutenberg.org/files/65909/65909-0.txt ; capture https://web.archive.org/web/20260211202500id_/https://www.gutenberg.org/files/65909/65909-0.txt | book | B | Smith's dictionary on talaria, the winged sandals of Hermes |  TALARIA entry, opening sentence: "small wings, fixed to the ancles of Hermes and reckoned among his attributes" | Smith's dictionary says talaria were small wings fixed to the ancles of Hermes, reckoned among his attributes. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

Why this source, and how it was opened (all by ordinary means, no browser, no challenge bypassed):

- Opened myself: `https://www.gutenberg.org/files/65909/65909-0.txt` → HTTP 200, 2,255,095 bytes.
- Body text, not a caption: the `TALARIA` entry begins "TĀLĀRĬA, small wings, fixed to the ancles of Hermes and reckoned among his attributes (πέδιλα, πτηνοπέδιλος)." — the anchor is that entry's first sentence, and the quote names **Hermes** and **talaria**.
- Not Merriam-Webster, not Britannica. It is a scholarly reference work (Smith's dictionary, abridged from
  the 1875 *Dictionary of Greek and Roman Antiquities*), tier B, and a different source from the
  existing S688 (Yates 1875 via LacusCurtius) and S687 (Theoi).
- Wayback capture of the same page exists and works:
  `https://web.archive.org/web/20260211202500id_/https://www.gutenberg.org/files/65909/65909-0.txt`
  (CDX `statuscode:200`, and the capture body contains the `TĀLĀRĬA` entry — checked directly).
- URL freshness: `65909` does not occur in `corpus/SOURCES.md` at BASE (grep: no match); the four
  Gutenberg URLs already in the registry are pg52081, pg62704, pg73533, pg9700.

Independently re-opened for the other three lines (also ordinary means, HTTP 200):

- `https://www.dictionary.com/browse/sabot` → "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc." (list is open, ends "etc.").
- `https://batashoemuseum.ca/standing-tall/` → the sentence appears in `data-img-description` (×2) and `thumbnail-description`, and **not** in body text; hence "An image caption states…".
- `https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes` → body text: "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl." (hedge "we have" present).

## 4. Canonical receipt — frozen counter, honest fixture

```
cd /fast/scratch/hyaku/kotodama-r62/CtlDHonest/clone && timeout 900 python3 -B reports/round-62/accept-d.py
```

Full stdout:

```
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
LOCATE PASS located=1 cited=1 at=2026-10-23T11:54Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
```

exit=0

```
RECEIPT CtlDHonest/D-honest-positive counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
```

**Verdict: the frozen counter is NOT wrong here.** Every leg passes on an honest fixture, so
accept-d.py does not false-negative on this repair shape. The expected PASS was reached; no leg
needed a counter revision, so no counter was edited.

## 5. Lane census cross-check (read-only, outside the counter)

`bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <clone>/corpus/SOURCES.md --root <clone> --today 2026-10-23`

- exit=0 (no E-code) on the fixture.
- On the fixture: `W03 S687 mined but unused` (S687's used-by now `—`).
- On the base registry: `W01 S687 tierC mined used-by=corpus/knowledge/.../footwear-codes-terminology.md`.

So the repair trades the round-61-routed W01 (tier-C row as sole support) for a W03 (mined but
unused) — both are warnings, and the lane census does not gate on W-codes.

## 6. Boundary probes (frozen counter, in scratch copies only)

Each probe is a copy of the honest fixture with one mutation; the counter is untouched.

| probe | mutation | result | legs that FAIL |
|---|---|---|---|
| A | mark-only "repair": the three base lines kept and marked `[to-verify]`, line 93 back on S687, no new row | FAIL (exit 1) | SET, NOMARK, OPEN, HEDGE, CAPTION, SOLE, ROWS, LOCATE |
| B | S693 anchor quote truncated to 8 words ("small wings fixed to the ancles of Hermes"), line 93 shortened to match | FAIL (exit 1) | LINK (`93:content=6 shared=4 order=3/4`) |
| F | S693 anchor quote replaced by a fabricated sentence not on the page | FAIL (exit 1) | LINK, LOCATE (`S693: … quote-absent; … HTTPError (passes=3)`) |
| G | S693 source cell stripped of its Wayback capture | FAIL (exit 1) | ROWS (`S693:urls`) |
| H | S693 tier B → C | FAIL (exit 1) | SOLE (`id=S693 tier=C`) |
| I | S693 re-pointed at the Bata Shoe Museum page with that page's caption-only quote | FAIL (exit 1) | SOLE, LINK |
| J | S687 status `mined` → `queued` (the census-correct demotion) | FAIL (exit 1) | APPEND — S687's status cell is pinned by the frozen counter, so a lane that also demotes the status gets a miss |

Probe J is worth the L1's attention: **the frozen APPEND leg pins S687's status cell.** It compares
`cells[:-2]` plus `cells[-1]`, i.e. cells 0–10 and the trailing empty cell; only the used-by cell
(11) is free. A landing that demotes S687 to `queued` (the census-correct end state for an
uncited row) therefore fails APPEND. In this fixture S687 keeps `mined` with used-by `—`, which
costs a W03 warning but satisfies the counter. Smallest counter change that would allow the
demotion: extend the S687 exception to compare only cells 0–7 and 12, leaving 8–11 free.

## 7. Gap found: the declared FRESH clause is not a counter leg

`claims.json` D `controls_required_before_data` names two clauses that `accept-d.py` does not
implement as legs: **FRESH** ("no reused base registry URL") and **KEEP** ("63/74/75 keep >= 60%
base content words"). Both are satisfied by this fixture when computed by hand:

- FRESH: S693's two URLs (`…/files/65909/65909-0.txt` and its `web.archive.org/web/20260211202500id_/`
  capture) — neither appears among the base registry's URLs.
- KEEP (fraction of BASE line's content words retained, counter STOP list, 4+ chars):
  line 63 → 12/12 = 1.000; line 74 → 6/8 = 0.750 (dropped `adopted`, `europeans`); line 75 → 10/10 = 1.000.
  All three ≥ 0.60.

But a probe that puts **S688's already-registered LacusCurtius URL** into S693's live-URL slot
(probe C) still prints `ACCEPT-D-62: PASS` with every leg PASS — the reused-URL case is invisible to
the frozen counter. Same for a capture pointing at an unrelated page (probe D): the row's Wayback
URL need not be a capture *of the same page* and the counter does not notice, as long as one of the
row's URLs locates the quote (probe D passes because the live URL still locates it).

Smallest counter change that would close the FRESH hole: in the ROWS leg, additionally require that
no URL of a NEW-block row occurs in the BASE registry (i.e. compare against
`git show BASE:corpus/SOURCES.md`), and require the capture URL to embed the same path as the live
URL. Both are checkable with the bytes already in the counter.

## 8. Review-only notes (not legs)

- The S693 anchor is page body text, not a caption: the `TALARIA` dictionary entry's first
  sentence, in the plain-text transcription of the printed book. The nearby
  `[Illustration: Talaria. (From a Statue of Hermes at Naples.)]` line is an illustration caption and
  is **not** the anchor.
- The three repaired lines' wording beyond the shared words is carried by their pages: the sabot
  list really does run open to "etc."; the heel sentence really is caption-only on the Bata page;
  the BBC page really does say "we have".
- Line 93 is now backed by a tier-B row instead of the tier-C Theoi row, so it is no longer sole
  support of a tier-C row.

## 9. Risks and blockers

- **S687's status is pinned by the frozen counter** (probe J). If the L1 wants the census-correct
  `queued` demotion, accept-d.py needs the APPEND exception widened *before* its first run on the
  landed object; otherwise keep `mined` + used-by `—` (W03 warning, counter PASS).
- **FRESH and KEEP are not counter legs.** The landed repair is FRESH- and KEEP-clean by hand, but
  the counter does not enforce either; a mutation that reuses a base URL would pass.
- **Perseus/LacusCurtius rate limiting.** `www.perseus.tufts.edu` returned HTTP 429 for every
  request during this seat's window (including through the base locator's own retry), and
  `web.archive.org` intermittently returned 429 for the Perseus capture. The Gutenberg host was
  stable, which is why S693 is a Gutenberg-hosted book rather than a Perseus/LSJ entry. The
  `web.archive.org` 429s were transient: the same capture was fetched successfully several times.
- No tool installs were needed for this seat; nothing was installed or updated.

## 10. Files changed by this seat

- Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`: **none** (read-only).
- Scratch only, under `/fast/scratch/hyaku/kotodama-r62/CtlDHonest/`:
  `clone/` (honest fixture), `probeA/` `probeB/` `probeC/` `probeD/` `probeE/` `probeF/` `probeG/`
  `probeH/` `probeI/` `probeJ/` (one-mutation copies of the fixture).
- This report: `.ufo/waves/round-62/w1/CtlDHonest.md` (one write, absolute path).
