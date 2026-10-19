- Seat: K01 | scout | claim D | date 2026-10-19 | baseline 9bccc9b

# R38-K01 — register-residue scout: the F-6 counter contract and the RL-8 era leg

**Mission (verbatim, `reports/round-38/targets.json` seat `K01`):** "Register-residue scout:
the exact F-6 counter requirements (what `derived_forms`/`derived_ok` should emit and who
consumes it — argot gate L3b, typed pipeline), the RL-8 era-leg spec from the r27/r28 law
records; which files change."

**Write scope.** This file only. No tool, gate, packet, component, fixture, pin, expectation
row or filed round-1..37 byte written; `git status --porcelain` at the stamp shows only
`?? reports/round-38/`. Every isolated-copy control below ran under
`.scratch/k38/{iso,iso2}/` (gitignored, built by `git archive HEAD | tar -x`). No commit, no
push, no install, no network. No `reports/round-*/run-validation.py` was executed in-tree
(F-C13-1); `reports/round-38/run-validation.py` does not exist at this stamp
(`ls` → No such file), so claim D's declared counting command is `to-verify` and this file
uses the underlying gate commands instead.

**Stamp.** `date -u +%FT%TZ` → **2026-10-19T11:09:27Z**; `git rev-parse --short HEAD` →
`9bccc9b`. All measurements from lane root with `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`.

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth, never clearance.

---

## 0. Headline — four findings the D block must not build past

1. **F-6's producer does not belong in the argot gate.** The forecast asks the *coverage
   block* for the two counters, and the coverage block is the **projection's**
   (`examples/culture-d4/typed-labels.d4.yml`), built by `tools/d2-typed-labels.py`. The argot
   gate prints a different, stdout-only `coverage:` line. A change confined to the gate cannot
   satisfy F-6 as specified.
2. **Nothing consumes the counters — so a bare key addition is a vacuous pass.** No code path
   reads `derived_forms`/`derived_ok`, and the typed pipeline's `L3b-argot` leg never parses
   the gate's coverage line. §3.2 measures this; the D block's threshold ("no vacuous-pass")
   needs a consumer, not just a producer.
3. **The F-6 change costs a re-pin cascade of 4 moved read-set rows plus the frozen r7
   baseline**, which claim D's `after_required` does not cover ("filed bytes untouched except
   the two named tool/example artifacts"). Measured end-to-end in an isolated copy: §4.
4. **RL-8's substance is enforceable in the existing law gate without new bytes in the
   packet**, because `registers.QREG-04` already carries the machine-readable floor. §5.2.

---

## 1. The two residues, as declared and as filed

| residue | declared where | filed disposition |
|---|---|---|
| F-6 counters | `reports/round-17/d4/design-brief.md:306-307` — "the coverage block reports `derived_forms` and `derived_ok` counts that agree" | r26 `reports/round-26/register/execution-3.md:74`: "**not designed**; the leg reports `derived_pairs`/`violations` instead"; r26 `reports/round-26/argot/D24-forecast-closure.md:87` re-measures `derived_forms` → 0 files anywhere |
| RL-8 era leg | r26 `reports/round-26/register/rules.md:110-126` (`REGISTER-ERA-01`, "specified here and unimplemented"); r27 `reports/round-27/law/rules.md:173-192` (`RLAW-04`, "a finding (id unassigned)") | r27 `reports/round-27/law/impl-8.md:68` files `RL-8`, owner "whoever grows the leg"; r27 `reports/round-27/argot/D20-gap-closure-record.md:168`: "**still open, carried** … `x59` catches the era plant (`L4-FAIL`) but no delivered gate does" |

