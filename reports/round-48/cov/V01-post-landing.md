# V01 — cartography landing: post-landing verification (claim C)

- Seat: `V01` | role: verifier | claim: **C** (coverage) | round 48, loop 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json` `baseline_commit` `a01405d`
- Out path: `reports/round-48/cov/V01-post-landing.md` (this file)
- Write surface: this file only. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was written. Scratch rehearsal lives under `.scratch/` (disposable; the durable copy of the harness is §7 below).
- Non-author statement: I drafted no part of the C entry, header, or README edit, and I judged no fragment's prose. This seat builds and proves the **post-landing measurement**, not the content.

**One-line judgment.** The landing is **not applied at my seat time** (the target path does not exist — §1.4), so the post-landing state is `could-not-evaluate` and I certify nothing about the landed bytes. What I can certify is the instrument: a nine-leg receipt that exits 1 against the live pre-apply tree, exits 0 against a staged 224 tree, and fails on each of five planted defects. The material finding is that **`reports/round-28/readme/sweep.py` alone cannot certify this claim**: it returns `ok: true` on a 260-line entry, on an unsorted row, on two entries with identical `- topic:` lines, and on a duplicated row (`rows 225 files 224`). The claim's `after_required` therefore needs the external legs in §3, not a sweep-green assertion.

---

## 1. Pre-landing invariants measured at `a01405d`

Everything the receipt will assert about the post-state is pinned here first, so the post-state is a **delta** from a measured baseline, not a remembered one.

### 1.1 Census and partition shape

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
```

Culture-material length discipline (`wc -l corpus/knowledge/culture-material/*.md`):

```
n 25  min 103  median 149  mean 150.2  max 221  total 3756
sorted [103,109,112,113,124,129,130,131,140,142,143,143,149,149,
        154,156,162,166,173,175,175,177,179,201,221]
```

The live max is `funerary-material-culture.md` at **221**. The claim's band is `<=~250`; a landed entry at 222–250 would therefore be a new partition max — inside the claim but outside the partition's observed envelope. The receipt reports that as a note, not a pass.

### 1.2 README anchors (all re-read, not carried)

| Anchor | Live bytes at `a01405d` | Post-landing target |
|---|---|---|
| `corpus/README.md:1`,`:3` | two identical `# kotodama-shokunin corpus index` H1s | Ca's leg; C does not own it |
| `corpus/README.md:11` | `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**` | repair to `25/26/25/29/24/94` (rev 2.4) |
| `corpus/README.md:234` | `## culture-material/ (25)` | `(26)` |
| `corpus/README.md:240` | `- \`calendar-festival-systems.md\` …` | new row goes **after** this line |
| `corpus/README.md:241` | `- \`costume-semiotics.md\` …` | new row goes **before** this line |
| `corpus/README.md:544` | `Total knowledge entries: 223.` | `224.` |
| `corpus/README.md:548` | `(total 223 files; directory totals 25/26/25/29/24/94).` | `224` / `25/26/26/29/24/94` |

Arithmetic recomputed, not asserted:

```
25+23+26+25+24+94 = 217   (rev-2.4 prose vector — wrong)
25+26+25+29+24+94 = 223   (correct rev-2.4)
25+26+26+29+24+94 = 224   (rev-2.5 target)
```

The rev-2.4 prose defect is real and is **in scope for the rev-2.5 edit** (`claims.json` C `after_required`: "the rev-2.4 prose-vector defect repaired in the same edit").

### 1.3 Sweep baseline (green, and its exact scope)

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", ..., "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
EXIT=0
```

The sweep's positive legs are: index rows vs files, missing/ghost, duplicate-row **reported**, row-topic byte equality (`reports/round-28/readme/sweep.py:60-61,74-83`), section-header drift, totals line, and the counts footer (`:119-213`). Its `ok` predicate is **only**:

```text
ok = (not (missing or ghosts or mismatches or drift or footer_findings)
      and totals_line == total_files)          # sweep.py:191-194
