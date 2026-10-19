- Seat: K01 | scout | claim D | date 2026-10-19 | baseline da68a6d

# K01 — packet-state scout (v3 chain, live D4 numbers, stale-figure census)

All numbers below were re-measured at the working tree at `da68a6d`
(`git log --oneline -1` → `da68a6d round-33: admit O/C/A …`); `git status --porcelain`
at scout time showed only `?? reports/round-34/` — the tree is otherwise clean, so
every live figure below is the filed-baseline figure.

## 1. The v3 chain

### 1.1 Renderer defaults (the pin claim D moves)

| what | path:line | value |
|---|---|---|
| baseline default | `tools/exercise-handoff-e2e.py:1933` | `V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"` |
| frozen-dir default | `tools/exercise-handoff-e2e.py:1934` | `V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"` |

Two further uses of the same constant pair that a re-pin must not miss:

- `tools/exercise-handoff-e2e.py:3185` — the packet's own §validation prose interpolates
  `V3_BASELINE_DEFAULT`, so the *rendered packet text* names the baseline directory.
  A re-pin changes packet bytes (and therefore `packet_sha256`) even before any claim
  prose is touched. `reports/round-30/handoff/declared-in-r6/packet.md:295` quotes that
  sentence verbatim.
- `tools/exercise-handoff-e2e.py:4561` — `baseline_default, frozen_default = V3_BASELINE_DEFAULT, V3_FROZEN_DIR_DEFAULT`
  in `main()`; `--baseline PATH` (:4488) overrides it at run time.

