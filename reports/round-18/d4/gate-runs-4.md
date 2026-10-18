# R18-D06 — gate run 4: the isolated-copy run

- round 18, shard **D06** (gate runs ×4, fourth leg — the isolated copy);
  claim **D** (`depth`). Assignment and write scope as in `gate-runs-1.md`; this
  file only, plus gitignored scratch under `.scratch/r18d03-06/`.
- date: 2026-10-18, local -03:00. Gate revision mirrored:
  `tools/gates/typed-pipeline-gate.py` sha256
  `286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9`.
- canon: NON-CANON engineering evidence.

## 0. Verdict

**Every verdict reproduces byte-for-byte in an isolated copy of the working
tree: the D4 declared run's blocked stdout, the D2 default run's baseline
stdout, the stand-in adapter's channel-leg failure, and the missing-D4-packet
traceback.** The mirror is built from the live tree (not from `HEAD`), so the
uncommitted generalized gate is mirrored faithfully; it carries no `.git`, no
`.scratch`, and no large per-round blobs.

## 1. Mirror provenance and construction

```
bash .scratch/r18d03-06/isolate.sh <mirror> -- true        # 2026-10-18 08:00 -03:00
```

- copied: `tools/`, `examples/`, `corpus/`, `reports/round-17/tests/frozen/`,
  `reports/round-18/` → 14 MB; `__pycache__` pruned; no `.git`, no `.scratch`.
- mirror gate sha256 `286d6e82711427ea…` = the live gate at build time (checked
  inside the mirror before the runs).
- the stand-in adapter was copied into the mirror at
  `<mirror>/.scratch-adapters/` and invoked by a mirror-relative path with
  `R18_FIXTURE_ROOT=<mirror>` (the scratch fixture resolves its root from that
  variable; its own hash is pinned in `gate-runs-2.md` §1).

## 2. Isolated run matrix (all four verdicts compared against the in-place runs)

| run | command (inside the mirror) | exit | stdout sha256 | vs in-place |
|---|---:|---|---|---|
| D4 declared | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **2** | `0e82305b59b159de…` | **byte-identical** to the in-place run (`gate-runs-1.md` §1) |
| D2 default | `python3 tools/gates/typed-pipeline-gate.py` | **0** | `15cdfbda73cd56cb…` | **byte-identical** to the pre-generalization baseline and the in-place run (`gate-runs-3.md` §1) |
| D4 + on-channel stand-in | `… --adapter .scratch-adapters/assemble-d4-typed-onchannel.py examples/culture-d4/packet.d4.yml` | **1** | `e5c8f18334e24a97…` | **byte-identical** to the in-place run — note the adapter path differs (`.scratch-adapters/…` vs `.scratch/r18d03-06/adapters/…`) and the output does not embed it |
| D4 missing file | `… examples/culture-d4/absent.yml` | **1** | (traceback) | defect reproduced: `FileNotFoundError`, no stable diagnostic (`gate-runs-3.md` §3) |

Consequences: the blocked D4 verdict is a property of the artifact set, not of
this checkout; the D2 byte-identity holds under a different working directory
and a different relative layout; and the missing-packet crash travels with the
gate, so it is not a shell or path artifact of the lane root.

## 3. Harness validation inside the same mirror (pre-run calibration)

Before the D4 runs, the same mirror was used to validate this shard's own
harness: the D2 default run reproduced `15cdfbda…` byte-identically there too,
and the findings parser (`run-gate.py`) reproduced the 15 holds + 1 note set of
the D2 expected file with `set_equal: true`, `counts_equal: true`, no duplicate
keys. The parser is therefore calibrated against a known-green run before it is
used to judge the D4 runs, which never reach the finding-emission stage.

## 4. Equality against the expected set

No isolated run produced findings to compare: the two D4 runs stop at
`L1-build` (exit 2) and at the channel leg (exit 1). The exact expected set used
for the comparison in this shard is
`examples/culture-d4/expected-holds.json` (`09490a27…`, 15 holds + 1 note +
0 fails), corroborated by an independent derivation from the filed projection
(identical 16 rows, delta none) — see `gate-runs-1.md` §3.

## 5. Caveats

- A mirror of a moving source tree is a snapshot: the mirror was built after all
  four legs of this shard's evidence were pinned to gate `286d6e82…`. If the O
  shard lands another revision, all four run files need a re-run.
- The mirror is 14 MB and lives under the gitignored `.scratch/`; it is
  scratch evidence, not a filed artifact, and it is never referenced by a
  manifest.
- Exit codes are engineering verdicts about a NON-CANON packet and expected set;
  none of them is a clearance, a canon statement, or a rights statement.

## 6. Revision watch (appended while the wave was still moving)

This mirror was built from the working tree at gate `286d6e82…`. Later samples
(2026-10-18 07:48–07:52 -03:00, revisions `65b1d4f7…` → `7ec051df…`) show the D4
declared run still at exit 2 and the D2 default still byte-identical
(`15cdfbda…`), so the mirror's conclusions about *which* verdicts are stable
remain valid, but the mirror bytes are not the final tree. Rebuild the mirror
with `.scratch/r18d03-06/isolate.sh` and repeat the matrix on the final
revision once the D4 adapter lands.
