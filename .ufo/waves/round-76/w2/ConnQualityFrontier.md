# ConnQualityFrontier — round 76 wave 2 (leaf, read-only falsification)

Scope: connect the source-census frontier, the R76-M1 attribution criterion, and the C/Ca counter failures. Evidence is committed bytes at the cited revisions. Two measurement receipts are not committed; they are marked `UNCOMMITTED` where used.

Revisions: base `98c486bdb4650ba5b8e651d332910e8ee60ad121`; freeze `df0f0309d61e5485bb17035d3f8791b1e6a11d40`; Ca landing `a43ed807ea38b5fc5a7875a839d576cea73aba7c`; C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a`. All four resolve in the lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. They do **not** resolve in `/home/vgpnk/Projects/shokuknow`, which is the read-only source repo; no source-repo bytes were used.

Tooling: read `/home/vgpnk/.omp/agent/RULES.md`. No tool installed or upgraded. No pacman transaction. No scratch directory created. No build, test, linter or formatter run. Only `git show`, `git grep`, `git ls-tree`, `git diff` and file reads were used.

## Verdict

- **C (coverage): FAILS as declared.** Final measure at C landing `722e69f`: `ACCEPT-C-76: FAIL legs=11/13` (`UNCOMMITTED`, `reports/round-76/telemetry/measures-c.txt`, untracked in the lane). Failing legs: ROWS and COLLCHECK. The 11 passes include `INDEX` twice, so 10 of 12 distinct legs pass.
- **Ca (calibration): FAILS as declared, and the landed lesson under-reports it.** Final measure at Ca landing `a43ed80` with combined `722e69f`: `ACCEPT-CA-76: FAIL legs=5/12` (`UNCOMMITTED`, `reports/round-76/telemetry/measures-ca.txt`, untracked). Seven legs fail: LEDGER, REPAIR, ANNOTATE, NOSTUB, R1EXEMPT, SEPARABLE, COMBINED. The landed lesson's routed paragraph names only two of them (L76-13, L76-19), although it instructs "report their exact failing legs".
- **R76-M1 criterion (QUALITY 29): binds the wrong thing.** It correctly governs number-to-named-artifact for the three round-75 sizes (L76-05/17/18). It does not govern whether the named artifact is the statement the ledger claims to test. L76-13 and L76-19 both pass through that gap.
- **Coverage axis moved, governance axis did not.** The C landing adds one knowledge file (252→253), three registry rows (817→820) and the `GB/T 33661` ground (base grep: 0 matches). Census is clean. The same landing also writes non-row lines into the registry and resolves the showGb alias by literal URL. Both are governance harms. I report the contradiction without smoothing it into a score.

## 1. Source-census frontier (committed evidence)

| fact | evidence |
|---|---|
| Base registry 817 rows, A491/B310/C16 | `git show 98c486b:corpus/SOURCES.md` rows counted by tier column |
| Lands registry 820 rows, A493/B311/C16 | `git show 722e69f:corpus/SOURCES.md`; rows S894–S896 at lines 849–851 |
| Registry diff is 8 insertions | `git diff --stat 98c486b 722e69f -- corpus/SOURCES.md` |
| Two identified non-row lines among the 8 insertions (the other 3 rows are S894–S896; 3 further insertions unidentified) | `722e69f:corpus/SOURCES.md:854` (`- calendar-standard design — S896 → S895 → S894 …`) and `:902` (`**State-standard calendar compilation (round 76).** Question …`) |
| Census exit 0, no E-code | `reports/round-76/telemetry/census-end.txt` (committed at 722e69f); grep for E-codes returns 0; final line `kotodama ok …` |
| New ground is absent at base | `reports/round-76/telemetry/gap-sweep.txt` (committed): `GB/T 33661` base matches 0; `news.gmw.cn/...content_24559485.htm` 0; `openstd.samr.gov.cn/bzgk/std/newGbInfo` 0 |
| Knowledge files 252→253 | `git ls-tree -r --name-only 98c486b|722e69f -- corpus/knowledge \| grep -c '\.md$'` |

The census is clean. The frontier moved on coverage. Two governance problems sit in that same landing:

1. **Non-row registry lines (ROWS leg).** `722e69f:corpus/lessons/round-76.md:85` (R76-M3) calls these "study-path/search-log appends" and routes them without a fix. The frozen ROWS predicate reads any added line outside `row_set` as a violation, so the FAIL is honest as declared. The lane still wrote non-row content into the authoritative registry in the same landing that claims "no pre-existing row status/recheck/used-by changed".
2. **showGb alias (COLLCHECK leg).** Frozen pre-data decision `C-P3` (`df0f030:reports/round-76/claims.json`, `pre_data_corrections`) says: "Collapse the showGb 302 alias and newGbInfo target into one registry-record document." The frozen map record `S938 → S895` (`df0f030:.ufo/waves/round-76/assimilation/id-renumber-map.json`) names `…/std/showGb?type=online&hcno=…`. The row `S895` names `…/newGbInfo?hcno=…`. The counter's literal URL compare therefore rejects the map, even though the decision it implements says the two are one document.
   - Factual support for the alias exists in the committed stage: `df0f030:.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S896-openstd.showGb-followed-2026-10-27.html` and `…/S896-openstd.newGbInfo-live-2026-10-27.html`. The showGb capture is a body with the same `国家标准|GB/T 33661-2017` title. The 302 header itself is not in the file.
   - Diagnosis: a counter-implementation gap against the frozen `C-P3` decision, not a factual error in the map. The claim still fails as declared under its frozen leg. CritMapAlias owns the detailed trace.

## 2. R76-M1 attribution: criterion and where it stops

- The mined mistake is `corpus/lessons/round-76.md:83`: "a number read from a staged copy or probe is filed as though measured from a different committed artifact". The fix is `corpus/QUALITY.md:199` (criterion 29), grounded at `:203`, with red/green evidence at `:201` against `.ufo/waves/round-76/w1/stage/RevengerMistakes/recurrence.txt`.
- The criterion works for the three staged-copy sizes. The round-75 lesson states `6862 B`, `5933 B`, `2514 B` at `98c486b:corpus/lessons/round-75.md:92–94`. The committed lane files are `30920`/`24166`/`23049` (Ca ledger L76-05/17/18, observed at base and at Ca landing). Those are correctly re-derived.
- The criterion does not stop the next three cases.

### 2a. L76-13: the stated artifact is not the round-75 statement (attribution recurrence)

The Ca ledger is frozen at `df0f030:reports/round-76/ledger.json`, pair `L76-13`:
- `stated_at`: `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:8`
- `stated_text`: `byte counts 111487 / 225123 / 1085244 / 697092 / 45238`
- `expected_after`: `109588`

Three committed numbers for the same S885 notice page:

| value | artifact |
|---|---|
| 109588 | `98c486b:reports/round-75/evidence/S885.txt:5` (`bytes: 109588`); the receipt |
| 111486 | `98c486b:corpus/lessons/round-75.md:28` (`HTTP 200, 111486 B`); the round-75 statement the claim is about |
| 111487 | `98c486b:corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:8`; a knowledge file, not a round-75 statement |

- The round-75 lesson number is 111486, not 111487. L76-13 therefore does not test a round-75 landed statement at all. It tests a knowledge-file line. The Ca counter catches this only through its path allowlist (LEDGER: "not one of the frozen append-only files") and SEPARABLE ("forbidden read `corpus/knowledge/**`"). Criterion 29 does not catch it, because the sentence does name its artifact (the knowledge file) and the criterion is satisfied.
- The knowledge file's own line 8 also disagrees with the committed receipt (111487 vs 109588). That is a second R76-M1-class number inside a lane artifact at base. Cause not established.
- The SCORECARD row (`a43ed80:SCORECARD.md:1526`, `| L76-13 | 111487 | 109588 | …`) records the knowledge-file token as the "old token", so the correction row carries the same mis-attribution.

### 2b. L76-19: a real mismatch behind a line-wrapped quote

- `df0f030:reports/round-76/ledger.json`, `L76-19`: `stated_at` `corpus/lessons/round-75.md:48`; `stated_text`: `S892's window (`chars=4097 before=284`)`; `expected_after`: `2020`.
- At base, `corpus/lessons/round-75.md:47–48` is wrapped: line 47 ends with `S892's`, line 48 begins `(`chars=4097 before=284`)`. The counter searches per line, so the two-line quote is "not found". The value `284` **is** on line 48.
- The receipt is `98c486b:reports/round-75/evidence/S892.txt:13`: `window: chars=4097 min=4096 pad=400 before=2020 after=2026`. So the mismatch 284 vs 2020 is real.
- The landed lesson states the counter's finding as "stated value not found at the specified lesson line" (`722e69f:corpus/lessons/round-76.md:89`). That wording is itself inaccurate: the value is found; the wrapped quote is not. This is a second attribution slip, in the routed text.

### 2c. Correction rows are not the frozen rederive commands (verbatim claim is false)

`a43ed80:SCORECARD.md:1535` says the correction table "is a verbatim projection of the 19 ANNOTATE pairs". Compared with the frozen `ledger.json` `rederive` field:
- L76-01…L76-18 (except L76-16, a REPAIR with no row): command identical.
- L76-19 (`SCORECARD.md:1531`): ledger `git grep -h -E ^window: chars= …` vs row `git grep -h -E '^window: chars=' …`. Quoting added.
- L76-20 (`:1532`) and L76-21 (`:1533`): ledger `git grep -h -o -E ^sha256: [0-9a-f]{8} …` vs row `git grep -h -o -E '^sha256: [0-9a-f]{8}' …`. Quoting added.

The frozen ledger's unquoted `rederive` strings are not executable under the counter's argv parser (uncommitted `measures-ca.txt`: "L76-19 treats `chars=` as a path operand"; "L76-20/21 treat the base revision as a path operand"). So three ANNOTATE rows fail as NOSTUB/ANNOTATE, while the lane's SCORECARD calls the projection verbatim. The re-typed commands are the lane's fix; the frozen ledger was not.

### 2d. REPAIR statement does not match its frozen pattern

- `ledger.json` `L76-16` REPAIR: `statement_after` requires `^\| accept-c-75 \|.*?committed counter sha256 `([0-9a-f]{12})``.
- `a43ed80:SKILL.md:707` contains `315c5f3f27fd…` but not the phrase `committed counter sha256 \``. The REPAIR leg fails with "no-match in SKILL.md" (uncommitted `measures-ca.txt`). The SCORECARD prose (`:1535`) claims the repair "distinguishes" the digests, which is true in wording but not in the frozen pattern.

## 3. C and Ca counter failures (where each fails and why)

### C (final, uncommitted measure at 722e69f, 11/13)
- **ROWS — FAIL.** Honest as declared; see §1(1). The predicate forbids added lines outside `row_set`; the committed registry appends two such lines (`SOURCES.md:854`, `:902`). The diff has 8 insertions in all: 3 rows and 5 other lines, of which I identified only these 2 by content.
- **COLLCHECK — FAIL.** Validator gap against `C-P3`; see §1(2).
- **INDEX counted twice; SCRATCHMIRROR absent.** The frozen 13-leg table is `ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX` (`58e6c81:reports/round-76/telemetry/controls-c.txt:16`). `R76-M2` (`722e69f:corpus/lessons/round-76.md:84`) says the implementation was repaired to match "the already-frozen 13-leg list" and that "predicate/config bytes were not changed". So the duplicated INDEX and the absent scratch-mirror leg are frozen. The 11/13 is inflated by one double-counted pass.
- **Frozen constants** — PASS (`FROZENCFG`). `df0f030:reports/round-76/claims.json` `min_admitted=1`.

### Ca (final, uncommitted measure at a43ed80 with combined 722e69f, 5/12)
- **LEDGER — FAIL**: L76-13 path not in the append-only allowlist; L76-19 `stated_text` not found on the line (§2a, §2b).
- **REPAIR — FAIL**: L76-16 `statement_after` no-match (§2d).
- **ANNOTATE — FAIL**: L76-19/20/21 rederive not executable (§2c).
- **NOSTUB — FAIL**: stubs L76-19/20/21 `rederive-cmd` (same cause).
- **R1EXEMPT — FAIL**: `reports/round-76/telemetry/r1exempt-green.txt` and `r1exempt-red.txt` are not committed at Ca landing. They do not exist in the lane worktree either (`reports/round-76/telemetry/` has no such files). The receipts the claim requires were never produced in the lane.
- **SEPARABLE — FAIL**: L76-13 forbidden read of `corpus/knowledge/**`.
- **COMBINED — FAIL**: a C-owned README heading change at line 410 is outside Ca's frozen APPENDONLY exemption; the frozen `owned_inplace` line number is invalid.
- **PASS**: BASEMISMATCH (20 red pairs), APPENDONLY, RECEIPTS, FROZENCFG, STAMP.

## 4. Cross-axis and source-governance pattern

1. **Attribution recurs in the calibration ledger itself.** R76-M1 was mined in round 76 and fixed for sizes (QUALITY 29). The same class reappears in L76-13 (wrong stated artifact, three values for one page) and the routed text's "value not found" (§2b). The criterion's wording is "name the artifact the sentence names"; it does not require the named artifact to be the statement under test. That is a gap in the criterion, not only in the ledger.
2. **Re-typed derivation strings.** The SCORECARD claims a verbatim projection; three rows differ from the frozen ledger in quoting, and the frozen ledger's own strings cannot be parsed. Correction rows are being hand-edited, not copied, and the claim calls them verbatim.
3. **Authority receipts are not committed.** The lesson calls "the final C counter receipt and Ca counter receipt" the authority (`722e69f:corpus/lessons/round-76.md:89`). The only final receipts are `measures-c.txt` and `measures-ca.txt`, both untracked in the lane (`git status`: `??`). The committed telemetry at 722e69f and a43ed80 holds only do-nothing controls at freeze (`controls-c.txt`, `controls-ca.txt`). The R1EXEMPT receipts are absent everywhere.
4. **The routed text under-reports Ca.** `722e69f:corpus/lessons/round-76.md:89` names two failing legs (L76-13, L76-19); the measure shows seven. The instruction in the same paragraph to report "their exact failing legs" is not met for Ca.
5. **Coverage landed with governance harm.** The C move raises coverage (new ground, +1 file, +3 rows, census 0 E-codes) and adds non-row lines to the registry and an alias the counter cannot resolve. These are reported as a contradiction: coverage up, two governance legs red. Neither is smoothed away.
6. **Draft and frozen config both sit in the committed tree.** `df0f030:.ufo/waves/round-76/CLAIMS-DRAFT.md:35` says `n>=2` and `:44` says "fewer than two candidate files landing". The frozen `claims.json` says `min_admitted=1` and the kill rule "the single selected candidate a does not land". The draft header says "The freeze commit supersedes this file", and `C-P2` documents the change. This is low severity: the frozen config governs, but two contradictory thresholds are committed side by side.

## 5. Evidence index

| claim | path (committed unless marked) | line |
|---|---|---|
| R76-M1 mined mistake | `722e69f:corpus/lessons/round-76.md` | 83 |
| R76-M2 frozen leg table | `722e69f:corpus/lessons/round-76.md` | 84 |
| R76-M3 non-row appends | `722e69f:corpus/lessons/round-76.md` | 85 |
| Routed to round 77 (under-reports Ca) | `722e69f:corpus/lessons/round-76.md` | 89 |
| Census section | `722e69f:corpus/lessons/round-76.md` | 75–77 |
| Criterion 29 (attribution) | `722e69f:corpus/QUALITY.md` | 199, 201, 203 |
| Registry rows 817→820 | `722e69f:corpus/SOURCES.md` | 849–851 |
| Non-row registry lines | `722e69f:corpus/SOURCES.md` | 854, 902 |
| Frozen C config (min_admitted, kill rule, C-P3) | `df0f030:reports/round-76/claims.json` | `claims[0]`, `pre_data_corrections` |
| Frozen C leg table (INDEX×2) | `58e6c81:reports/round-76/telemetry/controls-c.txt` | 16 |
| Final C measure (uncommitted) | `reports/round-76/telemetry/measures-c.txt` (untracked) | ROWS, COLLCHECK lines |
| Final Ca measure (uncommitted) | `reports/round-76/telemetry/measures-ca.txt` (untracked) | LEDGER…COMBINED lines |
| Frozen Ca ledger, L76-13 | `df0f030:reports/round-76/ledger.json` | pair `L76-13` |
| Frozen Ca ledger, L76-19 | `df0f030:reports/round-76/ledger.json` | pair `L76-19` |
| S885 receipt bytes 109588 | `98c486b:reports/round-75/evidence/S885.txt` | 5 |
| S892 receipt before=2020 | `98c486b:reports/round-75/evidence/S892.txt` | 13 |
| Lesson 111486 / before=284 | `98c486b:corpus/lessons/round-75.md` | 28; 47–48 |
| Knowledge-file 111487 | `98c486b:corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` | 8 |
| SCORECARD correction table | `a43ed80:SCORECARD.md` | 1509–1535 (rows 1526, 1531–1533) |
| REPAIR target | `a43ed80:SKILL.md` | 707 |
| Showgb alias evidence (stage) | `df0f030:.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S896-openstd.showGb-followed-2026-10-27.html` | body |
| Ground sweep at base | `722e69f:reports/round-76/telemetry/gap-sweep.txt` | 7, 13, 19 |
| Census end, no E-codes | `722e69f:reports/round-76/telemetry/census-end.txt` | — |

Worktree note: the lane worktree is dirty (`M SCORECARD.md`, `M .ufo/waves/round-76/w1/stage/ExecAdaptC/claim-C.json`, untracked `reports/round-76/telemetry/measures-*.txt`, `reports/round-76/counters/`). Nothing above reads the worktree SCORECARD or any modified file; the two `measures-*.txt` receipts are cited only as uncommitted disclosure.

## 6. Checks the main agent should run (not run by this seat)

- Re-derive L76-13 and L76-19 from committed bytes at base (the two `git show` commands in §2a and §2b), and confirm whether `narrative-structure-frameworks.md:8` or the round-75 lesson is the statement the ledger is meant to test.
- Confirm that R1EXEMPT receipts are absent at `a43ed80` (`git ls-tree -r --name-only a43ed80 -- reports/round-76/telemetry | grep r1exempt` should be empty).
- Confirm the SCORECARD rows at `a43ed80:SCORECARD.md:1531–1533` differ from `df0f030:reports/round-76/ledger.json` `rederive` for L76-19/20/21.
