- Seat: R01 | reviewer | claim D | date 2026-10-19 | baseline da68a6d

# R01 — Adversarial review of the D block (stale-number hunt, renderer-contract, freeze design)

Mission (targets.json R01): stale-number hunt (any live-vs-packet mismatch the builders
missed), renderer-contract violations, freeze-design holes. Read-only: no filed byte was
edited, no `reports/round-*/run-validation.py` was executed in-tree (F-C13-1); the only
runs are gate/selftest/tool invocations (§1) and read-only python readers.

## 1. What I ran (independent of every other seat)

```
python3 -B tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md
  -> INFO scan: fields=16/16 glossary-entries=20 findings=0                          exit 0
python3 -B tools/d2-typed-labels.py --selftest        -> selftest: 163/163 checks passed
python3 -B tools/assemble-d4-typed.py --selftest      -> selftest: 12/12 checks passed
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml -> 20/20 legs
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml -> 13/13 legs
python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
  -> byte-identical deterministic projection                                          exit 0
```
plus: a parse-and-recompute of **all 58 manifest rows** of the r6 packet
(`| A-nn | path | role | sha256 | N bytes |`): every digest **and** byte size equals the
live file — **0 mismatches, 0 missing paths**. And a read-only import of the renderer's own
mining functions to get the live values the builder must match:

```python
import importlib.util, pathlib   # tools/exercise-handoff-e2e.py, no main() invoked
m.v3_mine_d4(root)        -> counts: lexicon 62 / names 8 / symbols 8 / costumes 6 /
                             rank_rules 4 / era_records 8 / contact 2 / provenance 9 ...
m.v3_mine_d4_labels(root) -> labels 82, native-form 64, translated-label 12,
                             borrowed-strata 6, findings_total 12, hold_or_fail 12,
                             unresolved 0, quarantine 0, conflicts 0, reconciliations 6,
                             alias_rows 4
m.v3_mine_d4_holds(root)  -> hold 12, note 0, fail 0, rows 12, notes 0
m.v3_mine_d4_typed(root)  -> channel_rows 12, counts {hold 12, note 0, fail 0}
```
Cross-check on artifact digests (live): `typed-labels.d4.yml` = `c23b0ab5…`,
`expected-holds.json` = `e6ae9828…`, `packet.d4.yml` = `aac91246…`; `c23b0ab5…` equals the
round-31 sweep baseline copy (`reports/round-31/sweep/frozen/r31-post/inputs/examples/culture-d4/typed-labels.d4.yml`),
so the live projection is the one the r31 sweep froze.

**Independent corroboration of the structural defect** (D16 §4, read and re-checked against
the code): an isolated `git archive` render today reproduces the filed r6 packet
**byte-for-byte**, 13 stale mismatches inclusive. I verified the code paths that force this
(§4 F9): the D4 rows are copied from the filed map at `:2599-2607`, the twin is built from
the same row objects (`v3_build_twin`, `tools/exercise-handoff-e2e.py:2621`).

## 2. Stale-census review (D03/D16/D04 fragments vs my own measurements)

I re-measured every D03 §2 row. Rows 1–8 are **correct as filed in their fragments**:

| D03 row | site | filed/claimed stale | my independent live value | verdict |
|---|---|---|---|---|
| 1–3 | `packet.md:148` D4-CL05 (grounding, `#stats`, statement) | 74 / 56 / 16 / 15; `labels 74` | 82 / 64 / 12 / 12; `labels 82` (`typed-labels.d4.yml:36-38,46`; `typed_labels.stats` = {fail 0, hold 12, labels 82}) | confirmed |
| 4 | `:149` D4-CL06 | hold 15, note 1, "three D2L-RANK rows, plus one D2L-RANK note", +9/+1 | hold 12, note 0; all 12 rows `D2L-FORM-UNRESOLVED` (6 `GAR-*` + 6 `LEX-GAR-*`), zero rank rows, `notes: []` | confirmed |
| 5 | `:150` D4-CL07 | conflicts 4 / quarantine handles 3 | 0 / 0 (reconciliation records 6 stays) | confirmed |
| 6 | `:152` D4-CL09 | 13 / 3 / 4, "adapt_status cannot-evaluate" | 0 / 0 / 0; `grep -c cannot-evaluate typed-labels.d4.yml` = **0**; all `adapt_status` values are `executable` (`:322,:357,:391,:426,:464,:499,:533,:568`); `act_rules/unresolved/quarantine/residuals` = `[]` | confirmed |
| 7 | `:307` OQ-V3-05 | twelve form + three rank + one note; 13/3/4 | 12 form holds / 0 rank / 0 notes; 0/0/0 | confirmed |
| 8 (sweep find) | `:151` D4-CL08 | `d2-typed-labels.py --selftest exit 0 50/50` | printed total is `163/163` (my run); the renderer's witness floor is `v3_selftest_witness(..., 50)` (`:3468-3473`), so `50/50` is a stale r20-era snapshot, `163/163` is the live printed claim | confirmed |
| 9 (sweep find) | `:144` D4-CL01 | "twelve authored inputs"/"twelve authored components" | 13 component files, registry `C-01..C-13` (`01-brief.yml:161` says C-13 "added round 27"), 13 `assembly.source_sha256` entries in `packet.d4.yml` | confirmed (map-sourced, see F1) |
| 10 (sweep find) | `:20` scope field | "twelve authored components" | 13 | confirmed **but unfixable by the drafted patch set** — see F1 |

