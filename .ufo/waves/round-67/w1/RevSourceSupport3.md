# RevSourceSupport3 — blind per-row source support, S817–S822

Seat: RevSourceSupport3 (reviewer, leaf, no dispatch). Lane: kotodama-shokunin, tip `b78f8b8`
(base `ad5b52b0…`). Reviewed 2026-10-24 12:20–12:50 UTC.
Scope: independent per-row verification of the six fragments S817–S822 (opened by
ScoutRow07/08/09 under `.ufo/waves/round-67/rows/`) and the per-row support legs of
`reports/round-67/accept-c.py` rev0. Read-only: no git/jj writes, no installs, lane untouched;
fetches were plain `curl` (no automation, no challenge solving).

## PER-ROW VERDICTS

Method per row: parse the 11-cell `ROW=` line; fetch the live URL and the `id_` capture with
`curl --compressed`; assert the anchor string in **body text** of both; assert capture original
query-aware-normalizes equal to the live URL; check the URL against `corpus/SOURCES.md` and all
22 landed fragments; recompute the RESTATE metrics with the counter's own helpers
(`content_words`, `ordered_hits`, `in_order_coverage`); check the longest verbatim bullet↔quote
run (brief limit 12); verify each teaches-cell claim keyword against the page.

### S817 — Milwaukee Public Museum, "Medicine and Healing" — **PASS (one scope defect)**
- live `https://www.mpm.edu/educators/wirp/great-lakes-traditional-culture/medicine-healing`
  → HTTP 200, 22,083 chars text; anchor (21 words) present verbatim in body.
- capture `20260312143012id_/…` → HTTP 200, 21,872 chars, anchor present, captured original
  normalizes equal. Base/fragment duplicate: none (grep base=0, one fragment).
- teaches claims all verified on the page: "Sweat baths were used to relieve colds, fevers, and
  rheumatism"; "The sweat lodge was a small wigwam just large enough for one person and
  completely covered with birchbark or blankets"; "heated stones were carried inside"; "created
  steam by sprinkling water on the stones"; "rubbed down, wrapped up, and put to bed"; Midewiwin
  role confirmed in the anchor itself.
- RESTATE metrics: bullet 11 content words, 3 in-order quote words, 6 novel, teaches coverage
  0.00, quote-echo 0.00, longest verbatim run 1 — comfortably inside every bound.
- **DEFECT (LOW/MEDIUM, unscored by the counter):** the scope cell reads "Great Lakes sweat
  bath: cure, Midewiwin rite, **lodge kit**". The page contains no "kit" and no "bundle"; its
  only container is "two or three tubes … kept in a deerskin bag or cloth wrapping", the
  healer's curing apparatus — not a lodge kit. Drop "lodge kit" (scope must describe the row's
  actual evidence; accept-c never checks the scope cell, so this would land silently).

### S818 — Lopez Terrada, Medical History Suppl. 29 (2009), PMC2836216 — **CONDITIONAL (bullet drift)**
- live HTTP 200, 78,758 chars text; anchor present verbatim in body, in the right context:
  "Physicians attended the municipal university, while the education of surgeons and
  apothecaries was an apprenticeship system overseen exclusively by their own guilds and
  regulated by their respective colleges."
- capture `20261016194944id_/…` → HTTP 200, 78,758 chars, anchor present, normalized equal.
  Unique vs base and fragments.
- teaches claims supported: fueros initiated 14th–15th c. territorial control "generally
  effected through guilds"; examinations with theoretical and practical components administered
  by other professionals; the 1499 Valencian college creation.
- RESTATE metrics: 9 content words, 3 in-order quote words, 6 novel, teaches coverage 0.00,
  longest verbatim run 3.
- **DEFECT (MEDIUM, semantic):** BULLET says "Valencian surgeons and apothecaries **entered
  guilds exclusively through supervised apprenticeship**". The source places exclusivity on
  *oversight of education* ("the education … overseen exclusively by their own guilds"), not on
  *entry* to the guild. The bullet turns an education-monopoly claim into a membership-route
  claim. Fix the clause to "guild colleges exclusively oversaw surgeons' and apothecaries'
  apprenticeship education" before the entry is written; RESTATE cannot see this drift because
  it never compares the bullet to the page.

