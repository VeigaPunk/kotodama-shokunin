- Seat: P01 | planner | claim O | date 2026-10-19 | baseline 139e3b6

# P01 — execution plan for claim O (lessons-index reconciliation + falsifier disposition)

Plan only. This seat writes nothing else: no README edit, no SKILL.md edit, no tool
edit, no lesson edit. Every number below was measured by this seat at the round-33
tree (HEAD `139e3b662900557afe54f632b468619593dc9fcb`); the commands are in
§5. Where a measurement must be re-taken at apply time, the plan says so rather
than letting a reader inherit a pin.

Dependencies: `op/K01-falsifier-scout.md` and `op/K02-lessons-census.md` did not
exist when this plan was written (`ls reports/round-33/op/` → empty). Both legs
were therefore scouted by this seat directly; §2.1 and §1.2 carry the findings
K01/K02 were to deliver, marked as self-measured and cross-checkable. See
`## Owed`.

---

## 0. The claim-O contract this plan serves

From `reports/round-33/claims.json` (claims[0], id `O`):

- **(a) lessons leg** — README carries one row per `corpus/lessons/*.md` file
  (33/33), prose arithmetic states 33, every new row's `bytes`/`lines`/`sha8`
  re-measured from live bytes, owners resolve, format classes documented; filed
  lesson files untouched. Counting commands: the c31 audit (exit 0, zero
  findings) and its `--selftest`.
- **(b) falsifier leg** — a dated disposition record at
  `reports/round-33/op/O05-falsifier-disposition.md`: located + bounded fix draft
  + control, or carried with owner + reason.
- **Zero regressions** vs the O07 baseline receipt (battery 10/10, craft
  selftests, gate selftests, c31 selftest).

### 0.1 Declaration-time state, re-measured (2026-10-19)

