# RevLessonFinal — attacking the Gate-row checker before `corpus/lessons/round-65.md` exists

Seat: RevLessonFinal (attack). Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base revision `17c32302c6845c8f164b985a8cb312d3181c8788`. Subject: `tools/check-gate-quotes.py`
(587 lines, sha256 `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`
— measured by `sha256sum` at attack time) and the `QUOTES` leg of `reports/round-65/accept-ca.py`
(lines 172-178), which requires `exit=0` and `"0 finding"` in the child's stdout for
`corpus/lessons/round-65.md`.

Method: 50+ single-row fixtures built against a private corpus (`lessons/round-65.md` +
`SOURCES.md` with a known `teaches` cell), each run through the real tool
`python3 -B tools/check-gate-quotes.py <fixture>` and, for the leg-level cases, through the real
`python3 -B reports/round-65/accept-ca.py --root <fixture-root>`. Fixtures lived in `/tmp`
(ephemeral, `rm -rf` after each case); nothing was written to the lane repo except this report.
`--selftest` on the lane's bytes prints `SELFTEST: 52/52 pass`.

The purpose of every line below is the same: the `QUOTES` leg must print `0 findings` on the
assembled lesson, so each shape here is a shape the scribes must **not** write. §A is the shape
that passes. §B is every shape measured to trip, one example row each. §C is every shape that
**passes while violating the rule** — the attack surface, by severity. §D is the scribe
pre-flight. §E is residual risk.

Dependency recorded, not waited on: `corpus/lessons/round-65.md` does **not** exist at attack time
(measured; no S750-S775 row either in `corpus/SOURCES.md`). The live `QUOTES` leg on the lane's bytes
therefore reads `QUOTES FAIL exit=2 out=['GATE_QUOTES: 0 findings']` — the counter's own detail line
carries the clean summary beside a FAIL, which is §C-2 in one string.

## A. The shape that passes (write every row this way)

Round-56's rows are the working precedent (`corpus/lessons/round-56.md` → `GATE_QUOTES: 0 findings`,
verified). One row, one physical line, unquoted locator prose, one quoted span, full `Grounds`,
`. Seat:` before the seat name:

```
- S750 — <url> — accessed 2026-10-24 — <locator prose, unquoted, ending in ":">: “<≤25-token verbatim quote>”. Grounds: <the row's whole teaches cell>. Seat: <SeatName>.
```

Parsing facts that follow from the code (`QUOTE` L104, `quote_run_details` L153-172,
`gate_rows` L278-297, `accessed` L217):

- The row is only read if it matches `ROW` (L102) `^(?:-\s+(?:\*\s+)?|\*\s+)(S\d+)\b` **at column 0**.
  `- S750`, `- * S750`, `* S750` are read; nothing else is.
- Continuation lines are joined only when the next physical line starts with whitespace and is
  non-blank; a blank line, an unindented line, or a new bullet ends the row.
- Only the **first** `## Gate…` section is scanned, and the next line matching `^## ` closes it.
  `### ` does **not** close it. The heading must be `## Gate` or `## Gate <anything>`;
  `## The Gate` produces *no Gate section* (exit 2).
- A quoted span separated from the next quoted span by punctuation/whitespace only is **one run**;
  any letter, digit or underscore in the gap splits it. So `"Title": “body”` is one quotation.
- Word count is whitespace tokens of the span text: `mother-in-law` = 1, `(39%)` = 1, `[sic]` = 1,
  and a spaced em/en dash `—`/`–` = 1. Exactly **25 passes; 26 fails.**
- Nothing else on the row is read: tier, date, status, `used-by` are invisible to this tool.

## B. Every shape measured to trip (one example row per shape)

Each "measured" line is the tool's own output line for that fixture. `L` is the fixture lesson.
Controls that stay green are listed too, so nobody over-corrects.

### B1. over-cap (7 shapes; `words=<n>`)

| # | shape | example row (body only; wrap with `- S750 — https://e.test/a …` as in §A) | measured |
|---|---|---|---|
| 1 | 26 tokens inside one straight span | `p. 4: "w0 w1 … w25".` | `S750 words=26` |
| 2 | same in curly quotes | `p. 4: “w0 w1 … w25”.` | `S750 words=26` |
| 3 | same in guillemets | `p. 4: «w0 w1 … w25».` | `S750 words=26` |
| 4 | quoted locator title adjacent to the body quote, gap `: ` only | `Table 2 "Counts of pointing forms used": "w0 … w20".` | `S750 words=26` (5+21 merged) |
| 5 | quote hard-wrapped across two indented physical lines | `p. 4: "w0 … w12`<br>`␣␣w13 … w25".` | `S750 words=26` |
| 6 | two quoted spans with a space-only gap | `p. 4: "w0 … w12" "x0 … x12".` | `S750 words=26` |
| 7 | 24 real words that tokenise to 26 because of spaced dashes | `p. 4: "w0 … w10 — x0 … x10 — y0 y1".` | `S750 words=26` |

