# R11-O18 — adversarial review: does the handoff-e2e exercise fail closed on D2/D3 drift?

- seat: **R11-O18** (reviewer, adversarial), claim O (`handoff-e2e-exercise`), round 11, loop 1 of 3, 2026-10-17.
- assignment (verbatim): "HANDOFF R11-O18 (reviewer): adversarial — the exercise must fail closed if D2/D3 artifacts drift; tamper a source and show the exercise catches it; reports/round-11/handoff/review-18.md."
- writes: **this file only**; all scratch under `.scratch/r18/` (`export TMPDIR=$PWD/.scratch` in every scratch-writing command); no file of rounds 5–10 touched; no git operation.
- reviewed revision: `tools/exercise-handoff-e2e.py` sha256 `d5b346b877be098f17e34cec1787e487d689e4bbd34160b667a54383394a6c8e`
  (observed 2026-10-17T19:16:23-03:00; the file was rewritten three times during this review — see §6 history).
- independent, un-asked-for evidence: the live tree itself drifted while I reviewed, and the exercise caught it (§2.1).

## 1. Verdict

**The assigned property holds for every artifact the exercise reads.** 20 tamper probes were applied to
pristine sandbox copies; **17 failed closed** (exit 1 `E2E-DIGEST` or exit 2 `E2E-ARTIFACT`/`E2E-BASELINE`),
**3 stayed green** — all three on bytes the exercise does not read or on its own explicit `--freeze` act
(§3, F-18-04). One live, unscheduled drift was caught in passing (§2.1).

Two blockers were found and **were fixed by the implementer while this review ran**; both are recorded with
their pre-fix measurements because they cost claim-O legs time (§3, F-18-02, F-18-03). One blocker is
**open at filing time**: the claim's counting command is red *right now* because a sibling claim (D) re-emitted
a read-set file after O froze its baseline (§3, F-18-01).

## 2. The assigned question

### 2.1 A real drift, caught (strongest evidence — not a synthetic tamper)

`examples/culture-d2/typed-labels.d2.yml` was re-emitted by the D workstream during round 11. The O baseline
had pinned the earlier bytes:

```
2026-10-17T19:15:30-03:00, lane repo root, TMPDIR=$PWD/.scratch
$ sha256sum examples/culture-d2/typed-labels.d2.yml
a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43  examples/culture-d2/typed-labels.d2.yml
$ python3 tools/exercise-handoff-e2e.py
FAIL input-digest: examples/culture-d2/typed-labels.d2.yml: frozen e70ba1477dbe… live a3aa452cd5ae…
FAIL verdict: 1 read-set file(s) changed since the baseline was frozen: examples/culture-d2/typed-labels.d2.yml
handoff-e2e: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: examples/culture-d2/typed-labels.d2.yml
exit 1
```

The baseline pins 21 read-set files (`reports/round-11/handoff/expected.json`, sha256
`c8abc7990bded965b376e85999224a67d349c5b2fdd81070a7c05eda6c09ad0b`, observed 19:15). The tool's
`E2E-DIGEST` names the drifted file. **Fail-closed demonstrated on a live change, not on a fixture.**

### 2.2 Tamper matrix (20 probes, revision `d5b346b8`, 2026-10-17T19:16:23-03:00)

Method: one pristine sandbox copy of the lane tree per probe (19 MB; `.scratch/r18/mksandbox.sh`); each probe
re-freezes a baseline inside the sandbox, verifies exit 0, applies one tamper, re-runs, records exit and message.
The live tree is never mutated. Raw records: `.scratch/r18/exercise-matrix-v5.json` (+`-v4`, `-v3` for the earlier
revisions).

