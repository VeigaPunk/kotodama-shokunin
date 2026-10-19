- Seat: Ca02 | verifier | claim Ca | date 2026-10-19 | baseline `7ceff59` | HEAD `7ceff59`
- Out path: `reports/round-43/calib/Ca02-verify.md` (this file is this seat's only write)
- Contract: `reports/round-43/claims.json:49-59` (claim Ca); mission `reports/round-43/targets.json` seat Ca02
- Subject: `reports/round-43/calib/Ca01-dispositions.md` (v2 sha256 `2ebbcd0abe624f137286d14b73e5a2a8425d64b5b90ae7c3a3b6b2c7bd3f727b`, 33 409 B, mtime 14:00:23; an earlier 32 807 B revision was re-read after the mid-verification update and every finding below persists in v2), cross-checked against `reports/round-43/calib/Ca03-queue-update.md`
- Method: every row re-measured from filed bytes at HEAD; Ca01's numbers were **not** used as inputs. No `reports/round-*/run-validation.py` executed. `git status --porcelain` before/after → `?? reports/round-43/` only.
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, lane root, 2026-10-19.

# Ca02 — independent verification of the per-finding dispositions

## 0. Verdict at a glance

| named row | Ca01 class | Ca02 verdict | delta |
|---|---|---|---|
| `r38-O07-empty-fragment` | `recorded` (+ prevention `routed-with-owner`) | **AGREE** | none; Ca03's runner evidence strengthens the prevention leg |
| `r38-O08-fragment-defect` | `recorded` | **AGREE** | none; digest citations reproduce exactly |
| `r38-O02-fragment-defects` | `could-not-recover` (all three) | **PARTIAL DISAGREE** | D-1/D-2 agree `could-not-recover`; **D-3 must be `recorded`** — a weaker form survives at `O02:164` |
| `r39-review-findings-disposition` | `fixed-with-evidence` | **AGREE ON CLASS, 2 SUB-CLASSES DISAGREE** | R01-13 is `fixed-with-evidence` (r40), not `recorded`; R01-4's evidence is the r39 audit, not Ca03's r40 audit |

No row is silently dropped. Two rows agree unchanged, one is partially wrong, one carries two
sub-class errors and one stale count line. The corrections are all in the **disposition record**,
not in filed bytes; nothing here reopens a filed artifact.

## 1. Independent measurement bundle

| # | command | output (2026-10-19, HEAD `7ceff59`) |
|---|---|---|
| M1 | `wc -c reports/round-38/op/O07-scribe.md` | `0` |
| M1 | `sha256sum reports/round-38/op/O07-scribe.md` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty-file digest) |
| M2 | `sha256sum reports/round-38/op/O02-isolated.md` | `e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d` |
| M2 | `git show dfb0719:reports/round-38/op/O02-isolated.md \| sha256sum` | `e314dbf3…` (identical — no post-filing edit) |
| M2 | `grep -Fn "plus 44 controls" O02` | no match, exit 1 |
| M2 | `grep -Fn "green and names nothing" O02` | no match, exit 1 |
| M2 | `grep -Fn "does not match the frozen packet digest" O02` | no match, exit 1 |
| M2 | `grep -Fn "plus 45 controls" O02` | hits `:20`, `:62`, `:203` |
| M2 | `grep -n "assembled-vs-frozen" O02` | `:164` — *"it surfaces through the assembled-vs-frozen packet compare (`:3951-3957`)"* |
| M2 | `grep -c "58-member" O02` | `0` |
| M3 | `grep -Fn "is exactly the digest O01" reports/round-38/op/O08-regression.md` | `:83` |
| M3 | `grep -Fn "e581275129eb" reports/round-38/op/O01-guard-design.md` | `:144`, `:309` |
| M3 | `grep -Fc "ae22013b5ddd77aa…" O08` | `2` (`:80`, `:241`); narrative repeats at `:18`, `:83`, `:250` |
| M3 | `sed -n '94p' O08` vs `sed -n '257p' O01` | O08 `…exit 0 with no manifest-roster row`; O01 `…exit 0 with the manifest-roster row green` (the one-hunk difference) |
| M4 | `sha256sum tools/exercise-handoff-e2e.py` | `e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553` = O01's declared patched digest |
| M4 | isolated `git archive HEAD` + `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit **0**; `selftest: OK — positive run (…) plus 45 controls`; m15b green and names the member |
| M5 | `wc -c reports/round-39/cov/C05-audit.md`; `grep -n '4/4 PASS'` | `28221` B; `:46` |
| M5 | `grep -n 'R01-' reports/round-39/cov/C05-audit.md` | `:150-153` (R01-14), `:165` (R01-9/F5), `:169-180` (R01-8/10/11/12/13), `:193` (R01-4 closure) |
| M6 | `grep -n 'R01-1 ruling folded' reports/round-39/calib/recount-ledger-successor.json` | `:8` — mechanism + ruling folded |
| M7 | `wc -c reports/round-39/calib/isolation-replay-protocol.md`; `grep -c '^## '`; `tail -1` | `2829` B; `3`; `## 3. Step 0 — determine the close commit` (file ends on the heading) |
| M7 | `grep -ci 'discriminator' protocol` | `0` |
| M8 | `grep -n 'ROOT = ' reports/round-{33..38}/run-validation.py` | r33 `:23` relative; r34 `:10`, r35 `:9`, r36 `:8`, r37 `:5`, r38 `:5` absolute — **five**, while the landed protocol `:10` names three |
| M9 | `grep -c 'clone' reports/round-39/validation.json` | `0` |
| M10 | `ls corpus/knowledge/linguistics/*.md \| wc -l`; entries | `25`; includes `taboo-strata-lifecycle.md`, `dialect-register-consistency.md`, `translation-protocol-fidelity.md` |
| M10 | `reports/round-40/validation.json` | `acceptance_checks_passed: True` |
| M11 | `grep -rli 'taboo' corpus/knowledge/verification/*.md \| wc -l` | `11` over 24 files; `grep -ci taboo` on the one new file: `worked-example-verification.md` → 1 |
| M12 | `python3 -c json.loads(<Ca01 §8 fence>)` | **parses**; 4 rows; computed leg counts `1 fixed / 10 recorded / 7 routed / 4 c-n-r = 22`, identical to `counts.sub_leg_*` |
| M13 | `grep -rn 'min_bytes\|min-bytes\|MIN_BYTES' reports/round-4[0-2]/run-validation.py tools/harness/` | exit 1 — no durable min-bytes check |
| M14 | `git status --porcelain` | `?? reports/round-43/` only |