Shape 7 is the live precedent in this lane: `corpus/lessons/round-58.md:40` S506 is
`words=26` today on a quote whose text reads as ~24 words —
`“ordered the Board on Geographic Names – the federal body tasked with naming geographic places – to implement procedures …”`
(the two spaced en dashes are tokens). `corpus/lessons/round-58.md:87` S569 is `words=30`.
So `corpus/lessons/round-58.md` alone does **not** print 0 findings; the round-65 lesson must not
inherit that style.

Green controls (do not "fix" these): exactly 25 tokens; `mother-in-law`/`twenty-six` as single
tokens; a hyphenated-25 row; a quote with a leading or trailing `…`; bare `&` prose (`AT&T`, `R&D`,
`&notaref;`); two quotes separated by prose (`"…" and next: "…"`) even when their tokens sum past 25.

### B2. ellipsis-joined (4 shapes)

| # | shape | example | measured |
|---|---|---|---|
| 8 | ellipsis inside one span joining two fragments | `Abstract: "the first two … have recognition as emblems".` | `S750 words=8` (`ellipsis-joined`) |
| 9 | ellipsis between two spans, punctuation-only gap | `Abstract: "alpha bravo charlie" … "delta echo foxtrot".` | `S750 words=6` |
| 10 | three dots instead of `…` | `p. 4: "alpha bravo ... charlie delta".` | `S750 words=5` |
| 11 | ellipsis with no spaces around it | `p. 4: "alpha…bravo".` | `S750 words=1` |

Rule: any `…`/`...` with non-blank text on **both** sides trips. A leading/trailing marker does not.
If the source sentence itself elides, quote a contiguous run of the source instead of reproducing
the elision, or accept the finding and get it reviewed — the leg has no waiver path, so it must be
avoided by wording, not by annotation.

### B3. doubled-locator (5 shapes; reported as `doubled-locator`, no word count)

| # | shape | example row | measured |
|---|---|---|---|
| 12 | locator section name in single quotes, then the same text as the first quoted span | `section 'Transformations', ¶1: "Transformations", ¶1: "draw an ontological distinction".` | `S750 doubled-locator` |
| 13 | same with the title double-quoted | `"Results", ¶2: "Results", ¶2: "the effect was large".` | `S750 doubled-locator` |
| 14 | same with the `via Wayback <id>` access note | `… — accessed 2026-10-21 via Wayback 20260605210113 — §2 'Methods': "Methods": "the real quote".` | `S750 doubled-locator` |
| 15 | title on line 1, body quote on the indented continuation | `§2 'Methods':`<br>`␣␣"Methods": "the real quote".` | `S750 doubled-locator` |
| 16 | any one-word quote that also occurs anywhere in the locator text before the first `: ` | locator `Abstract` + `"Abstract"` | `S750 doubled-locator` |

The test is a plain substring test (`doubled_locator` L215-232): the **first** span whose preceding
text ends in `: ` is the "title"; it is red iff that span's text is a non-empty substring of
everything between ` — accessed … — ` and the colon. Consequence: **never put a quoted span before
your body quote**, and never start the body quote with the locator's own words. Round-54 still
carries 13 rows of this class (measured: `check-gate-quotes.py corpus/lessons/round-54.md` →
`13 doubled-locator`).

### B4. truncated-grounds (3 shapes; reported as `truncated-grounds`)

| # | shape | example | measured |
|---|---|---|---|
| 17 | Grounds is a proper prefix of the S-id's registry `teaches` cell | `Grounds: the keeper was a. Seat: X.` vs teaches `the keeper was a guardian of the gate.` | `S750 truncated-grounds` |
| 18 | same truncation, quote marks around it — delimiters are stripped before comparing | `Grounds: "the keeper was a". Seat: X.` | `S750 truncated-grounds` |
| 19 | same truncation after an HTML reference is decoded | `Grounds: the keeper was a&hellip;. Seat: X.` | `S750 html-entity` (and the decode feeds the prefix test) |

Green controls: Grounds **equal** to the whole teaches cell, ending in one or two full stops
(`the keeper was a guardian of the gate.`); Grounds that is shorter but not a prefix
(`the guardian kept the ga.`); Grounds longer than teaches (see §C-6 — that is a blind spot, not a
licence).

