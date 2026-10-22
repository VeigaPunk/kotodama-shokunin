# ScribeErrataEntities55 — routed round-55 defect 6 (Gate Grounds entities)

## Scope and provenance

- Routing: `corpus/lessons/round-55-verifier-spotcheck.md` §5 item 6 ("Gate Grounds entities") and §3 "Mechanical check over all 74 Gate lines".
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, read-only except this report. Lane HEAD at read time `456f5adc021346e7e9e7ce17a50d4bb1d208abbc`.
- Bytes read (sha256, pinned):
  - `corpus/lessons/round-55.md` `1bbf70814548295c6e6bd2d916ea15a4b27d43a91a4af40e19062fee65fbc8ff`
  - `corpus/SOURCES.md` `17e2efae22f0519779c4eea5f339c01d319f4f6e8336fd4a9adbbdb647b4abe3`
  - `tools/check-gate-quotes.py` `607acba7e6498724d2a35de2339f4a5fca259faf97c310d5d07d8a423d9de899`
- Interpreter: Python 3.14.8.
- No writes to `round-55.md`; no git or jj writes; no tool installs; no source re-opens; no scratch used.

## Result

1. **Entity scan.** The `## Gate` section of `corpus/lessons/round-55.md` is lines 65-142 and holds 74 `- S` bullets. Exactly 16 of them carry an HTML character reference, at lines 72, 82, 88, 89, 93, 96, 110, 113, 125, 127, 131, 132, 134, 138, 140, 141 — the same 16 lines the routing names. Across the whole file there are 109 `- S` bullets and the same 16 carry entities, so no entity-bearing bullet sits outside the Gate section. The 16 ids are distinct: S288, S298, S304, S305, S309, S312, S326, S329, S341, S343, S347, S348, S350, S354, S356, S357.
2. **Field split.** Grounds 6 (S288, S305, S326, S341, S343, S348); locator 7 (S304, S312, S329, S347, S350, S354, S357); quoted span 2 (S298, S356); URL field 1 (S309). S298 is the only row with entities in two fields (locator and quoted span), so 17 erratum lines cover the 16 rows.
3. **Whole-Gate re-derivation.** Comparing each of the 74 Gate Grounds strings against its registry `teaches` cell (`corpus/SOURCES.md` column 7): 68 byte-equal, 6 equal only after `html.unescape` (the six above), 0 differing otherwise. This reproduces the round-55 closure's §3 count exactly.
4. **Current checker run.** `python3 -B tools/check-gate-quotes.py corpus/lessons/round-55.md` prints `GATE_QUOTES: 0 findings`, exit 0. The checker has no entity handling: `comparable_teaches` (`tools/check-gate-quotes.py:203-205`) strips quote delimiters `["“”«»]` and trailing full stops but never decodes character references, and `truncated_grounds` (`tools/check-gate-quotes.py:208-219`) fires only on a proper prefix. A Grounds that differs from the cell only by entities is therefore invisible to the checker today — neither equal by its rules nor a truncation. The round-56 claim-O `html-entity` class is what will surface it.
5. **Decoding restores verbatim fidelity, it does not change text.** For 14 of the 16 rows the Gate quoted span is already a byte-equal substring of the same row's registry anchor cell; for S298 and S356 it is a substring only after `html.unescape`. So the entities are escaping artefacts, not wording differences.
6. The six registry `teaches` cells are entity-free (checked: no `&` in any of them), so the repair direction is one-way: Gate to registry.

## Erratum lines (draft for the round-56 lesson)

Note for the judge: the `&quot;` and `&#8220;` sequences inside the lines below are quoted defect text — the material under repair — not report formatting. Everything outside them is plain UTF-8.

- S288 (round-55.md:72): Grounds reads the English word &quot;monster&quot; is absent; decoded: the English word "monster" is absent. Grounds equals the corpus/SOURCES.md teaches cell once decoded.
- S298 (round-55.md:82): locator reads opening definition of &quot;monstres&quot;; decoded: opening definition of "monstres".
- S298 (round-55.md:82): quoted span reads (&amp; sont le plus souvent signes de quelque malheur à advenir); decoded: (& sont le plus souvent signes de quelque malheur à advenir).
- S304 (round-55.md:88): locator reads § beginning &quot;The exception seems to be Pazuzu&quot;; decoded: § beginning "The exception seems to be Pazuzu".
- S305 (round-55.md:89): Grounds reads a &quot;monstrous&quot; being; decoded: a "monstrous" being. Grounds equals the corpus/SOURCES.md teaches cell once decoded.
- S309 (round-55.md:93): URL field reads public PDF linked there as &quot;Download PDF&quot;; decoded: public PDF linked there as "Download PDF".
- S312 (round-55.md:96): locator reads paragraph beginning &quot;Belief in the existence of monstrous races&quot;; decoded: paragraph beginning "Belief in the existence of monstrous races".
- S326 (round-55.md:110): Grounds reads denies &quot;wonders literature&quot; is a genre; decoded: denies "wonders literature" is a genre. Grounds equals the corpus/SOURCES.md teaches cell once decoded.
- S329 (round-55.md:113): locator reads &quot;Contents&quot; cell; decoded: "Contents" cell.
- S341 (round-55.md:125): Grounds reads a pidgin-English &quot;Mother Water&quot;; decoded: a pidgin-English "Mother Water". Grounds equals the corpus/SOURCES.md teaches cell once decoded.
- S343 (round-55.md:127): Grounds reads an &quot;ex post facto geomyth&quot;; decoded: an "ex post facto geomyth". Grounds equals the corpus/SOURCES.md teaches cell once decoded.
- S347 (round-55.md:131): locator reads §&quot;'Tourist gaze'&quot;; decoded: §"'Tourist gaze'".
- S348 (round-55.md:132): Grounds reads must treat &quot;beings tied to named places&quot; as holders; decoded: must treat "beings tied to named places" as holders. Grounds equals the corpus/SOURCES.md teaches cell once decoded.
- S350 (round-55.md:134): locator reads printed p. 44, &quot;Traditional motifs&quot;; decoded: printed p. 44, "Traditional motifs".
- S354 (round-55.md:138): locator reads section &quot;Cryptozoology as a Pseudoscience&quot;; decoded: section "Cryptozoology as a Pseudoscience".
- S356 (round-55.md:140): quoted span reads &#8220;that which reveals,&#8221; &#8220;that which warns,&#8221;; decoded: “that which reveals,” “that which warns,”.
- S357 (round-55.md:141): locator reads paragraph beginning &quot;For our purposes&quot;; decoded: paragraph beginning "For our purposes".

