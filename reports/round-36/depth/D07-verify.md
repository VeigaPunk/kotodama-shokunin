- Seat: D07 | verifier (claim D, independent isolated-copy verification of D03) | rebuild the archive myself and re-run D03's legs | date 2026-10-19 | baseline ce103bf

# D07 — independent verification of D03 (and of claim D's premise)

**Write scope:** this file only. All scratch work under `.scratch/{r36-d07,d07-iso,d07-r7}/`.
No in-tree byte written; no commit, push, install or network. Every number below is a
command output from an isolated `git archive ce103bf` copy I built myself — never a
re-run inside the live tree, and never `reports/round-*/run-validation.py` in-tree
(F-C13-1).

**Verdict in one line.** D03's measurements reproduce **exactly** on my own rebuild
(§2, §4), its three tamper controls reproduce with the same verdicts (§5), and its
central finding — **claim D's `before` is stale, the register-form domain is non-empty
at `ce103bf`** — is confirmed by my own independent parse (§1). One D03 number, its
component digest `0f0828731366ce52`, I could **not** reproduce from D01's filed prose
across 400+ layout variants; recorded as a named discrepancy, not smoothed (§3).

## 0. What I rebuilt, and how

| copy | command | purpose |
|---|---|---|
| `.scratch/r36-d07` | `git archive ce103bf \| tar -x` | baseline legs, my own re-derivation, tamper controls (§1, §4, §5) |
| `.scratch/d07-iso` | same + my own application of D01 §5.1/§5.2 | the assigned mission — re-run D03 §4.2 from scratch (§2, §3) |
| `.scratch/d07-r7` | same | the r7 read-set question, R03's claim (§6) |

`git status --porcelain` in-tree is `?? reports/round-36/` only, and
`git diff --stat HEAD -- reports examples corpus tools` is empty (§7): no filed byte
was edited by this seat.

## 1. Claim D's premise — falsified, independently

Claim D's `before` (`reports/round-36/claims.json:18`) reads *"Register-form domain
empty … the form class has no instances."* That is a quotation of the **r25** filed
record (`SCORECARD.md:312`) and is **false at `ce103bf`**. My own parse of the delivered
packet — text-level, no gate stdout — finds 8 register records:

| id | form | base | op | my re-derivation | match | axis | stage |
|---|---|---|---|---|---|---|---|
| L-55 | `tuum` | `tum` | lengthen | `tuum` | yes | fire | E1 |
| L-56 | `kit` | `tik` | reverse | `kit` | yes | mark | E1 |
| L-57 | `lom` | `mol` | reverse | `lom` | yes | mark | E1 |
| L-58 | `nees` | `nes` | lengthen | `nees` | yes | fire | E1 |
| L-59 | `huum` | `hum` | lengthen | `huum` | yes | fire | E1 |
| L-60 | `mees` | `mes` | lengthen | `mees` | yes | fire | E1 |
| L-61 | `reek` | `rek` | lengthen | `reek` | yes | fire | E1 |
| L-62 | `saam` | `sam` | lengthen | `saam` | yes | fire | E1 |

**8/8 match** with my own `reverse`/`lengthen` implementations; no unresolved base, no
self-base, no duplicate term. The gate's `register_scoped=14` decomposes exactly as
**8 derived forms + 6 borrowed loans** (`L-49..L-54`), which is an independent
decomposition of that counter — not a read-back of it.

