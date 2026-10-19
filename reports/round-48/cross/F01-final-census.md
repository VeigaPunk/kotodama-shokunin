# F01 — final census: the five numbers the round must prove

- **Seat:** F01, verifier, claim `cross`, loop-2 position 2.
- **Out path:** `reports/round-48/cross/F01-final-census.md`.
- **Baseline commit:** `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19) = `reports/round-48/claims.json` `baseline_commit`.
- **Writes:** this file only; fixtures under `.scratch/f01/`. No corpus write, no filed-byte edit, no git mutation, no in-tree `run-validation.py`.
- **Verdict.** In-tree at `a01405d` the five numbers are **not present** (223 / 25 / rev 2.4 / H1 2 / green at 223==223): nothing is applied. On the **filed draft bytes** staged in `.scratch/f01/`, with W01's slice rule and both Ca hunks, the same five read **224 / 26 / rev 2.5 / H1 1 / green at 224==224** and the 17-check census passes. One content decision remains open (the duplicated caveat line C10 adds, F2); the W01 pin drift observed mid-seat was corrected in W01's current revision (F1). The staged result is a prediction; the delivery certificate is the post-apply run of §8.

## 1. The five numbers, measured

| # | Number | Live at `a01405d` | Required | Real staged drafts | Proof |
|---|---|---|---|---|---|
| 1 | Total entries | **223** | **224** | **224** | `find corpus/knowledge -name '*.md' \| wc -l` |
| 2 | culture-material | **25** | **26** | **26** | `ls corpus/knowledge/culture-material/*.md \| wc -l` |
| 3 | README revision | **2.4** (2.5 count 0) | **2.5** | **2.5**, once | `grep -c '^revision: 2\.5\b' corpus/README.md` |
| 4 | README level-1 headings | **2** | **1** | **1** | `grep -c '^# ' corpus/README.md` |
| 5 | Sweep | **223 rows == 223 files**, `ok True`, exit 0 | **224 == 224**, footer 224 | **224 == 224**, footer `25/26/26/29/24/94`, exit 0 | `python3 -B reports/round-28/readme/sweep.py --json` |

Live outputs:

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ grep -c '^# ' corpus/README.md
2
$ grep -c '^revision: 2\.5' corpus/README.md
0
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

Sweep instrument: `reports/round-28/readme/sweep.py`, sha256
`9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`.

Arithmetic re-computed: 223 + 1 = 224; 25 + 1 = 26; footer 25/26/25/29/24/94 →
25/26/26/29/24/94 (25+26+26+29+24+94 = **224**); `Total knowledge entries: 223.`
(`corpus/README.md:544`) → 224; footer `(total 223 files; …)` (`:548`) → 224;
section header `## culture-material/ (25)` (`:234`) → 26.

## 2. Preconditions re-verified

- **Cartography is unowned.** `find corpus/knowledge -iname '*cartograph*'` → no output.
  `grep -rn 'cartograph' corpus/knowledge/` → **2 lines in 2 files**, both by-product uses:
  `myth-symbol/cosmology-cosmography.md:102` (calibration) and
  `civilizations/mesoamerica-primary-sources.md:58` (lienzos). `mapmaking|map-making` → 0.
  The only `*map*` slug is `synthesis/dialect-faction-map-workflow.md` (a linguistics
  workflow). `grep -in 'cartograph\|survey map\|mapmaking' corpus/README.md` → no match.
- **Slug free:** `corpus/knowledge/culture-material/cartography-and-mapmaking.md` absent.
- **Partition band (measured on the 25 files):** min 103, median 149, max **221**
  (`funerary-material-culture.md`). `<=~250` is 29 lines of headroom over the live max, not
  a fabricated cap. r47's assembled draft was **790 = 51 head + 739 body**
  (`reports/round-47/review/R01-review.md:90`; `reports/round-47/review/R03-c-content.md:96`),
  3.6× the max and 5.3× the median. The r48 landable draft is **240 lines** by W01's assembler
  (§3.2): inside discipline.

## 3. Census of the filed drafts (staged, not applied)

### 3.1 What the fragments actually are

| Fragment | Fence | Lines | Shape as filed |
|---|---|---|---|
| `reports/round-48/cov/C02-header.md` | `:111-135` (` ````markdown `) | **23** | 1 H1 + the eight head fields (`topic`, `gap filled`, `sources`, `couples`, `source`, `verified-at`, `recheck`, `scope`); block sha `708dec15…`, file sha `2ff5b15d…` |
| `reports/round-48/cov/C01-entry.md` | `:69-298` (` ````markdown `) | **228** | **1 H1 + a complete second head block** (fence lines 1-12), then `## 1.` at fence line 13; block sha `e5255657…`, file sha **`4c2815a7…`** (W01's current pin, `:81`/`:125`) |
| `reports/round-48/cov/C10-readme.md` patch A | `:83-150` | 3 hunks, +24/−4 | against live (pre-Ca); post 595 lines, sha `5767d3c4…` |
| `reports/round-48/cov/C10-readme.md` patch B | `:162-228` | 3 hunks | against post-Ca; post 593 lines, sha `3960c5e2…` |
| `reports/round-48/calib/Ca01-readme-fix.md` hunk 1 | `:50-59` | −2 lines | removes the duplicate H1 at `:3` and its blank |
| `reports/round-48/calib/Ca01-readme-fix.md` hunk 2 | `:307-…` | −2 lines | removes the orphan `revision: 2.0` stub at `:42-43` |

**Pins at census time** (2026-10-19, after the seats' final revisions): C01 file
`4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d`; C02 file
`2ff5b15da54eba4ff2f99be0eac2ba6e584b3edf782ac546b6241b067bd96653`; C10
`049f17cbfe2d98a7f3b4808af0e4ab180e975157a0a3246b58ab2f47bc7ec68c`; Ca01
`2696ab94add387653d2f7f71057e34388957a22d343b2862f69b00783d41691a`; Ca02
`2feb3a45c0e67555d97a9412650834b300b07db7b20126b95ea42f7999c07cbd`; W01
`684c525423a03848110e05e4d396da8fa14b9fa703aef284c8b5afd3d9c758ce`. W01's prose was
revised twice during this seat; its **landing bytes stayed stable** at 239/`d1de5db5…`
as-filed and 240/`d4cb0ee1…` landable throughout. A fragment whose **block** changes after
this census invalidates its staged numbers and must be re-pinned (W01's rule).

**Topic coupling is byte-exact.** C02's `- topic:` is **766 chars**, sha256
`bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495`. C10's row
(`:132` in patch A, `:210` in patch B) is the same 766 bytes — `EQUAL: True`, and the sweep
reports `topic_mismatch 0` on every staged variant. C01's own `- topic:` is a **different**
text (**1045 chars**, sha `23d94f41…`), so C02 is the authoritative head; using C01's head
would break the row.

### 3.2 Assembly: W01's revised rule matches the bytes

W01 was revised while this seat ran. The current `reports/round-48/cov/W01-landing-spec.md`
(census-time sha `684c5254…`) §3.2 prescribes exactly the required slice —
`entry = C02_block + "\n\n" + C01_block[first "## 1.":]` — and ships a tested, fail-closed
assembler (§3.4). I ran that assembler on the current fragments and reproduced its stated
digests exactly:

| Assembly | Lines | H1s | `- topic:` | sha256 | Census |
|---|---:|---:|---:|---|---|
| **W01 as-filed** (no correction) | **239** | 1 | 1 | `d1de5db512de1ab2fb526012ac83ec67e7f3105e7aaf934302e16f2f2522a3d1` (37,592 bytes) | 17/17 on the staged README |
| **W01 landable** (L1 boundary row) | **240** | 1 | 1 | `d4cb0ee17f0662a6c15cacfbd9e5c633fc0452570d94d7c322cef5c859caf508` (37,836 bytes) | **17/17 PASS** |
| Naive whole-block concatenation | 252 | **2** | **2** (conflicting) | `f4f1aa0c6f53c17a304210dd05814d12480098947bd71519d43845ff792095d1` | **14/17 FAIL** |

The naive assembly is the hazard the assembler prevents: it passes the sweep (`rows 224
files 224`, `topic_mismatch 0`, exit 0) because `topic_of()` (`sweep.py:74-82`) reads the
*first* `- topic:` and C02's is first. Only the census's entry-structure legs (H1 count, topic
count) and the 252 > 250 length leg catch it. A hand assembly that skips W01's slice would
land a two-H1, two-head-block entry on a green sweep.

My earlier manual slice (240 lines, sha `6fa8e3aa…`) differed from W01's output only by one
trailing blank line; **the assembler output is authoritative**, and all staged results below
use it. The L1 correction adds one boundary row and its cited anchors resolve
(`corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:42` = PARCEL,
`:45` = CLAIM).

### 3.3 README variants staged on the real entry

| Applied to a staged 224 tree | README lines | README sha256 | Census |
|---|---:|---|---|
| Patch A only (C, pre-Ca) | 595 | `5767d3c43d286e0863c44c55cfd1ebe8d13e7d8cd5a19c5d2c3424bc0e25648f` — **matches C10 `:79`** | 15/17 (two H1 legs fail, correctly) |
| Ca hunk 1 + Patch B | 593 | `3960c5e2753a1cb2f8a7345b9f7210ad35405da9fe1189f0fb590772a22cebc7` — **matches C10 `:157`** | **17/17 PASS** |
| Ca hunks 1+2 + Patch B | 591 | `66f194bbba47f89a8f4c7b454772c2ca1a01a33b4b714a4f669bff8169893075` | **17/17 PASS**; `revision: 2.0` dup count 1 |

`git apply --check` on patch A, Ca hunk 1 and Ca hunk 2 against live → **exit 0** each
(GNU `patch` reports "fuzz 1" on Ca hunk 1 but produces the exact −2-line result; `git apply`
does not, so the diff is clean). C10's two post-state shas were reproduced independently, byte
for byte, which is the strongest cross-check in this census.

### 3.4 A duplicated caveat introduced by patch A/B

Patch A and B insert `Non-canon examples and passing structural gates do not certify
historical truth.` as the last line of the rev-2.5 block. That sentence already exists at
`corpus/README.md:40` and, wrapped, at `:88`. After staging it appears **three** times:
staged `:20` (inside rev 2.5), `:57` (exact), `:103` (wrapped). No instrument reads it; no
leg fails. It reads as an accidental duplication, not a deliberate restatement — see F2.

## 4. Findings

**F1 (resolved during the seat) — W01's shape rule and pins now match the bytes.**
W01's first revision required C01 to be body-only while C01's fence is a whole entry. Its
current revision (`reports/round-48/cov/W01-landing-spec.md:91` §3.2) fixes that with the
slice rule, and its assembler (`:137` §3.4, fail-closed on both file and block digests)
reproduces **239 / 37,592 / `d1de5db5…`** as-filed and **240 / 37,836 / `d4cb0ee1…`**
landable — I ran it on the current fragments and got both digests exactly. The transient
issue I observed mid-seat (W01 pinned C01's whole-file sha `a075a9da…` after C01 revised its
prose to `4c2815a7…`) is fixed in the current W01, which re-pins `4c2815a7…` at `:81`/`:125`
and now checks the **block** sha as well. Lesson for the round: pin the block digest as the
landing identity, because seat-side prose is not landing bytes. Note also that C02 must remain
the authoritative head: C01's own `- topic:` is 1045 chars (`23d94f41…`) and does not match
C10's row, while C02's is the 766-char row text.

**F2 (content duplication) — patch A/B adds a third copy of an existing caveat.**
Measured above (§3.4). The rev-2.5 block's closing line duplicates `corpus/README.md:40` and
the wrapped occurrence at `:88`. Recommendation: drop the `+Non-canon examples…` line from
both patch variants (a one-line deletion in each); if the intent was to restate the caveat,
it needs a reason, not a silent third copy. Owner: C10.

**F3 (calibration: correct the line-shift accounting) — the Ca edit is two hunks, not one.**
Ca01's `:50-59` removes the duplicate H1 (−2 lines); its `:307-…` hunk removes the orphan
`revision: 2.0` stub at `:42-43` (−2 more). If the integrator applies both, every README
citation below `:44` shifts by **−4**, not −2. My first pass assumed −2 and was wrong; the
measured end states are 593 lines (hunk 1 only) and 591 lines (both). The Ca claim's
`after_required` names only the H1; Ca03/R04 should state whether hunk 2 is in scope, because
applying it changes the Ca before/after statement and the line-shift table.

**F4 (calibration, instrument gap) — two green-sweep false negatives, measured.**
1. A duplicated index row leaves the sweep at **exit 0 / `ok True` while printing
   `rows 225 files 224`**: `duplicate_rows` is computed at `sweep.py:131` and stored at
   `:155` but never read by the pass predicate at `:191-193`, and `total_rows` is not compared
   with `total_files`. Control N6 below.
2. A two-H1, 252-line entry also leaves the sweep green (§3.2) because entry structure is
   outside every sweep leg.
   Consequence: the delivery certificate must assert `rows == files == 224` **and** the entry
   structure, as the census does. Recommendation to Ca05: the proposed
   `tools/check-readme-structure.py` should add `rows == files` (or the sweep's duplicate leg
   should gate); this finding is independent of the heading control.

**F5 (arithmetic, live defect) — the rev-2.4 prose vector at `corpus/README.md:11` sums 217.**
`25/23/25/29/24/94 → **25/23/26/25/24/94**`: the pre-vector is 220 (correct), the written
post-vector is **217** against a stated 223. Correct post-vector in the sweep's order
(`sweep.py:50-57`) is **25/26/25/29/24/94 = 223**. Rev 2.5 must state
**25/26/26/29/24/94 = 224**; patch A/B does, and the census verifies it by parsing the whole
rev-2.5 block (a single-line parse would miss it — C10 writes a multi-line block).

**F6 (instrument gap) — "rev 2.5" is not machine-checked.** `grep -n 'revision'
reports/round-28/readme/sweep.py` → no match; the sweep parses section headers, rows, the
totals line and the `Counts checked` footer only (`sweep.py:59-66`). A green sweep without a
rev-2.5 block passes. Provenance for number 3 is therefore a grep plus the F5 arithmetic,
both in the census.

**F7 (grounding, not a defect) — the length budget has a measured basis.** culture-material
min/median/max = 103/149/221; 240 lines is 1.09× the current max and inside `<=250`; r47's
790 was 3.6×/5.3×. The r47 class was not "long" but "out-of-band plus unmeasured defect
surface", which is the distinction Ca02's row records.

## 5. Ca's non-numeric leg (r47 over-build disposition)

`reports/round-48/calib/Ca02-overbuild.md` is filed and **structurally verified** by this seat:

- the fenced JSON parses; `schema kotodama-defect-queue-successor-v1`, `round 48`,
  `baseline_commit a01405d`;
- one row, id `r47-entry-overbuild-defect-class`, class `routed-with-owner`, owner and
  `next_touch` named, nine instance findings B1–B9 present;
- parent `reports/round-40/op/defect-queue-v2.json` pinned at
  `dfc9265d…` — live `sha256sum` equals the pin;
- predecessor `reports/round-47/calib/queue-successor-r47.json` pinned at `9508b6aa…` — live
  `sha256sum` equals the pin; the r47 successor carries 3 rows and none is an over-build row,
  so this is a new row, not a duplicate.

It is **drafted, not applied**: `reports/round-48/calib/queue-successor-r48.json` does not
exist. Status: **drafted-verified, pending apply** (integrator). This leg is not one of the
five numbers and does not block them, but the manner of its application is in scope for the
round's Ca claim.

## 6. Controls (the instruments are not rubber-stamping)

All controls were run on byte-identical copies of the sweep (sha `9b2ccac0…`) and its real
exit codes captured with `--json`.

| Control | Mutation | Measured |
|---|---|---|
| N1 | staged entry removed, row kept | exit **1**; `rows 224 files 223`; orphan 1; `header_drift {'culture-material': {declared 26, files 25}}`; `FOOTER_TOTAL` + `FOOTER_DIR_TOTALS` |
| N2 | entry kept, row deleted | exit **1**; `rows 223 files 224`; `missing_from_index 1` |
| N3 | footer left at 223 | exit **1**; `FOOTER_TOTAL` + `FOOTER_DIR_TOTALS` |
| N4 | section header left at 25 | exit **1**; `header_drift {'culture-material': {declared 25, files 26}}` |
| N5 | row topic `the`→`a` | exit **1**; `topic_mismatch 1`, class `REWRITE`, `row_chars 386` vs `topic_chars 388` |
| N6 | new row duplicated in place | exit **0**, `ok True`, **`rows 225 files 224`**, `duplicate_rows ['cartography-and-mapmaking.md']` (F4.1) |
| N7 | census mutant: duplicate H1 + the 217 vector | census **13/17** — exactly the H1 (2 legs) and vector (2 legs) checks fail |
| N8 | naive entry assembly | census **14/17** — length (252), H1 count 2, topic count 2 fail; sweep still green (F4.2) |

## 7. State at close

```
live in-tree, a01405d       staged, filed drafts (W01 landable assembly)
1 total 224        223      224
2 culture-material  25       26
3 README rev 2.5   2.4        2.5 (once)
4 H1 count           2        1
5 sweep           223==223   224==224, footer 224
census verdict    4/19       17/17 PASS
```

Two of the four passing in-tree checks are `sweep exit 0` and `sweep ok` at the *wrong*
total; they are consistency, not progress. Nothing under `corpus/` has changed
(`git status --porcelain -- corpus/` → empty).

## 8. Reopen protocol (tested; run after the integrator applies C + Ca)

Copy the block to `.scratch/f01/census.py` and run from the repo root. Read-only; exits 0
only when every check passes. Expected counts: **19/19 in-tree** (17 base + 2 git legs) and
**17/17 on a non-git staging root**. Test results at this seat: live **4/19**; W01 landable
entry + Ca hunk 1 + Patch B **17/17**; + both Ca hunks **17/17**; naive assembly
**14/17**; duplicate-H1/217-vector mutant **13/17**.

```python
#!/usr/bin/env python3
"""F01 five-number census. Read-only. Usage: python3 census.py [ROOT]"""
import glob, json, os, re, subprocess, sys
root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
R = lambda p: os.path.join(root, p)
rows = []

def rec(name, ok, got, want):
    rows.append((name, bool(ok), got, want));

# 1-2 counts
files = glob.glob(R("corpus/knowledge/*/*.md"))
cm = glob.glob(R("corpus/knowledge/culture-material/*.md"))
rec("total 224", len(files) == 224, len(files), 224)
rec("culture-material 26", len(cm) == 26, len(cm), 26)

