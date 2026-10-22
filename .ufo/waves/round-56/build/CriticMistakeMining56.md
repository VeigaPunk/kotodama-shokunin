# CriticMistakeMining56 — round 56: where the round-55 Gate HTML entities came from

Seat: KotodamaR56.CriticMistakeMining56 (critic, leaf). Axes judged: operability, calibration.
Everything below was read at claim base `052f145cbcff6996c153d460d81ce346ce74bfbc` unless a scratch path is named. No lane file other than this report was written. No installs.

## Verdict

The round-55 integrator wrote the entities, not a seat and not a stray hand edit. `_gate_text` in `/fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/integrate-rows.py:420-425` deliberately rewrote `&`, `"`, `“` and `”` as `&amp;`, `&quot;`, `&#8220;` and `&#8221;` so that each Gate line would carry one quoted span. The L1 then wrote that choice into the lesson as policy (`corpus/lessons/round-55.md:67`).

The checker's "0 findings" was a correct answer to the rules it had. It had no rule that looks at entities, and decoding alone would not have produced a finding either.

This is the second round in a row where quote marks were rewritten so that a span-shape test would pass. Round 54 switched locator titles to single quotes, which was mined as R55-M1. Round 55 encoded the marks as entities. A falsify seat caught all 16 lines with an exact fix, but the fix was carried to Frontier instead of being applied.

## Evidence

1. **The seats wrote plain text.** Across `.ufo/waves/round-55/build/*.md`, the only file containing an `&name;` or `&#n;` reference is `ExecIntegrateRows55.md`, and only inside its embedded tool source (lines 342 and 640-643). The source lines carry plain marks, for example:
   - `ScoutMonsterTheory.md:34`, the curly quotes around “that which reveals,”
   - `ScoutPareMonsters.md:25`, the plain `& sont`
   - `ReviewRestrictedBeings.md:22`, `§"'Tourist gaze'"`
   - `ScoutCryptozoology.md:161`, `"Traditional motifs"`
2. **The tool encoded on purpose.** The function is at `integrate-rows.py:420-425`: `_gate_text` with the docstring "Encode nested quotation marks so a Gate row has one quoted span". `gate_line` (`:428-436`) applies it to the URL, locator, quote and Grounds. The seat's own report states the intent (`ExecIntegrateRows55.md:6`: "Quote characters ... are HTML-entity encoded ... without extra raw quote spans"). Its line 206 records widening the encoding to URLs to turn its self-built one-span comparison (`compare-round54-gates.py`) green.
3. **15 of the 16 lines are byte-identical to the tool's output.** I loaded the tool read-only, parsed the round-55 seat blocks and regenerated each Gate line with `gate_line`. Fifteen entity lines in `round-55.md` match the generated text byte for byte after the S-id (S288, S304, S305, S309, S312, S326, S329, S341, S343, S347, S348, S350, S354, S356, S357).
   - S298 (`:82`) is the tool's output plus one later hand edit: `à avenir` became `à advenir`, the falsify fix from `.ufo/waves/round-55/falsify/ReviewRowsS295toS299.md:9`.
   - That hand edit touched the line and left its `&quot;` and `&amp;` in place.
4. **The entities began in round 55.** Counting entity-bearing lines inside `## Gate` per lesson gives rounds 49-54: 0, 0, 0, 0, 0, 0, and round 55: 16. Round 55 is the round `_gate_text` arrived.
5. **The encoding was declared policy, not an accident.** `round-55.md:67` reads: "Nested quotation marks inside a quote or a Grounds are written as HTML entities so that a line carries one quoted span."
   - No rule requires one span. `git grep 'one quoted span'` at base finds only this lesson line. QUALITY.md has no such rule, and `tools/check-gate-quotes.py` groups spans into runs by design (docstring "How a quotation is found").
   - The same preamble claims "its Grounds is the row's whole `teaches` cell". At the byte level that is false for six rows (S288, S305, S326, S341, S343, S348), as the verifier spot-check (§3) itself measured.
6. **The checker's silence was not a decoding miss.** I ran the base checker on the committed lesson and on an `html.unescape` copy of it. The copies are in `/fast/scratch/hyaku/kotodama-r56/CriticMistakeMining56/{enc,dec}/corpus/`, each with the base `SOURCES.md` beside it.
   - Both runs give `GATE_QUOTES: 0 findings` and exit 0.
   - The decoded Grounds are equal to their `teaches` cells, not proper prefixes, so `truncated-grounds` correctly stays silent. This matches `.ufo/waves/round-55/falsify/ReviewGateToolCode.md:14`: "none became a prefix after decoding".
   - So the spot-check's §5 item 6 diagnosis, "the checker's whole-teaches comparison does not decode them", names the wrong cause. Nothing in that path would have fired.
7. **Whether the encoding sits in the quote or the Grounds.** Per row, the entity sits only in the Grounds for six rows (S288, S305, S326, S341, S343, S348). For the other ten it sits in the locator, URL or quoted passage.
   - Inside S298 and S356 the quoted passage itself is no longer verbatim: `(&amp; sont`, and `&#8220;that which reveals,&#8221;`.
   - The spot-check's script compared Grounds only. That is why §3 and §5 item 6 say "six" while the real count is 16, the count CriticRestrictedSection gave and claim O's ENTITY leg now uses.
