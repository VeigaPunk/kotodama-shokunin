- Seat: D05 | executor | claim D | date 2026-10-19 | baseline da68a6d

# D05 — `declared-in-r7/packet.md` DRAFT (D02+D03+D04 merged) + section manifest

## 0. Dependency status

At run time `reports/round-34/` held only `claims.json`, `targets.json` and `telemetry/dispatch-declared.json`
(measured: `find reports/round-34 -type f`). D01/D02/D03/D04 fragments were therefore absent, so this seat
performed their work itself per the missing-dependency rule: the layout/render decision (§1), the ledger-row
rewrite (§2–§3), the OQ rewrite (§3 L307) and the merge (§3) are all in this fragment. Owed paths: §9.

## 1. What the draft is — and why it is expressed as base ∪ delta

**Base (filed, immutable).** `reports/round-30/handoff/declared-in-r6/packet.md`, sha256
`6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`, 105584 bytes, 335 lines.

**The renderer reproduces those bytes exactly at HEAD `da68a6d`.** Command:
`python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0,
`packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` — byte-identical to the
filed r6 packet. So the new revision is *exactly* "renderer output + the corrected rows", not a rewrite.

**Draft.** The same renderer, with the §4 overlay landed, emits a packet of
`107109` bytes, sha256 `c0e5b4d5a611b70c611a644446c9b37628fb27c29c662a7605040c997696fcbd`, 335 lines — the base with exactly
10 replaced lines (L95, L113, L125, L148, L149, L150, L152, L288, L295, L307).

**Why base ∪ delta rather than 105 KB of inline prose:** the other ~104 KB is the filed r6 text, unchanged
byte-for-byte. Retyping it by hand is a transcription risk with no epistemic gain; the fenced replacement
lines in §3 plus the digest above make the reconstruction byte-verifiable (reconstruct, then `sha256sum` must
equal `c0e5b4d5a611b70c611a644446c9b37628fb27c29c662a7605040c997696fcbd`). The frozen artifact set itself was produced and measured in an isolated `git archive`
copy (§5) — this seat never wrote outside its `out` path.

**Closed-loop control (the draft is the renderer's own output).** The four corrected rows were parsed back
into row dicts and fed through the renderer's own `v3_build_packet` (`tools/exercise-handoff-e2e.py:2674`);
the rebuilt text was compared byte-for-byte with the base-plus-replacements control:
`rows+bullets patched: 6` / `patched == rendered: True` (first pass, 106,667 bytes, sha256 `10ac9766…`>).
The final freeze (§5) adds the §4 prose cells and the self-referencing baseline path, giving the digest above.

## 2. Line-delta census (base = r6 packet, 1-based lines)

| line | change | live source |
|---|---|---|
| 95 | A-57 manifest row role cell: the claims-map row no longer says the packet carries the twelve D4 rows "verbatim" | `reports/round-20/handoff/claims-map.md` (filed; 8 of 12 rows still come from it) + this fragment §4 |
| 113 | dependency_manifest `reports/round-20/handoff/claims-map.md` line: same correction | same as L95 |
| 125 | claim_ledger intro: names the live re-composition of the four prose rows instead of "carried from claims-map" | this fragment §4 + `reports/round-33/adj/A02-handoff.md:92-136` |
| 148 | D4-CL05 row rewritten: typed_labels 82 (was 74), native-form 64 (was 56), findings_total 12 / hold_or_fail 12 / label holds 12 / label fails 0 / conflicts 0 (was 16/15/12/0/…) | `examples/culture-d4/typed-labels.d4.yml:29-47` (`:46` typed_labels 82, `:37` native-form 64, `:32` findings_total 12, `:30` conflicts 0), `:2865-2869` stats (hold 12, labels 82) |
| 149 | D4-CL06 row rewritten: hold 12 / note 0 / fail 0 (was hold 15 / note 1), twelve D2L-FORM-UNRESOLVED rows and zero D2L-RANK rows, live `revision_note` cited | `examples/culture-d4/expected-holds.json:46-51` (counts hold 12/note 0/fail 0; the twelve rows are D2L-FORM-UNRESOLVED), `:32` revision_note (round-28 law-replay, "UNCHANGED at 12 holds / 0 notes / 0 fails"), `:27` round-30 generation note, `examples/culture-d4/components/01-brief.yml:66` (six unresolved garment form slots) |
| 150 | D4-CL07 row rewritten: conflicts 0 and quarantine 0 (was conflicts 4 / quarantine 3), six reconciliation records | `examples/culture-d4/typed-labels.d4.yml:45` reconciliation_records 6, `:30` conflicts 0, `:40` rank_quarantine_handles 0 |
| 152 | D4-CL09 row rewritten: rank panel live (component/normalized/gate-projected 4/4/4, act rules 0, residuals 0, unresolved 0, quarantine 0, conflicts 0, one declared skip); its `open:` leg now cites D2's own live residuals | `examples/culture-d4/typed-labels.d4.yml:306-309` rank_rules coverage 4/4/4, `:303` act_rules [], `:604` residuals [], `:168`/:605 skipped (one declared skip); D2 live residuals `examples/culture-d2/typed-labels.d2.yml` coverage (unresolved 13 / quarantine 3 / conflicts 4) |
| 288 | §validation links bullet: 106 links over 27 rows (was 105) — the corrected D4-CL06 row adds `expected-holds.json#revision_note` | `tools/harness/packet_links.py --packet <twin> --json` → links_checked 106, resolved 106 |
| 295 | §validation gate bullet: baseline path re-pointed to the new revision (renderer default move, D10) | this fragment §4 (defaults at `tools/exercise-handoff-e2e.py:1933-1934`) |
| 307 | OQ-V3-05 rewritten to the live state: twelve form holds, zero rank holds, zero notes, zero fails; the 13/3/4 residuals stay D2-owned | `examples/culture-d4/expected-holds.json:46-51`; `examples/culture-d2/typed-labels.d2.yml` coverage (13/3/4); `reports/round-20/handoff/claims-map.md:251` (the stale predecessor); `reports/round-25/v3-supersession/declared-in-r4/packet.md:310` (the round-25 correction this follows) |

Nothing else differs: the census was computed by full-line comparison of the two files (336 split entries
each, same line count); the A-28/A-29/A-30/A-31 manifest rows that differ between *r4* and *r6* are already
live in r6 (`:66-69`) and stay as they are.

