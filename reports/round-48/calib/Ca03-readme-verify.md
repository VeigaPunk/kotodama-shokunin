# Ca03 — README duplicate-H1 fix: independent verification

- Seat: `Ca03` | role: verifier | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19; `git status --porcelain` shows no modified tracked file), equal to `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`).
- Out path: `reports/round-48/calib/Ca03-readme-verify.md` (this file).
- Non-author statement: I drafted neither `Ca01-readme-fix.md` nor `Ca02-overbuild.md`, and I edited no corpus byte. Every finding below is measured on the live bytes at the baseline or on a scratch copy under `.scratch/round-48-ca03/`. The fix is verified **as staged bytes**, not as landed bytes.

**One-line judgment.** The duplicate-H1 defect is real and live (`grep -c` = 2 at lines 1 and 3), the surgical edit (delete the blank line and the second H1) yields count 1 with the unmodified r28 sweep still green at 223==223 and every other heading byte-identical. The **README half of Ca PASSES** the claim's thresholds, with two conditions: apply by content anchor (not line number), and treat the staged green as a prediction whose delivery certificate is the post-apply sweep.

---

## 1. Before-state at the baseline (measured)

| Measurement | Command | Result |
|---|---|---|
| README digest | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| size | `wc -l` / byte count | 575 lines / 143,866 bytes |
| duplicated H1 | `grep -n '^# kotodama-shokunin corpus index' corpus/README.md` | `1:…` and `3:…` (count **2**) |
| all H1 lines | `grep -c '^# ' corpus/README.md` | **2** |
| H2 lines | `grep -n '^## ' corpus/README.md` | 7: `177:## linguistics/ (25)`, `205:## myth-symbol/ (26)`, `234:## culture-material/ (25)`, `261:## synthesis/ (29)`, `293:## verification/ (24)`, `320:## civilizations/ (94)`, `417:## Known gaps (frontier)` |
| duplicate heading at any level | `grep -n '^#\{1,6\} ' corpus/README.md \| sed 's/^[0-9]*://' \| sort \| uniq -d` | exactly one line, `# kotodama-shokunin corpus index` — no duplicated H2 |
| fenced / indented `#` lines | `grep -n '^```'`, `grep -n '^[[:space:]]\+#'` | none, so a naive `^# ` count is safe on this file today |
| line endings | `grep -c $'\r' corpus/README.md` | 0 (LF-only) |

First four lines, `cat -A` (the `$` is end-of-line; no trailing-space or CR artefact):

```
# kotodama-shokunin corpus index$
$
# kotodama-shokunin corpus index$
$
```

The head block is two identical top-level headings separated by one blank line. This is the filed defect, re-confirmed independently at this round's baseline.

### 1.1 Baseline sweep and its selftest

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
EXIT=0

$ python3 -B reports/round-28/readme/sweep.py --selftest
… selftest: 12/12 checks passed        (exit 0)
```

The sweep is green **with the defect present**. That is the point: the green is not evidence the head is clean.

---

## 2. Why the sweep cannot see this defect

The instrument's legs are section headers, rows, topics, totals and footer (`reports/round-28/readme/sweep.py:59-68`):

- `SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$", re.M)` — `sweep.py:59`
- `TOTALS_RE = re.compile(r"^Total knowledge entries: (\d+)\.\s*$", re.M)` — `sweep.py:62`
- `FOOTER_RE = …` — `sweep.py:66`

There is no H1 or heading-count leg anywhere in the module (the only `^#` in its regexes is the `##` section matcher). This matches the filed finding: `reports/round-39/cross/X00-connector.md:252-256` ("pre-existing and sweep-blind … a separate recorded act") and the queue's own reason at `reports/round-40/calib/Ca01-queue-v2.md:179`. A heading-count control is therefore required in addition to the sweep; the claim asks for exactly that (`reports/round-48/claims.json:45,51`).

---

## 3. Defect provenance and the "separate recorded act" condition

| Record | Line | What it says |
|---|---|---|
| r37 defect queue | `reports/round-37/op/defect-queue.json:103-111` | `R36-README-DUPLICATE-HEADING`, class `carried-with-owner`, owner `r38+ defect-queue completion`, `verification: null` |
| r40 queue v2 | `reports/round-40/calib/Ca01-queue-v2.md:175-182` | class `carried-with-owner`; owner "integrator to assign a corpus-index editor (a round owning corpus-surface repair)"; reason: live re-verified grep count 2, sweep-blind, "repair must be a separate recorded correction"; `next_touch`: "r42 or r44 (corpus-owning build round): remove the redundant title as a separate recorded act, then re-run the sweep plus a heading-count control the sweep lacks" |
| r39 door | `reports/round-39/cross/X00-connector.md:252-256` | must not be silently fixed inside a revision delta; if repaired, "it is a separate recorded act" |
| r38 scope | `reports/round-38/adj/A01-scope.md:176-187` | F-A02-2: live defect, routed; "Owner: integrator (a one-line heading removal, or a recorded no-fix with reason)" |
| r48 declaration | `reports/round-48/claims.json:41-51` | Ca is its own claim with `before` (`:44`), `after_required` (`:45`), counting commands (`:46-50`), thresholds (`:51`) |
| r48 non-goal | `reports/round-48/claims.json:58` | "the README duplicate-heading removal is a live defect fix on the index, not a rewrite of a closed round's filed bytes" |

