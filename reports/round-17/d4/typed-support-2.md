# R17-D19 — the D4 hold set: naming, documentation, expected-holds fragment (typed support, seat 2)

- round: 17 (operator loop 2 of 3, build round 1 of 4; 64 declared workers,
  `opencode-go/deepseek-v4.1-flash`) · shard: **D19** (typed support: hold-set
  documentation), claim **D `culture-d4-assembly`**.
- assignment (verbatim): "D4 R17-D18..D19 (typed support): typed-packet derivation
  + hold-set documentation; D4 expected-holds.json fragment;
  reports/round-17/d4/typed-support-{1,2}.md."
- date: 2026-10-18 (stamps local UTC-3; UTC where stated). Reference revision
  `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17 declare); baseline
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit).
- canon: NON-CANON engineering evidence. Nothing here is a canon record, a
  clearance, a handoff or a rights statement.
- writes: **this file** plus `reports/round-17/d4/expected-holds.fragment.json`
  (the named-set freeze record, written 2026-10-18) plus in-lane scratch under
  `.scratch/r17d18/`. No tool, gate, packet, projection, component, baseline or
  earlier-round byte is edited; no commit, no push.
- status: **complete for this seat's scope** — the contract (§1–§3), the named
  hold set with amendment A-19-1 (§4, 17/1/0) and the fragment are written; the
  *delivered* `examples/culture-d4/expected-holds.json` is derived at landing
  from the typed packet (§5), which does not exist yet (dependency record in
  typed-support-1.md §7).
- companion: `reports/round-17/d4/typed-support-1.md` (the derivation contract;
  its §5.2–5.6 rules are the ones this hold set is compared under).

## 0. Verdict

1. **The hold set must be named pre-implementation and pinned exactly.** Claim D
   requires "hold set named pre-implementation in design docs"; the round-17
   counting contract measures it twice — D2 (the typed packet's emitted finding
   set equals the expected file in both directions, key `(id, severity, where)`,
   counts and detail strings pinned) and D8 (the set is named in the design docs
   pre-implementation and matches the expected file)
   (`reports/round-17/scope.md:109` and `:123`).
2. **The D2 analogue is the template**: `examples/culture-d2/expected-holds.json`
   (schema `kotodama-typed-pipeline-holds-v1`), 15 holds + 1 note + 0 fails,
   compared by `tools/gates/typed-pipeline-gate.py` L3 legs
   (`L3-holds`/`L3-notes`/`L3-fails`/`L3-counts`/`L3-details`/`L3-baseline-set`),
   with the gate's internal constant asserted equal to the committed file in both
   directions (`:74-88`).
3. **This seat's deliverable is the D4 fragment** — the named hold set
   (17 holds + 1 note + 0 fails after amendment A-19-1) as a canonical-JSON
   freeze record (`reports/round-17/d4/expected-holds.fragment.json`), plus the
   contract that keeps the fragment, the design's pre-implementation naming, and
   the derived delivered file from drifting apart.

## 1. What the hold set is, and what it is not

- It is the **complete finding set** the D4 typed run emits, at severities
  `hold` and `note`, keyed `(id, severity, where)`, with counts
  `{hold: H, note: N, fail: 0}` and detail strings pinned. In D2 the set is 10
  `D2L-FORM-UNRESOLVED` holds (one per costume gloss with an owed form slot), 2
  `D2L-NATIVE` holds (diacritic-bearing forms held for their owner), 3
  `D2L-RANK` holds, 1 `D2L-RANK` note, 0 fails
  (`examples/culture-d2/expected-holds.json`; re-measured 2026-10-18:
  `python3 tools/d2-typed-labels.py --json` → `stats {fail: 0, hold: 15,
  labels: 58, note: 1}`).
- It is **not** a clearance. Exit 0 means "the emitted findings equal the frozen
  expected set" — every hold is still open design debt; the D2 gate prints a
  banner saying so and the holds verbatim.
- It is **not** the legacy gate output. The legacy run's `PHON-INVENTORY` fails
  are the minus-basis of the channel differential, not members of the set.

## 2. The exactness contract (what "equals" means)

1. Comparison key: the triple `(id, severity, where)` as a **set**
   (order-insensitive); counts `hold`, `note`, `fail` pinned; `detail` strings
   pinned (full finding objects, canonical JSON).
2. Both directions: no extra hold, no missing hold, no severity swap; every
   pinned note present and **never counted as a hold**; fail set empty.
3. A hold downgraded to a note, renamed, deleted, or an unpinned note appearing
   is a mismatch (the D2 design §6 hazard control 3 / the round-17 counting
   contract D2). This is the laundering channel the D4 negatives probe
   (`reports/round-17/tests/neg-*.md`).
4. The set is over the **typed run only** (the D4 typed packet's
   `pipeline_findings` carried verbatim from the D4 projector).

## 3. Naming rules for the D4 instance

- **Class substitution.** The D4 analogue of the D2 `D2L-*` vocabulary is
  `D4L-*` (typed-support-1.md §5.5): `D4L-FORM-UNRESOLVED` for an owed form slot,
  `D4L-NATIVE` for a supplied native form held for its owner, `D4L-RANK` for rank
  conflicts, `D4L-DATA`/`D4L-SCOPE`/`D4L-MATERIAL`/`D4L-BORROW` for their classes.
  The expected file must carry **exactly the ids the delivered D4 projector
  emits** — if the D4 derivation reuses D2's ids verbatim, the expected file
  follows the emitted vocabulary, not this substitution. The contract is the
  equality, not the spelling; the spelling above is this seat's pre-implementation
  proposal.
- **One hold per owed slot.** Every off-channel record with a declared form slot
  and no supplied native/borrowed form carries exactly one hold naming the record
  (D2: `GAR-01..GAR-10` → `LEX-GAR-01..10`). The count of such records is a
  property of the D4 design; the expected file must not contain a hold without a
  matching routed record (the adapter's coverage leg refuses the reverse).
- **The note is pinned separately.** D2's single note (`D2L-RANK` @
  `SR-01#a|SR-01#b`) is a rank-adapter band-keyed pair — it must appear and must
  not be counted as a hold. D4's note set (if any) follows the same rule.