The comparison is `registry_teaches` (L193-212) reading `../SOURCES.md` relative to the lesson file,
`cells[7]` of a row that `split("|")` into **exactly 13** cells. Round-65 rows S750-S775 therefore
must carry a complete, single-line `teaches` cell and a Gate Grounds that is either the whole cell or
not a prefix of it.

### B5. html-entity (7 shapes; reported as `html-entity`, once per row)

| # | shape | example | measured |
|---|---|---|---|
| 20 | numeric decimal, **no semicolon needed** | `p. 4: "caf&#233 bar".` | `S750 html-entity` |
| 21 | numeric hex | `p. 4: "caf&#xE9; bar".` | `S750 html-entity` |
| 22 | named reference with semicolon | `p. 4: "one &copy; two".` | `S750 html-entity` |
| 23 | `&amp;` in a citation URL's query string — the most likely accidental hit | `- S750 — https://e.test/x?a=1&amp;b=2 — …` | `S750 html-entity` |
| 24 | encoded quote marks around an over-cap quote | `p. 4: &#8220;w0 … w25&#8221;.` | `S750 html-entity` + `S750 words=26` (2 findings) |
| 25 | invalid code point still counts | `p. 4: &#0;` | `S750 html-entity` |
| 26 | double-encoded entity decodes once, then still counts | `p. 4: "one &amp;hellip; two".` | `S750 html-entity` |

This is the round-55/56 heredity: `corpus/lessons/round-55.md` prints `16 html-entity` today
(measured), the residue of an integration tool that entity-encoded `&`, `"` and curly quotes
(R56-M1). Green controls: bare `&` (`AT&T`, `R&D`, `?a=1&b=2`), `&notaref;` (unknown name),
`&#;`/`&#x;` (malformed), and a short quote with no other defect (`&#8220;one two&#8221;` still trips
`html-entity` alone — it is **never** green once a reference exists).

### B6. document-level shapes (no row needed)

| # | shape | measured |
|---|---|---|
| 27 | no `## Gate` section (e.g. heading written `## The Gate`) | `GATE_QUOTES_ERROR: … no '## Gate' section` on stderr, **`GATE_QUOTES: 0 findings` on stdout**, exit 2 |
| 28 | lesson not valid UTF-8 | `GATE_QUOTES_ERROR: … not valid UTF-8`, exit 2 |
| 29 | Gate row placed before any `## Gate` heading, or after a `## ` heading inside the section | row not scanned, exit 0 |
| 30 | Gate-shaped table (`\| S750 \| url \| date \| "quote" \|`) | **0 findings, exit 0** — see §C-3 |

## C. Attack findings (shapes that pass while violating the rule)

Severity is mine; every line is measured, not inferred.

**C-1 (HIGH) — the `QUOTES` leg is satisfiable with zero Gate rows; it certifies nothing about
coverage.** A lesson whose Gate body is `(no rows yet)` prints `GATE_QUOTES: 0 findings`, exit 0, and
`accept-ca.py` prints `QUOTES PASS exit=0 out=['GATE_QUOTES: 0 findings']`. So the frozen predicate
`ACCEPT-CA-65: every leg … prints PASS` can be green while `corpus/lessons/round-65.md` contains no
Gate row at all, and equally while it contains rows for none of S750-S775. This is R64-M10's
control-vacuity class reproduced in a new instrument. Fix before the leg is cited: require the
lesson's Gate to contain all 26 ids the claim names (`S750`…`S775`) — one line per id, matching `^- S7(5[0-9]|6[0-9]|7[0-5])\b` — and require `>= 26` rows. As it stands the leg measures
formatting of whatever happens to be there, never presence.

**C-2 (HIGH) — the error path prints the clean summary on stdout.** With the heading written
`## The Gate`, the tool writes `GATE_QUOTES_ERROR: … no '## Gate' section` to stderr and
**`GATE_QUOTES: 0 findings` to stdout**, exit 2. Any seat, receipt, or transcript that shows the last
stdout line (the natural `| tail -1`) reports a false green on a document that was never evaluated.
The counter survives only because `r_quotes` also tests `q.returncode == 0` (L177). Two consequences:
a Gate fragment reviewed by stdout alone can be stamped clean while unparsed; and the scribes must
never paste a `tail -1` line as evidence — paste `exit=$?` with it. Fix in the tool: on any unreadable
document print `GATE_QUOTES: ERROR`, not a finding count, or suppress the summary when `errors`.

**C-3 (MED) — five row shapes are invisible; a 40-token quote passes in all of them.** Measured,
each exit 0 / `0 findings` with a deliberately 40-token span:

1. `- **S750** — …` (bolded id): `ROW` requires `S\d+` directly after the bullet.
2. `  - S750 — …` (bullet indented — measured at two spaces; `ROW` anchors at column 0).
3. `| S750 | url | date | "quote" |` (Gate written as a table): no bullet, never scanned.
4. An **unindented** continuation line: the row closes at the end of line 1, so a quote that starts
   on line 2 is never read (indented continuations are joined; unindented ones are not).
5. A blank line inside the row: same effect, mid-row.

Add: a **second** `## Gate` section is never scanned (`gate_section` takes the first heading match
and stops at the next `^## `), so a "Gate (continued)" block is entirely unchecked while stdout says
`0 findings`. Scribes must keep all 26 rows in the one first `## Gate` section, as plain
column-0 `- S7NN — ` bullets, one logical row per row.

**C-4 (MED) — doubled-locator is disabled by three innocent-looking restyles of the access field.**
Measured red→green pairs on the same doubled title:

| access field | result |
|---|---|
| `— accessed 2026-10-24 —` | `doubled-locator` (red) |
| `– accessed 2026-10-24 –` (en dashes) | `0 findings` (green) |
| `— accessed 24 Oct 2026 —` (word date) | `0 findings` (green) |
| no `accessed` field at all | `0 findings` (green) |

The class is gated on ` — accessed \d{4}-\d{2}-\d{2}[^—]* — ` (`doubled_locator` L217-219), so any
reformatting of the date/dash pattern silently removes the only check that sees a repeated locator
title. The scribes' canonical form (§A) is exactly the form that keeps it armed; a seat that
"tidies" the row to en dashes or a prose date disarms it for every row it touches. Record this in the
round-65 lesson as a scope caveat rather than claiming the class always runs.

**C-5 (MED) — truncated-grounds is disabled whenever the registry row does not parse, including
before the registry rows land.** Measured: with the lane's **real** `corpus/SOURCES.md` (S750 absent)
a Gate row with `Grounds: portrait of a miner. Seat: X.` prints `0 findings`; the same row with S750
present prints `truncated-grounds`. Also green:

| condition | measured |
|---|---|
| `teaches` cell contains a `\|` (row splits into 14 cells, `registry_teaches` skips it) | `0 findings` |
| S-id has no row in `../SOURCES.md` | `0 findings` |
| `. Seat:` marker written `; Seat:` or `— Seat:` | `0 findings` |
| a second `Grounds:` clause before `. Seat:` (span absorbs it, not a prefix) | `0 findings` |
| Grounds truncated but marked with `…` at the cut | `0 findings` |

Consequence for the wave: the `QUOTES` leg has teeth for the truncation class **only after** the 26
registry rows are in `corpus/SOURCES.md` with pipe-free single-line `teaches` cells and the Gate rows
carry the literal `. Seat:`. Run the leg after the registry lands, and treat a pre-registry green as
no evidence. This is the same ordering class as R64-M1.

**C-6 (LOW) — truncated-grounds only sees truncation, never invention.** Grounds equal to teaches
plus an invented tail (`… guardian of the gate and also a thief.`) and Grounds with reordered wording
both print `0 findings`. A scribe can pass the leg with a Grounds that says something the teaches cell
never said. Support review (the R64-M7 overreach class) remains the only check — the leg must not be
described as certifying Grounds fidelity.

**C-7 (LOW) — over-cap is bypassable by putting a word, digit or underscore in the gap.** Measured:
`"Table 2 counts" ¶4: "w0 … w22"` = 26 tokens across two spans but `0 findings`, because `¶4` puts a
digit in the gap (`WORDISH` L106, `quote_run_details` L160-166). The same two spans with the gap `: `
are `words=26` red. So "two quotations" is a formatting property, not a reading: a row can carry 26+
tokens of quotation as two adjacent spans with any word between them. This is legitimate when the
quote really is two quotations; it must not be used to launder a single over-long quote.