**Reading.** The defect is overdue per its own `next_touch` ("r42 or r44 … corpus-owning build round"); r48 is a corpus-owning build round (claim C lands one entry). The "separate recorded act" condition is satisfied at declaration: the fix is claim **Ca**, separate from the C landing, with its own counting command and threshold — it is not folded silently into C's rev-2.5 delta. The durable record of the act is the integrator's `LOG.md` entry, which I did not verify (`to-verify`; it does not exist yet at seat time).

---

## 4. The edit, exact bytes, and the two variants I tested

Both variants were generated from the live bytes and written under `.scratch/round-48-ca03/`; nothing under `corpus/` was modified.

### 4.1 Recommended — delete the blank line and the second H1 (lines 2–3)

`diff -u corpus/README.md .scratch/round-48-ca03/README.B-drop-lines2-3.md`:

```diff
@@ -1,7 +1,5 @@
 # kotodama-shokunin corpus index
 
-# kotodama-shokunin corpus index
-
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
 myth-symbol entries landed (`mineral-stone-symbolism.md`,
 `purity-pollution-boundary-systems.md`, `sacred-topography-pilgrimage.md`),
```

After-bytes:

| Property | Before | After (B) |
|---|---|---|
| lines | 575 | **573** |
| bytes | 143,866 | **143,832** (−34 = 33-byte H1 line + 1-byte blank line) |
| sha256 | `7c788a1d…cdcd` | **`d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079`** |
| H1 count | 2 | **1** |
| head shape | H1, blank, H1, blank | H1, blank, revision text |

This matches the house shape of an entry head (`corpus/knowledge/culture-material/timekeeping-instruments.md:1-3`: title, blank, `- topic:`). No other byte differs: the unified diff has one hunk and removes exactly two lines.

### 4.2 Alternative — delete line 3 only

`README.A-drop-line3.md`: 574 lines, 143,833 bytes, sha256 `84e16f566e170ac4be9d7f01d90ca1743640d36c899d9c81808c5dc8c0065633`, H1 count 1, sweep green. It leaves **two** consecutive blank lines between the H1 and the revision text. It satisfies the claim but is cosmetically worse; I recommend 4.1. The choice is the integrator's, and both were measured.

---

## 5. Independent verification matrix

All post-edit measurements use the **unmodified filed sweep** imported as a module and called with the staged README text and the live knowledge root (method used by prior rounds; the module takes `readme_text` as its first argument, `sweep.py:119`). No instrument was edited.

| # | Check | Command / method | Result |
|---|---|---|---|
| V1 | count 2 → 1 | `grep -c '^# kotodama-shokunin corpus index' .scratch/…/README.B-…md` | **1** (PASS) |
| V1b | same for variant A | same on `README.A-…md` | **1** (PASS) |
| V2 | sweep still green after the edit | `importlib` import of `reports/round-28/readme/sweep.py`; `sw.sweep(staged_text)` | `ok true`, rows **223** files **223**, missing `[]`, ghosts `[]`, topic_mismatch `[]`, header_drift `{}`, totals_line 223, totals_ok true, footer_findings `[]`, footer_ok true, `readme_sha256 d407260d…0079` (PASS) |
| V3 | no other heading touched | heading-set diff (`grep -n '^#\{1,6\} '` on both, line-number prefix stripped) | one deleted line only — the duplicate H1. All 7 H2 strings byte-identical; their line numbers shift by 2 (`177→175`, `205→203`, `234→232`, `261→259`, `293→291`, `320→318`, `417→415`) because the deleted lines sit above them. (PASS) |
| V4 | rows / topics / totals / footer untouched | same sweep legs as V2; full diff has one hunk at the head | 223 rows, 223 files, 0 mismatch, totals 223, footer `[25, 26, 25, 29, 24, 94]` (PASS) |
| V5 | no encoding/EOF change | `grep -c $'\r'`; `tail -c 1 \| xxd` | 0 CR bytes; final byte `0a` both before and after (PASS) |
| V6 | heading-count control | `test "$(grep -c '^# ' corpus/README.md)" -eq 1` | **FAIL at HEAD** (count 2), **PASS** on both staged variants (count 1). This is a stopgap control, not the durable one — see §7. |
| V7 | orthogonality with C's rev-2.5 head insertion | staged B + a synthetic rev-2.5 paragraph inserted before the rev-2.4 block → `README.COMBINED-rev25-sim.md`; sweep called on it | H1 count **1**, `ok true`, 223==223 (the sim adds no entry, so 223 is expected), footer_ok true. The head fix and a rev-2.5 insertion do not disturb each other. (PASS; prediction only) |
| V8 | no second duplicate at any level | `uniq -d` over all heading lines before and after | after: none; only the one H1 remains (PASS) |
| V9 | instrument intact | `python3 -B reports/round-28/readme/sweep.py --selftest` | 12/12 PASS, exit 0 (run at baseline; instrument unmodified) |