Stale-adjacent surface, found while sweeping (belongs to K02's census as well): the
module docstring at `tools/exercise-handoff-e2e.py:38-40` still says *"its current
baseline is under `reports/round-22/handoff/declared-in-r2/`"* — i.e. the docstring names
**r2**, not r6, so a plain `grep declared-in-r6` re-pin census will not surface it.

### 1.2 The revision directories actually filed

`find reports -maxdepth 4 -name 'declared-in-*' -type d`:

| revision | directory | produced by | file set | packet.md sha256 |
|---|---|---|---|---|
| r2 | `reports/round-22/handoff/declared-in-r2/` | renderer `--freeze` (frozen_by `tools/exercise-handoff-e2e.py --profile v3`) | expected.json, freeze.txt, packet.md, run.log, twin.json | `a97a0f0a0a497cb4…` |
| r3 | `reports/round-23/wording/declared-in-r3/` | `reports/round-23/wording/wording-check.py --check` (seat build, **not** a renderer freeze) | expected.json, freeze.txt, packet.md, run.log (**no twin.json**) | `084dc5db9a8d923b…` |
| r4 | `reports/round-25/v3-supersession/declared-in-r4/` | `reports/round-25/v3-supersession/v3-supersession-check.py --check` (seat build) | expected.json, freeze.txt, packet.md (**no twin, no run.log**) | `5f58db4a52b68856…` |
| r5 | `reports/round-26/handoff/declared-in-r5/` | renderer `--freeze` | 5 files | `e3fb1ca500d62981…` |
| **r6 (current default)** | `reports/round-30/handoff/declared-in-r6/` | renderer `--freeze` | 5 files | `6ced88ad009f1cfc…` |

Precedent note for P01/D01: r3 and r4 were *seat-built wording supersessions* whose own
`freeze.txt` first line explicitly disclaims the renderer
(`reports/round-25/v3-supersession/declared-in-r4/freeze.txt:1-2`), while r2/r5/r6 are true
renderer freezes. Claim D asks for a renderer freeze (`expected.json + freeze.txt + tamper
control`, `counting_commands` includes `--profile v3 --quiet`), so **r7 belongs to the
r2/r5/r6 shape**, and the 5-file set is the shape to mirror.

### 1.3 declared-in-r6 file shapes (measured)

| file | bytes | sha256 |
|---|---|---|
| `packet.md` | 105,584 | `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` |
| `twin.json` | 103,625 | `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e` |
| `expected.json` | 10,856 | `ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0` |
| `freeze.txt` | 586 | `6fe70c0c2b3a03ee82181a4906dc9670f73424c54efddec8fc632d213cca5d59` |
| `run.log` | 1,603 | `b5ee33510af0297e162e24bcdcf4aea563cbf7f3d112faf85720587479e3ed47` |

`packet_sha256`/`twin_sha256` recorded in freeze.txt and expected.json equal the measured
digests above — the freeze is byte-honest at r6.

**freeze.txt format** (6 lines, assembled at `tools/exercise-handoff-e2e.py:4113-4125`,
written at `:4126`):

```
frozen: <YYYY-MM-DD> by tools/exercise-handoff-e2e.py --profile v3
packet_sha256: <64 hex>
twin_sha256: <64 hex>
gate: exit 0, fields=16/16, glossary-entries=20, findings=0
semantics: uncertainty exit 0, links 105/105 resolved
claims: 27 statuses 16/7/4; v2-subset ad35c860acf3b452…; alias leg landed
read set: 58 files; component digests 26/26; d4 pins 8/8
```

(the 7th line is emitted only on a re-freeze: `re-frozen <key>: <old>… -> <new>…`, built at
`:4105-4112`; the r6 file carries the `re-frozen packet_sha256: ec30b11f… -> 6ced88ad…` row,
proving r6 was itself a re-freeze over an earlier r6-directory write.)

**expected.json shape** — 26 top-level keys
(`alias_state, baseline_digest, claim_ids, counts, cross_refs, declared_expectation,
expected_exit, expected_finding_ids, expected_links_findings, expected_links_unresolved,
expected_scan, expected_uncertainty_findings, field_digests, frozen_at, frozen_by,
glossary_entry_ids, inputs, limits, links, packet_id, packet_sha256, packet_version,
profile, twin_sha256, uncertainty, v2_subset_digest`), written by `v3_freeze`
(`tools/exercise-handoff-e2e.py:3978-4127`). Load-bearing values at r6:

- `profile` `kotodama-handoff-e2e/3`, `packet_id` `kotodama.handoff.d2d3d4-e2e`, `packet_version` `3.1.1`
- `inputs` — **58** read-set entries (`len(V3_READ_SET)`), each a bare sha256
- `field_digests` — **16** entries (one per contract §4 field)
- `counts` — 20 keys; the D4 group already reads **live**: `d4_typed_labels 82`, `d4_holds 12`, `d4_lexicon 62`, `d4_symbols 8`, `d4_costumes 6`, `d4_rank_rules 4`, `d4_era_records 8`, `d4_edges 54`, `d4_claims 12`, `claims 27`, `edges 88`
- `links` `{exit 0, findings 0, links 105, resolved 105}`; `uncertainty.statuses {supported 16, partial 7, unresolved 4}`
- `cross_refs` `component_digests_checked/matched 26/26`, `d4_pins_checked/matched 8/8`, `gate_exit 0`, `gate_scan {fields 16/16, glossary_entries 20, findings 0}`

**Critical observation for claim D**: `expected.json.counts.d4_typed_labels = 82` and
`d4_holds = 12` are **already live-correct** while the packet prose in the same directory
says 74 and 15. The baseline file and the packet body of the *same revision* disagree.
This is the "self-contradiction" the claim names, and it means the r6 baseline cannot be
used to detect the staleness — only a re-read of the D4 bytes can.

**twin.json shape** — 7 top-level keys: `artifact_manifest` (58), `claim_ledger` (27),
`coupling_edges` (88), `open_questions` (10), `packet_id`, `packet_version`, `profile`.

**run.log shape** — 14 lines: exercise/gate/gate verdict/semantics/v2-subset/alias-state/
packet sha/twin sha/read-set + 4 `d4 leg:` lines + the gate's own `INFO scan:` line.

## 2. Live D4 numbers at da68a6d

`examples/culture-d4/typed-labels.d4.yml` — the `coverage` block at `:29-47` (JSON-formatted):

| key | line | live value | packet prose says |
|---|---|---|---|
| `typed_labels` | `:46` | **82** | 74 |
| `labels_by_kind.native-form` | `:37` | **64** | 56 |
| `labels_by_kind.translated-label` | `:38` | **12** | 12 (agrees) |
| `labels_by_kind.borrowed-strata` | `:36` | **6** | 6 (agrees) |
| `findings_total` | `:32` | **12** | 16 |
| `findings_hold_or_fail` | `:31` | **12** | 15 |
| `label_findings_hold` | `:34` | **12** | 12 (agrees) |
| `label_findings_fail` | `:33` | **0** | 0 (agrees) |
| `conflicts` | `:30` | **0** | 4 |
| `rank_quarantine_handles` | `:40` | **0** | 3 |
| `rank_rules_unresolved_items` | `:44` | **0** | 13 |
| `reconciliation_records` | `:45` | **6** | 6 (agrees) |

Corroborating live reads inside the same file: `typed_labels.stats = {"fail": 0, "hold": 12, "labels": 82}`
(`:2865-2869`, JSON key `hold` = 12 not 15); `era_reconciliation.alias_rows` has **4** rows
(`:137-162`); `era_material_reconciliation.summary = {claims 6, findings 0}` (`:129-134`);
`rank_rules.quarantine = []` and `rank_rules.residuals = []` (zero-length).

`examples/culture-d4/expected-holds.json` — `counts` at `:46-49`:
`{"hold": 12, "note": 0, "fail": 0}`, `holds` = 12 rows all `D2L-FORM-UNRESOLVED`
(no `D2L-RANK` row at all), `notes = []` (`:125`). Live sha256 `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3`,
7,146 bytes — identical to the digest the packet's own §artifact_manifest A-31 row carries.

Live D4 artifact digests (all match the packet's A-28..A-33 manifest rows):
`packet.d4.yml aac91246c…` (101,892 B), `packet.d4.typed.yml d581e0ad5…` (108,251 B),
`typed-labels.d4.yml c23b0ab53…` (82,161 B), `expected-holds.json e6ae9828d…` (7,146 B),
`brief.md 00aa85ff6…` (3,912 B), `ASSEMBLY.md 37b6a98901…` (7,646 B).

## 3. Stale-figure census (line-quoted)

### 3.1 `packet.md:68-69` — the two manifest rows the claim names as already agreeing

```
68 | A-30 | examples/culture-d4/typed-labels.d4.yml | d4 typed-label projection: 82 labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12 findings, 0 unresolved rank items, 4 era-alias rows | c23b0ab532… | 82,161 bytes |
69 | A-31 | examples/culture-d4/expected-holds.json | d4 committed hold set: 12 holds / 0 note / 0 fail, pinned to packet, projection and projector digests | e6ae9828d… | 7,146 bytes |
```

**Verdict: AGREE with live, on every figure and digest.** A-30's `82 / 64 / 12 / 6 / 12 / 0
unresolved` and A-31's `12 / 0 / 0` all match §2. A-30's `4 era-alias rows` matches
`era_reconciliation.alias_rows` length 4. These rows are generated from live bytes by the
renderer, which is exactly why they agree and the carried prose rows do not.

### 3.2 `packet.md:148-152` — the claim_ledger D4 rows

Each of these five rows is generated by the renderer **verbatim** from
`reports/round-20/handoff/claims-map.md` (§4 below). Quoted evidence and verdicts:

**`:148` D4-CL05** — carries four stale figures plus an internal self-contradiction:
> `grounding: …#coverage (typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 16, findings_hold_or_fail 15, label_findings_fail 0) and …#stats (fail 0, hold 12, labels 74)` … statement: `The D4 typed channel types 74 labels — 56 native-form, 12 translated-label, 6 borrowed-strata — and carries 16 findings of which 15 are hold-or-fail (12 label holds, 0 label fails)`

Stale: `74` (live 82), `56` (live 64), `findings_total 16` (live 12), `findings_hold_or_fail 15`
(live 12), `stats labels 74` (live 82), `16 findings` / `15 hold-or-fail` in the statement.
Already live: `translated-label 12`, `borrowed-strata 6`, `label_findings_fail 0`, `hold 12`.
**Self-contradiction inside one sentence**: the row quotes `stats (fail 0, hold 12, labels 74)`
— the live `stats` block reads `hold: 12` yet the same row asserts `findings_hold_or_fail 15`.

**`:149` D4-CL06** — 
> `grounding: examples/culture-d4/expected-holds.json#counts (hold 15, note 1, fail 0) …` … statement: `The committed D4 hold set is 15 holds, 1 note and 0 fails, pinned to the delivered bytes: twelve D2L-FORM-UNRESOLVED holds keyed to each garment twice (record id and slot id) and three D2L-RANK holds, plus one D2L-RANK note for the band-keyed pair`

Stale: `hold 15` (live 12), `note 1` (live 0), `three D2L-RANK holds` (live: none — all 12
holds are `D2L-FORM-UNRESOLVED`), `one D2L-RANK note` (live: `notes` is empty).
Already live: `fail 0`, and the "twelve D2L-FORM-UNRESOLVED holds keyed to each garment twice"
clause. The row is thus internally split: its `#counts` quote is the round-20 hold set and its
row-list clause is the live one.

**`:150` D4-CL07** —
> `…the same file's …#reconciliation_records and …#conflicts counts carry four conflicts without collapsing them` … statement: `… while the reconciliation's own conflicts (4), quarantine handles (3) and reconciliation records (6) are carried as counts rather than collapsed into a cleaner ledger.`

Stale: `conflicts (4)` and `four conflicts` (live `coverage.conflicts` = 0), `quarantine handles (3)`
(live `rank_quarantine_handles` = 0, `rank_rules.quarantine` = []). Already live: `reconciliation
records (6)`; the whole era/material resolution clause (6 records, 0 findings) matches
`era_material_reconciliation.summary`.

**`:151` D4-CL08** — an **extra stale figure not named anywhere in `claims.json`**:
> `… the run evidence is tools/assemble-d4-typed.py --selftest exit 0 with 12/12 checks in a mirror that copies only examples/culture-d4, and the unchanged-foreign-path control is tools/d2-typed-labels.py --selftest exit 0 50/50 plus tools/gates/typed-pipeline-gate.py over examples/culture-d2/packet.d2.typed.yml exit 0 13/13 legs …`

Measured live in this seat: `python3 tools/d2-typed-labels.py --selftest` →
`selftest: 163/163 checks passed … no file outside the temporary directory touched`, exit 0.
So **`50/50` at `:151` is stale** (live 163/163). `12/12` for `assemble-d4-typed.py --selftest`
is still live (re-ran it: `selftest: 12/12 checks passed`, exit 0).
This matters twice over:
1. `claims.json`'s `after_required` says "every claim-ledger/OQ number equal to a measured live
   value" and its thresholds say "zero stale figures … audited against live bytes by two
   independent seats" — but the claim's own `stale_numbers` field enumerates only
   "74/56/16/15", "hold 15 note 1", "conflicts 4, quarantine 3". A verifier working from that
   enumeration will pass a packet that still says `50/50`.
2. The renderer only *requires* `N/N >= minimum` at `tools/exercise-handoff-e2e.py:3468-3473`
   (`v3_selftest_witness`, minima `50` and `12` applied at `:3551-3552`), so `50/50` and
   `163/163` are both "green" to the gate — the stale figure is invisible to the automated
   legs and is exactly the class of staleness claim D exists to close.
   Rewriting this basis must also preserve the `12/12` token: `V3_ALIAS_WITNESS_TOKENS =
   ("era_reconciliation", "12/12")` at `tools/exercise-handoff-e2e.py:1978`, enforced at
   `:2605-2618` (`E2E-UNC` "D4-CL08 is typed supported but its basis lacks the run witness").

**`:152` D4-CL09** —
> `grounding: …#rank_rules_unresolved_items 13 and …#rank_quarantine_handles 3 and …#conflicts 4 in the same file's coverage block; open: the thirteen unresolved rank items, three quarantine handles and four conflicts are inherited D2 normalization residuals …` … statement: `… the packet's coverage block holds 13 unresolved rank items, 3 quarantine handles and 4 conflicts; none of them is promoted, resolved or hidden by this packet, and they are inherited D2 normalization residuals rather than D4 design debt.`

Stale: `13` (live `rank_rules_unresolved_items` = 0), `3` (live `rank_quarantine_handles` = 0),
`4` (live `conflicts` = 0) — in both the basis and the statement.
Note the exact values `13 / 3 / 4` are the **live D2** figures, not merely old D4 ones
(§5.2), so the row's `open:` clause and the phrase "in the same file's coverage block" are
both falsified by the live D4 coverage block, which reads `0 / 0 / 0`.

### 3.3 `packet.md:307` — OQ-V3-05

```
307 | - OQ-V3-05: D4's inherited and own holds stay open: twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts — kotodama; blocking for the affected D2 rank records and the six garment terms, not for this envelope (unresolved claims: D4-CL09)
```

Stale: `three rank holds + one note` (live 0 and 0 — the hold set is twelve
`D2L-FORM-UNRESOLVED` rows and nothing else), `thirteen unresolved rank items`, `three
quarantine handles`, `four conflicts` (live 0/0/0). Already live: `twelve form holds`.
This row is **not** generated from live bytes and **not** carried from the claims-map — it is
a hardcoded literal in the renderer at `tools/exercise-handoff-e2e.py:3524-3532`:

```python
"id": "OQ-V3-05",
"question": (
    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
    "kotodama; blocking for the affected D2 rank records and the six garment terms, not for "
    "this envelope"
),
```

Consequence for the build plan: closing OQ-V3-05 needs a **renderer source edit**, which is a
second shared-file change beyond the two default lines at `:1933-1934`; it must be drafted as
before/after text like the defaults.

### 3.4 Rows that are NOT stale (so the audit can be scoped)

- `packet.md:66,67` (A-28/A-29) — digest and record-count rows match live.
- `packet.md:129` D2-CL01 — `58 labels (46 native-form / 10 translated-label / 2 borrowed-strata), findings_total 16 with 15 hold-or-fail`: matches live `examples/culture-d2/typed-labels.d2.yml#coverage` (`typed_labels 58`, `native-form 46`, `translated-label 10`, `borrowed-strata 2`, `findings_total 16`, `findings_hold_or_fail 15`). **D2 rows are live-green.**
- `packet.md:130,301` D2-CL02 / OQ-V2-03 — `13 unresolved rank items, 3 quarantine handles, 4 conflicts, 10 reconciliation records`: matches live D2 coverage exactly.
- `packet.md:285` — `typed channel 82 labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12 findings (12 hold-or-fail), 0 unresolved rank items, 0 quarantine handles; hold set 12 holds / 0 note`: matches live; it is generated by the renderer from live bytes at `tools/exercise-handoff-e2e.py:3137-3146`. **This is the row that contradicts `:148-152` inside the same document.**
- `packet.md:278-291` — the rest of §validation is renderer-generated (`58 files`, `26 digests`, `16/16`, `20/20`, `27 rows 16/7/4`, `105 links`, `88 edges`) and all match `expected.json`.

## 4. Root cause of the staleness

The D4 ledger rows are not a stale template — they are a **by-design verbatim carry from an
immutable filed artifact**:

- `tools/exercise-handoff-e2e.py:2289-2307` — `v3_parse_claims_map()` reads
  `reports/round-20/handoff/claims-map.md` (constant `CLAIMS_MAP` at `:184`) with `D4_ROW_RE`,
  taking each row's `kind / evidence_status / status / u.basis / links / statement` as text.
- `tools/exercise-handoff-e2e.py:2600-2603` — `v3_build_claim_rows()` appends those 12 rows to
  the ledger unchanged; the only cross-check is the D4-CL08 alias-witness token test (`:2605-2618`).
  **No leg compares any carried number against live bytes.**
- `tools/exercise-handoff-e2e.py:2566` — the renderer's own manifest text calls the file
  "the twelve D4 claim rows as filed; this packet carries them verbatim".

The corresponding source lines still carrying the round-20 figures:

| packet.md line | claims-map.md source | what it carries |
|---|---|---|
| `:148` | `:99` (statement), `:104` (u.basis) | 74 / 56 / 16 / 15 |
| `:149` | `:109` (statement), `:116` (u.basis) | hold 15 / note 1 |
| `:150` | `:121-126` (statement), `:127` (u.basis) | conflicts (4) / quarantine (3) |
| `:151` | `:138` (u.basis) | `--selftest … 50/50` |
| `:152` | `:152-156` (statement), `:158` (u.basis) | 13 / 3 / 4 |
| `:307` | `:251` (OQ table row) | 12 form + 3 rank + 1 note, 13 / 3 / 4 |

`reports/round-20/handoff/claims-map.md` is a filed round-20 byte
(sha256 `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`, 24,888 B, 275 lines)
and per `shared_rules`/non-goals it may not be edited. Therefore **claim D cannot be closed by
re-rendering alone**: the r7 build must override the carried rows (or re-derive them from live
D4 bytes) somewhere in the renderer/plan, and must say so explicitly, or the same six figures
will re-appear verbatim in the new packet.

## 5. Staleness timeline (git, measured from the filed blobs)

| commit | round | `typed-labels.d4.yml` coverage | `expected-holds.json` counts |
|---|---|---|---|
| `e571894` | round-18 | 74 / 56 / 12 / 6, findings 16 (15 h-of), conflicts 4, quarantine 3, unresolved 13 | hold 15 / note 1 / fail 0 |
| `35b6797` | round-20 | identical to r18 | identical to r18 |
| `0e81d9d` | round-22 | 74 / 56 / 12 / 6, **findings 12 (12), conflicts 0, quarantine 0, unresolved 0** | **hold 12 / note 0 / fail 0** |
| `4f09c99` | round-26 | **82 / 64 / 12 / 6**, findings 12, conflicts 0, quarantine 0, unresolved 0 | 12 / 0 / 0 |
| `6c0ac44`,`3b13a2f`,`11df1fd` | 27/28/30 | unchanged from r26 — matches live | unchanged |

Also confirmed against the filed sweep copies: the frozen r27/r28/r31 projections
(`reports/round-27/pinsweep/frozen/r27-post/…`, `reports/round-28/pinsweep/frozen/r28-post/…`,
`reports/round-31/sweep/frozen/r31-post/…`) all read 82 / 64 / 12 and 12 holdings.

So, against the r6 packet frozen at round-30:
- the **conflict / quarantine / unresolved / hold-count** prose has been stale since **round 22**
  (4, 3, 13, 15, 1 all changed then);
- the **label counts** 74/56 have been stale since **round 26** (commit `4f09c99`; the +8 is
  the register-stratum landing, whose own note reads "the stamp register landed in
  04-lexicon.yml (8 register-scoped records…)" — `examples/culture-d4/expected-holds.json:40`;
  74+8=82 and 56+8=64, borrowed-strata and translated-label unchanged).

Honest limit: I read the live and filed blobs at those commits directly; I did **not** verify
*which* round-22/round-26 seat action caused each move (the commits are the evidence, the
cause is `to-verify`).

## 6. Constraints this places on the D block

1. `expected.json` at r6 **already** carries live D4 counts (§1.3), so a naive diff of old-vs-new
   baseline will show almost no D4 count change; the staleness lives only in packet prose.
2. The r7 freeze will change `packet_sha256` even if no claim prose is touched, because the
   rendered §validation text interpolates `V3_BASELINE_DEFAULT` (`:3185`) — the packet will name
   `declared-in-r7`. Plan the freeze after (or in the same step as) the default move, or the
   packet will name a directory that does not yet exist.
3. Rewriting rows `:148-152` requires deciding *where* the live numbers come from. Candidates
   visible in the tree: keep the verbatim carry and post-process (the renderer already mines
   `d4_labels` / `d4_holds` at `:3503-3504`, and the same live values are already rendered at
   `:3137-3146`), or split the row source. This is a renderer-source decision, so its before/after
   text belongs in the D-block drafts alongside the `:1933-1934` defaults.
4. The gate is blind to this class: `handoff-packet-check.py` scans fields/glossary/findings and
   the OLD r6 pair still exits 0 with `fields=16/16, glossary-entries=20, findings=0`
   (`run.log:3`, `freeze.txt:4`) — i.e. shape-green while semantically stale. Any claim-D
   negative control must name the *semantic* class, not the shape class.
5. `50/50` at `:151` is a stale figure the claim's own enumeration omits; whoever writes the
   r7 ledger should fix it and whoever audits should grep for it explicitly.
6. Freshness/`to-verify`: I did not execute any round runner; the only tools I ran were
   `python3 tools/d2-typed-labels.py --selftest` and `python3 tools/assemble-d4-typed.py --selftest`
   (both write only to their own temp dirs and reported "no file outside the temporary
   directory touched").

## Owed

- `reports/round-34/scout/K02-repin-census.md` — K02 owns the full per-surface pin census.
  **Status at this seat's close: that fragment has landed** (25 KB) and it already carries the
  two surfaces a plain `grep declared-in-r6` would miss — its row B1 covers
  `tools/exercise-handoff-e2e.py:3185` and its table row at :161 covers the `:38-40` docstring
  that names **declared-in-r2** (wrong revision, not merely stale). No further action owed;
  recorded here only so the integrator can cross-check rather than re-derive.
- `reports/round-34/depth/D05-packet-draft.md` — the r7 packet bytes themselves; I only
  enumerated the state they must be built from.
- Which round-22 / round-26 seat action moved each D4 figure (I cite the commits, not the
  cause) — `to-verify`.

## Citations

Commands run (working tree, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git log --oneline -3` → `da68a6d`, `139e3b6`, `cdd66d7`
- `git status --porcelain` → `?? reports/round-34/`
- `sha256sum reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json,freeze.txt,run.log}`
- `sha256sum examples/culture-d4/{typed-labels.d4.yml,expected-holds.json,packet.d4.yml,packet.d4.typed.yml,brief.md,ASSEMBLY.md} tools/d2-typed-labels.py`
- `stat -c '%s %n' …` (byte sizes in §1.3, §2)
- `python3 -` + `json.load` over `examples/culture-d4/typed-labels.d4.yml` and
  `examples/culture-d4/expected-holds.json` (coverage, stats, hold-id census)
- `python3 -` + `json.load` over `reports/round-30/handoff/declared-in-r6/expected.json` and `twin.json` (key inventory)
- `python3 tools/d2-typed-labels.py --selftest` → `selftest: 163/163 checks passed …`, exit 0
- `python3 tools/assemble-d4-typed.py --selftest` → `selftest: 12/12 checks passed …`, exit 0
- `sed -n '148,152p' reports/round-30/handoff/declared-in-r6/packet.md` (line-start confirmation)
- `for c in e571894 35b6797 0e81d9d 4f09c99 6c0ac44 3b13a2f 11df1fd; do git show $c:examples/culture-d4/…` (§5 timeline)
- `find reports -maxdepth 4 -name 'declared-in-*' -type d`; `ls -la` per revision dir
- `python3 -` over `reports/round-{27,28,31}/*/frozen/*/inputs/examples/culture-d4/typed-labels.d4.yml`

File:line references:

- `tools/exercise-handoff-e2e.py:1-98` (docstring: profile contract, read sets, assertions)
- `tools/exercise-handoff-e2e.py:34,38-40,57,184,1930-1934,1935-1959,1960-1975,1978,2289-2307,2566,2599-2616,2600-2603,3137-3146,3185,3468-3473,3502-3512,3524-3532,3542-3551,3978-4124,4149,4488,4561`
- `reports/round-30/handoff/declared-in-r6/packet.md:66,67,68,69,129,130,148,149,150,151,152,285,295,301,307`
- `reports/round-30/handoff/declared-in-r6/{freeze.txt,run.log}` (whole files, 6 and 14 lines)
- `reports/round-30/handoff/declared-in-r6/expected.json` (key inventory; `counts`, `links`, `uncertainty`)
- `reports/round-20/handoff/claims-map.md:99,104,109,116,121-127,138,152-158,251`
- `examples/culture-d4/typed-labels.d4.yml:29-47,129-134,137-162,2865-2869`
- `examples/culture-d4/expected-holds.json:2-6,40,46-49,125`
- `examples/culture-d2/typed-labels.d2.yml` (coverage block, for the D2/D4 contrast)
- `reports/round-22/handoff/declared-in-r2/freeze.txt:1-4`;
  `reports/round-25/v3-supersession/declared-in-r4/freeze.txt:1-2`;
  `reports/round-26/handoff/declared-in-r5/freeze.txt:1-4`
- `reports/round-34/claims.json:24-36` (claim D before/after/thresholds),
  `reports/round-34/targets.json:14` (K01 mission), `:5-12` (`shared_rules`)