## 3. The 10 replacement lines (verbatim, for byte-exact reconstruction)

Replace these lines of the base by line number; nothing else changes.

### L95

````
| A-57 | reports/round-20/handoff/claims-map.md | the twelve D4 claim rows as filed; the four prose rows (D4-CL05/06/07/09) are re-composed from the live artifacts in this build | 4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8 | 24,888 bytes |
````

### L113

````
- reports/round-20/handoff/claims-map.md @sha256:4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8 (the twelve D4 claim rows as filed, with the four prose rows re-composed live into the ledger)
````

### L125

````
Claim kinds are the contract §6 kinds. The 15 v2 rows are carried verbatim from reports/round-15/handoff/packet-v2-05.yml (subset-equality control: their normalized digest is `ad35c860acf3b452…`); the twelve D4 rows come from reports/round-20/handoff/claims-map.md; its four prose rows (D4-CL05, D4-CL06, D4-CL07, D4-CL09) are re-composed from the live artifacts in this run (F-A02-H1 — the filed prose measured a pre-family-clean generation), the remaining eight are carried as filed. Every row carries the round-15 uncertainty dimension as `uncertainty_status` + `uncertainty_basis` in the clause grammar (`grounding:` always; `restriction:` on partial rows; `open:` + `owner:` on unresolved rows) and a `links` cell of machine-checkable `path#token` specs; the delivered tables are parsed back into a machine twin and judged by tools/harness/packet_uncertainty.py and tools/harness/packet_links.py (read-only here). The D2 rows are labelled a derived projection (author-side) so they cannot be read as world claims. Statements are read from the live records and the filed rows, not paraphrased from documentation.
````

### L148

````
| D4-CL05 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#coverage (typed_labels 82, labels_by_kind native-form 64 / translated-label 12 / borrowed-strata 6, findings_total 12, findings_hold_or_fail 12, label_findings_hold 12, label_findings_fail 0, conflicts 0) and examples/culture-d4/typed-labels.d4.yml#typed_labels (stats fail 0, hold 12, labels 82), re-read from the delivered bytes; the projection is the projector's own output and the check leg reports byte-identical determinism | examples/culture-d4/typed-labels.d4.yml#coverage; examples/culture-d4/typed-labels.d4.yml#labels_by_kind; examples/culture-d4/typed-labels.d4.yml#stats; examples/culture-d4/typed-labels.d4.yml#typed_labels; tools/gates/d4-typed-labels-check-gate.py | The D4 typed channel types 82 labels — 64 native-form, 12 translated-label, 6 borrowed-strata — and carries 12 findings, all of them the twelve owed garment/slot form holds (12 label holds, 0 label fails, 0 conflicts); the committed projection is the projector's own deterministic output, and its check leg reports byte-identity rather than a re-derivation. |
````

### L149

````
| D4-CL06 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/expected-holds.json#counts (hold 12, note 0, fail 0) with the row list, whose twelve holds are all D2L-FORM-UNRESOLVED rows keyed to each garment twice (record id and slot id) and whose D2L-RANK population is zero; the emitted set equals the committed file, and the round-18 +9 hold / +1 note delta stands as that historical generation's reconciliation (reports/round-18/d4/holds.md), and the live examples/culture-d4/expected-holds.json#revision_note (the round-28 law-replay note, re-read this run) states the hold set is UNCHANGED at 12 holds / 0 notes / 0 fails, with the active pin generation round-30-qreg-records repeating the unchanged set | examples/culture-d4/expected-holds.json#counts; examples/culture-d4/expected-holds.json#holds; examples/culture-d4/expected-holds.json#revision_note; examples/culture-d4/components/01-brief.yml#hold_set_declaration; reports/round-18/d4/holds.md | The committed D4 hold set is 12 holds, 0 notes and 0 fails, pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to each garment twice (record id and slot id), and zero `D2L-RANK` rows of either severity; the emitted set equals the committed file, the round-17 brief's six unresolved garment form slots are met by those twelve keyed holds (+6 holds / 0 notes against the declaration), and the round-18 +9 hold / +1 note delta remains that historical generation's reconciliation (reports/round-18/d4/holds.md) rather than a present D4 expectation; the live examples/culture-d4/expected-holds.json#revision_note records the round-28 law-replay build with the hold set UNCHANGED at 12 holds / 0 notes / 0 fails, and the active generation round-30-qreg-records repeats the unchanged set. |
````

### L150

````
| D4-CL07 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation, six records GAR-01..GAR-06 each carrying an era block tagged E0 or E1 and a material block resolved by slot identity to a CMAT record, summary claims 6 findings 0; the same file's examples/culture-d4/typed-labels.d4.yml#reconciliation_records, examples/culture-d4/typed-labels.d4.yml#conflicts and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles counts carry six reconciliation records with zero conflicts and zero quarantine handles | examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation; examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED; examples/culture-d4/typed-labels.d4.yml#reconciliation_records; examples/culture-d4/typed-labels.d4.yml#conflicts; examples/culture-d4/packet.d4.yml#materials | The D4 projection's era and material reconciliation resolves all six garment records by declared row and slot identity — each record's era block tagged in scope, each material block resolved to a `CMAT` record — with zero findings, and its own ledger carries six reconciliation records with zero conflicts and zero quarantine handles rather than a residual pool folded into a cleaner ledger. |
````

### L152

````
| D4-CL09 | designer interpretation | derived projection (author-side), holds open | unresolved | grounding: examples/culture-d4/typed-labels.d4.yml#rank_rules, whose coverage block carries four packet-native RK rules preserved once each in the normalized and gate-projected views (rank_rules_component 4, rank_rules_normalized 4, rank_rules_gate_projected 4), with zero act rules, zero residuals, zero unresolved rank items, zero quarantine handles and zero conflicts, plus one declared skip of the D2 prose-rank adapter and residual tables; open: the thirteen unresolved rank items, three quarantine handles and four conflicts the pre-family-clean generation inherited are no longer D4-owned and were not resolved in D2, where they stay open (OQ-V2-03); owner: kotodama, blocking for the affected D2 rank records, not for this envelope | examples/culture-d4/typed-labels.d4.yml#rank_rules; examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items; examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles; examples/culture-d4/typed-labels.d4.yml#conflicts | The D4 rank view is packet-native and carries zero unresolved rank items, zero quarantine handles and zero conflicts: four RK rules are preserved once each in the normalized and gate-projected views, the D2 prose-rank adapter and residual tables are declared skipped rather than evaluated, and the thirteen unresolved rank items, three quarantine handles and four conflicts the pre-family-clean generation inherited stay open in D2 (OQ-V2-03) instead of being re-carried or promoted here. |
````

