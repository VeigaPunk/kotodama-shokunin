- Seat: X02 | critic | cross | date 2026-10-19 | baseline ac47c78

# X02 — honesty review of both r42 blocks

Scope: every claim in `reports/round-42/claims.json` (O and C), the mission text in
`reports/round-42/targets.json`, and every r42 seat fragment landed at this seat's
close (`op/O02,O03,O04,O06,O07,O08,O09,O10`, `scout/K01`, `cov/C02,C08`,
`review/R02`, `scribe/S02`, `adj/A01`, `calib/Ca01`, `plan/P01`). Every number below
was re-derived by this seat on the live tree at `ac47c78`
(`git rev-parse HEAD` = `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`; `git status
--porcelain` = `?? reports/round-42/` only). All commands read-only, lane root,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; no filed byte edited, no
`reports/round-*/run-validation.py` executed anywhere, no git/network/install.

## Verdict

The **before-states verify** and the wave's **negative results are honest** — several
seats filed findings against their own chartered work (O04's §4 kills the fix it was
sent to verify; O08 refuses a re-class; O03 self-reports a peer divergence). Two
independent implementations plus mine converge on the same corrected census.

But the **declared claims carry three defects the seats largely caught and the receipt
must not smooth over**: (X02-1) claim O's named fix host and cited "policy arithmetic"
are not both present in the filed artifact it names; (X02-2) claim O's threshold "the
wrapped field reads 4/4 targets" is unachievable as chartered and conflates extraction
with resolution; (X02-3) claim C's declared footer vector sums to 218 against its own
declared total 224. One filed artifact was also edited in place after its commit
(X02-4), and one seat mis-attributed a digest (X02-8). Neither claim's after-state is
established: claim O has no landed fix, claim C has 1 of 4 entry drafts. **No axis is
improved at this cut; both claims are `unprovable`/`could-not-evaluate` pending
landing.**

## Independently reproduced by this seat (my own commands, not inherited)

1. **Digests.** `sha256sum reports/round-42/{claims,targets}.json` =
   `513ae210…1b58` / `6db0a9eb…7b23` — both equal the `durable_sources` pins in
   `telemetry/dispatch-declared.json:15-24`; that file itself =
   `50d29b3f…aff4`. All three match.
2. **Wrapped-field census.** My own scan of all 220 entries for a `- couples:` field
   with continuation lines returns **exactly 1**:
   `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (5 continuations).
   Confirms Ca04 D1 and O09/O04/O07/O08/O10/K01.
3. **The r39 arithmetic reproduces byte-exact at `dfb0719`.** I extracted the r39 tree
   (`git archive dfb0719 corpus/knowledge`) — **212** entries — and re-ran the
   single-line extractor with the policy's two-tier resolver:
   `2504 = 2335 direct + 163 fallback + 0 ambiguous + 6 unresolved`. Block/rule-D:
   `2508 = 2337 + 163 + 0 + 8`. At `ac47c78` (220 entries): single-line
   `2607 = 2435+166+0+6`, block `2611 = 2437+166+0+8`. Every figure matches O03 §6,
   O04 §5, O07 §3, O08 §3, O10 §4 exactly.
4. **Rule D reads `tone-prosody.md`; rules B/C emit the phantom `prosody.md`.** The
   `:76-77` break falls inside the filename. Confirms O07 §2, O10 §1, O04 §4, O08
   §2.4, R02 item 3, O03 §5.
5. **Claim C before-state.** `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **23**;
   `find corpus/knowledge -name '*.md' | wc -l` → **220**; live vector
   `25/23/25/29/24/94`. `python3 -B reports/round-28/readme/sweep.py` → exit **0**,
   `rows 220 files 220`, `readme_sha256 d2eed26b…`.
