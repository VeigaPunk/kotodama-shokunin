# ExecAdaptC — ACCEPT-C-77 (round 77, wave 1, BUILD seat)

Seat: `ExecAdaptC` (leaf). Assignment: adapt `reports/round-76/accept-c.py` into
`ACCEPT-C-77` under `.ufo/waves/round-77/w1/stage/ExecAdaptC/` for the round-77
claim C, with the six required changes and a `--selftest` that proves the
do-nothing controls and the J-series junk landings. No lane file was written;
nothing was committed. Only `stage/ExecAdaptC/**` and this report were created.

**Verdict: BUILT and GREEN — `SELFTEST: 37/37`, clean fixture `PASS legs=13/13`.**

**Mid-wave contract change, observed and followed.** `CLAIMS-DRAFT.md` was
rewritten at 22:33 (37 lines) after my first read: the C section now names the
13-leg lineage set — "Counter must preserve the lineage legs ENTRIES, ROWS,
REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR,
COLLCHECK, FROZENCFG, INDEX (13 unique); exactly one INDEX." The earlier
15-name draft (FROZENCFG, STAMP, LEDGELIST?, COUNTS, ENTRIES, ROWS, APPENDONLY,
COLLCHECK, INDEX, EVIDENCE, GATE, REJECTS, CENSUS, GROUND, RECEIPTS) is no
longer the contract. The counter now implements exactly the 13 names, in that
order, and the folded checks live inside them (STAMP→FROZENCFG+EVIDENCE,
COUNTS→ENTRIES+ROWS, APPENDONLY→ROWS' rule-2-cell rule, RECEIPTS→GROUND+CENSUS,
LEDGELIST→the LEGCOUNT refusal).

## Files written

| path (relative to the lane) | bytes / sha256 | what |
|---|---|---|
| `.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py` | 142196 B, `5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4` | the ACCEPT-C-77 counter (3303 lines, 110 functions) |
| `…/claims-C.skeleton.json` | `24e1d6dddf5b5227223a23203ec5add7a540bf4e1066ab4dda4dfcb0055cdceb` | the draft claim document, loadable as `reports/round-77/claims.json` |
| `…/SCHEMA-NOTE.md` | `a17b89f4c31656a5cce4a4342333cc282f36c07da0b5b2f636a3a3444dd9ccad` | per-key contract, per-leg readings, freeze choices |
| `…/diff-summary.md` | `5e9a907ee3d7b38b84c1cd3bbba97b5a03a580cc16b6f36b2416d9c2103b58ef` | r76→r77 diff summary (legs, constants, helpers) |
| `…/legs-generated.txt` | `a9b088bc88a4e45810d67a8b8df9d1000ba450d2c209ce3640896c9d33cac2f8` | `--emit-legs` JSON + one name per line |
| `…/selftest-receipt.txt` | `e622cb94b5d78ec23c254a9f909c3c04088796c318a0aad8150b26fd2c477abe` | raw `--selftest` output (37 cases) |
| `…/draft-skeleton-load.txt` (+ `.py`) | `3703d514…bb2d6` / `e368e0aa…ecea0f` | loader proof over the draft-shaped claim |
| `…/scratchmirror-real.txt` (+ `.py`) | `acce205e…ab06a3` / `bcc6745f…95f9fab` | SCRATCHMIRROR over the **real** r77 assimilation artifacts |
| `…/census-invocation.txt` | `cd0e757ff58796d13ffe77dd62d7de9104c1277a837db7bf2794552e24d15d5d` | the CENSUS invocation run on the full base tree |
| `…/scratch-probe.txt` (+ `.py`) | `a296d4f2…310837` / `1edf1399…76eb` | `/tmp` refusal + `--work` grading |
| `…/redbefore.txt` | `2d8d0719b6c8b89b4df97a85e905b908f25af40cf5cc9841318ad30daba888a8` | refusals: r76 freeze, unfrozen lane head |

`3303` lines — `wc -l accept-c.py`; `110` functions, `67` shared with r76, `43`
new, `110` dropped — `python3` + `ast.parse` over both files; `2420` added /
`5762` removed diff lines, 31 hunks — `diff -u reports/round-76/accept-c.py
accept-c.py | grep -c '^+' / '^-'`.

## The six required changes

