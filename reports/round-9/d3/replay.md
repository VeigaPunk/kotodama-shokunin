# R9-D04 — frozen replay of the D3 artifacts (tools/replay-frozen.py)

- round: 9 (loop 1 of 3, build round 2 of 4) · shard: D04 (depth / replay) · date: **2026-10-17**, stamps UTC unless marked (local = UTC-3; every command below was run on the revision named next)
- baseline revision: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (`reports/round-9/claims.json:6`); measurement tree = that revision plus the untracked round-9 worker output present at each stamp
- owns: **this file only**. No tool, packet, component, freeze, gate, manifest or LOG edit is made by this shard inside the repository. Every scratch tree lives outside the repo (`/home/vgpnk/r9d04-scratch/`), and the receipts quoted here are retained there.
- tested objects: `python3 tools/replay-frozen.py` (`a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464`), the committed D3 freeze `examples/culture-d3/expected.json` (`74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080`), the D3 artifacts (`examples/culture-d3/packet.json` `bdf635ce…`, `packet.gates.yml` `306bcac7…`, components, `controls.json`, `handoff.md`), `tools/assemble-culture-d3.py` (`ba8d19d5…`) and `tools/check-evidence-coupling.py` (`849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e`).
- requirement tested (assignment R9-D04 / claim D `after_required`, `reports/round-9/claims.json`): "D3 replays frozen without digest drift"; record it.

## 0. Verdict — read this first

| leg | command | observed | status |
|---|---|---|---|
| A tool selftest | `python3 tools/replay-frozen.py --selftest` | `selftest: 79/79 checks passed`, exit 0 (20:49Z) | **PASS** |
| B **D3 projection frozen manifest** (proposed, scratch) | `python3 tools/replay-frozen.py <proposal>/MANIFEST.tsv --repo-root <d3root>` | `REPLAY OK: 5/5 rows reproduced`, exit 0 (20:50Z) | **PASS** (reproduction only: all five rows are recorded *red* holds and stay red) |
| B controls C1–C4 (tamper) | snapshot / gate / output tamper, live-input drift | exit 2 `snapshot_tampered` 5/5, `gate_digest_mismatch` 1/5, `expected_output_tampered` 1/5 (no gate launched in any could-not-evaluate row); live-input drift does not move the replay | **PASS** |
| C post-regeneration, isolated copy of the delivered tree | `python3 tools/assemble-culture-d3.py` in `/home/vgpnk/r9d04-scratch/iso` | regenerated `packet.json` 37222 B `bdf635ce…`, `packet.gates.yml` 14191 B `306bcac7…` — **byte-equal to the lane bytes and to every pin**; `--check` exit 0 | **PASS — no digest drift after regeneration** |
| D **committed D3 freeze** (the in-repo surface) | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | **exit 2**, 3 × `D3-SNAPSHOT` digest mismatch; 21/24 manifest entries match (20:49Z; reproduced identically in the isolated copy, 20:50Z) | **RED — see §4; this is the round's D3 replay blocker unless the parent re-freezes with documentation** |
| E refresh exercise (scratch) | same guard, `--frozen /home/vgpnk/r9d04-scratch/expected-refresh.json` (exactly 3 digest lines updated) | exit 0, `findings: []`; tampered twin → exit 2 `D3-SNAPSHOT`; half-frozen tree (packet edited) still caught → exit 2 | **PASS as a demonstrated remediation path, not committed** |
| F regression baselines | round-3 + attempt-1 manifests (`tools/gates/frozen/round-3/…`), round-4 dir, `handoff-packet-check/r9-pre` pin | round-3 7/7 `gate_digest_mismatch` exit 2; attempt-1 same; round-4 has **no** `MANIFEST.tsv` → exit 2 `manifest_unreadable`; `handoff.md` still equals its r9-pre pin | recorded (fail-closed; round-8 gate repairs drifted those pins) |

The D3 artifacts themselves are replay-stable: they have not changed since the round-7 checkpoint (`git log --oneline -1 -- examples/culture-d3/packet.json …` → `57c3ce6` for every D3 artifact), regeneration reproduces them byte-for-byte, and a frozen manifest built over the D3 legacy projection replays 5/5. The only red is the **committed** freeze, whose 3 drifted pins name files that round 8 changed (`e1694ba`), not D3 work.

