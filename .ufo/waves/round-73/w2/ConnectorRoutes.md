# ConnectorRoutes — cross-claim, cross-source pattern and route report (round 73, wave 2 = FALSIFY)

**Seat:** `ConnectorRoutes` (leaf connector, hyaku run 7, round 73, wave 2)  
**Lane Root:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`  
**Fleet Root:** `/home/vgpnk/Projects/shokunin`  
**Landed Revision:** `0316b8883b4f8d44b8efd720140e7f52f734a102` (base `8841ad3b896a0227674fa0725b818c999118046f`)  
**Frozen Claims:** `reports/round-73/claims.json` (freeze commit `af65165cf269db346ef872e16a656eccd7264d01`)  
**Tooling Record:** No tool installed or updated. System Python 3.14.8, `git` 2.56.0, `curl` 8.23.0 preinstalled and sufficient. `pacman` untouched (orchestrator host-wide pause respected).  
**Download Hygiene:** No scratch downloads performed outside local repo inspection; peer fetch artifacts consulted in `reports/round-73/evidence/`, `.ufo/waves/round-73/w1/`, and local telemetry receipts.

---

## 1. Executive Summary & Context Synthesis

Round 73 operated across two declared axes:
1. **Coverage (Claim C, assimilation-sourced):** Assimilated the `conlang-scholarship` theme from `/home/vgpnk/Projects/shokuknow/merge/kotodama/` onto uncovered ground, admitting two entries (`corpus/knowledge/linguistics/conlang-scholarship.md` and `conlang-scholarship.amend-2026-10-23.md`), appending five new registry rows (`S876`–`S880`) to `corpus/SOURCES.md`, and re-pointing all citations by document.
2. **Calibration (Claim Ca, records):** Resolved round-72 routed defects R1–R3 and formalized an append-only stated-vs-observed ledger (`reports/round-73/ledger.json`, 8 pairs) to detect and repair discrepancies between declarative statements (in `SCORECARD.md`, `SHONEN.md`, `corpus/README.md`, `SKILL.md`) and observed repository bytes.

Wave 1 (34 of 37 seats reporting) exposed major vulnerabilities in both claims:
- Claim C's draft predicate was satisfiable without opening any source (`CritCCounterVacuity.md`), while staged entries leaked campaign IDs (`S728`, `S769`, `S806`) naming unrelated lane documents (`RevClaimsFidelity.md`).
- Claim Ca's draft `observe_cmd` was an unconstrained shell string allowing vacuous constant echoes, and its `BASEMISMATCH` was under-scoped (`CritCaVacuity.md`).

When landed data was first graded at commit `85f17eb` (C) and `e62d731` (Ca), both claims experienced immediate second-order breakages:
- Claim C failed `GROUND`, `SCRATCHMIRROR`, and `COLLCHECK` because committed pre-data receipts did not match the shapes expected by `accept-c.py` (R73-M6).
- Claim Ca failed `SEPARABLE` because Claim C's `corpus/README.md` footer cited `S876`, and Ca's counter r1 silently fell back to reading an uncommitted worktree ledger due to a bug in `load_ledger` passing a dict to `git -C` (R73-M5).
Both claims required emergency counter revisions (`r2`, `r3`) and a post-grading repair commit (`0316b88`).

This report details **six recurring defect patterns** across claims C and Ca, proves each with verbatim reproducing commands and outputs, evaluates coverage under QUALITY criteria 1–23, defines concrete routed actions for round 74, and establishes exact sentence-level cross-reference hooks connecting round 73's landed rows to the lane's older foundational entries.

---

## 2. Six Recurring Defect Patterns

### Pattern 1: Artifact-Shape vs Counter-Leg Mismatch Caught Only at First Grading (Late Grading / Base-Only Blindness)
**Severity:** MAJOR

#### Mechanism
Pre-dispatch validation runs counters only at `lands == base` (the do-nothing control) or in isolated synthetic selftest fixtures. At `lands == base`, pre-committed telemetry artifacts (`gap-sweep.txt`, `validate-receipt.txt`, `id-renumber-map.json`) do not exist, so every artifact-reading leg fails for the generic reason "file missing". Consequently, subtle shape mismatches between what the counter legs parse and what the pre-data scripts actually output remain completely invisible until the *landed* data commit is graded. The landing commit then immediately scores red, forcing hurried mid-flight repairs.

#### Evidence Pointers
1. **Claim C Pre-Data Receipt Format Mismatch (R73-M6):**  
   At commit `85f17eb`, when landed entries were first graded, `accept-c.py` failed `GROUND`, `SCRATCHMIRROR`, and `COLLCHECK`:
   - `gap-sweep.txt` printed regex-escaped domain fragments rather than the literal tokens the counter searched for.
   - `validate-receipt.txt` omitted the row-id list required by the counter.
   - `id-renumber-map.json` placed assignments directly in a top-level JSON list rather than under a `"map"` object key.  
   This forced emergency repair commit `0316b8883b4f8d44b8efd720140e7f52f734a102`.
2. **Reproducing Command (running `accept-c.py` at freeze commit `af65165`):**  
   Running the counter against the freeze commit `af65165` (where receipts exist but landing is absent) directly exposes these exact shape failures:
   ```bash
   python3 -B reports/round-73/accept-c.py --root . --lands af65165cf269db346ef872e16a656eccd7264d01
   ```
   *Verbatim Output:*
   ```
   # round-73 acceptance counter — claim C (conlang-scholarship assimilation)
   # counter sha256 (self): 95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416
   # stamped revision: af65165cf269db346ef872e16a656eccd7264d01
   # evaluated revision: af65165cf269db346ef872e16a656eccd7264d01
   # measured revision (lane main): 0316b8883b4f8d44b8efd720140e7f52f734a102
   # tree: 7b50777ed53b124e984d9945d8369568be51a02d
   # base revision: 8841ad3b896a0227674fa0725b818c999118046f
   ...
   LEG FAIL GROUND
        receipt does not name ojs.unito.it; receipt does not name philol.msu.ru; receipt does not name journals.rudn.ru; receipt does not name cyberleninka.ru/article/n/klassifikatsii; receipt does not name sanders.phonologist.org
   ...
   LEG FAIL SCRATCHMIRROR
        receipt does not carry S876, S877, S878, S879, S880; no registry-append commit reachable from lands for S876
   LEG FAIL COLLCHECK
        .ufo/waves/round-73/assimilation/id-renumber-map.json has no map object; map records no old->new for S876; map records no old->new for S877; map records no old->new for S878; map records no old->new for S879; map records no old->new for S880
   ACCEPT-C-73: FAIL legs=1/11
   ```
3. **Claim Ca Worktree Ledger Bug (R73-M5):**  
   In `accept-ca.py` revision r1, `load_ledger` passed the clone dict instead of a path to `git -C`:
   ```bash
   git diff 3537899^! reports/round-73/accept-ca.py
   ```
   *Verbatim Output:*
   ```diff
   --- a/reports/round-73/accept-ca.py
   +++ b/reports/round-73/accept-ca.py
   @@ -404,7 +404,8 @@ def load_ledger(root, clone, lands, ledger_arg):
        """(obj, source, sha, raw, error). source: 'lands' | 'worktree-uncommitted'."""
        rel = ledger_arg
        if not os.path.isabs(rel):
   -        r = git(clone, "show", "%s:%s" % (lands, rel))
   +        r = git(clone["path"] if isinstance(clone, dict) else clone,
   +                "show", "%s:%s" % (lands, rel))
            if r.returncode == 0:
                raw = r.stdout
   ```
   Because `r.returncode != 0`, the counter silently fell back to reading the worktree ledger (`source=worktree-uncommitted`). In r1's selftest, worktree and commit agreed, so the bug was invisible until grading the first landed commit `e62d731` (`reports/round-73/counter-revisions.md:6`).

#### Coverage by QUALITY Criteria (1–23)
- **QUALITY 8/9:** Check that declared commands run on declared inputs before dispatch, but running on `lands == base` is blind to post-base receipt shapes.
- **QUALITY 23:** Drafted in round 73 specifically to catch this:  
  `"...the counter is also run at the FREEZE commit (receipts present, landing absent) so artifact-vs-leg shape mismatches show before data..."` (`corpus/QUALITY.md:77`).
- **Was that catch exercised? NO.**  
  While the sentence was appended to `QUALITY.md` in commit `0316b88`, **no freeze-commit control receipt** (e.g. `controls-c-freeze.txt` or `controls-ca-freeze.txt`) was ever committed under `reports/round-73/telemetry/`. The telemetry directory holds only `controls-c.txt` and `controls-ca.txt` stamped at base `8841ad3b896a0227674fa0725b818c999118046f`. The catch was formulated in prose after the defect bit, but never evidenced in telemetry.

#### Routed Action for Round 74
Enforce in round-74 dispatch gates that every counter must ship a committed freeze-commit receipt (`reports/round-74/telemetry/controls-*-freeze.txt` with `--lands <freeze_sha>`) proving that all pre-committed receipts parse cleanly and that the only remaining failing legs are those that assert the landing commit itself.

---

### Pattern 2: Asymmetrical UA-Gated Direction Errors (Mono-UA Wall Illusions)
**Severity:** MAJOR

#### Mechanism
Scouts probing candidate source URLs rely on a single User-Agent profile (either default `curl` or a standard Chrome browser UA), observe an HTTP error or challenge interstitial (e.g., HTTP 403, 429, Cloudflare challenge, or CAPTCHA), and declare the source "walled", "bot-blocked", or "unreachable". The fatal flaw is assuming that server gating is monotonic or that browser UAs always penetrate better. In practice, servers gate in **both directions**: some block default command-line tools while serving browsers, while others (such as academic publishers like Springer) serve full payloads to command-line tools while triggering JS challenges on browser profiles.

#### Evidence Pointers
1. **Springer Chapter Asymmetry in Round 73 (R73-M3):**  
   `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15` (staged row S910).  
   When fetched with browser UA, Springer served a 3,038-byte HTML challenge shell (`<title>Client Challenge</title>`). When fetched with plain `curl/8.7.1`, it served the complete 325,225-byte chapter. Scouts in wave 1 and round-72 notes had treated Springer as an impassable wall based on browser-UA probing alone (`corpus/lessons/round-73.md:48, 110`).
   ```bash
   grep -n "Client Challenge" corpus/lessons/round-73.md
   ```
   *Verbatim Output:*
   ```
   48:| conlang-scholarship.amend-2026-10-23b.md | S909, S910 | status: UA "curl/8.7.1" -> HTTP 200, 325225 B, wall absent; retry UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 3038 B, wall present ("Client Challenge"); automation: none; the Springer chapter page serves in full under the plain UA and is walled under the browser UA, so an unreachability ground would be VOID (QUALITY 22); S909 (MGIMO PDF) is reachable HTTP 200, 5824942 B with its nine-field abstract span present; neither row is cited by an admitted entry — adoption stays at the five declared rows (CORPUS rule 4) | a later round that takes the amendment as its theme and re-opens S909/S910 by ordinary means | https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15 ; https://doi.org/10.1007/978-3-032-03277-5_15 ; https://mgimo.ru/upload/iblock/c34/vestnik-mgimo-2015-1-40.pdf | not adopted |
   110:| R73-M3 stale-premise | wave-1 seats and the round-72 Routed-to-73 notes read a Springer/Cambridge "wall" from one UA each; measured here: Springer `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15` answers HTTP 200 / 325225 B to `curl/8.7.1` and HTTP 200 / 3038 B `Client Challenge` to the browser UA; Cambridge answers 429 / 1302 B to both | QUALITY 21 probes the canonical slug, not the UA | QUALITY 22 (UA bound to its response, both directions) with `reports/round-73/telemetry/quality22-controls.txt` filed; the S894/S910 Gate rows are its first applications | fixed |
   ```
2. **UNESCO ICH Elements Reverse Asymmetry in Round 71/72:**  
   In round 71, `ScoutOpenSourcesC` refused eight UNESCO elements asserting "live CAPTCHA walls" using default `curl` (`corpus/lessons/round-71.md:33-39`). In round 72, `ScoutCDXCanonical` demonstrated that using a browser UA returned HTTP 200 with full 154,144-byte narrative payloads (`corpus/lessons/round-72.md:103`).
3. **Cambridge University Press Genuine Rate Limit (staged S894):**  
   `https://doi.org/10.1017/cnj.2024.21` returned HTTP 429 (1,302 B) with a `__cf_bm` challenge cookie under *both* UAs, confirming that the block was a genuine rate limit rather than UA gating (`corpus/lessons/round-73.md:47`).

