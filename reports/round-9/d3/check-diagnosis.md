# R9-D01 — D3 `--check` pin-drift diagnosis

- round: 9 (loop 1 of 3, build round 2 of 4) · shard: R9-D01 · date: 2026-10-17 (all stamps UTC)
- baseline revision: `e1694bad6ac96aca45a11ca5746582b275929355` (declared, `reports/round-9/claims.json:5`);
  measurement HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
- lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- owns: **this file only**. No tool, packet, component, pin, gate or LOG edit is made by this shard.
  Admission is the orchestrator's; this shard certifies no canon and absorbs no cross-shard decision.
- scratch: `/var/tmp/d3diag/` (outside the repo). `/tmp` was out of inodes at measurement time
  (`df -i /tmp`: `IUsed 1048576, IFree 0, IUse% 100%`), so `TMPDIR=/var/tmp` was set for any
  command that needs a temp dir.

## 0. Verdict (read this first)

| leg | command | result | status |
|---|---|---|---|
| D3 assembly check | `python3 tools/assemble-culture-d3.py --check` | both outputs `byte-identical deterministic assembly`, exit 0 | **PASS — no drift of the two D3 outputs** |
| D3 assembler selftest | `TMPDIR=/var/tmp python3 tools/assemble-culture-d3.py --selftest` | `selftest: 85/85 checks passed`, exit 0 | **PASS** |
| committed pin manifest | `examples/culture-d3/expected.json` `manifest` (24 entries) vs working tree | 21/24 match, **3 drift** | **DRIFT — see §2** |
| D3 frozen pin replay | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | exit 2, `3 × D3-SNAPSHOT` | **COULD-NOT-EVALUATE — pin refuses edited inputs, by design** |

So: the D claim's `--check` clause holds on the delivered tree. The *frozen* clause does not hold
until `expected.json` is re-authored. **The three drifts are legitimate and demonstrably
verdict-preserving for D3** (§3–§4); they are round-8 repairs that landed after the pin was frozen,
and the pin is behaving exactly as `corpus/knowledge/synthesis/worldbible-integration-contract.md:70`
requires. Refreshing the pin is a cross-shard/orchestrator act, flagged not absorbed (§6).

## 1. Receipts (verbatim)

Verbatim tool output, in the order printed, at the stamps shown.

- `2026-10-17T20:49:43Z`, `python3 tools/assemble-culture-d3.py --check`:
  `packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly` — exit 0.
- `2026-10-17T20:49:06Z`, `TMPDIR=/var/tmp python3 tools/assemble-culture-d3.py --selftest` (tail):
  `selftest: 85/85 checks passed — fixture CLI assemble/--check/determinism/tamper plus missing, invalid-JSON, invalid-UTF8, wrong-root, unexpected-key, missing-key, collision, wrong-type, below-minimum and serializer-absent fail-closed controls; real naming gate (CROSS-HOLD, no PHON/DERIV FAIL) and real costume gate (R-01 note, no R-02) run read-only; no file outside the temporary directory touched` — exit 0.
- `2026-10-17T20:49:43Z`, `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json`
  (stdout is one JSON object): `counts {"D3-SNAPSHOT": 3, "total": 3}`, `exit: 2`, findings:

  ```
  D3-SNAPSHOT manifest digest mismatch for 'corpus/knowledge/synthesis/worldbible-integration-contract.md':
              declared 50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1,
              actual   5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069
  D3-SNAPSHOT manifest digest mismatch for 'tools/gates/costume-era-consistency-gate.py':
              declared 29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03,
              actual   e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f
  D3-SNAPSHOT manifest digest mismatch for 'tools/gates/naming-collision-gate.py':
              declared 8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526,
              actual   d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
  ```

Exit-2 semantics are the tool's documented freeze behaviour, not a crash:
`tools/check-evidence-coupling.py:59` — `D3-SNAPSHOT  frozen input digest or manifest unreadable/mismatched
(exit 2, no traceback; --frozen only)`; `:70` — "The guard verifies EVERY manifest digest first … any
unreadable/mismatched/unsafe entry exits 2 with D3-SNAPSHOT before any [domain check]". No traceback was printed.

## 2. What the pin is, and what drifted

`examples/culture-d3/expected.json` (`profile kotodama-d3-evidence-coupling/1`, `expected_exit 0`,
`finding_ids []`) carries a 24-entry `manifest` of repo-relative path → sha256. It is the predeclared
computational snapshot for the D3 packet: per `:74-75`, the parent creates `expected.json` after inputs
land and predeclares the expectation; the tool reads it only under `--frozen`. `expected.json` is
deliberately **not** an entry of its own manifest (no self-hash), so only the inputs can drift.

