# R9-D08 — D3 docs + example regeneration evidence

- round 9 (loop 1 of 3, build round 2 of 4) · shard R9-D08 · date 2026-10-17 (all stamps UTC)
- tree under test: lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at
  `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (declared baseline `reports/round-9/claims.json:5`
  = `e1694bad6ac96aca45a11ca5746582b275929355`), worktree clean for tracked files
  (`git status --short` → only untracked `.scratch/`, 2026-10-17T20:48Z)
- owns: **this file only**. No tool, packet, component, pin, gate, README, handoff or LOG edit
  is made by this shard. Admission is the orchestrator's.
- claim under test: depth claim **D** (`reports/round-9/claims.json`), the docs/example slice —
  target `R9-D08` in `reports/round-9/targets.json`
- sibling shards cross-referenced, not duplicated: `check-diagnosis.md` (R9-D01, same pin-drift
  cluster, mechanical refresh steps in its §6), `determinism.md` (R9-D02),
  `interop.md` (R9-D06), `capability-draft.md` (R9-D07)
- scratch: `.scratch/d3-docs-r9/regen/` (untracked, **not** a deliverable). All commands below
  ran from the repo root or from that sandbox as stated.

## 1. Docs surface under test (measured 2026-10-17T20:48–20:50Z)

| doc | lines | sha256 (measured) | freeze status |
|---|---:|---|---|
| `examples/culture-d3/README.md` | 171 | `d0f62ad7472ef04176130ad4b9e732cf8ae1b61db9efa6da787dac19a3929aa4` | outside the computational freeze (by design) |
| `examples/culture-d3/handoff.md` | 286 | `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc` | outside the computational freeze (by design) |

Command: `wc -l examples/culture-d3/README.md examples/culture-d3/handoff.md` and
`sha256sum` on both, 2026-10-17T20:48:51Z.

Both round-7 dispatch-#14 doc duties are present (handoff envelope + directory README); the D3
room has no `ASSEMBLY.md` (the D2 room's is its own artifact) — `reports/round-7/d3-contract.json`
requires only that "README documents real commands and expected holds", which the README does.
Freeze exclusion verified: `examples/culture-d3/expected.json` manifest (24 keys) contains
neither doc path (python check, 2026-10-17T20:49Z); all 24 manifest paths exist on disk.

## 2. Example regeneration evidence (the core of this shard)

Sandbox tree: `tools/assemble-culture-d3.py`, `tools/assemble-d2.py`, `tools/gates/{naming-collision-gate.py,costume-era-consistency-gate.py,handoff-packet-check.py}`,
`examples/culture-d3/components/*.json` plus the committed `packet.json`/`packet.gates.yml` copies.
Both outputs were **deleted** before the build, so the run proves regeneration from components alone.

```sh
cd .scratch/d3-docs-r9/regen
rm -f examples/culture-d3/packet.json examples/culture-d3/packet.gates.yml
find . -type f | sort > before.list
python3 tools/assemble-culture-d3.py            # exit 0
find . -type f | sort > after.list
diff before.list after.list                     # see exactly-two-files note below
sha256sum examples/culture-d3/packet.json examples/culture-d3/packet.gates.yml
python3 tools/assemble-culture-d3.py --check    # exit 0
sha256sum examples/culture-d3/packet.json examples/culture-d3/packet.gates.yml > run1.sha
python3 tools/assemble-culture-d3.py            # second build, exit 0
sha256sum -c run1.sha                           # both OK
cmp examples/culture-d3/packet.json ../../../examples/culture-d3/packet.json
cmp examples/culture-d3/packet.gates.yml ../../../examples/culture-d3/packet.gates.yml
```

Observed, 2026-10-17T20:49–20:50Z (stdout quoted from the sandbox runs):

- build stdout: `Wrote examples/culture-d3/packet.json (37222 bytes)` /
  `Wrote examples/culture-d3/packet.gates.yml (14191 bytes)`, exit 0
- the before/after file-list diff adds exactly the two outputs (the only other line is my own
  `after.list`): no third file is written by the default build
- regenerated digests, measured in the sandbox:
  `packet.json` = `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829`,
  `packet.gates.yml` = `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425`
  — byte-identical to the committed tree (both `cmp` silent, exit 0; same values as the
  repo-root `sha256sum` of 2026-10-17T20:48:51Z and as README.md:27–28 / handoff.md A-PACKET/A-GATES)
- `--check` after regeneration: exit 0, `packet.json: byte-identical deterministic assembly;
  packet.gates.yml: byte-identical deterministic assembly`
- second consecutive build: `sha256sum -c` → both `OK` (byte-stable; determinism detail is R9-D02's)
- the regenerated packet's `assembly.source_sha256` (four component digests) and
  `assembly.serializer_sha256` equal the actual component/serializer bytes measured at the repo
  root (python read of the packet, 2026-10-17T20:48Z) — the generated packet pins its real inputs

**Conclusion:** the committed examples are reproducible artifacts: deleting both outputs and
running the documented default build restores byte-identical committed bytes, and the README's
rebuild instructions reproduce as written.

## 3. Documentation claim verification (machine-checked, 2026-10-17T20:48–20:50Z)

### 3.1 Digest claims

| claim surface | rows checked | match | drift |
|---|---:|---:|---:|
| README.md:25–39 digest table (6 rows parsed by regex + controls/expected/3 tools rows checked targetedly) | 11 | **11** | 0 |
| handoff.md:56–74 artifact-manifest `A-*` rows (path+digest parsed from the markdown table) | 17 | **16** | 1 — `A-CONTRACT` |
| README.md:100–104 `sha256sum`-block prefixes (4 ledgers + contract) | 5 | **4** | 1 — contract prefix `50c4c2f2…` |
| expected.json manifest keys (whole-file `sha256` over 24 keys) | 24 | **21** | 3 (finding F1) |

Machine-check commands (both parse the docs verbatim and hash the named paths):
`python3` inline parsers run 2026-10-17T20:48–20:50Z, regex `\| \`([^\`]+)\` \| \`([0-9a-f]{64})\` \|`
for README and `\| (A-[A-Z0-9+ -]+) \| ([^ |]+) \| [^|]+ \| \`([0-9a-f]{64})\` \|` for handoff.

### 3.2 Observed-run claims (README.md:83–95 table and handoff.md:205–247 validation block)

Re-run on the delivered tree:

| documented run | documented | re-observed 2026-10-17 | verdict |
|---|---|---|---|
| `assemble-culture-d3.py --check` | exit 0 byte-identical | exit 0, both outputs byte-identical | reproduces |
| `check-evidence-coupling.py packet.json` | exit 0, `findings: []`, `counts.total: 0` | exit 0, exactly that JSON | reproduces |
| `check-evidence-coupling.py --selftest` | exit 0; positives 5/5, domain 16/16, malformed 4/4, frozen 5/5 | exit 0; `selftest_passed: true`, `positive_controls 5/5`, `domain_controls 16/16`, `malformed_controls 4/4`, `frozen_checks 5/5`, 32 results | reproduces exactly |
| `naming-collision-gate.py packet.gates.yml` | exit 1: CROSS-HOLD ×2 + NAME-NEAR REVIEW, no phonology/derivation FAIL | exit 1 with exactly those three findings | reproduces |
| `costume-era-consistency-gate.py packet.gates.yml` | exit 1: exactly one finding, R-01 note | exit 1, exactly R-01 | reproduces |
| `handoff-packet-check.py handoff.md` | exit 0, `fields=16/16 glossary-entries=20 findings=0` | same string, exit 0 | reproduces |
| `… --frozen examples/culture-d3/expected.json` | exit 0, `findings: []` | **exit 2, `D3-SNAPSHOT` ×3** | **does NOT reproduce — finding F1** |

### 3.3 Structural / count claims (all re-derived from bytes, 2026-10-17)

- controls.json counts: 3 positive / 16 domain / 4 malformed (README.md:33, handoff.md:64) — verified
  by python read; names quoted in §5 sweep.
- packet record counts (README.md:4–8, handoff.md `scope` row): eras 2 · lexicon 20 · names 6 ·
  utterances 7 · beliefs 2 · symbols 2 · materials 3 · objects 4 · costumes 4 · rank_rules 1 ·
  references 5 · bridges 5 (+ sound_changes 1, speech_rules 1) — all match.
- `canon_status: NON-CANON`, `handoff_status: prepared-not-accepted`, `screening.status: unresolved`,
  `real_language_sweep_performed: false` — match the docs' boundary statements (README.md:10–16).
- beliefs B01/B02 both `truth_status: unresolved`; C03 `claimed_status: violation` with
  RR1 (plant-cloth, visitor, hall, assembly, no exemptions); symbols SY01/SY02 audience-scoped —
  match README.md:129–152 expected-holds text.
- bridges: BR01 S01→U01/U02, BR02 S02→C01/C02, BR03 S03→NR1, BR04 S04→O01/O04 (`analogy`),
  BR05 S05→SY01/B01, all `design-only`/`constructed-rule` — match README.md:122–124.
- generated-packet hygiene: `grep -c '2026\|/home/' examples/culture-d3/packet.json` → 0 matches
  (exit 1); final byte `0a` (clean newline) — consistent with the "no timestamps or absolute
  paths" boundary claim.
- expected.json shape: 24 keys, `expected_exit: 0`, `finding_ids: []`, docs excluded (§1) — as
  documented; its own `limits` field states "later input edits invalidate this snapshot before
  verdict", which is exactly what finding F1 then exercises.

## 4. Findings

### F1 — the freeze is invalidated by round-8's legitimate edits; three doc rows and the frozen run no longer reproduce (blocking the frozen element of claim D)

`python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json`
→ **exit 2**, `counts: {D3-SNAPSHOT: 3, total: 3}`, findings:

1. `manifest digest mismatch for 'corpus/knowledge/synthesis/worldbible-integration-contract.md': declared 50c4c2f2…, actual 5f4c02bf…`
2. `manifest digest mismatch for 'tools/gates/costume-era-consistency-gate.py': declared 29a9361c…, actual e6bffd70…`
3. `manifest digest mismatch for 'tools/gates/naming-collision-gate.py': declared 8c5afb0a…, actual d9e4e8f4…`

Attribution (git receipts, 2026-10-17T20:49Z): at the freeze-era round-7 baseline `30caac6`
the three files hash to exactly the declared values; at round-8 admit `e1694ba` they hash to the
current values — `git show --stat e1694ba -- …` shows the contract +3 lines and the two gates
+236/+73 lines ("harness+gate repairs"). So the freeze was accurate when written and was
invalidated by round 8, not by any defect in it or in the guard.

Stale documentation rows (same root cause — dated observations that no longer reproduce):

- `examples/culture-d3/README.md:46–48` ("the packet-vs-frozen guard run is observed … exit 0 /
  `findings: []`") and row `README.md:91`
- `examples/culture-d3/handoff.md:39` (`validation` field), `:239–241` (validation block's frozen
  run), `:278` (OQ-D3-06 "observed exit 0 / findings []")

Not a gate bug: the guard fail-closes (could-not-evaluate, exit 2) instead of blessing a stale
pin, which is the contract-correct behavior (d3-contract.json `guard_cli`: "returns exit2
D3-SNAPSHOT on tamper"). Remediation is parent-owned and mechanical: refresh the three digests
in `expected.json` after the re-verification that this session already observed (`--check` 0,
guard non-frozen 0, gates exactly as documented), then re-run frozen mode → expected exit 0;
finally update or re-date the five doc rows above. The deeper contract reading and the
step-by-step refresh recipe are in `reports/round-9/d3/check-diagnosis.md` §6 (R9-D01); the
round-8 precedent is the D2 re-pin cited there. This shard writes none of those files.

### F2 — the contract digest is stale in two docs (same root cause)

README.md:104 prints the contract prefix `50c4c2f2…`; handoff.md:27 (`contract_ref`, which even
claims "re-measured 2026-10-17 from current bytes") and handoff.md:74 (`A-CONTRACT`) print the
full `50c4c2f2…`. Current bytes: `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`.
Round 8 already recorded this transition (`reports/round-8/adjacency.md:128`
"worldbible-integration-contract.md 50c4c2f2… -> 5f4c02bf…", same digest at
`reports/round-8/depth/findings.md:8`), so the docs simply never followed it. Contract revision
string stays `1.0.0` per that record; only the digest column is wrong.

### F3 — nuance for the acceptance ledger: a green `--selftest` does not clear the committed freeze

The selftest's `frozen_checks 5/5` runs fixture manifests in scratch; it stays green while the
committed `expected.json` fails (`F1`). The README does not conflate the two; the round-9
acceptance ledger must not either. Claim D's frozen element is currently **could-not-evaluate**,
honestly reported, not green.

## 5. Negative sweeps (each claim carries the command that produced it)

- *No other stale digest in the docs' claim surface* — the two row parsers above scanned every
  digest row in both tables plus every `sha256sum`-block prefix: 11 + 17 + 5 = 33 rows, with the
  single contract-drift cluster (F1/F2) as the only mismatch. Commands: the two
  `python3` inline parsers, 2026-10-17T20:48–20:50Z.
- *No third file written by the default build* — sandbox `find | sort` before/after diff, quoted
  in §2; the only added paths are the two outputs (plus this shard's own bookkeeping file).
- *No timestamps or absolute paths in the generated packet* — `grep -c '2026\|/home/' packet.json`
  → 0 (exit 1).
- *No manifest path missing* — all 24 `expected.json` keys exist (`os.path.exists` over the
  manifest, 2026-10-17T20:49Z).
- *Docs excluded from the freeze* — `examples/culture-d3/handoff.md` and `README.md` are both
  absent from the 24-key manifest (same python check) — no self-digest cycle.

## 6. Limits, non-claims, environment

- This shard re-verifies docs against bytes and the example regeneration; it does **not**
  re-fetch or re-verify any source URL (freshness hunters own that), does not re-run the
  field-by-field packet-vs-contract check (R9-D11), and does not replace R9-D03/R9-D04 receipts
  (it corroborates them on the docs/example slice).
- Environment: `/tmp` was out of inodes during this session (`df -i /tmp` →
  `IUsed 1048576, IFree 0, IUse% 100%`; `mktemp -d /tmp/…` failed with "No space left on
  device"), so all scratch was repo-local under `.scratch/d3-docs-r9/`. Same condition recorded
  by R9-D01 §0. A re-runner of tempfile-based tools needs `TMPDIR=/var/tmp`.
- `.scratch/d3-docs-r9/` is untracked scratch, not a deliverable; if it is cleaned, every result
  in this fragment stands on the quoted commands and outputs alone.
- The acceptance-runner receipt remains **pending** and is not declared passed by this shard.
  No canon, promotion, or completion claim is made anywhere in this fragment.

## 7. Reproduce (repo root, 2026-10-17)

```sh
python3 tools/assemble-culture-d3.py --check                    # exit 0, byte-identical
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json   # exit 0, findings []
python3 tools/check-evidence-coupling.py --selftest             # exit 0, 5/5 · 16/16 · 4/4 · 5/5
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json              # exit 2, 3 × D3-SNAPSHOT (F1)
sha256sum examples/culture-d3/README.md examples/culture-d3/handoff.md
```
