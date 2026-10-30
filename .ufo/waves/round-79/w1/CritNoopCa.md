# CritNoopCa — Ca junk correction vs presence-only checker (round-79 W1)

Seat: critic (Ca). Bounded item: cheapest Ca junk correction that passes a
presence-only checker; exact false payload. Status: probe executed, raw output
preserved.

## Counterexample

Any accept-ca.py shaped as a **presence** predicate — "a correction record for
S884 with a non-empty `actual_token` exists at `--lands`" — is passed by a
lying correction that ratifies the drifted receipt token. Cheapest false
payload (fixture `junk-corrections.json` → `junk[0]`, J-CA1):

```json
{
  "id": "S884",
  "receipt": "reports/round-78/telemetry/census-end.txt",
  "receipt_sha256": "05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867",
  "measured_revision": "4b255745dea45a45d88b17e3c3fea4cdb6700cf7",
  "old_token": "corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md",
  "actual_token": "corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md"
}
```

Every field is present and well-formed; only the two tokens are swapped, so the
correction asserts the registry was wrong and the receipt's drifted token is
the truth. `worldbuilding-setting-practice.amend-2026-10-24-r13.md` never
existed in this lane (exact-path `git log --all -- <path>` is empty). Presence
flips `unresolved` 1→0 while binding nothing.

## Probe (executed; raw output in receipts/)

Fixture repo: isolated, initialized at
`/fast/scratch/hyaku/kotodama-r79/CritNoopCa/fixture-repo` (root verified via
`git rev-parse --show-toplevel` before any commit; deleted after receipts were
copied). FREEZE commit stands in for lane commit
`4b255745dea45a45d88b17e3c3fea4cdb6700cf7`; honest + 6 junk scenarios as
branches. Driver + checkers re-runnable from this stage's fixtures.

Result matrix (presence-only checker vs reference binding checker):

| scenario | presence-only | binding (reference) |
|---|---|---|
| do-nothing (no correction) | FAIL exit 1 | MISMATCH=1 UNRESOLVED=1 exit 0 |
| honest correction | PASS exit 0 | MISMATCH=1 UNRESOLVED=0 exit 0 |
| J-CA1 lying-token (above) | **PASS exit 0** | FAIL exit 1 — OLD-TOKEN, ACTUAL-TOKEN |
| J-CA2 swap-as-fix | **PASS exit 0** | FAIL exit 1 — ACTUAL-TOKEN |
| J-CA3 vacuous prose note | **PASS exit 0** | FAIL exit 1 — BINDABLE |
| J-CA4 truncated 7-hex digest | **PASS exit 0** | FAIL exit 1 — RECEIPT-DIGEST |
| J-CA5 wrong measured revision (binds lane base 44f76d45…) | **PASS exit 0** | FAIL exit 1 — REVISION, RECEIPT-DIGEST, OLD-TOKEN, ACTUAL-TOKEN |
| J-CA6 changed receipt (line 33 repaired in place) | **PASS exit 0** | FAIL exit 1 — RECEIPT-UNCHANGED, RECEIPT-DIGEST |

The exact junk classes the draft names (do-nothing / lying / wrong revision /
changed receipt) all pass presence-only except do-nothing; each fails the
binding checker on the leg designed for it. Honest correction passes both and
is the only scenario with UNRESOLVED=0.

## Evidence (measured from committed lane bytes, 2026-10-30)

- Receipt: `reports/round-78/telemetry/census-end.txt` at
  `4b255745dea45a45d88b17e3c3fea4cdb6700cf7`, line 33:
  `S884 … used-by=…worldbuilding-setting-practice.amend-2026-10-24-r13.md`.
- sha256 of committed receipt bytes: `05b5011a…e35867` (matches
  `reports/round-79/telemetry/baseline-census-mismatch.json` from ScoutR78Truth).
- Registry `corpus/SOURCES.md` S884 used-by cell at `4b255745…` and at base
  `44f76d45…`: `…worldbuilding-setting-practice.amend-2026-10-23.md`.