Twin mirrors confirmed at the same rows (my own path walk): `claim_ledger[19]` (D4-CL05
basis), `[20]` (D4-CL06), `[21]` (D4-CL07 statement+basis), `[23]` (D4-CL09 basis),
`open_questions[8]` (OQ-V3-05). The twin has no scope field, so the `:20` site is
packet-only.

## 3. Findings

### R01-F1 (BLOCKING — the drafted fix surface is incomplete: a third emission source)

The §scope line is emitted from a **hard-coded renderer literal**, not from the map:

```
tools/exercise-handoff-e2e.py:2779
        f"{counts['contact']} contact layers, twelve authored components); all native spellings are "
```

Evidence: (i) `grep -rn "2779" reports/round-34/` → **no fragment drafts this patch**;
(ii) D16's integrator table A–F covers `CLAIMS_MAP` (`:184`), the new map file, the
docstring (`:2290`), the intro literal (`:2699-2700`), the OQ literal (`:3524-3531`) and the
module docstring (`:29-34`) — but not `:2779`; (iii) D03 rows 9–10 give target **wording**
for packet text, not the literal; a packet-byte splice at `:20` is **erased at freeze**,
because `v3_freeze` re-writes `packet.md` from `assembly.packet`
(`tools/exercise-handoff-e2e.py:4085`, twin at `:4086`). D16's byte-identical re-render
proves the point: today's render emits `twelve authored components`, so `declared-in-r7`
will too until `:2779` is patched. Under D03's own audit pattern set (which counts
`twelve authored` ×3 as stale), the claim's "zero stale figures" threshold **fails on this
site**.

Required addition to the integrator's patch list:
`G | tools/exercise-handoff-e2e.py:2779 | "twelve authored components" | "thirteen authored components"`
(and the D4-CL01 map row's "twelve authored inputs/components" → thirteen, which rides
D16's new map).

Related, and it must be decided consciously: the read set still pins only **12** D4
components — `D4_COMPONENTS` lists `01-brief…12-provenance` (`:153-166`), while the live
tree has a 13th (`13-register-law.yml`), which enters the packet only through
`packet.d4.yml`'s own `assembly.source_sha256` pin (13 entries, re-measured in the 26/26
component leg). The r6 packet is already internally split here: `:20` says "twelve authored
components" while `:279` says "component digests … (9 D2, 4 D3, **13 D4**)".
- Option A (minimal): emit "thirteen authored components (twelve pinned as component rows;
  the thirteenth enters by the packet's own assembly pin)". No read-set change.
- Option B (thorough): add `13-register-law.yml` to `D4_COMPONENTS` → read set 58→59, one
  new manifest row, and the read-set/component lines (all f-string-derived) move with it;
  `CLAIMS_MAP` re-pointing itself does **not** change the count — the constant is already a
  member of `V3_READ_SET` (`:1957`), so re-pointing replaces a path, it does not add one.
Either way the phrase cannot ship unchanged; Option B is the only one where "every live D4
component is pinned by the read set" is true.

### R01-F2 (major — D03 §3.2 misattributes the live hold delta to the filed r18 receipt)

