# R18-D17 — reviewer 1/4: the D4 hold set re-derived by hand

- round: 18 (operator: loop 2 of 3, build round 2 of 4; 64 workers,
  `opencode-go-2/deepseek-v4.1-flash`; `reports/round-18/claims.json`), lane
  `kotodama-shokunin`, claim **D**.
- assignment (verbatim): "D R18-D17..D20 (reviewers x4): hold-set hand
  re-derivation; circularity (did the re-pin bless its own change?); cross-check
  vs D2/D3 lessons; SKILL/capability-row drafts; reports/round-18/d4/review-{1..4}.md."
- date: 2026-10-18, stamps UTC. Evidence window 10:19:20Z–10:27:30Z. Reference
  revision HEAD `c66ac3c951b346a2a56f9386e3324b4f5fe33902` (round-18 declare,
  07:17:35 -0300); baseline `3dd3754207032cb81f5fb3e202fe85cf79211339`.
- canon: NON-CANON engineering review. Nothing here is a canon record, a lore
  handoff, a clearance, or a rights/attribution ruling.
- writes: **this file only**, plus gitignored scratch under `.scratch/r18d/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  packet, projection, expected file, tool, or earlier-round byte is edited by
  this seat. No commit, no push.

## 0. Verdict

**The D4 hold set re-derived by hand from the delivered bytes is a
six-obligation set — one owed garment form per costume — and zero rank
obligations. The landed `examples/culture-d4/expected-holds.json` carries 15
holds + 1 note; four of those rows (3 holds + 1 note) name records whose
identifiers occur zero times in the D4 packet, and all 16 rows are the
projector's own output verbatim (proved in review-2 §2).**

Read together: "gate findings exactly equal the D4 expected hold set" is
currently a true statement about **two artifacts that agree by construction**,
and an unproven statement about **the D4 drill's named design debt**. The
pre-implementation locus that exists in the delivered tree — component
`examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration`
with acceptance criterion A-07 ("the typed pipeline's finding set equals
contract.hold_set_declaration exactly (six holds, zero notes, zero fails)",
`01-brief.yml:222`) — says six holds, zero notes, zero fails. The landed file
says fifteen holds, one note. No artifact I can find in the tree dispositions
that delta.

The claim-D equality leg is therefore **not yet acceptable as evidence for the
hold set being right** (see review-2 for the circularity analysis and review-3
for the lesson-by-lesson map). It may still be acceptable as a *regression*
pin, which is a different and weaker claim, and the reviewers of the O claim
should be asked which of the two the round is asserting.

## 1. Method — rules stated before measurement

The rules below were written down before the counts were computed, and are
derivable from the packet alone; the projector's classification code was not
used to decide any of them. Script: `.scratch/r18d/hand-derive.py` (scratch,
read-only over the tree).

| rule | statement (from delivered bytes) |
|---|---|
| **R1** owed-form obligation | a costume whose `form_slot` names `LEX-GAR-nn` and for which the packet supplies no surface form for that slot owes exactly one form. The form's absence is decidable from the packet: the slot id appears in no lexicon record and no `term` equals the garment string. |
| **R2** the slot-side view | the packet's own top-level `form_slots` block (`packet.d4.yml:2124`, supplied by `09-costumes.yml:124`) declares each slot `status: unfilled` with a `kind_owed` — the same obligation seen from the slot side, not a second obligation. |
| **R3** rank obligation | a rank finding is D4's only if the records it names exist in the D4 packet. The D4 packet declares its rank rules as `RK-01..RK-04` (`packet.d4.yml:1705`). |

Commands (cwd = lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18T10:19–10:24Z):

```sh
python3 .scratch/r18d/hand-derive.py
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json
```

## 2. Result

| derivation | observed |
|---|---|
| R1: costumes with an owed `LEX-GAR-nn` slot | **6** — `GAR-01..GAR-06`, each pointing at `LEX-GAR-01..LEX-GAR-06` |
| R2: `form_slots` rows with `status: unfilled` | **6** — the same six slots, `owner` = the six costumes, `kind_owed` = `native-form` ×5 and `borrowed-strata` ×1 (`LEX-GAR-06`, the market-day coat) |
| R3: occurrences of the emitted rank rows' records in the D4 packet | `WR-02` 0, `WR-09` 0, `WR-08` 0, `TR-04` 0, `TR-06` 0, `SR-01` 0 — **all zero** |
| R3: D4's own rank rule ids | `RK-01, RK-02, RK-03, RK-04` |
| **hand-derived D4 obligation count** | **6** (one per owed garment form); **0** rank obligations derivable from the D4 packet |

The projector's own run over the same packet
(`--packet examples/culture-d4/packet.d4.yml --json`, 10:20Z) emits 16
findings: 6 `D2L-FORM-UNRESOLVED` keyed at the costume ids `GAR-0x`, 6 keyed at
the slot ids `LEX-GAR-0x` (the R1 and R2 views of the same six obligations),
and 4 rows that are D2's hardcoded rank block (3 holds + 1 note,
`tools/d2-typed-labels.py:1042-1190`; the projector contains no D4 rank
adaptation — `grep -c REGISTER tools/d2-typed-labels.py` → 0).

## 3. The four sets in play, and what each is

| set | source (all delivered) | count | relation to the D4 packet |
|---|---|---|---|
| **A — pre-declared** | `01-brief.yml` `contract.hold_set_declaration` + A-07, named 2026-10-18 before packet implementation | 6 holds (`D4L-*` @ `GAR-01..06`), 0 notes, 0 fails | one row per owed form, keyed at the costume id |
| **B — round-17 frozen fragment** | `reports/round-17/d4/expected-holds.fragment.json`, amendment A-19-1 | 17 holds + 1 note | **zero overlap** with the delivered packet's ids (`GD-*`, `AL-*#plain`, `RG-*`, `SM-03`; intersection with the landed file = 0 — measured) — a design-fork culture, not this one |
| **C — live emission** | `tools/d2-typed-labels.py --packet … --json` | 15 holds + 1 note | 12 rows = the six R1/R2 obligations double-keyed; 4 rows = D2 constants naming records absent from D4 |
| **D — landed expected file** | `examples/culture-d4/expected-holds.json` (07:24:35 -0300, 2850 bytes) | 15 holds + 1 note | equals **C** exactly, tuple for tuple including `detail` strings (0 only-expected / 0 only-emitted; pins verify) |