`python3 -B reports/round-25/audit/c31-lessons-index-audit.py`:

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
  C31-1 unindexed-file: ['round-26.md', ..., 'round-32.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26], 'measured': [26, 33]}}
exit=1
```

`--selftest` → `SELFTEST OK: 28/28 checks passed`, exit 0. Both readings reproduce
`claims.json` O.before exactly (7 unindexed files, stated [26,26] vs measured
[26,33], 33 files vs 26 rows). Exit codes verified without a pipe: run **1**,
selftest **0** (`main()` returns `0 if not res["findings"] else 1`).

---

## 1. Leg A — lessons-index reconciliation design

### 1.1 Target state (what "after" must read)

The README is a **live index, not a filed lesson file**: `corpus/lessons/README.md`
is not in the filed-bytes set (`reports/round-1..32/**`, `corpus/lessons/*.md`
lesson files, `tools/gates/frozen/**`, fleet `.ufo/**`). Its own closing rule
(`corpus/lessons/README.md`, last block: "Superseding edits land as a new revision
block here, never as an in-place rewrite of the per-round rows' provenance
claims") is the convention revision 2 already followed — it repaired table cells
and appended a block. Claim O's acceptance requires the same shape: the c31 tool's
`INDEX` is hard-wired to `corpus/lessons/README.md`
(`reports/round-25/audit/c31-lessons-index-audit.py:36-38`), so **no separate
revision file can turn C31 green**. A new revision file would be a new artifact,
not this claim's after-state.

Post-edit expectation, exact:

```
index present: True
lesson files:  33
index rows:    33
queue rows:    <49 + rows actually added; see §1.4>
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0
exit 0
```

plus `--selftest` 28/28 exit 0 (the tool is filed round-25 bytes — **no seat may
edit it**; if it cannot be satisfied without editing the tool, honest-stop per §4).

### 1.2 Row-draft contract (O01) — measured cells, live at plan time

Insert **7 rows in filename order after the `round-25.md` row and before the
`supplement-opencode-1.md` row** (`corpus/lessons/README.md:94-95`). Column shape
copied from the existing rows (`:71-95`): file · format · contract · open-questions
carried · disposition pointer · pin.

| file | format | contract | open-questions carried | disposition pointer | pin |
|---|---|---|---|---|---|
| `corpus/lessons/round-26.md` | gate-keeper | 4/4 | refs Q-02-1, Q-04-1, Q-14-1, Q-23-1..3 (no own ids) | `reports/round-26/validation.json` | bytes=60054 lines=222 sha8=cae06660 |
| `corpus/lessons/round-27.md` | gate-keeper | 4/4 | — (see §1.4 limit) | `reports/round-27/validation.json` | bytes=54972 lines=203 sha8=f15e285b |
| `corpus/lessons/round-28.md` | gate-keeper | 4/4 | — (see §1.4 limit) | `reports/round-28/validation.json` | bytes=50419 lines=145 sha8=dd832ff7 |
| `corpus/lessons/round-29.md` | gate-keeper | 3/4 | — (see §1.4 limit) | `reports/round-29/validation.json` | bytes=17847 lines=118 sha8=b6765d33 |
| `corpus/lessons/round-30.md` | gate-keeper | 3/4 | Q-30-1..5 | `reports/round-30/validation.json` | bytes=30665 lines=181 sha8=56e77835 |
| `corpus/lessons/round-31.md` | gate-keeper | 4/4 | Q-31-1..4 | `reports/round-31/validation.json` | bytes=16637 lines=73 sha8=8870bbdd |
| `corpus/lessons/round-32.md` | gate-keeper | 4/4 | Q-32-1..6 | `reports/round-32/validation.json` | bytes=12879 lines=66 sha8=8aacfc2b |

Cell derivation rules (each cell re-derived at apply time, never inherited):

1. **format** — the tool's own classifier (`c31-…py:76-82`): `fragment-index` iff
   `^## Fragment index$`; else `gate-keeper` iff `^## Gate$`; else `plain`. All 7
   measure `gate-keeper` (no new class → C33 stays green, §3 histogram moves
   14 → 21).
2. **contract** — count of line-anchored `source:`/`verified-at:`/`recheck:`/
   `scope:` (`c31-…py:85-95`), rendered `n/4`. r29/r30 are 3/4 and the missing key
   is **`recheck:`**, not `scope:` — measured: both carry
   `source:`/`verified-at:`/`scope:`, the same shape as round 16. Consequence for
   §1.3: the README's §3 sentence describing the 3/4 class as "each has `source:`,
   `verified-at:` and `recheck:` but no `scope:` line" is **already inaccurate for
   round 16** and becomes inaccurate for rounds 29–30; the Revision-3 block must
   reword it (e.g. "3/4 — the missing key varies by round: `scope:` for rounds
   5–15, `recheck:` for rounds 16, 29, 30").
3. **pin** — `bytes` = `os.path.getsize`, `lines` = `len(text.splitlines())`,
   `sha8` = first 8 of sha256 of the file bytes. **Re-measure at apply time**;
   the values above are this seat's, and they are cross-checked by two independent
   filed sources: `corpus/lessons/round-32.md:45` carries r26–r31 pins
   `60054/222/cae06660`, `54972/203/f15e285b`, `50419/145/dd832ff7`,
   `17847/118/b6765d33`, `30665/181/56e77835`, `16637/73/8870bbdd` — **6/6 equal
   to this seat's measurement** — and `reports/round-33/op/K02-lessons-census.md`
   (landed after this plan's first draft) measures **7/7 equal**, r32 included.
4. **disposition pointer** — must name a **live path** (C35 lesson: the tool does
   not resolve pointers, so this is hand-verified). All 7 targets exist
   (`reports/round-{26..32}/validation.json`, checked). Do not point at
   `reports/round-N/` bare if a `validation.json` exists.
5. **open-questions carried** — ids from §4 only; cross-references to already-queued
   rows are annotated, never re-queued (r26's six tokens are references, not new
   items).

### 1.3 Prose-arithmetic correction map (O02) — line-keyed

Every count site in the README, with the required after-value. Historical
revision blocks (`:3-30` revision 1.9 … `:305-330` revision 2) are **dated
readings and are not edited**; the reconciliation lands as a new appended
**Revision 3** block that states what moved and why.

| line | current | required after |
|---|---|---|
| `:6` | "one row per file the runner's partition glob returns (26 at the final stamp …)" | 33 at the new stamp (new Revision-3 block owns the movement; the `:6` sentence is inside the round-25 revision-1 preamble — treat it as history, not as a live count; if the integrator prefers a live reading, the Revision-3 block is the place, not an in-place rewrite) |
| `:35` | `--selftest  # 26/26, exit 0` | still 28/28, exit 0 (the comment is already stale by two — fix to `28/28`; the tool's own selftest count is what binds) |
| `:39-40` | `ls … wc -l  # 26` / `find … # 26` | re-measured count (33 at plan time) |
| `:97` | `**Rows: 26. Files: 26.**` | `**Rows: 33. Files: 33.**` — **exact literal**, C34b regex `\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*` |
| `:118` | gate-keeper "**14 files.**" | **21 files** |
| `:136-140` | "rounds 17–23 carry 4/4"; 3/4 list; "gate-keeper **14** = the 13 filed plus the round-25 lesson"; "Total 26" | 4/4 gains rounds 26–28, 31–32; 3/4 list gains rounds 29, 30; gate-keeper **21** = the 13 filed plus rounds 25–32 (8); Total **33** |
| `:207` | "Rows: **49**. Of the 26 index rows, **23 carry at least one question**" | `Rows: **<measured>**` (C34b regex `Rows:\s*\*\*(\d+)\*\*`), "Of the 33 index rows, **26 carry at least one question**" (r30/r31/r32 gain ids; r26–r29 carry none → 7 rows carry none: r1, r25, README self-row, r26, r27, r28, r29) |
| `:209-212` | owner classes path 37 / role token 12 | recomputed from the queue table after §1.4 |
| `:256-257` | "146 files under nine directories beside the 26 `*.md` lesson files" | the subdirectory table is unchanged (no new evidence dirs); the `*.md` count → **33** |
| `:285` | "`--selftest` is 26/26 in-memory checks" | **28/28** (the tool's own `SELFTEST OK: 28/28`, measured) |
| §5 subdir table | nine dirs / 146 files | re-measure `find corpus/lessons -mindepth 2 -type f \| wc -l` at apply time; unchanged if nothing landed |
| new block | — | **Revision 3 (round 33)**: names the 7 rows added, the arithmetic moves, the queue additions, the c31 receipt (exit 0, findings 0, selftest 28/28) with its stamp, and cross-references `reports/round-26/zzz-lessons-index-revision-3.md` (the filed round-26 queue-disposition revision) instead of duplicating it |

Fragility, measured (2026-10-19, both regexes against candidate strings):

| literal | queue regex `Rows:\s*\*\*(\d+)\*\*` | table regex `\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*` |
|---|---|---|
| `**Rows: 33. Files: 33.**` | no match | `[('33','33')]` |
| `Rows: **33**` | `['33']` | no match |
| `Rows: **64**. Of the 33 index rows` | `['64']` | no match |

So the table line must keep the **leading** `**` before `Rows` and the
`. Files: N.**` tail: writing the table count as `Rows: **33**` would be read by
the *queue* regex and compared against the queue-row count, and C34b would report
a table/queue cross-mismatch rather than the truth. Keep both literals verbatim.

### 1.4 Queue delta (O02) and the owner-normalization trap

The queue is §4 (`:150-212`), read by the tool as rows starting `| Q-` other than
`| Q-id` (`c31-…py:110-115`). Zero Q-30/31/32 rows are in the README today
(`grep -c "Q-3[0-2]-" corpus/lessons/README.md` → 0). The lessons carry **15
explicit ids** that must appear:

- `Q-30-1` operator/freshness · `Q-30-2` parent/lesson indexing · `Q-30-3`
  gate-owner/semantic ceiling · `Q-30-4` telemetry owners · `Q-30-5`
  retrospective owner (`corpus/lessons/round-30.md:103-105,142,146,173`)
- `Q-31-1` orchestrator/D landing anchor · `Q-31-2` O owner + parent/sweep
  denominator · `Q-31-3` parent/lesson indexing · `Q-31-4` parent + validator
  evidence-path boundary (`corpus/lessons/round-31.md:57-60`)
- `Q-32-1` … `Q-32-6` (`corpus/lessons/round-32.md:55-60`)

**Owner-normalization rule (a real trap).** `resolves()` accepts exactly: a live
repo-relative path, a `round-N` pointer that resolves, or the role tokens
`operator`, `parent`, `lore-shokunin`, `integrator` (`c31-…py:131-149`). The
lessons' own owner labels — `orchestrator`, `gate owner`, `r32 validator`,
`retrospective owner`, `telemetry owners`, `O owner` — **do not resolve** and
would turn C32 red. Each new row's owner cell must be normalized to a resolving
token (e.g. `orchestrator` → `parent`; `gate owner` → the gate's live path such as
`tools/gates/register-law-gate.py`; `r32 validator` → `parent`) and the original
label may be kept in the question cell. O03 verifies each cell against the tool's
`resolves()` semantics before the integrator applies anything.

Extraction completeness is a named limit (README §6 already says the queue is
"extracted, not exhaustive of prose"). r27/r28/r29 name open legs in prose
without ids (`corpus/lessons/round-27.md` tail: "D — partially met, with two named
open legs"; `round-28.md` addendum: `X57-G6` ledger off the acceptance surface;
`round-29.md` closeout: "C remains incomplete … O has open work"). O02 must
either add Q-27-1/Q-28-1/Q-29-1-style rows with lesson-line citations, or record
the explicit decision not to, with the reason — and the Revision-3 block must
state the limit rather than imply completeness. The §2 rows' open-questions cells
for r27–r29 follow that decision.

### 1.5 Negative controls (O06) — mirror harness, not live-tree mutations

The controls must not write into `corpus/lessons/` on the live tree (that would
move the partition and is a filed-surface risk). Use the round-26 pattern —
`git clone -q . .scratch/<name>/repo` (`reports/round-26/zzz-lessons-index-revision-3.md`
§0) — and mutate the **clone**:

| # | mutation in the clone | expected |
|---|---|---|
| C-pos | none (clone of the reconciled tree) | findings 0, exit 0 — proves the harness adds no red |
| C-1 | add `corpus/lessons/round-99.md` | `C31-1 unindexed-file ['round-99.md']`, FAIL C31, exit 1 |
| C-2 | add a row naming `corpus/lessons/round-98.md` | `C31-2 ghost-row`, exit 1 |
| C-3 | table line → `**Rows: 32. Files: 33.**` | `C34-2 prose-arithmetic-drift`, exit 1 |
| C-4 | change one row's `sha8=` | `C34-1 pin-drift`, exit 1 |
| C-5 | add a queue row owned `orchestrator` | `C32-1 unresolvable-owner`, exit 1 (documents §1.4) |
| C-6 | change one row's format cell | `C34-3 shape-cell-drift`, exit 1 |

Feasibility measured by this seat on a **partial** mirror
(`.scratch/p01-mirror`, tool + README + one lesson + a fake `round-99.md`):
C31-1 fired on the fake file, C34b fired on the stated counts, exit 1. Lesson for
O06: a **partial** mirror also false-fires C32 (every owner path is missing in the
mirror) — use a full clone, or read only the C31/C34 legs and name the C32 noise.
Do not present a partial-mirror C32 red as a defect.

### 1.6 Integration order and write ownership

1. O07 baseline receipt **before any edit** (battery/craft/d4/c31 selftests).
2. Integrator applies the README edit (rows → arithmetic → queue → Revision-3
   block), one atomic change.
3. Post-edit: c31 run + `--selftest` + `--json` receipt captured to a round-33
   path; O01/O02/O03/O04 fragments re-read against the applied bytes.
4. Controls C-pos/C-1..C-6 in the clone.
5. R01–R03 review; S01 folds into the operability receipt.
6. X00/A09 pin-cascade check before and after (see §3 R2).

---

## 2. Leg B — the falsifier-mismatch disposition plan

### 2.1 The artifact, located and reproduced (self-scouted; K01 landed — see §6)

The routed debt is named at `SCORECARD.md:443-445`: "Routed debt recorded for the
operator: the falsifier audit's filename mismatch (substance 5/5), 7 unindexed
lessons, 12 standing open items in the dossier, the promotion + freshness
decisions."

**It is the round-31 jin'i-ryu telemetry-closure rule's landed audit, and it is
recorded at `corpus/lessons/round-32.md:41` (finding F-X16-3):**

> "The `SKILL.md:715` audit, verbatim, prints **5 records**
> (`reports/round-{19,25,26,27,28}/availability.json` — all admitted rounds): it
> requires a file literally named `telemetry/closing-snapshot.json`, but the
> landed snapshots are named `telemetry/availability-close-N.json`. Every record
> it names IS closed; the instrument cannot see the closures. … the substantive
> form of the same check … passes 5/5."

The three surfaces, verified by this seat:

- **The instrument**: `SKILL.md:713-715`, checklist item ending with the inline
  audit `glob('reports/round-*/availability*.json') … and not
  os.path.exists(… 'telemetry','closing-snapshot.json')`.
- **The landed convention**: `reports/round-19/telemetry/availability-close-19.json`
  and `reports/round-{25,26,27,28}/telemetry/availability-close-{25,26,27,28}.json`
  — five files; each carries `closes` (e.g. `reports/round-19/availability.json`)
  and `closes_sha256` (read at plan time). The in-repo validator already encodes
  this name: `reports/round-31/run-validation.py:780` builds
  `telemetry/availability-close-<N>.json`. (The round-31 draft proposed the
  **unsuffixed** name `availability-close.json`,
  `reports/round-31/jinii/draft.md:56-57` — so the draft, the landing and the
  SKILL audit name three different files; only the landed convention is on disk.)
- **Reproduction (this seat, 2026-10-19)**: the SKILL.md:715 command verbatim
  prints the five `availability.json` paths (false-fire); the re-keyed command
  (`… os.path.exists(os.path.join('reports', r, 'telemetry',
  'availability-close-%s.json' % r.split('-')[1]))`) prints nothing — all five
  records are closed. Substance is intact; only the instrument's filename is
  wrong.

### 2.2 Decision criteria — bounded fix vs carry

**Bounded fix** requires ALL of: (1) the defective bytes are in a file the
integrator may edit as a drafted change (SKILL.md — not filed-round bytes);
(2) the change is bounded (one command string inside one checklist item);
(3) there is a control that is red on the pre-fix command and green on the
post-fix command, on the same tree; (4) no filed-round/lesson byte changes;
(5) the rule's semantics are unchanged — a filename key, optionally plus the
substantive `closes`/`closes_sha256` check; (6) the change is recorded in LOG.md
by the integrator with before/after.

**Carry** is required when ANY of: (a) the item is a rule change rather than an
instrument repair (operator-owned); (b) the fix would touch filed bytes;
(c) the target is not identifiable; (d) the fix would pre-empt an operator
decision that is already routed.

**Applying the criteria to this instance:**

- The **instrument re-key** = bounded fix (satisfies 1–6). This is the round-33
  O disposition.
- The **LOG.md falsification clause (i)** — `corpus/lessons/round-32.md:41`
  records that it "has therefore fired on day one for an instrumental reason" —
  = **carry**: rewording or retiring a recorded falsification clause is a rule
  change, operator-owned (criterion a). Owner `operator`; reason: the clause's
  status is an operator ruling, and the instrument repair does not settle it;
  next touch: the round-33 close record / next operator decision.
- Adjacent F-X16 family items (`Q-32-2` AGENTS.md:40-42 residue, `Q-32-3`
  checklist position, `Q-32-4` draft-vs-landing) are **out of claim O's leg**:
  name them in the disposition record as routed-not-absorbed with their Q-ids,
  and do not fix them here. Fixing the checklist position (Q-32-3) would move the
  very line O's fix edits — that is an integrator/operator call, not a seat's.

### 2.3 What O05 must produce (`reports/round-33/op/O05-falsifier-disposition.md`) — O05 landed; adopt its §3b/§4, see §6

1. Located artifact + quoted lines (as §2.1) with file:line citations and the
   date.
2. **Fix draft** — exact before/after text block for `SKILL.md:715`'s command
   string, re-keyed to `availability-close-<N>.json`, **keyed on the exact
   string, not on the line number** (line numbers shift; §3 R1). Optionally add
   the substantive leg (read the snapshot's `closes` and compare
   `closes_sha256` to the record's live digest) — if added, say so and keep the
   negative control (C-1: point one snapshot's `closes_sha256` at the wrong
   digest in a clone → the substantive check must fire).
3. **Control** — the pre-fix command's non-empty output and the post-fix
   command's empty output, both quoted with their stamps; plus the substantive
   form's 5/5 (each snapshot's `closes` names its record; `closes_sha256`
   recomputed).
4. **Carry row** — the LOG clause (i) with owner + reason + next touch (§2.2).
5. **Round-33 self-application** — once re-keyed, the audit becomes a live check
   for round 33's own record: `reports/round-33/availability.json` (when it
   lands) must be closed by `reports/round-33/telemetry/availability-close-33.json`
   per `AGENTS.md:32-39`, or the re-keyed audit prints it. Record this as the
   integrator's owed act at round close, not as a seat action.

---

## 3. Risks, collisions, and what a reader must not misread

- **R1 — SKILL.md is a two-claim write surface.** Claim C's `C14` drafts the
  box-1 citation pointer fixes, which may also land in SKILL.md. Apply order:
  O's one-line re-key and C's citation drafts must be serialized, and both must
  be keyed on strings, not line numbers. X00 (`cross/X00-connector.md`) owns the
  collision matrix; A09 owns the pin-cascade list.
- **R2 — no live gate re-runs the lessons instruments today.** `grep` over
  `reports/round-32/sweep/run-sweep.py`, `final-sweep.md`, `run-validation.py`,
  `sweep-audit.py` for `x57|c31-lessons|lessons-index` returns **no matches**, so
  the README edit does not drift any round-32-sweep command. Filed readings that
  bind the README digest (`reports/round-26/audit/x63-lessons-receipt.json:74-75`,
  `reports/round-27|28/audit/x57-lessons-receipt.json`, observed `ec7469da…`) are
  dated measurements of the pre-edit bytes — a later x57 re-run reading a new
  digest is a new measurement, not a defect. Do not "repair" those receipts.
- **R3 — the self-row exemption is singular.** Only the README's own row carries
  `sha8=self-referential` and is exempt from C34 (`c31-…py:245-247`); no new row
  may claim the token.
- **R4 — pins are re-measured, never inherited** (the tool's own C34 rule). If a
  lesson lands mid-round, the partition moves and the after-state is 34/34 with
  an added row — record it as a new measurement.
- **R5 — literal-string fragility** (§1.3): keep `**Rows: N. Files: N.**` and
  `Rows: **N**` shapes exactly.
- **R6 — owner tokens** (§1.4): `orchestrator`/`gate owner`/`r32 validator` do
  not resolve; C32 would go red.
- **R7 — `reports/round-26/zzz-lessons-index-revision-3.md` is filed round-26
  bytes** (a queue-disposition revision of the index, 23 411 B). Do not edit it,
  do not copy its "Rows: 27. Files: 27." as a live count; cross-reference it.
- **R8 — extraction completeness is a named limit**, not a green. The Revision-3
  block must state which prose-named open items were extracted and which were
  deliberately not (§1.4).

---

## 4. Honest-stop triggers

Stop and report (do not force a pass) if: the c31 tool would need an edit to go
green (filed round-25 bytes); the README edit cannot be applied by the integrator
before the round's validation (claim O unverifiable); a lesson lands after the
edit and the row set moves without a re-measure; the falsifier fix would require
editing a filed round or the LOG clause rather than the instrument; or the
controls in §1.5 cannot be run in a clone (no network/space) — in that case the
claim is reported with the control leg unproven, not asserted.

## 5. Commands this plan rests on (all read-only, 2026-10-19)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-25/audit/c31-lessons-index-audit.py            # exit 1, findings 2
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest # 28/28, exit 0
# per-file cells (bytes/lines/sha8/format/contract) — inline python, corpus/lessons/{round-2[6-9],round-3[0-2]}.md
python3 -c "…glob('reports/round-*/availability*.json')…'closing-snapshot.json'"   # prints 5 (false-fire)
python3 -c "…'availability-close-%s.json' % r.split('-')[1]…"                      # prints nothing
ls reports/round-{19,25,26,27,28}/telemetry/availability-close-*.json               # 5 files
grep -rn "x57\|c31-lessons\|lessons-index" reports/round-32/{sweep/run-sweep.py,final-sweep.md,run-validation.py}  # no matches
```

## 6. Cross-check against the fragments that landed after this plan's first draft

`ls reports/round-33/op/` was empty when this plan was drafted; by the time it
closed, K01, K02, O01, O03, O04, O05, O07 and O08 had landed. Reconciliation:

| element | this plan | landed fragment | verdict |
|---|---|---|---|
| falsifier location | §2.1: F-X16-3 at `corpus/lessons/round-32.md:41`; instrument `SKILL.md:713-715`; route Q-32-1 | `op/K01-falsifier-scout.md` §1–2: same, plus the `:36` heading and the `:55` route | **full agreement**, independently measured |
| false-fire reproduction | §2.1: verbatim command → 5 rows; re-keyed → empty | K01 §3: same | full |
| row cells (7 files) | §1.2 table | `op/K02-lessons-census.md`, `op/O01-row-drafts.md`: identical bytes/lines/sha8/format | **7/7 equal**; K02 supplied the `recheck:` nuance now folded into §1.2 rule 2 |
| disposition pointers | §1.2 rule 4: `validation.json` for all 7 | K02 prefers `round-30/routed-resolution.json`, `round-31/closure-ledger.json`, `round-32/completion-ledger.json`; O01 uses `validation.json` with the ledgers as secondary | both classes resolve; integrator picks one per row, O03's pointer checks govern |
| bounded fix | §2.2 criteria + §2.3 filename-key sketch | `op/O05-falsifier-disposition.md` §3b: a **content-keyed** repoint (any `telemetry/availability-close-*.json` whose `closes` names the record and whose `closes_sha256` matches the record's live bytes) with a 7-scenario control set | O05's draft is strictly stronger; **adopt O05 §3b** as the fix of record |
| the LOG clause (i) | §2.2: carry — the reword is a rule change, operator-owned | O05 D-2: **no change required once D-1 lands** (clause (i) is satisfied as written; the day-one fire is explained as instrumental); a reword, if chosen, is a new dated LOG entry | compatible; O05's reading is the tighter one — the plan's carry row is the *reword option*, not a required act |
| checklist position | §2.2: routed, not absorbed (Q-32-3) | O05 §3c: same routing | full |
| snapshot key name | not in this plan's draft | K01 and O05 D-3: the lesson prose says `closes_record`, the live key is `closes` | recorded as a carried lessons-write note (filed lesson, append-only) |

Two additions this cross-check forces into the plan of record:

1. §1.2 rule 2's `recheck:` correction (applied) and the §3 wording repair it
   forces in the Revision-3 block (§1.3).
2. The `reports/round-31/run-validation.py:780` exposure O05 demonstrates at its
   §6: that closure test is **name-exact** (`availability-close-<N>.json`), so a
   correction-named snapshot is invisible to it — the same defect class as
   F-X16-3 in a filed instrument. **Routed, not absorbed** (filed bytes; today's
   five snapshots all carry the exact name). It belongs in the round-33 report's
   routed list beside Q-32-2..Q-32-6.

## Owed

- The `op/` dependency set this plan was to be built from — `K01-falsifier-scout.md`,
  `K02-lessons-census.md`, `O01-row-drafts.md`, `O03-owner-checks.md`,
  `O04-format-checks.md`, `O05-falsifier-disposition.md` — was absent at drafting
  and present at close (§6). The integrator folds §6 into the claim-O receipt
  rather than treating this plan as those seats' input.
- Integrator-applied drafts this plan specifies but does not write: the README
  edit (§1.2/§1.3/§1.4 + Revision-3 block) and O05's §3b SKILL.md repoint.
- `reports/round-33/availability.json` + `reports/round-33/telemetry/availability-close-33.json`
  — the re-keyed audit's own round-33 closure leg (§2.3.5); integrator's owed act.

## Citations

- `reports/round-33/claims.json` (claims[0] `O`, `before`/`after_required`/`counting_commands`)
- `reports/round-33/targets.json` (seat P01; shared_rules)
- `REGIMEN.md` (per-round contract; freshness pause)
- `reports/round-25/audit/c31-lessons-index-audit.py:36-38,76-95,110-149,245-247` and its `main()` exit rule
- `corpus/lessons/README.md:6,35,39-40,71-97,116-140,150-212,254-260,283-287,305-330`
- `corpus/lessons/round-30.md:103-105,142,146,173`; `corpus/lessons/round-31.md:57-60`; `corpus/lessons/round-32.md:41,45,55-60`
- `corpus/lessons/round-27.md`, `round-28.md`, `round-29.md` tails (open legs in prose)
- `reports/round-26/zzz-lessons-index-revision-3.md` §0 (clone-control pattern)
- `SKILL.md:713-715`; `AGENTS.md:32-42` (`wc -l AGENTS.md` = 42)
- `reports/round-31/run-validation.py:780`; `reports/round-31/jinii/draft.md:56-57`
- `reports/round-32/fragment-index-x20.md:81`; `reports/round-32/scope.md:29`
- `SCORECARD.md:443-445`
- `reports/round-{19,25,26,27,28}/telemetry/availability-close-*.json` (read: `closes`, `closes_sha256`)
- `reports/round-26/audit/x63-lessons-receipt.json:74-75`; `reports/round-27/audit/x57-lessons-selftest.json:7`
- Commands: c31 run/selftest/json; the two audit one-liners (verbatim + re-keyed); `git rev-parse HEAD`; `git log --oneline -3`; `wc -l`; `ls`/`grep` as listed in §5; the `.scratch/p01-mirror` partial-mirror probe