Both are carried into r38 by r37's queue: `reports/round-37/op/O01-queue-draft.md:119`
(`R36-D-F6`, "no producer exists for the named counters") and `:153` (`R36-D-RL8`, "the law
can declare era but no gate grades the E0/E1 dating constraint"). The r36 D claim was
**rejected as declared** (`reports/round-36/validation.json` claims.D: `"D: claim failed as
declared — the before-state … is stale"`), and nothing landed under it.

---

## 2. F-6 — the exact requirement

### 2.1 What must emit, and where

The requirement's own counting command, filed at r26
(`reports/round-26/argot/D24-forecast-closure.md:151`), names the file:

```
| coverage block | grep -c "derived_forms\|derived_ok" examples/culture-d4/typed-labels.d4.yml | ≥1 each |
```

So F-6 is a **projection** requirement, and the producer is the projector:

- the live coverage block is `examples/culture-d4/typed-labels.d4.yml:29-47`, 13 keys:
  `typed_labels`, `labels_by_kind`, `label_findings_fail`, `label_findings_hold`,
  `rank_rules_component`, `rank_rules_normalized`, `rank_rules_gate_projected`,
  `rank_rules_unresolved_items`, `rank_quarantine_handles`, `reconciliation_records`,
  `conflicts`, `findings_total`, `findings_hold_or_fail` — **neither counter present**
  (measured: `json.load(...)['coverage']`, sorted keys above).
- the producer is `tools/d2-typed-labels.py:2879-2895`, the `coverage = { ... }` literal,
  emitted into the projection at `:2918` (`"coverage": coverage`).
- the argot gate's own line is a **different contract**: `tools/gates/argot-derivation-gate.py:917-920`
  prints `coverage: <path> records=… register_scoped=… derived_pairs=… claimed_chains=…
  borrow_pairs=… violations=… rule_holds=…`. `derived_pairs` is a real number (8 over the
  delivered packet) but under a key set the forecast does not name.

**Measured, live:**

```
$ for t in derived_forms derived_ok derived_pairs; do printf "%-16s examples=%s tools=%s\n" ...; done
derived_forms    examples=0 tools=0
derived_ok       examples=0 tools=0
derived_pairs    examples=0 tools=2      # tools/gates/argot-derivation-gate.py only (+ its .pyc)
```

`grep -rl "derived_pairs" tools/ examples/` → `tools/gates/argot-derivation-gate.py` and
`tools/gates/__pycache__/argot-derivation-gate.cpython-314.pyc`. **One producer, one file.**
This confirms the r36 census at a new baseline; the finding has not moved since `ce103bf`.

### 2.2 What the counters should mean, from the delivered domain

The forecast's wording is "counts that **agree**", and its sibling clause is F-5
(`design-brief.md:305-306`): "every derived quote form's check **passes in the delivered
packet (zero fails)**". Reading the two together, the pair is a producer/consumer split:

- `derived_forms` = how many register-scoped forms declare a derivation at all;
- `derived_ok` = how many of those re-derive (i.e. `derived_forms` minus the violations).

Over the delivered tree the honest values are therefore **8 and 8**, and the agreement
`derived_ok == derived_forms - violations` is what "agree" means. Both numbers already exist
under other names: `derived_pairs=8` and `violations=0` on the gate's line (§2.1). The
distinction is not informational, it is **contractual** — F-6 asks for the pair in the
projection so the hold-set pins can bind it (r25 `reports/round-25/argot/delta.md:198`: "new
coverage keys + gate leg + **expectation row**"; `:148` Δ-step 4: "so `expected-holds.json`
can pin it … a new leg with no expectation row is not a delivered leg").

### 2.3 The derivation census the counters must reproduce

Parsed from the packet's own bytes (the projector's own reader, `runpy` over
`tools/gates/naming-collision-gate.py`), records carrying a `derivation` mapping:

| id | term | base | construction | `register` | `stage` |
|---|---|---|---|---|---|
| L-55 | tuum | tum | STAMP-LENGTHEN | stamp | E1 |
| L-56 | kit | tik | STAMP-REVERSE | stamp | E1 |
| L-57 | lom | mol | STAMP-REVERSE | stamp | E1 |
| L-58 | nees | nes | STAMP-LENGTHEN | stamp | E1 |
| L-59 | huum | hum | STAMP-LENGTHEN | stamp | E1 |
| L-60 | mees | mes | STAMP-LENGTHEN | stamp | E1 |
| L-61 | reek | rek | STAMP-LENGTHEN | stamp | E1 |
| L-62 | saam | sam | STAMP-LENGTHEN | stamp | E1 |

**Eight, and the count is not a coincidence of the register stratum**: the projection's own
label census marks exactly **10** records with `route: derived` — the 8 above plus `L-46
mesar` and `L-47 kalen` (`construction: CRAFT-AGENT` / `ATTRIBUTIVE`, `register: null`,
`derived_from: null`). So a producer that counts `route == "derived"` would emit **10**,
and one that counts a `derivation` mapping emits **8**. That is the one design decision the
emitter carries, and it must be stated: **the forecast's relation is the `derived_from` +
`derivation` pair** (`design-brief.md:303`, F-3), so the correct domain is the 8, not the 10.

`L-46`/`L-47` are also the reason a naive "count the derived ones" emitter would silently
disagree with the gate's `derived_pairs=8` and the D block would ship a counter that does not
match the leg it is supposed to pin.

---

## 3. Who consumes it — and why the naive fix is vacuous

### 3.1 The declared consumers, tested

The mission names two candidate consumers: "argot gate L3b, typed pipeline".

| candidate | does it read the counters? | evidence |
|---|---|---|
| `L3b-argot` in the typed pipeline | **No** | `tools/gates/typed-pipeline-gate.py:524-541` runs the sibling gate and keeps only lines matching `line.startswith("FINDING D4L-ARGOT-")` (`:530`); `argot_lines` feeds `argot_fails` (`:533`), which feeds the check (`:539`). The gate's `coverage:` line is discarded. |
| the typed pipeline's selftest | **No — substring only** | `tools/gates/typed-pipeline-gate.py:1471`: `check("argot derivation leg: the mirrored leg runs on the family packet", argot_probe.returncode in (0, 1) and "coverage:" in argot_probe.stdout, ...)`. It asserts the literal word `coverage:` appears, not any key. |
| `expected-holds.json` | **No** | its `holds` rows are `D2L-FORM-UNRESOLVED` etc.; no derivation counter appears. |
| `tools/exercise-handoff-e2e.py` (v3) | **No — a fixed key list** | `:2165-2185` `v3_mine_d4_labels` reads exactly `typed_labels`, `labels_by_kind`, `findings_total`, `findings_hold_or_fail`, `rank_rules_unresolved_items`, `rank_quarantine_handles`, `conflicts`, `reconciliation_records`, `assembly.packet_sha256`, `assembly.reader_sha256`; `:2167` raises if the four **top-level** keys `coverage`/`era_reconciliation`/`rank_rules`/`assembly` are absent — new keys *inside* `coverage` are read by nobody. |
| `tools/d2-typed-labels.py`'s own `--check` | **No** | `--check` is byte-identity of the projection against a fresh build (`tools/gates/d4-typed-labels-check-gate.py:21-22`), not a key-set assertion. |
| `tools/assemble-d4-typed.py` | **No** | its `coverage` (`:377`) is the **routing-table** coverage, a different object entirely. |

**Consequence, stated plainly.** Adding the two keys to `coverage = {...}` produces a
delivered artifact that no leg reads. Under the claim's own threshold ("the new coverage
named (no vacuous-pass)") that is exactly a vacuous pass: the counters would be present in
the projection and asserted by nothing. The honest fix therefore has **two** halves — a
producer *and* a consumer — and the D block must name the consumer before it claims F-6.

### 3.2 The consumer that costs nothing: the gate's own expectation

The one consumer available without a new pin surface is the **argot gate's selftest**, which
already evaluates packets through the same code path the legs use
(`argot-derivation-gate.py:760-846`). A control that asserts the pair agrees —
`totals["derived_pairs"] == expected_derived_forms` and `violations == 0` — is a real
assertion over the delivered packet, runs in-tree, and is already registered in the battery's
gate set. The selftest currently carries **27** checks
(`python3 -B tools/gates/argot-derivation-gate.py --selftest` → `selftest: 27/27 checks passed`);
a non-vacuous F-6 control would move that count. **This is the cheapest honest consumer and
this scout recommends it as the named consumer for the D claim.**

The alternative consumer — `exercise-handoff-e2e.py`'s `v3_mine_d4_labels` — is *also*
available and costs no new file, but it changes the v3 assembled packet and therefore the r7
frozen baseline row (§4). Recorded, not recommended for this round.

---

## 4. The F-6 pin cascade, measured in an isolated copy

Claim D's `after_required` says "filed bytes untouched except the two named tool/example
artifacts". **That is not what F-6 costs.** Measured by applying the change in a `git archive`
copy (`git archive HEAD | tar -x -C .scratch/k38/iso2`) and converging the chain.

### 4.1 The naive emitter drifts the D2 baseline too

The first emitter tried was unconditional — the two keys added to `coverage` at
`tools/d2-typed-labels.py:2894` for every family. Measured in `.scratch/k38/iso`:

```
projector selftest                      163/163 -> 162/163
  failure: boundary compatibility: D2 projection keeps its exact baseline digest
           (tools/d2-typed-labels.py:3115 asserts the D2 serialized projection ==
            a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43)
examples/culture-d2/typed-labels.d2.yml  a3aa452cd5ae77c3 -> 422fa211da002aa4   (MOVED)
```

The D2 projection carries its own `coverage` block (it has 2 occurrences of `"coverage"`),
so an unconditional emitter moves `examples/culture-d2/typed-labels.d2.yml` — a **filed D2
artifact**, pinned in `examples/culture-d2/expected-holds.json:4`, in the frozen round-23
generation (`tools/gates/frozen/round-23/repin-d2/freeze.txt:11`, "(unchanged)"), and in the
projector's own hard-coded literal at `tools/d2-typed-labels.py:3115`. That is a D2-tree
regression bought for a D4 counter, and it is a **harm to the operability axis** the round
must not take.

### 4.2 The family-guarded emitter leaves D2 byte-identical

Measured in `.scratch/k38/iso2` with the emitter guarded on family:

```python
# DRAFT — reports/round-38/scout/K01-residue.md §4.2; NOT APPLIED.
# tools/d2-typed-labels.py, immediately after the `coverage = { ... }` literal at :2879-2895
# (before `shown = shown_path(packet_path)` at :2896):
    if family != DEFAULT_FAMILY:
        deriv = [e for e in (packet.get("lexicon") or [])
                 if isinstance(e, dict) and isinstance(e.get("derivation"), dict)]
        coverage["derived_forms"] = len(deriv)
        coverage["derived_ok"] = len(deriv)
```

`DEFAULT_FAMILY` is the module's own declared constant (used at `:2560`, `:2789`, `:2837`,
`:2855`), so the guard is the projector's existing idiom, not a new concept. Result:

```
d4 emit exit=1 (the delivered packet carries 12 declared holds; exit 1 is its clean verdict)
projector selftest                      163/163 checks passed
examples/culture-d2/typed-labels.d2.yml a3aa452cd5ae77c3   (UNMOVED — byte-identical)
d4 coverage                            derived_forms 8 / derived_ok 8
```

`derived_ok` above is the **provisional** form of the counter (it equals `derived_forms`
because `violations=0` on the delivered packet). An honest emitter should read the
violation count from the replay rather than assume zero; the draft above is deliberately the
cheapest shape that proves the guard works, and the D executor owns the final form.

### 4.3 The residual cascade is exactly 4 moved read-set rows

With the guarded emitter applied and the chain converged (regenerate the D4 typed packet via
`tools/assemble-d4-typed.py --emit`; re-point `expected-holds.json`'s `projection_sha256` and
`projector_sha256`; re-point `typed-pipelines.json` profile `[0]`'s `projection.sha256` and
`expected.sha256`), the isolated copy measures:

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: E2E-DIGEST: 4 read-set file(s) changed since the baseline was frozen:
  examples/culture-d4/expected-holds.json, examples/culture-d4/packet.d4.typed.yml,
  examples/culture-d4/typed-labels.d4.yml
```

and the row-by-row comparison against `reports/round-34/handoff/declared-in-r7/expected.json`:

| read-set row | r7 frozen | after the F-6 change |
|---|---|---|
| `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cf` | `2921ba9a69bf` |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c8` | `6908a1af60e8` |
| `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384` | `1c012da026ed` |
| `tools/d2-typed-labels.py` | `2819f68769df` | `431f5728d6a6` |
| **moved** | | **4** |

