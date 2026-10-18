# X21 — spot-check audit: the round-20 handoff v3 claims, re-derived

- round 20 (operator loop 2 of 3, build round 4 of 4; 64 workers on
  `opencode-go/deepseek-v4.1-flash`) · seat **X21** (SCRIBE X21..X22 —
  spot-check auditors: v3 claims + README rows) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X21..X22: spot-check auditors (v3 claims +
  README rows)." This file is the v3-claims leg; the README-rows leg is
  `x22-readme-rows-spotcheck.md`.
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  declared baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`, HEAD
  `122086b` plus the live round-20 working tree.
- canon: NON-CANON engineering evidence. This audit admits no claim, certifies
  no round, and is not a lore receipt or a clearance.
- writes: **this file only**; read-only instruments and receipts under
  `.scratch/` (`TMPDIR=$PWD/.scratch` exported). The round's counting command
  was run only in its read-only `--check` mode, which writes no
  `validation.json` (round-14 lesson: a counting command can itself be a
  writer).
- measurement window 12:56Z–13:23Z UTC. Pins (all measured at the stamps
  below): exercise `81dba418c81b25916b0760a843f4d11266398bf1ac180cc75da462a21e337059`,
  v3 baseline `40ba13de89002bea5d3e891671ec5d0c5df9a7fca0d52d19f572e4c3620b50de`,
  packet `packet-v3-16.md` `9f37c08af9bd56fce668ccb42bd34351d21e650c49e27898ff7736a70dfdd730`,
  runner revision `d6fee0cea8ac5ef45f524dd2fe89b0321c44bf3c4c939bf78857e6864a191e4d`
  (it moved twice more during the window — X21-N2). A later write to any
  pinned surface invalidates the reading that names it.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the delivered exercise runs green: exit 0, `16/16 + 20/20 + 0`, links `61/61`, packet `6de822f4…` | **PASS** |
| 2 | the exercise selftest control matrix green: positive run + 22 controls | **PASS** |
| 3 | the v3 packet document gate-clean: exit 0, `fields=16/16 glossary-entries=20 findings=0` | **PASS** |
| 4 | the packet's 27 claim rows parse; 51/51 basis locators and 102/102 links resolve; 0 duplicate/short bases | **PASS** |
| 5 | v2-subset equality re-derived by this seat: 15/15 carried rows equal, field by field | **PASS** |
| 6 | every D4 claim's cited measurement re-derived against live D4 bytes | **PASS** (12/12 rows, §4) |
| 7 | v2 paths unchanged: filed digests identical to the 12:56Z pre-state; successor replay green | **PASS** |
| 8 | the O evidence the D4-CL08 flip rests on | **PASS** (§5) |
| 9 | the round runner (read-only `--check`, revision `d6fee0ce`): acceptance true, C/D/O all pass | recorded |
| 10 | census divergence: exercise assembles 24 claims (9 D4) vs the packet document's 27 (12 D4) | **finding X21-F1** |
| 11 | the runner's live census comparison is inert (the exercise summary carries no `claims=` token) | **finding X21-N3** |

## 1. Method (independent instruments)

Every reading below was re-run from this seat, not read from a peer receipt:
my own claim-ledger parser (`.scratch/x21-claims-audit.py`), a v2-subset
comparator (`.scratch/x21-v2-subset.py`), a D4 measurement re-derivation
(`.scratch/x21-d4-recheck.py`, validated against the D seats' own counts), and
the lane's own tools (gate, harness validators, projector, adapter,
typed-pipeline gates). The instruments were calibrated before use: the claim
parser reproduces the round-15 audit's published v2 readings exactly (15
claims, 8/5/2; 23/23 basis locators; 50/50 links).

Pre-state controls captured at 12:56Z, before the wave touched anything:
`tools/exercise-handoff-e2e.py` `a21934ad…` (0 `culture-d4` mentions); the
filed v2 digests (below); the v2 exercise run green (exit 0, 8/8 checks,
`16/16 + 20/20`, packet `6583b6bd…`); D4 digests (packet `e7ecd204…`,
typed-labels `a59990bb…`, expected-holds `09490a27…`, typed packet
`f63ed531…`).

## 2. The delivered exercise surface (claim D's computational leg)

Pinned revision `81dba418…` (byte-stable across its freeze, per
`reports/round-20/handoff/frozen.md` §1):

| command | observed |
|---|---|
| `python3 tools/exercise-handoff-e2e.py --quiet` | exit 0; `handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 links=61/61 packet_sha256=6de822f4ed8c7269225e216dc3f1ce9b07a483a2ab2ce4f3646cf02ef9950a2f` |
| `python3 tools/exercise-handoff-e2e.py --selftest` | exit 0; `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=61/61, statuses=14/7/3) plus 22 controls` |
| `python3 tools/harness/packet_uncertainty.py --packet reports/round-20/handoff/twin.json --require-oq` | exit 0; `claims=24 findings=0` |
| `python3 tools/harness/packet_links.py --packet reports/round-20/handoff/twin.json` | exit 0; `links=61 resolved=61 findings=0` |
| v2 successor replay (`reports/round-15/handoff/frozen-verify.py --baseline reports/round-20/wart/expected-v2-07-r20.json`) | exit 0; `v2: exit=0 fields=16/16 glossary=20/20 findings=0 claims=15/15 statuses={supported 8, unresolved 2, partial 5} links=50/50 packet_sha256=24f9dd39bdad…` |

The frozen baseline (`reports/round-20/handoff/expected.json`, `40ba13de…`)
pins 42 input digests, `claims 24`, `d4_claims 9`, `uncertainty {supported 14,
partial 7, unresolved 3}`, `links 61/61`, `edges 48` (`d4_edges 14`), gate scan
`16/16 + 20/20 + 0`, and the packet/twin digests above. The freeze seat's
tamper matrix (9/9 controls) is filed in `frozen.md` §3; this seat did not
re-run it and does not count it as its own evidence.

## 3. The v3 packet document (claim D's document leg)

`reports/round-20/handoff/packet-v3-16.md` `9f37c08a…` (the newest keyed
build; builds 13–16 all parse to the same ledger):

- gate: `python3 tools/gates/handoff-packet-check.py reports/round-20/handoff/packet-v3-16.md`
  → exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0`.
