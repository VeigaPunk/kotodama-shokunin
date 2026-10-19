- Seat: R01 | reviewer | claim cross | date 2026-10-19 | baseline `7ceff59`
- Out path: `reports/round-43/review/R01-review.md` (the only write)
- Contract: `targets.json` seat R01 — "review the whole round's evidence chain — O's
  resolver + selftest + census, C's spare landing + README, Ca's dispositions.
  Named-verifier judgment per claim."

# R01 — non-author review: three claims, two stale premises, one false queue row

**Method / boundary.** Every number below was re-derived by this seat with read-only
commands at HEAD `7ceff59a0216a8ea21ee43262d9fc72abf770cee` (= round baseline `7ceff59`),
lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. I did not edit a filed
byte, did not stage anything under `corpus/`, did not execute any
`reports/round-*/run-validation.py`, and did not run git-mutating/network/install commands.
`git status --porcelain` at my cuts → `?? reports/round-43/` only.

**Review window.** The round's fragments landed while this seat read. At the cut used for
the verdicts (~14:00 local) the following were present: K01, K02, P01, O02, O03, O04, O06,
O07, O10, O12, C01–C07, Ca01, Ca03, X00, S01, S02, A01. During the same window O05 and X01
landed and were read (O09 landed but was not read); O05 independently found two O02 controls
non-discriminating, and X01 files the same C-duplicate and O-fork trades recorded here. Ca02
(`calib/Ca02-verify.md`) landed after the first draft and was read; §4.5 folds its verdict.
**Absent at the final cut: O01 (`op/O01-tool-draft.md`); R02 and X02 were not present in my
listing.** Where a verdict depends on an absent artifact I say so rather than infer it.

## 1. Verdict summary

