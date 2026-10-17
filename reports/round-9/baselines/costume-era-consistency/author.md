# costume-era-consistency-gate — committed `expected.json` baseline (round 9, claim O)

- role: **baseline author** — one of the two workers on this gate (author / independent re-runner).
  This seat writes only `tools/gates/expected/costume-era-consistency-gate/r9-pre/*` and this
  fragment. No gate behavior was changed; nothing was committed (the orchestrator integrates once
  per round).
- date: 2026-10-17 (local -03:00). Lane revision at freeze: HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (`git rev-parse HEAD`), which is the `revision` pinned in `expected.json`. The round-9 declared
  `baseline_revision` is `e1694bad6ac96aca45a11ca5746582b275929355`; the graded gate and fixture
  bytes are identical at both (`git diff --stat e1694ba..HEAD` lists only the round-9
  `claims.json`/`targets.json`, and `git diff --stat e1694ba..HEAD -- tools corpus examples` is
  empty), so the pin is truthful either way — see §4 item 2 and `freeze.txt`.
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (layout),
  §4 (required `expected.json` fields), §5 (freeze procedure), §6 (verify procedure, tamper
  semantics, class mapping). Self-test = capability, frozen run = measurement.
- claim under test: `reports/round-9/claims.json` claim **O** — “committed expected.json drift-pin
  baselines for all 7 structural gates (tools/gates/*.py) … NO gate behavior changes”. This
  fragment supplies the `costume-era-consistency-gate` shard.

## 1. Deliverable

```text
tools/gates/expected/costume-era-consistency-gate/r9-pre/
  packet.yml       # byte copy of tools/gates/fixtures/costume-era-consistency-gate.yml
  expected.json    # digest pin + expected verdict (schema kotodama-frozen-run-v1)
  run.log          # observed gate stdout at freeze time, verbatim (25 FINDING lines, exit 1)
  freeze.txt       # frozen_by / frozen_at / command / revision / check results
```

Counts and digests (all commands run 2026-10-17 from the lane root):

| Item | Command | Observed |
|---|---|---|
| gate digest | `sha256sum tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` |
| snapshot digest | `sha256sum …/r9-pre/packet.yml` | `36d92113d0cb8e04687c36694b507e93f25ca08c04003d75b7b537de65c1ea0e` |
| copy is a byte copy | `cmp tools/gates/fixtures/costume-era-consistency-gate.yml …/r9-pre/packet.yml` | identical (exit 0); fixture digest equals the snapshot digest |
| run | `python3 tools/gates/costume-era-consistency-gate.py …/r9-pre/packet.yml > …/run.log` | exit 1; 25 `FINDING` lines, 21 unique IDs; stderr 0 bytes |
| stdout pin | `sha256sum …/r9-pre/run.log` | `482c1597a22096b2a0a09f09ce476f6ae5bbd6db70baf50df128fb0c1ed608b3` |
| expected-set agreement | `comm`-style set diff of observed IDs vs `tools/gates/fixtures/costume-era-consistency-gate.expected` | empty (observed 21 = expected 21); the `.expected` fixture set and the frozen ID set are identical |

`expected.findings` (21, set-compared, stdout order deliberately not part of the contract):
`E-01, EAR-01, EAR-04, G-ERA, MAT-01…MAT-07, R-01…R-07, T-01, T-02, T-03`; per-ID counts are in
`expected.json` `finding_counts` (total 25 lines: `G-ERA`, `MAT-02`, `MAT-03`, `MAT-05` fire twice).

**Inputs the gate reads: `packet.yml` only.** Evidence: the gate opens exactly one file in a graded
run — `run_file` → `open(path, …)` at `tools/gates/costume-era-consistency-gate.py:1176`; the only
other `open()` sites are selftest-only (`_pin_fixture`, def at :1480, opens at :1489–1495;
`EXPECTED_PATH` read at :1533 inside `selftest`, def at :1511). CLI surface: `:1147–1149` (usage),
`:1631–1646` (`main`). So the `inputs` map is a one-entry map by measurement, not by assumption.
The module docstring (:40–41) says this kernel “is NOT a registered fleet gate”; the lane registry
does carry the row (`SKILL.md:186`, class `gate`), so the two statements are about different
registries — noting it here so the registry scribe does not read them as a contradiction.

## 2. Freeze procedure executed (standard §5, in order)

1. **Tree clean around the gate and the input.** `git status --porcelain tools/` → only the new
   untracked baseline directory; no modified gate or fixture. The gate and its fixture pair are
   tracked and unmodified (`git status --porcelain tools/gates/` empty apart from `??` baseline
   paths).
2. **`--selftest` recorded.** `python3 tools/gates/costume-era-consistency-gate.py --selftest` →
   exit 0, `self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs`; re-checked
   `git status --porcelain tools/gates/` afterwards, empty (the selftest repins its fixture
   byte-identically; fixture digests unchanged before/after).
3. **Byte-identical copy + digests** (§1 table); the copy was never edited afterwards.
4. **Gate run over the snapshot copy** (never the fixture path) → `run.log`, exit 1.
5. **`expected.exit` / `class` / `findings` written from the observed run**, not from memory; the
   ID set was machine-compared to the fixture `.expected` set (difference empty).
6. **`freeze.txt`** carries `frozen_by`, `frozen_at`, command, revision, and every check result.

## 3. Verify procedure and controls (standard §6) — all measured on this gate

| # | Check | Command / action | Observed |
|---|---|---|---|
| 1 | digest check first | `sha256sum -c` over the `inputs` map recomputed from `expected.json` (interim external check; the gate does **not** verify digests internally today) | `packet.yml: OK`, exit 0 |
| 2 | gate-revision check | copy of the gate with one appended comment line run over the snapshot | copy sha256 `94397904effbe518a7919966ce05227c19b298485bc2cca99b2d20cf8bba325f`; stdout **byte-identical** to `run.log` → only `gate_sha256` names the revision read ⇒ `gate_revised` (could-not-evaluate) |
| 3 | verdict compare | full re-verify script (digests, `expected.exit`, ID set, stdout pin) | exit 1 = expected; ID set match; `stdout_sha256` match; `VERIFY: OK` |
| 4 | tamper control | copy in `/dev/shm`, `printf '\n# tampered byte\n' >> packet.yml` | sha256 `887e1d544a0f25fe844277cfe04f2c2c87824ea775c8588b46ab62b73b1d7a41` ⇒ digest **FAILED** ⇒ `snapshot_tampered`; a re-run of the gate over the tampered copy still exits 1 with stdout **byte-identical** to `run.log` (`cmp` clean) — measured: stdout comparison alone would false-pass; only the digest step sees the edit |
| 5 | determinism | three reruns of the graded command | exit 1 each; stdout sha256 `482c1597…` all three times = the frozen `run.log` |
| 6 | could-not-evaluate control | `printf 'name: x\ncostumes: [\n'` to a scratch file | exit 2, `FINDING G-DATA: [could-not-evaluate] costumes must be a list` |
| 7 | regression: no gate behavior change | `python3 tools/check-gate-battery.py` (battery over all seven gates, disposable mirror) | exit 0 before the O15 extension landed: `battery_exit 0`, `pass 7 / fail 0 / unevaluable 0`; `originals modified 0 / preserved true` |
| 8 | regression: battery controls | `python3 tools/check-gate-battery.py --selftest` | `SELFTEST OK 10/10 controls behaved as expected` (exit 0) at 17:50; after the O15 seat extended the runner (`tools/check-gate-battery.py` mtime 17:52:19) the same command reads `SELFTEST OK 28/28 controls behaved as expected` |
| 9 | **tamper rejection through the committed tooling** (stronger than the ad-hoc row 4) | `cp -r <baseline> /dev/shm/k9-batroot/expected/costume-era-consistency-gate/`, append one comment line to the copy's `packet.yml`, then `python3 tools/check-gate-battery.py --baselines-root /dev/shm/k9-batroot` | exit 2; baseline reads `snapshot_tampered` with finding `BASELINE-TAMPERED`: `packet.yml: digest 887e1d544a0f25fe… does not match the pin 36d92113d0cb8e04…` — the same tamper value recorded in `freeze.txt`, now read by the lane's own validator |
| 10 | baseline validation of the shipped tree | `python3 tools/check-gate-battery.py` (default roots) | exit 2 *because three gates were still uncovered at that instant*, not because of this shard: `pinned` 4 baselines (costume, phonology, handoff, lexicon), `gates_uncovered` {myth, naming, provenance}, `unevaluable 0`, and this baseline's record carries `gate_sha256 match`, `stdout_pin match`, `inputs_checked 1`, `findings []` |

- Note on row 10: the extended battery's default roots are `tools/gates/expected/` **and**
  `tools/gates/frozen/` (its §root list shows both, 2 files each at 17:5x) — so the O15 seat's tool
  already discovers across two of the three roots observed in §4, and this baseline sits under the
  tool's default root.

Machine re-verify recipe (this gate's shard; exit 0 = everything matches):

```sh
cd <lane root>
python3 - <<'PY'
import hashlib, json, os, subprocess, sys
b = "tools/gates/expected/costume-era-consistency-gate/r9-pre"
e = json.load(open(b + "/expected.json")); sh = lambda p: hashlib.sha256(open(p,"rb").read()).hexdigest()
assert sh("tools/gates/costume-era-consistency-gate.py") == e["gate_sha256"]
assert all(sh(f"{b}/{r}") == d for r, d in e["inputs"].items())
r = subprocess.run([sys.executable, "tools/gates/costume-era-consistency-gate.py", b + "/packet.yml"], capture_output=True, text=True)
assert r.returncode == e["expected"]["exit"]
assert sorted({l.split()[1].rstrip(":") for l in r.stdout.splitlines() if l.startswith("FINDING ")}) == e["expected"]["findings"]
print("costume-era baseline: OK")
PY
```

### 3.1 Pair reconciliation with the re-runner seat (`rerun.md`)

The second seat of this pair (`reports/round-9/baselines/costume-era-consistency/rerun.md`, landed
17:50:51) independently re-ran the gate in a copied tree and verified this baseline field by field.
Reconciliation of the two artifacts, measured 17:5x:

- `rerun.md:10` pins the subject baseline as `expected.json` sha256
  `7ec01a1dce6182db329233594563dc31d52ce9d4c4cb9c89bc64e693e992c689`. The file in the tree hashes
  to exactly that value (`sha256sum …/expected.json`, re-checked after this seat's last write), so
  the pair's subject identity is coherent: nothing was changed in the pinned file after the
  independent verification.
- Independent agreement on the pins (their numbers, not copied from here): `gate_sha256`
  `e6bffd70…`, `packet.yml` `36d92113…`, `expected.exit 1` / 21 IDs, `stdout_sha256 482c1597…`
  (their isolated run hashed to the same). Their tamper digest `887e1d54…` reproduces the value in
  `freeze.txt` §tamper.
- Disclosure, because this seat briefly broke that coherence and fixed it: between 17:49 and 17:5x
  this seat added extra descriptive fields to `expected.json` (a `revision_note`, `input_class`,
  `finding_counts`, `tamper_evidence`, `layout_note`, …) and changed `revision` to the round-9
  declared `baseline_revision`; that version hashed to `644b5734485e2186896dc5a4a48d0b7a53babeea7dde645aa64d53c6410a2348`,
  i.e. it no longer matched `rerun.md`'s pin. The file was reverted to the verified revision, and
  every fact from the reverted version now lives here and in `freeze.txt` instead. Deliberate
  choice, stated plainly: the standard's §4 required field set is complete as it stands, and no
  fact is worth invalidating an independent verifier's pin for.
- Consequence to report, not to hide: this baseline therefore pins `revision a7bb205d…` while the
  `naming-collision-gate` baseline pins `e1694bad…` — the registry scribe recorded this as open
  item 2 (`reports/round-9/baselines/registry.md` §5). Both are truthful for the graded bytes; the
  orchestrator's single round-9 commit is the reconciliation point.

## 4. Cross-seat observations the orchestrator must settle (reported, not absorbed)

Measured 2026-10-17 between 17:48 and 17:52 — round-9 baseline seats did **not** converge on one
root, and one seat diverged on input class too:

1. `tools/gates/expected/<gate>/<baseline-id>/` — this shard (the path this assignment names).
2. `tools/gates/frozen/<gate>/r9-pre/` — observed for `handoff-packet-check` and
   `lexicon-coverage-audit` (the standard's own root, `gate-frozen-run-standard.md` §3).
3. `reports/round-9/baselines/<gate>/` — observed for `naming-collision-gate` (whose
   `expected.json` `layout_note` names that root as the round-9 baseline root, while
   `reports/round-9/targets.json` names `reports/round-9/baselines/<gate-name>/` for the
   *fragment*).
4. Input class: this shard freezes the gate's own fixture; the `naming-collision-gate` shard
   froze `examples/culture-d2/packet.d2.yml`. Both are defensible; the round should pick one so
   the seven baselines are comparable — a claim of "7/7 per the gate standard" reads differently
   when the graded objects differ in kind.
5. **Discovery, measured against the landed validator (updated 17:5x).** The extended battery
   (`tools/check-gate-battery.py`, O15 seat) resolves by default under `tools/gates/expected/`
   **and** `tools/gates/frozen/`; its own output names both roots. Discovery sweep run this seat:
   `find tools/gates/expected tools/gates/frozen reports/round-9/baselines -name expected.json` —
   the third root still holds the `naming-collision-gate` baseline that the validator does not
   reach, so if the round keeps that root the battery needs it declared (`--baselines-root`), or
   that baseline should move. This seat's own baseline is under the validator's default root and
   reads `pinned` (§3 row 10).
6. **Do not duplicate this baseline under a second root.** The standard's naming rule is that a
   bare baseline id must resolve under exactly one gate directory — two `r9-pre` candidates for
   `costume-era-consistency-gate` fail closed and the run is not compared. Consolidation should be
   a move, not a copy.
7. `.gitignore` line 3 is `*.log`, so **`run.log` is ignored by pattern**:
   `git check-ignore -v …/r9-pre/run.log` → `.gitignore:3:*.log`; `git status --porcelain --ignored`
   shows `!! …/run.log`. The baseline commits without its verbatim stdout unless the orchestrator
   adds `git add -f tools/gates/expected/costume-era-consistency-gate/r9-pre/run.log`. If the round
   prefers a pattern-safe name, the sibling lanes' `.out` convention (e.g.
   `tools/gates/frozen/round-3/*.out`) is available — this seat did not rename it because the
   standard's layout names `run.log`.
8. Environment hazard observed during this seat: `/tmp` was **inode-exhausted** —
   `df -i /tmp` → `1048576 1048576 0 100% /tmp` while `df -h /tmp` showed 8.5G free, and
   `mkdir -p /tmp/k9-era` → `No space left on device` (2026-10-17T17:48-03:00). Scratch was moved
   to `/dev/shm/k9-era/`; it held only tamper/control copies and was never inside the repo.

## 5. Registry row (draft for the R9-O17 registry scribe — do not treat as landed)

| Field | Value |
|---|---|
| name | `costume-era-consistency-gate` |
| class | gate (exits 1 on findings; a probe would not) |
| entry command | `python3 tools/gates/costume-era-consistency-gate.py <culture-packet.yml>` |
| self-test | `python3 tools/gates/costume-era-consistency-gate.py --selftest` → exit 0, 10/10 checks |
| frozen baseline | `tools/gates/expected/costume-era-consistency-gate/r9-pre/expected.json` (sha256 `7ec01a1d…`, gate_sha256 `e6bffd70…`, revision `a7bb205d…`) |
| verdict map | exit 0 `clean` / exit 1 `findings` (any severity) / exit 2 `could-not-evaluate` (`G-DATA`); frozen run: exit 1, 21 IDs |
| pin coverage | `inputs.packet.yml` sha256 `36d92113…` + `gate_sha256` + advisory `stdout_sha256` |
| drift readings | digest differs → `snapshot_tampered`; gate digest differs → `gate_revised` (both could-not-evaluate, exit 2) |

## 6. Limits, honesty notes, and to-verify

- **Interim check, not gate-internal.** This baseline's own digest verification was an external
  `sha256sum -c` recomputed from `expected.json`; the gate does not read `expected.json` today
  (standard §8 records that gap). The enforcement half landed during this seat: the extended
  battery's baseline check now reads a tampered snapshot as `snapshot_tampered` /
  `BASELINE-TAMPERED` and exits 2 (§3 rows 9–10, measured — not an expectation). What this shard
  supplies is the pinned values that validator reads.
- **Digests are integrity, not truth.** The frozen run says these bytes, under this gate revision,
  produced this verdict. It is not a design PASS for the fixture packet (which is a synthetic
  audit packet declared NOT canon at `tools/gates/costume-era-consistency-gate.py:1185`) and
  never a canon ruling.
- **Advisory stdout pin.** `stdout_sha256` is a whole-output convenience; the verdict contract is
  the finding-ID set, and today the set is stable across reruns (three reruns measured) — a future
  gate revision that reorders or rewraps lines may keep the set while changing the pin.
- Measured during this seat, no longer `to-verify`: the extended battery discovers and validates
  this baseline (`pinned`, §3 row 10) and turns a tampered snapshot into
  `snapshot_tampered` / `BASELINE-TAMPERED` (§3 row 9).
- Still `to-verify` (for the re-runner seat / auditors, not claimed here): that the orchestrator
  force-adds `run.log` (item 7 above — the file is ignored by pattern); whether the round wants a
  second, D2-packet baseline for this gate (item 4) and which single root the seven baselines
  should live under (items 1–5) — both are round decisions, not this seat's.
- **No gate behavior changed:** no edit to `tools/gates/costume-era-consistency-gate.py` or its
  fixture pair (`git status --porcelain tools/gates/*.py tools/gates/fixtures/` → 0 lines); the
  battery selftests re-run green over all seven gates (§3 rows 7–8).
