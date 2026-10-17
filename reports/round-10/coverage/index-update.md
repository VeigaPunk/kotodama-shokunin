# R10-C21 — index updater: `corpus/README.md` rows + known-gaps vs actual partition contents

- seat: R10-C21 index updater. lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  assignment: *after ≥8 entries land (poll, max 20 min): update `corpus/README.md`
  index rows + known-gaps to match actual partition contents; record sweep
  command + counts; `reports/round-10/coverage/index-update.md`.*
- date: 2026-10-17, local clock UTC−03:00 (all times below UTC). Poll window
  opened 21:26:34Z (baseline snapshot, 30 s cadence, 20-min cap → 21:46Z);
  threshold (8 landed) observed 21:35:23Z; window closed by completion, not by
  the cap. Final sweep 21:39:57Z.
- revision binding: `git rev-parse HEAD` = `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
  ("round-10: availability attempt 3"); declared round-10 `baseline_revision` =
  `9dc18ec1339bffd6f81e74f1a5742464ef578749` (`reports/round-10/claims.json`).
  No commit was made by this seat.
- role limits: this seat counts and repairs index prose. Its writes are
  `corpus/README.md` and this fragment (scratch under `.scratch/`). It admits
  no entry, judges no entry's quality or sources (R10-C11..C20 own that),
  touches no gate, ledger, or canon, and does not absorb sibling fragments'
  evidence as its own.

## 1. Landing state observed

Baseline at 21:26:34Z (`ls corpus/knowledge/<partition>` per partition, sorted,
saved to `.scratch/r10-c21-baseline-files.txt`, 61 lines):

| partition | before | after | new |
|---|---|---|---|
| linguistics | 16 | 19 | `language-shift-obsolescence-revival.md`, `numerals-and-measures.md`, `sound-symbolism.md` |
| myth-symbol | 16 | 19 | `direction-symbolism.md`, `plant-symbolism.md`, `divination-omen-systems.md` |
| culture-material | 16 | 18 | `transport-mobility-lexicon.md`, `vessel-container-lexicon.md` |
| verification | 13 | 15 | `header-conformance-readings.md`, `verification-independence-anti-circularity.md` |
| synthesis | 24 | 24 | — (unchanged; corroborated by `audit-unchanged.md`) |
| civilizations | 94 | 94 | — (unchanged; corroborated by `audit-unchanged.md`) |

Landing window from file mtimes (`stat -c '%Y %n'`, filtered to files absent
from the baseline snapshot): earliest `verification/header-conformance-readings.md`
21:31:46Z, latest `linguistics/language-shift-obsolescence-revival.md` 21:38:48Z.
Ten entries, matching the C-claim's declared 3/3/2/2 split. Mtimes are last-write
times, so the window is a lower bound on author activity, not a schedule.

Counts command (re-run 21:39:57Z, exit 0):

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files = 189; totals.marker_occurrences = 633
```

## 2. The sweep — index rows vs the files they name

The index convention this sweep enforces: every row is `- \`<file>\` — <topic>`,
where `<topic>` is the entry's `- topic:` head-block text, multi-line topics
joined with single spaces, rows ordered by filename within each partition.
That convention was derived by measurement, not assumed: applying it to the
179 pre-round-10 entries matched every row but the two named in §4.

Canonical command (run from the lane root; the same script is kept at
`.scratch/r10-c21-sweep.py`, untracked and disposable):

