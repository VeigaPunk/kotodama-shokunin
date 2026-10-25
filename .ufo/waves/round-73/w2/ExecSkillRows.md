# ExecSkillRows — attack on the seven SKILL.md gate rows (round 73, wave 2 FALSIFY)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
Lands: `0316b8883b4f8d44b8efd720140e7f52f734a102` (verified `git -C "$D/lane" rev-parse HEAD`)
Base: `8841ad3b896a0227674fa0725b818c999118046f`
Claims read first: `reports/round-73/claims.json` (claim C, claim Ca).

Target: `SKILL.md:698-704`, the seven rows `accept-c-71`, `accept-ca-71`, `accept-d-71`,
`accept-c-72`, `accept-ca-72`, `accept-c-73`, `accept-ca-73`.

Every command below ran in a throwaway clone:

```
D=$(mktemp -d) && git -C "$D" init -q && git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane" \
  && git -C "$D/lane" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
# D=/tmp/tmp.FafbZEtAQx ; git -C "$D" rev-parse --show-toplevel -> /tmp/tmp.FafbZEtAQx
```

One extra layout was built for the CENSUS legs, because those legs read a *fleet* script that the lane
does not contain: `/tmp/execskillrows/fleet/scripts/sources-census.sh` (copy of the fleet's read-only
script) + `/tmp/execskillrows/fleet/kotodama-shokunin` (second clone at the lands revision). Nothing was
written under `/home/vgpnk/Projects/shokunin/**` or in the lane tree except this report.

---

## 1. Findings

### F1 — BLOCKER. `SKILL.md:704` (accept-ca-73, self-test cell) names a scenario count the counter does not print.

Cell: `... (prints `SELFTEST OK: 9 scenarios`)`.

```
$ cd /tmp/tmp.FafbZEtAQx/lane
$ python3 -B reports/round-73/accept-ca.py --selftest > /tmp/execskillrows_ca73st.txt 2>&1; echo "RC=$?"
RC=0
$ tail -1 /tmp/execskillrows_ca73st.txt
SELFTEST OK: 10 scenarios — do-nothing control (BASEMISMATCH found=2, REPAIR/ANNOTATE/NOSTUB FAIL), clean landing 9/9, stub-row control (ANNOTATE+NOSTUB FAIL), append-only removal FAIL, in-place-outside-footer FAIL, shell-string argv FAIL, min-pairs gate FAIL, authorized SKILL.md registry append 9/9, CLI exit 2 on a bad --lands
```

old → new: **`SELFTEST OK: 9 scenarios` → `SELFTEST OK: 10 scenarios`**.

The lane already holds the contradicting receipt, committed in the same landing as the row set:

```
$ sed -n '1,8p' reports/round-73/telemetry/selftest-r3.txt
# selftest receipts after counter r3
$ python3 -B reports/round-73/accept-c.py --selftest
SELFTEST: 29/29
$ python3 -B reports/round-73/accept-ca.py --selftest
ERROR: base 8841ad3b896a0227674fa0725b818c999118046f is not a commit in /tmp/r73-ca-selftest-yeg6vu1k/lane
SELFTEST OK: 10 scenarios — do-nothing control ...
$ sed -n '6p' reports/round-73/telemetry/selftest-r2.txt
SELFTEST OK: 9 scenarios — do-nothing control ...
```

Cause, traced to commits:

```
$ git log --oneline -S'SELFTEST OK: 9 scenarios' -- SKILL.md
e62d731 round-73 Ca: SCORECARD corrections (L01-L03, L06, L07), SHONEN pointers (L04/L05), SKILL.md gate rows (L08), ...
$ git log --oneline -S'SELFTEST OK: 10 scenarios' -- SKILL.md
(no output)
$ git log --oneline --diff-filter=A -- reports/round-73/telemetry/selftest-r3.txt
85f17eb round-73 C: conlang-scholarship adoption — ...; counter r3 + receipts
```

The row was written against r2; r3 added scenario "7b worktree-only ledger" (`reports/round-73/counter-revisions.md`, r3
row: "selftest gains scenario 7b") and its receipt (`10 scenarios`) landed later, and the row text was never
updated. My run also shows the extra scenario executing (`selftest: worktree-only ledger (r2 bug class)` header,
`ERROR: --lands must be 40 hex` line) before the `SELFTEST OK: 10 scenarios` line. So the self-test cell of a
row that Ca lands as an admitted statement is false at the lands revision, and a reader comparing the row to
`selftest-r3.txt` would have to conclude the receipt is stale when it is the row that is.

