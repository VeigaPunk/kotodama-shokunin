- Seat: C15 | scribe | claim C | date 2026-10-19 | baseline 4a7aede

# C15 — coverage receipt draft: claim C before→after with the counting commands

**Assignment** (`reports/round-35/targets.json:163-167`, seat C15): "Coverage receipt draft:
before->after with the counting commands." Out path: `reports/round-35/cov/C15-receipt.md`.
Binding shared rules read at `reports/round-35/targets.json:5-13` — `:6` write only the assigned
out path, `:8` new corpus entries are drafted as fenced blocks and landed by the integrator only,
`:10` **never** execute any `reports/round-*/run-validation.py` in-tree (F-C13-1 prevention),
`:12` missing dependency → do what you can, record the owed path.

**Status: DRAFT.** Every *before* figure below is a live measurement taken by this seat in the
window named below. The *after* side is (a) the declared target (`reports/round-35/claims.json:29`)
and (b) a read-only assertion block (§4) whose negative control was executed at the before state —
the after-legs are shown to be able to fail, so a green run of that block after landing is a real
reading, not a green-by-construction self-test. Nothing was landed by this seat: no corpus entry,
no README byte, no tool byte. No round runner was executed anywhere.

**Measurement window.** 2026-10-19 (in-session), lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. `git rev-parse HEAD` →
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (matches `reports/round-35/claims.json:9-10`); `git status --porcelain
corpus/` → empty, so the working tree is byte-identical to HEAD for every corpus path measured here.

## 1. Claim under receipt

`reports/round-35/claims.json:21-35` — claim **C**, axis **coverage**:

| field | `reports/round-35/claims.json` | content |
|---|---|---|
| claim | `:24` | expand the two thinnest knowledge partitions with ten new sourced entries: +6 culture-material (18 → 24) and +4 myth-symbol (19 → 23), each gap-named, frontmatter-complete, decision-record carrying, source-resolving; README index reconciled to the new counts |
| before | `:26-27` | `linguistics 21 / myth-symbol 19 / culture-material 18 / synthesis 29 / verification 20 / civilizations 94 = 201 files` |
| after_required | `:29` | `culture-material 24, myth-symbol 23, total 211`; every new entry passes the entry audit; README partition counts and index rows reconciled by the counting command; zero fabricated sources |
| counting commands | `:31-33` | (1) per-partition `ls … \| wc -l` loop; (2) `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`; (3) `python3 reports/round-35/run-validation.py` |
| thresholds | `:35` | 10/10 new entries audited clean (two independent auditors); README counts == live census; inventory total 211 |

This receipt owns the **counting** legs of that claim only. Entry quality (frontmatter 4/4,
resolving source pointers, decision record, gap statement) is C13/C14/C17's and R01/R02's evidence;
the README delta is C11's draft.

## 2. Before — measured live at `4a7aede`

### 2.1 Counting command 1 — per-partition census (verbatim, `reports/round-35/claims.json:31`)

```sh
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21
19
18
29
20
94
$ find corpus/knowledge -name "*.md" -type f | wc -l
201
```

The loop order is the one `reports/round-35/claims.json:26` uses, and it is the same order the README footer vector
uses (`corpus/README.md:473` = `21/19/18/29/20/94`), i.e. index 0 is `linguistics`. The totals line
agrees with `reports/round-35/claims.json:27` (`total` 201) and with the README totals line (`corpus/README.md:469`).

### 2.2 Counting command 2 — inventory (verbatim shape, `reports/round-35/claims.json:32`)

```sh
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# exit 0; "schema": "kotodama-source-audit-inventory/1"; totals.files = 201
# (full JSON ~107 kB; the per-file rows are the tool's own output, not reproduced here)
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge \
  | python3 -c "import json,sys,collections;d=json.load(sys.stdin);c=collections.Counter(f['path'].split('/')[0] for f in d['files']);print('totals.files', d['totals']['files'], '| per-dir', [c[p] for p in ['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']])"
totals.files 201 | per-dir [21, 19, 18, 29, 20, 94]
```

