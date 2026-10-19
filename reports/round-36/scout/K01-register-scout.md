# K01 — register-domain scout

- Seat: K01 | scout | claim D | date 2026-10-19 | baseline ce103bf
- Round 36, loop 1 position 4, single 32-seat batch (declared devin fallback after hyper 402;
  `reports/round-36/telemetry/availability-attempt-1.json`).
- Write scope: this file only. No tool, gate, packet, component, pin, or filed 8–35 byte written;
  no commit, no push. Measurement stamp **2026-10-19T09:29:40Z** (`date -u +%FT%TZ`).
- Canon: NON-CANON engineering evidence. A digest is integrity, never truth, never clearance.

**Verdict in one line.** The r25 record "the register-form domain in the delivered D4 packet is
EMPTY" (`SCORECARD.md:312`) was true at the r25 worktree (`f74fc940…`) and is **false at the
round-36 baseline `ce103bf`**: the domain now carries 8 replaying register forms and a 5-row law.
Claim D's stated `before` ("Register-form domain empty") therefore no longer describes the tree, and
the claim as worded is **already satisfied in substance**. What is genuinely owed is a short,
nameable residue (F-6 counters, `head2`, the era leg), not a build. Claim D as drafted would
re-do work r26/r27 landed — reported to the planner rather than absorbed.

## 1. The r25 record, and why it is stale

`SCORECARD.md:312` (round-25 depth row) reads: "the register-form domain in the delivered D4 packet
is EMPTY (the register class was design-forecast, never built into components), so the leg stands
ready over an empty domain". Its own instrument, `reports/round-25/argot/current-state.md:5`, states
the worktree it measured: `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`. That is **before** r26 and r27.

The lineage that closed it, from the scorecard's own rows:

| round | landed | source |
|---|---|---|
| 26 | the `stamp` register lands: 8 forms (tuum/kit/lom/nees/huum/mees/reek/saam), axis→op rule (mark→reverse, fire→lengthen), era E1 | `SCORECARD.md:329` |
| 27 | component 13 + the `register_law` block, RGL-01..05 | `SCORECARD.md:345` |
| 28 | the law replay leg `tools/gates/register-law-gate.py`; RL-4 fixed (8 records reach the packet) | `SCORECARD.md:363` |
| 30 | QREG-05..08 land, resolving the 4 `D4L-LAW-DANGLING` findings | `SCORECARD.md:400` |

r26 itself said so at the time: `reports/round-26/argot/D24-forecast-closure.md:88-92` names
`register_scoped=6` as the **loan layer**, not the register, and §5 warns that reading it as the
register domain is a false closure. The r26 register stratum landed *after* that review's stamp, and
the review's own §2 timing note anticipates exactly this.

## 2. The domain, measured at `ce103bf` (not read from any summary)

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
→ coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 \
            claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
→ dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4…
→ exit 0
```

`register_scoped=14` decomposes exactly: **8** `derived_pairs` (the stamp forms) + **6**
`borrow_pairs` (the loan layer `L-49..L-54`, which carry a layer register — the class
`D24` §5.2 warns about). The register's own share is the 8, and it is non-zero.

```
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
→ coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 \
            force_failures=0 consequence_failures=0 dangling=0 findings=0
→ exit 0
```

The 8 derived records, parsed from the packet's own bytes:

| id | term | base | register | op | axis |
|---|---|---|---|---|---|
| L-55 | tuum | tum | stamp | lengthen | fire |
| L-56 | kit | tik | stamp | reverse | mark |
| L-57 | lom | mol | stamp | reverse | mark |
| L-58 | nees | nes | stamp | lengthen | fire |
| L-59 | huum | hum | stamp | lengthen | fire |
| L-60 | mees | mes | stamp | lengthen | fire |
| L-61 | reek | rek | stamp | lengthen | fire |
| L-62 | saam | sam | stamp | lengthen | fire |

`derivation.op` census over the packet: `{lengthen: 6, reverse: 2}` — the eight rows above, and
nothing else. The packet's contract now declares the fields the forecast asked for
(`examples/culture-d4/packet.d4.yml:40-41`: `derived_from`, `derivation`; `:52` `register_law`), so
F-3's "checked through `derived_from` + `derivation`" is delivered in the schema.

## 3. Which existing legs verify the form class — all green, all current

| leg | command | result |
|---|---|---|
| derivation replay | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | exit 0, `derived_pairs=8 violations=0` |
| derivation replay selftest | `… --selftest` | `selftest: 27/27 checks passed`, exit 0 |
| law gate | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | exit 0, 0 findings |
| law gate selftest | `… --selftest` | `selftest: 45/45 checks passed`, exit 0 |
| typed pipeline (argot wired) | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed`, `ok L3b-argot`, exit 0 |
| assembler | `python3 -B tools/assemble-culture-d4.py --selftest` / `--check` | `81/81 checks passed` / `byte-identical deterministic assembly`, exit 0 |
| typed labels | `python3 -B tools/d2-typed-labels.py --selftest` | `163/163 checks passed`, exit 0 |
| battery | `python3 -B tools/check-gate-battery.py --selftest` | `SELFTEST OK 44/44 controls behaved as expected`, exit 0 |

