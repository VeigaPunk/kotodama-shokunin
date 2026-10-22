# CriticClaimO2 — falsifiers F1-F10 re-run against landed claim O (round 55, falsify wave)

Seat: `KotodamaR55.CriticClaimO2`. The landed tool is `tools/check-gate-quotes.py` at `454a2dc`. I ran it in a sandbox clone at `/fast/scratch/hyaku/kotodama-r55-falsify/CriticClaimO2/lane`. I also re-ran `accept-o.py` at the claim C tip `eb0a331`, and ran the tool read-only on the live working copy.

The scratch directory holds the following:
- `fx/corpus/lessons/gen.md` holds the F2-F8 rows plus the extra rows S973-S983. Its `fx/corpus/SOURCES.md` sits beside it, because the landed truncation rule reads the registry.
- `noreg/gen.md` is the same lesson with no registry.
- `mutate.py` and `mut/` hold 13 mutants of the tool.
- `probe/` holds the rows S990-S992.
- `census/` compares the landed tool with the base tool (`f4015e7`) on all 34 lessons that have a Gate section.

I changed nothing in the lane except this file, and I installed nothing.

## Verdict

**Seven falsifiers pass outright: F1, F2, F3, F4, F8, F9 and F10. F6 and F7 pass once the row carries the `accessed` field the rule anchors on. F5 fails.**

- **F5 is a defect in the tool.** It is a documentation gap: the rule compares everything from the first `Grounds:` up to `. Seat:` as one string. So a truncated first Grounds is never reported, and the docstring does not say so.
- **F6 and F7 fail as literally written**, but only because those fixture rows have no `— accessed <date> — ` field. The docstring states that anchor, so this is a limit of the fixture, not a tool defect.
- **The landed rules differ from the stand-in in the old CriticClaimO report.** The truncated-grounds rule uses the registry: a Grounds is reported when it is a proper prefix of its SOURCES.md `teaches` cell. Because of this, rounds 51-53 stay silent by construction. The 165 false positives that the closure regex would have given do not occur.

The remaining failures are limits of `accept-o.py`, not of the tool, and two of them now have concrete evidence:
- **Mutant M3 shows the KEEP53 gap.** It keeps the length test and drops the prefix test, which puts 7, 76 and 142 false `truncated-grounds` lines on rounds 51, 52 and 53. Selftest still passes 24/24 and `accept-o.py` still exits 0. KEEP53 cannot see these lines because it keeps only `words=` lines.
- **The TRUNC leg depends on an unpinned registry.** Changing one word in the S241 `teaches` cell makes TRUNC fail with `missing=['S241']`.

**I also found three boundary defects in the tool that no falsifier covered.**
- The docstring promises that a complete Grounds sentence is not reported. A complete sentence that copies only the first sentence of a longer `teaches` cell is reported anyway (S973).
- Doubled locators in rows that write `accessed <date> via Wayback … —` are missed (S992). Real Gate rows have this shape, for example `round-50.md:47` S062 and `:49` S064.
- The selftest misses mutants M3 and M5. This is a gap under the claim's own falsifier.

## Falsifiers, one line each

- **F1 — CARRIED (tool).**
  - Rounds 51, 52 and 53 each give output byte-identical to the base tool: 2, 7 and 12 findings, each run exit 1, with 0 `truncated-grounds` and 0 `doubled-locator` lines. Round 53 also matches `reports/round-55/base-gate-r53.txt` apart from the summary line.
  - Across all 34 lessons with a Gate section, only `round-54.md` differs from the base tool.
  - Limit of accept-o: KEEP53 would not catch a regression here. `accept-o.py:107` filters to `words=` lines, and mutant M3 passes all eight legs with 225 false lines on rounds 51-53.
- **F2 — CARRIED.**
  - The real row `round-52.md:115` (S179, which has no Grounds) gets no finding.
  - The synthetic row S967 (`gen.md:12`) gets no finding either. The rule needs `\bGrounds:` (`check-gate-quotes.py:204`).
- **F3 — CARRIED, as long as a registry is present.**
  - With a registry beside the lesson, all four endings are reported as `truncated-grounds`: S962 `reaches T`, S963 `Sanniyä`, S964 `the 17` and S965 `the maker —` (`gen.md:7-10`), plus S972 `(sacrifices` (`gen.md:17`).
  - With no SOURCES.md at `../SOURCES.md` (`noreg/gen.md`), all of them go silent, with nothing on stderr.
  - The docstring states this boundary: "Missing registry files or rows are skipped" (`check-gate-quotes.py:50-51`).
  - The rule only detects a Grounds that copies its `teaches` cell and was then cut. Two limits follow from the documented prefix rule:
    - A paraphrased Grounds that was cut is missed (S974 `the guardian kept the ga`).
    - A case difference is missed (S975 `the keeper was a` against `The keeper was …`).
