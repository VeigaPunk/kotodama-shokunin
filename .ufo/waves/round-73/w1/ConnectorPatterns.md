# ConnectorPatterns — cross-claim and cross-source pattern report (round 73, w1)

**Seat:** `ConnectorPatterns` (leaf connector, hyaku run 7, round 73)  
**Date:** 2026-10-25  
**Lane Root:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`  
**Fleet Root:** `/home/vgpnk/Projects/shokunin`  
**Tooling Record:** No tool installed or updated. System Python 3, `git`, `pdftotext`, `curl`, and `grep` preinstalled and sufficient. `pacman` untouched (orchestrator host-wide pause respected).  
**Download Hygiene:** No scratch downloads performed outside local repo inspection; peer fetch artifacts consulted in `/tmp/ScoutS*/` and local `.ufo/waves/round-73/w1/` reports.  

---

## 1. Executive Summary & Context Synthesis

Round 73 operates across two declared axes:
1. **Coverage (Claim C):** Assimilation of the `conlang-scholarship` theme from `/home/vgpnk/Projects/shokuknow/merge/kotodama/` onto uncovered ground, admitting two entries (`conlang-scholarship.md` and `conlang-scholarship.amend-2026-10-23.md`), appending five new registry rows (`S876`–`S880`) to `corpus/SOURCES.md`, and re-pointing all citations by document.
2. **Calibration (Claim Ca):** Resolution of the round-72 routed defects R1–R3 and formalization of an append-only stated-vs-observed ledger (`reports/round-73/ledger.json`, $\ge 8$ pairs) to detect and repair discrepancies between declarative statements (in `SCORECARD.md`, `SHONEN.md`, `corpus/README.md`, `SKILL.md`) and observed repository bytes.

The connector's task is to analyze:
- (a) The five theme sources' bibliographic shapes (journal article, complete monograph vs announcement booklet, special-issue editorial overview, aggregator repository paper);
- (b) The staged amendments' failure classes from rounds 71–72 (`corpus/lessons/round-71.md`, `round-72.md`, `round-72-verifier-spotcheck.md`);
- (c) The Ca ledger methodology (stated-vs-observed pairs);

and identify **$\le 5$ recurring patterns** that predict where a row, entry, or self-assessment will fail. For each pattern, this report details evidence pointers, the check that catches it, whether existing `QUALITY.md` criteria (1–21) cover it, and provides concrete text for **QUALITY criterion 22** and an additional criterion (**QUALITY criterion 23**). Finally, it articulates one bounded, non-obvious synthesis move across the round's claims.

---

## 2. Five Recurring Failure Patterns

### Pattern 1: Cross-Campaign ID-Namespace Collision & Citation Contamination

#### Nature & Mechanism
Identifiers are strictly local to their generation context, but three independent S-id namespaces currently overlap:
1. **Staged namespace:** `S859`..`S990` (132 rows in `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md`);
2. **Expansion register namespace:** `S776`..`S835` (`shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`);
3. **Lane registry namespace:** `S001`..`S875` (799 rows in `kotodama-shokunin/corpus/SOURCES.md`).

When draft entries or amendments are written during multi-round staging campaigns, authors frequently cite temporary campaign-round IDs. When imported into the lane, if an entry retains an un-remapped ID that numerically collides with a preexisting lane row, it produces a catastrophic silent defect: an entry discussing linguistics cites an S-id that in the lane registry points to an entirely unrelated document. Furthermore, static renumbering maps become stale whenever an intermediate round lands a different set of rows.

#### Evidence Pointers
1. **Staged conlang draft campaign-ID leak:**
   - `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md:11`: `- gap filled: ... Round 1 added a conference paper (S728) because no venue could be reached.`
   - In the lane registry (`corpus/SOURCES.md:683`), `S728` is:  
     `| S728 | Henrike Frye, 2022 "Corrective input", Child-directed Speech in Qaqet: A Language of East New Britain, Papua New Guinea...`  
     This is an unrelated paper on child-directed speech in Papua New Guinea, not a conlang conference paper.
   - `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23c.md:14`: cites `S769` (in lane: Iona & Peter Opie, *The Lore and Language of Schoolchildren*).
   - `conlang-scholarship.amend-2026-10-24.md:42` and `conlang-methodology.amend-2026-10-24.md:17`: cite `S806` (in lane: Jaiswal & Williams, "A glimpse of Ayurveda...").
2. **Precedent in round 72:**
   - `corpus/lessons/round-72.md:97` (ScoutMergeScan routing to r73): staged era-periodization amendments cite campaign IDs `S726`, `S732`, `S746`, `S757`, which name unrelated lane documents.
3. **Stale renumbering map drift:**
   - Round-71 `.ufo/waves/round-71/assimilation/id-renumber-map.json` mapped `S859` $\to$ `S874` and `S860` $\to$ `S875` assuming linear continuation after row 784.
   - Round 72 adopted rows `S874` and `S875` by document from staged `S863` (ihchina) and `S867` (bunka). The round-71 map was rendered invalid, yet remained on disk until ScoutMapIds regenerated it in round 73 (`.ufo/waves/round-73/w1/ScoutMapIds.md`).

#### The Check That Catches It
A mechanical pre-landing collision lint (`tools/check-namespace-collisions.py`):
```python
# Scan all admitted markdown entries for S-id tokens: \bS\d{3,4}\b
# For each cited S-id:
# 1. Assert S-id >= next_free_id OR S-id belongs to the pre-existing lane registry.
# 2. If S-id < next_free_id, assert that the cited document title/URL matches
#    the lane registry row at corpus/SOURCES.md:S-id verbatim.
# 3. Assert zero occurrences of known campaign-only IDs (e.g. S728, S769, S806).
```

#### Coverage by Existing QUALITY Criteria (1–21)
- **NOT COVERED.**
  - **QUALITY 1 (Provenance):** Forbids invented sources, but `S728` is a real source in the registry; it is simply the *wrong* document.
  - **QUALITY 7 (Claim separability):** Governs inter-claim dependencies within a single round's landing, but does not regulate imports from external staging packages or cross-campaign ID collisions.

---

### Pattern 2: Bibliographic Container / Carrier Shape Misclassification

#### Nature & Mechanism
A source's physical artifact shape is mischaracterized in the staged row or entry, causing distorted tier assignments, false scope constraints, and quote leakage. Three distinct sub-manifestations occur:
1. **Monograph vs. Announcement Booklet:** A full-length book is assumed to be merely a table of contents or announcement booklet, artificially demoting its tier and scoping.
2. **Special-Issue Editorial Overview vs. Empirical Study:** An opening editorial summarizing a journal issue is used as a proxy for an empirical study in that issue, leading to attribution of details (like "semester-long") that exist in the underlying study but are absent from the editorial carrier.
3. **Structural Mislocation & Lexemic Invention:** A source from an aggregator repository with unnumbered sections is assigned an arbitrary numeric section label (e.g. "§1"), and the entry introduces terminology (e.g. "автоконланги") absent from the source.

#### Evidence Pointers
1. **S882 Monograph Misidentification:**
   - `shokuknow/merge/kotodama/SOURCES.append.md:30`: Describes `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` as a "series announcement booklet with the book's contents" and assigns Tier B on the premise that it only supports claims about the book's coverage.
   - `ScoutS882.md:93-105`: Inspection of the 1,055,723-byte PDF revealed it is the **complete typeset monograph** of 185 pages (66,924 words), containing the full preface, chapters 1–6, conclusion, three appendices, and complete bibliography. The staged tier justification was factually incorrect.
2. **S901 Editorial Overview vs. S894 Study Leakage:**
   - `conlang-scholarship.amend-2026-10-23.md:9,17`: Attributes "a semester-long language-construction project" to `S901` (`anderson-etal-cjl-sotl.pdf`).
   - `ScoutS901.md:100-104`: Anderson, Grant & Sanders (2024) is the opening editorial of the special issue. The token "semester" occurs **0 times** in the PDF. The token originated in `S894` (Sowers-Wills 2024 abstract). Attributing it to S901 is an attribution defect.
3. **S893 Section Mislocation & Non-Verbatim Lexeme:**
   - `conlang-scholarship.amend-2026-10-23.md:31`: Asserts the quote is located in "§1".
   - `ScoutS893.md:118-120`: The article has unnumbered headings. The classification passage sits in the 4th section (comparison section, printed p. 32). Furthermore, the amendment uses the lexeme "автоконланги", which occurs 0 times in both HTML and PDF (the source uses "личные, или персональные, языки" / "авторские языки").
4. **Precedent in round 71:**
   - `corpus/lessons/round-72.md:102`: RAD Benesh `S869` cited `/benesh-international/`, which was a locale-picker shell rather than the canonical article text.

#### The Check That Catches It
An automated container-inspection protocol (`tools/check-container-shape.py`):
1. **PDF Metadata Inspection:** Extract page count (`pdfinfo | grep Pages`) and word count. If page count $> 50$ and text covers complete chapters, reject descriptions asserting "announcement booklet" or "table of contents".
2. **Token Attribution Lint:** For every specific claim in an amendment (e.g. `semester-long`), verify that `pdftotext <file> - | grep -i '<token>'` returns $\ge 1$. If 0, fail the attribution.
3. **Unnumbered Section Check:** If a document lacks numbered section headings (`<h\d>` or PDF running headers), forbid numeric section citations like "§1" in the registry anchor cell; require the verbatim heading text.

#### Coverage by Existing QUALITY Criteria (1–21)
- **PARTIALLY COVERED, BUT INCOMPLETE.**
  - **QUALITY 6 (Source authority stays claim-scoped):** Restricts publisher descriptions and abstracts to Tier B, but does not detect when an author mistook a complete book for an announcement or vice versa.
  - **QUALITY 18 (Row anchors resolvable on page):** Requires anchor quotes to be findable in body text, but does not prevent conceptual token leakage across neighboring papers in a special issue.

---

### Pattern 3: Client-Profile Artifacts & Composed-Slug Wall Illusion

#### Nature & Mechanism
Automated command-line HTTP clients using default request profiles (e.g., `curl/8.x` or default Python `urllib`) frequently receive HTTP 403, 429, or Cloudflare/DDOS challenge interstitials from academic and cultural institutional servers (OJS platforms, UNESCO, state databases). Scouts testing with default tools rule the source "challenge-walled", "CAPTCHA-blocked", or "unreachable". However, sending a standard browser-shaped `User-Agent` header returns immediate HTTP 200 with full payload.
A paired failure occurs in archive verification: scouts construct a guessed URL pattern ("composed slug") that yields 0 Wayback CDX captures, falsely concluding "no capture exists", whereas following the canonical redirect target yields hundreds of valid captures.

#### Evidence Pointers
1. **UNESCO CAPTCHA Wall Illusion in round 71:**
   - `corpus/lessons/round-71.md:33-39`: ScoutOpenSourcesC refused eight candidates citing "ich.unesco.org live CAPTCHA walls".
   - `corpus/lessons/round-72.md:103`: ScoutCDXCanonical proved that all eight UNESCO element URLs return HTTP 200 with full narrative text under a browser User-Agent (`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ... Chrome/130.0`). The CAPTCHA wall was purely an artifact of plain `curl` request headers.
2. **Capoeira "No Capture" Falsification:**
   - `corpus/lessons/round-71.md:109`: Capoeira rejected on grounds of "no Wayback capture under that URL".
   - `corpus/lessons/round-72.md:109`: ScoutCapoeiraReopen demonstrated that the scout probed the pattern-composed slug `capoeira-00892` (0 captures), while the canonical slug `capoeira-circle-00892` had 135 status-200 captures dating back to 2017.
3. **RAD Benesh and DNB Falsifications:**
   - `corpus/lessons/round-72.md:102`: Probed `/benesh-international/` had 0 captures, while canonical `/about-us/benesh-international-benesh-movement-notation/` had 25 captures. DNB "only 1999–2000 captures" was false (1,882 modern captures existed; the domain simply failed DNS resolution).
4. **Round 73 Claim C Foundation:**
   - `reports/round-73/claims.json:59`: Explicitly identifies `mistake_to_mine` as R2 and `quality_candidate` as QUALITY 22 (UA-record clause).

#### The Check That Catches It
A two-tier fetch discipline and canonical CDX resolution check:
1. **Dual-UA Probe Requirement:** Any fetch script or scout re-open command must execute:
   ```bash
   # Tier 1: standard curl
   # If HTTP status in {403, 429, 503} or body matches challenge signatures:
   curl -sSL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" "$URL"
   ```
2. **Canonical Slug Resolution:** Query `https://web.archive.org/cdx/search/cdx?url=<canonical_slug>&output=json&filter=statuscode:200` only after following all live HTTP 301/302 redirects to effective final URLs.

