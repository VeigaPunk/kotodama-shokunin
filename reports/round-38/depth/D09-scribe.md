- Seat: D09 | scribe | claim D | date 2026-10-19 | baseline 9bccc9b

# D09 — landed-changes material for claim D

**Mission** (`reports/round-38/targets.json`, seat `D09`): *"Landed-changes material."*
Out path: `reports/round-38/depth/D09-scribe.md`.

**Status: DRAFT — no artifact of claim D is landed, and this seat landed none.** The D residue
legs exist only as *drafts* in sibling fragments and in scratch candidate patches; not one tool,
example or pin byte has moved (`git diff --name-status 9bccc9b` → empty; §5). This seat therefore
does **not** write a landed-changes list, because there is nothing landed to list. What it can do —
and does below — is (a) measure the before-state first-hand, (b) measure the **pin cascade** each
landing drags, (c) hand the integrator a commit-ready inventory keyed to the measurements, and
(d) reconcile its own independent cascade measurement against the siblings' (§5), so the
landed-changes section can later be filled from evidence rather than from intent.

**Dependency state, and it moved under this seat.** At this seat's first sample `find
reports/round-38 -type f` returned 4 files (the two declarations, the two telemetry records). At
finalization it returns 15, including `plan/P01-d-plan.md`, `depth/D03-isolated.md`,
`depth/D05-verify.md`, `depth/D07-receipt.md`, `depth/D10b-verify.md`, `cross/X02-honesty.md` and
the three `adj/` fragments. **`depth/D01-f6-design.md`, `depth/D02-rl8-design.md`,
`depth/D04-pins.md`, `depth/D06-verify-pins.md`, `depth/D08-gap-fill.md`, `scout/K01-residue.md`
and `cross/X00-connector.md` are still absent** — including the two files D03's mission names as
its inputs. §1–§4 below are this seat's own first-hand measurements, taken before the siblings
landed; §5 folds them explicitly and attributes each.

**Baseline.** `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`.
`git status --porcelain` → `?? reports/round-38/` (one row). This seat moved no tracked byte.

**Write scope.** This file only. No tool, gate, packet, component, pin, frozen baseline or filed
byte written. No commit, no push, no install, no network.

**F-C13-1 / freeze rule honoured.** No `reports/round-*/run-validation.py` was executed anywhere,
in-tree or in a copy. No `--freeze` of `reports/round-34/handoff/declared-in-r7` was run. Every
mutation control ran in a `git archive HEAD` copy under `.scratch/`; the in-tree tree was never
mutated, and the filed r7 bytes were never read-write.

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth and never clearance.

---

## §1 The before-state, measured first-hand

Claim D (`reports/round-38/claims.json:13-18`) names two residues. Both are absent at `9bccc9b`,
measured, not quoted:

**(a) the F-6 counters.** `design-brief.md:306-307` (`reports/round-17/d4/`) fixes the Δ3
signature: *"the coverage block reports `derived_forms` and `derived_ok` counts that agree."*
The tokens occur **0** times in `examples/` and **0** times in `tools/`:

```
$ for t in derived_forms derived_ok derived_pairs; do printf "%s: " "$t"; \
    grep -rlc "$t" examples/ tools/ 2>/dev/null | wc -l; done
derived_forms: 0
derived_ok: 0
derived_pairs: 2
```

The argot leg prints its own differently-named coverage line, and the projection's `coverage`
block carries no derivation counts at all:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 \
          claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0
```

`tools/gates/argot-derivation-gate.py:917-921` is the print; `derived_pairs` is the gate's own key
set, which r25 named as **not** the forecast's (`reports/round-25/argot/delta.md:255`: *"the gate's
coverage line uses `derived_pairs` instead, a different key set from the forecast's"*). The
projection block is `examples/culture-d4/typed-labels.d4.yml:29-46` — `labels_by_kind`,
`typed_labels: 82`, `findings_total: 12`, `conflicts`, `rank_rules_*`, `reconciliation_records` —
no `derived_forms`, no `derived_ok`. The emitter of that block is
`tools/d2-typed-labels.py:2879-2895`.

