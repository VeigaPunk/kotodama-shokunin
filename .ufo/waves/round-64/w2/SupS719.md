# SupS719 — blind support re-check of the repaired S719 row

Axes judged: **coverage, operability, calibration**. Read-only review; no row, counter,
registry, or lane index was edited. Leaf seat (no subagent dispatch).

## Judged artifact (hash-pinned)

`.ufo/waves/round-64/rows/ScribeRowS719/row.txt`
sha256 `bfb71fac2c399901d6b18bdc4a97815ad2902bdad00639078459f08bead1308f`,
mtime `2026-10-23 23:52:10 -0300`, 11 cells, 1467 bytes.

**The file changed during this review.** My first two reads showed the inherited
bullet (`…helping caregivers attract a baby's attention…`) and teaches cell
(`…portray IDS-like prosody as attention-grabbing without assuming that vowels are
always clearer.`). Between those reads and my byte copy the lane seat
`kotodama-r64.FixRowS719` wrote the hedged revision (its report
`.ufo/waves/round-64/w2/FixRowS719.md`, mtime 23:52:32, quotes exactly the landed
BULLET text). The verdict below applies **only** to sha `bfb71f…`; the earlier state
is recorded in F2.

## Verdict

**SUPPORTED** — the repaired bullet now stays within the caveated finding.

## Proof

### 1. Anchor located live (independent re-open)

- `curl -sSL -A '<desktop UA>' https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content`
  → `HTTP 200 application/pdf; charset=UTF-8 327063`, `PDF document, version 1.3, 14 page(s)`.
- Canonical instrument, from the lane root:
  `python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'` →
  `LOCATED https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content` (exit 0).
- Quote is contiguous body text in §4's first paragraph: extracted text lines 271–273
  (`4. Effects of IDS on Performance` / `The evidence summarized in Section 3 revealed
  that infants attend preferentially to IDS, / and in particular to IDS-like prosody
  (with the aforementioned caveats).`). PDF page 6 = printed p. 162 (range 157–170 over
  14 pages; page-6 footer reads `162 Alejandrina Cristia`). The locator `Section 4,
  first paragraph` is accurate; no heading/caption/nav text is quoted.
- Capture leg: direct GET of
  `https://web.archive.org/web/20240415004434id_/https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content`
  → `HTTP 200 application/pdf 327063`; `cmp -s` reports **byte-identical to the live PDF**.
  The capture's embedded original normalises equal to the live URL (exact string match).
  Live URL is absent from `corpus/SOURCES.md` (0 hits) and appears in no other staged row
  (`grep -F` over `.ufo/waves/round-64/rows/*/row.txt` → only S719), satisfying the
  pre-landing uniqueness rule.

### 2. The bullet's propositions map onto the source's own caveats

Bullet: `- In reviewed studies, infants often attend preferentially to IDS-like prosody,
but age, speaker, and stimulus conditions qualify this tendency. (S719)`

| bullet clause | source support (verbatim locus in the fetched PDF text) | judgment |
|---|---|---|
| "In reviewed studies" | review article; the anchor itself says "The evidence summarized in Section 3 revealed…" | correct secondary framing at tier B; no primary-data claim |
| "infants often attend preferentially to IDS-like prosody" | anchor: "infants attend preferentially to IDS, and in particular to IDS-like prosody"; §3 "typically revealing robust preferences for IDS over ADS (Werker and McLeod 1989)" | "often" weakens, never strengthens, the source tendency — no overclaim |
| "age … conditions qualify" | §3 (text 236–251): "the draw towards IDS is modulated by experience"; "effect sizes increase with age … infants 0–9 months"; "development of preference may be non-linear"; 6-month-olds driven more by repetition than prosody; 7–9-month-olds by acoustic-phonetic differences beyond prosody | supported |
| "speaker … conditions qualify" | §3 (text 240–242): "the preference for IDS is weaker for male voices (Werker and McLeod 1989), who tend to produce less prototypical IDS" | supported |
| "stimulus … conditions qualify" | §3 (text 256–268): preference "greater for natural than simulated, synthesized, or filtered speech"; four synthetic pitch experiments = one positive, one opposite, two null; "Simplifying the stimuli could alter the way in which infants process the stimuli" | supported |
| "qualify this tendency" | anchor's parenthetical "(with the aforementioned caveats)"; §4: "exceptions typically involve less than ideal stimuli" | faithful paraphrase of the source's own qualifier |