The round-18 claim text says "findings exactly equal the D4 expected hold set
(15 holds + the declared note set)". That number is set **C/D**. It is reachable
only by adopting four rows about records the D4 packet does not contain.

## 4. What "exactly" can mean here — the two readings the parent must separate

1. **Set equality against artifact C/D** — "the pipeline emits what the
   committed D4 baseline says". This is a *regression pin*: it detects drift in
   the pipeline, and it is silent about whether the baseline is the right
   answer for the drill. It is what the round can currently prove.
2. **Debt equality against artifact A** — "the pipeline's findings are the
   drill's named design debt". This is what the D3 precedent demands
   (`examples/culture-d3/expected.json` `declared_expectation`: "fixed before
   tool implementation … not generated from a printed verdict") and what A-07
   restates for D4. It is **not** established: A says 6/0/0, C/D say 15/1/0.

The double-keying of the six obligations is a *view* question, not a defect by
itself: the projector emits one row per costume record and one per slot record,
and both are traceable to delivered bytes. The rank block is different in kind:
its `where` values name records that exist only in D2's component tree, its
`detail` strings ("act-collision: genuine-priority-gap") are D2's conflict
determinations, and the 4 rows appear for *any* packet handed to the projector.
A hold set that includes them is red for a reason that has nothing to do with
the D4 drill.

## 5. The one reconciliation the parent should require before admitting D

Exactly one of the following, filed as a new record (append-only; the
round-17 fragment is never edited):

- **(a) Re-scope the baseline to the named debt.** The D4 expected file is
  re-derived to the A-07 six-hold set, and the generalized gate's D4 leg pins
  *that* set; the engine's extra rows (the six `LEX-GAR-*` slot-keyed rows and
  the four D2 rank rows) are then classified by a *declared rule* in the round's
  design record — which of them are legitimate per-packet views, which are
  passenger findings to be excluded from the D4 equality leg — and the rule is
  what the gate implements. The claim's "15 holds" text is corrected to the
  measured set either way.