Note the trap in the message itself: it reports `4 file(s)` but names only **three** —
`tools/exercise-handoff-e2e.py:1445` renders `', '.join(drifted[:3])`. A verifier who counts
the names in the message will undercount by one; the row-by-row census above is the
authoritative count, and `tools/d2-typed-labels.py` is the row the message hides.

Every other leg of the converged chain is green in the isolated copy:

```
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   -> summary: 20/20 legs passed
python3 -B tools/gates/d4-typed-labels-check-gate.py                             -> byte-identical deterministic projection (exit 0)
python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml -> byte-identical deterministic assembly
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml -> derived_pairs=8 violations=0 (exit 0)
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml     -> findings=0 (exit 0)
python3 -B tools/d2-typed-labels.py --selftest                                    -> 163/163
python3 -B tools/check-gate-battery.py                                            -> pass 7 / fail 0 / unevaluable 0, coverage 10/10
```

**The one thing the isolated copy cannot converge** is the frozen r7 baseline itself: the
`E2E-DIGEST` above *is* the r7 row refusing the change, which is the correct behaviour and
is precisely why the D claim's "two named artifacts" budget is wrong. The r7 row may not be
re-frozen this round (`targets.json` shared_rules; `claims.json` non_goals: "no re-freeze of
`declared-in-r7`"). So F-6 as specified **cannot** land green inside this round's declared
byte budget, and the D block must either (a) scope the emitter to the gate's selftest
consumer of §3.2, which moves no read-set row at all, or (b) report the 4-row cascade as
owed to the next re-freeze.

---

## 5. RL-8 — the era-leg spec and its cleanest landing

### 5.1 The spec, from the law records

Two filings specify the same mechanism in two vocabularies:

```
reports/round-26/register/rules.md:110-112        rule REGISTER-ERA-01:
                                                    a record with register == "stamp" must carry stage >= E1
                                                    a `stamp` record with stage E0  ->  D4L-ERA (FAIL)
reports/round-27/law/rules.md:175-178             rule RLAW-04:
                                                    a row with register == "stamp" and a speech_act must carry era_rule >= E1
                                                    a stamp-act claimed at E0  ->  a finding (id unassigned)
```

`RGL-05`'s own substance, landed in the packet:

- `examples/culture-d4/components/13-register-law.yml:49` — `kind: era`, `register: stamp`,
  `consequence: "every stamp form is available_from E1, the era 03-orthography dates the
  stamp-house to; an E0 stamp claim is a defect and E3 is reserved and unoccupied"`.
- `examples/culture-d4/packet.d4.yml:2854` (`id: "RGL-05"`) and `:2863` (the same
  `consequence` string).
- the component's own `law_binding.enforcement` (`13-register-law.yml:57`) already *declares*
  the gap: "no gate executes these rows. The era leg (RGL-05) is specified and unimplemented
  — `tools/gates/argot-derivation-gate.py` has no era concept … The rows are a declared law
  with named non-execution, not a claim of enforcement."

### 5.2 The floor is already machine-readable — in a different block

The critical finding for the landing decision: **the era floor does not have to be added to
the packet.**

| block | row | field | value | file:line |
|---|---|---|---|---|
| `registers` | QREG-04 | `era_rule` | `"a stamp form is available_from E1"` | `examples/culture-d4/packet.d4.yml:1366`; component `examples/culture-d4/components/04-lexicon.yml:253` |
| `registers` | QREG-05..08 | `era_rule` | `"E1"` (bare) | `packet.d4.yml:1381,1396,1411,1426` |
| `register_law` | RGL-05 | `consequence` | prose only — **no machine field** | `packet.d4.yml:2863` |

So the law gate can read the floor from `registers.QREG-04.era_rule` — a field the packet
already carries and that `contract.record_fields_amendments.R30-QREG-ACTS`
(`packet.d4.yml:124-138`) already lists among the act rows' `additional_fields` — and needs
**no packet byte**. This matters because any packet edit re-opens the full pin cascade of §4
*plus* the frozen r7 baseline; a gate-only change does not.

The two open ownership questions, carried from the filings, are:

- `reports/round-27/law/rules.md:226` (`RU-L5`): "`RLAW-04`'s era bound reads `era_rule`,
  which the contract does **not** list — `contract.record_fields.registers` has no
  `era_rule`; `QREG-04` carries the field anyway. A contract change would silently empty the
  rule's domain." The amendment at `:124-138` covers the **act** rows QREG-05..08; it does
  **not** amend the base `record_fields.registers` list, so `QREG-04`'s `era_rule` remains an
  undeclared field. A gate that reads it inherits that exposure, and the D block should name
  it.
- r36 `reports/round-36/depth/D06-gap-fill.md` §2.1 owed the same decision as "which block
  owns the era floor (`registers` QREG-04 vs the `register_law` RGL-05 row)".

### 5.3 The change site, with the gate's own idiom

`tools/gates/register-law-gate.py` is the right gate and the only one that already has the
pieces:

- `:121-122` — `DECLARED_KINDS` **already contains `"era"`**, so the kind is declared vocabulary;
- `:231-243` — `declared_registers(packet)`, which collects every `registers` row's `id`,
  `register` and `title` — the resolution surface the draft's floor lookup joins;
- `:337-341` — the gate already resolves each row's `register` against that set;
- `:353-357` — it already reads `kind` and validates it against `DECLARED_KINDS`;
- `:204-211` — `law_rows(packet)` returns `(identity, speech)`; the `identity` half is the
  `registers` block the era floor is read from (`:252` unpacks it in `evaluate_packet`);
- `:605` in the sibling `tools/gates/lexicon-coverage-audit.py` — `_era_index(eras, era)`,
  the ordinal resolution the draft below reuses; the packet's `eras` list is
  `["E0","E1","E2","E3"]` (parsed from `packet.d4.yml`'s `eras:` block);
- `:424-432` — `_tamper_law_field`, the gate's existing single-token tamper helper the
  selftest uses to prove each clause fires;
- `:561-585` — the delivered-packet tamper control loop (force / speaker / speaker-id /
  consequence), the pattern a new era control would join.

```python
# DRAFT — reports/round-38/scout/K01-residue.md §5.3; NOT APPLIED.
# tools/gates/register-law-gate.py: a record-side era leg for RGL-05's substance.
#
# New finding id, additive to the existing D4L-LAW-* set:
#     D4L-LAW-ERA   a register-scoped record's stage predates the era floor the
#                   law declares for its register                          [FAIL]
#
# Resolution, in evaluate_packet() beside the existing clause resolutions
# (after the `register`/`axis`/`kind` block, ~:337-357):
#   floor = None
#   for row in identity:                      # `registers` rows, already read at :200-215
#       if row.get("era_rule") and row.get("register") in registers:
#           m = re.search(r"\bE(\d)\b", text_of(row["era_rule"]))
#           if m: floor = "E%d" % int(m.group(1)); break
#   eras = packet.get("eras") or []
#   floor_at = _era_index(eras, floor) if floor else None
#   if floor_at is not None:
#       for block, rows in record_blocks(packet):      # lexicon etc.
#           for row in rows:
#               if text_of(row.get("register")).strip() != "stamp": continue
#               stage_at = _era_index(eras, text_of(row.get("stage")).strip())
#               if stage_at is not None and stage_at < floor_at:
#                   counters["era_failures"] += 1
#                   findings.append(finding(
#                       "D4L-LAW-ERA", "FAIL",
#                       "record %s carries register 'stamp' at stage %r, before the floor %s "
#                       "the `registers` block declares (%s); RGL-05's dating constraint is "
#                       "violated" % (row.get("id"), row.get("stage"), floor, ...)))
#
# `_era_index` is the sibling audit's own ordinal resolver
# (tools/gates/lexicon-coverage-audit.py:605) and should be re-declared here rather than
# imported, matching this gate's existing read-only-by-path discipline (it loads only
# naming-collision-gate.py, :175-181).
#
# Selftest additions required by the gate's own discipline (:560-582 pattern):
#   delivered-era-tamper-adds-a-line   an E1 stamp form moved to E0 -> exactly one new
#                                      D4L-LAW-ERA line naming the record
#   delivered-era-clean-identical      the delivered packet's line set is unchanged
#   era-floor-read-from-registers      the floor resolves from QREG-04's era_rule
```

**Measured, that control's two directions** (this seat's own fixtures under `.scratch/k38/`,
delivered tree untouched):

| # | fixture | edit | argot gate | law gate | lexicon audit |
|---|---|---|---|---|---|
| A | `.scratch/k38/packet-E0-stamp.yml` | record `L-56 kit` `stage: "E1"` → `"E0"` (1 line changed) | exit **0**, `violations=0` | exit **0**, `findings=0` | exit **1**, `FINDING D-stage-mismatch: 'kit' is formed in 'E0' but construction 'STAMP-REVERSE' is only available from 'E1'` |
| B | `.scratch/k38/packet-E0-both.yml` | A, plus all 7 `available_from: "E1"` → `"E0"` | exit **0** | exit **0** | exit **0**, 0 findings |

**Reading.** Control A fires, so the tree is not blind to an E0 stamp record — but the firing
finding is `D-stage-mismatch`, a **construction-availability** check in the lexicon audit,
not the register-era rule. Control B isolates this: widen the construction's own availability
and the E0 stamp record sits there with **zero findings anywhere**. The only era protection
over the stamp register is incidental to `constructions[].available_from`
(`STAMP-REVERSE`/`STAMP-LENGTHEN` at `packet.d4.yml:1274-1304`, both `available_from: E1`);
`RGL-05`'s substance is enforced by nothing. This independently reproduces r36
`reports/round-36/depth/D06-gap-fill.md` §2.1's two-way control at the r38 baseline, by the
same method, on a different tree revision.

**A trap the D block must respect.** `tools/d2-typed-labels.py` resolves the D2 rank
component relative to the **packet's own directory** (r27 `reports/round-27/law/impl-8.md`
§2.2: two byte-identical packets report `findings_total=12` in place and `16` out of tree).
Every packet-level control for RL-8 must therefore be run **in place with a verified
byte-for-byte restore**, or in an isolated copy at the same relative path — never by copying
a packet out of the tree.

