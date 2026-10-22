# Round 56 pre-dispatch clause check — claim O (CriticClauseListO56)

Non-author seat, QUALITY criterion 11 (`corpus/QUALITY.md:39`). Claim base `052f145`; draft `reports/round-56/claims.json` and `separability-manifest.json` taken from the worktree (uncommitted).

Scratch: `/fast/scratch/hyaku/kotodama-r56/CriticClauseListO56/repo` is `git archive 052f145` plus the two worktree JSON files, with a throwaway `git init` (scratch HEAD `54912cc`) and `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` unset. Mutant checkers were built by `mkimpl.py <base-tool> <out> <variant>` as patches on the base `tools/check-gate-quotes.py`, each in its own copy of the tree.

No tools were installed or upgraded. I read `/home/vgpnk/.omp/agent/RULES.md` first. Nothing was written in the lane except this report.

## Baseline (confirmed, no defect)

- Base `python3 -B reports/round-56/accept-o.py` exits 1 with ENTITY FAIL (count=0), EXIT FAIL (round55=0 fixture=0), DECODE FAIL (all six missing) and BADUTF8 FAIL (exit=1, Traceback). NOFALSE, KEEP, FORMAT and SELFTEST PASS (27/27). This matches `before` and `expected_pre_landing_counting`.
- `python3 -B reports/round-56/criterion11-controls-o.py repo HEAD` exits 0 and prints `CONTROLS 17/17 as expected`. Each RED fails exactly its own leg, and the others pass.
- **(3) The 16 ENTITY rows are the true set.** I wrote my own scan of the `## Gate` rows in rounds 49 to 55: numeric `&#N;` or `&#xH;`, or `&name;` where `name;` is in `html.entities.html5`. It yields exactly 72 S288, 82 S298, 88 S304, 89 S305, 93 S309, 96 S312, 110 S326, 113 S329, 125 S341, 127 S343, 131 S347, 132 S348, 134 S350, 138 S354, 140 S356 and 141 S357.
  - All 16 are in round 55.
  - S356 uses `&#8220;`/`&#8221;`, S298 uses `&quot;` and `&amp;`, and the other 14 use `&quot;` only.
  - No row in rounds 49 to 55 carries a hex reference (`grep -cE '&#[xX]'` gives 0 for every round).
  - No registry `teaches` cell in `corpus/SOURCES.md` carries a reference.
- **The pins can be reached honestly.** The faithful variant decodes those references and then applies the unchanged base rules. With it, `accept-o.py` exits 0 and all eight legs PASS. It prints exactly the 16 round-55 triples and the 6 fixture triples.
- **(5) The S953 boundary holds for what it tests.** `'T;'`, `'D;'`, `'T'`, `'D'`, `'b'` and `'b=2'` are not in `html.entities.html5`, and `html.unescape(S953 row) == S953 row`.
- **(5) Real bare `&` in rows 49 to 55 that a careless rule would flag:**
  - prose `& `: round-52:71 S143 and round-53:149 S223;
  - URL query parameters: round-51:33, 51, 75, 76; round-52:29, 93, 105, 107, 108; round-53:137; round-54:28, 30.
  
  The careless mutants are caught:
  - `anyamp` (rule `&\S+`) exits 1 with KEEP FAIL on rounds 51–54 and DECODE FAIL (S953 extra).
  - `namedany` (rule `&[A-Za-z][A-Za-z0-9]*;`, no table lookup) exits 1 with DECODE FAIL (S953 extra).
  - `nodecode` (detects but does not decode) exits 1 with DECODE FAIL (S951 truncated-grounds and S955 words=26 missing).

## Findings

