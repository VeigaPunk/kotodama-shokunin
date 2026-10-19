- Seat: K02 | scout | claim C | date 2026-10-19 | baseline 4a7aede

# K02 — Entry-audit scout: the instruments, the checker command, the defect classes, the README reconciliation pattern

**Role limits.** Read-only scout. My only write is this file (plus disposable
`.scratch`). I executed **no** `reports/round-*/run-validation.py` (F-C13-1) and
no tool with a write path into the lane. I admit no entry, certify no round, and
absorb no sibling fragment's evidence. Every figure below was re-measured at
HEAD `4a7aede` (`git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`)
in the window 2026-10-19T08:14Z–08:20Z; `git status --porcelain` showed only
`?? reports/round-35/`, so every live number is a baseline number.
`reports/round-35/run-validation.py` does **not** exist yet
(`ls: cannot access 'reports/round-35/run-validation.py'`) — claim C's third
counting command lands mid-round from another seat; do not treat its absence as
a C failure.

## 1. The instruments a round-35 entry audit can stand on

| # | instrument | path | kind | sha256[:16] | reads | exit |
|---|---|---|---|---|---|---|
| A | per-entry QUALITY bar + `couples:` resolution | `reports/round-19/audit/entry-audit.py` | read-only checker, `--selftest` | `e7992c325a479aa7` | corpus entries | 0 all clear; 2 any fail |
| B | README index + counts-footer sweep | `reports/round-28/readme/sweep.py` | read-only checker, `--selftest` | `9b2ccac0046831fd` | `corpus/README.md` + tree | 0 clean; 1 findings |
| C | uncertainty-marker inventory (claim C's declared counter) | `tools/source-audit-inventory.py` | read-only counter | `f617bb99318f501d` | corpus tree | 0; 2 could-not-evaluate |
| D | the **filed** runner's per-entry legs (precedent — cited, never executed) | `reports/round-10/run-validation.py:349-377` | filed code | `23d6dc09002fe18c` | entries + README | — |

A and B were executed by this seat at HEAD; neither has a write path inside the
lane — A's only `open(..., "w")` calls are inside its `tempfile` selftest
fixtures (`entry-audit.py:165,167,178`) and B's are inside its `tempfile`
selftest trees (`sweep.py:257,397`); B's live leg opens `corpus/README.md` and
the tree read-only (`sweep.py:76,284`). Readings:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-19/audit/entry-audit.py --selftest   # 7 PASS, exit 0
python3 -B reports/round-28/readme/sweep.py --selftest        # selftest: 12/12 checks passed, exit 0
```

## 2. The frontmatter checker command

### 2.1 The filed bar — round-10's `entry_checks()` (the strongest checker in-tree)

`reports/round-10/run-validation.py:81-82`:

```python
C_FRONTMATTER_FIELDS = ("topic", "sources", "verified-at", "recheck", "couples")
```

and its four legs, `:349-377`:

- **frontmatter** — each of the five fields must match
  `(?m)^\s*[-*]?\s*<field>\s*:\s*(\S.*)$` **anywhere in the file** (not
  head-block-scoped), else it is appended to `missing_frontmatter` (`:354-360`).
- **gap** — a `gap` field/clause `(?i)(?:^|[\s.;—–|-])gap(?:[\s-]+(?:filled|addressed|served))?\s*:\s*(\S[^\n]{0,300})`
  **or** a `##`–`####` heading containing `gap` followed by a non-empty line
  (`:361-367`). This accepts the live `- gap: …` head-field form.
- **decision record** — `(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*\n+\s*(\S[^\n]*)`
  (`:368-370`): a heading naming "decision record", followed by a non-empty line.
- **retrievable locator** — at least one repo path matching
  `REPO_PATH_RE` (`:111-112`, `corpus|tools|reports|examples/…​.(md|json|py|yml|yaml|tsv|txt)`)
  that **exists on disk**, or a URL (`:371-376`).
- **README legs** — `readme_index()` (`:380-399`) parses `## <part>/ (N)`
  headers, `- \`<file>.md\`` rows per section, and `^Total knowledge entries: (\d+)\.`
  — the three README surfaces a round-35 delta must move.

**Do not execute it.** The file writes `reports/round-10/validation.json`; it is
cited here as the declared bar, read at filed bytes only.

### 2.2 The instrument I ran, and its measured false-negative surface

`entry-audit.py` (A) is the *round-19 cohort's* bar, and it reads **0/5** on live
committed exemplar entries from the two partitions claim C touches:

```sh
python3 -B reports/round-19/audit/entry-audit.py \
  corpus/knowledge/culture-material/transport-mobility-lexicon.md \
  corpus/knowledge/myth-symbol/plant-symbolism.md \
  corpus/knowledge/culture-material/material-culture-inference-method.md \
  corpus/knowledge/myth-symbol/animal-symbolism.md \
  corpus/knowledge/verification/label-channel-routing-verification.md
# TOTAL 0/5 clear the bar   exit=2
```

| entry | src locators | couples unresolved | gap_named | decision | bar |
|---|---|---|---|---|---|
| `culture-material/transport-mobility-lexicon.md` | 13/14 | 0 | **False** | True | False |
| `myth-symbol/plant-symbolism.md` | **0/0** | 0 | True | True | False |
| `culture-material/material-culture-inference-method.md` | 10/10 | 0 | **False** | **False** | False |
| `myth-symbol/animal-symbolism.md` | 10/11 | 0 | **False** | **False** | False |
| `verification/label-channel-routing-verification.md` | 7/7 | **1** | True | True | False |

Three distinct false-negative mechanisms, all reproducible:

1. **`gap_named` misses the live `- gap:` head field.** A's `GAP_RE`
   (`entry-audit.py:26`) lists `residual gap|gap filled|the gap this entry fills|known gaps|missing from|no entry (covers|states)|not covered by`;
   the live wording is `- gap: … — this entry fills it` (`transport-mobility-lexicon.md:3`,
   `plant-symbolism.md:3`) — a different word order, so it does not fire. Round-10's
   leg **does** accept this form. Corpus-wide A reads `gap_named` on only **27/201**
   files.
2. **`source_bullets` counts only `  - ` sub-bullets.** `plant-symbolism.md`
   carries its sources as one long single-line `- sources:` value → `0/0`, so the
   `n_src >= 1` conjunct can never pass. **113/201** corpus files read
   `source_bullets == 0` for the same reason.
3. **`decision_record` misses headings the round-10 regex also misses** —
   `material-culture-inference-method.md` and `animal-symbolism.md` carry no
   `decision record` heading at all (`grep -nE "^#{2,4}.*([Dd]ecision|DR-[A-Z]{2}-)"`
   → no hits), so this one is a *true* negative: the two entries predate the
   round-10 decision-record convention. Corpus-wide A reads `decision_record`
   on **38/201**; the stricter heading census `^#{2,4}.*[Dd]ecision[- ]?[Rr]ecord.*`
   matches **22/201 files** (heading classes measured: `## 10. Decision record` ×2,
   `## 9. Decision record (author)`, `## 9. Decision record`,
   `## 8. Decision record — …` ×2 plus `## 8. Decision record: …` ×1, and six
   distinct `## 6. Decision record — …` headings).

**Consequence for round 35:** the entry-audit bar must be stated as *the
round-10 legs applied to the ten new entries*, or as a **widened** A — not as
"`entry-audit.py` says PASS", which is red-by-construction on this corpus
(corpus-wide `quality_bar` **15/201**). This is the same class as round-10's
finding **F1** (`reports/round-10/coverage/audit-myth-culture.md` §1.7/§5:
entries that name their gaps and cite sources "in prose forms the runner's
regexes do not accept" — fix entry-side or runner-side, never silently green).

### 2.3 Head-field census at HEAD — the "4/4 or documented 3/4" reading

Claim C's `after_required` names the four fields
`source / verified-at / recheck / scope`. Measured over 201 files (opening block
= text before the first `## `; anchored `^-\s*<field>\s*:`):

| field | corpus | linguistics | myth-symbol | culture-material | synthesis | verification | civilizations |
|---|---|---|---|---|---|---|---|
| `topic` | 201/201 | 21 | 19 | 18 | 29 | 20 | 94 |
| `sources` | 201/201 | 21 | 19 | 18 | 29 | 20 | 94 |
| `couples` | 201/201 | 21 | 19 | 18 | 29 | 20 | 94 |
| `verified-at` | 198/201 | 21 | 19 | 18 | 29 | **17** | 94 |
| `recheck` | 198/201 | 21 | 19 | 18 | 29 | **17** | 94 |
| `source` (singular) | 131/201 | 3 | 19 | **0** | 29 | 5 | 75 |
| `scope` | **0/201** | 0 | 0 | 0 | 0 | 0 | 0 |
| `gap` | 2/201 | 0 | 1 | 1 | 0 | 0 | 0 |
| `status` | 0/201 | 0 | 0 | 0 | 0 | 0 | 0 |

Three readings follow, and **P01/C12 must pin which one is the round's bar** —
the claim's literal list is not attainable as four head fields:

- **`- scope:` is not a field in this corpus (0/201).** "Scope-bearing" is a
  *property of the `verified-at` line* (round-10 review criterion:
  "`verified-at` dated and scope-bearing" —
  `reports/round-10/coverage/review-C04.md:19`). A literal 4/4
  (`source`+`verified-at`+`recheck`+`scope`) is therefore unreachable and must
  not be used as the gate.
- **The measurable tail trio** `source|sources` + `verified-at` + `recheck` is
  198/201; the three exceptions are exactly the round-9/10 **documented class**:
  `verification/citation-format-and-source-registry.md`,
  `verification/myth-consistency-gate.md`,
  `verification/provenance-audit-ledger-format.md` — the same three files round-10
  recorded as the B-remainder (3/179), unchanged at 201. That is the "documented
  3/4 class" precedent, and it is a *pre-existing carried* class, not a new defect.
- **The singular `source:` leg must not be required of culture-material.** The
  partition reads **0/18** on it (round-10 class A: culture-material A 0/18,
  `audit-myth-culture.md` §1.5); its established form is plural `sources:` only.
  Requiring singular `source:` would fail all six new culture-material entries at
  birth. myth-symbol reads 19/19 on the singular leg — the two target partitions
  differ here, and the audit must say which leg it applied to which partition.

The house profile the round-10 cohort actually adopted is the five fields
`topic / sources / couples / verified-at / recheck` (201/201 on the first three,
198/201 on the tail pair) plus a `- gap:` head field naming the gap
(`transport-mobility-lexicon.md:3`, `plant-symbolism.md:3` are the two live
exemplars; 2/201 corpus-wide).

## 3. Per-entry defect classes (consolidated, with precedent and live status)

| id | class | how it is detected | precedent | live status at HEAD |
|---|---|---|---|---|
| D1 | **phantom `couples:` target** — a path that resolves nowhere (wrong partition + wrong filename) | A's `couples_unresolved` leg (brace-aware, three bases: entry dir, lane root, `corpus/knowledge/`) | `reports/round-19/audit/x26-spotcheck-entries.md` §3 X26-1 | **still live**: `verification/label-channel-routing-verification.md` still lists `../linguistics/phonology-sanity.md` → 1 unresolved (re-measured) |
| D2 | **README row is a condensed paraphrase**, not the entry's own `- topic:` text | B's `topic_mismatch` leg (`REWRITE` class), byte-equal compare after space-joining continuations | `reports/round-20/readme/reconcile.md` §3 (10 rows, wrong from birth — composed ~30 s after the topics were final) | clean at HEAD (0 mismatches); the class is the reason B exists |
| D3 | **stale present-tense counts footer** — a dated claim whose numbers no longer match the tree | B's `FOOTER_TOTAL` / `FOOTER_DIR_TOTALS` / `FOOTER_ABSENT` legs | `corpus/README.md` revision 1.8 block; `reports/round-28/readme/sweep.py` docstring (round-27's sweep went green because it never read the footer) | clean at HEAD (`footer_ok True`) |
| D4 | **gap/source prose form the checker's regex does not accept** | run the bar, then read the file: a red leg with the substance present is D4, not a content defect | round-10 **F1** (`audit-myth-culture.md` §1.7, §5) | **live on 2 exemplars** (§2.2 items 1–2); 27/201 `gap_named`, 113/201 `source_bullets==0` under A |
| D5 | **entry asserts a surface fact the same round moved** (stale boundary claim) | re-read the entry's own `recheck:` line and compare against the live tool surface | `x26-spotcheck-entries.md` §3 X26-2 (the "seven-name constant" claim vs the nine-gate battery) | not re-measured here (out of claim C scope); named so C13/C14/C17 do not re-file it as new |
| D6 | **missing frontmatter tail** (`verified-at`/`recheck`) | §2.3 census | `audit-myth-culture.md` §1.5, §2.4 (B 3/179, same three files) | exactly 3 files, same three, unchanged |
| D7 | **filed-runner citation decay** — an audit cites runner lines that no longer exist | `wc -l` the cited runner | `reports/round-19/audit-1.md:25,70` and `audit-2.md:104` cite `reports/round-19/run-validation.py:443-455` / `:835-873`; the filed runner is **24 lines** (1868 bytes, `sha256 5b27a80de1f4b110…`) — the citations do not resolve | live; affects round-19 provenance only |
| D8 | **instrument false-negative over the pre-existing cohort** (the meta-class of D4) | run the instrument corpus-wide and compare against a known-good exemplar | this fragment §2.2 | `quality_bar` 15/201, `gap_named` 27/201 |

D1–D4 and D8 are the classes a round-35 auditor will actually hit. D2/D3 are
README-side; D1/D4/D6/D8 are entry-side; D5/D7 are provenance-side.

## 4. The README reconciliation pattern

### 4.1 The convention (measured, not assumed)

Derived in round 10 (`reports/round-10/coverage/index-update.md:52`), enforced
since, and encoded in B:

- every index row is ``- `name.md` — <topic>`` where `<topic>` is the entry's own
  `- topic:` head-block text with continuation lines **space-joined**;
- rows sit inside their partition's `## <part>/ (N)` section, ordered by filename;
- `N` in the header equals the live file count;
- `Total knowledge entries: N.` equals the corpus file total;
- the counts footer is a **dated present-tense claim carrying its own command**;
- a reconciliation adds a **new `revision:` block at the top** (currently
  `revision: 1.9 — Round-28 …`, `corpus/README.md:3`); superseded readings are
  preserved below as dated records, never edited (`revision: 1.8` block,
  `corpus/README.md:17-33`, does exactly this for the 199/19 footer defect).

### 4.2 Round-35 delta arithmetic (exact anchors at HEAD)

| surface | path:line | now | after +6 culture-material / +4 myth-symbol |
|---|---|---|---|
| new revision block | `corpus/README.md:3` (1.9 block above it) | `revision: 1.9` | new block above, e.g. `revision: 1.10 — Round-35 …` |
| myth-symbol header | `corpus/README.md:147` | `## myth-symbol/ (19)` | `## myth-symbol/ (23)` |
| culture-material header | `corpus/README.md:169` | `## culture-material/ (18)` | `## culture-material/ (24)` |
| index rows | inside each section | 201 rows | 211 rows (10 added in filename order, topics byte-equal) |
| totals line | `corpus/README.md:469` | `Total knowledge entries: 201.` | `Total knowledge entries: 211.` |
| footer total | `corpus/README.md:473` | `(total 201 files; …)` | `(total 211 files; …)` |
| footer vector | `corpus/README.md:473` | `21/19/18/29/20/94` | `21/23/24/29/20/94` |
| footer date | `corpus/README.md:471` | `Counts checked 2026-10-18` | re-dated at the round-35 measurement |
| index re-measure line | `corpus/README.md:482,486,490` | three dated sweeps | add a fourth dated line naming the instrument |

Section order is fixed: `linguistics, myth-symbol, culture-material, synthesis,
verification, civilizations` (`reports/round-28/readme/sweep.py:50-57`) — the
footer vector is compared **in that order**, so a reordered vector reds even when
the total matches (`FOOTER_DIR_TOTALS` control).

### 4.3 What B measures, and what it does not

B's legs: rows/files, missing, ghosts, duplicate rows, topic byte-equality
(`REWRITE` / `NO_TOPIC_FIELD`), section-header drift, totals line, and the footer
(total + vector + absence). **B has no row-order leg**: an index whose rows are
sorted wrongly still reads green. Row order is convention-only
(`index-update.md:52`); if the round wants it enforced, that is a new control for
a new instrument, stated as such rather than assumed.

Live reading of B at HEAD (`python3 -B reports/round-28/readme/sweep.py`):

```
parts {"civilizations": 94, "culture-material": 18, "linguistics": 21,
       "myth-symbol": 19, "synthesis": 29, "verification": 20}
rows 201 files 201
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 201 totals_ok True
footer {"date": "2026-10-18", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge",
        "total": 201, "dir_totals": [21, 19, 18, 29, 20, 94]}
footer_findings [] footer_ok True
readme_sha256 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c
exit 0
```

**The README is exactly reconciled before the +10 landing** — so any red after
the landing is the landing's, not carried debt.

### 4.4 Counts, command-carried (two independent methods)

```sh
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
# 21 19 18 29 20 94        (total 201 via find corpus/knowledge -name '*.md' | wc -l)
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals: files 201, files_with_any_mark 147, files_with_marker 135, lines 36395,
#         raw_lines 717, raw_occurrences 731, ci_occurrences 733,
#         marker_occurrences 655, bare 621, detailed 34, marker_lines 650,
#         unparenthesized 78   (exit 0)
```

Both agree, and both match claim C's declared `before` (201; 21/19/18/29/20/94).

**Cross-check (independent seat):** `reports/round-35/scout/K01-coverage-census.md`
landed during my run and reads the same baseline by its own commands — total 201
(`:38`), partition vector and inventory `lines 36395` (`:51-59`), README totals
line at `corpus/README.md:469` and footer vector at `:471-473` (`:110-111`). Two
seats, two instrument sets, same numbers; no divergence to report.

## 5. Audit recipe for round 35 (what C12/C13/C14/C17 should run)

1. **Land check** — `git status --porcelain -- corpus/knowledge` names the ten new
   files; `python3 -B reports/round-19/audit/entry-audit.py --since 4a7aede` (A's
   `git_new_entries` leg; at my measurement it reported *no entries given* —
   nothing had landed yet).
2. **Bar** — apply the **round-10 legs** (§2.1) to each new entry, head-block
   scoped for the tail fields, with the partition-specific `source:` ruling of
   §2.3. Record each leg's observed result, not a single boolean.
3. **Resolution** — every `couples:`/source pointer opened or `to-verify`-marked;
   A's unresolved list is the fast check, but its three-base resolution misses
   nothing only for path-shaped refs (prose shorthands are a known false-positive
   class — `audit-myth-culture.md` §2.5 clears two such by reading context).
4. **Duplication** — slug and title overlap against the 201 pre-existing titles
   (round-10's method: fewer than four shared content terms of length > 3).
5. **README** — after the integrator lands the delta (§4.2), re-run B; require
   `rows == files == 211`, 0 missing/ghosts/mismatches/drift, `totals_line 211`,
   `footer_ok True`, and record `readme_sha256`.
6. **Inventory** — `source-audit-inventory.py --json --summary` → `totals.files 211`.
7. **Two independent auditors** (claim C's threshold) — C13 and C14 must not share
   an instrument instance; a second process of the same read-only tool plus one
   manual re-read is the round-19 precedent (`x26-spotcheck-entries.md` §1).

## 6. Limits

- Point-in-time: every count is 2026-10-19T08:14Z–08:20Z at `4a7aede`; re-measure
  before quoting after the landing.
- A is a round-19-cohort bar applied to a round-10-cohort corpus; the false
  negatives in §2.2 are *instrument* properties, not verdicts on those entries.
- The `--since` leg reads `git diff` + untracked files; a landed-then-committed
  entry would not appear (no commits are made in this round, so the leg is sound
  here — stated, not assumed).
- I did not read the ten drafts (they do not exist yet); §5 is a method, not a
  result. No entry-quality verdict is issued by this seat.

## Owed

- The interpretation of claim C's four-field frontmatter list
  (`source / verified-at / recheck / scope`) is an **owed decision** for P01/C12:
  `- scope:` is 0/201 in this corpus, so the literal 4/4 is unreachable and the
  measurable reading must be pinned before C13/C14/C17 audit against it (§2.3).
- `reports/round-35/cov/C12-audit-runbook.md` — the runbook that turns §5 into a
  runnable recipe; owed by seat C12, not produced here.
- `reports/round-35/run-validation.py` — absent at my measurement; its C legs will
  fix the exact README/entry criteria. Re-check §2.1/§4.2 against it when it lands.

## Citations

Commands executed by this seat (read-only, at `4a7aede`, 2026-10-19T08:14Z–08:20Z):

- `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`; `git status --porcelain` → `?? reports/round-35/` only
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21 19 18 29 20 94; `find corpus/knowledge -name '*.md' | wc -l` → 201
- `python3 -B reports/round-19/audit/entry-audit.py --selftest` → 7 PASS, exit 0
- `python3 -B reports/round-19/audit/entry-audit.py <5 exemplars>` → `TOTAL 0/5 clear the bar`, exit 2
- `python3 -B reports/round-19/audit/entry-audit.py --since 4a7aede…` → "no entries given"
- `python3 -B reports/round-28/readme/sweep.py` → rows 201 / files 201, footer_ok True, readme_sha256 `053966a2147e5e71…`, exit 0
- `python3 -B reports/round-28/readme/sweep.py --selftest` → 12/12, exit 0
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → totals.files 201 (full block §4.4), exit 0
- head-field census script (inline, §2.3) → topic 201 / sources 201 / couples 201 / verified-at 198 / recheck 198 / source 131 / scope 0 / gap 2 / status 0
- corpus-wide `entry-audit.audit_entry()` sweep (inline) → gap_named 27, decision 38, source_bullets==0 113, quality_bar 15
- `grep -nE "^#{2,4}.*([Dd]ecision|DR-[A-Z]{2}-)"` on the two exemplars → no hits; corpus-wide `^#{2,4}.*[Dd]ecision[- ]?[Rr]ecord.*` → 22 files
- `sha256sum` → `corpus/README.md 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`; `reports/round-10/run-validation.py 23d6dc09002fe18c…`; `reports/round-19/run-validation.py 5b27a80de1f4b110…`; `reports/round-19/audit/entry-audit.py e7992c325a479aa7…`; `reports/round-28/readme/sweep.py 9b2ccac0046831fd…`; `tools/source-audit-inventory.py f617bb99318f501d…`
- `wc -l reports/round-19/run-validation.py` → 24; `reports/round-10/run-validation.py` → 1069
- `grep -n "^## \|^Total knowledge entries\|^Counts checked\|^Index rows" corpus/README.md` → headers :123/:147/:169/:190/:222/:245, known gaps :342, totals :469, footer :471/:473, sweeps :482/:486/:490; `wc -l` → 493

Files read (path:line):

- `reports/round-10/run-validation.py:81-82` (`C_FRONTMATTER_FIELDS`), `:100-101` (`INVENTORY_COMMAND`), `:110-112` (`URL_RE`, `REPO_PATH_RE`), `:349-377` (`entry_checks`), `:380-399` (`readme_index`)
- `reports/round-19/audit/entry-audit.py:26` (`GAP_RE`), `:27` (`DECISION_RE`), `:28-31` (`CALIB_RE`, `CANON_RE`, `URL_RE`, `MDREF_RE`), `:49-71` (`source_locators`), `:74-96` (`couples_targets`), `:99-134` (`audit_entry`), `:137-148` (`git_new_entries`, the `--since` leg), `:100` (only read-mode open outside fixtures), `:165,167,178` (selftest `open(..., "w")` fixtures)
- `reports/round-28/readme/sweep.py:4-15` (docstring: the round-28 footer defect), `:20-31` (docstring: the leg list), `:50-57` (`PARTS` order), `:59-72` (regexes incl. `FOOTER_RE`), `:119-237` (`sweep`, incl. the footer legs), `:239-431` (selftest controls 1–12)
- `reports/round-10/coverage/audit-myth-culture.md` §1.5 (A/B/C readings), §1.7 + §5 (F1), §2.3 (index-vs-files script), §2.4 (A/B/C script + observed `files=179 A=115 B=176 C=179`), §2.5 (field census, `couples` prose shorthands), §3.2 (CLOSE index-vs-files, README digest)
- `reports/round-10/coverage/audit-unchanged.md` §1.3 (per-entry digest re-derivation), §2.1–2.2 (baseline identity, independent counts)
- `reports/round-10/coverage/index-update.md:52` (row convention), §2 (sweep script)
- `reports/round-10/coverage/review-C04.md:19` (`verified-at` "dated and scope-bearing" criterion)
- `reports/round-19/audit/x26-spotcheck-entries.md` §1 (method + selftest 7/7), §2 (re-derivation table), §3 X26-1/X26-2, §4 (filler auditor), §5 (limits)
- `reports/round-19/audit/x27-coverage-readme-vs-files.md` §1 (the tool's stated scope limit: no row↔content comparison)
- `reports/round-19/audit/receipt-entries-new.json` (the 10-entry receipt: 8 pass / 2 fail on the phantom `couples` path)
- `reports/round-19/audit-1.md:25,70`, `reports/round-19/audit-2.md:104` (runner-line citations that no longer resolve — D7)
- `reports/round-20/readme/reconcile.md` §1 (two count methods), §2 (before/after sweep, convention), §3 (ten `REWRITE` rows, wrong-from-birth timeline, repair)
- `reports/round-20/readme/verify.md` V1–V3 (sweep re-run, second count method, before/after reconstruction)
- `reports/round-28/readme/sweep.py` docstring + `corpus/README.md:17-33` (revision 1.8 footer-defect record), `:3` (revision 1.9)
- `corpus/QUALITY.md` (the five admission criteria the bar encodes)
- `corpus/knowledge/culture-material/transport-mobility-lexicon.md:3` and `corpus/knowledge/myth-symbol/plant-symbolism.md:3` (`- gap:` head-field exemplars)
- `reports/round-35/claims.json` (claim C: field list, thresholds, counting commands), `reports/round-35/targets.json` (K02 mission; C12/C13/C14/C17/C11/P01 out-paths)
