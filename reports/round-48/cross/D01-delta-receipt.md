# D01 — delta receipt: the predicted post-landing README + sweep, and the only delivery certificate

- Seat: `D01` | role: executor (cross) | claim: **cross** (serves C's README rev 2.5 and Ca's duplicate-H1 removal) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`)
- Out path: `reports/round-48/cross/D01-delta-receipt.md` (this file)
- Mission (`reports/round-48/targets.json`, seat D01): "Delta receipt: predict the post-landing README sha + sweep output by staged tree; cite the post-apply sweep as the only delivery certificate (the readme-prediction-vs-delivery practice)."
- Statement: this seat wrote no corpus, tool or README byte. The staged tree lives only under `.scratch/d01/`, which is disposable. Every number below is measured; the one predicted byte value is labelled as a prediction and is decomposed so a delivery mismatch is diagnosable rather than mysterious.

**One-line judgment.** A 224-entry staging tree carrying C02's filed `- topic:` line and the seven README edits (E1–E7) is **sweep-green at `rows 224 files 224`, exit 0**, and predicts `corpus/README.md` sha256 `4db8ecafe134fccd8ee2b10d73b5ccc18bcc26177c4db9f21e7826cc056c9e68` (582 lines, 145,261 bytes, H1 count 1). That sha is **keyed to one topic line and one rev-2.5 wording**; the *structural* reading it produces has a stable digest (`0dd02023…`) that any prose change cannot move and a topic mismatch cannot fake. The post-apply sweep's own `readme_sha256` line is the delivery certificate — not this prediction. Three flags are recorded in §10, one of which (an arithmetic slip in the C10/claims wording) would land a 223-summing vector if copied literally.

---

## 1. The rule this receipt is written to, and why the prediction is not the certificate

The queue carries the defect from r36: a staged README digest differed from the delivered digest while the sweep was green, and the staged value was treated as the certificate (`reports/round-37/op/defect-queue.json:242-251`, id `readme-prediction-vs-delivery`, class `carried-with-owner`, owner `integrator`, next_touch "predict by staged-tree sha, cite post-apply sweep"). The sweep reading that certifies a landing is "**measured at close, never predicted**" (`reports/round-39/cov/C06-delta-receipt.md:17-18`).

This receipt therefore has two layers, and they are not interchangeable:

| Layer | What it is | Authoritative? |
|---|---|---|
| **Prediction** (§5–§6) | sha256 and sweep reading of a staged tree built from the filed topic line + a drafted rev-2.5 block | No. A forecast for the integrator's diff review. |
| **Certificate** (§8) | the post-apply `sweep.py` run against the landed tree: its `readme_sha256`, its structural reading, its exit code | **Yes — the only one.** |

The r36 failure mode is avoided structurally, not by promise: the prediction is decomposed into (a) bytes that the sweep constrains and (b) free prose, and the certifying check (§8) tests (a) with a digest that is invariant to (b). A prose difference is then a recorded note, not a false red; a structural difference is a hard fail.

---

## 2. Before state — measured, not carried

All commands from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ wc -l -c corpus/README.md
575  143866
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
```