```

`duplicate_rows` is computed at `sweep.py:155` and never enters `ok`. There is no length leg and no order leg. §2 measures the consequences.

### 1.4 Gap still unowned, and the slug still free

```
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...': No such file or directory
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|graticule|theodolit|survey map)' corpus/knowledge/ | wc -l
0
$ for kw in cartograph mapmaking portolan cadastral graticule theodolite; do
    printf '%-12s files=%s lines=%s\n' "$kw" \
      "$(grep -rli -- "$kw" corpus/knowledge/ | wc -l)" \
      "$(grep -rni -- "$kw" corpus/knowledge/ | wc -l)"; done
cartograph   files=2 lines=2
mapmaking    files=0 lines=0
portolan     files=0 lines=0
cadastral    files=2 lines=2
graticule    files=0 lines=0
theodolite   files=0 lines=0
```

**Post-landing trap, measured.** After the entry lands, a naive `grep -rli cartograph` returns **3 files** (3 lines on the staged mock; more once the real entry's body uses the word), because the new entry counts itself. Re-running the gap probe without an exclusion would look like a collision. Every post-landing absence check must be:

```
grep -Rli --exclude=cartography-and-mapmaking.md -- cartograph corpus/knowledge | wc -l   # must stay 2
```

The same applies to `mapmaking` (0 → 1 naively) and any other term the entry uses.

### 1.5 Load-bearing neighbour lines re-read

| Citation | Live text (spot-checked) | Used for |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md:27` | "Cosmography = … how the world is drawn (maps), named …" | the competing sentence R03 B8 requires the entry to answer |
| `…/cosmology-cosmography.md:71` | "T-O diagrams are symbolic, not survey maps (§10)" | the partition's own disclaimer |
| `…/cosmology-cosmography.md:102` | "T-O diagrams are symbolic devices, not cartographic claims" | calibration row |
| `linguistics/naming-systems.md:70` | "…a map is an archive of coups." | R03 B3 — the quote is **verbatim present**; do not "correct" it |
| `culture-material/craft-artisan-lexicon.md:44` | `| Steel (Japan) | **tamahagane** …` | R03 B4 — this is **not** the workshop ladder |
| `…/craft-artisan-lexicon.md:54`,`:65` | ladder table header / design rule | the correct anchor |

---

## 2. Measured blind spots in `sweep.py` (each with a planted control)

I staged a 224-file knowledge tree and a 224-row README under `.scratch/v01-stage-*`, then ran the **filed instrument in-process** with `root_override` (`sweep.py:119`) — no edit to the instrument, no corpus write. Five controls:

| Control | Staged defect | Sweep verdict | Receipt verdict |
|---|---|---|---|
| A | 210-line entry, correct row/order/footer | `ok: true`, 224==224 | `ok: true` |
| B | same, entry **260 lines** | **`ok: true`** | `LENGTH 260 >250` |
| C | same, row inserted **after** `costume-semiotics.md` | **`ok: true`** | `ROW_ORDER` |
| D2 | two culture-material files with **identical `- topic:`** text and matching rows | **`ok: true`** | `SECOND_OWNER` |
| F | a duplicated `calendar-festival-systems.md` row | **`ok: true`** with `rows 225 files 224` | `DUPLICATE_ROW` + `ROW_COUNT` |

Exact control outputs:

```
B  rows 224 files 224  ok True   | receipt: fails ["LENGTH 260 >250 (r47 draft was 739)"]
C  rows 224 files 224  ok True   | receipt: fails ["ROW_ORDER culture-material rows are not in filename order"]
D2 rows 2   files 2    ok True   | receipt: fails ["SECOND_OWNER duplicate topic lines: {\"MOCK …\": [\"cartography-and-mapmaking.md\", \"zz-mock-copy.md\"]}"]
F  rows 225 files 224  ok True   | receipt: fails ["DUPLICATE_ROW [\"calendar-festival-systems.md\"]", "ROW_COUNT rows=225 files=224"]
```

