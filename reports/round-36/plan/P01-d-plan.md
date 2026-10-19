- Seat: P01 | planner | claim D | date 2026-10-19 | baseline ce103bf

# P01 — the register build plan: the component/packet content design, the verifying legs, and the pin re-freeze list

- **Seat:** P01 (planner, claim **D**), round 36, loop 1, position 4.
- **Mission (binding, `reports/round-36/targets.json`):** "Register build plan from K01: the
  component/packet content design, which legs verify it, the pin re-freeze list (new rows)."
- **Baseline:** `ce103bf5885af00023cdc4a174c17602476cdcf8` (`git rev-parse HEAD`; `git status
  --porcelain` → `?? reports/round-36/` only — no tracked byte moved by this seat).
- **Write scope:** this file only. Every command ran from the lane root with
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Scratch under `.scratch/p01/`,
  `.scratch/iso/`, `.scratch/iso2/` (all `git archive HEAD` copies). No tool, gate, packet,
  component, pin or filed 1–35 byte written; no commit, no push, no install, no network.
- **F-C13-1 honoured:** no `reports/round-*/run-validation.py` executed in-tree or in a copy; no
  `--freeze` of `reports/round-34/handoff/declared-in-r7`. The only filed code executed is
  read-only gates, the read-only assembler, and the read-only e2e exercise.
- **Dependency note:** the mission says "from K01". `reports/round-36/scout/K01-register-scout.md`
  did **not exist** when this plan was first written (`ls reports/round-36/scout/` →
  `K02-timekeeping-scout.md` only); it **landed during the seat's run** and is reconciled in §7.
  The plan is derived from the **filed** sources the claim names
  (`reports/round-25/argot/`, `reports/round-26/register/`, `reports/round-27/law/`,
  `reports/round-28/law/`, `reports/round-30/fixes/`) plus this seat's own measurements. Where a
  peer D fragment has landed concurrently it is named and reconciled, never silently absorbed.
- **Canon:** NON-CANON engineering design. No real language, institution, script or argot is
  described, cited or approximated. No clearance claimed. A pin is integrity, never truth.

---

## 0. Headline — the claim's `before` is stale; the plan is re-aimed onto the surface that is genuinely open

Claim D's declared `before` reads:

> "Register-form domain empty (`reports/round-25/argot/` + SCORECARD r25 row); register law/strata
> exist but the form class has no instances" — `reports/round-36/claims.json`