#### Coverage by QUALITY Criteria (1–23)
- **QUALITY 21:** Mandated canonical-slug CDX querying, but ignored client User-Agent headers.
- **QUALITY 22:** Created in round 73 (`corpus/QUALITY.md:66-75`), requiring every Gate rejection line opening with `wall:`, `captcha:`, or `status:` to bind both `curl/8.7.1` and browser-shaped UA to their respective response status, byte count, and marker.
- **Was that catch exercised? YES.**  
  Verified mechanically by `reports/round-73/telemetry/quality22-controls.txt`:
  ```bash
  cat reports/round-73/telemetry/quality22-controls.txt
  ```
  *Verbatim Output:*
  ```
  # QUALITY 22 controls (red-before): GROUND / SHAPE / automation counts over three fixture Gate lines
  GROUND='^[|*-].*\| *(wall|captcha|status):'
  SHAPE='UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent).*UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'
  missing: GROUND=1 SHAPE=0 automation-none=0 -> FAIL
  compliant: GROUND=1 SHAPE=1 automation-none=1 -> PASS
  automation: GROUND=1 SHAPE=1 automation-none=0 -> FAIL
  real lesson corpus/lessons/round-73.md: GROUND=2 SHAPE=2 automation-none=2 -> PASS
  ```

#### Routed Action for Round 74
Incorporate dual-UA probing into `tools/reopen-row.py` so that automated source verification tests both `curl/8.7.1` and Chrome UA automatically, emitting exit 1 if a scout rejects a source that serves full payload under either profile.

