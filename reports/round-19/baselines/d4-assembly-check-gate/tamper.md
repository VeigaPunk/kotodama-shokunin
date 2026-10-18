# Tamper-control fragment — `d4-assembly-check-gate`, baseline `r19-pre`

- role: round-19 baseline **tamper-control** seat (claim O, R29-O12)
- date: 2026-10-18 (local -03:00); lane revision `169c616613899f7ba86b8fb58ed808bdfd4b5ccd`
- subject: `tools/gates/expected/d4-assembly-check-gate/r19-pre/`
  (`expected.json` sha256 `fb59f03d6e32d8d664ba513dda2d671606032ebc7e58d577fa06957d35c0fc30`)
- standard applied: `corpus/knowledge/verification/gate-frozen-run-standard.md` §6. Every edit was made
  on a **copy** under `$PWD/.scratch/r19o-baselines/`; the committed baseline and the live gate were
  never edited.

## 1. Class map, each row measured

| # | control | action | reading | exit |
|---|---|---|---|---|
| 1 | positive | untouched baseline, default roots, `python3 tools/check-gate-battery.py` | `pinned` (`inputs_checked 16`, `gate_sha256 match`, `stdout_pin match`, `findings []`) | 0 |
| 2 | digest tamper | `printf '\n# tampered byte\n' >> packet.d4.yml` in a copied root; `check-gate-battery.py --baselines-root <copy>` | `snapshot_tampered`; `BASELINE-TAMPERED`: digest `8c3563af1718cb61b02c21d8bd1a5e59cff7e4961556a9a57de3b4996c4e1871` ≠ pin `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | 2 |
| 3 | verdict drift | the same edit applied to a scratch copy, gate re-run | `… differs from the deterministic assembly` | 1 |
| 4 | **component drift** | one component file edited (`06-myth.yml` → `40ae98094c51f10e8fbcccb10ee15d4b931724b2563829fa2fd6c609d261786c`), committed packet re-run | `… differs from the deterministic assembly` while the packet's digest is unchanged | 1 |
| 5 | gate revision | gate copy + one appended comment line, read through the committed validator with a mirror `gates_dir` | `gate_revised`; `BASELINE-GATE-REVISED`: `gate_sha256 df1a364b… differs from the live … 566da05ce8177e11…` | 2 |
| 6 | legacy shape | `inputs` emptied in a copy | `unpinned (legacy)`; `BASELINE-UNPINNED` | 2 |
| 7 | could-not-evaluate | nonexistent input path | `assembly error: [Errno 2] No such file or directory: …` | 2 |
| 8 | usage | `--help` | usage line on stderr | 2 |

## 2. Why this gate needs the component pins (the control that carries the design)

Row 4 is the load-bearing control for this baseline. The adapter does not compare the graded packet to a
stored expected file: it re-builds from the live component tree and compares. A baseline that pinned only
`packet.d4.yml` would keep reading `pinned` after a component edit while the gate's verdict had silently
changed. The 12 component pins, the two assembler pins and the reader pin in `inputs` are what make that
edit visible to the digest step — and the edit was measured, not imagined.

## 3. The stdout trap, measured

After the byte tamper (row 2) the gate still exits 1 with a stable message; after the gate edit (row 5)
the stdout is **byte-identical** to `run.log`. A comparison that looked only at stdout would read both as
matches. Only the digest step and the `gate_sha256` pin turn them into could-not-evaluate readings — the
round-12 incident's shape (`gate-frozen-run-standard.md` §6), reproduced here on this baseline through
the lane's own validator, not an ad-hoc script.

## 4. Open dependency (reported, not fixed)

`python3 tools/gates/d4-assembly-check-gate.py --selftest` exits 2
(`assembly error: [Errno 2] No such file or directory: '--selftest'`). The round-19 validator's per-D4-gate
selftest leg requires that command to exit 0 with a `N/N checks passed` line; as of this seat's
measurement the leg is open and belongs to the round-19 O-battery seats (the adapters are outside this
seat's write scope). Recorded here so the gap is not smoothed into green.

## 5. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
R=.scratch/r19o-baselines/tamper-root
rm -rf "$R" && mkdir -p "$R" && cp -r tools/gates/expected "$R/expected"
printf '\n# tampered byte\n' >> "$R/expected/d4-assembly-check-gate/r19-pre/packet.d4.yml"
python3 tools/check-gate-battery.py --baselines-root "$R/expected"   # exit 2, snapshot_tampered
# component drift: edit any examples/culture-d4/components/*.yml in a mirror, re-run the gate -> exit 1
```
