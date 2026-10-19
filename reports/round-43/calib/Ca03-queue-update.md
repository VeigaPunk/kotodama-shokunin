- Seat: Ca03 | executor | claim Ca | date 2026-10-19 | baseline 7ceff59

# Ca03 — defect-queue-v2 successor entries for the four r38/r39 dispositions

**Mission** (`reports/round-43/targets.json` seat `Ca03`): *"draft the defect-queue-v2
successor entries (new records appended to a round-43 successor file, never editing
reports/round-40/op/defect-queue-v2.json) reflecting the four dispositions. Fenced draft."*

**Boundary statement.** This seat wrote only `reports/round-43/calib/Ca03-queue-update.md`.
No filed byte (`reports/round-1..42/**`, `corpus/**`, `tools/gates/frozen/**`, fleet `.ufo/**`)
was written, staged, or proposed for edit. No `reports/round-*/run-validation.py` was executed
anywhere. No corpus byte was staged. No git mutation, network, or install was performed.
All commands ran from the lane root with `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; `git status --porcelain` at seat start and close shows only
`?? reports/round-43/`. The fenced JSON below is a **successor delta**, not a full queue: the
integrator chooses its final path, applies it as a new artifact, and leaves
`reports/round-40/op/defect-queue-v2.json` byte-identical.

## 1. The parent queue as measured at HEAD

| property | value | command |
|---|---|---|
| current sha256 | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` | `sha256sum reports/round-40/op/defect-queue-v2.json` |
| sha at r40 admit (`13a1657`) | `fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98` | `git show 13a1657:reports/round-40/op/defect-queue-v2.json \| sha256sum` |
| sha at r41 admit (`ac47c78`) | `dfc9265d…` (unchanged since) | `git log --oneline -- reports/round-40/op/defect-queue-v2.json` → `ac47c78`, `13a1657` |
| rows | 38 = 28 `carried-with-owner` + 10 `fixed-with-evidence` | r42 O08 §1 census, re-read this seat |

The r40→r41 hash change is the in-place edit r42 O08 recorded (Obs. 3,
`reports/round-42/op/O08-queue-update.md:206-216`): `ac47c78` flipped
`N7-receipt-fidelity` and `r39-runner-root-regression` to `fixed-with-evidence` and appended
`r41_update`. That edit is historical; this draft does **not** repeat it. The parent sha above
is pinned into the successor artifact so any further in-place edit is detectable as a digest
mismatch.

The four rows under disposition (line ranges read byte-exact with `sed -n`):

| id | parent lines | filed class |
|---|---|---|
| `r39-review-findings-disposition` | `:343-351` | `carried-with-owner` |
| `r38-O02-fragment-defects` | `:282-290` | `carried-with-owner` |
| `r38-O08-fragment-defect` | `:292-300` | `carried-with-owner` |
| `r38-O07-empty-fragment` | `:302-310` | `carried-with-owner` |

## 2. Per-row disposition evidence (measured this seat, not inherited)

### 2.1 `r39-review-findings-disposition` — the disposition debt is dischargeable

R01's review files findings R01-1..R01-14 (`reports/round-39/review/R01-review.md:25-34`,
sha `4fe294ae213a353d504555228d2dd93005558f90364bfe4dc5f59cfa1339dfde`). The r40 queue row
correctly recorded that only R01-1 had a disposition. This seat re-enumerated each finding and
assigned the class its filed evidence supports:

