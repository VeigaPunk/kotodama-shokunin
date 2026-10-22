# CriticMistakeMining — round 55: the round-54 Gate cut and doubled locators

Seat: `KotodamaR55.CriticMistakeMining` (leaf critic). Judged on: operability and calibration. Lane files read only. Scratch: `/fast/scratch/hyaku/kotodama-r55/CriticMistakeMining/`. No installs or upgrades. No git or jj writes.

## Result

Yes, there was a fixed-width cut, at **220 characters**. The round-54 Gate generator wrote `Grounds: <teaches[:220]>. Seat:`. Every one of the 17 routed rows is a row whose seat `teaches:` text ran past 220 characters, and no other row was cut. The doubled locators came from the same generator. It took the locator up to `: "`, but took the quote greedily from the line's *first* `"` to its last. So any seat locator that contained a double-quoted title was copied into the quote.

The checker reported 0 findings for two reasons:

1. It has no class for truncation.
2. Its three real findings on the first draft (S255, S259 and S262) were cleared by turning the locator's double quotes into single quotes. That hides one copy from the checker's `"…"` regex. The duplicated span itself stays in the line.

The round-54 lesson records those three as "fixed before filing". That is true only of S255.

## Evidence

**The cut is at 220 characters.**
- In the L1 draft `/fast/scratch/hyaku/kotodama-r54-a2/gate-lines.md` (15:44), all 17 truncated Grounds are exactly 220 characters long.
- The longest uncut Grounds is S256, at 214 characters.
- In the landed `corpus/lessons/round-54.md:23-68`, S263 and S279 read 218 characters. That is the same cut with two inner `"` stripped afterward.

**The cut matches the seat `teaches:` lines exactly.**
- For each row, I looked up the seat block through `/fast/scratch/hyaku/kotodama-r54-a2/idmap.tsv` and read its `teaches:` line in `.ufo/waves/round-54/build-a2/*.md`.
- In every row, the Gate Grounds is a prefix of the teaches text.
- The rows whose teaches ran past 220 characters are S241, S242, S244, S248, S250, S251, S253, S255, S259, S263, S264, S265, S275, S276, S277, S278 and S279. That set equals the spot-check's list (`corpus/lessons/round-54-verifier-spotcheck.md:77`). Their teaches range from 224 characters (S242) to 609 characters (S263, 102 words).
- The rows whose teaches ran 220 characters or less are uncut. S257, at 200 characters, is whole.

**The registry is uncut.**
- `corpus/SOURCES.md` holds the full teaches text. For example, S241's cell is 250 characters and ends "…a living orator speaks for him."
- So only the Gate template sliced the text, and the registry can serve as an exact oracle for the Gate.

**A second template defect: a doubled full stop.**
- The template appended `. Seat:` without removing the teaches text's own final full stop. The 29 uncut rows therefore end `owed.. Seat:`.
- This defect is what makes the spot-check heuristic `[a-z,;] ?\. Seat:` work at all (see the attack below).

**How the doubled locators were made.**
- Seat line `ScoutMaskTheory.md:61`: `- "Transformations", ¶1: "draw … a body"`.
- Draft `gate-lines.md:1` reads `"Transformations", ¶1: "Transformations", ¶1: "draw … a body"`.
- Taking the locator up to `: "` and the quote as everything from the first `"` to the last `"` reproduces this exactly. It also reproduces S243 (`ScoutNuo.md:29`), S259 (`ScoutMalagan.md:18`) and S262 (`ScoutSowei.md:40`).
- S255's seat quote has no locator (`ScoutRomanImagines.md:139`), so the draft copied the quote into the locator slot.

**What changed between the draft and the landed lines.**
- `gate-lines.md` was rewritten as `gate-test.md` (15:46), which is the landed text.
- Every double-quoted locator became single-quoted: `'Transformations', ¶1: "Transformations", ¶1: …`.
- Only S255's locator was rewritten for real, to `IMAGO, section 'Jus imaginum'`.
- Inner `"` in the Grounds of S262, S263, S279 and S280 were stripped.

**Checker runs.** I wrapped each draft in a `## Gate` heading and ran `python3 -B tools/check-gate-quotes.py` (sha `81bbef86…`, the same bytes as commit `25375f1`):

| file | result |
|---|---|
| `gate-lines` draft | S255 words=38, S259 words=31, S262 words=26; exit 1 |
| `gate-test` draft | 0 findings; exit 0 |
| landed `round-54.md` | 0 findings; exit 0 |

These match the residual review's §5 (`.ufo/waves/round-54/residual/ReviewGateQuoteTool.md:72-87`). That review asked to "quote the locator title once". Instead, S259 and S262 still carry the duplicated span (S259's run is now 6+19 = 25 words, exactly at the cap).

**The false record.** `corpus/lessons/round-54.md` `## Falsify`, row ReviewGateQuoteTool, says the three runs "were fixed before filing".

