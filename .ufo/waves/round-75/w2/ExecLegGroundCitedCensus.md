# ExecLegGroundCitedCensus — round-75 claim C, legs GROUND / CITEDLINES / CENSUS

Seat: executor (leaf, no delegation, no background jobs, no `task` spawns). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` at base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Round-75 `claims.json` and `ledger.json` were
read and never edited; no lane file outside this wave dir and this report was written; no
git/jj state touched (read-only `git show`/`clone --shared` only); the fleet repo, `scripts/`,
`templates/`, `.ufo/state`, other lanes and `shokuknow/` were not written. No tool was
installed or upgraded (nothing needed: `git`, `python3`, `gawk` via the fleet census script,
`tar` already present); no `pacman`. Scratch
`/fast/scratch/hyaku/kotodama-r75/ExecLegGroundCitedCensus/` was created for the mock and
deleted before yield.

## 1. Deliverable

| file | bytes | lines | sha256 |
|---|---|---|---|
| `.ufo/waves/round-75/w2/parts/leg-ground-cited-census.py` | 7724 | 170 | `1391d0698bd3b15e4abbb1d4649288b3a7a0172019249a4c66315461026acec8` |

Functions defined (nothing else; no top-level code, no imports): `leg_ground`,
`leg_citedlines`, `leg_census`, and the two private helpers
`_ground_cited_census_has_zero`, `_ground_cited_census_ecodes` (helper prefix is the
file's leg stem with hyphens turned into underscores, since `-` is not an identifier
character). Shared helpers are only called, never redefined: `read_tree`, `parse_rows`,
`urls_in`, `dedupe`, `leg`, `Missing`, `REGISTRY`, `GROUND_RECEIPT` from PART A.
`python3 -B -m py_compile` is clean for the part alone and for PART A + every part file
landed so far in contract order (`206539` bytes, `compile()` OK); no identifier of mine
collides with a sibling part (`grep -n 'def leg_ground\|def leg_citedlines\|def leg_census\|_ground_cited_census_' *.py`
returns only my file).

## 2. The frozen wording, as I read it

From `reports/round-75/claims.json`, claim C `legs[]` (DRAFT, not frozen, wording treated as
final for this wave):

- **GROUND**: "reports/round-75/telemetry/gap-sweep.txt names the 808-row registry and 0
  matches per fragment at base; the counter independently re-derives 0 at base".
- **CITEDLINES**: "tools/check-cited-lines.py over the entries from the materialized tree
  prints 'CITED-LINES: 0 finding(s)'".
- **CENSUS**: "sources-census.sh validate against the materialized registry exits 0 with no
  ^E[0-9][0-9] line".

### 2.1 Implementation per leg

**GROUND** — the receipt is read from `mat` (committed bytes at `<lands>`); the base count and
the per-fragment zeros are re-derived from `mat_base`, which the counter materialized itself,
so the receipt cannot vouch for itself. Checks: (a) the receipt names an `N-row` registry and
`N == len(parse_rows(base_registry))` (808 at this base); (b) every `cfg["fragments"]` entry is
named by the receipt and carries a standalone `0`; (c) no fragment occurs in the base registry
text (case-insensitive) — the independent re-derivation of the claim's "0 rows per fragment at
base".

**CITEDLINES** — `<mat>/tools/check-cited-lines.py` (the materialized tree's own copy) is run
under `sys.executable -B` over exactly the `cfg["entries"]` paths that exist; the leg passes
only when the tool exits `0` **and** stdout contains `CITED-LINES: 0 finding(s)`. A missing
entry is a FAIL with the path named, never a silently shorter run.

**CENSUS** — `<fleet_root>/scripts/sources-census.sh validate --file
<mat>/corpus/SOURCES.md --today <cfg.access_date>` must exit `0` with no E-code finding. No
lane-directory-name materialization is needed: `--file` derives its root as the parent of
`corpus/` (`sources-census.sh:497-502`), i.e. the same `git archive` tree, so every row's
`used-by` path is resolved against the graded tree (E11 stays live and meaningful); `--root`
would instead have required symlinking `<mat>` under a lane name a fleet `shokunin.conf`
knows, which would grade through a path the counter did not build. `--today` is the frozen
`access_date` (`2026-10-27`), so the E08 open-date check is deterministic instead of depending
on wall-clock.

### 2.2 Ambiguities and how each was resolved

| # | Ambiguity in the frozen text | Reading taken | Why |
|---|---|---|---|
| A1 | GROUND names "0 matches **per fragment**", while `ground.terms` (`narrative structure`, `narratology`) also exists in the claim's config | `terms` is **not** graded by GROUND: only `cfg["fragments"]` is. The leg may be neither stronger nor weaker than its wording, and the wording names fragments only | The assign prompt says the same ("0 matches per frozen fragment"); `terms` remains available to whatever leg the frozen text gives it |
| A2 | "0 matches per fragment" — may a single global "0 matches" over a list of fragments satisfy it? | No: the `0` must belong to that fragment's own receipt entry (its line, plus continuation lines up to a blank line or the next fragment's line) | Otherwise a decorative zero anywhere nearby satisfies the leg; a global total is exactly the false-green shape the w1 critic named. Mutant `g5` pins this reading |
| A3 | The fragment string itself contains digits (`_0588`, `_1113`); a naive "0 nearby" search could be satisfied by them | The fragment strings are stripped from the window before the `0` token is looked for, and `0` must be a standalone token (`808`, `10`, `0x` never match) | Keeps the check on the count column only |
| A4 | CENSUS: "no `^E[0-9][0-9]` line" — but the script emits TSV `<lane>\t<E-code>\t...`, so the literal anchored pattern can never match its own output (verified: a failing run prints `file\tE01\tS894 fields=10`) | The field form `(?:^\|\t)(E\d\d)(?=\t\|$)` is used, which also still matches a bare `E01` line; the exit status remains the load-bearing check (the script exits 1 on any E finding) | Literal-only would make the clause dead text; the field form implements the wording's meaning (no E-code finding line). Tested on `file\tE01\t…`, bare `E11\t…`, warning-only `W04` (no match) and `WE01` (no match) |
| A5 | CENSUS: "against the materialized registry" — `--file` or `--root`? | `--file <mat>/corpus/SOURCES.md` | Documented in 2.1; keeps one graded tree and no fleet-root lane layout |
| A6 | CITEDLINES: which `check-cited-lines.py`? The frozen text says "from the materialized tree"; the w1 critic proposed pinning its blob to `<freeze>` | The tool at `<lands>` is run, exactly as written; **no** freeze-blob pin is added | Pinning would be stronger than the frozen text. Recorded as residual risk (§7), not silently implemented |
| A7 | CENSUS's `--today` is unstated; `cfg` carries `access_date` | Frozen `access_date` is passed | Deterministic grading; matches r74 and the claim's own access date |
| A8 | GROUND's "the 808-row registry": literal 808 or the base's actual row count? | Compared against `len(parse_rows(mat_base registry))`, which is 808 at this frozen base | Same value today; derived so the leg follows the frozen base rather than a hard-coded number that could drift from it |

## 3. Test method (real, not asserted)

Scratch `/fast/scratch/hyaku/kotodama-r75/ExecLegGroundCitedCensus/`:

1. `git clone --shared` of the lane → `lane/`, `git -C lane checkout --detach
   f556d104…`; asserted `git -C lane rev-parse --show-toplevel` equals the clone dir before the
   first commit; commits used a throwaway identity passed as `-c user.name=mock -c
   user.email=mock@example.invalid` (repo config untouched).
2. `git archive <base> | tar -x` → `mock-base/` (the `mat_base` input).
3. Mock **lands**: the three unlanded drafts
   (`.ufo/waves/round-75/drafts/narrative-structure-frameworks*.md`) copied to
   `corpus/knowledge/myth-symbol/`; nine synthetic rows `S885`..`S893` (11 cells, `mined`,
   `opened 2026-10-27`, `180d`, used-by = the draft entry paths) inserted after the `S884` row
   inside `## Registry`; `reports/round-75/telemetry/gap-sweep.txt` written with the `808-row`
   registry line and `-> 0 matches` per frozen fragment; one commit → `git archive` →
   `mock-lands/` (the `mat` input). Census afterwards reports `file rows 817` (808 + 9) and
   `exit 0`, as a landed registry should.