Staged artefacts (scratch; hashes pin the bytes I measured):

```
d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079  README.B-drop-lines2-3.md      (recommended, 573 lines)
84e16f566e170ac4be9d7f01d90ca1743640d36c899d9c81808c5dc8c0065633  README.A-drop-line3.md         (alternative, 574 lines)
a2c5b17fe287e0fd7e6624578bad61179b136104ddcac90db92ebc75fec3e5fc  README.COMBINED-rev25-sim.md  (orthogonality sim, 577 lines)
```

---

## 6. Verdict on the README half of Ca

**PASS**, against the claim's own thresholds (`reports/round-48/claims.json:51`):

- heading count **2 → 1** — measured on staged bytes (V1);
- sweep **green after** — measured with the unmodified instrument (V2), 223==223 with only Ca applied;
- no other heading touched — measured (V3);
- the fix is a **separate recorded act** at declaration (claim Ca vs claim C, §3). The durable LOG entry remains the integrator's obligation.

**Conditions on the integrator's apply (not optional):**

1. **Apply by content, not line number.** Remove the second occurrence of the exact line `# kotodama-shokunin corpus index` together with the blank line that precedes it (variant B). If C's rev-2.5 header is applied first, every line number below the head shifts; a line-numbered patch will mis-apply.
2. **Re-run the sweep on the landed bytes.** The staged green is a prediction. The delivery certificate is `python3 -B reports/round-28/readme/sweep.py` after both C and Ca are applied — expected 224==224 with the footer vector and totals line at 224 (C's leg, not mine to certify).
3. If both edits are applied in one pass, the expected landed sequence is: rev-2.5 header inserted above rev-2.4, duplicate H1 removed, README length = 575 − 2 (removal) + the rev-2.5 paragraph length. The sha in this report (`d407260d…`) is **not** the post-landing sha; it is the Ca-only staged sha.

---

## 7. Could-not-evaluate / to-verify

- **Ca02's over-build queue-successor row was not present at my write.** `reports/round-48/` held only `claims.json`, `targets.json` and `telemetry/dispatch-declared.json` (16:37), so the second half of Ca — dispositioning the r47 over-build class — is **`could-not-evaluate`** from this seat. I did not infer it from the target list. `to-verify`.
- **Ca05's durable heading-count control is not filed.** The sweep has no heading leg (§2) and my `grep -c` control (V6) is a stopgap, not a gate. The claim permits "added to the sweep or a durable note filed" (`claims.json:45`); whether Ca05's artefact satisfies that is `to-verify` from here.
- **Ca01's fragment** was likewise absent; I derived the edit from the live bytes rather than reviewing Ca01's diff, so the recommendation in §4 is mine and independently measured. If Ca01 proposes a different variant, the matrix in §5 still applies to whichever bytes are staged.
- **Post-landing state** (224==224, README rev 2.5, LOG entry) is outside this seat; the final census/validation seats own it.
- **Not run:** any `reports/round-*/run-validation.py` (forbidden in-tree; `reports/round-48/run-validation.py` does not exist at my write), any git mutation, any network call.

---

## 8. Reproducing this report

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sha256sum corpus/README.md                     # 7c788a1d…
grep -n '^# kotodama-shokunin corpus index' corpus/README.md   # 1, 3
python3 -B reports/round-28/readme/sweep.py    # green at 223
python3 -B reports/round-28/readme/sweep.py --selftest          # 12/12

# stage the recommended edit (deletes lines 2–3)
mkdir -p .scratch/round-48-ca03
python3 - <<'PY'
lines = open("corpus/README.md", encoding="utf-8").read().splitlines(keepends=True)
open(".scratch/round-48-ca03/README.B-drop-lines2-3.md", "w", encoding="utf-8", newline="").write("".join(lines[:1] + lines[3:]))
PY
sha256sum .scratch/round-48-ca03/README.B-drop-lines2-3.md      # d407260d…
grep -c '^# ' .scratch/round-48-ca03/README.B-drop-lines2-3.md # 1

# sweep the staged text with the unmodified filed instrument
python3 - <<'PY'
import importlib.util
spec = importlib.util.spec_from_file_location("sweep28", "reports/round-28/readme/sweep.py")
sw = importlib.util.module_from_spec(spec); spec.loader.exec_module(sw)
txt = open(".scratch/round-48-ca03/README.B-drop-lines2-3.md", encoding="utf-8").read()
inv = sw.sweep(txt)   # live corpus/knowledge root; only the README text varies
print(inv["ok"], inv["total_rows"], inv["total_files"], inv["footer_findings"], inv["readme_sha256"])
# True 223 223 [] d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079
PY
```

Write surface: this file only under `reports/round-48/`; three scratch copies under `.scratch/round-48-ca03/`. No corpus byte, no filed round, no tool, no gate was modified.
