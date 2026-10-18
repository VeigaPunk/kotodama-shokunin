# R20-D review — the v3 D4 claim-set design, verified against live bytes

- topic: An independent-style review of `design.md`, `claims-map.md` and
  `uncertainty-plan.md` as filed: what was measured, what the measurements
  support, which controls fire when a witness is removed, and what a second
  reader must still re-run. This is a **review record**, not a receipt for the
  v3 packet, the O claim, or the audit re-run — none of those exists yet, and
  this file claims none of them.
- scope: the three design files under `reports/round-20/handoff/`, read against
  the live repo bytes on 2026-10-18. No file outside `reports/round-20/handoff/`
  was written by this seat; scratch lives under `.scratch/r20d/`
  (`TMPDIR=$PWD/.scratch` before every scratch-writing command). The O seat's
  alias bytes moved in the working tree during this filing (HEAD
  `caf1beac…` plus uncommitted edits); §4 records the flip measurement and its
  provenance.
- sources: `examples/culture-d4/**`, `reports/round-18/d4/**`,
  `reports/round-19/validation.json`, `tools/harness/packet_links.py`,
  `tools/harness/packet_uncertainty.py`, `tools/assemble-d4-typed.py`,
  `tools/d2-typed-labels.py`, `tools/gates/typed-pipeline-gate.py`,
  `tools/gates/handoff-packet-check.py` (read only, not run over a packet that
  does not exist), the round-15 v2 surfaces for the delta baseline.
