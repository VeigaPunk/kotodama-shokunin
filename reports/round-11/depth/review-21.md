# R11-D21 — hold-set completeness re-derivation, by hand, from the D2 typed-label pipeline

- seat: **R11-D21** (adversarial reviewer, hold-set completeness), round 11 (loop 1 of 3,
  build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D21 (reviewer): hold-set completeness re-derivation by
  hand from tools/d2-typed-labels.py selftest output; divergence = finding;
  reports/round-11/depth/review-21.md."
- writes: this file only, plus in-lane scratch under `.scratch/` (`TMPDIR=$PWD/.scratch`).
  No tool, gate, packet, component, projection, baseline or earlier-round byte is edited.
  `reports/round-{8,9,10}/**` and `tools/gates/{frozen,expected}/**` are read-only here.
- clock: stamps UTC (`date -u`); local time is UTC-03:00.
- revision measured: `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (= `e3ef171`, the round-11
  claims commit); measurement window 2026-10-17T22:01–22:07Z.
- scope guard: this is NON-CANON engineering review. Nothing here admits a round, a
  capability or a canon fact. Canon, rights and gate semantics are other seats' business.

## 0. Verdict

**The hold set that the round-11 D claim must equal, hand-derived from the tool and its
selftest output at `e3ef171`, is 15 holds + 1 note + 0 fails in the merged findings channel** —
`D2L-FORM-UNRESOLVED ×10` (GAR-01..GAR-10), `D2L-NATIVE ×2` (L-15, L-16),
`D2L-RANK ×4` of which **3 are holds** (genuine-priority-gap) and **1 is a note**
(`SR-01#a|SR-01#b`, band-keyed-pair). The derivation is in §2; every element is
independently re-checked in §1.3, not read back from the tool.

Completeness divergences found (details §4):

| id | divergence | class |
|---|---|---|
| F1 | `--selftest` (39/39, exit 0) does **not** pin the hold set: five one-line mutations, incl. an **empty** hold set, all still pass 39/39 and exit 0 | check gap — the core property of claim D is unfalsifiable by the tool's own control matrix |
| F2 | a **second channel** computes 9 further holds (`R-MAT-BRIDGE-MISSING ×9`) and **none are carried** into the merged finding list; the list's own counter (`findings_hold_or_fail: 15`) hides them | completeness — "the finding set" is channel-dependent and the loss is silent |
| F3 | 2 of those 9 are classified `hold` where the round-8 shard receipt classified the same two records as carried-flag **notes**: the packet's `maps_to: null` (11-costumes.yml:138,189) is read by the strict loader as the string `'null'`, so the `maps_to is None` note branch never fires. The two filed sources disagree on the intended class — design-spec §7 expects "D2L-MATERIAL findings" for both (severity unstated), the shard receipt records `7 holds + 2 notes` | classification — a 2-element severity divergence inside a channel the merged list never carries |
| F4 | counters contradict the finding list: `coverage.label_findings_fail: 2` / `typed_labels.stats.fail: 2` vs **0** fail-severity findings (the 2 are pre-reclassification values) | reporting — a hand-deriver reading counters gets a different set than one reading findings |
| F5 | `python3 tools/d2-typed-labels.py --check` exits 1 (stale `packet_sha256` pin at typed-labels.d2.yml:9) | **known, not new** at derivation time — filed round-9 (`reports/round-9/d3/interop.md` §4.1–4.2) and round-10 A2 (`reports/round-10/findings-scribe.md:95`); **closed by the landing at 22:13-14Z**: re-pin to `a3aa452c…`, `--check` rc 0 (22:14:22Z, §2.2) |
| F6 | adjacent, report-only: 7 filed earlier-round artifacts are modified in the worktree (`git status --porcelain`, 22:05:51Z) | out of my assignment; flagged for the owner of the sweep |

**Limit and addendum:** `reports/round-11/depth/design.md` landed at 22:07:31Z (after the
derivation below was complete) and `tools/typed-gate-flow.py` — the adapter/e2e — landed at
22:10Z, rewritten four times while measured. §2.1 compares the design's named expected set
against this hand derivation element by element; §2.2 verifies the **wired** run the same
way: its 16 findings are identical to the projector's on all four fields and equal to §2's set
on `(code, severity, where)`, with the e2e green at 22:12:19Z (`rc 0`, `findings: 16 (hold
15, note 1)`, `10 PHON artifact(s) retired, 0 added`). What remains open — the expected
artifact's renamed file still missing, the mutation controls not yet demonstrating, the
projection re-pin not yet performed — is listed in §2.2 and §6.

## 1. Method — hand derivation, with independent re-checks

### 1.1 Inputs and receipts

| input | command | result |
|---|---|---|
| selftest matrix | `python3 tools/d2-typed-labels.py --selftest` | rc 0; 39 `ok`, 0 `FAIL`; no stderr; stdout sha256 `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252`, byte-stable across two runs (`diff -q`) |
| finding document | `python3 tools/d2-typed-labels.py --json` | rc 1; `stats {labels: 58, hold: 15, note: 1, fail: 0}`; stdout sha256 `880d0e45f75f1c14c9528a80a70ff1b6d1c034145ed741796f7038f03c124624`, identical on a second run |
| frozen projection | `examples/culture-d2/typed-labels.d2.yml` | sha256 `e70ba147…`; carries the same 16 findings as `--json` (id/severity/where/detail compare: 0 only-in-either) |
| byte pin | `python3 tools/d2-typed-labels.py --check` | rc **1** — sole diff line is `assembly.packet_sha256` (`8da90b07…` frozen vs `e0f21509…` live); `reader_sha256` current (F5) |
| tool / packet / gate digests | `sha256sum …` | tool `0da0015f…`, packet `e0f21509…`, gate `e6bffd70…`, assembler `8ea6bdde…` |

The selftest stdout digest is the same `7231139c…` recorded by round 8
(`reports/round-8/validation.json` → `claims.D.measurement.selftest.stdout_sha256`) and
re-verified by round 9 (`reports/round-9/d3/interop.md:41`): the matrix has not changed since
round 8, so the blind spots in §4/F1 are inherited, not introduced by round 11.

### 1.2 Derivation rules (what the selftest output lets one conclude)

The selftest output is 39 check lines. The lines that bear on the hold set, and what each
does **and does not** fix:

| selftest line | fixes | does not fix |
|---|---|---|
| `live packet: the ten GAR costume labels are typed translated-label` | 10 costume labels exist, all `translated-label` | that any of them holds |
| `live packet: each GAR label keeps its owed form slot (LEX-GAR-0x)` | each carries `label_id LEX-GAR-0x` | whether a supplied form exists for the slot |
| `live packet: the owed form slots stay held, never passed` | `status == to-verify` on ≥10 labels (a label-level property) | any finding; a hold can vanish while the status stays |
| `live packet: no GAR label is graded on the sound channel` | no `E-LABEL-INVENTORY`/`W-LABEL-INVENTORY` finding | `D2L-NATIVE` holds/fails, `D2L-FORM-*`, `D2L-RANK` |
| `live packet: pipeline evaluates (exit 0/1, never 2)` | exit not 2 | which holds exist; a *shrinking* set keeps exit 1, an **empty** set makes exit 0 — both pass |
| `probe: a claim on the closed inventory in E0 is a reject` / `probe: a foreign era label holds rather than merging by number` | two synthesized probe packets | the live packet's own set |

So the selftest **license** to conclude is only: ten typed costume labels with owed
`LEX-GAR-0x` slots. The holds themselves must be derived from the declared rules
(§1.3) — which is exactly what this seat did.

### 1.3 Independent re-checks (my own code, not the tool's checkers)

1. **`D2L-FORM-UNRESOLVED ×10`.** Rule (`validate_labels`, tools/d2-typed-labels.py:791-796):
   a `translated-label` whose `label_id` is not in the set of *supplied* sound-form
   `label_id`s holds. Hand check: only the 10 costume labels carry a `label_id` at all
   (`label_id` non-None count = 10, values `LEX-GAR-01..10`); all 46 `native-form` and 2
   `borrowed-strata` labels carry `label_id: None`, so `supplied_label_ids` is empty and all
   ten are forced holds. No eleventh translated label exists (kind census: 10/46/2 = 58).
2. **`D2L-NATIVE ×2`.** My own scan of all 48 supplied sound forms against the packet's
   declared inventory (`phonology.consonants ∪ vowels ∪ {' ', '-', '·'}`) reports exactly two
   offenders: `L-15 sára`, `L-16 sará` — both only `á`; no other form carries a combining
   mark. The integration layer reclassifies exactly this shape (`reclassify_parser_finding`,
   :2288-2313, acute set `áéíóú`) to hold, citing `02-phonology.yml:73`'s minimal pair. The
   set is complete in both directions.
3. **`D2L-RANK` holds = 3.** Projected gate rules are the 5 with gate-modelled kinds
   (WR-02, WR-03, WR-04, WR-08, WR-09; grade/rite-state/occasion-exemption/wearer-category/act
   are non-projectable, :954, :1202-1203). Conflicts need same kind+value, opposite effects,
   overlapping eras and a shared in-scope rank: `WR-02#g|WR-09#g` and `WR-08#g|WR-09#g` fire
   (both values map to one gate value, `GATE_VALUE_MAP`); the act pass adds
   `TR-04#a|TR-06#a` (prohibit vs obligate, same object) and `SR-01#a|SR-01#b`
   (band-keyed pair); `WR-03|WR-06` cannot fire (WR-06 not projected). Severity is hold iff
   triage is `genuine-priority-gap` (:2480-2483): the three above hold, the band-keyed pair is
   the single note. Matches the document exactly.
4. **Everything else is clean by derivation, not by absence:** all 10 reconciliation claims
   resolve (`era` = identity tag for E0/E1/E2; `material` resolved by name key), so the
   record-level path contributes **0** findings; 2 borrowed forms resolve `layer_ref` to the 2
   declared layers with substitutions that derive their forms (no `D2L-BORROW`); no duplicate
   ids, kinds, statuses, scripts or eras fire (`D2L-DATA/SCOPE` = 0). The packet carries no
   `form_slots` and no explicit `typed_labels` block, so nothing else can project.

## 2. The derived hold set (pre-wiring, `examples/culture-d2`)

| # | finding id | severity | where | derivation source (independent of the run) |
|---|---|---|---|---|
| 1-10 | `D2L-FORM-UNRESOLVED` | hold | `GAR-01`..`GAR-10` | design-spec §1.5 table (`reports/round-8/depth/design-spec.md:236`): GAR-01..10 → `translated-label`, slot `LEX-GAR-0x`, `to-verify`; slots visible at `examples/culture-d2/components/11-costumes.yml:217-386`; independent authoring source `reports/supplement-opencode-1/22-label-representation.md` §1 (per review-22 §2) |
| 11-12 | `D2L-NATIVE` | hold | `L-15`, `L-16` | my own inventory scan (§1.3.2) + `02-phonology.yml:73` (accent declared by the minimal pair) |
| 13 | `R-RANK-CONFLICT` → `D2L-RANK` | hold | `WR-02#g|WR-09#g` | rank block's conflict×triage tables (`CONFLICT_TRIAGE`, :1178-1187; spec §4) |
| 14 | `R-RANK-CONFLICT` → `D2L-RANK` | hold | `WR-08#g|WR-09#g` | same |
| 15 | `R-RANK-CONFLICT` → `D2L-RANK` | hold | `TR-04#a|TR-06#a` | same |
| — | `R-RANK-CONFLICT` → `D2L-RANK` | **note** | `SR-01#a|SR-01#b` | `CONFLICT_TRIAGE["SR-01#a|SR-01#b"] = band-keyed-pair` |

**Totals:** 15 holds, 1 note, 0 fail/reject; exit 1 (`:2493` — exit 2 is reserved for
`D2L-DATA`). This equals capability-draft §5 Reading A and review-22 §2's pre-change
inventory (the sibling drafts measured the same 16 findings).

### 2.1 Design comparison (added after `design.md` landed, 22:07:31Z)

`reports/round-11/depth/design.md` §4.2-4.4 names an expected hold set; it landed *after*
this seat's derivation was complete, so the comparison below is derivation-first, not a
transcription of the design. Element by element:

| element | design.md | this derivation (§2) | verdict |
|---|---|---|---|
| 10 × `D2L-FORM-UNRESOLVED`, `GAR-01..GAR-10` | §4.2 rows 1-10 | rows 1-10 | **identical** |
| 2 × `D2L-NATIVE`, `L-15`/`L-16` | §4.2 rows 11-12 | rows 11-12 | **identical** |
| 3 × `D2L-RANK` holds (`TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g`) | §4.2 rows 13-15 | rows 13-15 | **identical pairs and order** |
| note `SR-01#a\|SR-01#b`, excluded from the hold set | §4.3 | note row | **identical** |
| fail set ∅ | §4.3 | totals | **identical** |
| comparison key `(id, severity, where)` as a set, counts, full `detail` pins | §4.4(1)-(3) | §5.2 requirement | design already requires what M5 motivates |
| committed baseline `examples/culture-d2/expected-holds.json` (writer D06, reviewer **D21** = this seat) | §4.5 | file absent at 22:07:53Z | `to-verify` — reviewed on landing |
| 9 reconciliation-channel holds | not named; §4.4(4) scopes the set to the typed run | §3 / F2 | **gap — see below** |

**Circularity leg supplied by this review.** The design derives its set by running
`python3 tools/d2-typed-labels.py --json` (design §4.1, commands at `:244-245`) — the same
projector output an e2e would compare against, which is review-22's C1 pattern (harvested
expectation). It is not self-blessing here only if something independently confirms the
harvested set; this review is that something: every element was re-derived from rules,
component bytes and the packet (§1.3), and the two derivations agree exactly. The agreement
is the evidence; the design's own run is not.