Artifact digests re-computed and matching Ca01's §1 pins exactly: `defect-queue-v2.json`
`dfc9265d…`, `R01-review.md` `4fe294ae…`, `C05-audit.md` `e5f3b585…`,
`recount-ledger-successor.json` `64b93cfd…`, `basename-couples-policy.md` `105dfff6…`,
`O01-guard-design.md` `d863af31…`, `O03-verify.md` `cc24b79c…`, `O02-isolated.md`
`e314dbf3…`, `O08-regression.md` `3818df94…`.

## 2. Per-row verdicts

### 2.1 `r38-O07-empty-fragment` → **AGREE** (Ca01: `recorded`; prevention `routed-with-owner`)

- The measured fact is exact: 0 bytes, empty-file digest (M1). Filed bytes immutable, so
  `recorded` is the only correct primary class.
- The prevention leg is genuinely unlanded: no `min_bytes`/`MIN_BYTES` check exists (M13).
- Ca03 adds the stronger evidence: the r41/r42 runner's `empty` computation is dead code —
  `missing` contains only non-existent paths, `empty` intersects it with `os.path.isfile`
  (always false), and `os.path.getsize` is called on those non-existent paths
  (`reports/round-41/run-validation.py:168-173,183`; `reports/round-42/run-validation.py:177-182,192`).
  I reproduced those lines by reading. This does not change Ca01's class; it confirms the
  prevention leg must stay routed (r44 runner / template).
- **Verdict: class stands; cite Ca03's runner evidence as the reason the prevention is not "fixed".**

### 2.2 `r38-O08-fragment-defect` → **AGREE** (Ca01: `recorded`)

- O08 `:83` asserts `ae22013b…` *"is exactly the digest O01 §6 declares"*; O01 `:144` and `:309`
  declare `e5812751…`. The values differ (M3).
