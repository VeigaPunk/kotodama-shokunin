- Seat: O11 | scribe | claim O | date 2026-10-19 | baseline ac47c78

# O11 — receipt fold, post-review

**Fold status: post-review, partial. Claim O is NOT established.** The adversarial
leg arrived while this seat was writing: R02, X01, X00 landed at ~16:00–16:01Z, and
**X02 landed at 16:01:56Z** — all folded below. Only `review/R01-review.md` and
`op/O05-traps.md` remain absent. This fragment folds the reviews against the O-block
fragments and against my own independent read-only re-derivation, and records what
the claim still owes. It asserts **no acceptance**, re-classes **no** queue row,
and edits no filed byte. Its interim axis verdict agrees with X02 §"Axis honesty":
**no axis is improved** — claim O is `unprovable` at this cut.

## 1. What is landed, and what the fold is over

`find reports/round-42 -type f | sort` at `2026-10-19T16:01:56Z` → 29 files.
Relevant to claim O: `scout/K01-n6-scout.md`, `plan/P01-plan.md`,
`op/O02-controls.md`, `O03-predicted.md`, `O04-verify.md`, `O06-receipt.md`,
`O07-gap-fill.md`, `O08-queue-update.md`, `O09-scribe.md`, `O10-gap-fill.md`,
`O12-policy-check.md`; `cross/X00-connector.md`, `X01-trades.md`, `X02-honesty.md`;
`review/R02-review.md`; `scribe/S01-integration-draft.md`.

**Still absent** (per-path `[ -f ]`): `op/O01-fix-draft.md` (**the fix itself**),
`op/O05-traps.md`, `review/R01-review.md`, `reports/round-42/run-validation.py`,
`reports/round-42/validation.json`.

**Therefore claim O's `after_required` is unmet in every part**
(`reports/round-42/claims.json:16`): no durable fixed extractor exists at any host,
the wrapped field is not read whole by any *landed* instrument, no corrected census
is filed, and no fix selftest is green. What the wave produced is a fix **draft**
(O02's fenced battery, O10's fenced patch), a **prediction** (O03), a
**pre-landing verification of the repair surface** (O04), and four independent
recounts. The `counting_commands` entry
`python3 reports/round-42/run-validation.py` is not runnable — the file does not
exist, and running any round runner in-tree is prohibited for this seat
(`targets.json:8`).

## 2. The number the wave converged on — and my own reproduction

Seven seats now report the same quadruple. I re-derived it myself rather than
quoting it (heredoc, lane root, `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`, read-only, no runner executed):

| extractor | entries | refs | direct | fallback | ambiguous | unresolved |
|---|---|---|---|---|---|---|
| single-line (r19 `entry-audit.py:75` shape) | 220 | 2607 | 2435 | 166 | 0 | 6 |
| block + hyphen-retained rejoin (the fix) | 220 | 2611 | 2437 | 166 | 0 | 8 |

Arithmetic checks: `2435+166+0+6 = 2607` and `2437+166+0+8 = 2611` (both `True`).
Agreed by O03 §6, O04 §5, O06 §3, O07 §2, O08 §3, O10 §4, O12 §3, R02 §7, X01 T1 —
and by this seat's run. **Wrapped `couples` fields: 1**, at
`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`; my blank-line-and-
next-field-stop scan over all 220 entries returns exactly one, matching O03 §2,
O04 §2, O07 §1, O08 §2.1, O12 §3.

I also reproduced the r39 baseline at its own commit: single-line extraction over
the `dfb0719` tree (`git ls-tree` + `git show`, no checkout) gives
`entries=212 refs=2504`, the filed policy's ref total
(`reports/round-39/calib/basename-couples-policy.md:35-36`), and `2508` under block
extraction — the same +4 delta. *Caveat, mine:* my `dfb0719` run judged Tier-1
existence only against the `corpus/knowledge` file list, so its direct/unresolved
split is an artifact of an incomplete existence oracle. O12 §2 records the same
false start and its cause (the lane-root base is what makes lane-root files
`direct`); I therefore cite only the refs-level reproduction and report no class
split at `dfb0719`. O12's whole-tree run is the authoritative one.

