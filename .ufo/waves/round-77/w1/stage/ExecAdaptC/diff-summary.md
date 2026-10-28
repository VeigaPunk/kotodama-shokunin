# ACCEPT-C-77 — diff summary against `reports/round-76/accept-c.py`

Seat `ExecAdaptC` (round 77, wave 1). Adapted file:
`.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py`, realigned to the
**22:33 rewrite of `.ufo/waves/round-77/CLAIMS-DRAFT.md`**, which names the
13-leg lineage set (ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND,
CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX — one INDEX).
The earlier 15-name draft (STAMP/LEDGELIST/COUNTS/APPENDONLY/RECEIPTS) is no
longer the contract; those checks survive folded into the named legs (table below).

## Measured shape

| measurement | round 76 | round 77 | command |
|---|---:|---:|---|
| lines | 6627 | 3303 | `wc -l reports/round-76/accept-c.py …/accept-c.py` |
| functions (`ast`) | 177 | 110 | `python3` + `ast.parse` per file |
| shared function names | — | 67 | same AST pass (`set(a) & set(b)`) |
| new function names | — | 43 | same AST pass (`set(b) - set(a)`) |
| dropped r76 functions | — | 110 | same AST pass (`set(a) - set(b)`) |
| diff added / removed lines | — | 2420 / 5762 | `diff -u … \| grep -c '^+' / '^-'` (31 hunks) |
| counter sha256 | `9db9305d…` (r76 file) | `5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4` | `sha256sum` |
| py_compile | — | silent, exit 0 | `python3 -B -m py_compile accept-c.py` |
| selftest | 94/94 (r76 receipt) | 37/37 | `python3 -B accept-c.py --selftest` → `selftest-receipt.txt` |

## The 13 legs and where each r76/r77 check lives

