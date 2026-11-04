# Round 89 · w1 · CriticClaims: adversarial review of claims F and C

Seat: CriticClaims (critic, non-author). This report is evidence. It is not a verdict, admission or edit.
Frozen inputs: `reports/round-89/claims.json` (sha256 `cd74cfc2…`) and `measure89.py` (sha256 `6bc14bcd…`) at freeze `1cbd0efc56edaa9394e3532fc5d8ef924f122f01`, base `42816d25…`. I did not amend the predicate, counter or controls. Every repair below sits outside the frozen bytes.
Stage: `.ufo/waves/round-89/w1/stage/CriticClaims/`. Receipts are listed in §Receipts.

Axes judged: freshness and coverage. Axes watched for harm: calibration, depth and the governance rule in prompt §5 and §2.

## Ranked findings

### 1. BLOCKER (governance): F is a freshness axis move while freshness is paused by the open round-11 L0 question
- **Counterexample.** `.ufo/l0-questions.md:47` (kotodama | round-11) ends: "Freshness axis-move claims are paused until ruled." claims.json `lowest_axis` and SCORECARD line 1954 say F "does not depend on" that question. The pause clause, though, covers the whole class of freshness axis moves, not only the hash-stability mechanism. The lane read it that way itself for rounds 83–88 (SCORECARD 1713, 1742, 1764, 1811, 1828, 1858: "freshness paused (round-11 L0)", "no waiver asserted").
- F also chooses a recheck threshold of its own: the window 90 < d ≤ 366 days. The paused question is "drift-recheck threshold calibration". F decides the question for itself rather than routing around it. Prompt §5 / rule 270 says "Route around open L0 questions; never treat them as answered."
- **Impacted axes:** freshness admission, calibration (a self-ruling presented as fact).
- **Smallest safe correction (no predicate change):** keep F's work, but report F as "measured; admission contingent on the operator's ruling on round-11 L0". Append an L0 question: does live source re-verification fall inside the round-11 freshness pause? Do not record a freshness score delta in SCORECARD until that is ruled. Rewrite the "does not depend" sentence in the report as an argument for the judge, not a fact. The Rust judge may still reject F on this ground alone. That is a tradeoff the judge decides, not a defect L1 can fix.

### 2. HIGH (freshness): a lazy F landing passes 5/5 with real, unforged captures and quotes copied from the registry row itself
- **Counterexample, executed.** Fixture commit `c8f429af` sits on the freeze chain (bundle `fixtures.bundle`, branch `fx-F-lazy-titlequote`). It advances 10 rows to `2027-11-05` (as_of+366). Each lesson quote is a title fragment taken from that row's own `source` cell, e.g. S009 "Conlang Atlas of Language Structures" and S021 "Do Large Language Models Always Tell The Same Stories?". The captures are my real live fetches (HTTP 200). The other 6 rows get bare `NOT-LOCATED` lines with no evidence, even though all 16 answered 200. The frozen counter gives `ACCEPT-F-89: PASS legs=5/5`, rc=0 (`receipt-F-lazy-titlequote-F.txt`).
- **Scope.** All 16/16 population rows can be backed by some quote copied from their own registry row, so the page never has to be read.
- S032's capture is the linkinghub redirect stub. It is 2774 bytes, its visible text is only "Redirecting", and the title quote still matches because `contains()` runs over raw HTML (meta and attribute text). The paywalled teaching is never reached.
- **Why it matters.** AXES defines freshness as "skill claims re-verified against live surfaces". A title quote re-verifies that the URL resolves, not the claim. This survivor is not declared: claims.json `bounds` names only the forged capture. Independent re-fetch does not close it, because a re-fetch agrees with a title quote.
- **The lazy landing also harms freshness.** The rows promised a 90-day cadence (`90d`). Setting d = as_of+366 nearly quadruples the interval. S009 is a tier-C live statistics page whose bytes changed between two fetches minutes apart (`refetch-stability.txt`).
- Feasibility is not the problem. With the same captures, teaching-bound text is locatable: S009 "1323 conlangs … 127 natlangs … 145 features"; S157 "two distinct whistles replace the five Spanish vowels, and there are four whistles for consonants"; S163, S084, S104–S107, S020, S021, S031 and S033 all show their teaches/anchor tokens.
- **Smallest safe correction (outside the predicate; L1 instruction to executors plus a separate non-graded receipt):**
  (a) Every LOCATED quote must be drawn from visible text (scripts and tags stripped) that carries the row's `teaches`/`anchor` clause. It must not be a substring of the row's own `source` cell or of `<meta>`/markup. The lesson line names the teaches clause it locates.
  (b) Commit a supplementary receipt listing each advanced row as teaching-bound yes/no. Report that count next to the counter result. If fewer than 10 rows are teaching-bound, say so.
  (c) Set new rechecks near as_of+91..+120 (e.g. `2027-02-03`). That meets ADVANCED (> 2027-02-02) and keeps the 90-day cadence.
  (d) Use `NOT-LOCATED` only with a fetch receipt (status, or teaching absent). All 16 URLs answered 200 at 19:10:58–19:11:00 −03:00 (`live-probe.txt`), so a bare NOT-LOCATED for any of them would be false provenance.
  (e) Prefer the 11 rows that carry used-by (S031 S032 S033 S084 S104 S106 S107 S142 S157 S163 S875) and report "skill-claim-bearing rows re-verified k/11". The 5 queued rows (S009 S012 S020 S021 S105, used-by "—") back no skill claim. They count toward ≥10 but re-verify nothing the skill teaches.

