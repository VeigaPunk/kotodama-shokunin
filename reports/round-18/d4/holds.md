# R18-D01/D02 — the D4 emitted hold set: derivation and reconciliation

- **Round:** 18 (operator loop 2 of 3, build 2 of 4; `reports/round-18/claims.json`),
  claim **D** (`depth`), shards **D01** (extraction) and **D02** (reconciliation).
- **Assignment (verbatim):** "D R18-D01..D02 (holds derivation): extract D4's
  emitted hold set from `tools/d2-typed-labels.py --packet
  examples/culture-d4/packet.d4.yml` output; reconcile against the round-17
  design-doc union; write `examples/culture-d4/expected-holds.json` (ids +
  where-keys + severities); `reports/round-18/d4/holds.md`."
- **Date:** 2026-10-18 (stamps UTC). Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  baseline revision `3dd3754207032cb81f5fb3e202fe85cf79211339` (round-18 declare).
- **Writes:** `examples/culture-d4/expected-holds.json` (new file, landed) and this
  file; gitignored scratch under `.scratch/r18d01/` only (`export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command). No tool, packet, component, projection,
  round-17 design byte or earlier-round byte is edited. No commit, no push.
- **Canon:** NON-CANON engineering evidence. Not a canon record, not a lore
  handoff, not a clearance; no real-language, rights, or authenticity claim is
  made or implied anywhere.

## 0. Verdict

**The D4 hold set is extracted, committed, and reconciled; every pre-declared
delta is dispositioned below.**

- The delivered packet projects: `74 labels / 15 holds / 1 note / 0 fails`
  (`stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}`), exit 1.
- `examples/culture-d4/expected-holds.json` lands **derived, never copied** —
  2850 bytes, sha256 `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98`,
  built by `.scratch/r18d01/derive-holds.py` from two byte-identical projector
  runs (run digest `991b8d310ced1fd1d767340b56d6bde464e59897e868a06c1876f52a43d47cfa`).
- Two independent equality checks pass (§6): an inline replication of the D2
  gate's L3 comparison over the D4 file (12/12), and the D4 projection-check
  gate (exit 0).
- The default D2 gate path is untouched and green at its round-17 sha (§6).
- The reconciliation covers **three** pre-declared sets, not one: the round-17
  design-doc union (17 holds + 1 note, §3), the delivered tree's own
  `01-brief.yml` declaration (6 holds / 0 notes / 0 fails, §4), and the emitted
  set (§2). Deltas: 6 union rows keyed to records the delivered tree does not
  carry, 11 union rows with no delivered trigger and no engine path, and a
  +9 hold / +1 note delta against the delivered declaration.

## 1. Commands, exits, and pins (all 2026-10-18, lane root, `TMPDIR=$PWD/.scratch`)

| command | exit | observed |
|---|---:|---|
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` (×2) | 1 | 16 findings; the two runs `cmp` identical (`991b8d31…`) |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit .scratch/r18d01/emit.yml` | 1 | writes the deterministic projection |
| `cmp .scratch/r18d01/emit.yml examples/culture-d4/typed-labels.d4.yml` | 0 | identical — the committed projection is the projector's own output (`a59990bb…`) |
| `python3 tools/d2-typed-labels.py --packet … --check examples/culture-d4/typed-labels.d4.yml` | 0 | `byte-identical deterministic projection` |
| `python3 tools/gates/d4-typed-labels-check-gate.py` | 0 | same line through the round-18 thin gate (sibling file, read-only use) |
| `python3 tools/assemble-culture-d4.py --check` | 0 | `packet.d4.yml: byte-identical deterministic assembly` |
| `python3 .scratch/r18d01/derive-holds.py --write` | 0 | lands the expected file (§0) |
| `python3 .scratch/r18d01/verify-holds.py` | 0 | 12/12 checks (§6) |
| `python3 tools/d2-typed-labels.py --selftest` | 0 | 39/39 |
| `python3 tools/gates/typed-pipeline-gate.py` | 0 | `summary: 16/16 legs passed`, stdout sha `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | 12/12 |