Why this matters to the claim: B is exactly the r47 failure class (R03 measured **739 body lines / 17,601 words / 240 table rows / 15 H2 sections** against a 103–221 partition, `reports/round-47/review/R03-c-content.md:36-44`). 739 is 3.34× the live max and 2.96× the claim band. **A sweep-green landing is compatible with repeating that defect.** The receipt's length leg is the only thing in the round that can catch it.

---

## 3. The post-landing receipt — nine legs

The script is in §7 (extract and run; it is read-only). Each leg names what it proves and why it is not redundant with the sweep.

| # | Leg | Assertion | Why it is needed |
|---|---|---|---|
| 1 | `CENSUS` | `total_files == 224`; `culture-material == 26` | the claim's headline delta |
| 2 | `SWEEP` | `sweep.ok` true: rows/files, missing, ghosts, topic equality, header drift, footer, totals | index integrity |
| 3 | `LENGTH` | entry `<=250` lines; 222–250 emits a note | r47 over-build class; sweep has no length leg (control B) |
| 4 | `ROW_ORDER` | culture-material row names are sorted; the new basename is present | README row placement; sweep has no order leg (control C) |
| 5 | `DUPLICATE_ROW` / `ROW_COUNT` | unique row names; `total_rows == total_files` | sweep reports duplicates but does not fail on them (control F) |
| 6 | `SECOND_OWNER` | no two entries in any partition share a `- topic:` line | sweep compares row↔file only, never file↔file (control D2) |
| 7 | `ABSENCE` | excluding the new file: `cartograph 2/2`, `mapmaking 0/0`, `portolan 0/0`, `graticule 0/0`, `theodolite 0/0`, `cadastral 2/2` | the post-landing probe self-poisons without `--exclude` (§1.4) |
| 8 | `CONTRACT` | exactly one `- topic:`; exactly one H1; all eight header fields present | the entry contract; a missing `- recheck:` is the kind of silent omission a content review can miss |
| 9 | `README_H1` | reported always; enforced (`==1`) only when `--h1-expected 1` | separates C's landing from Ca's separate fix |

Leg 9 is deliberately opt-in. C's `after_required` does not include the duplicate-H1 removal; Ca's does. If both land in one integration, run with `--h1-expected 1`; if only C lands, leave it unset and the receipt reports `readme_h1: 2` without failing.

**Manual leg (not scripted, because it is prose):** the entry's `- gap filled:` line must contain absence counts that reproduce under the same `--exclude` command. R03 B2 was exactly an unreproducible count (`2 files / 3 lines` from a command that yields `2/2`). The post-landing reviewer should re-run each number stated in that line; the receipt cannot parse arbitrary prose without guessing.

### 3.1 Verified behaviour of the receipt

```
# live tree, pre-apply
$ python3 -B .scratch/v01-post-landing-verify.py
{"ok": false, "fails": ["MISSING_ENTRY culture-material/cartography-and-mapmaking.md"]}   EXIT=1

# staged 224 tree, 210-line entry
$ python3 -B .scratch/v01-post-landing-verify.py \
    --root .scratch/v01-stage-A-210/knowledge --readme .scratch/v01-stage-A-210/README.md
"ok": true
"census": {"total": 224, "parts": {"civilizations": 94, "culture-material": 26,
           "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}}
"entry": {"lines": 210, "band": "ok<=221", "sha256": "<mock>"}
"sweep": {"rows": 224, "files": 224, "footer": {"total": 224,
          "dir_totals": [25, 26, 26, 29, 24, 94]}, "totals_line": 224}
"absence_excluding_new": {"cartograph": [2,2], "mapmaking": [0,0], "portolan": [0,0],
                          "graticule": [0,0], "theodolite": [0,0], "cadastral": [2,2]}
"fails": []
"notes": ["naive cartograph file count post-landing=3 (self-poisoned; use --exclude)"]  EXIT=0

# staged 224 tree, 260-line entry
"fails": ["LENGTH 260 >250 (r47 draft was 739)"]                                          EXIT=1
```

A missing contract field (`- recheck:` deleted from the stage) yields `fails: ["CONTRACT missing - recheck:"]`.