The second command is this seat's derivation over the tool's own `files[].path` rows (the tool does
not print a directory vector); it is a **cross-method agreement leg**: the `ls`-based census (§2.1)
and the inventory-based count give the identical vector at `4a7aede`. The inventory counts markers,
not verified facts (`corpus/README.md:474`), and a marker count is not a quality score
(`corpus/README.md:473`-adjacent caveat block).

### 2.3 State pins (so the before state is recoverable, not asserted)

| pin | value | command |
|---|---|---|
| baseline commit | `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` | `git rev-parse HEAD` |
| corpus tree object | `751aa21c4b4d638c49fbd3269774d25c1d1e6d7a` | `git rev-parse HEAD:corpus/knowledge` |
| sorted path-manifest digest | `d2639fd67d4ad9330288de9dabad070a67e837bca07f44b764d178eeae50807f` | `git ls-tree -r --name-only 751aa21c… \| sort \| sha256sum` |
| live manifest digest (same value) | `d2639fd6…` (201 paths) | `find corpus/knowledge -name '*.md' -type f \| sort \| sed 's\|^corpus/knowledge/\|\|' \| sha256sum` |
| content digest (per-file sha256s, sorted) | `cc5deee39b7e0bc369fa36979ec524bddef02ea139796347b915a548bddb880c` | `find corpus/knowledge -name '*.md' -type f \| sort \| xargs sha256sum \| sha256sum` |
| `corpus/README.md` digest | `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c` | `sha256sum corpus/README.md` |

The two manifest digests agreeing is the measurement that the **before state is exactly the
baseline commit's corpus** — the pinned tree object and the live tree are the same 201 paths. §4's
delta leg (`git ls-tree -r --name-only 751aa21c…` minus the live file set) therefore reads
`new 0 / removed 0` at the before state (observed, §4.3): the pin is real, not decorative.

### 2.4 Before → after vector (after values are the declared target, `reports/round-35/claims.json:29`)

| partition | before (measured, §2.1) | after (target) | delta | README anchor before | README anchor after (target) |
|---|---|---|---|---|---|
| linguistics | 21 | 21 | 0 | `corpus/README.md:123` `## linguistics/ (21)` | unchanged |
| myth-symbol | 19 | **23** | +4 | `corpus/README.md:147` `## myth-symbol/ (19)` | `## myth-symbol/ (23)` |
| culture-material | 18 | **24** | +6 | `corpus/README.md:169` `## culture-material/ (18)` | `## culture-material/ (24)` |
| synthesis | 29 | 29 | 0 | `corpus/README.md:190` `## synthesis/ (29)` | unchanged |
| verification | 20 | 20 | 0 | `corpus/README.md:222` `## verification/ (20)` | unchanged |
| civilizations | 94 | 94 | 0 | `corpus/README.md:245` `## civilizations/ (94)` | unchanged |
| **total** | **201** | **211** | **+10** | `corpus/README.md:469` `Total knowledge entries: 201.` | `Total knowledge entries: 211.` |

README count sites the after state must move (all three, per revision-1.8 precedent at
`corpus/README.md:17-35`, where a stale footer was the recorded defect): the section header, the
totals line `:469`, and the counts footer `:471-473`
(`(total 201 files; directory totals 21/19/18/29/20/94).` → `(total 211 files; directory totals
21/23/24/29/20/94).`). Note the footer vector order is linguistics-first, so the after vector is
**21/23/24/29/20/94** — writing it in the census loop's order is the same string; writing it in
"the two partitions that moved" order is not.

## 3. After — what the counting commands must show once the ten entries land

### 3.1 Counting command 3 is absent (owed)

```sh
$ ls reports/round-35/run-validation.py
ls: cannot access 'reports/round-35/run-validation.py': No such file or directory   # rc=2
```