Manifest sha256 (`sha256sum examples/culture-d3/expected.json`, 2026-10-17):
`74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080`.

The pin was authored at `57c3ce6` ("checkpoint: preserve unfinished round-7 D3 integration") — verified
with `git show 57c3ce6:examples/culture-d3/expected.json`, whose manifest already carries the three
declared digests quoted in §1. Drift table:

| manifest entry | pinned sha256 | actual sha256 | first changed at | documented cause |
|---|---|---|---|---|
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `50c4c2f2…8fb7268c1` | `5f4c02bf…fd4f79069` | `e1694ba` round-8 admit | round-8 metadata pass (header fields only) |
| `tools/gates/costume-era-consistency-gate.py` | `29a9361c…b3e5b3a43f03` | `e6bffd70…ceec478f` | `e1694ba` round-8 admit | round-8 O-shard parser hardening |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a…f19aa526` | `d9e4e8f4…1a630a1d` | `e1694ba` round-8 admit | round-8 O-shard parser hardening |

Command: `git log --oneline -4 -- <path>` per file (2026-10-17) — each shows only `e1694ba` after the
pin-authoring checkpoint; `git diff --stat 57c3ce6 HEAD -- tools/gates/ corpus/knowledge/synthesis/worldbible-integration-contract.md`
reports 599 insertions/73 deletions across 7 gate files plus `3 +` on the contract.

The other 21 entries, including every D3 input and output, still match — notably
`examples/culture-d3/components/{04,05,06,07}*.json` (the packet's own recorded `assembly.source_sha256`),
`examples/culture-d3/packet.json` `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829`,
`examples/culture-d3/packet.gates.yml` `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425`,
`tools/assemble-culture-d3.py` `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014`,
`tools/assemble-d2.py` `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d`,
`tools/check-evidence-coupling.py` `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e`,
`tools/gates/handoff-packet-check.py` `e2fa3223b2aa5738…`.

Command for the whole table (stdlib, no writes):
`python3 - <<'PY' … hashlib.sha256(path.read_bytes()) per manifest key … PY` (2026-10-17; the same
computation is what `tools/check-evidence-coupling.py:1465-1489` performs).

## 3. Is each drift legitimate?

**Contract `.md` — legitimate, content-inert for D3.** The whole diff against `57c3ce6` is three added
header lines (`corpus/knowledge/synthesis/worldbible-integration-contract.md:5-7`): a `source:` line, a
`verified-at: 2026-10-17 …` line, and a `recheck:` line. No rule text changed. The change is receipted
inside the round-8 batch that made it, including its digest transition, at
`reports/round-8/metadata/m07-synth-13-24.md:126`:
`worldbible-integration-contract.md 50c4c2f25a728e69… -> 5f4c02bfc4e6e4e9…`, with the row at `:110`
recording "added 3 fields" for row 24. D3 does not read this file at all: `packet.json` contains no
reference to it (`grep -c worldbible-integration-contract examples/culture-d3/packet.json` → 0; the only
repo paths inside the packet are the four `corpus/lessons/round-6-sources/*.json` references,
`examples/culture-d3/packet.gates.yml` and the two tool paths), and neither `tools/assemble-culture-d3.py`
nor `tools/check-evidence-coupling.py` opens it (`grep -rn worldbible-integration-contract tools/` matches
only `tools/gates/handoff-packet-check.py:6`, a docstring citation). Its manifest membership is snapshot
coverage, not a computed input.

**Both gates — legitimate, verdict-preserving on D3.** The round-8 O-shard edits are additive strictness
in the YAML/JSON subset parsers: flow nesting depth cap (`MAX_FLOW_DEPTH = 64`), rejection of
anchor/alias/tag syntax, and duplicate-key rejection in flow mappings, block mappings, mapping-list
entries and JSON objects (`object_pairs_hook=_json_object_no_duplicates`); see
`git diff 57c3ce6 HEAD -- tools/gates/naming-collision-gate.py tools/gates/costume-era-consistency-gate.py`.
They tighten rejection of malformed input and add no new accept path. The new bytes are already the
audited revision of record — `reports/round-8/operability/audit.md:23,25` lists `d9e4e8f4…` and
`e6bffd70…` under "Audited artifacts (sha256 at audit time)" — while the old bytes are the ones
round-8's own replay shard recorded as pins (`reports/round-8/depth/test-replay.md:37-38`).

Differential proof on the actual D3 projection (this shard, 2026-10-17T20:49Z): pinned round-7 gate
bytes (extracted with `git show 57c3ce6:<path>` into `/var/tmp/d3diag/old/`) and current bytes were run
as `python3 <gate> examples/culture-d3/packet.gates.yml`:

| gate | old exit / stdout sha256 | new exit / stdout sha256 | identical |
|---|---|---|---|
| `naming-collision-gate.py` | 1 / `c784dd037f62bf63501fe5f22c10519c50dee7213e5c75a4be2be50d48f2fe04` | 1 / same | **yes** |
| `costume-era-consistency-gate.py` | 1 / `926ceb7d752e55c4e31cb6c21ba96f0f6ab7dd6ef3abdb3dbed624489e32c9ce` | 1 / same | **yes** |

Both kept the D3-declared outcomes — naming: `NAME-NEAR REVIEW` plus `CROSS-HOLD HOLD … real-language
sweep not performed`; costume: `FINDING R-01: [note] C03 … declared violation … material/technical review
continues`, no `R-02`. This agrees with the assembler's own gate-facing assertions, which run the real
committed gates read-only and pass 85/85 on the delivered tree (§1).

Independent corroboration from round 8 that these repairs do not change verdicts on frozen artifacts:
`reports/round-8/depth/docs.md:150-157` (pre-repair replay `REPLAY OK: 7/7 rows`) and `:159-175`
(post-repair `COULD-NOT-EVALUATE gate_digest_mismatch`, "the pin is doing exactly what the frozen-run
standard requires"), with the verdict-preservation and re-pin remediation demonstrated in
`reports/round-8/depth/test-replay.md` §0/§6.

Cross-check: the same two gate digests are pinned in the *other* lane manifests with the same old values
(`tools/gates/frozen/round-3/MANIFEST.tsv` per `reports/round-8/depth/test-replay.md:37-38`), so this is
one systemic post-pin repair incident, not a D3-specific corruption of `expected.json`.

## 4. Does the drift change D3's meaning?

No, on the evidence above: the packet and projection bytes are unchanged and still match their own pins
(§2), all four component digests match both the manifest and the packet's internal
`assembly.source_sha256`, the assembler reproduces both outputs byte-for-byte on a clean run, and the two
gate-facing verdicts are byte-identical between pinned and current gate revisions (§3). The drift is
confined to snapshot coverage of three inputs that D3 computes nothing from — one content-doc and two
parser-hardened gates.

## 5. Limits

- This shard measured the working tree at HEAD `a7bb205` with the round-9 wave in flight. At the
  `2026-10-17T20:49:43Z` receipt the tree carried untracked `reports/round-9/{freshness,baselines,d3}/`,
  `tools/gates/expected/`, `tools/gates/frozen/{handoff-packet-check,lexicon-coverage-audit}/` and
  `.scratch/`, plus tracked-but-modified `corpus/knowledge/civilizations/{bali,byzantium,carthage,mali-songhai}.md`
  (other shards' in-flight work). None of these paths is a key of the D3 manifest, so no digest above is
  touched by them; the three drifted entries were re-measured on the settling tree and kept the shas in §1.
  A later edit by another round-9 shard to a manifest key would re-open the verdict.
- Digest recording is frame-checking, not proof of correctness of the gate repairs themselves: this shard
  shows verdict preservation on the D3 projection only (two gates, one input). The round-8 audit and replay
  shards above carry the broader claims.
- `/tmp` inode exhaustion (§0) is an environment condition, not a repo defect; it is noted because a
  re-runner of `--selftest` or any tempfile-based tool needs `TMPDIR=/var/tmp` at this revision.

## 6. Remediation (flagged to the orchestrator; not absorbed here)

Re-author `examples/culture-d3/expected.json` after the three inputs are re-acknowledged, per the
contract's own `recheck:` rule (`corpus/knowledge/synthesis/worldbible-integration-contract.md:7`:
"on any contract revision or pinned-digest change — both lanes re-read and acknowledge before importing
under it") and §4 (`:70`: "changing a referenced file invalidates that delivery's digest even if its
filename stays unchanged"). The mechanical refresh is: recompute sha256 for the 24 manifest keys (or only
the three drifted ones), keep `profile`, `expected_exit 0`, `finding_ids []`, `declared_expectation` and
`limits` byte-for-byte, then confirm
`python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json`
exits 0 with `finding_ids []`. Round-8 precedent for the equivalent D2 re-pin (`reports/round-8/depth/test-replay.md` §6)
shows the re-pin is sufficient to restore green; the same was not done for the D3 manifest. Until then,
D3's frozen element stays **could-not-evaluate**, honestly — not green, and not a silent pass.

## 7. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 tools/assemble-culture-d3.py --check                    # exit 0
TMPDIR=/var/tmp python3 tools/assemble-culture-d3.py --selftest # 85/85
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json              # exit 2, 3 × D3-SNAPSHOT
sha256sum examples/culture-d3/{packet.json,packet.gates.yml,expected.json} tools/assemble-culture-d3.py
git log --oneline -4 -- tools/gates/naming-collision-gate.py
```