- **Fail set empty.** A fail anywhere in the pipeline finding set is an automatic
  mismatch; a D4 packet that produces a `D4L-DATA` fail is malformed input, not a
  hold set.

## 4. The D4 named hold set (instance) — named pre-implementation in the design brief, documented and frozen here

The D4 design brief names the candidate set before any D4 byte exists
(`reports/round-17/d4/design-brief.md:385-411`, R17-D01, 2026-10-18, sha256
`a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f`,
as-read 06:34; the brief was edited in flight (earlier `091e7aa9…` at 06:31)): **18
holds, 1 note, 0 fails** (brief `:389`). The brief's §7.2 freeze rules are
binding on the hold-set seat (`:412-426`); this section records the set as named,
row by row, with the proving leg each row must be proven by (freeze rule 2), and
the one conditional row (row 8) flagged.

| # | id | severity | count | where | proving leg / trigger (brief §7.1) |
|---|---|---|---|---|---|
| 1 | `D4L-FORM-UNRESOLVED` | hold | 6 | `GD-01`..`GD-06` | gloss-routed goods/measure slots with no supplied sound form (Δ1 class 1; channel leg L2) |
| 2 | `D4L-REGISTER-UNRESOLVED` | hold | 6 | `AL-01#plain`, `AL-02#plain`, `AL-03#plain`, `AL-04#plain`, `AL-05#plain`, `AL-06#plain` | argot loans supplied and checked in the quote slot; the plain doublet is owed (Δ1 class 2; channel leg) |
| 3 | `D4L-BORROW` | hold | 1 | `AL-03` | donor separation incomplete: `ultimate: null` (Δ4; borrow check) |
| 4 | `D4L-ERA` | hold | 1 | `RG-02` | register-emergence declared as a prose span → partial, raw retained (Δ5; era check) |
| 5 | `D4L-RANK` | hold | 2 | `RG-05#a\|RG-07#a`; `RG-06#a\|RG-09#a` | register-law genuine-priority-gaps (Δ6; rank leg) |
| 6 | `D4L-MATERIAL` | hold | 1 | `SM-03` | sealed-measure slot with no resolved route (Δ7; material coverage) |
| 7 | `D4L-RANK` | note | 1 | `RG-08#a\|RG-08#b` | band-keyed pair, reported not held (rank leg) |
| 8 | ~~`D4L-NATIVE`~~ | ~~hold~~ | ~~1~~ | ~~`QN-01`~~ | **dropped by amendment A-19-1** — the trigger is absent in the landed component drafts (see below) |

Counts after amendment A-19-1: **`{hold: 17, note: 1, fail: 0}`** (the brief's
pre-amendment target was 18/1/0, `design-brief.md:389`).

