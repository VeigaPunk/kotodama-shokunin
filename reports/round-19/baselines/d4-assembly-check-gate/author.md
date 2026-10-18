# d4-assembly-check-gate — committed `expected.json` baseline (round 19, claim O)

- seat: **R29-O10 baseline author** (author half of the pair on this gate). This seat writes only
  `tools/gates/expected/d4-assembly-check-gate/r19-pre/*` and this fragment. No gate behavior was
  changed; nothing was committed (the orchestrator integrates once per round).
- date: 2026-10-18 (local -03:00). Lane revision at freeze: HEAD
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` (`git rev-parse HEAD`), the value pinned as `revision` in
  `expected.json`. The round-19 declared `baseline_revision`
  `e5718945a1ab0a0c3db955338d2cae77d68fd348` grades the same bytes: `git diff --stat e571894..HEAD`
  lists only `reports/round-19/{claims,targets}.json`, and
  `git diff --stat e571894..HEAD -- tools examples corpus` is empty (0 lines).
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §3, §4, §5, §6.
- claim under test: `reports/round-19/claims.json` claim **O** — "the D4 family carries committed
  `expected.json` baselines under the standard layout". This fragment supplies the
  `d4-assembly-check-gate` shard.

## 1. Deliverable

```text
tools/gates/expected/d4-assembly-check-gate/r19-pre/
  packet.d4.yml                                 # graded argv input (byte copy)
  examples/culture-d4/components/01-brief.yml … 12-provenance.yml   # the 12 component files
  tools/assemble-culture-d4.py                  # the wrapped assembler
  tools/assemble-d2.py                          # the base assembler it reuses
  tools/gates/costume-era-consistency-gate.py   # the frozen reader both assemblers load
  expected.json                                 # digest pin + expected verdict
  run.log                                       # observed gate stdout at freeze time, verbatim
  freeze.txt                                    # frozen_by / frozen_at / command / revision / checks
