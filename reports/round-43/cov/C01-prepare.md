# C01 — confirm-and-prepare the r42 lithic spare (claim C)

- Seat: C01 | executor (claim C) | round 43 | date 2026-10-19 | baseline `7ceff59`
- Mission (verbatim, `reports/round-43/targets.json` → `seats[id=C01].mission`): *"Confirm-and-prepare the C01 lithic spare for landing: re-read reports/round-42/cov/C01-mineral-spare.md fenced bytes; confirm the entry contract (header fields, - couples:, - sources:, calibration, recheck, scope) is complete; state the exact target path under myth-symbol/ and confirm it is free. Report the byte range to apply."*
- Writes: this file only. No corpus byte, no tools byte, no filed round-1..42 byte. No `run-validation.py` executed. No commit, push, install, or network.

## Verdict

**BLOCKED — the spare's topic is already owned on disk.** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` is present at HEAD, tracked, clean, and **byte-identical to r42 C04's fenced entry** (61,884 bytes, sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`). The r43 claim-C "before" state says "lithic slot named but unbuilt since r42's C01/C04 collision routed this draft to spare" (`reports/round-43/claims.json:39`) — **the slot is built; what was routed was a second draft of the same topic.** The spare's own filed header says so: "C01 and C04 authored the same lithic topic mid-wave … C04 lands … THIS draft is routed as the named spare for a future re-scoped claim" (`reports/round-42/cov/C01-mineral-spare.md:1`).

Landing the spare as myth-symbol entry 27 would create two entries owning one register topic, and its fenced head block contains measured claims that are now false. It cannot land unmodified, and re-authoring is not a path/front-matter adjustment. **Recommendation: do not apply; route to the integrator for a re-scope or a retirement record.**

## 1. Live partition state (measured at HEAD `7ceff59`)

```
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do printf '%s ' "$p"; ls corpus/knowledge/$p/*.md | wc -l; done
linguistics 25
myth-symbol 26
culture-material 25
synthesis 29
verification 24
civilizations 94
```

`python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_ok True`, `footer_ok True`, exit 0; README sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`. The current index is **rev 2.4**, explicitly recording the three r42 landings and the spare routing (`corpus/README.md:3-12`). The lithic row is live at `corpus/README.md:219`.

The consumed slot:

```
$ ls corpus/knowledge/myth-symbol/ | grep -iE 'mineral|stone|gem|lapid|lithic'
mineral-stone-symbolism.md
$ git log --oneline -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore
$ git status --porcelain corpus/knowledge/myth-symbol/ | wc -l
0
```

## 2. Identity of the two drafts

r42 had **two seats target the same filename**: `reports/round-42/cov/C01-entry-1.md:1` ("entry 1 of 4 … `mineral-stone-symbolism.md`") and `reports/round-42/cov/C04-entry-4.md:5` ("Proposed landing path … `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`"). C04's fence content is byte-identical to the live file:

```
disk   61884 bytes sha256 c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f
C04    61884 bytes sha256 c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  equal=True
spare  55101 bytes sha256 6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89  equal=False
```

The spare is a **different draft of the same register** (its title: "material properties as symbol, the scarcity ladder, and the lapidary as an institution"; the landed entry: "the lapidary code, material prestige, and the quarry-to-regalia chain"). Its `- gap filled:` line claims "the lithic slot is named but never built" and "no entry owns stone" — both false at HEAD because `mineral-stone-symbolism.md` is the entry that owns stone and its `- topic:` line opens "the lithic register of a fictional culture's symbolic grammar — the mineral slot the register family lacks".

## 3. Why claim C cannot be satisfied as declared

Claim C requires "myth-symbol 26 -> 27, total 223 -> 224" and calls the spare "the partition's stone/gem/metal register entry, completing myth-symbol's named lapidary slot" (`reports/round-43/claims.json:39`). Three independent blockers:

1. **Duplicate ownership.** The lapidary slot is completed by `mineral-stone-symbolism.md`. Two lithic-register entries would restate one topic — the exact condition r42's integrator ruling resolved by routing this draft to spare.
2. **False bytes in the spare's head block.** Applied unmodified, the entry would assert at `reports/round-42/cov/C01-mineral-spare.md:7` that the slot is "never built", that "no entry owns stone", that the corpus has 220 files, and that a filename sweep returns "0 hits"; at `:24` it asserts myth-symbol 23 / total 220. At HEAD the sweep returns 1 hit (`mineral-stone-symbolism.md`) and the counts are 26/223. Those are provenance claims, not cosmetics — `corpus/QUALITY.md:5-8` bars unverified claims laundered into assertion.
3. **No lawful path to 224.** Overwriting `mineral-stone-symbolism.md` is barred by the shared rules and would keep the count at 26, not raise it to 27. A second filename keeps the count at 27 but duplicates the topic and still imports the false head block.

The spare's `- couples:` line also never names `mineral-stone-symbolism.md`, so even a mechanically adjusted landing would leave the duplicate uncoupled — a coupling defect under `corpus/QUALITY.md:13-15`.

## 4. Entry-contract audit (holds — the draft itself is contract-complete)

Fragment physical line numbers; fence opens at line 3 and closes at line 219.

| contract leg | location | status |
|---|---|---|
| `# Title` | `:4` | present |
| `- gap filled:` | `:7` | present (4,572-byte line; measured claims now stale — §3) |
| `- topic:` | `:6` | present (1,354 bytes) |
| `- sources:` (block) | `:8` | present |
| `- calibration:` | `:21` | present (1,921 bytes) |
| `- couples:` | `:22` | present, **single physical line** (3,851 bytes) — no wrapped field, r42 plan H1 satisfied; group-aligned by partition (`myth-symbol —`, `linguistics —`, `culture-material —`, `synthesis —`, `verification —`, `handoff target:`) |
| `- source:` | `:23` | present |
| `- verified-at:` (ISO date) | `:24` | present (`2026-10-19`); counts stale (§3) |
| `- recheck:` | `:25` | present |
| `- scope:` | `:26` | present |
| decision record | `## 10. Decision record` | present, 16 unique `DR-MS-*` ids |
| calibration of contested/discredited readings | `## 11. Calibration bank` | present, 5 inline `(to-verify)` markers |
| usability surface | `## 2`–`## 9`, `## 12` | present: 69 table rows, build order, NON-CANON worked example |
| canon hygiene | `## 13. Handoff` | present; ends at lore-shokunin, decides no canon |

Citation resolution over the fenced bytes: **120 backticked tokens**, of which 86 are path-shaped — 52 full/partition-relative paths resolve on disk (52/52) and 34 bare basenames resolve uniquely under `corpus/knowledge/**` (34/34 unique, 0 ambiguous, 0 missing); every cited line number is within the target file (0 out-of-range). So the draft is internally contract-complete; the defect is topical, not structural.

## 5. Target path, collision status, and byte range (conditional preparation)

- **No landing path is stated anywhere in the spare's fenced bytes.** The only path-bearing prose is the unfenced integrator ruling at `:1`. Any path is therefore the integrator's choice, not the author's.
- **Taken and not overwritable:** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`.
- **A free filename exists but is not recommended:** `corpus/knowledge/myth-symbol/lithic-register-symbolism.md` is absent from the partition (`test -e` → absent by `ls`); `sort -c` over the 26 live names plus this slug exits 0 and places it between `hero-journey-variants.md` and `mineral-stone-symbolism.md` — i.e. immediately adjacent to the duplicate. Filename freedom does not cure the topic collision.
- **Byte range to apply** (if a future re-scope ever sanctions these exact bytes): fragment lines **4–218** (215 content lines), bytes **[328, 55429)** of `reports/round-42/cov/C01-mineral-spare.md`, length **55,101** bytes, sha256 **`6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89`**. Fence integrity: open fence line 3 at byte offset 316, close fence line 219 at byte offset 55,429; file length 55,433 bytes; content ends with one LF.

## 6. Disposition options for the integrator (this seat decides none)

- **A. Retire the spare as superseded (recommended).** File a successor note that `mineral-stone-symbolism.md` owns the topic; no corpus delta. Claim C then cannot reach 224 as declared and must be reported failed/re-scoped — the honest outcome, matching r42's own ruling.
- **B. Re-scope coverage to a genuinely unbuilt gap.** The only K02 gap with no entry is R2 dream/vision/trance (`reports/round-42/scout/K02-myth-gaps.md:216-259`, proposed `dream-vision-trance.md`); measured `ls corpus/knowledge/*/ | grep -iE 'dream|trance|vision'` → no filename. K02 records R2's provenance debt explicitly (`:453-459`: Vitebsky/Bourguignon/Winkelman etc. are 0 files, no network), so a landing would carry a declared `(to-verify)` shelf. **This needs a fresh draft; the lithic spare is not it.**
- **C. Land the spare anyway.** Rejected on evidence: duplicate ownership plus false head-block claims. If the integrator nonetheless wants it, the minimum lawful form is a full head-block re-author (gap, verified-at, couples-to-the-landed-entry) plus a stated second-entry justification — beyond this seat's authority and beyond "path/front-matter adjustments".
- **D. Replace C04's entry with the spare.** This is an overwrite of filed corpus bytes and is barred by the shared rules; it would also leave the count at 26.

## 7. Commands run (all from lane root, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`)

```
git rev-parse --short HEAD                                   -> 7ceff59
git status --porcelain                                      -> only ?? reports/round-43/
ls corpus/knowledge/myth-symbol/*.md | wc -l                -> 26
find corpus/knowledge -name '*.md' | wc -l                  -> 223
python3 -B reports/round-28/readme/sweep.py                 -> rows 223 files 223; exit 0
ls corpus/knowledge/myth-symbol/ | grep -iE 'mineral|stone|gem|lapid|lithic'
                                                            -> mineral-stone-symbolism.md
sha256sum-style fence comparison (Python)                   -> disk == C04 fence; spare != disk
python3 fence-byte extractor                                -> [328,55429), 55101 bytes, sha 6999a912…
citation resolver (86 path-shaped tokens)                   -> 52/52 full paths, 34/34 unique basenames, 0 line OOR
```

## 8. Scope statement

Only `reports/round-43/cov/C01-prepare.md` was written. No corpus byte was staged or edited; `mineral-stone-symbolism.md` was read, never touched. No `reports/round-*/run-validation.py` was executed. No network, install, commit, or push. The collision is reported, not routed around.