**Residual divergences design ↔ derivation (both report-only):**

1. The design excludes the 9 reconciliation-channel holds (§3/F2) — correct for the *merged*
   finding list, but the exclusion must be **stated in the baseline file and in L3's
   wording**. Otherwise a later fix that carries `reconciliation["findings"]` either breaks
   L3 silently or gets absorbed by a re-pin (design §5.2's own guard says a re-pin that
   changes the hold set is a finding, not a pass — this is the concrete future instance).
2. The design's L3 reads the projector's `findings[]` (16 objects), so it inherits the F2
   loss by construction. No contradiction between the documents today; recorded so the two
   definitions of "the finding set" cannot drift apart unnoticed.

### 2.2 Post-landing verification of the wiring (writer iterating while measured)

`tools/typed-gate-flow.py` (R11-D05) appeared at 22:10Z and was rewritten four times while this
seat measured it (`7fb44ebb…` 22:10Z → `25dec236…` ~22:11:35Z → `7bff2edf…` 22:12:19Z →
`f3b417bb…` 22:12:45Z). Everything below is stamped; the writer's final state is `to-verify` at
this seat's close.

**Verified — the property this seat owns: the wired finding set equals the hand-derived set
exactly.**

| check | command / stamp | result |
|---|---|---|
| e2e over `examples/culture-d2` | `python3 tools/typed-gate-flow.py`, 22:12:19Z, tool `7bff2edf…` | **rc 0**; `findings: 16 (hold 15, note 1)`; `delta: 10 PHON artifact(s) retired, 0 added, retained lines identical`; `summary: 5/5 checks passed` |
| set identity vs the projector | `--json` doc 22:12:32Z vs `python3 tools/d2-typed-labels.py --json` | 16/16 findings identical on **all four fields** (`code, severity, where, detail`); 0 only-in-either |
| set identity vs §2 | same doc, `(code, severity, where)` vs the §2 table | **equal** — 15 holds, 1 note, no missing, no extra |
| comparison key in the wiring | `finding_key = (code, severity, where, detail)` (`:227`), `normalized_findings` (`:221`), pin checks `expected-pins` / `expected-delta-match` / `expected-verdicts-match` | exact-set equality including details — §5.2's requirement; a count-preserving swap (M5) would fail it |
| channel differential | e2e output, same run | `removed 10, off-records 10` — exactly the ten `PHON-INVENTORY` lines retire |

