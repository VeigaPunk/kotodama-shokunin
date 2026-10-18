# Rerun fragment — `d4-assembly-check-gate`, baseline `r19-pre`

- role: round-19 baseline **rerunner** (independent verifier half of the pair; claim O, seat R29-O11)
- date: 2026-10-18 (local -03:00); lane revision at every measurement:
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` (`git rev-parse HEAD`)
- subject baseline (authored by the other seat, read-only here):
  `tools/gates/expected/d4-assembly-check-gate/r19-pre/`
  (`expected.json` sha256 `fb59f03d6e32d8d664ba513dda2d671606032ebc7e58d577fa06957d35c0fc30`)
- standard applied: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4, §5, §6
- I changed nothing in the repository. Every copy, mirror, tamper and re-run happened under
  `$PWD/.scratch/r19o-baselines/` (`TMPDIR=$PWD/.scratch`), which is gitignored.

## 0. The independent run is a mirror run

I built a mirror preserving the repository's relative layout (adapter, both assemblers, the packet, the
12 components, the reader, and the baseline pair) and ran from the **mirror root** with the author's
relative argv:

```sh
(cd .scratch/r19o-baselines/mirror && \
  python3 tools/gates/d4-assembly-check-gate.py \
    tools/gates/expected/d4-assembly-check-gate/r19-pre/packet.d4.yml)
```

| measurement | observed |
|---|---|
| mirror gate digest | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` = the pinned `gate_sha256` |
| mirror run exit | 0 |
| mirror stdout vs the author's `run.log` | `cmp` clean — byte-identical |
| mirror stdout sha256 | `5f14c09a0128dbed113877fe85b4ce72f0cccc4b5b46c126263c9137a00bdfb6` |

## 1. `expected.json` verified field by field (no field taken on trust)

| field | pinned | independently recomputed |
|---|---|---|
| `schema` | `kotodama-frozen-run-v1` | matches the standard's §4 name |
| `gate` / `gate_script` | `d4-assembly-check-gate` / `tools/gates/d4-assembly-check-gate.py` | equals the directory name and the live script |
| `gate_sha256` | `df1a364b…544a` | `sha256sum` of the live gate = same |
| `revision` | `169c6166…5ccd` | `git rev-parse HEAD` = same |
| `inputs` | 16 entries | all 16 copies recompute to their pins, and each copy equals its live file (16/16) |
| `expected` | exit 0 / class `clean` / findings `[]` | my mirror run exited 0 with the byte-identical line |
| `stdout_sha256` | `5f14c09a…dfb6` | author `run.log` **and** my mirror run both hash to this |

Inputs-coverage claim checked, not accepted: an independent `sys.addaudithook("open")` trace over the
graded command reproduced the same read set recorded in `freeze.txt` (packet + 12 components + both
assemblers + reader), so the `inputs` map covers every input a graded run reads.

## 2. Controls

| case | edit (on copies only) | reading | exit |
|---|---|---|---|
| positive | untouched mirror baseline, mirror run | exit 0, stdout == `run.log` | 0 |
| A — drift | one comment line appended to a copy of the packet | `… differs from the deterministic assembly` (tampered digest `8c3563af1718cb61…`) | 1 |
| B — **component drift** | `printf '\n# component drift\n' >> components/06-myth.yml` (new digest `40ae98094c51f10e8fbcccb10ee15d4b931724b2563829fa2fd6c609d261786c`), then the committed packet re-run | `… differs from the deterministic assembly`, while the packet's own digest is **unchanged** — the verdict is a function of the component tree, and only the component pins in `inputs` make that edit visible to the digest step | 1 |
| C — gate revision | gate copy + one appended comment line, read through the committed validator with a mirror `gates_dir` | `gate_revised` / `BASELINE-GATE-REVISED`: `gate_sha256 df1a364b… differs from the live … 566da05ce8177e11…` | 2 |
| D — tamper through the committed tooling | the packet edit inside a copied baseline root, read by `python3 tools/check-gate-battery.py --baselines-root <copy>` | `snapshot_tampered` / `BASELINE-TAMPERED`: `packet.d4.yml: digest 8c3563af… does not match the pin e7ecd204…` | 2 |
| E — legacy shape | `inputs` emptied in a copy | `unpinned (legacy)` / `BASELINE-UNPINNED` | 2 |
| F — could-not-evaluate | nonexistent input path | `assembly error: [Errno 2] No such file or directory: …` | 2 |
| G — usage | `--help` | usage line on stderr | 2 |

- **Why case B matters.** The adapter's verdict is not a function of the graded packet alone: it
  re-builds from the live component tree, so a component edit silently changes what "the deterministic
  assembly" means. A baseline that pinned only `packet.d4.yml` would keep reading `pinned` through such
  an edit. This is why the assembly baseline carries the 12 component pins, the two assembler pins and
  the reader pin.
- **The stdout trap.** After case A the gate still exits 1 with a stable message, and after case C the
  stdout is **byte-identical** to `run.log`; only the digest step and the gate pin turn those edits into
  could-not-evaluate readings (`gate-frozen-run-standard.md` §6, the round-12 incident's shape).

## 3. What this fragment establishes, and what it does not

- **Establishes (measured):** at revision `169c6166…`, the committed adapter bytes grade the committed
  packet to exit 0 with a stable stdout; the baseline's 16 pins recompute to the same values; the verdict
  reproduces byte-for-byte from an isolated mirror; a component edit and a packet edit both read
  could-not-evaluate through the lane's own validator, never a silent pass.
- **Does not establish:** that the assembled packet is good design, that any content in it is true, or
  that lore accepted anything. Integrity evidence only (§10).
- **Residual limits.** The graded run reads the live component tree and the live assembler; the baseline
  pins those bytes by copy, so a later live edit is caught by the pin recomputation and this re-run, not
  by the battery's digest step alone. The adapter's `--selftest` currently exits 2 (an open O leg owned by
  the battery seats, recorded in `author.md` §6).
