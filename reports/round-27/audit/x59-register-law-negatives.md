# R27-X59 — shard audit: the register law's negatives

- **Seat:** SCRIBE **X59** (shard auditor — law negatives), round 27 (operator:
  loop 3 of 3, build 3 of 4; 64 workers on `devin/deepseek-v4-1-flash-high`).
- **Claim audited:** **D / depth** `register-law` (`reports/round-27/claims.json`).
  Its `after_required` reads: "the register law lands: a D4 component declares the
  stamp register's speech-act rules (what may be said in-register, by whom, with
  what record consequences), wired into the packet deterministically; the
  syllabify disagreement fixed (one algorithm, forms re-verified)".
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`claims.json:5`); lane HEAD at this audit `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- **Write scope:** `reports/round-27/audit/x59-register-law-negatives.py` and this
  file, plus gitignored scratch under `.scratch/x59/`. **No component, packet,
  tool, gate, fixture, pin, corpus entry or filed round-8–26 byte was written**;
  no commit, no push. `export TMPDIR=$PWD/.scratch` preceded every scratch write;
  the two clone-based controls below ran under `.scratch/x59/` and wrote nothing
  in the lane worktree.
- **Canon:** NON-CANON engineering evidence. This audit adjudicates no round; it
  reports what the delivered bytes do against the law the claim names.

## 0. Headline

**The register law landed while this audit ran. Its arithmetic and admissibility
halves are green; two properties of the landing remain unenforced, and both are
reproducible.**

| # | finding | level |
|---|---|---|
| **X59-F1** | The law landed as a **new top-level `register_law:` block** in `examples/culture-d4/components/13-register-law.yml` (rows `RGL-01..05`), contributed through the component's own `packet_keys: [register_law]` declaration. This audit re-derived it from the packet, not from the seat's prose. | the claim's core clause **landed** |
| **X59-F2** | **A tampered law value is invisible to every delivered gate.** Independently reproduced end-to-end: a `holder` edit yields exactly the same 12 projector findings as the clean packet. The law is a declaration with no teeth. | standing HOLD (`L6b`) |
| **X59-F3** | The `register_law` block is declared in **neither** `PACKET_KEYS` nor `RECORD_FIELDS` in `tools/assemble-culture-d4.py`. A/B control in a scratch clone: stripping an `id` from a `register_law` row assembles **exit 0** (landing `id: None`); the same edit to a `lexicon` row refuses **exit 2**. | standing HOLD (`L9`) |
| **X59-F4** | The eight delivered `stamp` records pass **every** negative this auditor constructs: axis→op 8/8, era 8/8, admissibility 8/8, oath-void 8/8, reference resolution 8/8. The landed half is sound. | pass |
| **X59-F5** | The syllabify fix **did** land: `tools/gates/argot-derivation-gate.py` moved from `5b5abe78…` (round-25 bytes) to `b5406bcd…`. The sibling X54 seat measures the divergence in depth; this audit confirms the digest moved and does not re-grade it. | the claim's second clause **landed** |

The two HOLDs are the honest state, not a defect of the landing: the D seats'
own design names the enforcement gap (`reports/round-27/law/rules.md` §1 marks
five of six rules "replayable? **no**", `LL-3`). They are recorded here because a
reader of the claim alone would not see them.

## 1. What was measured, at what revision

Digests read by this seat at the close of this audit, 2026-10-18 (`sha256sum`):

| surface | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc` |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` |
| `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `examples/culture-d4/expected-holds.json` | `857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f` |
| `reports/round-27/run-validation.py` | `7c8c725c68183b110aa78101ed0235db5bc18367aea00c872d487cfeb191b725` |

**The tree moved under this audit.** The packet digest went `dd25077b…` (round-26)
→ `c5441e3d…` → `86079a67…` across the window, and the gate digest moved once.
Every number below was taken at the `86079a67…` packet and the `b5406bcd…` gate;
the §1 digests are the control that fixes which bytes were graded. A reader
re-running this fragment on a later tree must re-take the digests.

## 2. The independent instrument