---

## 6. Which files change — the answer the planner asked for

### F-6 (as specified: the counters in the coverage block)

| file | change | verdict |
|---|---|---|
| `tools/d2-typed-labels.py` | the guarded emitter of §4.2 (after `:2895`) | **required** — the producer |
| `tools/gates/argot-derivation-gate.py` | a selftest control asserting the pair agrees (§3.2) | **required for non-vacuity** — the consumer |
| `examples/culture-d4/typed-labels.d4.yml` | regenerated (`coverage` gains 2 keys) | **moved bytes** |
| `examples/culture-d4/expected-holds.json` | `projection_sha256`, `projector_sha256` → new rows | **moved bytes** |
| `examples/culture-d4/packet.d4.typed.yml` | regenerated (its `assembly` pins the projection) | **moved bytes** |
| `tools/gates/typed-pipelines.json` | profile `[0]` `projection.sha256`, `expected.sha256` | **moved bytes** |
| `reports/round-34/handoff/declared-in-r7/expected.json` | 4 read-set rows | **MOVED — and forbidden this round** |

If the D block takes the §3.2 consumer only (the gate selftest) and **does not** land the
emitter, then **no artifact byte moves at all** and the counters remain undelivered — which
would be an honest *partial* F-6, and must be reported as such, never as delivered.

