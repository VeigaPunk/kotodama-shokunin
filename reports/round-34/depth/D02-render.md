- Seat: D02 | executor | claim D | date 2026-10-19 | baseline da68a6d

## Mission (targets.json, seat D02, verbatim)

"Render the new packet: run tools/exercise-handoff-e2e.py against a BUILD of the packet from live bytes (follow D01's sketch; do NOT touch the renderer defaults — the integrator applies that); write the rendered packet draft bytes under your out as a fenced block + the exact command."

D01's sketch `reports/round-34/depth/D01-layout.md` was **absent** at dispatch time (`find reports/round-34 -type f` returned only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`). Proceeded per the missing-dependency rule: used the renderer's own `--freeze` path as the build, and recorded the owed sketch under `## Owed`.

## 1. The exact build/render command (verified, exit 0)

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/d02
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d02/rendered
```

stdout (exit 0, ~3.2 s):

```
frozen: 2026-10-19 by tools/exercise-handoff-e2e.py --profile v3
packet_sha256: 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
twin_sha256: 6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e
gate: exit 0, fields=16/16, glossary-entries=20, findings=0
semantics: uncertainty exit 0, links 105/105 resolved
claims: 27 statuses 16/7/4; v2-subset ad35c860acf3b452…; alias leg landed
read set: 58 files; component digests 26/26; d4 pins 8/8
no tracked value changed since the previous freeze
froze .scratch/d02/rendered: packet sha256 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
```

- `--freeze DIR` renders the packet from the live read set and writes the five-file revision set (`packet.md`, `twin.json`, `expected.json`, `freeze.txt`, `run.log`) into `DIR`; it refuses to write anything if preflight, gate, uncertainty or links go red (`tools/exercise-handoff-e2e.py:3978-3992,:4101`).
- **The renderer defaults were not touched.** `--freeze` takes its target from argv and never reads `V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT` (`tools/exercise-handoff-e2e.py:1933-1934`, consumed only at `:4571-4572` on the verify path). The integrator's equivalent command for the filed revision is the stdout's last line with the round-34 path:

```bash
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7
```

## 2. Result: the render reproduces the filed r6 bytes EXACTLY

| file | rendered (`.scratch/d02/rendered/`) | filed (`reports/round-30/handoff/declared-in-r6/`) | verdict |
|---|---|---|---|
| packet.md | 105,584 B, sha256 `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` | same bytes, same sha | **byte-identical** (`cmp` silent) |
| twin.json | 103,625 B, sha256 `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e` | same bytes, same sha | **byte-identical** (`cmp` silent) |
| run.log | 1,603 B, sha256 `b5ee33510af0297e162e24bcdcf4aea563cbf7f3d112faf85720587479e3ed47` | same bytes, same sha | **byte-identical** (`cmp` silent) |
| expected.json | sha256 `0ad28212bc6a76103b65532a4b2c95f3016c4ef9877ad03281a3404438a4b7eb` | sha256 `ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0` | differs in exactly two keys: `/frozen_at` (`2026-10-19` vs `2026-10-18`) and `/baseline_digest` (folds `frozen_at`) |
| freeze.txt | 521 B (9 lines) | 586 B (includes the r6→r30 re-freeze diff lines) | differs: no previous baseline existed in my empty target dir |

Read-set drift check against the r6 pins (`expected.json.inputs`, 58 paths):

```bash
python3 - <<'PY'
import json, hashlib
b=json.load(open('reports/round-30/handoff/declared-in-r6/expected.json'))
drift=[(r,b['inputs'][r][:12],hashlib.sha256(open(r,'rb').read()).hexdigest()[:12]) for r in b['inputs']
       if hashlib.sha256(open(r,'rb').read()).hexdigest()!=b['inputs'][r]]
