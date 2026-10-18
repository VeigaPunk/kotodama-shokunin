# R18-D25 — docs: gate documentation draft + doc-surface sweep (round 18)

- round: 18 (operator loop 2 of 3, build round 2 of 4) · seat **R18-D25**
  (docs) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D21..D28 (scribes+docs x8): frozen-manifest
  records; fragment ledger; capability drafts; ASSEMBLY.md/README updates for
  culture-d4 (new files only); docs; run logs; disposition drafts; spot-check
  ledger. reports/round-18/d4/scribe-{1..8}.md."
- date: 2026-10-18. Reference revision `c66ac3c`; readings 10:19–10:31Z.
- canon: NON-CANON. Draft text and a read-only sweep; nothing here is canon,
  a clearance, or a registry act. The parent lands docs.
- writes: **this file only** + `.scratch/r18d21/`. No SKILL.md, README.md,
  SCORECARD.md or corpus byte edited.

## 1. Doc-surface sweep (read-only, 10:29Z)

```sh
grep -rln "typed-pipeline-gate\|typed_pipeline_gate" SKILL.md README.md SCORECARD.md corpus/ examples/
# → SCORECARD.md; corpus/lessons/round-11.md; corpus/lessons/round-17.md;
#   corpus/lessons/round-18.md          (SKILL.md, README.md: no hits)
grep -rln "d4-typed-labels-check-gate\|d4-assembly-check-gate" . --exclude-dir=.git --exclude-dir=.scratch
# → the two gate files themselves (+ tool help text) at this stamp
```

| surface | mentions the typed-pipeline gate? | what it says today | owner of the update |
|---|---|---|---|
| `SKILL.md` §Gates and probes | **no** — the 12-row registry table lists the 7 legacy gates, `frozen-replay`, `uncertainty-inventory`, `D2 assembly drift`, `contrastive craft example`, `isolated legacy selftest battery` | silent on the typed-pipeline gate and on the two new D4 gates | parent (registry act; a new row is a new row, never an edit of a legacy row) |
| `README.md` | no | no gate enumeration | — |
| `SCORECARD.md:161` | yes — the round-17 depth row states the D2-bound rejection verbatim | correct for round 17, stale for round 18 | parent adds a round-18 row; the r17 row stays as the record of the rejection |
| `corpus/lessons/round-{11,17,18}.md` | yes | round-11 = the freeze record, round-17 = the rejection, round-18 = the opening census | lessons files are per-round records; round 18's entry is X01's and the parent appends |
| `examples/culture-d4/ASSEMBLY.md:66-75` | indirectly — the "Pending" block naming the D4 typed tools | stale (scribe-4 §1) | parent, via the scribe-4 draft |
| `tools/gates/frozen/round-11/README.md` | yes — the generation index | current | untouched; a round-18 generation gets its own index |

**Finding F-D25-1 (doc obligation, not a defect):** the two round-18 gates
live under `tools/gates/`, and `corpus/knowledge/verification/gate-frozen-run-standard.md`
§1 puts every registered gate in scope for the two-evidences clause
(selftest + frozen run), while §2 says a self-test never stands in for a
frozen run. Neither new gate has a registry row or a frozen row at this
stamp. Draft rows below.

## 2. Draft — registry rows for the two new gates (paste into `SKILL.md` §Gates; parent owns placement)

```markdown
| d4-typed-labels-check-gate | gate | `python3 tools/gates/d4-typed-labels-check-gate.py [PROJECTION]` | 0 projection is the peer's deterministic build / 1 drift / 2 could-not-evaluate | — (delegates: `tools/d2-typed-labels.py --check`) | the peer's exit/stdout forwarded unchanged; input path passed verbatim so the recorded line is replay-stable | read-only (peer invoked with `--check`) | kotodama-shokunin |
| d4-assembly-check-gate | gate | `python3 tools/gates/d4-assembly-check-gate.py [PACKET]` | 0 packet is the assembler's deterministic build / 1 drift / 2 could-not-evaluate | — (delegates: `tools/assemble-culture-d4.py --check`) | same forwarding contract | read-only (peer invoked with `--check`) | kotodama-shokunin |
```

Owes, per the frozen-run standard: one frozen row each (pinned gate digest,
pinned input copy, committed expected verdict + `output_sha256`). Until then a
reader must treat them as `UNKNOWN` for the conformance claim, exactly as §1
of that standard states — a thin wrapper improves replayability, it does not
by itself satisfy the two-evidences clause.