| path | sha256 | note |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | 82859 bytes; equals the blob at `3dd3754` (`git show 3dd3754:examples/culture-d4/packet.d4.yml \| sha256sum`) |
| `examples/culture-d4/typed-labels.d4.yml` | `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d` | likewise committed at `3dd3754` |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | the projector, unchanged since the round-11 freeze |
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` | as-read; equals the round-11 `run-receipt.json` pin and `reports/round-18/d4/interop-1.md` §2 |

**The round-17 blocker is gone at this revision.** `tools/d2-typed-labels.py` no
longer refuses the D4 packet: `packet.d4.yml:1789-1793` declares `eras` as the
tag list `["E0","E1","E2","E3"]` (records under `era_records:` `:1794` /
`named_eras:` `:1915`), where the 09:49Z round-17 revision carried records and
the projector exited 2 (`reports/round-17/d4/typed-run.md` §4). `ASSEMBLY.md:69-75`
still lists `typed-labels.d4.yml`, `packet.d4.typed.yml` and
`expected-holds.json` as pending and `tools/d2-typed-labels.py` as "not a
substitute" — that paragraph is superseded by the delivered bytes; `ASSEMBLY.md`
is a filed round-17 artifact and is not edited here (routed in §7).

## 2. The emitted set (= the content of `expected-holds.json`)

Counts `{"hold": 15, "note": 1, "fail": 0}`; coverage from the projection:
74 labels — `native-form` 56, `translated-label` 12, `borrowed-strata` 6.

| severity | id | where | detail |
|---|---|---|---|
| hold | `D2L-FORM-UNRESOLVED` | `GAR-01` | `label_id LEX-GAR-01 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `GAR-02` | `label_id LEX-GAR-02 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `GAR-03` | `label_id LEX-GAR-03 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `GAR-04` | `label_id LEX-GAR-04 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `GAR-05` | `label_id LEX-GAR-05 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `GAR-06` | `label_id LEX-GAR-06 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `LEX-GAR-01` | `label_id LEX-GAR-01 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `LEX-GAR-02` | `label_id LEX-GAR-02 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `LEX-GAR-03` | `label_id LEX-GAR-03 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `LEX-GAR-04` | `label_id LEX-GAR-04 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `LEX-GAR-05` | `label_id LEX-GAR-05 has no supplied native/borrowed form` |
| hold | `D2L-FORM-UNRESOLVED` | `LEX-GAR-06` | `label_id LEX-GAR-06 has no supplied native/borrowed form` |
| hold | `D2L-RANK` | `TR-04#a\|TR-06#a` | `act-collision: genuine-priority-gap` |
| hold | `D2L-RANK` | `WR-02#g\|WR-09#g` | `R-05-class: genuine-priority-gap` |
| hold | `D2L-RANK` | `WR-08#g\|WR-09#g` | `R-05-class: genuine-priority-gap` |
| note | `D2L-RANK` | `SR-01#a\|SR-01#b` | `act-collision: band-keyed-pair` |

The 12 form rows are one hold per owed slot, keyed twice: once at the garment
record id (`where: GAR-0n`) and once at the owed slot's own projected record
(`where: LEX-GAR-0n`). Emitted at `tools/d2-typed-labels.py:793` (hold for a
`translated-label` whose `label_id` is not supplied); the `LEX-GAR-0n` labels
exist because `project_labels` projects every `form_slots` entry as a label
(`tools/d2-typed-labels.py:622`, `_form_slot_label(slot, "11-costumes", slot["id"])`).

## 3. Reconciliation A — the round-17 design-doc union (17 holds + 1 note)

Union sources (read-only; all NON-CANON round-17 design bytes):

| path | sha256 | what it names |
|---|---|---|
| `reports/round-17/d4/design-brief.md` §7.1 (`:385-411`) | `a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f` | the candidate set: 18 holds / 1 note pre-amendment |
| `reports/round-17/d4/typed-support-2.md` §3-§4 (`:80-88`, `:113-121`, `:123-158`) | `02c31c5bd924c6dddfa469fcaa1029c724d95e42f9dafda7ca279b7c75eafbbe` | the freezing, amendment A-19-1, and the naming rule |
| `reports/round-17/d4/expected-holds.fragment.json` | `ee0908e108b22feafb014da40851db34c421a5ae91a3e37ff2791d45a266686a` | the frozen union: `{hold: 17, note: 1, fail: 0}` |

