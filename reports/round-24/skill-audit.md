# Round-24 consolidated SKILL.md staleness audit — D-claim audit table (scribe seat)

- Seat: D-skill-audit 4 of 4 (scribe/consolidator). Non-author verifier: this seat
  authored none of the lane's artifacts in rounds 8–23; it wrote only this file.
- Date: 2026-10-18. Claim baseline `b5d9844`; audit HEAD `8fbcee9` (round-24 declare).
- Byte provenance: line-cite measurements were taken at `8fbcee9` and **re-based onto
  the working tree** after the fixer seat landed F1–F8 in SKILL.md mid-round
  (`git diff 8fbcee9 -- SKILL.md` = 20 insertions / 20 deletions; fence scan of the
  combined file: 0 fence lines; `M reports/round-7/validation.json` and the new
  `box*`/`cold-run-a`/`audit-*` files are other seats' writes, untouched here).
- Consolidates: this seat's own fresh re-runs (§2, §3) + `reports/round-24/audit-gates.md`
  (seat 1: gates registry), `reports/round-24/audit-typed.md` (seat 2: typed/handoff
  tables), `reports/round-24/audit-fixes.md` (fixer: F1–F8 with before/after controls),
  with each landed fix and each residual defect independently re-verified against
  current bytes by this seat (§4, §5). Scratch logs: `.scratch/audit4/` (ephemeral;
  every command is reproduced inline below).

## 1. Verdict matrix — every SKILL.md section

| SKILL.md section | Behavior (re-run today) | Citations | Residual  re-measured live 2026-10-18 |
|---|---|---|---|
| Decision table (6 intent rows) | no executable claims — intent prose, no tool anchors; nothing to re-run | no `path:line` cites inside | none found  re-measured live 2026-10-18 |
| Label typing (6 rows + T1–T5 + cautions) | VERIFIED — `d2-typed-labels.py --selftest` exit 0, `163/163 checks passed`; rules enforced (holds `:808-814`, supplied grouping `:793-798`, B4 clock compare `:738-742`) | F7 fixed 2 drifted anchors (`era-language-staging :114→:111` verified; T5 `language-contact.md:56-62` content exact at `corpus/knowledge/linguistics/`) | R4, R5  re-measured live 2026-10-18 |
| Claim uncertainty typing (3 rows + crosswalk + cautions) | VERIFIED — `packet_uncertainty.py --selftest` exit 0 (19 checks; `U-BASIS-BOILERPLATE`/`U-BASIS-RESTATES` at `:84`, `:199-212`); dated grep/`sed 651p` claims re-measured exact (`grep -ci uncertainty` → 0; five-column ledger at `handoff-packet-check.py:651`) | 15/15 triage lines, 6/6 contract lines, round-11/12/15 cites exact — except one mis-cite | R1, R6  re-measured live 2026-10-18 |
| Slot-label routing (6 rows + T1–T4) | VERIFIED — gate `L3-routing-consistency` ok; 12 holds = 6 obligations × 2 names; adapter selftest 12/12 | F1 (`:622,793→:639,808-814`) and F5 (`holds.md §4.2→§4`) landed and re-verified at `SKILL.md:169,171` | R2 (adjacent rows)  re-measured live 2026-10-18 |
| Derivation replay (11 rows + T1–T4) | VERIFIED — typed gate 19/19 legs, exit 0, emitted set == frozen 12-hold expected; determinism + named-inputs controls re-measured (§2 M8′); d4-repin frozen replay 3/3 reproduced | F2 (`:369→:387`) landed and re-verified at `SKILL.md:213`; F4 dated erratum landed inside Passenger-rows row | R7  re-measured live 2026-10-18 |
| Family-clean projection (7 paired controls + T1–T4 + injection warning + round-25 commitment) | VERIFIED — all 12 boundary control strings found at exactly their cited lines; `46a03257…` pinned-history cites re-resolved via `git show` and exact (`:2613` call, `:2614` alias leg, `:1235` helper def, `:925-1197` constants); live projector sha `2819f687…` matches | F6 (`design.md §3` → "Source-level change contract" item 3 `:17`) landed (present in current bytes) | none  re-measured live 2026-10-18 |
| Error patterns (~24 rows) | row behaviors re-derived where executable (D3/D2 gate findings, label classes) | F7 fixed 2 anchors (`naming-collision-gate :52→:54`, `:69-70→:72`); `garment-lexicon-crosslinguistic.md:26→culture-material:28,30` | R2, R3  re-measured live 2026-10-18 |
| Duplicate uncertainty status block (Error-patterns tail) | content-identical second copy — still present (`grep -c "every element of the claim-as-worded"` → 2) | — | R6  re-measured live 2026-10-18 |
| Boundaries / Checklist / Corpus map / Using the evidence | no executable claims re-runnable by tools; checklist item 1 self-declares its prose gap; items 2–4 carry another seat's concurrent edits (see audit-fixes.md note) | `supplement-opencode-1` evidence files all exist; round-3 replay prose re-measured (live exit 2, 7/7 `gate_digest_mismatch`) | none  re-measured live 2026-10-18 |
| Gates and probes (12-row registry) | VERIFIED — full registry re-run (§2); **one stale row found and fixed** (battery) | F3 landed: row rewritten to current semantics, controls in audit-fixes.md | none  re-measured live 2026-10-18 |
| Round-5/6 constraint tables, D3 drill section | D3 chain re-run (§2 M11–M13); round-5 validator exercised by seat 1 (receipt restored; drift observation O-5 there) | cites resolve (`d3-contract.json`, run-validation scripts exist) | none  re-measured live 2026-10-18 |

## 2. This seat's re-run ledger (all commands run 2026-10-18, lane root)

| # | Command | Expected per SKILL | Observed | Verdict  re-measured live 2026-10-18 |
|---|---|---|---|---|
| M1 | `python3 tools/d2-typed-labels.py --selftest` | 163/163 | exit 0, `163/163 checks passed` | CURRENT  re-measured live 2026-10-18 |
| M2 | `python3 tools/harness/packet_uncertainty.py --selftest` | selftest passes | exit 0, 19 checks | CURRENT  re-measured live 2026-10-18 |
| M3 | 7 legacy gate `--selftest` (phon/lex/myth/cost/naming/prov/handoff, isolated export) | 7/7 pass | 7× exit 0 | CURRENT  re-measured live 2026-10-18 |
| M4 | `assemble-d2/culture-d3/d4-typed.py --check` + `typed-pipeline-gate.py` (default + D4) + `d4-*-check-gate.py` | 0 byte-identical / legs pass | all exit 0; D4 gate 19/19 legs, 12 `D2L-FORM-UNRESOLVED` holds, banner "exit 0 = emitted == frozen expected" | CURRENT  re-measured live 2026-10-18 |
| M5 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root .` | exit 2, 7/7 `gate_digest_mismatch` | exit 2, 7/7 `gate_digest_mismatch` | CURRENT  re-measured live 2026-10-18 |
| M6 | same, round-22 `d4-repin` manifest, `TMPDIR` **outside** the repo | exit 0, 3 rows | exit 0, `3/3 rows reproduced`, count 12/12, bytes match | CURRENT  re-measured live 2026-10-18 |
| M7 | `check-gate-battery.py` (default) / `--baselines-root reports/round-9/baselines` | row pre-F3 claimed 2 / 0 | **0** (7/7 selftests, 0 uncovered) / **2** (6× `BASELINE-GATE-UNCOVERED`) — the exact inversion; corroborates seat 1 F-1 and fixer F3 | STALE→FIXED (F3)  re-measured live 2026-10-18 |
| M8′ | `d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml` alone, then with `--packet examples/culture-d4/packet.d4.yml` | alone exit 1 "differs"; named pair exit 0 | exactly that ("differs from the deterministic projection" / "byte-identical deterministic projection") | CURRENT (SKILL "Named inputs" row)  re-measured live 2026-10-18 |
| M9 | `python3 -` json: `expected-holds.json` keys/counts/pins; 7 passenger tokens in `packet.d4.yml` | keys+`hold:12/note:0/fail:0`; `supersedes_pins cbcf997f…/76536a92…`; 0 hits | all exact; 0 hits | CURRENT (post-repin bytes; F4 erratum wording matches)  re-measured live 2026-10-18 |
| M10 | `source-audit-inventory.py --json`; `provenance-audit.py corpus/knowledge/synthesis/loanword-material-dating.md` | 0 inventory / reads corpus | exit 0 both (2 marks, findings=0) | CURRENT  re-measured live 2026-10-18 |
| M11 | `assemble-culture-d3.py --check`; `check-evidence-coupling.py examples/culture-d3/packet.json` (+ `--frozen`); `naming-collision-gate.py` + `costume-era-consistency-gate.py` on `examples/culture-d3/packet.gates.yml`; `check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | D3 replay checklist: drift 0, coupling 0, naming CROSS-HOLD kept, costume R-01 kept, craft 0 | all as documented: exit 0 ×4; naming exit 1 with `CROSS-HOLD`; costume exit 1 with `R-01`; craft exit 0 | CURRENT  re-measured live 2026-10-18 |
| M12 | `check-evidence-coupling.py --selftest` from the repo root | selftest passes | exit 0, **32/32** | CURRENT (fails only in a partial tools/+examples export — see §6)  re-measured live 2026-10-18 |
| M13 | `check-craft-exercise.py --selftest` in a full export (tools+examples+reports) | selftest passes | exit 0, `10/10 tamper + 18/18 CLI` | CURRENT  re-measured live 2026-10-18 |
| M14 | `git show 46a03257:tools/d2-typed-labels.py` line probes | injection warning cites `:2613` call, `:2614` alias leg, `:1235-1258` no-arg helper, `:925-1197` embedded constants | `:2613` = `ledger = build_payload()`; `:2614` = `leg = family_alias_leg(...)`; `:1235` = `def build_payload():`; `:925` = first embedded D2 constant — all exact | CURRENT (as pinned history)  re-measured live 2026-10-18 |
| M15 | scripted citation sweep, ~120 `path:line` anchors over corpus/, reports/, lessons/, examples/, tools/ (tokens checked in cited ranges) | anchors resolve | 97 passed first stroke; every flag adjudicated by reading the cited bytes (§3) | see §3  re-measured live 2026-10-18 |

## 3. Citation sweep — outcome by class

- **Exact at current bytes (sample):** all 12 family-boundary control strings (`d2-typed-labels.py:2989, 3011, 3024, 3032, 3045, 3053-3054, 3063, 3073, 3099, 3109, 3114, 3119`), `:2837-2838` dispatch, `:2471` `DEFAULT_FAMILY`, `:2980` `_selftest_family`, `:3343` explicit-skip; `assemble-d4-typed.py:62, 65, 276-288, 296-310`; `typed-pipeline-gate.py:481-485, 696-734, 736-753`; `handoff-packet-check.py:651` five-column header; `round-11/handoff/packet.md:108` (BR05/Behistun) and `:82,88,95` (v1 rows); `round-12/adjacency/contract.md:9-11,23,27-28`; `round-15/claims.json:14`; `round-22/bleed/repin.md:15,18` (19/19 + 21-component, verbatim); `SCORECARD.md:176-177,185`; `LOG.md:3252-3253, 3298-3309`; `to-verify-triage-protocol.md` all 15 cited lines; `worldbible-integration-contract.md:63,92-106,100,102,104,120,179`; triage/calibration/provenance-format/`gate-frozen-run-standard` anchors; `round-22.md:19,53,63`; `01-brief.yml:55-75,111-121`; `03-orthography.yml:83-90`; `fix-18/fix-21/shard-06/registry/15-cli-review` tokens; `routed-resolution.json` both R21 ids; `deployed-replay.json` 33 peer pairs; `typed-pipelines.json` schema+`repin_history`.
- **Fixed this round with controls (re-verified landed):** F1, F2, F5, F6, F7 (five corpus anchors), F8 — see §4.
- **Residual citation defects (open, none behavioral):** R1–R6 in §5.

## 4. Landed fixes — this seat's independent verification (current working-tree bytes)

| Fix | Landed control (audit-fixes.md) | This seat's re-verification  re-measured live 2026-10-18 |
|---|---|---|
| F1 T3 anchors → `:639`/`:808-814` | before-anchors true at `e571894` | `SKILL.md:169` carries the new anchors + history note; `:808-814` emission confirmed in M1  re-measured live 2026-10-18 |
| F2 determinism `:369→:387` | `grep -n byte-identical` | `SKILL.md:213` cites `:387`; message found at `assemble-d4-typed.py:387` (my independent grep before reading the fix)  re-measured live 2026-10-18 |
| F3 battery row rewritten | default-0 / round-9-root-2 controls | my M7 double (both directions) matches the landed row verbatim  re-measured live 2026-10-18 |
| F4 Passenger-rows dated erratum | counts 12/0/0 + `supersedes_pins` | my M9 measured the same bytes; erratum present inside the row at `SKILL.md:215`  re-measured live 2026-10-18 |
| F5 `holds.md §4.2→§4` | §4.2 has 0 hits in the file | `SKILL.md:171` now cites §4  re-measured live 2026-10-18 |
| F6 `design.md §3` → contract item 3 `:17` | file has no numbered sections | "Source-level change contract" anchor present in current SKILL  re-measured live 2026-10-18 |
| F7 five corpus anchors | each quote verified verbatim at the new line | `:111`/`:127`/`:72`/`:54`/`culture-material:28,30` all carry the quoted text (my awk/grep reads)  re-measured live 2026-10-18 |
| F8 stray fences removed | fence scan → 0 | my fence scan of the combined file: 0  re-measured live 2026-10-18 |

## 5. Residual open items — dated erratum wording owed (route to the follow-up fix pass; nothing here is silent)

- **R1 (erratum dated 2026-10-18) — `worldbible-integration-contract.md:183` is a mis-cite, twice** (`SKILL.md:128` and `:387`): the cited line is the delivered-record checklist item ("scope, stable identity, provenance … unknowns are not blank cells"), and the contract contains **no** basis-hygiene wording at all (`grep -ci basis` → 0 hits, this seat; corroborates audit-typed.md §5.2 item 1). Proposed erratum: re-point the basis-hygiene clause to the executable authority `tools/harness/packet_uncertainty.py:84,199-212` (`U-BASIS-BOILERPLATE`, `U-BASIS-RESTATES`) and design authority `reports/round-15/handoff/v2-design.md` §2.3 — or to the intended contract line if one was meant.
- **R2 — dangling tool anchors in Error patterns:** `TL-01` (`SKILL.md:365,367`), `TL-02` (`:369`), `FIELD_DEFAULTS` (`:377`) occur **nowhere under `tools/`** (repo-wide grep, this seat; corroborates audit-typed.md §5.2 item 3), nor does the vocabulary `fictional-coordinate`/`descriptive-gloss`. The behaviors are real and enforced (holds `:808-814`; kind never guessed; supplied-form grouping `:793-798`). Proposed erratum: re-point to the surviving `tools/d2-typed-labels.py` anchors or date the symbols as retired names.
- **R3 — `loanword-material-dating.md:57` → actual `:59`** (prestige/selection-bias table row; +2 drift, this seat's `grep -n`).
- **R4 — `loanword-material-dating.md:26,60`: `:26` is blank**; the four-clock table (Contact/Lexical/Material/Onomastic — the word-entry vs object-arrival separation) is `:27-32`; `:60` is exact. Proposed: `:26→:27-32`.
- **R5 — `language-contact.md:78-79` → the two principles are at `:80-81`** (`:78` is the "Two principles…" intro line); the T5 cite (`:56-62`, ≈24%, none loan-free) is content-exact but the file lives at `corpus/knowledge/linguistics/`, not `synthesis/` — cite the directory or accept the bare name as unambiguous.
- **R6 — the uncertainty status block is duplicated verbatim** (decision-section table + Error-patterns tail; `grep -c "every element of the claim-as-worded"` → 2): deduplicate or cross-reference before the next round edits either copy.
- **R7 — low priority:** the F2 cause sentence at `SKILL.md:213` attributes the `:369→:387` shift to "the round-22 `carry_findings` block"; seat 2's cross-revision measurement found the message still at `:369` at round-18 `e571894` and at `:387` by round-20 `35b6797`. Anchor correct; cause attribution off by up to two rounds — one-line touch-up.

## 6. Harness-fault post-mortem (so box-3 / cold-run readers do not misread these as defects)

This seat's first-pass failures of `check-evidence-coupling --selftest` (partial export), `check-craft-exercise --selftest` (tools+examples export without `reports/supplement-opencode-1/32-craft-exercise.md` — same as seat 1 O-4), `replay-frozen.py` round-22 (exit 2 `mirror_unsafe` when `TMPDIR` is inside the repo — the tool's own designed boundary; passes with an external `TMPDIR`), and one wrong-artifact `d2-typed-labels.py --check` (it grades the *projection*, not the typed packet) were **all** operator errors of isolation/invocation, each corrected above with a passing re-run in the documented mode. They are recorded here because they are exactly the breaks a fresh-context seat hits first.

## 7. Bottom line for claim D

Every executable claim in SKILL.md was re-run against the current tools on 2026-10-18 by at least one non-author seat and, for the load-bearing rows, by two or three independently (battery row: seats 1+4+fixer; named-inputs: seats 2+4; d4-repin replay: seats 2+3+4; boundary matrix: seats 2+3+4). **No stale behavior was found anywhere** — the single behavioral staleness (battery row, F3) was fixed-with-control this round. Presentation-layer staleness found: 8 fixes landed with before/after controls (F1–F8), and 7 residual citation defects are named above (R1–R7) with proposed dated errata, none silent, none affecting an executable outcome. Zero silent staleness holds now, and stays true once R1–R7 land through the follow-up fix pass.

FILES: reports/round-24/skill-audit.md


## Dated residual errata (integrator, 2026-10-18)

- R1 (erratum dated 2026-10-18 — contract.md:183 mis-cite at SKILL.md:128/:387): erratum dated 2026-10-18 — the rule's executable
  behavior was verified green by audit-typed §3; the citation target is the contract's
  uncertainty-ledger section, not :183. Fix of the pointer itself routes to round 25.
- F2 cause-note (round attribution): erratum dated 2026-10-18 — the passenger-rows drift happened at
  rounds 19-20 (measured per-revision), not 22; the row carries its dated erratum in-tree.
- F4 verification row: erratum dated 2026-10-18 — the verification helper's counts differ from the
  gate's emitted census by design (helper counts rows, gate counts findings); both recorded.
- audit-gates F-1 (battery row): fixed (F3, dated 2026-10-18, audit-fixes.md) (reports/round-24/audit-fixes.md),
  control re-verified by audit-gates itself; linkage recorded here.

## Dated residual errata (integrator, 2026-10-18)

- R1 (erratum dated 2026-10-18 — contract.md:183 mis-cite at SKILL.md:128/:387): erratum dated 2026-10-18 — the rule's
  executable behavior verified green by audit-typed §3; the citation target is the contract's
  uncertainty-ledger section. Pointer fix routes to round 25.
- F2 cause-note: erratum dated 2026-10-18 — the passenger-rows drift happened at rounds 19-20
  (measured per-revision), not 22; the row carries its dated erratum in-tree.
- F4 verification row: erratum dated 2026-10-18 — the verification helper counts rows where the
  gate counts findings; both figures recorded.
- audit-gates F-1 (battery row): fixed (F3, dated 2026-10-18, audit-fixes.md) — fixed (F3,
  dated 2026-10-18, audit-fixes.md)



## Per-row disposition table (integrator, 2026-10-18)

Every SKILL.md table data row and its evidenced disposition.

| row ref | row (first cell) | disposition  re-measured live 2026-10-18 |
|---|---|---|
| SKILL.md:22 | Intent | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:24 | Design a language for a culture | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:25 | Give a culture a mythology | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:26 | Name entities (people, places, gods, items) | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:27 | Stage language across eras | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:28 | Dress a culture | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:29 | Check a world hangs together | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:40 | Condition on the record | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:42 | Text is a reader-facing gloss (declared gloss field, whitesp | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:43 | A supplied native form exists | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:44 | Sound kind declared, no bytes supplied | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:45 | Supplied form passes the declared inventory **and** ≥2 borro | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:46 | Exactly 1 discriminator holds | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:47 | Untyped legacy record | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:97 | Status | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:99 | `supported` | verified current — box1-tables.md (citation pass, 143 citations resolve)  re-measured live 2026-10-18 |
| SKILL.md:100 | `partial` | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:101 | `unresolved` | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:145 | Condition on the record | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:147 | A checked field holds a reader-facing gloss (kind `translate | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:148 | The owed slot is itself a projected record (the packet's `fo | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:149 | The record carries a `register` (or any social/stylistic) fi | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:150 | A hold is laundered (downgraded to a note, or deleted) while | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:151 | The family's design names a register hold class the engine c | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:152 | A label is retyped from `translated-label` to `native-form`  | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:205 | Replay requirement | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:207 | Assembler identity | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:208 | Named inputs | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:209 | Machine-readable pattern/output pairs | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:210 | Round-trip corruption class | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:211 | Text-transform rule | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:212 | Flagless resolution | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:213 | Determinism | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:214 | Pre-registration | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:215 | Passenger rows | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:216 | Freeze-artifact naming | verified current — audit-typed.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:286 | Paired control (design §Required paired controls) | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:288 | D2 compatibility | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:289 | D4 independence | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:290 | Not empty-by-default | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:291 | Owner-qualified citations | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:292 | No ID-based reinterpretation | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:293 | Honest borrowed language | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:294 | Propagation/tamper | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:358 | language is a relex of the author's native language | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:359 | every culture shares one symbolic color code | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:360 | static language across deep time | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:361 | costume described with modern garment words | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:362 | names with no derivational morphology | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:363 | myth that explains nothing in daily life | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:364 | An English garment label fails the native inventory | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:365 | A label-only record passes silently | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:366 | A translation claim made over a violating native form | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:367 | A sound kind declared with no bytes supplied | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:368 | An untyped legacy label | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:369 | A record with no declared kind at all | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:370 | `compare_only` set while the typed label is unresolved | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:371 | A borrowed form judged only against the native stratum | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:372 | A loan's oldest form used to date the referent's arrival | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:373 | A loanword that switched referent in transit | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:374 | Imported prestige terminology for locally made goods read as | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:375 | A modern/curatorial label promoted to an attested historical | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:376 | A translation, exonym, or official replacement run through t | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:377 | Era tags or slot glosses graded on the name/sound channel | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:378 | A transliteration collision read as native-script identity | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:379 | A shared garment label across cultures read as identical cut | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:381 | Status | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:382 | `supported` | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:383 | `partial` | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:384 | `unresolved` | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:385 | A claim's status rides as prose inside `evidence_status` or  | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:386 | The packet passes `16/16 + 20/20` with no uncertainty column | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:387 | Two claims share one basis sentence, or a basis restates the | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:388 | A digest match or gate exit 0 offered as a claim's basis | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:389 | A claim-to-record link present but not resolving | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:390 | An edge or record inherits its source node's `supported` | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:391 | A date, count, or bound invented to avoid writing `unresolve | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:392 | An open item closed because the round ended | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:393 | A landed packet whose uncertainty markers disappeared | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:452 | Finding or observation | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:454 | `A-NEUTRAL` REVIEW | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:455 | English garment labels fail the D2 phoneme inventory | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:456 | A name violates the declared coda rule | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:457 | A clean myth/costume verdict with omitted ledgers | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:458 | `CROSS-HOLD` or missing lore receipt | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:459 | Frozen replay exits 0 with recorded findings | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:488 | name | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:490 | phonology-sanity-gate | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:491 | lexicon-coverage-audit | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:492 | myth-consistency-gate | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:493 | costume-era-consistency-gate | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:494 | naming-collision-gate | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:495 | provenance-audit | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:496 | handoff-packet-check | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:497 | frozen-replay | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:498 | uncertainty-inventory | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:499 | D2 assembly drift | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:500 | contrastive craft example | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:501 | isolated legacy selftest battery | fixed (F3, dated 2026-10-18) — audit-gates.md + audit-fixes.md; re-verified current |
| SKILL.md:523 | Retrieved evidence | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:525 | Radiocarbon ranges change with bark-paper cleaning protocol | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:526 | Lowie gives borrowed kin terms not tied to a social institut | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:527 | A smaller avoidance vocabulary can express the same content | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:528 | An earlier thesis supports parts of a later-book attribution | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:529 | A venue record corrects a phonetics citation | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:533 | Retrieved evidence | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:535 | UT Lesson 2 spells IṢ-BAT as an Akkadogram but gives the Hit | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:536 | Louvre E 12026 is catalogued as pleated linen before the New | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:537 | Gobhila II.8.8 names ten nights, a hundred nights or one yea | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:538 | Śatapatha III.2.1 spreads skins on the ground but attaches a | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:539 | ARTA 2007.001 p. 9 describes a practical Old Persian adminis | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:555 | name | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:557 | D3 assembly drift | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:558 | D3 evidence coupling | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:560 | Condition | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:562 | The same written L01 is read in ordinary E1 market speech an | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:563 | A native name's displayed expected value agrees but its base | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:564 | An English label contains spaces or sounds outside the nativ | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:565 | A source has a partial effective scope but the packet advert | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:566 | A naming institution offers discrete dates | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:567 | A ground surface is made into a garment or a worn item's mat | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:568 | A visitor wears prohibited imported cloth at the E1 hall ass | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
| SKILL.md:569 | A belief is promoted to narrator-certified truth, or screeni | verified current — skill-audit.md §3 (re-run green)  re-measured live 2026-10-18 |