### RL-8 (the era leg)

| file | change | verdict |
|---|---|---|
| `tools/gates/register-law-gate.py` | `D4L-LAW-ERA` resolution + `era_failures` counter + `coverage:` line key + 2–3 selftest controls | **required** — the leg |
| `examples/culture-d4/packet.d4.yml` | **none** — the floor is already at `registers.QREG-04.era_rule` (`:1366`) | **no change** |
| `examples/culture-d4/components/13-register-law.yml` | the `law_binding.enforcement` prose (`:57`) still says the era leg is unimplemented | **stale after landing** — must be brought in line, which is a *filed-ish* component edit; see §7 |
| `tools/gates/expected/register-law-gate/r30-post/` | the gate's frozen baseline pins `gate_sha256 15f8b232…` | **moved** — the battery's duty-2 check compares `gate_sha256` against the live script (`tools/check-gate-battery.py:528-543`, `gate_revised`) |

**That last row is load-bearing and easy to miss.** `tools/gates/expected/register-law-gate/r30-post/expected.json`
carries `"gate_sha256": "15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169"` and
`"inputs"` naming both the packet and `tools/gates/register-law-gate.py`. Editing the gate
makes the battery's duty-2 read `gate_revised` unless a new baseline generation is committed.
The battery currently reports `pass 7 / fail 0 / unevaluable 0`, `coverage 10/10`
(`python3 -B tools/check-gate-battery.py`, exit 0), and the round must not leave that red.
By contrast the **argot** gate has no committed `expected/` baseline at all
(`ls tools/gates/expected/` → `costume-era-consistency-gate d4-assembly-check-gate
d4-typed-labels-check-gate phonology-sanity-gate register-law-gate`), so editing the argot
gate costs no baseline generation. **That asymmetry is the reason the §3.2 F-6 consumer is
the cheap one and the RL-8 gate edit is not.**

---

## 7. Contested scope — reported, not absorbed

1. **The `derived_forms`/`derived_ok` domain.** Count the 8 `derivation` records or the 10
   `route: derived` records (§2.3)? The forecast's F-3 names the `derived_from`+`derivation`
   pair, so 8; but this is a contract decision, not a measurement. **Owner: the D planner /
   integrator.**
2. **The consumer.** §3.2's gate selftest (free, no pin) versus the v3 e2e's
   `v3_mine_d4_labels` (also free of new files, but changes the assembled packet and hence
   the r7 row). **Owner: the D planner.**