The 17 hold `where` tokens and the note `where`, enumerated individually for the
counting runner's design-doc naming leg (it matches each token separately —
`reports/round-17/run-validation.py:172-173`, `:706-733`; range notation alone
would leave four tokens unnamed, typed-support-1.md F-D18-9):
`GD-01`, `GD-02`, `GD-03`, `GD-04`, `GD-05`, `GD-06`,
`AL-01#plain`, `AL-02#plain`, `AL-03#plain`, `AL-04#plain`, `AL-05#plain`,
`AL-06#plain`, `AL-03`, `RG-02`, `RG-05#a|RG-07#a`, `RG-06#a|RG-09#a`, `SM-03`;
note `RG-08#a|RG-08#b`.

**Amendment A-19-1 (row 8 dropped; recorded, never silent — brief §7.2 rule 1,
`design-brief.md:403-406`).** The brief makes row 8 conditional: it requires
02-phonology to declare a length or diacritic mark *with its own minimal pair*,
and lets the hold-set seat drop the row only by recording the decision that makes
it impossible. The landed component drafts (2026-10-18 06:31-32,
`reports/round-17/d4/components/`) record exactly that decision:

- `02-phonology.yml` `stress_record.minimal_pairs[0]`: "no delivered minimal
  pair contrasts length; length is a design contrast declared here for 04 to
  use, and a later round that delivers a length pair must record it
  (to-verify)" — no minimal pair declares the mark;
- `02-phonology.yml` `accent`: "Vowel length is contrastive only on the stressed
  syllable and is written as a **double vowel** (aa ee ii oo uu)" — an
  in-inventory spelling, so no supplied form can carry an out-of-inventory
  symbol on that account;
- `03-orthography.yml:45`: "length is notated by doubling the vowel in
  romanization and by the long mark in the script; **no diacritics are used, so
  no form carries a symbol outside 02's inventory**" (scheme `D4-roman-1`,
  lowercase ASCII).

With no declared diacritic and no delivered minimal pair, the D2 `L-15`/`L-16`
class has no D4 trigger: a `D4L-NATIVE` hold at `QN-01` is unprovable, and the
brief's freeze rule 2 ("a row the gate cannot prove does not enter the file")
requires the drop. If the delivered components change (a length pair delivered,
or a diacritic mark introduced), row 8 returns by a recorded amendment naming
the component decision — the count moves back to 18/1/0.

**Freeze record (this seat's application of the brief §7.2).**

1. *Named pre-implementation* — the naming source is the design brief dated
   2026-10-18, before any D4 byte existed; this file repeats the ids and `where`s
   so the runner's design-doc naming leg finds them in the brief and in this
   file (`reports/round-17/run-validation.py:706-733`).
2. *Every row names its proving leg* — the table's last column; row 7 is the only
   note and is never counted as a hold; row 8 is dropped because its leg cannot
   prove it (A-19-1).
3. *Row 8's conditionality is resolved by A-19-1* — recorded above with the
   component quotes, never silently.
4. *Severity is not negotiated downward*; the delivered packet carries zero
   fails (freeze rules 3-4).
5. *Any later change* to this set is a recorded amendment naming the component
   decision that forced it (freeze rule 1).

**The delivered file is not this fragment.** `examples/culture-d4/expected-holds.json`
must be *derived* from the delivered typed packet's `pipeline_findings` (exact
`detail` strings and pins), not copied from the named set; §5 has the method. The
named set is the freeze against which the derived file is read: if the derived
set differs from this table, the difference is either a recorded amendment or a
finding — never a silent re-pin.

## 5. The expected-holds.json fragment

### 5.1 File and form

- fragment path: `reports/round-17/d4/expected-holds.fragment.json` (this seat's
  write). It is the **named pre-implementation freeze record** (§4), not the
  delivered file: it carries the exact `(id, severity, where)` set from the brief
  with `detail` null placeholders, the declared counts, and a
  `status: named-pre-implementation` marker; it carries **no pins** (pins are
  properties of delivered bytes and must never be guessed — F-D19-2).
- the delivered file: `examples/culture-d4/expected-holds.json` is *derived* at
  landing time (schema `kotodama-typed-pipeline-holds-v1`, D2's shape:
  `{schema, packet_sha256, projection_sha256, …, counts:{hold,note,fail},
  holds:[…], notes:[…]}`) from the delivered typed packet — §5.2's command —
  never copied from the fragment. Two runner interface constraints from
  typed-support-1.md §8 apply to the delivered file: omit `projector_sha256`
  (the runner pins that key to `tools/d2-typed-labels.py`; F-D18-7) and expect
  the routing-consistency leg to compare only the FORM-class holds against
  `typed_channel` (F-D18-6).
