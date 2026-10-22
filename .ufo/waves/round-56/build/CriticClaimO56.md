# Round 56 build critic — claim O (CriticClaimO56)

Scope: claim O as declared at `b4b7db9` (instruments at claim base `045f458`; lane tip `456f5ad`). Read: `reports/round-56/claims.json` claim O, `reports/round-56/accept-o.py`, `reports/round-56/fixtures/` (`SOURCES.md`, `lessons/entities.md`, `lessons/bad-utf8.md`), `reports/round-56/base-gate-keep.txt`, `reports/round-56/telemetry/criterion11-controls-o.txt`, `corpus/lessons/round-55-verifier-spotcheck.md:124` (§5 item 6), `corpus/lessons/round-55.md:65-142`, `.ufo/waves/round-56/predispatch/CriticClauseListO56.md` (findings it already raised are not repeated).

Method: sandbox clone `/fast/scratch/hyaku/kotodama-r56/CriticClaimO56/lane` (git env vars unset). `mkvariant.py` there patches the base `tools/check-gate-quotes.py` (sha256 `607acba7…`) into one checker with seven modes, chosen by the `GQ_MODE` environment variable:

| mode | detection | decoding |
|---|---|---|
| `strict` | the claim's rule: `&#N;`, `&#xH;`, or `&name;` where `name;` is in `html.entities.html5` | the matched references only, row only |
| `strictreg` | same as strict | strict, plus each registry `teaches` cell decoded after the cell split |
| `unescape` | same as strict | `html.unescape` of the whole row (the obvious one-liner) |
| `fixpoint` | same as strict | strict, repeated until nothing changes |
| `regsplit` | same as strict | strict, plus each registry line decoded before the cell split |
| `table` | `&quot;`, `&amp;`, `&rsquo;`, `&hellip;` and numeric references only | the same set |
| `sidcheat` | none | none; findings keyed on the 23 S-ids in ENTITY and DECODE |

Probe fixture: `/fast/scratch/hyaku/kotodama-r56/CriticClaimO56/probe/lessons/falsify.md` with its registry `probe/SOURCES.md` (rows S971–S981). The sandbox tool was restored afterwards (sha256 `607acba7…`). Nothing was written in the lane except this report. No tools were installed.

## Headline

**All seven modes pass all eight legs of `accept-o.py` (exit 0), including `sidcheat` and `table`.** Every `SELFTEST` line reads `27/27`, the base count. The legs therefore pin the 16 round-55 rows and the fixture's S-ids. They do not pin the decoding policy, and they do not pin generalisation. The claim's review-only item 3 admits the generalisation gap. The falsifiers below make it testable.

## (1) Decode, or only flag?

**Verdict:** decoding is defensible, but it adds diagnostic completeness, not gate strength. Any row with a reference already fails through `html-entity`. Decoding only surfaces the second finding on that row, such as the hidden 26-word quote in S955 or the truncated Grounds in S951, so the author sees every defect in one run. Its risk is policy drift, and today nothing pins the policy. Measured counterexamples follow.

- **Double encoding (`&amp;quot;`, `&amp;#8220;`).**
  - Probe row S976 (`falsify.md:10`): `&amp;#8220;w0 … w25&amp;#8221;`.
  - `strict` reports `html-entity` only; `fixpoint` adds `words=26`.
  - Single-pass decoding is HTML-correct, because `&amp;#8220;` renders as the literal text `&#8220;`. No leg distinguishes the two policies.
  - In round 55, S298 (`round-55.md:82`) has `(&amp; sont …` inside its quote. Decoding is right there: Paré's text has `&`, and the word count is the same either way (one token).
- **Semicolon-free names inside quote material.** Pre-dispatch finding 5 added S961, but S961 has its names in the URL, outside any quote. So it pins detection only, not decoding.
  - Probe S975 (`falsify.md:9`): `"w0 … w12" &laquo &raquo "w13 … w25"`.
  - `unescape` turns the gap into `« »`, merges the two quotes into one 26-word run, and reports `words=26` **with no `html-entity` finding**.
  - `strict` reports nothing.
  - So the `unescape` checker fails a row and gives no reason a reader can act on.
- **Numeric references without `;`.**
  - Probe S980 (`falsify.md:15`): `&#8220w0 … w25&#8221`. Every HTML5 parser renders this as a curly-quoted 26-word quote.
  - `strict` reports nothing, exit 0: an encoding leak that passes the gate.
  - `unescape` reports `words=26` without `html-entity`.
  - The statement "a numeric reference, decimal or hexadecimal, or a named reference ending in `;`" does not say whether `;` binds the numeric forms. That is a calibration gap.
  - A bare `&#` followed by digits is essentially never benign in prose or URLs; a URL fragment such as `&#s` is not digits.