- verified-at: 2026-10-18, lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` plus the O seat's
  uncommitted alias edits.
- recheck: after the packet seat renders `packet-v3-*`, after the O seat's
  bytes are committed (the flip is evidence-keyed and symmetric), and before
  the v3 baseline is frozen.

## 1. Verdict

**The design is internally consistent and its witnesses are real, with three
limits stated rather than papered over.** Every D4 fact the three files assert
was re-read from the delivered bytes; every link spec the claims-map files was
resolved by the lane's own resolver; every claim row was re-extracted from the
markdown and validated by the lane's own uncertainty validator with zero
findings; and each of the seven mutations that removes a required element fires
its stable code. The limits: (a) no v3 packet exists, so nothing here is
evidence that the *packet* will pass — only that its planned rows validate in
isolation; (b) the round-19 alias wart's flip condition is **met by measured
runs** (§4) and `D4-CL08` is therefore typed in its landed form — but the O
seat's own receipts (battery, d2/d3/d4 gate set) are theirs to file, and a
revert of their uncommitted bytes re-flips the row; (c) the D4 receipt rows the
design cites are read as evidence, not re-derived (this seat ran no D4 gate
over the D4 artifacts themselves).

## 2. Measurements (commands and observed results, 2026-10-18)

| # | command (lane root; `TMPDIR=$PWD/.scratch`) | observed |
|---|---|---|
| 1 | `python3 tools/harness/packet_links.py --links "<48-spec draft list>"` | exit 0, `links=48 resolved=48 findings=0` |
| 2 | re-extract the twelve rows' link lines from `claims-map.md`, then `python3 tools/harness/packet_links.py --links "<46 unique specs>"` | exit 0, `links=46 resolved=46 findings=0` |
| 3 | `python3 tools/harness/packet_links.py --links "<18 record-id specs from the coverage map>"` | exit 0, `links=18 resolved=18 findings=0` |
| 4 | re-extract the twelve rows from `claims-map.md` (statement, kind, evidence status, status, basis, links) → `python3 tools/harness/packet_uncertainty.py --claims-json … --json` | exit 0, `claims=12 findings=[]`; pre-flip census 7 supported / 2 partial / 3 unresolved; kinds 7 designer interpretation / 3 generative rule / 1 screening statement / 1 candidate world-fact |
| 5 | read `examples/culture-d4/packet.d4.yml` block ids | 153 distinct namespaced ids over 22 families + 14 contract rules `RG-01..RG-14`; 6 costumes with `form_slot`, 6 with `material_ref`, 4 rank rules with `wearer_ranks`, 4 era records with `costume_seam`; three `to-verify` lines (957 `donor_stage`, 1557 `composition`, 2266 `donor`) |
| 6 | read `examples/culture-d4/typed-labels.d4.yml` (pre-flip, 09:5xZ) | `coverage`: typed_labels 74, labels_by_kind 56/12/6, findings_total 16, findings_hold_or_fail 15, label_findings_fail 0, label_findings_hold 12, rank_rules_unresolved_items 13, rank_quarantine_handles 3, conflicts 4, reconciliation_records 6; `stats {fail: 0, hold: 12, labels: 74}`; 74 label rows (62 supplied / 12 to-verify); 13 `act_rules`, all `cannot-evaluate`; `era_reconciliation.basis[0]` named `examples/culture-d2/components/12-rank-rules.yml era_aliases (A1)` |
| 7 | read `examples/culture-d4/expected-holds.json` | `counts {hold: 15, note: 1, fail: 0}`; by id `D2L-FORM-UNRESOLVED` ×12, `D2L-RANK` ×3; one note at `SR-01#a|SR-01#b` |
| 8 | read `examples/culture-d4/components/01-brief.yml` | `contract.hold_set_declaration`: six holds, `counts {hold: 6, note: 0, fail: 0}`, acceptance criterion `A-07` requiring equality with the emitted set — the +9/+1 delta D4-CL06 grounds |
| 9 | `sha256sum`-equivalent read of the four delivered D4 artifacts (pre-flip) | `packet.d4.yml e7ecd204…`, `typed-labels.d4.yml a59990bb…`, `packet.d4.typed.yml f63ed531…`, `expected-holds.json 09490a27…` (matching the pins in the round-18 receipts) |
| 10 | read `tools/check-gate-battery.py` | `REGISTERED_GATE_NAMES` = seven structural gates + the two D4 adapters (nine) — the `9/9` the design's validation row cites |
| 11 | read `tools/assemble-d4-typed.py` selftest (pre-flip) | the mirror copied `examples/culture-d2` with the wart comment — the second measured location of D4-CL08's then-open element |
| 12 | `python3 tools/harness/packet_links.py --selftest` / `packet_uncertainty.py --selftest` | not re-run by this seat; the round-15 audit and round-18 receipts record both green. **To-verify for the packet seat** |
| 13 | re-measure the live D4 projection counts after the O edits | identical to #6: 74 labels 56/12/6, coverage block byte-equal, `stats` equal, `findings_total` 16, `era_material` summary equal — only the era-reconciliation block changed (`alias_rows` 10 → 4; basis rewritten) |
| 14 | read the live `era_reconciliation.basis` | `"examples/culture-d4/packet.d4.yml named_eras (A1)"`, `"examples/culture-d4/packet.d4.yml era_reconciliation: skipped — the packet declares no reconciliation rows (the D2 leg's examples/culture-d2/components/11-costumes.yml is not read for family d4)"` |
| 15 | `python3 tools/assemble-d4-typed.py --selftest` (mirror copies only `examples/culture-d4`) | exit 0, `selftest: 12/12 checks passed — build/determinism/--check/tamper plus stale-projection, coverage-gap and malformed-packet controls` |
| 16 | `python3 tools/d2-typed-labels.py --selftest` | exit 0, `selftest: 50/50 checks passed` (the round-18/19 receipts record 39/39 at the earlier revision — the O seat extended the matrix) |
| 17 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml` ×1, stdout hashed | exit 0, `summary: 13/13 legs passed`; stdout sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` — **equal to the round-18 pre-generalization baseline** in `reports/round-18/d4/determinism.md` §2, so the D2 output bytes did not move |
| 18 | `git status --porcelain examples/culture-d2/` | empty — the D2 artifacts are untouched |
| 19 | **post-flip re-validation** (after the D4-CL08 row was re-typed): re-extract the twelve rows from the updated `claims-map.md` → `packet_uncertainty.py --claims-json … --json`, then `packet_links.py --links "<48 unique specs>"` | uncertainty exit 0, `claims=12 findings=[]`, census **8 supported / 2 partial / 2 unresolved**; links exit 0, `links=48 resolved=48 findings=0` |