| # | leg (draft order) | r76 counterpart | what the r77 leg grades |
|---|---|---|---|
| 1 | ENTRIES | ENTRIES | one admitted entry, absent at base; provenance header (source/verified-at/recheck/ground/topic) without placeholders; ≥1 `## ` section; body ≥ the smallest base entry (derived, 478 words on this base); citations of mined rows; knowledge tree `knowledge_before → +n` with the diff exactly the entries (absorbs r77-draft COUNTS' knowledge half) |
| 2 | ROWS | ROWS | ONLY `| S### |` ids added inside the frozen row_set (r76 defect 1); `rows_before → +k`; 11 cells / mined / opened / cadence / used-by exactly the citing entries / live URL + same-page capture / anchor quote; a pre-existing row may change only its rule-2 cells (status, recheck, used-by) — no removal, no reorder (absorbs APPENDONLY's registry half) |
| 3 | REPOINTED | REPOINTED | every `source:` line carries exactly one id whose row URL names that document; every inline S-id resolves to a frozen lane row or a base-held row; `removed_ids[]` (draft: S886/S888/S889/S890/S891/S896) must be gone; a campaign-namespace id is never cited as a lane row |
| 4 | GATE | GATE | `## Gate` access date; one admit row per row with URL, date, ≤25-token/≤80-char located quote and the evidence path |
| 5 | EVIDENCE | EVIDENCE | committed capture per row: fetch names the frozen document, UA recorded, HTTP 200, positive bytes, 64-hex digest, `claims-source` naming `<freeze>` + `claims-frozen: yes` (absorbs r77-draft STAMP's evidence half), window scope re-derived from bytes, Gate quote inside the window |
| 6 | REJECTS | REJECTS | ≥1 admit and ≥1 reject; frozen refused staged ids in the Gate reject table with reason+flip, never lane rows; declared triage counts sum |
| 7 | GROUND | GROUND | sweeps absent at base unconditionally, present in the admitted entry; fragments absent from the base registry, present at lands; the declared ground receipt committed with no nonzero exit line (absorbs the receipt check of r77-draft RECEIPTS) |
| 8 | CITEDLINES | CITEDLINES | the committed `tools/check-cited-lines.py` over the entries prints `CITED-LINES: 0 finding(s)` |
| 9 | CENSUS | CENSUS | `sources-census.sh validate --file <landed registry> --today <date>` exits 0 with no E-code line; a declared census-start receipt is committed and records the declared row count |
| 10 | SCRATCHMIRROR | (r76's mirror receipt slot) | reg-ids == the base registry id set; staged-ids covers every row_set staged id; collisions == reg-ids ∩ staged-ids; no adopted lane id already in reg-ids; the 1-3-space proof detects exactly one planted row and its list matches, the 4-space proof detects nothing; an optional mirror receipt is graded when declared |
| 11 | COLLCHECK | COLLCHECK | document identity (`_doc_url_key`) of the frozen document_url vs the row's source cell, plus the pinned staged→lane map when declared (r76 defect 2; raw-string/suffix comparison deleted) |
| 12 | FROZENCFG | FROZENCFG | frozen claims.json byte-identical at lands, strict base ancestry, round/status/frozen stamps, the pinned map digest (when declared), and the graded checkout IS `<lands>` (absorbs r77-draft STAMP's identity half) |
| 13 | INDEX | INDEX | README index row inside the entry's partition, every heading vs the live count, last footer total+vector, older footers preserved; PLUS `required_sections[]` checked here and never as out-of-set rows — for this claim the required `## Paths` bullet and `## Search log` entry in `corpus/SOURCES.md` |
| — | (dropped) | — | no other r76 leg exists: REPOINTED and CITEDLINES are r76 names and are kept; the r76 `INDEX` duplicate (R76-M2) is now impossible — `LEGS` names each leg once and main() refuses a frozen list that differs (duplicate, reorder, extra, missing) with exit 2 and `legs=0/13` |

Folded checks (r77 15-name draft → the 13 lineage legs): STAMP → FROZENCFG +
EVIDENCE; COUNTS → ENTRIES + ROWS; APPENDONLY → ROWS' rule-2-cell rule;
RECEIPTS → GROUND (ground receipt) + CENSUS (census-start); LEDGELIST → the
r76-style LEGCOUNT refusal in `main()` (plus `--emit-legs` and the printed
generated list), since the draft's C list carries no LEDGELIST name.

## Constants and schema replaced

- `ROUND 76 → 77`; every path under `reports/round-77/**`; lesson
  `corpus/lessons/round-77.md` with `BASE_LESSON = round-76.md`;
  `.ufo/waves/round-77/assimilation`; `ACCEPT-C-76 → ACCEPT-C-77`; scratch
  `kotodama-r76 → kotodama-r77`.
- `CLAIM_KEYS` = `entries, rows_before, knowledge_before, row_set,
  required_sections, ground, rejects, legs`.
- Optional frozen keys: `min_entries`, `rows_after`/`knowledge_after`,
  `map {path, sha256}`, `removed_ids[]`, `staged_ids` (path), `scratch_mirror
  {dir, receipt}`, `census_start {path, rows, contains[]}`,
  `ground.receipt {path, contains[]}`.
- Removed r76 schema: `candidates[]`, `min_admitted`, `requoted[]`,
  `reused_rows[]`, `map` as a REQUIRED key, `ground`-as-receipt-only, the
  r76 guard-proof `guard-proof` hard-coded PATH (now `scratch_mirror.dir`).

## Helper functions carried

67 shared names, unchanged semantics unless noted: `_lane_root`, `git`,
`git_bytes`, `sha256_text`, `counter_sha256`, `read_tree`, `tree_files`,
`is_ancestor`, `clone_at`, `materialize`, `parse_rows`, `row_cells`,
`row_usedby`, `leg`, `dedupe`, `header_block`, `section_block`, `gate_section`,
`quoted_spans`, `quote_ok`, `table_rows`, `urls_in`, `norm_url`, `nfkc_ws`,
`norm_label`, `_cfg_pct_decode`, `_doc_url_key`, `_archive_original`, `_window`,
`_evidence`, `_evidence_count`, `_evidence_fold`, `_min_entry_words`,
`_entry_citations`, `_entry_topic`, `_rows_cadence_ok`, `_footer_blocks`,
`_readme_sections`, `_md_count`, `_map_records`, `_paths_from_spec`,
`_staged_ids`, `_frozen_claim`, `_cfg_int`, `_cfg_sweeps`,
`_cfg_refusal_text`, `_cfg_access_date`, `_scratch_root`, `_forbidden_scratch`,
`leg_census`, `leg_evidence`, `leg_gate`, `leg_rejects`, `leg_ground`,
`leg_frozencfg`, `leg_index`, `leg_collcheck`, `leg_entries`, `leg_rows`,
`leg_repointed`, `leg_citedlines`, `load_frozen_config`, `print_receipt`,
`refuse`, `run_legs`, `main`, `run_selftest` (the last four rewritten in body,
same role).

Deleted from r76 (110 names): the r76 candidate/threshold config helpers
(`_cfg_candidates`, `_cfg_requoted`), the mirror/guard/map-collision machinery
(`_mirrorcoll_*`, `_guard_*`), the repointed campaign-id helpers
(`_repointed_*`), the loose URL matcher (`urls_compatible`, `_url_keys`,
`neutral_url_keys`, `_norm_path`, `_row_url_keys`, `_row_has_url`), the
`_gate_admit_row`/`_entries_*` r76 entry readers, and the r76 fixture/mutant
machinery (replaced by the `_st_*` fixture builder and the 35-case matrix).
