# Tamper-control fragment — `d4-typed-labels-check-gate`, baseline `r19-pre`

- role: round-19 baseline **tamper-control** seat (claim O, R29-O09)
- date: 2026-10-18 (local -03:00); lane revision `169c616613899f7ba86b8fb58ed808bdfd4b5ccd`
- subject: `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/`
  (`expected.json` sha256 `93b84da0cbd3b2a8531319555c9848c0fb85a79e675a4fc8768096e2b22f776a`)
- standard applied: `corpus/knowledge/verification/gate-frozen-run-standard.md` §6 (verify order, tamper
  semantics, class map). Every edit was made on a **copy** under `$PWD/.scratch/r19o-baselines/`; the
  committed baseline and the live gate were never edited.

## 1. Class map, each row measured

| # | control | action | reading | exit |
|---|---|---|---|---|
| 1 | positive | untouched baseline, default roots, `python3 tools/check-gate-battery.py` | `pinned` (`inputs_checked 6`, `gate_sha256 match`, `stdout_pin match`, `findings []`) | 0 |
| 2 | digest tamper | `printf '\n# tampered byte\n' >> typed-labels.d4.yml` in a copied root; `check-gate-battery.py --baselines-root <copy>` | `snapshot_tampered`; `BASELINE-TAMPERED`: digest `9426d00edff3fa294f4572ace5d8fd9c785a99a4767d52447bce3e21331313da` ≠ pin `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d` | 2 |
| 3 | verdict drift | the same edit applied to a scratch copy, gate re-run | `… differs from the deterministic projection` | 1 |
| 4 | gate revision | gate copy + one appended comment line, read through the committed validator with a mirror `gates_dir` (`inspect_baselines(..., gates_dir=…)`) | `gate_revised`; `BASELINE-GATE-REVISED`: `gate_sha256 05f99629… differs from the live … 84e86ff115efc681…` | 2 |
| 5 | legacy shape | `inputs` emptied in a copy | `unpinned (legacy)`; `BASELINE-UNPINNED` | 2 |
| 6 | usage | `--help`; a second path argument | usage line on stderr | 2 |
| 7 | target absent / malformed | nonexistent path; `printf 'not: [\n'` | `… differs from the deterministic projection` (drift, not could-not-evaluate — see §3) | 1 |

## 2. The measurement that makes the digest step load-bearing

After the byte tamper (row 2), re-running the gate over the tampered copy still exits **1** with a
stable one-line message; the edit is invisible to a stdout-only comparison. Only the digest step turns
it into `snapshot_tampered`, and it does so through the lane's own validator
(`tools/check-gate-battery.py --baselines-root`), not through an ad-hoc script. Row 4 shows the
complementary case: after a gate edit the stdout is **byte-identical** to `run.log`, so only
`gate_sha256` names the revision that was read.

## 3. Reported, not fixed: the adapter's class boundary

A missing or malformed target exits **1**, not 2. The peer's `--check` answers one question —
byte-identity — so "no file there" is reported as "differs from the deterministic projection". That is
fail-closed (it never passes), but it means this gate's could-not-evaluate class is reachable only via a
usage error or a broken live packet. Recorded as an honest boundary of the adapter; this seat changed no
gate behavior, and the round-19 registry row for the gate states the verdict map with that caveat.

## 4. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
R=.scratch/r19o-baselines/tamper-root
rm -rf "$R" && mkdir -p "$R" && cp -r tools/gates/expected "$R/expected"
printf '\n# tampered byte\n' >> "$R/expected/d4-typed-labels-check-gate/r19-pre/typed-labels.d4.yml"
python3 tools/check-gate-battery.py --baselines-root "$R/expected"   # exit 2, snapshot_tampered
```