### L288

````
- claim-to-record links: 106 links over 27 rows; `tools/harness/packet_links.py` resolves all of them against the live bytes with zero findings in this run
````

### L295

````
- gate: `python3 tools/gates/handoff-packet-check.py packet.md` over the isolated copy, run from a directory outside the repository; declared expectation, checked after the run — exit 0, fields=16/16, glossary-entries=20, findings=0; the observed values are compared against the frozen baseline in `reports/round-34/handoff/declared-in-r7/expected.json`, whose run log records the verdict of the run it froze
````

### L307

````
- OQ-V3-05: D4's own holds stay open: twelve form holds, zero rank holds, zero notes and zero fails; the thirteen unresolved rank items, three quarantine handles and four conflicts recorded by the pre-family-clean generation are D2-owned residuals, removed from D4 ownership by the round-22 family-clean repair and still open in D2 (OQ-V2-03) — kotodama; blocking for the six owed D4 garment terms and the affected D2 rank records, not for this envelope (unresolved claims: D4-CL09)
````

## 4. The renderer change this draft requires (DRAFTED — a seat never edits shared files)

The frozen revision is only re-derivable with this overlay landed: the D4 ledger rows are parsed verbatim
from the **filed** `reports/round-20/handoff/claims-map.md` (`tools/exercise-handoff-e2e.py:2289-2321`, rows at
`:97-102,:107-118,:119-129,:150-160`) and `OQ-V3-05` was a hard-coded literal (`:3523-3531`), so neither could
self-correct. The overlay (i) extends the two miners with the live counts the prose needs, (ii) adds
`v3_live_d4_prose`, which re-composes D4-CL05/06/07/09 and the OQ-V3-05 passenger from live bytes and
**fails closed** (`E2E-DRC`) if the structural premises the prose rests on no longer hold, (iii) corrects the
three cells that asserted "carried verbatim", and (iv) moves the two defaults. Guards kept: label kinds sum
to `typed_labels`; findings_total = hold_or_fail = label holds = holds; zero label fails/conflicts/quarantine/
unresolved/rank holds/notes/fails; every hold row is `D2L-FORM-UNRESOLVED`; the rank panel keeps exactly one
declared skip with zero act rows and zero residuals; era rows are one per garment record; the hold set exceeds
the brief's six declared form slots.

Unified diff against the in-tree bytes (`tools/exercise-handoff-e2e.py`, 237,319 bytes at da68a6d); the
integrator applies this and then freezes. Edit sites: `:2161`/`:2186` miners, new function before `:2322`,
call site after `:3515`, OQ literal `:3523-3531`, prose cells `:2566`, `:2881`, `:2934`, defaults `:1933-1934`.

````diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -1930,8 +1930,8 @@
 V3_PROFILE = "kotodama-handoff-e2e/3"
 V3_PACKET_ID = "kotodama.handoff.d2d3d4-e2e"
 V3_PACKET_VERSION = "3.1.1"
-V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"
-V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"
+V3_BASELINE_DEFAULT = "reports/round-34/handoff/declared-in-r7/expected.json"
+V3_FROZEN_DIR_DEFAULT = "reports/round-34/handoff/declared-in-r7"
 V3_READ_SET = (
     *V1_READ_SET,
     V2_PACKET_MD,
@@ -2180,6 +2180,16 @@
         "verdicts": len(era.get("verdicts", [])),
         "packet_sha256": assembly.get("packet_sha256"),
         "reader_sha256": assembly.get("reader_sha256"),
+        "label_hold": coverage.get("label_findings_hold"),
+        "label_fail": coverage.get("label_findings_fail"),
+        "rank_component": (obj["rank_rules"].get("coverage") or {}).get("component_rules"),
+        "rank_normalized": (obj["rank_rules"].get("coverage") or {}).get("normalized"),
+        "rank_gate_projected": (obj["rank_rules"].get("coverage") or {}).get("gate_projected"),
+        "rank_act_rules": len(obj["rank_rules"].get("act_rules") or []),
+        "rank_residuals": len(obj["rank_rules"].get("residuals") or []),
+        "rank_skips": len(obj["rank_rules"].get("skipped") or []),
+        "era_records": len((obj.get("era_material_reconciliation") or {}).get("records") or []),
+        "era_findings": len((obj.get("era_material_reconciliation") or {}).get("findings") or []),
     }
 
 
@@ -2194,6 +2204,8 @@
         "note": counts.get("note"),
         "fail": counts.get("fail"),
         "rows": len(obj["holds"]) if isinstance(obj["holds"], list) else None,
+        "rank_rows": sum(1 for row in obj["holds"] if str(row.get("id", "")).startswith("D2L-RANK")),
+        "row_ids": sorted({str(row.get("id")) for row in obj["holds"]}),
         "notes": len(obj.get("notes", [])) if isinstance(obj.get("notes"), list) else None,
         "packet_sha256": obj["packet_sha256"],
         "projection_sha256": obj["projection_sha256"],
@@ -2317,6 +2329,113 @@
             }
         )
     return rows
