# Round 29 adjacency audit — register law

Scope: claim A in `reports/round-29/claims.json:25-30` — inspect the register/law content and both register knowledge entries for out-of-province material; verify that the speech-act framework is used as in-world design rather than as a real-world rights ruling; check the province boundary.

## Verdict

**PASS: no out-of-province bleed found in the reviewed material.** The speech-act framework is used as a design toolkit for a declared NON-CANON D4 scenario. No real-world legal-rights ruling, canon decision, or game mechanic is made. `PROVINCE.md` remains accurate; no change to it is indicated. This is an adjacency finding, not legal clearance, canon review, or a claim that the fictional design is historically true.

## Evidence

- `PROVINCE.md:1-14,16-31` places linguistic-cultural worldbuilding, its own corpus, gates, examples and reports in this lane; it reserves canon to lore-shokunin and refuses real-world rights/attribution rulings and game mechanics. Both reviewed knowledge entries are indexed under linguistics and explicitly reserve canon to lore-shokunin (`corpus/README.md:138-139`).
- `corpus/knowledge/linguistics/register-strata-attestation.md:34-45` distinguishes a speech variety from the separate law over speech acts. Sections 2 and 4 (`:47-72,90-103`) present Austin/Searle as a designer's toolkit and translate it into hypothetical speaker, venue, force and consequence fields. Its source statement says the frameworks are cited, not blended into claims about real communities (`:26`); its limits and handoff reserve fictional truth and canon (`:298-313`).
- `examples/culture-d4/components/04-lexicon.yml:1-17,282-287` and `examples/culture-d4/components/13-register-law.yml:1-25,60-71` explicitly mark the components as NON-CANON/design choices and disclaim real-world language, institution, community and rights decisions. The law component says it does not describe or approximate a real institution, court or register (`:60-71`). The assembled packet also declares NON-CANON (`examples/culture-d4/packet.d4.yml:1-5`); its `register_law` rows at `:2710-2789` instantiate only the fictional stamp register, acts, speakers, forces and record consequences.
- The ceiling entry is likewise reference/design method only and routes canon to lore-shokunin (`corpus/knowledge/linguistics/register-lexicon-ceilings.md:1-3,241-248`). Its real-world cases are explicitly calibrated as linguistic analogues, not legal or gameplay content (`:176-189`).

## Potential false positives checked

- “Rights, duties, permissions” in `register-strata-attestation.md:17` names Searle's theoretical account of deontic powers; it does not apply that theory to adjudicate anyone's actual rights. The fictional “furnace right” and `L-15`'s “right-of-way” are D4 design/gloss content (`examples/culture-d4/components/01-brief.yml:81,97`; `examples/culture-d4/components/04-lexicon.yml:172`), not real-world rulings.
- “Verlan” and “language games” in `register-lexicon-ceilings.md:180-183` are linguistic examples of constrained word operations. They are not game-development mechanics, which remain outside this province.

## Independent ceiling re-measurement

Re-run at **2026-10-18 20:55:53 UTC**:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1; date -u; python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest; python3 -B reports/round-28/ceiling/measure-ceiling.py
```

Result: self-test **10/10**; 27 mark-axis plain words; delivered reader **19 legal / 8 illegal**; pre-fix reader **18 / 9**, differing by `L-45`; reversal mechanism holds **27/27**. This agrees with the round-28 correction, which marks 18/9 as the historical pre-fix reading and supersedes it with 19/8 (`register-strata-attestation.md:343-402`).

Locator note, not an adjacency finding: the entry's round-27 source note identifies the packet law block at line 2617 (`register-strata-attestation.md:14`), while the currently checked packet block starts at line 2710. The source note explicitly cites that churning packet by revision rather than digest; use the current packet location when citing the present tree.

**Disposition:** no bleed to route; no canon/right/game-mechanics finding; province unchanged.
