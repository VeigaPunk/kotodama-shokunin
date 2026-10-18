# R20-A12 — frozen replay audit: every frozen manifest re-run, live and isolated (NON-CANON)

- seat: R20-A12 (frozen replay auditor, of R20-A09..A12). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- assignment (verbatim, my batch): *"AUDIT R20-A09..A12 (entry+handoff auditors x4):
  v3 packet adversarial pass; README-vs-files diff independent re-derivation;
  alias-wart negative re-runs; frozen replay audits."* This file is the fourth leg.
- date: 2026-10-18 (lane-local UTC−03:00; all stamps below UTC). Declared
  round-20 baseline `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`
  (`reports/round-20/claims.json`); HEAD at the readings `122086b`
  ("round-20: declare claims D/O/C"). The wave was **live** throughout: the
  round-20 O change to `tools/d2-typed-labels.py` landed between my 12:56Z and
  13:05Z passes, and its effect on the round-18 frozen row is reported in §5.
- role limits: this seat audits and reports. Writes: this file plus gitignored
  scratch under `.scratch/audit/` and `.scratch/audit/alias-rerun/` (receipt).
  It edits no tool, no manifest, no receipt, admits no claim, and executes no
  historical validator that writes into the repo. Where a reading disagrees
  with a filed record, the disagreement is reported, not repaired.
- instruments: `tools/replay-frozen.py` (selftest re-run, §2);
  `TMPDIR=/tmp/kotodama-r20-audit` for live replays (the tool refuses in-repo
  mirrors by design, `tools/replay-frozen.py:177`); isolated era trees under
  `/tmp/kotodama-r20-audit/iso-r3` and `iso-r11` built by `git show <rev>:<path>`
  and `git archive <rev> examples` (§4), never by editing the live tree.

## 1. Verdict at a glance (all readings 2026-10-18)

