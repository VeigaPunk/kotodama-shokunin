# Round 18 — Scope watch (SCRIBE X02)

- **Date:** 2026-10-18. **Regimen:** operator loop 2 of 3, build round 2 of 4
  (64 workers, `opencode-go-2/deepseek-v4.1-flash`, per `claims.json`).
- **Lane state at check time:** HEAD `c66ac3c`
  ("round-18: declare claims O/D/C (gate generalization, D4 gate verification,
  civ-map revision)", 2026-10-18 07:17:35 -0300); baseline `3dd3754`
  ("round-17: C/O verified; D rejected …") is HEAD's direct parent
  (`git rev-parse HEAD^` = `3dd3754207032cb81f5fb3e202fe85cf79211339`).
  `claims.json` state: `declared-before-dispatch`.
  Observation window: ~07:19–07:24 -0300 (before/after snapshots bracketing
  the start of the worker wave).
- **Verdict: IN SCOPE AND CLEAN, with two informational findings and one
  closure observation.** Fleet root
  clean; filed rounds 8–17 (including the rejected round-17 bytes) byte-stable
  across the observation window; the claim-O re-pin targets are pinned and
  unchanged; PROVINCE accurate. Nothing absorbed, nothing repaired in place.

## 1. Fleet root clean

`git status --porcelain=v1` in `/home/vgpnk/Projects/shokunin` → empty
(0 lines, checked twice, 2026-10-18 07:19 and 07:23 -0300). Fleet HEAD
`35b17a60bd91ac8710c61ec731da969d7a52ede2` "close kotodama round-17:
REJECTED on D (gate D2-bound); C/O verified", 2026-10-18 07:16:51 -0300.

Sibling sweep (read-only, `git -C <lane> status --porcelain=v1 | wc -l`,
2026-10-18): 19 of 20 lane repos clean (`dirty=0`). `lore-shokunin`
`dirty=2` — out-of-lane, reported as F-X02-1, never touched from here.
`kotodama-shokunin` itself reported `dirty=0` in the same sweep, consistent
with the full-status checks in §2.

## 2. Filed rounds 8–17 untouched (incl. the rejected round-17 bytes)

Scope of this check: every file under `reports/round-8` … `reports/round-17`
(the filed-round surface), plus the specific filed pin artifacts that
round-18 claim O names as its re-pin cascade targets
(`tools/gates/frozen/round-11/**`, `tools/gates/expected/**`,
`reports/round-16/handoff/expected-v2-07.json` and its packet pair).
Living tooling that claim O legitimately generalizes (e.g.
`tools/gates/typed-pipeline-gate.py`) is not a filed receipt of rounds 8–17
and is not part of this "untouched" set by design; only its pinned
receipts/frozen artifacts are.

**Method (all commands 2026-10-18, `TMPDIR=$PWD/.scratch`).**

1. **Working-tree cleanliness.** `git status --porcelain=v1` over the whole
   lane → empty at both observation points (before and after the worker
   window); over rounds 8–17 → empty; `git ls-files --others
   --exclude-standard` over rounds 8–17 → 0 untracked; no diff vs HEAD.
   So on-disk bytes equal committed bytes throughout.
2. **Commit hygiene.** Only two commits landed since the round-16 admit
   `f30b6f8`: `3dd3754` (round-17 close) and `c66ac3c` (round-18 declare).
   `git diff --name-only 3dd3754^ 3dd3754 -- reports/round-8 … reports/round-16`
   → empty (the r17 close filed `reports/round-17/`, corpus, examples, tools,
   SCORECARD and LOG, zero paths under rounds 8–16).
   `git diff --name-only c66ac3c^ c66ac3c -- reports/round-8 … reports/round-17`
   → empty; `git show --stat c66ac3c` touches exactly
   `reports/round-18/claims.json` (+32) and `reports/round-18/targets.json`
   (+11).
3. **Cross-round byte proof.** `reports/round-17/validation.json` records the
   filed baseline of rounds 8–16 as 694 per-file sha256 rows at baseline
   `f30b6f8`. Recomputing every row against current on-disk bytes
   (2026-10-18): **694 match / 0 mismatch / 0 missing** — no filed byte of
   rounds 8–16 has changed since it was recorded, across the round-17 close
   and into this round.