### S819 — NLM, "Andreas Vesalius: Author & Title Description" — **PASS (tier caveat)**
- live HTTP 200, 3,421 chars text; anchor (23 words) present verbatim; the
  `vesalius_home.html` landing page is a turn-the-pages index with no prose (the seat's own
  rejects.txt records this correctly — good rejection).
- capture `20260803194629id_/…` → HTTP 200, 3,421 chars, anchor present, normalized equal.
- teaches claims supported: "the famous woodcut illustrations of De fabrica influenced the
  depiction of anatomy for centuries"; "confirming and refuting many of Galen's anatomical and
  physiological tenets"; "praise and condemnation".
- RESTATE metrics: 11 content words, 3 in-order, 7 novel, teaches coverage 0.00, longest run 2.
- **CAVEAT (LOW):** BULLET reads "Fabrica verified Galen's anatomical tenets by dissection,
  **then** refuted them" — the source asserts concurrent "confirming and refuting", no ordering.
  Drop "then". Tier A is defensible only because the scope is literally *NLM's own account*; if
  the entry uses this row for anatomy-history claims generally, criterion 6 makes it B.

### S820 — Tognotti, Emerging Infectious Diseases 19(2) 2013, PMC3559034 — **PASS**
- live HTTP 200, 36,827 chars text; anchor (15 words) present verbatim: "…the first permanent
  plague hospital (lazaretto) was opened by the Republic of Venice in 1423 on the small island
  of Santa Maria di Nazareth…".
- capture `20260927110912id_/…`: my first fetch returned `000` (transient), the retry returned
  HTTP 200 with the anchor present; the row's ACCESS note ("replay needs `--compressed`") is
  correct and useful. Normalized equal; unique vs base/fragments.
- teaches claims supported: island siting, moat/ditch encirclement, maritime quarantine and
  sanitary cordons.
- RESTATE metrics: 10 content words, 5 in-order, 5 novel, teaches coverage 0.00, longest
  verbatim run 5 ("first permanent plague hospital") — inside the 12-word limit.
- Minor (informational): the bullet's "Venice's **quarantine** island" is present-day framing;
  the 1423 foundation was a plague hospital, quarantine of goods arriving later. No action needed
  if the entry keeps the "hospital" framing.

### S821 — Ito et al. 2021, Med Educ Online, PMC8676632 — **CONDITIONAL (tier inflation)**
- live HTTP 200, 45,739 chars; anchor present verbatim, and the surrounding sentence supports
  the teaches cell: "In Japan, traditional medicine (known as Kampo) is regulated by the
  government and prescribed by over 90% of physicians along with modern medicine under the
  national health insurance system."
- capture `20250214131132id_/…` → HTTP 200, 45,755 chars, anchor present, normalized equal
  (the seat's 523-on-save note is plausible; the retained capture is same-page and byte-verified
  by me). Unique vs base/fragments.
