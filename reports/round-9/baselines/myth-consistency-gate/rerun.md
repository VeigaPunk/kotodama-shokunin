# myth-consistency-gate baseline — independent re-run (round 9, rerunner seat R9-O)

- **role:** rerunner — second worker of the `myth-consistency-gate` baseline pair (author +
  independent auditor). This worker writes only this file
  (`reports/round-9/baselines/myth-consistency-gate/rerun.md`); the author seat owns
  `expected.json`, `packet.yml`, `run.log`, `freeze.txt` and `author.md` in the same directory.
  Nothing here was committed; the orchestrator integrates once per round.
- **date:** 2026-10-17, UTC timestamps in the receipts below (`date -u`).
- **lane revision:** `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (HEAD, `git rev-parse HEAD`;
  `git cat-file -t a7bb205…` → `commit`). Declared round-9 `baseline_revision` is
  `e1694bad6ac96aca45a11ca5746582b275929355` (`git cat-file -t` → `commit`). Measured
  `git diff --stat e1694ba..HEAD` → claims.json 34+ / targets.json 125+, `2 files changed,
  159 insertions(+), 0 deletions`; scoped `git diff --stat e1694ba..HEAD -- tools corpus
  examples` → **empty**. The gate, the graded packet and the fixtures are byte-identical at
  the declared revision and at HEAD (three-way digest match below), so every pin here binds
  to both — recorded, not assumed.
- **gate under test:** `tools/gates/myth-consistency-gate.py`,
  sha256 `5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08`
  (worktree == `git show HEAD:…` == `git show e1694ba:…`).
- **fixture pair (capability evidence):** `tools/gates/fixtures/myth-consistency-gate.yml`
  `f94a700cc2d6cfadf91d8c96493fdc1e87dd50e53aa117d7598f12f524197086`;
  `…/myth-consistency-gate.expected`
  `c871b6d33c2a29f74d17ce7642c73e328a0b212fddd618699c4a3c8464f45abb`.
- **standard followed:** `corpus/knowledge/verification/gate-frozen-run-standard.md` §4
  (required fields), §5 (freeze), §6 (verify, tamper semantics, class mapping), §7/§9 (first
  real baseline grades the D2 packet; this gate's turn in the §9 gate order).

## 0. Environment limit measured during this re-run

- `/tmp` was **inode-exhausted** for the whole run: `df -i /tmp` →
  `tmpfs 1048576 1048576 0 100% /tmp`, and a write probe (`echo test > /tmp/.spaceprobe`) →
  `No space left on device` (2026-10-17T20:4xZ; same condition round 8's audit documented).
  By-volume space was free (`df -h /tmp` → 8.5G avail): inode pressure under the 64-worker
  wave, not a full disk.
- All scratch for this seat lived **outside the repository** at `~/.cache/kotodama-r9-myth/`
  (on `/home`, 782G free). Status: **hazard observed, not a blocker** — every command below
  ran. No repository file was created, modified or deleted by this seat; §4's digest
  re-check of the graded files after every run is the evidence.

## 1. Capability re-executed in an isolated mirror (not the live fixtures)

| # | Command (2026-10-17T20:49Z) | Observed |
|---|---|---|
| 1 | `cp -r tools/gates ~/.cache/kotodama-r9-myth/mirror-tools/tools/` | copied; `sha256sum` manifest of every mirror file identical before and after the selftests (`diff` → IDENTICAL) |
| 2 | `python3 <mirror>/tools/gates/myth-consistency-gate.py --selftest` ×2 | exit **0** both runs; stdout sha256 `80e7d9dc86a29cf56591cfa0cf5bd8fab82a84d4b9d67f03200f1bd689c5aa53` identical across runs |
| 3 | output, verbatim | `selftest: OK — fixture exit 1; planted IDs present: MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02; clean control exit 0 (0 findings); fixture and expected verified against the embedded constants under tools/gates/fixtures/` |
| 4 | `git status --porcelain` after | no tracked modification attributable to this seat |

- Capability only; per standard §2 it never substitutes for the frozen run. Determinism
  measured: two runs left every mirror file byte-identical.

## 2. Independent reference measurement this seat minted itself (before reading the baseline)

Purpose: fix this gate's verdict contract independently first, so §4 compares two
measurements, not a paraphrase.

| # | Command | Observed |
|---|---|---|
| 1 | `cp tools/gates/fixtures/myth-consistency-gate.yml <scratch>/ref/packet.yml` | digest = fixture digest `f94a700c…` |
| 2 | `python3 tools/gates/myth-consistency-gate.py <scratch>/ref/packet.yml > run.log` | exit **1**; six FINDING lines; stdout sha256 `88385088ca2ee13192b9669a02cbe44aebf9c22df752a2af76138a13e1cf77d2`; stderr 0 bytes |
| 3 | ID set vs committed `.expected` (order-insensitive) | identical 6/6: `MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02`; stdout order is P01, P02, **M02, M01**, S01, S02 — standard §4's set-not-order rule holds |
| 4 | negative probes: missing path / scalar root / `name: ""` | each exit **2**, `FINDING G-DATA:` (`cannot read …` / `expected 'key: value'…` / `packet \`name\` is missing or empty`) |
| 5 | probe `name: probe` only | exit **1**, three HOLDs: `MC-P00`, `MC-M00`, `MC-S00` |
| 6 | tamper calibration: byte copy + `printf '\n# tampered byte\n' >>` | digest changed; gate over the tampered copy → exit 1, **same six IDs** — the run cannot see the edit; only the digest check reads `snapshot_tampered` |