**Correction to the r25 record.** `reports/round-25/argot/delta.md:8.2` §3b states "The new gate is
not wired into anything … `grep -n "argot" tools/gates/typed-pipeline-gate.py` → 0 lines". That is
**no longer true**: `tools/gates/typed-pipeline-gate.py:84` declares `ARGOT_GATE`, `:517-541` runs it
as leg `L3b-argot` and folds its `D4L-ARGOT-DERIV` FAILs into the verdict, and the run above prints
`ok L3b-argot`. The argot leg is a pipeline leg at this baseline.

The battery registration is real but partial: `tools/check-gate-battery.py:130` registers
`register-law-gate.py` (`REGISTER_LAW_GATE_NAMES`), while `argot-derivation-gate.py` is **not** in
`GATE_NAMES`, `D4_GATE_NAMES` or `REGISTER_LAW_GATE_NAMES` (`:117-132`). So the derivation leg is
reached through the typed pipeline but is not a battery-registered gate. Worth a name if D touches it.

## 4. What content the form class still needs — the residue, named

The forecast's element table (`reports/round-25/argot/forecast.md:33-41`, F-1..F-8) versus the tree:

| # | element | state at `ce103bf` | evidence |
|---|---|---|---|
| F-1 | quote forms derived from a plain base by a declared operation | **DELIVERED** | 8 rows, `derived_pairs=8` |
| F-2 | `head2` for measure words | **DECLARED, UNUSED** | `derivation_ops: [head2, reverse, lengthen]` (`components/04-lexicon.yml:269`), but no record's `op` is `head2`; the packet's own note says "`head2` is declared but unused: over the delivered tree it is an identity" (`packet.d4.yml:281`) |
| F-2b | `reverse` for the numeral series | **DELIVERED as op** | 2 rows (`kit`, `lom`); the numeral series is not built |
| F-3 | `derived_from` + `derivation` fields | **DELIVERED** | `packet.d4.yml:40-41`; 8 records carry both |
| F-4 | relation between two records of the same packet | **DELIVERED** | gate resolves `base` against the packet's own lexicon |
| F-5 | every derived form's check passes, zero fails | **DELIVERED (non-vacuous now)** | `derived_pairs=8 violations=0` — the set has members, so the pass is real |
| F-6 | coverage block reports `derived_forms` / `derived_ok` agreeing | **NOT DELIVERED — and no producer exists** | `grep -rl "derived_forms\|derived_ok" examples tools` → **no match** (exit 1). The only hits repo-wide are filed prose under `reports/round-17..30`. The live coverage block (`examples/culture-d4/typed-labels.d4.yml:29-47`) carries `labels_by_kind`, `typed_labels: 82`, `rank_rules_*`, `reconciliation_records` — no derivation counters |
| F-7 | control: form ≠ `apply(op, base)` → FAIL `D4L-ARGOT-DERIV` | **DELIVERED** | emitted by `argot-derivation-gate.py`; asserted by `c-02-negative-control-rejected` in its 27/27 selftest |
| F-8 | required-controls row C-02 | **DELIVERED** | as F-7 |

Residue, precisely three items:

1. **F-6 — the counter contract.** The gate prints `derived_pairs` / `violations`; the forecast asked
   for `derived_forms` / `derived_ok` **in the coverage block**. r26 dispositioned this as "not
   designed" (`reports/round-26/register/execution-3.md:74`). It is a key-set mismatch, not a missing
   capability — the numbers exist under other names. If D takes this, the honest scope is: add the two
   keys to the projection's coverage block, and the pin cascade follows.
