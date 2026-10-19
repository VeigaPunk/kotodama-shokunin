- Seat: C03 | verifier | claim C | date 2026-10-19 | baseline ce103bf

# C03 — independent verification of the two timekeeping audits and the README delta numbers

Mission (verbatim, `reports/round-36/targets.json` → `seats[id=C03].mission`):
*"Verify both audits + the delta numbers with your own commands."* Claim C
(`reports/round-36/claims.json:22-27`): land the routed timekeeping spare
(`reports/round-35/cov/C04-timekeeping-spare.md`), one new culture-material entry
+ README reconciliation; before `CM 24 / total 211`, after `CM 25 / total 212`,
sweep-green 212/212.

This seat writes **only** this fragment. No corpus byte, no `tools/**` byte, no
filed round byte is touched, and `reports/round-36/run-validation.py` was **not**
executed in-tree (F-C13-1); the only round-35 reconstruction ran in a `git
archive` copy under `.scratch/c03/`.

**Dependency status at write time (2026-10-19, single 32-seat devin batch).**
The two audits this seat is charged with verifying **do not exist**:
`reports/round-36/cov/C01-audit.md` and `reports/round-36/cov/C02-audit-delta.md`
are absent — the directory `reports/round-36/cov/` did not exist at all before
this file created it (`ls reports/round-36/` → `claims.json`, `targets.json`,
`telemetry/`; §7 control 1). `reports/round-36/run-validation.py` is likewise
absent. Their verification is therefore recorded **could-not-evaluate** (§6) with
the exact commands that must be re-run once they land. Everything that *is*
measurable from the delivered tree — the spare's integrity, the live count
surfaces, the delta numbers C02 owes, and the r35 runbook's own readings — is
verified independently below.

## 1. Method and the readings this verification stands on

Every reading was taken by this seat with its own commands, from the lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, at
`git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8` (`ce103bf`),
`git status --porcelain` → only `?? reports/round-36/` (the live tree is clean
against the baseline; no filed byte is dirty).

| surface | command | reading |
|---|---|---|
| partition census | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` | `21 / 23 / 24 / 29 / 20 / 94` = **211** |
| lane inventory | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 211` |
| index instrument | `python3 -B reports/round-28/readme/sweep.py` | `rows 211 files 211`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_line 211 totals_ok True`, `footer_ok True`, **exit 0** |
| index instrument controls | `python3 -B reports/round-28/readme/sweep.py --selftest` | `selftest: 12/12 checks passed` |
| README row count | `grep -c '^- \`[A-Za-z0-9._-]*\.md\`' corpus/README.md` | **211** |
| README digest | `sha256sum corpus/README.md` (via the instrument's own reading) | `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` |

**Claim C's `before` is the live state, exactly.** `CM 24 / total 211` holds
today, and no landed entry exists for the spare's domain:
`ls corpus/knowledge/culture-material/` → 24 files, none named
`timekeeping-instruments.md`; `grep -rln "timekeeping-instruments" corpus/` → no
hit. The `after` state (`CM 25 / total 212`) is therefore genuinely owed, not
already delivered — the delta has not been applied.

The README is already at revision 2.0 from the round-35 landing
(`corpus/README.md:3`), with headers `## linguistics/ (21)` `:136`,
`## myth-symbol/ (23)` `:160`, `## culture-material/ (24)` `:186`,
`## synthesis/ (29)` `:213`, `## verification/ (20)` `:245`,
`## civilizations/ (94)` `:268`, `Total knowledge entries: 211.` `:492`,
`Counts checked 2026-10-19 from the repo root:` `:494`,
`(total 211 files; directory totals 21/23/24/29/20/94).` `:496`.

## 2. The delta numbers, independently derived (C02's remit)

Re-derived from the live tree by this seat, not carried over from any draft:

| surface | now (pinned) | after +1 culture-material entry |
|---|---|---|
| `## culture-material/` header, `corpus/README.md:186` | `(24)` | `(25)` |
| `Total knowledge entries:`, `corpus/README.md:492` | `211.` | `212.` |
| footer vector, `corpus/README.md:496` | `21/23/24/29/20/94` | `21/23/25/29/20/94` |
| footer date, `corpus/README.md:494` | `2026-10-19` | re-measure at close |
| all other five headers and totals | unchanged | unchanged |
| row insertion point (filename order) | — | after `textile-technology.md` (`:206`), before `trade-economy-lexicon.md` (`:207`) |

The other five partition counts are untouched by this claim: `21/23/24/29/20/94`
→ `21/23/25/29/20/94` moves **exactly one** element and `211` → `212` moves the
total by exactly one. Confirmed by recomputation, not arithmetic on the drafts.

