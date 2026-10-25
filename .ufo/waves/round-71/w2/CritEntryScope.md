# CritEntryScope — round 71, wave 2 (falsify: canon overreach in the claim-C entry)

Seat: L1Kotodama71.CritEntryScope (leaf critic; read-only on lane bytes; this file is the only write).
Target: `corpus/knowledge/culture-material/dance-performance-movement-codes.md` as landed at
`498db73` (only commit touching it; lane HEAD `cb77200`).
Axes: (A1) body statements that decide a world's canon; (A2) `- scope:` / `- refuses:` fidelity to
QUALITY criterion 5 and lane convention; (A3) handoff pointer resolves and names the right canon
authority; (A4) real-tradition claims stay within what the cited record states.
No tools installed or updated.

## Verdict summary

| axis | verdict | finding |
|---|---|---|
| A1 body canon | **FAIL (fixable, 1 line)** | F1 — `:38-39` tells the worldbuilder to fix "which school's variant is canonical in-world" |
| A2 scope/refuses | PASS with notes | F3 stale wave-1 PASS provenance; F4 `- refuses:` is a corpus-unique header field |
| A3 handoff | PASS with note | path resolves, contract assigns canon to lore; F2 paraphrase omits lore's *decision* authority |
| A4 real-tradition claims | PASS with notes | Flamenco/Kabuki/Oruro/Sema re-located in captures; F5 S873 never cited; F6 Tango "defined by" overstates |

## F1 — FAIL: the movement-vocabulary section assigns an in-world canon decision (A1)

Counterexample (entry `:38-39`):

> A worldbuilder deciding a dance "grammar" should fix, in order: the atomic
> units, the combinatorics, and which school's variant is canonical in-world.

This is the only body sentence that frames the method's output as *canon*. It contradicts the
entry's own `- scope:` ("it decides no world's canon", `:23`) and `- refuses:` ("claims of canon …
for any world", `:24`), and the lane authorities:
- `corpus/QUALITY.md` criterion 5: "no entry decides what is true in any world. Canon recording and
  consistency verification belong to lore-shokunin; entries end at the handoff."
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:17` — lore owns "canon decisions";
  `:100` — "Canon standing | Lore's own policy … otherwise `not canonized` | Lore only";
  `:96` — kotodama output is a "candidate world-fact", not canon.
- `PROVINCE.md:16` — "**Refuses:** claiming or recording canon — that is lore-shokunin".

Each of the other imperative steps (`:98-108` "decide / fix / state / choose") is a design choice
and is covered by `:123-124` ("this entry proposes systems only"); only `:39` names the outcome
canon. A reader following `:38-39` will mark a school variant as canon inside kotodama, i.e.
the duplicate-authority case the contract forbids.

Smallest safe correction (one clause, `:39`):
`…the combinatorics, and which school's variant the design proposes as the in-world standard
(a candidate for the lore handoff, not canon).`

Command:
```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
rg -n -i '\b(canon\w*|decid\w*|decision|must|should|true|truth|really|real|authentic|correct|official)\b' \
  corpus/knowledge/culture-material/dance-performance-movement-codes.md
```
Output (hits): `:23 scope`, `:24 refuses`, `:38-39` (F1), `:55` "must stay coupled" (describes the
real traditions' coupling, not a world — PASS), `:100`, `:103` ("decide whether…" design step —
PASS), `:110` refusal rule (PASS), `:123` handoff (see F2). No other canon-bearing statement.

## F2 — note: handoff paraphrase drops lore's decision authority (A3)

`:122-124` (section `:119`): "The handoff to lore-shokunin stays through the world-bible integration contract;
lore records and verifies canon, and this entry proposes systems only."
- Pointer: the contract is named by title only; its path is in `- couples:` (`:22`,
  `synthesis/worldbible-integration-contract.md`) and resolves (`test -f` OK, below). PASS.
- Wording mirrors `PROVINCE.md:17` ("lore records and verifies them"), so it is lane-consistent,
  but the contract (`:17`) and the sibling `footwear-codes-terminology.md:10` ("canon belongs to
  lore-shokunin") say lore *decides*. Combined with F1 the omission leaves "who decides" open.
Correction (optional, pairs with F1): `lore decides, records and verifies canon`.

Command:
```
for p in culture-material/masks-masquerade.md culture-material/dress-through-eras.md \
  culture-material/music-instrument-lexicon.md linguistics/gesture-co-speech-pointing.md \
  myth-symbol/ritual-liminality.md culture-material/calendar-festival-systems.md \
  culture-material/craft-artisan-lexicon.md synthesis/costume-language-coupling-table.md \
  synthesis/symbol-lexicon-colexification.md civilizations/india-classical-sanskrit.md \
  civilizations/japan-edo.md civilizations/taino.md synthesis/worldbible-integration-contract.md \
  culture-material/transport-mobility-lexicon.md culture-material/funerary-material-culture.md; do
  test -f corpus/knowledge/$p && echo "OK $p" || echo "MISSING $p"; done
rg -n -i 'canon|lore' corpus/knowledge/synthesis/worldbible-integration-contract.md
```
Result: 15/15 OK (13 couples + 2 gap-filled partial owners). Contract `:2,:12,:17,:100` assign canon
to lore. Entry ends at the `## Limits and handoff` section (QUALITY 5 "entries end at the handoff"). PASS.