D03's replacement D4-CL06 text reads "…reports/round-18/d4/holds.md reconciles the brief's
six-row declaration with a documented **+6 hold / +0 note delta**". The arithmetic is right
(brief declares 6 holds / 0 notes at `examples/culture-d4/components/01-brief.yml:216`;
live emits 12 / 0), but the **citation is false**: the filed receipt documents the r18
generation as "74 labels / 15 holds / 1 note / 0 fails" and a "**+9 hold / +1 note** delta
against the delivered declaration" (`reports/round-18/d4/holds.md:25-26,:36-40`). No filed
receipt documents a +6/+0 transition; that transition is the r26/r27/r28 history recorded
in `examples/culture-d4/expected-holds.json#revision_note` ("The hold set is UNCHANGED at
12 holds / 0 notes / 0 fails"). Recommended wording (the round-25 revision's own model,
`reports/round-25/v3-supersession/declared-in-r4/packet.md:152`): keep the r18 +9/+1 delta
as *that historical generation's* reconciliation, and cite expected-holds.json#revision_note
for the live 12/0/0. The row's `links` cell may keep the r18 receipt (it is read-only
history), but the statement must not claim it evidences +6/+0.

### R01-F3 (major — three divergent OQ-V3-05 wordings; the literal is authoritative)

Three candidate texts exist: D03 §3.5 (packet bullet), D04 §3a (renderer literal), D16
table E (candidate). They are not identical. Decision rule for the integrator: the row is
generated from the literal (`tools/exercise-handoff-e2e.py:3524-3531`), so **D04's literal
patch wins**; D03's §3.5 splice is inert (erased by `v3_freeze:4085`) and D16's table E is
superseded by D04's wording. Separately, D03's instruction "splice each fenced block in
place of the row at the stated line of the new packet" is structurally wrong for **all**
sites, not just OQ: the D4 rows are map-sourced, so D03's blocks are target wording for the
successor map, not packet edits. The integrator should land D16's A–E (+ my G) and let the
renderer produce the packet.
Live-accurate content the chosen wording must keep (my measurement): 12 form holds /
0 rank holds / 0 notes / 0 fails; D4 coverage 0 unresolved / 0 quarantine / 0 conflicts;
the 13/3/4 residuals are D2-owned and already routed by OQ-V2-03 (`packet.md:301`, live
D2 = 13/3/4 per `examples/culture-d2/typed-labels.d2.yml:30,40,44`); the six owed garment
terms stay the D4 blocker.

### R01-F4 (freeze-design hole — the freeze has no semantic leg; the rot class is invisible)

`v3_freeze` (`:3978`) refuses on gate/uncertainty/link findings and pins
`field_digests` — digests of the *stale* prose bytes. Nothing asserts that quoted numbers
equal live artifacts, which is exactly why r6 froze green while contradicting its own
manifest rows (`:68-69`) and validation line (`:285`). Required closure for r7, in addition
to the wording fix: a **stale-figure leg** in the round validator (D16's row-scoped audit
tool is a usable start; it must stay **row-scoped** — the same digits 13/3/4 and hold 15/note
1 are *fresh* in D2 rows: `packet.md:284,:301`, RD-D2-01/02 `:266-267`, and A-11 `:49`).
Better still, a preflight in the renderer so the freeze refuses stale prose rather than
reporting it afterwards. A new control belongs with the existing m12 set
(`:4414-4448`: m12a baseline tamper, m12b read-set tamper, m8 re-typed v2 row,
scan-expectation tamper — none of them can detect a stale literal): the missing control is
"mutate the map/literal wording (not the artifacts), require the audit leg red".

### R01-F5 (freeze-design hole — no target-dir guard; in-place re-freeze over a filed dir is possible)

`v3_freeze` does `target.mkdir(parents=True, exist_ok=True)` (`:4076`) and overwrites
`expected.json`/`packet.md`/`twin.json`/`run.log`/`freeze.txt` in place. The r6 pair *was*
re-frozen in place — `reports/round-30/handoff/declared-in-r6/freeze.txt` line 8:
`re-frozen packet_sha256: ec30b11f… -> 6ced88ad…`. Hazard for this round: any integrator
invocation of `--freeze reports/round-30/handoff/declared-in-r6` (or any filed pair dir)
would silently rewrite filed bytes. Required: r7 freezes into a **new** dir only, and the
round validator asserts post-build that the filed anchors are unchanged — use R02's five
digests as the anchors (`packet.md 6ced88ad…`, `twin.json 6633443d…`,
`expected.json ea1e2927…`, `freeze.txt 6fe70c0c…`, `run.log b5ee3351…`, quoted from
`reports/round-34/review/R02-d-review.md` §0 and re-checkable with `sha256sum`).

