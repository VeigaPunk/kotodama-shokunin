- Seat: R02 | reviewer (second adversarial pass over op/) | claim O | date 2026-10-19 | baseline 139e3b6

# R02 — adversarial review of `op/`: lessons-README delta correctness (row-format parity) and O05's disposition logic

## 0. What was reviewable, and what was not

`op/` at this seat's first read was **empty** (all seats run in one batch). The mission's two
named objects are `op/O02-readme-delta.md` and `op/O05-falsifier-disposition.md`.

| object | state at review | consequence |
|---|---|---|
| `op/O02-readme-delta.md` | **ABSENT at the first read**; landed later in the wave and graded in **§7** | the delta is verified green on its own bytes; one design decision and three defects are filed in §7 |
| `op/O05-falsifier-disposition.md` | landed; read in full | disposition logic reviewed, its central control **re-executed by this seat** (§5) |
| `op/O01-row-drafts.md` | landed; reviewed in full | §2–§4 below; rows re-graded with the filed tool itself |
| `op/K01`, `K02`, `O03`, `O04`, `O07`, `O08`, `P01` | landed; cross-checked | used as the comparison surface; the disagreements are named as findings |
| `op/O06-controls.md` | landed later in the wave; graded in **§8** | eleven controls, sound; its C9 independently corroborates §2's V1 |

Method note: this seat's measurements are its own (raw `wc`/`sha256sum` loops and the filed
tool's own `census()`), not inherited from K02/O01/O04. Where three seats agree (§1) the
agreement is an independent cross-check; where they disagree (§3) the disagreement is the
finding.

## 1. The parity surface, re-measured independently

`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (2026-10-19, lane root,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`), exit **1**:

```
lesson files:  33
index rows:    26
queue rows:    49
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  FAIL C31_index_rows_eq_files   PASS C32_owners_resolve   PASS C33_formats_documented
  PASS C34_pins_rederived        PASS C34c_shape_cells_rederived   FAIL C34b_prose_arithmetic
findings:      2
  C31-1 unindexed-file: ['round-26.md'..'round-32.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26], 'measured': [26, 33]}}
```

`--selftest` → `SELFTEST OK: 28/28 checks passed`, exit **0**.
`index_sha256` = `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`
(29 059 B, 346 lines), matching `sha256sum corpus/lessons/README.md` (two routes, one value).
`git rev-parse HEAD` = `139e3b662900557afe54f632b468619593dc9fcb`; `git ls-files | wc -l` = 2655.

This seat's independent per-file measurement of the seven unindexed files:

| file | bytes | lines | sha8 | format | contract |
|---|---|---|---|---|---|
| round-26.md | 60054 | 222 | cae06660 | gate-keeper | 4/4 |
| round-27.md | 54972 | 203 | f15e285b | gate-keeper | 4/4 |
| round-28.md | 50419 | 145 | dd832ff7 | gate-keeper | 4/4 |
| round-29.md | 17847 | 118 | b6765d33 | gate-keeper | **3/4** (no `recheck:`) |
| round-30.md | 30665 | 181 | 56e77835 | gate-keeper | **3/4** (no `recheck:`) |
| round-31.md | 16637 | 73 | 8870bbdd | gate-keeper | 4/4 |
| round-32.md | 12879 | 66 | 8aacfc2b | gate-keeper | 4/4 |

**O01's drafted row cells match this table on all 21 pin values, all 7 format cells and all 7
contract cells** (`op/O01-row-drafts.md:55-61`); K02 §2/§4 and O04 §1 independently report the
same values. Four-way agreement, no drift.

## 2. O01's rows are parity-correct — proven by the filed tool, not by inspection

`op/O01-row-drafts.md` §6 self-checks its drafts with a re-implementation. That is not
sufficient evidence for a row contract enforced by regexes: the decisive test is the filed tool
itself against a preview of the applied README. This seat ran that test.

Harness (scratch, gitignored): `reports/round-25/audit/c31-lessons-index-audit.py` copied to
`.scratch/c31-copy.py` (verbatim bytes), loaded with `importlib`, with `m.ROOT`/`m.LESSONS`
re-pointed at the lane root and `m.INDEX` pointed at a preview file built from the **live
README bytes** with O01's seven rows extracted verbatim from the fragment and inserted after
`:94`, plus the named prose edits. `m.run_checks()` is then the tool's own verdict.

**Harness bug found and fixed first, recorded so a re-runner does not repeat it:** the copy's
own `ROOT` is `dirname(__file__)/../../..`, which from `.scratch/` resolves to
`/home/vgpnk/Projects` — the first run reported `files 0` and 33 ghost rows. That was a harness
error, not a draft defect; `m.ROOT`/`m.LESSONS` must be overridden explicitly.

| preview | rows/files | queue | checks | verdict |
|---|---|---|---|---|
| **V1** — O01's 7 rows + `:97` → `**Rows: 33. Files: 33.**`, §4 untouched | 33/33 | 49 | **all six PASS, findings 0** | **O01's rows are machine-sufficient and parity-correct** |
| **V2** — V1 + 15 new §4 queue rows, `:207` left at `Rows: **49**` | 33/33 | 64 | FAIL C34b `{queue_rows: {stated: 49, measured: 64}}` | the §4 count is a live C34b surface |
| **V3** — V2 + `:207` → `Rows: **64**` | 33/33 | 64 | all six PASS, findings 0 | the trap is closable |
| **NEG** — O01's rows, `:97` left stale | 33/33 | 49 | FAIL C34b `{table_rows_vs_files: {stated: [26,26], measured: [33,33]}}` | the table leg is live |