So the D claim's core property — "findings exactly equal the expected hold set" — is
**confirmed against an independent derivation**, not merely self-consistent: the 15 holds in
the wired run are the ones §1.3 re-derived from rules and component bytes. That is the leg
review-22's C1 (harvested expectation) requires, since the design's own set was read off the
same projector output.

**Iteration snapshot at 22:12:45Z (items open while the writer was mid-flight; the settled
state is the block below):**

1. **The expected artifact moved mid-iteration.** The first revision read
   `examples/culture-d2/typed-gate.expected.yml` (emitted 22:11Z, sha `44b145d3…`); the later
   revision reads `examples/culture-d2/typed-gate.expected.json`, which **did not exist at
   22:12:45Z** — the e2e then exits 1 on `expected-present` alone (`summary: 5/6 checks
   passed`, `missing: examples/culture-d2/typed-gate.expected.json`). The orphan `.yml` is
   untracked, so no filed byte is harmed; the released name and format are D06's to settle.
2. **The mutation controls cannot yet demonstrate anything.** `--selftest` at 22:12:32Z exits 1
   with `AssertionError: expected file must carry the owed-form holds` (`:669`), and an earlier
   snapshot crashed the controls in `FileNotFoundError` (`:635`, derived packet absent). The
   D17-D19 analogues must be shown passing once the artifacts settle.
