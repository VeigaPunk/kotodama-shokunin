# CriticClaimO — attack on claim O before it lands (round 55, build wave)

Seat: `KotodamaR55.CriticClaimO`. Lane HEAD `8eda954` (declaration), claim base `f4015e7`. I read `reports/round-55/claims.json` (claim O), `reports/round-55/accept-o.py`, `corpus/lessons/round-54-verifier-spotcheck.md` §5, `corpus/lessons/round-54.md` `## Gate` (lines 21-68) and the pre-dispatch report `.ufo/waves/round-55/predispatch/CriticClauseListO.md`. I don't repeat findings that the revised instruments already fixed (the KEEP53 exit status, FORMAT, sha256 pins, two-way reds, and ESCAPE detail pinning).

Work was done in `/fast/scratch/hyaku/kotodama-r55/CriticClaimO/`:
- `scan.py` and `scan.txt` give a per-row Grounds ending and span census for rounds 51-54.
- `standin.py` is a never-landed stand-in checker with five variants.
- `tcopy/` is a `git archive HEAD` copy with the stand-in in place.
- `gen-fixture.md` holds the falsifier rows.
- `rule_b.py` is a convention-aware truncation rule.

I did not change anything in the lane except this file. I installed nothing.

## Verdict

**The two S-id lists are right, but the definitions behind them only hold for one file.**
- Both lists match my own reading of round 54.
- The closure's truncation regex is not a definition. It reads the round-54 double-stop separator by accident. On rounds 51-53 it fires 165 times (7 + 54 + 104 lines), and by my reading every one of those is a false positive.
- `accept-o.py` cannot see any of this. A plausible implementation that emits all 165 false positives passes all eight legs with exit 0 (I ran it; see falsifier F1).
- Three more weak predicates also pass with exit 0: spurious findings on S-ids inside the union, wrong line numbers, and hard-coded S-id lists. SELFTEST passes at base.

## 1. Is `truncated-grounds` well defined?

**My reading of round-54 `## Gate` (46 rows, lines 23-68).** Seventeen rows end their Grounds without a sentence end:

S241 `silent and a`, S242 `valued as mater`, S244 `ridiculed depe`, S248 `the clan carries the`, S250 `second li`, S251 `an ensembl`, S253 `the mask st`, S255 `wax and the`, S259 `a planted bus`, S263 `as a personi`, S264 `on a public`, S265 `the societies, a`, S275 `not wearable ␠`, S276 `is a named ␠`, S277 `so collec`, S278 `and the d`, S279 `and the idiom ␠`.

This is exactly `TRUNC_WANT` (17 = 17, no difference).
- The other 29 rows all end `<word>.. Seat:`. The Grounds carry their own full stop, and the integrator appended `. Seat:` after it (`scan.txt` lines 6-49).
- All 17 truncated Grounds are 218-220 characters long. A length cap is the cause, so a rule based on length is fragile: the pre-dispatch critic showed S263 and S279 are 218 characters.

**Why the regex works only on round 54.** The closure's `[a-z,;] ?\. Seat:` does not detect truncation. It detects a single full stop, which is a truncation only under the round-54 convention. Rounds 51-53 use the Grounds' own full stop as the separator, `… not meaning. Seat:`. There, a single full stop is the normal case for a complete sentence.

| file | closure-regex lines | distinct S-ids | true truncations (my reading) |
|---|---|---|---|
| round-51.md | 7 | 7 | 0 |
| round-52.md | 54 | 36 | 0 |
| round-53.md | 104 | 44 | 0 |
| round-54.md | 17 | 17 | 17 |

**Round-53 hits are all false positives.** I read all 104 endings (`scan.txt` lines 60-183). Every one is a complete sentence or a deliberate label phrase, for example:
- `round-53.md:40` S187 `…an absolute frame decides where the hands go.`
- `:46` S189 `…universality is occurrence, not meaning.`
- `:159` S223 `the same row, the adult half.`
- `:94` S202 is 282 characters and complete.

**Round-52 and round-51 hits are also all false positives, with two special shapes:**
- `round-52.md:115` (`- S179 has a published corrigendum …; cite accordingly. Seat: …`) is a row with **no Grounds at all**. A rule anchored on `Seat:` still fires on it.
- `round-51.md:36,43,44,45` (S079, S086, S087, S088) carry two Grounds per row, with the first one ending in `. ; same URL`. A rule anchored on `Seat:` never examines the first Grounds, so truncation there is invisible.

No other lesson with a Gate section (rounds 5-50, 32 files) has a closure hit.

**The regex also misses real truncations,** even in round-54 convention. It misses a truncation that ends in:
- a capital letter (`reaches T. Seat:`),
- a digit (`dated to the 17. Seat:`),
- a non-ASCII lowercase letter (`at the Sanniyä. Seat:`; round 54 itself writes `Sanniyäkuma`),
- an em dash (`the maker — . Seat:`).

