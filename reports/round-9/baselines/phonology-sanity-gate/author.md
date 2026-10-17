# phonology-sanity-gate frozen baseline — author seat (round 9, claim O)

- role: **author seat** of the `phonology-sanity-gate` baseline pair. This seat writes (a) this
  fragment and (b) the baseline bundle
  `tools/gates/expected/phonology-sanity-gate/r9-pre/{packet.yml,run.log,expected.json,freeze.txt}`.
  Nothing here was committed: the orchestrator integrates once per round. The pair's independent
  second seat owns `reports/round-9/baselines/phonology-sanity-gate/rerun.md`; **this fragment claims
  no independent verification** of its own work.
- date: 2026-10-17, timestamps local (-03:00). Lane revision: base `e1694bad6ac96aca45a11ca5746582b275929355`
  (round-9 `claims.json` `baseline_revision`), freeze-time HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (`git rev-parse HEAD`, 2026-10-17T17:50-03:00). Measured at freeze time:
  `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355 -- tools/gates examples` → empty output, so the
  graded artifact tree is byte-identical at both revisions.
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (layout), §4
  (`expected.json` fields), §5 (freeze procedure), §6 (verify / tamper / class mapping). Self-test =
  capability, frozen run = measurement (standard §2).
- environment measured: `/tmp` was **inode-exhausted** for this seat —
  `mkdir -p /tmp/r9-phon-freeze` → `No space left on device` while `df -h /tmp` reported 8.5G free
  (2026-10-17T17:50-03:00). All throwaway copies therefore lived in `.scratch/r9phon-author/` inside the
  lane and were removed before this fragment was written; the live tree outside the bundle was untouched.

## 1. Baseline identity and snapshot choice

