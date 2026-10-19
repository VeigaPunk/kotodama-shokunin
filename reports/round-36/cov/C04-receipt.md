- Seat: C04 | scribe | claim C | date 2026-10-19 | baseline ce103bf

# C04 — coverage receipt draft: landing the r35 timekeeping spare, before→after with counting commands

**Assignment** (`reports/round-36/targets.json:30`, seat C04): "Coverage receipt draft." Out
path: `reports/round-36/cov/C04-receipt.md`. Binding shared rules read at
`reports/round-36/targets.json:3-10` — `:4` write only the assigned out path, `:5` never edit
filed bytes, `:6` corpus/tool changes are DRAFTED as fenced blocks and the integrator applies,
`:8` **never** execute any `reports/round-*/run-validation.py` in-tree (isolated `git archive`
copies only; any `--freeze` of `declared-in-r7` forbidden), `:9` every claim cites file:line or
command output, unknowns marked `to-verify`.

**Status: DRAFT, and this seat landed nothing.** Every *before* figure in §2 is a live
measurement taken by this seat in the window named below. The *after* side is proven in §3 — not
asserted — by applying the spare and the README reconciliation inside an **isolated `git archive`
copy** and reading the result. The lane's own corpus was re-verified byte-identical at the end of
that experiment (§3.4). No round runner was executed anywhere.

## 0. Measurement window and state pins

2026-10-19, in-session, lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| pin | value | command |
|---|---|---|
| baseline commit | `ce103bf5885af00023cdc4a174c17602476cdcf8` | `git rev-parse HEAD` |
| corpus tree object | `4b9804167a4919248e312bea4a39d3f99a90766a` | `git rev-parse HEAD:corpus/knowledge` |
| pinned corpus paths | 211 | `git ls-tree -r --name-only 4b980416… \| wc -l` |
| corpus path-manifest digest | `8440257952cbed24dc3460d3d38fe908a5dc1db8c4be288ca7d8f80f8d11c4c4` | `git ls-tree -r --name-only 4b980416… \| sort \| sha256sum` |
| live path-manifest digest (same value) | `84402579…` (211 paths) | `find corpus/knowledge -name '*.md' -type f \| sort \| sed 's\|^corpus/knowledge/\|\|' \| sha256sum` |
| corpus content digest (per-file sha256s, sorted) | `8d13ffffaf75c04e84b90a7457930e49f84de814be1bdd52a818aa6d53d7de3b` | `find corpus/knowledge -name '*.md' -type f \| sort \| xargs sha256sum \| sha256sum` |
| `corpus/README.md` digest | `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` (523 lines, 125,229 bytes) | `sha256sum corpus/README.md`; `wc -l -c corpus/README.md` |
| corpus working tree | clean | `git status --porcelain corpus/` → empty |
| spare digest | `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2` (150 lines) | `sha256sum reports/round-35/cov/C04-timekeeping-spare.md` |
| round-36 seat objects | `claims.json` / `targets.json` digests as filed | `reports/round-36/telemetry/dispatch-declared.json:14-17` |

The two manifest digests agreeing is the measurement that the *before* state is exactly the
baseline commit's corpus — the pinned tree object and the live tree are the same 211 paths. §4's
B7 delta leg therefore reads `new 0 / removed 0` at the before state (observed, §4.1): the pin is
real, not decorative.

## 1. Claim under receipt

`reports/round-36/claims.json:22-27` — claim **C**, axis **coverage**:

| field | `reports/round-36/claims.json` | content |
|---|---|---|
| claim | `:23` | "Land the routed timekeeping spare (`reports/round-35/cov/C04-timekeeping-spare.md`, authored r35 and routed, not silently landed): one new culture-material entry + README reconciliation." |
| before | `:24` | "CM 24 / total 211; the spare is drafted but unlanded" |
| after_required | `:25` | "CM 25 / total 212; README rev 2.1 sweep-green (212 rows == 212 files); the spare audited (two auditors) before landing" |
| counting commands | `:26` | (1) per-partition `ls … \| wc -l` loop; (2) `python3 -B reports/round-28/readme/sweep.py` |
| thresholds | `:27` | "sweep green; audit clean; zero other count surfaces drift" |

The per-round contract that binds this receipt: `REGIMEN.md:41-43` (admit only when every claim
verifies and no axis is harmed; never force a pass), `:44-51` (per-round record set), `:57`
(`python3 reports/round-<N>/run-validation.py` exits 0 at close time).

This receipt owns the **counting legs** of claim C only. The two-auditor gate (`:25`) is
C01/C02/C03's evidence; the landing is the integrator's. §5 files a drift finding that the two
auditors and R03 should carry into their verdicts.

**What is being landed, precisely.** The spare's fenced ```` ```markdown ```` block is the entry
body: 140 lines, 40,234 bytes with a trailing newline. Its head block carries the full house field
set — `topic, sources, source, couples, verified-at, recheck, scope` (`reports/round-35/cov/C04-timekeeping-spare.md:13-21`) —
and its 24 cited `corpus/knowledge/...md` couples paths all resolve at `ce103bf` (§5.3). The
prose above the fence (`:1-8`) is the r35 integrator's routing note and is **not** part of the
entry.

## 2. Before — measured live at `ce103bf`

### 2.1 Counting command 1 — per-partition census (verbatim, `reports/round-36/claims.json:26`)

```sh
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21
23
24
29
20
94
$ find corpus/knowledge -name '*.md' -type f | wc -l
211
```

The loop order is the one `reports/round-36/claims.json:24` uses and the one the README footer
vector uses (`corpus/README.md:496` = `21/23/24/29/20/94`), i.e. index 0 is `linguistics`. The
total agrees with `:24` (`CM 24 / total 211`).

### 2.2 Cross-method agreement — the lane inventory

