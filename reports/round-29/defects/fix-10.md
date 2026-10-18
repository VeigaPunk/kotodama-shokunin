# R29-O10 — stale D4 claim prose in handoff v3

- Date: 2026-10-18.
- Status: **bounded correction landed as an append-only revision; current handoff green.**

## Defect and correction

The round-23 v3 packet described a pre-family-clean D4 state as current: inherited rank holds, a note, conflicts, quarantine handles, and unresolved rank items. The R25 correction did not rewrite the filed parent. It created `reports/round-25/v3-supersession/declared-in-r4/packet.md`, built from the r3 parent by the declared five-line delta plus a provenance note, and pinned the new bytes. The frozen grammar checker alone could not see the stale semantic prose, so the correction also carries a detector and a negative control on the parent.

`reports/round-25/v3-supersession/evidence.md` §§1–3.4 records the exact original and corrected claims and the control protocol. On **2026-10-18**, `python3 reports/round-25/v3-supersession/v3-supersession-check.py --root .scratch/r25-o11-clone2 --check` was reported exit 0 with **52/52** controls; the stale detector was clean on r4 and detected the named stale rows on the predecessor. The older wording checker was also reported green at **17/17** on that date. These are cited as historical controls, not a claim that this round reran a historical validator.

## Independent current control

At **2026-10-18 17:59:23−03:00**, with `TMPDIR=$PWD/.scratch`, I ran `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` against the current default. It exited 0: fields **16/16**, glossary **20/20**, findings **0**, links **105/105**, claims **27**, statuses **16/7/4**, and the v2 subset was equal. This proves the live default handoff works; it does not replace the r4 content detector's historical control.

## Disposition

Keep r3 and earlier revisions immutable. The new revision is the bounded correction; the remaining renderer claim-map question recorded by the R25 author is separate and should be routed to its owner if a native regenerated packet is required.