# X62 — frozen replay audit (round 28)

- round 28 (operator: loop 3 of 3, build round 4 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` per `reports/round-28/claims.json`) · seat
  **X62** (SCRIBE X62 — replay audit) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X61..X62: sweep double-check + replay audit."
- date: 2026-10-18. Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Claim under check:
  `reports/round-28/claims.json` claim **O** (`operability`, capability
  `final-pin-sweep`), declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`; lane HEAD at every measurement
  below `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- canon: **NON-CANON engineering evidence.** This audit admits nothing, certifies
  no round, and grants no promotion. A reproduced red verdict stays red.
- writes: **this file** and its read-only tool
  `reports/round-28/audit/x62-frozen-record-audit.py`, plus gitignored scratch
  under `.scratch/x62-r28/`. No tool, gate, packet, pin, validator or
  shared-bookkeeping byte was edited; no filed round-8–27 artifact was written;
  no commit, no push. `export TMPDIR` preceded every scratch-writing command.
- measurement window: 2026-10-18T20:11Z–20:16Z UTC. **The wave was live
  throughout**; the packet moved `86079a67…` → `543d68a8…` inside the window.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the frozen surface is **12 generations / 86 rows**; every row's recorded output, snapshot and command re-derive against the record | measured |
| 2 | **0 record findings** — no row's recorded `finding_count` contradicts its own recorded output file, no output or snapshot digest is off, no command names a gate or input its row does not | measured |
| 3 | **0 receipt findings** — every machine receipt that declares rows agrees with its manifest on exit code, finding count, pins and output path | measured |
| 4 | **0 manifest problems** — every manifest carries the documented column schema and no short row | measured |
| 5 | receipts: `freeze-receipt.json` **4/12**, `freeze.txt` **5/12**, either **8/12**; READMEs **2/12** | measured |
| 6 | the current generation `round-26/post-register` replays **4/6 reproduced, 2 mismatch (2 supersession, 0 drift)** | measured |
| 7 | both mismatches are the D4 rows: the **round-27 law landing and the round-28 RL-4 fix moved the packet** `86079a67…` → `543d68a8…` (and the typed packet `1c4b8808…` → `15c81ec1…`), so the row that pins the pre-landing packet no longer reproduces | measured |
| 8 | **0 of the 2 moved rows carry a later generation at the live digest** | **finding X62R28-A2** |
| 9 | `tools/gates/frozen/README.md` is declared by `gate-frozen-run-standard.md:54` and is **absent**, so **12 of 12 generations are unindexed** | **finding X62-B1** (round-27, now sized) |
| 10 | six rows across two generations read a snapshot in a third generation | advisory (§3) |
| 11 | the tool's own controls pass **22/22**, including four record-internals controls that bite on a real frozen row and five duty-E successor controls | measured |
| 12 | the round's own validator independently flags one filed round-27 artifact as changed from the declared baseline; §6 measures it and reports the tree as clean at this stamp | measured |

## 1. Method — the record, not the row

X61 (`reports/round-28/audit/x61-pin-sweep.md`) sweeps the rows: does each
recorded verdict reproduce? X62 audits the frozen surface **as a record**: is each
generation internally consistent, does its receipt agree with its manifest, and
does the current generation actually replay? The two questions are separate — a
record can be internally consistent and still not reproduce (today's case), and a
row can reproduce while its record contradicts itself.

```sh
export TMPDIR=/var/tmp PYTHONDONTWRITEBYTECODE=1   # see X61 §5 — /tmp is a shared tmpfs
python3 -B reports/round-28/audit/x62-frozen-record-audit.py --selftest   # 22/22, exit 0
python3 -B reports/round-28/audit/x62-frozen-record-audit.py             # text
python3 -B reports/round-28/audit/x62-frozen-record-audit.py --json      # receipt
python3 -B reports/round-28/audit/x62-frozen-record-audit.py --no-replay # records only
```

Six duties: **A** inventory; **B** record internals (four checks, none of which
launches a gate); **C** receipt agreement; **D** current-generation replay;
**E** successor coverage (new this round); **F** frozen-root index (new this
round). Only duty D executes anything, so the receipt names which rows were
*measured* and which were *read*.

## 2. The record is internally consistent, and that is not a small result

| duty | check | rows | findings |
|---|---|---:|---:|
| B | recorded output's `^FINDING ` count vs recorded `finding_count` | 86 | **0** |
| B | recorded output's digest vs `output_sha256` | 86 | **0** |
| B | committed snapshot vs `input_sha256` | 86 | **0** |
| B | recorded `command` names the row's own gate and input | 86 | **0** |
| C | receipt-declared rows vs manifest rows | 26 | **0** |
| A | manifest column schema, short rows | 12 | **0** |

Duty B is the check that catches a hand-edited record, and it needs no gate. It
is clean across all 86 rows, including the 25 rows X61 cannot evaluate: a stale
gate pin makes a row *unreproducible*, it does not make the row *inconsistent*.
Keeping those two readings apart is the point of having both seats.

Duty C covers 26 declared rows across 4 receipts:

| generation | receipt | declared rows | findings |
|---|---|---:|---:|
| `frozen/round-18` | `freeze-receipt.json` | 2 | 0 |
| `frozen/round-22/d4-repin` | `freeze-receipt.json` | 3 | 0 |
| `frozen/round-26/gate-input` | `freeze-receipt.json` | 6 | 0 |
| `frozen/round-26/post-register` | `freeze-receipt.json` | 6 | 0 |

Three receipt shapes exist on this tree and each is handled shape-aware: a `rows`
list of objects (round-18, round-22), and an int `rows` with a positional
`verdicts` list plus `pins` / `input_pins` maps (round-26, both generations). A
shape the function cannot address is reported as such, never as a pass — the
control `unaddressable receipt is not a pass` measures that.

**A definitional correction to round 27.** Round-27's X62 reported "8 of 11
generations carry a receipt" by counting either `freeze.txt` or
`freeze-receipt.json`. Those are two different things: `freeze-receipt.json` is
the machine receipt duty C compares against; `freeze.txt` is the human one. This
round splits the count — **json 4, txt 5, either 8** — so the shape of the record
stays visible instead of collapsing into one number. The "either" figure
reproduces round-27's 8 exactly; the extra generation is the round-17 manifest,
which round-27's scope missed (X61 §2, finding X61R28-A1).

## 3. The current generation, replayed

`round-26/post-register` — 4 reproduced, 2 mismatch, 0 could-not-evaluate:

| row | gate | input | observed | recorded | verdict |
|---:|---|---|---|---|---|
| 2 | `typed-pipeline-gate.py` | `examples/culture-d4/packet.d4.yml` | exit 2, 0 findings | exit 0, 12 findings | **mismatch** (supersession) |
| 3 | `typed-pipeline-gate.py` | `examples/culture-d4/packet.d4.typed.yml` | exit 2, 0 findings | exit 0, 12 findings | **mismatch** (supersession) |
| 4 | `typed-pipeline-gate.py` | `examples/culture-d2/packet.d2.yml` | exit 0, 15 findings | exit 0, 15 | reproduced |
| 5 | `typed-pipeline-gate.py` | `examples/culture-d2/packet.d2.typed.yml` | exit 0, 15 findings | exit 0, 15 | reproduced |
| 6 | `typed-pipeline-gate.py` | `controls/typed-without-source.yml` | exit 2, 0 findings | exit 2, 0 | reproduced |
| 7 | `typed-pipeline-gate.py` | `controls/typed-stale-source.yml` | exit 2, 0 findings | exit 2, 0 | reproduced |

Both mismatches are supersessions, not drift: the live input each row names no
longer hashes to the row's own `input_sha256`. The moved surfaces:

| surface | frozen pin | live | moved by |
|---|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `dd25077bc016…` | `543d68a82640…` | round-27 law landing, then the round-28 RL-4 fix |
| `examples/culture-d4/packet.d4.typed.yml` | `618a78c90fc0…` | `15c81ec11b42…` | same |

**The two control rows still reproduce exactly**, and that is the reading that
matters most here: `typed-without-source.yml` and `typed-stale-source.yml` are
the negative controls frozen in round 26, and they still refuse with exit 2 and
zero findings. A generation whose controls still bite has not rotted — it has
been superseded on two positive rows while its refusals hold.

**X62R28-A2 — the current generation has no successor inside the frozen root, and
its two moved rows have none anywhere.** Duty E asks, for every moved row,
whether a later generation pins the live digest. Here the answer is 0 of 2, and
for two separate reasons:

1. **No generation after `round-26/post-register` exists in the frozen root.**
   `round-27` and `round-28` both froze their successors outside it, at
   `reports/round-27/pinsweep/frozen/r27-post/` and
   `reports/round-28/pinsweep/frozen/r28-post/`. A successor question asked only
   of `tools/gates/frozen/**` can therefore never be answered yes.
2. **Even repo-wide, these two rows have no successor.** Both re-pin manifests
   declare only the two D4 adapter rows:

   ```sh
   cut -f1,3 reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv
   # tools/gates/d4-assembly-check-gate.py     examples/culture-d4/packet.d4.yml
   # tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
   ```

   The moved rows here are `typed-pipeline-gate.py` rows, and no re-pin manifest
   on this tree names that gate. This is the same finding X61 §2 (X61R28-A2)
   reaches from the row side, by different machinery — two seats, one finding.

## 4. Inventory: receipts, READMEs, and foreign snapshots

| generation | rows | `freeze-receipt.json` | `freeze.txt` | README |
|---|---:|---|---|---|
| `frozen/round-11` | 11 | no | no | **yes** |
| `frozen/round-18` | 2 | **yes** | no | **yes** |
| `frozen/round-18/repin-d2` | 11 | no | **yes** | no |
| `frozen/round-20/repin-d2` | 11 | no | **yes** | no |
| `frozen/round-22/d4-repin` | 3 | **yes** | **yes** | no |
| `frozen/round-23/repin-d2` | 11 | no | **yes** | no |
| `frozen/round-25/gate-input` | 6 | no | **yes** | no |
| `frozen/round-26/gate-input` | 6 | **yes** | no | no |
| `frozen/round-26/post-register` | 6 | **yes** | no | no |
| `frozen/round-3` | 7 | no | no | no |
| `frozen/round-3/attempt-1` | 7 | no | no | no |
| `reports/round-17/tests/frozen` | 5 | no | no | no |

**Advisory: six rows across two generations read a snapshot in a third
generation.** `round-18/repin-d2` and `round-20/repin-d2` pin their D2 rows
against snapshots under `round-11/typed-pipeline/`. A generation that reads
outside its own directory is not wrong — round 27's sweep called this "current
(its packet is its own snapshot)" for the round-17 manifest and it is a legitimate
pattern — but it means a reader cannot audit one generation directory in
isolation. Advisory, not a finding.

**X62-B1, now sized.** `corpus/knowledge/verification/gate-frozen-run-standard.md:54`
declares the layout:

```text
tools/gates/frozen/
  README.md                          # index: baseline id → gate, revision, verdict class
```

That file does not exist. Duty F measures the cost of its absence:
**`index_present: false`, `generations_unindexed: 12`**. Round 27 filed the same
finding as a boolean (its X61-B2 / X62-B1); this round attaches the size, because
"the index is missing" and "twelve generations have no index" are different
amounts of work. The standard is present and does declare the index
(`index_declared: true`), so this is not a stale-document problem — it is a
documented artifact that was never built.

## 5. Controls

22 controls, all passing. The four that bite on real frozen bytes:

| control | what it measures |
|---|---|
| `a clean frozen row audits clean` | a real `round-26/post-register` row audits to zero findings, so duty B is not vacuous |
| `a self-contradicting record is caught` | `finding_count + 1` on that same real row produces `record_inconsistent` |
| `a re-written output is caught` | a flipped `output_sha256` produces `output_tampered` |
| `a command naming another gate is caught` | a `command` naming a peer gate produces `record_inconsistent` |

Plus five duty-E successor controls (`a later row at the live digest is a re-pin`,
`an earlier superseded row is not a successor`, `verdict is order-independent`,
`a row is never its own successor`, and `an out-of-scope successor reads declared
but not in-scope` — the last one pins the exact round-28 shape), three
generation-ordinal controls, four unsafe-path refusals, three command-parsing
controls and two duty-F controls. Duty E's index and scope are injectable, so all
five successor controls run in memory and never read the repo.

**Disclosed defect.** The first draft's `a clean frozen row audits clean` control
**failed**, and it was the control that was wrong, not the tool: the fixture set
`input_sha256` to a placeholder digest while `audit_row` checks the *snapshot*
against that pin. The fixture now derives the pin from the real committed
snapshot. The failure was worth keeping in the record because it is the control
doing its job — a control that cannot fail is not a control.

## 6. One filed round-27 artifact changed, and it is restored

At 20:13Z this seat's window caught `reports/round-27/gate-tests/receipt.json`
modified in the working tree: its recorded `d4-source` and `d4-typed` runs had
been re-executed at 20:13:19Z against the just-moved packet and rewritten
in place from `exit 0 / 12 hold lines` to `exit 2 / 0 hold lines`. That is a
filed round-27 artifact being overwritten during a round-28 wave.

Measured now:

```sh
git hash-object reports/round-27/gate-tests/receipt.json     # 854ed1a37805a7f8…
git show 6c0ac44:reports/round-27/gate-tests/receipt.json | git hash-object --stdin
                                                             # 854ed1a37805a7f8…
```

Both sides hash `854ed1a3…`: **the file matches the declared baseline at this
stamp**, so the in-place write did not survive. The round's own validator
independently recorded the same event — `reports/round-28/validation.json`
carries `protected_filed_artifacts.measurement.differences` naming
`reports/round-27/gate-tests/receipt.json` with `baseline_blob 854ed1a3…` and
`observed_blob fbc1f4b6…` at `measured_at_utc 2026-10-18T20:13:51+00:00`, one
difference out of 1587 protected paths. Two instruments, independently, caught
the same transient in the same minute.

This is the class the lane's `tools/harness/receipt_guard.py` exists to prevent
(`F4` in `reports/round-24/cold-run.md:30`: "those scripts overwrite filed
receipts in place"). It is reported here as an **observed transient that was
recovered**, not as a live defect; a reader at a later stamp should re-take the
hash rather than trust this one. What the tree needs at close is the round-28
receipt under `reports/round-28/gate-tests/`, which exists.

## 7. Findings

| id | finding | level | evidence |
|---|---|---|---|
| **X62R28-A2** | 0 of 2 moved rows in the current generation carry a later generation at the live digest: no generation follows it in the frozen root, and no re-pin manifest anywhere on the tree names `typed-pipeline-gate.py` | **coverage gap + convention** | §3; `grep -c typed-pipeline-gate reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` → 0; X61 §2 reaches the same finding from the row side |
| **X62-B1** | `tools/gates/frozen/README.md` is declared by the standard and absent; **12 generations are unindexed** | standing (round-27), now sized | §4 |
| **X62R28-A3** | `reports/round-27/gate-tests/receipt.json` was rewritten in place mid-wave and is restored at this stamp; the same event is in the round's own validator | measured transient, recovered | §6 |
| — | the record is internally consistent across all 86 rows and all 26 receipt-declared rows | measured | §2 |
| — | the current generation's two control rows still reproduce their refusals exactly | measured | §3 |
| — | six rows across two generations read a snapshot in a third | advisory | §4 |

## 8. What this seat did not check

- It adjudicates nothing. Claim O's verdict is the runner's to issue, and
  `reports/round-28/validation.json` is the record of it.
- It does not verify that a re-pinned row's *content* is honest — only that a
  digest matches. A pin is integrity, never truth and never clearance.
- It reads the historical generations as records (duties A–C) and re-executes
  only the current one (duty D), so the receipt names which rows were *measured*
  and which were *read*. A historical generation's exit code is not re-measured
  here; X61 §3 does that.