+
+
+V3_D4_WORD_KEYS = ("hold", "note", "fail", "rank_hold", "reconciliations", "conflicts", "quarantine",
+                   "era_records", "rank_component", "rank_act", "rank_residual", "unresolved", "rank_skips",
+                   "d2_unresolved", "d2_quarantine", "d2_conflicts")
+
+NUM_WORDS = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
+             "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty")
+
+V3_D4_PROSE_TEMPLATES = {'D4-CL05': {'basis': "grounding: examples/culture-d4/typed-labels.d4.yml#coverage (typed_labels «labels», labels_by_kind native-form «native» / translated-label «translated» / borrowed-strata «borrowed», findings_total «findings_total», findings_hold_or_fail «hold_or_fail», label_findings_hold «label_hold», label_findings_fail «label_fail», conflicts «conflicts») and examples/culture-d4/typed-labels.d4.yml#typed_labels (stats fail «fail», hold «hold», labels «labels»), re-read from the delivered bytes; the projection is the projector's own output and the check leg reports byte-identical determinism", 'statement': "The D4 typed channel types «labels» labels — «native» native-form, «translated» translated-label, «borrowed» borrowed-strata — and carries «findings_total» findings, all of them the «hold_words» owed garment/slot form holds («label_hold» label holds, «label_fail» label fails, «conflicts» conflicts); the committed projection is the projector's own deterministic output, and its check leg reports byte-identity rather than a re-derivation.", 'links': 'examples/culture-d4/typed-labels.d4.yml#coverage; examples/culture-d4/typed-labels.d4.yml#labels_by_kind; examples/culture-d4/typed-labels.d4.yml#stats; examples/culture-d4/typed-labels.d4.yml#typed_labels; tools/gates/d4-typed-labels-check-gate.py', 'status': 'supported', 'kind': 'designer interpretation', 'evidence_status': 'derived projection (author-side)', 'placeholders': ['«borrowed»', '«conflicts»', '«fail»', '«findings_total»', '«hold_or_fail»', '«hold_words»', '«hold»', '«label_fail»', '«label_hold»', '«labels»', '«native»', '«translated»']}, 'D4-CL06': {'basis': "grounding: examples/culture-d4/expected-holds.json#counts (hold «hold», note «note», fail «fail») with the row list, whose «hold_words» holds are all D2L-FORM-UNRESOLVED rows keyed to each garment twice (record id and slot id) and whose D2L-RANK population is «rank_hold_words»; the emitted set equals the committed file, and the round-18 +«hist_hold_delta» hold / +«hist_note_delta» note delta stands as that historical generation's reconciliation (reports/round-18/d4/holds.md), and the live examples/culture-d4/expected-holds.json#revision_note (the round-28 law-replay note, re-read this run) states the hold set is UNCHANGED at «hold» holds / «note» notes / «fail» fails, with the active pin generation round-30-qreg-records repeating the unchanged set", 'statement': "The committed D4 hold set is «hold» holds, «note» notes and «fail» fails, pinned to the delivered bytes: «hold_words» `D2L-FORM-UNRESOLVED` holds keyed to each garment twice (record id and slot id), and «rank_hold_words» `D2L-RANK` rows of either severity; the emitted set equals the committed file, the round-17 brief's six unresolved garment form slots are met by those «hold_words» keyed holds (+«decl_hold_delta» holds / «note» notes against the declaration), and the round-18 +«hist_hold_delta» hold / +«hist_note_delta» note delta remains that historical generation's reconciliation (reports/round-18/d4/holds.md) rather than a present D4 expectation; the live examples/culture-d4/expected-holds.json#revision_note records the round-28 law-replay build with the hold set UNCHANGED at «hold» holds / «note» notes / «fail» fails, and the active generation round-30-qreg-records repeats the unchanged set.", 'links': 'examples/culture-d4/expected-holds.json#counts; examples/culture-d4/expected-holds.json#holds; examples/culture-d4/expected-holds.json#revision_note; examples/culture-d4/components/01-brief.yml#hold_set_declaration; reports/round-18/d4/holds.md', 'status': 'supported', 'kind': 'designer interpretation', 'evidence_status': 'derived projection (author-side)', 'placeholders': ['«decl_hold_delta»', '«fail»', '«hist_hold_delta»', '«hist_note_delta»', '«hold_words»', '«hold»', '«note»', '«rank_hold_words»']}, 'D4-CL07': {'basis': "grounding: examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation, six records GAR-01..GAR-06 each carrying an era block tagged E0 or E1 and a material block resolved by slot identity to a CMAT record, summary claims «era_records» findings «era_findings»; the same file's examples/culture-d4/typed-labels.d4.yml#reconciliation_records, examples/culture-d4/typed-labels.d4.yml#conflicts and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles counts carry «reconciliations_words» reconciliation records with «conflicts_words» conflicts and «quarantine_words» quarantine handles", 'statement': "The D4 projection's era and material reconciliation resolves all «era_records_words» garment records by declared row and slot identity — each record's era block tagged in scope, each material block resolved to a `CMAT` record — with zero findings, and its own ledger carries «reconciliations_words» reconciliation records with «conflicts_words» conflicts and «quarantine_words» quarantine handles rather than a residual pool folded into a cleaner ledger.", 'links': 'examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation; examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED; examples/culture-d4/typed-labels.d4.yml#reconciliation_records; examples/culture-d4/typed-labels.d4.yml#conflicts; examples/culture-d4/packet.d4.yml#materials', 'status': 'supported', 'kind': 'designer interpretation', 'evidence_status': 'derived projection (author-side)', 'placeholders': ['«conflicts_words»', '«era_findings»', '«era_records_words»', '«era_records»', '«quarantine_words»', '«reconciliations_words»']}, 'D4-CL09': {'basis': 'grounding: examples/culture-d4/typed-labels.d4.yml#rank_rules, whose coverage block carries «rank_component_words» packet-native RK rules preserved once each in the normalized and gate-projected views (rank_rules_component «rank_component», rank_rules_normalized «rank_normalized», rank_rules_gate_projected «rank_gate_projected»), with «rank_act_words» act rules, «rank_residual_words» residuals, «unresolved_words» unresolved rank items, «quarantine_words» quarantine handles and «conflicts_words» conflicts, plus «rank_skips_words» declared skip of the D2 prose-rank adapter and residual tables; open: the «d2_unresolved_words» unresolved rank items, «d2_quarantine_words» quarantine handles and «d2_conflicts_words» conflicts the pre-family-clean generation inherited are no longer D4-owned and were not resolved in D2, where they stay open (OQ-V2-03); owner: kotodama, blocking for the affected D2 rank records, not for this envelope', 'statement': 'The D4 rank view is packet-native and carries «unresolved_words» unresolved rank items, «quarantine_words» quarantine handles and «conflicts_words» conflicts: «rank_component_words» RK rules are preserved once each in the normalized and gate-projected views, the D2 prose-rank adapter and residual tables are declared skipped rather than evaluated, and the «d2_unresolved_words» unresolved rank items, «d2_quarantine_words» quarantine handles and «d2_conflicts_words» conflicts the pre-family-clean generation inherited stay open in D2 (OQ-V2-03) instead of being re-carried or promoted here.', 'links': 'examples/culture-d4/typed-labels.d4.yml#rank_rules; examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items; examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles; examples/culture-d4/typed-labels.d4.yml#conflicts', 'status': 'unresolved', 'kind': 'designer interpretation', 'evidence_status': 'derived projection (author-side), holds open', 'placeholders': ['«conflicts_words»', '«quarantine_words»', '«rank_act_words»', '«rank_component_words»', '«rank_component»', '«rank_gate_projected»', '«rank_normalized»', '«rank_residual_words»', '«rank_skips_words»', '«unresolved_words»']}}
+V3_OQ_V3_05_TEMPLATE = "D4's own holds stay open: «hold_words» form holds, «rank_hold_words» rank holds, «note_words» notes and «fail_words» fails; the «d2_unresolved_words» unresolved rank items, «d2_quarantine_words» quarantine handles and «d2_conflicts_words» conflicts recorded by the pre-family-clean generation are D2-owned residuals, removed from D4 ownership by the round-22 family-clean repair and still open in D2 (OQ-V2-03) — kotodama; blocking for the six owed D4 garment terms and the affected D2 rank records, not for this envelope"
+
+
+def v3_live_d4_prose(d4_rows, d4_labels, d4_holds, d4, typed):
+    '''Re-compose the four D4 prose rows and the OQ-V3-05 passenger from the live artifacts.
+
+    F-A02-H1: the rows parsed from the filed claims-map measured a pre-family-clean
+    generation (and the label counts moved again when the register records landed), so
+    the numbers here are read from the live bytes and the structural premises the prose
+    rests on are asserted first - a stale or reshaped live state raises rather than
+    emitting prose that no longer describes it.
+    '''
+    kinds = d4_labels["by_kind"]
+    live = {
+        "labels": d4_labels["labels"],
+        "native": kinds.get("native-form"),
+        "translated": kinds.get("translated-label"),
+        "borrowed": kinds.get("borrowed-strata"),
+        "findings_total": d4_labels["findings_total"],
+        "hold_or_fail": d4_labels["hold_or_fail"],
+        "label_hold": d4_labels["label_hold"],
+        "label_fail": d4_labels["label_fail"],
+        "conflicts": d4_labels["conflicts"],
+        "quarantine": d4_labels["quarantine"],
+        "reconciliations": d4_labels["reconciliations"],
+        "unresolved": d4_labels["unresolved_items"],
+        "era_records": d4_labels["era_records"],
+        "era_findings": d4_labels["era_findings"],
+        "rank_component": d4_labels["rank_component"],
+        "rank_normalized": d4_labels["rank_normalized"],
+        "rank_gate_projected": d4_labels["rank_gate_projected"],
+        "rank_act": d4_labels["rank_act_rules"],
+        "rank_residual": d4_labels["rank_residuals"],
+        "rank_skips": d4_labels["rank_skips"],
+        "hold": d4_holds["hold"],
+        "note": d4_holds["note"],
+        "fail": d4_holds["fail"],
+        "rank_hold": d4_holds["rank_rows"],
+        "hist_hold_delta": 9,
+        "hist_note_delta": 1,
+        "decl_hold_delta": (d4_holds["hold"] or 0) - 6,
+        "d2_unresolved": typed["unresolved_items"],
+        "d2_quarantine": typed["quarantine"],
+        "d2_conflicts": typed["conflicts"],
+    }
+    problems = []
+    if live["labels"] != sum(live[key] or 0 for key in ("native", "translated", "borrowed")):
+        problems.append("the label kinds no longer sum to typed_labels")
+    if len({live["findings_total"], live["hold_or_fail"], live["label_hold"], live["hold"]}) != 1:
+        problems.append("findings_total / findings_hold_or_fail / label holds / holds no longer coincide")
+    if any(live[key] for key in ("label_fail", "conflicts", "quarantine", "unresolved", "rank_hold", "note", "fail")):
+        problems.append("a non-zero D4 hold/fail/residual count reappeared")
+    if set(d4_holds["row_ids"]) != {"D2L-FORM-UNRESOLVED"}:
+        problems.append("the hold rows are no longer all D2L-FORM-UNRESOLVED")
+    if any(live[key] for key in ("rank_act", "rank_residual", "era_findings")) or live["rank_skips"] != 1:
+        problems.append("the rank/era panel shape moved (act rows, residuals, findings or the declared skip)")
+    if not (live["era_records"] == live["reconciliations"] == d4["counts"]["costumes"]):
+        problems.append("the era/material rows are no longer one per garment record")
+    if live["rank_component"] != live["rank_normalized"] or live["rank_component"] != live["rank_gate_projected"]:
+        problems.append("the rank rules are no longer preserved once each in the normalized/gate-projected views")
+    if live["decl_hold_delta"] <= 0:
+        problems.append("the hold set no longer exceeds the brief's six declared form slots")
+    values = {}
+    for key, value in live.items():
+        if not isinstance(value, int):
+            problems.append("count %s is not an integer: %r" % (key, value))
+            continue
+        values[key] = str(value)
+        if key in V3_D4_WORD_KEYS:
+            if 0 <= value < len(NUM_WORDS):
+                values[key + "_words"] = NUM_WORDS[value]
+            else:
+                problems.append("count %s is outside the word range: %r" % (key, value))
+    if problems:
+        raise Failed("E2E-DRC", "the live D4 bytes no longer match the D4 prose premises: " + "; ".join(problems))
+
+    def fill(text):
+        for key, value in values.items():
+            text = text.replace("\u00ab" + key + "\u00bb", value)
+        leftover = re.findall("\u00ab[a-z_]+\u00bb", text)
+        if leftover:
+            raise Failed("E2E-DRC", "unfilled D4 prose placeholder(s): " + ", ".join(sorted(set(leftover))))
+        return text
+
+    rows = []
+    for row in d4_rows:
+        template = V3_D4_PROSE_TEMPLATES.get(row["claim_id"])
+        if template is None:
+            rows.append(dict(row))
+            continue
+        rebuilt = dict(row)
+        rebuilt["basis"] = fill(template["basis"])
+        rebuilt["statement"] = fill(template["statement"])
+        rebuilt["links"] = list(template["links"].replace("; ", ";").split(";"))
+        rows.append(rebuilt)
+    return rows, fill(V3_OQ_V3_05_TEMPLATE)
+
 
 
 def v3_load_v2_edges(root):
