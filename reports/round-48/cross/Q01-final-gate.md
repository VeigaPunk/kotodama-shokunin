# Q01 — final quality gate (round 48, loop 2, position 2)

- Seat: `Q01` | role verifier | claim **cross** | out path `reports/round-48/cross/Q01-final-gate.md` (this file).
- Baseline: `git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af` (`a01405d`), equal to `reports/round-48/claims.json:7` and `telemetry/dispatch-declared.json:11`. No drift.
- Gate cut: `2026-10-19T19:43:54Z` (UTC), then a final write-surface scan at `19:44Z`. The wave was live; fragments filed while I read, and every judgement below is bound to the artifact name and measurement stated with it.
- Non-author statement: I drafted no C or Ca fragment and edited no fragment, corpus byte, tool, README, queue or filed round. I wrote only this file. All commands ran from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Gate verdict.** The round is **honest and harm-free on disk** — corpus holds at 223/25, `corpus/README.md` is byte-unchanged (`7c788a1d…`), no tracked or staged modification exists, no seat wrote outside its declared out path, and every arithmetic expression I recomputed in both C bodies is correct. But **neither claim is delivered and neither `after_required` is met**:

- **C — coverage: NOT CERTIFIED.** There is no single assembled C artifact. Two rival bodies exist (C01 227 lines, C13 181), three different `- topic:` texts exist, and most C verifiers audited r47's fragments or a sweep fixture rather than either body. The two seats chartered to certify the assembled contract and the non-author content — **C05 and R03 — never filed**. `audits PASS` is therefore false as a description of the filed chain, exactly the condition `claims.json:31` requires.
- **Ca — calibration: README half PASS-staged; disposition half unmerged.** The duplicate-H1 fix is surgical, byte-identical across six independent stagings (`d407260d…`, 573 lines, H1 2→1, sweep green). But three different queue-successor drafts target one file with two competing ids for one class (N02 measured this as a merge-level FAIL), the second duplicate-line defect (`revision: 2.0` at `:42`/`:44`) is undispositioned, and five different heading-control drafts exist in five paths. Nothing is applied.

**Axes: no move recordable. No axis harmed.** Coverage stands at 223; calibration stands at the unfixed README; adjacency/operability/usability are untouched. The r47 over-build class is **not** repeated by either body on line count (227 and 181 vs 790), but it is repeated in *process*: audits were again run on non-final bytes while the round says "audits PASS".

---

## 1. What I measured at the gate (independent, not carried)

```console
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 -B reports/round-28/readme/sweep.py | tail -4
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -o '^revision: [0-9.]*' corpus/README.md | sort | uniq -c | head -2
      2 revision: 2.0
      1 revision: 2.4
$ git status --porcelain -- corpus tools reports/round-1..47 corpus/lessons tools/gates/frozen LOG.md PROVINCE.md
(empty)
$ git diff --name-only; git diff --cached --name-only
(empty)
```