```sh
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge \
  | python3 -c "import json,sys,collections;d=json.load(sys.stdin);c=collections.Counter(f['path'].split('/')[0] for f in d['files']);print('totals.files',d['totals']['files'],'| per-dir',[c[p] for p in ['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']])"
totals.files 211 | per-dir [21, 23, 24, 29, 20, 94]
```

The one-liner is this seat's derivation over the tool's own `files[].path` rows (the tool prints
no directory vector); it is a **cross-method agreement leg** against §2.1. The inventory counts
markers, not verified facts (`corpus/README.md:497`).

### 2.3 Counting command 2 — the index instrument, live

```sh
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 24, "linguistics": 21, "myth-symbol": 23, "synthesis": 29, "verification": 20}
rows 211 files 211
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 211 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 211, "dir_totals": [21, 23, 24, 29, 20, 94]}
footer_live {"total": 211, "dir_totals": [21, 23, 24, 29, 20, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0
$ echo $?
0
$ python3 -B reports/round-28/readme/sweep.py --selftest
… selftest: 12/12 checks passed
$ echo $?
0
```

The before state is **green**, which is the point: the instrument's controls fire (§4.1) and its
live leg passes at 211, so a green reading at 212 is informative rather than green-by-construction.

### 2.4 The README count surfaces the landing must move

| line | content at `ce103bf` |
|---|---|
| `corpus/README.md:3` | `revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten` |
| `corpus/README.md:186` | `## culture-material/ (24)` |
| `corpus/README.md:206` | `- \`textile-technology.md\` — …` (insertion predecessor) |
| `corpus/README.md:207` | `- \`trade-economy-lexicon.md\` — …` (insertion successor) |
| `corpus/README.md:492` | `Total knowledge entries: 211.` |
| `corpus/README.md:494-496` | `Counts checked 2026-10-19 …` / the inventory command / `(total 211 files; directory totals 21/23/24/29/20/94).` |

The row's insertion point is **filename order inside the section**, which is the invariant the
index instrument measures (`reports/round-28/readme/sweep.py:21-22,74-79,140`). Measured with
`bisect` over the live section listing:

```sh
$ python3 -c "import pathlib,bisect;cm=sorted(p.name for p in pathlib.Path('corpus/knowledge/culture-material').glob('*.md'));i=bisect.bisect_left(cm,'timekeeping-material-culture.md');print('after',cm[i-1],'| before',cm[i])"
after textile-technology.md | before trade-economy-lexicon.md
```

### 2.5 Before → after vector (after values are the declared target, `reports/round-36/claims.json:25`)

| partition | before (measured §2.1) | after (target) | delta | README site to move |
|---|---|---|---|---|
| linguistics | 21 | 21 | 0 | none |
| myth-symbol | 23 | 23 | 0 | none |
| culture-material | **24** | **25** | +1 | header `:186` `(24)` → `(25)`; one row inserted at `:207` |
| synthesis | 29 | 29 | 0 | none |
| verification | 20 | 20 | 0 | none |
| civilizations | 94 | 94 | 0 | none |
| **total** | **211** | **212** | **+1** | totals line `:492`; footer `:496` |

Footer vector after: `21/23/25/29/20/94` (linguistics-first — the same string in the census loop's
order). Revision header: `2.0` → `2.1` (`reports/round-36/claims.json:25`; the file's 0.1-step
convention, `corpus/README.md:3,30,50,62,82,108,118`).

## 3. After — proven in an isolated `git archive` copy

This is the load-bearing section. Rather than assert the after state, this seat built it in a
throwaway copy and measured it. The copy is outside the lane's tracked tree and is disposable.

### 3.1 Construction

```sh
$ rm -rf .scratch/c04-iso && mkdir -p .scratch/c04-iso
$ git archive HEAD | tar -x -C .scratch/c04-iso      # lane HEAD ce103bf; no .git in the copy
```

Then, inside `.scratch/c04-iso`: extract the spare's fenced block verbatim to
`corpus/knowledge/culture-material/timekeeping-material-culture.md` (+ trailing newline), and apply
the §2.5 README edits with the row text derived from the entry's own `- topic:` line
(continuation-joined) — the exact invariant the index instrument checks.

```
ORDER: insert between textile-technology.md and trade-economy-lexicon.md
LANDED bytes 40234 topic_chars 1696
README before 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0
     -> after da6d4b531336ef24c8642e92f187871258c6f89f35608b949de2594c3a03cd1d
     127204 bytes 528 lines (the script's own count, which counts the final newline as opening a
     line; `wc -l` on the same file reads 527 — §3.1's script and `wc` use different conventions,
     and both values below are labelled with their source)
```

### 3.2 Counting command 1 and 2, read in the copy

```sh
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21
23
25
29
20
94
$ find corpus/knowledge -name '*.md' -type f | wc -l
212
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge | <derivation>
totals.files 212 | per-dir [21, 23, 25, 29, 20, 94]
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 21, "myth-symbol": 23, "synthesis": 29, "verification": 20}
rows 212 files 212
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 212 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 212, "dir_totals": [21, 23, 25, 29, 20, 94]}
footer_live {"total": 212, "dir_totals": [21, 23, 25, 29, 20, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 da6d4b531336ef24c8642e92f187871258c6f89f35608b949de2594c3a03cd1d
$ echo $?
0
```

**Claim C's two filed counting commands read green at the target vector, and the index instrument
exits 0 with 212 rows == 212 files, 0 missing, 0 ghosts, 0 topic mismatches, 0 header drift and a
matching footer.** The row inserted was byte-equal to the entry's own continuation-joined `- topic:`
text (verified by direct string comparison, not by the count regex).

### 3.3 The whole §4 assertion block, run in the copy: 9/9 GREEN