3. **The projection re-pin has not happened.** `python3 tools/d2-typed-labels.py --check` still
   exits 1 at 22:12:32Z (design §5.1 / D07); F5 stands until it does.
4. **The F2 exclusion holds but is unwritten.** The wired set is the merged 16, so the nine
   reconciliation-channel holds stay outside; whether the expected document *states* that
   exclusion cannot be checked until it is released in final form. (The first `.yml` revision
   carried `off_sound_channel` and `owed_slots` but an empty finding list — the writer's
   intermediate state, not a defect claim.)
5. Cosmetic, report-only: in the 22:12:32Z JSON doc the `typed-packet-pinned` check reports
   `ok: true` with the detail string "derived typed packet differs from …" — a stale message
   on a passing check.

**Settled verification (22:14:22Z).** After the writer stopped: `tools/typed-gate-flow.py`
`ae55e6fa…`, `examples/culture-d2/typed-gate.expected.json` `e962849a…`,
`examples/culture-d2/typed-labels.d2.yml` re-pinned to `a3aa452c…` (design §5.1's predicted
post-re-pin bytes).

| command | result |
|---|---|
| `python3 tools/typed-gate-flow.py` | **rc 0**, `summary: 10/10 checks passed`, `findings: 16 (hold 15, note 1)`, `10 PHON artifact(s) retired, 0 added, retained lines identical` |
| `python3 tools/typed-gate-flow.py --selftest` | **rc 0**, `14/14 checks passed` — mirrored e2e, `--check`/`--json`, and the tamper, smuggled-label, dropped-owed-form, laundered-hold, malformed and missing-input controls |
| `python3 tools/d2-typed-labels.py --check` | **rc 0** — "byte-identical deterministic projection"; **F5 closed by the re-pin** |

