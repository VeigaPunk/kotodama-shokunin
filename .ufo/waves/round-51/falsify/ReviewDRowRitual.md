# Falsify seat: claim D row 44 (`ritual-liminality.md:63`)

Round 51 attempt 3, hyaku phase 3, 2026-10-22. Author-lane attack; verdict is a recommendation, not an admission.

## Item attacked

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:44` (one of the four new rows, lines 44–47), verbatim:

> | `ritual-liminality.md:63` | sacrifice typology, including calendrical rites that consume herd products (the Vedic milk oblation, the royal horse rite) | which animals and products the herd can spare; the rite's form, meaning and budget stay there (§10) |

Provenance: `git diff bff83ba HEAD -- <entry>` shows this row as an added line (`+`), so it is genuinely claim D's new material, not pre-existing.

## Commands run (cwd: lane repo root)

| Command | Output | Exit |
|---|---|---|
| `python3 -B reports/round-51/boundary-count.py` | `rows=15 resolved=15 distinct=15` | 0 |
| `git diff bff83ba HEAD -- corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` piped to `grep 'ritual-liminality\|symbolism-synthesis\|celestial-symbolism\|numerals-and-measures'` | all four new rows appear as `+` lines; row 44 present | 0 |
| `git diff bff83ba HEAD -- <entry>` piped to `grep` (see above) — also confirms the §5 numerals seam sentence added at line 93 region | `+Counting words and classifiers such as "head of cattle" belong to ...` | 0 |
| `realpath .ufo/waves/round-51/falsify` | `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-51/falsify` (write target inside the lane, as assigned) | 0 |

No writes to the lane other than this report. No git state changes (diff/show only).

## Check 1 — does the anchored line support the "What it owns" cell?

The anchor resolves: `ritual-liminality.md` is unique under `corpus/knowledge/` (only `corpus/knowledge/myth-symbol/ritual-liminality.md`; the counter's basename resolution agrees — `resolved=15 distinct=15`). Line 63, verbatim:

> | calendrical / maintenance | feed the machine that keeps time | Aztec veintena rites, Tlacaxipehualiztli gladiatorial sacrifice on the temalacatl stone; New Fire (cosmology-cosmography §8); Vedic agnihotra daily milk oblation; aśvamedha year-long royal horse rite (modern agnicayana performance documented: Staal 1983) | the calendar-owning priesthood's budget |

Line 63 sits inside §4 "Sacrifice: theories, typology, substitution" (section spans lines 51–69), whose body is the sacrifice theory sequence (line 53) plus the typed typology table (types × logic × exemplars × social license). So the cell's head noun "sacrifice typology" is exactly what the anchored section owns, and the two parenthetical exemplars appear on line 63 nearly word-for-word: "the Vedic milk oblation" ← "Vedic agnihotra daily milk oblation"; "the royal horse rite" ← "aśvamedha year-long royal horse rite". "Calendrical" mirrors the row's own type label ("calendrical / maintenance" — "feed the machine that keeps time"), and "budget" mirrors the line's fourth column ("the calendar-owning priesthood's budget"). No overclaim found.

Scoping is correct too: the cell says "**including** calendrical rites that consume herd products", not the neighbour's whole calendrical register — line 63's exemplars also include non-herd Aztec and New Fire material, which the cell properly does not claim. One wording note (low, no fix required): "herd products" read narrowly covers the milk oblation but the horse rite consumes a herd *animal*; in this entry's own idiom (§6 products table lists meat, milk, hide, blood as products; the boundary cell says "which animals **and** products") the phrase is consistent. Optional tightening if ever touched: "herd animals or products".

## Check 2 — is the boundary developed/narrowed in the named body section?

The cell names §10; §10 develops and narrows the seam:

- Line 146: `## 10. Ritual, myth and symbol of the herd`
- Line 148 (lead): "The herd is ledger, offering and metaphor at once (design frame, **H**): write the rite from the herd's books outward (`ritual-liminality.md:63`)." — cites the exact same anchor and states the herd-outward direction of the seam.
- Line 155 (§10 table row): "Sacrifice economy | offerings drawn from the herd's surplus males `(to-verify)` | an animal taboo implies a rite (`symbolism-synthesis-method.md:69`); **sacrifice belongs to myth-symbol**" — explicitly narrows: the herd supplies what it can spare; the sacrifice itself stays with the neighbour.
- Line 171 (§11 build step 8): "Ritual | each taboo written with its rite | §10; `symbolism-synthesis-method.md:69`" — the build order routes through the same section.

