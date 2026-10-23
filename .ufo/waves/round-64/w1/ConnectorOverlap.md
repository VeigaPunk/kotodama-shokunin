# ConnectorOverlap — round 64 wave 1

Axes named: **coverage (C)**, **operability (O)**, **calibration (Ca)**. One move. No counter edited, no entry integrated, no sibling written.

## Verdict

The entry topic stays inside kotodama. It is linguistic-cultural worldbuilding for fictional language practices (caregiver registers, early talk, correction, bilingual childhoods, narrative/literacy, address-as-a-learning episode), handed to the world bible and not recorded as canon. It does **not** own child-language acquisition research as a method, and it does **not** own the world bible.

Contested scope to report, not absorb:

1. **Method vs topic (chousa).** `chousa-shokunin/PROVINCE.md` owns question framing, source hierarchy, citation chaining, hop resolution, and claim-vs-source verification. It does not own this subject. Contested only if the entry starts teaching that method. Contract route already exists: `corpus/knowledge/synthesis/worldbible-integration-contract.md:166` (“Evidence retrieval methodology is the actual task → chousa”). Nearest tooling prior art is `chousa-shokunin/tools/quote-reopen.py` (TSV `id/source_id/quote`, verdicts `VERBATIM|ABSENT|TOO_LONG|NO_SOURCE|UNREACHABLE`, 25-word cap, 8 MiB, head-stripped HTML). It is not this lane’s locator. Do not port it.
2. **Canon vs design prompts (lore).** `lore-shokunin/PROVINCE.md:3` and `MANIFEST.json` roster domain “fictional-world records + consistency verification” own the world bible. Lore’s own adjacent line (`PROVINCE.md:28`) already names kotodama packets and records CM-g packet intake as uncovered; the contract’s bilateral read is still pending (`worldbible-integration-contract.md:15`). Skeleton §10 already refuses canon. Contested only if §9’s choice table is later filled with settled in-world facts (named peoples, laws, dates). Do not write a lore receipt.
3. **Intra-lane partial owners (the non-obvious seam).** No sibling owns the topic. Three kotodama entries already own adjacent slices. Restating them inside the new file would make the coverage claim “unowned → one entry” false at review, and patching those neighbours this round fails C’s `NOHARM` (the knowledge diff may list only the new entry).

## Roster map decided against

Read 2026-10-23, read-only. All 21 `*-shokunin/PROVINCE.md` files under `/home/vgpnk/Projects/shokunin/`. `MANIFEST.json` `roster` has 13 rows; eight provinces exist off-roster (chousa, kotodama, mado, mori, souji, tabi, tameshi, tsukuroi). Off-roster is not unowned — ownership is the province text.

| lane | roster | decided against because |
|---|---|---|
| lore | yes | owns records and canon, not the generative craft; handoff recipient |
| chousa | no | owns research *method*, not acquisition as a design topic |
| kotoba | yes | prompt/skill craft; kotodama refuses it by name (`PROVINCE.md:20`) |
| kengaku | yes | LLM/model evaluation, not child-language research |
| kasegi | yes | bounty and security research only |
| audio | yes | SFX/soundtrack measurement; “sound of talk” in §2 is a linguistic register, not a WAV. Refuses narrative canon |
| game-dev-2d | yes | headless 2D fixtures; refuses narrative canon |
| game-dev-3d | yes | headless 3D fixtures; refuses narrative canon |
| kake | yes | web publishing |
| kagi | yes | secrets; “child” in its province is an undeclared directory |
| kama | yes | local model serving; “child” is a llama-server process |
| kaidoku | yes | shipped-artifact RE; “acquisition” is hardware/signal |
| revenger | yes | shipped-artifact RE; refuses narrative canon |
| kumitate | yes | orchestration runtime; routes research method to chousa |
| mado | no | desktop/compositor |
| mori | no | fleet/host observability; “acquisition” is slot acquisition |
| souji | no | repo hygiene |
| tabi | no | browser craft |
| tameshi | no | fixture/mutation method, not this subject |
| tsukuroi | no | host operability |
| kotodama | no | **keeps the topic** — domain is conlang, registers, naming, for fictional worlds, feeding the bible (`PROVINCE.md:3-7`); refuses canon, chousa’s method, kotoba, game mechanics (`PROVINCE.md:16-20`) |