Cell-shape facts confirmed mechanically on O01's verbatim rows: **7/7 parse under `ROW_RE`,
7/7 carry all three `CELL_RE` tokens, 6 cells each, `cells[1]`/`cells[2]` exactly
`gate-keeper` and `4/4`|`3/4`** — i.e. C34c re-derives them green.

### 2a. The C34b parser asymmetry, measured (a hardening of O04 §4's warning)

Two probe files isolate the two regexes:

- queue count — `Rows: **49**` then `Rows: **64**` → the tool read **49**: **first match governs**.
- table pair — `**Rows: 33. Files: 33.**` then `**Rows: 26. Files: 26.**` → the tool read
  **[26, 26]**: **last match governs**.

So: any new `Rows: **N**` line above §4 shadows the queue count, and any later
`**Rows: n. Files: n.**` line — **including one written inside §3 to describe class counts** —
shadows the table pair. The delta must keep both shapes unique and correct, in that order.

## 3. Findings, severity-ranked

### F-R02-1 — HIGH (claim-breaking): O01's delta list omits `README.md:207`

`op/O01-row-drafts.md` §5 claims to list "the README bytes that must change with them … so the
two fragments cannot drift apart", and names `:97`, `:1-9`, §3 (`:118-127`, `:134-140`), §4's
new rows, and `:97-104`. It does **not** name `:207` (`- Rows: **49**. Of the 26 index rows,
**23 carry at least one question**;`), which is the **first** `Rows: **N**` match and therefore
the C34b queue leg (`reports/round-25/audit/c31-lessons-index-audit.py:297-298,303-305`).
K02 §7 **does** name it ("must become … 49 + 13 = 62 … iff option (a)"). The two sibling
fragments have already drifted on exactly the surface this seat's mission names.

Reproduced consequence: V2 above — add the §4 rows O01 requires, leave `:207`, C34b reds and
the claim's own counting command exits non-zero. **Remedy:** the delta must carry `:207`, with
the number equal to the queue-row count actually applied, and the second sentence of `:207`
("Of the 26 index rows, **23 carry at least one question**"; "the three that carry none …")
must be restated against the applied rows — O01's r26 cell ("— (no new ids; cites Q-02-1..4,
Q-04-1, Q-14-1, Q-23-1..3)") makes "carries" a judgement, so the delta must state which
convention it used: 4 of the 7 new rows name ids (r26, r30, r31, r32) → `23 → 27` on the
"names any id" reading, or `23 → 26` if a citing row is not a carrying row.

### F-R02-2 — HIGH (decision-blocking): the §4 id set is 13 in K02 and 15 in O01

`op/K02-lessons-census.md` §5 measures that only rounds 30/31/32 declare ids of their own and
that Q-30-4 is resolved (`round-30.md:138`) and Q-30-5 dispositioned (`:146`), so the live
carry is **Q-30-1..3, Q-31-1..4, Q-32-1..6 = 13**; its §7 computes `49 + 13 = 62`.
`op/O01-row-drafts.md` §5 says **"Q-30-1..5, Q-31-1..4, Q-32-1..6 (15 ids)"** and its r30 row
cell reads "Q-30-1..5 (Q-30-4 resolved at the two readers; Q-30-5 attribution defect corrected
in the current retrospective)". Both readings are traceable to the lesson bytes; they are not
the same reading, and the C34b number (62 vs 64) is a function of the choice. This seat's own
id scan agrees with K02's measurement that `Q-30-1..5` are all **declared** in the file (the
question is which are *carried*), and that rounds 26–29 declare none (`grep -o 'Q-2[6-9]-[0-9]*'`
over the four files → zero hits, independently reproduced). **Remedy:** one owner (parent)
decides the id set; the Revision 3 block states the set, the count and the arithmetic; a row
cell that cites a closed-at-source id must say so in the cell, as O01's does.

### F-R02-3 — HIGH (honesty): the machine legs cannot distinguish V1 from V3

V1 is **fully green with findings 0** while leaving §4's traceability rule
(`corpus/lessons/README.md:227-232`) unmet for the new ids — the exact gap O01 §5 and K02 §5
both name. Claim O's counting command (`c31-lessons-index-audit.py` exit 0) and its threshold
("C31/C34b PASS + findings == 0") therefore **cannot certify §4 coverage**; they certify the
row/file set, the pins, the shape cells and the two prose counts only. Consequence for the
record: a machine-green round may ship with 13–15 ids unowned in the index, and
`C32_owners_resolve` stays green because C32 only inspects rows that exist
(`:213-227` — "C32 does not fire on absent rows", O01 §5, reproduced in V1). **Remedy:** the
receipt (`O08`/`S01`) must declare which option was taken (rows added vs prose pointers) and
must not present "findings: 0" as covering §4; route to `cross/X04-honesty.md`.

### F-R02-4 — MEDIUM (provenance): adding rows in place contradicts §0's stamp unless a Revision 3 block lands

`corpus/lessons/README.md:22-29` states "Every `bytes=` / `lines=` / `sha8=` cell below was
re-measured from the live bytes at **2026-10-18T17:35Z**". Seven rows measured on 2026-10-19
make that sentence false for those rows. `README.md:303-305` supplies the file's own rule:
"Superseding edits land as a new revision block here, never as an in-place rewrite of the
per-round rows' provenance claims." The filed lesson `corpus/lessons/round-32.md:45` already
names this operation on the record — "rows are parent-owned additions, never edits". Round 26's
precedent (`reports/round-26/zzz-lessons-index-revision-3.md`, `…-revision-4.md`) is a
**separate revision file**, which cannot satisfy round 33 (below, F-R02-5). **Remedy:** the
delta must append a dated **Revision 3 block** stating: the seven rows added, their measurement
stamp and tool, that revision-1/2 rows' provenance claims stand unedited, and the post-edit
anchor numbers (F-R02-6). Without it, the applied file carries a self-contradiction the tool
cannot see.

