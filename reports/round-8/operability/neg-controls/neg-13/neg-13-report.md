# neg-13 — negative control + repair receipt (shard R8-O13, defect index 9 = review 26 §3 D9)

- **Round:** 8 (loop 1 of 3, build 1 of 4) · **shard:** R8-O13 (operability, claim O)
- **neg-control dir:** `reports/round-8/operability/neg-controls/neg-13/`
- **Date:** 2026-10-17. Consolidated control runs: D9 post-fix `run_at_utc = 2026-10-17T20:28:41Z`
  (header of `evidence-control-postfix.txt`); fail-before and extra-control headers in their own files.
- **Baseline:** declared `e7ca0faeb6680fa9891b907be628d9db578c28f4` (`reports/round-8/claims.json`);
  worktree `HEAD = cf338a713060f274269cdacb18cdc0085bb06aeb` (`git rev-parse HEAD`).
- **Role:** repair shard. Writes only my hunks in `tools/gates/naming-collision-gate.py`
  (the D9 validator), this directory, and this report. No commit, no push.
- **Assigned defect:** "defect index 9" (dispatch). Index convention is derived from sibling
  receipts below, not assumed.

## 0. Defect selection (dependency status and index derivation)

`reports/round-8/operability/defect-inventory.json` (R8-O03's artifact) did **not** exist when
this shard started — `ls reports/round-8/operability/` at 20:12–20:16 UTC showed only
`battery-rerun.json`, `o01-diagnosis.md`, `o02-fix.md` and `neg-controls/`. Per the shard fallback
("if inventory lands late, fall back to the two named reviews directly") both named reviews were
read in full: `reports/supplement-opencode-1/26-parser-controls.md` (§3 register D1–D10) and
`reports/supplement-opencode-1/29-local-boundaries.md` (F1–F6).

**Index assignment: 1-based register order over review 26 §3 D1…D9, then review 29's selftest
defects.** Sibling receipts fix the convention:

- `neg-04-report.md` §0: "The first defect in register order is review 26 §3 D1 … so this shard
  owns D1" → index 1 = D1.
- `neg-07-report.md` §0: "so defect index 3 = review 26 §3 D3 … 1-based register order" → index 3 = D3.
- `neg-09` (probe docstring): index 5 = D5; `neg-10-control.py`: "defect index 6 = review 26 §3 D6";
  `neg-11-report.md` §0: "defect index 7 = review 26 §3 D7"; `neg-12/.scratch/` (in flight at write
  time) is the D8 ReDoS payload set → index 8 = D8.

Therefore **defect index 9 = review 26 §3 D9** (`formation.output` str.format template that reaches
into objects; `tools/gates/naming-collision-gate.py`). D10 is explicitly "note, not a defect"
(`26-parser-controls.md:175-181`), so the register continues with review 29's selftest defects
(index 10 = F1 — see §5).

**Inventory landed after dispatch.** Poll found it at 20:22 UTC. Later revision inspected
(sha256 `c20a57fede1049280f5c59d8237d42d364c2ef45d74455e141ce962b3c9d5f10`; an earlier revision
`a56b8b63…` is quoted in `neg-11-report.md` — the inventory was revised during the round). Its
per-file `idx` field enumerates defects per file, so its `idx 13 = R26-D9` is this shard's defect
(file `tools/gates/naming-collision-gate.py`, severity `low`, `suggested_control`: "packet with
output '{stem.__class__}' -> assert no interpreter-internal rendering … fail-before = \"<class
'str'>\" echoed"). Its `status_working_tree` still reads `present_in_working_tree`, which predates
this shard's repair.

## 1. Defect and pre-fix reproduction

Review 26 §3 D9 (`26-parser-controls.md:159-162`): "`formation.output` is a packet-controlled
`str.format` template that reaches into objects — `:1300-1324` `output.format(**match.groupdict())`
with `output: "{stem.__class__}"` produced `… yields "<class 'str'>" …` in the finding text. No code
execution is possible (`str.format` has no call syntax), but interpreter internals are reachable
from packet text and are echoed into the report; `{stem.__class__.__mro__}`-style templates are
accepted packets."

Pre-fix code path: `_gate_c` resolved the template with `replayed = output.format(**match.groupdict())`
and caught only `(KeyError, IndexError)`.

Pre-fix reproduction (`--from-git e7ca0fa`; gate sha256 `8c5afb0a5abc8b00…` = the review 26 §0 pin,
so the bytes are also the declared baseline's; full transcript in `evidence-control-prefix.txt`):

| payload `formation.output` | pre-fix rc | pre-fix finding | rendered value in the report |
|---|---|---|---|
| `{stem.__class__}` | 1 | DERIV-REPLAY FAIL | `yields "<class 'str'>"` |
| `{stem.__class__.__mro__}` | 1 | DERIV-REPLAY FAIL | `yields "(<class 'str'>, <class 'object'>)"` |
| `{stem[0]}` | 1 | DERIV-REPLAY FAIL | `yields 't'` |
| `{stem!r}` | 1 | DERIV-REPLAY FAIL | `yields "'tal'"` |
| `{stem:>8}` | 1 | DERIV-REPLAY FAIL | `yields '     tal'` |
| `{stem}in{` | 1 | *(no finding — traceback)* | uncaught `ValueError` at pre-fix `:1720` |

The last row is an adjacent pre-fix defect found while building the control (a malformed template
crashed the gate instead of producing a finding); the same validator repairs it.

## 2. Repair

`tools/gates/naming-collision-gate.py` (worktree, uncommitted; the file also carries sibling
shards' D3/D4/D8 hunks, which are not mine):

- `import string` (line 112);
- `_TEMPLATE_FIELD_RE` + `_template_problem(template, group_names)` (line 1259, after
  `_match_with_budget`): parses the template with `string.Formatter().parse` and returns a
  diagnostic for the first placeholder that leaves the subset;
- wiring in `_gate_c` (line 1490): the diagnostic is emitted as a stable
  `DERIV-HOLD` HOLD finding — `output template is outside the accepted subset (<reason>); replay is
  not possible` — and the template is **never rendered**;
- docstring bullet "Gate C output template" (line 69).

Accepted subset: plain `{name}` placeholders naming the pattern's named groups. Refused: attribute
access (`{stem.__class__}`), indexing (`{stem[0]}`), conversions (`{stem!r}`), format specs
(`{stem:>8}`, including nested spec fields), positional fields (`{}`, `{0}`), fields naming no
group, and malformed braces. Escaped literal braces (`{{…}}`) remain allowed (they render a
literal, no field). Exit-code contract unchanged (0 clean / 1 findings / 2 could-not-evaluate);
this defect is a content finding, not a parse failure, so it is a HOLD finding, not exit 2.

Post-repair digest: `tools/gates/naming-collision-gate.py` sha256
`d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`.

## 3. Evidence

Control: `neg-13-control.py` (sha256 `b1bd044ba31ce1de…`), 8 checks. Isolation: payloads are written
only into a scratch temp dir; the gate runs as a subprocess; the repository is never written by the
control.

| run | command | exit | result | transcript |
|---|---|---|---|---|
| post-fix, live tree | `python3 .../neg-13/neg-13-control.py` | 0 | `NEG-13 RESULT: PASS (8/8 checks)` | `evidence-control-postfix.txt` (sha256 `8294189458a56957…`) |
| fail-before, `e7ca0fa` bytes | `python3 .../neg-13/neg-13-control.py --from-git e7ca0fa` | 1 | `NEG-13 RESULT: FAIL (6/8 checks)`, each failure naming `PRE-FIX PATTERN OBSERVED` | `evidence-control-prefix.txt` (sha256 `3ba9ecdd0fa8c3a2…`) |

Post-fix checks: attribute access, attribute chain, indexing, conversion, format spec → exit 1 with
only `DERIV-HOLD` and "outside the accepted subset", no `<class` substring; malformed `{stem}in{` →
stable `DERIV-HOLD`, no traceback; plain `{stem}in` on a matching name → exit 0 clean; plain
`{stem}in` on a mismatching name → still `DERIV-REPLAY` naming the replayed form.

Harness re-verification after the repair (all run on this date in the live tree):

- `python3 tools/gates/naming-collision-gate.py --selftest` → exit 0,
  `selftest: OK — fixture findings 12 across 11 ids (…); positive control clean; malformed inputs exit 2; missing profile held; case policy routed`.
- `python3 tools/check-gate-battery.py --selftest` → exit 0, `SELFTEST OK 10/10 controls behaved as expected`.
- `python3 tools/check-gate-battery.py` → exit 0, summary `pass 7 / fail 0 / unevaluable 0`, originals preserved.
- `python3 tools/check-craft-exercise.py --selftest` → exit 0, `10/10 tamper cases detected`, `18/18 cases passed`.

## 4. Limits

- The subset is a deliberate minimal choice: conversions and format specs cannot reach interpreter
  internals for a `str`, but they are refused anyway so the template language stays auditable.
- A field must name a group of the *matched* pattern; a field naming another group is refused
  (pre-fix that raised `KeyError` → DERIV-HOLD, so no behavior regression for that case).
- Only the `formation.output` path was audited; other packet-text→finding-text paths were not swept
  by this shard (D9 covers this one site).
- The inventory's `status_working_tree` for `R26-D9` predates this repair.
- The control's scratch root is chosen by free space (`--scratch-root` / `NEG13_SCRATCH_DIR`
  override) because the shared default temp dir hit ENOSPC under the 64-worker load during this
  round.

## 5. Extra: index-10 (review 29 F1) fixture-pin repair — unassigned work shipped here

Before the index convention above was pinned (inventory still absent), this shard had built the
review 29 §F1 defect repair. It is kept, clearly labeled as extra, because claim O's after-required
names "the legacy assert-based/fixture-writing selftest … defects from supplemental reviews 26/29"
and no O-shard directory existed for index 10 at write time.

- **Defect:** five of seven gate selftests rewrote their committed fixtures in place with a
  truncating `open(..., "w")` write, so tampering was silently erased and the write was non-atomic
  (review 29 §F1).
- **Repair:** each of the five writer gates (`phonology-sanity-gate.py`, `myth-consistency-gate.py`,
  `lexicon-coverage-audit.py`, `costume-era-consistency-gate.py`, `provenance-audit.py`) now pins
  the committed fixture to the embedded constant: a present file is verified byte-for-byte, a
  divergent file fails loudly with `SELFTEST FAIL: … diverges from the embedded constant; refusing
  to overwrite` and is left untouched, and a missing file is regenerated atomically
  (temp file + `os.replace` + fsync). Docstrings/messages that described the old rewrite behavior
  were updated in the same files.
- **Control:** `extra-index10-fixture-pin-control.py` (sha256 `7c2622874b0e2473…`), 17 checks
  (clean=no writes incl. mtime; tamper=refused + preserved; absent=atomic byte-identical
  regeneration; naming/handoff reader gates still fail loudly on tamper).
- **Evidence:** post-fix exit 0 `PASS (17/17)` → `evidence-extra-f1-postfix.txt`
  (sha256 `58a1abce91e66592…`); fail-before `--from-git e7ca0fa` exit 1 `FAIL (10/17)`, each
  failure naming `PRE-FIX PATTERN OBSERVED` (silent erasure ×5, in-place rewrite ×5) →
  `evidence-extra-f1-prefix.txt` (sha256 `cf8a4a5c9f4ee5a9…`). Batteries after this repair are in
  §3 (all green).
- **Recommendation to the orchestrator:** credit this as index 10 if it is unassigned, or drop it —
  it is uncommitted, localized to the five selftest heads/docstrings, and every affected selftest
  and battery stays green either way.

## 6. Files written

- `reports/round-8/operability/neg-controls/neg-13/neg-13-control.py` (sha256 `b1bd044b…`)
- `reports/round-8/operability/neg-controls/neg-13/extra-index10-fixture-pin-control.py` (sha256 `7c262287…`)
- `reports/round-8/operability/neg-controls/neg-13/evidence-control-postfix.txt` (`82941894…`)
- `reports/round-8/operability/neg-controls/neg-13/evidence-control-prefix.txt` (`3ba9ecdd…`)
- `reports/round-8/operability/neg-controls/neg-13/evidence-extra-f1-postfix.txt` (`58a1abce…`)
- `reports/round-8/operability/neg-controls/neg-13/evidence-extra-f1-prefix.txt` (`cf8a4a5c…`)
- `reports/round-8/operability/neg-controls/neg-13/neg-13-report.md` (this file)
- repair hunks in `tools/gates/naming-collision-gate.py` (D9) and, as the documented extra, in
  `tools/gates/{phonology-sanity-gate,myth-consistency-gate,lexicon-coverage-audit,costume-era-consistency-gate,provenance-audit}.py`