| # | tampered artifact | class | exit | diagnostic |
|---|---|---|---|---|
| T1 | `examples/culture-d2/components/05-lexicon.yml` (L-01 gloss text) | content | 1 | `E2E-DIGEST` — assembler recorded 9bdcb8d895be… measured 008136f302a1… |
| T2 | `.../components/03-morphosyntax.yml` (comment appended) | byte-only, inert | 1 | `E2E-DIGEST` — recorded bd2f78c19eb4… measured a1e2eacff941… |
| T3 | `examples/culture-d2/packet.d2.yml` (comment appended) | packet | 1 | `E2E-DIGEST` — 1 read-set file changed since the baseline |
| T4 | `examples/culture-d3/components/04-language.json` (L01→L01x) | content | 1 | `E2E-DIGEST` — recorded fee4ad61a6aa… measured 5ae8c753c695… |
| T5 | `examples/culture-d3/packet.json` (L01→L01x) | packet | 1 | `E2E-DIGEST` — read-set file changed |
| T6 | `examples/culture-d3/components/07-evidence.json` deleted | missing | 2 | `E2E-ARTIFACT` — read-set file unreadable |
| T7 | `examples/culture-d2/typed-labels.d2.yml` (native-form→translated-label) | projection | 1 | `E2E-DIGEST` — read-set file changed |
| T8 | `tools/gates/handoff-packet-check.py` (comment appended) | judge | 1 | `E2E-DIGEST` — read-set file changed |
| T9 | `.../components/02-phonology.yml` (invalid YAML appended) | malformed | 1 | `E2E-DIGEST` — recorded 23500df0f97a… measured 64dc7e035171… |
| T10 | `examples/culture-d3/expected.json` (`expected_exit` 0→1) | D3 freeze manifest | 1 | `E2E-DIGEST` — read-set file changed |
| T11 | `corpus/.../worldbible-integration-contract.md` (comment appended) | authority | 1 | `E2E-DIGEST` — read-set file changed |
| T12 | `tools/assemble-d2.py` (comment appended) | producer | 1 | `E2E-DIGEST` — read-set file changed |
| T13 | `.../components/12-rank-rules.yml` (comment appended) | not read | **0** | **FAIL-OPEN** — see F-18-04 |
| T14 | `examples/culture-d2/reviews/11-costumes.md` (comment appended) | prose surface | **0** | **FAIL-OPEN** — see F-18-04 |
| T15 | gate replaced by a lying stub (prints a fake clean scan, exit 0) | judge | 2 | `E2E-ARTIFACT` — could not read the FIELD_NAMES tuple |
| T16 | the frozen baseline edited (packet digest/declared values) | baseline | 2 | `E2E-BASELINE` — integrity digest mismatch, re-freeze required |
| T17 | component tamper **then** `--freeze` | re-pin attempt | 1 | freeze refuses; the tree stays red (`E2E-DIGEST`) |
| T17b | `packet.d2.yml` tamper **then** `--freeze` | re-pin attempt | **0** | **FAIL-OPEN by design** — see F-18-04 |
| T18 | `corpus/lessons/round-6-sources/05.json` (newline appended) | closed ledger | 1 | `E2E-DIGEST` — read-set file changed |
| T19 | `tools/d2-typed-labels.py` (comment appended) | producer | 1 | `E2E-DIGEST` — read-set file changed |

Additional matrix run at the earlier revision `38d1cba4` (19:09–19:11, `.scratch/r18/exercise-matrix-v2.json`,
`-v3.json`) recorded the same catch behaviour for T1–T9, T11, T12, T15–T17; T10 was still fail-open there because
`examples/culture-d3/expected.json` was not yet read — the rewrite fixed that (T10 now caught).

### 2.3 What "fail closed" means here, measured

- Drift of a read-set file → exit 1 `E2E-DIGEST`, naming the file (T3–T5, T7, T8, T10–T12, T18, T19).
- Drift of a component that only the assembler manifests name → exit 1 `E2E-DIGEST` with both digests (T1, T2, T4, T9).
- Missing artifact → exit 2 `E2E-ARTIFACT` (T6).
- Edited baseline → exit 2 `E2E-BASELINE` (T16); a re-signed scan expectation is refused (selftest control).
- A tampered judge (even one that lies about a clean scan) → non-zero, because the gate's bytes are both read
  and hashed (T8, T15).
- No FAIL-OPEN probe returns a "pass" while claiming success: T13/T14/T17b return a genuine exit 0 pass, which is
  why they are filed as a coverage boundary rather than a silent failure (§3, F-18-04).

## 3. Findings

### F-18-01 — OPEN (blocker for claim O as filed): the claim's counting command is red because O froze before D wrote

- Evidence: §2.1 (live run exit 1 at 19:15:30 and 19:16:23, `E2E-DIGEST`, typed-labels frozen `e70ba147…` vs live `a3aa452c…`).
- Cause: coordination, not defect. The D claim re-emitted `typed-labels.d2.yml` at ~19:13, after the O baseline was frozen
  (19:13, `reports/round-11/handoff/expected.json`).
- Impact: `python3 tools/exercise-handoff-e2e.py` and `reports/round-11/run-validation.py`'s O leg (which requires the
  exercise to exit 0; `reports/round-11/run-validation.py:1013-1197`) cannot pass until the baseline is re-frozen over the
  post-D bytes. The exercise is behaving correctly; the *claim state* is red.
