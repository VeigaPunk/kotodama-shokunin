# Round-75 claim-C counter — assembly contract (L1, pre-freeze)

The counter `accept-c.py` is assembled by the L1, in this order, from files in
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75/w2/parts/`:

1. PART A — lines 1-510 of `.ufo/waves/round-75/counters/accept-c.py` (docstring, imports, constants, regexes,
   helpers `norm_label norm_url nfkc_ws git git_bytes sha256_text counter_sha256 read_tree tree_files is_ancestor
   clone_at materialize parse_rows row_cells row_usedby leg dedupe header_block header_field_names source_lines
   urls_in neutral_url_keys _norm_path urls_compatible gate_section section_block quoted_spans quote_ok table_rows
   verdict_of is_admit_row is_reject_row col_index table_header`, constants `ROUND CLAIMS LESSON EVIDENCE_DIR ASSIM
   GROUND_RECEIPT BASE_LESSON CLAIM_KEYS RECHECK_RE REFUSAL_RE README_HEADING_RE ROW_SHAPED_LINE_RE ...`). FIXED. Nobody
   edits it; a seat needing a change in PART A messages the L1 (KotodamaR75a2) with the exact diff.
2. `part-cfg.py` — owner ExecCtrCfgMain: `_frozen_claim _paths_from_spec _id_list _row_pairs load_frozen_config` and the
   shared leg helpers (`_row_url_keys _gate_admit_row _min_entry_words _evidence _window _entry_citations`) — the r74
   lines 473-745. Leg seats CALL these helpers, never redefine them.
3. leg parts in this order, one file each, owner = the named seat; each defines the leg function and its private
   helpers (prefix `_<legfile>_`) ONLY:
   `leg-entries.py` -> `leg_entries(ctx)`; `leg-rows.py` -> `leg_rows`; `leg-repointed.py` -> `leg_repointed` (+ `_map_records`);
   `leg-gate.py` -> `leg_gate`; `leg-evidence.py` -> `leg_evidence` (+ `_evidence_core`); `leg-rejects.py` -> `leg_rejects`;
   `leg-ground-cited-census.py` -> `leg_ground leg_citedlines leg_census`; `leg-mirror-coll.py` -> `leg_scratch_mirror`
   `leg_collcheck` (+ `_guard_files _negated`); `leg-frozencfg.py` -> `leg_frozencfg`; `leg-index.py` -> `leg_index`
   (+ `_readme_sections _footer_blocks _entry_topic _md_count`).
4. `part-main.py` — owner ExecCtrCfgMain: `LEGS` (ordered ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS GROUND CITEDLINES
   CENSUS SCRATCHMIRROR COLLCHECK FROZENCFG INDEX — the order of claims.json claim C `legs`), `run_legs print_receipt refuse main`
   and the `if __name__ == "__main__": sys.exit(main())` guard. Verdict line `ACCEPT-C-75: PASS|FAIL legs=<p>/<n>`.
5. `part-selftest-fixtures.py` and `part-selftest-run.py` (owners ExecSelftestFixtures / ExecSelftestMutants) go BEFORE
   `part-main.py`'s guard: `run_selftest()` is called by `main(--selftest)`.

## cfg (dict returned by `load_frozen_config(root, freeze)`; every value read from `git show <freeze>:reports/round-75/claims.json`)

`freeze, frozen_sha256, base, access_date` ("2026-10-27"), `rows` (lane ids in order: S885..S893), `row_staged` (dict lane id ->
LIST of staged ids, from the `staged` text "S876/S885/S917/S921"), `row_doc` (dict lane id -> the claim's `document` string),
`reused` (list, empty), `reused_staged` (dict, empty), `entries` (3 repo-relative paths), `fragments` (9), `terms` (list;
r74's `cjk_terms` renamed), `refused_staged` (list of staged ids named in rejects.refused_staged_not_appended prose, e.g. ["S870"]),
`refused_staged_text` (the raw strings), `refused_files` (rejects.refused_files_pending_triage strings), `counts` (dict; may be {}),
`map_path, map_sha256, frozen_legs` (names in order), `allowed_ids` (set of lane ids), `forbidden_ids` (sorted staged ids not
lane ids), `owned_inplace` (claim list), `claim_keys`.

## ctx (dict handed to every leg)

`root` (lane repo, read-only git), `lands`, `mat` (checkout at lands — graded bytes), `mat_base` (git-archive tree at base),
`cfg`, `fleet_root`, `scratch` (scratch root; honour `$HYAKU_SCRATCH` and `--work`; NEVER hardcode /tmp, QUALITY 14 /
prompt §7.4). A leg returns bool via `leg(NAME, passed, detail)` (PART A prints one line per leg, detail first line <= 300 chars).
Every graded byte is read from `mat` (never from the lane worktree). Config reads only from `cfg`.

## Rules for every part

- Implement exactly the claim-C leg text in `reports/round-75/claims.json` (the frozen text is the claim); a leg may not
  be stronger or weaker than its wording; where the wording is ambiguous, state the reading in a comment and in your report.
- Template = round-74 counter `.ufo/waves/round-74/counters/accept-c.py` (mutation-tested in r74); the r75 deltas come from the
  w1 findings (`.ufo/waves/round-75/w1/{CritCCounterVacuity,RevClaimsFidelity,RevAssimilationContract,SimplifierRows,
  SentinelScope,MutRegistryCollision,ExecRenumber}.md`): multi-id staged rows, by-document map, page-level Persee URLs, whole-document
  vs excerpt evidence windows, README partition-heading exemption, owned_inplace.
- No new top-level imports; use those PART A imports. No network access in a leg (evidence is graded from committed bytes).
- Python 3 stdlib only. Deterministic. Python source must `python3 -B -m py_compile` clean when concatenated.
