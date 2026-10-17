# R9-O20 — battery selftest still green with the O15 baseline-validation extension

- seat: **R9-O20 auditor** (claim O — operability). This file is the seat's only repository
  write; no gate, fixture, battery, baseline or corpus byte was written by it (every drill in
  §3 ran on copies outside the repository — see §5 scratch receipts).
- date: 2026-10-17, measurements 17:49–18:04 -03:00 (`date -Iseconds` →
  `2026-10-17T18:03:55-03:00` at the final revision check).
- lane revision: HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (`git rev-parse HEAD`).
- subject: `tools/check-gate-battery.py`, sha256
  `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1`, **uncommitted at audit
  time**: `git diff --stat HEAD -- tools/check-gate-battery.py` →
  `1 file changed, 648 insertions(+), 19 deletions(-)`. That working-tree revision is the O15
  extension (docstring “duty 2”, `tools/check-gate-battery.py:20-40`: “Committed baseline
  validation (round 9, claim O15)”).
- every measurement below re-hashed the subject before and after and observed the same
  `0a126b70…` bytes; no run in this fragment measured a moving file.

## 1. Primary receipt — `--selftest` green with the extension

Run from the lane root, 2026-10-17 17:55, 17:59 and 18:03 -03:00 (three independent runs, one
command):

```text
python3 tools/check-gate-battery.py --selftest
```

- **exit 0**
- **output sha256 `8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28`**,
  byte-identical in all three runs (captured to `selftest-final.txt` and `selftest-confirm.txt`,
  §5)
- final line: `SELFTEST OK 28/28 controls behaved as expected`
- subject sha256 before run == after run: `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1`

Full output, verbatim:

```text
control CTRL-PASS-EXIT0: exit=0 outcome=pass ids=-
control CTRL-RECOGNIZED-FAIL: exit=1 outcome=fail ids=GATE-SELFTEST-FAIL
control CTRL-FAIL-LINE-ID: exit=1 outcome=fail ids=GATE-SELFTEST-FAIL
control CTRL-EXIT1-UNRECOGNIZED: exit=1 outcome=unevaluable ids=GATE-CRASH-EXIT1
control CTRL-CRASH-EXIT1: exit=1 outcome=unevaluable ids=GATE-CRASH-EXIT1
control CTRL-MARKER-THEN-CRASH: exit=1 outcome=unevaluable ids=GATE-CRASH-EXIT1
control CTRL-MISSING-GATE: exit=None outcome=unevaluable ids=GATE-FILE-MISSING
control CTRL-TIMEOUT-GATE: exit=None outcome=unevaluable ids=GATE-TIMEOUT
control CTRL-BASELINE-PINNED: exit=0 outcome=pinned ids=-
control CTRL-BASELINE-TAMPERED: exit=2 outcome=snapshot_tampered ids=BASELINE-TAMPERED
control CTRL-BASELINE-UNPINNED: exit=2 outcome=unpinned (legacy) ids=BASELINE-UNPINNED
control CTRL-BASELINE-GATE-REVISED: exit=2 outcome=gate_revised ids=BASELINE-GATE-REVISED
control CTRL-BASELINE-GATE-UNPINNED: exit=2 outcome=gate_unpinned ids=BASELINE-GATE-UNPINNED
control CTRL-BASELINE-MALFORMED: exit=2 outcome=no baseline ids=BASELINE-GATE-UNCOVERED,BASELINE-MALFORMED
control CTRL-BASELINE-GATE-UNKNOWN: exit=2 outcome=no baseline ids=BASELINE-GATE-UNCOVERED,BASELINE-GATE-UNKNOWN
control CTRL-BASELINE-INPUT-MISSING: exit=2 outcome=no baseline ids=BASELINE-INPUT-MISSING
control CTRL-BASELINE-PATH-ESCAPE: exit=2 outcome=no baseline ids=BASELINE-PATH-ESCAPE
control CTRL-BASELINE-EXTERNAL-INPUT: exit=2 outcome=no baseline ids=BASELINE-EXTERNAL-INPUT
control CTRL-BASELINE-EXPECTED-ABSENT: exit=2 outcome=no baseline ids=BASELINE-EXPECTED-ABSENT
control CTRL-BASELINE-EXPECTED-INCONSISTENT: exit=2 outcome=no baseline ids=BASELINE-EXPECTED-INCONSISTENT
control CTRL-BASELINE-AGGREGATE: exit=0 outcome=pinned ids=-
control CTRL-BASELINE-STDOUT-ADVISORY: exit=0 outcome=pinned ids=-
control CTRL-BASELINE-UNCOVERED-GATE: exit=2 outcome=pinned ids=BASELINE-GATE-UNCOVERED
control CTRL-BASELINE-NONE-FOUND: exit=2 outcome=- ids=BASELINE-GATE-UNCOVERED,BASELINE-NONE-FOUND
control CTRL-BASELINE-ROOT-MISSING: exit=2 outcome=- ids=BASELINE-GATE-UNCOVERED,BASELINE-ROOT-MISSING
control CTRL-COMBINED-EXIT: exit=2 outcome=- ids=-
control CTRL-TREE-DIFF: exit=0 outcome=- ids=-
control CTRL-STABLE-IDS: exit=0 outcome=- ids=-
SELFTEST OK 28/28 controls behaved as expected
```