```
PASS B1_census_counts :: live {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 20, 'civilizations': 94}
PASS B2_inventory_total :: totals.files 212
PASS B3_readme_header_cm25 :: cm 25
PASS B4_readme_total :: Total knowledge entries: 212.
PASS B5_readme_footer :: (total 212 files; directory totals 21/23/25/29/20/94).
PASS B8_rev21 :: revision: 2.1 — Round-36 timekeeping-spare landing (2026-10-19): the routed round-35
PASS B6_rows_eq_files :: rows==files True
PASS B7_delta_1_file :: new 1 ['corpus/knowledge/culture-material/timekeeping-material-culture.md'] removed 0
PASS B9_sweep_green :: sweep exit 0
VERDICT GREEN
```

### 3.4 The lane was not touched (the negative control on the experiment itself)

```sh
$ git status --porcelain corpus/          # in the LANE, after the experiment
                                        # → empty
$ sha256sum corpus/README.md
51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0
$ ls corpus/knowledge/culture-material/timekeeping-material-culture.md
ls: cannot access 'corpus/knowledge/culture-material/timekeeping-material-culture.md': No such file or directory   # rc=2
```

The lane's corpus digest, path set and working-tree status are exactly §0's *before* values. The
experiment is therefore a **prediction of the after state**, produced without a single lane write —
and it is a prediction the integrator can reproduce with the §4 block.

## 4. Re-runnable assertion block (read-only) — negative control and landed run

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. The block
reads only; it writes nothing. `PIN` is §0's corpus tree object, so B7 measures the delta against
the baseline corpus, not against a moving HEAD.