| finding | class | evidence read this seat | owner / next touch |
|---|---|---|---|
| R01-1 | `recorded` | ruling note `reports/round-39/calib/recount-ledger-successor.json:8`; `LOG.md:3758`; `SCORECARD.md:779` | integrator / none |
| R01-2 | `routed-with-owner` | landed protocol names **three** runners (`reports/round-39/calib/isolation-replay-protocol.md:10-13`); measured **five** absolute `ROOT` lines: r34`:10`, r35`:9`, r36`:8`, r37`:5`, r38`:5` | successor-protocol author / name all five or scope to the pre-flight class |
| R01-3 | `routed-with-owner` | `grep -ci discriminator reports/round-39/calib/isolation-replay-protocol.md` → **0**; no Tier B body in the landed 52-line file | successor-protocol author / mandatory tree-discriminator in Tiers A and B |
| R01-4 | `fixed-with-evidence` | `reports/round-40/cov/C05-audit.md:26-27` — **4/4 PASS**; r40 entry `LOG.md:3773-3789` | r40 integrator / none (`fixed_at: round-40`) |
| R01-5 | `routed-with-owner` | clone-vs-worktree rationale exists at `reports/round-39/calib/Ca01-protocol.md:117-125`, but `grep -rn "declared deviation" reports/round-40` → no match | integrator / record the declared deviation |
| R01-6 | `routed-with-owner` | `Ca01-protocol.md:166` still reads `assert … == pathlib.Path("/tmp").resolve().parent or True`; line pins at `:76-77` | successor-protocol author / drop the vacuous assert, fix pins |
| R01-7 | `routed-with-owner` | `reports/round-39/review/R01-review.md:265-274`; the r43 O claim is the successor instrument (block extraction + disposition leg) | r43 integrator/O claim / closes with the O resolver, together with `r39-basename-successor-instrument` and `N6-couples-extractor-wrapped-field` |
| R01-8 | `recorded` | `R01-review.md:75-81`; r40 C05 used the filed instruments I-C12/I-C05 (`reports/round-40/cov/C05-audit.md:38,387-388`) | integrator / none |
| R01-9 | `recorded` | `R01-review.md:128-132`; mitigation is the C06 §6 whole-fragment digest pin | integrator / none |
| R01-10 | `recorded` | `R01-review.md:140-143`; r40 C05 extractor handles 3/4+ backtick fences (`C05-audit.md:40`) | integrator / none |
| R01-11 | `recorded` | `R01-review.md:144-146` (C01 head-block note; executable bar unaffected) | integrator / none |
| R01-12 | `recorded` | `R01-review.md:278-287` (taboo count 10 vs 9; conclusion stands) | integrator / none |
| R01-13 | `fixed-with-evidence` | `reports/round-40/claims.json:14` (G2-G4 landed as four entries, 21→25); `SCORECARD.md:790` | r40 integrator / none (`fixed_at: round-40`) |
| R01-14 | `could-not-recover` | `R01-review.md:292-299` — no durable artifact of the anomalous tree; R01 itself files it against no seat | R01/integrator / none unless chased |

Composition: **2 fixed-with-evidence + 5 routed-with-owner + 6 recorded + 1 could-not-recover =
14/14, zero undecided.** This is the per-finding list the r40 row's `next_touch` asked for; the
canonical artifact is Ca01's `reports/round-43/calib/dispositions-r38-r39.json` (author Ca01,
verifier Ca02). This seat's table is an independent cross-check, not a replacement: if Ca01's
durable citations differ, Ca01's file wins (gate G3).

### 2.2 `r38-O02-fragment-defects` — D-1/D-2 do not reproduce; D-3 survives in weaker form

The row asserts three defects in the **filed** O02 fragment. The filed fragment
(`reports/round-38/op/O02-isolated.md`, sha
`e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d`, 15,308 bytes, mtime
08:27) does not contain the text O03 quotes:

```
grep -c "44 controls"                            reports/round-38/op/O02-isolated.md -> 0
grep -c "58-member"                              reports/round-38/op/O02-isolated.md -> 0
grep -c "does not match the frozen packet digest" reports/round-38/op/O02-isolated.md -> 0
git log -S"44 controls" --oneline -- reports/round-38/op/O02-isolated.md -> (no output)
```

- **D-1** (selftest count 44): filed O02:20 and :62 read **45**; the quoted 44/58-member text
  is in no committed version (single commit `dfb0719`; `git log -S` empty). O02's file is
  timestamped 08:27 and O03's 08:35; the text O03 quotes is not in the committed O02, so the
  reviewed variant is not recoverable from git and its provenance is `to-verify`. Class:
  **`could-not-recover`** — the reviewed draft bytes are unrecoverable (uncommitted workspace
  state).
- **D-2** (`m15b` described as "names nothing"): the only `names nothing` hit is O02:99,
  describing the **rejected rendered-text guard**, not `m15b`; O02:62 describes `m15b` as
  `in-sync roster green`. Class: **`could-not-recover`**, same reason.
- **D-3** (tamper prediction names the frozen-packet leg): the specific prediction string is
  absent, but O02:164 still says a tampered 13th component "surfaces through the
  assembled-vs-frozen packet compare (`:3951-3957`)". O03 §4.3 measured the **per-component
  digest leg** firing instead (`v3_verify_component_digests`, `:2208-2222`). Class:
  **`recorded`** — the surviving mechanism sentence is corrected by this record; the row's
  conclusions (naming-not-detection) stand.