## 1. What "frozen replay" surfaces exist for D3 (sweep)

```
find tools/gates/frozen -name 'MANIFEST*.tsv' -o -name 'expected.json' | sort      # 2026-10-17T20:51Z
  tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv
  tools/gates/frozen/round-3/MANIFEST.tsv
  tools/gates/frozen/handoff-packet-check/r9-pre/expected.json     (round-9 O-baseline shard)
grep -rl "culture-d3" tools/gates/frozen/                         # → (none)
grep -rln "replay-frozen" tools/                                  # → tools/replay-frozen.py only
```

So: **no committed frozen manifest covers any D3 artifact** (both round-3 manifests replay the D2 packet rows), and the only in-repo freeze that names D3 bytes is `examples/culture-d3/expected.json` — the guard's snapshot manifest, plus the O-shard's r9-pre handoff pin. Legs B–E below cover all three.

Tool facts used: `replay-frozen.py` verifies `gate_sha256`, the snapshot's `input_sha256` and the recorded output's `output_sha256` **before** launching, then runs `[python3, <pinned gate>, <input>]` inside a temp mirror holding a verified copy of the pinned snapshot, comparing exit code, `^FINDING ` count and output bytes (`tools/replay-frozen.py:166-290`); exit 0 reproduces, 1 mismatches, 2 could-not-evaluate. The live input path is validated for safety but **never opened**.

## 2. Leg B — a frozen manifest over the D3 legacy projection (proposed, scratch)

The D3 legacy projection is a packet the existing gates read directly (command: `for g in phonology-sanity-gate lexicon-coverage-audit myth-consistency-gate costume-era-consistency-gate naming-collision-gate; do python3 tools/gates/$g.py examples/culture-d3/packet.gates.yml; done`, 20:49Z → exit 1 with 2/47/3/1/3 findings; `provenance-audit.py` exits 2 — it does not accept this input, so it is not a row).

Proposal built by `/home/vgpnk/r9d04-scratch/build-d3-manifest.py` into `/home/vgpnk/r9d04-scratch/d3root/tools/gates/frozen/round-9-d3-proposal/` (MANIFEST.tsv `70affb9d7820bd74704258fd37428be6ce600d377b979c5d2c580a1803adb187`): five rows, each recording the gate revision, the pinned projection (`input_sha256 306bcac7…`), the observed exit/finding count and the exact output bytes, produced the same way the replay reproduces them (mirror cwd, relative argv).

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
TMPDIR=/home/vgpnk/r9d04-scratch/tmp python3 tools/replay-frozen.py \
  /home/vgpnk/r9d04-scratch/d3root/tools/gates/frozen/round-9-d3-proposal/MANIFEST.tsv \
  --repo-root /home/vgpnk/r9d04-scratch/d3root
# REPLAY OK: 5/5 rows reproduced the recorded verdicts (reproduction only: a reproduced red verdict stays red)
# exit 0 — every row exit=1, counts 2/47/3/1/3, bytes=match, launched=yes   (receipts/replay-proposal.json)
```

Two of the five rows are the holds documented in `examples/culture-d3/README.md:88-93` — legacy naming CROSS-HOLD ×2 + NAME-NEAR ×1, and costume R-01 (C03's declared RR1 violation kept visible). The other three are the projection's own observed packet-level findings, recorded here for the first time in the round: phonology `G-DATA` ×2 (`phonology.notable_rules` / `phonology.tones` missing — REVIEW, check could not evaluate), lexicon `C-entry-unevaluable` ×47 (legacy D2 lexicon fields absent from the projection's 20 entries), myth `MC-P00`/`MC-M00`/`MC-S00` (legacy role/motif/symbol ledgers absent). They are receipts, not endorsements: each is the recorded byte output in `<gate>.out` beside the manifest. A replayed red stays red — the replay asserts reproduction, not design cleanliness.

**Controls (isolated copies of the proposal root; each is one mutation):**

| case | mutation | observed |
|---|---|---|
| C1 | one newline appended to the pinned snapshot | `{'reproduced': 0, 'could_not_evaluate': 5, 'exit': 2}`, sole reason `snapshot_tampered`, **no gate launched** |
| C2 | `# drift` appended to `tools/gates/naming-collision-gate.py` | `{'reproduced': 4, 'could_not_evaluate': 1, 'exit': 2}`, reason `gate_digest_mismatch` |
| C3 | `FINDING X-9 injected` appended to the costume row's `.out` | `{'reproduced': 4, 'could_not_evaluate': 1, 'exit': 2}`, reason `expected_output_tampered` |
| C4 | live input mutated (`examples/culture-d3/packet.gates.yml` under the proposal root, digest `f2dcacdd…` ≠ pin) | `{'reproduced': 5, 'exit': 0}` — and the receipt is **byte-identical** to the clean run (`f69b7127…` both): the replay never reads the live input |

