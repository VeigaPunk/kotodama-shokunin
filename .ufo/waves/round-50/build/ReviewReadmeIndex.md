# ReviewReadmeIndex: round-50 claim C, one culture-material row

Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (base 4ad2683). Scope: how to add one culture-material row to `corpus/README.md` so `tools/check-readme-heading.py`, `tools/check-readme-revisions.py` and `reports/round-28/readme/sweep.py` stay green.

Lane untouched. All runs used temp copies: `/tmp/r50-readme-green` (unmodified) and `/tmp/r50-readme-sim` (simulated landing with a stand-in entry). Lane `corpus/README.md` sha256 `666fb794…c35` at start and end. No installs or updates.

## 1. Current state (unmodified copy)

| gate | command | result |
|---|---|---|
| heading | `python3 -B tools/check-readme-heading.py` | rc 0; single H1 at line 1; 0 findings |
| revisions | `python3 -B tools/check-readme-revisions.py` | rc 0; 0 findings; 1 advisory `REVISION-ORPHAN` at lines 90–101 (pre-existing rev-1.9 body; warnings never fail) |
| sweep | `python3 -B reports/round-28/readme/sweep.py` | rc 0; rows 225 = files 225; `culture-material` 27; totals 225; footer 2026-10-19 `25/26/27/29/24/94` |
| footer command | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files` 225 |
| selftests | sweep / heading / revisions `--selftest` | 12/12; 8/8; all passed with 1 SKIP (§6) |

## 2. Procedure (apply to `corpus/README.md`; re-grep anchors before applying)

**A. Revision record.** Insert above the current `revision: 2.6` line (line 3 at baseline). Label `2.7` is unused at baseline. The body is 6 lines with no blank line inside, no line starting `#`, `revision:` or a code fence, and one blank line after it. Write the final sentence only after the post-landing sweep returns exit 0.

```
revision: 2.7 — Round-50 culture-material landing (2026-10-21): one culture-material
entry landed (`pastoralism-animal-husbandry.md`), its row added in filename order
between `music-instrument-lexicon.md` and `ritual-garments.md` with the entry's
`- topic:` text byte-equal; `## culture-material/` moved 27 → **28**, totals line
225 → **226**, footer vector `25/26/27/29/24/94` → `25/26/28/29/24/94`. Re-measured
with `python3 reports/round-28/readme/sweep.py`: 226 rows vs 226 files, exit 0.

```

**B. Four present-tense pins**, each changed once (baseline line numbers):
- L266 `## culture-material/ (27)` → `## culture-material/ (28)`
- L578 `Total knowledge entries: 225.` → `Total knowledge entries: 226.`
- L580 `Counts checked 2026-10-19 from the repo root:` → `Counts checked 2026-10-21 from the repo root:` (date is convention; no gate reads it)
- L582 `(total 225 files; directory totals 25/26/27/29/24/94).` → `(total 226 files; directory totals 25/26/28/29/24/94).`

Do **not** change the historical `225` literals at L13 (`**225**` in rev 2.6) and L22 (`225 rows vs 225 files`). An exhaustive grep for `225` in the README finds only these four present-tense and two historical hits. A global replace would corrupt the historical ones.

Scope check: grep for `\b225\b`, `knowledge entries: 2\d\d`, `culture-material/ \(27\)` and `directory totals 25/26/27` in `corpus/QUALITY.md`, `corpus/SOURCES.md`, `tools/source-audit-inventory.py` and `reports/round-28/readme/sweep.py` returned no matches.

**C. Row.** Insert after L285 (`- \`music-instrument-lexicon.md\` — …`) and before L286 (`- \`ritual-garments.md\` — …`). This is inside `## culture-material/` (L266 to the `## synthesis/` header at L295). Text:

`- \`pastoralism-animal-husbandry.md\` — <TOPIC>`

Generate `<TOPIC>` rather than typing it. From the lane root, in a temp copy:

```
python3 -B -c "import sys; sys.path.insert(0,'reports/round-28/readme'); import sweep; print('- \`pastoralism-animal-husbandry.md\` — ' + sweep.topic_of('corpus/knowledge/culture-material/pastoralism-animal-husbandry.md'))"
```

This one-liner was run on the simulation; its output was byte-equal to the simulated row (`ROW_RE` needs exactly ` — ` with U+2014 and ASCII spaces, one line, no trailing space). Filename order: `music-instrument-lexicon.md` < `pastoralism-animal-husbandry.md` < `ritual-garments.md`. This is convention only; the sweep does not check order.