**(b) the RL-8 era leg.** `examples/culture-d4/components/13-register-law.yml:57` states it in the
delivered bytes: *"The era leg (RGL-05) is specified and unimplemented — tools/gates/argot-derivation-gate.py
has no era concept (reports/round-26/register/rules.md section 5, RL-8)."* The spec is
`reports/round-26/register/rules.md:110-113`:

```
rule REGISTER-ERA-01:
  a record with register == "stamp" must carry stage >= E1
  a `stamp` record with stage E0  ->  D4L-ERA (FAIL)
```

and the gap is owned at `reports/round-27/law/impl-8.md:68` (`RL-8`, *"whoever grows the leg"*).
The law gate carries `era` only as a **kind token** in `DECLARED_KINDS`
(`tools/gates/register-law-gate.py:121-122`) — it never reads `stage`:
`law_rows` (`:204-211`), `packet_record_ids` (`:214-228`) and `declared_registers` (`:231-243`)
resolve ids and register names, not eras.

**The gap is live, measured (control N).** In an isolated `git archive 9bccc9b` copy, rewriting one
stamp record's `stage: "E1"` → `stage: "E0"` (`packet.e0.yml`) produces **zero findings in both
gates**:

```
$ python3 -B tools/gates/register-law-gate.py packet.e0.yml
coverage: packet.e0.yml law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 \
          force_failures=0 consequence_failures=0 dangling=0 findings=0
exit=0
$ python3 -B tools/gates/argot-derivation-gate.py packet.e0.yml
coverage: packet.e0.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 \
          borrow_pairs=6 violations=0 rule_holds=0
exit=0
```

An E0-dated stamp form — the defect `REGISTER-ERA-01` names — reads green. That is RL-8
reproduced, not inherited from the filed record.

**Both gates are green pre-round**, so the round starts from a clean baseline and any red the D
block produces is attributable to the D block:

```
$ python3 -B tools/gates/argot-derivation-gate.py --selftest   → selftest: 27/27 checks passed (exit 0)
$ python3 -B tools/gates/register-law-gate.py --selftest      → selftest: 45/45 checks passed (exit 0)
$ python3 -B tools/check-gate-battery.py                      → pass 7, fail 0, battery_exit 0
$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
                                                              → summary: 20/20 legs passed (exit 0)
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 \
            statuses=16/7/4 v2_subset=equal alias_leg=landed \
            packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

---

## §2 The load-bearing finding: the two landings have **different blast radii**

This is the material a landed-changes section needs, because it decides whether claim D's
`after_required` (*"filed bytes untouched except the two named tool/example artifacts"*,
`claims.json:16`) is reachable.

### §2.1 The RL-8 era leg is chain-neutral (control F)

Appending the era leg's bytes to `tools/gates/register-law-gate.py` alone, in an isolated archive
copy, leaves the r7 default chain **exit 0 with the packet digest unmoved**:

```
$ printf '\n# d09: hypothetical era leg byte\n' >> tools/gates/register-law-gate.py
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 ... packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

**Why.** The law gate is in the **battery's** registered set but **not** in `V3_READ_SET`:

- `tools/check-gate-battery.py:130-132` → `REGISTER_LAW_GATE_NAMES = ("register-law-gate.py",)`,
  folded into `BASELINE_ONLY_GATE_NAMES` and `REGISTERED_GATE_NAMES`.
- `tools/exercise-handoff-e2e.py:1939-1953` → `V3_READ_SET` expands to **58** members; the law
  gate is **not** one of them (verified by resolving every constant in the tuple).
- `reports/round-34/handoff/declared-in-r7/expected.json` `inputs` (58 rows): law gate **absent**,
  argot gate **absent**, `typed-pipeline-gate.py` **absent**.

The battery does police the law gate's bytes, and it fails closed on a revision
(`tools/check-gate-battery.py:540-545`, `BASELINE-GATE-REVISED`). Control C, measured:

```
$ printf '\n# d09 control\n' >> tools/gates/register-law-gate.py   # isolated copy
$ python3 -B tools/check-gate-battery.py
  "summary": { "battery_exit": 2, "fail": 0, "pass": 7, "unevaluable": 0 }
```

So an era leg on the law gate requires a **new battery baseline** under a default root (the
existing one is `tools/gates/expected/register-law-gate/r30-post/expected.json`, which pins
`gate_sha256 15f8b232…`; `reports/round-30/fixes/battery-registration.md` names exactly this
freeze step as the integration dependency). It does **not** require an r7 re-freeze.

