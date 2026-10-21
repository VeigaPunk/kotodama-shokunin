# ReviewLessonGate — round-50 falsify, C/Gate seat

**Item attacked:** `corpus/lessons/round-50.md` → `## Gate` at landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (landed bytes only; the working tree is dirty with post-landing falsify edits and was **not** used as evidence).
**Verdict: HOLDS** (22/22 bullets pass the required contract), with **2 MEDIUM** and **4 LOW** findings, all locator/route defects, none of which falsify a quote.

Method: private clone `git clone -q --shared … /tmp/r50gate-4180537` → `git checkout 1c779e4a`; every Gate URL re-opened live this session (2026-10-21) with `curl`; PDFs rendered/read via `pdftotext`/`pdftoppm` (poppler, pre-installed); no installs, no lane writes, no jj/git mutation in the lane. Temp clone deleted after the run.

---

## 1. Required contract, row by row

For every bullet S048–S069 the Gate must carry (a) a URL, (b) access date `2026-10-21`, (c) a verbatim quote ≤25 words, (d) a location matching its `corpus/SOURCES.md` row, (e) a named build seat whose report carries the quote.

| row | URL | date | quote ≤25 w | verbatim at stated location | location ⊆ SOURCES anchor | quote in named seat report |
|---|---|---|---|---|---|---|
| S048 | ✓ | ✓ | 9 | ✓ | ✓ | ✓ `ScribeSec01Register.md` |
| S049 | ✓ | ✓ | 12 | ✓ | ✓ | ✓ `ScribeSec11Decision.md` |
| S050 | ✓ | ✓ | 18 | ✓ | ✓ | ✓ `SrcZederDomestication.md` |
| S051 | ✓ | ✓ | 16 | ✓ (Abstract) | ✓ | ✓ `SrcSherratt.md` |
| S052 | ✓ | ✓ | 13 | ✓ (p. 19 image) | ✓ | ✓ `SrcEvansPritchard.md` |
| S053 | ✓ | ✓ | 24 | ✓ (Texte intégral ¶1) | ✓ | ✓ `SrcHerskovits.md` |
| S054 | ✓ | ✓ | 15 | ✓ (p. 1244 image) | ✓ | ✓ `SrcHardin.md` |
| S055 | ✓ | ✓ | 25 | ✓ (PDF p. 15) | ✓ | ✓ `SrcOstrom.md` |
| S056 | ✓ | ✓ | 10 | ✓ (Abstract, p. 85) | ✓ | ✓ `ScribeSec09Relations.md` |
| S057 | ✓ | ✓ | 17 | ✓ (Description ¶1) | ✓ | ✓ `SrcGalatyJohnson.md` |
| S058 | ✓ | ✓ | 19 | ✓ (y5115e08 item 2) | ✓ | ✓ `SrcFulani.md` |
| S059 | ✓ | ✓ | 19 | ✓ (ingress ¶ under H1) | ✓ | ✓ `SrcSamiReindeer.md` |
| S060 | ✓ | ✓ | 14 | ✓ (PDF p. 4) | ✓ | ✓ `SrcMongolFiveSnouts.md` |
| S061 | ✓ | ✓ | 21 | ✓ (ch. 8 Overview ¶1) | ✓ | ✓ `SrcYak.md` |
| S062 | ✓ | ✓ | 22 | ✓ (Description sent. 3) | ✓ | ✓ `SrcUnescoGer.md` |
| S063 | ✓ | ✓ | 15 | ✓ (Description ¶2) | ✓ | ✓ `SrcBedouin.md` |
| S064 | ✓ | ✓ | 13 | ✓ (lines 130–142) | ✓ | ✓ `SrcDumuzi.md` |
| S065 | ✓ | ✓ | 11 | ✓ (IR084700 gloss) | ✓ | ✓ `SrcPeku.md` |
| S066 | ✓ | ✓ | 9 | ✓ (EA004 Description) | ✓ | ✓ `SrcPeku.md` |
| S067 | ✓ | ✓ | 21 | ✓ (Abstract) | ✓ | ✓ `ScoutCalibrationRegistry.md` |
| S068 | ✓ | ✓ | 25 | ✓ (PMC8214430 Intro ¶1) | ✓ | ✓ `SrcAndeanCamelids.md` |
| S069 | ✓ | ✓ | 22 | ✓ (decision sent. 4) | ✓ | ✓ `SrcUnescoTranshumance.md` |

