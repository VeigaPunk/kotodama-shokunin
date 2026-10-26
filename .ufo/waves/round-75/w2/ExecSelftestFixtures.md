# ExecSelftestFixtures — round-75 w2, claim-C selftest fixture half

Seat: `ExecSelftestFixtures` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Date: 2026-10-27.

Built: `.ufo/waves/round-75/w2/parts/part-selftest-fixtures.py` — the fixture half of the assembled
claim-C counter (`build_fixture`, `MUTANTS`, `SURVIVORS`, `_selftest_scratch`, `_sfx_*` helpers).
Nothing in `reports/round-75/claims.json`, `ledger.json`, `accept-c.py` or any sibling part was
edited. No tool installed (no `pacman`, no network, no `uv`); only `git` and `python3` from the host.

## 1. Result

**L1 ruling applied (claims.json edited pre-data): `rejects.counts = {adopted 3, path_present 6,
refused 31, total_staged_files 40}` and the lesson must state `3 adopted / 6 path-present / 31
refused`.** The fixture now carries both — the frozen `counts` object and that exact triple in one
lesson paragraph. Two assemblies were run, and the difference between them is one line in
`leg-rejects.py`, not anything in this fixture:

1. **Stock parts (`leg-rejects.py` as of 16:59): `SELFTEST: 84/85`.** The only failing case is
   `clean`, red on REJECTS, because that revision still enforces `total == adopted + refused`:

   ```
   LEG FAIL REJECTS
        triage counts do not partition the staged files: 3 adopted + 31 refused != 40 staged
   ACCEPT-C-75: FAIL legs=12/13
   ```

   3 + 31 = 34 ≠ 40; the ruled triple adds the `path_present` column. This is the leg's arithmetic,
   not the fixture's — every other case, including all five rejects mutants, stays green.
2. **Ruled assembly (the same parts with exactly one line changed in a scratch copy of
   `leg-rejects.py`: `if t != a + r + int(counts.get("path_present") or 0):`): `SELFTEST: 85/85`,
   clean PASS 13/13.** That copy lives only in scratch and was deleted; `leg-rejects.py` in the
   parts directory is untouched, and ExecLegRejects owns it (the L1 says it has been messaged).

```
SELFTEST: 85/85
CASE mutant-table: PASS -- 78 mutants over 13/13 legs
CASE clean: PASS -- PASS 13/13 at 9c1a58b6c753
CASE lands-eq-base: PASS -- refused, FAIL printed
CASE freeze-eq-lands: PASS -- graded FAIL, FROZENCFG green
CASE missing-lands: PASS -- exit 2 naming --lands
CASE missing-freeze: PASS -- exit 2 naming --freeze
CASE no-data: PASS -- data legs red, FROZENCFG green
  ... 78 × CASE mutant:<name>: PASS -- LEG FAIL <expected leg> ...
```

and the positive fixture grades green on its own (exit 0, every leg PASS):

```
$ python3 -B accept-c.py --root <lane> --fleet-root <fleet> --lands 9c1a58b6c753 --freeze 4d8f04fe1f04
# stamped revision: 9c1a58b6c7531ee2a6798854b4b91295bd6ca4aa
# base revision: bf368424358e000469b50a2a074cc26adb391737
# freeze revision: 4d8f04fe1f043fcf0da00f9771c34a133acfeb13
# frozen map: .ufo/waves/round-75/assimilation/id-renumber-map.json sha256=596a432491e115ffa72d5351b27b88553e232cfef30196c5c552764d2010baf7
LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
     files=3 last-line=CITED-LINES: 0 finding(s) in 3 file(s)
LEG PASS CENSUS
     exit=0 last-line=file	ok	stub
LEG PASS SCRATCHMIRROR
     receipt@0 append@1 rows=9 entries=3
LEG PASS COLLCHECK
     ids=808 staged=12 collisions=5 guard=ok/ok map=12
LEG PASS FROZENCFG
  lands 9c1a58b6c753: lands==freeze=no first-parent-chain=yes claims@lands=frozen-bytes map=...(sha256-match) ledger=no-pin counter=absent
LEG PASS INDEX
     corpus/README.md: 6 section(s), myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s), 34 base / 42 lands line(s), 10 exempt line(s)
ACCEPT-C-75: PASS legs=13/13
rc 0
```

