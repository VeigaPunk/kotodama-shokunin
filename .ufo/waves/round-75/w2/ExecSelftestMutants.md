# ExecSelftestMutants — round 75, wave 2 (claim C counter: selftest runner half)

Seat: `ExecSelftestMutants` (leaf executor). Lane base read-only at
`f556d1049fe651d3d63975600b13acd9fb686f15`; nothing was landed, staged or committed by me.
I did not edit `reports/round-75/claims.json`, `ledger.json` or any counter.

## Deliverable

| file | sha256 | size |
| --- | --- | --- |
| `.ufo/waves/round-75/w2/parts/part-selftest-run.py` | `1f4c1ac484e859cd9e7dbba4e573f0b359137be7ffa76966759c83ec7efac14b` | 14715 bytes, 327 lines |

Function definitions only (CFG-CONTRACT item 5): no top-level imports (PART A's imports are
used), no `__main__` guard, ASCII only, module-level names `_STR_LEG_ORDER`, `_STR_TIMEOUT`,
`_str_scratch`, `_str_tmpdir`, `_str_slug`, `_str_mutants`, plus the two required functions
`_run_counter(lane, fleet, lands, freeze=None, extra=None, omit_lands=False)` and
`run_selftest()`. No sibling part defines any of these names (checked across all 14 parts).

## Interface agreed with ExecSelftestFixtures (message exchange, acted on by both)

- `MUTANTS` = list of 3-tuples `(name, expected_leg, mutate)`; `expected_leg` is one of the 13
  claim-C leg names; `mutate` is a dict spec **or** a zero-arg callable returning one.
  (`_str_mutants()` also accepts the r74 mapping shape plus `EXPECTED_FAIL`, so an assembly
  mistake cannot silently skip every mutant; that fallback is exercised in my unit harness.)
- `build_fixture(prefix, mut=None) -> (lane, fleet, base, freeze, lands)`, all absolute paths,
  `base`/`freeze`/`lands` 40-hex; `mut=None` builds a tree that passes 13/13; specs are
  independent per prefix; cleanup is mine.
- Optional `_selftest_scratch()` (idempotent) is consumed through `globals()`, so both halves
  share one scratch root; `build_fixture` is called with the caller's `prefix` and spec only.

## What run_selftest() asserts

Seven fixed cases plus one case per `MUTANTS` entry (final: 78 mutants, 85 cases):

| case | assertion |
| --- | --- |
| `mutant-table` | `MUTANTS` is non-empty; every one of the 13 legs is exercised by at least one mutant; no mutant expects an unknown leg name |
| `clean` | `build_fixture("r75st-clean")` → exit 0, `ACCEPT-C-75: PASS legs=13/13`, every one of the 13 legs `LEG PASS`, receipt carries `# evaluated revision: <lands>` and `# freeze revision: <freeze>` |
| `lands-eq-base` | counter run at the frozen base → exit 2, an `ACCEPT-C-75: FAIL` line (stdout or stderr), and never a `PASS` line |
| `freeze-eq-lands` | counter run at the freeze → **graded**, exit 1, `ACCEPT-C-75: FAIL`, `LEG PASS FROZENCFG`, `LEG FAIL ENTRIES`/`LEG FAIL ROWS`, no `REFUSED` on stderr |
| `missing-lands` | `--lands` omitted → exit 2 and `--lands` named on stderr |
| `missing-freeze` | `--freeze` omitted → exit 2 and `--freeze` named on stderr |
| `no-data` | lands commit after the freeze with no claim-C artefact (`{"no_data": True}`) → exit 1, data legs red, `FROZENCFG` green |
| `mutant:<name>` | exit 1, `ACCEPT-C-75: FAIL`, and `LEG FAIL <expected_leg>`; a wrong-leg mutant is reported with the legs that did go red |

`SELFTEST: <passed>/<total>` is printed last; exit 0 only when every case passes. A case that
cannot run (fixture build raised, returned the wrong tuple or a non-40-hex shim) is recorded as
a **failed case with the reason**, never dropped from the denominator; `build_fixture` missing
entirely yields `CASE fixtures: FAIL` + `SELFTEST: 0/1`.

Readings where the claim text needed one (also commented in the part):
- `lands == freeze` is graded, not refused — the counters' own `refuse()` path is rejected by the
  case, and FROZENCFG must be green because `claims.json` at lands is byte-identical to the freeze blob.
