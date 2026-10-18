# R29-O14 — stale-snapshot readings and frozen-replay limits

- Date: 2026-10-18.
- Status: **historical snapshot changes are classified; independent replay closure remains routed.**

## Finding and bounded disposition

The R26 `gate-input` generation was captured before its register-stratum D4 packet change. Its later red is a stale-snapshot/supersession reading, not evidence that the current packet should be rolled back. The R26 regression recorded an A/B control: `python3 tools/replay-frozen.py tools/gates/frozen/round-26/gate-input/MANIFEST.tsv --json` was **4/6 reproduced, 2 mismatches** after the register landing, while the same command in a throwaway clone with the pre-register D4 inputs restored was **6/6 reproduced** on 2026-10-18. R26's `post-register` successor was recorded **6/6** at its own stamp; R27 later moved the D4 packet again, and R28 added its own successor generation. These are different snapshots, not one mutable baseline.

## Instrument limitation found later

Do not treat those historical replay counts as independent proof that current `replay-frozen.py` grades each pinned D4 snapshot correctly. R28's adversarial review `reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md` §2 measured the replay tool launching the gate from its repository path, causing `ROOT`-relative reads from the live lane. Its dated replay command against `round-26/post-register` produced mismatches citing live assembly bytes; the review also showed the in-repo `TMPDIR` attempt is refused as `mirror_unsafe`. This conflicts with a clean snapshot-replay interpretation, so the stale-snapshot classification and the replay-tool defect must not be conflated.

## Route

No manifest was repaired in place. Route **frozen replay isolation and exit-classification** to R30: a bounded closure requires a replay control that provably runs the gate with all root-relative peers from the pinned snapshot, and returns `could-not-evaluate` rather than a content mismatch when that precondition fails. R29 did not rerun replay with an external temporary directory because that would violate the round's mandated scratch boundary. Current per-generation replay status is therefore **to-verify**, not claimed green.