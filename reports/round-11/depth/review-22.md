# R11-D22 — circularity audit of the round-11 re-pin (does any change bless itself?)

- seat: **R11-D22** (adversarial reviewer, circularity), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D22 (reviewer): circularity audit of the re-pin (did any change bless itself?); reports/round-11/depth/review-22.md."
- writes: this file only (plus in-lane scratch under `.scratch/d22/`). No tool, gate, packet, component, projection, expected set, baseline, manifest or earlier-round byte is edited by this seat; `reports/round-{8,9,10}/**`, `tools/gates/frozen/**` and `tools/gates/expected/**` are read-only here. No commit, no push.
- clock: all stamps UTC (`date -u +%FT%TZ`); local time is UTC-03:00. Lane revision at audit start: `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (`e3ef171`, the round-11 claims commit; `git rev-parse HEAD`).
- wave state: **live throughout** — the audited wiring (`tools/typed-gate-flow.py`) was re-hashed three times in this seat's window (`ae55e6fa…` 22:13Z → `a7e1224f…` 22:17:01Z → `5758e315…` 22:19:03Z), and the frozen generation's snapshot/report files were refreshed at 22:17:28Z / 22:18:17Z. Every reading below names its stamp; the parent must re-run §3 on the settled tree.
- canon: NON-CANON engineering review. Nothing here admits a round, a capability or a canon fact.

## 0. Verdict

**The delivered re-pin is not self-blessed on the facts it records, but its mechanics leave the expectation regenerable from the observation, and this seat demonstrated end-to-end that a dropped owed form can be blessed with exit 0 by one command.**

What is verified sound (independent re-runs, §3):

| leg | reading | stamp |
|---|---|---|
| projection re-pin | emitted bytes hash exactly the pre-registered prediction `a3aa452c…` (`design.md` §5.1), diff = one line, `--check` exit 0 | 22:13Z |
| frozen generation `round-11` (10 rows) | `replay-frozen.py` → **10/10 reproduced, exit 0** in an isolated copy; tamper controls all fail closed (gate → `gate_digest_mismatch`, snapshot → `snapshot_tampered`, output → `expected_output_tampered`, each exit 2, no launch on could-not-evaluate rows) | 22:15Z and 22:19Z |
| wired e2e | `python3 tools/typed-gate-flow.py` → exit 0, 10/10 checks, findings 16 (hold 15, note 1), delta "10 PHON artifact(s) retired, 0 added, retained lines identical" | 22:17Z, 22:19Z |
| old generations / checkers (C3/C4) | every pre-change digest re-verified identical (round-3 manifests, all `r9-pre` `expected.json`, the five gates, `replay-frozen.py`, `check-gate-battery.py`); only the sanctioned changes moved | 22:16Z |
| green legs (claim D c6) | `d2-typed-labels --selftest` 39/39; `assemble-d2 --selftest` 42/42; `assemble-culture-d3 --selftest` 85/85; `check-gate-battery --selftest` 28/28; `d2-typed-labels --check` exit 0 (post re-pin) | 22:19Z |

Findings (details §4):

| id | pattern | severity | one line |
|---|---|---|---|
| **F-R22-1** | C1/C6 | **high (mechanism)** | `typed-gate-flow.py --emit` regenerates the expected set from the same run that produces the findings; nothing compares the new set with the previous one. Demonstrated: blank GAR-01's `garment` (record and its `form_slot` declaration kept) → no hold for GAR-01; pre-re-pin the flow exits 1; after `--emit` the flow exits **0** with 14 holds / 9 owed slots — the debt was blessed |
| **F-R22-2** | C2/C4 coverage | medium | the landed frozen generation pins the five source gates and the two packets, but **not** the flow itself nor its hold-set output (`typed-gate-flow.out` sits unpinned in the generation; the flow cannot be a `replay-frozen` row because it lives outside `tools/gates/`). A later edit to the flow or its expected set leaves the replay green |
| **F-R22-3** | C3 mechanism | medium | `--freeze DIR` has no append-only guard: a second freeze into the same directory silently overwrote a marker line (exit 0, demonstrated in `.scratch/d22/freeze-test`) |
| **F-R22-4** | consistency | medium | the expected set's identity column changed mid-wave (`where` `GAR-0N` → `LEX-GAR-0N`, 22:14Z → 22:18Z readings; expected file regenerated 19:17:05−03:00) with no receipt; `design.md` §4.2 still names `GAR-0N` |
| **F-R22-5** | fragment hygiene | low | `shard-assembler.md` declares its adapter source sha `3f67af66…` (22:12Z); the scratch file at 22:13Z hashed `95ac9d05…` (selftest 22/22). The fragment's landing check is stale |
| **F-R22-6** | derivative count | low | the D26 ledger and the X04 draft record `D2L-NATIVE ×1`; the projector's own JSON has `D2L-NATIVE ×2` (L-15, L-16) — 15 holds = 10 FORM + 2 NATIVE + 3 RANK |
| **F-R22-7** | design conformance | low | `design.md` §3.2 prescribes an exit-semantics banner ("exit 0 = the emitted findings equal the frozen expected hold set; every hold below is still open design debt"); the landed `report()` prints no such line (grep: the wording occurs in no tool output). The substance is visible — the 15 hold lines are emitted verbatim and `findings: 16 (hold 15, note 1)` is printed — but the explicit "exit 0 is not clean" sentence is missing |
| **F-R22-OOL** | out-of-lane, reported | conformance | seven **filed** earlier-round receipts were rewritten in the worktree during the wave (cause and evidence §5.5); not this re-pin's work, reported for the owner of the sweep |

Bottom line for the parent: the re-pin as *delivered* is a legitimate new-generation freeze of current bytes, and the claim's equality assertion holds against the committed expected set; but "a re-pin that changes the hold set is reported as a finding, not a pass" (`design.md` §5.2) is **discipline, not mechanism** for this expected-set family — nothing stops or records a shrink. §7 lists the four concrete guards, all cheap.

## 1. What "the re-pin" is, and why circularity is the right audit

Claim **D** (`reports/round-11/claims.json`) wires the round-8 typed-label projection into the D2 gate flow: "findings must equal the expected hold set exactly", "frozen replay re-pinned and green". The lane's standard (`corpus/knowledge/verification/gate-frozen-run-standard.md` §3 append-only, §5 freeze procedure, §6 verify mapping) and the round-8 precedent (`reports/round-8/depth/test-replay.md` §6: never re-bless pins in place; re-freeze under a new generation directory) fix what a legitimate re-pin looks like.

A re-pin is the lane's canonical place for a change to bless itself: the freeze procedure records what was **observed** (§5 step 5), which is correct for a regression pin and tautological by construction. The audit question is therefore **what independent evidence remains outside the loop** — authored expectations, tamper controls, unchanged old generations, verdict-preservation probes, and mutation controls showing the verdict is computed from the input rather than copied from the declaration.

### 1.1 Threat model — six self-blessing patterns

| id | pattern | what would show it | what rules it out |
|---|---|---|---|
| C1 | **harvested expectation**: the "expected" set is transcribed from the run under test | the set is regenerated from the run and nothing else anchors it | an authored source names the same members; mutation of the input moves the verdict |
| C2 | **tautological pin**: the new pin is produced by the tool under test over its own output, nothing else constrains it | freeze steps "run → capture → pin" with no pre-change snapshot and no cross-check | pin names byte-copied snapshots; a pre-registered prediction or an old-generation probe |
| C3 | **in-place re-bless**: an earlier generation is edited so old pins name new bytes | any pre-change digest moves | §2 digest table re-verified at close |
| C4 | **checker co-change**: the verification path is edited so the change defines its own green | checker digests differ | checker digests unchanged, or a reviewed co-change with its own controls |
| C5 | **verdict rewrite**: the re-pin changes an expected finding set with no per-change justification | new expectation differs from the old on the same inputs | every changed expected row dispositioned; before/after record |
| C6 | **self-issued exemption**: the sound-channel exemption is driven by the same projection it validates | mutating the input (not the projection) still yields exemption | input mutation flips the verdict; declaration and hold cross-checked against a source independent of the label row |

## 2. Pre-change baseline and the close-of-audit delta (C3 result)

Pre-change digests were captured by this seat at 2026-10-17T22:01:40Z (rev `e3ef171`), full output `.scratch/d22/baseline-digests.txt`; the close sweep (`.scratch/d22/close-digests.txt`) re-hashed the same set. **Delta: only the two sanctioned changes.**

| artifact | pre-change | close of audit |
|---|---|---|
| `tools/assemble-d2.py` | `8ea6bdde…c8655d` | unchanged |
| `tools/d2-typed-labels.py` | `0da0015f…89c802` | unchanged |
| `tools/replay-frozen.py` (checker) | `a2fb5c98…c79464` | unchanged |
| `tools/check-gate-battery.py` (checker) | `0a126b70…e1aa1` | unchanged |
| the five culture gates | `d5fe087f…`, `2c4dd397…`, `5368b135…`, `e6bffd70…`, `d9e4e8f4…` | unchanged |
| `tools/gates/frozen/round-3/MANIFEST.tsv` / `attempt-1` | `d5337590…` / `613e5945…` | unchanged |
| the five `r9-pre` `expected.json` files | `9dc21cd5…`, `0fad58ba…`, `425c74c0…`, `2763614f…`, `7ec01a1d…` | unchanged |
| `examples/culture-d2/packet.d2.yml` | `e0f21509…` | unchanged |
| `examples/culture-d2/typed-labels.d2.yml` | `e70ba147…` | **`a3aa452c…`** — the re-pin (predicted, §3.1) |
| `tools/typed-gate-flow.py`, `examples/culture-d2/{packet.d2.typed.yml,typed-gate.expected.json}`, `tools/gates/frozen/round-11/**` | absent | new files (the wiring and its generation) |

No earlier-round artifact was touched by the re-pin: C3 ruled out. (The separate rewrites of filed *receipts* under `reports/round-5..9/` are F-R22-OOL, §5.5 — not this seam.)

## 3. Independent verification of the delivered re-pin

### 3.1 Projection re-pin (C2 evidence: a pre-registered prediction that came true)

`design.md` §5.1 predicted the post-re-pin bytes **before** the act: `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`. In an isolated mirror (`.scratch/d22/wire/`):

```sh
python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml   # exit 1 (findings), wrote 3010 lines
sha256sum examples/culture-d2/typed-labels.d2.yml   # a3aa452c… = the prediction
diff <committed copy> examples/culture-d2/typed-labels.d2.yml   # one line: packet_sha256 8da90b07… → e0f21509…
python3 tools/d2-typed-labels.py --check            # exit 0
```

The match is not self-fulfilling: the predicted value was filed in `design.md` (22:06Z) before the re-emit, so the implementation could have failed it. (It is a determinism claim, not an independent correctness claim.)

### 3.2 Frozen generation `tools/gates/frozen/round-11/` (10 rows)

- Manifest `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376` (matches `repin.md`'s record; re-read 22:19Z).
- Rows: 5 gates × typed packet + 5 gates × legacy packet. Pins name the current gate bytes (verified against disk: `d9e4e8f4…`, `d5fe087f…`, `e6bffd70…`, `2c4dd397…`, `5368b135…`). Inputs are byte copies: `packet.d2.yml` `e0f21509…` = live; `packet.d2.typed.yml` `e8a83445…` = live (re-hash 22:19Z).
- Independence: `clean` replay in an isolated copy (`.scratch/d22/ctl-r11/`): **10/10 reproduced, exit 0** (22:15Z and again 22:19Z after the generation's refresh).
- Tamper controls (my harness, one mutation per fresh copy): gate byte → 2 rows `gate_digest_mismatch`, exit 2; snapshot byte → 5 rows `snapshot_tampered`, exit 2; recorded output byte → 1 row `expected_output_tampered`, exit 2; no could-not-evaluate row launched a gate.
- Verdict content: typed naming row exit 1 / 7 findings (`feb64881…`) vs legacy 17 (`ebc8850d…`); the differential is exactly the ten `GAR-*` `PHON-INVENTORY` lines. Reproduced independently in my own mirror via the D03 adapter fragment as well: legacy 17 → typed 7, diff `7,16d6`, zero `PHON-INVENTORY` in the typed run (22:13Z).

**Invocation caveat for the parent's counting run:** in the lane with the round rule's `TMPDIR=$PWD/.scratch`, `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` exits **2** `mirror_unsafe` (temp root inside the repo root; 10/10 could-not-evaluate, 22:19Z). Use a TMPDIR outside the repo (as `reports/round-11/run-validation.py` documents) or `--repo-root <isolated tree>`. This is fail-closed behaviour, not a red generation.

### 3.3 The wired e2e and the expected set

`python3 tools/typed-gate-flow.py` → **exit 0**, 10/10 checks, findings 16 (hold 15, note 1); `delta: 10 PHON artifact(s) retired, 0 added, retained lines identical`; the flow emits the 15 hold lines verbatim (severities included), `typed sound channel: 0 translated-label artifact(s)` and `findings: 16 (hold 15, note 1)`. The `design.md` §3.2 banner sentence ("exit 0 = …; every hold below is still open design debt") is **not** printed by the landed `report()` (F-R22-7). The expected file (`examples/culture-d2/typed-gate.expected.json`, `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa`) carries: `expected_findings` 16, `owed_slots` = `LEX-GAR-01..10`, `packet_sha256 e0f21509…`, `typed_packet_sha256 e8a83445…`, the per-gate verdict bundle, and a `basis` naming the independent grounding (component `form_slot` declarations; 05-lexicon supplies no `LEX-GAR-*`; supplement-22 §1/§5(a); round-8 design-spec §1.3/§6/§7/§8).

This seat's own grounding checks of the set's members: the ten `D2L-FORM-UNRESOLVED` holds correspond to the ten declared slots in `examples/culture-d2/components/11-costumes.yml:407-416` and the ten `form_slot` strings in the packet (re-verified: packet form_slot slots = 10 = committed `owed_slots`); `L-15`/`L-16` are real lexemes (`packet.d2.yml:684,697`) and the `sára`/`sará` accent pair is declared by 02-phonology's own `minimal_pair_delivered` (component line 73); the `TR-04`/`SR-01`/`WR-*` rule ids exist in `12-rank-rules.yml:318,431` and are referenced by packet records. The 3 `R-RANK` holds' *classification* (genuine-priority-gap) stays the rank adapter's judgement — `to-verify` (§6).

### 3.4 C4 — checkers unchanged

`tools/replay-frozen.py` (`a2fb5c98…`) and `tools/check-gate-battery.py` (`0a126b70…`) are byte-identical to the pre-change baseline, and none of the five gate scripts moved. The new flow tool is new code with its own control matrix (`--selftest` 14/14, exit 0 at 22:16Z and 22:19Z), covering tamper, smuggled-label, dropped-owed-form, laundered-hold, malformed and missing-input cases.

## 4. Findings by pattern

### F-R22-1 (C1/C6, high, mechanism) — the expectation is regenerable from the observation, and nothing compares the old and new sets

`tools/typed-gate-flow.py --emit` writes **both** derived artifacts from the same run:

```python
if args.emit:
    Path(args.typed_packet).write_bytes(result["derived_bytes"])
    Path(args.expected).write_bytes(result["expected_bytes"])
```

and `expected-file-current` then requires the committed expected file to equal `render_expected(expected_doc)` for the current run. So the expected set is, by construction, a snapshot of the current behaviour; its authority rests on (a) the `basis` block naming independent sources, (b) the frozen generation, (c) the design's written guard "a re-pin that changes the hold set is reported as a finding, not a pass" — which **no command enforces or records** for this family. (D08's scratch `repin-frozen.py`, 31/31 selftest, does enforce verdict-delta refusal — but for the TSV/`kotodama-frozen-run-v1` families, not `kotodama-typed-gate-expected-v1`.)

**Demonstration (isolated mirror `.scratch/d22/wire4/`, flow sha `5758e315…`, 22:19Z).** The edit is a *plausible* authoring slip, not a hostile one: blank GAR-01's display string while keeping the record and its `form_slot` declaration (`garment: ""`; the assembler accepts it, exit 0; the packet still carries `form_slot: "LEX-GAR-01, …"`).

| step | command | result |
|---|---|---|
| 1 | `python3 tools/typed-gate-flow.py` | exit **1**, 5 FAIL checks — `hold-set-equal` (observed 15 findings vs expected 16), `expected-pins`, `expected-delta-match`, `expected-file-current` |
| 2 | `python3 tools/typed-gate-flow.py --emit` | exit 0 — regenerates the typed packet **and** the expected set (15 findings, 9 owed slots) |
| 3 | `python3 tools/typed-gate-flow.py` | exit **0**, 10/10 checks — the dropped owed form is now the frozen expectation |

The record still declares its slot in the packet (the obligation was machine-visible), but the flow derives `owed_slots` from the *typed label row* (`build_typed_packet` marks `owed_form` only for records the projection types as `translated-label`), so record and hold vanish together and `owed-slots-crosscheck` passes vacuously (9 vs 9). Same class as `neg-18.md` fx18a (label-row-derived hold) — the wiring inherits it: the cross-check compares two derivations of the same source, so it cannot see a jointly-shrunk set.

What *does* catch the class today: any input edit without a re-pin fails on pins (step 1). What does not: a re-pin, because nothing diffs the expectation against the previous generation, the component's `form_slots` ledger, or the packet's own `form_slot` declarations.

### F-R22-2 (C2/C4, medium) — the frozen generation does not pin the flow or its hold-set output

The round-11 generation's 10 rows are the five source gates over the two packets. `typed-gate-flow.out` (the file that carries the 15 holds and the 10-check verdict) is present but **not a manifest row**; `tools/typed-gate-flow.py` and `examples/culture-d2/typed-gate.expected.json` are pinned by nothing in the generation. `replay-frozen.py` whitelists gates as `*.py` directly under `tools/gates/`, so the flow cannot be a row where it lives (this is why `design.md` §5.2 asked for a `tools/gates/typed-pipeline-gate.py` row pinning exit 0 / 15 findings / stdout — the landed shape deviates). Consequence: a later edit to the flow or to its expected set leaves `replay-frozen round-11` at 10/10. The standard's §3 index (`tools/gates/frozen/README.md`) is also still absent, and no `freeze.txt` / `repin.json` records the generation's revision/author/before-after state.

### F-R22-3 (C3 mechanism, medium) — `--freeze` overwrites an existing generation

Demonstrated in `.scratch/d22/freeze-test/` (scratch only): freeze into `gen/` (exit 0, "froze 10 row(s)"), append `MARKER-IN-PLACE` to its `MANIFEST.tsv`, freeze again into the same `gen/` → exit 0, marker **gone**. The standard's "existing baselines are never rewritten" is unenforced here; the lane itself was observed refreshing `round-11` files at 22:17:28Z / 22:18:17Z (consistent with re-freezing into the existing directory; the manifest hash did not change because inputs and gates did not).

### F-R22-4 (C5, medium) — an unreceipted expectation change mid-wave

At 22:14Z the generation's `typed-gate-flow.out` and the flow's output named the ten holds `where: GAR-0N` (also `design.md` §4.2); at 22:18Z the same artefacts name `where: LEX-GAR-0N` (the expected file was regenerated at 19:17:05−03:00 after a flow revision at 19:17:01). The substance is benign (the same ten records/slots; arguably the better identity), but no receipt records the change of the identity column, and `design.md` §4.2 still carries the old spelling. This is precisely the C5 pattern — an expectation rewritten without a before/after record — in its mildest possible form; it shows why F-R22-1's guard is needed.

### F-R22-5 (low) — fragment/source hash drift

`shard-assembler.md` §1 declares `.scratch/D03/assemble-d2-typed.py` sha `3f67af66349d3bcaaa0eaa279853a24c017f031ae3c8be729fe94472cff4209d` (450 lines, "22:12Z") and gives it as the integrator's landing check; at my read (22:13Z) the same path hashed `95ac9d05ff880234e4fafa33de3cac09db2fee248c760c61fa2dda7631318215` (selftest 22/22 from a lift-shaped mirror). The integrator must not land by the fragment's hash. (For the record: the *landed* wiring is `tools/typed-gate-flow.py`; the D03/D04 adapter files are not in `tools/`.)

### F-R22-6 (low) — derivative count

`reports/round-11/depth/scribe.md` §1.2 and `reports/round-11/report-draft.md` record `D2L-NATIVE ×1`; the projector's own `--json` (the scribe's saved receipt `.scratch/D26-typed-json.json`) has `D2L-NATIVE ×2` (`L-15`, `L-16`), and 15 holds = 10 `D2L-FORM-UNRESOLVED` + 2 `D2L-NATIVE` + 3 `D2L-RANK` holds (plus 1 `D2L-RANK` note). The authoritative set (expected file, design §4, review-21) is 16 findings / 15 holds; the derivative documents should be corrected before admission.

### F-R22-7 (low, design conformance) — the exit-semantics banner is not implemented

`design.md` §3.2 requires the flow to print, before the finding lines, one banner naming the semantics ("exit 0 = the emitted findings equal the frozen expected hold set; every hold below is still open design debt"). The landed `report()` (`tools/typed-gate-flow.py`) prints no such line, and the wording occurs in no tool output (`grep -n 'still open' tools/typed-gate-flow.py` → no hit; readings at 22:19Z and 22:20:50Z, flow `5758e315…`). The substance is visible — the 15 hold lines are emitted verbatim with severities and `findings: 16 (hold 15, note 1)` is printed — but the one-line guard the design wrote against "exit 0 read as clean" is missing; either implement it or amend the design.

## 5. Independent falsification runs by this seat

All runs were re-executed by this seat; scratch under `.scratch/d22/` with `TMPDIR=$PWD/.scratch`.

1. **Pre-wire mutation controls over the projector** (`.scratch/d22/mutations.py`, pre-change tools): M-A rename GAR-03's slot → the hold follows the input (`LEX-GAR-99`); M-B delete GAR-05's `form_slot` line → exit 2 with a new `D2L-DATA` fail, not a silent pass; M-C append a supplied native form bound to `LEX-GAR-03` → the hold clears (15 → 14), and the supplied form is checked against the inventory. Holds are computed from packet bytes.
2. **Adapter-level wiring** (D03 fragment lifted into a mirror): typed packet built (10 routing rows, 16 findings carried); naming gate legacy 17 → typed 7, diff exactly the ten `GAR-*` lines, 0 `PHON-INVENTORY`.
3. **The re-pin-blesses-a-shrink demonstration** (§4, F-R22-1), reproduced on the latest flow revision.
4. **Replay controls** over the landed generation (§3.2): clean 10/10 exit 0; three tamper classes exit 2 with the right reasons.
5. **Filed-receipt contamination (F-R22-OOL, out-of-lane — reported, not absorbed).** `git status --short` at 22:06Z shows seven filed earlier-round files modified, all stamped 22:01–22:03Z: `reports/round-5/validation.json` (−361 lines, `passed:true` → `passed:false`), `reports/round-6/validation.json` (−421), `reports/round-6/checkpoint-validation.json`, `reports/round-7/validation.json`, `reports/round-8/validation.json`, `reports/round-9/validation.json` (stdout pins/`git_status` fields updated to the current tree), `reports/round-10/coverage/index-update-22.md` (+68/−?). Cause, measured: `reports/round-5/run-validation.py:194` writes `validation.json` beside itself, and the F-claim's 1:1 recheck includes ledger rows 102/120/129/130/131 (`python3 reports/round-N/run-validation.py`); running a filed validator in the live tree overwrites its historical receipt. The rewritten round-5 receipt still contains its own claim "the previous acceptance receipt is regenerated only in an isolated copy, never overwritten in this tree". This is the same in-place re-bless class the audit guards against (direction: redder, not greener) and it also invalidates those receipts as historical evidence until reverted (round 10 reverted a comparable defect once: `LOG.md` round-10 "Conformance defects"). Recommended owner action: revert the seven paths (`git restore`), and re-run those ledger rows from a mirror or with output redirection.

## 6. Residual risk, limits, and what remains `to-verify`

1. **The claim's counting command was not run by this seat.** `python3 reports/round-11/run-validation.py` writes `reports/round-11/validation.json` (`reports/round-11/run-validation.py` exists, `4fdf3d5d…`); running it is outside this seat's write scope. The parent's acceptance run is the authority for the claim; the D-leg discovery must find the flow (its scan accepts `--e2e`/`--flow`/… flags or an e2e line in `reports/round-11/depth/*.md`).
2. **"Findings exactly equal the expected hold set" is a regression/equality assertion, not a clearance.** Verified as such: exit 0 with 15 holds carried and the holds printed verbatim. It must not be read as the culture being clean; the design's explicit banner sentence is missing (F-R22-7).
3. **Excluded populations must be stated.** The expected set is the projector's top-level `/findings` (16 entries). `design-review.md` DR-01 measured 9 further nested holds (`R-MAT-BRIDGE-MISSING` under `era_material_reconciliation`) and `rank_rules` debts carried as counters. They are excluded by construction; the expected file's `basis` does not say so. The round report (or the expected file's basis) should state the excluded population and its disposition, so "no more/no fewer" cannot silently mean "narrower".
4. **R-RANK classification** (`to-verify`): the three holds' `genuine-priority-gap`/`R-05-class` reading is the rank adapter's judgement; re-deriving it needs `reports/round-8/depth/shard-rank.md` §4 (out of this seat's scope).
5. **Moving target.** The flow changed three times inside the audit window (§0). All green readings name their stamps; re-run §3.1–§3.3 after the wave settles, and re-hash `tools/typed-gate-flow.py`, `examples/culture-d2/{packet.d2.typed.yml,typed-gate.expected.json}`, `tools/gates/frozen/round-11/MANIFEST.tsv` before quoting any reading.
6. **Not verified by this seat:** the flow's behaviour under `--typed-override`; the O-axis exercise; the freshness rechecks (claim F). Nothing here covers them.

## 7. Recommendations (concrete, with owners)

| # | recommendation | closes | owner |
|---|---|---|---|
| 1 | Make the re-pin emit a before/after record: `freeze.txt` (revision, stamp, command, author role) plus `repin.json` diffing `expected_findings` / `owed_slots` / `expected_delta` / `expected_gate_verdicts` against the previous generation, and **refuse** a `--freeze` that would change the hold set unless a `--allow-hold-change` flag is given (then record both sets). D08's scratch `repin-frozen.py` (31/31) is the working pattern; extend it to the `kotodama-typed-gate-expected-v1` family | F-R22-1, F-R22-3, F-R22-4 | D05/D08 + integrator |
| 2 | Add an obligation check independent of the label row: every packet record carrying `form_slot:` must be either on the checked channel or named by a hold/owed-slot (the ten declarations are already in the packet; a blanked display string must not remove the debt) | F-R22-1 residual | D05 (flow) |
| 3 | Cover the flow in the frozen generation: either land `tools/gates/typed-pipeline-gate.py` (replay-eligible) and add its row (exit 0, 15 findings / 16 lines, stdout pin — `design.md` §5.2's original intent), or pin `typed-gate-flow.out`'s sha in the generation's freeze record; add the `tools/gates/frozen/README.md` index and the `freeze.txt` | F-R22-2 | integrator |
| 4 | Add `--freeze` refusal for an existing generation directory (or a `--force` that records the overwrite and the before/after manifest digests) | F-R22-3 | D05 |
| 5 | Revert the seven rewritten filed receipts and re-run the affected ledger rows from a mirror; record the constraint "filed validators are never run in the live tree" in the round notes | F-R22-OOL | integrator / F-rerun seats |
| 6 | Correct the derivative count (`D2L-NATIVE ×2`) in `scribe.md`/`report-draft.md`; reconcile `design.md` §4.2's `where` column (`GAR-0N`) with the delivered expected set (`LEX-GAR-0N`) | F-R22-4, F-R22-6 | scribes / integrator |

## 8. Receipts

```sh
# lane root, 2026-10-17, export TMPDIR=$PWD/.scratch unless noted
git rev-parse HEAD                                                # e3ef1719… at audit start
sha256sum tools/assemble-d2.py … > .scratch/d22/baseline-digests.txt   # 22:01:40Z (pre-change table, §2)
diff <pre-change table> <close table>                             # only typed-labels.d2.yml + new files (§2)

# 3.1 projection re-pin (mirror .scratch/d22/wire/)
python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml   # a3aa452c…, diff 1 line
python3 tools/d2-typed-labels.py --check                          # exit 0

# 3.2 frozen generation (isolated, .scratch/d22/ctl-r11-gen2/)
python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv --repo-root <iso> --json
#   {'rows': 10, 'reproduced': 10, 'mismatch': 0, 'could_not_evaluate': 0, 'exit': 0}
# tamper: gate -> 2x gate_digest_mismatch; snapshot -> 5x snapshot_tampered; output -> 1x expected_output_tampered; all exit 2
# lane invocation with TMPDIR=$PWD/.scratch -> exit 2 mirror_unsafe (10x could-not-evaluate) — use TMPDIR outside the repo

# 3.3 wired e2e (lane)
python3 tools/typed-gate-flow.py                                   # exit 0, 10/10, findings 16 (hold 15, note 1)
python3 tools/typed-gate-flow.py --selftest                        # exit 0, 14/14

# §4 F-R22-1 demonstration (mirror .scratch/d22/wire4/, flow 5758e315…)
#   blank GAR-01 garment value in components/11-costumes.yml; python3 tools/assemble-d2.py  # exit 0
python3 tools/typed-gate-flow.py                                   # exit 1, 5 FAIL checks
python3 tools/typed-gate-flow.py --emit                            # exit 0
python3 tools/typed-gate-flow.py                                   # exit 0, 10/10 — 15 findings / 9 owed slots

# §4 F-R22-3 freeze-overwrite demonstration (.scratch/d22/freeze-test/)
python3 tools/typed-gate-flow.py --freeze …/gen                    # exit 0
printf 'MARKER-IN-PLACE\n' >> …/gen/MANIFEST.tsv
python3 tools/typed-gate-flow.py --freeze …/gen                    # exit 0; marker gone

# §5.5 filed-receipt contamination
git status --short                                                 # 7 filed paths modified, 22:01–22:03Z
git diff --stat -- reports/round-{5,6,7,8,9}/validation.json reports/round-6/checkpoint-validation.json reports/round-10/coverage/index-update-22.md
grep -n 'validation.json' reports/round-5/run-validation.py        # :194 writes beside itself

# §3.4 green legs
python3 tools/d2-typed-labels.py --selftest                        # 39/39
python3 tools/assemble-d2.py --selftest                            # 42/42
python3 tools/assemble-culture-d3.py --selftest                    # 85/85
python3 tools/check-gate-battery.py --selftest                     # 28/28
```

Scratch receipts: `.scratch/d22/{baseline-digests.txt,close-digests.txt,poll.log,mutations.py,replay-controls.py,pre-typed.json,flow-e2e*.out,flow-selftest.out,wire/,wire2/,wire3/,wire4/,ctl-r3-check/,ctl-r11-gen/,ctl-r11-gen2/,freeze-test/}`. This file's own sha256 is reported by the parent's integration step (a file cannot name its own hash without self-reference).

## 9. Close-of-audit snapshot (2026-10-17T22:20:50Z, rev `e3ef171` + wave)

Stable across the last two readings (22:19:03Z and 22:20:50Z):

| artifact | sha256 |
|---|---|
| `tools/typed-gate-flow.py` | `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` |
| `examples/culture-d2/typed-gate.expected.json` | `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` (16 findings, 10 owed slots; hold `where` = `LEX-GAR-0N`) |
| `examples/culture-d2/packet.d2.typed.yml` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` (== the generation's snapshot pin) |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376` |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` (the re-pin) |

At this snapshot `python3 tools/typed-gate-flow.py` → exit 0, `summary: 10/10 checks passed` (receipt `.scratch/d22/flow-close.out`). The wave may still write after this stamp; the parent's counting run on the settled tree is the authority.
