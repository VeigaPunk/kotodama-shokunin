# X62 — frozen replay audit (round 27)

- round 27 (operator: loop 3 of 3, build round 3 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` per `reports/round-27/claims.json`) · seat
  **X62** (SCRIBE X62 — frozen replay audit) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X61..X62: pin-sweep double-check + frozen
  replay audit."
- date: 2026-10-18. Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Claim under check:
  `reports/round-27/claims.json` claim **O** (`operability`, capability
  `pin-sweep`), declared baseline
  `4f09c990d4c17f23b5e2cda0871f81db875635fc`; lane HEAD at every measurement
  below `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- canon: **NON-CANON engineering evidence.** This audit admits nothing, certifies
  no round, and grants no promotion. A reproduced red verdict stays red.
- writes: **this file** and its read-only tool
  `reports/round-27/audit/x62-frozen-record-audit.py`, plus gitignored scratch
  under `.scratch/x62/`. No tool, gate, packet, pin, validator or
  shared-bookkeeping byte was edited; no filed round-8–26 artifact was written;
  no commit, no push.
- measurement window: 2026-10-18T19:15Z–19:26Z UTC. **The wave was live
  throughout**: `examples/culture-d4/packet.d4.yml` moved from
  `dd25077bc016…` to `c5441e3d0b23…` inside this window (see §4).

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the frozen surface is **11 generations / 81 rows**; every row's recorded output, snapshot and command re-derive against the record | measured |
| 2 | **0 record findings** — no row's recorded `finding_count` contradicts its own recorded output file, no output or snapshot digest is off, no command names a gate or input its row does not | measured |
| 3 | **0 receipt findings** — every machine receipt that declares rows agrees with its manifest on exit code, finding count, pins and output path | measured |
| 4 | **0 manifest problems** — every manifest carries the documented column schema and no short row | measured |
| 5 | **8 of 11 generations carry a receipt**; the three that do not are `round-3`, `round-3/attempt-1` and `round-11` | measured |
| 6 | **2 of 11 generations carry a README**; the frozen-root index `gate-frozen-run-standard.md:54` declares is absent | **finding X62-B1** |
| 7 | the current generation `round-26/post-register` replays **4/6 reproduced, 2 mismatch (2 supersession, 0 drift)** | measured |
| 8 | the two mismatches are the D4 rows: the **round-27 register-law landing moved the assembler's deterministic output** `dd25077bc016…` → `c5441e3d0b23…`, so the row that pins the pre-landing packet no longer reproduces | **finding X62-B2** |
| 9 | **six rows across two generations read a snapshot in a third generation** (`round-18/repin-d2` and `round-20/repin-d2` → `round-11`) | advisory (§3) |
| 10 | the tool's own controls pass **16/16**, including four record-internals controls that bite on a real frozen row | measured |

## 1. Method — the record, not the row

X61 (`reports/round-27/audit/x61-pin-sweep.md`) sweeps the rows: does each
recorded verdict reproduce? X62 audits the frozen surface **as a record**: is
each generation internally consistent, does its receipt agree with its manifest,
and does the current generation actually replay? The two questions are separate —
a record can be internally consistent and still not reproduce (today's case), and
a row can reproduce while its record contradicts itself.

```sh
export TMPDIR=/var/tmp PYTHONDONTWRITEBYTECODE=1    # outside the repo; see §5
python3 -B reports/round-27/audit/x62-frozen-record-audit.py --selftest   # 16/16, exit 0
python3 -B reports/round-27/audit/x62-frozen-record-audit.py             # text
python3 -B reports/round-27/audit/x62-frozen-record-audit.py --json      # receipt
python3 -B reports/round-27/audit/x62-frozen-record-audit.py --no-replay # records only
```

Four duties: **A** inventory (rows, inputs, receipt, README, foreign snapshots);
**B** record internals (four checks, none of which launches a gate); **C** receipt
agreement; **D** current-generation replay. Only duty D executes anything, so the
receipt distinguishes rows that were *measured* from rows that were *read*.

## 2. The record is internally consistent — 0 findings across 81 rows

Duty B, per row, before any gate runs:

1. the recorded `output` file's `^FINDING ` line count equals the recorded
   `finding_count`;
2. the recorded output's sha256 equals the recorded `output_sha256`;
3. the committed snapshot under `input_snapshot` equals the recorded
   `input_sha256`;
4. the recorded `command` names the same gate and input as the row.

All four hold for **all 81 rows** across all 11 generations. This is the check
that catches a hand-edited record, and it needs no gate to run — so it is
available even where a gate revision has moved out from under its row. It is
exactly the class the standard's §5 step 5 warns about ("write the expected
verdict from what was observed — never from memory") and §6 step 1 verifies.

**Controls (16/16, `--selftest`, 2026-10-18T19:26Z).** The checks are not
asserted to bite; they are made to bite on a **real frozen row**
(`round-26/post-register/d4-source.out`, 12 findings):

| control | injected | caught as |
|---|---|---|
| clean row | none | `audit_row` returns `[]` |
| self-contradicting record | `finding_count` 12 → 13 | `record_inconsistent` |
| re-written output | `output_sha256` → `b`×64 | `output_tampered` |
| command naming another gate | `command` → `other-gate.py` | `record_inconsistent` |

The remaining controls cover the manifest header, the path refusals, the absent
receipt, the in-repo mirror and the unaddressable-receipt shape.

## 3. Receipt agreement — three shapes, all addressed

Four generations carry a machine `freeze-receipt.json`, and they do **not** share
a schema. A comparator that assumed one shape would either crash or silently skip
rows, so the tool routes each receipt to its own comparison and reports a shape it
cannot address as such, never as a pass:

| generation | receipt shape | rows addressed | findings |
|---|---|---:|---:|
| `round-18` | `rows`: list of row objects | 2 | 0 |
| `round-22/d4-repin` | `manifest_rows`: list | 3 | 0 |
| `round-26/gate-input` | `rows`: int + `verdicts`: list of `{label, exit, findings}` | 6 | 0 |
| `round-26/post-register` | same as above, plus `pins` and `input_pins` maps | 6 | 0 |

For the round-26 shape the `verdicts` are **positional labels, not row
addresses**, so they are compared against the manifest in manifest order and the
receipt's `pins` / `input_pins` maps are compared against the manifest's digests
separately. The first draft of this tool compared every receipt by `(gate, input)`
key and reported thirteen spurious findings — six per round-26 generation because
the verdicts carry no key, and one for round-22 whose rows live under
`manifest_rows`. That defect is fixed and the shape-aware routing is what §3 now
reports; the "unaddressable receipt is not a pass" control guards the regression.

## 4. Finding X62-B2 — the current generation is superseded mid-round

Duty D replays the newest generation (`round-26/post-register`, 6 rows) in a
mirror outside the repo:

| row | gate | input | recorded | observed | class |
|---|---|---|---:|---:|---|
| 2 | `typed-pipeline-gate.py` | `examples/culture-d4/packet.d4.yml` | exit 0, 12 findings | **exit 2, 0 findings** | supersession |
| 3 | `typed-pipeline-gate.py` | `examples/culture-d4/packet.d4.typed.yml` | exit 0, 12 findings | **exit 2, 0 findings** | supersession |
| 4 | `typed-pipeline-gate.py` | `examples/culture-d2/packet.d2.yml` | exit 0, 15 findings | reproduced | — |
| 5 | `typed-pipeline-gate.py` | `examples/culture-d2/packet.d2.typed.yml` | exit 0, 15 findings | reproduced | — |
| 6 | `typed-pipeline-gate.py` | `…/controls/typed-without-source.yml` | exit 2, 0 findings | reproduced | — |
| 7 | `typed-pipeline-gate.py` | `…/controls/typed-stale-source.yml` | exit 2, 0 findings | reproduced | — |

**Tally: 4/6 reproduced, 2 mismatch (2 supersession, 0 drift), 0
could-not-evaluate.** Both mismatches are the D4 input-class rows, and the cause
is measured, not inferred:

```
$ export TMPDIR=/var/tmp; M=$(mktemp -d /var/tmp/x62-XXXX); mkdir -p $M/examples/culture-d4
$ cp tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml \
     $M/examples/culture-d4/packet.d4.yml
$ cd $M && python3 <lane>/tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
FAIL L1-assembler: packet bytes dd25077bc016 are not tools/assemble-culture-d4.py's
                   deterministic assembly (c5441e3d0b23)
```

The round-27 register-law landing moved the deterministic assembly output of
`tools/assemble-culture-d4.py` from `dd25077bc016…` to `c5441e3d0b23…` while this
seat measured (`sha256sum examples/culture-d4/packet.d4.yml`, 19:24Z:
`c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a`). The
`round-26/post-register` generation pins the **pre-landing** packet
(`dd25077bc016…`), so its two D4 rows are superseded — exactly the mechanism the
round-26 D20 seat named, recurring one round later. The gate bytes themselves are
unchanged (`b749ad07cf17…` at HEAD, the generation's own pin), which is why this
reads as a supersession and not a `gate_digest_mismatch`.

**Why this matters for claim O.** Claim O's `after_required` asks for "every
frozen manifest … re-verified against the amended packet". At this stamp the
*newest* generation on the tree does **not** reproduce against the amended packet
— it is superseded by it. The X61 sweep reports the same two rows as
supersessions, by different machinery. Whether that is a gap in the sweep or a
re-pin the round must still land is the parent's reading; this seat records the
measurement and does not launder a supersession into a pass.

## 5. Finding X62-B1 — the frozen-root index is absent

`corpus/knowledge/verification/gate-frozen-run-standard.md:54` lays out the
frozen tree with a root index:

```text
tools/gates/frozen/
  README.md                          # index: baseline id → gate, revision, verdict class
```

Measured: **absent**. Duty A counts **2 of 11 generations** carrying a README
(`round-11`, `round-18`), and none at the frozen root. The standard's §5 step 7
requires "Commit the baseline with its README index row" — so six generations
after round 18 have no home for that row. Same finding as X61-B2, reached by the
inventory duty rather than by a `test -f`; both name it as a gap on the lane's own
verification knowledge surface, handed to the parent.

## 6. Advisory — six rows read across a generation boundary

Duty A counts each row's `input_snapshot` against its own generation directory:

| generation | rows | own snapshot | foreign snapshot rows |
|---|---:|---:|---:|
| `round-11` | 11 | 11 | 0 |
| `round-18/repin-d2` | 11 | 0 | 11 |
| `round-20/repin-d2` | 11 | 0 | 11 |
| `round-23/repin-d2` | 11 | 11 | 0 |

`round-18/repin-d2` and `round-20/repin-d2` both read three distinct files under
`tools/gates/frozen/round-11/typed-pipeline/`. Every one of the 81 rows' snapshots
verifies against its pin, so nothing is broken — but the re-pin directory is not a
complete record of its own read set, and a future edit to the round-11 generation
would move twenty-two rows across two later generations at once.
`round-23/repin-d2` is the contrast case: the same duty, its own snapshots.
Recorded, not repaired — no historical manifest may be edited.

## 7. Cross-checks against the peer instruments

| reading | this tool | peer | agree |
|---|---|---|---|
| rows / generations | 81 / 11 | `replay-frozen.py` over `**/MANIFEST.tsv`: 81 / 11 | yes |
| row verdicts (X61 sweep) | supersession ×6, drift ×0 | X61: supersession ×6, drift ×0 | yes |
| current generation | 4/6 reproduced, 2 supersession | X61 `round-26/post-register`: 6/6 **before** the landing; X61's later sample reads the same supersession | time-ordered |
| baselines pinned | not this tool's duty | X61: 19/19; battery: 19/19 | yes |
| battery coverage | not this tool's duty | `check-gate-battery.py`: 9/9, exit 0 | yes |

The current-generation disagreement with X61's *first* sample is not a
disagreement: X61 read `round-26/post-register` 6/6 at 19:14Z, before the
round-27 D landing moved the assembler output; this seat read it 4/6 at 19:24Z,
after. The live wave is why every number here names its stamp.

## 8. Limits

- **Reproduction is not correctness.** A reproduced `exit_code=2` control is still
  a refusal; a reproduced 12-finding row is still twelve open holds. Nothing here
  reads a design as clean.
- **The record checks prove internal consistency, not truth.** A record whose
  output file, count, pin and command all agree can still describe a gate run
  that never happened; what it cannot do is survive a later hand-edit without
  contradicting itself. Digest agreement is not a truth measure
  (`gate-frozen-run-standard.md` KTD-FR-S-0007).
- **Only the current generation is re-executed.** Historical generations are read
  as records; a historical row that would now reproduce is not re-run here, and a
  historical row's staleness is X61's reading, not this one.
- **One generation is named `CURRENT` by hand.** A later round that lands a newer
  generation makes `round-26/post-register` historical and this tool would keep
  replaying it until taught otherwise; the constant is stated in the source.
- **`/tmp` was unusable during this window** (tmpfs at 80%, `Errno 122 Disk quota
  exceeded`), so every replay here used `TMPDIR=/var/tmp`. The TMPDIR constraint
  itself is X61-B1; this is a second, independent reason to name the mirror parent
  in any replay receipt.
