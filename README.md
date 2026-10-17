# kotodama-shokunin — 言霊

Linguistic-cultural worldbuilding: the coupling of word and world.

Kotodama designs conlangs and their diachronic stages, mythic and symbolic
systems, era models, costume and material-culture terminology, and naming
systems for fictional worlds. It generates those systems and hands them
off. It does not record canon. Canon standing belongs to lore-shokunin
([shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible)).

Rank: **shonen**. `SHONEN.md` is still here. A search of the fleet
`MANIFEST.json` in the sibling checkout finds no `kotodama` row, so this
repository is not a registered roster member. `MINT.md` is the mint record
that lives here.

## Province

**Owns.** The generative craft and its records:

```
corpus/knowledge/linguistics
corpus/knowledge/myth-symbol
corpus/knowledge/culture-material
corpus/knowledge/synthesis
```

plus this lane's gates and reports.

**Hands off.** Canon — lore records and verifies it. Real-world rights and
attribution rulings. Game mechanics (the game-dev lanes). General source
research (chousa). Web publishing (kake). Prompt and skill craft (kotoba).

The handoff format is
`corpus/knowledge/synthesis/worldbible-integration-contract.md`.
Contested scope goes to the integrator. Sibling repositories, the world
bible, and domain source trees stay read-only.

Claims this lane cannot verify are marked `to-verify`. That marker is a
feature of the corpus, not a leftover.

## Start here

1. `PROVINCE.md` — the boundary and the handoff rule.
2. `corpus/README.md` — the index generated from per-entry topic lines.
3. `corpus/QUALITY.md` — the admission bar, including the `to-verify` discipline.
4. `examples/culture-d2/` — a culture built end-to-end from the corpus.
5. `examples/handoff-packet.sample.md` — a non-canon packet. Its header
   says it is not canonized and that lore disposition is required.
6. `SCORECARD.md` — each score names its counting command and the commit
   it was measured against.

## Run the gates

Six gates live in `tools/gates/`. From the repository root:

```sh
python3 tools/gates/phonology-sanity-gate.py --selftest
python3 tools/gates/lexicon-coverage-audit.py --selftest
python3 tools/gates/myth-consistency-gate.py --selftest
python3 tools/gates/naming-collision-gate.py --selftest
python3 tools/gates/costume-era-consistency-gate.py --selftest
python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md
python3 tools/gates/provenance-audit.py --selftest
```

`--selftest` is the hermetic verdict for the gates that implement it. The
handoff check grades a packet against the contract. A passing packet is
not canon: the sample's own header says lore has not accepted it.

`tools/assemble-d2.py` assembles the D2 culture packet.

## How to read a score

The scorecard's counting commands are part of the claim. Re-run the
command against the commit named in the row. A `to-verify` count moving
down is only an improvement when the triage note says the flag was
resolved, not when the word was deleted.

## Fleet

The protocol lives in [shokunin](https://github.com/VeigaPunk/shokunin).
Handoffs travel to lore. They do not write lore's repository.