### F-R02-5 — MEDIUM (pin cascade): the README edit reds a filed runner, and two digest pins become stale

- `reports/round-26/run-validation.py:97` pins `README_BASELINE_BLOB = "a31870556c733498…"`
  and `:1494-1500` asserts `corpus/lessons/README.md`'s Git blob equals it — round 26's claim C
  **required** a new-file revision. Editing the README in round 33 makes that filed runner go
  red **if it is re-run**. It is not among round 33's counting commands, so the honest handling
  is a declared supersession in the round's LOG entry, not silence — and `tools/gates/frozen/**`
  is untouched either way.
- `reports/round-25/validation.json:1020` pins the README sha256 `ec7469da…` (a stamp
  measurement), and `op/O07-baseline-receipt.md` lists the same digest under **"Digest pins
  (regression comparison anchors)"**. That list must not be read as "these bytes are invariant":
  claim O's whole point is that the README moves. The four named selftests (battery 44/44, craft
  10/10+18/18, d4 81/81, c31 28/28) are the invariance surface; the README digest is an
  expected-move surface.
- The structural reason the README has been stale since `fc13cd2` (its only commit,
  `git log --oneline -- corpus/lessons/README.md` → one row): the round-25 tool hardcodes
  `INDEX = corpus/lessons/README.md` (`:36`), while rounds 26–28 filed *new revision files*
  instead (`reports/round-26/zzz-lessons-index-revision-3.md:7`, `C51-C52.md:26`,
  `C53.md:296`). A revision file elsewhere can never close C31. Round 33's `shared_rules`
  carve-out ("the lessons README … drafted by seats and applied by the integrator") is what
  authorizes the edit; the delta should cite it.

### F-R02-6 — MEDIUM (integration mechanics): every later README anchor shifts by +7

Inserting 7 rows after `:94` moves: `:97`→`:104`, `:111`→`:118`, `:144`→`:151`, `:207`→`:214`,
`:234`→`:241`, `:279`→`:286`, `:307`→`:314`. K02 §7, O04 §5 and O01 §5 all cite **pre-edit**
numbers. **Remedy:** apply every edit by content match (the exact current strings are quoted in
K02 §7 and O04 §5), and have the Revision 3 block carry post-edit anchors; a delta that
instructs "edit line 207" after its own earlier insertion lands on the wrong line.

### F-R02-7 — LOW (factual error in O01 §4): round-32.md *is* pinned by a filed artifact

`op/O01-row-drafts.md` §4: "`round-32.md` is pinned only by the live read — no filed artifact
pins it." False: `reports/round-32/scribe/fragment-ledger.md:273` pins "`corpus/lessons/round-32.md`
(12879 bytes, sha256 prefix `8aacfc2bd9f5`, …)". The value agrees with the live read, so no
numeric harm — but the provenance sentence is wrong as written and should be corrected rather
than carried. (The six-file corroboration via `corpus/lessons/round-32.md:45` is accurate: this
seat read the filed table and all six triples match live bytes.)

### F-R02-8 — LOW (divergence): three disposition-pointer cells differ between K02 §6 and O01 §2

r30 → K02 `reports/round-30/routed-resolution.json` (+validation.json) vs O01
`reports/round-30/validation.json` (+routed-resolution.json); r31 → K02
`reports/round-31/closure-ledger.json` (+final-sweep.md) vs O01 `…/validation.json`
(+closure-ledger.json); r32 → K02 `reports/round-32/completion-ledger.json` (+final-dossier.md)
vs O01 `…/validation.json`. Every named surface exists, and the column is hand-checked only
(`README.md:309-313`, and the round-4 pointer defect at `:314-323` is the precedent for why it
still needs a human). Parity with the filed rows favours O01: **11 of the 26 existing §2 rows
name a `reports/round-N/validation.json`** — it is the modal pointer form (O03's C32 leg is
about queue owners, not this column). **Remedy:** pick one, and have the delta state which
fragment it followed.

### F-R02-9 — LOW (tool blind spots and pre-existing stale prose the delta must fix or decline)

C34b reads exactly two surfaces (`:297-300`); C33 is a substring test (`:229-235`), so it
passes while §3's histogram says gate-keeper **14** against a measured **21** (O04's F2, this
seat's §1). Lines carrying counts the tool never reads, all currently stale or about to be:

| line | now | note |
|---|---|---|
| `:6` | "(26 at the" | opening census paragraph |
| `:35` | `# 26/26, exit 0` | **already wrong at baseline** — live selftest is 28/28 (`:55` says 28, `:285` says 26/26) |
| `:39`, `:40` | `# 26 (2026-10-18)` | the two counting-command comments |
| `:140` | "Total 26 = the runner's file set" | §3 histogram arithmetic |
| `:207` | "Of the 26 index rows, **23 carry at least one question**" + "the three that carry none" | second sentence of the C34b anchor line |
| `:256-257` | "146 files under nine directories beside the 26 `*.md` lesson files" | 146/9 still correct (re-measured: 146 files, 9 dirs); only "26" moves |
| `:285` | "the tool's `--selftest` is 26/26 in-memory checks" | **already wrong at baseline** — live 28/28 |
| `:325` | "146 files under nine directories" | still correct |

`:285` and `:35` are a **pre-existing self-contradiction** (§1 `:55` and revision 2 `:338` both
say 28) that no round-33 fragment lists. The delta should correct both, or the receipt must
decline them explicitly as out-of-scope-for-claim-O; leaving them silently stale while
"reconciling" the file is the failure mode the round-25 claim C31 exists to prevent.