- **Input surface attested by reading the gate, not assumed:** the only graded-run read is
  `path.read_text(...)` at `tools/gates/myth-consistency-gate.py:849` (`path = Path(argv[0])`
  at `:847`); no `getenv`/`environ`, no network imports; the remaining `open()`/`subprocess`
  sites are `--selftest`-only (inside `tools/gates/fixtures/`). So for a baseline run the
  full read set is **exactly the one snapshot file**, and the `inputs` pin can be checked to
  exhaustion.

## 3. Measurement over the graded snapshot (the author's `packet.yml`)

| # | Command (2026-10-17T20:5xZ) | Observed |
|---|---|---|
| 1 | `cmp reports/round-9/baselines/myth-consistency-gate/packet.yml examples/culture-d2/packet.d2.yml` | byte-identical (exit 0) |
| 2 | `sha256sum` both | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` both; equal at `e1694ba` and in the worktree |
| 3 | `python3 tools/gates/myth-consistency-gate.py examples/culture-d2/packet.d2.yml > d2-run.log` | exit **0**; **zero FINDING lines** (stdout 0 bytes, sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` = empty-string digest); stderr empty |
| 4 | packet digest re-checked after the run | unchanged `e0f21509…` → the gate is read-only over its input |

- Consequence, checked against the author artifacts in §4: a clean verdict on this gate is a
  **legitimate empty stdout**, so a 0-byte `run.log` is the verbatim artifact, not an
  unfinished freeze. The author's `expected.json` (`stdout_note`) and `freeze.txt` state
  this explicitly, so a later reviewer cannot read the empty file as a broken freeze.
- What this is: a measured engineering verdict (`clean`, exit 0) over immutable bytes. What
  it is **not**: canon, design approval, or a claim that the D2 packet is coherent in the
  myth sense — the kernel grades its checkable subset only (gate docstring: §3/§4/§6; era
  alignment and semantic comparison remain manual review).

## 4. Committed-baseline verification — the pair's deliverable (the core)

**Artifact digests at verification time** (2026-10-17T20:57–21:0xZ; these exact bytes were
verified — a later edit to any of them voids this receipt):

| file | sha256 |
|---|---|
| `expected.json` | `a87edc5327112367e310c6ff3b24bf099e704e0109e278f1c04e0443db5215b4` |
| `freeze.txt` | `ed066e15cee6dfb63cb75e9bfb4a54d87d52ba80890b4b37aa2324fd0f7b477d` |
| `packet.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `run.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (0 bytes) |
| `author.md` | `afff897e0d11fd1ba8571a88bbd80a736d296677f6bf0580a9b41e500eab09ba` |

Verification driver: `~/.cache/kotodama-r9-myth/verifier.py` (auditor-written, stdlib only,
out-of-repo, receipt at `…/verify-receipt.json`); it copies the gate and snapshot into a
mirror tree and runs the gate there — never a live path.

| step (standard §6 order) | Command / method | Observed | Class |
|---|---|---|---|
| 1 digest check | recompute `inputs.packet.yml` vs the pin | `e0f21509… == e0f21509…` — **match** | pass |
| 2 gate-revision check | sha256 live gate vs `gate_sha256` | `5368b135… == 5368b135…` — **match** | pass |
| 3 verdict compare | gate over the snapshot **copy** in the mirror (`different cwd`) | exit **0**; finding-ID set **`[]`**; stdout sha256 `e3b0c44…`; equals `expected.exit 0` / `class clean` / `findings []` — **verdict match** | `clean`, check exits **0** (`compared-match`) |
| C-A tamper control | copy + append `"\n# tampered byte (rerun control A)\n"`, re-check digest, re-run gate | digest check **refuses** (`snapshot_tampered`, could-not-evaluate); the gate over the tampered copy still exits 0 with the same (empty) finding set — **invisible to the run**, exactly the standard §6 calibration case | pass |
| C-B gate-revision control | gate copy + one appended comment byte into the mirror | sha256 `382e39915a15bc4f87db27bfdde75e4890b7951af6de846369960eefcb8cbe30` ≠ pin → check **refuses** (`gate_revised`) | pass |

**Author claims reproduced byte-exactly by this seat** (independent re-derivation, same
outcomes):

- tamper copy digest: author claims `265bd5c6a37fd90a5e0692ce39a6564622e0a787bc4293cf7dcedf944f7009d7`
  → my reproduction of the same procedure: **`265bd5c6…` — equal**; gate over it: exit 0,
  0-byte stdout.