The runner does not exist at this seat's cut (it is the validator seat's artifact, `S04`'s
validation-leg spec in `reports/round-35/targets.json`). Per `reports/round-35/targets.json:10` this seat does not
execute it in-tree under any circumstance; per `REGIMEN.md:57` the close-time requirement is that
`python3 reports/round-<N>/run-validation.py` exits 0 **at close time**, run from an isolated
`git archive` copy (F-C13-1: filed runners rewrite their own receipts). This fragment supplies the
values that runner's C-legs must assert, not a run of it.

### 3.2 Expected after-readings, per command

| leg | command | before (measured) | after (required) |
|---|---|---|---|
| census vector | §2.1 loop | 21/19/18/29/20/94 | **21/23/24/29/20/94** |
| census total | `find … \| wc -l` | 201 | **211** |
| inventory total | `tools/source-audit-inventory.py --json --summary` | `totals.files 201` | **`totals.files 211`** |
| inventory vector | §2.2 derivation | `[21,19,18,29,20,94]` | **`[21,23,24,29,20,94]`** |
| README headers | `grep -n '^## <part>/ ('` | 21/19/18/29/20/94 | **21/23/24/29/20/94** |
| README totals line | `corpus/README.md:469` | `Total knowledge entries: 201.` | **`Total knowledge entries: 211.`** |
| README footer | `corpus/README.md:471-473` | `(total 201 files; directory totals 21/19/18/29/20/94).` | **`(total 211 files; directory totals 21/23/24/29/20/94).`** |
| README rows vs files | §4 A6 | 21/19/18/29/20/94 (equal) | equal at the new vector (C11/R03 own the row text) |
| new-file delta | §4 A7 vs pinned tree | 0 new | **exactly 10: 6 `culture-material/`, 4 `myth-symbol/`, 0 removed** |

The ten new paths are not named here on purpose: their names are C01–C10's drafts, which had not
landed at this seat's cut (§5). A receipt that invented ten filenames would be fabricating
landing evidence; the delta leg in §4 reports the real names at the moment it runs.

## 4. Re-runnable assertion block (read-only) — and its negative control

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. The block
reads only; it writes nothing (no `open(...,'w')`, no `git` mutation). `PIN` is §2.3's tree object,
so A7 measures the delta against the baseline corpus, not against a moving HEAD.