| manifest | live tree (13:04:45Z) | isolated era tree | class |
|---|---|---|---|
| `tools/gates/frozen/round-3/MANIFEST.tsv` | **7/7 could-not-evaluate** (`gate_digest_mismatch`) | **7/7 reproduced**, exit 0 | documented historical-pin generation |
| `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | **7/7 could-not-evaluate** (same class) | **7/7 reproduced**, exit 0 | same |
| `tools/gates/frozen/round-4/` | **no manifest** (`manifest_unreadable`) | — | documented: "Round-4 outputs have no frozen manifest and remain unpinned legacy evidence" (`corpus/README.md`, Known gaps) |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | **10 reproduced + 1 could-not-evaluate** (line 2, `gate_digest_mismatch`) | **11/11 reproduced**, exit 0 | line-2 superseded pin documented (`reports/round-19/regression.md` N2) |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | **1 reproduced + 1 mismatch** (row 2 — new, §5) | — (row 2 is the live-peer surface) | row 2 superseded by the round-20 peer change; repin owed at this stamp |
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | **11/11 reproduced**, exit 0 | — | the round-18 re-pin successor, green |

Every live `gate_digest_mismatch` row is the tool's pre-execution refusal: the
on-disk gate bytes are not the pinned revision, so no gate was launched and no
comparison was made (exit 2, precedence over exit 1). That is the documented
historical-pin class, not a regression: `reports/round-18/gate/design.md:123`
records round-3 as "superseded generation; every pinned gate was revised after
round 3", and `reports/round-18/gate/regression.md:66` (row 4e) records the
isolated 7/7 + 7/7 reproduction that §4 re-derives independently.

## 2. Instrument control

`TMPDIR=/tmp/kotodama-r20-audit python3 tools/replay-frozen.py --selftest` →
`selftest: 79/79 checks passed`, exit 0 (12:58Z). The tool refuses in-repo
mirror roots, refuses unsafe paths before normalisation, verifies gate/input/
output digests before any gate runs, and launches each pinned gate as
`[python3, <gate>, <input>]` with cwd = a private mirror (module docstring and
`run_in_mirror`, `tools/replay-frozen.py:171-198`). A reproduced red verdict is
still red — this audit asserts reproduction only.

Adjacent frozen surface re-read the same day: `python3 tools/check-gate-battery.py`
→ exit 0, `pass 7 / fail 0 / unevaluable 0`, baselines `9/9` gates covered,
`17` pins verified, `originals: modified 0, preserved true` (13:00Z; JSON at
`.scratch/audit/battery-r20.json`).

## 3. Live-tree readings, row by row

- **round-3 / attempt-1**: rows 2-8 are 7 rows over six gates; every row reads
  `could-not-evaluate / gate_digest_mismatch`, e.g.
  `ROW 2 ... gate=tools/gates/phonology-sanity-gate.py ... detail: gate: on-disk
  bytes are not the pinned revision`. Both manifests end
  `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of
  7 row(s)`, exit 2. Note the two generations pin **different input snapshots**
  (round-3 `input_sha256` 54be6319…, attempt-1 f424fcf1…) and the same output
  digests; both reproduce in §4.
- **round-11**: 11 rows; 10 reproduced (naming 7/17 findings, phonology 3,
  costume/lexicon/myth 0 — the typed/raw channel differential on the record),
  line 2 `typed-pipeline-gate.py` `could-not-evaluate / gate_digest_mismatch`.
  The manifest's own README claims `REPLAY OK: 11/11`; that claim is true of
  the pinned revision (a3f6fce, §4) and stale for the live tree, and
  `reports/round-19/regression.md` N2 already records the line-2 reading as
  EXPECTED, with the re-pin successor at `round-18/repin-d2/MANIFEST.tsv`
  (11/11 green here).
- **round-18**: at 12:56Z both rows reproduced (row 2 exit 0, row 3 exit 0).
  After the round-20 O change landed, row 2 reads
  `mismatch reason=replay_mismatch ... exit=1/0 ... output bytes differ from the
  recorded output` (§5). Row 1 of that generation remains **pending by design**
  (`tools/gates/frozen/round-18/freeze-receipt.json` `pending` block;
  `tools/gates/frozen/round-18/README.md` §Rows).
- **round-18/repin-d2**: 11/11 reproduced, exit 0, including the re-pinned
  `typed-pipeline-gate.py` row (recorded exit 0) and the legacy rows whose
  recorded red exits (1) reproduce as red.

## 4. Isolated re-derivations (the part the live tree cannot show)

Method: build an era tree outside the repo, restore the pinned tool revisions
from git, verify every restored file's sha256 against the manifest's
`gate_sha256` cells, then replay with `--repo-root <iso>`.

- **round-3, both manifests**: six gates restored from revision `291c714` hash
  exactly to the six pinned digests
  (`fb05c644… phonology`, `63ee4ec6… lexicon`, `26d246e9… myth`,
  `29a9361c… costume`, `8c5afb0a… naming`, `4aaea6e9… provenance` — verified
  with `sha256sum`, `.scratch/audit/iso-r11-gates.txt` records the round-11
  set, the round-3 set was verified in the same pass). Replay:
  `REPLAY OK: 7/7` for `round-3/MANIFEST.tsv` **and** `7/7` for
  `round-3/attempt-1/MANIFEST.tsv`, exit 0 each — the same result row 4e of
  `reports/round-18/gate/regression.md` reported at 10:36Z, re-derived
  independently here.
- **round-11**: six gates restored from revision `a3f6fce` (the round-11 admit
  commit) hash exactly to the pinned digests — including
  `d102fd1d… typed-pipeline-gate.py`, the revision the live tree no longer
  carries. A gates-only iso is **not sufficient** for row 2: the round-11 gate
  revision loads its peers by path (`ADAPTER tools/assemble-d2-typed.py`,
  `PROJECTOR tools/d2-typed-labels.py`, `SERIALIZER tools/assemble-d2.py`), and
  the run needs `examples/culture-d2/expected-holds.json`. With the peers
  restored from `a3f6fce` and `git archive a3f6fce examples` extracted into the
  iso, the replay reads `REPLAY OK: 11/11 rows reproduced`, exit 0. Two
  intermediate runs are part of the record: without peers, row 2 traced back
  (`load_peer` on a missing adapter); with peers but without `examples/`, row 2
  still failed on `FAIL L3-baseline — missing:
  examples/culture-d2/expected-holds.json`. Both intermediates are method
  evidence, not record defects.

## 5. The round-18 row-2 supersession (measured, routed to the parent)

At 12:56Z the round-18 manifest replayed 2/2. After the round-20 O change to
`tools/d2-typed-labels.py` (sha 0da0015f… → fd70df51… → 8eaeba12… → 76536a92…
during 12:59-13:04Z), the same replay reads:

```
ROW 2 mismatch reason=replay_mismatch gate=tools/gates/d4-typed-labels-check-gate.py
  input=tools/gates/frozen/round-18/inputs/examples/culture-d4/typed-labels.d4.yml
  exit=1/0 count=0/0 bytes=differ launched=yes
  detail: exit code 1 != recorded 0; output bytes differ from the recorded output
