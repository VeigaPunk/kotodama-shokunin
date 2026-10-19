- Seat: Ca01 | executor | claim Ca | date 2026-10-19 | baseline `7ceff59` | HEAD `7ceff59`
- Out path: `reports/round-43/calib/Ca01-dispositions.md` (this file is the only write)
- Contract: `reports/round-43/claims.json:49-59` (claim Ca); mission `reports/round-43/targets.json` seat Ca01
- Filed-byte edits: **none**. No `reports/round-*/run-validation.py` executed. No corpus staging.

# Ca01 — per-finding dispositions for the four carried r38/r39 rows

## 0. What this pass does

The four named rows (`r39-review-findings-disposition`, `r38-O02-fragment-defects`,
`r38-O08-fragment-defect`, `r38-O07-empty-fragment`) assert defects, an empty fragment, or a
missing disposition, but carry no per-finding disposition on record. This pass re-reads each
cited evidence artifact at HEAD and re-runs every measuring command that still has a durable
subject. Each finding lands one of the claim's four classes:

`fixed-with-evidence` | `routed-with-owner` | `recorded` | `could-not-recover`

A class is assigned from measured bytes, not from the row's prose. Two rows changed meaning
under re-measurement: the O02 row's three quoted defects **do not reproduce** against the filed
O02 bytes, and most R01-8…R01-14 findings **were already recorded** in the filed r39 C05 audit
(the queue row's "unrecorded" premise is only true for R01-2/3/5/6/7).

Vocabulary note: this is the defect-queue's four-class vocabulary (`reports/round-43/claims.json:49-59`), not
`corpus/knowledge/synthesis/finding-disposition-workflow.md`'s design-defect classes. The
corpus entry's rule that a disposition is a record and never a clearance is followed: nothing
here admits a round or clears a defect.

## 1. Evidence bundle (all commands run 2026-10-19 at HEAD `7ceff59`, lane root)

Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. `git status --porcelain`
before and after → `?? reports/round-43/` only.

| # | command | measured output |
|---|---|---|
| E1 | `wc -c reports/round-38/op/O07-scribe.md` | `0` |
| E1 | `sha256sum reports/round-38/op/O07-scribe.md` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty-file digest) |
| E2 | `git show dfb0719:reports/round-38/op/O02-isolated.md \| sha256sum` | `e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d` |
| E2 | `sha256sum reports/round-38/op/O02-isolated.md` | `e314dbf3…` (identical — the filed blob equals the commit blob; no post-filing edit) |
| E3 | `grep -Fn "plus 44 controls" reports/round-38/op/O02-isolated.md` | no match (exit 1) |
| E3 | `grep -Fn "green and names nothing" reports/round-38/op/O02-isolated.md` | no match (exit 1) |
| E3 | `grep -Fn "does not match the frozen packet digest" reports/round-38/op/O02-isolated.md` | no match (exit 1) |
| E4 | `grep -Fn "plus 45 controls" reports/round-38/op/O02-isolated.md` | hit at `:62` and `:203` (also `:20`) |
| E4 | `grep -Fn "m15b in-sync roster green" reports/round-38/op/O02-isolated.md` | hit at `:62` and `:203` |
| E4 | `grep -Fn "v3_verify_component_digests" reports/round-38/op/O02-isolated.md` | hit at `:161` |
| E5 | `grep -Fn "is exactly the digest O01" reports/round-38/op/O08-regression.md` | hit at `:83` |
| E5 | `grep -Fn "e581275129eb" reports/round-38/op/O01-guard-design.md` | hit at `:144` and `:309` |
| E5 | `grep -Fc "ae22013b5ddd77aa1b598cef1f5a57f0fb76bfc6eb8541d56e180fe70abcf6c2" reports/round-38/op/O08-regression.md` | `2` (`:80`, `:241`) |
| E6 | `wc -c reports/round-39/calib/isolation-replay-protocol.md` | `2829`; sha256 `bd5b4e3d695ae5c7532b6d10dc076f1bbf9051a378ee2c88607e9110079b6b81` |
| E6 | `grep -c '^## ' reports/round-39/calib/isolation-replay-protocol.md` | `3` (§1, §2, §3 heading — the file ends at the `## 3. Step 0` heading) |
| E6 | `grep -n 'rounds 34' …isolation-replay-protocol.md` | `:10` — "Legacy runners (rounds 34, 35, 36)" |
| E7 | `grep -n 'ROOT = ' reports/round-{33,34,35,36,37,38}/run-validation.py` | r33 `:23` relative (`parents[2]`); r34 `:10`, r35 `:9`, r36 `:8`, r37 `:5`, r38 `:5` all absolute `/home/vgpnk/Projects/shokunin/kotodama-shokunin` — **five** absolute runners |
| E8 | `grep -n 'single physical line' reports/round-39/calib/basename-couples-policy.md` | `:16` |
| E8 | `grep -c 'to-verify' …/basename-couples-policy.md` | `0` |
| E8 | `grep -c 'phonology-sanity' …/basename-couples-policy.md` | `0` |
| E9 | `sed -n '70,78p' corpus/knowledge/linguistics/phonetics-phonology.md` | wrapped `- couples:` field; four named targets: `sound-change.md`, `tone-prosody.md`, `sound-symbolism.md`, `writing-systems.md` |
| E9 | existence check of those four | `sound-symbolism.md` exists, `writing-systems.md` exists, `sound-change.md` absent, `tone-prosody.md` absent |
| E10 | `grep -rli 'taboo' corpus/knowledge/verification/*.md \| wc -l` | `11` at HEAD (24 verification files) |
| E11 | `ls -l reports/round-39/cov/C05-audit.md`; `grep -n '4/4 PASS'` | 28,221 bytes; `:46` "**4/4 PASS** the round-35/36 structural contract" |
| E12 | `grep -n 'R01-1 ruling folded' reports/round-39/calib/recount-ledger-successor.json` | `:8`; Ca02 mechanism at `Ca02-replay-verify.md:31,122` (`ROOT = os.getcwd()`) |
| E13 | `grep -rn 'min_bytes\|min-bytes\|MIN_BYTES' reports/round-4[0-2]/run-validation.py tools/harness/` | exit 1 — no durable min-bytes check |
| E14 | `ls corpus/knowledge/myth-symbol/*.md \| wc -l`; `find corpus/knowledge -name '*.md' \| wc -l` | `26`; `223` |