| # | requirement | where |
|---|---|---|
| 1 | round constants 76→77; `row_set` per row `{lane_id, staged_id, document_url}` | `ROUND`, every `reports/round-77/**` path, lesson `round-77.md` (`BASE_LESSON` = `round-76.md`), `ACCEPT-C-77`; `_cfg_row_set` (r76 `{id, staged, document}` accepted as aliases). The loader reads the draft row_set as `row_staged: {'S897': ['S897'], 'S898': ['S903']}` — `draft-skeleton-load.txt`; the receipt prints it as `adopted rows: S897<-S897 S898<-S903` |
| 2 | ROWS counts only `| S### |` additions inside the frozen row_set; the required Paths/Search-log lines live in `required_sections[]` (target `corpus/SOURCES.md`) and are checked by INDEX | `leg_rows` (by-id additions; non-row added lines invisible), `_cfg_required_sections`, `leg_index`. Red case `index-required-section` fails INDEX and leaves ROWS PASS (receipt: `FAIL legs=12/13`, failing set `INDEX`) |
| 3 | COLLCHECK compares DOCUMENT identity, not raw strings | `_doc_url_key` (host without `www.`, percent-decoded path, archive wrapper folded) used by `leg_collcheck`, `leg_rows`, `leg_evidence`, `leg_gate`; `urls_compatible`/`_url_keys`/`_norm_path` deleted (their suffix/substring test called `/docs/beta-alias` compatible with `/docs/beta`). Cases: `collcheck-map-alias` red, `collcheck-archive-identity` green |
| 4 | frozen `legs[]` generated from the leg table, never hand-typed | `LEGS` tuple is the only list; `legs_generated()`; `--emit-legs`; `main()` refuses any frozen list that differs (duplicate, reorder, extra, missing) with exit 2 and `legs=0/13`. Independent check: the freeze checklist's `legcount.py --claim C --counter <file> --print counter` prints the same 13 names in order, exit 0 |
| 5 | honour `TMPDIR`/`--work`/`$HYAKU_SCRATCH`, no hardcoded `/tmp` | `_scratch_root`, `_forbidden_scratch` (`os.sep + "tmp"`). `grep -nE '/tmp' accept-c.py` → no output, exit 1. `scratch-probe.txt`: system tmp refused (exit 2, 0 LEG lines, no dir created), `--work` grades `PASS legs=13/13` |
| 6 | `--selftest` covers do-nothing, base refusal, J1/J2/J3, GREEN | 33 fixture cases + 2 leg-table cases; every graded case asserts an EXACT failing-leg set; the registry gains its `## Paths`/`## Search log` lines and ROWS stays green (`index-required-section` reddens INDEX only). Receipt: `SELFTEST: 37/37` |

## Leg table (13, draft order — generated)

```
ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS GROUND CITEDLINES CENSUS
SCRATCHMIRROR COLLCHECK FROZENCFG INDEX
```
`legs-generated.txt`; the freeze checklist's own tool agrees:
`python3 -B .ufo/waves/round-77/w1/stage/ExecFreezeChecklist/legcount.py --claim C
--counter <file> --print counter` prints the same names, exit 0.

## Selftest matrix (raw: `selftest-receipt.txt`)

