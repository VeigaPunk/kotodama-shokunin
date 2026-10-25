# ConnectorPatterns — Cross-Claim & Cross-Source Pattern Report (Round 74, Wave 1)

**Seat:** `ConnectorPatterns` (leaf connector, hyaku run 7, round 74)  
**Date:** 2026-10-25  
**Lane Root:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`  
**Fleet Root:** `/home/vgpnk/Projects/shokunin`  
**Base Revision:** `f7104cbce186bc2e1522abf0cfd619cc834628bb`  
**Tooling Record:** No tool installed or upgraded. Pre-installed system Python 3.14, `git`, `curl`, and `grep` sufficed. Host-wide pacman pause respected.  
**Download Hygiene:** No new downloads executed. Inspected local repository bytes, staged merge package `/home/vgpnk/Projects/shokuknow/merge/kotodama/` (read-only), prior round wave records (`.ufo/waves/round-73/w2/Mut*.md`), and local wave-1 peer artifacts (`/tmp/q74/`, `.ufo/waves/round-74/w1/Scout*.md`).

---

## 1. Executive Summary & Context Synthesis

Round 74 operates across two declared axes:
1. **Coverage (Claim C):** Assimilation of the `worldbuilding-setting-practice` theme (CJK practitioner craft: Japanese novel-setting blogs, Chinese web-fiction practitioner interviews and reprints) onto uncovered ground. Admits two entries (`corpus/knowledge/culture-material/worldbuilding-setting-practice.md` and `.amend-2026-10-23.md`), opens four new registry rows (`S881`–`S884`), and re-uses pre-existing lane row `S877` (updating `used-by` in place) while refusing duplicate appends.
2. **Calibration (Claim Ca):** Resolution of round-73 closure routed defects 1–5 (tracking six leftover `.ufo/waves/round-73/w2/` seat files, committing missing `PASS`-at-lands receipts, reconciling scenario-count drift, and ensuring census readers parse the latest `corpus/README.md` footer) via an append-only stated-vs-observed ledger (`reports/round-74/ledger.json`, $\ge 10$ pairs).

This report connects:
- **(a) The four theme sources' bibliographic shapes:** two Japanese practitioner blogs (`litmemo.com`, `tuduku.space`), one interview byline chain (`chinawriter.com.cn` 2025 interview from 《文汇报》), one youth magazine reprint (`chinawriter.com.cn` 2022 article from 《青春》), and one pre-existing monograph document (`philol.msu.ru conlangs.pdf` already at lane `S877`);
- **(b) Failure classes from rounds 71–73:** `corpus/lessons/round-71.md`, `round-72.md`, `round-73.md` (`## Mistakes` / `## Corrections`), and `corpus/lessons/round-73-verifier-spotcheck.md`;
- **(c) The Ca ledger methodology & round-73 counter survivors:** the stated-vs-observed pairs in `ledger.json` and the mutation test survivors in `.ufo/waves/round-73/w2/MutPredicateC.md`, `MutLedgerCa.md`, `MutLandedCa.md`, and `MutLandedC.md`.

Across these surfaces, this report establishes **five recurring failure patterns** that predict where rows, entries, counters, and self-assessments fail. For each pattern, we provide concrete evidence pointers, the check that catches it, and an evaluation of existing criteria in `corpus/QUALITY.md` (1–24). We propose the exact text for **QUALITY criterion 25** ($\le 8$ lines) and formulate one bounded, non-obvious connector synthesis move.

---

## 2. Five Recurring Failure Patterns

### Pattern 1: Staging-Pipeline Shift & False Rejection Laundering (URL $\leftrightarrow$ Quote Mispairing)

#### Nature & Mechanism
In multi-source batch-staging pipelines (such as `corpus-expansion-1` producing `SOURCES.append.md` and `absent-defect-register.md`), row data frequently experiences an off-by-one index slip or copy-paste transposition. A live URL $N$ is paired with the quoted anchor text belonging to URL $N-1$ or with an unrelated quote from a completely different domain or language.

When reviewers or quarantine scouts verify the row, they search for the paired quote on URL $N$, find 0 occurrences, and rule the source `payload-absent` or `refused`. The source is cataloged as a dead or fabricated payload, when in reality the host is 100% live (HTTP 200 under browser UA), topically relevant, and carries the author's key conceptual terminology. The quarantine mechanism thus launders a clerical staging error into a permanent rejection of authoritative material.

