# R11-D11 — test determinism: two consecutive e2e assemblies byte-identical

- seat: **R11-D11** (test shard, determinism), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D11 (test determinism): two consecutive e2e assemblies byte-identical; reports/round-11/depth/test-determinism.md."
- writes: this file only (plus in-lane scratch under `.scratch/d11/`). No tool, gate, packet, baseline, manifest or earlier-round byte is edited by this seat; no commit, no push.
- clock: all stamps UTC (`date -u`); local is UTC-03:00.
- revision under test: `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (`e3ef171`, the claims commit) with the **pre-wiring** tools, sha256 captured at test time (`.scratch/d11/logs/tools-sha-at-test.txt`):
  - `tools/assemble-d2.py` `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d`
  - `tools/d2-typed-labels.py` `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`
  - `tools/gates/costume-era-consistency-gate.py` (reader) `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f`
  - environment: Python 3.14.7, Linux 7.2.3-arch1-3, 2026-10-17T22:02–22:20Z (the pre-wiring and wired test windows).
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability, or a canon fact.

## 0. Verdict

**PASS — byte-identical, and not by luck of one environment.** Two consecutive
assemblies of the D2 e2e chain reproduce the same bytes (`cmp` clean), and the
same bytes reappear across a second isolated copy at a different absolute path,
a different working directory, `PYTHONHASHSEED` 0/1/random, `LC_ALL=C`, a
stripped `env -i` environment, and an mtime touch of a source component. All
five gates print byte-identical stdout
with identical exit codes across every run. The one red leg in the chain —
`python3 tools/d2-typed-labels.py --check` exiting 1 — was the **already-filed
stale pin** in the artifact as then on disk (§5), not nondeterminism: the fresh
projection was itself bit-stable across all probes, and the re-pin closed
red-side-to-the-predicted-bytes mid-round (§5, closed).

Scope note: the D-wiring landed while this shard was in flight, in two phases
and both tested. First the **pre-wiring** chain (§§1–6) —
`assemble-d2.py` → `d2-typed-labels.py --emit` → the five gates. Then the
**wired** e2e entry point `tools/typed-gate-flow.py` (R11-D05, sha256
`5758e315…`) landed and was run the same way (§7, closed): two consecutive
runs, a second copy, and five environment perturbations all print
byte-identical stdout (sha256 `204857cbb84d49cf39b51272…`, 49 lines) with
exit 0 every time. Determinism holds on the wired chain too.

## 1. What "the e2e assembly" is at the tested revision

The claim-D chain as runnable at `e3ef171` has five stages; a full "assembly"
is stages 1–2, and stages 3–5 are the evaluation that consumes the assembled
bytes:

| # | stage | command | writes |
|---|---|---|---|
| 1 | packet assembly | `python3 tools/assemble-d2.py` | `examples/culture-d2/packet.d2.yml` |
| 2 | typed-label projection | `python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml` | `examples/culture-d2/typed-labels.d2.yml` |
| 3 | phonology gate | `python3 tools/gates/phonology-sanity-gate.py examples/culture-d2/packet.d2.yml` | stdout only |
| 4 | lexicon / myth / costume gates | `python3 tools/gates/lexicon-coverage-audit.py …`, `… myth-consistency-gate.py …`, `… costume-era-consistency-gate.py …` | stdout only |
| 5 | naming gate | `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` | stdout only |

Stage 2 is invoked as the round-8 pipeline's projection step (`--emit`); its
exit 1 is the tool's own contract ("findings emitted and the report is still
complete", docstring §Exit codes), and it is exit-1 in every run, uniformly.

## 2. Method — isolation, so the test cannot bless itself

- All runs happened in **self-contained copies** of `tools/`, `examples/`,
  `corpus/` under `.scratch/d11/runA`, `runB`, `runH` (scratch is gitignored).
  No run in this shard wrote inside the on-disk repository tree; the assembly
  legs only ever wrote inside copies.
- The only repository-tree legs were non-mutating: `python3 tools/assemble-d2.py
  --check` twice (exit 0 both times; `sha256sum` of `packet.d2.yml` and
  `typed-labels.d2.yml` identical before/after — `--check` writes nothing).
- Comparator: `cmp` on artifact bytes plus `sha256sum` on every artifact and
  every captured stdout; exit codes read from the shell, not the program text.
- Harness: `.scratch/d11/det-run.sh` (scratch) — per run it executes stages
  1–2 and the five gates, capturing `stdout+stderr` bytes and exit codes into
  `.scratch/d11/logs/<run>.<stage>.{out,exit}` and artifact hashes into
  `<run>.{packet,typed}.sha`.

## 3. Probes run (each against a fresh or reset copy)

| probe | what varies | runs |
|---|---|---|
| P1 consecutive | nothing — pass 2 immediately after pass 1 in `runA` | `A-pass1`, `A-pass2` |
| P2 second copy | absolute path (`runB` vs `runA`) | `B-pass1` |
| P3 cwd | process cwd (repo root vs `.scratch/d11`) | `X-cwd` |
| P4 hash seed | `PYTHONHASHSEED=0 / 1 / random` | `H0-seed0`, `H1-seed1`, `H2-seedrandom` |
| P5 locale | `LC_ALL=C LANG=C` | `H3-locc` |
| P6 mtime | `touch` of `components/02-phonology.yml` +1s before re-run | `B-mtime` |
| P7 live check leg | repo-tree `assemble-d2.py --check` ×2 | `live.check1/2` |
| P8 stripped env | `env -i PATH=/usr/bin:/bin TMPDIR=… python3 …` (no HOME, locale, seeds) | `C-envi` |

## 4. Results

**Artifact bytes** (all ten executions 22:02–22:08Z — P1, P2, P4, P5, P6, P8 plus P3's cwd run; each runs stages 1–2):

- `packet.d2.yml` = `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` in *every* run (all ten), `cmp` clean against `A1.packet.bin` in each comparison; identical to the live repository packet (so the repo leg adds no divergence).
- `typed-labels.d2.yml` (fresh emit) = `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` in every run; `cmp` clean.

**Gate stdout** (sha256 of captured bytes; identical across all nine gate-running runs — P1, P2, P4, P5, P6, P8; 45 gate executions):

| gate | stdout sha256 | exit |
|---|---|---|
| phonology-sanity-gate | `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` (3 FINDING lines) | 1 |
| lexicon-coverage-audit | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) | 0 |
| myth-consistency-gate | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) | 0 |
| costume-era-consistency-gate | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) | 0 |
| naming-collision-gate | `ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b` (17 FINDING lines) | 1 |

Exit codes across all runs: stage1 `0`; stage2 `1` (contract, §1); gates
`1/0/0/0/1` — constant. `e3b0c442…b855` is the sha256 of zero bytes (empty
stdout = fully clean gates).

**No wall-clock or environment leakage:** the artifacts contain no
`generated_at`/`timestamp` field (grep over both outputs finds only component
prose; the two `2026-10-17` strings in the packet are authored content from
`components/12-rank-rules.yml:87` and `08-symbols.yml:7,525`, confirmed by
grep in the component sources). Runs spanning ~6 minutes of wall clock
reproduce identical bytes, so no sub-run-resolution clock enters any output.

## 5. Drift disposition (the only red in the chain)

`python3 tools/d2-typed-labels.py --check` exits 1 at the tested revision:
the then-on-disk `examples/culture-d2/typed-labels.d2.yml` (working-tree
bytes, filed state since `e1694ba`) =
`e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f`,
fresh emit = `a3aa452c…`. `diff` (`.scratch/d11/logs/typed-drift.diff`) is
exactly one changed line:

```
9c9
<     "packet_sha256": "8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e",
---
>     "packet_sha256": "e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643",
```

- **Cause, named and previously filed:** the artifact's recorded packet pin is
  stale since the round-8 admit commit `e1694ba` (the packet was re-pinned
  inside the same commit; the derived artifact was not re-emitted). Round 9
  filed it (`reports/round-9/d3/interop.md` §4; `reports/round-9/d3/scribe.md:90`)
  and round 10 re-filed it (`reports/round-10/fix-02.md`, `fix-07.md:177`,
  `fix-08.md:101`, `fix-09.md:401`).
- **Disposition: neither defect-in-determinism nor environmental. It is a
  stale-artifact freshness condition.** The determinism question is whether
  repeated assemblies of the *same inputs* yield the same bytes — they do,
  across every probe including fresh-process, fresh-path and reseeded runs.
  The genuinely new byte (`a3aa452c…`) is itself reproduced identically by
  every independent run in this shard.
- **Repair ownership:** re-emitting/re-pinning the committed artifact is the
  D-wiring owner's call (claim D's "frozen replay re-pinned" leg); this seat
  changed no artifact. After any re-emit, the determinism receipts still apply
  and the `--check` red closes iff the re-emit lands with the wire.
- **Independent cross-check with the design (R11-D01):** the design fragment
  `reports/round-11/depth/design.md` §5.1 predicts the re-pinned projection
  bytes as `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`
  (3010 lines). My ten independent emits measured exactly that hash at exactly
  3010 lines (`wc -l`). Two independently derived artifacts agree on the
  re-pin's target byte, so the re-emit is mechanical and carries no
  uncertainty this shard can see.
- **Closed in-round, to the predicted bytes.** The re-pin landed at 22:15:59Z
  (`.scratch/d11/poll-wired.log`: the artifact sha flipped `e70ba147…` →
  `a3aa452c…`). At 22:18:08Z `python3 tools/d2-typed-labels.py --check` exits
  0 ("byte-identical deterministic projection") and `cmp` shows the on-disk
  artifact is byte-identical to `A1.typed.bin` — the fresh emit this shard had
  measured ten times. The red leg is closed by the D owner, not by this seat.

## 6. What this does not prove

- It does not assert the outputs are *right* — hold-set equality is R11-D09/D12;
  wiring-vs-design is R11-D20; the stale-pin repair was the D owner's and is
  recorded closed in §5.
- Single host, single interpreter (Python 3.14.7), no concurrency/parallel-run
  test, no cross-version test. Within those bounds determinism is total.
- The claim-D counting command (`python3 reports/round-11/run-validation.py`)
  did not exist at first test time (it landed 22:12:55Z, X03's); of its legs,
  `assemble-d2.py --check` (exit 0 ×2, §2) and the wired e2e (§7) are covered
  here, the runner itself is not this shard's to grade.
- The wired e2e chain was **measured and closed in §7** (on
  `tools/typed-gate-flow.py`, sha pinned there), not left to-verify.

## 7. Wired-chain closure — measured and closed (22:18–22:20Z)

The wiring landed as **`tools/typed-gate-flow.py`** (R11-D05; sha256
`5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075`) — not
under the design's working name `tools/gates/typed-pipeline-gate.py`; the
adapter role is the tool's `--emit`, and the derived artifacts are written to
`examples/culture-d2/packet.d2.typed.yml`
(`e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb`) and
`examples/culture-d2/typed-gate.expected.json`
(`7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa`).

Receipt (harness `.scratch/d11/det-run-wired2.sh`; copies `runW1`/`runW2`;
all exits 0):

| run | command | stdout sha256 | comparison |
|---|---|---|---|
| W1 pass 1 | `python3 tools/typed-gate-flow.py` | `204857cbb84d49cf39b51272651451609fa9a5ad29f4befdc712b07067d1f181` (49 lines) | — |
| W1 pass 2 (consecutive) | same | `204857cb…` | `cmp` IDENTICAL |
| W2 (second copy) | same | `204857cb…` | cross-copy IDENTICAL |
| E probes ×5 (`PYTHONHASHSEED`=0/1/random, `LC_ALL=C`, `env -i`) | same | `204857cb…` each | IDENTICAL |
| `--check` ×2 (per copy) | `… --check` | `760ce121869b16f316a4cc1fab8e14108cd97d33514435f4a89cb3c8f5dfb144` ("byte-identical deterministic derivation") | IDENTICAL |
| `--json` ×2 | `… --json` | `121e8c8ca62d7572bfdcd817f469e4cdae711e4b798964744cd6a7f0eeb69f8b` | IDENTICAL |
| `--emit` ×2 | `… --emit` | derived artifacts byte-identical after each emit and equal to the pre-run on-disk bytes | IDENTICAL |
| `--selftest` | `… --selftest` | "selftest: 14/14 checks passed" | exit 0 |

Default e2e and `--check` write nothing (artifact-hash snapshot before == after
each run). Run stdout: 49 lines, 15 `D2L-…[hold]` findings plus the note, and
the sound-channel line `off=GAR-01,…,GAR-10 on=0`. This closes D11 on the
wired chain: **two consecutive e2e assemblies are byte-identical**, also across
copies and environments.

Limits kept honest: the receipts pin `typed-gate-flow.py` at `5758e315…` (live
sha re-checked 22:19Z, unchanged); if the tool is edited again, these receipts
hold for the pinned revision, and a re-run is the closure for any new one.

## 8. Evidence trail (scratch, untracked)

- `.scratch/d11/logs/verdict.txt` — consolidated receipt: revision, tool
  shas, all `cmp` results, all artifact/gate hashes, all exit codes (64 lines,
  2026-10-17T22:03:51Z).
- `.scratch/d11/logs/` — per-run stdout and exit files for P1–P8; `A1/A2.*.bin`
  frozen output bytes; `typed-drift.diff`; `repo-status-at-test.txt`;
  `tools-sha-at-test.txt`; `wired-tools-sha.txt`; `live.wired-check.out`.
- `.scratch/d11/det-run.sh` — the pre-wiring harness (stages as §1);
  `.scratch/d11/det-run-wired2.sh` — the wired harness (§7); copies `runW1`,
  `runW2` (wired), `runA`–`runH` (pre-wiring) under `.scratch/d11/`.
- `.scratch/d11/poll-wiring.sh` + `poll.log` — the pre-wiring watch (60s
  cadence); `.scratch/d11/poll-wired.sh` + `poll-wired.log` — the post-design
  watch (60s cadence; it caught the 22:15:59Z re-pin, and kept logging).
- `.scratch/d11/wired/` — wired receipts: `W1.*`/`W2.*` stdout+exit files,
  `E-seed0|1|seedrandom|locc|envi.e2e.out`, `SELFTEST.out`, pre/after/emit
  artifact-hash snapshots, `*.cmp.verdict` files.
- Live legs: `.scratch/d11/logs/live.check1.out`, `live.check2.out` (both
  `packet.d2.yml: byte-identical deterministic assembly`, exit 0);
  `live.wired-check.out` (`typed gate artifacts: byte-identical deterministic
  derivation`, exit 0, 22:18:38Z).