The row text the delta must use is the spare's own continuation-joined `- topic:`
head-block text — the equality `reports/round-28/readme/sweep.py:21,22,74-79,140`
measures — measured by this seat at **1 706 bytes** for the spare. It must be
emitted from the landed entry's bytes at integration time, never retyped
(`reports/round-35/cov/C04-entry-4.md:10`, the round-19/20 defect).

## 3. Audit of the spare draft (C01's remit)

### 3.1 Integrity — the r35 pin reproduces bit-exactly

The spare fences its entry body in a single 3-backtick `markdown` block
(`reports/round-35/cov/C04-timekeeping-spare.md`, 150 lines, fragment sha256
`258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2`). Extracting
the fence interior and adding the terminating newline gives:

| extraction | bytes | sha256[:16] |
|---|---|---|
| fence interior, no trailing newline | 40 233 | `9350fa107a6e37a2` |
| fence interior **+ trailing newline** | **40 234** | **`9805c0b854334ed3`** |
| r35 C13 audit's independent pin (`reports/round-35/cov/C13-audit-1-5.md:197`) | 40 234 | `9805c0b854334ed3` |

**AGREE.** The spare's bytes are unaltered since round 35, and the r35 auditor's
staged-entry pin is reproduced exactly by a second, independent extraction. This
is the load-bearing integrity reading for claim C: what will land is byte-for-byte
what was audited.

### 3.2 Structure — every contract leg present

Read against the r35 audit runbook's check list
(`reports/round-35/cov/C12-audit-runbook.md` §1, families 1a/1b/1c/2/3/4):

| leg | reading |
|---|---|
| frontmatter 1a (4/4) | `- sources:` ✔ `- verified-at:` ✔ `- recheck:` ✔ `- scope:` ✔ — all four present |
| frontmatter 1b (round-10 5-field set) | `topic` ✔ `sources` ✔ `verified-at` ✔ `recheck` ✔ `couples` ✔ — 5/5 |
| frontmatter 1c | no empty scalar field; `- verified-at:` carries ISO `2026-10-19` |
| resolving pointers | 26 distinct backticked repo paths under my ext-before-backtick rule; **0 unresolved**. Under the wider C02 rule (any backticked `corpus|tools|reports|examples/` token, `:line` suffix stripped) it is **29 distinct, 0 unresolved** — my first rule missed three `path:line`-suffixed tokens (`civilizations/benin.md`, `civilizations/persia-sasanian.md`, `myth-symbol/animal-symbolism.md`). The one non-resolving token under *both* rules is the literal glob `corpus/knowledge/*/*.md` used inside a quoted shell command, i.e. not a pointer (§3.5) |
| line citations | 8 distinct `path:line` / `path:line-range` citations under my rule; **0 missing files, 0 out-of-range**. This is a **lower bound** — the wider rule finds 20, and the r35 interop finding F12 (`C13-audit-1-5.md:130`) records the same undercount class |
| couples targets | 31 distinct `corpus/knowledge/**` paths with line anchors re-resolved; **all resolve**, none out of range |
| decision record | `## 9. Decision record — …` heading present; **12** rows `DR-TK-1 … DR-TK-12` |
| gap statement | `- gap filled:` present, with the measured absence sweep |
| urls | 0 external URLs (nothing is claimed resolved by network, consistent with `- verified-at:`) |
| `to-verify` marks | 33 — every unresolved precision figure is marked, none laundered into prose |

Structural verification of the spare: **PASS**, matching the r35 C13 audit's
`0 structural findings; 28 repo paths, 0 unresolved` (`C13-audit-1-5.md:200`) and
`17 path:line citations resolved, 0 unresolvable` (`:201`) on the readings I can
re-derive.

### 3.3 The absence sweep reproduces, at the baseline it was written against

The spare quotes a 26-term instrument-vocabulary loop. Re-run by this seat over
the **current** tree, `grep -ril -- "$kw" corpus/knowledge/*/*.md | wc -l`:
**0 files for all 26 terms** — water clock, clepsydra, clepsammia, gnomon,
sundial, escapement, pendulum, hourglass, incense clock, bell tower, canonical
hour, clockmaker, muwaqqit, wadokei, shichen, toki no kane, horologium, foliot,
quadrant, sandglass, candle clock, night clock, standard time, railway time,
vigilia — with **one exception**: `curfew` → **1** (see §4.3).

Re-run over the isolated r35 tree (`.scratch/c03/`, `git archive 4a7aede`):
**0 for all 26 terms, `curfew` included**. The spare's gap statement is therefore
accurate as written *at its own baseline*, and the `curfew` hit is a **new
occurrence** introduced by the round-35 landing.