---

## 4. Post-landing check on the r47 defect class (B1–B9)

R03's nine blocking defects are the reason r47's draft was correctly not landed. The receipt cannot judge prose, but each defect has a mechanical probe that will catch a recurrence in the **landed** bytes. These are `pending apply` and must be run by the post-landing reviewer against the real file, not the fragments.

| R03 ID | Defect | Probe on the landed entry |
|---|---|---|
| B1 | `0.2 mm × 1:50,000 = 10 m`; 200 m is **20×**, not "ten times" | recompute every scale/precision ratio; grep the sentence and divide |
| B2 | gap count `2 files / 3 lines` unreproducible | compare each count in `- gap filled:` to `grep --exclude` output (§3, manual leg) |
| B3 | false accusation that `naming-systems.md:70` lacks "archive of coups" | `grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md` must return `:70`; the entry must not call the quote invented |
| B4 | workshop ladder cited at `craft-artisan-lexicon.md:44` | `sed -n '44p'` is the Steel (Japan) row; the ladder is `:54-65` |
| B5 | typology cross-refs say `§1–3` / `§2` | the form typology is `§4.1` in the assembled entry |
| B6 | handoff says provenance is `§9` | provenance/charter must be `§8` |
| B7 | worked example states three incompatible update rules | one rule stated once; the example must not contain both "every breach" and "per levy year" as the same rule |
| B8 | "owns no made map" without answering `cosmology-cosmography.md:27` | the entry must dispose `:27` as well as `:71`/`:102` |
| B9 | "minimum build per form" covers 5 of 8 forms | either retitle to "five common forms" or list all eight |

The receipt's `SECOND_OWNER` leg covers the ownership half of B8 mechanically; the prose half is a reviewer call.

---

## 5. Apply-surface assertion

After the integrator applies C, the corpus delta must be exactly one new file plus the index:

```
$ git status --porcelain corpus/
 M corpus/README.md
?? corpus/knowledge/culture-material/cartography-and-mapmaking.md
```

Any other `M`/`D` under `corpus/` is a scope violation (frozen-bytes rule, `AGENTS.md`). `git diff --stat corpus/` should show README only. The entry must be an addition (`??`), never a modification of an existing path.

---

## 6. What this seat can and cannot certify

**Certified now (measured, with controls):**
- the pre-landing invariants in §1;
- the receipt's ability to fail on each of five planted defects and to pass a clean 224 stage;
- the four sweep blind spots (length, order, duplicate topic, duplicate row);
- the post-landing absence-probe self-poisoning and its `--exclude` fix.

**`could-not-evaluate` (blocked on the landing):**
- the landed entry's line count, topic byte-equality, and contract completeness;
- whether the B1–B9 class recurs;
- the post-apply sweep receipt and README sha;
- the claim's "audits clean" threshold. R03 already recorded that at r47 the audit chain was the blocker, not the content (`R03-c-content.md:242-250`). This seat certifies the **measurement**, not the audit verdicts; C03/C04/C05/C14 and R03 own those on the assembled bytes.

**Axis statement:** coverage is unchanged by this seat (+0 now; the +1 is contingent on a clean apply). Calibration is improved: four failure classes that the round's standard instrument cannot see are now measured, named, and gated.

---

## 7. The receipt script (durable copy)

`.scratch/` is disposable, so the durable copy is this fence. Extract and run from the lane root:

```bash
awk '/^```python$/{f=1;next}/^```$/{if(f){exit}}f' \
  reports/round-48/cov/V01-post-landing.md > .scratch/v01-post-landing-verify.py
```

