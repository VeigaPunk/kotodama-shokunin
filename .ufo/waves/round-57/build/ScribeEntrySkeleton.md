# Round 57 C — heraldry entry skeleton

## Findings

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/QUALITY.md:5-20` requires cited/checkable support for every factual claim, inline `(to-verify)` for claims that cannot be verified, an explicit calibration status, named coupling, worldbuilder-usable decision aids, and a lore handoff rather than canon decisions.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/monsters-hybrid-beings.md:3-12` and `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/civilizations/kongo-kingdom.md:3-12` use the requested head-field order: topic, gap filled, sources, couples, source, verified-at, recheck, scope. Their body patterns include one-owner boundaries, decision tables, calibration, lore handoff, recheck, and scope.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/PROVINCE.md:16-29` reserves canon and the world bible to lore-shokunin; Kotodama supplies a reference and hands off through the world-bible integration contract.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/claims.json:13-22,98-103` fixes the C export at S413-S480 and identifies the topic, one-entry/count requirement, and the review-only need to map partial owners and demonstrate substantive coverage. At least 20 distinct S-ids and the live LOCATE/FRESH requirements belong to the eventual landed entry, not this skeleton.
- Zero-owner filename sweep, run at the declared claim base:

  ```text
  git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only 0314aa981071220d206760b5263467faeea05b60 corpus/knowledge | grep -ciE 'herald|emblem|kamon|tamga|insign'
  0
  ```

  The pipeline printed `0`; `grep -c` returns status 1 for no matching lines. This is only the filename sweep, not proof of a substantive gap. The entry must map partial owners and state its boundary.

## Draft behavior and gates

Structure-only outline for one NON-CANON myth-symbol reference entry. Every factual sentence is to be added only with an opened, source-backed quote and a `[NEW-...]` citation; no external sources were opened for this seat. Reserve only S413-S480 for this claim, keep the final entry at or below 230 lines, and defer canon to lore-shokunin. The zero-owner command above was run; no acceptance command, build, or test was run.

## Proposed entry skeleton (draft only; product file not edited)

```markdown
# Heraldry, emblems and inherited identity marks — a linguistic-cultural design system for worldbuilders

- topic: Heraldry, emblems and inherited identity marks as a comparative design system for worldbuilders: mark categories, authorities, visual grammars, transmission, use, and period staging; reference method, not fictional canon.
- gap filled: At claim base, the filename sweep below returns 0; that establishes no filename match, not absence of partial material. Map semantic neighbors and the entry boundary in §2.
  Filename sweep: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only 0314aa981071220d206760b5263467faeea05b60 corpus/knowledge | grep -ciE 'herald|emblem|kamon|tamga|insign'` → 0.
- sources:
  - In-corpus anchors (`corpus/knowledge/`-relative `path:line`, re-read at integration): see §2 and the relevant decision sections.
  - External shelf — only sources opened this round by ordinary means and registered in `corpus/SOURCES.md` in C's reserved S413-S480 block. Cite supported claims with `[NEW-...]` and a located quote; do not treat a lead or abstract as substantive evidence.
- couples: myth-symbol — `animal-symbolism.md`, `color-symbolism.md`; culture-material — `costume-semiotics.md`; linguistics — `naming-systems.md`; synthesis — `worldbible-integration-contract.md`. §2 names each neighbor's owner boundary and this entry's one-way seam.
- source: Lane-side authority is the §2 in-corpus anchor map plus the opened, registered external rows. Design sequence: classify the mark and its bearer/right; identify authority; specify grammar and transmission; choose use-surface and audience; date each layer; hand off canon questions.
- verified-at: 2026-10-22 — written against claim base `0314aa981071220d206760b5263467faeea05b60`; pre-entry knowledge count 232. Record the post-entry count only at landing with the declared acceptance command.
- recheck: See §16.
- scope: Comparative, source-scoped design method for heraldry, emblems and inherited identity marks. Examples do not establish universal equivalences or fictional canon; lore-shokunin owns canon and the world bible.

