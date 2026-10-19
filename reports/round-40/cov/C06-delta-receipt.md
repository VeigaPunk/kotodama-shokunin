- Seat: C06 | executor (claim C) | README rev-2.3 delta draft + coverage receipt draft | date 2026-10-19 | baseline fd55e1f

# C06 — `corpus/README.md` revision-2.3 delta draft + claim-C coverage receipt draft

**Assignment** (`reports/round-40/targets.json:83-88`, seat C06): "README rev 2.3 delta draft:
linguistics header 21→25, totals 212→216→220, footer vector 21/23/25/29/24/94 →
25/23/25/29/24/94, 4 rows in filename order (linguistics section) + coverage receipt draft."
Out path: this file only. Binding shared rules read at `reports/round-40/targets.json:4-9`;
claim C read at `reports/round-40/claims.json:13-18`; this seat's obligations read at
`reports/round-40/plan/P01-plan.md:58-63` (P01 §1.5 step 5) and X00's constraints at
`reports/round-40/cross/X00-connector.md:36-38` (README row byte-equal to the landed
`- topic:`; sweep green post-apply; rows re-derived from the FINAL filename set).

**Status: DRAFT — integrator-applied.** This seat wrote **zero** bytes outside this file and
the disposable scratch under `.scratch/c06/`: no corpus entry, no README byte, no tool byte, no
filed-round byte. No `reports/round-*/run-validation.py` was executed anywhere (absolute rule,
`reports/round-40/targets.json:8`). Every *before* figure below is this seat's own measurement
at the pinned state (§2); every *after* figure is either the declared target
(`reports/round-40/claims.json:16`) or a mechanically generated value from the tested generator
(§5), and the sweep reading that certifies the landing is **measured at close, never
predicted** (§8 — the `readme-prediction-vs-delivery` rule,
`reports/round-37/op/defect-queue.json:242-251`).

Note on the mission's "totals 212→216→220": the 212→216 leg is revision 2.2's move, already
landed in the pinned README (`corpus/README.md:9-10`); **this delta's totals leg is 216 → 220**
(P01 `reports/round-40/plan/P01-plan.md:58-61` states the same). The footer-vector leg is the
first slot only: 21/23/25/29/24/94 → **25**/23/25/29/24/94.

**What landed at this seat's cut** (polls 14:48:19Z–15:00:55Z): scouts K01/K03, executors
C01/C02/C03 (all three staged and digested, §6), X00's connector. **C04's fragment
(`reports/round-40/cov/C04-entry-4.md`) was still absent at the 15:00:55Z poll** — the fourth
row's bytes stay owed (§Owed); the delta is otherwise complete and the full 21→25 arithmetic is
proven end-to-end with a labeled candidate probe in the fourth slot (§5.4). Three of four rows
are known byte-exact (§6).

---

## 1. The invariant the delta must satisfy (measured, not assumed)

An index row is ``- `<file>.md` — <text>`` where `<text>` is the entry's own `- topic:`
head-block text with continuation lines space-joined to one line. That is what the lane's index
instrument measures (row contract measured and pinned by r39 C06,
`reports/round-39/cov/C06-delta-receipt.md:30-38`; re-accepted this seat by the §5.3 synthetic
rig, whose applied copy the sweep reads clean including the verbatim-topic leg). Instrument
`reports/round-28/readme/sweep.py`: sha256
`9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` (identical to the r39 pin);
`--selftest` 12/12 (`python3 -B reports/round-28/readme/sweep.py --selftest` → `selftest: 12/12
checks passed`, run this seat 2026-10-19); read-only in live mode per its own docstring
(`sweep.py:28-30` — "no code path that writes inside the lane"; the only write sites are the
`--selftest` synthetic-tree controls, `sweep.py:76,257,284,397,421`).

Baseline reading at authoring (all legs green, measured this seat 2026-10-19 at HEAD `fd55e1f`):

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 21, "myth-symbol": 23,
       "synthesis": 29, "verification": 24}
