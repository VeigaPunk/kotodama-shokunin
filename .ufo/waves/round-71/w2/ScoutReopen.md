# ScoutReopen — round 71 wave 2: re-open five claim-C rows (S861, S864, S868, S871, S873)

Seat: `L1Kotodama71.ScoutReopen` (falsify, leaf; no spawns). Findings only; no lane bytes edited except this file.
Tooling: no installs or updates. Access date for every re-open: **2026-10-25**.
Measured revision: lane `HEAD = baf3b6a65aef9bacc6319e8904c423b788dc8af6`. Tree state at measurement: two lane files dirty from concurrent siblings — `corpus/README.md` (date line 2026-10-24 → 2026-10-25) and the entry's *Calibration shelf* line (adds `(S873)`); neither touches the five rows' prose, the `- source:` header block, or any count leg.

## Method

1. Re-opened each row's URL: live first, capture when the live page is a challenge wall. Fetch = plain HTTP GET with a browser UA (no browser automation, no captcha solving).
2. Located the quoted span by exact substring on the fetched HTML after tag-strip + HTML-unescape + whitespace-normalize (`re.sub(r'\s+',' ')`), and recorded the character offset in the normalized text.
3. Located the anchor: paragraph index inside the element narrative (`<p>` extraction), or nearest preceding `<h2>` for HTML articles.
4. Re-ran the claim-C counter and the frozen counting command.

## Row-by-row verdict

| row | URL opened (result) | quote re-located | anchor as claimed (registry / Gate) | anchor as located | span | anchor |
|---|---|---|---|---|---|---|
| **S861** | capture `web.archive.org/web/20260925201518/https://ich.unesco.org/en/RL/tango-00258` (200, 184,996 B). Live `ich.unesco.org/en/RL/tango-00258` = CAPTCHA wall | "the music, dance and poetry of tango both embodies and encourages diversity and cultural dialogue" — **found, offset 40,347**, verbatim (15 words) | "element record 00258, inscription narrative, paragraph 1" | narrative is the paragraph **immediately after** the `Inscribed in 2009 (4.COM) …` line → **¶2** under the round's own convention (see §Convention) | **PRESENT** | **FAIL** (off-by-one) |
| **S864** | capture `…/20210227223454/https://ich.unesco.org/en/RL/carnival-of-oruro-00003` (200, 190,840 B). Live = CAPTCHA wall | "the dancers walk the four kilometres of the processional route" — **found, offset 37,891**, verbatim (10 words) | "element record 00003, inscription narrative, paragraph 3" | ¶1 `Inscribed in 2008 (3.COM) …`, ¶2 `The town of Oruro, situated at an altitude of 3,700 metres …`, ¶3 `The Carnival, which takes place every year …` ← **quote here** | **PRESENT** | **PASS** |
| **S868** | live `https://www.abt.org/explore/learn/ballet-dictionary/` (200, 190,728 B) | "the positions of the feet are standard in all methods" — **found, offset 31,795**, verbatim (10 words) | "Ballet Dictionary page, 'Positions of the arms' paragraph" | entry headed `bras, positions des` → body opens "Positions of the arms. Although the positions of the feet are standard in all methods, the positions of the arms are not, each method having its own set of arm positions." | **PRESENT** | **PASS** |
| **S871** | live `https://www.wisdomlib.org/hinduism/book/the-natyashastra/d/doc209696.html` (200, 99,751 B) | "the Aṅgahāras consist of six, seven, eight or nine Karaṇas" — **found, offset 6,993**, verbatim (10 words, diacritics exact) | "chapter IV (karaṇa), section on aṅgahāra" / "chapter IV (karaṇa) aṅgahāra section" | page h2 order: `… Aṅgahāras` (¶16-29) → `Uses of Aṅgahāras` (¶28-29) → **`Karaṇas` (¶29-34)** ← quote in ¶30-34 → `Definition of Karaṇas` | **PRESENT** | **DRIFT** (label only: it is the *Karaṇas* section, one section after *Aṅgahāras*) |
| **S873** | live `https://plato.stanford.edu/entries/dance/` (200, 136,043 B) | "This is a vexed methodological question" — **found, offset 635**, verbatim (6 words) | "entry 'The Philosophy of Dance', section 1 (methodological questions)" / "entry section 1" | sentence is in the **untitled lead** ("What counts as "philosophy" of dance? This is a vexed methodological question."), *before* h2 `1. Analytic Approaches to Dance as Art`; page carries `substantive revision Wed Sep 3, 2025` | **PRESENT** | **DRIFT** (label only: preamble, not §1). The entry's `- source:` line (line 15) repeats the same mislabel "section 1, methodological questions" |

Totals: **5/5 spans PRESENT** (verbatim, offset-anchored). Anchors: **2 PASS, 1 FAIL, 2 DRIFT**.

## Convention check (why S861 is FAIL and S864 is PASS)

The round's paragraph numbering counts the `Inscribed in YYYY …` line as ¶1; the narrative body follows. Re-derived from the same captures:

| row | page structure (prose `<p>`, chrome dropped) | quote paragraph | Gate label |
|---|---|---|---|
| S862 | ¶1 inscription, ¶2 Mevleviye history, ¶3 whirling/training ← quote, ¶4 secularisation | ¶3 | ¶3 ✓ |
| S863 | ¶1 inscription, ¶2 Chhau narrative (single para) ← quote | ¶2 | ¶2 ✓ |
| S865 | ¶1 inscription, ¶2 Flamenco narrative (single para) ← quote | ¶2 | ¶2 ✓ |
| S867 | ¶1 inscription, ¶2 Kabuki origin ← quote, ¶3 plays, ¶4 post-1868 | ¶2 | ¶2 ✓ |
| **S861** | ¶1 inscription, **¶2 tango narrative ← quote** | **¶2** | **¶1 ✗** |
| S864 | ¶1 inscription, ¶2 Oruro town, ¶3 Carnival/procession ← quote | ¶3 | ¶3 ✓ |

