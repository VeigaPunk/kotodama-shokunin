# Rerun fragment — `costume-era-consistency-gate`, baseline `r9-pre`

- role: round-9 baseline **rerunner** (independent verifier shard; claim O — operability)
- date: 2026-10-17, 17:48–17:50 -03:00 (`date -Iseconds`)
- lane revision at every measurement: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (`git rev-parse HEAD`; unchanged before and after the run; `git status --porcelain tools/gates/`
  showed only the authors' untracked `tools/gates/expected/` and `tools/gates/frozen/handoff-packet-check/`)
- subject baseline (authored by a different worker, read-only here):
  `tools/gates/expected/costume-era-consistency-gate/r9-pre/`
  (`expected.json` sha256 `7ec01a1dce6182db329233594563dc31d52ce9d4c4cb9c89bc64e693e992c689`)
- standard applied: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4 (required
  fields), §5 (freeze procedure), §6 (verify order, tamper semantics)
- I changed nothing in the repository: every copy, tamper and re-run below happened under
  `/var/tmp/r9-costume-era-rerun/`. No gate bytes, fixture bytes, or baseline bytes were edited
  in place.

## 0. Access receipts and scratch substitution

- **`/tmp` was unusable at 17:48.** Attempted:
  `mkdir -p /tmp/r9-costume-era-rerun` → `mkdir: cannot create directory
  '/tmp/r9-costume-era-rerun': No space left on device` (exit 1), twice. Cause measured:
  `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp` — **inode exhaustion**, not byte
  exhaustion (`df -h /tmp` showed 8.5G free). 64 round-9 workers share this mount.
- Substitution: all scratch work ran in `/var/tmp/r9-costume-era-rerun/` (root filesystem,
  `df -h /var/tmp` → 782G free). The assignment names “a `/tmp` copy”; the /tmp substitution is
  recorded here as the deviation, with the failing command and status above as the receipt.
- Dependency: the author's baseline was absent when this shard started (17:48);
  `find tools/gates/frozen reports/round-9 -type f` listed no costume baseline. The independent
  fixture measurements (§1–§2 part 1, §4) were made first; the baseline appeared at 17:49 and
  §2 part 2 / §3 / §5 were measured against it. No polling beyond the first check was needed.

## 1. Copies are byte-identical to the live tree

Commands (from the lane root):

```
mkdir -p /var/tmp/r9-costume-era-rerun/pristine/tools/gates/fixtures
cp tools/gates/costume-era-consistency-gate.py            /var/tmp/r9-costume-era-rerun/pristine/tools/gates/
cp tools/gates/fixtures/costume-era-consistency-gate.yml  /var/tmp/r9-costume-era-rerun/pristine/tools/gates/fixtures/
cp tools/gates/fixtures/costume-era-consistency-gate.expected /var/tmp/r9-costume-era-rerun/pristine/tools/gates/fixtures/
sha256sum <live paths>; (cd /var/tmp/r9-costume-era-rerun/pristine && sha256sum <copied paths>)
```

| file | live sha256 | copy sha256 |
|---|---|---|
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` | identical |
| `tools/gates/fixtures/costume-era-consistency-gate.yml` | `36d92113d0cb8e04687c36694b507e93f25ca08c04003d75b7b537de65c1ea0e` | identical |
| `tools/gates/fixtures/costume-era-consistency-gate.expected` | `4b0724f9038d8a6a7a6189e91bdfdbf6e04beb101bac2b2ef37a708e704d0279` | identical |

Worktree-vs-commit check at the same moment: `git hash-object` on the three paths returned
`0bb40ed33c063e65f9a39a589237d674fcc6e599`, `8001e666d89927358236ca95245a9a3b160ca99b`,
`f7bf7eec78c1ea0f11efe0ec3b44efc92618b5ac` — equal to `git ls-tree HEAD` for those paths, so the
graded bytes are the committed bytes at `a7bb205d…`.

## 2. Independent execution in the copied tree (live tree never used)

**(1) Fixture copy, isolated selftest** — `cd /var/tmp/r9-costume-era-rerun/pristine &&
python3 tools/gates/costume-era-consistency-gate.py --selftest`

- exit `0`; stdout: `self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs`.
- The selftest read the **copied** fixture and printed no `SELFTEST FAIL … diverges` line, so the
  copy matched the gate's embedded fixture constant (a divergent copy does print that line —
  measured in §4 tamper B). The live tree was not executed against in this step; the selftest's
  own fixture paths in the output are the copy's
  (`…/r9-costume-era-rerun/pristine/tools/gates/fixtures/…`).

**(2) Fixture copy, graded run** — `python3 tools/gates/costume-era-consistency-gate.py
tools/gates/fixtures/costume-era-consistency-gate.yml`

- exit `1`; stdout 25 `FINDING` lines (`grep -c '^FINDING'` = 25), **21 unique IDs**
  (`grep -o '^FINDING [A-Z0-9-]*' | sed 's/FINDING //' | sort -u | wc -l` = 21):
  `E-01 EAR-01 EAR-04 G-ERA MAT-01 MAT-02 MAT-03 MAT-04 MAT-05 MAT-06 MAT-07 R-01 R-02 R-03 R-04
  R-05 R-06 R-07 T-01 T-02 T-03`; stderr 0 bytes (`wc -c` = 0).
- stdout sha256 = `482c1597a22096b2a0a09f09ce476f6ae5bbd6db70baf50df128fb0c1ed608b3`.
- **The author's `run.log` is byte-identical to this independent run** (`diff -q` → identical;
  same sha256), and all three ID sets agree: observed = committed
  `fixtures/costume-era-consistency-gate.expected` = `expected.findings` in the baseline
  (`diff` of the three sorted lists → empty; 21 lines each).

## 3. The authored `expected.json` verifies

Field-by-field against `gate-frozen-run-standard.md` §4, measured 17:50 (no field taken on trust):

| field | pinned | independently recomputed |
|---|---|---|
| `schema` | `kotodama-frozen-run-v1` | matches the standard's §4 name |
| `gate` | `costume-era-consistency-gate` | equals the directory/baseline gate name |
| `gate_sha256` | `e6bffd70…478f` | `sha256sum` of the live gate = same |
| `revision` | `a7bb205d…4ddd` | `git rev-parse HEAD` at 17:50 = same (no drift during the run) |
| `inputs` | `packet.yml → 36d92113…1ea0e` | `sha256sum` of the baseline copy = same; copy `diff -q` vs the live fixture = identical |
| `expected.exit`/`class` | `1` / `findings` | my isolated run exited 1 with findings |
| `expected.findings` | 21 IDs | equals my observed set (diff empty) |
| `stdout_sha256` | `482c1597…08b3` | author `run.log` **and** my independent run both hash to this |

- **Inputs-coverage claim checked, not accepted.** `freeze.txt` claims “inputs the gate reads:
  `packet.yml` only”. Sweep: `grep -n "open(\|FIXTURE_PATH\|EXPECTED_PATH"
  tools/gates/costume-era-consistency-gate.py` returns exactly one read on the graded path
  (`open(path …)` at `tools/gates/costume-era-consistency-gate.py:1176`, inside `run_file`, which
  `main` calls with `argv[1]`); the remaining `open`/`FIXTURE_PATH`/`EXPECTED_PATH` sites
  (lines 1490, 1495, 1513, 1515, 1530, 1533) are inside `selftest()`. So the one-entry `inputs`
  map is complete for a graded run — the pin set covers every input the gate reads.
- Interim external digest check in the standard's own form (§6 step 1), generated from the
  `inputs` map: `sha256sum -c` in the baseline directory → `packet.yml: OK`, exit `0`.
- Gate-revision check: recomputed `gate_sha256` above; equal, so class `gate_revised` is not
  triggered by the delivered baseline.

## 4. Tamper controls — never a silent pass

All tampering happened on **copies** under `/var/tmp`; each case was judged by an explicit
§6-style verifier (`/var/tmp/r9-costume-era-rerun/verify-baseline.py`, scratch tool, **not
committed** — lane tooling for this is claim O15's job) that maps classes per the standard:

| case | edit on the copy | verifier reading | exit |
|---|---|---|---|
| A — baseline copy, packet bytes | `printf '\n# tampered byte\n' >> packet.yml` | `class: snapshot_tampered`; `packet.yml: pinned=36d92113… got=887e1d544a0f25fe844277cfe04f2c2c87824ea775c8588b46ab62b73b1d7a41` | `2` |
| A′ — same edit applied to the **fixture** copy instead | comment line appended | `sha256sum -c` → `FAILED` (check exit 1 → `snapshot_tampered`, could-not-evaluate) | maps to `2` |
| B — semantic edit (fixture copy) | `max_width_m: 0.6` → `max_width_m: 1.5` (one line, verified 1 occurrence before the edit) | digest check `FAILED`; note the gate output *changes* here: 24 lines, `T-01` no longer raised | `2` |
| C — the committed fixture `.expected` list (fresh copy) | deleted the `T-01` line | digest check `FAILED` on `.expected` (gate itself never reads it) | `2` |
| D — gate revision | gate copy + one appended comment, `sha256 1b363a6f453715cde4ddb0b1f9966a8724f806ea5798df9534d8868cae0bcf23` | `class: gate_revised` (pinned `e6bffd70…` ≠ observed) | `2` |
| E — legacy shape | `inputs` set to `{}` in a copy of the baseline | `class: unpinned (legacy)` | `2` |
| F — no baseline | `expected.json` removed | `class: no baseline` | `2` |

- **The load-bearing demonstration, measured twice.** After tamper A the gate re-run over the
  tampered input still exits `1` with stdout **byte-identical** to `run.log`
  (`cmp` clean) — a comparison that looks only at stdout would read a match. Only the digest
  step turns the edit into `snapshot_tampered`. Same for A′ (append to the fixture copy) and C
  (an edited expected-ID list). This is the round-12 incident's shape (`gate-frozen-run-standard.md`
  §6: “the gate **still prints the same six findings** … Only the digest check turns it into
  `snapshot_tampered`”), reproduced here on this baseline.
- Positive control: the untouched baseline copy reads `class: findings | exit 0 | compared
  verdict match: exit=1 findings=21`.
- My tampered digest `887e1d54…` reproduces the value the author's `freeze.txt` records for the
  same tamper (independent agreement on the tamper artifact, not a copy of their number).
- Tamper B's second layer: with the semantic edit present, `--selftest` in that copy exits `1`
  with `SELFTEST FAIL: …/costume-era-consistency-gate.yml diverges from the embedded constant;
  refusing to overwrite` — the fixture pin and the digest pin fail independently.

## 5. What this fragment does and does not establish

- **Establishes (measured, not asserted):** at revision `a7bb205d…`, the committed gate bytes
  grade the committed fixture to exit 1 / 21 finding IDs; the baseline's pins recompute to the
  same values; the verdict reproduces byte-for-byte from an isolated copy; and every
  tamper/edit tested reads `could-not-evaluate` (`snapshot_tampered` / `gate_revised` /
  `unpinned (legacy)` / `no baseline`), never a silent pass.
- **Does not establish:** that the fixture is good design, that any corpus claim behind a
  finding is true, or that lore accepted anything. This is integrity evidence per
  `gate-frozen-run-standard.md` §10 (“digests are integrity, not truth”).
- **Residual limits (honest bounds).**
  - The baseline is **untracked** at this revision (`git status --porcelain` → `?? tools/gates/expected/`);
    until an integration commit carries it, it is worktree-only per §5 step 7, and the pinned
    `revision` names the commit the *gate and fixture* came from, not a commit containing the
    baseline.
  - `git check-ignore -v tools/gates/expected/costume-era-consistency-gate/r9-pre/run.log` →
    `.gitignore:3:*.log` — the author's `freeze.txt` integration note is correct: `run.log`
    needs `git add -f` (or a `.gitignore` exception) or the baseline commits without its verbatim
    stdout. Flagged for the orchestrator; not edited here.
  - The fixture `.expected` ID list is outside this baseline's `inputs` map (it lives in
    `tools/gates/fixtures/`), which is correct per §4 (only files *the gate reads* are pinned,
    and the gate never reads it) — but it means a later edit to that list is caught by the
    selftest layer (§4 tamper B), not by this baseline.
  - Tamper cases A–F are scratch-tree reproductions; the verifier tool used for them is
    uncommitted scratch (`to-verify`: no committed baseline-verifier existed at 17:50 —
    sweep: `grep -rln "expected.json" tools/ --include="*.py"` returned only
    `tools/check-evidence-coupling.py`, which is D3-specific and does not read this baseline).
  - Intermediate shell error, disclosed: my first tamper attempt at 17:48 used a
    `cp -a …/tools <newdir>/` collapse that placed the copy one level too high, so its
    `sha256sum`/gate calls failed with `No such file or directory` (no edit reached any file).
    The tree was rebuilt (`mkdir -p <dir>/tools/gates/fixtures` then per-file `cp`) and every
    number above comes from the corrected trees; the failed attempt produced no measurement.

## 6. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin          # revision a7bb205d…
B=tools/gates/expected/costume-era-consistency-gate/r9-pre
G=tools/gates/costume-era-consistency-gate.py
python3 "$G" --selftest                                      # exit 0, 10/10
python3 "$G" "$B/packet.yml" | sha256sum -                 # 482c1597…08b3 (exit 1)
python3 - <<'PY' | (cd "$B" && sha256sum -c /dev/stdin)     # packet.yml: OK
import json; m=json.load(open("tools/gates/expected/costume-era-consistency-gate/r9-pre/expected.json"))
[print(d, p) for p, d in sorted(m["inputs"].items())]
PY
# tamper: copy to scratch, append a comment, re-check -> snapshot_tampered (exit 2)
```
