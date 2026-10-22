# ScoutEntryMechanics — round 55, claim C: entry head, README index and record mechanics

- Seat: leaf, no subagent dispatch. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim base `f4015e7`.
- Read-only. Nothing in the lane was edited, staged or landed. The only file written is this report. No git and no `jj` ran.
- Evidence is line-referenced at base; every number below was measured in this session, not carried.
- Axes judged: coverage (what shape the entry and its row must take), operability (exact commands and base readings), calibration (how strong each format claim actually is).

## 0. Result

The entry contract is round 50's `ReviewEntryContract.md` §2 (`:32-99`); there is no round-55 contract file (`ls .ufo/waves/round-55` shows only build spec, dispatch and predispatch). The model is `corpus/knowledge/culture-material/masks-masquerade.md` (152 lines), and at base it **passes the §2.9-A mechanical checker unchanged, the provenance gate with `findings=0`, and the couples resolver with exit 0**. The README needs four text changes plus one revision block; the new row goes **between README lines 307 and 308** (`mineral-stone-symbolism.md` then `motif-index-usage.md`). Base sweep: exit 0, `rows 230 files 230`, `topic_mismatch 0 []`. Decision prefix `DR-MON` is unused in `corpus/`, `tools/` and `reports/`.

## 1. Entry head — exact order, column 0, eight fields

The checker extracts head keys with `^- ([a-z][a-z \-]*?):` at column 0 and compares the list to a fixed sequence (`ReviewEntryContract.md:44-55`; checker `:123-127,154`). Any other column-0 `- lowercaseword:` bullet in the opening block breaks the comparison, including inside `- sources:`.

| # | key | model line | enforced rule |
|---|---|---|---|
| 1 | `- topic:` | `masks-masquerade.md:3` | exactly one; no column-0 continuation line beginning `- ` + word char; must hold the register's whole words (for C: monster, bestiary…) so later probes find it |
| 2 | `- gap filled:` | `:4` | the absence sweep as run, with measured result, base sha, and `path:line` boundaries |
| 3 | `- sources:` | `:5` (nested `:6-7`, two-space indent) | gate-checked by `tools/gates/provenance-audit.py:75-76,310-318`; nested items may not start at column 0 |
| 4 | `- couples:` | `:8` | exactly one; each `;`-group starts with a partition label + em dash; every `*.md` token must resolve (cross-partition as `../<partition>/<file>.md`, same directory as bare basename) |
| 5 | `- source:` | `:9` | singular key, present in addition to the plural, so both head readings are satisfied |
| 6 | `- verified-at:` | `:10` | date + base sha + commands actually run with measured values |
| 7 | `- recheck:` | `:11` | trigger first; the model short-circuits to `see §13.` and still passes — the fuller form is contract-preferred, not checker-enforced |
| 8 | `- scope:` | `:12` | scope, exclusions and the `lore-shokunin` handoff |

Exact key sequence: `topic, gap filled, sources, couples, source, verified-at, recheck, scope`. In the model the head is lines 3–12, line 13 blank, first H2 at line 14; title on line 1, blank line 2.

## 2. Heading and body rules (checker-enforced)

- Line 1 exactly `# <Title> — <subtitle>`: one H1, U+2014 with one space each side, first line of the file (`masks:1`). One H1 in the whole file.
- H2s `## 1. …` through `## N. …`, consecutive; **zero** `###` lines; last H2 contains `Scope`; at least one H2 contains `Recheck` (the contract places it immediately before Scope, `:42`); one H2 contains `Calibration`.
- A paragraph beginning `**NON-CANON` at column 0.
- At least one pipe table with a `|---|` separator row, blank line before and after.
- Every `§N` must be ≤ the H2 count (model: 14 H2, max §13).
- Forbidden tokens: `TODO`, `TBD`, `placeholder`, `scaffold`, `MVP` (case-insensitive).
- Measured on the model: 152 lines, keys in CANON order, 14 H2 numbered 1..14, no H3, checker prints `PASS`. Length ceiling: contract `≤250` (`:36`); this wave's declared bound is `≤230` lines and is not machine-checked (see §7).