6. **O08's filed-byte observation confirmed.** `git show
   13a1657:reports/round-40/op/defect-queue-v2.json | sha256sum` = `fe596a9d…`;
   live file = `dfc9265d…`; `git diff 13a1657 ac47c78 --stat` on it = `15 insertions,
   5 deletions`.
7. **C02's entry-2 citations are honest.** I spot-checked 12 of its `path:line`
   anchors (`symbolism-synthesis-method.md:40,48,68`; `animal-symbolism.md:46,69`;
   `plant-symbolism.md:20`; `death-afterlife-eschatology.md:49`;
   `ritual-liminality.md:57`; `direction-symbolism.md:25`;
   `bathing-and-body-hygiene.md:50`; `israel-ancient-hebrew.md:150`; `inuit.md:140`;
   `cuisine-food-lexicon.md:74`; `ritual-garments.md:62`;
   `eschatology-world-end-systems.md:105`; `politeness-taboo-euphemism.md:73`) —
   every one resolves and says what C02 claims. Its target
   `myth-symbol/purity-pollution-systems.md` does not yet exist (proposed).

## Findings

### X02-1 — claim O's named fix host and its cited arithmetic are not both in the filed artifact it names (high)

`claims.json:16` (O `after_required`) names the host as *"likely the r39 C12 runbook's
resolver or a tools/harness couples checker"*; `claims.json:18` (`thresholds`) requires
*"the corrected census reproduces the r39 policy's arithmetic minus the phantoms"*.
Filed facts, each re-measured this seat:

- `reports/round-35/cov/C12-audit-runbook.md` is a **runbook document** — its pointer
  family (§2) is about backticked repo paths, not couples resolution (K01's finding;
  I confirmed by grep). It contains no couples resolver.
- `tools/` carries **no** couples resolver: `grep -rln couples tools/ --include='*.py'`
  → only `tools/gates/provenance-audit.py` (field-presence only) and
  `tools/source-audit-inventory.py`.
- The landed `reports/round-39/calib/basename-couples-policy.md` **contains no
  arithmetic at all** (X02-5): `grep -c 2504` = 0, `grep -c 2335` = 0.

So the claim's named host is not identifiable from filed bytes, and the "policy
arithmetic" it must reproduce lives only in the r39 *authoring draft*
(`Ca03-basename-policy.md:35-36`) and in filed r39 records — not in the artifact the
claim names. The wave correctly found the live host elsewhere
(`tools/gates/provenance-audit.py:244-260`, rule C, `" ".join` at `:259`; O10 §2, R02
item 4), **but that gate does not tokenize `couples`** (its finding is `empty-couples`
only) — it is the host of the *block-extraction defect*, not of the *census*. An honest
receipt must keep those two roles distinct rather than naming one host for both.

### X02-2 — "the wrapped field reads 4/4 targets" is unachievable as chartered and conflates two readings (high)

`claims.json:18` sets the threshold *"the wrapped field reads 4/4 targets"*, while the
same claim's `before` (`:14`) says *"4 named, 2 phantom"* — i.e. only **2** of the 4
tokens name existing files. Measured, the field yields 4 **tokens**, of which
`sound-symbolism.md` and `writing-systems.md` exist (`direct`) and `sound-change.md` +
`tone-prosody.md` do not (`unresolved`, prospective seeds):

- read as **resolution**, 4/4 is unsatisfiable by any fix — a verifier would fail a
  correct tool;
- read as **extraction**, 4/4 is met by the obvious space-join parser that still
  mangles `tone-prosody.md` into the phantom `prosody.md` — a false green.

Both readings are traps; the claim text does not disambiguate. Confirmed independently
by O04 §4, O07 §2, O08 §2.4, O10 §1, R02 item 5, O03 §5. The receipt must state the
threshold as *4 of 4 tokens captured, and `prosody.md` never emitted*.

### X02-3 — claim C's declared footer vector is arithmetically wrong (high)

`targets.json` seat C06 declares the README rev-2.4 delta as *"myth-symbol 27, totals
224, vector 25/23/27/25/24/94"*. In README section order
(`linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`;
`reports/round-28/readme/sweep.py:50-57`), `25/23/27/25/24/94` sums to **218**, not 224;
the literal vector moves **culture-material** 25 → 27 and leaves myth-symbol at 23 —
contradicting the same sentence's *"myth-symbol 27"*. The correct vector is
`25/27/25/29/24/94` (sum **224**). Independently found by C08 §5 (its D1) and R02.
Applied literally, the sweep's `footer_dir_totals` leg goes red (the `--selftest`
control "stale footer dir vector flagged" is exactly this class).

### X02-4 — a filed artifact was edited in place after its commit (medium)

The r40 queue `reports/round-40/op/defect-queue-v2.json` hashes `fe596a9d…` at its own
commit `13a1657` but `dfc9265d…` at HEAD; `ac47c78` (r41) changed it 15+/5− to flip
`N7-receipt-fidelity` and `r39-runner-root-regression` to `fixed-with-evidence` and
append an `r41_update` block. The queue's own notes assert the filed bytes are untouched
and r41's X00 named the filed r40 queue immutable with a successor required. O08 filed
this as Observation 3; I confirm it independently. This bears directly on claim O's
queue-update leg: a re-class written into that path is not durable in the way the
queue's own notes assume.

### X02-5 — the landed r39 policy is truncated at its §6 header (medium)

`reports/round-39/calib/basename-couples-policy.md` is **107 lines / 5832 bytes** and
ends at `...PYTHONDONTWRITEBYTECODE=1\`):` — its §6 lead-in. Measured: `grep -c '```'`
= 0, `grep -c RESULT` = 0, `grep -c 2504` = 0; no §6 script, no §7. The authoring draft
`Ca03-basename-policy.md` is **359 lines / 19409 bytes** and carries all of them. The
policy landed in one commit (`fd55e1f`), so this is a landing defect, not a later edit.
Independently found by O03 §9. Consequence: queue row `r39-basename-successor-instrument`'s
`next_touch` and any receipt text that cites "the policy's §6 recipe" cite a recipe
absent from the landed bytes.