| field | value |
|---|---|
| baseline id | `r9-pre` (phase pre: before the round's edits land) |
| root | `tools/gates/expected/phonology-sanity-gate/r9-pre/` |
| gate | `tools/gates/phonology-sanity-gate.py`, sha256 `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230` |
| snapshot | `packet.yml` = **byte copy** of `examples/culture-d2/packet.d2.yml`, sha256 `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` (`cmp` clean; origin tracked and unmodified: `git ls-files --error-unmatch` ok, `git status --porcelain` empty at freeze time) |
| run log | `run.log`, sha256 `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` (verbatim stdout; stderr 0 bytes, kept out per §3) |
| frozen at / by | 2026-10-17T17:50:33-03:00 / lane kotodama-shokunin round-9 claim O, baseline author seat |

Why a real artifact and not the fixture: the committed fixture pair is already the `--selftest`
(capability) input, and the standard §9 names the D2 culture packet as the intended first real input.
A real, mutable-by-design artifact is what makes the digest pin load-bearing.

Live verdict measured **before** freezing (2026-10-17T17:50-03:00):
`python3 tools/gates/phonology-sanity-gate.py examples/culture-d2/packet.d2.yml` → exit 1, 3 `FINDING`
lines, one distinct ID `A-NEUTRAL` (`notable_rules[1] 'n → m / _ p'`, `[2] 'n → m / _ b'`,
`[7] 's → h / _ #'`). The rerunner seat recorded the same digest and the same verdict independently in
`reports/round-9/baselines/phonology-sanity-gate/rerun.md` §5 — recorded here as agreement between two
seats, not as this seat's evidence.

## 2. Freeze procedure, executed (standard §5)

All commands ran from the lane root on 2026-10-17; the full transcript with observed output is in the
bundle's `freeze.txt`. Summary:

| # | step | observed |
|---|---|---|
| 1 | `python3 tools/gates/phonology-sanity-gate.py --selftest` | exit 0: `fixture exit 1; 15/15 planted finding IDs present; 29 control cases passed`; fixture pair bytes unchanged afterwards (`96dfa97e…`, `165bcc61…`) |
| 2 | `cp examples/culture-d2/packet.d2.yml <baseline>/packet.yml`; `cmp` | byte-identical to origin |
| 3 | gate over the **snapshot copy** → `run.log` | exit 1, 3 FINDING lines, ID set `{A-NEUTRAL}`, stderr 0 bytes |
| 4 | gate over the **live** origin path | exit 1, stdout byte-identical to `run.log` |
| 5 | 3 reruns over the baseline path | stdout byte-identical to `run.log` each time |
| 6 | isolated mirror (gate copy + packet copy, other cwd) | exit 1, stdout byte-identical to `run.log` |
| 7 | tamper control: copy + one comment byte, `sha256sum -c` | `FAILED`, exit 1 → `snapshot_tampered`; the gate over the tampered copy still printed byte-identical findings |
| 8 | gate-revision control: gate copy + one comment byte | stdout byte-identical → only `gate_sha256` names the revision read |
| 9 | input digest re-verified after every run | `packet.yml: OK` (gate is read-only over its input) |

## 3. The frozen verdict (counts, with their commands)

| quantity | command (2026-10-17, bundle dir) | value |
|---|---|---|
| exit code | `python3 tools/gates/phonology-sanity-gate.py <baseline>/packet.yml; echo $?` | `1` |
| finding lines | `grep -c '^FINDING' run.log` | `3` |
| distinct finding IDs | `grep -o '^FINDING [A-Z0-9-]*' run.log \| sort -u \| wc -l` | `1` (`A-NEUTRAL`) |
| stdout bytes | `wc -c run.log` | `654` |

The contract is the **ID set**, order-insensitive (§4): `expected.exit 1`, `expected.class findings`,
`expected.findings ["A-NEUTRAL"]`. Three lines carry one distinct ID because the gate emits one line per
distinct (level, id, message) tuple; the line count is recorded for legibility, not as the pin.

## 4. Verification of the committed bundle (standard §6 order), one pass

Digest check first, then gate revision, then the verdict — measured 2026-10-17T17:51-03:00:

```
step1 digest  packet.yml: got=e0f21509…437b643 want=e0f21509…437b643 -> OK
step2 gate_sha256: got=d5fe087f…dec34230 want=d5fe087f…dec34230 -> OK
step3 verdict: exit=1 want_exit=1 ids=['A-NEUTRAL'] want_ids=['A-NEUTRAL']
compared verdict reading: match -> check exit 0
```

Battery cross-check (`python3 tools/check-gate-battery.py`, claim O15 runner, 2026-10-17T17:52-03:00):
the record `expected/phonology-sanity-gate/r9-pre/expected.json` reads **`pinned`** with
`inputs_checked = 1`, `stdout_pin.reading = match`, and 0 baseline findings. The battery's own scope line
is honest and worth repeating: it "verifies digests and pins only; the verdict comparison is the
baseline's own re-run receipt" — so this section and the rerunner's §6 are the verdict half, and neither
seat's evidence alone is the whole pair.

## 5. Non-vacuity controls (a baseline that cannot fail proves nothing)

- **clean class reachable** — the gate's own `CLEAN_PACKET` constant written to scratch
  (sha256 `36be66044aa2c0a1e103413816af96bc42f500cfc3da1c7bf8d538d50ce8fe8e`) → exit **0**, 0 stdout
  bytes. Exit 1 is not automatic, and the `clean` reading of §6 is reachable on this gate.
- **verdict comparison is sensitive** — a throwaway copy with `phonology.tones: 0 → 6`
  (sha256 `40a71dbe085032a91dcf058f922708a1470b40115398e55ae0ef148c5f88a39d`) → observed set
  `{A-NEUTRAL, T-TONE}` ≠ expected `{A-NEUTRAL}`: the set comparison reports a mismatch rather than a
  silent pass. (In the live order the digest check would fire first on that copy, since its digest
  differs from the pin; this control exercises §6 step 3 in isolation.)
- **path/timing independence** — snapshot path, live origin path and isolated mirror all produced
  byte-identical stdout; 3 reruns reproduced `run.log` exactly; the input digest re-verified after every
  run.

## 6. Negative controls and sweeps (each claim with its command and date)

- **no gate behaviour change** — `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355 -- tools/gates examples`
  → empty output (2026-10-17T17:50-03:00). This seat modified no gate script, fixture, or example packet;
  the bundle is additive.
- **fixture pair untouched by the selftest run** — `sha256sum tools/gates/fixtures/phonology-sanity-gate.{yml,expected}`
  → `96dfa97e…`, `165bcc61…` (unchanged; this is a *writer* gate whose selftest regenerates its fixtures
  deterministically — for it the pin is the script bytes plus this baseline, not the fixture).
- **no internal digest mode** — `grep -rn "expected.json\|--frozen" tools/gates/*.py` → **NO HITS**
  (2026-10-17T17:50-03:00): the interim external `sha256sum -c` / battery pass is the check that ran,
  exactly as standard §6 and §8 declare. Standard §8's row "gate-internal digest verification" therefore
  remains **not implemented**, reported rather than smoothed over.
- **origin packet tracking** — `git ls-files --error-unmatch examples/culture-d2/packet.d2.yml` → tracked;
  `git status --porcelain examples/culture-d2/packet.d2.yml` → empty (unmodified).

## 7. Contested scope — reported to the integrator, not absorbed here

The battery's discovery roots are fixed and fail closed: `tools/check-gate-battery.py:114`
(`BASELINE_ROOTS = (GATES_DIR / "expected", GATES_DIR / "frozen")`; docstring line 17 names
`tools/gates/expected/`; file state as read 2026-10-17T17:51:51-03:00, 932 lines). Measured census at
that time (`find tools/gates/expected tools/gates/frozen reports/round-9/baselines -maxdepth 3 -name expected.json`):

| baseline found | discoverable by the battery? |
|---|---|
| `tools/gates/expected/costume-era-consistency-gate/r9-pre/` | yes |
| `tools/gates/expected/phonology-sanity-gate/r9-pre/` (this one) | yes |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/` | yes |
| `reports/round-9/baselines/{handoff-packet-check,myth-consistency-gate,naming-collision-gate}/expected.json` | **no** |
| `provenance-audit` | none landed yet at that time |

Consequence measured on the same run: the battery reports `gates_covered = [costume-era, lexicon,
phonology]`, `gates_uncovered = [handoff-packet-check, myth-consistency-gate, naming-collision-gate,
provenance-audit]`, `baseline_exit = 2` — i.e. claim O's "7/7 gates carry a committed baseline the battery
validates" **cannot pass** until those bundles move under a discovery root (one `mv`, owned by their
author seats) or the roots are deliberately widened by the integrator. This seat reports that state and
does not move sibling trees.

Re-check at 2026-10-17T17:53-03:00 (`python3 tools/check-gate-battery.py`, piped to JSON, no scratch file):
`gates_covered` = `[costume-era-consistency-gate, handoff-packet-check, lexicon-coverage-audit,
phonology-sanity-gate]` (handoff-packet-check moved into a discovery root in the meantime), `gates_uncovered`
= `[myth-consistency-gate, naming-collision-gate, provenance-audit]`, `baseline_exit = 2`, and this gate's
record still reads `pinned` (inputs_checked 1, 0 findings). The uncovered set is live state, not this
fragment's verdict: re-read it from the battery, not from here.

Two further scope notes, both faithful to the standard:

- **no second copy here.** Standard §3: "the same baseline id under two gate directories makes `r9-pre`
  ambiguous, which the gate standard fails closed rather than compares." This seat therefore did **not**
  also place the bundle in `reports/round-9/baselines/phonology-sanity-gate/` (where the rerunner seat's
  `rerun.md` was written expecting the author's files). The pair dir keeps the fragment and the rerun
  receipt; `expected.json` and `freeze.txt` name the canonical path, and `rerun.md` §6 can verify there.
- **`reports/round-9/baselines/` is the fragment home, not the pin home** for this pair. If the
  integrator wants a single fleet convention, the cheap, non-destructive move is to widen
  `BASELINE_ROOTS` (or normalize the three sibling bundles) — not to duplicate pins.

## 8. Handoff — registry fields for the O17 scribe

| name | kind | entry command | verdict map | self-test | pinned-value path | write scope |
|---|---|---|---|---|---|---|
| phonology-sanity-gate | gate | `python3 tools/gates/phonology-sanity-gate.py <packet.yml>` (`-` = stdin) | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` → exit 0, fixture exit 1, 15/15 planted IDs, 29 controls | `tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json` (baseline `r9-pre`, battery reading `pinned`) | selftest rewrites its own fixtures; normal run and frozen run read-only |

## 9. What this does not claim

- Not design quality, not canon, not that the D2 packet is a good design: a matching digest proves byte
  identity, and a frozen verdict proves what this gate revision said about these bytes (standard §10).
- Later edits to `examples/culture-d2/packet.d2.yml` do **not** invalidate this baseline — the graded
  bytes are the frozen copy — but they do change the live verdict; that earns a **new** baseline id,
  never a re-pin of `r9-pre` (standard §3, append-only).
- No independent verification by this seat; no admission of claim O by this seat; no fleet-level
  conformance claim while four gates are uncovered (§7).
- Sources for the operational claims above are commands run inside this lane on 2026-10-17 and the corpus
  entry `corpus/knowledge/verification/gate-frozen-run-standard.md`; no external source is cited and none
  is needed for a lane-local engineering evidence fragment. Anything not measured here would be marked
  `to-verify`; nothing in this fragment is.