**C-8 (LOW) — the leg's stdout test is an unanchored substring.** `r_quotes = q.returncode == 0 and
"0 finding" in q_out` (accept-ca L177). The string `"0 finding"` is a substring of `"10 findings"`;
measured with ten over-cap rows the tool prints `GATE_QUOTES: 10 findings` and the substring test is
literally satisfied — the leg still FAILs only because the exit code is 1. If the exit contract ever
changes (or a wrapper normalises the code), ten findings would read as PASS. Fix: test
`q_out.rstrip().endswith("GATE_QUOTES: 0 findings")` and drop the substring form.

**C-9 (INFO) — the leg reads only `corpus/lessons/round-65.md`.** Every draft Gate fragment under
`.ufo/waves/round-65/` is unchecked, and a scribe's fragment has no `../SOURCES.md` beside it, so even
a manual run there leaves truncated-grounds silent (measured: `0 findings` for a deliberately
truncated Grounds). The recipe in §D-3 fixes that within the wave's write scope.

## D. Scribe pre-flight (run this before handing a row or the lesson up)

1. **Write the shape of §A.** One physical line per row, `- S7NN — ` at column 0, unquoted locator
   prose ending in `:`, one quoted span, `. Grounds: <whole teaches cell>. Seat: <name>.`
2. **Count tokens, not words.** ≤25 tokens by whitespace split; spaced dashes, `[sic]`, `(39%)` and
   bracketed editorial marks each cost a token. 25 passes, 26 fails. Prefer 24 or fewer.
3. **No quoted span before the body quote**, and no bolded/indented/table row — the checker either
   reports it or silently skips it, and a silent skip is the worse outcome.
4. **Never write an ellipsis** inside or between spans. Split the quotation or pick a contiguous run.
5. **No HTML references anywhere on the row** — not in the quote, not in Grounds, not in the URL
   query (`&amp;`, `&#233`, `&#xE9;`, `&copy;`, `&hellip;`). Copy the URL with a bare `&`.
6. **Keep `— accessed 2026-10-24 — ` byte-exact** (em dashes, ISO date). Restyling disarms
   doubled-locator (C-4).
7. **Grounds = the row's whole `teaches` cell** (or a text that is not a prefix of it), copied from
   `corpus/SOURCES.md` after the registry row lands, with the literal `. Seat:` after it. Never end a
   Grounds mid-word, never insert `…` at the cut, never add a second `Grounds:` clause.
8. **One `## Gate` section.** All rows in the first one; no "Gate (continued)", no Gate table.
9. **Run the tool on the assembled lesson and keep both lines of evidence:**
   ```
   python3 -B tools/check-gate-quotes.py corpus/lessons/round-65.md; echo "exit=$?"
   ```
   The acceptable pair is `GATE_QUOTES: 0 findings` **and** `exit=0`. A `0 findings` line with
   `exit=2` is an unparsed document (heading wrong, or not UTF-8), not a clean one (C-2).
10. **Fragment test inside the wave's write scope** (the tool reads `../SOURCES.md` beside the lesson,
    so give the fragment its own corpus):
    ```
    D=.ufo/waves/round-65/w1/frag; mkdir -p "$D/lessons"
    cp corpus/SOURCES.md "$D/SOURCES.md"
    { printf '# frag\n\n## Gate\n\n'; cat .ufo/waves/round-65/rows/S750.txt; printf '\n\n## Status\n'; } > "$D/lessons/frag.md"
    python3 -B tools/check-gate-quotes.py "$D/lessons/frag.md"; echo "exit=$?"
    ```
    Without the `SOURCES.md` copy the truncated-grounds class is silent (C-5, measured).
11. **Do not cite a `tail -1`.** Quote the finding lines plus `exit=`; the summary line alone can be
    green on an error path.
12. **Re-run after the registry lands.** A green before S750-S775 exist in `corpus/SOURCES.md`
    certifies only over-cap/ellipsis/entity/doubled-locator — not Grounds truncation.

## E. Residual risk and verification gaps

- The `QUOTES` leg (accept-ca L172-178) cannot see: row presence (C-1), tier, date, `used-by`,
  registry-vs-Gate agreement beyond the prefix test, quote-vs-source truth (no network), or any
  fragment outside `corpus/lessons/round-65.md` (C-9). A green `QUOTES` leg is a formatting result
  only. Recommend the leg grow a row-presence assertion over S750-S775 before it is cited as
  coverage evidence (C-1), and switch to an anchored end-of-output match (C-8).
- I did not modify the tool, the counter, or any lane file, and I ran no git/jj write. The 30/16/2
  findings I report for `round-54.md`, `round-55.md`, `round-58.md` are the tool's live output on the
  lane's committed bytes at `17c32302`, not a claim about those rounds' acceptance at the time.
- No tool was installed or upgraded; no package manager transaction was run (pacman guard respected).
- Time-boxed: I did not attempt to forge a passing `accept-ca.py` end-to-end receipt against a fake
  root for legs other than `QUOTES`; the `--root` probe was used only to observe the `QUOTES` line,
  and the harness roots were deleted after each case.
- Fixtures use a synthetic URL (`https://e.test/a`) and synthetic teaches cells; every measured line
  in §B/§C is reproducible from §A plus the example text in the table, with the tool at sha256
  recorded in the header.

Report: .ufo/waves/round-65/w1/RevLessonFinal.md