1. **Severity: blocks dispatch (criterion 11: a statement word with neither a failing leg nor a review-only entry).**
   - **Statement words:** "reports every Gate row that carries an HTML character reference (numeric, or an HTML5 named reference) as html-entity" (`reports/round-56/claims.json:125`).
   - **Where the clause list falls short:** No clause entry (`claims.json:127-198`) and no `review_only` entry (`claims.json:200-204`) carries these words.
   - **Why no leg can fail on them:** The legs see only `&quot;`, `&amp;` and decimal `&#N;`. That covers ENTITY's 16 rows (`accept-o.py:62-65`) and the fixture rows S951, S952, S954 and S955 (`accept-o.py:66-68`). No input has a hex numeric reference or any other HTML5 name.
   - **Demonstration:** The `narrow` variant detects and decodes only `&quot;|&amp;|&#[0-9]+;`. Running `cd narrow && python3 -B reports/round-56/accept-o.py` passes all eight legs and exits 0.
   - **Probe that separates the variants:** `probe/lessons/shifted.md` adds `S958 … "theta &#x2019;nine&#x2019; ten"` and `S959 … "iota &rsquo;eleven&rsquo; twelve"`. The faithful variant reports `:15 S958 html-entity` and `:16 S959 html-entity` (8 findings, exit 1). The narrow variant reports neither (6 findings).
   - **Minimal fix:** Add two fixture rows, one hex numeric (`&#x2019;`) and one named reference other than quot/amp (`&rsquo;`), with registry rows. Add `(line, S958, html-entity)` and `(line, S959, html-entity)` to DECODE / `FIX_WANT` and to the statement. Then re-pin the fixture sha256s, re-land the instruments, and re-run the control builder at the new claim base.
   - **Weaker alternative:** Move "numeric (decimal or hex) or any HTML5 name" to `review_only`.

2. **Severity: should fix (question 2: a hard-coded implementation passes).**
   - **The gap:** The control builder's own GREEN stand-in (`criterion11-controls-o.py:56-95`) is a hard-coded implementation. It prints the 16 + 6 triples for any path ending in `round-55.md` or `entities.md`, and every leg passes on it (`## GREEN: exit 0`).
   - **Why it passes:** Every positive input to ENTITY and DECODE is a fixed path with fixed lines.
   - **Demonstration:** The same stand-in on a renamed copy of the fixture with one line inserted (`standin/tools/check-gate-quotes.py probe/lessons/shifted.md`) prints `GATE_QUOTES: 0 findings` and exits 0. The faithful variant reports the shifted triples (`:9 S951 html-entity`, `:9 S951 truncated-grounds`, … `:13 S955 words=26`).
   - **Minimal fix:** Add one leg, for example SHIFT. At run time, `accept-o.py` copies the fixture to a temp `lessons/<other-name>.md` with one blank line inserted after the title, and the fixture registry to the temp `SOURCES.md`. It then requires `FIX_WANT` with every line +1 and the path substituted.
   - **What still remains:** S-id hard-coding is then the only shortcut left. That is for the falsify-wave mutation tester, and `review_only` item 3 already names generalisation.