| union row(s) | named proving leg | delivered-tree measurement | disposition |
|---|---|---|---|
| 6× `D4L-FORM-UNRESOLVED` @ `GD-01`..`GD-06` | channel leg (L2) | `grep -c "GD-" examples/culture-d4/packet.d4.yml` → **0**; same sweep over `components/` → 0 | **class present, keys superseded** — the delivered owed-slot records are `GAR-01..06` + `LEX-GAR-01..06`; the emitted 12 `D2L-FORM-UNRESOLVED` rows are this class |
| 6× `D4L-REGISTER-UNRESOLVED` @ `AL-01#plain`..`AL-06#plain` | channel leg (L2) | `grep -c "AL-01#plain"` packet → **0**; `AL-` in the delivered tree is the **allophony** namespace (`01-brief.yml:170`, `02-phonology`; the assembler records `allophony` as a non-packet key); `grep -c "REGISTER" tools/d2-typed-labels.py` → **0** | **unprovable, not in the file** — no engine path; freeze rule 2 (brief §7.2, `design-brief.md:412-426`) excludes a row the gate cannot prove |
| 1× `D4L-BORROW` @ `AL-03` | borrow check | engine path exists (`tools/d2-typed-labels.py:707-709`, donor separation); the delivered ledgers are complete (packet carries 15 `donor_form`/`substitutions` lines; 6 `borrowed-strata` labels; 0 borrow findings) | **trigger absent** — no delivered borrow deficit to hold |
| 1× `D4L-ERA` @ `RG-02` | era check | `RG-02` in the delivered tree is a **contract rule** (`01-brief.yml:188`); era reconciliation over the delivered packet: `findings []`, 6/6 records `R-ERA-IN-SCOPE` | **trigger absent; namespace collision** — no register-emergence concept delivered |
| 2× `D4L-RANK` @ `RG-05#a\|RG-07#a`, `RG-06#a\|RG-09#a` | rank leg | `RG-09` → **0** hits; `RG-05`..`RG-08` are the delivered contract rules (`01-brief.yml:191-194`); the emitted rank rows are D2's constant block (§5) | **unprovable** — no register-law rank adapter; the union's two rows are not the emitted three |
| 1× `D4L-MATERIAL` @ `SM-03` | material coverage | `grep -c "SM-"` packet → **0**; `grep -c "sealed" tools/d2-typed-labels.py` → **0**; material leg over the delivered packet: 6/6 `R-MAT-RESOLVED`, 0 findings | **unprovable, no delivered record** |
| note `D4L-RANK` @ `RG-08#a\|RG-08#b` | rank leg | `RG-08` is a delivered contract rule; the emitted note is `D2L-RANK` @ `SR-01#a\|SR-01#b` (D2 constant row) | **superseded** — same class (band-keyed pair), different key |
| union row 8 `D4L-NATIVE` @ `QN-01` | native-form check | dropped pre-implementation by amendment A-19-1 (`typed-support-2.md:135-160`); `grep -c "QN-"` packet → **0** | **consistent, no delta** |

Arithmetic: 17 union holds = 6 rows whose class is carried by the emitted 12
(superseded keys) + 11 rows with no delivered trigger (6 register + 1 borrow +
1 era + 2 rank + 1 material). The union's note is replaced by the emitted note.

## 4. Reconciliation B — the delivered tree's own declaration (6 holds / 0 notes / 0 fails)

`examples/culture-d4/components/01-brief.yml` (`a2bc3111b8e936d2aa78feca86b871996455cc98d7d639f3825a88df8a1c056f`)
`contract.hold_set_declaration` (`:195-208`, counts `:205`, acceptance criterion
A-07 `:224`) names **6 holds, 0 notes, 0 fails** — `D4L-FORM-UNRESOLVED` @
`GAR-01`..`GAR-06` — and `:215` binds: "A finding set other than this six-hold
set is a mismatch to report, not to absorb." The declaration is echoed by
`brief.md:44-50` and `ASSEMBLY.md:59-68`, and travels into the packet at
`packet.d4.yml:121-151`.

Delta against the emitted set (15 holds / 1 note):

