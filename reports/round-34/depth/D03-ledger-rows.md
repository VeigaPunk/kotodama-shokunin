- Seat: D03 | executor (claim-ledger rewrite) | D | date 2026-10-19 | baseline da68a6d

**Mission:** every number-bearing row of the new packet's D4 section, rewritten to live values, each cell citing its live source line.

**Method.** I did not trust any prose. Every number below is read from the live artifact bytes at baseline `da68a6d` with a deterministic sweep (script in §9, run from `.scratch/d03/number-sweep.py`); the three source files are digest-pinned in §1. Nothing under `reports/round-1..33/**` was edited or executed; the only commands run were `sha256sum`, `grep`, `python3 -` readers and the two D4 gates (§3, evidence lines). No round runner was invoked.

## 1. Live-value census (measured at da68a6d, this run)

Digest pins at read time:

| artifact | sha256 |
|---|---|
| `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` |
| `examples/culture-d4/packet.d4.yml` | `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` |

| quantity | live value | live source line (file:line) |
|---|---|---|
| typed_labels | 82 | `examples/culture-d4/typed-labels.d4.yml:46` |
| labels_by_kind native-form | 64 | `examples/culture-d4/typed-labels.d4.yml:37` |
| labels_by_kind translated-label | 12 | `examples/culture-d4/typed-labels.d4.yml:38` |
| labels_by_kind borrowed-strata | 6 | `examples/culture-d4/typed-labels.d4.yml:36` |
| findings_total | 12 | `examples/culture-d4/typed-labels.d4.yml:32` |
| findings_hold_or_fail | 12 | `examples/culture-d4/typed-labels.d4.yml:31` |
| label_findings_fail | 0 | `examples/culture-d4/typed-labels.d4.yml:33` |
| label_findings_hold | 12 | `examples/culture-d4/typed-labels.d4.yml:34` |
| conflicts | 0 | `examples/culture-d4/typed-labels.d4.yml:30` |
| rank_quarantine_handles | 0 | `examples/culture-d4/typed-labels.d4.yml:40` |
| rank_rules_unresolved_items | 0 | `examples/culture-d4/typed-labels.d4.yml:44` |
| reconciliation_records | 6 | `examples/culture-d4/typed-labels.d4.yml:45` |
| stats fail / hold / labels | 0 / 12 / 82 | `examples/culture-d4/typed-labels.d4.yml:2866-2868` |
| expected-holds counts hold / note / fail | 12 / 0 / 0 | `examples/culture-d4/expected-holds.json:47-49` |
| expected-holds hold rows | 12 (all `D2L-FORM-UNRESOLVED`, severity `hold`) | `examples/culture-d4/expected-holds.json:53-120` (12 `id`/`severity` pairs, census run) |
| expected-holds notes rows | 0 (`notes` list empty) | `examples/culture-d4/expected-holds.json` `notes` key (python census: `len(notes)=0`) |
| era_material_reconciliation records | 6, every `findings` entry empty | `examples/culture-d4/typed-labels.d4.yml:48-` (6 `"record":` occurrences, 0 non-empty findings) |
| era_material summary | claims 6, findings 0 | `examples/culture-d4/typed-labels.d4.yml` `"summary"` block (`"claims": 6, "findings": 0`) |
| era_reconciliation alias_rows | 4 | `examples/culture-d4/typed-labels.d4.yml:137` (4 entries counted) |
| form_slots status | 6 × `unfilled` (5 `native-form`, 1 `borrowed-strata`) | `examples/culture-d4/packet.d4.yml:2491-2527` (lines 2496, 2502, 2508, 2514, 2520 native-form; 2526 borrowed-strata) |
| rank_rules gate rows | 4, all `adapt_status: executable` | `examples/culture-d4/typed-labels.d4.yml:322,357,391,426` (8 occurrences = component 4 + gate-projected 4) |
| rank act_rules / unresolved / quarantine / residuals | `[]` / `[]` / `[]` / `[]` | `examples/culture-d4/typed-labels.d4.yml:306-310` (`act_rules: []`), `:595` (`unresolved: []`), `:603` (`quarantine: []`), `:604` (`residuals: []`) |
| `cannot-evaluate` occurrences in D4 projection | 0 | `grep -c cannot-evaluate examples/culture-d4/typed-labels.d4.yml` → `0` |
| component registry rows | 13 (`C-01`..`C-13`) | `examples/culture-d4/components/01-brief.yml` (`id: C-\d+` census = 13; `C-13` at `:161`) |
| D4 component files | 13 | `ls examples/culture-d4/components/*.yml` = 01-brief … 13-register-law |
| packet.d4.yml assembly source pins | includes `13-register-law.yml` | `examples/culture-d4/packet.d4.yml:2887-2888` |
| D4 scope counts (lexicon/names/symbols/costumes/rank rules/contact layers) | 62 / 8 / 8 / 6 / 4 / 2 | `examples/culture-d4/packet.d4.yml` id-prefix census (`L:62`, `NM:8`, `SYM:8`, `GAR:6`, `RK:4`, `CT:2`) |
| brief's declared hold set | 6 holds / 0 notes / 0 fails | `examples/culture-d4/components/01-brief.yml:206-216` (`counts: {hold: 6, note: 0, fail: 0}` at `:216`; A-07 restates it at `:235`) |