4. Assembly and execution: `exec()` of PART A (lines 1-510 of
   `.ufo/waves/round-75/counters/accept-c.py`) + `part-cfg.py` + my part in one namespace, then
   each leg called with the contract `ctx` (`root land mat mat_base cfg fleet_root scratch`).
5. Two cfg paths were exercised: (a) a hand-built stub cfg per `CFG-CONTRACT.md` (written
   before `part-cfg.py` landed), and (b) the **real**
   `part-cfg.py:load_frozen_config(lane, <mock freeze>)`. For (b) the mock freeze commit is the
   lane's DRAFT `claims.json` with `map.sha256` filled from a mock by-document map (the draft
   carries `null`, which `load_frozen_config` refuses by design). It loaded
   `access_date='2026-10-27'`, `entries=3`, `fragments=9`,
   `terms=['narrative structure', 'narratology']`, `rows=S885..S893` — so the legs read the
   same keys the frozen config actually exposes.
6. Positive format tolerance was checked too: the receipt as a Markdown table
   (`| frag | 0 |`) and as a wrapped pair (`frag:` newline `0 matches`) both PASS.

Positive mock: `LEG PASS GROUND`, `LEG PASS CITEDLINES` (`files=3 last-line=CITED-LINES: 0
finding(s) in 3 file(s)`), `LEG PASS CENSUS` (`exit=0 last-line=file ok
<mat>/corpus/SOURCES.md`).