@@ -2563,7 +2682,7 @@
         D4_READER: "d4 reader gate named by the packet's own assembly block",
         UNCERTAINTY_TOOL: "this run's uncertainty judge (round-15 harness validator, read-only here)",
         LINKS_TOOL: "this run's link judge (round-15 harness validator, read-only here)",
-        CLAIMS_MAP: "the twelve D4 claim rows as filed; this packet carries them verbatim",
+        CLAIMS_MAP: "the twelve D4 claim rows as filed; the four prose rows (D4-CL05/06/07/09) are re-composed from the live artifacts in this build",
     }
     for rel in SOURCE_LEDGERS:
         obj = json_file(root, rel)
@@ -2878,7 +2997,7 @@
         "grammar, and claim-to-record links plus coupling-edge records resolved against live bytes)"
     )
     add(
-        f"- {CLAIMS_MAP} @sha256:{digests[CLAIMS_MAP]} (the twelve D4 claim rows carried verbatim into the "
+        f"- {CLAIMS_MAP} @sha256:{digests[CLAIMS_MAP]} (the twelve D4 claim rows as filed, with the four prose rows re-composed live into the "
         "ledger)"
     )
     add(
@@ -2931,7 +3050,7 @@
     add(
         "Claim kinds are the contract §6 kinds. The 15 v2 rows are carried verbatim from "
         f"{V2_PACKET_YML} (subset-equality control: their normalized digest is "
-        f"`{v2_subset_digest[:16]}…`); the twelve D4 rows are carried from {CLAIMS_MAP}. Every row carries "
+        f"`{v2_subset_digest[:16]}…`); the twelve D4 rows come from {CLAIMS_MAP}; its four prose rows (D4-CL05, D4-CL06, D4-CL07, D4-CL09) are re-composed from the live artifacts in this run (F-A02-H1 — the filed prose measured a pre-family-clean generation), the remaining eight are carried as filed. Every row carries "
         "the round-15 uncertainty dimension as `uncertainty_status` + `uncertainty_basis` in the clause "
         "grammar (`grounding:` always; `restriction:` on partial rows; `open:` + `owner:` on unresolved rows) "
         "and a `links` cell of machine-checkable `path#token` specs; the delivered tables are parsed back into "
@@ -3509,6 +3628,9 @@
         if len(self.v2_rows) != 15:
             raise ArtifactError(f"{V2_PACKET_YML}: holds {len(self.v2_rows)} claim rows, expected 15")
         self.d4_rows = v3_parse_claims_map(root)
+        self.d4_rows, self.oq_v3_05 = v3_live_d4_prose(
+            self.d4_rows, self.d4_labels, self.d4_holds, self.d4, self.typed
+        )
         self.open_questions = list(self.v2_open_questions) + [
             {
                 "id": "OQ-V3-04",
@@ -3522,12 +3644,7 @@
             },
             {
                 "id": "OQ-V3-05",
-                "question": (
-                    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
-                    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
-                    "kotodama; blocking for the affected D2 rank records and the six garment terms, not for "
-                    "this envelope"
-                ),
+                "question": self.oq_v3_05,
                 "unresolved_claims": "D4-CL09",
             },
             {
````

## 5. Verification (isolated `git archive` copy at `.scratch/d05/iso`; no in-tree round runner executed)

| # | command (in the isolated copy) | observed |
|---|---|---|
| 1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7` | exit **0** — `frozen: 2026-10-19`; `packet_sha256 c0e5b4d5…`; `twin_sha256 a45977d1…`; `gate: exit 0, fields=16/16, glossary-entries=20, findings=0`; `semantics: uncertainty exit 0, links 106/106 resolved`; `claims: 27 statuses 16/7/4; v2-subset ad35c860acf3b452…; alias leg landed`; `read set: 58 files; component digests 26/26; d4 pins 8/8` |
| 2 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` (default chain → declared-in-r7) | exit **0** — `fields=16/16 glossary=20/20 findings=0 links=106/106 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=c0e5b4d5…` = `freeze.txt:2` |
| 3 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest --quiet` | exit **0** — positive run plus **39 controls** (all listed in the run output; includes the preservation control "the 58 read-set files are byte-identical before and after a run") |
| 4 | `python3 tools/gates/handoff-packet-check.py <draft packet>` (in-tree path, and again from a foreign cwd) | exit **0** — `INFO scan: fields=16/16 glossary-entries=20 findings=0` |
| 5 | `python3 -B tools/harness/packet_links.py --packet <draft twin> --repo-root . --json` | exit **0** — `links_checked 106, resolved 106, findings []` |
| 6 | `python3 -B tools/harness/packet_uncertainty.py --packet <draft twin> --require-oq --json` | exit **0** — `claims 27, findings []` |
| 7 | `sha256sum` over the frozen set | packet `c0e5b4d5…` (107,109 B), twin `a45977d1…` (104,847 B), expected.json `37514f8e…` (10,856 B), freeze.txt `fb574799…` (521 B), run.log `8bce6903…` (1,603 B) |
| 8 | baseline `inputs` equality r6 ↔ new | **identical, 58/58** — no read-set file changed for this revision |
| 9 | `git status --porcelain` in the repo | only `?? reports/round-34/` — filed bytes untouched; r6 packet `6ced88ad…`, r4 `5f58db4a…`, `claims-map.md` `4b1b9a35…` (= the packet's own A-57 pin) all re-measured unchanged |

**Stale-figure audit of the frozen draft** (patterns from `claims.json` claim D's before-block and
`reports/round-33/adj/A02-handoff.md:99-108`): `typed_labels 74`, `native-form 56`, `labels 74`,
`findings_hold_or_fail 15`, `hold 15`, `hold 15, note 1`, `three rank holds`, `one note`,
`twelve form holds + three rank holds + one note`, `rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`,
`quarantine handles (3)`, `conflicts (4)`, `carry four conflicts` → **0 hits each**. Live values present:
`typed_labels 82` ×1, `native-form 64` ×1, `labels 82` ×2, `hold 12, note 0, fail 0` ×1 (plus the worded form).
`zero rank holds` ×1, `106 links over 27 rows` ×1, `declared-in-r7/expected.json` ×1. Two survivors are
deliberate and live: `15 holds` ×1 in `RD-D2-01` (D2's own `findings_hold_or_fail` is 15 —
`examples/culture-d2/typed-labels.d2.yml` coverage), and the words "thirteen unresolved rank items, three
quarantine handles and four conflicts" ×3 — all three now explicitly *historical / D2-owned* (D4-CL09 `open:`,
its statement, OQ-V3-05), with D2's live 13/3/4 as the referent.

## 6. Negative controls

1. **The overlay is load-bearing.** With the *unpatched* renderer (staged from `HEAD`) and the new baseline:
   `--profile v3 --baseline reports/round-34/handoff/declared-in-r7/expected.json --quiet` → exit **1**,
   `packet_sha256=(not assembled)` (refused at the frozen-packet comparison, `tools/exercise-handoff-e2e.py:1490`).
   Restoring the patched renderer → exit 0 with `packet_sha256=c0e5b4d5…`. (First attempt at this control was
   invalid — the `git show` redirect resolved against the real repo and silently kept the patched file; re-run
   with an explicit `git show HEAD:… > .scratch/d05/iso/…`.)
2. **The old pair still gates green.** `handoff-packet-check.py` on the r6 packet → exit 0, 16/16, 20, 0
   (`reports/round-33/adj/A02-handoff.md:33`) while carrying the stale prose: shape-green ≠ current. This is the
   semantic-stale class my method catches and the shape gate cannot.
3. **A re-injected stale figure is caught.** Copy of the draft with `(hold 12, note 0, fail 0)` →
   `(hold 15, note 1, fail 0)`: the audit reports 1 hit for `hold 15` / `note 1` / `hold 15, note 1` (0 in the
   draft) while the gate still exits 0.
4. **Fail-closed guards fire.** The first overlay attempt refused to emit (`E2E-DRC the live D4 bytes no longer
   match the D4 prose premises: the era/material rows are no longer one per garment record; count labels out of
   the word range: 82`) — a stale/shape-shifted live state raises instead of producing prose that no longer
   describes it.

## 7. Section manifest — every delivered section and its live source

| section | live source |
|---|---|
| `packet_id`, `packet_version` (3.1.1) | renderer constants `tools/exercise-handoff-e2e.py:1931-1935`; no wall-clock content |
| `contract_ref` | `corpus/knowledge/synthesis/worldbible-integration-contract.md` digest `5f4c02bf…` re-measured this run = packet `:14` = `expected.json.cross_refs.contract_digest` |
| `producer`, `recipient`, `request_ref`, `baseline_bible_ref`, `canon_standing`, `handoff_status` | contract §4/§6/§8 (packet `:7-18`); `examples/culture-d3/packet.json` `prepared-not-accepted` / `NON-CANON` |
| `subject_refs` (12 namespaced candidates) | live D2/D3/D4 packets named in `:19` (`examples/culture-d2/packet.d2.yml`, `examples/culture-d3/packet.json` L01–L20, `examples/culture-d4/packet.d4.yml`) |
| `scope` + delivered record sets | live bytes of the three drills; D4 counts re-read this run (62 lexicon / 8 names / 8 symbols / 6 costumes / 4 rank rules / 8 era records / 2 contact layers / 9 provenance rows) |
| `artifact_manifest` (58 rows + inline glossary row) | every digest re-measured at assembly; this run: component digests 26/26 matched, d4 tree pins 8/8 matched |
| `dependency_manifest` | live files; the claims-map line corrected (§3 L113) because 4 of 12 rows are now live-composed |
| `claim_ledger` (27 rows) | 15 v2 rows verbatim from `reports/round-15/handoff/packet-v2-05.yml` (subset digest `ad35c860acf3b452…`); 8 D4 rows as filed in `reports/round-20/handoff/claims-map.md:54-192`; 4 D4 rows live-composed (§4) |
| `coupling_edges` (88 rows) | 34 v2 rows from `packet-v2-05.yml`; 54 `D4E-*` rows measured from `examples/culture-d4/packet.d4.yml` bytes at assembly |
| `requested_decisions` (14 rows) | filed rows; live counts re-checked: D2 58 labels / 15 hold-or-fail / 13 unresolved / 21 `to-verify` lines (`examples/culture-d2/typed-labels.d2.yml`, `packet.d2.yml`), D4 six form slots (`examples/culture-d4/packet.d4.yml#form_slots`) |
| `validation` | computed live this run: read set 58 files, component digests 26/26, d4 pins 8/8, links 106/106, statuses 16/7/4, gate exit 0 / 16/16 / 20 / 0 |
| `open_questions` (10 rows) | 7 v2 rows from the v2 twin; `OQ-V3-05` live-composed (§4); `OQ-V3-04`, `OQ-V3-06` unchanged |
| glossary payload (20 rows) | live D3 lexicon in source order, `examples/culture-d3/packet.json` |

## 8. What the draft asserts about itself (bear with the self-reference)

- `packet_version` stays 3.1.1 (a prose/value correction, not a version bump): the claim says the form moves
  with the revision name (`declared-in-r7`), as rounds 22/23/25/26/30 did.
- `:295` now names `reports/round-34/handoff/declared-in-r7/expected.json`, which is only true once the §4
  default move is landed; freeze before re-pointing the default would leave the packet naming r6 and the
  freeze unreproducible. Order: **apply §4 → freeze → run the default chain**.

## 9. Sibling-fragment reconciliation (they landed after my render; added 2026-10-19)

Sibling fragments appeared while this seat was working, so the five corrected rows now exist in **two
competing texts**. Measured comparison (line-by-line, `reports/round-34/depth/`):

- `D02-render.md` carries the **r6 bytes unchanged** (row lengths 1091/1150/1202/1370/308 B = the stale r6
  lines at `packet.md:148,149,150,152,307`) — it is the base render, not the correction.
- `D03-ledger-rows.md` carries its **own live-measured rewrites** (1088/1122/1226/1472/311 B). Its number
  census agrees with mine on every count I compared: typed_labels 82, native-form 64, translated 12,
  borrowed 6 (`examples/culture-d4/typed-labels.d4.yml:36-38,46`), findings_total 12 / hold_or_fail 12 / label
  holds 12 / label fails 0 (`:31-34`), conflicts 0 (`:30`), quarantine 0 (`:40`), unresolved 0 (`:44`),
  reconciliation_records 6 (`:45`), hold 12 / note 0 / fail 0 (`expected-holds.json:46-51`). That is useful
  independent agreement on the values; the **wording and link cells differ**, and three differences are
  substantive rather than cosmetic:
  1. D03's D4-CL06 basis attributes a `+6 hold / +0 note delta` to `reports/round-18/d4/holds.md`, whose filed
     text documents a `+9 hold / +1 note` delta (`packet.md:149` carried it); mine keeps +9/+1 as that
     generation's history and derives +6/+0 against the brief's six declared slots
     (`examples/culture-d4/components/01-brief.yml:66`). The round-18 receipt was not re-filed, so a reader can
     only verify +6/+0 against the declaration, not against that receipt.
  2. D03's link set stops at 4 links for D4-CL06 (no `expected-holds.json#revision_note`); mine has 5, which is
     why the census moves 105 → 106 (`packet.md:288`).
  3. D03's D4-CL09 adds `adapt_status executable` on the four gate-projected rules — verified true against the
     live bytes (`examples/culture-d4/typed-labels.d4.yml` rank_rules `gate_rank_rules[*].adapt_status`) and a
     fair detail; mine cites the component/normalized/gate-projected 4/4/4 triple and the declared skip.
- **Choosing a set is a freeze decision.** My set is the one that has been frozen, gated, link-resolved
  (106/106), uncertainty-judged and e2e-green with its digest pinned (`c0e5b4d5…`, §5). If the integrator
  prefers D03's text, the §4 templates must be replaced with D03's wording, the link census recomputed
  (105 → 105 for a 4-link D4-CL06), and the whole §5/§6 evidence re-run — the digest in §1 will **not** hold,
  and the packet must be re-frozen. Landing both texts is not possible: one row per claim id.

## Owed

- `reports/round-34/depth/D01-layout.md`, `D02-render.md`, `D03-ledger-rows.md`, `D04-oq-glossary.md` — absent at
  run time (only `claims.json`/`targets.json`/`telemetry/dispatch-declared.json` existed). Their content is
  folded into §1 (render), §2–§3 (ledger rows), §3 L307 (OQ): nothing is missing from the draft, but the named
  fragments do not exist as files.
- `reports/round-34/depth/D06-twin-expected.md` — the twin/expected.json/freeze.txt/run.log bytes and digests
  exist only in the isolated copy (`.scratch/d05/iso/reports/round-34/handoff/declared-in-r7/`, scratch, may be
  cleaned). The integrator re-creates them by freezing with the §4 patch; digests are pinned in §5 row 7 so a
  mismatch is detectable. `D06-twin-expected.md` remains to be written.
- `D07-gate-run.md`, `D08-links-uncertainty.md`, `D09-freeze-design.md`, `D10-repin-drafts.md` — folded into §5
  (gate/links/uncertainty/freeze), §6 (controls) and §4 (re-pin drafts) here.
- `to-verify`: whether the integrator also re-points `V3_FROZEN_DIR_DEFAULT` (used by the selftest fixture,
  `tools/exercise-handoff-e2e.py:4149,4172`, and the v3 CLI default chain `:4561`). Drafted as a new row in §4;
  the selftest ran green with it moved inside the isolated copy (39 controls), so the move is exercised, not
  merely proposed.
- `to-verify`: no second independent seat has yet audited these numbers against live bytes (claim D threshold
  asks for two independent seats). D18/D20 exist for exactly that and their fragments were absent.

## Citations

- `reports/round-30/handoff/declared-in-r6/packet.md:1,3,5,66-69,95,113,125,148,149,150,152,285,288,295,307`;
  `.../declared-in-r6/{expected.json,freeze.txt,run.log,twin.json}` (sha256 re-measured: packet `6ced88ad…`)
- `reports/round-30/handoff/declared-in-r6/expected.json` — `counts.d4_typed_labels 82`, `counts.d4_holds 12`,
  `inputs` 58 files (identical to the new revision's)
- `tools/exercise-handoff-e2e.py:1490,1931-1935,2161-2200,2186-2202,2289-2321,2566,2599,2674,2881,2934,3128-3160,3515,3523-3531,3806,3978-4040,4149,4172,4561`
- `tools/gates/handoff-packet-check.py`; `tools/harness/packet_links.py`; `tools/harness/packet_uncertainty.py`
- `examples/culture-d4/typed-labels.d4.yml:29-47,168,303,306-309,604-605,614,2865-2869`;
  `examples/culture-d4/expected-holds.json:6,27,32,46-51`; `examples/culture-d4/components/01-brief.yml:66`;
  `examples/culture-d2/typed-labels.d2.yml` coverage (58 / 46,10,2 / 16 / 15 / 13 / 3 / 4 / 10);
  `examples/culture-d2/packet.d2.yml` (21 `to-verify` lines); `examples/culture-d3/packet.json`;
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` (digest `5f4c02bf…`)
- `reports/round-20/handoff/claims-map.md:97-102,107-118,119-129,150-160,251` (the filed, stale row source)
- `reports/round-25/v3-supersession/declared-in-r4/packet.md:9,151-155,310` (the filed round-25 corrective rows,
  reused as the wording base with the label counts re-measured)
- `reports/round-33/adj/A02-handoff.md:92-136` (F-A02-H1: the named finding this draft closes), `:33-40` (the
  green re-runs of the stale pair)
- `corpus/lessons/round-25.md:82-85` (the hard-coded-literal diagnosis: two sources, partial staleness)
- this seat's commands, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all 2026-10-19:
  `sha256sum` over both packet revisions and the frozen set; `python3 -B tools/exercise-handoff-e2e.py --profile v3
  --quiet` (r6 reproduction), `--freeze`, `--quiet`, `--selftest --quiet`, `--baseline …/declared-in-r7/expected.json
  --quiet` (the red control), `python3 tools/gates/handoff-packet-check.py <draft>` (in-tree and foreign cwd),
  `python3 -B tools/harness/packet_links.py --packet <draft twin> --repo-root . --json`,
  `python3 -B tools/harness/packet_uncertainty.py --packet <draft twin> --require-oq --json`,
  a full-line diff of the two packets, `git status --porcelain`, `find reports/round-34 -type f`)
- `.scratch/d05/{build.py,verify.py,patch_iso.py,make_fragment.py,patched-e2e.py}` — the seat's own scratch tooling
  (scratch; not a deliverable)
