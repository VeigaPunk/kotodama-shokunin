- Seat: P01 | planner | claim D | date 2026-10-19 | baseline 9bccc9b

# P01 — the residue execution plan for claim D (the register residue, correctly claimed)

- **Seat:** P01 (planner, claim **D**, depth), round 38, loop 1, position 6.
- **Mission (binding, `reports/round-38/targets.json`):** "Residue execution plan from K01."
- **Out:** this file only. No tool, gate, component, packet, pin or filed 1–37 byte written; no
  commit, no push. Every command ran with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
  from the lane root.
- **Canon:** NON-CANON engineering plan. No real language, institution, script or argot is
  described, cited or approximated. No clearance claimed.

## 0. Headline

Claim D is **executable as declared**, and this plan prices it with live measurements rather than
predictions. Two findings change the shape of the work:

1. **The F-6 emitter and the era leg are cheap and do not move a single frozen pin** — but only if
   they land in `tools/gates/argot-derivation-gate.py`, which is **not a read-set member** of the
   r7 freeze and **not a battery-registered gate**. Both facts are measured in §4. Every other
   candidate host reddens a filed artifact.
2. **The era leg, if it emits a `D4L-ERA`-class id, is invisible to the typed pipeline** — the
   pipeline filters the argot leg's output to `FINDING D4L-ARGOT-` (`typed-pipeline-gate.py:531`).
   A tampered packet would therefore read *green* through the pipeline. §6.2 prices both fixes.

I verified the whole landing end-to-end in an isolated `git archive` copy (§3): the era leg and the
two counters land, the delivered packet stays clean, the r26 C-E1 control fires with **exactly the
8 findings r26 predicted**, and every filed chain still exits 0.

**Dependency note.** The mission says "from K01", but `reports/round-38/scout/K01-residue.md` does
not exist at write time (`ls reports/round-38/` → `claims.json targets.json telemetry`). This plan
therefore derives its before-state from the **filed** r36 census the claim itself names
(`reports/round-36/scout/K01-register-scout.md`) and re-measures every load-bearing number on the
delivered revision at `9bccc9b`. Where r38-K01 later disagrees, this plan is subordinate to the
filed measurement — recorded under `## Owed`.

## 1. The before-state, re-measured at `9bccc9b` (not inherited)

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit=0

$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0
exit=0