## 4. Positive / mutant table

Matrix over the three legs (`P` pass, `F` fail). Every mutant changes only the mock in its own
copy; each is expected to fail exactly its own leg.

| case | what it does | ground | citedlines | census |
|---|---|---|---|---|
| positive | mock lands as built | P | P | P |
| p1_table_receipt | receipt as a Markdown table with `0` per fragment | P | P | P |
| p2_wrapped_receipt | receipt as `frag:` / `0 matches` continuation | P | P | P |
| g1_receipt_807_rows | receipt says `807-row registry` | **F** | P | P |
| g2_receipt_nonzero_fragment | `iris.unipa.it -> 2 matches` | **F** | P | P |
| g3_receipt_missing | `gap-sweep.txt` deleted | **F** | P | P |
| g4_base_names_fragment | base registry row mutated to name `persee.fr/doc/comm_…_1113` | **F** | P | P |
| g5_receipt_global_zero_only | one `0 matches over the base registry` line with the nine fragments listed under it | **F** | P | P |
| c1_entry_multi_id_line | `- note: S885 and S886 both carry this sentence` appended to the canonical entry | P | **F** | P |
| c2_entry_invalid_utf8 | `\xff\xfe` appended to the amendment entry | P | **F** | P |
| n1_row_ten_cells | 10-cell row `S894` appended inside `## Registry` | P | P | **F** |
| n2_used_by_missing_path | `S894` with `used-by = corpus/knowledge/myth-symbol/nope.md` (inside Registry) | P | P | **F** |
| n3_duplicate_id | second `S885` row | P | P | **F** |

Verbatim FAIL details (one line each, as printed by PART A's `leg()`):

```
g1  LEG FAIL GROUND        receipt names a 807-row registry; the base holds 808
g2  LEG FAIL GROUND        receipt shows no 0 for fragment 'iris.unipa.it'
g3  LEG FAIL GROUND        receipt missing: reports/round-75/telemetry/gap-sweep.txt
g4  LEG FAIL GROUND        base registry already names the fragment 'persee.fr/doc/comm_0588-8018_1966_num_8_1_1113'
g5  LEG FAIL GROUND        receipt shows no 0 for fragment 'persee.fr/doc/comm_0588-8018_1966_num_8_1_1113'; receipt shows no 0 for fragment 'persee.fr/doc/comm_0588-8018_1966_num_8_1_1120'; … (truncated at 300 chars)
c1  LEG FAIL CITEDLINES    tool exit=1; no zero-findings line over 3 file(s): CITED-LINES: 1 finding(s) in 3 file(s) (files=3 last-line=CITED-LINES: 1 finding(s) in 3 file(s))
c2  LEG FAIL CITEDLINES    tool exit=2; no zero-findings line over 3 file(s): (no stdout) (files=3)
n1  LEG FAIL CENSUS        census exit=1; census TSV carries E-code line(s): E01 (exit=1 last-line=file	E01	S894 fields=10)
n2  LEG FAIL CENSUS        census exit=1; census TSV carries E-code line(s): E11 (exit=1 last-line=file	E11	S894 missing used-by corpus/knowledge/myth-symbol/nope.md)
n3  LEG FAIL CENSUS        census exit=1; census TSV carries E-code line(s): E03 (exit=1 last-line=file	W03	S885 mined but unused)
```

Three further mutants were run through the **real** `load_frozen_config` cfg (mock freeze
`cebc21e0…`, mock lands `f35ee9c8…`):

```
cfg-g1_receipt_807   GROUND F   receipt names a 807-row registry; the base holds 808
cfg-c1_multi_id      CITED F    tool exit=1; no zero-findings line over 3 file(s): CITED-LINES: 1 finding(s) in 3 file(s) (files=3 …)
cfg-n2_used_by       CENSUS F   census exit=1; census TSV carries E-code line(s): E12 (exit=1 last-line=file	E12	S894 row outside Registry section)
```

(`cfg-n2` appended the row after the last byte of the file, so it landed outside `## Registry`
and the census answered E12 rather than E11; the hand-built-cfg `n2` above shows the E11 path
on a row that sits inside the section.)

## 5. w1 junk paths that apply to my legs

- **CritCCounterVacuity / r74 F1 (CITEDLINES: stub tool in the graded tree).** *Survives* my
  leg: the frozen text names "tools/check-cited-lines.py … from the materialized tree" and pins
  no blob, so a replaced stub printing the required line passes. The critic's repair #1 (pin the
  tool to `git show <freeze>:tools/check-cited-lines.py`) would close it, but adding the pin here
  would be stronger than the frozen text; it is a freeze decision for the L1, not a leg
  implementation choice.