Filename sweep this turn: `corpus/knowledge/**/*{social,acqui,caregiver}*` → no hits. The entry path does not exist yet (`entry exists False`). Claim C’s “0 filename owners” still holds. No sibling province line claims language socialization, caregiver register, or child-language acquisition as subject matter.

## Evidence (intra-lane seams the skeleton does not name)

- `corpus/knowledge/linguistics/gesture-co-speech-pointing.md:142-151` (§9 “Acquisition and learning”) already owns caregiver *pointing*: preverbal pointing, caregiver pointing frequencies, gesture-before-word, taught adult pointing form. Skeleton §3 (“Turn-taking, babble and the first words”) collides if it restates that manual channel.
- `corpus/knowledge/linguistics/naming-systems.md:1,55-57` owns name-slot grammar and life-stage names (Japanese childhood `yōmyō`; Balinese teknonymy). `kinship-terminology.md:3` owns “kin terms borrowed into address systems (… teknonymy, register strata)”.
- `sociolinguistics-registers.md:1,50,114` owns register systems, honorific ladders, and age-graded address. It does not own infant-directed speech as a participation practice.
- Staged address row is the caregiving episode, not the inventory: `rows/ScribeRowS739/row.txt` quote “Parents can use various terms of address to children depending on situational contexts.” That slice is the new entry’s. The inventories stay with the neighbours.
- Three reopen programs, not one (operability must not be read as coverage’s live check):
  - C `LIVE` is pinned to `reports/round-61/reopen-quote.py` (`accept-c.py:45-46,69,75-76`): `LOCATED|NOT_LOCATED`, urllib redirects, PDF via pypdf, echo-host refusals. Docstring still says it fetches with redirects followed.
  - O scores the unchanged `tools/reopen-row.py` (`accept-o.py:11,142`): `LOCATED|CAPTION_ONLY|ABSENT|TRUNCATED|UNREACHABLE|REFUSED|MALFORMED|NO_QUOTE|NO_ROW`, hand-followed redirects, caption split, wall budget vs socket timeout (`DRIP`).
  - Sibling prior art: `chousa-shokunin/tools/quote-reopen.py` (header above). Different registry grammar and verdict set.
  A green `accept-o.py` does not locate S718–S743. A green chousa verifier would be absorbing another lane’s method.

Inherited defects re-checked this turn (not fixed here):

```
MISSING mined ['ScribeRowS723', 'ScribeRowS740']
MISSING rej []
bullets 19 missing ids ['S721', 'S723', 'S727', 'S733', 'S740', 'S741', 'S743']
entry exists False
```

`LIVE`’s frozen subset includes S723 (`accept-c.py:45`). Those two row dirs are still absent, so `ROWS` and `LIVE` cannot pass until they land. Observed receipt, not a check this seat re-ran: `reports/round-64/telemetry/dry-run-c.txt` begins `FILE FAIL` (entry absent) and `ROWS FAIL` (`S718:rows=0` …).

Counter stamp, recorded not edited: `accept-c.py:2` still says “revision 0” while inline comments say revision 1 (`:224`), revision 3 (`:395`), and revision 4 (`:405`). The frozen predicate in `claims.json` does not name a revision number. No leg was judged wrong from that stamp alone; do not revise the counter to “clarify” it.

`FILE` bounds that constrain the move (`accept-c.py:16-17,154`): one H1, no H3, ≤ 16 H2, ≤ 250 lines, a `- topic:` line. Skeleton (`.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md`) is 63 lines, H2s = 10. `ONEID` plus `tools/check-cited-lines.py:17-19`: a line with two S-ids is `MULTI-ID`; a `|` line carrying any S-id is `TABLE-ID`. `RESTATE` (`accept-c.py:271`) requires every S718–S743 citation to be a single bullet of the shape `- … (Snnn)`. `LINK` (`accept-c.py:36-37`): no new-row live URL in the entry.

