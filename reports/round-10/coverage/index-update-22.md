# R10-C22 — index backup: independent re-run of the index-vs-files sweep after C21

- seat: R10-C22 (index backup). lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  assignment: *independently re-run the index-vs-files sweep after C21; diff your
  result against C21's; `reports/round-10/coverage/index-update-22.md`.*
- date: 2026-10-17, local clock UTC−03:00; all times below UTC. Post-C21 sweep
  run 21:41–21:44Z; final receipts stamped 21:43:51Z.
- revision binding: worktree HEAD `e3a1ec9` ("round-10: availability attempt 3");
  declared round-10 `baseline_revision` `9dc18ec1339bffd6f81e74f1a5742464ef578749`.
  No commit was made by this seat.
- artifacts diffed: `reports/round-10/coverage/index-update.md` (R10-C21),
  sha256 `fc106c246bb013522a3509b933e12395bb895f84f1b3e2043799aaeca1569718`;
  `corpus/README.md`, sha256
  `9df4b7c579b89d6ff51ace4600cb0518b897d2e6d0819150e3fde6bbf5b8333c`.
- role limits: this seat counts and diffs. Its only writes are this fragment and
  `.scratch/` scratch (untracked, disposable). It edits no corpus file, admits no
  entry, judges no entry's quality or sources (R10-C11..C20 own that), and does
  not absorb C21's evidence as its own: the numbers below come from an
  independent re-implementation, not from C21's script or receipts.

## 1. Independent sweep — method

Instrument `.scratch/r10-c22-sweep.py` (sha256
`ee7d53a85e80d144f04094b0114e4081f20d048a67a9a38c16d37e8952d02fad`), written
from the README/file layout, not derived from C21's tooling. It lists
`corpus/knowledge/*/` files, bounds README sections at **every** `## ` header,
parses `## <partition>/ (N)` headers and `- \`<file>\` …` rows, and reports per
partition: `files`, `index_rows`, `header_count`, `non_md_files`,
`files_missing_from_index`, `index_rows_without_file`, `duplicate_rows`,
`rows_pointing_to_other_partition`, `rows_without_description`,
`rows_out_of_alphabetical_order`, `directory_without_readme_section`; plus
totals (`actual_files`, `index_rows`, `sum_header_counts`, `declared_total_line`,
`declared_dir_counts`, `revision_line`, `global_duplicate_rows`). Exit 0 iff zero
problems. JSON receipt: `.scratch/r10-c22-post.json`, sha256
`3cf041174bf5d7bafe5ea509a5bccd79aa515e6267c16cd937bc6d7302da998f`.

Command (from the lane root):

```sh
python3 .scratch/r10-c22-sweep.py    # exit 0 on the post-C21 tree
```

## 2. Independent sweep — result on the post-C21 tree

```
readme sha256 9df4b7c579b89d6ff51ace4600cb0518b897d2e6d0819150e3fde6bbf5b8333c
verdict consistent, problems []  (exit 0)
files 189  index_rows 189  sum_header_counts 189  declared_total_line 189
declared_dir_counts [19, 19, 18, 24, 15, 94]   global_duplicate_rows []
civilizations 94/94/94   culture-material 18/18/18   linguistics 19/19/19
myth-symbol 19/19/19     synthesis 24/24/24          verification 15/15/15
(files / rows / header; every partition: 0 missing, 0 phantom, 0 duplicate,
 0 unordered, 0 rows without description)
```