```sh
python3 - <<'PY'
import re, pathlib
def topic_of(path):
    out=[]; in_t=False
    for l in path.read_text().split('\n'):
        if l.startswith('## '): break
        if l.startswith('- topic: '):
            in_t=True; out.append(l[len('- topic: '):]); continue
        if in_t:
            if l.startswith('  ') and l.strip(): out.append(l.strip()); continue
            elif l.strip()=='': continue
            else: break
    return ' '.join(out)
readme = pathlib.Path('corpus/README.md').read_text()
rows = {m.group(1): m.group(2) for m in re.finditer(r'^- `([^`]+\.md)` — (.*)$', readme, re.M)}
parts={}; missing=[]; mism=[]; orphan=[]
for part in ['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']:
    files=sorted(pathlib.Path(f'corpus/knowledge/{part}').glob('*.md'))
    parts[part]=len(files)
    for f in files:
        if f.name not in rows: missing.append(f.name)
        elif topic_of(f)!=rows[f.name]: mism.append(f.name)
for name in rows:
    if not any(pathlib.Path(f'corpus/knowledge/{p}/{name}').exists() for p in parts):
        orphan.append(name)
print('parts', parts, 'rows', len(rows), 'files', sum(parts.values()))
print('missing_from_index', len(missing), missing)
print('topic_mismatch', len(mism), mism)
print('orphan_rows', len(orphan), orphan)
PY
```

Final run 21:39:57Z, exit 0, re-confirmed 21:41:19Z, exit 0 (full output in
`.scratch/r10-c21-sweep-final.txt`):

```
parts {'linguistics': 19, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 24, 'verification': 15, 'civilizations': 94} rows 189 files 189
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
```

Control history before the new rows were trusted (the sweep was itself revised
twice): the 21:28Z pass covered the four thin partitions only (61 files) with a
first-physical-line extractor and returned 0 missing / 0 mismatch; the first
six-partition pass flagged `africa-primary-sources.md`; `phonetics-phonology.md`
became visible only once the extractor joined multi-line topics, since its row
had been cut at the first physical line and therefore matched the truncated
extraction. Both §4 defects were real and both were caught before any new row
was inserted; the final check joins continuation lines rather than comparing
first lines, which is the stricter of the two.

## 3. Changes made to `corpus/README.md`

1. Revision line 1.2 → 1.3 (`corpus/README.md:3`): records the ten-entry
   refresh, the landing window, and the two repairs.
2. Ten rows inserted, each verbatim from the landed entry's `- topic:` line,
   alphabetically placed: `language-shift-obsolescence-revival.md`,
   `numerals-and-measures.md`, `sound-symbolism.md` (linguistics);
   `direction-symbolism.md`, `divination-omen-systems.md`,
   `plant-symbolism.md` (myth-symbol); `transport-mobility-lexicon.md`,
   `vessel-container-lexicon.md` (culture-material);
   `header-conformance-readings.md`, `verification-independence-anti-circularity.md`
   (verification).
3. Partition headers re-counted: linguistics 16→19, myth-symbol 16→19,
   culture-material 16→18, verification 13→15; synthesis and civilizations
   unchanged at 24 and 94.
4. Total/counts block (`corpus/README.md:302`): 179 → 189 files; directory
   totals 19/19/18/24/15/94; a sweep line added naming the command's home in
   this fragment.
5. Known gaps (`corpus/README.md:228`): one round-10 bullet added — what
   landed, where the receipts live, the re-measured index, and the open
   questions the new entries state rather than close (header integrator
   question; round-9 open items). No earlier gap bullet was deleted or
   rewritten.

## 4. Drift this sweep found

1. **`africa-primary-sources.md` row was a paraphrase** (pre-existing). At
   21:29Z the row read "Bounded sub-Saharan primary-source map: Ajami
   manuscripts, oral-performance and language archives, …", which is not the
   entry's `- topic:` text; it was the one row of the 179 that did not match
   verbatim. Row replaced with the entry's current topic line; now at
   `corpus/README.md:134`. (The entry's own topic line is unchanged by the
   round-8 commit that last touched the file — `git show e1694ba --
   corpus/knowledge/civilizations/africa-primary-sources.md` contains no
   `- topic:` edit — so the divergence was on the row's side.)
2. **`phonetics-phonology.md` row was truncated** (pre-existing). The row
   stopped at the first physical line of a multi-line topic (`…— IPA`); it now
   carries the full topic (`…— IPA categories, inventory design, phonotactics,
   markedness, allophony, prosody/tone, environment & anatomy effects, conlang
   pitfalls`); now at `corpus/README.md:34`.
3. **`divination-omen-systems.md` was revised after landing.** The row copied
   from the file at 21:38Z said "a twelve-row technique typology"; the file was
   rewritten by its author ("fourteen-row") before the final sweep, which
   flagged the mismatch. Row re-synced at 21:39Z (`corpus/README.md:52`). A
   second author edit landed at ~21:41Z (file mtime after the 21:39:57Z sweep);
   the topic line was unchanged by it and the 21:41:19Z sweep still returns
   zero mismatches. This is the case that justifies re-running the sweep after
   the last landing rather than trusting the copy made at insert time.

## 5. Limits

- This fragment certifies index-vs-file correspondence only: every row names a
  real file, every file has a row, and each row reproduces that entry's own
  `- topic:` text. It says nothing about whether an entry is correct, sourced,
  or non-duplicative — reviewers R10-C11..C20 own that, and their verdicts sit
  in the sibling `review-*.md` fragments (at least one reviewer has already
  filed a source-resolvability defect against an entry; the index is
  unaffected by it).
- Counts are point-in-time (21:39:57Z, tree `e3a1ec9` plus uncommitted
  round-10 writes). Any later write to `corpus/knowledge/` invalidates them
  until the sweep is re-run.
- `divination-omen-systems.md`'s post-landing edit is direct evidence that
  entries can change under the index; the C-claim's own acceptance runner
  should re-run this sweep at close rather than cite this receipt as final.
- No commit was made and no file outside `corpus/README.md`, this fragment and
  `.scratch/` was written by this seat.