### F-R02-10 — LOW (documentation): O04's F1 H2 sub-shape finding is confirmed independently

This seat's own scan: `^## [DOCA] — ` occurs in **exactly four files, rounds 29 (3), 30 (3),
31 (3), 32 (1)**, and `^### [DOCA] — ` occurs **zero times** in those four. So the H2 per-axis
form is genuinely introduced by this batch, and §3's sub-shape sentence (`README.md:119-122`,
which names only rounds 21–23) does not cover it. Not a class violation (both forms classify
`gate-keeper`; C33 cannot see it) — a §3 documentation gap the delta should close, as O04 §5
item 2 drafts.

### F-R02-11 — LOW (shared-file stray, report-only): `AGENTS.md:42`

`AGENTS.md` ends with a bodyless heading at `:42`:
`### 2.2 \`SKILL.md\` — append one item to "## Checklist (executable where a tool exists)" (after :534)`.
It is the file's last line, has no body, and sits outside the file's own section structure — an
instruction-shaped fragment that a seat or integrator could mistake for authorization. This seat
edits nothing; reported for `cross/X02-conformance.md` / `A08`. Related citation check that came
out **clean**: "the checklist section ends at :534" (K01 §2, O05 §3c) is correct — `## Checklist`
heads at `:522`, its last content line is `:534`, `:535` is blank and `:536` is `## Corpus map`.
Do not "fix" that citation.

## 4. The parity spec + checker (the O02-grading deliverable)

Run from the lane root with `TMPDIR=$PWD/.scratch`, with the script placed at
`<lane-root>/.scratch/r02-parity.py` (it derives `ROOT` as `dirname(__file__)/..`, which is the
lane root from that path — the exact verified placement). Verified behaviour this session:

- live `corpus/lessons/README.md` → `FAILS=2` (`P1 unindexed-file` = the seven; `P10 table
  prose [26,26] != measured [26,33]`) — **the same two defects the filed tool reports**, plus
  a 13-line inventory of the tool-blind prose in §F-R02-9.
- positive control (a synthetic README carrying all 33 rows and the 49 real queue rows) →
  `FAILS=0` — so the acceptance criterion is reachable, not vacuous.
- negative controls: one row removed → `P1`; one `sha8` poisoned → `P5` (`round-31.md: sha8
  cell deadbeef != live 8870bbdd`).

It adds the checks the filed tool does not make: **all three `bytes=`/`lines=`/`sha8=` tokens
present per row** (the tool compares only the keys it finds, so a partially-pinned row passes
`C34` today), **exactly 6 cells per row** (column parity), and a report of every non-table line
carrying a stale-count token.

```python
#!/usr/bin/env python3
"""R02 parity checker: re-derives the lessons-index row contract from the live
round-25 tool's regexes and applies it to a candidate README. Read-only."""
import glob,hashlib,os,re,sys
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
LESSONS=os.path.join(ROOT,"corpus","lessons")
INDEX=os.path.join(LESSONS,"README.md")
ROW_RE=re.compile(r"(?m)^\|\s*`?corpus/lessons/([A-Za-z0-9_.-]+\.md)`?\s*\|(.*)\|\s*$")
CELL_RE=re.compile(r"(bytes|lines|sha8)=([0-9a-f]+|self-referential)")
CONTRACT=("source:","verified-at:","recheck:","scope:")
def sha8(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()[:8]
def cls(t):
    if re.search(r"^## Fragment index\s*$",t,re.M): return "fragment-index"
    if re.search(r"^## Gate\s*$",t,re.M): return "gate-keeper"
    return "plain"
def census():
    out={}
    for p in sorted(glob.glob(os.path.join(LESSONS,"*.md"))):
        n=os.path.basename(p); t=open(p,encoding="utf-8").read()
        out[n]={"bytes":os.path.getsize(p),"lines":len(t.splitlines()),"sha8":sha8(p),
                "format":cls(t),"contract":f"{sum(1 for k in CONTRACT if re.search(rf'^{k}',t,re.M))}/4"}
    return out
def main(path=None):
    path=path or INDEX
    text=open(path,encoding="utf-8").read()
    live=census(); fails=[]; warns=[]
    rows=[]
    for line in text.splitlines():
        m=ROW_RE.match(line)
        if not m: continue
        name=m.group(1)
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        pin=dict(CELL_RE.findall(line))
        rows.append((name,cells,pin,line))
    names=[r[0] for r in rows]
    miss=sorted(set(live)-set(names)); ghost=sorted(set(names)-set(live))
    dup=sorted({n for n in names if names.count(n)>1})
    if miss: fails.append(f"P1 unindexed-file: {miss}")
    if ghost: fails.append(f"P2 ghost-row: {ghost}")
    if dup: fails.append(f"P3 duplicate-row: {dup}")
    for name,cells,pin,line in rows:
        if name not in live or name=="README.md": continue
        if len(cells)!=6: warns.append(f"W1 {name}: {len(cells)} cells (parity: 6)")
        for k in ("bytes","lines","sha8"):
            if k not in pin: fails.append(f"P4 {name}: missing {k}= token (tool blind to this; parity requires it)")
        for k in ("bytes","lines","sha8"):
            if k in pin and str(live[name][k])!=str(pin[k]):
                fails.append(f"P5 {name}: {k} cell {pin[k]} != live {live[name][k]}")
        if len(cells)>=3:
            if cells[1]!=live[name]["format"]: fails.append(f"P6 {name}: format cell {cells[1]} != live {live[name]['format']}")
            if cells[2]!=live[name]["contract"]: fails.append(f"P7 {name}: contract cell {cells[2]} != live {live[name]['contract']}")
    # queue rows
    qn=0
    for line in text.splitlines():
        if line.startswith("| Q-") and not line.startswith("| Q-id"):
            qn+=1
            parts=[c.strip() for c in re.split(r"(?<!\\)\|",line.strip().strip("|"))]
            if len(parts)!=4:
                fails.append(f"P8 malformed queue row ({len(parts)} cells): {parts[0] if parts else '?'}")
    stated={}
    for m in re.finditer(r"Rows:\s*\*\*(\d+)\*\*",text): stated.setdefault("queue",[]).append(int(m.group(1)))
    for m in re.finditer(r"\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*",text): stated["table"]=[int(m.group(1)),int(m.group(2))]
    if stated.get("queue") and stated["queue"][0]!=qn: fails.append(f"P9 queue prose {stated['queue'][0]} != measured {qn}")
    if stated.get("table") and (stated["table"][0]!=len(rows) or stated["table"][1]!=len(live)):
        fails.append(f"P10 table prose {stated['table']} != measured {[len(rows),len(live)]}")
    # tool-blind prose counts
    blind=[(i,l) for i,l in enumerate(text.splitlines(),1)
           if re.search(r"\b(26|27|28|49|146)\b",l) and not l.startswith("|")]
    print(f"index rows={len(rows)} files={len(live)} queue={qn}")
    print(f"FAILS={len(fails)}")
    for f in fails: print("  "+f)
    print(f"WARNS={len(warns)}")
    for w in warns: print("  "+w)
    print(f"tool-blind prose lines carrying stale-count tokens: {len(blind)}")
    for i,l in blind: print(f"  :{i}: {l.strip()[:110]}")
    return 1 if fails else 0
if __name__=="__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else None))
```