#### Coverage by Existing QUALITY Criteria (1–21)
- **PARTIALLY COVERED.**
  - **QUALITY 21:** Explicitly enforces canonical-slug CDX probing for "no capture" rulings.
  - **QUALITY 10:** Forbids bypassing access controls via browser automation or solved CAPTCHAs, but **does not** mandate User-Agent recording or testing a browser profile before declaring a source walled.
  - This gap is the direct motivation for **QUALITY 22**.

---

### Pattern 4: Receipt-Verdict Decoupling / Unverified Rerun Overstatement

#### Nature & Mechanism
A calibration failure where a formal summary table (`SCORECARD.md`, `SHONEN.md`, or a fleet report) asserts a passing gate verdict (e.g. "ACCEPT-CA-72 PASS legs=12/12"), but the committed telemetry receipt backing that statement reads `FAIL`.
This happens when an integrator runs an initial gate check, experiences failure on legs that depend on the unfiled report itself (e.g. `REPORTCORR`, `REPORTLAST`), files the report claiming that a subsequent rerun passed, but fails to commit the rerun receipt. The repository is left in a state where the public self-assessment is contradicted by committed test artifacts.

#### Evidence Pointers
1. **Round-72 Routed Defect R2:**
   - `SCORECARD.md:1401`: Calibration row claims `ACCEPT-CA-72 PASS legs=12/12 at the measured revision`.
   - `reports/round-72/telemetry/measures-ca.txt`: Committed receipt at stamped revision `21ad3088` reads:
     ```
     LEG FAIL REPORTCORR
     LEG FAIL REPORTLAST
     ACCEPT-CA-72: FAIL legs=12/12
     ```
   - `.ufo/reports/round-72/kotodama.md:27`: Claims both legs passed on a post-report rerun, but **no rerun receipt was committed anywhere in the repository**.
   - `corpus/lessons/round-72-verifier-spotcheck.md:31`: Non-author verifier spot-check flags this as defect R2 ("missing receipt leaves the gate's final verdict unevidenced and the SCORECARD row overstated").
