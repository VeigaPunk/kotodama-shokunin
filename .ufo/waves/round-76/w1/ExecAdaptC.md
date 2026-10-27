# ExecAdaptC — ACCEPT-C-76 (round 76, wave 1, BUILD seat)

Seat: `ExecAdaptC` (leaf). Assignment: adapt `reports/round-75/accept-c.py` into
`ACCEPT-C-76` under `.ufo/waves/round-76/w1/stage/ExecAdaptC/`, data-driven by the
frozen `claims.json`, for the DRAFT threshold claim C (four candidate files,
`n >= 2` admitted, rows `817 -> 817+k`), plus the draft claim object and a
schema-delta note. No lane file was written; nothing was committed.

**Verdict: BUILT, selftest green — `SELFTEST: 94/94`.**

## Files written (all inside my seat's `w1/stage` area)

| path | bytes / sha256 | what |
|---|---|---|
| `.ufo/waves/round-76/w1/stage/ExecAdaptC/accept-c.py` | 6686 lines, `9db9305d5b4a7a8df8e9173e521e34ed40ef52b7680631dd2039e14a5142dd12` | the ACCEPT-C-76 counter |
| `.ufo/waves/round-76/w1/stage/ExecAdaptC/claim-C.json` | 14161 B, `771cb2821901249f0688739f286855a464f31a3e69de213e202408d26a7ea316` | the DRAFT claim document (loadable as `reports/round-76/claims.json`) |
| `.ufo/waves/round-76/w1/stage/ExecAdaptC/SCHEMA-DELTA.md` | 8 KB | per-key schema deltas, per-leg readings, refusals, findings |
| `.ufo/waves/round-76/w1/stage/ExecAdaptC/selftest-receipt.txt` | 96 lines | raw `--selftest` output |
| `.ufo/waves/round-76/w1/stage/ExecAdaptC/redbefore-r75-freeze-refusal.txt` | 4 lines | red-before: round-76 counter at round-75's freeze (exit 2) |

Numbers cited:
- `6686` — `wc -l .ufo/waves/round-76/w1/stage/ExecAdaptC/accept-c.py` (round-75: `6145` — same command on `reports/round-75/accept-c.py`).
- `43` functions changed/added of `178` — `python3`+`ast` per-function `difflib` over both files (table below).
- `1237` added / `696` removed diff lines — `diff -u reports/round-75/accept-c.py accept-c.py | grep -c '^+'` / `'^-'`.

## Selftest (the load-bearing receipt)

```
$ HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r76/ExecAdaptC python3 -B accept-c.py --selftest
CASE mutant-table: PASS -- 87 mutants over 13/13 legs
CASE clean: PASS -- PASS 13/13 at 415e1e4aea8a
CASE lands-eq-base: PASS -- refused, FAIL printed
CASE freeze-eq-lands: PASS -- graded FAIL, FROZENCFG green
CASE missing-lands: PASS -- exit 2 naming --lands
CASE missing-freeze: PASS -- exit 2 naming --freeze
CASE no-data: PASS -- data legs red, FROZENCFG green
... 87 `CASE mutant:<name>: PASS -- LEG FAIL <LEG>` ...
SELFTEST: 94/94
```
`94` cases — `grep -c '^CASE ' selftest-receipt.txt`; `87` mutants —
`grep -c '^CASE mutant:' selftest-receipt.txt`; round-75's receipt was 85/85, so
the denominator grew by the new limbs (below) and no case is red.
Full raw output: `selftest-receipt.txt` (same directory).

Scratch-root discipline (prompt §7.4):
```
$ grep -nE '"/tmp|/tmp/' accept-c.py
(no output)
$ echo $?
1
```
The only `/tmp` token the round-75 counter carried was `os.path.abspath("/tmp")`
in `_forbidden_scratch`; it is now `os.path.abspath(os.sep + "tmp")`.
Scratch resolution is `--work` → `$HYAKU_SCRATCH/kotodama-r76/counter` →
`$TMPDIR/kotodama-r76/counter` (an operator-chosen TMPDIR) → the operator default
`/fast/scratch/hyaku/kotodama-r76/counter`; the system temporary directory is
refused with a FAIL line, never written to.
`python3 -B -m py_compile accept-c.py` — silent, exit `0`.

## Constants replaced (and made data-driven)