### F2 — BLOCKER. `SKILL.md:703` (accept-c-73, verdict-map cell) states a denominator the counter cannot produce on a FAIL.

Cell: ``Output ends `ACCEPT-C-73: PASS` or `: FAIL legs=11/11` ``.

Measured in the clone (CENSUS leg degraded, see F5) and in the fleet layout:

```
$ cd /tmp/tmp.FafbZEtAQx/lane
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102; echo "RC=$?"
LEG PASS ENTRIES
...
LEG FAIL CENSUS
     census script not found: /tmp/tmp.FafbZEtAQx/scripts/sources-census.sh
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-73: FAIL legs=10/11
RC=1

$ cd /tmp/execskillrows/fleet/kotodama-shokunin
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102; echo "RC=$?"
...
ACCEPT-C-73: PASS legs=11/11
RC=0
```

old → new: **`: FAIL legs=11/11` → `: FAIL legs=<n>/11` (measured 10/11 and 1/11); `PASS` carries `legs=11/11` too**.

The script computes the left number, unlike accept-c-72, and the row's own sibling row (accept-ca-73) already uses
the correct `<n>/9` form:

```
$ sed -n '1204p' reports/round-73/accept-c.py
    print("ACCEPT-C-73: %s legs=%d/%d" % ("PASS" if ok else "FAIL", passed, total))
$ sed -n '552p' reports/round-72/accept-c.py
    print("ACCEPT-C-72: %s legs=10/10" % ("PASS" if ok else "FAIL"))
```

The lane's own committed receipt contradicts the cell directly:

```
$ sed -n '35,40p' reports/round-73/telemetry/controls-c.txt
LEG FAIL SCRATCHMIRROR
     receipt missing: .ufo/waves/round-73/assimilation/validate-receipt.txt
LEG FAIL COLLCHECK
     collision id files missing under .ufo/waves/round-73/assimilation
ACCEPT-C-73: FAIL legs=1/11
exit=1
```

This matters because the row is a *gate* row: the entire point of the round-72 row's parenthetical ("the denominator
is a literal, so a FAIL receipt still reads `legs=10/10`") is to tell a reader how to parse a red receipt. Copying
the same shape onto c-73 without the literal is a false parsing instruction: `grep 'ACCEPT-C-73: FAIL legs=11/11'`
over a red receipt finds nothing, and the two committed red receipts read `1/11` and `10/11`.

### F3 — BLOCKER. `SKILL.md:698` and `SKILL.md:699` (accept-c-71, accept-ca-71) advertise exit 2 on input error; neither script has an exit-2 path.

Cells: `0 pass / 1 fail / 2 input error.`

```
$ grep -n 'return 2' reports/round-71/accept-c.py reports/round-71/accept-ca.py
(no output)
$ grep -n 'exit(2)\|SystemExit\|sys.exit' reports/round-71/accept-c.py reports/round-71/accept-ca.py
reports/round-71/accept-c.py:132:    sys.exit(main())
reports/round-71/accept-ca.py:150:    sys.exit(main())
$ sed -n '127,133p' reports/round-71/accept-c.py
    print("ACCEPT-C-71: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1
$ sed -n '147,151p' reports/round-71/accept-ca.py
    print("ACCEPT-CA-71: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1
```

And an actual input error — a `--root` that does not exist — is an uncaught traceback with exit **1**, i.e. it is
indistinguishable from a graded FAIL, and no verdict line is printed:

```
$ python3 -B reports/round-71/accept-c.py --root /nonexistent; echo "RC=$?"
Traceback (most recent call last):
  ...
FileNotFoundError: [Errno 2] No such file or directory: '/nonexistent/corpus/knowledge/culture-material'
RC=1
$ python3 -B reports/round-71/accept-ca.py --root /nonexistent; echo "RC=$?"
Traceback (most recent call last):
  ...
FileNotFoundError: [Errno 2] No such file or directory: '/nonexistent/corpus/SOURCES.md'
RC=1
```