**D. Entry file** (required by the gates, not checked for content): `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`. Exactly one new `.md` in that directory; the sweep counts every `.md` there, so no stray drafts. Its `- topic:` line must be followed by a line starting `- ` plus a word character. The 8-field head's `- gap filled:` satisfies this. A non-word bullet after the topic (e.g. `- \`x\``) makes `TOPIC_RE` fail to match (checked, §4).

## 3. Simulated landing (`/tmp/r50-readme-sim`, stand-in entry, 226 files)

Applied A–C with `edit`. Results:
- heading rc 0.
- revisions rc 0; the advisory `REVISION-ORPHAN` moved to lines 97–108 (count unchanged).
- sweep rc 0: rows 226 = files 226; `culture-material` 28; totals 226 ok; footer 2026-10-21 `25/26/28/29/24/94` ok; missing, orphan, topic_mismatch and drift all empty.
- `source-audit-inventory.py` `files=226`.
- Selftests: sweep 12/12, heading 8/8, revisions all passed with the same SKIP.

Edit-tool facts observed:
- The anchor line must be fully displayed. L285 was truncated and the edit was refused until I read `:285:raw`.
- The tag rotated `53C5 → FEEF` after the edit, so re-read before a second edit.
- All line numbers in one edit call refer to the original numbering.

## 4. Negative controls (in-memory variants of the simulated README)

Each variant fails only its intended class.

| variant | failing class |
|---|---|
| row separator `-` instead of ` — ` | sweep `missing_from_index` |
| row text + `.` | sweep `topic_mismatch` |
| header left at `(27)` | sweep `header_drift` {culture-material: declared 27, files 28} |
| totals line left at 225 | sweep `totals_ok` false |
| footer total left at 225 | sweep `FOOTER_TOTAL` |
| footer vector left at 25/26/27 | sweep `FOOTER_DIR_TOTALS` |
| revision label `2.6` reused | revisions `REVISION-DUP` |
| revision label `1.9` at top | revisions `REVISION-ORDER` |
| blank line after label | revisions `REVISION-STUB` |
| `# note` line inside record | heading `H1-COUNT` |
| blank line inside record | revisions advisory `REVISION-ORPHAN` only; verdict stays green |
| row deleted | sweep `missing_from_index` |
| ghost row for absent file | sweep `orphan_rows` |
| non-word bullet after topic | `TOPIC_RE` no match (would be `NO_TOPIC_FIELD` on the entry) |

Also checked: `topic_of(entry)` equals the simulated row's topic text (true).

## 5. Not covered by these gates (verify elsewhere)

- Entry contract: 8-field head, decision tables, calibration flags, length (≤ ~250 lines), lore handoff.
- Every cited S-id resolves to a `corpus/SOURCES.md` row whose used-by names the entry (claims.json `after_required`).
- Footer date and row order: convention only.
- The pre-existing `REVISION-ORPHAN` advisory at L90–101 is out of C's scope; do not fix it in this landing.

## 6. Calibration warning for claim O and any selftest reading

`tools/check-readme-revisions.py --selftest` prints "all checks passed" in a non-git copy, with `SKIP control: base c42d675 … (base object unreachable)`. That skip-pass is R3, which claim O is changing to fail-closed. After O lands, the same temp-copy selftest must return nonzero unless the base object resolves. Do not count this SKIP as a green control.

## 7. Unrun checks and limits

- No real entry exists in the lane yet. The simulation used a stand-in with a synthetic topic containing U+2014 and U+2192. A real topic with other Unicode matches only if generated by `topic_of` (§2C).
- Not run: the lane itself after any landing, `--json` receipts, the revisions selftest git control (base object), O's and Ca's gates, and any entry-contract or SOURCES checks.

## 8. Installs and writes

No installs or updates. No lane writes except this report. Temp artifacts: `/tmp/r50-readme-green`, `/tmp/r50-readme-sim`, `/tmp/r50-*.out`, `/tmp/r50-st-*.out`.

## 9. Checks for the main agent after landing (run once)

1. `python3 -B tools/check-readme-heading.py && python3 -B tools/check-readme-revisions.py && python3 -B reports/round-28/readme/sweep.py`. Expect exit 0 each. Revisions shows one advisory `REVISION-ORPHAN`, shifted by the record length.
2. `find corpus/knowledge -name '*.md' | wc -l` → 226; `ls corpus/knowledge/culture-material/*.md | wc -l` → 28.
3. `python3 -B tools/source-audit-inventory.py` → `files=226`.
4. `python3 -B reports/round-28/readme/sweep.py --selftest` → 12/12.