The stand-in misses all four (`gen-fixture.md` rows S962-S965).

**A rule that fits all four files.** In a Gate section where some row ends its Grounds `.. Seat:` (the double-stop convention), flag a row when the Grounds text before `. Seat:` has no terminal `.`, `!`, `?` or `…` of its own. In a single-stop file, report nothing, because truncation cannot be decided from the shape there. I measured this rule (`rule_b.py`):
- round 54: 17 hits, exactly `TRUNC_WANT`;
- rounds 51, 52 and 53: 0 hits each.

It also catches the capital, digit, non-ASCII and em-dash endings by construction. The docstring must state its false-positive boundary: a file that mixes the two conventions, and non-final Grounds (the round-51 ` ; same URL` shape).

## 2. Is `doubled-locator` well defined?

**My reading of round 54.** Thirteen rows put a single-quoted locator name `'X'` and then repeat it as `"X"` before the real quote:

S239, S240, S243, S246, S249, S259, S262, S265, S266, S267, S268, S275, S277.

This is exactly `DOUBLED_WANT`.
- S273 has two straight spans only because of the escaped `\"mask of Agamemnon\"`, and it is not doubled.
- S259 and S262 repeat a paragraph incipit, not a section name. The closure counts them anyway, and so do I.

**Rounds 51-53.** A rule of the form "a `'X'` name repeated as a `"X"` span" gives 0 hits on every other lesson with a Gate section (measured corpus-wide), so that rule is consistent.

The naive rule ("two or more spans before `Grounds:`") gives 20, 31 and 33 hits on rounds 51, 52 and 53. Every one is a false positive: the locator is quoted once, for example:
- `round-53.md:49-50` S189 `§4 "Variation in gesture across languages and cultures": "…"`;
- `round-52.md:41-47` S134 `"Defining Speech Surrogacy", article PDF p. 1: "…"`.

Quoting a locator once is allowed (the round-55 brief: "Never repeat the locator as a quoted string").

**Generalisation gap.** The single-quote rule misses a locator that was already double-quoted and is then repeated: `§2 "Methods", ¶3: "Methods", ¶3: "…"` (`gen-fixture.md` S968, missed by the stand-in). The class needs a definition that does not depend on the quote style: the first quoted span before the real quote repeats text already present in the locator, in any quote style.

## 3. Legs that pass vacuously or check a weaker predicate

I ran these in `tcopy/` with `STANDIN_VARIANT=<v> python3 -B reports/round-55/accept-o.py`.

| variant | what it breaks | accept-o |
|---|---|---|
| `plain` | closure regex for truncation: 7, 54 and 104 false `truncated-grounds` lines on rounds 51, 52 and 53 | **exit 0**, all eight legs PASS (KEEP53 `lines=12 base=12`) |
| `nofalse` | prints a spurious `S265 words=26` on round 54 | **exit 0**: NOFALSE only tests S-ids outside the union of the two sets |
| `line1` | every new-class finding prints line 1 | **exit 0**: no leg reads the line number |
| `hardcode` | new classes come from hard-coded S-id lists, with no rule | **exit 0** |
| `naivedbl` | two-span doubled rule | exit 1 (DOUBLED, NOFALSE and ESCAPE catch S273 and S904); its 33 false `doubled-locator` lines on round 53 are still invisible to KEEP53 |

Leg by leg:

- **KEEP53 is weaker than its intent.** `kept` filters to `words=` lines (`accept-o.py:107`), so any new-class finding on round 53 is unchecked. The base output (`base-gate-r53.txt`) is the complete expected stdout.
- **NOFALSE checks too little.** `stray` (`:106`) only tests S-ids outside the union. A wrong finding on any of the 26 union S-ids passes, whether it is `words=`, an unknown detail word, or a duplicate.
- **DOUBLED, TRUNC and ESCAPE compare sets.** Line number and multiplicity are ignored, so a finding pointing at the wrong line still counts as the shape being "reported". In round 54, row S`n` sits at line `n − 216` (S239 at 23, S284 at 68; checked against the stand-in output).
- **SELFTEST is vacuous for the new classes.** It passes at base (12/12, `claims.json` O `before`), and a stub printing `SELFTEST: 12/12 pass` also passes. That a red and a green case exist for each new class is review-only.
- **Nothing mechanical tests generalisation.** The only input carrying the new classes is round 54, which the lists were derived from, so a hard-coded list passes.
- **The round-53 and round-54 lessons are not pinned.** `PINS` covers only the fixture and `base-gate-r53.txt`. Current sha256 values:
  - round-54.md `5b685de288da64a1e451fcb71b88a881eabcc7ba9465f36d55d25f6925620928`
  - round-53.md `5c0413a74edbd09242d4f4ab9f526b5f863b6860721978ecd6d8409ddf0e13d2`

  An in-place errata fix to round 54 (defect 1 says "file full grounds as errata") would silently change what TRUNC measures.