### R01-F6 (minor, design fact — the frozen baseline is date-bearing)

`expected.json` carries `frozen_at: datetime.date.today().isoformat()`
(`:4012`, and the v1 twin at `:1540`) and its `baseline_digest` covers that field, so a
re-freeze on another day produces different `expected.json` bytes for identical inputs.
The r7 "byte-preservation / re-runnable" claim must therefore be scoped: reproducibility is
within the freeze date; a re-runner validates by re-running the exercise against the pinned
baseline, not by byte-comparing `expected.json` across days.

### R01-F7 (minor — non-atomic freeze ordering)

`expected.json` is written first (`:4084`), then `packet.md`/`twin.json` (`:4085-4086`), the
run log (`:4104`) and `freeze.txt` (`:4126`). A crash mid-freeze leaves a baseline whose
`packet_sha256` may name a file that was never written; no temp-dir-plus-rename guard
exists. Low probability, but the r7 receipt should record the freeze as one command run, and
the validator should assert the pair's internal consistency (packet sha == freeze.txt ==
expected.json.packet_sha256), which it already must do.

### R01-F8 (pre-empted non-defects — do not "fix" these)

- **"8 era records" is live.** `v3_mine_d4` returns `era_records: 8` (the section's own
  record census), matching `packet.md:285` and A-28 `:68`. Do not change it to 4 (the
  `ER-01..ER-04` prose in D4-CL02 counts a different sub-table).
- **D2 rows are live**: `examples/culture-d2/typed-labels.d2.yml:29-46` still reads
  conflicts 4 / findings_total 16 / hold-or-fail 15 / unresolved 13 / quarantine 3 /
  reconciliation_records 10, and `examples/culture-d2/expected-holds.json#counts` is
  15/1/0. `packet.md:284`, `:301`, `:129-130`, `:266-267` and A-11 `:49` are correct as
  filed; any symmetric "fix" corrupts live rows (D03 §8 and D16 §2 both say this — I agree,
  independently measured).
- **Other emitted count literals in the v3 builder are live**: "its 15 claim rows"
  (`:2698`), "34 carried v2 edge mappings" (`:2713`, `:2956`), "12 namespaced candidates"
  (`:2749`), "The 15 v2 rows" (`:2932`) — all match live (27 claims, 88 edges = 34 + 54,
  12 subject_refs). My scan of the builder region for digit-bearing literals found `:2779`
  and the OQ literal as the only stale ones.

### R01-F9 (corroboration + the round-25 trap, with evidence)