---

### Pattern 3: Cross-Campaign ID and Namespace Collisions & Semantic Contamination
**Severity:** BLOCKER (if unmitigated, injects corrupted, false attributions into corpus knowledge)

#### Mechanism
Identifiers are strictly local to the campaign or staging directory in which they are coined. Three independent S-id namespaces currently overlap:
1. Staged package: `S859`..`S990` (`shokuknow/merge/kotodama/SOURCES.append.md`);
2. Quarantine / absent-defect register: `S776`..`S835` (`absent-defect-register.md`);
3. Lane registry: `S001`..`S875` (before round 73).
When external drafts are imported into the lane, if an entry retains an un-remapped campaign ID that numerically coincides with an existing lane registry row, it results in catastrophic semantic corruption: an entry discussing constructed linguistics cites an S-id that in the lane registry points to child speech in New Guinea or Ayurvedic medicine.

#### Evidence Pointers
1. **Staged Conlang Draft Citing Qaqet Child Speech:**  
   In `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md:11`:
   ```bash
   grep -n "S728" /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md
   ```
   *Verbatim Output:*
   ```
   11:- gap filled: `linguistics/conlang-methodology.md` cites Rosenfelder, Peterson, Okrent and Higley for craft and WALS, PHOIBLE and APiCS for typology. Round 1 added a conference paper (S728) because no venue could be reached. This entry establishes that peer-reviewed venues exist, and that the literature is not English-only.
   ```
   Checking what `S728` actually names in the lane registry (`corpus/SOURCES.md:683`):
   ```bash
   grep -E '^\s*\|\s*S728\s*\|' corpus/SOURCES.md
   ```
   *Verbatim Output:*
   ```
   | S728 | Henrike Frye, 2022 "Corrective input", Child-directed Speech in Qaqet: A Language of East New Britain, Papua New Guinea - https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf ; capture https://web.archive.org/web/20250505204752id_/https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf | book | B | Frye’s secondary account of Schieffelin’s report on Kaluli maternal elema prompting for child utterance correction | § 8.1 Previous research on corrective input, paragraph 1: "Kaluli mothers use elema ‘say it like this’ to prompt the children to correct" | Helps worldbuilders represent children learning explicit utterance correction from caregivers. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-sociolinguistics-registers.md |
   ```