The sweep at the baseline is green **with both claimed README defects live** — which is the point of Ca:

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
exit=0
```

`sweep.py --selftest` → `selftest: 12/12 checks passed`, exit 0. The instrument has no heading leg: its regexes are sections/rows/topics/totals/footer only (`reports/round-28/readme/sweep.py:59-66`; `sweep()` at `:119`; totals at `:160`). Confirmed independently by Ca03 (`reports/round-48/calib/Ca03-readme-verify.md:8`) and N01 (`reports/round-48/cross/N01-numbers.md` §4.5).

---

## 3. The edit set the prediction stages (E1–E7)

Anchors are the **live** line numbers at `a01405d`; the row text is C02's filed topic value (`reports/round-48/cov/C02-header.md:114`), which the README row must copy byte-for-byte or the sweep emits a `REWRITE` (`sweep.py:60-61,74-84`).

| # | Target | Before (live) | After | Note |
|---|---|---|---|---|
| E1 | `corpus/README.md:2-3` | blank + second H1 | *(both deleted)* | Ca03's recommended form (`reports/round-48/calib/Ca03-readme-verify.md:92`). Deleting `:2-3` and deleting `:3-4` are **byte-identical** because both blanks are empty; the surviving file is H1, blank, rev 2.4. |
| E2 | before `:5` | `revision: 2.4 …` starts | 8-line `revision: 2.5 …` block + blank | Content below; only this block is free prose. |
| E3 | `:11` | `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**` | `… → **25/26/25/29/24/94**` | Repairs the live rev-2.4 defect. |
| E4 | `:234` | `## culture-material/ (25)` | `## culture-material/ (26)` | Must equal the live file count or `header_drift` fires. |
| E5 | after `:240` (`calendar-festival-systems.md`), before `:241` (`costume-semiotics.md`) | — | one row: `` - `cartography-and-mapmaking.md` — <C02 topic> `` | `cal` < `car` < `cos`; verified sort position (C02 §1.4, N01 §3.3). |
| E6 | `:544` | `Total knowledge entries: 223.` | `Total knowledge entries: 224.` | `totals_ok` must stay true. |
| E7 | `:548` | `(total 223 files; directory totals 25/26/25/29/24/94).` | `(total 224 files; directory totals 25/26/26/29/24/94).` | Footer order is the README section order, **not** the claims.json listing order (`sweep.py:50-57`). |

### 3.1 Arithmetic, recomputed

```
25/23/25/29/24/94 = 220   (rev-2.3's after-vector, consistent)
25/23/26/25/24/94 = 217   (what rev 2.4 wrote — wrong by -6)
25/26/25/29/24/94 = 223   (correct rev-2.4 after-vector = live footer)
25/26/26/29/24/94 = 224   (rev-2.5 target)
```

Per-slot error in the live rev-2.4 line, stated-after vs true-after: myth-symbol `23` vs `26` (**−3**), culture-material `26` vs `25` (**+1**), synthesis `25` vs `29` (**−4**) — net **−6**, exactly the gap between 217 and 223. N01 §3.2 reaches the same per-slot figures independently.

### 3.2 The rev-2.5 block as staged (free prose — see §6)