- semantic mutant (MOT-04 `index_checked: true` → `cf_atu: "ATU 1200"` + `index_checked: false`,
  one replacement site): author claims `2e6c2d675f985dd6f6de5f42c8edcb6943f26de1b83661ec7b1c4fc0a932da5c`
  → my reproduction: **`2e6c2d67…` — equal**; gate exit **1**, exactly one line:
  `FINDING MC-M02: motif MOT-04 claims comparison 'ATU 1200' without a checked entry, edition, or narrative witness [spec §4 MC-M02]`
  (stdout sha256 `fd38e9e202466bddca4c7290fdb74d89ebf1b6bcc742dfadd4b9bd868779ffe2`).
  This is the **non-vacuity proof**: the clean frozen verdict is contingent on the graded
  bytes, not on a gate that cannot fail here.
- `run.log` byte-compare: author's frozen `run.log` vs this seat's independent stdout
  (`d2-run.log`) → `cmp` clean, **byte-identical** (both empty). Two independent runs of the
  same bytes produced the same verbatim output.
- revision field: `revision: a7bb205…` resolves to a commit; `revision_note`'s claim that the
  graded tree equals the declared `e1694ba` tree was independently measured by this seat
  (scoped diff empty, three-way digest matches in the header).

**Integration note (verified, author-flagged):** `.gitignore:3` is `*.log`, and
`git check-ignore -v reports/round-9/baselines/myth-consistency-gate/run.log` →
`.gitignore:3:*.log …` (exit 0). The orchestrator must `git add -f` the 0-byte `run.log` or
the baseline commits without its verbatim stdout.

**Interim-check disclosure (standard §6 step 1 / §8):** the gate has no internal
`--frozen` mode; the digest step ran externally (this seat's verifier, and independently
`sha256sum` comparisons), exactly the interim arrangement the standard's §8 table declares.

## 5. Cross-shard layout observation (reported, never absorbed)

Measured 2026-10-17: three different baseline roots are in use simultaneously —

- `reports/round-9/baselines/naming-collision-gate/` (naming author; its `expected.json`
  names `reports/round-9/baselines/*/expected.json` as the battery-extension discovery glob);
- `tools/gates/expected/costume-era-consistency-gate/r9-pre/` (costume author);
- `tools/gates/frozen/handoff-packet-check/r9-pre/` (handoff author; the standard §3 root).

The myth author landed in `reports/round-9/baselines/myth-consistency-gate/`, verified in
place here. Where a round-9 baseline must live is a cross-shard decision for the
orchestrator: **the R9-O15 battery extension's discovery glob must match the decided root(s),
or gates whose authors chose another root will read as missing baselines.** Reported fact, no
action taken in this seat. Battery state at this write time (measured): `python3
tools/check-gate-battery.py --selftest` → exit 0, `SELFTEST OK 10/10 controls behaved as
expected`; no `expected.json`/baseline-validation code present in `tools/check-gate-battery.py`
yet — validation of this baseline by the extended battery is pending R9-O15.

## 6. What this pair proves — and what it does not

- **Proves:** these exact bytes (packet `e0f21509…`, gate `5368b135…`) produced this exact
  verdict (exit 0, no findings) under a named revision; the verdict reproduces from a copy in
  isolation (three paths: live path, this seat's ref copy, and the mirror copy — all
  byte-identical stdout); any edit to the snapshot reads `snapshot_tampered` rather than a
  silent pass; the verdict is sensitive to a two-token semantic edit (mutant → exit 1).
- **Does not prove:** that the D2 packet is good design, that a clean myth verdict means the
  packet's myth content is coherent beyond the kernel subset, or that lore accepted anything.
  A matching digest proves byte identity, never design quality (standard §10).
- **Trust boundary (disclosed):** the verifier is same-seat tooling and belongs to the trusted
  base (standard §10, KTD-FR-S-0007) — the digest chain proves the baseline bytes, not that
  this seat's driver is honest. Independent-of-the-author yes (different worker, different
  tooling, different scratch tree); independent of the lane's toolchain no — deterministic
  re-execution is what lets a stranger repeat §1–§4 (KTD-FR-S-0008).
- **Two-evidences status for this gate after this pair:** selftest (capability) green and
  re-executed; frozen run (measurement) present and verified ⇒ the clause is met for this
  gate pending integration (force-add of `run.log`, registry row by the R9-O17 scribe).

## 7. Verdict summary

| Check | Result |
|---|---|
| capability: `--selftest` in mirror, ×2 | green, deterministic (stdout sha identical) |
| §6 step 1: `inputs` digests | match |
| §6 step 2: `gate_sha256` | match |
| §6 step 3: exit + finding-ID set in mirror | match (`exit 0`, `[]`, class `clean`) |
| control A: tamper → digest refusal | refuses; gate itself blind (exit 0) |
| control B: gate revision → refusal | refuses |
| author's tamper/mutant digests | reproduced exactly |
| non-vacuity (mutant flips verdict) | confirmed (exit 1, `MC-M02`) |
| frozen `run.log` vs independent stdout | byte-identical |
| repository write footprint of this seat | none (all scratch out of repo; graded files re-checked after every run) |

Rerun verdict: **the `myth-consistency-gate` r9-pre baseline is valid and independently
reproduced — digests match, gate revision matches, verdict matches, refusals fire, and the
pin is non-vacuous.**
