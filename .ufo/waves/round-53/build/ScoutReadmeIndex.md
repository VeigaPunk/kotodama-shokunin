# ScoutReadmeIndex — records and index mechanics for claim C (round 53)

Assigned item: the exact `corpus/README.md` edits that index
`corpus/knowledge/linguistics/gesture-co-speech-pointing.md` (header count, insertion
point, byte-equal row format, totals line, footer vector, revision line), the exact
`corpus/lessons/README.md` edits that index `round-53.md` and
`round-52-verifier-spotcheck.md`, and the four controls run and pasted.

Lane state read at: HEAD `60f1d2a3d832b926e37f82b11c67496d131a1431`, clean tree except
`?? .ufo/waves/round-53/` and `?? corpus/lessons/round-53.md`. All measurements below were
taken on a private sandbox clone (`/fast/scratch/hyaku/kotodama-r53/ScoutReadmeIndex`,
`git clone --shared` of the lane) plus read-only runs in the lane. No installs. Nothing in
the lane was written except this report.

---

## 1. `corpus/README.md` — the five edits

Base line numbers (HEAD `60f1d2a`, 645 lines). Apply by **content anchor**, not by line
number: inserting the revision block shifts every later line by +11.

| # | base line | before (exact) | after (exact) |
|---|---|---|---|
| 1 | before 3 | — (file is `# kotodama-shokunin corpus index`, blank, then `revision: 2.9 …`) | prepend the `revision: 2.10` block (§1.1) at the top of the revision span, one blank line after it; the `2.9` block then begins at line 13 |
| 2 | 242 | `## linguistics/ (27)` | `## linguistics/ (28)` |
| 3 | between 245 and 246 | — (after the `dialect-register-consistency.md` row, before `historical-linguistics.md`) | the new row, §1.2 |
| 4 | 614 | `Total knowledge entries: 228.` | `Total knowledge entries: 229.` |
| 5 | 618 | `(total 228 files; directory totals 27/26/28/29/24/94).` | `(total 229 files; directory totals 28/26/28/29/24/94).` |

Not changed, and why:

- the footer's date line `Counts checked 2026-10-22 from the repo root:` stays
  (round 52's landing already stamped this date; the round is the same day and
  `reports/round-28/readme/sweep.py` reads the date but only checks its shape);