2. **`head2` — declared but with no domain.** Kept deliberately (`packet.d4.yml:281`), and r26
   measured that `head2` is an identity over the delivered tree. A `head2` stratum (measure words)
   does not exist. D should either give it a domain or record it as a permanently declared-but-unused
   operation; the current state is honest prose with no test.
3. **RL-8 — the era leg.** `RGL-05`'s substance (a stamp form is `available_from E1`; an E0 stamp
   claim is a defect) is **specified and unimplemented**: `reports/round-26/register/rules.md:128`,
   `reports/round-27/law/impl-8.md:68` — "the argot gate has no era concept, so an E0-dated stamp form
   produces no finding". The law gate's `DECLARED_KINDS` includes `era`
   (`register-law-gate.py:121`) so the row is *shaped* correctly, but nothing grades the dating.

Also standing, not new: **RL-3**, the register-lexicon ceiling — all 8 forms are material-presence
forms and the 5 legal abstractions refuse `reverse`, so the register cannot spell its own law's
vocabulary (`SCORECARD.md:345`, `:352`).

## 5. The freeze/read-set collision (load-bearing for X00 and R03)

This is the finding the cross seat and reviewer 3 need. It is a **narrow asymmetry, not a hole**, and
both sides are stated so neither is over-read.

**Side A — the packet declares 13 D4 components.** `examples/culture-d4/packet.d4.yml`'s
`assembly.source_sha256` block records **13** D4 component digests, `13-register-law.yml` among them:

```
python3 -c "…re.findall(r'components/(\d\d-[a-z-]+\.yml)', assembly_block)…"
→ 13: 01-brief 02-phonology 03-orthography 04-lexicon 05-naming 06-myth 07-symbolism 08-eras
     09-costumes 10-ritual-calendar 11-contact-history 12-provenance 13-register-law
```

The r7 packet says the same in prose: `packet.md:20` "…thirteen authored components";
`packet.md:66` "13 component digests in its assembly". The renderer agrees:
`tools/exercise-handoff-e2e.py:2783` emits "thirteen authored components".

**Side B — the freeze read set carries 12.** `D4_COMPONENTS`
(`tools/exercise-handoff-e2e.py:157-169`) is a 12-tuple ending at `12-provenance.yml`; it feeds
`V3_READ_SET` (`:1939`). The frozen row's own `inputs` map
(`reports/round-34/handoff/declared-in-r7/expected.json`, 58 entries) contains 12 D4 components, and
`13-register-law.yml` is **absent**:

```
python3 -c "…set(expected['inputs']) & packet_d4_digest_set…"
→ NOT in read set: ['examples/culture-d4/components/13-register-law.yml']
```

The docstring states the undercount as intent: `exercise-handoff-e2e.py:52` "the twelve D4
components"; `freeze.txt:7` "read set: 58 files; component digests 26/26".

**Why the run still passes, and why that is the point.** `v3_verify_component_digests`
(`exercise-handoff-e2e.py:2208`) reads the digests from each **packet's own** `assembly` block, not
from the read set. So it checks 9 D2 + 4 D3 + **13** D4 = 26 — which is exactly the `26/26` in
`freeze.txt:7` and `run.log:9`. The 13th D4 component is therefore verified **transitively**, through
the packet manifest, while the read set that claims to be the run's inputs names only 12.

**The honest consequence, no more and no less.** An edit to `13-register-law.yml` that regenerates the
packet is caught (the packet digest is a read-set member and the packet's own manifest is checked
live). What is *not* true is the reverse reading: the freeze row cannot be audited for completeness by
reading its `inputs` map, because that map omits a file whose bytes the packet it pins depends on.
`13-register-law.yml` sha256 `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`.

**What this means for claim D.** Any D move that edits `13-register-law.yml` or `04-lexicon.yml`
(the two register components — both **are** read-set members for `04-lexicon`, only `13-register-law`
is not) moves the packet, the projection, the typed packet and the hold-set pins together. The
re-pin list is therefore the standard D4 cascade, and it is already enumerated in filed evidence —
r26 `reports/round-26/register/repin.json` (4 new pins + `component_digests` for 01-brief/04-lexicon),
r27 `reports/round-27/pinsweep/d4-pins.json`, r28/r30 rows in `expected-holds.json#pin_generations`
and the `d4` profile in `tools/gates/typed-pipelines.json`. A D change adds a **new** generation row;
filed rows are never edited. `python3 tools/assemble-culture-d4.py --check` → exit 0, so the tree is
currently drift-free and a re-pin would be a clean delta.

