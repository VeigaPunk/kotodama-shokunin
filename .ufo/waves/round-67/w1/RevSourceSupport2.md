# RevSourceSupport2 — blind support review of S811-S816 (r67, claim C)

Seat contract: for each of S811-S816, open the row fragment, re-fetch the live URL **and**
the archive capture, verify the anchor quote in body text, then judge whether the row's
`teaches` cell is supported (not merely quotable). Frozen artifacts read first:
`reports/round-67/claims.json`, `reports/round-67/accept-c.py`, `reports/round-67/telemetry/controls-c.txt`,
`corpus/QUALITY.md`.

- Fragments reviewed: `.ufo/waves/round-67/rows/ScoutRow04/{row-S811,row-S812}.txt`,
  `.ufo/waves/round-67/rows/ScoutRow05/{row-S813,row-S814}.txt`,
  `.ufo/waves/round-67/rows/ScoutRow06/{row-S815,row-S816}.txt` (all six present at 12:40Z; none absent).
- Method: `curl -sSL --compressed -A 'Mozilla/5.0 (X11; Linux x86_64)'` on live URL and on the row's
  `web.archive.org/web/<ts>id_/` capture; HTML stripped; quote searched verbatim in both bodies;
  teaches/bullet claims then searched as keywords/claims in the same body. Capture identity and
  URL uniqueness checked with accept-c.py's own `norm_url_q`/`row_urls`.
- No tool installs (curl + python3 stdlib only).
- `lsp` not used: the changed artifacts are Markdown corpus rows and a Python counter; no language
  server is the semantic authority for registry prose. All counter-side claims below are executed
  from `accept-c.py`'s own functions, not from text grep.

## Verdicts

| id | support verdict | one-line basis |
|---|---|---|
| S811 | **PASS with overstated wording (fix required)** | quote + provenance chain verified live and in capture; teaches/bullet harden the paper's hedge |
| S812 | **PASS** | quote and every teaches detail verified live and in capture |
| S813 | **FAIL — teaches contradicts the cited paper; drafted bullet would fail RESTATE** | paper concludes the mask has no proof of plague use and specimens likely were not protective; quote is 26 words; bullet has 2 in-order quote hits |
| S814 | **PASS on substance, tier + wording defects** | quote verified; "seeding iatrochemistry" is not in the source; teaches 246 chars; tier A questionable |
| S815 | **PARTIAL — three teaches specifics absent from the source** | 185 illustrations / first illustrated Nahua text / Aztec-native authorship verified; "1552", "New World", "body-ordered" are not on the page |
| S816 | **PASS (one low inference)** | quote + Sanggye Gyatso 17th-c. chart commission verified live and in capture; "teaching charts/curriculum" wording is inference |

## Per-id evidence

### S811 — Ebers papyrus (JMLA 2023, PMC10621680) — tier A, docs/paper `paper`
- Live `https://pmc.ncbi.nlm.nih.gov/articles/PMC10621680/`: HTTP 200, 156,319 B.
  Capture `20250227171945id_/...`: HTTP 200, 44,277 B decoded — **quote present in both**:
  "one of the oldest and most complete contemporaneous perspectives on Ancient Egyptian healing practices"
  (abstract and again in the body: "The Ebers Papyrus remains one of our oldest and most complete…").
- Teaches provenance is supported in the body: "Ebers obtained the papyrus from Edwin Smith… the
  American antiquities collector for whom the oldest and most complete Ancient Egyptian surgical
  papyrus was named"; "Smith purchased the medical papyrus in 1862"; "In 1872, Smith sold the papyrus
  to Ebers".
- **Defect (medium):** teaches says "the oldest near-complete witness" and the bullet says "Egypt's
  oldest complete healing witness". The source says *one of the oldest and most complete … perspectives*.
  "near-complete" occurs 0 times; the definite superlative + "complete" is a hardened hedge. RESTATE
  cannot see this (it only counts overlapping words). Fix: restore "one of the oldest and most
  complete" in teaches and bullet before lands.
- Tier A is defensible (peer-reviewed JMLA). Capture identity normalizes equal; no base URL collision.

### S812 — Galen (Internet Encyclopedia of Philosophy, `iep.utm.edu/galen/`) — tier A, docs
- Live: HTTP 200, 60,390 B; capture `20261001114120id_/`: HTTP 200 (21,152 B gzip, 34,300 B decoded)
  — **quote present in both**: "Galen traveled to Egypt (Alexandria) where he lived for perhaps five
  years (152-157)".
- Every teaches detail verified in the body: Smyrna/Corinth "Rationalist … Empiricist"; the autopsy
  quote ("physicians of that area instruct their pupils with the aid of autopsy"); "In 157 Galen
  returned to his hometown to become a surgeon to the gladiators"; "left for Rome" in 162; "Galen was
  made personal physician to Marcus Aurelius".
- Tier note (low): IEP is a peer-reviewed encyclopedia; registry precedent admits essay/reference-work
  `docs|A` (S125 Oxford Research Encyclopedia of Linguistics = docs A), so A is consistent. No action.
