# lexicon-coverage-audit baseline — independent re-run (round 9, rerunner seat R9-O)

- **Role:** rerunner — paired seat to the baseline author. This seat writes only this file
  (`reports/round-9/baselines/lexicon-coverage-audit/rerun.md`); the author seat owns
  `tools/gates/frozen/lexicon-coverage-audit/r9-pre/{packet.yml,expected.json,run.log,freeze.txt,digests.sha256}`
  and `reports/round-9/baselines/lexicon-coverage-audit/author.md`. Nothing here was committed; the
  orchestrator integrates once per round. No lane file was modified by this seat (scratch lives
  outside the repo, §1).
- **Date:** 2026-10-17; commands ran 17:47–17:53 (-03:00) = 20:47–20:53Z; UTC receipts inline.
- **Revision binding (re-measured by this seat, not copied from the author):**
  `git rev-parse HEAD` → `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`;
  `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355..HEAD` → `reports/round-9/claims.json`
  (34) + `reports/round-9/targets.json` (125), 159 insertions, 0 deletions;
  `git diff --stat e1694ba..HEAD -- tools corpus examples` → **empty** (exit 0), so the graded tree
  is byte-identical between the claim's declared baseline revision and HEAD.
  `git status --porcelain -- tools/gates/lexicon-coverage-audit.py tools/gates/fixtures/lexicon-coverage-audit.{yml,expected}`
  → **empty**: the gate and its fixture pair are clean.
- **Gate under test:** `tools/gates/lexicon-coverage-audit.py`, sha256
  `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287` (recomputed by this seat,
  equals the `gate_sha256` pin in `expected.json`).
- **Standard followed:** `corpus/knowledge/verification/gate-frozen-run-standard.md` §4 (required
  `expected.json` fields), §5 (freeze procedure), §6 (verify procedure, tamper semantics, class
  mapping). Self-test = capability, frozen run = measurement (§2).

## 1. Environment limit measured during this re-run

- `/tmp` was **inode-exhausted** for the whole run: `df -i /tmp` → `tmpfs 1048576 1048576 0 100%
  /tmp` (2026-10-17T20:47Z). Everything below therefore ran with scratch on the root filesystem:
  `/var/tmp/r9-lexicon-rerun/` (`df -h /` → 782G available), `TMPDIR` redirected there, and the
  copied tree at `/var/tmp/r9-lexicon-rerun/verify/tree` (446M; full delivered tree copy excluding
  `.git` and `__pycache__`). This is the same hazard the round-8 O-audit and the phonology rerunner
  recorded; status here: **hazard observed, no evidence lost, no lane path blocked.**

## 2. Capability re-executed: `--selftest` in an isolated mirror (never the live tree)

| # | Command | Observed |
|---|---|---|
| 1 | `cp tools/gates/lexicon-coverage-audit.py` + `fixtures/lexicon-coverage-audit.{yml,expected}` into `/var/tmp/r9-lexicon-rerun/mirror/tools/gates/` | mirror digests equal the live digests (yml `a1b8ed7c…`, .expected `bd20bb40…`) |
| 2 | `python3 tools/gates/lexicon-coverage-audit.py --selftest` (cwd = mirror, `TMPDIR` off /tmp) | exit **0**; 14 `PASS` lines; `selftest: 14/14 checks passed` |
| 3 | `sha256sum` of the mirror fixture pair after the selftest | unchanged (`a1b8ed7c…`, `bd20bb40…`) — the selftest regenerates its fixture byte-identically |

- This re-executes capability only; per §2 it never substitutes for the frozen run.

## 3. Measurement this seat minted itself (before the author's `expected.json` was read)

Purpose: an independent reference verdict for the frozen snapshot, not derived from any author
artifact. Input: byte copy of the committed fixture (`tools/gates/fixtures/lexicon-coverage-audit.yml`).

| # | Command (cwd = mirror) | Observed |
|---|---|---|
| 1 | `cp tools/gates/fixtures/lexicon-coverage-audit.yml pre/packet.yml` | sha256 `a1b8ed7c3548ace7a631b6b2752673f6a65a44896caecef170e373d67ec59187` |
| 2 | `python3 tools/gates/lexicon-coverage-audit.py pre/packet.yml > baseline-run.log` | exit **1**; 20 `FINDING` lines / **18 unique IDs**; stderr **0 bytes**; stdout sha256 `af5794955b60b455b433a570434bf0ab69c110b66c891eab567d5addef0be4f4` |
| 3 | unique-ID set vs `tools/gates/fixtures/lexicon-coverage-audit.expected` (both `sort -u`, `diff`) | **empty diff — 18/18 IDs identical** |
| 4 | digest re-check of `pre/packet.yml` after the run | `OK` → gate is read-only over its input |
| 5 | context only: D2 packet `examples/culture-d2/packet.d2.yml` (sha256 `e0f21509…`) | exit **0**, 0 findings — matches the round-3 frozen row; not baseline evidence (§3 forbids live-path verdicts) |