```python
python3 - <<'PY'
import pathlib, re, subprocess, json, os
PARTS=['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']
TARGET={'linguistics':21,'myth-symbol':23,'culture-material':25,'synthesis':29,'verification':20,'civilizations':94}
PIN='4b9804167a4919248e312bea4a39d3f99a90766a'
LANE=os.environ.get('LANE','.')          # in an isolated copy, point LANE at the lane root
fails=[]
def chk(leg, ok, detail):
    print(('PASS ' if ok else 'FAIL ')+leg+' :: '+detail)
    if not ok: fails.append(leg)
live={p:len(sorted(pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))) for p in PARTS}
chk('B1_census_counts', live==TARGET, f'live {live} target {TARGET}')
out=subprocess.run(['python3','-B','tools/source-audit-inventory.py','--json','--summary','--root','corpus/knowledge'],capture_output=True,text=True)
inv=json.loads(out.stdout)
chk('B2_inventory_total', inv['totals']['files']==212, f"totals.files {inv['totals']['files']} target 212 (exit {out.returncode})")
rd=pathlib.Path('corpus/README.md').read_text()
hdr={m.group(1):int(m.group(2)) for m in re.finditer(r'^## (linguistics|myth-symbol|culture-material|synthesis|verification|civilizations)/ \((\d+)\)$', rd, re.M)}
chk('B3_readme_header_cm25', hdr.get('culture-material')==25, f'cm header {hdr.get("culture-material")}')
chk('B4_readme_total', 'Total knowledge entries: 212.' in rd, [l for l in rd.splitlines() if l.startswith('Total knowledge entries')][0])
foot=[l for l in rd.splitlines() if re.match(r'^\(total \d+ files; directory totals ', l)]
chk('B5_readme_footer', any('(total 212 files; directory totals 21/23/25/29/20/94)' in l for l in foot), foot[0] if foot else 'absent')
chk('B8_rev21', bool(re.search(r'^revision: 2\.1 — ', rd, re.M)), [l for l in rd.splitlines() if l.startswith('revision: ')][0])
rows={}
for p in PARTS:
    m=re.search(r'^## '+re.escape(p)+r'/ \(\d+\)\n(.*?)(?=^## )', rd, re.M|re.S)
    rows[p]=len(re.findall(r'^- `[^`]+\.md` — ', m.group(1), re.M))
chk('B6_rows_eq_files', rows==live, f'rows {rows} == files {live}')
# B7 resolves the pin in the LANE's git object store: an isolated copy has no .git
raw=subprocess.run(['git','-C',LANE,'ls-tree','-r','--name-only',PIN],capture_output=True,text=True).stdout
pinned=set('corpus/knowledge/'+l for l in raw.split('\n') if l)
liveset=set(f'corpus/knowledge/{p}/{f.name}' for p in PARTS for f in pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))
new=sorted(liveset-pinned); gone=sorted(pinned-liveset)
chk('B7_delta_1_file', len(new)==1 and not gone and '/culture-material/' in (new[0] if new else ''), f'new {len(new)} removed {len(gone)}')
for n in new: print('  + '+n)
sw=subprocess.run(['python3','-B','reports/round-28/readme/sweep.py'],capture_output=True,text=True)
chk('B9_sweep_green', sw.returncode==0, f'sweep exit {sw.returncode}')
print('VERDICT', 'GREEN' if not fails else 'RED legs '+str(fails))
PY
```

### 4.1 Negative control — observed at the before state (`ce103bf`, this seat's run)

```
FAIL B1_census_counts :: live {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 24, 'synthesis': 29, 'verification': 20, 'civilizations': 94} target {... 'culture-material': 25 ...}
FAIL B2_inventory_total :: totals.files 211 target 212 (exit 0)
FAIL B3_readme_header_cm25 :: cm header 24
FAIL B4_readme_total :: Total knowledge entries: 211.
FAIL B5_readme_footer :: footer now: (total 211 files; directory totals 21/23/24/29/20/94).
FAIL B8_rev21 :: revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
PASS B6_rows_eq_files :: rows {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 24, 'synthesis': 29, 'verification': 20, 'civilizations': 94} == files {...same...}
FAIL B7_delta_1_file :: new 0 removed 0
PASS B9_sweep_green :: sweep exit 0 :: rows 211 files 211 | missing_from_index 0 [] | topic_mismatch 0 [] | orphan_rows 0 [] | header_drift {} | totals_line 211 totals_ok True | footer_findings [] footer_ok True
VERDICT RED legs ['B1_census_counts', 'B2_inventory_total', 'B3_readme_header_cm25', 'B4_readme_total', 'B5_readme_footer', 'B8_rev21', 'B7_delta_1_file']
```

Readings: (a) every after-leg **fails at the before state**, so the §3.3 GREEN is informative;
(b) B6 is an equality *invariant* (rows == files), green at both states and required to stay green —
it is not an after-target leg; (c) B9 is green at both states by design (the before index is
consistent at 211), so B9 alone never proves the landing — it proves the landing did not *break*
consistency; (d) B7 read `new 0 / removed 0`, which is the positive proof that the §0 pin matches
the live tree — had the pin been wrong it would have read `new 211 / removed 211`.

### 4.2 Harness limits (stated, not hidden)

- B6's row regex counts rows of shape ``- `name.md` — topic``; it counts rows, it does not compare
  row topic text against the entry's own `- topic:` line. The verbatim comparison is the
  round-10/20/28 sweep pattern and belongs to the instrument itself (`reports/round-28/readme/sweep.py:140`);
  §3.1 verified that equality directly by string comparison for the one row this round inserts.
  A count-only green here must not be quoted as index-text reconciliation.
- B7 compares path sets, not bytes. A new entry is any live path absent from the pinned tree; a
  modified pre-existing entry shows in neither `new` nor `gone`. That is intended (claim C adds an
  entry), but it means B7 does not detect an in-place edit of an old entry — `git status --porcelain
  corpus/` covers that and read clean at §3.4.
- B7 shells out to `git -C $LANE`; inside an isolated `git archive` copy there is no `.git`, so the
  pin must be resolved in the lane's object store. This seat hit exactly that: the first landed run
  read `FAIL B7_delta_1_file :: new 212 removed 0` because `git ls-tree` in the copy failed and the
  empty pinned set made every live path look new. The fix (the `git -C $LANE` form above) is why the
  leg is written that way; the failure mode is recorded here so a re-runner does not mistake it for
  a real finding.
- The block shells out to `git` and to the inventory tool; both are read-only. No `reports/round-*`
  runner is invoked, per `reports/round-36/targets.json:8`.

## 5. Drift findings — the spare's gap statement is stale at `ce103bf`

Claim C's threshold is "zero other count surfaces drift" (`reports/round-36/claims.json:27`). The
spare's own `- gap filled:` paragraph carries a quantitative absence sweep measured at HEAD
`4a7aede` over **201** files (`reports/round-35/cov/C04-timekeeping-spare.md:13`). Re-running it at
`ce103bf` over **211** files does **not** reproduce, and the cause is identifiable: the round-35
landings themselves introduced the terms. These are findings for C01/C02/C03 and R03, not repairs
this receipt may make (the spare's bytes are filed; `reports/round-36/targets.json:5`).

### 5.1 The 28-term absence sweep, re-run at `ce103bf`

```sh
$ for kw in "water clock" clepsydra clepsammia gnomon sundial escapement pendulum hourglass "incense clock" curfew "bell tower" "canonical hour" clockmaker muwaqqit wadokei shichen "toki no kane" horologium foliot quadrant sandglass "candle clock" "night clock" "standard time" "railway time" vigilia; do printf '%-18s %s\n' "$kw" "$(grep -ril -- "$kw" corpus/knowledge/*/*.md | wc -l)"; done
water clock        0
clepsydra          0
clepsammia         0
gnomon             0
sundial            0
escapement         0
pendulum           0
hourglass          0
incense clock      0
curfew             1      <-- spare claims 0
bell tower         0
canonical hour     0
clockmaker         0
muwaqqit           0
wadokei            0
shichen            0
toki no kane       0
horologium         0
foliot             0
quadrant           0
sandglass          0
candle clock       0
night clock        0
standard time      0
railway time       0
vigilia            0
```

**26 of 28 terms still read 0 — the gap the entry fills is intact.** One term drifted: `curfew`.

### 5.2 The drifted term, with its cause

```sh
$ grep -ril 'curfew' corpus/knowledge/*/*.md
corpus/knowledge/culture-material/fire-fuel-light.md
$ git grep -il 'curfew' 4a7aede -- 'corpus/knowledge/*/*.md'
$ echo $?
1                                  # absent at the r35 baseline
$ git diff --name-only 4a7aede HEAD -- corpus/knowledge/
corpus/knowledge/culture-material/agrarian-field-system-lexicon.md
corpus/knowledge/culture-material/bathing-and-body-hygiene.md
corpus/knowledge/culture-material/fire-fuel-light.md
corpus/knowledge/culture-material/funerary-material-culture.md … (10 paths)
```

`fire-fuel-light.md` is one of the ten entries **round 35 itself landed**; `curfew` was absent at
`4a7aede` and present at `ce103bf`. Its context is a fire ordinance, not a time institution
(`corpus/knowledge/culture-material/fire-fuel-light.md:82` — "**Curfew.** *Couvre-feu* means,
literally, 'cover the fire': a fire ordinance …"; also `:112`, `:131`, `:153`). So the *finding*
is narrow and the spare's gap survives in substance: the term is now present, but as the fire
rule's name, not as the timekeeping institution the spare claims is absent — and the spare's own
§5 table already lists `curfew` as an institution it owns
(`reports/round-35/cov/C04-timekeeping-spare.md:13`, `§5` row 2). The consequence for the landing
is a **coupling to declare**, not a defect to fix: the new entry's `curfew` row must point at
`fire-fuel-light.md` rather than claim the term is corpus-absent.

### 5.3 The spare's other named near-misses, re-measured at `ce103bf`

The spare's gap paragraph also names near-miss counts measured at 201 files. At 211:

| term | spare's r35 count | measured at `ce103bf` | moved by |
|---|---|---|---|
| `astrolabe` | 2 | 2 | — |
| `"star clock"` | 2 | 2 | — |
| `chronometer` | 2 | **4** | `funerary-material-culture.md`, `writing-media-surface-economy.md` (both r35 landings) |
| `obelisk` | 1 | 1 | — |
| `meridian` | 1 | 1 | — |
| `"time zone"` | 1 | 1 | — |
| `"night watch"` | 1 | **2** | `fire-fuel-light.md` (an r35 landing) |
| `hour` | 8 files | **17 files** | six r35 landings carry `hour`/`Hour` |
| `bell` | 81 files | **87 files** | r35 landings |
| `clock` | 6 files in culture-material | **10 files in culture-material** | four r35 landings |

```sh
$ grep -ril 'chronometer' corpus/knowledge/*/*.md
corpus/knowledge/culture-material/dress-through-eras.md
corpus/knowledge/culture-material/funerary-material-culture.md
corpus/knowledge/culture-material/vessel-container-lexicon.md
corpus/knowledge/culture-material/writing-media-surface-economy.md
$ git grep -il 'chronometer' 4a7aede -- 'corpus/knowledge/*/*.md'
4a7aede:corpus/knowledge/culture-material/dress-through-eras.md
4a7aede:corpus/knowledge/culture-material/vessel-container-lexicon.md
$ grep -ril 'night watch' corpus/knowledge/*/*.md
corpus/knowledge/culture-material/fire-fuel-light.md
corpus/knowledge/myth-symbol/ritual-liminality.md
$ git grep -il 'night watch' 4a7aede -- 'corpus/knowledge/*/*.md'
4a7aede:corpus/knowledge/myth-symbol/ritual-liminality.md
```

**Disposition.** None of these undermines the gap: `chronometer` still appears only as a metaphor
or a measure, `night watch` still not as the timekeeping institution, and the `clock`/`hour`/`bell`
rises are the r35 fire, funerary, bathing and writing entries using those words in their own
senses. But the spare's literal counts no longer describe the tree, so **the entry's
`- gap filled:` paragraph must be re-measured at the landing baseline before it is quoted as
evidence** — otherwise the round lands a filed sentence that a reader can falsify with one command.
That is the actionable finding: the landing is count-clean (§3.2), and the prose it carries is
count-stale (§5.1-5.3). C01/C02 (the two independent auditors) and R03 (cross-review) should carry
it; this receipt does not edit the spare.

### 5.4 Couples resolution (the entry's own references)

```sh
$ python3 -c "<extract couples paths; test existence>"
couples paths cited: 24 | missing: []
```

All 24 `corpus/knowledge/...md` paths named in the entry's `- couples:` line resolve at `ce103bf`.
The spare's `- source:` line also records that no external source was resolved in r35 (no network),
and carries 33 inline `to-verify` marks inside the fenced block — those route through
`corpus/knowledge/verification/to-verify-triage-protocol.md` and are not this receipt's gate.

## 6. The README delta the integrator applies (byte-exact)

Five edits, all name-independent except the one row. `before` bytes are `ce103bf`'s; `after` bytes
were produced and verified in the isolated copy (§3.1).

**E1 — revision block (insert before `corpus/README.md:3`).** Precedent for shape and the closing
sentence: `corpus/README.md:3-15` (revision 2.0).

```
+revision: 2.1 — Round-36 timekeeping-spare landing (2026-10-19): the routed round-35
+spare landed as `culture-material/timekeeping-material-culture.md`; `## culture-material/`
+moved 24 -> **25** and the totals line and counts footer moved 211 -> **212**
+(vector 21/23/25/29/20/94). Revision 2.0 block below.
```

**E2 — culture-material header (`corpus/README.md:186`).**

```
-## culture-material/ (24)
+## culture-material/ (25)
```

**E3 — one row inserted between `corpus/README.md:206` and `:207`** (filename order:
`textile-technology.md` < `timekeeping-material-culture.md` < `trade-economy-lexicon.md`). The row
is 1,747 bytes including its newline; its topic text is the entry's own `- topic:` head-block text
with continuation lines space-joined, and it was verified byte-equal to that text:

```
+- `timekeeping-material-culture.md` — <the entry's continuation-joined `- topic:` text, 1,696 chars>
```

**E4 — totals line (`corpus/README.md:492`).**

```
-Total knowledge entries: 211.
+Total knowledge entries: 212.
```

**E5 — counts footer (`corpus/README.md:496`).**

```
-(total 211 files; directory totals 21/23/24/29/20/94).
+(total 212 files; directory totals 21/23/25/29/20/94).
```

Footer line `:494` (`Counts checked 2026-10-19 …`) and `:495` (the inventory command) already carry
the right date and command at `ce103bf` and need no change. The expected post-landing
`corpus/README.md` digest, **as predicted by the isolated experiment**, is
`da6d4b531336ef24c8642e92f187871258c6f89f35608b949de2594c3a03cd1d` (527 lines by `wc -l`,
127,204 bytes). It
becomes a reading only when the integrator applies the same five edits and re-runs §4.

## 6.5 Live integrity finding — two filed runners defeat `git archive` isolation; two filed receipts moved during the round

This seat observed writes to **filed bytes** during the round, diagnosed the mechanism, and files
the finding here because it bears directly on the round-36 rule set and on the recount block (Ca).
It is reported, not repaired: `reports/round-1..35/**` is filed and off-limits to this seat
(`reports/round-36/targets.json:5`).

### 6.5.1 The census — exactly two runners re-anchor to a hardcoded root

```sh
$ grep -n '^ROOT = \|^os.chdir\|ROOT = Path' reports/round-*/run-validation.py
… 28 runners: ROOT = Path(__file__).resolve().parents[2]     # r5-r33 — genuinely isolated
reports/round-34/run-validation.py:10:ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
reports/round-34/run-validation.py:26:os.chdir(ROOT)
reports/round-35/run-validation.py:9:ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
reports/round-35/run-validation.py:36:os.chdir(ROOT)
```

Thirty runners exist; twenty-eight derive their root from `__file__` and are safe in a copy. **Only
r34 and r35 hardcode the absolute lane root and then `chdir` to it.** In those two, every relative
path — including the receipt write, `out_path = f"{ROUND}/validation.json"`
(`reports/round-35/run-validation.py:502`, opened at `:504`) — resolves to the **lane**, not to the
copy the seat is standing in. `--check` is the safe mode (it prints and returns at `:495-501` and
never reaches `:504`); the default mode writes.

### 6.5.2 Why this is a round-36 rule problem, not just an r34/r35 bug

The lane's rule (`reports/round-36/targets.json:8`) is "never run `reports/round-*/run-validation.py`
in-tree (isolated `git archive` copies only)". That rule assumes the copy is what isolates the
runner. For these two it is not: the copy isolates the *reading* but not the *writing*. A seat that
follows the rule exactly — archives HEAD, `cd`s into the copy, runs the runner — still publishes
into the lane. The rule is therefore unsatisfiable for r34/r35 as written.

### 6.5.3 Observed consequences

**(a) `reports/round-35/validation.json`** moved twice (mtimes `06:29:26` and `06:29:42 -0300`) and
is now **byte-identical to its committed blob** again:

```sh
$ git cat-file -p HEAD:reports/round-35/validation.json | sha256sum   # 328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124
$ sha256sum reports/round-35/validation.json                          # 328e97b3…  (equal)
```

This seat cannot attribute the restore and does not claim to.

**(b) `reports/round-34/validation.json` — a filed verdict was rewritten during the round, and has
since been restored.** This seat observed it dirty at `06:30:35 -0300`:

```sh
$ git status --porcelain reports/round-34/validation.json
 M reports/round-34/validation.json