| claim | named-verifier judgment | one-line basis |
|---|---|---|
| **O — operability** | **unprovable-but-better** | The claim's `before` is false: a tracked successor exists and is green. The residual work (D2 disposition, four-class census, ambiguous control, blank-line fix) is real and would improve the axis — but the named deliverable O01 is absent, so the claim as declared cannot be verified, and minting a second resolver would fork the parser. |
| **C — coverage** | **unchanged** (as filed: claim blocked; **harmed** if executed as declared) | The lithic slot is already owned by `mineral-stone-symbolism.md` (r42 C04). Landing the spare at its declared path overwrites; landing under a new slug duplicates the topic and imports false provenance claims. No corpus delta is the correct outcome. |
| **Ca — calibration** | **improved** (conditional on adopting Ca02's two corrections) | The per-finding disposition pass exists, is measured, and correctly falsifies the r38-O02 D-1/D-2 quotes. Ca02 landed and independently confirmed the two cross-seat corrections (D-3 `recorded`; R01-13 `fixed-with-evidence`). |

No axis is harmed by anything **already written** in `reports/round-43/`. The harm risks are
all in the not-yet-applied integration: a second resolver (O), a duplicate lithic entry (C),
or filing Ca's disposition table with an unreconciled class.

---

## 2. Claim O — operability

### 2.1 The `before` is factually false at HEAD

`claims.json:27` says "no durable instrument implements the r39 basename-couples policy; the
only resolver that ever ran (r39 I-C05) lives in ephemeral `.scratch`". Measured:

```
$ git log --oneline -3
7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore
ac47c78 round-41: admit O/Ca — ...
456674d round-40: final receipt refresh ...

$ git ls-files tools/harness/ | grep couples
tools/harness/couples-reference-extractor.py
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
```

The tool is tracked in `7ceff59` (r42's commit, whose message records "N6 successor
extractor" and whose `validation.json` files claim O `"passed": true`). Its selftest and
census, run by this seat:

```
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS glob fragment classified
rc=0

$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
rc=0
```

The I-C05 conflation is also real: r39 I-C05 is a source-pointer/citation resolver
(`reports/round-39/cov/C05-audit.md:30`), not a couples resolver; queue row
`r39-ic05-resolver-durability` is about that instrument. K01 reached the same conclusion
(`scout/K01-resolver-scout.md` §4). The claim's `before` must be re-written before any
admission text cites it.

### 2.2 What the landed tool genuinely does not do (the real r43 work)

The claim is not empty — it is mis-addressed. Four measurable gaps remain at HEAD:

1. **Blank-line over-capture (confirmed).** `couples_block` *skips* blank lines instead of
   terminating at them (`tools/harness/couples-reference-extractor.py:64-65`:
   `if not following.strip(): continue`). An indented prose paragraph after a blank line is
   therefore swallowed as a continuation. Reproduced by this seat with a synthetic fixture:

   ```
   parts: ['language — `writing-systems.md`',
           'This indented paragraph after a BLANK line mentions `sound-change.md` in prose.']
   joined: language — `writing-systems.md` This indented paragraph after a BLANK line mentions `sound-change.md` in prose.
   tokens: ['sound-change.md', 'writing-systems.md']      # the prose token is captured
   ```

   The live corpus has **0** such fields today (223 distinct basenames, 0 duplicates), so
   the census is not wrong now. But the r42 controls required a blank-line boundary
   (`reports/round-42/op/O02-controls.md:27`, control 4; `op/O05-traps.md:190-196`), and the
   landed code does not implement it. K01 independently found the same (K01 §5 F5).

2. **No ambiguous control.** The r42 selftest has a phantom check (re-labelled
   `prospective`) and a glob check, but no synthetic two-hit basename
   (`couples-reference-extractor.py:242-295`). The live index has 223 distinct basenames,
   so `ambiguous` is untested live too. The r43 claim explicitly requires a synthetic
   ambiguous negative (`claims.json:26,34`).

3. **No fallback mapping list in `--census`; no named reason per unresolved token.**
   `main()` prints only totals, wrapped fields, unresolved names, and misalignment
   (`:306-319`). Per-entry mode prints `class` and `mapping`, but unresolved/prospective rows
   leave `mapping` blank and carry no `reason` (`:175-182`). The claim's "every fallback
   mapping listed" and "a named reason" (`claims.json:26,28`) are **not** met by the landed
   path. O10's census schema is a spec for the missing output, not an execution of it.

4. **The filed policy still prescribes the defect.** Both the r39 landing and the r42 "full"
   successor say §1: "the `- couples:` line … (**single physical line**; extraction per
   `entry-audit.py:75`)" (`reports/round-39/calib/basename-couples-policy.md:16`;
   `reports/round-42/calib/basename-couples-policy-full.md:16`), and the full doc's §6 recipe
   uses the single-line `couples_field()` (`:148-150`). A tool that "implements the r39
   policy" literally reproduces D1. The r42 tool implements the *fix* (block + hyphen heal),
   not the filed text. This is a live conformance contradiction: the successor instrument and
   the policy document disagree, and the claim does not resolve it. K01 §5 F6 files the same.

### 2.3 The O02 controls: well designed, two defects

O02 filed 25 controls with a 25/25 green run on a reference host (`op/O02-controls.md:340`,
`:374`). That is useful work. Two findings:

- **S7a is not discriminating for the bug that exists.** The boundary fixture is
  `"- couples: method — `writing-systems.md`\n\nBody prose names `sound-symbolism.md`.\n"`
  (`op/O02-controls.md:272-274`) — the prose is **non-indented**. A host that skips blank
  lines but still requires indentation on continuations stops at that prose and passes S7a.
  The real F5 case needs an **indented** prose paragraph after the blank line (the fixture I
  used in §2.2). As written, S7a tests the C14 `fields_of` over-capture, not the r42 host's
  blank-line over-capture.
- **The controls are not run against the deliverable.** O02 §3 requires an injectable
  `classify(ref, entry_dir, index=None)`; the r42 host's third parameter is
  `prospective=False` (`:134`), so the controls cannot run against it without an API change.
  O02's 25/25 green is on a host the seat wrote, not on O01. That is a conditional, not a
  verification of the landed tool.

### 2.4 O01 is absent; the claim cannot close

`op/O01-tool-draft.md` does not exist at any cut (`ls` → No such file or directory).
O04 (`op/O04-verify.md`) and O12 (`op/O12-negative-proof.md`) both correctly recorded
`could-not-evaluate` for the draft, while verifying the r42 reference host. The claim's
counting commands name `tools/harness/basename-couples-resolver.py --selftest/--census`
(`claims.json:30-31`), a path that does not exist. `reports/round-43/run-validation.py` also
does not exist. So even a perfect draft would not yet have its declared commands runnable.