Two runs of step 2 in the mirror are byte-identical, so the verdict is not order- or path-dependent.

## 4. Committed-baseline verification (the pair's deliverable)

All of the following re-executed by this seat against the delivered tree and its byte copy; no value
below is copied from `author.md`.

### 4.1 Artifact digests at verification time (sha256)

| artifact | sha256 |
|---|---|
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/packet.yml` | `a1b8ed7c3548ace7a631b6b2752673f6a65a44896caecef170e373d67ec59187` |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/expected.json` | `0fad58ba70d545328d015990de5184bdd371e575810eb7e79c96bcc7c8a4ff9c` |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/run.log` | `af5794955b60b455b433a570434bf0ab69c110b66c891eab567d5addef0be4f4` |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/freeze.txt` | `4909a6b49b838e96c8ca00bf049b832dc55332243342b59222e42a4d56a6d788` |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/digests.sha256` | `4d392240e61c63cc2146d05bb1e354c0b75cd33d9603e7ea33a428a83c0c2f25` |
| `reports/round-9/baselines/lexicon-coverage-audit/author.md` | `89ee7c56b3392e8ceeb4832f4f00ceb1e331351c790748e7b849ded4962b880d` |

Command: `sha256sum` over both shard directories, 2026-10-17T20:52Z.

### 4.2 Checks, each one re-run by this seat

| # | Check (standard §6 order) | Command | Observed | Result |
|---|---|---|---|---|
| 1 | snapshot provenance | `cmp r9-pre/packet.yml tools/gates/fixtures/lexicon-coverage-audit.yml` | identical; digest equals the live fixture digest | byte copy confirmed |
| 2 | **digest check first** | recompute `inputs` map vs file | `packet.yml`: pin `a1b8ed7c…` = recomputed `a1b8ed7c…` | match |
| 3 | gate revision | recompute gate sha256 vs `gate_sha256` pin | `2c4dd397…` = `2c4dd397…` | match (gate not revised) |
| 4 | command re-run in the copied tree | `python3 tools/gates/lexicon-coverage-audit.py tools/gates/frozen/lexicon-coverage-audit/r9-pre/packet.yml` (cwd = `…/verify/tree`) | exit **1**; 20 lines; 18 unique IDs; stderr 0 | equals `expected.exit` and `expected.findings` |
| 5 | finding-ID set compare | `sort -u` diff vs `expected.findings` | empty | **set match, including both repeated IDs** (`C-entry-unevaluable` ×2, `D-stage-mismatch` ×2) |
| 6 | per-ID counts | dict compare vs `expected.finding_counts` | 18 entries, 20 lines total | match |
| 7 | whole-output pin (advisory) | stdout sha256 vs `stdout_sha256` | `af579495…` = `af579495…` | match |
| 8 | committed `run.log` | `cmp` vs this seat's fresh stdout | byte-identical | match |
| 9 | determinism | second full run in the mirror | stdout sha256 `af579495…` again | two independent runs + committed log all byte-equal |
| 10 | post-run integrity | `sha256sum -c digests.sha256` in the baseline dir | `packet.yml: OK` (exit 0); live fixture, gate, `run.log`, `expected.json` digests unchanged | no write-back |

`expected.json` parses as JSON with `schema: "kotodama-frozen-run-v1"`; every §4-required field is
present and each value above was re-measured, not accepted.

## 5. Tamper semantics reproduced (§6, load-bearing point)

Everything on throwaway copies under `/var/tmp/r9-lexicon-rerun/`; no frozen or committed byte edited.

| # | Condition | Command | Observed | Class per §6 |
|---|---|---|---|---|
| 1 | input edited | append `\n# tampered byte\n` to a copy → `sha256sum -c digests.sha256` | `packet.yml: FAILED`, exit **1**; tampered digest `e1b738b7474d62047cee8c4d6691b046573529422cd7593d8a142a85b79651ea` (= the author's recorded `tampered_copy_sha256`) | `snapshot_tampered` → could-not-evaluate (exit 2); comparison refused |
| 2 | gate over the tampered copy | `python3 <mirror>/tools/gates/lexicon-coverage-audit.py tampered/packet.yml` | exit **1**, same 18-ID set, stdout **byte-identical** to the untampered run | the run alone cannot see the edit — only the digest step detects it |
| 3 | gate bytes edited | sha256 of a gate copy with one appended line | `32b8e261…` ≠ pin `2c4dd397…` | `gate_revised` → could-not-evaluate (exit 2); re-freeze, never compare |