Gate legs (run live, read-only; not round runners):

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
summary: 20/20 legs passed            exit 0
$ python3 tools/gates/d4-typed-labels-check-gate.py
examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic projection   exit 0
$ python3 tools/assemble-d4-typed.py --selftest
selftest: 12/12 checks passed …       exit 0
$ python3 tools/d2-typed-labels.py --selftest
selftest: 163/163 checks passed …     exit 0
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml
summary: 13/13 legs passed            exit 0
stdout sha256 9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606
```

## 2. Stale → live delta (filed `declared-in-r6/packet.md` at `da68a6d`)

| # | cell | filed (stale) | live | class |
|---|---|---|---|---|
| 1 | `:148` D4-CL05 grounding | typed_labels 74, native-form 56, findings_total 16, findings_hold_or_fail 15 | 82, 64, 12, 12 | declared in claim D |
| 2 | `:148` D4-CL05 grounding `#stats` | labels 74 | labels 82 (fail 0, hold 12 unchanged) | declared in claim D |
| 3 | `:148` D4-CL05 statement | 74 labels / 56 native-form / 16 findings / 15 hold-or-fail | 82 / 64 / 12 / 12 | declared in claim D |
| 4 | `:149` D4-CL06 grounding+statement | hold 15, note 1; "three D2L-RANK rows, plus one D2L-RANK note"; +9 hold delta | hold 12, note 0; zero rank holds, zero notes; +6 hold / +0 note delta | declared in claim D |
| 5 | `:150` D4-CL07 grounding+statement | conflicts 4, quarantine handles 3 | 0, 0 | declared in claim D |
| 6 | `:152` D4-CL09 grounding+statement | unresolved rank items 13, quarantine handles 3, conflicts 4 | 0, 0, 0 | declared in claim D |
| 7 | `:307` OQ-V3-05 | twelve form + three rank + one note; 13 / 3 / 4 | twelve form + zero rank + zero notes; 0 / 0 / 0 | declared in claim D |
| 8 | `:151` D4-CL08 grounding | `tools/d2-typed-labels.py --selftest exit 0 50/50` | live `163/163` exit 0 | **sweep find** (§5) |
| 9 | `:144` D4-CL01 grounding+statement | "twelve authored inputs" / "twelve authored components" | 13 registry rows, 13 component files, 13 assembly pins | **sweep find** (§5) |
| 10 | `:20` scope field (D4 clause) | "twelve authored components" | 13 | **sweep find** (§5) |

Rows 1–7 are exactly the class claim D declares. Rows 8–10 are additional stale figures found by walking every numeric token in the D4 region (§8 control, §9 script) — they are in the same rows/section, so the new packet cannot ship them and still meet "every claim-ledger/OQ number equal to a measured live value".

## 3. Replacement rows — exact bytes for the assembler

Splice each fenced block in place of the row at the stated line of the new packet. Column count (7) and the closed uncertainty grammar (`grounding:`, `open:` + `owner:`) are preserved; every `links` cell is byte-identical to the filed row, so `packet_links.py` / `packet_uncertainty.py --require-oq` see the same link specs.