### 3.4 Couples drift — the spare's sibling set is now one landing stale

The spare's `- couples:` list names 20 corpus siblings. Re-measured against the
live tree, **none of the ten round-35 entries appears in it** — not
`fire-fuel-light.md`, `furniture-interior-lexicon.md`,
`agrarian-field-system-lexicon.md`, `bathing-and-body-hygiene.md`,
`funerary-material-culture.md`, `writing-media-surface-economy.md`, nor the four
myth-symbol entries, and not `linguistics/register-lexicon-ceilings.md` (r28).
The spare was authored before those files existed, so the omission is expected,
not a defect in the draft — but it is a **material drift for landing**: the
closest new sibling by far is `culture-material/fire-fuel-light.md`, which
carries the `curfew`/`couvre-feu` etymology, a "light is bought by the hour"
craft claim (`fire-fuel-light.md:27,75`), a risk-word row (`:112`) and an
explicit "is the curfew a fire rule or a time rule" build step (`:131`) — i.e.
the fire-side half of exactly the institution the spare's §5–§6 own
(`C04-timekeeping-spare.md`, §5 institutions table, §6 ownership axis). Landing
the spare without a couples line to it leaves the two entries overlapping on the
curfew/bell institution with neither pointing at the other. This is a
landing-time reconciliation item for the integrator, and it is the concrete form
of the cross-claim question `review/R03-cross-review.md` is charged with.

## 4. Findings — two live defects in the delivered tree, and three stale readings

### F1 — LIVE DEFECT: the `culture-material/` rows are not in filename order

Measured by this seat with its own parse of `corpus/README.md`:

```
culture-material rows 188..212  count=24  internal_blank_lines=[211]  contiguous=False
```

Position 11–13 of the section, as filed:

| line | row (as filed) | ASCII position |
|---|---|---|
| `:198` | `furniture-interior-lexicon.md` | 12 |
| `:199` | `funerary-material-culture.md` | 13 |
| `:200` | `fire-fuel-light.md` | **11** |

`sorted(["fire-fuel-light.md","funerary-material-culture.md","furniture-interior-lexicon.md"])`
→ `fire-fuel-light.md`, `funerary-material-culture.md`,
`furniture-interior-lexicon.md`. The filed order is a **three-row rotation**, and
it is the only order defect in the file: all five other sections are
filename-sorted and internally contiguous (`linguistics` 138..158, `myth-symbol`
162..184, `synthesis` 215..243, `verification` 247..266, `civilizations`
270..363 — all `contiguous=True`).

**Provenance is pinned to the r35 landing.** In the isolated r35 baseline tree
(`git archive 4a7aede` → `.scratch/c03/`), all six sections are sorted
(`culture-material sorted=True`, rows 171..188, 18 rows, `contiguous=True`). In
the round-35 commit `ce103bf`, the six culture-material rows were appended in the
order `agrarian-field-system-lexicon`, `bathing-and-body-hygiene`,
`furniture-interior-lexicon`, `funerary-material-culture`, `fire-fuel-light`,
`writing-media-surface-economy` — i.e. `fire-fuel-light` was placed after
`furniture-interior-lexicon` instead of before it. The defect was introduced by
this landing, not inherited.

**Why no instrument caught it.** Neither index sweep has a row-order leg:
`reports/round-28/readme/sweep.py:120-150` compares row *sets* and row *topics*
(`missing`, `ghosts`, `mismatch`, `dup`, `drift`) and never the sequence;
`reports/round-27/readme/sweep.py:97-106` is the same. So the sweep is **exit 0
while carrying the defect**, and the round-35 audit fragments (`C13`, `C14`) and
review fragments (`R02`, `R09`) contain **no order finding** — `grep -n
"order\|sort"` over `C13-audit-1-5.md` and `R09-cross-review.md` returns nothing
about row placement. The r35 plan and author fragments *did* state the rule and
even named the correct neighbours
(`reports/round-35/cov/C06-entry-6.md:246`: "`fire-fuel-light.md` sorts after
`dress-through-eras.md` and before `garment-lexicon-crosslinguistic.md`" —
correct at the time, before the other five landed around it), and
`cov/C03-entry-3.md:290`, `cov/C05-entry-5.md:257`,
`scribe/S01-c-receipt.md:129` all assert "filename order". The rule was stated
and then not measured.