**What O02 must satisfy to pass this review** (each item is a check, not an opinion):
`P1/P2/P3` clean; `P4/P5` clean for all 33 rows; `P6/P7` clean (5×`4/4`, 2×`3/4` among the new
rows); `P8` clean for every new queue row (exactly 4 cells, escaped inner pipes); `P9` = the
queue count actually applied (49 + the F-R02-2 decision); `P10` = `[33, 33]`; plus an explicit
disposition — fix or decline, stated — for each §F-R02-9 line, and the Revision 3 block of
F-R02-4.

## 5. O05's disposition logic — reviewed, and its central control re-executed

Verdict: **the disposition logic is sound and the fix is bounded, correctly typed, and
reproduced here.** Specific checks:

1. **The counting-command trap is acknowledged.** `test -s
   reports/round-33/op/O05-falsifier-disposition.md` passes on any non-empty file, so the
   artifact's own content carries the claim. O05 does not rely on the file's existence: it
   carries a located finding, a before/after byte pair, and a control table.
2. **Located, not asserted.** Independently reproduced by this seat at HEAD: the `SKILL.md:715`
   one-liner verbatim → **5 rows**, exit 0; `SKILL.md` sha256 `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`, `wc -l` 715; `closes_record` occurs **2×** in
   `corpus/lessons/round-32.md` and **0 files** under `reports/round-*/telemetry/*.json` — so
   O05's §2.1 trap ("a re-keyed audit that tested `closes_record` would false-fire a second
   time") is a real hazard, not a hypothetical.
3. **The draft's own command works.** This seat extracted the §3b one-liner **verbatim from the
   fragment bytes** (515 chars, no embedded newline — O05's `newline_in_command=False`
   reproduced) and ran it on the live tree: **0 rows**, exit 0, against OLD's 5. The false fire
   is cleared by the draft's bytes, tested from the fragment rather than from a retyped copy.
4. **The control set is a control, not a demonstration.** `legacy-name-only` (a file literally
   named `telemetry/closing-snapshot.json`, no valid snapshot) is where OLD says green and NEW
   says red — the pair that proves the old green was name-based. The three "still fires"
   scenarios (unclosed, digest-mismatch, wrong-pointer) each target a distinct failure of the
   replacement predicate, and the two non-falsifiers (receipt-absent, pre-convention `state:
   null`) keep the audit's scope unchanged.
5. **The fix does not rewrite filed bytes.** The target is `SKILL.md:713-715` — a shared file,
   which round 33's `shared_rules` explicitly route as draft-then-integrator-applies. The
   alternative (reword LOG.md clause (i)) is correctly marked append-only, and D-3
   (`closes_record` in the filed lesson) is correctly classed carried-with-owner, since
   `corpus/lessons/round-32.md` is a filed lesson. No row is unassigned; no row claims a
   promotion/canon/closure verdict.