**That premise is false at `ce103bf`.** Measured this seat, first command of the run:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit=0
```

`derived_pairs=8` — eight register forms are delivered and replay clean. The domain was closed by
**round 26** (`SCORECARD.md:329`, capability `register-stratum`) and extended by rounds 27/28/30.
The `EMPTY` text the claim quotes is `SCORECARD.md:312`, a **historical r25 row**, correctly
superseded two rows later.

Three peer fragments reached the same correction independently and are on record:
`reports/round-36/depth/D01-design.md:22`, `reports/round-36/depth/D06-gap-fill.md:31`,
`reports/round-36/depth/D09-gap-fill.md:14`, and `reports/round-36/review/R01-d-review.md` §0
row 1. The convergence is not consensus-by-repetition: each measured the delivered bytes.

**Consequence for this plan.** Claim D's `after_required` ("register-form domain non-empty with
verified forms; derivation replay clean; law gate exit 0; typed pipeline holds updated; every pin
re-frozen as a new row") is **already satisfied at the baseline**. Re-drafting the eight form
records would be dead work duplicating filed bytes. So this plan targets the three surfaces that
**are** open, in the order D01 drafted them, and adds the one thing D01 did not measure: **the legs
that would verify the new content currently accept four defect classes silently** (§3). Without
that guard work, "verified forms" is not a measurable claim.

---

## 1. What is delivered, exactly (so the plan does not duplicate it)

Measured, not read from the claim.

| surface | reading at `ce103bf` | command / citation |
|---|---|---|
| 8 register form records | `L-55..L-62`, all `register: stamp`, `stage: E1` | `examples/culture-d4/components/04-lexicon.yml:236-243` |
| derivation pairs | 8, replayed clean | argot gate, §0 |
| `registers` block | 8 rows `QREG-01..08` | `examples/culture-d4/packet.d4.yml:1329` |
| `register_law` block | 5 rows `RGL-01..05` | `examples/culture-d4/packet.d4.yml:2788`; component `13-register-law.yml` |
| contract admits the fields | `register, derived_from, derivation, doublet_of` in `contract.record_fields.lexicon` | `examples/culture-d4/packet.d4.yml:39-42` |
| the four legs | green | §2 below |

Baseline digests (`sha256`, lane root, this seat):

```
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
76ecdfdcbf09c3c7f384d74cd81ddc5e57ef261a4be4267579081766fa8b986d  tools/gates/typed-pipelines.json
```

---

## 2. Baseline legs re-run on the delivered revision (the claim's own thresholds)

Every leg claim D's `after_required` names is green **at the baseline**, over the delivered forms.
Re-run this seat, lane root:

| # | leg | command | result | exit |
|---|---|---|---|---|
| V-1 | derivation replay | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `derived_pairs=8 violations=0 rule_holds=0` | 0 |
| V-2 | replay selftest | `… argot-derivation-gate.py --selftest` | `27/27` (peer D03 §2) | 0 |
| V-3 | law gate | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 dangling=0 findings=0` | 0 |
| V-4 | law selftest | `… register-law-gate.py --selftest` | `selftest: 45/45 checks passed` | 0 |
| V-5 | typed pipeline | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` (incl. `ok L3b-argot`) | 0 |
| V-6 | typed selftest | `… typed-pipeline-gate.py --selftest` | `selftest: 19/19 checks passed` | 0 |
| V-7 | assembler selftest | `python3 -B tools/assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| V-8 | typed-labels selftest | `python3 -B tools/gates/d4-typed-labels-check-gate.py --selftest` | `selftest: 163/163 checks passed` | 0 |
| V-9 | gate battery | `python3 -B tools/check-gate-battery.py` | `{battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}`; originals preserved | 0 |
| V-10 | v3 e2e default chain | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | `exit=0 fields=16/16 links=105/105 claims=27` | 0 |

**This is the plan's most important finding for the integrator:** the claim's `counting_command`
is `python3 -B reports/round-36/run-validation.py`, which **does not exist** at the baseline
(`reports/round-36/` holds only `claims.json targets.json telemetry/`). Claim D's threshold is
therefore unmeasurable as filed; the parent owns the verdict (R01 §0 row 8 says the same).

---

## 3. The verifying legs do not currently verify — four silent-acceptance classes (this seat's new measurement)

This is the part of the plan that is not a restatement. "Verified forms" is only a claim if a
tampered form **fails**. It does not. Four defects were injected, each into a **component**, then
**re-assembled** and graded in an isolated copy (`.scratch/iso`, `.scratch/iso2`, built with
`git archive HEAD | tar -x`; in-tree runners never executed). Re-assembly is what makes this a
real test: a hand-edited packet would only prove the pin catches byte drift, which is already known.

| # | injected defect (in the component) | argot gate | law gate | class |
|---|---|---|---|---|
| T-1 | `L-56` (`kit`) record **deleted** from `04-lexicon.yml` | `register_scoped=13 derived_pairs=7 … violations=0`, **exit 0** | `record_ids=182`, **exit 0** | **silent** |
| T-2 | `L-56` `stage: E1 → E0` (a register form before the register exists) | exit 0 | exit 0 | **silent** |
| T-3 | `L-56` `doublet_of: L-42 → L-99` (names no delivered record) | exit 0 | exit 0 | **silent** |
| T-4 | `L-56` `register: stamp → cant` (an undeclared register name) | exit 0 | exit 0 | **silent** |

Root causes, each cited to the code:

- **T-1 — the domain can shrink silently.** The gate *counts* the domain and prints it
  (`argot-derivation-gate.py:917-920`), but **nothing pins the expected count**. A grep over the
  whole tool tree finds `register_scoped`/`derived_pairs` only inside the gate itself — no
  `expected.json`, no baseline, no fixture asserts a number:
  `grep -rn "register_scoped\|derived_pairs" tools/` → 7 hits, **all in `argot-derivation-gate.py`**
  (single-file census: `... | sed 's/:.*//' | sort | uniq -c` → `7 tools/gates/argot-derivation-gate.py`).
  Worse, `claimed_chains` stayed at 8 while `derived_pairs` fell to 7, and the two are never
  compared. A form quietly disappearing is read as *a smaller domain*, not a defect — the
  `calibration` note at `argot-derivation-gate.py:68-70` states this limit in prose — "This gate is a
  **capability plus a replay**, not a clearance: exit 0 means 'every register-scoped form that
  states its inputs re-derives', not that the stratum is complete" — but nothing enforces it.
- **T-2 — the era leg has no emitter.** `D4L-ERA` is a **declared kind**
  (`tools/gates/register-law-gate.py:121` `DECLARED_KINDS = (… "era" …)`) and RGL-05 declares the
  rule (`13-register-law.yml:49`), but no code path emits it:
  `grep -rn "D4L-ERA" tools/ examples/` → **0 hits**. The r26 control C-E1 predicted exactly this
  (`reports/round-26/register/forms.md` §3: "the era leg is **not implemented** … C-E1 currently
  produces **no finding**. That is a named gap, not a pass").
- **T-3 — `doublet_of` is never resolved.** The field is in the contract
  (`packet.d4.yml:42`) and on all 8 records, but no leg reads it:
  `grep -rn "doublet_of" tools/ --include=*.py` → **0 hits**. The law gate's `design_row`
  resolver (`register-law-gate.py:362-368`) checks law rows, not lexicon back-pointers.
- **T-4 — an undeclared register name on a *form* is ungraded.** The law gate grades register
  names in `register_law` rows (`D4L-LAW-REGISTER`, `register-law-gate.py:47`) but the argot gate
  treats `register:` as free text when scoping a record.

**A fifth measurement, correcting my own first read.** `13-register-law.yml` is **absent** from the
r7 read set (`reports/round-34/handoff/declared-in-r7/expected.json#inputs` has 58 members; the D4
component membership is `01-brief.yml … 12-provenance.yml`, 19 D4 members total, component 13 not
among them). I initially read that as a blind spot; **it is not one.** The packet pins component 13
in its own `assembly.source_sha256` (`packet.d4.yml:2888`,
`c0d77181ac567c4c…`), and the r7 read set pins `packet.d4.yml`, so a component-13 edit is covered
**transitively**. Measured control: a genuinely undeclared force (`wibble-binding`) in component 13
**fires** `D4L-LAW-FORCE` (exit 1), and a component-13-only key moves the packet digest from
`aac91246cede` to `86e4ec73641a`, reddening the v3 e2e guard. Recorded here because the r7 row is
still worth a note in the freeze list (§5) — component 13 has no *direct* row, so a future round
that drops the packet's source-digest block would lose the cover.

**Plan consequence.** Any new register content must land **together with a count-and-invariant
guard**, or the round cannot honestly claim "verified". The guard is a **tool change**, which per
`targets.json` shared_rules is **drafted as a fenced block** for the integrator to apply, never
written into `tools/` by a seat.

---

## 4. The content design (the genuinely open surfaces, in landing order)

Three surfaces are open. They are ordered by cost; the plan recommends **A and B together** and
**C as the guard that makes them verifiable**.

### 4.1 Surface A — the `doublets:` block (the forecast's Δ2)

The assembler already admits it — `PACKET_KEYS` includes `"doublets"`
(`tools/assemble-culture-d4.py:81`), `RECORD_FIELDS["doublets"] = ("id",)` (`:122`), and the
assembler's own fixture template emits a `doublets:` block (`:469-471`) — but it is **empty**:

```
$ grep -c "doublets" examples/culture-d4/packet.d4.yml            # 0
$ for f in examples/culture-d4/components/*.yml; do grep -c doublets $f; done   # 0 for all 13
```

Design: 8 rows, one per register form, declared by `04-lexicon.yml` (the stratum's existing owner,
`reports/round-26/register/design.md` §6). Each row carries `id`, the pair members (`plain`, the
base id; `register_form`, the derived id), the operation, and the era. **No assembler edit is
needed** — `doublets` is in `PACKET_KEYS` and requires only `id`.

Reconciliation with D01: `reports/round-36/depth/D01-design.md:236-270` drafted this block first
and reached the same "no new assembler edit" reading. This plan adopts it and adds the era field,
which D01's draft omits and which T-2 shows is ungraded.

### 4.2 Surface B — the base-side pointer (the relation is one-directional)

Each register record points back (`doublet_of: L-42`); no base points forward. So a consumer
reading a **plain** record cannot tell a register form exists for it without scanning all 62
records. The eight pairs are already known and measured, so the move is cheap.

Two options, priced:
- **B-1 (recommended):** the `doublets` block of A **is** the forward index — no per-record edit,
  no contract change, no schema risk.
- **B-2:** a `register_form:` field on each of the 8 base records. This is a
  `contract.record_fields.lexicon` change, which is a **contract amendment** and a larger pin
  cascade. Recorded, not recommended.

D01 reached the same preference (`D01-design.md:299-300`).

### 4.3 Surface C — the guard (what makes A and B verifiable)

Drafted as fenced blocks for the integrator. Two independent guards, because T-1 and T-2/T-3/T-4
have different mechanisms:

```python
# DRAFT (fenced — integrator applies; seat writes no tools/ byte)
# GUARD-1, count pin: extend the argot gate's coverage leg so the delivered domain size is
# compared against a declared baseline rather than merely printed. The declaration lives beside
# the gate's existing fixture pin (argot-derivation-gate.py:103 EXPECTED_PATH) so the count is a
# checked fact, not a log line.
#
#   The pin is on `derived_pairs`, NOT on `register_scoped`: K01 measured that
#   register_scoped=14 decomposes as 8 register forms + 6 loan-layer borrow pairs
#   (L-49..L-54). Pinning register_scoped alone would conflate the stratum with the
#   loan layer and would NOT catch T-1 (which moved it 14->13 only because the
#   dropped record was a derived form; a dropped borrow pair would move it too).
#   borrow_pairs is pinned separately so the loan layer's shrinkage is still named.
#
#   REGISTER_DOMAIN_PIN = {"derived_pairs": 8, "borrow_pairs": 6}
#   ...
#   if counters["derived_pairs"] != REGISTER_DOMAIN_PIN["derived_pairs"]:
#       findings.append(("D4L-ARGOT-COVERAGE",
#           "register domain shrank: %d register forms replay, %d declared"
#           % (counters["derived_pairs"], REGISTER_DOMAIN_PIN["derived_pairs"])))
#   if counters["borrow_pairs"] != REGISTER_DOMAIN_PIN["borrow_pairs"]:
#       findings.append(("D4L-ARGOT-COVERAGE",
#           "loan layer shrank: %d borrow pairs delivered, %d declared"
#           % (counters["borrow_pairs"], REGISTER_DOMAIN_PIN["borrow_pairs"])))
#   if counters["claimed_chains"] != counters["derived_pairs"]:
#       findings.append(("D4L-ARGOT-COVERAGE",
#           "%d record(s) claim a derivation but %d replay"
#           % (counters["claimed_chains"], counters["derived_pairs"])))
#
#   NOTE (K01 §3): this gate is NOT in GATE_NAMES / D4_GATE_NAMES /
#   REGISTER_LAW_GATE_NAMES (check-gate-battery.py:117-132), so a pin landed here runs
#   only when the typed pipeline runs it as L3b-argot. Registering it in the battery is
#   part of this guard's work, not optional polish.
```

```python
# GUARD-2, era leg: emit the D4L-ERA class the law already declares (register-law-gate.py:121
# DECLARED_KINDS includes "era"; component 13 RGL-05 states the rule) over the register-scoped
# lexicon records. The gate has no era concept today (grep -c D4L-ERA tools/gates/*.py -> 0), so
# this is a new emitter, not a re-wire.
#
#   for rec in register_scoped_records:
#       if rec.get("register") == "stamp" and rec.get("stage") != "E1":
#           findings.append(("D4L-ERA", "FAIL",
#               "register form %s is stamped %s; the register is available_from E1 "
#               "(13-register-law.yml RGL-05)" % (rec["id"], rec.get("stage"))))
#   for rec in register_scoped_records:
#       if rec.get("doublet_of") and rec["doublet_of"] not in delivered_ids:
#           findings.append(("D4L-REGISTER-UNRESOLVED", "HOLD",
#               "register form %s names doublet_of %s, which no record delivers"
#               % (rec["id"], rec["doublet_of"])))
```

**Required negative controls** (each must fire, in the integrator's isolated copy, on the T-1..T-4
bytes this plan measured):
- T-1 → `D4L-ARGOT-COVERAGE` (`register_scoped` 13 ≠ 14)
- T-2 → `D4L-ERA`
- T-3 → `D4L-REGISTER-UNRESOLVED`
- T-4 → `D4L-LAW-REGISTER` on the record's `register` value (extension of the existing class)
- **and** a clean-packet control: the delivered bytes stay `exit 0` with zero new findings.

The last control is load-bearing: a guard that reddens the clean packet is not a guard, it is a
regression. All four T-* controls and the clean control must be run in the **same** isolated copy
and captured as command output.

---

## 5. The pin re-freeze list (new rows, never in-place edits)

Measured by injecting one legal content move (`L-56` gloss amended, arithmetic unchanged) into an
isolated copy and re-assembling. The packet digest moved `aac91246cede` → `3174cb4787e1` and the
following surfaces reddened. Each must be re-frozen as a **new row**; filed bytes stay untouched.

### 5.1 Live (non-filed) surfaces that must be re-pointed

| # | surface | what pins | re-freeze action |
|---|---|---|---|
| P-1 | `tools/gates/typed-pipelines.json` (`profiles[]` entry `id: d4`, `:4`) | `packet.sha256`, `projection.sha256`, `expected.sha256` | add a new `generation` row; keep `round-30-qreg-records` as a superseded row. Reddens as `FAIL L1-profile: packet: pins aac91246cede, live …` |
| P-2 | `examples/culture-d4/expected-holds.json` | `packet_sha256`, `projection_sha256`, `active_pin_generation` | append a `pin_generations[]` row; the r26 landing's `reports/round-26/register/repin.json` is the precedent for the row shape |
| P-3 | `tools/gates/expected/register-law-gate/r30-post/expected.json` | `gate_sha256`, `stdout_sha256`, packet read set | new baseline dir under a new id (r36-post); the r30-post dir stays byte-identical |
| P-4 | `tools/gates/expected/d4-assembly-check-gate/…` | packet + component tree | new baseline row |
| P-5 | `tools/gates/expected/d4-typed-labels-check-gate/…` | projection | new baseline row |
| P-6 | `tools/gates/frozen/…` (new `round-36/` manifest) | the leg verdicts over the new bytes | freeze a **new** `round-36/post-register` manifest; the r26 one replays red on a moved packet and is already filed as superseded (`reports/round-26/register/repin.json` `cascade_reported_not_repaired`) |

### 5.2 The r7 handoff row — a NEW row, and the `--freeze` prohibition

`reports/round-34/handoff/declared-in-r7/` pins `examples/culture-d4/packet.d4.yml` among its 58
read-set members, so a packet move reddens the v3 default chain (measured:
`E2E-DIGEST: examples/culture-d4/typed-labels.d4.yml assembly.packet_sha256: the tree recorded
aac91246cede… but the bytes measure 3174cb47…`).

**The r34 row is pinned and its `--freeze` is FORBIDDEN** by this round's hard boundaries. The
successor must be a new row built by `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze
reports/round-36/handoff/declared-in-r8` (a new directory) plus a re-point of the default pair —
`V3_BASELINE_DEFAULT` and `V3_FROZEN_DIR_DEFAULT`, live at `tools/exercise-handoff-e2e.py:1937-1938`
(the r34 repin row `R34-D-default-pointer` cites `:1933-1934`, its line numbers at that revision;
the file has since shifted) — exactly as r34 did for r7
(`reports/round-34/handoff/repin.json` rows `R34-D-default-pointer`, `R34-D-stale-row`). **This
plan does not perform that freeze** — it is the integrator's, after the content lands.

### 5.3 Note on component 13

`13-register-law.yml` has **no direct r7 read-set row** (58 inputs; `D4_COMPONENTS` = `01…12`), but
it is covered **transitively** via `packet.d4.yml`'s `assembly.source_sha256`
(`packet.d4.yml:2888`). If the freeze list is ever rebuilt, adding component 13 to
`D4_COMPONENTS` (`tools/exercise-handoff-e2e.py:157-170`) would make the cover direct rather than
derived. Recorded as a cheap hardening, not a defect.

### 5.4 Cascade order (matters — a self-referential pin trap)

The r26 landing recorded the trap: `tools/gates/typed-pipelines.json` pins the packet, and the
packet's own `assembly` block pins the assembler, so **the freeze must follow the re-point edit,
not precede it** (`reports/round-26/register/repin.json` `profile_repin` + `SCORECARD.md:330`).
Recommended order: content → assemble → projection (`d2-typed-labels.py --emit`) → typed packet
(`assemble-d4-typed.py`) → P-1/P-2 → gate baselines P-3/P-4/P-5 → frozen manifest P-6 → r8
handoff row §5.2.

---

## 6. What this plan recommends, and what it refuses

**Recommended (the minimum honest claim-D round):**
1. Surface A (the `doublets` block, 8 rows, era field included) — §4.1.
2. Surface B-1 (the `doublets` block **is** the forward index) — §4.2.
3. Surface C GUARD-1 + GUARD-2, with the five controls — §4.3.
4. **Surface D — the F-6 counter contract** (§7.1): the coverage block gains `derived_forms` /
   `derived_ok` so the derivation counts are a *checked key set*, not free-text log lines. K01
   measured this as the one forecast element with **no producer anywhere** in `examples/` or
   `tools/`; it is additive and it is the cheapest way to make GUARD-1's count pin contract-shaped
   rather than gate-internal.
5. The pin re-freeze list, new rows only — §5.

**Refused, with reasons:**
- **Re-authoring the eight form records.** They are delivered; doing it again duplicates filed
  bytes and cannot move the axis.
- **Claiming the `before→after` as filed.** The `before` is false and the `after` is already
  satisfied; the parent must re-scope or record the claim as premise-corrected, not passed.
- **B-2 (`register_form:` on base records).** A contract amendment; larger cascade for the same
  information B-1 carries for free.
- **Any in-place edit of a filed round-1..35 byte, and any `--freeze` of
  `reports/round-34/handoff/declared-in-r7`.**
- **Running any `reports/round-*/run-validation.py` in-tree.** Claim D's `counting_command`
  cannot be executed by any seat; the parent runs it at close.

**Named limits of this plan:**
- `head2`'s proper domain is **1 of 62**, not empty — `op_head2('haitun')` is the only proper
  derivation (`reports/round-36/depth/D06-gap-fill.md:178-193`). The r26 "empty proper domain"
  wording is superseded; the *substance* (no `head2` stratum is buildable) stands. This plan does
  not build one.
- The axis→operation rule's usable domain is **32 of 54 bases**, not the r26-filed 32/54-minus-13;
  re-measured 22 unusable (`reports/round-36/depth/D01-design.md` §4). Not this round's work, but
  any future form-set expansion inherits it.
- The four T-* defects were measured on **my own injected bytes**, not on a delivered defect. They
  prove the legs do not *detect* the classes; they do not prove the delivered tree *has* such a
  defect. The delivered tree is clean on every leg in §2.

---

## 7. Reconciliation with K01 (landed during this seat's run)

`reports/round-36/scout/K01-register-scout.md` landed after §0–§6 were written. It is the seat this
plan's mission names, so it is reconciled item by item rather than absorbed.

### 7.1 K01 findings this plan adopts (they extend it)

| # | K01 finding | effect on this plan |
|---|---|---|
| K1 | **F-6 has no producer.** `grep -rl "derived_forms\|derived_ok" examples tools` → **no match**; the forecast asked for those two keys **in the coverage block** (`reports/round-25/argot/forecast.md:33-41`), and the live block (`typed-labels.d4.yml:29-47`) carries none of them | **adopted as Surface D** (§6 item 4). This is a key-set mismatch, not a missing capability — the numbers exist under the names `derived_pairs`/`violations`. It makes GUARD-1 contract-shaped instead of gate-internal. |
| K2 | **The derivation leg is not battery-registered.** `check-gate-battery.py:130` registers `register-law-gate.py`; `argot-derivation-gate.py` is in **none** of `GATE_NAMES` / `D4_GATE_NAMES` / `REGISTER_LAW_GATE_NAMES` (`:117-132`) | **adopted.** GUARD-1 lands in the argot gate, so registering that gate in the battery is part of the guard work, not optional polish — otherwise the count pin runs only when the typed pipeline runs it. |
| K3 | **`register_scoped=14` decomposes as 8 forms + 6 borrow pairs** (`L-49..L-54`, the loan layer) | **adopted as a refinement of GUARD-1.** A bare `register_scoped == 14` pin would be **wrong** — it conflates the register stratum with the loan layer. The pin must be on `derived_pairs == 8` (the register's own share), with `borrow_pairs` pinned separately. This corrects my §4.3 draft, which pinned `register_scoped: 14`. |
| K4 | **The `26/26` component-digest check is transitive, not read-set-based.** `v3_verify_component_digests` (`exercise-handoff-e2e.py:2208`) reads digests from each packet's **own** `assembly` block, so 13 D4 components are verified while the read set names 12 | **adopted — it confirms my §5.3 from the other direction.** My control (a component-13 edit moves the packet digest, reddening the guard) and K01's reading agree: the cover is real but derived. §5.3's hardening note stands as the cheap fix. |

### 7.2 Where this plan and K01 differ

- **Scope of the residue.** K01 names three items (F-6, `head2`, RL-8/era). This plan names four
  surfaces and **splits K01's RL-8 in two**: the era rule (T-2, needs an emitter) and the
  `doublet_of` resolution (T-3, needs a resolver). K01 does not measure `doublet_of` at all; this
  plan does, and found it never read (`grep -rn "doublet_of" tools/ --include=*.py` → **0 hits**).
  K01's `head2` item is **not** in this plan's recommended set: it has no domain and D06 re-measured
  its proper domain at **1 of 62**, so building a `head2` stratum is not a claim-D move.
- **K01 does not measure the tamper classes.** Its §3 lists the legs as "all green, all current",
  which is true and is the same reading as this plan's §2 — but green-over-the-delivered-tree and
  *discriminating* are different claims, and T-1..T-4 show the difference. K01's §3 note that the
  argot leg "is reached through the typed pipeline but is not a battery-registered gate" is the
  closest it comes; it does not test whether either leg catches a shrunken domain.
- **K01 asks the planner to decide D's scope** (§6: "Either narrow D to the three-item residue, or
  re-scope it; the scout cannot decide that, the planner must"). **This plan's answer, as the
  planner:** narrow D to the four surfaces of §4 plus the guard of §4.3 and the re-freeze list of
  §5, and record the claim's `before`/`after_required` as **premise-corrected, not passed**. The
  load-bearing half of `after_required` was met three rounds before the claim was written; claiming
  it now would be claiming r26's work.

### 7.3 One correction to K01

K01 §5 says "`04-lexicon` … **is** a read-set member, only `13-register-law` is not". Confirmed by
this seat's own measurement (`declared-in-r7/expected.json#inputs`, 58 entries: `04-lexicon.yml`
present, `13-register-law.yml` absent). No disagreement — recorded because it is the load-bearing
fact for §5.2's re-point: editing `04-lexicon.yml` (the surface A/B owner) moves the r7 chain
**directly**, not only transitively.

---

## Owed

- `reports/round-36/scout/K01-register-scout.md` — **landed during this seat's run**; reconciled in
  §7 above. Its §6 hands the D-scope decision to the planner; §7.2 records this plan's answer.
- `reports/round-36/depth/D04-repin.md` — the pin re-freeze row authoring that §5 specifies.
  `D01-design.md:350` names this seat; it has not landed at write time.
- `reports/round-36/depth/D02-packet-draft.md` — the `doublets` block bytes as a fenced draft.
  Not landed at write time (`ls reports/round-36/depth/` → `D01, D03, D06, D09`).
- `reports/round-36/run-validation.py` — **does not exist**; claim D's `counting_command` is
  unrunnable by any seat (F-C13-1). The parent owns it.
- The GUARD-1/GUARD-2 fenced blocks of §4.3 are **drafts**; per shared_rules the integrator
  applies tool changes. No `tools/` byte was written by this seat.

## Citations

Every reading above is a command output or a `file:line`, all taken at
`ce103bf5885af00023cdc4a174c17602476cdcf8` with `TMPDIR=$PWD/.scratch` and
`PYTHONDONTWRITEBYTECODE=1`.

```sh
# domain non-empty (the claim's stale premise)
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
#   -> records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0 ; exit 0

# the four legs
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/register-law-gate.py --selftest          # 45/45
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # 20/20
python3 -B tools/gates/typed-pipeline-gate.py --selftest        # 19/19
python3 -B tools/assemble-culture-d4.py --selftest              # 81/81
python3 -B tools/gates/d4-typed-labels-check-gate.py --selftest # 163/163
python3 -B tools/check-gate-battery.py                          # pass 7 fail 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet   # exit 0

# the delivered content
sed -n '236,243p' examples/culture-d4/components/04-lexicon.yml      # L-55..L-62
grep -n "^registers:\|^register_law:" examples/culture-d4/packet.d4.yml   # :1329 :2788

# the four silent-acceptance classes (isolated git-archive copies; component tamper + re-assemble)
#   T-1 L-56 deleted      -> register_scoped=13 derived_pairs=7  exit 0
#   T-2 L-56 stage E1->E0 -> exit 0 (both gates)
#   T-3 L-56 doublet_of L-42->L-99 -> exit 0
#   T-4 L-56 register stamp->cant  -> exit 0
grep -rn "doublet_of" tools/ --include=*.py                      # 0 hits (never resolved)
grep -rn "D4L-ERA" tools/ examples/                              # 0 hits (declared kind, no emitter)
grep -rn "register_scoped\|derived_pairs" tools/                 # 7 hits, all in argot-derivation-gate.py

# the pins that move on a packet change
grep -rl "aac91246cede" tools/ examples/ | grep -v __pycache__
sha256sum examples/culture-d4/{packet.d4.yml,typed-labels.d4.yml,packet.d4.typed.yml,expected-holds.json} \
          examples/culture-d4/components/{04-lexicon.yml,13-register-law.yml} tools/gates/typed-pipelines.json

# the r7 read set (58 members; component 13 absent, covered transitively)
python3 -c "import json; d=json.load(open('reports/round-34/handoff/declared-in-r7/expected.json'))['inputs']; print(len(d)); print('13-register-law.yml' in d)"

# the doublets block is admitted but empty
grep -c "doublets" examples/culture-d4/packet.d4.yml             # 0
grep -n '"doublets"' tools/assemble-culture-d4.py                # :81 PACKET_KEYS, :122 RECORD_FIELDS
```

Peer fragments reconciled (read, not absorbed):
`reports/round-36/depth/D01-design.md` (§3.1 `doublets`, §4 rule domain),
`reports/round-36/depth/D03-isolated-verify.md` (§1 premise correction, §2 baseline legs),
`reports/round-36/depth/D06-gap-fill.md` (§2.2 `head2` 1-of-62),
`reports/round-36/depth/D09-gap-fill.md` (§1 premise correction),
`reports/round-36/review/R01-d-review.md` (§0 rows 1/6/7/8),
`reports/round-36/review/R03-cross-review.md` (§1 read set, component 13 transitive cover).

Filed sources cited: `reports/round-25/argot/current-state.md`, `reports/round-26/register/design.md`,
`reports/round-26/register/forms.md`, `reports/round-26/register/review.md`,
`reports/round-26/register/repin.json`, `reports/round-27/law/review.md`,
`reports/round-30/fixes/qreg-dangles.md`, `reports/round-34/handoff/repin.json`,
`SCORECARD.md:312,329,330,345,363`.