So S861's `paragraph 1` is the single off-by-one among the rows I re-opened: the same rule that makes S863/S865/S867 "¶2" makes tango "¶2", not "¶1". Registry row (SOURCES.md:816) and Gate row (lessons/round-71.md:19) both carry `¶1`. One-cell fix in each; the span itself is correct and admitted.

Adjacent (outside my five, flagged for the row reviewer): S866's 2024 capture interposes a nomination-file block before the narrative (`P1 Talchum … Nomination file No. 01742 …`, then `Inscribed in 2022 (17.COM)`, then the narrative), so its `¶1` is only true if that block is treated as chrome — inconsistent with the S863/S865 convention. Not graded here.

## What else the re-open confirms

- **Live UNESCO walls persist.** `ich.unesco.org/en/RL/tango-00258` and `…/carnival-of-oruro-00003` both returned the "testing whether you are a human visitor" frame today (support IDs 5619449045446617541 / 5619449045439775796). The Gate's reject-sweep statement ("ich.unesco.org live CAPTCHA walls … flip: Wayback captures of the same elements, used") is accurate, and both named captures resolve to real content (not CAPTCHA frames).
- **S873 can never have a capture.** SEP serves `meta-robots: noarchive`; the registry correctly cites it live-only.
- **S868 is live-only** (no capture in the registry row) and the live page is stable (ABT `meta-article:modified_time: 2018-06-07`).
- **Word bound.** All five quotes are ≤25 words (15 / 10 / 10 / 10 / 6), as the Gate header claims.
- **Entry prose fidelity for the five rows** (spot-checked against the fetched text): S861 "music, dance and poetry … embodied identity … cultural dialogue" ✓; S864 "four kilometres … twenty hours" ✓ (entry omits the 28,000/10,000/50-group figures, which the source also carries); S868 "foot positions standard, arm positions diverge by school" ✓; S871 "karaṇas combine into mātṛkās and aṅgahāras" ✓ ("Two Karaṇas will make one Mātṛkā, and two, three, or four Mātṛkās will make up one Aṅgahāra"); S873 had no body prose at my measurement (header citation only — see §Two predicate observations for the concurrent edit).

## Counting commands re-run

Frozen claim-C command from `reports/round-71/claims.json` (`counting_command`, verbatim):

```
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l; find corpus/knowledge -type f -name '*.md' | wc -l; grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md; python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md; test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md
```
```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
cited-lines-exit=0   entry-exit=0
```

Counter script:

```
python3 -B reports/round-71/accept-c.py --lands HEAD
LEG PASS ENTRY / COUNTS (culture-material=36 corpus=243) / CITED (13) / ROWS / USEDBY-PATHS / CITED-LINES (exit=0) / SWEEP (single owner)
ACCEPT-C-71: PASS
```

Independent re-derivation (find, not `os.listdir`): culture-material 36 (maxdepth 1 = all), corpus 243, nested `.md` below partitions = 0 → the two counting styles agree. Before-state from base `acc2d614`: registry 784, culture-material 35, corpus 242 (matches `telemetry/controls-c.txt` and the claim's `before`). Deltas: +13 registry rows (= S861-S873, no extras), +1 partition file, +1 corpus file.

## Two predicate observations (not FAILs of claim C)

1. **`CITED` leg is header-blind.** It runs `TOKEN_RE.findall` over the whole entry, so the `- source:` header block counts. Per-row body mentions at my measurement: S861-S867 and S869-S872 appear in body prose (S868 once, line 37); **S873 appeared 0 times outside the header** — cited only in the `- source:` list (line 15) and alluded to in *Calibration shelf* ("SEP's entry is tier B") without the id. A concurrent sibling edit landed mid-run (uncommitted, line 116: `… not a historical authority on any specific tradition (S873).`), so S873's body count is now 1. Either way the leg is not load-bearing — 12 of 13 rows are body-cited independently of the header — but as written the leg would pass an entry whose citations exist only in `- source:` lines.
2. **Capture provenance is not in the entry.** The entry's `- source:` lines for S861/S864 give only the CAPTCHA-walled live URLs; the readable copy (the Wayback timestamps) exists only in `SOURCES.md`. A 180-day recheck following the entry alone hits the wall. Cheap fix: append the capture URL to those two `- source:` lines.

## Verdict

Claim C survives the re-open on evidence: all five assigned spans are verbatim present at the cited URLs/captures, the counter and the frozen counting command both pass at HEAD, and the count deltas match the declared before/after. The defects found are anchor-level, not source-level: **S861 `¶1` → `¶2`** (real, must be corrected in `SOURCES.md:816` and `lessons/round-71.md:19`), and label drift on **S871** (say *Karaṇas* section, ¶30-34) and **S873** (say lead paragraph, before §1).

## Remaining unknowns

- Whether the S861 `¶1` was copied from the wave-1 scout note or introduced at Gate/registry write time — not decidable from the lane; wave-1 `ScoutOpenSourcesC.md` records no paragraph indices, so the drift was introduced when the Gate/registry rows were written.
- S866's `¶1` (outside my five) needs the same convention test by the row reviewer.
- No semantic-server route was used (this is prose-source verification, not code navigation); all location claims are exact-substring evidence on fetched bytes, not inference.