Receipts: `receipts/replay-c1.json`, `replay-c2.json`, `replay-c3.json`, `replay-c4-live-drift.json`. These are the same fail-closed classes the tool's own `--selftest` proves on fixtures (leg A, 79/79, including `snapshot-tampered`, `gate-digest-mismatch`, `output-tampered`, `record-inconsistent` and the path-safety refusals).

**Proposal status: not committed and not a re-blessing.** The manifest is a scratch artifact offered to the parent; adopting it into the repo (a generation directory of the parent's choosing) is an integration decision, not this shard's.

## 3. Leg C — no digest drift after regeneration

The D3 packet was regenerated in an isolated **full copy** of the delivered tree (`rsync -a --exclude .git ./ /home/vgpnk/r9d04-scratch/iso/`, 20:50Z). The lane tree was deliberately not regenerated: R9-D01/D02 own that work and a lane regeneration would mutate the very bytes the freeze pins.

```sh
cd /home/vgpnk/r9d04-scratch/iso
python3 tools/assemble-culture-d3.py         # exit 0: Wrote packet.json (37222 bytes); Wrote packet.gates.yml (14191 bytes)
python3 tools/assemble-culture-d3.py --check # exit 0: packet.json: byte-identical …; packet.gates.yml: byte-identical …
sha256sum examples/culture-d3/packet.json examples/culture-d3/packet.gates.yml
# bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829  packet.json
# 306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  packet.gates.yml
```

Both digests equal the lane's committed bytes **and** the round-7 recorded digests (`examples/culture-d3/handoff.md:58` A-PACKET `bdf635ce…`; A-GATES `306bcac7…`). Chain: lane bytes = regenerated bytes = pin. The proposal manifest's snapshot is the same `306bcac7…`, so Leg B's 5/5 replay holds over the regenerated artifact too. Receipt: `receipts/iso-regen-and-guard-committed.txt`.

## 4. Leg D — the committed D3 freeze is RED (3 of 24 pins drifted)

```sh
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json   # exit 2
python3 - <<'EOF'   # per-entry digest audit, 20:49Z → 24 entries, 21 match, 3 mismatch
EOF
```

| manifest key | declared (round-7 freeze) | actual (today) | last changed by |
|---|---|---|---|
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `50c4c2f25a72…` | `5f4c02bfc4e6…` | `e1694ba` "round-8: admit F/O/D …" (`git show --stat e1694ba -- <file>` → 3 insertions) |
| `tools/gates/costume-era-consistency-gate.py` | `29a9361c7b96…` | `e6bffd7020c0…` | `e1694ba` (73 lines changed) |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a5abc…` | `d9e4e8f4f93a…` | `e1694ba` (236 lines changed) |

- The guard's own hash is unchanged since the freeze (`849494b0…` = `examples/culture-d3/handoff.md:67` A-TOOL-GUARD), as are all 21 remaining entries — including `packet.json`, `packet.gates.yml`, all four components, `controls.json`, both new tools, the round-6 ledger files and the reconciliation. Commit `57c3ce6` is the last commit touching any D3 artifact, so **the drift is entirely in three inputs that round 8 edited after the freeze**.
- The same 3 findings reproduce in the isolated copy (receipt `receipts/iso-regen-and-guard-committed.txt`), so the red is a property of the *pins*, not of the delivered tree.
- Consequently "D3 replays frozen without digest drift" is **not true of the committed surface at this revision**. Per the freeze's own limit text ("later input edits invalidate this snapshot before verdict") and round-7's `I08` integration note ("All future pinned-input edits must fail snapshot verification or receive a documented reverified freeze refresh"), the freeze is doing exactly its job; the round must either refresh it with a recorded re-verification or carry the red.

## 5. Leg E — the refresh path, exercised in scratch (not committed)

`/home/vgpnk/r9d04-scratch/expected-refresh.json` (`083ca2b1f3aae43b27b7da947bddd5f95f5780d04f110d0b0551266b93c44f04`) is the committed `expected.json` with **exactly three digest lines** replaced (text-level substitution; `diff` against the committed file shows 3 changed lines, all of them the digest values above) and nothing else — same 24 keys, same `expected_exit: 0`, same empty `finding_ids`.

| probe | result |
|---|---|
| `check-evidence-coupling.py examples/culture-d3/packet.json --frozen …/expected-refresh.json` (lane tree) | exit 0, `counts {'total': 0}`, `findings []` |
| same file in the isolated tree **after** regeneration | exit 0, `findings []` |
| twin with the `packet.json` entry set to `000…0` (declared tamper) | exit 2, 1 × `D3-SNAPSHOT` |
| isolated tree with one byte appended to `packet.json` (a post-freeze input edit) | exit 2, 1 × `D3-SNAPSHOT` ('manifest digest mismatch for examples/culture-d3/packet.json') |

Receipts: `receipts/guard-refresh-lane.json`, `guard-refresh-iso-postregen.json`, `guard-refresh-tampered-lane.json`, `guard-refresh-iso-packetedit.json`. Digest-first ordering holds: every rejection happens before any verdict, and the refresh is *only* the three drifted values — no diagnostic, threshold or expectation was weakened, and no packet was regenerated to make a red pass.

## 6. Leg F — regression baselines and the handoff pin

| leg | command | result |
|---|---|---|
| round-3 manifest, live tree | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` (20:50Z) | exit 2, **7/7 `gate_digest_mismatch`** ("gate: on-disk bytes are not the pinned revision"); manifest digest unchanged since round 8 (`d5337590…`) |
| round-3 attempt-1 | same with `attempt-1/MANIFEST.tsv` | exit 2, 7/7 `gate_digest_mismatch` (manifest `613e5945…`); receipt `receipts/replay-r3-attempt1-live.json` |
| round-4 generation dir | `…round-4/MANIFEST.tsv` | exit 2 `manifest_unreadable` — that directory holds only `.out` files; an honest fail-closed receipt, not a silent skip |
| handoff pin (O shard, `r9-pre`) | `sha256sum examples/culture-d3/handoff.md tools/gates/frozen/handoff-packet-check/r9-pre/packet.md` | both `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc` — the handoff artifact has not drifted since the O shard froze it (20:51Z) |

The round-3 red is the round-8 gate-repair drift already disclosed in `reports/round-8/depth/test-replay.md` (§3, §6): pins naming pre-repair gate bytes cannot be re-blessed in place. Nothing in round 9 has re-pinned them, and this shard does not.

## 7. What this means for the round (parent decision, not mine)

1. **D3 artifacts: no drift.** Regeneration is byte-identical, a projection-level frozen manifest replays 5/5 with all tamper classes fail-closed, and the handoff artifact still matches its r9-pre pin. The replay leg of the D3 acceptance is satisfiable.
2. **The committed freeze must be refreshed or the red carried.** `examples/culture-d3/expected.json` predates three round-8 edits. A minimal, auditable refresh is the 3-line file in §5; the parent should perform it (or delegate to a fresh same-identity shard) with the re-verification recorded, never by editing the round-7 record in place silently.
3. **If the parent wants a committed D3 frozen manifest**, §2's proposal is ready to adopt as-is; it pins live (post-round-8) gate revisions, which round 9's O claim says will not change behavior — any later gate edit would fail these pins closed rather than silently pass.
4. **Not claimed:** the projection proposal is not committed; the refresh is not committed; no canon, no lore receipt, no authenticity certification, and no independent re-run of another shard's work is asserted here.
5. **Corroboration by sibling shards (landed while this one ran, read 20:51Z after my own measurements).** `reports/round-9/d3/check-diagnosis.md:20-46,73-75` and `reports/round-9/d3/evidence-coupling.md:309-343` independently record the same guard exit 2 with the same three digest pairs and the same `e1694ba` attribution, and `reports/round-9/d3/determinism.md:55-56` the same regenerated digests `bdf635ce…`/`306bcac7…`; `check-diagnosis.md:171-176` reaches the same refresh recipe. My legs are additive (the `replay-frozen.py` projection manifest, its tamper controls, the live-input-drift control and the handoff-pin cross-check) rather than duplicate; the agreement is independent re-measurement, not shared input.

## 8. Re-run recipe

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/home/vgpnk/r9d04-scratch/tmp          # the shared /tmp is full under the 64-worker fleet
python3 tools/replay-frozen.py --selftest                                   # 79/79, exit 0
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv      # exit 2 (round-8 gate drift)
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
  --frozen examples/culture-d3/expected.json                                # exit 2, 3 D3-SNAPSHOT
python3 tools/replay-frozen.py \
  /home/vgpnk/r9d04-scratch/d3root/tools/gates/frozen/round-9-d3-proposal/MANIFEST.tsv \
  --repo-root /home/vgpnk/r9d04-scratch/d3root                              # exit 0, 5/5
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
  --frozen /home/vgpnk/r9d04-scratch/expected-refresh.json                   # exit 0, findings []
```

## 9. Limits and environment

- Scratch is outside the repo by design (`/home/vgpnk/r9d04-scratch/`: `iso/` full tree copy, `d3root`, `d3root-c1..c3`, `receipts/`, `expected-refresh*.json`, `build-d3-manifest.py`), so no pin, gate, packet or freeze byte in the lane was touched — `git status --porcelain examples/culture-d3/` is empty at every measurement. Receipts are retained for the parent; deleting them later removes the corroborating bytes, not the digests quoted above.
- The shared 16G `/tmp` was full at the start of this shard (`/tmp/r9d04-r3-live.json: No space left on device`, 20:49Z); all replay runs therefore used `TMPDIR` under home. This is environmental, not a tool defect — but note the known round-8 observation that an uncreatable mirror exits 1 with a traceback rather than 2 (`reports/round-8/depth/test-replay.md` §8); it did not occur here.
- The tree was not frozen for this shard: the O-baseline and freshness shards were landing files concurrently (`tools/gates/expected/`, `tools/gates/frozen/handoff-packet-check/`, `reports/round-9/baselines/`, `reports/round-9/freshness/`). Every digest quoted above is a stamp-specific measurement; a re-runner must compare pins, never remembered live values.
- Coverage of my own negative claims: "no committed manifest covers D3" — `grep -rl "culture-d3" tools/gates/frozen/` → none (20:51Z); "no other consumer of the tool" — `grep -rln "replay-frozen" tools/` → the tool only (20:51Z); "D3 artifacts unchanged since round 7" — `git log --oneline -1 -- <each artifact>` → `57c3ce6` for all seven paths, and 21/24 freeze entries byte-match their round-7 declared digests (20:49Z).

FILES: reports/round-9/d3/replay.md
SUMMARY: D3 replay shard green on tool (79/79), a proposed projection manifest (5/5) with all tamper classes fail-closed, and byte-identical post-regeneration; the committed freeze `examples/culture-d3/expected.json` is RED with 3 drifted pins (`worldbible-integration-contract.md`, `costume-era-consistency-gate.py`, `naming-collision-gate.py`, all last changed by round-8 `e1694ba`; 21/24 match, guard hash unchanged), and a scratch 3-line refresh restores exit 0 — parent must refresh with documented re-verification or carry the red.
