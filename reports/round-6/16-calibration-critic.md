# 16 CRITIC — count and provenance adversary (round 6)

Author-side calibration review. Scope: falsify the F admission design and the
available evidence fragments; name the exact checks the parent must run. I did
not edit any other scope, judge promotion/canon, or re-fetch any URL; all URL
verification below is named as parent work. Review time: 2026-10-17, while the
worker wave was still landing output.

## 1. Review-time state (missing ≠ failure)

Present and inspected by me: `corpus/lessons/round-6-sources/{02,05,06,07,08,11,13}.json`
(7 fragments, 14 audit rows) and `reports/round-6/{01-plan-review.md,14-linguistic-review.md,15-material-review.md}`.

Absent at writing — **unreviewed, not failed**: fragments `03` (Egypt), `04`
(Aegean), `09` (Persia), `10` (Etruria), `12` (Nubia) — 10 of the 24 required
rows; plus `reports/round-6/run-validation.py`, `parent-source-spotchecks.json`,
`parent-reconciliation.json`, `validation.json`, and the lane report. The
counting command being absent is a design gap until the parent lands it
(`LOG.md` round-6 entry already conditions it: "once the actual deliverable
exists"), not evidence against any worker.

Verified now, by me, locally:

- All 12 corpus entries hash-match `baseline.json` in both worktree and
  `git show 030c3928de74ed514853bc1f7490e0f8bb4d451f:<path>` (12/12 MATCH);
  HEAD = baseline revision; `git status` shows only `LOG.md` (parent-owned
  round-6 entry) plus the two new untracked directories. No corpus
  `corpus/knowledge/**` bytes moved. `no_harm` holds so far.
- Each fragment's top-level `entry_sha256_before` equals the baseline value for
  its `entry`; each fragment has `round=6`, correct `baseline_revision`,
  exactly 2 audits; all 14 `id`s and `question` fields byte-match
  `targets.json`; all 14 `source_url`s are single valid HTTP(S) URLs;
  every `retrieved_passage=true` row has non-empty excerpt and locator; all
  Latin-script excerpts ≤40 words (CJK note, §4.5).
- No duplicate main-row passage: 14 distinct (URL, normalized-excerpt) keys
  across 7 entries. Even before the missing five fragments land, the raw
  material for "≥6 distinct passages across ≥4 entries" is present — but only
  the parent's re-fetches can make it count (§5).
- Entry-locator spot-checks passed: quoted entry text found at the cited
  lines for 02 (line 36), 05 (11, 55), 06 (99, 116), 07 (76), 08 (55, 107,
  109, 111–114), 11 (line 102, incl. the 1554–1558 / 1701–1704 wording),
  13 (127, 130, 165).

## 2. Vector-by-vector falsification results (available fragments only)

**2.1 Duplicate passages across rows — no violation found; two counting traps.**
No two rows reuse one (URL, excerpt). Traps: (a) 05-A's corroboration reuses
one URL for several distinct locators (Hattian Wikipedia ×2; UT `hitol/00` ×2)
— these are distinct passages by the declared key, but the parent must count
each key once and must not count one page-fetch as several "independent"
retrievals; (b) 02-A's second `extra_corroboration` reuses the main row's URL
with a different excerpt — same trap.

**2.2 URL/locator mismatches — four provenance-weak spots to re-fetch first.**
(1) 13-A's `source_url` is a Wayback wrapper
(`web.archive.org/web/2023/https://sacred-texts.com/...`) with no pinned
snapshot id (disclosed); the live sacred-texts page 403'd. (2) 11-B's
`source_url` is the Crossref API JSON endpoint, not the article; the passage
is the publisher-deposited abstract (Cambridge 429'd). Round-5 precedent
(`parent-reconciliation.json`, meso-13/PHON-A11) accepts publisher-deposited
abstracts as abstract-scoped content, but the parent must adopt that rule
explicitly here and re-fetch the same endpoint — the worker asks which URL
counts. (3) 08-A/08-B Hebrew Wikisource pages are marked `לא בדוק`
("not proofread") with three displayed textual versions; the citation is to
the displayed text, not a named manuscript (disclosed). (4) 05-B's main
locator is an image caption inside a tertiary page; captions are content, but
the parent's re-fetch must find the caption, not only body prose.

**2.3 Catalogue-as-content — no violation found.** The two museum-object
corroborations (02-B Cleveland 1963.154; 06-B Shanghai Museum CI00010993) are
explicitly `retrieved_passage=false`/provenance-only and are not counted as
passages. No available row claims catalogue metadata as content. The five
absent fragments are untested for this vector.

**2.4 Secondary quotation presented as primary — no fabrication found; two
labels to pin.** All six `primary-text` rows (06-A, 06-B, 08-A, 08-B, 13-A,
13-B) are translations/transcriptions with the mediator (translation, edition,
host) disclosed in `retrieval_method`/`limits`; none claims an unmediated
autograph. 08-A's English gloss is the worker's own, disclosed as such. Two
pins for the parent: (a) 07-A labels Herodotus/Josephus quotes reproduced
inside Wikipedia as `secondary-scholarly` — they are tertiary-embedded
translations; wording wobble, disclosed, no content risk; (b) a validator
word-cap must be CJK-aware (§4.5).

**2.5 Generic caveat substituted for the question — none found.** All 14 main
excerpts engage the specific named claim (Sumerian/Akkadian coupling, kaunakes
naming, Hattic layering, Yazılıkaya horned hats, oracle selectivity, Zhouli
six-vessels, Melqart etymology, Timna chemistry, Sotah 7:6, Taube jade,
Gobhila II,8, ŚB 3.2.1). 07-B's "universal king-only wearing law" half is
verified only as calibrated absence and is disclosed as such in `limits`; the
bounded entry claim itself asserts only "monopoly unsupported", which the
paper's silence supports.

**2.6 False whole-claim support — the one live admission risk.** 9 of 14 rows
claim `whole-bounded-claim`; claims.json's own rule is "Partial support does
not verify an entire compound claim." Under a strict rule ("whole = every
conjunct evidenced by the cited `source_url`"), four rows are downgraded
candidates, all disclosed in the fragments themselves:
- **08-B**: the 4/8-garment conjunct rests explicitly on Yoma 7:5
  (`corroboration_1`), not on the cited Exodus 28 URL. Clearest case.
- **05-A**: the four-category rule, Hattic non-IE status and CTH-bilingual
  legs arrive via corroboration rows (Wikipedia Hattian, UT `hitol/00`,
  Lesson 3), not the cited Lesson-2 URL.
- **08-A**: the qere-perpetuum/'Jehovah'/HaShem conjuncts rest on the Jewish
  Encyclopedia corroborations; Sotah 7:6 covers the Temple/substitute split.
- **06-A**: the four-component-table demonstration rests partly on the
  companion DB99 page (`corroboration_url`); paired-charges leg is on the
  main page.
Borderline, likely defensible as-is: **02-A** (guardrail leg is inference from
the same page — disclosed), **02-B** (the question's dated-object leg comes
via a different URL, but the audited bounded entry claim is covered by the
FIT page). Genuinely whole within one URL: 07-B, 11-A, 11-B (abstract-scoped),
13-A, 13-B.
**Admission impact: none — F's bar is passage-based, not scope-based
("Supported totals do not decide improvement").** Downgrades change
reconciliation quality, not F. The parent must pick one whole-claim rule and
apply it uniformly before publishing any whole/supported counts (round-5
reconciliation combined companion rows conservatively; same discipline here).

**2.7 Inappropriate all-civilization coverage claims — none found so far.** No
available fragment claims corpus-wide coverage; LOG.md's round-6 entry frames
the wave as new earlier-reference surfaces, not a retry of the fifteen
round-5 residuals. The residual risk is in the parent's own wording: the
admission must say "≥6 distinct passages across ≥4 of the twelve assigned
entries", never "all civilizations" or "freshness restored corpus-wide", and
must not read any round-5 residual as closed by this wave.

**2.8 Calibration uniformity red flag (not a schema violation).** All 14
available rows are `supported` (11 of them whole-bounded-claim). Round-5's
comparable raw tally was 13/22 supported with 8 unresolved. Either the
guard-railed entries make support the honest outcome, or scope inflation is
systematic. §2.6 identifies four concrete candidates; the parent's
reconciliation must not rubber-stamp a 100% rate and should record, per row,
which sense of "supported" applies: factual confirmation vs
calibration-consistent confirmation (02-A/02-B support the entry's *cautions*).

## 3. Admission-design vulnerabilities (the claim F itself)

1. **The declared counting command does not exist.** `counting_command:
   python3 reports/round-6/run-validation.py` names a file absent at critic
   time. Until it exists, runs green, and encodes the checks in §4, F cannot
   verify *by its own declared instrument*. Landing it is parent work; round-5
   (`reports/round-5/run-validation.py`) is the working template: schema
   fields, URL validity, word cap, entry-hash binding, dedup, parent-check
   gates, historical-byte preservation.
2. **The distinctness key is prose, not code.** "Keyed by source URL, locator
   and short excerpt" must be implemented (URL trimmed of trailing `/`,
   excerpt whitespace/case-normalized, locator normalized) or the ≥6 count is
   eyeball-arbitrary.
3. **Corroboration-shape variance defeats naive counting.** Five optional
   shapes are in use: `extra_corroboration[]` (02), `corroboration[]` with two
   different internal key sets (05, 07, 11), flat `corroboration_1_*` fields
   (08), `corroboration_url`/`corroboration_note` (06),
   `additional_excerpts`/`questions_for_parent` (13). All are legal
   "separately labelled optional fields", but the parent's passage counter
   must walk *all* of them (an undercount hides passages; a naïve
   field-name counter miscounts), and abstract-only corroboration with
   `retrieved_passage=false` (02-A Jagersma) must never enter the count.
4. **Whole-claim rule ambiguity** (§2.6): must be fixed by the parent in
   `parent-reconciliation.json` before totals are reported anywhere.
5. **Parent re-fetch independence**: the ≥3 re-fetches must be parent-executed
   fetches whose excerpts are transcribed from what the parent actually
   received, keyed with result and directly-relevant/non-bibliographic fields
   (round-5 `parent-source-spotchecks.json` shape). Copying a worker excerpt
   is not a re-fetch.
6. **Tertiary weight**: several mains are Wikipedia/FIT/Livius pages. That is
   schema-legal and the fragments disclose it, but the reconciliation must
   keep "the tertiary page says X" from becoming "the entry's cited
   scholarship (Bonnet 1988, Lipiński p. 235, Melchert 2003, Seeher 2011) is
   verified" — 07-A and 05-A say this correctly in `limits`; the parent report
   must not drop that qualifier.

## 4. Exact checks the parent must run

Order matters: run 1–4 before reading any verdict as a count.

1. **Baseline/no-harm re-check at closure** (rerun after all fragments land):
   SHA256 of each of the 12 entries == `baseline.json` values ==
   `git show 030c3928de74ed514853bc1f7490e0f8bb4d451f:<path>`; `git status`
   shows only expected new fragments + parent `LOG.md`/report paths; historical
   ledgers/reports/gates/examples byte-identical (`git diff 030c3928... --stat`
   scoped to `corpus/lessons/round-5-sources/`, `tools/`, `examples/`,
   `reports/round-5/` must be empty).
2. **Fragment completeness**: exactly 12 fragments `02..13` (01/14/15/16 are
   reports, not fragments), each with the 6 top-level fields and exactly 2
   audits; ids+questions byte-match `targets.json`; top-level
   `entry_sha256_before` matches baseline for the mapped entry; 24 rows total.
3. **Mechanical row checks** (mirror round-5 validator): single HTTP(S)
   `source_url`, `source_kind` in the declared enum, `verdict`/`support_scope`
   in enums, excerpt ≤40 words with a CJK-aware counter (06-B's classical
   Chinese excerpt is 1 whitespace token / 24 chars — legitimate; a
   whitespace-split counter happens to pass it, an ≥N-words floor would
   false-flag), `retrieved_passage=true` ⇒ non-empty excerpt+locator,
   `retrieved_passage=false` ⇒ empty excerpt, `accessed_at` present
   (formats vary: date-only, `Z`, `-03:00` — parse leniently).
4. **Distinct-passage count**: dedupe ALL retrieved-passage rows — mains and
   every corroboration shape — on (normalized URL, normalized locator,
   normalized excerpt); exclude `retrieved_passage=false` and anything
   bibliographic/metadata (abstracts-only records like 02-A's Jagersma entry);
   require ≥6 distinct keys AND ≥4 distinct entries; report the number with
   the key list in `parent-reconciliation.json`. Also report the raw page-fetch
   count separately so one-page-many-excerpts inflation is visible.
5. **Parent re-fetch ≥3**: parent-executed fetches of directly relevant
   non-bibliographic passages, each recorded with URL, locator, excerpt the
   parent actually received, result, and date — recommended first picks, per
   §2: PLOS Sukenik 2021 (07-B), Crossref 10.1017/S0956536105050017 (11-B,
   decide and record the endpoint rule), UT `hitol/20` (05-A), AFE DB99 page
   (06-A), Wisdomlib ŚB 3.2.1 (13-B).
6. **URL/locator resolution for every `retrieved_passage=true` main row**:
   the excerpt (or its spliced halves, for ellipsis-stitched excerpts: 02-B,
   05-A, 08-A corroborations) must occur at the named locator on the live page
   or a pinned snapshot; 13-A's Wayback URL must be resolved to a concrete
   snapshot id and recorded; failed access stays unresolved — do not let a
   re-fetch failure flip any verdict, and never let identity metadata become
   content confirmation.
7. **Entry-locator verification**: every `entry_locator`/`entry_claim` quote
   must occur in the entry at the baseline bytes (my spot-checks passed for
   the 7 available fragments; the 5 absent fragments need the same check —
   cheap grep for the quoted strings).
8. **Whole-claim adjudication**: apply one uniform rule (§2.6/§3.4);
   downgrade-or-justify 05-A, 06-A, 08-A, 08-B; record per-row dispositions in
   `parent-reconciliation.json` with reasons, round-5 style. F does not depend
   on the outcome; publication hygiene does.
9. **Coverage wording**: the report/LOG/SCORECARD admission text must assert
   only the measured scope (24 rows; ≥6 distinct passages across ≥4 of twelve
   assigned entries; ≥3 parent re-fetches) and must state that the fifteen
   round-5 residuals remain residual absent separate evidence.
10. **Land `reports/round-6/run-validation.py`** (or an equivalent re-declared
    procedure) encoding checks 2–4 and 8's recorded rule, run it to exit 0,
    and cite it in the lane report; a F admission without its declared
    counting instrument is self-nonconforming.
11. **Report-order conformance**: lane work commit first, lane report last,
    citing the commit's HEAD hash, `git merge-base --is-ancestor` check;
    corrections as new commits, never amended.

## 5. Unreviewed (must appear as such in the parent report)

Fragments 03, 04, 09, 10, 12 (10 rows), `run-validation.py`,
`parent-source-spotchecks.json`, `parent-reconciliation.json`,
`validation.json`, lane report — all absent at my review time; no verdict is
predicted for them. My own review is author-side, performed without fetching
any external URL, and is not independent promotion verification.

## Questions left for the parent

1. Adopt or reject the strict whole-claim rule and say which four rows move
   (§2.6). 2. Does a Crossref-deposited abstract satisfy the direct-content
   threshold, and against which URL is 11-B counted (worker asked the same)?
   3. Confirm ≥3 parent re-fetch plan targets (§4.5). 4. Confirm the validator
   will be landed before measurement so `counting_command` is executable as
   declared.

## Addendum (same session, appended before any commit)

Fragments 03, 04, 09, 10, 12 landed on disk at 14:51–14:57, during/just after
this review. They remain **uninspected by me** — every statement about them
above (§1 absence list, §2 untested vectors, §5 unreviewed list) describes my
actual review-time state, not a prediction of their content. Sections §4.2,
§4.3, §4.6 and §4.7 apply to them unchanged and are the parent's fastest path
to closing the remaining vectors. Verified still true at addendum time: all
12 entries byte-match baseline; `git status` shows only parent `LOG.md` plus
the new fragment/report files.

## 6. Addendum 2 (same critic identity, after 03/04/09/10/12 landed)

Scope of this pass, per revised instruction: inspect ONLY the five formerly
uninspected ledgers for (a) schema/question IDs/entry hashes, (b) source-kind
mislabelling, (c) fabricated entry_claims, (d) partial-support laundering into
whole claims, (e) URL-to-quotation alignment, (f) duplicate or metadata
counting. I re-fetched nothing and did not re-audit 02/05/06/07/08/11/13;
earlier-ledger facts restated below come from my recorded §1–§2 pass. Still
author-side, not independent verification.

### 6.1 Mechanical results (five ledgers, 10 rows)

All pass: top-level fields present; `round=6`; `baseline_revision` correct;
exactly 2 audits each; all `id`s and `question` fields byte-match
`targets.json`; top-level `entry_sha256_before` equals the baseline value for
the mapped entry; all URLs single HTTP(S) (09-A is plain `http://` — allowed);
excerpts ≤40 words (max 39, 12-A); every `retrieved_passage=true` row has
excerpt+locator; kinds all in the declared enum. No fabricated entry_claims:
every quoted entry anchor I checked resolves in the entry bytes — egypt lines
60/147, aegean 63/103/133, persia 41–48/54/79/80/84, etruria 41/49/51/140/
141/144, nubia 48/50/74/82/85.

### 6.2 Exact-row findings

- **R6-03-A** (secondary-scholarly, Ritner SAOC54 open PDF): kind correct.
  Whole-claim defensible — the cited printed p. 35 carries gloss
  ("god's words"), Thoth `nb mdw-ntr`, and the ritual rubric (n. 161) inside
  one page; the entry's caution leg is disclosed as entry-side guard, not
  source-proven. URL-to-quotation: parent must confirm printed-p.35 header
  ("THE VOCABULARY OF MAGIC 35", PDF p. 53/340) and both quoted sentences;
  OCR garbles transliteration (disclosed) — English sentences must match.
  Worker's A14 note is an entry-side locator question for the parent (A14's
  excerpt carries no mdw-ntr passage; R93 does), no fragment fault.
- **R6-03-B** (museum-object, Louvre E 12026): genuine object-content fields
  (lin/toile/pleated/date/findspot), not identity metadata; record's
  bibliography (VE93, Janssen, Hall/Pedrini) correctly quarantined in
  `corroboration_notes` as bibliography-only — no laundering. Decision
  needed: the excerpt is a stitched field-label/value string, not running
  prose; recommend the parent accept museum record fields as a passage
  (content) and record the decision once. Dating is catalogue attribution
  ("contexte de fouilles"), correctly not re-dated.
- **R6-04-A** (secondary-scholarly, Rutter L15): **whole-claim laundering
  candidate** — the main URL covers only the Linear-A-undeciphered pole; the
  readable-Greek-Linear-B pole rests on corroborations (Rutter L26, LiBER).
  Under the strict main-source rule → partial. Discipline good: pirated
  Killen scan refused; ResearchGate 403 kept unresolved; a bad arXiv match
  discarded.
- **R6-04-B** (repository-scholarship, Boloti proof PDF): genuinely whole —
  the quoted sentence and its next sentence in the same paragraph carry both
  halves ("adequate evidence… virtually no direct information";
  "hypothetical or dubious"). Same-PDF corroborations (PDF pp. 156, 175) are
  distinct passages of one file; parent page-fetch count should show one
  file. Parent: confirm printed p. 246 = PDF p. 259 quote.
- **R6-09-A** (secondary-scholarly, ARTA 2007.001 PDF): **whole-claim
  laundering candidate** — archive-composition + Old-Persian-counterexample +
  "may not demonstrate general use" legs are on the main PDF, but the
  Behistun-monumental leg rests on the livius DB §70 corroboration, which the
  worker itself labels "access aid only, not an edition of record". Strict
  rule → partial. `http://` scheme allowed; parent re-fetch should record
  TLS status. Hallock OIP-92 correctly left unresolved (no PDF href found).
- **R6-09-B** (secondary-scholarly, Boyce via Internet Archive): partial,
  self-marked — good calibration. URL uses a full pinned snapshot id
  (`20261009104155`) — the good practice 13-A's `/web/2023/` lacks. Entry
  line 83's Zoroastrian-essay quotation left author-side/unchecked (source
  404s now) — correct refusal to force resolution; Shahbazi 1974 stays
  bibliographic.
- **R6-10-A** (peer-reviewed, Science Advances via PMC): **whole-claim
  laundering candidate** — non-IE + "not yet fully understood" legs are on
  the main PMC page; the alphabet-adaptation leg rests on the Mnamon
  corroboration and the Tyrsenian leg on a tertiary corroboration that the
  worker confines to the entry's declared bibliography-check role. Strict
  rule → partial. The worker's `limits` assign each leg to its evidence —
  nothing hidden. Genetics-paper language characterization correctly not
  treated as a linguistic argument.
- **R6-10-B** (peer-reviewed, BMCR 2008.05.37): mostly whole within the main
  review (object biography, both separated datings, layout/calendar, LL 8.3,
  identity limits); Krall-1892 and Nesi-hensu sub-points sit on tertiary
  corroboration but are outside the bounded core — defensible as whole, or a
  marginal downgrade; parent adjudicates. Good refusals: AMZ homepage
  explicitly not counted as object confirmation and no museum-object kind
  claimed; primary monograph [LL07] stays unread. Label note: "peer-reviewed"
  for BMCR is generous (editorially vetted review venue, not refereed
  article) — content status unaffected; parent should accept or normalize
  the label uniformly for both 10 rows.
- **R6-12-A** (peer-reviewed, Rilly Ityopis PDF): partial, correct. NES
  naming variant ("Northern" vs entry's "North Eastern") recorded;
  Trigger-confirmation nuance recorded; Rowan leg honestly tertiary-only
  (CiteSeerX returned HTML, kept unresolved); Old-Nubian non-identity leg
  disclosed as resting on the R&D publisher-excerpt corroboration.
- **R6-12-B** (primary-text, Strabo Loeb via LacusCurtius): partial,
  correct; translation mediator named. URL-to-quotation check item: the
  excerpt prints "Among these **fugitive** were the generals…" as verbatim
  archaism — parent must confirm the page really prints singular "fugitive";
  if the page reads "fugitives", the verbatim claim has a transcription slip
  (substantive alignment unaffected). Two extra Strabo quotes live in
  non-schema optional fields (`source_excerpt_secondary`,
  `source_excerpt_ambassadors`) — legal, and excluded from threshold
  counting under the rule below.

### 6.3 Duplicate and metadata counting (whole 24-row set, for the new rule)

24 main rows yield **24 distinct (URL, normalized-excerpt) keys — zero
duplicates** anywhere in the set. No main row is metadata-only; borderline
case is 03-B (field-value stitch, decision in §6.2). Under the operator's
revised counting rule — **main rows only, directly relevant non-bibliographic
scholarly/primary/museum text; tertiary retained but excluded; corroboration
never counted toward the threshold**:

- tertiary mains excluded: 02-A, 02-B, 05-B, 07-A → **20** qualifying mains
  if `secondary-scholarly` counts as scholarly; **15** if it does not
  (excluded would additionally be 03-A, 04-A, 09-A, 09-B, 11-A).
- entries with ≥1 qualifying main: 11 of 12 (all but 02), or 10 of 12 under
  the stricter reading.
- the ≥6-passage/≥4-entry threshold is therefore met by count under either
  interpretation **without using any corroboration row** — but it is
  fail-closed until the parent's relevance sign-off and re-fetch confirmation
  (§6.4 V4/V6).

### 6.4 Fail-closed validator recommendations (binary; any failure ⇒ F fails)

- **V1 Completeness/schema**: exactly fragments 02–13; all six top-level
  fields; 2 audits each; ids+questions byte-equal to targets.json; top-level
  `entry_sha256_before` equals baseline for the mapped entry; 24 rows.
- **V2 Passage-class gate**: a row may enter the ≥6 count only with
  `retrieved_passage=true` AND `source_kind` ∈ {primary-text, peer-reviewed,
  repository-scholarship, museum-object} (+ secondary-scholarly only if the
  parent's recorded decision includes it); `catalogue` and `unavailable`
  can never carry a passage; `tertiary` excluded by the operator rule.
- **V3 Mains-only distinctness**: dedupe on (URL: lowercase host, strip
  trailing `/`; locator: whitespace-collapsed; excerpt: NFKC, lowercase,
  whitespace-collapsed). Count mains only; if the count without
  corroborations is <6, F fails — no inflation path exists.
- **V4 Relevance sign-off**: the parent lists the counted keys (≥6) in
  `parent-reconciliation.json`, each with `directly_relevant: true` and a
  one-line reason; unlisted or unconfirmed keys do not count.
- **V5 Snapshot pinning**: any `web.archive.org` source_url used by a counted
  row must contain a 14-digit snapshot id. 09-B passes; **13-A's `/web/2023/`
  wrapper fails V5** and must be pinned to a concrete snapshot or re-verified
  live before its key can count.
- **V6 Parent re-fetch + string match**: ≥3 parent-executed re-fetches, each
  storing the parent-received excerpt and result; additionally, every counted
  key's excerpt must string-match at its locator (PDF pages via pdftotext
  page number) after the V3 normalization — this also settles the named
  slips: 12-B "fugitive/fugitives", 03-A OCR-garbled transliterations
  (English sentences must match exactly), 03-B French field values.
- **V7 Whole-claim scope**: apply one recorded rule; default = any
  whole-bounded-claim row with a conjunct evidenced only off `source_url`
  counts as partial in reported totals unless the parent records an explicit
  justification. On my inspection the downgrade candidates are 04-A, 09-A,
  10-A (strict rule) with 10-B borderline; earlier-ledger candidates from
  §2.6 were 05-A, 06-A, 08-A, 08-B (02-A/02-B defensible). F is
  passage-based, so these moves do not change admission — only reported
  totals.
- **V8 No-harm**: 12 entry hashes == baseline == `git show 030c3928…:<path>`;
  historical trees (reports/round-5/**, corpus/lessons/round-5-sources/**,
  tools/**, examples/**) byte-identical; unexpected paths in `git status`
  fail.
- **V9 Label policy**: record the BMCR "peer-reviewed" decision and the
  03-B museum-field "passage" decision once each, then apply uniformly.

### 6.5 Limits of this addendum

No URL was fetched by me in this pass; alignment findings are internal
consistency plus directives. The five ledgers' excerpts, locators and
page-number claims (Boloti p. 246/PDF 259, Ritner p. 35/PDF 53, Rilly PDF
p. 6, ARTA pp. 1–2/5–8, Boyce snapshot paragraphs, LacusCurtius §54, Louvre
fields, PMC abstract/introduction) are all parent re-fetch targets under V6.
Nothing here predicts the admission verdict or claims independent
verification; the parent owns integration, judgment and publication.