2. **Round-73 ScoutLedgerSweepB Findings:**
   - `ScoutLedgerSweepB.md:21-22`: Confirms M1 and M2 mismatches directly against current HEAD `8841ad3`.
3. **Round-71 CASTAMP Defect:**
   - `corpus/lessons/round-71.md:110`: Receipt header in `measures-ca.txt` stamped a counter sha256 (`1ce25fb9`) that did not exist at the stamped revision (`64da9e14`), requiring an appended correction receipt in round 72 (`measures-ca-restamp-64da9e14.txt`).

#### The Check That Catches It
A mechanical receipt-verdict reconciliation check (`tools/check-receipt-verdicts.py`):
```python
# For every line in SCORECARD.md or fleet reports asserting "ACCEPT-<CLAIM>-<ROUND> PASS legs=M/M":
# 1. Locate the corresponding receipt in reports/round-<ROUND>/telemetry/measures-<claim>.txt
# 2. Parse the terminal line of the receipt:
#    assert "ACCEPT-<CLAIM>-<ROUND>: PASS legs=M/M" in receipt_tail
# 3. Assert exit code == 0.
# 4. If the report claims a post-report rerun passed, assert that a matching
#    measures-<claim>-rerun.txt (or updated measures-<claim>.txt) is committed
#    at the exact landed revision.
```