### §2.2 The F-6 emitter is NOT chain-neutral — it drags a pin cascade (controls E, I, J, K)

`derived_forms`/`derived_ok` have to appear in the projection's `coverage` block
(`typed-labels.d4.yml:29-46`) to satisfy `design-brief.md:306-307`, and that block is emitted by
`tools/d2-typed-labels.py:2879-2895`. Both the file and its emitter are pinned, transitively:

| # | surface | pinned where | moved by |
|---|---|---|---|
| 1 | `examples/culture-d4/typed-labels.d4.yml` | `V3_READ_SET` (`exercise-handoff-e2e.py:1939-1953`) | adding the two keys |
| 2 | `tools/d2-typed-labels.py` (the projector) | `expected-holds.json` `projector_sha256` (`2819f687…`) | any emitter edit |
| 3 | `examples/culture-d4/expected-holds.json` | `V3_READ_SET`; `v3_verify_d4_pins` (`exercise-handoff-e2e.py:2225-2260`) | re-pinning 1 and 2 |
| 4 | `tools/gates/typed-pipelines.json` (d4 first-match profile) | `L1-profile` leg | re-pinning 1 and 3 |
| 5 | `examples/culture-d4/packet.d4.typed.yml` | `assemble-d4-typed.py --check` determinism leg | re-emitting the projection |

Measured, each in its own isolated archive copy:

**Control E — keys added to the projection only:**
```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=1 ...
handoff-v3: E2E-DIGEST: examples/culture-d4/expected-holds.json projection_sha256: the tree \
            recorded c23b0ab532cf… for examples/culture-d4/typed-labels.d4.yml but the bytes \
            measure 0059642fbcfa…
```

**Control I — the emitter's byte moved only:**
```
handoff-v3: E2E-DIGEST: examples/culture-d4/expected-holds.json projector_sha256: the tree \
            recorded 2819f68769df… for tools/d2-typed-labels.py but the bytes measure 825c8b3562fb…
```
and in the same copy the typed gate loses two legs:
```
FAIL L1-projection_freshness: projector does not reproduce the committed projection byte-for-byte
FAIL L1-build: projector does not reproduce the committed projection byte-for-byte
```

**Control J — projection + expected-holds + projector + typed-pipelines re-pinned (4 surfaces):**
```
summary: 20/20 legs passed        (typed gate green)
handoff-v3: exit=1 ...
handoff-v3: E2E-DIGEST: d4 leg failed: tools/assemble-d4-typed.py --check exit 1: \
            examples/culture-d4/packet.d4.typed.yml differs from the deterministic typed packet
```
→ the fifth surface (`packet.d4.typed.yml`) surfaces only after the first four are re-pinned.

**Control K — the full five-surface cascade:** the chain advances past the digest legs and stops at
an **unrelated** boundary:
```
handoff-v3: E2E-UNC: the D4-CL08 landed form is not backed by this run: the alias witnesses are \
            red (tools/d2-typed-labels.py --selftest exit 1; tools/assemble-d4-typed.py --selftest exit 0)
```
The cause is `tools/d2-typed-labels.py:3114-3115`, a selftest control that asserts the **D2**
projection keeps its exact baseline digest (`a3aa452cd5ae…`) while the mirror holds
`examples/culture-d2`. Patching the shared emitter for a D4 key breaks a D2 freeze-control:
`selftest: 162/163 checks passed — failures: boundary compatibility: D2 projection keeps its exact
baseline digest`. The untouched copy passes `163/163`, so the failure is caused by the patch, not
pre-existing.

**Consequence.** An F-6 emitter that lives in `tools/d2-typed-labels.py`'s shared `coverage` dict
cannot be landed without also re-pinning five surfaces and re-baselining a D2 freeze-control —
which is outside claim D's declared `after_required` (*"filed bytes untouched except the two named
tool/example artifacts"*).

### §2.3 The one F-6 route that IS chain-neutral (control L, control M)