## 3. Controls — what fires when a witness is removed

Every claim row's basis names a witness; each witness has a mutation that must
make a stable code fire. Measured this pass:

| control | mutation | observed |
|---|---|---|
| duplicate basis | copy `D4-CL01`'s basis onto `D4-CL02` | exit 1, `U-BASIS-DUPLICATE` |
| `partial` without a bound | `D4-CL04` basis with the `restriction:` clause removed | exit 1, `U-BASIS-NO-RESTRICTION` |
| `unresolved` without an owner | an `unresolved` row's basis with `owner:` removed | exit 1, `U-BASIS-NO-OWNER` |
| off-vocabulary status | a row's status set to `tentative` | exit 1, `U-STATUS-VOCAB` |
| thin/placeholder basis | a row's basis `grounding: unknown` | exit 1, `U-BASIS-SHORT` |
| dangling token selector | `packet.d4.yml#ER-99` | exit 1, `L-TOKEN-MISSING` |
| dangling block selector | `typed-labels.d4.yml#no_such_block` | exit 1, `L-TOKEN-MISSING` |

Design-level controls that are specified but not yet measurable (they need the
v3 packet): the v2-subset equality mutation (m8), the glossary-count mutation
(m9), the canon-trap basis mutation (m10), and the wart-flip guard (m11). They
are named in `design.md` §6 and must be *run*, not asserted, by the impl seat.

## 4. The alias-wart check — flip condition met, measured and controlled

The round-19 routed wart: the projector's era-alias leg required the D2 alias
component even for D4 packets. The design made `D4-CL08` evidence-keyed
(`design.md` §4) with a four-part control set. All four legs were measured:

1. **D4-side basis** — the live projection's `era_reconciliation.basis` names
   the D4 packet's own `named_eras` and an **explicit documented skip**
   ("the packet declares no reconciliation rows (the D2 leg's … is not read for
   family d4)"), and `alias_rows` fell from 10 (all D2-derived) to 4. Measured
   by reading the live bytes (#14).
2. **The run without the foreign tree** — `tools/assemble-d4-typed.py
   --selftest` builds a mirror that copies only `examples/culture-d4` (the
   selftest's `shutil.copytree` of `examples/culture-d2` is gone from the live
   bytes) and reports **exit 0, 12/12 checks passed** (#15). This is the run
   the flip rule demands: a d4 path that works with no D2 tree present.
3. **The foreign path unchanged** — the D2 control is byte-identical:
   `tools/d2-typed-labels.py --selftest` exit 0 50/50 (#16), and the D2 typed
   gate exits 0 with stdout sha256 `9a69985a…` equal to the round-18
   **pre-generalization** baseline (#17); `examples/culture-d2/` is untouched
   (#18). A resolution that moved the D2 bytes would not be evidence for this
   claim.
4. **The negative control** — the same d4 run with the D2 tree restored must
   still exit 0 (a fix that makes the d2 path depend on the d4 tree is a
   regression). This leg belongs to the O seat's own receipts; **to-verify**
   until the O claim files it, and the audit seat should demand it.

Provenance and limits of this flip: the O bytes were **uncommitted working-tree
edits** at measurement time (HEAD `caf1beac…`), so the row is typed in the
landed form on the strength of measured live behaviour, not of a commit; the O
claim's own gate-set receipt (battery, d2/d3/d4 runs) is still owed; and the
rule is symmetric — if the O bytes are reverted, `D4-CL08` re-flips to
`unresolved`, `OQ-V3-04` re-opens in a new build, and the census returns to
15/7/5.

## 5. Cross-check against the D claim's `after_required`

| requirement (round-20 D claim) | covered by this design | still owed by |
|---|---|---|
| "v3 assembles a handoff packet from D2+D3+D4 artifacts" | §6 profiles, read set, manifest delta | impl + packet seats |
| "D4 claims enter the claim ledger with uncertainty {status,basis}" | `claims-map.md` §1 (12 rows, validator-clean as filed) | packet seat renders; audit re-derives |
| "claim-to-record links resolve into culture-d4 records" | 46/46 link specs + 18/18 coverage ids resolved | packet seat carries the specs verbatim |
| "handoff-packet-check 16/16 + 20/20" | §5 target, glossary-stays-D3 rule, m9/m10 controls | impl + packet seats run the gate |
| "contract-v2 audit re-run yields pass-with-named-gaps or better" | §7 expected verdict + named remainders | audit seat |
| "v2 paths unchanged and green" | §0 read-only rule + §6 v2-subset equality control | impl seat (m8), freeze seat (v2 baseline untouched) |
| "the wart closed" (O claim's subject) | the design's flip rule + this section's measured legs 1–3 | O seat: the negative control (leg 4) and its own gate-set receipts; audit seat: verify |

## 6. Limits, hazards for the packet seat, and to-verify

- **No packet was built and no gate was run over one** by this seat; the
  `16/16 + 20/20` target is a declared expectation with a control, not a
  measured verdict.
- **Hazard — resolver branch on `.yml`-suffixed JSON**: `typed-labels.d4.yml`
  is JSON bytes with a `.yml` suffix, so the resolver treats an `L<n>`-shaped
  selector as a **line anchor** (its JSON branch keys off the `.json` suffix).
  No D4 link spec in `claims-map.md` uses an `L<n>` selector for that file;
  the packet seat must keep it that way and prefer block tokens
  (`#coverage`, `#stats`, `#era_reconciliation`).
- **Hazard — generated packet lines move**: `packet.d4.yml` is regenerated by
  `tools/assemble-culture-d4.py`; line anchors would drift on a rebuild. The
  design therefore uses record-id tokens (`#ER-01`, `#L-49`) and only cites
  line numbers in prose (`design.md` §8.8), never as selectors.
- **Hazard — canon-verb traps**: the gate's traps reach basis cells
  (round-15 probes C1/C2). The twelve bases were written to avoid
  `certif/establish/grant/award … canon` spans and the
  "this packet … is canon" shape, but the packet seat must re-run the gate
  rather than trust this reading (control m10).
- **Hazard — the D4 bytes are moving in this wave**: `typed-labels.d4.yml` is
  an O-seat edit surface this round. The packet seat must pin the D4 digests
  **after** the O bytes stop, and re-run the §4 legs on the pinned revision
  before freezing; a D4 byte that moves after the freeze re-pins as a new row.
- **To-verify (packet seat)**: the live pair counts and record-id total at
  build time; the census on the frozen revision; whether the round-18 receipts
  are manifest rows or claim links only (`design.md` §9 leaves it to the seat
  with a recorded reason).
- **To-verify (audit seat)**: re-resolve the basis-inline locators (the
  validator does not), re-derive the census from the rendered ledger rather
  than from `expected.json`, and demand the O seat's negative control (§4 leg 4).
- This review's own footprint: `reports/round-20/handoff/review.md` plus
  gitignored scratch under `.scratch/r20d/` (`counts.txt`,
  `d4-inventory.txt`, `claims-d4.json`, `claims-from-md.json`,
  `claims-final.json`, `claims-final2.json`, `file-check.txt`,
  `file-level-control.txt`, `final-control.txt`). No filed round-8..19
  artifact, corpus file, tool, packet or sibling path was written.