```

## 2. Counts and digests (all commands run 2026-10-18 from the lane root)

| item | command | observed |
|---|---|---|
| gate digest | `sha256sum tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` |
| graded snapshot | `sha256sum …/r19-pre/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` (equals the round-18 MANIFEST pin for `examples/culture-d4/packet.d4.yml`) |
| copy is a byte copy | `cmp examples/culture-d4/packet.d4.yml …/r19-pre/packet.d4.yml` | identical (exit 0) |
| run | `python3 tools/gates/d4-assembly-check-gate.py …/r19-pre/packet.d4.yml > …/run.log` | exit 0; one stdout line; stderr 0 bytes |
| stdout pin | `sha256sum …/r19-pre/run.log` | `5f14c09a0128dbed113877fe85b4ce72f0cccc4b5b46c126263c9137a00bdfb6` |
| `expected.json` | `sha256sum …/r19-pre/expected.json` | `fb59f03d6e32d8d664ba513dda2d671606032ebc7e58d577fa06957d35c0fc30` (independently recomputed by `reports/round-19/run-validation.py --check` → `input_sha256`) |

## 3. Inputs the gate reads — measured, not assumed

The adapter loads the assembler with `runpy` and calls its build, so the verdict is a function of the
whole component tree. A `sys.addaudithook("open")` trace over the graded command (scratch script under
`.scratch/`, not committed) recorded exactly: the graded packet, the 12 component files,
`tools/assemble-culture-d4.py`, `tools/assemble-d2.py`, and
`tools/gates/costume-era-consistency-gate.py`. The adapter itself is pinned by `gate_sha256`. Hence the
16-entry `inputs` map is complete for a graded run by measurement.

Every pinned copy equals its pin **and** the live file it was copied from — 16/16
`copy == live == pin`, recomputed 2026-10-18.

## 4. Freeze procedure executed (standard §5, in order)

1. **Tree clean around the gate and the inputs** — `git status --porcelain` showed no modification to
   the adapter, the assemblers, the packet, the components or the reader; `git hash-object` on the
   adapter equals `git rev-parse HEAD:…`.
2. **Capability evidence recorded** — the adapter has no `--selftest` of its own, so the capability
   evidence is the wrapped assembler's: `python3 tools/assemble-culture-d4.py --selftest` → exit 0,
   `selftest: 81/81 checks passed …`. Recorded in `freeze.txt` rather than claimed as an adapter
   selftest.
3. **Byte-identical copies + digests** — the snapshot and the fifteen read dependencies, `cmp`-clean
   against the live paths; never edited afterwards.
4. **Gate run over the snapshot copy** (never the live packet path) → `run.log`, exit 0.
5. **`expected.exit` / `class` / `findings` written from the observed run**, not from memory:
   exit 0, class `clean`, findings `[]`.
6. **`freeze.txt`** carries `frozen_by`, `frozen_at`, the command, the revision, the read-set
   evidence, and every check result.

## 5. Controls (full receipts in `rerun.md` and `tamper.md` beside this file)

| # | control | observed |
|---|---|---|
| 1 | determinism | three reruns → stdout sha256 `5f14c09a…` each time, equal to `run.log` |
| 2 | digest check | every `inputs` digest recomputed from the committed copies equals its pin; every copy equals its live file |
| 3 | battery | the lane's own validator reads this baseline `pinned`, `inputs_checked 16`, `gate_sha256 match`, `stdout_pin match`, `findings []` |
| 4 | drift | one comment line appended to a snapshot copy → gate exit 1, `… differs from the deterministic assembly` |
| 5 | **component drift** (the load-bearing control for this gate) | one component file edited (`06-myth.yml`, digest `40ae98094c51f10e…`) → the committed packet no longer matches the live build → exit 1, while the packet's own digest is unchanged |
| 6 | tamper through the committed tooling | the snapshot edit in a copied baseline root, read with `--baselines-root` → `snapshot_tampered` / `BASELINE-TAMPERED`, exit 2 |
| 7 | gate revision | gate copy + one appended comment → stdout byte-identical; only `gate_sha256` names the revision (`gate_revised`) |
| 8 | could-not-evaluate | a missing input path → `assembly error: …`, exit 2 |

## 6. Limits and honesty notes

- **Live-tree reads.** The adapter resolves `ROOT/examples/culture-d4/components` and the live assembler,
  so a graded run builds from the live tree; the baseline pins those bytes by copy, and the re-run
  receipt plus the pin recomputation catch a later live edit. The battery's digest step compares the
  copy to the pin, never the copy to the live file — stated so the reading is not overclaimed.
- **`--selftest` on the adapter exits 2** (measured: `assembly error: [Errno 2] No such file or
  directory: '--selftest'`). The round-19 validator's per-D4-gate selftest leg requires that command to
  exit 0 with a `N/N checks passed` line; as of this seat's measurement that leg is **open**, and it
  belongs to the round-19 O-battery seats (the adapters are outside this seat's write scope). Reported
  as a dependency, not fixed here.
- **Digests are integrity, not truth.** Exit 0 is byte-identity of a NON-CANON packet — not a design
  PASS, not a canon ruling.
- `run.log` is ignored by `.gitignore:3:*.log`; the orchestrator needs `git add -f` (see `freeze.txt`).

## 7. Registry row (draft for the round-19 registry scribe — do not treat as landed)

| field | value |
|---|---|
| name | `d4-assembly-check-gate` |
| class | gate (exit 1 on drift; a probe would not) |
| entry command | `python3 tools/gates/d4-assembly-check-gate.py <packet.yml>` |
| capability evidence | wrapped assembler `tools/assemble-culture-d4.py --selftest` → 81/81, exit 0 |
| frozen baseline | `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json` (sha256 `fb59f03d…`, `gate_sha256 df1a364b…`, revision `169c6166…`) |
| verdict map | exit 0 `clean` / exit 1 drift / exit 2 could-not-evaluate (usage error, missing input, assembler error) |
| pin coverage | `gate_sha256` + 16 input digests + advisory `stdout_sha256 5f14c09a…` |
| drift readings | digest differs → `snapshot_tampered`; gate digest differs → `gate_revised` (both exit 2) |