- **F4 — CARRIED, with a boundary DEFECT.**
  - The single-stop complete row S960 (`gen.md:5`) is silent.
  - Counterexample S973 (`gen.md:18`): the same complete sentence is reported when its `teaches` cell continues as `… not meaning. Its surface form varies by culture.`
  - This contradicts the docstring: "A complete Grounds sentence, including one ending in a single full stop, is not reported" (`check-gate-quotes.py:51-52`).
  - Fix the docstring. Old text: "A complete Grounds sentence, including one ending in a single full stop, is not reported." New text: "A Grounds equal to the whole teaches cell, ending in a single or a double full stop, is not reported; a complete sentence that copies only the opening sentence or clause of a longer teaches cell is reported."
- **F5 — DEFECT (tool documentation).**
  - Row S966 (`gen.md:11`) has a truncated first Grounds followed by ` ; same URL — … Grounds: a complete second ground.. Seat: X.` It gets no finding.
  - The cause is the lazy pattern `\bGrounds:\s*(.*?)\. Seat:` (`:204`). It captures both Grounds as one string, which is never a prefix of the `teaches` cell.
  - Real rows with this shape exist: `round-51.md:36,43,44,45` (S079, S086, S087, S088).
  - None of those Grounds copy their `teaches` cell, so today nothing is lost on real rows.
  - Smallest fix: add a docstring line after line 52: "Only the text from the first `Grounds:` to the row's `. Seat:` is compared, as one string; in a row carrying two Grounds (the round-51 ` ; same URL` shape) a truncated first Grounds is not reported."
- **F6 — CARRIED once the row has an `accessed` field; FAILS as written. This is a fixture limit, not a tool defect.**
  - The literal row S968 (`gen.md:13`, no `accessed` field) is silent, because `doubled_locator` returns False at `:177`.
  - The same row with `— https://example.org/a — accessed 2026-10-22 — ` added (S978, `gen.md:21`) is reported as `doubled-locator`.
  - The docstring states the anchor: "after the `accessed <date> — ` field" (`:45`).
- **F7 — CARRIED once the row has an `accessed` field; FAILS as written. This is a fixture limit.**
  - The curly-quote repeat S969 (`gen.md:14`) is silent without the field.
  - The same row with the field (S979, `gen.md:22`) is reported as `doubled-locator`.
- **F8 — CARRIED.**
  - S970 and S971 are silent without the field, and S980 and S981 are silent with it (`gen.md:15-16,23-24`).
  - S273, whose quote contains escaped quotes, stays silent: there is no round-54 stray finding, and the selftest green case `doubled-locator-s273-escaped-green` passes.
  - Extra near-miss S982 (`gen.md:25`) is a false positive: `§3 'Monsters and marvels', ¶2: "marvels", and later "wonders of the east"`. A one-word real quote that appears inside the section title, followed by another quoted span, is reported as `doubled-locator`. The cause is the plain substring test `quoted_title in locator` (`:191`). The docstring says the span's "text also appears in the locator", so this is a documented boundary. Its likelihood is low, so I record it rather than fix it.
- **F9 — CARRIED as written; GAP once extended.**
  - Deleting each new class rule turns selftest red:
    - M1 (doubled-locator off): exit 1, `SELFTEST: 22/24 pass`.
    - M2 (truncated-grounds off): exit 1, `23/24`.
  - Each new escape rule is also caught:
    - M8 (no guillemets) fails `guillemets-26`.
    - M9 (no star row) fails `star-bullet-26`.
    - M10 (no wrap join) fails `hard-wrapped-26`.
    - M11 (no gap ellipsis) fails `ellipsis-between-spans`.
  - Weakening mutants that survive selftest and `accept-o.py` (both exit 0):
    - **M3**: the truncation test becomes length-only (`and source_teaches.startswith(grounds)` → `and True`). It gives 7, 76 and 142 false lines on rounds 51, 52 and 53. Missing selftest green case, appended to `class_cases` (`:378-386`):
      `("truncated-grounds-shorter-not-prefix-green", lesson("- S900 — p. 1: \"short\". Grounds: the guardian kept the ga. Seat: Scout.\n"), {"S900": "the keeper was a guardian of the gate."}, None),`
    - **M5**: the "another span follows" test is dropped. Probe S990 (`probe/…/p.md:5`, `Section 'Results', ¶1: "Results".`) is then reported. Missing green case:
      `("doubled-locator-single-span-green", lesson("- S900 — URL — accessed 2026-10-22 — Section 'Results', ¶1: \"Results\".\n"), None, None),`
  - **M7** (spans taken from the whole line) also survives, but it is an equivalent mutant: spans before the `accessed` field get an empty `before` string and never match `:\s+$`. It is not a gap.
  - **M13** (case-folded prefix) also survives, but it widens the rule rather than weakening it. That is a design choice, not a gap.