- Capture caveat (protocol, not row defect): the `id_` replay serves gzip; a reviewer who omits
  `--compressed` sees a binary blob with the quote absent. Verified present after decompression.

### S813 — Ruisinger, plague-doctor mask (NTM 2020, PMC8156585) — tier A, paper — **FAIL**
- Live: HTTP 200, 42,008 B; capture `20260728172941id_/`: HTTP 200 — quote present in both. But the
  anchor quote is the paper's *methods* sentence, 26 words:
  "contemporary textual and image sources in regard to protective clothing used in times of plague and
  the respective role of the beak-like part of the mask".
- **Semantic failure:** the paper's stated conclusion contradicts the row's teaches. Body: "The
  conclusion: the beak mask is not mentioned before the mid-seventeenth century, and then only in Italy
  and Southern France. There is no proof at all of its use during plague outbreaks in Middle Europe.
  And the specimens in Ingolstadt and Berlin? Both masks present details which suggest that they were
  not used as protective clothing at all." The teaches cell ("reconstructs the beaked plague costume as
  17th-century anti-epidemic protective clothing … then weighs … authenticity") reads the paper as
  *reconstructing* protective use; the paper argues the opposite — 17th-c. Italian/French iconography,
  no Middle-European outbreak use, surviving specimens probably never protective. The bullet
  ("frames the beaked mask as protective plague-era clothing") repeats the weaker error by omitting
  the negative finding.
- **Mechanical failure:** quote raw length 26 words (> the 8-25 contract); scope cell 76 chars
  (> 60); and under accept-c.py's own `ordered_hits` the drafted bullet yields **2** in-order quote
  words (< 3) because the bullet uses "beaked"/"plague-era" while the quote has "beak-like"/"plague"
  in a different order (`needle=…protective,clothing,…,plague…`; `haystack=…beaked,mask,protective,plague,clothing…`).
  If the entry adopts this BULLET verbatim, **ACCEPT-C-67 RESTATE fails**. Reproduce:
  `python3 - <<'PY' … import accept-c; ordered_hits(content_words(quote), content_words(bullet)) → 2`.
- Repair (keeps the id, so it does not touch the S829+ id/APPEND sequencing): re-quote from the
  conclusion, e.g. "There is no proof at all of its use during plague outbreaks in Middle Europe"
  (14 words, verbatim), set teaches to the negative finding (17th-c. Italian/southern-French
  iconography; Ingolstadt/Berlin masks likely non-protective, authenticity unresolved), shorten the
  scope cell to <=60 chars, and make the bullet reuse >=3 of the new quote's content words. A rewritten
  row is *stronger* knowledge and removes the S791-pomander overlap concern by moving the row from
  "costume as prophylaxis" to "costume iconography vs. evidence".

### S814 — Paracelsus (Distillations / Science History Institute) — tier A claimed, docs
- Live: HTTP 200, 61,534 B; capture `20261011051916id_/`: HTTP 200, 61,255 B — **quote present in
  both**: "For Paracelsus, mastering chemical as well as magical cures was crucial to understanding
  illness and wellness".
- Supported: rejection of "traditional Galenic humoral theory"; "insistence on the core practices of
  purging and bloodletting"; "its rejection of new empirical work using chemistry and anatomy".
- **Defect (medium):** teaches says "seeding iatrochemistry" — the string "iatrochem" occurs **0**
  times in the article; that historiographic label is added by the row. Same for "wedding alchemy to
  healing" only insofar as the title says "the Alchemist Who Wed Medicine to Magic" (acceptable).
  Reword to "chemical medicine" or drop the label unless a second source carries it.
- **Format (low):** teaches 246 chars (>240 contract), scope 67 chars (>60). Not counter-enforced
  (`accept-c.py` ROWS checks only cell count/kind/tier/status/opened/used-by/URL), so this lands
  malformed unless fixed.
- **Tier (medium):** `docs|A` for a dated magazine book-review essay is out of line with registry
  precedent — Smithsonian Magazine is `docs|B` (S615), while `docs|A` instances are reference works or
  institutional pages (S125 Oxford Research Encyclopedia, S322 British Library blog). Recommend tier B,
  or tier A only if the row cites Moran's *Paracelsus: An Alchemical Life* (the reviewed book) rather
  than Drago's review of it. QUALITY criterion 6 ("reserve tier A for sources primary or authoritative
  for the exact scope") points the same way.

### S815 — Cruz-Badianus herbal (Tufts Tisch Library special collections) — tier B, docs
- Live: HTTP 200, 191,213 B; capture `20261011022805id_/`: HTTP 200, 93,309 B — **quote present in
  both**: "It is the earliest known work on Mexican medicinal practices and treatment of diseases".
- Supported in body: "Codex Barberini is the first illustrated text of Nahua medicine, containing 185
  illustrations of herbs used for treatment"; "composed by Martín de la Cruz in the Aztec language and
  was then translated into Latin by Juan Badiano"; "written and translated by Aztec natives".
