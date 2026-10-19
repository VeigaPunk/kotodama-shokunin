- Seat: O03 | executor | claim O | date 2026-10-19 | baseline 139e3b6

# O03 — owner-resolution checks (C32 leg) for the round-26..32 index rows and queue items

## 0. Scope, method, and the dependency gap

Mission: owner-resolution checks (C32 leg) for every new row and queue item
proposed by O01 (`op/O01-row-drafts.md`) and O02 (`op/O02-readme-delta.md`).
Neither fragment exists at this stamp (`find reports/round-33 -type f` →
`claims.json`, `targets.json`, `telemetry/dispatch-declared.json` only,
2026-10-19T03:54Z). Per the shared missing-dependency rule I did every part
that does not need their bytes: I derived the *candidate* row and queue items
from the live lesson bytes (r26–r32), ran the resolution check on each with the
audit tool's own resolver, and filed the per-item verdicts. What O01/O02 add —
their exact drafted cells — is verified against this table at integration; the
one alignment step that cannot be done without their bytes is named in §9 and
`## Owed`.

Method: every verdict below is produced by `resolves()` and `owner_cell()` from
`reports/round-25/audit/c31-lessons-index-audit.py:138-167` — the same two
functions the C32 check calls at `:213-227` — loaded read-only via `runpy`
(no import side effects: the module guards on `if __name__` at `:463`). No file
was written by the probe commands.

## 1. The resolver contract, as the tool actually implements it

`resolves(owner_token)` (`c31-lessons-index-audit.py:151-167`) accepts exactly:

| form | evidence | note |
|---|---|---|
| repo-relative path that exists | `:164-166` | `os.path.exists(ROOT/tok)` |
| literal role token `operator` / `parent` / `lore-shokunin` / `integrator` | `:158` | hard-coded set |
| `round-N` pointer whose `reports/round-N/` exists | `:160-162` | `os.path.isdir` |

It strips backticks and **one trailing parenthetical** (`:153-155`) and nothing
else — a slash- or plus-compound (`parent/operator`, `parent + validator`) is
not split and therefore fails.

The README's own prose states a narrower rule — "a live path in this repo, the
literal `operator`, or a round pointer" (`corpus/lessons/README.md:146-148`) —
while practice already uses `parent` (9 rows) and `operator` (3 rows):
measured classes over the filed queue are **path 37 / role-token 12, zero
unresolved** (`README.md:211-213`; re-measured this seat, §7 control P1). The
tool is the enforcing surface; `parent` is both established practice and
tool-green. This prose/tool divergence is a **documentation note for O02's
delta, not a defect**: the §4 prose could name the four role tokens the tool
accepts.

## 2. Index-row leg — disposition-pointer cells for the seven new rows

The §2 pointer column is **not machine-checked** by C31–C34 (`README.md:309-312`
says so in the C35 revision block; the round-4 pointer that named a
nonexistent path was a hand-caught finding, `README.md:314-323`). So this leg
is hand-verified here, C35-style, with the resolution criterion "the pointer
must name a surface that exists at HEAD".

| row | candidate disposition pointer | verdict | evidence |
|---|---|---|---|
| `corpus/lessons/round-26.md` | `reports/round-26/validation.json` | RESOLVES | exists; `acceptance_checks_passed: true` (`reports/round-26/validation.json:2`) |
| `corpus/lessons/round-27.md` | `reports/round-27/validation.json` | RESOLVES | exists; `acceptance_checks_passed: False` at both filed receipts (lesson `corpus/lessons/round-27.md:168-194`) |
| `corpus/lessons/round-28.md` | `reports/round-28/validation.json` | RESOLVES | exists; `acceptance_checks_passed: true` (`corpus/lessons/round-28.md:94`) |
| `corpus/lessons/round-29.md` | `reports/round-29/validation.json` | RESOLVES | exists (`ls reports/round-29/`) |
| `corpus/lessons/round-30.md` | `reports/round-30/validation.json` + `reports/round-30/routed-resolution.json` | RESOLVES | both exist; the lesson's own handoff names the ledger digest (`corpus/lessons/round-30.md:160`) |
| `corpus/lessons/round-31.md` | `reports/round-31/validation.json` + `reports/round-31/closure-ledger.json` | RESOLVES | both exist; ledger is the round's own falsification surface (`corpus/lessons/round-31.md:57-60`) |
| `corpus/lessons/round-32.md` | `reports/round-32/validation.json` + `reports/round-32/completion-ledger.json` | RESOLVES | both exist; the lesson routes its own rows to the ledger (`corpus/lessons/round-32.md:60`) |

