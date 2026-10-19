- Seat: D15 | executor | claim D | date 2026-10-19 | baseline da68a6d

# D15 — spare build seat: gap-fill on claim D's critical path

## What I found to fill, and why this is the largest gap

At read time the only landed fragment in the round was
`reports/round-34/depth/D11-preservation.md` (a pre-build preservation
snapshot, which owes nothing a spare can supply). The D block's critical path
is `declared-in-r7`, and the seam no other D seat is assigned to is **how the
renderer obtains the twelve D4 claim rows at all**. Establishing that seam
turned out to change what "rewrite the ledger prose to live numbers" means, so
that is what I built and then executed end to end in an isolated mirror.

Two findings, both measured, are the deliverable's spine:

1. **The stale D4 figures are not rendered from live bytes and cannot be fixed
   by editing the packet draft.** `tools/exercise-handoff-e2e.py:2289-2306`
   (`v3_parse_claims_map`) regex-extracts all twelve D4 rows out of
   `reports/round-20/handoff/claims-map.md` — a *filed* round, therefore
   uneditable — and carries statement/basis/links verbatim into the ledger
   (`tools/exercise-handoff-e2e.py:2566,2881,2934,3511,3561`). The constant is
   `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"`
   (`tools/exercise-handoff-e2e.py:184`), and `CLAIMS_MAP` is read-set index 57
   of 58 in `V3_READ_SET` (`tools/exercise-handoff-e2e.py:1957`), so it is
   digest-pinned in `expected.json.inputs`. Any live-number fix is therefore a
   **new claim-row source plus a one-constant renderer redirect** — a shared
   file change, drafted below, never applied by this seat.