## Check 3 — duplicate authority or (to-verify) laundering?

- **No same-noun duplication.** The other 14 rows' ownership cells name: parcel/plough/calendar, wild acquisition, dairy/law, route/draught, money words, fibre chain, lexical field, dung-as-fuel, the herd's signs, shepherd-king office, regional cases, taboo→rite rule, sky figures, counting words. None claims "sacrifice" or a typology of rites. The nearest neighbour, the `symbolism-synthesis-method.md:69` row (line 45), owns the consistency *rule* ("an animal taboo implies a rite") and the symbol grammar — a different noun, and line 155 of this entry assigns the rule and the sacrifice to different owners consistently. Inside `myth-symbol/`, `myth-ritual-theories.md` covers origin *theories* of myth (its §13 sends contested items to `to-verify`; no sacrifice-typology ownership), so there is no rival owner behind the anchor either. §10's own line 158 defers the herd's signs to `animal-symbolism.md:73,:110`, again no clash with this row.
- **No laundering.** The only `(to-verify)` on this seam is line 155's "offerings drawn from the herd's surplus males `(to-verify)`". Row 44 does not restate that claim as fact: its boundary cell asks the design question "which animals and products the herd can spare" without asserting the surplus-males answer, and it explicitly parks the rite's "form, meaning and budget" with the neighbour. The row carries no S-id and no `(to-verify)` of its own; every factual particular in the cell (milk oblation, horse rite) is line-63-backed.
- **Must-not-cite holds for this row:** no S-id at all, no citation of `sign-languages-manual-modality.md`, no mention of the round lesson or the counter script.

## Check 4 — genuine neighbour or filler?

Genuine. The seam is substantive (what the herd can spare vs. the rite's form/meaning/budget — a real pastoral cost line), the neighbour really owns the claimed inventory (a typed sacrifice typology whose calendrical row names herd-consuming exemplars), the entry's §10 lead and §11 step 8 both route design work through the seam, and the boundary cell's nouns trace to the anchored line itself ("budget" ← "the calendar-owning priesthood's budget"). Not filler.

## External source checks (opened 2026-10-22)

The row cites no S-id, so the anchor line is the load-bearing support and was checked in-corpus. As a sanity check on the two exemplars I ran web searches whose result extracts included:

- `https://en.wikipedia.org/wiki/Agnihotra` — agnihotra is the Vedic daily (twice-daily) fire rite whose principal offering is milk. Supports "the Vedic milk oblation".
- `https://en.wikipedia.org/wiki/Ashvamedha` and `https://www.britannica.com/topic/ashvamedha` — aśvamedha is the Vedic year-long royal horse sacrifice. Supports "the royal horse rite".

Both corroborate line 63's exemplars and hence the row's parenthetical. The row's claims are anchored, not S-id-tiered, so QUALITY criterion 6 tier-checking does not attach to this row directly (the neighbour's own Staal 1983 aside was not re-opened — out of this seat's falsifier).

## Findings

- **LOW (wording, no fix required)** — `pastoralism-animal-husbandry.md:44`: "calendrical rites that consume herd products" is loose for the aśvamedha exemplar, which consumes a herd animal rather than a product; the entry's §6 product table (meat included) and the boundary cell's own "animals **and** products" make the phrase consistent as written. Smallest fix, if ever touched: "herd animals or products".

No high- or medium-severity findings. The row's anchor resolves, the ownership cell is supported verbatim by the anchored line, the boundary is developed and explicitly narrowed at the named section (§10, lines 148 and 155), there is no duplicate authority and no laundering of the line-155 `(to-verify)`, and the neighbour is genuine.

## Verdict

**HOLDS** for `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:44`.

## Unrun checks

- The other three new rows (45–47), the line-29 lead, and the line-93 numerals seam: only the counter and diff-cross-check above; per-row anchor audits belong to sibling seats.
- Retention of the 11 pre-existing rows verified only via `distinct=15` (counter) and the diff showing the four new rows as pure additions, not by a full row-by-row before/after table.
- External re-opening of `ritual-liminality.md` §4's own source attributions (e.g. Staal 1983): not this row's falsifier.
- No LSP server was available/available-applicable here: the seat toolset has no `lsp` device and the artifacts are Markdown prose whose references are literal `file:line` anchors, so direct reads plus the counter are the correct instruments; no semantic reference resolution was silently skipped.