2. **Additional Colliding Campaign IDs in Staged Amendments:**
   - Staged `conlang-scholarship.amend-2026-10-23c.md:14` cited `S769`, which in the lane registry is Iona & Peter Opie's *The Lore and Language of Schoolchildren* (`corpus/SOURCES.md:724`).
   - Staged `conlang-scholarship.amend-2026-10-24.md:42` and `conlang-methodology.amend-2026-10-24.md:17` cited `S806`, which in the lane registry is Jaiswal & Williams, "A glimpse of Ayurveda" (`corpus/SOURCES.md:761`).
3. **Hardcoded Prohibition in Round-73 Counter:**  
   Because no general rule existed, `accept-c.py` had to hardcode an explicit blacklist:
   ```bash
   grep -n "DEFAULT_FORBIDDEN" reports/round-73/accept-c.py
   ```
   *Verbatim Output:*
   ```
   122:DEFAULT_FORBIDDEN = ("S728", "S769", "S806")
   ```

#### Coverage by QUALITY Criteria (1–23)
- **QUALITY 1 (Provenance):** Forbids invented sources, but `S728` exists in the registry—it is simply the wrong document.
- **QUALITY 7 (Claim separability):** Governs inter-claim lands within a single round, not external staging imports.
- **QUALITY 15 (Clause-scoping):** Checks MULTI-ID and TABLE-ID, but is blind to ID-to-document semantics.
- **QUALITY 1–23 DO NOT COVER THIS PATTERN.**  
  While `ConnectorPatterns.md` in wave 1 recommended QUALITY 23 for namespace isolation, the actual QUALITY 23 adopted by the round was assigned to counter selftest receipts.
- **Was that catch exercised? NO**, as a quality criterion; it was only enforced ad-hoc via Claim C's `REPOINTED` leg.

#### Routed Action for Round 74
Codify **QUALITY 24 (Cross-Campaign Namespace Isolation)**: No staged S-id may be cited in an admitted knowledge entry, amendment, or registry row until re-pointed to an unoccupied lane identifier ($S \ge \text{next\_free\_id}$) via document URL matching. Implement `tools/check-namespace-collisions.py` to assert that zero pre-existing lane S-ids appear in staging drafts unless the cited document URL and title match the lane registry verbatim.

---

### Pattern 4: Self-Hosted Denominators and Unconstrained Observe Commands
**Severity:** MAJOR