```python
#!/usr/bin/env python3
"""V01 post-landing receipt for the r48 C claim. Read-only; exits 0 only on pass."""
import argparse, hashlib, importlib.util, json, os, re, subprocess, sys

LANE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NEW_REL = "culture-material/cartography-and-mapmaking.md"
FIELDS = ["topic", "gap filled", "sources", "source", "couples",
          "verified-at", "recheck", "scope"]
ABSENCE = {"cartograph": (2, 2), "mapmaking": (0, 0), "portolan": (0, 0),
           "graticule": (0, 0), "theodolite": (0, 0), "cadastral": (2, 2)}


def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(LANE, "corpus", "knowledge"))
    ap.add_argument("--readme", default=os.path.join(LANE, "corpus", "README.md"))
    ap.add_argument("--new", default=NEW_REL)
    ap.add_argument("--expect-total", type=int, default=224)
    ap.add_argument("--h1-expected", type=int, default=None)
    args = ap.parse_args()

    spec = importlib.util.spec_from_file_location(
        "sweep28", os.path.join(LANE, "reports", "round-28", "readme", "sweep.py"))
    sweep28 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sweep28)

    with open(args.readme, encoding="utf-8") as fh:
        text = fh.read()
    inv = sweep28.sweep(text, root_override=args.root)
    newpath = os.path.join(args.root, args.new)
    fails, notes = [], []

    if not os.path.isfile(newpath):
        print(json.dumps({"ok": False, "fails": ["MISSING_ENTRY " + args.new]}, indent=1))
        return 1

    n_lines = sum(1 for _ in open(newpath, encoding="utf-8"))
    entry = open(newpath, encoding="utf-8").read()
    sha = hashlib.sha256(open(newpath, "rb").read()).hexdigest()
    parts = {k: v["files"] for k, v in sorted(inv["parts"].items())}

    if inv["total_files"] != args.expect_total:
        fails.append(f"CENSUS total={inv['total_files']} expected={args.expect_total}")
    if parts.get("culture-material") != 26:
        fails.append(f"CENSUS culture-material={parts.get('culture-material')} expected=26")

    if not inv["ok"]:
        fails.append("SWEEP " + json.dumps({
            "missing": inv["missing_from_index"], "ghost": inv["orphan_rows"],
            "mismatch": [m["row"] for m in inv["topic_mismatch"]],
            "drift": inv["header_drift"], "footer": inv["footer_findings"],
            "totals": inv["totals_line"]}))

    band = "ok<=221" if n_lines <= 221 else "new-partition-max<=250" if n_lines <= 250 else "FAIL>250"
    if n_lines > 250:
        fails.append(f"LENGTH {n_lines} >250 (r47 draft was 739)")
    elif n_lines > 221:
        notes.append(f"LENGTH {n_lines} exceeds the prior partition max 221 but is inside the claim band")

    names = [f for f, _ in sweep28.parse_readme(text).get("culture-material", {"rows": []})["rows"]]
    if names != sorted(names):
        fails.append("ROW_ORDER culture-material rows are not in filename order")
    if NEW_REL.split("/")[1] not in names:
        fails.append("ROW_ABSENT " + NEW_REL)
    if len(names) != len(set(names)):
        fails.append("DUPLICATE_ROW " + json.dumps(
            sorted({f for f in names if names.count(f) > 1})))
    if inv["total_rows"] != inv["total_files"]:
        fails.append(f"ROW_COUNT rows={inv['total_rows']} files={inv['total_files']}")

    files = sorted(f for f in os.listdir(os.path.join(args.root, "culture-material"))
                   if f.endswith(".md"))
    topics = {}
    for f in files:
        t = sweep28.topic_of(os.path.join(args.root, "culture-material", f))
        if t is not None:
            topics.setdefault(t, []).append(f)
    dup = {t: v for t, v in topics.items() if len(v) > 1}
    if dup:
        fails.append("SECOND_OWNER duplicate topic lines: " + json.dumps(dup)[:400])

    absence = {}
    for kw, expect in ABSENCE.items():
        fc = int(sh(f"grep -Rli --exclude=cartography-and-mapmaking.md -- {kw} {args.root} | wc -l"))
        lc = int(sh(f"grep -Rni --exclude=cartography-and-mapmaking.md -- {kw} {args.root} | wc -l"))
        absence[kw] = [fc, lc]
        if (fc, lc) != expect:
            fails.append(f"ABSENCE {kw}={fc}/{lc} expected={expect[0]}/{expect[1]}")
    naive = int(sh(f"grep -Rli -- cartograph {args.root} | wc -l"))
    notes.append(f"naive cartograph file count post-landing={naive} (self-poisoned; use --exclude)")

    for fld in FIELDS:
        if not re.search(r"^- " + re.escape(fld) + r":", entry, re.M):
            fails.append("CONTRACT missing - " + fld + ":")
    if len(re.findall(r"^- topic:", entry, re.M)) != 1:
        fails.append("CONTRACT topic line is not exactly one")
    if len(re.findall(r"^# ", entry, re.M)) != 1:
        fails.append("CONTRACT entry H1 count != 1")

    h1 = len(re.findall(r"^# ", text, re.M))
    if args.h1_expected is not None and h1 != args.h1_expected:
        fails.append(f"README_H1 count={h1} expected={args.h1_expected}")

    print(json.dumps({
        "ok": not fails,
        "census": {"total": inv["total_files"], "parts": parts},
        "entry": {"path": args.new, "lines": n_lines, "band": band, "sha256": sha},
        "readme_sha256": inv["readme_sha256"], "readme_h1": h1,
        "sweep": {"rows": inv["total_rows"], "files": inv["total_files"],
                  "footer": inv["footer"], "totals_line": inv["totals_line"]},
        "absence_excluding_new": absence,
        "fails": fails, "notes": notes,
    }, indent=1))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
```