#### Evidence Pointers
1. **Quarantine Refusal of Chinawriter Sources S816 and S817:**
   - In `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:129-130`:
     - Row `S816` (URL `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html`, 爱潜水的乌贼 2025 《文汇报》 interview) was paired with the quoted span: `这个我肯定考虑过。我自己就是资深读者…`.
     - Row `S817` (URL `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html`, 爱潜水的乌贼 2022 《青春》 reprint) was paired with the quoted span: `Sowers-Wills's 'Phonology from the inside out…'` (an English linguistics paper by Anderson et al., S901/S894!).
   - In reality, `grep -n '这个我肯定考虑过'` on the 2022 page (`32582252.html:220`) hits **1 occurrence** (the author's statement on worldbuilding disclosure pace), while the 2025 page (`40494534.html:215`) carries the famous worldbuilding order quote: `我先做的是世界观，再考虑怎么升级，再考虑升级的表现`.
   - The staging pipeline transposed the 2022 quote onto the 2025 row (`S816`) and injected an English conlang quote onto the 2022 row (`S817`). Rounds 68 and 71 quarantine-refused both as `payload-absent` without checking cross-row shifts.
2. **Precedents in Round 72:**
   - `corpus/lessons/round-72.md:98`: In `shokuknow/SOURCES-PROPOSED.md`, `## Gate — S864` carried the quote for `S863`.
   - `corpus/lessons/round-72.md:109-110`: Staged row `S934` was a duplicate of `S903` wearing Słon's Poland identity; staged `S936` was `S918` wearing 潘蕾 2014 identity.
3. **LitMemo Blog Staged Section Misalignment:**
   - `.ufo/waves/round-74/w1/ScoutLitmemo.md:83-87`: Staged row `S883` cited section `「小説の世界観はどう作る？」節` (0 hits) and `設定資料集 を本文とズレさせない3ステップ 節` (0 hits as section; it was the link text of a card pointing to a separate article).

#### The Check That Catches It
A staging-batch bidirectional locator and language-consistency lint (`tools/check-staging-alignment.py`):
1. **Language/Character Consistency:** Assert that a URL on a CJK domain does not carry an ASCII/Latin-only anchor quote (and vice-versa).
2. **Matrix Shift Diagnostic:** When a quote fails on URL $N$, search for that exact string across URLs $N-1$, $N+1$, and all URLs in the same staged batch. If found on URL $M$, flag as `STAGING_ALIGNMENT_SHIFT(N -> M)` rather than `PAYLOAD_ABSENT`.
3. **Re-quoting Mandate:** For any live HTTP 200 page proposed for quarantine refusal, require the scout to extract the page's actual `<title>`, `<h1>`, and top-level headings to confirm whether the document itself is on-topic before ruling it dead.

#### Coverage by Existing QUALITY Criteria (1–24)
- **NOT COVERED.**
  - **QUALITY 12 (Re-test stated rejection grounds):** Mandates recording verbatim tool output of the re-test, but accepts `grep` exit 1 on the declared pair without checking whether the quote was mispaired.
  - **QUALITY 18 (Row anchors resolvable on page):** Applies only to admitted rows, not to the quarantine triage that filters staged rows before admission.

---

### Pattern 2: Cross-Campaign ID-Namespace Collision & Phantom Re-use

#### Nature & Mechanism
Repositories undergoing sequential expansion operate across three distinct identifier spaces:
1. **Staged expansion namespace:** `S859`..`S990` in `shokuknow/merge/kotodama/SOURCES.append.md`;
2. **Expansion defect register namespace:** `S776`..`S835` in `absent-defect-register.md`;
3. **Lane canonical registry namespace:** `S001`..`S880` in `kotodama-shokunin/corpus/SOURCES.md`.

When staged knowledge entries are drafted during expansion campaigns, authors cite provisional staged IDs or campaign IDs. If these entries are imported into the lane without strict by-document re-pointing:
- An entry cites a campaign ID that numerically collides with an existing, unrelated lane row (e.g. citing `S728` for a conlang conference paper when lane `S728` is a study on Qaqet child-directed speech in Papua New Guinea).
- An expansion package proposes appending a document that already exists in the lane under an earlier ID (e.g. staged `S882` proposing `philol.msu.ru conlangs.pdf`, which already exists in the lane registry as `S877`). Appending it creates a duplicate-URL violation (census warning W04 / error E04).

#### Evidence Pointers
1. **Duplicate Monograph Row in Round 74:**
   - Staged package `SOURCES.append.md:30` proposes appending row `S882` for Sidorova & Shuvalova (2006) `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf`.
   - Lane registry `corpus/SOURCES.md:832` already carries this exact document at row `S877` (admitted in round 73). Appending `S882` would duplicate the document.
   - `reports/round-74/claims.json:15` explicitly notes: "staged S882 is NOT appended: its document already holds lane row S877... S877's used-by changed in place old->new and logged."
2. **Round-72 Campaign ID Leakage:**
   - `corpus/lessons/round-72.md:97`: Staged era-periodization amendments cited campaign IDs `S726`, `S732`, `S746`, `S757`, all pointing to unrelated lane documents.
3. **Counter Case-Sensitivity Blind Spot:**
   - `.ufo/waves/round-73/w2/MutPredicateC.md:59-60, 227-243` (F7): The counter's REPOINTED leg caught uppercase `(S894)` (`TOKEN_RE = r"\bS\d{3,}\b"`), but mutant P5b containing lowercase `(staged s894)` survived as `PASS legs=11/11`.

#### The Check That Catches It
A canonical URL uniqueness check and case-insensitive token validator (`tools/check-id-namespaces.py`):
1. **URL Pre-Existence Gate:** Before appending any staged row, check its canonical URL against `corpus/SOURCES.md`. If URL exists at row $S_k$, forbid appending a new row; require re-pointing entry citations to $S_k$ and updating $S_k$'s `used-by` cell.
2. **Case-Insensitive Identifier Lint:** Scan all admitted entry prose with `(?i)\b(?:staged\s*)?s[0-9]{3,}\b`. For every matched token, assert that its numeric value maps to an admitted row in the round's declared row set or pre-existing lane registry, and assert that the document cited in prose matches the registry row.

#### Coverage by Existing QUALITY Criteria (1–24)
- **NOT COVERED.**
  - **QUALITY 1 (Provenance):** Checks that sources are cited, but is satisfied if an ID exists in `SOURCES.md`, even if it points to an unrelated document.
  - **QUALITY 7 (Claim separability):** Enforces intra-round file and ID independence between claims, but does not govern imports from external staging namespaces.

---

### Pattern 3: Dynamic Graded-Tree Config Leak / Contract-Shrinking Survivors

#### Nature & Mechanism
An acceptance counter is declared as an objective test oracle to verify that a landed commit satisfies the round's claim. However, if the counter loads its configuration (such as `row_set`, `entries`, `rejects`, or expected `legs`) dynamically from `reports/round-<N>/claims.json` located inside the graded tree (`<lands>`) or falls back to the active worktree, the graded object controls its own evaluation criteria.

A defective or adversarial landing can edit `claims.json` at `<lands>`, removing difficult requirements (e.g. reducing required rows from 5 to 2, deleting refused-file checks, or removing legs), and the counter will execute against the shrunken contract and report a clean pass.

#### Evidence Pointers
1. **MutPredicateC Blocker Finding F1 (Round 73):**
   - `.ufo/waves/round-73/w2/MutPredicateC.md:64, 71-104`: Mutant P7b rewrote `claims.json` at lands so that `row_set` contained only `[{"id": "S876"}, {"id": "S877"}]`, added only two rows, stubbed the second entry, and ran the frozen counter:
     ```
     $ python3 -B reports/round-73/accept-c.py --root . --lands b88f66f69d2b
     # config source: lands tree: row_set, entries...
     ACCEPT-C-73: PASS legs=11/11
     ```
   - The counter passed 11/11 even though claim C's frozen declaration required five rows (`S876`..`S880`).
2. **Ca Counter Worktree Leak (Round 73 Mistakes R73-M5):**
   - `corpus/lessons/round-73.md:112`: `accept-ca.py` r1 read the ledger from the uncommitted worktree because a dict was passed to `git -C`. Its selftest passed because worktree and commit agreed.
3. **Round-74 Draft Claims Warning:**
   - `reports/round-74/claims.json:3`: "A rule changed after any seat scores landed data is not the claim's rule."
   - `reports/round-74/claims.json:124`: Identifies `quality_candidate` as "QUALITY 25 — a counter reads its constants from the frozen commit and ships junk-landing controls (R73 routed defect 4)".

#### The Check That Catches It
Immutable freeze oracle binding:
1. **Mandatory `--freeze <40hex>` Argument:** The counter must require `--freeze <commit>` on the CLI (or hardcode the frozen digest as a constant).
2. **Frozen Config Loader:** The counter reads `claims.json` and `ledger.json` strictly via `git show <freeze>:<path>`, never from `<lands>` and never from the worktree.
3. **Immutability Assertion:** The counter verifies that `git diff <freeze> <lands> -- reports/round-<N>/claims.json` is strictly empty.

#### Coverage by Existing QUALITY Criteria (1–24)
- **NOT COVERED.**
  - **QUALITY 14 (Judged object stays frozen):** Guards entry bytes and reviewer packets during blind adjudication, but does not regulate counter execution or `claims.json` loading.
  - **QUALITY 17/19 (Receipt stamping & clone execution):** Enforces that the counter runs in a clone at the stamped revision, but does not prevent the counter from loading mutated configuration from that same clone.

---

### Pattern 4: Circular Truth & Degenerate Constant-Printers in Verification Ledgers

#### Nature & Mechanism
In a stated-vs-observed calibration ledger (Claim Ca), each row declares an `observe_cmd` to re-derive ground truth from repository bytes and compare it against `stated_token`. If the `observe_cmd` does not genuinely read and depend on repository state, but instead prints a hardcoded constant or evaluates an environment variable, the observation is decoupled from repository bytes.

Similarly, if an observe command targets an artifact that the landing commit itself creates or appends to (such as grep-ing for an author-invented marker in `LOG.md`), truth becomes completely circular: the repair author creates the evidence that makes their own observation pass. Furthermore, when `rederive` commands in correction rows are checked only for string presence rather than executed, invalid commands pass undetected.

#### Evidence Pointers
1. **MutLedgerCa Major Survivors (Round 73):**
   - `.ufo/waves/round-73/w2/MutLedgerCa.md:16-30, 34-40`:
     - **M1b:** `observe` command `["python3","-c","import os;assert os.sep;print(str(505))"]` survived (`PASS legs=9/9`); the counter's clone-read guard was satisfied by `os.sep` while the printed token was hardcoded.
     - **M2b:** `observe` command `["wc","-l","/dev/null"]` survived (`PASS legs=9/9`) because `wc` was an allowlisted binary operating on a non-repo constant.
     - **M3b:** `observe` command `["grep","-c","R73-CIRCULAR","LOG.md"]` survived because the repair author appended the marker line to `LOG.md` in the exact same landing commit.
     - **M5:** `rederive` command yielded 38 while the row claimed 245; it survived because `NOSTUB` verified string presence, not execution.
     - **M9:** `observe` command reading `os.environ['LC_ALL']` returned `C.UTF-8` injected by the counter's own environment wrapper.
     - **M10:** An in-place edit of `reports/round-72/telemetry/measures-ca.txt` (`FAIL` $\to$ `PASS`) made a committed correction row false while all 9 legs stayed green.
2. **Round-73 Verifier Spot-Check Routing:**
   - `corpus/lessons/round-73-verifier-spotcheck.md:87` (Routed defect 4): Explicitly flags "ledger constant-printers" for round-74 hardening.

#### The Check That Catches It
A dual-clone canary probe and tracked-input constraint (`tools/check-ledger-integrity.py`):
1. **Canary Perturbation Test:** During counter selftest or ledger verification, execute each `observe_cmd` in a secondary clone where the target file has been perturbed (or deleted). If `observe_cmd` prints the exact same token in both the pristine and perturbed clones, reject it as a constant-printer.
2. **Tracked Base-File Target:** Require that the primary file argument of any allowlisted binary (`grep`, `wc`, `cat`, `sha256sum`) is a tracked file existing at `<base>`, and forbid targeting paths modified by the landing commit for pairs lacking `statement_after`.
3. **Execution of Rederive Commands:** Execute the `rederive` command in a controlled subshell and assert that its stdout contains the observed token.

#### Coverage by Existing QUALITY Criteria (1–24)
- **NOT COVERED.**
  - **QUALITY 11 (Each claim clause is shown able to fail):** Applies to claim declarations, but does not audit the internal command semantics of ledger observe scripts.
  - **QUALITY 17/19:** Pins revision hashes, but does not inspect whether commands evaluate constants or circular inputs.

---

### Pattern 5: Receipt-vs-Verdict Decoupling & Narrative Overstatement

#### Nature & Mechanism
A calibration failure where summary documentation (`SCORECARD.md`, `SHONEN.md`, or the round's report) declares a passing verdict (e.g. `ACCEPT-CA-72 PASS legs=12/12`), but the committed telemetry receipt backing that statement reads `FAIL` or is absent entirely.

This occurs when an integrator experiences gate failures on legs that depend on the unfiled report itself (e.g. `REPORTCORR`, `REPORTLAST`), files the report claiming that a subsequent rerun passed, but fails to commit the rerun receipt. The repository is left in an unbacked state where public declarations contradict committed test evidence.

#### Evidence Pointers
1. **Round-72 Routed Defect R2:**
   - `SCORECARD.md:1401`: Calibration row asserted `ACCEPT-CA-72 PASS legs=12/12`.
   - `reports/round-72/telemetry/measures-ca.txt`: Committed receipt read `LEG FAIL REPORTCORR`, `LEG FAIL REPORTLAST`, `ACCEPT-CA-72: FAIL legs=12/12`.
   - `.ufo/reports/round-72/kotodama.md:27`: Stated that a post-report rerun passed, but **no rerun receipt was committed**.
   - `corpus/lessons/round-72-verifier-spotcheck.md:31` & `corpus/lessons/round-73.md:109` (R73-M2): Routed as defect R2, requiring ledger pair `L06`.
2. **Round-73 Verifier Spot-Check Finding:**
   - `corpus/lessons/round-73-verifier-spotcheck.md:15`: "Defect: no committed PASS-at-lands receipt for either counter. The only ACCEPT-C-73/ACCEPT-CA-73 lines under reports/round-73/telemetry/ are FAIL controls (controls-c.txt 1/11; controls-ca*.txt 4/9–5/9)."
   - `MutLedgerCa.md:44`: Landed-bytes finding confirms that no `measures-ca.txt` was committed under `reports/round-73/telemetry/`.

#### The Check That Catches It
A mechanical receipt-verdict reconciliation leg (`RECEIPTS` leg in `accept-ca.py`):
1. **Scorecard & Report Extraction:** Parse `SCORECARD.md` and `.ufo/reports/round-<N>/kotodama.md` for all patterns matching `ACCEPT-<CLAIM>-<ROUND>\s*:\s*PASS\s+legs=([0-9]+)/([0-9]+)`.
2. **Receipt Verification:** Assert that for each claimed pass, there exists a committed file `reports/round-<N>/telemetry/measures-<claim>.txt` (or `-rerun.txt`) whose terminal line matches the claimed pass verbatim.
3. **Stamp Alignment:** Assert that `# stamped revision:` equals `# evaluated revision:` equals `<lands>`, and that the process exit code recorded in the receipt was 0.

#### Coverage by Existing QUALITY Criteria (1–24)
- **NOT COVERED.**
  - **QUALITY 17/19:** Mandates that receipts pin revision hashes and run in clones, but as explicitly acknowledged in `reports/round-73/claims.json:57`: "QUALITY 17/19 pin the stamp but nothing forces a post-report rerun to be committed." There is no existing criterion that fails a claim when the scorecard asserts a pass unevidenced by a committed receipt.

---

## 3. Comparative Pattern Summary Matrix

| # | Pattern Name | Graded Surface | Key Concrete Evidence | Catching Check | Existing QUALITY Coverage? | Proposed Resolution |
|---|---|---|---|---|---|---|
| **P1** | Staging Shift / Mispairing | Registry rows & Quarantine | Chinawriter S816/S817 swapped quotes in `absent-defect-register.md:129-130`; S883 blog section mismatch | `check-staging-alignment.py`: cross-row search on failed quotes; language consistency lint | **NO** (Q12 checks re-test output; Q18 checks admitted rows; neither detects cross-row shift) | Stage-shift lint & live re-quoting |
| **P2** | Cross-Campaign ID Collision | Knowledge entries & `SOURCES.md` | Staged S882 conlangs.pdf duplicates lane S877; conlang draft cited Papua New Guinea S728; MutPredicateC P5b `(staged s894)` | `check-id-namespaces.py`: URL uniqueness in `SOURCES.md`; case-insensitive token scan `(?i)\bs\d+\b` | **NO** (Q1 checks existence; Q7 checks intra-round separability; neither catches external ID collisions) | By-document URL joins & reused-row in-place update |
| **P3** | Dynamic Config Leak | Acceptance counters (`accept-*.py`) | `MutPredicateC.md` F1: P7b rewrote `claims.json` at lands to 2 rows and passed 11/11; R73-M5 worktree read | Counter mandates `--freeze <rev>`; reads config strictly via `git show <freeze>:<path>`; asserts empty diff | **NO** (Q14 freezes judged objects in review; Q17/19 pin stamps; neither restricts config loading) | **QUALITY 25 (Freeze config & junk controls)** |
| **P4** | Circular Truth / Constant Printers | Ledger pairs & `accept-ca.py` | `MutLedgerCa.md`: M1b `import os; assert os.sep`, M2b `wc -l /dev/null`, M3b `grep R73-CIRCULAR LOG.md`, M5 unexecuted rederive | Dual-clone canary execution in selftest; target path must be tracked at `<base>` and unappended in lands | **NO** (Q11 checks claim clauses; Q17/19 pin stamps; neither inspects command semantics) | Ledger canary probe in `--selftest` |
| **P5** | Receipt-vs-Verdict Decoupling | Scorecards, Reports & Telemetry | Round-72 SCORECARD asserted `PASS 12/12` while `measures-ca.txt` read `FAIL`; round-73 committed 0 PASS receipts | `check-receipt-verdicts.py`: assert scorecard verdict matches terminal line of committed telemetry receipt | **NO** (Q17/19 pin stamp grammar, but do not enforce scorecard-to-receipt terminal match) | Counter `RECEIPTS` binding leg |

---

## 4. Proposed Shape of QUALITY Criterion 25

In accordance with the prompt specification ($\le 8$ lines), grounded in round-73 `MutPredicateC` finding F1, `MutLedgerCa` survivors, and round-73 verifier spot-check routed defect 4:

```markdown
25. **A counter reads its configuration from the frozen commit and ships junk-landing controls** — adds to criteria 11, 14, 19 and 23. A round counter takes `--freeze <commit>` (or embeds the frozen digest) and loads its row sets, entries, refused lists, and ledger definitions strictly from `<freeze>` (via `git show <freeze>:<path>` or clone), never falling back to `<lands>` or the worktree, failing closed if `<lands>` modifies declared configuration. Every counter ships paired junk-landing controls in its pre-data telemetry: at least one stub-entry landing, one un-remapped staged-row landing, and one forged-evidence landing must each demonstrably fail their specific legs under the frozen counter. Grounded in round-73 `MutPredicateC` (P7b rewritten claims.json passed 11/11) and R73 routed defect 4.
```

---

## 5. One Bounded, Non-Obvious Move: The Connector Synthesis

### 5.1 The Strategic Problem: Second-Order Tension Across Coverage and Calibration
In round 74, the two declared claims exhibit a direct structural tension:
- **Claim C (Coverage):** Assimilates four theme sources (`litmemo.com`, `tuduku.space`, `chinawriter.com.cn` 2025 interview, `chinawriter.com.cn` 2022 reprint) and re-uses conlang monograph `S877`. However, two of these sources (`S899`/`S900`) were previously quarantine-refused in rounds 68/71 due to URL $\leftrightarrow$ quote mispairing (Pattern 1), while `litmemo` and `tuduku` carry staged locator and count discrepancies. Furthermore, as proven by `MutPredicateC` F3, a landing that satisfies header schemas with filler text and zero quoted body spans can pass `ENTRIES` 11/11.
- **Claim Ca (Calibration):** Establishes the stated-vs-observed ledger to repair round-73 routed defects (untracked files, missing PASS receipts, scenario-count drift, README footer reading). However, as proven by `MutLedgerCa` (M1b/M2b/M5), ledger observe commands can be subverted by constant-printers or author-appended circular targets, while `MutPredicateC` F1 proved that a landing can rewrite `claims.json` to pass vacuously.

If Claim C and Claim Ca proceed under disconnected verification gates, round 74 risks admitting entries with unanchored filler or mispaired quotes, while Claim Ca risks accepting constant-printing observe commands that provide an illusion of calibration.

### 5.2 The Proposed Move: "Pre-Freeze Dual-Boundary Contract: Immutable Freeze Oracle Coupling with Bidirectional Quoted-Span Enforcement"
Synthesize the verification mechanisms of Claim C and Claim Ca into a single, cohesive pre-freeze contract enforcing three synchronized guarantees:

1. **Immutable Freeze Oracle Coupling (Fixing Pattern 3):**
   Mandate that both `accept-c.py` and `accept-ca.py` take `--freeze <commit>` and load `claims.json` and `ledger.json` strictly from that commit. In addition, `accept-c.py` Leg 1 (`SEPARABLE`) asserts that `git diff <freeze> <lands> -- reports/round-74/claims.json` is empty. This prevents any landing from altering its own grading criteria.
2. **Bidirectional Quoted-Span Enforcement (Fixing Pattern 1 & MutPredicateC F3):**
   Couple Claim C's `ENTRIES` leg to `EVIDENCE`: for each cited row (`S881`, `S882`, `S883`, `S884`, `S877`), the entry body must contain at least one verbatim quoted span ($\le 25$ words) that occurs within that row's committed evidence window. This guarantees that:
   - The re-quoted Chinawriter spans (rescued from the round 68/71 quarantine mispairing) actually appear in and anchor the worldbuilding entry prose.
   - Filler entries with zero quoted spans (MutPredicateC P1 survivor) are mathematically impossible to land.
   - Staged S882 re-use (lane `S877`) is verified to be cited by the entry, with `S877`'s `used-by` cell updated in place and tracked in the ledger.
3. **Selftest Canary Mutation Scenario (Fixing Pattern 4):**
   Incorporate an active canary scenario into `accept-ca.py --selftest`: execute the ledger's observe commands against a synthetic fixture where target tokens are altered. Any observe command that produces the expected token on both the pristine and perturbed fixture is flagged as a degenerate constant-printer (`OBSERVE_CONSTANT_DETECTED`), failing the selftest.

### 5.3 Affected Axes
- **Coverage (Claim C):** DIRECTLY IMPROVED. Safely assimilates the `worldbuilding-setting-practice` theme (two entries, rows `S881`–`S884`, re-used `S877`) onto uncovered ground, anchored by verified verbatim practitioner quotes rather than filler or mispaired stubs.
- **Calibration (Claim Ca):** DIRECTLY IMPROVED. Closes round-73 routed defects 1–5, eliminates constant-printing observe commands, and binds filed scorecard verdicts to committed telemetry receipts.
- **Discernment & Quality:** NO HARM (STRENGTHENED). Embeds the principles of QUALITY 25 directly into the pre-data counter architecture.

### 5.4 Risks & Second-Order Effects
1. **Runtime Surface:** Reading configuration via `git show <freeze>:<path>` is an in-memory blob lookup taking $<0.05$s. The selftest canary scenario adds $<0.2$s. Total runtime overhead is negligible.
2. **Contract Surface:** Zero ambiguity between draft claims and landed bytes: the freeze commit hash serves as the cryptographic boundary.
3. **Substrate Surface:** Clean separation of concerns; no git index or working tree mutation; all inspections occur over committed revisions.

### 5.5 Verification Plan
1. **Pre-Data Verification (Freeze Commit):**
   - Run `python3 -B reports/round-74/accept-c.py --selftest` and `accept-ca.py --selftest`: assert exit 0 and commit receipts under `reports/round-74/telemetry/`.
   - Run do-nothing controls at `lands == base`: assert `controls-c.txt` prints `FAIL` and `controls-ca.txt` prints `FAIL` on declared mismatch pairs.
   - Run junk-landing controls: assert that a stub entry with zero quotes fails `ENTRIES`, and an observe command using `print(str(505))` fails the canary check.
2. **Post-Data Verification (Landed Commit):**
   - Run `python3 -B reports/round-74/accept-c.py --root . --lands <lands> --freeze <freeze>` $\implies$ `ACCEPT-C-74: PASS legs=11/11`.
   - Run `python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin` $\implies$ `ACCEPT-CA-74: PASS legs=10/10`.
   - Verify `reports/round-74/telemetry/measures-c.txt` and `measures-ca.txt` are committed with `# stamped revision:` == `# evaluated revision:` == `<lands>`.

---

## 6. Conclusion

By systematically tracing the five failure patterns—**Staging-Pipeline Shift**, **Cross-Campaign ID Collision**, **Dynamic Graded-Tree Config Leak**, **Circular Ledger Truth**, and **Receipt-Verdict Decoupling**—round 74 avoids the pitfalls that affected rounds 71–73. Codifying **QUALITY 25** and enacting the **Pre-Freeze Dual-Boundary Contract** guarantees that both coverage and calibration advance robustly, leaving no unverified claims or vacuous counter survivors.