With that, the hold-set leg of claim D is verified end-to-end against this seat's independent
derivation, and §5 items 2, 3 and 5 are demonstrated in the landed path (the dropped-owed-form
control is the analogue of M1 and it now fails the wired run as it must). F2 and F3 remain
undispositioned design facts, not regressions introduced by the wiring.

## 3. Channel accounting — the completeness question

`run_pipeline` assembles the merged `findings[]` from three sources: loader/parser findings,
integration-layer findings, and **per-record** reconciliation findings
(tools/d2-typed-labels.py:2484-2490 iterates `reconciliation["records"]` → `record["findings"]`).
The reconciliation driver, however, writes its record-side flags and slot conflicts into the
**top-level** `reconciliation["findings"]` (:1989-1990, producers `_material_record_flags`
:1886-1920 and `_slot_conflicts` :1923-1964) — and nothing reads that list.

Measured (live packet, 22:0xZ):

```text
reconcile_scoped(packet)            -> summary {claims: 10, findings: 9, by_severity: {hold: 9},
                                                 by_code: {R-MAT-BRIDGE-MISSING: 9}}
sum(len(r["findings"]) for records) -> 0
merged findings[]                   -> 16 (15 hold + 1 note)
coverage.findings_hold_or_fail      -> 15
```

So the tool **computes 24 holds** (15 merged + 9 reconciliation-only) and **reports 15**.
Both the frozen artifact and the live run show this (frozen: same 16 findings; its
`era_material_reconciliation.summary` likewise says `hold: 9`), i.e. the loss is stable and
predates round 11. The exit code cannot reveal it: exit is 1 either way once any hold exists.

