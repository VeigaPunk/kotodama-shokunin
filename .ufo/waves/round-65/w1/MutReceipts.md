# MutReceipts — receipt-mutant enumeration (attack, round 65)

Scope: the round's receipts `reports/round-65/telemetry/final-measures-{c,o,ca}.txt`
(absent at the lane tip — lands not yet committed). I attacked every frozen counter
(`reports/round-65/accept-{c,o,ca}.py`, tip bytes) with each mutant class named in the
assignment, in an isolated scratch copy of the lane (`/tmp/k65-MR`, `cp -a`; lane
working tree untouched, no git/jj write, no commit). No tools installed.

Detector method: mutate the smallest behaviour-bearing point (the receipt file at its
intended path, or one receipt field of the one receipt a leg actually parses), run the
same counter on pristine / mutated / restored bytes, compare leg outcomes. Where the
baseline at tip is already FAIL (all C/Ca legs: entry, rows and R1-R7 lands absent),
that baseline is *inconclusive*, so for R1 I first shaped a PASS-capable baseline
(the receipt's four R1-required strings plus the three repeat markers) and mutated
from there; `RESTORED` row returns R1 to PASS.

## Answer in one line

All four mutant classes **survive** against `ACCEPT-{C,O,CA}-65`: no frozen leg opens
any round-65 `final-measures-*.txt`. A receipt carrying a wrong counter sha, a stale
sha, the declaration commit as its measured revision, and no tree line lands
indistinguishable from an honest one.

## Table — round-65 receipts `final-measures-{c,o,ca}.txt`

| # | Mutant | What it fakes | Killing leg / closure in the frozen counters | Probe (pristine vs mutated) | Verdict |
|---|---|---|---|---|---|
| M1 | wrong `counter sha256` (64×`0`) | "this verdict was produced by counter X" while X never ran | **none.** `accept-c.py`: 0 refs to `final-measures`. `accept-o.py`: refs at :423 and :1087 are comments only. `accept-ca.py`: constant `CA64` (:66) is the *round-64* path. | 3 mutant receipts injected → `accept-ca` leg vector identical `['R1 PASS','R2 FAIL','R3 FAIL','R4 FAIL','R5 FAIL','R6 FAIL','R7 FAIL','CRITERION FAIL','QUOTES FAIL']`, diff `[]`; `accept-c` 10/10 legs identical. `chmod 000` on all three → both counters still run, **no PermissionError** (uid 1000; mode-000 blocks open). | **survives** |
| M2 | stale sha of an earlier counter revision (used `979050ce…` = round-64 `accept-c` counter) | verdict attributed to a superseded counter | **none**, same no-reader; nothing binds a receipt sha to `reports/round-63/telemetry/revisions.txt` (accept-ca R2 only greps the strings `Correction (round 65, R2)` and `final-measures-c.txt`, :127). | same as M1 (receipt bytes never opened). Field-level: in the one receipt a leg *does* parse (r64 `final-measures-ca.txt`), R1 prints PASS with the stale sha (`M2-stale-counter-sha`), with the sha line removed (`M2b`), and with a wrong sha (`M1`). | **survives** |
| M3 | `measured revision:` = declaration commit `17c32302…` (also covers any non-lands or nonexistent hash) | pins the pre-data declaration, not the bytes the verdict was measured on | **none for round-65.** No leg requires the measured revision to equal a lands constant, to descend from `BASE`, or even to exist. Contrast: r64's R1 hardcodes `TRUE_REV` (:108) and fails any other revision (`M3a-measured=old-95c9194` FAIL, `M3b-measured=base-declaration` FAIL) — a historical constant, not a lands-vs-declaration rule. | injected receipt names `17c32302…` → zero leg delta (accept-c, accept-ca); no open. | **survives** |
| M4 | tree line removed | receipt no longer pins a tree hash of its read inputs (the R1 class QUALITY criterion 17 is landed for) | **only a documentary shape check.** `accept-ca.py` CRITERION (:166-170) is `^1[7-9]\.\s` **and** the literal `tree hash` anywhere in `corpus/QUALITY.md`. It never inspects a round-65 receipt. Gameable: appended `17. Receipts are advisory prose; a tree hash need not be recorded and no measured revision is required.` → `CRITERION PASS`; restored → `CRITERION FAIL`. Contrast: r64 R1 *does* require `^tree: <tree-of-TRUE_REV>$`; removing it or naming the base tree fails (`M4-tree-line-removed` FAIL, `M3c-tree=base-tree` FAIL). | injected receipt without tree line → zero leg delta. | **survives** |

Verdict line for a fabricated receipt that copies an honest run's leg lines and adds
any of M1-M4 (or all four): every counter prints its own PASS, and nothing in the
three frozen instruments reads the receipt. **4/4 survive.**

## Contrast probe — the only receipt-parsing leg (r64 R1), shaped PASS baseline

Detector `python3 -B reports/round-65/accept-ca.py --root /tmp/k65-MR`; receipt
`reports/round-64/telemetry/final-measures-ca.txt`; tree of `8bab271c…` =
`0ec0e50ea828ca6d8e20298f72af49414692e9e4`.

| Mutant | R1 |
|---|---|
| (shaped baseline, unchanged) | PASS |
| wrong counter sha | **PASS** (unread) |
| stale counter sha | **PASS** (unread) |
| counter-sha line removed | **PASS** (unread) |
| measured revision = old `95c9194e…` | FAIL |
| measured revision = base `17c32302…` | FAIL |
| tree = base tree `fc0615e3…` | FAIL |
| tree line removed | FAIL |
| restored | PASS |

So even where a receipt is validated, the counter-sha family (M1/M2) has no check at
all; R1's revision/tree checks exist only as literal constants for the round-64 file.

## Adjacent O receipt (found while tracing every receipt reader)

`accept-o.py` MUTEX (:1186-1200) writes `exactness-sweep-o65.txt` with a **hardcoded**
header `tool sha256 c0f10a84…` (:1187) and, when the file is committed, compares only
`committed.splitlines()[-len(sweep_rows):]` (:1199) — header lines, including the
counter/tool sha pins, are never compared or recomputed. Extraction probe of that exact
expression with a wrong (`f`×64) header sha: `equal=True` → a wrong or stale tool sha in
the committed sweep header **survives MUTEX**. Today the hardcoded sha does equal
`sha256sum tools/reopen-row.py` (`c0f10a84…` at tip and at `17c32302`), so the header is
honest now but unverified. MUTEX's baseline at tip is `not_committed` (file absent), so
this false-stamp path is only reachable after the file lands.

Also observed: `accept-o.py --root . --only FRAG` prints
`ACCEPT-O-65: PASS [filtered: 1/26 legs]` at tip. The filtered marker is present
(weak mitigation); FULL bounds filtered-green inside a full run, not inside a
hand-written receipt.

## Restoration evidence

| Path | sha256 | State |
|---|---|---|
| lane `reports/round-64/telemetry/final-measures-ca.txt` | `c69d173954…e5317cb6` | untouched; scratch original `/tmp/CA64.orig` identical |
| lane `corpus/QUALITY.md` | `e853b7020f…d61c2c2` | untouched; scratch restored to identical |
| scratch shaped r64 receipt (after last probe) | `e34a58aa14…c2b35d4` | RESTORED row = R1 PASS; scratch copy disposable, mutants removed |
| scratch `reports/round-65/telemetry/final-measures-*.txt` | — | mutant files deleted; directory back to its 5 tip files |

Lane `git status` after probes: only the pre-existing untracked wave/report/tool paths;
no modified tracked file, no index or jj change by this seat. Scratch copy
`/tmp/k65-MR` holds the shaped receipt and the probe scripts (`probe-r1.py`,
`probe-receipts.py`).

Raw probe transcript: `.ufo/waves/round-65/w1/MutReceipts-evidence.txt`.

## Findings

- **HIGH (coverage):** no frozen round-65 counter reads its own claim's receipt. The
  four named fake classes are undetectable, and so is a wholly fabricated receipt.
  Because the predicates are frozen but the counters are pre-data revisions, the
  closure belongs in a receipt leg per claim (recompute counter sha256 and compare;
  require the declared lands revision, not the declaration commit; require
  `^tree: $(git rev-parse <measured>^{tree})$`; require the receipt's leg lines to
  equal the current run's). None of that exists at rev 1.
- **MEDIUM:** CRITERION is a keyword presence check, satisfiable by a criterion that
  negates the rule; it cannot enforce M4 on any receipt.
- **MEDIUM:** the O sweep receipt's sha pins are write-only (hardcoded header, last-N-line
  compare).
- **LOW:** a filtered `PASS [filtered: 1/26 legs]` line is a legal verdict string at tip;
  only the bracket distinguishes it from a full run.

Report: .ufo/waves/round-65/w1/MutReceipts.md
