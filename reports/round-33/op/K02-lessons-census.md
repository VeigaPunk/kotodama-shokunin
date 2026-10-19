- Seat: K02 | scout (claim O, leg a) | lessons census: the 7 unindexed files and their row cells | date 2026-10-19 | baseline 139e3b6

# K02 — lessons census for the seven unindexed lesson files (round 26–32)

Input for O01 (row drafts) / O02 (README delta) / O04 (format checks) / O07 (baseline receipt).
All measurements are read-only, taken at `HEAD = 139e3b662900557afe54f632b468619593dc9fcb`
(`git rev-parse HEAD`, matching the declared `baseline_commit` in `reports/round-33/claims.json:8`).
No file was written by this seat except this fragment.

## 1. The audit re-run: the declared before-state reproduces exactly

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-25/audit/c31-lessons-index-audit.py
```

stdout, verbatim, exit **1**:

```
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
```

- **The seven unindexed files are confirmed and are exactly `round-26.md … round-32.md`** — no more, no fewer (C31-1 detail above).
- The reverse direction is clean: findings carry no `C31-2 ghost-row` and no `C31-3 duplicate-row`, so every one of the 26 index rows names a live file.
- `C34b` drift is stated `[26, 26]` vs measured `[26, 33]` — i.e. the README's own `**Rows: 26. Files: 26.**` (`corpus/lessons/README.md:97`) is the drifting prose, and the row count (26) is *not* drifting; only the file count is.
- `--selftest` → `SELFTEST OK: 28/28 checks passed`, exit **0**.
- Index bytes independently hashed: `sha256sum corpus/lessons/README.md` → `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`, 29059 bytes — identical to the tool's own `index_sha256` field (two routes, one value).

## 2. Per-file row cells — the six §2 columns, measured

Column contract is the README's own (`corpus/lessons/README.md:63-65`): **file · format (§3) ·
contract (`source:`/`verified-at:`/`recheck:`/`scope:` of 4) · open-questions carried (ids from §4) ·
disposition pointer · pin**.

| file | format | contract | open-questions carried | disposition pointer (proposed) | pin |
|---|---|---|---|---|---|
| `corpus/lessons/round-26.md` | gate-keeper | 4/4 | — (see §5) | `reports/round-26/validation.json` | bytes=60054 lines=222 sha8=cae06660 |
| `corpus/lessons/round-27.md` | gate-keeper | 4/4 | — (see §5) | `reports/round-27/validation.json` | bytes=54972 lines=203 sha8=f15e285b |
| `corpus/lessons/round-28.md` | gate-keeper | 4/4 | — (see §5) | `reports/round-28/validation.json` | bytes=50419 lines=145 sha8=dd832ff7 |
| `corpus/lessons/round-29.md` | gate-keeper | 3/4 (no `recheck:`) | — (see §5) | `reports/round-29/validation.json` | bytes=17847 lines=118 sha8=b6765d33 |
| `corpus/lessons/round-30.md` | gate-keeper | 3/4 (no `recheck:`) | Q-30-1..3 (+Q-30-4 resolved, Q-30-5 dispositioned) | `reports/round-30/routed-resolution.json` | bytes=30665 lines=181 sha8=56e77835 |
| `corpus/lessons/round-31.md` | gate-keeper | 4/4 | Q-31-1..4 | `reports/round-31/closure-ledger.json` | bytes=16637 lines=73 sha8=8870bbdd |
| `corpus/lessons/round-32.md` | gate-keeper | 4/4 | Q-32-1..6 | `reports/round-32/completion-ledger.json` | bytes=12879 lines=66 sha8=8aacfc2b |

Full digests for the same seven files (for a row that wants more than the sha8 cell):

| file | bytes | lines | sha256 |
|---|---|---|---|
| round-26.md | 60054 | 222 | `cae066608c27149f6476e6f75e3930cbc15f65f6c99af0fc1d34784c76e272e4` |
| round-27.md | 54972 | 203 | `f15e285b5a77c926b84ac520d301f2c8c0510e04b1692d6ff7fc1aad6b6f298b` |
| round-28.md | 50419 | 145 | `dd832ff71b267c75cb6fb05645ccebee6c5f9a4b81dbd5b9e58e251778aa7895` |
| round-29.md | 17847 | 118 | `b6765d33a7d50661093d4fcbe4d02fdae7abe95b93b105862f95f4e968f96383` |
| round-30.md | 30665 | 181 | `56e7783595920ac1cc0fb2792db4d73e76868ce3a2e119936f4794bb5bf2d59b` |
| round-31.md | 16637 | 73 | `8870bbdd4a4f29038af62b2e0a6a69506f000b467b8ef1009c5fcb92bc532625` |
| round-32.md | 12879 | 66 | `8aacfc2bd9f55ec9dae3a721dc793a83bf071e90b98955ffa2cb45a33437ab64` |

**Two independent measurement routes, agreeing byte for byte.** Route A: the §1 tool's own
census (`--json` → `live[]` rows, each `bytes`/`lines`/`sha8` recomputed from live bytes).
Route B: shell `wc -c`, `wc -l`, `sha256sum | cut -c1-8` on the same paths. Every cell above is
identical across A and B. (The tool's `C34` check would fail on drift, and it passes: `PASS
C34_pins_rederived`, `PASS C34c_shape_cells_rederived`.)

## 3. Format class — derivation per the §3 taxonomy

The §3 classifier (`reports/round-25/audit/c31-lessons-index-audit.py:47-78`) assigns
`fragment-index` if `^## Fragment index$` matches, else `gate-keeper` if `^## Gate$` matches,
else `plain`. Measured per file:

| file | `^## Gate$` | `^### Rule$` | `^## Fragment index$` | class |
|---|---|---|---|---|
| round-26.md | 1 (`:11`) | 1 (`:15`) | 0 | gate-keeper |
| round-27.md | 1 (`:11`) | 1 (`:15`) | 0 | gate-keeper |
| round-28.md | 1 (`:11`) | 1 (`:15`) | 0 | gate-keeper |
| round-29.md | 1 (`:9`) | 1 (`:13`) | 0 | gate-keeper |
| round-30.md | 1 (`:9`) | 1 (`:13`) | 0 | gate-keeper |
| round-31.md | 1 (`:11`) | 1 (`:15`) | 0 | gate-keeper |
| round-32.md | 1 (`:11`) | 1 (`:15`) | 0 | gate-keeper |

All seven are **gate-keeper**, and they are the *newer* sub-shape the §3 note already
accommodates (`corpus/lessons/README.md:119-122`: "rounds 21–23 carry the newer `### Rule` +
per-axis-section shape with no marker vocabulary. Both are counted as gate-keeper"). Measured
marker vocabulary across the seven: `Opening <axis> reading:` — **0 files** (the two `Opening`
hits in `round-32.md:51`/`:64` are prose, not a reading marker); `spot-check` — present in
round-26 (`:29`,`:155`,`:168`,`:172`), round-27 (`:194`), round-28 (`:126`), **absent in
round-29/30/31/32**; `Admitted`/`Rejected` line-anchored — 0 files. So r29–r32 are the
marker-*less* end of the sub-shape; the classifier still reads them gate-keeper because it keys
on the `## Gate` heading alone. Nothing here contradicts §3, but §3's prose (":116-118") states
the marker vocabulary as part of the gate-keeper definition and names only rounds 21–23 as the
marker-less precedent — **the integrator may want a sentence extending that precedent to
rounds 26–32** (flagged, not drafted here).

## 4. Contract column — derivation

Measured `contract_lines` (whole-file, line-anchored `^key:`, per the tool's `contract_lines()`
at `:81-89`), independently confirmed with `grep -c "^source:" / "^verified-at:" / "^recheck:" /
"^scope:"`:

| file | source | verified-at | recheck | scope | cell |
|---|---|---|---|---|---|
| round-26.md | 1 | 1 | 1 | 1 | **4/4** |
| round-27.md | 1 | 1 | 1 | 1 | **4/4** |
| round-28.md | 1 | 1 | 1 | 1 | **4/4** |
| round-29.md | 1 | 1 | **0** | 1 | **3/4** |
| round-30.md | 1 | 1 | **0** | 1 | **3/4** |
| round-31.md | 1 | 1 | 1 | 1 | **4/4** |
| round-32.md | 1 | 1 | 1 | 1 | **4/4** |

Round-29 and round-30 are the **round-16 outlier shape**: `source:` + `verified-at:` + `scope:`
and **no `recheck:`** (`corpus/lessons/round-16.md` is the filed precedent the README names at
`:140-142`). The other five join the 4/4 set. Live histogram over all 33 files: **4/4 = 13**,
**3/4 = 15**, **0/4 = 5** (README self-row + rounds 1–4); no file carries another count.

## 5. Open-question rows each lesson carries (each file's tail read)

Reading rule used: the ids the file itself declares in its own queue/ledger/open-routes section
at the tail. Measured result — **only rounds 30, 31, 32 declare `Q-<round>-n` ids of their own**;
rounds 26–29 carry their open legs as named prose sections with no ids:

| file | tail sections (line refs) | ids the file declares | notes |
|---|---|---|---|
| round-26.md | `## Closeout and rejected readings` `:170`; `## Status at the closing stamp` `:176`; `## Dated observations` `:194` | **none minted** (`Q-26-*` does not exist); **cites** `Q-02-1..4` (`:126`), `Q-14-1` (`:141`), `Q-04-1` + `Q-23-1..3` (`:163-164`) | `:206` carries "Three consequences the parent must carry" (red-is-not-a-defect; the r26 revision already declared 27/27; this seat's own write moved the readings and must be dispositioned as a new row or named delta). The cited ids are *existing* §4 rows referenced as superseded statuses, not new ids. |
| round-27.md | `## Closeout and rejected readings` `:139`; `## Dated observations` `:145`; `## Status at the closing stamp` `:163`; `## Boundary record` `:196` | **none** (`Q-27-*` does not exist) | `:194` "D — partially met, with **two named open legs**"; `:192` the receipt's D flip under an unchanged `runner_sha256`. |
| round-28.md | `### The lessons ledger …` `:82`; `## Closeout and rejected readings` `:92`; `## Addendum` `:135` | **none** (`Q-28-*` does not exist) | `:126` "D — met at the bytes, with **three named residues**"; `:139-143` the addendum items (a)(b)(c), including a new top-level failure class. |
| round-29.md | `## Closeout and rejected readings` `:101`; `## Boundary record` `:112` | **none** (`Q-29-*` does not exist) | `:110` "**C remains incomplete**" (six-versus-four calibration unresolved, provider launches unknown); `:116` known limits. |
| round-30.md | `## Open routes and boundary record` `:101`; `## Handoff cut` `:156`; `### Parent closeout actions` `:168` | **Q-30-1 `:103`, Q-30-2 `:104`, Q-30-3 `:105`, Q-30-4 `:115`, Q-30-5 `:142`** | Q-30-4 is **resolved** at `:138`; Q-30-5 is **dispositioned** at `:146`; `:173` keeps Q-30-1, Q-30-2, the remaining Q-30-3 limits visible. So the *live* carry is Q-30-1..3; Q-30-4/Q-30-5 are closed-at-source. |
| round-31.md | `## The lessons ledger …` `:51`; `## Open routes and boundary record` `:55`; `## Dated integration observation` `:64` | **Q-31-1 `:57`, Q-31-2 `:58`, Q-31-3 `:59`, Q-31-4 `:60`** | `:68` "Q-31-2 **narrows**" (denominator named; remainder routed to the validator seat). All four still open as of `:73`. |
| round-32.md | `## The lessons ledger at regimen close` `:43`; `## Open routes` `:53`; `## Boundary record` `:62` | **Q-32-1 `:55`, Q-32-2 `:56`, Q-32-3 `:57`, Q-32-4 `:58`, Q-32-5 `:59`, Q-32-6 `:60`** | Q-32-5 is *this census's own item* ("7 unindexed lessons (r26–r32); add parent-owned rows using the §Ledger pins") — it is what round 33's claim O leg (a) discharges. Q-32-6 transfers Q-31-2/Q-31-4 remainders. |

**Consequence the row drafters must decide (flagged, not decided here).** The §2 column says
"open-questions carried (**ids from §4**)" (`corpus/lessons/README.md:63-65`), and §4's table
currently ends at `Q-S1-1`
(`corpus/lessons/README.md:200`) — it holds **no** `Q-30-*`, `Q-31-*` or `Q-32-*` row. So a new row that cites
`Q-30-1..3` / `Q-31-1..4` / `Q-32-1..6` cites ids that have no §4 row, which breaks the §4
traceability rule at `corpus/lessons/README.md:227-232` ("anything above must be traceable to a lesson file"). Two
consistent options, both for O01/O02 (owner: parent):
(a) add §4 rows for the ids that are carried (Q-30-1..3, Q-31-1..4, Q-32-1..6 = **13 ids**,
each with an owner that resolves under `resolves()` at
`reports/round-25/audit/c31-lessons-index-audit.py:151-167`), then the §4 "Rows: **49**"
prose at `corpus/lessons/README.md:207` must be restated to the new count and the C34b queue check re-run; or
(b) keep the new rows' open-questions cell as prose pointers to the lesson's own queue section
and record the §4 gap explicitly. Option (a) is the only one that keeps C32 meaningful for the
new ids; option (b) leaves `Q-30..Q-32` unowned in the index. This seat measured the ids and
their owning sections; it does not choose.

## 6. Disposition pointers — proposed cells, existence-verified

The §2 column asks where the round's verdict lives, not for a verdict
(`corpus/lessons/README.md:247-250`). Proposed
pointers, each verified present by `test -f` at this stamp (sha8 of the pointer file given for
the record; the §2 cell itself carries no pointer pin):

| file | proposed pointer | exists | sha8 |
|---|---|---|---|
| round-26.md | `reports/round-26/validation.json` | yes | `99f2c3f3` |
| round-27.md | `reports/round-27/validation.json` | yes | `71783dc3` |
| round-28.md | `reports/round-28/validation.json` | yes | `ed8aa84c` |
| round-29.md | `reports/round-29/validation.json` | yes | `8b4396cd` |
| round-30.md | `reports/round-30/routed-resolution.json` (+ `reports/round-30/validation.json`) | yes / yes | `a16b41b8` / `6592378d` |
| round-31.md | `reports/round-31/closure-ledger.json` (+ `reports/round-31/final-sweep.md`) | yes / yes | `b9a66c2d` / `a32d9e2a` |
| round-32.md | `reports/round-32/completion-ledger.json` (+ `reports/round-32/final-dossier.md`) | yes / yes | `b90ed472` / `b82319b5` |

Two round-specific cautions the pointer cell should not hide, both from the lessons' own bytes:
round-27's receipt path served **two disagreeing receipts 98 s apart** with the same
`runner_sha256` field (`corpus/lessons/round-27.md:165-192`), and round-29's lesson records that
its runner and `validation.json` were still absent at its last inventory
(`corpus/lessons/round-29.md:110`) — a pointer to the filed receipt is correct but must not read
as a round verdict. Also relevant to leg (b) of claim O: the round-26 lesson's third consequence
(`corpus/lessons/round-26.md:206`) is a **filed falsifier-style leg** — "a consumer must re-run
X63 and C31 against the settled bytes once this file's bytes are final" — which is exactly the
instrument whose false-fire round 32 recorded as F-X16-3 / `Q-32-1`.

## 7. What must move in the README for C34b to go green (arithmetic, measured)

Not drafted here (O02 owns the delta); listed so the delta is complete and re-derivable:

| README location | current bytes | must become |
|---|---|---|
| `:97` | `**Rows: 26. Files: 26.**` | `**Rows: 33. Files: 33.**` (the C34b regex at `:299` reads exactly this pair; measured 26→33 files, 26→33 rows once 7 rows are added) |
| `:207` | `- Rows: **49**.` | the new §4 queue-row count **iff** option (a) in §5 is taken (49 + 13 = 62 if all thirteen new ids are carried); unchanged at 49 under option (b). The C34b queue regex at `:297` re-derives this number. |
| `:118` | gate-keeper `**14 files.**` | **21 files** (live histogram: gate-keeper 21) |
| `:124-125` | fragment-index `**5 files**` | unchanged (5) |
| `:126-132` | plain `**7 files.**` | unchanged (7 = rounds 1–4, 7, 16, README) |
| `:138-141` | "Histogram arithmetic: gate-keeper **14** … Total 26 = the runner's file set" | gate-keeper 21, total **33** |
| `:134-142` | "rounds 17–23 carry 4/4 and the rest — rounds 5 (both), 6, 7, 8, 9, 10, 11, 12, 14, 15 and the supplement — carry 3/4" | the 4/4 set adds rounds 26, 27, 28, 31, 32; the 3/4 set adds rounds 29, 30; the round-16 outlier sentence gains rounds 29–30 as the same shape. Measured totals: 4/4 = 13, 3/4 = 15, 0/4 = 5 (README + rounds 1–4). |
| `:83` | the `round-13` absence row | **preserve as-is**: it is a data row the row regex (`reports/round-25/audit/c31-lessons-index-audit.py:42`) does not count (it names no `corpus/lessons/…` path), and round-32's own ledger reading depends on that distinction (`corpus/lessons/round-32.md:45`: "26 naming `corpus/lessons/*.md` paths … plus the round-13 absence row"). |

## 8. Cross-checks

- **Round-32's own pins agree with this census, all six of them.** `corpus/lessons/round-32.md:45`
  records `bytes/lines/sha8` for rounds 26–31: `60054/222/cae06660`, `54972/203/f15e285b`,
  `50419/145/dd832ff7`, `17847/118/b6765d33`, `30665/181/56e77835`, `16637/73/8870bbdd`. My live
  re-measurement of the same six paths returns the identical six triples. This is an independent
  agreement between the r32 scribe's instrument and mine, not inheritance — the values above were
  produced from live bytes in this round.
- **Round-32's census arithmetic agrees on the set size.** `:45` states "6 filed lessons sit
  outside it — rounds 26–31 — and this file makes 7"; the §1 tool now reports exactly 7
  (C31-1). Round-32's `:45` also states the README "carries 27 data rows: 26 naming
  `corpus/lessons/*.md` paths … plus the round-13 absence row", which matches my read of the
  table (`corpus/lessons/README.md:69-95` = 26 path rows; `:83` = the absence row).
- **The sibling row-draft seat's cells agree with this census on all seven files.**
  `reports/round-33/op/O01-row-drafts.md:55-61` (the §2-shaped rows) and `:72-78` (its measurement
  table) carry the same seven `bytes/lines/sha8` triples, the same seven `gate-keeper` format
  cells and the same contract cells (4/4 for r26/27/28/31/32, 3/4 for r29/30) that §2/§4 above
  measure — two seats, two independent runs over the same live bytes. Its round-26 id enumeration
  (`Q-02-1..4`, `Q-14-1`, `Q-04-1`, `Q-23-1..3`) also matches mine, and I re-read
  `corpus/lessons/round-26.md:126` to confirm the `Q-02-1..4` range form is literal in the filed
  bytes. Where the two fragments differ it is a cell-convention choice, not a measurement
  disagreement: O01 lists round-30 as `Q-30-1..5` with the two closures parenthesised, while §5
  above reports the live carry as Q-30-1..3 with Q-30-4/Q-30-5 closed-at-source — both readings
  cite the same lines (`round-30.md:103-105,115,138,142,146,173`).
- **The seven files are the only partition delta since the index's last touch.** `git status
  --porcelain corpus/lessons/` is empty at this stamp (no uncommitted lesson bytes), and the
  index was last touched at `fc13cd2` (round 25) per `corpus/lessons/round-31.md:53` and
  `corpus/lessons/round-32.md:45`; `round-32.md` is the newest file in the partition
  (`ls corpus/lessons/`, 33 `*.md`).

## Known limits (this census)

- The "open-questions carried" column is a **reading of each lesson's own queue/ledger prose**,
  not a machine-verifiable extraction — the same limit the index names for itself
  (`corpus/lessons/README.md:298-301`). Rounds 26–29 declare no ids, so their carry is a
  judgement about which prose legs are open items; the line refs in §5 are the evidence, and
  O01/O02 own the cell wording. `to-verify` if a row draft claims an id these files do not
  declare.
- Whether round-30's Q-30-5 should appear as *carried* or *closed* in a new row is a reading of
  `round-30.md:142` against `:146`/`:173`; this census reports both states with line refs and
  does not pick.
- Pointer-file digests in §6 are at *this* stamp; a later write to any `reports/round-<N>/`
  artifact would move them, and the §2 pointer cell carries no pin by design.

## Owed

none — this mission named no dependency fragment. K01 (falsifier scout) is the other leg of
claim O and is not an input to this census; nothing here waits on it.

## Citations

Paths (line refs as used above):
- `corpus/lessons/README.md` — `:61-65` §2 columns, `:67` table header, `:69-95`
  26 path rows, `:83` round-13 absence row, `:97` `**Rows: 26. Files: 26.**`, `:111-142` §3
  (taxonomy `:116-132`, contract coverage `:134-142`), `:144` §4 heading, `:200` last queue row,
  `:202-232` queue arithmetic (`:207` `Rows: **49**`, `:227-232` traceability rule), `:247-250`
  disposition-pointer rule, `:298-301` known limit.
- `corpus/lessons/round-26.md` — `:11`,`:15` Gate/Rule; `:163-164` superseded statuses;
  `:170`,`:176`,`:194` tail sections; `:206` three consequences; contract lines `:3`,`:5`…
- `corpus/lessons/round-27.md` — `:11`,`:15`; `:139`,`:145`,`:163`,`:196`; `:192`,`:194`.
- `corpus/lessons/round-28.md` — `:11`,`:15`; `:82`,`:92`,`:126`,`:135`,`:139-143`.
- `corpus/lessons/round-29.md` — `:9`,`:13`; `:101`,`:110`,`:112`,`:116`.
- `corpus/lessons/round-30.md` — `:9`,`:13`; `:101-107`; `:103`,`:104`,`:105`,`:115`,`:138`,
  `:142`,`:146`; `:156`,`:168`,`:173`.
- `corpus/lessons/round-31.md` — `:11`,`:15`; `:51`,`:53`,`:55-62`; `:57-60`,`:68`,`:73`.
- `corpus/lessons/round-32.md` — `:11`,`:15`; `:43`,`:45`,`:49`,`:51`,`:53-60`,`:62`,`:66`.
- `corpus/lessons/round-16.md` — the 3/4-no-`recheck:` precedent named at README `:140-142`.
- `reports/round-25/audit/c31-lessons-index-audit.py` — `:42` ROW_RE, `:47-54` format markers,
  `:56` CONTRACT_LINES, `:81-89` contract_lines(), `:151-167` resolves(), `:293-317` C34b,
  `:337-432` selftest.
- `reports/round-33/claims.json:8` baseline commit; `reports/round-33/targets.json` seat K02.

Commands (all from repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1, stdout quoted in §1.
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json` → census rows in §2.
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → `SELFTEST OK: 28/28`.
- `sha256sum corpus/lessons/README.md; wc -c corpus/lessons/README.md` → `ec7469da…`, 29059.
- `for f in corpus/lessons/round-2{6..9}.md corpus/lessons/round-3{0..2}.md; do wc -c <$f; wc -l <$f; sha256sum $f; done`
- `grep -n "^#\{1,3\} " corpus/lessons/round-{26..32}.md`
- `grep -c "^source:" "^verified-at:" "^recheck:" "^scope:"` per file (contract column, §4).
- `grep -on "Q-[0-9S][0-9]*-[0-9]" corpus/lessons/round-{26..32}.md | sort -u` (ids per file, §5).
- `grep -n "Opening\|spot-check" corpus/lessons/round-{26..32}.md` (marker vocabulary, §3).
- `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`; `git status --porcelain corpus/lessons/` → empty.
- `test -f` + `sha256sum` over the pointer candidates in §6 (all `EXISTS`).
- `python3` histogram over the `--json` census: contract lengths `{0:5, 3:15, 4:13}`, formats
  `{gate-keeper:21, fragment-index:5, plain:7}`.