- The block is structural, not textual: `CLAIMS_MAP` (`:184`) is read by
  `v3_parse_claims_map` (`:2289-2307`, requires exactly 12 rows) and the rows enter the
  ledger verbatim (`:2599-2607`); the twin copies the same objects (`:2621`). The map is
  filed round-20 bytes carrying the stale text (`reports/round-20/handoff/claims-map.md:99-105`,
  `:116`, `:124`, `:155/:158`, `:251`). A re-render therefore reproduces the defect
  byte-for-byte (D16 §4's isolated-archive proof; my code reading agrees).
- **The round-25 correction is itself partially stale — do not copy it verbatim.** Its
  D4-CL05 row still asserts `typed_labels 74, labels_by_kind native-form 56`
  (`reports/round-25/v3-supersession/declared-in-r4/packet.md:151`), which was live at the
  r22-post generation (`tools/gates/expected/d4-typed-labels-check-gate/r22-post/typed-labels.d4.yml`:
  74/56, conflicts 0, findings 12) but is not live now (82/64; the change landed between
  r22-post `60b526b0…` and r28-post `339bfd83…`, both sweeps on disk; the r26
  register-stratum note records the 8 register-scoped records landing —
  `expected-holds.json#supersedes_pins.previous_revision_note`). Its findings/hold/OQ
  corrections (12/12, 12/0/0, zero rank holds) **are** live-correct and are the right wording
  model. Any seat diffing r6 against r4 must re-measure the label counts against live bytes;
  D04 §3a already says it re-measures, and the emitted literal must carry 82/64.

## 4. Integrator action list (delta over D16's A–F)

1. `G`: `tools/exercise-handoff-e2e.py:2779` — `twelve authored components` → target wording
   per F1 (Option A or B); plus the read-set decision if Option B.
2. `D4-CL06` map row — apply F2's citation correction (r18 receipt = historical +9/+1;
   live 12/0/0 cited to expected-holds.json#revision_note).
3. `OQ-V3-05` — land D04's literal wording only (F3); drop D03 §3.5/D16 table E as
   duplicates; do not packet-splice any D4 row (F3).
4. Wire the stale-figure audit leg (F4) and assert the five r6 anchors (F5) post-build.

## 5. Limits

- I did not build an isolated `git archive` render myself; D16 §4 reports exactly that
  experiment and the byte-identical diff, and I verified the code paths that make it true.
- `D05`/`D07`/`D17`/`D19`/`D20` had not landed at my read time (`find reports/round-34 -type f`
  at review time), so no draft-packet gate run exists yet to review; when D05 lands, re-run
  D03's §8 pattern walk **plus** a `grep -c "twelve authored"` on the rendered packet — the
  latter is the F1 tell.
- I did not run any filed round runner; all executions are tools/gates/selftests (§1).

## Owed: none

(Fragment dependencies of this seat were the filed r6 pair and the landed D-block fragments,
all present; later-landing D fragments are covered by §5's re-check note.)

## Citations

- `reports/round-34/targets.json:65` (R01 mission), `reports/round-34/claims.json:20-38` (claim D)
- `reports/round-30/handoff/declared-in-r6/packet.md:20,:68,:69,:144,:148,:149,:150,:151,:152,:266,:267,:279,:284,:285,:301,:307`
- `reports/round-30/handoff/declared-in-r6/expected.json` (`counts.d4_holds 12`, `d4_typed_labels 82`, `d4_era_records 8`); `freeze.txt:1-8`; `twin.json` (`claim_ledger[19,20,21,23]`, `open_questions[8]`)
- `examples/culture-d4/typed-labels.d4.yml:29-47` (coverage), `:322,:357,:391,:426,:464,:499,:533,:568` (adapt_status), `:2865-2869` (stats), `typed_labels.stats` via json
- `examples/culture-d4/expected-holds.json` (`counts {hold 12, note 0, fail 0}`, 12 rows all `D2L-FORM-UNRESOLVED`, `notes: []`, `revision_note`, `supersedes_pins.previous_revision_note`)
- `examples/culture-d4/packet.d4.yml:2161-2206` (era_records), `:2491-2527` (form_slots), 13 `assembly.source_sha256` entries incl. `13-register-law.yml`
- `examples/culture-d4/components/01-brief.yml:161` (C-13 "added round 27"), `:216` (`counts: {hold: 6, note: 0, fail: 0}`)
- `examples/culture-d2/typed-labels.d2.yml:29-46`; `examples/culture-d2/expected-holds.json#counts`
- `tools/exercise-handoff-e2e.py:153-166` (D4_COMPONENTS 12), `:184` (CLAIMS_MAP), `:1933-1934`, `:1957` (CLAIMS_MAP in V3_READ_SET), `:2289-2307`, `:2599-2607`, `:2621` (v3_build_twin), `:2674` (v3_build_packet), `:2698/:2713/:2749/:2779/:2932/:2956` (literals), `:3468-3473` (witness floor 50), `:3524-3531` (OQ literal), `:3978` (v3_freeze), `:4012` (frozen_at), `:4076,:4084-4086,:4104,:4126` (freeze writes), `:4414-4448` (m12/m8/scan controls)
- `reports/round-20/handoff/claims-map.md:57,:62,:99-105,:116,:124,:155,:158,:251`
- `reports/round-18/d4/holds.md:25-26,:36-40`
- `reports/round-25/v3-supersession/declared-in-r4/packet.md:151,:152,:153,:155,:310`; `freeze.txt:1-9` (corrections list)
- `tools/gates/expected/d4-typed-labels-check-gate/r22-post/typed-labels.d4.yml` (74/56); `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/examples/culture-d4/typed-labels.d4.yml` (82/64); `reports/round-31/sweep/frozen/r31-post/inputs/examples/culture-d4/typed-labels.d4.yml` (`c23b0ab5…` = live)
- Round-34 fragments read: `depth/D03-ledger-rows.md` (§1–§8), `depth/D04-oq-glossary.md` §2–§3a, `depth/D16-gap-fill.md` §2–§5, `review/R02-d-review.md` §0, `review/R03-d-review.md` §verdict
- Commands: the §1 block; my manifest re-measure loop (58 rows, 0 mismatches); `python3 -c` json reads of `expected-holds.json` and `typed-labels.d4.yml`; `grep -rn "2779" reports/round-34/` (no hits); `grep -c '^ok '` over the d2 selftest output (163)
