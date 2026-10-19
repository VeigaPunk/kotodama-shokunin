- Seat: D07 | executor | claim D | date 2026-10-19 | baseline 9bccc9b

# D07 — depth receipt: claim D before→after, counting commands, and what the F-6/RL-8 residue actually is

**Assignment** (`reports/round-38/targets.json`, seat `D07`): *"Depth receipt draft."* Out path
`reports/round-38/depth/D07-receipt.md`. Binding `shared_rules` read at
`reports/round-38/targets.json`: write only the assigned out path under `reports/round-38/`; never
edit filed bytes (`reports/round-1..37/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet
`.ufo/**`) — tool/example changes are DRAFTED as fenced blocks for the integrator; no git
commits/pushes/installs/network; **ABSOLUTE** never run any `reports/round-*/run-validation.py`
in-tree (F-C13-1), isolated `git archive` copies only, and no re-freeze of
`reports/round-34/handoff/declared-in-r7`; every claim cites file:line or command output, unknowns
are `to-verify`, never fabricate.

**Status: DRAFT.** Every figure below is a live measurement taken by this seat at baseline
`9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` in the window named in §1. This seat landed nothing: no
packet byte, no component byte, no tool byte, no pin, no corpus entry. No round runner was executed
anywhere, in-tree or in a copy. No `--freeze` was attempted. The two controls in §4 were run on
copies under `.scratch/d07/`.

## 0. Headline — both D residues are real, and the era one is now *proven* open, not inferred

Claim D (`reports/round-38/claims.json`) names two residues carried from the rejected r36 D claim
(`reports/round-36/validation.json` `claims.D.failures[0]`, `reports/round-36/scout/K01-register-scout.md`
§4). This seat measured both against the live tree:

| residue | claimed state | measured at `9bccc9b` | verdict |
|---|---|---|---|
| **F-6** — `derived_forms`/`derived_ok` counters in the coverage block | "no emitter exists anywhere" | `grep -rl "derived_forms\|derived_ok" examples tools` → **exit 1, no match**. The live coverage block (`examples/culture-d4/typed-labels.d4.yml:29-47`) carries `typed_labels`, `labels_by_kind`, `rank_rules_*`, `reconciliation_records`, `conflicts`, `findings_*` — no derivation keys. Its producer (`tools/d2-typed-labels.py:2879-2894`) emits no such key. The argot gate's own counters (`derived_pairs`, `violations`, `tools/gates/argot-derivation-gate.py:567,571`) are printed to the gate's `coverage:` line (`:917-920`) and never cross into the projection. | **confirmed open — no producer, in either direction** |
| **RL-8** — the era leg (RGL-05's substance) | "specified, unimplemented" | **now measured, not just cited**: an L-55 `stage: "E1"`→`"E0"` tamper — which the packet's own RGL-05 text calls *"a defect"* (`examples/culture-d4/packet.d4.yml:2863`) — produces **no finding** from the argot gate (`violations=0`, exit 0) and **no finding** from the law gate (`findings=0`, exit 0). Neither gate contains the token `stage`, `available_from` or an era concept at all (`grep -c` → 0 in both). | **confirmed open — and the blind spot is demonstrated, not assumed** |

Everything else claim D's `after_required` names — the register-form domain, the derivation replay,
the law gate, the typed pipeline — is **already green at the baseline** and was already green at
`ce103bf`; §3 receipts that state so the round is not credited for it.

## 1. Measurement window and state pins

| pin | value | command |
|---|---|---|
| lane root | `/home/vgpnk/Projects/shokunin/kotodama-shokunin` | — |
| baseline | `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` | `git rev-parse HEAD` |
| working tree | clean except this round's own directory: `?? reports/round-38/` | `git status --porcelain` |
| stamp | `2026-10-19T11:04:53Z` | `date -u +%FT%TZ` |
| env | `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` | before every scratch-writing command |

`git status --porcelain` returns only `?? reports/round-38/`, so **every `examples/`, `tools/` and
`corpus/` surface measured below is byte-identical to HEAD**, which is what makes §1.1 a recoverable
state pin rather than an assertion.

### 1.1 Digests (every reading below binds to these bytes)

```
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3  tools/d2-typed-labels.py
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
```

The packet, projection, typed packet, hold-set and the two gate digests are **identical to the
`ce103bf` readings** in `reports/round-36/scout/K01-register-scout.md` §Citations — the r36→r38
baseline move (`ce103bf`→`9bccc9b`) did not touch the D4 chain. That is stated because it means the
residue is not a regression introduced by the intervening rounds.

## 2. The claim under receipt

`reports/round-38/claims.json`, claim **D**, axis **depth**:

| field | content |
|---|---|
| claim | Land the r36 register residue, correctly claimed: (a) the register F-6 counters — an emitter for `derived_forms`/`derived_ok` exists nowhere (K01 r36 census), so the argot/typed legs cannot count them; (b) the RL-8 era leg (the register-law gate's era check). Re-run the register legs (argot, law, typed pipeline) and record pins as new rows. |
| before | r36 K01: no `derived_forms`/`derived_ok` emitter anywhere in `examples/` or `tools/`; RL-8 era leg missing; both named as residue when the stale r36 claim was rejected |
| after_required | the counters emit from the packet/components (or a documented equivalent the legs can count); the era leg runs; argot/law/typed legs green with the new coverage named; pins updated as new rows; filed bytes untouched except the two named tool/example artifacts |
| counting_commands | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`; `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml`; `python3 reports/round-38/run-validation.py` |
| thresholds | two independent verifiers; legs green; the new coverage named (no vacuous-pass) |

`reports/round-38/targets.json` seat `D07` is an **executor** seat whose mission is the receipt
itself, not the landing. The sibling seats carry the design (`D01`, `D02`), the isolated verify
(`D03`), the pins (`D04`), the verifiers (`D05`, `D06`, `D10b`) and the scribe material (`D09`).
This receipt therefore records the *before* and the *grading surface* and leaves the *after* to be
measured by `D05`/`D10b` on whatever the integrator lands — that is the honest scope of a receipt
draft, and it is stated rather than papered over.

## 3. Before → after, clause by clause

### 3.1 Before — measured, with the producer surface named

**F-6.** The forecast's own wording: *"the coverage block reports `derived_forms` and `derived_ok`
counts that agree"* (`reports/round-17/d4/design-brief.md:306-307`, quoted at
`reports/round-25/argot/forecast.md:37`). r25 dispositioned it **NOT DELIVERED**
(`reports/round-25/argot/delta.md:41`); r26 dispositioned it **"not designed"**
(`reports/round-26/register/execution-3.md:74`). Measured now:

```
$ grep -rl "derived_forms\|derived_ok" examples tools      # no match, exit 1
$ grep -n "derived_forms\|derived_ok" examples/culture-d4/typed-labels.d4.yml   # no match
```

There are exactly **two** surfaces the keys could live on, and neither carries them:

| surface | what it emits | line | carries F-6 keys? |
|---|---|---|---|
| the projection's coverage block | `typed_labels`, `labels_by_kind`, `label_findings_*`, `rank_rules_*`, `rank_quarantine_handles`, `reconciliation_records`, `conflicts`, `findings_*` | emitted `tools/d2-typed-labels.py:2879-2894`; landed `examples/culture-d4/typed-labels.d4.yml:29-47` | **no** |
| the argot gate's coverage line | `records`, `register_scoped`, `derived_pairs`, `claimed_chains`, `borrow_pairs`, `violations`, `rule_holds` | counted `tools/gates/argot-derivation-gate.py:567,571`; printed `:917-920` | **no** — and it is stdout, not a projection block |

So the residue is precise: **the numbers exist under the names `derived_pairs`/`violations`; the
forecast's names exist nowhere.** It is a key-set gap plus a producer gap — the argot gate's
`Counter` (`tools/gates/argot-derivation-gate.py:545-548`, keys enumerated in §3.3) is not written
into the projection, and the projection's producer has no derivation input at all.