1. **+6 holds @ `GAR-01..06`** — the declared six where-keys are exactly the
   emitted six `GAR-0n` rows; only the id spelling differs (declared
   `D4L-FORM-UNRESOLVED`, emitted `D2L-FORM-UNRESOLVED`). Resolved by the
   pre-declared naming rule in `typed-support-2.md:80-88` ("The expected file
   must carry **exactly the ids the delivered D4 projector emits** … The
   contract is the equality, not the spelling"), so the file carries `D2L-*`.
2. **+6 holds @ `LEX-GAR-01..06`** — the packet carries a second naming of the
   same six slots: `form_slots:` at `packet.d4.yml:2124` (component
   `09-costumes.yml:124-131`, packet key declared at `:15`). The projector
   projects each slot as a label (`tools/d2-typed-labels.py:622`) and each owed
   slot then emits its own hold at `:793`. The declaration counted one hold per
   garment record; the delivered packet names the slots again in their own
   block.
3. **+3 rank holds and +1 note** — the rank leg emits D2's constant rows for any
   packet. Re-measured on the delivered D4 projection: every `rank_rules` record
   cites `examples/culture-d2/components/12-rank-rules.yml:318-329`, and the era
   alias rows are `12-rank-rules era_aliases.era-1..3` — D2 component data. So
   the declared "0 notes" cannot hold for any packet through this projector.

Disposition: `expected-holds.json` carries the **emitted** set (the gate's
equality target; claim D's "15 holds + the declared note set"). The declaration
is a filed round-17 byte: **reported, not absorbed, not edited** — amending it is
a component edit by its owner (a re-declare, never an in-place edit), and A-07
as written is a boundary the parent decides (§7).

## 5. What the equality now carries (reported, not absorbed)

- **Rank rows are D2's.** `D2L-RANK` @ `WR-02#g|WR-09#g`, `WR-08#g|WR-09#g`,
  `TR-04#a|TR-06#a` (holds) and `SR-01#a|SR-01#b` (note) come from D2's constant
  block and cite D2's component; they are packet-independent.
- **Era alias rows are D2's** (`12-rank-rules era_aliases`, D2's
  `11-costumes` rows) — the era legs add no D4 findings, they inherit D2's
  reconciliation bookkeeping.
- **The projector is D2's** (`tools/d2-typed-labels.py`, sha `0da0015f…`), the
  decision carried from round 17 (`reports/round-17/d4/typed-support-1.md:386-393`,
  F-D18-7). The D4 expected file therefore carries the `D2L-*` vocabulary; if
  the lane later writes `tools/d4-typed-labels.py`, this file must be
  re-derived and re-pinned as a **new row/file**, never edited in place.

## 6. Verification (what was run, and its result)

- **Derivation determinism.** Two `--json` runs `cmp` identical
  (`991b8d31…`); the derivative script refuses to write if they differ.
- **Independent equality check** (`.scratch/r18d01/verify-holds.py`, 12/12):
  replicates the D2 gate's L3 comparison verbatim
  (`tools/gates/typed-pipeline-gate.py:305-333`) with `expected_path` pointed at
  the D4 file — `L3-holds` (both directions), `L3-notes`, `L3-fails` empty,
  `L3-counts` `{15,1,0}`, `L3-baseline` set equality, `L3-details` (all 16 detail
  strings), no extra/missing/severity swap, and all three pins re-derived from
  the delivered bytes.
- **Projection identity.** `cmp` of a fresh `--emit` against the committed
  `typed-labels.d4.yml` → identical; `--check` (with `--packet`) exit 0;
  `tools/gates/d4-typed-labels-check-gate.py` exit 0.
- **Assembler identity.** `tools/assemble-culture-d4.py --check` exit 0 — the
  packet the holds are keyed to is the assembler's own deterministic build.
- **Default D2 path regression-proved** (gate sha `d102fd1d…`, unchanged):
  projector `--selftest` 39/39; D2 gate live run exit 0, `16/16 legs passed`,
  stdout `15cdfbda…` — the same digest independently measured by the sibling
  interop seat (`reports/round-18/d4/interop-1.md:33`); gate `--selftest`
  12/12.
- **Hygiene.** No filed byte moved: `git status --porcelain` shows only new
  untracked files this round (this worker's: `examples/culture-d4/expected-holds.json`;
  scratch is gitignored). `3dd3754`'s committed packet/projection blobs equal the
  working-tree bytes used here.

## 7. Limits and what the parent must route

1. **Pins are three, not five.** The file carries `packet_sha256`,
   `projection_sha256`, `projector_sha256` (the committed D2 schema's key set).
   No `adapter_sha256` / assembler pin: `tools/assemble-d4-typed.py` and
   `examples/culture-d4/packet.d4.typed.yml` do not exist ("not landed",
   `ASSEMBLY.md:69-75`), so nothing can be pinned. The assembler identity lives
   on the O-side gate leg (declared assembler pin), not in this file.
2. **Any packet revision voids the pins.** Re-run
   `python3 .scratch/r18d01/derive-holds.py --write` after an assembler/component
   edit and land the result as this round's record; the round-17 fragment's
   discipline ("derived, never copied") is carried forward.
3. **The delivered declaration under-declares** (§4): `01-brief.yml`
   `hold_set_declaration` (6/0/0) and its A-07 cannot pass through this
   projector (emitted 15/1/0). Either the owner re-declares (a component edit +
   reassembly, a new round's bytes) or A-07 is superseded by this file — the
   parent's decision; nothing is absorbed here.
4. **`ASSEMBLY.md` §4's "Pending" paragraph is superseded** by the delivered
   bytes and this landing; it is a filed round-17 byte, so it is routed, not
   edited.
5. This file reports a derivation, not a gate verdict: whether the generalized
   D4 gate reproduces this set, and whether the round-18 frozen manifest replays
   green, are the sibling D/O seats' legs (`reports/round-18/claims.json` claim
   D's `after_required`).
6. NON-CANON throughout; hold counts are design debt, never a clearance.
