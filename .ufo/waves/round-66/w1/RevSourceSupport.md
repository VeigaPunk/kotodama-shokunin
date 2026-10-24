# RevSourceSupport — blind per-row support sample (claim C)

Seat: `L1-kotodama-r66.RevSourceSupport` · round 66 v2 · lane `kotodama-shokunin`
Base: `94209e8f80969dbac48d56c5d0e2e623635b8616` · sample drawn 2026-10-24, before any row was read.

## 0. Sample pre-registration (blind)

Sample frame: S777–S800 (24 ids). Seed: `sha256(reports/round-66/claims.json)` =
`18fa9803b6b13052e1728a23fd40fda4602710396262d6e037457655f5028d6f`; `random.Random(int(seed,16)).sample(ids,6)`.

**Sampled ids: S777, S784, S790, S792, S794, S795.**
The seed and id list were fixed and printed while `.ufo/waves/round-66/rows/` was empty
(`find … -type f` → 0), so no row content influenced the draw.

State at sample time: all six were unwritten; five landed inside this window and S795 landed at the end of it.
Final tally: **2 support, 3 defects (2 overreach, 1 unsupported), 1 row absent**.

| id | verdict | one-line ground |
|---|---|---|
| S777 | **unavailable** (row absent) | topic path itself fails: no UNESCO ICH element whose page states an incense claim (§2) |
| S784 | **support**, weak anchor | element 01207 page and its capture both carry the inscription line; capture replayed by this seat |
| S790 | **support**, bullet adds "court" | V&A *Ownership & Use* note supports every teaches clause; "court" is not in the source |
| S792 | **overreach** | anchor covers only the Aztec clause; teaches conflates a death metaphor into "palace aromas marked breath and soul", and strips the source's hedge |
| S794 | **overreach** | "Parisian" and "curial etiquette" occur 0× in the source |
| S795 | **UNSUPPORTED** | the anchor quote is not what Bedini wrote — "passage of" was substituted for "k'o (quarter) of"; the cited capture is a different page that cannot replay it |

## 1. Verdicts — the five sampled rows that landed

### S790 — SUPPORT (with one bullet overreach)
Row: `.ufo/waves/round-66/rows/ScoutRow07/row-S790.txt` (V&A O78794, "Pair of gloves").
Independent fetch: `https://collections.vam.ac.uk/item/O78794/pair-of-gloves-unknown/` → HTTP 200,
52,730 bytes. Anchor quote found verbatim (`"Recipes for scenting gloves survive from the 17th
century using ingredients such as musk, ambergris, floral extracts and aromatic spices."`).
Located context (same page, *Ownership & Use* block): "In an age when personal hygiene involved the
masking of body odours rather than washing them away, gloves were often perfumed. Recipes for
scenting gloves survive…"; object description: "Pair of brown **doeskin** gloves, England, **1660s**".
Capture replay: `web.archive.org/web/20260108224147id_/…` → HTTP 200, 52,148 bytes, quote present at
char 3139 — the capture is a real replay, not a shell.
Teaches cell (`row-S790.txt` cell [6], 258 chars): every assertion — 1660s, doeskin, musk/ambergris/
floral extracts/aromatic spices, odour-masking — is in the located context. The cell even carries the
correct hedge ("period practice, not confirmation this pair retains perfume").
Overreach (low): the BULLET line places the practice "**at the 1660s English court**". The source says
"someone well-born and very wealthy" and never says *court*. Drop "court" or quote the class language.

### S793 (out of sample, cited only as evidence of a gap) — not scored
`scent-perfume` registry sibling; its capture also replays correctly (200, quote present). Its teaches
cell is 256 chars — see §3.2.