#### Coverage by Existing QUALITY Criteria (1–21)
- **NOT COVERED.**
  - **QUALITY 17:** Pins measured revision and tree hash of read inputs.
  - **QUALITY 19:** Enforces that receipts run at the revision they stamp inside a materialized clone.
  - As explicitly noted in `reports/round-73/claims.json:57`: "QUALITY 17/19 pin the stamp but nothing forces a post-report rerun to be committed." There is no criterion penalizing a mismatch between the declared verdict in the scorecard and the committed receipt.

---

### Pattern 5: Structural Accounting Drift / Index-Registry Lag

#### Nature & Mechanism
When content changes land (such as adding new `.md` knowledge files, appending `corpus/SOURCES.md` rows, or adding gate scripts), secondary tracking files, table headers, and census documents are not atomically updated. The primary content lands cleanly, but secondary documentation drifts, creating immediate mismatches for subsequent calibration sweeps.

#### Evidence Pointers
1. **Corpus README File-Count Lag in round 72:**
   - `corpus/README.md:732`: Stated `Total knowledge entries: 243.` and `culture-material/ (36)`.
   - `ScoutLedgerSweepA.md:27-29`: Round 72 landed `heritage-taxonomy-models.md` and `heritage-taxonomy-models.amend-2026-10-24-r13.md` in `corpus/knowledge/culture-material/`, bringing actual knowledge files to **245** and culture-material files to **38**. `corpus/README.md` was never updated.
