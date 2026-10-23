# ScribeReadmeFrontier — round-64 wave-1 README / frontier item

Seat: `ScribeReadmeFrontier` (scribe). Scope: run `.ufo/waves/round-64/integrate-w2.py` in a **copy** of the lane tree, diff the resulting `corpus/README.md` against the real one, report the exact byte-level delta; read the README's frontier / known-gaps surface and propose a minimal honest update naming the new entry and its partition as a patch fragment (real README **not** edited); check the index row's topic string against the entry's `- topic:` line.

Lane bounds honored: no subagent dispatch; no write to the real lane tree except this report file; no commit, no jj operation; no product code, counter, or judge edited.

Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReadmeFrontier/` (`lane/` first copy, `lane2/` clean copy used for the final patched README, `lane3/` clean copy used for the real-S723 re-run).

---

## 1. What I ran (commands and outcomes)

### 1.1 Scratch copies

```
mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReadmeFrontier
cp -a /home/vgpnk/Projects/shokunin/kotodama-shokunin .../lane    # 596M
cp -a /home/vgpnk/Projects/shokunin/kotodama-shokunin .../lane2   # clean re-copy
cp -a /home/vgpnk/Projects/shokunin/kotodama-shokunin .../lane3   # clean re-copy, real S723
```

`lane2`/`lane3` `corpus/README.md` sha256 == the real file's (`9ec525257f0017c043cfba4c827343443f9d16a00b65a6808a88103a8aab731a`), so the copies were byte-identical at the README.

### 1.2 Baseline measurement of the real tree (read-only)

```
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do n=$(ls corpus/knowledge/$p/*.md | wc -l); echo "$p $n"; done
linguistics 29
myth-symbol 29
culture-material 31
synthesis 29
verification 24
civilizations 95
total: 237
```

Real README: `sha256 9ec525257f0017c043cfba4c827343443f9d16a00b65a6808a88103a8aab731a`, 160844 bytes, 711 lines. Section headers at lines 299/331/363/396/428/455; `## Known gaps (frontier)` at 553; `Total knowledge entries: 237.` at 680; `Counts checked 2026-10-23 …` block at 682–684.

### 1.3 First run — the shipped assembler **fails** on the shipped skeleton

```
$ cd lane && python3 -B .ufo/waves/round-64/integrate-w2.py --root . --rows-dir .ufo/waves/round-64/rows --dry-run
INTEGRATE_ERROR missing contribution ids: S723, S740
EXIT=2
```

S723/S740 row directories were absent from `.ufo/waves/round-64/rows/` at that time (31 of 32 contribution directories present). **S723 landed during this seat's run** (verified below); **S740 is still missing as of this report**.

To exercise the README path I supplied scratch-only scaffolds for the absent ids and derived `readme-row.txt` from the skeleton's own `- topic:` line. Scaffolds are labelled `SCAFFOLD` and use `https://example.invalid/…`; they are scratch-only and are **not** proposed as data.

### 1.4 Second run — a shipped-assembler defect (blocking), and its exact mechanism

```
INTEGRATE_ERROR .../rows/ScribeRowS723/row.txt: ROW has 13 cells, not 11     # my scaffold's fault; fixed
INTEGRATE_ERROR .../rows/ScribeRowS723/row.txt: BULLET must be one line ending with exactly (S723)   # my scaffold's fault; fixed
INTEGRATE_ERROR generated entry would fail check-cited-lines.py at line 4: S718,S743   # SHIPPED DEFECT
```

**Defect (shipped, not mine):** `.ufo/waves/round-64/integrate-w2.py` rewrites the skeleton's `- source:` line so the generated entry carries no S-id range:

```python
text = text.replace(
    "Round-64 row citations S718–S743 in `corpus/SOURCES.md` supply the source claims; each claim is limited to its cited row.",
    "Round-64 registry rows in `corpus/SOURCES.md` supply the source claims; each claim is limited to its cited row.",
)
```

The shipped skeleton `.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md:4` reads:

```
- source: S718–S743 in `corpus/SOURCES.md` are the intended evidence anchors; each inserted claim must stay within its cited row.
```

The replacement target string **is not present in either skeleton** (verified: `False` for `rows/ScribeEntrySkeleton/entry.md` and `False` for `stage/skeleton/entry.md`). The replacement is therefore a no-op, the S-id range survives into the generated entry, and the assembler's own `check-cited-lines.py` guard rejects it: `generated entry would fail check-cited-lines.py at line 4: S718,S743` — a genuine MULTI-ID finding under `tools/check-cited-lines.py` (a range is two ids at its ends; `tools/check-cited-lines.py:147-149` selftest cases `range-ascii` / `range-endash`).

Note the two skeletons differ from each other: `stage/skeleton/entry.md:4` reads `- source: the round-64 registry rows in \`corpus/SOURCES.md\` are the evidence anchors; …` (no S-ids, no MULTI-ID), while `rows/ScribeEntrySkeleton/entry.md:4` carries the literal `S718–S743`. The stage copy assembles clean; the rows copy does not.

**Workaround used in scratch only** (patched the scratch copy's replacement target to the *actual* skeleton string):

```
python3 - <<'PY'   # in lane2/ and lane3/
old = '"Round-64 row citations S718–S743 in `corpus/SOURCES.md` supply the source claims; each claim is limited to its cited row."'
new = '"S718–S743 in `corpus/SOURCES.md` are the intended evidence anchors; each inserted claim must stay within its cited row."'
PY
```

After the workaround the assembler completes cleanly:

```
$ python3 -B .ufo/waves/round-64/integrate-w2.py --root . --rows-dir .ufo/waves/round-64/rows
PLAN root=…/lane3
registry: append 32 rows after current final row; 643 -> 675 rows
entry: write corpus/knowledge/linguistics/language-socialization-and-acquisition.md with 26 mapped bullets
README: insert index row; linguistics header 29 -> 30; total/footer 237 -> 238; directory totals 30/29/31/29/24/95
WROTE corpus/SOURCES.md
WROTE corpus/knowledge/linguistics/language-socialization-and-acquisition.md
WROTE corpus/README.md
ASSEMBLED registry_rows=675 entry_files=238
EXIT=0
```

**Owner:** the assembler is `.ufo/waves/round-64/integrate-w2.py`, owned by the integration seat (`ExecIntegrate`). It is not a frozen counter leg, so I did not edit it in the lane; I patched only my scratch copy. The fix is a one-line change to the replacement target string (or, equivalently, to the skeleton line 4 so it carries no S-id range). **Recommendation to the integrator: fix one or the other before the real run — the shipped pair cannot assemble.**

### 1.5 Third run — with the **real** S723 row (no scaffold for S723)

`lane3` was re-copied after S723 landed (`ScribeRowS723/row.txt`, HELM "Language from birth to 5 years old", tier B, overextension/underextension) and assembled with a scaffold for S740 only:

```
ASSEMBLE_OK
sha256(corpus/README.md) = 6f674e1ffce78e7e34b16018b5fce0bdad9eee3856816aa23990b11ecdb1a118
```

**Identical to the scaffolded run's README digest** — the README delta is independent of the row payloads (it depends only on the index row string and the partition counts). S740's payload cannot change the README delta either.

---

## 2. The exact byte-level README delta

Baseline (real): `sha256 9ec525257f0017c043cfba4c827343443f9d16a00b65a6808a88103a8aab731a`, 160844 bytes.
Assembled: `sha256 6f674e1ffce78e7e34b16018b5fce0bdad9eee3856816aa23990b11ecdb1a118`, 161194 bytes.
**Net +350 bytes.**

Unified diff, `n=0` (four hunks, exactly four added lines and three deleted lines):

```
@@ -299 +299 @@
-## linguistics/ (29)
+## linguistics/ (30)
@@ -328,0 +329 @@
+- `language-socialization-and-acquisition.md` — language socialization and acquisition as culturally organized participation in language across caregiver interaction, early talk, correction, multilingual life, narrative, literacy, and address — a sourced design reference for fictional language practices, not a universal developmental sequence.
@@ -680 +681 @@
-Total knowledge entries: 237.
+Total knowledge entries: 238.
@@ -684 +685 @@
-(total 237 files; directory totals 29/29/31/29/24/95).
+(total 238 files; directory totals 30/29/31/29/24/95).
```

Byte accounting, reconciled exactly:

| changed line | old bytes | new bytes | Δ |
|---|---|---|---|
| `## linguistics/ (29)` → `(30)` | 20 | 20 | 0 |
| new index row + `\n` | 0 | 349 | **+349** |
| `Total knowledge entries: 237.` → `238.` | 29 | 29 | 0 |
| footer `(total 237 files; directory totals 29/29/31/29/24/95).` → `(total 238 files; directory totals 30/29/31/29/24/95).` | 54 | 54 | 0 |
| **net** | | | **+350** |

Sum of line deltas = +350 = measured net = +350. No other byte of the 711-line file changes: the header block, the other five partition sections, the whole `## Known gaps (frontier)` body, and every other prose line are byte-identical.

**Vector semantics.** The footer's six-vector stays in the README's own section order (`linguistics/myth-symbol/culture-material/synthesis/verification/civilizations`): `29/29/31/29/24/95` → `30/29/31/29/24/95`. Only the `linguistics` element moves. The totals line moves 237 → 238 and the footer's `total` moves 237 → 238 in the same transaction (the four-part landing transaction the lane's own `corpus/knowledge/verification/index-sweep-verification.md` §6 "Counts move together" and DR-IS-04 require).

**Index row placement.** The assembler appends the new row at the **end** of the `## linguistics/` section (after `writing-systems.md`, position 30 of 30), *not* in filename order. The lane's recorded convention is filename order (`index-sweep-verification.md` §6 "Rows: added in filename order"; DR-IS-07; every prior revision block in the README says "its row added in filename order"). Measured on the real README, all six partitions are currently in strict filename order (0 adjacent inversions each, verified). The assembled README introduces exactly one inversion:

```
linguistics: 30 rows, violations: [('writing-systems.md', 'language-socialization-and-acquisition.md')]
myth-symbol: 29 rows, violations: []
culture-material: 31 rows, violations: []
synthesis: 29 rows, violations: []
verification: 24 rows, violations: []
civilizations: 95 rows, violations: []
```

Correct filename slot is index **8**, between `language-shift-obsolescence-revival.md` (real README line 307) and `linguistic-anthropology.md` (real README line 308). I re-placed the row at that slot in `lane2` and re-measured: `linguistics: 30 rows, violations: []`, sweep exit 0. **Recommendation: the landing must place the row at the filename-order slot; `integrate-w2.py`'s `assemble_readme` currently appends at the section end.** (Nothing in `reports/round-28/readme/sweep.py` checks filename order — it checks rows-vs-files, ghosts, topic equality, header drift, totals line, footer — so a filename-order defect is invisible to the sweep and to `accept-c.py`'s SWEEP leg. This is a gap in the instrument, not in the landing.)

---

## 3. Topic-string check — index row vs the entry's `- topic:` line

**PASS — byte-equal.**

Extracted from the *generated* entry `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` with the same rule the assembler and the sweep use (`^- topic:(.*?)(?=\n- \w)`, continuations space-joined), then compared to the README row's text after the em dash:

```
byte-equal: True
topic sha256: 25ef9354ae60f0b51254e7475fdc97a89f1c2268575b0d134f8b9957b67fd4a5
row   sha256: 25ef9354ae60f0b51254e7475fdc97a89f1c2268575b0d134f8b9957b67fd4a5
topic bytes: 299
```

The topic string (299 bytes) is:

> language socialization and acquisition as culturally organized participation in language across caregiver interaction, early talk, correction, multilingual life, narrative, literacy, and address — a sourced design reference for fictional language practices, not a universal developmental sequence.

The assembler's own `readme_row_from_skeleton` raises `AssemblyError` if the row topic differs from the generated entry's `- topic:`, and it did not raise — so this is enforced twice over.

**Independent re-measurement of the sweep's topic leg on the assembled README** (`reports/round-28/readme/sweep.py`, exit 0):

```
parts {"civilizations": 95, "culture-material": 31, "linguistics": 30, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 238 files 238
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 238 totals_ok True
footer {"date": "2026-10-23", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 238, "dir_totals": [30, 29, 31, 29, 24, 95]}
footer_live {"total": 238, "dir_totals": [30, 29, 31, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
```

`accept-c.py`'s SWEEP leg on the assembled tree: `SWEEP PASS exit=0 topic_row=True`.

### 3.1 Topic-ownership measurement for the new entry (needed for honest revision prose)

Read-only scan of all 237 real entries' own `- topic:` lines and filenames:

- **Filename owners of "language socialization / acquisition": 0** (`grep` over `corpus/knowledge/**` filenames: no file name contains `socialization` or `acquisition`).
- **Topic-line owners of the new topic: 0.** The three linguistics entries whose topic line contains the token "acquisition" (`gesture-co-speech-pointing.md`, `language-shift-obsolescence-revival.md`, `sacred-registers-liturgical-language.md`) own *acquisition* in other senses — gesture development, second-language acquisition, and register acquisition — not language socialization/acquisition as a register.
- **One-way partial mentions:** `linguistics/dialect-register-consistency.md` (mentions "resocialization" as a registered mechanism, citing `linguistic-anthropology.md:117-123`), `linguistic-anthropology.md:122` (Resocialization in the anti-society induction list), `civilizations/hopi.md`. None is an owner of this topic.

So the honest statement is: **0 filename owners, 0 topic-line owners**; partial owners cited one-way exist and must not be read as owners. This matches the wording convention of the recent revision blocks (e.g. rev 2.16: "before it, 0 filename owners and partial owners cited one-way in its §6").

---

## 4. The README's frontier surface — what exists, and what does not

**Correction to the task premise:** `corpus/README.md` has **no `## Frontier` heading**. Its only frontier surface is `## Known gaps (frontier)` at line 553. Verified: `grep -n "^## Frontier" corpus/README.md` → no match; the `## Frontier` headings live in `corpus/lessons/round-49.md` … `round-59.md` (and round-63's lesson uses `## Sources & frontier`). There is **no `corpus/lessons/round-64.md`** yet — that file is the `ScribeLesson` seat's scope, not mine, and I did not create it.

So the "minimal honest update" has two surfaces:

1. **A new `revision:` block at the head of `corpus/README.md`** — required by the lane's own append-only landing rule (`index-sweep-verification.md` §6 "Revision blocks are append-only: a landing writes a NEW revision block with its own re-measurement line"; DR-IS-07). The current newest label is `2.16`; the next is `2.17`. `tools/check-readme-revisions.py` requires unique labels in non-increasing order top-to-bottom, so `2.17` must be inserted directly under the H1.
2. **One bullet appended to `## Known gaps (frontier)`** — naming the new entry and its partition, and stating what remains open.

Both were applied in `lane2` (scratch only) and re-measured:

```
$ python3 -B reports/round-28/readme/sweep.py   → exit 0 (238 rows vs 238 files, 0 topic mismatches)
$ python3 -B tools/check-readme-revisions.py    → exit 0, findings 0 (labels 2.17, 2.16, … 1.3; 1 pre-existing REVISION-ORPHAN warning, unchanged)
$ python3 -B tools/check-readme-heading.py      → exit 0, findings 0 (h1 1, headings {1:1, 2:7})
$ python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/language-socialization-and-acquisition.md → 0 findings, exit 0
```

The pre-existing `REVISION-ORPHAN` warning (unheaded paragraph at lines 180/191 of the real README, the round-28 landing note) is carried unchanged by the patch — it is a dated record, not a new defect, and the control explicitly keeps it advisory.

**Receipt — `accept-c.py` re-run against the patched copy** (`lane2`, S723 **scaffolded** + S740 scaffolded; completed 2026-10-23, wall time 170.93 s):

```
FILE PASS exists lines=81 h1=1 h2=10 h3=0 topic=True
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
HOSTS PASS bad=[]
SWEEP PASS exit=0 topic_row=True
ACCEPT-C-64: FAIL
```

The **SWEEP leg — the only leg this seat's scope touches — prints PASS on the patched README**, confirming that the §4.1 fragment (revision block + filename-order index row + known-gaps bullet) leaves the index structurally consistent with the assembled tree: the new bullet's prose is outside the sweep's structural comparison, which the lane's own audit records (`reports/round-19/audit/x27-coverage-readme-vs-files.md:140-142`, DR-IS-09 open). `ACCEPT-C-64: FAIL` is not attributable to the patch: the failing legs on this run are ROWS, RESTATE, LINK, APPEND, NOHARM and LIVE, whose causes are enumerated and corrected in §5/F6 (my two scaffolds — `lane2` predates the real S723 — plus the S687 `mined → queued` enactment and the not-yet-committed landing). The authoritative run, with the **real** S723 row, is F6b in §5: `SWEEP PASS exit=0 topic_row=True` and `LIVE PASS … bad=[]`, with the only failures being my S740 scaffold and the two named non-README obligations. **No claim is made that claim C passes.**

### 4.1 Proposed patch fragment (NOT applied to the real README)

Apply to the real `corpus/README.md`. Three edits, in this order.

**(a) New revision block — insert after the H1 and its blank line, before `revision: 2.16`.** Real README lines 1–3:

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -1,5 +1,17 @@
 # kotodama-shokunin corpus index
 
+revision: 2.17 — Round-64 linguistics landing (2026-10-23): one
+linguistics entry landed (`language-socialization-and-acquisition.md`,
+language socialization and acquisition as culturally organized participation
+in language), its row added in filename order between
+`language-shift-obsolescence-revival.md` and `linguistic-anthropology.md`
+with the entry's `- topic:` text verbatim; `## linguistics/` moved 29 → **30**;
+the totals line and the counts footer moved 237 → **238** and the footer
+vector 29/29/31/29/24/95 → **30/29/31/29/24/95**. Re-measured with
+`python3 -B reports/round-28/readme/sweep.py`: 238 rows vs 238 files, exit 0.
+Non-canon examples and passing structural gates do not certify historical
+truth.
+
 revision: 2.16 — Round-63 culture-material landing (2026-10-23): one
```

**(b) Index row at the filename-order slot — insert between real README line 307 (`language-shift-obsolescence-revival.md`) and line 308 (`linguistic-anthropology.md`):**

```diff
@@ -305,6 +317,7 @@
 - `language-contact.md` — how languages converge — borrowing scales and hierarchies, loanword adaptation, pidgins/creoles/mixed languages, Sprachbund (linguistic-area) features, and using strata of loans to date fictional history
 - `language-shift-obsolescence-revival.md` — The life-cycle side of language contact — … (unchanged)
+- `language-socialization-and-acquisition.md` — language socialization and acquisition as culturally organized participation in language across caregiver interaction, early talk, correction, multilingual life, narrative, literacy, and address — a sourced design reference for fictional language practices, not a universal developmental sequence.
 - `linguistic-anthropology.md` — Language as cultural practice — … (unchanged)
```

**(c) Known-gaps bullet — append at the end of the `## Known gaps (frontier)` bullet list, immediately before the `Total knowledge entries: 238.` line (real README line 680 becomes 693 after (a) and (b)):**

```diff
@@ -677,11 +690,27 @@
   `reports/round-{5,6}/parent-reconciliation.json` receipts and name the drift;
   do not edit the old runners.
 
-Total knowledge entries: 237.
+- Round 64 adds one linguistics entry
+  (`linguistics/language-socialization-and-acquisition.md`, language
+  socialization and acquisition as culturally organized participation in
+  language: caregiver registers, early talk, correction, multilingual
+  childhoods, narrative and literacy, names and address), supported by 26
+  registry rows S718–S743 and six disposition rows S744–S749 that record
+  rejected or queued candidates rather than mined claims. The entry is a
+  sourced design reference, not a universal developmental sequence and not
+  fictional canon; each claim stays inside its cited row, and every row
+  carries its own recheck interval. The index was re-measured after the
+  landing (238 rows vs 238 files; 0 missing, 0 ghosts, 0 topic mismatches;
+  `## linguistics/` 30, footer 238 / 30/29/31/29/24/95; exit 0) with
+  `python3 -B reports/round-28/readme/sweep.py`; command and receipts in
+  `reports/round-64/`. The rows 5–7 residuals carried by the rounds 5–7
+  bullets above remain open.
+
+Total knowledge entries: 238.
```

**Honesty constraints embedded in the fragment, and why:**

- The bullet names the entry and its partition (`linguistics`) explicitly — that was the ask — and says what the entry *is* ("a sourced design reference, not a universal developmental sequence and not fictional canon") in the entry's own `- topic:` wording rather than in a paraphrase.
- It states 26 mined rows and six disposition rows, and characterises the six as *dispositions* (rejected/queued candidates), not as mined claims — matching `accept-c.py`'s own REJECTS leg semantics.
- It does **not** claim a universal developmental sequence, a canon decision, or truth: the corpus's own standard (rev 2.16's closing sentence, `index-sweep-verification.md` DR-IS-08) is that a green sweep certifies description, not veracity.
- It carries the round-5/6/7 residuals forward as still open, so the new bullet does not read as closing older gaps.
- It states the measured numbers *with* the instrument and the exit code, per DR-IS-03 ("a green reading is quoted only with the README digest, the instrument identity and its selftest verdict, and the date"). The digest to cite at landing time is the post-landing README sha256 — measured in scratch as `b24276c6e0d89732fb493a380a130e16f370ef3f01bda55e230c171fa7a7fd59` for the patched file, 162938 bytes. **Re-measure and cite the real digest at landing; do not reuse the scratch digest.**
- It does not name a "gap filled" line: only 44 of 237 entries carry `- gap filled:` in their header, so the convention is not universal, and the new entry's own header (from the skeleton) carries `- topic:`, `- source:`, `- verified-at:`, `- recheck:` — no `- sources:`, no `- couples:`, no `- gap filled:`. See §6.

**Not proposed:** a `## Frontier` heading inside `corpus/README.md`. Adding one would invent a section the file has never had; the lane's frontier prose lives in `corpus/lessons/round-NN.md` (owned by `ScribeLesson`), and the README's own frontier is `## Known gaps (frontier)`.

---

## 5. Findings

**F1 (BLOCKING, shipped assembler vs shipped skeleton).** `.ufo/waves/round-64/integrate-w2.py`'s `- source:` replacement target string is not present in `.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md:4`, so the replacement is a no-op, the literal `S718–S743` survives into the generated entry, and the assembler aborts with `generated entry would fail check-cited-lines.py at line 4: S718,S743`. Reproduced twice: once against `rows/ScribeEntrySkeleton/entry.md`, and once via the stage copy `stage/skeleton/entry.md` (which has no S-ids and assembles clean). Owner: `ExecIntegrate` (assembler) / `ScribeEntrySkeleton` (skeleton). Fix: align the replacement target with the skeleton line, or drop the S-id range from the skeleton's `- source:` line. Neither file is a frozen counter; I did not edit either.

**F2 (BLOCKING, missing row).** `ScribeRowS740` is still absent from `.ufo/waves/round-64/rows/` as of this report (S723 landed mid-run and is now present). `integrate-w2.py` exits 2 with `missing contribution ids: S740` without it. Owner: `ExecRowS740`. The README delta is unaffected by S740's payload (§1.5).

**F3 (landing-correctness defect in the assembler, not caught by any gate).** `assemble_readme` appends the new index row at the **end** of the `## linguistics/` section, not at its filename-order slot (index 8 of 30, between `language-shift-obsolescence-revival.md` and `linguistic-anthropology.md`). All six partitions are in strict filename order today (0 inversions each); the assembled file introduces exactly one inversion, violating `index-sweep-verification.md` §6 / DR-IS-07 and every prior revision block's "its row added in filename order" wording. `reports/round-28/readme/sweep.py` and `accept-c.py`'s SWEEP leg are both **blind** to filename order (they check rows-vs-files, ghosts, topic equality, header drift, totals, footer). Re-placing the row at slot 8 in scratch restored 0 inversions with sweep exit 0. Owner: `ExecIntegrate` (fix `assemble_readme`) and, separately, an instrument owner for the order leg (see F4).

**F4 (instrument gap, calibration axis).** Neither `reports/round-28/readme/sweep.py` nor `tools/check-readme-revisions.py` nor `tools/check-readme-heading.py` asserts filename order of the index rows, even though the lane's own verification entry records it as a landing rule (`index-sweep-verification.md` §6, DR-IS-07). A landing can therefore break the ordering convention and every gate stays green. A pre-data revision to `sweep.py` adding a filename-order leg (with its own selftest control) would close this; that is a counter change and therefore **not** mine to make — recording it for the canonical judge.

**F5 (README count drift is the assembler's job and it is correct here).** The assembler moves the header count, the totals line, and the footer total + six-vector in one transaction, exactly as DR-IS-04 requires. Measured: `## linguistics/ (29)` → `(30)`, `Total knowledge entries: 237.` → `238.`, footer `(total 237 files; directory totals 29/29/31/29/24/95).` → `(total 238 files; directory totals 30/29/31/29/24/95).` Sweep `footer_findings []`, `header_drift {}`, `totals_ok True`. No drift found.

**F6 (claim-C counter legs — observation only, not my scope to fix).**

**F6a — run on `lane2` (S723 *scaffolded*, S740 scaffolded; S723 had not landed when `lane2` was copied).** `accept-c.py --root .` printed:

```
FILE PASS   ROWS FAIL bad=['S723:quote_words=2', 'S723:no_capture', 'S740:quote_words=2', 'S740:no_capture'] checked=26
REJECTS PASS  ONEID PASS  RESTATE FAIL bad=['line27:S723:content=3', 'line63:S740:content=3'] lines=26
HOSTS PASS  LINK FAIL bad=['S723:registry_hits=2', 'S740:registry_hits=2']
APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=675 +32=True
NOHARM FAIL diff=[]  SWEEP PASS exit=0 topic_row=True
LIVE FAIL subset=['S718','S723','S728','S733','S738','S743'] bad=['S723:NOT_LOCATED quote under 8 words']
ACCEPT-C-64: FAIL
```

**F6b — run on `lane3` (S723 **real**, S740 scaffolded only).** `timeout 400 python3 -B reports/round-64/accept-c.py --root .` (wall time 105.60 s) printed:

```
FILE PASS exists lines=81 h1=1 h2=10 h3=0 topic=True
ROWS FAIL bad=['S740:quote_words=2', 'S740:no_capture'] checked=26
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line63:S740:content=3'] lines=26
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=675 +32=True
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=[]
ACCEPT-C-64: FAIL
```

**Correction to an earlier reading of mine.** The `S723:*` findings in F6a are **scaffold artifacts of mine, not a counter/row-shape defect**. `lane2` was copied before the real S723 landed, so its `| S723 |` registry line was my `example.invalid` placeholder; every `S723:*` string in F6a traces to that placeholder (the placeholder's anchor cell is the two-word `"scaffold quote"` → `quote_words=2`; it has no `web.archive.org` capture → `no_capture`; its URL appears on both the S723 and S740 lines → `registry_hits=2`; its bullet has three content words → `content=3`; and its two-word quote is `NOT_LOCATED` under the LIVE leg's ≥8-word rule). With the **real** S723 row in place (F6b), every S723 finding disappears and the LIVE leg — which includes S723 in its frozen subset — prints `PASS bad=[]`.

I verified the real S723 row against the counter's own extraction rules before drawing that conclusion: the registry line has 11 cells; the source cell ends `…/web/20260324122540id_/https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html`; `CAPTURE_RE` matches it (`ts=20260324122540`); `norm_url(cap.group(2)) == norm_url(urls[0])`; and the anchor quote "In overextension, children use a simple word to refer to many different things." normalises to **13 words**, inside the leg's 8–25 band. The real row's `CAPTURE:` field reads `timestamp=20260324122540; original=https://…`; that field format differs from some siblings' `url=` (S718) but is not what the counter reads — the counter reads the registry **source cell**, where the archive URL does sit. **There is no frozen-counter defect on S723. I withdraw the earlier claim.**

What actually remains failing on `lane3` (F6b), and who owns each:

- `ROWS` / `RESTATE` — **caused by my S740 scaffold only.** With a real S740 these should clear; the lane3 result shows zero findings for any of the 25 other mined rows.
- `APPEND … s687_queued=False` — **claim C's enactment obligation, not mine.** `accept-c.py:347-356` requires a registry row `| S687 …` whose status cell is `queued`; the base row at `ff30a20` reads `mined` and the measured registry still reads `mined` (`corpus/SOURCES.md:642`). The routed provenance is `ScoutLessonRecon.md:10` (round-62 item 7 / round-63 defect 6.4) and `CriticCa.md` §C, which states the flip belongs to C, not to Ca. Owner: `ExecIntegrate` (the land), with the old→new logged in the round-64 lesson. The counter is frozen and I did not touch it.
- `NOHARM diff=[]` — **not a defect; a landing-state artifact.** The leg runs `git diff --name-only <base> main -- corpus/knowledge` (`accept-c.py:360-364`), which compares two **commits**, so an uncommitted working tree reads as empty. I verified satisfiability in scratch: after committing the new entry on `main`, the same command prints exactly `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` and nothing else. Owner: whoever commits the landing.
- `SWEEP PASS` — the leg this seat's scope owns, green on both the assembler output and the §4.1 patched README.
- `ACCEPT-C-64: FAIL` — **no claim is made that claim C passes.** Every remaining failure above is either my own scaffold or a named non-README obligation.

**F7 (entry header shape, out of my scope).** The generated entry's header carries `- topic:`, `- source:`, `- verified-at:`, `- recheck:` — but no `- sources:`, no `- couples:`, no `- gap filled:`. Measured across the 237 real entries: `- sources:` 237/237, `- couples:` 224/237, `- verified-at:` 221/237, `- gap filled:` 44/237. The new entry therefore diverges from the one universal convention (`- sources:`). `- source:` (singular) is also not the field name any instrument reads. This is an entry-shape question for `ExecIntegrate`/`ReviewerEntry`; the `- verified-at:` line additionally still says "cited source claims await L1 insertion and review", which becomes stale the moment the bullets are inserted. Not a README defect, but it is the kind of thing the landing should not carry silently.

---

## 6. Scope boundaries and non-claims

- The real `corpus/README.md` was **not** modified. `sha256` of the real file is unchanged at `9ec525257f0017c043cfba4c827343443f9d16a00b65a6808a88103a8aab731a` (160844 bytes) — verified by re-reading it after all scratch work.
- No lane `jj` operation, no commit, no index mutation, no edit to any counter, judge, or product code. All changes were confined to `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReadmeFrontier/` and to this report file.
- **No claim is made that claim C passes.** `ACCEPT-C-64: FAIL` was printed on the scratch trees. With the **real** S723 row in place (`lane3`, F6b) the only failures are my own S740 scaffold (`ROWS`/`RESTATE`) and two named non-README obligations (the S687 `mined → queued` enactment, and `NOHARM`'s requirement that the landing be committed on `main`). The SWEEP leg — the only leg my scope touches — printed `PASS exit=0 topic_row=True` on both the assembler output and the patched README.
- **No claim is made that the entry's content is true.** The sweep and the cited-lines tool certify description and citation shape; `corpus/README.md`'s own footer says "The inventory counts markers, not verified facts", and `index-sweep-verification.md` DR-IS-08 rejects reading a green sweep as correctness or canon.
- The scratch scaffolds are labelled `SCAFFOLD`/`example.invalid` and are not proposed as data; the README delta was shown to be independent of them (§1.5). The `lane3` tree carries the **real** S723 row and a scaffold for S740 only.
- No `corpus/lessons/round-64.md` was created — that is `ScribeLesson`'s scope.

## 7. Artifact paths

- This report: `.ufo/waves/round-64/w1/ScribeReadmeFrontier.md`
- Scratch tree with the assembled README: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReadmeFrontier/lane3/corpus/README.md` (sha256 `6f674e1ffce78e7e34b16018b5fce0bdad9eee3856816aa23990b11ecdb1a118`, 161194 bytes) — assembler output only.
- Scratch tree with the assembler output **plus** the §4.1 patch applied: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReadmeFrontier/lane2/corpus/README.md` (sha256 `b24276c6e0d89732fb493a380a130e16f370ef3f01bda55e230c171fa7a7fd59`, 162938 bytes) — all three README controls exit 0.
- Patched assembler (scratch only): `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReadmeFrontier/lane3/.ufo/waves/round-64/integrate-w2.py`.

## 8. Tooling

No tool was installed or upgraded for this seat. Everything used was already present: `python3` (3.14, stdlib only), `git` (read-only `show`/`diff`/`log` in the lane), `grep`, `sha256sum`, `wc`, `diff`. No pacman transaction was run.
