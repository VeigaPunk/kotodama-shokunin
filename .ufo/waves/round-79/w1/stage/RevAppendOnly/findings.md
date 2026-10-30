# RevAppendOnly — fixtures & review findings (round-79 W1, seat RevAppendOnly)

Scope: historical receipt/LOG/QUALITY append-only preservation for the round-78
`census-end.txt` S884 used-by mismatch (CLAIMS-DRAFT Ca candidate), plus the expected
digest checking command for the correction binding. No shared files edited; no lane
mutations. Lane base `44f76d456c1b326a71ffdb381590af825cbf11be` (worktree clean at base).

## Findings

### F1 — mismatch is real, single-celled, and missing-path class (evidence)

- `git show 4b255745:reports/round-78/telemetry/census-end.txt` line 33:
  `S884 … used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`
- Registry `corpus/SOURCES.md` row S884 (line 839) at `4b255745`: used-by cell is
  `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`
  (identical at base `44f76d45`; row count for S884 = exactly 1 at both revisions).
- `census-start.txt:33` carries the correct `…10-23.md` token; the start↔end diff is
  exactly the one line-33 hunk. `git log --follow` on census-end.txt shows exactly one
  commit (`4b255745`). Matches `corpus/lessons/round-78-verifier-spotcheck.md` routed defect 2.
- The receipt's old token names a path that **never existed** in the lane:
  `git cat-file -e 4b255745:corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` → exit 128;
  the actual-token path exists. The drift is therefore missing-path class, not a mere
  string skew — the ScribeCorrection "warning vs missing-path error" distinction must land
  as missing-path.

### F2 — historical bytes are append-only-preserved today (evidence)

- Receipt blob `62eb55b7…` sha256 `05b5011a…` (3901 B) identical at `4b255745` and base.
- `git diff 9fa0615c..44f76d45 -- LOG.md` deletions: 0; same for SCORECARD.md: 0.
- QUALITY criterion 25 marker text ("Binds from round 74") present and unchanged at
  `f556d10` and base (append rule self-described at QUALITY.md criterion-23 addendum).
- Round-78 verifier confirms round-78 diff scope = LOG.md, SCORECARD.md, round-78 lesson,
  two telemetry receipts, 93 insertions / 0 deletions.

### F3 — the correction binding must carry four fields, all re-derivable (requirement)

Original receipt digest (git blob sha1 **and** sha256), measured revision (40-hex
`4b255745dea45a45d88b17e3c3fea4cdb6700cf7`), old token verbatim, actual token verbatim.
Checking commands and observed values: `digest-check-command.md` §2–§3. Both digests are
given because git sha1 alone is git-internal; sha256 is the fleet-report convention
(QUALITY 17 tree-hash style). A correction binding only one digest is weaker, not wrong.

### F4 — fixture probe results (isolated repo, raw outputs in `probe/`)

Fixture repo `/fast/scratch/hyaku/kotodama-r79/RevAppendOnly/fixture-ao` (git 2.56.0),
receipt bytes copied verbatim from lane `4b255745` (identical blob `62eb55b7…`).

| control | result |
|---|---|
| C1 green: original receipt at fixture round-78 analog commit `dcbf906b` | `DIGEST: PASS`, exit 0 (`probe-1-green.txt`) |
| C2 red: in-place rewrite of receipt line 33 (commit `cd3a76e3`) | `DIGEST: FAIL` both digests changed, exit 1 (`probe-2-red-inplace.txt`) |
| C3 green: append-only correction (commit `f097ba60` touches only new correction file + LOG append; receipt diff empty; LOG deletions 0) | digest PASS, bindings re-derive (`probe-3-green-append.txt`) |
| C4 red: lying correction binding the rewritten receipt's blob `770e5ebb…` | `BINDING: FAIL`, exit 1 (`probe-4-red-lying-binding.txt`) |
| usage: non-commit revision | exit 2 (`probe-usage.txt`) |

### F5 — limits (stated)

- The digest check proves the receipt **path** is byte-preserved at the measured revision;
  it cannot detect a rewritten lane history that replaces `4b255745` itself — only an
  external pin can (same stated limit as QUALITY 25's one-liner). The fleet report's
  recorded hash is the external anchor.
- The check guards the receipt only. Old/actual token bindings and the never-existed-path
  fact need their own legs (commands in `digest-check-command.md` §3); the round-79 Ca
  counter should re-run them rather than read correction prose (QUALITY 26's verify-by-
  re-running class).
- Fixture is a shape demonstration on copied bytes; it is not a run of the round-79
  counter (none exists yet at base — O/Ca are pre-freeze candidates).

## Tooling record

- No installs. git 2.56.0 (system). Fixture repo used git's bundled plumbing only.
- Scratch: `/fast/scratch/hyaku/kotodama-r79/RevAppendOnly/` — removed after receipts
  copied to this stage (`probe/`, `digest-check-command.md`).

## Hand-off notes for ExecCaCounter / ScribeCorrection / ScribeClaims

- Bind in the correction/ledger row: `receipt_blob=62eb55b77f44bf47c283c98c5645dd7141e98495`,
  `receipt_sha256=05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`,
  `measured_revision=4b255745dea45a45d88b17e3c3fea4cdb6700cf7`,
  `old_token=…/worldbuilding-setting-practice.amend-2026-10-24-r13.md`,
  `actual_token=…/worldbuilding-setting-practice.amend-2026-10-23.md`.
- Kill rules: in-place receipt edit → digest leg FAIL (C2); correction binding ≠ receipt
  blob at measured revision → binding leg FAIL (C4); do-nothing (no correction) fails by
  absence; a correction whose old_token ≠ receipt line 33 or actual_token ≠ registry row
  at the measured revision fails the token legs (commands §3).
- LOG.md/SCORECARD.md round-79 entries must be new appended sections (0 deletions —
  verified pattern from rounds 55/59 correction-row precedent: "the filed rows are not
  edited").