## F3 — note: wave-1 H5 PASS was given to text that did not land (A2, provenance)

`.ufo/waves/round-71/w1/RevDanceEntryShape.md:121-123` passes H5 on a draft scope line "(59)":
"decides nothing about any world, names no canon fact, makes no promotion or clearance verdict,
and ends at the handoff". The landed `:23` reads only "real codification schemes a worldbuilder
can adapt; it decides no world's canon". The landed line still satisfies QUALITY 5 in substance
(canon refused; the entry ends at its handoff section), but the "names no canon fact / no
promotion or clearance verdict" legs the reviewer cited are absent, so H5 cannot be cited as
evidence for the landed bytes. Siblings carry the full form (`bathing-and-body-hygiene.md:10`,
`timekeeping-instruments.md:10`, `linguistics/sacred-registers-liturgical-language.md:24`).
Correction (optional): restore the reviewed wording or re-run H5 on `498db73` bytes.

Command:
```
sed -n 115,126p .ufo/waves/round-71/w1/RevDanceEntryShape.md
sed -n 23,24p corpus/knowledge/culture-material/dance-performance-movement-codes.md
git log --format='%h %s' -- corpus/knowledge/culture-material/dance-performance-movement-codes.md
```

## F4 — tradeoff: `- refuses:` is a corpus-unique header field (A2)

```
rg -l '^- refuses:' corpus | wc -l     # 1 (this entry only)
rg -l '^- scope:'   corpus | wc -l     # 39
```
Every other entry folds refusals into `- scope:`. No gate reads the field
(`rg -n 'refuses:' tools/` → no header parser), so it is harmless today but is a second convention.
Its content is correct against `SKILL.md:553-557` / `PROVINCE.md:16-19` (canon; real-world
rights/attribution). Not a defect for the judge; smallest correction if consolidating: merge `:24`
into `:23`.

## F5 — note: S873 is "mined" but cited 0 times in the body (A4, adjacent)

```
E=corpus/knowledge/culture-material/dance-performance-movement-codes.md
for i in $(seq 861 873); do printf "S$i %s\n" "$(sed -n '26,$p' $E | rg -c "S$i\b" || echo 0)"; done
```
S861–S872 cited 1–2 times each; **S873 = 0** (the calibration shelf `:116` names "SEP's entry"
without the id). `- sources:` `:21` says all 13 rows are used; `corpus/SOURCES.md:828` lists the
entry in S873's used-by. This matters for scope: SEP ("a vexed methodological question", Gate
`corpus/lessons/round-71.md:31`) is the only source that grounds the `- refuses:` "universal dance
taxonomies" leg, while `:28` asserts the near-universal "Movement vocabularies behave like
lexicons" from three codified traditions (S871/S872/S868).
Correction: hedge `:28` to "Codified movement vocabularies …" and cite `(S873)` on the `:116`
shelf line (one id per line keeps QUALITY 15). Overlaps RevRows/RevEntry axes; recorded here for
the refusal leg only.

## F6 — note: Tango sentence overstates the record; step 6 uses an undefined term (A4)

- `:59` "Tango is defined by UNESCO as the music, dance and poetry of tango together — an embodied
  identity". Capture 20260925201518 reads: "As one of the most recognizable embodiments of that
  identity, the music, dance and poetry of tango both embodies and encourages diversity and cultural
  dialogue." UNESCO describes tango as an embodiment of a Río de la Plata identity; it does not
  "define" it. Calibration shelf `:114` limits tier A to "what the record itself states".
  Correction: "UNESCO's record describes the music, dance and poetry of tango as one embodiment of a
  regional identity (S861)".
- `:103` "the contact/identity register" — "contact" appears only in the S861 registry scope cell
  (`SOURCES.md:816` "emigration/contact dance register"), never in the body. Correction: name it
  in the Tango paragraph or drop "contact".

Re-located claims (PASS), via `curl -sSL -A 'Mozilla/5.0' https://web.archive.org/web/<capture>/<url>`
with HTML stripped:
- Flamenco 20210302140159: "fusing song (cante), dance (baile) and musicianship (toque)"; "differing
  depending on whether the performer is male (heavier use of the feet) or female"; "Transmission
  occurs through dynasties, families, social groups and Flamenco clubs" — supports `:56-58`.
- Kabuki 20200330004935: onnagata, aragoto/wagoto, "the mie, in which the actor holds a
  characteristic pose" — supports `:93`.
- Mevlevi Sema 20220323094705: "1,001 days of reclusive training within the mevlevi-houses
  (mevlevihane)" — supports "training regime and venue register" `:82` (second fetch of this capture
  was refused, `curl: (7) Failed to connect`; first fetch succeeded).
- Oruro: wave-1 quote (`w1/ScoutOpenSourcesC.md:19`) contains "repeat the journey for a full twenty
  hours without interruption" — supports `:68-69` (not re-fetched).

## Smallest safe correction set

1. `:39` — replace "is canonical in-world" with "the design proposes as the in-world standard (a
   candidate for the lore handoff, not canon)". **Required for A1 PASS.**
2. `:123` — "lore decides, records and verifies canon". Optional.
3. `:59`, `:103`, `:28`, `:116` — F5/F6 wording/citation fixes. Optional, not canon-bearing.