#### Mechanism
In calibration claims or self-assessment ledgers (such as Round-73 Ca, Round-72 Ca, or Round-69 Ca2), the author of the claim authors:
(a) the set of pairs to evaluate,
(b) the denominator (e.g. "finds $\ge 8$ mismatches"),
(c) the `observe_cmd` that recomputes ground truth from committed bytes.
This allows two distinct forms of vacuity:
1. **Unconstrained Execution:** An author can supply an unconstrained command (such as `echo 245`) that always outputs the expected value, decoupled from actual repo state.
2. **Denominators Without Scope:** An author chooses a small, easily repaired subset of errors (e.g. 2 untracked files) to satisfy "$\ge 8$ pairs", while dozens of identical errors across the repository remain untracked and unmeasured.

#### Evidence Pointers
1. **CritCaVacuity Finding on Draft Ca Predicate:**  
   In wave 1, `CritCaVacuity.md:28-37` pointed out that in `reports/round-72/accept-ca.py`, the `REPORTCORR` leg was a substring test that passed even on the do-nothing control at base (`reports/round-72/telemetry/controls-ca.txt:13`). In the draft round-73 ledger, `observe_cmd` was an unrestricted string that could be satisfied by `echo <expected>`.
2. **Selective Untracked-File Denominator:**  
   Ledger pair L01–L08 tracked exactly 2 files in `.ufo/waves/round-72/w1/` (`ScoutMergeScan.md` and `ScribeLesson.md`). Meanwhile, `git status` / `git ls-files --others` at base held **62 untracked files** across the repository (`CritCaVacuity.md:51-56`). The claim asserted that "all unannotated mismatches were repaired", when only an author-selected sub-inventory was evaluated.
3. **Hardened Allowlist Added to `accept-ca.py`:**  
   In response to wave-1 critique, `accept-ca.py` was forced to introduce an explicit allowlist and AST-level checks on `observe_cmd`:
   ```bash
   grep -A 8 "OBSERVE_ALLOWLIST" reports/round-73/accept-ca.py
   ```
   *Verbatim Output:*
   ```python
   OBSERVE_ALLOWLIST = {
       "git": ["ls-tree", "show", "cat-file", "log", "diff", "status"],
       "python3": ["-c", "-B"],
   }
   ```

#### Coverage by QUALITY Criteria (1–23)
- **QUALITY 8/9/11:** Check that declared commands run and are able to fail, but do not prevent authors from restricting the denominator to a compliant sub-population or authoring trivial commands.
- **Was that catch exercised? NO.**  
  Enforcement exists only in round-73 `accept-ca.py` internal logic.

#### Routed Action for Round 74
Establish standardized, repository-wide measurement domains for calibration claims (e.g., repository-wide untracked file counts via `git ls-files --others --exclude-standard`, complete inventory scans across all partition directories, and exhaustive gate registries).

---

### Pattern 5: Receipt-Verdict Decoupling and Unverified Rerun Overstatements
**Severity:** MAJOR

#### Mechanism
A public summary document (`SCORECARD.md`, `SHONEN.md`, or a fleet report) asserts a passing gate verdict (e.g. "ACCEPT-CA-72 PASS legs=12/12 at the measured revision"), but the committed telemetry receipt backing that statement reads `FAIL`. This occurs when an author runs a gate check before all carrying documents are filed, encounters failures on report-dependent legs (`REPORTCORR`, `REPORTLAST`), files the report claiming that a subsequent rerun passed, but fails to commit the passing rerun receipt. A paired failure occurs when a scorecard cites a tool's `--selftest` mode as evidence, but no selftest receipt was committed and the tool's selftest actually fails at HEAD.

#### Evidence Pointers
1. **Round-72 Defect R2 (SCORECARD PASS vs Receipt FAIL):**  
   `SCORECARD.md:1401` claimed: `ACCEPT-CA-72 PASS legs=12/12 at the measured revision`.  
   Running a check against the committed receipt `reports/round-72/telemetry/measures-ca.txt`:
   ```bash
   tail -n 5 reports/round-72/telemetry/measures-ca.txt
   ```
   *Verbatim Output:*
   ```
        commits=10 report-names-lands=False
   LEG PASS NOHARM
        census exit=0
   ACCEPT-CA-72: FAIL legs=12/12
   exit=1
   ```
   The scorecard statement was false as filed, requiring ledger pair L06 in round 73 to annotate the failure and commit `reports/round-73/telemetry/measures-ca72-rerun.txt` (PASS 12/12 at `21ad3088`).
