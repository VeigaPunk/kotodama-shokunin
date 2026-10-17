# kotodama-shokunin — 言霊

Linguistic-cultural worldbuilding. Languages, myths, symbols, eras,
costume, and naming, designed as one system and handed to the world
bible.

言霊 (kotodama, "word-spirit") is the premise, as `SKILL.md` states it:
a culture's language is evidence of its world. Myth shapes vocabulary,
era shapes register, costume carries a lexicon, and symbols fossilize
into words. This repository is where those systems are generated. The
world bible — entities, relations, timeline, canon — belongs to
lore-shokunin ([shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible)).
Kotodama supplies systems. It does not edit the bible, and it does not
declare canon.

## The job

`PROVINCE.md` owns conlang design and diachronic staging, mythic and
symbolic systems, era and period models, costume and material-culture
terminology, and naming systems, plus this lane's gates and the records
under `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis}`.

It refuses canon claims (lore), real-world rights and attribution rulings,
game mechanics (the 2D and 3D lanes), general source-research method
(chousa), web publishing (kake), and prompt or skill craft (kotoba).
Contested scope is reported to the integrator.

The handoff format is
`corpus/knowledge/synthesis/worldbible-integration-contract.md`.
Sibling repositories, the world bible, and domain source trees are
read-only. Writes stay in this repository, its own fleet round reports,
and allowed append-only L0 questions.

## A worked example

`examples/culture-d2/` is a culture built end-to-end from components.
`tools/assemble-d2.py` assembles the gate-facing packet without
reconciling design disagreements. `--check` compares bytes and does not
write:

```sh
python3 tools/assemble-d2.py --check
```

The script's docstring is the contract: run it from any directory; it
uses the costume gate's reader on selected blocks, and it is not a
general YAML loader. Gates live under `tools/gates/`.

## Read this first

1. [`PROVINCE.md`](PROVINCE.md) — owns, refuses, and the lore handoff.
2. [`SKILL.md`](SKILL.md) — the premise and the decision surface.
3. [`corpus/knowledge/synthesis/worldbible-integration-contract.md`](corpus/knowledge/synthesis/worldbible-integration-contract.md) — how a system leaves this repo.
4. [`examples/culture-d2/`](examples/culture-d2) — one culture, in parts.

## On disk

| Path | Role |
|---|---|
| `SKILL.md` | Operating manual. |
| `PROVINCE.md` | Boundary, including the write scope. |
| `corpus/knowledge/` | Linguistics, myth and symbol, material culture, synthesis. |
| `examples/culture-d2/` | The D2 culture and its packet. |
| `tools/assemble-d2.py` | Packet assembly. `--check` is read-only. |
| `tools/gates/` | Consistency gates the assembler reads. |
| `MINT.md`, `SHONEN.md` | Mint record and promotion checklist. Rank is shonen. |
| `LOG.md`, `SCORECARD.md` | Audit trail and axis verdicts. |

## Fleet

Protocol and roster: [shokunin](https://github.com/VeigaPunk/shokunin).
This repository is a sibling lane. It is not an object in the fleet
root's `MANIFEST.json` `roster` array (13 ids, ending at `kaidoku`,
read 2026-10-17). Canon decisions stay with lore. Rank **shonen**.