$ grep -rl "derived_forms\|derived_ok" examples/ tools/          # no match, exit 1
$ grep -c "D4L-ERA" tools/gates/argot-derivation-gate.py         # 0
```

| the claim's `before` asserts | measured at `9bccc9b` | evidence |
|---|---|---|
| "no derived_forms/derived_ok emitter anywhere in examples/ or tools/" | **confirmed** — `grep -rl` → no match, exit 1 | §1 command block; matches `reports/round-36/depth/D06-gap-fill.md:230-239` |
| "RL-8 era leg missing" | **confirmed** — the gate has no era concept; `DECLARED_KINDS` already carries `"era"` but nothing grades dating | `tools/gates/register-law-gate.py:121`; `grep -c D4L-ERA` → 0 |
| the argot/law/typed legs are otherwise green | **confirmed** — argot exit 0, law exit 0, typed pipeline 20/20, battery 7 pass / 20 baselines pinned, handoff-v3 exit 0 packet `45f57132…` | §4.1 |

Unlike r36, this claim's `before` is **not stale**: both residues are real and both are unclaimed
work. That is the whole reason r36's D was rejected and this one is executable
(`reports/round-36/validation.json:53`).

## 2. What each half of claim D actually requires

### 2.1 (a) The F-6 counters

`reports/round-17/d4/design-brief.md:306-307` fixes signature (b) as "the coverage block reports
`derived_forms` and `derived_ok` counts that agree". The requirement, stated exactly:

- two counters, **agreeing** (i.e. `derived_forms == derived_ok` is the clean condition);
- reported in **the coverage block** — the block the projection carries and the gate prints.

The numbers already exist under different names. The argot gate computes both:

- `derived_pairs` — incremented once per record carrying a `derived_from`/`derivation` pair
  (`argot-derivation-gate.py:567`), i.e. the **derived forms counted**;
- `violations` — incremented whenever the declared chain does not yield the candidate
  (`:571,587,619,626,652`), i.e. the **derived forms that did not check**.

So the honest emitter is `derived_forms = derived_pairs` and `derived_ok = derived_pairs -
violations`, and it is a **key-set addition, not a new capability** — exactly the reading
`reports/round-36/plan/P01-d-plan.md:389` recorded. Delivered values would be `derived_forms=8`,
`derived_ok=8`.

**Consumers.** Two, and they are different:

1. `tools/gates/typed-pipeline-gate.py:517-541` runs the argot gate as leg `L3b-argot` and grades
   its FAIL lines. It reads the gate's **stdout**, so a coverage-line addition is visible to it only
   if the pipeline is taught to read it — today it is not (`:530-531` takes only `FINDING` lines).
2. `tools/d2-typed-labels.py:2879-2892` builds the **projection's** `coverage` block that lands in
   `examples/culture-d4/typed-labels.d4.yml`. This is the block a reader actually inspects.

**These two are not the same target, and the difference decides the cascade (§4).** The forecast
says "the coverage block"; the delivered coverage block is the projection's. But the projection is
produced by a **read-set member** (`tools/d2-typed-labels.py` — §4.2), so emitting there reddens the
r7 chain. Emitting on the gate's own `coverage:` line satisfies the same sentence at zero pin cost.
This plan recommends the gate line as the primary host and names the projection as an optional
second half with its price stated (§5).

### 2.2 (b) The RL-8 era leg

`reports/round-26/register/rules.md:107-112` §5 specifies the rule verbatim:

```
rule REGISTER-ERA-01:
  a record with register == "stamp" must carry stage >= E1
  a `stamp` record with stage E0  ->  D4L-ERA (FAIL)
```

and `:151` files the control `C-E1`: a probe with every `stage: E1` rewritten to `stage: E0` must
emit the era FAIL. `reports/round-27/law/impl-8.md:68` files the gap as `RL-8`, owner "whoever grows
the leg". The declared kind already exists (`register-law-gate.py:121` `DECLARED_KINDS` includes
`"era"`), and the rule is stated in packet bytes (`examples/culture-d4/components/13-register-law.yml:49`
RGL-05, `:57` `enforcement:` "The era leg (RGL-05) is specified and unimplemented").

**One correction to the r26/r36 framing, measured (§3.3).** "A record with `register == "stamp"`" is
the spec's own wording, and it is load-bearing. The argot gate's `record_register()` is **broader**
than that: when a record declares no `register:` of its own it resolves the record's
`loan_layer`/`layer` through the packet's `layers` block and returns **that layer row's**
`register:` value (`argot-derivation-gate.py:377-388`). The two delivered loan records `L-53 'gal'`
and `L-54 'mar'` carry `loan_layer: "North-road kin layer"` and `stage: "E0"` but **no `register:`
field of their own** (`packet.d4.yml:969-982`, `:989-1002`); the layer row `LY-02` they resolve to
carries `register: "craft"` (`packet.d4.yml:1207-1222`, the field at `:1221`). So `record_register()`
returns `craft` for them, and an era leg written against it fires on both — **2 false findings on
the clean delivered packet**. A leg written against the record's own `register:` field, scoped to
`stamp`, fires on none. Both readings are in §3.3 with outputs. This is the single implementation
decision most likely to produce a false red, and it is the D02/D05 pair's first obligation.

## 3. The landing, verified in isolation before it is planned

All of §3 ran in `git archive HEAD` copies under `.scratch/p01h/repo/` — the delivered tree was
never written. The patch is a fenced draft for the integrator (§3.4), not an applied edit.

### 3.1 The emitter and the coverage line

A counter assignment at the end of `evaluate_packet` plus two keys on the existing print:

```
derived_forms = derived_pairs
derived_ok    = derived_pairs - violations
```

Measured on the delivered packet:

```
coverage: … derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0 derived_forms=8 derived_ok=8
exit=0
```

The two keys agree, and they agree **non-vacuously**: `derived_pairs=8` is a real member set
(`reports/round-36/scout/K01-register-scout.md:110` F-5), so `derived_ok=8` is not an
empty-set pass. A shrunken domain would move both and break the agreement — which is what makes the
pair a contract rather than a log line.

### 3.2 The era leg, correctly scoped

Scoped to the record's own declared `register:` value:

```
for each form record with declared register == "stamp":
    if stage < "E1"  ->  FINDING D4L-ERA: FAIL — register-scoped form <id> '<term>'
                         (register 'stamp') is claimed at stage '<stage>';
                         the register is available_from E1 (13-register-law.yml RGL-05)