2. **Four of the twelve rows need semantic rewrites, not number swaps.** The
   live D4 projection has *emptied* its rank-residual surface, so
   D4-CL07's "conflicts (4) … quarantine handles (3)" and D4-CL09's
   "re-carries D2's rank-rule adaptation rows with `adapt_status:
   cannot-evaluate`" are **false at the bytes**, not merely misnumbered.
   D4-CL06's hold arithmetic has also moved twice since the filed row was
   written. A numbers-only pass would have left three false statements in a
   "live" revision.

The strongest single piece of evidence for finding 1 is internal to the filed
revision: the r6 packet already prints the live value in one cell and the stale
value in another. `reports/round-30/handoff/declared-in-r6/packet.md:69` (the
A-30 manifest row, computed at render time) reads "82 labels (64 native-form /
12 translated-label / 6 borrowed-strata), 12 findings, 0 unresolved rank
items", while `:148` (the same revision's D4-CL05 row, carried from the filed
source) reads "typed_labels 74, … native-form 56 …, findings_total 16,
findings_hold_or_fail 15". Same revision, same file, same run: the computed
leg is live, the carried leg is stale. This is the self-contradiction the round
declaration names, now explained by mechanism rather than by symptom.

## The stale-figure census (contradicted value → live value, with live citation)

| site (r6 packet.md) | stale text | live value | live source |
|---|---|---|---|
| :148 D4-CL05 | typed_labels 74 / native-form 56 / findings_total 16 / findings_hold_or_fail 15 / `#stats` "(fail 0, hold 12, **labels 74**)" | typed_labels 82 / native-form 64 / findings_total 12 / findings_hold_or_fail 12 / stats labels 82 | `examples/culture-d4/typed-labels.d4.yml:46` (`typed_labels: 82`), `:31` (`findings_hold_or_fail: 12`), `:32-34`, `:35-39` (`labels_by_kind`), `:2865-2869` (`"stats": {"fail": 0, "hold": 12, "labels": 82}`) |
| :149 D4-CL06 | "15 holds, 1 note and 0 fails … three `D2L-RANK` holds, plus one `D2L-RANK` note" / "+9 hold / +1 note delta" | 12 holds, 0 notes, 0 fails, all twelve `D2L-FORM-UNRESOLVED` (one per `GAR-0x` and one per `LEX-GAR-0x`) | `examples/culture-d4/expected-holds.json` `counts {hold 12, note 0, fail 0}`, `holds` list length 12, `id` counter `{D2L-FORM-UNRESOLVED: 12}`, `where` counter = 6×`GAR-0x` + 6×`LEX-GAR-0x`, `notes: []` |
| :150 D4-CL07 | "conflicts (4), quarantine handles (3)" | conflicts 0, quarantine handles 0, reconciliation records 6 | `examples/culture-d4/typed-labels.d4.yml:30` (`conflicts: 0`), `:40` (`rank_quarantine_handles: 0`), `:45` (`reconciliation_records: 6`) |
| :152 D4-CL09 | "re-carries D2's rank-rule adaptation rows with `adapt_status: cannot-evaluate` … 13 unresolved rank items, 3 quarantine handles and 4 conflicts" | D4 carries **no** rank residual: `rank_rules.act_rules == []`, `.unresolved == []`, `.quarantine == []`; coverage 0 / 0 / 0 | `examples/culture-d4/typed-labels.d4.yml` `rank_rules` block (keys `act_rules, unresolved, quarantine, residuals` all empty), `:44` (`rank_rules_unresolved_items: 0`), `:40`, `:30` |
| :307 OQ-V3-05 | "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts" | twelve form holds, 0 notes, 0 fails, 0 / 0 / 0 (the 13 / 3 / 4 residuals are **D2's**) | renderer literal `tools/exercise-handoff-e2e.py:3521-3531`; the D2 residual values the text was copied from are live at `examples/culture-d2/typed-labels.d2.yml:30,32,40,45,46` and `packet.md:284` |

The 13 / 3 / 4 / 10 figures are **not stale as D2 facts** — they are live for
the D2 channel (`examples/culture-d2/typed-labels.d2.yml:30` conflicts 4,
`:32` findings_total 16, `:40` rank_quarantine_handles 3, `:45`
reconciliation_records 10, `:46` typed_labels 58; corroborated by the computed
line `packet.md:284`). They became stale only where the D4 row and OQ-V3-05
restated them as D4's own. The rewrite below keeps every D2-attributed
occurrence intact and re-attributes the D4 ones.

Reproduce the census:

```
grep -n "D4-CL0[5679]\|OQ-V3-05" reports/round-30/handoff/declared-in-r6/packet.md
python3 -c "import json;c=json.load(open('examples/culture-d4/typed-labels.d4.yml'))['coverage'];print(c)"
python3 -c "import json;print(json.load(open('examples/culture-d4/expected-holds.json'))['counts'])"
```

### Why the numbers moved (the repair history, from live bytes)

`examples/culture-d4/expected-holds.json` `revision_note` (round-28 law-replay
build) states it directly: *"The hold set is UNCHANGED at 12 holds / 0 notes /
0 fails: a law row is not a form, so the six garment-form obligations still
route to their twelve record/slot rows and the register stratum owes no form
slot."* The same file's `pin_generations[1]` (round-30 QREG records) repeats
"unchanged at 12 holds, zero notes, zero fails". So the filed D4-CL06 row
records the round-18 measurement (15 / 1), and rounds 28/30 superseded it
without the row being re-issued — which is exactly the class of drift claim D
exists to close.

The brief's own declaration is six holds — `examples/culture-d4/components/01-brief.yml`
`hold_set_declaration.expected_findings` lists `GAR-01..GAR-06`, and criterion
A-07 restates "six holds, zero notes, zero fails" — so against the live
emitted set of twelve the delta is **+6 hold / +0 note**, not the filed
"+9 hold / +1 note".

## Executed proof (this is not a sketch; the render was run)

An isolated mini-repo was built under `.scratch/d15/` (gitignored, never in a
filed round): the 58-file v3 read set plus the gate and the component inputs,
copied read-only from the tree; the renderer was copied to
`.scratch/d15/tools/exercise-handoff-e2e.py` and the two drafts below applied
**to that copy only**; the new claim-row source was written to
`.scratch/d15/reports/round-34/handoff/declared-in-r7/claims-map.md`.

Commands and observed output:

```
$ python3 .scratch/d15/tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d15/out
frozen: 2026-10-19 by tools/exercise-handoff-e2e.py --profile v3
packet_sha256: 062e889fa7829e93c62855a83dfe51025e56af06f906c8f2d68dd15164a912bb
twin_sha256:   d417205c127d36bc46b7a4506026dbda0b5e0c593d683db2a4e0d790775bacc4
gate: exit 0, fields=16/16, glossary-entries=20, findings=0
semantics: uncertainty exit 0, links 105/105 resolved
claims: 27 statuses 16/7/4; v2-subset ad35c860acf3b452…; alias leg landed
read set: 58 files; component digests 26/26; d4 pins 8/8
no tracked value changed since the previous freeze

$ python3 .scratch/d15/tools/exercise-handoff-e2e.py --profile v3 --baseline out/expected.json --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=062e889fa7829e93c62855a83dfe51025e56af06f906c8f2d68dd15164a912bb
EXIT=0

$ sha256sum .scratch/d15/out/packet.md          # == freeze.txt packet_sha256 line
062e889fa7829e93c62855a83dfe51025e56af06f906c8f2d68dd15164a912bb

$ freeze twice (out/ and out2/) -> identical packet and twin digests   # determinism
062e889f…  out/packet.md   062e889f…  out2/packet.md
d417205c…  out/twin.json   d417205c…  out2/twin.json
```

The new pair self-verifies against its own frozen baseline (`exit=0`), so the
claim's `e2e --quiet exit 0 with packet_sha256 == freeze.txt` leg holds for
this draft. Statuses stay `16/7/4` and `v2_subset_digest` stays
`ad35c860acf3b452…` (identical to r6's freeze line), i.e. the change does not
touch the v2 rows, the census, or any axis the baseline counts.

**Input delta r6 → r7 (the "only the source moved" proof):**

```
r6 inputs: 58   r7 inputs: 58
paths added:   ['reports/round-34/handoff/declared-in-r7/claims-map.md']
paths removed: ['reports/round-20/handoff/claims-map.md']
digest-changed paths among the 57 shared: []          # none
DIFFERS: packet_sha256, twin_sha256
same: counts, claim_ids, v2_subset_digest, alias_state, uncertainty, links
baseline_digest 714b41fc58595b96e56888cd… -> f63015c4d025212d9363408f…
```

Packet shape: 335 lines before and after; 105,584 → 106,320 bytes; **16
changed lines** in `diff` (5 content rows + the artifacts-manifest row + the
two prose references to the source path + the surrounding context lines).

### Stale-figure audit of the rendered draft

| token | r6 packet | r7 draft |
|---|---:|---:|
| `typed_labels 74` | 1 | **0** |
| `native-form 56` | 1 | **0** |
| `findings_hold_or_fail 15` | 1 | **0** |
| `15 holds, 1 note` | 1 | **0** |
| `conflicts (4)` | 1 | **0** |
| `labels 74` | 1 | **0** |
| `findings_total 16` | 2 | 1 — the D2-CL01 row, live for D2 (`typed-labels.d2.yml:32`) |
| `thirteen unresolved` | 2 | 1 — OQ-V3-05's D2 attribution, live (`typed-labels.d2.yml` residuals, `packet.md:284`) |
| `3 quarantine handles` / `4 conflicts` | 4 / 4 | 4 / 4 — every remaining occurrence is D2-attributed (`:130`, `:152`, `:284`, `:301`, `:307`); verified by `grep -o` context print |

The four rows and the OQ row in the twin carry the new text
(`twin.json` `claim_ledger`, 27 rows; `open_questions` 10 rows, `OQ-V3-05`
present).

## Draft 1 — the renderer change (BEFORE → AFTER, for the integrator)

Shared file `tools/exercise-handoff-e2e.py`; four hunks. The file's sha256 at
baseline is `a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df`;
the patched copy that produced the digests above is
`2d16b014d78f9b249eb1959ea9e725e2de362358506cea14f9d34010345a9e93` (237,075
bytes, from 236,871 — +204 bytes).

**Hunk 1 — `tools/exercise-handoff-e2e.py:184`**

```python
# BEFORE
CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"
# AFTER
CLAIMS_MAP = "reports/round-34/handoff/declared-in-r7/claims-map.md"
```

**Hunk 2 — `tools/exercise-handoff-e2e.py:2290` (docstring)**

```python
# BEFORE
    """The twelve D4 rows as filed in reports/round-20/handoff/claims-map.md."""
# AFTER
    """The twelve D4 rows as declared in this round's handoff source."""
```

**Hunk 3 — `tools/exercise-handoff-e2e.py:2566` (artifact-manifest description)**

```python
# BEFORE
        CLAIMS_MAP: "the twelve D4 claim rows as filed; this packet carries them verbatim",
# AFTER
        CLAIMS_MAP: "the twelve D4 claim rows as declared in this round's handoff source; this packet carries them verbatim",
```

**Hunk 4 — `tools/exercise-handoff-e2e.py:3521-3531` (the OQ-V3-05 literal)**

```python
# BEFORE
                "question": (
                    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
                    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
                    "kotodama; blocking for the affected D2 rank records and the six garment terms, not for "
                    "this envelope"
                ),
# AFTER
                "question": (
                    "D4's own holds stay open: twelve form holds, zero notes and zero fails, and the "
                    "projection counts zero unresolved rank items, zero quarantine handles and zero conflicts "
                    "(the thirteen unresolved rank items, three quarantine handles and four conflicts are the "
                    "D2 channel's residuals, counted on the D2 row) — kotodama; blocking for the affected D2 "
                    "rank records and the six garment terms, not for this envelope"
                ),
```

Every BEFORE block above was re-applied to the baseline file bytes as an
assertion (exactly one occurrence each) and every AFTER block re-checked
against the patched copy, by re-reading this fragment's own code blocks — see
"Self-check of the drafts" below. The mirror patch used those same bytes.

Hunks 1–3 also move the packets' own `§artifact_manifest` A-57 row and the two
prose references to the source at `:2881` / `:2934` automatically, because
those render from the constant. Nothing else in the renderer needs to move:
the source path is replaced at the same `V3_READ_SET` index, so the `A-nn`
manifest ids stay stable (verified: the draft's manifest ids are unchanged
except A-57's path/digest/description cells).

## Draft 2 — the new claim-row source (the round-20 file, 10 replacements)

Land as `reports/round-34/handoff/declared-in-r7/claims-map.md`: copy the
filed `reports/round-20/handoff/claims-map.md` (sha256
`4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`, 24,888
bytes — the same file the r6 revision already pins as read-set entry A-57) and
apply these ten replacements. The result measured in the mirror is 25,467
bytes, sha256 `f71751e0681f97959ed9a2877c545bf2bc61082d6a082b27293edeb86969251c`,
and it re-parses to exactly 12 rows under the renderer's own `D4_ROW_RE`
(verified by running the renderer's extractor on it). Each replacement fired
exactly once (asserted in the run). Eight rows (D4-CL01..04, CL08, CL10..12)
are carried byte-identical.

**R1 — D4-CL05 statement**

```
BEFORE: types 74 labels — 56 native-form, 12
  translated-label, 6 borrowed-strata — and carries 16 findings of which 15 are
  hold-or-fail (12 label holds, 0 label fails);
AFTER:  types 82 labels — 64 native-form, 12
  translated-label, 6 borrowed-strata — and carries 12 findings, all of them
  holds (12 label holds, 0 label fails);
```

**R2 — D4-CL05 basis (coverage figures)**

```
BEFORE: (typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 16, findings_hold_or_fail 15, label_findings_fail 0)
AFTER:  (typed_labels 82, labels_by_kind native-form 64 / translated-label 12 / borrowed-strata 6, findings_total 12, findings_hold_or_fail 12, label_findings_fail 0)
```

**R3 — D4-CL05 basis (`#stats` parenthetical)**

```
BEFORE: #stats (fail 0, hold 12, labels 74)
AFTER:  #stats (fail 0, hold 12, labels 82)
```

**R4 — D4-CL06 statement**

```
BEFORE: The committed D4 hold set is 15 holds, 1 note and 0 fails,
  pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to
  each garment twice (record id and slot id) and three `D2L-RANK` holds, plus
  one `D2L-RANK` note for the band-keyed pair; the emitted set equals the
  committed file, and the round-17 brief's six-row declaration is reconciled by
  a documented +9 hold / +1 note delta rather than absorbed or silently
  re-declared.
AFTER:  The committed D4 hold set is 12 holds, 0 notes and 0 fails,
  pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to
  each garment twice (record id and slot id — `GAR-01..GAR-06` and
  `LEX-GAR-01..LEX-GAR-06`); the emitted set equals the committed file, and the
  round-17 brief's six-row declaration is reconciled by a documented +6 hold /
  +0 note delta rather than absorbed or silently re-declared.
```

**R5 — D4-CL06 basis**

```
BEFORE: #counts (hold 15, note 1, fail 0) with the row list, whose holds are twelve D2L-FORM-UNRESOLVED rows keyed to each garment twice and three D2L-RANK rows, plus one D2L-RANK note for the band-keyed pair; the emitted set equals the committed file and reports/round-18/d4/holds.md reconciles the brief's six-row declaration with a documented +9 hold delta rather than absorbing it
AFTER:  #counts (hold 12, note 0, fail 0) with the row list, whose holds are twelve D2L-FORM-UNRESOLVED rows keyed to each garment twice (GAR-01..GAR-06 and LEX-GAR-01..LEX-GAR-06); the emitted set equals the committed file, its own revision_note records that the hold set is unchanged at 12 holds / 0 notes / 0 fails since the round-28 law-replay build, and reports/round-18/d4/holds.md's reading of 15 holds / 1 note stands filed as a superseded measurement rather than absorbed
```

**R6 — D4-CL07 statement**

```
BEFORE: while the reconciliation's own conflicts (4), quarantine
  handles (3) and reconciliation records (6) are carried as counts rather than
  collapsed into a cleaner ledger.
AFTER:  while the reconciliation carries six reconciliation records
  and the file's coverage block counts zero conflicts and zero quarantine
  handles — carried as measured counts rather than asserted away.
```

**R7 — D4-CL07 basis**

```
BEFORE: counts carry four conflicts without collapsing them
AFTER:  counts carry six reconciliation records and zero conflicts, taken as measured rather than collapsed
```

**R8 — D4-CL09 statement**

```
BEFORE: The D4 projection re-carries D2's rank-rule adaptation rows
  with `adapt_status: cannot-evaluate` — speech is not a gate-modelled channel
  — and the packet's coverage block holds 13 unresolved rank items, 3
  quarantine handles and 4 conflicts; none of them is promoted, resolved or
  hidden by this packet, and they are inherited D2 normalization residuals
  rather than D4 design debt.
AFTER:  The D4 projection carries no rank residual of its own: its
  `rank_rules` block's `act_rules`, `unresolved` and `quarantine` lists are
  empty and the coverage block counts 0 unresolved rank items, 0 quarantine
  handles and 0 conflicts, so the D2 normalization residuals (13 unresolved
  rank items, 3 quarantine handles, 4 conflicts) stay D2's own and are counted
  on the D2 row rather than restated here; what stays open for D4 is the six
  garment terms the twelve `D2L-FORM-UNRESOLVED` holds key (claim D4-CL04),
  and no residual is promoted, resolved or hidden by this packet.
```

**R9 — D4-CL09 basis**

```
BEFORE: whose act rows carry adapt_status cannot-evaluate because speech is not a gate-modelled channel, with examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items 13 and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles 3 and examples/culture-d4/typed-labels.d4.yml#conflicts 4 in the same file's coverage block; open: the thirteen unresolved rank items, three quarantine handles and four conflicts are inherited D2 normalization residuals and none of them is promoted by this packet; owner: kotodama, blocking for the affected D2 rank records, not for this envelope
AFTER:  whose act_rules, unresolved and quarantine lists are empty at the delivered bytes, with examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items 0 and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles 0 and examples/culture-d4/typed-labels.d4.yml#conflicts 0 in the same file's coverage block; the D2 normalization residuals (13 unresolved rank items, 3 quarantine handles, 4 conflicts) are counted on the D2 channel in this packet's own D2 fact row rather than restated as D4 debt; open: the six garment terms stay owed through twelve D2L-FORM-UNRESOLVED holds (claim D4-CL04), and no rank or form residual is promoted or hidden by this packet; owner: kotodama, blocking for the affected D2 rank records and the six garment terms, not for this envelope
```

**R10 — the §4 open-question table row (`reports/round-20/handoff/claims-map.md:251`)**

```
BEFORE: | `OQ-V3-05` | D4's inherited and own holds stay open: 12 form holds + 3 rank holds + 1 note, 13 unresolved rank items, 3 quarantine handles, 4 conflicts |
AFTER:  | `OQ-V3-05` | D4's own holds stay open: 12 form holds, 0 notes, 0 fails; the projection carries 0 unresolved rank items, 0 quarantine handles and 0 conflicts (the 13/3/4 residuals are D2's, counted on the D2 row) |
```

R10 does not affect the render (the renderer carries its own OQ literal — hunk 4);
it is included so the landed source file does not itself carry a figure its own
rows contradict.

**Status kept unchanged, deliberately.** D4-CL09 stays `unresolved` with
`(author-side), holds open`: the open leg is real and still measured — the six
garment terms remain owed through the twelve `D2L-FORM-UNRESOLVED` holds
(`examples/culture-d4/expected-holds.json` `holds`, and D4-CL04's `form_slots`
are all `unfilled`). Keeping the status also keeps the `16/7/4` census and the
`--require-oq` routing (`OQ-V3-05 → D4-CL09`) unchanged, which is why the
v2-subset digest is bit-identical. Flipping it to `supported` would change the
census and is **not** this seat's call — recorded as a decision for the
integrator under Owed.

## Self-check of the drafts (this fragment's own bytes, verified)

The four Draft-1 hunks were lifted back out of this fragment's code blocks and
re-applied to the baseline file bytes, then compared against the mirror copy
that produced every digest above:

```
hunks found in the fragment: 4
hunk 1: BEFORE occurrences in baseline file = 1; AFTER occurrences in patched copy = 1
hunk 2: BEFORE occurrences in baseline file = 1; AFTER occurrences in patched copy = 1
hunk 3: BEFORE occurrences in baseline file = 1; AFTER occurrences in patched copy = 1
hunk 4: BEFORE occurrences in baseline file = 1; AFTER occurrences in patched copy = 1
SELF-CHECK: PASS
round-trip sha256: 2d16b014d78f9b249eb1959ea9e725e2de362358506cea14f9d34010345a9e93
patched copy sha256: 2d16b014d78f9b249eb1959ea9e725e2de362358506cea14f9d34010345a9e93
ROUND-TRIP: identical
```

So the drafts in this fragment are sufficient on their own: applying the four
hunks to a byte-identical copy of `tools/exercise-handoff-e2e.py` reproduces
the patched copy bit for bit, and Draft 2's ten replacements reproduce the new
claim-row source at sha256
`f71751e0681f97959ed9a2877c545bf2bc61082d6a082b27293edeb86969251c`. (This
seat's first transcription of hunk 4 read `kotadama` where the file reads
`kotodama`; the self-check caught it and the fragment was corrected before
handoff — the check above is the corrected state.) The Draft-2 replacements are
not machine-re-applied here because they are quoted as claims-map source rather
than as python; they were asserted single-occurrence at build time in the
mirror, and the resulting file's digest is the check that matters.

## Negative and tamper controls (both directions measured)

**(a) The gate is shape-only; it cannot see semantic staleness.** Running the
filed r6 packet through the gate on an isolated copy:

```
$ cp reports/round-30/handoff/declared-in-r6/packet.md .scratch/d15/r6-packet.md
$ python3 tools/gates/handoff-packet-check.py .scratch/d15/r6-packet.md
INFO scan: fields=16/16 glossary-entries=20 findings=0        # exit 0
```

A revision with five contradicted tables still scans 16/16, 0 findings. This
names the class my method catches that the gate cannot: **carried-prose
staleness** — a cell whose text was vendored from an earlier round while the
computed cells around it moved on.

**(b) A number tamper passes the gate and is caught only by the freeze pin.**

```
$ python3 -c "mutate '82 labels' -> '92 labels' in a copy"
mutated offset 14052 -> b'projection: 92 labels (6'   sha256 9b774c0eccc8248b…
$ python3 tools/gates/handoff-packet-check.py .scratch/d15/tamper.md
INFO scan: fields=16/16 glossary-entries=20 findings=0        # exit 0 — NOT caught
$ expected.json packet_sha256: 062e889fa7829e93c62855a83dfe51025e56af06f906c8f2d68dd15164a912bb
  9b774c0e…  .scratch/d15/tamper.md                            # caught by the pin
```

**(c) A structural tamper IS caught by the gate** (proving the control battery
is not vacuous):

```
$ python3 -c "replace '## artifact_manifest' with '## manifest_removed'"
mutation landed, bytes 105899 -> 105898
$ python3 tools/gates/handoff-packet-check.py .scratch/d15/tamper-struct2.md
FINDING HO-MISSING: FAIL — required field/section `artifact_manifest` absent …
INFO scan: fields=15/16 glossary-entries=20 findings=1        # exit 1
```

**(d) The filed r6 pair is still fully green at HEAD**, i.e. the defect claim D
addresses is invisible to every existing leg, not a red baseline:

```
$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
EXIT=0
```

`6ced88ad…` equals the r6 `freeze.txt` value, so the input-digest leg passes
too — the read set has **not** drifted. That is the decisive fact for the
diagnosis: the renderer read the very same live bytes and produced 82 in one
cell and 74 in another, so the fix belongs in the row source, not in the inputs.

## Observation for the integrator (not part of claim D, do not fix silently)

`tools/exercise-handoff-e2e.py:2636` reads `read_text(ROOT, RECONCILIATION)`
with the **module** root rather than the `root` argument passed down from
`--root` (`v3_build_twin` is called with `root=...` at
`tools/exercise-handoff-e2e.py:3563`, but that line ignores it). Consequence: a
`--root` run against a mirror that is not reachable from the module's own
`ROOT` fails with `E2E-ARTIFACT read-set file unreadable:
reports/round-6/parent-reconciliation.json`, which is how this seat found it.
In-tree runs are unaffected (ROOT == root), and this seat did **not** patch it
(the drafts above are the only renderer change proposed). It is a latent
root-coupling wart worth its own row if the round wants mirror runs; recorded
here so it is not rediscovered as a mystery.

## Relationship to the landed D fragments (convergence, and what is unique here)

Fragments landed while this seat worked. Read at close, the mechanism above is
**convergent, not novel**, and saying so is part of the handoff:

- Route A (the twelve rows carried from the filed `round-20/handoff/claims-map.md`)
  was reached independently by `reports/round-34/depth/D01-layout.md:143-164`,
  `D02-render.md:71,140`, `D08-links-uncertainty.md` and `D12-receipt.md`, and
  restated by `D16-gap-fill.md` §4. Route B (the hardcoded `OQ-V3-05` literal) by
  `D02-render.md:142` and `D01-layout.md`. Two independent live-value censuses
  agree with mine cell for cell (`D03-ledger-rows.md` §1: 82 / 64 / 12 / 6,
  findings 12, conflicts 0, quarantine 0, unresolved 0, reconciliations 6, same
  `file:line` sources).
- `D02-render.md:71` states the binding consequence most sharply and it matches my
  measurement exactly: with read-set drift 0, "re-running the renderer — or moving
  the default to a freshly frozen `declared-in-r7` — yields **byte-identical
  output carrying the same stale digits**". My in-tree run reproduces its
  `6ced88ad…` result.

What this fragment has that the others do not:

1. **An executed AFTER render.** D02 rendered the *unchanged* sources (proving the
   stale bytes reproduce); D16 rendered inside a `git archive` isolate with the
   sources likewise unmoved. Neither measured a redirected render. The mirror run
   above did, and it is green on every leg with `packet_sha256 062e889f…` /
   `twin_sha256 d417205c…`.
2. **Semantic rewrites, not only figures.** D03 delivers replacement values and
   D04 the OQ rows; neither rewrites D4-CL07's and D4-CL09's *false sentences*
   about rank residuals that no longer exist in the D4 projection. A values-only
   pass leaves three statements contradicted by the bytes they cite.
3. **Byte-exact, self-checked drafts.** The four renderer hunks round-trip from
   this fragment's own code blocks to the exact patched copy (see "Self-check of
   the drafts").

**Naming collision the integrator must break.** `D01-layout.md:150-164` sends the
new source to `reports/round-34/handoff/claims-map-v3-next.md`; this fragment sent
it to `reports/round-34/handoff/declared-in-r7/claims-map.md`; `D16-gap-fill.md` §7
records that three seats propose three names. The path is a free parameter — but it
is *not* digest-free: the path string is printed in the packet itself (the
`§artifact_manifest` A-57 row, and the two prose references rendered from the
constant at `tools/exercise-handoff-e2e.py:2881,2934`) and it is a key of
`expected.json.inputs`. **If the integrator lands the source at any path other than
the one this fragment used, the measured `062e889f…` no longer applies and the
packet must be re-frozen and re-measured.** The source *content* digest
(`f71751e0681f97959ed9a2877c545bf2bc61082d6a082b27293edeb86969251c`) is
path-independent; the packet digest is not. D01's name is as good as mine — it
should win if D01's layout is what the integrator follows, with this fragment
treated as the executed proof that the route works.
`D16-gap-fill.md` §7 also notes that `D10-repin-drafts.md`'s census omits the
`CLAIMS_MAP` re-point; hunks 1–3 here are exactly that missing row.

**Still-absent seats.** `D05-packet-draft.md`, `D17-verify-gates.md` and
`D19-verify-repin.md` had not landed at this seat's close. This fragment
substitutes for D05's deliverable in reproducible form rather than as a fenced
105 KB artifact: the draft is byte-identical to the filed r6 `packet.md` outside
16 lines, and one command regenerates it once the two drafts are applied
(`python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7`).
D17/D19's independent re-runs remain owed to those seats.

## Owed

1. **The two drafts are unapplied, by rule.** The integrator (or D05/D07) must
   land `reports/round-34/handoff/declared-in-r7/claims-map.md` (Draft 2,
   target sha256 `f71751e0681f97959ed9a2877c545bf2bc61082d6a082b27293edeb86969251c`)
   and apply Draft 1's four hunks to `tools/exercise-handoff-e2e.py`, then
   re-render so the filed revision carries the digests the mirror measured
   (`packet_sha256 062e889fa7829e93c62855a83dfe51025e56af06f906c8f2d68dd15164a912bb`,
   `twin_sha256 d417205c127d36bc46b7a4506026dbda0b5e0c593d683db2a4e0d790775bacc4`).
   Those digests are **mirror measurements, not filed bytes**: they are
   reproducible only if the integrator lands Draft 2 byte-exactly (in
   particular the ten replacements and nothing else) and applies only Draft 1's
   four hunks. Any extra edit will move them; re-measure at freeze time and
   treat the mirror values as the expected, not the authoritative, result.
2. **Decision owed: D4-CL09's status.** Kept `unresolved` here so the census
   and `--require-oq` routing stay stable. Whether a row whose grounding is now
   "carries no residual of its own" should stay `unresolved` is a
   claim-evidence judgement for the claim-D owner (and D18/D20 as verifiers),
   not for this seat. Flipping it changes `statuses 16/7/4` and the v2-subset
   check's context.
3. **The D05 draft must be re-derived, not patched.** D02/D05's sketches
   predate this finding; if any of them assumed the packet could be rendered
   from live bytes without the source redirect, their drafts will reproduce the
   stale rows. `reports/round-34/depth/D02-render.md` and
   `reports/round-34/depth/D05-packet-draft.md` should be re-checked against
   this fragment by D17/D20.
4. **`reports/round-18/d4/holds.md` is a filed superseded reading** (+9 hold /
   +1 note against a 15-hold set). The rewritten D4-CL06 row names it as such
   rather than editing it. If the round wants the round-18 doc re-issued, that
   is a new supersession row, not an edit — out of scope here.
5. **Naming drift noticed, not claimed:** the brief declares its holds as
   `D4L-FORM-UNRESOLVED` (`examples/culture-d4/components/01-brief.yml`
   `hold_set_declaration.expected_findings`) while the live emitted set uses
   `D2L-FORM-UNRESOLVED` (`examples/culture-d4/expected-holds.json` `holds[].id`).
   Recorded as an observation only — this seat did not measure whether it is a
   defect or a deliberate re-homing, so it is `to-verify`.
6. No `reports/round-34/run-validation.py` exists yet, so the claim's third
   counting command could not be run; the mirror used the renderer directly, and
   the round validator is the integrator's to add.

## Citations

Contract and declaration (read-only):

- `REGIMEN.md:25-50` — per-round contract; `:60-69` scope and stop rules.
- `reports/round-34/claims.json:20-37` — claim D, before/after,
  counting commands and thresholds; `:68-74` non-goals.
- `reports/round-34/targets.json:5-11` — the binding shared rules; `:37` this
  seat's row (`depth/D15-gap-fill.md`).
- `reports/round-34/depth/D11-preservation.md` — the only fragment landed at
  read time; its `## Owed` items overlap mine only on the post-build re-run,
  which belongs to the integrator.

Renderer (read-only; the patched copy lives only under `.scratch/d15/`):

- `tools/exercise-handoff-e2e.py:184` `CLAIMS_MAP` constant; `:1957` its place in
  `V3_READ_SET` (index 57/58); `:2289-2306` `v3_parse_claims_map` and `D4_ROW_RE`;
  `:2331,2599-2617,2621-2628` claim-row assembly; `:2566` manifest description;
  `:2636` the ROOT-hardcoded reconciliation read; `:2881,2934` prose references;
  `:310-317` `cell()` (whitespace flatten + pipe guard); `:3511,3561` call sites;
  `:3521-3531` the OQ-V3-05 literal; `:3693-3724` `run_gate`; `:3806-3830`
  `v3_exercise` digest leg; `:4020-4126` `v3_freeze` (expected.json / freeze.txt
  / run.log writers); `:4487,4559-4600` CLI.
- sha256 at baseline: `a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df`.

Live artifacts (read-only, the values the rewrite cites):

- `examples/culture-d4/typed-labels.d4.yml:30,31,32,33,34,35-39,40,44,45,46`
  (coverage block), `:2865-2869` (`typed_labels.stats`), and the `rank_rules`
  block (`act_rules`, `unresolved`, `quarantine`, `residuals` all empty).
- `examples/culture-d4/expected-holds.json` — `counts`, `holds` (12 rows, ids,
  `where` keys), `notes: []`, `revision_note`, `pin_generations`,
  `supersedes_pins`, `active_pin_generation: round-30-qreg-records`.
- `examples/culture-d4/components/01-brief.yml` — `hold_set_declaration`
  (six `D4L-FORM-UNRESOLVED` rows) and criterion A-07.
- `examples/culture-d2/typed-labels.d2.yml:30,32,40,45,46` — the D2 residuals
  the D4 row and OQ-V3-05 were copied from.
- `reports/round-20/handoff/claims-map.md:97-190` (the twelve D4 rows),
  `:251` (the OQ table row); sha256
  `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`.
- `reports/round-30/handoff/declared-in-r6/packet.md:69,148,149,150,152,284,307`
  and `:49,129,130,266,301`; `freeze.txt`; `expected.json`.
- `reports/round-18/d4/holds.md` (the superseded 15/1 reading, quoted, never
  edited).

Commands run (all read-only with respect to the tree; writes confined to
`.scratch/d15/`, which is gitignored):

- `python3 .scratch/d15/tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d15/out`
  → `packet_sha256 062e889f…`, `twin_sha256 d417205c…`, gate `16/16`,
  `glossary-entries=20`, `findings=0`, `links 105/105 resolved`, `statuses
  16/7/4`.
- `python3 .scratch/d15/tools/exercise-handoff-e2e.py --profile v3 --baseline out/expected.json --quiet`
  → `exit=0 … packet_sha256=062e889f…`.
- Second freeze into `.scratch/d15/out2/` → identical packet/twin digests.
- `sha256sum .scratch/d15/out/packet.md` → equals the `freeze.txt` line.
- `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (in-tree, against
  the current default r6 baseline) → `exit=0 … packet_sha256=6ced88ad…`.
- `python3 tools/gates/handoff-packet-check.py .scratch/d15/r6-packet.md` →
  `fields=16/16 … findings=0`, exit 0.
- `python3 tools/gates/handoff-packet-check.py .scratch/d15/tamper.md` →
  exit 0 (number tamper not caught); `sha256sum` differs from the pin.
- `python3 tools/gates/handoff-packet-check.py .scratch/d15/tamper-struct2.md`
  → exit 1, `FINDING HO-MISSING`, `fields=15/16`, `findings=1`.
- `diff reports/round-30/handoff/declared-in-r6/packet.md .scratch/d15/out/packet.md`
  → 16 changed lines; `wc -l -c` → 335 lines both, 105,584 → 106,320 bytes.
- Expected.json comparison (`inputs` delta, `counts`, `claim_ids`,
  `v2_subset_digest`, `uncertainty`, `links`) → only the two digests and the one
  input path differ.
- `grep -c` / `grep -o` stale-token census over both packets (table above).
- Not executed, per the shared rules: no `reports/round-*/run-validation.py`
  (F-C13-1), no round runner, no commit, no install, no network.