Independent count cross-check with the README's own declared command (run
21:43Z, exit 0, receipt `.scratch/r10-c22-inventory-post.json`, sha256
`562c94ced5efa937abb4c5af6f8f58a810192120d809060463eea6f1558aa000`):

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files = 189; totals.marker_occurrences = 633
```

Both agree with the README's counts block (`Total knowledge entries: 189`;
`(total 189 files; directory totals 19/19/18/24/15/94)`) and with revision 1.3.

## 3. Diff against C21's result

C21's `index-update.md` §2 final run (21:39:57Z) declares:
`parts {linguistics 19, myth-symbol 19, culture-material 18, synthesis 24,
verification 15, civilizations 94} rows 189 files 189; missing_from_index 0;
topic_mismatch 0; orphan_rows 0`.

| check | C21 (21:39:57Z) | mine (21:41–21:44Z, sha `9df4b7c5…`) | diff |
|---|---|---|---|
| files / rows / headers | 189 / 189 / n/a | 189 / 189 / 189 | none |
| partition totals | 19/19/18/24/15/94 | 19/19/18/24/15/94 | none |
| files missing from index | 0 | 0 | none |
| index rows without file (orphans) | 0 | 0 | none |
| row text == entry `topic:` text | 0 mismatches | 0 mismatches (§4) | none |
| declared total/counts line | 189; 19/19/18/24/15/94 | same, parsed and compared | none |
| duplicate rows (per-section, global) | not checked | 0 | extra, clean |
| rows without description / ordering | not checked | 0 / 0 unordered | extra, clean |

The one place my instrument initially diverged from C21 was my own parser: its
counts-line regex expected the pre-round-10 wording ("directory totals
**remain** 16/16/16/24/13/94") and returned `declared_dir_counts None` against
C21's new wording. That was an assumption in my tool, not a defect in C21's
edit; the regex was widened and the tamper control re-run (§6, r5/r6). Beyond
that, two independently written implementations agree on every count.

## 4. Independent reproduction of C21's topic-fidelity claim

C21 §2 asserts the stronger convention: every row reproduces its entry's
`- topic:` head-block text (continuation lines joined with single spaces), and
that applying it to the pre-round-10 README matched 177 rows exactly and exposed
2 defects (§4: `africa-primary-sources.md` paraphrase, `phonetics-phonology.md`
truncation). I re-implemented that check independently
(`.scratch/r10-c22-topic-fidelity.py`, sha256
`85a9eadf3a3a17d1beb1930061cec034c0b826eb89707cdf97d643a9b220b937`) and ran it
against both README revisions:

```
POST (current, rev 1.3): rows=189 checked=189 mismatch=0   (exit 0)
PRE  (HEAD:corpus/README.md, rev 1.2): rows=179 checked=179 mismatch=2
  MISMATCH africa-primary-sources.md
    row   : ...'Bounded sub-Saharan primary-source map: '
    topic : ...'primary-source landscapes for sub-Sahara'
  MISMATCH phonetics-phonology.md
    row   : ...'speech sounds and sound systems for fictional cultures — IPA'
    topic : ...'s for fictional cultures — IPA categories, inventory design, phonotact'
```

That is 177 exact matches plus exactly the two defects C21 names, with the same
divergence points. C21's repairs and its convention claim are therefore
reproduced, not merely accepted.

## 5. The ten new rows

The ten round-10 entries verified here (each the only untracked corpus file of
its name; sha256 at 21:44Z):

| new entry | partition | sha256 |
|---|---|---|
| `language-shift-obsolescence-revival.md` | linguistics | `89d2a225dd709a7947c4f9d967ffd6ce858f784bfef10f581b11a863dc6c8315` |
| `numerals-and-measures.md` | linguistics | `57fc76695c9fed38cf87ddccbaf7e5c5d322125f65b98aea154baf5046129340` |
| `sound-symbolism.md` | linguistics | `4f14b05a7df542ad5e3dca39c20cb02dc3f5745c70395418770da93794fddd5d` |
| `direction-symbolism.md` | myth-symbol | `5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426` |
| `divination-omen-systems.md` | myth-symbol | `6666e7dbd5cc5a4bd9833b3e842843854af8ef7b365396c6d1737aac8cbf2ba4` |
| `plant-symbolism.md` | myth-symbol | `a9fd5e8fc2b005293569b9bd7225a4a42002183458aa7e36ece147793623d63f` |
| `transport-mobility-lexicon.md` | culture-material | `36a7370ff49cda98030cc978c059c23fbc32d86eec690bcf0caa5555d66ad272` |
| `vessel-container-lexicon.md` | culture-material | `073e7fc54b600a81a75e0db480f73597e2295f8daa317a74e9246846b5de2df3` |
| `header-conformance-readings.md` | verification | `d627eba3b99f56933b6eae2ab1339013be57da30a5e5608b4d75ddb7f36feb90` |
| `verification-independence-anti-circularity.md` | verification | `743bce544c888a9159728af4b6f5dcecb98166adc3a77d30e7794b5d711d0cff` |

All ten were checked per-row (`.scratch/r10-c22-newrow-check.py`, sha256
`e904858e2318f6bbbfb86ac4ebf905f12d1be92a86053ce0861c7d4133d9b33f`): each row
sits in its entry's partition section, description length 554–2523 characters,
no description shared with any other row, and description/topic overlap ≥ 6
words. All ten pass; the full-text equality check in §4 is the binding one.
`numerals-and-measures.md` exercises the multi-line joining rule (its topic's
first physical line is 11 words; the row carries the joined 126-word topic) —
both my check and the fidelity run agree.

Timing edge worth recording: `myth-symbol/divination-omen-systems.md` carries
mtime 21:41:20Z — **after** C21's 21:39:57Z final sweep. This matches C21 §4.3's
account of a post-landing author rewrite and row re-sync, and it is exactly the
case its §5 flags as invalidating point-in-time counts. My checks, run after
that write, re-certify the index against the newer bytes: fidelity 0/189
mismatches, divination file sha256
`6666e7dbd5cc5a4bd9833b3e842843854af8ef7b365396c6d1737aac8cbf2ba4`. The
backup sweep is thus not a re-run of the same instant but a later certification.

Landing window independently measured from file mtimes (UTC): first
`verification/header-conformance-readings.md` 21:31:46Z, then 21:32:36,
21:33:06, 21:33:47, 21:36:19, 21:36:51, 21:38:07, 21:38:19, 21:38:48, and last
`myth-symbol/divination-omen-systems.md` 21:41:20Z — consistent with C21's
21:31:46–21:38:48 window plus that one later rewrite.

Live in-flight detections (my instrument ran through the wave): at ~21:30:47Z it
reported `verification: 14 files vs 13 rows` (1 missing row, stale dir totals,
stale total line, exit 1); at ~21:35Z, 8 missing rows across
culture-material/linguistics/myth-symbol/verification (exit 1); at 21:41Z+ the
tree is consistent (exit 0). README sha transitions observed on a 20 s watcher:
`9cf3beae` (baseline) → `e998910e` 21:28:39Z (africa row repair) → row
insertions 21:37:08Z–21:39:48Z → `9df4b7c5` from 21:40:08Z, stable through
21:44Z. `corpus/README.md` mtime 21:39:51Z.

## 6. Controls

Eight planted defects in `.scratch/plant/`, each run through the same sweep;
all detected with exit 1 and the expected problem class:

| control | planted | detected as |
|---|---|---|
| r1 | row deleted | `linguistics: 1 files missing from index` |
| r2 | phantom row added | `verification: 1 index rows without file` |
| r3 | header count 16→17 | `linguistics: header (17) != rows (15)` |
| r4 | total line 179→178 | `README total line (178) != actual files (179)` |
| r5 | dir totals 94→93 (old wording) | `declared dir totals … != actual …` |
| r6 | dir totals 94→93 (rev-1.3 wording) | same class on the new wording |
| r7 | two rows swapped | `linguistics: rows not in alphabetical order` |
| r8 | row description stripped | `myth-symbol: 1 rows without description ['trickster.md']` |

Positive control: the real tree returns `consistent`, exit 0 (§2). Instrument
defect self-caught and fixed before any verdict was filed: the first version
bounded sections only at `## <p>/ (N)` headers, so the `## Known gaps` bullet
``- `python3 tools/replay-frozen.py …` `` leaked into the civilizations section
as a phantom row (95 rows / 94 files). Fix: bound at every `## ` header; the
pre-C21 baseline then returned 179 = 179 = 179 = 179, exit 0.