## Proposed move

Insert one H2 into the new entry only, between skeleton §9 and §10, before bullets are filled. No edit to neighbour files (that fails `NOHARM`). No S-id and no URL anywhere in the section (that fails `ONEID` / `RESTATE` / `LINK`). No H3. Do not retarget `LIVE` onto `tools/reopen-row.py` or onto `quote-reopen.py`.

```markdown
## Boundary — partial owners, one way

Neighbours keep the slices below. This entry cites them by path and does not restate them. Design questions here stay conditional; lore records canon.

| Neighbour | What it already owns | What this entry keeps |
|---|---|---|
| `gesture-co-speech-pointing.md:142` | gesture acquisition, including caregiver pointing | spoken participation: infant-directed sound, babble, first words, correction episodes |
| `naming-systems.md:1`; `kinship-terminology.md:3` | name-slot grammar, life-stage names, teknonymy, kin-term inventories | the caregiving episode that teaches a child an address form |
| `sociolinguistics-registers.md:1` | register systems, honorific ladders, age-grading | caregiver register as participation, not the ladder |
| `../synthesis/worldbible-integration-contract.md:159` | lore owns the world bible; chousa owns retrieval method | §10 handoff only; no canon decision and no method port |

Claim C’s live check runs `reports/round-61/reopen-quote.py`. Claim O scores `tools/reopen-row.py`. `chousa-shokunin/tools/quote-reopen.py` is the nearest sibling prior art and is not a locator for either claim.
```

That is 11 H2s (≤ 16) and about 15 added lines. Topic line unchanged, so `SWEEP`’s verbatim README topic is untouched.

## Affected axes

- **Coverage — improved, none harmed.** Review-only “topic fit” and “one-way pointing to partial owners instead of restatement” (`claims.json` claim C) become a `FILE`-legal section. The 26-row claim is not narrowed. Neighbour files stay out of the knowledge diff.
- **Calibration — improved, Ca legs untouched.** Stops a second owner inside linguistics, and stops a green O (or a chousa verifier) being read as C’s `LIVE`. `accept-ca.py` lands are not in this move.
- **Operability — not harmed.** `tools/reopen-row.py` and `accept-o.py` bytes stay as pinned. Merging the three reopeners would be the harm; this move refuses it.

## Risks

- A later bullet that puts `(S718)`–`(S743)` inside the boundary table fails `RESTATE` (shape) and `ONEID` (`TABLE-ID`). Keep new-row citations as the section bullets only.
- Reciprocal pointer rows added to `gesture-co-speech-pointing.md` or `naming-systems.md` fail `NOHARM`. One way, new file only.
- Line budget: 26 bullets plus this section must stay ≤ 250. This insert is small; long per-bullet prose is the actual threat.
- S723 and S740 are still missing. This section does not create them. `ROWS` and `LIVE` stay red until those rows exist. Do not treat this proposal as an `ACCEPT-C-64` pass.
- Do not “fix” the `accept-c.py` revision-0 docstring. If a stamp leg is ever added, its forcing control is: docstring revision number equals the highest inline `revision N` comment, else `FAIL`, with the current file as the must-fail specimen. Not this move.

## Verification (not run as a pass)

This seat did not execute `accept-c.py`, `accept-o.py`, or `accept-ca.py`. An unrun check has not passed. After the integrator inserts the section and nothing else under `corpus/knowledge`:

1. `python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/language-socialization-and-acquisition.md` → `CITED-LINES: 0 finding(s)`.
2. Entry has one H1, zero H3, ≤ 16 H2, ≤ 250 lines, and the original `- topic:` line byte-for-byte.
3. `git diff --name-only ff30a205c8d23b35f1ac533740121a955a9fda96 -- corpus/knowledge` lists only the new entry.
4. The boundary section matches neither `https?://` nor `\bS\d{3,}\b`.
5. `tools/reopen-row.py` and `reports/round-61/reopen-quote.py` are unchanged versus the base.

Tools installed: none.