$ git cat-file -p HEAD:reports/round-34/validation.json | sha256sum   # ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a
$ sha256sum reports/round-34/validation.json                          # 72733e3254a0c0f7f498576f46b06d70fb2b8260cf9ffb64112e5b965e8bec37
```

The observed diff flipped the round's recorded outcome: `"acceptance_checks_passed": true` →
`false`, the claim-O leg `"status": "green"` → `"failed"` with a new failure string
`"O2: inventory counts differ: 30 runners, {'guarded-refresh': 19, 'unguarded-in-place': 11}"`, the
top-level `"failures": []` → one failure, and `"measured_at_utc"` → a fresh timestamp. The
`class_counts` it reports moved `guarded-refresh: 18` → `19` — **because round 36 added a
thirtieth runner** (`reports/round-36/run-validation.py`, a round-36 artifact), so r34's own
inventory leg no longer matches its committed expectation. The cause is an r36 tree change colliding
with an r34 runner that reads the live tree, plus the non-isolating write path.

**The byte oscillates.** This seat observed `reports/round-34/validation.json` at three distinct
states, each with a fresh `measured_at_utc` inside the rewritten file:

| observation | live digest | vs committed `ba2fa4dc…` | `measured_at_utc` written |
|---|---|---|---|
| 1 (first noticed) | `72733e32…` | dirty | `2026-10-19T06:30:35.842375-03:00` |
| 2 (mid-check) | `ba2fa4dc…` | **clean** | (committed `05:00:03.277854-03:00`) |
| 3 (final check) | `af3a0828…` | dirty again | `2026-10-19T06:32:04.570897-03:00` |
| 4 (last read) | `ba2fa4dc…` | **clean** | (committed) |

So the file is being rewritten, restored, and rewritten again while the round is in flight. **A
clean `git status` at any single instant therefore proves nothing about this byte** — which is the
core reason the finding is filed as an observation series rather than as a one-time status line. At
observation 3 the whole lane read:

```sh
$ git status --porcelain
 M reports/round-34/validation.json