- The one-hunk difference is visible without executing anything: O08 `:94` ends the m15b string
  with *"no manifest-roster row"*, O01 `:257` with *"the manifest-roster row green"*. Independent
  corroboration: the HEAD tool hashes to `e5812751…` (O01's value) and its selftest is green with
  45 controls and m15b naming the member (M4).
- `recorded` is right: filed bytes cannot be edited; the correction is the successor record.
  Ca01's corrected-attribution text is accurate.
- **Verdict: agree, no change.**

### 2.3 `r38-O02-fragment-defects` → **PARTIAL DISAGREE** (Ca01: all three `could-not-recover`)

The row asserts three defects in the **filed** O02 fragment. The filed blob equals the `dfb0719`
commit blob (M2), so the artifact O03 quotes is not the artifact that was filed.

**D-1 (`44` vs `45`) — AGREE `could-not-recover`.**
`grep -Fn "plus 44 controls"` → exit 1; `58-member` → 0 hits; filed O02 says **45** at `:20`,
`:62`, `:203`. The artifact measured today yields 45 (M4). No committed version contains 44, so
the reviewed intermediate draft is unrecoverable. No correction row against O02 is owed.

**D-2 (`m15b` "names nothing") — AGREE `could-not-recover`.**
`grep -Fn "green and names nothing"` → exit 1. The only "names nothing" in O02 is `:99`, about the
rejected rendered-text guard (G7), not m15b. O02 `:62`/`:203` describe m15b as in-sync roster
green; O01 `:228` asserts the member is named. The quoted description is absent.

**D-3 (tamper prediction names the frozen-packet leg) — DISAGREE: `recorded`, not
`could-not-recover`.**
The exact quoted string is absent (`grep -Fn "does not match the frozen packet digest"` → exit 1),
but a **weaker form survives in the filed bytes** at O02 `:160-166`:

```text
160  - The guard is naming, not detection. The 13th component is already digest-checked by
161    v3_verify_component_digests (:2208-2222) — a mutated 13th component reds E2E-DIGEST
162    with or without the read-set expansion (O05 §4, R02 Finding 6). Under the guard, a tampered
163    13th component still cannot produce the per-input input-digest leg, because the file is
164    not a read-set member; it surfaces through the assembled-vs-frozen packet compare
165    (:3951-3957). …
```

The first sentence states the correct leg; the last sentence attributes the tamper's surfacing to
the **assembled-vs-frozen compare**, which O03 §4.3 measured is not what fires first
(`v3_verify_component_digests` runs inside `V3Assembly` before the guard and before `:3951-3957`).
So a weaker D-3 persists: the paragraph is internally inconsistent, and the trailing claim needs
the correction. Ca01's §3 D-3 quotes only `:160-162` and calls the filed text "the opposite and
correct mechanism" — it does not read `:164`. Ca03 §2.2 (`:99-104`) reads `:164` and assigns
`recorded`; that is the evidence-supported class.

- **Row-level recommendation:** `recorded` (Ca03) or `could-not-recover` **with an explicit
  `recorded` sub-leg for D-3**. The integrator should not file a blanket "all three
  could-not-recover": it would leave O02 `:164` uncorrected. D-1/D-2 stay `could-not-recover`.
- Ca01's sentence *"the cited quotes cannot be recovered in any durable artifact"* is imprecise:
  the **original draft text** is unrecoverable, but the **quotes themselves** are durably in
  `O03-verify.md:257-306`. Reword to "the pre-filing draft is unrecoverable; the quotes are
  recorded in O03, which cannot be treated as a source for filed O02 bytes."

### 2.4 `r39-review-findings-disposition` → **AGREE ON CLASS; two sub-classes and one count need correction**

The meta-row class `fixed-with-evidence` is correct **conditional on the integrator filing
`dispositions-r38-r39.json`**: the row's defect is the absence of a per-finding record, and the
successor artifact supplies it. The underlying findings are not all fixed, and Ca01 says so
(5 routed + 1 c-n-r + R01-1 residual). My independent per-finding reconciliation:

| finding | Ca01 | Ca03 | Ca02 verdict | evidence |
|---|---|---|---|---|
| R01-1 | `recorded` + residual `routed` | `recorded`, next_touch none | **Ca01** | ledger `:8` records the mechanism, but R01 `:240-244` requires the ruling *in the protocol text*; the protocol has no such section (M7). Residual routed is real. |
| R01-2 | `routed` | `routed` | **agree** | protocol `:10` names 3; r37 `:5`, r38 `:5` also absolute (M8) — five total. |
| R01-3 | `routed` | `routed` | **agree** | `grep -ci discriminator` → 0; no Tier B body in the 52-line file. Live defect. |
| R01-4 | `fixed` (r39 audit) | `fixed` (r40 audit) | **Ca01 citation; class fixed** | The fixing artifact is `reports/round-39/cov/C05-audit.md` (28,221 B, `:46` 4/4 PASS), filed at `dfb0719`. `reports/round-40/cov/C05-audit.md:26-27` is a **different audit** (of the r40 linguistics drafts); its 4/4 PASS cannot evidence R01-4. Ca03's `fixed_at: round-40` is a misattribution. |
| R01-5 | `routed` | `routed` | **agree** | `grep -c clone reports/round-39/validation.json` → 0 (M9); no declared-deviation record. |
| R01-6 | `routed` | `routed` | **agree** | `Ca01-protocol.md:166` still has `… or True`; line pins `:76-78` off by one. Canonical stub is truncated before §5. |
| R01-7 | `routed` | `routed` | **agree** | policy still says "single physical line" at both `:16`; `grep -c to-verify` → 0; r43 O is the named successor. |
| R01-8 | `recorded` | `recorded` | **agree** | `C05-audit.md:169-174` folds it. |
| R01-9 | `recorded` | `recorded` | **agree** | `C05-audit.md:165` F5 folds it. |
| R01-10 | `recorded` | `recorded` | **agree** | `C05-audit.md:175-176`; r39 staged both fence shapes 4/4. |
| R01-11 | `recorded` | `recorded` | **agree** | `C05-audit.md:176-177`; executable bar unaffected. |
| R01-12 | `recorded`, HEAD 11 | `recorded`, r39 10 | **Ca01's number** | HEAD is 11 over 24 files; `worked-example-verification.md` carries 1 (M11). 10 + 1 is consistent; class `recorded` either way. |
| R01-13 | `recorded` | `fixed`, r40 | **Ca03** | r40 landed G2–G4 as four entries (`reports/round-40/claims.json:14`; linguistics 21→25); HEAD has `taboo-strata-lifecycle.md`, `dialect-register-consistency.md`, `translation-protocol-fidelity.md`; r40 acceptance true (M10). `fixed-with-evidence`, `fixed_at: round-40`. Ca01's `recorded` is stale. |
| R01-14 | `could-not-recover` | `could-not-recover` | **agree** | R01 `:292-299` self-files it; C05 `:150-153` records `to-verify`; no durable handle. |
| (minor) | `recorded` | omitted | **Ca01 completeness** | R01 `:245-247`; including it is harmless and more complete. |

Two further corrections to Ca01's draft:

1. **Counts line §2 (`Ca01-dispositions.md:86-87`) is wrong.** It reads
   `fixed 1, recorded 8, routed 6, could-not-recover 5` (sum 20). The JSON's own `counts` block
   declares 22 legs at `1 / 10 / 7 / 4`, and a programmatic recount of the fence reproduces
   exactly `1 / 10 / 7 / 4 = 22` (M12). Line 81's *finding-level* count
   (`1 fixed, 8 recorded, 5 routed, 1 c-n-r` = 15 findings) is correct against §6. Correct lines
   86-87 to the JSON's 22-leg numbers, or delete the sentence and cite `counts`.
2. **`parent_row` line ranges are off by one at the end in all four rows.**
   The queue rows are `:282-290` (O02), `:292-300` (O08), `:302-310` (O07), `:343-351`
   (r39-review); Ca01's JSON says `:282-291`, `:292-301`, `:302-311`, `:343-352`. Ca03's table is
   exact. Metadata-only, but the integrator should not propagate the long ranges.
3. **Field name precision:** the r39 receipt field is `acceptance_checks_passed: True`, not
   `acceptance`. Substance unchanged; cite the exact key.

## 3. Internal consistency and write-surface check

- The fenced JSON parses (12 335 chars, 4 rows) and its `counts` reproduce a programmatic leg
  recount (M12). `findings_dispositioned: 19` is consistent with 3 O02 + 1 O08 + 15 R01 findings;
  O07's two legs are not "findings" under that definition. No finding is dropped.
- **No filed byte is proposed for edit.** Ca01 `:4`, `:131`, `:213-214`, `:502` all state
  successor-only; the JSON pins `defect-queue-v2.json` at `dfc9265d…`; the four
  `queue_successor_entries` are new r43 records. I found no edit/rewrite instruction for
  `reports/round-1..42/**`, `corpus/lessons/**`, `tools/gates/frozen/**`, or corpus bytes.
- `git status --porcelain` at verification time: `?? reports/round-43/` only. Ca01's `writes`
  list (`Ca01-dispositions.md`) is true; the integrator's later writes (the JSON + queue successor)
  are new files, not edits.
- This seat wrote only this file. The isolated `git archive` tree lives under `.scratch/ca02-tree`
  (gitignored); no corpus, tools, or filed-round bytes were touched.

## 4. Cross-claim alert (claim C) — independently confirmed

**The lithic slot is already built at HEAD; claim C's before-state is false.**

- `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **26**; the listing includes
  `mineral-stone-symbolism.md` (61 884 B, sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`).
