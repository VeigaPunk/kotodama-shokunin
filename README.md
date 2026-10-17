# kotodama-shokunin — 言霊

Linguistic-cultural worldbuilding. A culture's language is evidence of its
world: myth shapes vocabulary, era shapes register, costume carries a
lexicon, and symbols fossilize into words.

Rank: **shonen**. [`SHONEN.md`](SHONEN.md) boxes are open. Marks of `[~]`
are the lane asserting, and `[x]` waits on a named non-author verifier.

Fleet: [shokunin](https://github.com/VeigaPunk/shokunin). Canon recording
belongs to lore-shokunin
([shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible)).

## The question

> Does this language, myth, naming system, or costume lexicon hang
> together as one culture, and is the handoff to the world bible shaped
> so lore can record it without this lane writing canon?

## Boundary

**Owns:** conlang design and diachronic staging, mythic and symbolic
systems, era models, costume and material-culture terminology, naming
systems, and the gates in this repository.

**Hands off:** canon — lore records and verifies the world bible. This
lane generates systems and hands them off. Also outside: real-world
rights rulings, game mechanics, general source-research method (chousa),
web publishing (kake), prompt craft (kotoba).

Sibling repositories, the world bible, and domain source trees are
read-only. Contested scope is reported, never absorbed. The handoff
format is `corpus/knowledge/synthesis/worldbible-integration-contract.md`.

## Gates and the sample culture

[`tools/gates/`](tools/gates/) holds the craft checks:

| Gate | File |
|---|---|
| phonology | `tools/gates/phonology-sanity-gate.py` |
| myth | `tools/gates/myth-consistency-gate.py` |
| naming collisions | `tools/gates/naming-collision-gate.py` |
| costume and era | `tools/gates/costume-era-consistency-gate.py` |
| lexicon coverage | `tools/gates/lexicon-coverage-audit.py` |
| provenance | `tools/gates/provenance-audit.py` |
| handoff packet | `tools/gates/handoff-packet-check.py` |

`handoff-packet-check.py` validates one Markdown packet against the
integration contract (16 required envelope fields, named in its
docstring).

The worked sample is [`examples/culture-d2/`](examples/culture-d2/).
Assemble its gate-facing packet without resolving design disagreements:

```sh
python3 tools/assemble-d2.py --check
```

`--check` compares bytes and does not write. Omitting it writes
`examples/culture-d2/packet.d2.yml`. A sample packet also sits at
`examples/handoff-packet.sample.md`.

## Map

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | decision table and error patterns |
| [`PROVINCE.md`](PROVINCE.md) | owned craft and the lore handoff |
| [`corpus/knowledge/`](corpus/knowledge/) | linguistics, myth-symbol, culture-material, synthesis |
| [`MINT.md`](MINT.md) | why the lane was minted |
| [`LOG.md`](LOG.md), [`SCORECARD.md`](SCORECARD.md) | rounds and axis verdicts |

Findings go to lore as a list. This lane does not pick the canon answer.