Word counts: max 25 (S055, S068), then S053 = 24 — inside the ≤25-word rule carried from `corpus/lessons/round-49.md:25` (`Quotes are verbatim, ≤25 words, with their location.`) and required by `corpus/SOURCES.md:8-9` (the lesson's `## Gate` "holds each row's URL, access date and verbatim quote"). All 22 bullets carry `accessed 2026-10-21`. All 22 bullet URLs equal the URL in their SOURCES row (programmatic `url_ok` check, 22/22).

### Spot evidence (verbatim re-fetches, this session)

```
$ curl -sS https://www.fao.org/4/y2647e/y2647e02.htm   # S048
  …Where human population densities are very low, i.e. where hunting-gathering is relatively easy,
  there is little or no impetus to herd animals.          (heading: CLASSIFYING PASTORAL SYSTEMS)
$ curl -sS https://www.fao.org/4/y2647e/y2647e08.htm   # S049
  Tenure is thus divided by both ecology and the potential for agriculture.
                                                       (heading: LAND TENURE AND THE COMMON PROPERTY RESOURCES DEBATE)
  SOCIAL STRUCTURES → "A key aspect of pastoral systems is the strong relationship between wealth in livestock and labour."
$ curl -sS https://sametinget.se/renmarken              # S059
  <h1 id="upperContentH">Renmärken</h1><div class="ingress"><p>Ett renmärke är kombinationen av snitt på både höger och vänster öra. Renmärket talar om vem som äger renen.</p>
$ curl -sSL http://web.archive.org/web/20260605210113/https://etcsl.orinst.ox.ac.uk/section5/tr532.htm   # S064
  <a name="para15" href="c532.htm#line130"><sup>130-142</sup></a>"Every night\nyour count is made and your tally-stick put into the ground, so your herdsman…
$ curl -sSL http://web.archive.org/web/20260103060250/…00872   # S062
  …It is light enough for nomads to carry; flexible enough to fold and pack; and sturdy enough to be dismantled and reassembled.
$ curl -sSL https://d-nb.info/1152169939/34 ; pdftotext   # S060 (p. 4)
  …which is an aggregate of the “five snouts” represented by horses, yaks/cattle, camel, goats and sheep (National Statistical Yearbook 2013, p. 212).
$ curl -sS https://www.ahdictionary.com/word/indoeurop.html   # S065
  Oldest form <i>*pek̑u‑</i>, becoming <i>*peku‑</i> in centum languages.   (byte-equal to the Gate quote incl. combining circumflex + U+2011 hyphens)
```

## 2. MEDIUM findings

### M1 — S058's bullet URL does not serve its quote (`corpus/lessons/round-50.md:43`)

The bullet is `S058 — https://www.fao.org/4/y5115e/y5115e00.htm — accessed 2026-10-21 — chapter y5115e08, item 2 (baartol): "Typically, seasonal migration starts with the beginning of the rains in May or June and leads towards the west."`

The URL is the book's front matter. Its own bytes do not contain the quote:

```
$ curl -sS https://www.fao.org/4/y5115e/y5115e00.htm   →  7 108 bytes, TOC only
  quote present: False
```

The quote is in the chapter file `https://www.fao.org/4/y5115e/y5115e08.htm` (verified: list "There are four types of pastoral movement:", item 2 = *Seasonal migration (baartol)*, quote = its last sentence). The TOC does link it (`href="y5115e08.htm#bm08"`), so the bullet is one click from correct — but under the SOURCES contract the Gate's URL is supposed to be the page the quote sits on, and the row's own anchor (`corpus/SOURCES.md:87`, "chapter y5115e08 item 2 (baartol); chapter y5115e0d") shows the row's URL is also the front matter. `SrcFulani.md:30` and `:54` already carry the chapter URL.

**Smallest fix:** in the S058 row and bullet, replace the row URL with `https://www.fao.org/4/y5115e/y5115e08.htm` (append-only ⇒ a superseding row, as with S060's pages), or keep the front matter and put the chapter URL in the bullet next to the locator. Quote, date, seat and location are all correct — this is a URL/locator defect only.

### M2 — the Gate header's re-fetch claim has no landed evidence pointer, and the cited receipt is absent from the landed commit (`corpus/lessons/round-50.md:3,30-31`)

Line 31: `S048 and S049 quotes were re-fetched by the integrator and matched under the named headings.` The only pointer the lesson gives for that receipt is line 3: `source: … reports/round-50/validation.json (acceptance receipt)`.

That file is **not in the landed commit**:

```
$ git ls-tree 1c779e4a reports/round-50/
100644 blob 52aa5cbf…  reports/round-50/claims.json
100755 blob bec4549…  reports/round-50/jj-colocation-probe.py
100755 blob c3a05bbd…  reports/round-50/run-validation.py
040000 tree 23a835d…  reports/round-50/separability
040000 tree 8c3ef1a…  reports/round-50/telemetry
   # no validation.json
$ git ls-files reports/round-50/ | grep validation      → (nothing; it exists only as an untracked working-tree file)
```

No wave report records an integrator re-fetch of S048/S049 either (`grep -rn "re-fetch" .ufo/waves/round-50/build/` hits only `SrcBedouin.md:196` and `SrcFulani.md:19`, both self-reports about their own fetches).

**The claim itself is true** — I re-fetched both FAO pages independently: the S048 quote sits under heading `CLASSIFYING PASTORAL SYSTEMS` (next heading `PASTORAL SPECIES`), the S049 quote under `LAND TENURE AND THE COMMON PROPERTY RESOURCES DEBATE`; both match verbatim. So this is a *provenance-pointer* defect, not a falsification: a reader of the landed tree cannot check the re-fetch claim because the cited receipt is not in it.

**Smallest fix:** land `reports/round-50/validation.json` with the round (it must land with the bytes that produced it — see the wave's own R50-M4), or drop the "re-fetched by the integrator" clause from the Gate header and keep the two bullets' own access dates.

## 3. LOW findings

- **L1 — S051 locator overstates the cut point (`corpus/lessons/round-50.md:36`).** The bullet says `Abstract, opening sentence: "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction"`. The abstract's opening sentence is `Andrew Sherratt is perhaps best known for the concept of a 'Secondary Products Revolution', which stressed that the 'primary' pattern … was followed by a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction.` The quote is a mid-sentence fragment with no ellipsis marking the cut; `SrcSherratt.md:66-70` says so honestly ("The fragment starts mid-sentence"). Fix: `Abstract, opening sentence (fragment after "was followed by")`, or add `…` before the fragment. (The Introduction carries a *different* wording — "a more diversified exploitation **for their secondary products** …" — so the abstract wording is uniquely the Gate's; the quote is correct.)
- **L2 — S054's locator adds a word the printed heading lacks (`corpus/lessons/round-50.md:39`, `corpus/SOURCES.md:83`).** Rendered p. 1244 (`pdftoppm -f 2 -l 2 -r 130`) prints the section head as **"Tragedy of Freedom in a Commons"**, with no leading "The"; both the row and the bullet write "§The Tragedy of Freedom in a Commons". Quote, page and section are right. Fix: drop "The" from the heading in both places (append-only row ⇒ superseding row for SOURCES.md).
- **L3 — S052's route note is stale (`corpus/lessons/round-50.md:37`).** The bullet says `(archive.org unreachable; …)`. As of this session `https://archive.org/details/nuerdescriptiono00evan` answers **HTTP 200** (item metadata); only the restricted full text is blocked (`/download/…_djvu.txt` → **401**, borrow-gated). The duke.edu mirror is genuinely open and did serve the scan (PDF page 43 = printed p. 19, confirmed by rendering the page image: `INTEREST IN CATTLE 19`). Fix: `archive.org reachable, full text borrow-restricted (401)`.
- **L4 — S062's route note is UA-dependent (`corpus/lessons/round-50.md:47`).** The bullet says `(live page CAPTCHA)`. True for a bare `curl/8` UA (JS challenge page, no quote), false for a browser UA (HTTP 200, 153 115 bytes, quote present). Both Wayback captures named in the SOURCES row (`20241219152138`, `20260103060250`) and the live page carry a byte-identical Description (I diffed all three) — the row's "byte-identical description" claim **holds**. Fix: `(live page served under a browser UA; plain-curl gets a JS challenge)`.
- **L5 — adjacent to the Gate: S060's row carries wrong bibliographic pages (`corpus/SOURCES.md:89`).** The row says *Natural Hazards 92(Suppl 1):95–107*. Crossref says volume 92, issue **S1**, pages **165–181**, published 2017-12-13:
  ```
  $ curl -sS https://api.crossref.org/works/10.1007/s11069-017-3128-4 | …
  container: ['Natural Hazards'] | volume: 92 | issue: S1 | page: 165-181 | published: 2017-12-13
  ```
  The Gate bullet for S060 (quote/URL/location) is unaffected; the row's citation cell is wrong. (Independent corroboration of the wave's own `ReopenS060` finding.)

## 4. Notes on the cross-check the assignment asked for (6 quotes vs `Src*.md`)

I ran the seat cross-check over **all 22** bullets, not 6, with two passes: (a) exact substring, (b) whitespace/quote-mark normalised. Result: **22/22 quotes are present in the seat report named in their bullet** (S053's is a `>` block-quote split across two lines, so only the normalised pass matches it — a real trap for a naive grep-based checker).

Coverage caveat worth recording: **3 of the 22 quotes are not in any `Src*.md` file** — S048 (`ScribeSec01Register.md`), S049 (`ScribeSec11Decision.md`), S067 (`ScoutCalibrationRegistry.md`). A checker restricted to `Src*.md` would silently cover only 19/22 rows. S056's quote does appear in a `Src*` file (`SrcKhazanov.md:169`) but there as a longer variant with a *different* URL (`https://www.chungara.cl/Vols/2019/AOP/AOP-KHAZANOV.pdf`, "abstract, sentence 2 (PDF p. 1)"); the landed row and the Gate use the SciELO PDF opened by `ScribeSec09Relations` — the same article, two routes, so the quote text is corroborated from both.

Two content notes on the "Grounds …" clauses (not quote defects):
- S048's bullet claims it grounds "conditions, typology, species count and stage-ladder refutation", but its single quoted sentence only carries the *conditions* clause. The other three are real and present in the same source (verified: "Any classification of this type must be treated as a simplification"; "herders seem to manage between two and four species of roughly equal importance simultaneously."; "In most parts of the world, Africa excepted, agriculture seems to have started earlier than pastoralism." / "Pastoralism was seen as an evolutionary stage in human history"), and the row's anchor names the matching sections — so the claim is supportable from the row, just not from the quoted sentence alone.
- S049's bullet claims it grounds "§8 and the labour-wealth link (§Social structures)"; the quoted sentence is the tenure sentence. The labour-wealth sentence ("the strong relationship between wealth in livestock and labour") is in §Social Structures on the same page and is named in the row's anchor, but it is not the Gate's quote. Same shape as S048.

## 5. Residual risk / verification gaps (honest)

- Three Gate bullets quote pages that are **bot-walled or archive-mediated**; I verified the quoted bytes through a text-rendering proxy (`r.jina.ai`) or the named Wayback capture, not through the same route the seat used: **S051** (Springer serves a "Client Challenge" page to plain curl), **S053** (OpenEdition serves an Anubis proof-of-work challenge — 8 `anubis` markers in the served HTML), **S062** (UNESCO CAPTCHA for plain curl; both named Wayback captures verified). The quoted strings match the served content exactly, but a re-opener following the same raw route gets a challenge, not text.
- **S052's PDF text layer is not trustworthy** even though the Gate quote is: `pdftotext` renders the sentence as `…relationships in — terms of cattle.` with a spurious em-dash; the rendered page image (PDF p. 43) shows `relationships in / terms of cattle.` with no dash. The Gate quote matches the **printed page**, so the Gate is right and the text layer is noisy — but any automated re-check that greps `pdftotext` output will report a false miss on S052.
- I did **not** adjudicate two claims that belong to sibling seats and are already logged in the wave's carried list: S050's row anchor "paragraph 3" (its Ganj Dareh quote is prose ¶4 in the PMC rendering) and S064's row parenthetical "Grain's third speech" (the capture shows the `130-142` label and the quoted paragraph; the speech ordinal I did not verify). The Gate's own S064 locator ("lines 130–142") **is** verified.
- The `## Gate` header's opening claim "Every row S048–S069 was opened on 2026-10-21 by the round-50 build seat named in its bullet" holds for the seats named; note that `SrcSamiReindeer.md:31` also opened the same FAO `y2647e02` URL with a *different* candidate row and anchor set, so the URL has two seat provenance trails while the quote itself traces to `ScribeSec01Register.md` only.
- I checked the entry's own use of the cited rows only where a quoted sentence was load-bearing (S048 conditions/typology/species/stage-ladder, S049 tenure/labour-wealth, S050 management-before-morphology): all present in the cited pages.

## 6. Verdict

**HOLDS.** Every S048–S069 bullet in the landed `## Gate` carries a URL, the access date 2026-10-21, a verbatim quote of ≤25 words, and a location that matches its `corpus/SOURCES.md` row; I re-opened all 22 sources this session and confirmed each quote byte-for-byte at the stated location, and each quote in the named build seat's report. The defects are locator/route precision (M1 S058 URL vs chapter, M2 missing landed receipt for the re-fetch claim) and four low locator/route slips (L1–L4) — none changes a quoted word. Smallest fixes are stated inline above.