### X02-6 — O03 §4's class prose contradicts O03's own §6 arithmetic (medium)

O03 §4 asserts the wrapped field's two live tokens are `fallback` "because
`corpus/knowledge/linguistics/` held only 21 entries at r39 close". Tier 1
(`basename-couples-policy.md` §2) is satisfied by **any** existing file at
`<entry dir>/<token>`, whatever the partition's entry count. I verified at `dfb0719`:
`sound-symbolism.md` and `writing-systems.md` **exist** in
`corpus/knowledge/linguistics/` → both `direct`, matching O03's own §6 `direct=2337`
(+2 direct) and §8 item 2. O03's numbers are right; its §4 prose is wrong. It also says
"24 at HEAD" where the live partition is **25**. An integrator quoting O03 §4 verbatim
would import a false class label. O04 §7 Divergence 1 caught this; I confirm it.

### X02-7 — O03 §8 acceptance item 6 is a false-green test (low)

O03 §8 item 6 reads: *"Any landed tool reporting a wrapped-field count of 2, **or
reading `sound-symbolism.md`/`writing-systems.md` as `direct` at `dfb0719`**, is
reproducing C14's blank-line-blind `fields_of`…"*. The second clause is inverted — those
two files exist at `dfb0719`, so `direct` is the **correct** result; a verifier applying
it literally would fail a correct tool. O04 §7 Divergence 2 caught this; I confirm it.

### X02-8 — a digest is attributed to the wrong path (low, citation integrity)

O04's Citations (`op/O04-verify.md:327`) pins the policy under test as
`reports/round-39/calib/basename-couples-policy.md` with *"sha256 `125ede77…`"*. That
digest is the **draft** `Ca03-basename-policy.md`
(`sha256sum` → `125ede77e3f5…7850`); the landed policy is `105dfff6c667…941cf`
(`sha256sum` → confirmed; O06 §1 pins the correct value, O07:279 attributes
`125ede77…` to the draft). A digest attributed to the wrong path makes "the policy
says X" unverifiable — the same class of defect the lane's digest discipline exists to
catch.

### X02-9 — "the fix host is unresolved" understates the wave's own finding (low)

O04 (its Owed and `:324-328`) and O09 §2 state `tools/` carries no couples resolver and
that the durable host is unresolved. True of a *resolver* — but O10 §2 and R02 item 4
located the **live block-extraction host** `tools/gates/provenance-audit.py:244-260`.
The receipt should reconcile "no resolver exists" with "the live block reader is
`provenance-audit.py`", rather than reading as if no live host exists.

## Round-level honesty assessment

- **What the wave got right, on record:** every seat that lacked a dependency said so
  rather than inventing one (O03, O04, O06, O09, C02, C08 all label in-flight/absent
  state). O04's §4 is a negative result against its own chartered fix. O08 refuses the
  `fixed-with-evidence` re-class with reasons. O03 self-reports a peer divergence. S02's
  telemetry draft labels every sample **partial** and keeps `launched_workers` /
  `completed_workers` / `failed_workers` / `runtime_concurrency` `null` with owners
  rather than inferring 32/32/0 — I confirm no `validation.json` exists and the declared
  digests match. This is the honesty posture the regimen asks for.
- **What the receipt must not smooth:** X02-1, X02-2, X02-3 are defects in the *mission
  text*, not in the seats. The seats largely caught them; the integrator must not let
  "4/4 targets" or the vector `25/23/27/25/24/94` survive into the filed receipt or the
  README delta.
- **Axis honesty:** neither claim's after-state is established — claim O has no landed
  fix (no `op/O01-fix-draft.md` at any cut; no durable fixed extractor), claim C has 1
  of 4 entry drafts and no C06 delta. So **no axis may be judged improved** at this cut;
  the honest interim verdict is `unprovable` (O) and `could-not-evaluate` (C) pending
  landing and an isolated acceptance run. A round that reported `improved` here would be
  claiming an after-state that does not exist.

## Owed

