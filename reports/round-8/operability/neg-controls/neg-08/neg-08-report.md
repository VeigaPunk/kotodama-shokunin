# neg-08 — negative control + repair receipt (shard R8-O08)

- **Round:** 8 · **shard:** R8-O08 (operability) · **claim:** O
- **Assignment (verbatim):** "OPERABILITY R8-O08: defect index 4, same protocol as
  R8-O04. neg-controls/neg-08/."
- **Date:** 2026-10-17 · `checked_at_utc = 2026-10-17T20:29:18Z` (all commands below
  were run in this window; each receipt file in this directory carries its own run)
- **Baseline:** declared `e7ca0faeb6680fa9891b907be628d9db578c28f4`
  (`reports/round-8/claims.json`); worktree `HEAD = cf338a713060f274269cdacb18cdc0085bb06aeb`.
  Pre-fix bytes for both controls are taken from `cf338a7` by `git show`, and their
  sha256 values equal the review-26 §0 pins, so the controls bind to the declared
  baseline.
- **Role:** repair/verification shard. Writes only the repaired naming-gate hunks
  (§2), this directory, and this report. No commit, no push. Live fixtures were not
  touched (`git status --short tools/gates/fixtures/` → empty at write time; all
  selftest runs went through `tools/check-gate-battery.py`, which mirrors the tree).

## 0. Defect selection — the index space is read two ways by sibling shards

The inventory (`reports/round-8/operability/defect-inventory.json`) did **not**
exist when this shard started:

```
$ ls -la reports/round-8/operability/          # 2026-10-17T20:12Z
ls: cannot access 'reports/round-8/operability/': No such file or directory
```