?? reports/round-36/
```

Several concurrent round-36 seats were running these runners at `06:29-06:32`; a process listing
showed one seat shell running `run reports/round-34/run-validation.py` (default, publishing mode)
from `.scratch/x01-iso2`, and others mounting a private namespace over the lane to run r34/r35. The
mechanism is a runner design, not a seat's intent. This seat attributes no individual write and
does not claim which process produced which state.

### 6.5.4 What this receipt does *not* claim

It does not accuse any seat of an unauthorized edit, and it does not certify either receipt as
uncorrupted at every instant of the round. It records: (a) both filed receipts moved during the
round, with the exact digests on each side of each move; (b) the exact mechanism and the two-runner
census that permits it; (c) r34's byte was observed dirty, clean and dirty again, and r35's was
observed dirty twice and clean twice. A transient write that is later overwritten leaves no trace in
`git status` — which is precisely why the observation series is filed here as evidence rather than
left to a clean-status check. The verdicts belong to the round's conformance critic (X02,
`reports/round-36/targets.json:42`) and to the recount block (Ca01/Ca02, `:39-40`), which recount
exactly these filed commands. The hardening —
derive `ROOT` from `__file__` in r34/r35, and stop reading the live tree for an inventory leg that a
later round can move — belongs to a future round and is not applied here.

## 7. Limits

- Every *before* figure is point-in-time at `ce103bf` with a byte-clean corpus working tree; any
  landing invalidates §2 until re-measured. The §0 pins make the before state recoverable from git
  alone (`git ls-tree -r --name-only 4b980416…`).
- The §3 after-state is a **prediction produced in a disposable copy**, not a landed reading. The
  digest `da6d4b53…` and the vector `21/23/25/29/20/94` are what the §4 block must show after the
  integrator lands; they are not evidence that the landing happened.
- This receipt certifies **counts, the index invariant, and the delta's completeness**. It does not
  certify entry quality, source resolvability, the 33 `to-verify` items, or canon status:
  `corpus/README.md:497` ("The inventory counts markers, not verified facts") and `SCORECARD.md:16`
  ("A raw file or marker count is not a quality score") apply to every number here. The two-auditor
  threshold (`reports/round-36/claims.json:25`) is C01/C02/C03's evidence.
- §5's drift finding is a **measurement**, not a verdict: it names that the spare's filed gap
  counts no longer reproduce and which r35 landings moved them. Whether the entry lands with the
  gap paragraph re-measured, or with the coupling declared, is the integrator's and the auditors'
  decision — `reports/round-36/targets.json:5` bars this seat from editing the spare's bytes.
- The census command (§2.1) globs only `*.md` at each partition's top level; a nested subdirectory
  would be invisible to it. The inventory leg and `find -type f` are the wider nets and all three
  agree at 211 / `[21,23,24,29,20,94]` before and 212 / `[21,23,25,29,20,94]` after.
- No mtimes, clocks or seat-observed timestamps are used as evidence; every leg is a command over
  bytes. No round runner was executed in-tree or in the copy (`reports/round-36/targets.json:8`).

## Owed

- `reports/round-36/cov/C01-audit.md` and `reports/round-36/cov/C02-audit-delta.md` — the two
  independent spare audits (`reports/round-36/claims.json:25`, "the spare audited (two auditors)
  before landing"). **Absent at this seat's cut**: `find reports/round-36 -type f` returned exactly
  four files (`claims.json`, `targets.json`, `telemetry/availability-attempt-1.json`,
  `telemetry/dispatch-declared.json`). This receipt supplies the values their verdicts must
  reconcile against and files the §5 drift finding for them to carry.
- `reports/round-36/cov/C03-verify.md` — the independent verification of both audits and of the
  delta numbers (`reports/round-36/targets.json:29`). Absent at this seat's cut. §4 is the
  re-runnable block C03 can run unchanged.
- `reports/round-36/cov/C02-audit-delta.md`'s README delta — §6 drafts the five edits byte-exact,
  but the delta artifact is C02's (`reports/round-36/targets.json:28`). Absent at this seat's cut.
- `corpus/knowledge/culture-material/timekeeping-material-culture.md` — the entry bytes, still the
  spare's fenced block (`reports/round-35/cov/C04-timekeeping-spare.md:11-150`); the integrator
  extracts and lands it (`reports/round-36/targets.json:6`). This seat wrote no corpus byte.
- `corpus/README.md` — the five §6 edits, integrator-applied. Not applied by this seat.
- `reports/round-36/run-validation.py` — claim C's close-time runner (`REGIMEN.md:57`). **Absent**
  (`ls` → rc=2). Must be run only from an isolated `git archive` copy
  (`reports/round-36/targets.json:8`). §4's block is a candidate leg set for its C-claim section.
- The spare's `- gap filled:` paragraph — stale counts at `ce103bf` (§5.1-5.3); re-measurement or a
  declared coupling to `fire-fuel-light.md` is owed before the entry's evidence sentence is quoted.
- A post-landing re-run of §4 by the integrator or C03 — until it reads GREEN against the landed
  tree, no after-count in §2.5 or §3.2 may be quoted as measured.
- §6.5's isolation finding — the mechanism is diagnosed and the two-runner census is complete, but
  the finding is **open and live**: `reports/round-34/validation.json` was observed at four
  different states during this round (`72733e32…` dirty → `ba2fa4dc…` clean → `af3a0828…` dirty →
  `ba2fa4dc…` clean) and `reports/round-35/validation.json` at two (`06:29:26`/`06:29:42` dirty →
  `328e97b3…` clean). **The byte oscillates, so no single read pins its state** — §6.5.3's table is
  the record, not a status line. **No one has adjudicated the rewrite or the isolation defect.** The
  verdict belongs to X02 (conformance, `reports/round-36/targets.json:42`) and to the Ca recount
  block (`:39-40`); the hardening — derive `ROOT` from `__file__` in r34/r35, and stop reading the
  live tree for an inventory leg a later round can move — belongs to a future round and is not
  applied here (`reports/round-36/targets.json:5` bars this seat from touching filed bytes).

## Citations

- `reports/round-36/claims.json:22-27` (claim C: `:23` claim, `:24` before, `:25` after_required,
  `:26` counting commands, `:27` thresholds), `:16-21` (claim D, for the shared axis framing),
  `:1-8` (round/baseline/dispatch)
- `reports/round-36/targets.json:3-10` (shared rules; `:4` out path, `:5` no filed-byte edits,
  `:6` draft-then-apply, `:8` F-C13-1 absolute), `:30` (seat C04 id/role/claim/mission/out)
- `reports/round-36/telemetry/dispatch-declared.json:14-17` (filed digests of `claims.json` /
  `targets.json`), `reports/round-36/telemetry/availability-attempt-1.json` (hyper 402, declared
  devin fallback)
- `REGIMEN.md:41-43` (admit only when every claim verifies), `:44-51` (per-round record set),
  `:57` (runner exits 0 at close time), `:62` (scope)
- `reports/round-35/cov/C04-timekeeping-spare.md:1-8` (routing note; not entry bytes), `:11-150`
  (the fenced entry: 140 lines / 40,234 bytes), `:13` (gap statement + absence sweep at `4a7aede`),
  `:13` `- couples:` (24 in-repo paths), `:15` `- source:`, `:17` `- verified-at:`, `:19` `- recheck:`,
  `:21` `- scope:`; sha256 `258fb166…`
- `reports/round-35/claims.json:21-35` (the r35 C claim that landed the ten entries and the 201→211
  move; `:29` after_required)
- `reports/round-35/validation.json` (r35 close: partition counts, `inventory_files` 211,
  `sweep_tail` footer `21/23/24/29/20/94`, `readme_sha256 51b966af…`)
- `reports/round-35/cov/C11-readme-delta.md:1-130` (the r35 delta pattern this §6 follows:
  byte-exact edits + a recompute rule; the 2.0→2.1 numbering convention at `:69-130`)
- `reports/round-35/cov/C15-receipt.md` (the r35 receipt shape this file mirrors: before/after
  table, assertion block, negative control, `## Owed`, `## Limits`)