Round tokens: `ROUND = 76`, `reports/round-76/{claims.json,evidence/,telemetry/gap-sweep.txt}`,
`corpus/lessons/round-76.md`, `.ufo/waves/round-76/assimilation/`, `BASE_LESSON =
corpus/lessons/round-75.md`, verdict prefix `ACCEPT-C-76`, scratch `kotodama-r76`,
announced: `migration` — the sed pass was read back by
`grep -n "ROUND = \|ACCEPT-C-7\|kotodama-r7" accept-c.py`.

Every constant the counter grades with is read from
`git show <freeze>:reports/round-76/claims.json` (`load_frozen_config`), and
FROZENCFG re-derives each of them from those bytes. New frozen keys:
`candidates[].admitted`, `min_admitted`, `rows_before`, `knowledge_before`,
`ground.sweeps[]`, `ground.receipt`, `requoted[]`. `entries[]` survives only as
an optional cross-check that must equal the admitted subset.

## Per-leg diff against the round-75 counter

| leg | changed function(s) (+/- lines) | round-75 assumption removed |
|---|---|---|
| ENTRIES | `leg_entries` +25/-0 | exact 3-entry set → `n >= min_admitted`, refused-candidate absence, `knowledge_before + n` |
| ROWS | `leg_rows` +100/-9 | exact 9-row set → `rows_before -> rows_before+k`, k derived from cited DOCUMENTS, one row per document, no base-held re-add, no tier-C-only support |
| REPOINTED | `_repointed_problem` +19/-14, `leg_repointed` +5/-4 | hard-coded `S870 -> S893` → frozen `requoted[]`; already-held base rows resolvable by document |
| GATE | none | (generic over `cfg["rows"]+cfg["reused"]`, access date frozen) |
| EVIDENCE | `_evidence` +1/-1 (path token) | none |
| REJECTS | none | (counts bound to `len(entries)`; family sums) |
| GROUND | `leg_ground` +113/-57, `_ground_scope_files`/`_ground_hits` new | receipt-only ground → frozen `sweeps[]` before/after probes with the admission gate |
| CITEDLINES | none | none |
| CENSUS | none | none |
| SCRATCHMIRROR | none | none |
| COLLCHECK | `_repointed_pairs` +25/-2 | map `url` only → also `staged_url_cell_urls`/`normalized_document_url` |
| FROZENCFG | `_frozencfg_compare` +74/-2, `leg_frozencfg` +15/-5 | compares the new frozen constants |
| INDEX | `leg_index` +51/-38 | `myth-symbol` + frozen vector `32/32/40/29/24/95` → partition derived from the entry paths, every heading vs its live count, footer vector vs the LIVE counts |

Mechanical/config functions changed for the same reason: `_cfg_candidates`,
`_cfg_int`, `_cfg_sweeps`, `_cfg_requoted` (new), `load_frozen_config`,
`print_receipt`, `main`, `_scratch_root`, `_forbidden_scratch`. Fixture half:
`build_fixture`, `_sfx_claims_text`, `_sfx_lesson`, `_sfx_ground`, `_sfx_map_text`,
`_sfx_readme_*`, `_sfx_entry_text`, `_sfx_evidence_files`, `_sfx_base_*`,
`_sfx_collision_files`, `_sfx_receipt`, `_sfx_guard_*`, `_selftest_scratch`,
`_str_scratch`, `run_selftest` (fixture ids, prefixes, 817-row base, 252-file
knowledge tree, 4 candidates, 3 rows, 2 admitted).

## Red-before for every changed read path (clean passes first)

`CASE clean: PASS -- PASS 13/13` is the positive fixture; each row below is the
mutant that reddens exactly that new read path (raw lines in
`selftest-receipt.txt`):