4. **Byte snapshot over the window.** 766 files under rounds 8–17
   (canonical digest = sha256 of the `LC_ALL=C sort -z` path-ordered
   `sha256sum` listing):
   **`c0594947a34c413c92ad08e000707a7c066b03428d6c14c2b06fcb9bb4787788`
   identical before and after the observation window** (set-diff: 0 changed,
   0 added, 0 removed). With `*.log` and `__pycache__/` excluded — the filed
   filter used by round 17's runner ("git-ignored scratch logs are not filed
   bytes") — 761 files, digest
   `a2b92453c7a73c884eb0676bfac3f7b8ed0f7abebb0175e11f5a605fe294d6a1`.
   `find … -links +1` over rounds 8–17 → empty: no filed file is hardlinked
   (scratch mirrors cannot leak writes into filed bytes through links).
5. **Round-17 specifically (the rejected round's bytes).** 67 files on disk,
   67 tracked, 0 modified vs HEAD, per-round digest
   `4a65327bdff87a4d8544b5a28e229fc168e9b70c642b07146467dbbddb07fc6a`
   (= the `3dd3754` blobs). The D rejection is a verdict recorded in
   SCORECARD/LOG and at fleet HEAD `35b17a6`; it changed no filed byte of
   `reports/round-17/`.
6. **Re-pin targets pinned before/after.** All hash lines in
   `.scratch/x02-pins-before.txt` vs `.scratch/x02-pins-after.txt` are
   identical (the only diff is this scribe's own header lines). Spot values:
   `tools/gates/frozen/round-11/MANIFEST.tsv`
   `aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063`;
   `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json`
   `c49ebc9e71ce870af621604bb0e00886b45ad8f4028777f202ec845ede6cc902`;
   `reports/round-9/baselines/handoff-packet-check/expected.json`
   `9dc21cd508e3dcfb225564cdccf65a8f88d9768029e876ac7e47d4c55f21c690`;
   `reports/round-16/handoff/expected-v2-07.json`
   `dc75c5d7e347987e81efe6f6fe17314e8f6a2ce26a12a1ca7ec3567a21dcaad1`
   (`frozen_by` R15-O08, pins gate stdout sha and census — the helper-pinned
   expected file claim O names); packet pair
   `717e29e5…`/`1295f5b3…`. Any in-place re-pin during this round would have
   registered here as drift; none did during the window.

Per-round digests at both observation points (unchanged): round-8 153 files
`9628e733…`, round-9 90 `15491acc…`, round-10 73 `09b18616…`, round-11 254
`a54cc844…`, round-12 44 `35172dcf…`, round-13 2 `2b5810bf…`, round-14 40
`2a289ea4…`, round-15 20 `a166b03e…`, round-16 23 `a00ee933…`, round-17 67
`4a65327b…` (full hashes in the digest above; a round-11 typed-pipeline live
mirror exists only under `.scratch/r18-o11*`, git-ignored — see F-X02-2).

This re-checks the round-12 receipt-clobber defect class
(`reports/round-12/defects/ledger.json` FRR-12a/b): no filed receipt was
overwritten, and the append-only rule (re-pins as new rows/files, never
in-place edits) held through the observation window.

Post-window observation (07:25:54 -0300): other round-18 workers began
landing deliverables as **new untracked files** — `reports/round-18/gate/`,
`examples/culture-d4/expected-holds.json`,
`tools/gates/d4-assembly-check-gate.py`,
`tools/gates/d4-typed-labels-check-gate.py`, `corpus/lessons/round-18.md`.
Re-run at that moment: filed rounds 8–17 aggregate digest still
`c0594947…` (set-identical) and `git status` over rounds 8–17 still 0 lines.
In-flight landing is confined to new files; no filed round byte has moved.

## 3. PROVINCE accurate

Checked 2026-10-18 against `PROVINCE.md` (committed, unmodified since
`c53782a`, 2026-10-17; `git diff HEAD -- PROVINCE.md` empty):

- **Owned partitions all exist (6/6):** `ls corpus/knowledge/` →
  civilizations, culture-material, linguistics, myth-symbol, synthesis,
  verification.
- **Civilizations count = 94:** `ls corpus/knowledge/civilizations/ |
  grep -c '\.md$'` → 94 (unchanged by round-17 C's seven fixed entries).
- **Adjacent contract file exists:**
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`.
- **Refuses/adjacency consistent:** the round-18 claims (O: this lane's own
  typed gate + re-pin cascade; D: non-canon `examples/culture-d4/` gate
  verification; C: civ-map revision in the owned civilizations partition)
  all sit inside the owned partitions and the "own gates / non-canon
  examples / reports" clause. No claim asserts canon, lore acceptance,
  cultural permission or real-world clearance. Lane root carries the
  bookkeeping PROVINCE implies: LOG.md, MINT.md, SCORECARD.md, SHONEN.md,
  SKILL.md, README.md, AGENTS.md.

## 4. Round-18 declaration coherence

- `claims.json` and `targets.json` agree on round (18), date (2026-10-18),
  and baseline (`3dd3754207032cb81f5fb3e202fe85cf79211339`).
- **Worker arithmetic closes:** `claims.json` declares `workers: 64`;
  `targets.json` allocates O-generalization 20 + D4-gate 28 + C-map 10 +
  X 6 = **64**. The round-17 discrepancy (declared 64 vs 60 seats,
  `reports/round-17/scope.md` F-X02-1) does not recur — noted as F-X02-3.
- Claim ids/axes O/operability, D/depth, C/coverage; `state:
  declared-before-dispatch`; all three claims share the counting command
  `python3 reports/round-18/run-validation.py`.
- Expected-absent pre-dispatch artifacts (deliverables, not defects):
  `reports/round-18/run-validation.py` does not exist yet (this scribe's
  watch confirms the directory holds only `claims.json` and `targets.json`);
  the claim-D input tree `examples/culture-d4/` (17 files) is present from
  round 17 as declared.

## 5. Findings — reported, not absorbed

- **F-X02-1 (out-of-lane, informational):** `lore-shokunin` working tree is
  dirty (2 lines, 2026-10-18): `?? .scratch/` and
  `?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`.
  Recurring class (r16 F-X02-1, r17 F-X02-2); cause/disposition are lore's
  own scope, left untouched.
- **F-X02-2 (scratch usage, no action):** this round's claim-O workers keep
  live mirrors of filed rounds under `.scratch/` (e.g.
  `.scratch/r18-o11/mirror-live-t0/reports/round-16/handoff/…`). Verified
  compliant: `.scratch/` is git-ignored (`.gitignore`), the mirrors are
  copies (no hardlinks into filed rounds), and the filed bytes of rounds
  8–17 plus the re-pin pins were byte-stable across the window — the
  re-pin/replay work is not touching filed bytes in place.
- **F-X02-3 (closure observation):** round 17's worker-arithmetic
  discrepancy does not recur (§4). r17's F-X02-3 historical round-3
  manifest replay pin (exit 2 on later-fixed gates) remains the recorded
  historical-pin class; not re-run by this scribe (read-only watch; claim-O
  owners hold frozen-replay verification).

## 6. Commands (all run 2026-10-18, ~07:19–07:24 -0300)

- `git status --porcelain=v1` — lane (empty, full) and fleet root (empty),
  at both observation points; `git status`/`ls-files --others` over rounds
  8–17 (empty / 0).
- `git rev-parse HEAD^` → `3dd37542…`; `git show --stat c66ac3c`;
  `git diff --name-only 3dd3754^ 3dd3754 --` (and `c66ac3c^ c66ac3c --`)
  over rounds 8–17 → empty.
- `python3 -` recheck of `reports/round-17/validation.json`
  `filed_rounds.baseline` rows (694) vs on-disk sha256 → 694/0/0.
- `find reports/round-{8..17} -type f -not -path '*__pycache__*' -print0 |
  LC_ALL=C sort -z | xargs -0 sha256sum | sha256sum` → `c0594947…`, run
  before and after the window (set-diff empty); filtered variant (excl
  `*.log`) → `a2b92453…` (761 files); `find … -links +1` → empty.
- `sha256sum` over `tools/gates/frozen/round-11/**` (excl `*.log`),
  `reports/round-9/baselines/**`, `tools/gates/expected/**`,
  `reports/round-16/handoff/*v2-07*` → before/after identical.
- `ls corpus/knowledge/`; `ls corpus/knowledge/civilizations/ | grep -c
  '\.md$'` → 94; `git diff HEAD -- PROVINCE.md` → empty.
- `for d in */; do git -C "$d" status --porcelain=v1 | wc -l; done` —
  sibling sweep, 20 lanes; fleet `git log -1`.

## 7. Compliance self-attestation

This scribe wrote only `reports/round-18/scope.md`, plus scratch snapshots
under `.scratch/` (`x02-filed-before.txt`, `x02-filed-after.txt`,
`x02-filed-after2.txt`, `x02-filed-final.txt`, `x02-pins-before.txt`,
`x02-pins-after.txt`, `x02-pins-final.txt`) with
`TMPDIR=$PWD/.scratch` exported. No git mutations, no commits, no writes
outside the lane repo, no filed-round bytes of rounds 8–17 touched (all
snapshots are new files), no historical validator executed. Out-of-province
observations routed to §5 per PROVINCE ("report, never absorb").
