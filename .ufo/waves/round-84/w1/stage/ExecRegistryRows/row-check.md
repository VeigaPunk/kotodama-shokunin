# ExecRegistryRows — registry census and row audit (round 84, w1)

**Verdict.** At base `81499ee4` the `## Gates and probes` registry holds **74 data
rows** with an **8-cell** header and separator; the instrument set
`reports/round-*/accept-*.py` holds **61** files and **0** are unrowed; **0**
entry-command `.py` tokens are dead; **25** top-level `tools/*.py` carry no row.
The three drafted rows are exactly 8 cells each and add 3 data rows, 2
instruments and 1 tool row. After they land, in the same table, the house
checker must print:

```text
GATE-REGISTRY: 0 missing / 77 registered / 63 instruments / 0 dead
GATE-REGISTRY-INFO: 25 tools without a row
```

with `registered` = data rows (`74 + 3`), `instruments` = `61 + accept-d84 +
accept-o84`, and `unrowed` unchanged at the base 25 because the only new
top-level tool is named by row 1.

## 0. Freeze revision delta — read before pasting

The dispatched brief quoted r0 `3ca2cf288fb593618e0559ea86a36e2dd3110eb8`.
The lane has since moved twice: **HEAD is r2
`7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2`** (committed 2026-11-04 10:31:06),
`reports/round-84/counter-revisions.md` declares r2 current, and
`.ufo/waves/round-84/build-w1.py` plus `spec-v1.json` embed r2. The r0→r2 diff
touches only frozen constants, never a counter code line:

- r1 `e160a72e`: claim D's `decision_heading` `## 2. The decision table` →
  `## 2. Six design decisions` and `anchors_heading` `## 4. Attested anchors`
  → `## 3. Attested anchors`.
- r2 `7e6ee2f8`: claim O's `shape_markers` entry `SOUNDLAW_ERROR:` →
  `SOUNDLAW_ERROR` (label-constant match), plus the `semantics` and
  `min_trace_columns` keys.

The three rows therefore pin **r2**, not the brief's r0: `accept-d84` and
`accept-o84` grade `FROZENCFG` by comparing the `--freeze` `claims.json` bytes
to the lands bytes, so a row pinned to r0 or r1 fails at an r2 lands even
though the counter bytes are identical. If the L1 instead lands the r0 claims
bytes, swap the freeze token in rows 2 and 3 to the landed revision; nothing
else in the rows changes.

Frozen bytes used here (read with `git show <r2>:<path>`):

| path | sha256 at r2 |
|---|---|
| `reports/round-84/accept-d84.py` | `efee17ffca19d8da9d111a0aa1e1a6cdf8685e91cd4f337aa6779bf03b6e3337` |
| `reports/round-84/accept-o84.py` | `cbabd31cbc36c29572487ff86ef803247a7cbe09715157451bbebb12601c9512` |
| `reports/round-84/claims.json` | `279a74dc91c061f186d8eac15424a676e103ad89d34ff0581be28b89abfb4572` |
| `reports/round-84/counterlib.py` | `c3707d1a3de0fa61fa76190190726e110f46b5b793a28aa2438860ae3c8a8ecc` |

`SKILL.md` and `tools/check-gate-registry.py` are byte-identical between base
and r2 (`git diff --quiet 81499ee4..7e6ee2f8 -- SKILL.md
tools/check-gate-registry.py` exits 0 for both), so the base census below is
also the r2 census.

## 1. Independent census at base (commands and raw output)

Run from any directory; no counter or checker code is used for these numbers.

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export LC_ALL=C
B=81499ee45b5751d388fefc78583810878de01ecd

# data rows: all table lines in the section, minus header + separator
git show "$B":SKILL.md \
  | awk '/^## Gates and probes$/{f=1;next} /^## /{if(f)exit} f&&/^\|/{n++} END{print n-2}'
# 74

# header and separator cell counts (first two table lines)
git show "$B":SKILL.md \
  | awk '/^## Gates and probes$/{f=1;next} /^## /{if(f)exit} f&&/^\|/{print; c++; if(c==2)exit}' \
  | awk -F'|' '{print NF-2}'
# 8
# 8

# instrument set
git ls-tree -r --name-only "$B" -- reports \
  | grep -cE '^reports/round-[^/]+/accept-[^/]+\.py$'
# 61