The pre-repair defect (wave-1 `ReviewSupportA` D1; `CriticEntrySweep` CE3) was that the
bullet stated the preference flatly and added an unstated caregiver-efficacy claim
("helping caregivers attract a baby's attention"). The landed bullet carries the hedge
in the claim itself, names the three qualifier dimensions the paper actually documents,
and makes no caregiver-effect assertion. I find no remaining overreach: no invented
number, no new causal claim, no scope widening beyond "infants" as the reviewed
population, and tier B remains honest (survey, not primary experiment).

### 3. Frozen-counter arithmetic on the landed row (replication, not acceptance)

Replicated `reports/round-64/accept-c.py:80,98–100` (`anchor_quote` / `content_words`)
against the current cells:

- 11 cells; `anchor_quote(cell 6)` returns the full 24-word sentence (the section
  locator is unquoted, so `QUOTE_RE.search` no longer captures `Effects of IDS on
  Performance`); quote_words 24 ∈ [8,25].
- bullet clause: 20 normalised words, 13 content words (≥5); in-order quote hits = 5
  (`infants, attend, preferentially, like, prosody`) ≥3; novel content words = 8
  (`reviewed, studies, often, speaker, stimulus, conditions, qualify, tendency`) ≥1;
  longest consecutive copied run = 6 tokens (`attend preferentially to ids like prosody`)
  ≤12; exactly one terminal `(S719)`.
- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`
  → `S719 OK`, `CHECK-ROWS: 32/32 clean` (run twice, before and after the landed edit;
  both clean).
- Assembler consequence: `.ufo/waves/round-64/integrate-w2.py:192` renders
  `contributions[sid]["fields"]["BULLET"]`, i.e. this row.txt bullet ships verbatim into
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`.

## Findings by severity

### F1 — MEDIUM (calibration / receipt integrity): the wave-2 record for this row is stale and its claimed scratch artifact is absent

- `.ufo/waves/round-64/w2/B2FixS719.md` (mtime `20:05:44`) documents as its "corrected
  bullet" the **pre-hedge** text: line 9 `BULLET: - Infants attend preferentially to
  IDS-like prosody, helping caregivers attract a baby's attention. (S719)`. That is not
  what the lane row contains; the support defect wave 1 named is still present in this
  report's text.
- The artifact that report cites for its corrected row,
  `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS719/row.txt` (and `cristia-2013.pdf`),
  does not exist: `/home/vgpnk/.cache/hyaku/` contains only `kotodama-r64-w1` and
  `kotodama-r64-w2` (hyphen), and neither contains a `FixS719` directory. The report's
  substantive claim (live PDF re-fetched, quote located) is independently reproduced by
  my own fetch (identical 327,063-byte PDF), so the sourcing is sound — the *receipt* is
  not.
- Impact: any record or integration that consumes B2FixS719.md's "Corrected lines"
  instead of the lane row reintroduces the exact NOT-SUPPORTED bullet from wave 1. The
  canonical artifact is the row at sha `bfb71f…`. Recommendation for the L1: cite the row
  sha in the claim record and treat B2FixS719.md as superseded (optionally annotate it);
  do not treat its absent scratch artifact as verified evidence.

### F2 — LOW (operability / sequencing): the row mutated mid-wave; judgments must be hash-pinned