### 3. HIGH (coverage): C is not new ground, and the counter cannot tell a real entry from a copy of the existing section
- **Counterexample, evidence.** `corpus/knowledge/linguistics/semantics-pragmatics.md` §4 "Evidentiality and mirativity: grammar of where you know from" (lines 66–82) is a dedicated 2286-byte section. It already holds:
  - source vs. mirative;
  - "Evidential ≠ epistemic modality (certainty): Palmer (1986) keeps them separate" — the very separation C names as its surface;
  - the Willett hierarchy;
  - Tuyuca, Quechua, Korean, Turkish and Matses data;
  - design calibrations;
  - a 3-column × 5-row inventory → cultural-effect table.
- claims.json `C.surface` describes this as "only scattered sub-bullets". That misstates the base, which is a calibration defect.
- Lane precedent goes against counting this as coverage. Round 86 (README:875): "deepens the existing orality entry rather than claiming first coverage". Round 88 (README:905): "claims no new coverage surface". Prompt §6 item 9 says to name the axis by the surface, not by the number it produces; the partition count 33→34 is that number.
- **Counterexample, executed.** Fixture commit `c9628f51` (branch `fx-C-filler-copy-sec4`):
  - the entry is §4 copied verbatim, followed by one repeated design sentence padded to 8209 B under `## Design note n` headings;
  - three new rows S936–S938 point at WALS chapter 77, chapter 78 and feature 77A, with real 200 captures;
  - the gate quotes are page titles ("Semantic Distinctions of Evidentiality", "Coding of Evidentiality");
  - the new S-ids appear only in the header `sources:` line;
  - README bookkeeping is done (row, header 34, footer).
  The frozen counter gives `ACCEPT-C-89: PASS legs=8/8`, rc=0 (`receipt-C-filler-copy-sec4-C.txt`). §4's table alone satisfies TABLE, since `tables(§4)` = [(3, 5)]. This is the "8 KB of fluent filler with three thin sources" case, and it uses honest captures. That makes it a second undeclared survivor, distinct from `C-forged-capture`.
- **Impacted axes:** coverage (claimed but not moved), depth and calibration (duplicate authority: two files teaching the same evidential facts can drift apart).
- **Smallest safe correction (no predicate change):**
  (a) In the report/SCORECARD prose, not claims.json, correct the surface statement to acknowledge §4 and list the delta subtopics the new entry adds. Candidates are ground §4 lacks: evidential strategies vs. grammatical evidentials; WALS 77A/78A distribution and coding loci; person interaction (egophoric/conjunct–disjunct, first-person effects); evidentials in questions and commands; narrative genre and tense coupling; areal diffusion and borrowing; epistemic-modality scales as a separate design axis.
  (b) Do not copy §4's table or data rows; cross-link §4 instead.
  (c) Commit a non-graded overlap receipt: 8-word shingle overlap between the new entry and semantics-pragmatics.md, conlang-methodology.md and semantic-fields-lexicon-building.md, reported as a number.
  (d) Each new S-id must be cited inline against at least one body claim it supports, and its gate quote must carry that claim, not the page title. Report the count of body-cited claims per id.
  (e) If the delta is mostly restatement, report coverage as contested, or the move as depth per the r86/r88 precedent, and let the judge rule.