- RESTATE metrics: 10 content words, 4 in-order, 3 novel, teaches coverage 0.00, longest run 6.
- **DEFECT (MEDIUM, authority):** tier **A** for an e-learning-program paper's contextual
  framing sentence. `corpus/QUALITY.md:29` (criterion 6): "publisher descriptions and abstracts
  are tier B for substantive claims about a work … reserve tier A for sources primary or
  authoritative for the exact scope." The exact scope here is *Japan's regulation/insurance
  status*, for which an education-program report is secondary. Either file B, or swap to the
  institutional source I verified independently today
  (`https://www.okayama-u.ac.jp/eng/research_highlights/index_id177.html`, HTTP 200, capture
  `20251116155119`, body quote "When he arrived in Japan in 753 CE, it is said that he had with
  him 36 kinds of herbal medicines…"). The bullet also adds "across Japan", a mild amplification
  of "in Japan" (source context) — acceptable but tighten it.

### S822 — Sajjadi, Encyclopaedia Iranica, "BIMARESTAN" — **PASS (access note)**
- live URL: **HTTP 200 with a full desktop UA** (`curl -sSL --compressed -A "Mozilla/5.0 (X11;
  Linux x86_64) AppleWebKit/537.36 … Chrome/126 Safari/537.36"` → 200, 398,617 bytes,
  30,548 chars text) and **the anchor is verbatim in the live body**. Same URL returns **403**
  with `curl/8.9.1` (5,509-byte body) and with a bare `Mozilla/5.0` (5,466 bytes) — so the
  block is UA-shape dependent, exactly as the row's ACCESS note says ("keep a browser UA").
  Finding for the re-opener: the row should name a *full* browser UA, because the short
  `Mozilla/5.0` form that other rows in this wave use is refused; that cost me one false-403
  round before the Chrome-UA fetch.
- capture `20261024123927id_/…` (created today ~12:39 UTC) replays HTTP 200, 30,546 chars,
  anchor present; normalized equal; unique vs base and fragments.
- scope checked, both elements supported in the page body: etymology — "BĪMĀRESTĀN, hospital
  (from Persian bīmār "sick," Pahlavi wēmār, with the suffix denoting place -stān). Both
  bīmārestān and the shorter form mārestān entered Arabic…"; institutional order — endowments,
  physician administrators, "often contained living quarters for physicians and medical
  students", "Quite often they were located near madrasas".
- RESTATE metrics: 9 content words, 5 in-order, 4 novel, teaches coverage 0.00, longest run 5.
- Semantic nit (LOW): the bullet's "doubled as medical schools" weakens the source's stronger
  "aside from their primary function, hospitals were also the **principal centers** of medical
  education" — keep the source's strength if the entry can carry the words.

### Rows that could not be reviewed
None — all six fragments landed during this seat's window. (At 09:39 local, `rows/` did not
exist; S821/S822 fragments appeared at 09:41 local from ScoutRow09.)

## CROSS-CUTTING FINDINGS (claim C blockers found while reviewing these six)

1. **S807/S808 have no fragments.** `find .ufo/waves/round-67/rows -name 'row-S80[78].txt'` →
   empty; the landed census is S805, S806, S809–S820, S823–S826, S829–S832. Claim C's SET leg
   requires S805–S828 exactly once each, so C cannot pass until S807/S808 land. (Blocking,
   not mine to fix.)
2. **Reject-row ids vs APPEND — resolved by lands sequencing, with a residual dependency.**
   `accept-c.py:70` bounds additions to `NEW_IDS ∪ {S801..S804}`; APPEND rejects any appended id
   outside that set (`accept-c.py:351-389`). Fragments S829–S832 exist on disk (tier C/B, status
   rejected, `used-by` not the entry) and claim Ca's D4 leg requires ≥2 new today-dated rejects.
   L1's resolution (2026-10-24) is per-claim lands separation: C's receipt runs at A_c where the
   registry carries only S805–S828 (rejects append later at A_ca), so the two predicates are
   jointly satisfiable as sequenced, and no counter revision is made. I accept that as the design
   and record the dependency it creates: **C's PASS is conditional on the registry append order
   A_r (S801–S804) → A_c (S805–S828 only) → A_ca (rejects)**. If any S829+ row reaches
   `corpus/SOURCES.md` before A_c, APPEND prints `extra=[…]` and C fails for a reason no
   per-row review can see. Verification gap: nothing in the frozen counters asserts that order —
   they read only the lands tree each is pointed at.
3. **Scope-length rule is unenforced and already violated.** The seat brief caps scope at 60
   chars; no accept-c leg reads `c[4]`. Landed rows S813 (76 chars) and S814 (67) exceed it, and
   S817 carries an unsupported scope element ("lodge kit"). A drafting-rule bound with no leg is
   a silent-failure class for all 24 rows, not just mine.

## INSTRUMENT FINDINGS (accept-c.py rev0 — executed, not merely read)

Anchored to `reports/round-67/accept-c.py` sha256
`3e5f1a5883c52ee41ce6c61aa536bc289d9b23abe5bafa48fcf744b5efaa97a5` (unchanged from `b78f8b8`;
`accept-ca.py` is the file carrying the applied QUOTES-'S' fix, not this counter). The counter's
helpers were imported in-memory (no fixtures, no writes) and the leg predicates evaluated on
constructed inputs:

