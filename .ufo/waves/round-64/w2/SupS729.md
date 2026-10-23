# SupS729 — blind support of the re-sourced S729

Axes: coverage (is the new work real breadth or a renamed duplicate?), operability (does the
staged row satisfy the frozen ROWS/RESTATE contract the counter applies?), calibration (tier,
scope and bullet bounded to the anchored evidence).

## Snapshot and transition

- 2026-10-23T23:50: row on disk was still the wave-1 Farran draft (sha256 `d3ac805e…`,
  mtime 20:38:03) — i.e. the same work as S718.
- 23:54:40: `ReSourceS729` landed the repaired row. Verified snapshot for this review:
  `sha256 6f501f88c997f561c948f61da1876691e3490e63dab19fe0fdee86e931f04309`,
  mtime `2026-10-23 23:54:40 -0300`, unchanged through 23:58.
- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`
  → `CHECK-ROWS: 32/32 clean` (S729 included) at 23:58.
- No files edited by this seat. Scratch only in
  `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/SupS729/`.

**VERDICT: SUPPORTED** — genuinely different work, verbatim 20-word quote located live and in
the same-page capture, tier A honest for the scoped claim, bullet faithful and RESTATE-clean.
One MEDIUM integration hazard outside the row (stale stage artifacts) and two LOW precision
nits on the row (locator paragraph index; scope wording).

## Finding 1 (MEDIUM, operability/integration — outside the row)

**Stale `stage/` copies still carry the pre-repair Farran S729 row and bullet.** If the L1
integrates from these, claim C ships the duplicate after all.

- `.ufo/waves/round-64/stage/rows.txt:9` begins
  `| S729 | Farran, Lee, Yoo & Oller, 2016 "Cross-Cultural Register Differences…` (old row).
- `.ufo/waves/round-64/stage/bullets.json` has
  `"S729": "- Lebanese mothers use more infant-directed speech across both registers in this caregiving setting (S729)"` (old bullet).
  Both files are dated 20:01, before the repair; grep for the old bullet hits only this file
  (plus `.ufo/waves/round-64/w2/B2ReviewRowS729.md`, which quotes the draft it reviewed).
- `integrate.py` (older helper) re-stages exactly `stage/rows.txt` + `stage/bullets.json` from
  `~/.cache/hyaku/kotodama-r64/`; that cache no longer holds the wave-1 draft
  (`ScribeRowS729/row.txt` is absent), so a rerun would either fail or re-emit stale bytes.
- `integrate-w2.py` is safe: `entry_from_skeleton` renders
  `contributions[sid]["fields"]["BULLET"]` (line ~192) from live `rows/*/row.txt`, and
  `collect_contributions` rejects wrong ids/classes.

Required: assemble with `integrate-w2.py` only, and delete or regenerate
`stage/rows.txt` + `stage/bullets.json` before the acceptance run so no path can emit the
Farran duplicate. The frozen counter reads `corpus/SOURCES.md`, not `stage/`, so this is a
hazard, not a counter failure.

## Finding 2 (LOW, calibration/form — the row's anchor locator)

Row locator says **"para. 2"**. The quote is in the section's **third** numbered body paragraph.

- Raw HTML immediately before the quote:
  `<a id="article1.body1.sec3.sec1.p3" name="article1.body1.sec3.sec1.p3" class="link-target"></a><p>The results are shown in …`
- Section body (`h2 Results` → `h3 Prevalence of pragmatic contexts`), from the page:
  - p1: "Table 2 shows how many clips in the dataset were tagged as belonging to each combination…"
  - p2: "We ran the model with 10 chains of 10,000 iterations…"
  - p3: "The results are shown in Table 2. Conversational basics and inform contexts were more
    prevalent in the ADS register compared to the IDS register. Questions, Imperatives, Reading,
    Singing, Comfort, and Vocal Play were more frequent in the IDS register compared to the ADS register."
- Counting only the prose after the rendered table gives "para. 2", so the scribe's reading is
  defensible; the article's own ids say p3. Recommend `para. 3` (or the paragraph's opening
  words) in the next pre-data revision. Support is unaffected: the section name is exact, the
  quote is verbatim, and the locator is not parsed by the counter.

## Finding 3 (LOW/optional, calibration precision — scope cell)

The scope reads "…60 North American English-speaking infants aged 3–20 months". The page's
Participants text says "60 typically developing infants (28 female) from
**primarily-English-speaking** North American families, with cross-sectional recordings collected
between 3- and 20-months-old"; the abstract says "60 North American, English-speaking, 3- to
20-month-old infants". Also, the analysed unit is **3,607 adult speech clips** from daylong
recordings of those 60 infants, not per-infant rates. Both are consistent with the scope as
written; naming the clip count would only add precision. No claim change needed.

## Identity: genuinely different work (coverage)