Reading: 10 legacy controls + **18 new `CTRL-BASELINE-*` controls**, all behaving as declared;
the extension is a strict addition to the selftest, it did not displace or weaken a legacy
control.

## 2. Pre-extension control (for contrast)

Before the extension landed (17:49-03:00) the same command on the HEAD bytes
(`tools/check-gate-battery.py` sha256
`077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67`) gave: exit 0,
`SELFTEST OK 10/10 controls behaved as expected`, output sha256
`03f14e3d2d16fd7b0203631b8031a84e216fed1568e55ba257ad1596e96569cf`. The 8 executed controls
in that output match the first 8 lines of §1 verbatim; the two structural controls
(`CTRL-TREE-DIFF`, `CTRL-STABLE-IDS`) also match. Delta is exactly the 18 baseline controls.

## 3. Independent tamper / revision drills (auditor-run, outside the repository)

Scratch copy made 17:59-03:00: `cp tools/check-gate-battery.py <scratch>/tools/` +
`cp -r tools/gates <scratch>/tools/gates` (scratch root in §5). The copy carried the same 5
committed `expected.json` as the live tree (verified by `find … | wc -l` = 5 in both). Drills
modified **copies only**; the live subject sha256 was re-checked after each drill and never
moved.

| # | drill | observed |
|---|---|---|
| 1 | clean copy, `python3 tools/check-gate-battery.py` | exit 2; baseline summary: `baselines_found 5, pinned 5, readings {'pinned': 5}`, covered `[costume-era-consistency-gate.py, handoff-packet-check.py, lexicon-coverage-audit.py, phonology-sanity-gate.py, provenance-audit.py]`, uncovered `[myth-consistency-gate.py, naming-collision-gate.py]`; battery summary `{'battery_exit': 2, 'fail': 0, 'pass': 7, 'unevaluable': 0}` |
| 2 | appended one newline to the pinned snapshot input `expected/costume-era-consistency-gate/r9-pre/packet.yml` (copy) | exit 2; readings `{'pinned': 4, 'snapshot_tampered': 1}`; finding `BASELINE-TAMPERED`: `packet.yml: digest 8fe4b57914466021... does not match the pin 36d92113d0cb8e04...` — a tampered snapshot is reported, **never a silent pass** |
| 3 | appended a comment line to the copy of `tools/gates/phonology-sanity-gate.py` | exit 2; readings `{'gate_revised': 1, 'pinned': 4}`; finding `BASELINE-GATE-REVISED`: `gate_sha256 d5fe087ffb2342e5... differs from the live phonology-sanity-gate.py af5ba185e89cc09c...: re-freeze, never compare across an unnamed revision` |

Drill 1's exit 2 is produced solely by `BASELINE-GATE-UNCOVERED` for the two gates without a
committed baseline — the standard's fail-closed reading (§6), and the intended behaviour of the
extension, not a regression. All seven gate selftests still passed inside the same run
(`pass 7, fail 0, unevaluable 0`).

## 4. Live-tree battery run and the coverage status at audit time

Run from the lane root, 2026-10-17 18:00 -03:00:

```text
python3 tools/check-gate-battery.py          # exit 2
```

- selftests: `pass 7, fail 0, unevaluable 0` (all seven gates pass in isolation).
- baselines (default roots `tools/gates/expected`, `tools/gates/frozen`): `pinned 5`,
  uncovered `[myth-consistency-gate.py, naming-collision-gate.py]`; exit 2 from
  `BASELINE-GATE-UNCOVERED` only.
- the five committed baselines present at 18:03:55-03:00 (`find tools/gates/expected
  tools/gates/frozen -name expected.json`, sha256 of each):