Where the 9 come from: every one of the 9 `CMAT-*` records declares `maps_to` to a
`10-materials MAT-*` target and no bridge scope is declared to the packet, so each is held
"carried, not merged" (spec §3.2; `reports/round-8/depth/shard-era-material.md:52`).

## 4. Findings (divergences), each with evidence

### F1 — the selftest does not pin the hold set (class: check gap; severity for claim D: high)

Five one-line mutations in isolated full copies of the tree
(`.scratch/r11d21/{mirror-base,M1..M5}`, `TMPDIR` under `.scratch`), each run against the
untouched packet:

| control | one-line mutation | selftest | live `--json` after mutation |
|---|---|---|---|
| M1 | `_fail(findings, D2L_FORM, label.get("id"),` → `False and _fail(…)` (silences the 10 FORM holds) | **39/39, rc 0** | exit 1, `{hold: 5, note: 1}` (10 holds silently gone) |
| M2 | `triage.get("status") == "genuine-priority-gap"` → `== "no-such-status"` (demotes the 3 rank holds) | **39/39, rc 0** | exit 1, `{hold: 12, note: 4}` |
| M3 | `reclassified = reclassify_parser_finding(item)` → `= None` (turns the 2 acute holds into fails) | **39/39, rc 0** | exit 1, `{fail: 2, hold: 13}` |
| M4 | M1+M2+M3 and a silenced native-inventory check | **39/39, rc 0** | **exit 0, `ok: true`, `{hold: 0}`** — an empty hold set |
| M5 | FORM hold `where` → `"SWAP#"+id` (count-preserving identity swap) | **39/39, rc 0** | exit 1, `{hold: 15, note: 1}`, where ids all `SWAP#GAR-0x` |

M4 is the decisive one: the tool's own control matrix passes with **no holds at all**.
M5 shows even a count-based equality check is insufficient — the *identities* can change
under a constant count. Consequence: claim D's "findings exactly equal the expected hold
set" was, at derivation time, enforceable only by the landing's own e2e assertion; nothing in
the tool would stop a regression that quietly reshapes or empties the set. The landed wiring
now supplies that assertion and demonstrates the analogous control (§2.2) — the blindness of
the tool's own matrix remains a fact about the tool. (These controls mutated copies under
`.scratch/r11d21/`; this seat wrote nothing outside `reports/round-11/depth/review-21.md` and
`.scratch/`.)

### F2 — 9 computed holds never reach the finding list (completeness)

Evidence: §3 block; code path `:1989-1990` vs `:2484-2490`. Consequence for claim D: an e2e
that compares "findings" against a design-named set must say **which channel** it compares.
If the landing starts carrying the reconciliation-level findings (arguably the correct fix),
the merged set changes by +9 holds in the same beat — that must be dispositioned as a named
change, never absorbed as "the expected set was 24 all along".

### F3 — `maps_to: null` read as the string `'null'` (classification; 2 of the 9)

`11-costumes.yml:138` (CMAT-03) and `:189` (CMAT-08) declare `maps_to: null` plus a
`maps_to_note` ("REPORT, do not merge…", OQ-3). The strict loader has no null literal
(`parse_scalar` :213-262 returns unknown scalars as text), so the packet's bare
`maps_to: null` (packet.d2.yml:3172, :3253) loads as `'null'` (type `str`). Probe:

```text
_material_record_flags(records with maps_to=None)  -> [('R-MAT-CARRIED-FLAG','note'), …]
_material_record_flags(records with maps_to='null') -> [('R-MAT-BRIDGE-MISSING','hold'), …]
```

The two filed sources disagree on which class is intended, and this review does not resolve
them (design authority is D01's):

- design-spec §7 (open items): "pack-ox down (CMAT-03) and silk (CMAT-08) have no `maps_to`
  target; the tool reports both as `D2L-MATERIAL` findings" — it names the class, not the
  severity;
- round 8's shard receipt recorded `R-MAT-BRIDGE-MISSING: 7, R-MAT-CARRIED-FLAG: 2`
  (`shard-era-material.md:893`, `:912`) — the two carried flags as **notes**.

The integrated tool yields **9 holds** (`reports/round-8/depth/test-consistency.md:224`,
reproduced here). Observable, mechanical divergence: the strict loader's null handling moves
those two records from the note branch to the hold branch; whichever class the lane intends,
the cause is the loader's `null` → `'null'` coercion, not the packet authors, and the
severity of two elements of this channel is therefore unresolved between filed sources.

### F4 — counters contradict the finding severities (reporting)

`coverage.label_findings_fail: 2` (:2499, from the pre-reclassification `parse_result.stats`)
and `typed_labels.stats.fail: 2`, while the emitted findings carry those same two records
(L-15/L-16) as **holds** and contain **zero** fail-severity entries. A reader who derives the
set from counters gets "fail 2, hold 10" at label level; a reader of `findings[]` gets
"hold 12". Same totals, contradictory severities — exactly the kind of divergence a
hold-set equality check must not be built on.

### F5 — `--check` red (known at derivation time; resolved by the landing at 22:13Z)

`python3 tools/d2-typed-labels.py --check` → exit 1, one-line diff at
`typed-labels.d2.yml:9`: `packet_sha256 8da90b07…` (artifact) vs `e0f21509…` (live packet,
`assemble-d2.py --check` green). Filed by round 9 (`reports/round-9/d3/interop.md` §4.1-4.2)
and round 10 (A2, `reports/round-10/findings-scribe.md:95`). Not a new divergence; noted
because claim D explicitly requires the frozen replay to be "re-pinned and green", and this
is the pin that is currently red.

**Resolved 22:13Z** — the landing re-emitted the projection to `a3aa452c…` (design §5.1's
predicted bytes, 3010 lines) and `python3 tools/d2-typed-labels.py --check` now exits 0 with
"byte-identical deterministic projection" (22:14:22Z, §2.2). This seat did not perform or
ratify the re-pin; the re-pin is D07's, and it is recorded here only so the F5 row is not
read as still open.

### F6 — adjacent observation (report, never absorb)

`git status --porcelain` at 22:05:51Z shows 7 modified tracked files of earlier rounds:
`reports/round-10/coverage/index-update-22.md`, `reports/round-5/validation.json`,
`reports/round-6/checkpoint-validation.json`, `reports/round-6/validation.json`,
`reports/round-7/validation.json`, `reports/round-8/validation.json`,
`reports/round-9/validation.json` (combined diffstat `127 insertions, 881 deletions`).
capability-draft.md §7.4 flagged three of these earlier; the set has grown. Not my
assignment and not touched by me — the round's owner should decide (revert vs. new-file
correction).

### Minor (in-lane, adjacent to the D2L-ERA vocabulary, reported not absorbed)

`era_reconciliation.two_to_one[].tags` carry leading spaces (`[" E0"," E1"," E2"]` for
ERX-R, `[" E2","E1"]` for ERX-3) because `ERA_TAG_RE` (:2212) matches a preceding non-alnum
character. Nothing in the merged finding set depends on it today; a consumer matching tags
exactly would miss. Recorded as an observation for the era owner.

## 5. What the landing must satisfy (requirements, not design)