old → new: **`2 input error` → `no 2 path exists; an unusable --root raises FileNotFoundError and exits 1 with no verdict line`** (both rows).
Severity BLOCKER because the cell is an admitted statement about a verdict map and it is false in the direction that
matters: a red receipt from these two gates can be a crash, and a caller keying on exit 2 for "could-not-evaluate"
will never fire.

### F4 — MAJOR. `SKILL.md:701` (accept-c-72, self-test cell) points at a `§5` that does not exist in SKILL.md.

Cell: ``... — measured `SELFTEST: 10/11`, exit 1 at HEAD (see §5)``. The measured number reproduces (see §2), but the pointer does not:

```
$ grep -on 'see §[0-9.]*' SKILL.md
701:see §5
$ grep -n '10/11' SKILL.md
701:| accept-c-72 | gate | ... measured `SELFTEST: 10/11`, exit 1 at HEAD (see §5) | ...
$ grep -n '^## ' SKILL.md | tail -12
20:## Decision table
505:## Error patterns
551:## Boundaries (hard)
564:## Checklist (executable where a tool exists)
578:## Corpus map
602:## Using the evidence
619:## Gates and probes
724:## Source-to-system constraints — round 5
734:## Source-to-system constraints — round 6
749:## Source-bounded culture drill — D3 (round 7)
```

SKILL.md's headings are unnumbered; the only `10/11` in the file is the row itself. The `§5` the row means is the
w1 draft's `## 5. Measured runs`, which was never landed:

```
$ grep -n '^#\|§5' .ufo/waves/round-73/w1/drafts/skill-gates-rows.md | head
1:# SKILL.md §Gates and probes — missing registry rows (round-73 w1, seat ScribeSkillGates)
7:## 1. What is missing, measured
25:## 2. Exact insertion anchor
43:## 3. Rows to insert (verbatim)
53:## 4. Per-gate detail (facts the 8 columns cannot carry)
106:## 5. Measured runs (all read-only; nothing written inside the lane)
```

old → new: **`(see §5)` → `(measured; receipt below)`** — the pointer must name a landed artefact
(`reports/round-73/telemetry/…` or a SKILL.md heading), not a draft section.

### F5 — MAJOR. `SKILL.md:701` (accept-c-72) entry command is incomplete: without `--fleet-root` the gate crashes instead of grading.

Cell entry command: `python3 -B reports/round-72/accept-c.py --root . --lands <40-hex>`.
The script defaults the fleet root to the *parent of `--root`* and then executes `<fleet-root>/scripts/sources-census.sh`:

```
$ sed -n '532p;549p' reports/round-72/accept-c.py
    ap.add_argument("--fleet-root", default=None, help="fleet root (default: lane parent)")
    fleet_root = args.fleet_root or os.path.dirname(os.path.abspath(root))
$ sed -n '433,435p' reports/round-72/accept-c.py
        os.path.join(fleet_root, "scripts/sources-census.sh")
    args = [script, "validate", "--root", fleet_root, "kotodama"]
    r = subprocess.run(args, cwd=root, capture_output=True, text=True)
```

