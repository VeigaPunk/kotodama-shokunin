# ConnectSiblingToponymy58 — claim C sibling overlap (round 58)

Seat: KotodamaR58A2.ConnectSiblingToponymy58 (connector, leaf). Read-only scan, 2026-10-23. Axes: coverage, adjacency.

## Result

No sibling lane owns toponymy. Across all 20 sibling lanes (every `/home/vgpnk/Projects/shokunin/*-shokunin` except kotodama), `corpus/knowledge`, `PROVINCE.md` and `SKILL.md` contain **0** hits for the field's own terms. The only real adjacency is lore-shokunin, which owns *place entities and the names recorded on them*. kotodama already owns name generation, and lore's own PROVINCE.md says so. Two lanes state that split in writing: kotoba confirms kotodama owns naming, and chousa owns research method.

Census receipt, run from the fleet root:

```
for d in $(ls -d *-shokunin | grep -v kotodama); do rg -i -c -g '!*.json' '\b(toponym\w*|exonym\w*|endonym\w*|hydronym\w*|gazetteer\w*|place[- ]names?|geographic(al)? names?|onomast\w*|UNGEGN|cartograph\w*)\b' $d/corpus/knowledge $d/PROVINCE.md $d/SKILL.md | awk -F: '{s+=$2} END{print s+0}'; done
→ 0 for each of: audio chousa game-dev-2d game-dev-3d kagi kaidoku kake kama kasegi kengaku kotoba kumitate lore mado mori revenger souji tabi tameshi tsukuroi
```

A broader pattern that added `atlas` and `geograph*` produced 2 false positives. `game-dev-2d-shokunin/corpus/knowledge/2026-10-19-tilemaplayer-body-rid-attribution.md:80` uses "atlas" for a Godot tile atlas, and `kengaku-shokunin/corpus/knowledge/benchmark-selection.md:20` names the benchmark "MCP-Atlas". Neither is an overlap.

## Overlaps (path:line, then the boundary rule for the entry)

| # | Sibling path:line | What it says | Boundary rule for `toponymy-place-names.md` |
|---|---|---|---|
| 1 | `lore-shokunin/PROVINCE.md:3` | Owns "fictional-world records — entities (characters, places, factions, items), relations, timeline events". | kotodama owns real-world toponymic *systems and method*. A place's existence, location and history in the world are lore's. |
| 2 | `lore-shokunin/PROVINCE.md:28` | "Kotodama also owns name generation (`…/linguistics/naming-systems.md`, `…/verification/naming-collision-gate.md`) … lore owns the names and dates recorded on landed entities and events." | This is the governing split. The entry owns how place names are built, layered, standardised and changed. Lore owns which name a landed place entity carries. Note that lore's pointer names `naming-systems.md`, not the new file. |
| 3 | `lore-shokunin/SKILL.md:7-8,16` | Sibling arbitration: "Lore owns fictional-world entities, relations, timeline and integration". Its scope covers "fictional entities, places, factions…". | The entry yields options. It never states which gazetteer, naming authority, renaming or official form exists in-world. |
| 4 | `lore-shokunin/corpus/knowledge/seed.md:9-10,24` | Entity schema `{id, kind (character\|place\|faction\|item), name, …}`; "Names/aliases index-checked: two entities sharing a name must disambiguate." | Exonyms, dual names and former names are handed off as name records against lore entity IDs. Spelling must never be used as identity. |
| 5 | `lore-shokunin/corpus/knowledge/2026-10-12-lore-decision-table.md:17`; `…/2026-10-12-lore-consistency-checklist.md:8`; `lore-shokunin/corpus/README.md:67` | "The checker does not yet check aliases"; name collisions are "unmeasured"; CM-a (aliases, name variants, homonyms) is `uncovered`, and its r103 candidate was REJECTED. | The entry must **not** claim that lore verifies exonyms, renamings or dual names. Lore has no alias coverage. The handoff goes through kotodama's own contract (rows 8–9). |
| 6 | `lore-shokunin/corpus/knowledge/r103-canon-status-and-supersession.md:36-52`, cited at `lore-shokunin/SKILL.md:27` | A later record that corrects or voids an earlier one is appended, never overwritten. Supersession is a sourced in-world declaration. | Renaming as politics, as a design lever: an in-world renaming is a lore event that supersedes a name. The entry supplies the pattern (regime change, commemoration, removal of a derogatory name) and lore records the event. |
| 7 | `kotoba-shokunin/SKILL.md:14-16`; `kotoba-shokunin/PROVINCE.md:53` | "kotodama owns naming and language for fictional worlds despite the similar name". | No toponymy overlap, and no rule is needed in the entry. This confirms kotodama's naming ownership. |
| 8 | `chousa-shokunin/PROVINCE.md:5-7` | Owns "source hierarchy … claim-vs-source verification". | Method adjacency only. The entry's tier A/B rows follow kotodama's frozen rowcheck, not chousa's method, so no entry sentence is needed. |
| 9 | `tsukuroi-shokunin/corpus/knowledge/adjacency-anchors-r19.json:605` | "Cites tsukuroi's host-operability domain to reject world-bible ownership." | None. It is a refusal. |

