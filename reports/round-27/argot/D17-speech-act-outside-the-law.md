# R27-D17 — adversarial review 1 of 4: a speech act outside the law, passing

- **Seat:** R27-D17 (reviewer 1 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (round-26 admit); lane HEAD at every measurement
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` (`git log --oneline -1`). Measurement
  stamp **2026-10-18T19:33:47Z** (`date -u +%FT%TZ`).
- **Review target:** the round-27 register **law** — the `register_law` block
  (`examples/culture-d4/components/13-register-law.yml`, `RGL-01..RGL-05`) and
  the `registers` block (`examples/culture-d4/components/04-lexicon.yml`,
  `QREG-01..QREG-04`) — against the delivered gates, and the independent law
  instrument `reports/round-27/audit/x59-register-law-negatives.py`.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r27-d17/`. `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command. **No component, packet, tool, gate, fixture, pin or
  filed rounds 8–26 byte was written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence. Findings are review evidence, never
  canon rulings.

**Assignment.** Reviewer 1 of 4, adversarial: *a speech act outside the law
passing?* The law the round-27 claim lands is a **speech-act law**: it says what
may be said in the `stamp` register, by whom, with what force, and with what
record consequence (`13-register-law.yml:23-24`). The adversarial question is
whether a **speech act that the law forbids** can pass every delivered gate
unnoticed. Four such acts are planted below, and the answer is **yes for all
four**: the law landed as **data no gate reads**.

**Verdict in one line.** The register law is **specified, hosted and owned** —
the round-26 `RD-5c`/`RL-6` gap (the law had no owning component) is **closed**
by a new component, wired deterministically, and it reaches the packet
field-for-field — but it has **no replay leg**: a planted violation of any of
its four acts produces **no new finding in any delivered gate**, and the one
independent instrument that does catch the era act (`L4-FAIL`) also reports the
same two holds on the **clean** packet, so it cannot distinguish the tampered
tree from the untampered one by exit code.

## 0. The law, as landed — and the artifact identity

Two blocks, two owners, both admitted by their own per-file `packet_keys`
(measured, runner-owned census below):

| block | owner component | rows | packet |
|---|---|---|---|
| `registers` (identity + operation/era rules) | `examples/culture-d4/components/04-lexicon.yml` | `QREG-01..04` | present |
| `register_law` (the speech-act law) | `examples/culture-d4/components/13-register-law.yml` | `RGL-01..05` | present |

```
$ sha256sum tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml \
            examples/culture-d4/components/13-register-law.yml
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc  examples/culture-d4/packet.d4.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
```

The runner's own component-ownership census agrees the packet's rows **are** the
declaring component's rows, field for field:

```
component_ownership.register_law = {component: 13-register-law.yml,
  component_ids == packet_ids == [RGL-01..RGL-05], rows_equal: true}
component_ownership.registers    = {component: 04-lexicon.yml,
  component_ids == packet_ids == [QREG-01..QREG-04], rows_equal: true}
```

The four acts the law states (`13-register-law.yml:29-33`, `kind` in
`{admissibility, exclusion, asymmetry, no-segment, era}`):

| id | act | holder | consequence |
|---|---|---|---|
| `RGL-01` | a charge / lot-naming / attested oath | a stamp-holder, or a speaker they attest | the form binds; the act is entered on the stamp-roll |
| `RGL-02` | **an oath** | **none — no binding oath** | a `stamp` oath is **void** |
| `RGL-03` | a guest broker's act | a guest broker under a stamp-name | binds, entered under the stamp-name, **may not keep the roll** |
| `RGL-05` | any in-register form | admitted by `RGL-01`/`RGL-03` | available_from **E1**; an E0 claim is a defect |

## 1. The four plants, and what every delivered gate does with them

Each plant is a **text transform of the delivered packet** (never a
re-serialization of the component), written under
`.scratch/r27-d17/`. The control is the **clean** packet through the same gate.

| plant | the act it violates | file |
|---|---|---|
| `T1-stamp-oath` | `RGL-02`: a `stamp` form declared as an **oath** (the law says void) | `T1-stamp-oath.yml` |
| `T2-stamp-out-of-slot` | `RGL-01`: a `stamp` form used in a **non**-stamp-act slot (a plain greeting) | `T2-stamp-out-of-slot.yml` |
| `T3-stamp-at-E0` | `RGL-05`: a delivered `stamp` form (`L-55`) **restaged to E0** | `T3-stamp-at-E0.yml` |
| `T4-guest-roll-erased` | `RGL-03`: the guest asymmetry **erased** (`RGL-03.consequence` → "may keep the furnace roll") | `T4-guest-roll-erased.yml` |
| `T5-oath-inverted` | `RGL-02` inverted: "an oath spoken in stamp is **BINDING**" | `T5-oath-inverted.yml` |
| `T6-holder-widened` | `RGL-01` widened: holder = "anyone at all" | `T6-holder-widened.yml` |

Measured against **every delivered gate** (lane root, `TMPDIR=$PWD/.scratch`):

```
$ for f in T1..T6; do for g in argot-derivation-gate.py typed-pipeline-gate.py \
      d2-typed-labels.py d4-assembly-check-gate.py; do …; done; done
```

| gate | `T1` | `T2` | `T3` | `T4` | `T5` | `T6` | **clean control** |
|---|---:|---:|---:|---:|---:|---:|---:|
| `argot-derivation-gate.py` | exit 0 | exit 0 | exit 0 | exit 0 | exit 0 | exit 0 | **exit 0** |
| `typed-pipeline-gate.py` | exit 2 | exit 2 | exit 2 | exit 2 | exit 2 | exit 2 | exit 0 |
| `d2-typed-labels.py` | exit 2 | exit 2 | exit 2 | exit 2 | exit 2 | exit 2 | exit 2 |
| `d4-assembly-check-gate.py` | exit 1 | exit 1 | exit 1 | exit 1 | exit 1 | exit 1 | exit 0 |

The `exit 2` rows are **input-class refusals** (the probe is a packet, not the
typed packet or the component those tools expect), and `d4-assembly-check-gate`
exits 1 because the mutated packet no longer matches the assembler's
deterministic output. **Neither is a law finding**: no gate emits an `RGL-*` or
`L4/L7` finding on any plant, and the argot gate — the one the claim's register
leg names — reads **exit 0, `violations=0` on all six**, identical to the clean
packet.

The control direction is what makes this a finding rather than an absence of
test: the argot gate **does** catch the *arithmetic* class on the same tree
(`violations=1` for a mis-derived form, see `D18`), so the leg is discriminating
in its own domain and simply has **no law domain at all**.

## 2. The one instrument that reads the law, and its own exit-code limit

`reports/round-27/audit/x59-register-law-negatives.py` (R27-X59) is the
independent law auditor, built on `ruby -ryaml` rather than the lane's loader.
Its controls are honest — `--controls` reads **8/8 caught**:

```
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py --controls
control-1-op-contradicts-axis      ok  law=L3  findings=2
control-2-early-era                ok  law=L4  findings=2
control-3-form-mismatch            ok  law=L3  findings=2
control-4-stray-construction       ok  law=L5  findings=2
control-5-oath-in-register         ok  law=L7  findings=2
control-6-dangling-doublet         ok  law=L8  findings=2
control-6b-law-row-without-id      ok  law=L9  findings=2
control-7-clean-stays-clean        ok  law=no-FAIL  findings=2
controls: 8/8 caught
```

But the live run carries **two holds on the clean packet**:

```
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py
FINDING L6b-HOLD: a tampered law value is not a finding in any delivered gate …
FINDING L9-HOLD: the `register_law` block is landed and every row carries an `id`,
  but the assembler declares it in neither `PACKET_KEYS` nor `RECORD_FIELDS` …
counters: … law_rows=5 register_law_block=5 speech_act_rows=5 …
failures: 2
```

Measured across the six plants and the clean control, the instrument's exit code
is **1 in every case**:

| tree | exit | findings beyond the clean set |
|---|---:|---|
| **clean packet** | **1** | `L6b-HOLD`, `L9-HOLD` (the baseline set) |
| `T1-stamp-oath` | 1 | — (same set) |
| `T2-stamp-out-of-slot` | 1 | — (same set) |
| `T3-stamp-at-E0` | 1 | **`L4-FAIL`** (the era act **is** caught) |
| `T4-guest-roll-erased` | 1 | — (same set) |
| `T5-oath-inverted` | 1 | — (same set) |
| `T6-holder-widened` | 1 | — (same set) |

**This is the honest state of the law's teeth, and `x59` says so itself.** Only
`RGL-05`'s era act (`T3`) moves the finding set — and even that does not move the
exit code, because the clean tree already exits 1 on its two holds. A consumer
that grades the law by `x59`'s exit code grades **nothing**: `1` is both the
clean and the tampered verdict. The instrument's own `L6b` message names the
cause exactly: *"the law is a declaration with no teeth — the enforcement leg is
unowned."*

## 3. The assembler does not validate the new block (measured A/B)

`x59`'s `L9-HOLD` is not a guess. Measured in two isolated copies under
`.scratch/r27-d17/` (`ab2`, `ab3`), the same edit applied to the two blocks:

```
# A — strip the `id` from a `register_law` row (13-register-law.yml)
$ python3 -B tools/assemble-culture-d4.py
… exit 0   (the packet regenerates; the row lands with no `id`)

# B — strip the `id` from a `lexicon` row (04-lexicon.yml, L-02)
$ python3 -B tools/assemble-culture-d4.py
assembly error: lexicon[1]: missing field(s) ['id'] needed by the gate-facing packet
exit 2
```

The cause is structural and reproducible:

```
$ python3 -c "import importlib.util; … assemble-culture-d4 …"
register_law in PACKET_KEYS:   False
register_law in RECORD_FIELDS: False
registers    in PACKET_KEYS:   True   RECORD_FIELDS['registers'] = ('id',)
```

`register_law` reaches the packet **only** through the component's own per-file
`packet_keys: [register_law]` declaration (`13-register-law.yml:18`), which the
assembler honours (`assemble-culture-d4.py:258-264`), but the assembler's record
validator (`:315-325`) iterates `RECORD_FIELDS` and so has **no field list** for
the block. A `register_law` row can therefore lose its `id` and assemble clean.
The `registers` block does not have this hole because it **is** in
`RECORD_FIELDS` — so the gap is specific to the new block, not to the assembler's
design.

## 4. What is settled — and the round-26 gap that is genuinely closed

This review is adversarial, so the closures are stated with their commands too.

| # | what the round-26 review named | state now | evidence |
|---|---|---|---|
| `RD-5c` / `RL-6` | "the delivered tree has **no component that owns a register law** … someone must own it" (`reports/round-26/register/review.md` §6.3) | **CLOSED** | a new component `13-register-law.yml` declares `packet_keys: [register_law]` and carries `RGL-01..05`; the runner's `law_blocks.declaring_components` names it, and `component_ownership.register_law.rows_equal = true` |
| `RD-4` / `RL-3` | the gate's `syllabify` disagrees with the design's stated algorithm on 15 of 62 forms | **PARTLY closed — see `D18`** | the cluster class is fixed (gate `b5406bcd…`, `is_legal_syllable` at `:217`); the diphthong class is not |
| the law's *record* surface | — | **CLOSED** | `contract.record_fields.register_law` is declared (`01-brief.yml:183`), and every landed row carries all twelve declared fields (no declared-but-absent field) |
| the law's *enforcement* | — | **OPEN, and named** | §1–§3 above: zero delivered-gate teeth, and the assembler does not validate the block |

The law's **content** is also not merely restated prose: each row carries
`act` / `holder` / `force` / `consequence` / `axis` / `evidence` / `follows` /
`cite` / `design_row`, so the five round-26 `RGL-01..05` design statements are
landed as machine-readable records rather than quoted. The runner's clause
coverage agrees: `{admissibility: true, agent: true, consequence: true}`,
`rule_ids = [QREG-01..04, RGL-01..05]`, `rows_with_universal_fields = 9 of 9`.

## 5. Named limits of this review

| id | limit | statement |
|---|---|---|
| **D17-L1** | **the law is unenforced by construction, and the design says so** | `13-register-law.yml`'s own `law_binding.enforcement` reads: *"no gate executes these rows … The rows are a declared law with named non-execution, not a claim of enforcement."* This review **confirms** that statement by measurement; it does not contest it. The gap is therefore **declared, not laundered** — which is the standard this lane holds. |
| **D17-L2** | the plants are **mutations of a NON-CANON packet**, not attested data | every form in `T1..T6` is a probe. No claim about any language, institution or register is made or implied. |
| **D17-L3** | `exit 2` from two gates is an **input-class refusal**, not a finding | those rows are reported so a reader does not mistake a refusal for a catch; the finding is the **absence of a law finding**, not the exit code. |
| **D17-L4** | the instrument `x59` is **attributed, not re-implemented** here | this seat re-ran it and read its output; it did not re-derive the law from `ruby -ryaml`. `D20` records the independent-instrument question separately. |

## 6. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sha256sum tools/gates/argot-derivation-gate.py examples/culture-d4/components/13-register-law.yml
python3 -B reports/round-27/audit/x59-register-law-negatives.py --controls   # 8/8 caught
python3 -B reports/round-27/audit/x59-register-law-negatives.py              # exit 1, L6b+L9 holds
for f in T1-stamp-oath T2-stamp-out-of-slot T3-stamp-at-E0 T4-guest-roll-erased \
         T5-oath-inverted T6-holder-widened; do
  python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d17/$f.yml   # exit 0, violations=0
  python3 -B reports/round-27/audit/x59-register-law-negatives.py --packet .scratch/r27-d17/$f.yml
done
grep -n "enforcement" -A 3 examples/culture-d4/components/13-register-law.yml
```
