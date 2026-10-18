# Rerun fragment — `d4-typed-labels-check-gate`, baseline `r19-pre`

- role: round-19 baseline **rerunner** (independent verifier half of the pair; claim O, seat R29-O08)
- date: 2026-10-18 (local -03:00); lane revision at every measurement:
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` (`git rev-parse HEAD`)
- subject baseline (authored by the other seat, read-only here):
  `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/`
  (`expected.json` sha256 `93b84da0cbd3b2a8531319555c9848c0fb85a79e675a4fc8768096e2b22f776a`)
- standard applied: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4, §5, §6
- I changed nothing in the repository. Every copy, mirror, tamper and re-run below happened under
  `$PWD/.scratch/r19o-baselines/` (`TMPDIR=$PWD/.scratch`), which is gitignored; no gate, fixture or
  baseline byte was edited in place.

## 0. The independent run is a mirror run, not the author's command

I built a mirror tree that preserves the repository's relative layout
(`.scratch/r19o-baselines/mirror/{tools/gates,tools,examples/culture-d4,examples/culture-d2/components}`),
copied the gate, the peer, the packet, the components, the reader and the baseline pair into it, and ran
from the **mirror root** with the same relative argv the author used:

```sh
(cd .scratch/r19o-baselines/mirror && \
  python3 tools/gates/d4-typed-labels-check-gate.py \
    tools/gates/expected/d4-typed-labels-check-gate/r19-pre/typed-labels.d4.yml)
```

The adapter echoes the argv path verbatim, so a mirror run at the same relative path produces the same
stdout string — the comparison below is a byte comparison, not a lookalike.

| measurement | observed |
|---|---|
| mirror gate digest | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` = the pinned `gate_sha256` |
| mirror run exit | 0 |
| mirror stdout vs the author's `run.log` | `cmp` clean — byte-identical |
| mirror stdout sha256 | `3aa553930235d77bee021c044fdf4d626ab2389012c751cc8d5ad00d8cb7599a` |

## 1. `expected.json` verified field by field (no field taken on trust)

| field | pinned | independently recomputed |
|---|---|---|
| `schema` | `kotodama-frozen-run-v1` | matches the standard's §4 name |
| `gate` / `gate_script` | `d4-typed-labels-check-gate` / `tools/gates/d4-typed-labels-check-gate.py` | equals the directory name and the live script |
| `gate_sha256` | `05f99629…1841` | `sha256sum` of the live gate = same |
| `revision` | `169c6166…5ccd` | `git rev-parse HEAD` = same |
| `inputs` | 6 entries | all 6 copies recompute to their pins, and each copy equals its live file (6/6) |
| `expected` | exit 0 / class `clean` / findings `[]` | my mirror run exited 0 with the byte-identical line |
| `stdout_sha256` | `3aa55393…599a` | author `run.log` **and** my mirror run both hash to this |

Inputs-coverage claim checked, not accepted: an independent `sys.addaudithook("open")` trace over the
graded command reproduced the same six-file read set recorded in `freeze.txt`, so the one-entry-per-file
`inputs` map covers every input a graded run reads.

## 2. Controls

| case | edit (on copies only) | reading | exit |
|---|---|---|---|
| positive | untouched mirror baseline, mirror run | exit 0, stdout == `run.log` | 0 |
| A — drift | one comment line appended to a copy of the snapshot | `… differs from the deterministic projection` | 1 |
| B — gate revision | gate copy + one appended comment line (`71ce84a536d70036b581671047b26fb562aa8d8ca98df0bbfd981ce83880e975`) | stdout still **byte-identical** to `run.log`; only `gate_sha256` names the revision | 0 (run) / `gate_revised` (class) |
| C — tamper through the committed tooling | the same edit inside a copied baseline root, read by `python3 tools/check-gate-battery.py --baselines-root <copy>` | `snapshot_tampered` / `BASELINE-TAMPERED`: `typed-labels.d4.yml: digest 9426d00e… does not match the pin a59990bb…` | 2 |
| D — legacy shape | `inputs` emptied in a copy | `unpinned (legacy)` / `BASELINE-UNPINNED` | 2 |
| E — usage | `--help`, and a second path argument | usage line on stderr | 2 |
| F — missing target | nonexistent path | `… differs from the deterministic projection` (the peer's `--check` answers byte-identity; see the author fragment §6) | 1 |

- **The load-bearing demonstration.** After case A the gate still exits 1 with a stable message, and
  after case B the gate's stdout is **unchanged** — a comparison that looked only at stdout would read
  both as matches. Only the digest step (C) and the gate pin (B) turn those edits into
  could-not-evaluate readings. This is the round-12 incident's shape
  (`gate-frozen-run-standard.md` §6), reproduced on this baseline.

## 3. What this fragment establishes, and what it does not

- **Establishes (measured):** at revision `169c6166…`, the committed adapter bytes grade the committed
  projection to exit 0 with a stable stdout; the baseline's pins recompute to the same values; the
  verdict reproduces byte-for-byte from an isolated mirror; and every edit tested reads
  could-not-evaluate, never a silent pass.
- **Does not establish:** that the projection is good design, that any content behind it is true, or
  that lore accepted anything. Integrity evidence only (§10, "digests are integrity, not truth").
- **Residual limits.** The graded run reads the live packet and peer (the adapter hardcodes the packet
  path); the baseline pins those bytes by copy. The adapter's could-not-evaluate class is reachable only
  through a usage error or a broken live packet. Both are stated in `freeze.txt`, not smoothed over.