## 3. Calibration codes — `corpus/knowledge/verification/calibration-registry.md:33-39`

Codes table header at `:33`, five code rows at `:35-39`. Cite them in a Status column, as the model does (`masks-masquerade.md:137`, "Codes as in `../verification/calibration-registry.md:35-39`").

| code | status (verbatim from `:35-39`) | stop rule |
|---|---|---|
| R | "Rejected/discredited as the specified general inference" | "Do not use as evidence; may portray the theory as a dated ideology or choose a fictional premise explicitly" |
| C | "Contested empirical or historical interpretation" | "Preserve alternatives, scope, and discriminating evidence; do not report one reading as settled" |
| B | "Bounded, usable within a named domain" | "Carry population, genre, period, task, and exceptions; no extrapolation by resemblance" |
| H | "Heuristic or interpretive framework, not an established causal law" | "Generate with it; label the designer's choices instead of presenting a discovery" |
| T | "Unresolved provenance or claim check" | "Mark `(to-verify)` inline at the exact dependency; do not make it load-bearing" |

## 4. Decision-record prefix

Use **`DR-MON-01`, `DR-MON-02`, …**. `grep -rn 'DR-MON'` returns 0 lines under `corpus/`, `tools/` and `reports/`; the only hits in the lane are `.ufo/waves/round-55/build-spec.json`, `build-dispatch.json`, `build-sent-payload.json` and `gen-build-spec.py`, which carry this dispatch text, not a record. Existing prefixes are two-to-four letter blocks (`DR-MS`, `DR-MMC`, `DR-CM`, `DR-TK`, …), so `DR-MON` is distinct. Table form: `| ID | Decision | Trigger | Failure if skipped |` (`ReviewEntryContract.md:62`).

## 5. README — exact edits at base

Section order and headers at base: linguistics `:262`, myth-symbol `:293`, culture-material `:322`, synthesis `:353`, verification `:385`, civilizations `:412`, Known gaps `:509`. The sweep's canonical order is that same six-part order (`reports/round-28/readme/sweep.py:49-56`), which is also the footer vector order.

| edit | base anchor | current text | after landing |
|---|---|---|---|
| section header | `README.md:293` | `## myth-symbol/ (26)` | `## myth-symbol/ (27)` |
| index row | between `:307` and `:308` (`mineral-stone-symbolism.md`, `motif-index-usage.md`) | — | new line 308: ``- `monsters-hybrid-beings.md` — <topic text>`` |
| totals line | `:636` | `Total knowledge entries: 230.` | `Total knowledge entries: 231.` |
| counts footer | `:638-640` | `Counts checked 2026-10-22 from the repo root:` / command line / `(total 230 files; directory totals 28/26/29/29/24/94).` | keep date and command; `(total 231 files; directory totals 28/27/29/29/24/94).` |
| revision block | above `:3` (`revision: 2.11 — Round-54 …`) | — | new `revision: 2.12 — Round-55 myth-symbol landing (2026-10-22): …` block |
| tail (convention, not checked) | end of file | last paragraph is an `Index rows re-measured 2026-10-19 …` reading | append `Index rows re-measured 2026-10-22 …` paragraph |

Insertion is alphabetical by filename: `mineral-stone-symbolism.md` < `monsters-hybrid-beings.md` < `motif-index-usage.md`; the on-disk `sorted()` order agrees (`monsters` would be index 14 of 27). Line numbers below the row shift by one after insertion, and again by the revision block's height at the top, so edit by anchor text.

Row text rule: one line, exactly ``- `monsters-hybrid-beings.md` — `` then the topic text. The topic may span lines in the entry; the row must be the continuation-joined string with **single** spaces, byte-equal (`sweep.py:74-82`). The model row (`README.md:340`) is this shape and the base sweep reports `topic_mismatch 0 []`.