# 3 revision 2.5
txt = open(R("corpus/README.md"), encoding="utf-8").read()
rev_all = re.findall(r"^revision: 2\.5\b.*$", txt, re.M)
rec("rev 2.5 present once", len(rev_all) == 1, len(rev_all), 1)
mblk = re.search(r"^revision: 2\.5\b.*?(?=^revision: )", txt, re.M | re.S)
rev_block = mblk.group(0) if mblk else ""

# 4 heading count (level-1)
h1 = re.findall(r"^# .*$", txt, re.M)
rec("H1 count 1", len(h1) == 1, len(h1), 1)
rec("H1 is the index title", h1 == ["# kotodama-shokunin corpus index"], h1[:1], "index title")

# 5 sweep
out = subprocess.run([sys.executable, "-B", R("reports/round-28/readme/sweep.py"), "--json"],
                     capture_output=True, text=True)
try:
    inv = json.loads(out.stdout)
except Exception:
    inv = {}
rec("sweep exit 0", out.returncode == 0, out.returncode, 0)
rec("sweep ok", inv.get("ok") is True, inv.get("ok"), True)
rec("sweep rows==files==224", inv.get("total_rows") == inv.get("total_files") == 224,
    [inv.get("total_rows"), inv.get("total_files")], [224, 224])