## 3. The reviews' findings, folded

**3.1 R02 Trap B / X01 T4 — the obvious fix is a false-green generator, confirmed
first-hand.** The natural template for a block parser is the already-shipped
`tools/gates/provenance-audit.py:244-260` `field_block`, whose join is
`" ".join(part for part in parts if part)` (`:259`). I imported that module and
called `field_block(lines, "couples")` on the live entry: `present=True`, content
ending `... prospective sibling files: sound-change.md, tone- prosody.md,
sound-symbolism.md, writing-systems.md`; tokenized →
`['sound-change.md', 'prosody.md', 'sound-symbolism.md', 'writing-systems.md']`.
**Same 4 tokens, wrong 4** — it emits the phantom `prosody.md`. R02 §4 and X01 T5
report the identical probe. On `conlang-methodology.md` the same call stops
correctly at the unindented prose (line 9), so the host's *extent* is right and
only its *separator* is wrong.

**3.2 The join rule, measured four ways.** `:76` ends `tone-`, `:77` begins
`prosody.md`. Newline-join → `prosody.md`; space-join → `prosody.md`; empty-join
(hyphen deleted) → `toneprosody.md`; **hyphen kept and concatenated →
`tone-prosody.md`**. Only the last names the intended sibling, corroborated by the
entry's own body at `phonetics-phonology.md:279` ("Natural partners:
`sound-change.md` …, `tone-prosody.md`"). Consensus across K01 §4, O02 §4, O04 §4,
O06 §2.5, O07 §2, O10 §1, O12 §3, R02 §4, X01 T5.

**3.3 R02 §3 / X01 T6 / O12 §4 — the claim's census wording is wrong in
direction.** `claims.json:15` says the policy's `2504 = 2335 + 163 + 0 + 6`
"becomes the corrected baseline with the 2 phantom attributions dispositioned",
and `after_required` says "reproduces the r39 policy's arithmetic **minus** the
phantoms". Measured: nothing is subtracted. The fix **adds** 4 refs (2 resolving,
2 not) and unresolved **rises** 6 → 8. The r39 census's 6 unresolved tokens contain
no phantom at all — all six are real dangling references already attributed by
Ca04 D1. The two tokens the fix exposes (`sound-change.md`, `tone-prosody.md`) are
newly *surfaced*, not pre-existing. The honest statement is
`2504/2335/163/0/6 → 2508/2337/163/0/8` at `dfb0719`, and
`2607/2435/166/0/6 → 2611/2437/166/0/8` live. Agreed by O06 §3, O08 §3, O12 §4,
R02 §8, X01 T6.

**3.4 R02 §8 / X01 T6 — the threshold as written is unsatisfiable.** "Reproduces
the r39 policy's arithmetic" cannot hold at the live tree: the policy's figure is a
212-entry measurement (`basename-couples-policy.md` §5.5 "212 files at adoption")
and the live tree is 220. O12 §5 decomposes the growth cleanly: refs 2504 → 2607 =
+103, contributed exactly by the 8 entries `dfb0719..ac47c78` added (10+12+10+11
linguistics, 16+12+12+20 verification); fallback 163 → 166 = +3, all from
`sacred-registers-liturgical-language.md`; unresolved 6 → 6 (single-line) — the new
entries introduce no dangling token. **This closes the `to-verify` I carried in my
first draft** (§4 of the earlier revision): the +3 fallback movement is now
attributed per-entry by O12 §5, and I independently confirm the four new
linguistics entries carry 10/12/10/11 couples tokens with 10/12/9/11
unique-basename-resolvable.