Vectors recomputed: `25+23+26+25+24+94 = 217` (rev-2.4's written destination), `25+26+25+29+24+94 = 223` (correct rev-2.4), `25+26+26+29+24+94 = 224` (rev-2.5). The rev-2.4 defect is real and the repair value is 223, not 224. The second duplicate (`revision: 2.0` at `:42` and `:44`, the first a truncated orphan) is real and is in **no** claim.

**Write-surface census.** `targets.json` declares 64 unique out paths; 64 files exist under `reports/round-48/`, of which 61 are declared seat outs, `claims.json`, `targets.json` and `telemetry/dispatch-declared.json` are the three allowlisted contract files. Zero undeclared files, zero zero-byte files, zero non-telemetry strays. This matches A03's gate at its cut and A04's pre-apply census.

**Completeness: 61 / 64 seat outs filed.** Missing at my cut:

| Seat | Declared out | What it uniquely owns | Consequence |
|---|---|---|---|
| **C05** | `cov/C05-length-contract.md` | line count + full entry-contract checklist on the assembled body | the one seat chartered to catch a missing header field or a >250 assembly never ran |
| **R03** | `review/R03-c-content.md` | non-author content judgement on the r48 landing bytes | `after_required`'s "audits PASS" has no content leg; r47's block on exactly this seat's verdict is not answered |
| Q01 | `cross/Q01-final-gate.md` | this gate | filed by this write |

Two absences are not bookkeeping: C05 and R03 are the seats whose r47 analogues found the blocking defects (`R03-c-content.md:188-196`; C05-equivalent length check). A round cannot claim "audits PASS" while both are missing.

---

## 2. Claim C — evidence chain, seat by seat

| Link | Filed artifact | Object actually audited | Verdict at that object | Usable for the r48 landing? |
|---|---|---|---|---|
| Gap/collision | `C06-collision.md` | pre-draft tree | PASS — 0 filename, 0 topic owners, slug free, lands A | **pre-draft only**; no body seen |
| Freshness | `C06`, `X04`, `F01` | 223 tree | PASS — independently reproduced | yes for ownership; landing HEAD must re-run |
| Body A | `C01-entry.md` | its own 227-line fence | self-report | **candidate**, not certified |
| Body B | `C13-scribe.md` | its own 181-line fence | self-report ("assembly candidate") | **rival candidate** |
| Header | `C02-header.md` | 23-line head block | 19/19 couples, 23 anchor assertions, 0 failures | **only conforming head** (8 fields) |
| Arithmetic | `C03-arithmetic.md` | **r47's 790-line assembly** | r47 defects reproduced; "no r48 draft" at its cut | **no** — r48 body never audited |
| Citations | `C04-citations.md` | anchor baseline | 56 anchors exact; draft `could-not-evaluate` | **no** — body never audited |
| Length/contract | **absent (`C05`)** | — | — | **blocking absence** |
| Boundary | `C07-boundary.md` | **r47 draft** | O1/O2/U1/R1; agrarian under-claim blocking | **no** — body never audited |
| Boundary draft | `E01-boundary.md` | a 13-row draft | all anchors quoted live | integration-ready input, not applied |
| Neighbours | `C15-neighbors.md` | **r47 table** | 7/7 dispositioned; F1 `:27` blocking | **no** — body never audited |
| Capless check | `C09-couples.md` | C02's field | 19/19 direct; P2 two mandated tokens absent (corrected field 21) | applies to C02's head only |
| Shelf | `C08-shelf.md` | **r47 shelf** | two blocking shelf defects; no r48 body | **no** |
| Provenance | `C18-provenance.md` | C02 head + M02 | PASS with P1/P2 carry-forwards; body absent | partial |
| Content | `C12-content.md` | C02/M01/M02/E01 fragments | "real content, not budget-ready"; 27-line example > C14's 25 ceiling | **no** — C01 body absent at its cut |
| Example | `C14-example.md` | **r47 example** | gate built; r47 fails W3/W4/W5/W9; r48 `could-not-evaluate` | **no** |
| Method | `M03-method.md` | **r47 body** | PASS on substance; r47 `could-not-evaluate` for r48 | **no** |
| Structure | `C17-structure.md` | **both bodies** | PASS structure; C01 head non-conforming; choose one body, do not concatenate | **yes, structural only** |
| Admission clauses | `E02-register.md` | **C01 body (second pass)** | PASS on five QUALITY clauses; notes two different head blocks | **yes for clause fit, not for truth of citations/arithmetic** |
| Topic | `C16-topic.md` | C02's topic | PASS byte-equal to seed; body promise ledger `could-not-evaluate` | applies to C02's topic only |
| README | `C10-readme.md` | staged 224 README | green in stage; two order variants | **prediction** |
| Sweep | `C11-sweep.md` | staged 224 tree with a **136-line fixture** | 224==224 green; fixture explicitly not C01 | **mechanism only** |
| Post-landing | `V01-post-landing.md` | instrument rehearsal | `could-not-evaluate`; nine-leg receipt demonstrated | **owed** |
| Census | `F01-final-census.md` | 223 tree + staged fixture | 4/17 in-tree; reopen protocol tested | **owed** |
| Landing wire | `W01-landing-spec.md` | apply sheet | gates defined against a manifest digest | **owed** |
| Delta receipt | `D01-delta-receipt.md` | staged 224, C02 topic | predicts README `4db8ecaf…` (582 lines) | **prediction** |
| Over-build critic | `X03-overbuild.md` | fragments, no body | 114 lines for 4 sections projects 7.9k–10.4k words | **warning**, not a verdict |

**Reading of the chain.** Only `E02` (admission clauses) and `C17` (structure) measured a candidate body. The four legs that failed r47 — arithmetic on assembled bytes (C03), citation anchors on assembled bytes (C04), contract/length on the assembly (C05), and a non-author content verdict (R03) — have no r48 result. `C14` and `C12` explicitly recorded `could-not-evaluate` for the body. This is the same defect shape r47 filed (`R03-c-content.md:248`: "Re-run the audits on the corrected bytes and file the results, not the pre-fix verdicts"), one round later.

### 2.1 The assembly is undetermined — a blocking finding

- **Two bodies.** `C01-entry.md` fenced body: **227 lines, 14 H2, 81 table lines** (my extraction; C01 reports 227 and sha `2a66774974b80d9b…`). `C13-scribe.md` §5: **181 lines, 14 H2, 52 table lines** (C13 reports `c93a54fc…`). They are not revisions of one draft: C01's section map is §1 register / §2 boundary / §3 chain / §4 forms / §5 projection / §6 trade / §7 provenance / §8 silences / §9 build / §10 decisions / §11 example / §12 bank / §13 recheck / §14 scope; C13's is §1 ownership / §2 object test / §3 typology / §4 chain / §5 projection / §6 symbols / §7 reproduction / §8 silences / §9 warrant / §10 build / §11 example / §12 bank / §13 decisions / §14 recheck+scope. Same topic, different architecture, different head.
- **Three topics.** Seed and C02: **766 chars**, sha `a42926b1d0fe5ac5…` (prefix-inclusive; C16 reports `bc7274f4…` on its own base). C01: **1,045 chars**, sha `aed27f526727bef2…`. C13: a third text of its own. The sweep compares the README row to the landed entry's `- topic:` byte-for-byte (`reports/round-28/readme/sweep.py`, `TOPIC_RE`/`ROW_RE`). A README staged from C02's topic and a body landed from C01's head is a guaranteed `topic_mismatch`.
- **Two head fields.** C02's head has all eight fields (23 lines, `- topic:` first). C01's internal head has **seven** — it has `- gap filled:` before `- topic:` and **no `- source:`**. C17's finding is correct and load-bearing: the assembler must strip C01's internal head and prepend C02's, producing **239 lines** (23 + 216), one H1, all fields.
- **Two hashes for one file.** C01 and this seat measure the fenced body at 227 lines / `2a667749…`; C17 and E02 report **228 lines / `e5255657…`**. The difference is a fence-inclusion frame, not two byte sets, but the integrator must pin one extraction convention before any verifier can cite a digest. `reports/round-48/cov/W01-landing-spec.md` already requires verdicts against a manifest digest (`W01:474`); that digest does not exist yet.
- **No assembled digest.** `claims.json:31` requires "audits PASS" on the landing. No seat filed the assembled artifact (C02 head + chosen body) with a sha and line count, and no verifier ran on it. C13 explicitly labels its block a candidate (§10.1); C17 says "the integrator must choose one and pin its sha256; do not concatenate the two."

### 2.2 Contract and content defects in the candidates (new, not B1–B9)

| ID | Defect | Evidence | Required fix |
|---|---|---|---|
| **Q-C1** | No assembled artifact or digest; C's audit chain is fragment-scoped | §2 above; `C17:218`; C13 §10.1 | assemble, sha, re-run C03/C04/C05/C14 + R03 on it |
| **Q-C2** | C01's head omits `- source:` and orders `gap filled` before `topic` | my parse: 7 fields, 0 `- source:`; C17:217 | use C02's 23-line head; strip C01's |
| **Q-C3** | Topic conflict: 766 / 1,045 / third text | my hashes; C16:132 (only C02 verified) | pick one topic, stage the README row from the chosen head, re-run sweep |
| **Q-C4** | C01's `- sources:` contains an internal pointer to "`## Self-audit` below the fence" that will not exist in a landed file | `C01-entry.md:75` inside the fence | delete the parenthetical before apply, or replace with "re-read at a01405d" |
| **Q-C5** | Both bodies omit `agrarian-field-system-lexicon.md` from boundary and couples, although C07 files it as a **blocking under-claim** (parcel/claim institution) and A01 independently names the same gap | my grep: C01 contains `agrarian` 0 times; C07:186-192; A01:8 | add the agrarian row and couples token, or record a named exception from C07/A01 |
| **Q-C6** | Boundary/couples target counts disagree across the chain (C02 19, C09 corrected 21, E01 13 rows, C07 12 + agrarian, A02 r47 23) | `C02:130`; `C09:171-172`; `E01:30-44`; `C07:231`; `A02:154` | one canonical boundary surface, then recompute the couples delta |
| **Q-C7** | C01 at 227 lines is 6 over the live partition max (221); inside the round's `<=~250` but a new partition maximum | my `wc -l`; `C01:313` admits it; `V01:40` flags 222–250 as a note | integrator decision: accept as a recorded note, or take C01's own three cuts + merge to 221 |
| **Q-C8** | C05 and R03 absent; no length/contract or content verdict exists on either body | §1 census | both must file (or the claim must record `could-not-evaluate` and not land) |

**What is genuinely clean in the bodies.** I recomputed every arithmetic expression in both drafts (19 distinct checks: `0.2 mm × N/1000`, `1 cm × N`, `200/10`, arcmin at 10 km, `sec 60°`, `1° longitude at 60°`, centuria side/area, 32-point rose, `12 m / 12 km`, `12/2`, `0.3 mm` at both scales, `sec² = 4`): **all 19 pass**. `naming-systems.md:70` is quoted verbatim, never "corrected". The craft ladder is cited `:54-65`, never `:44`. Every body cites `cosmology-cosmography.md:27` (C01 4 times, C13 twice, C02 twice), so r47's B8 is answered — X02's "B8 partial" finding is against C11's 136-line fixture (`entry:30`, `entry:126`), not a landing candidate. All eight forms are covered with a "cannot show" column; the worked example states one update rule once. Couples resolve: C01 14/14, C02 19/19, C13 17/17, all repo-relative. The r47 B1–B9 content defects are absent from both bodies.

---

## 3. Claim Ca — evidence chain

| Leg | Filed artifact | Result | Status |
|---|---|---|---|
| Defect scout | `K02-readme-defect.md` | duplicate H1 at `:1`/`:3`, count 2; rev-2.4 vector 217; sweep has no heading leg; second duplicate `revision: 2.0` at `:42`/`:44` | measured |
| Fix draft | `Ca01-readme-fix.md` | variant B deletes `:3-4`; 575→573; sha `d407260d…`; sweep green | tested |
| Independent verify | `Ca03-readme-verify.md` | variants A and B; `d407260d…` / `84e16f56…`; no other heading moved; −2 shift mapped | PASS |
| Review | `R04-readme.md`, `X05-readme.md` | surgical; sweep-neutral; second duplicate and open queue row flagged | PASS with conditions |
| Integrity | `Ca07-integrity.md` | 223 rows, 6 section headers, 12 revision blocks, footer byte-identical; one H1 removed | PASS |
| Wire | `W02-landing-spec.md` | `sed -i '2,3d'`; post-conditions; content-anchor order | ready |
| Heading control | `Ca05-heading-control.md` | `tools/check-readme-heading.py`, 244 lines, 8/8 selftest, red live / green staged | draft, not applied |
| Rival controls | `K02` (`tools/check-readme-headings.py`, 6/6), `P01` (`tools/harness/readme-heading-control.py`), `R04` (`tools/gates/readme-heading-control.py`), `Ca01` (`tools/check-readme-structure.py`) | five paths for one control | **conflict** |
| Over-build disposition | `Ca02-overbuild.md` (row `r47-entry-overbuild-defect-class`), `W02` (rows `R36-README-DUPLICATE-HEADING` + `r47-overbuilt-entry-draft`), `Ca06-process-row.md` (row `r48-entry-quality-not-gated`) | three drafts, one target file `calib/queue-successor-r48.json` | **merge conflict** |
| Integrity verify | `N02-integrity.md` | legs 1–3 PASS; leg 4 **FAIL as proposed**: two rows own one class and each names the other as an alias | blocking |

**Ca README verdict: PASS on staged bytes, `could-not-evaluate` on delivery.** The fix is byte-unambiguous: `d407260d…`, 573 lines, H1 1, `## ` 7, `revision:` 6, sweep `223==223` exit 0, no content line changed except the duplicate H1 and one blank. The only delivery certificate is the post-apply sweep (Ca-first, or one atomic README write with C's rev-2.5). It has not been run because nothing was applied.

**Ca disposition verdict: not fileable as drafted.** Blocking findings:

| ID | Defect | Evidence |
|---|---|---|
| **Q-Ca1** | Two rows for one class (`r47-entry-overbuild-defect-class` and `r48-entry-quality-not-gated`), each incidence 1, each aliasing the other → double count | `Ca02:107`; `Ca06:86,89`; `N02:26` |
| **Q-Ca2** | Three drafts target one path with different row sets; a fourth variant (`W02`) closes `R36` as `fixed-with-evidence` while the fix is not yet applied | `Ca02:79`; `W02:147,215`; `Ca06:21` |
| **Q-Ca3** | The second duplicate-line defect (`revision: 2.0`, `:42`/`:44`) is in no successor draft, although K02/F01/X01/X05 all flag it | my `grep -o '^revision: [0-9.]*'` → `2 revision: 2.0`; `K02:400`; `F01:152-160`; `X05:125-127` |
| **Q-Ca4** | Five different heading-control paths/drafts; none applied or invoked; the claim's other branch ("durable note filed") is also not filed | my path census (32 mentions of `tools/check-readme-heading.py`, 3 each of two others, 1 each of two more); `R04:99` |
| **Q-Ca5** | The claim's counting command `python3 reports/round-48/run-validation.py` is forbidden in-tree and the file does not exist | `claims.json:49`; `R04:146`; `A01:8`; `P01:172` |

**One arithmetic correction that must reach the README edit.** `claims.json`/`targets.json` C10's shorthand ("synthesis 25→29, myth-symbol 23→26, culture-material 26→25 = 224") produces **223**, not 224 (`P01:102`; `R02:207`; `Ca05:509`). C10's own filed draft gets it right: repair rev-2.4 to `25/26/25/29/24/94` (223) and state rev-2.5 as `25/26/26/29/24/94` (224). The contract text, not the draft, is the misleading artifact.

---

## 4. Round-record integrity findings

These do not block a landing by themselves, but the round must not file them as green:

| ID | Finding | Evidence |
|---|---|---|
| **Q-R1** | The freshness gate's first live use is **not durably reproducible**. The candidates and overlay exist only in gitignored `.scratch`; the filed `claims.json` alone returns exit 3 (`could-not-evaluate`), the filed claims plus the used overlay returns exit 2 (malformed, because O was dropped after the run). | `O01:9,59`; `O04:9,31,40`; `R01:192-205`; `X04:106-114` |
| **Q-R2** | Two of the three gate checks do not measure their clauses. **Ca is vacuous** (`count_eq` counts files matching the glob, not headings; it would pass after the fix and before it). **O's STALE is a probe artefact** (`capability_present` runs the resolver's `--selftest` in a one-file corpus and reads the exit code); direct measurement reproduces the declared soft-wrap drop, so O's drop was correct as a dispatch decision but the record's ground ("premise false") is wrong. Only **C FRESH** is gate-sound. | `O01:9`; `O02:8`; `R05:8,192`; `X04:116-132` |
| **Q-R3** | Declared instants post-date their own files by 7–9 minutes (`19:45:00Z` vs mtimes `19:36:19Z`–`19:37:31Z`), and seats had filed before the declared time. Info only: digests bind, timestamps do not. Do not cite `19:45:00Z` as a measurement time. | `A03:202-209`; `S02:45-57`; `X04:195-198` |
| **Q-R4** | `S03-shonen.md` carries all four boxes `[~]` and no `[x]`; that is correct at its cut, but C05 and R03 are now known absent, so box 4's "no cross-domain bleed" and box 2's chain leg remain `could-not-evaluate`, not carried-green. | `S03:29-52`; §1 census |
| **Q-R5** | The round's own "the gate caught a stale premise" headline is contradicted by O01/O02/R05. The closing snapshot must record the correction in a **new** append-only telemetry file; `claims.json` and `dispatch-declared.json` are digested contract artifacts and must not be edited. | `claims.json:23`; `dispatch-declared.json:20`; Q-R2 |

---

## 5. What is actually green (and what it is green for)

1. **Corpus hold and write surface.** 223 / 25 / README sha unchanged; no tracked or staged modification; 64 files, all classified; zero undeclared or zero-byte files. A03/A04/N03/A01/X02 agree with my scan.
2. **Gap freshness and one-owner safety at the file level.** 0 filename owners, 0 topic owners, slug free, lands `A`; no existing entry's `- couples:` claims the register. Reproduced by C02/C06/C09/A02/F01 and by me.
3. **Arithmetic.** All 19 recomputations in both bodies pass; B1's `200 m ÷ 10 m = 20` is stated correctly; no draft repeats "ten times".
4. **r47 content defects.** B2 (2 files / 2 lines), B3 (`archive of coups` verbatim), B4 (`:54-65`), B8 (`:27` cited), B9 (8 of 8 forms) are all absent from both bodies.
5. **Staged 224 mechanics.** Three independent stagings (`C11` 8b0252…, `C13` 7ee7abb…, `D01` 4db8ecaf…) reach `rows 224 files 224`, footer `25/26/26/29/24/94`, exit 0. These are **predictions**, not delivery certificates; each is keyed to a different topic text and entry fixture.
6. **Ca README edit.** Six independent stagings agree on `d407260d…` / 573 lines / H1 1 / sweep green. This is the strongest delivered-vs-staged leg in the round; the delivery run is still owed.
7. **Sweep blind spots are now measured, not suspected.** No length, no H1, no row-order, no duplicate-topic, and duplicate rows are reported but non-gating (`sweep.py:191-194`). This is the substantive calibration gain of the round even before Ca applies.

---

## 6. Required integrator decisions (ordered; nothing below was done by a seat)

1. **Choose the C assembly.** Pick C01's body or C13's (not both, not concatenated: `C17:218`). Prepend **C02's 23-line head**, strip the body's internal head. Pin the assembled sha and line count in a filed artifact and state the extraction convention (fence-exclusive vs fence-inclusive — the 227/228 and `2a667749`/`e5255657` split).
2. **Resolve the topic.** If C02's head is used, C02's 766-char topic is the README row text. If C01's head text is preferred, the README row must be regenerated and the sweep re-run; the seed's "byte-equal" claim then needs an explicit amendment.
3. **Fix the two body defects** before the audits: remove C01's `## Self-audit below the fence` self-reference (`C01:75`); add the agrarian boundary row and couples token or record a named C07/A01 exception (`C07:186-192`).
4. **Run the missing audits on the assembled bytes:** C03 (arithmetic), C04 (anchors), C05 (length/contract), C14 (example), and R03 (non-author content). Until C05 and R03 file, "audits PASS" is not available and C must be recorded `could-not-evaluate`/not landed.
5. **Apply Ca first (or as one atomic README write), then C's README hunks by content anchor.** Ca: delete `:3-4`; expect 573 / `d407260d…` / H1 1 / sweep 223==223. Then C: rev-2.5 block, rev-2.4 repair to **223** (`25/26/25/29/24/94`), header 25→26, row in filename order, totals 224, footer `25/26/26/29/24/94`. Re-derive anchors after the −2 shift (`K02:140-158`; `R04:84-95`).
6. **File one canonical heading control** (recommend `tools/check-readme-heading.py`, Ca05's 244-line 8/8 version) and invoke it in the apply wire; run it red before the fix and green after, on the same path. Do not leave five drafts.
7. **File one canonical queue successor** with one over-build row (resolve Ca02/Ca06's double count per `N02:26`), the `R36-README-DUPLICATE-HEADING` close, and a new row for the `revision: 2.0` duplicate at `:42`/`:44`. Pin parent `dfc9265d…` and predecessor `9508b6aa…`; never edit either.
8. **File the freshness-gate inputs and a correction note** under `reports/round-48/telemetry/` (new append-only file): candidates, overlay, command, exit code, decision digest; state that the Ca probe was vacuous and the O red was a probe artefact; do not edit `claims.json`.
9. **Do not run `reports/round-48/run-validation.py` in-tree.** Its appearance in `claims.json:49` is a contract defect; record the substitution (sweep + heading control on landed bytes) in the round record.
10. **Deliver the certificate after apply:** live sweep `224==224`, footer 224, H1 count 1, entry `<=250` measured on the landed file, `git status` = `M corpus/README.md` + one `??` entry, and `corpus/knowledge` 224 / culture-material 26. Until that run, every 224 number in this round is a prediction.

---

## 7. Axis verdicts at this gate

| Axis | Verdict | Basis |
|---|---|---|
| **coverage** | **unchanged (223), no harm; +1 NOT recordable** | real gap, real method, two right-sized bodies, but no assembled+audited landing; C05/R03 absent |
| **calibration** | **unchanged, no harm; +1 NOT recordable yet** | Ca README fix safe and staged; disposition unmerged; gate's first use mis-recorded |
| **adjacency / one-owner** | **no harm; one open under-claim** | 0 owners at file/topic level; agrarian under-claim open (C07/A01); boundary counts conflict |
| **usability** | **improved in draft, not delivered** | 227 or 181 lines vs 790; 0 H3; 52–81 decision rows; C01 six lines over the live partition max |
| **operability** | **untouched** | O rests by declaration; gate evidence is incomplete but the gate itself is selftest-green (62/62) |

No axis is harmed by anything on disk. No claim may be recorded improved at this gate.

---

## 8. Could-not-evaluate / to-verify (owner + reason)

| Item | Status | Owner | Reason |
|---|---|---|---|
| C landing bytes and line count | `could-not-evaluate` | integrator | no assembled artifact; two bodies |
| C arithmetic/citation/contract/content on the assembly | `could-not-evaluate` | C03/C04/C05/R03 | audits ran on r47 or fragments; C05/R03 absent |
| C topic byte-equality after assembly | `could-not-evaluate` | integrator/C10 | three topic texts; only C02's matches the seed |
| README post-apply sha | `to-verify` | D01/C11 | three staged predictions keyed to different topics; only the live sweep certifies |
| Ca queue row as filed | `could-not-evaluate` | integrator | three drafts, one target, N02 merge FAIL |
| Heading control as landed/invoked | `could-not-evaluate` | integrator | five drafts, none applied |
| Freshness gate replay from filed bytes | `could-not-evaluate` | integrator/O01/O04 | inputs only in `.scratch`; filed claims exit 3, filed+overlay exit 2 |
| `revision: 2.0` duplicate disposition | open | integrator/Ca | in no claim, no successor draft |
| Dispatch launch/completion/failure counts | `could-not-evaluate` | integrator | no observed-dispatch sample filed; requested 64 is not observed |
| External bibliographic accuracy | `to-verify` | any author | no network; every edition/page marked `(to-verify)` |

---

## 9. Commands and write surface

```console
$ git rev-parse HEAD                              -> a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l      -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l -> 25
$ python3 -B reports/round-28/readme/sweep.py     -> rows 223 files 223, exit 0
$ sha256sum corpus/README.md                      -> 7c788a1d…cdcd
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2
$ grep -o '^revision: [0-9.]*' corpus/README.md | sort | uniq -c -> 2 revision: 2.0
$ python3 (fence extraction + field/row/couples/topic audit over C01, C02, C13)
  C01: 227 lines, 14 H2, 81 table lines, 7 fields (no - source:), 14/14 couples, topic 1045 chars
  C02:  23 lines, 8 fields, 19/19 couples, topic 766 chars (== seed)
  C13: 181 lines, 14 H2, 52 table lines, 8 fields, 17/17 couples, third topic text
$ python3 (19 arithmetic recomputations over both bodies) -> 19/19 pass
$ python3 (census of targets.json vs files) -> 64 declared, 61 present, 0 undeclared, 0 zero-byte
$ python3 -B tools/harness/claims-freshness.py --selftest -> SELFTEST OK: registry 43/43 + seam 19/19
$ git status --porcelain -- corpus tools reports/round-1..47 corpus/lessons tools/gates/frozen LOG.md PROVINCE.md -> empty
$ git diff --name-only; git diff --cached --name-only -> empty
```

**Write surface:** this file only — `reports/round-48/cross/Q01-final-gate.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed in-tree. `git status --porcelain` at my write cut showed only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.

**Bottom line for the integrator.** Do not record either claim as improved and do not apply a C body until one assembly is chosen, pinned, and audited by C03/C04/C05/R03 on those bytes. The Ca README fix is safe to apply as a separate recorded act now, provided the successor is merged into one canonical row set and the `revision: 2.0` duplicate is dispositioned. Everything else in this round is honest preparation, not delivery.