rec("sweep totals line 224", inv.get("totals_line") == 224, inv.get("totals_line"), 224)
rec("footer total 224", (inv.get("footer") or {}).get("total") == 224,
    (inv.get("footer") or {}).get("total"), 224)
rec("footer dirs 25/26/26/29/24/94", (inv.get("footer") or {}).get("dir_totals") == [25, 26, 26, 29, 24, 94],
    (inv.get("footer") or {}).get("dir_totals"), [25, 26, 26, 29, 24, 94])
rec("no missing/ghosts/mismatch/drift",
    not inv.get("missing_from_index") and not inv.get("orphan_rows")
    and not inv.get("topic_mismatch") and not inv.get("header_drift"),
    [len(inv.get("missing_from_index") or []), len(inv.get("orphan_rows") or []),
     len(inv.get("topic_mismatch") or []), inv.get("header_drift")], "all empty")

# 6 rev-2.5 prose vector sums 224 and matches footer dirs
vec = None
if rev_block:
    # the bolded post-landing vector, not the plain pre-landing one
    ms = re.findall(r"\*\*(\d+(?:/\d+){5})\*\*", rev_block)
    if ms: vec = [int(x) for x in ms[-1].split("/")]
rec("rev2.5 vector sums 224", vec is not None and sum(vec) == 224, vec, "sum 224")
rec("rev2.5 vector == footer order", vec == [25, 26, 26, 29, 24, 94], vec, [25, 26, 26, 29, 24, 94])