- **Defects (medium):** teaches claims "1552", "first New World book", and "body-ordered remedies".
  None are in the page: "1552" occurs only inside SVG path coordinates (6 raw hits, 0 in text); the page
  says "sixteenth century"; "New World" 0 hits (page says "Mexican"/"Americas"); no "body part"/"by
  body"/"ordered" remedy organization. The bullet repeats "in 1552". Fix: scope/teaches to
  "sixteenth-century Cruz-Badianus herbal", "first illustrated text of Nahua medicine", the 185 herb
  illustrations and Cruz/Badiano authorship — all source-verified — or cite a source that carries the
  1552 date and body order. Tier B is right.

### S816 — Four Tantras / Blue Beryl (Himalayan Art Resources set 253) — tier B, docs
- Live: HTTP 200, 22,489 B; capture `20260310213249id_/`: HTTP 200, 18,054 B — **quote present in
  both**: "The Four Tantras was discovered as a 'Revealed Treasure' text (terma) by Draba Ngonshe in
  the 11th century".
- Supported in body: "The Blue Beryl … is a commentary to the Four Tantras medical text"; "The Blue
  Beryl medical charts were designed and commissioned by Desi Sanggye Gyatso in the late 17th century";
  "created some time after that but prior to his death in 1705". Teaches' "17th-century commentary
  supplying the teaching charts" is a fair compression.
- Low inference: "teaching charts" (page: "medical charts"/"Medical Paintings") and the bullet's
  "medical curriculum" — neither string is in the page. Harmless but not quote-supported; prefer
  "medical charts".
- Tier B is right; no host/URL collision (`himalayanart.org` is new to the registry; S628/S643/S651 use
  `rubinmuseum.org`/`vam.ac.uk` for amulet objects, not a duplicate).

## Cross-cutting findings (apply to all six)

1. **The frozen predicate cannot separate "quotable" from "supported".** RESTATE (`accept-c.py:292-322`)
   is purely lexical: S811, S814, S815 and S816 all pass it *with* the defects above; S813 is the only
   one that also fails mechanically, and that failure is incidental (word choice), not semantic. So
   `ACCEPT-C-67: PASS` is not evidence of row support; the `review_only` leg ("blind per-row support")
   is load-bearing and this seat's verdicts belong in the closure record. Concrete demonstration:
   `ordered_hits`/`in_order_coverage` imported from the counter and run over each pair (S811 3/0.00,
   S812 3/0.00, S813 2/0.00, S814 5/0.00, S815 5/0.00, S816 5/0.11).
2. **CAPTURE (`accept-c.py:399-417`) is regex-only.** It requires a 14-digit capture whose original
   URL normalizes equal to the live URL; it never fetches the capture. A capture serving a bot wall or
   unrelated page passes. All six captures do normalize equal and *do* contain their quotes (verified
   here), but the leg cannot know that. Also note `id_` replays can be gzip: a check without
   `--compressed` yields a binary body and a false "capture empty" finding — I hit this on S812 before
   re-fetching.
3. **Row-format limits are not counter-enforced.** Quote 8-25 words (S813 = 26), scope <=60 chars
   (S813 = 76, S814 = 67), teaches <=240 chars (S814 = 246) are contract rules only; ROWS
   (`accept-c.py:258-281`) checks cells/kind/tier/status/opened/used-by/URL. These can land malformed
   under a green predicate.
4. **Host budget.** My six span 5 distinct hosts: `pmc.ncbi.nlm.nih.gov` twice (S811, S813),
   `iep.utm.edu`, `www.sciencehistory.org`, `tischlibrary.tufts.edu`, `www.himalayanart.org`. HOSTS
   needs >=10 across 24 rows, so the remaining 18 rows must contribute >=5 more hosts; no collision
   with any base row URL (checked with accept-c's `norm_url_q`; `pmc.ncbi.nlm.nih.gov` is already a base
   host, which is allowed — only exact normalized URLs are constrained).

## Residual risk / verification gaps

- The entry and README row are not yet drafted, so RESTATE/ONEID were evaluated against the fragments'
  `BULLET=` proposals. If the scribe rewrites bullets, re-run `accept-c.py` at lands; S813's bullet in
  particular must not be copied verbatim (2 in-order hits).
- I did not re-derive the row `kind` enum values against corpus convention beyond accepting the
  counter's list; `paper`/`docs` are both in `KINDS` (`accept-c.py:78-81`).
- Capture bodies were verified by verbatim string match plus claim-keyword search, not by diffing the
  full captured article; several captures are smaller than the live pages (S815 live 191,213 B vs
  capture 93,309 B; S812 live 60,390 B vs capture 34,300 B decoded; S816 live 22,489 B vs capture
  18,054 B; S813 live 42,008 B vs capture 42,006 B) but each does contain the quoted text and the
  specific sentences the teaches relies on, searched verbatim in the captured body.
- L1's APPEND/D4 sequencing ruling (S829+ reject rows land at A_ca) is outside this seat's id scope and
  does not change these verdicts; the S813 repair keeps the S813 id, so it adds no new id to APPEND.
- `Report: .ufo/waves/round-67/w1/RevSourceSupport2.md`