2. **SKILL.md Gate Registry Gap:**
   - `SKILL.md:662-697`: The §Gates and probes registry ends at round 69.
   - `ScoutLedgerSweepB.md:24`: `reports/round-71/` and `reports/round-72/` created `accept-c.py`, `accept-ca.py`, and `accept-d.py`, but none of these five gates were registered in `SKILL.md`.
3. **Stale Line Number Citations in SHONEN.md:**
   - `SHONEN.md:6`: Cited `SKILL.md:468` (Error patterns) and `:522` (Checklist).
   - `ScoutLedgerSweepA.md:30-31`: Due to earlier edits, Error patterns shifted to line 505 and Checklist shifted to line 564.
4. **Heading-vs-Row Off-by-One Drift in Staged Packages:**
   - `corpus/lessons/round-72.md:98`: In `shokuknow/SOURCES-PROPOSED.md`, `## Gate — S864` carries the quote for `S863`. Table headings and row contents drifted out of alignment by one position.

#### The Check That Catches It
An automated repository-wide census validation (`scripts/sources-census.sh validate` combined with `tools/check-corpus-index.py`):
```bash
# 1. Re-derive actual knowledge file count:
ACTUAL_COUNT=$(find corpus/knowledge -type f -name '*.md' | wc -l)
# 2. Extract declared count from corpus/README.md:
DECLARED_COUNT=$(grep -oE 'Total knowledge entries: [0-9]+' corpus/README.md | awk '{print $NF}')
[ "$ACTUAL_COUNT" -eq "$DECLARED_COUNT" ] || exit 1
# 3. Check per-directory partition sums against section headers in corpus/README.md.
```

#### Coverage by Existing QUALITY Criteria (1–21)
- **NOT COVERED.**
  - Existing criteria focus on source admission, citation granularity, receipt stamping, and claim falsifiability. None governs secondary index integrity or repository self-description synchronization.

---

## 3. Comparative Pattern Summary Matrix

| # | Pattern Name | Surface Affected | Key Evidence | Check That Catches It | Covered by QUALITY 1–21? | Proposed Remedy / Criterion |
|---|---|---|---|---|---|---|
| **P1** | Cross-Campaign ID Collision | Entries & Registry (`.md`, `SOURCES.md`) | `conlang-scholarship.md:11` cites `S728` (Qaqet child speech in lane); round-72 era citations `S726`, `S732` | `tools/check-namespace-collisions.py` (URL join verification; zero cross-namespace S-id leaks) | **NO** (Q1 checks existence, Q7 checks separability; neither checks namespace collisions) | **QUALITY 23 (Cross-Campaign ID Isolation)** |
| **P2** | Container / Carrier Shape Misclassification | SOURCES rows & Entry Scoping | `S882` monograph (185 pp.) misclassified as announcement booklet; `S901` editorial leaked "semester-long" token from `S894` | `tools/check-container-shape.py` (pdfinfo pages $>50 \implies$ monograph; token attribution check) | **PARTIAL** (Q6 covers tier scope; Q18 covers anchor quotes; neither detects container misclassification) | Protocol rule in Lesson 73 Gate |
| **P3** | Client-Profile Artifacts & Composed-Slug Illusion | Gate Rejection Discipline | UNESCO live CAPTCHA wall (plain curl blocked, browser UA HTTP 200); Capoeira composed slug (0 captures) vs canonical (135) | Dual-UA curl probe + canonical slug CDX query before ruling "unreachable/walled" | **PARTIAL** (Q21 mandates canonical CDX; Q10 forbids bypass; neither mandates browser UA test) | **QUALITY 22 (UA-Record Clause)** |
| **P4** | Receipt-Verdict Decoupling | Scorecards & Telemetry Receipts | SCORECARD round 72 asserts `PASS 12/12` while `measures-ca.txt` reads `FAIL`; post-report rerun never committed | `tools/check-receipt-verdicts.py` (assert scorecard verdict matches terminal line of committed receipt) | **NO** (Q17/Q19 pin stamp and materialization, but do not enforce scorecard-to-receipt terminal match) | Ca Ledger M1/M2 repair + Gate check |
| **P5** | Structural Accounting Drift | Corpus Index & Registry (`README`, `SKILL`) | `corpus/README.md` stated 243 entries while live find observed 245 after round-72 landing; SKILL gate gap | `tools/check-corpus-index.py` (validate README totals and partition headers against `find` count) | **NO** (Q8/Q9 check declared commands; no criterion enforces index-to-filesystem equality) | Ca Ledger M3/M6 repair + census leg |