Revision-block convention (`README.md:3-12` pattern; `tools/check-readme-revisions.py:111-155`): newest first directly above the previous label, one `revision: 2.12 — …` label line immediately followed by non-blank body text, a blank line between blocks, labels unique and non-increasing. Base reading: labels `2.11 … 1.3`, `findings 0`, one pre-existing warning `REVISION-ORPHAN lines=[143, 154]`, exit 0. That warning is carried, not repaired.

A faithful 2.12 body, mirroring the 2.11 wording: one myth-symbol entry landed (`monsters-hybrid-beings.md`, monsters and hybrid beings as a cultural category); "its row added in filename order between `mineral-stone-symbolism.md` and `motif-index-usage.md` with the entry's `- topic:` text byte-equal"; `## myth-symbol/` moved 26 → **27**, totals line 230 → **231**, footer vector `28/26/29/29/24/94` → `28/27/29/29/24/94`; re-measured with `python3 reports/round-28/readme/sweep.py`: 231 rows vs 231 files, exit 0.

## 6. Baseline readings (measured this session, lane root)

```
python3 -B reports/round-28/readme/sweep.py           exit 0
parts {"civilizations": 94, "culture-material": 29, "linguistics": 28, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 230 files 230   missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 230 totals_ok True
footer {"date": "2026-10-22", "total": 230, "dir_totals": [28, 26, 29, 29, 24, 94]}   footer_ok True
readme_sha256 617279332bcf83239c6507d030ea9acfa8ee75e97343a9c1083f9f4d82df7e77

python3 -B tools/check-readme-heading.py                exit 0  h1_lines [1]  headings {"1": 1, "2": 7}  findings 0
python3 -B tools/check-readme-revisions.py              exit 0  findings 0  warnings 1 (REVISION-ORPHAN 143,154)
provenance-audit.py masks-masquerade.md                 exit 0  findings=0  to-verify-count 1
basename-couples-resolver.py masks-masquerade.md        exit 0  (direct and fallback rows, none unresolved)
```

## 7. What the sweep checks about a row against the entry's `- topic:` line

- `ROW_RE` (`sweep.py:60`) captures `(.*)` after ``- `<file>.md` — `` on **one** line; the row description cannot wrap.
- `TOPIC_RE` (`:61`) takes the entry's `^- topic:(.*?)` up to the next line beginning `- ` + word character, then `topic_of` (`:74-82`) strips each line and joins non-empty lines with **one space**.
- The two strings are compared with `!=` (`:136-148`). Any difference in case, punctuation, spacing or trailing whitespace is a finding; class is `REWRITE` when a topic exists and `NO_TOPIC_FIELD` when it does not, and the run prints `topic_mismatch <n> [...]` with `row_chars` and `topic_chars`.
- Consequence: a continuation line inside `- topic:` that begins `- ` + word char silently truncates the topic and the README row can then never match; a period at the end of the topic must also end the row.
- Other legs in the same run: `SECTION_RE` (`:59`) declared count vs files on disk → `header_drift`; files with no row → `missing_from_index`; rows with no file → `orphan_rows`; duplicate rows; `TOTALS_RE` (`:62`) totals line; `FOOTER_RE` (`:66-72`) total and the six-value directory vector compared in the canonical partition order. `ok` is false on any of them (`:191-194`), and header drift or a stale footer makes the run exit 1.

## 8. Claim C record legs — `reports/round-55/accept-c.py`