- **F10 — CARRIED (tool).**
  - All 30 round-54 new-class findings print line `n − 216` (30/30), for example `corpus/lessons/round-54.md:63 S279 truncated-grounds`.
  - Limit of accept-o: no leg reads the line number.

## Other attacks on what landed

- **`check-gate-quotes.py:176` — DEFECT, small. Doubled locators are missed in rows that write `accessed <date> (…)` or `accessed <date> via Wayback … —`.**
  - Probe S992 (`probe/…/p.md:7`): `accessed 2026-10-21 via Wayback 20260605210113 — §2 'Methods': "Methods": "the real quote"` gets no finding.
  - 11 of the 401 Gate rows in the corpus do not match the anchor. Examples: `round-50.md:47` S062 and `:49` S064 (`via Wayback`), `round-53.md:33` S185 (`(HTTP 200; …)`), and `round-52.md:34` S096 (`re-opened`).
  - Old: `accessed = re.search(r" — accessed \d{4}-\d{2}-\d{2} — ", line)`
  - New: `accessed = re.search(r" — accessed \d{4}-\d{2}-\d{2}[^—]* — ", line)`
  - I ran the new regex in `mut/W1`:
    - `accept-o.py` passes all eight legs.
    - `round-54.md` still gives 13 `doubled-locator` findings.
    - Every other lesson gives 0.
    - S992, S978 and S979 are reported.
  - The `re-opened` and `attempted` rows stay out of scope, and the docstring should say so.
- **Pinning in `accept-o.py` — limit of accept-o.**
  - The TRUNC verdict reads `corpus/SOURCES.md` `teaches` cells, which are not pinned. In the `regmut/` copy I changed only the first word of the S241 cell (`the mask is …` → `thes mask is …`). The result was `TRUNC FAIL count=16 missing=['S241']`, exit 1.
  - The reverse case is that an in-place errata fix to a round-54 Grounds, or to a `teaches` cell, silently changes what TRUNC measures.
  - Today all the inputs agree:
    - The live working copy's `corpus/SOURCES.md` has uncommitted changes, yet it gives a round-54 output identical to the landed run (30 findings).
    - At `eb0a331` the registry has 357 rows, all with 13 cells, and `accept-o.py` passes all eight legs.
    - The live `round-54.md` sha256 is `5b685de2…0928` and `round-53.md` is `5c0413a7…13d2`, the values the old report recorded.
  - Smallest correction: add both lesson files to `PINS`, and state in the docstring that TRUNC is measured against the S239-S284 `teaches` cells as they stand at the run.
- **`accept-o.py:107` (KEEP53) — limit of accept-o, now confirmed by mutant M3.**
  - Old: `kept = [l for l in r53.stdout.splitlines() if FINDING.match(l) and FINDING.match(l).group(4).startswith("words=")]`
  - New: `kept = [l for l in r53.stdout.splitlines() if FINDING.match(l)]`
  - With this change, M3 fails KEEP53. The landed tool still passes, because its round-53 output equals `base-gate-r53.txt` line for line.
- **Live round-55 draft.** `corpus/lessons/round-55.md` gives `GATE_QUOTES: 0 findings`, exit 0. The draft is uncommitted; this is a read-only run.

## Impacted axes

- **Operability.** The landed tool is a usable gate: there are no new findings on any lesson other than round 54. It has three gaps:
  - It goes silent when no registry is beside the lesson.
  - It misses doubled locators after a Wayback-style `accessed` field.
  - It does not document the non-final-Grounds boundary.
- **Calibration.**
  - The `truncated-grounds` class detects a Grounds that copied its registry `teaches` cell and was then cut. It does not detect truncation in general, and its docstring sentence about complete sentences over-claims (S973).
  - The acceptance cannot tell the landed rule from a length-only rule, because of M3 and KEEP53.

## Unrun checks

- I did not re-run `criterion11-controls-o.py` with the proposed selftest cases or the KEEP53 change applied.
- I did not apply any proposed fix to the lane. The regex widening was exercised only in the scratch copy `mut/W1`.
- I opened no web sources; this review needed none.
