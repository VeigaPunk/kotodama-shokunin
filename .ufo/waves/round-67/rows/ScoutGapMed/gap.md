# ScoutGapMed — claim-C gap verification at base ad5b52b0ab5691358cd38718ab75649dc9916f9a

Verdict: **gap confirmed.** The medicine/healing/physician/remedy register is unowned in
`corpus/knowledge` at the base. All mentions are partial-scope (bathing hygiene
infrastructure, scent prophylaxis, myth-symbol apotropaic purity, civilization notes),
never whole-register owners.

## Command 1 — filename census (expect 0)

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ git ls-tree -r --name-only ad5b52b0ab5691358cd38718ab75649dc9916f9a -- corpus/knowledge | grep -ciE '(^|[^a-z])(medicin|healing|physician|remedy|remedie|surgery|surgical|apothec|hospital|leech|physick|doctor|shaman|curander|herbal)([^a-z]|$)'
0
```

(0 files; grep exit 1 = no match. `git show <base> -- corpus/knowledge/culture-material/medicine-healing-codes.md` fails — entry absent. Culture-material has 34 files, none medicine-named.)

## Command 2 — topic-line sweep (expect only partial-scope mentions)

```
$ grep -rniE '^-?\s*topic\s*:.*(medicin|healing|physician|remedy|surgery|apothec|hospital|shaman|curander|herbal|disease|plague)' corpus/knowledge/
6 matches in 6 files — all partial-scope, none owns the register:
```

| file | matched term | scope of hit |
|---|---|---|
| civilizations/haudenosaunee.md:2 | "False Face medicine traditions" | boundary note on one society's living tradition (kept off-limits) |
| civilizations/mongol.md:3 | "shamanic vocabulary" | language/dress/relay-system entry; religion via vocabulary only |
| culture-material/scent-perfume-aromatics-codes.md:3 | "disease codes" | scent prophylaxis + timekeeping; explicitly bounded "status and disease codes" |
| myth-symbol/amulets-talismans-apotropaic-marks.md:3 | "plague, illness" | apotropaic objects answering disease as one danger among named demons/evil eye |
| myth-symbol/sacred-kingship-mythic-charter.md:3 | "plague" | plague as one observability channel of king's-body doctrine |
| myth-symbol/sacred-topography-pilgrimage.md:5 | "healing archive" | healing as one function inside the votive/ex-voto shrine economy |

Supplement (body text, not `- topic:`): `bathing-and-body-hygiene.md` has §8 "Health,
medicine and the hygiene revolution" — disease-control infrastructure + spa-town business,
explicitly "let the medicine be argued"; its topic line owns the water-and-body institution,
not the healing register. Matches claim's expected partial owners exactly
(bathing / scent prophylaxis / myth-symbol purity).

## Command 3 — sibling ownership (expect no substantive owner)

```
$ grep -rliE 'medicin|healing|physician' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin 2>/dev/null | head -5
/home/vgpnk/Projects/shokunin/chousa-shokunin/.ufo/waves/round-29/falsify/ScoutFreshnessH/rederive-receipt.json
/home/vgpnk/Projects/shokunin/chousa-shokunin/.ufo/waves/round-29/falsify/MutOrder/receipt-baseline.json
/home/vgpnk/Projects/shokunin/chousa-shokunin/.ufo/waves/round-29/falsify/RerunCounterB/receipt-1.json
```

Only `.ufo` wave-receipt artifacts (counter fixtures, not corpus canon); filtering
`/\.ufo/` yields **zero** hits. No lore-shokunin canon owner — the register is free to
claim in kotodama with the standard lore handoff line.

## Registry boundary at base (for ROWS/APPEND legs)

```
$ git show <base>:corpus/SOURCES.md | grep -cE '^\| *S[0-9]+'
724
$ ... | tail -8 unique ids
S793–S800   (base ends at S800)
```

S801–S804 vacant at base → free for Ca disposition rows; S805–S828 free for claim-C rows
(24 expected). S753 (Penn Museum mancala row, tier B) is the one declared in-place
used-by flip.

## Build order for corpus/knowledge/culture-material/medicine-healing-codes.md (5 lines)

1. **Register map**: open the entry by staking the partition — medical systems/theories, institutions, practitioners/guilds, prophylaxis costume+amulets, materia medica — naming which neighbors hold their slices (bathing owns hygiene infrastructure; scent owns prophylactic aromatics; amulets owns the objects' symbolic mechanism).
2. **Source-grounded bullets by class**: one bullet per registry row (S805–S828, tier A/B, anchored quote kept verbatim), grouped under the five classes so each row lands in exactly one section.
3. **Cross-cultural patterns + design protocol**: extract the recurring grammar across the cited cultures (who may treat, where treatment happens, what the treater wears/carries, materia flow) and state the decision protocol a worldbuilder runs.
4. **Calibration**: a calibration shelf flagging the contested/discredited readings the sources support or refute, mirroring the sibling entries' calibration convention.
5. **One-way pointing + lore handoff**: Boundaries section pointing to the partial owners (bathing, scent, amulets, civilization entries) without restating their content; final line hands canon decisions to lore-shokunin.
