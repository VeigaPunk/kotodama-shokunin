# R18-D27 — disposition drafts: the four D4 hold-set namings and the emitted set

- round: 18 (operator loop 2 of 3, build round 2 of 4) · seat **R18-D27**
  (disposition drafts) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D21..D28 (scribes+docs x8): frozen-manifest
  records; fragment ledger; capability drafts; ASSEMBLY.md/README updates for
  culture-d4 (new files only); docs; run logs; disposition drafts; spot-check
  ledger. reports/round-18/d4/scribe-{1..8}.md."
- date: 2026-10-18 · reference revision `c66ac3c` · readings 10:20–10:31Z.
- canon: NON-CANON. Disposition **drafts** for the parent; this seat decides
  nothing, edits no component, and blesses no re-declaration.
- writes: **this file only** + `.scratch/r18d21/`. No commit, no push.
- relation to siblings: the D01/D02 fragment `reports/round-18/d4/holds.md`
  owns the extraction and the per-row reconciliation; this file drafts the
  **disposition language** the parent can carry into LOG/SCORECARD, adds one
  independent equality check, and lists the three items that need a
  parent/owner decision rather than an integration note.

## 0. The four namings, side by side

| # | naming | source (read-only, NON-CANON) | holds / notes / fails | relation to the emitted set |
|---|---|---|---|---|
| 1 | design-doc union | `reports/round-17/d4/design-brief.md` §7.1 (18/1/0 pre-amendment) and `typed-support-2.md` amendment A-19-1 → the frozen union `expected-holds.fragment.json` (17/1/0) | 17 / 1 / 0 (`ee0908e1…`) | 6 of its rows share a **class** with the emitted 12 (keys differ: `GD-0n`, `AL-0n#plain`); 11 rows have no delivered trigger; its note is replaced |
| 2 | delivered registry declaration | `components/01-brief.yml:195-208` (`a2bc3111…`), echoed at `brief.md:44-50`, `ASSEMBLY.md:59-68`, travelling in the packet at `packet.d4.yml:121-151` | 6 / 0 / 0 | its six `where` keys are the emitted first six; ids differ; it omits the six `LEX-GAR-*` re-keys, the three rank holds and the note |
| 3 | emitted projection | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` (×2 identical, digest `991b8d31…` per holds.md §6) | 15 / 1 / 0 | **this is the equality target** |
| 4 | landed expected file | `examples/culture-d4/expected-holds.json` (`09490a27…`, 2850 B, landed 10:24:55Z) | 15 / 1 / 0 | set-equal to #3 (below); pins to packet `e7ecd204…`, projection `a59990bb…`, projector `0da0015f…` |

Claim D's wording ("15-hold expected set") matches #3 = #4; the round-16-era
"expected set" idea (#1/#2) is the pre-implementation forecast, and the delta
between forecast and delivery is the matter this file dispositions.

## 1. Independent check performed by this seat (⟦IC⟧, 10:29Z)

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json > .scratch/r18d21/proj-d4.json   # exit 1
# then, keyed (id, severity, where, detail):
#   expected rows 16 / projector rows 16 ; set equality True ; both asymmetries []
#   declared counts {hold: 15, note: 1, fail: 0}
#   pin re-derivation: packet / projection / projector digests all equal live bytes
```

This is an independent re-derivation from the delivered bytes (the D01/D02
fragment built the file with its own script): the file is not merely
self-consistent, it equals a fresh projector run executed by another seat.
No delta to disposition between #3 and #4.

## 2. Disposition drafts (parent-facing language)

**D-D1 — the expected file carries the emitted set, not the forecast.**
`examples/culture-d4/expected-holds.json` names 15 holds + 1 note + 0 fails,
keyed `(id, severity, where)` with per-row `detail`, pinned to the delivered
packet/projection/projector bytes. Draft LOG sentence:
> The D4 expected set was **derived, never copied**, from two byte-identical
> projector runs and reconciled against all pre-declared namings; the landed
> file equals a fresh run measured by an independent seat (16/16 rows, zero
> deltas).

**D-D2 — six forecast rows are "class carried, keys superseded".**
The union's `D4L-FORM-UNRESOLVED` @ `GD-01..06` name the same design class the
emitted 12 `D2L-FORM-UNRESOLVED` rows carry (`GAR-0n` and `LEX-GAR-0n`).
Disposition: **superseded keys, class preserved** — recorded, not repaired;
the `GD-` keys exist in no delivered byte (`grep -c "GD-" packet.d4.yml` → 0,
holds.md §3).

**D-D3 — eleven forecast rows are not carried, each with its named reason.**
Six `D4L-REGISTER-UNRESOLVED` (`AL-0n#plain`) → unprovable (no engine path;
`AL-` is the delivered allophony namespace); one `D4L-BORROW` → trigger absent
(borrow ledgers complete); one `D4L-ERA` @ `RG-02` → trigger absent +
namespace collision (`RG-02` is a delivered contract rule); two `D4L-RANK` →
unprovable (no register-law rank adapter; the emitted rank rows are D2's
constant block); one `D4L-MATERIAL` @ `SM-03` → unprovable (no `SM-` record;
material leg clean 6/6). Draft LOG sentence:
> The forecast's eleven rows without a delivered trigger are reported as
> **unprovable/absent**, not absorbed into the gate and not silently dropped:
> the gate may hold only what it can prove.