- **Integrator:** fix claim C's declared vector to `25/27/25/29/24/94` before drafting
  the README rev-2.4 delta; restate claim O's threshold as "4 of 4 tokens captured and
  `prosody.md` never emitted"; record X02-1 (host/arithmetic not both filed), X02-4
  (queue edited in place), X02-5 (policy truncated at §6), X02-8 (digest
  mis-attribution) as defect rows rather than letting them vanish into the receipt.
- **Independent verifier:** reproduce X02-2's two-reading trap on the *landed* fix once
  `op/O01-fix-draft.md` exists — no landed patch existed at any cut of this seat.
- `to-verify` (not verifiable by me): whether `tone-prosody.md` is the intended token
  (a reading of `:76-77`, not provable from filed bytes) — O04/O07/O10 concur.
- `to-verify`: the fallback movement 163 → 166 (+3) is measured at the two trees but
  not decomposed (O08's `to-verify`); I confirm the two values, not the attribution.

## Citations

- Claim text: `reports/round-42/claims.json:14,16,18` (O before/after/thresholds),
  `:20-22` (C); `reports/round-42/targets.json` seats `C06` (the vector mission text),
  `O03`, `O04`, `X02` (`cross/X02-honesty.md`).
- Baselines/digests: `git rev-parse HEAD` → `ac47c786…b4`; `sha256sum
  reports/round-42/claims.json` → `513ae210…1b58`; `…/targets.json` → `6db0a9eb…7b23`;
  `…/telemetry/dispatch-declared.json` → `50d29b3f…aff4`.
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (`:76`
  ends `tone-`, `:77` begins `prosody.md`); `:279` (the same two names in prose).
- Extractor hosts: `reports/round-19/audit/entry-audit.py:75`;
  `reports/round-27/audit/entry-audit.py:275`;
  `reports/round-35/cov/C14-audit-6-10.md:229-236`;
  `tools/gates/provenance-audit.py:244-260` (`:259` the `" ".join`), `:76` (single-line
  field regex, no tokenizer).
- Policy: `reports/round-39/calib/basename-couples-policy.md` (107 lines, sha
  `105dfff6…941cf`; truncated at §6 lead-in, `:104-107`);
  draft `reports/round-39/calib/Ca03-basename-policy.md` (359 lines, sha `125ede77…7850`,
  `:35-36` the arithmetic). `reports/round-39/calib/Ca04-verify.md` (D1, `:29-31`
  arithmetic, `:107-115` owed).
- Queue: `reports/round-40/op/defect-queue-v2.json:362-369` (N6 row);
  `git show 13a1657:… | sha256sum` → `fe596a9d…`; live → `dfc9265d…`;
  `git diff 13a1657 ac47c78 --stat` → `15 insertions(+), 5 deletions(-)`.
- Claim C state: `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 23; `find
  corpus/knowledge -name '*.md' | wc -l` → 220; `python3 -B reports/round-28/readme/sweep.py`
  → exit 0, `readme_sha256 d2eed26b…`; `--selftest` → 12/12.
- Peer fragments cross-checked: `op/O02-controls.md`, `op/O03-predicted.md` (§4 vs §6/§8
  contradiction), `op/O04-verify.md` (`:324-328`, `:327` digest, §4/§5/§7),
  `op/O06-receipt.md` (§1 pins), `op/O07-gap-fill.md` (§2, `:279`), `op/O08-queue-update.md`
  (§2-§4, Obs. 3), `op/O09-scribe.md` (§2), `op/O10-gap-fill.md` (§1-§4),
  `scout/K01-n6-scout.md` (host), `cov/C02-entry-2.md` (12 anchors re-read),
  `cov/C08-verify.md` (§1, §5 D1), `review/R02-review.md` (items 3-6),
  `scribe/S02-telemetry-draft.md` (§1-§3), `adj/A01-entries-bleed.md`,
  `calib/Ca01-gap-fill.md`, `plan/P01-plan.md`.
- Command outputs (this seat, 2026-10-19, lane root, `TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`, all read-only): (a) `git archive dfb0719 corpus/knowledge`
  → 212 entries; (b) three-mode recount at `dfb0719` →
  `single 2504/2335/163/0/6`, `newline 2508/2337/163/0/8`, `hyphen 2508/2337/163/0/8`;
  (c) wrapped-field scan → 1 field / 5 continuations; (d) rule probe on `:72-77` →
  A `[]`, B/C `prosody.md…`, D `tone-prosody.md…`; (e) `sha256sum` of the policy files
  and the queue at `13a1657` vs live; (f) `wc -lc` + fence/`2504` counts on the landed
  policy; (g) Tier-1 existence probe at `dfb0719` for the 5 candidate basenames;
  (h) the 12 C02 anchor reads. No filed byte edited; no `run-validation.py` executed;
  nothing staged under `corpus/`; no git/network/install.