Citation convention: a bare basename (`O01-guard-design.md`, `defect-queue-v2.json`, …) is
shorthand for the full path first given in this file; every bare basename remaining after the
two explicit r39 paths below resolves uniquely under `find reports corpus -name <basename>`.
Artifact digests cited below (sha256): `reports/round-40/op/defect-queue-v2.json`
`dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`;
`reports/round-39/review/R01-review.md` `4fe294ae213a353d504555228d2dd93005558f90364bfe4dc5f59cfa1339dfde`;
`reports/round-39/cov/C05-audit.md` `e5f3b5852dfb453d8b8f7ab48069f53d0e696a1cb2ac753c02071c6755c9801f`;
`recount-ledger-successor.json` `64b93cfd023814ddf6097c23396d9a02ec4f9f161e908cf171235af0ca7d2c17`;
`basename-couples-policy.md` `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`;
`O01-guard-design.md` `d863af319395a4df6a32b6ac1f6956e7cb637c8bdcee0b46dab5401d08d458d0`;
`O03-verify.md` `cc24b79ce545d405a9076c255c45db5074648bb265b28ea2a8f787af5a5f3267`;
`O02-isolated.md` `e314dbf3…`; `O07-scribe.md` `e3b0c442…`; `O08-regression.md`
`3818df945e4a1850d34e7147d4d4b9c4255adabf5f3cff8578e6fd33dc4b2539`.

## 2. Disposition summary

| named row | row class | owner | one-line result |
|---|---|---|---|
| `r39-review-findings-disposition` | **fixed-with-evidence** | integrator (apply this successor record) | all 14 numbered findings + the unnumbered minor dispositioned below; 1 fixed, 8 recorded, 5 routed, 1 could-not-recover |
| `r38-O02-fragment-defects` | **could-not-recover** | integrator correction record | the three quoted defects are absent from the filed O02 bytes; the cited quotes cannot be recovered in any durable artifact |
| `r38-O08-fragment-defect` | **recorded** | integrator correction record | D-4 reproduces; corrected attribution supplied; filed bytes untouched |
| `r38-O07-empty-fragment` | **recorded** | integrator (record); r44 runner work (prevention) | 0 bytes re-measured; prevention leg has no durable instrument and is routed |