All 21 candidate pointers probed with `test -e` in one pass; 21/21 EXISTS. No
row needs the "not filed; record is `LOG.md`" escape form the round-1..4 rows
use (`README.md:70-73`), because every round 26–32 filed a `validation.json`.

**Additional row-cell requirement.** The pointer cell must not be the *only*
cell that resolves: §2 rows also carry a pin and a format/contract cell, whose
re-measurement is O04's and K02's leg. My cross-check of the pin source O01
will draw from — round-32's §Ledger pins
(`corpus/lessons/round-32.md:45`) — reproduces exactly, 6/6 MATCH (§6).

## 3. Carried-cell leg — the §4 ids each new row names

A row's "open-questions carried" cell names §4 ids; a named id that is not in
§4 is a dangling cross-reference. Measured per lesson file (regex
`Q-[0-9]{2}-[0-9]+` over live bytes, set-difference against the 49 filed §4
ids):

| lesson file | ids named | in §4 today | dangling today |
|---|---|---|---|
| `round-26.md` | Q-02-1, Q-04-1, Q-14-1, Q-23-1..3 | 6/6 | 0 |
| `round-27.md` | none | — | 0 |
| `round-28.md` | none | — | 0 |
| `round-29.md` | none | — | 0 |
| `round-30.md` | Q-30-1..5 | 0/5 | 5 (must be minted by O02) |
| `round-31.md` | Q-30-2, Q-31-1..4 | 0/5 | 5 |
| `round-32.md` | Q-30-2, Q-31-1..4, Q-32-1..6 | 0/11 | 11 |

The r26 ids resolve in §4 (`README.md:152,157,176,197-199`), so its carried
cell is safe as-is — with the caveat the r26 lesson itself records: those
cells are the six **stale readings** it classed
(`corpus/lessons/round-26.md:161-164`), so O01 should either carry the ids plus
the staleness class, or name the class and the ids. Resolution either way; the
staleness wording is O01/O02's call.

The 15 dangling ids are **collision-free**: `grep -c` for `Q-26-1`, `Q-27-1`,
`Q-28-1`, `Q-29-1`, `Q-30-1`, `Q-30-3`, `Q-31-1`, `Q-32-1`, `Q-32-6` in
`README.md` → 0 each. Rounds 27–29 name no new id at all, so any r27/r28/r29
queue row O02 mints (see §5) opens a fresh, collision-free `Q-2{7,8,9}-*`
namespace.

## 4. Queue-row owner leg — the fifteen new items, per-item verdicts

Owner tokens below are the *prefix* each lesson's open-route bullet puts before
its `/` (e.g. `Q-30-3 — gate owner / semantic ceiling`), which is what a
literal transcription into the owner cell would carry. Verdict column is
`resolves()` on that literal token; the last column is the accepted rewrite
(probed, §7 controls P2).