8. **The catch was made and then dropped.** `.ufo/waves/round-55/falsify/CriticRestrictedSection.md:94` names all 16 lines, gives the counting command, and gives the exact fix ("replace `&quot;` with `"` on all 16 lines").
   - The lesson's Falsify section applied other CriticRestrictedSection items (`round-55.md:211`) but filed this one under Frontier (`round-55.md:241`, "HTML entities in 16 Gate lines").
   - In the same commit `173cab6`, the L1 hand-edited S298's line without decoding it.

## Proposed `## Mistakes` row

| id | class and description | evidence | captured-by | fix |
|---|---|---|---|---|
| R56-M? | integration shape (recurrence of R55-M1) — round 55's Gate generator encoded `&`, `"`, `“` and `”` as HTML entities so each line would show one quoted span, and the lesson declared that as policy (`round-55.md:67`). It filed 16 Gate lines with entities; in ten of them the entity sits in the locator, URL or quoted passage, and in two (S298, S356) the quote is no longer verbatim. The checker had no rule for entities and correctly reported 0 findings; a falsify seat's exact 16-line fix was carried to Frontier rather than applied, and the verifier routed it as "six Grounds" with a wrong cause | `integrate-rows.py:420-436` (scratch, round 55); `.ufo/waves/round-55/build/ExecIntegrateRows55.md:6,206`; 15/16 lines byte-equal to regenerated tool output, S298 differs only by the falsify word fix; Gate entity lines per round, rounds 49-54: 0, round 55: 16; `.ufo/waves/round-55/falsify/CriticRestrictedSection.md:94`; `round-55.md:241`; the base checker gives 0 findings on both the committed and the `html.unescape`d lesson | QUALITY none: no rule required plain-text Gate lines or forbade re-encoding quote marks, and no rule required a falsify DEFECT with an exact mechanical fix to be applied or explicitly declined. The falsify seat CriticRestrictedSection did catch it | (a) claim O's `html-entity` class, red before landing (accept-o ENTITY `count=0`), green only at exactly the 16 rows. (b) The round-56 integrator emits plain UTF-8: delete `_gate_text` from `gate_line`. (c) A round-56 erratum for `round-55.md:67` and the 16 lines (filed bytes not rewritten). (d) The Gate rule: a Gate line is plain UTF-8, and a quote span is the source's characters, never a re-encoding of them |

## The fix can be shown to fail

- **Detection, part (a).** This is already declared. `python3 -B reports/round-56/accept-o.py` is ENTITY FAIL (`count=0`) before landing, and its red controls (S357 dropped, S288 on the wrong line, S289 added, S288 doubled) each fail it.
- **Producer, part (b).** This is not covered by claim O and is the live regression risk. I ran it in memory, without writing any file: I loaded the round-55 `integrate-rows.py` and generated Gate lines for the 99 round-55 seat blocks that have a URL, a `teaches` sentence and a quote of at most 25 words.
  - With `_gate_text` as shipped, 23 lines carry an entity.
  - With `_gate_text` replaced by identity, 0 lines carry an entity.
  - The base checker's quote classes give 0 findings on the identity-version lines. Dropping the encoding therefore costs no new finding: the run grouping and `doubled-locator` already handle quoted locators.
  - Failing check after O lands: run `python3 -B tools/check-gate-quotes.py corpus/lessons/round-56.md`. If any Gate line is produced through the old `_gate_text`, it exits 1 with an `html-entity` finding. With the plain emitter it exits 0.
- **Disposition, part (d).** Count falsify items marked DEFECT with an exact replacement whose target bytes are still present at the round tip and that are not listed as declined. Round 55 would have flagged CriticRestrictedSection:94.

## Counterexamples to the routed framing (calibration)

- **Wrong cause.** Spot-check §5 item 6 says the "checker's whole-teaches comparison does not decode them". Decoding the whole lesson still gives 0 findings (evidence 6), so a mistake row that cites "decode" as the cause would give false provenance. The cause is the producer, plus the missing class, plus a dropped falsify fix.
- **Wrong count.** "Six Grounds" undercounts. Ten of the 16 lines carry the entity outside the Grounds, and two of those corrupt the verbatim quote.
- **Latent edge for O's DECODE leg.** This is a bound, not a defect, and no round-55 row trips it. Once a row is decoded, a quoted locator directly followed by `: "` merges into the quote's run.
  - S357 decodes to `"For our purposes": "Monsters ..."`, which is one run of 21 words, 3 of them locator words.
  - A 23-word quote behind a 3-word quoted locator would read as `over-cap`. Raw quoted locators in rounds 49-54 already behave this way, so this is carried behaviour, not new.

## Side observation (outside this mistake)

- The S298 over-read survives in the registry. "gives one birth thirteen causes" is still in SOURCES.md `teaches` (base `corpus/SOURCES.md:327`) and in the Gate Grounds, although `ReviewRowsS295toS299.md:11-12` gave the replacement and `round-55.md:219` records only the entry-side fix. The word fix on the same line was applied.

## Second candidate

R55-M5, the separability export over-breadth, was already mined. It is not repeated here.

## Unrun checks

- I ran neither `accept-o.py` nor `accept-c.py`, nor the round-56 tool after landing.
- The producer check ran in memory against the round-55 integrator only. If the round-56 integration seat (ExecIntegrateRows56) uses a different emitter, it needs the same identity-versus-shipped count.