print('read set', len(b['inputs']), 'drift', len(drift), drift)
PY
# read set 58 drift 0 []
```

Verify-path cross-check (the claim's second counting command; the delivered pair is shape-green today):

```bash
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
# handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
#   statuses=16/7/4 v2_subset=equal alias_leg=landed
#   packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
```

**Binding consequence for claim D (`after_required`).** `packet.md`/`twin.json` are a pure function of (a) the 58-file read set, (b) the renderer source, (c) the filed `reports/round-20/handoff/claims-map.md` prose, (d) the filed `reports/round-15/handoff/packet-v2-05.yml` rows. With read-set drift at 0, re-running the renderer — or moving the default to a freshly frozen `declared-in-r7` — yields **byte-identical output carrying the same stale digits**. The r7 revision therefore cannot be produced by render or default-move alone: the digits must change in the sources that feed the render (§5), i.e. the shared-file drafts the integrator applies.

## 3. The rendered draft bytes

The full 105,584-byte draft is byte-for-byte the filed `reports/round-30/handoff/declared-in-r6/packet.md` (§2); every byte outside the five rows below is already the correct r7 byte. These are the exact current bytes of the five rows the r7 revision must change — retrieved from the render output with

```bash
sed -n '148p;149p;150p;152p;307p' .scratch/d02/rendered/packet.md
```

| packet.md line | byte offset | row bytes (incl. trailing LF) | sha256(row incl. LF) |
|---|---|---|---|
| 148 (D4-CL05) | 42501 | 1096 | `0e5bc28cdb1f378a49afab498986bcdf1df8b3ad66a2790d23a88ba22c3b5363` |
| 149 (D4-CL06) | 43597 | 1151 | `645ca6a12043fbf8fe513724667225739f94e0ca682cc6110245c41fe6efa1d5` |
| 150 (D4-CL07) | 44748 | 1207 | `7f9b2cea55faf24be7de3989b61d9fdc28e580058f9f50e864c5cdc341e2b454` |
| 152 (D4-CL09) | 47619 | 1375 | `1fee5414867484dfae984bfccc69ac6164fe26135c3a232247a765cee69e2dfd` |
| 307 (OQ-V3-05) | 102007 | 311 | `29cc0b72cc0059bcbc3ff495a7b14d67106da2053548a2a0761f003717553f45` |

Section context for splicing: `## claim_ledger` starts at line 123, `## coupling_edges` at 157 (so the D4 rows sit in the last table of the ledger block, D4-CL01..D4-CL12 = lines 144-155); `## open_questions` starts at 297 and OQ-V3-05 is the second-to-last row of that block (OQ-V2-01..OQ-V2-07 lines 299-305, OQ-V3-04 306, OQ-V3-05 307, OQ-V3-06 308) — all offsets from `grep -n '^## ' reports/round-30/handoff/declared-in-r6/packet.md`.

Line 148 — D4-CL05 (stale: typed_labels 74 / native-form 56 / findings_total 16 / findings_hold_or_fail 15):

```
| D4-CL05 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#coverage (typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 16, findings_hold_or_fail 15, label_findings_fail 0) and examples/culture-d4/typed-labels.d4.yml#stats (fail 0, hold 12, labels 74), re-read from the delivered bytes; the projection is the projector's own output and the check leg reports byte-identical determinism | examples/culture-d4/typed-labels.d4.yml#coverage; examples/culture-d4/typed-labels.d4.yml#labels_by_kind; examples/culture-d4/typed-labels.d4.yml#stats; examples/culture-d4/typed-labels.d4.yml#typed_labels; tools/gates/d4-typed-labels-check-gate.py | The D4 typed channel types 74 labels — 56 native-form, 12 translated-label, 6 borrowed-strata — and carries 16 findings of which 15 are hold-or-fail (12 label holds, 0 label fails); the committed projection is the projector's own deterministic output, and its check leg reports byte-identity rather than a re-derivation. |
```

Line 149 — D4-CL06 (stale: hold 15, note 1, twelve FORM + three RANK holds, one RANK note):

