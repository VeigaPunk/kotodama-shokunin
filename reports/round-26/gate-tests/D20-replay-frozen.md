# R26-D20 — replay-frozen: the round-26 re-pin reproduces; the superseded tails named

- **Seat:** R26-D20 (gate+tests 4 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum`; supporting evidence for claim **O** (the pin tails).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **Write scope:** `tools/gates/frozen/round-26/{gate-input,post-register}/**`
  (**new** generations), `reports/round-26/gate-tests/freeze.py`, this fragment,
  and gitignored scratch. **No byte of `tools/gates/frozen/round-25/**` or any
  earlier generation was edited; no commit, no push.**
- **Canon:** NON-CANON. A reproduced red verdict stays red; a re-pin is a new
  recording, never an in-place edit (`tools/gates/frozen/round-18/README.md`).

## 0. Verdict

**Two round-26 generations were frozen this round; the newer one replays 6/6
with zero mismatch and zero could-not-evaluate.** The first was taken before the
register stratum landed; the landing moved the D4 packet, so — following the
lane's rule that a re-freeze is a new recording — the second generation was
frozen beside it and the first is classified with the superseded tails.

```
TMPDIR=/var/tmp python3 tools/replay-frozen.py \
  tools/gates/frozen/round-26/post-register/MANIFEST.tsv
→ REPLAY OK: 6/6 rows reproduced the recorded verdicts
```

## 1. Why a new generation was needed — the stale pin, measured

### 1.1 The round-25 pin (the O claim's sibling tail)

`tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` pins
`tools/gates/typed-pipeline-gate.py` at
`879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`. The live
gate is `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85`
(`sha256sum`, 2026-10-18) — and the committed blob at `fc13cd2` **and** at HEAD
is the same `b749ad07…`. So the round-25 pin was taken mid-wave on an
uncommitted gate revision, and the round-25 close commit swept a later revision
in. Every one of its six rows refuses before a gate runs:

```
ROW 2 could-not-evaluate reason=gate_digest_mismatch gate=tools/gates/typed-pipeline-gate.py
  detail: gate: on-disk bytes are not the pinned revision: tools/gates/typed-pipeline-gate.py
  ... rows 2-7 all read gate_digest_mismatch (6 could-not-evaluate, 0 mismatch, 0 reproduced)
```

This is the **same class** the round-25 scribe named for the sibling generations
(`reports/round-25/scribe/frozen-rows.md` §2-§3): a filed row pins the gate
*bytes*, so a later gate revision supersedes its row rather than reproducing it.
It is one of the two "sibling pin tails" the round-26 O claim chases; this seat
supplies the re-pin evidence for the typed-pipeline surface.

### 1.2 The first round-26 generation (`gate-input`)

Frozen at 18:08Z against packet `e7ecd204…`. The register stratum landed at
18:19:48Z (packet → `dd25077b…`), which moved the D4 inputs, so its two D4 rows
now read `replay_mismatch` with a **moved input** — a supersession, not drift
(§3). It is kept as filed; the successor is the `post-register` generation.

## 2. The current round-26 generation (`post-register`)

`tools/gates/frozen/round-26/post-register/` — 6 rows, the same schema and the
same four input-class rows as the round-25 predecessor, plus its two fail-closed
controls. `freeze-receipt.json` records the pins and the verdicts; every input
is a byte copy under `inputs/`.

| row | input | recorded verdict |
|---|---:|---|
| 1 | `examples/culture-d4/packet.d4.yml` | exit 0, 12 findings |
| 2 | `examples/culture-d4/packet.d4.typed.yml` | exit 0, 12 findings |
| 3 | `examples/culture-d2/packet.d2.yml` | exit 0, 15 findings |
| 4 | `examples/culture-d2/packet.d2.typed.yml` | exit 0, 15 findings |
| 5 | control: typed packet, declared source absent | exit **2** |
| 6 | control: typed packet, `packet_sha256` stale | exit **2** |

Replay (2026-10-18T18:22Z): **6/6 reproduced, 0 mismatch, 0
could-not-evaluate, exit 0.** The two controls record exit 2 with 0 findings —
the input-class refusal, never a verdict, which is the round-25 gate-input fix
holding.

The generator is `reports/round-26/gate-tests/freeze.py`:

```
python3 reports/round-26/gate-tests/freeze.py --generation post-register          # build
python3 reports/round-26/gate-tests/freeze.py --generation post-register --check  # replay
```

## 3. Every generation replayed, with its class named

The battery replays all eleven `MANIFEST.tsv` generations on every run
(2026-10-18, `TMPDIR` outside the repo). The split is principled, so no row is
hand-waved:

| generation | rows | replay | class |
|---|---:|---|---|
| `round-26/post-register` | 6 | **OK 6/6** | **current** |
| `round-26/gate-input` | 6 | mismatch 2 (input moved) | superseded by the register landing |
| `round-25/gate-input` | 6 | could-not-evaluate 6 | `gate_digest_mismatch` (stale pin, §1.1) |
| `round-23/repin-d2` | 11 | could-not-evaluate 1, reproduced 10 | superseded gate row |
| `round-22/d4-repin` | 3 | mismatch 2 (input moved) + 1 gate | superseded by the register landing |
| `round-20/repin-d2` | 11 | could-not-evaluate 1, reproduced 10 | superseded gate row |
| `round-18/repin-d2` | 11 | could-not-evaluate 1, reproduced 10 | superseded gate row |
| `round-18` | 2 | mismatch 2 (inputs moved), 0 reproduced | superseded projection pin (§3.1) |
| `round-11` | 11 | could-not-evaluate 1, reproduced 10 | superseded gate row |
| `round-3` | 7 | could-not-evaluate 7 | superseded gate bytes |
| `round-3/attempt-1` | 7 | could-not-evaluate 7 | superseded gate bytes |

### 3.1 The classification rule

- **`could-not-evaluate` / `gate_digest_mismatch`** — the gate bytes moved after
  the freeze; the documented cascade (a re-pin is a new generation, never an
  in-place edit).
- **`replay_mismatch` with a moved input** — the row's live input no longer
  hashes to its own `input_sha256`, i.e. a later generation superseded it. The
  round-18 projection pin superseded by the round-22 family-clean build
  (`reports/round-25/scribe/frozen-rows.md` §3) and the round-26 `gate-input`
  rows superseded by the register landing are both this class. Recorded.
- **`replay_mismatch` with the input unmoved** — the pinned input still hashes
  to its pin yet the gate's output differs. Nothing superseded it; that is
  genuine drift and a new finding. **Zero such rows at this stamp.**

## 4. Limits

- **Replay asserts reproduction, not correctness.** A reproduced `exit_code=2`
  row is still a refusal; a reproduced 12-finding row is still twelve open
  holds.
- **The generation binds to today's bytes.** A later edit to the gate, the
  packets or the controls supersedes these rows and requires a new generation —
  which is exactly what happened within this round (§1.2).
- **`TMPDIR` must sit outside the repository** for the replay, or every row
  reads `mirror_unsafe` (measured: the round-25 scribe recorded the same
  constraint). The battery sets it explicitly and checks the root is outside.
- **This seat does not edit any filed row.** The round-25 generation and the
  first round-26 generation stay as filed; the disposition of those tails is the
  parent's.