2. **Round-72 Defect R73-M4 (Unreceipted Failing Selftest):**  
   `SCORECARD.md:1402` and `round-72.md` cited `accept-c.py --selftest` without committing a receipt.  
   Running the round-72 counter's selftest at the round-73 base:
   ```bash
   python3 -B reports/round-72/accept-c.py --selftest
   ```
   *Verbatim Output:*
   ```
   SELFTEST: 10/11
   --- clean fixture: expected PASS 10/10, got exit=1
   LEG PASS ENTRIES
   LEG PASS ROWS
   LEG PASS REPOINTED
   LEG PASS GATE
   LEG PASS REJECTS
   LEG FAIL GROUND
        receipt missing: reports/round-72/telemetry/gap-sweep.txt
   LEG PASS CITEDLINES
   LEG PASS CENSUS
        exit=0 head=2fabb50fa08f last-line=kotodama	ok	stub
   LEG PASS SCRATCHMIRROR
   LEG PASS COLLCHECK
   ACCEPT-C-72: FAIL legs=10/10
   ```
   The selftest was red at HEAD (`exit=1`), recorded as mistake R73-M4 (`corpus/lessons/round-73.md:111`).

#### Coverage by QUALITY Criteria (1–23)
- **QUALITY 17/19:** Pin measured revision, tree hash, and materialized clone execution, but do not compare the text of `SCORECARD.md` with the terminal line of the receipt.
- **QUALITY 23:** Mandated committing selftest receipts and red-before controls.
- **Was that catch exercised? PARTIALLY.**  
  Exercised for selftests (`reports/round-73/telemetry/selftest.txt`, `selftest-r2.txt`, `selftest-r3.txt`). But mechanical reconciliation between `SCORECARD.md` verdict text and `measures-*.txt` terminal lines remains unexercised by any quality check.

#### Routed Action for Round 74
Implement `tools/check-receipt-verdicts.py` to parse every `ACCEPT-*-*` verdict declared in `SCORECARD.md` and assert exact string and exit-code matching against the terminal lines of the corresponding `reports/round-*/telemetry/measures-*.txt` receipts at the stamped revision.

---

### Pattern 6: Structural Accounting Drift / Index-Registry Lag
**Severity:** MINOR

#### Mechanism
When content changes land (such as adding `.md` knowledge files, appending `corpus/SOURCES.md` rows, or introducing gate scripts), secondary tracking files (`corpus/README.md` entry counters and directory section headers), gate registries (`SKILL.md`), and cross-file line citations (`SHONEN.md`) are not atomically updated. The primary payload lands cleanly, but secondary documentation drifts immediately, creating maintenance backlog and invalidating subsequent calibration sweeps.

#### Evidence Pointers
1. **README File-Count Lag in Round 72 (Ledger Pairs L01, L02, L03):**  
   Round 72 landed two knowledge entries in `culture-material/`, bringing total knowledge entries to 245 and culture-material entries to 38. However, `corpus/README.md` remained un-updated at base `8841ad3`:
   ```bash
   git show 8841ad3b896a0227674fa0725b818c999118046f:corpus/README.md | grep -E '(Total knowledge entries|culture-material/ \()' -n
   ```
   *Verbatim Output:*
   ```
   407:## culture-material/ (36)
   732:Total knowledge entries: 243.
   ```
2. **SKILL.md Gate Registry Omission (Ledger Pair L08):**  
   `SKILL.md` §Gates and probes ended at round 69 (`accept-o-69`). Five gates added in rounds 71 and 72 (`accept-c-71`, `accept-ca-71`, `accept-d-71`, `accept-c-72`, `accept-ca-72`) were never registered in `SKILL.md` until repaired in round 73.
3. **SHONEN.md Pointer Drift (Ledger Pairs L04, L05):**  
   `SHONEN.md:6` cited `SKILL.md:468` (Error patterns) and `:522` (Checklist). Prior edits had shifted these sections to lines 505 and 564.
4. **Resolution in Round 73:**  
   To prevent round 73 from re-introducing drift when Claim C added 2 more knowledge entries (245 $\to$ 247), Claim C appended a dated footer to `corpus/README.md`:
   ```bash
   git show 0316b8883b4f8d44b8efd720140e7f52f734a102:corpus/README.md | tail -n 4
   ```
   *Verbatim Output:*
   ```
   Total knowledge entries: 247.

   Counts checked 2026-10-25 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 247 files; directory totals 32/29/38/29/24/95 — linguistics 30 + 2, culture-material 36 → 38 per the L02 correction). The inventory command `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` counts markers, not verified facts.
   ```

#### Coverage by QUALITY Criteria (1–23)
- **QUALITY criteria 1–23 do not cover secondary index synchronization or line-number maintenance.**
- **Was that catch exercised? NO.**

#### Routed Action for Round 74
Add an index-reconciliation check to `scripts/sources-census.sh validate` that verifies `corpus/README.md` file counts and partition headers against `git ls-tree` of `corpus/knowledge/`, and verifies `SKILL.md` §Gates against all `reports/round-*/accept-*.py` scripts.

---

## 3. Comparative Pattern Summary Matrix