```

| # | fixture | command | result |
|---|---|---|---|
| A | delivered packet | `argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **exit 0**, `D4L-ERA` count **0** |
| B | C-E1 control — all 21 `stage: "E1"` rewritten to `stage: "E0"` in a scratch copy | `argot-derivation-gate.py .scratch-ctl-E0.yml` | **exit 1**, `D4L-ERA` count **8** |

Control B reproduces r26's prediction **exactly** — 8 findings, one per delivered stamp form
(`reports/round-26/register/rules.md:151`; `reports/round-36/depth/D01-design.md:314` "a probe with
every stage: E1 -> E0 must emit 8 findings, exit 1"). That is the discriminating control the
r36 census said no seat had built (`reports/round-36/depth/D06-gap-fill.md:113-120`).

### 3.3 The false-positive trap, measured both ways

| era-leg scoping | delivered packet | reading |
|---|---|---|
| `record_register(entry, layers)` (the gate's own broader resolver) | **exit 1, 2 × `D4L-ERA`** — `L-53 'gal'` and `L-54 'mar'`, both `register 'craft'`, `stage 'E0'` | **false red.** These are the loan-layer records, not stamp forms. The leg would break the delivered tree. |
| the record's own `register:` field, scoped to `stamp` | **exit 0, 0 findings** | correct |

The spec's own words are `register == "stamp"` (`rules.md:111`). The broader resolver is right for
the *derivation* leg (it must see layer-scoped loans — that is why `borrow_pairs=6`) and wrong for
the *era* leg (RGL-05 governs the stamp register only). Recorded because it is the difference
between a green landing and a rejected one, and because a reviewer re-deriving from
`record_register()` will get a different answer.

### 3.4 The fenced draft (integrator applies; no in-tree edit made)

```python
# fenced draft — tools/gates/argot-derivation-gate.py
# (1) the era leg, inserted in evaluate_packet before `declared_ops = packet_declares_ops(packet)`
    # RL-8 / REGISTER-ERA-01 (reports/round-26/register/rules.md section 5; RGL-05).
    # Scoped to the record's OWN declared register, not record_register(): the latter
    # also resolves loan layers, and two delivered loans are register "craft" at E0.
    for block, entries in record_blocks(packet):
        for position, entry in enumerate(entries):
            if not is_form_record(entry):
                continue
            declared_register = text_of(entry.get("register")).strip()
            if declared_register.casefold() != "stamp":
                continue
            stage = text_of(entry.get("stage")).strip()
            if stage and stage.upper() < "E1":
                counters["era_failures"] += 1
                findings.append(finding(
                    "D4L-ARGOT-ERA", "FAIL",           # id choice: see section 6.2
                    "register-scoped form %s %r (register %r) is claimed at stage %r; "
                    "the register is available_from E1 (13-register-law.yml RGL-05, "
                    "REGISTER-ERA-01 / RL-8)"
                    % (record_id(entry, block, position), record_form(entry),
                       declared_register, stage)))

# (2) the F-6 counters, at the end of evaluate_packet before `return`
    # F-6 signature (b), reports/round-17/d4/design-brief.md:306-307.
    counters["derived_forms"] = counters["derived_pairs"]
    counters["derived_ok"] = counters["derived_pairs"] - counters["violations"]

# (3) the coverage line gains the two keys (the existing print, two appended %d)
    ... "rule_holds=%d derived_forms=%d derived_ok=%d"
        ... totals["rule_holds"], totals["derived_forms"], totals["derived_ok"]))
```

Selftest additions (the claim's ">=2 controls" bar — §7.3 of the O claim is the sibling's, this is
D's):

```python
# fenced draft — tools/gates/argot-derivation-gate.py selftest()
    # the era leg discriminates, and it is scoped to `stamp` alone
    era_ctl = E0_STAMP_CONTROL          # a committed control with the 8 stamp forms at E0
    checks.append(("era-leg-fires-on-E0-stamp", bool(_classes(run(era_ctl)[1], "D4L-ARGOT-ERA"))))
    checks.append(("era-leg-silent-on-delivered", not _classes(
        run(DELIVERED_PACKET_TEXT)[1], "D4L-ARGOT-ERA")))
    checks.append(("era-leg-ignores-loan-layers", not _classes(
        run(LOAN_LAYER_CONTROL)[1], "D4L-ARGOT-ERA")))   # the section 3.3 trap, pinned
    # the F-6 counters agree, and they agree non-vacuously
    _c, _f, _t = run(POSITIVE_CONTROL)
    checks.append(("f6-counters-agree", _t["derived_forms"] == _t["derived_ok"]))
    checks.append(("f6-counters-non-vacuous", _t["derived_forms"] > 0))
```

`era-leg-ignores-loan-layers` is the control that makes §3.3 permanent rather than a note.

## 4. The cascade — measured, host by host

This is the section the integrator needs. Every row is a live measurement in an isolated copy, not
an inference. The two governing facts:

- **`tools/gates/argot-derivation-gate.py` is NOT a member of the r7 read set.**
  `reports/round-34/handoff/declared-in-r7/expected.json#inputs` has 58 entries;
  `grep`-confirmed absence. Editing it → handoff-v3 **exit 0, packet `45f57132…` unchanged**.
- **`tools/d2-typed-labels.py` IS a read-set member.** Editing it → handoff-v3 **exit 1**,
  `E2E-DIGEST: … expected-holds.json projector_sha256: the tree recorded 2819f68769df… but the
  bytes measure 842e8e213dde…`.

### 4.1 The baseline chain at `9bccc9b` (pre-change control)

```
python3 -B tools/gates/argot-derivation-gate.py --selftest     # 27/27
python3 -B tools/gates/register-law-gate.py --selftest        # 45/45
python3 -B tools/gates/typed-pipeline-gate.py --selftest      # 19/19
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # 20/20 legs
python3 -B tools/assemble-culture-d4.py --check               # byte-identical deterministic assembly
python3 -B tools/check-gate-battery.py                        # exit 0, 7 pass, 20 baselines pinned, coverage 10/10
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet  # exit 0, fields=16/16, links=105/105, packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

### 4.2 What each candidate host costs

| host | in r7 read set? | battery-registered? | measured effect of an edit | verdict |
|---|---|---|---|---|
| `tools/gates/argot-derivation-gate.py` | **no** | **no** (`check-gate-battery.py:117-132`: absent from `GATE_NAMES`, `D4_GATE_NAMES`, `REGISTER_LAW_GATE_NAMES`) | handoff-v3 **exit 0**, packet `45f57132…` **unchanged**; battery **exit 0**; typed pipeline **20/20** (`L3b-argot` ok); own selftest 27/27 → re-pinned count | **free — recommended host** |
| `tools/gates/register-law-gate.py` | no | **yes** (`REGISTER_LAW_GATE_NAMES`) | battery **exit 2**, `BASELINE-GATE-REVISED`: "gate_sha256 15f8b23251ca2ad0… differs from the live register-law-gate.py …: re-freeze, never compare across an unnamed revision". handoff-v3 still exit 0. | reddens a filed baseline → needs a **new** `tools/gates/expected/register-law-gate/r38-post/` freeze row |
| `tools/d2-typed-labels.py` (the projection) | **yes** | yes (as a pin inside `d4-typed-labels-check-gate` baselines) | handoff-v3 **exit 1** `E2E-DIGEST`; `examples/culture-d4/expected-holds.json` carries `projector_sha256: 2819f687…` at 4 places, all of which must move; typed pipeline stays 20/20 (its `L4-pins` reads `typed-pipelines.json`, not the projector) | reddens the r7 chain → needs a new pin generation row |
| `examples/culture-d4/typed-labels.d4.yml` (the projection output) | **yes** | yes | same class as above, plus `typed-pipelines.json` `profiles[0].projection.sha256` | reddens the r7 chain |

**The honest reading.** The claim's `after_required` says "the counters emit from the
packet/components (or **a documented equivalent** the legs can count)". The gate's `coverage:` line
is that documented equivalent: same two keys, same agreeing relation, same consumer-visible place,
**zero filed pins moved**. The projection route is also legal but buys a pin cascade and an
`expected-holds.json` rewrite for the same two integers. This plan recommends the gate host and
prices the projection route as an optional second half (§5, R-3).

### 4.3 What the gate host does **not** need

No new `tools/gates/expected/…` baseline, no `typed-pipelines.json` generation row, no
`expected-holds.json` `pin_generations[]` row, no packet/component edit, no assembler edit, no
`--freeze`, no re-freeze of `declared-in-r7`. The r26 four-site cascade
(`reports/round-26/register/repin.json`) was triggered by editing **components**; this landing edits
none. That is the difference between r36's refused "re-author the forms" route and this one.

### 4.4 One opt-in: battery registration

`argot-derivation-gate.py` is a real gate that the battery does not know about
(`check-gate-battery.py:117-132`; also named in `reports/round-36/scout/K01-register-scout.md:99-102`
as K2). Registering it — adding it to `REGISTER_LAW_GATE_NAMES` — makes the battery demand a
baseline for it. Measured in a scratch copy:

```
REGISTER_LAW_GATE_NAMES = ("register-law-gate.py", "argot-derivation-gate.py")
→ battery exit 2   (BASELINE-GATE-UNCOVERED: argot-derivation-gate.py has no committed expected.json)
```

So registration is **in-scope only with** a new `tools/gates/expected/argot-derivation-gate/r38-post/`
freeze row and its mirrored read set (packet + gate + naming-collision-gate + the new control
fixture). That is real operability work and it is the O block's territory, not D's — recorded here so
R03 can see the collision: **if O registers the argot gate while D grows it, the freeze row must pin
D's post-change bytes, so the freeze must follow D's landing** (the r26 ordering trap:
`reports/round-36/plan/P01-d-plan.md:336`).

## 5. The work order

| # | step | command | expected | why in this order |
|---|---|---|---|---|
| R-1 | apply the §3.4 draft to the argot gate | — | — | nothing downstream moves; the gate is unread-set |
| R-2 | add the 5 selftest checks of §3.4 + the 2 control fixtures | `python3 -B tools/gates/argot-derivation-gate.py --selftest` | 32/32 (27 + 5), was 27/27 | the controls must exist before the count is pinned |
| R-3 | *(optional, priced)* add `derived_forms`/`derived_ok` to the **projection** coverage block | `python3 -B tools/d2-typed-labels.py --emit …` | `typed-labels.d4.yml` moves | **only** if the integrator accepts the §4.2 cascade: new `typed-pipelines.json` generation row, `expected-holds.json` `pin_generations[]` row, `projector_sha256` ×4 |
| R-4 | run the D legs on the delivered revision | `argot … packet.d4.yml`; `register-law … packet.d4.yml`; `typed-pipeline-gate.py … packet.d4.yml` | exit 0; `derived_forms=8 derived_ok=8`; 0 `D4L-ARGOT-ERA`; 20/20 | claim's counting commands |
| R-5 | run the controls | C-E1 scratch control; the loan-layer control | exit 1 with 8 era findings; exit 0 | the discriminating pair |
| R-6 | verify no filed artifact moved | `assemble-culture-d4.py --check`; `check-gate-battery.py`; `exercise-handoff-e2e.py --profile v3 --quiet` | byte-identical; exit 0 / 20 pinned; exit 0 packet `45f57132…` | the no-harm proof |
| R-7 | land the pin record **as new rows** | — | — | only if R-3 was taken; §4.3 says none are needed for R-1/R-2 |
| R-8 | integration order if O also lands | — | — | D's bytes first, then the O guard, then any freeze row (r26 ordering trap) |

**Re-pin list for the recommended route (R-1 + R-2): empty.** Stated explicitly because every prior
register round carried one and a reader will expect it. For R-3 the list is:
`typed-pipelines.json profiles[0].{packet,projection,expected}.sha256` (new generation row, keep
`round-30-qreg-records` as superseded), `expected-holds.json` `projector_sha256` ×4 +
`pin_generations[]` row, and a new `tools/gates/expected/d4-typed-labels-check-gate/r38-post/` freeze
row — the shape `reports/round-26/register/repin.json` and `reports/round-30/fixes/qreg-dangles.md`
already establish. Filed rows are appended, never edited.

## 6. Named risks, with the measurement behind each

### 6.1 The era leg's scoping (§3.3) — highest risk

Wrong scoping turns the delivered tree red with 2 false findings. Mitigation: the
`era-leg-ignores-loan-layers` selftest check. Owner: D02 (design) + D05 (verify).

### 6.2 The era leg's finding id is invisible to the typed pipeline — measured, and the D block must decide

`tools/gates/typed-pipeline-gate.py:530-533`:

```
argot_lines = [line for line in proc.stdout.splitlines()
               if line.startswith("FINDING D4L-ARGOT-")]
result["argot_lines"] = argot_lines
argot_fails = [line for line in argot_lines if "FAIL" in line]
```

The filter keeps only `FINDING D4L-ARGOT-` lines. An era FAIL emitted as `D4L-ERA` — the id r26 and
r36 both name (`reports/round-26/register/rules.md:112`; `reports/round-36/depth/D01-design.md:172`)
— is **dropped before `argot_fails` is computed**, so `check("L3b-argot", …)` passes and the pipeline
reports a tampered packet as green. This is precisely the vacuous-pass class X02 and D10b exist to
hunt, and it is a *new* one, not a restatement.

Two fixes, both cheap, and they are **not equivalent**:

| fix | consequence |
|---|---|
| emit the id as `D4L-ARGOT-ERA` (family-consistent with `D4L-ARGOT-DERIV`/`-RULE`/`-COVERAGE`/`-DATA`) and name `D4L-ERA` / `RGL-05` / `REGISTER-ERA-01` in the message text | pipeline sees it immediately; the r26-filed id survives as a resolvable token in the message; **no pipeline edit** |
| keep the id `D4L-ERA` and widen the pipeline filter at `:531` | id fidelity to the r26 record; costs a `typed-pipeline-gate.py` edit and a re-pin of that gate's own selftest expectation |

This plan **recommends the first** and records the second as the alternative, because the id is the
pipeline's contract surface and the r26 name is preserved inside the message either way. **The
integrator must decide and the decision must be recorded**, since r26 filed `D4L-ERA` as the id and
a reader grepping for it will otherwise find nothing. Owner: integrator; the D10b seat's mission
("the F-6 emitter's output consumed by the argot leg (not just present) — a vacuous-pass guard") is
the natural place to verify whichever is chosen.

### 6.3 The `derived_ok == derived_forms` agreement is satisfiable by a broken gate

If `violations` were miscounted, both keys move together and still agree. Mitigation: the
`f6-counters-non-vacuous` check (`derived_forms > 0`) plus the existing
`fixture-ids-match-expected-file` and `positive-control-clean` checks, which pin `violations`
independently. The agreement is a contract only in combination with a non-zero count — recorded so
the pair is not presented as stronger evidence than it is.

### 6.4 The claim's own `after_required` names a pin update that the recommended route does not need

`after_required` says "pins updated as new rows". On the recommended route **no pin moves**, so this
clause is satisfied vacuously and must be **reported as such, not ticked**. The honest verdict
wording is: "no pin cascade was triggered because the changed instrument is outside every frozen
read set; the clause is met in the trivial sense and this is recorded rather than presented as
re-pinning work". A reader who sees "pins updated" should be able to find the rows; there are none.

## 7. Reconciliation with the claim and with r36

- **Claim D is executable as declared.** Unlike r36, the `before` re-measures true (§1). The claim
  does **not** need the r36 "premise-corrected" treatment.
- **The claim's `after_required` is met by §3** — "the counters emit from the packet/components (or
  a documented equivalent the legs can count)" → the gate's coverage line; "the era leg runs" → §3.2
  control B, 8 findings; "argot/law/typed legs green with the new coverage named" → §4.1 + R-4;
  "pins updated as new rows" → §6.4, vacuously, and named as such.
- **The claim's threshold** is "two independent verifiers; legs green; the new coverage named (no
  vacuous-pass)". The two verifiers are the D05/D06 pair, and §6.2/§6.3 are the two vacuous-pass
  hazards they must attack. D10b is the third, on consumption.
- **What this plan refuses**, with reasons: re-authoring the register forms (delivered since r26;
  `reports/round-36/validation.json:53`); building a `head2` stratum (proper domain is 1 of 62,
  `reports/round-36/depth/D06-gap-fill.md:178-193`); renaming `derived_pairs` away
  (`reports/round-36/depth/D06-gap-fill.md:239-244` — the leg's contract is its own and is
  documented); any edit to `13-register-law.yml` or `04-lexicon.yml` (both trigger the four-site
  component cascade for no depth gain); any in-place edit of a filed byte; any in-tree execution of
  `reports/round-*/run-validation.py` (F-C13-1); any re-freeze of
  `reports/round-34/handoff/declared-in-r7`.
- **Where this plan differs from r36's P01.** r36 §6 recommended Surface A (`doublets`, 8 rows) and
  Surface B-1 alongside Surface D; both required **component** edits and the full cascade. This plan
  recommends neither: the r36 round was rejected and nothing landed, so the residue is unchanged and
  the cheapest honest claim-D move is the two-instrument route of §3, which touches no component at
  all. Surface A/B-1 remain open and are not this claim's.

## Owed

- **`reports/round-38/scout/K01-residue.md`** does not exist at write time. This plan used the filed
  r36 census (`reports/round-36/scout/K01-register-scout.md`) and re-measured every load-bearing
  number itself. If r38-K01 lands a different F-6 consumer map or era-leg spec, this plan is
  subordinate to it.
- **The era-leg finding id** (§6.2) — decision owed by the integrator; two options priced, neither
  chosen by this seat.
- **`reports/round-38/run-validation.py`** does not exist yet, so claim D's third counting command
  (`python3 reports/round-38/run-validation.py`) is `to-verify` until the integrator lands it. Per
  F-C13-1 it must not be run in-tree regardless.
- **The projection-side F-6 half** (§4.2 R-3) — priced, not recommended, not decided here.
- **Battery registration of the argot gate** (§4.4) — O's territory; the D/O ordering constraint is
  recorded for R03, not resolved.
- **Not measured by this seat:** whether the `D4L-ARGOT-ERA` id survives the typed pipeline's JSON
  output path (`typed-pipeline-gate.py:996-1000` `document["argot"]`) end-to-end; the code reading
  at `:531` is conclusive for the *check*, but the JSON consumer was not exercised. D10b's job.

## Citations

All commands from the lane root with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; isolated
copies under `.scratch/p01*/repo/` via `git archive HEAD`. Baseline `git rev-parse HEAD` →
`9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`.

Digests of the instruments this plan's numbers bind to (measured 2026-10-19):

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3  tools/d2-typed-labels.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
```

Measurements run:

```
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml      # exit 0; derived_pairs=8 violations=0
python3 -B tools/gates/argot-derivation-gate.py --selftest                            # 27/27
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml         # exit 0; law_rows=5 findings=0
python3 -B tools/gates/register-law-gate.py --selftest                                # 45/45
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml       # 20/20, ok L3b-argot
python3 -B tools/gates/typed-pipeline-gate.py --selftest                              # 19/19
python3 -B tools/assemble-culture-d4.py --check                                       # byte-identical deterministic assembly
python3 -B tools/check-gate-battery.py                                                 # exit 0; 7 pass, 20 pinned, coverage 10/10
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                         # exit 0; packet 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
grep -rl "derived_forms\|derived_ok" examples/ tools/                                 # no match, exit 1
grep -c "D4L-ERA" tools/gates/argot-derivation-gate.py                                # 0
```

Isolated-copy probes (`.scratch/p01*/repo/`, delivered tree untouched):

```
# read-set collision
append to tools/d2-typed-labels.py      -> handoff-v3 exit 1  E2E-DIGEST projector_sha256 2819f687… vs 842e8e21…
append to tools/gates/argot-derivation-gate.py -> handoff-v3 exit 0  packet 45f57132…
# baseline-pin collision
append to tools/gates/register-law-gate.py     -> battery exit 2  BASELINE-GATE-REVISED 15f8b232… vs 6860758a…
append to tools/gates/argot-derivation-gate.py -> battery exit 0  findings 0
REGISTER_LAW_GATE_NAMES += argot-derivation-gate.py -> battery exit 2  BASELINE-GATE-UNCOVERED
# the landing, applied
era leg + F-6 counters, stamp-scoped -> delivered exit 0, 0 D4L-ERA, derived_forms=8 derived_ok=8
era leg + F-6 counters, C-E1 control (21 × stage E1->E0) -> exit 1, 8 × D4L-ERA
era leg scoped via record_register() -> delivered exit 1, 2 × D4L-ERA (L-53 'gal', L-54 'mar', register 'craft')
patched gate selftest -> 27/27 (no check lost); typed pipeline 20/20; battery exit 0; handoff-v3 exit 0 packet 45f57132…
```

Source lines cited: `tools/gates/argot-derivation-gate.py:109,304-314,335-341,360-411,516-541,543-670,567,571,587,619,626,652,662,885-928`;
`tools/gates/register-law-gate.py:100-200,320-420,440-545,590-647` (esp. `:121` `DECLARED_KINDS`);
`tools/gates/typed-pipeline-gate.py:517-541,530-533,996-1000`;
`tools/check-gate-battery.py:117-132,155-162,494-600,700-800`;
`tools/d2-typed-labels.py:2879-2892,2965-2976`;
`tools/exercise-handoff-e2e.py:157-169,1939-1953`;
`examples/culture-d4/packet.d4.yml:40-41,1009-1178,1220`;
`examples/culture-d4/components/04-lexicon.yml:236-243,244-260`;
`examples/culture-d4/components/13-register-law.yml:45-49,57`;
`examples/culture-d4/typed-labels.d4.yml:5,9,29-47,295`;
`reports/round-17/d4/design-brief.md:296-310`;
`reports/round-25/argot/forecast.md:33-41`;
`reports/round-26/register/rules.md:107-128,151`;
`reports/round-26/register/execution-3.md:74`;
`reports/round-27/law/impl-8.md:55-80`;
`reports/round-34/handoff/declared-in-r7/{expected.json (58 inputs); freeze.txt:7; packet.md}`;
`reports/round-36/scout/K01-register-scout.md:99-142,205-215`;
`reports/round-36/depth/D01-design.md:150-200,300-330`;
`reports/round-36/depth/D06-gap-fill.md:91-135,220-270`;
`reports/round-36/plan/P01-d-plan.md:336,344-397`;
`reports/round-36/validation.json:53,59,147`;
`tools/gates/expected/register-law-gate/r30-post/expected.json`;
`tools/gates/typed-pipelines.json` (profiles[0]);
`examples/culture-d4/expected-holds.json` (`projector_sha256` ×4).