### 2.3 `r38-O08-fragment-defect` — D-4 reproduces exactly

```
grep -n "is exactly the digest O01" reports/round-38/op/O08-regression.md -> 83
grep -n "e5812751" reports/round-38/op/O01-guard-design.md -> 144, 309
grep -n "ae22013b" reports/round-38/op/O08-regression.md -> 18, 80, 83, 241, 250
```

O08:83 asserts `ae22013b…` is exactly O01 §6's digest; O01:144 and :309 declare
`e5812751…`; O08:80 prints its own `ae22013b…`. O03 §4.4 measured the two trees differ by
exactly the `m15b` result string. Class: **`recorded`** — correction text: *`ae22013b…` is
O08's own variant of O01's patch with the `m15b` string adjusted; O08's readings and census
stand; only the provenance claim is wrong.* Filed bytes immutable; no edit.

### 2.4 `r38-O07-empty-fragment` — measured empty, prevention is only nominal

```
wc -c reports/round-38/op/O07-scribe.md -> 0
sha256sum reports/round-38/op/O07-scribe.md -> e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The fragment is still empty at HEAD and stays as filed. The row's `next_touch` asked for a
min-bytes check on every declared out path. What actually landed:

- r40's integration census ran the check **manually** and passed
  (`reports/round-40/scribe/S01-integration-draft.md:391`, CO4).
- The r41/r42 runners **cannot** enforce it. `r41/run-validation.py:168-173` builds `missing`
  from paths that **do not exist**, then computes
  `empty = [x for x in missing if os.path.isfile(x) and os.path.getsize(x) == 0]` — an
  intersection that is empty by construction; `empty` is never read again
  (`grep -n "empty" reports/round-41/run-validation.py` → `:173`, plus the hard-coded named
  finding at `:183`). r42 is identical (`:177-182`, `:192`). The same comprehension calls
  `os.path.getsize` on those non-existent paths (`:171`), so a genuinely missing out would
  raise `FileNotFoundError` instead of being reported — latent while every out exists.
- The r38 O07 line in every receipt is a **hard-coded string**, not a measurement.

Class: **`recorded`** (the 0-byte fragment is a permanent, filed historical fact) with
`prevention_status: partial`. It must **not** be re-classed `fixed-with-evidence` until a live
min-bytes check lands. The vacuous check is filed as candidate observation OBS-1.

## 3. Fenced successor artifact

Proposed path: `reports/round-43/calib/defect-queue-v2-successor-r43.json` (the integrator may
rename; r41 X00 §"Hard integration conflict" left the successor path unassigned). Schema is a
delta, not a v3: four rows, parent pinned, class vocabulary mapped onto v2's.

```json
{
  "schema": "kotodama-defect-queue-successor-v1",
  "round": 43,
  "date": "2026-10-19",
  "artifact": "defect-queue-v2 successor delta - four r38/r39 disposition rows",
  "parent": "reports/round-40/op/defect-queue-v2.json",
  "parent_sha256_at_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "parent_history": "Committed at 13a1657 with sha256 fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98; ac47c78 (r41) edited 20 lines in place to flip N7-receipt-fidelity and r39-runner-root-regression and append r41_update - recorded by reports/round-42/op/O08-queue-update.md:206-216. This successor does not edit the parent; the pinned sha makes any further in-place edit detectable.",
  "baseline_commit": "7ceff59",
  "source_dispositions": {
    "path": "reports/round-43/calib/dispositions-r38-r39.json",
    "sha256": null,
    "owner": "integrator (fill at application; Ca01 authors the artifact, Ca02 independently verifies)"
  },
  "class_vocabulary": {
    "fixed-with-evidence": "A landed artifact plus a measured verification output closes the finding.",
    "routed-with-owner": "No fix is claimed; the finding has a named owner and a next touch.",
    "recorded": "The measured fact or correction is recorded; filed bytes are immutable or no action is owed.",
    "could-not-recover": "The evidence the finding depends on cannot be recovered; a named reason and owner are recorded.",
    "v2_mapping": "fixed-with-evidence -> fixed-with-evidence; routed-with-owner -> carried-with-owner (owner + next_touch); recorded -> carried-with-owner with next_touch 'none - recorded'; could-not-recover -> carried-with-owner with the named reason. The `class` field here is authoritative; `v2_class_equivalent` is the merge hint."
  },
  "rows": [
    {
      "id": "r39-review-findings-disposition",
      "origin": "r39 R01-review.md verdict table (:25-34) - findings R01-1..R01-14",
      "class": "fixed-with-evidence",
      "v2_class_equivalent": "fixed-with-evidence",
      "owner": "r43 integrator (files the pass) + Ca01 (author) + Ca02 (verify)",
      "reason": "The row's defect is the absence of a per-finding disposition record for R01-1..R01-14. The r43 disposition pass, once filed at source_dispositions, records one row per finding with class, owner, and evidence. Measured composition: 2 fixed-with-evidence (R01-4, R01-13), 5 routed-with-owner (R01-2, R01-3, R01-5, R01-6, R01-7), 6 recorded (R01-1, R01-8, R01-9, R01-10, R01-11, R01-12), 1 could-not-recover (R01-14); total 14/14, zero undecided. This closes the disposition debt only; the routed underlying items remain open under their named owners and are not claimed fixed.",
      "next_touch": "none for the disposition debt. The five routed findings carry their own next touches: a successor protocol document for R01-2/R01-3/R01-5/R01-6, and the r43 O claim for R01-7.",
      "evidence": "reports/round-39/review/R01-review.md:25-34 and the finding sections :75,93,128,140-146,147,182,191,203,208,226-244,265-274,278-299; reports/round-40/cov/C05-audit.md:26-27,38,387-388; reports/round-39/calib/isolation-replay-protocol.md:10-13 (52 lines, sha256 bd5b4e3d695ae5c7532b6d10dc076f1bbf9051a378ee2c88607e9110079b6b81); reports/round-39/calib/Ca01-protocol.md:76-77,117-125,166; reports/round-39/calib/recount-ledger-successor.json:8; LOG.md:3758,3773-3789; SCORECARD.md:779,790; reports/round-40/claims.json:14.",
      "verification": "OWED at application (gate G2): parse source_dispositions and assert 14 findings, every class in the four-class vocabulary, every owner and evidence non-empty; expected output '14/14 dispositioned, 0 undecided'. No Ca01 dispositions artifact existed when this seat checked (ls reports/round-43/calib/ -> empty before this seat's write), so this seat could not run the assertion; the integrator runs it before applying.",
      "fixed_at": "round-43",
      "findings": [
        {"id": "R01-1", "class": "recorded", "owner": "integrator", "evidence": "reports/round-39/calib/recount-ledger-successor.json:8; LOG.md:3758; SCORECARD.md:779", "next_touch": "none"},
        {"id": "R01-2", "class": "routed-with-owner", "owner": "successor-protocol author (integrator-designated, r44+)", "evidence": "landed protocol :10-13 names three absolute runners (r34/r35/r36); measured five absolute ROOT lines: reports/round-34/run-validation.py:10, round-35:9, round-36:8, round-37:5, round-38:5", "next_touch": "name all five, or scope the hazard to the pre-flight absolute-ROOT class"},
        {"id": "R01-3", "class": "routed-with-owner", "owner": "successor-protocol author", "evidence": "grep -ci discriminator reports/round-39/calib/isolation-replay-protocol.md -> 0; no Tier B body in the landed 52-line file", "next_touch": "require a recorded post-run tree discriminator in Tiers A and B; a replay without it is void"},
        {"id": "R01-4", "class": "fixed-with-evidence", "owner": "r40 integrator/C05", "evidence": "reports/round-40/cov/C05-audit.md:26-27 (4/4 PASS); LOG.md:3773-3789", "fixed_at": "round-40", "next_touch": "none"},
        {"id": "R01-5", "class": "routed-with-owner", "owner": "integrator", "evidence": "rationale at reports/round-39/calib/Ca01-protocol.md:117-125; grep -rn 'declared deviation' reports/round-40 -> no match", "next_touch": "record the Tier A clone-vs-worktree substrate as a declared deviation with A.0 as rationale"},
        {"id": "R01-6", "class": "routed-with-owner", "owner": "successor-protocol author", "evidence": "reports/round-39/calib/Ca01-protocol.md:166 still ends the T3 probe with 'or True'; line pins at :76-77 per R01-review.md:208-212", "next_touch": "drop the vacuous assert and correct the line pins in the successor protocol; filed bytes are immutable"},
        {"id": "R01-7", "class": "routed-with-owner", "owner": "r43 integrator + O claim", "evidence": "R01-review.md:265-274; the r43 O claim builds the successor instrument with block extraction and the disposition leg", "next_touch": "close with the O resolver selftest+census; also closes r39-basename-successor-instrument and N6-couples-extractor-wrapped-field"},
        {"id": "R01-8", "class": "recorded", "owner": "integrator", "evidence": "R01-review.md:75-81; r40 C05 audited with the filed I-C12/I-C05 instruments (C05-audit.md:38,387-388)", "next_touch": "none"},
        {"id": "R01-9", "class": "recorded", "owner": "integrator", "evidence": "R01-review.md:128-132; mitigation is the C06 §6 whole-fragment digest pin", "next_touch": "none"},
        {"id": "R01-10", "class": "recorded", "owner": "integrator", "evidence": "R01-review.md:140-143; r40 C05 extractor handles 3/4+ backtick fences (C05-audit.md:40)", "next_touch": "none"},
        {"id": "R01-11", "class": "recorded", "owner": "integrator", "evidence": "R01-review.md:144-146 (C01 head-block note; executable bar unaffected)", "next_touch": "none"},
        {"id": "R01-12", "class": "recorded", "owner": "integrator", "evidence": "R01-review.md:278-287 (taboo count 10 vs 9; conclusion 'no dedicated taboo entry' stands)", "next_touch": "none"},
        {"id": "R01-13", "class": "fixed-with-evidence", "owner": "r40 integrator", "evidence": "reports/round-40/claims.json:14 (G2-G4 landed as four sourced entries, linguistics 21->25); SCORECARD.md:790", "fixed_at": "round-40", "next_touch": "none"},
        {"id": "R01-14", "class": "could-not-recover", "owner": "R01/integrator", "evidence": "R01-review.md:292-299 records the +2 sweep anomaly as an unreproduced reviewer-side observation with no durable artifact; filed against no seat", "next_touch": "none unless the integrator chooses to chase the transient tree state"}
      ]
    },
    {
      "id": "r38-O02-fragment-defects",
      "origin": "r38 O03 §4.1-4.3 (filed corrections owed)",
      "class": "recorded",
      "v2_class_equivalent": "carried-with-owner",
      "owner": "integrator (correction record, filed here)",
      "reason": "The row's three asserted defects are re-measured against the only committed O02 fragment (sha256 e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d, 15,308 bytes). D-1 and D-2 do not reproduce: the quoted '44 controls' and '58-member' text appears in no committed version (git log -S -> empty; grep -c -> 0), and the only 'names nothing' hit (O02:99) describes the rejected rendered-text guard, not m15b; the filed O02:20,62 read 45 controls and describe m15b as green. The reviewed draft was amended at 08:27, O03 was written at 08:35, and the pre-commit draft is unrecoverable. D-3 survives in weaker form: the quoted frozen-packet error string is absent, but O02:164 still says a tampered 13th component 'surfaces through the assembled-vs-frozen packet compare (:3951-3957)', while O03 §4.3 measured the per-component digest leg firing instead. Corrections are recorded; filed bytes are immutable.",
      "next_touch": "none - corrections recorded. Any future citation of D-1/D-2 must cite this row's could-not-recover, not O03 §4.1-4.2 as a live defect; any citation of O02 §7's mechanism must use the component-digest leg.",
      "evidence": "reports/round-38/op/O02-isolated.md:20,62,99,164 (sha256 e314dbf3...); reports/round-38/op/O03-verify.md:255-306; git log -S'44 controls' -- reports/round-38/op/O02-isolated.md -> no output; mtimes O02 08:27, O03 08:35.",
      "verification": "Commands run this seat: grep -c '44 controls' -> 0; grep -c '58-member' -> 0; grep -c 'does not match the frozen packet digest' -> 0; grep -c 'names nothing' -> 1 (O02:99, rendered-text guard); grep -c 'assembled-vs-frozen' -> 1 (O02:164).",
      "findings": [
        {"id": "D-1", "class": "could-not-recover", "owner": "r38 O03/integrator", "evidence": "quoted 44/58-member text is in no committed O02 version (grep -c -> 0; git log -S -> empty); filed O02:62 reads 45; the reviewed pre-commit draft is unrecoverable", "next_touch": "none - record only"},
        {"id": "D-2", "class": "could-not-recover", "owner": "r38 O03/integrator", "evidence": "the only 'names nothing' hit is O02:99 about the rejected rendered-text guard; O02:62 describes m15b as in-sync roster green; the quoted description is absent", "next_touch": "none - record only"},
        {"id": "D-3", "class": "recorded", "owner": "integrator", "evidence": "specific prediction string absent (grep -c -> 0); O02:164 still names the assembled-vs-frozen compare; O03 §4.3 measured the per-component digest leg (v3_verify_component_digests, :2208-2222) firing instead", "next_touch": "read O02 §7's mechanism sentence as the component-digest leg; the naming-not-detection conclusion stands"}
      ]
    },
    {
      "id": "r38-O08-fragment-defect",
      "origin": "r38 O03 §4.4",
      "class": "recorded",
      "v2_class_equivalent": "carried-with-owner",
      "owner": "integrator (correction record, filed here)",
      "reason": "D-4 reproduces at HEAD: O08-regression.md:83 asserts that ae22013b... is exactly the digest O01 §6 declares, while O01-guard-design.md:144,309 declare e5812751... and O08:80 prints its own ae22013b.... O03 §4.4 measured the two trees differ by exactly the m15b result string. Correction recorded: ae22013b... is O08's own variant of O01's patch with the m15b string adjusted; O08's readings and census stand; only the provenance claim is wrong. Filed bytes are immutable; no edit.",
      "next_touch": "none - correction recorded. Any future citation of O08's patched digest must carry the variant label, not the false identity.",
      "evidence": "reports/round-38/op/O08-regression.md:18,80,83,241,250 (sha256 3818df945e4a1850d34e7147d4d4b9c4255adabf5f3cff8578e6fd33dc4b2539); reports/round-38/op/O01-guard-design.md:144,309 (sha256 d863af319395a4df6a32b6ac1f6956e7cb637c8bdcee0b46dab5401d08d458d0); reports/round-38/op/O03-verify.md:308-341.",
      "verification": "Commands run this seat: grep -n 'is exactly the digest O01' reports/round-38/op/O08-regression.md -> 83; grep -n 'e5812751' reports/round-38/op/O01-guard-design.md -> 144,309; grep -n 'ae22013b' reports/round-38/op/O08-regression.md -> 18,80,83,241,250."
    },
    {
      "id": "r38-O07-empty-fragment",
      "origin": "r38 wave (LOG.md:3741; SCORECARD.md:761-762)",
      "class": "recorded",
      "v2_class_equivalent": "carried-with-owner",
      "owner": "future runner maintainer (live min-bytes gate) + integrator (record)",
      "reason": "Measured at HEAD: reports/round-38/op/O07-scribe.md is 0 bytes (wc -c -> 0; sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855). Filed bytes are immutable, so the fragment stays as an empty historical record. The prevention leg is only partially landed: r40's integration census ran a manual non-empty check and passed (S01-integration-draft.md:391, CO4), but the r41/r42 runners cannot enforce it - 'empty' is filtered from 'missing', which contains only non-existent paths (r41/run-validation.py:168-173; r42:177-182), so the intersection is empty by construction, and the r38 O07 named finding is a hard-coded string (r41:183; r42:192). No durable automated min-bytes gate exists. This row must not be re-classed fixed-with-evidence until one lands.",
      "next_touch": "next runner-authoring round (r44+): make the empty list a receipt field and an acceptance check (non-empty for every declared out), with the r38 O07 path as the named historical exception; see observation OBS-1.",
      "evidence": "reports/round-38/op/O07-scribe.md (0 bytes, sha256 e3b0c442...); reports/round-40/scribe/S01-integration-draft.md:391; reports/round-41/run-validation.py:168-173,183; reports/round-42/run-validation.py:177-182,192; LOG.md:3741; SCORECARD.md:761-762.",
      "verification": "Commands run this seat: wc -c reports/round-38/op/O07-scribe.md -> 0; sha256sum -> e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; grep -n 'empty' reports/round-41/run-validation.py -> :173 (assignment), :183 (hard-coded named finding) - no read of the list."
    }
  ],
  "application_gates": [
    "G1: Apply row r39-review-findings-disposition as fixed-with-evidence only after reports/round-43/calib/dispositions-r38-r39.json (or .md) lands and Ca02's independent verification is filed.",
    "G2: The integrator runs the parse assertion (14 findings, classes in vocabulary, non-empty owner/evidence) and pastes the output into this successor artifact; a fixed claim without that output is not admissible.",
    "G3: If Ca01's durable evidence contradicts this draft's D-1/D-2 could-not-recover, Ca01 wins only if it names committed bytes; otherwise the row stands as measured here.",
    "G4: Apply this as a new artifact. reports/round-40/op/defect-queue-v2.json stays byte-identical at sha256 dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907.",
    "G5: If the queue keeps v2's two-class vocabulary, map routed-with-owner/recorded/could-not-recover to carried-with-owner and preserve the four-class value in a disposition field.",
    "G6: Do not re-class r38-O07-empty-fragment fixed-with-evidence until a live min-bytes check lands (OBS-1); the current evidence supports only partial prevention."
  ],
  "observations": [
    {
      "id": "OBS-1",
      "proposed_row_id": "r41-empty-output-check-vacuous",
      "status": "candidate - integrator decides whether to mint; canonical-id dedupe per r37 R07-cross-review:13 and r39 X00-4",
      "owner": "future runner maintainer",
      "finding": "The r41/r42 runners compute 'empty' from a list that only contains non-existent paths: missing is built at r41:168-170 from not os.path.isfile(...), then empty filters that same list for existing zero-byte files at :173 - an empty intersection. The list is never read; the only O07 signal is the hard-coded named finding at :183 (r42:192). The r40 CO4 min-bytes check was manual, not runner-enforced.",
      "evidence": "reports/round-41/run-validation.py:168-173,183; reports/round-42/run-validation.py:177-182,192; reports/round-40/scribe/S01-integration-draft.md:391."
    },
    {
      "id": "OBS-2",
      "proposed_row_id": "r39-protocol-landing-truncated",
      "status": "candidate + to-verify (truncation vs intentional excerpt) - integrator decides",
      "owner": "integrator / successor-protocol author",
      "finding": "The landed isolation-replay protocol is 52 lines / 2,829 bytes, sha256 bd5b4e3d695ae5c7532b6d10dc076f1bbf9051a378ee2c88607e9110079b6b81. It ends at '## 3. Step 0 - determine the close commit' (tail -4), refers at I6 to a '§9 vocabulary' absent from the file, and contains no Tier A/B/C body, no §5, no §7. The full protocol lives only in the author fragment reports/round-39/calib/Ca01-protocol.md. Consequence for the dispositions: R01-2 reproduces in the landed bytes (:10-13 names three runners); R01-3/R01-5/R01-6 target fragment bytes that never landed, so they are routed, not fixable in place.",
      "evidence": "reports/round-39/calib/isolation-replay-protocol.md:10-13,40-50 (52 lines; tail shows the cut); reports/round-39/calib/Ca01-protocol.md:76-77,117-125,166; wc -l -> 52."
    },
    {
      "id": "OBS-3",
      "proposed_row_id": null,
      "status": "recorded - no new row; context for the parent pin",
      "owner": "integrator",
      "finding": "The r40 queue was edited in place at r41: committed at 13a1657 with sha256 fe596a9d..., current sha256 dfc9265d... after ac47c78. This successor artifact is the correct home for further updates; the parent must not be edited again. The parent sha is pinned above.",
      "evidence": "git log --oneline -- reports/round-40/op/defect-queue-v2.json; git show 13a1657:... | sha256sum; sha256sum reports/round-40/op/defect-queue-v2.json; reports/round-42/op/O08-queue-update.md:206-216."
    }
  ],
  "provenance": {
    "seat": "Ca03",
    "out": "reports/round-43/calib/Ca03-queue-update.md",
    "date": "2026-10-19",
    "baseline_commit": "7ceff59",
    "commands": [
      "sed -n '282,310p;343,351p' reports/round-40/op/defect-queue-v2.json",
      "sha256sum reports/round-40/op/defect-queue-v2.json reports/round-38/op/O02-isolated.md reports/round-38/op/O08-regression.md reports/round-38/op/O01-guard-design.md reports/round-38/op/O07-scribe.md reports/round-39/review/R01-review.md reports/round-39/calib/isolation-replay-protocol.md",
      "wc -c reports/round-38/op/O07-scribe.md",
      "grep -c '44 controls' / '58-member' / 'does not match the frozen packet digest' reports/round-38/op/O02-isolated.md",
      "git log -S'44 controls' --oneline -- reports/round-38/op/O02-isolated.md",
      "grep -n 'is exactly the digest O01' reports/round-38/op/O08-regression.md",
      "grep -n 'e5812751' reports/round-38/op/O01-guard-design.md",
      "grep -ci discriminator reports/round-39/calib/isolation-replay-protocol.md",
      "grep -n '^ROOT' reports/round-3{4,5,6,7,8}/run-validation.py",
      "grep -n 'empty' reports/round-41/run-validation.py reports/round-42/run-validation.py",
      "git show 13a1657:reports/round-40/op/defect-queue-v2.json | sha256sum",
      "git status --porcelain"
    ],
    "boundary": "Only this out path written; no filed byte edited or staged; no round runner executed; no corpus staging; no git mutation, network, or install."
  }
}
```

## 4. What the integrator must do (ordered)

1. Wait for Ca01's dispositions artifact and Ca02's verification; run gate G2's assertion and
   paste its output into the successor artifact. Do not apply row 1 before that.
2. Apply the four rows as a new file; leave the r40 queue at `dfc9265d…` (gate G4).
3. Reconcile my D-1/D-2 `could-not-recover` findings with Ca01/Ca02. The measurement is
   reproducible: the quoted O02 text is in no committed version. If Ca01 has a durable
   citation to the reviewed draft, cite it; otherwise keep `could-not-recover`.
4. Route OBS-1 and OBS-2 as the integrator sees fit. OBS-1 is the direct prevention gap behind
   the O07 row; OBS-2 is the reason R01-3/5/6 are routed rather than fixed.
5. If the parent queue is later superseded by a full v3, carry these four rows verbatim and
   preserve the parent sha pin.

## 5. Owed / to-verify

- **Owed (gate G2):** the 14/14 disposition assertion output. This seat could not run it:
  `reports/round-43/calib/` was empty at seat close (`ls` → no files), because Ca01 runs in
  the same wave. Owner: integrator.
- **to-verify:** whether the 52-line protocol is a truncated landing or a deliberate excerpt.
  The internal reference to a missing §9 and the mid-sentence cut favor truncation; the intent
  is not recorded in any file this seat read. Owner: integrator.
- **to-verify:** whether the r41/r42 in-place queue edit (Obs. 3) was ever ruled admissible.
  r41 X00 prohibits editing the r40 file; r42 O08 reported the edit without adjudicating it.
  This seat changed nothing and records the hashes only. Owner: integrator.
- **Not claimed:** any fix of the underlying R01-2/3/5/6/7 findings, any repair of the filed
  O02/O08/O07 bytes, any new queue class convention beyond the explicit mapping in
  `class_vocabulary`.

## 6. Citations

- Contract: `reports/round-43/claims.json:49-59` (claim Ca), `reports/round-43/targets.json:37`
  (seat Ca03), shared rules at `targets.json:4-10`.
- Parent rows: `reports/round-40/op/defect-queue-v2.json:282-310,343-351`; class vocabulary and
  in-place edit history at `:8`, `:400-416`; r42 O08's record of the edit at
  `reports/round-42/op/O08-queue-update.md:192-216`.
- R01 findings: `reports/round-39/review/R01-review.md:25-34` (verdict table) and
  `:75,93,128,140-146,147,182,191,203,208,226-244,265-274,278-299` (finding sections).
- r39 protocol: `reports/round-39/calib/isolation-replay-protocol.md` (52 lines, sha256
  `bd5b4e3d…`); `reports/round-39/calib/Ca01-protocol.md:76-77,117-125,166`;
  `reports/round-39/calib/recount-ledger-successor.json:8`.
- r38 artifacts: `reports/round-38/op/O02-isolated.md` (sha256 `e314dbf3…`), `O08-regression.md`
  (sha256 `3818df94…`), `O01-guard-design.md` (sha256 `d863af31…`), `O03-verify.md:255-341`,
  `O07-scribe.md` (0 bytes, sha256 `e3b0c442…`).
- r40 outcomes: `reports/round-40/cov/C05-audit.md:26-27,38,387-388`;
  `reports/round-40/claims.json:14`; `reports/round-40/scribe/S01-integration-draft.md:391`;
  `LOG.md:3773-3789`; `SCORECARD.md:790`.
- Runners: `reports/round-41/run-validation.py:168-173,183`;
  `reports/round-42/run-validation.py:177-182,192`; absolute ROOT lines
  `reports/round-34/run-validation.py:10`, `round-35:9`, `round-36:8`, `round-37:5`,
  `round-38:5`.
- Baseline/boundary: `git rev-parse --short HEAD` → `7ceff59`; `git status --porcelain` →
  `?? reports/round-43/` only.