| case | expecting | got (receipt line) |
|---|---|---|
| emit-legs / emit-legs-json | 13 names, no duplicate, prints the list | `PASS -- 13 name(s), no duplicate` |
| **clean** | all 13 PASS | `ACCEPT-C-77: PASS legs=13/13` |
| **do-nothing `lands == freeze`** | data legs red, structural legs green | `FAIL legs=3/13` — failing set exactly `CITEDLINES COLLCHECK ENTRIES EVIDENCE GATE GROUND INDEX REJECTS REPOINTED ROWS` (CENSUS, SCRATCHMIRROR, FROZENCFG green) |
| **`lands == base`** | refused exit 2, FAIL printed, no leg line | `FAIL legs=0/13 (refused: lands … is the frozen claim base …)`, exit 2 |
| **J1 stub entry** | ENTRIES only | `FAIL legs=12/13`, set `{ENTRIES}` |
| **J2 Gate quote absent** | GATE (+EVIDENCE) | `FAIL legs=11/13`, set `{EVIDENCE, GATE}` |
| **J3 shrunk claims.json at lands** | FROZENCFG only | `FAIL legs=12/13`, set `{FROZENCFG}` |
| row-extra / row-usedby-extra / pre-row-edit | ROWS only | `FAIL legs=12/13`, set `{ROWS}` |
| pre-row-rule2-cell (status/recheck/used-by edit) | allowed | `PASS legs=13/13` |
| collcheck-alias (frozen doc is a different route) | COLLCHECK (+EVIDENCE, GATE) | `FAIL legs=10/13`, set `{COLLCHECK, EVIDENCE, GATE}` |
| collcheck-prose-only | COLLCHECK (+REPOINTED, ROWS) | `FAIL legs=10/13`, set `{COLLCHECK, REPOINTED, ROWS}` |
| collcheck-map-alias | COLLCHECK only | `FAIL legs=12/13`, set `{COLLCHECK}` |
| collcheck-archive-identity (capture wrapper for the same document) | green | `PASS legs=13/13` |
| rowset-only-map-absent (no pinned map) | green | `PASS legs=13/13` |
| map-sha-mismatch | FROZENCFG only | `FAIL legs=12/13`, set `{FROZENCFG}` |
| index-footer / index-required-section (drops the appended registry Paths+Search-log lines) | INDEX only, ROWS green | `FAIL legs=12/13`, set `{INDEX}` |
| evidence-window-sha / evidence-stamp-wrong | EVIDENCE only | `FAIL legs=12/13`, set `{EVIDENCE}` |
| rejects-empty | REJECTS only | `FAIL legs=12/13`, set `{REJECTS}` |
| ground-before-present / ground-after-missing / ground-receipt-missing | GROUND only | `FAIL legs=12/13`, set `{GROUND}` |
| census-red | CENSUS only | `FAIL legs=12/13`, set `{CENSUS}` |
| counts-extra-knowledge | ENTRIES + INDEX | `FAIL legs=11/13`, set `{ENTRIES, INDEX}` |
| entry-missing | 6 legs | `FAIL legs=7/13`, set `{CITEDLINES, ENTRIES, GROUND, INDEX, REPOINTED, ROWS}` |
| repointed-legacy-id (entry keeps S886) | REPOINTED only | `FAIL legs=12/13`, set `{REPOINTED}` |
| repointed-source-no-url | REPOINTED only | `FAIL legs=12/13`, set `{REPOINTED}` |
| citedlines-multi (one line cites S004 and S005) | CITEDLINES only | `FAIL legs=12/13`, set `{CITEDLINES}` |
| scratchmirror-regids / -collisions-stale / -indent-guard | SCRATCHMIRROR only | `FAIL legs=12/13`, set `{SCRATCHMIRROR}` |
| scratchmirror-collision-recorded | green | `PASS legs=13/13` |
| legcount-duplicate | refused exit 2 | `FAIL legs=0/13 (refused: LEGCOUNT: the frozen claims.json repeats the leg name(s) INDEX; …)` |

`35` cases — `len(_ST_CASES)`; `5` all-pass, `2` refused, `28` graded; `37`
CASE lines including the two leg-table cases — `grep -c '^CASE ' selftest-receipt.txt`.

## Measured against the real artifacts (not fixtures)

**SCRATCHMIRROR on the lane's actual staging bytes** (`scratchmirror-real.txt`,
read-only: base `corpus/SOURCES.md` from `git archive` + a copy of
`.ufo/waves/round-77/assimilation/`):
```
LEG PASS SCRATCHMIRROR
     reg-ids=820 staged=132 collisions=38 planted=S897
```
i.e. reg-ids equals the 820 base ids, the staged universe is 132 ids and
contains both row_set staged ids (S897, S903), collisions equals
`reg-ids ∩ staged-ids` (38, re-derived — `comm -12` equivalent measured in
Python: `intersection size: 38 equal: True`), and the 1-3-space proof plants
exactly one row (S897) whose list matches while the 4-space proof detects
nothing.

**CENSUS invocation on the full base tree** (`census-invocation.txt`):
`sources-census.sh validate --file <base tree>/corpus/SOURCES.md --today
2026-10-27` → `exit=0`, 0 `E-code` lines, last line `file ok <…>/corpus/SOURCES.md`.

**Red-before** (`redbefore.txt`): a round-76 freeze cannot be graded —
`REFUSED: cannot read reports/round-77/claims.json at freeze df0f0309d61e …
ACCEPT-C-77: FAIL legs=0/13`, exit 2; the same for the unfrozen lane head
`211f9526`. The counter is not vacuously green.

**Draft-shaped claim loads** (`draft-skeleton-load.txt`): rows `['S897','S898']`,
staged `{'S897': ['S897'], 'S898': ['S903']}`, entries 1, counts 820/253,
`required_sections` `[('Paths',1,…),('Search log',1,…)]`, sweeps
`lishisuo\.cssn\.cn` / `onomastica\.ijppan` over `corpus/knowledge`, refused
staged `S933,S934,S936,S939-S944`, removed ids `S886,S888-S891,S896`,
`frozen_legs == generated: True (13)`, and the D1 Wayback capture folds to the
live document (`same page capture folds to the live document: True`).

**Base facts used by the fixtures/contract** (measured, this seat):
`820` rows — `git show 211f9526:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`;
`253` knowledge `.md` — `git ls-tree -r --name-only 211f9526 corpus/knowledge | grep -c '\.md$'`;
smallest base entry `478` words — `git archive 211f9526 corpus/knowledge | tar -x`
then `find … -name '*.md' -print0 | xargs -0 wc -w | sort -n | head -1`.