- **The registry's `&#124;` pipe escapes.**
  - `corpus/SOURCES.md` carries 12 references in 3 rows:
    - S246 (line 275, source cell): the served-page entities `&#100;&#97;&#9532;&#233;`, inside backticks as evidence;
    - S320 (line 349, anchor cell): 5 `&#124;` marking verse line breaks;
    - S361 (line 361, source cell): 2 `&#124;`, including the URL `prop=revisions&#124;proofread`.
  - `&#124;` is the registry's only pipe-escape convention; `\|` has 0 uses.
  - No `teaches` cell carries a reference today, so O's row-only decoding is safe *now*.
  - **Counterexample A (registry decoded before the split).**
    - Mode `regsplit` turns `&#124;` into `|`. The row then has more than 13 cells, and `registry_teaches` drops it silently through its `len(cells) != 13` guard.
    - Probe S979 (`falsify.md:14`; its registry source cell carries `&#124;`): base and `strict` report `truncated-grounds`; `regsplit` loses it.
    - `regsplit` still passes all eight legs.
  - **Counterexample B (row and teaches decoded asymmetrically).**
    - Probe S978 (`falsify.md:13`): Grounds `alpha &#124; beta.`, teaches `alpha &#124; beta and the rest`.
    - Base reports `truncated-grounds`. `strict`, the claim's literal semantics, reports only `html-entity`, so the truncated diagnosis is lost. The row still fails, through `html-entity`.
    - `strictreg` reports both.
  - **A later SOURCES-side check.** If the html-entity rule were reused on `SOURCES.md`, it would misfire on all three rows, and decoding would mangle them:
    - decoding before the cell split breaks the 13-cell grammar (S320, S361);
    - decoding S246 destroys its evidence.
  - Such a check must split cells first, exempt backtick code spans, and either accept `&#124;` as the table pipe escape or migrate the registry to `\|`. It also needs a `check-source-access.py` and sweep audit, which I did not run.
- **References inside URLs in Gate rows.** A copied href such as `?a=1&amp;b=2` is flagged, and the decoded URL is the real one. That is a true finding (the Gate is plain UTF-8 text) and correct semantics. Bare query `&` in rounds 51–54 (12 rows, listed by the pre-dispatch critic) stays unflagged under all five decoders: KEEP passes for each.

## (2) Can a hard-coded implementation pass?

**Yes, measured.**

- **S-id cheat.** `sidcheat` detects nothing. It emits the expected findings when the row's S-id is one of the 16 round-55 ids or S951/952/954/955/958/959/960. Result: `ENTITY PASS … DECODE PASS … moved_exit=1 moved_missing=0 … SELFTEST PASS 27/27`, exit 0.
  - The run-time moved copy defeats only path and line keys; it keeps the S-ids.
  - On a renumbered copy (S95x→S99x and S96x→S98x in both the lesson and its registry), `strict` reports the expected 10 findings and `sidcheat` reports `GATE_QUOTES: 0 findings`.
- **Narrow table.** `table` detects and decodes only quot, amp, rsquo, hellip and numeric references, and also passes, exit 0.
  - On the probe it misses S971 (`&ldquo;…&rdquo;` around a 26-word quote: both `html-entity` and `words=26`), S972, S973 and S974.
  - It also passes the renumbered copy, so renumbering alone does not close this gap.

## (3) Legs that pass vacuously

- **SELFTEST.** It passes at base (27/27) and on every mutant. No leg requires a selftest case for the new class. A landing that does not touch the selftest passes, so review-only item 2 is the only guard.
- **NOFALSE.** It cannot fail for any decoding policy tested.
  - The 6 round-55 Grounds with references (S288, S305, S326, S341, S343, S348) differ from their teaches cells before decoding and **equal** them after decoding. "Equal" is excluded from `truncated-grounds`, so no prefix arises.
  - The 10 others have their references in locators. Each decoded locator quote is separated from the real quote by prose (letters), so no run merges.
  - All 5 real decoders print 0 strays. NOFALSE catches only fabricated output, which is what RED-NOFALSE is.
- **KEEP.** Rounds 49–54 print identical output under every mode, including `unescape`, `fixpoint`, `regsplit` and `table`. So KEEP guards unrelated regressions only and pins no decoding policy.
- **BADUTF8.** It is single-path only.
  - A mutant that stops at the first undecodable file (`continue` changed to `break`) passes all eight legs.
  - On `bad-utf8.md round-55.md` that mutant prints `GATE_QUOTES: 0 findings`, exit 2: round 55's 16 findings are silently dropped. `strict` prints all 16, exit 2.
  - Invalid UTF-8 in the *registry* is still swallowed (`registry_teaches` catches `UnicodeError` and returns `{}`), which silently disables `truncated-grounds`. That is out of the claim's words: a tradeoff, not a defect.
- **DECODE.** It is not vacuous, but the Grounds rule is exercised only through `&quot;` (S951). A checker that adds `&quot;` to the quote-stripping regex in `comparable_teaches`, without decoding, gets S951 right. Probe S973 (`&mdash;` in Grounds, teaches `Alpha—beta and the rest`) separates the two: `strict` reports `truncated-grounds`, and `table` misses it.

## (4) Other lessons that gain findings after O lands