- `git show --stat 7ceff59 -- corpus/knowledge/myth-symbol/` adds **192 lines** for
  `mineral-stone-symbolism.md`, alongside `purity-pollution-boundary-systems.md` and
  `sacred-topography-pilgrimage.md`.
- `corpus/README.md:6,10,219,544,548` already documents the entry and the 223 total
  (`myth-symbol 23 → 26`, totals `220 → 223`, sweep `223 == 223`).
- The r42 spare's own header (`reports/round-42/cov/C01-mineral-spare.md:1`) says C04 landed and
  *"THIS draft is routed as the named spare for a future re-scoped claim"*.

Landing the spare under `myth-symbol/` would either overwrite the existing lithic entry
(forbidden) or create a second lithic register while raising the count to 27. I am not proposing a
filename and not touching corpus bytes; the C seats/integrator must adjudicate the claim before
any apply. This is a round-level blocker for claim C, independent of the Ca dispositions.

## 5. New observations outside the four rows (for the integrator, not filed as Ca rows)

1. **The r39 isolation-replay protocol landed truncated.** 2 829 B, three H2 sections, file ends
   at the `## 3. Step 0 — determine the close commit` heading (line 52); it references "the §9
   vocabulary" and "Tiers A and B" that do not exist in the file. This is why R01-2/3/5/6 can only
   be routed: the canonical artifact is incomplete, not merely unamended. It is not represented
   as its own queue row. Recommend a successor row (`r39-protocol-landing-truncated`, owner
   integrator/protocol author) through Ca03's queue mechanism — this seat does not create it.
