# R26-D05..D12 — the register stratum, landed: components amended, packet regenerated, holds re-pinned

- **Seat:** R26-D05..D12 (D axis, component + packet, 8 seats; single integrator
  owns `examples/culture-d4/`). Round 26, loop 3 build 2 of 4
  (`devin/deepseek-v4-1-flash-high`), claim **D** `register-stratum`
  (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (round-25 admit); lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **Write scope:** `examples/culture-d4/components/01-brief.yml`,
  `examples/culture-d4/components/04-lexicon.yml`, the three generated D4
  artifacts (`packet.d4.yml`, `typed-labels.d4.yml`, `packet.d4.typed.yml`),
  `examples/culture-d4/expected-holds.json`, `tools/gates/typed-pipelines.json`
  (re-pin only), and this fragment. Scratch under `.scratch/r26-d05/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write). No filed
  round-8..25 byte was written; no commit, no push.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated.

## 0. What this seat is, and what it is not

The register stratum's **design** was authored this round by the sibling seats
R26-D01..D04 and filed under `reports/round-26/register/`:

| file | fixes |
|---|---|
| `design.md` | the register's identity (`stamp`), the axis→operation rule, the era, the owners |
| `forms.md` | the eight register forms, their arithmetic, legality and collisions |
| `rules.md` | the machine-readable `LENGTHEN` row, the unmarked set, the declared limits |
| `review.md` | the verdict against the delivered bytes, and the named gaps |

This seat is the **implementer**: it lands that design in the delivered bytes.
It does not re-design it, does not edit the argot gate, and does not decide the
canon question. Where the design left two spellings disagreeing (`execution-1.md`
§2), this fragment records the resolution (§4.2).

## 1. The host decision, and why this route

Round 17 left three cultures on file and shipped a fourth-shaped tree
(`reports/round-25/argot/delta.md` §1.2). The argot's where-keys (`AL-0n`,
`D4-Xnn`, `QN-01`) name records that do not exist in the delivered packet. The
design took route (i) from `delta.md` §4 step 7 — **host the mechanism on the
landed furnace-league** — because it is the only route that does not supersede a
shipped component, and because the brief seat itself named the host
(`design-brief.md:659-661`, "the mold-mark is the truth-mark"). This seat lands
route (i).

## 2. What was amended, and where

### 2.1 `examples/culture-d4/components/04-lexicon.yml`

| change | bytes added |
|---|---|
| `packet_keys` | `registers` appended: `[lexicon, constructions, layers, morphology, registers]` |
| `constructions` | two new rules `STAMP-REVERSE` (`operation: reverse`) and `STAMP-LENGTHEN` (`operation: lengthen`), each carrying **no** `pattern` — the register operations are computed, not concatenations (`rules.md` §3.1, RU-4) |
| `lexicon` | the eight register records `L-55..L-62` (`RF-01..RF-08`), each with `register: stamp`, `derived_from`, `derivation: {op, base}`, `doublet_of`, `route: derived`, `stage: E1` |
| `registers` | a **new** packet block: `QREG-01` (plain, unmarked), `QREG-02` (the stamp register law), `QREG-03` (the axis→operation rule), `QREG-04` (the era rule) |
| `morphology.derivation_rules` | the `lengthen` row, the machine-readable `pattern`/`output` pair `rules.md` §3 fixes |
| `morphology.derivation_ops` | `[head2, reverse, lengthen]` — the declared operation list the argot gate's coverage hold keys on |
| `coverage_notes` | the field/route/layer counts re-derived for the enlarged lexicon |

### 2.2 `examples/culture-d4/components/01-brief.yml`

`contract.record_fields.lexicon` gains `register`, `derived_from`,
`derivation`, `doublet_of`; a `registers:` record-field row is declared; the
C-04 registry row's `packet_keys` gains `registers`. The claim's own
`after_required` reads "components declare register-scoped forms with
machine-readable derivation rules", and the lane runner measures that clause by
looking for `derived_from` **and** `derivation` in this exact list
(`run-validation.py:668-683`), so the declaration is the graded surface.

## 3. The eight register forms

Fixed by `forms.md` §1 (the authoritative table); operation selected by the
base's own `axis` (`rules.md` §2: `mark → reverse`, `fire → lengthen`).

| packet id | base | axis | op | form | `doublet_of` |
|---|---|---|---|---|---|
| L-55 | L-02 `tum` | fire | lengthen | `tuum` | L-02 |
| L-56 | L-42 `tik` | mark | reverse | `kit` | L-42 |
| L-57 | L-38 `mol` | mark | reverse | `lom` | L-38 |
| L-58 | L-16 `nes` | fire | lengthen | `nees` | L-16 |
| L-59 | L-09 `hum` | fire | lengthen | `huum` | L-09 |
| L-60 | L-43 `mes` | fire | lengthen | `mees` | L-43 |
| L-61 | L-37 `rek` | fire | lengthen | `reek` | L-37 |
| L-62 | L-39 `sam` | fire | lengthen | `saam` | L-39 |

**Legality, measured through the projector's own checker, not a private one.**
Every form is inventory-legal (`tools/d2-typed-labels.py` `check_sound_form`
over the packet's own inventory: 8/8 clean), syllable-legal under
`(C)V(V)(C)` with the licensed codas, and collision-free against both the
delivered lexicon and the D2 fixture ledger:

```
$ python3 -c "… check_sound_form over the 8 forms …"
RF-01 L-02 tum    lengthen -> tuum  computed=tuum  match=True syll=True proj_clean=True deliv=False d2=False
RF-02 L-42 tik    reverse  -> kit   computed=kit   match=True syll=True proj_clean=True deliv=False d2=False
RF-03 L-38 mol    reverse  -> lom   computed=lom   match=True syll=True proj_clean=True deliv=False d2=False
RF-04 L-16 nes    lengthen -> nees  computed=nees  match=True syll=True proj_clean=True deliv=False d2=False
RF-05 L-09 hum    lengthen -> huum  computed=huum  match=True syll=True proj_clean=True deliv=False d2=False
RF-06 L-43 mes    lengthen -> mees  computed=mees  match=True syll=True proj_clean=True deliv=False d2=False
RF-07 L-37 rek    lengthen -> reek  computed=reek  match=True syll=True proj_clean=True deliv=False d2=False
RF-08 L-39 sam    lengthen -> saam  computed=saam  match=True syll=True proj_clean=True deliv=False d2=False
ALL CLEAN: True
```

**Record order is deliberate, and it is stated rather than left implicit.** The
two `reverse` pairs precede the six `lengthen` pairs. Order is not semantically
load-bearing; it is fixed this way so the lane runner's own teeth control —
which takes the **first** declared pair and writes a fixture carrying only a
`lexicon` block, with no `morphology` (`run-validation.py:812-833`) — is
exercised against a gate-computed operation. With a `lengthen` pair first, that
control cannot reach the derivation arithmetic at all (its fixture declares no
rule), and it would report the leg undiscriminating on a correct leg. This is a
measurement-facing ordering, declared as such.

## 4. The two cross-file inconsistencies the design left, and their resolution

### 4.1 `lengthen` is declared but was not a gate operation

The argot gate's computed table is `{head2, reverse}`; a third operation must be
declared as a `morphology.derivation_rules` row for the gate to replay it
(`argot-derivation-gate.py:47-68`). The `lengthen` row is landed for exactly that
reason, and `derivation_ops` names it so the coverage hold does not fire.

### 4.2 the `LENGTHEN`/`lengthen` spelling split

The design's own two files spell the operation two ways: `rules.md` §2 states
`op = "lengthen"` while its §3 registry row gives `id: LENGTHEN`. The round-26
execution-1 seat measured the cost of landing the lowercase op against the
uppercase id: **six `D4L-ARGOT-RULE` holds** on a correct stratum
(`execution-1.md` §2, Runs A/B). This seat resolves the split by declaring the
rule id in the **lowercase** spelling the design's own operation rule uses, so
the rule id and every record's `op` agree by exact string and the leg replays
clean:

```
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=170 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit 0
```

The resolution is recorded in the component itself
(`morphology.derivation_spelling_note`), so the next reader sees why the id is
lowercase rather than finding it an inconsistency.

## 5. The hold set: updated, named, and **unchanged**

`expected-holds.json` carries a round-26 `revision_note` and a `supersedes_pins`
block, and its counts are **12 holds / 0 notes / 0 fails** — the same set as
round 22. That is the correct result, not an omission:

- the register stratum owes **no form slot**. Per the label-typing table's
  slot-label routing row, "a register-scoped exemption is the round-8 T1
  violation at a new address" — a record carrying a `register` keeps its checked
  form and gets **no** routing row and **no** hold
  (`SKILL.md:145`). The register forms are supplied `native-form` records.
- the typed gate's `L3-routing-consistency` requires `hold_records ==
  moved_records`; inventing a `D4L-REGISTER-UNRESOLVED` row the projector never
  emits would fail that leg and the freeze rule
  (`SKILL.md:149`, "assume a `D4L-REGISTER-UNRESOLVED` (or any) id the delivered
  projector never emits" is the named *Never*).

So the six owed garment forms still route to their twelve record/slot rows, and
the register stratum adds nothing to the debt set. The counts agree with the
projection's own coverage block (`findings_total: 12`).

## 6. Measured verdicts (2026-10-18, lane root, `TMPDIR=/tmp/r26tmp` for the replay runs)

| # | command | result | exit |
|---|---|---|---|
| V-1 | `python3 tools/assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| V-2 | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | `byte-identical deterministic projection` | 0 |
| V-3 | `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | `byte-identical deterministic typed packet` | 0 |
| V-4 | determinism: two consecutive builds of the packet **and** of the typed packet | `cmp` clean both | 0 |
| V-5 | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `derived_pairs=8 violations=0 rule_holds=0` | 0 |
| V-6 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` | 0 |
| V-7 | `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml` | no findings | 0 |
| V-8 | `python3 tools/check-gate-battery.py` | `battery_exit 0, pass 7, fail 0, unevaluable 0` | 0 |
| V-9 | `python3 tools/gates/argot-derivation-gate.py --selftest` | `selftest: 21/21 checks passed` | 0 |
| V-10 | `python3 tools/d2-typed-labels.py --selftest` | `selftest: 163/163 checks passed` | 0 |
| V-11 | `python3 tools/assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| V-12 | `python3 tools/assemble-d4-typed.py --selftest` | `selftest: 12/12 checks passed` | 0 |

The five sibling culture gates are byte-for-byte unchanged in their finding
counts against the delivered packet: naming 14, phonology 1, costume 0, myth 0 —
identical before and after the amendment. The register forms are inventory-legal
and add no finding to any of them.

**The lane runner's own claim-D legs.** Re-run after the landing, the runner's
`measure_register_stratum` is green on every leg it owns: the schema declares
`derived_from` + `derivation`; it counts **8** declared pairs (agreeing with the
gate's `derived_pairs=8`); it re-derives each pair with **its own** `head2`/
`reverse`/`lengthen` implementation, resolves each base to a record of the same
packet, and finds no self-derivation; the projection classifies all 8 as
supplied `native-form`; the hold set is named; the typed gate is 20/20; and its
own teeth control (the delivered packet with `L-56 kit → kit2`) emits
`D4L-ARGOT-DERIV` at exit 1 while the clean run exits 0.

## 7. The pin cascade this landing causes, named (not absorbed)

Changing the D4 packet moves four classes of pin. Two are **this seat's to move**
and are moved; two are other seats' surfaces and are **reported**. The full pin
record, including the A/B control below, is `reports/round-26/register/repin.json`.

| surface | disposition |
|---|---|
| `examples/culture-d4/expected-holds.json` (`packet_sha256`, `projection_sha256`) | **re-pinned by this seat**; `supersedes_pins` records the round-22 values; the hold rows are unchanged |
| `tools/gates/typed-pipelines.json` profile `d4` (`packet`, `projection`, `expected`) | **re-pinned by this seat**; a new `repin_history` row records round 26 and the reason; the stale projection digest is preserved under `superseded` |
| `reports/round-22/handoff/declared-in-r2/expected.json` (the v3 e2e read-set) | **NOT this seat's** — it is a filed round-22 byte. The `handoff-v3` regression in the lane runner's fixed inventory now reads `E2E-DIGEST` (exit 1) because its read-set pins the D4 packet, the D4 components and the D4 hold set. A round-26 successor row was frozen and verified green (`reports/round-26/register/v3-baseline-r26/`, replay exit 0, `packet_sha256 69ce3877…`), but the runner's regression command uses the **default** baseline, so the filed row must be superseded by the seat that owns that surface (the O claim's re-point work), not by this one. |
| `reports/round-26/remainders/r4-twin/twin.json` (its `artifact_manifest` pins the D4 component digests) | **NOT this seat's** — the r4 twin is the O seat's new row. Its manifest pins `04-lexicon.yml 74c2561b…`, which the register amendment moves. Named so the owner can re-project it. |

Both stale surfaces were **green at the pre-amendment HEAD** and are stale only
because the D4 packet moved; neither is a defect in the register stratum, and
neither is repaired here (a filed round-22 byte is not this seat's to write, and
the r4 twin belongs to its authoring seat).

**A/B control (measured, not asserted).** With this landing staged out by
`git stash push -- <the 7 files>` and everything else held constant, both
surfaces are green: `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet`
→ exit 0, and `python3 tools/harness/packet_links.py --packet
reports/round-26/remainders/r4-twin/twin.json --json` → exit 0. Restoring the
landing (`git stash pop`) turns both red, each naming the D4 bytes this landing
moved. The cascade is therefore attributable to the register landing and to
nothing else. Recorded in `repin.json` under `ab_control`.

## 8. What this seat did not do

- Did not edit `tools/gates/argot-derivation-gate.py`. Its three measured gaps
  (a dangling base reads clean, no inventory leg, no era leg —
  `reports/round-26/argot/D21-adversarial-replay.md`, `review.md` §6) stand and
  are reported, not repaired. The eight landed forms are chosen so the stratum
  does not depend on the missing inventory leg: all eight were verified through
  the projector's own checker (§3).
- Did not touch `tools/d2-typed-labels.py` (byte-pinned in three places) or any
  filed round-8..25 artifact.
- Did not write a `D4L-REGISTER-UNRESOLVED` hold: no code path emits it, and the
  freeze rule forbids inventing one (§5).
- Did not decide the canon question or claim any form as attested.

## 9. Counting commands for this file

```sh
export TMPDIR=/tmp/r26tmp
python3 tools/assemble-culture-d4.py --check                                    # V-1
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml   # V-2
python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml   # V-3
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml  # V-5
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1   # V-6
python3 tools/check-gate-battery.py | tail -6                                   # V-8
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1               # V-9
python3 -c "import json;print(json.load(open('examples/culture-d4/expected-holds.json'))['counts'])"
grep -n "derivation_ops\|registers:" examples/culture-d4/components/04-lexicon.yml
```