**O verdict.** `unprovable-but-better`: the r42 tool plus the four residual fixes would
improve operability; the claim as declared is unprovable (false `before`; absent O01), and a
second resolver at the claim-named path would **harm** the axis by forking the parser
(K01 §7; r42 K01's D1d divergence warning). The correct integration is a patch to
`couples-reference-extractor.py` (or an explicit supersession record), not a new live
resolver.

---

## 3. Claim C — coverage

### 3.1 The slot is owned; the claim's `before` is false

`claims.json:40` says "lithic slot named but unbuilt since r42's C01/C04 collision". Measured:

```
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/myth-symbol/ | grep -iE 'mineral|stone|gem|lapid| lithic'
mineral-stone-symbolism.md
```

`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` is 192 lines / 61,884 bytes,
sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`, added in
`7ceff59` and indexed at `corpus/README.md:219`. Its H1 is "Stone, gem and metal symbolism —
the lithic register: the lapidary code, material prestige, and the quarry-to-regalia chain"
(`:1`). `reports/round-42/validation.json` records claim C failed as declared with the ruling:
"C01 and C04 authored the same lithic register mid-wave; C04 lands, C01 routes as the named
spare … a successor round can land the spare under a re-scoped claim." README rev 2.4 says
the same at `corpus/README.md:5-12`. The spare's own line 1 says it is "routed as the named
spare for a future re-scoped claim" (`reports/round-42/cov/C01-mineral-spare.md:1`).
**r43 claim C is not a re-scope; it is the same scope.** Six C-block seats independently
reached this (K02, C01, C02, C03, C06, C07), and this seat did too; X01 reaches it as well
(T1, citing A01 at `adj/A01-scope.md:124-161`).

### 3.2 Both landing routes are barred

- **Declared path** (`mineral-stone-symbolism.md`, per `reports/round-42/cov/C01-entry-1.md:3`,
  `:28`): the write would be `M`, not `A` — an overwrite of a tracked, audited entry,
  violating the claim's own "no existing entry overwritten" (`claims.json:41`) and the
  shared rule at `targets.json:9`.
- **New slug** (`stone-symbolism.md`, `stone-gem-metal-register.md`, `lithic-register.md`,
  etc.): the count reaches 27/224, but two entries own the one lapidary slot named at
  `symbolism-synthesis-method.md:23,:29`. The spare's own `- gap filled:` (`:7`) and
  `- verified-at:` (`:24`) assert a 220-file tree at `ac47c78`, "no entry owns stone", and
  myth-symbol 23 — all false at HEAD (223 files, myth-symbol 26, owner present). Applying
  them "unmodified" would file false provenance, which `corpus/QUALITY.md:5-8` bars. C01
  (`cov/C01-prepare.md` §3) and C07 (`cov/C07-scribe.md` §3.3) reach the same conclusion.

### 3.3 The source audit found real defects (minor, but they matter if re-scoped)

C03 (`cov/C03-audit.md`) checked the spare and filed:

- **F3:** `politeness-taboo-euphemism.md:73` is the Steiner/Radcliffe-Brown/Douglas line;
  Frazer is at `:74` (method) and `:124` (calibration), registered at `:21`. I verified:
  `sed -n '73p' …` contains no Frazer; `:74` does. Off-by-one, correct file and substance.
- **F4:** `symbolism-synthesis-method.md:48` says "polarity axes", not "slots"/"enumeration"
  as the spare paraphrases. Paraphrase drift.
- **F5:** three same-round `reports/round-42/` paths cited by the spare did not exist at the
  `ac47c78` baseline it names. Not fabrication; a provenance-wording defect.

### 3.4 The sweep cannot certify this claim

C02/C05/C07 all show the same mechanism: the r28 sweep checks rows↔files, topic bytes,
totals, and the footer. It has **no ownership leg**. C05 staged a 224-file tree with two
lithic owners and got `rows 224 files 224`, `topic_mismatch 0`, `footer_ok True`, exit 0
(`cov/C05-delta-receipt.md` §3.4/§4.4). So "224==224 sweep-green" is necessary but not
sufficient; the claim's threshold would pass a duplicate-topic partition.

C02 and C05 also disagree on the hypothetical filename: C02 uses `stone-symbolism.md`
(`cov/C02-readme-draft.md:67`), C05 uses `stone-gem-metal-register.md`
(`cov/C05-delta-receipt.md:44`). That inconsistency is moot while no landing should occur,
but it shows no canonical path was agreed; the integrator must not treat either as a contract.

**C verdict.** `unchanged` on the evidence actually filed (no corpus delta; the claim is
blocked, and the blocking is correct). **`harmed`** if the integrator lands it as declared:
either an overwrite or a duplicate topic with false provenance. The spare should be retired
as superseded, or claim C re-scoped to a genuinely unowned gap with a fresh draft — the
spare itself is not that draft.

---

## 4. Claim Ca — calibration

### 4.1 The four rows, re-measured

| row | this seat's measurement | class that survives |
|---|---|---|
| `r38-O07-empty-fragment` | `wc -c reports/round-38/op/O07-scribe.md` → `0`; sha256 `e3b0c442…` (empty-file digest), identical at `dfb0719` | `recorded`; prevention `routed-with-owner` — the r41/r42 runners filter `empty` from `missing`, so no durable min-bytes check exists (Ca03 `:227-235`) |
| `r38-O08-fragment-defect` | `O08-regression.md:83` says `ae22013b…` "is exactly the digest O01 §6 declares"; `O01-guard-design.md:144,:309` declare `e5812751…`; O03 §4.4 shows the one-hunk `m15b` difference | `recorded` — the corrected attribution is "O08's own variant with the m15b string adjusted"; O08's readings stand |
| `r38-O02-fragment-defects` | see §4.2 | D-1/D-2 `could-not-recover`; **D-3 partially reproduces** |
| `r39-review-findings-disposition` | see §4.3 | one class per finding; the list is complete 14/14 + one unnumbered note |

### 4.2 The O02 row: D-1/D-2 are not in the filed artifact; D-3 is weaker, not absent

This seat independently hit the same wall as Ca01/Ca03:

```
$ grep -c "44" reports/round-38/op/O02-isolated.md
0
$ grep -n "45 controls" reports/round-38/op/O02-isolated.md
20: ... exit 0 with 45 controls ...
62: | selftest ... | ... plus 45 controls ...
203: ... "plus 45 controls" ...
$ grep -Fn "green and names nothing" reports/round-38/op/O02-isolated.md
(no match; the only "names nothing" is :99, the rejected rendered-text-guard row)
```

So **D-1 does not reproduce**: O02 says 45, not 44, and the string "plus 44 controls" is
absent. **D-2 does not reproduce as stated**: the only "names nothing" is `O02:99`, a
different (rejected) row; `O02:62` says "m15b in-sync roster green", which matches O01's
actual assertion. The likely explanation is the one Ca03 gives: O03 reviewed a pre-filing
draft that was amended before commit; no committed version of O02 contains the quoted text
(`git log -S"44 controls"` → empty). The queue row's phrase "three measured defects in the
filed O02 fragment" is therefore false for D-1/D-2 at HEAD.

**D-3 deserves a narrower correction than Ca01 gives it.** O02:160-164 says:

> "The 13th component is already digest-checked by `v3_verify_component_digests`
> (`:2208-2222`) — a mutated 13th component reds `E2E-DIGEST` with or without the read-set
> expansion … it surfaces through the assembled-vs-frozen packet compare (`:3951-3957`)."

O03 §4.3 measured the **per-component digest leg** firing, not the frozen-packet leg. O02
names the component leg in its first sentence and the frozen compare in its second, so the
defect is a **contradictory second sentence**, not "the wrong leg" wholesale. Ca01
(`calib/Ca01-dispositions.md` §3, D-3) classes D-3 `could-not-recover`; Ca03
(`calib/Ca03-queue-update.md:205`) says it "survives in weaker form". Ca03's reading is the
accurate one: the row should read **D-3 partially reproduces — correct the second sentence to
name the component-digest leg**; D-1/D-2 are `could-not-recover`.

### 4.3 The R01 family: complete, but two cross-seat class disputes

Ca01's table (`calib/Ca01-dispositions.md:167-181`) covers R01-1..R01-14 plus one unnumbered
note, zero undecided. The substance is sound: R01-4 fixed (`C05-audit.md` exists, 4/4 PASS at
`:46`), R01-8..R01-12 recorded in `C05-audit.md:165-180`, R01-14 `could-not-recover`.
Two disagreements with Ca03 must be reconciled before the successor queue is filed:

1. **D-3** — see §4.2. Ca01: c-n-r; Ca03: weaker form. Recommend the narrower correction.
2. **R01-13** — Ca01 classes it `recorded` (`calib/Ca01-dispositions.md:182`); Ca03 classes it
   `fixed-with-evidence` (`calib/Ca03-queue-update.md:67`, `:199`), citing
   `reports/round-40/claims.json:14` (G2-G4 landed as four entries, linguistics 21→25).
   I read that line: r40 claim C is exactly "Land K01-r39's routed gaps G2-G4 as four
   sourced entries … 21 -> 25". Ca03 is right; Ca01 under-credits. This changes the
   composition from Ca01's "1 fixed / 8 recorded" to Ca03's "2 fixed / 6 recorded" (both
   sum correctly once the unnumbered note is counted; the difference is R01-13).

### 4.4 The r39 protocol is truncated — the routed findings cannot be applied to it

Ca01/Ca03 both route R01-2/3/5/6 to the "protocol successor". I confirmed why: the landed
`reports/round-39/calib/isolation-replay-protocol.md` is **52 lines / 2,829 bytes**, has
three H2 headings, and ends at the `## 3. Step 0 — determine the close commit` heading.
`grep -c '^## '` → 3. It never contains §4-§9, Tier B, the five-runner census, the clone
deviation, or the `or True` line. So:

- R01-2 (three runners named vs five measured) is visible at `:10-13`;
- R01-3 (Tier B discriminator), R01-5 (clone deviation), R01-6 (`or True` in Ca01's protocol
  draft) have no landed text to amend;
- the r40 Ca03 receipt's citation to "protocol `:1-52` and §4" (`reports/round-40/calib/
  Ca03-receipt.md:205`) cites a §4 that does not exist in the filed file.

This is a calibration finding in its own right: the "landed protocol" is a stub, and the
routing language must say "protocol successor must first land §3-end", not "amend §4".

### 4.5 Ca02 has now landed and confirms both reconciliations

`calib/Ca02-verify.md` (257 lines) landed after this review's first draft and was read. It
re-measured every row independently (`O02` sha `e314dbf3…`, O07 `0` bytes, O08 digests, the
r39 protocol, the r40 claims) and reached:

- `r38-O07-empty-fragment`: **AGREE** — `recorded`; prevention stays routed (no min-bytes
  check; the r41/r42 `empty` leg is dead code).
- `r38-O08-fragment-defect`: **AGREE** — `recorded`; the `ae22013b…` / `e5812751…` mismatch
  and the one-hunk `m15b` difference reproduce.
- `r38-O02-fragment-defects`: **PARTIAL DISAGREE** — D-1/D-2 `could-not-recover` (the quoted
  strings are absent); **D-3 `recorded`**, because the weaker form survives at `O02:164`.
  That is exactly the correction §4.2 files.
- `r39-review-findings-disposition`: **AGREE on class, two sub-class corrections** —
  **R01-13 is `fixed-with-evidence`** (r40 G2-G4, `reports/round-40/claims.json:14`), which
  is exactly §4.3's reconciliation; and R01-4's evidence is the r39 audit, not Ca03's r40
  audit.

So the disposition artifact now has its independent verifier, and the verifier independently
reached the two corrections this review files. The remaining action is for Ca01 to adopt
Ca02's two sub-class changes before its JSON is filed; Ca03's table already carries the
R01-13 fixed class.

**Ca verdict.** `improved` — the pass exists, is measured, corrects a queue row that would
otherwise have been copied forward as three live defects, and now has an independent verifier.
It is conditional on (a) adopting Ca02's D-3 `recorded` and R01-13 `fixed-with-evidence`
corrections, and (b) recording the protocol truncation as the reason R01-3/5/6 cannot be
applied to the filed text.

---

## 5. Cross-cutting findings

### 5.1 No write-surface violation observed

At every cut, `git status --porcelain` → `?? reports/round-43/` only; `git diff HEAD` empty;
the r19/r27/r28 instruments and the r42 extractor retained their digests
(`e7992c32…`, `fb589b28…`, `9b2ccac0…`, `d8d23a26…` per O12 §2, matched by my own
`sha256sum`). Nothing was staged under `corpus/`. The C seats correctly wrote no corpus bytes.
O02's §4/§5 were placeholders at 13:57 and had filled by 13:58; the final fragment is
complete (25/25 at `op/O02-controls.md:340`). No seat wrote outside its out path in the
window I could see.

### 5.2 The round's own premises were stale, and its verifiers caught it

Both O and C were authored as if r42's C landing had not happened: O ignores the landed
extractor, C calls an owned slot "unbuilt". Every claim-specific verifier caught the
mismatch (K01, K02, C01, C02, C03, C06, C07, O04, O12). That is a credit to the round's
verification discipline, but it is also a process finding: the claim texts (`claims.json:27`,
`:40`) should have been re-measured against `7ceff59` before dispatch. The integrator should
not carry either `before` sentence into `LOG.md`/`SHONEN.md`.

### 5.3 Integration commands do not yet exist

Three paths named by the claims are absent at my cut:
`tools/harness/basename-couples-resolver.py` (O), `reports/round-43/run-validation.py`
(all claims), and `reports/round-43/calib/census-r43.json` (O's artifact). The integration
must either create them or amend the counting commands to the actual paths; otherwise the
round's validation cannot run its own thresholds.

---

## 6. Named findings (for disposition)

| id | claim | severity | finding |
|---|---|---|---|
| R01-43-1 | O | blocking-for-text | `claims.json:27` false: `tools/harness/couples-reference-extractor.py` is tracked in `7ceff59`, selftest 8/8, census 223/2730; I-C05 is a citation resolver, not a couples resolver. Re-scope O to hardening, not minting. |
| R01-43-2 | O | blocking-for-threshold | O01 draft absent at every cut; O04/O12 `could-not-evaluate`; the claim's `--selftest/--census` path does not exist. |
| R01-43-3 | O | defect | `couples_block` skips blank lines (`:64-65`); blank + **indented** prose is captured as couples tokens (reproduced). O02 S7a's non-indented fixture does not catch it. Fix the terminator and add an indented-prose control. |
| R01-43-4 | O | defect | `--census` prints no fallback mappings and no per-token reason (`:306-319`, `:175-182`); the claim's "every mapping listed / named reason" is unmet by the landed path. O10 is a spec, not an execution. |
| R01-43-5 | O | conformance | Policy §1/§6 still prescribe single-line extraction (`basename-couples-policy.md:16`; `-full.md:16,148-150`); the r42 tool implements the fix, the policy text does not. A successor note must reconcile, or "implements the policy" is false. |
| R01-43-6 | C | blocking | Lithic slot owned (26/223; `mineral-stone-symbolism.md`, sha `c99f44ca…`, r42 C04). Declared path overwrites; new slug duplicates and imports stale `:7`/`:24` claims. r42 ruling requires a re-scope. |
| R01-43-7 | C | audit | C03 F3 (Frazer `:73` → `:74`/`:124`), F4 (`:48` paraphrase), F5 (same-round paths absent at `ac47c78`). All minor; all must be fixed if the spare is ever re-scoped. |
| R01-43-8 | C | mechanism | The r28 sweep has no ownership leg; C05 staged a green 224 tree with two lithic owners. `224==224` cannot certify this claim. |
| R01-43-9 | Ca | calibration | D-1/D-2 of `r38-O02-fragment-defects` do not reproduce (O02 says 45; "names nothing" is `:99`, the rendered-text guard). Ca01/Ca03 caught it; **D-3 partially reproduces** at `O02:164` (frozen-compare sentence) while `O02:161` names the component leg. Ca01's blanket `could-not-recover` for D-3 is too strong; use Ca03's weaker-form correction. |
| R01-43-10 | Ca | calibration | R01-13: Ca01 `recorded` vs Ca03 `fixed-with-evidence`; `reports/round-40/claims.json:14` supports fixed (G2-G4 landed, 21→25). Reconcile to fixed before filing the successor queue. |
| R01-43-11 | Ca | calibration | `isolation-replay-protocol.md` is 52 lines / 3 H2, truncated at §3; R01-3/5/6 have no landed text to amend, and the r40 receipt's "§4" citation is to an absent section. Record the truncation as the reason for routing. |
| R01-43-12 | all | process | The claim texts were not re-measured at `7ceff59` before dispatch; both stale `before` sentences must not enter `LOG.md`/`SHONEN.md`. |

None of these is a canon, promotion, or admission verdict; they are review findings for the
integrator to disposition.

---

## 7. Integration asks

1. **Do not admit O or C as declared.** Re-scope O to "harden the r42 extractor + complete
   the disposition leg + file the census"; record C as `blocked-by-topic-collision` (the
   spare stays routed). A "claim failed as declared" is the honest outcome for C, matching
   r42's own ruling.
2. **O implementation:** patch `tools/harness/couples-reference-extractor.py` (or land the
   claim-named path with an explicit supersession record that keeps one live resolver).
   Fix the blank-line terminator; add an ambiguous control and an indented-prose boundary
   control; emit every fallback mapping and a named reason per unresolved/ambiguous token;
   add a stdout/JSON census artifact. Add a successor note that policy §1/§6 single-line
   text is superseded by block + hyphen-retained extraction.
3. **C:** no corpus/README delta. If a future round re-scopes, start from a fresh draft with
   a new absence sweep; do not apply the spare's `- gap filled:`/`- verified-at:` bytes.
4. **Ca:** file Ca01's disposition JSON after Ca02; reconcile D-3 (weaker form, per Ca03) and
   R01-13 (`fixed-with-evidence`, per r40 claims); keep the R01-2/3/5/6 routes but name the
   protocol truncation as the reason they cannot be applied yet.
5. **Runner:** create `reports/round-43/run-validation.py` or amend the claim commands; pin
   the resolver sha and the census sha in the receipt. Re-run the two independent verifiers
   after the patched tool lands.

---

## 8. Evidence commands (reproducible)

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

git rev-parse HEAD                                   # 7ceff59a0216a8ea21ee43262d9fc72abf770cee
git status --porcelain                               # ?? reports/round-43/ only
ls corpus/knowledge/myth-symbol/*.md | wc -l         # 26
find corpus/knowledge -name '*.md' | wc -l           # 223
sha256sum corpus/knowledge/myth-symbol/mineral-stone-symbolism.md  # c99f44ca…
sha256sum reports/round-42/cov/C01-mineral-spare.md  # 2b9326e3…; body 6999a912…

python3 -B tools/harness/couples-reference-extractor.py --selftest   # 8 PASS, rc 0
python3 -B tools/harness/couples-reference-extractor.py --census     # 223/2730 -> 2556/166/2/5/1
python3 -B tools/harness/couples-reference-extractor.py \
  corpus/knowledge/linguistics/phonetics-phonology.md                # 4 tokens: 2 direct, 2 prospective

wc -c reports/round-38/op/O07-scribe.md                              # 0
grep -c "44" reports/round-38/op/O02-isolated.md                     # 0
grep -n "45 controls" reports/round-38/op/O02-isolated.md            # :20,:62,:203
grep -n "names nothing" reports/round-38/op/O02-isolated.md          # :99 only (rendered-text guard)
sed -n '160,164p' reports/round-38/op/O02-isolated.md                # component leg + frozen compare
grep -n "e5812751" reports/round-38/op/O01-guard-design.md           # :144,:309
grep -n "is exactly the digest O01" reports/round-38/op/O08-regression.md  # :83

wc -l reports/round-39/calib/isolation-replay-protocol.md            # 52
grep -c '^## ' reports/round-39/calib/isolation-replay-protocol.md  # 3

sed -n '73,74p' corpus/knowledge/linguistics/politeness-taboo-euphemism.md
grep -n "G2-G4" reports/round-40/claims.json                         # claim C, 21->25
```

## 9. What I could not evaluate

- **O01's tool body** — absent; O04/O12's `could-not-evaluate` stands. I verified the
  reference host and the requirement surface, not a draft.
- **Ca02's independent verification** — landed after the first draft and was read; §4.5 folds
  its verdict. It confirms O07/O08 and D-1/D-2, and corrects D-3 to `recorded` and R01-13 to
  `fixed-with-evidence`.
- **R02 and X02** — not present in my listing at the final cut. X01 landed during the window
  and was read; its T1 (C duplicate), T3 (resolver fork) and T6 (Ca class disagreement)
  corroborate §2–§4. This review does not supersede R02/X02.
- **Any external source** — no network; the spare's `(to-verify)` legs remain as filed.

*End of R01 review.*