- the footer's command line `` `python3 tools/source-audit-inventory.py --json --summary
  --root corpus/knowledge` `` stays — I ran it at base (`EXIT=0`): `totals.files` **228**
  and per-directory `27/26/28/29/24/94`, so it is truthful before and after;
- the "Superseded reading, preserved as the dated record it was" paragraph stays
  (rounds 2.1–2.9 moved only the numbers there);
- the prose at `corpus/README.md:83` that names `dialect-register-consistency.md` in a
  list is not an index row — leave it.

Why each edit is load-bearing, measured (sandbox controls, each reverted afterwards):

- row missing only → sweep `rows 228 files 229`, `missing_from_index 1
  ['linguistics/gesture-co-speech-pointing.md']`, **exit 1**;
- header left at 27 → `header_drift {'linguistics': {'declared': 27, 'files': 28}}`,
  **exit 1**;
- totals line left at 228 → `totals_line 228 totals_ok False`, **exit 1**;
- footer left at `(total 228 … 27/…` → **exit 1**, measured:
  `footer_findings [{"class": "FOOTER_TOTAL", "declared": 228, "live": 229, "date":
  "2026-10-22"}, {"class": "FOOTER_DIR_TOTALS", "declared": [27, 26, 28, 29, 24, 94],
  "live": [28, 26, 28, 29, 24, 94], "order": ["linguistics", "myth-symbol",
  "culture-material", "synthesis", "verification", "civilizations"]}] footer_ok False`
  (the footer leg, `reports/round-28/readme/sweep.py:163-190`, reads both the total and the
  six directory totals in section order).

### 1.1 Revision block, ready to paste (goes above the `revision: 2.9` block)

The format is round 52's own (`git show 7cee23b -- corpus/README.md`: label line,
two-line landing statement, filename-order sentence with "byte-equal", header move,
totals move, footer vector move, then the re-measure sentence; 15 insertions, 3
deletions over five hunks). Same shape as 2.8 and 2.9. Label `2.10` sorts above `2.9`
under `tools/check-readme-revisions.py`'s numeric `label_key` (`re.M`-anchored
`^revision: <label>`, newest first) — verified, `findings 0`.

```
revision: 2.10 — Round-53 linguistics landing (2026-10-22): one linguistics entry
landed (`gesture-co-speech-pointing.md`, co-speech gesture, pointing and
quotable gestures as conlang and worldbuilding method; before it, 0 filename
owners and 0 topic-line owners, with partial owners cited one-way in its §2),
its row added in filename order between `dialect-register-consistency.md` and
`historical-linguistics.md` with the entry's `- topic:` text byte-equal;
`## linguistics/` moved 27 → **28**, totals line 228 → **229**, footer vector
`27/26/28/29/24/94` → `28/26/28/29/24/94`. Re-measured with
`python3 reports/round-28/readme/sweep.py`: 229 rows vs 229 files, exit 0.
```

### 1.2 The index row — how to make it byte-equal

`sweep.py`'s `ROW_RE` (`reports/round-28/readme/sweep.py:60`) is
`^- \`([^\`]+\.md)\` — (.*)$` (hyphen, space, backtick-name, backtick, space, **U+2014**,
space, topic) and its `topic_of` (`:74-82`, over `TOPIC_RE` at `:61`) joins the
entry's `- topic:` block by stripping each line and joining with **one space**. Generate
the row from the entry itself rather than transcribing it:

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 -B - <<'PY'
import re
p = 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md'
text = open(p, encoding='utf-8').read()
m = re.search(r"^- topic:(.*?)(?=\n- \w)", text, re.M | re.S)
assert m, 'entry has no - topic: block terminated by another - <word> line'
topic = ' '.join(x for x in (l.strip() for l in m.group(1).strip('\n').splitlines()) if x)
print(f'- `gesture-co-speech-pointing.md` — {topic}')
PY
```

Paste that one line between the `dialect-register-consistency.md` and
`historical-linguistics.md` rows. I verified the join on a deliberately wrapped
three-line probe topic: with the row built by this snippet the sweep reports
`topic_mismatch 0`. Both ways of getting it wrong were measured: one extra space
inside the topic text gives `topic_mismatch 1
['linguistics/gesture-co-speech-pointing.md']` (REWRITE), exit 1; a malformed
`name` — `topic` separator (extra spaces around the em dash) does not parse as a row at
all, so the row vanishes: `rows 228 files 229`, `missing_from_index 1`, exit 1.

### 1.3 Sweep and controls at the worktree (unpatched, base), pasted

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 28, "linguistics": 27, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 228 files 228
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 228 totals_ok True
footer {"date": "2026-10-22", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 228, "dir_totals": [27, 26, 28, 29, 24, 94]}
footer_live {"total": 228, "dir_totals": [27, 26, 28, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 bbc55fafadee8091f63c76aa724ba5b0add5f4ff563b6dfcd40238236a731f17
EXIT=0

$ python3 -B tools/check-readme-revisions.py
readme /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/README.md
sha256 bbc55fafadee8091f63c76aa724ba5b0add5f4ff563b6dfcd40238236a731f17
revision_lines [3, 14, 25, 36, 57, 69, 81, 91, 100, 109, 136, 156, 168, 188, 214, 224]
labels ["2.9", "2.8", "2.7", "2.6", "2.5", "2.4", "2.3", "2.2", "2.1", "2.0", "1.8", "1.7", "1.6", "1.5", "1.4", "1.3"]
findings 0
warnings 1
  REVISION-ORPHAN lines=[123, 134] unheaded paragraph inside revisions span (starts 'round-28 C entry landed (`linguistics/register-lexicon-ceili')
EXIT=0

$ python3 -B tools/check-readme-heading.py
readme /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/README.md
sha256 bbc55fafadee8091f63c76aa724ba5b0add5f4ff563b6dfcd40238236a731f17
h1_lines [1]
headings {"1": 1, "2": 7}
findings 0
EXIT=0
```

### 1.4 The same three after the five edits, in the sandbox (probe entry)

Probe entry written to the planned path with a `- topic:` line of the planned shape (only
the entry body was synthetic; the README edits are the ones above, applied by exact-string
replacement):

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 28, "linguistics": 28, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 229 files 229
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 229 totals_ok True
footer {"date": "2026-10-22", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 229, "dir_totals": [28, 26, 28, 29, 24, 94]}
footer_live {"total": 229, "dir_totals": [28, 26, 28, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 564ea5a43144771139debe3129496629edf025b48608ec7f96e6e1a23d0932ec
sweep_exit=0

$ python3 -B tools/check-readme-revisions.py
revision_lines [3, 13, 24, 35, 46, 67, 79, 91, 101, 110, 119, 146, 166, 178, 198, 224, 234]
labels ["2.10", "2.9", "2.8", "2.7", "2.6", "2.5", "2.4", "2.3", "2.2", "2.1", "2.0", "1.8", "1.7", "1.6", "1.5", "1.4", "1.3"]
findings 0
warnings 1
  REVISION-ORPHAN lines=[133, 144] unheaded paragraph inside revisions span (...)
exit=0

$ python3 -B tools/check-readme-heading.py
h1_lines [1]
headings {"1": 1, "2": 7}
findings 0
exit=0
```

`reports/round-53/accept-c.py` against that sandbox (probe entry cites no S-id, so the
SIDS leg is expected to fail; the three README-dependent legs are what this item owns):

```
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []
SIDS FAIL cited=0 bad=['no S-id cited']
exit=1
```

and with the single index row removed again (claim C's red-before leg, which is also
round-52 routed defect 2's requirement — gate on the sweep's own exit code, never a pipe):

```
$ python3 -B reports/round-28/readme/sweep.py     # row deleted
rows 228 files 229 … missing_from_index 1 ['linguistics/gesture-co-speech-pointing.md']
SWEEP_EXIT=1
$ python3 -B reports/round-53/accept-c.py
SWEEP FAIL exit=1 rows 228 files 229 missing_from_index 1 ['linguistics/gesture-co-speech-pointing.md']
ACCEPT_EXIT=1
```

---

## 2. `corpus/lessons/README.md` — index the two missing lesson files

Base: 526 lines; the audit measures **42 lesson files, 40 index rows** and fails twice.

```
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py     # at base
index present: True
lesson files:  42
index rows:    40
queue rows:    78
formats:       {'gate-keeper': 26, 'fragment-index': 5, 'plain': 11}
  FAIL C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  FAIL C34b_prose_arithmetic
findings:      2
  C31-1 unindexed-file: ['round-52-verifier-spotcheck.md', 'round-53.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [40, 40], 'measured': [40, 42]}}
EXIT=1
```

`round-52-verifier-spotcheck.md` is committed (`6524184`), 157 lines.
`round-53.md` is **untracked** (`?? corpus/lessons/round-53.md`, 44 lines at the time of
reading) and is still being written by the integrator.

### 2.1 Two rows after base line 110 (the `round-52.md` row)

Order is the file's own: `round-49`, `round-49-verifier-spotcheck`, `round-50`,
`round-50-verifier-spotcheck`, `round-51`, `round-51-verifier-spotcheck`, `round-52`,
then the two new ones. The row **must start with `|`**: `ROW_RE` is
`^\|\s*\`?corpus/lessons/…`; I hit a control where a `- ` bullet carrying the same pipes
was silently not a row (C31 went to 41 rows). Cells are exactly six, matching the header
`| file | format | contract | open-questions carried | disposition pointer | pin |`.

Measured at base by the audit's own `classify` / `contract_lines`:

```
| `corpus/lessons/round-52-verifier-spotcheck.md` | plain | 0/4 | none (routed defects carry no Q ids) | non-author closure record; fleet MANIFEST kotodama r52 | bytes=19714 lines=157 sha8=0c9bccc9 |
| `corpus/lessons/round-53.md` | gate-keeper | 4/4 | none (no Q ids) | `reports/round-53/claims.json` | bytes=4003 lines=44 sha8=f3e02236 |
```

`round-53.md`'s pin is **provisional** — it is the untracked working-tree file. Pin it
**last**, after its final edit, with the audit's own numbers:

```
python3 -B - <<'PY'
import hashlib, os
for n in ('round-52-verifier-spotcheck.md', 'round-53.md'):
    p = os.path.join('corpus/lessons', n); b = open(p, 'rb').read()
    print(n, 'bytes=%d lines=%d sha8=%s' % (len(b), len(b.decode().splitlines()), hashlib.sha256(b).hexdigest()[:8]))
PY
```

Shape cells drift too: `round-53.md` is `gate-keeper` only while it keeps an exact
`## Gate` line, and `4/4` only while `source:`, `verified-at:`, `recheck:` and `scope:`
all appear at line start (`c31-lessons-index-audit.py:47-56,72-90`). Re-derive both from
the audit, not from this table, if the lesson's headings change.

### 2.2 Three prose edits

- line 112, leading text: `**Rows: 40. Files: 40.**` → `**Rows: 42. Files: 42.**`
  (this is the only table count `C34b` machine-reads, regex
  `\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*`; its other count regex reads the queue
  `Rows: **78**` at line 261, which does not change).
- line 261: `Of the 40 index rows` → `Of the 42 index rows`, and
  `the ten that carry none are` → `the twelve that carry none are` (the queue stays
  **78**; the two new rows carry no question, so the "carry at least one" count stays 30).
- lines 266-267, the enumeration of no-question files: insert
  `round-52-verifier-spotcheck.md` and `round-53.md` before "and this README's self-row".

Exact replacement for the last one (base bytes):

```
  `round-51.md` (no Q ids), `round-51-verifier-spotcheck.md` and `round-52.md`
  (no Q ids), and this README's self-row.
```

→

```
  `round-51.md` (no Q ids), `round-51-verifier-spotcheck.md`, `round-52.md`
  (no Q ids), `round-52-verifier-spotcheck.md` and `round-53.md` (no
  ids), and this README's self-row.
```

### 2.3 A `## Revision 9` block at the foot (after base line 526, one blank line)

The file's convention is one numbered `## Revision N` section per integration, appended,
never an edit of an earlier one (Revision 8 is the round-52 landing and reads "40/40 …
ten indexed files carry no question"). Ready to paste:

```
## Revision 9 — round-52 closure and round-53 lesson rows (2026-10-22)

Adds two §2 rows: `round-52-verifier-spotcheck.md` (the non-author closure
record, plain, routed item 6 of that closure) and `round-53.md` (gate-keeper),
both pinned from the live bytes by
`reports/round-25/audit/c31-lessons-index-audit.py --json`. §2's count line is
42/42; the queue still has 78 rows and twelve indexed files carry no question.
The round-53 lesson's bytes are the integrator's final record, so a later edit
to it must re-pin its row, never edit a filed one. Earlier histogram prose is
dated history. Re-run
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` for the verdict.
```

The format histogram needs no change: the two files are already on disk at base, so
`gate-keeper 26 / fragment-index 5 / plain 11 (42 files)` is the same before and after;
only the **row** count moves 40 → 42.

### 2.4 After the edits, in the sandbox, pasted

```
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py
index present: True
lesson files:  42
index rows:    42
queue rows:    78
formats:       {'gate-keeper': 26, 'fragment-index': 5, 'plain': 11}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0
exit=0
```

Controls (each reverted):

- drop the `round-53.md` row → `index rows: 41`, `FAIL C31_index_rows_eq_files`,
  `FAIL C34b_prose_arithmetic` (`stated [42,42] measured [41,42]`), exit 1;
- append one line to `round-53.md` after pinning → `FAIL C34_pins_rederived`,
  `C34-1 pin-drift: [('round-53.md', 'bytes', …), ('round-53.md', 'lines', …), ('round-53.md', 'sha8', …)]`.

---

## 3. Routed item closed by this

`corpus/lessons/round-52-verifier-spotcheck.md:151` (inside item 6, `## Routed defects
(lane, next round)` at :130): "Index this file in `corpus/lessons/README.md`." —
satisfied by §2.1's first row. The other four bullets of item 6 (undrafted drummed-speech
and decline sections, the checker's limits and `dry-run.py check` gaps, S072, the
separability spelling misses) are not index work and stay open for their owners.

---

## 4. Facts, inference, gaps

Observed (commands above, base and sandbox): every number and line quoted; the five
README edits are sufficient and each is necessary; the two lesson rows plus the three
prose edits take the audit from 2 findings to 0.

Inference: none load-bearing. The only projection is §1.1's revision text wording, which
follows 2.7/2.8/2.9 sentence for sentence.

Gaps:
- the entry does not exist yet in the lane, so §1.2's row is a generator, not a pasted
  row; the final row's length and wording depend on the entry's own `- topic:` line;
- `corpus/lessons/round-53.md` is untracked and still changing, so §2.1's second pin is
  provisional by construction (pinning procedure given);
- I did not run `reports/round-53/d-count.py`, `dry-run.py`, `claims-agree.py` or
  `tools/check-claim-separability.py` (claims D and the L1's declaration instruments, not
  this item), and I did not run `accept-c.py` in the lane (it needs the real entry and the
  S187+ rows).

---

## 5. Live-tree note taken while this item ran (2026-10-22)

Claim D's edit landed into the working tree during this item:
`M corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (8 insertions, 8
deletions). Its `- topic:` line is **not** among the changed lines, so the README row for
that file is still byte-equal and the sweep is still green with the change in the tree
(measured: `rows 228 files 228`, `topic_mismatch 0`, `missing_from_index 0`, exit 0). If a
later D edit does touch the `- topic:` line, that row must be re-pinned in the same
landing or the C sweep leg fails.

`corpus/README.md` and `corpus/lessons/README.md` were left untouched by this item; the
edits in §1 and §2 are proposals for the integration owner.