3. **Severity: should fix.**
   - **Statement words:** "applies its quote and Grounds rules to the decoded row" (`claims.json:125`).
   - **What the legs check:** DECODE checks only the over-cap quote rule (S955 `words=26`) and the truncated-grounds rule (S951). The ellipsis-joined and doubled-locator rules (`tools/check-gate-quotes.py:153`, `:183`, `:222-240`) have no decoded-input leg.
   - **Demonstration:** On `probe2/lessons/ell.md`, with the row `S961 … "lambda one &hellip; mu two"`:
     - faithful reports `:5 S961 html-entity` and `:5 S961 words=5` (ellipsis-joined), exit 1;
     - narrow reports `GATE_QUOTES: 0 findings`, exit 0.
     
     The narrow variant already passes all eight legs (finding 1).
   - **Minimal fix:** Add the `&hellip;` fixture row with its two triples to DECODE (it also covers finding 1's named-reference gap), or narrow the statement to "its over-cap and truncated-grounds rules".

4. **Severity: should fix.**
   - **Statement words:** "the html-entity (line, S-id) pairs are exactly …" and "the triples are exactly …".
   - **The gap:** `triples()` builds a set (`accept-o.py:83-85`), so duplicate finding lines collapse. FORMAT only checks that the summary equals the number of lines.
   - **Demonstration:** The `dup` variant prints one html-entity finding per reference instead of per row. `corpus/lessons/round-55.md` then shows S298 three times and S356 four times, with `GATE_QUOTES: 35 findings`. `cd dup && python3 -B reports/round-56/accept-o.py` still passes all eight legs and exits 0. The round-55 summary moves from 16 to 35, which any record citing the finding count would inherit.
   - **Minimal fix:** In ENTITY and DECODE, compare sorted lists (or `collections.Counter`) instead of sets, or make the statement say "once per row".

5. **Severity: should fix (question 5: the boundary is not pinned for semicolon-less names).**
   - **Statement and boundary words:** "an HTML5 named reference", and the `review_only` boundary "an ampersand counts only as a numeric or HTML5 named reference".
   - **What S953 does and does not test:** S953 rules out `&T;`, `&D;` and `&b=2`. It does not test the HTML5 legacy names that need no semicolon (`amp`, `copy`, `reg`, `not`, …, which are in `html.entities.html5` without `;`).
   - **Demonstration:**
     - `html.unescape("https://x.invalid/?a=1&region=eu&copy=2&not=1")` gives `https://x.invalid/?a=1®ion=eu©=2¬=1`.
     - The `legacy` variant uses `html.unescape(ref) != ref` with `;` optional, which is the careless "does it decode?" rule. It passes all eight legs and exits 0.
     - On the S960 probe row (URL `?a=1&region=eu&copy=2`), legacy reports `:17 S960 html-entity` and faithful does not.
   - **Exposure today:** Latent only. No real Gate row in rounds 49 to 54 changes under `html.unescape`. The next registry URL with `&copy=`, `&reg…` or `&not…` would be flagged, and its Grounds or quote mangled.
   - **Minimal fix:** Make the statement and docstring boundary say "a named reference ending in `;`", and add the S960 URL row to the fixture as an unreported boundary row. Or name the semicolon-less case explicitly in `review_only`.

6. **Severity: note (question 4: two leg directions have no red control).**
   - **The gap:** BADUTF8 has four directions: exit 2, a first line starting `GATE_QUOTES_ERROR: `, the path named, and no Traceback. FORMAT's directions include "a summary that counts them". The controls (`criterion11-controls-o.py:96-114`) have no red for "names the path" and none for a summary/line-count mismatch.
   - **The legs themselves do fail:**
     - `nopath` drops the path from the error line: BADUTF8 FAIL, stderr first line `'GATE_QUOTES_ERROR: not valid UTF-8 at byte 81'`, exit 1.
     - `badsum` adds one to the summary: `FORMAT FAIL malformed_runs=['round55', 'fixture']`, exit 1.
   - **The other reds are sound:** each changes one clause alone with a near-miss.
   - **Minimal fix:** Add RED-BADUTF8-PATH (`GATE_QUOTES_ERROR: not valid UTF-8`, exit 2) and RED-FORMAT-COUNT (round-55 summary `17 findings` over 16 lines) to `CONTROLS`.

## Question 1 summary: statement words without a leg

| Statement words | Leg |
|---|---|
| "numeric" (hex) | none (finding 1) |
| "an HTML5 named reference" (beyond quot/amp) | none (finding 1) |
| "applies its quote … rules to the decoded row" | over-cap only (finding 3) |
| "applies its … Grounds rules to the decoded row" | truncated-grounds S951 |
| "answers a lesson that is not valid UTF-8 with exit 2 and a GATE_QUOTES_ERROR line" | BADUTF8 |
| ENTITY, NOFALSE, EXIT, DECODE, KEEP, BADUTF8, FORMAT, SELFTEST leg texts | each matches its clause and leg |

VERDICT: defects found (6)
