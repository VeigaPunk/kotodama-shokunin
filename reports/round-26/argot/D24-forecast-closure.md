# R26-D24 — review 4 of 4: the round-17 forecast, formally closed or its delta named

- **Seat:** R26-D24 (reviewer 4 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a`. Measurement stamp **2026-10-18T18:07:26Z**
  (`date -u +%FT%TZ`).
- **Review target:** the round-17 argot-derivation forecast (Δ3, F-1..F-8) and
  its surrounding material (A-1..A-11), against the delivered tree and the
  checking leg `tools/gates/argot-derivation-gate.py` sha256 `5b5abe78…`.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r26-d21/`. No tool, gate, packet, component, pin file, or filed
  rounds 8–25 byte touched; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 4 of 4: *the round-17 forecast formally closed (delta
zero or named)*. This file states the formal closure condition, tests it against
the delivered bytes, and — because the condition does **not** hold at this
seat's sample — names every residual delta element with a measured command. It
also states what would be a **false closure**, so the round cannot close on
wording.

**Verdict in one line.** The formal closure condition is **delta zero**: every
forecast element F-1..F-8 and A-1..A-11 delivered in the packet. At this seat's
stamp the delta is **not zero**: the *checking leg* is delivered (F-7's id is
emitted by a live code path), but the *relation* is not — the delivered packet
carries **no** `derived_from`/`derivation` pair, no `registers:`/`doublets`, and
the leg's own coverage line reads `derived_pairs=0`. So the correct closure is
**"delta named"**, and the named remainder is exactly Δ3's domain: the register
stratum has not landed. A closure that reads "delivered" on the strength of the
leg's existence alone is a **false closure** (§5).

## 1. The formal condition, and its two halves

The claim's `after_required` (`reports/round-26/claims.json:14`) says the stratum
"lands in D4 end-to-end" and "the round-17 forecast is marked delivered with the
delta closed". Those are two statements, and they are not the same test:

| test | condition | verdict at 18:07Z |
|---|---|---|
| **stratum lands** | the packet declares register-scoped forms with machine-readable derivation rules, the packet regenerates, the labels classify them, the leg replays them, the typed gate passes with the hold set updated | **NOT MET** (§2) |
| **forecast closed, delta zero** | every F-1..F-8 and A-1..A-11 element is delivered in the packet | **NOT MET** (§3) |
| **forecast closed, delta named** | every undelivered element is named with evidence, and no element is silently dropped | **MET by `reports/round-25/argot/delta.md` and re-measured here** |

So the honest disposition is the third row, and the round-26 D artifact must not
claim the second.

## 2. The stratum's state at this stamp (measured, not inferred)

```
$ export TMPDIR=$PWD/.scratch
$ grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/ | wc -l
0
$ grep -rn "derived_from" examples/
examples/handoff-packet.sample.yml:31:#   records requires a new packet_version with a supersedes/derived_from
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | head -1
coverage: examples/culture-d4/packet.d4.yml records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
```

The only `derived_from` under `examples/` is a **comment** in the handoff sample
about packet revisions, unrelated to the argot. `derived_pairs=0` is the leg's
own statement that no register derivation exists to replay. The D-seat scribe's
capability-row draft records the same at its own stamp
(`reports/round-26/scribe/capability-row.md` §0: four of six `after_required`
legs "measured unmet"), and the independent spot-check auditor agrees
(`python3 reports/round-26/audit/x60-register-derivation-spotcheck.py` →
`counters: … derived_pairs=0 … failures: 0`, exit 0).

**Timing note.** The 28 D workers were live during this seat's window
(`.scratch/r26-d-reg/`, `-d13`, `-d17-d20`, `-d21`, stamped 18:02–18:08Z), and
this review's own poll for `D4L-REGISTER-UNRESOLVED` was still negative at
18:07:26Z. If the stratum lands after this file, the three tests in §1 must be
**re-run**, not assumed: §3's table is the instrument.

## 3. Element-by-element closure test (F-1..F-8), re-measured at 18:07:26Z

Counts are `grep -rl -- <token>` file counts over the three surfaces.

| # | forecast element (`design-brief.md`) | delivered? | measured evidence (2026-10-18T18:07:26Z) |
|---|---|---|---|
| F-1 | quote forms derived from a plain base by a declared operation (`:301-302`) | **NO** | `derived_from` → examples **1** (a comment), tools 3 (the gate), r17 2 |
| F-2 | `head2` for measure words (`:302-303`) | **NO** | `head2` → examples **0**, tools 3 (the gate + fixture), r17 4 |
| F-2b | `reverse` for the numeral series (`:303-304`) | **NO** | `reverse` → examples 5 (all `sorted(…, reverse=True)` / unrelated), r17 5 |
| F-3 | checked through `derived_from` + `derivation` fields (`:303`) | **NO** | the packet's `contract.record_fields.lexicon` carries neither; `derivation:` hits in examples are `morphology.derivation_rules`/`derivation_note` only |
| F-4 | a relation between **two records of the same packet** (`:304`) | **NO** | no code path resolves a base to a record; `D21` §1 measures that a dangling base reads clean |
| F-5 | every derived quote form's check passes, zero fails (`:305-306`) | **VACUOUS** | trivially true: `derived_pairs=0` means no fail can exist. Not a delivery |
| F-6 | coverage block reports `derived_forms` / `derived_ok` (`:306-307`) | **NO** | `derived_forms` → 0 files anywhere; `derived_ok` → 0; the live coverage block (`typed-labels.d4.yml:29-37`) carries `labels_by_kind`, `findings_total`, `conflicts` — no derivation counts |
| F-7 | control: form ≠ `apply(op, base)` → FAIL `D4L-ARGOT-DERIV` (`:308-310`) | **PARTIAL** | the id is now **emitted by a live code path** (`tools/gates/argot-derivation-gate.py`, 5 tool files reference it), which round 25 did not have; but the **delivered packet produces zero** (`… packet.d4.yml | grep -c D4L-ARGOT-DERIV` → **0**), which is correct for a control-only id — the element is "the control exists", and it does |
| F-8 | required-controls row C-02 (`:456`) | **PARTIAL** | the gate's selftest asserts the exact id set and the design's own `saalum`/`saalu` trap (`fixture-names-the-violating-form`); C-02's *sibling* C-01 (private segment → FAIL) has **no** implementation (`D21` §4) |

**Delta set at this stamp:** F-1, F-2, F-2b, F-3, F-4, F-6 (undelivered), F-5
(vacuous), F-7/F-8 (partially delivered: the id and its control exist; the
domain does not).

## 4. Surrounding elements (A-1..A-11), re-measured

| # | element | delivered? | evidence |
|---|---|---|---|
| A-1 | six argot loans `AL-01..AL-06` in the quote slot | **NO** | the six loans delivered are `L-49..L-54` (`trade`/`craft` layers), not the design's `AL-` ids |
| A-2 | the eleven worked derivations (`D4-X02`, `D4-X13..X22`) | **NO** as packet data / **YES** as algorithms | the gate's `DESIGN_TABLE` re-derives all 11 (`design-table-rederived-11` ok); the design's ids occur in 0 files under `examples/`/`tools/` |
| A-3 | eight quote names by `reverse` | **NO** | each of `inak, usam, urin, akas, akim, aruk, isun, asum` → 0 occurrences |
| A-4 | Δ1 register-scoped slots `<id>#plain`/`<id>#quote`, hold `D4L-REGISTER-UNRESOLVED` | **NO** | `#quote` → 0 files under examples/tools; `D4L-REGISTER-UNRESOLVED` → 0 under examples/tools |
| A-5 | Δ2 slot cardinality, `doublet_of` | **NO** | `doublet_of` → 0 files under examples/tools |
| A-6 | Δ5 register-era clock, `D4L-ERA` | **NO** | `D4L-ERA` → 0 under examples/tools |
| A-7 | the design's §4 packet shape (`registers, doublets, measures, oaths`) | **NO** | the packet has none of the four keys |
| A-8 | the design's §4 component plan (`06-register-contract`) | **NO** | the landed component set is the D2/D3 family; no register-contract component |
| A-9 | the design receipt "11/11 derivations reproduce" | **REPRODUCIBLE NOW (as algorithms)** | the gate's selftest re-derives all 11 from the design's own table; the receipt's *scratch* checker is superseded, but the claim it made is independently reproduced |
| A-10 | the design's spine COUNT × QUOTE | **NO — superseded by path A** | the landed tree is the furnace-league (FIRE × MARK); `reports/round-25/argot/delta.md` §1.2 records this and it is not re-litigated here |
| A-11 | hold-set lettering `D4L-FORM-UNRESOLVED` at `GAR-01..06` | **PARTIAL, lettering drifted** | the declaration names `D4L-FORM-UNRESOLVED`; the engine emits `D2L-FORM-UNRESOLVED`; `examples/culture-d4/expected-holds.json` carries 12 `D2L-FORM-UNRESOLVED` holds and **0** `D4L-` rows (`grep -c "D4L-" examples/culture-d4/expected-holds.json` → **0**) |

## 5. What would be a false closure

The round's temptation is to close the forecast on the strength of the leg's
existence. Three readings are false, and each has a measured counter:

1. **"The leg landed, so Δ3 is delivered."** False: the leg is the *checker*
   (F-7/F-8's half). F-1..F-4 are the *relation*, and the relation is not in the
   packet — `derived_pairs=0`. Counter:
   `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`.
2. **"`register_scoped=6` is the register domain, so it is non-empty."** False:
   those six are the **loan-layer** records `L-49..L-54`, counted via their
   layer's `register` (`04-lexicon.yml:103,117`) — the label-typing table's
   *borrowed-strata* row, not the forecast's quote register. `D22` §2 measures
   this and the independent auditor prints `register_scoped=6
   register_scoped_declared=18` (the 18 being prose rows it excludes).
3. **"F-5 is satisfied: zero fails."** False: F-5 is *vacuous* at
   `derived_pairs=0` — a set with no members has no failures. A vacuous pass is
   not a delivery (`reports/round-25/argot/delta.md` §1's F-5 row says the same).

## 6. What closure would require (the instrument for a re-run)

**Timing note (added at 18:08Z).** The D-design seats filed
`reports/round-26/register/{design,forms,rules}.md` during this seat's window
(`design.md` names the register `stamp`; `rules.md` fixes its derivation-rule
registry). Those are **design documents**, not the stratum: `grep -rl
"D4L-REGISTER-UNRESOLVED" examples/ tools/` → **0** at 18:08:29Z, and no
component or packet under `examples/` carries a `derived_from`/`derivation` pair.
So the design half is now on disk and the delivered half is not. The table below
is what decides whether the delivered half landed; re-run it, do not assume.

If the stratum lands, the closure test is mechanical. Every row below must be
re-run and the numbers must move:

| test | command | required |
|---|---|---|
| relation declared | `grep -c "derived_from" examples/culture-d4/packet.d4.yml` | ≥1 |
| relation in the contract | `grep -A2 "record_fields" … \| grep derived_from` | present |
| non-empty domain | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `derived_pairs>=1`, `violations=0`, exit 0 |
| base resolves to a record | `D21` §1's fixture | a dangling base must **not** read clean |
| no self-derivation | `D21` §2's fixture | a self-pair must **not** read clean |
| coverage block | `grep -c "derived_forms\|derived_ok" examples/culture-d4/typed-labels.d4.yml` | ≥1 each |
| hold set named | `grep -c "D4L-REGISTER-UNRESOLVED" examples/culture-d4/expected-holds.json` | ≥1 if any register slot is owed |
| determinism | `python3 tools/assemble-culture-d4.py --check` | exit 0 (already met) |

## 7. Controls carried by this fragment

- The closure test is a **table of commands**, so a later reader re-runs it
  rather than trusting this file.
- Each "NOT MET" row carries a token count with its surface, so a false "MET"
  claim is refutable by the same command.
- The **false-closure** section (§5) is the control on this review itself: it
  names the three readings that would let the round close without the domain,
  and the counter for each.

## 8. Counting commands for this file

```
export TMPDIR=$PWD/.scratch
date -u +%FT%TZ
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | head -1
grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/ | wc -l
grep -rn "derived_from" examples/
grep -c "derived_forms\|derived_ok" examples/culture-d4/typed-labels.d4.yml
grep -c "D4L-" examples/culture-d4/expected-holds.json
python3 reports/round-26/audit/x60-register-derivation-spotcheck.py | tail -3
```