## 7. Limits

- Point-in-time: README sha `9df4b7c5…`, 189 corpus files, 21:44Z 2026-10-17.
  Any later write to `corpus/knowledge/` or `corpus/README.md` invalidates these
  counts until the sweep is re-run.
- Scope: index-vs-file correspondence and row/topic text only. Nothing here
  certifies an entry's correctness, sourcing, or non-duplication; reviewers
  R10-C11..C20 own that, and the C-claim's acceptance runner should re-run this
  sweep at close rather than cite this receipt as final.
- `divination-omen-systems.md`'s intermediate history is uncommitted and not
  reconstructible; I certify the end state only (row == topic on current bytes),
  which is consistent with C21's account.
- Agreement with C21 is two independent implementations agreeing on the same
  tree, not a byte-identical tool comparison; C21 additionally records the
  pre-repair runs of its own sweep, which I did not re-execute (my pre-state
  reproduction in §4 uses the committed rev-1.2 README instead).
- Reported, not dispositioned (outside this seat, no action taken): the
  worktree carries rewritten `reports/round-5/validation.json` and
  `reports/round-9/validation.json` bytes against HEAD, which round-10's F
  targets say should not be rewritten in place; sibling
  `reports/round-10/coverage/review-C04.md` §2 filed the same observation. The
  parent owns that call.

## 8. Interaction with the acceptance runner (reported, not self-served)

`reports/round-10/run-validation.py` (read at 21:44Z) classifies coverage
fragments as `review-*`, `audit-*`, or "authorship" — exempting only the exact
name `index-update.md` (lines 493–499). This fragment's mandated name
`index-update-22.md` therefore lands in its `authorship` bucket and would count
toward the `C_MIN_ENTRIES` authorship threshold if left as is; it is not an
authorship fragment. This seat did not rename or edit anything to suit the
runner (its name is fixed by `reports/round-10/targets.json`), and did not
modify the runner. The parent should either widen the runner's exemption to
`index-update*.md` or discount one authorship slot.

Also disclosed: this seat invoked that runner once (21:44:36Z) to read its
checks; the runner rewrites `reports/round-10/validation.json` as its own
output on each run, so that file's bytes are now a 21:44:36Z regeneration of
the same script over the same tree, not X03's earlier run. No source file was
changed by that invocation.