- The refusal stream is not part of the claim, so `ACCEPT-C-75: FAIL` is looked for in stdout+stderr;
  a PASS line in either stream fails the case.
- Leg names come from the literal claims order (`_STR_LEG_ORDER`), not from the assembled `LEGS`,
  so a leg list reordered in `part-main.py` cannot make the coverage case vacuous.

Scratch: every fixture, the counter's own grading clone (via `TMPDIR`) and my temp dir live under
`$HYAKU_SCRATCH/kotodama-r75` (fallback `/fast/scratch/hyaku/kotodama-r75`, system tmp only if
`/fast` is absent). Cleanup removes exactly the fixture paths returned, their per-prefix parent
when it sits strictly below the scratch root, and this run's `selftest-tmp-<pid>` — never the
scratch root and never a seat directory (tested; see "cleanup" below).

## Assembled run (all parts present)

Assembly reproduced by me in scratch, in the order CFG-CONTRACT + `part-main.py`'s ASSEMBLY note
require: PART A (lines 1-510 of `.ufo/waves/round-75/counters/accept-c.py`), `part-cfg.py`, the ten
leg parts in claims order, `part-main.py` **body** (its last three lines are the guard),
`part-selftest-fixtures.py`, `part-selftest-run.py`, then the guard. Counter sha256
`64a578d26e3c42407e90e06a455dc3ac5c4d407105743591a96e0cf5b9902018` (6104 lines);
`part-selftest-fixtures.py` sha256 `7b4c507de076233e4e90fde7a93c807257c34fd2d90b07eaba5258e46b9d4343`
(the fixture owner's own final bytes). Command:

```
cd <scratch>/asm && HYAKU_SCRATCH=<scratch> python3 -B accept-c.py --selftest
→ SELFTEST: 85/85   exit 0
```

Transcript sha256 `ab3d3932b7d8a8c926e70d933d8a981495f8a162052503e7b382b5395a1bf0dd`:

```text
CASE mutant-table: PASS -- 78 mutants over 13/13 legs
CASE clean: PASS -- PASS 13/13 at c4087ae7fbbe
CASE lands-eq-base: PASS -- refused, FAIL printed
CASE freeze-eq-lands: PASS -- graded FAIL, FROZENCFG green
CASE missing-lands: PASS -- exit 2 naming --lands
CASE missing-freeze: PASS -- exit 2 naming --freeze
CASE no-data: PASS -- data legs red, FROZENCFG green
CASE mutant:entry_missing: PASS -- LEG FAIL ENTRIES
CASE mutant:entry_stub: PASS -- LEG FAIL ENTRIES
CASE mutant:entry_body_short: PASS -- LEG FAIL ENTRIES
CASE mutant:entry_header_placeholder: PASS -- LEG FAIL ENTRIES
CASE mutant:entry_template_token: PASS -- LEG FAIL ENTRIES
CASE mutant:entry_at_base: PASS -- LEG FAIL ENTRIES
CASE mutant:row_extra: PASS -- LEG FAIL ROWS
CASE mutant:row_removed_pre_existing: PASS -- LEG FAIL ROWS
CASE mutant:row_pre_existing_edited: PASS -- LEG FAIL ROWS
CASE mutant:row_staged_opened: PASS -- LEG FAIL ROWS
CASE mutant:row_recheck_prose: PASS -- LEG FAIL ROWS
CASE mutant:row_escaped_pipe: PASS -- LEG FAIL ROWS
CASE mutant:row_cell_count: PASS -- LEG FAIL ROWS
CASE mutant:row_status_queued: PASS -- LEG FAIL ROWS
CASE mutant:row_usedby_extra: PASS -- LEG FAIL ROWS
CASE mutant:row_usedby_missing: PASS -- LEG FAIL ROWS
CASE mutant:row_anchor_no_quote: PASS -- LEG FAIL ROWS
CASE mutant:row_missing_s890: PASS -- LEG FAIL ROWS
CASE mutant:source_url_mismatch: PASS -- LEG FAIL REPOINTED
CASE mutant:source_staged_id: PASS -- LEG FAIL REPOINTED
CASE mutant:inline_staged: PASS -- LEG FAIL REPOINTED
CASE mutant:inline_base_row: PASS -- LEG FAIL REPOINTED
CASE mutant:gate_quote_tokens: PASS -- LEG FAIL GATE
CASE mutant:gate_quote_chars: PASS -- LEG FAIL GATE
CASE mutant:gate_admit_date: PASS -- LEG FAIL GATE
CASE mutant:gate_admit_locator: PASS -- LEG FAIL GATE
CASE mutant:gate_admit_url: PASS -- LEG FAIL GATE
CASE mutant:gate_reject_no_flip: PASS -- LEG FAIL GATE
CASE mutant:gate_reject_no_url: PASS -- LEG FAIL GATE
CASE mutant:evidence_missing: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_quote_absent: PASS -- LEG FAIL EVIDENCE
CASE mutant:window_sha_tamper: PASS -- LEG FAIL EVIDENCE
CASE mutant:window_bytes_mismatch: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_bad_ua: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_bad_status: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_bad_body_sha: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_short_window: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_whole_4096: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_visible_mismatch: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_scope_unknown: PASS -- LEG FAIL EVIDENCE
CASE mutant:evidence_fetch_other: PASS -- LEG FAIL EVIDENCE
CASE mutant:rejects_no_s870: PASS -- LEG FAIL REJECTS
CASE mutant:rejects_no_counts: PASS -- LEG FAIL REJECTS
CASE mutant:rejects_family_renamed: PASS -- LEG FAIL REJECTS
CASE mutant:quarantine_missing: PASS -- LEG FAIL REJECTS
CASE mutant:quarantine_no_refused: PASS -- LEG FAIL REJECTS
CASE mutant:ground_missing: PASS -- LEG FAIL GROUND
CASE mutant:ground_fragment_missing: PASS -- LEG FAIL GROUND
CASE mutant:ground_rows_wrong: PASS -- LEG FAIL GROUND
CASE mutant:ground_fragment_at_base: PASS -- LEG FAIL GROUND
CASE mutant:citedlines_multi_id: PASS -- LEG FAIL CITEDLINES
CASE mutant:citedlines_table_id: PASS -- LEG FAIL CITEDLINES
CASE mutant:citedlines_tool_missing: PASS -- LEG FAIL CITEDLINES
CASE mutant:census_fail: PASS -- LEG FAIL CENSUS
CASE mutant:receipt_missing: PASS -- LEG FAIL SCRATCHMIRROR
CASE mutant:receipt_no_exit: PASS -- LEG FAIL SCRATCHMIRROR
CASE mutant:receipt_missing_id: PASS -- LEG FAIL SCRATCHMIRROR
CASE mutant:receipt_in_append: PASS -- LEG FAIL SCRATCHMIRROR
CASE mutant:receipt_no_file_flag: PASS -- LEG FAIL SCRATCHMIRROR
CASE mutant:coll_adopted_in_regids: PASS -- LEG FAIL COLLCHECK
CASE mutant:coll_adopted_in_collisions: PASS -- LEG FAIL COLLCHECK
CASE mutant:coll_fourspace_found: PASS -- LEG FAIL COLLCHECK
CASE mutant:coll_plant_real_id: PASS -- LEG FAIL COLLCHECK
CASE mutant:coll_tab_plant: PASS -- LEG FAIL COLLCHECK
CASE mutant:coll_lowercase_plant: PASS -- LEG FAIL COLLCHECK
CASE mutant:coll_staged_missing: PASS -- LEG FAIL COLLCHECK
CASE mutant:config_edited_at_lands: PASS -- LEG FAIL FROZENCFG
CASE mutant:claims_missing_at_lands: PASS -- LEG FAIL FROZENCFG
CASE mutant:map_sha_mismatch: PASS -- LEG FAIL FROZENCFG
CASE mutant:index_missing_row: PASS -- LEG FAIL INDEX
CASE mutant:index_topic_mismatch: PASS -- LEG FAIL INDEX
CASE mutant:index_heading_stale: PASS -- LEG FAIL INDEX
CASE mutant:index_footer_total: PASS -- LEG FAIL INDEX
CASE mutant:index_footer_vector: PASS -- LEG FAIL INDEX
CASE mutant:index_older_footer_edited: PASS -- LEG FAIL INDEX
CASE mutant:index_row_outside_section: PASS -- LEG FAIL INDEX
CASE mutant:index_row_duplicated: PASS -- LEG FAIL INDEX
CASE mutant:index_sid_row: PASS -- LEG FAIL INDEX
SELFTEST: 85/85
```

## Unit evidence for the runner itself (independent of the fixture part)

A harness in scratch execs `part-selftest-run.py` into one namespace, supplies a fake
`build_fixture` (git init, three commits, `-C` on every call, toplevel asserted) and a fake
counter body whose verdict shapes follow the claim, then runs `--selftest`:

```
CASE clean: PASS -- PASS 13/13 at <sha>          (20 cases)
SELFTEST: 20/20                                  exit 0
HARNESS_BREAK=clean → CASE clean: FAIL -- exit 1, want 0 | ... | ENTRIES must be green
SELFTEST: 19/20                                  exit 1
```

Further probes against the same part: `_run_counter` against a counter that sleeps 5 s with
`_STR_TIMEOUT = 1` → `returncode 124`, `TIMEOUT after 1s` on stderr (a hang is a reported case
failure, not a kill); missing `build_fixture` → `CASE fixtures: FAIL ... SELFTEST: 0/1`, exit 1;
`build_fixture` returning `("zz","zz","zz")` → cases fail with "non-40-hex commit", no crash;
`build_fixture` raising → cases fail with "raised RuntimeError: boom", no crash; dict-shaped
`MUTANTS` + `EXPECTED_FAIL` → normalised to `[('a','ENTRIES',{...}), ('b','ROWS',{...})]`;
a non-dict spec is reported, not swallowed. `compile()` of PART A + this part succeeds.

## Defects the selftest caught (fixture snapshot at 16:57, 77/85)

Quote from the owner's reply: "Fixture half is stable and green ... `SELFTEST: 85/85`", and the
same lands sha `c4087ae7fbbe923c38726e8f8c5d7f32d04a9e96` for `r75st-clean` in both runs. The
cases that were red against the earlier fixture bytes, all fixed by the fixture owner:

- `clean`: positive tree red on ENTRIES and INDEX (entry bodies 355/373 words against the
  478-word gate; header padding counted in the wrong place) — no PASS 13/13 at all.
- wrong leg red: `row_escaped_pipe`, `gate_quote_tokens`, `gate_quote_chars`,
  `rejects_family_renamed`, `citedlines_multi_id`, `citedlines_table_id`.
- `build_fixture` crash: `evidence_quote_absent` (`TypeError: _sfx_evidence_text() got multiple
  values for argument 'quote'`); a later mid-edit snapshot crashed every non-`no_data` spec with
  `TypeError: not all arguments converted during string formatting` (11 `%s` for 12 values).

Two cleanup defects of my own were found by running for real and are fixed in the shipped part:
(1) the first version removed `<scratch>/<seat-name>`, which deleted the seat's own scratch tree
when `HYAKU_SCRATCH` was unset — it now removes only its own `selftest-tmp-<pid>`; (2) the first
fixture cleanup left 61k empty per-prefix directories because it required a single parent across
the whole run — it now groups by parent and removes each fixture-owned parent. Last run left
`<root>` and the counter's own empty `counter/` work dir only (2 entries).

## Risks / open items

- PART A's docstring (line 154) says the selftest scratch root is `$SHOKUNIN_SCRATCH`; the wave
  dispatch, CFG-CONTRACT prompt §7.4 and the fixture builder use `$HYAKU_SCRATCH/kotodama-r75`.
  The part honours HYAKU first, then SHOKUNIN, then `/fast/scratch/hyaku`. The L1 may want the
  docstring reconciled; no behaviour depends on the resolution.
- The shared scratch root is being wiped by sibling seats mid-wave (my `harness.py` and assembled
  copies vanished at ~17:00 along with several seat dirs). A sibling `rm -rf <root>` during a
  selftest run shows up as failed fixture builds — reported as failed cases, never as a false
  PASS — but a green run needs a quiet root.
- The `clean` case asserts the receipt lines `# evaluated revision: <full lands>` and
  `# freeze revision: <full freeze>`; `part-main.py:88,92` print them and the assembled run
  confirms it. If `print_receipt` is later changed to abbreviate, that case fails by design.
- Mutant coverage is a hard case: if a mutation is dropped so that any of the 13 legs loses its
  only mutant, `mutant-table` fails. That is intended (a selftest that stops exercising a leg is
  not evidence about that leg).

## Files written by me

- `.ufo/waves/round-75/w2/parts/part-selftest-run.py` (only implementation file)
- this report (`.ufo/waves/round-75/w2/ExecSelftestMutants.md`)

No tool installs or upgrades were needed. Scratch under
`/fast/scratch/hyaku/kotodama-r75/ExecSelftestMutants/` is deleted before yielding.
