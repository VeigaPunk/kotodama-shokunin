# R9-D12 — scribe: D3 acceptance ledger fragment

- round: 9 (loop 1 of 3, build round 2 of 4) · shard: R9-D12 (scribe) · 2026-10-17 (stamps UTC)
- baseline revision (declared): `e1694bad6ac96aca45a11ca5746582b275929355` (`reports/round-9/claims.json`)
- measurement HEAD: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (all commands below run there unless stated)
- writes: **this file only**. The ledger ties sibling D3 fragments together; it certifies no
  canon, performs no re-pin, admits nothing. SCORECARD admission is the orchestrator's.
- canon: NON-CANON engineering evidence. A frozen pin proves bytes and a verdict, never
  design quality, scholarship, cultural clearance or lore acceptance.

Status at this handoff: **complete for this shard's scope; the D3 acceptance verdict is NOT
uniformly green.** All twelve round-9 D3 fragments (D01–D11 plus this scribe) have landed and
are tied in below; the round's counting command (`reports/round-9/run-validation.py`, landed
`20:53Z`) itself reports `claims.D.passed: false` with the frozen leg as the sole D failure.
Fifteen acceptance legs: **13 green** (byte-identical assembly; assembler selftest 85/85; guard
selftest 5/5+16/16+4/4+5/5; live run 0 findings; determinism under 13 probes + isolated mirror;
replay-tool selftest 79/79; D05's 32-case CLI negatives; d2 interop byte-identical to the
round-8 admitted values; D04's proposed projection manifest 5/5; D08 regen/docs; D10's 62/63
independent re-derivation; D11's 138/138 contract check; D09's clean circularity audit), **one
could-not-evaluate — red by design** (the committed freeze: `--frozen
examples/culture-d3/expected.json` exits 2 with `3 × D3-SNAPSHOT` because three pinned inputs
were legitimately revised by the round-8 admission commit `e1694ba` after the pin was authored
at `57c3ce6`; verdict-preserving for D3 — D01, D10 and D09 reproduced the pinned-vs-current
gate differential independently), and **one gated draft** (D07's SCORECARD row). The refresh
recipe exists (D01 §6) and was demonstrated in scratch (D04 leg E), but **no committed re-pin
has happened**, so claim D's "replays frozen" clause stands as could-not-evaluate — and any
later green must satisfy D09 S1's re-verification record (§3.4). The decision to re-pin or to
admit with the exception recorded is the orchestrator's (§5, §6).

## 1. Measurement environment and concurrency

```sh
git rev-parse HEAD && git status --porcelain && date -u +%FT%TZ
```

Observed `2026-10-17T20:47–20:52Z`:

```
a7bb205d3aecdaa24d91c047c8719cd8689e4ddd
?? .scratch/
?? reports/round-9/baselines/
?? reports/round-9/d3/
?? reports/round-9/freshness/
?? tools/gates/expected/
?? tools/gates/frozen/handoff-packet-check/
```

- At the measurement window `20:47–20:52Z` the worktree had no `M` entries at all. By `20:54Z`
  sibling shards' tracked edits had begun landing (the round-9 metadata sweep's
  `corpus/knowledge/civilizations/*.md` and `culture-material/*.md` stragglers, and
  `tools/check-gate-battery.py` — O15 work); **none of them is a D3 manifest key** —
  re-verified `20:54:21Z`: the 24-key sweep still reads 21 match / the same 3 mismatch, and
  `git status --porcelain -- <the 24 manifest keys>` is empty. The untracked round-9 additions
  are sibling evidence (`baselines/`, `tools/gates/expected/`, `tools/gates/frozen/*` are O-shard
  work; `d3/`, `freshness/`, `metadata/`, `.scratch*/` are D/F/metadata shards). A digest of a
  tracked manifest key cannot be moved by an untracked addition; a re-runner must nonetheless
  re-run the sweep at integration, since the wave was still editing other tracked files.
- **Environment constraint (two shards hit it):** `/tmp` is out of inodes —
  `df -i /tmp` → `1048576 1048576 100%` (2026-10-17), and a scratch write to `/tmp` failed with
  `No space left on device`. All this shard's scratch ran under `$HOME/.cache/scribe-r9-d3/`;
  D01 used `TMPDIR=/var/tmp`. A re-runner of `--selftest` or any tempfile-based tool must
  redirect `TMPDIR` at this revision (D01 §5 records the same condition independently).