- `census-start.txt:33` at `4b255745…` correctly shows `…10-23`; only the end
  receipt drifted. Already routed as defect 2 of
  `corpus/lessons/round-78-verifier-spotcheck.md:67` (append-only correcting
  entry requested — that is exactly this Ca claim).
- The `-r13` filename family does exist in-lane for a *different* entry
  (`heritage-taxonomy-models.amend-2026-10-24-r13.md`), so suffix/family fuzzy
  matching in a checker is a live confusion risk, not a hypothetical one.

## Impacted axes

- Ca counter calibration (frozen accept-ca.py): the `unresolved 1→0` verdict
  must require re-derived bindings, or the claim's own "lying correction must
  fail" clause is unmet. This is a fixable defect, not a tradeoff.
- QUALITY 25(b)/26 junk-fixture discipline: the freeze must ship the six
  receipts above (or the four draft-named classes at minimum) as red-befores;
  a presence-shaped counter would pass five of six.
- Receipts append-only integrity (QUALITY 17/19 family): J-CA6 shows the
  in-place repair needs its own leg (RECEIPT-UNCHANGED), independent of token
  checks.

## Smallest safe correction

accept-ca.py grades only committed bytes (`git show`), takes `--lands` +
`--freeze`, and flips `unresolved` to 0 only when all five legs pass (reference
implementation: `fixtures/binding-checker.py`):

1. **RECEIPT-UNCHANGED** — receipt bytes at `--lands` == receipt bytes at `--freeze`.
2. **RECEIPT-DIGEST** — stated `receipt_sha256` == sha256 of the committed receipt at the stated measured revision (full 64-hex; no truncated digests).
3. **REVISION** — `measured_revision` is 40-hex, an ancestor of `--lands`, and equals the frozen expected revision read from `git show <freeze>:reports/round-79/claims.json` (not merely "some ancestor" — J-CA5 binds the lane base, which is a valid ancestor and must still fail).
4. **OLD-TOKEN** — stated `old_token` == the token parsed from the committed receipt's S884 line.
5. **ACTUAL-TOKEN** — stated `actual_token` == the S884 used-by cell of the committed registry at the measured revision, and != old_token.

Baseline with no correction: re-derive MISMATCH=1 from committed receipt vs
committed registry and report UNRESOLVED=1 (do-nothing control). Junk fixtures
J-CA1–J-CA6 ship with the freeze as red-befores, one receipt line each
(fixture, commit, command, `LEG FAIL <name>`, exit code).

Review-only residue (not mechanically checkable, name it as such per QUALITY 11):
whether the correction record's prose *explains* the drift cause
(uncommitted/regressed working-tree state at capture, per the spot-check) —
the legs above verify the binding, not the narrative.

## Fixtures and commands

- `stage/CritNoopCa/fixtures/correction-contract.md` — assumed correction-record shape + leg definitions (for ExecCaCounter/ScribeClaims alignment; L1 arbitrates final path/shape).
- `stage/CritNoopCa/fixtures/junk-corrections.json` — honest payload + J-CA1…J-CA6 exact false payloads (tokens/digests measured from lane bytes).
- `stage/CritNoopCa/fixtures/presence-only-checker.py` — straw-man vacuous predicate (do not ship anything shaped like it).
- `stage/CritNoopCa/fixtures/binding-checker.py` — reference binding checker (`--repo --lands --freeze --expect-revision`).
- `stage/CritNoopCa/receipts/probe-ca-junk-presence-only.txt` — verbatim probe output; `probe-driver.sh.txt` — driver; `SHA256SUMS` — fixture hashes.

Re-run: recreate a scratch dir, copy `probe-driver.sh.txt` to `probe.sh`, point
`LANE`/`STAGE`/`SCRATCH` at the right places, `bash probe.sh`.

## Tooling record

No installs. Used system `/usr/bin/python3` (3.14.8) and `git` (2.56.0) only;
no lane/fleet mutations (fixture repo lived in own scratch, now removed).