### 3.1 replaces the `D4-CL05` row (filed at `packet.md:148`)

```text
| D4-CL05 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#coverage (typed_labels 82, labels_by_kind native-form 64 / translated-label 12 / borrowed-strata 6, findings_total 12, findings_hold_or_fail 12, label_findings_fail 0) and examples/culture-d4/typed-labels.d4.yml#stats (fail 0, hold 12, labels 82), re-read from the delivered bytes; the projection is the projector's own output and the check leg reports byte-identical determinism | examples/culture-d4/typed-labels.d4.yml#coverage; examples/culture-d4/typed-labels.d4.yml#labels_by_kind; examples/culture-d4/typed-labels.d4.yml#stats; examples/culture-d4/typed-labels.d4.yml#typed_labels; tools/gates/d4-typed-labels-check-gate.py | The D4 typed channel types 82 labels — 64 native-form, 12 translated-label, 6 borrowed-strata — and carries 12 findings, all of them hold-or-fail (12 label holds, 0 label fails); the committed projection is the projector's own deterministic output, and its check leg reports byte-identity rather than a re-derivation. |
```

### 3.2 replaces the `D4-CL06` row (filed at `packet.md:149`)

```text
| D4-CL06 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/expected-holds.json#counts (hold 12, note 0, fail 0) with the row list, whose holds are twelve D2L-FORM-UNRESOLVED rows keyed to each garment twice and no D2L-RANK rows and no notes on the live bytes; the emitted set equals the committed file and reports/round-18/d4/holds.md reconciles the brief's six-row declaration with a documented +6 hold / +0 note delta rather than absorbing it | examples/culture-d4/expected-holds.json#counts; examples/culture-d4/expected-holds.json#holds; examples/culture-d4/components/01-brief.yml#hold_set_declaration; reports/round-18/d4/holds.md | The committed D4 hold set is 12 holds, 0 notes and 0 fails, pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to each garment twice (record id and slot id), and no `D2L-RANK` hold or note remains on the live bytes; the emitted set equals the committed file, and the round-17 brief's six-row declaration is reconciled by a documented +6 hold / +0 note delta rather than absorbed or silently re-declared. |
```

Derivation of the delta cell, for the record: brief declares 6 holds (`01-brief.yml:216` `counts: {hold: 6, note: 0, fail: 0}`), live emits 12 holds (`expected-holds.json:47`) and 0 note rows → `+6 hold / +0 note`. The filed `+9 hold / +1 note` was computed against the 15/1 set and cannot survive.

### 3.3 replaces the `D4-CL07` row (filed at `packet.md:150`)

```text
| D4-CL07 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation, six records GAR-01..GAR-06 each carrying an era block tagged E0 or E1 and a material block resolved by slot identity to a CMAT record, summary claims 6 findings 0; the same file's examples/culture-d4/typed-labels.d4.yml#reconciliation_records and examples/culture-d4/typed-labels.d4.yml#conflicts counts carry zero conflicts and zero quarantine handles without collapsing them | examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation; examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED; examples/culture-d4/typed-labels.d4.yml#reconciliation_records; examples/culture-d4/typed-labels.d4.yml#conflicts; examples/culture-d4/packet.d4.yml#materials | The D4 projection's era and material reconciliation resolves all six garment records by declared row and slot identity — each record's era block tagged in scope, each material block resolved to a `CMAT` record — with zero findings, while the projection's own conflicts (0), quarantine handles (0) and reconciliation records (6) are carried as counts rather than collapsed into a cleaner ledger. |
```

`six records`, `findings 0`, `reconciliation records (6)` are already live-correct and are kept verbatim; only the two counters move.

### 3.4 replaces the `D4-CL09` row (filed at `packet.md:152`) — numbers fixed; status wording flagged (§4)