**Four seats now agree by separate measurement**: D01 (`D01-design.md:23-66`), D03
(`D03-isolated-verify.md:36-78`), D05 (`D05-receipt.md:20-29`), and this seat. Claim D's
`after_required` ("register-form domain non-empty with verified forms … derivation
replay clean … law gate exit 0") is therefore **already satisfied at the baseline** by
the r26 closure (`SCORECARD.md:329`, commit `4f09c99`). Whether a round may take depth
credit for a domain closed ten rounds earlier is the parent's call; this seat supplies
the measurement, not the verdict.

## 2. The assigned mission — D03 §4.2 rebuilt from scratch

I rebuilt `.scratch/d07-iso` from `git archive ce103bf` and applied D01 §5.1 (the
`packet_keys` extension + the 8-row `doublets:` block) and §5.2 (the 8 base-side
`register_form` fields) **myself**, from the filed prose, then re-ran D03's rows:

| D03 §4.2 row | command | my result | D03's | agree |
|---|---|---|---|---|
| 1 | `assemble-culture-d4.py` | `Wrote examples/culture-d4/packet.d4.yml (103932 bytes)` | 103932 bytes | **yes** |
| 2 | `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` exit 0 | same | **yes** |
| 3 | `assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` exit 0 | 81/81 | **yes** |
| 4 | parse packet | 8 `doublets` rows `DB-01..DB-08`; 8 base records carry `register_form` | 8 rows / 8 bases | **yes** |
| 5 | `argot-derivation-gate.py` | `records=195 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` exit 0 | identical | **yes** |
| 6 | `register-law-gate.py` | `law_rows=5 identity_rows=8 record_ids=191 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0` exit 0 | identical | **yes** |
| 12 | `typed-pipeline-gate.py` | `summary: 20/20 legs passed` exit 0 (after re-pin) | 20/20 | **yes** |

The **byte count 103932 matching exactly** is the strong signal: two independent
applications of the same prose produced the same file size, the same 8-row block with
the same `plain_slot`/`register_form`/`op`/`axis` pairing, and the same leg counters.
D03 §4.2 step 4 ("`register_form` present on all 8 bases") is confirmed — my first
packet parse missed it only because the assembler re-renders the record in multi-line
form (in my `.scratch/d07-iso` copy at `packet.d4.yml:315,401,486,739,752,765,802,815`,
+277 lines vs the live tree because the added `doublets` block shifts the lexicon down);
the field is present 8 times
on the bases and 8 times in the `doublets` block.

**My own bidirectional cross-check** (not D03's): for every one of the 8 `doublets`
rows, `base.register_form == row.register_form`, `form.doublet_of == row.plain_slot`,
`form.derived_from == base.term`, `form.register == row.register`, `form.axis ==
row.axis` → **defects: none**. No duplicate `(owner, slot)`. D03 §4.1's `8/8` claim
holds.

## 3. The one number I could not reproduce — named, not smoothed

D03 §5 reports the Drafts-1+2 **component** digest as
`examples/culture-d4/components/04-lexicon.yml` → `0f0828731366ce52`, packet →
`3067107f4a8df6d3`. My own application of D01 §5.1/§5.2 produces:

```
182990b6c1282b0dc  examples/culture-d4/components/04-lexicon.yml   (mine)
9e92e995688c7fd7   examples/culture-d4/packet.d4.yml             (mine)
103932 bytes                                       (matches D03 exactly)
```

Same **length**, different **digest**. I searched the placement space
systematically — 20 top-level anchors × 8 field-insertion sites (`end`, after `axis`,
`stage`, `layer`, `field`, `route`, `evidence`, `follows`) × quoted/unquoted row
styles × 4 `packet_keys` spellings, plus pre/post newline variants (~400 combinations):
**no combination yields `0f0828731366ce52`.** D01's filed prose does not pin the exact
byte layout D03 used, so the digest is not reproducible from the evidence D03 cites.

**This is a bookkeeping gap, not a correctness failure.** Every *semantic* result
reproduces (byte count, row count, pairing, leg counters, tamper verdicts). The reading
is either that D03 applied an unreported formatting variation, or that its digest line
carries a typo. **Consequence:** D04's re-pin list must not carry `0f082873…` or
`3067107f…` as authoritative without re-measuring, and the integrator should re-derive
the digest from the actually-landed bytes. Recorded, not fixed — the digest is D03's
number, not mine to overwrite.

## 4. Baseline legs — my own runs, unmodified archive

Every row D03 §2 filed, re-run by me in `.scratch/r36-d07`:

| # | command | result | exit |
|---|---|---|---|
| 1 | `assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| 2 | `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| 3 | `argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| 4 | `argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed` | 0 |
| 5 | `register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 … findings=0` | 0 |
| 6 | `register-law-gate.py --selftest` | `selftest: 45/45 checks passed` | 0 |
| 7 | `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` (incl. `ok L3b-argot`) | 0 |
| 7b | `typed-pipeline-gate.py` (bare, no packet arg) | `summary: 16/16 legs passed` | 0 |
| 8 | `typed-pipeline-gate.py --selftest` | `selftest: 19/19 checks passed` | 0 |
| 9 | `assemble-d4-typed.py --check` | `byte-identical deterministic typed packet` | 0 |
| 10 | `assemble-d4-typed.py --selftest` | `selftest: 12/12 checks passed` | 0 |
| 11 | `d4-assembly-check-gate.py` | `byte-identical deterministic assembly` | 0 |
| 12 | `d4-typed-labels-check-gate.py` | `byte-identical deterministic projection` | 0 |
| 13 | `check-gate-battery.py` | `summary {battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}`; `originals {modified: 0, preserved: true}` | 0 |
| 14 | `replay-frozen.py --selftest` | `selftest: 79/79 checks passed` | 0 |
| 15 | `replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4 rows reproduced the recorded verdicts` | 0 |
| 16 | `d2-typed-labels.py --selftest` | `selftest: 163/163 checks passed` | 0 |

Row 7 vs 7b is worth naming: the D4 packet argument adds the D4-only legs (20/20); the
bare run is the D2 default (16/16). Both green, and D03's row 7 is the correct one for
the D4 surface.

**The two red historical manifests D03 §2.1 flagged are red for me too, and already
filed as superseded.** `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` replays
`2 mismatch, 4 reproduced` — its D4 rows pin the post-*register*, pre-*law* packet
`dd25077bc016…`, while the live packet is `aac91246cede…` (moved by the r27/r28 law and
the r30 QREG landing). This is **pre-filed**, not a new defect:
`reports/round-27/scribe/frozen-rows.md:127` records exactly this row going red "when
the law merged", and `reports/round-32/final-sweep.md:164` names it superseded. The
settled successor `reports/round-31/sweep/frozen/r31-post` is 4/4 green (row 15). I
also confirmed the frozen receipt's own pin `b749ad07cf171027` equals the live
`typed-pipeline-gate.py` digest, so the mismatch is an **input-bytes** drift, not a
tool-drift or a tampered gate.

## 5. Tamper controls — independently reproduced, same verdicts

I rebuilt D03 §3's three probes myself on my `.scratch/d07-iso` copy:

| probe | my transform | my result | exit | D03's verdict | agree |
|---|---|---|---|---|---|
| term tamper | `L-56 term: kit → kat` | `FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kat' … 'reverse' applied to 'tik' yields 'kit'; the stated inputs and rules do not yield the candidate`; `violations=1` | **1** | same finding, exit 1 | **yes** |
| domain emptied | remove the 8 `L-55..L-62` blocks | `records=187 register_scoped=0 derived_pairs=0 claimed_chains=8 borrow_pairs=0 violations=0 rule_holds=0` | **0** | `register_scoped=0`, exit 0 | **yes** |
| duplicate slot | inject `DB-09 {plain_slot: L-02, register_form: L-55, owner: L-02, slot: register-form}` | argot `records=196 register_scoped=14 … violations=0` exit 0; law `record_ids=192 … findings=0` exit 0 | 0 / 0 | no finding, both green | **yes** |

The derivation leg has **teeth** (term tamper → named FAIL, exit 1). Two honest readings
D03 named are confirmed by me:

1. **An emptied domain is silent.** With all 8 pairs removed the gate exits **0** with
   `register_scoped=0`. The `D4L-ARGOT-COVERAGE` hold is gated on that counter being
   non-zero, so removing the *records* while the register declaration survives leaves it
   at 0 and no hold fires. **This is the r25 failure mode reproduced**: a clean exit over
   an empty domain. It is exactly why claim D's `before` mattered — and it is why a
   future landing that empties the domain would not be caught by this leg.
2. **A duplicate `(owner, slot)` is silent.** The forecast's Δ2 cardinality invariant
   (one form per `(owner, slot)`) is *stated* by the `doublets` block and **enforced
   nowhere**: a concrete duplicate lands green through assemble + both register gates +
   the typed pipeline. D01 §3.3/§5.1's "no code path emits C-07" is extended by D03 and
   now by me to "a duplicate lands silently end-to-end".

Both are gate/leg work outside a verifier's write scope. Recorded, not fixed.

## 6. The load-bearing cross-claim question — R03's answer, independently confirmed

R03 (`R03-cross-review.md:17,284`) claims a D4 **component-tree** edit reddens the r7
default chain. I verified this myself in `.scratch/d07-r7`:

```
# baseline
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
            statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a95…

# after appending ONE comment line to examples/culture-d4/components/04-lexicon.yml
handoff-v3: exit=1 …
handoff-v3: E2E-DIGEST: D4 component examples/culture-d4/components/04-lexicon.yml:
            the assembler recorded ed7093d6b921… but the bytes measure 234457d358a4…

# control: the same edit to 13-register-law.yml (NOT a read-set member)
handoff-v3: exit=1
handoff-v3: E2E-DIGEST: D4 component examples/culture-d4/components/13-register-law.yml:
            the assembler recorded c0d77181ac56… but the bytes measure dffd5dec727d…
```

**Confirmed, and stronger than R03 stated.** The read set is 58 files
(`reports/round-34/handoff/declared-in-r7/expected.json#inputs` → 58 entries), and
`04-lexicon.yml` **is** a member while `13-register-law.yml` **is not** — yet **both**
edits redden the chain, because the E2E digest check reads the component's recorded
digest from the packet's own assembly block, not from the read-set roster alone. So
**any** D4 component edit that moves a recorded digest reddens the r7 default chain, and
claim D's content change certainly does. A successor freeze + renderer re-point is
mandatory (the r34 precedent), never a re-freeze of `declared-in-r7` — which
`REGIMEN.md` and `claims.json#non_goals` forbid and this seat did not issue.

## 7. In-tree integrity

```
$ git status --porcelain
?? reports/round-36/
$ git diff --stat HEAD -- reports examples corpus tools
(empty)
```

The only untracked path in-tree is this round's own directory. `.scratch/` is gitignored
(`git check-ignore -q .scratch` → ignored), so every probe above lives outside the
tracked tree. No `reports/round-*/run-validation.py` was executed in-tree; the one
attempt I made was inside an isolated `git archive` copy, where the **receipt guard
correctly refused** to overwrite the filed `reports/round-26/validation.json`
(`receipt_guard: refusing overwrite … [RECEIPT-GUARD-COMMITTED]`, exit 3) — the r14
guard working as designed. I did not force it with `REFRESH_RECEIPTS=1`; I read the
filed receipt instead, whose claim-D block carries `derived_pairs: 8`,
`register_scoped: 14`, `violations: 0`, `selftest_exit: 0`,
`typed_gate_carries_the_leg: true` — identical to my own live measurement, so the filed
r26 acceptance and my rebuild agree.

## Owed

1. **D03's component/packet digests** (`0f0828731366ce52` / `3067107f4a8df6d3`) — not
   reproducible from D01's filed prose across ~400 layout variants (§3). Owner: D03, or
   the integrator who lands the bytes. The re-pin list (D04) must re-measure rather than
   quote them.
2. **D02's route supersedes D03's rehearsal.** D02 landed with a *different* shape
   (`register_forms:` block, `D02-packet-draft.md:135`, packet `66c34ad5a4eb…`) than
   D01's `doublets` block (`3067107f4a8df6d3`). D03 §4.2's numbers are therefore a
   rehearsal of D01's route, **not** of the route D02 proposes to land. Which route the
   integrator takes changes the re-pin list; both are internally consistent.
3. **The two unenforced invariants** — the empty-domain clean exit (§5.1) and the silent
   duplicate-slot row (§5.2). Gate/leg work, outside a verifier's scope. Owner: whichever
   seat owns gate changes, or a future round.
4. **Claim D's verdict** — `after_required` is satisfied at the baseline by the r26
   closure (§1); the claim's own counting command is a round runner this seat may not
   execute. Whether claim D verifies as declared or must be re-scoped to the genuinely
   open surface (D01/D02's `doublets`/`register_forms` block) is the parent's decision.
5. **The r7 successor freeze** (§6) — required by any accepted content landing; the
   new-row draft is D04's, not this seat's.

## Citations

**Files read (in-tree, `ce103bf`)**
- `REGIMEN.md`; `reports/round-36/{claims.json:18-20,targets.json}`;
  `reports/round-36/telemetry/{dispatch-declared,availability-attempt-1}.json`
- `reports/round-36/depth/D01-design.md:23-66,236-296` (the drafts I re-applied);
  `reports/round-36/depth/D02-packet-draft.md:135,280,326-379` (the alternate route);
  `reports/round-36/depth/D03-isolated-verify.md` (the file under verification);
  `reports/round-36/depth/D05-receipt.md:20-64`
- `reports/round-36/review/R03-cross-review.md:17,19-29,284` (the r7 claim I re-tested)
- `reports/round-25/argot/{current-state.md:74-88,delta.md:27,155,206,330}`; `SCORECARD.md:312`
- `reports/round-26/register/{forms.md:25-48,repin.json}`; `reports/round-26/validation.json`
  (claim-D block: `derived_pairs 8`, `register_scoped 14`, `violations 0`)
- `reports/round-27/scribe/frozen-rows.md:127,155-158`; `reports/round-32/final-sweep.md:164`
- `reports/round-34/handoff/declared-in-r7/{expected.json,freeze.txt}` (58-file read set)
- `examples/culture-d4/packet.d4.yml:290,1009-1183,1329` (lexicon, the 8 register
  records `L-55..L-62`, `registers:` — the live tree carries **no** `doublets:` key;
  the `doublets:` line numbers quoted in §2 are of my modified copy under `.scratch/`);
  `examples/culture-d4/components/{04-lexicon.yml:14,156,165,173,199,200,201,205,206,13-register-law.yml}`;
  `examples/culture-d4/typed-labels.d4.yml` (the 8 forms typed `native-form`, `route: derived`, era E1)
- `tools/assemble-culture-d4.py` (`PACKET_KEYS`/`RECORD_FIELDS`);
  `tools/gates/{argot-derivation-gate.py,register-law-gate.py,typed-pipeline-gate.py:84,517-541,typed-pipelines.json}`;
  `tools/gates/frozen/round-26/post-register/{MANIFEST.tsv,freeze-receipt.json}`;
  `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv`; `tools/exercise-handoff-e2e.py` (V3_READ_SET)

**Commands** — all run in the isolated copies named in §0, tabulated verbatim in §1, §2,
§4, §5, §6. Digests by `sha256sum`; integrity by `git status --porcelain` and
`git diff --stat HEAD -- reports examples corpus tools`.

**Scratch (gitignored, not evidence by itself)**: `.scratch/{r36-d07,d07-iso,d07-r7}/`.

**Canon**: NON-CANON. This file records an independent engineering verification and its
measurements; it makes no promotion, canon, clearance or closure verdict.