- **Wording mismatch.** The task brief says "seven legs"; `claims.json` and `accept-o.py` have eight. The falsify-wave brief should say eight.

## Falsifiers for the falsify wave

Each line gives the input, the expected output, and the defect it exposes.

- **F1, round-53 silence.** `python3 -B tools/check-gate-quotes.py corpus/lessons/round-53.md` at the landed tip.
  - Expected: stdout byte-equal to `reports/round-55/base-gate-r53.txt`, meaning 0 `truncated-grounds` and 0 `doubled-locator` lines.
  - Any new-class line is a false positive. The closure regex gives 104.
  - Same check for round 52 (base: 7 findings, exit 1) and round 51 (base: 2 findings, exit 1); the base outputs are in `base-r51.txt` and `base-r52.txt` in my scratch directory.
- **F2, no-Grounds row.** `round-52.md:115` S179 must get no `truncated-grounds` finding.
- **F3, truncation endings the regex misses** (double-stop file, with at least one `.. Seat:` row present). Each of these must give `truncated-grounds`:
  - `Grounds: … reaches T. Seat: X.`
  - `Grounds: … at the Sanniyä. Seat: X.`
  - `Grounds: … dated to the 17. Seat: X.`
  - `Grounds: … the maker — . Seat: X.`
- **F4, complete row in round-53 style.** `Grounds: the register's universality is occurrence, not meaning. Seat: X.` in a single-stop file must give no finding.
- **F5, first of two Grounds truncated.** `Grounds: … created without a. ; same URL — … Grounds: complete.. Seat: X.` The checker must either flag it or its docstring must exclude non-final Grounds explicitly.
- **F6, locator already double-quoted, then repeated.** `- S968 — §2 "Methods", ¶3: "Methods", ¶3: "the quoted sentence itself". …` must give `doubled-locator`; the single-quote rule misses it.
- **F7, curly repeat.** `- S969 — p. 4, 'Results': “Results”: “the quoted sentence itself”. …` must give `doubled-locator`.
- **F8, near-misses that must stay silent:**
  - `- S970 — 'Results', ¶1: "Results are mixed across the sites". …` (the real quote starts with the section name);
  - `- S971 — §4 "Variation in gesture across languages": "An obvious place". …` (locator quoted once; round-53 shape at lines 49-50);
  - S273 with escaped quotes (already covered by NOFALSE).
- **F9, mutation test.** Delete each new class rule in turn. `--selftest` must exit 1 each time. If it exits 0, record a gap (the claim's own falsifier).
- **F10, line numbers.** Every round-54 new-class finding must print line `n − 216` for S`n`.

## Smallest safe corrections, in priority order

1. **KEEP53 compares every finding line.** Change `kept = [l for l in r53.stdout.splitlines() if FINDING.match(l)]` and require `kept == base53`. Add a red control: round 53 gains one `truncated-grounds` line. This alone catches F1 and the `plain` stand-in.
2. **Define `truncated-grounds` by convention, not by the closure regex.** Use the `rule_b.py` rule above (17 on round 54, 0 on rounds 51-53), and document the mixed-convention and non-final-Grounds boundary in the docstring.
3. **Define `doubled-locator` independently of quote style,** so that F6 and F7 are caught and F8 stays silent.
4. **Compare round-54 findings as exact (line, S-id, detail) triples.** Each `DOUBLED_WANT` row is at line `n − 216` with `doubled-locator`, and each `TRUNC_WANT` row likewise with `truncated-grounds`. Nothing else may appear: no `words=` lines and no duplicates. This replaces NOFALSE's union test.
5. **Pin round-53.md and round-54.md by sha256** (values above), or say in the statement that errata are filed elsewhere and never in place.
6. **Make generalisation mechanical.** Pin a second fixture holding F2-F8, with an exact expected finding set. Without it, SELFTEST and the generalisation claim stay review-only, and a hard-coded list passes.

## Impacted axes

- **Operability:** a checker that floods rounds 51-53 with false positives is a worse gate than none, because readers learn to ignore it.
- **Calibration:** the regex that defines truncated grounds detects a separator convention, not truncation, and the leg set cannot tell the difference.

I found no hidden regression in the existing `words=` behaviour: the stand-in's `words=` lines on rounds 51, 52 and 53 are identical to the base tool's.

## Unrun checks

- I did not run `criterion11-controls-o.py` with the proposed controls, or `accept-o.py` with corrections 1 and 4 applied.
- The real landed tool did not exist when I ran this; every run above used my stand-in, which is never landed.
- No web sources were opened (out of scope).
