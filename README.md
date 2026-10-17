# kotodama-shokunin — 言霊

**Linguistic-cultural worldbuilding.** The coupling of word and
world-spirit: conlang design, myth and symbol, era staging, costume and
material-culture lexicon, naming systems — generated here, recorded
elsewhere.

A culture's language is not decoration on its world. It is evidence of
it. Myth shapes vocabulary, era shapes register, costume carries a
lexicon, and symbols fossilize into words.

A **shokunin lane**: an expert agent for one domain, minted and trained
under the [shokunin skill](https://github.com/VeigaPunk/shokunin).
Rank: **shonen**. Promotion is a named non-author review of
[`SHONEN.md`](SHONEN.md), never self-attestation.

This lane answers: *does this culture's language, myth, era, and dress
actually couple — and can the resulting system be handed to the world
bible without this lane claiming canon?*

## Domain

From [`PROVINCE.md`](PROVINCE.md): the generative/coupling craft and its
records in `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis}`.

**Canon is not this lane's.** [lore-shokunin](https://github.com/VeigaPunk/shokunin-world-bible)
owns the world bible and consistency verification. kotodama *hands off*
systems; lore records and verifies them. The handoff format is
`corpus/knowledge/synthesis/worldbible-integration-contract.md`.

**Refuses:** claiming canon; real-world rights/attribution rulings;
game mechanics (game-dev-2d/3d); general source-research method
([chousa](https://github.com/VeigaPunk/chousa-shokunin)); web publishing
([kake](https://github.com/VeigaPunk/kake-shokunin)); prompt/skill craft
([kotoba](https://github.com/VeigaPunk/kotoba-shokunin)).

Sibling repositories, the world bible, and domain source trees are
**read-only**. Only this repo is written.

## What's here

| Path | Role |
|---|---|
| [`SKILL.md`](SKILL.md) | decision table: language, myth, naming, era, dress, consistency-check handoff |
| [`PROVINCE.md`](PROVINCE.md) | generative craft vs canon ownership |
| [`examples/culture-d2/`](examples/culture-d2/) | end-to-end culture packet (brief → phonology → myth → costume → naming) |
| [`tools/assemble-d2.py`](tools/assemble-d2.py) | assemble D2's gate-facing records |
| [`tools/gates/`](tools/gates/) | phonology, naming-collision, myth-consistency, costume-era, lexicon, provenance, handoff |
| [`corpus/`](corpus/) | sourced notes and lessons |
| [`SCORECARD.md`](SCORECARD.md) · [`LOG.md`](LOG.md) · [`SHONEN.md`](SHONEN.md) · [`MINT.md`](MINT.md) | axes, trail, promotion, mint evidence |

## A first check

```sh
python3 tools/assemble-d2.py --check
```

`--check` compares assembled bytes without writing. The frozen round-3
gate outputs live under `tools/gates/frozen/round-3/`. Culture D2 is a
worked example, not a canon ruling.

## How a lane learns

Append-only corpus; every claim separates observation / inference /
unknown; unverified claims are marked `to-verify`. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme).