- All 35 `corpus/lessons/*.md` with a `## Gate` heading were run under the base tool and under strict, strictreg, unescape, fixpoint and regsplit.
- **Only `corpus/lessons/round-55.md` changes**, in every mode: base exit 0 with 0 findings, then exit 1 with 16 findings. The diff of the base and strict runs over all 35 files is exactly +16 `html-entity` lines (51 → 67 findings), with no other class added or lost.
- **All 16 are true.** Each row physically carries `&quot;`, `&amp;` or `&#8220;`/`&#8221;` (`round-55.md:72, 82, 88, 89, 93, 96, 110, 113, 125, 127, 131, 132, 134, 138, 140, 141`). This matches the pre-dispatch critic's independent scan.
- Six of the 16 are the spot-check's "six Grounds" (§5 item 6). The other ten have references in locators (`§ beginning &quot;…&quot;`) or quotes (S298, S356). The spot-check routed six; the claim flags 16. The extra ten are true, not over-reach, but the lesson should say why the count differs from the routed six.
- No other round's Gate (1–32, 49–54, supplements) carries a reference, so no other lesson gains a finding.

## Falsifiers for the falsify wave

Each one is runnable from the sandbox. Each names the expected output under the claim's semantics; the `strictreg` mode in this report's scratch is the reference I propose.

1. **S-id generalisation.** Run the landed tool on the renumbered copy (fixture plus registry, S95x→S99x and S96x→S98x). It must print the 10 DECODE triples with the new ids. A shortcut keyed on S-ids prints 0 findings.
2. **Named reference outside the four** (probe S971): `&ldquo;w0 … w25&rdquo;` must give `html-entity` and `words=26`.
3. **Decoding before word count** (probe S972): a 26-word quote with one `&nbsp;` join must give `html-entity` and `words=26`. Python's `str.split()` splits on U+00A0, so the undecoded row counts 25 words.
4. **Grounds decoding beyond `&quot;`** (probe S973): `Grounds: Alpha&mdash;beta.` against teaches `Alpha—beta and the rest` must give `html-entity` and `truncated-grounds`.
5. **Case-sensitive HTML5 name** (probe S974): `&QUOT;` must give `html-entity`.
6. **Semicolon-free legacy names in quote material** (probe S975): must print **no** finding. A checker that prints `words=26` with no `html-entity` is decoding outside the claim's own definition.
7. **Double encoding** (probe S976): must give `html-entity` only, from one decoding pass. `words=26` means repeated decoding.
8. **Reference on a continuation line** (probe S977, `falsify.md:11-12`): must give `html-entity` at line 11, the row's first line.
9. **Registry split before decode** (probe S979, `&#124;` in the registry source cell): `truncated-grounds` must survive.
10. **Symmetric teaches decoding** (probe S978): `strict` prints `html-entity` only; base and `strictreg` also print `truncated-grounds`. This is a decision for the L1, not a leg failure: the statement decodes "the row" only.
11. **Numeric reference without `;`** (probe S980): `strict` exits 0 on a rendered 26-word quote. The claim must decide whether this is a reference, and pin the answer with a fixture row.
12. **Invalid code points** (probe S981: `&#0;`, `&#xD800;`): `html-entity` is expected under the statement, and the decoded value is U+FFFD. The docstring should say so.
13. **Multi-path UTF-8 error.** `tools/check-gate-quotes.py reports/round-56/fixtures/lessons/bad-utf8.md corpus/lessons/round-55.md` must print all 16 round-55 findings, then the `GATE_QUOTES_ERROR` line, and exit 2.
14. **Selftest mutation.** Remove the new class from the landed selftest, or make `has_ref` always false: `--selftest` must exit 1. If it exits 0, record the gap, as the claim's own falsifier says.

## Impacted axes and smallest safe corrections

- **Operability** (the claim's own axis): the legs pass for five decoding policies and two shortcuts.
  - Smallest correction inside the existing leg design: extend the DECODE moved copy to rewrite S-ids in the lesson and its registry, which closes `sidcheat`.
  - Add fixture rows for falsifiers 2, 6 and 7, plus 3 or 4. They close `table`, `unescape` and `fixpoint`.
  - Require `SELFTEST: n/n` with n > 27.
  - Each of these needs new pins and a re-run of the control builder, so either it is a re-declaration, or it goes to the falsify wave as falsifiers. It cannot be folded silently into the landing.
- **Calibration:**
  - Write in the statement and docstring whether `;` is required for numeric references (falsifier 11).
  - Make single-pass decoding explicit (falsifier 7).
  - Make the lesson explain 16 found against the 6 routed.
- **Latent, no current exposure:** registry pipe escapes (falsifiers 9 and 10) and any future SOURCES-side entity rule. Decode the `teaches` cell with the same decoder *after* splitting cells, and never decode a registry line before the split.

**Unrun:** `check-source-access.py` and the README sweep against a hypothetical `\|` migration; mutation of an actually landed selftest (nothing has landed yet).