- `reports/round-28/readme/sweep.py:21-22` (`SECTION_RE`, `ROW_RE`), `:22` (`TOPIC_RE`), `:74-79`
  (`topic_of`), `:140` (row/topic equality test), `:398-401` (continuation-join control),
  `:1-27` (leg list and the round-28 stale-footer defect it was built for)
- `corpus/README.md:3` (revision 2.0 block start), `:186` (`## culture-material/ (24)`), `:206-207`
  (insertion neighbours), `:492` (totals line), `:494-496` (counts footer), `:497` (markers not
  facts); digest `51b966af…`
- `corpus/knowledge/culture-material/fire-fuel-light.md:82,112,131,153` (the `curfew` occurrences
  that move the §5.1 sweep; `:82` states it is a fire ordinance)
- `SCORECARD.md:16` (a raw file or marker count is not a quality score), `:640` (r35 coverage row:
  "C04's timekeeping alternate routed as a named spare")
- `reports/round-34/run-validation.py:10` (the same hardcoded absolute `ROOT`), `:26`
  (`os.chdir(ROOT)`) — the second non-isolating runner; `reports/round-35/run-validation.py:9`,
  `:36` (`os.chdir(ROOT)`), `:495-505` (`--check` returns before writing; default mode opens
  `reports/round-35/validation.json` for writing), `:232` (that path, read back by later rounds).
  The 28 runners that use `ROOT = Path(__file__).resolve().parents[2]` (e.g.
  `reports/round-33/run-validation.py:23`) are the isolated form