```
| D4-CL06 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/expected-holds.json#counts (hold 15, note 1, fail 0) with the row list, whose holds are twelve D2L-FORM-UNRESOLVED rows keyed to each garment twice and three D2L-RANK rows, plus one D2L-RANK note for the band-keyed pair; the emitted set equals the committed file and reports/round-18/d4/holds.md reconciles the brief's six-row declaration with a documented +9 hold delta rather than absorbing it | examples/culture-d4/expected-holds.json#counts; examples/culture-d4/expected-holds.json#holds; examples/culture-d4/components/01-brief.yml#hold_set_declaration; reports/round-18/d4/holds.md | The committed D4 hold set is 15 holds, 1 note and 0 fails, pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to each garment twice (record id and slot id) and three `D2L-RANK` holds, plus one `D2L-RANK` note for the band-keyed pair; the emitted set equals the committed file, and the round-17 brief's six-row declaration is reconciled by a documented +9 hold / +1 note delta rather than absorbed or silently re-declared. |
```

Line 150 — D4-CL07 (stale: conflicts (4), quarantine handles (3)):

```
| D4-CL07 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation, six records GAR-01..GAR-06 each carrying an era block tagged E0 or E1 and a material block resolved by slot identity to a CMAT record, summary claims 6 findings 0; the same file's examples/culture-d4/typed-labels.d4.yml#reconciliation_records and examples/culture-d4/typed-labels.d4.yml#conflicts counts carry four conflicts without collapsing them | examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation; examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED; examples/culture-d4/typed-labels.d4.yml#reconciliation_records; examples/culture-d4/typed-labels.d4.yml#conflicts; examples/culture-d4/packet.d4.yml#materials | The D4 projection's era and material reconciliation resolves all six garment records by declared row and slot identity — each record's era block tagged in scope, each material block resolved to a `CMAT` record — with zero findings, while the reconciliation's own conflicts (4), quarantine handles (3) and reconciliation records (6) are carried as counts rather than collapsed into a cleaner ledger. |
```

Line 152 — D4-CL09 (stale: rank_rules_unresolved_items 13 / rank_quarantine_handles 3 / conflicts 4, "thirteen unresolved rank items, three quarantine handles and four conflicts"):

```
| D4-CL09 | designer interpretation | derived projection (author-side), holds open | unresolved | grounding: examples/culture-d4/typed-labels.d4.yml#rank_rules, whose act rows carry adapt_status cannot-evaluate because speech is not a gate-modelled channel, with examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items 13 and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles 3 and examples/culture-d4/typed-labels.d4.yml#conflicts 4 in the same file's coverage block; open: the thirteen unresolved rank items, three quarantine handles and four conflicts are inherited D2 normalization residuals and none of them is promoted by this packet; owner: kotodama, blocking for the affected D2 rank records, not for this envelope | examples/culture-d4/typed-labels.d4.yml#rank_rules; examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items; examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles; examples/culture-d4/typed-labels.d4.yml#conflicts | The D4 projection re-carries D2's rank-rule adaptation rows with `adapt_status: cannot-evaluate` — speech is not a gate-modelled channel — and the packet's coverage block holds 13 unresolved rank items, 3 quarantine handles and 4 conflicts; none of them is promoted, resolved or hidden by this packet, and they are inherited D2 normalization residuals rather than D4 design debt. |
```

Line 307 — OQ-V3-05 (stale: "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts"):

```
- OQ-V3-05: D4's inherited and own holds stay open: twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts — kotodama; blocking for the affected D2 rank records and the six garment terms, not for this envelope (unresolved claims: D4-CL09)
```

Rows 151 (D4-CL08) and 153-155 are the only other rows in the D4 block and carry **no** live-contradicting figure: D4-CL08's `alias_rows 4` matches live (`examples/culture-d4/typed-labels.d4.yml#era_reconciliation.alias_rows` = 4 rows), and D4-CL04's form-slot text matches live (`examples/culture-d4/packet.d4.yml#form_slots` = six slots, all `status: unfilled`). A full-packet token sweep for the stale figures (`74 labels`, `native-form 56`, `typed_labels 74`, `hold 15`, `15 holds`, `note 1`, `four conflicts`, `three quarantine`, `thirteen unresolved`, …) hits lines 148, 149, 150, 152, 307 and **no others**; the remaining hits (L49, L129-130, L266-267, L284, L301) are D2-scoped figures that are still live (58 labels / 16 findings / 13 unresolved / 3 quarantine / 4 conflicts / 10 reconciliations — measured below).

## 4. Live values behind each stale figure (measured 2026-10-19 at da68a6d)