# entry-command cell of every table row (4th field; rows start and end with |)
cells() { git show "$B":SKILL.md \
  | awk '/^## Gates and probes$/{f=1;next} /^## /{if(f)exit} f&&/^\|/' \
  | awk -F'|' '{print $4}'; }

# instruments absent from every entry-command cell
comm -23 \
  <(git ls-tree -r --name-only "$B" -- reports \
      | grep -E '^reports/round-[^/]+/accept-[^/]+\.py$' | sort -u) \
  <(cells | grep -oE 'reports/round-[^/]+/accept-[^/]+\.py' | sort -u) | wc -l
# 0

# dead .py tokens: entry-command paths absent from the base tree
comm -23 \
  <(cells | grep -oE '(tools|reports)/[A-Za-z0-9_./-]+\.py' | sort -u) \
  <(git ls-tree -r --name-only "$B" | sort -u) | wc -l
# 0

# top-level tools with no row
comm -23 \
  <(git ls-tree -r --name-only "$B" -- tools | grep -E '^tools/[^/]+\.py$' | sort -u) \
  <(cells | grep -oE '(tools|reports)/[A-Za-z0-9_./-]+\.py' | sort -u) | wc -l
# 25

# cell-count distribution of the registry table (includes header + separator)
git show "$B":SKILL.md \
  | awk '/^## Gates and probes$/{f=1;next} /^## /{if(f)exit} f&&/^\|/' \
  | awk -F'|' '{print NF-2}' | sort | uniq -c
#      70 8      (header + separator + 68 data rows)
#       6 9      (6 data rows)
```

An independent scratch parser that reads the same blob and tree (not
committed, and not importing the checker) returned the same counts and also
`unrowed_instruments: []`, `dead_tokens: []`, and the six 9-cell row names
below. The house tool on an isolated base export corroborates the same base
state:

```sh
mkdir -p base-export && git archive "$B" | tar -x -C base-export
python3 base-export/tools/check-gate-registry.py --root base-export
# GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead
# GATE-REGISTRY-INFO: 25 tools without a row
# exit 0
```

## 2. Shape audit: 8-cell registry rows versus 11-cell data rows

- `## Gates and probes` header: 8 cells, exactly
  `name | kind | entry command | verdict map | self-test | pinned values |
  write scope | owner`. Separator: 8 cells, every cell matching `:?-{3,}:?`.
- Data rows: 74. Distribution **68 × 8 cells + 6 × 9 cells**. The six 9-cell
  rows are pre-existing (`accept-c-66`, `accept-ca-66`, `accept-o-66`,
  `accept-c-67`, `accept-ca-67`, `accept-o-67`); each carries a literal `|`
  inside its verdict cell, written `PASS|FAIL`, so a naive pipe split yields 9
  cells. This is house data the checker tolerates (`9-cell row tolerated` in
  its selftest); the drafted rows avoid the defect by spelling the alternatives
  as separate backticked strings (`PASS legs=...` / `FAIL legs=...`) and parse
  to 8.
- The **11-cell** shape belongs to a different table:
  `corpus/SOURCES.md` `## Registry` (header at line 28) has 837 rows and
  **837/837 rows carry 11 cells** (`awk -F'|' '{print NF-2}' | sort | uniq -c`
  → `837 11`). The claim-D rows S914–S917 are graded there; the three rows in
  this file are registry rows and must stay 8 cells. No S-id appears in them.
- Drafted rows: 3 lines, each starts and ends with `|`, each parses to exactly
  8 cells, and no cell contains an internal `|` (the cell-count check is the
  pipe check: a leaked pipe would produce 9+ cells). No absolute scratch path
  appears in any cell; the only absolute path is the device sink `/dev/stdout`
  justified in §4.
- Placement matters: the rows must be inserted inside the `## Gates and
  probes` table, before the next `## ` heading (base line 743). Appending them
  at end-of-file puts them under a later section; a scratch simulation did
  that and the checker still read `74 registered` with both new instruments
  missing. Inserting them after the last existing table row produced the clean
  result in §5.

## 3. Dead-token / path resolution for the three rows

| token in a drafted row | at base `81499ee4` | at freeze r2 `7e6ee2f8` | status |
|---|---|---|---|
| `tools/apply-sound-laws.py` | absent | absent | the new claim-O tool; lands with row 1 |
| `reports/round-84/accept-d84.py` | absent | present | frozen counter; row 2 names it |
| `reports/round-84/accept-o84.py` | absent | present | frozen counter; row 3 names it |

