# X22 — spot-check audit: the round-20 `corpus/README.md` rows, re-derived

- round 20 (operator loop 2 of 3, build round 4 of 4; 64 workers on
  `opencode-go/deepseek-v4.1-flash`) · seat **X22** (SCRIBE X21..X22 —
  spot-check auditors: v3 claims + README rows) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X21..X22: spot-check auditors (v3 claims +
  README rows)." This file is the README-rows leg; the v3-claims leg is
  `x21-v3-claims-spotcheck.md`.
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  declared baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`, HEAD
  `122086b` plus the live round-20 working tree.
- canon: NON-CANON engineering evidence. This audit admits no entry, certifies
  no round, judges no entry's quality or sources, and blesses no canon.
- writes: **this file only**; read-only instruments and receipts under
  `.scratch/` (`TMPDIR=$PWD/.scratch` exported for every command).
- measurement window 12:56Z–13:06Z UTC; the pin below binds to the README bytes
  measured at the stamp, and a later write to `corpus/README.md` or
  `corpus/knowledge/**` invalidates the readings until the sweep is re-run.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | 199 rows vs 199 files; **0 missing, 0 ghosts, 0 topic mismatches, 0 header drift** | **PASS** (13:05Z, sha `a20b6b26…`) |
| 2 | the ten round-19 rows repaired to byte-equal `- topic:` text | **PASS** (3 samples byte-equal; pre-state receipt shows exactly the ten) |
| 3 | counts vector `19/19/18/29/20/94` = 199, two independent methods | **PASS** |
| 4 | known-gaps: round-20 bullet present; three closures re-checked with commands | **PASS** |
| 5 | claim C's declared `linguistics 20` | **NOT REPRODUCIBLE** — the tree measures 19; the README records it |
| 6 | revision line's `--selftest` 39/39 reading | **dated 13:02Z, superseded in-round** by the O seat's 50/50 (note X22-N1) |

## 1. Method (independent instrument, pre/post controls)

The audit is this seat's own sweep, not a re-read of the C receipts:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/x22-readme-audit.py --receipt .scratch/x22-pre.json    # 12:56Z pre-state
python3 .scratch/x22-readme-audit.py --receipt .scratch/x22-final.json  # 13:05Z settled
```

`x22-readme-audit.py` parses every `- \`<file>.md\` — <topic>` row, joins each
entry's own `- topic:` head-block text (continuation lines space-joined),
compares byte-equal, checks `## <partition>/ (N)` headers, the totals block,
and the presence of the round-20 known-gaps bullet. Second method: the lane's
`tools/source-audit-inventory.py` plus a plain `find` count per partition.

**Pre-state control (12:56Z, sha `45627588…`):** 199 rows / 199 files, 0 missing,
0 orphan, **10 topic mismatches** — the ten round-19 rows (five synthesis, five
verification), e.g. `synthesis/era-material-scoped-reconciliation.md` carried a
condensed paraphrase (622 chars) instead of its 713-char topic. The C seat's
receipt measures the same ten (`reports/round-20/readme/reconcile.md` §2); the
repair is `reports/round-20/readme/verify.md` V3a/V3b.

## 2. Counts re-derived (two methods, 13:05Z)

| partition | README header | my `find` count | inventory | README vector position |
|---|---|---|---|---|
| linguistics | (19) | 19 | 19 | 1 |
| myth-symbol | (19) | 19 | 19 | 2 |
| culture-material | (18) | 18 | 18 | 3 |
| synthesis | (29) | 29 | 29 | 4 |
| verification | (20) | 20 | 20 | 5 |
| civilizations | (94) | 94 | 94 | 6 |
| **total** | — | **199** | **199** | `19/19/18/29/20/94` |

The counts block states the command
(`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`),
a date (2026-10-18), and the vector; the vector equals the disk counts in the
README's own section order, and the `Total knowledge entries: 199.` line equals
the file total. No count in the block is un-dated.

## 3. Rows vs files (the C02 requirement, re-derived)

At 13:05Z (sha `a20b6b26…`): `missing_from_index []`, `orphan_rows []`,
`topic_mismatch []`, `header_drift {}`. Every row names an existing file; every
file has exactly one row; every row is byte-equal to its entry's `- topic:`
text. Spot-check samples re-verified byte-equal:

- `synthesis/era-material-scoped-reconciliation.md` (713 chars) — repaired;
- `verification/two-reader-interop-agreement.md` (699 chars) — repaired;
- `synthesis/typed-label-routing-workflow.md` (658 chars) — repaired.

## 4. Known gaps (the C03 requirement, re-derived)

The round-20 bullet is present and names the closures and the still-open rows.
The three closures it claims were re-checked with commands:

| closure claimed | control run by this seat | observed |
|---|---|---|
| gate battery registers nine gates; coverage 9/9 | `python3 tools/check-gate-battery.py` | exit 0; duty 1 `{battery_exit 0, pass 7, fail 0, unevaluable 0}`, originals 30/30 preserved; duty 2 `baselines_found 17, coverage "9/9", gates_registered 9, gates_uncovered [], pinned 17` |
| per-gate `expected.json` layout shipped | `ls tools/gates/{expected,frozen}/` | `expected/` 4 gate dirs, `frozen/` 7 gate dirs (+4 round dirs); the residues the gap file names (three live roots; round-4 unpinned) remain stated, not absorbed |
| D2 typed-handling bullet superseded | `tools/d2-typed-labels.py` exists; `--selftest` | exit 0, **50/50** checks at 13:04Z (see X22-N1) |

The still-open rows were spot-checked: `d4-assembly-check-gate.py --selftest`
→ exit 2 `No such file or directory: '--selftest'`; `reports/round-7/validation.json`
`acceptance_checks_passed` → **false**; both match the README's statements.
No closed item was found still described as open, and no open item was found
described as closed on this sample.

## 5. The claim-vs-tree discrepancy (claim C, verbatim)

Claim C's `after_required` declares "command-carried counts: civilizations 94,
**linguistics 20**, myth-symbol 19, culture-material 18, synthesis 29,
verification 20". The tree measures **19** linguistics files; the declared six
numbers sum to **200** against **199** files. The README does not absorb the
number: revision 1.5 records "the round-20 claim's declared linguistics 20 is
not reproducible; the tree measures 19" and carries the measured vector. The C
seat's gap refresh reached the same reading independently
(`reports/round-20/readme/gaps.md` §0, item 1), and the round draft records it
(`reports/round-20/report-draft.md` §1). **The claim's parenthetical count is
not reproducible at this stamp; the reconciliation itself is against the actual
partition contents and is verified.**

## 6. Notes and findings

- **X22-N1 — the revision line's dated `--selftest` count is superseded inside
  the same round.** Revision 1.5 says "`--selftest` 39/39 measured 2026-10-18
  13:02Z". The O seat's per-family alias change to `tools/d2-typed-labels.py`
  landed minutes later and grew the selftest to **50/50** (measured 13:04Z,
  exit 0, including mirror checks: "the mirror build is byte-identical to the
  filed d4 projection"). The count is honestly dated, but a reader at round
  close sees a stale number for the live tool. Disposition: re-measure the
  count (or re-stamp it) before the round closes; this audit does not edit the
  README.
- **X22-N2 — the README was a moving target during the wave.** Shas measured by
  this seat inside ~9 minutes: `45627588…` (pre) → `51da21d4…` → `a8846ddd…` →
  `fa167121…` → `a20b6b26…` (watcher also saw `a9675ebf…`). Every reading above
  binds to `a20b6b26…`; a later write invalidates them.
- **X22-N3 (out of seat scope, reported not touched).** Filed
  `reports/round-{5,7,9}/validation.json` were transiently modified in the
  worktree during the wave (old runners refresh their receipt in place) and
  were restored by 13:04Z (`git diff` empty for all three). The README's
  round-20 bullet now records the same class of drift for the round-5/6
  runners. No filed byte was touched by this seat.

## 7. Limits

- **Same-convention.** The verbatim `- topic:` convention is the lane's
  round-10 convention; this audit re-runs it rather than re-justifying it.
- **Correspondence only.** "Verbatim" means the row equals the entry's own
  topic text; nothing here certifies an entry's quality, sources or canon.
- **Point-in-time.** The pin is `corpus/README.md` sha256
  `a20b6b263f089364dbfa236afdca58f160954d03d2ef9822c9540ef8ef584f7b` measured
  2026-10-18T13:05Z. The C seat's own verification is same-seat
  (`verify.md` §5 says so); this file is the independent-seat re-measure and
  still does not judge the entries themselves.
- The round's counting command `python3 reports/round-20/run-validation.py`
  did not exist at this stamp; no reading here is a runner verdict.

### 2026-10-18T13:25Z — post-stamp movement and the runner reading

`corpus/README.md` moved `a20b6b26…` → `1a359d55…` after this audit's 13:05Z
stamp (the C seat continued refining the known-gaps text). Re-measured on
`1a359d55387eef1aebd79316a7bf19d53a2ac6f0bcacb1cd109bdeff1294e7ce` at 13:25Z
with the same instrument (`--receipt .scratch/x22-post-stamp.json`): rows 199 /
files 199, 0 missing, 0 orphan, **0 topic mismatches**, 0 header drift, counts
vector `19/19/18/29/20/94` equal to disk, round-20 known-gaps bullet present —
**unchanged on every leg**, so the verdict above carries to the newer bytes.
The round's counting command now exists (`reports/round-20/run-validation.py`)
and its read-only `--check` run (revision `d6fee0ce…`, 13:20Z) reports claim C
**pass** with the declared-vs-live linguistics delta documented in the README
(`declared_deltas: [{partition: linguistics, declared: 20, live: 19,
documented_in_readme: true}]`), consistent with §5 above.
