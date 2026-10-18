# d4-typed-labels-check-gate — committed `expected.json` baseline (round 19, claim O)

- seat: **R29-O07 baseline author** (author half of the pair on this gate). This seat writes only
  `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/*` and this fragment. No gate behavior was
  changed; nothing was committed (the orchestrator integrates once per round).
- date: 2026-10-18 (local -03:00). Lane revision at freeze: HEAD
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` (`git rev-parse HEAD`), the value pinned as `revision` in
  `expected.json`. The round-19 declared `baseline_revision`
  `e5718945a1ab0a0c3db955338d2cae77d68fd348` grades the same bytes: `git diff --stat e571894..HEAD`
  lists only `reports/round-19/{claims,targets}.json`, and
  `git diff --stat e571894..HEAD -- tools examples corpus` is empty (0 lines).
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (layout), §4
  (required `expected.json` fields), §5 (freeze procedure), §6 (verify order and class map).
- claim under test: `reports/round-19/claims.json` claim **O** — "the D4 family carries committed
  `expected.json` baselines under the standard layout". This fragment supplies the
  `d4-typed-labels-check-gate` shard.

## 1. Deliverable

```text
tools/gates/expected/d4-typed-labels-check-gate/r19-pre/
  typed-labels.d4.yml                          # graded argv input (byte copy)
  examples/culture-d4/packet.d4.yml            # packet the peer reads (byte copy)
  examples/culture-d2/components/11-costumes.yml     # component the peer consults
  examples/culture-d2/components/12-rank-rules.yml   # component the peer consults
  tools/d2-typed-labels.py                     # the wrapped peer tool
  tools/gates/costume-era-consistency-gate.py  # the frozen reader the peer loads
  expected.json                                # digest pin + expected verdict
  run.log                                      # observed gate stdout at freeze time, verbatim
  freeze.txt                                   # frozen_by / frozen_at / command / revision / checks
```

## 2. Counts and digests (all commands run 2026-10-18 from the lane root)

| item | command | observed |
|---|---|---|
| gate digest | `sha256sum tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` |
| graded snapshot | `sha256sum …/r19-pre/typed-labels.d4.yml` | `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d` (equals the round-18 MANIFEST pin for `examples/culture-d4/typed-labels.d4.yml`) |
| copy is a byte copy | `cmp examples/culture-d4/typed-labels.d4.yml …/r19-pre/typed-labels.d4.yml` | identical (exit 0) |
| run | `python3 tools/gates/d4-typed-labels-check-gate.py …/r19-pre/typed-labels.d4.yml > …/run.log` | exit 0; one stdout line; stderr 0 bytes |
| stdout pin | `sha256sum …/r19-pre/run.log` | `3aa553930235d77bee021c044fdf4d626ab2389012c751cc8d5ad00d8cb7599a` |
| `expected.json` | `sha256sum …/r19-pre/expected.json` | `93b84da0cbd3b2a8531319555c9848c0fb85a79e675a4fc8768096e2b22f776a` (independently recomputed by `reports/round-19/run-validation.py --check` → `input_sha256`) |

## 3. Inputs the gate reads — measured, not assumed

A `sys.addaudithook("open")` trace over the graded command (scratch script under `.scratch/`, not
committed) recorded exactly these non-stdlib reads: the graded projection, the D4 packet,
`tools/d2-typed-labels.py`, `tools/gates/costume-era-consistency-gate.py`, and the two D2 component
files. The adapter itself is pinned by `gate_sha256`; the interpreter and stdlib are the trusted base.
So the six-entry `inputs` map is complete for a graded run by measurement.

Every pinned copy equals its pin **and** the live file it was copied from — 6/6
`copy == live == pin`, recomputed 2026-10-18.

## 4. Freeze procedure executed (standard §5, in order)

1. **Tree clean around the gate and the inputs** — `git status --porcelain` showed no modification to
   the adapter, the peer tool, the packet, the components or the reader; `git hash-object` on the
   adapter equals `git rev-parse HEAD:…`.
2. **Capability evidence recorded** — the adapter has no `--selftest` of its own, so the capability
   evidence is the wrapped peer's: `python3 tools/d2-typed-labels.py --selftest` → exit 0,
   `selftest: 39/39 checks passed …`. Recorded in `freeze.txt` rather than claimed as an adapter
   selftest.
3. **Byte-identical copies + digests** — the snapshot and the five read dependencies, `cmp`-clean
   against the live paths; never edited afterwards.
4. **Gate run over the snapshot copy** (never the live projection path) → `run.log`, exit 0.
5. **`expected.exit` / `class` / `findings` written from the observed run**, not from memory:
   exit 0, class `clean`, findings `[]`.
6. **`freeze.txt`** carries `frozen_by`, `frozen_at`, the command, the revision, the read-set
   evidence, and every check result.

## 5. Controls (full receipts in `rerun.md` and `tamper.md` beside this file)

| # | control | observed |
|---|---|---|
| 1 | determinism | three reruns → stdout sha256 `3aa55393…` each time, equal to `run.log` |
| 2 | digest check | every `inputs` digest recomputed from the committed copies equals its pin; every copy equals its live file |
| 3 | battery | the lane's own validator reads this baseline `pinned`, `inputs_checked 6`, `gate_sha256 match`, `stdout_pin match`, `findings []` |
| 4 | drift | one comment line appended to a snapshot copy → gate exit 1, `… differs from the deterministic projection` |
| 5 | tamper through the committed tooling | the same edit in a copied baseline root, read with `--baselines-root` → `snapshot_tampered` / `BASELINE-TAMPERED`, exit 2 |
| 6 | gate revision | gate copy + one appended comment → stdout byte-identical; only `gate_sha256` names the revision (`gate_revised`) |
| 7 | usage / could-not-evaluate | `--help` and a second path argument → exit 2 |

## 6. Limits and honesty notes

- **Live-tree reads.** The adapter hardcodes `ROOT/examples/culture-d4/packet.d4.yml`, so a graded run
  reads the live packet; the baseline pins those bytes by copy, and the re-run receipt plus the pin
  recomputation catch a later live edit. The battery's digest step compares the copy to the pin, never
  the copy to the live file — stated so the reading is not overclaimed.
- **Missing/malformed target exits 1, not 2.** The peer's `--check` answers byte-identity, so
  "no such file" is reported as "differs from the deterministic projection". Fail-closed, but the
  could-not-evaluate class is reachable only through a broken live packet or a usage error. Reported,
  not fixed: this seat changed no gate behavior.
- **Digests are integrity, not truth.** Exit 0 is byte-identity of a NON-CANON projection — not a design
  PASS, not a canon ruling.
- `run.log` is ignored by `.gitignore:3:*.log`; the orchestrator needs `git add -f` (see `freeze.txt`).

## 7. Registry row (draft for the round-19 registry scribe — do not treat as landed)

| field | value |
|---|---|
| name | `d4-typed-labels-check-gate` |
| class | gate (exit 1 on drift; a probe would not) |
| entry command | `python3 tools/gates/d4-typed-labels-check-gate.py <projection.yml>` |
| capability evidence | wrapped peer `tools/d2-typed-labels.py --selftest` → 39/39, exit 0 |
| frozen baseline | `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` (sha256 `93b84da0…`, `gate_sha256 05f99629…`, revision `169c6166…`) |
| verdict map | exit 0 `clean` / exit 1 drift / exit 2 could-not-evaluate |
| pin coverage | `gate_sha256` + 6 input digests + advisory `stdout_sha256 3aa55393…` |
| drift readings | digest differs → `snapshot_tampered`; gate digest differs → `gate_revised` (both exit 2) |