**The integrator that was not used.** ExecIntegrateRows' tool (16:18, after landing; `.ufo/waves/round-54/build-a2/ExecIntegrateRows.md:5`) has neither defect:
- `split_quote_line` opens the quote at the `"` that follows `": "`.
- Its `gate_line` writes `Grounds: %s Seat:` with no slicing and one full stop.
- For example, its row S944 (ScoutMalagan-1) has an undoubled locator and 271 characters of Grounds.
- One caveat: its Grounds is the seat's `scope:`, not `teaches:`.

## Proposed `## Mistakes` row

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R55-M1 | integration shape. A Gate generator cut Grounds at a fixed 220 characters and parsed quotes greedily (from the first `"` to the last), so locators holding a quoted title were copied into the quote. The red findings were then cleared by re-quoting the locator (from `"` to `'`), not by removing the copy, and the lesson recorded them as fixed. | `/fast/scratch/hyaku/kotodama-r54-a2/gate-lines.md` (17 Grounds at exactly 220 characters, the full prefix of each seat's `teaches:`; 13 doubled spans) against `gate-test.md` (the quote swap); `corpus/SOURCES.md` teaches cells uncut (S241 250 characters); `.ufo/waves/round-54/residual/ReviewGateQuoteTool.md:72-87`; `corpus/lessons/round-54-verifier-spotcheck.md:77-78` | none. No tool compared Gate Grounds with anything. `check-gate-quotes.py` counts only `"…"` and `“…”` spans, so single-quoting a locator removes it from the count. The round-54 Output asked for `teaches:` "(one line)" with no length cap. QUALITY criteria 1-11 do not cover the shape of a lesson's Gate line. | Generate Gate Grounds from the registry teaches cell, whole, with one closing full stop, and parse the quote as the span opened after `": "`. Add a check: each Gate row's Grounds must equal its `corpus/SOURCES.md` teaches cell, ignoring inner `"`. A fix to a quote-cap finding must change the quoted text, not its quote marks. |

**The proposed check fails and passes.** Probe: `scratch/grounds_vs_registry.py <lesson> corpus/SOURCES.md`.
- On landed `round-54.md`, it reports MISMATCH 17 (exactly S241 … S279 as routed) and exits 1.
- On a copy with Grounds restored from the registry and one full stop (`scratch/round-54-grounds-fixed.md`), it reports MISMATCH 0 and exits 0.
- It does not depend on the doubled full stop or on how a cut word happens to end.

## Attack on claim O's `truncated-grounds` as drafted

Draft: `/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/check-gate-quotes.py`, sha `14d70326…`.

- **Counterexample 1: correct rows are flagged.**
  - `truncated_grounds` (line 170) is the spot-check regex `[a-z,;] ?\. Seat:`. Its docstring (lines 47-50) makes `owed.. Seat:` the clean shape.
  - On the corrected copy (whole Grounds, one full stop), it reports **46 of 46** Gate rows as `truncated-grounds`. On landed `round-54.md` it reports 17.
  - So the class passes only while the round-54 doubled-full-stop defect is present. It would push the round-55 Gate to keep `..`, or report every correct row.
  - The unused ExecIntegrateRows output has one full stop, and 96 of its 105 rows trip the same regex.
- **Counterexample 2: cuts are missed.** On `scratch/trunc-probe.md`, a Grounds cut at a digit (`conventionally 1.`, a cut of "18") is not flagged. A cut after `(see Pliny` is flagged. A character-class test cannot see a cut that ends at a digit or a capital.
- **Counterexample 3: the generator's own output escapes `doubled-locator`.**
  - The class needs the locator title in *single* quotes (`SINGLE_QUOTE`, line 80, used in `doubled_locator`).
  - On the generator's raw pre-swap output (`gate-lines` wrapped), it finds **0** doubled locators, against 13 on the landed file.
  - So it detects the shape only after the cosmetic quote swap, not the defect the generator makes.
- **Impact:** operability (the ACCEPT legs pass on round-54 only because of an unrelated defect) and calibration (`NOFALSE` cannot see this, because the false positives appear only on correct input).
- **Smallest safe correction:**
  - For `truncated-grounds`, compare Grounds with the registry teaches cell, as in the probe. Or at least accept `[.!?]` plus one closure full stop as clean, and add a red-green control on a single-full-stop row.
  - For `doubled-locator`, also match a double-quoted locator title repeated as the next span.
  - Add both corrected copies above as green controls.
- **Verdict:** this is a fixable defect, not a tradeoff.

## Unrun checks

- I did not run `reports/round-55/accept-o.py` or `criterion11-controls-o.py` against the draft tool. That is the O seats' job.
- I did not re-open any source. Quote fidelity is out of scope.
- I did not recover the L1's round-54 generator script itself; it is not in the scratch tree. The 220-character slice and the greedy quote parse are inferred from the outputs, which reproduce exactly on the five seat lines I checked. [INFERENCE] for the code itself.