Sub-leg counts (a row can carry more than one leg): `fixed-with-evidence` 1,
`recorded` 8, `routed-with-owner` 6, `could-not-recover` 5. Zero findings dropped.

## 3. `r38-O02-fragment-defects` → could-not-recover (three sub-findings)

The row (`defect-queue-v2.json:282-291`) cites `reports/round-38/op/O03-verify.md:255-306`
for D-1…D-3. Each quoted defect was tested with a fixed-string grep against the filed O02
artifact. None of the three quoted strings exists, and the filed blob digest equals the
`dfb0719` commit blob digest, so this is not a later repair: the artifact O03 says it measured
is not the artifact that was filed.

### D-1 — quoted selftest count `44`

- O03 `:257-270` quotes O02 §2 as recording `plus 44 controls` on both the 58- and 59-member
  builds.
- Filed O02 says **45** at `:20`, `:62`, `:203`; `grep -Fn "plus 44 controls"` → exit 1.
- O01 §6.1 also reports 45 (`O01-guard-design.md:90,253,302`). The arithmetic in the filed
  artifact is correct.
- **Class: `could-not-recover`.** The quoted 44 cannot be recovered from filed bytes; the
  intermediate draft O03 read is not durable (`.scratch/o02/` holds build scripts, not a
  pinned fragment). Owner: integrator correction record. Action: correct the queue row — do
  not file a correction against O02, which already carries the right number.

### D-2 — quoted `m15b` description "names nothing"

- O03 `:272-286` quotes O02 §2 as describing the in-sync control as "the `manifest-roster`
  leg is green and names nothing".
- Filed O02 `:62` says `m15b in-sync roster green …`; `:203` repeats it.
  `grep -Fn "green and names nothing"` → exit 1. The only "names nothing" in O02 is `:99`,
  and it describes the **G7 rendered-text guard**, which is correctly vacuous.
- O01's landed assertion is green-and-names-the-member (`O01-guard-design.md:228`).
- **Class: `could-not-recover`.** Same owner/action as D-1.

### D-3 — quoted tamper prediction naming the frozen-packet leg

- O03 `:288-306` quotes O02 §7 as predicting
  `E2E-DIGEST: the assembled packet does not match the frozen packet digest`.
- That string does not exist in filed O02 (`grep -Fn` → exit 1). Filed O02 §7 `:160-166`
  already says the **opposite and correct** mechanism: "a mutated 13th component reds
  `E2E-DIGEST` with or without the read-set expansion (O05 §4, R02 Finding 6)" and cites
  `v3_verify_component_digests` at `:2208-2222` (`:161`).
- **Class: `could-not-recover`.** Same owner/action as D-1.

Row note (honesty): O03's conclusions elsewhere stand and its D-4 reproduces (§4). The
defect is in the **queue row's evidence citation**, not in O02. This disposition does not
edit O03 or O02; it files the correction as a new successor record.

## 4. `r38-O08-fragment-defect` → recorded (D-4 reproduces)

- Claim: O08 §1/§8 says its patched digest `ae22013b5ddd77aa…` "is exactly the digest O01 §6
  declares" (`O08-regression.md:83`; repeated at `:241`).
- Filed O01 declares `e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553`
  (`O01-guard-design.md:144` and `:309`).
- The two values differ. O03's diff (`O03-verify.md:319-328`) shows one hunk, the `m15b`
  result string, so `ae22013b…` is O08's own variant of O01's patch.
- O08's readings stand (same functional tree); only the provenance sentence is wrong.
- **Class: `recorded`.** Filed bytes are immutable and the correction is now on record here.
  Owner: integrator correction record. Corrected text to carry forward: "`ae22013b…` is
  O08's own `m15b`-string variant of O01 §6's patch; O01 declares `e5812751…`. The two are
  functionally equivalent for the claim's thresholds; they are not the same artifact."

## 5. `r38-O07-empty-fragment` → recorded (prevention leg routed)

- Record leg: `wc -c reports/round-38/op/O07-scribe.md` → `0`; sha256 `e3b0c442…` (the empty
  file digest). Filed bytes immutable. **Class: `recorded`** with a cited command.