6. **One cascade O05 does not name (new).** Applying §3b changes `SKILL.md`'s bytes, and the
   round-32 dossier binds box 1's **closed** inventory condition to the current bytes:
   `reports/round-32/dossier-d11-shonen-boxes.md:205` ("inventory condition closed, 28/28
   re-verified at `79fe91d3…`"), `dossier-d12-capability-inventory.md:97`,
   `dossier-d13-operator-decisions.md:48`, `final-dossier.md:46` (with the command
   `python3 -B reports/round-30/craft/box1-survey.py`, which exists, sha8 `d923ae0f`) and
   `:133`, `scribe/fragment-ledger.md:178,235`. After the edit, `79fe91d3…` no longer describes
   HEAD. This does not block claim O (round 33 makes no promotion verdict), but the integrator
   should **re-run `python3 -B reports/round-30/craft/box1-survey.py` after applying §3b** and
   record the new SKILL sha with the result, so the condition is re-bound rather than left
   silently stamp-stale. Recommended as a one-line addition to O05 §5's D-1 row.
7. **Honest limits, correctly filed.** The malformed-snapshot traceback is declared as a
   preference for loud failure; the §6 adjacent exposure
   (`reports/round-31/run-validation.py:780`'s name-exact closure test) is routed, not absorbed,
   with a demonstrated fixture. That is the correct posture for a filed-round artifact.

## 6. What this review could not do at its first read

`op/O02-readme-delta.md` and `op/O06-controls.md` were absent when §0–§5 were written; both
landed later in the wave and are graded in §7/§8 below. The §0–§5 text is left as the record of
the first read. Rows graded in §2 were graded against the live partition at HEAD; any later
write to a `corpus/lessons/round-*.md` byte moves the pins and voids V1/V3's green.

## 7. Addendum — `op/O02-readme-delta.md` graded (the mission's primary object)

**Verdict: the delta is correct, complete on the machine surface, and independently verified
green — with one design decision the round must make explicitly and three small defects.**

Its own scratch reconstruction survived (`.scratch/o02/proposed-README.md`) and its digest
**matches O02 §3's claim exactly**: sha256
`335bb22ab68f39f3fddc8224d2556bda17329e6d7258f972df14f320c2c6a7f5`, 43 261 B, 446 lines. So
the review is of the actual proposed bytes, not of prose about them.

| check | result |
|---|---|
| filed tool (`run_checks()` with `INDEX` patched to the proposed bytes) | 33 rows / 33 files / 78 queue / `{gate-keeper 21, fragment-index 5, plain 7}` — **all six checks PASS, findings 0** — O02's central claim reproduced |
| R02 parity checker (§4) | `FAILS=0`, `WARNS=0` — 33 rows × 6 cells, all three pin tokens present per row, every format/contract cell re-derived; 78 queue rows each exactly 4 cells |
| D6 owner arithmetic, via the tool's own `resolves()` | filed 49 = **37 path + 12 role-token**; added 29 = **22 path + 7 role-token**; totals **59 / 19**, added role tokens `parent` 6 + `operator` 1 → **parent 15, operator 4** — every number in D6, including its parenthetical, is exact |
| D1's 21 receipt-derived values | all correct: `acceptance_checks_passed: true` ×7, `measured_at_utc` ×7 (O02 writes `Z` where r26–r28/r30–r32 carry `+00:00` — same instant, notation only; r29 carries a literal `Z`), runner sha8 ×7 = `73297683, 36b59706, 20e09ea8, 59df391b, 2f447223, 9e01c427, 6fd1b96e` |
| D7 counts | `find corpus/lessons -mindepth 2 -type f \| wc -l` → 146; `… -mindepth 1 -maxdepth 1 -type d \| wc -l` → 9 — both confirmed |
| D8's revision block re-tripping C34b | does not: the proposed bytes grade findings 0, so the block's non-quoting wording works as O02 claims |
| pointer cells vs siblings | O02's seven pointers all name `reports/round-N/validation.json` — the modal filed form (11/26 rows), consistent with O01 and with F-R02-8's recommendation |

### F-R02-12 — HIGH: O02 mints 17 ids that O01 and K02 both say do not exist, and the mix is machine-green

O02's D1 rows carry `Q-26-1, Q-26-2` / `Q-27-1..4` / `Q-28-1..5` / `Q-29-1..3`, and its D5
defines all of them. O01's rows carry `—` for those same four files (and "no new ids" for r26);
K02 §5 measured "`Q-26-*` does not exist" and "none minted or cited" for rounds 26–29. O02 is
**honest** about this — §D5's provenance note says the rounds 26–29 rows are "first-assigned ids
with the lesson's own wording condensed", each citing a lesson line — so this is a declared
mint, not a fabrication. Three consequences:

1. The round now has **three incompatible §4 designs**: K02's 13 ids (`49 + 13 = 62`), O01's 15
   ids (`49 + 15 = 64`), O02's 29 rows (`49 + 29 = 78`). All are defensible readings; only one
   can be applied.
2. **The §2 cells and the §4 rows must come from the same design.** O01's row for r26 says the
   file carries no ids; O02's §4 defines `Q-26-1`/`Q-26-2`. Applying O01's rows with O02's §4
   makes the index assert that ids it indexes do not exist.
3. **The tool cannot catch that.** Reproduced: O01's seven rows transplanted into O02's proposed
   bytes (its 29-row §4, its D2/D6 prose) grade **all six checks PASS, findings 0**. So this is
   the sharpest instance of F-R02-3: a green counting command is not evidence that the index is
   internally consistent, only that its arithmetic and its file set are.

**Remedy:** the integrator applies **one** fragment's §2 rows together with **that fragment's**
§4 treatment (O02's D1+D5 is self-consistent and verified green; O01's rows + a K02-style
13-row §4 is V1/V3-green), and states in the Revision 3 block which design was applied and how
many ids it mints. Mixing is the failure mode.

### F-R02-13 — MEDIUM: D3 fixes one stale selftest count and leaves its twin

D3a corrects `README.md:35` (`# 26/26, exit 0` → `# 28/28, exit 0`) and D3's own rationale names
that contradiction. But `README.md:333` — "**Controls:** the tool's `--selftest` is 26/26
in-memory checks" — is **still stale in the proposed bytes** (the §4 checker's blind-line
inventory lists `:333` on the proposed file). Live selftest is 28/28 and §1's own prose
(`:55`) says 28. Same class of defect, same file, same round: fixing one instance and leaving
the other is the outcome §F-R02-9 warns about. **Remedy:** add `:333` to D3 (one line, no
regex exposure — "26/26" is not one of C34b's two shapes).

### F-R02-14 — MEDIUM: D5's insertion point splits the §4 table

D5 says "insert immediately before `### Queue arithmetic`". The live bytes are `:200` (last
filed queue row), `:201` (blank), `:202` (`### Queue arithmetic`). Inserting immediately before
the heading therefore lands the 29 rows **after the blank line**, so the filed table and the new
rows render as two separate tables and the new rows are not contiguous with the table they
extend. The tool is line-based (`line.startswith("| Q-")`) and cannot see this. **Remedy:**
insert after `:200`, before the blank line — or state the split deliberately.

### F-R02-15 — LOW: the default D1–D8 leaves the header parenthetical stale

D0 is optional and excluded from the reconstruction digest, so the recommended application
leaves `README.md:6`'s "(26 at the final stamp …)" as a current-state claim that the file's own
revision-3 block contradicts. O02 declares this and measured the `D0+D9` variant
(`c842cb65…`) green, which is honest — the receipt should simply say whether D0 was applied.

### F-R02-16 — LOW: insertion-position divergence across the three drafts

O01 inserts before the supplement row (`:95`); O02's D1 inserts after it; O06's harness inserts
after the last `ROW_RE` match (its `:461,468,555-556`), i.e. also after the supplement. Order is
invisible to every check, but the filed table keeps the non-round-numbered
`supplement-opencode-1.md` row last. Pick one — O01's position preserves the filed ordering —
and state it.

*Also verified clean:* D9 rewrites the file's own closing rule sentence (`:303-305`) and the
proposed bytes stay green, so the rewrite breaks no regex and preserves the rule's text.

## 8. Addendum — `op/O06-controls.md` reviewed

**Verdict: sound, and it independently corroborates §2's V1.** Eleven controls (C0–C9), each
with a named expected finding class, expected check and expected exit. Its two digest pins were
**re-verified by this seat against the live scratch files**: `.scratch/o06-controls.py` →
`1263f15686ce2662669e8a2b9d21222b2424d117a7e057fa72085bc8262a0d2d`, `.scratch/o06-receipt.json`
→ `9e500c14e22bafdfd06d5630fb53f651ae4bacbb695c8f1e63aa7cd2b6024549` — both exact.

- **C9 corroborates V1 from a second instrument.** O06 applied O01's seven drafted rows and
  reached `findings: []`, exit 0 — the same verdict this seat reached by a different harness
  (§2 V1). Two independent applications of the same draft, one answer.
- **C8 is a real catch, verified directly by this seat.** On the live tree (2 findings present):
  `… --json > /dev/null` → **exit 0**, while the plain mode → **exit 1** — matching the tool's
  `main()` (`reports/round-25/audit/c31-lessons-index-audit.py:444-447`, which returns 0 in json
  mode before the finding-count return). The integrator must file the **plain** mode's exit as
  the claim's counting-command result; a `--json` receipt alone is not a verdict.
- C4a/C4b derive each lie from the measurement (`measured+1` / `stated+1`) rather than
  hardcoding a number, so the lies cannot silently become true after the edit; C5 proves the
  target state is reachable; C6/C7 exercise the pin and shape-cell drifts that §2a's probes
  touch from the other direction. **No conflict** with §2a's measured first-match/last-match
  asymmetry: O06 mutates the two prose surfaces and expects the two right classes.
- O06 §8's own limit ("They do not verify the content of O02's new queue rows") is exactly
  F-R02-3/F-R02-12, stated honestly by the author.
- One advisory: C9's phrase "the arithmetic they imply" is ambiguous about the §4 queue count.
  If a re-runner reads C9 as covering O01's rows *plus* O02's D5/D6, the green says nothing
  about the §2/§4 id consistency (F-R02-12); O06 should say which arithmetic C9 applied.

## Owed

- `reports/round-33/op/O08-receipt.md` / `scribe/S01-op-receipt.md` — the receipts must carry:
  (i) which §4 design was applied and how many ids it mints (F-R02-12), (ii) the **plain**-mode
  exit of the counting command, not `--json` (§8), (iii) whether D0/D9 were applied
  (F-R02-15), and (iv) the §F-R02-9 disposition of `:333` (F-R02-13).
- `reports/round-33/op/O03-owner-checks.md` — its per-item verdicts should be read against the
  applied §4 design; its table predates O02's 29-row set.
- Nothing else: O02 and O06 both landed and are graded above.

## Citations

- `reports/round-25/audit/c31-lessons-index-audit.py` — `:36` hardcoded `INDEX`, `:42` `ROW_RE`,
  `:45` `CELL_RE`, `:47-54` format markers, `:56` contract keys, `:72-89` `classify`/
  `contract_lines`, `:119-135` `parse_index`, `:138-167` `owner_cell`/`resolves`, `:213-227`
  C32, `:229-243` C33 substring test, `:245-291` C34/C34c, `:293-317` C34b (first-match queue,
  last-match table), `:337-432` selftest.
- `corpus/lessons/README.md` — `:22-29` the re-derivation stamp sentence, `:35`, `:39`, `:40`,
  `:55`, `:94`, `:95`, `:97`, `:111-142` (§3 taxonomy and histograms), `:119-122` sub-shape
  sentence, `:144`, `:200`, `:207`, `:227-232` traceability rule, `:234`, `:247-250`
  disposition-pointer rule, `:256-257`, `:279`, `:285`, `:303-305` revision-block rule, `:307`,
  `:309-313`, `:314-323`, `:325`, `:338`.
- `corpus/lessons/round-26.md` … `round-32.md` — the seven lesson bytes; `round-30.md:138,146`;
  `round-32.md:36,41,45,55`; `round-16.md` (the 3/4 precedent).
- `reports/round-33/op/O01-row-drafts.md` §2 (the rows), §4, §5, §6; `op/K02-lessons-census.md`
  §2, §4, §5, §6, §7; `op/O04-format-checks.md` §1, §2 F1/F2, §4, §5; `op/O03-owner-checks.md`
  §0–§2; `op/O05-falsifier-disposition.md` §1, §2, §3a/§3b/§3c, §4, §5, §6;
  `op/O07-baseline-receipt.md` (four commands + digest pins); `op/K01-falsifier-scout.md` §1–§5;
  `op/P01-plan.md` §2.2.
- `reports/round-26/run-validation.py:97,1494-1500` (README blob assertion);
  `reports/round-25/validation.json:1020` (README sha256 pin);
  `reports/round-26/zzz-lessons-index-revision-3.md:7`,
  `reports/round-26/lessons/C51-C52.md:26`, `C53.md:296` (the new-file revision precedent);
  `reports/round-26/audit/x63-lessons-audit.md:219` (no README write);
  `reports/round-32/scribe/fragment-ledger.md:273` (round-32.md's filed pin);
  `reports/round-32/dossier-d11-shonen-boxes.md:205`, `dossier-d12-capability-inventory.md:97`,
  `dossier-d13-operator-decisions.md:48`, `final-dossier.md:46,133`,
  `scribe/fragment-ledger.md:178,235` (the `79fe91d3…` box-1 pins);
  `reports/round-30/craft/box1-survey.py` (exists, sha8 `d923ae0f`);
  `reports/round-19/telemetry/availability-close-19.json:4-5` (key `closes`, not
  `closes_record`); `reports/round-31/run-validation.py:780,792-812`.
- `SCORECARD.md:427-445` (round-32 record, `:443-445` the routed-debt sentence);
  `SKILL.md:522`, `:534`, `:660`, `:713-715`; `AGENTS.md:42` (the bodyless heading);
  `reports/round-33/claims.json` (claim O), `reports/round-33/targets.json` (seat R02,
  `shared_rules`).
- Commands (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`; `git ls-files | wc -l` →
  2655; `git log --oneline -- corpus/lessons/README.md` → one commit `fc13cd2`;
  `git hash-object corpus/lessons/README.md` → `a31870556c733498243b56697896504a2fb3679a`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1, output quoted in §1;
  `… --json` → `index_sha256` `ec7469da…`; `… --selftest` → 28/28 exit 0;
  `sha256sum corpus/lessons/README.md` → `ec7469da…` (29 059 B); per-file
  `wc -c`/`wc -l`/`sha256sum | cut -c1-8`/`grep -c '^## Gate$'` over the seven files (§1 table);
  `grep -o 'Q-2[6-9]-[0-9]*' corpus/lessons/round-{26,27,28,29}.md` → zero hits;
  `awk`/`grep` counts over the §2 rows (11 of 26 name `validation.json`) and the §4 queue
  (49 rows; `grep -c '^| Q-'` → 50 lines including the header);
  `grep -c '^## [DOCA] — '` / `'^### [DOCA] — '` per file (H2: 29×3, 30×3, 31×3, 32×1, zero
  elsewhere) — F-R02-10;
  `find corpus/lessons/*/ -type f | wc -l` → 146 over 9 directories (`:256-257`, `:325` still
  correct);
  harness `.scratch/c31-copy.py` + `importlib` with `m.ROOT`/`m.LESSONS` overridden, previews
  V1/V2/V3/NEG and probes A/B (§2, §2a); positive/negative controls via `.scratch/r02-parity.py`
  (§4); `sed`/`re` extraction of O05 §3b's one-liner (515 chars, no newline) and its execution
  on the live tree → 0 rows vs OLD 5 rows (§5.3);
  `grep -c closes_record corpus/lessons/round-32.md` → 2;
  `grep -l closes_record reports/round-*/telemetry/*.json` → 0;
  `sha256sum SKILL.md` → `79fe91d3…`; `wc -l SKILL.md` → 715;
  `ls reports/round-33/op/` at each read (§0; O02 and O06 absent at the first read, landed
  before this fragment closed).
- Commands of the §7/§8 addendum (same stamp and env): `sha256sum .scratch/o02/proposed-README.md`
  → `335bb22ab68f39f3fddc8224d2556bda17329e6d7258f972df14f320c2c6a7f5` (43 261 B, 446 lines —
  matches O02 §3); `python3 -B .scratch/r02-parity.py .scratch/o02/proposed-README.md` →
  `FAILS=0 WARNS=0`; `importlib` + `m.INDEX=.scratch/o02/proposed-README.md` → 33/33/78, six
  PASS, findings 0; owner classes over the queue rows via the tool's `owner_cell`/`resolves`
  → filed 49 = 37 path + 12 role-token, added 29 = 22 path + 7 role-token, added role tokens
  `parent` 6 + `operator` 1; `json.load` over `reports/round-{26..32}/validation.json` for
  `acceptance_checks_passed`/`measured_at_utc`/`runner_sha256[:8]` → all 21 values match O02's
  cells; `find corpus/lessons -mindepth 2 -type f | wc -l` → 146 and
  `find corpus/lessons -mindepth 1 -maxdepth 1 -type d | wc -l` → 9;
  **MIXED build** (O01's seven rows transplanted into O02's proposed bytes at
  `.scratch/o02-mixed-with-o01-rows.md`) → 33/33/78, six PASS, findings 0 — F-R02-12's evidence;
  `sha256sum .scratch/o06-controls.py` → `1263f156…` and `.scratch/o06-receipt.json` →
  `9e500c14…` (both match O06's pins);
  `… --json > /dev/null` → exit **0** while the plain mode → exit **1** on the live tree with
  2 findings present (O06's C8, verified directly).