**3.5 R02 §2 / O03 §9 / O12-F1 — the filed r39 policy is a truncated prefix.**
Verified first-hand: `wc -l -c reports/round-39/calib/basename-couples-policy.md`
→ `107 5832`; `tail -6` ends on the §6 lead-in
`(export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1):`; `grep -c '```'` → **0**;
`grep -c RESULT` → **0**; `grep -c 2504` → **0**. The draft
`Ca03-basename-policy.md` is `359 19409` with 4 fences, and O12 §1 establishes the
sharper fact I did not measure: the filed file is **byte-identical to draft lines
41–147** (`diff <(sed -n '41,147p' draft) filed` → no output), i.e. it stops exactly
where the §6 fence opens and omits §6 and §7 entirely. Git provenance confirms a
landing defect, not a later edit: `git log --oneline --all` on the path → single
commit `fd55e1f`; `git show fd55e1f:… | wc -l -c` → `107 5832`. O12 §1 also names
why the r39 gate passed it (`reports/round-39/run-validation.py:117-121` checks one
marker string, `fallback`, which sits in the landed §2).

**Consequence for K01.** `scout/K01-n6-scout.md` cites the policy's "§6 recipe
`:149-258`" and "the filed-run output `:260-264`", and §5 argues "the policy's own
§6 recipe still carries the N6 defect". Those citations are to the **draft**, not
the landed file — the landed file has 107 lines and no §6. K01's numbers are right
(I reproduced `2504` at `dfb0719`), but its landed-policy citations do not resolve
and its "policy's §6 recipe" claim is unverifiable from the durable object. Same
defect in O03 §5's citation of "the policy's own §5.5 … list … `:99` region": the
filed §5 ends at `:102` with the glob-fragment rule and contains no such list.

**3.6 O03 §4's class table contradicts O03 §6's own arithmetic.** O03 §4 states
that at `dfb0719` the two live tokens classify `fallback`, "because
`corpus/knowledge/linguistics/` held only 21 entries at r39 close (24 at HEAD)".
Its §6 table reports `direct=2337` for that same tree. I checked the tree directly:
`git ls-tree -r --name-only dfb0719` contains
`corpus/knowledge/linguistics/sound-symbolism.md` and `…/writing-systems.md`; the
r19/policy Tier-1 candidate list is **entry-dir first** (`entry-audit.py:87-95`), so
both resolve `direct` — §6 is right and §4's label is wrong. O03 §4's "24 at HEAD"
aside also conflates the partition size with resolvability. R02 §5 independently
gets this right ("2 `direct` + 2 `unresolved`"). This is a citation-level defect in
O03, not a numeric one.

**3.7 O03 §5's join recommendation is self-contradictory.** O03 §5 recommends
"**drop the hyphen and merge (`tone-prosody.md`)**", but its own table two lines
above shows `dehyphen (drop "-") -> toneprosody.md # over-merge`. Dropping the
hyphen cannot yield `tone-prosody.md`. The correct rule is hyphen-**retained**
(K01 §4, O02 §4, O10 §1 rule D, O12 §3, R02 §4, X01 T5, and my §3.2).

**3.8 The wrapped-field count is 1, not 2.** O03 §3, O04 §2, O07 §1, O12 §3 and
R02 §2 all reach 1 via the indent rule; I confirm 1, and I measured the
over-capture that can produce 2: C14's `fields_of`
(`reports/round-35/cov/C14-audit-6-10.md:234`, `elif cur and line.strip():`) has no
blank-line terminator and swallows the body paragraph of `conlang-methodology.md`
into the `couples` value. K01 §6 D1b and O03 §3 name this hazard; my measurement
confirms it, and O02 §5 files it as a third defect class.

**3.9 X01 T1 / T3 — the census is a measurement of one tree state.** The four C
entries are themselves couples-bearing inputs, so a "corrected census" that does
not name its entry count and tree digest will be stale the moment C lands, and the
Tier-2 uniqueness assumption (policy §5.5: "re-run §6 and re-adjudicate") must be
re-checked at 224. X01 measures 220 basenames / 220 distinct / **0 collisions** at
baseline. Landing order therefore matters: census last, or twice with both states
recorded.

**3.10 X01 T2 — C's new entries can manufacture O's phantoms.** A new myth-symbol
entry whose `- couples:` names a nonexistent file adds a census phantom
indistinguishable from the pre-existing ones. X01 requires a pre-landing
token-class check on each of the 4 drafts. This is a cross-block dependency the
integrator must sequence, and it is outside this seat's scope to execute.