# 7 entry length and structure discipline
entry = R("corpus/knowledge/culture-material/cartography-and-mapmaking.md")
n = len(open(entry, encoding="utf-8").read().splitlines()) if os.path.exists(entry) else None
rec("entry <=250 lines", n is not None and n <= 250, n, "<=250")
elines = open(entry, encoding="utf-8").read().splitlines() if n is not None else []
rec("entry has exactly one H1", sum(1 for x in elines if x.startswith("# ")) == 1,
    sum(1 for x in elines if x.startswith("# ")), 1)
rec("entry has exactly one - topic:", sum(1 for x in elines if x.startswith("- topic:")) == 1,
    sum(1 for x in elines if x.startswith("- topic:")), 1)

# 8 landing safety (in-tree only)
if os.path.isdir(R(".git")):
    st = subprocess.run(["git", "-C", root, "status", "--porcelain", "--", "corpus/knowledge"],
                        capture_output=True, text=True).stdout
    lines = [l for l in st.splitlines() if l.strip()]
    want = ["?? corpus/knowledge/culture-material/cartography-and-mapmaking.md"]
    rec("corpus/knowledge delta is exactly one new file", lines == want, lines, want)
    diff = subprocess.run(["git", "-C", root, "diff", "--name-only", "--", "corpus/knowledge"],
                          capture_output=True, text=True).stdout.strip()
    rec("no modified/deleted existing entry", diff == "", diff, "empty")

print(f"root: {root}")
for name, ok, got, want in rows:
    print(("PASS " if ok else "FAIL ") + name + f" | got={got} want={want}")
print("VERDICT:", "PASS" if all(r[1] for r in rows) else "FAIL", f"({sum(r[1] for r in rows)}/{len(rows)})")
sys.exit(0 if all(r[1] for r in rows) else 1)
```

## 9. Limits of this seat

- The staged column is a **prediction on draft bytes**, not a landed state. The delivery
  certificate is the post-apply run of §8 against the in-tree root; no other run can close
  numbers 1–5.
- The landable assembly is W01's §3.2 rule (`reports/round-48/cov/W01-landing-spec.md:91`),
  reproduced by its assembler at 240 lines / sha `d4cb0ee1…`. W01's current revision pins the
  C01 file at `4c2815a7…` and checks the block sha `e5255657…`; the landing identity is the
  block, and it is stable.
- Not evaluated here: content quality, citation anchors, boundary rulings, worked-example
  consistency, shelf honesty. Those are C03–C18/R03/X03 legs; the five numbers are necessary,
  not sufficient.
- Not run: `reports/round-*/run-validation.py` (forbidden in-tree), any corpus write, any
  packet-surface change, any re-freeze. No filed byte was edited.