- `ENTRY` = `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md`; `TOTAL` 231; `FIRST_SID` 285; `FLOOR` 20 distinct ids.
- SET: every file under `corpus/knowledge`, any extension, equals the 230 paths in `reports/round-55/base-knowledge-files.txt` plus exactly that entry.
- SWEEP: runs `reports/round-28/readme/sweep.py` with `cwd=root`, no pipe, and requires exit 0 plus `rows 231 files 231` and `missing_from_index 0`. So the whole README edit (header, row, totals, footer) is load-bearing: a row without the footer bump makes the sweep exit 1 and fails this leg, which is the declared `RED-SWEEP-EXIT` control.
- FLOOR/RANGE: every `\bS\d{3}\b` occurrence anywhere in the entry — head, body, recheck, scope — is collected; each must be ≥ S285, match **exactly one** `^\| S\d{3} ` row, and that row must split into at least 13 pipe cells. Range notation is rejected by `\bS\d{3}\s*(?:[–—-]|to)\s*S?\d{3}\b`, so `S285 to S290` and `S285–S290` both fail.
- STATUS: `cells[8].strip() == "mined"`. USEDBY: `cells[11]` contains the entry path. ACCESS: `tools/check-source-access.py` exit 0.
- There is **no line-count leg**. The 230-line bound lives in the dispatch text only; the contract's own cap is 250. Follow 230.
- `--root` is only meaningful for a complete clone: the sweep derives its lane from its own file location (`sweep.py:44-47`), so a clone must contain `reports/round-28/readme/sweep.py` as well.

## 9. Calibration note on the head shape

The eight-field order is **not** the myth-symbol norm. Census of the 26 myth-symbol entries: 18 carry six keys (`topic, sources, couples, source, verified-at, recheck`); 0 carry the exact CANON eight; `binding-speech-complex.md` and `mineral-stone-symbolism.md` carry eight with `gap filled` **before** `topic`; `sacred-topography-pilgrimage.md` carries nine (`gap` plus `gap filled`) and would fail the checker. The nearest exact-CANON precedent is the model itself, a culture-material entry landed last round (`masks-masquerade.md:3-12`).

So: writing monsters in masks' order is the strictest-checker-safe choice and the newest C precedent, but it would be the **first** exact-CANON head in myth-symbol — state that as a deliberate uniformity move toward the newest generation, not as partition practice. Contract §3 (`:204`) records the DR-1 conflict about plural-only `sources:`; the eight-field head satisfies both readings and is what the model does.

## 10. Pitfalls worth pre-empting

1. A `- topic:` continuation beginning `- ` + word char truncates the topic and guarantees a row mismatch.
2. The README row cannot wrap; the entry topic can. Join is one space, so a double space fails.
3. Every S-id mentioned anywhere in the entry must be a `mined` row whose `used-by` names the entry; do not name ids in `- recheck:` or Scope that the body does not cite, and never write an id range.
4. SOURCES rows must start `| S285 ` with the space after the id and keep all eleven columns; a short row fails RANGE through the 13-cell test.
5. Adding the file without bumping `## myth-symbol/ (26)` produces `header_drift` and sweep exit 1.
6. Both the totals line and the footer total must be 231, and the footer vector must be `28/27/29/29/24/94` in the order linguistics, myth-symbol, culture-material, synthesis, verification, civilizations.
7. The revision label must be unique, non-increasing, and followed by non-blank body text; the pre-existing `REVISION-ORPHAN` warning at lines 143/154 is carried.
8. No column-0 `- word:` bullet may appear in the opening block outside the eight keys (nested `- sources:` items stay indented two spaces).
9. `- topic:` count and `- couples:` count must each be exactly one; partition-labelled `;`-groups inside the couples value are fine.

## 11. Unrun checks

- No entry, README edit, SOURCES row or revision block was written, and `accept-c.py` was not run (at base it fails SET by construction).
- No clone, no sandbox, no counterfactual tree; the post-landing row/file/header/footer arithmetic is derived from the sweep's own comparison code, not observed on a landed tree.
- No external source was opened; no source text, quote or locator was verified (not this seat's question).
- Claim O's files were not read or checked.
- Only the model entry was run through the gates; no other myth-symbol entry was audited.

## 12. Tooling record

No installs or upgrades; no package manager touched. Commands were read-only: `reports/round-28/readme/sweep.py`, `tools/check-readme-heading.py`, `tools/check-readme-revisions.py`, `tools/gates/provenance-audit.py`, `tools/harness/basename-couples-resolver.py`, `grep`, `sed`, `awk`, and an in-memory copy of the §2.9-A checker (no file written). No `git` or `jj` invocation of any kind.