Run:

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/v01-post-landing-verify.py                       # C only
python3 -B .scratch/v01-post-landing-verify.py --h1-expected 1       # C + Ca in one apply
```

---

## 8. What I did not verify

- **The landed entry's bytes.** They do not exist at `a01405d`; every entry-dependent leg is `could-not-evaluate`, not pass.
- **The content, arithmetic and citations inside the draft.** C03/C04/C05/C14 and R03 own those. My §4 checklist is a probe list, not a verdict.
- **The README rev-2.5 edit as drafted by another seat.** I verified the live anchors and the arithmetic (§1.2) and measured that the edit shape makes the sweep green (stage A), but I did not review C10's or W01's diff.
- **Ca's duplicate-H1 fix.** Owned by Ca01/Ca03; my receipt only counts H1s and enforces a count when asked.
- **The r47 fragment files.** I used R03's measured summary (739 lines, B1–B9), not the fragments, which are filed bytes outside this round.

---

## 9. Command transcript (all run 2026-10-19, lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain --untracked-files=no        # empty: no tracked modifications
$ find corpus/knowledge -name '*.md' | wc -l
223
$ python3 -B reports/round-28/readme/sweep.py        # exit 0; rows 223 files 223; sha 7c788a1d…
$ python3 -B .scratch/v01-rehearse.py                # controls A/B/C green-blind; legs bite
$ python3 -B .scratch/v01-post-landing-verify.py     # exit 1: MISSING_ENTRY (pre-apply)
$ python3 -B .scratch/v01-post-landing-verify.py --root .scratch/v01-stage-A-210/knowledge \
    --readme .scratch/v01-stage-A-210/README.md      # exit 0
$ python3 -B .scratch/v01-post-landing-verify.py --root .scratch/v01-stage-B-260/knowledge \
    --readme .scratch/v01-stage-B-260/README.md      # exit 1: LENGTH 260 >250
$ python3 -c "print(sum([25,23,26,25,24,94]), sum([25,26,25,29,24,94]), sum([25,26,26,29,24,94]))"
217 223 224
```

No `reports/round-*/run-validation.py` was executed. No corpus, tools, README, LOG, frozen-gate, or fleet byte was written or staged. No git commit/push, no install, no network. Scratch stages are symlink farms under `.scratch/v01-stage-*` plus mock entries labelled `MOCK`; they are not landing candidates and must not be copied into `corpus/`.

**Owed.** The post-apply run of §7 against the real bytes, by the integrating parent, with `--h1-expected` set according to whether Ca lands in the same apply. Until that run exists, the round has a **provisional** C verdict, not a delivery certificate.