- **(b) Re-declare the debt.** A supersession record names the 15-hold + 1-note
  set as the D4 drill's debt with each delta from A dispositioned explicitly:
  the twelve label rows (naming the double-key), the three rank holds and the
  note (naming the D2 provenance, the `0`-occurrence measurement, and *why*
  they are adopted as D4 debt rather than excluded). Component `01-brief.yml`
  is not edited; A-07's supersession is recorded by pointer.

Either record must be checkable by a reader who does not run the projector —
that is the whole point of separating the pre-registration from the tool.
Without one of them, the admission decision rests on an artifact that agrees
with its own checker by construction (review-2).

## 6. Limits

- This review re-derives and compares; it does not re-verify the packets,
  the projection or the gate (sibling seats own those legs). The generalization
  named by claim O had **not landed** at my last stamp (10:27:30Z; gate
  `tools/gates/typed-pipeline-gate.py` still sha `d102fd1d…`, size 28604,
  mtime 2026-10-17 19:26:49 -0300), so no post-change D4-path measurement could
  be made here; review-3 lists the tests to run when it lands.
- The hand derivation covers the hold *classes* the delivered pipeline can
  express. Classes the D4 design docs named but no engine carries (register
  doublets, borrow-ledger holds) are not re-derived here; their absence from
  the landed file is a design-fork fact, not a claim of mine.
- NON-CANON throughout; canon status and any real-world claim are out of
  province (`PROVINCE.md`).

## 7. Addendum — reconciliation landed; post-change re-measurement (10:24–10:33Z)

After §1–§6 were written, two things changed inside the window. This section is
the correction and the current reading.

1. **The reconciliation record exists.**
   `reports/round-18/d4/holds.md` (R18-D01/D02; landed 10:24:55Z, the expected
   file at 10:24:35Z) dispositions every delta §5 asked for: the round-17 union
   row by row (§3), the delivered declaration delta by delta (§4 — the +6
   `GAR-0n` rows carry the same keys and class; the +6 `LEX-GAR-0n` rows are the
   `form_slots` block's second naming of the same six slots; the +3 rank holds
   and +1 note are D2's packet-independent constant block), and it routes the
   A-07 boundary to the parent (§7.3) rather than absorbing it. My §0 phrase
   "no artifact I can find in the tree dispositions that delta" is superseded by
   this file. What remains is the **parent decision** — supersede A-07 by
   pointer or have the owner re-declare the component — and that decision is now
   the only thing standing between the delivered artifacts and a coherent D4
   debt statement.
2. **I re-measured the reconciliation's key claims independently** and they
   hold: the 12 label rows are the six obligations seen twice (my R1/R2: six
   costumes → six slots, the slot block declaring the same six; two views →
   twelve rows); the three rank holds and the note name records with **0**
   occurrences in the D4 packet; the expected file equals the emission on the
   4-tuple key. Their §4.3 sentence — "the declared '0 notes' cannot hold for
   any packet through this projector" — is exactly the measurement in my §3.
3. **The generalized gate now reaches the D4 family.** At gate sha `7fad95e0…`
   and `7a3bb816…` (10:31–10:33Z) the D4 run prints `ok L1-assembler` and
   `ok L1-expected-holds` — the declared-family identity leg resolves
   `tools/assemble-culture-d4.py` through the filename convention, and the
   declared expected file loads and self-consistently parses — then stops at
   `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` (exit 2). The
   D4 L3 equality discussed in §4 had no execution at this stamp; the adapter
   (and `examples/culture-d4/packet.d4.typed.yml`) is the remaining piece
   (review-3 §2 L-D7, review-4 §0). The default D2 path stayed byte-identical
   through all five gate revisions measured (`15cdfbda…` default,
   `9a69985a…` frozen row).
4. The §5 ask therefore narrows: not "produce a disposition" (done, in
   `holds.md`) but "record the parent's A-07 decision and land the missing
   adapter piece — or declare its absence as an explicit limit of claim D".
   The hand derivation itself (§2–§4) stands unchanged.