2. **The r41/r42 runner's empty-file check is dead code** (r41 `:168-173,183`; r42 `:177-182,192`):
   `missing` contains only non-existent paths; `empty` intersects it with `os.path.isfile`
   (always false), the second `missing` comprehension requires `x not in missing` while iterating
   `missing` (always false), and `os.path.getsize` is called on non-existent paths. This supports
   keeping O07's prevention `routed` and strengthens Ca03's OBS-1. It is a runner bug, not a
   disposition-row defect.
3. The r39 C05 audit already folds R01-8…R01-14 (`:165-180`) and closes R01-4 (`:193`). The
   queue row's "only R01-1 is recorded" premise is stale; Ca01 states this correctly, but the
   successor record should name C05 as the pre-existing disposition carrier, not present the
   whole list as newly discovered.

## 6. Gate for the integrator

Apply `reports/round-43/calib/dispositions-r38-r39.json` only after these amendments:

1. **D-3 → `recorded`** (O02 `:164` correction), with D-1/D-2 remaining `could-not-recover`;
   choose row class `recorded` or a mixed `could-not-recover` + recorded sub-leg. Do not file a
   blanket "all three c-n-r".
2. **R01-13 → `fixed-with-evidence`, `fixed_at: round-40`** (r40 claims `:14`; linguistics 25;
   r40 acceptance true).
3. Keep **R01-4's evidence as `reports/round-39/cov/C05-audit.md:46`**; do not adopt Ca03's r40
   audit citation.
4. Correct **`Ca01-dispositions.md:86-87`** to the JSON's `1/10/7/4 = 22` (or delete the sentence).
5. Optionally fix the four `parent_row` end lines to `:282-290`, `:292-300`, `:302-310`,
   `:343-351`, and cite `acceptance_checks_passed`.

With those five edits, all four row classes stand: O07 `recorded` (+ prevention routed), O08
`recorded`, O02 `recorded`/mixed, R01 `fixed-with-evidence`. Zero findings dropped; no filed byte
edited.

## 7. Limits / `to-verify`

- **Verification pin:** Ca01 v2 sha256 `2ebbcd0abe624f137286d14b73e5a2a8425d64b5b90ae7c3a3b6b2c7bd3f727b`
  (33 409 B) and Ca03 sha256 `3b69db52e2833486549ff4167d57541c3815a2f747b0ac090a458dfba554b613`
  (33 556 B), both at 2026-10-19 14:00Z. A later revision is detectable as a digest mismatch;
  any such revision must be re-verified against this file rather than assumed addressed.
- `to-verify`: the pre-filing O02 draft O03 read (mtime 08:27 vs O03 08:35). `git log -S"44
  controls"` is empty and the file has one commit (`dfb0719`); its bytes are unrecoverable. I did
  not infer them.
- I did not run any `run-validation.py`, in-tree or copied; the only filed code executed was the
  v3 tool selftest in an isolated `git archive` of HEAD.
- R01-13's r40 landing was verified by entry presence, the r40 claim text, and the r40 acceptance
  flag; I did not re-audit the four entries' content (outside claim Ca).
- The cross-claim collision in §4 is reported, not adjudicated: filenames and corpus changes are
  the C seats'/integrator's decision.