**Instrument:** `reports/round-27/audit/x59-register-law-negatives.py` (new, this
seat's; NON-CANON audit evidence, not a lane gate). It is deliberately built on
different machinery from the gate it audits:

| dimension | the lane gate | this instrument |
|---|---|---|
| YAML parsing | the naming gate's hand-checked subset loader (`runpy` by path) | `ruby -ryaml -rjson` (a full YAML 1.1 loader) |
| `reverse` / `lengthen` | the gate's `OP_FUNCTIONS` + the packet's `pattern`/`output` pair | re-implemented here from the design prose (`design-language.md` §5) |
| kernel dependency | loads `naming-collision-gate.py` by path | none — no lane code is imported |

**Controls (a checker that cannot say no is not a checker).** Eight planted
controls, all caught:

```
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py --controls
control-1-op-contradicts-axis      ok  law=L3  findings=3
control-2-early-era                ok  law=L4  findings=3
control-3-form-mismatch            ok  law=L3  findings=3
control-4-stray-construction       ok  law=L5  findings=3
control-5-oath-in-register         ok  law=L7  findings=3
control-6-dangling-doublet         ok  law=L8  findings=3
control-6b-law-row-without-id      ok  law=L9  findings=2
control-7-clean-stays-clean        ok  law=no-FAIL  findings=2
controls: 8/8 caught
```

`control-7` asserts **no FAIL** rather than zero findings, and says why: the two
HOLDs below are standing properties of the tree that no packet bytes can remove,
so a control requiring an empty finding list could never pass. A control that
cannot pass is not a control.

## 3. The nine laws, and the verdict on the delivered packet

```
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py
counters: admissibility_checked=8 era_checked=8 law_rows=5 law_wiring_checked=5
  oath_checked=8 plain_records=0 records=62 refs_checked=8 register_law_block=5
  register_rows=4 rule_checked=8 speech_act_rows=5 stamp_records=8
findings: L6b HOLD, L9 HOLD
```

| law | what it tests | verdict |
|---|---|---|
| **L1** | the `registers:` block declares the identity rows `QREG-01..04` | **pass** — 4 rows |
| **L2** | `plain` is declared `unmarked`; no plain record is graded register-scoped | **pass** — 0 scoped |
| **L3** | every `stamp` record's op equals its axis's selection **and** replays to the delivered form under this instrument's own operations | **pass 8/8** |
| **L4** | every `stamp` record is staged E1 or later | **pass 8/8** (all E1) |
| **L5** | every `stamp` record rides a `STAMP-*` construction | **pass 8/8** |
| **L6** | a speech-act law surface exists and every law row carries a speech-act field | **pass** — 5 rows, all carry `act`/`holder`/`consequence` |
| **L6b** | a tampered law value is visible to some gate | **HOLD** — the enforcement leg is unowned (X59-F2) |
| **L7** | no `stamp` record sits in the religion field | **pass 8/8** |
| **L8** | `doublet_of` and `derivation.base` resolve to delivered records | **pass 8/8** |
| **L9** | the assembler declares and validates the `register_law` block | **HOLD** — the block is in neither `PACKET_KEYS` nor `RECORD_FIELDS` (X59-F3) |

## 4. X59-F1 — the law landed, and where

The law reached the packet as a **new top-level block**, not as rows inside
`registers:`:

```
$ python3 -c "… ruby -ryaml … print([r['id'] for r in packet['register_law']])"
['RGL-01', 'RGL-02', 'RGL-03', 'RGL-04', 'RGL-05']
$ python3 -c "… print(sorted({k for r in packet['register_law'] for k in r}))"
['act', 'axis', 'cite', 'consequence', 'evidence', 'follows', 'holder', 'id', 'kind', 'register']
```

The component carries its own `packet_keys: [register_law]` declaration
(`13-register-law.yml:18`), and the assembler honours a per-file declaration over
its global `PACKET_KEYS` list (`tools/assemble-culture-d4.py:258-262`) — which is
why the block reaches the packet even though `register_law` is not in the
assembler's global key set. The five rows state, per the claim's own clause, the
**act**, the **holder**, and the **consequence**; `kind` distinguishes
admissibility / exclusion / asymmetry / no-segment / era.

**The instrument accepts three landing shapes** (`RGL-0n` in `registers:`,
`QREG-05..` speech-act rows in `registers:`, or a top-level `register_law:`
block), because the tree used the first in round 26's design and the third in
round 27's landing. A later shape change will not need an edit.

**A note on the shape chosen.** Round 26's design named the rows `RGL-01..05` and
placed them in `registers:`; the round-27 landing kept the ids and moved the block
to its own top level, in a new component `13-register-law.yml`. The
`contract.record_fields.registers` list (`[id, title, register, class, law, axis,
evidence, follows]`) does not fit these rows — they carry `act`/`holder`/`kind`
instead of `title`/`class`/`law` — which is consistent with the block having been
given its own namespace rather than being folded into `registers:`.

## 5. X59-F2 — independently reproduced: the law has no teeth

The round-27 design reports this itself (`reports/round-27/law/rules.md` §3.1,
control `C-A4`). This seat re-derived the property **end-to-end**, not by reading
the design's probe: a scratch clone with the `holder` of `RGL-03` rewritten to a
nonsense value still emits **exactly 12 findings**, identical to the clean packet.

```
$ cd .scratch/x59/clone   # git clone --shared, then the tampered component copied in
$ python3 tools/assemble-culture-d4.py            # exit 0
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml | grep -c '^FINDING'
12                                                # the clean packet also emits 12
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml | grep -ci 'register_law\|RGL-0'
0
```

**Why this matters for the claim.** The claim's `after_required` asks that the law
be "wired into the packet deterministically". The landing satisfies *presence* and
*determinism*: the rows flow through the assembler byte-deterministically, and the
typed pipeline is green (`20/20 legs` source, `17/17` typed). It does **not**
create enforcement: no delivered gate reads `act`, `holder`, `kind` or
`consequence`. The design is honest about this — `law/rules.md` §1 marks five of
six rules "replayable? **no**" and names the gap `LL-3` rather than presenting it
green. This fragment exists so the parent sees both halves: **the law lands as a
declaration; the enforcement leg is a named, unowned gap.**

**Corroboration, stated as corroboration.** The design seat reached the same
conclusion from its own probe (`.scratch/r27-law/A/culture-d4/packet.tamper.yml`,
`grep -c FINDING` → 12, identical to clean). This seat's route differs: it tampers
in a fresh clone through its own loader and compares finding sets. The two are
independent confirmations of one property of the tree.

## 6. X59-F3 — the `register_law` block is declared but not validated

The assembler's record validator keys on `RECORD_FIELDS`
(`tools/assemble-culture-d4.py:118-125`), and `register_law` is absent from both
`RECORD_FIELDS` and the global `PACKET_KEYS`:

```
$ grep -c 'register_law' tools/assemble-culture-d4.py
0
```

So a malformed row is not refused. **A/B control, scratch clones, identical
edit:**

```
$ python3 - <<'PY'   # in a clone, on 13-register-law.yml
   replace '- {id: RGL-01,' -> '- {zzz_no_id: 1,'
$ python3 tools/assemble-culture-d4.py    ; echo $?
0                                          # exit 0 — the row lands with id: None
$ python3 -c "… print([r.get('id') for r in packet['register_law']])"
[None, 'RGL-02', 'RGL-03', 'RGL-04', 'RGL-05']

# the same edit to a lexicon row (the control that shows the validator works
# where the field list exists):
$ python3 tools/assemble-culture-d4.py    ; echo $?
2                                          # exit 2 — refused
```

**Reading.** The block reached the packet by a route the assembler's schema does
not know: the component's own `packet_keys` declaration. That is a legitimate
mechanism (`assemble-culture-d4.py:230`), but it means the block has no field
list, so its rows are never checked for the one field every other record type is
checked for. The `contract.record_fields` declaration was added mid-audit
(`register_law` is now present there), which narrows the gap to the assembler's
own validator — but the validator is what refuses a bad row, and it still does
not.

## 7. X59-F5 — the syllabify fix landed

The claim's second clause is "the syllabify disagreement fixed (one algorithm,
forms re-verified)". At this audit's start the gate had not moved
(`5b5abe78…`, the round-25 bytes); at its close it had:

```
$ sha256sum tools/gates/argot-derivation-gate.py
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb
```

The sibling X54 seat measures the divergence in depth (it adds the packet's own
`syllables:` field as a third witness, which no earlier round consulted) and
reports `gate_emits_non_syllable: []` on the settled tree — down from 67 of 70.
This audit confirms the digest moved and **does not** re-grade the algorithm: X54
owns that measurement. The corroboration is noted, not claimed as this seat's.

## 8. What this seat did *not* do

- It did **not** grade the round-27 D claim. It measured the law surface and
  reports the two HOLDs; whether they block acceptance is the parent's call.
- It did **not** edit any component, packet, gate, fixture, pin, corpus entry or
  sibling fragment. The two clone-based controls ran under `.scratch/x59/` and
  wrote nothing in the lane worktree.
- It did **not** re-measure the syllabify divergence (X54 owns it) or the sweep
  inventory (X60/O37 own that).
- It did **not** run the round-27 counting command as its own verdict; it ran it
  once and reports its `protected_filed_artifacts` reading in the X60 fragment.

## 9. Limits

- A receipt binds the bytes it was taken against. Every number above carries its
  digest or its command; a number without one is not a measurement. **The tree
  moved during this audit** (§1) — a re-run must re-take the digests.
- `L6b` measures that *no delivered gate* reads a law field. It does not prove no
  gate *could* — a future leg could; that is the enforcement leg's job and it is
  unowned, not impossible.
- `L9` measures the assembler as it stands at the recorded digest. The contract
  declaration was added mid-audit; a later assembler edit could close it, and the
  instrument re-reads the live source on every run.
- NON-CANON engineering evidence. No source-freshness certification, real-world
  rights clearance, lore acceptance or promotion is claimed.

## 10. Reproduce

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/x59-register-law-negatives.py --controls   # 8/8 caught
python3 -B reports/round-27/audit/x59-register-law-negatives.py              # 2 HOLDs
python3 -B reports/round-27/audit/x59-register-law-negatives.py --json       # receipt
sha256sum examples/culture-d4/packet.d4.yml tools/gates/argot-derivation-gate.py
python3 -c "… ruby -ryaml … print([r['id'] for r in packet['register_law']])"  # RGL-01..05
grep -c 'register_law' tools/assemble-culture-d4.py                          # 0
```

Receipts (scratch, gitignored): `.scratch/x59/controls.txt`,
`.scratch/x59/packet.json`; the two clone-based A/B controls under
`.scratch/x59/wire*/`.