## 6. Verdict for the baseline

**Baseline `lexicon-coverage-audit / r9-pre` is VALID as frozen-run evidence.** Digests match,
`gate_sha256` matches, the command re-executed in a copied tree reproduces exit 1 with exactly the
committed 18-ID set (20 lines, counts equal), stdout is byte-identical across two independent runs
and the committed `run.log`, the tampered snapshot is refused, and a deliberately edited gate reads
`gate_revised`. Reading per §6 row 1: compared verdict, **match**, class `findings`, check would
exit 0.

Scope limits of this verdict:

- It says nothing about the fixture packet's design quality — the input is the gate's own fictional
  planted-defect fixture, and a `findings` verdict here is the fixture behaving as planted.
- The `snapshot_tampered` / `gate_revised` reads above are the **interim external** checks literally
  executed (external `sha256sum -c`, external sha256 of the gate). The in-tool mapping — battery
  validating every committed `expected.json`, tampered snapshot → could-not-evaluate inside
  `tools/check-gate-battery.py` — is shard **R9-O15's** deliverable and is **not** claimed here; the
  gate has no `--frozen` mode (standard §8 open item, unchanged by this round's O work).
- The baseline is **on-disk (untracked) evidence today**: `git status --porcelain -- tools/gates/frozen/lexicon-coverage-audit reports/round-9/baselines/lexicon-coverage-audit`
  → `??` for both directories. Only the orchestrator's round-9 integration commit makes it
  committed evidence (§5 step 7); until then, no conformance claim may cite it.

## 7. Measured observations for the integrator (reported, not absorbed)

1. **Baseline-root divergence (round-9, measured 2026-10-17T20:52Z).** `find` over `reports/round-9`,
   `tools/gates/frozen`, `tools/gates/expected` → `expected.json` files are landing under **three**
   roots this round:
   - `tools/gates/frozen/lexicon-coverage-audit/r9-pre/expected.json` (this gate, canonical §3 layout);
   - `reports/round-9/baselines/{handoff-packet-check,myth-consistency-gate,naming-collision-gate}/expected.json`;
   - `tools/gates/expected/{costume-era-consistency-gate,phonology-sanity-gate}/r9-pre/expected.json`
     (+ `tools/gates/frozen/handoff-packet-check/r9-pre/expected.json`).
   This gate has **exactly one** copy repo-wide (duplicate sweep: one hit), so bare id `r9-pre`
   resolves under exactly one gate directory here — but a battery discovery rule (R9-O15) that scans
   only one root will miss gates; a union sweep is needed. Reported to R9-O15/R9-O17 via the
   author's `author.md` §6 as well.
2. **Finding-ID extraction gotcha, recorded so no validator repeats it:** IDs contain lowercase
   letters; extracting with `grep -o '^FINDING [A-Z0-9-]*'` truncates every ID at its first
   lowercase character (measured: 20 bogus one-letter tokens). Working forms:
   `re.findall(r'^FINDING ([A-Za-z0-9-]+):', text, re.M)` or
   `grep -o '^FINDING [A-Za-z0-9-]*' | sed 's/FINDING //'` — the colon must not be captured into
   the ID. (Independent of the author's note in `author.md` §3.9, same failure mode from the other
   side.)
3. **No gate behavior change:** the recomputed gate digest equals the pin, `git status` for the gate
   is clean, and no gate file under `tools/gates/` was touched by this shard or (per digest) by the
   author shard.

## 8. What this seat did not do

- No write inside the lane repo except this file; no commit, no push (orchestrator integrates).
- No claim about the other six gates' baselines (sibling shards) beyond the §7.1 discovery sweep.
- No battery modification and no in-tool tamper mapping (R9-O15); no registry rows (R9-O17); no
  gate `--frozen` mode.

**check result: baseline valid — digests match, observed exit and finding-ID set equal expected
(exit 1 / class `findings`), tampered snapshot refused, edited gate reads `gate_revised`; pair's
frozen-run deliverable confirmed by an independent seat.**