```
revision: 2.5 — Round-48 culture-material cartography expansion (2026-10-19): one
culture-material entry landed (`cartography-and-mapmaking.md`); `## culture-material/`
moved 25 → **26**; the totals line and the counts footer moved 223 → **224** and the
footer vector 25/26/25/29/24/94 → **25/26/26/29/24/94**. This revision also repairs the
rev-2.4 prose vector (it read `25/23/26/25/24/94`, which sums 217, not the 223 it names).
Re-measured with `python3 -B reports/round-28/readme/sweep.py`: 224 rows vs 224 files,
exit 0. Non-canon examples and passing structural gates do not certify historical truth.
```

The last sentence is the house's standing caveat; it is carried in rev 2.1–2.3 (`corpus/README.md:21-22`, `:29-30`, `:40`) and rev 2.4 is the one recent block that omits it — rev 2.5 restores it. The rev-2.4 repair sentence is the one Ca/rev-2.5 asks for ("the rev-2.4 prose-vector defect repaired in the same edit", `reports/round-48/claims.json:29`).

---

## 4. What was staged (and what was deliberately not)

- `.scratch/d01/tree-c02/knowledge/` — a byte copy of `corpus/knowledge` plus one **staging fixture** at `culture-material/cartography-and-mapmaking.md` whose only load-bearing line is `- topic: <C02 topic>`. The sweep reads entry content only through `topic_of` (`sweep.py:74-84`), so a fixture is sufficient for the README/sweep arithmetic and no claim is made about the entry's body, length or quality.
- `.scratch/d01/tree-c02/README.md` — `corpus/README.md` with E1–E7 applied by script, not by hand.
- **Not staged:** the entry body (C01/C03 seats), the over-build disposition (Ca02), the heading-count control (Ca05), the rev-2.0 duplicate at `:42` (§10 F-D01-2).

Topic pinning: the topic line C02 filed is 766 characters; `sha256("- topic: " + value + "\n")` = `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a`, which reproduces C02's own pinned seed digest (`reports/round-48/cov/C02-header.md:114` header claim; the digest is the line **with** its LF, not the value alone — value-only is `bc7274f4…`). The README row line is 801 characters / 811 UTF-8 bytes, `sha256(row + "\n")` = `41dcc4f82e0dc068b5313ef277da7a0458627862c995616b00052b3735935673`.

---

## 5. The predicted reading (staged tree, verbatim sweep output)

```
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_live {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 4db8ecafe134fccd8ee2b10d73b5ccc18bcc26177c4db9f21e7826cc056c9e68
exit=0
```

Staged README: **582 lines** (live 575, net **+7** = −2 E1, +8 E2, +1 E5), **145,261 bytes** (delta **+1,395**), **H1 count 1**. Every sweep leg green; no other corpus file touched.

---

## 6. The sha is a prediction; here is exactly what moves it

Two classes of bytes exist in the post-landing README:

**Constrained (the sweep measures them).** The six section headers and their declared counts, the 224 row filenames and row texts, the totals line, the footer date/command/total/vector. Any change here is a defect the sweep or the certificate catches.

**Free (the sweep never reads them).** The rev-2.5 block, and any other revision prose. A wording change moves the byte sha while leaving the structural reading identical.

Measured sensitivity, all on the C02 topic and the staged tree:

| Variant | README sha256 | Sweep | Structural digest |
|---|---|---|---|
| **Primary** — E1 deletes `:2-3`, rev-2.5 as above | `4db8ecaf…c9e68` | green, 224/224 | `0dd02023…b97221b` |
| E1 deletes only the H1 line (double blank kept) | `088c5f64…e2492` | green, 224/224 | `0dd02023…b97221b` |
| One rev-2.5 word changed (`expansion`→`landing`) | `b9eef2b6…ecbf21` | green, 224/224 | `0dd02023…b97221b` |
| Staging topic instead of C02's topic | `702c5a27…145438` | green, 224/224 | `0dd02023…b97221b` |
| README row altered by one character vs the entry | `d2a4e15a…` | **RED** — 1 `REWRITE` | `8c4f1bdf…` |

The structural digest is the delivery invariant: it is identical for every legal prose variant and different the moment a row stops matching its entry's `- topic:` (the instrument's topic-equality leg, `sweep.py:74-84`, emitting class `REWRITE`). The full-byte sha is informational and will differ if the integrator rewords the rev-2.5 block; that is **not** a failure, and it must not be "fixed" by editing the prediction or the history.

---

## 7. Expected intermediate states — the landing is atomic

Both halves of the delta must land in one motion. Measured:

```
# entries landed, README not yet:
ok=False  missing=['culture-material/cartography-and-mapmaking.md']  rows=223 files=224
# README landed, entry not yet:
ok=False  missing=[]  ghosts=['culture-material/cartography-and-mapmaking.md']  rows=224 files=223
# both landed:
ok=True   rows=224 files=224
```

A red sweep at either intermediate point is **expected**, not evidence of a bad edit. The integrator should not roll back on it; it certifies only after both halves are on disk.

---

## 8. The certificate — integrator's acceptance sequence

1. Re-check the live tree at apply time: `find corpus/knowledge -name '*.md' | wc -l` → `223`; `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → *No such file*. If the slug exists, stop — collision, do not overwrite.
2. Apply the entry (C02 head + body seats' sections) and E1–E7 in one motion.
3. Run the certificate from the lane root:

```python
#!/usr/bin/env python3
"""D01 delivery certificate for the r48 C+Ca landing. Read-only."""
import hashlib, importlib.util, json, sys
PREDICTED_STRUCT = "0dd02023434636b9fa933f36ebcb6d5bf27a78a6595fc7a94ca2fab09b97221b"
PREDICTED_SHA    = "4db8ecafe134fccd8ee2b10d73b5ccc18bcc26177c4db9f21e7826cc056c9e68"
KEYS = ("parts","total_rows","total_files","missing_from_index","orphan_rows",
        "topic_mismatch","header_drift","totals_line","footer")
def die(m): print("FAIL " + m); sys.exit(1)
readme = open("corpus/README.md", encoding="utf-8").read()
h1 = sum(1 for l in readme.split("\n") if l == "# kotodama-shokunin corpus index")
if h1 != 1: die(f"heading count {h1} != 1")
spec = importlib.util.spec_from_file_location("sweep", "reports/round-28/readme/sweep.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
inv = mod.sweep(readme)
if not inv["ok"]:
    die("sweep not ok: " + json.dumps({k: inv[k] for k in
        ("missing_from_index","orphan_rows","topic_mismatch","header_drift","footer_findings")}))
got = hashlib.sha256(json.dumps({k: inv[k] for k in KEYS}, sort_keys=True,
                                 separators=(",", ":")).encode()).hexdigest()
print("readme_sha256 " + inv["readme_sha256"])
print("struct_sha256 " + got)
if got != PREDICTED_STRUCT: die("structural reading != D01 prediction")
if (inv["total_rows"], inv["total_files"]) != (224, 224): die("not 224/224")
if inv["footer"]["dir_totals"] != [25, 26, 26, 29, 24, 94]: die("footer vector wrong")
print("PASS structure matches the D01 prediction; 224/224; H1 count 1")
if inv["readme_sha256"] != PREDICTED_SHA:
    print("NOTE readme_sha256 differs from the D01 byte prediction — record the cause; do not edit history")
```

4. Expected outputs, all measured on the staged tree:

```
readme_sha256 4db8ecafe134fccd8ee2b10d73b5ccc18bcc26177c4db9f21e7826cc056c9e68
struct_sha256 0dd02023434636b9fa933f36ebcb6d5bf27a78a6595fc7a94ca2fab09b97221b
PASS structure matches the D01 prediction; 224/224; H1 count 1
exit 0
```

5. Record the landed `readme_sha256` in the round's close artifacts. If it equals `4db8ecaf…`, the byte prediction held; if not, write one sentence naming which free-prose bytes differ. **Never** retro-edit this receipt to match delivery.
6. Independent cross-checks the certificate does not replace: `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 224`; `python3 -B reports/round-28/readme/sweep.py --selftest` → 12/12.

The certificate was tested in three states before being written here: live tree → `FAIL heading count 2 != 1` (correct, defect live); simulated post-apply tree → `PASS … 224/224; H1 count 1`, exit 0; simulated tree with the footer vector typo `25/26/25/29/24/94` → `FAIL sweep not ok … FOOTER_DIR_TOTALS`, exit 1.

---

## 9. What this receipt cannot certify

- **The entry's length, quality or method.** The staging fixture is not a draft; C05/C12/C17/R03 own those. `<= ~250` is a C-claim threshold (`reports/round-48/claims.json:31`), not a delta-receipt measurement.
- **Any value if the topic line changes after this read.** The prediction is pinned to the 766-character line at `reports/round-48/cov/C02-header.md:114`; a single character moves both the row and the sha. Re-run the generator with the delivered topic.
- **Ca's second half.** The over-build queue-successor (Ca02) is outside the README delta.
- **Any external source.** No network at seat time; nothing external is asserted here.
- **The r47 content defects.** B1–B9 (`reports/round-47/review/R03-c-content.md` §5) are addressed by the entry seats; this receipt cannot see the body.
- **Immutability of the prediction's inputs.** C02/C10 may be amended after this read; the pins (topic digest `9424fb81…`, fragment at `:114`) let a later reader detect that.

---

## 10. Flags for the integrator

**F-D01-1 — an arithmetic slip in the C10/claims wording that would land a 223-summing vector.**
`reports/round-48/targets.json` (seat C10) reads: "repair the rev-2.4 prose-vector (synthesis 25->29, myth-symbol 23->26, culture-material 26->25 = 224)". The three per-slot corrections are right; the "= 224" is wrong. They yield `25/26/25/29/24/94 = **223**` — the rev-2.4 total. The 224 belongs to rev 2.5, whose vector is `25/26/26/29/24/94` (culture-material also +1). Applying C10's sentence literally, with 224 as the target, risks writing a vector that sums 223 while the file count is 224 — the exact r28-analogue footer defect. The staged E3/E7 pair above is the verified form.

**F-D01-2 — a second live duplicate in the same README, outside Ca's stated scope.**
`corpus/README.md:42` is a dangling duplicate of the `revision: 2.0` first line (byte-identical to `:44`; `:42` has no body). N01 §4.1 (`reports/round-48/cross/N01-numbers.md:99`) and K02's result line and §5 (`reports/round-48/scout/K02-readme-defect.md:9,381`) report it independently. Ca's `before` field names only the duplicate H1 (`reports/round-48/claims.json:44`), and K02 says the Ca edit must **not** absorb the rev-2.0 duplicate. It is therefore correct for E1 to leave it. But it is the same defect class as the H1 and it remains live and sweep-blind after this round — it should be filed as its own queue row or folded into a Ca successor, not silently repaired inside this delta.

**F-D01-3 — the heading count is not a sweep leg.**
The certificate above checks H1 count itself because `sweep.py` never reads headings (`:59-66`). If Ca05's control does not land, the heading assertion lives only in this ad-hoc check and in the post-apply command record; that is weaker than a durable gate. Ca05's `reports/round-48/calib/Ca05-heading-control.md` is the intended home.

---

## 11. Commands and write-surface statement

All commands run from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l ; ls corpus/knowledge/culture-material/*.md | wc -l
223 ; 25
$ sha256sum corpus/README.md ; wc -l -c corpus/README.md
7c788a1d…f31cdcd ; 575 143866
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ python3 -B reports/round-28/readme/sweep.py            # exit 0, 223==223, both defects live
$ python3 -B reports/round-28/readme/sweep.py --selftest # 12/12, exit 0
$ python3 -B .scratch/d01/predict-c02.py                 # staged tree: 224==224, exit 0
$ python3 -B .scratch/d01/certify.py                     # live: FAIL heading count 2 != 1
$ (cd .scratch/d01/sim && python3 -B certify.py)         # staged: PASS, exit 0
$ python3 -c "print([sum(map(int,v.split('/'))) for v in ['25/23/26/25/24/94','25/26/25/29/24/94','25/26/26/29/24/94']])"
[217, 223, 224]
$ diff -u corpus/README.md .scratch/d01/tree-c02/README.md | grep -c '^@@'
4                         # four hunks: head, rev-2.4 vector, culture-material, footer
$ diff -u corpus/README.md .scratch/d01/tree-c02/README.md | grep -c '^[+-]'
19                        # includes the ---/+++ file header; 17 changed lines
$ git status --porcelain corpus/ tools/ README.md
(empty)
```

**Write surface:** this file only — `reports/round-48/cross/D01-delta-receipt.md`. Scratch artifacts (`predict.py`, `predict-c02.py`, `certify.py`, `topic-c02.txt`, `tree/`, `tree-c02/`, `sim/`, `readme.diff`) live only under `.scratch/d01/` and are disposable; the durable values are reproduced in §3–§8. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.