**3.11 O08's queue delta remains conditional.** `op/O08-queue-update.md` §5 supplies
a `carried-with-owner` content refresh for row `N6-couples-extractor-wrapped-field`,
gated on five conditions. Its gate 2 (a second seat independently reproduces the
mangling) is now satisfied — O04 §4, O10 §1, R02 §4, X01 T5 and my §3.2 all
reproduce it. Gates 1, 3, 4, 5 are the integrator's to rule on. **The row's class
stays `carried-with-owner`**: O08 §4 is right that no re-class to
`fixed-with-evidence` is admissible while no fix is landed, and O08's §5 delta is a
status refresh only. This seat applies nothing.

**3.12 R02 cross-block note — `N6` is overloaded.** The v2 queue's `N6` is the
extractor defect (`defect-queue-v2.json:362-369`); the r40 Ca03 receipt
(`reports/round-40/calib/Ca03-receipt.md:86-88`) uses `N6` for a different item (the
corpus phantom-repair rollup) and calls the extractor D1 `N4`. O08's mission must
target the v2 row id, not the receipt's `N6`.

**3.13 X02's nine findings, folded.** X02 (`cross/X02-honesty.md`) is the honesty
critic and is the last review to land. Its nine findings, against the O block:

- **X02-1 (host and arithmetic not both filed).** `claims.json:16` names the host as
  "likely the r39 C12 runbook's resolver or a tools/harness couples checker", but C12
  is a runbook *document*, `tools/` holds no couples resolver, and the landed policy
  contains no arithmetic (`grep -c 2504` → 0). X02 asks the receipt to keep two roles
  distinct: the **census resolver** (none exists) and the **live block-extraction
  host** (`tools/gates/provenance-audit.py:244-260`, which does not tokenize
  `couples` — its finding is `empty-couples` only). My §3.1 measured that host
  directly; X02's distinction is correct and I adopt it.
- **X02-2 (the "4/4 targets" threshold is a two-reading trap).** Read as
  *resolution* it is unsatisfiable (only 2 of the 4 named files exist); read as
  *extraction* it is met by the space-join parser that still mangles
  `tone-prosody.md` into `prosody.md`. The receipt must state it as "4 of 4 tokens
  captured, and `prosody.md` never emitted". My §3.2 and §3.3 measure both legs.
