# R26-D25 — capability-row draft: the register stratum

- round: 26 (operator: loop 3 of 3, build round 2 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R26-D25** (D-scribe 1 of 4).
- claim under draft: `reports/round-26/claims.json` claim **D**, axis `depth`,
  capability `register-stratum`.
- date: 2026-10-18. Declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (`claims.json:5`). Lane HEAD at every measurement below
  `1ad491a1a4b0aef9ebdc1861dfb8237727503825`, `git status --porcelain` clean at
  the opening read (18:00:34Z) and carrying only round-26 in-flight evidence at
  the closing reads.
- **status: DRAFT ONLY — the orchestrator admits.** This seat edits no
  `SCORECARD.md`, no `SKILL.md`, no `LOG.md`, no tool, gate, example, component
  or packet. Everything below is proposed text plus read-only receipts.
- writes: this file only, plus gitignored scratch under `.scratch/r26d/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  commit, no push. No filed artifact of rounds 8–25 was modified.
- canon: **NON-CANON engineering evidence.** A capability row records a
  demonstrated run; it is not canon, not lore acceptance, not a clearance and
  not a real-world etymology check.

## 0. Verdict at this seat's stamp — read this before the row text

**The register stratum is NOT on disk at 2026-10-18T18:05:17Z, and the row in
§3 is therefore NOT landing-ready.** The claim's `after_required` is a
conjunction of six legs; **four are measured unmet**, one is met, and one is
met in a narrower form than the claim words. The measurement is not a judgement
about the D seats — the 28 D workers were live and their scratch is visible
(`.scratch/r26-d-reg/`, `-d13`, `-d17-d20`, `-d21`, all stamped 18:02–18:05Z) —
it is a statement about what the tree carries.

| # | `after_required` leg (`claims.json:14`) | measured | evidence |
|---|---|---|---|
| 1 | components **declare register-scoped forms** with machine-readable derivation rules (`head2`/`reverse` or designed equivalents) | **NOT MET** | `registers:` / `doublets:` / `doublet_of` / `#plain` / `#quote` → **0** files under `examples/` and **0** under `tools/` (measured 18:03:17Z and re-measured 18:05:08Z) |
| 2 | the packet **regenerates deterministically** | **MET (pre-existing)** | `python3 tools/assemble-culture-d4.py --check` → exit 0, "byte-identical deterministic assembly"; `--selftest` 81/81 |
| 3 | **typed labels classify the register forms** per the label-typing table | **MET (pre-existing)** | `examples/culture-d4/typed-labels.d4.yml:31-35` → `labels_by_kind {native-form 56, translated-label 12, borrowed-strata 6}`; `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` exit 0, 0 findings |
| 4 | the **argot leg REPLAYS the register derivations** and finds them clean | **NOT MET as worded** | the leg runs and is wired, but over D4 it reports `derived_pairs=0` over `register_scoped=6` — it replays **no register derivation**, because leg 1 never landed a `derived_from`/`derivation` pair to replay |
| 5 | the **D4 typed gate passes with the hold set updated and named** | **PARTIAL** | gate exit 0, 20/20 legs (source) and 17/17 (typed), but the hold set is **unchanged** at 12/0/0 and carries no `D4L-REGISTER-UNRESOLVED` row — nothing was updated because nothing landed |
| 6 | the **round-17 forecast is marked delivered with the delta closed** | **NOT MET** | `reports/round-25/argot/delta.md:1` still reads "the round-17 argot-derivation forecast is **not delivered**", and no round-26 artifact contradicts it |

Two legs of the claim's `after_required` are additionally **not reachable from
the delivered packet as it stands**: §4 shows that the six register-scoped
records the argot leg actually finds are *contact roads, loan layers, loans and
symbols* — not the quote-register forms the forecast designs — so a
`derived_from`/`derivation` pair planted on them would be a derivation over a
base that is not a form. That is the honest form of the gap and it is named in
§4, not smoothed.

## 1. What the row would assert — and what it must not

The row records a **capability**: a register-scoped form whose derivation from
a stated base is declared in the packet's own machine-readable schema and
replayed by a gate that can compute the declared operation, with a negative
control proving the relation can fail. It is not a claim that any register form
is a good name, that the register design is sound, or that the stratum is
complete.

**Admission gate.** The claim requires the stratum "landed in D4 end-to-end".
At 18:05:17Z it is not landed: the schema carries no relation field, the packet
carries no register pair, and the only register-scoped derivations on disk are
the ones this seat planted in scratch (§5). The row below is therefore
**prospective** — written so the orchestrator can see the exact text a
successor round would land, with every cell it must re-measure marked.

**One capability IS newly admitted by this round's bytes and belongs in the
table.** The round-25 lesson's closeout listed as unmet: "the D leg is **wired
into the D4 typed gate** … the gate that was to grow the leg does not invoke
it". That is now **false**, and the correction is measured: the gate at
`fc13cd2` (the round-26 declared baseline) already carries an `L3b-argot` leg
(`tools/gates/typed-pipeline-gate.py:517-541`) that invokes the sibling by
single input, folds its `FAIL` lines into the verdict as `D4L-ARGOT-DERIV`, and
prints `ok L3b-argot` on both the D4 source and the D4 typed run. §3.2 is the
row for **that** capability — it is landing-ready today.

## 2. Pin surface at this seat's measurement (all `sha256sum`, cwd = lane root)

Measured 2026-10-18T18:05:08Z unless a row names its own stamp. These are the
digests the register row will have to pin; **every one moved between the
round-25 drafts and now**, which is the reason no round-25 pin may be inherited.

| artifact | sha256 | note vs the round-25 draft |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` | round-25 drafts pinned `07db6e9b…`; **moved** |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | round-25 settled `879d40bf…`; **moved**, and this is the digest at the declared baseline `fc13cd2` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | unchanged |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | unchanged |
| `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | unchanged |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | unchanged |
| `examples/culture-d4/packet.d4.typed.yml` | `ffece0feb52c5b0b8ae6b0f8c1848d6220ad2dc2b36b1faac6385d62f4bfd84e` | unchanged |
| `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` | unchanged |
| `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` | unchanged; counts 12/0/0 |
| `tools/gates/typed-pipelines.json` | `396f4678133ad3223752c27d7153fdff06945abfa49137a307e10ef6e29b44d0` | unchanged; its `d4` profile pins the **live** `typed-pipeline-gate.py` at `879d40bf…` → **stale** (§6) |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | matches the profile pin |
| `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` | matches the profile pin |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` | matches the D4 expected-holds pin |
| `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` | — |
| `tools/gates/fixtures/argot-derivation-gate.expected` | `38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018` | — |

**Re-pin obligation.** Any edit to the argot gate, the typed-pipeline gate, the
projector, the adapter or the packet after this seat's stamp moves these pins.
Re-run the §5 commands at integration and re-pin before citing any digest here.

## 3. LANDING-READY text

### 3.1 SCORECARD "Capabilities" row — register stratum (**NOT landing-ready**)

Intended surface: `SCORECARD.md` §Capabilities, whose columns are
`name | demonstrated behavior | command / evidence | first working`. **Do not
land this row at this round's stamp**: its own evidence cell would have to say
`derived_pairs=0`. The row text is filed so a successor round lands a corrected
version rather than re-deriving it.

```markdown
| register-stratum derivation (D4) | A register-scoped form declares its base and its operation in the packet's own schema (`derived_from` + `derivation`, or the packet's machine-readable `pattern`/`output` rule); the argot leg replays every such pair against the declared operation and reports `derived_pairs`/`violations`; a form the stated inputs and rules do not yield is `D4L-ARGOT-DERIV` FAIL, an unreplayable declaration is `D4L-ARGOT-RULE` HOLD, and a declared-but-undelivered relation is `D4L-ARGOT-COVERAGE` HOLD; the typed pipeline's `L3b-argot` leg folds any argot FAIL into the D4 verdict, so a broken register derivation cannot read green | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`; `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` (exit 0, 20/20 legs incl. `L3b-argot`); `python3 reports/round-26/run-validation.py` | round 26 (declared round 17 as forecast — `reports/round-17/d4/design-brief.md:296-310`; delta `reports/round-25/argot/delta.md`; **the row is provisional until `derived_pairs > 0`**) |
```

Three obligations for whoever lands it:

- The row **must** carry the `derived_pairs > 0` condition. Omitting it would
  let a reader conclude the stratum was exercised when the leg's own coverage
  line says otherwise — the round-25 row's `zero-rows-by-design` clause is the
  precedent, and this row is the mirror case (a clause that says *not* zero).
- The row **must** name the leg's honest scope, which the gate states in its own
  docstring: exit 0 means "every register-scoped form that states its inputs
  re-derives", never that the stratum is complete or that a hold elsewhere is
  closed.
- `first working` must not read "round 17": round 17 filed a forecast and
  `reports/round-25/argot/delta.md` measures it undelivered. A capability whose
  first working round is claimed must name the round whose bytes carried it.
- **The claim's `counting_command` had no receipt at this seat's close.** Measured
  18:11:49Z: `python3 reports/round-26/run-validation.py --selftest` → **29/29,
  exit 0**, but `--check` → **exit 2** with `could-not-evaluate: SameFileError:
  …/reports/round-26/adjacency.md and …/reports/round-26/adjacency.md are the
  same file` (reproduced at two stamps and two runner digests, `1096269f…` and
  `1f74a85f…`). **No `reports/round-26/validation.json` exists**, so the row's own
  evidence cell cannot yet cite the counting command. That is an obstacle the
  parent must disposition, and this seat did not edit the runner.

### 3.2 SCORECARD "Capabilities" row — argot-derivation wiring (**landing-ready today**)

This row records the capability the round-26 bytes actually demonstrate: the
argot leg is not merely on disk, it **grades the D4 verdict**. It is the
correction of the round-25 closeout's "the gate that was to grow the leg does
not invoke it".

```markdown
| argot-leg wiring (D4 typed pipeline) | The typed-pipeline gate invokes the argot-derivation sibling as a graded leg (`L3b-argot`) over the same single input, folds every `FINDING D4L-ARGOT-DERIV … FAIL` line into the run's finding set as a `fail`, and prints `ok L3b-argot` only when the sibling exits 0 or 1 with no FAIL line — so a register derivation whose stated inputs and rules do not yield the form fails the D4 verdict instead of being reported beside it; the leg is guarded on the generalized path, so the D2 default run keeps its pre-round-25 output byte for byte | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0, 20/20 legs, `ok L3b-argot`; `… examples/culture-d4/packet.d4.typed.yml` → exit 0, 17/17, `ok L3b-argot`; `--selftest` 19/19 (mirrored sibling selftest green + mirrored-leg-runs control); `python3 reports/round-26/run-validation.py` | round 25/26 boundary — the leg is present at the round-26 declared baseline `fc13cd2` (`tools/gates/typed-pipeline-gate.py:517-541`); round 25's closeout recorded it as absent, and this row is the correction |
```

- The row **must not** claim the leg discriminates *on D4*: it discriminates on
  its fixture (4 planted `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE`) and on scratch
  controls (§5), while the delivered packet exercises it vacuously. The row's
  wording above is deliberately about **wiring**, not about the register domain.
- "round 25/26 boundary" is honest and matches the D2 row's "round 3; selftest
  supplement-opencode-1" pattern (`SCORECARD.md:46`): the artifact is present at
  the round-26 declared baseline and absent from the round-25 closeout's reading.

## 4. The load-bearing measurement — what the six register-scoped records are

The argot gate reports `register_scoped=6` over D4. Enumerated by calling the
gate's own `record_blocks()` / `record_register()` / `record_id()` (this seat,
18:04:11Z, scratch under `.scratch/r26d/`), those six are:

| block | id | form | register | why it is scoped |
|---|---|---|---|---|
| `lexicon` | `L-49` | `sal` | trade | `loan_layer`/`layer` resolves to `LY-01`, whose `register: trade` |
| `lexicon` | `L-50` | `kar` | trade | same layer |
| `lexicon` | `L-51` | `gul` | trade | same layer |
| `lexicon` | `L-52` | `res` | trade | same layer |
| `lexicon` | `L-53` | `gal` | craft | `LY-02`, `register: craft` |
| `lexicon` | `L-54` | `mar` | craft | same layer |

Three facts follow, and they are the reason leg 4 of §0 is unmet **as worded**
rather than merely unimplemented:

1. **None of the six is a quote-register form.** They are the six loan records
   of the two contact layers. The forecast's argot — a quote register whose
   forms derive from plain bases by `head2`/`reverse` — has no representative
   here. This is the round-25 delta's root cause restated at the byte level:
   the culture that hosts the argot is not the culture that shipped
   (`reports/round-25/argot/delta.md` §1.2, path A).
2. **The gate reaches them through the layer, not through a `register` field on
   the record.** `record_register()` reads `entry["register"]` first and falls
   back to resolving `loan_layer`/`layer` against the declared `layers` block
   (`tools/gates/argot-derivation-gate.py:293-317`). So the six are
   *register-scoped by loan layer* — a real reading, and a different one from
   the forecast's slot-scoped reading.
3. **A `derived_from`/`derivation` pair planted on any of them would be a
   derivation over a base that is not a form.** `sal`, `kar`, `gul`, `res`,
   `gal`, `mar` are underived loan roots; their "derivation" is the borrow
   substitution, which the gate already replays as the `borrow_pairs=6` leg. The
   register derivation the claim wants needs *new records*, not new fields on
   these six.

Also measured: `packet_declares_ops(packet)` returns `[]` over the delivered
D4 packet — `morphology.derivation_rules` carries `CX-01/02/03` but nothing
declares an argot operation, so the `D4L-ARGOT-COVERAGE` hold the gate can emit
does **not** fire on D4. `grep -n "derivation_ops\|head2\|reverse"
examples/culture-d4/packet.d4.yml` → no hits. A reader who assumed the coverage
hold was firing would be reading a hold that the delivered bytes do not earn.

## 5. Measured controls (this seat, 2026-10-18T18:02–18:05Z)

Scratch only, `TMPDIR=$PWD/.scratch`, the delivered tree untouched. Four packets
built by copying `examples/culture-d4/packet.d4.yml` and injecting register
records at the head of the `lexicon` block.

**(a) The relation replays and can fail — the control the claim's leg 4 needs.**
Three correct register pairs (`saalu`←`head2`(`saalumi`), `nim`←`reverse`(`min`),
`suk`←`reverse`(`kus`)) injected into the real packet:

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/argot-derivation-gate.py .scratch/r26d/ctl/reg-ok.yml    # exit 0
python3 tools/gates/argot-derivation-gate.py .scratch/r26d/ctl/reg-bad.yml   # exit 1
python3 tools/gates/argot-derivation-gate.py .scratch/r26d/ctl/reg-rule.yml  # exit 1
```