## 6. Answers the D block should build on

- **Claim D's `before` is false.** Do not re-build the stratum. Either narrow D to the three-item
  residue in §4, or re-scope it; the scout cannot decide that, the planner must.
- **The `after_required` is already met for the load-bearing half**: "register-form domain non-empty
  with verified forms (derivation replay clean over the new forms; law gate exit 0 over them)" — both
  commands exit 0 with non-vacuous counts at `ce103bf`.
- **"forms verified by two independent seats"**: the two legs are independent of each other
  (`argot-derivation-gate.py` sha256 `b5406bcd…` and `register-law-gate.py` sha256 `15f8b232…`), and
  `typed-pipeline-gate.py` runs the former as a third path. Whether that satisfies the threshold is the
  reviewer's call, not the scout's — but the instruments exist and are green.
- **The nearest real depth gap on this axis** is F-6 plus RL-8, both of which are *additive* (new
  counters, a new era check) and neither of which requires touching filed bytes.

## Owed

- **F-6 producer.** No code path emits `derived_forms` / `derived_ok` anywhere in `examples/` or
  `tools/` (`grep -rl` → no match). Whoever takes F-6 must add the keys *and* a producer; the numbers
  exist only under the names `derived_pairs` / `violations`.
- **`head2` domain.** No measure-word stratum exists; `head2` is a declared operation with zero
  instances. Owner: the D executor who scopes the residue.
- **RL-8 era leg.** Specified, unimplemented; owner recorded in
  `reports/round-27/law/impl-8.md:68` as "whoever grows the leg". Not this seat's.
- **`13-register-law.yml` read-set membership.** The asymmetry in §5 is reported, not repaired —
  `tools/exercise-handoff-e2e.py` is a live tool and changing `D4_COMPONENTS` is a re-pin decision,
  which is the planner's/integrator's, not a scout's.
- **Not measured by this seat:** the round-36 `run-validation.py` does not exist yet
  (`ls reports/round-36/run-validation.py` → No such file), so claim D's declared counting command
  `python3 -B reports/round-36/run-validation.py` is `to-verify` until the integrator lands it. Per
  F-C13-1 it must not be run in-tree regardless.

## Citations

Files (sha256 measured 2026-10-19T09:29:40Z, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223  reports/round-34/handoff/declared-in-r7/freeze.txt
```

Commands run (all from lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml     # exit 0
python3 -B tools/gates/argot-derivation-gate.py --selftest                            # 27/27
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml         # exit 0
python3 -B tools/gates/register-law-gate.py --selftest                                # 45/45
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml       # 20/20, ok L3b-argot
python3 -B tools/assemble-culture-d4.py --selftest                                    # 81/81
python3 -B tools/assemble-culture-d4.py --check                                       # byte-identical
python3 -B tools/d2-typed-labels.py --selftest                                        # 163/163
python3 -B tools/check-gate-battery.py --selftest                                     # 44/44
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                         # exit 0, packet 45f57132…
grep -rl "derived_forms\|derived_ok" examples tools                                    # no match, exit 1
git rev-parse HEAD                                                                     # ce103bf5885af00023cdc4a174c17602476cdcf8
```

Source lines cited: `SCORECARD.md:312,329,345,352,363,400`;
`reports/round-25/argot/current-state.md:5`; `reports/round-25/argot/forecast.md:33-41`;
`reports/round-25/argot/delta.md:8.2`; `reports/round-26/argot/D24-forecast-closure.md:88-92`;
`reports/round-26/register/execution-3.md:74`; `reports/round-26/register/rules.md:128`;
`reports/round-27/law/impl-8.md:68`; `examples/culture-d4/packet.d4.yml:40-41,52,269,281`;
`examples/culture-d4/typed-labels.d4.yml:29-47`; `tools/gates/typed-pipeline-gate.py:84,517-541`;
`tools/check-gate-battery.py:117-132`; `tools/exercise-handoff-e2e.py:52,157-169,1939,2208,2783`;
`reports/round-34/handoff/declared-in-r7/{packet.md:20,66; freeze.txt:7; run.log:9}`.