- **GROUND fabricated receipt (r74 F8).** *Partly rejected now.* The count, the per-fragment
  naming and the zero's ownership are all checked, the fragment's own digits cannot supply the
  zero, and a global-only zero fails (`g5`). A receipt that fabricates plausible per-fragment
  zeros still passes: offline provenance of a receipt is not gradeable, and the leg's real
  defence is the independent re-derivation from `mat_base` (`g4`), exactly as the wording says.
- **CENSUS semantic drift (r74 F10).** *Not* caught here and not supposed to be: the wording is
  exit 0 plus no E-code. Byte identity of pre-existing rows and exact added rows belong to ROWS;
  cell semantics belong to the Gate/scouts.
- **Census row-binding blind spots (MutRegistryCollision F2/F3, 4-space and tab rows,
  4-digit ids).** The census simply does not count those rows; my leg inherits exactly the
  census's verdict, which is what the wording asks. Noted so nobody reads CENSUS green as
  evidence of indentation or id-frontier correctness.

## 6. Scope receipts

- Read-only in the lane: `git show f556d104…:corpus/SOURCES.md`, `git ls-tree`, `git show
  <base>:corpus/lessons/…` and `tools/check-cited-lines.py` reads. The only lane writes are the
  part file and this report.
- The census script was invoked as a read-only validator (`validate` writes only stdout, per its
  own header and `out_sink()`); no `--out`, no `--root` fleet writes, no fixture created under
  the fleet tree.
- The checked-in drafts were read at
  `.ufo/waves/round-75/drafts/narrative-structure-frameworks{,amend-2026-10-23,amend-2026-10-23b}.md`
  and pass `CITED-LINES: 0 finding(s) in 3 file(s)` unchanged at base+lane — so the positive mock
  is the real entry text, not filler.

## 7. Residual risk / open items for the L1

1. **CITEDLINES authority is the graded tree** (A6). A landing that replaces
   `tools/check-cited-lines.py` passes this leg. If the L1 wants the critic's repair, the frozen
   leg text must say so and I will implement the pin.
2. **GROUND receipt provenance** (above): only the base-side re-derivation is independent.
3. **Receipt shape.** The leg wants the `0` on (or immediately under) the fragment's own line. A
   gap-sweep written as one global "0 matches" total will FAIL by design (A2). The scribe's
   receipt should print one line per fragment.
4. **`cfg["terms"]` is ungraded** here by the wording (A1). If the freeze intends the CJK/term
   sweep to be graded, the leg text must name it; `ground.terms` is already loaded by
   `part-cfg.py`.
5. My legs assume `mat`/`mat_base` are the counter's own materializations (contract §ctx); they
   never read the lane worktree.
6. Post-integration gates (counter assembly, `--selftest`, do-nothing receipts) belong to the
   parent; this seat ran only the three legs on the mock described above.

## 8. Installs

None. Nothing was installed, upgraded or removed; no `pacman`, no `pip`/`uv`/`npm`/`cargo`.
