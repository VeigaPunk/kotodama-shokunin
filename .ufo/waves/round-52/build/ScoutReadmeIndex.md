# ScoutReadmeIndex — records and index mechanics for claim C (round 52)

Assigned: exact README/index edit mechanics for claim C's linguistic entry
`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (corpus
index, revision block, counts) and for a new `corpus/lessons/round-52.md` row
(lessons index + its audit script). Read-only over the lane; every proposed edit
was proved in the private sandbox clone
`/fast/scratch/hyaku/kotodama-r52/ScoutReadmeIndex`.

Lane state at measurement: HEAD `dea5ece63ca4372c41766ab242df1e26c2e6898a`,
`corpus/README.md` sha256 `f425c6ffd378af55a4a35fe851a2ceb5dd3a3d17fd9bca0c4b45864be9436ac0`,
`corpus/lessons/README.md` clean (not in `git status`). Worktree carries an
uncommitted `M` on `corpus/knowledge/linguistics/sign-languages-manual-modality.md`
and untracked `corpus/lessons/round-52.md` + `.ufo/waves/round-52/`; both READMEs
are untouched, so the mechanics below are read from clean bytes.

---

## 1. `corpus/README.md` — five edit sites, nothing else

Round 51's precedent (`git show da31d3c -- corpus/README.md`) touched exactly four
regions and nothing else: (a) a new `revision:` block inserted directly under the
H1, (b) the partition header count, (c) the one index row, (d) the
`Total knowledge entries:` line and the `Counts checked` footer. It did **not**
touch `## Known gaps` or the superseded-reading paragraph. Reproduce that shape.

Base line numbers (`corpus/README.md`, 633 lines):

| site | line | current bytes |
|---|---|---|
| revision block insertion point | 3 (after `# kotodama-shokunin corpus index` + blank, before `revision: 2.8`) | `revision: 2.8 — Round-51 linguistics landing …` |
| `## linguistics/` header | 231 | `## linguistics/ (26)` |
| row insertion point | after 253 | `- \`sound-symbolism.md\` — …` then 254 `- \`syntax-typology.md\` — word-order typology …` |
| totals line | 602 | `Total knowledge entries: 227.` |
| counts footer | 604-606 | `Counts checked 2026-10-22 from the repo root:` / `` `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` `` / `(total 227 files; directory totals 26/26/28/29/24/94).` |

### 1.1 The row (byte-equal to the entry's `- topic:` text)