---

## 4. Proposed QUALITY Criteria

### 4.1 QUALITY Criterion 22: UA-Record Clause for Source Reachability

Grounded in the round-71 UNESCO CAPTCHA wall artifact (falsified in round 72 by ScoutCDXCanonical), the Capoeira composed-slug falsification (K71-8), and the round-73 `frontier_step.quality_candidate`:

```markdown
22. **Fetch verdicts record User-Agent and test browser profiles before wall rulings** — adds to criterion 10 (ordinary means) and criterion 21 (canonical probe). Every live fetch command in a scout report, gate check, or re-open script must record the exact `User-Agent` string used. No source may be ruled unreachable, paywalled, or blocked by a challenge/CAPTCHA wall based on a plain-tool default User-Agent (such as `curl/*` or `python-requests/*`) alone: the scout or checker must retry the canonical URL using a standard browser-shaped User-Agent (`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`). A source is ruled challenge-walled only when both plain and browser-shaped requests fail or present an insurmountable challenge. In accordance with criterion 10, automated bypass of an active challenge remains strictly prohibited; a challenge met under both user agents is routed around solely via ordinary public copies or archive captures.
```

### 4.2 QUALITY Criterion 23: Cross-Campaign ID-Namespace Isolation

Grounded in Pattern 1 (staged conlang draft citing `S728`, which names Qaqet child-directed speech in the lane registry; staged era drafts citing `S726`, `S732`, `S746`, `S757`; and the stale round-71 renumbering map):

```markdown
23. **Cross-campaign identifiers join by document, never by S-id** — adds to criterion 1 (provenance) and criterion 7 (separability). When assimilating staged entries, amendments, or proposed sources from an external expansion package or branch, identifier numbers are strictly local to their originating namespace. No staged S-id may be cited in an admitted knowledge entry, amendment, or registry row until re-pointed to an unoccupied lane registry identifier ($S \ge \text{next\_free\_id}$) via document URL matching. Any citation of a campaign-internal id that coincides numerically with a preexisting lane identifier naming an unrelated document is a critical provenance defect. Check: `python3 -B tools/check-namespace-collisions.py <entry>` verifies that every S-id token in admitted entries resolves to a registry row whose URL matches the cited work.
```

---

## 5. One Bounded, Non-Obvious Move: The Connector Synthesis

### 5.1 The Strategic Problem: Inter-Claim Second-Order Regressions
In round 72, the lane executed a dual-claim dispatch:
- Claim C (Coverage): Landed heritage-taxonomy entries and registry rows S874/S875.
- Claim Ca (Calibration): Repaired round-71 defects.

While both claims passed their respective internal counters, the landing of Claim C directly broke the repository's calibration surface:
1. Two new `.md` files landed in `culture-material/`, but `corpus/README.md` was not updated, leaving the stated entry count at 243 vs. 245 observed (Defect M1–M3).
2. Two seat reports (`ScoutMergeScan.md`, `ScribeLesson.md`) were left untracked in the worktree (Defect R1).
3. The calibration counter for Ca failed on report evaluation legs (`REPORTCORR`, `REPORTLAST`), and the final report claimed a post-report rerun passed without committing the rerun receipt (Defect R2).

In round 73, history threatens to repeat itself: Claim C lands two conlang entries and rows S876–S880, while Claim Ca establishes the stated-vs-observed ledger. If Claim C lands without an atomic index update, it will immediately invalidate the freshly repaired Ca ledger count (moving 245 $\to$ 247 without documentation). Furthermore, if conlang entries are admitted while retaining staged campaign IDs (`S728`), they will inject semantic corruption into the corpus.

### 5.2 The Proposed Move: "Atomically Coupled Pre-Landing Contract"
Synthesize the Ca ledger's stated-vs-observed verification method into the Claim C landing contract, enforcing three synchronized invariants prior to the freeze commit:

1. **Pre-Landing Index & Ledger Coupling:**  
   Configure `accept-c.py` to enforce that `corpus/README.md` has already been updated to record the post-landing totals (**247 entries**, `linguistics/` partition **32**, vector `30/29/38/32/24/95`) and that the new entries are indexed. Claim C must not land as an "unindexed file addition".
2. **Automated Campaign-ID Re-pointing Gate:**  
   Require `accept-c.py` Leg 3 (`REPOINTED`) to execute a regex scan over the admitted conlang files ensuring:
   - `\bS728\b`, `\bS769\b`, and `\bS806\b` occur **0 times**;
   - All citations resolve to the newly minted S-block (`S876`–`S880`), joined strictly by document URL.
3. **Committed Post-Report Rerun Discipline for Ca:**  
   Resolve defect R2 by mandating that if `accept-ca.py` has report-dependent legs, the post-report rerun receipt (`reports/round-73/telemetry/measures-ca.txt`) must be committed in the final landing commit, proving 100% leg pass at the stamped revision, completely eliminating the unbacked "PASS on rerun" narrative.

### 5.3 Affected Axes
- **Calibration (Claim Ca):** DIRECTLY IMPROVED. Closes routed defects R1 (untracked files committed), R2 (receipt-verdict divergence resolved with committed receipt), and R3 (SKILL gate registry updated for rounds 71–73). Eliminates the recurring pattern of post-report rerun overstatement.
- **Coverage (Claim C):** DIRECTLY IMPROVED. Safely admits the `conlang-scholarship` theme (2 entries, 5 rows S876–S880) onto uncovered ground without campaign-id corruption or broken citation pointers.
- **Discernment & Quality:** NO HARM. Adopts QUALITY criterion 22 (preventing false CAPTCHA/wall rejects) and establishes QUALITY criterion 23 (preventing campaign-id collisions).

### 5.4 Risks & Second-Order Effects
1. **Runtime Surface:** Pre-flight index verification adds minor execution time ($<0.5$s) to `accept-c.py`, well within the test deadline.
2. **Contract Surface:** Prevents Claim C and Claim Ca from conflicting over file ownership; `corpus/README.md` is updated append-only via the standard revision block convention.
3. **Substrate Surface:** Leaves `jj`/`git` state pristine; all checks operate over committed bytes (`git show <lands>:<path>`).

### 5.5 Verification Plan
1. **Pre-data Verification:** Run `python3 -B reports/round-73/accept-ca.py --root . --lands base` to verify that the do-nothing control fails exactly on the declared mismatches (R1 untracked, R2 receipt mismatch, R3 missing gate rows, README 243 vs 245).
2. **Post-data Verification:**
   - Execute `git grep -E '\b(S728|S769|S806)\b' corpus/knowledge/linguistics/conlang-scholarship*.md` $\implies$ 0 hits.
   - Run `python3 -B reports/round-73/accept-c.py --root . --lands <lands>` $\implies$ `ACCEPT-C-73: PASS legs=10/10`.
   - Run `python3 -B reports/round-73/accept-ca.py --root . --lands <lands>` $\implies$ `ACCEPT-CA-73: PASS legs=8/8`.
   - Confirm `reports/round-73/telemetry/measures-ca.txt` is committed and contains `ACCEPT-CA-73: PASS` at `<lands>` with zero failing legs.

---

## 6. Conclusion
The five recurring patterns identified—**ID-Namespace Collision**, **Container Shape Misclassification**, **Client-Profile Wall Illusions**, **Receipt-Verdict Decoupling**, and **Structural Accounting Drift**—explain the vast majority of defects observed across rounds 71–72. Incorporating the **UA-record clause (QUALITY 22)** and the **Cross-Campaign ID-Namespace Isolation clause (QUALITY 23)**, while coupling Claim C's landing to Claim Ca's index accounting, provides a sound, non-obvious architecture that guarantees round 73 advances both coverage and calibration without secondary regression.