```text
| D4-CL09 | designer interpretation | derived projection (author-side), holds open | unresolved | grounding: examples/culture-d4/typed-labels.d4.yml#rank_rules, whose four gate-projected rules now all carry adapt_status executable (component/gate-projected/normalized 4/4/4) with the foreign-leg skip recorded, and whose coverage block reports examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items 0, examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles 0 and examples/culture-d4/typed-labels.d4.yml#conflicts 0; open: the rank-rule residuals this row once re-carried are absent from the D4 projection on the live bytes, so the affected D2 rank records stay with the D2 family's own open row rather than this packet's; owner: kotodama, blocking for the six garment terms, not for this envelope | examples/culture-d4/typed-labels.d4.yml#rank_rules; examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items; examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles; examples/culture-d4/typed-labels.d4.yml#conflicts | The D4 projection's rank rules are all gate-modelled and executable (4/4/4) and its coverage block holds 0 unresolved rank items, 0 quarantine handles and 0 conflicts; the D2 normalization residuals that earlier revisions re-carried through D4 are no longer present in this projection, so this row's remaining debt is the form-slot holds plus the D2 family's own open row (D2-CL02 / OQ-V2-03), not D4 rank debt. |
```

### 3.5 replaces the `OQ-V3-05` bullet (filed at `packet.md:307`)

```text
- OQ-V3-05: D4's holds stay open on the six garment terms: twelve form holds and zero rank holds, with zero notes, zero unresolved rank items, zero quarantine handles and zero conflicts in the live coverage block — kotodama; blocking for the six garment terms, not for this envelope (unresolved claims: D4-CL09)
```

### 3.6 sweep-find rows (found by the §8 walk, not named in claim D)

`packet.md:151` (D4-CL08) — one clause only; replace `50/50` with `163/163`:

```text
the unchanged-foreign-path control is tools/d2-typed-labels.py --selftest exit 0 163/163
```