- Owner: O integrator (re-freeze after the last write to any read-set file), or the parent (freeze last in the round).
  `--freeze` prints the old→new digests; re-freezing is the sanctioned, recorded act, so this is a bookkeeping step, not a
  re-decision.

### F-18-02 — RESOLVED in-tree (measured; recorded because it cost a lane check): baseline was placed under the battery's default baseline root

- What I measured at 19:10 (`tools/gates/expected/handoff-exercise/r11/expected.json`, sha256 `1ab17670…`):
  `python3 tools/check-gate-battery.py` gained **7 findings** over its pre-existing set — `BASELINE-GATE-UNKNOWN` ×1,
  `BASELINE-EXTERNAL-INPUT` ×5, `BASELINE-EXPECTED-ABSENT` ×1 — because `tools/check-gate-battery.py:114` reads
  `tools/gates/expected/**` as gate baselines. Battery without that directory: 2 findings (`BASELINE-GATE-UNCOVERED` ×2,
  pre-existing). Raw: `.scratch/batt-with.json`, `.scratch/batt-without.json`.
- `reports/round-11/handoff/design.md` §8 had explicitly forbidden that location ("Do not commit it under
  `tools/gates/expected/**`…"), so this was an implementation-vs-design divergence.
- Resolution observed 19:13–19:14: the directory is gone, the default baseline is `reports/round-11/handoff/expected.json`,
  and the battery re-measured at exactly the pre-existing 2 findings (`.scratch/batt2.json`).

### F-18-03 — RESOLVED in-tree (measured): `--selftest` was red at the two revisions before the rewrite

- At revisions `c202927e` (19:06) and `38d1cba4` (19:08–19:11) `--selftest` exited 1 with an uncaught
  `AssertionError`: the fixture root copied `FIXTURE_INPUTS` (sources + tools) but not the component files that
  `verify_component_digests()` re-measures — `cannot hash examples/culture-d2/components/02-phonology.yml`.
- A second, independent selftest defect existed in that revision: the placeholder control prepended `TBD` to `- OQ-01:`
  while the gate's rule is "first non-placeholder occurrence wins". Measured directly on the committed gate and the frozen
  packet: gate **exit 0**, `INFO scan: fields=16/16 glossary-entries=20 findings=0`, so the control's
  `assert gate["exit"] == EXIT_FAIL` (line 1304, rev `38d1cba4`) could not pass even after the fixture fix.
- State at filing: `--selftest` exits 0 and names positive, malformed, missing-artifact, baseline-tamper, read-set-tamper,
  scan-tamper and preservation controls (measured 19:16:23, rev `d5b346b8`). Claim O's "positive + malformed controls" leg
  is satisfied *on the current revision*.

### F-18-04 — OPEN (scope boundary, needs a declared rule): coverage equals the read set; `--freeze` can bless packet-level drift

Three probes pass — none of them hides a failure, but each is a place where a reader might assume coverage that does not exist:

1. **T13** `examples/culture-d2/components/12-rank-rules.yml` — one of the D2 components not merged into `packet.d2.yml`
   (the packet's `assembly.source_sha256` covers 9 of the 15 component files; measured 19:16:23: the file hashes
   `28696a5a7040…` and no check reads it). The exercise re-measures the 9 D2 + 4 D3 component digests the assemblers
   recorded (13/13 matched) — that is the boundary.
2. **T14** `examples/culture-d2/reviews/11-costumes.md` — review prose, never an input.
3. **T17b** `packet.d2.yml` tamper **then** explicit `--freeze`: re-freeze exit 0, exercise exit 0 thereafter. The act is
   recorded — `freeze.txt` prints `re-frozen input examples/culture-d2/packet.d2.yml: e0f21509e14a… -> e7bf7b1e3543…` —
   but nothing re-runs the producers' own consistency check. Measured in the same sandbox immediately after the bless:
   `python3 tools/assemble-d2.py --check` → **exit 1** "packet.d2.yml differs from deterministic assembly", while
   `python3 tools/exercise-handoff-e2e.py` → exit 0. So a blessed packet can be internally inconsistent with its
   components without the exercise noticing. (Component-level tamper cannot be blessed the same way: T17 shows the freeze
   refuses, exit 1.)
- Recommendation (owner: O integrator / claimant, not this review): state the rule "coverage = the 21 read-set files +
  the 13 component files the assemblers name" in the packet's `limits`/`open_questions`, and add the assemblers' own
  `--check` to the exercise's validation leg (or to the O leg of `run-validation.py`) so a blessed inconsistent packet is
  caught by something.

### F-18-05 — OPEN (note): three baseline fields are evidence-of-record, not enforced checks

Sweep at rev `d5b346b8`: the only baseline keys compared at run time are `profile`, the declared block
(`expected_exit`, `expected_finding_ids`, `expected_scan`), `inputs` (21 files), `packet_sha256`, `glossary_entry_ids`
and `baseline_digest` (`tools/exercise-handoff-e2e.py:1345-1428`). `field_digests` (:1482), `cross_refs` (:1483) and
`counts` (:1492) are written at freeze time and read nowhere else in the tool (`grep -n '"counts"\|field_digests\|cross_refs"'`
returns only the freeze-side writes). They are useful as frozen evidence for a human reader, but tampering them would not
be caught. Low severity: `baseline_digest` already makes any baseline edit detectable, so this is a documentation-of-record
note, not a hole.

### F-18-06 — OPEN (note): the frozen baseline is untracked at filing time

`git status --porcelain` (2026-10-17T19:16) lists `?? reports/round-11/handoff/` and `?? tools/exercise-handoff-e2e.py`.
Workers never commit (lane rule), so this is expected; the parent's admission step must commit the tool *and* the baseline
together, or claim O's "committed expected.json baseline" leg is satisfied only on disk.

## 4. What passed (positive evidence, revision `d5b346b8`)

- **17/20 tamper probes fail closed** (§2.2), including the byte-only and malformed classes and a lying gate stub.
- **A real, unscheduled drift was caught** (§2.1).
- **Selftest green with named controls**, exit 0 (19:16:23).
- **Read-only over the lane**: sha256 over every file of a sandbox tree before/after two normal runs is identical; the
  isolated packet directory lands under `TMPDIR` (`…/.scratch-ex/handoff-e2e-<rand>/isolated`) and is cleaned up
  (no leftover entries). The gate really runs from that foreign cwd — the `gate-exit` record names it.
- **Deterministic**: two runs differ only in the random temp-directory path in the `gate-exit` line.
- **Lane checks untouched by the relocation**: gate battery back to its pre-existing 2 findings (19:14).
- **Committed baseline sane**: 21 pinned inputs, all 21 verified equal to live bytes at 19:15 (`inputs` loop re-measured
  by this review); `declared` block equals the tool's constants.

## 5. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch

# live state (red at filing, see F-18-01)
python3 tools/exercise-handoff-e2e.py                      # exit 1 E2E-DIGEST (typed-labels re-emitted by D)

# the matrix (fresh sandbox per probe; mutates nothing in the repo)
bash .scratch/r18/mksandbox.sh <tag>                       # tar copy of the lane tree, minus .git/.scratch
python3 .scratch/r18/matrix4.py                            # 20 probes -> .scratch/r18/exercise-matrix-v5.json

# battery impact of baseline placement
(cd .scratch/r18/sandbox-batt2 && TMPDIR=$PWD/.scratch-ex python3 tools/check-gate-battery.py)  # 2 findings, pre-existing
```

## 6. Revision history observed during this review (so a re-reader can tell what was measured when)

| time (local) | tool sha256 (first 16) | state |
|---|---|---|
| 19:06 | `c202927e36fc2afa` | first appearance; baseline absent; `--selftest` crashed |
| 19:08–19:11 | `38d1cba4…` | run green; baseline committed under `tools/gates/expected/handoff-exercise/r11/`; selftest red (F-18-03) |
| 19:12–19:13 | `c896eb14…`, `708d8d5b…`, `6d3a34d0…`, `e4301461…` | mid-rewrite; live run exit 2/1; baseline relocated and old dir removed (F-18-02 fixed) |
| 19:15 | `e74e5aea…` | stable; selftest 0; matrix v4 (17/20) |
| 19:16 | `d5b346b8…` | **filed revision**; selftest 0; matrix v5 reproduces 17/20; live run red on the real D drift |

## 7. Limits of this review

- I reviewed the **drift/fail-closed question and the tamper response only**, plus adjacent observations. Envelope
  completeness and placeholder-vs-live content are O16/O17's remit; D2/D3 semantics and the packet's *quality* are
  lore's and the domain gates'; canon decisions are out of province.
- I did **not** run `reports/round-11/run-validation.py` (it writes shared round files; not my file set). Its O leg's
  requirements were read from source only.
- I did **not** verify the read-set digests in the committed baseline against an independent copy of history — only
  against live bytes at 19:15 (21/21 equal).
- The tool was moving while I reviewed; findings F-18-02/F-18-03 are historical (resolved), F-18-01/F-18-04/F-18-05/F-18-06
  are open **at revision `d5b346b8`** and must be re-checked if the file changes again. Every exit code above carries the
  revision it was measured at.
- Tamper probes exercise the *mechanism* on sandbox copies; they do not prove the absence of other fail-open classes —
  the sweep is 20 probes over the classes named in §2.2, not exhaustive.

## 8. Receipts (commands, outputs, timestamps)

```sh
# 2026-10-17, lane repo root, TMPDIR=$PWD/.scratch unless noted
python3 tools/exercise-handoff-e2e.py --quiet                      # 19:16:23 exit 1 E2E-DIGEST (typed-labels drift)
python3 tools/exercise-handoff-e2e.py --selftest                   # 19:16:23 exit 0 (controls named)
sha256sum tools/exercise-handoff-e2e.py                            # d5b346b877be098f… (filed revision)
sha256sum reports/round-11/handoff/expected.json                   # c8abc7990bded965… (21 pinned inputs)
sha256sum examples/culture-d2/typed-labels.d2.yml                  # a3aa452cd5ae77c3… (post-D re-emission)
python3 tools/assemble-d2.py --check                               # 19:03 exit 0 (live tree regenerates byte-identically)
python3 .scratch/r18/matrix4.py                                    # 19:16 20 probes -> 17 CAUGHT / 3 open (matrix-v5.json)
(cd .scratch/r18/sandbox-batt2 && python3 tools/check-gate-battery.py)  # 19:14 exit 2; findings = BASELINE-GATE-UNCOVERED ×2
```

Scratch evidence (not filed): `.scratch/r18/{tampers.py,matrix4.py,exercise-matrix-v2..v6.json,prematrix.json}`,
`.scratch/batt-with.json`, `.scratch/batt-without.json`, `.scratch/batt2.json`.

## 9. Filing-time update (2026-10-17T19:17–19:18, after §1–§8 were written)

The O seat re-froze the baseline while this review was being written, exactly along F-18-01's axis:

```
# 19:17:29, lane repo root, TMPDIR=$PWD/.scratch
$ python3 tools/exercise-handoff-e2e.py --quiet
handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 packet_sha256=6583b6bdbf5e3fe0…
$ python3 tools/exercise-handoff-e2e.py --selftest          # exit 0
$ sha256sum reports/round-11/handoff/expected.json
a94f9ded9d0938ec1510a1834b83162635c9e94a04b70461d5db0b98a0031d7a  reports/round-11/handoff/expected.json
```

- Baseline re-frozen (sha256 `a94f9ded…`; earlier same-window values `c8abc799…` → `55ec3b03…`); all **21** pinned inputs
  re-measured equal to live bytes at 19:17 (0 mismatches), typed-labels pinned at `a3aa452cd5ae77c3…`.
  `freeze.txt` records the move: `re-frozen packet_sha256: 72739729… -> 6583b6bd…`.
- **F-18-01 is therefore resolved in-tree at 19:17** (was red 19:15:30–19:16:23). The mechanism of the catch is unchanged;
  only the pin moved.
- The tool changed twice more during this window (`e74e5aea…`→`d5b346b8…`→`a21934ade22b2cda`). The tamper matrix was
  re-run at `a21934ad` (19:18, `.scratch/r18/exercise-matrix-v6.json`): **17 CAUGHT / 3 open, identical per-probe verdicts**
  to the `e74e5aea` and `d5b346b8` runs tabulated in §2.2.
- `python3 tools/d2-typed-labels.py --check` now exits 0 (19:17) — the D workstream's re-emission closed the round-10 A2
  stale-projection drift that this review's T7 probe uses; the probe still catches a deliberate re-tamper.
- Conclusion at filing: **claim O's executable legs are green (run exit 0, selftest exit 0, battery unaffected); the
  drift question is answered by §2.2 with 17/20 probes failing closed and the three open items in F-18-04/§3.** Because the
  tool is still being edited, re-check by hash: if `tools/exercise-handoff-e2e.py` differs from `a21934ad…`, re-run
  `python3 .scratch/r18/matrix4.py` and `python3 tools/exercise-handoff-e2e.py --selftest` before quoting §2.2.

— R11-O18, 2026-10-17T19:18-03:00.