The two counters are the argot leg's own subject matter, and its coverage line is **not** pinned:
`V3_READ_SET` does not contain the argot gate, the battery's `REGISTERED_GATE_NAMES` does not
contain it either (`check-gate-battery.py:130-132`; control B measured that a mutated argot gate
leaves the battery `pass 7, battery_exit 0`), and the typed gate's L3b leg reads only
`FINDING D4L-ARGOT-*` lines (`tools/gates/typed-pipeline-gate.py:528-540`), never the `coverage:`
line.

Adding `derived_forms=`/`derived_ok=` to the argot gate's own coverage line
(`tools/gates/argot-derivation-gate.py:917-921`), in an isolated copy, leaves **every** chain
green:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_forms=8 \
          derived_ok=8 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit=0
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 \
            statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f57132…   ← unmoved
$ python3 -B tools/check-gate-battery.py          → pass 7, fail 0, battery_exit 0
$ python3 -B tools/gates/argot-derivation-gate.py --selftest  → selftest: 27/27 checks passed
$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
                                                  → summary: 20/20 legs passed
```

**And the counters are not vacuous — they discriminate (control M).** Tampering one stamp form's
`term` (`tuum` → `tuuXm`) so its declared chain no longer yields it:

```
$ python3 -B tools/gates/argot-derivation-gate.py packet.tamper.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-55 'tuuXm' (register 'stamp'): declared \
          chain 'lengthen' applied to 'tum' does not yield the candidate; …