| # | Pattern Name | Severity | Primary Surface | Key Evidence | Covered by QUALITY 1–23? | Exercised in R73? | Routed Action for Round 74 |
|---|---|---|---|---|---|---|---|
| **P1** | Artifact-Shape vs Counter Mismatch at First Grading | MAJOR | Pre-data Telemetry Receipts & Counters | `accept-c.py` at `af65165` fails GROUND/SCRATCHMIRROR/COLLCHECK; Ca worktree ledger bug r1 | QUALITY 23 (added in `0316b88`) | **NO** (no freeze-commit control receipt committed) | Commit `controls-*-freeze.txt` (`--lands <freeze_sha>`) before falsify dispatch |
| **P2** | Asymmetrical UA-Gated Direction Errors | MAJOR | Gate Rejection Discipline & Re-openers | Springer chapter (S910) 3,038 B Client Challenge under Chrome UA vs 325,225 B under curl | QUALITY 22 | **YES** (`quality22-controls.txt` & S894/S910 rows) | Embed dual-UA curl into `tools/reopen-row.py`; invalidate "wall" if either UA passes |
| **P3** | Cross-Campaign ID Collisions & Semantic Contamination | BLOCKER | Entries & SOURCES Registry | Staged `conlang-scholarship.md:11` cites `S728` (Qaqet child speech in lane registry) | **NO** (Q1, Q7, Q15 blind to external staging collisions) | **NO** (only ad-hoc blacklist in `accept-c.py`) | Enact **QUALITY 24** (Cross-Campaign Namespace Isolation) + `tools/check-namespace-collisions.py` |
| **P4** | Self-Hosted Denominators & Unconstrained Commands | MAJOR | Calibration Claims & Ledgers | Draft `observe_cmd` allowed `echo 245`; R1 checked 2 files while base had 62 untracked | QUALITY 11 (partial) | **PARTIALLY** (`accept-ca.py` command allowlist) | Standardize objective repository-wide measurement domains (e.g. repo-wide `ls-files`) |
| **P5** | Receipt-Verdict Decoupling / Unverified Rerun | MAJOR | Scorecards & Telemetry Receipts | `SCORECARD:1401` claimed PASS while `measures-ca.txt` read FAIL; `accept-c-72 --selftest` exits 1 | QUALITY 17/19 (stamp), QUALITY 23 (selftest receipt) | **PARTIALLY** (selftest receipts committed; scorecard matching unexercised) | Implement `tools/check-receipt-verdicts.py` to match scorecard claims against receipt tails |
| **P6** | Structural Accounting Drift / Index-Registry Lag | MINOR | Corpus Index & Gate Registries | README stated 243 entries vs 245 observed; SKILL gate gap (L01–L05, L08) | **NO** | **NO** | Add index and gate registry reconciliation checks to `sources-census.sh validate` |

---

## 4. Cross-Reference Connections to Lane's Foundational Entries

Round 73 landed five new registry rows (`S876`–`S880`) and two new knowledge entries:
- `corpus/knowledge/linguistics/conlang-scholarship.md` (Enguehard 2022 [S876], Sidorova & Shuvalova 2006 [S877]);
- `corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` (Novikov 2022 [S878], Kostyukhin 2023 [S879], Anderson/Grant/Sanders 2024 [S880]).

In later rounds, the following three foundational entries should cross-reference these landed assets. Below are the **exact sentence-level hooks** (do not edit now; for future round adoption):

### 1. `corpus/knowledge/linguistics/conlang-methodology.md`
- **Target Hook 1 (Stage 0 — Society vs Phonemes, line 36):**  
  *Existing text:*
  > "Rule (Rosenfelder 2010; Peterson 2015): start from the society, not the phonemes. Okrent 2009 documents how the great failures of the genre — a priori philosophical languages — collapsed by ignoring how real languages live inside real communities."  
  *Sentence-level hook to append:*  
  > "Novikov (2022, S878) refines this dichotomy by arguing that the a priori / a posteriori distinction operates as a continuous scale rather than a binary division, because an inventor's native linguistic worldview inevitably structures even supposed a priori systems (`linguistics/conlang-scholarship.amend-2026-10-23.md` §1)."
- **Target Hook 2 (Stage 2 — Phonotactics & Name Generation, line 50):**  
  *Existing text:*
  > "Test: write 20 personal names and 10 place names from phonotactics alone. If you reach outside the inventory, fix the inventory or fix the ambition. Names are the language's first public surface (couples `naming-systems.md`)."  
  *Sentence-level hook to append:*  
  > "To calibrate the required grammatical and lexical depth for naming languages versus literary media, apply Henning's volume rule as documented by Sidorova & Shuvalova (2006, S877), which demonstrates that character and place naming requires strict phonotactics but no extensive inflectional apparatus (`linguistics/conlang-scholarship.md` §4)."

