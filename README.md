# kotodama-shokunin — 言霊

**Word-spirit.** A culture's language is not decoration on its world;
it is evidence of it. Myth shapes vocabulary, era shapes register,
costume carries a lexicon, and symbols fossilize into words.

This is a [shokunin](https://github.com/VeigaPunk/shokunin) lane for
linguistic-cultural worldbuilding: conlang design and diachronic
staging; mythic and symbolic systems; era / period models; costume and
material-culture terminology; naming systems. Rank: shonen.

Kotodama *generates* systems and hands them off. It never records
canon. Canon — entities, relations, timeline, consistency — belongs to
lore-shokunin
([shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible)).
The handoff format is
`corpus/knowledge/synthesis/worldbible-integration-contract.md`.

Sibling repositories, the world bible, and domain source trees are
**read-only**. This lane writes only this repository.

## Province

**Owns:** the generative / coupling craft and its records under
`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis}`;
this lane's own gates and reports.

**Refuses:** claiming or recording canon (→ lore); real-world rights /
attribution rulings on reference works; game mechanics (game-dev-2d /
3d); general source-research method (chousa); web publishing (kake);
prompt / skill craft (kotoba). Contested scope → report to the
integrator, never absorb.

Full boundary: [`PROVINCE.md`](PROVINCE.md).

## Start here

1. [`SKILL.md`](SKILL.md) — coupling premise and decision table.
2. [`PROVINCE.md`](PROVINCE.md) — owns / refuses / handoff contract.
3. [`tools/gates/`](tools/gates/) — executable sanity over culture packets.
4. [`examples/`](examples/) — worked packets, when present.

## Gates

Each gate prints `FINDING <id>: …` or stays silent. Exit `0` clean,
`1` findings, `2` could-not-evaluate.

```
python3 tools/gates/phonology-sanity-gate.py --selftest
python3 tools/gates/naming-collision-gate.py --selftest
python3 tools/gates/myth-consistency-gate.py --selftest
python3 tools/gates/costume-era-consistency-gate.py --selftest
python3 tools/gates/lexicon-coverage-audit.py --selftest
python3 tools/gates/provenance-audit.py --selftest
python3 tools/gates/handoff-packet-check.py --selftest
```

A clean phonology packet is not a finished language. A clean handoff
packet is not canon — lore still has to admit it. `tools/assemble-d2.py`
is the assembler used when a swarm's disk inventory is the truth
source; see `LOG.md` for the last assembly.

## What's in the repo

```
kotodama-shokunin/
├── SKILL.md          coupling craft
├── PROVINCE.md       domain + lore handoff
├── SHONEN.md         promotion checklist
├── MINT.md           why this lane was minted
├── LOG.md            append-only audit trail
├── SCORECARD.md      axis verdicts
├── AGENTS.md         operating rules
├── examples/         worked packets
├── tools/
│   ├── assemble-d2.py
│   └── gates/        phonology, naming, myth, costume, lexicon, provenance, handoff
└── corpus/           knowledge/{linguistics,myth-symbol,culture-material,synthesis}
```

Protocol: append-only corpus; claims you cannot verify are marked
`to-verify`; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme) for how a lane
learns.