rows 216 files 216; missing_from_index 0; topic_mismatch 0; orphan_rows 0; header_drift {}
totals_line 216 totals_ok True
footer total 216, dir_totals [21, 23, 25, 29, 24, 94]; footer_ok True; exit 0
readme_sha256 e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a
```

The vector order is the README's own section order (linguistics-first; measured by the sweep's
`footer_live.order`, same output). K03 measured the identical census independently
(`reports/round-40/scout/K03-gaps.md:7-10`: linguistics 21, verification 24 — "claim C's
premise holds"), P01 states it at plan time (`reports/round-40/plan/P01-plan.md:14-19`), and
X00 confirms it (`reports/round-40/cross/X00-connector.md:204`). Three fragments, one reading.

## 2. Before state — measured (claim-C receipt, counting commands)

`git rev-parse HEAD` → `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` (== the declared baseline
`fd55e1f`, `reports/round-40/claims.json:7`). `git status --porcelain` → ` M LOG.md`
(parent-owned) + `?? reports/round-40/` only: the corpus tree is byte-identical to HEAD for
every path measured here. Env for every command:
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, lane root.

### 2.1 Counting command 1 (verbatim, `reports/round-40/claims.json:17`)

```sh
$ ls corpus/knowledge/linguistics/*.md | wc -l
21
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21
23
25
29
24
94
$ find corpus/knowledge -name "*.md" -type f | wc -l
216
```

The loop order is the README footer vector's order (`corpus/README.md:522` =
`21/23/25/29/24/94`, linguistics-first), so the after vector is **25/23/25/29/24/94** — same
string in the census loop's order; writing it in any other order would not be.

### 2.2 Counting command 2 (verbatim, `reports/round-40/claims.json:17`)

```sh
$ python3 -B reports/round-28/readme/sweep.py
# exit 0; readings quoted in §1; readme_sha256 e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# exit 0; schema kotodama-source-audit-inventory/1, "read_only": true; totals.files 216
#         (per-directory derivation: [21, 23, 25, 29, 24, 94])
```

The inventory counts markers, not verified facts (`corpus/README.md:523`); a marker count is
not a quality score. Entry quality is C05's and R01's evidence; this receipt owns **counts and
their reconciliation** only.

### 2.3 State pins (the before state is recoverable from git alone)

| pin | value | command |
|---|---|---|
| baseline commit | `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` | `git rev-parse HEAD` |
| corpus tree object | `608ef479d23051d6b4211bc40e52ccb7ffeaf4b2` | `git rev-parse HEAD:corpus/knowledge` |
| pinned path-manifest digest | `a89679bf6830314d04be3b6c6041e89f920f3ee57d80411e1ce06f1d7e9ea2eb` | `git ls-tree -r --name-only 608ef479… \| sort \| sha256sum` |
| live manifest digest (same value) | `a89679bf…` (216 paths) | `find corpus/knowledge -name '*.md' -type f \| sort \| sed 's\|^corpus/knowledge/\|\|' \| sha256sum` |
| `corpus/README.md` digest | `e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a` | `sha256sum corpus/README.md` |
| README size | 549 lines / 132,721 bytes | `wc -lc corpus/README.md` |
| sweep instrument digest | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` | `sha256sum reports/round-28/readme/sweep.py` |

The two manifest digests agreeing is the measurement that the before state is exactly the
baseline commit's corpus. §8's A7 leg reads `new 0 / removed 0` against this pin at the before
state (observed, §8.1) — the pin is real, not decorative.

## 3. Line map of the pinned README (all edits reference these)

| line | content (pinned bytes) |
|---|---|
| 1, 3 | `# kotodama-shokunin corpus index` — **duplicated H1, carried defect** (`R36-README-DUPLICATE-HEADING`, `reports/round-37/op/defect-queue.json:103-131`; X00-7 of r39) — **not touched by this delta** |
| 5–12 | `revision: 2.2 — Round-39 verification-partition expansion (2026-10-19): four …` block |
| 14, 16 | duplicated `revision: 2.0` opening line — **carried defect** (same queue rows) — **not touched by this delta** |
| 158 / 182 / 208 / 235 / 267 / 294 | section headers `## linguistics/ (21)` / `## myth-symbol/ (23)` / `## culture-material/ (25)` / `## synthesis/ (29)` / `## verification/ (24)` / `## civilizations/ (94)` |
| 160–180 | the 21 linguistics rows, filename-sorted (160 `color-terminology.md` … 180 `writing-systems.md`) |
| 391 | `## Known gaps (frontier)` — no round-39 bullet was added by rev 2.2; none added here |
| 518 | `Total knowledge entries: 216.` |
| 520 | `Counts checked 2026-10-19 from the repo root:` — date already current; **no edit** |
| 521 | the inventory command line — **no edit** |
| 522 | `(total 216 files; directory totals 21/23/25/29/24/94).` |
| 523 | `The inventory counts markers, not verified facts.` — **no edit** |
| 524–531 | superseded-reading paragraph, ends `…with the ten round-35 entries.` (records moves up to rev 2.0; revs 2.1/2.2 did **not** append to it) |
| 533–549 | dated `Index rows …` paragraphs (round-10 / round-19 / round-20 / round-35; 549 is the file's last line, ending `…partition counts 21/23/24/29/20/94).`) |

## 4. Byte-exact, name-independent edits (apply in this order; rows in §5 land in the same motion)

### E1 — new revision block (insert between line 4 and line 5)

before (lines 3–5):

```
# kotodama-shokunin corpus index

revision: 2.2 — Round-39 verification-partition expansion (2026-10-19): four
```

after (lines 3–6):

```
# kotodama-shokunin corpus index

revision: 2.3 — Round-40 linguistics-partition expansion landing (2026-10-19): the four
```

The full block is drafted in §7 with ⟨…⟩ slots filled at integration time. Insertion goes
**after the blank line following the duplicated H1 (line 3) and before `revision: 2.2`** — the
exact position rev 2.2 itself took above rev 2.1 (pinned lines 3–5), with one blank line
separating the new block from the rev-2.2 block (the applied rev-2.2 shape, pinned lines
12–14). The duplicated-H1 and duplicated-rev-2.0-line defects are inserted around, never
repaired here (P01 `reports/round-40/plan/P01-plan.md:154-156` collision control; the r39
X00-7 precedent).

### E2 — linguistics section header (line 158)

```
-## linguistics/ (21)
+## linguistics/ (25)
```

### E3 — totals line (line 518)

```
-Total knowledge entries: 216.
+Total knowledge entries: 220.
```

### E4 — counts footer (line 522 only)

```
-(total 216 files; directory totals 21/23/25/29/24/94).
+(total 220 files; directory totals 25/23/25/29/24/94).
```

Lines 520 (date — already 2026-10-19) and 521 (command) are unchanged; the sweep's footer leg
compares the declared total and six directory totals against the live tree and does not parse
the date, but the block remains an honest present-tense claim only if re-measured at landing —
§8's post-apply sweep is that re-measurement.

### E5 — new dated index paragraph (append after line 549, the current last line)

```
Index rows re-measured 2026-10-19 at HEAD `⟨sha⟩` after the round-40 wave
(220 rows vs 220 files; the four new rows above added to the linguistics section;
0 missing, 0 ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches; partition
counts 25/23/25/29/24/94).
```

⟨sha⟩ and the reading are **measured at close** (the landing commit and the post-apply sweep);
if the sweep is not green, E5 is not written. Precedent for the shape: the round-35 paragraph
at `corpus/README.md:546-549`.

**Deliberately not in this delta:** (a) any edit to the superseded-reading paragraph
(:524–531). Revision 2.0 appended its move there; revisions 2.1 and 2.2 did not (their moves
live only in their blocks, :5-21). This delta follows the **most recent landing precedent
(rev 2.2)** and records the move in the §7 block only; if the integrator prefers the rev-2.0
style, the optional append after line 531 is `Revision 2.3 moved the totals 216 → 220 and
\`## linguistics/\` 21 → 25 with the four round-40 entries.` — one decision, either reading
sweeps green. (b) A new `## Known gaps (frontier)` bullet — revisions 1.7–2.2 added none; the
round-40 coverage record belongs to this receipt and S01's dossier, not the index. (c) Any
repair of the carried H1/rev-2.0 duplication defects (see E1). (d) **No edit of any existing
row** — the 21 linguistics rows stay byte-identical; the delta only inserts.

## 5. The four row insertions (name-dependent — rule + tested generator, not guessed bytes)

**Rule.** Each new row is ``- `<file>.md` — <entry's own continuation-joined `- topic:` text>``
inserted where `<file>.md` sorts (ASCII) among the section's rows. Existing rows are
filename-sorted today (verified in §1's sweep: `orphan_rows 0`, and structurally in the
synthetic check, §5.3), so "filename order" and "row order" coincide.

**Final-filename authority (X00 C1, `reports/round-40/cross/X00-connector.md:36-38`):** the
integrator fixes the final filename set and C06's rows are re-derived mechanically from the
**landed bytes** at apply time — the generator (§5.1) emits each row from the entry file
itself, so the landing equality is whatever the landed bytes say, never this draft's table.
The anchors below are the generator's own staged dry-run output, not hand arithmetic.

### 5.1 Generator (tested; integrator places it, e.g. `reports/round-40/readme/readme-delta.py`)

Read-only unless `--apply` names a path. This is the round-39 C06 generator
(`reports/round-39/cov/C06-delta-receipt.md:237-377`, field-tested end-to-end there) narrowed
to the linguistics partition; totals/footer always computed over all six partitions. The exact
tested bytes were written this seat to `.scratch/c06/readme-delta.py` (disposable; the source
is r39 §5.1 with the docstring, default `--parts ["linguistics"]`, and nothing else changed —
diff is 3 lines). Invocation:

```sh
python3 readme-delta.py                     # text report
python3 readme-delta.py --json              # machine delta
python3 readme-delta.py --apply OUT.md      # write reconciled copy to OUT.md
python3 readme-delta.py --root ROOT         # dry-run against a staged tree
```

`--apply` writes only the path given and only the three mechanical families (header, rows,
totals/footer line). E1/E5's prose is **not** written by it — apply those by hand from §4/§7 so
the prose is authored, not templated (the r35 placeholder lesson, `SCORECARD.md:681-684` via
r39's X00). **Apply-order rules** (measured in the r35 synthetic run, inherited unchanged): one
global bottom-up pass over the whole file for all row insertions; on a shared anchor, larger
`merged_index` first; a row that sorts first in a section inserts at header line + 1. Entries
land **before** the README delta in one motion, or the tree sits in an intermediate red state
(expected reds: entries-without-rows = 4 `missing_from_index`; rows-without-entries = 4
ghosts — X00 integration steps,
`reports/round-40/cross/X00-connector.md:124-136`).

### 5.2 Anchors — staged dry-run with the three landed entries (measured, final poll 15:00:55Z)

Staged tree `.scratch/c06/staged-knowledge/` = full copy of `corpus/knowledge` + the three
landed fences under their declared names. Generator run read-only against the pinned README:

| landed fragment → staged file | sorts | insert after line | after row |
|---|---|---|---|
| `dialect-register-consistency.md` (C02) | after `conlang-methodology.md` | **161** | `conlang-methodology.md` |
| `taboo-strata-lifecycle.md` (C01) | after `syntax-typology.md` | **179** | `syntax-typology.md` |
| `translation-protocol-fidelity.md` (C03) | after `syntax-typology.md` | **179** (shared with C01) | `syntax-typology.md` |

The C01/C03 shared anchor 179 is the measured shared-anchor case: `translation-protocol-fidelity`
sorts after `taboo-strata-lifecycle` (`tab` < `tra`), so on apply it takes the larger
`merged_index` and lands second in the bottom-up pass — final row order `…syntax-typology`,
`taboo-strata-lifecycle`, `translation-protocol-fidelity`, `writing-systems` — filename order
preserved. The §5.3 synthetic rig reproduced exactly this case (adjacent pair on one anchor)
before it mattered.

**Fourth slot (C04, absent at cut):** K03's scout proposes
`sacred-registers-liturgical-language.md`, sorting between `register-strata-attestation.md` and
`semantic-fields-lexicon-building.md` (`reports/round-40/scout/K03-gaps.md:32`; X00 concurs,
`reports/round-40/cross/X00-connector.md:204-206`). K03 §5 routes the byte-consistency duty to
C01–C04 ("exact filenames are the executors' choice", `reports/round-40/scout/K03-gaps.md:175-177`),
and C03 independently recorded C04's in-flight topic as K03 §3-E4
(`reports/round-40/cov/C03-entry-3.md` §Disjointness). C03's declared name for itself
(`translation-protocol-fidelity.md`, its §Filename) already matches K03's proposal, and C02's
declared name matches K03's E2 proposal; C01 self-derived a different name for E1
(`taboo-strata-lifecycle.md` vs K03's `taboo-euphemism-lifecycle-stages.md`) — recorded, not
resolved: the landing name is whatever C01's fence declares and the integrator applies.

### 5.3 Acceptance of the generator itself (measured end-to-end this seat)

Synthetic tree `.scratch/c06/synth/` (copy of the live README + all 216 real entries + **4
probe linguistics entries** with multi-line `- topic:` heads, chosen to cover the hard cases:
`aaa-probe-first.md` first-in-section; `linguistic-anthropology-aaa.md` / `-bbb.md` an adjacent
pair sharing one anchor; `zzz-probe-tail.md` last-in-section; a redirected sweep copy
`.scratch/c06/sweep-synth.py` with only its `LANE` constant re-pointed, the r35/r39 C11/C06
method):

- generator on the **live** tree: 0 missing rows, totals/footer before == after — no-op (the
  reader is calibrated);
- generator on the synthetic tree: 4 rows emitted, anchors exactly `159 / 165 / 165 / 180` —
  first-in-section, shared-anchor pair, and tail all hit;
- `--apply` to a scratch copy → redirected sweep on the applied copy: **220 rows vs 220 files,
  0 missing, 0 ghosts, 0 topic mismatches, 0 header drift, totals_line 220 totals_ok True,
  footer total 220 / [25, 23, 25, 29, 24, 94] footer_ok True, exit 0**;
- negative controls, both observed on the applied copy: deleting one applied row → exit 1,
  `missing_from_index 1 ['linguistics/zzz-probe-tail.md']`; reverting the totals line to 216 →
  exit 1, `totals_line 216 totals_ok False`.

### 5.4 Full-target dry-run (the 21→25 arithmetic proven, not asserted)

With the three landed entries staged **plus one clearly-labeled CANDIDATE probe** in the fourth
slot under K03's proposed name (`sacred-registers-liturgical-language.md`, disposable probe
topic text — not C04's bytes), the generator reads the full target:

```
linguistics  declared 21 rows 21 live 25  header '## linguistics/ (21)' -> '## linguistics/ (25)'
   + dialect-register-consistency.md          insert after line 161  (after conlang-methodology.md) row_chars=499
   + sacred-registers-liturgical-language.md  insert after line 174  (after register-strata-attestation.md) row_chars=218  [CANDIDATE]
   + taboo-strata-lifecycle.md                insert after line 179  (after syntax-typology.md) row_chars=932
   + translation-protocol-fidelity.md         insert after line 179  (after syntax-typology.md) row_chars=1335
totals Total knowledge entries: 216. -> Total knowledge entries: 220.
footer (total 216 files; directory totals 21/23/25/29/24/94). -> (total 220 files; directory totals 25/23/25/29/24/94).
```

The candidate line exists only to prove the arithmetic; at apply time the generator re-emits
that row from C04's **landed bytes under the final name** — the candidate's bytes and name must
never reach the index (the r39 staging-name lesson:
`reports/round-39/cov/C06-delta-receipt.md:628-631`).

## 6. The rows, byte-pinned to the landed draft fences

The row bytes below are **derived from the landed draft fences** (the fence's own `- topic:`,
continuation-joined) at the fragment digests pinned here. They are a cross-check for the
integrator, not a substitute for the generator: the landing equality is whatever the landed
bytes say at apply time, and §8's post-apply sweep is what certifies it. All three landed
fragments declare their landing path explicitly (C01 `:3` "Proposed landing path", C02 same
mechanism, C03 header `:1` + §Filename). Full fragment sha256s, fence sha256s and row sha256s
measured this seat; rows listed in **index (filename) order**:

| fragment | sha256 (whole file) | fence sha256 | declared path | row sha256 (full row line) |
|---|---|---|---|---|
| `reports/round-40/cov/C02-entry-2.md` | `123d2a078753bc7667f06e9023e2ed79452b9b5e5f13fdbe9daf56dbafbca2c8` | `e0ea254391922addc4076ab6cf3bafc7c6321b9caaa97db99fff99965230dd37` | `linguistics/dialect-register-consistency.md` | `fb82477b60cc067b22cbfc121acdb5d2a058458045e1d23cbb86a63c2bab13b8` |
| `reports/round-40/cov/C01-entry-1.md` | `ff3e004cdb797506779ac92cc43c2d44f52170bb15b1e4f9ec28257abf7ed4f6` | `4b48d6fe1d5289290d2358cbbd36e18aeae39b579a6f990302b1229f3073298c` | `linguistics/taboo-strata-lifecycle.md` | `039cbcad013f65624a4e9e808903c84a958e2fe95ede3d297bd253d452318612` |
| `reports/round-40/cov/C03-entry-3.md` | `fa7df06a1a5db1161f2dd89ff947cc91eb59261cb55a31789fc31e667120ceee` | `1962fa5d947224c2bc3a5bd8a0ef555b9fc22e1736b44d122e778bd7a5a5b0f9` | `linguistics/translation-protocol-fidelity.md` | `7760a2065edaf612f8234f39a7e173beed1a36374b199c5d6bbc4619736fcc1c` |
| `reports/round-40/cov/C04-entry-4.md` | **absent at 15:00:55Z** | — | candidate `linguistics/sacred-registers-liturgical-language.md` (K03 §2 `:34`) | **owed** (§Owed) |

**Filename/allocation state:** X00 closed the seat→topic mapping C01→E1 (taboo lifecycle),
C02→E2 (dialect/register), C03→E3 (translation fidelity), C04→E4 (sacred registers; K03 §3-E4)
(`reports/round-40/cross/X00-connector.md:45-54`, §C2; C03's own disjointness note names the
same four). Four distinct topics per K03 §3's scopes; no filename collision against the 21
existing entries (K03 §2 `:25-34`; re-verifiable with one `ls` at apply). K03 §5's
routed-not-absorbed note (`reports/round-40/scout/K03-gaps.md:172-174`) is repeated for the
integrator: landing these linguistics entries does **not** discharge r39's G2/G3/G4
verification-gate gaps.

**The three derived rows (from the pinned draft fences, index order):**

```
- `dialect-register-consistency.md` — how lects form and drift inside one language — founder effects and migration trajectories, the koineization process model (mixing, leveling, simplification, reallocation, focusing) with its focusing deadline reconciled, focal/relic/transition area mechanics, and anti-language formation (anti-society conditions, overlexicalization zones, renewal, second-life trajectories) — the reference mechanics a built dialect map's internal consistency is checked against
```

```
- `taboo-strata-lifecycle.md` — the lexical-diachronic lifecycle of a forbidden word as a **form-history**: the inventory of form-building operations a taboo substitution can be minted with (mincing, compound circumlocution and its univerbation, semantic shift, borrowing, graphic substitution, reading substitution, understatement, clipping/initialism); the word-level lifecycle states (plain → charged → substituted → fossil or live rung → replaced or reanalyzed) as a branching state graph, never a universal ladder; and the **read-off** — the procedure for ordering the strata a taboo deposits in a lexicon against each other and against the language's other dated strata, using four bracketing tests (sound-law bracketing, loan bracketing, legal/orthographic bracketing, semantic-chain bracketing), the false-fossil exclusion checklist, and negative strata. Method and lane policy only; canon decisions belong to lore-shokunin.
```

```
- `translation-protocol-fidelity.md` — The linguistics of **glossing and translation commentary as cultural practice**, and the fidelity criteria a built packet's translation apparatus is audited against. Supplies: the three objects a reader of a rendered text meets (the lexicographic gloss, the apparatus translation note, the equivalence claim) and why they must not be merged; the anatomy of a translation note (its provenance type, its skeleton fields, its anchor, its one dominant job); the assert/license split — what a gloss states, what it licenses a reader to infer, and the laundering classes that collapse the two; thick translation (Appiah) as the reference frame and paratext layers (Genette) as the carriers — preface, glossary, footnote, interlinear, tooltip; domestication vs foreignization (Venuti) as a declared design axis rather than a fidelity binary; the interpreter/mediator as a register office and power class; and the ten fidelity criteria (note-presence, context-field completeness, assertion licensing, translation-vs-original separation, apparatus attribution, mediation recording, era-of-rendering, register equivalence, name-first conformance, skip-test survival) that a fidelity check reads against the packet's own declared protocol. Reference and method only; canon decisions belong to lore-shokunin.
```

(Each row was extracted programmatically from its fragment's fence with the sweep's own topic
rule, TOPIC_RE continuation-joined, and byte-checked via the generator's staged dry-run; the §6
table pins the digests. The fourth row is C04's fence under its final name — emitted
mechanically at apply, never drafted here.)

## 7. Drafted revision 2.3 block (fill ⟨…⟩ at integration time)

```
revision: 2.3 — Round-40 linguistics-partition expansion landing (2026-10-19): the four
round-40 entries landed — `⟨n1⟩.md`, `⟨n2⟩.md`, `⟨n3⟩.md`, `⟨n4⟩.md` (K01-r39's routed gaps
G2–G4 plus K03's fourth) — each naming the gap it fills, with the author fragments under
`reports/round-40/cov/`, the gap scout at `reports/round-40/scout/K03-gaps.md`, and the audit
under `reports/round-40/cov/C05-audit.md`. `## linguistics/` moved 21 → **25**; its four rows
were added in filename order with each entry's own `- topic:` text byte-equal; the totals line
and the counts footer moved 216 → **220** and the footer vector 21/23/25/29/24/94 →
**25/23/25/29/24/94**. Re-measured with `python3 reports/round-28/readme/sweep.py`: ⟨rows 220
vs 220 files, 0 missing, 0 ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches,
totals line 220, footer 220 / 25/23/25/29/24/94, exit 0 — measured at close⟩. Non-canon
examples and passing structural gates do not certify historical truth.
```

⟨…⟩ slots: the four filenames **in filename order** (three known: `dialect-register-consistency.md`,
`taboo-strata-lifecycle.md`, `translation-protocol-fidelity.md`; ⟨n2⟩ is C04's final name —
under K03's candidate it sorts second), and the sweep reading measured **after** the entries +
README land. Do not write this block with a predicted reading — the round-28 defect was exactly
a present-tense claim that was never re-measured (`corpus/README.md:52-61`, reason statement;
P01 `reports/round-40/plan/P01-plan.md:62-63` gate: "delta's numbers re-derived from the
actual draft filenames, not asserted").

## 8. Receipt — after-state assertion block and its negative control

### 8.1 The block (read-only; runs from the lane root; `PIN` is §2.3's tree object)

```python
python3 - <<'PY'
import pathlib, re, subprocess, json
PARTS=['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']
TARGET={'linguistics':25,'myth-symbol':23,'culture-material':25,'synthesis':29,'verification':24,'civilizations':94}
PIN='608ef479d23051d6b4211bc40e52ccb7ffeaf4b2'
fails=[]
def chk(leg, ok, detail):
    print(('PASS ' if ok else 'FAIL ')+leg+' :: '+detail)
    if not ok: fails.append(leg)
live={p:len(sorted(pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))) for p in PARTS}
chk('A1_census_counts', live==TARGET, f'live {live} target {TARGET}')
out=subprocess.run(['python3','-B','tools/source-audit-inventory.py','--json','--summary','--root','corpus/knowledge'],capture_output=True,text=True)
inv=json.loads(out.stdout)
chk('A2_inventory_total', inv['totals']['files']==220, f"totals.files {inv['totals']['files']} target 220 (exit {out.returncode})")
rd=pathlib.Path('corpus/README.md').read_text()
hdr={m.group(1):int(m.group(2)) for m in re.finditer(r'^## (linguistics|myth-symbol|culture-material|synthesis|verification|civilizations)/ \((\d+)\)$', rd, re.M)}
chk('A3_readme_headers', hdr==TARGET, f'headers {hdr}')
tot=[l for l in rd.splitlines() if l.startswith('Total knowledge entries')][0]
chk('A4_readme_total', tot=='Total knowledge entries: 220.', tot)
footline=[l for l in rd.splitlines() if re.match(r'^\(total \d+ files; directory totals ', l)]
chk('A5_readme_footer', any('(total 220 files; directory totals 25/23/25/29/24/94)' in l for l in footline), f'footer now: {footline[0] if footline else "absent"}')
rows={}
for p in PARTS:
    m=re.search(r'^## '+re.escape(p)+r'/ \(\d+\)\n(.*?)(?=^## )', rd, re.M|re.S)
    rows[p]=len(re.findall(r'^- `[^`]+\.md` — ', m.group(1), re.M))
chk('A6_rows_eq_files', rows==live, f'rows {rows} == files {live}')
pinned=set('corpus/knowledge/'+l for l in subprocess.run(['git','ls-tree','-r','--name-only',PIN],capture_output=True,text=True).stdout.split('\n') if l)
liveset=set(f'corpus/knowledge/{p}/{f.name}' for p in PARTS for f in pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))
new=sorted(liveset-pinned); gone=sorted(pinned-liveset)
chk('A7_delta_4_files', len(new)==4 and not gone and all('/linguistics/' in n for n in new), f'new {len(new)} removed {len(gone)}')
for n in new: print('  + '+n)
print('VERDICT', 'GREEN' if not fails else 'RED legs '+str(fails))
PY
```

**Negative control — observed at the before state (this seat's run, 2026-10-19, ~14:3x–14:4xZ):**

```
FAIL A1_census_counts :: live {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94} target {'linguistics': 25, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
FAIL A2_inventory_total :: totals.files 216 target 220 (exit 0)
FAIL A3_readme_headers :: headers {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
FAIL A4_readme_total :: Total knowledge entries: 216.
FAIL A5_readme_footer :: footer now: (total 216 files; directory totals 21/23/25/29/24/94).
PASS A6_rows_eq_files :: rows {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94} == files {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
FAIL A7_delta_4_files :: new 0 removed 0
VERDICT RED legs ['A1_census_counts', 'A2_inventory_total', 'A3_readme_headers', 'A4_readme_total', 'A5_readme_footer', 'A7_delta_4_files']
```

Readings: (a) every after-leg **fails at the before state**, so a later GREEN is informative,
not green-by-construction; (b) A6 is an equality *invariant* — green now, required to stay
green after; (c) A7 read `new 0 / removed 0`, the positive proof that the §2.3 pin matches the
live tree. The block shells out only to `git ls-tree` and the read-only inventory tool; it
writes nothing. It counts rows — it does **not** compare row text with `- topic:` bytes; that
verbatim leg is §1's sweep and §5.3's applied-copy reading, and a count-only green must never
be quoted as index-text reconciliation (the r19 lesson, `corpus/README.md:95-101`).

### 8.2 The integrator's acceptance sequence (claim C thresholds, `reports/round-40/claims.json:18`)

1. C05's audit over all four drafts lands, clean or defect-listed (audit leg — C05/R01's
   evidence; absent at this seat's cut). X00's chain is C05 → C06's final filename set → apply
   (`reports/round-40/cross/X00-connector.md:124-136`).
2. Apply the four entries (C04's under its declared final name; the §5.4 candidate probe never
   lands), then E1–E5 + the four generated rows in one motion.
3. `python3 -B reports/round-28/readme/sweep.py` → **must** read `rows 220 files 220`,
   `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`,
   `totals_line 220 totals_ok True`, footer `{total 220, dir_totals [25, 23, 25, 29, 24, 94]}`,
   `footer_ok True`, exit 0. `ls corpus/knowledge/linguistics/*.md | wc -l` → **25**.
4. Diff the landed README against this draft before trusting the sweep (the r35 apply left
   placeholder lines the sweep then caught; the r36 staged prediction diverged from the
   delivered digest — r39 X00-3's reason, inherited).
5. Re-run §8.1's block → VERDICT GREEN; fill §7's ⟨…⟩ and write E5 with the landing sha.
6. Inventory cross-check: `python3 -B tools/source-audit-inventory.py --json --summary --root
   corpus/knowledge` → `totals.files 220`.

Until step 3/5 read green on the landed tree, **no after-count in this fragment may be quoted
as measured** — every after value here is target or generated, never landed.

## 9. Limits and cross-fragment consistency

- All before figures are point-in-time at `fd55e1f` with a byte-clean corpus tree; any landing
  invalidates §2 until re-measured (the §2.3 pins make the before state recoverable from git
  alone). The three §6 row bytes are draft-derived: if an executor fragment is amended before
  landing, the pinned fence digests detect it and the generator re-emits the row mechanically.
- This receipt certifies **counts and their reconciliation** — never entry quality, source
  resolvability, or canon status (`corpus/README.md:523`; the audit is C05's, the adversarial
  fabrication hunt is R01's, the admission verdict is the integrator's per
  `REGIMEN.md:41-43`).
- The census command globs only `*.md` at each partition's top level; the inventory and
  `find -type f` legs are the wider nets and agree at 216 (nesting case closed at the r35
  baseline by that round's receipt measurement, re-derivable with the same two commands).
- No `reports/round-*/run-validation.py` was executed anywhere by this seat (absolute rule,
  `reports/round-40/targets.json:8`). The round's close-time runner is the integrator's
  artifact; `REGIMEN.md:57`'s exit-0-at-close requirement stands regardless of this fragment.
- Cross-fragment readings, no divergence found: K03 §2's sort table matches the generator's
  measured anchors for all four names (`reports/round-40/scout/K03-gaps.md:29-34` vs §5.2/§5.4:
  dialect after conlang-methodology, sacred-registers after register-strata-attestation,
  taboo/translation pair before writing-systems — K03's E1 name differs, same slot); P01 §1.5's
  C06 obligations (revision block above rev 2.2, header 21→25, totals 216→220, vector first
  slot, 4 rows filename order, coverage receipt) are all carried (`reports/round-40/plan/
  P01-plan.md:58-63`); X00's C1/C2 constraints and chain are adopted (§5 rule, §8.2 step 1).
  Known name divergence, recorded: C01's `taboo-strata-lifecycle.md` vs K03's proposed
  `taboo-euphemism-lifecycle-stages.md` — both sort into the same slot (after
  `syntax-typology.md`); the landing name is C01's declared one per K03 §5
  (`reports/round-40/scout/K03-gaps.md:175-177`). No peer fragment proposes a different
  count-line, vector order, or row rule.

## Addendum — fragment-landing timeline (this seat's polls, all 2026-10-19)

- ≤14:07Z (first listing): `reports/round-40/` held claims.json, targets.json,
  telemetry/dispatch-declared.json, plan/P01-plan.md, adj/A01-audit.md, calib/Ca03-receipt.md,
  cross/X01-trades.md, scribe/S02-telemetry-draft.md — no cov/, no scout/.
- ~14:14Z poll: `scout/K01-touched-census.md`, `scout/K03-gaps.md`, `cov/C01-entry-1.md` landed.
- 14:48:19Z poll: cov/ = C01 only (C02/C03 not yet).
- 14:51:32Z poll: cov/ = C01, C02, C03; cross/ gained X00-connector.md.
- 14:53:37Z / 14:54:58Z / 15:00:55Z polls: **C04 still absent** — folded state: 3 of 4 rows
  byte-known (§6), fourth slot carried as §5.4's candidate probe + §Owed.
- All §1–§8 measurements predate or ignore the landing-boundary state; the §2.3 pins keep the
  before state recoverable from git alone regardless of what lands later.

## Owed

- `reports/round-40/cov/C04-entry-4.md` — the fourth executor fragment, absent at the
  15:00:55Z poll. Its landed fence supplies the fourth row's bytes and final filename
  (candidate: `sacred-registers-liturgical-language.md`, K03 §2 `:34`, anchor after line 174 /
  `register-strata-attestation.md` — re-derived mechanically at apply, §5.4). P01's fallback
  path (`reports/round-40/plan/P01-plan.md:48-53`) governs if C04 never lands: the claim
  reports 3/4 honestly rather than forcing a pass.
- `reports/round-40/cov/C05-audit.md` — the audit leg of claim C's threshold ("entries audited
  pre-landing" / "audit 4/4 PASS", `reports/round-40/claims.json:16,18`); absent at this seat's
  cut. Apply gate: entries land only after C05 is clean or its defects are filed (X00 chain).
- The integrator's application of §4/§5/§7 to `corpus/README.md` + the four entries, then the
  §8.2 sequence (post-apply sweep + GREEN §8.1 + diff-vs-draft). Nothing is landed until then.
- `reports/round-40/run-validation.py` — required by `REGIMEN.md:57` at close; integrator-
  authored, isolated-copy execution only (the r39 isolation-replay protocol; never in-tree).

## Citations

- `reports/round-40/claims.json:7` (baseline `fd55e1f`), `:9` (axes), `:13-18` (claim C: `:15`
  before, `:16` after_required, `:17` counting commands, `:18` thresholds), `:32-33` (non_goals)
- `reports/round-40/targets.json:4-9` (shared rules), `:83-88` (seat C06)
- `REGIMEN.md:27-30` (per-round contract), `:41-43` (admit rule), `:57` (close-time runner)
- `reports/round-40/plan/P01-plan.md:14-19` (baseline census), `:58-63` (this seat's step 5 +
  gate), `:67-70` (integration step 7), `:154-156` (collision control)
- `reports/round-40/scout/K03-gaps.md:5-21` (baseline + routing fact), `:25-34` (collision
  table + sort positions), `:66-153` (E1–E4 scopes + sources), `:172-177` (routed-not-absorbed;
  filename ownership)
- `reports/round-40/cross/X00-connector.md:20-21` (surface ownership), `:29`,
  `:36-38` (C1 constraints on this delta), `:45-54` (seat→topic mapping), `:124-136`
  (chain + apply + sweep green), `:204-206` (census + sort confirmation)
- Landed executor fragments (digests in §6): `reports/round-40/cov/C01-entry-1.md` (`:3`
  proposed landing path `taboo-strata-lifecycle.md` + sort note), `C02-entry-2.md` (declared
  `dialect-register-consistency.md`), `C03-entry-3.md` (`:1`, `:13`, `:14` filename +
  disjointness)
- `corpus/README.md` pinned bytes: `:1,3` (duplicated H1), `:5-12` (rev 2.2), `:14,16`
  (duplicated rev-2.0 line), `:158` (`## linguistics/ (21)`), `:160-180` (21 rows), `:182`,
  `:391`, `:518` (totals), `:520-523` (counts footer block), `:524-531` (superseded paragraph,
  ends at rev 2.0), `:533-549` (dated index paragraphs; 549 last). Read at sha256
  `e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a` (549 lines / 132,721 bytes)