| changed read path | clean | red |
|---|---|---|
| threshold `n >= min_admitted` | `LEG PASS ENTRIES` | `mutant:candidate_extra_admitted` |
| a refused candidate must not land | `LEG PASS ENTRIES` | `mutant:candidate_refused_written` |
| `knowledge_before + n` | `LEG PASS ENTRIES` | `mutant:candidate_extra_admitted` |
| `rows_before -> rows_before+k` | `LEG PASS ROWS` | `mutant:row_extra` |
| one row per document (duplicate) | `LEG PASS ROWS` | `mutant:row_duplicate_document` |
| one row per document (base-held re-add) | `LEG PASS ROWS` | `mutant:row_document_at_base` |
| no tier-C sole support | `LEG PASS ROWS` | `mutant:tier_c_only_support` |
| `requoted[]` observability | `LEG PASS REPOINTED` | `mutant:requote_uncited` |
| campaign id vs already-held row | `LEG PASS REPOINTED` | `mutant:inline_staged`, `mutant:inline_unknown_row` |
| sweep before-state (absent at base) | `LEG PASS GROUND` | `mutant:ground_before_present` |
| sweep after-state (present when admitted) | `LEG PASS GROUND` | `mutant:ground_after_missing` |
| receipt declared → graded | `LEG PASS GROUND` | `mutant:ground_missing`, `mutant:ground_fragment_missing` |
| map schema tolerance | `LEG PASS COLLCHECK` (fixture map uses the real `staged_url_cell_urls` shape for 2 of 3 rows) | `mutant:coll_staged_missing` |
| every partition heading vs live count | `LEG PASS INDEX` | `mutant:index_heading_other`, `mutant:index_heading_stale` |
| footer vector vs live counts | `LEG PASS INDEX` | `mutant:index_footer_vector` |
| new frozen constants re-derived | `LEG PASS FROZENCFG` | `mutant:config_edited_at_lands`, `mutant:map_sha_mismatch` |

Second red-before (the counter is not vacuously green outside its own fixtures):
```
$ python3 -B accept-c.py --root . --lands 4f5e3b2535c2c06c51627dc2736c40183847cae1 \
      --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 --fleet-root /home/vgpnk/Projects/shokunin
REFUSED: cannot read reports/round-76/claims.json at freeze 5d0167464309: fatal: path '...' does not exist
ACCEPT-C-76: FAIL legs=0/13 (refused: ...)
exit=2
```
(receipt: `redbefore-r75-freeze-refusal.txt`.) A round-75 freeze cannot be graded
by the round-76 counter, and the refusal prints FAIL, never PASS.

## Draft claim object (`claim-C.json`) and schema deltas

`SCHEMA-DELTA.md` carries the full key table and the per-leg readings. The shape:

- `candidates[]` — the draft's four paths, each `admitted: true` in the plan,
  with the draft's campaign `cites` and document URLs;
  `min_admitted: 2`; `entries[]` = the same four paths (mutually consistent).
- `rows_before: 817`, `knowledge_before: 252`;
  `row_set[]` = S894 (S908/S935, ONE document), S895 (S916), S896 (S932),
  S897 (S938), S898 (S937) — k=5;
  `reused_rows: []` (S892/S885 are cited as already-held rows, not re-opened);
  `requoted: []`.
- `ground.sweeps[]` — four records: `GB/T 33661` gated by candidates a and d,
  `digital\.archives\.go\.jp` gated by candidates a and c, scope
  `corpus/knowledge`; `ground.fragments[]` = the five new-document fragments;
  `ground.receipt = reports/round-76/telemetry/gap-sweep.txt`.
- `rejects.counts = {adopted: 4, path_present: 9, refused: 27,
  total_staged_files: 40}` (sums to 40).
- `map.path = .ufo/waves/round-76/assimilation/id-renumber-map.json`,
  `map.sha256 = 13372a06662d4cef812440cb8302e35e8c448bfea14f0997de0fa7cee70130fc`
  (the current `ScoutIdMap` staged bytes — **provisional**, re-pin at the freeze).
- `legs[]` = the 13 frozen leg names with round-76 wording; `access_date`
  2026-10-27; `owned_inplace` = the `## culture-material/ (40)` → `(44)` heading.

The draft document was fed through the real loader in a throw-away repo under my
scratch (git init + one commit, `rev-parse --show-toplevel` asserted):
```
rows = ['S894','S895','S896','S897','S898']
entries = 4 admitted candidate basenames
min_admitted = 2; rows_before = 817; knowledge_before = 252
sweeps = 4 (GB/T 33661 x2, digital\.archives\.go\.jp x2) scope corpus/knowledge
fragments = 5; receipt = reports/round-76/telemetry/gap-sweep.txt
counts = {'adopted': 4, 'path_present': 9, 'refused': 27, 'total_staged_files': 40}
```
and `_repointed_pairs` on the real `id-renumber-map.json` returns `err: None`
with the 8 documented pairs (S908→S894, S935→S894, S916→S895, S932→S896,
S938→S897, S937→S898, S919→S892, S921→S885) and a URL for each.

## Findings (frozen text vs measured base)