- **X02-6 (O03 §4 prose contradicts O03's own §6).** X02 confirms §3.6 above and
  adds the live partition count: O03 §4 says "24 at HEAD" where the live
  `corpus/knowledge/linguistics/` is **25**. My §2's census is over 220 entries;
  `ls corpus/knowledge/linguistics/*.md | wc -l` → 25.
- **X02-7 (O03 §8 item 6 is a false-green test).** O03 §8 item 6 tells verifiers that
  reading `sound-symbolism.md`/`writing-systems.md` as `direct` at `dfb0719` is
  evidence of the C14 over-capture. It is inverted — those files exist at `dfb0719`
  (my §3.6 checked the tree), so `direct` is the correct result. A verifier applying
  it literally would fail a correct tool.
- **X02-8 (a digest is attributed to the wrong path).** `op/O04-verify.md`'s
  Citations pin the policy under test as `basename-couples-policy.md` with sha256
  `125ede77…`; that digest is the **draft** `Ca03-basename-policy.md`. The landed
  policy is `105dfff6…` (my §3.5 measured both). O06 §1 pins the correct value.
- **X02-9 ("the fix host is unresolved" understates the finding).** O04/O09 say
  `tools/` carries no couples resolver; true of a *resolver*, but O10 §2 and R02 §4
  located the live *block-extraction* host. X02's reconciliation is the one I use in
  §3.13's X02-1 bullet.
- **X02-4, X02-5** (queue edited in place; policy truncated at §6) are the same
  findings as O08 Obs. 3 and O03 §9 / O12-F1; folded at §3.5 and §3.11. I confirm
  X02-5's measurements against my own (§3.5) — `wc -c` gives the draft as `19409`
  bytes and the landed file as `5832`, both matching X02 exactly.
- **X02-3** (the C06 vector) is folded at §4 below.
- **X02's own honesty assessment** — that every seat labelled its absent
  dependencies rather than inventing them, and that **no axis may be judged improved
  at this cut** — is the interim verdict this fold adopts. I reproduce X02's digest
  check: `sha256sum reports/round-42/claims.json` → `513ae21042c7516e…` and
  `targets.json` → `6db0a9ebcde81d55…`, both equal to the `durable_sources` pins in
  `telemetry/dispatch-declared.json`.

## 4. The C leg — review-confirmed defects the integrator must fix

Outside this seat's claim, but folded because four seats file them as blocking:

- **The C06 mission vector is arithmetically impossible.** `targets.json:163` binds
  C06 to "vector `25/23/27/25/24/94`". I computed it: **sums to 218**, not 224. The
  README's canonical order is `[linguistics, myth-symbol, culture-material,
  synthesis, verification, civilizations]` (sweep `footer_live.order`, which I read
  live: `footer_live {"total": 220, "dir_totals": [25, 23, 25, 29, 24, 94], "order":
  ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification",
  "civilizations"]}`). The mission literal leaves myth-symbol at 23 and drops
  synthesis 29 → 25. Correct rev-2.4 vector: **`25/27/25/29/24/94`** (sum 224).
  R02 §12 and X01 T7 both derive this independently; I confirm the arithmetic.
- **The baseline sweep is green.** I ran `python3 -B reports/round-28/readme/sweep.py`
  live: `rows 220 files 220`, `missing_from_index 0`, `topic_mismatch 0`,
  `orphan_rows 0`, `header_drift {}`, `totals_line 220 totals_ok True`,
  `footer_ok True`, `readme_sha256 d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f`,
  exit 0 — matching R02 §11 and X01 T8. So the C threshold is satisfiable, but a
  README built to the mission vector would be sweep-RED (X01 T7).

## Owed

- **O01 (the fix) does not exist.** Until `op/O01-fix-draft.md` lands, there is
  nothing for O04/O05 to verify (O04's own Verdict records this). `op/O05-traps.md`
  and `review/R01-review.md` are also still absent — the fold is post-review for
  R02/X01/X02/X00 only.
- **Integrator: the fix host must be a NEW instrument.** Every extractor that
  implements the defect is a filed byte (`reports/round-19/audit/entry-audit.py:75`,
  `reports/round-27/audit/entry-audit.py:275`, both
  `re.search(r"^- couples:\s*(.*)$", text, re.M)`), and the round's non-goal "no
  filed byte rewrites" bars patching them in place. `tools/harness/` holds no
  couples resolver. X01 T4's recommended shape is a thin census instrument (new
  file under `tools/`) that **imports** `provenance-audit.field_block` rather than
  adding a fourth hand-rolled parser — but that import alone is insufficient
  (§3.1: the host's `" ".join` mangles the token), so the join rule must be
  supplied by the new instrument. R02 §9 and K01 §7 agree the host choice is the
  integrator's.
- **Integrator: restate claim O's `after_required`/threshold** (§3.3, §3.4) — the
  filed 212-entry arithmetic is not reproducible at the live 220-entry tree, and
  the wording presents a subtraction where the measurement is additive.
- **Integrator: file the r39 policy truncation as a defect row** (§3.5). Repairing
  it means editing filed r39 bytes, outside every seat's scope; the correction can
  only be a successor note (O12's drafted content at `op/O12-policy-check.md` §6).
  O12-F1 also asks the r39 gate-coverage record to note that
  `run-validation.py:117-121` verified a marker, not the document.
- **Integrator: the queue successor artifact still does not exist** (O08 §6 Obs. 1).
  r41's X00 required one and named the filed r40 queue immutable.
- **Integrator: seven unresolved tokens remain undispositioned** (O12 §4): the X26-1
  path at two carriers (`verification/label-channel-routing-verification.md:14`,
  `synthesis/typed-label-routing-workflow.md:16`), three `language-contact.md:7`
  seeds, the `-gate.md` glob fragment (policy §5.6 says do not count it — which
  makes the "corrected unresolved" number 8 raw or 7 §5.6-conformant, per O12 §3),
  and the two N6-exposed seeds.
- **Integrator (X02's filing request):** record X02-1 (host and arithmetic not both
  filed), X02-2 (the 4/4 two-reading trap), X02-4 (queue edited in place), X02-5
  (policy truncated at §6) and X02-8 (the O04 digest mis-attribution) as defect rows
  rather than letting them vanish into the receipt. Restate claim O's threshold as
  "4 of 4 tokens captured and `prosody.md` never emitted".
- **Integrator: fix O03 §4's and §8-item-6's prose before quoting them.** §3.6 and
  §3.13's X02-7 show §4's `fallback` label and §8 item 6's inverted test would each
  fail a correct tool; O03's *numbers* are right and its §6 table is the
  authoritative one.
- **to-verify (carried, not resolved here):** whether the successor instrument
  should treat lane-root files as Tier-1 resolvable when the census runs from a
  corpus-subtree root (O12 §Owed). And `ambiguous` is untested live in both trees —
  O05's synthetic fixture is its only coverage (O12 §Owed).
- **Claim C** (`cov/C02-entry-2.md`, `C07-verify.md`, `C08-verify.md` present;
  `C01`, `C03`–`C06` and `scout/K02-myth-gaps.md` absent) is outside this seat's
  scope; the C leg's completeness is not asserted here. X02's interim verdict is
  that C is `could-not-evaluate` — 1 of 4 entry drafts, no C06 delta.

## Citations

- Assignment, write boundary, prohibitions: `reports/round-42/targets.json:4-9`
  (shared rules; `:8` no in-tree `run-validation.py`), seat `O11` (`:111-115`),
  `:41-72` (O01–O05), `:90-93` (O08), `:118-121` (O12), `:163` (C06 vector).
- Claim O and thresholds: `reports/round-42/claims.json:13-18`; non-goals
  (`no filed byte rewrites`) `:19-21`.
- Filed extractors: `reports/round-19/audit/entry-audit.py:31,34-42,74-96`
  (`:75` single-line capture, `:87-95` Tier-1 candidate order), sha256
  `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`;
  `reports/round-27/audit/entry-audit.py:275`, sha256
  `fb589b28cf4769ac2ce39d820640bb464a93601f4486f54268d31e1c4c06bcda`.
- C14 block parser and its over-capture: `reports/round-35/cov/C14-audit-6-10.md:199,208-222,225-236`
  (`:234` the blank-line-blind append), `:249-260,263-288`, sha256
  `bf402bc6ebeeb6744e231065f83c2c2f0d2c2f7108a950ad9e2d13221dd309cb`.
- Live host: `tools/gates/provenance-audit.py:76-77` (`FIELD_RE`, `INDENT_RE`),
  `:244-260` (`field_block`; `:259` the `" ".join`), `:318-323` (couples used for
  presence only), `:448-449` (multi-line control), sha256
  `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a`.
- Wrapped field bytes: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (`:76` ends `tone-`, `:77` begins `prosody.md`; `:279` the intended-name
  corroboration), sha256 `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`.
- Landed policy and its truncation: `reports/round-39/calib/basename-couples-policy.md`
  (`107` lines / `5832` bytes, sha256
  `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`; `:35-36` the
  arithmetic; `:93-96` §5.5 re-adjudication; `:97-102` §5.6 glob fragments; ends
  mid-§6 at `:107`); draft `reports/round-39/calib/Ca03-basename-policy.md`
  (`359` lines, 4 fences, sha256 `125ede77…a17850`); landing commit `fd55e1f`.
- Origin finding: `reports/round-39/calib/Ca04-verify.md` (D1; `to-verify`
  full-recount at `:114-115`).
- Queue row: `reports/round-40/op/defect-queue-v2.json:362-369`
  (`N6-couples-extractor-wrapped-field`, class `carried-with-owner`);
  `reports/round-40/calib/Ca03-receipt.md:86-88` (the N4/N5/N6 senses).
- Sweep: `reports/round-28/readme/sweep.py:44-51` (partition order), `:106`,
  `:163-192` (footer leg), `:206-210` (`footer_live`).
- Wave fragments folded: `op/O02-controls.md` (§1,§3,§4,§5),
  `op/O03-predicted.md` (§2,§3,§4,§5,§6,§9), `op/O04-verify.md` (§1,§2,§4,§5,§6),
  `op/O06-receipt.md` (§2,§3,§5), `op/O07-gap-fill.md` (§1,§2),
  `op/O08-queue-update.md` (§2,§3,§4,§5,§6), `op/O09-scribe.md` (items 1–5),
  `op/O10-gap-fill.md` (§1,§2,§3,§4), `op/O12-policy-check.md` (§1,§2,§3,§4,§5,§6),
  `scout/K01-n6-scout.md` (§1,§4,§5,§6,§7), `plan/P01-plan.md` (§1.1,§1.2);
  `review/R02-review.md` (§2,§3,§4,§5,§7,§8,§9,§11,§12, cross-block notes);
  `cross/X01-trades.md` (T1–T9); `cross/X00-connector.md`;
  `cross/X02-honesty.md` (X02-1 through X02-9; "Independently reproduced",
  "Axis honesty"); `scribe/S01-integration-draft.md` (§0).
- Command outputs (this seat, 2026-10-19, lane root at `ac47c78`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only; no filed
  byte edited; no `run-validation.py` executed in-tree or in a copy; no git
  mutation, network or install):
  (a) `find reports/round-42 -type f | sort` → 27 files at `16:01:27Z`;
  per-path `[ -f ]` → `op/O01-fix-draft.md`, `op/O05-traps.md`,
  `review/R01-review.md`, `cross/X02-honesty.md`, `run-validation.py`,
  `validation.json` all absent.
  (b) live-tree re-parse (rule D = indent-bounded field + hyphen-retained rejoin,
  per-entry dedup + one-level brace expansion, policy §2 classifier) →
  single-line `220 / 2607 = 2435+166+0+6`; block `220 / 2611 = 2437+166+0+8`;
  arithmetic `True`; wrapped fields `1`.
  (c) `dfb0719` re-parse via `git ls-tree` + `git show` (no checkout) →
  `212 entries`, single-line `refs=2504`, block `refs=2508`; class split at that
  tree is oracle-limited and is explicitly **not** reported as a finding.
  (d) join-rule probe → newline/space-join `prosody.md`; empty-join
  `toneprosody.md`; hyphen-retained `tone-prosody.md`.
  (e) `importlib` of `tools/gates/provenance-audit.py` → `field_block` on
  `phonetics-phonology.md`: present `True`, tokens
  `['sound-change.md','prosody.md','sound-symbolism.md','writing-systems.md']`;
  on `conlang-methodology.md`: present `True`, stops at line 7 (no over-capture).
  (f) `dfb0719` existence checks → `sound-symbolism.md` and `writing-systems.md`
  present; `sound-change.md`, `tone-prosody.md`, `prosody.md` present nowhere
  repo-wide; `corpus/knowledge/linguistics/` = 21 `.md`; `corpus/knowledge` = 212.
  (g) `wc -l -c reports/round-39/calib/basename-couples-policy.md` → `107 5832`;
  `tail -6` ends mid-§6; `grep -c '```'`/`RESULT`/`2504` → `0`/`0`/`0`;
  draft `359` lines with 4 fences; `git log --oneline --all` on the path → single
  commit `fd55e1f`; `git show fd55e1f:… | wc -l -c` → `107 5832`.
  (h) `python3 -B reports/round-28/readme/sweep.py` → `rows 220 files 220`,
  `footer_ok True`, `readme_sha256 d2eed26b…`, exit 0.
  (i) C06 vector arithmetic → mission literal sums to `218`; correct vector
  `25/27/25/29/24/94` sums to `224`.
  (j) `sha256sum` of the load-bearing files → policy `105dfff6…e941cf`, draft
  `125ede77…a17850`, `claims.json` `513ae210…1b58`, `targets.json`
  `6db0a9eb…7b23`; `ls corpus/knowledge/linguistics/*.md | wc -l` → 25;
  `wc -c` on the draft → `19409`.
  (k) new linguistics entries' own `couples` token counts → 10/12/10/11 tokens,
  unique-basename-resolvable 10/12/9/11.