In the isolated clone — the layout SKILL.md:628-630 itself mandates for gate runs ("Run that battery in an isolated
repo export") — the command dies before printing any verdict:

```
$ cd /tmp/tmp.FafbZEtAQx/lane
$ python3 -B reports/round-72/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102; echo "RC=$?"
LEG PASS ENTRIES
LEG FAIL ROWS
...
LEG PASS CITEDLINES
Traceback (most recent call last):
  ...
  File "/tmp/tmp.FafbZEtAQx/lane/reports/round-72/accept-c.py", line 435, in leg_census
    r = subprocess.run(args, cwd=root, capture_output=True, text=True)
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp.FafbZEtAQx/scripts/sources-census.sh'
RC=1
```

No `ACCEPT-C-72:` line at all, so the verdict cell's "Output ends `ACCEPT-C-72: PASS` or `: FAIL legs=10/10`" and
"2 on missing or non-40-hex `--lands`, or when `--root` has no `.git`" are both false for this input: the failure is
an unhandled exception on exit 1. The identical condition in the round-73 counter is handled as a leg:

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b888… 
LEG FAIL CENSUS
     census script not found: /tmp/tmp.FafbZEtAQx/scripts/sources-census.sh
```

old → new: **entry command `… --root . --lands <40-hex>` → `… --root . --lands <40-hex> [--fleet-root <fleet>]`, and the verdict map gains `or a missing `<fleet>/scripts/sources-census.sh` (uncaught FileNotFoundError, exit 1, no verdict line)`** — or the counter must map it to 2.

### F6 — MINOR. `SKILL.md:698` (accept-c-71) admits a gate that is red on every tree it can be pointed at, and the row does not say so.

The row's verdict map is honest (1 = fail) and the write-scope cell does say "no revision pin — grades whatever tree
`--root` names", so no cell is literally false. But the gate is red at the lands revision **and at the base**, because
its COUNTS leg pins the round-71 counts:

```
$ cd /tmp/tmp.FafbZEtAQx/lane
$ python3 -B reports/round-71/accept-c.py --root .; echo "RC=$?"
LEG PASS ENTRY
LEG FAIL COUNTS
     culture-material=38 corpus=247 (want 36/243)
LEG PASS CITED
LEG PASS ROWS
LEG PASS USEDBY-PATHS
LEG PASS CITED-LINES
LEG PASS SWEEP
ACCEPT-C-71: FAIL
RC=1
$ git -C /tmp/execskillrows.base/base rev-parse HEAD   # second clone at 8841ad3b
8841ad3b896a0227674fa0725b818c999118046f
$ cd /tmp/execskillrows.base/base && python3 -B reports/round-71/accept-c.py --root .; echo "RC=$?"
LEG FAIL COUNTS
     culture-material=38 corpus=247 (want 36/243)
ACCEPT-C-71: FAIL
RC=1
```

The pin is real (`reports/round-71/accept-c.py:68`: `count_ok = (cm == 36) and (ctotal == 243)`), so this is a stale
gate, not a stale cell: its 0 branch is unreachable on the lane since round 72. Old → new: **pinned-values cell should
read `… counts 36 and 243 (stale since round 72; the gate is red at HEAD)`**.
Same class, expected rather than stale: `accept-c-72` at the round-73 lands reads `LEG FAIL ROWS` / `LEG FAIL CENSUS`
(measured above) because it pins S874/S875 as the only new rows and a round-72-authorized path set; that is what
`--lands` is for and I do not file it as a finding.

---

## 2. Cell-by-cell reproduction (all seven rows)

Commands run from `/tmp/tmp.FafbZEtAQx/lane` unless noted. `L=0316b8883b4f8d44b8efd720140e7f52f734a102`.

| row (SKILL.md line) | cell | claimed | measured | verdict |
|---|---|---|---|---|
| accept-c-71 (:698) | entry | `ACCEPT-C-71: PASS`/`: FAIL`, no `legs=`, exit 0/1/2 | `ACCEPT-C-71: FAIL`, exit 1, `grep -c 'legs='` = 0 | reproduces except the 2 branch → **F3** |
| accept-c-71 | self-test | `—` (no `--selftest`; argparse error, exit 2) | `error: unrecognized arguments: --selftest`, exit **2** | reproduces |
| accept-c-71 | pinned values | entry path, 36/243, `>=12` ids | `:68` `(cm == 36) and (ctotal == 243)`; `:74` `len(cited) >= 12` | reproduces (stale, **F6**) |
| accept-ca-71 (:699) | entry | `ACCEPT-CA-71: PASS`/`: FAIL`, no `legs=`, exit 0/1/2 | `ACCEPT-CA-71: PASS`, exit 0, `grep -c 'legs='` = 0 | reproduces except the 2 branch → **F3** |
| accept-ca-71 | self-test | `—` (argparse error, exit 2) | `error: unrecognized arguments: --selftest`, exit **2** | reproduces |
| accept-ca-71 | pinned values | 21-id slice, verdict set, S807/S812/S835, six round-70 receipts | `:134` `len(rows) == 21`; `:40` `VERDICTS = {"PRESENT","REFUSED","UNVERIFIABLE"}`; `:139` `UNREACHABLE = {"S807","S812","S835"}`; `:29-34` six `reports/round-70/telemetry/*` paths | reproduces |
| accept-d-71 (:700) | entry | ends `ACCEPT-D-69: PASS`/`: FAIL legs=8/8`; no `ACCEPT-D-71` | `ACCEPT-D-69: PASS legs=8/8`, exit 0; `grep -c 'ACCEPT-D-71'` = 0, `grep -c 'ACCEPT-D-69'` = 1 | reproduces |
| accept-d-71 | self-test | prints GREEN/DO-NOTHING fixtures, `SELFTEST: n/2` | `GREEN FIXTURE: PASS (legs 8/8)` / `DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)` / `SELFTEST: 2/2`, exit 0 | reproduces |
| accept-d-71 | write scope | no-`.git` tree prints `SELFTEST: COULD-NOT-EVALUATE (no git)`, exit 2 | `git archive` export: `SELFTEST: COULD-NOT-EVALUATE (no git)`, exit 2 | reproduces |
| accept-c-72 (:701) | entry | ends `ACCEPT-C-72: PASS`/`: FAIL legs=10/10` (literal) | fleet layout: `ACCEPT-C-72: FAIL legs=10/10`, exit 1 | denominator reproduces; command **F5** |
| accept-c-72 | self-test | `SELFTEST: 10/11`, exit 1 at HEAD (see §5) | `SELFTEST: 10/11`, exit 1, then `ACCEPT-C-72: FAIL legs=10/10` (`LEG FAIL GROUND` — `receipt missing: reports/round-72/telemetry/gap-sweep.txt`) | number reproduces; pointer **F4** |
| accept-c-72 | pinned values | base `b60c7b14…`, S874/S875, ten mutants | `:66 BASE="b60c7b14…"`, `:76 NEW_IDS=("S874","S875")`, `MUTANTS` = 10 keys (`drop_entry repoint rows gate_quote no_rejects ground_zeros receipt_no_exit collisions multi_id_line head_ahead`) | reproduces |
| accept-c-72 | write scope | selftest leaves `mkdtemp` dirs behind | `mkdtemp`=1 (`:700`), `rmtree`=0 | reproduces |
| accept-ca-72 (:702) | entry | ends `ACCEPT-CA-72: PASS`/`: FAIL legs=12/12` | `ACCEPT-CA-72: FAIL legs=12/12`, exit 1 | reproduces |
| accept-ca-72 | self-test | `—` (argparse error, exit 2) | `error: the following arguments are required: --lands`, exit **2** | reproduces |
| accept-ca-72 | verdict map | 2 on missing/malformed `--lands`; absent revision = leg FAILs, exit 1 | `--lands zzz` → `ERROR: --lands must be 40 hex`, exit 2; `--lands 000…0` → `ACCEPT-CA-72: FAIL legs=12/12`, exit 1 | reproduces |
| accept-ca-72 | pinned values | base, fleet root, five R71 report commits, seven w2 paths, CASTAMP | `:23 BASE`, `:26 KNOWN_R71_REPORT_COMMITS` = 5, `W2_FILES` = 7, `:37 CASTAMP` | reproduces |
| accept-c-73 (:703) | entry | ends `ACCEPT-C-73: PASS`/`: FAIL legs=11/11` | fleet layout `ACCEPT-C-73: PASS legs=11/11` exit 0; clone `FAIL legs=10/11` exit 1 | **F2** |
| accept-c-73 | self-test | prints `SELFTEST: 29/29` | `SELFTEST: 29/29`, exit 0 | reproduces |
| accept-c-73 | verdict map | 2 on missing/malformed `--lands` | `ERROR: --lands must be a 40-hex commit (the worktree is never graded, QUALITY 19)`, exit 2 (both) | reproduces |
| accept-c-73 | pinned values | base `8841ad3b…`, five rows, refused staged ids + campaign ids | `:102 BASE`, `:121 DEFAULT_ROWS=("S876".."S880")`, `:123 DEFAULT_REFUSED_STAGED=("S869","S894","S910")`; `claims.json` carries the five-row map and S894/S910 | reproduces |
| accept-ca-73 (:704) | entry | ends `ACCEPT-CA-73: PASS`/`: FAIL legs=<n>/9` | `ACCEPT-CA-73: PASS legs=9/9`, exit 0 (receipt header stamps `0316b888…`) | reproduces |
| accept-ca-73 | self-test | prints `SELFTEST OK: 9 scenarios` | `SELFTEST OK: 10 scenarios`, exit 0 | **F1** |
| accept-ca-73 | verdict map | 2 on input error | `ERROR: --lands must be 40 hex`, exit 2 | reproduces |
| accept-ca-73 | pinned values | ledger 8 pairs + must_track, fleet pin `80d8c9b5…`, observe allowlist | `len(pairs)` = 8; `fleet_pin` = `80d8c9b576d45d3c390e1e8edc6c149cfb698483`; `must_track` = 2 paths | reproduces |

Supporting measurements quoted above and not repeated: `sha256sum reports/round-73/accept-ca.py` =
`222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89` (the r3 hash recorded in
`reports/round-73/counter-revisions.md`), `reports/round-73/accept-c.py` = `95aee881…` (the r1 hash recorded there).
`accept-d-71 --selftest` with `git` removed from PATH → `SELFTEST: COULD-NOT-EVALUATE (git unavailable: [Errno 2] No
such file or directory: 'git')`, exit 2.

---

## 3. Structural checks (all pass)

```
$ awk -F'|' '/^\| accept-(c|ca|d)-(71|72|73) \|/ {printf "%s NF=%d\n", $2, NF}' SKILL.md
 accept-c-71  NF=10
 accept-ca-71  NF=10
 accept-d-71  NF=10
 accept-c-72  NF=10
 accept-ca-72  NF=10
 accept-c-73  NF=10
 accept-ca-73  NF=10
```

Ten pipe-split fields = 8 cells with the leading/trailing empties; no cell carries a stray pipe (a stray `|` would
raise NF above 10). All seven rows sit at `SKILL.md:698-704`, contiguous, no other line in SKILL.md mentions these
gate names (`grep -c` = 7).

L08 (registry tail = highest tracked gate):

```
$ python3 -c "import pathlib,re;fs=[(int(re.search(r'round-(\d+)',str(p)).group(1)),p.stem) for p in pathlib.Path('reports').glob('round-*/accept-*.py')];r,n=max(fs);print(n+'-'+str(r))"
accept-ca-73
$ grep -n '^| accept-' SKILL.md | tail -1
704:| accept-ca-73 | gate | `python3 -B reports/round-73/accept-ca.py --root . --lands <40-hex> --fleet-root /home/vgpnk/Projects/sho…
$ python3 -c "import re;s=open('SKILL.md').read();print(re.search(r'(?s).*\| (accept-[a-z]+-\d+) \|', s).group(1))"
accept-ca-73
$ sed -n '697p' SKILL.md | cut -c1-20
| accept-o-69 | gate |
```

`stated_at` (`SKILL.md:697`) and `stated_text` (`| accept-o-69 | gate |`) match the base bytes, and the REPAIR pair's
`statement_after` re-derivation lands on `accept-ca-73` = the tail row = the max tracked gate. L08 reproduces.
Only seven `reports/round-7*/accept-*.py` files exist (71: c, ca, d; 72: c, ca; 73: c, ca), so the maximum is not
an artefact of an untracked script.

SHONEN.md:6 pointers:

```
$ sed -n '505p;564p;20p' SKILL.md
## Error patterns
## Checklist (executable where a tool exists)
## Decision table
$ grep -n '^## Error patterns$' SKILL.md
505:## Error patterns
$ grep -n '^## Checklist' SKILL.md
564:## Checklist (executable where a tool exists)
```

`:505` (Error patterns), `:564` (Checklist) and `:20` (Decision table) all resolve exactly. L04/L05 reproduce.

README footer numbers (the footer lives in **`corpus/README.md`**, not the root `README.md`, which carries no such
text — `grep -n 'Total knowledge entries\|directory totals' README.md` is empty):

```
$ sed -n '775,777p' corpus/README.md
Total knowledge entries: 247.

Counts checked 2026-10-25 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 247 files; directory totals 32/29/38/29/24/95 — linguistics 30 + 2, culture-material 36 → 38 per the L02 correction).
$ find corpus/knowledge -type f -name '*.md' | wc -l
247
$ for d in corpus/knowledge/*/; do printf "%-40s %s\n" "$d" "$(find "$d" -type f -name '*.md' | wc -l)"; done
corpus/knowledge/civilizations/          95
corpus/knowledge/culture-material/       38
corpus/knowledge/linguistics/            32
corpus/knowledge/myth-symbol/            29
corpus/knowledge/synthesis/              29
corpus/knowledge/verification/           24
$ grep -n '^## .*(\([0-9]*\))' corpus/README.md
344:## linguistics/ (30)
376:## myth-symbol/ (29)
407:## culture-material/ (36)
445:## synthesis/ (29)
477:## verification/ (24)
503:## civilizations/ (95)
```

The footer's `32/29/38/29/24/95` is in the README's own heading order (linguistics, myth-symbol, culture-material,
synthesis, verification, civilizations) and each position matches the measured count; the sum is 247; the `247`
matches `find`. The `36 → 38` clause is a statement correction, not a this-round change — at the pinned base
culture-material was already 38 (`git ls-tree -r --name-only 8841ad3b… corpus/knowledge/culture-material` → 38 `.md`)
and linguistics was 30 → 32 — which is what the clause says ("per the L02 correction"). Reproduces.

---

## 4. What I could NOT check

- I never pointed a counter's `--root` at the real lane tree; every run used a clone/`git archive` under `/tmp`. A
  lane-local run could differ only if it reads ignored worktree files; the accept-ca-73 header shows
  `source=lands` for the ledger, so I believe not, but I did not exercise it.
- `accept-c-73`'s CENSUS leg passed only against a **synthetic** fleet root (`/tmp/execskillrows/fleet`, one copied
  `scripts/sources-census.sh`). I did not re-run `scripts/sources-census.sh validate` against
  `/home/vgpnk/Projects/shokunin`; claim C's `census-start.txt`/`census-end.txt` were read as bytes, not re-executed.