`reports/round-28/readme/sweep.py` (`topic_of`, `TOPIC_RE`
`^- topic:(.*?)(?=\n- \w)` with `re.M|re.S`) joins the `- topic:` line and its
continuations with single spaces and compares the result to the row text
**exactly** (`sweep.py` sweep(), `topic_mismatch`). `ROW_RE` is
`^- `([^`]+\.md)` — (.*)$` per line: the row is one long line, em dash U+2014
with one space each side, filename bare (no partition prefix).

Alphabetical position in the linguistics section (`sound-symbolism.md` <
`speech-surrogates-whistled-drummed.md` < `syntax-typology.md`; `so` < `sp` < `sy`):

```
- `speech-surrogates-whistled-drummed.md` — <the entry's joined - topic: text>
```

Generate the text instead of transcribing it (verified: this command reproduces
README line 251 for `sign-languages-manual-modality.md` char-for-char, 582 chars):

```sh
python3 -B -c "import sys; sys.path.insert(0,'reports/round-28/readme'); \
from sweep import topic_of; \
print('- \`speech-surrogates-whistled-drummed.md\` — ' + \
topic_of('corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md'))"
```

Mechanical constraint on the entry itself: no continuation line of `- topic:` may
begin with `- ` + a word character, and the topic must be a single logical line
(`sweep.py:61` comment; contract §2.3 row 1).

### 1.2 Header, totals, footer

- line 231: `## linguistics/ (26)` → `## linguistics/ (27)` (`SECTION_RE` is
  `^## ([a-z-]+)/ \((\d+)\)\s*$`; header drift is a finding).
- line 602: `Total knowledge entries: 227.` → `Total knowledge entries: 228.`
- line 606: `(total 227 files; directory totals 26/26/28/29/24/94).` →
  `(total 228 files; directory totals 27/26/28/29/24/94).`
- line 604 date stays `2026-10-22` (round 51 changed `2026-10-21`→`2026-10-22`
  only because its count was measured that day; the footer vector order is
  `PARTS` = linguistics, myth-symbol, culture-material, synthesis, verification,
  civilizations, so **only the first element moves 26→27**).
- Re-run `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  before writing the footer; it must read `totals.files 228` (now `227`).

### 1.3 Revision block (paste-ready, draft 2.9)

Inserted at line 3, label line followed immediately by body (a label followed by a
blank line is a `REVISION-STUB` finding in `tools/check-readme-revisions.py`):

```
revision: 2.9 — Round-52 linguistics landing (2026-10-22): one linguistics entry
landed (`speech-surrogates-whistled-drummed.md`, speech surrogates — whistled,
drummed and other instrument-borne speech (horns, reed pipes, xylophones, jaw
harps, gongs) — as conlang and worldbuilding method; before it, 0 filename
owners and 1 partial topic-line mention (`culture-material/music-instrument-
lexicon.md:3`, the "talking drums" coupling, which stays there and is cited
one-way in its §2), its row added in filename order between `sound-symbolism.md`
and `syntax-typology.md` with the entry's `- topic:` text byte-equal;
`## linguistics/` moved 26 → **27**, totals line 227 → **228**, footer vector
`26/26/28/29/24/94` → `27/26/28/29/24/94`. The routed rev-1.9
`REVISION-ORPHAN` residual is carried, not repaired. Re-measured with
`python3 reports/round-28/readme/sweep.py`: 228 rows vs 228 files, exit 0.
```

Correction to the round-51 wording this draft replaces: the sign-language block
could state "0 topic-line owners" because its topic sweep returned 0. **Speech
surrogates cannot.** Measured at the lane worktree on live corpus bytes:

- filename owners: `find corpus/knowledge -iname '*surrogat*' -o -iname '*whistl*'
  -o -iname '*drum*' | wc -l` → **0**.
- topic-line mentions of surrogate-register words
  (`grep -rliP '^- topic:.*\b(speech surrogat\w*|surrogate language\w*|whistled
  speech|whistle speech|whistled register\w*|drummed speech|drum language|drum
  speech|talking drum\w*)\b' corpus/knowledge`) → **1**:
  `corpus/knowledge/culture-material/music-instrument-lexicon.md:3` ends
  `… (inventor heroes, named divine instruments, musical contests, talking drums)`.
  The loose sweep (`\b(drum\w*|whistl\w*)\b` on topic lines) returns 2, the second
  being `civilizations/finnic-sami.md:3` ("noaidi drum interpretation"), which is a
  different object. Write the honest count, not the round-51 template.

Sanity check before landing: `grep -c '^revision: 2\.9' corpus/README.md` → 1, and
labels must read strictly descending (base has 15 labels, 2.8 … 1.3; 16 after).

### 1.4 What must not move

- `## Known gaps (frontier)` (line 475+): round 51 left it alone and this wave has
  no gap line naming speech surrogates (grep for `surrogat|whistl|drum` in
  `corpus/README.md` hits only `music-instrument-lexicon.md` row 308 and
  `finnic-sami.md` row 410).
- `## linguistics/` rows are appended in filename order only; no other row's text
  or provenance changes.

---

## 2. Proof of the edit set (sandbox simulation)

Applied exactly the five sites above to the sandbox clone, plus a stub entry
carrying a one-line `- topic:`, then ran the three gates **in the sandbox**:

```
parts {"civilizations": 94, "culture-material": 28, "linguistics": 27, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 228 files 228
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 228 totals_ok True
footer {"date": "2026-10-22", ... "total": 228, "dir_totals": [27, 26, 28, 29, 24, 94]}
footer_live {"total": 228, "dir_totals": [27, 26, 28, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 6006743ba56660bd410c2fa37c2774e7016595d19c2f088627e21cda3eb86ea2
SWEEP_EXIT=0

# tools/check-readme-revisions.py
revision_lines [3, 14, 25, 36, 57, 69, 81, 91, 100, 109, 136, 156, 168, 188, 214, 224]
labels ["2.9", "2.8", "2.7", "2.6", "2.5", "2.4", "2.3", "2.2", "2.1", "2.0", "1.8", "1.7", "1.6", "1.5", "1.4", "1.3"]
findings 0
warnings 1
  REVISION-ORPHAN lines=[123, 134] unheaded paragraph inside revisions span (starts 'round-28 C entry landed (`linguistics/register-lexicon-ceili')
REV_EXIT=0

# tools/check-readme-heading.py
h1_lines [1]
headings {"1": 1, "2": 7}
findings 0
HEAD_EXIT=0
```

Negative control (the rule the sweep actually enforces): rewriting the same row as
a condensed paraphrase produced
`topic_mismatch 1 ['linguistics/speech-surrogates-whistled-drummed.md']`, exit 1.
A row that summarizes instead of copying `- topic:` fails; only byte equality
passes.

## 3. Base-state outputs in the lane (for the report's "before" column)

```
$ python3 -B reports/round-28/readme/sweep.py            # lane, exit 0
parts {"civilizations": 94, "culture-material": 28, "linguistics": 26, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 227 files 227
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []
header_drift {}   totals_line 227 totals_ok True
footer {"date": "2026-10-22", ..., "total": 227, "dir_totals": [26, 26, 28, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 f425c6ffd378af55a4a35fe851a2ceb5dd3a3d17fd9bca0c4b45864be9436ac0

$ python3 -B tools/check-readme-revisions.py              # exit 0
labels ["2.8","2.7","2.6","2.5","2.4","2.3","2.2","2.1","2.0","1.8","1.7","1.6","1.5","1.4","1.3"]
findings 0   warnings 1 (REVISION-ORPHAN lines=[112, 123], the routed rev-1.9 debt)

$ python3 -B tools/check-readme-heading.py                # exit 0
h1_lines [1]   headings {"1": 1, "2": 7}   findings 0

$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
totals.files 227 (files_with_marker 161, lines 41061)   -> must read 228 after C
```

---

## 4. `corpus/lessons/README.md` — exact edit for `round-52.md`

Audit script: `reports/round-25/audit/c31-lessons-index-audit.py` (six checks:
C31 index rows == files, C32 owners resolve, C33 formats documented, C34 pins
re-derived, C34b prose arithmetic, C34c shape cells re-derived; `--selftest`
28/28). The §1 counting commands are `ls corpus/lessons/*.md | wc -l` and
`find corpus/lessons -maxdepth 1 -name '*.md' | wc -l`.

Base state — this is **already red before any round-52 edit**, with two findings,
one of which is not about round 52:

```
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py     # lane, exit 1
index present: True   lesson files: 40   index rows: 38   queue rows: 78
formats: {'gate-keeper': 25, 'fragment-index': 5, 'plain': 10}
  FAIL C31_index_rows_eq_files   PASS C32  PASS C33  PASS C34  PASS C34c
  FAIL C34b_prose_arithmetic
findings: 2
  C31-1 unindexed-file: ['round-51-verifier-spotcheck.md', 'round-52.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [38, 38], 'measured': [38, 40]}}
```

`corpus/lessons/round-52.md` **already exists** (untracked, 41 lines, 6040 bytes,
created 2026-10-22T09:21:01; `gate-keeper` shape: `## Gate` at line 25; head lines
`source:`/`verified-at:`/`recheck:`/`scope:` at 3-6 → contract 4/4; no `Q-52-*`
ids, `grep -c 'Q-52'` → 0). Round 51's filer (`10f433c`) changed exactly four
things for its one new lesson: one §2 row, §2's `**Rows: N. Files: M.**` line, the
§4 "Of the N index rows" bullet, and a new `## Revision N` block at the foot. Do
the same, but with **two** rows — indexing only `round-52.md` leaves C31 red.

Live pins (`reports/round-25/audit/c31-lessons-index-audit.py --json`; sha8 = first
8 hex of sha256, `bytes`=size, `lines`=line count). **Re-measure immediately
before the edit**: `round-52.md` is live and grows at close.

| file | bytes | lines | sha8 | format | contract |
|---|---|---|---|---|---|
| `corpus/lessons/round-51-verifier-spotcheck.md` | 15397 | 131 | `051135de` | plain (no `## Gate`) | 0/4 |
| `corpus/lessons/round-52.md` | 6040 | 41 | `70e61749` | gate-keeper (`## Gate` :25) | 4/4 |

### 4.1 Rows — after line 108 (`round-51.md` row), keeping round order

```
| `corpus/lessons/round-51-verifier-spotcheck.md` | plain | 0/4 | none (the routed defects carry no Q ids) | `corpus/lessons/round-51.md` (outside-review record) | bytes=15397 lines=131 sha8=051135de |
| `corpus/lessons/round-52.md` | gate-keeper | 4/4 | none (no Q ids) | `reports/round-52/claims.json` | bytes=6040 lines=41 sha8=70e61749 |
```

(Format/contract/pin cells are machine-re-derived by C34c/C34; a wrong cell fails.)
`round-51-verifier-spotcheck.md`'s content review is
`corpus/lessons/round-51.md`'s outside-review record, matching the
`round-49-verifier-spotcheck.md` row's shape at line 105.

### 4.2 Count line — line 110

`**Rows: 38. Files: 38.**` → `**Rows: 40. Files: 40.**` (the only string the
`C34b` regex `\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*` reads, and it must equal
`[rows, files]`).

### 4.3 §4 queue bullet — line 259 (prose; the tool reads only `Rows: **78**`)

```
- Rows: **78**. Of the 40 index rows, **30 carry at least one question**;
  the ten that carry none are `round-1-gates-and-triage.md` (its lessons
  were closed within round 1), `round-25.md` (this round's own claims are
  pending, not carried), `round-49.md`, `round-49-verifier-spotcheck.md`,
  `round-50.md`, `round-50-verifier-spotcheck.md` (no new Q ids),
  `round-51.md` (no Q ids), `round-51-verifier-spotcheck.md` (the routed
  defects carry no Q ids), `round-52.md` (no Q ids), and this README's
  self-row.
```

Keep `Rows: **78**.` — no queue rows are added, so `len(queue_rows)` stays 78.

### 4.4 Revision block at the foot (after `## Revision 7 …`)

```
## Revision 8 — round-52 lesson rows (2026-10-22)

Adds two §2 rows, both pinned from the live bytes by
`reports/round-25/audit/c31-lessons-index-audit.py --json`:
`round-51-verifier-spotcheck.md`, which the round-51 index revision left
unindexed, and `round-52.md`. §2's count line is 40/40; the queue still has 78
rows and ten indexed files carry no question. Live histogram: gate-keeper 25,
fragment-index 5, plain 10 (40 files total); earlier histogram prose is dated
history. Before this revision the audit exited 1 with `C31-1 unindexed-file:
['round-51-verifier-spotcheck.md', 'round-52.md']` and `C34-2
prose-arithmetic-drift`; after it, `findings: 0`, exit 0. Re-run
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` for the verdict.
```

§3's histogram prose (lines 132-164) is left as dated history — revisions 4-7 all
did this; the live histogram lives in the revision block only. Line 359
("revision 1 … revisions 4 and 5 below") is stale but revisions 6 and 7 both left
it, so leave it and do not add a seventh claim to that sentence.

### 4.5 Proof (sandbox, same edits + a copy of the real `round-52.md`)

```
lesson files: 40   index rows: 40   queue rows: 78
formats: {'gate-keeper': 25, 'fragment-index': 5, 'plain': 10}
  PASS C31  PASS C32  PASS C33  PASS C34  PASS C34c  PASS C34b
findings: 0    EXIT=0
--selftest: SELFTEST OK: 28/28 checks passed
```

---

## 5. Facts claim C's §2 boundary must reconcile (observed, not inferred)

Partial owners re-read at the lane worktree, exact lines:

- `corpus/knowledge/linguistics/phonetics-phonology.md` — `## 7. Environment,
  anatomy, society → inventory (calibrated)` at **:194**; whistled coupling at
  **:197-198** ("Whistled speech: mountains + long-distance herding → whistled
  registers (Silbo Gomero, Kuşköy, Chinantec; Meyer 2008)"), drum coupling at
  **:199-200** ("Drum language: tone + gongs → … Kele/Congo; Carrington 1949;
  needs tonal lexicon + redundancy"). (The wave context's ":197-199" is this pair.)
- `corpus/knowledge/culture-material/music-instrument-lexicon.md` — table row
  **:98** "instruments that speak" (dùndún, atumpan, Lokele drum-speech) and
  **:100** "**The talking drum is this lane's centerpiece coupling** … Drum and
  whistle speech are language phenomena, not merely music phenomena."
- `corpus/knowledge/linguistics/orality-formulaic-language.md` **:114** (media
  extensions: drums as broadcast layer, Busnel & Classe 1976 on whistled
  registers) and **:124** (meter table: lexical tone → "drum/whistle speech").
- `corpus/knowledge/linguistics/sound-symbolism.md` **:121** (coupling table row
  "music | tone-language drum/whistle speech — phonological encoding on
  instruments"), and its `- couples:` at **:19** states the split the new entry
  must not contradict: `phonetics-phonology.md` "§7 owns whistled/drum channels".

So the entry's §2 must hand channel acoustics and the inventory coupling to
`phonetics-phonology.md` §7, the instrument taxonomy to
`music-instrument-lexicon.md`, the oral-formulaic broadcast layer to
`orality-formulaic-language.md`, and keep the surrogate as designed method
(encoding, ambiguity, ecology, social control, decline). It should also cite
`:19`/`:100` one way so a reader is not told two files own the same thing.

## 6. Result

- C's corpus-index landing is a five-site edit (revision 2.9 block, header 26→27,
  one byte-equal row after `sound-symbolism.md`, totals 227→228, footer vector
  first element 26→27 with the `2026-10-22` date kept); proved green on all three
  gates in the sandbox, and proved able to fail on a paraphrased row.
- The lessons index needs two rows, not one: `round-51-verifier-spotcheck.md`
  (base defect, already present at HEAD) and `round-52.md`, plus the 40/40 count
  line, the §4 bullet and a Revision 8 block; proved `findings: 0`, exit 0,
  selftest 28/28. Leaving the spotcheck row out keeps C31 red and would make the
  round's own index claim false.
- Unrun checks: none for these two files. No tool installed; no pacman/uv/npx
  call. No lane file was edited; all experiments ran in
  `/fast/scratch/hyaku/kotodama-r52/ScoutReadmeIndex`.
- Remaining unknown (owner: L1/integrator): whether the wave will land
  `round-51-verifier-spotcheck.md`'s row in the same edit as `round-52.md`; the
  audit cannot go green otherwise, and `round-52.md`'s pin must be re-measured at
  the moment of writing because the file is untracked and still growing.