## Findings for the L1

1. **Leg set changed under the wave.** The 22:33 draft is authoritative and
   names the 13 lineage legs; the counter implements exactly those. The freeze
   checklist's `legcount.py` and the C harness (`C_GREEN=FROZENCFG`) were told
   and agree. `STAMP`, `LEDGELIST`, `COUNTS`, `APPENDONLY`, `RECEIPTS` are no
   longer leg names; a frozen `legs[]` containing them is refused by LEGCOUNT.
2. **A frozen `legs[]` mismatch is now a refusal, not a graded leg** (the r76
   shape): `ACCEPT-C-77: FAIL legs=0/13`, exit 2, no LEG line. The counter
   prints its generated list in the receipt and via `--emit-legs`.
3. **REPOINTED carries the rewrite clause**: one id per `source:` line, the
   line's URL must be that row's document, every inline id must resolve, and
   the draft's legacy ids (config `removed_ids`) must be gone. This is the only
   guard against a landed entry that keeps S886/S888/S889/S890/S891/S896.
4. **CITEDLINES** runs the *committed* `tools/check-cited-lines.py` over the
   entry; the fixture uses a stand-in with the same contract, so a landing's
   real tool is what runs at the freeze.
5. **D2 locator note (from KotodamaR77 / ScribeLesson R77-M16)**: the counter
   does not grade locator prose; the Gate quote is graded against the committed
   evidence window. The "PDF p.4 / journal p.114 with attribution" wording is a
   lesson/evidence-producer obligation, recorded here so it is not lost.
6. **Scratch asymmetry** with the harness: claim Ca's draft requires a
   missing-`--work` refusal; claim C's does not, and the r76 C counter (the
   pattern) resolved an operator default. My `_scratch_root` keeps that shape
   and never invents the system temp dir; `ExecGapSweep` bound control 3 to
   claim Ca by default after this exchange (`--scratch-refusal ca`), so no
   change is needed on either side.

## Risks

- **R1 `required_sections[]` must be frozen.** The loader refuses an absent or
  empty list (r76 defect 1's fix is config-driven); the required non-row edits
  are the `## Paths` bullet and the `## Search log` entry **in
  `corpus/SOURCES.md`** (the r76 landing appended exactly such lines, and r76's
  ROWS wrongly failed them). The skeleton's patterns key on S897/S898 and the
  round-77 phrase; pin them to the literal appended text at the freeze.
- **R2 refusal ids must match the Gate.** Every S-id in the `rejects` prose is
  required in the Gate reject table; ids that are only *held* (S906/S907/S911)
  or merely recounted must stay out of the refusal keys or the Gate owes them a
  row.
- **R3 evidence stamps.** EVIDENCE requires `claims-source` naming `<freeze>`
  and `claims-frozen: yes` (r76 producer emitted both); a producer that omits
  them fails the leg on an otherwise good capture.
- **R4 same-page capture.** ROWS requires a live URL **and** a
  `web.archive.org/web/<ts>id_/<original>` capture folding to the same document
  (QUALITY 18); a row with only the live URL fails.
- **R5 rule-2 exemption.** ROWS tolerates status/recheck/used-by edits on
  pre-existing rows (the kill rule's own wording); any other pre-existing-row
  change fails there, not in claim Ca.
- **R6 no real freeze/lands exists yet**, so no graded run of the real claim
  has been made by this seat.

## Unrun checks (explicit)

- No run against a real round-77 `<freeze>`/`<lands>`: neither exists.
- CENSUS is exercised in the selftest against a stub fleet script; the real
  script was run only against the base tree (`census-invocation.txt`), not a
  landing.
- EVIDENCE/GATE/ROWS/REPOINTED are exercised only on fixtures: the real entry,
  evidence captures and Gate do not exist at this wave.
- `junk-fixtures.py` (the J-series driver) is `ExecAdaptJunk`'s seat; my J1/J2/J3
  cases are the counter's own in-process fixtures, not that driver's output.
- `accept-ca-77` is `ExecAdaptCa`'s seat; untouched.

## Installs

None. No package, tool or system file was installed, upgraded or removed.

## Scratch

All scratch lived under `/fast/scratch/hyaku/kotodama-r77/ExecAdaptC` and was
deleted after the receipts above were copied into the stage dir. No lane file,
git index, jj state, fleet-root file, `scripts/`, `templates/`, `.ufo/state`,
`.ufo/watchdog.log`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`,
`corpus/**`, `reports/round-76/**`, `reports/round-77/**` or `shokuknow` path
was written.