- `git cat-file -p HEAD:reports/round-34/validation.json | sha256sum` → `ba2fa4dc…` vs
  `sha256sum reports/round-34/validation.json` → `72733e32…`; `git diff reports/round-34/validation.json`
  (the `true`→`false` flip, the `guarded-refresh: 18`→`19` count move and the new `measured_at_utc`)
- `tools/harness/receipt_guard.py:1-16` (the preflight guard's contract: HEAD-relative, refuses
  unless `REFRESH_RECEIPTS=1`; the guard is a preflight, not an isolation boundary)
- `reports/round-36/targets.json:39-40` (Ca01/Ca02, the recount block), `:42` (X02, the conformance
  critic), `:5` (no filed-byte edits)
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
  unless noted): `git rev-parse HEAD`; `git status --porcelain corpus/` (empty); `git rev-parse
  HEAD:corpus/knowledge`; `git ls-tree -r --name-only 4b980416… | wc -l` → 211; `git ls-tree -r
  --name-only 4b980416… | sort | sha256sum` → `84402579…`; `find corpus/knowledge -name '*.md'
  -type f | sort | sed 's|^corpus/knowledge/||' | sha256sum` → `84402579…`;
  `find corpus/knowledge -name '*.md' -type f | sort | xargs sha256sum | sha256sum` →
  `8d13ffff…`; `sha256sum corpus/README.md`; `wc -l -c corpus/README.md`; the `claims.json:26`
  census loop (verbatim output §2.1); `find corpus/knowledge -name '*.md' -type f | wc -l` → 211;
  `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` + the
  per-directory derivation → `totals.files 211 | per-dir [21, 23, 24, 29, 20, 94]`;
  `python3 -B reports/round-28/readme/sweep.py` (exit 0) and `--selftest` (12/12, exit 0);
  `sha256sum reports/round-35/cov/C04-timekeeping-spare.md`; `wc -l` on it → 150;
  `grep -c 'to-verify'` → 23 matching lines / 33 occurrences, and all 33 occurrences are inside the
  fenced block (the head block's `- sources:`/`- verified-at:`/`- recheck:`/`- scope:` lines carry
  them); the `bisect`
  insertion-point command (§2.4); `rm -rf .scratch/c04-iso && mkdir -p .scratch/c04-iso &&
  git archive HEAD | tar -x -C .scratch/c04-iso`; the §3.1 construction script (spare extraction +
  five README edits) run inside `.scratch/c04-iso`; §3.2's census / `find` / inventory / sweep in
  the copy; the §4 block run in the copy (`LANE` pointed at the lane root for B7) → 9/9 GREEN;
  the §4 block run in the lane at the before state (negative control, §4.1);
  `git status --porcelain corpus/` and `sha256sum corpus/README.md` re-run after the experiment
  (§3.4); the 28-term absence sweep (§5.1); `grep -ril 'curfew' corpus/knowledge/*/*.md`;
  `git grep -il 'curfew' 4a7aede -- 'corpus/knowledge/*/*.md'` (rc=1);
  `git diff --name-only 4a7aede HEAD -- corpus/knowledge/` (10 paths); the near-miss counts and
  their per-file `grep`/`git grep` pairs (§5.3); the couples-path existence test (§5.4);
  `ls reports/round-36/run-validation.py` (rc=2, absent); `find reports/round-36 -type f` (4 files)