### 2. `corpus/knowledge/linguistics/naming-systems.md`
- **Target Hook 1 (Section 1 — The frame: four name systems plus one force, line 42):**  
  *Existing text:*
  > "Working rule: every name in the ledger records three things — a **claim** (who may say it, when, in which language), a **fossil** (of an older language, regime, or taboo), and a **spell** (what in-world happens if it is said)."  
  *Sentence-level hook to append:*  
  > "When establishing a naming language for characters and toponyms without building a full conversational grammar, follow Henning's volume rule (Sidorova & Shuvalova 2006, S877): a naming language requires phonotactic rules and a curated root list, but no dedicated syntax or morphological inflection (`linguistics/conlang-scholarship.md` §4)."
- **Target Hook 2 (Section 2 — Anthroponymy: the slot system, line 61):**  
  *Existing text:*
  > "The **name lexicon** is a distinct semantic field: archaic, sacred, or legally curated roots that ordinary speech has lost (couples semantic-fields-lexicon-building)."  
  *Sentence-level hook to append:*  
  > "Kostyukhin's (2023, S879) comparison of personal-language taxonomies confirms that personal and naming registers naturally prioritize lexical curation over grammatical complexity (`linguistics/conlang-scholarship.amend-2026-10-23.md` §2)."

### 3. `corpus/knowledge/synthesis/conlang-blueprint-template.md`
- **Target Hook 1 (Section 0 — Brief, scope, and reference passport, line 18):**  
  *Existing text:*
  > "Working language ID: [ ]; specification version: [ ]; requested scene uses: [ ]; era/locality: [ ]; variation to represent: [ ]; recipient: lore-shokunin."  
  *Sentence-level hook to append:*  
  > "Classify the project's purpose under the taxonomy of Sidorova & Shuvalova (2006, S877; artlang 2.1 vs personal language 2.2) and determine whether the design target is a cultural jargon, a naming language, or a full narrative vehicle per Henning's volume rule (`linguistics/conlang-scholarship.md` §§3–4)."
- **Target Hook 2 (Section 1 — Phoneme inventory, line 32):**  
  *Existing text:*
  > "Framework: contrastive phonology plus the International Phonetic Alphabet (International Phonetic Association 1999); choose a coherent contrast system, not a list of evocative letters."  
  *Sentence-level hook to append:*  
  > "The pedagogical model of Sowers-Wills, reported by Anderson, Grant & Sanders (2024, S880), shows that pairing natural-language phonological systems with typological universals provides an optimal scaffold for introductory language construction (`linguistics/conlang-scholarship.amend-2026-10-23.md` §3)."
- **Target Hook 3 (Section 3 — Morphology and grammatical commitments, line 60):**  
  *Existing text:*
  > "Framework: inflection versus derivation, synthesis versus segmentation, and morphology–phonology interfaces (Haspelmath & Sims 2010); these dimensions vary within a language."  
  *Sentence-level hook to append:*  
  > "Novikov (2022, S878) warns that Standard Average European structures frequently bleed into purportedly alien morphological designs, demonstrating that grammatical choices reflect the creator's cultural baseline unless explicitly defamiliarized (`linguistics/conlang-scholarship.amend-2026-10-23.md` §1)."

---

## 5. Verification on Landed Revision (`0316b8883b4f8d44b8efd720140e7f52f734a102`)

The landed revision cleanly passes both acceptance counters:

1. **Claim C Counter:**
   ```bash
   python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102
   ```
   *Result:* `ACCEPT-C-73: PASS legs=11/11` (all legs green: ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK).
2. **Claim Ca Counter:**
   ```bash
   python3 -B reports/round-73/accept-ca.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102 --fleet-root /home/vgpnk/Projects/shokunin
   ```
   *Result:* `ACCEPT-CA-73: PASS legs=9/9` (all legs green: LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, NOSTUB, APPENDONLY, SEPARABLE, TRACKED, STAMP).

---

## 6. Explicit Disclosure of What Could NOT Be Checked

1. **Live Network Probing of Paywalled Publishers:**  
   Could not execute live re-fetches against Cambridge University Press (`doi.org/10.1017/cnj.2024.21`, staged S894) beyond what was captured in wave 1 telemetry; attempting to bypass the Cloudflare HTTP 429 response or solve interstitials is strictly forbidden by QUALITY criteria 10 and 16.
2. **Unadopted Expansion Packages:**  
   Did not check the validity of candidate amendments outside the admitted theme (e.g. `naming-systems.amend-*`, `calendar-*`, `era-*`); these are explicitly quarantined for future rounds.
3. **Sibling Lane Working Trees:**  
   Did not mutate or run tests in sibling lanes; cross-lane gap sweep evidence was verified strictly from committed telemetry (`reports/round-73/telemetry/gap-sweep.txt`).
4. **Lane Mutability:**  
   Executed strictly as a leaf member; no lane files outside this report were created or modified.
