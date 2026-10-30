# RevCaContract — round-79 W1 review report

Seat item: **Ca mismatch metric: original discrepancy remains historical; annotation must
not assert mismatch erased.** Lane base `44f76d456c1b326a71ffdb381590af825cbf11be`.
Read-only probe; no lane/fleet mutation. Raw probe output preserved at
`stage/RevCaContract/probe-r79-ca-mismatch.txt`; full contract at
`stage/RevCaContract/metric-contract.md`.

## Evidence (re-derived at base, verbatim in the probe)

- STATED token (`44f76d45:reports/round-78/telemetry/census-end.txt:33`):
  `used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`
- ACTUAL token (`4b255745dea45a45d88b17e3c3fea4cdb6700cf7:corpus/SOURCES.md` S884 row,
  line 839; identical bytes at base): `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`
- **MISMATCH=1 at base** — confirmed by the probe run.
- Original receipt binding material: blob `62eb55b77f44bf47c283c98c5645dd7141e98495`,
  sha256 `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`, committed at
  `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` (round-78 honest-stop lands — the recorded
  round-78 revision per `corpus/lessons/round-78-verifier-spotcheck.md:4`).
- The stated token was never present in the registry at ANY revision
  (`git log --all -S … -- corpus/SOURCES.md` empty) and the file it names was never
  committed. The `r13` suffix exists at base only under the heritage-taxonomy family
  (`heritage-taxonomy-models.amend-2026-10-24-r13.md`, S874/S875) — the receipt token is
  a chimera. Control: `census-start.txt` S884 line matches the registry (`…10-23.md`);
  the end receipt alone is anomalous (routed defect 2, same lesson :67).

## Finding 1 (the seat's core): two metrics, or history gets erased

The counter and the annotation must keep **two counts distinct**:

1. `mismatch` — historical, time-invariant, re-derived **at base = 1**. Both operands
   are immutable (append-only receipt; pinned registry revision). After the correction
   lands this count **must remain 1**. Any post-correction print of `mismatch=0`
   (without the `unresolved` qualifier) asserts erasure and is a lying correction under
   the draft's own failure modes.
2. `unresolved` — live, lands-derived: 1 at base (no correction), 0 after the
   append-only correction binds the four fields.

Resolution ≠ erasure: the correction closes the mismatch by binding truth to the
record; it does not delete the mismatch from history. This reading is the only one
consistent with the draft's "re-derives mismatch=1 at base and unresolved mismatch=0
after the new correction".

## Finding 2: the correction row's minimum binding

Four fields, each mechanically re-derivable at `<lands>`: original receipt digest
(path + blob + sha256), measured revision (`4b255745…`), old token, actual token — plus
re-derivation commands (QUALITY 12/27 shape). The counter must reject 1-, 2- and
3-field rows (J5 precedent: id-only correction rows fail ANNOTATE); a digest- or
revision-omitting row is the *partial-erasure* shape — the lane could later forget the
receipt was ever wrong while the count looks clean.

## Finding 3: failure-mode → leg mapping

| draft failure | leg |
|---|---|
| do-nothing | no four-field row at lands → `unresolved` stays 1 → FAIL |
| lying correction | any bound field ≠ frozen constant re-derived via `git show` at the named revisions → FAIL |
| wrong revision | row names a revision whose registry carried the stated token — none exists (probe §6); any other revision for these bytes → FAIL |
| changed receipt | receipt blob at lands ≠ `62eb55b7…` → APPENDONLY FAIL (J6 precedent) |

Constants read at `--freeze`, graded at `--lands` (QUALITY 25/26); the census receipts
carry no stamped revision, so the measured-revision binding is external to the receipt
(flagged below).

## Finding 4: review-only clause (QUALITY 11)

Whether the annotation *prose* asserts erasure is a wording judgment — named
review-only with a checklist in the stage contract: forbidden framings ("mismatch
erased", "mismatch corrected to 0", count resets); required framing (recorded
mismatch=1 historical; unresolved=0 after correction).

## Disposition observation (supports L1, outside my bounded item)

The sizing rule wants SCORECARD/SHONEN self-assessment mismatches. Observed: no
SCORECARD line and no `SHONEN.md` line states the r13 token for S884/worldbuilding —
the mismatch lives only in the census receipt. Per the CLAIMS-DRAFT pre-freeze
disposition, Ca is rejected before freeze and the correction lands as **unclaimed
conformance repair** (QUALITY 20: records repair → trends `unchanged`).

## Out-of-scope flag

Round-78 census receipts lack `# stamped revision` headers (criterion-17 gap) — why the
correction must pin `4b255745` externally. Census-tool header repair belongs to another
seat/round.

## Verification status

Only re-derivations actually run are claimed: probe legs 1–8 all executed read-only at
base/round-78 revisions on 2026-10-30 (raw output preserved). No counter selftest, no
fixture repository, no live fetches were run by this seat; no implementation checks are
claimed beyond the committed bytes read.