- Two reads of row.txt during this review returned different BULLET/teaches cells; the
  landed edit is timestamped 23:52:10. A support verdict taken on the earlier text would
  be **NOT-SUPPORTED** (flat preference + unstated caregiver-efficacy claim, dropping the
  anchor's own parenthetical). This verdict is on sha `bfb71f…` only. Sibling seats or
  the integrator should re-hash before consuming; no action needed on content.

### F3 — INFO (calibration): B2ReviewRowS719's "none once anchor cell is fixed" is not a support admission

- `.ufo/waves/round-64/w2/B2ReviewRowS719.md` judged the bullet against the frozen
  RESTATE leg ("asserts only the preference the quote states — no overreach"), while the
  same report records the caveat as a "defensible gloss" concern. Its remit was the
  mechanical `quote_words=5 / in_order=0` failure, and its "none" verdict does not
  supersede wave-1 `ReviewSupportA`'s NOT-SUPPORTED finding. Recorded so the receipt set
  is not misread as clearing the caveat defect before FixRowS719 landed the hedge.

### F4 — INFO (calibration gap, no action): the frozen counter cannot distinguish the unhedged bullet from the repaired one

- The pre-repair bullet (`Infants attend preferentially to IDS-like prosody, helping
  caregivers attract a baby's attention.`) also satisfies the RESTATE arithmetic:
  10 content words, 5 in-order hits, 5 novel content words, longest copied run 5 ≤12.
  Hedge fidelity is therefore review-enforced, not counter-enforced, on this row. No
  counter change is proposed (claims are frozen; any revision is the L1's stamped
  pre-data call with its forcing receipt), but the support-review control is load-bearing
  for this row and should stay in the acceptance record.

### F5 — INFO (operability): the ACCESS line's capture-GET failure no longer reproduces

- Row ACCESS says "archive availability API returned HTTP 429 and direct capture GET
  could not connect". Today the direct capture GET returns `HTTP 200 … 327063` and the
  bytes are identical to the live PDF (`cmp -s` clean). Favorable drift; the capture leg
  is now independently verified. ACCESS is a dated historical record, so nothing is
  wrong with the row — noted so a future re-run does not treat the note as current.

### F6 — INFO (coverage): teaches-cell clause outside the anchor

- Teaches now reads `Helps worldbuilders depict IDS-like prosody as an attention cue
  with age-, speaker-, and stimulus-dependent exceptions; vowel clarity varies.`
  "vowel clarity varies" is not in this anchor (it summarises §2.2's less-straightforward
  vowel-space evidence) but teaches is a use gloss, not an empirical assertion, and the
  clause is consistent with the row's scope cell. No action; the prior wording had the
  same property.

## Residual risk and verification gaps

- Support was judged against the anchor sentence plus the §3/§4 caveat passages it points
  at; I did not audit every claim in the 14-page review. The bullet's three qualifier
  dimensions are each anchored to explicit §3 text (cited above).
- Text extraction: `pdftotext -layout` (poppler) was used for reading and locating; the
  canonical locator's own (pypdf) path independently returned `LOCATED`, so
  extraction-method risk is covered for the anchor.
- The row may change again after my hash; the verdict binds only to `bfb71f…`. The
  assembler ships row.txt BULLET fields (integrate-w2.py:192), so a later edit would
  change the entry without any report being regenerated — hash-pinning at integration is
  the mitigation.
- I did not run `reports/round-64/accept-c.py` (not this seat's gate and the entry does
  not exist yet); the mechanical statements above are replications of its ROWS/RESTATE
  arithmetic plus the row checker, not a claim-C acceptance.

## Tooling

No installs or upgrades. System `curl`, `poppler/pdftotext`, `python3`, `sha256sum`,
`cmp` sufficed. Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/SupS719/`
(`s719.pdf`, `cap.pdf`, `s719.txt`, scratch `rows/` copy used only for an abandoned
alternative-bullet probe — the lane row was never modified by this seat).

## Appendix — inbound coordination (out of this seat's scope; no claim-O verdict)

`kotodama-r64.RevVerifyO2` reported (IRC) that rev4's m5 mutant in
`reports/round-64/accept-o.py` is syntactically invalid. I corroborated read-only, so the
O lane does not have to re-derive it:

- Landed counter sha256 `6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1`.
- m5 rebuilt from `MUTANTS` via `ast.literal_eval` + exact single replace of the
  `tools/reopen-row.py` needle (count 1): mutant sha256
  `795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6`; `py_compile` →
  `IndentationError: unexpected indent`, line 605. Of all ten rev4 mutants, m5 is the
  only one that fails to parse (m1, m10, m2, m3, m9, m6, m7, m8, mread compile).
- Counter run against the broken mutant (`--root` scratch, `--only
  EDGE_SCHEMEREL,EDGE_SLASHLESS`): `EDGE_SCHEMEREL FAIL rows=[]` ;
  `EDGE_SLASHLESS FAIL rows=[]`. The m5 isolation check at accept-o.py:1117–1121
  requires `EDGE_SCHEMEREL PASS`, so `mut_bad` is non-empty and MUT fails — the
  reported ACCEPT-O-64 FAIL follows from the counter's own legs.
- Dedenting the replacement to an 8-space `if` with a 12-space body (mutant sha256
  `804c9473d752833e143971b734f44b64d853e93f4edafbd64a64f504be35babc`) compiles and
  yields `EDGE_SCHEMEREL PASS rows=[('S2816','REFUSED',1)]` and
  `EDGE_SLASHLESS FAIL rows=[('S2641','UNREACHABLE',2)]` — pins `["EDGE_SLASHLESS"]`
  with SCHEMEREL PASS is the correct expectation.
- The rev4 docstring at lines 118–119 ("former to FAIL and the latter to PASS") is
  inverted relative to the code's m5 requirement (SCHEMEREL PASS, SLASHLESS FAIL).
- No counter edit was made by this seat; scratch receipts under
  `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/SupS719/m5/`. Any change belongs to the
  L1's stamped pre-data revision with its forcing receipt.

Report: .ufo/waves/round-64/w2/SupS719.md