- Concurrency caveat: sibling shards wrote into the tree throughout the measurement window
  (untracked additions; tracked edits began at `20:54Z` — first bullet). Every digest and verdict
  below names its stamp; re-runs after integration may legitimately differ where sibling work
  lands, but no tracked D3 input moved during the window (§4 recomputation matches D01's).

## 2. Claim D acceptance ledger — leg by leg

Claim D's `after_required` (`reports/round-9/claims.json`): `--check` exits 0 byte-identical;
`check-evidence-coupling.py --selftest` green; **D3 replays frozen without digest drift**;
capability row enters SCORECARD only on demonstrated run (orchestrator admits). The claim's
counting command `python3 reports/round-9/run-validation.py` **landed at `20:53Z`** (O16,
`reports/round-9/validation.json`): it reports `claims.D.passed: false`,
`acceptance_checks_passed: false`, the single D failure being
`tools/check-evidence-coupling.py --frozen examples/culture-d3/expected.json exit 2 (expected 0:
no digest drift)` with `finding_ids [D3-SNAPSHOT ×3]` — i.e. the counting command records the
same honest red this ledger does (D09 §6 checked it independently).

| # | leg | command | observed | status | sources (fragment + this shard) |
|---|---|---|---|---|---|
| 1 | deterministic assembly | `python3 tools/assemble-culture-d3.py --check` | `packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly`, exit 0 | **PASS** | D01 §1 (`20:49:43Z`); D02 §1 (`20:48Z`); D03 §2; this shard `20:47:26Z` + isolated mirror |
| 2 | assembler selftest | `TMPDIR=… python3 tools/assemble-culture-d3.py --selftest` | `selftest: 85/85 checks passed …`, exit 0 | **PASS** | D01 §1 (`20:49:06Z`); D05 baselines (85/85 with default and redirected temp dir); this shard `20:52:2xZ` |
| 3 | guard selftest | `python3 tools/check-evidence-coupling.py --selftest` | `selftest_passed: true`; positive 5/5, domain 16/16, malformed 4/4, frozen 5/5; exit 0 | **PASS** | this shard `20:47Z`; D03 §1 (full JSON receipt); D07 §5.1 |
| 4 | live coupling run | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | `{"counts": {"total": 0}, "exit": 0}` | **PASS** | this shard `20:48Z`; D03 §2; D07 §5.1 |
| 5 | frozen replay (committed pin) | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | `counts {"D3-SNAPSHOT": 3}`, `exit: 2`; 21/24 manifest entries match | **COULD-NOT-EVALUATE — red by design** (§3) | D01 §1 (`20:49:43Z`); D03 §3; D04 leg D; D07 §5.2; D08 F1; D10 F2; this shard `20:48Z` + 24-key recomputation `20:52Z` |
| 6 | determinism | double regeneration + environment probe matrix | D02: 13 probes all `IDENTICAL`, in-place double regen, leak sweep clean; this shard: isolated mirror build1 == build2 == committed bytes | **PASS** | D02 §2–§5 (`20:48–49Z`); this shard `20:50:1xZ` |
| 7 | replay-frozen tool | `python3 tools/replay-frozen.py --selftest` | `selftest: 79/79 checks passed`, exit 0 | **PASS** | this shard `20:49Z`; D04 leg A (`20:49Z`) |
| 8 | CLI negatives | malformed/absent inputs → stable exit 2 | D05 battery 32/32 (29 negatives + 3 controls), all exit 2, no tracebacks, no writes, diagnostics byte-stable; this shard's 5 probes agree in kind | **PASS** | D05 (whole fragment; 5 battery runs `20:48–52Z`); this shard `20:51:3xZ` |
| 9 | interop (d2-typed-labels, assemble-d2) | no cross-contamination after round 9 | `d2-typed-labels.py --selftest` 39/39 exit 0; `assemble-d2.py --check` exit 0; both stdout digests byte-identical to round-8 admitted values; no round-9 file in the d2 read-set | **PASS (assigned legs)**; one pre-existing red recorded outside round 9 (`d2-typed-labels.py --check` exit 1, stale one-line packet pin dated to `e1694ba`) | D06 §1–§3, §6; red in D06 §4 |
| 10 | D3 projection frozen manifest (proposed, scratch) | `python3 tools/replay-frozen.py <proposal>/MANIFEST.tsv --repo-root <d3root>` | `REPLAY OK: 5/5 rows reproduced`, exit 0; C1–C4 tamper/live-drift controls all fail-closed or provably never read the live input; reproduced holds stay red (reproduction, not clearance) | **PASS as reproduction**; manifest **not committed** — adoption is the integrator's call | D04 §1–§2 |
| 11 | D3 docs + example regeneration | build from components alone in a sandbox; doc-claim re-observation | outputs byte-identical to committed (`bdf635ce…`/`306bcac7…`); documented runs re-observed; five doc rows stale from the same 3-entry root cause | **PASS (regen); doc findings filed** | D08 §2–§4 |
| 12 | independent re-derivation (adversarial) | hand rebuild of the projection from components, byte-compare | 62/63 checks passed; the one failure is a 36-byte prose divergence between the two committed artifacts (F1, informational); patching that sentence reproduces committed bytes exactly | **PASS (with F1 resource note)** | D10 §1–§3 |
| 13 | D3 contract cross-check | packet vs `reports/round-7/d3-contract.json` field by field | 138/138 packet-side contract checks pass; contract-consistent; F-1 records the same stale freeze and recommends refresh, "never weakening the check" | **PASS (packet); F-1 = the §3 finding** | D11 §Verdict, §F-1, §Packet field-by-field |
| 14 | SCORECARD capability row | reproducible-D3-assembly row text | draft landed with admission checklist | **DRAFT, gated** — D07 §2: "Do not land the row while that run is red" | D07 §2–§3 |
| 15 | circularity audit (D09) | adversarial audit of the whole D3 acceptance evidence | No fabricated or self-blessed green found anywhere; every shard reports the frozen red honestly. **S1 (blocking condition):** any later green from a re-pin must carry its re-verification record (minimum record listed) or it is indistinguishable from blessing the tamper. S2–S6: selftest cannot see the committed freeze; D04's proposal self-captured (controls prove it can fail); control matcher accepts supersets; freeze unpinned by construction; `--selftest` sits outside the assembler's exit-2 envelope; hash-convention note | **PASS (no false green); conditions attach to any later green** | D09 §2–§3, §6 addendum |

Pins for the green legs (measured `2026-10-17T20:49:29Z`, `sha256sum`):

| artifact | sha256 | bytes |
|---|---|---|
| `examples/culture-d3/packet.json` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` | 37222 |
| `examples/culture-d3/packet.gates.yml` | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` | 14191 |
| `examples/culture-d3/expected.json` | `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` | — (24-entry manifest) |
| `examples/culture-d3/controls.json` | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` | — |
| `examples/culture-d3/handoff.md` | `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc` | — |
| `examples/culture-d3/README.md` | `d0f62ad7472ef04176130ad4b9e732cf8ae1b61db9efa6da787dac19a3929aa4` | — |
| `tools/assemble-culture-d3.py` | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` | — |
| `tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` | — |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` | — |
| `tools/replay-frozen.py` | `a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464` | — |
| `examples/culture-d3/components/04-language.json` | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` | — |
| `examples/culture-d3/components/05-ritual.json` | `20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d` | — |
| `examples/culture-d3/components/06-material.json` | `ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7` | — |
| `examples/culture-d3/components/07-evidence.json` | `1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3` | — |

The packet/projection digests equal the committed git blobs at HEAD (D02 §4: `git hash-object`
== `git rev-parse HEAD:` for both), and equal their entries in the pin manifest (§3) — the
worktree is a fresh assembly of committed inputs, not a stale copy.

## 3. The frozen-pin incident (the ledger's sharp edge)

### 3.1 What the pin is

`examples/culture-d3/expected.json` (`profile kotodama-d3-evidence-coupling/1`,
`expected_exit: 0`, `finding_ids: []`, `declared_expectation` fixed before tool
implementation, 24 manifest entries) is the predeclared computational snapshot the guard
verifies under `--frozen`; any manifest mismatch exits 2 with `D3-SNAPSHOT` **before any
domain check** (`tools/check-evidence-coupling.py:59, :70-75`). It is deliberately not an
entry of its own manifest (no self-hash) and excludes the generated `handoff.md`/`README.md`
(no output cycle). Authored at `57c3ce6` (round-7 checkpoint), verified by
`git show 57c3ce6:examples/culture-d3/expected.json` (D01 §2).

### 3.2 What drifted — three entries, one cause commit

Independent recomputation by this shard (`python3 -` one-liner over all 24 keys,
`2026-10-17T20:52Z`; same computation the guard performs at
`tools/check-evidence-coupling.py:1465-1489`): **24 entries, 21 match, 3 mismatch** — exactly
the guard's findings, no fourth drift, no missing key.

| manifest entry | pinned sha256 | actual sha256 | first changed at | documented cause |
|---|---|---|---|---|
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `50c4c2f2…8fb7268c1` | `5f4c02bf…fd4f79069` | `e1694ba` | round-8 metadata pass, +3 header lines only (`reports/round-8/metadata/m07-synth-13-24.md:110,126`) |
| `tools/gates/costume-era-consistency-gate.py` | `29a9361c…b3e5b3a43f03` | `e6bffd70…ceec478f` | `e1694ba` | round-8 O-shard parser hardening (+73 lines vs round-1 base) |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a…f19aa526` | `d9e4e8f4…1a630a1d` | `e1694ba` | round-8 O-shard parser hardening (+236 lines vs round-1 base) |

Attribution commands (this shard, `2026-10-17`): `git log --oneline -3 -- <path>` per file —
each shows only `e1694ba` after the pin-authoring checkpoint `57c3ce6`; the worktree bytes
equal `git show HEAD:<path>` bytes for all three. D01 §2 reports the same table from
`git diff --stat 57c3ce6 HEAD` (599 insertions / 73 deletions across seven gate files, `3 +`
on the contract).

### 3.3 Is the drift legitimate and verdict-preserving? — yes, on D01's evidence

- The contract change is content-inert for D3: three added header fields, no rule text; the
  packet contains no reference to the file (`grep -c worldbible-integration-contract
  examples/culture-d3/packet.json` → 0, D01 §3). Its manifest membership is snapshot
  coverage, not a computed input.
- The gate edits are additive parser strictness (flow-depth cap, anchor/alias/tag rejection,
  duplicate-key rejection) with no new accept path (D01 §3, citing the diff). **Differential
  proof on the actual D3 projection** (D01 §3, this shard has not re-run it): pinned round-7
  gate bytes and current bytes both exit 1 with byte-identical stdout on
  `examples/culture-d3/packet.gates.yml` — naming `c784dd03…` (NAME-NEAR + CROSS-HOLD), costume
  `926ceb7d…` (R-01 note, no R-02). The assembler's own gate-facing assertions pass 85/85 on
  the delivered tree (leg 2).
- The new gate bytes are the audited revision of record (`reports/round-8/operability/audit.md:23,25`);
  the old bytes are round-8's own recorded pins (`reports/round-8/depth/test-replay.md:37-38`).
  This is one systemic post-pin repair incident across lane manifests, not a D3-specific
  corruption (D01 §3 cross-check).

### 3.4 What the red leg means for claim D

- Under reading (a) **"the committed pin matches the delivered tree"**: currently false, and
  it fails *closed* — the guard exits 2 and refuses comparison, which is exactly the
  freeze discipline `corpus/knowledge/synthesis/worldbible-integration-contract.md:70` and the
  frozen-run standard require. The red is not a defect; it is the pin working.
- Under reading (b) **"no input has changed since freeze"**: already violated legitimately by
  round-8 (`e1694ba`), documented above.
- Remediation is mechanical and has lane precedent: re-author `expected.json` after the three
  inputs are re-acknowledged (recompute digests from bytes, keep `profile`, `expected_exit`,
  `finding_ids`, `declared_expectation`, `limits` as predeclared), then confirm the `--frozen`
  command exits 0 with no findings — D01 §6 gives the recipe; the round-8 D2 re-pin
  (`reports/round-8/depth/test-replay.md` §6) is the precedent. **As of this stamp no shard
  has performed it** (`examples/culture-d3/expected.json` digest unchanged:
  `74496aa8…`, this shard `20:49:29Z`). Until it is performed, claim D's frozen clause is
  **could-not-evaluate**, and any admission text that calls it green would be wrong.
- **D04 leg E demonstrated the refresh in scratch** (`replay.md` §0): updating exactly the
  three digest lines yields `--frozen` exit 0 with `findings: []`; a tampered twin still exits 2
  `D3-SNAPSHOT`; a half-frozen tree (packet edited) is still caught. The remediation is
  validated, not merely proposed — and still not committed.
- **Independent confirmations of the red**: D01, D03 §3, D04 leg D, D07 §5.2, D08 F1 and D10 F2
  all record the same 3-entry drift. D10 additionally re-ran the *pinned round-7 gate bytes*
  (`8c5afb0a…`/`29a9361c…`, extracted with `git show 57c3ce6:`) against the projection and got
  byte-identical output to the current gates — the round-8 hardening is behavior-neutral on
  this artifact. **D08 F3** states the ledger rule plainly: a green `--selftest` (leg 3, fixture
  manifests in scratch) does not clear the committed freeze (leg 5). **D08 F2** adds that five
  doc rows still print the pre-round-8 contract digest (`README.md:46-48,91,104`;
  `handoff.md:27,39,74,239-241,278`) — re-date them at re-pin time.
- **D07 §2 gates the SCORECARD row on the re-pin**: "Do not land the row while that run is red."
- **D10 F1 nuance for any re-pin or future drift-pin**: `packet.gates.yml`'s `assembly.rule` and
  `packet.json`'s `assembly.legacy_projection.rule` are intentionally different sentences
  (36-byte delta; no gate reads either string), so a byte-level cross-artifact assertion written
  against one reads as drift against the other; unify or record as intentional — no behavior
  impact either way.
- **D09 S1 — blocking condition on any later green**: after this wave the only step to a green
  frozen leg is a re-pin, and a re-pin is "mechanically indistinguishable from a
  bless-the-tamper operation" (D09 §2 demonstrated the bless path in an isolated copy) unless it
  carries a re-verification record. D09 lists the minimum record: the pre-refresh freeze token
  (sha256 `74496aa8…`, git blob `c420ac4c…`), the three keys with old → new digests and the
  causing commit (`e1694ba`), the verdict-preservation differential on the projection
  (D01/D10/D09 each reproduced it), the byte-level no-change traversal (components match pins;
  outputs hash to their HEAD blobs; `--check` 0 and D04 leg C regeneration), `expected_exit` /
  `finding_ids` kept predeclared, a stamped revision, and — D09's recommendation — the green
  re-run performed by a different shard than the re-piner. This ledger carries the pre-refresh
  anchor (D09 S4 requests exactly that); the post-refresh `expected.json` sha256 must be
  recorded at admission.
- **D09 addendum (`20:53Z`)**: the counting command `reports/round-9/run-validation.py` /
  `validation.json` landed while the fragments were still being written; its D verdict is
  `passed: false` with the frozen leg as the sole D failure — the round's own counting command
  agrees that no green frozen leg exists at this revision.

## 4. This shard's independent receipts (raw)

All commands run from the lane repo root at HEAD `a7bb205`, `2026-10-17T20:47–20:52Z`;
scratch under `$HOME/.cache/scribe-r9-d3/` (outside the repo). Verbatim observations:

```text
$ python3 tools/assemble-culture-d3.py --check
packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly
exit=0

$ python3 tools/check-evidence-coupling.py --selftest        # exit 0
{"domain_controls": {"passed": 16, "total": 16},
 "frozen_checks": {"passed": 5, "total": 5},
 "malformed_controls": {"passed": 4, "total": 4},
 "positive_controls": {"passed": 5, "total": 5},
 "selftest_passed": true, ...}

$ python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json
{"counts": {"total": 0}, "exit": 0, "findings": []}
exit=0

$ python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
      --frozen examples/culture-d3/expected.json
{"counts": {"D3-SNAPSHOT": 3, "total": 3}, "exit": 2, "findings": [<the three in §3.2>]}
exit=2

$ TMPDIR=/var/tmp python3 tools/assemble-culture-d3.py --selftest
selftest: 85/85 checks passed — fixture CLI assemble/--check/determinism/tamper plus … controls; …
exit=0

$ python3 tools/replay-frozen.py --selftest
selftest: 79/79 checks passed
exit=0
```

Isolated mirror determinism (proof that the committed artifacts are the deterministic output
of the committed inputs, without touching the delivered tree):

```text
$ M="$HOME/.cache/scribe-r9-d3/mirror"; rm -rf …; mkdir -p "$M"
$ git archive HEAD | tar -x -C "$M"; cd "$M"
$ python3 tools/assemble-culture-d3.py --check        # exit 0, same byte-identical line
$ python3 tools/assemble-culture-d3.py >/dev/null     # build 1, exit 0
$ python3 tools/assemble-culture-d3.py >/dev/null     # build 2, exit 0
$ sha256sum examples/culture-d3/packet.json examples/culture-d3/packet.gates.yml   # both builds
bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829  examples/culture-d3/packet.json
306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  examples/culture-d3/packet.gates.yml
BUILD1==BUILD2 ; check after builds exit=0
```

The mirror digests equal the committed artifacts' digests (§2 table) and the manifest pins —
three independent routes to the same bytes (D02 in place, this shard in a `git archive`
mirror, `git hash-object` in D02 §4).

CLI negatives (in the mirror, so the delivered tree was untouched; every one exits 2 with a
stable diagnostic and no traceback):

| invocation | observed | exit |
|---|---|---|
| guard, no arguments | `CLI-ERROR D3-DATA usage: expected <packet.json> [--frozen <expected.json>]` | 2 |
| guard, `--bogus` | `CLI-ERROR D3-DATA usage: unknown option '--bogus'` | 2 |
| guard, invalid-JSON packet | `packet is not valid JSON: Expecting value: line 1 column 1 (char 0)` | 2 |
| assembler, component removed | `assembly error: missing component: examples/culture-d3/components/06-material.json` | 2 |
| assembler, component with extra top-level key | `assembly error: 05-ritual.json: top-level keys must be exactly ['beliefs', 'naming_rule', 'speech_rules', 'symbols']; missing=[] unexpected=['extra_key']` | 2 |

(The guard's own selftest additionally covers four malformed cases and two CLI-usage cases;
the assembler selftest covers missing/invalid-JSON/invalid-UTF8/wrong-root/unexpected-key/
missing-key/collision/wrong-type/below-minimum/serializer-absent controls — leg 2.) D05's
fragment is the full negative matrix (now landed): 29 negative cases + 3 controls —
**32/32 at the declared expectations across five battery runs, all negatives exit 2, no
tracebacks, no output writes, diagnostics byte-stable on repeat**, with the tool digest
unchanged before/after (`ba8d19d5…`, `cli-negatives.md` §"Delivered-tree baselines"); these
five probes are this shard's corroboration only.

## 5. Fragment roster and integration status

| shard | file | status at this stamp (`20:53Z`) |
|---|---|---|
| R9-D01 diagnosis | `check-diagnosis.md` | **landed**; read and tied in (§3) |
| R9-D02 determinism | `determinism.md` | **landed**; tied in (§2 leg 6) |
| R9-D03 evidence-coupling | `evidence-coupling.md` | **landed**; tied in (legs 3–4) — full selftest JSON, all 16 domain controls re-driven from two cwds, malformed 4/4, §3 records the same 3-entry drift as could-not-evaluate |
| R9-D04 frozen replay | `replay.md` | **landed**; tied in (legs 7, 10, 11) — tool selftest 79/79; proposed scratch D3 manifest replays 5/5 with C1–C4 tamper controls; committed freeze red (leg 5); refresh exercise exit 0 in scratch, **not committed** |
| R9-D05 CLI negatives | `cli-negatives.md` | **landed**; tied in (leg 8) — 29 negatives + 3 controls, all exit 2, no tracebacks, no writes, 5 battery runs, tool digest unchanged |
| R9-D06 interop | `interop.md` | **landed**; tied in (leg 9) — assigned legs green with stdout byte-identical to round-8 admitted values; one pre-existing red recorded outside round 9 (d2-typed-labels `--check`) |
| R9-D07 capability row | `capability-draft.md` | **landed (draft only)**; tied in (leg 14) — SCORECARD row + depth-row text + admission checklist; explicitly gated on the frozen re-pin |
| R9-D08 docs/regen | `docs.md` | **landed**; tied in (leg 11 context, §3.4, §6) — regeneration from components alone byte-identical; F1 freeze-invalidation blocking the frozen element, F2 contract digest stale in five doc rows, F3 selftest-green ≠ freeze-clear |
| R9-D09 circularity audit | `findings.md` | **landed**; tied in (leg 15, §3.4) — no fabricated/self-blessed green found; S1 minimum record for a legitimate re-pin; S2 selftest-blindness + proposal self-capture; S3 superset control matcher; S4 freeze self-pin gap; S5 `--selftest` envelope; S6 convention notes; §6 addendum checked the counting command |
| R9-D10 adversarial re-derivation | `findings-10.md` | **landed**; tied in (leg 12) — independent hand rebuild 62/63 checks; F1 36-byte prose divergence (informational); F2 frozen red independently confirmed, including pinned-gate differential |
| R9-D11 contract cross-check | `contract-crosscheck.md` | **landed**; tied in (leg 13) — 138/138 packet-side checks; F-1 = the same stale freeze; recommends refresh, never weakening the check |
| R9-D12 scribe | this file | landed |

Polling record: background pollers at 60 s cadence over `reports/round-9/d3/` from `20:48Z`
(read-only for this shard). D01/D02 landed at `20:49–20:50Z`, D03–D08 by `20:52Z`, D10 at
`20:52Z`, D09 at `20:53Z` (its addendum the same stamp), D11 at `20:54Z` — all twelve fragments
landed inside the 20-minute cap; no shard needed the missing-dependency extension. **Reconciliation duty:**
every landed verdict was checked against §2 as it arrived; none contradicts a row. D01, D03,
D04, D07, D08, D09, D10 and D11 independently converge on the same three-entry freeze drift and
the same disposition (refresh with record, never weaken); D09's audit found no false green. No
contradiction remains to preserve — the one residual disagreement-shaped item is the re-pin
decision itself, which is the orchestrator's (§3.4, §6).

## 6. Limits, `to-verify`

1. **Not green as a whole.** Legs 1–4, 6–13 and 15 are green; leg 5 is could-not-evaluate
   pending the committed re-pin decision; leg 14 is a gated draft (D07). The round's counting
   command landed at `20:53Z` and its verdict is `claims.D.passed: false`,
   `acceptance_checks_passed: false`, the sole D failure being the frozen leg — the claim as
   delivered does not pass, and this ledger does not claim otherwise. No admission, capability,
   canon or promotion is claimed by this ledger.
2. **`to-verify`:** the integration commit hash (all pins here are worktree/HEAD `a7bb205`
   values); the outcome of the re-pin decision (§3.4) and the post-refresh `expected.json`
   sha256; a re-run of `reports/round-9/run-validation.py` after any re-pin; the five stale doc
   rows (D08 F2); the test-only residuals D09 S3 (control matcher accepts supersets) and S5
   (`--selftest` outside the assembler's exit-2 envelope) — both are owners'/orchestrator's calls,
   neither blocks this ledger.
3. **Decision flagged, not absorbed** (out of this shard's province): re-authoring
   `examples/culture-d3/expected.json` is an orchestrator/cross-shard act (D01 §6 recipe; D04
   leg E scratch demonstration; D08 F1); the five stale documentation rows (D08 F2:
   `README.md:46-48,91,104`; `handoff.md:27,39,74,239-241,278`) need re-dating at the same
   time; SCORECARD admission is the orchestrator's, and D07 §2 instructs: do not land the
   capability row while the frozen run is red.
4. **Digest recording is frame-checking.** The pins above prove bytes and verdicts at named
   stamps, not that the gate repairs or the packet's content are correct or scholarly;
   round-8's audit/replay shards carry the broader repair claims, and this ledger cites them
   read-only.
5. **Environment:** `/tmp` inode exhaustion (§1) is an environment condition, not a repo
   defect; it is recorded because a re-runner of any tempfile-based leg needs `TMPDIR`
   redirected at this revision.

FILES: reports/round-9/d3/scribe.md | SUMMARY: D3 acceptance ledger, all 11 sibling fragments integrated — 13 of 15 legs green (byte-identical assembly; assembler selftest 85/85; guard selftest + live run clean; determinism 13 probes + isolated mirror; replay-tool 79/79; D05's 32-case CLI negatives; d2 interop byte-identical to round-8 admitted values; D04's proposed projection manifest 5/5; D08 docs/regen; D10 re-derivation 62/63; D11 contract 138/138; D09 circularity audit clean), 1 could-not-evaluate (committed freeze red-by-design at `3 × D3-SNAPSHOT` from round-8 `e1694ba` revisions; re-pin demonstrated in scratch only — claim-D frozen clause stands could-not-evaluate and any later green must satisfy D09 S1's record), 1 gated draft (D07 row); the round counting command landed `20:53Z` with `claims.D.passed: false` matching this ledger; orchestrator decisions (re-pin record, SCORECARD admission, doc re-dating) listed in §3.4 and §6.