Per the shard protocol ("if absent, read the two reviews directly and take the
Nth defect you confirm"), the two named reviews were read
(`reports/supplement-opencode-1/26-parser-controls.md`,
`29-local-boundaries.md`). Under that fallback reading — index N = the Nth defect
in register order, which is what sibling shards used — **index 4 = review 26 §3
D4 (boolean coercion re-renders authored forms)**; that repair and its control are
§2/§3.2 below.

The inventory landed at 20:23Z (`ls -la` showed `defect-inventory.json`, 31424 B).
Its 0-based list position 4 is a *different* defect:

```
$ python3 -c "import json; d=json.load(open('reports/round-8/operability/defect-inventory.json'));
> print(d[4]['idx'], d[4]['defect_id'], d[4]['file'])"
5 R26-D2-lexicon tools/gates/lexicon-coverage-audit.py
```

Sibling shards read the same assignment template in three different spaces —
this is a finding for the parent, not a preference of this shard:

| shard | assigned index | defect it shipped | space it used | source |
|---|---|---|---|---|
| R8-O04 | 0 | R26-D1 (unterminated flow) | inventory position 0 | `neg-04/neg-04-report.md` §0 |
| R8-O05 | 1 | R26-D2-phonology (dup keys) | inventory position 1 (0-based) | `neg-05/neg-05-report.md:28` ("index 1 (0-based; `idx: 2` …) = `R26-D2-phonology`") |
| R8-O07 | 3 | R26-D2-naming (+ D3) | inventory `idx` 3 (1-based → position 2) | `neg-07/neg-07-report.md` ("defect index 3 … = `R26-D2-naming`") |
| R8-O09 | 5 | review 26 §3 D5 (tabs/multi-doc) | register order, 1-based | `neg-09/probe-prefix.py:2` |
| R8-O10 | 6 | review 26 §3 D6 | register order | `neg-10/neg-10-control.py:2` |
| R8-O11 | 7 | review 26 §3 D7 | register order | `neg-11/neg-11-report.md:1` |
| R8-O12 | 8 | review 26 §3 D8 | register order | `neg-12/neg-12-control.py:2` |
| R8-O13 | 9 | review 26 §3 D9 (+ index 10 = R29 F1 as extra) | register order | `neg-13/extra-index10-fixture-pin-control.py:2` |

This shard therefore delivered **both readings**, so the assignment is satisfied
whichever space the parent intended:

1. **Assigned index 4 = `R26-D2-lexicon`** (inventory position 4): verified repaired
   in the working tree, with the isolated fail-before/pass-after control
   `neg-08-control.py` (§1, §3.1). The repair hunks were **already present** when
   this shard started — I did not author them (see §1.2) — so the contribution here
   is the independent verification and the missing control.
2. **Index 4 = review 26 §3 D4** (fallback/register reading): repaired by this shard
   in `tools/gates/naming-collision-gate.py` with its own control
   `neg-08-d4-control.py` (§2, §3.2).

Coverage observed at 20:29Z (inventory positions with a filed control):
0 (`neg-04`), 1 (`neg-05`), 2 (`neg-07`), 4 (this shard), 6 (`neg-07-d3-control`),
7 (this shard), 8 (`neg-09`), 9 (`neg-10`), 10 (`neg-11`), 11 (`neg-12`),
14 (`neg-13` extra). **No control seen at that moment** for positions 3
(`R26-D2-costume`), 5 (`R26-D2-myth`), 12 (`R26-D9`), 13 (`R26-D10`), 15–19
(review-29 items other than F1) — although the position 3/5 *repairs* were already
live (probes below), so that gap was a control gap, not a repair gap. By the
acceptance run at 20:32Z the gap had closed for the required ids: `neg-06/` landed
(costume, D2) and `reports/round-8/validation.json` records
`required_review_ids = [D1…D9, F1, F5]`, `repaired = [D1…D9, F1, F5]`,
`unrepaired = []`, `uncovered_required = []`, with `uncovered_optional =
[D10, F2, F3, F4, F6]` (the D10 coverage note and the review-29 items this shard
does not own).

```
$ # evidence-residual-probes.txt (2026-10-17T20:29Z, live worktree)
costume block-dup (position 3)   rc=2 FINDING G-DATA: … duplicate key 'costumes'
costume flow-dup                 rc=2 FINDING G-DATA: … duplicate key 'a' in flow mapping
myth flow-dup (position 5)       rc=2 FINDING G-DATA: duplicate key 'consonants'
myth block-dup                   rc=2 FINDING G-DATA: duplicate key 'phonology'
```

## 1. Assigned defect `R26-D2-lexicon` (index 4)

### 1.1 Defect and pre-fix reproduction

Inventory entry (position 4, `idx` 5): *"D2: duplicate keys silently last-win in
block mappings and on the JSON path (`json.loads` without `object_pairs_hook`)"*,
file `tools/gates/lexicon-coverage-audit.py`, severity high, evidence pointer
review §3 D2 (cited `:465`; JSON `:498-503`), suggested control *"assert exit 2 /
duplicate-key error for the JSON dup and YAML block dup; fail-before = silent
`[{'term':'b'}]`"*.

Fresh pre-fix receipt (`evidence-lexicon-prefix.txt`, control run against
`git show cf338a7:tools/gates/lexicon-coverage-audit.py`, sha256
`63ee4ec6…` = review-26 §0 pin):

```
NEG-08 json-duplicate-key-rejected          rc=1 FAIL
NEG-08 block-duplicate-key-rejected         rc=1 FAIL
NEG-08 flow-duplicate-key-rejected          rc=2 FAIL   ("'lexicon' must be a list of entries" — the duplicate was never named)
NEG-08 nested-duplicate-key-rejected        rc=1 FAIL
NEG-08 quoted-plain-key-collision-rejected  rc=1 FAIL
NEG-08 RESULT: FAIL (5/9 checks)
```

i.e. the pre-fix gate evaluated the duplicate-key packet (last key winning) with
no duplicate diagnostic — the defect the review and the inventory both recorded.

### 1.2 Working-tree state (attribution)

The duplicate-key rejection is present in the live gate (observed 20:26–20:29Z;
`sha256(tools/gates/lexicon-coverage-audit.py) = 2c4dd397…`, not the review pin):

```
$ grep -n "duplicate key\|object_pairs_hook" tools/gates/lexicon-coverage-audit.py
370: raise PacketError("duplicate key %r in flow mapping" % flow_key)
492: raise PacketError("duplicate key %r" % key)          # block mapping
530: def _json_object_no_duplicates(pairs):
544: return json.loads(stripped, object_pairs_hook=_json_object_no_duplicates)
```

Those hunks are **not this shard's work**: they were already in the worktree when
R8-O08 started (this shard's first diff of the file, 20:14Z, already showed the
flow-mapping check and the JSON hook). Attribution to a sibling shard (the
lexicon gate was being edited concurrently by the D3/D6 sweep); this shard verified
them and ships the isolated control the claim requires. Post-fix receipt
(`evidence-lexicon-postfix.txt`):

```
NEG-08 json-duplicate-key-rejected          rc=2 PASS
NEG-08 block-duplicate-key-rejected         rc=2 PASS
NEG-08 flow-duplicate-key-rejected          rc=2 PASS
NEG-08 nested-duplicate-key-rejected        rc=2 PASS
NEG-08 quoted-plain-key-collision-rejected  rc=2 PASS
NEG-08 guard-clean-json-evaluates           rc=1 PASS
NEG-08 guard-clean-yaml-equals-json         rc=1 PASS
NEG-08 guard-repeated-keys-across-entries-ok rc=1 PASS
NEG-08 guard-tab-indentation-still-exit-2   rc=2 PASS
NEG-08 RESULT: PASS (9/9 checks)
```

## 2. Secondary repair: review 26 §3 D4 (index 4 under the register reading)

### 2.1 Defect and pre-fix reproduction

Review §3 D4: `_parse_scalar` maps `true|yes|false|no` (any case) to `bool` and
`_s()` renders booleans back as `"true"`/`"false"`, so a form-bearing field is
audited as a form the packet never authored. Fresh receipt
(`prefix-receipt.txt`, 20:20Z, pre-edit worktree
`sha256(db3cee7c…)`):

```
--- unquoted-no rc=1
    FINDING PHON-INVENTORY: FAIL — name N1 'false': symbol /f/ at position 1 is not in the declared inventory …
--- quoted-no rc=1
    FINDING CROSS-HOLD: HOLD — …
--- unquoted-007 rc=1
    FINDING PHON-INVENTORY: FAIL — name N1 '7': symbol /7/ at position 1 …
--- quoted-007 rc=1
    FINDING PHON-INVENTORY: FAIL — name N1 '007': symbol /0/ at position 1 …
```

The quoted twin of the same authored token audits differently, and `007` loses its
leading zeros — both are the review's counterexample class.

### 2.2 Repair (this shard's hunks in `tools/gates/naming-collision-gate.py`)

Typing is now scoped to the keys the gate actually reads as typed values; every
other scalar keeps its authored text (quoted scalars stay text in every position,
typed keys included):

- new constant `_TYPED_KEYS` (post-edit line 218): `enabled`, `onset_clusters`,
  `adapted`, `opaque`, `compare_only` → `"bool"`; `max_distance` → `"number"`.
- `_parse_scalar(text, typed=None)` (line ~226): the `true/yes/false/no` and
  integer/float coercions now run only when `typed` matches; the `&*!` subset
  rejection and quote handling are unchanged.
- `_parse_value(text, typed=None)` (line ~375) forwards `typed`;
  `_parse_flow` passes `_TYPED_KEYS.get(key)` for flow-mapping values (line 394);
  `_parse_map` does the same for block-mapping values (line 483). Flow-sequence
  items and sequence scalars stay untyped by design — those positions are forms.

Verified still present at 20:29Z (`grep -n "_TYPED_KEYS"` → lines 218, 394, 483)
although the file moved under this shard (siblings are editing the same file:
digests observed in sequence `db3cee7c` pre-edit → `244f103d` post-edit →
`eb12cac2` → `a624a476` → `e4acaf56` → `d9e4e8f4`). Post-edit receipt
(`postfix-receipt.txt`): authored `no`/`yes`/`007` audit identically to their
quoted twins, and `id: 007` renders as authored.

## 3. Negative controls

### 3.1 `neg-08-control.py` — assigned defect (index 4 = `R26-D2-lexicon`)

Contract: pointed at the live gate every check passes (exit 0); pointed at pre-fix
bytes (`--pre-fix-from-git cf338a7`) the duplicate-key checks observe the pre-fix
pattern and the control exits 1, naming it. Checks: JSON dup, block dup, flow dup,
nested dup, quoted/plain key collision (all must exit 2 naming `duplicate key`);
guards: clean JSON evaluates, clean YAML equals its JSON twin, the same key in
sibling entries is not a duplicate, tab indentation still exits 2.

```
$ python3 neg-08-control.py                      # exit 0, PASS (9/9)   → evidence-lexicon-postfix.txt
$ python3 neg-08-control.py --pre-fix-from-git cf338a7   # exit 1, FAIL (5/9) → evidence-lexicon-prefix.txt
```

### 3.2 `neg-08-d4-control.py` — secondary repair (D4)

Contract: pointed at the live gate every check passes (exit 0); pointed at pre-fix
bytes the authored-form checks observe the pre-fix pattern and the control exits 1.
Checks: authored `no`/`yes`/`007` names and an authored `007` id must audit
identically to their quoted twins and never render as `false`/`true`/`7`; guards:
`enabled: false`, `opaque: true`, `max_distance: 0` still act as typed booleans/
numbers, a non-boolean token on a typed key does not crash, tab indentation still
exits 2.

```
$ python3 neg-08-d4-control.py                   # exit 0, PASS (11/11) → evidence-postfix-live.txt
$ python3 neg-08-d4-control.py --pre-fix-from-git cf338a7  # exit 1, FAIL (4/11) → evidence-prefix-git.txt
```

Isolation (both controls): payloads are written only into a scratch directory
(system temp, with a local fallback — see §5.3); the gate runs as a subprocess;
nothing under the repository is written; the git-materialised pre-fix copy lives
only in the scratch directory.

## 4. Selftests and the registered battery (after this shard's edit)

`evidence-battery.txt` (single run, 20:29Z):

```
$ python3 tools/gates/naming-collision-gate.py --selftest
selftest: OK — fixture findings 12 across 11 ids (CROSS-HOLD, DERIV-AFFIX, DERIV-HOLD,
DERIV-REPLAY, NAME-LEXEME, NAME-NEAR, NAME-REUSE, NAME-VISUAL, PHON-CODA,
PHON-INVENTORY, PHON-ONSET); positive control clean; malformed inputs exit 2;
missing profile held; case policy routed
exit=0
$ python3 tools/check-gate-battery.py --selftest
SELFTEST OK 10/10 controls behaved as expected
exit=0
$ python3 tools/check-craft-exercise.py --selftest
SELFTEST OK 10/10 tamper cases detected
CLI-SELFTEST OK 18/18 cases passed
exit=0
```

The battery's own contract makes its exit 0 the statement that all seven gate
selftests passed **in a mirrored copy** and the live gate tree was preserved
(`tools/check-gate-battery.py` docstring); the lexicon selftest was deliberately
not run on the live tree because that gate is one of the five fixture-writing
selftests (review 29 F1). `evidence-battery-gates.txt` is the same battery run
alone, and `evidence-digests.txt` records the sha256 of every artifact in this
directory plus both gate digests at the same timestamp (`generated
2026-10-17T20:30:53Z`; final control re-runs at that time: both exit 0).

## 5. Quarantine and limits (explicit)

1. **Cross-gate legs of D4 are quarantined, not repaired.** Review §3 D4 also
   records per-gate typing divergence (myth coerces `on|off`, phonology coerces
   `true|false`). Reason for quarantine: (a) the reproduced counterexample and the
   inventory's `file` field for `R26-D4` name the naming gate; (b) both files were
   being edited concurrently by sibling shards at the time (D3/D5/D6 sweep), and a
   second writer on them risks clobbering a sibling's repair; (c) probes with the
   strongest available payloads found no *observed* re-rendered form in those gates
   (`evidence-crossgate.txt`: phonology `names[].name: true` → rc=0, no name
   finding; myth `roles[].role: no|true` → no rendering; lexicon `term: true` →
   rendered as authored). The residual is the divergence itself, marked
   **to-verify** for a follow-up round with a shared typing table.
2. **This shard does not own review 29's fixture-writing class** (`R29-F1a/b/c`) —
   shard R8-O13 filed controls for it (`neg-13/`); noted here only as a boundary.
3. **Environment note (affects reproducibility).** `/tmp` hit inode exhaustion
   during this batch (`df -i /tmp` → `IUsed 1048576, IFree 0, IUse% 100` at
   20:16Z; a `mkdir /tmp/...` failed with "No space left on device" while ~8.5 GB
   of space remained). Both controls therefore fall back to a scratch directory
   next to themselves if the system temp cannot be created; receipts show
   `/var/tmp/...` paths for the git-materialised pre-fix copies.
4. **Race note.** `tools/gates/naming-collision-gate.py` was edited by several
   shards while this one ran (five digests observed, §2.2). The control run in
   §3.2 pins the digest it tested; if integration rewrites the file, re-run
   `neg-08-d4-control.py` — it exits non-zero the moment the authored-form
   preservation is gone.
5. **Not tested here:** the other four gates' duplicate-key handling as *repairs*
   (only probed, §0); JSON path of the costume/lexicon gates beyond the probes;
   no fuzzing or complexity screen (review §3 D8 is shard R8-O12's).

## 6. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 reports/round-8/operability/neg-controls/neg-08/neg-08-control.py
python3 reports/round-8/operability/neg-controls/neg-08/neg-08-control.py --pre-fix-from-git cf338a7
python3 reports/round-8/operability/neg-controls/neg-08/neg-08-d4-control.py
python3 reports/round-8/operability/neg-controls/neg-08/neg-08-d4-control.py --pre-fix-from-git cf338a7
python3 tools/check-gate-battery.py --selftest
python3 tools/check-craft-exercise.py --selftest
```

## 7. Files in this directory

| file | content |
|---|---|
| `neg-08-control.py` | control for the assigned defect (index 4 = `R26-D2-lexicon`) |
| `neg-08-d4-control.py` | control for the secondary repair (`R26-D4`) |
| `evidence-lexicon-postfix.txt` / `evidence-lexicon-prefix.txt` | §3.1 runs |
| `evidence-postfix-live.txt` / `evidence-prefix-git.txt` | §3.2 runs |
| `prefix-receipt.txt` / `postfix-receipt.txt` | raw D4 before/after reproductions (§2) |
| `evidence-battery.txt`, `evidence-battery-gates.txt` | §4 runs |
| `evidence-digests.txt` | sha256 of every artifact here + both gate digests (20:30:53Z) |
| `evidence-crossgate.txt` | §5.1 cross-gate probes |
| `evidence-residual-probes.txt` | §0 coverage probes (costume/myth dup handling) |