- Prevention leg: the row's next_touch is "a non-empty check on every declared out path".
  No durable instrument implements it: `grep -rn 'min_bytes\|min-bytes\|MIN_BYTES'` over
  `reports/round-4[0-2]/run-validation.py` and `tools/harness/` → exit 1. The r40 integration
  draft's CO4 check (`reports/round-40/scribe/S01-integration-draft.md:391`) was a per-round
  manual census, not a durable check. **Class: `routed-with-owner`** — owner r44 runner /
  round-runner-template work (`templates/round-runner-template.py`), action: add a min-bytes
  assertion to the declared-out-path census. This is prevention debt, not a reopening of the
  immutable r38 fragment.

## 6. `r39-review-findings-disposition` → fixed-with-evidence (this successor record)

The queue row (`defect-queue-v2.json:343-350`) says R01-2…R01-14 have no individual
disposition: `grep -c 'R01-' reports/round-39/validation.json` → `0` (re-verified this seat).
That part is true. It is also **partly stale**: the filed r39 C05 audit already folds
R01-8…R01-14 as carried notes at `reports/round-39/cov/C05-audit.md:169-180`, and R01-4 closed when C05 landed.
Per-finding dispositions:

| finding | subject (R01-review.md) | class | owner | evidence / next action |
|---|---|---|---|---|
| R01-1 | replay mechanism altered executed bytes; ruling required | **recorded** (residual leg **routed**) | integrator / protocol successor | Ledger note `recount-ledger-successor.json:8` names the mechanism and folds the ruling; Ca02 states the actual adaptation `ROOT = os.getcwd()` (`Ca02-replay-verify.md:31,122`). Residual: R01's alternative required the ruling **in the protocol text** (`reports/round-39/review/R01-review.md:241-244`); the canonical protocol has no such section (E6). Routed to the protocol successor. |
| R01-2 | protocol names 3 absolute runners, measured 5 | **routed-with-owner** | integrator / protocol successor | `isolation-replay-protocol.md:10` names rounds 34/35/36 only; r37 `:5` and r38 `:5` are also absolute (E7). Action: amend §1 to name r34–r38 (or scope to "any runner with an absolute ROOT"). |
| R01-3 | Tier B has no discriminating wrong-tree observable | **routed-with-owner** | integrator / protocol successor | Canonical protocol is truncated at `## 3` (2,829 B, 3 H2 sections, E6), so the mandatory post-run tree-discriminator does not exist in the filed copy. Action: add it to Tiers A and B before the protocol is relied on. |
| R01-4 | C05 audit absent at R01 close; claim C threshold unmet | **fixed-with-evidence** | C05 seat / integrator | `reports/round-39/cov/C05-audit.md` exists (28,221 B) and reads **4/4 PASS** at `:46`; r39 `validation.json` acceptance `true`. |
| R01-5 | Tier A substrate is a shared clone, not a worktree | **routed-with-owner** | integrator (record) | Rationale is in `Ca01-protocol.md:111-130`; no r39 record carries the declared deviation: `grep -c 'clone' reports/round-39/validation.json` → `0`, and the r39 LOG entry is silent. Action: record the deviation with A.0 as rationale. |
| R01-6 | `or True` vacuous assert + three line nits | **routed-with-owner** | integrator / protocol successor | `Ca01-protocol.md:166` carries `… or True`; the canonical copy is truncated before §5, so nothing was applied. Action: tighten or delete the line and fix the r34/r35/r36 line numbers in the same amendment. |
| R01-7 | D1 wrapped couples field; D2 blocker/`(to-verify` mapping + phantom second carrier | **routed-with-owner** | r43 claim O (D1 instrument) + policy successor (D1 text, D2) | Policy still says "single physical line" (`basename-couples-policy.md:16`; the r42 full successor repeats it at `:16`). The wrapped field is `phonetics-phonology.md:72-77` with four named targets, two of which exist (E9) — the r43 O instrument implements block reading but the policy text must follow. D2: `grep -c 'to-verify'` in both policy docs → 0; the r42 full doc names only one phantom carrier (`basename-couples-policy-full.md:232-235`, `label-channel-routing-verification.md:14`), not `synthesis/typed-label-routing-workflow.md:16`. |
| R01-8 | C02's inline regex replication labelled as the filed instrument | **recorded** | C02 / integrator | `reports/round-39/cov/C05-audit.md:169-174` folds it with the exact `HEADER_RE` mismatch; conclusions unaffected. No action blocks. |
| R01-9 | C04 self-audit pins the pre-reword staged size | **recorded** | C04 / integrator | `reports/round-39/cov/C05-audit.md:165` (F5) records 24,277 B vs 24,296/24,297 B and the intact C06 whole-fragment pin. |
| R01-10 | fence-shape heterogeneity (4-backtick vs 3-backtick) | **recorded** | integrator (staging) | `reports/round-39/cov/C05-audit.md:175-176`; the r39 landing staged both shapes (4/4 PASS), so the note is carried, not a live defect. |
| R01-11 | C01 has no head-block `- calibration:` field | **recorded** | C01 / integrator | `reports/round-39/cov/C05-audit.md:176-177`; executable bar unaffected. |
| R01-12 | K01's term counts use a flag that prints filenames; taboo 9 vs 10 | **recorded** | K01 / integrator | `reports/round-39/cov/C05-audit.md:177-179` re-measured 10 at the 20-file pre-landing partition. At HEAD the count is **11** over 24 files: the four r39 verification landings added `worked-example-verification.md`, which carries one taboo mention (`grep -ci taboo` → 1). 10 + 1 = 11 is consistent, not a new defect. Conclusion ("no dedicated taboo entry") stands. |
| R01-13 | K01's G2–G4 gaps remain unallocated | **recorded** | lane planner / coverage rounds | `reports/round-39/cov/C05-audit.md:179-180` carries them as gaps, not defects. |
| R01-14 | reviewer-side +2 sweep anomaly, no durable artifact | **could-not-recover** | integrator | `reports/round-39/review/R01-review.md:292-299` self-files it against no seat; `reports/round-39/cov/C05-audit.md:150-153` records `to-verify` and could not reproduce any extra-file state. No durable handle exists. |
| (minor, unnumbered) | negative control wrote one scratch probe into the live `.scratch` | **recorded** | Ca01 protocol successor | `reports/round-39/review/R01-review.md:245-247`; bounded side effect, already declared. Action: name it in the protocol's escape-demonstration section. |