- canonical form (measured on the D2 file, byte-identical): insertion order,
  `json.dumps(doc, indent=1, ensure_ascii=False) + "\n"`.

### 5.2 The derivation is mechanical and already validated

The fragment is derived, never hand-edited. Scratch tool
`.scratch/r17d18/derive-holds-fragment.py` (this seat; read-only over the repo)
reads a delivered typed packet through the shipped strict loader
(`load_packet_file`), splits `pipeline_findings` into holds/notes/fails, takes
the pins from the typed packet's `assembly` block plus the projector's sha256,
and renders the canonical form. Validated against the D2 analogue
(2026-10-18, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```sh
python3 .scratch/r17d18/derive-holds-fragment.py \
    --typed examples/culture-d2/packet.d2.typed.yml \
    --projection examples/culture-d2/typed-labels.d2.yml \
    --projector tools/d2-typed-labels.py \
    --check examples/culture-d2/expected-holds.json
# → "examples/culture-d2/expected-holds.json: byte-identical fragment", exit 0
# (emitted scratch bytes sha256 a5dc26d5b495a90e05ce42d4d8b6d08f047359c377e458f9190b1d310d6dde3a
#  == the committed file's sha256, 3434 bytes, hold 15 / note 1 / fail 0)
```

For D4 the same command runs over `examples/culture-d4/packet.d4.typed.yml` once
the tree lands; `--typed-channel-only` restricts the fragment to the holds whose
`where` names a `typed_channel` record (the typed-label contribution) when a
rank fragment is merged alongside.

### 5.3 What the fragment vouches for

The named set's exact `(id, severity, where)` membership and counts (17/1/0) with
the A-19-1 amendment, under the exactness contract (§2). It does **not** vouch
for the `detail` strings or pin values — those are derived from the delivered
typed packet (§5.2), and the *derived* file, not this fragment, is what the
gate's constant must equal in both directions.

## 6. Findings and limits

- **F-D19-1 — the pre-implementation naming landed (resolved).** The design
  brief names the candidate set at `design-brief.md:385-411` (18/1/0) before any
  D4 byte; §4 documents it and applies the freeze rules, so the runner's
  design-doc naming leg has the ids and `where`s in two documents.
- **F-D19-2 — the fragment carries no pins.** The pins (`packet_sha256` etc.)
  are properties of delivered bytes; the fragment ships the named holds + counts
  with `detail` null and no pins, and the delivered file is *derived* (§5.2).
  Guessing a pin is the drift the D2 freeze discipline forbids.
- **F-D19-3 — row 8 dropped by amendment A-19-1; the named set is 17/1/0.**
  Evidence: `02-phonology.yml` `stress_record.minimal_pairs[0]` ("no delivered
  minimal pair contrasts length … (to-verify)"), `accent` (length written as a
  double vowel), and `03-orthography.yml:45` ("no diacritics are used, so no form
  carries a symbol outside 02's inventory"). With no declared diacritic and no
  delivered pair, the D2 `L-15`/`L-16` class has no D4 trigger and the row is
  unprovable (brief §7.2 rule 2). If the delivered components change, the row
  returns by a recorded amendment.
- **F-D19-4 — the delivered-file interfaces are constrained by the runner.**
  Omit `projector_sha256` (the runner pins that key to `tools/d2-typed-labels.py`;
  typed-support-1.md F-D18-7) and expect the routing-consistency leg to compare
  only the FORM-class holds against `typed_channel` (F-D18-6). The fragment
  documents both so the integrator's landing is explicit.
- **F-D19-5 — the naming leg needs each `where` token individually.** The D8 leg
  matches per token (`run-validation.py:172-173`, `:706-733`); the range
  `AL-01#plain`..`AL-06#plain` left four tokens (`AL-02#plain`..`AL-05#plain`)
  unnamed in every design doc (measured 2026-10-18: `grep -l` → 0 files each).
  §4 now enumerates all 17 `where`s and the note `where` individually
  (re-measured: every token ≥1 file) — see typed-support-1.md F-D18-9.
- **Limits.** This fragment does not vouch for the D4 derivation tooling (none
  exists at this stamp; typed-support-1.md §5.7), the components (drafts at
  `reports/round-17/d4/components/`), or any real-world claim. Canon status is
  lore's (`PROVINCE.md`).