### 4. MEDIUM: the declared forged-capture survivor is an acceptable bound only if the re-fetch defence actually runs, and that defence does not cover findings 2–3
- A forged capture passes because `sha256`, `http_status` and `fetched_at` are self-declared in the author's own manifest. The checks prove self-consistency, not provenance. As a stated-before-data bound this is acceptable, since no offline counter can verify the web. It becomes a hole if the re-fetch is never executed.
- **In-round defence, now partly supplied.** This seat is non-author and fetched all 16 population URLs live at 2026-11-04T19:10:58–19:11:00−03:00. Raw captures are in `refetch-captures.tgz` and their sha256 in `cap-sha256.txt`. A second fetch shows 12/16 rows byte-stable. S009, S104, S106 and S875 differ between fetches. For those four, agreement must be checked by quote containment (`measure89.contains`), not by hash.
- **Repair.** Before the close, L1 or the closure checks each executor quote against these independent captures and records an agreement table (k/n). Any advanced row whose quote is absent from the independent capture is treated as unbacked in the report. C's three new sources need the same non-author re-fetch.
- None of this closes findings 2–3: an honest capture with a teaching-free quote still agrees. The bound is acceptable only together with the corrections in findings 2 and 3.

### 5. MEDIUM (separability): C citing a population row kills F, and the cited separability script is not committed
- **Counterexample, executed.** Fixture `e5d5da10` (`fx-FC-cite-pop`) lands F plus C, with C also citing S009 (CALS, which carries WALS-derived features and so is a plausible evidentiality citation) and updating S009's used-by, as contract §2b requires of a citing entry. Result: F `LEG FAIL OTHERCELLS observed=["S009"]`, rc=1, while C passes 8/8. The claims stay separable only while C avoids the 16 population ids. Without the used-by update, the registry contract is silently broken instead.
- claims.json `separability` says "reports/round-89/separability89.py builds both overlays from committed revisions". That file is absent at freeze `1cbd0efc` and at dispatch `9ad00be1` (`git ls-tree` lists 13 files under reports/round-89/, none of them separability89.py). As stated, the pointer is false provenance.
- **Repair.** Instruct the C author to cite none of S009 S012 S020 S021 S031 S032 S033 S084 S104 S105 S106 S107 S142 S157 S163 S875 and to change no base row's recheck. Commit separability89.py (or point to `tools/check-claim-separability.py`) with its executed overlay receipts before the close, or state in the report that the pointer was not delivered.

### 6. MEDIUM (freshness): OTHERCELLS forbids fixing a stale item that genuine re-verification finds
- **Evidence.** S142's anchor cell quotes `"The style of notation used by these hunting signals appears`. The live (Wayback) PDF reads "The style of notation used **for** these hunting signals appears to be unique to this source." The registry locator is not verbatim. AXES freshness asks for stale items to be "flagged or fixed", and F's OTHERCELLS leg forbids changing any non-recheck cell of a population row.
- **Repair.** Flag such defects in the lesson as a stale finding with the verbatim correct text. Leave them unchanged this round and carry the fix to round 90. Do not hide them to keep OTHERCELLS green.

### 7. LOW: the population is mechanical, not cherry-picked, but several rows cannot show drift through their URL
- **Reproduced.** `check-sources-recheck.py --registry <base SOURCES.md> --as-of 2026-11-04 --window 90` printed `RECHECK-QUEUE: 0 due / 20 upcoming / 16 on-release / 859 rows`, rc=0. That matches claims.json. The rule is deterministic, so this is not cherry-picking.
- Some included rows are as non-live as the excluded repo-path rows:
  - S142's only URL is a fixed 2025-03-31 Wayback snapshot, so it can never drift;
  - S032 resolves to a paywall redirect stub;
  - S875 is a search form.