| control | mutation | exit | coverage line |
|---|---|---|---|
| baseline | none (delivered packet) | 0 | `records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| **CTL-A** `reg-ok.yml` | 3 correct register pairs added | **0** | `records=159 register_scoped=9 derived_pairs=3 … violations=0` |
| **CTL-B** `reg-bad.yml` | `nim` mutated to `min2` | **1** | `… derived_pairs=3 … violations=1` |
| **CTL-C** `reg-rule.yml` | `derivation: ARGOT-NOSUCH` | **1** | `… derived_pairs=1 … rule_holds=1` |

CTL-B's exact line:

```
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-02 'min2' (register 'quote'): declared chain 'reverse' applied to 'min' yields 'nim'; the stated inputs and rules do not yield the candidate
```

CTL-C's exact line:

```
FINDING D4L-ARGOT-RULE: HOLD — register-scoped form Q-09 'xel': declared derivation 'ARGOT-NOSUCH' is neither a declared argot operation (head2, reverse) nor a licensed packet rule (CX-01, CX-02, CX-03); replay is not possible
```

So the leg is live, discriminating and correctly typed **on a D4 packet** — it
simply has no delivered pairs to grade. This is the strongest available
evidence that the round-26 gap is a **domain** gap, not an engine gap, and it is
what makes §3.1's `derived_pairs > 0` condition the right landing gate.

**(b) The gate's own fixture, and its selftest.**

```sh
python3 tools/gates/argot-derivation-gate.py --selftest        # 21/21, exit 0
python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml
# exit 1; 4× FINDING D4L-ARGOT-DERIV + 1× FINDING D4L-ARGOT-RULE; stdout sha256 556d31d6f66715cb…
```

The fixture's committed expectation
(`tools/gates/fixtures/argot-derivation-gate.expected`) is exactly
`D4L-ARGOT-DERIV` ×4 + `D4L-ARGOT-RULE` ×1, so the planted set and the recorded
set agree. `--selftest` moved 18/18 (round 25) → **21/21** at `5b5abe78…`; the
three added checks are not itemized in this file — the successor seat that
freezes the row should read the selftest's own list rather than inherit this
count.

**(c) The typed pipeline's own controls already cover the wiring.**

```sh
python3 tools/gates/typed-pipeline-gate.py --selftest   # 19/19, exit 0
```

The selftest mirrors the argot sibling and its two fixtures into the temp
mirror, runs the mirrored sibling's selftest, and probes the mirrored leg on
the family packet (`tools/gates/typed-pipeline-gate.py:1397-1472`). So the
wiring of §3.2 is covered by a control the gate itself owns, not only by this
seat's reading.

**(d) A cross-seat control this seat did not run but read.** The X60 seat's
independent instrument `reports/round-26/audit/x60-register-derivation-spotcheck.py`
re-derives the register forms through a **different parser** (`ruby -ryaml`,
YAML 1.1) and its own `head2`/`reverse` implementations, with a `--controls`
mode. A successor seat freezing §3.1 should require that instrument's agreement
rather than accepting this file's readings; independence is the point and this
seat's enumeration in §4 shares the gate's own helpers.

## 6. Two pins this round moved, named so they are not inherited

**(a) `tools/gates/typed-pipelines.json`'s `d4` profile is stale.** The profile
pins `typed-pipeline-gate.py` at `879d40bf…`; the live gate is `b749ad07…`
(§2), and the file itself declares the discipline: "a stale pin refuses (exit
2, `L1-profile`) until it is re-pinned with a command and a date"
(`tools/gates/typed-pipelines.json:3`). **Measured, and the behaviour is
correct:** the D4 source run prints `ok L1-profile` and exits 0 at 20/20, so
the profile pin is checked against the *profile*'s own targets rather than the
grading gate's bytes — the pin is stale as a *record*, not as a *gate*. The
successor pin belongs to the O seats; it is named here because §3.2's row cites
that gate and a reader comparing the two digests will find the disagreement.

**(b) `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` now replays 6/6
`could-not-evaluate`.** Measured 18:02:14Z with `TMPDIR` **outside** the repo
(`TMPDIR=/var/tmp/kotodama-r26`, or every row reads `mirror_unsafe` exit 2):

```sh
TMPDIR=/var/tmp/kotodama-r26 python3 tools/replay-frozen.py --json \
  tools/gates/frozen/round-25/gate-input/MANIFEST.tsv
# summary {'rows': 6, 'reproduced': 0, 'mismatch': 0, 'could_not_evaluate': 6, 'exit': 2}
```

All six rows pin `typed-pipeline-gate.py` at `879d40bf…`; the live gate is
`b749ad07…`, so each row reads `reason: gate_digest_mismatch`. This is the
designed fail-closed behaviour of a re-freeze discipline ("a re-freeze is a new
recording, never an in-place edit") and the correct response is a **new
generation**, which is the O claim's row to land. The round-25 generation was
green 6/6 when it was recorded; it is red now because the pinned gate moved, not
because the recording was wrong.

## 7. What this seat did not do

- No `SCORECARD.md`, `SKILL.md`, `LOG.md`, `corpus/**`, `tools/**`,
  `examples/**` or filed round-8–25 byte was written.
- No frozen row, `MANIFEST.tsv`, `expected.json` or `freeze-receipt.json` was
  edited; §6 names the pin tails and leaves them to their owners.
- No independent promotion verification is claimed, and this draft admits
  nothing: the row in §3.1 is **not** proposed for landing at this round, and
  the row in §3.2 is proposed for the orchestrator's decision.
