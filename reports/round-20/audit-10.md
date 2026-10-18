# R20-A10 — README-vs-files independent re-derivation: index rows, counts, and the verbatim-topic repair (NON-CANON)

- seat: R20-A10 (entry auditor, of R20-A09..A12). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- assignment (verbatim, my batch): *"AUDIT R20-A09..A12 (entry+handoff auditors x4):
  v3 packet adversarial pass; README-vs-files diff independent re-derivation;
  alias-wart negative re-runs; frozen replay audits."* This file is the second leg.
- date: 2026-10-18 (lane-local UTC−03:00; stamps UTC). Declared round-20 baseline
  `caf1beac…`; HEAD `122086b`; the round-20 README revision landed inside my
  window (first read 12:59Z at rev 1.4 + partial 1.5 header, settled read
  13:09Z at rev 1.5 sha256 `1a359d55387eef1a…`).
- role limits: this seat audits and reports. Writes: this file plus gitignored
  scratch under `.scratch/audit/` (two instruments + receipts). No `corpus/`
  byte is edited by this seat; no row is repaired; no commit.
- criteria (claim C, `reports/round-20/claims.json`): README reconciled against
  the actual partition contents with command-carried counts; every index row
  names an existing file; known gaps name only still-open gaps; zero filler.
- instruments (both stdlib-only, read-only):
  - `.scratch/audit/r20-readme-diff.py` — section/row census: declared heading
    counts, row counts, disk counts, missing rows, unindexed ("ghost") files,
    duplicates, rows outside partitions, totals line, counts line;
  - `.scratch/audit/r20-readme-topics.py` — **verbatim topic comparison**,
    replicating the round-10 convention (`reports/round-10/coverage/
    index-update.md` §2: row text = the entry's `- topic:` head-block, multi-line
    topics joined with single spaces). This is the dimension the round-19
    coverage tool explicitly does not check (`reports/round-19/audit/
    x27-coverage-readme-vs-files.md` §1: "does not verify that an indexed
    description matches its file's content").

## 1. Verdict

| reading (stamp) | rows vs files | missing / ghosts | topic mismatches (verbatim) | class |
|---|---|---|---|---|
| rev 1.4 = HEAD `122086b` (13:02Z, from `git show HEAD:corpus/README.md`) | 199 / 199 | 0 / 0 | **10** | rev 1.4's "0 topic mismatches" was asserted, not measured — confirmed |
| rev 1.5 live (13:09Z, sha256 `1a359d55…`) | 199 / 199 | 0 / 0 | **0** | repair verified |

Claim C's *substance* is **verified** at rev 1.5; two claim-text discrepancies
are reported in §4. All counts below are re-derived from the files, never read
from the README's own prose.

## 2. rev 1.4 — the ten-row defect, independently re-derived

`python3 .scratch/audit/r20-readme-topics.py <git-show-rev-1.4>` (13:02Z):

```
parts {'linguistics': 19, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 29, 'verification': 20, 'civilizations': 94} rows 199 files 199
missing_from_index 0 []   topic_mismatch 10 [...]   orphan_rows 0 []
```

The ten mismatches are exactly the ten round-19 entries: the five verification
(`label-channel-routing-verification`, `pre-declared-hold-set-reconciliation`,
`generated-artifact-roundtrip-verification`, `gate-battery-surface-verification`,
`two-reader-interop-agreement`) and the five synthesis
(`typed-label-routing-workflow`, `generated-artifact-lifecycle`,
`hold-set-contract-in-brief`, `era-material-scoped-reconciliation`,
`finding-disposition-workflow`). Spot-check of one row: rev 1.4's row for
`label-channel-routing-verification.md` read a condensed rewrite ("The
verification procedure for label channel routing: which channel a form-bearing
record's string is graded on (sound/identity, recipient-adapted borrow, or
none), the routing rows R1–R6, …") while the entry's own `- topic:` reads "The
verification procedure for **label channel routing**: given one form-bearing
record in a linguistic-cultural packet, decide which channel …". This
corroborates rev 1.5's own account (`corpus/README.md` revision block) and the
round-19 auditor's stated tool limit — the defect class was real, and the
round-10 sweep's "0 mismatches" claim for rev 1.3 was a different, narrower
comparison (round-10's sweep ran before the ten entries existed).

## 3. rev 1.5 — full re-derivation (13:09Z)

`r20-readme-diff.py`:

```
linguistics      declared=19  rows=19  disk=19  missing=[] unindexed=[] dupes=[]
myth-symbol      declared=19  rows=19  disk=19  missing=[] unindexed=[] dupes=[]
culture-material declared=18  rows=18  disk=18  missing=[] unindexed=[] dupes=[]
synthesis        declared=29  rows=29  disk=29  missing=[] unindexed=[] dupes=[]
verification     declared=20  rows=20  disk=20  missing=[] unindexed=[] dupes=[]
civilizations    declared=94  rows=94  disk=94  missing=[] unindexed=[] dupes=[]
rows_total=199 disk_total=199 declared_total=199 outside=0
declared counts line: 19/19/18/29/20/94 disk: [19, 19, 18, 29, 20, 94]
problems: none
```

`r20-readme-topics.py` → `missing_from_index 0 []`, `topic_mismatch 0 []`,
`orphan_rows 0 []`, exit 0. Every index row names an existing file; every file
is indexed exactly once; the counts line and the totals line match the disk;
the ten repaired rows are now verbatim from their entries' `- topic:` text.

Cross-check with the lane's own count command
(`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`,
run 13:0xZ): `totals.files 199` — agrees. (The command emits a per-file census;
this seat read the totals only.)

## 4. Discrepancies reported, not absorbed

1. **Claim C's declared counts are wrong on one cell.** `claims.json` C
   `after_required` names "linguistics 20"; the tree holds **19** `.md` files
   under `corpus/knowledge/linguistics/`, the README's own counts line says 19,
   and `source-audit-inventory.py` totals 199 = 94+19+19+18+29+20. Rev 1.5
   handles this honestly — its revision block records "the round-20 claim's
   declared linguistics 20 is not reproducible; the tree measures 19". The
   claim text itself remains as declared; the parent may want to note the
   discrepancy in the round report rather than silently reading the claim as
   satisfied.
2. **Claim C's "before" is stale in part.** The before-text says the index rows
   "lag the actual partition contents"; measured at rev 1.4 the rows/files
   counts were already exactly reconciled (199/199, 0 missing, 0 ghosts — my
   §2 run). The *real* lag was the description dimension (ten paraphrase rows)
   plus the known-gaps bullets (F5/F6), which rev 1.5 repaired. The claim's
   substance stands; its stated reason needed the topic-level measurement to
   be true.
3. **Known-gaps section.** Rev 1.5 edits the D2 typed-handling bullet
   (superseded; `d2-typed-labels.py` + `--selftest` 50/50 measured here) and the
   battery bullet (nine registered gates, measured `pass 7 / fail 0 /
   unevaluable 0`, exit 0 — this seat re-ran it at 13:00Z). The C05..C08
   gap-refresh (`reports/round-20/readme/gaps.md`) independently marks the
   frontier rows F1–F11 filled/open/stale with pointers; its F5/F6 readings
   agree with the README edits. This seat did not re-adjudicate every gap row
   (that is the C seat's evidence, read here, not re-derived); the
   row-existence and count dimensions are the ones re-derived in §2–§3.

## 5. Commands (all 2026-10-18; lane root)

```sh
git show HEAD:corpus/README.md > .scratch/audit/readme-r14.md   # rev 1.4 control
python3 .scratch/audit/r20-readme-topics.py .scratch/audit/readme-r14.md   # 10 mismatches
python3 .scratch/audit/r20-readme-topics.py                                # 0 mismatches
python3 .scratch/audit/r20-readme-diff.py                                  # 0 problems
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
```

Limits: the comparator checks row text against the entry's own topic line, not
the truth of the topic; counts are `.md`-only per partition; the known-gaps
dimension is read from the C seat's evidence plus this seat's spot checks, not
fully re-derived.