| stale text | live value | live source | measuring command |
|---|---|---|---|
| `typed_labels 74` | **82** | `examples/culture-d4/typed-labels.d4.yml#coverage.typed_labels` | `python3 -c "import json;print(json.load(open('examples/culture-d4/typed-labels.d4.yml'))['coverage'])"` |
| `native-form 56` | **64** (translated-label 12, borrowed-strata 6) | same `#labels_by_kind` | same |
| `findings_total 16` / `findings_hold_or_fail 15` | **12** / **12** (`label_findings_hold` 12, `label_findings_fail` 0) | same | same |
| `hold 15, note 1, fail 0` | **hold 12, note 0, fail 0**; the 12 hold rows are all `id: D2L-FORM-UNRESOLVED`, `where` = `GAR-01..06` **and** `LEX-GAR-01..06` (each garment twice), `notes` list empty | `examples/culture-d4/expected-holds.json#counts` and `#holds` | `python3 -c "import json;e=json.load(open('examples/culture-d4/expected-holds.json'));print(e['counts'],[h['id'] for h in e['holds']][:3],len(e['notes']))"` |
| `(fail 0, hold 12, labels 74)` cited as `typed-labels.d4.yml#stats` | the anchor resolves — `stats` is a key **nested inside the projection block**, not top-level (no top-level `stats`; the 11 top-level keys are assembly, canon, coverage, era_material_reconciliation, era_reconciliation, findings, generator, label_kinds, name, rank_rules, typed_labels). Live `stats` = **fail 0, hold 12, labels 82** at `examples/culture-d4/typed-labels.d4.yml:2866-2869`; only the quoted `labels 74` is stale, so the row needs a corrected value, not a re-point | `examples/culture-d4/typed-labels.d4.yml:2866-2869` (`"stats": {fail 0, hold 12, labels 82}`); `#coverage.typed_labels` 82 | `sed -n '2866,2869p' examples/culture-d4/typed-labels.d4.yml`; `python3 -c "import json;print(sorted(json.load(open('examples/culture-d4/typed-labels.d4.yml'))))"` |
| `rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`, `conflicts 4` | **0**, **0**, **0** (`reconciliation_records` stays **6**) | `typed-labels.d4.yml#coverage`; `#rank_rules.unresolved` = 0 rows, `#rank_rules.quarantine` = 0 rows | as above |
| D4-CL07 "conflicts (4), quarantine handles (3) … reconciliation records (6)" | conflicts **0**, quarantine **0**, reconciliation records **6** (`era_material_reconciliation`: records 6, findings 0) | `typed-labels.d4.yml#coverage`, `#era_material_reconciliation` | as above |
| D2 figures quoted in OQ-V2-03 / D2 rows (13 unresolved / 3 quarantine / 4 conflicts / 10 reconciliations; 58 labels / 16 findings) | **still live, unchanged** | `examples/culture-d2/typed-labels.d2.yml#coverage` | same probe on the D2 file |

Row texts and live values are D03's (`depth/D03-ledger-rows.md`) and D04's (`depth/D04-oq-glossary.md`) replacement input; this seat supplies only the before-bytes and the measured after-values.

## 5. Where the stale digits enter the render (two routes, both shared/filed bytes)