| leg | S729 (new row) | S718 (unchanged row) | distinct? |
|---|---|---|---|
| title | "Pitch characteristics of real-world infant-directed speech vary with pragmatic context, perceived adult gender, and infant gender" | "Cross-Cultural Register Differences in Infant-Directed Speech: An Initial Study" | yes |
| authors | Neer, Brahmbhatt, Walsh & Warlaumont | Farran, Lee, Yoo & Oller | yes |
| year/venue | 2025, PLOS ONE 20(6):e0326569 | 2016, PLOS ONE 11(3):e0151518 | yes |
| DOI | `10.1371/journal.pone.0326569` (`<meta name="citation_doi">`) | `10.1371/journal.pone.0151518` (`<meta name="citation_doi">` on PMC4794163) | yes |

- Page metadata matches the row: `citation_author` = Emily M. Neer, Anvi Brahmbhatt,
  Catherine R. Walsh, Anne S. Warlaumont; `citation_date` = Jun 25, 2025;
  `citation_journal_title` = PLOS ONE; `citation_volume` 20; `citation_issue` 6;
  `citation_firstpage` e0326569; `citation_article_type` = Research Article.
- Registry (`corpus/SOURCES.md`, 749 lines): **0 hits** for `0326569`, `Neer`, `Warlaumont`,
  "Pitch characteristics", "IDS register", and also 0 for `IDSLabel`/`HomeBank`/`Bergelson`
  (no overlap with the source dataset's literature either).
- Staged rows: `grep -rF` for the live URL/DOI finds **only** `ScribeRowS729/row.txt`;
  `check-rows.py` dup-URL leg stays clean.
- The old Farran work remains covered by S718 — replacing S729 loses no coverage and removes
  the work-level duplicate ReviewerRegistry F2 / R2 named. (That audit flagged S729 as the
  only work-level duplicate; this seat re-checked S729 only.)

## Anchor quote: verbatim, live and capture

- Quote (20 words, within 8–25): `Questions, Imperatives, Reading, Singing, Comfort, and Vocal
  Play were more frequent in the IDS register compared to the ADS register.`
- Live fetch: `HTTP 200` `https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569`
  (66,843 bytes). Counter-normalised body text (NFKC/casefold/non-word→space, 75,252 chars)
  offset **29,329**; contiguous raw-HTML hit too.
- Context (200 chars around the hit): `…the results are shown in table 2 conversational basics
  and inform contexts were more prevalent in the ads register compared to the ids register
  questions imperatives reading singing comfort and vocal play were more frequent in the ids
  register compared to the ads register acoustic analyses we next examined two key utterance
  level acoustic characteristics…` → body text, in `Results → Prevalence of pragmatic
  contexts`, not a heading, caption, alt/title attribute or navigation.
- Lane locator re-run:
  `python3 -B reports/round-61/reopen-quote.py '<new live URL>' '<quote>'` →
  `LOCATED https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569` (exit 0).
- Capture: Wayback availability API returns closest snapshot
  `status 200 timestamp 20260617141044`; `…/web/20260617141044id_/<live URL>` fetched `HTTP 200`.
  Decoded article text is **identical** to live: whitespace-collapsed decoded text sha256
  prefix `5a949c81…` (78,109 chars both); counter-normalised text sha256 prefix `bf9b04a5…`
  (75,252 chars both); same quote offset 29,329 (raw HTML differs only by the Wayback
  toolbar/scripts: 66,843 vs 78,755 bytes). `CAPTURE`/`ACCESS` lines are accurate; the
  "same-page" claim is verified.
  (Note for other reviewers: the `id_` endpoint serves gzip unless `--compressed` is passed;
  an `--compressed`-less fetch looks like a 13k-char binary page and is not evidence of a bad
  capture.)

## Tier: A is honest

Contract: **A** = "primary or authoritative for that scope … original paper". The row's scope is
the paper's own reported comparison ("relative frequencies of pragmatic contexts across
infant-directed and adult-directed speech in daylong home recordings of 60 North American
English-speaking infants aged 3–20 months"), the anchor is that result, and the paper is a
peer-reviewed Research Article. Not inflated: the teaches cell opens "This study reports…" and
the bullet hedges "In this North American sample". Calibration caveat for the entry text: the
parent study is a **secondary analysis** of the IDSLabel/HomeBank corpora (four daylong LENA
corpora collected 2012–2016); A covers the paper's own finding, not a universal developmental
rule — the sample hedge must survive into the entry.

## Bullet: faithful and RESTATE-clean

Bullet: `- In this North American sample, questions, imperatives, and singing were more frequent
in infant-directed than adult-directed speech. (S729)`

Computed with the counter's own normaliser (`content_words` len≥4, non-stopword, alpha;
`norm_words` for copy runs):