**Consequence for this round.** The delta C02 owes inserts a row into
`culture-material/` "in filename order" (`reports/round-36/claims.json:23,25`), and
the revision-2.0 prose it will extend asserts the same rule
(`corpus/README.md:9`). If the integrator inserts the spare row into the section
as it stands, the section will be sorted in its new element but still carry the
r35 rotation — and the new row's own correct position (`after
textile-technology.md`, `before trade-economy-lexicon.md`) is unaffected by it.
The two are independent edits; both should be applied, and the second should not
be silently absorbed into "the new row is placed in filename order".

### F2 — LIVE DEFECT: a stray blank line splits the `culture-material/` section

`corpus/README.md:211` is an empty line between `warrior-material-culture.md`
(`:210`) and `writing-media-surface-economy.md` (`:212`). Measured:
`internal_blank_lines=[211]`, and no other section has any internal blank line
between its first and last row (`[]` for all five others). The section is
therefore also non-contiguous, which is why the row-sort comparison must be done
on the row sequence and not on a line range. Same provenance: absent at the r35
baseline, where `culture-material` rows 171..188 are `contiguous=True`.

### F3 — `corpus/README.md:9` states a property the file does not have

Revision 2.0's landing note reads `their ten rows were added in filename order
with each entry's own \`- topic:\` text byte-equal` (`corpus/README.md:9`). The
second half is true — the sweep's `topic_mismatch 0` over all 211 rows confirms
it. The first half is **false for the culture-material section** (§F1). This is a
present-tense claim in a filed, frozen-by-practice revision block; it is not this
seat's byte to edit, and it should not be rewritten — the fix is the row order
itself (or a new dated note appended, per the file's own rule at `:497-500`).

### F4 — the spare's near-miss counts are now stale (deltas only, all direction-correct)

The spare's `- gap filled:` paragraph quotes near-miss counts measured at r35.
Re-measured by this seat on both trees:

| term | r35 baseline (isolated) | live | note |
|---|---|---|---|
| `bell` | 81 files | **87** | |
| `clock` in `culture-material/` | 6 files | **10** | |
| `chronometer` | 2 | **4** | |
| `astrolabe`, `"star clock"`, `obelisk`, `meridian`, `"time zone"` | 2, 2, 1, 1, 1 | unchanged | |
| `curfew` | **0** | **1** | see F5 |

Every moved count moved **upward**, i.e. toward more near-misses, which
strengthens rather than weakens the spare's "no entry covers the instrument"
argument — the new hits are neighbours, not coverage. The specific new
`curfew` occurrence is `culture-material/fire-fuel-light.md` (9 word-boundary
occurrences, of which `:82` is the `couvre-feu` etymology and `:153` a
`to-verify`-marked attribution), i.e. a landed r35 sibling, and the `bell`/`clock`
rises are the same ten entries. **The spare's quoted counts must be re-measured
before they are printed as current** — a quoted count is a dated reading, and the
round-28 lesson (`corpus/README.md:17-35`) is exactly a present-tense claim that
was never re-measured.

### F5 — the spare's own "28 instrument terms" vs the loop's 26

The spare's `- verified-at:` line calls the sweep "the absence sweep in `- gap
filled:` (all 28 instrument terms → 0 files corpus-wide)". Parsing the quoted
loop (`for kw in … vigilia; do …`) yields **26** terms — the same count the r35
auditor reached and filed as `S3` (`reports/round-35/cov/C13-audit-1-5.md`, the
sweep row: "26 terms in the command; the draft's `- verified-at:` line calls them
'28 instrument terms' — the sweep reproduces, the term count is off by two,
S3"). Reproduced independently by this seat: **the sweep reproduces exactly; the
count 28 is wrong and 26 is right.** Review-tier only (the sweep's *result* is
unaffected), and it is already filed at r35 — restated here so the landing does
not inherit an uncorrected number.

### F6 — control: the false "already landed" hypothesis

Checked and refuted, so that claim C's `before` is not accepted on faith: no
`timekeeping-instruments.md` exists in `corpus/knowledge/**` (24 CM files), no
`corpus/**` file mentions the slug, and `corpus/README.md` carries no row, header
or footer movement for it. Had the entry already landed, the live total would
read 212; it reads 211.

## 5. Negative controls

- **Instrument calibration.** `reports/round-28/readme/sweep.py --selftest` →
  `12/12`; the same instrument on the isolated r35 tree reads `201/201`,
  `totals_ok True`, `footer_ok True`, exit 0, and on the live tree reads
  `211/211`, exit 0 — so the instrument discriminates between the two trees and
  its green is not vacuous.
- **The order defect is real, not a parser artefact.** Read with `cat -A`
  (`corpus/README.md:198-200`): the three rows are plain `- \`<file>.md\` — …`
  lines with no marker, prefix or continuation that could reorder them; the
  inversion survives a byte-level read.
- **The digest reading is not a coincidence of extraction.** Two extractions
  differing by one trailing newline give two different digests; only the
  fence-interior-plus-newline form matches the r35 pin, and that is the form a
  `git apply` of the fence would produce.
- **Falsifier for F1.** If any `corpus/README.md` section other than
  `culture-material/` were also unsorted, or if the r35 baseline tree were also
  unsorted, F1's provenance claim would fail. Measured: all six live sections
  sorted except `culture-material`, and all six r35-baseline sections sorted.

## 6. Verdicts on the two audits

**Status update.** Both audits **landed while this seat was working** (they were
absent at first read; present by the time this section was written). They are
verified below on their readings, not on their prose.

| audit owed | status | evidence |
|---|---|---|
| `reports/round-36/cov/C01-audit.md` (spare audited against the r35 runbook, two independent reads) | **verified** — 469 lines; its §1 pins match mine exactly (fragment sha `258fb166…`, entry `40 234` B / `9805c0b854334ed3…`); its §0 rows 4–5 (sweep reproduces at `4a7aede`; near-misses reproduce at `4a7aede`) reproduce under my own commands (§3.3, §3.4); its F3 (`28` vs `26`) is independently re-derived (§F5); its F4 (drift disclosure) matches my §F4 | §3.1–§3.4, §F4, §F5 |
| `reports/round-36/cov/C02-audit-delta.md` (second audit + README delta draft, rev 2.1) | **verified, and its delta is reproducible byte-for-byte** — §6a | §6a |
| the spare itself (the artifact both audits cover) | **independently verified**: digest reproduces bit-exactly, structure PASS, gap statement reproduces at its baseline, couples set is one landing stale | §3.1–§3.4 |
| the live count surfaces | **independently verified**: `21/23/24/29/20/94` = 211 by three methods; sweep green; README row count 211 | §1 |
| the delta numbers | **independently verified**: `(24)→(25)`, `211→212`, `21/23/24/29/20/94 → 21/23/25/29/20/94`, one element moved | §2, §6a |

**Both audits independently found the same two README defects this seat found**
(C01 §3.6/§4b-adjacent context and C02 §3 F1/F2, S2 each) — three seats, three
separate parsers, one defect pair. C02's F1 is my §F2 (the stray blank line,
`corpus/README.md:211`); C02's F2 is my §F1 (the three-row inversion at `:198-200`);
C02's F3 is my §F1's instrument-blind-spot observation. **No disagreement between
the three seats on any graded value.** The only tier difference is recorded by C02
itself (`C02-audit-delta.md` §2.5): C01 files the stale currency as a defect
(F4, S3) where C02 reports it as a reading with a named cause — same measurement,
different tier, and that tier choice is the parent's.

Claim C's threshold is *"sweep green; audit clean; zero other count surfaces
drift"* (`reports/round-36/claims.json:27`). On the delivered revision:

- **sweep green — yes** (exit 0, 211/211), §1;
- **audit clean — yes, on both audits as now landed**: the spare clears the
  structural contract on two instruments built by two different seats (C01) and
  is re-read clean by a third (this seat, §3.2), with zero S1 findings. The
  review-tier items are false positives or already-filed notes (§F5, C02 §2.5);
- **zero other count surfaces drift — yes**, with two live **structural** defects
  that are not count drift and that no count instrument can see (§F1, §F2),
  independently confirmed by C02 as its F2/F1.

This seat therefore **certifies the two audits' readings and the delta's
numbers**, and records claim C as **verified on the readings** — while noting
that the claim's own `after_required` (`CM 25 / total 212`) is **not yet true on
the delivered tree** (it is still `24` / `211`), because the delta is drafted, not
applied. The landing itself is the integrator's act, not a verification result.

## 6a. Verification of C02's rev-2.1 delta — reproduced byte-for-byte

C02's §4 drafts a seven-edit delta (E1–E7) and carries a candidate README. This
seat **rebuilt the delta from the filed bytes itself** and compared, rather than
accepting the draft's digests.

| check | C02's reading | this seat's reading | verdict |
|---|---|---|---|
| pre-state `corpus/README.md` | sha256 `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` (its §1), 125 229 B | `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`, 125 229 B, `wc -l` 523 (last line unterminated) | **agree** |
| post-state candidate `.scratch/c02/readme-2.1.md` | `fc2e6d070cd7d123b4248e63b42b34a5fba9012c26e96a1918c622b5d2115316`, 127 680 B | **identical digest, identical size** | **agree** |
| new row bytes | `49e67b35d3df34bd568d18ba82299c78d59861735c2c4a7cb3f3e7121c7c0982`, 1 741 B | **identical digest** when hashed as C02 does (no trailing newline), 1 741 B | **agree** |
| the three re-sorted rows | digests `a761585a…` (1 261), `c757326c…` (2 914), `83c9c421…` (2 292) | **all three identical**, same sizes; and each is a **byte-exact copy** of the filed row — `identical_bytes=True` for all three, so E3 moves rows verbatim and rewrites none | **agree** |
| diff content | E1–E7 | my `difflib` opcode walk finds exactly **15 added / 6 removed** lines: the 9-line rev-2.1 block, `## culture-material/ (25)`, the two re-sorted rows, the new row, `Total knowledge entries: 212.`, the footer vector — and as removals the old header, the two moved rows, the blank line, `211.`, the old vector. **No undeclared edit exists.** | **agree** |
| acceptance reading | `rows 212 files 212`, 0 missing, 0 ghosts, 0 topic mismatch, `header_drift {}`, `totals_line 212 totals_ok True`, `footer_findings [] footer_ok True`, exit 0 | reproduced exactly with the filed instrument imported read-only against a staged 212-file tree | **agree** |
| negative control | candidate vs **live** tree → `orphan_rows ['culture-material/timekeeping-instruments.md']`, `header_drift {'culture-material': {'declared': 25, 'files': 24}}`, `totals_ok False`, `FOOTER_TOTAL` + `FOOTER_DIR_TOTALS`, exit 1 | reproduced **identically**, including both footer classes | **agree** |

Two details worth recording, because they are the kind that silently rot:

- **C02's post-state line count is `532`, not `533`.** It reports "533 lines" and
  a pre-state of "524 lines"; both are one more than the byte count implies
  (`wc -l` 523 → 532) because the file's final line has no terminating newline and
  `wc -l` counts newlines. C02's line *numbers* in its §4.2 map are consistent with
  its own convention and its diff hunks are correct; only the two stated totals
  carry the off-by-one. Harmless for the delta, worth naming so a later reader
  does not re-derive a different number and think the delta changed.
- **C02's `- gap filled:` figure "201 files at HEAD 4a7aede"** is consistent with
  §3.3's isolated-tree census (`21/19/18/29/20/94` = 201 at `4a7aede`) and with
  C01's §3.6.

**Net verdict on C02's delta: REPRODUCED, all seven edits, both the acceptance
and the negative control.** It is correct as drafted, it repairs both README
defects this seat independently found (§F1, §F2), and it is the integrator's to
apply. This seat wrote no corpus byte.

## 6b. Write-scope attestation, and a concurrent in-tree runner observed

This seat wrote exactly one path: `reports/round-36/cov/C03-verify.md` (the
`out` in `reports/round-36/targets.json` → `seats[id=C03].out`). Every other
command in this fragment is read-only; the only reconstruction of a filed round
ran on a `git archive` copy under `.scratch/c03/`, and no
`reports/round-*/run-validation.py` was executed by this seat.

**Observed, not performed by this seat.** During the final citation sweep,
`git status --porcelain` reported `M reports/round-35/validation.json` — a
**filed** round-35 byte, modified at `2026-10-19 06:29:42 -03:00`, while this
seat's HEAD readings had been clean (`?? reports/round-36/` only) a few minutes
earlier. Evidence captured at the time:

| reading | value |
|---|---|
| HEAD (`git show HEAD:reports/round-35/validation.json`) | sha256 `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`; `measured_at_utc` `2026-10-19T06:19:14.685566-03:00` (`:218`); `X1-X3.measurement` `{"manifest": "pending-by-construction: …"}` (`:180`) |
| working tree at `06:29:42` | sha256 `8cd9d98ef9931853c87f2d0a92615a7128c5ac04e8585ea5043963af6c202010`; `measured_at_utc` `2026-10-19T06:29:42.347669-03:00`; `X1-X3.measurement` `{}` |
| working tree at `06:29:59`, then `06:30:12` | mtime `06:29:59.402224991`, size 7 820; by `06:30:12` `git status` reads clean again and the digest is back to HEAD's `328e97b3…` — the modified state was transient and has reverted |

The shape is consistent with an in-tree execution of
`reports/round-35/run-validation.py`: that runner computes
`measured_at_utc` from `datetime.datetime.now()` on every run
(`reports/round-35/run-validation.py:80`, emitted at `:413`) and rewrites
`{ROUND}/validation.json` (`:502-504`), and the two observed deltas are exactly a
timestamp bump plus a measurement field the runner renders. This seat **did not**
run it — the changed field is on a different leg (`X1-X3`, a `D`-claim item) and
no command of mine writes that path. Flagging it because the round's absolute
rule is that no `reports/round-*/run-validation.py` may be executed in-tree
(F-C13-1), and an in-tree execution by any other seat is the same violation with
the same consequence for filed bytes.

**A second instance, on a different round.** `git status --porcelain` later
reported `M reports/round-34/validation.json`; `git diff --stat` showed it
modified and `git status --porcelain reports/round-34/` was clean again four
seconds later, with `sha256sum reports/round-34/validation.json` equal to
`git show HEAD:reports/round-34/validation.json` (`ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`
both sides). C01 independently observed the same round-34 file transiently
flipping to `acceptance: false` during its run (`C01-audit.md` §4b, at
`06:28:02`, reverted by `06:28:15`) and recorded it in the same way. Two rounds,
two seats, the same transient-in-tree-runner signature — which is a **process
finding**, not a filed-byte defect: no round-34 or round-35 filed byte stands
edited, and the committed verdicts are what the tree holds.

**Stability of this fragment's readings under that writer.** The concurrent
mutation did not touch any surface this verification stands on: re-measured at
`06:30:12`, the partition census is still `21/23/24/29/20/94`, the sweep is still
exit 0 / 211-211, and `corpus/README.md` is still
`51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` — identical
to the digest in §1. The live tree was not quiescent at write time, which is
worth recording for the integrator: any further reading filed this round should
name its own measurement instant, as this one does.

## Owed

- `reports/round-36/cov/C01-audit.md`, `reports/round-36/cov/C02-audit-delta.md`
  — **landed during this seat's run and both are verified** (§6, §6a). No longer
  owed. Their readings agree with this seat's on every graded value; the one tier
  difference (C01 files the stale currency as F4/S3, C02 reports it as a reading
  with a named cause) is the parent's to settle — it is a severity choice, not a
  measurement conflict.
- **Applying the rev-2.1 delta** — C02's seven edits are reproduced and correct
  (§6a), and they repair the two README defects. Applying them is the integrator's
  act; until then claim C's `after_required` (`CM 25 / total 212`) is not true on
  the delivered tree. Owner: integrator.
- `reports/round-36/run-validation.py` — absent; the claim's declared counting
  command (`reports/round-36/claims.json:26`) cannot be executed this round. Per
  the absolute rule it must not be run in-tree in any case; run it only in a
  `git archive` copy once it exists. Owner: integrator.
- F1/F2 (`culture-material/` row order + the stray blank line at
  `corpus/README.md:211`) — **not this seat's bytes to fix**. Owner: integrator,
  as part of the README reconciliation this claim already owes. Fixing them makes
  the section sorted and contiguous; leaving them means the section is sorted in
  its new element and still carries the r35 rotation.
- F4 — the spare's quoted near-miss counts (`bell` 81, `clock` 6 CM,
  `chronometer` 2) are stale against the live tree (87, 10, 4); they must be
  re-measured at landing, not carried. Owner: whoever applies the spare.
- F5 — the spare's `- verified-at:` says "28 instrument terms" where the quoted
  loop has 26; already filed as `S3` at r35
  (`reports/round-35/cov/C13-audit-1-5.md`). Owner: integrator, at landing.
- §3.4 — the spare carries no `- couples:` line to
  `culture-material/fire-fuel-light.md`, the closest new sibling (curfew /
  `couvre-feu` / "light bought by the hour"). Owner: integrator / R03.

## Citations

- `reports/round-36/targets.json` — `seats[id=C03]` mission and `out`; `shared_rules`
  (write only the out path; never edit filed bytes; never run `run-validation.py`
  in-tree). Seat table read in full (32 seats).
- `reports/round-36/claims.json:1-27` — claim C (`:22-27`), its `before` `CM 24 /
  total 211`, `after` `CM 25 / total 212`, counting commands `:26`, thresholds
  `:27`, `non_goals` (end of file); baseline `ce103bf` (`:7`); `axes_in_play` (`:12`).
- `reports/round-36/telemetry/availability-attempt-1.json` — hyper 402, 32/32
  failed at launch, declared devin fallback (why this batch is devin-hosted).
- `reports/round-36/cov/C01-audit.md` (469 lines) — the first audit, verified in §6:
  its §1 pins (`258fb166…`; `40 234` B / `9805c0b854334ed3…`), its §0 rows 4–5
  (sweep and near-misses reproduce at `4a7aede`), its §3.3 26-term parse, its F3
  (`28` vs `26`), its F4 (drift), its §4b transient filed-byte event (the same
  class as this seat's §6b), and its §3.6 README arithmetic (which matches §2).
- `reports/round-36/cov/C02-audit-delta.md` (475 lines) — the second audit and the
  delta, reproduced in §6a: its §1 pins, its §2.2 pointer rule (49 raw tokens → 30
  distinct → 28 resolve, which corrected my narrower regex), its §2.3–§2.4
  authoring-pin readings, its §3 F1/F2/F3 (the same two README defects this seat
  found), its §4 E1–E7 with the E3/E4 row digests and the candidate digest
  `fc2e6d070cd7d123b4248e63b42b34a5fba9012c26e96a1918c622b5d2115316`, and its
  §4.4 acceptance + negative control.
- `reports/round-35/cov/C04-timekeeping-spare.md` — the spare; fragment sha256
  `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2`, 150 lines;
  fence interior + newline 40 234 bytes / sha256 `9805c0b854334ed3…`; row text
  1 706 bytes; 26-term loop; 33 `to-verify`; 12 DR-TK rows; 0 URLs.
- `reports/round-35/cov/C13-audit-1-5.md:197-203` — the r35 audit's staged-entry
  pin (`9805c0b854334ed3`, 40 234 bytes) reproduced in §3.1; `I-C12`/`I-C13`
  readings `:199-201`; the "28 vs 26" `S3` sweep row `:203`; the `hour` 8/12
  word-boundary note `:205`.
- `reports/round-35/cov/C12-audit-runbook.md` §1 — the per-entry check-list
  families (1a/1b/1c/2/3/4) used as the structural contract in §3.2.
- `reports/round-35/cov/C06-entry-6.md:246`, `cov/C03-entry-3.md:290`,
  `cov/C05-entry-5.md:257`, `scribe/S01-c-receipt.md:129` — the r35 fragments
  that state the filename-order rule (and C06's correct neighbour pair).
- `reports/round-35/cov/C04-entry-4.md:6,7,10,162` — the spare's own README-row
  instruction (byte-equal, never retyped) and the plan/draft slug drift.
- `reports/round-28/readme/sweep.py:21,22,74-79,120-150,398-401` — the row/topic
  equality contract and the *absence* of any row-order leg (F1); `--selftest`
  12/12. `reports/round-27/readme/sweep.py:97-106` — the same set-comparison
  shape.
- `corpus/README.md:3,9,136,160,186,188-212,211,213,245,268,492,494,496,497-500`
  — the live count surfaces, the revision-2.0 filename-order claim (`:9`), the
  `culture-material` row block including the inversion (`:198-200`) and the stray
  blank line (`:211`), and the append-don't-rewrite rule (`:497-500`).
  Digest `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`.
- `corpus/knowledge/culture-material/fire-fuel-light.md:3,4,20,27,75,82,112,131,153,171`
  — the closest new sibling: curfew/`couvre-feu`, "light is bought by the hour",
  the risk-word row, the fire-rule-or-time-rule build step.
- `git show ce103bf -- corpus/README.md` — the r35 landing's row additions, in
  the order that produced F1 (`fire-fuel-light` added after
  `furniture-interior-lexicon`).
- Commands run (all from the lane root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`, HEAD `ce103bf` unless stated):
  - `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`;
    `git status --porcelain` → `?? reports/round-36/` only
  - `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21 23 24 29 20 94
  - `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 211`
  - `python3 -B reports/round-28/readme/sweep.py` → 211/211, all legs green, exit 0
  - `python3 -B reports/round-28/readme/sweep.py --selftest` → 12/12
  - `grep -c '^- \`[A-Za-z0-9._-]*\.md\`' corpus/README.md` → 211
  - own README parse (section headers, row sequence, contiguity) → the §1/§F1/§F2 tables
  - own spare parse (fence extraction, digests, frontmatter legs, pointer and
    citation resolution, couples re-resolution, term count) → §3.1–§3.4, §F5
  - 26-term absence sweep, live and on the isolated r35 tree → §3.3, §F4
  - `rm -rf .scratch/c03 && mkdir -p .scratch/c03 && git archive 4a7aede | tar -x -C .scratch/c03`
    → the isolated r35 tree; `sha256sum .scratch/c03/corpus/README.md` →
    `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`
    (matches the pin in `reports/round-35/cov/C11-readme-delta.md`), and the
    r28 sweep redirected to that tree → 201/201, exit 0
  - `grep -n "order\|sort" reports/round-35/cov/C13-audit-1-5.md
    reports/round-35/cov/C14-audit-6-10.md reports/round-35/review/R09-cross-review.md`
    → no row-order finding (why F1 survived round 35)
- Scratch (disposable, not evidence): `.scratch/c03/` — the r35 `git archive`
  copy, the redirected `sweep-r35.py`, the extracted spare body
  (`spare-entry.md`).