- my parse: **27 rows** — the 15 v2 rows carried and 12 D4 rows
  (`D4-CL01…D4-CL12`); statuses **16 supported / 7 partial / 4 unresolved**;
  **51/51** basis locators resolve; **102/102** links resolve; 0 duplicate
  bases, 0 short/boilerplate bases.
- **v2-subset equality, re-derived by this seat**: the 15 v2 rows parsed from
  `packet-v2-05.md` and from `packet-v3-16.md` are equal field by field
  (`claim_id, kind, evidence_status, status, basis, links` after whitespace
  normalization; the v2 merged `uncertainty` cell re-merged from the v3
  `uncertainty_status`/`uncertainty_basis` columns) → **15/15 equal, 0
  mismatches** (`.scratch/x21-v2-subset.py`).
- the contract-audit re-run artifact `reports/round-20/handoff/audit-v3.md`
  (`10f09b9b…`) is the runner's chosen audit surface and classifies
  `pass-with-named-gaps` (leading verdict "PASS-with-named-minors on the
  audited build"), with the bilateral contract read named as the open gap and
  its owner; the runner's own `contract_audit` measurement reads the same.
  The audit's F-A1 (character-split `links` cells) was measured against bytes
  that no longer exist at that path — see X21-N1.

## 4. The D4 claims re-derived against live bytes (§7-style spot-check)

Reference bytes at 13:19Z: `packet.d4.yml` `e7ecd204…`, `typed-labels.d4.yml`
`cbcf997f…` (post-O; superseded `a59990bb…`), `expected-holds.json`
`09490a27…`, `packet.d4.typed.yml` `f63ed531…`. My re-derivation
(`.scratch/x21-d4-recheck.py`, post-O receipt
`.scratch/x21-post-o-d4-recheck.json`) reproduces every cited number:

| claim | cited measurement | re-derived from bytes |
|---|---|---|
| D4-CL01 | non-canon boundary; twelve authored inputs; registry `C-01` | `packet.d4.yml:2` `canon: "not canonized (D4 NON-CANON design drill)"`; `brief.md` §non-canon block; `01-brief.yml` registry lists 12 components |
| D4-CL02 | `era_records` ER-01..ER-04 on E0..E3; ER-04 reserved; no dates | `named_eras` 4 rows (`the stamp era` E0 … `the cold fire (reserved)` E3); `era_records` block present; brief declares tags fixture-relative |
| D4-CL03 | `rank_rules` RK-01..RK-04 with authority/jurisdiction/eras/property/wearer ranks | 4 rank-rule records; `costumes` 6 garment rows carry `wearer_ranks`; evidence `design-choice` |
| D4-CL04 | six unfilled `form_slots` `LEX-GAR-01…06`; gloss is a translated label; sixth slot's owed kind conditional | 6 slots, all `status: "unfilled"`, `kind_owed` native-form ×5 + borrowed-strata ×1; labels_by_kind translated-label 12 |
| D4-CL05 | 74 labels (56/12/6); 16 findings, 15 hold-or-fail; byte-identical projection | `coverage` block identical; `stats {fail 0, hold 12, labels 74}`; D4 gate exit 0 `byte-identical deterministic projection` |
| D4-CL06 | holds `{15, 1, 0}`; 12 form holds + 3 rank holds; +9 delta documented | `expected-holds.json counts {hold 15, note 1, fail 0}`; rows 12 `D2L-FORM-UNRESOLVED` + 3 `D2L-RANK`; one `D2L-RANK` note |
| D4-CL07 | six era/material records; 0 findings; 4 conflicts carried | `era_material_reconciliation.summary {claims 6, findings 0}`; `coverage.conflicts 4`, `reconciliation_records 6` |
| D4-CL08 | alias leg family-local; D2 component no longer named; run evidence | `era_reconciliation.basis` now `examples/culture-d4/packet.d4.yml named_eras (A1)` + the explicit skip row; adapter mirror holds no `culture-d2`; see §5 |
| D4-CL09 | D2 rank rows re-carried `cannot-evaluate`; 13 unresolved, 3 quarantine, 4 conflicts | `coverage.rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`, `conflicts 4`; 13 `act_rules` all `cannot-evaluate` |
| D4-CL10 | loan ledger complete as declared; donor stage/fibre/donor speech unmodelled `(to-verify)` | three `to-verify` packet lines (donor_stage, fibre, donor speech) |
| D4-CL11 | no real-language sweep / consultation / rights ruling claimed | screening statement present in the packet's D4 block; no clearance asserted |
| D4-CL12 | D4 culture rides as namespaced candidates only | subject refs `cand:kotodama.d4.*`, all unresolved |

No D4 row overstates its evidence on this pass; every cited number survives
re-derivation. The 16-finding set is unchanged by the O change (fail 0 / hold
15 / note 1 before and after).

## 5. The O evidence the D4-CL08 flip rests on

The packet types D4-CL08 `supported` on the per-family resolution landing. This
seat re-measured the evidence independently:

| leg | command | observed |
|---|---|---|
| D2 byte path unchanged | `python3 tools/d2-typed-labels.py --check`; `python3 tools/gates/typed-pipeline-gate.py` | exit 0 `byte-identical deterministic projection`; exit 0 `16/16 legs passed` |
| D4 pipeline | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0 `19/19 legs passed` |
| projector controls | `python3 tools/d2-typed-labels.py --selftest` | exit 0 `50/50 checks passed` (was 39/39 pre-O) |
| adapter without the foreign tree | `python3 tools/assemble-d4-typed.py --selftest`; source read | exit 0 `12/12 checks passed`; the mirror no longer copies `examples/culture-d2` (comment + code at `tools/assemble-d4-typed.py:433-441`); the runner independently reads `foreign_tree_copy_in_adapter: false` |
| live pins | `tools/gates/typed-pipelines.json`; runner `O.pins` | projector `76536a92…`, projection `cbcf997f…` pinned == live; `advisory_stale_pins: []`; the superseded `a59990bb…` is named, not silently replaced |

The `expected-holds.json` internal `projector_sha256`/`projection_sha256` still
name the round-19 values; the O receipt (`reports/round-20/wart/repin-r20.json`)
records this as a named drift and the live pins live in `typed-pipelines.json`.
This audit confirms both statements and treats the drift as declared, not
silent.

## 6. v2 paths unchanged (filed digests, re-measured at 13:20Z)

| filed surface | pre-state (12:56Z) | at 13:20Z |
|---|---|---|
| `reports/round-15/handoff/packet-v2-05.md` | `24f9dd39…` | `24f9dd39…` |
| `reports/round-15/handoff/packet-v2-05.yml` | `39cf4d53…` | `39cf4d53…` |
| `reports/round-15/handoff/expected.json` | `b927db31…` | `b927db31…` |
| `reports/round-11/handoff/expected.json` | `a94f9ded…` | `a94f9ded…` |

plus the v2 successor replay green (§2) and the v2-subset equality (§3). The
v2 path is unchanged and green on every surface this seat can measure.

## 7. Findings and notes

- **X21-F1 — census divergence (corroborates `frozen.md` F1).** The exercise
  assembles **24 claims (9 D4 rows, `D4-CL01…D4-CL09`)** and its baseline pins
  `statuses {14, 7, 3}`; the packet document carries **27 claims (12 D4 rows)**
  with `statuses {16, 7, 4}`; the design targets 27 / `{15, 7, 5}`; the
  runner's own selftest fixture still names `claims=27 statuses=15/7/5`.
  Neither surface is wrong on its own terms — the exercise proves what it
  assembles and the document renders the full claim map — but a consumer that
  reads the document's 27 rows and the tool's 24 will find no single census
  statement. Owner: the impl seat (tool) + the packet seat (document). This
  audit pins the delivered behaviour rather than the design's intent.
- **X21-F2 — the CLI has no `--profile` flag** (corroborates `frozen.md` F2).
  The design §6 and the runner's earlier revisions invoke `--profile v1/v2/v3`;
  the delivered CLI is single-profile (`kotodama-handoff-e2e/3`, default
  baseline `reports/round-20/handoff/expected.json`). Later runner revisions
  (including the `d6fee0ce` this seat ran) detect the absence and measure the
  default run plus the v2 successor replay instead — so the delivered pair is
  self-consistent; the design text is the stale surface.
- **X21-N1 — a keyed build moved in place.** `packet-v3-13.md` was audited by
  R20-D17 at sha `3ce440d5…` (13:11–13:13Z); by 13:13:14 the same path held
  `5b3b8ae6…`, in which the audit's F-A1 (character-split `links` cells) is
  gone. The repair is real, but a keyed build whose bytes move is not a stable
  consumer surface; the runner's build-rank discovery currently reads the
  newest key, which mitigates it for the runner only.
- **X21-N2 — the runner itself moved during the audit** (`4eeb9f4f` →
  `d6fee0ce` → `6da4f7ed` measured inside ~3 minutes). The runner reading in
  §0/§9 binds to `d6fee0ce`, verified byte-stable across the `--check` run.
- **X21-N3 — the runner's census cross-check is inert.** The runner compares
  the packet's row count to the exercise census only when the exercise summary
  line carries a `claims=` token; the delivered line carries none, so the
  comparison never fires (`expected_rows = 0`) and F1 passes unchecked by the
  round's own runner.
- **X21-N4 (out of seat scope, reported).** The exercise's summary line also
  omits the design's `statuses=`, `v2_subset=` and `alias_leg=` tokens; the
  runner's marker-based checks cover the same ground, but the design §6 summary
  contract and the delivered line have diverged.

## 8. Limits

- **Same-convention.** The v2-subset comparison re-merges the v2 uncertainty
  cell into the v3 split columns by the lane's own convention; a reader using a
  different normalization could get a different (defensible) reading.
- **Correspondence, not truth.** This audit re-derives what the bytes say; it
  certifies no claim's truth, no canon standing, no lore receipt, and no
  clearance.
- **Point-in-time.** The wave was live throughout (13:20Z onward: the runner,
  the packet builds and the D fragments were still moving). Every reading
  binds to the digest named beside it; the round's own counting command and
  the integrating parent retain the final verdict.

### 2026-10-18T13:25Z — post-stamp movement

Measured at this stamp, after the audit's readings were taken:
`tools/exercise-handoff-e2e.py` moved `81dba418…` → `84e2fbf1…` → `67abf063…`
(the impl seat is rewriting the ledger build to read
`reports/round-20/handoff/claims-map.md` — `CLAIMS_MAP` at line 177 — which, if
it lands, converges the exercise's D4 claim set toward the packet's twelve; in
the intermediate revisions a `--quiet` run exits 0 printing no summary line);
`reports/round-20/run-validation.py` moved `d6fee0ce…` → `6da4f7ed…`;
`corpus/README.md` moved `a20b6b26…` → `1a359d55…`. Unchanged at this stamp:
the v3 baseline `40ba13de…`, the packet builds 13–16 (13 still `5b3b8ae6…`),
the filed v2 digests of §6, and the D4 artifact digests of §4. Every reading in
this file binds to the digest named beside it; **X21-F1 should be re-measured
after the impl rewrite settles**, and the freeze's re-pin (if the rewrite lands)
is a new baseline row, never an in-place edit. A re-run of §2–§3 on the settled
tree is the next seat's business.

### 2026-10-18T13:30Z — the O re-pin cascade reached further (supersedes §4/§5 pins)

Measured at this stamp, after §4/§5 were written:

| surface | at §4/§5 stamp | at 13:30Z | reading |
|---|---|---|---|
| `examples/culture-d4/expected-holds.json` | `09490a27…` | `18d0cfce…` | pins moved to projection `cbcf997f…` / projector `76536a92…` with a `revision_note` and `supersedes_pins`; counts unchanged `{hold 15, note 1, fail 0}` |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5…` (repin receipt) | `7b9439c4…` | projector pin moved with a revision note; packet/projection pins unchanged |
| `examples/culture-d4/packet.d4.typed.yml` | `f63ed531…` | `e823db67…` | rebuilt (the projection change propagates); `assemble-d4-typed.py --check` exit 0 `byte-identical deterministic typed packet` |
| `tools/assemble-d4-typed.py` | `1ddad6a7…` | `92f5460b…` | the selftest mirror no longer copies `examples/culture-d2`; `--selftest` 12/12 |

Live pin channel re-verified: every `typed-pipelines.json` pin (packet,
assembler, projection, adapter) equals the live bytes; D4 pipeline 19/19 and D2
pipeline 16/16 green; D2 `--check` byte-identical. New receipts:
`tools/gates/frozen/round-20/repin-d2/`, `reports/round-20/repin/O11…O14`. The
§5 sentence "the internal pins still name the round-19 values — a named drift,
not edited here" described the state at 13:19Z; the seats subsequently edited
those pins **as new rows with revision notes and `supersedes_pins`**, which is
the discipline the rules require. The D4 claim numbers re-derived in §4 are
unchanged on the new bytes (coverage 74/56/12/6, findings 16, holds
`{15,1,0}`, era basis the packet's own `named_eras` + the documented skip).