- 0 rows are due; all were opened 10–16 days ago, so the expected drift yield is small. F is preventive hygiene, not drift repair.
- **Repair.** Label in the report which advanced rows are immutable-archive re-locates (S142), and do not present them as drift detection.

### 8. LOW: the Wayback fallback accepts a snapshot of any date
- `url_ok` accepts any `https://web.archive.org/web/<anything>/<row url>`, so a 2019 snapshot fetched today passes as "re-verification on 2026-11-04".
- **Repair.** Use Wayback only after a recorded live 403/429/challenge receipt. Record the snapshot timestamp in the manifest's extra fields and report the Wayback-backed count separately.

### 9. LOW: DISPOSED accepts unbacked LOCATED/NOT-LOCATED lines for unadvanced rows
- A LOCATED claim on a row that was not advanced is never capture-checked.
- **Repair.** Require every LOCATED line to be an advanced, backed row, or check the rest with a non-graded receipt. NOT-LOCATED lines need the fetch receipt described in 2(d).

## (a)–(e) answers in brief
- **(a)** F is real re-verification only if its quotes are bound to the teaching. As frozen, title or markup quotes satisfy it (finding 2). The ≥10/16 target is unreachable by do-nothing (control F-nowork fails ADVANCED and DISPOSED) but reachable by a lazy landing with real captures (PASS 5/5). The population is mechanically derived and not cherry-picked (finding 7). F conflicts with the round-11 L0 pause clause (finding 1).
- **(b)** C restates §4 of semantics-pragmatics.md unless the delta is enforced, and the counter passes a copy-plus-padding entry with three title-quoted sources (finding 3).
- **(c)** The claims are separable only if C avoids population ids, and separability89.py is missing (finding 5).
- **(d)** The forged-capture survivor is an acceptable bound only together with the executed re-fetch; reference captures are supplied. The larger undeclared holes are honest-capture, teaching-free quotes for F and copied filler for C (findings 2–4).
- **(e)** Axes at risk:
  - freshness: cadence weakening up to 366 days, and fix-forbidden stale items;
  - calibration: the "scattered sub-bullets" misstatement, the "does not depend on L0" assertion, and the missing separability script;
  - depth: duplicate authority with §4.

## Receipts (stage dir `.ufo/waves/round-89/w1/stage/CriticClaims/`)

| file | content |
|---|---|
| `live-probe.txt` | 16 population URLs and 3 WALS URLs, status, effective URL, bytes, fetched_at |
| `refetch-stability.txt` | second-fetch sha comparison (12 stable / 4 differ) |
| `cap-sha256.txt`, `refetch-captures.tgz` | independent raw captures with sha256 |
| `urls.json` | population URLs extracted with `measure89.urls` from base SOURCES.md |
| `fixture.py` | builds the three fixtures in a `git clone --shared` scratch clone and runs the frozen counter |
| `receipt-F-lazy-titlequote-F.txt` | lands `c8f429af…`, PASS 5/5, rc=0 |
| `receipt-C-filler-copy-sec4-C.txt` | lands `c9628f51…`, PASS 8/8, rc=0 |
| `receipt-FC-cite-pop-F.txt` / `receipt-FC-cite-pop-C.txt` | lands `e5d5da10…`; F FAIL OTHERCELLS rc=1, C PASS rc=0 |
| `fixtures.bundle` | the three fixture commits on top of `9ad00be1`, so the closure can re-grade |

To re-grade: `git clone --shared` the lane, then `git fetch <bundle> 'refs/heads/*:refs/heads/*'`, then run `measure89.py --freeze 1cbd0efc… --lands <sha>`.

Commands observed (rc):
- `check-sources-recheck.py` at base, rc=0.
- curl ×19 (16 population + 3 WALS), all rc=0 and HTTP 200; second curl ×16, rc=0.
- `fixture.py` runs:
  - first run: the C fixture failed INDEX (rc=1) because of my README bookkeeping (header 33, topic mismatch), which I fixed;
  - second run: F rc=0, C rc=0, combined F rc=1 / C rc=0.
- `git bundle create` rc=0.

The fixture clone sat in scratch only, and its toplevel was verified before the first commit. No lane, production or fleet file was edited; no tools were installed.