3. **The r7 re-freeze.** The 4-row cascade of §4.3 cannot be absorbed this round. Either the
   claim is scoped to the no-byte consumer, or the cascade is filed as owed to the next
   re-freeze. **Owner: the integrator** (`claims.json` non_goals forbids the re-freeze).
4. **The era floor's owner.** `registers.QREG-04.era_rule` (`:1366`) vs a new machine field
   on the `register_law` RGL-05 row. The former costs no packet byte and is what `RU-L5`
   names as the rule's intended source. **Owner: the D planner** (r36 `D06` owed the same).
5. **`RU-L5`'s contract exposure.** `QREG-04.era_rule` is not in the base
   `contract.record_fields.registers` list; the `R30-QREG-ACTS` amendment (`:124-138`) covers
   only QREG-05..08. A gate reading `QREG-04.era_rule` inherits that exposure. **Owner:
   the integrator** — a contract amendment is a packet change with its own cascade.
6. **`13-register-law.yml:57`'s enforcement prose.** It currently *asserts* the era leg is
   unimplemented. An RL-8 landing makes that sentence false, and the component is not one of
   claim D's "two named tool/example artifacts". **Owner: the D planner** — either name the
   component as a third artifact or leave the prose stale and record it.

---

## 8. What this seat did **not** do

- Did not write, edit or create any tool, gate, packet, component, fixture, pin,
  `expected-holds.json` row, `typed-pipelines.json` row or frozen baseline. Every control
  lives under `.scratch/k38/` (gitignored).
- Did not run any `reports/round-*/run-validation.py` in-tree (F-C13-1); none was executed in
  the isolated copies either. `reports/round-38/run-validation.py` does not exist.
- Did not re-freeze or touch `reports/round-34/handoff/declared-in-r7` — its bytes are pinned;
  the isolated copy *read* `expected.json` and the r7 chain still exits 0 unchanged in-tree:
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0,
  `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
- Did not edit `reports/round-38/claims.json` or `targets.json`, or any filed round-1..37 byte.
- Did not commit, push, install, or reach the network.
- Did not decide any contested item in §7.

---

## Owed

- **The F-6 consumer's exact shape** — which leg asserts the pair, and against which
  expectation row. This scout names two candidates (§3.1, §3.2) and recommends the gate
  selftest; the choice is the D planner's. **Owner: P01 / the D executor.**
- **The emitter's `derived_ok` semantics** — the draft's `derived_ok = derived_forms`
  assumes `violations == 0`, which is true over the delivered packet and false in general. An
  honest emitter must read the violation count from the replay. **Owner: the D executor (D01).**
- **The 4-row re-pin cascade + the frozen r7 row** (§4.3) — not absorbable this round.
  **Owner: the r38 integrator.**
- **`tools/gates/expected/register-law-gate/r30-post/`** — a new baseline generation is owed
  if the RL-8 leg lands, or the battery reads `gate_revised`. **Owner: the r38 integrator.**
- **`reports/round-38/run-validation.py`** does not exist at this stamp, so claim D's declared
  counting command (`python3 reports/round-38/run-validation.py`) is `to-verify`. **Owner:
  the r38 validation-leg seat (S01).**
- **Not measured by this seat:** whether the r7 frozen chain's own `inputs` map is the right
  place to absorb the cascade (that is claim O's roster defect, seat K02's mission), and
  whether `head2`'s proper domain (r36 §2.2: 1 of 62, `L-48 haitun`) belongs in the D claim
  — the r38 `claims.json` D claim does not name it.

## Citations

**Files (sha256 measured 2026-10-19T11:09:27Z, cwd = lane root, `TMPDIR=$PWD/.scratch`):**

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287  tools/gates/lexicon-coverage-audit.py
2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3  tools/d2-typed-labels.py
92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0  tools/assemble-d4-typed.py
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
76ecdfdcbf09c3c7f384d74cd81ddc5e57ef261a4be4267579081766fa8b986d  tools/gates/typed-pipelines.json
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43  examples/culture-d2/typed-labels.d2.yml
```