## 1. Vocabulary, scope and calibration key
Decide which terms the entry uses, what each can mean in the cited context, and how each claim is calibrated; do not universalize an English label.

## 2. One-owner boundary
Map partial owners and their `path:line` anchors; decide what this entry owns and what it points to without duplicating animal, color, costume, or naming systems.

## 3. What kind of mark is this?
Build a decision table distinguishing hereditary arms, office emblems, affinity badges, property marks, and crest rights; decide bearer, claimed relationship, and whether evidence supports the category.

## 4. Who grants, recognizes, regulates and protects it?
For each sourced setting, decide who may authorize, use, recognize, contest, inherit, or protect a mark, and what jurisdiction or remedy the evidence actually establishes.

## 5. Heraldic grammar: blazon as a design language
Decide how a design is specified and read; source each use of tinctures, ordinaries, charges, and blazon terminology, and keep this grammar scoped rather than treating it as universal.

## 6. Heraldic rights, cadency and marshalling
Decide what sources say about right to bear a mark, crest rights, cadency, and marshalling; separate rules from practice and record the authority and limits behind each claim.

## 7. Office and rank emblems that are not hereditary
Compare the source-supported choices for Mamluk blazons, Chinese rank badges, livery badges, and ecclesiastical hats; decide whether each identifies an office, rank, affiliation, person, or another sourced relation, and what happens when status changes.

## 8. Inherited identity and controlled difference
Decide how a mark passes, branches, changes, is shared, or is distinguished across generations; do not infer a rule of inheritance from resemblance alone.

## 9. Kamon, tamga and Polish clan arms: compare without collapsing
For Japanese kamon, steppe tamga, and Polish clan arms, decide what identity relation, use, and transmission each opened source supports; keep distinct systems distinct unless sources establish a comparison.

## 10. House, merchant and livestock marks
Decide who applies and recognizes each house, merchant, or livestock mark, what it identifies or records, and how ownership, transfer, duplication, or dispute is evidenced.

## 11. Seals and flags
Decide what a seal or flag authenticates, represents, or communicates in each sourced use, who may display or issue it, and how it differs from the identity mark placed on it.

## 12. Display surfaces, audiences and access
Choose where a mark appears (including dress, objects, buildings, documents, seals, and flags), who can see it, and what medium, scale, placement, or access rule changes its use.

## 13. Era staging and change
Date every sourced layer; decide what changes in authority, terminology, design, inheritance, or display over time, and flag any undated or anachronistic inference.

## 14. Worldbuilder decision table and build order
Give a usable sequence with columns for mark type, bearer, right/authority, visual grammar, transmission, surface/audience, era, source limit, and the design decision each answer enables.

## 15. Calibration bank
List tempting overclaims and label each mainstream, contested, or discredited with the reason and claim-scoped citations; mark unsupported generalizations `(to-verify)` rather than asserting them.

## 16. Handoff to lore
Specify which design choices can be sent to the world bible and which canon choices remain for lore-shokunin; do not record fictional houses, bearers, or histories as settled canon here.

## 17. Recheck
Name the filename sweep, the partial-owner seams, and the cited source rows that must be reopened before reuse; verify the final entry against the round's acceptance requirements at integration.

## 18. Scope
Restate the reference entry's boundary, its source limits, and its NON-CANON status; point single-tradition dossiers and neighboring systems to their owners.
```

## Touched surfaces and out-of-scope

- Touched: this seat report only, at `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-57/build/ScribeEntrySkeleton.md`.
- Not touched: the proposed knowledge-entry path, `corpus/SOURCES.md`, tools, claims, or any sibling/fleet file. No tools were installed. No external source was opened, so no quote, source tier, or factual historical claim is offered here.
- Artifact: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-57/build/ScribeEntrySkeleton.md`.