| RESTATE check | value | bound | result |
|---|---|---|---|
| content words | 14 | ≥5 | pass |
| in-order content words from quote | 5 — questions → imperatives → singing → more → frequent | ≥3 | pass |
| longest copied run | 4 — "were more frequent in" | ≤12 | pass |
| novel content words | 8 — north, american, sample, infant, directed, than, adult, speech | ≥1 | pass |
| clause == teaches (teaches_copy) | no | reject | pass |
| clause words | 17 | 6–25 (row bullet rule) | pass |

Faithfulness: the quote establishes exactly that those six labelled contexts were more frequent
in the IDS register than the ADS register; the bullet selects three of the six (questions,
imperatives, singing) with the same direction and no "only"/quantity claim; its "In this North
American sample" is the paper's own frame ("60 North American, English-speaking…"), and "than
adult-directed speech" keeps the register comparison explicit. No overreach, no invented
number. S718's bullet
(overall IDS rate, Lebanese vs American) and S729's (pragmatic-context mix, North American) are
distinct claims in the same §2 slot, so the entry no longer restates one work twice.

## Counter-shape simulation (accept-c ROWS leg, exact functions)

Run against the row with `accept-c.py`'s own `cells`, `anchor_quote`, `norm_words`, `URL_RE`,
`CAPTURE_RE`, `norm_url`:

- 11 cells; tier `A` ∈ {A,B}; status `mined`; opened `2026-10-23`; recheck `180d`;
  used-by contains `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`.
- quote 20 words ∈ [8,25]; teaches 20 words ≤ 25.
- `URL_RE.findall(source)[0]` = live URL; `CAPTURE_RE` matches
  `20260617141044` + original URL; `norm_url(capture_original) == norm_url(live)` → pass.
- LINK pre-check: 0 current `SOURCES.md` lines contain the new live URL (it will be exactly the
  appended row; the row line contains the URL twice — live and inside the capture URI — but the
  leg counts lines, not occurrences). Entry text does not carry the URL.
- APPEND: the row replaces one of the 26 appended ids; no base line is touched.

## Observations (not defects)

- **S729 is outside the frozen LIVE subset** (S718, S723, S728, S733, S738, S743)
  — `accept-c.py` will not refetch the new source; this seat's live+capture fetch is the only
  independent retrieval of the new URL.
- **used-by target absent on disk** (`corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
  does not exist yet); this is the expected forward dependency on the integration step. The
  skeleton (`rows/ScribeEntrySkeleton/entry.md`, 23:51) carries `<!-- BULLETS 2 -->`, and
  `integrate-w2.py`'s `BULLET_MAP[2]` = S718, S719, S729, S724, so the new bullet lands in §2
  "Caregiver registers and the sound of talk to children" — topic fit is right.
- **Registry comparison is nearly vacuous for round-64 rows**: the 32 new rows are staged, not
  yet appended; absence from `SOURCES.md` therefore cannot by itself prove novelty. The
  work-level check above (`DOI`/author/title searches plus S718 cross-check) is the substantive
  one.
- Row transition preserved in scratch: the pre-repair row (sha256 `d3ac805e…`) was the Farran
  duplicate; its old bullet survives only in `stage/bullets.json` and one w1 review.

## Residual risk

1. **Stage staleness (the real risk, Finding 1).** The row is correct on disk; the risk is the
   integration path reusing pre-repair bytes. Mitigation is operationally trivial (use
   `integrate-w2.py`, drop/regenerate `stage/`) but must be explicit in the L1 receipt.
2. **Secondary analysis provenance.** Tier A is for the paper's own result; the entry must not
   generalize beyond the daylong-recording, North American, 3–20-month sample. The bullet's
   hedge is doing that work — keep it verbatim during integration.
3. **Locator precision (Finding 2).** Two defensible paragraph counts (p3 by article ids,
   "para. 2" by post-table prose). No effect on located-ness.
4. **Bullet subset.** Three of six contexts named; legal subset, but if the L1 wants the full
   result in one line, "including" would make the selection explicit (adds no new claim).

## Verification gaps

- Full `accept-c.py` was not run (it needs the integrated 675-row registry + entry); the ROWS
  per-row checks were simulated with its own functions/regexes as above. RESTATE was recomputed
  with the same normaliser/content-word rules.
- S718 was audited for identity only (DOI/title/authors/venue), not re-reviewed field by field.
- The underlying IDSLabel/HomeBank dataset and its licence were not independently inspected;
  not needed for "does the quote support the scoped claim".

## Tooling

No installs or upgrades. Used: `curl` (live and Wayback id_ fetch, `--compressed`), Python 3
stdlib (HTML normalisation, row parsing, RESTATE maths, Wayback availability), `openssl`-free
sha256sum, `check-rows.py`, `reopen-quote.py`. Nothing mutated outside this report and the
scratch directory.