### S794 — OVERREACH (two assertions absent from the source; cells over length)
Row: `.ufo/waves/round-66/rows/ScoutRow09/row-S794.txt` (Centre de recherche du château de Versailles,
article964).
Independent fetch: live HTTP 200, 51,511 bytes (matches the row's own VERIFY figure). Quote verbatim:
"les gantiers-parfumeurs fabriquent les gants parfumés, dont le succès est à son apogée à la cour de
Louis XIV". Capture `20260608021222id_` replayed earlier in this window: HTTP 200, 50,770 bytes, quote
present (`/tmp/c794.html`).
Supported by the located passage: "Ce sont les gantiers qui s'emparent de ce savoir-faire et
parviennent à s'en arroger le **monopole**"; "…fabriquent les gants parfumés … les **eaux de senteur**
et tous les **cosmétiques** tels que les poudres, les pommades, les rouges, les fards…"; "dont le
succès est à son apogée à la cour de Louis XIV".
**Unsupported assertions in the teaches cell (cell [6]):**
1. "**Parisian** glovers" — the page contains `parisien*` **0 times**; the five `Paris` hits are a photo
   credit ("© Photo Les Arts Décoratifs, Paris/Jean Tholance") and an object caption ("Flaconnier,
   Paris, 1755-1756"). The guild toponym is not in the source. Delete "Parisian" or add a source that says it.
2. "courtiers whose **curial etiquette** demanded them" — `étiquette` occurs **0 times** on the page.
   The page describes production and commercial success, not a court demand-code. This is exactly the
   overreach class the entry is meant to avoid: an interpretive motive welded onto a production fact.
Neither defect is catchable by the counter (see §3.2); both would ship into the entry through the
BULLET line ("Parisian glovers monopolized…").

### S784 — SUPPORT, but the anchor is inscription boilerplate
Row: `.ufo/waves/round-66/rows/ScoutRow04/row-S784.txt` (UNESCO element 01207).
Independent fetch of the element page: HTTP 200, 155,824 bytes, `perfume` ×16, and the located line
"Inscribed in 2018 ( 13.COM ) on the Representative List of the Intangible Cultural Heritage of Humanity";
the element's H1 is "The skills related to perfume in Pays de Grasse: the cultivation of perfume plants,
the knowledge and processing of natural raw materials, and the art of perfume composition" — which is what
the teaches cell restates (cultivation / processing / composition, 2018, 13.COM).
Capture replay by this seat (`http://web.archive.org/web/20260906234122id_/…-01207`): **HTTP 200, 152,114
bytes, `Grasse` ×12, `perfume` ×16, inscription line present** — a real replay; the `http://` scheme worked
while `https://` was refusing connections. The row quotes "(13.COM)" where the page serves "( 13.COM )":
whitespace-only difference, acceptable.
The row's own VERIFY is honest about the anti-bot gate ("TSPD/JS anti-bot challenge … quote in body text N
for curl, Y via real-browser render"), which matches what this seat saw on other `ich.unesco.org/en/RL/*`
paths. **Weakness:** the anchor quote is the generic inscription sentence printed on every Representative
List element page — it identifies the *date and list*, not the Grasse content. The teaches cell's content
clauses ride on the element title, not on the quoted sentence, so the anchor demonstrates less than the
teaches claims. Acceptable, but do not cite this row for "what the listing says the skills are" unless the
title is in the anchor path.

### S792 — OVERREACH (conflation, hedge-stripped, anchor covers one clause)
Row: `.ufo/waves/round-66/rows/ScoutRow08/row-S792.txt` (Newman & Houston, *Paraíso perfumado*, Boletín
OPCA #22, Universidad de los Andes, 2022).
Independent fetch: live HTTP 200, 184,045 bytes; anchor quote verbatim in the Aztec banquet passage:
"Es posible que las flores fragantes sean un 'plato' inicial en un banquete elaborado, como lo registraron
observadores españoles con respecto a los palacios aztecas de Centroamérica en el siglo XVI (Sahagún, 1959,
Book 9: 335-336)".
Clause by clause against the article:
1. "fragrant flowers recreated Flower Mountain paradise" — **supported**: "las flores particularmente
   fragantes eran uno de muchos elementos diseñados para evocar el paraíso floral del reino de la realeza …
   recreaban la **Montaña de las Flores** para el rey".
2. "**Maya palace aromas marked breath and soul**" — **not supported**. The only breath material is the
   death expression: "a veces se describe la muerte usando una expresión que se refiere a la expiración de
   una fragante flor blanca, sak nikte' … como metáfora para el aliento de los difuntos" — a funerary
   metaphor for the breath of the dead, not palace aromas marking breath and soul. The teaches welds two
   passages into one claim; that context contains no `alma`.
3. "incense and breeze carried scent" — supported: "espacios aromatizados con flores y ramos, perfumes
   dulces e incienso fragrante"; "El viento, la música y las fragancias impregnaban los tronos".
4. "Sahagún records fragrant flowers as an opening course" — supported **only as a hedge**: the article says
   "**Es posible que** las flores fragantes sean un 'plato' inicial". The teaches drops "it is possible".
   Hedge-stripping on a primary-text inference is the calibration failure this axis exists for.
5. BULLET "…and **coded Maya kingship**" — gloss beyond the text: the article says flowers evoked the
   paradise of the royal realm for the king; `kingship`/`gobernante` = 0 hits, `rey` ×5.
6. Anchor coverage: the quote sits on the **Aztec** clause while the teaches is mostly **Maya**; no counter
   leg compares anchor↔teaches topical alignment (§3.3), so this passes `RESTATE` today.
Tier: A for a museum research bulletin is defensible for "the authors' own argument", but the piece is an
interpretive essay, not peer-reviewed. Lane precedent (S127, S190 in `corpus/SOURCES.md`) is to annotate
such grades with a tier note; add one, or grade B.

### S795 — UNSUPPORTED: the anchor quote is altered, and the capture cannot replay it
Row: `.ufo/waves/round-66/rows/ScoutRow10/row-S795.txt` (Bedini, "The Scent of Time", *Trans. Am. Phil.
Soc.* n.s. 53(5), 1963, JSTOR 1005923; cited live URL is an `archive.org/download/wikipedia-scholarly-
sources-corpus/…zip/10.2307%252F1005923.pdf` mirror).
Independent fetch of the cited PDF: HTTP 200, `application/pdf`, 8,751,290 bytes; `pdftotext -layout` yields
51 pages of OCR. The passage is there (`b795L.txt`, the two-line poem introducing the incense-stick
section):

> By burningincense[we] knowthe **k'o (quarter)of the** night, With graduated candle [we] confirmthe tally of
> the watches.

The row's anchor cell reads: `"By burning incense [we] know **the passage of** the night, With graduated
candle [we] confirm the tally of the watches."`
**"the passage of" is not in the poem.** The translator wrote "the k'o (quarter) of the night"; "passage of"
comes from a *different column* of the same page ("…to measure the passage of timeby the progressof the
burningincense"). The row silently swapped a technical term (k'o, a quarter-watch) for a phrase lifted from
adjacent body text. That is a fabricated anchor quote, and no counter leg can see it (§3.6).
Teaches cell, clause by clause:
- "fire clocks replacing clepsydrae when water supplies froze or failed" — **supported**, though the source's
  cause is drought: "The country was beset by a great drought … the wells and springs dried up and were
  exhausted … It was impracticable to use the customary water clocks or clepsydrae".
- "incense sticks marked into intervals" / "seals burned along template paths" — supported (incense seals,
  hundred-gradation seals, seals burned along laid-out tracks).
- "hanging cords releasing **gong balls**" — **not supported**: the source's device is "an incense stick to
  which a **small bell** was attached by a string at the designated point. When the incense had burned down
  to the string, the string parted and the bell fell". The single `gong` hit in the PDF is an unrelated
  passage about a metal gong announcing the hour. Plural "gong balls" is an embellishment.
- "across East Asia" — acceptable (China, Japan, Korea throughout).
Durability (R65-D1 class): the row's own CAPTURE cell admits "no Wayback capture exists for this
archive.org download URL" and cites instead the **JSTOR landing page** (`/stable/1005923`, metadata only,
captured 20251011060403). That page does not contain the quote and never will — a re-opener cannot verify
this row from its capture. The live URL is also a third-party IA corpus mirror with a double-encoded
`%252F` path, not a stable publisher URL.
Teaches cell 249 chars (>240); scope 58 (ok).

## 2. The one sampled row that never landed — dependency finding

### S777 — assigned topic is not backed by an official listing; do not let ScoutRow01 anchor on Majlis
Evidence gathered independently of the row:
- `https://ich.unesco.org/en/lists?text=incense` (HTTP 200): the tag facet lists **"Incense (7)"**, i.e.
  incense is a keyword on seven elements, not an element.
- There is **no standalone UNESCO ICH element** for Arabian incense/bakhoor/frankincense; the closest is
  "Majlis, a cultural and social space" (nom. 01076, inscribed 2015, Oman/Qatar/KSA/UAE), where incense
  (dukhoon) appears only as an associated practice in UNESCO's own caption material.
- I fetched the Majlis element page itself (`https://ich.unesco.org/en/RL/majlis-a-cultural-and-social-space-01076`,
  HTTP 200, **155,992 bytes**) and scanned the served HTML: `incense` **0**, `dukhoon` **0**, `fragran`
  **0** occurrences. The description text is about sitting places, coffee/fire and conflict resolution.
  → An anchor quote about incense **cannot** be cut from that page. If S777 lands with a Majlis URL plus an
  incense quote, it is fabricated or lifted from the nomination-file PDF (a different URL — the source cell
  must then be the PDF, with the PDF's own capture, and the durability caveat of R65-D1 applies).
- Oman's "Land of Frankincense" is a **World Heritage** property, not an ICH element; citing it as an ICH
  listing would be a category error.

**Rule for the L1:** if S777 lands with a Majlis URL plus an incense quote, reject the row — the quote is
not on that page. The only honest S777 sources are the nomination-file PDF (different URL, its own capture,
R65-D1 durability caveat) or a replacement topic with a real official/scholarly page.

## 3. Instrument findings (claim C's own counter, `reports/round-66/accept-c.py`)

### 3.1 MED — CAPTURE leg never replays a capture (R65-D1 class re-opened)
`accept-c.py:53-54` defines `CAPTURE_RE` and the leg at `:296-311` accepts a row if the source cell merely
*contains* a `web.archive.org/web/\d{14}` string (or a "no-capture" marker). It never fetches the capture,
never checks its timestamp freshness, and never checks that the archived body contains the anchor quote.
The defect that round 65 routed (a committed capture replaying 404 while CDX said 200) would pass this leg
unchanged. Counter-evidence from this seat: two of my three successful replays needed `--compressed`
(the `id_` endpoint serves gzip; an uncompressed read looks like binary noise and any naive replay check
would report the quote absent). Today all three landed rows do replay — so this is an *instrument* gap,
not a present data defect. The review-only leg "blind per-row support" is the only place durability is
actually checked; it must not be waived.

### 3.2 LOW–MED — the ≤60-char scope and ≤240-char teaches caps promised to the scouts are unenforced
`ROWS` (`:192-214`) checks cell count, `kind`, tier ∈ {A,B}, status, opened date, used-by and extracts the
URL. It never measures cell [4] or cell [6]. Observed on the three landed sampled rows:

| row | scope len (≤60) | teaches len (≤240) |
|---|---|---|
| S784 | 52 | 209 |
| S790 | **65** | **258** |
| S792 | 35 | **260** |
| S793 (out of sample) | 50 | **256** |
| S794 | 56 | **264** |
| S795 | 58 | **249** |

4 of the 5 landed rows exceed the 240-char teaches cap (S784 is the only compliant one) and 1 of 5 exceeds
the scope cap. (S795 is 249 — see §1.) Because the caps are unenforced,
long teaches cells are where unsupported interpretive clauses (S794's "curial etiquette", "Parisian") ride
in. Either the caps are enforced in `ROWS` or the spec must stop promising them; leaving the promise while
the gate ignores it is a false stamp.

### 3.3 LOW — `RESTATE` is token-order matching and cannot see semantic drift
`:239-255` scores an entry bullet by in-order word overlap with the teaches cell and quote. A bullet that
repeats the quote's nouns in order but reverses or invents the relation between them passes. Confirmed
pattern: S790's bullet passes on tokens while adding "court", which the source does not say (§1).

### 3.4 LOW — tier A on a museum object record is defensible only for a narrow scope
`corpus/SOURCES.md` header: A = "primary or authoritative for that scope". S790 is graded A with scope
"1660s English perfumed-leather gloves and their scenting practice"; the anchor is the V&A's own
*Ownership & Use* note about its own object, so A holds only for "what this object is and what the museum
states about it". It must not be re-used as A for the general claim that 17th-century gloves were
perfumed. S793 (NHM explainer, B) and S794 (research-centre project page, B) are graded correctly.

### 3.5 HIGH — an out-of-frame row id exists on disk (S802) and `SET` cannot see it
`.ufo/waves/round-66/rows/ScoutReject02/row-S802.txt` opens **S802** — outside the frozen S777–S800
frame and outside the claim's "exactly 24" set. `corpus/SOURCES.md` currently holds neither `S801` nor
`S802` (grep count 0), so nothing is duplicated yet; the hazard is integration:
- `SET` (`accept-c.py:187-189`) only asserts that S777–S800 appear **exactly once each**. An extra S802 row
  is invisible to it, so a 25-row registry would still print `ACCEPT-C-66: PASS` — the "exactly 24 mined
  registry rows" wording of claim C has **no exact-count assertion** behind it.
- Integrating S802 also skips S801, leaving an id hole in the append-only sequence that later rounds will
  read as the baseline.
Recommendation: leave S802 out of this round's registry (its own scout is a reject seat; rejects belong in
`rejects.txt`), and if a 25th source is genuinely wanted, renumber it in a later round with its own
`opened` date. If it is integrated, `SET` must gain a `len(reg_by_id) == 24` / no-extra-new-id assertion.
Content/reproducibility note on the fragment (not scored, out of frame): the capture
(`20251115220917`, replayed over http from this host) is genuine — 80,218 chars of body text, `miasma` ×5,
`hospitals` ×17, anchor quote present — and the page does discuss hospital ventilation against miasma, so
the bullet's hospital clause is NOT the overreach I first suspected. The defect that remains is
reproducibility of the *live* cell: a plain curl GET to the live URL returned **HTTP 405** (1,363 bytes) on
2026-10-24, contradicting the fragment's "HTTP 200 via curl … quote in body text Y". A live-URL cell that
405s to a cold re-opener is the S753 durability class again; if S802 were ever integrated it would need the
405 declared in VERIFY, the way S784 declares its anti-bot gate.

### 3.6 HIGH — no leg checks the anchor quote against the source; S795 proves it
Nothing in `accept-c.py` fetches the source or the capture, so the quote cell is taken on trust. `RESTATE`
(`:239-255`) only compares *words the entry bullet shares with the quote and teaches* — a fabricated or
altered quote is self-consistent and passes. Demonstrated: S795 replaces the poem's "k'o (quarter) of" with
"the passage of" and passes every leg (cells count, kind, tier, status, opened, used-by, archive-URL shape,
token overlap). `CAPTURE` (§3.1) does not help because the only capture cited for S795 is a *different page*
(the JSTOR metadata landing page), which the leg accepts by shape.
Minimum fix for future rounds: a quote-fidelity check that fetches the capture (or PDF) with
`--compressed`, extracts text, and asserts the quote (whitespace-normalized) occurs; and require the capture
URL to be same-URL-normalized to the live URL, as the S795 row itself concedes it is not.

## 4. Residual risk / verification gaps
1. **1 of 6 sampled ids unscored** (S777 is absent from disk, with a pre-checked *negative* — no official
   listing whose page states an incense claim). Claim C's review-only leg "blind per-row support of the 24
   new sources" is satisfied for 5 of 6 only; S777 must be re-run or replaced.
   Of the 5 scored rows, **3 carry defects that would ship into the entry** (S795 fabricated quote fragment,
   S792 conflation/hedge-strip, S794 unsupported "Parisian"/"etiquette"), and 2 more need a bullet fix
   (S790 "court"; S784 weak anchor). S784 and S790 teaches cells are clean as written; their defects are in
   the anchor strength and the bullet respectively. On this sample the draft is **not ready to integrate**.
2. Sub-scope selection: row sources were fetched at my own chosen URLs; where a scout chose a different
   page on the same site (e.g. a Met essay vs a Met object record) my verdict does not transfer.
3. `web.archive.org` was intermittently unreachable from this host (repeated connection refusals/timeouts
   inside the window). Replays that did complete: S784 (over `http://`), S790, S793, S794, S802. `https://`
   refused while `http://` served 200 for the same capture, so a transient refusal must never be recorded as
   "capture absent" — re-probe both schemes before alleging a dead capture.
4. Tier grading for the remaining 18 rows, duplicate-host coverage (`HOSTS` ≥10) and the LINK leg were
   not audited here.

## 5. Tooling
No installs or upgrades; only `curl`, `python3` (stdlib) and the repo's own counter were used.