```
HIGH-1 fabricated row: quote_words_in_bullet=6 teaches_cov=0.42 novel=3
        teaches_words=12 quote_echo=0.00  -> RESTATE would PASS
        (invented quote, invented teaches, matching bullet)
HIGH-2 capture match: True  (ts "20990101000000" — cannot exist yet)
        normalize_equal: True -> CAPTURE would PASS
MEDIUM-5 case-variant duplicate seen as duplicate: False
        .../historicalanatomies/vesalius_bio.html  vs  .../Vesalius_Bio.html
MEDIUM-4 row_urls with three URLs picks only: https://example.org/one
MEDIUM-7 anchor_quote on a cell opening with a quoted title picks:
        'Grand Medicine Society'
```

- **HIGH-1 — RESTATE is self-referential.** `accept-c.py:296-322` grades the bullet against
  `anchor_quote(c[5])` and `teaches = c[6]` — both cells of the row under test. Nothing fetches
  the anchor. Criterion 18's "anchor quote must be findable in at least one named anchor's body
  text" (`QUALITY.md:57`) has **no frozen leg**; CAPTURE only compares the capture's embedded
  original to the live URL (`accept-c.py:402-424`). My per-row fetches above are the only
  execution of that criterion this wave has.
- **HIGH-2 — CAPTURE never resolves the capture.** `CAPTURE_RE` (`accept-c.py:75`) accepts any
  14-digit timestamp; there is no archive.org request anywhere, no `ts <= today` bound, and no
  check that the capture body holds the quote. A future timestamp passes.
- **MEDIUM-3 — `dirty_tracked` is printed but not enforced.** `stamp_ok` (`accept-c.py:200-206`)
  ignores `dirty_flag`; a worktree whose `main == --lands` but whose tracked files are modified
  passes STAMP while measuring bytes that are not at the stamped revision — the exact failure
  the round's receipt protocol text claims to exclude.
- **MEDIUM-4** — `row_urls()` takes the first non-archive URL only (`accept-c.py:140-144`); a
  second live URL in a source cell escapes LINK/HOSTS/CAPTURE.
- **MEDIUM-5** — `norm_url_q` does not case-fold the path (`accept-c.py:118-136`); case-variant
  duplicates of one page are two keys. Relevant to every NLM/PMC/museum host in this batch.
- **MEDIUM-6 — tier is an enum, not an authority test** (`accept-c.py:252-254`); S821's tier A
  is the live instance in my six rows.
- **MEDIUM-7 — `anchor_quote` takes the first quoted span** (`accept-c.py:146-149`); a quote
  cell opening with a quoted title (the S817 topic's own report title, or "bimaristan") makes
  RESTATE grade the bullet against the title, not the anchor.
- **LOW-8** — `content_words()` drops tokens <4 chars and stopwords, so thin/echo teaches cells
  slip the `teaches_thin` and `q_echo < 0.8` bounds when dates/short words carry the overlap.
- **LOW-9** — ONEID counts `(S###)` anywhere in the entry; a handoff cross-reference breaks the
  one-citation rule for that id (fails safe, but constrain the entry's handoff wording).

## CHECKS RUN (so the integrator can see coverage, not just claims)

Live+capture fetch and anchor-in-body assertion for all six rows; capture original
normalization for all six; base-registry and cross-fragment duplicate check for all six;
anchor uniqueness across the 22 landed fragments (none duplicated); cell-count/tier/status/
opened/used-by checks for all six (all 11 cells, all `mined`, all `2026-10-24`, all used-by the
medicine entry path); teaches-claim keyword verification against each page; RESTATE metric
recomputation with the counter's helpers; longest verbatim bullet↔quote run (max observed 6,
limit 12); tier/authority review against `QUALITY.md:29`.

## RESIDUAL RISK / GAPS

- Iranica 403s may be IP/UA/rate dependent; I saw 403 on four attempts across plain, curl and
  Chrome UAs at 12:42 UTC, so I treat S822's "live 200" claim as unproven rather than false.
- S818's captured page is byte-identical in text length to the live page (78,758 chars); I did
  not diff the HTML, only the extracted text the anchor lives in.
- S822's capture is 3 minutes older than my check and was created on the same day; I verified
  it replays with the quote, not that it was captured by the seat's own request.
- The 22 landed fragments are being written concurrently; S807/S808 and any re-writes after
  12:50 UTC are outside this review.
- Claims HIGH-1/HIGH-2/MEDIUM-* are code-read plus in-memory execution against rev0 at
  `b78f8b8`; no lane fixture was created (write scope), so the counter was not run end-to-end.

No tool installs or upgrades were performed.