The three commit ids are stable across rebuilds of the same prefix: base `bf368424…`, freeze
`4d8f04fe…` (moved from `a6b17813…` when the `counts` object entered the fixture's frozen claims),
lands `9c1a58b6…`. The fixture is deterministic.

## 2. Fixture shape (`build_fixture(prefix, mut=None) -> (lane, fleet, base, freeze, lands)`)

Scratch: `$HYAKU_SCRATCH/kotodama-r75/<prefix>` (then `$SHOKUNIN_SCRATCH`, then
`/fast/scratch/hyaku/kotodama-r75`, then `tempfile.gettempdir()` as the last resort — never a
hardcoded `/tmp`). Each call recreates exactly `<root>/<prefix>/{lane,fleet}`; distinct prefixes share
no state, no port, no socket. `git init` in the lane and `rev-parse --show-toplevel` is asserted equal
to the lane with a realpath compare before the first commit. Commit dates are fixed and strictly
increasing (09:00 / 10:00 / 11:00 UTC on 2026-10-27), identity is `selftest <selftest@fixture.invalid>`
passed per-commit with `-c`, so no global identity is used.

Shapes copied from the real round, not invented: the row cells, the eight-line evidence grammar and
its `whole-document` variant (3720 visible chars) follow
`.ufo/waves/round-75/counters/probe-receipts/S885.txt`; the registry grammar follows
`corpus/SOURCES.md` at base; the entries' provenance blocks follow the mirror entries in
`assimilation/validate/corpus/knowledge/myth-symbol/`; the join keys, staged ids and document URLs
follow `assimilation/id-renumber-map.json`.

| commit | content |
|---|---|
| **base** `bf368424…` | `corpus/SOURCES.md` with 808 rows `S077…S884` (11 cells, no pipe, `queued`/`180d`); `corpus/knowledge/` with 249 `.md` files in the six partitions 32/29/40/29/24/95, **every file exactly 478 words** so the frozen floor and the derived floor agree; `corpus/README.md` with six `## <part>/ (N)` sections and two preserved `Counts checked` footers; `reports/round-71/telemetry/quarantine-verdicts.md` (PRESENT 1 / REFUSED 2 / UNVERIFIABLE 1); `tools/check-cited-lines.py` |
| **freeze** `4d8f04fe…` | `reports/round-75/claims.json` — claim C with the 9 rows (staged `S876/S885/S917/S921`, `S902`, `S904`, `S864`, `S865`, `S866`, `S905`, `S919`, `S870`), 3 entry paths, the ruled `rejects.counts` (`adopted 3, path_present 6, refused 31, total_staged_files 40` — the four integer keys only, no `note`; see §5.1), the 40-file triage families, 9 fragments + 2 terms, `access_date`, the 13 leg names, `owned_inplace` and the map pin; the by-document map (12 assignments, every staged id → its lane id with the row's document URL, plus the `map` table); `.ufo/waves/round-75/assimilation/validate-receipt.txt` (`validate --file`, exit 0, nine ids, three entry basenames); `reg-ids` (the 808 base ids), `staged-ids` (12), `collisions` (their exact intersection: `S864 S865 S866 S870 S876`); `guard-proof/guard-proof.txt` (a **staged** id planted at 3 spaces, found) and `guard-proof/four-space-control.txt` (a staged id at 4 spaces, not found) |
| **lands** `9c1a58b6…` | the nine rows `S885…S893` appended (mined, `2026-10-27`, `180d`, anchor = `quote located: «…»`, `used-by` = exactly the entries whose `source:` line cites the id); the three entries (nine-field header before the first `## `, body ≥ 620 words, one S-id per line); `corpus/lessons/round-75.md` (`## Gate` admit table with URL + `2026-10-27` + a ≤25-token/≤80-char quote + locator, a reject table with probed URL/reason/flip, the ruled counts paragraph `3 adopted / 6 path-present / 31 refused` of the 40, `## Quarantine`); nine evidence captures (`ua` + `user-agent` browser-shaped, `http-status: 200`, `bytes`, 64-hex body `sha256`, `challenge: none`, `--- window ---` with recomputed `window-sha256`/`window-bytes`, `window-scope` `excerpt` ×8 (4200 chars) and `whole-document` ×1 (3720 chars = `visible-chars`)); `reports/round-75/telemetry/gap-sweep.txt` (808-row registry, 0 per fragment); `corpus/README.md` with the three verbatim `- topic:` rows inside myth-symbol, the `(32)` heading and the appended `Total knowledge entries: 252.` + `(total 252 files; directory totals 32/32/40/29/24/95)` block (base footers untouched) |

The positive lands therefore satisfies the frozen numbers themselves: 808 → 817 rows, 249 → 252 files,
myth-symbol 29 → 32, vector 32/32/40/29/24/95, floor 478.

`used-by` derivation is a single source of truth (the entries' `source:` lines), so the ROWS
"used-by exactly the citing entries" clause cannot be satisfied by accident:
`S885 → A,B,C`; `S886,S891,S892 → B`; `S887 → B,C`; `S888,S889,S890,S893 → A`.

## 3. MUTANTS — 78 named single defects (name → leg that must go red)

`MUTANTS` is a list of `(name, expected_leg, spec)`; `spec` is a dict (a zero-arg callable is also
accepted). Two special specs: `{"no_data": True}` and `{"lands_is_freeze": True}`.

| leg | mutants (all PASS in the runner: `LEG FAIL <leg>`) |
|---|---|
| ENTRIES (6) | `entry_missing`, `entry_stub`, `entry_body_short`, `entry_header_placeholder`, `entry_template_token`, `entry_at_base` |
| ROWS (12) | `row_extra`, `row_removed_pre_existing`, `row_pre_existing_edited`, `row_staged_opened`, `row_recheck_prose`, `row_escaped_pipe`, `row_cell_count`, `row_status_queued`, `row_usedby_extra`, `row_usedby_missing`, `row_anchor_no_quote`, `row_missing_s890` |
| REPOINTED (4) | `source_url_mismatch`, `source_staged_id` (S893→S870), `inline_staged` (body cites S864), `inline_base_row` (body cites S500) |
| GATE (7) | `gate_quote_tokens` (26 tokens), `gate_quote_chars` (103 chars), `gate_admit_date`, `gate_admit_locator`, `gate_admit_url`, `gate_reject_no_flip`, `gate_reject_no_url` |
| EVIDENCE (12) | `evidence_missing`, `evidence_quote_absent`, `window_sha_tamper`, `window_bytes_mismatch`, `evidence_bad_ua`, `evidence_bad_status`, `evidence_bad_body_sha`, `evidence_short_window`, `evidence_whole_4096`, `evidence_visible_mismatch`, `evidence_scope_unknown`, `evidence_fetch_other` |
| REJECTS (5) | `rejects_no_s870`, `rejects_no_counts`, `rejects_family_renamed`, `quarantine_missing`, `quarantine_no_refused` |
| GROUND (4) | `ground_missing`, `ground_fragment_missing`, `ground_rows_wrong`, `ground_fragment_at_base` |
| CITEDLINES (3) | `citedlines_multi_id`, `citedlines_table_id`, `citedlines_tool_missing` |
| CENSUS (1) | `census_fail` |
| SCRATCHMIRROR (5) | `receipt_missing`, `receipt_no_exit`, `receipt_missing_id`, `receipt_in_append`, `receipt_no_file_flag` |
| COLLCHECK (7) | `coll_adopted_in_regids`, `coll_adopted_in_collisions`, `coll_fourspace_found`, `coll_plant_real_id`, `coll_tab_plant`, `coll_lowercase_plant`, `coll_staged_missing` |
| FROZENCFG (3) | `config_edited_at_lands`, `claims_missing_at_lands`, `map_sha_mismatch` |
| INDEX (9) | `index_missing_row`, `index_topic_mismatch`, `index_heading_stale`, `index_footer_total`, `index_footer_vector`, `index_older_footer_edited`, `index_row_outside_section`, `index_row_duplicated`, `index_sid_row` |

Every one of the 13 legs is exercised (the runner's `mutant-table` case asserts that).

Notes on attribution, so a reviewer is not surprised by a second red leg:

* `gate_quote_tokens` / `gate_quote_chars` also redden EVIDENCE: the quote is stored identically in
  the row anchor, the Gate cell and the window (one defect, carried consistently), but the EVIDENCE
  leg filters Gate spans by `quote_ok` first, so an over-cap span leaves it no span to couple.
* `row_missing_s890` and `row_anchor_no_quote` also redden the coupling legs (evidence row keys /
  Gate anchor quote). The named leg is the clause the defect violates.
* `map_sha_mismatch` also reddens REPOINTED and COLLCHECK: both read the map under its pin.

Coverage of the w1 junk paths (mapping also written above `MUTANTS` in the part):

* **CritCCounterVacuity.md**: each leg's structural junk landing is a mutant (`entry_stub`/`entry_body_short`,
  `row_staged_opened`, `source_url_mismatch`, `gate_quote_*`, `window_sha_tamper`,
  `rejects_family_renamed`, `ground_*`, `citedlines_*`, `census_fail`, `receipt_*`, `coll_plant_real_id`,
  `config_edited_at_lands`, `index_*`). The survivors that no committed-bytes counter can refuse are
  listed in `SURVIVORS` with the reason, never asserted red.
* **MutRegistryCollision.md m1…m8**: m1/m2 are the positive control (the clean guard proof plants a
  staged id at 3 spaces and reports it found); m3 → `coll_fourspace_found`; m4 → the proof must plant
  a *staged* id inside the 1-3-space grammar (`coll_plant_real_id` + the base/clean proof); m5 →
  `coll_tab_plant`; m6 → `coll_lowercase_plant`; m7 → SURVIVOR `guard_four_digit_id`; m8 →
  `coll_adopted_in_collisions` / `coll_adopted_in_regids`.
* **junk-fixtures.py**: J1 → `entry_stub`; J2 → `evidence_quote_absent`; J3 →
  `config_edited_at_lands` / `claims_missing_at_lands`. J4x/J5-J10/G/R are claim Ca's and are not
  fixtures of this counter.

### SURVIVORS (recorded, not asserted red)

`entry_filler_body` (ENTRIES is a length-and-shape gate), `gate_fabricated_quote` (page truth needs
the routed ordinary re-open), `evidence_fabricated_window` (the stored window authenticates bytes, not
a fetch), `mirror_fabricated_receipt` (prose-only mirror; CENSUS owns execution),
`guard_fabricated_marker` (the guard is pattern-matched, not executed), `guard_four_digit_id` (m7),
`citedlines_stub_tool` (no blob is pinned — the fixture ships a real linter instead),
`ground_fabricated_receipt` (offline-unprovable; the independent base re-derivation is what bites).

## 4. What the fixture had to decide, and why

1. **The floor is the frozen 478, and the base tree is built to match.** `leg_entries` grades the
   frozen constant and only *reports* the derived minimum. The fixture makes all 249 base files
   exactly 478 tokens anyway, so the positive receipt prints no provenance note and the fixture is
   the same shape as the round rather than a weaker one.
2. **Entry padding targets the body, not the file.** The first assembled run failed ENTRIES on the
   positive tree (355/373-word bodies) because the long provenance header ate the 620-word file
   target. `_sfx_pad_body` pads from the first `## `; the body is 620 words.
3. **`check-cited-lines.py` is embedded, faithfully.** An assembled counter running from a scratch
   directory has no lane (`LANE` points at a non-repo), so reading the lane's tool silently degraded
   to a stub and the two CITEDLINES mutants stayed green. The part now ships a ~60-line
   reimplementation of the real tool's contract (MULTI-ID / TABLE-ID, `CITED-LINES: k finding(s) in m
   file(s)`, exit 1 on k>0). The frozen wording pins no blob, so this is a fixture's own tool, not a
   weakened authority — and a stub would have hidden exactly the defect the leg exists for.
4. **The reject table is one table for two legs.** GATE reads its probed-URL/reason/flip columns;
   REJECTS reads the same rows as refused-file buckets. Bucket rows therefore declare their file
   count as `(N)`, carry a real probed URL and a `rejected` verdict, and a dedicated
   `probe-only candidate` row (no declared count) absorbs the flip/URL mutants so they do not
   cascade into REJECTS.
5. **`## Quarantine` is re-derived, not asserted.** The lesson's numbers (PRESENT 1 / REFUSED 2 /
   UNVERIFIABLE 1, total 4, S816/S817) match the committed
   `reports/round-71/telemetry/quarantine-verdicts.md` the leg reads.

## 5. Risks / open items (for the L1 and the leg owners — not fixed here, not mine to edit)

1. **REJECTS: the ruled triple is in the fixture; `leg-rejects.py` has not caught up.** With the L1
   ruling the fixture states `3 adopted / 6 path-present / 31 refused` of 40 and freezes the matching
   `counts`. The stock leg (16:59) still checks `t == a + r`, so the clean fixture goes red with
   `triage counts do not partition the staged files: 3 adopted + 31 refused != 40 staged`; adding
   `path_present` to that identity makes the whole suite 85/85 (§1). The leg owner must make the
   ternary sum the check (and keep the bucket reconciliation against `refused`, which the fixture
   already satisfies: the seven frozen families sum to 31).
2. **`rejects.counts.note` will break FROZENCFG on the real landing.** `part-cfg.load_frozen_config`
   keeps only integer values in `cfg["counts"]`, while `leg_frozencfg._frozencfg_counts` stringifies
   *every* frozen key and compares the two maps; the note the L1 added to `counts` therefore makes
   `got_counts != want_counts`. The fixture's `counts` deliberately carries the four integer keys
   only (so its FROZENCFG stays green), but the real claims.json does not. Either the leg compares
   only the integer keys, or the note moves out of `counts`. My fixture change is not a fix for the
   real file — it is a way to keep the fixture's frozen claim byte-consistent with what the loader
   can parse. Flagged to `KotodamaR75a2` together with this report.
3. **Gate quote-cap mutants cascade into EVIDENCE** by construction (see §3). If the runner is ever
   tightened to "exactly one red leg", these three cases (`gate_quote_tokens`, `gate_quote_chars`,
   plus `row_missing_s890`, `row_anchor_no_quote`, `map_sha_mismatch`) will need the cascade
   documented or the fixture relaxed; today the runner asserts the named leg is red, which is the
   right assertion.
4. **CENSUS runs against a fleet stub** in the fixture (the fixture's fleet root carries
   `scripts/sources-census.sh`). That grades the leg's own contract (exit 0, no `E\d\d` line); the
   real fleet script over the real landing is the L1's post-integration gate.
5. **The fixture hard-codes the round's real shape numbers** (808/817 rows, 249/252 files,
   32/32/40/29/24/95, 478). If the frozen claim's numbers move after this wave, the positive fixture
   will not track them: `_SFX_BASE_PARTITIONS`, `_SFX_LANDS_MYTH`, `_SFX_BASE_WORDS` and the row
   tuples are the single place to change.
6. Not a defect but worth recording: the fixture's registry/entries are synthetic text in the real
   grammar. It proves the counter's mechanics, never page truth; the claim's kill rule rests on the
   routed ordinary re-open, and `SURVIVORS` says so.

## 6. Files written

| path | sha256 |
|---|---|
| `.ufo/waves/round-75/w2/parts/part-selftest-fixtures.py` (1408 lines, `python3 -B -m py_compile` clean when assembled) | `ce6dffc2c12a2b9c2dc7693d14996b0ca62c7fd0034b72c159b5155cf791238e` |
| `.ufo/waves/round-75/w2/ExecSelftestFixtures.md` (this report) | not self-referential; the part above is the artifact that matters |

No lane file outside `.ufo/waves/round-75/w2/` was written; the lane's git/jj state and index are
untouched (read-only `git show`/`git ls-tree` only). All scratch lived under
`/fast/scratch/hyaku/kotodama-r75/ExecSelftestFixtures/` (assembly copy, selftest receipt, the report
clean fixture) and was deleted before this report was yielded; no `/tmp` path is cited.