The kotodama-side anchors the entry should point to are local, so the entry needs no new contract:
- `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md:42` is the Naming ledger row. kotodama supplies "Slot grammar, derivations, aliases, exonyms, taboo rules, candidate labels", lore decides "Entity identity, approved names, official/contested status", and the stop condition is "Matching strings do not prove matching entities".
- The same contract at `:79` (envelope: "Trace endonym/exonym … without merging identities or losing old forms") and `:153` ("preserve obsolete names as historically scoped aliases where lore approves").
- `kotodama-shokunin/corpus/knowledge/synthesis/naming-canon-workflow.md:47` is the Place row ("feature versus settlement; naming date versus settlement date; competing local/official forms"). `:18` separates entity identity from name identity. `:21` says only lore-shokunin can accept.

## Proposed move (one, bounded)

Write the entry's canon-boundary section in lore's own split wording, and route it through the existing contract rows instead of through lore:

> This file owns how place names are built, stratified, standardised, romanized and changed. It does not own any world's place entities or the names recorded on them; that is lore-shokunin's province (lore `PROVINCE.md:28`). Hand off endonyms and exonyms, dual and former names, and renaming patterns as Naming-ledger records under `synthesis/worldbible-integration-contract.md` §3. Each record is keyed to a lore entity ID or a namespaced candidate ID, and old forms are kept as historically scoped aliases. Lore currently has no alias/name-variant check (its CM-a row is uncovered), so a handoff is not a consistency verdict. For slot grammar and the short typology see `naming-systems.md` §3/§5 (one-way pointer).

Why it is non-obvious: the obvious wording is "lore checks names". That would be false, because lore's own records say aliases are unchecked. A reviewer would mark such a sentence NOT-SUPPORTED, or it would later contradict lore's CM-a row.

Affected axes:
- **Adjacency** improves: the boundary is stated with citations to both sides.
- **Coverage** is unaffected: the section is boundary prose, not a claim C row, so it cites no S5xx row and does not touch the predicate legs.

## Risks

- **Lore's pointer will not reach the new entry.** `lore-shokunin/PROVINCE.md:28` names only `naming-systems.md`. Because the claim's pointer is one-way (new entry → `naming-systems.md`), lore's path does not reach the new file. Fixing that means editing lore, which is out of bounds for this lane. If adjacency is graded both ways, L1 may log it as a question for lore.
- **The boundary prose could break a predicate leg.** If `accept-c.py` counts every `(S…)` citation or sentence in the entry, the section must carry no S-id, and no row-quote material may be pasted into it. I did not run `accept-c.py`; L1 should check that its legs ignore boundary prose without citations.
- **Lore's line numbers can drift.** Lore's PROVINCE map is append-only ("earlier text stands"), so `:28` should hold. Re-check it with `sed -n 28p lore-shokunin/PROVINCE.md` at integration.

## Verification for L1

- Census: re-run the loop above. Expect 0 for all 20 lanes.
- `sed -n 28p /home/vgpnk/Projects/shokunin/lore-shokunin/PROVINCE.md` should contain "lore owns the names and dates recorded on landed entities".
- `sed -n 67p /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/README.md` should show `CM-a | aliases, name variants, homonyms | uncovered`.
- `sed -n 42p corpus/knowledge/synthesis/worldbible-integration-contract.md` (in the lane) should show the Naming ledger row.
- After landing, `python3 -B reports/round-58/accept-c.py` should still pass with the boundary section in place.

installs: none.