The two counters are new relative to the base (they were frozen at r0, after
base), so the assignment's "resolves at base or is the new tool" is met in the
operative form: each `.py` path resolves at base, at the round's frozen
counters commit, or is the new tool. All three must exist at lands; then the
checker's dead-token scan is empty. The non-`.py` example paths
`examples/sound-laws/rules.json`, `examples/sound-laws/proto-lexicon.tsv`,
`examples/sound-laws/expected.tsv` and
`examples/sound-laws/expected-trace.tsv` are likewise absent at base and r2
and land with claim O; the checker only scans `.py` tokens, so they do not
enter its dead list.

## 4. Output sink for `apply-sound-laws`

The frozen contract requires `apply --rules --input --out PATH [--trace
PATH]`, so the gate needs a path that keeps the run read-only for the tree.
`/dev/null` occurs **0** times in `SKILL.md` (`git show "$B":SKILL.md |
grep -c /dev/null` → 0): no gate row uses it, so the drafted row does not
introduce it. The house does run a tool with a device sink —
`python3 tools/d2-typed-labels.py --emit /dev/stdout` appears as a recorded
command in `reports/round-12/recount/` — so **`/dev/stdout`** is the
house-precedented form: it is a real path, it leaves every repo byte untouched,
it keeps the derived TSV observable in the gate's own output, and it needs no
scratch path (which a committed read-only row cannot name). A repo-relative
out path would dirty the tree; a temp path would put an absolute scratch path
in committed text and require cleanup.

Assumption stated for the implementer: the landed tool writes the named
`--out` directly (the contract names no atomic rename). If it stages to a
temporary file and renames, a device sink fails and the row must name a
regular file under a named `--work`, with `scratch` added to the write scope;
the counter's DEMO leg already exercises a regular-file out.

## 5. Post-round `GATE-REGISTRY` lines and why

Base measurement (house tool, base export):

```text
GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead
GATE-REGISTRY-INFO: 25 tools without a row
```

Scratch simulation of the post-round tree (base export + the two frozen
counters + a stub `tools/apply-sound-laws.py`), red before the rows and green
after inserting the three drafted rows at the end of the table:

```text
# before the rows (counters and stub tool present)
GATE-REGISTRY: 2 missing / 74 registered / 63 instruments / 0 dead
GATE-REGISTRY-INFO: 26 tools without a row          # exit 1

# after the rows
GATE-REGISTRY: 0 missing / 77 registered / 63 instruments / 0 dead
GATE-REGISTRY-INFO: 25 tools without a row          # exit 0
```

These are simulations in a disposable export, not a lands verdict; the lands
tree is expected to satisfy the same floors. Why each number moves:

- `registered` is the **data-row count** (`registered_rows` in the checker's
  JSON), not the covered-instrument count: `74 + 3 = 77`. Any additional gate
  row this round can only raise it; 77 is the floor.
- `instruments` is the glob `reports/round-*/accept-*.py`: `61 + 2 = 63`.
  Rows 2 and 3 name both new instruments; the 61 base instruments stay named
  by their existing rows, so `missing` stays 0.
- `dead` stays 0 because every `.py` token in every entry-command cell resolves
  at lands: the 61 base instruments, the two frozen counters, and the new
  tool.
- `tools without a row` counts top-level `tools/*.py` only. Base 25 of 30;
  the new tool makes 31 files and row 1 covers it, so the count stays **25**
  (the claim's `max_unrowed_tools`). A second new top-level tool without a row
  would raise it and must be rowed.
- The claim-O counter's `REGISTRY` leg reads exactly these two lines from its
  materialized lands tree and requires `missing == 0`, `dead == 0`,
  `registered >= 77`, `instruments >= 63`, `unrowed <= 25`
  (`reports/round-84/accept-o84.py` at r0–r2; constants in
  `reports/round-84/claims.json` claim O).

## 6. Boundaries observed

No edit outside `.ufo/waves/round-84/w1/stage/ExecRegistryRows/`; no
`SKILL.md` edit (the L1 lands every byte); no commit, push or mutating
git/jj command; no claim-D 11-cell row text (that is the rows seat's table);
no counter run against a real lands revision (none exists in this wave yet).
