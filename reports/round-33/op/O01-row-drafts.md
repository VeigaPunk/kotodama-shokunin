- Seat: O01 | executor | claim O | date 2026-10-19 | baseline 139e3b6

# O01 — lessons-index row drafts (one row per unindexed file, round-26..32.md)

## 0. What this is, and the one substitution made

Claim O leg (a) requires the lessons README index to carry one row per
`corpus/lessons/*.md` file (33/33) with cells re-measured from live bytes. This
fragment is the **row draft** for the seven unindexed files. It is a draft for
integrator application: no filed byte was edited by this seat.

**Substitution, declared.** The mission says the cells must match *K02's
measurements*. `reports/round-33/op/K02-lessons-census.md` **does not exist at
this seat's write time** (`ls reports/round-33/op/` → empty). Per the
missing-dependency rule this seat measured the partition itself with the round-25
tool of record and with raw byte reads, and records the K02 cross-check as owed.
The measurements below are live-command derived, not inherited from any round-33
fragment.

## 1. Before-state (reproduces the declared baseline)

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py
index present: True
lesson files:  33
index rows:    26
queue rows:    49
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  FAIL C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  FAIL C34b_prose_arithmetic
findings:      2
  C31-1 unindexed-file: ['round-26.md', 'round-27.md', 'round-28.md', 'round-29.md', 'round-30.md', 'round-31.md', 'round-32.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26], 'measured': [26, 33]}}
exit=1
```

Index bytes measured this stamp: `corpus/lessons/README.md` sha256
`ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c` (29 059 B,
346 lines) — identical to the `index_sha256` the tool prints in its `--json`
receipt, so the row set below is drafted against the bytes the tool graded.

## 2. The seven rows (copy verbatim)

Insertion point: **after the `round-25.md` row, `corpus/lessons/README.md:94`**,
before the `supplement-opencode-1.md` row at `:95`. Column order and cell shapes
match the existing rows (`file | format | contract | open-questions carried |
disposition pointer | pin`).

```
| `corpus/lessons/round-26.md` | gate-keeper | 4/4 | — (no new ids; cites Q-02-1..4, Q-04-1, Q-14-1, Q-23-1..3) | `reports/round-26/validation.json` (lesson read `false` at 18:28:22Z; live receipt `true`, measured 19:09:32Z) | bytes=60054 lines=222 sha8=cae06660 |
| `corpus/lessons/round-27.md` | gate-keeper | 4/4 | — (no queue ids; open legs `L6b-HOLD` and the syllabify witness are round-claim states, §Closeout) | `reports/round-27/validation.json` (lesson read two receipts 98 s apart, D flipped, both `false`; live `true`, 20:08:49Z) | bytes=54972 lines=203 sha8=f15e285b |
| `corpus/lessons/round-28.md` | gate-keeper | 4/4 | — (no queue ids; residues `L9-HOLD`, `L10-HOLD` and the four silent semantic tampers, §Closeout) | `reports/round-28/validation.json` (live `true`, measured 20:50:17Z) | bytes=50419 lines=145 sha8=dd832ff7 |
| `corpus/lessons/round-29.md` | gate-keeper | 3/4 | — (no queue ids; carried items are the scoped C/O/A remainders, §Closeout) | `reports/round-29/validation.json` (absent at the lesson's 21:13:09Z read; live `true`, 21:50:07Z) | bytes=17847 lines=118 sha8=b6765d33 |
| `corpus/lessons/round-30.md` | gate-keeper | 3/4 | Q-30-1..5 (Q-30-4 resolved at the two readers; Q-30-5 attribution defect corrected in the current retrospective) | `reports/round-30/validation.json` (lesson read `false` at 21:56:22Z; live `true`, 22:32:36Z); `reports/round-30/routed-resolution.json` | bytes=30665 lines=181 sha8=56e77835 |
| `corpus/lessons/round-31.md` | gate-keeper | 4/4 | Q-31-1..4 | `reports/round-31/validation.json` (live `true`, 00:28:05Z), `reports/round-31/closure-ledger.json` | bytes=16637 lines=73 sha8=8870bbdd |
| `corpus/lessons/round-32.md` | gate-keeper | 4/4 | Q-32-1..6 | `reports/round-32/validation.json` (live `true`, 00:59:27Z) | bytes=12879 lines=66 sha8=8aacfc2b |
```

## 3. Cell provenance, per row

Measured `2026-10-19` by `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json`
(`.scratch/o01-c31.json`), whose `live[]` block carries `bytes`, `lines`, `sha8`,
`format` (its own `classify()`) and `contract_lines` per file:

| file | bytes | lines | sha8 | format | contract_lines | open-questions basis |
|---|---|---|---|---|---|---|
| round-26.md | 60054 | 222 | cae06660 | gate-keeper | source:/verified-at:/recheck:/scope: | `round-26.md:126` (Q-02-1..4 twins), `:141` (Q-14-1), `:163-164` (Q-04-1, Q-23-1..3) |
| round-27.md | 54972 | 203 | f15e285b | gate-keeper | 4/4 | none minted or cited (`grep -no 'Q-[A-Za-z0-9]*-[0-9]*'` → no hits) |
| round-28.md | 50419 | 145 | dd832ff7 | gate-keeper | 4/4 | none minted or cited |
| round-29.md | 17847 | 118 | b6765d33 | gate-keeper | source:/verified-at:/scope: | none minted or cited |
| round-30.md | 30665 | 181 | 56e77835 | gate-keeper | source:/verified-at:/scope: | `round-30.md:103-105` (Q-30-1..3), `:115` (Q-30-4), `:142` (Q-30-5) |
| round-31.md | 16637 | 73 | 8870bbdd | gate-keeper | 4/4 | `round-31.md:57-60` (Q-31-1..4) |
| round-32.md | 12879 | 66 | 8aacfc2b | gate-keeper | 4/4 | `round-32.md:55-60` (Q-32-1..6) |

Two notes a reader must not misread:

- **`3/4` on r29/r30 means the file carries no `recheck:` line** (the tool's
  `contract_lines` returns `['source:', 'verified-at:', 'scope:']` for both). The
  index's §3 prose currently explains `3/4` as the pre-round-17 class plus the
  round-16 outlier; r29 and r30 are **new members of that class**, not a format
  regression. The cell must stay `3/4` — the tool's C34c compares it literally
  against `len(contract_lines)`.
- **All seven classify `gate-keeper`** (each carries an exact `## Gate` heading;
  none carries `## Fragment index`). The format cell is not a judgment call.

## 4. Independent agreement on six of seven pins

`corpus/lessons/round-32.md:45` — a **filed** lesson, written before this seat
ran — pins the same six files at the same values:

```
round-26 60054/222/cae06660; round-27 54972/203/f15e285b; round-28 50419/145/dd832ff7;
round-29 17847/118/b6765d33; round-30 30665/181/56e77835; round-31 16637/73/8870bbdd
```

This seat's live reads agree on all six (two routes: this seat's `sha256sum` +
`wc` loop, and the round-25 tool's `census()`). `round-32.md` is pinned only by
the live read — no filed artifact pins it.

One conflicting in-lesson pin is named rather than smoothed over:
`corpus/lessons/round-28.md:141` records this file's own post-write state as
`47 324 B, 135 lines` (sha256 `cb24a24e…`). Live bytes are `50 419 B, 145 lines`
(`dd832ff7…`). The file's own words explain the difference — the section carrying
that pin was "**Appended** rather than rewritten, per this file's own closing
rule", so later dated sections landed after the pin was taken. The row cell uses
the live measurement; the earlier pin stays true of the earlier revision.

## 5. Arithmetic and prose consequences (routed to O02, not duplicated here)

Applying these seven rows moves the measured state to **33 rows / 33 files**
(`formats {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}`). The README
bytes that must change with them are O02's delta, listed here only so the two
fragments cannot drift apart:

- `:97` `**Rows: 26. Files: 26.**` → `33 / 33` (the tool's C34b reads exactly
  this regex; a stale stated count keeps C34b red after the rows land).
- `:1-9` the opening census paragraph (states 26 rows, "three census formats").
- §3 histograms at `:118-127` (gate-keeper 14, fragment-index 5, plain 7, total 26)
  and the contract-coverage sentence at `:134-140` (must absorb the new `4/4`
  members r26/r27/r28/r31/r32 and the new `3/4` members r29/r30).
- §4 must gain queue rows for the ids these lessons carry: **Q-30-1..5,
  Q-31-1..4, Q-32-1..6** (15 ids), or an explicit routing note. Until those rows
  exist, §4's own rule ("anything a lesson names as *open* must appear above with
  an owner") is unmet for r30–r32 — C32 does not fire on absent rows, so this is
  a coverage gap the tool cannot see. O03 owns the owner-resolution verdicts for
  the new rows.
- §2's composition sentence at `:97-104` (which currently explains "Round 24 has
  no lesson file", the round-5 double row, round-13's absence) needs the r26–r32
  sentence: seven rows added, each naming a filed round lesson whose round is
  admitted in `LOG.md` (r26 `:3375`, r27 `:3388`, r28 `:3398`, r29 `:3411`,
  r30 `:3422`, r31 `:3470`, r32 `:3485`).

## 6. Self-check run against these drafts

This seat verified the draft rows mechanically before filing. The checker
`runpy`-loads `reports/round-25/audit/c31-lessons-index-audit.py`, takes the
**second** fenced block of this file (the §2 rows), parses each line with that
module's own `ROW_RE`, and compares every `bytes/lines/sha8` cell (`CELL_RE`),
`format` cell (`classify()`) and `contract` cell (`len(contract_lines())/4`)
against `census()` over the live partition. Run 2026-10-19, verbatim output:

```
fence count: 3
rows parsed: 7
pin 7/7  format 7/7  contract 7/7  trailing-pipe 7/7  ghosts []
SELFTEST OK
```

The same run re-derived the carried ids from the lesson bytes:
`round-30.md → Q-30-1..5`, `round-31.md → Q-31-1..4`, `round-32.md → Q-32-1..6`
(15 ids, exactly as the rows state), and `round-26/27/28/29` mint or cite none
beyond the §3 table. A first checker run read the **first** fence (§1's shell
block) and reported `rows parsed: 0` — the block-index bug was in the checker,
not in the drafts, and is recorded here so a re-runner does not repeat it.

This is a check of the *draft* against the tree at this stamp. It cannot prove
the applied README is correct — the integrator's post-edit check remains the tool
itself (`## Owed`), and a lesson landing after this stamp moves the pins.

## 7. Boundary

This seat wrote `reports/round-33/op/O01-row-drafts.md` and one scratch file
(`.scratch/o01-c31.json`, gitignored) only. No `corpus/lessons/*.md` byte, no
`corpus/lessons/README.md` byte, no filed round artifact, no tool and no gate was
written. No commit, no push, no network. The README edits in §2/§5 are drafts;
applying them is the integrator's act, not this seat's.

## Owed

- `reports/round-33/op/K02-lessons-census.md` — **the cell cross-check**. K02 was
  absent at this seat's write time, so the cells above are this seat's live
  measurements. When K02 lands, the integrator must diff K02's per-file
  `bytes/lines/sha8/format/contract` cells against §3 of this fragment; any
  disagreement is a K02-vs-O01 finding and the **live re-measurement at
  application time wins**, because a lesson landing after either stamp moves the
  bytes.
- `reports/round-33/op/O04-format-checks.md` — the C33 leg over these seven
  files (this fragment supplies measured classes, not the taxonomy audit).
- `reports/round-33/op/O03-owner-checks.md` — C32 verdicts for the new §4 rows
  named in §5 (Q-30-1..5, Q-31-1..4, Q-32-1..6); the ids exist in the lesson
  bytes but not yet in §4.

## Citations

- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (2026-10-19) —
  output quoted in §1, exit 1, findings C31-1 + C34-2, `index_sha256
  ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`.
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json >
  .scratch/o01-c31.json` — the `live[]` block is the source of every pin/format/
  contract cell in §3.
- `for f in corpus/lessons/round-2[6-9].md corpus/lessons/round-3[0-2].md; do
  wc -c; wc -l; sha256sum | cut -c1-8; grep -c '^## Gate$'; done` (2026-10-19) —
  the independent second route; agrees with the tool on all 21 values.
- `reports/round-25/audit/c31-lessons-index-audit.py:42-56` (ROW_RE, CELL_RE,
  FORMAT_MARKERS, CONTRACT_LINES), `:72-89` (classify, contract_lines), `:271-291`
  (C34c shape-cell comparison), `:296-317` (C34b prose arithmetic).
- `corpus/lessons/README.md:67-95` (existing row format and insertion point),
  `:94` (round-25 row), `:95` (supplement row), `:97` (stated `Rows: 26. Files:
  26.`), `:111-142` (§3 formats and histograms), `:202-232` (§4 queue arithmetic).
- `corpus/lessons/round-26.md:126,141,163-164` (ids cited); `round-30.md:103-105,
  115,142` (Q-30-1..5); `round-31.md:53,57-60` (Q-31-1..4); `round-32.md:45`
  (the six-file pin table), `:55-60` (Q-32-1..6), `:43-47` (ledger debt).
- `corpus/lessons/round-28.md:139-141` (the `47 324 B, 135 lines` self-pin and
  the "appended rather than rewritten" wording).
- `reports/round-{26,27,28,29,30,31,32}/validation.json` — existence and
  `acceptance_checks_passed` / `measured_at_utc` read for the disposition-pointer
  cells; sha256 prefixes `99f2c3f3`, `71783dc3`, `ed8aa84c`, `8b4396cd`,
  `6592378d`, `8ba960e4`, `204dfdda` (first 8 hex each).
- `LOG.md:3375,3388,3398,3411,3422,3470,3485` — the r26–r32 admission rows.
- `ls reports/round-33/op/` → empty (2026-10-19) — K02 absent, §0 substitution.
- Self-check command (run 2026-10-19): a stdlib-only script that imports
  `reports/round-25/audit/c31-lessons-index-audit.py` via `runpy`, re-reads the
  §2 fenced block with that module's `ROW_RE`/`CELL_RE`, and compares cells to
  `census()` — output `rows parsed: 7` / `pin 7/7  format 7/7  contract 7/7
  trailing-pipe 7/7  ghosts []` / `SELFTEST OK`; full text in §6.
- `python3 -B -c` id census over the lesson bytes (2026-10-19): `round-30.md`
  Q-30-1..5, `round-31.md` Q-31-1..4, `round-32.md` Q-32-1..6 — 15 ids, matching
  the rows' open-questions cells.
- `grep -n -i 'promotion\|canon\|clearance\|closed\|closure' reports/round-33/op/O01-row-drafts.md`
  (2026-10-19) → one hit, `:60`, the path `reports/round-31/closure-ledger.json`
  (a routed reference to a filed artifact, not a verdict claim).