The other two cited legs in that row are live-exact and must not move: `assemble-d4-typed.py --selftest` = `12/12` (ran it), and the D2 gate leg = `13/13` with stdout sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` — byte-identical to the digest the row states.

`packet.md:144` (D4-CL01) — two words, same row: `twelve authored inputs` → `thirteen authored inputs` (grounding) and `twelve authored components` → `thirteen authored components` (statement).
`packet.md:20` (scope field, D4 clause) — `twelve authored components` → `thirteen authored components`. (The rest of that clause — 62 lexicon records, 8 names, 8 symbols, 6 costumes, 4 rank rules, 2 contact layers — is live-exact and stays.)

If the assembler prefers to keep the sweep finds out of this claim's diff, they must still be dispositioned as a named debt row: the new packet would otherwise carry three figures its own manifest rows contradict (`A-28` at `packet.md:68` already says "13 component digests in its assembly", and `A-30`/`A-31` already carry the 82/64/12/6, 12/0/0 set).

## 4. Flagged for D04 + D05 + integrator: D4-CL09's older narrative is structurally dead (to-verify)

Beyond the three counters, the filed row's prose describes bytes that no longer exist:

- "whose act rows carry `adapt_status` cannot-evaluate because speech is not a gate-modelled channel" — live `act_rules: []` (`typed-labels.d4.yml:306`), all 8 `adapt_status` occurrences are `executable` (`:322,357,391,426,464,499,533,568`) and `cannot-evaluate` occurs **0×** in the D4 projection and its typed twin (`grep -c` → 0,0), while it still occurs 19× in `examples/culture-d2/typed-labels.d2.yml`. The D4 projection's `skipped` row records the reason: "packet-native rank rules only; no foreign fixture data is imported" (`typed-labels.d4.yml` `rank_rules.skipped`).
- Consequence: the `unresolved` status of D4-CL09 is no longer implied by the numbers. Two defensible dispositions, neither of which is mine to pick:
  - (a) keep `unresolved` with the §3.4 wording (conservative; the row then routes the D2-side debt instead of carrying it) — this is what §3.4 does, and it is the recommended draft;
  - (b) reclassify to `supported` with the zero-residual statement, which changes the packet's supported/unresolved counts and therefore any downstream uncertainty tally — needs the assembler's and a verifier's decision, not a numbers seat's.
- Whichever is chosen, `OQ-V3-05` must move in step (its `unresolved_claims` names `D4-CL09`; twin.json holds the pair).
- Not claimed: that the D2 rank debt is closed. It is live at `examples/culture-d2/typed-labels.d2.yml:30,40,44` (4 conflicts / 3 quarantine handles / 13 unresolved items) and belongs to D2-CL02 / OQ-V2-03, which the new packet carries unchanged.

## 5. D4 rows whose numbers I re-checked and do NOT touch

| row | numbers in the row | live check |
|---|---|---|
| D4-CL02 | four records ER-01..ER-04 on E0..E3 | `packet.d4.yml` `ER-01..04` census = 4 |
| D4-CL03 | RK-01..RK-04 | `packet.d4.yml` `RK-01..04` census = 4 |
| D4-CL04 | six slots LEX-GAR-01..06; five owe a native-form | `packet.d4.yml:2491-2527` (5 native-form, 1 borrowed-strata) |
| D4-CL08 | alias_rows 4; 12/12; 13/13 + sha256 | `typed-labels.d4.yml:137` = 4; selftest 12/12; gate 13/13 sha256 match (§1) — only `50/50` moves (§3.6) |
| D4-CL10 | PR-01..PR-09 | `packet.d4.yml` `PR-01..09` census = 9 |
| D4-CL11, D4-CL12 | no numbers | — |
| `packet.md:69` A-29/A-30/A-31 manifest rows | 12 hold / 0 note / 0 fail; 82 (64/12/6); 12 findings; 0 unresolved rank items | all live-exact (§1) |

## 6. D2 control — evidence that this is a D4-only edit

The filed D2 rows are still live-accurate and must not be touched by the D4 rewrite: `examples/culture-d2/typed-labels.d2.yml:29-46` still reads conflicts 4, findings_total 16 with 15 hold-or-fail, rank_rules_unresolved_items 13, rank_quarantine_handles 3, reconciliation_records 10; `examples/culture-d2/expected-holds.json` counts still `hold 15 / note 1 / fail 0` (15 hold rows + 1 note). So D2-CL01, D2-CL02 and OQ-V2-03 are correct as filed, and the 74/56/16/15-class staleness is confined to the D4 family. Any edit that "fixes" the D2 rows by symmetry would be a false edit.

## 7. Twin parity (for D06 / the assembler)

`reports/round-30/handoff/declared-in-r6/twin.json` is generated from the same claims: `claim_ledger[19]` is `D4-CL05` and carries the stale statement/grounding text, and the `open_questions` list carries `OQ-V3-05` verbatim ("twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts"). Editing only the Markdown cannot move the twin — the new revision must regenerate the twin from the corrected packet, and the re-pin cascade must treat both members of the pair together (a mixed pair would pass the shape gate while contradicting itself, which is exactly the failure this claim is about).

## 8. Controls

Positive control (the method detects the filed staleness): a literal scan of the filed `packet.md` matches every declared-stale pattern — `typed_labels 74` ×1, `native-form 56` ×1, `findings_total 16` ×2, `findings_hold_or_fail 15` ×1, `hold 15` ×1, `note 1` ×1, `conflicts 4` ×1, `quarantine handles (3)` ×1, `unresolved_items 13` ×1, `thirteen unresolved rank items` ×2, `three D2L-RANK` ×2, `50/50` ×1, `twelve authored` ×3.
Negative control (the replacement bytes are clean): the 8 corrected cells in §3 yield **0** stale-context matches under the same patterns.
Boundary control (the gate cannot see this class): the filed pair is shape-green — `handoff-packet-check.py` / links / uncertainty judge shape and link resolution, not whether a number matches the artifact it cites; the filed rows' numbers were green at round 30 and are wrong today. That is the semantic-stale class my sweep catches and the gate cannot.

Delivered-rows control (run against this file's own §3 fenced blocks, after write): 4 replacement claim rows extracted; each 7/7 columns against the filed row, each `links` cell byte-identical to the filed row's links cell, each stale-free under the §8 pattern set; the OQ-V3-05 replacement is stale-free and still ends `(unresolved claims: D4-CL09)`. Output: `cols 7/7; links identical True; stale-free True` ×4, `ALL REPLACEMENT CONTROLS PASS: True`. Digest chain (each observation invalidated by the next edit): 23,764 bytes / `d7c4271489893e1a6cbf5a4c4847ac0215002cdcecb8d2c34cdd6967ce5f48a8` before this note landed; 24,381 bytes / `ea3e8bdf31c74e16d8f1f4085d05a5e4ebdb28b082a96b964d1fcda75677d0d8` after it — this sentence itself is the next edit, so the integrator's `sha256sum reports/round-34/depth/D03-ledger-rows.md` at apply time is the authoritative pin, and the two observed digests above are the reproducibility record.

Caveat, stated plainly: this sweep checks figures whose live referents I could reach with a counting command. It does not certify prose ("byte-identical determinism", "no lore baseline exists") — those are the links/uncertainty seats' surface.

## 9. The sweep, re-runnable (integrator may land it as a tool; I did not write outside my out path)

`.scratch/d03/number-sweep.py` — a stdlib-only reader that (a) parses the five number blocks out of `typed-labels.d4.yml`, the counts/rows out of `expected-holds.json`, the `unfilled` slot census out of `packet.d4.yml` and the registry census out of `01-brief.yml`; (b) walks every numeric token in `packet.md` lines 20, 144–155, 306–308; (c) prints the live census. Run from the repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Observed output this run: 97 numeric tokens scanned, live census as §1, and the §8 control counts. Any D05/draft packet can be pointed at it by changing `PACKET`.

## Owed

- `reports/round-34/adj/A02-handoff.md` — the "live 82/64/12/12+0/0/0/0" fragment claim D cites as its live-number source; it did not exist when I ran (only `claims.json`, `targets.json`, `telemetry/` in `reports/round-34/`). I measured the live values myself instead (digests in §1), so my rows do not depend on it; the integrator should cross-check my census against A02 when it lands and file any disagreement against this fragment.
- `reports/round-34/scout/K01-packet-state.md` — filed-rows census fragment (absent at my run); its expected content overlaps §2 rows 1–7, which I derived independently.
- `reports/round-34/depth/D05-packet-draft.md` — the merged draft the assembler applies §3 into; my rows are the byte source for lines corresponding to `:144,:148,:149,:150,:151,:152,:20,:307` of the filed revision.
- Better: apply §3.4 option (a) or (b) — the state question in §4 is unresolved by design; D04's OQ refresh + a non-author verifier own it.
- Regenerate the twin with the packet (§7) and re-pin every surface that pins `declared-in-r6` (D10/K02's census), including `tools/exercise-handoff-e2e.py:1933-1934`, as new rows — drafted by D10, applied by the integrator.

## Citations

- `REGIMEN.md` (round contract, per-round contract and scope); `reports/round-34/claims.json` (claim D `before`/`after_required`/`thresholds`); `reports/round-34/targets.json` (seat D03 mission + `shared_rules`).
- `reports/round-30/handoff/declared-in-r6/packet.md:20,125,144-155,299-308` (filed rows, read-only).
- `reports/round-30/handoff/declared-in-r6/twin.json` (`claim_ledger[19]`, `open_questions`).
- `examples/culture-d4/typed-labels.d4.yml:29-47,48-63,137,290-310,322,357,391,426,464,499,533,568,595,603-612,2865-2871`.
- `examples/culture-d4/expected-holds.json:46-49,53-120` + python census (`holds` 12, `notes` 0, `pin_generations` r28/r30).
- `examples/culture-d4/packet.d4.yml:2491-2527,2528-2533,2887-2888` + id-prefix census.
- `examples/culture-d4/components/01-brief.yml:161,206-216,235`.
- `examples/culture-d2/typed-labels.d2.yml:29-46`; `examples/culture-d2/expected-holds.json` counts (D2 control).
- `tools/gates/typed-pipeline-gate.py` (13/13 D2 run, 20/20 D4 run), `tools/gates/d4-typed-labels-check-gate.py` (byte-identical), `tools/assemble-d4-typed.py --selftest` (12/12), `tools/d2-typed-labels.py --selftest` (163/163), `tools/gates/handoff-packet-check.py` (docstring: shape-only judging).
- Command outputs: `sha256sum examples/culture-d4/{typed-labels.d4.yml,expected-holds.json,packet.d4.yml}`; `git log --oneline -1` → `da68a6d`; `git status --porcelain` → only `?? reports/round-34/` (no filed bytes touched); `grep -c cannot-evaluate` (0/0/19); `.scratch/d03/number-sweep.py` run (97 tokens, §8 controls); `.scratch/d03-gate-out.txt` (D2 gate stdout, sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`).