**RL-8.** Specified at `reports/round-26/register/forms.md:142` (`RGL-05 | every stamp form is
available_from: E1; an E0 claim is a defect | mark`) and at
`reports/round-27/law/impl-8.md:68` (*"the argot gate has no era concept, so an E0-dated stamp form
produces no finding"*). The landed law row states the same substance in the packet:
`examples/culture-d4/packet.d4.yml:2863` — *"every stamp form is `available_from E1` … an E0 stamp
claim is a defect and E3 is reserved and unoccupied"*. The gate knows the `kind` value `era` is
legal (`tools/gates/register-law-gate.py:121` `DECLARED_KINDS` includes `"era"`) — so the row is
*shaped* correctly and nothing grades the dating.

### 3.2 After — what the baseline already satisfies (not this round's credit)

| # | clause of `after_required` | command | observed | verdict |
|---|---|---|---|---|
| A-1 | "argot … legs green" | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`, exit 0 | **already satisfied** |
| A-2 | "law … legs green" | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0`, exit 0 | **already satisfied** |
| A-3 | "typed pipeline" green | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `ok L3b-argot`, `ok L1-profile`, `summary: 20/20 legs passed`, exit 0 | **already satisfied** |
| A-4 | "the register forms are delivered" | `examples/culture-d4/components/04-lexicon.yml:236-243`; packet records at `examples/culture-d4/packet.d4.yml:1009` (L-56) and `:1053` (L-55) | 8 register records L-55..L-62, each with `register: stamp`, `derived_from`, `derivation {op, base}`, `doublet_of`, `stage: E1` | **already satisfied** (r26/r27/r30 work) |
| A-5 | "pins updated as new rows" | see §5 | the `round-30-qreg-records` generation matches all live digests; the superseded round-28 generation still exists as a row | **already satisfied**; a D landing adds a generation |
| A-6 | "filed bytes untouched" | `git status --porcelain examples/ tools/ corpus/ reports/round-1..37` | empty | **already satisfied** (this seat wrote none) |

Supporting legs, all green at `9bccc9b`:

```
$ python3 -B tools/gates/argot-derivation-gate.py --selftest    # selftest: 27/27 checks passed, exit 0
$ python3 -B tools/gates/register-law-gate.py --selftest        # selftest: 45/45 checks passed, exit 0
$ python3 -B tools/gates/typed-pipeline-gate.py --selftest      # selftest: 19/19 checks passed, exit 0
$ python3 -B tools/assemble-culture-d4.py --selftest            # selftest: 81/81 checks passed, exit 0
$ python3 -B tools/assemble-culture-d4.py --check               # packet.d4.yml: byte-identical deterministic assembly, exit 0
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4
            v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

The r7 packet digest is unchanged (`sha256sum reports/round-34/handoff/declared-in-r7/packet.md` →
`45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`), which is claim O's threshold
and this receipt's proof that no freeze byte moved.

### 3.3 The exact grading surface a landing must move

For whoever lands F-6 and RL-8, the surfaces are these and only these (both **live tools**, so the
change is a fenced draft for the integrator — `reports/round-38/targets.json` shared rule):

**F-6 producer.** The argot gate's counters are the only derivation census in the tree:

```
tools/gates/argot-derivation-gate.py:545-548   counters = Counter()   # keys: records, register_scoped,
                                               #   derived_pairs, claimed_chains, borrow_pairs,
                                               #   violations, rule_holds, borrow_holds
tools/gates/argot-derivation-gate.py:567       counters["derived_pairs"] += 1
tools/gates/argot-derivation-gate.py:571       counters["violations"] += 1
tools/gates/argot-derivation-gate.py:917-920   print("coverage: …")   # stdout, not a projection block
```

and the projection's producer emits its block at:

```
tools/d2-typed-labels.py:2879-2894             coverage = { … }       # no derivation input
examples/culture-d4/typed-labels.d4.yml:29-47  the landed block
```

So a faithful F-6 landing has two candidate shapes, and the integrator should pick one and record
it: **(a)** add `derived_forms`/`derived_ok` to the argot gate's own `coverage:` line (minimal,
keeps the single producer, but the forecast says *"the coverage block"* — i.e. the projection); or
**(b)** thread the argot counters into `tools/d2-typed-labels.py`'s `coverage` dict so the
projection carries them (matches the forecast's wording, but adds a cross-tool dependency and
therefore a pin cascade). The forecast's wording (`design-brief.md:306-307`) favours **(b)**;
the r25 delta's own note (`reports/round-25/argot/delta.md:198`, *"new coverage keys + gate leg +
expectation row"*) also favours **(b)**. Recorded as the recommended shape; the choice is the
integrator's.

**RL-8 hook point.** Both gates lack any era token (`grep -c` for `stage`, `available_from` → 0 in
`argot-derivation-gate.py` and `register-law-gate.py`). The natural place is the argot gate's
register loop, where `record_register` (`:365`) already resolves the register and the packet's own
`register_law` block is available — an `available_from` read off RGL-05's consequence against each
register-scoped record's `stage`. The law gate is the other candidate (it owns `DECLARED_KINDS`,
`tools/gates/register-law-gate.py:121`), but it grades the *law rows*, not the *forms*, and the
specified defect is a property of a form's dating — so the argot gate is the shape the filed specs
name (`reports/round-27/law/impl-8.md:68`). Either way the control the landing must file is
exactly the tamper in §4.2.

## 4. The negative controls — the legs discriminate, and the era blind spot is proven

A green leg over a domain is evidence only if the leg can go red. Two controls, both run on copies
under `.scratch/d07/`, never in-tree.

### 4.1 The derivation control still fires (the `violations=0` reading is real)

`.scratch/d07/neg-deriv.yml` is the delivered packet with one register form tampered
(`kit` → `kat`, a wrong `reverse` of `tik`):

```
$ python3 -B tools/gates/argot-derivation-gate.py .scratch/d07/neg-deriv.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kat' (register 'stamp'): declared chain
  'reverse' applied to 'tik' yields 'kit'; the stated inputs and rules do not yield the candidate
coverage: .scratch/d07/neg-deriv.yml records=187 register_scoped=14 derived_pairs=8
          claimed_chains=8 borrow_pairs=6 violations=1 rule_holds=0
exit=1
```

`violations=1`, exit 1 on the tampered copy; `violations=0`, exit 0 on the delivered packet. **The
A-1 reading is discriminating.** The same control shape is filed independently by round 26
(`reports/round-26/validation.json` `claims.D.measurement.control_violating_derivation`) and is
asserted inside the gate's own selftest (`c-02-negative-control-rejected`, one of the 27/27).

### 4.2 The era control — the RL-8 blind spot, demonstrated

`.scratch/d07/e0-stamp.yml` is the delivered packet with **one** byte-class change: L-55's
`stage: "E1"` → `stage: "E0"` (`examples/culture-d4/packet.d4.yml:1059`). By the packet's own
RGL-05 text (`:2863`) that is *"a defect"*. Measured:

```
$ python3 -B tools/gates/argot-derivation-gate.py .scratch/d07/e0-stamp.yml
coverage: .scratch/d07/e0-stamp.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8
          borrow_pairs=6 violations=0 rule_holds=0
exit=0                                  # ← no finding

$ python3 -B tools/gates/register-law-gate.py .scratch/d07/e0-stamp.yml
coverage: .scratch/d07/e0-stamp.yml law_rows=5 identity_rows=8 record_ids=183 registers=17
          speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0
exit=0                                  # ← no finding
```

The tamper is real (baseline `grep -c 'stage: "E0"'` → 53; tampered → 54; the L-55 record's own
line reads `stage: "E0"`). **Neither gate notices.** That is the RL-8 gap, demonstrated rather than
cited: it is the control a landing must turn from "no finding" into `D4L-*` exit 1.

Caveat stated plainly: this control proves the *absence* of a check, which is the residue's
substance. It is not a claim that the delivered tree is defective — the delivered tree dates every
stamp form `E1`, which is correct.

## 5. The pin surface — what is already frozen, and what a landing would owe

Measured by digest comparison, not by re-pin:

| pin surface | live value | pinned value | state |
|---|---|---|---|
| `tools/gates/typed-pipelines.json` `profiles[0]` (id `d4`, generation `round-30-qreg-records`) — packet | `aac91246cede8840…` | identical | current |
| … projection | `c23b0ab532cfb9d4…` | identical | current |
| … expected | `e6ae9828d6c82aa6…` | identical | current |
| … assembler | `tools/assemble-culture-d4.py` `943f487ba991d45d…` | identical | current |
| … adapter | `tools/assemble-d4-typed.py` `92f5460bcc34ffbb…` | identical | current |
| `examples/culture-d4/expected-holds.json` | `packet_sha256 aac91246…`, `projection_sha256 c23b0ab5…`, `projector_sha256 2819f687…`, `active_pin_generation round-30-qreg-records` | identical | current |
| the superseded generation | `pin_generations[0]` (round 28, packet `543d68a82640e1b0…`, projection `339bfd83bf668324…`) | still present as a row | correct — filed rows are never edited |
| `tools/gates/expected/register-law-gate/r30-post/` | pins packet `aac91246…` and gate `15f8b232…` | identical | current |

The superseded rows exist as rows and were not edited, which is what *"frozen as a new row"* means
(`tools/gates/typed-pipelines.json` `note`: *"editing this file cannot silently re-point a run — a
stale pin refuses (exit 2, L1-profile) until it is re-pinned with a command and a date. No filed
receipt is edited by a re-pin"*).

**What a D landing would owe.** Any F-6 or RL-8 change edits `tools/d2-typed-labels.py` and/or
`tools/gates/argot-derivation-gate.py`. Per the pin discipline:

- editing `argot-derivation-gate.py` alone moves **no** row in `typed-pipelines.json` (its
  `profiles[0]` pins packet/projection/expected/assembler/adapter, not the argot gate), but it does
  invalidate the `b5406bcd…` digest filed in `reports/round-30/audit/x38-law-gate-*.json` and
  `reports/round-30/rerun.json` — **those are filed bytes and must not be rewritten**; the new
  digest is recorded as a new row in this round's fragments, not by editing r30.
- editing `d2-typed-labels.py` **does** move `expected-holds.json`'s `projector_sha256` (currently
  `2819f687…`) and, if the projection's bytes change, `typed-labels.d4.yml` and therefore
  `typed-pipelines.json profiles[0].projection` — a new generation row plus a new
  `pin_generations[]` row. The r26 pattern is the template: `reports/round-26/register/repin.json`
  carries `new_pins` beside `superseded_pins` (*"the hold ROWS are unchanged, only the digests
  move"*).
- `13-register-law.yml` (`c0d77181…`) is **not** a member of the r7 read set — `reports/round-37/adj/A01-freeze-adjudication.md`
  adjudicates that as a roster/completeness defect (claim **O**'s scope, not D's). A D landing that
  touches it would move the packet; **neither F-6 nor RL-8 requires touching it** (F-6 is a
  projection/keys change, RL-8 is a gate check over existing `stage` values). Recorded so the D
  landing does not accidentally pick up O's re-freeze debt.

## 6. Counting commands for this receipt

Every command below was run by this seat, in this seat's shell, at the revision in §1, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. None is a round runner; none writes to the
repo except the two scratch controls.

```sh
# state pins
git rev-parse HEAD                                 # 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26
git status --porcelain                             # only "?? reports/round-38/"
date -u +%FT%TZ                                    # 2026-10-19T11:04:53Z

# the claim's legs (§3.2)
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml    # derived_pairs=8 violations=0, exit 0
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml        # findings=0, exit 0
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml      # ok L3b-argot; summary: 20/20 legs passed

# selftests
python3 -B tools/gates/argot-derivation-gate.py --selftest        # 27/27
python3 -B tools/gates/register-law-gate.py --selftest            # 45/45
python3 -B tools/gates/typed-pipeline-gate.py --selftest          # 19/19
python3 -B tools/assemble-culture-d4.py --selftest                # 81/81
python3 -B tools/assemble-culture-d4.py --check                   # byte-identical deterministic assembly

# F-6 producer census (§3.1, §3.3)
grep -rl "derived_forms\|derived_ok" examples tools               # no match, exit 1
grep -o 'counters\["[a-z_]*"\]' tools/gates/argot-derivation-gate.py | sort -u
grep -c "stage\|available_from" tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py  # 0 / 0

# the two controls (§4) — scratch only, the delivered tree untouched
python3 - <<'PY'
s=open('examples/culture-d4/packet.d4.yml').read()
open('.scratch/d07/neg-deriv.yml','w').write(s.replace('    term: "kit"','    term: "kat"',1))
i=s.find('    id: "L-55"'); seg=s[i:i+900]; j=seg.find('stage: "E1"')
open('.scratch/d07/e0-stamp.yml','w').write(s[:i]+seg[:j]+'stage: "E0"'+seg[j+len('stage: "E1"'):]+s[i+900:])
PY
python3 -B tools/gates/argot-derivation-gate.py .scratch/d07/neg-deriv.yml   # D4L-ARGOT-DERIV, violations=1, exit 1
python3 -B tools/gates/argot-derivation-gate.py .scratch/d07/e0-stamp.yml    # violations=0, exit 0  ← RL-8 gap
python3 -B tools/gates/register-law-gate.py    .scratch/d07/e0-stamp.yml     # findings=0, exit 0   ← RL-8 gap

# the pin surface (§5)
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml \
          examples/culture-d4/packet.d4.typed.yml examples/culture-d4/expected-holds.json \
          examples/culture-d4/components/04-lexicon.yml examples/culture-d4/components/13-register-law.yml \
          tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py \
          tools/d2-typed-labels.py tools/exercise-handoff-e2e.py
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet     # exit 0, packet_sha256=45f57132…
```

## Owed

| # | owed artifact | owner | reason |
|---|---|---|---|
| 1 | the **after** measurement of F-6 and RL-8 (does the landed emitter emit, does the era leg run) | `reports/round-38/depth/D05-verify.md`, `D10b-verify.md` | this seat is the receipt draft; the after-state exists only once the integrator applies the D01/D02 drafts. This receipt supplies the before-state, the grading surface (§3.3) and the control (§4.2) those verifiers need. |
| 2 | the fenced patch drafts for F-6 (producer shape (a) or (b), §3.3) and RL-8 (argot-gate era check) | `reports/round-38/depth/D01-f6-design.md`, `D02-rl8-design.md` | live-tool changes are DRAFTED, never applied by an executor seat (`reports/round-38/targets.json` shared rules). |
| 3 | the pin-cascade rows for whatever lands | `reports/round-38/depth/D04-pins.md` | §5 enumerates the surfaces; the new-generation rows are D04's assignment. |
| 4 | `reports/round-38/run-validation.py` | integrating parent / seat `S01` | the claim's third counting command does not exist at write time (`ls reports/round-38/run-validation.py` → No such file). This seat may not run a round runner in-tree (shared rule, F-C13-1) and has none to run in a copy. |
| 5 | the `head2` declared-but-unused operation | carried from `reports/round-26/register/execution-3.md:74` and `reports/round-36/scout/K01-register-scout.md` §4 | named in the r36 residue census but **not** in this round's claim D; unchanged at `9bccc9b`. Listed so the receipt does not read as claiming a closed register program. |
| 6 | the r7 read-set roster defect (`13-register-law.yml` absent from the 58-file read set; measured here: `len(inputs)=58`, 12 D4 components, 0 hits for `13-register-law`) | claim **O** / `reports/round-38/op/O04-fix-route.md` | reported, not absorbed — it is O's scope, and §5 records that neither F-6 nor RL-8 forces a freeze touch. |

## Citations

Every line reference was read in this window at the revision in §1.

| # | citation | what it establishes |
|---|---|---|
| 1 | `reports/round-38/claims.json` (claim D: claim/before/after_required/counting_commands/thresholds) | the claim under receipt |
| 2 | `reports/round-38/targets.json` seat `D07` (`"id":"D07"`, role executor, claim D, out `depth/D07-receipt.md`) and `shared_rules` | the binding mission and rules |
| 3 | `reports/round-36/validation.json` `claims.D.failures[0]` | the r36 rejection that named the residue |
| 4 | `reports/round-36/scout/K01-register-scout.md` §4 (F-1..F-8 table), §5 (freeze asymmetry), `## Owed` | the residue census this claim inherits |
| 5 | `reports/round-17/d4/design-brief.md:301-310` | the F-6 requirement verbatim ("the coverage block reports `derived_forms` and `derived_ok` counts that agree") |
| 6 | `reports/round-25/argot/forecast.md:37`, `reports/round-25/argot/delta.md:41,198,255,294` | F-6 dispositioned NOT DELIVERED; the recommended landing shape ("new coverage keys + gate leg + expectation row") |
| 7 | `reports/round-26/register/execution-3.md:74` | F-6 dispositioned "not designed" |
| 8 | `reports/round-26/register/forms.md:142` | RGL-05's substance: every stamp form `available_from: E1`; an E0 claim is a defect |
| 9 | `reports/round-27/law/impl-8.md:68` (`RL-8`) | "the argot gate has no era concept, so an E0-dated stamp form produces no finding" |
| 10 | `reports/round-27/law/impl-5.md:41,128` | the RGL-05 row-drop control that produced no finding; the era leg named as unexercised |
| 11 | `examples/culture-d4/packet.d4.yml:1053,1059` | the L-55 register record and its `stage: "E1"` line (the tampered byte in §4.2) |
| 12 | `examples/culture-d4/packet.d4.yml:1009,1015` | the L-56 register record (`kit`, tampered in §4.1) |
| 13 | `examples/culture-d4/packet.d4.yml:2863` | RGL-05's landed consequence text — "an E0 stamp claim is a defect" |
| 14 | `examples/culture-d4/components/04-lexicon.yml:236-243` | the 8 authored register rows |
| 15 | `examples/culture-d4/typed-labels.d4.yml:29-47` | the live coverage block — no `derived_forms`/`derived_ok` |
| 16 | `tools/d2-typed-labels.py:2879-2894` | the projection's coverage producer — no derivation input |
| 17 | `tools/gates/argot-derivation-gate.py:545-548,567,571,917-920` | the argot `Counter` and its keys; the `coverage:` print |
| 18 | `tools/gates/register-law-gate.py:121` (`DECLARED_KINDS` includes `"era"`) | the era row is shaped correctly; nothing grades the dating |
| 19 | `tools/gates/typed-pipeline-gate.py:517-541` (`L3b-argot`) | the argot leg is a typed-pipeline leg |
| 20 | `tools/gates/typed-pipelines.json` (`note`, `profiles[0]`, `profiles[1]`) | the pin discipline: a stale pin refuses (exit 2), a re-pin is a new row |
| 21 | `examples/culture-d4/expected-holds.json` (`packet_sha256`, `projection_sha256`, `projector_sha256`, `active_pin_generation`, `pin_generations[]`) | the live pin pointers and the superseded round-28 row |
| 22 | `reports/round-26/register/repin.json` | the re-pin-as-new-row template (`new_pins` beside `superseded_pins`) |
| 23 | `reports/round-37/adj/A01-freeze-adjudication.md` | the r7 read-set adjudication (claim O's scope, not D's) |
| 24 | `reports/round-34/handoff/declared-in-r7/expected.json` (58 `inputs`, 12 D4 components, 0 hits for `13-register-law`) | measured here; claim O's threshold, and proof no freeze byte moved |
| 25 | `reports/round-34/handoff/declared-in-r7/packet.md` (`sha256 45f57132…`) | the unchanged r7 packet digest |
| 26 | `tools/check-gate-battery.py:117-132` | the battery's registered gate list (does not name `argot-derivation-gate.py`) |
| 27 | `REGIMEN.md` per-round contract | "Admit only when every claim verifies and no axis is harmed; otherwise … never force a pass" |
| 28 | `AGENTS.md` | "Never fabricate domain knowledge or sources: cite a file, a command output, or a source"; "reports contested scope instead of absorbing it" |

Command/output evidence: §1 (`git rev-parse HEAD`, `git status --porcelain`, `date -u`), §1.1
(`sha256sum`), §3.2 (three gates + four selftests + `--check` + the v3 handoff run), §3.1/§3.3
(`grep` censuses), §4 (the two scratch controls and their exits), §5 (digest comparison against
`typed-pipelines.json`, `expected-holds.json`, `reports/round-34/handoff/declared-in-r7/`).

---

*This receipt claims no promotion, no canon, no clearance and no closure. A green gate is a
measurement, not a verdict. The one substantive addition beyond the r36 census is §4.2: the RL-8
era gap is now demonstrated by a live control (an E0-dated stamp form produces no finding from
either gate), not merely quoted from a filed design note.*