## 3. Draft — documentation block for the generalized typed-pipeline gate

To be placed wherever the parent documents tools (a new
`reports/round-18/gate/README.md`, a round-18 SCORECARD addendum, or a
`examples/culture-d2/ASSEMBLY.md` successor — **not** an edit of a filed
round-8..17 byte):

```markdown
### typed-pipeline-gate — declared-assembler pin (round 18)

    python3 tools/gates/typed-pipeline-gate.py [PACKET]      # D2 default, byte-identical
    python3 tools/gates/typed-pipeline-gate.py --assembler <pin> [PACKET]
    python3 tools/gates/typed-pipeline-gate.py --json | --selftest

Legs: L1 build (assembler identity, projector run, adapter build in a temp
mirror), L2 channel, L3 holds (emitted set == expected set keyed
(id, severity, where), counts and details pinned), L4 pins.

Exit codes: 0 = all legs pass (the emitted findings equal the expected set —
NOT a clearance; every hold line is printed verbatim); 1 = a leg mismatched;
2 = could-not-evaluate (stale pin, malformed packet, gate traceback, mirror
hazard).

The assembler-identity leg reads the **declared** assembler pin: the packet's
own `assembly` block when it names one, or the `--assembler` flag; the
default remains `tools/assemble-d2.py` over `examples/culture-d2/packet.d2.yml`,
byte-identical in behaviour to the round-11 revision. A D4 packet is refused
by the default path with exit 2 and
`packet bytes are not assemble-d2.py's deterministic assembly` — the round-17
boundary — and is graded through the declared leg instead.

Expected-set file: `examples/culture-d2/expected-holds.json` (D2) /
`examples/culture-d4/expected-holds.json` (D4, landed round 18, 15 holds +
1 note + 0 fails). A hold laundered into a note, deleted or renamed fails L3.
```

## 4. Doc-drift items the parent must not inherit silently

1. `SCORECARD.md:161` (round-17 depth row) states the gate "structurally
   cannot consume a D4 packet". After the generalization lands, that sentence
   is history, not current behavior: add the round-18 row rather than editing
   the round-17 one.
2. `examples/culture-d4/ASSEMBLY.md` §1/§3/§4/§5/§6 predate the landed
   `expected-holds.json`, the eras normalization (naming verdict 8 → 14) and
   the new pins (scribe-4 drafts the correction).
3. `tools/gates/frozen/round-11/README.md` and `MANIFEST.tsv` row 1 describe
   the pre-round-18 gate; a re-pin is a new generation (§scribe-1 §3).
4. Round-17's frozen record's live-path receipts are stale vs live bytes
   (packet `2776d85c…` → `e7ecd204…`); its replay stays green because it
   pins a snapshot copy (scribe-1 §4).
5. The `--help` text of the pre-generalization gate documents only
   `[--json] [--selftest] [packet]`; the after-state must document the declared
   pin in the same place, or the flag exists without a discoverable contract.

## 5. Limits

- Drafts only; no registry, SCORECARD, SKILL, README or corpus byte touched.
- The flag spelling in §3 (`--assembler <pin>`) is a documentation
  placeholder for whatever the O family lands ("packet-declared or flag",
  `reports/round-18/claims.json:14`); the parent must reconcile the wording
  with the delivered CLI before landing the block.

## 6. Post-state note on the doc draft (10:36Z)

The live gate still exposes `[-h] [--json] [--selftest] [packet]` — verified by
`--help` at 10:32Z and again at 10:36Z on the generalized revision (scribe-6
rows 2, 36) — so §3's flag placeholder stands: the delivered interface is
**packet-declared** at this stamp, and the doc block must not promise a flag
that does not exist. If the O family later adds `--assembler`/`--projection`/
`--expected` (the round-18 runner probes for all three), the §3 block is
already shaped for them and needs only the flag list confirmed.

Also updated by the wave: the registry rows in §2 are still owed (no
`SKILL.md` §Gates row for either new gate), a round-18 frozen generation now
exists (`tools/gates/frozen/round-18-repin/`) and its index/README is the
natural home for the new gates' two-evidences status, and `SCORECARD.md` gained
no round-18 row at this stamp (`grep -c "round-18" SCORECARD.md` → 0 as of
10:26Z per the X01 census; parent integrates).
