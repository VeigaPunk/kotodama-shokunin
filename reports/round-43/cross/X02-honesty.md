# X02 — honesty critic: are the claimed numbers measured, or only asserted?

- Seat: **X02** | role critic | claim cross | round 43 | baseline `7ceff59`
- Out path: `reports/round-43/cross/X02-honesty.md` (this file is this seat's only write)
- Snapshot of the tree audited: **2026-10-19T17:07:22Z**, HEAD `7ceff59a0216a8ea21ee43262d9fc72abf770cee`
- Method: every number below is either (a) re-measured by this seat with the command shown,
  (b) quoted from a named artifact with its digest/path, or (c) explicitly marked
  `to-verify` / `could-not-evaluate`. No filed byte was edited; nothing was staged under
  `corpus/`; no `reports/round-*/run-validation.py` was executed in-tree.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  lane root. Scratch probes: `.scratch/x02/` and `.scratch/x02run/`.

The mission is narrow: the **4/4 wrapped-field read**, the **223 → 224 count**, **each
disposition class**, any **"should work" wording**, and the **write surface** (no seat outside
its out path; nothing staged under `corpus/`). The report therefore spends its space on those
four things and files the other numeric defects it found as a secondary ledger.

---

## 0. Verdict at a glance

| focal object | status at the 17:07Z cut | basis |
|---|---|---|
| **4/4 wrapped-field read** | **MEASURED, but "4/4" as an arity is not sufficient** — three different join rules all yield 4 tokens; only the hyphen-healing rule yields the intended *identity set* | §1.1; my extraction vs O12-F1/O02 S1b/O09 S1b |
| **223 → 224** | **223 is measured; 224 does not exist.** No corpus landing occurred; the only 224s are explicitly labeled staged predictions. Claim C is blocked by an owned-topic collision. | §1.2; 26/223 live, README rev 2.4, sweep green |
| **each disposition class** | **All four rows reach a class, but Ca01's draft artifact is not integration-ready** — three class/count defects are corrected by Ca02; the JSON is fenced, not filed | §1.3, §4 |
| **"should work" wording** | **No substantive hedge found.** All regex hits are requirements, corrections, quotations, or a labeled hypothesis | §6 |
| **no seat outside its out path; nothing staged under `corpus/`** | **PASS at my cut** — 31 files, every non-contract file matches a declared out path; `git status` is only `?? reports/round-43/`; `git diff HEAD` over `corpus/`, `tools/`, r19/r27/r28 is empty | §5 |

Two round-level premises are **false at HEAD**, and the round's own seats caught both:

- **O's `before`**: "no durable instrument implements the r39 basename-couples policy"
  (`reports/round-43/claims.json:27`) — false. `tools/harness/couples-reference-extractor.py`
  is tracked at `7ceff59`, selftest 8/8 green; r42's validation records claim O `"passed":
  true`. Independently flagged by O12-F2 (`op/O12-negative-proof.md:244`), K01, O02, O07,
  O09, O10, A01, R01.
- **C's `before`**: "lithic slot named but unbuilt" (`claims.json:40`) — false. The slot is
  built by `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (192 lines, 61,884 B,
  sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`, added in
  `7ceff59`), and `corpus/README.md:5-12` rev 2.4 already records that C01's draft
  "collided with C04's and is routed as a named spare."

The round is **not** harmed in bytes: no seat wrote a corpus or tool byte, and the live tree is
unchanged from baseline. The harm is in the **contract text** and in **what must not be filed
as a measurement**.

---

## 1. The three focal number audits

### 1.1 The wrapped field: 4/4 by identity, not by count

Field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (file sha256
`b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`, 325 lines, 20,405 B).
Six physical lines; five are two-space-indented continuations; line 76 ends in `tone-`.

My own extraction (not using any seat's tool):

```
block lines 72-77:
  '- couples: language (this file, core method); myth (divine/true names, taboo'
  '  naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,'
  '  bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of'
  '  strata); costume (masks/mouthgear vs articulation, whistle & drum channels);'
  '  environment/anatomy design; prospective sibling files: sound-change.md, tone-'
  '  prosody.md, sound-symbolism.md, writing-systems.md'

naive block regex `[A-Za-z0-9_./{},\-]+\.md` on the newline-joined block:
  4 tokens = {'prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md'}
hyphen-retained heal (`tone-` + `prosody.md` -> `tone-prosody.md`):
  4 tokens = {'sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md'}
```

**Finding:** a count-only "4/4" threshold is a false green. Space-join and newline-join both
return **4** tokens while naming the wrong filename (`prosody.md`); de-hyphenation returns
`toneprosody.md`. Only the identity set above is correct. This is independently measured by
O12-F1 (`op/O12-negative-proof.md:200-215`), O02 S1b/S1e, O04 §1, and O05 trap 5.

Executed confirmations:

```
$ python3 tools/harness/couples-reference-extractor.py --selftest
8 PASS, exit 0 — incl. "wrapped positive 4/4 tokens [sound-change.md, sound-symbolism.md,
tone-prosody.md, writing-systems.md]" and "block read yields 4 tokens"

$ python3 tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
```

The 4/4 claim is therefore **measured**, with the caveat that the acceptance assertion must be
on token identity, not arity. The 4/4 does **not** flip the r19 gate green: the r19 instrument
also requires `gap=False`, and still reports `couples=0` (S01 §2.1).

### 1.2 223 → 224: 223 is measured, 224 is only a prediction

Measured at HEAD:

```
$ ls corpus/knowledge/myth-symbol/*.md | wc -l        -> 26
$ find corpus/knowledge -name '*.md' | wc -l          -> 223
per-partition: linguistics 25 / myth-symbol 26 / culture-material 25 / synthesis 29 /
               verification 24 / civilizations 94   (sum 223)
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; missing_from_index 0; topic_mismatch 0; orphan_rows 0;
header_drift {}; totals_line 223 totals_ok True; footer_ok True; exit 0
```

`corpus/README.md` is **revision 2.4**, total line **223**, footer vector `25/26/25/29/24/94`.
The 224 figure appears only in staged predictions, each labeled as such:

- C02 `cov/C02-readme-draft.md:20` — "Variant A ... conditional"; staged tree built in
  `.scratch/c02-stage/`; live README unchanged.
- C05 `cov/C05-delta-receipt.md:24,45` — "the prediction, not the delivery"; "prediction only";
  the staged tree is a scratch copy, and the live tree is untouched.
- C07 `cov/C07-scribe.md` §3.5 — a simulated README with sha `1c165a99…`, explicitly "not a
  delivery prediction".

No artifact claims a delivered 224. The claim-C landing is **blocked by a live topic
collision**, independently reported by K02, C01, C02, C03, C04, C05, C06, C07, A01, X00, X01
and R01. See §3.

### 1.3 The disposition classes: four rows, measured — with three corrections

The claim (`claims.json:49-59`) names four rows. My re-measurement of each row's evidence:

| row | Ca01 class | my measurement | honest class |
|---|---|---|---|
| `r38-O07-empty-fragment` | `recorded`; prevention `routed-with-owner` | `wc -c reports/round-38/op/O07-scribe.md` -> **0**; sha256 is the empty-file digest `e3b0c442…`; `grep -rn 'min_bytes\|min-bytes\|MIN_BYTES' reports/round-4[0-2]/run-validation.py tools/harness/` -> exit 1 | **recorded** + prevention **routed** |
| `r38-O08-fragment-defect` | `recorded` | O08 `:83` says `ae22013b…` "is exactly the digest O01 §6 declares"; O01 `:144,:309` declare `e5812751…`; `grep -Fc ae22013b… O08` -> 2. The one-hunk `m15b` difference is real. | **recorded** |
| `r38-O02-fragment-defects` | `could-not-recover` (all three) | filed O02 says "plus 45 controls" at `:20,:62,:203` (not 44); the only "names nothing" is `:99`, about the rejected rendered-text guard (not m15b); **but** O02 `:164` says the tamper "surfaces through the assembled-vs-frozen packet compare", which O03 measured is not the first firing leg. | **D-1/D-2 could-not-recover; D-3 recorded** (Ca02 §2.3; Ca03) |
| `r39-review-findings-disposition` | `fixed-with-evidence` (conditional on filing) | R01-1..R01-14 + one minor are all dispositioned; R01-4 is evidenced by the **r39** C05 audit (28,221 B, `:46` 4/4 PASS); **R01-13 is fixed at r40** (G2-G4 landed, linguistics 21 -> 25), not merely recorded | **fixed-with-evidence conditional; R01-13 `fixed-with-evidence` at r40** |

The artifact's own JSON counts are internally consistent — I parsed the fenced block:

```
counts.sub_leg_classes = {fixed 1, recorded 10, routed 7, could-not-recover 4}, total 22
row_classes = {fixed 1, recorded 2, routed 0, could-not-recover 1}
findings_dispositioned = 19; findings_dropped = 0
programmatic leg recount = 1 / 10 / 7 / 4 = 22  (matches the JSON)
```

But the prose summary at `calib/Ca01-dispositions.md:86-87` says
`fixed 1, recorded 8, routed 6, could-not-recover 5` (sum 20), contradicting its own JSON.
Ca02 caught this independently (`calib/Ca02-verify.md:162-165`, M12), and so did I.

**Verdict on the four classes:** every named row reaches a class with a citation and nothing is
silently dropped. But **Ca01 as drafted is not the artifact to file**: D-3 is misclassified,
R01-13 is stale, the summary count is wrong, the four `parent_row` end-lines are one past the
queue rows (`:282-291` etc. vs `:282-290` etc.), and the sentence "the cited quotes cannot be
recovered in any durable artifact" is false — the quotes are durably in `O03-verify.md:259-291`.
Ca02's §6 five-amendment gate is the correct precondition. After those amendments, the classes
stand.

**Zero-token-drop check (O):** the O09 assembled tool's census closes conservation exactly:
`2556 + 166 + 0 + 7 = 2729` couples findings + `1` named glob artifact = `2730` refs; 50
distinct fallback mappings / 166 occurrences; 7 unresolved rows each carry a named reason and
`c12=blocker`. I reproduced this (see §2).

---

## 2. Claim O — the instrument exists, but not at the claimed durable path

### 2.1 What is real

- `tools/harness/couples-reference-extractor.py` is tracked at `7ceff59`
  (`git ls-files` confirms), sha256 `d8d23a26…`, 332 lines; `--selftest` is **8/8 PASS**;
  r42 `validation.json` records O `"passed": true`.
- O09 assembled a **515-line successor body** for the claimed path, fenced at
  `op/O09-scribe.md:356-870`, sha256
  `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`. I extracted it
  byte-exact (hash matches), ran it from a clean scratch directory, and reproduced:
  - `--selftest` -> **27/27 PASS**, exit 0, including S1b "4/4 by identity", S3a/S3b
    ambiguous, S2 phantom, S8/S8b glob ordering, S7c blank-line over-capture;
  - `--census` -> `entries=223 refs=2730`, `direct=2556 fallback=166 ambiguous=0
    unresolved=7`, `glob-fragment=1` excluded, `conservation: True`,
    `fallback mappings (50 distinct)` summing to **166** occurrences, 7 unresolved rows with
    reasons (`declared-prospective-seed` x5, `dangling-reference` x2), each `c12=blocker`.

### 2.2 What is not real (at my cut)

- `tools/harness/basename-couples-resolver.py` **does not exist** (`ls` -> No such file).
  The claim's first two counting commands
  (`python3 tools/harness/basename-couples-resolver.py --selftest/--census`) **fail** at HEAD.
- `reports/round-43/calib/` contains **no census artifact** (only the Ca files). The 2730
  census was run from a fenced draft, not filed.
- `O01` — the seat that owns the draft — is **absent** at my cut (`op/O01-tool-draft.md`).
  O04, O05 and O12 correctly record `could-not-evaluate` rather than a pass; O09 supplies the
  assembled fallback body. R01's O verdict is `unprovable-but-better`.
- **Reproducibility trap:** the tool's lane-root discovery walks upward to the nearest
  `corpus/knowledge`. Running the same extracted body from `.scratch/x02` (which contains a
  stale 212-entry `corpus/` copy) silently yields `entries=212 refs=2508` (2337 direct / 163
  fallback / 7 unresolved). From `.scratch/x02run` (no shadow corpus) it yields 223/2730.
  Install it at `tools/harness/` or run it from a clean directory; never grade it from a
  scratch tree with a corpus copy above it.

### 2.3 Honest O verdict

**The claim's `before` is false; its `after_required` is not yet met; the axis is improvable if
the integrator applies O09's body and files the census.** As filed, claim O is
`could-not-evaluate`/not-yet-delivered, not "fixed". The 4/4 wrapped read is real; the
disposition leg and four-class census are real in the draft; the durable path is empty.

---

## 3. Claim C — a false premise, not a hard landing

Measured, independently:

```
corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
  192 lines, 61,884 B, sha256 c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f
  added by 7ceff59; title: "Stone, gem and metal symbolism — the lithic register..."
```

- The r42 C04 fenced body (`reports/round-42/cov/C04-entry-4.md`, fence `:53`/`:246`, body
  `:54-245`) extracts to the **same 61,884 bytes and same sha256** — I recomputed it.
- The r42 C01 spare body (`reports/round-42/cov/C01-mineral-spare.md:4-218`) is **55,101 B**,
  sha `6999a912…` — a *second draft of the same topic*, and its own line 1 says C04 lands and
  "THIS draft is routed as the named spare for a future re-scoped claim."
- `corpus/README.md:5-12` rev 2.4 records the collision and routing; `:219` already indexes
  the lithic entry; `:544` totals 223.
- Nine seats independently report the collision (K02, C01, C03, C04, C05, C06, C07, A01,
  X00); X01 and R01 file it as a trade/blocker; C06's verdict is "BLOCKING COLLISION"; C01's
  is "BLOCKED — the spare's topic is already owned on disk."

Claim C's threshold "no existing entry overwritten" and the shared rule "never overwrite an
existing entry; report collisions" both forbid the declared landing. A new slug would reach
27/224 arithmetically but create **two owners of one register** and land the spare's
now-false head block (`:7` "no entry owns stone", `:24` HEAD `ac47c78`/220 files). The sweep
cannot detect this: C05 measured a staged 224 tree with **two** lithic-register owners while
the sweep was green (`cov/C05-delta-receipt.md:159-161`). The honest C verdict is **blocked /
unchanged at 26/223**; no 224 was delivered.

---

## 4. Claim Ca — the pass exists; the filed artifact does not

At my cut:

- `reports/round-43/calib/dispositions-r38-r39.json` **does not exist**. Ca01's out is a
  `.md` with the JSON fenced at §8; Ca03's out is a `.md` with a queue-successor JSON fenced
  at §3. The claim's `after_required` names the JSON artifact and the queue successor; neither
  is filed as a separate artifact. The integrator must apply both.
- Ca01's four row classes are cited and measured (see §1.3), but carry the three defects
  Ca02 corrects: D-3 -> `recorded`; R01-13 -> `fixed-with-evidence` (r40); the §2 counts line
  -> `1/10/7/4 = 22`. Also reword "cannot be recovered in any durable artifact" (the quotes
  are in O03) and fix the four `parent_row` end lines.
- Ca02 independently re-measured every row and every cited digest; its M12 parse confirms the
  JSON's 22 legs. Its gate §6 is the correct precondition for filing.
- Ca03's queue successor pins the parent at
  `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`; I re-computed the
  parent sha and it matches; the parent file is not edited.

**Honest Ca verdict:** every named row reaches a class; zero findings are dropped (19
findings, 22 legs); every "fixed" claim has a re-run citation — but the artifact must be
filed with Ca02's amendments, and Ca01's prose count must not be copied.

---

## 5. Write surface and corpus integrity (the "no seat outside its out path" check)

Snapshot: **31 files** under `reports/round-43/` at 17:07Z = 3 contract/telemetry files
(`claims.json`, `targets.json`, `telemetry/dispatch-declared.json`) + 28 seat fragments.

```
declared outs in targets.json: 32
present at snapshot:           28
missing:                       O01 op/O01-tool-draft.md
                               O08 op/O08-policy-check.md
                               R02 review/R02-review.md
                               X02 cross/X02-honesty.md   (this file, written after the snapshot)
undeclared non-telemetry files: none
each present .md header's seat id == its path's declared seat: yes (checked all 28)
```

```
$ git status --porcelain=v1
?? reports/round-43/
$ git diff --stat HEAD -- corpus tools reports/round-19 reports/round-27 reports/round-28
(empty)
$ find corpus/knowledge -name '*.md' | wc -l     -> 223
$ ls corpus/knowledge/myth-symbol/*.md | wc -l   -> 26
$ ls reports/round-43/run-validation.py           -> No such file or directory
$ ls tools/harness/basename-couples-resolver.py   -> No such file or directory
$ ls reports/round-43/calib/*census*              -> No such file or directory
```

No `M`/`A`/`D` entry under `corpus/`, no staged index change, no filed-round edit, no
`run-validation.py` in the round directory. This is corroborated independently by O12's
static+dynamic write-surface gate and A01's scope audit; I did not rely on their reports alone.

**One provenance defect in the contract surface:** `reports/round-43/claims.json` is
**6,546 B / `9662e2bd…`**, while `telemetry/dispatch-declared.json` pins it at **6,353 B /
`beda7644…`**. S02 shows the live file is the canonical `indent=1` serialization, and no
formatting of the live content produces 6,353 B; the declared row therefore names different
content (or a staging copy that never landed). Both files carry the same nanosecond mtime
(`16:53:15.764970004Z`), so the cause is `to-verify`, owner integrator. The fix must be an
append-only amendment, never an edit to `dispatch-declared.json`.

---

## 6. Wording scan: no "should work" assertion

Regex `should work|should be|should read|probably|presumably|likely|I assume|appears to|seems to|expected to|will work|must work|obviously` over all `reports/round-43/**/*.md`:

| file:line | context | classification |
|---|---|---|
| `plan/P01-plan.md:381` | `"Should be fixed" is not a class.` | quotation / rule |
| `op/O04-verify.md:27` | "no requirement below should be read as ..." | disclaimer |
| `op/O07-durability.md:39` | "should be mandatory" | recommendation |
| `op/O03-predicted.md:523` | "any divergence should be explained ..." | requirement |
| `op/O03-predicted.md:527` | "whether they should be written" | to-verify question |
| `op/O05-traps.md:124` | "most likely to be missed" | risk note |
| `calib/Ca01-dispositions.md:506` | "should be carried into the next protocol amendment" | routing |
| `adj/A01-scope.md:195` | "it should read `25/26/25/29/24/94`" | correction |
| `review/R01-review.md:236` | "The spare should be retired" | recommendation |
| `review/R01-review.md:271` | "The likely explanation is ..." | labeled hypothesis |
| `review/R01-review.md:287` | "the row should read ..." | correction |

**No seat says "it should work" as a substitute for a measurement.** The hedges that exist are
properly bounded (predictions labeled, hypotheses named, corrections explicit).

---

## 7. Secondary numeric findings (not all claim-critical, all measured)

| id | severity | finding | evidence |
|---|---|---|---|
| **H1** | **blocking (contract)** | O's `before` is false: a durable, selftest-green resolver exists at HEAD | `git ls-files tools/harness/couples-reference-extractor.py`; `--selftest` 8/8; r42 `validation.json` O passed; O12-F2:244 |
| **H2** | **blocking (contract)** | C's `before` is false: the lithic slot is owned | 192 lines / 61,884 B / `c99f44ca…`; `git log 7ceff59 -- .../mineral-stone-symbolism.md`; README rev 2.4 |
| **H3** | minor (provenance) | `claims.json` 6,546 B / `9662e2bd…` vs dispatch-declared 6,353 B / `beda7644…`; cause `to-verify`, append-only fix | S02 §2 T1; A01-2 |
| **H4** | **must fix before Ca filing** | Ca01 §2 counts line says 1/8/6/5 (sum 20); its JSON and a programmatic recount say 1/10/7/4 (sum 22) | Ca01:86-87; Ca02:162-165; my parse |
| **H5** | **must fix before Ca filing** | Ca01 classes all three O02 sub-findings `could-not-recover`; D-3 survives at `O02:164` and must be `recorded` | Ca01 §3; Ca02 §2.3; `O02-isolated.md:160-166` |
| **H6** | **must fix before Ca filing** | Ca01 classes R01-13 `recorded`; r40 landed G2-G4 (linguistics 21 -> 25), so it is `fixed-with-evidence` at r40 | `reports/round-40/claims.json`; SCORECARD.md:790; Ca02 §2.4 |
| **H7** | must reword | Ca01's "the cited quotes cannot be recovered in any durable artifact" is false; O03-verify durably carries them | `O03-verify.md:259-291` |
| **H8** | minor (metadata) | Ca01's four `parent_row` end lines are one past the queue rows (`:282-291` vs `:282-290`, etc.) | `defect-queue-v2.json:282-290,292-300,302-310,343-351` |
| **H9** | **high if S01's table is used** | S01 classes R01-7 `fixed-with-evidence`, claiming the 263-line policy carries block extraction + disposition. Measured: the policy says "single physical line" at `:16`; `grep -ci block` = 0, `grep -ci disposition` = 0. R01-7 remains `routed` (Ca01/Ca03/Ca02 are correct). | `basename-couples-policy-full.md:14-25`; S01:394 |
| **H10** | minor | C07 says the live entry and C04 fence body are "both lengths 61343 bytes"; measured both are **61,884 B** (same sha `c99f44ca…`) | C07:215; my fence extraction |
| **H11** | minor (reproducibility) | K02's §4 sweep commands use `grep -i 'a|b|c'` without `-E`/`\|`; as written they return rc=1/no output. The `-E` forms reproduce K02's shown hits; the conclusion stands. | K02:129,132; my exact-command rerun |
| **H12** | minor | O04 says "**49 entries** carry braces"; measured **79 entries / 218 groups / 977 expanded occurrences** (O05 corrects it; I reproduced 79/218/977) | O04:188; O05:39,311 |
| **H13** | pre-existing docs defect | README rev 2.4 prose vector `25/23/25/29/24/94 → 25/23/26/25/24/94` sums to 217, not 223; footer/sweep are correct. C02's conditional rev 2.5 does not repair it. | `corpus/README.md:5-12`; A01:195 |
| **H14** | integration risk | The O09 tool resolves the lane root upward; run from a scratch tree containing a stale `corpus/` copy it silently reports 212/2508. Install at `tools/harness/` or run from a clean dir. | my `.scratch/x02` vs `.scratch/x02run` runs |
| **H15** | **blocking for O as declared** | The claimed durable path and census artifact are absent; the counting commands fail at HEAD. O09's fenced body is 27/27 and 223/2730, but integration has not happened. | `ls tools/harness/basename-couples-resolver.py`; `ls calib/*census*` |
| **H16** | positive | 28/32 declared out paths present; zero undeclared non-telemetry files; all headers match their seat; corpus/tools/filed rounds clean; no corpus staging | §5 |
| **H17** | positive | No substantive "should work" wording (§6) | §6 |
| **H18** | `could-not-evaluate` | O01, O08, R02 had not filed at 17:07Z. O08's independent policy-conformance checklist and R02's second review are unavailable; claim O's named author is absent. Do not score their silence as a pass. | missing-out scan |

---

## 8. Limits / `to-verify`

- **Snapshot, not close.** The round was still in flight at 17:07Z; O01, O08 and R02 may land
  after this file. Their absence is recorded as `could-not-evaluate`, not as failure. A
  post-write re-check at 17:10Z found the same three still absent (29 `.md` fragments present:
  28 seats + this file).
- **Pre-amendment `claims.json` bytes are unrecoverable** from the repo (no git history for
  the untracked round dir; the declared digest names different content). Cause stays
  `to-verify`, owner integrator.
- I did **not** re-run C02/C05's staged 224 sweeps; I verified that their 224 numbers are
  labeled predictions and that the live tree is 223. The staged scratch trees may be
  inspected, but a staged green is not a delivery certificate.
- I did **not** verify every citation in C03's 344-line source audit or every row of O05's
  trap matrix; I sampled the load-bearing numbers (4/4, 223/26, counts, brace/anchor/last-field
  populations) and report the rest as attributed to those seats, not independently certified.
- I did **not** execute any `run-validation.py`; none exists in `reports/round-43/`.
- The O09 body's 27/27 and 223/2730 were run from `.scratch/x02run` (same bytes, hash
  `43ce341f…`), not from the durable path, because writing `tools/harness/` is outside this
  seat's write surface.

---

## 9. Integration recommendations (evidence only; no decisions taken here)

1. **C:** do not apply the spare; record `blocked-by-topic-collision`; keep 26/223 and README
   rev 2.4. If a future round re-scopes, the spare's bytes are not the deliverable — its head
   block is stale and its topic is owned.
2. **O:** correct the `before` line in the round record (or re-scope O as
   census+disposition); apply O09's body to
   `tools/harness/basename-couples-resolver.py`; run `--selftest` and `--census`; file **one**
   census artifact (O06 and O10 disagree on the name; O06 owns the name by mission); pin the
   tool sha and label the r42 extractor as witness-only. Do not ship two live authorities.
3. **Ca:** apply Ca02's five amendments to the disposition JSON; file it as a new artifact and
   file the queue successor as a new artifact; do not edit
   `reports/round-40/op/defect-queue-v2.json`.
4. **Contract:** file an append-only amendment for the stale `claims.json` digest; fix the
   README rev 2.4 prose vector (217 -> 223) only if a README edit is otherwise made.
5. **Close:** re-run the write-surface census at the close cut; if O01/O08/R02 remain absent,
   record them `could-not-evaluate` with owner, not zero-impact.

---

## Appendix — command log (all from the lane root unless noted)

```
git rev-parse --short HEAD                                  -> 7ceff59
git status --porcelain                                      -> ?? reports/round-43/
ls corpus/knowledge/myth-symbol/*.md | wc -l                -> 26
find corpus/knowledge -name '*.md' | wc -l                  -> 223
python3 -B reports/round-28/readme/sweep.py                 -> rows 223 files 223, exit 0
sha256sum corpus/knowledge/linguistics/phonetics-phonology.md
                                                            -> b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b
python3 tools/harness/couples-reference-extractor.py --selftest  -> 8 PASS, exit 0
python3 tools/harness/couples-reference-extractor.py --census    -> 223/2730, 2556/166/2/5/1
python3 tools/harness/couples-reference-extractor.py corpus/knowledge/linguistics/phonetics-phonology.md
                                                            -> wrapped=True tokens=4 (2 direct, 2 prospective)
# O09 fenced body extraction and run:
python3 - (extract ```python fence from op/O09-scribe.md)
   body 515 lines, 21,732 B, sha256 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
   python3 -B .scratch/x02run/tool.py --selftest             -> SELFTEST OK: 27/27 controls, exit 0
   python3 -B .scratch/x02run/tool.py --census               -> entries=223 refs=2730;
                                                                 direct=2556 fallback=166 ambiguous=0 unresolved=7;
                                                                 glob-fragment=1; conservation True;
                                                                 50 distinct fallback mappings / 166 occurrences
# Ca01 JSON parse:
python3 - (parse ```json fence)                              -> counts 1/10/7/4 = 22; row classes 1/2/0/1;
                                                                 findings 19; dropped 0
# Wrapped-field independent extraction:
python3 - (block 72-77; newline join / space join / hyphen heal)
                                                            -> 4 tokens each; only hyphen heal yields tone-prosody.md
# Corpus integrity:
git diff --stat HEAD -- corpus tools reports/round-19 reports/round-27 reports/round-28  -> empty
ls reports/round-43/run-validation.py                        -> absent
ls tools/harness/basename-couples-resolver.py                -> absent
ls reports/round-43/calib/*census*                           -> absent
```

No filed byte was edited by this seat. Writes: this file only, plus disposable
`.scratch/x02/` and `.scratch/x02run/`.