```text
7ec01a1dce6182db329233594563dc31d52ce9d4c4cb9c89bc64e693e992c689  tools/gates/expected/costume-era-consistency-gate/r9-pre/expected.json
2763614ff26959e6b7fa7d96471e8d5e9e93616e37d47e3f0bec99b5caa62cde  tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json
9dc21cd508e3dcfb225564cdccf65a8f88d9768029e876ac7e47d4c55f21c690  tools/gates/frozen/handoff-packet-check/r9-pre/expected.json
0fad58ba70d545328d015990de5184bdd371e575810eb7e79c96bcc7c8a4ff9c  tools/gates/frozen/lexicon-coverage-audit/r9-pre/expected.json
425c74c084bb53bdf8aff8d4f143a6cbe062421e1362f234e5fe702463f95e87  tools/gates/frozen/provenance-audit/r9-pre/expected.json
```

- negative sweep for the two uncovered gates (2026-10-17T18:03:55-03:00, three consecutive
  polls at 18:00:36 / 18:01:36 / 18:02:36 each gave the same counts):
  `find tools/gates -path '*myth*' -name expected.json | wc -l` → `0`;
  `find tools/gates -path '*naming*' -name expected.json | wc -l` → `0`.

Status, stated as status: at this seat's audit window the O claim's 7-gate coverage read **5/7**
(myth-consistency-gate and naming-collision-gate baselines had not landed; their authors were
still active — `reports/round-9/baselines/` grew from 6 to 10 entries during the window). That
is an incompleteness of the round, not a defect of the extension: the extension's own reading
of the gap is fail-closed (`BASELINE-GATE-UNCOVERED`, exit 2), which is the behaviour the claim
requires.

## 5. Environment receipts (why scratch lived outside `/tmp`)

- `/tmp` was **inode-exhausted**, not byte-exhausted, for the whole window:
  `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp`; `df -h /tmp` → `8.5G` avail.
  Direct probe: `echo test > /tmp/r9o20-probe.txt` → `No space left on device`;
  `mkdir -p /tmp/r9o20-probe-dir` → `cannot create directory … No space left on device`.
- The battery is nevertheless unaffected, because it creates its mirrors through `tempfile`:
  `python3 -c "import tempfile; print(tempfile.gettempdir())"` → `/var/tmp` (Python's writability
  probe skips the unusable `/tmp`). Confirmation: with `/tmp` unwritable, `--selftest` still
  exited 0 (§1) and the battery mirror landed under `/var/tmp/gate-battery-…` — the same
  observation other seats recorded (`reports/round-9/baselines/registry.md:170`:
  “measured this run: `/var/tmp/gate-battery-…`, `removed: true`”;
  `reports/round-9/baselines/costume-era-consistency/rerun.md:21-22`: same `df -i` reading).
- Scratch receipts used by this fragment (outside the repository, ephemeral; the outputs are
  embedded verbatim above so this file stands alone):
  `/home/vgpnk/r9o20-scratch/selftest-final.txt` and `selftest-confirm.txt` (sha256
  `8b1fdd6f…`), `selftest-tmpdefault.txt` / `selftest-home-tmp.txt` (sha256 `03f14e3d…`),
  `drill/run1.json`, `drill/run2.json`, `drill/run3.json`, `live-battery.json`.
  The very first capture attempt, `> /tmp/r9o20-selftest-pre.txt`, failed with
  `No space left on device` — the receipt for the `/tmp` substitution.

## 6. What this audit does not establish

- It does **not** compare any baseline's expected verdict against a re-run: the extension never
  re-executes a gate over a baseline (it reports `verdict_replay: "not-run"`), so this fragment
  measures digest/pin/coverage machinery and the selftest only. Verdict comparison belongs to
  the baselines' own author/re-runner receipts (`reports/round-9/baselines/*/rerun.md`,
  `*/run.log`, `*/expected.json`).
- It does **not** admit claim O: coverage read 5/7 during the window (§4); admission of the
  round claim is the orchestrator's call.
- It binds only the uncommitted revision it measured: `0a126b70…`. If integration commits
  different bytes for `tools/check-gate-battery.py`, §1 must be re-run against the committed
  bytes before this receipt is cited.

## 7. Reproduction (from the lane root)

```text
sha256sum tools/check-gate-battery.py                       # expect 0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1
python3 tools/check-gate-battery.py --selftest              # exit 0; SELFTEST OK 28/28
python3 tools/check-gate-battery.py                         # exit 2 while any gate lacks a baseline
find tools/gates/expected tools/gates/frozen -name expected.json | sort
```