**Commands run (all from lane root unless the cwd is named; `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):**

```
# §0/§1 — the tree and the residues' current state
git rev-parse --short HEAD                                                  # 9bccc9b
git status --porcelain                                                      # only "?? reports/round-38/"
date -u +%FT%TZ                                                             # 2026-10-19T11:09:27Z
for t in derived_forms derived_ok derived_pairs; do ...; done               # 0/0, 0/0, 0/2
grep -rl "derived_pairs" tools/ examples/                                   # argot gate + its .pyc
ls reports/round-38/run-validation.py                                       # No such file

# §2 — the requirement and the domain
python3 -c "json.load(open('examples/culture-d4/typed-labels.d4.yml'))['coverage']"   # 13 keys, neither counter
python3 -c "<runpy naming gate; census lexicon records with a derivation>"   # L-55..L-62 = 8
python3 -c "<projection label census by route>"                             # route==derived = 10

# §3 — the consumer test
grep -n "ARGOT_GATE" tools/gates/typed-pipeline-gate.py                     # :84 decl, :517-541 leg
sed -n '1471p' tools/gates/typed-pipeline-gate.py                           # "coverage:" substring only
grep -n "derived_pairs\|derived_forms" tools/gates/typed-pipeline-gate.py   # no hits

# §4 — the cascade, in isolated copies
git archive HEAD | tar -x -C .scratch/k38/iso   ;  cd .scratch/k38/iso
  # (naive emitter applied) python3 -B tools/d2-typed-labels.py --selftest   # 162/163
  #                         sha256sum examples/culture-d2/typed-labels.d2.yml # 422fa211… (MOVED)
git archive HEAD | tar -x -C .scratch/k38/iso2  ;  cd .scratch/k38/iso2
  # (family-guarded emitter applied)
  python3 -B tools/d2-typed-labels.py --selftest                            # 163/163
  sha256sum examples/culture-d2/typed-labels.d2.yml                         # a3aa452c… (UNMOVED)
  python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml \
      --emit examples/culture-d4/typed-labels.d4.yml                        # exit 1; derived_forms 8 / derived_ok 8
  python3 -B tools/assemble-d4-typed.py --emit examples/culture-d4/packet.d4.typed.yml
  python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet             # E2E-DIGEST: 4 read-set rows
  python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml  # 20/20
  python3 -B tools/check-gate-battery.py                                    # pass 7 / fail 0 / unevaluable 0
  python3 -c "<compare every baseline['inputs'] row against live>"          # 4 moved rows

# §5 — RL-8's two-way control (fixtures under .scratch/k38/)
python3 -B tools/gates/argot-derivation-gate.py .scratch/k38/packet-E0-stamp.yml   # exit 0, violations=0
python3 -B tools/gates/register-law-gate.py     .scratch/k38/packet-E0-stamp.yml   # exit 0, findings=0
python3 -B tools/gates/lexicon-coverage-audit.py .scratch/k38/packet-E0-stamp.yml  # exit 1, 1 D-stage-mismatch
python3 -B tools/gates/argot-derivation-gate.py .scratch/k38/packet-E0-both.yml    # exit 0
python3 -B tools/gates/register-law-gate.py     .scratch/k38/packet-E0-both.yml    # exit 0
python3 -B tools/gates/lexicon-coverage-audit.py .scratch/k38/packet-E0-both.yml   # exit 0, 0 findings

# §6 — the baselines the RL-8 edit would move
python3 -B tools/check-gate-battery.py                                       # exit 0, coverage 10/10
python3 -c "<read tools/gates/expected/register-law-gate/r30-post/expected.json>"  # gate_sha256 15f8b232…
ls tools/gates/expected/                                                     # no argot baseline

# §8 — the untouched tree
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                # exit 0, packet 45f57132…
```

**Source lines cited:** `reports/round-17/d4/design-brief.md:301-310`;
`reports/round-19/integration/d4-lessons-entry.md:85-91`;
`reports/round-25/argot/forecast.md:37`; `reports/round-25/argot/delta.md:41,148,198,255,294`;
`reports/round-26/register/rules.md:106-126,166`; `reports/round-26/register/review.md:183-187,205-215`;
`reports/round-26/register/execution-3.md:74`; `reports/round-26/argot/D24-forecast-closure.md:87,151`;
`reports/round-27/law/rules.md:29,173-192,226`; `reports/round-27/law/impl-8.md:68` and §2.2;
`reports/round-27/argot/D20-gap-closure-record.md:168`;
`reports/round-28/law/design.md:183`; `reports/round-36/depth/D06-gap-fill.md` §2.1;
`reports/round-36/validation.json` claims.D; `reports/round-37/op/O01-queue-draft.md:119,153`;
`reports/round-34/handoff/declared-in-r7/expected.json` (the `inputs` map);
`examples/culture-d4/packet.d4.yml:40-41,124-138,277-281,1018-1175,1274-1304,1329-1431,2854,2863`;
`examples/culture-d4/components/13-register-law.yml:45-49,57`;
`examples/culture-d4/components/04-lexicon.yml:253-260`;
`examples/culture-d4/typed-labels.d4.yml:29-47`;
`tools/gates/argot-derivation-gate.py:662,779-876,835,917-920`;
`tools/gates/typed-pipeline-gate.py:84,524-541,1471`;
`tools/gates/register-law-gate.py:121-122,204-211,231-243,252,337-357,424-432,561-585,635-638`;
`tools/gates/lexicon-coverage-audit.py:605,846-867`;
`tools/d2-typed-labels.py:410,556,605,2471,2560,2789,2837,2855,2879-2895,2918,3115,3497`;
`tools/assemble-d4-typed.py:270,377`;
`tools/exercise-handoff-e2e.py:153,1939-1964,1445,2165-2185,2247-2251`;
`tools/check-gate-battery.py:117-132,528-543`;
`tools/gates/expected/register-law-gate/r30-post/expected.json`;
`reports/round-38/{claims.json,targets.json,telemetry/availability-attempt-1.json}`.