- `reports/round-28/readme/sweep.py:28-30` (read-only docstring), `:46-47` (LANE/README/
  KNOWLEDGE constants), `:76,257,284,397,421` (the only `open()` sites — writes confined to
  selftest synthetic trees); instrument sha256
  `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`; row contract pinned by
  r39 C06 (`reports/round-39/cov/C06-delta-receipt.md:30-38,237-377,394-414`)
- Filed precedent: `reports/round-35/cov/C11-readme-delta.md` (generator ancestor, apply-order
  bugs `:191-199`), `reports/round-37/op/defect-queue.json:242-251`
  (`readme-prediction-vs-delivery`), `:103-131` (R36 README carried defects), `SCORECARD.md:681-684`
  (r35 placeholder root cause)
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  HEAD `fd55e1f`): `git rev-parse HEAD`; `git status --porcelain`; `git rev-parse
  HEAD:corpus/knowledge`; `git ls-tree -r --name-only 608ef479… | sort | sha256sum`; `find
  corpus/knowledge -name '*.md' -type f | sort | sed 's|^corpus/knowledge/||' | sha256sum`;
  `sha256sum corpus/README.md reports/round-28/readme/sweep.py`; `wc -lc corpus/README.md`;
  `grep -n '^## \|Total knowledge entries\|^Counts checked\|^(total '` corpus/README.md; the
  `claims.json:17` census loop + linguistics-only count + `find | wc -l` (§2.1); `python3 -B
  tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → totals.files 216
  (exit 0); `python3 -B reports/round-28/readme/sweep.py` → green 216/216 exit 0;
  `--selftest` → 12/12; generator no-op on the live tree; synthetic +4-probe rig: anchors
  159/165/165/180, `--apply` + redirected sweep 220/220 exit 0, negative controls exit 1
  (`missing_from_index 1`; `totals_ok False`); staged dry-runs (3 landed entries → anchors
  161/179/179, totals 216→219; +CANDIDATE probe → anchors 161/174/179/179, totals 216→220,
  footer 25/23/25/29/24/94); fence/row digest extraction (§6 values); the §8.1 A-block (RED,
  §8.1 output); `ls` polls of `reports/round-40/**` (Addendum timestamps)
- Scratch (disposable, not evidence): `.scratch/c06/readme-delta.py` (source = r39 §5.1,
  3-line diff), `.scratch/c06/synth/**`, `.scratch/c06/sweep-synth.py`,
  `.scratch/c06/staged-knowledge/`, `.scratch/c06/row-*.txt`