```

Root cause, re-derived: the gate wraps `d2-typed-labels.py --check` over the
**frozen snapshot** of the old projection (a59990bb…); the changed peer's
deterministic build now differs from that snapshot, so the check reports drift
(exit 1) where the record says exit 0. The live projection was regenerated by
the O seat (`examples/culture-d4/typed-labels.d4.yml` now cbcf997f…,
`--check` exit 0 against the live peer), but the frozen row still pins the old
bytes. This is exactly the "superseded pin" class of round-11 line 2; per the
round's own rule ("re-pins are NEW rows"), the carry should be a **new**
manifest generation pinning the new projection snapshot + output, with
`round-18/MANIFEST.tsv` left byte-unchanged. At this stamp no such successor
row exists under `tools/gates/frozen/` (`ls`: round-3, round-4, round-11,
round-18 only) — the cascade is still owed, and the same applies to the other
surfaces that pin the old projector sha (see `audit-11.md` §4).

## 6. Filed-artifact mutations observed during the window (not this seat's writes)

Between 13:00:55Z and 13:01:01Z the worktree showed `reports/round-5/
validation.json`, `reports/round-7/validation.json` and `reports/round-9/
validation.json` modified in place (`git status --short`), consistent with old
rounds' validators being re-run (round-9's own header: "Writes ONLY
reports/round-9/validation.json"). The round-9 diff flipped
`acceptance_checks_passed` true→false and added baseline blocks; round-7's diff
replaced the recorded historical inventory totals with current-tree totals;
round-5's diff swapped one `tested_file_sha256` cell (check-gate-battery
0a126b70…→cd8c0ec2…) and one error string. By 13:04Z all three diffs were
**back to zero lines** — the filed bytes were restored. Recorded here as an
observation for the parent: the window contained a transient destructive
re-run of three filed receipts; the final bytes match HEAD, so no filed
artifact is mutated at this stamp, but the lane's append-only discipline
("corrections are NEW files") is worth re-affirming for the close.

## 7. Limits

- Reproduction only: this audit re-runs records; it does not certify that a
  recorded verdict is the *right* verdict, and a reproduced red row stays red.
- The isolated era trees are scratch, outside the repo, rebuilt from git
  history at named revisions; they are not filed artifacts and prove nothing
  beyond the reproduction they show.
- `round-4` has no manifest to replay; that is a documented gap, not a defect
  this seat can close.
- The live-tree readings are point-in-time against a live wave; §5's row-2
  mismatch is expected to change the moment the re-pin cascade lands.

## 8. Commands (all 2026-10-18; lane root; stamps UTC)

```sh
# selftest
TMPDIR=/tmp/kotodama-r20-audit python3 tools/replay-frozen.py --selftest
# live matrix (each: exit codes recorded in §1)
for m in round-3/MANIFEST.tsv round-3/attempt-1/MANIFEST.tsv round-11/MANIFEST.tsv \
         round-18/MANIFEST.tsv round-18/repin-d2/MANIFEST.tsv; do
  TMPDIR=/tmp/kotodama-r20-audit python3 tools/replay-frozen.py tools/gates/frozen/$m
done
# isolated era trees
for g in phonology-sanity-gate lexicon-coverage-audit myth-consistency-gate \
         costume-era-consistency-gate naming-collision-gate provenance-audit; do
  git show 291c714:tools/gates/$g.py > /tmp/kotodama-r20-audit/iso-r3/tools/gates/$g.py
done
TMPDIR=/tmp/kotodama-r20-audit python3 tools/replay-frozen.py \
  tools/gates/frozen/round-3/MANIFEST.tsv --repo-root /tmp/kotodama-r20-audit/iso-r3
TMPDIR=/tmp/kotodama-r20-audit python3 tools/replay-frozen.py \
  tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv --repo-root /tmp/kotodama-r20-audit/iso-r3
# round-11 era tree (gates + peers + examples from a3f6fce)
git archive a3f6fce examples | tar -x -C /tmp/kotodama-r20-audit/iso-r11
TMPDIR=/tmp/kotodama-r20-audit python3 tools/replay-frozen.py \
  tools/gates/frozen/round-11/MANIFEST.tsv --repo-root /tmp/kotodama-r20-audit/iso-r11
# battery
python3 tools/check-gate-battery.py     # exit 0; JSON kept at .scratch/audit/battery-r20.json
```

## 9. Final addendum (13:34Z) — the successor generation landed

`tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` (with
`run-receipt-repin.json` and `freeze.txt`) now exists: a NEW generation, the
round-11 successor shape (11 rows over the five legacy gates × typed/raw plus
the typed-pipeline row). Replay at 13:34Z:
`REPLAY OK: 11/11 rows reproduced the recorded verdicts`, exit 0.

Still open at the stamp: the **round-18 D4 typed-labels row** (§5) has no
successor TSV row — `round-18/MANIFEST.tsv` reads 1 mismatch + 1 reproduced,
and the round-20 generation carries the d2 rows only. The live D4 pins are
carried by the new `tools/gates/expected/d4-typed-labels-check-gate/r20-post/`
baseline, `tools/gates/typed-pipelines.json` (with its `superseded` note and
`repin` block) and the filed `reports/round-20/wart/repin-r20.json`. Whether the
lane also files a successor *manifest row* for that leg (as `repin-d2` did for
round-11 line 2) is the parent's call; the state is recorded here so the
reading is not lost. All other §1 live readings were unchanged at this stamp.