| id | lesson line | owner prefix as written | literal verdict | accepted rewrite(s) |
|---|---|---|---|---|
| Q-30-1 | `round-30.md:103` | `operator` | RESOLVES (role-token) | — |
| Q-30-2 | `round-30.md:104` | `parent` | RESOLVES (role-token) | — |
| Q-30-3 | `round-30.md:105` | `gate owner` | **FAILS (unresolved)** | `tools/gates/register-law-gate.py` (live path, probed) or `parent` |
| Q-30-4 | `round-30.md:115` | `parent` | RESOLVES (role-token) | — |
| Q-30-5 | `round-30.md:142` | `parent` | RESOLVES (role-token) | — |
| Q-31-1 | `round-31.md:57` | `orchestrator` | **FAILS (unresolved)** | `parent` (the orchestrator is the goal-mode parent: `reports/round-33/claims.json:7`) or `round-31` |
| Q-31-2 | `round-31.md:58` | `O owner + parent` | **FAILS (unresolved)** | `parent` (validator seat named in the status cell) or `round-30` |
| Q-31-3 | `round-31.md:59` | `parent` | RESOLVES (role-token) | — |
| Q-31-4 | `round-31.md:60` | `parent + validator` | **FAILS (unresolved)** | `parent` or `round-31` |
| Q-32-1 | `round-32.md:55` | `parent/operator` | **FAILS (unresolved)** | `parent` or `operator` |
| Q-32-2 | `round-32.md:56` | `parent` | RESOLVES (role-token) | — |
| Q-32-3 | `round-32.md:57` | `parent` | RESOLVES (role-token) | — |
| Q-32-4 | `round-32.md:58` | `parent` | RESOLVES (role-token) | — |
| Q-32-5 | `round-32.md:59` | `parent` | RESOLVES (role-token) | — |
| Q-32-6 | `round-32.md:60` | `r32 validator` | **FAILS (unresolved)** | `round-32` (round-pointer, probed) or `reports/round-32/completion-ledger.json` |

Score: **9/15 resolve as written, 6/15 go red.** The six are not defects in the
lessons — the lessons are prose records and their `X / Y` prefixes are
descriptive — but they are exactly the class that would flip
`C32_owners_resolve` to FAIL if O02 transcribes them literally. Every accepted
rewrite above was probed green (§7).

Where a compound names two owners, the queue's one-owner-per-row convention
(`README.md:144-146`) forces a choice; the row's **status** cell is the place
for the second owner, not the owner cell — the tool reads only
`| Q-id | question | owner | status |` (`c31-lessons-index-audit.py:138-148`)
and refuses a row that gains cells rather than misreading it (`:394-402`,
selftest control 4b).

## 5. Items in rounds 26–29 that name no Q-id but will need owners if O02 mints rows

The r26–r29 lessons name their open items in prose without ids. If O02 mints
`Q-2{6,7,8,9}-*` rows for them, the owner cell must resolve too; these are the
tokens the lessons themselves name, with resolution probed:

| origin | item (lesson line) | owner token the lesson names | probed verdict |
|---|---|---|---|
| r27 | runner control defects: list-vs-string, null battery parse, shared diphthong bug, moved expectations (`round-27.md:141,194`) | `parent` (admission is the parent's; `round-27.md:194`) | RESOLVES (role-token) |
| r28 | `L9-HOLD` — assembler declares `register_law` in neither `PACKET_KEYS` nor `RECORD_FIELDS` (`round-28.md:50,126`) | `tools/assemble-d4-typed.py` | RESOLVES (path) |
| r28 | `L10-HOLD` — no force vocabulary declared to check against (`round-28.md:50,126`) | `tools/gates/register-law-gate.py` | RESOLVES (path) |
| r29 | defect ledger routes/owners (`round-29.md:87`) | `reports/round-29/defects/ledger.json` | RESOLVES (path) |
| r30 | telemetry producer/consumer split (`round-30.md:115`) | `reports/round-30/telemetry/dispatch-declaration-x37.json` | RESOLVES (path) |

Note the r29 ledger's own owner strings are prose
(`"Owner of tools/gates/register-law-gate.py"`,
`"Round-30 acceptance-runner owner"` — `reports/round-29/defects/ledger.json`,
`entries[].owner`), **none of which resolve** under `resolves()`: they are
defect-ledger vocabulary, not index owner cells, and must not be copied
verbatim into §4. Flagged for O02; not a defect in the ledger.

## 6. Supporting cross-check — the pin source O01 will draw from is stable

Round-32's §Ledger pins (`corpus/lessons/round-32.md:45`) re-measured against
live bytes by this seat: round-26 `60054/222/cae06660`, round-27
`54972/203/f15e285b`, round-28 `50419/145/dd832ff7`, round-29
`17847/118/b6765d33`, round-30 `30665/181/56e77835`, round-31
`16637/73/8870bbdd` → **6/6 MATCH**. Round-32's own file has no claimed pin
live `12879/66/8aacfc2b` (it is the file that would add the seventh row; its
pin is O01/K02's to measure at drafting time). This is a cross-check, not my
leg — the pin cells are O04/K02's verdict.

## 7. Controls — the leg has teeth

All commands read-only, `runpy`-loaded resolver, no file written.

- **P1 (baseline green).** Resolver over the 49 filed §4 rows: `path 37`,
  `role-token 12`, `unresolved []` — reproduces `README.md:211-213`.
- **P2 (rewrites green).** Each §4/§5 accepted rewrite probed: `parent`
  (role-token), `operator` (role-token), `round-30`, `round-31`, `round-32`
  (round-pointer), `tools/gates/register-law-gate.py`,
  `tools/assemble-d4-typed.py`, `reports/round-29/defects/ledger.json`,
  `reports/round-30/telemetry/dispatch-declaration-x37.json`,
  `reports/round-32/completion-ledger.json` (path) — 10/10 RESOLVES.
- **N1 (the six literal tokens fail).** `orchestrator`, `gate owner`,
  `r32 validator`, `parent/operator`, `parent + validator`, `O owner + parent`
  → 6/6 FAILS `unresolved`.
- **N2 (a wrong path fails).** `corpus/lessons/__no_such_file__.md` → FAILS
  (same control the tool's own selftest runs, `c31-lessons-index-audit.py:389-390`).
- **N3 (a nonexistent round pointer fails).** `round-99` → FAILS with class
  `round-pointer`, proving the pointer branch tests `isdir`, not a regex
  (`:160-162`).
- **N4 (the tool's own selftest still green).**
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` →
  `SELFTEST OK: 28/28 checks passed`, exit 0 (2026-10-19T03:5xZ) — including
  `owner path resolves`, `operator token resolves`, `round pointer resolves`,
  `empty owner does not resolve`, `missing path does not resolve`,
  `owner with parenthetical annotation resolves`, and the three `owner_cell`
  malformed-row controls.
- **Baseline for the claim-O threshold.** The filed index at this stamp is
  **red** for the reasons the claim declares, not for owners:
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1,
  `PASS C32_owners_resolve`, `FAIL C31_index_rows_eq_files` (C31-1:
  `['round-26.md'..'round-32.md']`), `FAIL C34b_prose_arithmetic`
  (`stated [26,26]` vs `measured [26,33]`). So C32 is the one leg that is
  **already green and must stay green** across O01/O02's edits: the new rows
  and queue items can only harm it.

## 8. What O02's queue rows must satisfy (checklist for the integrator)

1. Owner cell contains exactly one token, in a form from §1: a live repo path,
   `operator` / `parent` / `lore-shokunin` / `integrator`, or a `round-N`
   pointer whose directory exists. Use the §4 rewrites for the six failing
   items; put the second owner, if any, in the status cell.
2. Backticks are fine (`resolves()` strips them, `:153`); one trailing
   parenthetical is fine; slashes/plus-compounds are not.
3. The row must keep exactly four cells — an unescaped `|` inside the question
   cell makes `owner_cell()` return `""` and the row is reported unresolvable
   (`:138-148`, selftest `:401-402`). A question containing a pipe must escape
   it as `\|` (`README.md:190` precedent: `--profile v2\|v3`).
4. Every `Q-*` id in a §2 row's carried cell must exist in §4 after the delta
   lands (the 15 ids in §3), or the cross-reference dangles.
5. Post-edit control (integrator): re-run the §1 tool and require
   `PASS C32_owners_resolve`, zero `C32-1` findings, `--selftest` 28/28 —
   the claim-O counting command already names this
   (`reports/round-33/claims.json`, claim O `counting_commands[1]`).

## 9. Boundary

Writes: this file only (`reports/round-33/op/O03-owner-checks.md`). No filed
round byte, no `corpus/lessons/*.md`, no README, no tool, no gate was written;
no commit or push; no network. Every probe ran read-only via `runpy` +
`os.path.exists`/`os.path.isdir` with `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`. Independence: all verdicts were produced by this
seat's own resolver calls over live bytes at 2026-10-19T03:54Z; where they
reproduce filed numbers (`README.md:211-213`, `round-32.md:45`) the agreement
is a cross-check, not inheritance.

## Owed

- `reports/round-33/op/O01-row-drafts.md` — not filed at 2026-10-19T03:54Z;
  the integrator must run this table's §2/§3/§6 verdicts against O01's actual
  row cells (pointer, carried ids, pin) and file any mismatch.
- `reports/round-33/op/O02-readme-delta.md` — not filed at the same stamp; the
  integrator must confirm every owner cell in O02's queue-row drafts appears in
  §4's rewrite column, or add a new probed verdict row here.
- `reports/round-33/op/K02-lessons-census.md` — not filed; §6's pin cross-check
  is mine and stays valid without it, but the per-row pin cells remain K02/O04's
  leg.
- The post-integration C32 re-run (checklist §8.5) is the integrator's, on the
  edited README bytes — this seat cannot run it against bytes that do not exist
  yet.

## Citations

- `reports/round-25/audit/c31-lessons-index-audit.py:138-148` (`owner_cell`), `:151-167` (`resolves`), `:158`, `:160-162`, `:164-166`, `:213-227` (C32), `:389-402` (selftest owner controls), `:463` (main guard)
- `corpus/lessons/README.md:67-73`, `:97`, `:144-150`, `:152,157,176,197-199`, `:211-213`, `:309-323`, `:330-334`
- `corpus/lessons/round-26.md:126,141,161-164,192`
- `corpus/lessons/round-27.md:141,186-194`
- `corpus/lessons/round-28.md:50,94,126`
- `corpus/lessons/round-29.md:87`
- `corpus/lessons/round-30.md:103-105,115,142,183`
- `corpus/lessons/round-31.md:57-60,68`
- `corpus/lessons/round-32.md:45,55-60`
- `reports/round-26/validation.json:2`; `reports/round-29/defects/ledger.json` (`entries[].owner`)
- `reports/round-33/claims.json:7` (orchestrator = goal-mode parent), claim O `counting_commands`
- Commands (2026-10-19T03:54Z, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  - `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1; `PASS C32_owners_resolve`; findings C31-1 (7 unindexed) + C34-2 (`stated [26,26]` vs `measured [26,33]`)
  - `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → exit 0, `SELFTEST OK: 28/28`
  - `runpy` + `resolves()` over the 15 new owner prefixes → 9 resolve, 6 fail (listed §4)
  - `runpy` + `resolves()` over 10 rewrites → 10/10 resolve; over 8 negative probes → 8/8 fail
  - `test -e` over 21 candidate disposition pointers → 21/21 EXISTS
  - pin re-measure of `corpus/lessons/round-26..31.md` vs `round-32.md:45` → 6/6 MATCH
  - `grep -c` for the 9 proposed new ids in `README.md` → 0 each (collision-free)
  - `find reports/round-33 -type f` → claims.json, targets.json, telemetry/dispatch-declared.json only