1. **Name the channel and the set, in full.** Either the merged 15+1 (with an explicit
   disposition of the 9 reconciliation-only holds), or a gate-facing set whose defining
   properties are checkable (capability-draft §5 Reading B) — the wording must say which.
2. **Equality must be a multiset over `(id, code, severity, where)`** — not a count (M5) and
   not a counter (F4). An exact-set assertion is the only thing that fails when one hold is
   swapped for another.
3. **The assertion must live in the e2e/runner, not in `--selftest` alone** — M1..M4 show the
   selftest cannot fail on hold-set damage. (Adding a live-packet exact-set check to the
   selftest would also close F1; that is the tool owner's call, and it is a new behaviour
   change that must itself be pinned.)
4. **Disposition the +9 / −2 questions explicitly at wiring time** (F2, F3): carrying
   reconciliation-level findings and fixing the loader's null handling each move the set; a
   re-pin that silently absorbs either is self-blessing (review-22's C-patterns).
5. **Keep the three round-11 negative controls aimed at the set** (D17-D19: smuggled label,
   dropped owed form, laundered hold): the dropped-owed-form control is the one M1 simulates,
   and it is currently invisible — it must be made visible by the e2e, not by the selftest.

**Status at 22:14:22Z (wiring settled):** items 2, 3 and 5 are satisfied in the wired path —
the comparison key is `(code, severity, where, detail)`, the e2e exits 1 on any mismatch, and
`--selftest` (14/14) demonstrates the tamper, smuggled-label, dropped-owed-form,
laundered-hold, malformed and missing-input controls. Item 1 is satisfied for the merged
channel: the released `typed-gate.expected.json` names the 16 findings and the wired set is
verified equal to §2's derivation. Item 4's two dispositions (F2 carry, F3 loader null) remain
untouched by the wiring, and whether the released expected document states the F2 nine-hold
exclusion is still `to-verify` (§2.2, §6).

## 6. Limits and `to-verify`

- **The wired flow landed mid-review and settled at 22:14:22Z** — five revisions of
  `tools/typed-gate-flow.py` while measured (`7fb44ebb…` → `ae55e6fa…`; §2.2). Settled
  verdicts re-run by this seat: e2e rc 0 (`10/10 checks`, `findings: 16 (hold 15, note 1)`,
  `10 PHON artifact(s) retired, 0 added, retained lines identical`); `--selftest` rc 0 (14/14,
  controls incl. tamper, smuggled-label, dropped-owed-form, laundered-hold, malformed,
  missing-input); `d2-typed-labels.py --check` rc 0 after the re-pin. Remaining `to-verify` for
  the integrator: whether the released expected document states the F2 nine-hold exclusion,
  and the F2/F3 dispositions themselves. Design §4.5 names this seat (D21) the reviewer of a
  committed `expected-holds.json`; the released baseline actually in the tree is
  `examples/culture-d2/typed-gate.expected.json` (`e962849a…`), which §2.2's comparison covers —
  a differently named file appearing later is a re-read event, not a re-review.
- **Reading B (gate-facing)** cannot be derived until the adapter lands; §5.1 says what it
  must name, not what it will be.
- **Whether the 9 bridge-missing holds *should* be holds** (bridge declaration is a
  materials/lore decision) is out of lane; I report the divergence between the computed
  severity and the components' declared notes, nothing more.
- **Not re-run by me:** the round-10 ledger rows (F), the handoff exercise (O), the frozen
  replay manifests. The `--check` red (F5) and the selftest digest were re-run by me; the
  rest are cited, not re-verified here.

FILES: reports/round-11/depth/review-21.md
SUMMARY: R11-D21 — hold set hand-derived (15 holds + 1 note) and independently re-checked; design.md §4.2-4.4 and the settled wiring's 16 findings match it element for element (e2e rc 0, 10/10 checks, 10 PHON artifacts retired / 0 added; wired `--selftest` 14/14; projection re-pin makes `--check` rc 0, closing F5); five mutation controls prove the round-8 `--selftest` cannot fail on hold-set damage; open for the integrator: 9 computed reconciliation holds never reach the merged list (F2) and two `maps_to: null` records carry an unresolved hold-vs-note divergence (F3).
