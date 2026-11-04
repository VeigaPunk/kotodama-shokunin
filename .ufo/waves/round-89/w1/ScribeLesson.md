# ScribeLesson — round 89 w1 (scribe; axes freshness, coverage; milestone r89-v1)

Lane HEAD read: `9ad00be1` (wave spec commit on top of freeze `1cbd0efc`; `git diff --stat 1cbd0efc 9ad00be1` touches only `.ufo/waves/round-89/*` and `reports/round-89/at-freeze-{C,F}.txt`). `measure89.py` sha256 `6bc14bcd…` equals the freeze blob. No production file, git state or sibling path was written.

## Paths written

- `.ufo/waves/round-89/w1/stage/ScribeLesson/lesson-skeleton.md` — draft of `corpus/lessons/round-89.md`: title, `## Gate` (intro with the exact line shapes measure89 reads; rows left `<TBD>` for other seats), `## Understanding and trial`, `## Mistakes` (R89-M1..M3), `## R88 routed-defect dispositions` (R88-V1..V7), `## Settlement`.
- `.ufo/waves/round-89/w1/stage/ScribeLesson/readme-block.md` — README append block in the round-85 metallurgy shape (row / `Total knowledge entries: 261.` / footer with `python3 -B tools/check-corpus-index.py --root .` and `34/36/43/29/24/95`). It also covers the required heading bump `## linguistics/ (33)` → `(34)` and gives a one-liner that regenerates the row from the landed entry's `- topic:`.
- `.ufo/waves/round-89/w1/stage/ScribeLesson/log-entry.md` — LOG round-89 entry in the r88 style. Post-WAVE-DONE and final-measurement paragraphs are `<TBD>`.
- `.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/{index-dryrun.txt,redbefore-repro.txt,r88v3-controls-noenv.txt}`.

## Observed commands (rc)

- `env -u KOTODAMA_ROOT python3 -B tools/check-finding-sets.py … --candidate reports/round-88/controls/{shotgun-all-labels,extra-id}.py --json --work <scratch>` was run in the lane worktree and in a shared clone at `42816d25`. Each returned rc1 with passed 0/13, and every case had rc2. With `KOTODAMA_ROOT=<lane>`, extra-id scored 4/13.
- Running `extra-id.py --packet p.json --json` directly without the variable gives rc2: `can't open file '<lane>/reports/tools/check-attestation-packet.py'`. Root cause: `parents[2]` of `reports/round-88/controls/x.py` is `<lane>/reports`.
- Red-before reproduction: substituting the one occurrence of `out.append(leg('BACKED', not bad,` with `True,` gives mutant sha256 `80a8aa561cbe…`, which equals the value in `selftest-redbefore.txt`. `python3 -B measure89.py --selftest --work <scratch>` then returns rc1, `SELFTEST: FAIL 18/21`, with BAD = bumponly, wrongquote, badurl. This matches the committed receipt.
- Index dry run uses a shared clone at `9ad00be1`, a stub entry with the candidate topic, and the block appended. Without the heading bump: `CORPUS-INDEX: FINDINGS … ids=HEADER_DRIFT` rc1. With `(34)`: `CORPUS-INDEX: OK files=261 rows=261 findings=0` rc0. The row regenerator output is byte-equal to the appended row.
- Read-only checks: `git ls-tree -r --name-only 9ad00be1 reports/round-89` (no `separability89.py`); `reports/round-88/claims.json:34` D counter has no `--work`; `tools/check-gate-registry.py` scans only the entry-command cell for path tokens and requires 8 cells.

## Findings / unresolved defects

1. **R89-M2 (R88-V3 sharpened).** The r88 controls do not just *need* `KOTODAMA_ROOT` for reproducibility. Their fallback can never resolve a root, so without the variable they always score 0/13. The proposed SKILL pinned-values append text and SCORECARD note are in the lesson skeleton's R88-V3 row. The SKILL r88 prose line 43 ("otherwise depend on the live working tree or fail their fallback path") is half wrong; I propose no edit and only disclose it.
2. **R89-M3.** `claims.json` `separability` names `reports/round-89/separability89.py`. The file is absent at the freeze and at dispatch (`9ad00be1`). It is not a frozen leg. L1 must land it as labelled post-dispatch, or record that it was not built.
3. **C topic placeholder.** ScribeEvidentiality had staged nothing when I drafted, so the row topic in `readme-block.md` is a candidate. L1 must regenerate the row from the landed entry: the index tool flags TOPIC_MISMATCH otherwise.
4. **Red-before limits.** The red-before mutates BACKED only. Whether the other legs can fail rests on the negative scenarios. The mutant bytes are not committed, though they can be rebuilt by the one-string substitution.
5. The lesson cites my receipts at their stage paths. If L1 wants them durable outside `.ufo`, they must be copied under `reports/round-89/`.

Out of scope / not done: no F/C rows, captures, registry or entry content; no measured numbers (left `<TBD>`). No canon or lore decisions. Tools installed or upgraded: none. Scratch `/fast/scratch/hyaku/kotodama-r89/ScribeLesson/` was removed before yield.