**D-D4 — the union's note is replaced, not laundered.**
Forecast note `D4L-RANK` @ `RG-08#a|RG-08#b` → the emitted note is
`D2L-RANK` @ `SR-01#a|SR-01#b` (same class: band-keyed pair; D2 constant row).
Disposition: **superseded key**; the note count stays 1 — a hold was never
moved into the note set.

**D-D5 — the declaration's arithmetic is under-specified, not wrong-headed.**
The delivered registry's 6/0/0 counts one hold per owed garment slot; the
projector keys the same six slots twice (record id and slot-label id) and emits
D2's constant rank rows for any packet. Disposition: **the file follows the
emitted set; the declaration is a filed round-17 byte of its owner** — a
re-declare is an owner act, never a scribe edit.

**D-D6 — the vocabulary is the projector's.** The expected file carries
`D2L-*` ids because the delivered projector is `tools/d2-typed-labels.py`
(`0da0015f…`, unchanged since the round-11 freeze) and the pre-declared naming
rule (`typed-support-2.md:80-88`) fixes ids to what the projector emits. Draft
LOG sentence:
> The D4 hold ids inherit the D2 projector's vocabulary by the pre-declared
> rule; a future `tools/d4-typed-labels.py` would require re-deriving and
> re-pinning the expected file as a **new** file/row.

**D-D7 — rank rows are packet-independent.** The three `D2L-RANK` holds and the
note cite D2 component data (`12-rank-rules.yml:318-329`, `era_aliases`); they
are D2's bookkeeping surfacing in every packet's projection, including D4.
Disposition: **carried as emitted, annotated in the docs** (scribe-5 draft),
never deleted to make the D4 set look D4-specific.

## 3. Items needing a decision (not an integration note)

1. **A-07 vs the emitted set.** `01-brief.yml:224` binds the registry's
   acceptance criterion to the six-hold set ("a finding set other than this
   six-hold set is a mismatch to report, not to absorb"). The landed file
   carries fifteen. The parent (with the component's owner) decides whether
   A-07 is read as "the six rows must appear" or is amended by a re-declare —
   this seat reports the divergence, per the round-17 lesson.
2. **Registry/`SCORECARD` rows for two unregistered gates.** The two new
   `tools/gates/d4-*.py` have no `SKILL.md` §Gates row and no frozen row
   (scribe-5 F-D25-1). Landing them without either leaves the two-evidences
   clause unsatisfied.
3. **The round-18 frozen generation's contents.** Which surfaces it pins (D4
   typed row + wrapper rows ± legacy D4 rows over live bytes) is an integration
   decision; scribe-1 §5 proposes the minimum set and the append-only rule.

## 4. What these dispositions are not

- Not an admission: the equality is a gate result over NON-CANON bytes; holds
  remain open design debt; no clearance, authenticity or canon claim follows.
- Not a repair of any round-17 byte: every disposition above is a record; the
  forecast file, the declaration, the design docs and the round-17 frozen copy
  all stay byte-stable.
- Not a re-freeze: pinning a new expected set into a frozen generation is the
  parent's act, on the settled tree.

## 5. Receipts

| item | value |
|---|---|
| expected file | `examples/culture-d4/expected-holds.json`, `09490a2756d123eb…`, 2850 B, landed 10:24:55Z (poll T2) |
| projector run receipt | `.scratch/r18d21/proj-d4.json` (this seat), digest `991b8d31…` per D01/D02 |
| equality reading | 16/16 rows, zero asymmetric rows, counts `{15,1,0}`, pins == live (10:29Z) |
| union fragment | `reports/round-17/d4/expected-holds.fragment.json` `ee0908e108b22fea…` (per holds.md §3) |
| declaration | `components/01-brief.yml` `a2bc3111b8e936d2…`, `:195-208`, `:224` |

## 6. Post-state note (10:31Z)

The D01/D02 fragment `reports/round-18/d4/holds.md` landed at 10:26Z and
carries the extraction and the per-row reconciliation this file drafts
dispositions for. Alignment check made by this seat: its §2 emitted table, its
§3 union dispositions (6 class-carried + 11 unprovable/absent + 1 replaced
note) and its §4 declaration delta (+6 `GAR` re-keys, +6 `LEX-GAR` re-keys,
+3 rank holds, +1 note) agree with the drafts in §2 above; the three
decision items in §3 (A-07 reading, unregistered gates, generation contents)
are unchanged by its landing.

One addition from the post-state readings: the generalized gate now accepts
the D4 packet to `ok L1-assembler` / `ok L1-expected-holds` but fails at
`L1-build: adapter missing: tools/assemble-d4-typed.py` (scribe-6 row 37), so
the equality target the dispositions are keyed to is *defined* but not yet
*graded*. Dispositions D-D1…D-D7 do not depend on the gate revision: they are
keyed to the emitted projection and the landed expected file, both of which
are byte-stable (verified by re-hashing at 10:31Z).
