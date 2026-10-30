# RevAppendOnly — round-79 W1 seat report

Seat: RevAppendOnly (reviewer). Scope: historical receipt/LOG/QUALITY append-only
preservation for the round-78 `census-end.txt` S884 used-by mismatch; expected digest
checking command for the Ca correction binding. Lane base
`44f76d456c1b326a71ffdb381590af825cbf11be` (worktree clean at base). No shared files
edited; no lane/fleet mutations; no subagent dispatch; no installs (git 2.56.0 system).

Deliverables under `.ufo/waves/round-79/w1/stage/RevAppendOnly/`:
- `digest-check-command.md` — the expected digest checking command + observed bound values.
- `findings.md` — full findings F1–F5 with evidence and hand-off kill rules.
- `probe/` — raw outputs of all runs (lane canonical block + 5 fixture controls + usage).

## Evidence summary (all read-only, raw output preserved)

1. **Mismatch confirmed, exactly one cell.** `census-end.txt:33` records S884 used-by
   `…/worldbuilding-setting-practice.amend-2026-10-24-r13.md`; registry row S884
   (`corpus/SOURCES.md:839`) at the measured round-78 revision
   `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` carries `…amend-2026-10-23.md` (same at
   base). `census-start.txt:33` is correct; the start↔end diff is the single line-33
   hunk; one S884 registry row at both revisions; receipt introduced by the single commit
   `4b255745`. The old-token path **never existed** in the lane (`git cat-file -e` → 128
   at both revisions) — missing-path class, matching routed defect 2 of
   `corpus/lessons/round-78-verifier-spotcheck.md`.
2. **Append-only preservation holds today.** Receipt blob `62eb55b77f44bf47c283c98c5645dd7141e98495`
   / sha256 `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867` / 3901 B,
   identical at `4b255745` and base. LOG.md and SCORECARD.md: 0 deletions
   `9fa0615c..44f76d45`; QUALITY criterion-25 marker text unchanged `f556d10`..base.
3. **Expected digest checking command** (exit 0 preserved / 1 in-place rewrite / 2 input
   error) delivered in `digest-check-command.md` §2 with observed values, plus token-binding
   checks §3 (old token count=1 in receipt; actual token count=1, old-token count=0 in
   registry row; never-existed path).
4. **Fixture probe (isolated repo `/fast/scratch/…/fixture-ao`, receipt bytes copied
   verbatim — identical blob):** green original PASS (exit 0); red in-place rewrite →
   `DIGEST: FAIL` (exit 1, both digests changed); green append-only correction (receipt
   untouched, LOG append 0 deletions) PASS; red lying correction binding the rewritten
   blob → `BINDING: FAIL`; non-commit revision → exit 2. Raw outputs in `probe/`.

## Findings for integration

- **F1** Correction must bind: git blob sha1 + sha256 of the receipt at measured revision
  `4b255745…`, old token verbatim, actual token verbatim. One digest alone is weaker.
- **F2** The correction records a missing-path drift, not mere string skew; ScribeCorrection
  should file it as missing-path class.
- **F3** LOG/SCORECARD round-29 entries append as new sections only (rounds 55/59
  precedent: filed rows are not edited); verified pattern: 0 deletions.
- **F4** Digest check cannot detect a lane history that replaces `4b255745` itself — only
  the externally recorded hash can (QUALITY 25's stated limit); noted, not closable in-lane.
- **F5** Fixture demonstrates checker shape on copied bytes; it is not a run of the
  round-79 counter (none exists at base — O/Ca are pre-freeze candidates).

## Tooling / hygiene

- Tools installed: none. Scratch `/fast/scratch/hyaku/kotodama-r79/RevAppendOnly/`
  removed after receipts copied to stage. No pacman; no PATH writes; no fleet-root writes.

Report trailer: `.ufo/waves/round-79/w1/RevAppendOnly.md` (this file),
stage `.ufo/waves/round-79/w1/stage/RevAppendOnly/` — both relative to lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