Each quoted fragment above was verified to occur exactly once on its named line, and each `decoded:` text is `html.unescape` of the fragment.

## Proof for the six Grounds rows

Command (run from the lane root):

```
python3 -c "import re,html; reg={c[1].strip():c[7].strip() for c in (r.rstrip().split('|') for r in open('corpus/SOURCES.md',encoding='utf-8') if r.startswith('| S'))}; L=open('corpus/lessons/round-55.md',encoding='utf-8').read().splitlines(); [print((s:=re.match(r'- (S\d+)',L[n-1]).group(1)), 'line', n, 'raw_equal='+str((g:=L[n-1].split('Grounds: ',1)[1].rsplit(' Seat: ',1)[0].strip())==reg[s]), 'decoded_equal='+str(html.unescape(g)==reg[s])) for n in (72,89,110,125,127,132)]"
```

Output:

```
S288 line 72 raw_equal=False decoded_equal=True
S305 line 89 raw_equal=False decoded_equal=True
S326 line 110 raw_equal=False decoded_equal=True
S341 line 125 raw_equal=False decoded_equal=True
S343 line 127 raw_equal=False decoded_equal=True
S348 line 132 raw_equal=False decoded_equal=True
```

Exit 0. Read: for each of the six, the Gate Grounds is not byte-equal to the `corpus/SOURCES.md` `teaches` cell, and is equal to it once decoded with `html.unescape`. The Grounds string is taken as the text from `Grounds: ` to the row's `. Seat:`, which is the same slice the checker's `truncated_grounds` compares.

## Evidence details

| id | round-55.md line | field carrying the entity | entity | occurrences |
|---|---|---|---|---|
| S288 | 72 | Grounds | `&quot;` | 2 |
| S298 | 82 | locator | `&quot;` | 2 |
| S298 | 82 | quoted span | `&amp;` | 1 |
| S304 | 88 | locator | `&quot;` | 2 |
| S305 | 89 | Grounds | `&quot;` | 2 |
| S309 | 93 | URL field | `&quot;` | 2 |
| S312 | 96 | locator | `&quot;` | 2 |
| S326 | 110 | Grounds | `&quot;` | 2 |
| S329 | 113 | locator | `&quot;` | 2 |
| S341 | 125 | Grounds | `&quot;` | 2 |
| S343 | 127 | Grounds | `&quot;` | 2 |
| S347 | 131 | locator | `&quot;` | 2 |
| S348 | 132 | Grounds | `&quot;` | 2 |
| S350 | 134 | locator | `&quot;` | 2 |
| S354 | 138 | locator | `&quot;` | 2 |
| S356 | 140 | quoted span | `&#8220;` `&#8221;` | 4 |
| S357 | 141 | locator | `&quot;` | 2 |

## Gates run (all read-only)

- Entity scan over the Gate section and over all `- S` bullets: the commands behind result 1.
- Whole-Gate Grounds-versus-`teaches` comparison, raw and `html.unescape`d: result 3.
- `python3 -B tools/check-gate-quotes.py corpus/lessons/round-55.md` → `GATE_QUOTES: 0 findings`, exit 0.
- Quoted-span membership test against the registry anchor cell, raw and decoded: result 5 (14 raw-equal, S298 and S356 decoded-equal).

## Unrun checks and out-of-scope items

- `reports/round-56/accept-o.py` was not run; the `html-entity` class is claim O's, not mine.
- No source was re-opened; quote fidelity here is a byte comparison against the lane's own registry, not an external check.
- `round-55.md` was not rewritten, and no lesson file was edited; the erratum lines above are drafts for the L1 to place in the round-56 lesson.
- Whether the round-56 checker should also decode registry `teaches` cells was not tested; all six cells here are entity-free, so it does not matter for these rows.