- `accept-d-71`'s "2 on usage/env": I exercised the no-`.git` and git-off-PATH branches only; other environment
  failures (unreadable object store, corrupt repo) were not simulated.
- F3: I tested a nonexistent `--root` only. I did not enumerate every malformed input, but the source has no
  `return 2` in either script, so no input can produce 2.
- The six round-70 receipt paths pinned by `accept-ca-71` were confirmed to exist in the script; I did not
  independently re-derive the V70-1..V70-5 legs from the round-70 receipts (the counter's own PASS is the only
  evidence I have for them).
- The content of the S876..S880 registry rows and the two conlang-scholarship entries (claim C's substance) was
  not checked here; that is other seats' lane. `claims.json`'s row map and the counter's `DEFAULT_ROWS` agree.
- I did not check the round-72 report's claim that its `--selftest` was ever run at freeze; only that the number in
  the SKILL.md row reproduces today.

## 5. Hygiene

- Nothing written outside `/tmp/execskillrows/`, `/tmp/execskillrows*` files, `mktemp -d` scratch dirs, and this
  report. Lane git state untouched (`git -C <lane> rev-parse HEAD` = `0316b88…`, only untracked wave files).
- No pacman, no installs, no network fetches (nothing to fetch: every input is committed bytes). No delegation, no
  background jobs, no labrat probe was needed.
- Scratch created: `/tmp/tmp.FafbZEtAQx` (clone at lands), `/tmp/execskillrows.base/base` (clone at base),
  `/tmp/execskillrows/fleet/` (fleet-shaped layout), `/tmp/tmp.J54X3D6uBZ` and `/tmp/tmp.LEg7iR3ZGD` (`git archive`
  exports), `/tmp/execskillrows_*.txt` (captured outputs), plus the counters' own `/tmp/r73-*` selftest dirs.

## 6. Fix list for the canonical writer

1. `SKILL.md:704` self-test cell: `9 scenarios` → `10 scenarios` (F1, BLOCKER).
2. `SKILL.md:703` verdict cell: `: FAIL legs=11/11` → `: PASS legs=11/11` / `: FAIL legs=<n>/11` (F2, BLOCKER).
3. `SKILL.md:698` and `:699` verdict cells: drop `2 input error` or add the branch to both round-71 counters; as
   shipped, an unusable `--root` exits 1 with a traceback (F3, BLOCKER).
4. `SKILL.md:701` self-test cell: replace `(see §5)` with a landed pointer (F4, MAJOR).
5. `SKILL.md:701` entry command: add `[--fleet-root <fleet>]` and disclose the missing-census crash, or make the
   round-72 counter degrade it to a leg / exit 2 like the round-73 counter (F5, MAJOR).
6. `SKILL.md:698` pinned-values cell: note the 36/243 pin is stale and the gate is red at HEAD (F6, MINOR).