**F1 — the draft's before-command scope is wrong (fails as written).**
```
$ git grep -l -E 'GB/T 33661' 98c486b -- corpus
98c486b...:corpus/lessons/round-68.md
98c486b...:corpus/lessons/round-69.md
$ git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus
98c486b...:corpus/lessons/round-68.md
```
Both print, i.e. exit `0`, not "nothing (exit 1)". Narrowed to knowledge ground
both are absent:
```
$ git grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge ; echo $?
1
$ git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus/knowledge ; echo $?
1
```
The draft claim therefore freezes `ground.sweeps[].scope = "corpus/knowledge"`,
and the claim's `before` sentence must name that scope. Root cause: the lane's
own lessons already discuss both instruments (round 68/69), so `corpus` is not
unheld ground.

**F2 — the round-76 by-document map has no `url` field.** The real map stores
`normalized_document_url` + `staged_url_cell_urls`; round-75's COLLCHECK read
`url` only and would have failed every record ("carries no url"). `_repointed_pairs`
now resolves `url` → `document_url` → `document` → first full URL in
`staged_url_cell_urls` → `normalized_document_url` (last resort), and the fixture
exercises both spellings.

**F3 — `map.sha256` is provisional.** `13372a06…` is the sha256 of
`w1/stage/ScoutIdMap/id-renumber-map.json` at write time
(`sha256sum id-renumber-map.json`). If that scout rewrites the map, the freeze
must re-pin and commit exactly those bytes.

## Measured base facts used by the draft

- `817` rows — `git show 98c486b:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`; last id `S893`.
- `252` knowledge `.md` files — `git ls-tree -r --name-only 98c486b corpus/knowledge | grep -c '\.md$'`; partitions `95/40/32/32/29/24` (civilizations/culture-material/linguistics/myth-symbol/synthesis/verification).
- `40` staged knowledge files — `find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge -name '*.md' | wc -l`.
- triage `4 / 9 / 27 = 40` — base-tree sha256 comparison per staged path: `same=0 diff=9 absent=31`; the four candidates are among the 31 absent, the 9 differing paths are the 3 round-75 narrative files + heritage 2 + worldbuilding 2 + conlang-scholarship 2.
- the five new-document fragments are absent from the base registry — `git show 98c486b:corpus/SOURCES.md | grep -c <fragment>` = `0` for `news.gmw.cn`, `digital.archives.go.jp/search`, `bzgk/std/newGbInfo`, `bzgk/std/showGb`, `xingzuobaike.com`.

## Unrun checks (explicit)

- The counter has **not** been run against a real round-76 `<freeze>`/`<lands>`:
  neither exists yet (the freeze is the L1's). Only the fixture lane and the
  loader-level draft validation above were exercised.
- `--selftest` was re-run AFTER the final `_scratch_root`/`_forbidden_scratch`
  TMPDIR edit: `exit=0`, `SELFTEST: 94/94`, `grep -nE '"/tmp|/tmp/' accept-c.py`
  still empty (exit 1). The verdict and the `sha256sum accept-c.py` in this report
  are the post-edit values, and `selftest-receipt.txt` is that run's raw output.
- `reports/round-76/telemetry/census-start.txt` (the frontier step's start census)
  is the L1's to produce; the CENSUS leg runs the fleet script at `<lands>`.
- `junk-fixtures.py` (QUALITY 25(b) J1–J3) is `ExecAdaptJunk`'s seat; not run here.
- `accept-ca-76` is `ExecAdaptCa`'s seat; not touched.

## Risks / blockers

- **R1** The frozen claim must state the triage triple and the refused-family
  rows consistently (counts.adopted == `len(entries)`; family rows sum to
  `refused`), or REJECTS goes red on a landing that is otherwise honest.
- **R2** `row_set` must be re-pinned if a scout finds two of the planned
  documents are one page (the draft's own S908+S935 collapse is already one row);
  k must stay `len(row_set)` and equal the distinct cited new documents.
- **R3** `map.sha256` (F3) and the map's committed bytes.
- **R4** The draft's `before` sentence must be re-scoped (F1) before the freeze,
  otherwise the claim ships a false negative statement.
- No installs (nothing installed, no package touched). Scratch
  `/fast/scratch/hyaku/kotodama-r76/ExecAdaptC` was deleted after copying the
  receipts above; no lane file, git index, jj state or fleet-root file was
  written.