coverage: packet.tamper.yml … derived_forms=8 derived_ok=7 … violations=1 …
```

`derived_ok` moves 8 → 7 while `derived_forms` stays 8. The counters carry the forecast's "counts
that agree" signature non-vacuously. This seat does **not** claim this route is the one the D
block will take — that is D01/D02's design call and the integrator's. It records that it is the
only measured route that satisfies F-6 without an r7 re-freeze, and that the `typed-labels.d4.yml`
route measured in §2.2 does not.

---

## §3 Commit-ready inventory (for the integrator to complete from landed bytes)

The D block's landed set is empty at this seat's cut. The list below is the **inventory of surfaces
the claim touches**, each with its pre-round digest, so the integrator can fill "landed" from
measurement. Digests are this seat's own `sha256sum` at `9bccc9b`:

| artifact | sha256 at `9bccc9b` | touched by |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` | F-6 counters (chain-neutral route) |
| `tools/gates/register-law-gate.py` | `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169` | RL-8 era leg |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` | F-6 counters (chain-dragging route) |
| `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` | F-6 counters (chain-dragging route) |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` | re-pin if route is chain-dragging |
| `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182` | re-emit if route is chain-dragging |
| `examples/culture-d4/packet.d4.yml` | `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` | **unchanged** on both routes |
| `tools/gates/typed-pipelines.json` | (d4 profile sha `76ecdfdcbf09…`) | re-pin if route is chain-dragging |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` | **unchanged**; the era leg does not edit the law rows |
| `reports/round-34/handoff/declared-in-r7/` | packet.md `45f57132…`, twin `0e229138…`, expected `bbe15887…` | **unchanged** (no re-freeze) |

Frozen references the D block must not move: `reports/round-34/handoff/declared-in-r7/packet.md`
`45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` and
`tools/gates/expected/register-law-gate/r30-post/expected.json` `gate_sha256 15f8b232…`
(a new battery baseline is a **new** file, never an in-place edit — `reports/round-30/fixes/battery-registration.md`).

---

## §4 Cross-claim observations (routed, not absorbed)

- **The argot gate's bytes are unpinned at round level.** It is absent from `V3_READ_SET`
  (`exercise-handoff-e2e.py:1939-1953`), absent from the battery's registered set
  (`check-gate-battery.py:130-132`), and has no baseline under any `BASELINE_ROOTS` root
  (`check-gate-battery.py:146-150`). Control B: mutating its bytes leaves the battery
  `pass 7, battery_exit 0`. That is why the chain-neutral F-6 route exists — and it is an
  operability asymmetry, which is the **O** claim's territory. Routed to `O01`/`O08`/`R03`; this
  seat does not adjudicate it.
- **`head2` is declared-but-unused**, not missing: `packet.d4.yml:281` says *"`head2` is declared
  but unused: over the delivered tree it is an identity, not a derivation"*. The r36 residue list
  named `head2` as residue; the packet's own note explains why it stays unused. Recorded so the
  landed-changes prose does not re-open it.

---

## §5 Reconciliation with the sibling fragments (folded, attributed)

The D block's peers landed while this seat wrote. Each independent measurement below is
**attributed at the point of use**; where a peer's figure agrees with §2 it is marked
*converges*, and where a peer went further it is marked *extends*. This seat did not re-run the
peers' controls.

**§5.1 The F-6 host route — three independent arrivals, one answer.** P01 §4.2 reaches the same
conclusion as §2.3 by the same measurement, from a different instrument set: it prices four
candidate hosts and recommends `tools/gates/argot-derivation-gate.py` as the *"free — recommended
host"*, measuring the projection route as `handoff-v3 exit 1 E2E-DIGEST` with `projector_sha256`
moving at *"4 places"*. D03 §5.2 measures the same split from the candidate-patch side
(`typed-labels.d4.yml c23b0ab5… unchanged` on the gate route; *"if D01/D02 choose instead to emit
the counters from a component or the projection, that moves typed-labels.d4.yml and the pin chain
with it"*). **Converges with §2.2/§2.3.** This seat's five-surface count (§2.2) is one surface
larger than P01's four-host table because it also counts the `packet.d4.typed.yml` re-emit, which
surfaced only at control J — the extra step is a superset, not a disagreement.

**§5.2 D10b found the hole §2.3's route leaves open — and it is load-bearing.** D10b §2–§3 measures
that on **both** routes *"no consumer reads the counters"*: the `L3b-argot` leg reads only
`FINDING D4L-ARGOT-*` lines and the exit code (`typed-pipeline-gate.py:530-539`), so a key-only
emitter is green everywhere, and even a *lying* coverage line (`derived_forms=0`, `violations=99`)
leaves `20/20 legs passed`. D10b's control C4 shows the leg is otherwise discriminating, so the gap
is specific to counters, not general. **This qualifies §2.3**: my control M showed the counters
*discriminate when read*; D10b shows that **nothing reads them**, so "the counters are
non-vacuous" is true of the numbers and false of the acceptance. A landed-changes section must
therefore report the consumer, not only the emitter.

**§5.3 D03 closed that hole and measured it.** D03 §3.1 builds the consumer probe
(`.scratch/d03/f6_consumer_probe.py`), which parses the gate's own `coverage:` line and
**re-derives** the two counters from the packet bytes through a fresh parse sharing no code path
with the gate's `Counter`; D03 §3 reports the candidate patch yields `derived_forms=8 derived_ok=8`,
adds an anti-vacuous `D4L-ARGOT-COVERAGE` HOLD that fires when `derived_forms > 0` and
`derived_ok == 0`, grows the gate's selftest 27 → **29** checks, and keeps `20/20` legs. D03 §5.1
independently reproduces §2.1's battery finding (`battery_exit: 0 → 2`, reading
`gate_revised`) and §2.1's remedy (*"owes a new baseline generation row"*). **Converges with §2.1;
extends §2.3 with the missing consumer.**

**§5.4 D03's scope caution is narrower than my §2.2, and correctly so.** D03 §5.2 reports *"both
residue legs as drafted are pure gate changes: no pin cascade, no re-freeze"* — measured on the
**gate route**, where the projection is untouched. My §2.2 measures the **projection route**, where
it is not. The two statements are both true and describe different landings; the inventory in §3
lists both so the integrator does not read either as universal.

**§5.5 A01 measured the same two hazards independently** (A01 §0: *"the D block's law-gate edit
turns a filed frozen pin red, and the O block's read-set edit breaks the r7 default chain"*).
**Converges with §2.1 and §2.2.**

**§5.6 X02's honesty finding applies to this file's own §2.3.** X02 §1 shows claim D's era-leg
acceptance is *"green is vacuous today"* — the same shape as D10b's counter finding. Any
landed-changes prose this seat later writes must therefore name the **negative control** (the
fired finding), not the green leg. Recorded so the integrator does not read §2.3's
`20/20 legs passed` as acceptance evidence; it is a non-regression reading only.

**§5.7 Still absent, so still owed.** `depth/D01-f6-design.md` and `depth/D02-rl8-design.md` —
the two files D03's mission names as its inputs — had not landed at D03's or this seat's samples
(D03 §0). `depth/D04-pins.md`, `depth/D06-verify-pins.md`, `depth/D08-gap-fill.md`,
`scout/K01-residue.md` and `cross/X00-connector.md` are likewise absent. The pin census in §3 is
therefore this seat's own, not D04's, and D04 owns the authoritative row set.

---

## Owed

- **The landed set still does not exist.** No tool, example or pin byte for claim D has moved
  (`git diff --name-status 9bccc9b` → empty; §5). The D residues live only as drafts
  (`plan/P01-d-plan.md` §3.4, `depth/D03-isolated.md` §3–§4 candidate patch, `depth/D10b-verify.md`
  §4 fenced guard). Until the integrator applies them, the *landed changes* half of this seat's
  mission is **could-not-evaluate**, and this file must be revised in a new revision rather than
  read as a landed-changes list.
- **`depth/D01-f6-design.md`, `depth/D02-rl8-design.md`** — the two drafts the D block's design
  seats owe, and D03's named inputs. Absent at every sample through this seat's finalization
  (`find reports/round-38 -type f`). Owner: D01/D02, then D03.
- **`depth/D04-pins.md`, `depth/D06-verify-pins.md`** — the authoritative pin row set. §3's
  inventory is this seat's own; D04 owns the row drafts and D06 verifies them.
- **`scout/K01-residue.md`, `cross/X00-connector.md`, `depth/D08-gap-fill.md`** — absent at this
  seat's finalization.
- **Integrator: the route decision for F-6**, now with D10b's qualification (§5.2): the landing
  must ship a **consumer**, not only an emitter, or claim D's `after_required`
  (`claims.json:16`, *"or a documented equivalent the legs can count"*) is satisfied in letter and
  not substance.
- **Integrator: a new battery baseline** if the era leg lands on the law gate (§2.1, §5.3). Do not
  edit `tools/gates/expected/register-law-gate/r30-post/`.
- **Integrator: a `reports/round-38/run-validation.py`** does not exist at this seat's cut, so the
  D claim's third counting command (`claims.json:17`) has no target yet.

## Citations

- `reports/round-38/claims.json:13-18`; `reports/round-38/targets.json` seat `D09` — claim D's
  scope, `after_required`, counting commands, and this seat's mission.
- `reports/round-17/d4/design-brief.md:306-307` — the Δ3 signature (`derived_forms`/`derived_ok`).
- `reports/round-25/argot/delta.md:41,255`; `reports/round-26/argot/D24-forecast-closure.md:151,173`
  — F-6 recorded NOT DELIVERED, and the `derived_pairs` key-set divergence.
- `reports/round-26/register/rules.md:110-113,125-128` — `REGISTER-ERA-01` spec and its measured
  non-implementation.
- `reports/round-27/law/impl-8.md:68` — `RL-8` ownership.
- `examples/culture-d4/components/13-register-law.yml:57` — the delivered declaration of
  non-enforcement.
- `examples/culture-d4/packet.d4.yml:281` — the `head2` declared-but-unused note;
  `:1009-1183` — the eight stamp records (all `stage: "E1"`).
- `examples/culture-d4/typed-labels.d4.yml:29-46` — the live `coverage` block (no derivation keys).
- `tools/d2-typed-labels.py:2879-2895` (coverage emitter), `:3114-3115` (the D2 baseline-digest
  selftest control).
- `tools/gates/argot-derivation-gate.py:917-921`; `tools/gates/register-law-gate.py:121-122,204-243,635-638`.
- `tools/gates/typed-pipeline-gate.py:528-540` (L3b reads only `FINDING D4L-ARGOT-*`).
- `tools/exercise-handoff-e2e.py:157-170,1939-1953,2225-2260`.
- `tools/check-gate-battery.py:130-132,146-150,540-545`.
- `reports/round-34/handoff/declared-in-r7/{expected.json,freeze.txt,packet.md}`;
  `reports/round-34/handoff/repin.json`; `reports/round-30/fixes/battery-registration.md`;
  `tools/gates/expected/register-law-gate/r30-post/expected.json`.
- Command evidence: every command and output quoted above ran in this seat's window under
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` from the lane root; mutation controls ran
  in `git archive HEAD` copies under `.scratch/d09*`. `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`;
  `git status --porcelain` → `?? reports/round-38/` only.