Route A — the 12 D4 ledger rows are parsed **verbatim from a filed round-20 artifact**: `tools/exercise-handoff-e2e.py:184` pins `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"`, and `v3_parse_claims_map` (`:2289-2321`) reads `statement`/`u.basis`/`links` out of it; `v3_build_claim_rows` (`:2599-2611`) concatenates those rows into the ledger unmodified. `reports/round-20/**` is filed round bytes and may not be edited, so the correction has to be either (i) a renderer draft that overlays live values onto these rows, or (ii) a round-34-local claims-map at a new path that the renderer (or D05's assembler) is pointed at. **Drafting an r7 packet without one of these two routes is not durable: the next `--freeze` re-emits the stale rows.**

Route B — `OQ-V3-05` is a hardcoded string literal in the renderer: `tools/exercise-handoff-e2e.py:3524-3533` (id at `:3524`; the "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts" text at `:3526-3529`). OQ-V3-04 and OQ-V3-06 sit in the same literal block (`:3510-3540`); the seven OQ-V2 rows are parsed from the filed `reports/round-15/handoff/packet-v2-05.yml`, so OQ-V2-03 (line 301) must NOT be rewritten — its figures are live (§4).

Both routes are shared-file changes: per the round's shared rules they are **drafted as before/after text** in the seat fragments and applied by the integrator; this seat touched neither.

## 6. The packet already contradicts itself in-file (free proof for the rewrite)

The live values are printed **inside the same packet bytes**, so the r7 rewrite is checkable against the file, not against external authority:

- `packet.md:68` A-30 — "d4 typed-label projection: 82 labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12 findings, 0 unresolved rank items, 4 era-alias rows" (live-mined, already correct).
- `packet.md:69` A-31 — "d4 committed hold set: 12 holds / 0 note / 0 fail" (live-mined, already correct).
- `packet.md:285` — "D4 read-only facts carried into this packet's D4 claim rows: … typed channel 82 labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12 findings (12 hold-or-fail), 0 unresolved rank items, 0 quarantine handles; hold set 12 holds / 0 note" (live-mined, already correct).
- `packet.md:148-152` — the D4 ledger rows quoting 74/56/16/15, hold 15 note 1, conflicts 4, quarantine 3 (stale).

So the claim's `before.self_contradiction` is confirmed and quantified: four live-mined surfaces agree with the live bytes, five parsed/hardcoded surfaces do not. Any r7 draft that sets rows 148/149/150/152/307 to the §4 values makes the file internally consistent — and the gate (`tools/gates/handoff-packet-check.py`) will still pass, because it checks shape (16/16 fields, 20 glossary entries, 0 findings), not figure currency (measured: gate verdict line in §1).

## 7. Coherence constraints for the integrator (measured, not assumed)

1. **The twin moves with the packet.** `v3_build_twin` (`tools/exercise-handoff-e2e.py:2621-2672`) places `open_questions` into `twin.json`, and both digests are frozen together in `expected.json` (`packet_sha256`, `twin_sha256`, `:4060-4061`). Editing the packet's OQ-V3-05 line without the renderer literal (route B) leaves packet/twin inconsistent and the links/uncertainty legs judging a different text than the gate sees.
2. **Unchanged-by-construction fields.** `v2_subset_digest` (`ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b`) covers only the 15 v2 rows, which are untouched by D03/D04's scope; status census 16/7/4 and claim count 27 are unaffected too (measured in §1). The `d4_legs` witnesses (`assemble-culture-d4.py --check`, `assemble-d4-typed.py --check`, two selftests 163/163 and 12/12) all pass on the current bytes.
3. **One freeze, then verify.** After the source drafts land: `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7` (refuses on any red) followed by `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` **only after** the two default lines `tools/exercise-handoff-e2e.py:1933-1934` move to `reports/round-34/handoff/declared-in-r7` — otherwise `--quiet` verifies the old pair and correctly reports the old sha.
4. **Expected.json is not byte-reproducible** (`/frozen_at` + `/baseline_digest`); the r7 `expected.json` will legitimately differ from r6's in exactly those two keys on an otherwise unchanged render — do not treat that as drift.
5. **`#stats` resolves but cannot be currency-checked** (see §4 row 5): row 148 cites `examples/culture-d4/typed-labels.d4.yml#stats`, which lives at `:2866-2869` as a nested key with live values `fail 0 / hold 12 / labels 82` — so the anchor resolves (consistent with links 105/105) and the only stale part is the quoted `labels 74`. The link leg validates *resolution*, not *currency*, so a row can carry a wrong figure with a valid anchor and stay green: flag to D08, the links owner, for the r7 receipt's honesty note.

## 8. Renderer wart observed (for D09 freeze design / D12 receipt)

`tools/exercise-handoff-e2e.py:4125` writes `freeze_lines.extend(diff or ["no tracked value changed since the previous freeze"])` — when the target dir holds **no previous** `expected.json`, `diff` is empty and `freeze.txt` claims "no tracked value changed since the previous freeze" although no previous freeze existed. My render's `freeze.txt` carries that line (521 B, last line). The r7 freeze into an empty `reports/round-34/handoff/declared-in-r7/` will reproduce the false provenance line unless the integrator pre-seeds `expected.json` or annotates it in the receipt. D12 owns the receipt wording; this is an FYI with evidence, not a claimed defect of claim D.

## Owed

- `reports/round-34/depth/D01-layout.md` — **owed by D01; absent at dispatch** (verified: `find reports/round-34 -type f` lists only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json` at 03:57). I substituted the renderer's own `--freeze` as the build path (§1). If D01's sketch names a different builder (e.g. a round-34-local script, or a new claims-map path per §5 route A(ii)), the integrator must reconcile my command/file-set with it; the layout file set I observed written is exactly `packet.md, twin.json, expected.json, freeze.txt, run.log` (`ls -la .scratch/d02/rendered/`), matching declared-in-r6's shape.
- Replacement row text — owed by D03 (ledger rows) and D04 (OQ rows); this seat delivered only before-bytes + measured after-values.

## Citations

Paths (all relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, at baseline commit da68a6d):

- `reports/round-34/targets.json` (seat D02 mission; shared_rules)
- `reports/round-34/claims.json` (claim D before/after_required, counting_commands)
- `REGIMEN.md` (round contract; F-C13-1 boundary)
- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP`), `:1933-1934` (v3 defaults), `:2161-2185` (`v3_mine_d4_labels`), `:2186-2203` (`v3_mine_d4_holds`), `:2289-2321` (`v3_parse_claims_map`), `:2476-2598` (`v3_manifest_rows`), `:2599-2617` (`v3_build_claim_rows`), `:2621-2672` (`v3_build_twin`), `:3477-3560` (`V3Assembly.__init__`, incl. hardcoded OQ-V3-04/05/06 at `:3510-3540`), `:3806-3977` (`v3_exercise`), `:3978-4128` (`v3_freeze`, freeze.txt at `:4125`), `:4475-4492` (`main`, `--freeze` wiring)
- `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json,freeze.txt,run.log}` (filed r6 pair; lines 68-69, 123, 144-155, 148-152, 262-269, 283-285, 297-308)
- `reports/round-20/handoff/claims-map.md` (filed D4 row prose — read-only route A source)
- `reports/round-15/handoff/packet-v2-05.yml` (filed v2 rows/OQ source)
- `examples/culture-d4/typed-labels.d4.yml` (`#coverage`, `#labels_by_kind`, `#rank_rules`, `#era_material_reconciliation`, `#era_reconciliation.alias_rows`), `examples/culture-d4/expected-holds.json` (`#counts`, `#holds`, `#notes`), `examples/culture-d4/packet.d4.typed.yml` (`#pipeline_counts`), `examples/culture-d4/packet.d4.yml` (`#form_slots`)
- `examples/culture-d2/typed-labels.d2.yml#coverage` (D2 live figures)
- `tools/gates/handoff-packet-check.py` (shape judge; 16/16 + 20 + 0)

Commands (run by this seat, 2026-10-19, TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1):

- `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d02/rendered` → exit 0; stdout quoted §1
- `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → `exit=0 … packet_sha256=6ced88ad009f…`
- `sha256sum` / `cmp` over the rendered vs filed five-file set (§2 table)
- `python3` drift probe over `expected.json.inputs` → `read set 58 drift 0 []`
- `grep -n '^## ' reports/round-30/handoff/declared-in-r6/packet.md` → section line numbers §3
- `sed -n '148p;149p;150p;152p;307p' .scratch/d02/rendered/packet.md` → the five row bytes quoted §3
- token sweep over the filed packet for stale figures (§4/§3: hits only at 148, 149, 150, 152, 307 plus D2-live lines 49, 129-130, 266-267, 284, 301)
- per-row `sha256`/byte-length probe (§3 table)
- `ls -la .scratch/d02/rendered/` → five files, sizes 105584/103625/10856/521/1603

Scratch (non-durable, `.scratch/d02/rendered/`, `.scratch/d02/freeze.stdout`): reproduced by the §1 command; no durable evidence depends on it.