Meta-row disposition: **`fixed-with-evidence`** — the missing per-finding list now exists as
this successor record; the filing action is the integrator's application of the fenced JSON in
§8. Residual debt is explicit: R01-2/3/5/6/7 and the R01-1 protocol-text leg remain routed.

## 7. Cross-claim collision alert (not this seat's claim; reported, not routed around)

Claim C's `before` states the lithic slot is "named but unbuilt", targeting myth-symbol
26 → 27. At HEAD the slot is **already built**:

- `ls corpus/knowledge/myth-symbol/*.md | wc -l` → `26`, and the listing includes
  `mineral-stone-symbolism.md`.
- `git log --oneline -1 -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` →
  `7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol
  entries, collision ruling + overwrite restore`.
- `git show --stat 7ceff59` lists `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md |
  192 +` (sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`).
- The r42 spare's own header (`reports/round-42/cov/C01-mineral-spare.md:1`) says C01 and C04
  authored the same lithic topic; **C04 landed; this draft is the named spare**.
- Therefore landing the spare under `myth-symbol/` either overwrites the existing lithic entry
  (forbidden) or creates a second lithic register while still raising the count to 27. The
  claim's "completing the named lapidary slot" premise is false at `7ceff59`.
- Action for the C seats/integrator: adjudicate before any bytes move; this seat does not
  choose a filename or route around the collision. The C06 collision verifier has the same
  live partition to check.

## 8. Fenced draft — `reports/round-43/calib/dispositions-r38-r39.json`

The integrator files this as a **new** artifact. It edits no filed byte and does not rewrite
`reports/round-40/op/defect-queue-v2.json` (sha256 pinned in `source.parent_sha256`).

```json
{
  "schema": "kotodama-finding-dispositions-v1",
  "round": 43,
  "date": "2026-10-19",
  "kind": "successor",
  "baseline_commit": "7ceff59",
  "head_at_measurement": "7ceff59",
  "source": {
    "parent_rows": "reports/round-40/op/defect-queue-v2.json",
    "parent_sha256": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
    "review": "reports/round-39/review/R01-review.md",
    "review_sha256": "4fe294ae213a353d504555228d2dd93005558f90364bfe4dc5f59cfa1339dfde",
    "audit": "reports/round-39/cov/C05-audit.md",
    "audit_sha256": "e5f3b5852dfb453d8b8f7ab48069f53d0e696a1cb2ac753c02071c6755c9801f"
  },
  "class_vocabulary": [
    "fixed-with-evidence",
    "routed-with-owner",
    "recorded",
    "could-not-recover"
  ],
  "constraints": {
    "filed_bytes_edited": false,
    "runner_executed": false,
    "corpus_staged": false,
    "writes": ["reports/round-43/calib/Ca01-dispositions.md"]
  },
  "rows": [
    {
      "id": "r38-O02-fragment-defects",
      "parent_row": "reports/round-40/op/defect-queue-v2.json:282-291",
      "class": "could-not-recover",
      "owner": "integrator correction record",
      "reason": "the three defects O03 quotes do not exist in the filed O02 artifact; the quoted intermediate draft is not durable",
      "evidence": [
        "reports/round-38/op/O02-isolated.md sha256 e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d",
        "git show dfb0719:reports/round-38/op/O02-isolated.md sha256 e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d",
        "grep -Fn 'plus 44 controls' -> no match (exit 1)",
        "grep -Fn 'green and names nothing' -> no match (exit 1)",
        "grep -Fn 'does not match the frozen packet digest' -> no match (exit 1)",
        "filed O02:62,:203 read 'plus 45 controls' and 'm15b in-sync roster green'",
        "reports/round-38/op/O03-verify.md:255-306"
      ],
      "findings": [
        {
          "fid": "D-1",
          "class": "could-not-recover",
          "claim": "O02 records 'plus 44 controls'; the artifact yields 45",
          "measured": "filed O02:20,:62,:203 record 45; the string 'plus 44 controls' is absent",
          "action": "correct the queue row; no correction row against O02 is owed"
        },
        {
          "fid": "D-2",
          "class": "could-not-recover",
          "claim": "O02 describes m15b as green and 'names nothing'",
          "measured": "filed O02:62 records 'm15b in-sync roster green'; O01:228 asserts the member is named",
          "action": "correct the queue row; no correction row against O02 is owed"
        },
        {
          "fid": "D-3",
          "class": "could-not-recover",
          "claim": "O02 predicts the assembled-vs-frozen leg fires",
          "measured": "filed O02:160-166 names v3_verify_component_digests (:161) as the firing leg; the quoted prediction string is absent",
          "action": "correct the queue row; no correction row against O02 is owed"
        }
      ]
    },
    {
      "id": "r38-O08-fragment-defect",
      "parent_row": "reports/round-40/op/defect-queue-v2.json:292-301",
      "class": "recorded",
      "owner": "integrator correction record",
      "reason": "D-4 reproduces: O08's ae22013b... is its own m15b-string variant, not O01's declared e5812751...",
      "evidence": [
        "reports/round-38/op/O08-regression.md:83,:241 (the false identity claim)",
        "reports/round-38/op/O01-guard-design.md:144,:309 (e581275129eb...)",
        "reports/round-38/op/O03-verify.md:308-341 (one-hunk diff)",
        "sha256 reports/round-38/op/O08-regression.md 3818df945e4a1850d34e7147d4d4b9c4255adabf5f3cff8578e6fd33dc4b2539"
      ],
      "corrected_attribution": "ae22013b5ddd77aa1b598cef1f5a57f0fb76bfc6eb8541d56e180fe70abcf6c2 is O08's own m15b-string variant of O01 section 6's patch; O01 declares e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553. Functionally equivalent for the claim's thresholds; not the same artifact.",
      "filed_bytes_edited": false
    },
    {
      "id": "r38-O07-empty-fragment",
      "parent_row": "reports/round-40/op/defect-queue-v2.json:302-311",
      "class": "recorded",
      "owner": "integrator (record); r44 runner work (prevention)",
      "reason": "the fragment is 0 bytes; the prevention leg has no durable instrument",
      "evidence": [
        "wc -c reports/round-38/op/O07-scribe.md -> 0",
        "sha256 reports/round-38/op/O07-scribe.md -> e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "grep -rn 'min_bytes|min-bytes|MIN_BYTES' reports/round-4[0-2]/run-validation.py tools/harness/ -> exit 1"
      ],
      "legs": [
        {
          "leg": "record",
          "class": "recorded",
          "action": "none; filed bytes immutable"
        },
        {
          "leg": "prevention",
          "class": "routed-with-owner",
          "owner": "r44 runner / templates/round-runner-template.py",
          "action": "add a min-bytes assertion to the declared-out-path census"
        }
      ]
    },
    {
      "id": "r39-review-findings-disposition",
      "parent_row": "reports/round-40/op/defect-queue-v2.json:343-352",
      "class": "fixed-with-evidence",
      "owner": "integrator (apply this successor record)",
      "reason": "the missing per-finding list now exists; 14 numbered findings plus one unnumbered minor are dispositioned",
      "evidence": [
        "grep -c 'R01-' reports/round-39/validation.json -> 0 (the original defect)",
        "reports/round-39/cov/C05-audit.md:150-180 (R01-4 and R01-8..R01-14 already folded)",
        "reports/round-39/calib/recount-ledger-successor.json:8 (R01-1 ruling)"
      ],
      "findings": [
        {
          "fid": "R01-1",
          "class": "recorded",
          "owner": "integrator",
          "evidence": "recount-ledger-successor.json:8; Ca02-replay-verify.md:31,:122",
          "residual": {
            "class": "routed-with-owner",
            "owner": "protocol successor",
            "action": "write the adapted-copy ruling into the protocol text, not only the ledger"
          }
        },
        {
          "fid": "R01-2",
          "class": "routed-with-owner",
          "owner": "integrator / protocol successor",
          "evidence": "isolation-replay-protocol.md:10 names 34/35/36; r37:5 and r38:5 are also absolute",
          "action": "name all five absolute runners or scope to the absolute-ROOT class"
        },
        {
          "fid": "R01-3",
          "class": "routed-with-owner",
          "owner": "integrator / protocol successor",
          "evidence": "canonical protocol 2829 B, 3 H2 sections, ends at '## 3. Step 0'",
          "action": "add the mandatory post-run tree-discriminator to Tiers A and B"
        },
        {
          "fid": "R01-4",
          "class": "fixed-with-evidence",
          "owner": "C05 seat / integrator",
          "evidence": "reports/round-39/cov/C05-audit.md 28221 B; :46 '4/4 PASS'; r39 validation acceptance true"
        },
        {
          "fid": "R01-5",
          "class": "routed-with-owner",
          "owner": "integrator",
          "evidence": "Ca01-protocol.md:111-130; grep -c clone reports/round-39/validation.json -> 0",
          "action": "record the clone-vs-worktree substrate as a declared deviation with A.0"
        },
        {
          "fid": "R01-6",
          "class": "routed-with-owner",
          "owner": "integrator / protocol successor",
          "evidence": "Ca01-protocol.md:166 'or True'; line nits per R01-review.md:208-212",
          "action": "tighten or delete the vacuous assert and fix the three line numbers"
        },
        {
          "fid": "R01-7",
          "class": "routed-with-owner",
          "owner": "r43 claim O (D1 instrument) + policy successor (D1 text, D2)",
          "evidence": [
            "basename-couples-policy.md:16 and basename-couples-policy-full.md:16 still say 'single physical line'",
            "corpus/knowledge/linguistics/phonetics-phonology.md:72-77 (wrapped field, 4 named targets)",
            "grep -c to-verify in both policy docs -> 0",
            "basename-couples-policy-full.md:232-235 names one phantom carrier only"
          ],
          "action": "amend the policy to read wrapped continuation lines; add the blocker/(to-verify mapping and the second phantom carrier"
        },
        {
          "fid": "R01-8",
          "class": "recorded",
          "owner": "C02 / integrator",
          "evidence": "C05-audit.md:169-174"
        },
        {
          "fid": "R01-9",
          "class": "recorded",
          "owner": "C04 / integrator",
          "evidence": "C05-audit.md:165 (F5)"
        },
        {
          "fid": "R01-10",
          "class": "recorded",
          "owner": "integrator (staging)",
          "evidence": "C05-audit.md:175-176; r39 landing 4/4 PASS"
        },
        {
          "fid": "R01-11",
          "class": "recorded",
          "owner": "C01 / integrator",
          "evidence": "C05-audit.md:176-177"
        },
        {
          "fid": "R01-12",
          "class": "recorded",
          "owner": "K01 / integrator",
          "evidence": "C05-audit.md:177-179; HEAD re-measure 11 over 24 files = 10 + the r39 worked-example entry's single taboo mention",
          "head_recheck": 11
        },
        {
          "fid": "R01-13",
          "class": "recorded",
          "owner": "lane planner / coverage rounds",
          "evidence": "C05-audit.md:179-180"
        },
        {
          "fid": "R01-14",
          "class": "could-not-recover",
          "owner": "integrator",
          "evidence": "R01-review.md:292-299; C05-audit.md:150-153; no durable artifact or attribution"
        },
        {
          "fid": "R01-minor",
          "class": "recorded",
          "owner": "protocol successor",
          "evidence": "R01-review.md:245-247",
          "action": "name the bounded .scratch side effect in the escape-demonstration section"
        }
      ]
    }
  ],
  "counts": {
    "named_rows": 4,
    "row_classes": {
      "fixed-with-evidence": 1,
      "recorded": 2,
      "routed-with-owner": 0,
      "could-not-recover": 1
    },
    "sub_legs_total": 22,
    "sub_leg_classes": {
      "fixed-with-evidence": 1,
      "recorded": 10,
      "routed-with-owner": 7,
      "could-not-recover": 4
    },
    "findings_dispositioned": 19,
    "findings_dropped": 0
  },
  "queue_successor_entries": [
    {
      "parent_id": "r38-O02-fragment-defects",
      "successor_class": "could-not-recover",
      "owner": "integrator correction record",
      "correction": "D-1/D-2/D-3 do not reproduce in filed O02 (e314dbf3...); filed O02 already carries 45 controls, m15b green, and the component-digest mechanism. The quoted defects are unrecoverable intermediate-draft readings. No correction row against O02 is owed."
    },
    {
      "parent_id": "r38-O08-fragment-defect",
      "successor_class": "recorded",
      "owner": "integrator correction record",
      "correction": "D-4 stands. ae22013b... is O08's m15b-string variant; O01 declares e5812751... Corrected attribution filed."
    },
    {
      "parent_id": "r38-O07-empty-fragment",
      "successor_class": "recorded",
      "owner": "integrator (record); r44 runner work (prevention)",
      "correction": "0-byte fragment remains immutable and recorded. Prevention leg (min-bytes census check) is unlanded and routed to r44."
    },
    {
      "parent_id": "r39-review-findings-disposition",
      "successor_class": "fixed-with-evidence",
      "owner": "integrator (apply)",
      "correction": "Per-finding dispositions filed in reports/round-43/calib/dispositions-r38-r39.json. Remaining routed legs: R01-1 protocol-text, R01-2, R01-3, R01-5, R01-6, R01-7."
    }
  ],
  "limits": [
    "O03's D-1/D-2/D-3 quotes cannot be traced to any durable artifact; this pass does not assert what O03 saw, only what the filed bytes contain.",
    "R01-12's original 10 was measured over the 20-file pre-landing verification partition; the HEAD reading of 11 is not a contradiction and is not a new defect.",
    "The r42 lithic collision (section 7 of Ca01-dispositions.md) is outside claim Ca and is reported for the C seats; no filename was chosen and no byte was staged."
  ]
}
```

## 9. Integration notes

1. File the fenced JSON above as `reports/round-43/calib/dispositions-r38-r39.json`
   (new artifact; sha256 to be recorded by the integrator after write).
2. Append the four `queue_successor_entries` to the r43 queue successor file — **never** edit
   `reports/round-40/op/defect-queue-v2.json`. The parent sha256 is pinned in the JSON.
3. No corpus bytes move for this claim. The only corpus-adjacent observation is the §7
   collision alert, which belongs to claim C.
4. The three `routed-with-owner` protocol legs (R01-2/3/6) and the R01-1 residual should be
   carried into the next protocol amendment; they are not silently closed here.

## 10. Limits / `to-verify`

- `to-verify`: whether O02 or O08 were amended between their authoring mtimes and the
  `dfb0719` commit. The commit blob equals the worktree blob for O02, so no post-filing edit
  is detectable; the pre-filing history is not in git (single admit commit) and is reported as
  unrecoverable, not inferred.
- `to-verify`: the exact command K01 used for the taboo count. This pass re-ran
  `grep -rli 'taboo' corpus/knowledge/verification/*.md | wc -l` and reports the measured 11
  with the file list, not K01's flag semantics.
- No claim of closure: this is a disposition record, not an admission verdict. The four
  `routed-with-owner` legs remain open by construction (`corpus/knowledge/verification/finding-disposition-workflow.md` §5: a disposition is not clearance).