```python
python3 - <<'PY'
import pathlib, re, subprocess, json
PARTS=['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']
TARGET={'linguistics':21,'myth-symbol':23,'culture-material':24,'synthesis':29,'verification':20,'civilizations':94}
PIN='751aa21c4b4d638c49fbd3269774d25c1d1e6d7a'
fails=[]
def chk(leg, ok, detail):
    print(('PASS ' if ok else 'FAIL ')+leg+' :: '+detail)
    if not ok: fails.append(leg)
live={p:len(sorted(pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))) for p in PARTS}
chk('A1_census_counts', live==TARGET, f'live {live} target {TARGET}')
out=subprocess.run(['python3','-B','tools/source-audit-inventory.py','--json','--summary','--root','corpus/knowledge'],capture_output=True,text=True)
inv=json.loads(out.stdout)
chk('A2_inventory_total', inv['totals']['files']==211, f"totals.files {inv['totals']['files']} target 211 (exit {out.returncode})")
rd=pathlib.Path('corpus/README.md').read_text()
hdr={m.group(1):int(m.group(2)) for m in re.finditer(r'^## (linguistics|myth-symbol|culture-material|synthesis|verification|civilizations)/ \((\d+)\)$', rd, re.M)}
chk('A3_readme_headers', hdr==TARGET, f'headers {hdr}')
chk('A4_readme_total', 'Total knowledge entries: 211.' in rd, [l for l in rd.splitlines() if l.startswith('Total knowledge entries')][0])
footline=[l for l in rd.splitlines() if re.match(r'^\(total \d+ files; directory totals ', l)]
chk('A5_readme_footer', any('(total 211 files; directory totals 21/23/24/29/20/94)' in l for l in footline), f'footer now: {footline[0] if footline else "absent"}')
rows={}
for p in PARTS:
    m=re.search(r'^## '+re.escape(p)+r'/ \(\d+\)\n(.*?)(?=^## )', rd, re.M|re.S)
    rows[p]=len(re.findall(r'^- `[^`]+\.md` — ', m.group(1), re.M))
chk('A6_rows_eq_files', rows==live, f'rows {rows} == files {live}')
pinned=set('corpus/knowledge/'+l for l in subprocess.run(['git','ls-tree','-r','--name-only',PIN],capture_output=True,text=True).stdout.split('\n') if l)
liveset=set(f'corpus/knowledge/{p}/{f.name}' for p in PARTS for f in pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))
new=sorted(liveset-pinned); gone=sorted(pinned-liveset)
chk('A7_delta_10_files', len(new)==10 and not gone, f'new {len(new)} (cm {sum(1 for n in new if "/culture-material/" in n)}, ms {sum(1 for n in new if "/myth-symbol/" in n)}) removed {len(gone)}')
for n in new: print('  + '+n)
print('VERDICT', 'GREEN' if not fails else 'RED legs '+str(fails))
PY
```

### 4.1 Negative control — observed at the before state (this seat's run)

```
FAIL A1_census_counts :: live {'linguistics': 21, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 29, 'verification': 20, 'civilizations': 94} target {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 24, 'synthesis': 29, 'verification': 20, 'civilizations': 94}
FAIL A2_inventory_total :: totals.files 201 target 211 (exit 0)
FAIL A3_readme_headers :: headers {'linguistics': 21, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 29, 'verification': 20, 'civilizations': 94}
FAIL A4_readme_total :: Total knowledge entries: 201.
FAIL A5_readme_footer :: footer now: (total 201 files; directory totals 21/19/18/29/20/94).
PASS A6_rows_eq_files :: rows {'linguistics': 21, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 29, 'verification': 20, 'civilizations': 94} == files {'linguistics': 21, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 29, 'verification': 20, 'civilizations': 94}
FAIL A7_delta_10_files :: new 0 (cm 0, ms 0) removed 0
VERDICT RED legs ['A1_census_counts', 'A2_inventory_total', 'A3_readme_headers', 'A4_readme_total', 'A5_readme_footer', 'A7_delta_10_files']
```

Readings: (a) every after-leg **fails at the before state**, so a later GREEN is informative;
(b) A6 is an equality *invariant* (rows == files), green at the before state and required to stay
green after — it is not an after-target leg; (c) A7 read `new 0 / removed 0`, which is the positive
proof that the §2.3 pin matches the live tree — had the pin been wrong, A7 would have read
`new 201 / removed 201` (this was observed once during harness development, when the pinned
names lacked the `corpus/knowledge/` prefix, and it is why the leg is written with the prefix).

### 4.2 Harness limits (stated, not hidden)

- A6's row regex counts rows of shape ``- `name.md` — topic``; it counts rows, it does not compare
  row topic text with the entry's own `- topic:` line. The verbatim comparison is the round-10/20/28
  sweep pattern (`reports/round-10/coverage/index-update.md:56-100`) and belongs to C11/R03; a
  count-only green here must not be quoted as index-text reconciliation.
- A7 compares path sets, not bytes: a new entry is any live path absent from the pinned tree. A
  modified pre-existing entry shows up in neither `new` nor `gone`; that is intended (claim C adds
  entries), but it means A7 does not detect an in-place edit of an old entry — the preservation legs
  (`git status --porcelain corpus/`) cover that and read clean at this seat's cut.
- The block shells out to `git` and to the inventory tool; both are read-only. No `reports/round-*`
  runner is invoked.

## 5. Dependency state at this seat's cut

```
$ find reports/round-35 -type f | sort
reports/round-35/claims.json
reports/round-35/targets.json
reports/round-35/telemetry/availability-attempt-1.json
reports/round-35/telemetry/availability-attempt-2.json
reports/round-35/telemetry/availability-attempt-3.json
reports/round-35/telemetry/dispatch-declared.json
$ ls reports/round-35/cov reports/round-35/scout reports/round-35/plan
ls: cannot access 'reports/round-35/cov': No such file or directory      # (also scout/, plan/)
# captured before this fragment landed; cov/ did not exist at capture time, so no sibling
# fragment (C01-C17, K*, P*, S01) was readable from it
```

The whole C block was still in flight at that capture: K01/K02 (scouts), P01 (plan), C01–C10 (the
ten entry drafts), C11 (README delta), C12–C14/C17 (audit instruments and audits) were all absent.
So this receipt carries no fold of sibling fragments. §4 is the machine-checkable half of that
reconciliation and can be re-run the moment the entries land.

A second read later in the same session (this fragment's own draft already on disk) shows the A
block and the scribes had landed — `reports/round-35/adj/*`, `reports/round-35/cov/C11-readme-delta.md`,
`reports/round-35/cov/C16-scribe.md`, `reports/round-35/scribe/S01-c-receipt.md` …
`reports/round-35/scribe/S05-telemetry-draft.md`, `reports/round-35/cross/X02-conformance.md`,
`reports/round-35/op/O04-regressions.md`, `reports/round-35/op/O08-validation-legs.md` — while the
ten entry drafts (C01–C10) were **still absent** and the corpus was **unchanged** (`ls` census still
21/19/18/29/20/94; `sha256sum corpus/README.md` still `053966a2…`), so §2's pins hold at the second
read. Cross-check against the two landed artifacts that bear on this receipt's numbers, no
divergence found:

- C11's declared delta is byte-identical to §3.2's expectations: `+Total knowledge entries: 211.`
  and `+(total 211 files; directory totals 21/23/24/29/20/94).`
  (`reports/round-35/cov/C11-readme-delta.md:105-118`), with the section headers
  `+## myth-symbol/ (23)` / `+## culture-material/ (24)` (`:92,99`).
- S01's before/after table reproduces the same two strings
  (`reports/round-35/scribe/S01-c-receipt.md:128-129`) and records the same before state — "BEFORE
  MEASURED 201; after-state owed to the integrator's landing" (`:348`).

S01 is the post-review final receipt and supersedes this draft for folding; the agreement above is
an agreement of declared strings, not a landed measurement — nothing had landed at either read.

## 6. Limits

- All before figures are point-in-time at `4a7aede` with a byte-clean corpus working tree; any
  landing invalidates §2 until re-measured. The pins in §2.3 make the before state recoverable from
  git alone (`git ls-tree -r --name-only 751aa21c…`).
- This receipt certifies **counts and their reconciliation**, never entry quality, source
  resolvability, or canon status: `corpus/README.md:474` ("The inventory counts markers, not
  verified facts") and `SCORECARD.md:16` ("A raw file or marker count is not a quality score")
  apply to every number here.
- The census command (§2.1) globs only `*.md` at each partition's top level; a nested subdirectory
  would be invisible to it. The inventory leg and `find -type f` are the wider nets, and all three
  agree at 201 / `[21,19,18,29,20,94]`. The nesting case is closed at this baseline by direct
  measurement, not assumed: `find corpus/knowledge -mindepth 1 -type d` → 6 (exactly the six
  partitions; `-mindepth 2 -type d` → none), and `find … -name '*.md' -type f` → 201, equal to the
  sum of the six top-level globs, so no `.md` file lives outside the six partitions.
- No mtimes, clocks, or seat-observed timestamps are used as evidence; every leg is a command over
  bytes.

## Owed

- `reports/round-35/cov/C01-entry-1.md` … `reports/round-35/cov/C10-entry-10.md` — the ten entry
  bytes (6 culture-material + 4 myth-symbol) whose landing produces the after state; absent at this
  seat's cut (§5). This receipt deliberately does not name their filenames.
- `reports/round-35/cov/C11-readme-delta.md` — the README count-line and index deltas; §2.4/§3.2
  supply the values its draft must reconcile against, but the row text is C11's. **Landed at this
  seat's second read** (§5); the remaining owed step is the integrator's application to
  `corpus/README.md`.
- `reports/round-35/run-validation.py` — claim C's counting command 3 (`reports/round-35/claims.json:33`); absent
  (`ls` → rc=2). Must be run only from an isolated `git archive` copy (`reports/round-35/targets.json:10`).
- `reports/round-35/cov/C13-audit-1-5.md`, `reports/round-35/cov/C14-audit-6-10.md`,
  `reports/round-35/cov/C17-audit-sample.md` — the 10/10-audited-clean threshold leg
  (`reports/round-35/claims.json:35`), which this receipt does not touch.
- `reports/round-35/cov/S01-c-receipt.md` — the final post-review receipt; this fragment is the
  pre-landing draft, and §4 must be re-run after the entries land for any after-state number to be
  quotable. **Landed at this seat's second read** (§5) — it is the fold that supersedes this draft.
- A post-landing re-run of §4's block (by the integrator or S01) — until it reads GREEN, no
  after-count in §2.4/§3.2 may be quoted as measured.

## Citations

- `reports/round-35/claims.json:21-35` (claim C: `:24` claim, `:26-27` before, `:29` after_required,
  `:31-33` counting commands, `:35` thresholds), `:9-10` (baseline commit), `:72` (no in-tree
  execution of any filed round runner)
- `reports/round-35/targets.json:5-13` (shared rules; `:10` F-C13-1 absolute), `:163-167` (seat C15
  id/role/claim/mission/out)
- `REGIMEN.md:27-30` (declare 1–3 claims; lowest non-retired axis), `:41-43` (admit only when every
  claim verifies and no axis is harmed), `:44-51` (per-round record set), `:57` (`python3
  reports/round-<N>/run-validation.py` exits 0 at close time)
- `corpus/README.md:123,147,169,190,222,245` (partition headers 21/19/18/29/20/94),
  `:469` (`Total knowledge entries: 201.`), `:471-473` (counts footer
  `(total 201 files; directory totals 21/19/18/29/20/94)` + the command it names), `:474` (inventory
  counts markers, not verified facts), `:479-480` (revision-1.9 note: totals 200 → 201 and
  `## linguistics/` 20 → 21), `:17-35` (revision 1.8: the stale-footer defect and the three count
  sites it had to move)
- `reports/round-10/coverage/index-update.md:41-46` (the same two counting commands used as the
  round-10 receipt's evidence), `:56-100` (the verbatim row-vs-`- topic:` sweep pattern, cited as
  C11/R03's leg), `:161-175` (that receipt's own limits section, the shape this §6 follows)
- `tools/source-audit-inventory.py:47-52` (documented invocations incl. `--json --summary`),
  `:545-553` (argparse: `--root`, `--json`, `--summary`, `--baseline`, `--selftest`),
  `:573` (summary suppresses occurrence lists)
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD`; `git status --porcelain corpus/` (empty); `git rev-parse
  HEAD:corpus/knowledge`; `git ls-tree -r --name-only 751aa21c… | sort | sha256sum`;
  `find corpus/knowledge -name '*.md' -type f | sort | sed 's|^corpus/knowledge/||' | sha256sum`;
  `find corpus/knowledge -name '*.md' -type f | sort | xargs sha256sum | sha256sum`;
  `sha256sum corpus/README.md`; `grep -n '^## \|^Total knowledge entries\|^Counts checked'
  corpus/README.md`; the `reports/round-35/claims.json:31` census loop (verbatim output §2.1); `find corpus/knowledge
  -name '*.md' -type f | wc -l` → 201; `python3 -B tools/source-audit-inventory.py --json --summary
  --root corpus/knowledge` (exit 0) and its per-directory derivation one-liner → `totals.files 201 |
  per-dir [21, 19, 18, 29, 20, 94]`; `ls reports/round-35/run-validation.py` (rc=2, absent);
  `find reports/round-35 -type f | sort` (6 files); `ls reports/round-35/cov reports/round-35/scout
  reports/round-35/plan` (all absent); the §4 assertion block (negative control, §4.1)
